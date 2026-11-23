---
description: "Gamemodes are plain Lua. On first start, every installation copies the built-in gamemodes into its own data"
---

# Server Owners: Gamemodes and Addons

Gamemodes are plain Lua. On first start, **every** installation copies the built-in gamemodes into its own **data
folder** and runs them from there: dedicated servers, players hosting locally, and the editor. You can change anything
without touching the game. (s&box only lets a game write to its data folder: `<s&box or server install>/data/<org>/<game>/`.)

## Where the files are

The server's log prints the exact path on startup:

```
stage gamemodes: Ok ... loading from data folder (C:\...\sbox\data\<org>\<game>\roleplay\lua)
```

```
roleplay/lua/
  README.txt
  gamemodes/
    base/       gamemode.json + gamemode/*.lua   (chat, scoreboard)
    darkrp/     gamemode.json + gamemode/*.lua   (jobs, money, items, doors, admin, HUD)
    sandboxrp/  gamemode.json + gamemode/*.lua   (small sample: roleplay names and props)
    _template/  copy this to start your own gamemode (folders starting with _ never load)
    <yours>/    add as many as you like
  addons/
    roll/       addon.json + *.lua               (sample: /roll and a dice widget)
    _template/  copy this to start your own addon
    <yours>/    drop-in addons, on by default
roleplay/lua_backups/   backups made by game updates and rp_lua_restore
roleplay/tmp/servers/<server-id>/   client side: scripts downloaded from each server you joined
```

## What players' games do

When a player joins a server, their game downloads that server's shared and client scripts into a **separate temp folder per server**: `roleplay/tmp/servers/<server Steam id>/lua/…`, plus a `server.txt` with the name, gamemode and last visit.

Servers can run their own modified Lua, so each server's files stay apart. They are never mixed with another server's files or with the player's own editable gamemodes in `roleplay/lua`.


- **Reuse:** on the next join only changed files are downloaded. Every file's fingerprint is checked against the server
  each time, so editing these copies can't change what runs.
- **Server-only files:** `sv_` files are never sent, so they never appear here.
- **Housekeeping:** folders of servers not visited for 30 days, and anything beyond the 20 most recent servers, are
  deleted automatically.

**A folder in `gamemodes/` replaces the built-in gamemode with the same id.** Built-in gamemodes you don't have a copy
of are still available. Existing copies are never overwritten by the framework, including after a game update.

## Typical changes

DarkRP keeps everything a server owner usually changes in **`darkrp/gamemode/config/`**; the features themselves are
in `darkrp/gamemode/modules/<feature>/` (one folder per feature, `sh_`/`sv_`/`cl_` files).

| You want to… | Edit |
|---|---|
| Change salaries, starting money, prices, hunger, arrest time, ranges | `config/sh_config.lua` |
| Add or remove jobs, change what a job wears | `config/sh_jobs.lua` (`DarkRP.createJob`, `outfit = { clothing paths }`, `police`, `mayor`) |
| Add shop items | `config/sh_items.lua` (`food`, `heal`, `model`); special effects in `modules/items/sv_items.lua` (`DarkRP.ItemUse`) |
| Add shop entities (placed in the world) | `config/sh_entities.lua`; behaviour in `modules/entities/sv_entities.lua` (`DarkRP.EntityInit` / `EntityUse`) |
| Change who may use admin commands | `DarkRP.GroupPermissions` in `config/sh_config.lua` |
| Add a whole feature | a new folder `modules/<name>/` with `sh_`/`sv_`/`cl_` files: it loads automatically |
| Restyle or replace chat, scoreboard, key hints, help or the Escape pause menu | `base/gamemode/modules/...`, or override the GM functions in your gamemode (`GM:PauseMenuButtons()` adds buttons) |
| Change the default map | `"maps"` in `gamemode.json`, or `"Map"` in `framework.json` |
| Set up the jail on a map | stand in the cell and type `/addjailpos` (admins); `/removejailpos` clears them |

Clothing paths for outfits: 204 items ship with s&box under `models/citizen_clothes/` (hats, shirts, uniforms, shoes,
hair, skins…); `clothing.GetAll()` in Lua lists them with titles and categories.

## Weapons, physics gun, tool gun and spawn menu

Everything below is Lua in **`base/gamemode/`** (so DarkRP and every gamemode derived from base gets it) and can be
changed in your gamemode's config or an addon. API details: `Docs/LUA_API.md` ("Weapons", "Tool gun", "Spawn menu").

| You want to… | Do this |
|---|---|
| Sell weapons and ammo in DarkRP | `darkrp/gamemode/config/sh_weapons.lua`: `DarkRP.createWeapon("weapon_smg", { price = 1200, allowed = { TEAM_GUN } })`, `DarkRP.createAmmo("smg1", { name = "SMG ammo", price = 60, amount = 30 })`. Players buy them in the M menu's Weapons / Ammo tabs or with `/buy <class>` |
| Tune the DarkRP money printer | `darkrp/gamemode/config/sh_entities.lua`, `money_printer`: `print_amount`, `print_interval` (s), `capacity`, and `upgrades = { { id, name, unit = "interval"/"amount"/"capacity", levels = { { cost, value }, ... } } }`. Players press E on it: collect (anyone nearby) or upgrade (owner) |
| Let players move their own DarkRP entities (like FPP) | By default only admins (`props.admin`) may physgun or tool shop entities (printers, ...); owners may not. Allow it for a group: `permissions.Grant("user", { "darkrp.entities.physgun", "darkrp.entities.tool" })` in a shared config file, or for one entity with `ownerPhysgun = true` / `ownerTool = true` in its `DarkRP.createEntity` |
| See the server browser with sample servers | `rp_browser_test_servers 1` in the console (0 hides them again). They are made up and can't be joined |
| Change the DarkRP M menu | Override `GM:MenuTabs()` (`{ id, label, Material Icons name }`, build it in `GM:MenuBuild_<id>(body)`) or `GM:MenuCommands()` (the Commands tab: `{ group, { { name, description, chat command, input placeholder } } }`) |
| Give a job weapons | `weapons = { "weapon_pistol" }` in `config/sh_jobs.lua` |
| Change what everyone spawns with | `GM.DefaultLoadout` (DarkRP: `config/sh_config.lua`, fists + physics gun + tool gun) |
| Add a weapon | a new file `gamemode/weapons/sh_weapon_<name>.lua` (or an addon file) with a `SWEP` table; copy `sh_weapon_smg.lua` and change the numbers. Models and sounds from sbox.game: put the package idents (`facepunch.w_mp5`) in `gamemode.json` → `"packages"` so players download them |
| Weapon sits wrong in the hand | hold it, look at yourself in third person (X), `rp weapon_offset x y z [pitch yaw roll]` until it fits, paste the printed `SWEP.WorldModelOffset/Angles` lines into the weapon file |
| Add a tool | a new file `gamemode/tools/sh_<mode>.lua` (or in an addon: `tools.LoadFolder("tools")`); copy `sh_remover.lua` |
| Allow more materials in the material tool | add `{ "Name", "materials/....vmat" }` to `tools.Get("material").Materials` (only listed materials can be used) |
| Add a tab to the Q menu | `spawnmenu.AddCreationTab("My tab", function(parent, search) ... end, "star", 60)` (client file); right-hand pages: `hook.Add("PopulateToolMenu", "id", function() spawnmenu.AddToolMenuOption("Utilities", "User", "mypage", "My page", "", "", function(panel) panel:Slider(...) end) end)` |
| Add NPCs / vehicles / entities the GMod way | `list.Set("NPC", "id", { Name = "...", Class = "...", Model = "...", Category = "..." })` (shared file), same for `"Vehicles"`, `"SpawnableEntities"` (`PrintName, ClassName, Category`); permissions `spawnmenu.npc`, `spawnmenu.vehicle`, `spawnmenu.entity.<class>` (admin) |
| Add a context-menu action (hold C) | `properties.Add("name", { MenuLabel = "...", Filter = function(self, ent, ply) ... end, Receive = function(self, ent, ply) ... end })` |
| Change limits while the server runs | Q menu > Utilities > Server settings (admins, permission `server.settings`); saved in the server's storage |
| Add a sound to the speaker tool / a wheel to the wheel tool | `table.insert(tools.Get("speaker").Sounds, { "Name", "sounds/x.sound" })`, `table.insert(tools.Get("wheel").Models, { "Name", "models/x.vmdl", "z" })` (axis "z" or "x") |
| Add props to the spawn menu | `spawnmenu.AddPropCategory("My props", { "models/....vmdl", "org.package" })` in a shared file; packages must also be in `"packages"` |
| Add spawnable entities | `spawnmenu.AddEntity("my_thing", { name, category, model, permission = "admin", Spawn = function(ply, trace) ... end })` |
| Change the prop limit | `GM.PropLimit` (DarkRP: 30, base: 50); `GM.EntityLimit` for spawn-menu entities (10) |
| Change the tool gun limits | `GM.Limits = { thrusters = 20, balloons = 30 }` in the gamemode config (DarkRP: `config/sh_config.lua`); only list what you change, `0` = unlimited. Categories: balloons, buttons, cameras, emitters, hoverballs, lights, speakers, spawners, texts, thrusters, wheels, constraints, ropes. Admins (permission `props.nolimit`) are not limited. In game: Q menu > Utilities > Server settings (permission `server.settings`), saved on the server and stronger than the config |
| Decide who may do what | permissions (`rp permissions` lists them): `props.spawn`, `props.spawn.cloud` (search sbox.game in the spawn menu, admins by default), `props.nolimit`, `props.admin` (touch everyone's props, `/cleanupall`), `tool.<mode>`, `spawnmenu.open`, `spawnmenu.entity.<id>`, `weapons.give.self` (Weapons tab, `/giveweapon`) |
| Keep props after a player leaves | `GM.RemovePropsOnDisconnect = false` |
| Block the physics gun on something | hook `PhysgunPickup(ply, ent)` returning false; for tools `CanTool(ply, trace, mode)` |

Players: hold **Q** for the spawn menu, **Z** undoes the last prop/tool action (`/undo`), `/cleanup` removes your props.
Physics gun: hold left mouse, wheel = closer/further, hold E + mouse = rotate, right click = freeze, R = unfreeze.

**Content that works everywhere:** s&box itself ships `models/dev/*`, `models/citizen_props/*` and `materials/dev/*`, so those exist on every server and client. Editor-only content (e.g. `models/sbox_props/...`) is missing in the real game.

Models from sbox.game packages work when listed in `"packages"`; a few community packages ship textures s&box can't stream (they show up grey), so check new packages in the real game.


- **Bots** (testing): `rp_bot [count] [name]` in the console spawns bot players that wander about (`rp_bot_kick [name|all]` removes them, `rp_bot_mode stand` makes them stand still); in game the permission `base.bot` (default admin) is needed. Max 32.

## Applying changes

- **`rp_lua_reload`** in the server console (or the host's console) reloads the running gamemode:
    - The new files are loaded first. **If one has an error, the reload is refused, the old scripts keep running**, and
    the console shows the file and line.
    - Entities the gamemode created (dropped items, placed doors) are recreated from saved data.
    - Players get `PlayerInitialSpawn` again. Connected players download the changed client files automatically.
    - Only the server can reload; on a client the command does nothing.
- **Restarting the server** also applies changes.

## Adding a new gamemode

```
roleplay/lua/gamemodes/myrp/gamemode.json
roleplay/lua/gamemodes/myrp/gamemode/sh_init.lua
roleplay/lua/gamemodes/myrp/gamemode/sv_init.lua
roleplay/lua/gamemodes/myrp/gamemode/cl_init.lua
```

```json
{ "id": "myrp", "title": "My RP", "version": "1.0.0", "apiVersion": 1,
  "entry": { "shared": "gamemode/sh_init.lua", "server": "gamemode/sv_init.lua", "client": "gamemode/cl_init.lua" },
  "dependencies": [ "base" ], "maps": { "default": "minimal" } }
```

Quicker: copy `gamemodes/_template/` to `gamemodes/myrp/` and change `"id"` to `"myrp"` (it must match the folder
name) and the title. The template derives from base and has one example module.

Deriving from `base` gives you chat and the scoreboard for free. Override anything with `function GM:Name(...)`,
and call `self.BaseClass.Name(self, ...)` to keep the base behaviour.

To run it, set `"DefaultGamemode": "myrp"` in `framework.json` and restart, or pick it in **Create Local Server**.

## Addons

An addon is Lua that runs **on top of** the gamemode: a chat command, a HUD widget, an admin tool. It doesn't replace
anything, so you can add features without editing the gamemode, and switch them off again per server.

```
roleplay/lua/addons/myaddon/addon.json
roleplay/lua/addons/myaddon/sh_*.lua   sv_*.lua   cl_*.lua
```

```json
{ "id": "myaddon", "title": "My Addon", "version": "1.0.0", "apiVersion": 1,
  "gamemodes": [ "base" ],
  "dependencies": { "otheraddon": ">=1.2.0" } }
```

- **Installing:** drop the folder into `roleplay/lua/addons/` and run `rp_lua_reload` (or restart). Every installed addon
  is **on** unless you switch it off. Start from `addons/_template/`: copy it and set `"id"` to the folder name.
- **Files:** every `sh_`, `sv_` and `cl_` file directly in the addon folder loads (shared first, then the realm's own,
  alphabetically). Put more files in subfolders and `include("sub/sh_x.lua")` them, or name exact files with
  `"entry": { "shared": ..., "server": ..., "client": ... }` like a gamemode.
- **`gamemodes`:** the addon only runs with these gamemodes or gamemodes derived from them (`"base"` = every gamemode
  built on base, DarkRP and Sandbox RP included). Leave it out for "any gamemode".
- **`dependencies`:** other addons that must be on, with an optional version rule: `"*"` any, `"1.2.0"` exactly,
  `">=1.2.0"`, `"<2.0.0"`, `"^1.2.0"` (1.x from 1.2.0), `"~1.2.0"` (1.2.x); combine with a space
  (`">=1.0.0 <2.0.0"`). Dependencies load first.
- **Load order:** framework, then the gamemode, then the addons (dependencies first, otherwise A–Z). So addons can
  override `GM` functions and add hooks.
- **Players** download the `sh_`/`cl_` files of the addons that are on, like gamemode files; `sv_` files never leave
  the server. Switched-off addons are not sent at all.
- **A broken addon** (an error while it loads) is skipped and reported; the gamemode and the other addons keep running.
  Addons that depend on it are skipped too.
- `"packages"` / `"collections"` work like in gamemode.json.

| Console command (server / host) | Does |
|---|---|
| `rp_addons` | Lists every installed addon: version, where it comes from, and whether it is loaded, off, made for another gamemode, waiting for a dependency or broken (with the reason) |
| `rp_addon_disable <id>` | Switches it off (saved in `framework.json` → `"DisabledAddons"`) |
| `rp_addon_enable <id>` | Switches it on again |

Both take effect with `rp_lua_reload` or a restart. You can also edit the list directly:
`"DisabledAddons": [ "roll" ]`.

## Live editing (DevMode)

With `"DevMode": true` in `framework.json`, the server checks its Lua files every 2 seconds and runs `rp_lua_reload` by itself when one changed (the running gamemode and its bases, every addon). Save a file and see the change a moment later, players included.

A file with an error is reported once and the previous scripts keep running until you fix it. **Only for testing: never enable DevMode on a public server.**


## Getting the original back

**`rp_lua_restore <id>`** (e.g. `rp_lua_restore darkrp`) moves your copy to `lua_backups/<id>-<time>/` and copies the
game's version in. Then run `rp_lua_reload`. It works for built-in addons too (`rp_lua_restore roll`, or
`rp_lua_restore addon:<id>` when a gamemode has the same id).

## Game updates

When the game ships changed files for a built-in gamemode or addon, your copy is **updated automatically on start**:

1. The whole copy is backed up to `lua_backups/<id>-<time>/`.
2. Each file is compared with what your copy was made from (`.rp_builtin.json` in the gamemode folder remembers that -
   leave it alone):
      - files you never changed get the game's new version;
      - files only you changed are kept;
      - files both you and the update changed get the game's version, and the log lists them so you can merge your
     changes back from the backup;
      - files you added stay; files the game dropped are removed if you never changed them.

Copies made before this existed have no `.rp_builtin.json`: they are replaced completely (after the backup) when the
game's version number is higher, and stamped otherwise.

Don't want that? `"LuaAutoUpdate": false` in `framework.json`: the log only tells you, and you update with
`rp_lua_restore <id>`.

## Rules the loader enforces

- **File names:** lowercase, starting with `sh_` (runs on server and players), `sv_` (server only, **never sent to
  players**) or `cl_` (players only).
- **Paths:** `include("gamemode/file.lua")` is relative to your gamemode folder; `..` is not allowed.
- **Public files:** `sh_` and `cl_` files are sent to every player who joins, so don't put secrets in them.
- **Sandbox:** no file system, OS, network or .NET access beyond the documented API (`Docs/LUA_API.md`). Data that
  should survive restarts goes through `storage.Get/Set`.

## Choosing the Lua source

`framework.json` → `"LuaSource"`:

| Value | Meaning |
|---|---|
| `"data"` (default) | The editable copy in the data folder: servers, local hosts and the editor |
| `"builtin"` | The game's own files, ignoring the data folder: for framework developers editing `Assets/lua` directly |

The same applies to addons: a folder in `roleplay/lua/addons/` replaces the game's addon with the same id.
