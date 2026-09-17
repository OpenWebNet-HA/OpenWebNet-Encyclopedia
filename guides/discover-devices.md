# Discover and Identify Devices

## Goal

Build a structured inventory of installed Physical Devices for one diagnostic `WHO`. Discovery is not complete when an ID is returned: each discovered instance must be interviewed and resolved as far as the available runtime and catalogue evidence permits.

The inventory should contain, for every installed Device:

- the 32-bit Device ID;
- diagnostic family and observed `WHERE` values;
- Device type using the preferred `EN_DEVICE.name` description;
- candidate brand or brands;
- candidate collection or collections;
- candidate SKU or SKUs;
- resolved item and firmware evidence;
- explicit ambiguity where the protocol does not select one catalogue record.

## Prerequisites

- an authenticated OpenWebNet connection;
- the diagnostic `WHO` for the target system;
- per-pass and per-interview timeout handling;
- access to `OPEN.db` and `MHCatalogue.db`;
- a collector that preserves raw frames.

## Phase 1: enumerate installed Device IDs

1. Send `*[WHO]*12*0##` to release prior enumeration state.
2. Send `*#[WHO]*0*13##`.
3. Collect `*#[WHO]*[WHERE]*13*[ID]##` responses during the four-second MyHOME_Suite discovery window.
4. For every new ID, send `*[WHO]*11#[ID]*0##` to suppress it during the active enumeration.
5. Repeat the same request.
6. Treat a complete pass with no new response as the capture-supported end condition.
7. Send `*[WHO]*12*0##` again to release scan state.

Use `*#[WHO]*0*13#1##` or `*#[WHO]*0*13#0##` only when the configured/unconfigured filter is intentionally required. Those frames exist in `OPEN.db` but are not the ordinary `ScanAID` member.

Deduplicate by the full 32-bit Device ID, not by `WHERE`. Preserve the raw numeric field and display the ID as exactly eight hexadecimal characters with leading zeroes.

## Phase 2: interview every discovered Device

The ID response from phase 1 does not contain the Device description or configuration. Obtain those frames by starting a separate interview for each unique ID:

| Send | Collect |
| --- | --- |
| `*[WHO]*10#[ID]*0##` | optional `DIMENSION 1`, versions, configurator reports, `DIMENSION 13`, repeated `DIMENSION 30`/`32`, errors, and Device `WHAT 4` |

For each unique ID:

1. Send `*[WHO]*10#[ID]*0##`.
2. Confirm that the returned `DIMENSION 13`, where present, matches the selected ID.
3. Collect the `DIMENSION 1` identity response produced by that interview.
4. Collect firmware, hardware, and microcontroller versions when reported.
5. Preserve `DIMENSION 30` and `32` for later configuration inspection.
6. Record whether `WHAT 4`, abort, timeout, or transport closure ended the interview.
7. Do not let one failed interview discard the ID discovered in phase 1.

The canonical `ScanByAID` scenario makes the same conceptual distinction: `ScanAID` enumerates IDs, then repeated `DiagAID` operations interview the discovered Devices.

## Phase 3: resolve catalogue identity

### Resolve the item and Device type

1. Interpret `DIMENSION 1` within the selected diagnostic family.
2. Resolve the reported model/`modobj` through the appropriate item/system association.
3. Resolve the corresponding `EN_ITEM`.
4. Enumerate `EN_DEVICE` records using that item.
5. Use `EN_DEVICE.name` as the preferred MyHOME_Suite-facing Device type or description.
6. Keep `EN_KEY_OBJECT.descr` for Module/Object functions; it is not the Physical Device type.

### Resolve brands and collections

Use the brand and line/collection values reported by `DIMENSION 1` to resolve the corresponding catalogue brand and collection records. Apply them as evidence when narrowing the candidate `EN_DEVICE` rows.

The documentation uses **collection** for the user-facing product collection represented by the catalogue line data. Retain the source field and table name when recording the database path.

A single installed implementation can correspond to several branded or collection-specific catalogue records. Return arrays rather than selecting the first numeric match.

### Resolve candidate SKUs

Collect `EN_DEVICE.code` from every candidate Device record surviving the item, brand, collection, and other established constraints. Do not convert an absent or ambiguous code into a unique SKU claim.

Reported firmware and hardware versions can narrow capability and reject incompatible candidates, but a shared firmware implementation does not by itself prove one SKU.

## Identifier boundaries

| Runtime or catalogue value | Meaning |
| --- | --- |
| `DIMENSION 13.ID` | installed Device instance |
| `DIMENSION 13.WHERE` | diagnostic response context |
| `DIMENSION 1` model/`modobj` | item/system implementation identity |
| `EN_ITEM` | shared catalogue item definition |
| `EN_DEVICE.name` | preferred Device type/description |
| `EN_BRAND` | catalogue brand |
| `EN_LINE` | catalogue line/collection |
| `EN_DEVICE.code` | candidate commercial SKU |
| `EN_KEY_OBJECT` | Module/Object function, not Device type |

The Device ID is not a catalogue primary key. Equal numeric values across these identifier spaces must not be joined.

Do not use the unresolved `DIMENSION 1` VALUE 2 as an Object, Virgin Object, form factor, firmware class, or additional Device discriminator.

## Inventory record

One useful representation is:

| Field | Cardinality |
| --- | --- |
| `device_id_raw` | one |
| `device_id_hex` | one |
| `diagnostic_who` | one per inventory operation |
| `observed_where` | one or more |
| `item` | zero or one resolved item, otherwise candidates |
| `device_type` | one common description or candidate descriptions |
| `brands` | zero or more |
| `collections` | zero or more |
| `skus` | zero or more |
| `firmware` | reported version plus candidate catalogue definitions |
| `identity_status` | unique, shared capability, ambiguous, or unresolved |
| `raw_frames` | all supporting discovery and interview frames |

The list should remain useful even when product identity is ambiguous. The installed ID is still a valid inventory key, and the candidate sets explain what further evidence is needed.

## Alternative selection methods

Use [Address Discovery](../diagnostics/address-discovery.md) when ID enumeration is unavailable or a known diagnostic address must be probed. Use local-button discovery to select one physically accessible Device when neither ID nor address is sufficient. A Device found by either route should still be interviewed and passed through the same catalogue-resolution phase before entering the inventory.

## Validation gates

- Do not declare the bus empty from one silent request.
- Do not merge Devices because their `WHERE` values match.
- Do not decode every `WHERE` as `A`/`PL`.
- Do not claim a unique SKU when several Device records survive.
- Do not substitute an Object description for `EN_DEVICE.name`.
- Do not leave Devices suppressed; always release scan state.
- Keep discovery failure, interview failure, and catalogue-resolution failure as separate statuses.

## Expected result

A structured installation inventory keyed by 32-bit Device ID and enriched with the strongest justified Device type, brand, collection, SKU, item, and firmware evidence. Every non-unique field remains an explicit candidate set.

See [Device Discovery](../diagnostics/device-discovery.md), [Device Interview](../diagnostics/device-interview.md), [Device Identity](../diagnostics/dim1-device-identity.md), [Physical Devices](../device-model/physical-devices.md), and [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md).
