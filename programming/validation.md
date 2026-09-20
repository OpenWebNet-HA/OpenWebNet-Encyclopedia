# Programming Validation

Programming validation checks a complete intended configuration against the available evidence for one resolved Physical Device before any write is sent. Passing catalogue and encoding checks establishes consistency with those sources, not proven runtime acceptance, persistence, or complete coverage of Device constraints. The numeric ranges in `OPEN.db` describe frame-field capacity; they do not establish that a value, Object, address, or property is valid for a particular Device.

Validation is a staged resolver. Each milestone consumes an established context and produces evidence required by the next milestone. If a required result is ambiguous or unresolved, stop before programming.

## Required input

Start with an immutable working record containing all available installation evidence:

| Input | Source |
| --- | --- |
| management `WHO` | selected diagnostic/programming family |
| Device selector | diagnostic `WHERE` and, where available, `DIMENSION 13` Device ID |
| identity projection | diagnostic `DIMENSION 1`, firmware version, and hardware version |
| Module projection | every `DIMENSION 30` record |
| address projection | every `DIMENSION 32` record |
| parameter projection | every `DIMENSION 35` record and any `DIMENSION 310` record |
| intended state | complete desired Module/Object layout, addresses, and property values |

Retain raw frames beside decoded values. Do not replace an unresolved field with a guessed catalogue identifier.

## Milestone overview

| Milestone | Goal | Required output |
| ---: | --- | --- |
| 1 | Resolve the installed Device | one item/firmware context or an explicit ambiguity set |
| 2 | Resolve the Module | one Device-local `slot` and its catalogue placement |
| 3 | Resolve the current role | enabled regular Object or disabled Module's Virgin Object |
| 4 | Prove the target Object is available | one permitted target Object and Object/firmware association |
| 5 | Build the property dictionary | applicable Object- and firmware-scoped `EN_CONF` definitions |
| 6 | Establish write eligibility | writable, visible, fixed, hidden, or conditional status |
| 7 | Build the base value domain | enumerated values or numeric bounds from `EN_CONF_RANGE` |
| 8 | Apply contextual filters | Object/firmware-specific effective domain |
| 9 | Apply conditions and conversions | selected branches and encoded value |
| 10 | Apply linked-property rules | cross-property-valid candidate configuration |
| 11 | Validate addresses | valid `SYS`/`ADDR` encoding for the resolved Object |
| 12 | Classify physical representation | physically representable, outside the established physical domain, or unresolved |
| 13 | Build wire values | validated `KEYO`, `SYS`/`ADDR`, and `INDEX`/`VAL_PAR` tuples |
| 14 | Validate the complete transfer | internally consistent replacement payload and verification plan |

The milestones are dependencies, not merely a convenient order. For example, an `INDEX` cannot be resolved safely before the Object, firmware, and `slot` are known.

## 1. Resolve the installed Device

### Goal

Establish the catalogue context corresponding to the installed Physical Device without confusing protocol values with database primary keys.

### Procedure

1. Use the management `WHO` to select the applicable diagnostic family.
2. Decode `DIMENSION 1` according to that family.
3. Resolve its item/model value through the documented item and system associations.
4. Resolve the candidate Physical Device records and use `EN_DEVICE.name` as the standard Device description.
5. Use the reported firmware version to narrow the applicable item/firmware association. Preserve hardware and microcontroller versions as observations; use them for selection only when an independently established mapping exists.
6. Preserve multiple SKU candidates when several catalogue items share the same implementation identity.
7. Retain the installed Device ID from `DIMENSION 13` separately from every catalogue identifier.

`DIMENSION 1` VALUE 2 is `N_CONF`, the physical configurator-position count. Do not use it as a Device class, Object, Virgin Object, or firmware key.

### Milestone output

Record at least:

- diagnostic family and `WHO`;
- raw and decoded identity projection;
- item/model identity;
- candidate SKU set;
- resolved firmware record and version evidence;
- installed Device ID;
- unresolved identity ambiguities.

### Stop conditions

Stop if no catalogue item or firmware can be justified. If several SKUs remain but share the same relevant firmware capability, validation may continue only with that common capability; do not claim a unique SKU.

See [Device Identity](../diagnostics/dim1-device-identity.md) and [Physical Device](../device-model/physical-devices.md).

## 2. Resolve the Module and `slot`

### Goal

Bind the intended change to one firmware-exposed Module and the numeric `slot` carried by programming frames.

### Procedure

1. Use diagnostic `DIMENSION 30.SLOT` as the Device-local `slot` number.
2. Correlate it with catalogue placement such as `EN_SLOTS.first_slot`.
3. Resolve the relevant `AS_OBJECT_FIRMWARE` and slot records for the selected firmware.
4. Retain UI-visible Module numbering only as presentation metadata.
5. Do not synthesize Modules merely because `EN_FIRMWARE.slots` declares a capacity.

### Milestone output

Produce one Module context containing:

- installed Device and firmware;
- protocol `slot`;
- matching catalogue slot records;
- current `DIMENSION 30` state;
- associated `DIMENSION 32` and `35` records;
- fixed-Object and slot-condition metadata.

### Stop conditions

Stop if the `slot` does not exist for the resolved firmware or if several incompatible catalogue placements remain.

## 3. Resolve the current Object or Virgin Object

### Goal

Interpret the current `DIMENSION 30.KEYO` in the correct external number space.

| `STATE` | Resolve `KEYO` against | Meaning |
| ---: | --- | --- |
| `0` | `EN_KEY_OBJECT.key_object` | enabled Module; regular configured Object |
| `1` | `EN_VIRGIN_OBJECT.virgin_key_object` | disabled Module; Virgin Object |

Neither value is an internal database primary key. Likewise, protocol `SLOT` is not `EN_SLOTS.id_slot`.

For a disabled Module, retain the Virgin Object as the role constraint from which permitted regular Objects will be derived. Do not send its `virgin_key_object` as a target `KEYO` merely because it was reported diagnostically.

### Milestone output

Produce exactly one of:

- a resolved current regular Object for an enabled Module; or
- a resolved Virgin Object with its functional role for a disabled Module.

Stop if `STATE` is absent or if `KEYO` does not resolve uniquely in the selected namespace.

See [`DIMENSION 30`: Modules and Objects](../diagnostics/dim30-modules.md).

## 4. Prove target Object availability

### Goal

Reduce the global Object catalogue to the set supported by this firmware, Module, and current configurable role.

### Procedure

1. If the Module is disabled, enumerate candidates related to its Virgin Object through `AS_OBJECT_VIRGIN_OBJECT`.
2. Intersect that set with Objects related to the resolved firmware through `AS_OBJECT_FIRMWARE`.
3. Intersect again with Objects placed at the resolved `slot` through `EN_SLOTS`.
4. Apply `fixed_ko` and slot-condition metadata.
5. If the Module is already configured, determine whether replacement is permitted; current membership alone does not prove writability.
6. Select the target by external `EN_KEY_OBJECT.key_object`, but retain its internal `id_key_object` for catalogue joins.
7. Retain the resolved `AS_OBJECT_FIRMWARE.id_object_firmware`; contextual filters depend on it.

Conceptually:

```text
permitted targets =
    Virgin-Object candidates, when applicable
  ∩ firmware-supported Objects
  ∩ `slot`-supported Objects
  ∩ satisfied fixed/conditional constraints
```

### Milestone output

Produce:

- one target `id_key_object`;
- its external programming `key_object`;
- one applicable Object/firmware association;
- one compatible slot placement;
- the evidence that admitted it to the permitted set.

### Stop conditions

Reject the target if it disappears at any intersection. Do not fall back to the global Object list.

See [Object Programming](object-programming.md), [Objects](../device-model/objects.md), and [Virgin Objects](../device-model/virgin-objects.md).

## 5. Build the applicable property dictionary

### Goal

Collect every configuration definition that can describe the resolved Object/firmware context.

`EN_CONF` uses two exclusive ownership scopes:

| Scope | Selection |
| --- | --- |
| Object property | resolved `id_key_object` and `id_firmware = 0` |
| Firmware property | `id_key_object = 0` and resolved `id_firmware` |

Collect their union:

```sql
SELECT *
FROM EN_CONF
WHERE (id_key_object = :object_id AND id_firmware = 0)
   OR (id_key_object = 0 AND id_firmware = :firmware_id)
```

The zero is a “not applicable” sentinel, not Object or firmware ID 0. Never require both resolved IDs on the same `EN_CONF` row.

Index the resulting dictionary by at least:

- scope;
- `EN_CONF.id_conf`;
- `idx`;
- symbolic name;
- semantic type;
- data type;
- `slot` and Object/firmware context.

An `idx` is not globally unique. It becomes a usable `DIMENSION 35.INDEX` only after this context has been resolved.

The union is a candidate property dictionary, not a list of writable parameters. In particular, firmware physical fields with `idx = -1` cannot be emitted as an unsigned `DIMENSION 35.INDEX`; neither a shared symbol nor catalogue presence establishes their transfer operation.

### Milestone output

Produce the complete context-specific property dictionary and identify whether each intended UI/property concept resolves to zero, one, or several definitions.

### Stop conditions

- zero matches: unresolved or unsupported property;
- one match: continue;
- several matches: disambiguate by scope, symbol, semantic type, filter, UI behavior, or capture evidence before continuing.

See [Configuration Programming](configuration-programming.md) for the write mapping.

## 6. Establish write eligibility

### Goal

Separate values that exist in the catalogue from values that the programmer may modify.

For each resolved `EN_CONF` definition, evaluate:

- `read_only`;
- `visible`;
- `hidden`;
- fixed-value data type;
- progressive/order metadata;
- applicable slot conditions;
- whether the value is calculated or compiled by MyHOME_Suite;
- whether it is reported by the Device but lacks a generic programming operation.

Classify the property as:

| Status | Programming treatment |
| --- | --- |
| writable | candidate for a write |
| conditional | writable only if its enabling condition is satisfied |
| fixed | preserve the defined value; do not offer arbitrary input |
| read-only | compare during verification but do not write |
| hidden | do not assume invalid; resolve the hiding condition |
| unsupported | omit from the payload |
| unresolved | fail closed |

Visibility is presentation metadata, not by itself permission to write. Conversely, a hidden property can still participate in conversions or linked rules.

## 7. Build the base value domain

### Goal

Derive the values allowed by the selected configuration definition before contextual narrowing.

Use `EN_CONF_DATA_TYPE` to choose interpretation and `EN_CONF_RANGE` to construct the base domain.

### Enumerated domain

When range rows provide discrete values, retain for each member:

- stored value;
- display name;
- default flag;
- ordering;
- digit width;
- step and min/max metadata where present.

Do not validate by display text alone; the wire carries the encoded stored value.

### Numeric domain

When a definition supplies numeric bounds, validate:

```text
min_value ≤ candidate ≤ max_value
(candidate - min_value) mod step = 0
```

Apply the step test only when a meaningful nonzero step is defined. Preserve digit-width and padding separately from numeric validity.

### Fixed, Boolean, padded, and user values

- Boolean properties must use the encoded values established by their definition; do not assume every Boolean uses arbitrary nonzero truth.
- Fixed values are not general input domains.
- `Range_Pad` values require both numeric validation and width-preserving encoding.
- `user_value` does not mean unrestricted; filters, conditions, and protocol capacity still apply.

A missing `EN_CONF_RANGE` row does not make the full `VAL_PAR` transport range valid.

### Milestone output

Produce a base domain with provenance back to `id_conf` and the exact range rows used.

## 8. Apply Object/firmware filters

### Goal

Narrow the base property domain for the particular Object implementation on the selected firmware.

1. Resolve the applicable `AS_OBJECT_FIRMWARE.id_object_firmware` from milestone 4.
2. Find `EN_FILTER` rows that bind that association to the resolved `EN_CONF.id_conf`.
3. Apply the related `EN_FILTER_RANGE` rows.
4. Respect the filter’s `whole_range` behavior as represented by the catalogue.
5. Intersect the filtered domain with the base domain.
6. Do not combine filters belonging to another Object/firmware association.

Conceptually:

```text
effective domain =
    base EN_CONF_RANGE domain
  ∩ ranges admitted by the applicable EN_FILTER context
```

If a relevant filter exists but cannot be interpreted, mark the property unresolved rather than silently using the broader base range.

### Milestone output

Produce the effective context-specific domain and retain the filter and filter-range identifiers that produced it.

## 9. Apply slot conditions and conversions

### Goal

Determine whether the target Object/property is active in this slot and convert the intended semantic value into its catalogue/wire representation.

1. Load `AS_SLOT_CONDITION` for the resolved slot placement.
2. Resolve its `EN_CONDITION`.
3. Follow the selected `EN_CONV_RULE` logic.
4. Supply all referenced item-level and Object-level symbols from the candidate configuration.
5. Evaluate explicit comparisons, unconditional branches, and jumps in their stored order.
6. Use `CONF_SYMBOL_REF` where it explicitly relates an item symbol to an Object symbol for the system and slot.
7. Record the branch taken and the resulting value.

A conversion is not valid merely because its output fits `0..65535`. Revalidate the converted result against the effective domain.

`CONF_SYMBOL_REF` is supporting mapping evidence, not a global symbol-alias table. A symbol correspondence from one system or slot must not be applied universally.

### Milestone output

Produce:

- satisfied/unsatisfied condition state;
- rule path;
- semantic input;
- converted catalogue value;
- evidence for any symbol correspondence.

Stop on a missing dependency, ambiguous branch, loop, or unmapped conversion output.

## 10. Apply linked-property rules

### Goal

Validate dependencies that cannot be decided from one property in isolation.

For Objects covered by `rules.db3`:

1. Confirm the resolved external Object number is one of the Objects represented there.
2. Bind expressions such as `$1`, `$2`, or `$21` to the corresponding resolved `EN_CONF.idx` only within that Object context.
3. Evaluate the rule using the complete candidate configuration, not only the changed property.
4. Apply `DisablelinkedParameter` behavior to dependent properties.
5. Re-run affected domains and write-eligibility classifications after a controlling value changes.

The current `rules.db3` evidence is limited to selected Temperature Control Objects. It is not a general Object, `WHO`, or parameter registry.

### Milestone output

Produce a complete candidate property set in which all referenced dependencies have values and no enabled rule is violated.

## 11. Validate an address

### Goal

Prove that one Module address can be encoded as a valid `DIMENSION 32` write.

1. Resolve the target Object’s functional system.
2. Select the applicable `OPEN.db` address rule using the management family and Object/device family.
3. Resolve the rule’s component structure and fixed values.
4. Validate every component domain and level rule.
5. Apply required prefixes, padding, validity conditions, and advanced offsets.
6. Establish the Object-specific numeric `ADDR` encoding independently of the functional or management `WHERE` string. An address-rule template alone does not authorize copying group markers or routing suffixes into `ADDR`.
7. Resolve `SYS` independently; do not assume it equals a functional `WHO`, diagnostic `WHO`, or either database’s internal system ID.
8. Decode the generated value again and require a round-trip match.

The result is the tuple:

```text
(SLOT, SYS, raw ADDR, decoded components, address-rule identity)
```

Do not force every family into `A`/`PL`. Temperature Control, CEN/CEN+, Energy Management, Access Control, interface, group, and environment forms use distinct grammars.

See [Address Programming](address-programming.md) and [Address Discovery](../diagnostics/address-discovery.md).

## 12. Classify physical representation

### Goal

Determine whether the effective property could also be represented by physical configurators. This does not determine which configuration mode produced the installed value.

1. Confirm through `AS_FIRMWARE_CONFIG_MODE` and `EN_CONFIG_MODE` that the firmware supports the distinct Physical configuration mode.
2. Enumerate demonstrated physical firmware-scoped `EN_CONF` definitions; do not treat `idx = -1` alone as proof because the common `AID`/ID field shares that structure.
3. Resolve each physical symbol's legal domain through its exact `EN_CONF_RANGE`.
4. For an address, compare decoded `DIMENSION 32` components with applicable physical symbols such as `A` and `PL`.
5. For an indexed property, compare its resolved Object definition with applicable firmware physical symbols such as `M`, `TYPE`, `PRE`, or `G1`.
6. Compare symbol, semantic type, domain, filters, `CONF_SYMBOL_REF`, conversion rules, sparse `EN_PHY_TO_ADV_TRANS` evidence, product documentation, and captures where applicable.
7. Establish the physical domain independently from the programming transport domain.

Classify the result as:

| Classification | Meaning |
| --- | --- |
| direct counterpart | symbol and semantics match in the resolved context |
| mapped counterpart | different symbols, but a conversion or independently corroborated semantic mapping exists |
| physically representable | intended effective value lies in the established physical domain |
| outside established physical domain | a counterpart is established, but this value is not in its legal physical domain |
| no physical counterpart established | inspected evidence does not establish a counterpart; this is not proof that none exists |
| unresolved | required physical-interface or mapping evidence is insufficient |

The canonical catalogue registers Virtual Configuration and Advanced Configuration as distinct modes. `OPEN.db` separately labels `ConfConfigurators` as virtual configuration and `ConfKO` as advanced configuration. Do not replace these source labels with a single umbrella category or infer the active mode from effective values alone.

If physical configurator values are themselves being resolved into a topology, use the deterministic reachability and Object-selection method in [Catalogue Resolution](../internals/catalogue-resolution.md#physical-configuration-resolution) before property-level validation.

## 13. Encode programming tuples

Only after semantic validation should values be converted into frames.

| Intended change | Validated output |
| --- | --- |
| Object selection | `(SLOT, EN_KEY_OBJECT.key_object)` for `DIMENSION 30` |
| Module address | `(SLOT, SYS, ADDR)` for `DIMENSION 32` |
| indexed property | `(INDEX, SLOT, VAL_PAR)` for `DIMENSION 35` |
| `ConfConfigurators` fields | twelve raw values for `DIMENSION 4` and `5`, subject to Device support and unresolved catalogue-position correlation |

For each encoded value retain:

- semantic intended value;
- raw user input;
- resolved Device, firmware, Module, and Object;
- `id_conf`, scope, and `idx`, where applicable;
- base and filtered domains;
- condition and conversion path;
- physical-representation classification;
- final wire value.

Perform an encode/decode round trip wherever a decoder exists. The result must reproduce the intended semantic value in the same context.

## 14. Validate the complete transfer

### Goal

Prove that the entire payload is coherent before the canonical advanced sequence resets all Objects.

Validate the complete desired Device state, not merely changed fields:

1. Include every Module/Object assignment that must remain after reset-all.
2. Require unique Device-local `slot` positions.
3. Require every address and parameter to reference an Object included in the same candidate layout.
4. Order each Module’s Object assignment before its address and parameter writes.
5. Preserve fixed and untouched Modules in the replacement plan.
6. Re-evaluate conditions and linked rules after combining all candidate values.
7. Confirm that every required value is present and every omitted value is optional, fixed, read-only, unsupported, or deliberately preserved.
8. Confirm all encoded fields fit their `OPEN.db` transport ranges.
9. Prepare the expected diagnostic read-back for `DIMENSION 30`, `32`, and `35`.
10. Preserve a recovery copy of the prior effective state.

Because `ConfKO` begins with reset-all, partial validation is unsafe. Do not transmit the reset frame until this milestone succeeds.

## Validation result model

Validation should return evidence, not only a Boolean.

| Result | Meaning |
| --- | --- |
| valid | allowed by the inspected constraints in the resolved context; runtime acceptance not yet verified |
| valid after conversion | allowed after a documented conversion path |
| conditionally valid | valid only while stated dependencies hold |
| physically representable | a physical counterpart and compatible physical value exist |
| outside established physical domain | valid in the resolved programming context but outside a demonstrated physical counterpart's domain |
| fixed/read-only | part of effective state but not an arbitrary write |
| invalid | excluded by an applicable capability, domain, filter, condition, or rule |
| ambiguous | more than one incompatible resolution remains |
| unresolved | required context or mapping is absent |

A useful validation record contains:

```text
status
reason
source evidence
resolved identifiers
candidate semantic value
encoded value
applicable domain
dependencies
warnings
expected read-back
```

Fail closed for programming when the status is ambiguous or unresolved. Diagnostics may preserve unknown values; programming must not transmit an invented interpretation.

## Revalidation triggers

Restart validation from the earliest affected milestone when any of these change:

| Change | Restart at |
| --- | ---: |
| Device identity or firmware | 1 |
| `slot` or Module layout | 2 |
| current Virgin Object or target Object | 3 |
| Object/firmware association | 4 |
| property or `INDEX` | 5 |
| controlling property value | 7 or 9 |
| functional system/address type | 11 |
| configuration method question | 12 |
| any member of the replacement payload | 14 |

Do not reuse a previously validated range after changing Object, firmware, slot, or a controlling property.

## Source boundaries

| Source | Validation authority |
| --- | --- |
| `MHCatalogue.db` | Device/firmware capability, Objects, slots, properties, domains, filters, conditions, and conversions |
| `rules.db3` | additional dependencies for selected Temperature Control Objects |
| `OPEN.db` | programming frames, transport ranges, address rules, sequence behavior, and errors |
| `OpenQuery.txt` | implementation queries used to assemble protocol scenarios |
| public OpenWebNet documents | shared functional meaning and public frame/address syntax |
| product documentation | physical configurator positions and product-specific behavior |
| observed traffic | runtime support, ordering, optional responses, and effective values |
| MyHOME_Suite UI | labels, selectable values, visibility, and workflow behavior |

Do not let a lower-level transport range override a narrower catalogue rule. When sources disagree, retain the discrepancy and the raw evidence rather than silently choosing the least restrictive interpretation.
