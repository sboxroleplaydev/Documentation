---
description: "View and mouse: LocalPlayer():SetFOV(fov [, seconds]) zooms (0 = back to the player's own setting); GetFOV()."
---

# View and mouse
<span class="realm realm-client">Client</span>

- `#!lua LocalPlayer():SetFOV(fov [, seconds])` zooms (0 = back to the player's own setting); `#!lua GetFOV()`.
- `#!lua input.GetMouseDelta()` → x, y (this frame), `#!lua input.GetMouseWheel()` → n, `#!lua input.SetLookScale(scale)` (0 = view
  locked, 1 = normal). Zoom and look scale reset when the client realm stops.

