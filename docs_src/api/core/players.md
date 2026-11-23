---
description: "Players: Identity: Nick/Name/GetName, SteamID/SteamID64, IsValid, IsLocalPlayer, IsListenServerHost, Ping."
---

# Players

Both realms (read-only):

- **Identity:** `Nick/Name/GetName`, `SteamID/SteamID64`, `IsValid`, `IsLocalPlayer`, `IsListenServerHost`, `Ping`.
- **Position and aim:** `GetPos`, `GetEyeAngles`, `GetShootPos`, `#!lua GetEyeTrace([dist])` → `{ Hit, HitPos, Distance, Entity, HitWorld }`.
- **NW vars:** `GetNWString/Int/Float/Bool/Var(key, default)`.
- **Library:** `#!lua player.GetAll()`, `#!lua player.GetCount()`; client also has `#!lua LocalPlayer()`.
- **Bots:** `#!lua player.CreateBot([name])` → Player or nil, reason (server, host only, at most 32): a real player body (scoreboard, health, loadout, PlayerInitialSpawn/PlayerSpawn/PlayerDisconnected hooks, random outfit) with no connection, `#!lua SteamID()` `bot_<n>`. `#!lua ply:IsBot()` (both realms), `#!lua player.GetBots()`, `#!lua ply:SetBotInput(forward, left [, jump [, run]])` (-1..1; jump = one jump; run held) and `#!lua ply:SetEyeAngles(ang)` (bots only), `#!lua ply:Kick()` removes a bot.

    A bot has no behaviour of its own: the base gamemode's `modules/bots/sv_bots.lua` makes it wander (`#!lua GM:BotThink(ply, state)` to change that; `#!lua GM.BotMode` = "wander"|"stand"). Console: `rp_bot [count] [name]`, `rp_bot_kick [name|all]`, `rp_bot_mode wander|stand` (permission `#!lua base.bot`, default admin; also `rp rp_bot ...`).

    DarkRP does not save a bot's profile.

- **Death ragdolls:** `#!lua ply:CreateRagdoll([seconds])` (server): every machine builds a physics ragdoll of the player's body (model, skin, clothes, last velocity) that lies there for `seconds` (default 10, max 120) and vanishes; client-side bodies, nothing networked per bone, at most 24 at once, one per player.

    Client: `#!lua ply:GetRagdollPos()` → Vector or nil (for a death camera). Base: `#!lua GM:DoPlayerDeath` creates one for `#!lua GM.RagdollTime` seconds (default 10, 0 = none) and the client shows a death camera behind and above it while you are dead.


Server only:

- `SetNWString/Int/Float/Bool/Var(key, value)`.
- `#!lua ChatPrint(text)`.
- `#!lua Kick(reason)` (not the host).
- `#!lua Spawn()`: respawn at a spawn point and run `PlayerSpawn`.
- `#!lua SetPos(vector)`: teleports through the owning client, which simulates its own movement.

## Movement (Garry's Mod style)

Defaults are GMod sandbox's (`player_default`), set by base's `#!lua GM:SetupMovement(ply)` on every spawn from `#!lua GM.PlayerMovement` (change the table or override `SetupMovement`; DarkRP: walk 160 / run 240 from its config). Setters are server only, getters work in both realms.

The owning client simulates the movement, so changes arrive there over the network (a moment later). Units are GMod's (1 unit = 1 inch).


| Setter / getter | Default | Meaning |
|---|---|---|
| `#!lua SetWalkSpeed(n)` / `#!lua GetWalkSpeed()` | 200 | no key held |
| `#!lua SetRunSpeed(n)` / `#!lua GetRunSpeed()` | 400 | Shift |
| `#!lua SetSlowWalkSpeed(n)` / `#!lua GetSlowWalkSpeed()` | 100 | Alt (the Walk button) |
| `#!lua SetCrouchedWalkSpeed(f)` / `#!lua GetCrouchedWalkSpeed()` | 0.3 | crouching (Ctrl) speed as a fraction of the walk speed |
| `#!lua SetJumpPower(n)` / `#!lua GetJumpPower()` | 200 | GMod jump power (sv_gravity 600); scaled to the map's gravity, so the jump is as high as in GMod (~33 units, more with a crouch jump) |
| `#!lua SetDuckSpeed(s)` / `#!lua SetUnDuckSpeed(s)` (+ getters) | 0.3 / 0.3 | seconds to crouch / stand up |
| `#!lua SetFriction(f)` / `#!lua GetFriction()` | 1 | ground friction multiplier (1 = sv_friction 8, stop speed 100) |
| `#!lua SetAcceleration(n)` / `#!lua SetAirAcceleration(n)` (+ getters) | 10 / 10 | sv_accelerate / sv_airaccelerate |
| `#!lua SetAirStrafing(b)` / `#!lua GetAirStrafing()` | true | steer in the air: strafe jumping and surfing (air speed cap 30 like Source, no air friction) |
| `#!lua SetBunnyHopping(b)` / `#!lua GetBunnyHopping()` | true | a jump right on landing keeps the speed (no cap, like GMod); one jump per key press |
| `#!lua SetNoclipSpeed(n)` / `#!lua GetNoclipSpeed()` | 800 | noclip: Shift ×2.5, Alt ×0.25, Space up, Ctrl down; accelerates and glides to a stop, leaving noclip keeps some momentum |

State (both realms): `#!lua ply:Crouching()`, `#!lua ply:OnGround()` / `#!lua ply:IsOnGround()`, `#!lua ply:IsSprinting()` (on the ground,
standing and faster than walking), `#!lua ply:GetVelocity()`. Move types: `#!lua ply:SetMoveType(MOVETYPE_WALK|MOVETYPE_NOCLIP|MOVETYPE_NONE)`,
`#!lua ply:Freeze(b)`, `#!lua ply:SetVelocity(v)` (adds, like GMod).

