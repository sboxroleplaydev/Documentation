---
description: "Richer client drawing for Lua (physics gun beams, glows, outlines). Like render.DrawBeam, the immediate functions"
---

# LuaRender.Fx

Source: `Code/Framework/Scripting/Api/LuaRender.Fx.cs`

Richer client drawing for Lua (physics gun beams, glows, outlines). Like render.DrawBeam, the immediate functions
only work inside PostDrawOpaqueRenderables / PostDrawTranslucentRenderables and are pooled.

```lua
render.DrawBeamEx(points, opts)   -- points = { Vector, ... } (2-32; drawn as a smooth spline)
opts: width (number) or widths = { start, middle, end }
color (Color)
brightness   -- 1-8, HDR glow
texture   -- "textures/beams/beam_crack_01.vtex", any .vtex/.png
scroll   -- texture units/s
unitsPerTexture   -- default 256
additive   -- default true
render.DrawSprite(pos, size, color [, brightness [, texture]])   -- camera-facing glow (default: a soft flare)
ent:SetHighlight(color | nil [, width [, throughWalls [, glow]]])   -- client, local only: an outline (glow: soft GMod-style halo)
```

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
