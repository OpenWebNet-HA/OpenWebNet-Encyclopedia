# `DIMENSION` Reference

`WHO 1` uses `DIMENSION` operations for Lighting values that are more structured or precise than ordinary `WHAT` values.

| `DIMENSION` | Meaning | Published operations |
| ---: | --- | --- |
| `1` | Level and transition speed | Read/report/write |
| `2` | Temporization | Read/report/write |
| `3` | Return only Lighting Objects that are ON | Read |
| `4` | 100-level dimmer status with ON/OFF speed | Identifier listed; no detailed flow in the source |
| `8` | Accumulated lamp working time | Read/report |
| `9` | Maximum lamp working time | Read/report/write |

## Value fields

| Field | Published range and encoding |
| --- | --- |
| `LEVEL100` | `100` = OFF; `101..199` = 1%..99%; `200` = maximum |
| `SPEED` | `0` = last speed; `1..254` = explicit speed; `255` = default speed |
| `HOURS` | `0..255` |
| `MINUTES` | `0..59` |
| `SECONDS` | `0..59` |
| `WORKING_TIME` | `1..100000` hours |

`LEVEL100` is offset by 100. It is not a literal percentage field and must not be decoded as `100%..200%`.

## `DIMENSION 1` - level and speed

Write:

~~~text
*#1*WHERE*#1*LEVEL100*SPEED##
~~~

Request and response/report:

~~~text
*#1*WHERE*1##
*#1*WHERE*1*LEVEL100*SPEED##
~~~

The PDF prints one write example without the `*` before `#1`; this conflicts with its common write grammar and the otherwise consistent frame family. This documentation uses the structurally consistent form above and records the source inconsistency rather than treating the missing separator as a new syntax.

## `DIMENSION 2` - temporization

~~~text
*#1*WHERE*#2*HOURS*MINUTES*SECONDS##
*#1*WHERE*2##
*#1*WHERE*2*HOURS*MINUTES*SECONDS##
~~~

This explicit duration is distinct from fixed-duration `WHAT 11..18` commands. The published event flow after a write reports ordinary Lighting state and, for a dimmer, a fine-grained level/speed report.

## `DIMENSION 3` - only Objects that are ON

`*#1*WHERE*3##` is a filtered request. The server returns ordinary Lighting status frames only for addressed lights or dimmers that are ON, then terminates the sequence with `ACK`.

This is not a scalar property response and should be modeled as a query producing zero or more result frames.

## `DIMENSION 4` - 100-level status

The canonical `DIMENSION` table names `4` as 100-level dimmer status with ON/OFF speed, but the document does not provide a detailed request/write flow for it. Do not invent its payload from `DIMENSION 1` merely because their descriptions overlap.

### Observed SCS behavior

Controlled first-hand captures on one F418U2 establish that `DIMENSION 1` and `DIMENSION 4` are distinct runtime state surfaces, even when they report the same `LEVEL100`. At `LEVEL100 = 130`, the same actuator emitted `DIMENSION 1` with a trailing value of `5` and `DIMENSION 4` with a trailing value of `2`. The published names therefore correspond to distinct secondary state on this Device; the observations do not establish the physical-time mapping or complete semantics of the `DIMENSION 4` trailing value.

Gateway handling is not uniform:

- through an MH202, explicit `DIMENSION 1` and `DIMENSION 4` reads preserved the requested dimension. In the sampled states, direct reads returned a trailing `0`, while subsequent actuator reports exposed nonzero values such as `5` for `DIMENSION 1` and `2` for `DIMENSION 4`;
- through an F454, direct reads returned the nonzero values in the sampled states, and a `DIMENSION 1` request while the actuator was OFF was answered with a `DIMENSION 4` frame instead;
- a positive-level `DIMENSION 4` write was observed to succeed through the MH202. The equivalent write through the F454 did not produce the expected state change in the sampled run, while the immediately following `DIMENSION 1` write succeeded. This is a bounded negative observation, not proof that every F454 firmware universally rejects `DIMENSION 4` writes.

A classic F414 observed through an MH200 supports `DIMENSION 1` reads and writes with the same `LEVEL100 + SPEED` structure. A companion tester report states that a `DIMENSION 4` request to that F414 timed out and ended in `NACK`; the raw DIM4 exchange is not present in the preserved capture, so that absence remains reported rather than capture-established evidence.

These observations have two implementation consequences:

1. do not collapse the secondary values of `DIMENSION 1` and `DIMENSION 4` into one field;
2. do not require a response to use the same `DIMENSION` identifier as the request, because the observed F454/F418U2 OFF-state query is a counterexample.

Device and gateway applicability remain part of capability handling. The cross-gateway evidence status and remaining unknowns are tracked in the [Relationship Register](../../reverse-engineering/relationship-register.md) and [Open Questions](../../reverse-engineering/open-questions.md).

## `DIMENSION 8` - working time

~~~text
*#1*WHERE*8##
*#1*WHERE*8*WORKING_TIME##
~~~

The response can also appear on the event session.

## `DIMENSION 9` - maximum working time

~~~text
*#1*WHERE*#9*WORKING_TIME##
*#1*WHERE*9##
*#1*WHERE*9*WORKING_TIME##
~~~

The value is expressed in hours. Read and write support still depends on the target capability.

## Capability boundary

The global `WHO 1` vocabulary does not imply that every Lighting Object implements every operation. Validate Device/firmware/Object applicability through the catalogue model where available.

## Evidence basis

Identifiers, ranges, direction, and frame flows come from [`WHO 1` specification](../../sources/openwebnet-public/pdf/WHO_1.pdf). MyHOME Suite ScenarioDevices corroborates functional level-control use but does not replace the published field encodings.

See [`WHAT` Reference](what.md), [Addressing](addressing.md), and the common [`DIMENSION` model](../../protocol/dimensions.md).
