# `DIMENSION` Reference

| `DIMENSION` | Meaning |
| ---: | --- |
| `1` | Switch ON |
| `2` | Maximum lux |
| `3` | Maintained level |
| `4` | Automatic switch ON |
| `5` | Switch ON delay |
| `6` | Automatic switch OFF |
| `7` | Switch OFF delay |
| `8` | Delay timer |
| `9` | Stand-by timer |
| `10` | Stand-by value |
| `11` | OFF value |
| `12` | Slave offset (GAP) value |
| `17` | State: Automatic / Manual / Stop |
| `18` | Centralised lux value |

Writes use the `#DIMENSION` form, for example the published maintained-level operation follows `*#24*WHERE*#3*Maint_lev##`. Reads use the corresponding non-`#` `DIMENSION` form.