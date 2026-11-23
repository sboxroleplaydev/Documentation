---
description: "1. lua/framework/sh, then sv or cl, alphabetically."
---

# Realms and files

| Prefix | Runs in | Notes |
|---|---|---|
| `sh_` | server **and** client | Each side runs its own copy, in its own Lua state. Safe to distribute. |
| `sv_` | server only | Never sent to clients, and the client loader refuses it. |
| `cl_` | client only | Sent to joining clients and verified by SHA-256. |

Load order:

1. `lua/framework/sh_*`, then `sv_*` or `cl_*`, alphabetically.
2. For each gamemode in dependency order: `#!lua entry.shared`, then `#!lua entry.server` or `#!lua entry.client`.
3. Addons that are on and made for this gamemode, dependencies first, otherwise A–Z (see "Addons").
4. Hooks `AddonsLoaded`, then `Initialize`.

Globals: `SERVER`, `CLIENT`, `REALM`, `GM`/`GAMEMODE`, `FRAMEWORK_VERSION`, `LUA_API_VERSION`.

