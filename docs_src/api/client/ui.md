---
description: "ui.AddStyle([[ .box { position: absolute; left: 20px; top: 20px; background-color: rgba(0,0,0,0.8); pointer-events: all; } ]])"
---

# UI
<span class="realm realm-client">Client</span>

```lua
ui.AddStyle([[ .box { position: absolute; left: 20px; top: 20px; background-color: rgba(0,0,0,0.8); pointer-events: all; } ]])
local box = ui.Create("panel", nil, "box")
local name = ui.Create("label", box); name:SetText("Hello")
local entry = ui.Create("textentry", box); entry:OnSubmit(function(text) print(text) end)
local btn = ui.Create("label", box, "button"); btn:SetText("Click"); btn:OnClick(function() print("clicked") end)
```

- **Kinds:** `panel`, `label`, `button`, `textentry`, `image`.
- **Panel methods:**
    - classes and style: `AddClass/RemoveClass/SetClass/HasClass`, `#!lua SetStyle(css)`;
    - text: `SetText/GetText`, `SetPlaceholder`, `SetMaxLength`;
    - input: `Focus/HasFocus`, `#!lua OnClick(fn)`, `#!lua OnSubmit(fn(text))`, `#!lua OnChange(fn(text))`;
    - images: `#!lua SetImage(src)`, `#!lua SetAvatar(ply or steamid64)` (see "Models, materials and textures");
    - images: also `"thumb:<model path or model package>"` (the model's icon; in the editor the engine's thumbnail, in a
    published game rendered by the framework at runtime - a few per frame, cached - since most models ship none);
    - visibility and structure: `SetVisible/IsVisible`, `Clear`, `Remove`, `IsValid`, `ScrollToBottom`, `ScrollToTop`,
    `#!lua SetParent(panel|nil)`, `#!lua GetChildCount()`, `#!lua SetTooltip(text|nil)`;
    - mouse: `OnMouseDown/OnMouseUp(fn(x, y, button))` (x, y = 0-1 fractions of the panel, button "left"/"right"/"middle"),
    `OnMouseEnter/OnMouseLeave(fn)`, `#!lua OnRightClick(fn)`, `#!lua GetMousePos()` → x, y (fractions), `#!lua GetSize()` → w, h
    (screen pixels, 0 before the first layout), `#!lua IsHovered()`.
- **Library:** `#!lua ui.AddStyle(css)`, `#!lua ui.SetCursor(visible)`, `#!lua ui.IsTyping()`, `#!lua ui.ScreenSize()`, `#!lua ui.IsMouseDown([button])`.
- **Components:** see "UI components" (windows, sliders, colour picker, ...).
- **Root:** covers the screen with `pointer-events: none`; give interactive panels `pointer-events: all`.
- **CSS precedence:** stylesheets are not guaranteed to apply in the order added. To override another gamemode's rule,
  use a more specific selector (e.g. `.lua-root .chat`).
- **Limits:** 4000 panels, 128 KB of CSS.
- **Minimal HUD text:** `#!lua hud.SetLine(id, text)` / `#!lua hud.RemoveLine(id)` / `#!lua hud.Notify(text [, s])` still exist.

