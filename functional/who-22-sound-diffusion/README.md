# `WHO 22` - Sound Diffusion

`WHO 22` is the later Sound Diffusion / Multimedia dialect. It uses structured source, speaker, area, and general addresses, with operation parameters embedded in `WHAT`.

## Core parameters

| Parameter | Published domain |
| --- | --- |
| Multimedia type | `1` voice; `2` right; `3` left; `4` stereo; `11` all sources |
| Source ID | `1`–`4` |
| Area / speaker point | `1`–`9` |
| Device state | `0` OFF; `1` ON |
| Frequency step | `1`–`15` |
| Modulation | `1` FM; `2` AM-LW; `3` AM-MW; `4` AM-SW |
| Stored station | `1`–`5` for F500; `1`–`15` for F500N |
| Track | `1`–`999` |
| Volume / volume step | absolute `0`–`31`; step `1`–`31` |
| Tone / balance value | `1`–`63` |
| 3D level | `0`–`10` |
| Loudness | `0` OFF; `1` ON |

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

## Source and speaker semantics

Source commands and reports use source addresses; volume/tone/balance operations generally apply to speaker endpoints or areas. `WHAT 35` carries routing intent by selecting a source while turning an amplifier on. Follow Me (`WHAT 34`) is a separate operation and should not be normalized to ordinary ON.

The same namespace includes tuner, media-track, presets, RDS, and equalization. Interpretation depends on the selected source and target class.

## Relationship to `WHO 16`

[`WHO 16`](../who-16-sound-system/) represents a different sound dialect. Similar terms do not imply compatible numeric values, address forms, or parameter layouts.

## Evidence basis

Parameters, identifiers, and allowed-message distinctions come from [`WHO_22.pdf`](../../sources/openwebnet-public/pdf/WHO_22.pdf). Where its summary table and detailed flow differ, this page records the more specific flow and notes the discrepancy.

See the [functional overview](../) for navigation by `WHO` and by function, and [`../../protocol/`](../../protocol/) for common frame and session syntax.
