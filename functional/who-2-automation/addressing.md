# Addressing

`WHO 2` uses the SCS Automation addressing model. `WHERE` selects a general scope, environment, point-to-point light point, group, or a point reached through a local-bus interface.

## `WHERE` forms

| Scope | `WHERE` form | Values |
| --- | --- | --- |
| General | `0` | Entire Automation system |
| Environment | `A` | `00`, `1..9`, or `100` as defined by the published Automation grammar |
| Point to point | `APL` | Address ranges depend on `A` |
| Group | `#GR` | `GR = 1..255` |
| Local bus | `APL#4#INTERFACE` | `INTERFACE = [0-1][1-9]` (`01..09`, `11..19`) |

## Point-to-point ranges

The published grammar constrains `PL` according to the `A` representation:

| `A` | Allowed `PL` |
| --- | --- |
| `00` | `01..15` |
| `1..9` | `1..9` |
| `10` | `01..15` |
| `01..09` | `10..15` |

These forms preserve significant leading zeroes. An Automation address should therefore be parsed according to the applicable grammar rather than converted to an integer before its address class is known. The published `WHO 2` table explicitly defines the local-bus form for point-to-point `APL`; its `interface` field is the same routing-interface concept called `Int` by the `WHO 1` specification. Unlike the `WHO 1` Lighting material, the published Automation table does not explicitly establish `#3` variants or local-bus General, Area, or Group forms. See the [canonical addressing reference](../../protocol/addressing.md#level-4--local-bus) for the cross-source distinction.

## Event expansion

Commands addressed to a group, environment, or the general scope can produce event/status frames for the individual Automation Objects affected by the operation. A group command can additionally produce a frame retaining the group `WHERE` itself.

The MyHOME_Suite `OPEN.db` address-rule definitions represent the same `A`/`PL` address family through system-specific point-to-point, environment, and advanced rules.

## Centralized transmitters and General scope

Centralized control devices configured with `A=GEN` target the General scope (`WHERE = 0`). In the referenced MyHomeServer1/LN4660M2 captures, the observed movement frame used the event-style form `*2*11#100#001#1*0##`.

Because OpenWebNet command frames carry only the target address rather than the originator address, frames with `WHERE = 0` do not identify which physical transmitter generated the command. In the [public MyHomeServer1/LN4660M2 traces](https://github.com/OpenWebNet-HA/MyHOME/tree/198a848e73edd2a887b993b98beffa98f3f20e36/tests/fixtures/traces/issue_445), the centralized operation was followed by individual point-to-point `DIMENSION 10` status reports from affected actuators on their respective `A`/`PL` addresses. Treat that telemetry sequence as observed behavior for the captured gateway/controller path rather than a universal requirement for every gateway implementation.

See [`WHAT` Reference](what.md) for movement commands, [`DIMENSION` Reference](dimensions.md) for advanced shutter state/position data, and [Addressing](../../protocol/addressing.md) for the common system-scoped addressing model.
