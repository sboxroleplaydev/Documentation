---
description: "GMod's layout: creation tabs on the left (Props, Entities, Weapons, NPCs, Vehicles) with a category tree, icon grid and search; tool tabs on the right..."
---

# Spawn menu and context menu

GMod's layout: creation tabs on the left (Props, Entities, Weapons, NPCs, Vehicles) with a category tree, icon grid and search; tool tabs on the right (Tools, Utilities) with a category list and the selected entry's control panel.

Typing in the search box keeps the menu open until Q or Escape. **Props:** spawnlists, your own spawnlists (saved in your cookies; right-click a prop to add/remove), mounted packages, sbox.game search (`#!lua props.spawn.cloud`). **Utilities:** client settings (icon size), clean up, undo history (click to undo that entry), players, server settings (limits, saved on the server, permission `#!lua server.settings`).


**Extending it (client, GMod names)** - full list in the header of `modules/spawnmenu/cl_spawnmenu.lua`: `#!lua spawnmenu.AddCreationTab(name, function(parent, search) end, icon, order, tooltip [, visible])`, `#!lua GetCreationTabs()`, `#!lua AddToolTab(id, name, icon)`, `#!lua AddToolCategory(tab, id, name)`, `#!lua AddToolMenuOption(tab, category, class, name, command, config, function(panel) end)`, `#!lua GetToolMenu(tab)`, `#!lua AddContentType(name, function(container, obj) end)`, `#!lua OpenTab(name)`, `#!lua ActivateTool(mode)`;

hooks `AddToolMenuTabs`, `AddToolMenuCategories`, `PopulateToolMenu`, `SpawnMenuOpen`, `OnSpawnMenuOpen`, `OnSpawnMenuClose`, `ContextMenuOpen`, `ContextMenuClose`, `SpawnlistContentChanged`. Registries (`list`, both realms, GMod's field names): `#!lua list.Set("SpawnableEntities", class, { PrintName, ClassName, Category, Model, SpawnFunction })`, `#!lua list.Set("Weapon", class, { ClassName, PrintName, Category })`, `#!lua list.Set("NPC", id, { Name, Class, Model, Category, Spawn })`, `#!lua list.Set("Vehicles", ...)`, `#!lua list.Set("DesktopWindows", id, { title, icon, init })`;

plus `list.Get/GetForEdit/Add/Remove/ Contains/Exists`. Props: `#!lua spawnmenu.AddPropCategory(name, entries)` (entries: model strings, `{ model, name }`, `{ header }`, or `{ type = "<content type>", ... }`), entities `#!lua spawnmenu.AddEntity(id, def)`.

Permissions: `#!lua spawnmenu.open`, `#!lua weapons.give.self`, `spawnmenu.entity.<id>`, `#!lua spawnmenu.npc`, `#!lua spawnmenu.vehicle`.


**Differences from GMod:** tab functions get a parent panel (`#!lua function(parent, search)`) instead of returning a VGUI panel; control panels are the tool panel builder (Slider/CheckBox/Key/... store tool ClientConVars, or cookies `spawnmenu.<key>` for entries without a tool: `#!lua panel:Get(key)`);

no Post Process, Dupes or Saves tabs (we have no contraption save format yet); NPC and vehicle tabs stay empty until something registers them. **Migration:** `#!lua GM:SpawnMenuTabs()` still works - it now returns `{ id, label, icon, tooltip, build(self, body, search) }` built from the creation tabs;

override it to add/remove tabs the old way. The old `GM:SpawnMenuBuildProps/Weapons/Entities` functions are gone (use `#!lua spawnmenu.AddCreationTab`).


**Context menu (hold C):** shows the properties of the object under your crosshair and the `DesktopWindows` icons. `#!lua properties.Add(name, { MenuLabel, Order, MenuIcon, Filter(self, ent, ply), Action(self, ent), Receive(self, ent, ply, data) })`, `#!lua self:Send(ent [, data])`;

base properties: remove, freeze, gravity. Hook `#!lua CanProperty(ply, name, ent)`. GM: `ContextMenuShow/Hide/IsOpen`. Server messages are checked again (filter, distance, rate limit).


- **Weapons tab:** permission `#!lua weapons.give.self`. Example entities: `item_healthkit`, `item_ammocrate`.
- `#!lua content.Search(query, function(results, err, done) end [, type])` (client): sbox.game search (models by default); loads every result page by page (up to 6000): the callback runs per page with that page's results and `done = false`, finally with `done = true`;

    a new search cancels the running one. `#!lua SetClipboardText(text)` (client) copies text to the clipboard. Details: results `{ ident, title, thumb, author }`.


