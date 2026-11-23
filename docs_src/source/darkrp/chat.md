---
description: "DarkRP chat channels on top of base chat."
---

# darkrp: module `chat`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/chat/`

## `sv_chat.lua` (server)

DarkRP chat channels on top of base chat.
```lua
normal text   -- local (LocalChatRange)   -- /y   -- yell (YellRange)   -- /w   -- whisper (WhisperRange)
// or /ooc   -- out of character, global   -- /advert   -- global advert (costs AdvertCost)
/me   -- local action
```

Functions defined:

- `GM:ChatRecipients(ply, text, teamOnly)`
- `GM:PlayerSay(ply, text, teamOnly)`
