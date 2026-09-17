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

## Expected response groups

The canonical sequences order the following response families:

| Order | `DIMENSION` | Data |
| ---: | ---: | --- |
| 1 | `1` | item/model identity, `N_CONF`, brand, line |
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
| 13 | — | `WHAT 4` end marker |

This is the canonical implementation order, not a guarantee that every Device returns every optional frame. Collectors should accept repeated records, retain unknown additions, and finish on the explicit end marker rather than on an assumed record count.

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

1. Resolve `DIMENSION 1` against catalogue item, brand, and line metadata.
2. Record the reported firmware, hardware, and microcontroller versions without assuming that a version number is a catalogue primary key.
3. Build one Module record per internal slot from `DIMENSION 30`.
4. Attach `DIMENSION 32` system/address data to the matching internal slot.
5. Preserve configured and unconfigured Module states.
6. Request detailed parameters only after the Module/Object layout is known.

The result is an installed-state view. Catalogue data supplies permitted capabilities; the interview supplies the choices and values currently reported by the Device.

## Detailed configuration phase

`OPEN.db` defines a separate `DiagKO` sequence beginning with `*#[WHO]*0*38#0##`. It can return repeated `DIMENSION 35` parameter records and `DIMENSION 310` Object-specific values. The database labels `DIMENSION 38` as a reset/select operation, while the sequence description frames it as retrieval of detailed Object/configuration information. Preserve that ambiguity until Device behavior is characterized per family.

## Errors and abnormal termination

`DIMENSION 31` reports Object state conditions, `DIMENSION 34` reports an address error, and `DIMENSION 39` reports a configuration-parameter error. `ACK` and `NACK` can also occur in the implementation sequences.

A timeout is not equivalent to `WHAT 4`: it leaves completion uncertain. Send `WHAT 6` when explicitly abandoning an active diagnostic operation if the transport and target support the close operation.
