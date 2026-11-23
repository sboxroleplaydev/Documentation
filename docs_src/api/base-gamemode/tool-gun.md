---
description: "gmodtool runs the selected tool mode. One shared file per tool in gamemode/tools/sh<mode>.lua"
---

# Tool gun

`gmod_tool` runs the selected **tool mode**. One shared file per tool in `gamemode/tools/sh_<mode>.lua`
(`#!lua tools.LoadFolder(dir)` for derived gamemodes and addons):

```lua
local TOOL = {}
TOOL.Name = "Colour"   TOOL.Category = "Render"   TOOL.Description = "Change the colour of props."
TOOL.Help = { left = "Paint", right = "Copy", reload = "Reset" }      -- shown on screen
TOOL.ClientConVar = { r = "255", g = "255", b = "255" }             -- player settings (cookies, sent to the server)
TOOL.Permission = "user"            -- default group for permission tool.<mode>
TOOL.AllowWorld = false             -- may it be used on the world?
if SERVER then
    function TOOL:LeftClick(trace)   -- return true = it did something (beam + sound for everyone)
        trace.Entity:SetColor(Color(self:GetClientNumber("r"), self:GetClientNumber("g"), self:GetClientNumber("b")))
        return true
    end
end
function TOOL.BuildCPanel(panel) panel:Color("Colour", "r", "g", "b") end
tools.Register(TOOL, "colour")
```

- **Tool methods:** `LeftClick/RightClick/Reload(trace)`, `Think`, `Holster`; `#!lua self:GetOwner()`, `#!lua GetWeapon()`,
  `#!lua GetMode()`, `#!lua GetClientInfo(key)`, `#!lua GetClientNumber(key [, default])`, `#!lua CanTouch(ent)`; multi-click tools:
  `#!lua SetObject(i, ent, pos)`, `#!lua GetEnt(i)`, `#!lua GetPos(i)`, `#!lua NumObjects()`, `#!lua ClearObjects()`.
- **Settings panel** (`#!lua TOOL.BuildCPanel(panel, tool)`, client): `#!lua panel:Help(text)`, `Label`, `#!lua Button(label, fn)`,
  `#!lua Slider(label, key, min, max [, decimals])`, `#!lua CheckBox(label, key)`, `#!lua ComboBox(label, key, options)`,
  `#!lua Choices(label, key, options)`, `#!lua Color(label, r, g, b [, a])` (full colour picker), `#!lua panel.Root` (a ui panel).
- **Client:** `#!lua tools.Select(mode)`, `#!lua tools.GetClientInfo(mode, key)`, `#!lua tools.SetClientInfo(mode, key, value)`,
  `#!lua tools.BuildPanel(parent, mode)`; the server can push values back with net message `#!lua base.tool.setinfo`.
- **Server:** `#!lua ply:SetToolMode(mode)`, `#!lua tools.GetPlayerInfo(ply, mode, key)`; shared `#!lua ply:GetToolMode()`,
  `#!lua tools.Get(mode)`, `#!lua tools.GetList()`. Who may use a tool on what: `#!lua GM:CanTool(ply, trace, mode)` (base: permission
  `tool.<mode>`, then `#!lua props.CanTouch`). Command: `rp gmod_toolmode <mode>`.
- **Built-in tools (33):** Construction: remover, duplicator, stacker, thruster, hoverball, balloon, button, wheel, mass, gravity, resizer, unbreakable, spawner. Constraints: weld, nocollide, rope, elastic, ballsocket, slider, hydraulic, muscle, winch, motor, keepupright.

    Render: colour, material (preview tiles, list `#!lua TOOL.Materials`), ropelook, light, emitter, speaker, text, trail, camera. Wording of names, descriptions and key hints is Facepunch's (their Sandbox, MIT). Not included: Wire (needs a whole signal system), Builder (our `builder:` plastic models + stacker cover it), Decal (needs Facepunch's decal resource assets).

- **Stages:** `TOOL.Stages = { [1] = { description = "Select the second object", left = "Finish" } }` changes the text
  after the first click (`#!lua self:SetObject` counts as a stage; shared as NW int `#!lua tool.stage`, `#!lua ply:GetToolStage()`).
  `#!lua tools.GetHelp(tool, stage)`. `TOOL.Status = function(tool) return { primary = "...", secondary = "...", hint = "..." } end`
  (client) adds readouts under the hints.
- **Screen and HUD:** while the tool gun is out its view model's dot-matrix screen shows the tool name scrolling by with the
  swipe on a change (`#!lua ply:SetViewModelScreen(text)`, `#!lua RpHeldWeapon.Screen.cs`: Facepunch's screen shader, at01 font), and the
  top-left panel shows the name (48 px), description, key glyphs with their actions and the status, like Facepunch's.
- **Helpers (server, `modules/tools/sv_helpers.lua`):** `tools.Num/Key/Color(tool, ...)` (clamped client settings),
  `#!lua tools.CreateGadget(tool, trace, { model, scale, size, kind, color, material, ang, lift })`, `tools.Place(tool, trace, weld,
  opts, setup)`, `tools.TwoClicks(tool, trace)`, `tools.Finish(ply, name, ents, fns)`, `tools.FinishConstraint`, `tools.AttachTo`.
  `#!lua tools.LengthTool({ mode, name, description, convars, setup, panel })` builds a piston tool (hydraulic/muscle/winch).
- **Settings panel extras:** `#!lua panel:Key(label, key)` (numpad keys or "Other key"; ClientConVars named `key...` are watched), `#!lua panel:TextField`, `#!lua panel:Divider`, `#!lua panel:Materials(label, key, list [, size])` (preview tiles), `#!lua ui.MaterialTile`, `#!lua ui.MaterialGrid(parent, materials, selected, fn [, size])`.

    Images: `#!lua p:SetImage("matthumb:materials/x.vmat")` renders a sphere wearing the material (3 per frame, cached).

- **Numpad (keys for contraptions):** `#!lua numpad.On(ply, key, function(ply, down) end, ent)` -> id, `#!lua numpad.Remove(id)`,
  `#!lua numpad.RemoveFor(ent)`, `#!lua numpad.Activate(ply, key, down)`, `#!lua numpad.Keys`, `#!lua numpad.IsKey(k)`, `#!lua numpad.KeyLabel(k)`.
  The client reports keys of your tools' `key...` settings (`#!lua base.numpad`), rate limited.
- **Engine API behind the tools (server):** `#!lua gadget.SetDriver(ent, "thruster"|"hoverball"|"keepupright"|"balloon", { force, speed, air, lift, strength, dir, enabled })`, `#!lua gadget.Control(ent, -1..1)`, `#!lua gadget.SetEnabled`, `#!lua gadget.GetDriver`, `#!lua gadget.ClearDriver`;

    `#!lua gadget.SetFx(ent, "light"|"trail"|"text"|"emitter", { color, a, b, c, text, pos, ang, on })`, `#!lua gadget.GetFx`, `#!lua gadget.RemoveFx(ent [, kind])` (meaning of a/b/c in `#!lua LuaGadgets.cs`). Constraints: `constraint.Elastic/Slider/Rod/Motor`, `#!lua constraint.SetMotor(c, degPerSec, torque)`, `#!lua constraint.SetLength(c, len)`, `GetLength`, `#!lua SetRopeLook(c, { width, color })`.

    Client: `#!lua LocalPlayer():SetViewOverride(pos, ang [, fov])`, `#!lua ClearViewOverride()`, `#!lua HasViewOverride()`.

- **Assets:** wheels (`models/construction/wheels/*`), hoverball, emitter/speaker and camera models, the vertex_tint shader
  and the tool gun screen come from Facepunch's Sandbox (MIT; licence files next to them).

