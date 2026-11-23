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

The historical touchscreen's calendar-based setters send three frames in order: select the return program, write the end date with `DIMENSION 30`, then write the end time with `DIMENSION 31`. For daily holiday mode, the first payload is `315#PROGRAM`; for vacation mode, it is `33002#PROGRAM`. The vacation setter uses two days as a dummy value before supplying the explicit deadline. This [tested client sequence](../../project/review/myopencommunity-hvac-history-review.md#calendar-mode-sequences) does not establish a two-day minimum or a Firmware timing requirement.

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

For the manual setpoint operation, `T` is a four-digit temperature value in `0050..0400` with 0.5 °C steps. `M` identifies the operating context: `1` heating, `2` conditioning, `3` generic.

A successful command-session submission is acknowledged with `ACK`; failure to submit the command to the bus is reported with `NACK`.

See [Addressing](addressing.md) for probe, zone and central-unit `WHERE` forms and [`DIMENSION` Reference](dimensions.md) for temperature/status payloads.

## Four-zone central-unit (`4695`) `WHAT` behavior

Inspection of BTicino four-zone central-unit `4695` (`HC/HS/L/N/NT4695`, `AM5875`) Firmware `01.01.03` (`LH4695_AM5875_010103.fwz`) alongside 13 gateway Firmwares establishes how `WHAT` commands and events behave on `#0#C` (`C = 1..99`, preserved on Generation B, C, and D gateways; collapsed to `00` and ignored on Generation A `MH200` `020102` and `H4684` `020054`). See the [four-zone central-unit evidence review](../../project/review/who4-4695-four-zone-central-unit.md).

| OpenWebNet `WHAT` on `#0#C` | Gateway SCS bus payload (Gen B/C/D) | `4695` Firmware `01.01.03` behavior | Resulting `#0#C` bus broadcast (`C0`) |
| --- | --- | --- | --- |
| `303` | `$18 D1 <CU> 03 02 C1 06 00 00` | Accepted in both Heating and Cooling seasons; sets unit to `OFF` | `*4*103*#0#C##` (`C0 16 00`) in Heating; `*4*203*#0#C##` (`C0 26 00`) in Cooling |
| `103` / `203` | `$18 D1 <CU> 03 02 C1 16/26 00 00` | `103` accepted only in Heating; `203` accepted only in Cooling; silently dropped on season mismatch (`NACK` on Gen A) | `*4*103*#0#C##` or `*4*203*#0#C##` when matched; silent (`TX=[]`) on mismatch |
| `302` | `$18 D1 <CU> 03 02 C1 07 00 00` | Accepted in both seasons; sets unit to Protection | `*4*102*#0#C##` (`C0 17 00`) in Heating; `*4*202*#0#C##` (`C0 27 00`) in Cooling |
| `102` / `202` | `$18 D1 <CU> 03 02 C1 17/27 00 00` | `102` accepted only in Heating; `202` accepted only in Cooling; silently dropped on season mismatch | `*4*102*#0#C##` or `*4*202*#0#C##` when matched; silent (`TX=[]`) on mismatch |
| `3101..3103` | `$18 D1 <CU> 03 02 C1 01 00..02 00` | Accepted in both seasons; activates weekly program `P` (`1..3`, encoded `00..02`) | `*4*110P*#0#C##` in Heating; `*4*210P*#0#C##` in Cooling |
| `1101..1103` / `2101..2103` | `$18 D1 <CU> 03 02 C1 11/21 00..02 00` | `1101..1103` accepted only in Heating; `2101..2103` accepted only in Cooling; silently dropped on season mismatch | `*4*110P*#0#C##` or `*4*210P*#0#C##` when matched; silent (`TX=[]`) on mismatch |
| `3100` | `$18 D1 <CU> 03 02 C1 01 FF 00` | Accepted in both seasons; resumes the stored active weekly program `P` (`1..3`) without changing program number | `*4*110P*#0#C##` in Heating; `*4*210P*#0#C##` in Cooling |
| `1` (Heating) / `0` (Cooling) | `$18 D1 <CU> 03 02 C1 F0/F1 00 00` | Same season: immediate no-op (`OFF` and active mode remain unchanged). Cross-season: switches season and enters Protection (`NACK` on Gen A) | Silent (`TX=[]`) on same season; `*4*102*#0#C##` (`C0 17 00`) or `*4*202*#0#C##` (`C0 27 00`) on season change |
| `311` | `$18 D1 <CU> 03 02 C2 00 00 00` | Dropped (`B4=0xC2` write unimplemented; `NACK` on Gen A); `111` and `211` on `#0#C` are `NACK`ed by gateways | Silent (`TX=[]`) |
| `1201..1216`, `2201..2216`, `3201..3216`, `3200` | `$18 D1 <CU> 03 02 C1 13/23/03 ...` | Dropped (`B5` low nibble `0x03` unimplemented in `4695` `01.01.03`) | Silent (`TX=[]`) |
| `115#PROGRAM`, `215#PROGRAM`, `315#PROGRAM` | `$18 D1 <CU> 03 02 C1 14/24/04 00..02 00` | Selects `4695` scenario `1..3` (`B5` low nibble `0x04`, encoded `00..02`, subject to `14`/`24` season filter) | `*4*115#110S*#0#C##` in Heating; `*4*215#210S*#0#C##` in Cooling (`#S*#0##` on Gen A) |
| `13DDD#P` .. `33DDD#P`, `3000`, `3000#P` | `$18 D1 <CU> 03 02 C1 15/25/05 <DDD> <00..02/FF>` (`B6=00` on `3000` / `3000#P`) | `B6 >= 01` with `B7 = 00..02` enters multi-day vacation (subject to `15`/`25` season filter); `B6 = 00` while in vacation exits back to weekly program `1..3` | `*4*13DDD*#0#C##` (`C0 15 <days>`) or `*4*23DDD*#0#C##` (`C0 25 <days>`); `*4*110P/210P*#0#C##` on exit |
| `110#TTTT`, `210#TTTT`, `310#TTTT` | Rejected (`NACK`, `TX=[]`) | Event/status report encoding only; all 13 gateways reject client-sent `110#TTTT`..`310#TTTT` commands | Emitted inbound by gateways from `C0 12/22 <T*2>` manual-mode broadcasts |

**`WHAT 3100` active weekly-program resume.** All 13 inspected gateways translate `*4*3100*#0#C##` (`*4*3100*#0##` on Generation A) to `$18 D1 <CU> 03 02 C1 01 FF 00` (`B5=0x01, B6=0xFF`). On Generation B, C, and D gateways where `<CU>` is preserved, `4695` Firmware `01.01.03` handles `B5=0x01, B6=0xFF` by keeping its stored program index (`1..3`) and switching operating state back to weekly-program execution, broadcasting `*4*110P*#0#C##` or `*4*210P*#0#C##`. By contrast, `*4*311*#0#C##` emits `B4=0xC2`, which `4695` Firmware `01.01.03` ignores.

**Season commands (`WHAT 1` and `WHAT 0`) on `#0#C`.** In `4695` Firmware `01.01.03`, `*4*1*#0#C##` (`C1 F0 00`) and `*4*0*#0#C##` (`C1 F1 00`) compare the requested season against the active season first: if the unit is already in the requested season, the handler exits with zero SCS transmissions and leaves an `OFF` unit (`103`/`203`) in `OFF`. When the season changes, `4695` Firmware `01.01.03` transitions into Protection (`*4*102*#0#C##` or `*4*202*#0#C##`) rather than Manual or Weekly Program; a client commanding a season switch followed by manual or programmed operation must therefore follow the season command with a season-agnostic manual write (`*#4*#0#C*#14*T*3##`) or program command (`*4*3100*#0#C##` or `*4*3101..3103*#0#C##`).

**Backup-battery load test (`WHAT 31`).** `4695` Firmware `01.01.03` periodically load-tests its backup battery through an internal 10-bit ADC channel and sets bit `2` (`0x04`) of `C0` status byte `B7` when the battery voltage falls below threshold. Generation B, C, and D gateways translate `C0` `B7` bit `2` into an inbound `*4*31*#0#C##` frame (`*4*31*#0##` on Generation A) accompanying the operating-state frame.
