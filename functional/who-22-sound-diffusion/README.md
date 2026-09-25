# `WHO 22` - Sound Diffusion

`WHO 22` is the later Sound Diffusion / Multimedia dialect. It uses structured source, speaker, area, and general addresses, with operation parameters embedded in `WHAT`.

## Core parameters

| Parameter | Published domain |
| --- | --- |
| Multimedia type | `1` voice; `2` right; `3` left; `4` stereo; `11` all sources |
| Source ID | `1..4` |
| Area / speaker point | `1..9` |
| Device state | `0` OFF; `1` ON |
| Frequency step | `1..15` |
| Modulation | `1` FM; `2` AM-LW; `3` AM-MW; `4` AM-SW |
| Stored station | `1..5` for F500; `1..15` for F500N |
| Track | `1..999` |
| Volume / volume step | absolute `0..31`; step `1..31` |
| Tone / balance value | `1..63` |
| 3D level | `0..10` |
| Loudness | `0` OFF; `1` ON |
| Preset | `2` normal, `3` dance, `4` pop, `5` rock, `6` classic, `7` techno, `8` party, `9` soft, `10` full bass, `11` full treble; `16..25` user defined |

The source describes frequency steps as `50`, `100`, … `750 Hz`; this appears unusually small for radio tuning. This reference preserves the published values without silently relabelling their unit.

## `WHAT`

| `WHAT` | Meaning |
| ---: | --- |
| `0` / `1` | Turn source or speaker OFF / ON |
| `2` | Source turned on |
| `3` / `4` | Increase / decrease volume |
| `5` / `6` | Search/tune toward higher / lower frequencies |
| `9` / `10` | Next / previous station |
| `11` / `12` | Next / previous track |
| `22` | Sliding request |
| `31` / `32` | Start / stop RDS message reporting |
| `33` | Store tuned frequency as a station |
| `34` | Turn amplifier ON using Follow Me |
| `35` | Turn amplifier ON using a specified source |
| `36` / `37` | Increment / decrement low tones |
| `38` / `39` | Increment / decrement mid tones |
| `40` / `41` | Increment / decrement high tones |
| `42` / `43` | Move balance right / left |
| `55` / `56` | Next / previous preset |

Most commands are parameterized. For example, source power uses `WHAT#MULTIMEDIA_TYPE#AREA`, while the target source remains in `WHERE`. A decoder must retain the entire `WHAT` field.

### Frequency search

For `WHAT 5` and `6`, an empty step parameter requests automatic search; a supplied frequency-step value requests movement by that step. The flat `WHAT` table's wording for `6` is therefore incomplete by itself; the allowed-message flow establishes both modes.

## `WHERE`

| Target | `WHERE` form |
| --- | --- |
| Source | `2#SOURCE_ID` |
| Speaker | `3#AREA#POINT` |
| Speaker area | `4#AREA` |
| General | `5#SENDER_ADDRESS` |
| All sources | `6` |

These are tagged target classes, not decimal numbers with punctuation. Keep the structure intact.

## `DIMENSION`

| `DIMENSION` | Meaning |
| ---: | --- |
| `1` | Volume |
| `2` | High tones |
| `3` | Medium tones |
| `4` | Low tones |
| `5` | Frequency |
| `6` | Track/station |
| `7` | Play status |
| `11` | Frequency and station |
| `12` | Device state |
| `17` | Balance |
| `18` | 3D |
| `19` | Preset |
| `20` | Loudness |

Absolute `DIMENSION` state complements relative `WHAT` operations. Prefer reported values for state caches instead of reconstructing state from increments.

### Payloads and concrete operations

| Dimension | Report payload following the dimension |
| --- | --- |
| `1` | `VOLUME` |
| `2`, `3`, `4` | `TONE_VALUE` |
| `5` | `MODULATION*FREQUENCY` |
| `6` | `STATION_OR_TRACK` |
| `11` | `MODULATION*FREQUENCY*STATION_OR_TRACK` |
| `12` | `DEVICE_STATE*MULTIMEDIA_TYPE` |
| `17` | `BALANCE` |
| `18` | `3D_LEVEL` |
| `19` | `PRESET` |
| `20` | `LOUDNESS` |

The detailed flows additionally show RDS text under dimension `10` and equalizer reports under `21#1`, `21#2`, and `21#3`. The equalizer selectors carry bands `1..3`, `4..6`, and `7..8` respectively, separated by `*`. The source does not supply a complete RDS text encoding or band-value domain.

Examples with unambiguous separators in the detailed flows include:

| Operation | Frame |
| --- | --- |
| Increase speaker volume | `*22*3#VOLUME_STEP*3#AREA#POINT##` |
| Decrease speaker volume | `*22*4#VOLUME_STEP*3#AREA#POINT##` |
| Follow Me | `*22*34#MULTIMEDIA_TYPE#AREA*3#AREA#POINT##` |
| Select source and turn on speaker | `*22*35#4#AREA#SOURCE_ID*3#AREA#POINT##` |
| Store tuned station | `*22*33#STATION*2#SOURCE_ID##` |
| Request source frequency | `*#22*5#2#SOURCE_ID*5##` |
| Request speaker volume | `*#22*3#AREA#POINT*1##` |
| Set speaker balance | `*#22*3#AREA#POINT*#17*BALANCE##` |
| Set speaker preset | `*#22*3#AREA#POINT*#19*PRESET##` |
| Set speaker loudness | `*#22*3#AREA#POINT*#20*LOUDNESS##` |

Source dimension requests use the general-source form `5#2#SOURCE_ID` in these flows; some responses instead use `2#SOURCE_ID`. Retain the reported address rather than requiring textual equality with the request. Status requests receive an action-session ACK while the specified state reports appear on the event session; dimension reads have their own response flows.

### Published inconsistencies

The detailed specification is not uniformly reliable as a copy-and-send frame catalogue. Speaker power examples omit separators that appear in the address table; speaker writes for dimensions `1..4` join the dimension marker to `WHERE` without the normal `*`; preset commands `55`/`56` contain an early `##`; and some tone-response dimension numbers disagree with the requested tone. RDS commands `31`/`32` are printed without a normal `WHERE` field. The source also shows `WHAT 21` source notifications outside its summary table.

Preserve these as source discrepancies. The ordinary frame grammar suggests possible corrections, but captures or implementation evidence are needed before treating a repaired frame as established. Occasional trailing empty fields in volume reports should be preserved by the parser. The compact tables above do not assert support for every read/write combination.

## Source and speaker semantics

Source commands and reports use source addresses; volume/tone/balance operations generally apply to speaker endpoints or areas. `WHAT 35` carries routing intent by selecting a source while turning an amplifier on. Follow Me (`WHAT 34`) is a separate operation and should not be normalized to ordinary ON.

The same namespace includes tuner, media-track, presets, RDS, and equalization. Interpretation depends on the selected source and target class.

## Relationship to `WHO 16`

[`WHO 16`](../who-16-sound-system/) represents a different sound dialect. Similar terms do not imply compatible numeric values, address forms, or parameter layouts.

One MH200N was observed reporting every sound event in both dialects. In those captures the `WHO 22` frame states as separate fields what `WHO 16` packs into one address:

| `WHO 16` | `WHO 22` counterpart | `WHO 22` fields |
| --- | --- | --- |
| `*16*3*11##` | `*#22*3#1#1*12*1*4##` | speaker area 1, point 1; state ON, stereo |
| `*16*3*12##` | `*#22*3#1#2*12*1*4##` | speaker area 1, point 2 |
| `*#16*11*1*17##` | `*#22*3#1#1*1*17##` | volume 17, same `0..31` scale |
| `*16*3*101##` | `*#22*2#1*12*1*4##` | source 1 active |
| `*16*3*112##` | `*22*2#4#1*5#2#2##` | area 1 selecting source 2 |
| `*#16*101*8*…##` | `*#22*5#2#1*10*…##` | RDS text, `DIMENSION 8` against `DIMENSION 10` |

This is **established for that Device** and was used to corroborate the `WHO 16` amplifier and routing addressing. It does not establish a general translation between the dialects: the value ranges, `WHAT` numbering and dimension indices differ, an MH200 on another plant emitted no `WHO 22` frames, and these captures cannot show whether the second dialect originates in the gateway or in another bus device. The claim record is in [Sound Matrix Source Routing](../../reverse-engineering/sound-matrix-routing.md).

## Evidence basis

Parameters, identifiers, and allowed-message distinctions come from [`WHO 22` specification](../../sources/openwebnet-public/pdf/WHO_22.pdf). Where its summary table and detailed flow differ, this page records the more specific flow and notes the discrepancy.

See the [functional overview](../) for navigation by `WHO` and by function, and [Protocol](../../protocol/) for common frame and session syntax.
