---
description: "Help screen (ShowHelp, H by default): every keybind with its key - rebindable ones can be changed by clicking"
---

# base: module `help`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/help/`

## `cl_help.lua` (client)

Help screen (ShowHelp, H by default): every keybind with its key - rebindable ones can be changed by clicking
"Change" and pressing a key - plus sections a gamemode adds:
```lua
function GM:HelpSections() return { { title = "Commands", lines = { "/job <name> - change job", ... } } } end
```

Functions defined:

- `GM:HelpSections()`
- `GM:HelpCreate()`
- `GM:HelpIsOpen()`
- `GM:HelpToggle()`
- `GM:HelpClose()`
- `GM:HelpRefresh()`
