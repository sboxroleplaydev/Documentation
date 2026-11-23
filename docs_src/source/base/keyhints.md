---
description: "Key hints: a small panel (bottom right) listing the keybinds registered with hint = true, as key caps."
---

# base: module `keyhints`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/keyhints/`

## `cl_keyhints.lua` (client)

Key hints: a small panel (bottom right) listing the keybinds registered with hint = true, as key caps.
```lua
GM.KeyHintsEnabled = false      in a derived gamemode turns the panel off completely
GM:KeyHintsFilter(bind)   -- return false to hide a bind from the panel
```

Players toggle it with the "Toggle key hints" bind (K by default); the choice is remembered (cookie).

Functions defined:

- `GM:KeyHintsFilter(bind)`
- `GM:KeyHintsCreate()`
- `GM:KeyHintsToggle()`
- `GM:CreateKeyCap(parent, keyName)`
- `GM:KeyHintsThink()`
