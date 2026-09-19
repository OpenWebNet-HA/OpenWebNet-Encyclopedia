# `DIMENSION` Reference

`WHO 24` uses `DIMENSION` operations for Lighting Management configuration and runtime state. Reads use the ordinary `DIMENSION` form; writable properties use `#DIMENSION`.

| `DIMENSION` | Property | Published value domain |
| ---: | --- | --- |
| `1` | Switch-on level | `1..100` percent |
| `2` | Maximum illuminance | `1..2000` lux |
| `3` | Maintained illuminance | `0..2000` lux |
| `4` | Automatic switch ON | `0` disabled; `1` enabled |
| `5` | Switch-on delay | `0..300` seconds |
| `6` | Automatic switch OFF | `0` disabled; `1` enabled |
| `7` | Switch-off delay | `0..900` seconds |
| `8` | Delay timer | `0..3600` seconds |
| `9` | Stand-by timer | `0..900` seconds |
| `10` | Stand-by level | `0..100` percent |
| `11` | OFF level | `0..100` percent |
| `12` | Slave offset (GAP) | `0..100` percent |
| `17` | Operating state | `MOD*EXIT*H*M*S` |
| `18` | Centralised illuminance | `SENSOR*LUX*ERROR` |

The detailed specification provides writes and reads for these properties. Scalar writes use `*#24*WHERE*#D*VALUE##` and reports use `*#24*WHERE*D*VALUE##`, with `D` replaced by the selected identifier. `WHERE` contains both [recipient and sender](addressing.md).

## Read-form inconsistencies

The source prints `*#24*WHERE*D##` for scalar requests `1..10`, but `*#24*WHERE*12*##` with a trailing empty value for slave offset. The state request is `*#24*WHERE*17##`. Its OFF-value request section instead repeats the write form `*#24*WHERE*#11*Off_val##`, apparently a copy error. That row does not establish a safe read command: do not send the write form when intending only to query. Confirm the OFF-value read variant on the target.

The illuminance request has a separate discrepancy, documented below. Preserve these distinctions rather than deriving every read mechanically by deleting the write marker.

## Maintained level

The published write form is `*#24*WHERE*#3*Maint_lev##`. `Maint_lev` is illuminance in lux, not a percentage; it should not be normalized as a `WHO 1` dimmer command.

## Timers and delays

`DIMENSION 5`, `7`, `8`, and `9` represent distinct timing properties: switch-on delay, switch-off delay, general delay timer, and stand-by timer. Their similar data type does not make them interchangeable.

## Stand-by and OFF values

`DIMENSION 10` and `11` configure values associated with stand-by and OFF behavior. They are separate from the enable/disable decisions represented by the automatic switching dimensions.

## Slave offset

`DIMENSION 12` carries the slave-offset/GAP value. Whether slave offset is enabled is controlled separately through parameterized `WHAT 2#[0-1]`; implementations should store both properties.

## Runtime state

State request: `*#24*WHERE*17##`.

State write: `*#24*WHERE*#17*MOD*EXIT*H*M*S##`.

State response/event: `*#24*WHERE*17*MOD*EXIT*H*M*S##`.

| Field | Meaning |
| --- | --- |
| `MOD` | `0` Stop; `1` Automatic; `2` Manual |
| `EXIT` | Return-to-automatic condition: `1` TIME; `2` FOR; `3` PROFILE; `4` NORMAL; `5` NEVER |
| `H*M*S` | Time or duration for TIME/FOR, with ranges `0..23`, `0..59`, `0..59` |

The source's `TIME` placeholder expands to three `*`-separated values. Do not treat the whole state report as one enum or transmit a literal `TIME` string.

## Centralised illuminance

The detailed read table uses `*#24*WHERE*18*SENSOR##`; response/event `*#24*WHERE*18*SENSOR*LUX*ERROR##`; write `*#24*WHERE*#18*SENSOR*LUX*ERROR##`.

`ERROR` is `0` when required parameters are available, `1` when the sensor is not configured, and `2` when present but missing required parameters. `LUX` is illuminance; the detailed table does not give a numeric range for it or `SENSOR`.

Pages 4–5 instead show selector-qualified examples `18#65` with response values `297*0`. That differs structurally from the `18*Sensor_addr` form on pages 21–22 and 39–41. Retain both as source variants and select only a form corroborated for the gateway; do not silently move the sensor between selector and payload.

State and illuminance are distinct from the configuration threshold in `DIMENSION 2`.

Capability support is device-specific. The namespace-level table defines available operations but does not imply that every Lighting Management endpoint accepts every write.

## Evidence basis

Domains and frame variants come from the [Lighting Management Specification](../../sources/openwebnet-public/pdf/WHO_24.pdf), pages 6–41. The discrepancies above are retained because they affect safe encoding and request/response matching.
