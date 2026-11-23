---
description: "Base chat box (client). Enter opens it, Enter sends, Escape closes."
---

# base: module `chat`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/chat/`

## `cl_chat.lua` (client)

Base chat box (client). Enter opens it, Enter sends, Escape closes.

Functions defined:

- `GM:ChatCreate()`
- `GM:ChatIsOpen()`
- `GM:ChatOpen(teamOnly)`
- `GM:ChatClose()`
- `GM:ChatAddLine(msg)`

## `sv_chat.lua` (server)

Base chat (server).

Flow: client sends "base.chat.say" -> GM:PlayerSay(ply, text, teamOnly) decides the final text ("" = drop; chat
commands are handled there) -> GM:ChatRecipients(ply, text, teamOnly) picks who hears it -> "base.chat.msg".

Server API:
```lua
chat.AddCommand(name, function(ply, args, argString) end [, help])   -- -- triggered by /name or !name
chat.Send(ply | { plys }, text [, color])   -- -- system line to some players
chat.Broadcast(text [, color])   -- -- system line to everyone
chat.SendMessage(recipients, message)   -- -- full message table (see below)
```

Message table: { name = "Bob", nameColor = Color, prefix = "(OOC)", prefixColor = Color, text = "...", color = Color }

Functions defined:

- `chat.SendMessage(recipients, msg)`
- `chat.Send(target, text, color)`
- `chat.Broadcast(text, color)`
- `chat.AddCommand(name, fn, help)`
- `GM:PlayerSay(ply, text, teamOnly)`
- `GM:ChatRecipients(ply, text, teamOnly)`
- `GM:FormatChatMessage(ply, text, teamOnly)`
