# `DIMENSION` Reference

`WHO 18` relies heavily on `DIMENSION` operations. They cover instantaneous power, accumulated energy, historical time series, Energy Management actuator state, totalizers, differential-current information, Stop&Go state, and automatic update configuration.

## Identifier table

| `DIMENSION` | Meaning |
| ---: | --- |
| `51` | Energy/unit totalizer |
| `52` | Energy/unit per month |
| `53` | Partial totalizer for current month |
| `54` | Partial totalizer for current day |
| `71` | Actuator information |
| `72` | Totalizers |
| `73` | Differential-current level |
| `113` | Active power |
| `250` | Complete Stop&Go status mask |
| `251` | Stop&Go open/closed |
| `252` | Stop&Go failure/no failure |
| `253` | Stop&Go blocked/not blocked |
| `254` | Stop&Go open for neutral-related short circuit |
| `255` | Stop&Go opened for ground fault |
| `256` | Stop&Go open for maximum-voltage condition |
| `257` | Stop&Go self-test disabled/enabled |
| `258` | Stop&Go automatic reset off/on |
| `259` | Stop&Go check off/on |
| `260` | Stop&Go waiting for closing |
| `261` | Stop&Go first 24 hours of opening |
| `262` | Stop&Go downstream power failure |
| `263` | Stop&Go upstream power failure |
| `511` | Daily hourly historical series |
| `512` | Monthly-average hourly historical series |
| `513` | Current-year daily monthly series |
| `514` | Previous-year daily monthly series |
| `1200` | Automatic update configuration / termination |

The value tuple and units are `DIMENSION`-specific. Numeric similarity does not imply a shared schema.

## Power and accumulated energy

### `DIMENSION 113` - active power

Request: `*#18*WHERE*113##`

Response/event: `*#18*WHERE*113*Val##`

`Val` is active power in watts. `DIMENSION 113` is also the event payload used when automatic active-power reporting is enabled through `DIMENSION 1200`.

### `DIMENSION 51` - energy/unit totalizer

Request: `*#18*WHERE*51##`

Response/event: `*#18*WHERE*51*Val##`

The published specification describes `Val` as the energy/unit totalizer value and labels its unit as Watt. This terminology is preserved rather than silently correcting the wire model from the word “totalizer.”

### `DIMENSION 52` - monthly energy/unit totalizer

Request: `*#18*WHERE*52#Y#M##`

Response/event: `*#18*WHERE*52#Y#M*Val##`

`Y` is the year in two-digit `yy` form and `M` is the month.

### `DIMENSION 53` - current-month partial totalizer

Request: `*#18*WHERE*53##`

Response/event: `*#18*WHERE*53*Val##`

### `DIMENSION 54` - current-day partial totalizer

Request: `*#18*WHERE*54##`

Response/event: `*#18*WHERE*54*Val##`

`DIMENSION 51..54` are scalar totalizer operations. They are distinct from the multi-frame historical series under `DIMENSION 511..514`.

## Energy Management actuator information

### `DIMENSION 71` - actuator status

Request: `*#18*WHERE*71##`

Response/event: `*#18*WHERE*71*disabled*forcing*threshold*protection*phase*advanced##`

The six fields are positional.

| Field | Value | Meaning |
| --- | ---: | --- |
| `disabled` | `0` | Enabled |
| `disabled` | `1` | Disabled |
| `forcing` | `0` | Not forced |
| `forcing` | `1` | Forced |
| `threshold` | `0` | Above threshold |
| `threshold` | `1` | Below threshold |
| `protection` | `0` | Not in protection |
| `protection` | `1` | Protection |
| `phase` | `0` | Disable of other phase |
| `phase` | `1` | Disable of local phase |
| `advanced` | `1` | Advanced |
| `advanced` | `2` | Basic |

The published event section contains inconsistent wording for `forcing`, while the request/response definition states `1 = Forced`, `0 = Not Forced`. The request/response definition is retained as the field semantics; the source discrepancy is not converted into a second state model.

### `DIMENSION 72` - totalizer state

Request: `*#18*WHERE*72#Tot_N##`

Response/event: `*#18*WHERE*72#Tot_N*Energy*D*M*Y*H*m##`

| Field | Meaning |
| --- | --- |
| `Tot_N` | Totalizer number, `1..2` |
| `Energy` | Energy accumulated since reset, in Wh |
| `D` | Day of last reset |
| `M` | Month of last reset |
| `Y` | Year of last reset |
| `H` | Hour of last reset |
| `m` | Minute of last reset |

This operation couples the accumulated value with the timestamp of its reset boundary.

### `DIMENSION 73` - differential-current level

Request: `*#18*WHERE*73##`

Response/event: `*#18*WHERE*73*level##`

The published range for `level` is `1..3`. The public specification does not assign a more detailed semantic label to each individual numeric level, so those meanings remain unspecified.

## Stop&Go status

Stop&Go exposes both a complete 13-bit state and individual one-bit `DIMENSION` values.

### `DIMENSION 250` - complete status mask

Request: `*#18*WHERE*250##`

Response/event: `*#18*WHERE*250*MASC##`

`MASC` is a 13-bit mask ordered `b13...b1`.

| Bit | Individual `DIMENSION` | State when `1` |
| ---: | ---: | --- |
| `b1` | `251` | Open |
| `b2` | `252` | Failure |
| `b3` | `253` | Blocked |
| `b4` | `254` | Open for neutral-related short-circuit condition |
| `b5` | `255` | Opened for ground fault |
| `b6` | `256` | Open for maximum-voltage condition |
| `b7` | `257` | Self-test disabled |
| `b8` | `258` | Automatic reset off |
| `b9` | `259` | Check off |
| `b10` | `260` | Waiting for closing |
| `b11` | `261` | First 24 hours of opening |
| `b12` | `262` | Downstream power failure |
| `b13` | `263` | Upstream power failure |

### Individual Stop&Go flags

Each `DIMENSION 251..263` can be requested independently using `*#18*WHERE*DIMENSION##` and returns one bit as `*#18*WHERE*DIMENSION*bN##`.

| `DIMENSION` | `1` | `0` |
| ---: | --- | --- |
| `251` | Open | Closed |
| `252` | Failure | No failure |
| `253` | Blocked | Not blocked / closed state |
| `254` | Open for specified short-circuit condition | Closed |
| `255` | Opened for ground fault | Closed |
| `256` | Open for maximum-voltage condition | Closed |
| `257` | Self-test disabled | Self-test enabled |
| `258` | Automatic reset off | Automatic reset on |
| `259` | Check off | Check on |
| `260` | Waiting for closing | Closed |
| `261` | First 24 hours of opening | Closed |
| `262` | Downstream power failure | No downstream failure |
| `263` | Upstream power failure | No upstream failure |

A Stop&Go event can expose the complete mask and/or individual status frames. State consumers should therefore be able to merge both representations.

## Historical series

Historical operations return sequences of frames. The `#` parameters attached to the `DIMENSION` identify the requested period; `Tag` identifies a point within the series.

### `DIMENSION 511` - daily hourly series

Request: `*#18*WHERE*511#M#D##`

Data frames: `*#18*WHERE*511#M#D*Tag*Val##`

| `Tag` | Meaning |
| ---: | --- |
| `1..24` | Hourly measure |
| `25` | Daily total |

The published source renders the unit as “Watt/h”; the operation represents the daily energy-history series. The same sequence can be initiated by `WHAT 57#M#D`.

### `DIMENSION 512` - monthly-average hourly series

Data frame: `*#18*WHERE*512#M*Tag*Val##`

Tags `1..24` identify hourly measures averaged over the selected month. Tag `25` carries the monthly-average total/unit value defined by the published protocol. The sequence is initiated by `WHAT 58#M`.

### `DIMENSION 513` - current-year monthly series

Data frame: `*#18*WHERE*513#M*Tag*Val##`

`Tag` identifies the day, `1..31`. The series represents daily values for the selected month in the current-year monthly graph model. It is initiated by `WHAT 59#M`.

### `DIMENSION 514` - previous-year monthly series

Data frame: `*#18*WHERE*514#M*Tag*Val##`

`Tag` identifies the measure/day, `1..31`. The series is used for the previous-year comparison graph and is initiated by `WHAT 510#M`.

## `DIMENSION 1200` - automatic active-power updates

`DIMENSION 1200` configures automatic reporting.

Start/update form: `*#18*WHERE*#1200#Type*Time##`

| Field | Meaning |
| --- | --- |
| `Type` | Energy type; published value `1` = active power |
| `Time` | Update/change reporting parameter in minutes, `1..255` |

After configuration, active-power events are reported as `*#18*WHERE*113*Val##`.

The published description states that `Time` indicates after how many minutes consumption/status is sent when it changes. It should therefore be treated as the protocol's update parameter rather than generalized into an unconditional sampling interval.

Stop form: `*#18*WHERE*#1200#Type*0##`.

## Request, response and event symmetry

A significant part of `WHO 18` uses the same `DIMENSION` payload for direct responses and asynchronous event traffic. This applies to active power, scalar totalizers, actuator status, totalizer state, differential-current level and Stop&Go status.

Parsers should decode these frames by `WHO`, `WHERE`, `DIMENSION` and payload shape rather than assuming that a given payload can only appear immediately after a request.

See [`WHAT` Reference](what.md) for command-driven historical transmission and actuator control, and [Addressing](addressing.md) for the device-family address grammar.