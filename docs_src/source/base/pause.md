---
description: "Pause menu (Escape). Replaces s&box's own escape menu while a base-derived gamemode runs; 's&box menu' opens that"
---

# base: module `pause`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/pause/`

## `cl_pause.lua` (client)

Pause menu (Escape). Replaces s&box's own escape menu while a base-derived gamemode runs; "s&box menu" opens that
one (settings, report, quit game). Everything is a GM function:
```lua
function GM:PauseMenuButtons()                     -- add, remove or reorder buttons
    local list = self.BaseClass.PauseMenuButtons(self)
    table.insert(list, 2, { id = "stuck", label = "I'm stuck", click = function()
    net.SendToServer("mygm.stuck") end })
    return list
end
GM:PauseMenuTitle()
GM:PauseMenuSubtitle()   -- -- the header
GM:PauseCreate / PauseOpen / PauseClose / PauseToggle / PauseIsOpen   -- -- or replace the whole menu
```

A button is { id, label, click = function() end, danger = true (red), confirm = "text" (needs a second click), keepOpen = true (don't close the menu after the click) }.

Functions defined:

- `GM:PauseMenuTitle()`
- `GM:PauseMenuSubtitle()`
- `GM:PauseMenuButtons()`
- `GM:PauseCreate()`
- `GM:PauseIsOpen()`
- `GM:PauseRebuild()`
- `GM:PauseOpen()`
- `GM:PauseClose()`
- `GM:PauseToggle()`
