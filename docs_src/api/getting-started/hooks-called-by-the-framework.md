---
description: "Gamemodes add their own hooks with hook.Run. Base adds PlayerSay; DarkRP adds PlayerCanChangeJob,"
---

# Hooks called by the framework

| Hook | Realm | When |
|---|---|---|
| `AddonsLoaded` | both | Gamemode and addons loaded, right before `Initialize` |
| `Initialize` | both | Gamemode and addons loaded |
| `Think` | both | Every frame (keep it cheap) |
| `#!lua PlayerInitialSpawn(ply)` | server | First spawn of a session |
| `#!lua PlayerSpawn(ply)` | server | Every spawn/respawn |
| `#!lua PlayerDisconnected(ply)` | server | Before the body is removed |
| `#!lua PlayerUse(ply, ent)` | server | The player pressed Use; the **server** traced 120 units from their eyes. `ent` is an Entity or a Player. |
| `#!lua PlayerButtonDown(action)` / `#!lua PlayerButtonUp(action)` | client | Input actions: `Use Reload Attack1 Attack2 Jump Duck Drop Flashlight Score Menu Chat View Voice Slot0-9 SlotPrev SlotNext ShowHelp(H) ShowTeam(N) ShowSpare1(B) ShowSpare2(M)`, plus `Escape` (return true to stop the engine handling it). Not sent while a Lua text box has focus. |
| `#!lua ContentMounted(mounted, failed)` | both | Packages queued with `content.AddPackage/AddCollection` finished mounting (two lists of idents) |
| `#!lua PostDrawOpaqueRenderables(depth, skybox)` / `#!lua PostDrawTranslucentRenderables(depth, skybox)` | client | Every frame: the place for `#!lua cam.Start3D2D` |
| `#!lua HUDPaint()` | client | Every frame: immediate 2D drawing on the screen |
| `#!lua ChatPrint(text)` | client | Server called `#!lua ply:ChatPrint`. Return true if you displayed it; otherwise it becomes a HUD notification. |
| `Shutdown` | both | World ending |

Gamemodes add their own hooks with `#!lua hook.Run`. Base adds `PlayerSay`; DarkRP adds `PlayerCanChangeJob`,
`PlayerChangedJob` and `PlayerDeath`.

