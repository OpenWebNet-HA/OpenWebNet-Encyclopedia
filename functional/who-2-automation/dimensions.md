# `DIMENSION` Reference

Known Automation `DIMENSION` identifiers include:

| `DIMENSION` | Meaning |
| ---: | --- |
| `10` | Automation status / position information |
| `11` | Go to level / absolute position |

## Absolute position

MyHOME_Suite 3.5.38 uses the absolute-position form `*#2*WHERE*#11#001*LEVEL##`.

Known level semantics are:

| Level | Meaning |
| ---: | --- |
| `0` | Closed |
| `1`–`99` | Percentage position |
| `100` | Open |
| `255` | Unknown position |

The parameter attached to `DIMENSION 11` is part of the Automation-specific operation and must be preserved when encoding the frame.