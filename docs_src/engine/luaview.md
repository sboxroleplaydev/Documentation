---
description: "The local player's view and raw mouse input, for weapons like scopes and the physics gun (client only)."
---

# LuaView

Source: `Code/Framework/Scripting/Api/LuaView.cs`

The local player's view and raw mouse input, for weapons like scopes and the physics gun (client only).

```lua
LocalPlayer():SetFOV(fov [, seconds])   -- zoom to a field of view (0 or nil = back to the player's setting)
LocalPlayer():GetFOV()   -- the current field of view
input.GetMouseDelta() → x
y   -- mouse movement this frame (pixels)
input.GetMouseWheel() → n   -- wheel movement this frame (+ up, - down)
input.SetLookScale(scale)   -- multiplies mouse look (0 = view locked, 1 = normal); kept until changed
```


Everything resets when the client realm stops, so a broken script can't leave the view zoomed or locked.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
