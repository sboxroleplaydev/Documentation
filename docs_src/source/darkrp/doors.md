---
description: "Tooltip for the door or dropped item you look at."
---

# darkrp: module `doors`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/doors/`

## `cl_doors.lua` (client)

Tooltip for the door or dropped item you look at.

Functions defined:

- `GM:DoorTipCreate()`
- `GM:DoorTipThink()`

## `sh_doors.lua` (shared)

Door geometry shared by the server (placing doors) and the client (the Door Placer's preview).

Functions defined:

- `DarkRP.DoorLayout(mins, maxs, pos, yaw, o)`

## `sh_glass.lua` (shared)

Finding window openings (shared: the server places the glass, the client shows the preview with the same code).

Functions defined:

- `DarkRP.IsGlass(ent)`
- `DarkRP.OpeningScan(ply, hit, hn, forward, snap)`
- `DarkRP.FindOpenings(ply, hit, hn, forward, snap)`

## `sv_doors.lua` (server)

Doors (class "rp_door").
Two sources:
```lua
-- * doors placed in the scene   -- a LuaEntity with class rp_door, key values title/price
-- e.g. the test world
-- * doors placed in game by admins with /adddoor
saved per map in storage ("mapdoors/<map>"). Cloud maps such
-- as thieves.rpdowntown3t ship without doors
-- so this is how a server owner sets them up
```

Use (E) opens/closes; owners lock/unlock with R or /lock /unlock; /buydoor and /selldoor.
Ownership and locks are saved in storage ("doors"), keyed by a stable door key.

NW vars on each door: door.key, door.title, door.price, door.owner (steamid), door.ownername, door.locked, door.open, door.yaw

Functions defined:

- `DarkRP.InitDoors()`
- `DarkRP.ConvertToDoor(ply, ent, title, price, away, double, side, yaw)`
- `DarkRP.PlaceModelDoor(ply, model, pos, yaw, title, price, away, double, side)`
- `DarkRP.UpdateMapDoor(door, title, price)`
- `DarkRP.RemoveMapDoor(door)`
- `DarkRP.FlipMapDoor(door)`
- `DarkRP.IsDoorOwner(ply, door)`
- `DarkRP.UseDoor(ply, door)`
- `DarkRP.SetDoorLocked(ply, door, locked)`

## `sv_glass.lua` (server)

Window glass placed with the Glass Placer tool (gamemode/tools/sh_glassplacer.lua): a pane fills an opening in a wall or a frame.
Up to DarkRP.Config.GlassLimit (2500) panes per map, built to cost almost nothing:
```lua
-- * No entity per pane. Panes are grouped by place into "chunks" of at most 64 boxes
a chunk is ONE entity (class "rp_glass", made with boxset.Create): one mesh
-- one static collider
-- one network object. Joining clients get the chunk from the engine's
-- own sync
-- a broken pane is a change of a few bits
-- nothing else is sent
* No Think hook per pane. Hits come through the weapon system's EntityTakeDamage (bullets, fists, melee), explosions through
-- the BlastDamage hook
-- fast props through one 0.15 s timer that only looks at props moving fast near a pane
-- * Loading is spread over frames: records are parsed 250 a tick
-- chunk entities built 2 a tick
```

A pane is one or a few thin boxes that follow the opening (arches, odd frames); the whole pane breaks at once.
Saved per map, compact: storage "mapglass2/<map>" = { v = 2, parts = n, n = count } and "mapglass2/<map>/<k>" = up to 250 records
each as one string "x,y,z,yaw,t,ox,oz,w,h[,ox,oz,w,h...]". Maps saved by the old system ("mapglass/<map>") are converted once.

```lua
-- API
DarkRP.AddGlass(ply, e) / DarkRP.RemoveGlass(ent, hitPos) / DarkRP.BreakGlass(pane, attacker, hitPos, dir) /
DarkRP.RepairGlass(pane) / DarkRP.RepairAllGlass() / DarkRP.FindGlass(ent, pos) / DarkRP.GlassStats().
-- Hook
CanBreakGlass(attacker, pane, ent) -> false blocks. Settings: DarkRP.Config.Glass* (config/sh_config.lua)
```

Functions defined:

- `DarkRP.BreakGlass(p, attacker, hitPos, dir)`
- `DarkRP.RepairGlass(p)`
- `DarkRP.RepairAllGlass()`
- `DarkRP.FindGlass(ent, pos)`
- `DarkRP.InitGlass()`
- `DarkRP.AddGlass(ply, e)`
- `DarkRP.RemoveGlass(ent, pos)`
- `DarkRP.GlassStats()`
