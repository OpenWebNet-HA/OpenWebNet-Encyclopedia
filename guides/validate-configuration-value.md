# Validate a Configuration Value

## Goal

Decide whether one intended semantic value is writable for the resolved Device, firmware, Module, and Object, and derive its wire encoding.

## Acquire the current state

Validation requires the installed context, not only the proposed value.

1. If the Device is not yet identified, execute [Discover and Identify Devices](discover-devices.md).
2. Start a fresh interview with `*[WHO]*10#[ID]*0##`, or the documented address/local alternative.
3. Collect identity, firmware, `DIMENSION 30`, and `DIMENSION 32` responses through Device `WHAT 4` or a classified timeout.
4. After resolving the Module/Object layout, send `*#[WHO]*0*38#0##`.
5. Collect the resulting repeated `DIMENSION 35` values and any `DIMENSION 310` response during the detailed-read window.
6. Transform those raw frames using [Read and Present a Device Configuration](read-device-configuration.md).

Do not validate against a stale or partially identified configuration without marking that limitation.

## Procedure

1. Take the resolved installed Device and firmware from the freshly acquired configuration model.
2. Resolve the internal slot and current Object or Virgin Object.
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
  AND :internal_slot >= s.first_slot
ORDER BY s.first_slot, sc.id_condition;
```

Then retrieve any external rules that refer to the same external Object number and configuration symbol:

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
  AND (
      "1_Parameter" = :conf_name
      OR "2_Parameter" = :conf_name
  )
ORDER BY N_RULES, Condition_order;
```

This correlation is semantic: `:key_object` is `EN_KEY_OBJECT.key_object`, not the catalogue primary key `id_key_object`. No declared foreign key connects these databases.

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

- treating `0–65535` as the allowed value set;
- resolving `INDEX` without Object/firmware context;
- merging filters from unrelated firmware associations;
- assuming a hidden value is invalid;
- assuming a physical counterpart uses the same range;
- validating only the changed property when linked rules depend on others.

See [Programming Validation](../programming/validation.md) for the complete fourteen-milestone resolver.
