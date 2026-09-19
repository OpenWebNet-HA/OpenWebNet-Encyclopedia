# Programming `WHAT` Reference

Programming `WHAT` values control session entry, reset, transfer completion, acceptance, abort, and close. Their meaning is scoped to the active management `WHO` and programming sequence.

## Canonical values

| `WHAT` | Direction | Frame | Meaning | Canonical use |
| ---: | --- | --- | --- | --- |
| `1` | programmer → Device | `*[WHO]*1*[WHERE]##` | start programming by address | address and local-interaction entry |
| `2` | programmer → Device | `*[WHO]*2*0##` | end programming session | `CloseConf` |
| `3` | either direction | `*[WHO]*3*0##` | abort programming | abort/error path |
| `4` | Device → programmer | `*[WHO]*4*[WHERE_FAKE]##` | end Device transmission | entry and virtual transfer |
| `4` | programmer → Device | `*[WHO]*4*0##` | end programmer transfer | mandatory end of `ConfKO` payload |
| `9` | programmer → Device | `*[WHO]*9#[ID]*0##` | start programming by Device ID | ID-selected entry |
| `14` | programmer → Device | `*[WHO]*14#0*0##` | reset all Objects | mandatory start of `ConfKO` |
| `14` | programmer → Device | `*[WHO]*14#[SLOT]*0##` | reset one Object slot | registered, not in canonical `ConfKO` |
| `51` | Device → programmer | `*[WHO]*51*[WHERE_FAKE]##` | wrong configuration | fatal transfer result |
| `52` | Device → programmer | `*[WHO]*52*[WHERE_FAKE]##` | configuration accepted | advanced-transfer result |

`OPEN.db` also registers `*[WHO]*1*0##` as a general programming start, `*[WHO]*7*0##` as deleting stored configuration, and `WHERE = 0` variants of `WHAT 51` and `52`. They are not members of the three canonical programming scenarios and must not be inserted into those flows without independent evidence.

## `WHAT 1`: start by address

The addressed and local-interaction entry sequences use the same frame. Their timer policy distinguishes the canonical scenarios: 15 seconds for addressed selection and 300 seconds for local interaction.

The target `WHERE` follows the selected management family's address rules.

## `WHAT 9`: start by Device ID

`ID` has the database range `0..4294967295`. It identifies the installed Device instance and must not be replaced by a catalogue identifier.

## `WHAT 14`: reset Object configuration

Reset-all precedes every canonical `ConfKO` payload. It indicates replacement-style advanced configuration. The registered one-slot variant is not used by that sequence.

## `WHAT 4`: two directions

The two `WHAT 4` frames have different roles:

- Device `*[WHO]*4*[WHERE_FAKE]##` terminates the Device's current response stream.
- Programmer `*[WHO]*4*0##` declares the end of advanced Object writes and prompts the final result.

Do not normalize them into one directionless marker.

## `WHAT 51` and `52`

`WHAT 51` is an error and stops the advanced-transfer timer. `WHAT 52` stops that timer and starts the three-second acceptance wait before outer session close.

`ConfConfigurators` includes `WHAT 51` but not `WHAT 52`; its positive path ends through configurator reports and Device `WHAT 4`.

## `WHAT 2` and `3`

`WHAT 2` closes the outer programming session and stops `ConfTimeOut`.

`WHAT 3` is stored twice in `OPEN.db` with opposite directions. `OpenQuery.txt` explicitly loads the programmer abort frame. Direction and active session state determine whether the programmer or Device initiated termination.

## Namespace boundary

Equal `WHAT` values in diagnostics or functional control are independent. Diagnostic `WHAT 4` is also an end marker, but its lifecycle must not be substituted for the programming state machine solely because the number matches.
