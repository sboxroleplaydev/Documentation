---
description: "Gamemodes can import sbox.game packages (models, materials, sounds, …) themselves, in addition to 'packages' /"
---

# Content

Gamemodes can import sbox.game packages (models, materials, sounds, …) themselves, in addition to `"packages"` /
`"collections"` in gamemode.json.

| API | Realm | Notes |
|---|---|---|
| `#!lua content.AddPackage(id)` | both | `"org.name"` or `"https://sbox.game/org/name"`. **Server:** becomes required content: connected players get it right away, joining players before their scripts run. **Client:** mounts on that client only. Returns true; mounting is asynchronous. |
| `#!lua content.AddCollection(source)` | server | A collection: a URL (`"https://example.com/content.json"`) or a JSON file looked up in the gamemode's folder, then its base gamemodes, then `data/roleplay/`. Errors are reported like script errors. |
| `#!lua content.IsMounted(id)`, `#!lua content.GetTitle(id)`, `#!lua content.GetModel(id)` | both | `GetModel` returns the package's main asset (e.g. its `.vmdl`) once mounted |
| `#!lua content.GetPackages()` | both | Server: the world's required list. Client: everything mounted on this machine. |
| `#!lua content.IsBusy()` | both | True while anything is still downloading |

Adds made while the gamemode loads are mounted **before the server opens**. Use a package in `Initialize` only if it
is in gamemode.json; otherwise wait for `ContentMounted`:

```lua
content.AddCollection("content.json")          -- lua/gamemodes/<yours>/content.json
hook.Add("ContentMounted", "spawnBarrels", function(mounted, failed)
    if table.HasValue(mounted, "fish.barrel") then
        ents.Create("prop", { model = "fish.barrel", pos = Vector(0, 0, 10) })
    end
end)
```

A collection file is `["org.a", "org.b"]` or `{ "packages": ["org.a", "org.b"] }`. Limits: 128 required packages, 16
collections at startup, 64 KB per collection, 15 s HTTP timeout.

