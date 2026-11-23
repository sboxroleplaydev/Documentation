---
description: "{ 'id': 'darkrp', 'title': 'DarkRP', 'version': '0.2.0', 'apiVersion': 1,"
---

# Gamemodes and derivation

```json
{ "id": "darkrp", "title": "DarkRP", "version": "0.2.0", "apiVersion": 1,
  "entry": { "shared": "gamemode/sh_init.lua", "server": "gamemode/sv_init.lua", "client": "gamemode/cl_init.lua" },
  "dependencies": [ "base" ] }
```

Dependencies load first. Each derived gamemode sees what the previous ones defined as `#!lua GM.BaseClass`, so you
override and extend like in GMod:

```lua
function GM:PlayerSpawn(ply)
    ply:SetNWInt("rp.health", 100)
    self.BaseClass.PlayerSpawn(self, ply)   -- keep base behaviour
end
```

