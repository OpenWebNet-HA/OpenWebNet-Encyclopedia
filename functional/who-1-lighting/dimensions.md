# `DIMENSION` Reference

`WHO 1` uses `DIMENSION` operations for Lighting values that are more structured or more precise than the ordinary `WHAT` vocabulary. The published protocol defines level, speed, temporization, status and operating-time functions; MyHOME_Suite functional data confirms the parameterized write forms used by the application.

| `DIMENSION` | Meaning |
| ---: | --- |
| `1` | Lighting level and transition speed |
| `2` | Temporization |
| `3` | Required-only-ON operation |
| `4` | 100-level status |
| `8` | Lamp working-time information |
| `9` | Lamp working-time information |

Read requests and responses follow the common `DIMENSION` frame classes documented in [`../../protocol/dimensions.md`](../../protocol/dimensions.md). Read and write support is operation- and Device-dependent and must not be inferred solely from the existence of a `DIMENSION` identifier.

## `DIMENSION 1` — level and transition speed

MyHOME_Suite uses the write form `*#1*WHERE*#1*LEVEL*SPEED##`.

`LEVEL` expresses the requested Lighting level while `SPEED` expresses the transition behavior. This operation provides finer control than the ordinary `WHAT 2`–`10` discrete levels. Encoders must preserve both values: transition speed is part of the operation rather than metadata external to the frame.

The MyHOME_Suite ScenarioDevices capability data also represents Lighting level control through this functional template, confirming that the operation is available to higher-level scenario actions as well as direct functional control.

## `DIMENSION 2` — temporization

MyHOME_Suite uses `*#1*WHERE*#2*HOURS*MINUTES*SECONDS##` for explicit Lighting temporization.

The three-value payload represents the duration as hours, minutes and seconds. This structured temporization is distinct from the predefined timed `WHAT 11`–`18` operations: those `WHAT` values select fixed durations, whereas `DIMENSION 2` carries an explicit duration.

## `DIMENSION 3` — required only ON

`DIMENSION 3` belongs to the Lighting advanced-operation vocabulary and is associated with the required-only-ON function. Its values are local to this `DIMENSION`; they must not be interpreted using the level or temporization schemas of `DIMENSION 1` or `2`.

## `DIMENSION 4` — 100-level status

`DIMENSION 4` provides Lighting status on the finer 100-level scale. It complements the coarse ordinary `WHAT` status values and allows a client to represent dimmer state with greater precision.

This status representation should remain distinct from a command template: a fine-grained reported level does not imply that every target supports the same write capabilities.

## `DIMENSION 8` and `DIMENSION 9` — lamp working time

`DIMENSION 8` and `DIMENSION 9` expose lamp operating-time information. These are informational/measurement functions rather than ordinary switching commands.

Working-time values describe accumulated operation and should not be normalized into Lighting level or temporization values merely because all are carried in `DIMENSION` frames.

## Capability model

The presence of a Lighting `DIMENSION` in the protocol namespace does not mean that every Lighting Object implements it. The MyHOME_Suite catalogue distinguishes command, actuator and dimmer capabilities at the Object/firmware level, while ScenarioDevices exposes only the operations usable in its scenario capability model. Protocol implementations should therefore separate the global `WHO 1` vocabulary from per-Object capabilities.

See [`what.md`](what.md) for ordinary Lighting operations and [`addressing.md`](addressing.md) for address scopes.