# `WHAT` Reference

`WHAT` in `WHO 2` expresses automation movement commands and states.

| `WHAT` | Meaning |
| ---: | --- |
| `0` | STOP |
| `1` | UP |
| `2` | DOWN |
| `10`–`12` | Advanced movement operations |
| `13` | Step operation supported by MyHOME Suite 3.5.38 |
| `14` | Step operation supported by MyHOME Suite 3.5.38 |

Ordinary command/status frames use `*2*WHAT*WHERE##`. The exact semantics and parameters of advanced operations remain scoped to `WHO 2`.