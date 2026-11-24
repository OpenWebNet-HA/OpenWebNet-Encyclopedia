# `DIMENSION` Reference

`WHO 4` uses `DIMENSION` frames for measured temperature, complete probe state, local offset, setpoint, fan-coil, valve and actuator state, split-unit control, and holiday deadline data.

## Functional `DIMENSION` table

| `DIMENSION` | Meaning | Access |
| ---: | --- | --- |
| `0` | Measured temperature | Read |
| `11` | Fan-coil speed | Read |
| `12` | Complete probe status | Read |
| `13` | Local set offset | Read |
| `14` | Setpoint temperature | Read / write |
| `19` | Valve status | Read |
| `20` | Actuator status | Read |
| `22` | Split control | Read / write |
| `30` | Holiday-scenario end date | Read / write |
| `31` | Holiday-scenario end time | Read / write |

The MyHOME_Suite ScenarioDevices capability data additionally defines Temperature Control action templates using `DIMENSION 7`, and write forms using `DIMENSION 5` and `11`. These implementation operations complement the published functional table and should be interpreted from their exact MyHOME_Suite templates rather than silently mapped onto unrelated public operations.

## MyHOME_Suite `DIMENSION 7` action model

ScenarioDevices defines `DIMENSION 7` actions with a two-field mode structure after the `DIMENSION` identifier. The first value selects the thermal context and the second selects the requested operating state.

### Thermal context

| First value | Context |
| ---: | --- |
| `0` | Generic |
| `1` | Heating |
| `2` | Cooling |
| `3` | Automatic |

### Operating state

| Second value | State | Additional value |
| ---: | --- | --- |
| `1` | Setpoint | four-digit `c1c2c3c4` temperature |
| `2` | Protection | none |
| `3` | Comfort | none |
| `4` | Eco | none |
| `5` | OFF | none; ScenarioDevices uses generic context `0` |

The exact MyHOME_Suite templates are:

| Operation | Generic | Heating | Cooling | Automatic |
| --- | --- | --- | --- | --- |
| Comfort | `*#4*ZAZB*#7*0*3*##` | `*#4*ZAZB*#7*1*3*##` | `*#4*ZAZB*#7*2*3*##` | `*#4*ZAZB*#7*3*3*##` |
| Eco | `*#4*ZAZB*#7*0*4*##` | `*#4*ZAZB*#7*1*4*##` | `*#4*ZAZB*#7*2*4*##` | `*#4*ZAZB*#7*3*4*##` |
| Protection | `*#4*ZAZB*#7*0*2*##` | `*#4*ZAZB*#7*1*2*##` | `*#4*ZAZB*#7*2*2*##` | `*#4*ZAZB*#7*3*2*##` |
| Setpoint | `*#4*ZAZB*#7*0*1*c1c2c3c4##` | `*#4*ZAZB*#7*1*1*c1c2c3c4##` | `*#4*ZAZB*#7*2*1*c1c2c3c4##` | `*#4*ZAZB*#7*3*1*c1c2c3c4##` |

OFF is encoded by ScenarioDevices as `*#4*ZAZB*#7*0*5*##`.

The MyHOME_Suite labels distinguish antifreeze/protection according to thermal context: heating uses antifreeze, cooling uses protection, and automatic/generic variants retain their own action labels. The wire structure remains the same two-value `DIMENSION 7` model.

## MyHOME_Suite local-control and fan-coil writes

ScenarioDevices also defines:

| Capability | Template |
| --- | --- |
| Local control | `*#4*ZAZB*#5*val##` |
| Fan-coil speed | `*#4*ZAZB*#11*val##` |

These are scenario-engine action templates. Their presence establishes that MyHOME_Suite can emit the write form for these operations; it does not by itself redefine every public read/status meaning attached to the same `DIMENSION` number.

## `DIMENSION 0` - measured temperature

A measured-temperature request uses `*#4*WHERE*0##`; the response carries the temperature value after `DIMENSION 0`.

Published measured/status temperature fields use four decimal digits and can represent `0000..0500` (`0.0..50.0` °C) with 0.1 °C resolution in the documented zone-status exchanges. This representation is distinct from setpoint-writing constraints.

### Historical signed-temperature interpretation

The touchscreen probe objects interpret raw `1010` as `-10` tenths of °C (-1.0 °C); exact tests cover both controlled and external probe objects. The shared converter subtracts `1000` and negates values at or above `1000`, while nonnegative tenths remain unchanged. This is implementation evidence for signed probe readings, not an expansion of the published status range above or permission to send negative setpoints through every thermal operation. See [Signed-temperature evidence](../../project/review/myopencommunity-reassessment.md#hvac-values-and-partial-records).

## `DIMENSION 11` - fan-coil speed

`DIMENSION 11` reports fan-coil speed in the published status model. ScenarioDevices additionally defines the write template `*#4*ZAZB*#11*val##`, establishing a MyHOME_Suite scenario action for fan-coil speed.

The public response/event form is `*#4*WHERE*11*SPEED*##`, including a trailing empty field. `SPEED` is `0` automatic, `1..3` the three speeds, or `15` OFF (public specification, page 15).

Read and write forms should therefore be distinguished by frame direction and operation context rather than assuming that the identifier is globally read-only in the implementation.

## `DIMENSION 12` - complete probe status

`DIMENSION 12` returns the complete probe state, combining the zone's target/status information with its operating context. It is the appropriate operation when a client needs more than the scalar measured temperature returned by `DIMENSION 0`.

The public request is `*#4*WHERE*12##` for master-probe addresses `1..99`. The response `*#4*WHERE*12*T*3##` gives the setpoint after local offset: `T` ranges over `0020..0430` in 0.1 °C units. The trailing `3` is fixed in this published flow; the actual heating/conditioning/protection state is also returned in a separate `*4*WHAT*WHERE##` frame. Do not interpret the final `3` as a complete replacement for that state frame (page 16).

The historical touchscreen client reconstructs its cached base setpoint by subtracting the known local offset from `T` while the knob is in its normal adjustment state. Its exact test combines offset `03` with `T=0250` and expects `0220` internally. The wire value remains 25.0 °C; the cached base value is 22.0 °C. See [probe-state evidence](../../project/review/myopencommunity-coverage-audit.md#probe-state-and-load-levels).

## `DIMENSION 13` - local set offset

`DIMENSION 13` reports the local setpoint offset applied at the probe. Local offset is separate from the central target temperature: a zone can therefore have a central setpoint and a probe-local adjustment simultaneously.

Request `*#4*WHERE*13##`; response/event `*#4*WHERE*13*OFFSET##` (pages 16–17).

| `OFFSET` | Knob state |
| --- | --- |
| `00` | No offset |
| `01`, `02`, `03` | +1, +2, +3 °C |
| `11`, `12`, `13` | -1, -2, -3 °C |
| `4` | Local OFF |
| `5` | Local protection |

These are codes, not signed decimal temperatures.

The historical touchscreen stores central operation separately from the local selector. Product tests start with a central manual mode, display OFF or protection under local override, then show manual again after normal adjustment resumes. The client displays zero offset during those overrides. This [client-state precedence](../../project/review/myopencommunity-hvac-history-review.md#probe-state-and-fan-coil-corrections) does not establish a physical reset.

## `DIMENSION 14` - setpoint temperature

`DIMENSION 14` is readable and writable. A zone setpoint written through the central unit uses `*#4*#WHERE*#14*T*M##`.

For this operation, `T` is encoded as four digits in `0050..0400` (5.0..40.0 °C) in 0.5 °C steps. `M` identifies the operating context: `1` heating, `2` conditioning, `3` generic.

The MyHOME_Suite functional parameter definitions likewise represent setpoint ranges and steps for Temperature Control operations; the exact parameter definition attached to the command remains authoritative for the implementation form being encoded.

The public read form is `*#4*WHERE*14##`, with response `*#4*WHERE*14*T*3##` for probe addresses `1..99`. The read table specifies 0.1 °C resolution over `0050..0400`; it does not change the 0.5 °C step specified for writes (page 18).

## Historical external-probe `DIMENSION 15`

BTicino touchscreen tests at `TS10_1_0_23` establish the external-temperature query `*#4*WHERE*15#1##`. The test report `*#4*11*15*1*123*1111##` yields temperature value `123`, after the first report field `1`. The trailing `1111` is not interpreted by the probe class. Earlier request variants were corrected in the product history; they are not interchangeable read forms. See [Temperature Control evidence](../../project/review/myopencommunity-integration.md#temperature-control).

## `DIMENSION 19` - valve status

`DIMENSION 19` reports cooling- and heating-valve state. Published valve/fan-coil values include OFF, ON, opened, closed, stop, and fan-coil speed states.

Request `*#4*WHERE*19##`; response/event `*#4*WHERE*19*CV*HV##`. `CV` is the conditioning valve and `HV` the heating valve, in that order (page 21).

| Value | Valve state |
| ---: | --- |
| `0` | OFF |
| `1` | ON |
| `2` | Opened |
| `3` | Closed |
| `4` | Stop |
| `5` | Fan-coil OFF |
| `6`, `7`, `8` | Fan-coil ON at speed 1, 2, 3 |

The published table defines values `0..8`; later information supplied by the MyHOME team documents additional fan-coil OFF-speed states `14`, `15`, and `16`. These extended values are emitted by the inspected `MyHomeServer1` `028206` and `F461` `020011` firmware tables and complement the older public PDF rather than changing the `DIMENSION 19` frame structure; retained-capture coverage is bounded by the [corpus audit](../../project/review/who4-dim19-20-output-codes.md#wider-retained-capture-corpus-audit).

## `DIMENSION 20` - actuator status

`DIMENSION 20` represents Temperature Control actuator state. The MyHOME_Suite address model supports an actuator selector appended to the zone address (`[ZA][ZB]#[N]`), allowing actuator instances to be distinguished from probe addressing.

Request `*#4*Z#N*20##`; response/event `*#4*Z#N*20*VALUE##`. The public target grammar includes `Z#N` (`Z = 0..99`, `N = 1..9`), `Z#0` for all actuators of a zone, and `0#0` for all actuators.

`VALUE` uses the same `0..8` labels as the valve table above, with additional `9` = fan-coil ON. It is therefore richer than a boolean ON/OFF value (page 22). Direct control must not be inferred merely from the existence of a status value: the public functional table classifies `DIMENSION 20` as read-only.

## `DIMENSION 22` - split control

`DIMENSION 22` is the read/write operation for split-unit control. The published protocol defines request, write and monitor/status exchanges for split control under `WHO 4`.

The request is `*#4*3#Z#N*22##`; the write is `*#4*3#Z#N*#22*MOD*SP*VEL*SWING##`. Read responses use `*#4*3#Z#N*22*MOD*SP*VEL*SWING##`. The request/write tables define `Z = 0..99`, `N = 1..9` (pages 66–68).

| Field | Published values |
| --- | --- |
| `MOD` | `0` OFF; `1` winter; `2` summer; `3` fan; `4` dehumidification; `5` automatic |
| `SP` | Temperature in tenths of °C, in 0.5 °C steps; examples `000`, `005`, `010` through `1270` |
| `VEL` | `0` automatic; `1` minimum; `2` medium; `3` maximum; `4` silent |
| `SWING` | `0` OFF; `1` ON |

The source also labels each field `NULL` for current/insignificant values, without defining a literal wire spelling. Do not transmit the letters `NULL` or assume a numeric sentinel without target-specific evidence. The monitor table omits the explicit `3#` prefix from its address note while the request/write tables include it; retain raw addresses when reconciling those reports. The write table also reverses its direction arrow; its write marker and section title establish a client write.

The broad published `SP` range is an encoding range, not a claim that a particular split unit accepts every temperature.

### Historical partial split writes

The touchscreen tests resolve the published `NULL` ambiguity for that implementation: omitted values are empty fields. Fan-mode and dehumidification writes include `*#4*45#1*#22*3**1*1##` and `*#4*45#1*#22*4**1*1##`; OFF uses a payload `0***`. This is implementation evidence for partial updates, not proof of support by every split unit or address variant.

After a non-OFF write, the client checks the first matching `DIMENSION 22` report for the exact `WHERE`, comparing only supplied write fields whose positions are present in that report. It clears the pending check even on a mismatch or a short report, emits an error for a compared mismatch, and emits no positive confirmation. Later unsolicited reports do not repeat that comparison. This [one-report check](../../project/review/myopencommunity-hvac-history-review.md#partial-split-writes-and-report-checking) is a library policy and does not verify omitted report fields or physical attainment of the requested state.

## `DIMENSION 30` - holiday end

The central unit uses separate date and time dimensions (pages 54, 57–58):

| Operation | Request | Response/event | Write |
| --- | --- | --- | --- |
| End date | `*#4*#0*30##` | `*#4*#0*30*D*M*Y##` | `*#4*#0*#30*D*M*Y##` |
| End time | `*#4*#0*31##` | `*#4*#0*31*H*MIN##` | `*#4*#0*#31*H*MIN##` |

`D` is `01..31`, `M` is `01..12`, `Y` is `2000..2099`, `H` is `00..23`, and `MIN` is `00..59`. Validate the actual calendar date as well as individual field ranges.

`DIMENSION 31` is omitted from the source's summary table but explicitly defined by its detailed flows. Some read examples mistakenly include the write marker; the response column and monitor forms establish the unprefixed report form. These operations set the deadline used by the [Temperature Control Commands](what.md).

## Historical timed-manual `DIMENSION 32`

The four-zone touchscreen class sets timed manual operation in two steps: `*4*312#0250#2*WHERE##`, then `*#4*WHERE*#32*H*MIN##` after 200 ms. The first duration is a dummy value overwritten by the second operation. The report parser consumes two values as a duration in hours and minutes, although source comments call the write an end time. Preserve this distinction rather than treating it as an absolute clock deadline. The delay and sequence are product behavior; no universal Firmware timing requirement is established.

## Historical BACnet HVAC dimensions

The BTicino touchscreen BACnet classes at `TS10_1_0_23` expose the following records under `WHO 4`. They are implementation extensions, not part of the public functional registry above. A read uses `*#4*WHERE*DIMENSION##`; a write uses `*#4*WHERE*#DIMENSION*VALUES##`.

| Dimension / class | Ordered writable fields | Additional report fields, in order |
| --- | --- | --- |
| `50` - underfloor heating | setpoint, status, mode | temperature, fault flag, fault description |
| `51` - AC split with fan coil | setpoint, status, mode, fan speed, air direction, reset filter fault | temperature, fault flag, fault description |
| `52` - air handling unit | setpoint, status, mode, humidity setpoint, airflow setpoint, minimum airflow, maximum airflow, recirculation, fan speed | temperature, fault flag, fault description, humidity, airflow, air quality, antifreeze alarm |
| `53` - variable air volume | setpoint, status, mode, airflow setpoint | temperature, fault flag, fault description |

Reports can therefore contain 6, 9, 16, or 7 ordered fields respectively. The writer retains empty positions for unspecified fields; its internal `-1` sentinel is not transmitted. For example, a status-only fan-coil write is `*#4*WHERE*#51**1****##`.

The class enums define status `0` inactive / `1` active, and mode `0` inactive, `1` winter, `2` summer, `3` fan, `4` dry, `5` normal automatic, `6` fast automatic, `7` energy-saving automatic. The remaining enum domains are:

| Field | Historical BACnet values |
| --- | --- |
| Fan speed, dimensions `51` / `52` | `0` automatic; `1` slow; `2` normal; `3` fast; `4` silent |
| Air direction, dimension `51` | `0` automatic; `1` forward; `2` backward; `3` random; `4` slow cycling; `5` cycling; `6` fast cycling; `7` stop |

A filter-reset write supplies `0` in the sixth value of dimension `51`: `*#4*WHERE*#51******0##`. The report decoder instead reads that position as a boolean filter flag. Write intent and report state therefore differ.

The report tests also distinguish a missing trailing field from an empty field already present: absent numeric fields can retain an internal unset sentinel, while present empty positions are converted to zero. The decoder does not treat an empty report position as an instruction to preserve cached state. This behavior must not be imported into the partial-write semantics.

These domains belong to this BACnet adapter model, not every `WHO 4` target. Numeric scaling and fault-description codes require the relevant adapter/Device evidence.

See [Temperature Control evidence](../../project/review/myopencommunity-integration.md#temperature-control).

## Temperature fields are operation-specific

Temperature-looking values in `WHO 4` do not have one universal range or resolution. In particular:

| Context | Published representation |
| --- | --- |
| Measured/status temperature | four digits, typically 0.1 °C resolution |
| Manual zone/central-unit setpoint write | `0050..0400`, 0.5 °C steps |
| MyHOME_Suite ScenarioDevices `DIMENSION 7` setpoint | four-digit `c1c2c3c4` field; use the associated implementation parameter definition for validation |
| Other MyHOME_Suite command parameters | range/step defined by the associated parameter record |

Decoders and encoders should therefore select the temperature representation from the `DIMENSION`/operation definition, not from `WHO 4` alone.

See [Addressing](addressing.md) for zone/probe/actuator forms, [`WHAT` Reference](what.md) for operating modes, [Cross-database functional coverage](../cross-database-coverage.md) for the implementation cross-reference, and [`DIMENSION`](../../protocol/dimensions.md) for the common `DIMENSION` frame classes.

## Observed firmware and live output codes for `DIMENSION 19`, `DIMENSION 20`, and `#20`

Published `WHO 4` v2.0.0 documentation defines `0..8` on `DIMENSION 19` and `DIMENSION 20`, documents `9` (`fan-coil ON`) only on `DIMENSION 20`, and classifies `DIMENSION 20` as read-only; live captures and static inspection of five gateway firmwares extend those operational tables without modifying the published specification boundary ([output-code evidence review](../../project/review/who4-dim19-20-output-codes.md)).

Across all five inspected gateway firmwares (`MH200N` `010108`, `F454` `020051`, `MH202` `010024`, `MyHomeServer1` `028206`, and `F461` `020011`), the discrete lookup table maps 14 SCS actuator byte values (`0..13`: `'01'` to `0`, `'00'` to `1`, `'10'` to `2`, `'11'` to `3`, `'12'` to `4`, `'20'` to `5`, `'21'..'23'` to `6..8`, `'2F'` to `9`, `'30'..'32'` to `10..12`, `'3F'` to `13`) and emits `9` on `DIMENSION 19` (`CV` / `HV`) as well as `DIMENSION 20`.

`MyHomeServer1` (`028206` `bt_termo`) and `F461` (`020011` `bt_termo`) expand the discrete lookup table to 23 entries (`0..22`) across `DIMENSION 19`, `DIMENSION 20`, and `#20`, adding `'24'..'26'` mapped to `14..16` (extended fan-coil OFF speeds `1..3`) and `'40'..'45'` mapped to `17..22`.

In `MyHomeServer1` (`028206`), `bt_thermo_manager` classifies `{0, 3, 5, 13, 14, 15, 16, 17, 100}` as inactive and `{1, 2, 4, 6..12, 18..22, 101..200}` as active (including `4` = `Stop`), whereas `bt_thermo_central_unit` classifies `{0, 3, 5, 13, 17, 100}` as inactive (omitting `14..16` from its inactive set) and `101..200` as active (`1%..100%`).

Proportional `0-10 V` SCS actuator bytes `0x80..0xE4` (`0%..100%`, encoded as `100 + pct` for codes `100..200`) are unsupported and dropped by `MH200N` (`010108`), emitted only on `DIMENSION 20` (and dropped on `DIMENSION 19`) by `F454` (`020051`) and `MH202` (`010024`), and emitted across `DIMENSION 19` (`CV` / `HV`), `DIMENSION 20`, and `#20` by `MyHomeServer1` (`028206`) and `F461` (`020011`).

In `MyHomeServer1` (`028206`), `bt_thermo_manager` emits `*#4*Z#N*#20*200##` (`100%`) and `*#4*Z#N*#20*100##` (`0%`) and compares proportional fan-coil speeds against `speed_pct + 100`.

Live sanitized capture of `MyHomeServer1` firmware `2.87.13` records spontaneous `#20` dimension writes followed by matching `20` status replies carrying `100` (`0%` proportional idle/OFF) on zone/actuator `1#3` (`*#4*1#3*#20*100##` and `*#4*1#3*20*100##`) and `2#3` (`*#4*2#3*#20*100##` and `*#4*2#3*20*100##`), alongside paired `0` (`OFF`) frames on `2#1` (`*#4*2#1*#20*0##` and `*#4*2#1*20*0##`). In this recording, the write/status intervals are `282.792 ms` for `1#3`, `24.241 ms` for `2#3`, and `17.264 ms` for `2#1`; these measurements do not establish a response-time guarantee.

Actuator and catalogue labels for discrete slots `10..13` (`'30'..'32'`, `'3F'`) and `17..22` (`'40'..'45'`) remain `unresolved`; these codes are absent from the non-synthetic retained payloads covered by the corpus audit below, even though `MyHomeServer1` (`028206` `bt_thermo_manager`) classifies `13` and `17` as inactive and `10..12` and `18..22` as active.

Output values `23..99` and values `> 200` have no mapping in the inspected `DIMENSION 19`, `DIMENSION 20`, or `#20` translators of `MH200N` (`010108`), `F454` (`020051`), `MH202` (`010024`), `MyHomeServer1` (`028206`), and `F461` (`020011`); for an unmapped SCS byte (such as `0x46`, `0x7F`, or `0xE5`), `DIMENSION 20` emits no frame on any of the five gateways and `MH200N` (`010108`), `F454` (`020051`), and `MH202` (`010024`) emit no frame on `DIMENSION 19`, whereas `MyHomeServer1` (`028206` `bt_termo`) and `F461` (`020011` `bt_termo`) leave the unmapped side empty and emit `*#4*WHERE*19*CV*HV##` with an empty value field (for example `*#4*1*19*0*##`).

A [pinned retained-capture audit](../../project/review/who4-dim19-20-output-codes.md#wider-retained-capture-corpus-audit) of `MyHOME` at `a881a4be711e7b8f03f044505c3810cfffcad403` and the retained `F461` gateway-frame excerpt in `OWNd` at `d04e453ea99b2b5dcaf36b2bfccc073eda522c48` found no extended fan-coil OFF codes `14..16`, proportional codes `101..200`, or discrete codes `10..13` and `17..22` in the examined non-synthetic payloads and logs. Synthetic/oracle fixtures and derived test expectations were inventoried separately; the audit does not cover separate bench captures, other revisions or unretained traffic. Gateway-emitted `#20` frames are retained for both `MyHomeServer1` (`2.87.13`) and `F461` (`2.0.11`), but their presence does not establish universal client-originated `#20` command support beyond the published read-only classification of `DIMENSION 20`.

## Four-zone central-unit (`#0#C`) `DIMENSION 14` and zone status behavior

Inspection of BTicino four-zone central-unit `4695` (`HC/HS/L/N/NT4695`, `AM5875`) Firmware `01.01.03` (`LH4695_AM5875_010103.fwz`) and 13 gateway Firmwares establishes the `DIMENSION 14` write, read, and zone-report behavior on `#0#C` plants ([four-zone central-unit evidence review](../../project/review/who4-4695-four-zone-central-unit.md)). The retained runs execute gateway Firmware with synthetic bus inputs or simulated controller/probe models; they do not execute the original `4695` Firmware. The separately reported original-controller execution awaits a retained record; see the [execution scope](../../project/review/who4-4695-four-zone-central-unit.md#execution-scope-and-outstanding-record).

**`DIMENSION 14` manual setpoint season filter (`M=1`, `M=2`, `M=3`) on `#0#C`.** Generation B, C, and D gateways translate `*#4*#0#C*#14*T*M##` (`T = 0050..0400` in 0.5 °C steps, encoded in half-degrees as `B6 = T_celsius * 2`, for example `0x24 = 36` for `18.0 °C`; `4695` Firmware `01.01.03` enforces `B6 <= 0x46` (`0.0..35.0 °C`), so intersected with gateway `0050..0400` accepted writes span `B6 = 0x0A..0x46` (`5.0..35.0 °C`) while `35.5..40.0 °C` (`B6 = 0x47..0x50`) is silently dropped with `TX=[]`) into `$18 D1 <CU> 03 02 C1 <B5> <B6> 00`, mapping `M=1` (heating) to `B5=0x12`, `M=2` (conditioning) to `B5=0x22`, and `M=3` (generic) to `B5=0x02` (Generation A collapses `<CU>` to `00`, which `4695` ignores). In `4695` Firmware `01.01.03`, the `$18 C1` season filter accepts `B5=0x12` (`M=1`) only when the central unit is in Heating season (dropping `M=1` silently with `TX=[]` in Cooling season), accepts `B5=0x22` (`M=2`) only when the central unit is in Cooling season (dropping `M=2` silently with `TX=[]` in Heating season), and accepts `B5=0x02` (`M=3`, `*#4*#0#C*#14*T*3##`) unconditionally in both Heating and Cooling seasons, broadcasting `$18 D2 <CU> 03 04 C0 12 <B6> <B7>` (`*4*110#TTTT*#0#C##` in Heating) or `C0 22 <B6> <B7>` (`*4*210#TTTT*#0#C##` in Cooling).

**`*#4*#0#C*14##` read behavior versus `*#4*#0#C##` status requests.** Across Generation A (`MH200` `020102`, `H4684` `020054`), Generation B (`MH200N` `010108`, `F453AV` `030014`, `F453` `010100`), and Generation C (`F454` `020051`, `F459` `020105`, `F450` `020010`, `MH202` `010024`), `*#4*#0#C*14##` is rejected with `NACK` (`TX=[]`), and all 13 gateways reject `*#4*#0#C*0##` and `*#4*#0#C*12##` with `NACK` (`TX=[]`). On Generation D (`MyHomeServer1` `028206`, `F461` `020011`, `F460` `020012`, `3488` `030205`), `*#4*#0#C*14##` strips the `#0#` prefix and transmits `$04 99 <CU> 30 0E` (a local Zone `C` `DIMENSION 14` read rather than a central-unit `C0` query), which `4695` Firmware `01.01.03` answers for its built-in master probe `Z = C` as `*#4*C*14*TTTT*3##`. To read the central unit's own operating mode and manual setpoint on Generation B, C, and D gateways, clients must send dimensionless `*#4*#0#C##` (`$04 99 <CU> 30 C0`, answered with `$18 D2 <CU> 03 04 C0 ...` -> `*4*WHAT*#0#C##`).

**Outbound broadcast asymmetry between built-in Zone `C` and slave zones `C+1..C+3`.** When `#0#C` changes setpoint or mode, `4695` Firmware `01.01.03` transmits its central `$18 D2 <CU> 03 04 C0 ...` broadcast (`*4*WHAT*#0#C##`) followed by `$04 90/91 <C+1..C+3> 30 <T*2>` or `$04 93 <C+1..C+3> 30 <mode>` master-to-slave push telegrams to its external slave zones, without immediately emitting a separate `$18 D2 <C> 03 04 12 ...` (`*#4*C*12*TTTT*3##`) status report for its built-in master probe `Z = C`. External slave probes `C+1..C+3` respond to the master-to-slave push by broadcasting their own `DIMENSION 12` (`*#4*(C+k)*12*TTTT*3##`) and `WHAT` (`*4*WHAT*(C+k)##`) updates on the SCS bus, whereas built-in Zone `C` emits `DIMENSION 0`, `DIMENSION 12`, `DIMENSION 13`, and `DIMENSION 14` frames on periodic thermal measurement cycles or when explicitly queried with `*#4*C##`, `*#4*C*0##`, `*#4*C*12##`, `*#4*C*13##`, or `*#4*C*14##` (`$04 99 <C> 30 00/12/0E/0D`).

## Evidence basis

Published payloads and page references above come from the [Temperature Control Specification](https://archive.openwebnet-ha.org/sha256/35/68/35685145d0db92e2f45bea1e45bf878b06927cfe5756aeb774436cf7bdc16d89.pdf), version 2.0.0. ScenarioDevices extensions and reported later-device behavior remain separately identified. The same PDF also defines [Temperature Control Fault Diagnostics](../../diagnostics/temperature-control-faults.md) under `WHO 1004`; those are not functional `WHO 4` dimensions.
