# Device Discovery

Device discovery by ID enumerates installed Device instances within one diagnostic `WHO`. The Device ID is a 32-bit transport value. This documentation displays it as exactly eight hexadecimal characters, preserving leading zeroes.

## Frames

| Purpose | Frame |
| --- | --- |
| Release/reset enumeration state | `*[WHO]*12*0##` |
| Request all Device IDs | `*#[WHO]*0*13##` |
| Request configured Device IDs only | `*#[WHO]*0*13#1##` |
| Request unconfigured Device IDs only | `*#[WHO]*0*13#0##` |
| Device ID response | `*#[WHO]*[WHERE]*13*[ID]##` |
| Suppress an already found Device | `*[WHO]*11#[ID]*0##` |
| Abort/close diagnosis | `*[WHO]*6*0##` |

`ID` ranges from `0` to `4294967295` in `OPEN.db`. The hexadecimal display form is a presentation convention; the frame field itself is the numeric transport representation used by the participating implementation.

## Enumeration algorithm

1. Send `*[WHO]*12*0##` to release any prior enumeration state.
2. Send the chosen `DIMENSION 13` request.
3. Collect every `DIMENSION 13` response during the response window.
4. For each newly discovered ID, send `*[WHO]*11#[ID]*0##`.
5. Repeat the same request.
6. Stop when a complete pass yields no new response.
7. Send `*[WHO]*12*0##` to release the enumeration state.

The request-repeat-suppress behavior is present in the `OPEN.db` `ScanAID` sequence and corroborated by observed traffic. In the sequence metadata, both the ID request and the ID response/flag steps are repeatable. `ScanIDWindowDiscoveryTimeWait` assigns a default four-second discovery window to the request.

The no-response termination rule is capture-derived behavior: the canonical frame database describes repetition and its response window but does not encode a declarative “empty pass” condition.

## Example with diagnostic `WHO 1001`

| Step | Example frame |
| --- | --- |
| Release prior state | `*1001*12*0##` |
| Request IDs | `*#1001*0*13##` |
| Receive one ID | `*#1001*10*13*5234376##` |
| Flag that ID | `*1001*11#5234376*0##` |
| Repeat request | `*#1001*0*13##` |
| Release after an empty pass | `*1001*12*0##` |

If the returned decimal ID is `5234376`, its documentation display is `004FDEC8`. The example illustrates conversion only; it does not identify a particular product.

## Collection rules

- Deduplicate by the full 32-bit ID, not by `WHERE`.
- Preserve the raw decimal field and the normalized eight-character hexadecimal display.
- Treat `WHERE` as response context, not as the Device identity.
- Apply the configured response timeout to each pass.
- Do not assume response order is stable.
- Do not assume one Device exists at only one functional address.

If several Devices respond simultaneously, a gateway may deliver their frames in an order unrelated to catalogue order, physical topology, or Device ID.

The `WHERE` inside a `DIMENSION 13` response is governed by the diagnostic family’s address grammar. It can assist later addressed operations, but it must not replace the 32-bit Device ID as the inventory key.

## Filters

The final `#1` and `#0` forms select configured and unconfigured Devices respectively according to the implementation labels in `OPEN.db`. They are concrete frame templates but are not members of the canonical `ScanAID` sequence, which uses the all-Device form.

The precise Device-side definition of “configured” is not expanded by the source. It must not be assumed to mean that every Module is configured, that every address is valid, or that no disabled Module remains.

## Scan-state operations

`OPEN.db` describes `WHAT 11` as sending a flag to every Device found and `WHAT 12` as deleting previous scans from memory. Observed enumeration behavior supports the narrower operational interpretation used here:

- `WHAT 11` suppresses or marks one already reported Device during the active scan;
- `WHAT 12` releases/resets the scan state before and after enumeration.

The database does not establish persistence beyond the scan workflow. These frames must not be described as permanent configuration writes.

## Sequence and scenario boundaries

`ScanAID` performs enumeration only. The higher-level `ScanByAID` scenario then repeats:

1. `DiagAID` for each discovered Device;
2. `DiagKO` for detailed configuration;
3. `CloseScan` to terminate that Device’s diagnostic session.

This separation is why receiving a `DIMENSION 13` response does not itself provide the Module list or configuration values.

## After discovery

Start a full interview with `*[WHO]*10#[ID]*0##`. This selects the installed Device instance directly and avoids relying on a potentially ambiguous functional address. See [Device Interview](device-interview.md).

Catalogue product identity is resolved later from `DIMENSION 1`; the Device ID is not a catalogue primary key, SKU, item model, Object number, or address. See [Physical Devices](../device-model/physical-devices.md).
