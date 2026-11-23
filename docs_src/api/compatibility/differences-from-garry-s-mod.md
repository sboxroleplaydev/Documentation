---
description: "Differences from Garry's Mod: Lua version: Lua 5.1 with GLua operators. No LuaJIT, bit, coroutines or goto."
---

# Differences from Garry's Mod

- **Lua version:** Lua 5.1 with GLua operators. No LuaJIT, `bit`, coroutines or `goto`.
- **Networking:** GMod-style `#!lua net.Start`/`WriteX`/`ReadX` works, but values travel as a list (bit sizes are ignored).
- **Client files:** `AddCSLuaFile` exists and does nothing: every `sh_`/`cl_` file is distributed automatically.
- **Addons:** GMod's `lua/autorun/` doesn't exist; addons are folders with an `#!lua addon.json` (see "Addons").
- **Players:** health, death and teams are gamemode concepts (DarkRP keeps health in NW vars). There is no engine
  damage system, ragdoll or player model API; weapons are base's Lua SWEP system (see "Weapons").
- **Movement:** GMod's speed/jump setters exist (see "Movement"); `SetJumpPower` is in GMod units and scaled to the
  map's gravity. No `SetMaxSpeed`, `SetStepSize` or `SetHull` yet; s&box's controller does the walking.
- **UI and commands:** UI is panels + CSS (plus `draw`/`surface` for immediate drawing); no VGUI/Derma (base has its own components: "UI components").
  `concommand` commands are typed as `rp <command>`.

