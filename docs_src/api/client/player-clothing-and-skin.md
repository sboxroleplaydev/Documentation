---
description: "Every player wears the outfit they picked in the s&box main menu by default, in any gamemode (base included), with no Lua needed. Setters are server-side..."
---

# Player clothing and skin

**Every player wears the outfit they picked in the s&box main menu by default**, in any gamemode (base included), with no Lua needed. Setters are server-side and replicate to everyone; they work on the citizen model (another model via `SetModel` takes the clothes off).

A forced outfit (`SetOutfit`) keeps the player's own skin/face item and skin tone unless you set them; `#!lua ResetClothing()` goes back to the menu outfit. DarkRP: jobs without `outfit` (Citizen) wear the player's own clothes, jobs with one wear it.


| Method | Notes |
|---|---|
| `#!lua ply:SetOutfit({ path, { path, tint }, ... } or nil)` | `nil` = the player's own Steam avatar outfit; `{}` = underwear only; tint 0–1 per item |
| `#!lua ply:GetOutfit()` | list of paths, or nil for their own avatar |
| `#!lua ply:AddClothing(path [, tint])`, `#!lua ply:RemoveClothing(path)`, `#!lua ply:ClearClothing()`, `#!lua ply:ResetClothing()` | `ResetClothing` = own avatar, default skin and height |
| `#!lua ply:SetSkinTone(0–1 or nil)`, `#!lua GetSkinTone()`, `#!lua ply:SetBodyHeight(0–1 or nil)`, `#!lua GetBodyHeight()` | |

`#!lua clothing.GetAll([category])` → `{ { path, title, subtitle, category, tintable }, ... }`, `#!lua clothing.GetCategories()`,
`#!lua clothing.IsValid(path)`, `#!lua clothing.GetTitle(path)`. Paths are `.clothing` files (204 ship with s&box under
`models/citizen_clothes/`, e.g. `models/citizen_clothes/hat/police_hat/police_hat.clothing`) or mounted package
idents. At most 32 items per outfit.

