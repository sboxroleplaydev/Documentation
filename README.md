# Roleplay documentation

Documentation website of the Roleplay Lua framework for s&box, built with [MkDocs](https://www.mkdocs.org/) and the Material theme and published to GitHub Pages: <https://sboxroleplaydev.github.io/Documentation/>

## How it works

The pages are **generated from the game project**, not written here:

| Page group | Source (in the game project) |
|---|---|
| Lua API (one page per `##` heading, grouped by `GROUPS` in the script), function index | `Docs/LUA_API.md` |
| Guides | `Docs/SERVER_OWNERS.md`, `Docs/DEDICATED_SERVER.md` |
| Tool gun modes, permissions, commands, limits, gamemode modules | `Assets/lua/**` (header comments, `TOOL.*`, `permissions.Register`, `concommand.Add`, `chat.AddCommand`, `limits.Register`) |
| Engine API | the `///` comment at the top of each `Code/Framework/Scripting/Api/Lua*.cs` |

`build_docs.py` reads those files and writes `docs_src/` (Markdown), `mkdocs.yml` and `overrides/partials/header.html`. These generated files **are committed**, so GitHub Actions can build the site without the game project.

## Update the documentation

```powershell
pip install -r requirements.txt
python build_docs.py --no-build   # regenerate docs_src/, mkdocs.yml, overrides/partials/
python build_docs.py --serve      # preview on http://127.0.0.1:8000 (a second `--no-build` run refreshes it live)
python build_docs.py              # full local build into site/
```

Then commit and push to `main`. When the API changes: edit the source (the header comment of the Lua module or C# file, or `LUA_API.md`), run the script, commit the result. Never edit `docs_src/` by hand, it is overwritten.

## Publishing

`.github/workflows/docs.yml` builds the site (`mkdocs build --strict`) and deploys it to GitHub Pages on every push to `main` (or manually under Actions > Deploy documentation > Run workflow).

One-time setup: repository **Settings > Pages > Build and deployment > Source: GitHub Actions**.

Settings in `build_docs.py`: `GAME_URL`, `DISCORD_URL`, `SITE_URL` (used for canonical links and `sitemap.xml`; change it if the site moves to a custom domain), `KEYWORDS`.

The Python packages are pinned in `requirements.txt`; `overrides/partials/header.html` is a copy of Material's header template, so update the pinned `mkdocs-material` version and regenerate together.
