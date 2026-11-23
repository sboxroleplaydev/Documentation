---
description: "These live on players, entities and globals (SetGlobalVar/GetGlobalVar). Only the server writes; everyone can read"
---

# Networked variables

These live on players, entities and globals (`SetGlobalVar`/`GetGlobalVar`). Only the server writes; everyone can read
them. Values are strings (≤ 1024 characters), numbers or booleans; up to 128 keys per object. **They are public**: send
private data with `#!lua net.Send` instead.

