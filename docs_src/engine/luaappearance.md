---
description: "Models, materials and textures for Lua. Asset references are engine paths ('models/dev/box.vmdl', 'materials/dev/devmeasuregeneric01.vmat') or sbox.game..."
---

# LuaAppearance

Source: `Code/Framework/Scripting/Api/LuaAppearance.cs`

Models, materials and textures for Lua. Asset references are engine paths ("models/dev/box.vmdl", "materials/dev/dev_measuregeneric01.vmat") or sbox.game package idents ("fish.barrel" = that package's main asset;
it must be mounted, see the content library).

Entity and Player methods (setters: server, or the client that owns a ClientsideModel):
```lua
SetModel(model)
GetModel()
SetMaterial(mat|"")
GetMaterial()
SetSkin(n)
GetSkin()
SkinCount()
SetBodygroup(name|index, value)
GetBodygroup(name|index)
GetBodygroups()
SetNoDraw(b)
GetNoDraw()
SetNotSolid(b)
IsNotSolid()
GetModelBounds() → mins
maxs
SetModelScale(s)
GetModelScale()
-- Player only
SetColor(Color)
GetColor()
-- Globals
util.IsValidModel(model)
util.IsValidMaterial(mat)
Model(path) / Material(path)   -- validated path strings
```

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
