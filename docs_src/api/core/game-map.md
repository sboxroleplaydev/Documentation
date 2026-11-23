---
description: "game.IsEditor() is true inside the s&box editor's play mode. game.GetServerName() ('' offline),"
---

# Game / map

`#!lua game.IsEditor()` is true inside the s&box editor's play mode. `#!lua game.GetServerName()` ("" offline),
`#!lua game.IsMultiplayer()`, `#!lua game.IsHost()` (true offline and on the server/listen host); client:
`#!lua game.LeaveToMenu()` (disconnects, a host stops its server; runs at the start of the next frame).

**`gui` (client, s&box's own overlays, GMod names where they exist):** `#!lua gui.ActivateGameUI()` opens s&box's escape
menu, `#!lua gui.HideGameUI()` closes it, `#!lua gui.OpenSettings([page])` (`display`, `graphics`, `audio`, `controls`,
`keybinds`, `game`, `storage`, `developer`, `about`), `#!lua gui.OpenBinds()`, `#!lua gui.OpenPlayerList()`.

 `#!lua game.GetMap()` returns the current map id (`"minimal"`, `"thieves.rpdowntown3t"`, …). `#!lua game.IsDedicated()` returns
true on a dedicated server.

Gamemodes declare their maps in `#!lua gamemode.json`:

```json
"maps": { "default": "thieves.rpdowntown3t", "available": [ "thieves.rpdowntown3t", "minimal" ] }
```

The default is used when the host doesn't pick one. The available list fills the map selector in Create Local Server,
where any other sbox.game map package can also be typed in.

