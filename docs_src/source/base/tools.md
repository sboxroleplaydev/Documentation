---
description: "Tool gun (client): settings, the on-screen help while holding the tool gun, and the settings panel builder."
---

# base: module `tools`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/tools/`

## `cl_tools.lua` (client)

Tool gun (client): settings, the on-screen help while holding the tool gun, and the settings panel builder.
```lua
tools.Select(mode)   -- asks the server to switch tool
tools.GetClientInfo(mode, key) -> string
tools.SetClientInfo(mode, key, value)   -- (saved in cookies, sent on)
tools.BuildPanel(parent, mode)   -- the tool's settings (TOOL.BuildCPanel) into a ui panel
```

Panel builder (the `panel` given to TOOL.BuildCPanel):
```lua
panel:Help(text)
panel:Slider(label, key, min, max [, decimals])
panel:CheckBox(label, key)
panel:Choices(label, key, { { label, value }, ... })
panel:Color(label, rKey, gKey, bKey [, aKey])
panel:Button(label, fn)   -- panel.Root (the ui panel, for your own controls)
```

Functions defined:

- `tools.GetClientInfo(mode, key)`
- `tools.SetClientInfo(mode, key, value)`
- `tools.Select(mode)`
- `tools.RebuildInfo()`
- `CP:Get(key)`
- `CP:Set(key, value)`
- `tools.NewPanel(parent, id)`
- `CP:Help(text)`
- `CP:Label(text)`
- `CP:Button(label, fn)`
- `CP:Slider(label, key, min, max, decimals)`
- `CP:CheckBox(label, key)`
- `CP:ComboBox(label, key, options)`
- `CP:Choices(label, key, options)`
- `CP:Color(label, rKey, gKey, bKey, aKey)`
- `CP:Key(label, key)`
- `CP:TextField(label, key, placeholder)`
- `CP:Divider()`
- `CP:Materials(label, key, list, size)`
- `tools.BuildPanel(parent, mode)`

## `sh_tools.lua` (shared)

Tool gun modes (GMod's TOOL tables). One shared file per tool in gamemode/tools/sh_<mode>.lua (also from addons
and derived gamemodes: tools.LoadFolder(dir)). A tool:

```lua
local TOOL = {}
TOOL.Name = "Remover"   TOOL.Category = "Construction"   TOOL.Description = "Removes props"
TOOL.Help = { left = "Remove", right = "...", reload = "..." }     -- shown on screen while holding the tool gun
TOOL.Stages = { [1] = { description = "Select the second object", left = "Finish" } }   -- per click stage (optional)
TOOL.ClientConVar = { r = "255" }      -- per-player settings (saved on the player's machine, sent to the server)
TOOL.Permission = "user"               -- default group for permission "tool.<mode>"
function TOOL:LeftClick(trace) return true end   -- server; true = it did something (beam + sound)
function TOOL:RightClick(trace) end   function TOOL:Reload(trace) end   function TOOL:Think() end
function TOOL:Holster() end
function TOOL.BuildCPanel(panel, tool) end         -- client: settings in the spawn menu's Tools tab
tools.Register(TOOL, "remover")
```


```lua
-- In tool functions
self:GetOwner()
self:GetWeapon()
self:GetMode()
self:GetClientInfo(key)
self:GetClientNumber(key [, default])
self:SetObject(i, ent, pos)
self:GetEnt(i)
self:GetPos(i)
self:NumObjects()
self:ClearObjects()
self:CanTouch(ent)
-- Who may use a tool on what
GM:CanTool(ply, trace, mode) (base: permission tool.<mode>, then props.CanTouch for
```

entities). Trace = util.TraceLine result (Entity, HitPos, HitNormal, HitWorld, ...).

Functions defined:

- `TOOLBASE:GetOwner()`
- `TOOLBASE:GetWeapon()`
- `TOOLBASE:GetMode()`
- `TOOLBASE:LeftClick(trace)`
- `TOOLBASE:RightClick(trace)`
- `TOOLBASE:Reload(trace)`
- `TOOLBASE:Think()`
- `TOOLBASE:Holster()`
- `TOOLBASE:CanTouch(ent)`
- `TOOLBASE:GetClientInfo(key)`
- `TOOLBASE:GetClientNumber(key, default)`
- `TOOLBASE:SetObject(i, ent, pos)`
- `TOOLBASE:GetEnt(i)`
- `TOOLBASE:GetPos(i)`
- `TOOLBASE:NumObjects()`
- `TOOLBASE:ClearObjects()`
- `TOOLBASE:SyncStage()`
- `tools.Register(tool, mode)`
- `tools.Get(mode)`
- `tools.GetList()`
- `tools.LoadFolder(dir)`
- `tools.Instance(ply, weapon, mode)`
- `PLAYER:GetToolMode()`
- `PLAYER:GetToolStage()`
- `tools.GetHelp(tool, stage)`
- `GM:CanTool(ply, trace, mode)`

## `sh_tools_length.lua` (shared)

Builder for the piston tools (hydraulic, muscle, winch): a "Rod" constraint (constraint.Rod) between two points whose
length Lua drives. tools.LengthTool({ mode, name, description, convars, setup(self, c, len, e1, e2), panel(panel) })
registers the tool; `setup` wires its keys / timers and returns the piston table { c, len, speed, target(p) -> length|nil, instant } that tools.Pistons then moves every frame (speed = units per second).

Functions defined:

- `tools.LengthTool(def)`

## `sv_helpers.lua` (server)

Helpers for tool gun modes that make things (server). Every tool uses the same rules: the prop limit, ownership, undo entries and server-side clamping of whatever the client sent.
```lua
tools.HasPhysics(ent)   -- a valid entity with a physics body
tools.Num(tool, key, def, min, max)   -- a clamped number setting (NaN-safe)
tools.Key(tool, key, def)   -- a key setting (checked with numpad.IsKey)
tools.Color(tool, rKey, gKey, bKey [, aKey]) a colour setting
tools.SurfaceAngle(trace [, yaw])   -- angle whose up points out of the surface that was hit
tools.CreateGadget(tool, trace, opts) -> ent | nil   -- a prop-class entity at the hit point (opts: model, size, color, kind, ang, lift, material)
tools.Finish(ply, name, ents, fns)   -- one undo entry (ents removed, fns called)
tools.AttachTo(ent, trace, weld)   -- weld to what was hit (props), or freeze on the world
tools.ReportError(ply, err)   -- chat message for a failed constraint call (limit errors were reported already)
tools.RemoveConstraint(c)   -- constraint.Remove, safe for stale values
```

Functions defined:

- `tools.HasPhysics(ent)`
- `tools.Num(tool, key, def, min, max)`
- `tools.Key(tool, key, def)`
- `tools.Color(tool, rk, gk, bk, ak)`
- `tools.SurfaceAngle(tr, yaw)`
- `tools.CreateGadget(tool, tr, opts)`
- `tools.Finish(ply, name, entities, fns)`
- `tools.ReportError(ply, err)`
- `tools.RemoveConstraint(c)`
- `tools.AttachTo(ent, tr, weld)`
- `tools.TwoClicks(tool, tr)`
- `tools.Place(tool, tr, weld, opts, setup)`
- `tools.FinishConstraint(tool, name, c, extra)`
- `tools.OnKey(tool, key, ent, fn)`

## `sv_tools.lua` (server)

Tool gun (server): the selected mode per player and their tool settings.
```lua
tools.GetPlayerInfo(ply, mode, key) -> string | nil
ply:SetToolMode(mode)
```

Clients send "base.tool.select" { mode } and "base.tool.info" { mode, key, value }. Only keys a tool declares in
TOOL.ClientConVar are kept, values are cut to 64 characters; tools still validate what they read.
Commands: "rp gmod_toolmode <mode>".

Functions defined:

- `tools.GetPlayerInfo(ply, mode, key)`
- `PLAYER:SetToolMode(mode)`
