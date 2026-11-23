---
description: "Props (shared): ownership rules used by the physics gun, the tool gun and the spawn menu."
---

# base: module `props`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/props/`

## `sh_props.lua` (shared)

Props (shared): ownership rules used by the physics gun, the tool gun and the spawn menu.
```lua
props.GetOwner(ent) -> steamid or ""
props.CanTouch(ply, ent) -> true if ply may move/edit ent
```

Spawned props are entities of class "prop_physics" with NW strings "owner" (SteamID) and "ownername".
Everything with an "owner" NW var follows the same rules (DarkRP shop entities too).

Functions defined:

- `props.GetOwner(ent)`
- `props.CanTouch(ply, ent)`

## `sv_props.lua` (server)

Props (server): spawning with limits and undo, cleanup.
```lua
props.Spawn(ply, model) -> ent | nil
reason
props.Count(ply)
props.RemoveAll(ply)
GM.PropLimit   -- per player, default 50; permission props.nolimit ignores it
GM.RemovePropsOnDisconnect (true)
-- Hooks
PlayerSpawnProp(ply, model) -> false blocks
PlayerSpawnedProp(ply, model, ent)
```

Commands: "rp gm_spawn <model>", /cleanup (your props), /cleanupall (props.admin).

Functions defined:

- `props.Count(ply)`
- `props.CanSpawn(ply, model, kind)`
- `props.Spawn(ply, model)`
- `props.SpawnAt(ply, model, pos, ang)`
- `props.RemoveAll(ply)`
- `GM:PhysgunPickup(ply, ent)`
- `GM:OnPhysgunFreeze(weapon, phys, ent, ply)`
- `GM:GravGunPickupAllowed(ply, ent)`
- `GM:OnPhysgunReload(weapon, ply)`
