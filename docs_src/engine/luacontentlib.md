---
description: "Lua library content: gamemodes import cloud content (sbox.game packages) themselves."
---

# LuaContentLib

Source: `Code/Framework/Scripting/Api/LuaContentLib.cs`

Lua library `content`: gamemodes import cloud content (sbox.game packages) themselves.

```lua
content.AddPackage("org.name")   -- queue a package; also accepts "https://sbox.game/org/name"
content.AddCollection("content.json")   -- server: a collection file (gamemode folder, then its bases, then data/roleplay/)
content.AddCollection("https://…")   -- server: a collection on any web server
content.IsMounted(id)
content.GetTitle(id)
content.GetModel(id)
content.GetPackages()
content.IsBusy()
hook "ContentMounted"(mounted, failed)   -- fired in both realms when a batch finished mounting
```


Server adds become part of the world's required content: players joining later get them before their scripts run, players already connected are sent them right away. Adds while the gamemode loads are mounted before the server
opens. A client add mounts on that client only.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
