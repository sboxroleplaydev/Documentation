---
description: "LUAAPIVERSION (currently 1) is the version of everything in this document. Every gamemode.json and"
---

# API versions and migration

`LUA_API_VERSION` (currently **1**) is the version of everything in this document. Every `#!lua gamemode.json` and
`#!lua addon.json` declares the version it was written for in `"apiVersion"`, and the loader **refuses** a mismatch with a
clear message (`'apiVersion' 2 is not supported (this framework provides Lua API v1)`), instead of letting old code
fail somewhere at runtime.

**What changes the version.** Only breaking changes: a function or hook removed or renamed, changed arguments or
return values, changed realm rules or file conventions. **New** functions, hooks, libraries and optional manifest fields
(addons, `content`, `clothing`, `draw`/`cam`, `concommand`, …) do **not** bump it, so v1 code
keeps loading.

**When it is bumped,** the framework's release notes list each break with its replacement here, under a heading
"v1 → v2", in this form:

| Old (v1) | New (v2) | What to do |
|---|---|---|
| *(example)* `#!lua hud.SetLine(id, text)` | `ui` panels | replace the call; behaviour is otherwise the same |

Migrating a gamemode or addon then means:

1. Read the "vN → vN+1" table and search your Lua for each old name.
2. Change the calls, then set `"apiVersion"` to the new number in gamemode.json / addon.json.
3. Load it (`rp_lua_reload`, or with `DevMode` just save) and check `rp_addons` / the console for errors.
4. Dependent addons (`dependencies`) must be migrated too; the loader blocks them until then.

**Framework protocol version** (`Protocol` in `rp_status`, currently v4) is separate: it guards the network handshake.
Servers and players only need the same game version; it never requires changes to your Lua. v4 added addon files
to the content download.

There have been no breaking changes so far: everything written for API v1 runs unchanged.
