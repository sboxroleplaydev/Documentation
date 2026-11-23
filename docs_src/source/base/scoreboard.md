---
description: "Base scoreboard (client). Hold Tab. Derived gamemodes change the columns by overriding"
---

# base: module `scoreboard`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/scoreboard/`

## `cl_scoreboard.lua` (client)

Base scoreboard (client). Hold Tab. Derived gamemodes change the columns by overriding
```lua
GM:ScoreboardColumns() and GM:ScoreboardRow(ply)
or the whole thing via GM:ScoreboardCreate()
```

Functions defined:

- `GM:ScoreboardColumns()`
- `GM:ScoreboardRow(ply)`
- `GM:ScoreboardTitle()`
- `GM:ScoreboardCreate()`
- `GM:ScoreboardShow()`
- `GM:ScoreboardHide()`
- `GM:ScoreboardThink()`
- `GM:ScoreboardRebuild()`
