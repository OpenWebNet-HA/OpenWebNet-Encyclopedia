# `WHAT` Reference

`WHAT` in `WHO 1` expresses lighting commands and states.

| `WHAT` | Meaning |
| ---: | --- |
| `0` | OFF |
| `1` | ON |
| `2`–`10` | Lighting level |
| `11`–`18` | Timed operations |
| `20`–`29` | Blinking operations |
| `30` | Step up |
| `31` | Step down |

The exact interpretation of the timed and blinking values is defined by the Lighting system; they must not be generalized to other `WHO` namespaces.

Ordinary command/status frames use `*1*WHAT*WHERE##`. Status requests use `*#1*WHERE##`.