---
description: "Roleplay Framework core library (shared). Loaded before any gamemode in both realms."
---

# `framework/sh_core.lua`

Roleplay Framework core library (shared). Loaded before any gamemode in both realms.
Garry's Mod-style helpers implemented in plain Lua on top of the sandboxed runtime.

Functions defined:

- `hook.Add(event, id, fn)`
- `hook.Remove(event, id)`
- `hook.GetTable()`
- `hook.Run(event, ...)`
- `ColorMeta:__tostring()`
- `ColorMeta.__eq(a, b)`
- `ColorMeta:IsValid()`
- `VectorMeta.__add(a, b)`
- `VectorMeta.__sub(a, b)`
- `VectorMeta.__unm(a)`
- `VectorMeta.__eq(a, b)`
- `VectorMeta.__mul(a, b)`
- `VectorMeta.__div(a, b)`
- `VectorMeta:__tostring()`
- `VectorMeta:Length()`
- `VectorMeta:Distance(o)`
- `VectorMeta:Dot(o)`
- `VectorMeta:LengthSqr()`
- `VectorMeta:Cross(o)`
- `VectorMeta:Normalize()`
- `VectorMeta:Angle()`
- `VectorMeta:ToScreen()`
- `VectorMeta:GetNormalized()`
- `AngleMeta.__add(a, b)`
- `AngleMeta.__sub(a, b)`
- `AngleMeta.__eq(a, b)`
- `AngleMeta:__tostring()`
- `AngleMeta:Forward()`
- `AngleMeta:Right()`
- `AngleMeta:Up()`
- `AngleMeta:RotateAroundAxis(axis, degrees)`
- `VectorMeta:Rotate(ang)`
- `math.Clamp(n, lo, hi)`
- `math.Round(n, decimals)`
- `string.Trim(s)`
- `string.StartWith(s, prefix)`
- `string.EndsWith(s, suffix)`
- `string.Explode(separator, s, usePatterns)`
- `table.Count(t)`
- `table.HasValue(t, value)`
- `table.Copy(t, seen)`
- `table.GetKeys(t)`
- `table.IsEmpty(t)`
