# Database Relationship Reconstruction

MyHOME Suite databases vary in how completely they declare relationships. ScenarioDevices declares its principal hierarchy, while many important `MHCatalogue.db` relationships are represented only by association-table structure and complete key coverage.

## Reconstruction criteria

Treat an undeclared relationship as structurally established only when:

1. table and column roles identify a plausible parent;
2. every non-sentinel child value resolves in the canonical revision;
3. cardinality matches the proposed model;
4. dependent association tables, queries, or UI behavior use the same relationship;
5. competing parent tables have been tested and rejected.

Document the relationship; do not modify the canonical database.

## Sentinel-aware validation

Values such as `0`, `NULL`, and negative version components can be implementation sentinels rather than broken references.

`EN_CONF` demonstrates why validation must include discriminator logic:

```text
Object-scoped:
    id_key_object resolves
    id_firmware = 0

Firmware-scoped:
    id_key_object = 0
    id_firmware resolves
```

The database contains no canonical row owned simultaneously by an Object and firmware. Treating both columns as mandatory parents would manufacture thousands of false orphan reports.

## Association paths

Important reconstructed catalogue paths include:

- Device → item, brand, and line;
- item → firmware and catalogue system;
- firmware → Object support;
- firmware/Object support → internal-slot placement;
- firmware → Virgin Object → internal-slot placement;
- Virgin Object → permitted Object;
- configuration definition → base ranges;
- Object/firmware association → contextual filter → filtered ranges;
- slot placement → condition → conversion rule.

Each association row has its own identity. The associated external Object number or internal slot must not be substituted for that row key.

## Relationship checks

Useful checks include:

```sql
SELECT child.parent_id
FROM child
LEFT JOIN parent ON parent.id = child.parent_id
WHERE child.parent_id IS NOT NULL
  AND child.parent_id <> 0
  AND parent.id IS NULL;
```

and cardinality inspection:

```sql
SELECT parent_id, COUNT(*)
FROM child
GROUP BY parent_id
ORDER BY COUNT(*) DESC;
```

These queries establish coverage, not semantics. The proposed relationship still needs an appropriate model and, for cross-database claims, independent corroboration.

## Revision comparison

Never compare databases by local row ID alone. The ScenarioDevices files demonstrate that equivalent semantic rows can acquire different local IDs after additional rows are inserted.

Use a complete semantic path, for example:

```text
Object System resource key and category
→ Device Object resource key and identifiers
→ Command resource key and frame fields
→ Parameter resource key and domain
```

The common ProgramData content is an exact semantic subset of the Program Files revision under that comparison, despite unstable local keys.

## False-positive warning

The rejected `EN_DEVICE.code → EN_LANGUAGE.code` relationship is the canonical failure example. The columns share a name and some values can appear compatible, but `EN_DEVICE.code` contains product codes/SKUs and is not a language reference.

Column-name similarity must never outrank value coverage, table role, and application semantics.
