# Virgin Objects

A Virgin Object is a catalogue template for a configurable Module before its final Object assignment. It links firmware/slot capability to a permitted set of concrete Objects.

“Virgin” describes configuration state and capability, not a separate physical component.

## Catalogue identity

`MHCatalogue.db.EN_VIRGIN_OBJECT` contains 18 definitions.

| Column | Role |
| --- | --- |
| `id_virgin_key_object` | Internal database key |
| `virgin_key_object` | Virgin Object number |
| `descr` | Virgin Object description |

The Virgin Object identifier space is distinct from `EN_KEY_OBJECT.key_object`. Equal numbers must not be treated as equivalent.

## Relationship chain

The catalogue uses three associations:

1. `AS_FIRMWARE_VIRGIN_OBJECT` connects a firmware to a Virgin Object and assigns an intermediate `id_fw_virgin_object`.
2. `EN_SLOT_KO_VIRGIN` places that firmware/Virgin-Object association at one or more internal slots.
3. `AS_OBJECT_VIRGIN_OBJECT` lists the concrete Objects permitted by a Virgin Object.

The resulting capability chain is:

`EN_FIRMWARE` → `AS_FIRMWARE_VIRGIN_OBJECT` → `EN_SLOT_KO_VIRGIN` → internal slot

and:

`EN_VIRGIN_OBJECT` → `AS_OBJECT_VIRGIN_OBJECT` → `EN_KEY_OBJECT`

Together they answer: “At this slot under this firmware, which Objects may this configurable Module become?”

## Canonical coverage

The canonical database contains:

| Structure | Rows |
| --- | ---: |
| Virgin Objects | 18 |
| Firmware/Virgin-Object associations | 75 |
| Slot placements | 169 |
| Virgin-Object/Object associations | 102 |

Every row in these association tables resolves to its parent record in the canonical data, although the source database does not declare all relationships as foreign keys.

## Capability, not runtime state

A Virgin Object relationship establishes that an Object is permitted by the catalogue. It does not establish that:

- an installed Module currently uses that Object;
- the Object is visible in every UI context;
- the user can select it under every configuration;
- the Device reported that Object in `DIMENSION 30`;
- the Object is enabled;
- the Object’s address or parameters are valid.

Runtime state must be obtained from diagnostic responses or project configuration.

## Examples

### Automation double command virgin

Virgin Object `500`, “Automation double command virgin”, permits five concrete Objects and is used by six firmware definitions in the canonical database.

For firmware `157`, it is placed at internal slots `3` and `4`, whose Object choices include:

- Light control;
- Automation control;
- Scheduled scenario;
- Scheduled scenario PLUS.

This corresponds to the free-command portion of `64391`, `64191`, and `64192`.

### Automation relay virgin

Virgin Object `510`, “Automation relay virgin”, permits three concrete Objects and is used by five firmware definitions.

For firmware `157`, it is placed at internal slots `1` and `2`, corresponding to the relay/actuator Modules.

### Dimmer actuator virgin

Virgin Object `528`, “Dimmer actuator virgin”, permits two concrete Objects. It is placed at both internal slots of firmware `590`, used by `F418U2`.

### Contact interface single virgin

Virgin Object `512`, “Contact interface single virgin”, permits ten Objects. It is placed at both slots of firmware `129`, used by `3477`.

### Daylight and motion sensor virgin

Virgin Object `515`, “Daylight and motion sensor virgin”, permits six Objects and is associated with twelve firmware definitions. This supports a family of sensor configurations but does not by itself define the Object active on a particular Device.

## Virgin Object and `DIMENSION 30`

`OPEN.db` defines `DIMENSION 30` with `SLOT`, `KEYO`, and `STATE`. The database describes `STATE` only as “configured or not configured”.

A `STATE` indicating an unconfigured Module is compatible with Virgin Object semantics, but `OPEN.db` does not carry a `virgin_key_object` field in this frame. Therefore:

- do not substitute the Virgin Object number for `KEYO`;
- do not assume an unconfigured `KEYO` directly encodes `EN_VIRGIN_OBJECT.virgin_key_object`;
- resolve permitted Objects through firmware and internal slot when the firmware is known.

Any direct wire representation of a Virgin Object remains protocol-family-specific and must be established separately.

## Conditions and visibility

A permitted Object can still be constrained by:

- `AS_SLOT_CONDITION`;
- `EN_CONDITION`;
- `EN_CONV_RULE`;
- `EN_FILTER` and `EN_FILTER_RANGE`;
- firmware-scoped configuration;
- MyHOME_Suite UI rules.

Consequently, `AS_OBJECT_VIRGIN_OBJECT` is a compatibility set, not a complete selection algorithm.

## Interpretation procedure

To determine which Objects a Module may expose:

1. identify the Physical Device’s `EN_ITEM`;
2. select the applicable firmware;
3. select the internal slot;
4. locate the firmware/Virgin-Object association for that slot;
5. enumerate the Virgin Object’s permitted Objects;
6. intersect that set with the firmware/Object rows present at the same slot;
7. apply slot conditions, configuration filters, and observed UI constraints;
8. compare the result with diagnostic `DIMENSION 30`.

The intersection step prevents a global Virgin Object vocabulary from being applied too broadly to a particular firmware.

## Source boundary

Virgin Objects are defined only by [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) in the canonical corpus.

`OPEN.db` supplies configured/unconfigured Module state but no explicit Virgin Object table or parameter. ScenarioDevices describes scenario-engine Objects and must not be used as a Virgin Object registry.
