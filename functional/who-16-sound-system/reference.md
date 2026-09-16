# Protocol Reference

## `WHAT`

| `WHAT` | Meaning |
| ---: | --- |
| `0` | ON amplifier / base-band source |
| `3` | ON amplifier / stereo-channel source |
| `10` | OFF amplifier / base-band source |
| `13` | OFF amplifier / stereo-channel source |
| `20` | Source cycle, base band |
| `23` | Source cycle, stereo channel |
| `30` | Sleep on base band |
| `33` | Sleep on stereo channel |
| `40` | Sleep OFF |
| `50` | Follow me, base band |
| `53` | Follow me, stereo channel |
| `100` | Source busy |
| `101` | Start RDS transmission |
| `102` | Stop RDS transmission |
| `1001`–`1015` | Increase volume by 1–15 |
| `1101`–`1115` | Decrease volume by 1–15 |
| `2001`–`2015` | Increase high tones by 1–15 |
| `2101`–`2115` | Decrease high tones by 1–15 |
| `5000` | Find first free higher frequency |
| `5001`–`5015` | Increase frequency in 0.05 MHz steps |
| `5100` | Find first free lower frequency |
| `5101`–`5115` | Decrease frequency in 0.05 MHz steps |
| `6001`–`6015` | Advance radio station/track by 1–15 |
| `6101`–`6115` | Move back radio station/track by 1–15 |

## `WHERE`

| `WHERE` | Meaning |
| --- | --- |
| `0` | General amplifiers |
| `#0`–`#9` | Amplifiers in environment 0–9 |
| `01`–`99` | Individual amplifier |
| `100` | General source |
| `101`–`109` | Source 1–9 |

## `DIMENSION`

| `DIMENSION` | Meaning |
| ---: | --- |
| `1` | Volume |
| `2` | High tones |
| `3` | Low tones |
| `4` | Balance |
| `5` | State |
| `6` | Frequency |
| `7` | Radio station / track |
| `8` | RDS |
| `9` | Frequency + radio station / track |
| `10` | Radio station |

`WHO 16` is a distinct sound-system dialect from [`WHO 22`](../who-22-sound-diffusion/).