# Retrieve an Actuator's Group Memberships

## Goal

Answer the installer or application question: “Which groups does this actuator belong to?”

The result should identify the Physical Device and actuator Module, list its effective group memberships, and retain the raw diagnostic values and catalogue definitions that support the answer.

## Prerequisites

- an inventory entry from [Discover and Identify Devices](discover-devices.md);
- the Device interview and Module/Object model described in [Read and Present a Device Configuration](read-device-configuration.md);
- access to `MHCatalogue.db` and applicable `rules.db3` data;
- the ability to send and receive diagnostic frames as MyHOME_Suite does.

## 1. Identify the Device and actuator Module

Run the Device interview using the installed Device ID, diagnostic address, or local-interaction workflow described in [Read and Present a Device Configuration](read-device-configuration.md).

From the resulting `DIMENSION 30` records:

1. build the complete Module list;
2. retain each protocol internal `SLOT`;
3. resolve configured `KEYO` values against `EN_KEY_OBJECT.key_object`;
4. select the actuator Module whose membership is required;
5. retain its internal `id_key_object` for catalogue joins.

Do not select a Module from its slot number alone. A Physical Device can contain actuator and command Modules with different property sets.

## 2. Request the detailed configuration

After resolving the Device's Module/Object layout, send:

`*#[WHO]*0*38#0##`

Collect the repeated `DIMENSION 35` responses during the MyHOME_Suite eight-second response window:

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

Retain every response as the raw tuple `(SLOT, INDEX, VAL_PAR)`. Do not merge equal indices from different Modules.

## 3. Resolve the group properties

Load the Object-scoped `EN_CONF` rows for the actuator's resolved `id_key_object`, using `id_firmware = 0`.

Select the properties that represent group-membership positions. Several common actuator Objects expose:

| Symbol | Common `INDEX` |
| --- | ---: |
| `G1` | 240 |
| `G2` | 241 |
| … | … |
| `G10` | 249 |

This layout is Object-scoped, not global. Other Objects can use different symbols or indices. Resolve the Object before interpreting any `INDEX`.

For every selected property:

1. match `EN_CONF.idx` to the response `INDEX` for the actuator's `SLOT`;
2. load its `EN_CONF_RANGE`;
3. apply applicable `EN_FILTER`, `EN_FILTER_RANGE`, conditions, and rules;
4. retain the selected `EN_CONF.id_conf` and raw `VAL_PAR`;
5. distinguish a missing response from a reported zero.

## 4. Interpret the memberships

For the common actuator definitions above, the catalogue provides a numeric range of `0` through `255` and a default of `0` for each position.

Suppose internal slot `2` produces these normalized values:

| `SLOT` | `INDEX` | `VAL_PAR` | Resolved property | Result |
| ---: | ---: | ---: | --- | --- |
| 2 | 240 | 7 | `G1` | member of group 7 |
| 2 | 241 | 12 | `G2` | member of group 12 |
| 2 | 242–249 | 0 | `G3`–`G10` | default/unassigned positions, subject to the applicable rules |

The user-facing result is:

> Groups 7 and 12

Retain provenance such as “Module internal slot 2; `G1=7`; `G2=12`.”

The catalogue permits zero and supplies it as the default. Treat zero as an unassigned position only where the applicable Object, filters, rules, or verified application behavior establish that meaning.

## 5. Handle incomplete or ambiguous results

- If the Object cannot be resolved, preserve the raw tuples and do not assume indices `240` through `249`.
- If several compatible `EN_CONF` definitions remain, report the candidate interpretations.
- If an expected group property is not reported, label it “not reported”; do not replace it with zero.
- If a value violates the effective filtered domain, retain it and add a warning.
- If no group-membership properties exist for the resolved Object, report that the Object exposes no catalogue-defined group list through this mechanism.

## Expected result

Return a record such as:

```text
Device ID: 004FBEC8
Module internal slot: 1
Object: Shutter actuator
Groups: [1, 3]
Raw properties:
  G1: INDEX 240, value 1
  G2: INDEX 241, value 3
Resolution status: resolved
```

The Object description is the Module function. Use the resolved `EN_DEVICE.name` separately for the Physical Device description.

See [`DIMENSION 30`](../diagnostics/dim30-modules.md), [`DIMENSION 35`](../diagnostics/dim35-configuration.md), [Configuration](../device-model/configuration.md), and [Configuration Reading](../diagnostics/configuration-reading.md).
