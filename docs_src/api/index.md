---
description: "Pick a topic. Every page lists the functions with their arguments, realm and limits. There are 484 documented function signatures; search them all in the..."
---

# Lua API

Pick a topic. Every page lists the functions with their arguments, realm and limits. There are **484** documented function signatures; search them all in the [function index](functions.md).

## Getting started

<div class="grid cards" markdown>

-   **[Realms and files](getting-started/realms-and-files.md)**

    Load order:

-   **[Gamemodes and derivation](getting-started/gamemodes-and-derivation.md)**

    { "id": "darkrp", "title": "DarkRP", "version": "0.2.0", "apiVersion": 1,

-   **[Hooks called by the framework](getting-started/hooks-called-by-the-framework.md)**

    Gamemodes add their own hooks with hook.Run. Base adds PlayerSay; DarkRP adds PlayerCanChangeJob,

-   **[Addons](getting-started/addons.md)**

    An addon is a folder lua/addons/<id>/ (server owners: roleplay/lua/addons/<id>/ in the data folder) that runs on top

-   **[Modules and files](getting-started/modules-and-files.md)**

    Base gamemode: GM:LoadModules(dir [, order]) loads every folder in dir (relative to the calling gamemode) as a

-   **[API versions and migration](getting-started/api-versions-and-migration.md)**

    clear message ('apiVersion' 2 is not supported (this framework provides Lua API v1)), instead of letting old code

</div>

## Core

<div class="grid cards" markdown>

-   **[Core libraries](core/core-libraries.md)**

    

-   **[GMod compatibility helpers](core/gmod-compatibility-helpers.md)**

    Common Garry's Mod helpers, so GMod-style code finds what it expects:

-   **[Game / map](core/game-map.md)**

    gui (client, s&box's own overlays, GMod names where they exist): gui.ActivateGameUI() opens s&box's escape

-   **[Content](core/content.md)**

    Gamemodes can import sbox.game packages (models, materials, sounds, …) themselves, in addition to "packages" /

-   **[Players](core/players.md)**

    Both realms (read-only):

-   **[Networked variables](core/networked-variables.md)**

    These live on players, entities and globals (SetGlobalVar/GetGlobalVar). Only the server writes; everyone can read

-   **[Entities](core/entities.md)**

    Server: ents.Create(class, { model, pos = Vector, ang = Angle, scale, physics = bool, tint = Color, size = Vector, offset = Vector }).

-   **[Models, materials and textures](core/models-materials-and-textures.md)**

    Asset references are engine paths ("models/dev/box.vmdl", "materials/dev/reflectivity30.vmat") or mounted

-   **[Networking](core/networking.md)**

    Server: net.Receive(name, fn(ply, data) [, { burst, rate }]), net.Send(name, ply|{plys}, data),

-   **[Storage](core/storage.md)**

    Keys: a-z 0-9  - with / between parts, up to 96 characters (e.g. players/7656…).

-   **[Physics, coordinates and effects](core/physics-coordinates-and-effects.md)**

    PhysObj:ComputeShadowControl({ pos, angle, secondstoarrive, maxspeed, maxangular, teleportdistance }) (GMod): moves a

</div>

## Client

<div class="grid cards" markdown>

-   **[Keyboard](client/keyboard.md)**

    has focus. s&box reserves F1–F12 and Escape for the engine: games never see them (not as actions, not as raw keys), in the editor or in the 

-   **[Player clothing and skin](client/player-clothing-and-skin.md)**

    Every player wears the outfit they picked in the s&box main menu by default, in any gamemode (base included),

-   **[Keybinds](client/keybinds.md)**

    keybind.Register("mygm.inventory", { key = "i", label = "Inventory", category = "My gamemode", hint = true,

-   **[Cookies](client/cookies.md)**

    256 keys, 1024 characters each).

-   **[UI](client/ui.md)**

    ui.AddStyle([[ .box { position: absolute; left: 20px; top: 20px; background-color: rgba(0,0,0,0.8); pointer-events: all; } ]])

-   **[3D2D and immediate drawing](client/3d2d-and-immediate-drawing.md)**

    GMod style. Works like in Garry's Mod:

-   **[View and mouse](client/view-and-mouse.md)**

    LocalPlayer():SetFOV(fov [, seconds]) zooms (0 = back to the player's own setting); GetFOV().

-   **[Beams, glows and outlines](client/beams-glows-and-outlines.md)**

    render.DrawBeamEx(points, opts) (inside PostDraw…Renderables): a smooth spline through 2–32 points. Options:

</div>

## Base gamemode

<div class="grid cards" markdown>

-   **[Weapons](base-gamemode/weapons.md)**

    GMod-style weapons, written once in a shared file (gamemode, module or addon). Base loads every

-   **[Props, undo and the physics gun](base-gamemode/props-undo-and-the-physics-gun.md)**

    Props (server): props.Spawn(ply, model) → ent | nil, reason (permission, limit, placement, ownership, undo),

-   **[Tool gun](base-gamemode/tool-gun.md)**

    (tools.LoadFolder(dir) for derived gamemodes and addons):

-   **[Spawn menu and context menu](base-gamemode/spawn-menu-and-context-menu.md)**

    GMod's layout: creation tabs on the left (Props, Entities, Weapons, NPCs, Vehicles) with a category tree, icon grid and

-   **[UI components](base-gamemode/ui-components.md)**

    Ready-made controls on top of ui panels, in one modern style (blurred glass, blue accent). Each returns a table with

-   **[Base gamemode](base-gamemode/base-gamemode.md)**

    Chat (server): client message base.chat.say. GM:PlayerSay(ply, text, teamOnly) handles /cmd and !cmd and

-   **[Sandbox](base-gamemode/sandbox.md)**

    Not available: io, debug, package, require, load/loadstring/dofile/loadfile, setfenv/getfenv,

</div>

## Compatibility

<div class="grid cards" markdown>

-   **[Differences from Garry's Mod](compatibility/differences-from-garry-s-mod.md)**

    Lua version: Lua 5.1 with GLua operators. No LuaJIT, bit, coroutines or goto.

</div>
