---
description: "Floating 3D2D signs above shop entities (name + status), drawn GMod-style."
---

# darkrp: module `entities`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/entities/`

## `cl_entities.lua` (client)

Floating 3D2D signs above shop entities (name + status), drawn GMod-style.

Functions defined:

- `GM:PostDrawTranslucentRenderables(depth, skybox)`

## `cl_printer.lua` (client)

Money printer menu (E on a printer): stored money with a collect button, a countdown to the next print, the
printer's stats and its upgrades. The server decides everything (sv_entities.lua); this only shows and asks.

Functions defined:

- `GM:PrinterMenuIsOpen()`
- `GM:PrinterMenuClose()`
- `GM:PrinterMenuOpen(ent)`
- `GM:PrinterMenuUpdate(force)`

## `sh_entities.lua` (shared)

DarkRP shop entities (shared definitions): things you buy that are placed in the world in front of you, owned by you, and removed when you leave. What they do is defined server-side in sv_entities.lua.
```lua
id (key)
name
description
price
max   -- per player
model
tint   -- optional Color
color
category
physics   -- default true: a physics object admins can move with the physics gun and tool gun
-- ownerPhysgun / ownerTool   -- default false: see "Who may touch shop entities" below
```

Functions defined:

- `DarkRP.createEntity(id, def)`
- `DarkRP.CanTouchEntity(ply, ent, kind)`
- `GM:CanTool(ply, trace, mode)`
- `DarkRP.PrinterUpgrade(def, id)`
- `DarkRP.PrinterLevel(ent, id)`
- `DarkRP.PrinterStats(ent, def)`

## `sv_entities.lua` (server)

Shop entities: buying places one in front of the player. They are entities of class "rp_entity" with
NW vars entity (id), owner (SteamID), ownername, title and status (shown in the look-at tooltip).

Functions defined:

- `DarkRP.UseEntity(ply, ent)`
- `DarkRP.RemoveEntitiesOf(ply)`
