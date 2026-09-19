# Open Questions

This page contains only questions that remain unresolved after cross-checking the canonical MyHOME Suite 3.5.38 databases, `OpenQuery.txt`, the incorporated captures, product documentation, and the relationships established elsewhere in this documentation.

Each entry states the known boundary before the missing evidence so that later investigations do not reopen facts that are already established.

## Diagnostic and programming fields

### `DIMENSION 32.SYS`

`MHCatalogue.db.EN_SYSTEM.sys_modobj` is the leading candidate. Lighting/Automation observations cannot distinguish it from coincident values in other namespaces.

A successful non-Lighting response is still required. The most discriminating cases are Thermoregulation, Energy Management, Access Control, and Integration Functions, whose `sys_modobj`, database system ID, and functional `WHO` values differ.

It also remains unknown how `SYS` selects one active context when an Object belongs to several catalogue systems.

### `DIMENSION 4` and `5`

The two dimensions each carry six Device-level configurator values. They are related to physical/Virtual configurator transfer and are not ordinary `EN_CONF.idx` records.

The exact positional and value encoding remains unresolved. In particular, controlled captures must determine whether the twelve values represent configurator contents, presence state, another encoding, or a combination of these, and whether positions `1..6` and `7..12` correspond directly to the two dimensions.

### `DIMENSION 310`

`DIMENSION 310` carries an Object-specific value without a generic configuration index. `OPEN.db` supplies neither ordinary parameter metadata nor a general decoder for it.

Its meaning and value domain remain to be established per Object and Device family.

### Hardware and microcontroller versions

`DIMENSION 3` and `6` use the same logical `Version*Release*Build` structure as the firmware response. No corresponding hardware- or microcontroller-version fields have been found in the canonical databases.

It remains unknown whether MyHOME Suite uses these values to distinguish product variants or compatibility, and whether an unpreserved data source maps them to catalogue Devices.

## Address selection and encoding

The database establishes system-to-rule associations, address templates, and Object-family qualification. It does not preserve the final selection and rendering algorithm.

The remaining questions are:

- How does MyHOME Suite choose among a system's family-qualified and family-unqualified address rules?
- How are `level_2_rule` and `level_4_rule` consumed? Their nonzero values occur on the Lighting/Automation general, environment, group, and F422 extension rules, but the runtime composition with the dedicated level rules is not encoded.
- How is `validity_rule` evaluated? The only nonempty expression in this revision is `MOD=SLA;` on the Thermoregulation slave-probe rule.
- How is `offset_adv` applied? It is populated only for the two F422 mode-specific rules, with values `496` and `256`.
- Under which Device layouts does the diagnostic outer `WHERE` follow the configured address of `slot` `1`, and what rule applies when slot `1` is absent, disabled, or differently addressed?

## Catalogue behavior

### Firmware selection

The catalogue firmware identity is the three-component `V.R.b` tuple distributed across `EN_FIRMWARE` and `EN_BUILDS`. An explicit `-1` is strongly corroborated as any or unspecified for that component, while a missing build row remains structurally distinct.

The exact MyHOME Suite selection precedence remains unknown when concrete components, `-1` sentinels, multiple build rows, missing build rows, `FW_default`, and localization metadata overlap.

### Object replacement

`fixed_ko`, visibility/editability metadata, conditions, firmware, slot, and product context all contribute to the available Object set.

The complete rule that determines whether MyHOME Suite displays and permits replacement of an Object at a particular Module remains unknown.

### Physical-to-advanced translation

`EN_PHY_TO_ADV_TRANS` contains explicit translation data for only three firmware definitions. Symbols, configuration types, filters, and observed behavior support additional property-level correlations but do not form a complete general translation table.

It remains unknown whether the remaining mappings can be reconstructed systematically or require Device-specific application logic.

### Catalogue-wide `N_CONF` equivalence

The meaning of `N_CONF` is established: it is the number of physical configurator positions provided by the Device. Resolved examples also match the count of applicable firmware-scoped physical configuration fields after excluding the common `AID`/ID field.

What remains open is whether that database-count equivalence holds for every catalogue firmware, including conditional fields, shared firmware definitions, and Devices without available product diagrams. This question does not reopen the meaning of `N_CONF`.

## Scenario Engine

The two ScenarioDevices databases are capability catalogues, not persisted scenario graphs. Their common semantic content and revision differences are established; local row identifiers are not stable across the two files.

The remaining questions are:

- Which ScenarioDevices copy does MyHOME Suite load, and under what installation, update, or runtime conditions?
- Are the Program Files and ProgramData copies synchronized or migrated?
- Where are user-authored scenario graphs and their node ordering, branches, bindings, and execution state persisted?
- How are frame-absent trigger and condition capabilities connected to runtime events?
- What application enumerations and UI behaviors define `CategoryFlag`, `WhereType`, Parameter `Type`, and `OperatorType`? Their stored value distributions and semantic clusters are known, but their exact enum contracts are not.
- What runtime matching behavior uses `ObjectMatchingId` and `CommandMatchingId`?

## Application internals

`OpenQuery.txt` establishes a set of named reads and their selected columns, but it is incomplete and does not identify callers or runtime control flow.

The remaining questions are:

- When and how are the databases opened, cached, invalidated, refreshed, synchronized, or migrated?
- Which application components execute each query in `OpenQuery.txt`, and are all named queries used?
- How are the separately selected address-rule columns consumed? The earlier bitwise-expression question was based on an incorrect source attribution; see the [Registry Source Correction](../internals/openwebnet-registry-and-state-machines.md#incompleteness-preserved-in-the-source).
- Which resources and application components resolve stored localization keys?
- What locale-selection, fallback, missing-key, and composed-label rules are applied?

## Evidence priorities

The highest-value next observations are:

1. one successful non-Lighting `DIMENSION 32` response whose candidate `SYS` values differ;
2. controlled `DIMENSION 4` and `5` captures across known physical configurator changes;
3. a controlled Device/item case exercising concrete, wildcarded, multiple, or missing firmware build records;
4. file-access, database-statement, and save-operation traces while creating one minimal scenario;
5. a runtime trace of address-rule selection for a system with both general and family-qualified rules;
6. hardware and microcontroller version observations across known revisions of the same product.

Each result should update the [Relationship Register](relationship-register.md) and then the appropriate reference section.
