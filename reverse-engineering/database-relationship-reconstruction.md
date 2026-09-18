# Database Relationship Reconstruction

MyHOME Suite databases vary in how completely they declare relationships. ScenarioDevices declares its principal hierarchy with foreign keys, while many central `MHCatalogue.db` relationships are encoded only by column roles, association tables, and complete key coverage.

Reconstruction documents those relationships without rewriting the canonical evidence.

## Declared, structural, and semantic relationships

Keep three kinds of relationship distinct:

| Kind | Evidence | Example |
| --- | --- | --- |
| Declared | SQLite foreign key or primary-key structure | ScenarioDevices `Commands.DeviceObject_Id → DeviceObjects.Id` |
| Structurally reconstructed | complete key coverage, compatible cardinality, and table role | `EN_DEVICE.id_item → EN_ITEM.id_item` |
| Semantic/cross-model | independent models connected by meaning rather than a database key | `DIMENSION 1.OBJECT_MODEL → AS_ITEM_SYSTEM.modobj` |

A structurally reconstructed relationship can be safe for analysis without being declared by SQLite. A cross-model relationship needs stronger semantic corroboration and must not be presented as a foreign key.

## Reconstruction workflow

For every proposed relationship:

1. identify the child and candidate parent namespaces;
2. inspect types, nullability, defaults, and declared constraints;
3. enumerate sentinel values before counting orphans;
4. test every populated non-sentinel value;
5. measure cardinality and duplicate parent candidates;
6. inspect association-table paths that depend on the relationship;
7. test competing parents and same-named columns;
8. seek an independent query, frame, UI, or product interpretation;
9. record scope, exceptions, confidence, and a falsifier;
10. add stable results to the [Relationship Register](relationship-register.md).

## Schema and source inspection

Start from the stored schema, not an ORM-style model inferred from names:

```sql
SELECT type, name, tbl_name, sql
FROM sqlite_master
WHERE type IN ('table', 'view', 'index', 'trigger')
ORDER BY type, name;
```

Inspect each candidate table:

```sql
PRAGMA table_info('EN_DEVICE');
PRAGMA foreign_key_list('EN_DEVICE');
PRAGMA index_list('EN_DEVICE');
```

The absence of a declared foreign key is a fact about enforcement, not proof that no application relationship exists.

## Sentinel-aware orphan testing

Do not classify a value as an orphan until its sentinel role has been tested.

```sql
SELECT c.parent_id, COUNT(*) AS occurrences
FROM child AS c
LEFT JOIN parent AS p ON p.id = c.parent_id
WHERE c.parent_id IS NOT NULL
  AND c.parent_id <> 0
  AND p.id IS NULL
GROUP BY c.parent_id;
```

Common patterns in the corpus include:

| Value pattern | Established use |
| --- | --- |
| `NULL` | absent/unknown where the column permits it |
| `0` | “not applicable” discriminator in `EN_CONF` ownership; family-unqualified address rule |
| `-1` | any/unspecified firmware component in strongly corroborated `V.R.b` patterns |
| empty text | distinct from `NULL`; sometimes an unused expression or label |

Sentinel meaning is column-specific. Never create a global rule that every `0` or `-1` has the same semantics.

## Polymorphic ownership: `EN_CONF`

`EN_CONF` demonstrates why ordinary foreign-key assumptions can be destructive:

```text
Object-scoped:
    id_key_object resolves
    id_firmware = 0

Firmware-scoped:
    id_key_object = 0
    id_firmware resolves
```

In the canonical database:

| Ownership pattern | Rows |
| --- | ---: |
| Object-scoped | 1,420 |
| Firmware-scoped | 1,463 |
| both parents populated | 0 |
| both parents zero | 0 |

The zero is part of an exclusive discriminator. Treating both parent columns as mandatory would manufacture false orphans and erase the data model.

## Verified catalogue relationships

The following full-coverage checks hold for MyHOME Suite 3.5.38:

| Child relationship | Rows checked | Non-sentinel orphans |
| --- | ---: | ---: |
| `EN_DEVICE.id_item → EN_ITEM.id_item` | 541 | 0 |
| `EN_DEVICE.id_brand → EN_BRAND.id_brand` | 541 | 0 |
| `EN_DEVICE.id_line → EN_LINE.id_line` | 541 | 0 |
| `EN_FIRMWARE.id_item → EN_ITEM.id_item` | 311 | 0 |
| `EN_BUILDS.id_firmware → EN_FIRMWARE.id_firmware` | 308 | 0 |
| `AS_ITEM_SYSTEM.id_item → EN_ITEM.id_item` | 223 | 0 |
| `AS_ITEM_SYSTEM.id_system → EN_SYSTEM.id_system` | 223 | 0 |
| `AS_OBJECT_SYSTEM.id_key_object → EN_KEY_OBJECT.id_key_object` | 251 | 0 |
| `AS_OBJECT_SYSTEM.id_system → EN_SYSTEM.id_system` | 251 | 0 |
| `AS_OBJECT_FIRMWARE` to firmware and Object parents | 827 | 0 |
| `EN_SLOTS.id_object_firmware → AS_OBJECT_FIRMWARE.id_object_firmware` | 1,725 | 0 |
| `EN_KEY_OBJECT.id_family → EN_OBJECT_ITEM_FAMILY.id_family` | 158 | 0 |
| `AS_FIRMWARE_VIRGIN_OBJECT` to both parents | 75 | 0 |
| `AS_OBJECT_VIRGIN_OBJECT` to both parents | 102 | 0 |
| `EN_CONF_RANGE.id_conf → EN_CONF.id_conf` | 14,346 | 0 |
| `EN_FILTER` to Object/firmware association and configuration | 1,909 | 0 |
| `AS_SLOT_CONDITION` to slot and condition | 1,000 | 0 |

These counts establish revision-specific structural integrity. Semantics come from the complete capability paths and their use in diagnostics, programming, and UI behavior.

## Association paths and row identities

Important capability paths include:

```text
Device → shared item → firmware → Object support → slot placement
```

```text
firmware → Virgin Object support → permitted Object set → slot placement
```

```text
configuration definition
→ base range
→ Object/firmware contextual filter
→ filtered range
```

```text
slot placement → condition → conversion rule
```

Each association has its own identity and scope. For example:

- `AS_OBJECT_FIRMWARE.id_object_firmware` is not an Object number;
- `EN_SLOTS.id_slot` is not the Device-local slot carried on the wire;
- `EN_KEY_OBJECT.id_key_object` is not `EN_KEY_OBJECT.key_object`;
- an `EN_FILTER.id_filter` must be interpreted in its Object/firmware association context.

Substituting an external identifier for an association-row key can produce apparently valid but semantically unrelated joins.

## Cardinality testing

Measure both directions:

```sql
SELECT id_item, COUNT(*) AS device_rows
FROM EN_DEVICE
GROUP BY id_item
ORDER BY device_rows DESC;
```

This reveals that several marketed Device/SKU records can share one capability item. The relationship is many Devices to one item, not a unique product lookup.

Likewise, count distinct internal positions separately from association rows:

```sql
SELECT ofw.id_firmware,
       COUNT(s.id_slot) AS association_rows,
       COUNT(DISTINCT s.first_slot) AS internal_slots
FROM AS_OBJECT_FIRMWARE AS ofw
JOIN EN_SLOTS AS s
  ON s.id_object_firmware = ofw.id_object_firmware
GROUP BY ofw.id_firmware;
```

One slot can offer several Object alternatives. `COUNT(EN_SLOTS rows)` is therefore not the firmware Module count.

## Conditions and indirect relationships

Not every relationship is a direct equality join. Conditions, symbols, and conversion rules can reference configuration concepts textually or through a chain of associations.

For these cases, require:

- an unambiguous owning firmware/Object/slot context;
- a parsed expression or symbol namespace;
- resolution of every referenced property;
- documented evaluation order;
- runtime/UI corroboration where behavior is claimed.

Do not convert textual references into foreign keys merely because a number appears inside the expression.

## Cross-database reconstruction

Independent SQLite files do not share primary-key namespaces. A cross-database relationship must state whether it connects:

- an external number intentionally reused across models;
- a parsed wire value to catalogue metadata;
- a resource-key semantic path;
- a functional `WHO` extracted from a literal frame;
- a revision-specific data pattern.

For example, all 11 nonzero `OPEN.db.EN_ADDRESS_RULE.object_device_family` values resolve to `MHCatalogue.db.EN_OBJECT_ITEM_FAMILY.id_family`, and the rule descriptions agree with family membership. This is a structurally and semantically corroborated cross-model relationship—not a declared foreign key.

See [Cross-Database Correlation](cross-database-correlation.md) for the staged resolution rules.

## Revision comparison

Never align two database revisions by local row ID alone. Compare the complete semantic path:

```text
Object System resource key and category
→ Device Object resource key and external identifiers
→ Command resource key and frame semantics
→ Parameter resource key, domain, and placeholder
```

Using this method, the common ScenarioDevices ProgramData content is an exact semantic subset of the Program Files copy despite divergent local IDs.

Report revision comparison as additions, removals, changed semantic rows, and unchanged semantic rows. Do not describe ID renumbering as a capability change.

## Preserve the canonical evidence

Do not add inferred foreign keys to the distributed databases. Apart from changing the source hash, doing so can impose false deletion/update behavior and mishandle sentinels.

If a derived constraint-enabled database is useful, label it as generated and publish:

- source hash;
- transformation script;
- sentinel/exclusion rules;
- orphan report;
- generated schema hash;
- explicit warning that it is not the canonical MyHOME Suite file.

## False-positive example

`EN_DEVICE.code → EN_LANGUAGE.code` is the canonical failure. The columns share the name `code`, and selected values can appear compatible, but `EN_DEVICE.code` stores product codes/SKUs. Table role and semantics reject the relationship.

Column-name similarity must never outrank namespace, coverage, cardinality, and application meaning.
