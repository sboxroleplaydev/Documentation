---
description: "Minimal client HUD bridge for Lua. Client scripts set text lines and short notifications;"
---

# LuaHud

Source: `Code/Framework/Scripting/Api/LuaHud.cs`

Minimal client HUD bridge for Lua. Client scripts set text lines and short notifications;

```lua
hud.SetLine(id, text)
hud.RemoveLine(id)
hud.Notify(text [, seconds])
```

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
