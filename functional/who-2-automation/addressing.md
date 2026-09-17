# Addressing

`WHO 2` uses the SCS Automation addressing model. `WHERE` selects a general scope, environment, point-to-point light point, group, or a point reached through a local-bus interface.

## `WHERE` forms

| Scope | `WHERE` form | Values |
| --- | --- | --- |
| General | `0` | Entire Automation system |
| Environment | `A` | `00`, `1`–`9`, or `100` as defined by the published Automation grammar |
| Point to point | `APL` | Address ranges depend on `A` |
| Group | `#GR` | `GR = 1`–`255` |
| Local bus | `APL#4#INTERFACE` | `INTERFACE = [0-1][1-9]` |

## Point-to-point ranges

The published grammar constrains `PL` according to the `A` representation:

| `A` | Allowed `PL` |
| --- | --- |
| `00` | `01`–`15` |
| `1`–`9` | `1`–`9` |
| `10` | `01`–`15` |
| `01`–`09` | `10`–`15` |

These forms preserve significant leading zeroes. An Automation address should therefore be parsed according to the applicable grammar rather than converted to an integer before its address class is known.

## Event expansion

Commands addressed to a group, environment, or the general scope can produce event/status frames for the individual Automation Objects affected by the operation. A group command can additionally produce a frame retaining the group `WHERE` itself.

The MyHOME_Suite `OPEN.db` address-rule definitions represent the same `A`/`PL` address family through system-specific point-to-point, environment, and advanced rules.

See [`what.md`](what.md) for movement commands, [`dimensions.md`](dimensions.md) for advanced shutter state/position data, and [`../../protocol/addressing.md`](../../protocol/addressing.md) for the common system-scoped addressing model.