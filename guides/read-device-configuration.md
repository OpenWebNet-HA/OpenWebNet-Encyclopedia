# Read and Present a Device Configuration

## Goal

Transform a completed set of raw diagnostic frames into a structured, user-presentable description of one installed Physical Device and its effective configuration.

The guide does not stop at collecting `DIMENSION` responses. Its output should answer:

- Which installed Device is this?
- Which Modules does it expose?
- Which function is assigned to each Module?
- Is each Module configured or still represented by a Virgin Object?
- What address and configuration values are effective?
- Which labels, choices, and constraints should be shown to a user?
- Which parts remain ambiguous, unsupported, or unreported?

## Prerequisites

- an inventory entry from [Discover and Identify Devices](discover-devices.md);
- a Device selector: preferably the discovered 32-bit ID, otherwise a diagnostic address or local-interaction workflow;
- access to `MHCatalogue.db`, `OPEN.db`, and applicable `rules.db3` data;
- the diagnostic `WHO` and Device-selection context;
- raw frames retained in arrival order.

## Acquire the raw frames

Start the Device interview before attempting to parse any `DIMENSION` response:

| Selection method | Send |
| --- | --- |
| Device ID | `*[WHO]*10#[ID]*0##` |
| diagnostic address | `*#[WHO]*[WHERE]*0##` |
| local interaction | `*[WHO]*5*0##`, then perform the Device-side interaction during the 300-second first-response window |

Collect the initial response stream in arrival order. The canonical stream can contain `DIMENSION 1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `13`, repeated `30` and `32`, applicable `31` errors, and Device `WHAT 4`.

Use the applicable 15-second first-response window for ID/address selection or the 300-second local-interaction window, followed by the 20-second further-information window used by MyHOME_Suite. Record whether `WHAT 4`, abort, timeout, or transport closure ended collection.

Only after this request/response phase should the following frames be parsed.

## Inputs

| Input | Purpose |
| --- | --- |
| `DIMENSION 1` | item/model, physical configurator count, brand, and collection/line evidence |
| `DIMENSION 2`, `3`, and `6` | firmware, hardware, and microcontroller versions |
| `DIMENSION 13` | installed Device ID |
| repeated `DIMENSION 30` | Module, Object or Virgin Object, and configured state |
| repeated `DIMENSION 32` | Module system and effective address |
| repeated `DIMENSION 35` | indexed configuration values |
| `DIMENSION 310` | special Object-specific value |
| `DIMENSION 31`, `34`, and `39` | Module, address, and property errors |
| terminal condition | `WHAT 4`, abort, timeout, or transport closure |

Do not discard optional omissions. “Not reported” is different from zero, disabled, unsupported, or invalid.

## 1. Establish the Device context

Begin with the identified inventory record:

1. confirm the interview belongs to the intended 32-bit Device ID;
2. retain the diagnostic `WHO` and selected `WHERE` or ID;
3. resolve the catalogue item and candidate `EN_DEVICE` records;
4. use `EN_DEVICE.name` as the preferred Device type or description;
5. retain candidate brands, collections, and SKUs;
6. resolve the applicable firmware capability from the item and reported version;
7. preserve ambiguity where several catalogue records remain.

The installed Device ID, catalogue primary keys, SKU, Object numbers, and functional addresses are separate identifier spaces.

Do not use unresolved `DIMENSION 1` VALUE 2 to refine identity or Device class.

## 2. Build the Module list

Use every `DIMENSION 30` response:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

1. Group records within the same Device interview.
2. Use protocol `SLOT` as the Device-local internal-slot key.
3. Do not renumber slots to match MyHOME_Suite visible Module numbering.
4. Correlate the internal slot with catalogue placement such as `EN_SLOTS.first_slot`.
5. Retain fixed-Object, hidden, conditional, and slot-capacity metadata.
6. Do not synthesize Modules only because `EN_FIRMWARE.slots` declares a capacity.

For each internal slot create one Module record, even when its function is unresolved.

## 3. Resolve configured and unconfigured functions

`DIMENSION 30.STATE` selects the namespace of `KEYO`:

| `STATE` | Resolve `KEYO` against | User interpretation |
| ---: | --- | --- |
| `1` | `EN_KEY_OBJECT.key_object` | configured Object/function |
| `0` | `EN_VIRGIN_OBJECT.virgin_key_object` | unconfigured Module role |

For a configured Module:

- use the resolved Object description as the function type;
- retain the internal `id_key_object` for catalogue joins;
- retain the external `key_object` as the protocol value.

For an unconfigured Module:

- show that the Module is unconfigured;
- use the Virgin Object description to explain its available role;
- derive permitted configured Objects through `AS_OBJECT_VIRGIN_OBJECT`;
- intersect them with firmware and slot support;
- present the surviving choices as available functions, not as the current function.

A Virgin Object is not an ordinary configured Object merely because the reported numbers happen to coincide in a database revision.

## 4. Attach and decode addresses

For every `DIMENSION 32` record:

`*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##`

1. attach it only to the Module with the same Device and internal `SLOT`;
2. retain raw `SYS` and `ADDR`;
3. resolve the Object and its functional system;
4. select the applicable `OPEN.db` address rule;
5. decode fixed prefixes, levels, component widths, padding, and offsets;
6. present system-specific fields such as `A`/`PL`, zone, CEN identifier, interface, or Energy Management target;
7. verify that re-encoding the displayed components reproduces the raw address.

Do not automatically equate `SYS` with a functional `WHO`, diagnostic `WHO`, or either database's internal system ID.

When no decoder is established, display the raw tuple and mark the address interpretation unresolved. A missing `DIMENSION 32` remains “not reported”; it does not prove that the Module has no address.

## 5. Request detailed configuration

The initial interview does not ordinarily supply the complete indexed property set. After its Module/Object layout is known, send the canonical detailed-read request:

`*#[WHO]*0*38#0##`

Collect the repeated `DIMENSION 35` responses produced by that request during the MyHOME_Suite eight-second response window:

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

A one-Module `DIMENSION 38` form exists, but the canonical `DiagKO` sequence uses the all-Module form. The source also uses reset terminology for `DIMENSION 38`; preserve that ambiguity and apply suitable caution on unfamiliar Devices.

Keep `DIMENSION 310` outside the generic indexed-property model because it carries no `INDEX`.

## 6. Resolve every indexed property

For each tuple `(SLOT, INDEX, VAL_PAR)`:

1. select the Module by internal slot;
2. require its resolved configured Object;
3. collect Object-scoped `EN_CONF` definitions using the Object's `id_key_object` and `id_firmware = 0`;
4. collect firmware-scoped definitions using `id_key_object = 0` and the resolved firmware;
5. form the union of those scopes;
6. select definitions whose `idx` equals `INDEX`;
7. use scope, symbol, semantic type, filters, conditions, and supporting UI/capture evidence to remove incompatible matches;
8. retain the selected `EN_CONF.id_conf` beside the raw tuple.

The zero values are “not applicable” sentinels on the unused ownership axis. `INDEX` is not globally unique and cannot be resolved without Device, firmware, Module, and Object context.

### Resolution outcomes

| Outcome | Presentation |
| --- | --- |
| one compatible definition | show the resolved property |
| several compatible definitions | show candidates or an ambiguity marker |
| no compatible definition | preserve `INDEX` and raw value as unknown |
| read-only/fixed definition | show the value without offering arbitrary editing |
| hidden definition | retain internally and explain the controlling condition where known |

## 7. Convert raw values into display values

Use the resolved `EN_CONF` definition to interpret `VAL_PAR`:

1. determine the `EN_CONF_DATA_TYPE`;
2. load `EN_CONF_RANGE` rows;
3. apply the applicable `EN_FILTER` and `EN_FILTER_RANGE` for the resolved Object/firmware association;
4. evaluate slot conditions, `EN_CONDITION`, `EN_CONV_RULE`, and `CONF_SYMBOL_REF`;
5. apply relevant `rules.db3` dependencies;
6. map encoded enumeration values to their display names;
7. preserve numeric width and padding where semantically significant;
8. retain both raw and decoded values.

A display name does not replace the encoded value. Store both so that verification and later programming can use the exact protocol representation.

Where the database supplies no unit or complete interpretation, do not invent one from the numeric range.

## 8. Determine presentation and editability

A user-presentable property record should include:

| Field | Purpose |
| --- | --- |
| label | catalogue description or symbolic fallback |
| value | decoded display value |
| raw value | exact `VAL_PAR` |
| possible values | effective filtered domain |
| default | catalogue default where applicable |
| editable | derived from read-only, fixed, hidden, conditional, and support evidence |
| visibility | current condition and UI metadata |
| source | Object- or firmware-scoped `id_conf` |
| status | resolved, ambiguous, unknown, warning, or error |

`visible`, `hidden`, and `read_only` must be interpreted with filters and conditions. Visibility alone does not prove writability, and a hidden value can still influence another property.

## 9. Attach errors without replacing valid state

- Attach `DIMENSION 31` to the matching Module.
- Attach `DIMENSION 34` to the matching Module address.
- Attach `DIMENSION 39` to the matching Module and `INDEX`.
- Preserve the last valid reported value separately from the error.
- Distinguish programming-context severity from diagnostic information.

The boolean fields in `DIMENSION 34` and `39` do not encode a detailed cause. Catalogue violations are possible explanations, not wire-level error codes.

## 10. Build the user-presentable model

A suitable output structure is:

```text
Device
  ID
  type/description
  brands[]
  collections[]
  SKUs[]
  firmware/hardware versions
  identity status
  diagnostic completion status
  Modules[]
    internal slot
    display order/name, when established
    configured state
    function or Virgin Object role
    available function choices[]
    address
      raw SYS/ADDR
      decoded components
      interpretation status
    properties[]
      label
      display value
      raw INDEX/VAL_PAR
      effective domain
      editable/visible state
      resolution status
    errors[]
```

The presentation layer may hide database primary keys from ordinary users, but the resolver must retain them in provenance so every displayed field can be traced back to its source.

## Completion and quality status

Classify the result independently at three levels:

| Level | Example statuses |
| --- | --- |
| interview | complete, timed out, aborted, transport failure |
| identity | unique, shared capability, ambiguous, unresolved |
| field | resolved, not reported, unsupported, ambiguous, unknown, error |

A Device can have a complete interview but ambiguous SKU, or a uniquely identified Device with an optional property not reported. Do not collapse those cases into one success flag.

## Expected result

One structured Device configuration suitable for an installer UI, report, or API response, with:

- user-facing Device, Module, function, address, and property labels;
- raw protocol values retained for every field;
- candidate sets wherever catalogue identity is not unique;
- effective allowed-value domains where resolved;
- explicit editability and visibility;
- provenance and resolution status;
- no invented interpretation for unknown fields.

See [Device Interview](../diagnostics/device-interview.md), [`DIMENSION 30`](../diagnostics/dim30-modules.md), [`DIMENSION 32`](../diagnostics/dim32-addressing.md), [`DIMENSION 35`](../diagnostics/dim35-configuration.md), [Configuration](../device-model/configuration.md), and [Programming Validation](../programming/validation.md).
