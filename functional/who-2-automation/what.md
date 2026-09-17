# `WHAT` Reference

`WHAT` in `WHO 2` expresses Automation movement commands. The published Automation specification distinguishes base motor-actuator commands from advanced commands carrying movement-step and priority parameters.

## Base commands

| `WHAT` | Function | Frame |
| ---: | --- | --- |
| `0` | Stop | `*2*0*WHERE##` |
| `1` | Up | `*2*1*WHERE##` |
| `2` | Down | `*2*2*WHERE##` |

For group addressing, an event may be reported for the group and for the individual Automation Objects affected by the command. For environment and general addressing, status/event reporting may likewise expand to the affected Objects.

## Advanced commands

| `WHAT` | Function | Optional parameters |
| ---: | --- | --- |
| `10` | Stop advanced | shutter priority |
| `11` | Up advanced | shutter step; shutter priority |
| `12` | Down advanced | shutter step; shutter priority |

The advanced operations use `WHAT` parameters rather than assigning the complete operation to the numeric `WHAT` alone. Implementations must therefore preserve the parameterized form of the command.

### Shutter step

The shutter-step parameter is in the range `1`–`99`; `100` or an omitted/null step denotes the complete movement to the open or closed endpoint, according to direction. Values `1`–`99` denote movement by the corresponding amount.

### Priority

Advanced commands can carry a priority operation composed of a set/clear selector and three priority flags:

| Priority flag | Meaning |
| --- | --- |
| `p1` | Safety priority |
| `p2` | High priority |
| `p3` | Medium priority |

The selector determines whether the indicated priority bits are set or cleared. A zero bit leaves the corresponding priority unaffected. With no priority bits selected, the priority operation has no effect.

## Extended movement states

The Automation data model also represents the following advanced shutter states:

| Value | State |
| ---: | --- |
| `10` | Stop |
| `11` | Up |
| `12` | Down |
| `13` | Step-by-step up |
| `14` | Step-by-step down |

These values are used as shutter-status values in `DIMENSION 10`; they must not be interpreted as additional published command functions merely because they occupy the same numeric range. See [`dimensions.md`](dimensions.md).

See [`addressing.md`](addressing.md) for `WHERE` forms and [`../../protocol/what.md`](../../protocol/what.md) for the common `WHAT` model.