---
description: "Admin: permission-checked commands and the audit log. Groups and permissions come from base (permissions module:"
---

# darkrp: module `admin`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/admin/`

## `sv_admin.lua` (server)

Admin: permission-checked commands and the audit log. Groups and permissions come from base (permissions module:
storage "admins", /setgroup, `rp setgroup`); the listen-server host and the offline player are superadmin.

Functions defined:

- `DarkRP.GetGroupFor(ply)`
- `DarkRP.RunAdminAction(ply, name, target, args)`
