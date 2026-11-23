---
description: "input.IsKeyDown(key), input.WasKeyPressed(key) (this frame), input.WasKeyReleased(key) and input.LookupBinding(action) (→ the key bound to an input..."
---

# Keyboard
<span class="realm realm-client">Client</span>

`#!lua input.IsKeyDown(key)`, `#!lua input.WasKeyPressed(key)` (this frame), `#!lua input.WasKeyReleased(key)` and `#!lua input.LookupBinding(action)` (→ the key bound to an input action, e.g. `"f4"`). Key names are s&box names: `"m"`, `"f4"`, `"tab"`, `"enter"`, `"space"`, `"mouse1"`, … `IsKeyDown`/`WasKeyPressed` return false while a Lua text box has focus.

**s&box reserves F1–F12 and Escape for the engine**: games never see them (not as actions, not as raw keys), in the editor or in the real game. That's why the GMod-style F1–F4 actions default to H, N, B and M.


