---
description: "Physics, constraints, sounds and player movement for Lua (GMod names where they exist)."
---

# LuaPhysics

Source: `Code/Framework/Scripting/Api/LuaPhysics.cs`

Physics, constraints, sounds and player movement for Lua (GMod names where they exist).

```lua
-- ent:GetPhysicsObject() → PhysObj (server)
IsValid
Wake
Sleep
IsAsleep
EnableMotion(b)
IsMotionEnabled
EnableGravity(b)
EnableCollisionSounds(b)
IsGravityEnabled
SetVelocity(v)
AddVelocity(v)
GetVelocity
SetAngleVelocity(v)
GetAngleVelocity
ApplyForceCenter(impulse)
ApplyForceOffset(impulse, worldPos)
SetMass(kg)
GetMass
GetPos
SetPos(v)
GetAngles
SetAngles(a)
GetEntity
ComputeShadowControl(params)
WorldToLocal/LocalToWorld(pos, ang, originPos, originAng)
util.RotateAroundAxis(ang, axis, deg)
ent:WorldToLocal/LocalToWorld(pos)
ent:WorldToLocalAngles/LocalToWorldAngles(ang)
ent:PhysicsInit()   -- server: gives an entity physics
ent:GetVelocity()   -- both
constraint.Weld/Ballsocket/Rope/NoCollide/RemoveAll/RemoveConstraints/GetAll/Remove   -- server
sound.Play(path, pos [, volume [, pitch]])   -- server: everyone hears it; client: only this client
ent:EmitSound(path [, volume [, pitch]])
surface.PlaySound(path)   -- client, 2D
ply:SetMoveType(MOVETYPE_WALK|MOVETYPE_NOCLIP|MOVETYPE_NONE)
ply:GetMoveType()
ply:Freeze(b)
ply:IsFrozen()
ply:SetVelocity(v)   -- adds, like GMod
ply:GetVelocity()
```

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
