---
description: "DarkRP items (shared definitions). What an item does when used is defined server-side in svitems.lua."
---

# darkrp: module `items`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/items/`

## `sh_items.lua` (shared)

DarkRP items (shared definitions). What an item does when used is defined server-side in sv_items.lua.
```lua
id (key)
name
description
price   -- 0 = not sold
stack   -- max per player
color
category
model   -- shown when dropped; without one it is a small box in the item's colour
```

Functions defined:

- `DarkRP.createItem(id, def)`
- `DarkRP.ItemPrice(item, ply)`

## `sv_items.lua` (server)

Items: inventory (in server profiles), shop purchases, use, drop and pick up.

Functions defined:

- `DarkRP.UseItemEffect(ply, item)`
- `DarkRP.Heal(ply, amount)`
- `DarkRP.GetItemCount(ply, id)`
- `DarkRP.CanGiveItem(ply, id, count)`
- `DarkRP.GiveItem(ply, id, count)`
- `DarkRP.TakeItem(ply, id, count)`
- `DarkRP.PickUpItem(ply, ent)`
