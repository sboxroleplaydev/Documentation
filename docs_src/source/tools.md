---
description: "Generated from tools/sh.lua. Mode = rp gmodtoolmode <mode>, permission tool.<mode>. Settings = the tool's ClientConVar keys."
---

# Tool gun modes

Generated from `tools/sh_*.lua`. Mode = `rp gmod_toolmode <mode>`, permission `tool.<mode>`. Settings = the tool's `ClientConVar` keys.

| Category | Name | Mode | Description | Settings | Gamemode |
|---|---|---|---|---|---|
| Constraints | Ball Socket | `ballsocket` | Connects two objects with a ball socket |  | base |
| Constraints | Elastic | `elastic` | Connects two objects with an elastic | constant, damping, width, r, g, b | base |
| Constraints | Motor | `motor` | Spins an object around an axis relative to another object | key_fwd, key_back, speed, torque, toggle, start, limited, min, max | base |
| Constraints | No Collide | `nocollide` | Disables collision between two objects |  | base |
| Constraints | Rope | `rope` | Connects two objects with a rope | addlength, width | base |
| Constraints | Slider | `slider` | Connects two objects with a sliding joint | friction, width, collide, limited, min, max, r, g, b | base |
| Constraints | Upright | `keepupright` | Constrains an object to stay upright | strength | base |
| Constraints | Weld | `weld` | Welds two objects together |  | base |
| Constraints | hydraulic | `hydraulic` |  | key, key_pull, min, max, speed, toggle, width, r, g, b | base |
| Constraints | muscle | `muscle` |  | key, min, max, period, start, width, r, g, b | base |
| Constraints | winch | `winch` |  | key, key_pull, min, max, speed, width, r, g, b | base |
| Construction | Balloon | `balloon` | Places a poppable balloon | lift, length, model, r, g, b | base |
| Construction | Button | `button` | Places a button that drives linked inputs | key, toggle | base |
| Construction | Duplicator | `duplicator` | Used to copy, paste and save whole contraptions |  | base |
| Construction | Fading Door | `fading_door` | Makes a prop fade away and let things through when you press a key | key, toggle, reversed | base |
| Construction | Gravity | `gravity` | Sets the gravity scale of an object | enabled | base |
| Construction | Hoverball | `hoverball` | Attaches a hoverball that holds objects at a set height | key_up, key_down, key_toggle, speed, air | base |
| Construction | Mass | `mass` | Sets the mass of an object | mass | base |
| Construction | Remover | `remover` | Removes objects from the world |  | base |
| Construction | Resizer | `resizer` | Resizes an object | step | base |
| Construction | Spawner | `spawner` | Places a spawner that creates props from a key or on a timer | key, model, interval, max, frozen, delay | base |
| Construction | Stacker | `stacker` | Duplicates objects along a direction with live preview | count, dir, relative, ox, oy, oz, rp, ry, rr, freeze, weld, nocollide, preview | base |
| Construction | Thruster | `thruster` | Attaches a thruster to an object | key, key_rev, power, toggle, invert, effects, model | base |
| Construction | Unbreakable | `unbreakable` | Makes an object immune to damage |  | base |
| Construction | Wheel | `wheel` | Attaches a wheel to an object | key_fwd, key_back, torque, speed, model, reversed, flip, r, g, b | base |
| DarkRP | Door Placer | `doorplacer` | Turns a model into a map door (saved per map) | title, price, swing, model, rotation, snap, double, side, preview | darkrp |
| DarkRP | Glass Placer | `glassplacer` | Fills a window frame with glass (saved per map) | snap, cx, cy, cz | darkrp |
| Render | Camera | `camera` | Place a camera at your current view. View it using its bound input. | key, fov, toggle | base |
| Render | Colour | `colour` | Changes the colour of an object | r, g, b, a | base |
| Render | Emitter | `emitter` | Places a configurable particle emitter | key, toggle, on, rate, speed, life, r, g, b | base |
| Render | Light | `light` | Place rope-mounted or loose lights, or update an existing light | key, toggle, brightness, radius, spot, cone, length, on, r, g, b | base |
| Render | Material | `material` | Changes the material of an object | override | base |
| Render | Rope Look | `ropelook` | Changes how ropes and cables look | width, r, g, b | base |
| Render | Speaker | `speaker` | Places a speaker that plays sounds from a key | key, sound, volume, pitch, loop | base |
| Render | Text | `text` | Places text on surfaces | text, size, scale, spin, r, g, b | base |
| Render | Trail | `trail` | Add or remove trails from objects | width, life, r, g, b | base |
