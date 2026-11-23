---
description: "Weapons (client): input, prediction, weapon selection (1-9, 0, mouse wheel), selector, ammo HUD, crosshair and"
---

# base: module `weapons`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/weapons/`

## `cl_weapons.lua` (client)

Weapons (client): input, prediction, weapon selection (1-9, 0, mouse wheel), selector, ammo HUD, crosshair and
tracers. The local player's weapons exist as client objects: PrimaryAttack/SecondaryAttack/Reload run here too
(prediction: animation, sound, tracer and ammo at once; the server decides hits and the real ammo count).
Hide HUD parts with GM:HUDShouldDraw("BaseAmmo" | "BaseCrosshair" | "BaseWeaponSelect").

Functions defined:

- `PLAYER:GetActiveWeapon()`
- `PLAYER:GetWeapon(class)`
- `GM:WeaponSelect(class)`
- `GM:WeaponSelectSlot(slot)`
- `GM:WeaponSelectStep(dir)`
- `GM:WeaponHUDThink()`
- `weapons.Tracers(shooter, hits, predicted)`

## `sh_weapons.lua` (shared)

Weapons (SWEPs), Garry's Mod style. Define one in any shared file (gamemode, module or addon):

```lua
local SWEP = {}
SWEP.PrintName = "Pistol"   SWEP.Slot = 1   SWEP.SlotPos = 0   SWEP.Category = "Weapons"
SWEP.Spawnable = true       SWEP.AdminOnly = false
SWEP.WorldModel = "facepunch.w_usp"   SWEP.ViewModel = "facepunch.v_usp"
SWEP.HoldType = "pistol"    SWEP.Handedness = "right"      -- "both" (default), "right", "left"
SWEP.Primary = { ClipSize = 18, DefaultClip = 54, Automatic = false, Ammo = "pistol", Damage = 12, Delay = 0.12, Cone = 0.015, NumShots = 1, Sound = "vidya.pistol-shoot" }
function SWEP:PrimaryAttack() ... end      -- default: shoot one bullet (see the base weapon below)
weapons.Register(SWEP, "weapon_pistol")
```


PREDICTION (like GMod): PrimaryAttack, SecondaryAttack and Reload run on the server AND on the shooting player's
client. On the client, effects (animation, sound, tracer, muzzle flash) play at once and ammo is predicted; damage, hits and the real ammo count only happen on the server, which sends the effects to everyone else. Write SWEP code
once; use SERVER/CLIENT only for things that must not run on one side. SWEP.Predicted = false: server only.

World models: weapons.WorldModelPresets holds how known models sit in the hand (offsets from Facepunch's sandbox).
Other models: SWEP.WorldModelOffset (Vector) / SWEP.WorldModelAngles (Angle); tune live with "rp weapon_offset".
View models: SWEP.ViewModel = "arms" shows only the arms (fists); SWEP.ViewModelBodygroups sets its bodygroups;
```lua
SWEP.ViewModelOffset = Vector(forward, left, up) shifts it in view space (e.g. to lift a low-held melee weapon).
```

Sprint: the gun drops into the sprint pose while sprinting, but comes up while firing/reloading (GMod-like);
```lua
SWEP.SprintPose = false keeps it up always (physgun, tool gun).
```

Hooks on the weapon: Initialize, Deploy, Holster, PrimaryAttack, SecondaryAttack, Reload, Think;
client: DrawHUD, DoDrawCrosshair(x, y) (return true to hide the default crosshair).
Base files: gamemode/weapons/sh_<class>.lua are loaded automatically (weapons.LoadFolder).

Functions defined:

- `game.GetAmmoMax(name)`
- `BASE:IsValid()`
- `BASE:GetOwner()`
- `BASE:GetClass()`
- `BASE:GetPrintName()`
- `BASE:GetMaxClip1()`
- `BASE:GetPrimaryAmmoType()`
- `BASE:Ammo1()`
- `BASE:Clip2()`
- `BASE:GetNextPrimaryFire()`
- `BASE:GetNextSecondaryFire()`
- `BASE:SetNextPrimaryFire(t)`
- `BASE:SetNextSecondaryFire(t)`
- `BASE:IsReloading()`
- `BASE:IsCarriedByLocalPlayer()`
- `BASE:Clip1()`
- `BASE:SetClip1(n)`
- `BASE:SetClip2(n)`
- `BASE:Initialize()`
- `BASE:Deploy()`
- `BASE:Holster()`
- `BASE:Think()`
- `BASE:DrawHUD()`
- `BASE:DoDrawCrosshair(x, y)`
- `BASE:TakePrimaryAmmo(n)`
- `BASE:CanPrimaryAttack()`
- `BASE:CanSecondaryAttack()`
- `BASE:SendWeaponAnim(param)`
- `BASE:EmitSound(path, volume, pitch)`
- `BASE:ShootEffects()`
- `BASE:ShootBullet(damage, num, cone)`
- `BASE:PrimaryAttack()`
- `BASE:SecondaryAttack()`
- `BASE:MeleeAttack(range, damage, force)`
- `BASE:DefaultReload()`
- `BASE:Reload()`
- `BASE:_StopShellReload()`
- `BASE:_LoadShell()`
- `BASE:_FrameworkThink()`
- `weapons.Register(swep, class)`
- `weapons.Get(class)`
- `weapons.GetStored(class)`
- `weapons.GetList()`
- `weapons.LoadFolder(dir)`
- `weapons.GetWorldModelPlacement(swep)`
- `weapons.GetViewModelBodygroups(swep)`
- `weapons.CreateInstance(class, owner)`
- `PLAYER:GetAmmoCount(ammo)`
- `PLAYER:GetActiveWeaponClass()`
- `PLAYER:GetWeaponClasses()`
- `PLAYER:HasWeapon(class)`
- `PLAYER:FireBullets(b)`

## `sv_weapons.lua` (server)

Weapons (server): inventory, switching, firing, ammo, dropping/pickup, loadout.
```lua
ply:Give(class [, noAmmo])
ply:StripWeapon(class)
ply:StripWeapons()
ply:SelectWeapon(class)
ply:GetActiveWeapon()
ply:GetWeapon(class)
ply:GetWeapons()
ply:DropWeapon([class])
ply:GiveAmmo(n, type)
ply:SetAmmo(n, type)
ply:RemoveAmmo(n, type)
ply:StripAmmo()
ply:FireBullets(bullet)
ply:WeaponButtonDown(1|2|3)   -- attack, attack2, reload held
util.BlastDamage(inflictor, attacker, pos, radius, damage)
-- Hooks
PlayerLoadout(ply)   -- GM: gives GM.DefaultLoadout
PlayerCanPickupWeapon(ply, class) -> false blocks
PlayerSwitchWeapon(ply, old, new) -> true blocks
PlayerCanDropWeapon(ply, weapon) -> false blocks
EntityTakeDamage(ent, damage, attacker, inflictor, hitPos) for bullets/melee hitting entities   -- true = handled
```

Functions defined:

- `PLAYER:WeaponButtonDown(b)`
- `PLAYER:GetActiveWeapon()`
- `PLAYER:GetWeapon(class)`
- `PLAYER:GetWeapons()`
- `PLAYER:SetAmmo(n, ammo)`
- `PLAYER:GiveAmmo(n, ammo)`
- `PLAYER:RemoveAmmo(n, ammo)`
- `PLAYER:StripAmmo()`
- `PLAYER:SelectWeapon(class)`
- `PLAYER:Give(class, noAmmo)`
- `PLAYER:StripWeapon(class)`
- `PLAYER:StripWeapons()`
- `PLAYER:DropWeapon(class)`
- `util.BlastDamage(inflictor, attacker, pos, radius, damage)`
- `weapons.Tracers(shooter, hits, predicted)`
- `GM:PlayerLoadout(ply)`
