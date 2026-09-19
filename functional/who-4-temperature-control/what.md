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
| `103` | OFF - heating |
| `203` | OFF - conditioning |
| `303` | OFF - generic |

Antifreeze is the heating-side protection state; thermal protection is the conditioning-side protection state. Generic forms are used where the operating mode is not specialized to heating or conditioning.

## Manual and programmed operation

| `WHAT` | Meaning |
| ---: | --- |
| `110` | Manual adjustment - heating |
| `210` | Manual adjustment - conditioning |
| `310` | Manual adjustment - generic |
| `111` | Programmed/automatic - heating |
| `211` | Programmed/automatic - conditioning |
| `311` | Programmed/automatic - generic |
| `115` | Daily holiday plan - heating |
| `215` | Daily holiday plan - conditioning |
| `315` | Daily holiday plan - generic |

A zone controlled through the central unit uses central-unit addressing; for example, automatic generic operation is commanded with `*4*311*#WHERE##` for the selected zone.

## Vacation, program and scenario forms

These operations target the central unit with `WHERE = #0`. The detailed flows on pages 29–52 establish the following values; the summary table on page 5 contains shifted/mismatched descriptions and must not override them.

| Operation | Heating | Conditioning | Generic/current context |
| --- | --- | --- | --- |
| Weekly program `1..3` | `1101..1103` | `2101..2103` | `3101..3103` |
| Restore last weekly program | - | - | `3100` |
| Scenario `1..16` | `1201..1216` | `2201..2216` | `3201..3216` |
| Restore last scenario | - | - | `3200` |
| Daily holiday plan, then return to program | `115#PROGRAM` | `215#PROGRAM` | `315#PROGRAM` |
| Vacation for `DDD` days, then return to program | `13DDD#PROGRAM` | `23DDD#PROGRAM` | `33DDD#PROGRAM` |
| Cancel vacation and choose weekly program | - | - | `3000#PROGRAM` |
| Cancel vacation and restore last weekly program | - | - | `3000` |

`DDD` is a three-digit day count. The summary table lists `000..999`, but the detailed command flows restrict it to `001..255`; use that narrower domain when encoding these documented commands. The vacation examples send `13002#3103`, `23002#3103`, or `33002#3103` for two days followed by weekly program 3. The source notes that the reported remaining period includes the current day, so its corresponding event examples report `13003`, `23003`, or `33003`; do not demand byte equality between the command and its event.

For daily holiday commands, the return-program parameter is `1101..1103` for heating, `2101..2103` for conditioning, and `3101..3103` for generic mode. The multi-day vacation commands use `3101..3103` in all three contexts. Daily-holiday event examples instead show the selected ordinal after `115#` or `215#`. Retain that command/report distinction. The deadline itself is set/read with [holiday date and time properties](dimensions.md#dimension-30---holiday-end).

Example: `*4*3102*#0##` selects weekly program 2 in the current thermal context. A reply/event can use the resolved heating or conditioning program code. An acknowledgement confirms submission, not that the requested mode was physically attained.

## Zone setup commands

Zone setup is performed through the central unit using `WHERE` forms `#1..#99`.

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

See [Addressing](addressing.md) for probe, zone and central-unit `WHERE` forms and [`DIMENSION` Reference](dimensions.md) for temperature/status payloads.
