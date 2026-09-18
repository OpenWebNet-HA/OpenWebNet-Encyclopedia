# `WHO 3` Protocol Reference

`WHO 3` is the published Power/Load Management namespace. It controls load-shedding priority states and reports measurements from the load-management control unit.

It predates and remains distinct from the richer Energy Management model in `WHO 18`.

## `WHAT` values

| `WHAT` | Meaning |
| ---: | --- |
| `0` | Load disabled |
| `1` | Load enabled |
| `2` | Load forced |
| `3` | Remove forcing |

The public command flow explicitly defines `WHAT 2` as a force command. All four values can appear as monitor/event status for a priority target.

## `WHERE` values

| Target | `WHERE` |
| --- | --- |
| General | `0` |
| Control unit / measurement target | `10` |
| Load priority | `#1`–`#8` |

The leading `#` is part of a priority address. A priority must not be normalized to bare decimal `1`–`8`.

## Load forcing

~~~text
*3*2*#PRIORITY##
~~~

The gateway answers with `ACK` if the command is forwarded to the bus or `NACK` if it is not. The same functional frame can appear on the event session as the resulting forced state.

## Status requests

General request:

~~~text
*#3*0##
~~~

The server returns one status frame for each priority, followed by a terminating acknowledgement:

~~~text
*3*STATE*#PRIORITY##
...
*#*1##
~~~

A single-priority request uses the corresponding `#PRIORITY` as `WHERE`:

~~~text
*#3*#PRIORITY##
~~~

The published text is typographically degraded in places, but the surrounding tables and repeated examples consistently establish general `0` and priority `#1`–`#8` targets.

## Measurement `DIMENSION` values

Measurements address the control unit with `WHERE=10`.

| `DIMENSION` | Meaning | Unit stated by the source |
| ---: | --- | --- |
| `0` | All measurements | ordered voltage, current, power, energy |
| `1` | Voltage | volt |
| `2` | Current | ampere |
| `3` | Power | watt |
| `4` | Energy | not specified in the source |

Request/response forms are:

~~~text
*#3*10*0##
*#3*10*0*VOLTAGE*CURRENT*POWER*ENERGY##

*#3*10*1##
*#3*10*1*VOLTAGE##
~~~

`DIMENSION 2`, `3`, and `4` use the same pattern. Successful command-session responses terminate with `ACK`; the report form can also appear on the event session.

The source does not define numeric scaling, signedness, precision, or the energy unit. Preserve raw values when those details are not established by Device evidence.

## Relationship to `WHO 18`

`WHO 3` provides priority-based load state and four basic measurements. `WHO 18` defines later Energy Management families, address forms, totalizers, histories, automatic updates, Stop&Go state, and actuator operations. Similar physical subject matter does not make their `WHAT`, `WHERE`, or `DIMENSION` identifiers interchangeable.

## Evidence basis

The value tables and frame flows come from [`WHO_3.pdf`](../../sources/openwebnet-public/pdf/WHO_3.pdf), version 1.0.0. The PDF's embedded text encoding is damaged, so this page was checked against rendered pages as well as extracted text. Ambiguous typography has not been used to invent additional ranges or units.
