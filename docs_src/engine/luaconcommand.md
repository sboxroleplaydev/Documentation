---
description: "GMod's concommand for Lua. s&box can't add console commands at runtime, so all Lua commands run through one"
---

# LuaConCommand

Source: `Code/Framework/Scripting/Api/LuaConCommand.cs`

GMod's `concommand` for Lua. s&box can't add console commands at runtime, so all Lua commands run through one
framework command: `rp <command> [args...]` (`rp` alone lists them).

```lua
concommand.Add(name, function(ply, cmd, args, argStr) end [, autoComplete, helpText])
concommand.Remove(name)
concommand.GetTable()
RunConsoleCommand(name, ...)
```


Like GMod: a command the client realm defines runs there (ply = the local player); otherwise a client sends it to the
server (rate-limited), where it runs with ply = that player. In the server console (dedicated) ply is nil.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
