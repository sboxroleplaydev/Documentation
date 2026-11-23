---
description: "Every registered permission. Each tool also registers tool.<mode> (see Tool gun modes)."
---

# Permissions

Every registered permission. Each tool also registers `tool.<mode>` (see Tool gun modes).

| Category | Permission | Default group | Description |
|---|---|---|---|
| Admin | `base.bot` | admin | Spawn and remove bots (rp_bot) |
| Admin | `base.setgroup` | superadmin | Change players' groups (/setgroup) |
| Building | `props.admin` | admin | Move, edit and remove everyone's props and map objects; /cleanupall |
| Building | `props.nolimit` | admin | Ignore the per-player prop limit |
| Building | `props.spawn.cloud` | admin | Spawn models from sbox.game that the server doesn't have yet (spawn menu search) |
| Building | `props.spawn` | user | Spawn props (spawn menu, gm_spawn) |
| Building | `server.settings` | admin | Change server limits (spawn menu, Utilities > Server settings) |
| Building | `spawnmenu.npc` | admin | Spawn NPCs from the spawn menu |
| Building | `spawnmenu.open` | user | Open the spawn menu (Q) |
| Building | `spawnmenu.vehicle` | admin | Spawn vehicles from the spawn menu |
| DarkRP | `darkrp.entities.physgun` | admin | Move your own shop entities (printers, ...) with the physics gun |
| DarkRP | `darkrp.entities.tool` | admin | Use the tool gun on your own shop entities (printers, ...) |
| Player | `base.kill` | user | Kill yourself (/kill) |
| Sandbox | `sandbox.spawn.props` | user | Spawn props |
| Weapons | `weapons.drop` | user | Drop your weapon (/dropweapon) |
| Weapons | `weapons.give.self` | admin | Give yourself any weapon (/giveweapon) |
