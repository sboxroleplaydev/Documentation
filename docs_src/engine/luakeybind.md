---
description: "Client library cookie (GMod-style): small values that persist on the player's machine, per gamemode."
---

# LuaKeybind

Source: `Code/Framework/Scripting/Api/LuaKeybind.cs`

Client library `cookie` (GMod-style): small values that persist on the player's machine, per gamemode.
```lua
cookie.GetString(name [, default])
cookie.GetNumber(name [, default])
cookie.Set(name, value)
cookie.Delete(name)
```

Stored in data/roleplay/cookies.json. Limits: 256 keys per gamemode, 1024 characters per value.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
