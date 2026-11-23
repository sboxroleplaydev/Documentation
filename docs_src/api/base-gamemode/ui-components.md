---
description: "Ready-made controls on top of ui panels, in one modern style (blurred glass, blue accent). Each returns a table with"
---

# UI components
<span class="realm realm-client">Client</span>

Ready-made controls on top of `ui` panels, in one modern style (blurred glass, blue accent). Each returns a table with
`Root` (a normal panel) and methods.

```lua
local w = ui.Window("Settings", { width = 480, height = 420 })
ui.CheckBox(w.Body, "Show names", true, function(on) end)
ui.Slider(w.Body, "Volume", 0, 100, 50, function(v) end)
ui.ColorPicker(w.Body, Color(255, 120, 0), function(c) end, { alpha = true })
ui.ComboBox(w.Body, "Mode", { { "Fast", "fast" }, { "Quality", "q" } }, "fast", function(v) end)
ui.Button(w.Body, "Save", function() w:Close() end, "primary")
```

`#!lua ui.Window(title, { width, height, onClose })` (`.Body`, `:Close()`, `:SetTitle()`), `#!lua ui.Button(parent, text, fn [, "primary"|"danger"])`, `#!lua ui.CheckBox` (switch; `:SetChecked/GetChecked`), `#!lua ui.Slider(parent, label, min, max, value, fn [, decimals])` (drag or type; `:SetValue/GetValue`), `#!lua ui.NumberEntry`, `#!lua ui.TextField(parent, label, text, fn [, placeholder])`, `#!lua ui.ColorPicker(parent, color, fn [, { alpha }])` (saturation/brightness square, hue and alpha bars, hex field, swatches; `:SetColor/GetColor`), `#!lua ui.ComboBox`, `#!lua ui.Tabs(parent, { { id, label } }, active, fn(id, body))` (`.Body`, `:Select`), `#!lua ui.Category(parent, title, expanded)` (collapsible, `.Body`), `#!lua ui.ProgressBar(parent, f [, text])`, `#!lua ui.Tile(parent, image, title, fn [, size])`, `#!lua ui.Label`, `#!lua ui.Divider`;

`#!lua ui.HSVToRGB(h, s, v)`, `#!lua ui.RGBToHSV(r, g, b)`. Classes start with `rpui-`; restyle them with `#!lua ui.AddStyle`.


