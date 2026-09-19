# Programming Session Lifecycle

`OPEN.db` models programming as a scenario composed from ordered sequences. The outer programming session and the inner transfer sequence have separate terminal frames and timers.

## Scenario composition

| Scenario | Entry | Transfer | Close |
| --- | --- | --- | --- |
| By address | `ConfAddressed` | `ConfConfigurators` | `CloseConf` |
| By Device ID | `ConfPoint2PointWithID` | repeated `ConfKO` | `CloseConf` |
| By local interaction | `ConfLocalButton` | repeated `ConfKO`, then `ConfConfigurators` | `CloseConf` |

A repeated `ConfKO` association means the scenario engine can invoke that sequence repeatedly. The database does not encode the application-level repetition count.

## Entry and initial projection

The entry sequence sends one mandatory start frame:

| Method | Frame |
| --- | --- |
| Address | `*[WHO]*1*[WHERE]##` |
| Device ID | `*[WHO]*9#[ID]*0##` |
| Local-interaction scenario | `*[WHO]*1*[WHERE]##` |

`ConfLocalButton` and `ConfAddressed` contain the same ordered frames. Their implementation difference is the first-response timer: the local-interaction sequence uses a 300-second window instead of the 15-second addressed/ID window. The frame still contains `WHERE`; `OPEN.db` does not explain how physical interaction and that value are coordinated.

After entry, the Device can report the same initial projection used by diagnostics:

1. `DIMENSION 1` identity;
2. firmware and hardware versions;
3. `DIMENSION 4` and `5` configurator values;
4. microcontroller version;
5. diagnostic bitmasks;
6. `DIMENSION 13` Device ID;
7. repeated `DIMENSION 30` Module/Object state;
8. repeated `DIMENSION 32` addresses;
9. repeated busy `DIMENSION 31` information;
10. `WHAT 4` end of transmission.

Only the start frame is marked mandatory. Collectors must tolerate omitted optional responses and repeated Module records.

## Transfer states

### Virtual-configurator transfer

`ConfConfigurators` requires `DIMENSION 4`, optionally writes `DIMENSION 5`, and accepts:

- `WHAT 51`: wrong configuration;
- `WHAT 3`: Device abort;
- echoed/reported `DIMENSION 4` and `5` values;
- Device `WHAT 4`: end of transmission.

The sequence does not include `WHAT 52`.

### Advanced Object transfer

`ConfKO` orders:

1. mandatory reset of all Objects;
2. mandatory repeated `DIMENSION 30` Object writes;
3. optional repeated `DIMENSION 32` address writes;
4. optional repeated `DIMENSION 35` parameter writes;
5. mandatory programmer `WHAT 4` end of transmission;
6. Device `WHAT 51` or `WHAT 52` result, applicable structured errors, or `WHAT 3` abort.

`AS_OPEN_SEQUENCE` contains no row with `open_order = 9` for `ConfKO`. Preserve the source numbering; do not invent a missing operation.

The error rows are alternatives associated with the active transfer. Their numeric `open_order` positions do not mean that an error can only be received after every earlier optional frame.

## Session close and abort

Normal close uses:

`*[WHO]*2*0##`

This is the sole mandatory member of `CloseConf`. Its stored timeout associations stop the ten-minute configuration timer and start the one-second scenario-close wait in the Suite sequence model; they do not prove Device-side commit or persistence.

Programmer abort and Device abort share:

`*[WHO]*3*0##`

`OPEN.db` stores separate rows distinguished by direction. The canonical programming sequences include the Device-to-programmer abort row; `OpenQuery.txt` separately loads the programmer abort together with diagnostic abort. Direction and active state are therefore required.

## Timing model

| Timer | Default | Role |
| --- | ---: | --- |
| `ConfTimeOut` | 600 s | maximum configuration session |
| `DeviceAnswerTimeOut` | 15 s | first identity response after address/ID start |
| `DeviceAnswerTimeOutByButton` | 300 s | first response in local-interaction programming |
| `DeviceMoreAnswerTimeOut` | 20 s | remaining initial information until Device `WHAT 4` |
| `DeviceAcceptTimeOut` | 2 s | virtual-configurator acceptance window |
| `DeviceKOTimeOut` | 50 s | advanced Object transfer |
| `CmdKoValueTimeWait` | 2 s | wait associated with Object writes |
| `KOAcceptTimeWait` | 3 s | wait after `WHAT 52` before scenario close |
| `CloseScenarioTimeWait` | 1 s | close-sequence wait |

These are MyHOME_Suite defaults, not wire-level constants.

## Completion classification

| Result | Evidence |
| --- | --- |
| Transfer accepted | expected Device terminal response for the active transfer |
| Transfer rejected | `WHAT 51` or fatal structured error |
| Warning | nonfatal structured error such as an unmanaged parameter |
| Aborted | `WHAT 3` from either participant |
| Timed out | an active timer expired without its stopping transition |
| Close sent | programmer transmitted `WHAT 2`; Device-side closure is not independently confirmed by transmission alone |
| Verified | a later diagnostic interview matches the intended effective state |

Closing a session does not change a rejection or timeout into success.
