---
description: "GMod-style weapons, written once in a shared file (gamemode, module or addon). Base loads every"
---

# Weapons

GMod-style weapons, written once in a **shared** file (gamemode, module or addon). Base loads every
`gamemode/weapons/sh_*.lua` (`#!lua weapons.LoadFolder(dir)` for your own folders).

```lua
local SWEP = {}
SWEP.PrintName = "SMG"   SWEP.Category = "Weapons"   SWEP.Slot = 2   SWEP.SlotPos = 0   SWEP.Spawnable = true
SWEP.HoldType = "smg"                   -- pistol, revolver, smg, ar2, rifle, shotgun, rpg, physgun, knife, melee, fists, grenade, ...
SWEP.Handedness = "both"                -- "right", "left"
SWEP.WorldModel = "facepunch.w_mp5"     -- model path or package ident; position in the hand comes from presets or:
SWEP.ViewModel = "facepunch.v_mp5"      -- "arms" = arms only (fists)
-- SWEP.WorldModelOffset = Vector(), SWEP.WorldModelAngles = Angle()   (tune live: rp weapon_offset x y z [p y r])
-- SWEP.ViewModelOffset = Vector(forward, left, up), SWEP.ViewModelBodygroups = n
-- SWEP.MuzzleFlash = "facepunch.rifle_muzzleflash"   -- prefab path / package ident, "none"; nil = the engine's default
SWEP.ReloadTime = 2.0   SWEP.ReloadSound = "drakefruit.rifle_reload"
SWEP.Primary = { ClipSize = 30, DefaultClip = 90, Automatic = true, Ammo = "smg1",
                 Damage = 9, Delay = 0.075, Cone = 0.03, NumShots = 1, Force = 1, Distance = 8192, Sound = "vidya.smg-shoot" }
weapons.Register(SWEP, "weapon_smg")
```

- **Prediction (like GMod):** `PrimaryAttack`, `SecondaryAttack`, `Reload` and `Think` run on the server **and** on the shooting player's client. The client plays animation, sound, tracer and muzzle flash at once and predicts the clip;

    the server decides hits, damage and ammo and sends the effects to everyone else. `SWEP.Predicted = false`: server only (the physics gun and tool gun work like that).

- **Hooks on the weapon:** `Initialize`, `Deploy`, `Holster` (both realms), `PrimaryAttack`, `SecondaryAttack`,
  `Reload`, `Think`; client: `DrawHUD`, `#!lua DoDrawCrosshair(x, y)` (true hides the default crosshair).
- **Helpers:** `#!lua self:ShootBullet(damage, num, cone)`, `#!lua self:MeleeAttack(range, damage, force)` (returns the trace;
  plays `b_attack_has_hit` on a hit), `#!lua self:DefaultReload()`, `#!lua self:CanPrimaryAttack()`, `#!lua self:TakePrimaryAmmo(n)`,
  `#!lua self:EmitSound(path [, vol, pitch])`, `#!lua self:SendWeaponAnim(param)`, `Clip1/SetClip1`, `Ammo1`,
  `Get/SetNextPrimaryFire`, `Get/SetNextSecondaryFire`, `IsReloading`, `GetOwner`, `IsCarriedByLocalPlayer`.
- **Sprinting (GMod-like):** while you sprint the view model drops into its sprint pose, but it comes up while an attack button is held, for 0.5 s after every shot or swing, and while reloading, so a gun never fires from the lowered pose (you keep your sprint speed). `SWEP.SprintPose = false` keeps the gun up all the time (physics gun, tool gun).

    A weapon can still force it with `#!lua ply:SetViewModelParam("b_sprint", ...)`.

- **Options:** `ReloadShells = true` + `ReloadShellTime`, `ReloadStartTime`, `ReloadShellSound` (shotgun: one round at a
  time, firing interrupts), `AllowDrop = false`, `DeployTime`, `DrawAmmo`, `DrawCrosshair`, `HitSound`/`SwingSound`
  (melee), `#!lua Primary.EmptySound`.
- **Ammo:** `#!lua game.AddAmmoType({ name, maxcarry })`, `#!lua game.GetAmmoMax(name)`. Built-in: pistol, 357, smg1, ar2,
  buckshot, sniper, rpg_round, grenade.
- **Players (server):** `#!lua ply:Give(class [, noAmmo])`, `StripWeapon`, `StripWeapons`, `SelectWeapon`, `GetActiveWeapon`, `GetWeapon`, `GetWeapons`, `#!lua DropWeapon([class])`, `GiveAmmo/SetAmmo/RemoveAmmo(n, type)`, `StripAmmo`, `FireBullets{ Num, Src, Dir, Spread, Damage, Force, Distance, Tracer, Inflictor, Callback }`, `#!lua WeaponButtonDown(1|2|3)` (attack, attack2, reload held right now).

    Shared: `HasWeapon`, `GetAmmoCount`, `GetActiveWeaponClass`, `GetWeaponClasses`.

- **Explosions (server):** `#!lua util.BlastDamage(inflictor, attacker, pos, radius, damage)`: players take damage that falls
  off with distance unless a wall is in between; physics props are pushed (`EntityTakeDamage` can take over).
- **Hooks:** `#!lua PlayerLoadout(ply)` (`#!lua GM.DefaultLoadout`), `#!lua PlayerCanPickupWeapon(ply, class)`,
  `#!lua PlayerSwitchWeapon(ply, old, new)`, `#!lua PlayerCanDropWeapon(ply, weapon)`, `#!lua EntityTakeDamage(ent, dmg, attacker, inflictor, pos)`.
- **Visuals (C#):** `ply:SetWeaponModels{ world, view, hold, hand, offset, angles, viewBodygroups, viewOffset, lowered, muzzleFlash }`
  (server), `#!lua ply:WeaponAnim(param [, skipOwner])`, `#!lua ply:GetMuzzlePos()`; client, `#!lua LocalPlayer()` only:
  `#!lua ply:SetViewModelParam(name, bool|number|nil)` (whole numbers are also set as int parameters, e.g. `"ironsights"`),
  `#!lua ply:SetViewModelVisible(b)`.
- **Built-in weapons:** `weapon_fists`, `weapon_crowbar`, `weapon_knife`, `weapon_pistol`, `weapon_357`, `weapon_smg`,
  `weapon_rifle`, `weapon_shotgun`, `weapon_sniper` (right click: scope), `weapon_grenade`, `weapon_physgun`, `gmod_tool`.
- **Commands:** `/giveweapon <class>` (permission `#!lua weapons.give.self`), `/dropweapon` (also `rp dropweapon`).

