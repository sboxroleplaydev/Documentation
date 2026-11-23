---
description: "Numpad (client): reports presses and releases of the keys your tools use (see shnumpad.lua)."
---

# base: module `numpad`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/numpad/`

## `cl_numpad.lua` (client)

Numpad (client): reports presses and releases of the keys your tools use (see sh_numpad.lua).
The watched keys are every tool setting named "key..." (TOOL.ClientConVar.key, key_up, ...), read from the cookies.

Functions defined:

- `numpad.GetWatched()`

## `sh_numpad.lua` (shared)

Numpad / key controls for contraptions (GMod's numpad library, with any keyboard key).
A tool that makes a controllable thing (thruster, motor, hydraulic, button, ...) lets the player pick a key
(TOOL.ClientConVar entries whose name starts with "key") and registers a listener on the server:
```lua
local id = numpad.On(ply, "kp_1", function(ply, down) ... end, ent)   -- called when that player presses / releases the key
numpad.Remove(id)
numpad.RemoveFor(ent)   -- (listeners of a removed `ent` go away on their own)
numpad.Activate(ply, key, down)   -- -- run the listeners by hand (a button entity does this)
```

The client only reports keys it was told to watch (numpad.GetWatched), so nothing is sent for keys nobody uses.
numpad.Keys is the list the key pickers offer (kp_0 .. kp_9 and a few more); numpad.IsKey(k) checks a key name.

Functions defined:

- `numpad.IsKey(k)`
- `numpad.KeyLabel(k)`

## `sv_numpad.lua` (server)

Numpad (server): listeners per player and key; the client reports presses of keys it watches.

Functions defined:

- `numpad.On(ply, key, fn, ent)`
- `numpad.Remove(id)`
- `numpad.RemoveFor(ent)`
- `numpad.Activate(ply, key, isDown)`
