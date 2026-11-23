---
description: "Money. Wallets live in server profiles; clients only ever see their own balance."
---

# darkrp: module `money`

Folder: `Assets/lua/gamemodes/darkrp/gamemode/modules/money/`

## `sv_money.lua` (server)

Money. Wallets live in server profiles; clients only ever see their own balance.
Every change is validated (whole numbers, never negative, capped) and written to the audit log.

Functions defined:

- `DarkRP.GetMoney(ply)`
- `DarkRP.CanAfford(ply, amount)`
- `DarkRP.AddMoney(ply, amount, reason)`
- `DarkRP.TransferMoney(from, to, amount, reason)`
- `PLAYER:GetMoney()`
- `PLAYER:CanAfford(n)`
- `PLAYER:AddMoney(n, reason)`
- `DarkRP.StartSalary()`

## `sv_moneydrop.lua` (server)

Cash in the world: /dropmoney <amount> drops a pile (rp_money) anyone can pick up with E;
/give <amount> hands money to the player you look at.
