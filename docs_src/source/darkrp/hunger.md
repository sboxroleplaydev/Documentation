---
description: "Hunger (NW var rp.hunger, 0-100): drops by 1 every HungerInterval seconds; at 0 the player starves slowly."
---

# darkrp: module `hunger`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/hunger/`

## `sv_hunger.lua` (server)

Hunger (NW var rp.hunger, 0-100): drops by 1 every HungerInterval seconds; at 0 the player starves slowly.
Food items (config/sh_items.lua, `food = n`) fill it up. Off with DarkRP.Config.HungerEnabled = false.

Functions defined:

- `DarkRP.StartHunger()`
