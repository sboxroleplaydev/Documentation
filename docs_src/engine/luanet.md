---
description: "Lua net library. Messages are named, carry one serialized value (see LuaSerializer), and are"
---

# LuaNet

Source: `Code/Framework/Scripting/Api/LuaNet.cs`

Lua `net` library. Messages are named, carry one serialized value (see `LuaSerializer`), and are
only delivered to a handler registered with `net.Receive` for that exact name.

```lua
Server:
net.Receive(name, fn(ply, data) [, { burst = n, rate = perSecond }]),
net.Send(name, ply|{plys}, data),
net.Broadcast(name, data)
Client:
net.Receive(name, fn(data)),
net.SendToServer(name, data)
```


Client→server messages pass the same guard as every framework request: authenticated sender, completed
handshake, per-message rate limit. Unknown names and malformed payloads count as violations. Names starting
with "rp." are reserved for the framework.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
