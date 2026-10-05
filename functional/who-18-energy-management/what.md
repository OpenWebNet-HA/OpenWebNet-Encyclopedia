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

### Historical Stop&Go controls

BTicino touchscreen tests at `TS10_1_0_23` establish additional Stop&Go commands:

| `WHAT` | Implemented operation |
| ---: | --- |
| `21` / `22` | Open / close |
| `23` / `24` | Enable / disable differential self-test |
| `28` / `29` | Enable / disable tracking |

They use the ordinary `*18*WHAT*WHERE##` form. The library schedules a `DIMENSION 250` read after each control to reconcile state. Earlier source labels reversed `21` and `22`; a documented correction and the mature tests establish the order above. The scheduled read is a client strategy, not a required protocol sequence. See [Stop&Go evidence](../../project/review/myopencommunity-integration.md#stopgo).

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

### Historical graph request variants

The touchscreen library selects request syntax independently of the returned graph encoding. Its compatibility mode treats the first [PIC version value](../who-13-integration-gateway/dimensions.md#historical-touchscreen-platform-properties) `<= 22` as old PIC. Exact tests establish this matrix:

| Graph encoding / operation | Normal command `WHAT` | Old-PIC read `DIMENSION` | Report `DIMENSION` |
| --- | --- | --- | ---: |
| Older daily graph | `52#M#D` | `56#M#D` | `56` |
| Older monthly-average graph | `53#M` | `57#M` | `57` |
| Older monthly graph | `56#M` | `510#M` | `510` |
| Newer daily graph | `57#M#D` | `511#M#D` | `511` |
| Newer monthly-average graph | `58#M` | `512#M` | `512` |
| Newer monthly graph | `59#M` | `513#M` | `513` |

Thus a newer daily graph can be requested as `*18*57#M#D*WHERE##` or, in old-PIC compatibility mode, `*#18*WHERE*511#M#D##`. These are historical implementation variants, not a rule that every Device accepts both forms. The PIC cutoff is a library policy; graph capability is detected separately.

The library can also force the read forms regardless of the reported PIC version. That option changes request syntax without forcing older graph decoding. It was introduced to avoid command traffic interrupting graph replies; the source does not identify the affected Device/Firmware combinations. See [graph-request history](../../project/review/myopencommunity-coverage-audit.md#historical-corrections).

BtExperience at `TS10_1_0_23` selects this forced-read option when constructing configured measurement objects. These objects initially use the older graph encoding and can switch to newer decoding independently; they do not consult the PIC property to choose command versus read syntax. Earlier consumers used the library's automatic PIC selection. The application's `advanced` measurement property reflects detected graph support, whereas the similarly named load Configuration flag controls the application's consumption-meter presentation. Neither establishes a physical retention period. See [Energy/PIC selection evidence](../../project/review/myopencommunity-energy-history-review.md#request-selection-and-capability-state).

The client sends graph requests through one connection to retain ordering and places the monthly graph request last because source comments report transmit/receive problems in some PIC versions. The affected Firmware versions are unspecified. Its assumption of ordered, uninterrupted graph packets is not a protocol-wide delivery guarantee. See [Energy evidence](../../project/review/myopencommunity-integration.md#energy-generations-and-measurements).

## Actuator commands

### Enable

`*18*71*WHERE##` enables the addressed Energy Management actuator.

The historical touchscreen library's API names differ from these published operations: `forceOn()` sends `74`, `forceOff(150)` sends `73#15`, and `enable()` sends `73`. These are serializers at `TS10_1_0_23`, with a confirmation TODO on the duration-based method; they do not redefine the published enable/forcing meanings or establish gateway acceptance. See [implementation evidence](../../project/review/myopencommunity-kb-provenance-audit.md).

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
