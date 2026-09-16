# Protocol Reference

`WHO 22` models Sound Diffusion using explicit source, speaker, area and general target forms. It includes amplifier power, source selection, tuner and track navigation, RDS, tone/balance adjustment, presets and absolute `DIMENSION` state.

## `WHAT`

| `WHAT` | Meaning |
| ---: | --- |
| `0` | Turn off |
| `1` | Turn on |
| `2` | Source turned on |
| `3` | Increase volume |
| `4` | Decrease volume |
| `5` | Automatic tuner search toward higher frequencies |
| `6` | Manual tuner search toward lower frequencies |
| `9` / `10` | Next / previous station |
| `11` / `12` | Next / previous track |
| `22` | Sliding request |
| `31` / `32` | Start / stop RDS message |
| `33` | Store tuned frequency as a station |
| `34` | Turn on amplifier using Follow Me |
| `35` | Turn on amplifier to a specified source |
| `36` / `37` | Increment / decrement low tones |
| `38` / `39` | Increment / decrement mid tones |
| `40` / `41` | Increment / decrement high tones |
| `42` / `43` | Increment / decrement balance |
| `55` / `56` | Next / previous preset |

Paired values are directional operations. They should remain explicit in an implementation because station, track, tone and balance navigation are semantically different even where their interaction pattern is similar.

## `WHERE`

| Target | `WHERE` form |
| --- | --- |
| Source | `2#sourceID` |
| Speaker | `3#area#point` |
| Speaker area | `4#area` |
| General | `5#sender_address` |
| All sources | `6` |

The first component identifies the target class. `3#area#point` is therefore not a numeric address with separators removed: it is a structured speaker address. Area commands and individual-speaker commands must remain distinct.

## `DIMENSION`

| `DIMENSION` | Meaning |
| ---: | --- |
| `1` | Volume |
| `2` | High tones |
| `3` | Medium tones |
| `4` | Low tones |
| `5` | Frequency |
| `6` | Track / station |
| `7` | Play status |
| `11` | Frequency and station |
| `12` | Device state |
| `17` | Balance |
| `18` | 3D |
| `19` | Preset |
| `20` | Loudness |

These `DIMENSION` operations provide absolute or structured state alongside the relative command vocabulary. A state cache should therefore use `DIMENSION` responses where available instead of attempting to reconstruct absolute values solely by counting increment/decrement events.

## Source selection and Follow Me

`WHAT 35` explicitly turns an amplifier on using a specified source, while `WHAT 34` uses Follow Me behavior. These operations encode routing intent in addition to power state. Likewise `WHAT 2` reports source-on state and should not be reduced to a generic amplifier ON event.

## Tuner, media and RDS

The namespace supports both tuner-oriented station/frequency operations and track-oriented media navigation. The target class and active source determine which interpretation is applicable. RDS start/stop and RDS-related `DIMENSION` data are source functions and should remain associated with the source rather than a speaker endpoint.

`WHO 22` is a separate protocol dialect from [`WHO 16`](../who-16-sound-system/); numeric values and address forms must not be translated between them by number alone.