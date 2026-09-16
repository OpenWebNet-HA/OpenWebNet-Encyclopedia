# `WHAT` Reference

`WHO 4` uses `WHAT` both for direct Temperature Control commands and for operating-state/event reporting. Several values encode the active heating/conditioning/generic mode together with the operating mode.

## Basic operating states

| `WHAT` | Meaning |
| ---: | --- |
| `0` | Conditioning mode |
| `1` | Heating mode |
| `20` | Remote control disabled |
| `21` | Remote control enabled |
| `22` | At least one probe OFF |
| `23` | At least one probe in antifreeze |
| `24` | At least one probe in manual mode |
| `30` | Failure detected |
| `31` | Central-unit battery fault |
| `40` | Release local probe adjustment |

## Protection and OFF states

| `WHAT` | Meaning |
| ---: | --- |
| `102` | Antifreeze |
| `202` | Thermal protection |
| `302` | Generic protection |
| `103` | OFF — heating |
| `203` | OFF — conditioning |
| `303` | OFF — generic |

Antifreeze is the heating-side protection state; thermal protection is the conditioning-side protection state. Generic forms are used where the operating mode is not specialized to heating or conditioning.

## Manual and programmed operation

| `WHAT` | Meaning |
| ---: | --- |
| `110` | Manual adjustment — heating |
| `210` | Manual adjustment — conditioning |
| `310` | Manual adjustment — generic |
| `111` | Programmed/automatic — heating |
| `211` | Programmed/automatic — conditioning |
| `311` | Programmed/automatic — generic |
| `115` | Daily holiday plan — heating |
| `215` | Daily holiday plan — conditioning |
| `315` | Daily holiday plan — generic |

A zone controlled through the central unit uses central-unit addressing; for example, automatic generic operation is commanded with `*4*311*#WHERE##` for the selected zone.

## Vacation, program and scenario forms

The central-unit protocol also uses parameterized `WHAT` families for vacation periods, weekly programs and scenarios. Their numeric encoding carries the selected heating/conditioning/generic context and, where applicable, a program, scenario or duration value. These forms are central-unit operations rather than ordinary probe commands.

The published protocol includes vacation periods up to 999 days, weekly-program selection, last-program restoration, scenario selection and last-scenario restoration. Holiday termination can additionally be controlled through `DIMENSION 30`; see [`dimensions.md`](dimensions.md).

## Zone setup commands

Zone setup is performed through the central unit using `WHERE` forms `#1`–`#99`.

| Operation | Frame form |
| --- | --- |
| Manual setpoint | `*#4*#WHERE*#14*T*M##` |
| Automatic/programmed mode | `*4*311*#WHERE##` |
| OFF | `*4*303*#WHERE##` |
| Antifreeze | `*4*102*#WHERE##` |
| Thermal protection | `*4*202*#WHERE##` |
| Generic protection | `*4*302*#WHERE##` |

For the manual setpoint operation, `T` is a four-digit temperature value from `0050` to `0400` in 0.5 °C steps. `M` identifies the operating context: `1` heating, `2` conditioning, `3` generic.

A successful command-session submission is acknowledged with `ACK`; failure to submit the command to the bus is reported with `NACK`.

See [`addressing.md`](addressing.md) for probe, zone and central-unit `WHERE` forms and [`dimensions.md`](dimensions.md) for temperature/status payloads.