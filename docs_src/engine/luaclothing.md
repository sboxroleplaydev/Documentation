---
description: "Player clothing and skin (citizen model only)."
---

# LuaClothing

Source: `Code/Framework/Scripting/Api/LuaClothing.cs`

Player clothing and skin (citizen model only).

Player methods (setters: server):
```lua
ply:SetOutfit({ "models/citizen_clothes/hat/fedora/fedora.clothing", { "…/hoodie.clothing", 0.4 }, ... } | nil)
    nil = the player's own Steam avatar outfit; {} = nothing but underwear. A tint (0-1) is optional per item.
ply:GetOutfit()   -- → list of paths, or nil when wearing their own avatar
ply:AddClothing(path [, tint])
ply:RemoveClothing(path)
ply:ClearClothing()
ply:ResetClothing()
ply:SetSkinTone(0-1 | nil)
ply:GetSkinTone()
ply:SetBodyHeight(0-1 | nil)
ply:GetBodyHeight()
```

Library (both realms):
```lua
clothing.GetAll([category])   -- → { { path, title, subtitle, category, tintable }, ... }
clothing.GetCategories()
clothing.IsValid(path)
clothing.GetTitle(path)
```

Items are .clothing paths (204 ship with s&box under models/citizen_clothes/) or mounted package idents.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
