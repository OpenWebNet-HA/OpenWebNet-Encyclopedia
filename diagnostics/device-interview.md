# Device Interview

A Device interview reads the runtime diagnostic projection of one Physical Device. It can be started by Device ID, diagnostic address, or local interaction.

## Start and termination frames

| Operation | Frame |
| --- | --- |
| Start by Device ID | `*[WHO]*10#[ID]*0##` |
| Start by address | `*#[WHO]*[WHERE]*0##` |
| Start by local/general interaction | `*[WHO]*5*0##` |
| Device end marker | `*[WHO]*4*[WHERE_FAKE]##` |
| General end marker variant | `*[WHO]*4*0##` |
| Abort/close diagnosis | `*[WHO]*6*0##` |

`OPEN.db` uses `DiagAdvanced`/`DiagAID`, `DiagAddressed`, and `DiagLocalButton` for the three start modes. The Device ID form is preferred when discovery has already established the 32-bit instance identity.

`DiagAdvanced` is the point-to-point ID sequence. `DiagAID` uses the same start frame and response order as the repeated per-Device step in the `ScanByAID` scenario.

## Expected response groups

The canonical sequences order the following response families:

| Order | `DIMENSION` | Data |
| ---: | ---: | --- |
| 1 | `1` | item/model identity, physical configurator-position count (`N_CONF`), brand, line |
| 2 | `2` | firmware version |
| 3 | `3` | hardware version |
| 4 | `4` | configurators 1–6 |
| 5 | `5` | configurators 7–12 |
| 6 | `6` | microcontroller version |
| 7 | `7` | diagnostic bitmask A |
| 8 | `8` | diagnostic bitmask B |
| 9 | `13` | Device ID |
| 10 | `30` | repeated Module/Object records |
| 11 | `32` | repeated Module-address records |
| 12 | `31` | Object-state errors when applicable |
| 13 | - | `WHAT 4` end marker |

This is the canonical implementation order, not a guarantee that every Device returns every optional frame. In `AS_OPEN_SEQUENCE`, the start frame is mandatory; the listed Device responses are optional, and `DIMENSION 30`, `32`, and the busy `DIMENSION 31` form are repeatable. The end marker is present at the final sequence position but is not marked mandatory by the database.

Collectors should therefore accept repeated records, retain unknown additions, and prefer the explicit end marker over an assumed record count while still handling timeout and abort paths.

## Timing and completion

| Phase | Default in `OPEN.db` |
| --- | ---: |
| Wait for the first response after address or ID start | `15` s |
| Wait for further Device information | `20` s |
| Wait for first response in local-button mode | `300` s |
| Maximum diagnostic session | `600` s |

The `20`-second further-information timer begins with `DIMENSION 1` and stops on the `WHAT 4` end marker in the canonical addressed and ID sequences. These are MyHOME_Suite defaults loaded through `OpenQuery.txt`, not wire-level constants.

## Collection state

For each active interview, retain:

- diagnostic `WHO` and start mode;
- selected Device ID or `WHERE`;
- raw frames in arrival order;
- one or more values for each `DIMENSION`;
- `DIMENSION 30` and `32` grouped by internal slot;
- structured errors;
- whether `WHAT 4`, `WHAT 6`, timeout, or transport closure ended the operation.

Do not overwrite repeated frames merely because their `DIMENSION` matches. `DIMENSION 30` and `32` are naturally multi-row data, and other dimensions may repeat during retries.

## Reconstructing the Device

1. Resolve `DIMENSION 1` against catalogue item, brand, and line metadata and retain `N_CONF` as the Device's physical configurator-position count.
2. Record the reported firmware, hardware, and microcontroller versions without assuming that a version number is a catalogue primary key.
3. Build one Module record per internal slot from `DIMENSION 30`.
4. Attach `DIMENSION 32` system/address data to the matching internal slot.
5. Preserve configured and unconfigured Module states.
6. Request detailed parameters only after the Module/Object layout is known.

The result is an installed-state view. Catalogue data supplies permitted capabilities; the interview supplies the choices and values currently reported by the Device.

The catalogue and runtime projections must remain distinct:

| Question | Strongest evidence |
| --- | --- |
| Which product capability is possible? | `MHCatalogue.db` item, firmware, slots, Objects, and constraints |
| Which installed Device responded? | `DIMENSION 13` plus diagnostic context |
| Which product description should be shown? | `EN_DEVICE.name` after `DIMENSION 1` resolution |
| Which configured Object or unconfigured Virgin Object is reported for a Module? | `DIMENSION 30` |
| Which functional address is reported for that Module? | `DIMENSION 32` |
| Which indexed value is reported? | `DIMENSION 35` interpreted through the resolved Object/firmware configuration |

## Detailed configuration phase

`OPEN.db` defines a separate `DiagKO` sequence beginning with `*#[WHO]*0*38#0##`. It can return repeated `DIMENSION 35` parameter records and `DIMENSION 310` Object-specific values. The database labels `DIMENSION 38` as a reset/select operation, while the sequence description frames it as retrieval of detailed Object/configuration information. Preserve that ambiguity until Device behavior is characterized per family.

`ScanKOTimeWait` assigns an eight-second response window to the all-Module operation. A one-Module variant, `*#[WHO]*0*38#[SLOT]##`, also exists but is not the command used by the canonical `DiagKO` sequence.

## Errors and abnormal termination

`DIMENSION 31` reports Object state conditions, `DIMENSION 34` reports an address error, and `DIMENSION 39` reports a configuration-parameter error. `ACK` and `NACK` can also occur in the implementation sequences.

A timeout is not equivalent to `WHAT 4`: it leaves completion uncertain. Send `WHAT 6` when explicitly abandoning an active diagnostic operation if the transport and target support the close operation.

`CloseScan` consists of the programmer `WHAT 6` frame. The canonical implementation assigns a 600-second diagnosis timeout and a one-second close wait around this lifecycle; applications may choose different policy but should record whether completion came from `WHAT 4`, `WHAT 6`, timeout, or transport loss.

## Observed-runtime limits

Observed `WHO 1001` traffic corroborates ID-based interview, repeated Module records, detailed configuration responses, and `WHAT 4` termination. It also shows product-specific response surfaces: a command-only Device can omit an observed `DIMENSION 32`, while a multi-Module sensor can expose many internal slots. These observations refine optionality but do not redefine the database sequence for all diagnostic families.
