---
description: "Based on the official s&box guides (Dedicated Servers,"
---

# Running a Dedicated Server

Based on the official s&box guides ([Dedicated Servers](https://sbox.game/dev/doc/networking/dedicated-servers/),
[Running Local Projects](https://sbox.game/dev/doc/networking/dedicated-servers/running-local-projects)) and tested with
this project on 2026-11-18 (engine 26.11.10a).

## Install

```
steamcmd +login anonymous +app_update 1892930 validate +quit
```

The server installs to `steamcmd/steamapps/common/sbox dedicated server`. An s&box game install also contains
`sbox-server.exe`.

**Steam client libraries are required.** On Windows, install the Steam client. On Linux, symlink `steamclient.so`
into `~/.steam/sdk64/`, as the official guide describes.

## Start

Published game:

```
sbox-server.exe +game <org.gameident> +hostname "My RP Server"
```

This local project (tested):

```
sbox-server.exe +game "C:/path/to/roleplay/roleplay.sbproj" +hostname "My RP Server"
```

| Flag | Meaning |
|---|---|
| `+game <ident or .sbproj path> [map]` | What to run |
| `+hostname <name>` | Server name shown in the browser (the framework uses it as the lobby name) |
| `+port <port>`, `+net_query_port <port>` | Ports |
| `+net_allow_local 1` | Allow `connect local` from the same machine (testing) |
| `+net_game_server_token <token>` | Stable server Steam id across restarts (only available once s&box is released, per the official guide) |

## Choosing the map

A map is either a built-in scene (`minimal`, the test world) or **any map package from sbox.game** (e.g.
`thieves.rpdowntown3t`). Cloud maps are downloaded on first use (≈30–50 s the first time, faster afterwards) and
loaded before the gamemode starts. Joining players download them automatically, and the server waits for their map to
finish loading before spawning them.

The first of these that is set wins:

1. **Command line:** `sbox-server.exe +game <game> <map> ...`, e.g. `+game ".../roleplay.sbproj" thieves.rpdowntown3t`.
2. **Server config:** `"Map": "thieves.rpdowntown3t"` in `framework.json`.
3. **The gamemode's default map**, from its `gamemode.json` (`"maps": { "default": ... }`). DarkRP defaults to
   `thieves.rpdowntown3t`, Base to `minimal`.

The map is shown in the server browser and available to Lua as `game.GetMap()`.

**DarkRP doors on cloud maps.** Rp Downtown ships without doors. Admins place them in game:

- `/adddoor [price] [width] [title…]`: aim at the floor on the hinge side of a doorway. The door swings from that
  point and extends to your left.
- `/removedoor`: look at a placed door to remove it.
- **Door Placer tool** (tool gun, category DarkRP, permission `admin.doors`): use real models, including sbox.game cloud models. Spawn a door model from the Q menu, put it in the doorway, set title/price, left click it with the tool: it becomes a saved door (hinge at one end of its long side, swings away from you or toward you).

    Left click a door again updates title/price, right click removes it, reload flips the hinge. Or enter a model path/package ident and click the floor. Tick **Double door**: the second leaf shows as a green ghost beside the model (right click picks the side), yellow lines mark the hinges (both at the outer ends, the leaves swing the same way).

    All doors swing smoothly (0.5 s, `DarkRP.DoorOpenTime`) with a wood knock when opened and a thud when shut (engine sound events; the engine has no door sounds, change `DarkRP.DoorSounds`). Records with a model store `model`, hinge position `x,y,z`, `yaw`, the model offset `ox,oy,oz` and the swing direction `dir` (1 or -1).


**Glass Placer tool** (tool gun, category DarkRP, permission `admin.doors`): aim at a window frame or at the wall next to an opening. A preview shows the glass (green outline and fill; other openings near your aim in blue), **R** switches between those openings, left click fills the picked one with a glass pane (engine glass shader, material `materials/glass/rp_glass.vmat`) in the middle of the wall and saves it per map (`storage/darkrp/mapglass/<map>.json`).

Right click removes a pane. Openings are found by probing straight through the wall on a grid, so any frame with collision works (windows, bars, doorways); walls are assumed vertical. The best match (the opening your aim is in or touches) comes first.

Arches and other odd outlines are filled with a few boxes that follow the shape (at most 12 per pane). `/noclip` toggles noclip for the owner (permission `admin.noclip`, default superadmin; the listen host is superadmin).


Placed doors are saved per map in the server's storage (`roleplay/storage/darkrp/mapdoors/<map>.json`), so server
owners can also edit that file directly. Door ownership survives restarts.

## Cloud content (packages)

Servers can require sbox.game packages (models, materials, sounds, …). Packages published through the Steam Workshop
are packages too. List them in the server's `framework.json`:

```json
"Packages": [ "fish.barrel", "org.another_package" ]
```

### Collections: one JSON file with all ids

Instead of listing everything in every server's config, put the ids into a **collection**: a JSON file on any web
server (or a file on the server). Edit it once, and every server using it gets the new content on its next start.

```json
"Collections": [ "https://example.com/rp/content.json", "collections/extra.json" ]
```

```json
{ "packages": [ "fish.barrel", "zethell.barrel", "https://sbox.game/org/name" ] }
```

(a plain array `[ "fish.barrel", … ]` works too). URLs are fetched over HTTP(S) with a 15 s timeout and a 64 KB limit.
A path is relative to the server's `data/<org>/<game>/roleplay/` folder. Unreachable or broken collections and invalid
entries are logged and skipped.

### Where the list comes from

All sources are combined and de-duplicated (max 128 packages):

- `framework.json`: `"Packages"` and `"Collections"`;
- each gamemode of the chain, in `gamemode.json`: `"packages"` and `"collections"` (a path there is relative to the
  gamemode folder, e.g. `"content.json"`);
- Lua: `content.AddPackage` / `content.AddCollection` (see `LUA_API.md`), also while the server is running.
- The **server** mounts everything before the map loads.
- **Joining players** receive the list with the scripts and mount the same packages before the gamemode's client Lua
  starts.
- **Failures are skipped:** a package that can't be found or mounted is logged and skipped; the server still starts.
- **Added while running** (from Lua): the server mounts the package, then every connected player mounts it too.

In Lua, a mounted package can be used directly: `ents.Create("prop", { model = "fish.barrel", ... })` uses the
package's main model.

**Steam Workshop collection ids** are not supported: game code can't use s&box's Workshop API. Use a JSON collection
instead (above).

## What the framework does on a dedicated server

1. **Boots headless:** the role shows as `dedicated server` in logs and Diagnostics.
2. **Hosts itself immediately:** no one presses "Create Local Server". It loads the world scene, loads the gamemode in
   the **server realm only** (a dedicated server has no client realm), and creates a **public** lobby named after
   `+hostname`.
3. **Publishes browser metadata:** one packed lobby key `rp = gamemode|frameworkVersion|protocol|map`, used by the
   in-game server browser (gamemode, framework version, compatibility check, map).
4. **Serves scripts to joining clients:** shared/client Lua is downloaded and verified on join. Server (`sv_`) Lua is
   never sent.

Server-local settings live in the server's own data folder, at `data/.../roleplay/framework.json`:

```json
{ "DefaultGamemode": "darkrp", "Map": "", "ServerName": "Roleplay Server", "MaxPlayers": 32, "ServerPassword": "",
  "DevMode": false, "DisabledAddons": [] }
```

- `+hostname` overrides `ServerName`.
- `ServerPassword` sets a lobby password. Players are asked for it by s&box's own password dialog.
- `DisabledAddons` lists Lua addons this server doesn't run (see `SERVER_OWNERS.md`, "Addons"; `rp_addons` lists them).
- **Never enable `DevMode` on a public server.** (It also reloads Lua automatically whenever a file changes.)

Gamemode data (profiles, doors, admin groups) is stored in the server's data folder under `roleplay/storage/<gamemode>/`.
The audit log is in `roleplay/audit/`.

## Making yourself admin (DarkRP)

On a dedicated server there is no listen host, so nobody is superadmin by default. Add your SteamId64 to the
server's `roleplay/storage/darkrp/admins.json`, then restart the server or rejoin:

```json
{ "7656119XXXXXXXXXX": "superadmin" }
```

After that, `/setgroup <player> <group>` works in game.

## Joining

- **In game:** Main menu → **Browse Servers** → Join. The list shows public lobbies of this game from Steam.
- **Direct Connect:** use the lobby id the server prints with the `status` console command, or `local` for a server
  on the same machine started with `+net_allow_local 1`.
- **Console:** `connect <lobbyId>` (engine), or `rp_connect <lobbyId|local>` (framework).

Connections go through Steam's relay by default. The official guide doesn't document direct IP:port joining.

## Tested

| Check | Result |
|---|---|
| `sbox-server.exe +game <roleplay.sbproj> +hostname "RP Dedicated Test" +net_allow_local 1` | Booted `role=dedicated server, headless=True`; 4 startup stages OK; found base 0.1.0 + darkrp 0.2.0 |
| Self-hosting | "Starting dedicated server 'RP Dedicated Test' (gamemode darkrp, max 32, Public)"; server realm ready (18 files, manifest 17); "DarkRP 0.2.0 ready: 4 jobs, 3 items, 2 doors"; Steam "Server started!" |
| Discovery from another process (the editor's menu) | Listed as "RP Dedicated Test", darkrp, fw 0.1.0, protocol 2 (compatible), map minimal, 0/32, ping ~32, Join button (screenshot) |
| `+game <roleplay.sbproj> minimal +hostname "RP Map Arg Test"` | The launch map overrode DarkRP's default: "Starting dedicated server … map minimal", 2 scene doors loaded, metadata `darkrp\|0.1.0\|2\|minimal` |
| Joining it | **Not verified.** The editor can't join other servers from play mode (see "Known limits"), and a standalone game client can't run while the editor is open on the same account. |

## Known limits

- **Joining from the editor doesn't work.** Joining a server from the **editor's play mode** fails with "GameInstance
  load failed" and unloads the project's code in the editor until it is restarted. The framework now refuses joins
  from the editor with a clear message. Test joining with the real game client.
- **Editor lobbies are invisible.** Editor-hosted lobbies are always private, so they never show in any browser.
- **No region data.** The platform's lobby information has no region, so the browser can't filter by region.
