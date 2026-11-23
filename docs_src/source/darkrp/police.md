---
description: "Police: wanted list, arrests and the jail."
---

# darkrp: module `police`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/police/`

## `sv_police.lua` (server)

Police: wanted list, arrests and the jail.
```lua
/wanted <name> <reason>   -- /unwanted <name>   -- (police jobs: job.police = true)
-- E on a wanted player as police
-- arrest -> jail for DarkRP.Config.ArrestTime seconds
-- prison jumpsuit
-- then released
/addjailpos
/removejailpos   -- (admin.jail) jail spawn points, stored per map like doors.
```

NW vars: rp.wanted (reason, "" = not wanted), rp.arrested (release time in CurTime, 0 = free).

Functions defined:

- `DarkRP.InitJail()`
- `DarkRP.IsArrested(ply)`
- `DarkRP.SendToJail(ply)`
- `DarkRP.SetWanted(ply, reason, by)`
- `DarkRP.Arrest(ply, by)`
- `DarkRP.Release(ply)`
