# MyHOME Suite Project and Plant Templates

The original MyHOME Suite 3.5.38 installer contains two separate SQLite templates, `MHPrj.db` and `PTDB.db`. Their declared structures describe project Objects, Devices, configuration/state records and spatial host associations. They contain no populated user project or installed Device inventory.

These files are application persistence sources. Their local identifiers do not automatically join to catalogue keys, physical Device identifiers, WHO values or the [ScenarioSuite schema](../scenario-engine/scenario-suite-database.md).

## Source identities

Both original members are under installer path `default/resTargetDir2/db/`. They are registered as private canonical evidence in the [artifact manifest](../sources/artifact-manifest.yaml).

| Source / artifact ID | Bytes | SHA-256 |
| --- | ---: | --- |
| `MHPrj.db` / `myhome-suite-3.5.38-mhprj` | 50176 | `74fc3762e47718da40f85562225fb676932349e39bd797ff94a073b8db8bd39a` |
| `PTDB.db` / `myhome-suite-3.5.38-ptdb` | 17408 | `606f0fef30b8db6c5a2998ae5ef88d7193488479ad97f7aea89c8f274c41ae64` |

| Structural inventory | MHPrj | PTDB |
| --- | ---: | ---: |
| Tables, including SQLite bookkeeping where present | 19 | 8 |
| Declared foreign-key rows | 22 | 6 |
| Empty tables | 17 | 5 |
| Shipped reference/seed rows | 6 | 32 |

Read-only integrity and foreign-key checks pass for these exact small datasets. This does not prove application enforcement settings or validate every populated-project operation. The declared constraints and shipped seeds are evidence of structure, not exercised application behavior.

## Project record structure

`MHPrj.db` declares a local relationship graph:

| Record group | Declared relationship | Boundary |
| --- | --- | --- |
| `RT_SYSTEM` | References `RT_BUS` | Database system/bus IDs are not automatically functional WHO values |
| `RT_DEVICE` | References a system and collection box | Separate local Device record |
| `RT_AS_KO_DEVICE` | References both `RT_DEVICE` and `RT_OBJECT` | Composite association key; no universal one-Object-per-Device rule follows |
| `RT_OBJECT` | References a collection and room; separately stores `id_rt_object`, `key_object` and `slot` | Local row ID, stored key and slot remain separate concepts |
| `RT_DEVICE_CONF` / `RT_OBJECT_CONF` | Reference their respective owner records | Configuration keys are scoped by owning row ID |
| `RT_DEVICE_STATE` / `RT_OBJECT_STATE` | Reference their owner and `RT_AS_AREA_TYPE` | Distinct state records, without observed installed state |
| `RT_AS_AREA_DEVICE_CODE` | References a Device and area association | No populated example is supplied |

The original Object room reference declares `ON DELETE SET DEFAULT`, with default room `1`. The shipped room table has a seed with `id_room=1`. This establishes the fallback declaration and seed relationship; no deletion or default assignment was executed. Other seed enum values retain unknown meaning.

`RT_PROJECT`, Device/Object/configuration/state/association/bus/system tables are empty. Only five `DB_INFO` rows and the room seed are populated. Metadata values `V=7`, `R=0`, `DATA_V=4`, `DATA_R=4`, `DATA_B=0` are preserved as database-local facts; their operational interpretation is unresolved and they are not product Firmware versions.

## Spatial and host structure

`PTDB.db` declares `EN_AREA` references to separate area-type and area-category tables. `AS_AREA_HOST` references area and host, with composite key `(area_id,host_id,progressive)`; the meaning/order policy of the third component is unresolved. `AS_AREA_RELATIONSHIP` declares separate parent and child references to areas, without establishing the complete application hierarchy-validation policy.

| Area-type ID | Stored label |
| ---: | --- |
| 1 | District |
| 2 | Building |
| 3 | Raiser |
| 4 | Floor |
| 5 | Indoor/Apartment |
| 6 | Common Areas |
| 7 | Technical Areas |
| 8 | Hotel Room |

`Raiser` is the original spelling. Categories `1..6` separately label Single room, Twin room, Double room, Triple room, Quadruple room and Suite. These spatial/type IDs are not the ScenarioSuite Start/OnlyIf/Action area IDs.

Area, host and association tables are empty. The shipped populated data comprises eight types, six categories and eighteen plant-metadata rows; `sqlite_sequence` is empty. The plant metadata contains `db_ver='2.0'`, a separate source version label. Credential-bearing schema defaults and populated plant network/GUID/identifier/contact values are withheld. Ordinary structural defaults remain recorded.

## Cross-source and execution limits

No cross-file constraint or populated bridge establishes a join between PTDB, MHPrj, catalogue identifiers and ScenarioSuite. In particular, `RT_DEVICE.id_device` is declared `INT`, while `EN_HOST.id_device` is declared `varchar(50)`; equal names do not establish equal identity semantics or an enforced length domain.

The [source report](../project/review/installer-databases-3.5.38/project-templates-report.txt) retains every table's sanitized metadata, declared constraints, finite reference rows and reproducible query evidence. The [source review](../project/review/installer-databases-3.5.38/project-templates-source-review.txt) verifies the original identities and the interpretation of the declared relationships. Exact original schema hashes remain available while credential-bearing defaults and raw sensitive declarations are not exported.

Identifier resolution, transaction behavior, application constraints and persistence workflows remain unresolved without a populated project or the corresponding loader/saver consumer. Empty templates are evidence of available structure, without proof of current installation or physical behavior.
