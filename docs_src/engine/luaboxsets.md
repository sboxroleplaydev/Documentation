---
description: "Box sets: up to 64 static boxes (walls of glass, fences, panels ...) that are ONE object - one networked entity, one"
---

# LuaBoxSets

Source: `Code/Framework/Scripting/Api/LuaBoxSets.cs`

Box sets: up to 64 static boxes (walls of glass, fences, panels ...) that are ONE object - one networked entity, one
mesh, one static collider - instead of one entity per box. Single boxes can be switched off and on (broken glass, opened barriers) and only that costs anything: one small rebuild of the set's mesh and collider. What the boxes mean
is up to Lua; this is only what Lua can't do itself (many solid boxes without many objects).

Server:
```lua
boxset.Create(class, { boxes = { cx, cy, cz, yaw, sx, sy, sz, ... }, material = "x.vmat", surface = "glass" }) -> Entity
seven numbers per box (centre in world units, yaw in degrees, size along the box's own forward/right/up), 1-64 boxes
ent:SetBoxesActive(first, count, bool)   -- boxes first .. first+count-1 (1-based) present or gone (no mesh, no collision)
ent:GetBoxActive(i) -> bool
ent:GetBoxCount() -> number
```

Joining clients get the set from the network (spec and an on/off bit mask); a change of one box is 8 bytes.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
