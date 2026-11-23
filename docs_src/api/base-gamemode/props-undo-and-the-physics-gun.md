---
description: "Props, undo and the physics gun: Props (server): props.Spawn(ply, model) → ent | nil, reason (permission, limit, placement, ownership, undo),..."
---

# Props, undo and the physics gun

- **Props (server):** `#!lua props.Spawn(ply, model)` → ent | nil, reason (permission, limit, placement, ownership, undo), `#!lua props.Count(ply)`, `#!lua props.RemoveAll(ply)`; shared `#!lua props.GetOwner(ent)`, `#!lua props.CanTouch(ply, ent)`. Spawned props are `prop_physics` with NW strings `owner` (SteamID), `ownername`, `model`. `#!lua GM.PropLimit` (50), `#!lua GM.RemovePropsOnDisconnect` (true).

    Hooks: `#!lua PlayerSpawnProp(ply, model)` → false blocks, `#!lua PlayerSpawnedProp(ply, model, ent)`, `#!lua CanTouchProp(ply, ent)` → bool overrides the ownership rule. Commands: `rp gm_spawn <model>`, `/cleanup`, `/cleanupall` (permission `#!lua props.admin`).

- **Limits (base, `modules/limits`):** GMod-style per-player limits for everything the tool gun makes. Shared: `#!lua limits.Register(id, default, label [, gadgetKind])`, `#!lua limits.Get(id)` (0 = unlimited), `#!lua limits.List()`. Categories: balloons 50, buttons 50, cameras 10, emitters 20, hoverballs 50, lights 5, speakers 10, spawners 5, texts 20, thrusters 50, wheels 50, constraints 50 (every weld/rope/motor/...), ropes 25 (rope, elastic, slider, rod, winch, hydraulic, muscle; they count as constraints too).

    Owners override with `GM.Limits = { thrusters = 20 }` (only the listed ones); an admin's change on the settings page wins over the config. Server: `#!lua limits.Count(ply, id)`, `#!lua limits.Check(ply, id [, notify])` → true | false, message, `#!lua limits.Notify(ply, id)` ("You've hit the thrusters limit!"), `#!lua limits.CountAll(ply)`.

    Hook `#!lua PlayerCheckLimit(ply, id, count, limit)` → false blocks, true allows. Counting is derived from the world (owner + gadget kind), so remover, undo, cleanup and disconnect free slots by themselves; constraints are tracked while a tool gun click runs (`#!lua limits.Current` is set by the tool gun) and dropped when they or their entity are gone.

    Permission `#!lua props.nolimit` ignores all limits. A gadget made with `#!lua tools.Place` / `#!lua tools.CreateGadget` (`kind = "thruster"`, ...) is checked automatically (`#!lua props.CanSpawn(ply, model, kind)`); gadgets no longer count against `#!lua GM.PropLimit`.

    A gadget kind without a category still counts as a prop. Tools that call `#!lua pcall(constraint.X, ...)` get the limit for free; report failures with `#!lua tools.ReportError(ply, err)` (silent for limit errors, the player was told already).

    Addons add a category with `#!lua limits.Register("dynamite", 10, "Dynamite", "dynamite")`.

- **Undo (server, GMod's library):** `#!lua undo.Create(name)`, `#!lua undo.AddEntity(ent)`, `#!lua undo.AddFunction(fn, ...)`,
  `#!lua undo.SetPlayer(ply)`, `#!lua undo.SetCustomUndoText(text)`, `#!lua undo.Finish()`; `#!lua undo.Do(ply)`, `#!lua undo.GetTable(ply)`,
  `#!lua undo.ReplaceEntity(old, new)`. Hook `#!lua CanUndo(ply, entry)`. Players press **Z** (rebindable), `rp undo` or `/undo`.
- **Physics gun** (`weapon_physgun`, server-authoritative): hold left mouse to carry, mouse wheel pushes/pulls, hold E and move the mouse to rotate, right click freezes, R unfreezes what you look at. GMod hooks: `#!lua PhysgunPickup(ply, ent)` (base: `#!lua props.CanTouch`);

    hold Shift while rotating to snap to `#!lua SWEP.SnapAngle` (45°), R twice quickly unfreezes all of that prop owner's props; the beam shows whenever left mouse is held (NW bool `#!lua physgun.firing`), held props get an outline in `#!lua SWEP.BeamColor`;

    `#!lua OnPhysgunPickup(ply, ent)`, `#!lua PhysgunDrop(ply, ent)`, `#!lua OnPhysgunFreeze(weapon, phys, ent, ply)` → false blocks, `#!lua OnPhysgunReload(weapon, ply)` → false blocks. NW vars on the holder: `#!lua physgun.ent` (entity id), `#!lua physgun.hit`; on the entity: `#!lua physgun.holder`.

    Sounds: Facepunch's s&box Sandbox physgun sounds (MIT, `Assets/weapons/physgun/sounds`) as `#!lua SWEP.Sounds` - idle hum while it's out, start + active loop while the beam is on, end, attach on pickup, freeze, unfreeze, E button clicks.

    **Gravity gun mode** (right mouse when nothing is held, like Facepunch's Sandbox physgun): hold right mouse to pull a loose object in a 35° cone towards you; within `#!lua SWEP.GravityGrabDistance` (200) it floats in front of you; left click launches it (`GravityLaunchSpeed`), right click drops it.

    Hooks (GMod names): `#!lua GravGunPickupAllowed(ply, ent)` (base: always `true`: any loose physical object, whoever owns it; only a hook returning `false` blocks it, DarkRP's `#!lua DarkRP.CanTouchEntity` rules apply to the beam only), `GravGunOnPickedUp`, `GravGunOnDropped`, `GravGunPunt` → false blocks the launch.

    NW vars on the holder: `#!lua physgun.grav` (entity id), `#!lua physgun.gravhold`. Sounds: Facepunch's `gravgun.*`.

- **Permissions:** `#!lua props.spawn` (user), `#!lua props.spawn.cloud` (admin), `#!lua props.nolimit` (admin), `#!lua props.admin` (admin).

