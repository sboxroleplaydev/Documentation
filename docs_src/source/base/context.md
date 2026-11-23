---
description: "Context menu (client), GMod's C menu: hold C while looking at an object. It shows the properties of that object"
---

# base: module `context`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/context/`

## `cl_context.lua` (client)

Context menu (client), GMod's C menu: hold C while looking at an object. It shows the properties of that object
(properties.Add, sh_properties.lua) and the desktop icons of list.Get("DesktopWindows") along the top.
```lua
GM:ContextMenuShow() / ContextMenuHide() / ContextMenuIsOpen()   -- hooks ContextMenuOpen() -> false cancels, ContextMenuClose()
list.Set("DesktopWindows", id, { title = "My window", icon = "widgets", init = function(icon, window) end })
a click opens a window (ui.Window) whose body `init` fills: init(icon, window) with window.Body.
```

Functions defined:

- `GM:ContextMenuIsOpen()`
- `GM:ContextMenuShow()`
- `GM:ContextMenuHide()`

## `sh_properties.lua` (shared)

Entity properties (GMod's `properties` library): the actions in the context menu (hold C while looking at an object).
```lua
properties.Add("name", {
    MenuLabel = "Freeze" | function(self, ent) -> text,    Order = 100,    MenuIcon = "ac_unit" (Material Icons name), Filter = function(self, ent, ply) -> bool,    -- shown / allowed? (runs on both sides: the server checks again)
    Action = function(self, ent) ... end,          -- client, when clicked; default: self:Send(ent)
    Receive = function(self, ent, ply, data) ... end,   -- server, after Filter passed; data = what Send() added
})
self:Send(ent [, data])   -- (client, inside Action)   -- asks the server to run Receive (data: a small table, optional)
properties.Get(name)
properties.GetForEntity(ent, ply) -> sorted list
```

Base properties: remove, freeze (toggle), gravity (toggle). Hook CanProperty(ply, name, ent) -> false blocks one.

Functions defined:

- `properties.Add(name, def)`
- `properties.Get(name)`
- `properties.Allowed(def, ent, ply)`
- `properties.GetForEntity(ent, ply)`
- `properties.Label(def, ent)`

## `sv_properties.lua` (server)

Properties (server): the client asks, the server checks the filter again and runs Receive.
