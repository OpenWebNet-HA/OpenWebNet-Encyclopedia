# Sources and Identifier Boundaries

This section is derived from preserved MyHOME_Suite 3.5.38 sources and the repository's functional OpenWebNet reference. Each source establishes a different layer.

## Canonical ScenarioDevices files

Both repository files were originally named `ScenarioDevices.sqlite`; the repository names distinguish their installation locations.

| Repository file | Original installation path | SHA-256 |
| --- | --- | --- |
| `ScenarioDevices-program-files.sqlite` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\ScenarioDevices.sqlite` | `2ce7ffe1286c3246271aed160116fe664407d9e8ff43595f50192e7d2ac85569` |
| `ScenarioDevices-programdata.sqlite` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_ScenarioDevices\ScenarioDevices.sqlite` | `cd3b9b67160f468cdbd30134357b8733c696aacd5d625129240dff6b79224fc3` |

The fingerprints match [`sources/manifest.yaml`](../sources/manifest.yaml). The paths establish packaging location, not precedence or runtime selection behavior.

## Evidence roles

| Source | What it establishes | What it does not establish alone |
| --- | --- | --- |
| ScenarioDevices files | editor capability hierarchy, resource keys, local IDs, categories, matching IDs, templates, and Parameter metadata | installed Device support, complete runtime graph, or public protocol semantics for frame-absent rows |
| [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/) | Physical Device, firmware, Module, Object, and configuration capability | ScenarioDevices ID equivalence |
| [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/) | systems, address rules, management frames, diagnostic/programming sequences, and timeouts | Scenario Engine graph or ScenarioDevices row mapping |
| [Functional reference](../functional/) | functional `WHO`, `WHAT`, `WHERE`, and `DIMENSION` semantics | MyHOME_Suite editor coverage by itself |
| [Cross-database functional coverage](../functional/cross-database-coverage.md) | corroborated intersections among implementation databases and functional frames | undeclared numeric joins |
| observed application/runtime behavior | UI labels, filtering, persistence, matching, and execution behavior | universal support beyond observed versions and Devices |

## Identifier namespaces

| Identifier | Scope |
| --- | --- |
| `ObjectSystems.Id` | local row key in one ScenarioDevices file |
| `FamilyId` | grouping value present only in the Program Files copy |
| `DeviceObjects.Id` | local row key and foreign-key target |
| `DeviceObjects.ObjectId` | ScenarioDevices Object identifier |
| `ObjectMatchingId` | sparse cross-role Object correlation |
| `Commands.Id` | local row key and Parameter foreign-key target |
| `Commands.CommandId` | ScenarioDevices command identifier |
| `CommandMatchingId` | sparse cross-role command correlation |
| `ChiOpen` | stored functional `WHO` evidence where present |
| catalogue `id_key_object` | internal primary key in `MHCatalogue.db` |
| catalogue `key_object` | external diagnostic/programming Object number |
| functional `WHO` / `WHAT` / `WHERE` | OpenWebNet wire namespaces |

Only the declared foreign keys inside one ScenarioDevices file can be joined automatically. Matching IDs are explicit correlations within that model but are not foreign keys.

## Cross-file identity

The common semantic content of `programdata` is an exact subset of `program-files` when compared using the full hierarchical path and non-local fields:

- Object System resource key and `CategoryFlag`;
- Device Object resource key and Object/matching identifiers;
- Command resource key and command/matching/address/frame fields;
- Parameter resource key, placeholder, domain, type, operator, and stored value.

Local primary keys differ after the additional Program Files rows, so row IDs are not cross-file identities.

## Correlation rules

A cross-source relationship can be documented as established when supported by one or more of:

1. a declared foreign key;
2. a literal OpenWebNet frame whose `WHO` and operation parse unambiguously;
3. an explicit matching identifier inside ScenarioDevices;
4. resource-key semantics corroborated by a literal frame or functional specification;
5. independently observed MyHOME_Suite behavior.

Do not correlate values only because their integers are equal. In particular, `FamilyId`, `ObjectId`, `CommandId`, catalogue system IDs, catalogue Object IDs, and OpenWebNet fields are independent until evidence connects them.

## Evidence labels

[Evidence and Confidence](../reverse-engineering/evidence-and-confidence.md) defines claim-level confidence and examination methods. Direct schema/row facts, source-derived interpretation and actual application/runtime observations have separate roles. A stored template does not establish installed support; a corroborated cross-source mapping does not make every interpretation universal. Unresolved selectors and enum meanings remain attached to the affected field rather than being filled with a plausible name.

## Separate ScenarioSuite database

Registered artifact `myhome-suite-3.5.38-mh202-1902-lgg-scen-suite-db-eng` preserves `Scen_SuiteDB_ENG.db`, SHA-256 `ae1e60ca9b06eeb1eecd5bc8e21ff5ba2bdb928aa47075a2e7d8995c41e06e29`. It is a distinct schema from both ScenarioDevices files: 79 tables, no declared foreign keys, and empty shipped scenario-working tables. The [source-specific analysis](scenario-suite-database.md) identifies exact joins and remaining compiler/runtime limits.

`ANA_OGGETTI.ID_OBJ`, `ANA_CHI.ID_CHI`, `ANA_COSA.ID_COSA`, `ANA_DOVE.ID_DOVE` and area/association IDs are local identities. Stored `OPEN_CHI`, `OPEN_COSA`, `OPEN_DOVE` and ordered `OPEN_FIELD_n` tokens belong to a different representation layer. Do not transfer CategoryFlag/matching-ID semantics or catalogue Module/Object identity by equal integers. Database version `1.0.53`, Suite `3.5.38` and Firmware `1.0.24` are separate scopes.

The [original generator and field consumers](scenario-suite-generator.md) provide method-level relationships for this separate source. Its graphic type selects the field-kind namespace; equal `ID_KIND` values across text and range tables do not override that dispatch. The [MH200N profile](scenario-suite-variants.md) has a separate fingerprint and database version.

Server-side JSON records and C++ runners in [MyHOMEServer1/F460](server-scene-processing.md) form another implementation layer. Their local type indices, numeric fields and object layouts must not be equated with editor IDs or catalogue Objects by numerical coincidence.
