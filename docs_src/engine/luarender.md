---
description: "Weapon visuals and immediate 3D lines for Lua."
---

# LuaRender

Source: `Code/Framework/Scripting/Api/LuaRender.cs`

Weapon visuals and immediate 3D lines for Lua.

Client: `render.DrawBeam(start, end, width [, color])` / `render.DrawLine(start, end [, color])`, only inside
PostDrawOpaqueRenderables / PostDrawTranslucentRenderables (like GMod). Pooled line renderers, max 512 per frame.
Players: `ply:SetWeaponModels{...}` (server), `ply:WeaponAnim(param [, skipOwner])`, `ply:GetMuzzlePos()` - see `RpHeldWeapon`.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
