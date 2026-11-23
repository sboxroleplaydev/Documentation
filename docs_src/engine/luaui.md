---
description: "Client-side UI for Lua, built on the engine's panel system and styled with CSS."
---

# LuaUi

Source: `Code/Framework/Scripting/Api/LuaUi.cs`

Client-side UI for Lua, built on the engine's panel system and styled with CSS.

```lua
local p = ui.Create("panel" | "label" | "button" | "textentry" [, parent] [, classes])
p:AddClass(c)
p:RemoveClass(c)
p:SetClass(c, on)
p:HasClass(c)
p:SetStyle("width: 200px; color: red;")
p:SetText(t)
p:GetText()
p:SetPlaceholder(t)
p:SetMaxLength(n)
p:Focus()
p:HasFocus()
p:OnClick(fn)
p:OnSubmit(fn(text))
p:OnChange(fn(text))
p:SetImage(src)
p:SetAvatar(ply|steamid64)   -- src: image path, https URL, package ident, "thumb:"   -- (ui.Create("image") or any panel's background)
p:SetVisible(b)
p:IsVisible()
p:Clear()
p:Remove()
p:IsValid()
p:ScrollToBottom()
p:ScrollToTop()
ui.AddStyle(css)
ui.SetCursor(visible)
ui.IsTyping()
ui.ScreenSize()
```


Panels live under one Lua root that covers the screen (pointer-events: none, so give interactive panels
"pointer-events: all"). Everything is removed when the client realm stops. Limits: 4000 panels, 128 KB of CSS.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
