---
description: "Permissions (shared). One system for every gamemode and addon built on base:"
---

# base: module `permissions`

Folder: `Assets/lua/gamemodes/base/gamemode/modules/permissions/`

## `sh_permissions.lua` (shared)

Permissions (shared). One system for every gamemode and addon built on base:

```lua
permissions.Register("sandbox.spawn.props", { default = "user", category = "Sandbox", description = "Spawn props" })
ply:HasPermission("sandbox.spawn.props")   -- -- both realms (clients use it to hide what they can't use)
```


Groups are ranked, lowest first (permissions.SetGroups). A group has a permission when
```lua
-- * the permission's default group is the same or lower in rank, or
-- * the group or a lower group was granted it   -- permissions.Grant, "*" = everything
unless the group or a lower one revoked it (permissions.Revoke). Revokes win over defaults and grants
```

Server owners set this in gamemode/config/sh_permissions.lua (base) or their gamemode's config.
Who is in which group is stored on the server (storage "admins") and set with /setgroup or "rp setgroup".

Functions defined:

- `permissions.SetGroups(list)`
- `permissions.IsGroup(group)`
- `permissions.GetRank(group)`
- `permissions.GetGroups()`
- `permissions.Register(id, info)`
- `permissions.Grant(group, perms)`
- `permissions.Revoke(group, perms)`
- `permissions.GroupHas(group, id)`
- `permissions.CanTarget(actor, target)`
- `permissions.GetAll()`
- `PLAYER:HasPermission(id)`
- `PLAYER:IsAdmin()`

## `sv_permissions.lua` (server)

Permissions (server): who is in which group. Stored in storage "admins" ({ [steamid] = group }); the listen-server
host and the offline player are always superadmin. The group is the NW string "usergroup" (ply:GetUserGroup()).

Functions defined:

- `permissions.GetGroupFor(ply)`
- `permissions.SetGroupBySteamID(steamid, group)`
- `permissions.FindPlayer(text)`
