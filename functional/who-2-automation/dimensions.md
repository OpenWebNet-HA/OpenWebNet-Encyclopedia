# `DIMENSION` Reference

The published `WHO 2` Automation protocol defines `DIMENSION 10` for advanced shutter state and `DIMENSION 11` for absolute positioning.

| `DIMENSION` | Function | Direction |
| ---: | --- | --- |
| `10` | Shutter status | Request / response / event |
| `11` | Go to level | Write |

## `DIMENSION 10` — shutter status

Request:

`*#2*WHERE*10##`

The status payload contains four values in this order:

`shutterStatus`, `shutterLevel`, `shutterPriority`, `shutterInfo`.

The corresponding status/event form is `*#2*WHERE*10*SHUTTER_STATUS*SHUTTER_LEVEL*SHUTTER_PRIORITY*SHUTTER_INFO##`.

### Shutter status

| Value | Meaning |
| ---: | --- |
| `10` | Stop |
| `11` | Up |
| `12` | Down |
| `13` | Step-by-step up |
| `14` | Step-by-step down |

### Shutter level

| Value | Meaning |
| ---: | --- |
| `0` | Fully closed |
| `1`–`99` | Current position (%) |
| `100` | Fully open |
| `255` | Unknown position |

### Shutter information

| Value | Meaning |
| ---: | --- |
| `0` | Normal |
| `12` | PUL + disabled |
| `13` | Disabled |
| `14` | Command not executed |
| `15` | PUL |

`shutterPriority` carries the Automation priority state associated with the advanced shutter. The priority model uses Safety, High, and Medium priority flags; see [`what.md`](what.md).

For general, environment, or group requests, the server can return one `DIMENSION 10` status frame for each Automation Object in the addressed scope.

## `DIMENSION 11` — go to level

`DIMENSION 11` writes an absolute shutter position. The published write form is:

`*#2*WHERE*#11#SHUTTER_PRIORITY*SHUTTER_LEVEL##`

MyHOME_Suite uses this operation with the priority field encoded in the parameterized `DIMENSION`, for example the canonical form `*#2*WHERE*#11#001*LEVEL##`.

The target level uses the same `0`–`100` position scale as shutter status. `0` is fully closed, `100` fully open, and intermediate values represent percentage position.

After a go-to-level operation, event traffic can include the `DIMENSION 11` operation, `DIMENSION 10` state updates, movement events, and a final stop/state update when the requested level is reached.

See [`addressing.md`](addressing.md) for scope expansion rules and [`../../protocol/dimensions.md`](../../protocol/dimensions.md) for the common `DIMENSION` frame classes.