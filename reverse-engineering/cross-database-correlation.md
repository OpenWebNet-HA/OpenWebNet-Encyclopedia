# Cross-Database Correlation

Cross-database work connects meanings, not local primary keys. Each database models a different projection of MyHOME Suite.

## Correlation sequence

Use staged resolution:

1. identify the installed Device and management family from traffic;
2. resolve catalogue item and candidate Physical Devices from `DIMENSION 1`;
3. select firmware using reported version evidence;
4. resolve Module/Object state using `DIMENSION 30`;
5. resolve the Object’s catalogue systems and families;
6. interpret `DIMENSION 32` and `35` in that context;
7. select `OPEN.db` address rules and management frames by established system and family semantics;
8. apply catalogue and `rules.db3` validation;
9. correlate functional behavior or ScenarioDevices actions only after the Object’s functional context is established.

Do not begin with a multi-database SQL join on similarly named integer columns.

## Object-family address-rule relationship

All 11 nonzero `OPEN.db.EN_ADDRESS_RULE.object_device_family` values resolve to `MHCatalogue.db.EN_OBJECT_ITEM_FAMILY.id_family`. Their rule descriptions, family names, and Object membership agree.

The relationship is:

```text
EN_ADDRESS_RULE.object_device_family
    value = 0 → family-unqualified rule
    value != 0 → EN_OBJECT_ITEM_FAMILY.id_family
                    ← EN_KEY_OBJECT.id_family
```

Family membership narrows candidate Objects. It does not replace system, firmware, slot, or condition filtering.

## Candidate mapping for `DIMENSION 32.SYS`

The leading candidate is `MHCatalogue.db.EN_SYSTEM.sys_modobj`.

| Candidate | Assessment |
| --- | --- |
| catalogue `id_system` | local primary key; partially coincident across models |
| `OPEN.db.id_system` | local workflow-registry key |
| functional `WHO` | functional namespace, but not called `SYS` and differs from catalogue grouping |
| diagnostic `WHO` | excluded by `SYS` range `1`–`255` |
| catalogue `xml_key_system` | useful semantic identifier but textual |
| catalogue `sys_modobj` | numeric external/model field associated with Object systems; strongest candidate |

`sys_modobj` values range from `0` through `21`; nonzero values fit the wire field. Multiple system variants can intentionally share one value, while Objects belonging to several systems can have several candidates. A reported `SYS` can therefore select the active system context of a reusable Object.

The mapping remains strongly inferred until a capture distinguishes it from database IDs and functional `WHO`. See [Hypothesis Testing](hypothesis-testing.md).

## Configuration correlation

`DIMENSION 35.INDEX` cannot be joined globally to `EN_CONF.idx`.

The effective lookup key includes:

```text
Physical Device
+ firmware
+ internal slot
+ configured Object
+ Object/firmware ownership scope
+ INDEX
```

Only then can `VAL_PAR` be interpreted through base ranges, contextual filters, conditions, conversions, and linked-property rules.

## Scenario correlation

ScenarioDevices supplies exact functional frames for selected actions, but its Object and Command identifiers remain local to that model.

Safe correlations use:

- parsed literal `WHO`, `WHAT`, `WHERE`, and `DIMENSION` values;
- resource-key semantics corroborated by a literal frame;
- explicit ScenarioDevices matching identifiers inside that model;
- established functional behavior of a resolved catalogue Object.

Do not equate ScenarioDevices `ObjectId` with `EN_KEY_OBJECT.key_object`.

## Result representation

A cross-database correlation should retain both sides:

```text
raw wire value
resolved wire namespace
database file and revision
internal row key
external catalogue identifier
semantic label
conditions and confidence
```

Collapsing these into one integer makes later validation and revision comparison unreliable.
