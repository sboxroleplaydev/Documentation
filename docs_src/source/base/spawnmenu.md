---
description: "Spawn menu (client), laid out like Garry's Mod's Q menu: hold Q to open, let go to close (once you type in a search box it"
---

# base: module `spawnmenu`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/spawnmenu/`

## `cl_spawnmenu.lua` (client)

Spawn menu (client), laid out like Garry's Mod's Q menu: hold Q to open, let go to close (once you type in a search box it
stays open until Q or Escape).
```lua
Left:   -- creation tabs (Props, Entities, Weapons, NPCs, Vehicles ...), a category tree and the icon grid, with a search box.
-- Right
tool tabs (Tools, Utilities ...): a list by category on top
-- the selected entry's control panel below
```


Extending it (GMod's names; client realm):
```lua
spawnmenu.AddCreationTab(name, function(parent, search) ... end, icon, order, tooltip [, visible])   -- a tab on the left
    `parent` is the tab's body (a ui panel); build into it. icon = a Material Icons name ("category"). visible() -> false hides it.
spawnmenu.GetCreationTabs() -> { [name] = { Name, Id, Function, Icon, Order, Tooltip } }
spawnmenu.AddToolTab(id, name, icon)   -- a tab on the right (base: "Main" = Tools, "Utilities")
spawnmenu.AddToolCategory(tab, id, name)
spawnmenu.AddToolMenuOption(tab, category, class, name, command, config, function(panel) ... end [, extra])
    an entry in a tool tab. `panel` is a control panel: Help
    Label
    Button
    Slider
    CheckBox
    ComboBox
    Choices
    Color
    Key
    TextField
    Materials
    Divider
    and .Root (a ui panel for your own controls). When `class` is a registered tool mode
    (or command is "gmod_tool <mode>") the entry selects that tool
    its settings are the TOOL's ClientConVars
    Without a tool
    panel:Slider(label, key, ...) etc. store `key` in your cookies ("spawnmenu.<key>"; read with panel:Get(key), defaults in panel.Defaults)
spawnmenu.GetToolMenu(tab) -> { { Name, Text, Items = { { ClassName, Text, Command, CPanelFunction } } }, ... }
spawnmenu.AddContentType(name, function(container, obj) return icon end)   -- how an entry of a spawnlist is shown
    built in: "model" { model, nicename }
    "entity" { spawnname, nicename, material }
    "weapon"
    "npc"
    "vehicle"
    "header" { text }
spawnmenu.AddPropCategory(name, entries) (sh_spawnmenu.lua): entries are "model" strings
{ "model", "name" }
{ header = "..." }
    or { type = "<content type>", ... }.
spawnmenu.ActivateTool(mode)
spawnmenu.GetActiveTab() / SetActiveTab(name)
spawnmenu.OpenTab(name)
```

Hooks: AddToolMenuTabs, AddToolMenuCategories, PopulateToolMenu (fill the tool tabs), SpawnMenuOpen() -> false keeps it closed, OnSpawnMenuOpen(), OnSpawnMenuClose(), SpawnlistContentChanged. Registries: list.Get("SpawnableEntities" | "Weapon" | "NPC" | "Vehicles").
GM functions: SpawnMenuShow/Hide/IsOpen/Refresh/RefreshTools; GM:SpawnMenuTabs() -> list of { id, label, build(self, body, search) }
(the default builds it from spawnmenu.GetCreationTabs(); override it, or return a changed list, to keep the older way of
adding tabs working).

Functions defined:

- `spawnmenu.AddCreationTab(name, func, icon, order, tooltip, visible)`
- `spawnmenu.GetCreationTabs()`
- `spawnmenu.GetActiveTab()`
- `spawnmenu.SetActiveTab(name)`
- `spawnmenu.OpenTab(name)`
- `spawnmenu.AddToolTab(id, name, icon)`
- `spawnmenu.AddToolCategory(tab, id, name)`
- `spawnmenu.AddToolMenuOption(tab, category, class, name, command, config, cpanel, extra)`
- `spawnmenu.GetToolMenu(tab)`
- `spawnmenu.AddContentType(name, fn)`
- `spawnmenu.CreateContentIcon(typ, container, obj)`
- `spawnmenu.ActivateTool(mode)`
- `spawnmenu.ModelMenu(model, extraLabel, extra)`
- `GM:SpawnMenuSplit(body, title)`
- `GM:SpawnMenuBuildCloud(scroll, search)`
- `GM:SpawnMenuTabs()`
- `GM:AddToolMenuTabs()`
- `GM:AddToolMenuCategories()`
- `GM:PopulateToolMenu()`
- `GM:SpawnMenuBuildToolColumn(right)`
- `GM:SpawnMenuCreate()`
- `GM:SpawnMenuIsOpen()`
- `GM:SpawnMenuOpen()`
- `GM:SpawnMenuShow()`
- `GM:SpawnMenuHide()`
- `GM:SpawnMenuRefreshTools()`
- `GM:SpawnMenuRefresh(leftOnly)`
- `GM:WeaponInputBlocked()`

## `cl_utilities.lua` (client)

Spawn menu, Utilities tab (client): client settings, clean up, undo history, players and server settings, like the
utility pages of Facepunch's Sandbox menu. They are ordinary spawnmenu.AddToolMenuOption entries: add your own the same way
(hook PopulateToolMenu -> spawnmenu.AddToolMenuOption("Utilities", "User", "myid", "My page", "", "", function(panel) ... end)).

## `sh_list.lua` (shared)

GMod's `list` library: named registries that gamemodes and addons fill and the spawn menu reads.
```lua
list.Set(type, key, value)
list.Get(type) -> a copy of the table
list.GetForEdit(type) -> the real table
list.Add(type, value) -> index
list.Remove(type, key)
list.Contains(type, key)
list.Exists(type)
```

Registries the base spawn menu reads (same names and field names as GMod):
```lua
-- "SpawnableEntities"   -- key = class   -- { PrintName, ClassName, Category, Author, Information, Model, SpawnFunction }
-- "Weapon"   -- key = class   -- { ClassName, PrintName, Category, Spawnable, AdminOnly }
"NPC"   -- key = id   -- { Name, Class, Model, Category, Weapons, KeyValues, Spawn = function(ply, trace) }
"Vehicles"   -- key = id   -- { Name, Class, Model, Category, KeyValues, Spawn = function(ply, trace) }
"DesktopWindows"   -- key = id   -- { title, icon, init = function(icon, window) } -- icons in the context menu (hold C)
"OverrideMaterials"   -- array of "materials/x.vmat" (the Material tool also lists these)
```

Both realms must register the same things (put them in a shared file) so the server accepts what the client shows.

Functions defined:

- `list.Set(t, key, value)`
- `list.Get(t)`
- `list.GetForEdit(t)`
- `list.Add(t, value)`
- `list.Remove(t, key)`
- `list.Contains(t, key)`
- `list.Exists(t)`

## `sh_plastic.lua` (shared)

The "Plastic" spawnlist: Garry's Mod's PHX plastic blocks and plates (models/hunter/blocks, models/hunter/plates), with GMod's names, order and sizes (read from the original models). They're built at runtime as builder boxes
(RpModels: "builder:<x>x<y>x<z>", 1 unit = 47.45, grey grid), so nothing has to be downloaded.
Loaded from sh_spawnmenu.lua once spawnmenu.AddPropCategory exists (the guard makes the module loader's own pass a
no-op whichever order it runs the files in).

## `sh_spawnmenu.lua` (shared)

Spawn menu (hold Q): props, weapons, entities and tools. What it offers is data gamemodes and addons can change:
```lua
spawnmenu.AddPropCategory(name, { "models/....vmdl" or "org.package", ... })   -- -- shown under Props
entries may also be { "model", "shown name" } and { header = "Section" } (a heading in the grid, like GMod's
-- spawnlists)
the Plastic list (sh_plastic.lua) uses both
spawnmenu.AddEntity(id, { name, category, model, permission = "admin", Spawn = function(ply, trace) return ent end })
```

Players also see every mounted model package and, with permission props.spawn.cloud, can search sbox.game.
```lua
-- Hooks
SpawnMenuOpen() -> false keeps it closed   -- client
OnSpawnMenuOpen()
OnSpawnMenuClose()
```

Permissions: spawnmenu.open (user), weapons.give.self (admin: the Weapons tab), spawnmenu.entity.<id>, spawnmenu.npc (admin), spawnmenu.vehicle (admin).
GMod registries (list.Set("SpawnableEntities" | "Weapon" | "NPC" | "Vehicles", key, table), see sh_list.lua) are read as well:
```lua
spawnmenu.SyncLists() turns SpawnableEntities entries into spawnmenu entities   -- called by the menu and the server
```

The menu's own extension API (tabs, tool menu, content types) is in cl_spawnmenu.lua.

Functions defined:

- `spawnmenu.AddPropCategory(name, models)`
- `spawnmenu.AddEntity(id, def)`
- `spawnmenu.SyncLists()`

## `sh_spawnmenu_construction.lua` (shared)

Spawnlists from Facepunch's s&box Sandbox (MIT, Assets/models/construction, licence file next to the models): steel structures, robotics, gears, wheels and thrusters. Generated from the model folders; add your own with spawnmenu.AddPropCategory.

## `sv_spawnmenu.lua` (server)

Spawn menu (server): every click is only a request; permissions, limits and ownership are checked here.
GM.EntityLimit: spawn-menu entities per player (default 10; props.nolimit ignores it).

## `sv_utilities.lua` (server)

Spawn menu utilities (server): clean up, and the server settings page (limits).
```lua
net "base.cleanup" { scope = "mine" | "all" | "<steamid>" }   -- props of the player / everyone's (props.admin) / one player's (props.admin)
net "base.setting" { key = "PropLimit" | "EntityLimit" | "limit.<category>", value = n }   -- permission server.settings (admin); kept in storage "base/settings"
```
