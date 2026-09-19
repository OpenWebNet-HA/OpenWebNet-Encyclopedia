# ZigBee Variant

The ZigBee OpenWebNet version 4.0 specification defines an interface-specific `WHO 18` Energy Management surface for ZigBee products. Its command and `DIMENSION` vocabulary differs materially from the SCS-oriented `WHO 18` reference, despite sharing the same namespace number.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. Its Confidential footer and unresolved public-release provenance remain recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The material below is **specification evidence for this interface revision**.

The source section heading says "Automation WHO = 18", while its prose and operation labels describe Energy Management parameters. The encyclopedia preserves that editorial inconsistency in the reconciliation record rather than treating "Automation" as a second functional meaning.

## Reset command - unresolved source conflict

The `WHO 18` summary table lists:

| `WHAT` | Summary-table action |
| ---: | --- |
| `0` | Reset |

The immediately following detailed Reset definition instead sends:

`*18*75*WHERE#9##`

and describes it as resetting the energy counter of ZigBee Devices.

The source therefore assigns two different `WHAT` values to Reset. Neither is promoted as an unqualified ZigBee reset value. The SCS-oriented use of `WHAT 75` is not independent evidence that the ZigBee detailed frame is correct because the two protocol variants cannot be equated by numeric identity.

The detailed Reset form supports both ZigBee unicast and broadcast `WHERE` forms and uses the interface-specific acknowledgement model.

## `DIMENSION` table

The ZigBee source defines:

| `DIMENSION` | Source action | Relationship to current SCS-oriented `WHO 18` documentation |
| ---: | --- | --- |
| `11` | Voltage | ZigBee-specific identifier in the current encyclopedia |
| `17` | Current | ZigBee-specific identifier in the current encyclopedia |
| `51` | Energy | Same numeric identifier as an SCS totalizer operation, but materially different source semantics |
| `112` | Frequency | ZigBee-specific identifier in the current encyclopedia |
| `113` | Active Power | Same source label as an SCS operation; variant applicability and payload evidence remain separate |
| `114` | Active Power Total | ZigBee-specific identifier in the current encyclopedia |
| `115` | Threshold Max Active Power | ZigBee-specific identifier in the current encyclopedia |
| `117` | Reactive Power | ZigBee-specific identifier in the current encyclopedia |
| `1200` | Report Power | Same numeric identifier as an SCS reporting operation, but different documented syntax and time units |

For `DIMENSION 11`, `17`, `51`, `112`, `113`, `114`, `115`, and `117`, the request form is:

`*#18*WHERE#9*DIMENSION##`

and the response form is:

`*#18*WHERE#9*DIMENSION*VALUE##`

The detailed definitions describe `VALUE` as the named quantity "in decimal". They do not define a scale, signedness rule, or physical unit for these values. The encyclopedia therefore preserves the quantity names without importing units or scaling from the SCS-oriented `WHO 18` reference.

The detailed request tables show unicast product addressing for these measurements. The source does not establish a broadcast measurement request merely because Reset permits broadcast addressing.

## Frequency/Energy source conflict

The use case titled "Get Frequency" on PDF page 53 sends `DIMENSION 51` and receives `DIMENSION 51`.

The `DIMENSION` table and detailed definitions on pages 54 and 55 instead define:

- `DIMENSION 51` as Energy;
- `DIMENSION 112` as Frequency.

This is a material source-internal contradiction. The encyclopedia preserves both locations. The mutually consistent table and detailed definitions are documented as their stated meanings, but the conflicting use case prevents treating the source as contradiction-free evidence for the Frequency/Energy mapping.

## `DIMENSION 1200` - Report Power

The ZigBee source defines the command form:

`*#18*WHERE#9*1200#TYPE*TIME##`

with:

| Field | ZigBee source definition |
| --- | --- |
| `TYPE` | `1` = active power |
| `TIME` | `0..255` seconds |

The section defines acknowledgement handling for this command but does not show the later power-report frame or explicitly state that `DIMENSION 113` is the resulting asynchronous payload. That relationship must not be inferred solely from the names "Report Power" and "Active Power".

This grammar materially differs from the SCS-oriented `DIMENSION 1200` operation, which the current encyclopedia documents with a write marker and a time value in minutes. Variant selection is therefore required before encoding or decoding `DIMENSION 1200`.

## Addressing and acknowledgements

The ZigBee Energy Management section uses the [ZigBee product-and-Unit `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing), not the SCS `1N`, `5N`, or `7N#0` Energy Management address families.

Measurement requests and Report Power use the unicast form shown by the source. Reset additionally documents broadcast addressing. `ACK`, `NACK`, and BUSY/NACK follow the common ZigBee-interface behavior.

## Evidence limits

The ZigBee version 4.0 section does not establish the SCS Stop&Go command family, SCS historical-series operations, SCS actuator-control model, or SCS `DIMENSION 250..263` and `511..514` surfaces for this interface. Their absence is not proof that no ZigBee implementation can expose additional operations.

The source does not provide sufficient scaling or unit information to turn the decimal measurement payloads into implementation-ready physical quantities beyond their named properties. That remains an explicit evidence gap.

See [`WHAT` Reference](what.md) and [`DIMENSION` Reference](dimensions.md) for the SCS-oriented Energy Management model, and [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for common ZigBee transport, addressing, and acknowledgement rules.
