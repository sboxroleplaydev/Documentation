---
description: "An addon is a folder lua/addons/<id>/ (server owners: roleplay/lua/addons/<id>/ in the data folder) that runs on top"
---

# Addons

An addon is a folder `lua/addons/<id>/` (server owners: `roleplay/lua/addons/<id>/` in the data folder) that runs on top
of the gamemode. It uses exactly the same API as gamemode code.

```json
{ "id": "roll", "title": "Dice Roll", "version": "1.0.0", "apiVersion": 1,
  "author": "you", "description": "…",
  "gamemodes": [ "base" ],
  "dependencies": { "otheraddon": "^1.0.0" },
  "entry": { "shared": "sh_init.lua" },
  "packages": [], "collections": [] }
```

| Field | Meaning |
|---|---|
| `id` | a-z, 0-9, `_`; must equal the folder name. Folders starting with `_` are templates and never load |
| `version`, `apiVersion` | semver; `apiVersion` must match `LUA_API_VERSION` (see "API versions") |
| `gamemodes` | optional: only with these gamemodes **or gamemodes deriving from them** (`"base"` = all base-derived ones) |
| `dependencies` | optional: other addons → version rule: `"*"`/`""` any, `"1.2.0"`/`"=1.2.0"`, `">=1.2.0"`, `">1.2.0"`, `"<=2.0.0"`, `"<2.0.0"`, `"^1.2.0"` (≥1.2.0 <2.0.0), `"~1.2.0"` (≥1.2.0 <1.3.0); space-separated parts must all hold |
| `entry` | optional: exact `sh_`/`sv_`/`cl_` entry files. Without it, every `sh_*.lua`, then `sv_*`/`cl_*`, directly in the folder loads (A–Z) |
| `packages`, `collections` | cloud content, as in gamemode.json |

- **Paths:** while an addon loads, `#!lua include()` and `file.Find/Exists` are relative to the addon folder.
- **Status:** an addon is *loaded*, *disabled* (server config), *incompatible* (`gamemodes`), *blocked* (a dependency is
  missing, off or the wrong version) or *invalid* (bad addon.json or a dependency cycle). `rp_addons` shows each with
  the reason.
- **Errors:** an error while an addon loads is reported (`[server|darkrp+roll] Addon 'roll' failed to load…`) and the
  addon is skipped; addons depending on it are skipped too. Unlike a gamemode error this never ends the session. Hooks
  the addon added before the error stay registered.
- **Clients** receive the `#!lua addon.json`, `sh_` and `cl_` files of the addons the server runs (never `sv_`, never addons
  that are off) and load the same set in the same order.
- **Storage** is per gamemode, shared by its addons: prefix your keys (`#!lua storage.Set("roll/stats/" .. sid, …)`).
  Prefix net message names, hook ids and globals with the addon id, too.

`addons` library (both realms): `#!lua addons.GetAll()` → `{ { id, title, version, author, description, loaded, error }, … }`
in load order; `#!lua addons.Get(id)` → that table or nil; `#!lua addons.IsLoaded(id)`.

**Sample addon `roll`:** `/roll [max]` in chat or the J key (rebindable); the server rolls, sends a chat line and a
`#!lua roll.result` message that the client widget shows. Settings in `ROLL` (`#!lua sh_roll.lua`); hook
`#!lua PlayerRolled(ply, result, max)` → return false to cancel.

