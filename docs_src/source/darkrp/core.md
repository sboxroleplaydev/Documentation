---
description: "Private state from the server (only ever our own): money, salary, inventory."
---

# darkrp: module `core`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/core/`

## `cl_private.lua` (client)

Private state from the server (only ever our own): money, salary, inventory.

## `sh_player.lua` (shared)

Player accessors (shared). Public state lives in NW vars, which only the server can set:
```lua
rp.name
rp.job
rp.hunger
...   -- group, health and permissions come from base
```

Private state (money, inventory) is never in NW vars; the server sends it only to its owner.

Functions defined:

- `PLAYER:GetRPName()`
- `PLAYER:GetJob()`
- `PLAYER:GetJobName()`
- `PLAYER:Hunger()`
- `PLAYER:IsWanted()`
- `PLAYER:GetWantedReason()`
- `PLAYER:ArrestTimeLeft()`
- `PLAYER:IsPolice()`
- `PLAYER:IsMayor()`

## `sh_util.lua` (shared)

DarkRP shared helpers.

Functions defined:

- `DarkRP.FormatMoney(n)`
- `DarkRP.FindPlayer(text)`

## `sv_core.lua` (server)

Core server helpers shared by the modules.

Functions defined:

- `DarkRP.UsePlayer(ply, target)`
- `DarkRP.SetHealth(ply, hp)`
- `DarkRP.FindPlayerBySteamID(sid)`

## `sv_data.lua` (server)

Player profiles: persisted with the framework's server-side storage ("players/<steamid>").
Everything loaded from disk is validated before use.

Functions defined:

- `DarkRP.LoadProfile(ply)`
- `DarkRP.GetProfile(ply)`
- `DarkRP.SaveProfile(ply)`
- `DarkRP.ReleaseProfile(ply)`
- `DarkRP.SaveAll()`
- `DarkRP.SendPrivate(ply)`
- `DarkRP.ValidateRPName(name)`
- `DarkRP.SetRPName(ply, name)`
