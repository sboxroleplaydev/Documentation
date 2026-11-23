---
description: "DarkRP F4 menu (M): a sidebar with you (name, job, wallet, salary) and the categories - Commands, Jobs, Entities, Weapons, Ammo, Shop, Inventory, Admin -..."
---

# darkrp: module `menu`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/menu/`

## `cl_menu.lua` (client)

DarkRP F4 menu (M): a sidebar with you (name, job, wallet, salary) and the categories - Commands, Jobs, Entities, Weapons, Ammo, Shop, Inventory, Admin - like GMod DarkRP's F4 menu. Jobs: a grid by category with a detail column
and "Become"; shop categories: tiles with the model's icon, price and Buy.
Every button only sends a request; the server decides.

Functions defined:

- `GM:MenuTabs()`
- `GM:MenuCreate()`
- `GM:MenuIsOpen()`
- `GM:MenuToggle()`
- `GM:MenuOpen()`
- `GM:MenuClose()`
- `GM:MenuRefresh()`
- `DarkRP.CountJobClient(command)`
- `GM:MenuBuild_jobs(body)`
- `GM:MenuBuild_entities(body)`
- `GM:MenuBuild_weapons(body)`
- `GM:MenuBuild_ammo(body)`
- `GM:MenuBuild_shop(body)`
- `GM:MenuBuild_inventory(body)`
- `GM:MenuCommands()`
- `GM:MenuBuild_commands(body)`
- `GM:MenuBuild_admin(body)`
