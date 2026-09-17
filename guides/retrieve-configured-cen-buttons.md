# Retrieve Configured CEN Buttons

## Goal

Answer the installer or application question: “Which CEN buttons are configured on this Physical Device?”

Starting only with a way to select the installed Device, this guide obtains the raw frames, resolves every Module and Object, identifies CEN-capable Objects, and returns each configured button with its CEN identifier and provenance.

## Prerequisites

- a Device selector: preferably its discovered 32-bit ID, otherwise a diagnostic address or local-interaction workflow;
- the applicable diagnostic `WHO`;
- access to `MHCatalogue.db` and applicable `rules.db3` data;
- the ability to establish the required session and send and receive frames as MyHOME_Suite does;
- raw frames retained in arrival order.

No previously captured interview or configuration response is assumed.

## 1. Interview the selected Device

Start one of these selection workflows:

| Selection method | Send |
| --- | --- |
| Device ID | `*[WHO]*10#[ID]*0##` |
| diagnostic address | `*#[WHO]*[WHERE]*0##` |
| local interaction | `*[WHO]*5*0##`, then perform the Device-side interaction |

A Device ID is represented as eight hexadecimal characters.

Collect the initial stream in arrival order. The frames needed by this guide are:

- `DIMENSION 1` for catalogue identity;
- `DIMENSION 2`, `3`, and `6` where reported, for firmware resolution;
- repeated `DIMENSION 30` records for the Module/Object layout;
- `DIMENSION 13` for the installed Device ID;
- applicable `DIMENSION 31` errors;
- Device `WHAT 4` as the normal interview terminator.

Use the applicable 15-second first-response window for ID/address selection or the 300-second local-interaction window, followed by the 20-second further-information window used by MyHOME_Suite. Record whether `WHAT 4`, abort, timeout, or transport closure ended collection.

## 2. Resolve the Device, Modules, and Objects

Resolve `DIMENSION 1` through the catalogue and use `EN_DEVICE.name` as the preferred Physical Device description. Retain candidate brands, collections, SKUs, and firmware when identity is not unique.

Parse every Module record:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

For each response:

1. use protocol `SLOT` as the Device-local internal-slot key;
2. if `STATE=1`, resolve `KEYO` against `EN_KEY_OBJECT.key_object`;
3. if `STATE=0`, resolve it against `EN_VIRGIN_OBJECT.virgin_key_object` and mark the Module unconfigured;
4. retain the configured Object's internal `id_key_object`;
5. attach any `DIMENSION 31` error without discarding a valid Module record.

This is a Device-wide question. Do not stop after the first scenario-related Module, and do not renumber internal slots to match MyHOME_Suite's visible Module numbering.

## 3. Identify CEN-capable Object properties

For every configured Module, load both applicable configuration scopes:

- Object-scoped `EN_CONF` rows using its `id_key_object` and `id_firmware = 0`;
- firmware-scoped rows using `id_key_object = 0` and the resolved firmware.

The zero is a “not applicable” sentinel on the unused ownership axis.

Identify definitions whose resolved semantics represent:

- the CEN or Scheduled scenario PLUS number;
- an upper, lower, or numbered button;
- any Object-specific component required to decode those values.

Use property identity and semantics, not matching numeric values or a global index list. CEN-capable Objects do not all expose the same properties.

### SQL example: find the CEN properties for each resolved Object

Resolve each configured `KEYO` first:

```sql
SELECT id_key_object, key_object, descr
FROM EN_KEY_OBJECT
WHERE key_object = :reported_keyo;
```

For that resolved Object and firmware, inspect the actual property definitions rather than assuming the indices used by one Object variant:

```sql
WITH applicable_conf AS (
    SELECT c.*, 'object' AS source_scope
    FROM EN_CONF AS c
    WHERE c.id_key_object = :id_key_object
      AND c.id_firmware = 0

    UNION ALL

    SELECT c.*, 'firmware' AS source_scope
    FROM EN_CONF AS c
    WHERE c.id_key_object = 0
      AND c.id_firmware = :id_firmware
)
SELECT
    source_scope,
    id_conf,
    conf_name,
    descr,
    idx,
    id_conf_data_type,
    hidden,
    visible,
    read_only
FROM applicable_conf
WHERE upper(conf_name) LIKE '%CEN%'
   OR upper(conf_name) LIKE '%BUTTON%'
   OR upper(conf_name) LIKE '%BUTT%'
   OR upper(descr) LIKE '%CEN%'
   OR upper(descr) LIKE '%BUTTON%'
ORDER BY idx, id_conf;
```

The text predicates produce candidates for semantic review; they do not themselves prove that a property is part of a CEN address. Retain only definitions compatible with the resolved Object.

Retrieve the base domains and the filters for the exact Object/firmware association:

```sql
SELECT
    c.id_conf,
    c.conf_name,
    c.idx,
    r.value,
    r.name AS range_name,
    r."default" AS default_value,
    r.min_value,
    r.max_value,
    r.step,
    f.id_filter,
    f.whole_range,
    fr.range AS filtered_range
FROM EN_CONF AS c
LEFT JOIN EN_CONF_RANGE AS r
  ON r.id_conf = c.id_conf
LEFT JOIN AS_OBJECT_FIRMWARE AS aof
  ON aof.id_key_object = :id_key_object
 AND aof.id_firmware = :id_firmware
LEFT JOIN EN_FILTER AS f
  ON f.id_conf = c.id_conf
 AND f.id_object_firmware = aof.id_object_firmware
LEFT JOIN EN_FILTER_RANGE AS fr
  ON fr.id_filter = f.id_filter
WHERE c.id_conf IN (:cen_low_id_conf, :cen_high_id_conf,
                    :button_1_id_conf, :button_2_id_conf)
ORDER BY c.idx, r.progressive;
```

If a variant has fewer properties, omit the absent `id_conf` parameters rather than binding an invented row.

If `rules.db3` is separate, attach it before checking for Object-specific dependencies:

```sql
ATTACH DATABASE 'rules.db3' AS rule_db;

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
      upper("1_Parameter") LIKE '%CEN%'
      OR upper("1_Parameter") LIKE '%BUTTON%'
      OR upper("2_Parameter") LIKE '%CEN%'
      OR upper("2_Parameter") LIKE '%BUTTON%'
  )
ORDER BY N_RULES, Condition_order;
```

Here `:key_object` is the external `EN_KEY_OBJECT.key_object`, not `id_key_object`. This is a semantic cross-database correlation; the files declare no foreign key between those columns.

## 4. Request the detailed configuration

After the complete Module/Object layout is known, send once:

`*#[WHO]*0*38#0##`

Collect the repeated responses during the MyHOME_Suite eight-second response window:

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

Join each response to a property through the resolved Module and `(SLOT, INDEX)`. Equal indices on different Modules remain separate values.

Retain applicable `DIMENSION 39` property errors. Keep any `DIMENSION 310` response outside the generic indexed-property model because it carries no `INDEX`.

A one-Module `DIMENSION 38` form exists, but the canonical `DiagKO` sequence uses the all-Module request above. The source also uses reset terminology for `DIMENSION 38`; preserve that ambiguity and exercise caution with unfamiliar Devices.

## Reference algorithm

```text
function retrieve_cen_buttons(selector):
    interview = acquire_complete_interview(selector)
    context = resolve_device_firmware_modules_and_objects(interview)
    candidates = []

    for module in context.modules:
        if module is not configured or module.object is unresolved:
            continue

        definitions = resolve_applicable_EN_CONF(
            module.object.id_key_object,
            context.firmware.id_firmware
        )

        semantic_set = identify_established_cen_and_button_properties(definitions)
        if semantic_set contains a CEN identity and at least one button:
            candidates.append(module, semantic_set)

    detailed = acquire_DIMENSION_35_with_DIMENSION_38()
    output = []

    for module, semantic_set in candidates:
        values = map responses by (module.internal_slot, property.idx)

        cen = decode_cen_components_only_with_established_rule(values, semantic_set)
        buttons = []

        for button_property in semantic_set.button_properties:
            response = values[button_property.idx]
            buttons.append(
                decode_or_mark_not_reported(button_property, response)
            )

        output.append(module, cen, buttons, raw tuples, statuses)

    return output for every candidate Module,
           including partial and ambiguous entries
```

Do not decide that a Module is CEN-capable merely because it reports indices `0` through `3`. Those indices recur on unrelated Objects; the resolved Object and its property definitions establish the semantics.

## 5. Decode a two-button Scheduled scenario PLUS Object

The catalogue defines one two-button “Scheduled scenario PLUS” Object with this Object-scoped property set:

| `INDEX` | Symbol | Meaning |
| ---: | --- | --- |
| 0 | `PPT_CEN_LOW` | low component of the Scheduled scenario PLUS/CEN number |
| 1 | `PPT_CEN_HIG` | high component of the Scheduled scenario PLUS/CEN number |
| 2 | `BUTTON_1` | upper button |
| 3 | `BUTTON_2` | lower button |

Suppose the detailed read yields:

| `SLOT` | low | high | upper button | lower button |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 33 | 0 | 5 | 6 |
| 4 | 33 | 0 | 7 | 8 |

The user-facing result is:

- CEN 33, Module internal slot 3: upper button 5; lower button 6;
- CEN 33, Module internal slot 4: upper button 7; lower button 8.

Retain the four raw `DIMENSION 35` tuples behind each Module result.

## 6. Combine and validate the values

For each selected property:

1. load `EN_CONF_RANGE`;
2. apply applicable `EN_FILTER`, `EN_FILTER_RANGE`, conditions, conversion rules, and `rules.db3` dependencies;
3. retain the selected `EN_CONF.id_conf`, raw `VAL_PAR`, and decoded value;
4. flag values outside the effective domain rather than discarding them.

The `LOW` and `HIG` names and catalogue ranges strongly indicate byte components. Where the combination rule has been independently established for the applicable Device family, decode them as:

`CEN = LOW + 256 × HIG`

Otherwise, show both raw components and mark the combined number as an evidence-backed inference. Do not silently promote the formula to a universal protocol rule.

CEN virtual addresses occupy the range `0` through `2047`; the effective Object, filter, and rule constraints still apply.

## 7. Handle Object variants and missing evidence

Do not apply the four indices above to every CEN-capable Object.

For example:

- another “Scheduled scenario PLUS” Object variant exposes only one `BUTTON_1`;
- “Scheduled scenario” and “Scenario module control” Objects use other symbols and layouts;
- a property absent from the resolved Object definition is not the same as a property reported as zero;
- a defined property with no response is “not reported,” not automatically unconfigured.

Also:

- if the interview does not terminate normally, return the partial result with its completion status;
- if Device, firmware, Object, or property resolution remains ambiguous, retain all compatible candidates;
- if a value violates its effective domain, preserve it with a warning;
- if no configured Object exposes CEN-button properties, return an empty list with the successful interview and resolution evidence.

## 8. Build the result

Return one entry per applicable Module:

| Field | Purpose |
| --- | --- |
| Device ID | identifies the installed Physical Device |
| Device | preferred `EN_DEVICE.name` |
| internal slot | preserves the protocol Module key |
| Object | identifies the configured Module function |
| CEN number | decoded identifier, or raw low/high components |
| buttons | Object-defined button names and decoded values |
| raw properties | exact `INDEX` and `VAL_PAR` tuples |
| status | resolved, inferred, ambiguous, not reported, or error |
| provenance | selected `id_key_object` and `id_conf` records |

## Expected result

```text
Device ID: 007B269D
Device: <resolved EN_DEVICE.name>
CEN Modules:
  - internal slot 3
    Object: Scheduled scenario PLUS
    CEN: 33
    upper button: 5
    lower button: 6
  - internal slot 4
    Object: Scheduled scenario PLUS
    CEN: 33
    upper button: 7
    lower button: 8
Interview status: complete
Resolution status: resolved
```

See [Device Discovery](../diagnostics/device-discovery.md), [Device Interview](../diagnostics/device-interview.md), [`DIMENSION 30`](../diagnostics/dim30-modules.md), [`DIMENSION 35`](../diagnostics/dim35-configuration.md), [Configuration](../device-model/configuration.md), and [Diagnostics](../diagnostics/README.md).
