# `WHO 2` - Automation

`WHO 2` defines the OpenWebNet Automation system. It covers movement commands, shutter state, relative and absolute positioning, priority handling, and Automation-specific addressing.

The published OpenWebNet Automation specification defines the functional command, addressing, and advanced shutter model. The MyHOME_Suite data structures complement that model with the address rules and frame forms used by the application. Device configuration is represented separately by the MyHOME_Suite catalogue model; diagnostic discovery and configuration reading belong to the diagnostic protocol rather than to `WHO 2` functional traffic.

The supplied [ZigBee Interface](../../protocol/zigbee-interface.md) also exposes `WHO 2`, but with a different transport, `WHERE` grammar, narrower position payloads, and a different `DIMENSION 11` write form. Its UP-value conflict remains unresolved. See the [ZigBee Automation Variant](zigbee-variant.md); this SCS-oriented reference does not settle the variant by namespace equality.

## Reference

| Subject | Page |
| --- | --- |
| Commands, movement and priority | [`WHAT` Reference](what.md) |
| `WHERE` forms and address scopes | [Addressing](addressing.md) |
| Shutter state and absolute positioning | [`DIMENSION` Reference](dimensions.md) |
| ZigBee-specific Automation semantics and source conflicts | [ZigBee Automation Variant](zigbee-variant.md) |

## Functional model

Ordinary movement commands use `*2*WHAT*WHERE##`. Advanced shutter state and absolute positioning use `DIMENSION` frames under the same `WHO` namespace.

`WHO 2` must be interpreted as a system-scoped protocol namespace: the meaning of `WHAT`, `WHERE`, `DIMENSION`, and their parameters is specific to Automation. In particular, numeric values used inside `DIMENSION 10` shutter state are not automatically additional command `WHAT` values.

Automation uses the SCS `A`/`PL` addressing family also used by Lighting, but the protocol semantics remain scoped to `WHO 2`. MyHOME_Suite represents the corresponding point-to-point, environment, and advanced address forms through its `OPEN.db` address-rule definitions.

For the common OpenWebNet frame language, see [Protocol](../../protocol/). For the Device → Module → Object → Configuration model used to describe physical Automation devices, see [Device Model](../../device-model/).
