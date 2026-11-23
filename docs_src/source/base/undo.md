---
description: "Undo (client): Z runs 'undo'; the server's answer shows as a notification."
---

# base: module `undo`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/undo/`

## `cl_undo.lua` (client)

Undo (client): Z runs "undo"; the server's answer shows as a notification.

## `sv_undo.lua` (server)

Undo (GMod's undo library, server). Tools and the spawn menu record what a player made; "undo" removes the newest.
```lua
undo.Create("Prop")
undo.AddEntity(ent)
undo.AddFunction(fn, args...)
undo.SetPlayer(ply)
undo.SetCustomUndoText("Undone my thing")
undo.Finish()   -- -- one entry; Finish pushes it
undo.Do(ply) -> true if something was undone
undo.GetTable(ply) -> the player's entries   -- newest last
undo.ReplaceEntity(old, new)   -- -- e.g. when a tool swaps an entity
```

Players: Z (rebindable), "rp undo" or /undo. Hook CanUndo(ply, entry) -> false blocks.

Functions defined:

- `undo.Create(name)`
- `undo.AddEntity(ent)`
- `undo.AddFunction(fn, ...)`
- `undo.SetPlayer(ply)`
- `undo.SetCustomUndoText(text)`
- `undo.Finish(text)`
- `undo.Sync(ply)`
- `undo.GetTable(ply)`
- `undo.ReplaceEntity(old, new)`
- `undo.Do(ply)`
- `undo.DoEntry(ply, n)`
