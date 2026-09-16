# `DIMENSION` Reference

Known Temperature Control `DIMENSION` identifiers include:

| `DIMENSION` | Meaning |
| ---: | --- |
| `0` | Measured temperature |
| `7` | Control/configuration operation used by MyHOME Suite 3.5.38 |
| `11` | Fan speed |
| `12` | Complete probe status |
| `13` | Local setpoint offset |
| `14` | Setpoint |
| `19` | Valve status/control |
| `20` | Actuator status/control |
| `22` | Split-unit operation |
| `30` | Holiday end |

MyHOME Suite 3.5.38 contains `DIMENSION 7` command templates used by its Temperature Control functions. Temperature parameters represented by the corresponding configuration templates use a supported range of 3–40 °C with 0.5 °C steps where that parameter definition applies.

The value structure is `DIMENSION`-specific; values must not be normalized across identifiers merely because they represent temperatures or states.