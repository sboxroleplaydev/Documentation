---
description: "Common Garry's Mod helpers, so GMod-style code finds what it expects:"
---

# GMod compatibility helpers
<span class="realm realm-shared">Shared</span>

Common Garry's Mod helpers, so GMod-style code finds what it expects:

- **Types:** `isstring`, `isnumber`, `isbool`, `istable`, `isfunction`, `isentity`, `isvector`, `isangle`, `tobool`
  (false for nil, false, 0, "0", "false").
- **Output:** `Msg`, `MsgN`, `MsgC` (colours ignored), `PrintTable`.
- **string:** `Split`, `Left`, `Right`, `Replace` (plain text), `PatternSafe`, `TrimLeft/TrimRight([char])`,
  `ToTable`, `Comma`, `#!lua FormattedTime(seconds [, format])`, `NiceTime`, `StartsWith`.
- **table:** `Random` (value, key), `KeyFromValue`, `RemoveByValue`, `Merge` (deep), `Add`,
  `#!lua SortByMember(t, member [, ascending])`, `Reverse`, `Empty`, `ClearKeys`.
- **math:** `Approach`, `Remap`, `Rand`, `Distance`, `Truncate`.
- **player:** `GetBySteamID`, `GetBySteamID64`, `GetHumans`.
- **JSON:** `#!lua util.TableToJSON(t [, pretty])`, `#!lua util.JSONToTable(json)` (nil for invalid JSON). Like GMod: sequential
  tables → arrays (`{}` → `[]`), Vectors → `"[x y z]"`, Angles → `"{p y r}"`, and back when reading; integer-like keys
  become numbers again. Limits: 1,000,000 characters, depth 64; a table containing itself is an error.
- **team:** `#!lua team.SetUp(id, name, color [, joinable])`, `GetName`, `GetColor`, `Valid`, `Joinable`, `GetAllTeams`,
  `GetPlayers`, `NumPlayers`, `TEAM_CONNECTING/UNASSIGNED/SPECTATOR`; `#!lua ply:Team()`, server `#!lua ply:SetTeam(id)`
  (NW int `team`).
- **net (GMod style):** `#!lua net.Start(name)`, `net.WriteString/Int/UInt/Float/Double/Bool/Bit/Table/Vector/Normal/Angle/Color/Entity/Data`, then `#!lua net.Send(ply|{plys})`, `#!lua net.Broadcast()` or `#!lua net.SendToServer()`; `#!lua net.Receive(name, function(len, ply) ... net.ReadX() ... end)` (`ply` is nil on the client; `len` is the number of values, not bits). `#!lua util.AddNetworkString` exists and does nothing.

    Messages sent with `#!lua net.Start` reach receivers GMod-style; the framework form `#!lua net.Send(name, ply, data)` / `#!lua fn(ply, data)` still works. Use one style per message name. Bit sizes are ignored; tables travel as JSON, entities by id (players by SteamID);

    a missing entity reads as `NULL`.

- **timer extras:** `#!lua timer.Adjust(id, delay [, reps [, fn]])`, `Pause`, `UnPause`, `Toggle`, `Stop` (paused and
  reset), `Start` (restart a full interval), `TimeLeft` (negative while paused, like GMod), `RepsLeft`, `Destroy`.
- **Players/entities:** `IsPlayer`, `IsBot`, `IsNPC`, `IsWorld`, `EyePos`, `EyeAngles` (players), server
  `#!lua ply:PrintMessage(HUD_PRINTTALK, text)` (all kinds go to chat), `NULL` (`#!lua IsValid(NULL)` is false), `HUD_PRINT*`.
- **Console commands:** `#!lua concommand.Add(name, function(ply, cmd, args, argStr) end [, autoComplete, helpText])`, `#!lua concommand.Remove`, `#!lua concommand.GetTable`, `#!lua RunConsoleCommand(name, ...)`. s&box can't add console commands at runtime, so players and server owners type **`rp <command> [args]`** (`rp` alone lists them).

    A command defined in the client realm runs there (ply = local player); otherwise a client sends it to the server (rate-limited), where ply is that player; in a dedicated server's console ply is nil.

- **Data files** (GMod `"DATA"`): `#!lua file.Read(path, "DATA")`, `#!lua file.Write(path, text)`, `#!lua file.Append`, `#!lua file.Delete`, `#!lua file.CreateDir`, `#!lua file.IsDir(dir, "DATA")`, `#!lua file.Size(path, "DATA")`, `#!lua file.Exists(path, "DATA")`, `#!lua file.Find(pattern, "DATA")`.

    Server realm: `data/roleplay/data/<gamemode>/`; client realm: one folder per server (`data/roleplay/clientdata/<server>/`). Paths: a-z, 0-9, `_ - . /`, no `..`; writable: .txt .json .dat .csv. Limits: 4 MB per file; 100 MB / 2,000 files (server), 20 MB / 500 files (client).

    Without "DATA", `#!lua file.Find` and `#!lua file.Exists` still look at the gamemode's own scripts.

- **User groups:** `#!lua ply:GetUserGroup()` (NW string `usergroup`, default "user"), server `#!lua ply:SetUserGroup(g)`,
  `#!lua ply:IsUserGroup(g)`, `#!lua ply:IsAdmin()` (admin or superadmin), `#!lua ply:IsSuperAdmin()`. Gamemodes with their own ranks
  override `GetUserGroup` (DarkRP does); `IsAdmin`/`IsSuperAdmin` then follow those ranks.

