---
description: "Asset references are engine paths ('models/dev/box.vmdl', 'materials/dev/reflectivity30.vmat') or mounted"
---

# Models, materials and textures

Asset references are engine paths (`"models/dev/box.vmdl"`, `"materials/dev/reflectivity_30.vmat"`) or **mounted
package idents** (`"fish.barrel"` = the package's main asset; see the `content` library). Invalid paths, `..`, missing
files and unmounted packages raise a Lua error.

**Entity and Player methods.** Setters run on the server (and replicate to every player), or on the client for its own
`ClientsideModel`. Getters work in both realms.

| Method | Notes |
|---|---|
| `#!lua SetModel(model)` / `#!lua GetModel()` | Entities: the collider follows the new model. Players: clothing is taken off for non-citizen models and put back when the default model returns |
| `#!lua SetMaterial(mat)` / `#!lua GetMaterial()` | Overrides every material; `""` or nil restores the model's own |
| `#!lua SetSkin(n)` / `#!lua GetSkin()` / `#!lua SkinCount()` | Skin = the model's material group (0 = default) |
| `#!lua SetBodygroup(name or index, value)` / `#!lua GetBodygroup(name or index)` / `#!lua GetBodygroups()` | `#!lua GetBodygroups()` → `{ { id, name, num }, ... }` like GMod |
| `#!lua SetNoDraw(b)` / `#!lua GetNoDraw()` | Hide without removing |
| `#!lua SetNotSolid(b)` / `#!lua IsNotSolid()` | Server, entities: things pass through it (its colliders become triggers on every machine; shape and mass stay) |
| `#!lua GetModelBounds()` | → `mins, maxs` (Vectors) |
| `#!lua SetModelScale(s)` / `#!lua GetModelScale()` | Entities only (0.05–20) |
| `#!lua SetColor(Color)` / `#!lua GetColor()` | Entities and players |

`#!lua ents.Create` also takes `material = "…vmat"`.

**Globals:** `#!lua Model(path)` and `#!lua Material(path)` validate and return the resolved path (GMod-style),
`#!lua util.IsValidModel(path)`, `#!lua util.IsValidMaterial(path)`.

**Client-only models:** `#!lua ClientsideModel(model)` (also `#!lua ents.CreateClientProp(model)`) creates an entity that exists
only on this client: not networked, no collision, removed when the client realm stops. Move and style it with the
normal methods (`SetPos`, `SetAngles`, `SetMaterial`, `SetColor`, `Remove`, …).

**Textures in the UI:** `#!lua ui.Create("image")`, then `#!lua img:SetImage(src)`. On any other panel, `SetImage` sets the background image (size it with CSS, e.g. `background-size: cover`). `src` is an `https://` URL, an image path (`.png`, `.jpg`, `.vtex`, `.svg`), a mounted package ident, or `"avatar:<steamid64>"`. `#!lua panel:SetAvatar(ply or steamid64)` shows a player's Steam avatar.

Plain `http://` is refused.


