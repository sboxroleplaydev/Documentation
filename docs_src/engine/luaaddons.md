---
description: "Lua library addons (both realms) and the server console commands for addons."
---

# LuaAddons

Source: `Code/Framework/Scripting/Api/LuaAddons.cs`

Lua library `addons` (both realms) and the server console commands for addons.

```lua
addons.GetAll()   -- → { { id, title, version, author, description, loaded, error }, ... } in load order
addons.Get(id)   -- → that table, or nil if the addon isn't running in this world
addons.IsLoaded(id) → true if it loaded without errors
-- hook "AddonsLoaded"   -- runs after all addons loaded, right before "Initialize"
```

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
