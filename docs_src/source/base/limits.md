---
description: "Limits (shared): per-player limits for everything the tool gun makes, like GMod's sboxmax settings."
---

# base: module `limits`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/limits/`

## `sh_limits.lua` (shared)

Limits (shared): per-player limits for everything the tool gun makes, like GMod's sbox_max* settings.
```lua
limits.Register(id, default, label [, kind])   -- a category; kind = the tool gun "gadget" kind it counts (optional)
limits.Get(id) -> number   -- the limit in force (GM.Limits[id] overrides the default; 0 = unlimited)
limits.List() -> { { id, label, default }, ... }   -- all categories, sorted
```

Server owners set them in the gamemode config:  GM.Limits = { thrusters = 20, balloons = 30 }  (only the ones you list).
Props are limited by GM.PropLimit (see props), spawn-menu entities by GM.EntityLimit.
Server side API and hooks: see sv_limits.lua.

Functions defined:

- `limits.Register(id, default, label, kind)`
- `limits.Get(id)`
- `limits.List()`

## `sv_limits.lua` (server)

Limits (server): the per-player counters behind the tool gun limits (see sh_limits.lua).
```lua
limits.Count(ply, id) -> number   -- what the player has now (entities by owner + gadget kind, constraints tracked)
limits.Check(ply, id [, notify]) -> true | false
message   -- may the player make one more? (notify = tell them)
limits.Notify(ply, id)   -- "You've hit the thrusters limit!"
limits.CountAll(ply) -> { id = n }   -- for the settings page
```

Counting is derived from the world, so removing a thing (remover, undo, cleanup, disconnect) frees its slot at once.
Admins with permission props.nolimit are never limited. Hook PlayerCheckLimit(ply, id, count, limit) -> false blocks
(true allows even over the limit), like GMod's.
Constraints made while a tool gun click runs are counted automatically (constraints and, for rope-like ones, ropes).

Functions defined:

- `limits.Count(ply, id)`
- `limits.CountAll(ply)`
- `limits.Notify(ply, id)`
- `limits.Check(ply, id, notify)`
- `limits.IsLimitError(err)`
