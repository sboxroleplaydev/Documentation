---
description: "Physics, coordinates and effects: PhysObj:ComputeShadowControl({ pos, angle, secondstoarrive, maxspeed, maxangular, teleportdistance }) (GMod): moves a"
---

# Physics, coordinates and effects

- `#!lua PhysObj:ComputeShadowControl({ pos, angle, secondstoarrive, maxspeed, maxangular, teleportdistance })` (GMod): moves a
  body towards a target by setting its velocities (carrying, physics guns).
- `#!lua WorldToLocal(pos, ang, originPos, originAng)` / `#!lua LocalToWorld(localPos, localAng, originPos, originAng)` → Vector,
  Angle (GMod). `#!lua ent:WorldToLocal(pos)`, `#!lua ent:LocalToWorld(pos)`, `#!lua ent:WorldToLocalAngles(a)`, `#!lua ent:LocalToWorldAngles(a)`.
- `#!lua Angle:RotateAroundAxis(axis, degrees)` and `#!lua Vector:Rotate(ang)` (in place, like GMod); `#!lua util.RotateAroundAxis(ang, axis, deg)`.
- `#!lua util.TraceLine` results also have `HitNormal`, `Normal`, `StartPos`, `Fraction`.
- **Builder models** ("plastic"): anywhere a model path is accepted, `"builder:<x>x<y>x<z>"` is a box built at runtime, sizes in PHX units (1 = 47.45, GMod's cube1x1x1; each 0.0625-16), GMod-style grey grid (engine core `gray_grid_8`, a cell every 0.25 units like GMod's hunter/myplastic), box collision, light mass.

    Every machine builds the same model from the name - nothing to download. The base spawn menu lists blocks ("Plastic GMod plastic"); the base spawn menu's "Plastic" list has GMod's blocks and plates with their names; add your own with `#!lua spawnmenu.AddPropCategory(name, { "builder:1x8x0.25", { "builder:1x1x1", "my name" }, { header = "Section" } })`.

- `#!lua ent:SetGhost(color | nil)` (client, client-side models): see-through preview look (rp_ghost shader, keeps the model's
  texture, no shadows). `#!lua cam.ToScreen(pos)` → x, y, visible in HUDPaint units; `#!lua Vector:ToScreen()` → { x, y, visible }.
- 3D2D canvases survive their WorldPanel objects being destroyed (they are rebuilt), so a scene change can't break
  `#!lua cam.Start3D2D` drawing.
- `#!lua util.Effect("Blood", pos, scale, dir)`: red droplets along `dir` plus an engine blood decal on the surface behind the hit. `#!lua util.Effect("Impact", pos, scale, dir)`: a bullet/punch decal matching the surface (engine `decals/impact/*`).

    Melee and `FireBullets` use both (blood on players, impact decals elsewhere). Melee hit sounds: `#!lua SWEP.FleshHitSound` (players), `#!lua SWEP.HitSound` / `#!lua SWEP.WorldHitSound` (engine `sounds/impacts/melee/*`).

- `#!lua util.Effect(name, pos [, scale])`: `"Explosion"`, `"Flash"`, `"Sparks"`, `"Freeze"` (short light flashes; Freeze is a
  dim blue glow). Server: everyone sees it.
- **Sounds you control (client, local):** `#!lua local snd = CreateSound(ent | ply, "path.sound")` (GMod's CSoundPatch, follows the entity; a looping sound loops until stopped) → `#!lua snd:Play()`, `#!lua snd:PlayEx(volume, pitch)`, `#!lua snd:Stop()`, `#!lua snd:IsPlaying()`, `#!lua snd:ChangeVolume(v [, seconds])`, `#!lua snd:ChangePitch(p [, seconds])`, `#!lua snd:FadeOut(seconds)`.

    At most 64 exist; they stop when the entity goes or the client realm stops. Keep one per use and reuse it.

- Constraints (server): `constraint.Weld/Ballsocket/Rope/NoCollide`, `GetAll`, `Remove`, `RemoveAll`,
  `#!lua RemoveConstraints(ent, type)`, `HasConstraints`.

