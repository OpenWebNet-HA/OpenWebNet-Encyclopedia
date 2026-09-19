# ZigBee Variant

The ZigBee OpenWebNet version 4.0 specification defines a `WHO 2` Automation variant for shutter products on the Legrand serial ZigBee interface. The variant reuses the base Stop/Up/Down command family but uses the [ZigBee product-and-Unit `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing) and defines narrower `DIMENSION 10` and `11` payloads than the SCS-oriented Automation reference.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. Its Confidential footer and unresolved public-release provenance remain recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The material below is **specification evidence for this interface revision**.

## Base commands and source conflict

The detailed Automation section defines:

| `WHAT` | Detailed ZigBee meaning |
| ---: | --- |
| `0` | Stop |
| `1` | Up |
| `2` | Down |

The use cases and detailed definitions in sections 9.1 through 9.3 consistently use `WHAT 1` for Up and `WHAT 2` for Down. However, the general frame examples on PDF page 11 label `*2*2*WHERE#9##` as Automation Up, both for unicast and broadcast.

This is a source-internal contradiction. The encyclopedia does not rewrite the page-11 examples or use them to redefine the detailed command table. A decoder or encoder that must interoperate with a specific interface should establish the applicable behavior independently before relying on the conflicting value.

The SCS-oriented Automation reference also defines advanced `WHAT 10..12` and command-translation `WHAT 1000`. Their absence from the ZigBee version 4.0 Automation section does not establish that no ZigBee implementation can support them.

## Acknowledgement and Supervisor behavior

Stop, Up, and Down use the interface-specific `ACK`, `NACK`, and BUSY/NACK behavior described in [ZigBee acknowledgement behavior](../../protocol/zigbee-interface.md#acknowledgement-behavior).

With Supervisor mode enabled through ZigBee `WHO 13`, the detailed command definitions show a server-originated command-state frame matching Stop, Up, or Down. The detailed Stop definition then shows a `DIMENSION 10` status frame; unlike the preceding `WHAT 0` report, that status frame is not explicitly labelled as conditional on Supervisor mode. The Up use case additionally shows a later Stop report when the shutter reaches its upper limit, followed by a `DIMENSION 10` status report with level `100`.

The source does not state whether the Stop-associated `DIMENSION 10` report is universal across supported shutters, so it is retained as documented sequence evidence rather than generalized into a mandatory rule. These ZigBee-interface behaviors must not be generalized to SCS Automation event ordering.

## `DIMENSION 10` - read position

Request:

`*#2*WHERE#9*10##`

Response:

`*#2*WHERE#9*10*STATUS*LEVEL*PRIORITY*INFO##`

The ZigBee variant defines:

| Field | Values |
| --- | --- |
| `STATUS` | `10` Stop; `11` Up; `12` Down |
| `LEVEL` | `0` fully closed; `1..99` current position; `100` fully open; `255` unknown |
| `PRIORITY` | source states this is always `000` |
| `INFO` | source states this is always `0` |

The source says calibrated shutters can expose their position and that an uncalibrated shutter returns `LEVEL=255` for unknown position.

The SCS-oriented `DIMENSION 10` reference defines additional status values and richer priority/information semantics. Those SCS values must not be imported into the ZigBee payload merely because the dimension number and field names overlap.

## `DIMENSION 11` - move to position

The ZigBee write form is:

`*#2*WHERE#9*#11*LEVEL##`

`LEVEL` is `0..100`. The source states that the operation can be sent when shutter calibration has been completed.

This grammar materially differs from the SCS-oriented `DIMENSION 11` form, which carries a separate priority parameter before the target level. The ZigBee version 4.0 section does not define that priority parameter for `DIMENSION 11`.

## State request

The ZigBee Automation state request is:

`*#2*WHERE#9##`

The server returns an ordinary `WHO 2` state frame followed by `ACK`. The detailed request section defines states `0` Stop, `1` Up, and `2` Down, subject to the separate page-11 Up-value contradiction described above.

## Evidence limits

The ZigBee version 4.0 Automation section documents `WHAT 0..2`, `DIMENSION 10`, `DIMENSION 11`, and the general state request. It does not establish the broader SCS advanced-command or priority model for this interface.

Calibration is identified by the source as relevant to position availability and position writes, but the document does not define the calibration procedure itself as an OpenWebNet `WHO 2` operation. That underlying mechanism is outside this page.

See [`WHAT` Reference](what.md) and [`DIMENSION` Reference](dimensions.md) for the SCS-oriented Automation model, and [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for common ZigBee transport, addressing, and acknowledgement rules.
