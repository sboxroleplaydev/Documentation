---
description: "Laws board (top right), toggled with L (rebindable). Rebuilt only when the laws change."
---

# darkrp: module `laws`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/laws/`

## `cl_laws.lua` (client)

Laws board (top right), toggled with L (rebindable). Rebuilt only when the laws change.

Functions defined:

- `GM:LawsCreate()`
- `GM:LawsToggle()`
- `GM:LawsThink()`

## `sv_laws.lua` (server)

The city's laws, set by the mayor (job.mayor = true): /addlaw <text>, /removelaw <n>, /resetlaws.
Shared with everyone through the global NW var "rp.laws" (one law per line); shown by cl_laws.lua.
