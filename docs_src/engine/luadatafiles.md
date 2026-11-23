---
description: "GMod's file functions for the 'DATA' path: a private folder per realm where Lua may read and write text."
---

# LuaDataFiles

Source: `Code/Framework/Scripting/Api/LuaDataFiles.cs`

GMod's file functions for the `"DATA"` path: a private folder per realm where Lua may read and write text.

```lua
file.Read(path, "DATA")
file.Write(path, text)
file.Append(path, text)
file.Delete(path)
file.CreateDir(dir)
file.IsDir(dir, "DATA")
file.Size(path, "DATA")
file.Exists(path, "DATA")
file.Find(pattern, "DATA") → files
folders
```

Without "DATA" (or with "LUA"), file.Find/Exists keep looking at the gamemode's own scripts.

Folders: the server realm uses data/roleplay/data/<gamemode>/; the client realm a folder per server
(data/roleplay/clientdata/<server>/), so one server can't read or fill another's files.
Rules: relative paths of a-z, 0-9, _ - . and /, no "..", writes only to .txt .json .dat .csv files (like GMod).
Limits: 4 MB per file; per folder 100 MB / 2,000 files on the server, 20 MB / 500 files on a client.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
