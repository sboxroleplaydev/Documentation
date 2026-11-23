---
description: "GMod-style immediate drawing (client only). Each frame the client realm runs:"
---

# LuaDraw

Source: `Code/Framework/Scripting/Api/LuaDraw.cs`

GMod-style immediate drawing (client only). Each frame the client realm runs:
```lua
hook "PostDrawOpaqueRenderables"(false, false)
hook "PostDrawTranslucentRenderables"(false, false)   -- → 3D2D
-- hook "HUDPaint"   -- → screen
```

Inside them:
```lua
cam.Start3D2D(pos, ang, scale) ... cam.End3D2D()
draw.SimpleText(text, font, x, y, color, xalign, yalign)
draw.SimpleTextOutlined(..., outlineWidth, outlineColor)
draw.DrawText(text, font, x, y, color, xalign)
draw.RoundedBox(radius, x, y, w, h, color)
surface.SetDrawColor(r, g, b, a | Color)
surface.DrawRect(x, y, w, h)
surface.DrawOutlinedRect(x, y, w, h [, t])
surface.SetFont(name)
surface.SetTextColor(..)
surface.SetTextPos(x, y)
surface.DrawText(text)
surface.CreateFont(name, { font, size, weight })
surface.GetTextSize(text) (estimate)
ScrW()
ScrH()   -- TEXT_ALIGN_LEFT/CENTER/RIGHT/TOP/BOTTOM
```


Drawing is mapped onto pooled panels that are only restyled when what is drawn changes, so static text costs
almost nothing per frame. Outside the hooks the functions raise an error.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
