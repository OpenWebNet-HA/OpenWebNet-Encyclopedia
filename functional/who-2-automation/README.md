# Overview

`WHO 2` defines the OpenWebNet Automation system. It covers movement commands, shutter state, relative and absolute positioning, priority handling, and Automation-specific addressing.

The published OpenWebNet Automation specification defines the functional command, addressing, and advanced shutter model. The MyHOME_Suite data structures complement that model with the address rules and frame forms used by the application. Device configuration is represented separately by the MyHOME_Suite catalogue model; diagnostic discovery and configuration reading belong to the diagnostic protocol rather than to `WHO 2` functional traffic.

## Reference

| Subject | Page |
| --- | --- |
| Commands, movement and priority | [`what.md`](what.md) |
| `WHERE` forms and address scopes | [`addressing.md`](addressing.md) |
| Shutter state and absolute positioning | [`dimensions.md`](dimensions.md) |

## Functional model

Ordinary movement commands use `*2*WHAT*WHERE##`. Advanced shutter state and absolute positioning use `DIMENSION` frames under the same `WHO` namespace.

`WHO 2` must be interpreted as a system-scoped protocol namespace: the meaning of `WHAT`, `WHERE`, `DIMENSION`, and their parameters is specific to Automation. In particular, numeric values used inside `DIMENSION 10` shutter state are not automatically additional command `WHAT` values.

Automation uses the SCS `A`/`PL` addressing family also used by Lighting, but the protocol semantics remain scoped to `WHO 2`. MyHOME_Suite represents the corresponding point-to-point, environment, and advanced address forms through its `OPEN.db` address-rule definitions.

For the common OpenWebNet frame language, see [`../../protocol/`](../../protocol/). For the Device → Module → Object → Configuration model used to describe physical Automation devices, see [`../../device-model/`](../../device-model/).