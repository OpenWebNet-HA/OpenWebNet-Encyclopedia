# `WHO 16` - Sound System

`WHO 16` controls the earlier Sound System dialect: amplifiers, sources, tuner frequency, stored stations, RDS, volume, tone, balance, sleep, and Follow Me.

## `WHAT` values

| `WHAT` | Meaning |
| ---: | --- |
| `0` / `3` | ON using base-band / stereo-channel source |
| `10` / `13` | OFF using base-band / stereo-channel source |
| `20` / `23` | Cycle source, base band / stereo channel |
| `30` / `33` | Sleep on base band / stereo channel |
| `40` | Sleep OFF |
| `50` / `53` | Follow Me, base band / stereo channel |
| `100` | Source busy |
| `101` / `102` | Start / stop RDS transmission |
| `1001..1015` | Increase volume by `1..15` |
| `1101..1115` | Decrease volume by `1..15` |
| `2001..2015` | Increase high tones by `1..15` |
| `2101..2115` | Decrease high tones by `1..15` |
| `5000` | Seek next higher free frequency |
| `5001..5015` | Increase frequency by `0.05..0.75 MHz` |
| `5100` | Seek next lower free frequency |
| `5101..5115` | Decrease frequency by `0.05..0.75 MHz` |
| `6001..6015` | Advance station/track by `1..15` |
| `6101..6115` | Move back station/track by `1..15` |

The final digits carry magnitude and are part of `WHAT`.

## `WHERE`

| Target | `WHERE` |
| --- | --- |
| All amplifiers | `0` |
| Amplifiers in environment `0..9` | `#0..#9` |
| Individual amplifier | `01..99` |
| All sources | `100` |
| Source `1..9` | `101..109` |

Amplifier and source targets share the namespace but have different ranges. Preserve leading zeroes on amplifier addresses.

## Amplifier address structure

A two-digit amplifier `WHERE` `EA` carries an environment digit followed by the amplifier number within that environment: `23` is amplifier 3 in environment 2. The F441M multichannel matrix ties environments to its outputs one to one: its documentation requires amplifiers on output `n` to be configured with room address `A = n`.

This decomposition is corroborated rather than published: the `WHO 22` counterparts emitted by one gateway write the same addresses as `3#AREA#POINT`, so `11` appears there as area 1, point 1. See [Sound Matrix Source Routing](../../reverse-engineering/sound-matrix-routing.md).

Single-digit amplifier addresses are admitted by the specification. Their environment is ambiguous and has not been observed on hardware.

## Matrix source routing

The specification defines no message that assigns a source to an amplifier. Source **cycling** is specified (`WHAT 20` / `23` on `WHERE 100`); directed selection is not.

Implementations perform directed selection with a three-digit `WHERE` outside both the amplifier and the source ranges:

~~~text
*16*3*10S##     activate source device S
*16*3*1ES##     route the amplifiers of environment E to source S
~~~

`E` is the environment digit of the amplifier addressing above, and `S` the source identifier used by `101`-`109`. Environment `0` does not occur in this form, because `10S` is a source device address.

| Frame | Effect |
| --- | --- |
| `*16*3*112##` | environment 1 listens to source 2 |
| `*16*3*121##` | environment 2 listens to source 1 |
| `*16*3*181##` | environment 8 listens to source 1 |

Routing is announced per environment, so every amplifier sharing an environment follows the change. Two amplifiers in one environment cannot listen to different sources.

Wall controls observed on one plant release the outgoing source with `*16*13*10S##` before routing; the routing frame alone was sufficient on the other. A routed environment reports the status of its amplifiers in response.

**Confidence: corroborated**, from captures on two installations (MH200 and MH200N, both with F441M), a controlled source change on one of them, and the `WHO 22` counterparts on the other. It is not published in [`WHO 16`](../../sources/openwebnet-public/pdf/WHO_16.pdf). The evidence path, competing reading, and open questions are recorded in [Sound Matrix Source Routing](../../reverse-engineering/sound-matrix-routing.md). Base-band installations, the `#E` environment form, and sources above 4 are untested.

## `DIMENSION` values

| `DIMENSION` | Meaning | Established detail |
| ---: | --- | --- |
| `1` | Volume | `0..31`; readable/reportable/writable |
| `2` | High tones | listed in the global table |
| `3` | Low tones | listed in the global table |
| `4` | Balance | listed in the global table |
| `5` | State | request returns ordinary `WHAT` state frames |
| `6` | Frequency | six decimal digits, expressed in kHz by the examples (`107000` = 107.00 MHz) |
| `7` | Stored station / track | station write range `1..5` |
| `8` | RDS | eight ASCII character codes as separate values |
| `9` | Frequency plus station/track | listed in the global table |
| `10` | Memorized station | station range `1..5` |

The source gives complete flows only for a subset. Do not invent payloads for table-only `DIMENSION` values `2`, `3`, `4`, or `9`.

## Volume

~~~text
*#16*WHERE*1##
*#16*AMPLIFIER*1*VOLUME##
*#16*WHERE*#1*VOLUME##
~~~

General or environment reads can return one response for each active amplifier, followed by a terminating acknowledgement.

## State

`*#16*WHERE*5##` returns ordinary `*16*WHAT*WHERE##` frames. Collective requests can expand to individual active amplifiers or sources. State is therefore a result sequence, not necessarily a scalar `DIMENSION 5` response.

## Frequency, station, and RDS

Frequency request/write:

~~~text
*#16*SOURCE*6##
*#16*SOURCE*6*0*FREQUENCY##
*#16*SOURCE*#6*0*FREQUENCY##
~~~

Stored station request/write uses `DIMENSION 7`; memorized-station write uses `DIMENSION 10`. A frequency or station change can additionally emit RDS (`DIMENSION 8`) when available.

RDS text is carried as eight separate decimal ASCII codes, not as literal characters. For example, the source encodes an eight-character label as eight `*`-separated values.

## Direction and capability

Relative `WHAT` operations and absolute `DIMENSION` values are complementary. Do not reconstruct authoritative volume, tone, or frequency state solely by counting relative commands when a corresponding report is available.

Support is target-dependent: amplifier addresses accept amplifier operations; source addresses accept source/tuner operations. A namespace-level identifier does not imply applicability to both.

## Relationship to `WHO 22`

`WHO 16` and [`WHO 22`](../who-22-sound-diffusion/) encode similar concepts using different commands, addresses, and properties. They are separate dialects and must not be translated by numeric coincidence.

One MH200N was observed emitting a `WHO 22` counterpart for every `WHO 16` sound event it reported, including amplifier power, volume, source power, routing and RDS. That correspondence is established for that Device and was used to corroborate the addressing above; it does not establish a general mapping, and an MH200 on another plant emitted no `WHO 22` frames at all. The observed pairs are tabulated in [Sound Matrix Source Routing](../../reverse-engineering/sound-matrix-routing.md).

## Evidence basis

Tables, ranges, and flows come from [`WHO 16` specification](../../sources/openwebnet-public/pdf/WHO_16.pdf). Where the global table lists a property without a detailed allowed-message flow, this page says so explicitly.

The amplifier address structure and the matrix routing form are not in that specification. They come from captures on two independent installations and are marked with their confidence where they appear; [Sound Matrix Source Routing](../../reverse-engineering/sound-matrix-routing.md) holds the claim records.

See the [functional overview](../) for navigation by `WHO` and by function, and [Protocol](../../protocol/) for common frame and session syntax.
