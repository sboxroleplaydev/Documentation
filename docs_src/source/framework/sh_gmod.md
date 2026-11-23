---
description: "Garry's Mod compatibility helpers (shared, pure Lua). Loaded after shcore.lua in every realm, so GMod-style code"
---

# `framework/sh_gmod.lua`

Garry's Mod compatibility helpers (shared, pure Lua). Loaded after sh_core.lua in every realm, so GMod-style code
(addons, ported gamemodes) finds the functions it expects. Names and behaviour follow the GMod wiki.

Functions defined:

- `string.Split(s, separator)`
- `string.Left(s, n)`
- `string.Right(s, n)`
- `string.TrimLeft(s, char)`
- `string.TrimRight(s, char)`
- `string.PatternSafe(s)`
- `string.Replace(s, find, replace)`
- `string.ToTable(s)`
- `string.Comma(n, separator)`
- `string.FormattedTime(seconds, format)`
- `string.NiceTime(seconds)`
- `table.Random(t)`
- `table.KeyFromValue(t, value)`
- `table.RemoveByValue(t, value)`
- `table.Merge(dest, source)`
- `table.Add(dest, source)`
- `table.SortByMember(t, member, ascending)`
- `table.Reverse(t)`
- `table.Empty(t)`
- `table.ClearKeys(t)`
- `math.Approach(current, target, change)`
- `math.Remap(value, inMin, inMax, outMin, outMax)`
- `math.Rand(low, high)`
- `math.Distance(x1, y1, x2, y2)`
- `math.Truncate(n, digits)`
- `player.GetBySteamID(steamid)`
- `team.SetUp(id, name, color, joinable)`
- `team.Valid(id)`
- `team.GetName(id)`
- `team.GetColor(id)`
- `team.Joinable(id)`
- `team.GetAllTeams()`
- `team.GetPlayers(id)`
- `team.NumPlayers(id)`
