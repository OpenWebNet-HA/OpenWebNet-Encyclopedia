# Validate a Configuration Value

## Goal

Decide whether one intended semantic value is writable for the resolved Device, firmware, Module, and Object, and derive its wire encoding.

## Prerequisites

- the applicable diagnostic `WHO`;
- a Device selector: 32-bit ID, diagnostic address, or local interaction;
- the intended Module, property, and semantic value;
- access to `MHCatalogue.db`, `OPEN.db`, and applicable `rules.db3`;
- the ability to send and receive frames as MyHOME_Suite does.

## Acquire the current state

Validation depends on the installed context, not only the proposed value.

Select the Device and collect a fresh interview:

| Selection method | Send | First-response window |
| --- | --- | ---: |
| Device ID | `*[WHO]*10#[ID]*0##` | 15 s |
| diagnostic address | `*#[WHO]*[WHERE]*0##` | 15 s |
| local interaction | `*[WHO]*5*0##`, then perform the Device-side interaction | 300 s |

Continue collecting during the 20-second further-information window used by MyHOME_Suite. Preserve identity and version frames, repeated `DIMENSION 30` and `32`, errors, and the terminal condition. Device `WHAT 4` is the normal interview terminator.

Resolve:

1. the catalogue item and all compatible `EN_DEVICE` candidates;
2. the applicable firmware;
3. the target internal `SLOT`;
4. the current enabled regular Object or disabled Module's Virgin Object;
5. the current address and configuration context.

Then request the detailed values:

`*#[WHO]*0*38#0##`

Proceed only where this operation's effects are established for the target family and firmware. Its `DiagKO` retrieval role and reset/select label in `OPEN.db` leave universal non-destructive behavior unresolved. If that boundary is not established, stop before requesting detailed values or programming from an incomplete snapshot. See the canonical [Detailed Configuration Reading](../diagnostics/dim35-configuration.md#reading-detailed-parameters) treatment.

Collect repeated `DIMENSION 35`, applicable `DIMENSION 39` errors, and any `DIMENSION 310` response during the eight-second response window.

Close the diagnostic session with `*[WHO]*6*0##` after detailed collection, including cleanup on failure when the transport permits.

Keep the current-state snapshot immutable for the rest of validation. If the interview or detailed read is partial, record that limitation and fail closed whenever missing state can affect the candidate value.

## Procedure

1. Take the resolved installed Device and firmware from the freshly acquired configuration model.
2. Resolve the `slot`, its enabled/disabled state, and the corresponding regular Object or Virgin Object.
3. Prove that the target Object survives the Virgin Object, firmware, and slot intersections.
4. Resolve the Object- and firmware-scoped `EN_CONF` property.
5. Evaluate `read_only`, `visible`, `hidden`, fixed-value, and conditional metadata.
6. Build the base domain from `EN_CONF_RANGE`.
7. Apply the applicable `EN_FILTER` and `EN_FILTER_RANGE` for the resolved `AS_OBJECT_FIRMWARE` context.
8. Evaluate slot conditions, `EN_CONDITION`, `EN_CONV_RULE`, and `CONF_SYMBOL_REF`.
9. Apply `rules.db3` dependencies for the supported Temperature Control Objects.
10. Revalidate the converted value against the effective domain.
11. Confirm the result fits the `OPEN.db` transport field.
12. Record the expected diagnostic read-back.

## Validation algorithm

```text
function validate_candidate(snapshot, target_slot, target_property, semantic_value):
    require snapshot identifies one Device context and compatible firmware context
    module = snapshot.modules[target_slot]
    if module is missing:
        return invalid("target Module was not reported")

    target_object = resolve_requested_or_current_object(module)
    if target_object differs from current object:
        prove target_object is allowed by:
            Virgin Object mapping
            AND firmware support
            AND slot placement
        otherwise return invalid or ambiguous

    definitions = object_scoped_EN_CONF(target_object)
                UNION firmware_scoped_EN_CONF(snapshot.firmware)

    property = resolve target_property within definitions
    if zero matches:
        return unknown_property
    if more than one compatible match:
        return ambiguous_property

    if property is fixed or read-only:
        return invalid("property is not writable")

    base_domain = decode EN_CONF_RANGE(property)
    filtered_domain = apply EN_FILTER and EN_FILTER_RANGE
    conditional_domain = apply:
        slot conditions
        EN_CONDITION
        EN_CONV_RULE
        CONF_SYMBOL_REF
        applicable rules.db3 dependencies
        current values of linked properties

    encoded = convert semantic_value using the selected definition
    if conversion is ambiguous or lossy without an established rule:
        return invalid_or_ambiguous

    if encoded not in conditional_domain:
        return invalid with rejected milestone and effective domain

    transport = resolve exact OPEN.db write-frame parameter
    if encoded does not fit transport:
        return invalid("wire representation cannot carry value")

    return valid {
        semantic value,
        encoded value,
        complete domain evidence,
        linked values assumed,
        expected DIMENSION 35 or DIMENSION 310 read-back
    }
```

### Milestone results

Do not return only `true` or `false`. Record each milestone independently:

| Milestone | Evidence |
| --- | --- |
| Device identity | candidate `id_device`, item, brand, collection, SKU |
| firmware | reported version and selected `id_firmware` |
| Module | `slot` and raw `DIMENSION 30` |
| Object eligibility | current Object or Virgin-to-Object intersection |
| property identity | selected `id_conf`, scope, symbol, and `INDEX` |
| writability | fixed, hidden, visible, and read-only metadata |
| base domain | `EN_CONF_RANGE` rows |
| filtered domain | selected Object/firmware filter rows |
| conditional domain | catalogue conditions and linked-property state |
| external rules | applicable `rules.db3` rows |
| conversion | semantic-to-wire transformation |
| transport | selected `OPEN.db` parameter envelope |
| read-back | expected diagnostic property and encoded value |

A failure at an early milestone prevents later milestones from making the value safe.

## SQL example: build the effective domain

Open or attach all three sources so cross-database provenance remains visible:

```sql
ATTACH DATABASE 'MHCatalogue.db' AS catalogue;
ATTACH DATABASE 'OPEN.db' AS open_ref;
ATTACH DATABASE 'rules.db3' AS rule_db;
```

Resolve the property from the union of its Object and firmware ownership scopes, then retrieve its base range and the filters for the exact Object/firmware association:

```sql
WITH applicable_conf AS (
    SELECT c.*, 'object' AS source_scope
    FROM catalogue.EN_CONF AS c
    WHERE c.id_key_object = :id_key_object
      AND c.id_firmware = 0

    UNION ALL

    SELECT c.*, 'firmware' AS source_scope
    FROM catalogue.EN_CONF AS c
    WHERE c.id_key_object = 0
      AND c.id_firmware = :id_firmware
),
object_firmware AS (
    SELECT id_object_firmware
    FROM catalogue.AS_OBJECT_FIRMWARE
    WHERE id_key_object = :id_key_object
      AND id_firmware = :id_firmware
)
SELECT
    c.source_scope,
    c.id_conf,
    c.conf_name,
    c.descr,
    c.idx,
    c.id_conf_data_type,
    c.hidden,
    c.visible,
    c.read_only,
    r.value,
    r.name AS range_name,
    r."default" AS default_value,
    r.min_value,
    r.max_value,
    r.step,
    r.digit,
    f.id_filter,
    f.whole_range,
    fr.range AS filtered_range
FROM applicable_conf AS c
LEFT JOIN catalogue.EN_CONF_RANGE AS r
  ON r.id_conf = c.id_conf
LEFT JOIN catalogue.EN_FILTER AS f
  ON f.id_conf = c.id_conf
 AND f.id_object_firmware IN (SELECT id_object_firmware FROM object_firmware)
LEFT JOIN catalogue.EN_FILTER_RANGE AS fr
  ON fr.id_filter = f.id_filter
WHERE c.conf_name = :conf_name
   OR c.idx = :index
ORDER BY c.source_scope, c.id_conf, r.progressive;
```

Use the symbol or index only after the Module and Object have been resolved. If both predicates select unrelated properties, narrow the query rather than merging their domains.

Retrieve catalogue conditions for the actual slot:

```sql
SELECT
    s.id_slot,
    s.first_slot,
    sc.id_condition,
    c.condition,
    c.id_conv_rule,
    cr.item_conf,
    cr.item_conf_value,
    cr.object_conf,
    cr.object_conf_value,
    cr.always_true
FROM catalogue.EN_SLOTS AS s
LEFT JOIN catalogue.AS_SLOT_CONDITION AS sc
  ON sc.id_slot = s.id_slot
LEFT JOIN catalogue.EN_CONDITION AS c
  ON c.id_condition = sc.id_condition
LEFT JOIN catalogue.EN_CONV_RULE AS cr
  ON cr.id_conv_rule = c.id_conv_rule
WHERE s.id_object_firmware = :id_object_firmware
  AND s.id_slot = :resolved_id_slot
ORDER BY s.first_slot, sc.id_condition;
```

`:resolved_id_slot` is the exact catalogue placement already resolved for the Module. A comparison such as `internal_slot >= first_slot` would incorrectly include unrelated earlier placements; multi-slot occupancy needs its established Object-specific rule.

Then retrieve complete external rule groups for the same external Object number:

```sql
SELECT
    KOBJECTS,
    N_RULES,
    "1_Parameter" AS controlling_property,
    Condition,
    "2_Parameter" AS affected_property,
    TrueCondition,
    FalseCondition,
    Condition_order
FROM rule_db.rules
WHERE KOBJECTS = :key_object
ORDER BY N_RULES, Condition_order;
```

This correlation is semantic: `:key_object` is `EN_KEY_OBJECT.key_object`, not the catalogue primary key `id_key_object`. Resolve `$N` references in the operands to configuration index `N`, not to `conf_name`. Evaluate complete ordered rule groups rather than selecting isolated rows by display name. No declared foreign key connects these databases.

Finally, inspect the actual `OPEN.db` parameter definition used by the selected write frame:

```sql
SELECT
    o.id_open,
    o.open_label,
    o.open_string,
    p.id_param,
    p.param_string,
    pt.param_type_descr,
    p.min_value,
    p.max_value,
    p.step_value,
    p.pad_value,
    p.num_digit
FROM open_ref.EN_OPEN AS o
JOIN open_ref.AS_OPEN_PARAM AS op
  ON op.id_open = o.id_open
JOIN open_ref.EN_OPEN_PARAM AS p
  ON p.id_param = op.id_param
LEFT JOIN open_ref.EN_PARAM_TYPE AS pt
  ON pt.id_param_type = p.id_param_type
WHERE o.id_open = :id_open
ORDER BY p.id_param;
```

The transport range is only the final encoding envelope. It must not replace the narrower catalogue, filter, condition, or rule-derived domain.

## Required result

Validation returns evidence rather than a Boolean:

- status and reason;
- resolved identifiers;
- base and filtered domains;
- condition and conversion path;
- dependencies;
- semantic input and encoded value;
- physical-representation classification;
- expected read-back.

Fail closed when the property, domain, condition, or encoding is ambiguous.

## Common mistakes

- treating `0..65535` as the allowed value set;
- resolving `INDEX` without Object/firmware context;
- merging filters from unrelated firmware associations;
- assuming a hidden value is invalid;
- assuming a physical counterpart uses the same range;
- validating only the changed property when linked rules depend on others.

See [Programming Validation](../programming/validation.md) for the complete fourteen-milestone resolver.
