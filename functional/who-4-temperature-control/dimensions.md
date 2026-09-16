# `DIMENSION` Reference

Known Temperature Control `DIMENSION` identifiers include:

| `DIMENSION` | Meaning |
| ---: | --- |
| `0` | Measured temperature |
| `7` | Control/configuration operation represented in the MyHOME_Suite 3.5.38 protocol data |
| `11` | Fan speed |
| `12` | Complete probe status |
| `13` | Local setpoint offset |
| `14` | Setpoint |
| `19` | Valve status/control |
| `20` | Actuator status/control |
| `22` | Split-unit operation |
| `30` | Holiday end |

The MyHOME_Suite 3.5.38 protocol data defines `DIMENSION 7` command templates for Temperature Control functions. The corresponding parameter definitions represent temperatures from 3–40 °C in 0.5 °C steps where that parameter definition applies.

The value structure is `DIMENSION`-specific; values must not be normalized across identifiers merely because they represent temperatures or states.