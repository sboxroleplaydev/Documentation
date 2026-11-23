---
description: "storage.Get(key), storage.Set(key, value), storage.Delete(key), storage.Exists(key), storage.Flush()."
---

# Storage
<span class="realm realm-server">Server</span>

`#!lua storage.Get(key)`, `#!lua storage.Set(key, value)`, `#!lua storage.Delete(key)`, `#!lua storage.Exists(key)`, `#!lua storage.Flush()`.

- **Keys:** `a-z 0-9 _ -` with `/` between parts, up to 96 characters (e.g. `players/7656…`).
- **Scope and format:** per gamemode, one JSON file per key. Values use the same types as `net` payloads, but up to
  512 KB and nesting 16.
- **Writes:** cached and flushed every 3 s, on `#!lua Flush()`, and at shutdown, with crash-tolerant writes. Corrupt files are
  kept aside and read as nil.

`#!lua log.Audit(category, message)` appends to `data/roleplay/audit/<date>.log`.

