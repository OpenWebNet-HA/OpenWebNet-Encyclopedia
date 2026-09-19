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
