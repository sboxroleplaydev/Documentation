---
description: "Every function and class-table field (SWEP., TOOL., GM.) mentioned in the Lua API pages, grouped by library or object. Use the search box (top) to find..."
---

# Function index

Every function and class-table field (`SWEP.*`, `TOOL.*`, `GM.*`) mentioned in the Lua API pages, grouped by library or object. Use the search box (top) to find one by name.

**Jump to:** [(globals)](#globals) · [addons](#addons) · [ang](#ang) · [Angle](#angle) · [cam](#cam) · [chat](#chat) · [clothing](#clothing) · [concommand](#concommand) · [constraint](#constraint) · [content](#content) · [cookie](#cookie) · [draw](#draw) · [ent](#ent) · [ents](#ents) · [file](#file) · [gadget](#gadget) · [game](#game) · [GM](#gm) · [gui](#gui) · [hud](#hud) · [img](#img) · [input](#input) · [keybind](#keybind) · [limits](#limits) · [list](#list) · [log](#log) · [net](#net) · [numpad](#numpad) · [p](#p) · [panel](#panel) · [PhysObj](#physobj) · [player](#player) · [ply](#ply) · [properties](#properties) · [props](#props) · [render](#render) · [self](#self) · [snd](#snd) · [spawnmenu](#spawnmenu) · [storage](#storage) · [SWEP](#swep) · [team](#team) · [timer](#timer) · [TOOL](#tool) · [tools](#tools) · [ui](#ui) · [undo](#undo) · [util](#util) · [Vector](#vector) · [weapons](#weapons)

## (globals)

| Signature | Page |
|---|---|
| `#!lua ActivateTool(mode)` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua AddCSLuaFile()` | [Modules and files](getting-started/modules-and-files.md) |
| `#!lua AddToolCategory(tab, id, name)` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua AddToolTab(id, name, icon)` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua AttachTo(ent\|nil [, offset [, ang]])` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua Button(label, fn)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua CanProperty(ply, name, ent)` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua CanTouch(ent)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua CanTouchProp(ply, ent)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua CanUndo(ply, entry)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua Capture(function(key) end)` | [Keybinds](client/keybinds.md) |
| `#!lua ChatAddLine(msg)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua ChatPrint(text)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua ChatPrint(text)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua ChatPrint(text)` | [Players](core/players.md) |
| `#!lua CheckBox(label, key)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua Choices(label, key, options)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ClearObjects()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ClearViewOverride()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ClientsideModel(model)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua Color(label, r, g, b [, a])` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ComboBox(label, key, options)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ContentMounted(mounted, failed)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua CreateFont(name, { font, size, weight })` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua DoDrawCrosshair(x, y)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua DropWeapon([class])` | [Weapons](base-gamemode/weapons.md) |
| `#!lua EntityTakeDamage(ent, dmg, attacker, inflictor, pos)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua FindMetaTable("Player" \\| "Entity" \\| "Panel")` | [Core libraries](core/core-libraries.md) |
| `#!lua Flush()` | [Storage](core/storage.md) |
| `#!lua FormattedTime(seconds [, format])` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua GetAirStrafing()` | [Players](core/players.md) |
| `#!lua GetBodyHeight()` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua GetBodygroup(name or index)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua GetBodygroups()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua GetBunnyHopping()` | [Players](core/players.md) |
| `#!lua GetChildCount()` | [UI](client/ui.md) |
| `#!lua GetClientInfo(key)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua GetClientNumber(key [, default])` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua GetColor()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua GetCreationTabs()` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua GetCrouchedWalkSpeed()` | [Players](core/players.md) |
| `#!lua GetEnt(i)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua GetEyeTrace([dist])` | [Players](core/players.md) |
| `#!lua GetFOV()` | [View and mouse](client/view-and-mouse.md) |
| `#!lua GetFriction()` | [Players](core/players.md) |
| `#!lua GetJumpPower()` | [Players](core/players.md) |
| `#!lua GetKey(id)` | [Keybinds](client/keybinds.md) |
| `#!lua GetKeyName(id)` | [Keybinds](client/keybinds.md) |
| `#!lua GetMaterial()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua GetMode()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua GetModel()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua GetModelBounds()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua GetModelScale()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua GetMousePos()` | [UI](client/ui.md) |
| `#!lua GetNoDraw()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua GetNoclipSpeed()` | [Players](core/players.md) |
| `#!lua GetPos(i)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua GetRunSpeed()` | [Players](core/players.md) |
| `#!lua GetSize()` | [UI](client/ui.md) |
| `#!lua GetSkin()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua GetSkinTone()` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua GetSlowWalkSpeed()` | [Players](core/players.md) |
| `#!lua GetTextSize(text)` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua GetWalkSpeed()` | [Players](core/players.md) |
| `#!lua GetWeapon()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua GravGunPickupAllowed(ply, ent)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua HUDPaint()` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua HasViewOverride()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua IsDown(id)` | [Keybinds](client/keybinds.md) |
| `#!lua IsHovered()` | [UI](client/ui.md) |
| `#!lua IsNotSolid()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua IsValid(NULL)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua KeyName(keyOrAction)` | [Keybinds](client/keybinds.md) |
| `#!lua KeybindPressed(id)` | [Keybinds](client/keybinds.md) |
| `#!lua KeybindReleased(id)` | [Keybinds](client/keybinds.md) |
| `#!lua Kick(reason)` | [Players](core/players.md) |
| `#!lua LocalPlayer()` | [Players](core/players.md) |
| `#!lua LocalPlayer()` | [Weapons](base-gamemode/weapons.md) |
| `#!lua LocalPlayer():SetFOV(fov [, seconds])` | [View and mouse](client/view-and-mouse.md) |
| `#!lua LocalPlayer():SetViewOverride(pos, ang [, fov])` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua LocalToWorld(localPos, localAng, originPos, originAng)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua Material(path)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua Model(path)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua NumObjects()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua OnChange(fn(text))` | [UI](client/ui.md) |
| `#!lua OnClick(fn)` | [UI](client/ui.md) |
| `#!lua OnPhysgunFreeze(weapon, phys, ent, ply)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua OnPhysgunPickup(ply, ent)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua OnPhysgunReload(weapon, ply)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua OnRightClick(fn)` | [UI](client/ui.md) |
| `#!lua OnSubmit(fn(text))` | [UI](client/ui.md) |
| `#!lua PhysgunDrop(ply, ent)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua PhysgunPickup(ply, ent)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua PlayerButtonDown(action)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua PlayerButtonUp(action)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua PlayerCanDropWeapon(ply, weapon)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua PlayerCanPickupWeapon(ply, class)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua PlayerCheckLimit(ply, id, count, limit)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua PlayerDisconnected(ply)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua PlayerInitialSpawn(ply)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua PlayerLoadout(ply)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua PlayerRolled(ply, result, max)` | [Addons](getting-started/addons.md) |
| `#!lua PlayerSpawn(ply)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua PlayerSpawnProp(ply, model)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua PlayerSpawnedProp(ply, model, ent)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua PlayerSwitchWeapon(ply, old, new)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua PlayerUse(ply, ent)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua PostDrawOpaqueRenderables(depth, skybox)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua PostDrawTranslucentRenderables(depth, skybox)` | [Hooks called by the framework](getting-started/hooks-called-by-the-framework.md) |
| `#!lua Remove(id)` | [Keybinds](client/keybinds.md) |
| `#!lua RemoveConstraints(ent, type)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua ResetClothing()` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua RunConsoleCommand(name, ...)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua ScrH()` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua ScrW()` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua SetAcceleration(n)` | [Players](core/players.md) |
| `#!lua SetAirAcceleration(n)` | [Players](core/players.md) |
| `#!lua SetAirStrafing(b)` | [Players](core/players.md) |
| `#!lua SetAvatar(ply or steamid64)` | [UI](client/ui.md) |
| `#!lua SetBodygroup(name or index, value)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua SetBunnyHopping(b)` | [Players](core/players.md) |
| `#!lua SetClipboardText(text)` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua SetColor(Color)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua SetCrouchedWalkSpeed(f)` | [Players](core/players.md) |
| `#!lua SetDuckSpeed(s)` | [Players](core/players.md) |
| `#!lua SetFaceCamera(b)` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua SetFriction(f)` | [Players](core/players.md) |
| `#!lua SetImage(src)` | [UI](client/ui.md) |
| `#!lua SetJumpPower(n)` | [Players](core/players.md) |
| `#!lua SetKey(id, key or nil)` | [Keybinds](client/keybinds.md) |
| `#!lua SetMaterial(mat)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua SetModel(model)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua SetModelScale(s)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua SetNoDraw(b)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua SetNoclipSpeed(n)` | [Players](core/players.md) |
| `#!lua SetNotSolid(b)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua SetObject(i, ent, pos)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua SetParent(panel\|nil)` | [UI](client/ui.md) |
| `#!lua SetPos(vector)` | [Players](core/players.md) |
| `#!lua SetRopeLook(c, { width, color })` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua SetRunSpeed(n)` | [Players](core/players.md) |
| `#!lua SetSkin(n)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua SetSlowWalkSpeed(n)` | [Players](core/players.md) |
| `#!lua SetStyle(css)` | [UI](client/ui.md) |
| `#!lua SetTooltip(text\|nil)` | [UI](client/ui.md) |
| `#!lua SetUnDuckSpeed(s)` | [Players](core/players.md) |
| `#!lua SetWalkSpeed(n)` | [Players](core/players.md) |
| `#!lua SkinCount()` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua Slider(label, key, min, max [, decimals])` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua SortByMember(t, member [, ascending])` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua Spawn()` | [Players](core/players.md) |
| `#!lua SteamID()` | [Players](core/players.md) |
| `#!lua WeaponButtonDown(1\|2\|3)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua WorldToLocal(pos, ang, originPos, originAng)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua fn(ply, data)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua function(parent, search)` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua include()` | [Addons](getting-started/addons.md) |
| `#!lua include(path)` | [Core libraries](core/core-libraries.md) |
| `#!lua pcall(constraint.X, ...)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |

## addons

| Signature | Page |
|---|---|
| `#!lua addons.Get(id)` | [Addons](getting-started/addons.md) |
| `#!lua addons.GetAll()` | [Addons](getting-started/addons.md) |
| `#!lua addons.IsLoaded(id)` | [Addons](getting-started/addons.md) |

## ang

| Signature | Page |
|---|---|
| `#!lua ang:Forward()` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua ang:Right()` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua ang:Up()` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |

## Angle

| Signature | Page |
|---|---|
| `#!lua Angle:RotateAroundAxis(axis, degrees)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |

## cam

| Signature | Page |
|---|---|
| `#!lua cam.End3D2D()` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua cam.Start3D2D(pos, ang, scale)` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua cam.ToScreen(pos)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |

## chat

| Signature | Page |
|---|---|
| `#!lua chat.AddCommand(name, fn(ply, args, argString), help)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua chat.Broadcast(text, color)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua chat.Send(target, text, color)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua chat.SendMessage(recipients, { prefix, prefixColor, name, nameColor, text, color })` | [Base gamemode](base-gamemode/base-gamemode.md) |

## clothing

| Signature | Page |
|---|---|
| `#!lua clothing.GetAll([category])` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua clothing.GetCategories()` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua clothing.GetTitle(path)` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua clothing.IsValid(path)` | [Player clothing and skin](client/player-clothing-and-skin.md) |

## concommand

| Signature | Page |
|---|---|
| `#!lua concommand.Add(name, function(ply, cmd, args, argStr) end [, autoComplete, helpText])` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |

## constraint

| Signature | Page |
|---|---|
| `#!lua constraint.SetLength(c, len)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua constraint.SetMotor(c, degPerSec, torque)` | [Tool gun](base-gamemode/tool-gun.md) |

## content

| Signature | Page |
|---|---|
| `#!lua content.AddCollection(source)` | [Content](core/content.md) |
| `#!lua content.AddPackage(id)` | [Content](core/content.md) |
| `#!lua content.GetModel(id)` | [Content](core/content.md) |
| `#!lua content.GetPackages()` | [Content](core/content.md) |
| `#!lua content.GetTitle(id)` | [Content](core/content.md) |
| `#!lua content.IsBusy()` | [Content](core/content.md) |
| `#!lua content.IsMounted(id)` | [Content](core/content.md) |
| `#!lua content.Search(query, function(results, err, done) end [, type])` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |

## cookie

| Signature | Page |
|---|---|
| `#!lua cookie.Delete(name)` | [Cookies](client/cookies.md) |
| `#!lua cookie.GetNumber(name [, default])` | [Cookies](client/cookies.md) |
| `#!lua cookie.GetString(name [, default])` | [Cookies](client/cookies.md) |
| `#!lua cookie.Set(name, value)` | [Cookies](client/cookies.md) |

## draw

| Signature | Page |
|---|---|
| `#!lua draw.DrawText(text, font, x, y, color, xalign)` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua draw.RoundedBox(r, x, y, w, h, color)` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua draw.SimpleText(text, font, x, y, color, xalign, yalign)` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |
| `#!lua draw.SimpleTextOutlined(…, outlineWidth, outlineColor)` | [3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md) |

## ent

| Signature | Page |
|---|---|
| `#!lua ent:LocalToWorld(pos)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua ent:LocalToWorldAngles(a)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua ent:SetGhost(color \| nil)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua ent:SetHighlight(color \| nil [, width [, throughWalls [, glow]]])` | [Beams, glows and outlines](client/beams-glows-and-outlines.md) |
| `#!lua ent:WorldToLocal(pos)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua ent:WorldToLocalAngles(a)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |

## ents

| Signature | Page |
|---|---|
| `#!lua ents.Create(class, { model, pos = Vector, ang = Angle, scale, physics = bool, tint = Color, size = Vector, offset = Vector })` | [Entities](core/entities.md) |
| `#!lua ents.CreateClientProp(model)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua ents.FindByClass(c)` | [Entities](core/entities.md) |
| `#!lua ents.FindInSphere(pos, r)` | [Entities](core/entities.md) |
| `#!lua ents.GetAll()` | [Entities](core/entities.md) |

## file

| Signature | Page |
|---|---|
| `#!lua file.Exists(path)` | [Modules and files](getting-started/modules-and-files.md) |
| `#!lua file.Exists(path, "DATA")` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua file.Find("gamemode/modules/*")` | [Modules and files](getting-started/modules-and-files.md) |
| `#!lua file.Find(pattern, "DATA")` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua file.IsDir(dir, "DATA")` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua file.Read(path, "DATA")` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua file.Size(path, "DATA")` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua file.Write(path, text)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |

## gadget

| Signature | Page |
|---|---|
| `#!lua gadget.RemoveFx(ent [, kind])` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua gadget.SetFx(ent, "light"\|"trail"\|"text"\|"emitter", { color, a, b, c, text, pos, ang, on })` | [Tool gun](base-gamemode/tool-gun.md) |

## game

| Signature | Page |
|---|---|
| `#!lua game.AddAmmoType({ name, maxcarry })` | [Weapons](base-gamemode/weapons.md) |
| `#!lua game.GetAmmoMax(name)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua game.GetMap()` | [Game / map](core/game-map.md) |
| `#!lua game.GetServerName()` | [Game / map](core/game-map.md) |
| `#!lua game.IsDedicated()` | [Game / map](core/game-map.md) |
| `#!lua game.IsEditor()` | [Game / map](core/game-map.md) |
| `#!lua game.IsHost()` | [Game / map](core/game-map.md) |
| `#!lua game.IsMultiplayer()` | [Game / map](core/game-map.md) |
| `#!lua game.LeaveToMenu()` | [Game / map](core/game-map.md) |

## GM

| Signature | Page |
|---|---|
| `#!lua GM.BaseClass` | [Gamemodes and derivation](getting-started/gamemodes-and-derivation.md) |
| `#!lua GM.BotMode` | [Players](core/players.md) |
| `#!lua GM.DefaultLoadout` | [Weapons](base-gamemode/weapons.md) |
| `#!lua GM.LoadedModules` | [Modules and files](getting-started/modules-and-files.md) |
| `#!lua GM.PlayerMovement` | [Players](core/players.md) |
| `#!lua GM.PropLimit` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua GM.RagdollTime` | [Players](core/players.md) |
| `#!lua GM.RemovePropsOnDisconnect` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua GM:BotThink(ply, state)` | [Players](core/players.md) |
| `#!lua GM:CanTool(ply, trace, mode)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua GM:ChatCreate` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:ChatRecipients` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:CleanChatText(text)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:CreateKeyCap(parent, text)` | [Keybinds](client/keybinds.md) |
| `#!lua GM:DoPlayerDeath` | [Players](core/players.md) |
| `#!lua GM:FormatChatMessage` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:GetPlayerColor(ply)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:GetPlayerDisplayName(ply)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:HelpSections()` | [Keybinds](client/keybinds.md) |
| `#!lua GM:KeyHintsFilter(bind)` | [Keybinds](client/keybinds.md) |
| `#!lua GM:LoadModules(dir [, order])` | [Modules and files](getting-started/modules-and-files.md) |
| `#!lua GM:PauseMenuButtons()` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:PauseMenuSubtitle()` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:PauseMenuTitle()` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:PlayerSay(ply, text, teamOnly)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:PlayerSpawn(ply)` | [Gamemodes and derivation](getting-started/gamemodes-and-derivation.md) |
| `#!lua GM:ScoreboardColumns()` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:ScoreboardCreate` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:ScoreboardRow(ply)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:ScoreboardTitle()` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua GM:SetupMovement(ply)` | [Players](core/players.md) |
| `#!lua GM:SpawnMenuTabs()` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua GM:event` | [Core libraries](core/core-libraries.md) |

## gui

| Signature | Page |
|---|---|
| `#!lua gui.ActivateGameUI()` | [Game / map](core/game-map.md) |
| `#!lua gui.HideGameUI()` | [Game / map](core/game-map.md) |
| `#!lua gui.OpenBinds()` | [Game / map](core/game-map.md) |
| `#!lua gui.OpenPlayerList()` | [Game / map](core/game-map.md) |
| `#!lua gui.OpenSettings([page])` | [Game / map](core/game-map.md) |

## hud

| Signature | Page |
|---|---|
| `#!lua hud.Notify(text [, s])` | [UI](client/ui.md) |
| `#!lua hud.RemoveLine(id)` | [UI](client/ui.md) |
| `#!lua hud.SetLine(id, text)` | [API versions and migration](getting-started/api-versions-and-migration.md) |
| `#!lua hud.SetLine(id, text)` | [UI](client/ui.md) |

## img

| Signature | Page |
|---|---|
| `#!lua img:SetImage(src)` | [Models, materials and textures](core/models-materials-and-textures.md) |

## input

| Signature | Page |
|---|---|
| `#!lua input.GetMouseDelta()` | [View and mouse](client/view-and-mouse.md) |
| `#!lua input.GetMouseWheel()` | [View and mouse](client/view-and-mouse.md) |
| `#!lua input.IsKeyDown(key)` | [Keyboard](client/keyboard.md) |
| `#!lua input.LookupBinding(action)` | [Keyboard](client/keyboard.md) |
| `#!lua input.SetLookScale(scale)` | [View and mouse](client/view-and-mouse.md) |
| `#!lua input.WasKeyPressed(key)` | [Keyboard](client/keyboard.md) |
| `#!lua input.WasKeyReleased(key)` | [Keyboard](client/keyboard.md) |

## keybind

| Signature | Page |
|---|---|
| `#!lua keybind.GetAll()` | [Keybinds](client/keybinds.md) |

## limits

| Signature | Page |
|---|---|
| `#!lua limits.Check(ply, id [, notify])` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua limits.Count(ply, id)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua limits.CountAll(ply)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua limits.Get(id)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua limits.List()` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua limits.Notify(ply, id)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua limits.Register("dynamite", 10, "Dynamite", "dynamite")` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua limits.Register(id, default, label [, gadgetKind])` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |

## list

| Signature | Page |
|---|---|
| `#!lua list.Set("DesktopWindows", id, { title, icon, init })` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua list.Set("NPC", id, { Name, Class, Model, Category, Spawn })` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua list.Set("SpawnableEntities", class, { PrintName, ClassName, Category, Model, SpawnFunction })` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua list.Set("Vehicles", ...)` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua list.Set("Weapon", class, { ClassName, PrintName, Category })` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |

## log

| Signature | Page |
|---|---|
| `#!lua log.Audit(category, message)` | [Storage](core/storage.md) |

## net

| Signature | Page |
|---|---|
| `#!lua net.Broadcast()` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua net.Broadcast(name, data)` | [Networking](core/networking.md) |
| `#!lua net.Receive(name, fn(data))` | [Networking](core/networking.md) |
| `#!lua net.Receive(name, fn(ply, data) [, { burst, rate }])` | [Networking](core/networking.md) |
| `#!lua net.Receive(name, function(len, ply) ... net.ReadX() ... end)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua net.Send(name, ply, data)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua net.Send(name, ply\|{plys}, data)` | [Networking](core/networking.md) |
| `#!lua net.Send(ply\|{plys})` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua net.SendToServer()` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua net.SendToServer(name, data)` | [Networking](core/networking.md) |
| `#!lua net.Start(name)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |

## numpad

| Signature | Page |
|---|---|
| `#!lua numpad.Activate(ply, key, down)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua numpad.IsKey(k)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua numpad.KeyLabel(k)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua numpad.On(ply, key, function(ply, down) end, ent)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua numpad.Remove(id)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua numpad.RemoveFor(ent)` | [Tool gun](base-gamemode/tool-gun.md) |

## p

| Signature | Page |
|---|---|
| `#!lua p:SetImage("matthumb:materials/x.vmat")` | [Tool gun](base-gamemode/tool-gun.md) |

## panel

| Signature | Page |
|---|---|
| `#!lua panel:Get(key)` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua panel:Help(text)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua panel:Key(label, key)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua panel:Materials(label, key, list [, size])` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua panel:SetAvatar(ply or steamid64)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua panel:SetKeyGlyph(keyOrAction)` | [Keybinds](client/keybinds.md) |

## PhysObj

| Signature | Page |
|---|---|
| `#!lua PhysObj:ComputeShadowControl({ pos, angle, secondstoarrive, maxspeed, maxangular, teleportdistance })` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |

## player

| Signature | Page |
|---|---|
| `#!lua player.CreateBot([name])` | [Players](core/players.md) |
| `#!lua player.GetAll()` | [Players](core/players.md) |
| `#!lua player.GetBots()` | [Players](core/players.md) |
| `#!lua player.GetCount()` | [Players](core/players.md) |

## ply

| Signature | Page |
|---|---|
| `#!lua ply:AddClothing(path [, tint])` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua ply:ClearClothing()` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua ply:CreateRagdoll([seconds])` | [Players](core/players.md) |
| `#!lua ply:Crouching()` | [Players](core/players.md) |
| `#!lua ply:Freeze(b)` | [Players](core/players.md) |
| `#!lua ply:GetMuzzlePos()` | [Weapons](base-gamemode/weapons.md) |
| `#!lua ply:GetOutfit()` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua ply:GetRagdollPos()` | [Players](core/players.md) |
| `#!lua ply:GetToolMode()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ply:GetToolStage()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ply:GetUserGroup()` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua ply:GetVelocity()` | [Players](core/players.md) |
| `#!lua ply:Give(class [, noAmmo])` | [Weapons](base-gamemode/weapons.md) |
| `#!lua ply:IsAdmin()` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua ply:IsBot()` | [Players](core/players.md) |
| `#!lua ply:IsOnGround()` | [Players](core/players.md) |
| `#!lua ply:IsSprinting()` | [Players](core/players.md) |
| `#!lua ply:IsSuperAdmin()` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua ply:IsUserGroup(g)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua ply:Kick()` | [Players](core/players.md) |
| `#!lua ply:OnGround()` | [Players](core/players.md) |
| `#!lua ply:PrintMessage(HUD_PRINTTALK, text)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua ply:RemoveClothing(path)` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua ply:ResetClothing()` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua ply:SetBodyHeight(0–1 or nil)` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua ply:SetBotInput(forward, left [, jump [, run]])` | [Players](core/players.md) |
| `#!lua ply:SetEyeAngles(ang)` | [Players](core/players.md) |
| `#!lua ply:SetMoveType(MOVETYPE_WALK\|MOVETYPE_NOCLIP\|MOVETYPE_NONE)` | [Players](core/players.md) |
| `#!lua ply:SetOutfit({ path, { path, tint }, ... } or nil)` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua ply:SetSkinTone(0–1 or nil)` | [Player clothing and skin](client/player-clothing-and-skin.md) |
| `#!lua ply:SetTeam(id)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua ply:SetToolMode(mode)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ply:SetUserGroup(g)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua ply:SetVelocity(v)` | [Players](core/players.md) |
| `#!lua ply:SetViewModelParam("b_sprint", ...)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua ply:SetViewModelParam(name, bool\|number\|nil)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua ply:SetViewModelScreen(text)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ply:SetViewModelVisible(b)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua ply:Team()` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua ply:WeaponAnim(param [, skipOwner])` | [Weapons](base-gamemode/weapons.md) |

## properties

| Signature | Page |
|---|---|
| `#!lua properties.Add(name, { MenuLabel, Order, MenuIcon, Filter(self, ent, ply), Action(self, ent), Receive(self, ent, ply, data) })` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |

## props

| Signature | Page |
|---|---|
| `#!lua props.CanSpawn(ply, model, kind)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua props.CanTouch(ply, ent)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua props.Count(ply)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua props.GetOwner(ent)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua props.RemoveAll(ply)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua props.Spawn(ply, model)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |

## render

| Signature | Page |
|---|---|
| `#!lua render.DrawBeamEx(points, opts)` | [Beams, glows and outlines](client/beams-glows-and-outlines.md) |
| `#!lua render.DrawSprite(pos, size, color [, brightness [, texture]])` | [Beams, glows and outlines](client/beams-glows-and-outlines.md) |

## self

| Signature | Page |
|---|---|
| `#!lua self.BaseClass.PauseMenuButtons(self)` | [Base gamemode](base-gamemode/base-gamemode.md) |
| `#!lua self:CanPrimaryAttack()` | [Weapons](base-gamemode/weapons.md) |
| `#!lua self:DefaultReload()` | [Weapons](base-gamemode/weapons.md) |
| `#!lua self:EmitSound(path [, vol, pitch])` | [Weapons](base-gamemode/weapons.md) |
| `#!lua self:GetOwner()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua self:MeleeAttack(range, damage, force)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua self:Send(ent [, data])` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua self:SendWeaponAnim(param)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua self:ShootBullet(damage, num, cone)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua self:TakePrimaryAmmo(n)` | [Weapons](base-gamemode/weapons.md) |

## snd

| Signature | Page |
|---|---|
| `#!lua snd:ChangePitch(p [, seconds])` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua snd:ChangeVolume(v [, seconds])` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua snd:FadeOut(seconds)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua snd:IsPlaying()` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua snd:Play()` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua snd:PlayEx(volume, pitch)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua snd:Stop()` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |

## spawnmenu

| Signature | Page |
|---|---|
| `#!lua spawnmenu.AddCreationTab(name, function(parent, search) end, icon, order, tooltip [, visible])` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua spawnmenu.AddEntity(id, def)` | [Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md) |
| `#!lua spawnmenu.AddPropCategory(name, { "builder:1x8x0.25", { "builder:1x1x1", "my name" }, { header = "Section" } })` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |

## storage

| Signature | Page |
|---|---|
| `#!lua storage.Delete(key)` | [Storage](core/storage.md) |
| `#!lua storage.Exists(key)` | [Storage](core/storage.md) |
| `#!lua storage.Flush()` | [Storage](core/storage.md) |
| `#!lua storage.Get(key)` | [Storage](core/storage.md) |
| `#!lua storage.Set("roll/stats/" .. sid, …)` | [Addons](getting-started/addons.md) |
| `#!lua storage.Set(key, value)` | [Storage](core/storage.md) |

## SWEP

| Signature | Page |
|---|---|
| `#!lua SWEP.BeamColor` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua SWEP.Category` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.FleshHitSound` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua SWEP.GravityGrabDistance` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua SWEP.Handedness` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.HitSound` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua SWEP.HoldType` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.MuzzleFlash` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.Primary` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.PrintName` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.ReloadSound` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.ReloadTime` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.Slot` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.SlotPos` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.SnapAngle` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua SWEP.Sounds` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua SWEP.Spawnable` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.ViewModel` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.ViewModelBodygroups` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.ViewModelOffset` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.WorldHitSound` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua SWEP.WorldModel` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.WorldModelAngles` | [Weapons](base-gamemode/weapons.md) |
| `#!lua SWEP.WorldModelOffset` | [Weapons](base-gamemode/weapons.md) |

## team

| Signature | Page |
|---|---|
| `#!lua team.SetUp(id, name, color [, joinable])` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |

## timer

| Signature | Page |
|---|---|
| `#!lua timer.Adjust(id, delay [, reps [, fn]])` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |

## TOOL

| Signature | Page |
|---|---|
| `#!lua TOOL.AllowWorld` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL.BuildCPanel(panel)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL.BuildCPanel(panel, tool)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL.Category` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL.ClientConVar` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL.Description` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL.Help` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL.Materials` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL.Name` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL.Permission` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua TOOL:LeftClick(trace)` | [Tool gun](base-gamemode/tool-gun.md) |

## tools

| Signature | Page |
|---|---|
| `#!lua tools.BuildPanel(parent, mode)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.CreateGadget(tool, trace, { model, scale, size, kind, color, material, ang, lift })` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.Get(mode)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.GetClientInfo(mode, key)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.GetHelp(tool, stage)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.GetList()` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.GetPlayerInfo(ply, mode, key)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.LengthTool({ mode, name, description, convars, setup, panel })` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.LoadFolder(dir)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.ReportError(ply, err)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua tools.Select(mode)` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua tools.SetClientInfo(mode, key, value)` | [Tool gun](base-gamemode/tool-gun.md) |

## ui

| Signature | Page |
|---|---|
| `#!lua ui.AddStyle(css)` | [UI](client/ui.md) |
| `#!lua ui.Button(parent, text, fn [, "primary"\|"danger"])` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.Category(parent, title, expanded)` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.ColorPicker(parent, color, fn [, { alpha }])` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.Create("image")` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua ui.HSVToRGB(h, s, v)` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.IsMouseDown([button])` | [UI](client/ui.md) |
| `#!lua ui.IsTyping()` | [UI](client/ui.md) |
| `#!lua ui.MaterialGrid(parent, materials, selected, fn [, size])` | [Tool gun](base-gamemode/tool-gun.md) |
| `#!lua ui.ProgressBar(parent, f [, text])` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.RGBToHSV(r, g, b)` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.ScreenSize()` | [UI](client/ui.md) |
| `#!lua ui.SetCursor(visible)` | [UI](client/ui.md) |
| `#!lua ui.Slider(parent, label, min, max, value, fn [, decimals])` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.Tabs(parent, { { id, label } }, active, fn(id, body))` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.TextField(parent, label, text, fn [, placeholder])` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.Tile(parent, image, title, fn [, size])` | [UI components](base-gamemode/ui-components.md) |
| `#!lua ui.Window(title, { width, height, onClose })` | [UI components](base-gamemode/ui-components.md) |

## undo

| Signature | Page |
|---|---|
| `#!lua undo.AddEntity(ent)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua undo.AddFunction(fn, ...)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua undo.Create(name)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua undo.Do(ply)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua undo.Finish()` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua undo.GetTable(ply)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua undo.ReplaceEntity(old, new)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua undo.SetCustomUndoText(text)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |
| `#!lua undo.SetPlayer(ply)` | [Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md) |

## util

| Signature | Page |
|---|---|
| `#!lua util.BlastDamage(inflictor, attacker, pos, radius, damage)` | [Weapons](base-gamemode/weapons.md) |
| `#!lua util.Effect("Blood", pos, scale, dir)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua util.Effect("Impact", pos, scale, dir)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua util.Effect(name, pos [, scale])` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua util.IsValidMaterial(path)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua util.IsValidModel(path)` | [Models, materials and textures](core/models-materials-and-textures.md) |
| `#!lua util.JSONToTable(json)` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua util.RotateAroundAxis(ang, axis, deg)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua util.TableToJSON(t [, pretty])` | [GMod compatibility helpers](core/gmod-compatibility-helpers.md) |
| `#!lua util.TraceLine({ start, endpos, filter })` | [Entities](core/entities.md) |

## Vector

| Signature | Page |
|---|---|
| `#!lua Vector:Rotate(ang)` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |
| `#!lua Vector:ToScreen()` | [Physics, coordinates and effects](core/physics-coordinates-and-effects.md) |

## weapons

| Signature | Page |
|---|---|
| `#!lua weapons.LoadFolder(dir)` | [Weapons](base-gamemode/weapons.md) |
