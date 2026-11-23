---
description: "Small general-purpose building blocks for contraptions (thrusters, hoverballs, lights ...), the engine side of the"
---

# LuaGadgets

Source: `Code/Framework/Scripting/Api/LuaGadgets.cs`

Small general-purpose building blocks for contraptions (thrusters, hoverballs, lights ...), the engine side of the
base gamemode's tool gun modes. Gameplay stays in Lua; this is only what Lua can't do itself.

Server:
```lua
gadget.SetDriver(ent, kind, { force, speed, air, lift, strength, dir = Vector (local), enabled })
-- kind: "thruster"   -- pushes along dir
-- "hoverball"   -- holds a height
-- "keepupright"
-- "balloon"   -- floats up
gadget.Control(ent, value)   -- -1..1: thruster power / hoverball moves its target height
gadget.GetDriver(ent) -> table or nil
gadget.ClearDriver(ent)
gadget.SetEnabled(ent, bool)
gadget.SetFx(ent, kind, { color, a, b, c, text, pos = Vector (local), ang = Angle (local), on })
-- kind: "light"   -- a intensity, b radius, c spot cone degrees or 0
-- "trail"   -- a width, b seconds
-- "text"   -- text, a font size, b scale
-- "emitter"   -- a particles per second, b speed, c lifetime
gadget.GetFx(ent, kind) -> table or nil
gadget.RemoveFx(ent [, kind])
```

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
