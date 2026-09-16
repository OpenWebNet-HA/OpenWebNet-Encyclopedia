# Overview

`WHO 18` defines the OpenWebNet Energy Management system. It covers energy measurement, accumulated consumption, historical series, Energy Management actuators, differential-current information, Stop&Go supervision, and automatic reporting of active power.

The namespace is heterogeneous: the selected `WHERE` identifies a device family, and the valid `WHAT` and `DIMENSION` operations depend on that family. A Stop&Go address, an energy meter/central unit address, and an Energy Management actuator address therefore cannot be treated as interchangeable numeric targets.

## Reference

| Subject | Page |
| --- | --- |
| Commands and command parameters | [`what.md`](what.md) |
| Device families and `WHERE` grammar | [`addressing.md`](addressing.md) |
| Measurements, totalizers, actuator state, Stop&Go and historical data | [`dimensions.md`](dimensions.md) |

## Device families

The published `WHO 18` model identifies three address families:

| Family | `WHERE` form | Published index range | Examples |
| --- | --- | ---: | --- |
| Stop&Go | `1N` | `N = 1–127` | Stop&Go protection/control devices |
| Energy measurement / central unit | `5N` | `N = 1–255` | F520, F523, 3522 and corresponding Legrand devices |
| Energy Management actuator | `7N#0` | `N = 1–255` | F522, F523 and corresponding Legrand devices |

See [`addressing.md`](addressing.md) for the implications of these forms.

## Operation classes

`WHO 18` uses all three principal functional frame patterns:

| Operation | General form |
| --- | --- |
| Command | `*18*WHAT*WHERE##` |
| `DIMENSION` request | `*#18*WHERE*DIMENSION##` |
| `DIMENSION` response/event | `*#18*WHERE*DIMENSION*VALUE...##` |
| `DIMENSION` setup/write | `*#18*WHERE*#DIMENSION...*VALUE...##` |

Several operations parameterize `WHAT` or `DIMENSION` using `#`. Those parameters are part of the operation grammar and must be preserved by parsers and encoders.

## Measurement model

Energy Management separates instantaneous values from accumulated and historical values. `DIMENSION 113` reports active power in watts. Totalizer operations expose accumulated values, while `DIMENSION 511`–`514` return time-series data for daily and monthly graphics. The published specification labels several accumulated values as “Watt”; where the frame description explicitly identifies energy since reset it uses Wh. Implementations should preserve the published field semantics rather than silently normalizing units from the identifier alone.

## Event model

Many `WHO 18` values can arrive both as direct responses and as events. Actuator state, totalizer state, differential-current level, active power, and Stop&Go status all have event forms. Clients maintaining state should therefore process `DIMENSION` events independently of whether they initiated the corresponding request.

Automatic active-power reporting is configured with `DIMENSION 1200`. Historical-series commands similarly cause a sequence of `DIMENSION 511`–`514` event frames rather than a single scalar response.

## Relationship to other energy systems

`WHO 18` is distinct from [`WHO 3`](../who-3-load-management/) Load Management and [`WHO 11`](../who-11-energy-distribution/) Energy Distribution. Their `WHAT`, `WHERE`, and `DIMENSION` namespaces are not interchangeable.

For common frame syntax, see [`../../protocol/`](../../protocol/).