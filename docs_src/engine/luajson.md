---
description: "util.TableToJSON(t [, pretty]) and util.JSONToTable(json), both realms, Garry's Mod compatible:"
---

# LuaJson

Source: `Code/Framework/Scripting/Api/LuaJson.cs`

`util.TableToJSON(t [, pretty])` and `util.JSONToTable(json)`, both realms, Garry's Mod compatible:
sequential tables become arrays, other tables objects (keys as strings), Vectors "[x y z]" and Angles "{p y r}";
reading turns those strings back into Vector/Angle and integer-like object keys back into numbers.
Invalid JSON gives nil (like GMod). Limits: 1,000,000 characters, nesting depth 64; cycles are an error.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
