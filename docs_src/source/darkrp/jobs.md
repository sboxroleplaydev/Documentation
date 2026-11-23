---
description: "DarkRP jobs (shared). Add jobs with DarkRP.createJob(name, definition)."
---

# darkrp: module `jobs`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/jobs/`

## `sh_jobs.lua` (shared)

DarkRP jobs (shared). Add jobs with DarkRP.createJob(name, definition).
```lua
command   -- unique id used by /job <command> and the F4 menu (a-z, 0-9, _)
color   -- Color shown in chat, scoreboard and HUD
salary   -- paid every DarkRP.Config.SalaryInterval seconds
max   -- maximum players in the job at once (0 = unlimited)
description
category
outfit   -- list of clothing paths the job wears (nil = the player's own avatar)
model   -- optional player model path instead of the citizen
police   -- may mark players wanted and arrest them   -- mayor   -- may set the city's laws
weapons   -- weapon classes the job gets on spawn, e.g. { "weapon_pistol" } (everyone also gets GM.DefaultLoadout)
```

Functions defined:

- `DarkRP.createJob(name, def)`

## `sv_jobs.lua` (server)

Job changes: validated on the server (exists, limits, cooldown, PlayerCanChangeJob hook).

Functions defined:

- `DarkRP.CountJob(command)`
- `DarkRP.CanChangeJob(ply, job)`
- `DarkRP.SetJob(ply, job, announce)`
- `DarkRP.ApplyJobLook(ply, job)`
