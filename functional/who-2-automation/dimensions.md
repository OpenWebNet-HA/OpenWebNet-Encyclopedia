# `DIMENSION` Reference

`WHO 2` uses `DIMENSION 10` for advanced shutter state and `DIMENSION 11` for absolute positioning. The published protocol defines the payload semantics; MyHOME_Suite implementation data confirms the parameterized absolute-position operation used by the application.

| `DIMENSION` | Function | Direction |
| ---: | --- | --- |
| `10` | Shutter status | Request / response / event |
| `11` | Go to level | Write |

## `DIMENSION 10` — shutter status

Request: `*#2*WHERE*10##`.

The status payload contains four values, in order: `shutterStatus`, `shutterLevel`, `shutterPriority`, `shutterInfo`.

The corresponding status/event form is `*#2*WHERE*10*SHUTTER_STATUS*SHUTTER_LEVEL*SHUTTER_PRIORITY*SHUTTER_INFO##`.

### Shutter status

| Value | Meaning |
| ---: | --- |
| `10` | Stop |
| `11` | Up |
| `12` | Down |
| `13` | Step-by-step up |
| `14` | Step-by-step down |

These are `DIMENSION 10` state values. Values `13` and `14` therefore describe step-by-step shutter state and must not be promoted to ordinary `WHO 2` command functions without separate evidence.

### Shutter level

| Value | Meaning |
| ---: | --- |
| `0` | Fully closed |
| `1`–`99` | Current position (%) |
| `100` | Fully open |
| `255` | Unknown position |

The level is the shutter's absolute position model. It is distinct from the relative shutter-step parameter used by advanced Up/Down commands.

### Shutter priority

`shutterPriority` carries the encoded priority state associated with the advanced shutter. The Automation priority model distinguishes Safety, High, and Medium priority flags. The same priority model participates in advanced movement commands and the parameterized absolute-position operation; see [`what.md`](what.md).

### Shutter information

| Value | Meaning |
| ---: | --- |
| `0` | Normal |
| `12` | PUL + disabled |
| `13` | Disabled |
| `14` | Command not executed |
| `15` | PUL |

For general, environment, or group requests, the server can return one `DIMENSION 10` status frame for each Automation Object in the addressed scope. This expansion is part of the functional addressing behavior rather than a change to the four-value payload.

## `DIMENSION 11` — go to level

`DIMENSION 11` writes an absolute shutter position. The published write form is `*#2*WHERE*#11#SHUTTER_PRIORITY*SHUTTER_LEVEL##`.

The MyHOME_Suite functional data uses the same parameterized operation. A concrete application form is `*#2*WHERE*#11#001*LEVEL##`, where the parameter attached to `DIMENSION 11` carries the priority field and `LEVEL` carries the target position. The parameter must therefore be preserved by encoders rather than treating the operation as an unparameterized `DIMENSION 11` write.

### Target level

| Value | Meaning |
| ---: | --- |
| `0` | Fully closed |
| `1`–`99` | Target position (%) |
| `100` | Fully open |

`255`, used by `DIMENSION 10` to report an unknown current position, is not a target position.

### Resulting state traffic

An absolute-position operation changes shutter state over time rather than representing an instantaneous scalar assignment. Event traffic can therefore include the `DIMENSION 11` operation, `DIMENSION 10` state updates, movement events, and a final stop/state update when the requested level is reached.

The exact sequence visible to a client depends on the addressed device and event propagation; clients should use the resulting state reports rather than assuming that the write frame alone represents the final physical state.

See [`addressing.md`](addressing.md) for scope expansion rules and [`../../protocol/dimensions.md`](../../protocol/dimensions.md) for the common `DIMENSION` frame classes.