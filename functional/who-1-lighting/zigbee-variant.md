# ZigBee Variant

The ZigBee OpenWebNet version 4.0 specification defines a `WHO 1` Lighting variant for the Legrand serial ZigBee interface. It reuses several familiar Lighting `WHAT` values but uses the [ZigBee product-and-Unit `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing), a smaller documented command set, ZigBee-specific event values, and a variant-specific `DIMENSION 1` payload.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. Its Confidential footer and unresolved public-release provenance remain recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The material below is **specification evidence for this interface revision**, not a tested-interoperability claim or a universal `WHO 1` definition.

## Command surface

The ZigBee source defines the following `WHAT` values:

| `WHAT` | ZigBee specification meaning | Relationship to the SCS-oriented reference |
| ---: | --- | --- |
| `0` | OFF | Same command meaning; different `WHERE` and transport |
| `0#SPEED` | OFF at requested speed | Same command family; different `WHERE` and transport |
| `1` | ON | Same command meaning; different `WHERE` and transport |
| `1#SPEED` | ON at requested speed; the source says this drives a dimmer to 100% | Same command family; different `WHERE` and transport |
| `2..10` | `20%..100%` | Same discrete levels; different `WHERE` and transport |
| `11..16` | Timed ON from 1 minute through 15 minutes | Same timed-value meanings in the current reference |
| `17` | Timed ON for 30 seconds | Variant source is explicit; it does not resolve the separate SCS source conflict |
| `18` | Timed ON for 0.5 seconds | Same timed-value meaning in the current reference |
| `32` | Toggle | ZigBee-specific extension relative to the current SCS-oriented table |
| `34` | Movement detected | ZigBee-specific event |
| `39` | End of movement detected | ZigBee-specific event |

For `0#SPEED` and `1#SPEED`, the ZigBee source defines `0` as the last speed used, `1..254` as explicit speed values, and `255` as the default speed. It does not state a physical time unit for the explicit values.

The SCS-oriented reference also documents blinking `WHAT 20..29`, relative dimming `WHAT 30..31`, and command translation `WHAT 1000`. Their absence from the ZigBee version 4.0 command table means only that this source does not establish them for this interface. It is not evidence that no ZigBee implementation can support them.

## Command acknowledgement and state reporting

Ordinary ZigBee Lighting commands use the interface-specific acknowledgement model described in [ZigBee acknowledgement behavior](../../protocol/zigbee-interface.md#acknowledgement-behavior). `ACK` means the command was sent according to the source; `NACK` means it was not, and BUSY uses the documented BUSY/NACK retry sequence.

When Supervisor mode is enabled through ZigBee `WHO 13`, the command definitions show server-originated state frames after OFF, ON, level, and timed operations. For dimmers, the detailed OFF and timed-OFF flows can show an additional OFF report when the dimmer reaches its 0% level, while ON at a requested speed reports the 100% state as `WHAT 10`. These are interface-specific event sequences and should not be transferred to SCS sessions by analogy.

Toggle is special in the source. It states that the product replies with its resulting state even when Supervisor mode is disabled and that Supervisor mode can therefore produce duplicate state replies. The switch case returns state `0` or `1`. The dimmer cases return `0` when OFF or `2..10` when ON according to the last dimming level.

Timed-ON examples return an ON or current-level state first and a later OFF state after the selected interval. The detailed `WHAT 11` example uses one minute; the table defines the other timing values.

## Movement-detector events

The source defines server-originated `WHAT 34` for movement detected and `WHAT 39` for end of movement detected. It says the detector must previously have completed a source-named "PnL" procedure with the OpenWebNet interface and points to the `WHO 25` use cases.

The movement-detector use case also shows `WHAT 32` Toggle at half of the detector's configured time while people continue to be detected. The source still labels `WHAT 32` as Toggle; the use case does not establish a separate occupancy-state meaning for that value.

The encyclopedia records only the OpenWebNet-visible dependency and events. It does not infer the underlying ZigBee commissioning or radio procedure from the term "PnL". See [ZigBee Binding](../who-25-transversal/zigbee-binding.md) for the OpenWebNet-visible `WHO 25` lifecycle.

## `DIMENSION 1` - level and speed

The ZigBee variant documents only `DIMENSION 1` in its Lighting `DIMENSION` table.

Read:

`*#1*WHERE#9*1##`

Response:

`*#1*WHERE#9*1*LEVEL*SPEED##`

Write:

`*#1*WHERE#9*#1*LEVEL*SPEED##`

The source defines `LEVEL` as `101..200`, expressed as the Lighting intensity percentage encoding. Unlike the SCS-oriented `DIMENSION 1` reference, this ZigBee section does not define `100` as OFF.

The source defines this `DIMENSION 1` `SPEED` field as `0..255`, with `0` described as immediate and `255` as the maximum delay. That wording materially differs from the SCS-oriented `DIMENSION 1` speed semantics, where `0` and `255` have different labels. The two variants must therefore not share one speed-value interpretation merely because the `DIMENSION` number is the same.

The ZigBee source does not specify a time unit for the `DIMENSION 1` speed field.

## Status request

The ZigBee Lighting state request is:

`*#1*WHERE#9##`

The response is an ordinary `WHO 1` state frame followed by `ACK`. The source defines switch state as `0` or `1`, and dimmer state as `0` or a discrete level `2..10`.

This request form belongs to the ZigBee address family. It is not an SCS `A`/`PL` request with a suffix added mechanically.

## Evidence limits

The ZigBee version 4.0 Lighting section documents `DIMENSION 1` only. It does not establish the SCS-oriented `DIMENSION 2`, `3`, `4`, `8`, or `9` operations for this interface.

The source establishes the command/event semantics above for the described interface revision, but not support by every ZigBee Lighting product or Firmware.

See [`WHAT` Reference](what.md) and [`DIMENSION` Reference](dimensions.md) for the SCS-oriented Lighting model, and [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for common ZigBee transport, addressing, and acknowledgement rules.
