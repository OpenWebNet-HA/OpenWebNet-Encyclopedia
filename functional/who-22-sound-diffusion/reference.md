# Protocol Reference

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
| `9` | Next station |
| `10` | Previous station |
| `11` | Next track |
| `12` | Previous track |
| `22` | Sliding request |
| `31` | Start RDS message |
| `32` | Stop RDS message |
| `33` | Store tuned frequency as a station |
| `34` | Turn on amplifier using Follow Me |
| `35` | Turn on amplifier to a specified source |
| `36` / `37` | Increment / decrement low tones |
| `38` / `39` | Increment / decrement mid tones |
| `40` / `41` | Increment / decrement high tones |
| `42` / `43` | Increment / decrement balance |
| `55` / `56` | Next / previous preset |

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

## `WHERE`

| Target | `WHERE` form |
| --- | --- |
| Source | `2#sourceID` |
| Speaker | `3#area#point` |
| Speaker area | `4#area` |
| General | `5#sender_address` |
| All sources | `6` |

`WHO 22` is a separate protocol dialect from [`WHO 16`](../who-16-sound-system/); their numeric values must not be merged.