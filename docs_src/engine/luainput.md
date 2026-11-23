---
description: "Client input → Lua. Each frame the client realm receives PlayerButtonDown(action) / PlayerButtonUp(action)"
---

# LuaInput

Source: `Code/Framework/Scripting/Api/LuaInput.cs`

Client input → Lua. Each frame the client realm receives `PlayerButtonDown(action)` / `PlayerButtonUp(action)`
for the project's input actions (not while a Lua text box has focus). Escape is reported as "Escape"; if a hook
returns true for it, the engine's own escape handling is suppressed.

Pressing Use also asks the server to run `PlayerUse(ply, ent)` for whatever the player is looking at (within
`UseRange` units); the server does the trace itself, so the client can't choose the target.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
