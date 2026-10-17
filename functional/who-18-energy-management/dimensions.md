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

The published range for `level` is `1..3`. The public specification does not assign a more detailed semantic label to each individual numeric level.

The historical touchscreen library labels `1` OK, `2` warning and `3` critical; its product tests preserve that ordering. These are the client's load-level classifications. The recovered implementation does not establish numerical differential-current thresholds or hardware trip guarantees. See [load-level evidence](../../project/review/myopencommunity-coverage-audit.md#probe-state-and-load-levels).

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

## Historical touchscreen extensions

The following operations and decoding choices are implementation evidence from the BTicino library at `TS10_1_0_23`. They do not establish support by every `WHO 18` Device or by the ZigBee variant.

### Stop&Go self-test interval

`DIMENSION 212` is read with `*#18*WHERE*212##` and written with `*#18*WHERE*#212*DAYS##`. The library defines `DAYS = 1..180`. Its tests independently verify all thirteen bits of `DIMENSION 250`, confirming the published `b13` through `b1` wire order, with opened state at the rightmost bit. See [Stop&Go evidence](../../project/review/myopencommunity-integration.md#stopgo).

### Measurement families and automatic updates

Configuration modes in this application differ from the `Type` selector on the wire:

| Application mode | Measurement family | Current-value `DIMENSION` | Update `Type` |
| ---: | --- | ---: | ---: |
| `1` | Electricity | `113` | `1` |
| `2` | Water | `1134` | `4` |
| `3` | Gas | `1130` | `2` |
| `4` | Hot water | `1134` | `4` |
| `5` | Heating/conditioning | `1132` | `3` |

Current-value reads use `*#18*WHERE*DIMENSION##` and reports carry a scalar value. The application requests automatic updates with `*#18*WHERE*#1200#Type*255##` and stops them with `*#18*WHERE*#1200#Type*0##`. Hot water shares the water selector. These additional selectors extend the published active-power-only description for this implementation.

The client falls back to 10-second polling until automatic-update support is detected. An update-control report can switch the client to newer graph handling; a received stop while updates are still wanted causes it to request updates again. Neither the polling interval nor that capability heuristic defines a Device's physical sampling interval.

### Electricity thresholds

| Operation | Implemented form / payload |
| --- | --- |
| Read threshold state | `*#18*WHERE*516##` |
| Threshold-state report | `*#18*WHERE*516*EXCEEDED1*ENABLED1*EXCEEDED2*ENABLED2##` |
| Read threshold `N` | `*#18*WHERE*517#N##` |
| Threshold-value report | `*#18*WHERE*517#N*VALUE##` |
| Write threshold `N` | `*#18*WHERE*#517#N*VALUE##` |

`N` is `1` or `2`; the library's zero-based index is converted before transmission. A disabled threshold takes precedence over its exceeded flag in the application's displayed state. The source does not establish a general threshold-value range or physical unit for every target.

The touchscreen application disables a threshold by writing value `0`, then restores its last nonzero value when re-enabled. A zero report updates the current value without clearing that remembered value; enabled state comes from `516`. This cache behavior is an application choice, not a guarantee that every Device accepts zero as a disable command. See [threshold evidence](../../project/review/myopencommunity-coverage-audit.md#threshold-enable-state).

### Legacy graph values and unavailable data

Older graph reports under `56`, `57`, and `510` contain packet numbers and byte-valued samples, including values assembled across packet boundaries. In the older daily graph, a single sample `255` is replaced with zero. In paired decoding, the value is `high*256 + low`, with only the complete pair `255*255` replaced with zero; `(3,255)` is explicitly tested as valid. For electricity the library multiplies older graph values by 100; the other application modes use a factor of 1. This follows executable behavior rather than the source's broader scaling comment. Newer `511..514` reports use tagged scalar samples as described above.

The exact tests and decoder establish these older packet layouts. Payload positions below follow the packet number:

| Report selector | Packet layout used by the client |
| --- | --- |
| `56#M#D` | Packet `1`: ignore first payload value, take the second as hour `1`; packets `2..8`: three hourly bytes each; packet `9`: hours `23` and `24`, then the daily-total high byte; packet `10`: daily-total low byte |
| `57#M` | Skip packet `1`; concatenate the three bytes from each packet `2..17`, then decode pairs across packet boundaries for the 24 hourly values |
| `510#M` | Packet `1`: two bytes; subsequent packets: three bytes; concatenate and decode pairs, stopping at the calendar month's day count |

For example, `*#18*WHERE*510#M*1*3*255##` produces a first daily value of `102300` in electricity mode. The skipped header values remain uninterpreted. The older monthly-average decoder divides reconstructed hourly totals by the month's day count, or completed days in the current month, with a minimum divisor of 1. Newer hourly averages are consumed directly.

A trailing unpaired byte produces no value. The partial-month test establishes decoding of a truncated packet prefix, not recovery from missing interior packets or reordering. The newer client decoders also assign graph positions by arrival order rather than the received tag. BtExperience can fill absent positions with zero when expanding a current-period graph for display; a displayed zero therefore need not represent a received zero measurement. See [packet and cache evidence](../../project/review/myopencommunity-energy-history-review.md#packet-decoding-and-cache-boundaries).

The same library converts raw scalar measurement/totalizer value `4294967295` to zero, including actuator `DIMENSION 72`. Its scalar test preserves `4294967294` as an unsigned value; the normalization must not be extended to all values above the signed 32-bit maximum. Preserve the raw value when retaining evidence: this normalization cannot distinguish unavailable data from actual zero consumption and is not a universal protocol sentinel definition.

`DIMENSION 51` remains the all-time totalizer. The library separately assembles a rolling total for the current and previous eleven months. BtExperience instead constructs its calendar-year graph and total from January onward, waiting for all required monthly values; it also has a separate rolling twelve-month view. These are derived application values, not additional wire dimensions.

Month-only graph replies carry no year field. This historical library assigns a month to the latest occurrence not later than the current month, then subtracts another year for `514`. That date reconstruction is a client policy, separate from the published current-year/previous-year descriptions. It does not establish a Device's retained-history depth. Explicit `52#Y#M` replies use `2000 + Y`. See [date and total evidence](../../project/review/myopencommunity-energy-history-review.md#dates-units-and-derived-totals).

Source comments label electricity as watt, water as litres, gas as dm³, and hot-water/heating quantities as calories. These are historical application unit labels; they do not resolve the published energy/power terminology or establish physical measurement units across all Devices. On detecting newer graph support, the library resubmits its pending graph request using the newer form.

See [Energy evidence](../../project/review/myopencommunity-integration.md#energy-generations-and-measurements).

## F520 simulator scope

The VDK 2.0 F520 model implements scalar reads `51..54` and `113`, and the `57`, `58`, `59`, and `510` command/report mappings above. Its `511` daily read also returns tagged samples. `72` totalizer and `75` reset handlers are explicitly unimplemented in this model; that absence does not establish a limitation of physical F520 hardware.

The simulator's `113` read emits the active-power report through its monitor path without sending the same report to the originating request socket. This is a model limitation, not a channel rule for physical F520 devices. See [simulator dispatch evidence](../../project/review/myopencommunity-coverage-audit.md#simulator-dispatch).

The simulator reads measurements from configured files and uses a fixed year value `13`. Its periodic-power handler parses the leading write marker in `#1200#Type` as an empty numeric component; the internal switch value `0` is not evidence for a separate public dimension-zero update operation. Simulation timing and generated totals should not be used to infer hardware precision, energy integration, or current Firmware behavior. See [Simulator evidence](../../project/review/myopencommunity-integration.md#simulator-models).

Its `52#Y#M` handler selects file data by month without using `Y`. For `512`, the built model computes tag `25` by dividing the sum of its 24 hourly averages by 24. A resource copy uses a different calculation and is not selected by the plugin build. Its `514` values subtract previous-year file values from current-file values. These model choices cannot establish year retention or the physical Device's historical-value calculations. See [F520 history evidence](../../project/review/myopencommunity-energy-history-review.md#f520-model-lineage).
