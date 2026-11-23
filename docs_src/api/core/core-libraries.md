# Core libraries

| API | Realm | Notes |
|---|---|---|
| `#!lua include(path)` | both | Relative to the gamemode folder: lowercase, `/`, no `..`. The realm prefix is enforced. |
| `hook.Add/Remove/Run/GetTable` | both | Insertion order; the first non-nil return wins, then `#!lua GM:event`. Errors are isolated. |
| `timer.Simple/Create/Remove/Exists` | both | A timer that errors is removed. Max 512. |
| `print`, `ErrorNoHalt`, `CurTime`, `RealTime`, `SysTime` | both | |
| `#!lua FindMetaTable("Player" \| "Entity" \| "Panel")` | both | Add your own methods, e.g. `#!lua function PLAYER:GetMoney() ... end`. |
| `Color`, `Vector`, `Angle`, `IsValid`, `IsColor/IsVector/IsAngle`, `math.Clamp/Round`, `string.Trim/StartWith/EndsWith/Explode`, `table.Count/HasValue/Copy/GetKeys/IsEmpty` | both | |

