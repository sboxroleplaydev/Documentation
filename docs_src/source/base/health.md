---
description: "Base HUD: health (bottom left) and a death overlay. Hide parts with GMod's HUDShouldDraw:"
---

# base: module `health`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/health/`

## `cl_health.lua` (client)

Base HUD: health (bottom left) and a death overlay. Hide parts with GMod's HUDShouldDraw:
```lua
function GM:HUDShouldDraw(name) if name == "BaseHealth" then return false end return self.BaseClass.HUDShouldDraw(self, name) end
```

Names: "BaseHealth", "BaseDeath" (and "BaseAmmo" once weapons exist).

Functions defined:

- `GM:HUDShouldDraw(name)`
- `GM:BaseHUDCreate()`
- `GM:BaseHUDThink()`

## `sh_health.lua` (shared)

Health (shared accessors, GMod names). The server owns the values (NW ints "health" / "maxhealth").

Functions defined:

- `PLAYER:Health()`
- `PLAYER:GetMaxHealth()`
- `PLAYER:Alive()`
- `PLAYER:GetRespawnTime()`

## `sv_health.lua` (server)

Health, damage and death (server). GMod-style:
```lua
ply:SetHealth(n)
ply:SetMaxHealth(n)
ply:TakeDamage(amount [, attacker [, inflictor]])
ply:Kill()
hooks: PlayerShouldTakeDamage(ply, attacker) -> false cancels
ScalePlayerDamage(ply, amount, attacker, inflictor)
-- -> a new amount
PlayerHurt(ply, attacker, healthLeft, taken)
PlayerDeath(victim, inflictor, attacker)
```

A dead player is hidden (a ragdoll of the body lies there for GM.RagdollTime seconds, default 10, 0 = none) and respawns
after GM.RespawnDelay seconds (GM:PlayerDeathThink can delay it).

Functions defined:

- `PLAYER:SetMaxHealth(n)`
- `PLAYER:SetHealth(n, attacker, inflictor)`
- `PLAYER:TakeDamage(amount, attacker, inflictor)`
- `PLAYER:Kill()`
- `GM:PlayerShouldTakeDamage(ply, attacker)`
- `GM:DoPlayerDeath(ply, attacker, inflictor)`
- `GM:PlayerDeath(victim, inflictor, attacker)`
- `GM:PlayerDeathThink(ply)`
