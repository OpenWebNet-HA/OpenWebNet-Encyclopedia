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
| `30` | Holiday-scenario end date/time | Read / write |

The MyHOME_Suite protocol data additionally defines Temperature Control command templates using `DIMENSION 7`. This implementation operation is not part of the published functional `DIMENSION` table above and should be treated according to its MyHOME_Suite command template rather than silently equated with another public `DIMENSION`.

## `DIMENSION 0` — measured temperature

A measured-temperature request uses `*#4*WHERE*0##`; the response carries the temperature value after `DIMENSION 0`.

Published measured/status temperature fields use four decimal digits and can represent `0000`–`0500` (0.0–50.0 °C) with 0.1 °C resolution in the documented zone-status exchanges. This representation is distinct from setpoint-writing constraints.

## `DIMENSION 11` — fan-coil speed

`DIMENSION 11` reports fan-coil speed. It is a status operation; its value must be interpreted using the Temperature Control fan-coil state model rather than as a temperature.

## `DIMENSION 12` — complete probe status

`DIMENSION 12` returns the complete probe state, combining the zone's target/status information with its operating context. It is the appropriate operation when a client needs more than the scalar measured temperature returned by `DIMENSION 0`.

Observed MyHOME/OpenWebNet traffic confirms this form is used for thermostat state reporting; for example, a frame can carry a four-digit target temperature followed by an operating-mode value.

## `DIMENSION 13` — local set offset

`DIMENSION 13` reports the local setpoint offset applied at the probe. Local offset is separate from the central target temperature: a zone can therefore have a central setpoint and a probe-local adjustment simultaneously.

## `DIMENSION 14` — setpoint temperature

`DIMENSION 14` is readable and writable. A zone setpoint written through the central unit uses `*#4*#WHERE*#14*T*M##`.

For this operation, `T` is encoded as four digits from `0050` to `0400` (5.0–40.0 °C) in 0.5 °C steps. `M` identifies the operating context: `1` heating, `2` conditioning, `3` generic.

The MyHOME_Suite functional parameter definitions likewise represent setpoint ranges and steps for Temperature Control operations; the exact parameter definition attached to the command remains authoritative for the implementation form being encoded.

## `DIMENSION 19` — valve status

`DIMENSION 19` reports cooling- and heating-valve state. Published valve/fan-coil values include OFF, ON, opened, closed, stop, and fan-coil speed states.

The published table defines values `0`–`8`; later information supplied by the MyHOME team documents additional fan-coil OFF-speed states `14`, `15`, and `16`. These extended values have been observed in real `WHO 4` status responses and complement the older public PDF rather than changing the `DIMENSION 19` frame structure.

## `DIMENSION 20` — actuator status

`DIMENSION 20` represents Temperature Control actuator state. The MyHOME_Suite address model supports an actuator selector appended to the zone address (`[ZA][ZB]#[N]`), allowing actuator instances to be distinguished from probe addressing.

Status frames observed on current systems use this operation to report actuator ON/OFF state. Direct control must not be inferred merely from the existence of a status value: the public functional table classifies `DIMENSION 20` as read-only.

## `DIMENSION 22` — split control

`DIMENSION 22` is the read/write operation for split-unit control. The published protocol defines request, write and monitor/status exchanges for split control under `WHO 4`.

Its payload is operation-specific and should be preserved as a structured split-control value set rather than normalized to the ordinary thermostat setpoint model.

## `DIMENSION 30` — holiday end

`DIMENSION 30` reads and writes the end of a holiday scenario. It is used with the central-unit holiday/vacation operations documented in [`what.md`](what.md), including return to a weekly program when the holiday deadline is reached.

## Temperature fields are operation-specific

Temperature-looking values in `WHO 4` do not have one universal range or resolution. In particular:

| Context | Published representation |
| --- | --- |
| Measured/status temperature | four digits, typically 0.1 °C resolution |
| Manual zone/central-unit setpoint write | `0050`–`0400`, 0.5 °C steps |
| MyHOME_Suite command parameters | range/step defined by the associated parameter record |

Decoders and encoders should therefore select the temperature representation from the `DIMENSION`/operation definition, not from `WHO 4` alone.

See [`addressing.md`](addressing.md) for zone/probe/actuator forms, [`what.md`](what.md) for operating modes, and [`../../protocol/dimensions.md`](../../protocol/dimensions.md) for the common `DIMENSION` frame classes.