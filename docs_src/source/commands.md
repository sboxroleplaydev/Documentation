---
description: "Console commands run as rp <command>; chat commands start with /."
---

# Commands

Console commands run as `rp <command>`; chat commands start with `/`.

| Kind | Command | Description | Defined in |
|---|---|---|---|
| chat | `/adddoor` | admin: place a door (aim at the doorway floor) | gamemodes/darkrp/gamemode/modules/doors/sv_doors.lua |
| chat | `/addjailpos` | admin: add a jail position where you stand | gamemodes/darkrp/gamemode/modules/police/sv_police.lua |
| chat | `/addlaw` | mayor: add a law | gamemodes/darkrp/gamemode/modules/laws/sv_laws.lua |
| chat | `/advert` | paid advert to everyone | gamemodes/darkrp/gamemode/modules/chat/sv_chat.lua |
| chat | `/buy` | Buy a weapon or ammo: /buy <class\|ammo> | gamemodes/darkrp/gamemode/modules/weapons/sv_weapons.lua |
| chat | `/buydoor` | buy the door you look at | gamemodes/darkrp/gamemode/modules/doors/sv_doors.lua |
| chat | `/cleanup` | Remove all your props | gamemodes/base/gamemode/modules/props/sv_props.lua |
| chat | `/cleanupall` | Remove everyone's props (admins) | gamemodes/base/gamemode/modules/props/sv_props.lua |
| chat | `/dropmoney` | drop money on the ground | gamemodes/darkrp/gamemode/modules/money/sv_moneydrop.lua |
| chat | `/dropweapon` |  | gamemodes/base/gamemode/modules/weapons/sv_weapons.lua |
| chat | `/give` | give money to the player you look at | gamemodes/darkrp/gamemode/modules/money/sv_money.lua |
| chat | `/give` | give money to the player you look at | gamemodes/darkrp/gamemode/modules/money/sv_moneydrop.lua |
| chat | `/giveweapon` | Give yourself a weapon: /giveweapon <class> | gamemodes/base/gamemode/modules/weapons/sv_weapons.lua |
| chat | `/hello` | Say hello | gamemodes/_template/gamemode/modules/example/sv_example.lua |
| chat | `/help` | list chat commands | gamemodes/base/gamemode/modules/chat/sv_chat.lua |
| chat | `/job` | change job, e.g. /job police | gamemodes/darkrp/gamemode/modules/jobs/sv_jobs.lua |
| chat | `/kill` | Kill yourself | gamemodes/base/gamemode/modules/health/sv_health.lua |
| chat | `/lock` |  | gamemodes/darkrp/gamemode/modules/doors/sv_doors.lua |
| chat | `/me` | describe an action | gamemodes/darkrp/gamemode/modules/chat/sv_chat.lua |
| chat | `/myaddon` |  | addons/_template/sv_init.lua |
| chat | `/noclip` | owner: toggle noclip | gamemodes/darkrp/gamemode/modules/admin/sv_admin.lua |
| chat | `/ooc` | yell | gamemodes/darkrp/gamemode/modules/chat/sv_chat.lua |
| chat | `/removedoor` | admin: remove a placed door | gamemodes/darkrp/gamemode/modules/doors/sv_doors.lua |
| chat | `/removejailpos` | admin: remove all jail positions on this map | gamemodes/darkrp/gamemode/modules/police/sv_police.lua |
| chat | `/removelaw` | mayor: remove a law by number | gamemodes/darkrp/gamemode/modules/laws/sv_laws.lua |
| chat | `/repairglass` | admin: repair all broken glass | gamemodes/darkrp/gamemode/modules/doors/sv_glass.lua |
| chat | `/resetlaws` | mayor: back to the default laws | gamemodes/darkrp/gamemode/modules/laws/sv_laws.lua |
| chat | `/roll` | Roll a dice: /roll [max] (default  | addons/roll/sv_roll.lua |
| chat | `/rpname` | set your roleplay name | gamemodes/darkrp/gamemode/modules/core/sv_data.lua |
| chat | `/selldoor` | sell the door you look at | gamemodes/darkrp/gamemode/modules/doors/sv_doors.lua |
| chat | `/setgroup` | Set a player's group: /setgroup <player> <group> | gamemodes/base/gamemode/modules/permissions/sv_permissions.lua |
| chat | `/undo` | Undo the last thing you made (Z) | gamemodes/base/gamemode/modules/undo/sv_undo.lua |
| chat | `/unlock` |  | gamemodes/darkrp/gamemode/modules/doors/sv_doors.lua |
| chat | `/unwanted` | police: clear a wanted status | gamemodes/darkrp/gamemode/modules/police/sv_police.lua |
| chat | `/w` | whisper | gamemodes/darkrp/gamemode/modules/chat/sv_chat.lua |
| chat | `/wanted` | police: mark a player as wanted | gamemodes/darkrp/gamemode/modules/police/sv_police.lua |
| chat | `/y` | yell | gamemodes/darkrp/gamemode/modules/chat/sv_chat.lua |
| console | `rp dropweapon` | Tune the held weapon's position: rp weapon_offset x y z [pitch yaw roll] | gamemodes/base/gamemode/modules/weapons/sv_weapons.lua |
| console | `rp gm_spawn` | Spawn a prop where you look: rp gm_spawn <model path or package> | gamemodes/base/gamemode/modules/props/sv_props.lua |
| console | `rp gmod_toolmode` | Select a tool gun mode: rp gmod_toolmode <mode> | gamemodes/base/gamemode/modules/tools/sv_tools.lua |
| console | `rp gmod_undo` | Undo the last thing you made (Z) | gamemodes/base/gamemode/modules/undo/sv_undo.lua |
| console | `rp permissions` | List permissions and which groups have them | gamemodes/base/gamemode/modules/permissions/sv_permissions.lua |
| console | `rp rp_bot_kick` | Remove bots: rp_bot_kick [name\|all] | gamemodes/base/gamemode/modules/bots/sv_bots.lua |
| console | `rp rp_bot_mode` | What bots do: rp_bot_mode wander\|stand | gamemodes/base/gamemode/modules/bots/sv_bots.lua |
| console | `rp rp_bot` | Spawn bot players: rp_bot [count] [name] | gamemodes/base/gamemode/modules/bots/sv_bots.lua |
| console | `rp setgroup` | Set a player's group | gamemodes/base/gamemode/modules/permissions/sv_permissions.lua |
| console | `rp undo` | Undo the last thing you made (Z) | gamemodes/base/gamemode/modules/undo/sv_undo.lua |
| console | `rp weapon_offset` | Tune the held weapon's position: rp weapon_offset x y z [pitch yaw roll] | gamemodes/base/gamemode/modules/weapons/sv_weapons.lua |
