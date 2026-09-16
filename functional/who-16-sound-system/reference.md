# Protocol Reference

`WHO 16` combines amplifier control, source selection, tuner navigation and audio parameters. The numeric structure of several `WHAT` families encodes both an operation and a magnitude, so clients should preserve the full value rather than normalize it to a bare action.

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

The `100x`/`110x`, `200x`/`210x`, `500x`/`510x`, and `600x`/`610x` ranges are parameterized command families encoded directly in `WHAT`. Their final digits carry the step magnitude.

## `WHERE`

| `WHERE` | Meaning |
| --- | --- |
| `0` | General amplifiers |
| `#0`–`#9` | Amplifiers in environment 0–9 |
| `01`–`99` | Individual amplifier |
| `100` | General source |
| `101`–`109` | Source 1–9 |

Amplifier and source targets occupy different ranges in the same namespace. Leading zeroes on individual-amplifier addresses are therefore significant protocol syntax.

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

`DIMENSION` operations expose absolute/structured sound-system information that complements relative `WHAT` operations. For example, a volume increment command and a volume `DIMENSION` value are different representations and should not be conflated.

## Source and amplifier state

ON/OFF, source cycling, sleep and Follow Me operations carry base-band/stereo-channel variants. Source-busy and RDS values are source-side state/event functions rather than amplifier-volume commands.

`WHO 16` is a distinct sound-system dialect from [`WHO 22`](../who-22-sound-diffusion/). Similar concepts such as volume, source and frequency have different `WHAT`, `WHERE`, and `DIMENSION` encodings in the two namespaces.