# Open Questions

This page contains only questions that remain unresolved after cross-checking the canonical MyHOME Suite 3.5.38 databases, `OpenQuery.txt`, the incorporated captures, product documentation, and the relationships established elsewhere in this documentation.

Each entry states the known boundary before the missing evidence so that later investigations do not reopen facts that are already established.

## WHO 13 gateway properties

### `DIMENSION 20`

Prior gateway-identification research has flagged `WHO 13 DIMENSION 20` as an encountered property, but the currently preserved evidence chain does not yet establish its classic SCS/TCP semantics. The canonical classic `WHO_13.pdf` registry does not define it, the ZigBee `WHO 13` registry does not define it, canonical MyHOME Suite `OPEN.db` provides no functional `WHO 13 DIMENSION 20` template, and the preserved F454 and MH202 gateway-information captures examined in the current correction do not contain it.

This is a **provenance gap**, not evidence that the property does not exist. Promotion to the functional reference requires the specific canonical source or first-hand capture that establishes the request/response form and payload, followed by semantic corroboration. Do not infer a meaning from diagnostic `DIMENSION 6` microcontroller-version fields or from any numerically similar namespace.

### `DIMENSION 40`

Existence is established more strongly than semantics. Independent first-hand F454 and MH202 gateway-information captures both show `*#13**40##` and both return `*#13**40*4*0##`.

What remains unresolved is the meaning of the two returned values, whether either field varies independently, and the applicability across gateway models and firmware revisions. The next discriminating evidence is a cross-model or cross-firmware observation in which at least one returned value differs, or a canonical implementation/specification source naming the fields. Until then, preserve the response as two positional unknown values.

The ZigBee specification's `DIMENSION 17` hardware-version definition is not part of this open question: that meaning is established for the ZigBee `WHO 13` variant. What remains unestablished is whether any classic SCS/TCP implementation reuses numeric `17` with the same semantics.

## Diagnostic and programming fields

### `DIMENSION 32.SYS`

`MHCatalogue.db.EN_SYSTEM.sys_modobj` is the leading candidate. Lighting/Automation observations cannot distinguish it from coincident values in other namespaces.

A successful non-Lighting response is still required. The most discriminating cases are Thermoregulation, Energy Management, Access Control, and Integration Functions, whose `sys_modobj`, database system ID, and functional `WHO` values differ.

It also remains unknown how `SYS` selects one active context when an Object belongs to several catalogue systems.

### `DIMENSION 4` and `5`

`OPEN.db` establishes the transport surface: `DIMENSION 4` carries `C1..C6`, `DIMENSION 5` carries `C7..C12`, and every `C` field has range `0..255`. The `ConfConfigurators` sequence sends the corresponding programming forms and is described there as virtual configuration.

What remains unresolved is the cross-database correlation to catalogue semantics. No canonical relation establishes that `C1` equals the firmware `EN_CONF` row with `progressive = 1`, or an equivalent positional rule for every firmware. Controlled observations are still needed to determine how `C1..C12` encode physical/configurator contents in Device families and how those transport positions correspond, where applicable, to firmware-specific symbols such as `A`, `PL`, `M`, `G`, `I`, `ZA`, `ZB`, `N`, `T`, and `S`.

This question no longer concerns the existence or numeric transport range of `C1..C12`; those are established. It concerns their Device-specific semantic correlation with catalogue definitions and physical positions.

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

### Physical-to-advanced and transport correlation

The catalogue-native physical topology mechanism is now established for condition-represented branches: resolve firmware physical definitions and legal domains, enumerate `AS_OBJECT_FIRMWARE`/`EN_SLOTS` candidates, constrain `AS_SLOT_CONDITION`/`EN_CONDITION` branches by reachability, select the matching Object topology, and only then evaluate applicable `EN_CONV_RULE` rows. `EN_PHY_TO_ADV_TRANS` remains a sparse supporting table with only three firmware rows and is not the generic mechanism.

Open boundaries remain narrower:

- whether and how `DIMENSION 4.C1..C12` correlate with firmware `EN_CONF` definitions or `progressive` ordering for each Device family;
- how to interpret catalogue candidates that have no explicit physical predicate when reconstructing a complete physical topology;
- whether textual irregularities such as `O/I` versus `I/O` have an application-level normalization not represented in the canonical databases;
- which property-level physical-to-advanced correspondences are complete when symbol, range, conversion, or `CONF_SYMBOL_REF` evidence is absent;
- how the registered catalogue mode labels correspond to every MyHOME Suite UI path beyond the exact sequence labels preserved in `OPEN.db`.

### Catalogue-wide addressed-form `N_CONF` equivalence

For the ordinary addressed Device form, the meaning of `N_CONF` is corroborated as the number of physical configurator positions provided by the Device. Resolved examples also match the count of applicable firmware-scoped physical configuration fields after excluding the common `AID`/ID field.

What remains open is whether that database-count equivalence holds for every catalogue firmware, including conditional fields, shared firmware definitions, and Devices without available product diagrams. This question does not reopen the addressed-form interpretation.

### Gateway `N_CONF = 15`

The empty-`WHERE` gateway identity form is a separate case. First-hand MH202 and F454 captures both return `N_CONF = 15`, outside the ordinary addressed-form `0..12` range. Numerically, `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern. A reserved or sentinel interpretation is therefore plausible, but the available evidence does not establish what the value signifies.

The open question is the exact gateway semantics of `N_CONF = 15`. Evidence that could resolve it includes an applicable MyHOME_Suite decoder or resource definition, an authoritative protocol definition, or controlled observations across gateway models and firmware revisions that distinguish literal count, reserved-value, and applicability interpretations.

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

1. recover the canonical provenance for classic `WHO 13 DIMENSION 20` and obtain a discriminating `DIMENSION 40` observation across a different gateway or firmware revision;
2. one successful non-Lighting `DIMENSION 32` response whose candidate `SYS` values differ;
3. controlled `DIMENSION 4` and `5` captures across known physical configurator changes;
4. a controlled Device/item case exercising concrete, wildcarded, multiple, or missing firmware build records;
5. file-access, database-statement, and save-operation traces while creating one minimal scenario;
6. a runtime trace of address-rule selection for a system with both general and family-qualified rules;
7. hardware and microcontroller version observations across known revisions of the same product.

Each result should update the [Relationship Register](relationship-register.md) and then the appropriate reference section.
