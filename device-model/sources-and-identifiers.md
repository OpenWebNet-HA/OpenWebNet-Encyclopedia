# Sources and Identifier Boundaries

The Device model is reconstructed from several sources that describe different layers of the implementation. They are complementary, not interchangeable.

## Canonical-source policy

The canonical evidence corpus is under [`sources/`](../sources/). Original evidence is preserved byte-for-byte. Provenance, byte sizes, original installation paths, and SHA-256 fingerprints are recorded in [`sources/manifest.yaml`](../sources/manifest.yaml).

Derived relationships and interpretations belong in documentation, not in the canonical databases.

Private packet captures are intentionally excluded from the repository. Findings supported by them can be documented without publishing installation-specific capture data.

## Evidence matrix

| Source | Strongest evidence | Does not independently establish |
| --- | --- | --- |
| [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Product catalogue, firmware capabilities, internal slots, Objects, Virgin Objects, configuration definitions and constraints | Exact runtime frame order or complete functional protocol |
| [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) | Systems, diagnostic families, frame templates, parameters, address rules, sequences, and timeouts | Complete Device catalogue or complete functional command vocabulary |
| [`OpenQuery.txt`](../sources/myhome-suite/3.5.38/support/OpenQuery.txt) | Queries used by MyHOME_Suite to assemble `OPEN.db` frames, sequences, address rules, and timeouts | Additional semantics absent from the queried tables |
| [ScenarioDevices databases](../sources/myhome-suite/3.5.38/databases/) | Scenario-engine Object systems, actions, triggers, conditions, frames, and parameter limits | Physical Device, firmware, Module, or catalogue Object identity |
| [`rules.db3`](../sources/myhome-suite/3.5.38/databases/rules.db3) | Cross-property validation for selected Temperature Control Objects | General Object registry or functional `WHO` mapping |
| [public OpenWebNet documents](../sources/openwebnet-public/) | Published frame syntax and functional behavior | MyHOME_Suite catalogue hierarchy or unpublished diagnostic semantics |
| Observed traffic | Actual values, ordering, repetition, and Device behavior | Universal support outside the observed Devices and versions |
| MyHOME_Suite UI | Display labels, field visibility, editability, and product-specific behavior | Wire encoding unless correlated with traffic or implementation data |

## Independent identifier spaces

The following identifiers must not be numerically joined without explicit evidence:

| Identifier | Namespace |
| --- | --- |
| `EN_DEVICE.id_device` | Internal Device catalogue record |
| `EN_DEVICE.code` | Product code/SKU |
| `EN_ITEM.id_item` | Shared catalogue capability item |
| `AS_ITEM_SYSTEM.modobj` | Catalogue item model value |
| diagnostic `ID` | Installed Device instance |
| `EN_FIRMWARE.id_firmware` | Catalogue firmware definition |
| `EN_SLOTS.id_slot` | Slot-assignment row |
| `EN_SLOTS.first_slot` | Internal slot position |
| `EN_KEY_OBJECT.id_key_object` | Internal Object database key |
| `EN_KEY_OBJECT.key_object` | Catalogue/Object number |
| `EN_VIRGIN_OBJECT.id_virgin_key_object` | Internal Virgin Object key |
| `EN_VIRGIN_OBJECT.virgin_key_object` | Virgin Object number |
| `EN_CONF.id_conf` | Configuration-definition key |
| `EN_CONF.idx` | Configuration index |
| `EN_SYSTEM.id_system` in `MHCatalogue.db` | Catalogue system |
| `EN_SYSTEM.id_system` in `OPEN.db` | Protocol implementation system record |
| functional `WHO` | OpenWebNet functional namespace |
| diagnostic `WHO` | Management/diagnostic namespace |
| ScenarioDevices `FamilyId`, `ObjectId`, `CommandId` | Scenario-engine namespaces |

Some of these identifiers are correlated by structure and behavior, but correlation must be documented explicitly.

## Supported cross-source correlations

### Diagnostic Device model

`OPEN.db` `DIMENSION 1` uses `OBJECT_MODEL`, `N_CONF`, `BRAND`, and `LINE`.

Supported counterparts and interpretations are:

| Diagnostic field | Catalogue/documentation counterpart | Status |
| --- | --- | --- |
| `OBJECT_MODEL` | `AS_ITEM_SYSTEM.modobj` | Corroborated |
| `BRAND` | `EN_BRAND.brand_modobj` | Corroborated |
| `LINE` | `EN_LINE.line_modobj` | Corroborated |
| `N_CONF` | physical configurator positions shown in product documentation | Corroborated across documented Devices; no direct `MHCatalogue.db` field identified |

`OPEN.db` describes `N_CONF` as the configurator number / number of physical configurators. Product diagrams for Devices including `F420`, `F429`, and `H4652/3` independently match their `N_CONF` values to the number of physical configurator positions. Treat it as a hardware-interface count, not as a Module, Object, Virgin Object, or firmware classification.

### Diagnostic Object identity

| Diagnostic field | Catalogue field | Status |
| --- | --- | --- |
| `DIMENSION 30.KEYO` | `EN_KEY_OBJECT.key_object` | Structurally and behaviorally corroborated |
| `DIMENSION 30.SLOT` | internal slot represented by `EN_SLOTS.first_slot` | Structurally corroborated |
| `DIMENSION 30.STATE` | no single catalogue column | Runtime state; database only labels configured/unconfigured |

### Diagnostic configuration

| Diagnostic field | Catalogue field | Status |
| --- | --- | --- |
| `DIMENSION 35.INDEX` | `EN_CONF.idx` | Strong terminology and behavior correlation |
| `DIMENSION 35.SLOT` | internal slot | Direct structural role |
| `DIMENSION 35.VAL_PAR` | selected `EN_CONF_RANGE.value` or user value | Context-dependent |
| `DIMENSION 310.VAL_PAR` | no generic indexed mapping | Object-specific and unresolved globally |

### Temperature Control validation

`rules.db3.rules.KOBJECTS` values `95`, `96`, and `184` align with catalogue Objects Hotel thermostat, Residential thermostat, and Master probe. Its `$N` parameter references align with those Objects’ `EN_CONF.idx` values.

This is a semantic/structural correlation; the files contain no foreign key.

Cross-source claims in this section are described directly as corroborated, inferred, context-dependent, or unresolved where qualification is necessary.

## Relationship reconstruction

The canonical `MHCatalogue.db` declares only a small subset of its relationships as foreign keys. A relationship can still be treated as structurally established when:

1. the association-table and column names identify the intended parents;
2. every child value resolves to the proposed parent in the canonical dataset;
3. the cardinality is consistent with the model;
4. dependent queries and UI behavior use the same relationship.

This establishes a documentation join, not permission to modify the canonical database.

Notable complete joins include:

- `EN_DEVICE.id_item` → `EN_ITEM.id_item`
- `EN_DEVICE.id_brand` → `EN_BRAND.id_brand`
- `EN_DEVICE.id_line` → `EN_LINE.id_line`
- `EN_FIRMWARE.id_item` → `EN_ITEM.id_item`
- `AS_OBJECT_FIRMWARE` → firmware and Object
- `EN_SLOTS.id_object_firmware` → `AS_OBJECT_FIRMWARE.id_object_firmware`
- firmware/Virgin-Object and Virgin-Object/Object associations
- `EN_CONF_RANGE.id_conf` → `EN_CONF.id_conf`
- `EN_FILTER` → Object/firmware association and configuration definition.

## Known exclusions and cautions

### Device code is not a language relation

`EN_DEVICE.code` contains valid product codes and must not be related to `EN_LANGUAGE.code`. This was a false relationship produced by name similarity.

### Public protocol versus implementation

The public documents can predate implementation behavior found in the databases. A difference must be documented as a source/version difference rather than silently reconciled.

### Scenario Object IDs

ScenarioDevices Object identifiers are application-level capability IDs. They must not be joined directly to catalogue Object numbers.

### System IDs

`EN_SYSTEM.id_system` in `MHCatalogue.db` and `EN_SYSTEM.id_system` in `OPEN.db` describe different registries. Link them through established system semantics, `WHO`, frame templates, or Device/Object evidence—not through equal numeric IDs.

### Counts are source-revision facts

Database row counts document the canonical source revision. They are neither protocol maxima nor claims about all MyHOME products.
