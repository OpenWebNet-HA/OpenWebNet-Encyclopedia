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
| [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Physical Device, firmware, Module, Object, and configuration capability | ScenarioDevices ID equivalence |
| [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) | systems, address rules, management frames, diagnostic/programming sequences, and timeouts | Scenario Engine graph or ScenarioDevices row mapping |
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

This section uses:

- **established** for direct schema/data facts or corroborated protocol mappings;
- **implementation-derived** for stable meaning recovered from resource keys and stored frames;
- **inferred** for the best explanation of a complete observed pattern without a direct declaration;
- **unknown** where competing explanations remain.
