---
description: "Networking: Server: net.Receive(name, fn(ply, data) [, { burst, rate }]), net.Send(name, ply|{plys}, data),"
---

# Networking

- **Server:** `#!lua net.Receive(name, fn(ply, data) [, { burst, rate }])`, `#!lua net.Send(name, ply|{plys}, data)`,
  `#!lua net.Broadcast(name, data)`.
- **Client:** `#!lua net.Receive(name, fn(data))`, `#!lua net.SendToServer(name, data)`.

Client messages pass the framework guard: sender, handshake, per-name rate limit. Unknown names, `rp.*` names and
malformed payloads are violations, and repeat offenders are kicked.

Payloads may be nil, a boolean, a number, a string (≤ 2048 characters) or a table of those (an array, or string keys
only). Limits: ≤ 8192 characters in total, nesting ≤ 8. **Validate every field in your handler.**

