---
description: "A world object Lua can see and control: map-placed (set Class and KeyValues in the"
---

# LuaEntity

Source: `Code/Framework/Scripting/Api/LuaEntity.cs`

A world object Lua can see and control: map-placed (set `Class` and `KeyValues` in the
editor, and make the object networked) or created at runtime with `ents.Create`.
Class, NW vars and tint are host-written; transforms of networked objects replicate automatically.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
