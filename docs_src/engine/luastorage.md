---
description: "Server-side persistent storage for gamemodes: storage.Get(key), storage.Set(key, value), storage.Delete(key), storage.Exists(key), storage.Flush()."
---

# LuaStorage

Source: `Code/Framework/Scripting/Api/LuaStorage.cs`

Server-side persistent storage for gamemodes: `storage.Get(key)`, `storage.Set(key, value)`, `storage.Delete(key)`, `storage.Exists(key)`, `storage.Flush()`.

Values are any serializable Lua value (see `LuaSerializer.Storage` limits). Each key is one JSON file in
data/roleplay/storage/<gamemode>/<key>.json. Writes are cached and flushed every few seconds, on
`storage.Flush()` and at shutdown, through the crash-tolerant `SafeDataFile`. Corrupt files are
kept aside and read as nil. Gamemodes cannot read each other's storage or anything outside their folder.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
