---
description: "Retained 3D UI: panels placed in the world (client only)."
---

# LuaUi.World

Source: `Code/Framework/Scripting/Api/LuaUi.World.cs`

Retained 3D UI: panels placed in the world (client only).

```lua
local p = ui.CreateWorld({ pos = Vector, ang = Angle, scale = 0.1, width = 512, height = 256, parent = ent|ply, facecamera = false, anchor = "center"|"topleft", classes = "" })
p:SetWorldPos(v)
p:SetWorldAngles(a)
p:SetWorldScale(s)
p:AttachTo(ent|ply|nil [, offset [, ang]])
p:SetFaceCamera(b)
```


The returned panel is a normal Lua panel: add children with ui.Create(kind, p), style them with ui.AddStyle/SetStyle.
Orientation follows GMod's cam.Start3D2D: x runs along ang:Forward(), y along ang:Right(), and the readable side
faces ang:Up(). scale = world units per pixel (GMod's 0.1 means 10 pixels per unit).

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
