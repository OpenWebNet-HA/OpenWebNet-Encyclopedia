# Retrieve an Actuator's Group Memberships

## Goal

Answer the installer or application question: “Which groups does this actuator belong to?”

Starting only with a way to select the installed Physical Device, this guide obtains the required raw frames, identifies the actuator Module and Object, resolves its group properties, and produces a user-presentable membership list.

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

A Device ID is displayed as eight hexadecimal characters. Encode the frame field as the decimal 32-bit transport value; do not send the hexadecimal display string.

Collect the initial stream in arrival order. The frames needed by this guide are:

- `DIMENSION 1` for catalogue identity;
- `DIMENSION 2`, `3`, and `6` where reported, for Firmware resolution;
- repeated `DIMENSION 30` records for the Module/Object layout;
- `DIMENSION 13` for the installed Device ID;
- applicable `DIMENSION 31` errors;
- Device `WHAT 4` as the normal interview terminator.

Use the applicable 15-second first-response window for ID/address selection or the 300-second local-interaction window, followed by the 20-second further-information window used by MyHOME_Suite. Record whether `WHAT 4`, abort, timeout, or transport closure ended collection.

## 2. Resolve the Device, Modules, and Objects

Resolve `DIMENSION 1` through the catalogue and use `EN_DEVICE.name` as the preferred Physical Device description. Retain candidate brands, collections, SKUs, and Firmware when identity is not unique.

Parse every Module record:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

For each response:

1. use protocol `SLOT` as the Device-local `slot` key;
2. if `STATE=1`, resolve `KEYO` against `EN_KEY_OBJECT.key_object`;
3. if `STATE=0`, resolve it against `EN_VIRGIN_OBJECT.virgin_key_object` and mark the Module unconfigured;
4. retain the resolved Object's internal `id_key_object`;
5. attach any `DIMENSION 31` error without discarding a valid Module record.

Select the actuator Module requested by the user. Do not select it from `slot` number alone: one Physical Device can contain actuator and command Modules with different property sets. If several actuator Modules match and the user has not supplied a distinguishing channel or address, return the candidates rather than guessing.

## 3. Request the detailed configuration

After resolving the complete Module/Object layout, send:

`*#[WHO]*0*38#0##`

Proceed only where this operation's effects are established for the target family and Firmware. `OPEN.db` uses it for `DiagKO` retrieval but labels it reset/select; the corpus does not establish universal non-destructive behavior. Otherwise classify group read-back as unresolved and stop before this request. See the canonical [Detailed Configuration Reading](../diagnostics/dim35-configuration.md#reading-detailed-parameters) treatment.

Collect the repeated responses during the MyHOME_Suite eight-second response window:

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

Retain every raw tuple `(SLOT, INDEX, VAL_PAR)`. Do not merge equal indices from different Modules. Also retain applicable `DIMENSION 39` property errors and any `DIMENSION 310` response separately; `DIMENSION 310` has no generic `INDEX`.

A one-Module `DIMENSION 38` form exists, but the canonical `DiagKO` sequence uses the all-Module request above. The source also uses reset terminology for `DIMENSION 38`; preserve that ambiguity and exercise caution with unfamiliar Devices.

## 4. Resolve the group properties

Load both configuration scopes applicable to the selected Module:

- Object-scoped `EN_CONF` rows with its `id_key_object` and `id_firmware = 0`;
- Firmware-scoped rows with `id_key_object = 0` and the resolved Firmware.

The zero is a “not applicable” sentinel on the unused ownership axis.

Select the definitions that represent group-membership positions. Several common actuator Objects expose:

| Symbol | Common `INDEX` |
| --- | ---: |
| `G1` | 240 |
| `G2` | 241 |
| … | … |
| `G10` | 249 |

This layout is Object-scoped, not global. Other Objects can use different symbols or indices. Resolve the Object before interpreting any `INDEX`.

For every selected property:

1. match `EN_CONF.idx` to `INDEX` for the selected internal `SLOT`;
2. load its `EN_CONF_RANGE`;
3. apply applicable `EN_FILTER`, `EN_FILTER_RANGE`, conditions, conversion rules, and `rules.db3` dependencies;
4. retain `EN_CONF.id_conf`, the raw response, and the decoded value;
5. distinguish a missing response from a reported zero.

### SQL example: resolve and constrain the group properties

First resolve the configured Object reported by `DIMENSION 30`:

```sql
SELECT id_key_object, key_object, descr
FROM EN_KEY_OBJECT
WHERE key_object = :reported_keyo;
```

Then retrieve the Object- and Firmware-scoped definitions, their base ranges, and the filters for the exact Object/Firmware pairing:

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
),
object_firmware AS (
    SELECT id_object_firmware
    FROM AS_OBJECT_FIRMWARE
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
    f.id_filter,
    f.whole_range,
    fr.range AS filtered_range
FROM applicable_conf AS c
LEFT JOIN EN_CONF_RANGE AS r
  ON r.id_conf = c.id_conf
LEFT JOIN EN_FILTER AS f
  ON f.id_conf = c.id_conf
 AND f.id_object_firmware IN (SELECT id_object_firmware FROM object_firmware)
LEFT JOIN EN_FILTER_RANGE AS fr
  ON fr.id_filter = f.id_filter
WHERE c.conf_name IN ('G1', 'G2', 'G3', 'G4', 'G5',
                      'G6', 'G7', 'G8', 'G9', 'G10')
ORDER BY c.idx, r.progressive;
```

If `rules.db3` is a separate file, attach it explicitly before testing for additional dependencies:

```sql
ATTACH DATABASE 'rules.db3' AS rule_db;

SELECT *
FROM rule_db.rules
WHERE KOBJECTS = :key_object
ORDER BY N_RULES, Condition_order;
```

The canonical rule database covers Objects `95`, `96`, and `184`. Its operands use `$N` configuration-index references, not names such as `G1`; load complete groups and evaluate applicable dependencies. An empty result is expected for Objects outside that coverage.

Here `:id_key_object` is the internal catalogue key, while `:key_object` is the external Object number reported on the wire. Do not interchange them.

## Reference algorithm

```text
function retrieve_groups(selector, requested_actuator):
    interview = acquire_complete_interview(selector)
    context = resolve_device_firmware_modules_and_objects(interview)

    actuator = select_actuator(context.modules, requested_actuator)
    if actuator is not unique:
        return ambiguous_actuator_candidates(actuator)

    if DIMENSION 38 effects are not established for the target family and Firmware:
        return unresolved_group_read_back without sending DIMENSION 38

    detailed = acquire_DIMENSION_35_with_DIMENSION_38()

    definitions = resolve_applicable_EN_CONF(
        actuator.object.id_key_object,
        context.firmware.id_firmware
    )

    group_positions = definitions whose established semantics are group membership
    result = []

    for property in group_positions ordered by property position:
        responses = detailed where
            SLOT == actuator.internal_slot and INDEX == property.idx

        if responses is empty:
            retain(property, status = "not reported")
            continue

        if responses contains conflicting values:
            retain_all(property, status = "conflicting responses")
            continue

        decoded = apply_range_filters_conditions_rules(property, responses[0])

        if decoded is established as unassigned:
            retain(decoded, status = "unassigned")
        else:
            result.append(decoded.group_identifier)

    return unique memberships in property order,
           plus every raw position and resolution status
```

Do not deduplicate raw property positions when two positions contain the same group number. The user-facing membership list can contain one group once, but provenance must show that the Device reported the duplicate assignment.

## 5. Interpret the memberships

For the common actuator definitions above, the catalogue provides the numeric range `0..255` and a default of `0` for each position.

Suppose `slot` `2` produces:

| `SLOT` | `INDEX` | `VAL_PAR` | Resolved property | Result |
| ---: | ---: | ---: | --- | --- |
| 2 | 240 | 7 | `G1` | member of group 7 |
| 2 | 241 | 12 | `G2` | member of group 12 |
| 2 | `242..249` | 0 | `G3..G10` | default/unassigned positions, subject to applicable rules |

The user-facing result is “Groups 7 and 12.” Retain provenance such as “Module `slot` 2; `G1=7`; `G2=12`.”

The catalogue permits zero and supplies it as the default. Treat zero as unassigned only where the applicable Object, filters, rules, or verified application behavior establish that meaning.

## 6. Handle incomplete or ambiguous results

- If the interview does not terminate normally, return the partial result with its completion status.
- If Device or Firmware identity remains ambiguous, retain all compatible catalogue candidates.
- If the Object cannot be resolved, preserve the raw tuples and do not assume indices `240..249`.
- If several compatible `EN_CONF` definitions remain, report the candidate interpretations.
- If an expected group property is not reported, label it “not reported”; do not replace it with zero.
- If a value violates the effective filtered domain, retain it and add a warning.
- If no membership properties exist for the resolved Object, report that the Object exposes no catalogue-defined group list through this mechanism.

## Close the diagnostic session

After detailed collection, send `*[WHO]*6*0##` before selecting another Device. Put cleanup in a finally-equivalent path and record whether it was sent or transport failure prevented it. `WHAT 4` ends the initial Device transmission; it does not replace this outer close.

## Expected result

```text
Device ID: 004FBEC8
Device: <resolved EN_DEVICE.name>
Module `slot`: 1
Object: Shutter actuator
Groups: [1, 3]
Raw properties:
  G1: INDEX 240, value 1
  G2: INDEX 241, value 3
Interview status: complete
Resolution status: resolved
```

The Object description is the Module function; it does not replace the Physical Device description.

See [Device Discovery](../diagnostics/device-discovery.md), [Device Interview](../diagnostics/device-interview.md), [`DIMENSION 30`](../diagnostics/dim30-modules.md), [`DIMENSION 35`](../diagnostics/dim35-configuration.md), [Configuration](../device-model/configuration.md), and [Diagnostics](../diagnostics/README.md).
