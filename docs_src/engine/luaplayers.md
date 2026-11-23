---
description: "Opaque handle Lua holds for a player. Everything is looked up live, so a stale handle is simply invalid."
---

# LuaPlayers

Source: `Code/Framework/Scripting/Api/LuaPlayers.cs`

Opaque handle Lua holds for a player. Everything is looked up live, so a stale handle is simply invalid.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
