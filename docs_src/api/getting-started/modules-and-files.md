---
description: "Base gamemode: GM:LoadModules(dir [, order]) loads every folder in dir (relative to the calling gamemode) as a"
---

# Modules and files

Base gamemode: `#!lua GM:LoadModules(dir [, order])` loads every folder in `dir` (relative to the calling gamemode) as a
module: its `sh_*.lua` files in both realms, then `sv_*.lua` (server) or `cl_*.lua` (client), alphabetically.
Names in `order` load first. `#!lua GM.LoadedModules` lists what was loaded.

`#!lua file.Find("gamemode/modules/*")` → files, folders (sorted) inside the gamemode's own Lua folder;
`#!lua file.Exists(path)`. Read-only; on a client only the shared/client files the server sent are visible.
`#!lua AddCSLuaFile()` exists for GMod compatibility and does nothing.

