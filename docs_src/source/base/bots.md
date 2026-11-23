---
description: "Bots (server): real players that nobody controls, like Garry's Mod's bots (they are in the scoreboard, have health, a loadout, take damage, die and..."
---

# base: module `bots`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/bots/`

## `sv_bots.lua` (server)

Bots (server): real players that nobody controls, like Garry's Mod's bots (they are in the scoreboard, have health, a loadout, take damage, die and respawn, and run the PlayerInitialSpawn / PlayerSpawn / PlayerDisconnected hooks) - but dumb.
```lua
rp_bot [count] [name]   -- spawn bots (count 1-16, default 1; permission base.bot, default admin)
rp_bot_kick [name|all]   -- remove the bot with that name, all bots, or (no argument) the newest one
rp_bot_mode [wander|stand]   -- what bots do: wander about (default) or just stand there
-- Engine side
player.CreateBot(name)
ply:IsBot()
ply:SetBotInput(forward, left [, jump [, run]])
ply:SetEyeAngles(ang)
```

This file is only the brain: bots wander (walk a while, pause, turn, sometimes jump, turn away from walls, hop low obstacles).
Gamemodes can change GM.BotThink(bot, state) to give them other behaviour.

Functions defined:

- `GM:BotThink(ply, st)`
