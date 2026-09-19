# `WHAT` Reference

`WHO 18` uses ordinary and parameterized `WHAT` values for Stop&Go control, historical-series transmission, Energy Management actuator control, and totalizer reset.

## Commands

| `WHAT` | Meaning | Parameters / notes |
| ---: | --- | --- |
| `26` | Activate automatic reset | Stop&Go |
| `27` | Deactivate automatic reset | Stop&Go |
| `57` | Start daily hourly totalizer series | `57#M#D` |
| `58` | Start monthly-average hourly series | `58#M` |
| `59` | Start current-year monthly series | `59#M` |
| `510` | Start previous-year monthly series | `510#M` |
| `71` | Enable actuator | Energy Management actuator |
| `73` | Force actuator | Optional `#Time` parameter |
| `74` | End forced actuator | Energy Management actuator |
| `75` | Reset totalizer | `75#Tot_N` |

## Stop&Go automatic reset

`WHAT 26` enables automatic reset and `WHAT 27` disables it. They apply to Stop&Go targets selected through the `1N` address family.

The command forms are `*18*26*WHERE##` and `*18*27*WHERE##`. Successful command processing is acknowledged with `ACK`.

Stop&Go status is read separately through `DIMENSION 250..263`; see [`DIMENSION` Reference](dimensions.md).

## Historical-series commands

The four commands `WHAT 57`, `58`, `59`, and `510` start transmission of data intended for graphical histories. They are an enumerated set, not the inclusive interval `57..510`. The command parameters select the requested calendar period; the returned data is carried by `DIMENSION 511..514` event frames.

| Command | Parameters | Resulting `DIMENSION` |
| --- | --- | ---: |
| `57#M#D` | Month, day | `511` |
| `58#M` | Month | `512` |
| `59#M` | Month | `513` |
| `510#M` | Month | `514` |

This is a multi-frame operation. The `WHAT` command starts transmission; it does not itself carry the historical values.

### Daily hourly series

`*18*57#M#D*WHERE##` starts the daily series. `DIMENSION 511` then reports tags `1..24` for the hourly measures and tag `25` for the daily total.

### Monthly-average hourly series

`*18*58#M*WHERE##` starts the monthly-average series. `DIMENSION 512` uses tags `1..24` for hourly monthly averages and tag `25` for the monthly average total/unit value defined by the published protocol.

### Current-year monthly graph

`*18*59#M*WHERE##` starts transmission through `DIMENSION 513`. The tag identifies the day, `1..31`.

### Previous-year comparison

`*18*510#M*WHERE##` starts transmission through `DIMENSION 514`. The tag identifies the measure/day, `1..31`.

## Actuator commands

### Enable

`*18*71*WHERE##` enables the addressed Energy Management actuator.

### Force for a specified time

`*18*73#Time*WHERE##` forces the actuator for the requested duration. The published `Time` field is expressed in tens of minutes and accepts values `1..254`.

The published prose also describes the resulting interval as beginning at 10 minutes. Its stated upper-duration prose is inconsistent with a literal `1..254` ten-minute encoding; implementations should preserve the encoded range and avoid deriving a corrected maximum duration without additional evidence.

### Force for default time

`*18*73*WHERE##` omits the `Time` parameter and requests the device's default forcing duration.

### End forcing

`*18*74*WHERE##` ends the forced state.

The current actuator state can be read through `DIMENSION 71`.

## Reset totalizer

`*18*75#Tot_N*WHERE##` resets the selected totalizer. `Tot_N` is `1` or `2`.

The state of a totalizer, including accumulated energy and last-reset timestamp, is available through `DIMENSION 72#Tot_N`.

See [Addressing](addressing.md) for valid target families and [`DIMENSION` Reference](dimensions.md) for returned values.
