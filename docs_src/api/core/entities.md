---
description: "Entities: Server: ents.Create(class, { model, pos = Vector, ang = Angle, scale, physics = bool, tint = Color, size = Vector, offset = Vector }). model may..."
---

# Entities

- **Server:** `#!lua ents.Create(class, { model, pos = Vector, ang = Angle, scale, physics = bool, tint = Color, size = Vector, offset = Vector })`. `model` may be a model path or a **mounted package ident** (`"fish.barrel"`), in which case the package's main model is used;

    packages come from `"packages"` in gamemode.json or `"Packages"` in framework.json. `size` stretches the model to exact dimensions, and `offset` moves the visible/solid part away from the entity's origin (for example a door whose origin is its hinge).

    Then use `ent:SetPos/SetAngles/SetColor/Remove` and the NW setters.

- **Both:** `#!lua ents.GetAll()`, `#!lua ents.FindByClass(c)`, `#!lua ents.FindInSphere(pos, r)`, and on an entity
  `IsValid/GetClass/GetId/GetPos/GetAngles/GetModel/GetKeyValue(k)` plus the NW getters.
- **Traces:** `#!lua util.TraceLine({ start, endpos, filter })`.
- **Map entities:** add a `LuaEntity` component in the editor with `Class` (e.g. `rp_door`) and `KeyValues`
  (`title=Shop;price=50`), and make the object networked so its movement replicates.

