# `WHAT` Reference

`WHAT` in `WHO 1` expresses lighting commands and states. Ordinary command and status frames use `*1*WHAT*WHERE##`; status requests use `*#1*WHERE##`.

## Switching and dimming

| `WHAT` | Meaning |
| ---: | --- |
| `0` | OFF |
| `1` | ON |
| `2` | 20% |
| `3` | 30% |
| `4` | 40% |
| `5` | 50% |
| `6` | 60% |
| `7` | 70% |
| `8` | 80% |
| `9` | 90% |
| `10` | 100% |
| `30` | Step up |
| `31` | Step down |

The discrete dimmer levels represented by `WHAT 2`–`10` are the protocol's ten-percent steps from 20% through 100%. Finer level control is provided by Lighting `DIMENSION` operations rather than by additional ordinary `WHAT` values.

## Timed operations

| `WHAT` | ON duration |
| ---: | --- |
| `11` | 1 minute |
| `12` | 2 minutes |
| `13` | 3 minutes |
| `14` | 4 minutes |
| `15` | 5 minutes |
| `16` | 15 minutes |
| `17` | 30 seconds |
| `18` | 0.5 seconds |

Timed commands switch the target ON for the duration encoded by the selected `WHAT`.

## Blinking operations

| `WHAT` | Blink period |
| ---: | --- |
| `20` | 0.5 seconds |
| `21` | 1 second |
| `22` | 1.5 seconds |
| `23` | 2 seconds |
| `24` | 2.5 seconds |
| `25` | 3 seconds |
| `26` | 3.5 seconds |
| `27` | 4 seconds |
| `28` | 4.5 seconds |
| `29` | 5 seconds |

These meanings are local to `WHO 1`; the same numeric `WHAT` values in another `WHO` do not inherit Lighting semantics.

See [`dimensions.md`](dimensions.md) for Lighting level, transition-speed, temporization, and operating-time `DIMENSION` values, and [`addressing.md`](addressing.md) for `WHERE` forms.