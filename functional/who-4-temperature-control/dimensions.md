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

## `DIMENSION 11` - fan-coil speed

`DIMENSION 11` reports fan-coil speed in the published status model. ScenarioDevices additionally defines the write template `*#4*ZAZB*#11*val##`, establishing a MyHOME_Suite scenario action for fan-coil speed.

The public response/event form is `*#4*WHERE*11*SPEED*##`, including a trailing empty field. `SPEED` is `0` automatic, `1..3` the three speeds, or `15` OFF (public specification, page 15).

Read and write forms should therefore be distinguished by frame direction and operation context rather than assuming that the identifier is globally read-only in the implementation.

## `DIMENSION 12` - complete probe status

`DIMENSION 12` returns the complete probe state, combining the zone's target/status information with its operating context. It is the appropriate operation when a client needs more than the scalar measured temperature returned by `DIMENSION 0`.

The public request is `*#4*WHERE*12##` for master-probe addresses `1..99`. The response `*#4*WHERE*12*T*3##` gives the setpoint after local offset: `T` ranges over `0020..0430` in 0.1 °C units. The trailing `3` is fixed in this published flow; the actual heating/conditioning/protection state is also returned in a separate `*4*WHAT*WHERE##` frame. Do not interpret the final `3` as a complete replacement for that state frame (page 16).

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

## `DIMENSION 14` - setpoint temperature

`DIMENSION 14` is readable and writable. A zone setpoint written through the central unit uses `*#4*#WHERE*#14*T*M##`.

For this operation, `T` is encoded as four digits in `0050..0400` (5.0..40.0 °C) in 0.5 °C steps. `M` identifies the operating context: `1` heating, `2` conditioning, `3` generic.

The MyHOME_Suite functional parameter definitions likewise represent setpoint ranges and steps for Temperature Control operations; the exact parameter definition attached to the command remains authoritative for the implementation form being encoded.

The public read form is `*#4*WHERE*14##`, with response `*#4*WHERE*14*T*3##` for probe addresses `1..99`. The read table specifies 0.1 °C resolution over `0050..0400`; it does not change the 0.5 °C step specified for writes (page 18).

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

The published table defines values `0..8`; later information supplied by the MyHOME team documents additional fan-coil OFF-speed states `14`, `15`, and `16`. These extended values have been observed in real `WHO 4` status responses and complement the older public PDF rather than changing the `DIMENSION 19` frame structure.

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

## `DIMENSION 30` - holiday end

The central unit uses separate date and time dimensions (pages 54, 57–58):

| Operation | Request | Response/event | Write |
| --- | --- | --- | --- |
| End date | `*#4*#0*30##` | `*#4*#0*30*D*M*Y##` | `*#4*#0*#30*D*M*Y##` |
| End time | `*#4*#0*31##` | `*#4*#0*31*H*MIN##` | `*#4*#0*#31*H*MIN##` |

`D` is `01..31`, `M` is `01..12`, `Y` is `2000..2099`, `H` is `00..23`, and `MIN` is `00..59`. Validate the actual calendar date as well as individual field ranges.

`DIMENSION 31` is omitted from the source's summary table but explicitly defined by its detailed flows. Some read examples mistakenly include the write marker; the response column and monitor forms establish the unprefixed report form. These operations set the deadline used by the [Temperature Control Commands](what.md).

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

## Evidence basis

Published payloads and page references above come from the [Temperature Control Specification](../../sources/openwebnet-public/pdf/WHO_4.pdf), version 2.0.0. ScenarioDevices extensions and reported later-device behavior remain separately identified. The same PDF also defines [Temperature Control Fault Diagnostics](../../diagnostics/temperature-control-faults.md) under `WHO 1004`; those are not functional `WHO 4` dimensions.
