---
description: "UI components (client) on top of the framework's ui library, in one modern dark style (blurred glass, blue accent)."
---

# base: module `ui`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/ui/`

## `cl_ui.lua` (client)

UI components (client) on top of the framework's ui library, in one modern dark style (blurred glass, blue accent).
Every component returns a table { Root = panel, ... } with methods; Root is a normal ui panel (SetVisible, Remove...).

```lua
ui.Window(title, { width, height, onClose })   -- -> w.Body (put content here), w:Close(), w:SetTitle(t)
ui.Button(parent, text, fn [, style])   -- style: "primary" | "danger" | nil
ui.CheckBox(parent, label, checked, fn(on))   -- -> :SetChecked(b) :GetChecked()   -- (a switch)
ui.Slider(parent, label, min, max, value, fn(v) [, decimals])   -- -> :SetValue(v) :GetValue()   -- (drag or type)
ui.NumberEntry(parent, value, fn(v) [, min, max])
ui.TextField(parent, label, text, fn(text) [, placeholder])
ui.ColorPicker(parent, color, fn(color) [, { alpha = true }])   -- -> :SetColor(c) :GetColor()
ui.ComboBox(parent, label, options, value, fn(value))   -- options = { { label, value }, ... }
ui.Tabs(parent, tabs, active, fn(id))   -- tabs = { { id, label }, ... } -> :Select(id); tabs.Body
ui.Category(parent, title, expanded)   -- -> c.Body, :SetExpanded(b)   -- (collapsible)
ui.ProgressBar(parent, fraction [, text])   -- -> :SetFraction(f [, text])
ui.Tile(parent, image, title, fn [, size])   -- icon tile (image: "thumb:<model>", a URL, a texture path)
ui.Label(parent, text [, class])
ui.Divider(parent)
```

Classes are prefixed "rpui-"; restyle them with ui.AddStyle.

Functions defined:

- `ui.Label(parent, text, class)`
- `ui.Divider(parent)`
- `ui.Button(parent, text, fn, style)`
- `ui.Window(title, opts)`
- `ui.CheckBox(parent, label, checked, fn)`
- `ui.NumberEntry(parent, value, fn, min, max)`
- `ui.Slider(parent, label, min, max, value, fn, decimals)`
- `ui.TextField(parent, label, text, fn, placeholder)`
- `ui.ColorPicker(parent, color, fn, opts)`
- `ui.ComboBox(parent, label, options, value, fn)`
- `ui.Tabs(parent, tabs, active, fn)`
- `ui.Category(parent, title, expanded)`
- `ui.ProgressBar(parent, fraction, text)`
- `ui.Tile(parent, image, title, fn, size)`
- `ui.MaterialTile(parent, material, title, fn, size)`
- `ui.MaterialGrid(parent, materials, selected, fn, size)`
