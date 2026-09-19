# `WHO 1` - Lighting

`WHO 1` defines the OpenWebNet Lighting system. It covers switching, discrete and fine-grained dimming, timed and blinking operation, status reporting, transition speed, temporization, and lamp operating-time information.

The published Lighting specification defines the functional command and `DIMENSION` model. The MyHOME_Suite data structures complement it with implemented address rules and functional command templates. Lighting Objects represented by the MyHOME_Suite catalogue may be command Objects, actuator Objects, dimmer Objects, or functions embedded in combined Devices; the functional `WHO 1` namespace describes their Lighting traffic rather than their physical Device class.

The supplied [ZigBee Interface](../../protocol/zigbee-interface.md) also exposes `WHO 1`, but with a different transport, `WHERE` grammar, documented command set, event surface, and `DIMENSION 1` semantics. See the [ZigBee Lighting Variant](zigbee-variant.md). SCS forms do not establish ZigBee-backed applicability merely because the namespace number is shared.

## Reference

| Subject | Page |
| --- | --- |
| Commands, states and timed operations | [`WHAT` Reference](what.md) |
| `WHERE` forms and address scopes | [Addressing](addressing.md) |
| Level, speed, temporization and operating-time `DIMENSION` operations | [`DIMENSION` Reference](dimensions.md) |
| ZigBee-specific Lighting semantics and evidence limits | [ZigBee Lighting Variant](zigbee-variant.md) |

## Functional model

Ordinary command/status frames use `*1*WHAT*WHERE##`; status requests use `*#1*WHERE##`. `DIMENSION` operations use the common frame classes defined in [`DIMENSION`](../../protocol/dimensions.md).

`WHAT 0..31` provide the ordinary Lighting vocabulary, including ON/OFF, discrete dimmer levels, timed ON, blinking and relative dimming. Fine level control and other structured values are carried by Lighting-specific `DIMENSION` operations.

Lighting uses the SCS `A`/`PL` address family, with point-to-point, environment, group, general and advanced forms. Address syntax and event expansion are described in [Addressing](addressing.md).

Lighting Management is a distinct protocol namespace under [`WHO 24`](../who-24-lighting-management/). Diagnostic discovery and configuration of Lighting-capable Devices belong to the diagnostic protocol rather than to functional `WHO 1` traffic.

For the Device → Module → Object → Configuration model, see [Device Model](../../device-model/).
