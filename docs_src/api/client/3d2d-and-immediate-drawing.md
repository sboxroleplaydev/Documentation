---
description: "GMod style. Works like in Garry's Mod:"
---

# 3D2D and immediate drawing
<span class="realm realm-client">Client</span>

**GMod style.** Works like in Garry's Mod:

```lua
surface.CreateFont("MySign", { font = "Inter", size = 30, weight = 800 })

hook.Add("PostDrawTranslucentRenderables", "signs", function()
    local ang = Angle(0, LocalPlayer():GetEyeAngles().y - 90, 90)   -- upright, facing the player
    cam.Start3D2D(Vector(0, 0, 80), ang, 0.1)
        draw.RoundedBox(8, -120, -30, 240, 60, Color(0, 0, 0, 200))
        draw.SimpleText("Hello", "MySign", 0, 0, color_white, TEXT_ALIGN_CENTER, TEXT_ALIGN_CENTER)
    cam.End3D2D()
end)

hook.Add("HUDPaint", "hud", function()
    draw.SimpleText("Top left", "DermaLarge", 20, 20, Color(255, 200, 80))
end)
```

- `#!lua cam.Start3D2D(pos, ang, scale)` / `#!lua cam.End3D2D()`: same orientation as GMod (x along `#!lua ang:Forward()`, y along
  `#!lua ang:Right()`, readable side towards `#!lua ang:Up()`); `scale` = world units per pixel.
- `#!lua draw.SimpleText(text, font, x, y, color, xalign, yalign)`, `#!lua draw.SimpleTextOutlined(…, outlineWidth, outlineColor)`,
  `#!lua draw.DrawText(text, font, x, y, color, xalign)` (multi-line), `#!lua draw.RoundedBox(r, x, y, w, h, color)`, `#!lua draw.RoundedBoxEx`
  (all corners rounded).
- `#!lua surface.SetDrawColor`, `DrawRect`, `DrawOutlinedRect`, `SetFont`, `SetTextColor`, `SetTextPos`, `DrawText`,
  `#!lua CreateFont(name, { font, size, weight })`, `#!lua GetTextSize(text)` (an **estimate**: no font metrics are available).
- `TEXT_ALIGN_LEFT/CENTER/RIGHT/TOP/BOTTOM`, `#!lua ScrW()`, `#!lua ScrH()` (UI units, the same units HUDPaint draws in).
- GMod font names work: `DermaDefault`, `DermaDefaultBold`, `DermaLarge`, `Trebuchet18/24`, `ChatFont`, `TargetID`,
  `TargetIDSmall`, `CloseCaption_Normal/Bold`, `GModNotify`, `HUDNumber5`, …
- These functions only work inside those hooks (otherwise: a Lua error). Drawing is mapped onto reused panels that
  are only restyled when what you draw changes; limits: 256 `Start3D2D` blocks and 6000 draw calls per frame.

**Retained 3D panels.** For signs that don't change every frame, or anything built with normal UI panels:

```lua
local p = ui.CreateWorld({ parent = ent, pos = Vector(0, 0, 40), ang = Angle(0, 0, 90), scale = 0.08,
                           width = 400, height = 100, facecamera = true })
p:SetStyle("background-color: rgba(0,0,0,0.8); justify-content: center; align-items: center;")
ui.Create("label", p):SetText("Shop")
```

Options: `pos`, `ang` (same convention as `#!lua cam.Start3D2D`), `scale` (units per pixel, default 0.1), `width`/`height` (CSS pixels), `parent` (Entity or Player: follows it; `pos`/`ang` are then relative), `facecamera`, `anchor` (`"center"` or `"topleft"`), `classes`.

Methods: `SetWorldPos`, `SetWorldAngles`, `SetWorldScale`, `#!lua AttachTo(ent|nil [, offset [, ang]])`, `#!lua SetFaceCamera(b)`, plus every normal panel method. Styles from `#!lua ui.AddStyle` apply here too. Limit: 512 world panels.


