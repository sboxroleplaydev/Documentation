---
description: "keybind.Register('mygm.inventory', { key = 'i', label = 'Inventory', category = 'My gamemode', hint = true,"
---

# Keybinds
<span class="realm realm-client">Client</span>

```lua
keybind.Register("mygm.inventory", { key = "i", label = "Inventory", category = "My gamemode", hint = true,
    pressed = function() OpenInventory() end })
keybind.Register("mygm.use", { action = "Use", label = "Interact", hint = true })   -- follows the game's settings
```

- `key` = a raw key players can rebind in the help screen (saved per player); `action` = an input action from the
  game's settings. F1–F12 and Escape are reserved by s&box and refused.
- `#!lua keybind.GetAll()` → `{ { id, label, category, key, keyname, action, hint, rebindable }, ... }`,
  `#!lua GetKey(id)`, `#!lua GetKeyName(id)`, `#!lua IsDown(id)`, `#!lua SetKey(id, key or nil)`, `#!lua Remove(id)`, `#!lua KeyName(keyOrAction)`,
  `#!lua Capture(function(key) end)` (the next key pressed; nil if cancelled). Hooks `#!lua KeybindPressed(id)` / `#!lua KeybindReleased(id)`.
- `#!lua panel:SetKeyGlyph(keyOrAction)` shows the engine's glyph for a key.
- **Base gamemode:** a key hints panel (bottom right) shows every bind with `hint = true` (toggle K;
  `GM.KeyHintsEnabled = false` turns it off, `#!lua GM:KeyHintsFilter(bind)` filters), and the help screen (H) lists all
  binds with "Change"/"Reset" for rebindable ones plus `#!lua GM:HelpSections()`. `#!lua GM:CreateKeyCap(parent, text)` makes
  a key cap for your own HUD.

