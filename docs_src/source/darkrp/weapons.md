---
description: "DarkRP weapon shop (shared definitions). Weapons are SWEP classes from base (or any addon)."
---

# darkrp: module `weapons`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/weapons/`

## `sh_weapons.lua` (shared)

DarkRP weapon shop (shared definitions). Weapons are SWEP classes from base (or any addon).
```lua
DarkRP.createWeapon(class, { price, allowed = { TEAM_GUN, ... } (nil = everyone), category, description })
DarkRP.createAmmo(ammoType, { name, price, amount, allowed })
```

Bought weapons are given straight away; they are lost on death and job change, like GMod DarkRP.

Functions defined:

- `DarkRP.createWeapon(class, def)`
- `DarkRP.createAmmo(ammo, def)`
- `DarkRP.CanBuyShopWeapon(ply, def)`
- `DarkRP.WeaponName(class)`

## `sv_weapons.lua` (server)

DarkRP weapon shop (server): buying weapons and ammo from the F4 shop or /buy <class|ammo>.
