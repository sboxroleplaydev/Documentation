---
description: "Beams, glows and outlines: render.DrawBeamEx(points, opts) (inside PostDraw…Renderables): a smooth spline through 2–32 points. Options:"
---

# Beams, glows and outlines
<span class="realm realm-client">Client</span>

- `#!lua render.DrawBeamEx(points, opts)` (inside PostDraw…Renderables): a smooth spline through 2–32 points. Options:
  `width` or `widths = { start, middle, end }`, `color`, `brightness` (1–8, glows), `texture`
  (e.g. `"textures/beams/beam_crack_01.vtex"`, ships with s&box), `scroll`, `unitsPerTexture`, `additive` (default true).
- `#!lua render.DrawSprite(pos, size, color [, brightness [, texture]])`: a camera-facing glow (default: a soft flare).
- `#!lua ent:SetHighlight(color | nil [, width [, throughWalls [, glow]]])` (entities and players, this client only): an outline, hidden behind other objects unless `throughWalls`; `glow = true` draws a Garry's Mod halo instead: in screen space, like `#!lua halo.Add` (mask of the visible model → 7×7 blur → added onto the screen outside the model; `#!lua RpHalo.cs` + `Assets/shaders/rp_halo_*.shader`).

    All halos of a frame share the last colour given.


