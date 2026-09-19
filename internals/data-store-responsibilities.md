# Data Store Responsibilities

MyHOME Suite separates product capability, protocol workflows, scenario-editor vocabulary, and selected cross-property validation into different stores. No single file is a complete model of the installation.

## Responsibility matrix

| Store | Strongest evidence | Does not establish alone |
| --- | --- | --- |
| `MHCatalogue.db` | Devices, SKUs, items, brands, lines, firmware, Modules, Objects, Virgin Objects, configuration definitions, ranges, filters, conditions, and conversions | current installed state, complete functional protocol, or scenario graph |
| `OPEN.db` | system registry, management frame templates, parameters, address rules, scenarios, sequences, direction, repetition, timers, and status transitions | complete Device catalogue, ordinary functional command vocabulary, or Device-specific support |
| `OpenQuery.txt` | named SQL statements intended to assemble selected `OPEN.db` structures | application control flow beyond those queries or semantics absent from the selected columns |
| ScenarioDevices files | scenario-editor Object Systems, Device Objects, Commands, Parameters, categories, matching IDs, and action templates | installed Device identity, catalogue Object equality, or persisted user scenarios |
| `rules.db3` | linked-property validation for selected Temperature Control Objects | a general Object registry or universal validation engine |
| Public OpenWebNet PDFs | published frame grammar and functional `WHO` semantics | MyHOME Suite management state machines or catalogue hierarchy |
| Observed traffic | actual ordering, values, repetition, and Device behavior | behavior of unobserved products or versions |
| MyHOME Suite UI | displayed labels, visibility, editability, and workflow behavior | wire encoding without a database or capture correlation |

## Composition, not a global join

The stores are composed through a sequence of resolved meanings:

1. a diagnostic response identifies an installed Device instance;
2. `DIMENSION 1` and version responses narrow the catalogue item and firmware;
3. `DIMENSION 30`, `32`, and `35` describe installed Module/Object/configuration state;
4. catalogue relationships determine supported alternatives and effective value domains;
5. `OPEN.db` determines the applicable management workflow and transport fields;
6. functional specifications determine the meaning of operational frames;
7. ScenarioDevices contributes editor capabilities only after a functional correlation is established.

A numeric match is not a composition rule. For example:

- `MHCatalogue.db.EN_SYSTEM.id_system` is not `OPEN.db.EN_SYSTEM.id_system`;
- ScenarioDevices `ObjectId` is not automatically `EN_KEY_OBJECT.key_object`;
- `EN_DEVICE.id_device` is not the installed 32-bit Device ID;
- diagnostic `SLOT` is not `EN_SLOTS.id_slot`;
- functional `WHO` is not a database primary key.

The complete identifier policy is maintained in [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md).

## Capability versus instance data

The preserved databases are principally capability and workflow registries. They describe what MyHOME Suite knows how to offer or send.

Installed state comes from diagnostic traffic, a loaded project, UI observations, or another persistence source not yet preserved.

| Question | Correct evidence |
| --- | --- |
| Can firmware offer Object `406` at `slot` `3`? | catalogue capability |
| Does this installed Module currently expose Object `406`? | `DIMENSION 30` or project state |
| Can this property accept value `7` in this context? | catalogue range, filter, condition, and linked-rule evaluation |
| Which frame writes the value? | `OPEN.db` programming sequence |
| Did the write take effect? | fresh diagnostic read-back |
| Can the scenario editor render an action for it? | ScenarioDevices plus functional correlation |

## Read-only evidence corpus

The repository copies are evidence, not a working MyHOME Suite installation. They must be opened read-only for analysis.

SQLite foreign-key declarations are not uniform across stores. ScenarioDevices declares its principal hierarchy foreign keys; many important `MHCatalogue.db` relationships are reconstructed from complete key coverage and association structure. Documentation must distinguish a declared constraint from a corroborated relationship.

## Failure policy

When a required correlation is missing, retain raw identifiers and source provenance, return an ambiguous or unresolved result, and do not select the first equal integer or widen a value domain to the protocol transport maximum.

Diagnostics can preserve unknown values. Programming should fail closed until the required context is resolved.
