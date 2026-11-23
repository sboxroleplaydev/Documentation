#!/usr/bin/env python3
"""Builds the documentation website of the Lua framework (MkDocs + Material).

    pip install -r requirements.txt
    python build_docs.py            # generate docs_src/ and mkdocs.yml, then build the site into site/
    python build_docs.py --serve    # generate, then serve on http://127.0.0.1:8000
    python build_docs.py --no-build # (second terminal) regenerate while --serve runs: the open page reloads by itself
    python build_docs.py --no-build # only generate

Single sources of truth (edit THESE, never the generated files in docs_src/):
  Docs/LUA_API.md               hand-written API reference; every "## Heading" becomes a page (grouped by GROUPS below)
  Docs/*.md                     guides (server owners, dedicated server, decisions, implementation status)
  Assets/lua/**                 module/tool/permission/command/limit reference generated from the Lua source comments
  Code/Framework/Scripting/Api  engine API reference generated from the /// comments of the C# API files

When the API changes: edit the source (or LUA_API.md), run this script again.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent                      # project root
DOCS = ROOT / "Docs"
LUA = ROOT / "Assets" / "lua"
API_CS = ROOT / "Code" / "Framework" / "Scripting" / "Api"
OUT = HERE / "docs_src"
SITE_NAME = "Roleplay for s&box"
GAME_URL = "https://sbox.game/roleplaydev/roleplay"
DISCORD_URL = "https://discord.gg/cSsA7QruyK"
SITE_URL = "https://sboxroleplaydev.github.io/Documentation/"   # set to the address the site is published at (e.g. "https://docs.example.com/") for canonical links and sitemap.xml
SITE_DESCRIPTION = ("Documentation of Roleplay, the Garry's Mod-style Lua framework for s&box: sandboxed Lua 5.1 gamemodes, the sandbox "
                    "base gamemode (props, tool gun, physgun, weapons, Q menu), DarkRP and the full Lua API reference.")
KEYWORDS = ("s&box, sbox, roleplay, s&box roleplay, sandbox, s&box sandbox, lua, lua framework, s&box lua, lua api, gamemode, "
            "gmod, garry's mod, darkrp, darkrp s&box, tool gun, physgun, addons, scripting, server owners, dedicated server, documentation")

# LUA_API.md "## title" -> group. First matching prefix wins; unknown headings land in "Reference" automatically.
GROUPS = [
    ("Getting started", ["Realms and files", "Gamemodes and derivation", "Hooks called by the framework", "Addons", "Modules and files", "API versions"]),
    ("Core", ["Core libraries", "GMod compatibility", "Game / map", "Players", "Networked variables", "Entities", "Networking", "Storage", "Content", "Physics", "Models, materials"]),
    ("Client", ["Keyboard", "Keybinds", "Cookies", "UI (client", "3D2D", "View and mouse", "Beams, glows", "Player clothing"]),
    ("Base gamemode", ["Weapons", "Props, undo", "Tool gun", "Spawn menu", "UI components", "Base gamemode", "Sandbox"]),
    ("Compatibility", ["Differences from Garry"]),
]
GUIDES = [  # file, title
    ("SERVER_OWNERS.md", "Server owners"), ("DEDICATED_SERVER.md", "Dedicated server"),
]


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "page"


def describe(text):
    """First readable sentence of a page, for <meta name="description"> and social cards."""
    mt = re.search(r"(?m)^# (.+)$", text)
    head = mt.group(1).replace("`", "") if mt else ""
    for ln in text.split("\n"):
        t = ln.strip()
        if not t or t.startswith(("#", "```", "|", "<", "!!!", "???", "---", "Source:", "Folder:", ":::")):
            continue
        listed = t.startswith(("- ", "* ", "+ "))
        t = re.sub(r"`#!lua ([^`]*)`", r"\1", t)
        t = re.sub(r"[`*_]|\[([^\]]*)\]\([^)]*\)", lambda m: m.group(1) or "", t).lstrip("-+ ").strip()
        if len(t) > 25:
            if listed and head:
                t = f"{head}: {t}"
            return (t[:155].rsplit(" ", 1)[0] + "...") if len(t) > 158 else t
    return ""


def write(rel, text):
    if rel.endswith(".md") and rel != "index.md" and not text.startswith("---"):
        d = describe(text)
        if d:
            text = '---\ndescription: "' + d.replace('"', "'").replace("\\", "") + '"\n---\n\n' + text
    p = OUT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def read(p):
    return Path(p).read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")


def clean_title(title):
    """Short page title: no backticks, no parenthetical notes ("Players", not "Players (`ply`, server)")."""
    t = re.sub(r"\s*\([^)]*\)", "", title).replace("`", "")
    t = re.sub(r"\s+", " ", t).strip()
    return t or title.replace("`", "")


def realm_of(title):
    m = " ".join(re.findall(r"\(([^)]*)\)", title)).lower()
    if "both realms" in m or "shared" in m:
        return "Shared"
    if "client" in m and "server" not in m:
        return "Client"
    if "server" in m and "client" not in m:
        return "Server"
    return ""


def group_of(title):
    for g, prefixes in GROUPS:
        if any(title.startswith(p) for p in prefixes):
            return g
    return "Reference"


# ------------------------------------------------------------------ LUA_API.md -> pages
SIG = re.compile(r"^(?:[A-Za-z_][\w]*[.:])+[A-Za-z_]\w*\s*\(.*\)$|^[A-Za-z_]\w*\s*\(.*\)$")
LUAISH = re.compile(r"^(?:[A-Za-z_][\w]*[.:])+[A-Za-z_]\w*(?:\s*\(.*\))?$|^[A-Za-z_]\w*\s*\(.*\)$|^(?:local |function |return )")


LISTLINE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+")


def fix_lists(md):
    """The sources are written for GitHub-style Markdown: a list may follow a text line directly and nested items use two
    spaces. Python-Markdown needs a blank line before a list and four spaces per nesting level; without this the bullets
    run together into one wall of text."""
    out, fenced, prev = [], False, ""
    for line in md.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            out.append(line)
            prev = line
            continue
        if not fenced:
            m = LISTLINE.match(line)
            if m:
                if prev.strip() and not LISTLINE.match(prev) and not prev.startswith((" ", "\t")) and not prev.lstrip().startswith("|"):
                    out.append("")
                if m.group(1):
                    line = m.group(1) * 2 + line[len(m.group(1)):]
        out.append(line)
        prev = line
    return "\n".join(out)


def sentences(text):
    """Split at sentence ends (". " + capital or bold) that are outside `code` and (parentheses)."""
    parts, cur, depth, tick = [], "", 0, False
    i = 0
    while i < len(text):
        ch = text[i]
        cur += ch
        if ch == "`":
            tick = not tick
        elif not tick:
            if ch in "([{":
                depth += 1
            elif ch in ")]}":
                depth = max(0, depth - 1)
            elif ch == ";" and depth == 0 and i + 1 < len(text) and text[i + 1] == " ":
                parts.append(cur.strip())
                cur = ""
                i += 1
            elif ch in ".?!" and depth == 0 and i + 2 < len(text) and text[i + 1] == " " and (text[i + 2].isupper() or text[i + 2:i + 4] == "**") and not cur.rstrip().endswith(("e.g.", "i.e.", "etc.")):
                parts.append(cur.strip())
                cur = ""
                i += 1
        i += 1
    if cur.strip():
        parts.append(cur.strip())
    return parts


def break_long(md, limit=380, chunk=230):
    """A paragraph or list item longer than `limit` characters becomes several short paragraphs (sentences grouped to ~`chunk`)."""
    lines, out, fenced, i = md.split("\n"), [], False, 0
    while i < len(lines):
        line = lines[i]
        if line.lstrip().startswith("```"):
            fenced = not fenced
            out.append(line)
            i += 1
            continue
        if fenced or not line.strip() or line.lstrip().startswith(("#", "|", ">", "!!!", "???", "<")):
            out.append(line)
            i += 1
            continue
        # one logical block: this line plus its lazy continuation lines (not blank, not a new list item, not code/table)
        j = i + 1
        while j < len(lines) and lines[j].strip() and not LISTLINE.match(lines[j]) and not lines[j].lstrip().startswith(("```", "|", "#")):
            j += 1
        block = lines[i:j]
        m = LISTLINE.match(block[0])
        joined = " ".join(b.strip() for b in block)
        if len(joined) <= limit or m is None and joined.startswith(("---", "***", "___")):
            out.extend(block)
            i = j
            continue
        head = block[0][:m.end()] if m else ""
        body = joined[len(head.strip()) + (1 if m else 0):] if m else joined
        body = joined[m.end():].strip() if m else joined
        groups, cur = [], ""
        for sent in sentences(body):
            cur = (cur + " " + sent).strip()
            if len(cur) >= chunk:
                groups.append(cur)
                cur = ""
        if cur:
            groups.append(cur)
        if len(groups) < 2:
            out.extend(block)
            i = j
            continue
        pad = " " * (len(m.group(1)) + 4) if m else ""
        out.append((head if m else "") + groups[0])
        for g in groups[1:]:
            out.append("")
            out.append(pad + g)
        out.append("")   # a list item with extra paragraphs must be closed by a blank line before the next item
        i = j
    return "\n".join(out)


def highlight_inline(md):
    """`lib.Func(args)` -> `#!lua lib.Func(args)` (pymdownx.inlinehilite) outside fenced code blocks."""
    out, fenced = [], False
    for line in md.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced:
            def sub(m):
                c = m.group(1)
                return f"`#!lua {c}`" if LUAISH.match(c) and not c.startswith("#!") and "`" not in c else m.group(0)
            line = re.sub(r"(?<!`)`([^`\n]+)`(?!`)", sub, line)
        out.append(line)
    return "\n".join(out)


def api_pages():
    text = read(DOCS / "LUA_API.md")
    parts = re.split(r"(?m)^## ", text)
    intro, sections = parts[0], parts[1:]
    nav, index, summaries = {}, [], {}
    for sec in sections:
        title, _, body = sec.partition("\n")
        title = title.strip()
        body = re.sub(r"(?m)^### ", "## ", body)   # sub-headings become page sections
        g = group_of(title)
        full, title = title, clean_title(title)
        realm = realm_of(full)
        rel = f"api/{slug(g)}/{slug(title)}.md"
        first = next((l.strip(" -*") for l in body.split("\n") if l.strip() and not l.startswith(("#", "|", "`", " "))), "")
        summaries[rel] = re.sub(r"[`*_]", "", first)[:140]
        seen = set()
        for m in re.finditer(r"`([^`\n]+)`", body):
            c = m.group(1).strip()
            if SIG.match(c) and c not in seen and len(c) < 160:
                seen.add(c)
                index.append((c, title, rel))
        # class tables (SWEP.PrintName, TOOL.Name, GM.PropLimit ...): fields named in text or assigned in the examples
        for m in re.finditer(r"`#?!?(?:lua )?((?:SWEP|TOOL|GM|ENT|EFFECT|PLAYER|ITEM)[.:][A-Za-z_]\w*)`", body):
            c = m.group(1)
            if c not in seen:
                seen.add(c)
                index.append((c, title, rel))
        fenced = False
        for ln in body.split("\n"):
            if ln.lstrip().startswith("```"):
                fenced = not fenced
                continue
            if not fenced:
                continue
            for m in re.finditer(r"\b((?:SWEP|TOOL|GM|ENT|EFFECT|PLAYER|ITEM)\.[A-Za-z_]\w*)\s*=[^=]", ln):
                if m.group(1) not in seen:
                    seen.add(m.group(1))
                    index.append((m.group(1), title, rel))
            m = re.match(r"\s*function\s+([A-Za-z_]\w*[.:][A-Za-z_]\w*)\s*\(([^)]*)\)", ln)
            if m:
                sig = f"{m.group(1)}({m.group(2)})"
                if sig not in seen:
                    seen.add(sig)
                    index.append((sig, title, rel))
        badge = f'<span class="realm realm-{realm.lower()}">{realm}</span>\n' if realm else ""
        write(rel, f"# {title}\n{badge}" + highlight_inline(break_long(fix_lists(body))))
        nav.setdefault(g, []).append((title, rel))
    return intro, nav, index, summaries


def api_overview(nav, summaries, index):
    out = ["# Lua API\n", "Pick a topic. Every page lists the functions with their arguments, realm and limits. "
           f"There are **{len(index)}** documented function signatures; search them all in the [function index](functions.md).\n"]
    for g, pages in nav.items():
        out.append(f"## {g}\n")
        out.append('<div class="grid cards" markdown>\n')
        for title, rel in pages:
            href = rel[len("api/"):]
            out.append(f"-   **[{title}]({href})**\n\n    {summaries.get(rel, '')}\n")
        out.append("</div>\n")
    write("api/index.md", "\n".join(out))
    # function index: grouped by library / object prefix
    groups = {}
    for sig, title, rel in index:
        m = re.match(r"([A-Za-z_]\w*)[.:]", sig)
        groups.setdefault(m.group(1) if m else "(globals)", []).append((sig, title, rel))
    lines = ["# Function index\n", "Every function and class-table field (`SWEP.*`, `TOOL.*`, `GM.*`) mentioned in the Lua API pages, grouped by library or object. "
             "Use the search box (top) to find one by name.\n"]
    lines.append("**Jump to:** " + " · ".join(f"[{k}](#{slug(k)})" for k in sorted(groups, key=str.lower)) + "\n")
    for k in sorted(groups, key=str.lower):
        lines.append(f"## {k}\n")
        lines.append("| Signature | Page |\n|---|---|")
        for sig, title, rel in sorted(groups[k]):
            lines.append(f"| `#!lua {sig.replace('|', chr(92) + '|')}` | [{title}]({rel[len('api/'):]}) |")
        lines.append("")
    write("api/functions.md", "\n".join(lines))


# ------------------------------------------------------------------ Lua source reference
def header_comment(path):
    """The leading block of `--` lines of a Lua file (without the dashes)."""
    out = []
    for line in read(path).split("\n"):
        if line.startswith("--"):
            out.append(re.sub(r"^--\s?", "", line))
        elif line.strip() == "" and not out:
            continue
        else:
            break
    return "\n".join(out).strip()


SPLIT = re.compile(r"(?<=[)\]}])[ \t]+(?=(?:[A-Za-z_][\w]*[.:])*[A-Za-z_][\w]*\()")
LABEL = re.compile(r"^([A-Z][\w /]*:)\s+(.*)$")


# a line of real Lua: an assignment, local/function/end/table fragments (not a signature with a description)
REALCODE = re.compile(r"^\s*(?:--|local\s|function\s|end\b|return\b|for\s|if\s|\}|[\w.\[\]\"']+\s*=[^=>]|[\w.]+\s*\{)")


def top_split(seg):
    """Split at ', ' outside (), [], {} and quotes."""
    parts, cur, depth, quote = [], "", 0, ""
    for i, ch in enumerate(seg):
        if quote:
            if ch == quote:
                quote = ""
        elif ch in "\"'":
            quote = ch
        elif ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth = max(0, depth - 1)
        elif ch in ",;" and depth == 0 and seg[i + 1:i + 2] == " ":
            parts.append(cur.strip())
            cur = ""
            continue
        cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts


NOTE = re.compile(r"^(.+?\S)\s+\(([^()]+)\)[,;.]?$")
HEAD = re.compile(r"^(.*\((?:server|client|both)[^()]*\))\s*:\s+(.+)$")


def expand_list(seg):
    """'a(x), b, c (server)' -> ['a(x)', 'b', 'c   -- server']; 'obj:M() (server): A, B' -> ['-- obj:M() (server)', 'A', 'B']."""
    items = top_split(seg)
    if len(items) < 2 and not HEAD.match(seg) and not NOTE.match(seg):
        return [seg]
    out = []
    for item in items:
        h = HEAD.match(item)
        if h:
            out.append("-- " + h.group(1))
            item = h.group(2)
        m3 = re.match(r"^(.+?\))\s+\((server|client|both)\)\s+(\w.+)$", item)
        if m3:
            item = f"{m3.group(1)}   -- {m3.group(2)}: {m3.group(3)}"
        n = NOTE.match(item)
        if n and (" " in n.group(2) or re.match(r"(?i)(server|client|both)", n.group(2))):
            item = n.group(1) + "   -- " + n.group(2)
        out.append(item.rstrip(".,;"))
    return out


def split_signatures(line):
    """'SetModel(m) GetModel()  SetSkin(n)' -> one signature per line, 'f(x)   explanation' -> 'f(x)  -- explanation'.
    Real Lua lines (= { function) stay as written."""
    body = line.strip()
    if REALCODE.match(line):
        return [line.rstrip()]
    indent = line[:len(line) - len(line.lstrip())]
    call = re.compile(r"(?:[A-Za-z_]\w*[.:])*[A-Za-z_]\w*\(")
    out = []
    for seg in re.split(r"\s{2,}", body):
        m = LABEL.match(seg)
        if m:
            out.append(f"-- {m.group(1)[:-1]}")
            seg = m.group(2)
        if not call.match(seg) and out and not out[-1].lstrip().startswith("--"):
            out[-1] += "   -- " + seg
            continue
        for part in SPLIT.split(seg):
            if part.strip():
                out += [indent + x for x in expand_list(part.strip())]
    return out


def render_header(text):
    """Header comment -> markdown: prose stays text, signature lines become a highlighted Lua block, one signature per line."""
    import textwrap
    text = re.sub(r"\s*\(Phase [^)]*\)", "", text)   # project history does not belong in a reference
    text = "\n".join(ln for ln in text.split("\n") if not re.search(r"Phase \d", ln))
    text = re.sub(r",[ \t]*\n[ \t]*(?=\S)", ", ", text)   # a wrapped list is one list
    out, block = [], []
    CALL = re.compile(r"(?:[A-Za-z_]\w*[.:])*[A-Za-z_]\w*\(")

    def flush():
        if block:
            real = any(REALCODE.match(l) and not l.lstrip().startswith("--") for l in block)
            if real:
                lines = textwrap.dedent("\n".join(block)).strip("\n").split("\n")
            else:   # a list of signatures: flush left, loose text lines become comments
                lines = []
                for l in block:
                    l = l.strip()
                    lines.append(l if l.startswith("--") or "(" in l or re.match(r"^[\w.:/<>]+(\s+--.*)?$", l) else "-- " + l)
            out.append("```lua\n" + "\n".join(lines) + "\n```\n")
            block.clear()
    for line in text.split("\n"):
        lab = LABEL.match(line.strip())
        if re.match(r"^\s+\S", line) or re.match(r"^\s*(?:[A-Za-z_]\w*[.:])+\w*\s*[\(\[=]", line) or re.match(r"^\s*(?:local |function |hook\.|net\.|util\.)", line):
            block.extend(split_signatures(line))
        elif lab and CALL.match(lab.group(2)):
            block.extend(split_signatures(line.strip()))
        else:
            flush()
            out.append(line if line.strip() else "")
    flush()
    return "\n".join(out).strip() + "\n"


def funcs(path):
    r = []
    for m in re.finditer(r"(?m)^function\s+([A-Za-z_][\w.:]*)\s*\(([^)]*)\)", read(path)):
        if "." in m.group(1) or ":" in m.group(1):
            r.append(f"{m.group(1)}({m.group(2)})")
    return r


def lua_module_pages():
    nav = {}
    for gm in sorted(d for d in (LUA / "gamemodes").iterdir() if not d.name.startswith("_")):
        mdir = gm / "gamemode" / "modules"
        if not mdir.is_dir():
            continue
        entries = []
        for mod in sorted(p for p in mdir.iterdir() if p.is_dir() and not p.name.startswith("_")):
            body = [f"# {gm.name}: module `{mod.name}`\n", f"Folder: `Assets/lua/gamemodes/{gm.name}/gamemode/modules/{mod.name}/`\n"]
            for f in sorted(mod.glob("*.lua")):
                realm = {"sh_": "shared", "sv_": "server", "cl_": "client"}.get(f.name[:3], "?")
                hdr, fn = header_comment(f), funcs(f)
                body.append(f"## `{f.name}` ({realm})\n")
                body.append(render_header(hdr) if hdr else "_No header comment._\n")
                if fn:
                    body.append("Functions defined:\n\n" + "\n".join(f"- `{x}`" for x in fn) + "\n")
            rel = f"source/{gm.name}/{mod.name}.md"
            write(rel, "\n".join(body))
            entries.append((mod.name, rel))
        if entries:
            nav[gm.name] = entries
    fw = []
    for f in sorted((LUA / "framework").glob("*.lua")):
        hdr = header_comment(f)
        fn = funcs(f)
        write(f"source/framework/{f.stem}.md", f"# `framework/{f.name}`\n\n" + ((render_header(hdr) + "\n") if hdr else "")
              + ("Functions defined:\n\n" + "\n".join(f"- `{x}`" for x in fn) + "\n" if fn else ""))
        fw.append((f.name, f"source/framework/{f.stem}.md"))
    nav["framework"] = fw
    return nav


def table(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)]
    out += ["| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |" for r in rows]
    return "\n".join(out) + "\n"


def tools_page():
    rows = []
    for f in sorted((LUA / "gamemodes").glob("*/gamemode/tools/sh_*.lua")):
        t = read(f)

        def g(k):
            m = re.search(r"TOOL\." + k + r'\s*=\s*"([^"]*)"', t) or re.search(r'' + k.lower() + r'\s*=\s*"([^"]*)"', t)
            return m.group(1) if m else ""
        cv = re.search(r"(?:TOOL\.ClientConVar|convars)\s*=\s*\{(.*?)\}", t, re.S)
        keys = ", ".join(re.findall(r"(\w+)\s*=", cv.group(1))) if cv else ""
        m = re.search(r'tools\.Register\(\w+,\s*"([^"]+)"', t) or re.search(r'mode\s*=\s*"([^"]+)"', t)
        mode = m.group(1) if m else f.stem[3:]
        rows.append((g("Category") or ("Constraints" if "LengthTool" in t else ""), g("Name") or f.stem[3:], f"`{mode}`", g("Description"), keys, f.parent.parent.parent.name))
    rows.sort()
    return ("# Tool gun modes\n\nGenerated from `tools/sh_*.lua`. Mode = `rp gmod_toolmode <mode>`, permission `tool.<mode>`. "
            "Settings = the tool's `ClientConVar` keys.\n\n" + table(["Category", "Name", "Mode", "Description", "Settings", "Gamemode"], rows))


def permissions_page():
    rows = []
    for f in sorted(LUA.rglob("*.lua")):
        for m in re.finditer(r'permissions\.Register\(\s*"([^"]+)"\s*,\s*\{(.*?)\}\s*\)', read(f), re.S):
            def d(k, body=m.group(2)):
                mm = re.search(k + r'\s*=\s*"([^"]*)"', body)
                return mm.group(1) if mm else ""
            rows.append((d("category"), f"`{m.group(1)}`", d("default"), d("description")))
    rows = sorted(set(rows))
    return ("# Permissions\n\nEvery registered permission. Each tool also registers `tool.<mode>` (see Tool gun modes).\n\n"
            + table(["Category", "Permission", "Default group", "Description"], rows))


def commands_page():
    rows = []
    for f in sorted(LUA.rglob("*.lua")):
        t = read(f)
        rel = f.relative_to(LUA).as_posix()
        for m in re.finditer(r'concommand\.Add\(\s*"([^"]+)"', t):
            end = t.find("\nend", m.start())
            tail = t[max(end, m.start()):max(end, m.start()) + 300]
            d = re.search(r'end,\s*nil,\s*"([^"]+)"', tail) or re.search(r'end,\s*"([^"]+)"', tail)
            rows.append(("console", f"`rp {m.group(1)}`", d.group(1) if d else "", rel))
        for m in re.finditer(r'chat\.AddCommand\(\s*"([^"]+)"', t):
            end = t.find("\nend", m.start())
            tail = t[max(end, m.start()):max(end, m.start()) + 300]
            d = re.search(r'end,\s*"([^"]+)"', tail)
            rows.append(("chat", f"`/{m.group(1)}`", d.group(1) if d else "", rel))
    rows = sorted(set(rows))
    return "# Commands\n\nConsole commands run as `rp <command>`; chat commands start with `/`.\n\n" + table(["Kind", "Command", "Description", "Defined in"], rows)


def limits_page():
    t = read(LUA / "gamemodes/base/gamemode/modules/limits/sh_limits.lua")
    rows = [(f"`{m[0]}`", m[1], m[2], f"`{m[3]}`" if m[3] else "(constraints)") for m in
            re.findall(r'limits\.Register\("(\w+)",\s*(\d+),\s*"([^"]+)"(?:,\s*"(\w+)")?', t)]
    return ("# Limits\n\nPer-player tool gun limits (base gamemode). Override with `GM.Limits = { thrusters = 20 }` in the gamemode config; 0 = unlimited; "
            "permission `props.nolimit` ignores them.\n\n" + table(["Category", "Default", "Label", "Gadget kind"], rows))


def reference_pages():
    for rel, fn in (("source/tools.md", tools_page), ("source/permissions.md", permissions_page),
                    ("source/commands.md", commands_page), ("source/limits.md", limits_page)):
        write(rel, fn())


# ------------------------------------------------------------------ C# engine API
def xml_to_md(s):
    s = re.sub(r"</?(?:para|remarks)>", "\n", s)
    s = re.sub(r"<c>(.*?)</c>", r"`\1`", s, flags=re.S)
    s = re.sub(r'<see cref="([^"]+)"\s*/>', r"`\1`", s)
    s = re.sub(r"<[^>]+>", "", s)
    return s.replace("&lt;", "<").replace("&gt;", ">").replace("&amp;", "&")


def engine_pages():
    entries = []
    for f in sorted(API_CS.glob("Lua*.cs")):
        m = re.search(r"((?:^[ \t]*///.*\n)+)", read(f), re.M)
        if not m:
            continue
        txt = "\n".join(re.sub(r"^\s*///\s?", "", ln) for ln in m.group(1).split("\n"))
        txt = xml_to_md(re.sub(r"</?summary>", "", txt)).strip("\n")
        if len(txt) < 20:
            continue
        name = f.stem
        write(f"engine/{slug(name)}.md",
              f"# {name}\n\nSource: `Code/Framework/Scripting/Api/{f.name}`\n\n" + render_header(txt)
              + '\n??? info "How to read the signatures"\n    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. '
                'Lines starting with `--` label a group (for example `Player only`).\n')
        entries.append((name, f"engine/{slug(name)}.md"))
    return entries


# ------------------------------------------------------------------ guides, index, nav
def guides():
    entries = []
    for fn, title in GUIDES:
        p = DOCS / fn
        if p.exists():
            write(f"guides/{slug(title)}.md", break_long(fix_lists(read(p))))
            entries.append((title, f"guides/{slug(title)}.md"))
    return entries


def nav_yaml(nav):
    def item(title, rel):
        return '{ "%s": "%s" }' % (title.replace('"', "'"), rel)
    lines = ["nav:"]
    for k, v in nav:
        if isinstance(v, str):
            lines.append(f"  - {item(k, v)}")
        else:
            lines.append(f'  - "{k}":')
            for sub in v:
                if isinstance(sub[1], list):
                    lines.append(f'      - "{sub[0]}":')
                    lines += [f"          - {item(t, r)}" for t, r in sub[1]]
                else:
                    lines.append(f"      - {item(sub[0], sub[1])}")
    return "\n".join(lines) + "\n"


CONFIG = """site_name: "%s"
site_description: "%s"
site_author: "Roleplay"
%sdocs_dir: docs_src
site_dir: site
use_directory_urls: false
extra_css: [stylesheets/extra.css]
extra:
  generator: false
theme:
  name: material
  custom_dir: overrides
  font: { text: Inter, code: JetBrains Mono }
  icon: { logo: material/code-braces }
  features: [navigation.tabs, navigation.tabs.sticky, navigation.sections, navigation.top, search.suggest, search.highlight, search.share, content.code.copy, content.code.annotate, toc.follow]
  palette:
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: custom
      accent: cyan
      toggle: { icon: material/weather-sunny, name: Light mode }
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: custom
      accent: indigo
      toggle: { icon: material/weather-night, name: Dark mode }
markdown_extensions:
  - tables
  - admonition
  - attr_list
  - md_in_html
  - def_list
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight: { anchor_linenums: true, use_pygments: true, auto_title: false }
  - pymdownx.inlinehilite: { custom_inline: [] }
  - pymdownx.tabbed: { alternate_style: true }
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - toc: { permalink: true }
validation:
  links: { not_found: ignore, absolute_links: ignore, unrecognized_links: ignore }
  nav: { omitted_files: ignore }
"""


HEADER_LINKS = """
    <a href="%s" class="md-header__button md-icon" title="Play Roleplay on s&amp;box" aria-label="Play Roleplay on s&amp;box" target="_blank" rel="noopener">
      {%% include ".icons/material/gamepad-variant.svg" %%}
    </a>
    <a href="%s" class="md-header__button md-icon" title="Join the Discord" aria-label="Join the Discord" target="_blank" rel="noopener">
      {%% include ".icons/fontawesome/brands/discord.svg" %%}
    </a>
"""


def header_override():
    """overrides/partials/header.html = Material's own header + two icon links after the light/dark switch (stays valid across Material updates)."""
    import material
    src = (Path(material.__file__).parent / "templates" / "partials" / "header.html").read_text(encoding="utf-8")
    anchor = '{% include "partials/javascripts/palette.html" %}\n    {% endif %}'
    if anchor not in src:
        print("warning: Material's header template changed, header icons skipped")
        return
    out = HERE / "overrides" / "partials"
    out.mkdir(parents=True, exist_ok=True)
    (out / "header.html").write_text(src.replace(anchor, anchor + HEADER_LINKS % (GAME_URL, DISCORD_URL), 1), encoding="utf-8", newline="\n")


def generate():
    header_override()
    # Empty the folder instead of deleting it: a running `--serve` keeps a handle on docs_src (Windows would refuse).
    OUT.mkdir(parents=True, exist_ok=True)
    for child in OUT.iterdir():
        if child.is_dir():
            shutil.rmtree(child, ignore_errors=True)
        else:
            child.unlink(missing_ok=True)
    intro, api_nav, api_index, summaries = api_pages()
    api_overview(api_nav, summaries, api_index)
    src_nav = lua_module_pages()
    reference_pages()
    eng = engine_pages()
    gd = guides()
    write("stylesheets/extra.css", read(HERE / "extra.css"))
    mv = re.search(r'Version\s*=\s*"([^"]+)"', read(ROOT / "Code/Framework/Core/FrameworkInfo.cs"))
    version = mv.group(1) if mv else "?"
    counts = (len(api_index), sum(len(v) for v in api_nav.values()), len(src_nav.get("base", [])) + len(src_nav.get("darkrp", [])), len(eng))
    write("index.md", f"""---
hide:
  - navigation
  - toc
description: "{SITE_DESCRIPTION}"
---

<div class="hero" markdown>

# {SITE_NAME}

A Garry's Mod-style Lua framework for s&box: gamemodes in sandboxed **Lua 5.1**, a sandbox base gamemode and DarkRP on top of it.

Version {version} · Lua API v1

[Lua API :material-arrow-right:](api/index.md){{ .md-button .md-button--primary }}
[Function index](api/functions.md){{ .md-button }}
[Server owners](guides/server-owners.md){{ .md-button }}

[:material-gamepad-variant: Play on s&box]({GAME_URL}){{ .md-button }}
[:fontawesome-brands-discord: Join the Discord]({DISCORD_URL}){{ .md-button }}

</div>

<div class="grid cards" markdown>

-   :material-code-braces: **[Lua API](api/index.md)**

    {counts[1]} topics, {counts[0]} function signatures: realms, hooks, players, entities, net, UI, physics, weapons, tools.

-   :material-magnify: **[Function index](api/functions.md)**

    Every function by library on one page. Use the search box to jump to a name.

-   :material-toolbox: **[Tool gun modes](source/tools.md)**

    Every tool with category, mode name and its settings; plus [permissions](source/permissions.md), [commands](source/commands.md) and [limits](source/limits.md).

-   :material-package-variant: **[Gamemode modules](source/base/props.md)**

    {counts[2]} modules of the base and DarkRP gamemodes, straight from the Lua source comments.

-   :material-engine: **[Engine API (C#)](engine/luaplayers.md)**

    {counts[3]} libraries the host provides to Lua.

-   :material-server: **[Guides](guides/server-owners.md)**

    Running and configuring a server, dedicated hosting.

</div>
""")
    nav = [("Home", "index.md")]
    lua_api = [("Overview", "api/index.md"), ("Function index", "api/functions.md")]
    for g in [g for g, _ in GROUPS] + ["Reference"]:
        if g in api_nav:
            lua_api.append((g, api_nav[g]))
    nav.append(("Lua API", lua_api))
    ref = [("Tool gun modes", "source/tools.md"), ("Permissions", "source/permissions.md"), ("Commands", "source/commands.md"), ("Limits", "source/limits.md")]
    for gm, entries in src_nav.items():
        ref.append((f"Modules: {gm}", entries))
    nav.append(("Reference", ref))
    if eng:
        nav.append(("Engine API", eng))
    nav.append(("Guides", gd))
    cfg = CONFIG % (SITE_NAME, SITE_DESCRIPTION.replace('"', "'"), ('site_url: "%s"\n' % SITE_URL) if SITE_URL else "")
    (HERE / "mkdocs.yml").write_text(cfg + nav_yaml(nav), encoding="utf-8", newline="\n")
    write("robots.txt", "User-agent: *\nAllow: /\n" + (f"Sitemap: {SITE_URL.rstrip('/')}/sitemap.xml\n" if SITE_URL else ""))
    print(f"generated {sum(1 for _ in OUT.rglob('*.md'))} pages, version {version}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true")
    ap.add_argument("--no-build", action="store_true")
    a = ap.parse_args()
    generate()
    if a.no_build:
        return
    cmd = [sys.executable, "-m", "mkdocs", "serve" if a.serve else "build", "-f", str(HERE / "mkdocs.yml")]
    sys.exit(subprocess.call(cmd, cwd=HERE))


if __name__ == "__main__":
    main()
