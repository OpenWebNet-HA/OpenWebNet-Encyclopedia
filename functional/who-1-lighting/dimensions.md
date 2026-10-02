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

A 27 September 2026 [public MH200/F418U2 trace](https://github.com/GreenGrassBlueOcean/MyHOME/blob/d7471368e04cbf311ea82668306d926baef4b178/tests/fixtures/traces/issue_466/myhome_trace_MH200_f418u2_dimmer_2026-09-27T12-15-00.json) through an MH200 running firmware 2.1.0 adds first-hand runtime evidence for the F418U2. Positive `DIMENSION 1` writes were accepted: a write to `LEVEL100 = 150` with `SPEED = 0` was followed immediately by a `DIMENSION 1` report with `LEVEL100 = 150` and trailing value `5`, while a later direct read at the same level returned trailing value `2`. A write to `LEVEL100 = 200` likewise produced an immediate trailing value `5`. Therefore, the written `SPEED` value must not be assumed to be echoed unchanged in the following report.

The same MH200/F418U2 trace also observed coarse `WHAT` commands and subsequent fine-level reads: `WHAT 3 -> LEVEL100 110`, `WHAT 5 -> LEVEL100 130`, `WHAT 7 -> LEVEL100 150`, and `WHAT 10 -> LEVEL100 200`. These are Device-path observations, not a replacement for the published `WHAT` table; the exact relationship between the coarse command labels and the F418U2 fine-level state remains implementation evidence rather than a universal encoding rule.

## `DIMENSION 2` - temporization

~~~text
*#1*WHERE*#2*HOURS*MINUTES*SECONDS##
*#1*WHERE*2##
*#1*WHERE*2*HOURS*MINUTES*SECONDS##
~~~

This explicit duration is distinct from fixed-duration `WHAT 11..18` commands. The published event flow after a write reports ordinary Lighting state and, for a dimmer, a fine-grained level/speed report.

### Historical timer handling

The BTicino touchscreen library at `TS10_1_0_23` ignores the report payload `255*255*255` as unusable timer state. It retains `0*0*0` as a zero duration. This is implementation evidence for interpreting historical reports, not an extension of the published minute/second ranges. See [Lighting evidence](../../project/review/myopencommunity-integration.md#lighting-and-automation).

## `DIMENSION 3` - only Objects that are ON

`*#1*WHERE*3##` is a filtered request. The server returns ordinary Lighting status frames only for addressed lights or dimmers that are ON, then terminates the sequence with `ACK`.

This is not a scalar property response and should be modeled as a query producing zero or more result frames.

## `DIMENSION 4` - 100-level status

The canonical `DIMENSION` table names `4` as 100-level dimmer status with ON/OFF speed, but the document does not provide a detailed request/write flow for it. Do not invent its payload from `DIMENSION 1` merely because their descriptions overlap.

Controlled first-hand captures on one F418U2 establish that `DIMENSION 1` and `DIMENSION 4` are distinct runtime state surfaces, even when they report the same `LEVEL100`. At `LEVEL100 = 130`, the same actuator emitted `DIMENSION 1` with a trailing value of `5` and `DIMENSION 4` with a trailing value of `2`. The published names therefore correspond to distinct secondary state on this Device; the observations do not establish the physical-time mapping or complete semantics of the `DIMENSION 4` trailing value.

Gateway handling is not uniform:

- through an MH202, explicit `DIMENSION 1` and `DIMENSION 4` reads preserved the requested dimension. In the sampled states, direct reads returned a trailing `0`, while subsequent actuator reports exposed nonzero values such as `5` for `DIMENSION 1` and `2` for `DIMENSION 4`;
- through an F454, direct reads returned the nonzero values in the sampled states, and a `DIMENSION 1` request while the actuator was OFF was answered with a `DIMENSION 4` frame instead;
- through an MH200 running firmware 2.1.0, the [public MH200/F418U2 trace](https://github.com/GreenGrassBlueOcean/MyHOME/blob/d7471368e04cbf311ea82668306d926baef4b178/tests/fixtures/traces/issue_466/myhome_trace_MH200_f418u2_dimmer_2026-09-27T12-15-00.json) shows `DIMENSION 1` reads and writes working while explicit `DIMENSION 4` requests receive no response in the captured windows. A positive `DIMENSION 4` write to `LEVEL100 = 130` was followed by a `DIMENSION 1` read still reporting `LEVEL100 = 150`, so the requested state change did not occur on that tested path. When the actuator was OFF, a `DIMENSION 1` request remained a `DIMENSION 1` response and returned `LEVEL100 = 100` with trailing value `2`;
- a positive-level `DIMENSION 4` write was observed to succeed through the MH202. The equivalent write through the F454 did not produce the expected state change in the sampled run, while the immediately following `DIMENSION 1` write succeeded. The MH200 trace independently shows another path on which the sampled positive `DIMENSION 4` write did not change state. These are bounded observations, not proof of a universal gateway-family rule.

A classic F414 observed through an MH200 supports `DIMENSION 1` reads and writes with the same `LEVEL100 + SPEED` structure. A companion tester report states that a `DIMENSION 4` request to that F414 timed out and ended in `NACK`; the raw DIM4 exchange is not present in the preserved capture. The new F418U2/MH200 trace independently shows no DIM4 response on the same gateway model, making an MH200-path limitation more plausible, but it does not by itself establish whether the cause is gateway-wide, firmware-specific, or interaction-specific.

These observations have three implementation consequences:

1. do not collapse the secondary values of `DIMENSION 1` and `DIMENSION 4` into one field;
2. do not require a response to use the same `DIMENSION` identifier as the request, because the observed F454/F418U2 OFF-state query is a counterexample;
3. treat `DIMENSION 4` availability and write behavior as gateway/Device-path capability. The tested MH200/F418U2 path did not expose DIM4 read/write behavior that was available through the tested MH202 path.

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

Identifiers, ranges, direction, and frame flows come from [`WHO 1` specification](https://archive.openwebnet-ha.org/sha256/8a/da/8adafaaeac5e07a5eee247792f70b659e4ea9d99b45fffbd415f94a49976fb4a.pdf). MyHOME Suite ScenarioDevices corroborates functional level-control use but does not replace the published field encodings.

See [`WHAT` Reference](what.md), [Addressing](addressing.md), and the common [`DIMENSION` model](../../protocol/dimensions.md).
