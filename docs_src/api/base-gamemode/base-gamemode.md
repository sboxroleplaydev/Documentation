---
description: "Base gamemode: Chat (server): client message base.chat.say. GM:PlayerSay(ply, text, teamOnly) handles /cmd and !cmd and"
---

# Base gamemode

- **Chat (server):** client message `#!lua base.chat.say`. `#!lua GM:PlayerSay(ply, text, teamOnly)` handles `/cmd` and `!cmd` and
  returns the final text (`""` drops it). `#!lua GM:ChatRecipients` and `#!lua GM:FormatChatMessage` decide who sees what and how.
- **Chat library (server):** `#!lua chat.AddCommand(name, fn(ply, args, argString), help)`, `#!lua chat.Send(target, text, color)`,
  `#!lua chat.Broadcast(text, color)`, `#!lua chat.SendMessage(recipients, { prefix, prefixColor, name, nameColor, text, color })`.
  `/help` lists all commands.
- **Chat box (client):** opens with Enter and closes with Esc. Override `#!lua GM:ChatCreate`, `ChatOpen`, `ChatClose`,
  `#!lua ChatAddLine(msg)` or `#!lua ChatPrint(text)`.
- **Scoreboard (hold Tab):** `#!lua GM:ScoreboardColumns()`, `#!lua GM:ScoreboardRow(ply)`, `#!lua GM:ScoreboardTitle()`, or replace
  `#!lua GM:ScoreboardCreate`/`Rebuild`.
- **Pause menu (Escape):** replaces s&box's escape menu while a base-derived gamemode runs. Escape first closes the chat or help screen (derived gamemodes close their own menus first, as DarkRP does with its M menu), otherwise it toggles the pause menu: Resume, Help & keys, Settings, s&box menu, and Leave / Disconnect / "Stop server & leave" (hosts confirm with a second click).

    Change it with `#!lua GM:PauseMenuButtons()` (a list of `{ id, label, click, danger, confirm, keepOpen }`; call `#!lua self.BaseClass.PauseMenuButtons(self)` and insert yours), `#!lua GM:PauseMenuTitle()`, `#!lua GM:PauseMenuSubtitle()`, or replace `GM:PauseCreate/PauseOpen/PauseClose/PauseToggle/PauseIsOpen`.

    Gamemodes not derived from base keep s&box's own menu unless they return true for `"Escape"` themselves.

- **Shared:** `#!lua GM:GetPlayerDisplayName(ply)`, `#!lua GM:GetPlayerColor(ply)`, `#!lua GM:CleanChatText(text)`.

