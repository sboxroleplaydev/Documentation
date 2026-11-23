---
description: "Garry's Mod CSoundPatch: sounds a script starts, changes and stops itself - loops like the physics gun hum."
---

# LuaSoundPatch

Source: `Code/Framework/Scripting/Api/LuaSoundPatch.cs`

Garry's Mod CSoundPatch: sounds a script starts, changes and stops itself - loops like the physics gun hum.
Client only and local (each client decides what it hears, e.g. for every beam it draws).

```lua
local snd = CreateSound(ent | ply, "sounds/x.sound")   follows the entity (a looping .wav loops until stopped)
snd:Play()
snd:PlayEx(volume, pitch)
snd:Stop()
snd:IsPlaying()
snd:ChangeVolume(volume [, seconds])
snd:ChangePitch(pitch [, seconds])   -- (0-4 / 0.1-4, faded over seconds)
snd:FadeOut(seconds)
```


At most `MaxPatches` exist; all stop when the client realm stops or the entity is removed.

??? info "How to read the signatures"
    `name(arg)` is the Lua call, `[ , x ]` marks an optional argument, `a | b` means either, `→` lists the return values. Lines starting with `--` label a group (for example `Player only`).
