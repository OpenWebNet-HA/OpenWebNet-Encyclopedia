# OpenWebNet Encyclopedia Machine KB Corpus

Generated deterministically from canonical documentation. Practical Guides are excluded.

# Document: ownkb:document:d000001

Source path: `device-model/README.md`
Namespace context: `contextual`
Area: `device-model`

## Device Model

Section ID: `ownkb:section:d000001:s000001`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `documentation`

The MyHOME device model describes how one physical product exposes configurable functions to MyHOME_Suite and to the diagnostic, programming, and functional protocols.

It is the canonical owner of entity definitions and catalogue relationships. The cross-area distinction between catalogue capability, installed state, runtime control, and programming is defined in [OpenWebNet Scope and Architecture](../protocol/scope-and-architecture.md).

The canonical hierarchy used throughout this documentation is:

**Physical Device â†’ Firmware â†’ Module â†’ Object â†’ Configuration**

Firmware is an implementation layer between the product model and its exposed Modules. In ordinary discussion the shorter **Physical Device â†’ Module â†’ Object â†’ Configuration** form remains sufficient.

### Reference

Section ID: `ownkb:section:d000001:s000002`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `evidence`, `source`

| Subject | Page |
| --- | --- |
| Evidence roles, identifier boundaries, and source handling | [Sources and Identifier Boundaries](sources-and-identifiers.md) |
| Product identity, catalogue records, and Device composition | [Physical Devices](physical-devices.md) |
| Firmware selection and capability projection | [Firmware](firmware.md) |
| Firmware-exposed Modules and `slot` positions | [Modules](modules.md) |
| Logical functions and Object identity | [Objects](objects.md) |
| Configurable Module templates and permitted Objects | [Virgin Objects](virgin-objects.md) |
| Configuration definitions, values, constraints, and protocol representation | [Configuration](configuration.md) |

### Canonical model

Section ID: `ownkb:section:d000001:s000003`

Applicability cues: `firmware`, `revision`
Provenance cues: `catalogue`, `source`

| Level | Meaning | Primary catalogue representation |
| --- | --- | --- |
| Physical Device | An installed hardware product instance | `EN_DEVICE` â†’ `EN_ITEM` |
| Firmware | A versioned capability definition for an item | `EN_FIRMWARE`, `EN_BUILDS` |
| Module | A firmware-exposed logical container at a `slot` | `EN_SLOTS`, `AS_OBJECT_FIRMWARE` |
| Object | The logical function assigned to or offered by a Module | `EN_KEY_OBJECT` |
| Virgin Object | A template constraining which Objects a configurable Module can become | `EN_VIRGIN_OBJECT` and association tables |
| Configuration | Object- or firmware-scoped properties and their allowed values | `EN_CONF`, ranges, filters, conditions, and conversion rules |

The [canonical `MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) contains 541 Device records, 210 item definitions, 311 firmware definitions, 158 Objects, 18 Virgin Objects, 1,725 `slot`/Object assignments, and 2,883 configuration definitions. These counts describe this source revision; they are not protocol limits.

### End-to-end catalogue path

Section ID: `ownkb:section:d000001:s000004`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`, `source`

For a catalogue Device, the principal capability path is:

1. `EN_DEVICE.id_item` selects the shared item definition in `EN_ITEM`.
2. `AS_ITEM_SYSTEM` associates the item with one or more catalogue systems and supplies the item-level `modobj`.
3. `EN_FIRMWARE.id_item` selects the firmware definitions available for that item.
4. `AS_OBJECT_FIRMWARE` associates each firmware with supported Objects.
5. `EN_SLOTS.id_object_firmware` places those Object options at `slot` positions.
6. Virgin-Object associations describe configurable Module templates and the Objects they permit.
7. `EN_CONF` defines Object-scoped or firmware-scoped configuration properties.
8. Ranges, filters, conditions, and rules constrain the values available in a particular context.

The original database declares few foreign keys. The relationships above are supported by complete key coverage in the canonical data and by the way the association tables are structured. They remain reconstructed relationships rather than modifications to the canonical source.

### Protocol projections

Section ID: `ownkb:section:d000001:s000005`

Applicability cues: `firmware`, `version`
Cautions: `do not`
Provenance cues: `catalogue`

The [canonical `OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) projects parts of the model onto diagnostic and programming frames:

| Operation | Model level exposed |
| --- | --- |
| `DIMENSION 1` | item/model identity, a field labelled `N_CONF`, brand, and line |
| `DIMENSION 2` | firmware version |
| `DIMENSION 3` | hardware version |
| `DIMENSION 6` | microcontroller version |
| `DIMENSION 13` | 32-bit Device ID |
| `DIMENSION 30` | `slot`, enabled/disabled Module state, and regular Object or Virgin Object identifier |
| `DIMENSION 32` | `slot`, system, and configured address |
| `DIMENSION 35` | configuration index, `slot`, and parameter value |
| `DIMENSION 38` | request/reset operation selecting one or all `slot` positions |
| `DIMENSION 310` | special Object parameter response |

These frames expose a runtime projection of the catalogue model; they do not reproduce the catalogue schema directly.

### Model boundaries

Section ID: `ownkb:section:d000001:s000006`

Applicability cues: `firmware`
Provenance cues: `catalogue`

A Physical Device is not equivalent to one OpenWebNet address, one Module, one Object, or one functional `WHO`.

- One product item can have several branded Device records.
- One item can have several firmware definitions.
- One firmware can expose several Modules.
- One Module can offer several Object choices.
- One Object can have several configuration properties.
- Different Modules of one Device can participate in different functional systems.
- The Device address used for discovery or interview can differ from the functional addresses configured on its Modules.

**Module** is the preferred term for a firmware-exposed logical container. **`slot`** is reserved for the numeric position or index used by diagnostic frames and catalogue structures.

The Device description and Object description are also distinct. `EN_DEVICE.name` is the preferred MyHOME_Suite-facing description for the physical model. `EN_KEY_OBJECT.descr` identifies an individual logical function.

### Evidence

Section ID: `ownkb:section:d000001:s000007`

Provenance cues: `catalogue`, `evidence`

The evidence sources and their identifier boundaries are defined in [Sources and Identifier Boundaries](sources-and-identifiers.md). In summary, `MHCatalogue.db` defines catalogue capability, `OPEN.db` defines diagnostic and programming structures, the ScenarioDevices databases describe scenario-engine capabilities, `rules.db3` adds selected configuration constraints, and the public OpenWebNet documents define published functional behavior.

Original evidence remains unchanged under [`sources/`](../sources/); derived relationships are documented outside the canonical corpus.

### Interpretation rules

Section ID: `ownkb:section:d000001:s000008`

Applicability cues: `gateway`, `only for`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `evidence`, `source`

Use each source only for the layer it establishes. Do not join independent identifier spaces because their numeric values happen to match, and do not promote implementation labels to protocol semantics without corroborating evidence.

For the ordinary addressed diagnostic form, the established interpretation of `DIMENSION 1.N_CONF` on corroborated Devices is the physical configurator-position count; it is not an Object or Device-class identifier. The separate empty-`WHERE` gateway variant has returned `N_CONF = 15` in observed MH202 and F454 cases, outside the ordinary `0..12` range, and its exact semantics remain unresolved. See [Physical Devices](physical-devices.md) and [`DIMENSION 1`: Device Identity](../diagnostics/dim1-device-identity.md). Catalogue-wide count equivalence and gateway sentinel semantics remain separate evidence gaps.

# Document: ownkb:document:d000002

Source path: `device-model/configuration.md`
Namespace context: `contextual`
Area: `device-model`

## Configuration

Section ID: `ownkb:section:d000002:s000001`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Configuration is the set of instance-specific values applied to an Object, Module, firmware, or Device. It turns catalogue capability into an operational function within an installation.

### Configuration layers

Section ID: `ownkb:section:d000002:s000002`

| Layer | Purpose |
| --- | --- |
| Object selection | Chooses the function exposed by a configurable Module |
| Enabled state | Enables or disables the Module/Object where supported |
| Addressing | Assigns a functional target such as `A`/`PL`, group, environment, CEN, zone, or another system-specific address |
| Operating mode | Selects an Object-specific behavior or modality |
| Parameters | Supplies delays, levels, button assignments, sensitivity, load type, presets, and other values |
| Associations | Links the Object to groups, scenarios, related Modules, or collections |
| Constraints | Defines types, ranges, defaults, visibility, read-only state, dependencies, and validation |

Not every Object uses every layer.

### Core catalogue table

Section ID: `ownkb:section:d000002:s000003`

Applicability cues: `firmware`

`EN_CONF` in `MHCatalogue.db` contains 2,883 configuration definitions.

| Column | Role |
| --- | --- |
| `id_conf` | Configuration-definition identifier |
| `id_key_object` | Object scope or sentinel `0` |
| `id_firmware` | Firmware scope or sentinel `0` |
| `conf_name` | Symbolic configuration name |
| `descr`, `descr_ext` | User-facing descriptions |
| `id_conf_type` | Semantic type such as address, group, or mode |
| `id_conf_data_type` | Storage/value type |
| `idx` | Configuration index |
| `hidden` | Hidden-state metadata |
| `visible` | Visibility metadata |
| `read_only` | Read-only metadata |
| `progressive` | Ordering/progression metadata |

### Two exclusive configuration scopes

Section ID: `ownkb:section:d000002:s000004`

Applicability cues: `firmware`

Every canonical `EN_CONF` row uses one of two patterns:

| Scope | Key pattern | Rows |
| --- | --- | --- |
| Object-scoped | valid `id_key_object`; `id_firmware = 0` | 1,420 |
| Firmware-scoped | `id_key_object = 0`; valid `id_firmware` | 1,463 |

No canonical row resolves simultaneously to both an Object and a firmware definition.

This is a discriminator pattern, not two mandatory foreign keys. Treating both columns as unconditional references would misrepresent half the table.

#### Object-scoped configuration

Section ID: `ownkb:section:d000002:s000005`

Object-scoped definitions describe reusable properties of a logical function. Examples include:

- Function type
- point-to-point address
- group membership
- mode
- delays
- setpoints
- scenario numbers
- button assignments.

#### Firmware-scoped configuration

Section ID: `ownkb:section:d000002:s000006`

Applicability cues: `firmware`
Uncertainty: `may`

Firmware-scoped definitions describe properties tied to one firmware capability rather than to a reusable Object alone. These can supply product-specific behavior, shared Device settings, or values used across several Modules.

A complete configuration UI may combine both scopes.

### Physical configuration and configuration modes

Section ID: `ownkb:section:d000002:s000007`

Applicability cues: `firmware`
Provenance cues: `catalogue`

The canonical catalogue represents configuration mode and physical configurator semantics separately.

`EN_CONFIG_MODE` contains distinct records for Virtual Configuration, Advanced Configuration, Physical configuration, and Product Programming. `AS_FIRMWARE_CONFIG_MODE` records which modes a firmware supports. A firmware can support both Virtual and Advanced configuration, so neither label should be used as an umbrella synonym for all non-physical configuration.

Mode support is a catalogue capability. It does not establish which mode configured an installed Device or which MyHOME Suite UI label was active for a particular operation.

#### Firmware-contextual physical definitions

Section ID: `ownkb:section:d000002:s000008`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`

Physical configurator interpretation is firmware- and definition-contextual. Firmware-scoped `EN_CONF` rows with `idx = -1` contain the principal physical definitions, but that structural pattern is not sufficient by itself: the common `AID`/ID definition also has `idx = -1` and is not a literal plug position.

For a demonstrated physical definition, `EN_CONF_RANGE` supplies the legal raw values and symbolic meanings. The correct conceptual lookup is:

```text
firmware + exact EN_CONF definition + raw value
```

not a universal lookup from the raw number alone. The same raw value can carry different labels for different symbols on the same firmware and across different firmware definitions.

`EN_CONF.progressive` records ordering metadata inside the catalogue. Although it can resemble physical ordering in examples, no canonical cross-database relation makes it equivalent to `DIMENSION 4.C1`, `C2`, and so on for every firmware.

#### Topology selection

Section ID: `ownkb:section:d000002:s000009`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `catalogue`

Physical configurator values can determine which Object alternative occupies a Device-local `slot`. The catalogue represents that selection through the firmware's Object/slot candidates and their conditions:

```text
EN_FIRMWARE
  -> AS_OBJECT_FIRMWARE
  -> EN_SLOTS
  -> AS_SLOT_CONDITION
  -> EN_CONDITION
```

Condition symbols must be resolved against that firmware's exact `EN_CONF` definitions and legal `EN_CONF_RANGE` domains before a branch is considered reachable. A stored condition that references a value outside the firmware's legal domain remains a stored catalogue row, but it is not a reachable physical configuration for that firmware.

A resolver must report zero-match, multi-match, unsupported-expression, and unresolved states rather than inventing precedence.

#### Property conversion

Section ID: `ownkb:section:d000002:s000010`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Topology selection is distinct from converting selected physical/item settings into effective Object properties. After an Object branch is selected, `EN_CONDITION.id_conv_rule` can lead to `EN_CONV_RULE`, which maps item-level configuration symbols and values into Object-level configuration.

`CONF_SYMBOL_REF` supplies additional symbol correspondence only in its recorded system and slot context. Because it has no firmware key, it is not a global symbol-alias table.

One physical selector can therefore participate in topology selection and, separately, contribute to one or more resulting Object properties. These are different catalogue operations and should not be described as one undifferentiated physical-to-advanced translation.

#### Physical counterparts of effective properties

Section ID: `ownkb:section:d000002:s000011`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `evidence`

A resolved Object property can have a physical counterpart, but the counterpart must be established in the exact firmware and Object context. Useful evidence includes compatible symbols, semantic types, legal ranges, filters, conversion rules, and contextual symbol references.

A physical counterpart does not identify the active configuration mode. `DIMENSION 32` and `35` report effective installed values; a value representable physically could still have been established through another supported configuration mode.

`EN_PHY_TO_ADV_TRANS` contains only three rows in the canonical MyHOME Suite 3.5.38 catalogue, for firmware IDs `160`, `691`, and `722`. It is supporting evidence for those cases, not the generic mechanism used to resolve physical topology or property conversion.

The authoritative algorithm, parameterized SQL, reachability rules, firmware `157` worked example, and `DIMENSION 4`/`5` boundary are documented in [Catalogue Resolution](../internals/catalogue-resolution.md#physical-configuration-resolution).

### Configuration type and data type

Section ID: `ownkb:section:d000002:s000012`

Provenance cues: `source`

`EN_CONF_TYPE` supplies semantic categories. Observed categories include:

- point-to-point address
- zone/room address
- group
- mode.

`EN_CONF_DATA_TYPE` supplies value representation. The canonical source uses:

| Data type | Typical role |
| --- | --- |
| `Enum` | Named choice |
| `Range` | Numeric interval or enumerated range rows |
| `Range_Pad` | Padded numeric/address value |
| `user_value` | User-entered value |
| `Boolean` | Two-state value |
| `Fixed_Value` | Fixed configuration value |

Semantic type and data type are independent: a mode can be an enumeration or range, and an address can use different representations.

### Allowed values and ranges

Section ID: `ownkb:section:d000002:s000013`

Cautions: `do not`

`EN_CONF_RANGE` contains 14,346 rows and resolves completely to `EN_CONF`.

| Column | Role |
| --- | --- |
| `id_conf_range` | Range/value identifier |
| `id_conf` | Configuration definition |
| `value` | Stored value |
| `name` | Display name |
| `default` | Default metadata |
| `digit` | Digit-width metadata |
| `step` | Step size |
| `min_value`, `max_value` | Numeric interval |
| `progressive` | Ordering |

A property can therefore use explicit named values, a numeric interval, or both forms of metadata.

Do not assume that a missing range row means the protocol accepts every value. Additional filters and rules can narrow the domain.

### Contextual filters

Section ID: `ownkb:section:d000002:s000014`

Applicability cues: `firmware`

`EN_FILTER` contains 1,909 rows. Every row resolves to both:

- an `AS_OBJECT_FIRMWARE.id_object_firmware` context
- an `EN_CONF.id_conf` definition.

This makes the filter context explicit: a configuration definition can have different allowed values for different Object/firmware combinations.

`EN_FILTER_RANGE` contains 6,152 range restrictions associated with filters.

The practical evaluation is:

1. select firmware;
2. select `slot` and Object;
3. collect applicable Object- and firmware-scoped configuration definitions;
4. locate the corresponding Object/firmware association;
5. apply `EN_FILTER`;
6. apply `EN_FILTER_RANGE`;
7. apply conditions and cross-property rules.

### `slot` conditions and conversion rules

Section ID: `ownkb:section:d000002:s000015`

Provenance cues: `catalogue`

The catalogue contains:

- 1,000 `AS_SLOT_CONDITION` rows
- 488 `EN_CONDITION` rows
- 7,899 `EN_CONV_RULE` rows.

`AS_SLOT_CONDITION` attaches a condition to a `slot`/Object assignment. `EN_CONDITION.id_conv_rule` selects the conversion-rule logic used by that condition.

`EN_CONV_RULE` can compare item-level and Object-level configuration symbols and values, mark an always-true rule, or jump to another rule. These structures affect capability selection and value conversion; they are not OpenWebNet frames.

`CONF_SYMBOL_REF` supplies explicit symbol correspondence between item configuration and Object configuration for a system and `slot`.

### Additional Temperature Control rules

Section ID: `ownkb:section:d000002:s000016`

Provenance cues: `catalogue`, `database`

[`rules.db3`](../sources/myhome-suite/3.5.38/databases/rules.db3) adds cross-property validation and linked-parameter disabling for three Object numbers:

| Object | Catalogue description | Validation rows |
| --- | --- | --- |
| `95` | Hotel thermostat | 149 |
| `96` | Residential thermostat | 152 |
| `184` | Master probe | 107 |

Its `rules` table references configuration indices using expressions such as `$1`, `$2`, and `$21`. Its `DisablelinkedParameter` table contains 194 dependency rows that enable, disable, or constrain related parameters.

The Object numbers and configuration indices align with `EN_KEY_OBJECT.key_object` in `MHCatalogue.db` and `EN_CONF.idx` for those Temperature Control Objects. There is no database foreign key between the files, so the correlation is semantic and structural rather than relational.

`rules.db3` is not a general Object or `WHO` registry.

### Diagnostic parameter representation

Section ID: `ownkb:section:d000002:s000017`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `evidence`

Diagnostics projects an installed configuration through `DIMENSION 32`, indexed `DIMENSION 35` values, and Object-specific `DIMENSION 310` values. The canonical frame definitions, detailed-read sequence, timeout, and unresolved `DIMENSION 38` reset/select effect are maintained in [`DIMENSION 35`: Configuration Parameters](../diagnostics/dim35-configuration.md#reading-detailed-parameters).

The shared â€œkconf indexâ€ terminology strongly supports correlating diagnostic `DIMENSION 35.INDEX` with catalogue `EN_CONF.idx`. Because the databases have no cross-file key, retain the raw frame, resolved Physical Device, firmware, `slot`, Object, and catalogue definition when documenting a mapping. `DIMENSION 310` contains no generic `INDEX` and must remain outside that correlation without Object-specific evidence.

### Address configuration

Section ID: `ownkb:section:d000002:s000018`

Addresses are configuration values scoped to the Objectâ€™s functional system. They are not one universal format.

Examples include:

- Lighting/Automation `A`/`PL`
- group and environment addresses
- Temperature Control zones
- CEN and CEN+ identifiers
- Energy Management target forms
- Access Control indicator addresses.

`DIMENSION 32` reports:

`*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##`

`SYS` and `ADDR` must be interpreted with the applicable Object/system rules. The `ADDR` numeric range in `OPEN.db` does not itself define the formatting or semantics of every functional address.

### Functional and scenario projections

Section ID: `ownkb:section:d000002:s000019`

The public OpenWebNet documents define runtime values such as `WHAT`, functional `DIMENSION` values, and `WHERE` grammars. Those values are not automatically configuration indices.

The ScenarioDevices databases define scenario-engine command parameters. Their `Parameters` tables establish ranges and placeholders for scenario actions, not `EN_CONF` in `MHCatalogue.db` identities.

A scenario parameter can correspond conceptually to a Device/Object configuration value while remaining a separate application-level identifier.

### Read-only and calculated values

Section ID: `ownkb:section:d000002:s000020`

Applicability cues: `firmware`
Uncertainty: `may`, `unknown`
Provenance cues: `catalogue`

Configuration values can be:

- user-selectable
- fixed by Object or firmware
- hidden by a condition
- narrowed by a filter
- read-only
- calculated or compiled by MyHOME_Suite
- reported by the Device
- reserved or unknown.

The `read_only`, `visible`, and `hidden` fields provide direct catalogue metadata. They may be complemented by filter and rule behavior.

For example, a preset position or load-dependent minimum level can have a value range in the catalogue while UI visibility or editability depends on another configuration property.

### Mapping requirements

Section ID: `ownkb:section:d000002:s000021`

Provenance cues: `catalogue`, `evidence`

A mapping between a UI field, catalogue definition, and protocol value requires compatible UI behavior, catalogue scope and index data, protocol `slot`/value evidence and, where available, the resulting runtime behavior. Numeric equality alone is insufficient.

### Sources

Section ID: `ownkb:section:d000002:s000022`

Provenance cues: `catalogue`, `evidence`, `source`

Primary configuration evidence comes from [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db), with protocol structure from [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) and [`OpenQuery.txt`](../sources/myhome-suite/3.5.38/support/OpenQuery.txt). [`rules.db3`](../sources/myhome-suite/3.5.38/databases/rules.db3) adds selected Temperature Control dependencies. ScenarioDevices and the public protocol documents describe adjacent runtime layers rather than catalogue configuration identity.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy.

# Document: ownkb:document:d000003

Source path: `device-model/firmware.md`
Namespace context: `contextual`
Area: `device-model`

## Firmware

Section ID: `ownkb:section:d000003:s000001`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Firmware is the catalogue layer that projects an item into a concrete set of Modules, supported Objects, configuration properties, and connection modes.

### Catalogue representation

Section ID: `ownkb:section:d000003:s000002`

Applicability cues: `firmware`, `revision`, `version`
Provenance cues: `catalogue`, `database`

`EN_FIRMWARE` in `MHCatalogue.db` contains 311 firmware definitions.

| Column | Role |
| --- | --- |
| `id_firmware` | Internal firmware-definition identifier |
| `id_item` | Item to which the firmware belongs |
| `firmware_V` | Version component |
| `firmware_R` | Release/revision component (`R`) |
| `slots` | Number of `slot` positions declared by the firmware |
| `id_status` | Firmware status |
| `FW_default` | Marks the default firmware definition |

All firmware rows resolve to an `EN_ITEM` record in the canonical database.

`EN_BUILDS` supplies the third firmware component and localization data:

| Column | Role |
| --- | --- |
| `id_build` | Internal build-row identifier |
| `firmware_b` | Build component (`b`) |
| `localization_level` | Build localization metadata |
| `id_firmware` | Firmware definition to which the build belongs |

A complete catalogue firmware version is therefore **Version.Release.Build**, written here as `V.R.b`: `firmware_V` and `firmware_R` come from `EN_FIRMWARE`, while `firmware_b` comes from each associated `EN_BUILDS` row. The identity is distributed across the two tables rather than stored as one textual version.

The relationship is not one-to-one in every case. In the canonical database, 19 firmware definitions have no `EN_BUILDS` row and 15 have more than one. A missing build row, an explicit build value, and an explicit `firmware_b = -1` must consequently remain distinct during resolution.

### Firmware selection

Section ID: `ownkb:section:d000003:s000003`

Applicability cues: `firmware`
Provenance cues: `catalogue`

A shared item can have one or several firmware definitions. Device capabilities must therefore be resolved through the firmware selected for the installed product, not from the item alone.

The catalogue path is:

`EN_DEVICE.id_item` â†’ `EN_FIRMWARE.id_item` â†’ selected `EN_FIRMWARE.id_firmware`

The exact selection rule can depend on all three reported components, default flags, localization metadata, and MyHOME Suite behavior. A row being marked `FW_default` does not prove that every installed Device of that item runs that firmware.

#### The `-1` sentinel

Section ID: `ownkb:section:d000003:s000004`

Applicability cues: `firmware`, `version`
Cautions: `must not`
Provenance cues: `evidence`

Negative components are implementation sentinels and must not be rendered as literal negative firmware versions. The canonical data provides strong evidence that `-1` means **any or unspecified value** for that component:

- all 101 firmware definitions with `firmware_V = -1` and `firmware_R = -1` have an associated `firmware_b = -1`, producing `-1.-1.-1`;
- all 101 of those definitions have `FW_default = 1`;
- another five definitions retain concrete version and release values but use `firmware_b = -1`: four are `1.0.-1`, and one is `5.2.-1`;
- an explicit `firmware_b = -1` is structurally different from having no `EN_BUILDS` row.

The mixed forms are particularly important: `1.0.-1` and `5.2.-1` show that the build sentinel can apply independently, rather than `-1.-1.-1` being only a malformed whole-version value.

The evidence therefore supports interpreting `-1.-1.-1` as a version-independent default or fallback and `V.R.-1` as any or unspecified build for a particular version and release. This is a **strongly corroborated interpretation of the data**, not a recovered MyHOME Suite comparison algorithm. Implementations should retain the raw components and must not claim that the precise wildcard-selection precedence is proven.

### Diagnostic firmware identity

Section ID: `ownkb:section:d000003:s000005`

Applicability cues: `firmware`, `version`
Cautions: `do not`
Provenance cues: `catalogue`, `database`, `documentation`

`OPEN.db` defines:

`*#[WHO]*[WHERE]*2*[FW_VERSION]##`

Its parameter description gives the logical form `Version*Release*Build`. In this documentation, the equivalent catalogue tuple is written `V.R.b` to distinguish the three stored numeric components from the `*` separators used by OpenWebNet frames.

This response can be used to select or corroborate a catalogue firmware definition, but the databases do not contain a direct cross-database key between `FW_VERSION` in `OPEN.db` and `id_firmware` in `MHCatalogue.db`.

Related Device-level responses are:

- `DIMENSION 3`: hardware version
- `DIMENSION 6`: microcontroller version.

These values identify implementation revisions. They are not Object or Module identifiers.

### Capability projection

Section ID: `ownkb:section:d000003:s000006`

Applicability cues: `firmware`

Once a firmware definition is selected, its capabilities are assembled through several associations:

| Association | Capability |
| --- | --- |
| `AS_OBJECT_FIRMWARE` | Objects supported by the firmware |
| `EN_SLOTS` | `slot` positions at which each firmware/Object association is available |
| `AS_FIRMWARE_VIRGIN_OBJECT` | Virgin Object templates supported by the firmware |
| `EN_SLOT_KO_VIRGIN` | `slot` positions to which those templates apply |
| firmware-scoped `EN_CONF` rows | Configuration properties belonging to the firmware rather than one Object |
| `AS_FIRMWARE_CONFIG_MODE` | Supported configuration modes |
| `AS_CONNECTION_FIRMWARE` | Supported connection modalities |
| `AS_FIRMWARE_PARAMETERS` | Parameter-file associations |
| `AS_FW_PACKAGE` | Firmware package associations |
| `EN_PHY_TO_ADV_TRANS` | sparse physical-to-advanced translation records for specific firmware definitions |

All 827 `AS_OBJECT_FIRMWARE` rows resolve to both a firmware definition and an Object. All 1,725 `EN_SLOTS` rows resolve to an `AS_OBJECT_FIRMWARE` row.

### Declared slots and Object alternatives

Section ID: `ownkb:section:d000003:s000007`

Applicability cues: `firmware`
Cautions: `must not`

`EN_FIRMWARE.slots` is the declared count of `slot` positions. It must not be compared directly with the number of `EN_SLOTS` rows: one `slot` can have several supported Object alternatives.

For example, firmware `157` declares four slots but has eleven slot/Object rows:

| `slot` | Objects offered |
| --- | --- |
| `1` | Light actuator; Automation actuator |
| `2` | Light actuator |
| `3` | Light control; Automation control; Scheduled scenario; Scheduled scenario PLUS |
| `4` | Light control; Automation control; Scheduled scenario; Scheduled scenario PLUS |

The Module count is four; the Object-option count is eleven.

### Firmware-scoped configuration

Section ID: `ownkb:section:d000003:s000008`

Applicability cues: `firmware`
Provenance cues: `database`

`EN_CONF` contains both Object-scoped and firmware-scoped definitions. Firmware-scoped rows use:

- `id_key_object = 0`
- an `id_firmware` resolving to `EN_FIRMWARE`.

The canonical database contains 1,463 such rows. They represent configuration that cannot be attributed solely to a reusable Object definition.

Object-scoped rows use the complementary pattern described in [Configuration](configuration.md).

### Default and fixed capability

Section ID: `ownkb:section:d000003:s000009`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`, `evidence`

`EN_SLOTS.fixed_ko` distinguishes one Object association from alternatives at a slot. In many firmware definitions exactly one association per slot carries `fixed_ko = 1`.

The database column name is evidence for a fixed/designated Object relationship. It is not, by itself, sufficient to decide every user-interface behavior:

- whether Function type is visible
- whether the user can change it
- whether another Object is selected automatically
- whether a Device variant hides alternatives.

Those behaviors require catalogue conditions, filters, and observed UI behavior.

### Firmware example

Section ID: `ownkb:section:d000003:s000010`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Firmware `157`, used by `64391`, `64191`, and `64192`, declares four `slot` positions and multiple Object alternatives. Its physical conditions select among those alternatives. For example, the catalogue condition `M1=CEN;M2=O/I` selects Objects `[6, 6, 400, 400]` across slots `1..4`. Treat this as an output of the generic resolver, not as a hard-coded firmware topology. See [Physical-configuration resolution](../internals/catalogue-resolution.md#worked-example-firmware-157).

### Sources

Section ID: `ownkb:section:d000003:s000011`

Applicability cues: `firmware`, `version`
Provenance cues: `source`

[`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) defines Firmware capabilities. [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) defines the diagnostic firmware-version response; observed traffic supplies the version returned by an installed Device. These values are correlated only when the selection is corroborated.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy.

# Document: ownkb:document:d000004

Source path: `device-model/modules.md`
Namespace context: `contextual`
Area: `device-model`

## Modules

Section ID: `ownkb:section:d000004:s000001`

Applicability cues: `firmware`

A Module is a firmware-exposed logical container within a Physical Device. A Device can expose one or more Modules, each located by a `slot`.

### Terminology

Section ID: `ownkb:section:d000004:s000002`

Applicability cues: `firmware`
Uncertainty: `may`
Provenance cues: `catalogue`

**Module** is the preferred term for the logical units presented by a Device in MyHOME_Suite and by the diagnostic protocol.

**`slot`** refers specifically to the numeric position used in catalogue structures and diagnostic frames. The `slot` locates the Module; it is not the Moduleâ€™s functional address.

The following must remain distinct:

| Term | Meaning |
| --- | --- |
| Physical Device | Installed hardware product |
| Module | Firmware-exposed logical container |
| `slot` | Numeric position locating a Module |
| Object | Logical function assigned to a Module |
| UI position | User-facing order or label, which may differ from the `slot` |
| Functional address | Address configured on an Object |

### Firmware-declared Module count

Section ID: `ownkb:section:d000004:s000003`

Applicability cues: `firmware`
Provenance cues: `catalogue`

`EN_FIRMWARE.slots` declares the number of `slot` positions for a firmware definition.

This is the closest catalogue representation of the Module count, but it is not the number of rows in `EN_SLOTS`. The latter records Object alternatives and can contain several rows for one `slot`.

Examples:

| Firmware | Declared slots | Slot/Object rows | Interpretation |
| --- | --- | --- | --- |
| `157` | `4` | `11` | four Modules with multiple Object alternatives |
| `145` | `2` | `8` | two command Modules, four Object alternatives per slot |
| `590` | `2` | `3` | two dimmer Modules; one slot carries an additional combined alternative |
| `194` | `1` | `1` | one fixed Light actuator Module |

### Catalogue slot representation

Section ID: `ownkb:section:d000004:s000004`

The primary path is:

`EN_FIRMWARE` â†’ `AS_OBJECT_FIRMWARE` â†’ `EN_SLOTS`

#### `AS_OBJECT_FIRMWARE`

Section ID: `ownkb:section:d000004:s000005`

Applicability cues: `firmware`

This association states that a firmware supports an Object:

| Column | Role |
| --- | --- |
| `id_object_firmware` | Association identifier |
| `id_firmware` | Firmware definition |
| `id_key_object` | Supported Object |

#### `EN_SLOTS`

Section ID: `ownkb:section:d000004:s000006`

Applicability cues: `firmware`, `revision`
Provenance cues: `catalogue`, `database`, `source`

This table places a firmware/Object association at a `slot`:

| Column | Role |
| --- | --- |
| `id_slot` | Slot-assignment record |
| `first_slot` | `slot` at which the Object association starts |
| `fixed_ko` | Marks the designated/fixed Object association in the catalogue data |
| `id_object_firmware` | Firmware/Object association |

All 1,725 `slot` records resolve to an `AS_OBJECT_FIRMWARE` association in the canonical database.

`first_slot` covers `1..17` in this source revision. That is observed catalogue coverage, not a universal protocol limit; `OPEN.db` permits diagnostic `[SLOT]` values in `1..255`.

### Object alternatives at a Module

Section ID: `ownkb:section:d000004:s000007`

Cautions: `must not`

A Module can expose:

- one Object only
- one designated Object plus alternatives
- a Virgin Object template that permits a set of Objects
- a fixed Object whose configuration is still editable
- no user-visible Object in a particular Device/UI context.

`fixed_ko` must not be translated mechanically into â€œFunction type not user modifiableâ€. The visible behavior can also depend on Virgin Object associations, conditions, filters, and product-specific UI rules.

#### Combined Device example

Section ID: `ownkb:section:d000004:s000008`

Applicability cues: `firmware`

Firmware `157`, used by `64391`, `64191`, and `64192`, shows why Object alternatives cannot be counted as Modules:

| `slot` | Designated Object | Additional Objects |
| --- | --- | --- |
| `1` | Light actuator | Automation actuator |
| `2` | Light actuator | - |
| `3` | Light control | Automation control; Scheduled scenario; Scheduled scenario PLUS |
| `4` | Light control | Automation control; Scheduled scenario; Scheduled scenario PLUS |

The Physical Device therefore has four Modules, with eleven `slot`/Object alternatives.

### Diagnostic Module enumeration

Section ID: `ownkb:section:d000004:s000009`

Provenance cues: `catalogue`, `database`, `evidence`

`OPEN.db` defines the Module/Object response:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

| Field | Database description | Range |
| --- | --- | --- |
| `SLOT` | â€œko slotâ€ | `1..255` |
| `KEYO` | â€œdevice object modelâ€ | `1..65535` |
| `STATE` | â€œconfigured or not configuredâ€ | `0..1` |

This response exposes the Deviceâ€™s current Module/Object state:

- `SLOT` locates the Module
- `KEYO` identifies the regular configured Object when `STATE = 0`, or the Virgin Object representing a disabled Module when `STATE = 1`
- `STATE` reports the Module's enabled/disabled state.

Resolve `KEYO` against `EN_KEY_OBJECT.key_object` for `STATE = 0` and `EN_VIRGIN_OBJECT.virgin_key_object` for `STATE = 1`. The polarity is established by controlled diagnostic/programming evidence correlated with MyHOME_Suite UI behavior; catalogue identity corroborates the selected namespace. It is not a cross-database foreign key.

#### Address response

Section ID: `ownkb:section:d000004:s000010`

`OPEN.db` defines:

`*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##`

This reports a system and address for the Object at a `slot`. It does not redefine the Module itself as an address.

#### Configuration response

Section ID: `ownkb:section:d000004:s000011`

`OPEN.db` defines:

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

Here `SLOT` selects the Module whose configuration property is being reported. `INDEX` selects the configuration property and `VAL_PAR` carries its value.

### Enabled, disabled, absent, and fixed

Section ID: `ownkb:section:d000004:s000012`

Applicability cues: `firmware`
Provenance cues: `catalogue`

These states are distinct:

| State | Meaning |
| --- | --- |
| Enabled | Module exists, `DIMENSION 30.STATE = 0`, and its regular configured Object applies |
| Disabled | Module exists, `DIMENSION 30.STATE = 1`, and its Virgin Object represents the Module |
| Absent from UI | MyHOME_Suite does not present the `slot` in that context |
| Fixed-function | Catalogue/UI does not allow selection of another Object |
| Alternative Object | Firmware supports another Object at the same `slot` |

For `DIMENSION 30`, a captured `STATE` value establishes enabled versus disabled under the corrected polarity, but it does not establish the other UI distinctions in this table.

For example, Device `007B269D` was observed with `slot` `1` disabled, `slot` `2` absent from the UI, and `slot` positions `3` and `4` displayed under shifted UI numbering. This demonstrates that UI position and `slot` cannot be assumed identical.

### Hardware-backed and logical Modules

Section ID: `ownkb:section:d000004:s000013`

Applicability cues: `firmware`
Provenance cues: `catalogue`

A Module can correspond directly to hardware, such as:

- a relay output
- a dimmer output
- a pushbutton pair
- a dry-contact input
- a sensor
- an IR scenario channel.

It can also represent a logical capability exposed by firmware. The catalogue establishes availability but does not always describe the physical implementation.

Command-only Devices such as `64360` expose Light control Objects as their actual hardware function. Those Objects are not alternate configurations of a hidden actuator.

### Repeated Modules

Section ID: `ownkb:section:d000004:s000014`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Some firmware definitions expose repeated Modules with the same Object vocabulary. Repetition does not make the Modules interchangeable at runtime: each `slot` can have its own Object selection, address, groups, and parameters.

The IP55 PIR sensor observed as Device `08CF44BF` illustrates a large Module set: one sensor Module plus optional IR scenario-control Modules across later slots. The catalogueâ€™s maximum observed `first_slot` of `17` is consistent with this class of Device.

### Conditions attached to slots

Section ID: `ownkb:section:d000004:s000015`

Provenance cues: `catalogue`, `database`

`AS_SLOT_CONDITION` associates `EN_SLOTS.id_slot` with `EN_CONDITION.id_condition`. The canonical database contains 1,000 such associations.

Conditions can restrict whether a slot/Object association is applicable. `EN_CONDITION` references `EN_CONV_RULE`, which expresses configuration-dependent logic. Therefore, the raw existence of an `EN_SLOTS` row establishes catalogue capability, not unconditional availability in every configuration.

### Sources

Section ID: `ownkb:section:d000004:s000016`

Provenance cues: `source`

[`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) defines declared slots, Object alternatives, and slot conditions. [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) defines the `DIMENSION 30`, `32`, and `35` wire structures. Observed traffic and MyHOME_Suite behavior establish the Modules actually reported, displayed, and editable.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy.

# Document: ownkb:document:d000005

Source path: `device-model/objects.md`
Namespace context: `contextual`
Area: `device-model`

## Objects

Section ID: `ownkb:section:d000005:s000001`

An Object is the logical function exposed by or assigned to a Module. It defines what that Module does, not the identity of the Physical Device containing it.

### Catalogue identity

Section ID: `ownkb:section:d000005:s000002`

Provenance cues: `catalogue`, `database`, `documentation`, `source`

`EN_KEY_OBJECT` in `MHCatalogue.db` contains 158 Object definitions.

| Column | Role |
| --- | --- |
| `id_key_object` | Internal database key |
| `key_object` | External/catalogue Object number |
| `descr` | Object description |
| `slots` | Object-level slot metadata stored as text |
| `visible` | Catalogue/UI visibility |
| `id_family` | Object-family reference |

The two Object identifiers serve different purposes:

- `id_key_object` joins catalogue tables
- `key_object` is the Object number exposed in the wider MyHOME_Suite model and correlated with diagnostic `KEYO`.

Documentation uses **Object**, not â€œKOâ€, except when quoting database column names or source descriptions.

### Device and Object descriptions

Section ID: `ownkb:section:d000005:s000003`

Provenance cues: `source`

The Device and Object answer different questions:

| Question | Source |
| --- | --- |
| What physical product is installed? | `EN_DEVICE.name` |
| What shared product/capability item does it use? | `EN_ITEM.descr` |
| What logical function does one Module expose? | `EN_KEY_OBJECT.descr` |

A Device can therefore have one standard Device description and several Object descriptions.

For example, `64391` is catalogued as â€œFlush mounted actuator and free controlâ€. Its Modules can expose Objects including:

- `6`: Light actuator
- `7`: Automation actuator
- `400`: Light control
- `401`: Automation control
- `404`: Scheduled scenario
- `406`: Scheduled scenario PLUS.

None of those individual Object descriptions is a complete Device-model name.

### Firmware and slot availability

Section ID: `ownkb:section:d000005:s000004`

Applicability cues: `firmware`
Provenance cues: `database`

Objects become available to a Device through:

`EN_FIRMWARE` â†’ `AS_OBJECT_FIRMWARE` â†’ `EN_SLOTS`

The canonical database contains:

- 827 firmware/Object associations
- 1,725 slot/Object placements.

A reusable Object can appear in many firmware definitions and at many slots. The same Object semantics can therefore be shared by different product models.

### Object-system associations

Section ID: `ownkb:section:d000005:s000005`

Cautions: `not evidence`
Provenance cues: `catalogue`, `database`, `evidence`

`AS_OBJECT_SYSTEM` associates an Object with a catalogue system. The canonical database contains 251 such rows.

This is a catalogue relationship. `EN_SYSTEM.id_system` in `MHCatalogue.db` is not the same identifier space as:

- functional OpenWebNet `WHO`
- diagnostic `WHO`
- `EN_SYSTEM.id_system` in `OPEN.db`
- ScenarioDevices `FamilyId`
- ScenarioDevices `ObjectId`.

A functional-system mapping can be made when the Objectâ€™s semantics, functional frame, or another explicit association establishes it. Numeric equality alone is not evidence.

### Diagnostic Object identity

Section ID: `ownkb:section:d000005:s000006`

Provenance cues: `catalogue`

`OPEN.db` defines:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

`KEYO` is described as the â€œdevice object modelâ€ and has range `1..65535`. When `STATE = 0`, `EN_KEY_OBJECT.key_object` supplies the corresponding regular configured Object number for an enabled Module. When `STATE = 1`, resolve against `EN_VIRGIN_OBJECT.virgin_key_object` for the disabled Module instead; see [Virgin Objects](virgin-objects.md).

This mapping is structurally and behaviorally supported, but there is no foreign key between the two databases. A decoder should retain both the raw `KEYO` value and the resolved catalogue Object record.

### Object roles

Section ID: `ownkb:section:d000005:s000007`

Cautions: `do not`
Provenance cues: `catalogue`

Objects can represent several roles:

| Role | Examples |
| --- | --- |
| Command | Light control, Automation control, AUX control |
| Actuator | Light actuator, Automation actuator, Dimmer actuator |
| Sensor | Daylight sensor, motion/presence sensor |
| State/input | Contact state |
| Scenario | Scheduled scenario, Scheduled scenario PLUS |
| Interface | Bus or system integration Objects |
| Temperature Control | Thermostat, probe, relay, fan-coil functions |
| Energy/access/hotel | Domain-specific functions represented by catalogue systems |

These roles describe logical function. They do not prove that every Device exposing the Object contains identical hardware.

### Command and Device Objects

Section ID: `ownkb:section:d000005:s000008`

`AS_KO_CMD_KO_DEV` records explicit command-Object to Device-Object pairings:

| Column | Role |
| --- | --- |
| `key_object_cmd` | Command Object number |
| `key_object_cmd_desc` | Command Object description |
| `key_object_dev` | Device/actuator Object number |
| `key_object_dev_desc` | Device/actuator Object description |

This table can establish that a command Object is intended to control a particular class of Device Object. It does not make the two Objects identical.

### Object families and collections

Section ID: `ownkb:section:d000005:s000009`

Provenance cues: `catalogue`

Additional catalogue relationships include:

- `EN_OBJECT_ITEM_FAMILY`: Object/item family vocabulary
- `AS_OBJECT_COLLECTION`: Object membership in collections
- `AS_OBJECT_FUNCTION`: special-function associations
- `AS_ICON_KO`: Object icons, subtypes, and modifiability metadata
- `AS_OBJECT_VIRGIN_OBJECT`: Objects permitted by a Virgin Object
- `RIF_MH_OBJECT`: installation/project Object instances with addresses and collection membership.

`RIF_MH_OBJECT` describes project-instance data structures, whereas `EN_KEY_OBJECT` describes reusable catalogue Object types.

### Functional OpenWebNet projection

Section ID: `ownkb:section:d000005:s000010`

Provenance cues: `catalogue`, `documentation`

Functional `WHO` documentation describes runtime frames emitted or consumed by configured Objects. It does not define the product hierarchy.

Examples:

- Light control and Light actuator Objects participate in Lighting traffic under `WHO 1`.
- Automation control and Automation actuator Objects participate in Automation traffic under `WHO 2`.
- Scenario Objects can participate in `WHO 0`, `WHO 15`, `WHO 17`, or `WHO 25`, depending on the function.
- Temperature Control Objects use `WHO 4`.

An Object label is not enough to manufacture a frame mapping. The mapping must be supported by the public protocol, an exact frame template, catalogue association, or observed traffic.

### ScenarioDevices evidence

Section ID: `ownkb:section:d000005:s000011`

Provenance cues: `catalogue`, `database`

The two ScenarioDevices databases describe scenario-engine capabilities through their own `ObjectSystems`, `DeviceObjects`, `Commands`, and `Parameters` tables.

They contain:

| Database | Object systems | DeviceObjects | Commands | Parameters |
| --- | --- | --- | --- | --- |
| Program Files copy | 29 | 44 | 157 | 42 |
| ProgramData copy | 27 | 42 | 151 | 40 |

These Object IDs are not `EN_KEY_OBJECT.key_object` in `MHCatalogue.db`. ScenarioDevices contributes:

- user-facing action/trigger/condition semantics
- exact functional frames where `Commands.Frame` is populated
- parameter limits for scenario commands.

It does not determine which Physical Device or `slot` exposes a catalogue Object.

See [cross-database functional coverage](../functional/cross-database-coverage.md) for the supported intersections.

### Object-scoped configuration

Section ID: `ownkb:section:d000005:s000012`

Applicability cues: `firmware`
Provenance cues: `database`

An Object can own reusable configuration definitions. In `EN_CONF`, Object-scoped rows use:

- an `id_key_object` resolving to `EN_KEY_OBJECT`
- `id_firmware = 0`.

The canonical database contains 1,420 Object-scoped configuration rows. Firmware-scoped configuration uses the complementary pattern described in [Configuration](configuration.md).

### Light-control-only Devices

Section ID: `ownkb:section:d000005:s000013`

Cautions: `must not`

The observed Devices `00C44420`, `00C443B9`, `00C4442E`, `00C44456`, `00C4445F`, and `00C4446E` expose Light control functionality without light-actuator hardware.

For these Devices, a Light control Object is their actual command hardware function. It must not be described as an alternate configuration of a light actuator merely because actuator and command Objects participate in the same functional `WHO`.

### Object `406`

Section ID: `ownkb:section:d000005:s000014`

Provenance cues: `catalogue`

Object `406` is catalogued as â€œScheduled scenario PLUSâ€. On products such as `64360` and the command Modules of `64391`, it is one of the Object choices offered at a Module.

Its catalogue presence establishes that the Module can expose that logical function. Its complete runtime and programming behavior must be documented from the relevant scenario protocol and observed traffic, not inferred from the Object number alone.

### Sources

Section ID: `ownkb:section:d000005:s000015`

Provenance cues: `catalogue`, `source`

[`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) defines catalogue Object identity and availability. [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) defines the diagnostic Object projection. ScenarioDevices and the [public OpenWebNet documents](../sources/openwebnet-public/) describe adjacent scenario and functional semantics.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy.

# Document: ownkb:document:d000006

Source path: `device-model/physical-devices.md`
Namespace context: `contextual`
Area: `device-model`

## Physical Devices

Section ID: `ownkb:section:d000006:s000001`

Provenance cues: `catalogue`

A Physical Device is one installed hardware product instance. It is the root of the Device â†’ Module â†’ Object â†’ Configuration model, but the catalogue describes the product model while diagnostic traffic identifies the individual installed instance.

### Catalogue identity

Section ID: `ownkb:section:d000006:s000002`

Applicability cues: `gateway`
Provenance cues: `catalogue`, `database`

The principal Device record is `EN_DEVICE` in `MHCatalogue.db`.

| Column | Role |
| --- | --- |
| `id_device` | Internal catalogue Device-record identifier |
| `code` | Product code or SKU |
| `name` | Standard MyHOME_Suite-facing Device description |
| `descr` | Additional catalogue description |
| `id_item` | Shared product/capability item |
| `id_brand` | Brand reference |
| `id_line` | Product-line or aesthetic-line reference |
| `visible`, `visibility_type` | Catalogue/UI visibility data |
| `dependent` | Marks a dependent Device record |
| `is_gateway` | Marks a gateway Device record |

All 541 Device rows in the canonical database resolve to an `EN_ITEM`, `EN_BRAND`, and `EN_LINE` row. The canonical database declares few of these relationships as foreign keys; the joins are nevertheless complete in this dataset.

#### Device, item, and SKU

Section ID: `ownkb:section:d000006:s000003`

Applicability cues: `firmware`
Provenance cues: `catalogue`

`EN_DEVICE.code` is the product code presented in the catalogue. It is not a language code. All 541 canonical Device rows contain a distinct non-null product code. Treating this column as a reference to `EN_LANGUAGE.code` would destroy valid SKU data.

Several branded products can share one `EN_ITEM` capability definition. For example, products `64391`, `64191`, and `64192` all select item `1184`, named â€œFlush mounted actuator and free controlâ€. They therefore share the same firmware, Module, Object, and configuration capability model while retaining distinct catalogue Device records.

#### Preferred description

Section ID: `ownkb:section:d000006:s000004`

Cautions: `do not`
Provenance cues: `catalogue`

When identifying a scanned physical product, use `EN_DEVICE.name` as the standard Device description. Do not substitute:

- `EN_ITEM.descr`, which describes the shared capability item
- `EN_KEY_OBJECT.descr`, which describes one logical Object
- a user-interface suffix added outside the catalogue
- an inferred class derived from one Module.

This preserves the distinction between â€œwhat product is installed?â€ and â€œwhat functions does it expose?â€.

### Catalogue systems and model identity

Section ID: `ownkb:section:d000006:s000005`

Cautions: `must not`
Provenance cues: `catalogue`

`AS_ITEM_SYSTEM` associates an item with a catalogue system:

| Column | Meaning |
| --- | --- |
| `id_item` | Product/capability item |
| `id_system` | Catalogue system |
| `modobj` | Item-level model value |
| `main` | Marks the main system association |

`EN_SYSTEM` in `MHCatalogue.db` is a catalogue namespace. Its `id_system` values must not be numerically joined to `EN_SYSTEM.id_system` in `OPEN.db`.

The item-level `modobj`, `EN_BRAND.brand_modobj`, and `EN_LINE.line_modobj` correlate with the `OBJECT_MODEL`, `BRAND`, and `LINE` values carried by diagnostic `DIMENSION 1`. This gives a supported identification path:

`DIMENSION 1` â†’ item/system model + brand + line â†’ catalogue item â†’ matching Device records

The path can yield several branded SKUs when multiple Device records share the same item and diagnostic identity values.

### Installed-instance identity

Section ID: `ownkb:section:d000006:s000006`

Provenance cues: `documentation`

The product code is not the bus instance identifier. `OPEN.db` defines the Device-ID response as:

`*#[WHO]*[WHERE]*13*[ID]##`

The `[ID]` parameter spans `0..4294967295`. Captured Device IDs are represented as eight hexadecimal characters in this documentation, preserving leading zeroes.

A Device ID identifies an installed physical instance. It is not:

- `EN_DEVICE.id_device`
- a SKU
- the item-level `modobj`
- an Object identifier
- a `slot`
- a configured functional address.

### Diagnostic identity dimensions

Section ID: `ownkb:section:d000006:s000007`

Applicability cues: `firmware`, `version`
Provenance cues: `catalogue`, `database`

The implementation database defines these Device-level identity responses:

| `DIMENSION` | Frame values | Scope |
| --- | --- | --- |
| `1` | `OBJECT_MODEL`, `N_CONF`, `BRAND`, `LINE` | Catalogue/model identity |
| `2` | `FW_VERSION` | Firmware version |
| `3` | `HW_VERSION` | Hardware version |
| `6` | `MICRO_VERSION` | Microcontroller version |
| `13` | `ID` | Installed-instance identifier |

`OPEN.db` describes `N_CONF` as â€œConfigurator numberâ€ and allows `0..12` for the ordinary addressed diagnostic form. Comparison with product configuration diagrams indicates that, in that addressed Device form, `N_CONF` represents the number of physical configurator positions provided by the Device.

#### `N_CONF` and physical configurators

Section ID: `ownkb:section:d000006:s000008`

Applicability cues: `firmware`, `gateway`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`

The interpretation is supported by Devices whose physical configuration layouts are documented independently:

| Device | `N_CONF` | Documented physical positions |
| --- | --- | --- |
| `F420` | `2` | 2 |
| `F429` | `3` | 3 (`A`, `G`, `M`) |
| `H4652/3` | `7` | 7 |

The correspondence across Devices with different values argues against interpreting ordinary addressed-form `N_CONF` as a Module count or general Device classification. In that corroborated scope, it describes the size of the Device's physical configurator interface.

The catalogue registers Physical configuration, Virtual Configuration, Advanced Configuration, and Product Programming as distinct modes, and a firmware can support more than one of them. Physical configuration constrains values to those representable by the firmware's demonstrated physical definitions. In the ordinary addressed Device form, `N_CONF` describes the physical configurator positions provided by the hardware, not the number of logical configuration parameters or the active configuration mode.

The empty-`WHERE` gateway identity form is a separate variant. Observed MH202 and F454 responses both carry `N_CONF = 15`, which is outside the ordinary addressed-form `0..12` range. Numerically, `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern, so a reserved or sentinel interpretation is plausible; its exact meaning is unresolved. Do not treat that gateway value as a proven physical-position count. See [`DIMENSION 1`: Device Identity](../diagnostics/dim1-device-identity.md#gateway-variant).

The ordinary addressed-form interpretation remains to be checked against additional Devices, particularly older products for which configuration diagrams are less readily available.

### Physical composition

Section ID: `ownkb:section:d000006:s000009`

Physical form and logical composition are separate properties. The recurring Device classes used by this reference are:

| Class | Characteristic | Examples |
| --- | --- | --- |
| Actuator-only | Hardware outputs without independently configurable command Modules | `F411U2` |
| Dimmer-only | Dimming outputs without independent command Modules | `F418U2` |
| Command-only | Input hardware exposing command Objects but no actuator hardware | `64360` |
| Combined actuator and free command | Actuator Modules plus independently configurable command Modules | `64391`, `64191`, `64192` |
| Actuator with hard-linked controls | Local buttons always operate built-in outputs | `H4661M2` |

The classification describes hardware composition. It does not define the Deviceâ€™s diagnostic identity values.

### Worked catalogue examples

Section ID: `ownkb:section:d000006:s000010`

#### `64391`, `64191`, and `64192`

Section ID: `ownkb:section:d000006:s000011`

Applicability cues: `firmware`

These three SKUs share item `1184`, item model `107`, and firmware `157`. The firmware declares four `slot` positions:

| Slots | Capability |
| --- | --- |
| `1..2` | actuator Object candidates |
| `3..4` | command/scenario Object candidates |

The exact Object selected in each slot can depend on physical configurator conditions. For example, `M1=CEN;M2=O/I` resolves to Objects `[6, 6, 400, 400]`; other reachable condition branches must be evaluated from the firmware's legal configurator domains. This is a combined Device, but the per-configuration topology should be derived rather than stored as an unconditional four-Module rule.

#### `64360`

Section ID: `ownkb:section:d000006:s000012`

Provenance cues: `catalogue`

SKU `64360` resolves to item `281`, â€œBasic controlâ€, with two command Modules. Its catalogue Object choices include Light control, Automation control, Scheduled scenario, and Scheduled scenario PLUS. No actuator Object is exposed by this item.

#### `F411U2`

Section ID: `ownkb:section:d000006:s000013`

Applicability cues: `firmware`

SKU `F411U2` resolves to item `2115`, â€œ2x10A actuator, 2DINâ€, and firmware `659`, which declares two slots. Both slots expose actuator capability.

#### `F418U2`

Section ID: `ownkb:section:d000006:s000014`

Applicability cues: `firmware`

SKU `F418U2` resolves to item `2065`, â€œ2x1,6A universal dimmer, 4DINâ€, and firmware `590`, which declares two dimmer slots.

#### `3476` and `3477`

Section ID: `ownkb:section:d000006:s000015`

SKU `3476` is a one-slot Basic control actuator. SKU `3477` is a two-slot Basic contacts interface whose Modules can expose contact-state and command functions. Similar physical installation style therefore does not imply the same logical composition.

### Dependent Devices and interfaces

Section ID: `ownkb:section:d000006:s000016`

Applicability cues: `gateway`
Cautions: `do not`
Provenance cues: `catalogue`

The catalogue contains additional Device-level associations:

- `AS_DEPENDENT_DEVICES` links master and dependent Device records.
- `AS_BUS_ITEM`, `AS_BUS_SYSTEM`, and `AS_BUS_INTERFACE` describe bus compatibility and interface roles.
- `AS_DEVICE_PICTURE` associates Device records with catalogue imagery.
- `EN_DEVICE.is_gateway` distinguishes gateway products.
- `EN_DEVICE.dependent` identifies dependent products.

These tables describe catalogue relationships. They do not by themselves establish diagnostic enumeration behavior.

### Address boundaries

Section ID: `ownkb:section:d000006:s000017`

Applicability cues: `scs`

A Device can carry several kinds of address:

1. a Device-level address used for discovery or interview;
2. configured functional addresses belonging to individual Modules/Objects;
3. installation-wide groups, environments, zones, CEN identifiers, or other system-specific associations.

For SCS Lighting/Automation Devices, the diagnostic `WHERE` of a Physical Device can resemble an `A`/`PL` address. That resemblance does not establish that every Device uses the first Moduleâ€™s configured address. The relationship must be documented per family or per verified behavior.

### Sources

Section ID: `ownkb:section:d000006:s000018`

Provenance cues: `evidence`, `source`

[`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) defines Device, item, brand, line, dependency, and bus records. [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) defines Device-identity frames and parameter ranges. Observed traffic and MyHOME_Suite behavior establish installed-instance values and displayed Device descriptions. Product configuration diagrams provide independent evidence for the physical configurator layouts used to interpret ordinary addressed-form `N_CONF`.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy and [`sources/manifest.yaml`](../sources/manifest.yaml) for provenance.

# Document: ownkb:document:d000007

Source path: `device-model/sources-and-identifiers.md`
Namespace context: `contextual`
Area: `device-model`

## Sources and Identifier Boundaries

Section ID: `ownkb:section:d000007:s000001`

The Device model is reconstructed from several sources that describe different layers of the implementation. They are complementary, not interchangeable.

### Canonical-source policy

Section ID: `ownkb:section:d000007:s000002`

Provenance cues: `capture`, `documentation`, `evidence`

The canonical evidence corpus is under [`sources/`](../sources/). Original evidence is preserved byte-for-byte. Provenance, byte sizes, original installation paths, and SHA-256 fingerprints are recorded in [`sources/manifest.yaml`](../sources/manifest.yaml).

Derived relationships and interpretations belong in documentation, not in the canonical databases.

Private packet captures are intentionally excluded from the repository. Findings supported by them can be documented without publishing installation-specific capture data.

### Evidence matrix

Section ID: `ownkb:section:d000007:s000003`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `evidence`, `source`

| Source | Strongest evidence | Does not independently establish |
| --- | --- | --- |
| [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Product catalogue, firmware capabilities, `slot` positions, Objects, Virgin Objects, configuration definitions and constraints | Exact runtime frame order or complete functional protocol |
| [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) | Systems, diagnostic families, frame templates, parameters, address rules, sequences, and timeouts | Complete Device catalogue or complete functional command vocabulary |
| [`OpenQuery.txt`](../sources/myhome-suite/3.5.38/support/OpenQuery.txt) | Queries used by MyHOME_Suite to assemble `OPEN.db` frames, sequences, address rules, and timeouts | Additional semantics absent from the queried tables |
| [ScenarioDevices databases](../sources/myhome-suite/3.5.38/databases/) | Scenario-engine Object systems, actions, triggers, conditions, frames, and parameter limits | Physical Device, firmware, Module, or catalogue Object identity |
| [`rules.db3`](../sources/myhome-suite/3.5.38/databases/rules.db3) | Cross-property validation for selected Temperature Control Objects | General Object registry or functional `WHO` mapping |
| [public OpenWebNet documents](../sources/openwebnet-public/) | Published frame syntax and functional behavior | MyHOME_Suite catalogue hierarchy or unpublished diagnostic semantics |
| Observed traffic | Actual values, ordering, repetition, and Device behavior | Universal support outside the observed Devices and versions |
| MyHOME_Suite UI | Display labels, field visibility, editability, and product-specific behavior | Wire encoding unless correlated with traffic or implementation data |

### Independent identifier spaces

Section ID: `ownkb:section:d000007:s000004`

Applicability cues: `firmware`
Cautions: `must not`
Provenance cues: `catalogue`, `database`, `evidence`

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
| `EN_SLOTS.first_slot` | `slot` position |
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

### Supported cross-source correlations

Section ID: `ownkb:section:d000007:s000005`

#### Diagnostic Device model

Section ID: `ownkb:section:d000007:s000006`

Applicability cues: `firmware`, `gateway`
Cautions: `must not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `documentation`, `evidence`

`OPEN.db` `DIMENSION 1` uses `OBJECT_MODEL`, `N_CONF`, `BRAND`, and `LINE`.

Supported counterparts and interpretations are:

| Diagnostic field | Catalogue/documentation counterpart | Status |
| --- | --- | --- |
| `OBJECT_MODEL` | `AS_ITEM_SYSTEM.modobj` | Corroborated |
| `BRAND` | `EN_BRAND.brand_modobj` | Corroborated |
| `LINE` | `EN_LINE.line_modobj` | Corroborated |
| `N_CONF` | physical configurator positions shown in product documentation for the ordinary addressed Device form | Corroborated across documented addressed Devices; no direct `MHCatalogue.db` field identified |

`OPEN.db` describes ordinary addressed-form `N_CONF` as the configurator number / number of physical configurators. Product diagrams for Devices including `F420`, `F429`, and `H4652/3` independently match their `N_CONF` values to the number of physical configurator positions. In that addressed Device scope, treat it as a hardware-interface count, not as a Module, Object, Virgin Object, or firmware classification.

The separate empty-`WHERE` gateway identity form must not inherit that interpretation automatically. Observed MH202 and F454 gateway tuples both contain `N_CONF = 15`, outside the ordinary `0..12` range. `15` is numerically `0xF`; viewed in four bits, it is `1111`, an all-ones pattern consistent with a sentinel convention but not proof of one. Preserve gateway `N_CONF` as an unresolved raw field unless stronger evidence establishes its semantics.

#### Diagnostic Object identity

Section ID: `ownkb:section:d000007:s000007`

Provenance cues: `catalogue`

| Diagnostic field | Catalogue field | Status |
| --- | --- | --- |
| `DIMENSION 30.KEYO`, `STATE = 0` | `EN_KEY_OBJECT.key_object` | Enabled Module, regular configured Object; polarity experimentally corroborated with UI behavior |
| `DIMENSION 30.KEYO`, `STATE = 1` | `EN_VIRGIN_OBJECT.virgin_key_object` | Disabled Module, Virgin Object; polarity experimentally corroborated with UI behavior |
| `DIMENSION 30.SLOT` | `slot` represented by `EN_SLOTS.first_slot` | Structurally corroborated |
| `DIMENSION 30.STATE` | no single catalogue column | Enabled/disabled runtime state; `OPEN.db` labels it generically, while controlled experiments establish numeric polarity |

#### Diagnostic configuration

Section ID: `ownkb:section:d000007:s000008`

Uncertainty: `unresolved`
Provenance cues: `catalogue`

| Diagnostic field | Catalogue field | Status |
| --- | --- | --- |
| `DIMENSION 35.INDEX` | `EN_CONF.idx` | Strong terminology and behavior correlation |
| `DIMENSION 35.SLOT` | `slot` | Direct structural role |
| `DIMENSION 35.VAL_PAR` | selected `EN_CONF_RANGE.value` or user value | Context-dependent |
| `DIMENSION 310.VAL_PAR` | no generic indexed mapping | Object-specific and unresolved globally |

#### Temperature Control validation

Section ID: `ownkb:section:d000007:s000009`

Uncertainty: `unresolved`
Provenance cues: `catalogue`, `source`

`rules.db3.rules.KOBJECTS` values `95`, `96`, and `184` align with catalogue Objects Hotel thermostat, Residential thermostat, and Master probe. Its `$N` parameter references align with those Objectsâ€™ `EN_CONF.idx` values.

This is a semantic/structural correlation; the files contain no foreign key.

Cross-source claims in this section are described directly as corroborated, inferred, context-dependent, or unresolved where qualification is necessary.

### Relationship reconstruction

Section ID: `ownkb:section:d000007:s000010`

Applicability cues: `firmware`
Provenance cues: `database`, `documentation`

The canonical `MHCatalogue.db` declares only a small subset of its relationships as foreign keys. A relationship can still be treated as structurally established when:

1. the association-table and column names identify the intended parents;
2. every child value resolves to the proposed parent in the canonical dataset;
3. the cardinality is consistent with the model;
4. dependent queries and UI behavior use the same relationship.

This establishes a documentation join, not permission to modify the canonical database.

Notable complete joins include:

- `EN_DEVICE.id_item` â†’ `EN_ITEM.id_item`
- `EN_DEVICE.id_brand` â†’ `EN_BRAND.id_brand`
- `EN_DEVICE.id_line` â†’ `EN_LINE.id_line`
- `EN_FIRMWARE.id_item` â†’ `EN_ITEM.id_item`
- `AS_OBJECT_FIRMWARE` â†’ firmware and Object
- `EN_SLOTS.id_object_firmware` â†’ `AS_OBJECT_FIRMWARE.id_object_firmware`
- firmware/Virgin-Object and Virgin-Object/Object associations
- `EN_CONF_RANGE.id_conf` â†’ `EN_CONF.id_conf`
- `EN_FILTER` â†’ Object/firmware association and configuration definition.

### Known exclusions and cautions

Section ID: `ownkb:section:d000007:s000011`

#### Device code is not a language relation

Section ID: `ownkb:section:d000007:s000012`

Cautions: `must not`

`EN_DEVICE.code` contains valid product codes and must not be related to `EN_LANGUAGE.code`. This was a false relationship produced by name similarity.

#### Public protocol versus implementation

Section ID: `ownkb:section:d000007:s000013`

Applicability cues: `version`
Provenance cues: `source`

The public documents can predate implementation behavior found in the databases. A difference must be documented as a source/version difference rather than silently reconciled.

#### Scenario Object IDs

Section ID: `ownkb:section:d000007:s000014`

Cautions: `must not`
Provenance cues: `catalogue`

ScenarioDevices Object identifiers are application-level capability IDs. They must not be joined directly to catalogue Object numbers.

#### System IDs

Section ID: `ownkb:section:d000007:s000015`

Provenance cues: `evidence`

`EN_SYSTEM.id_system` in `MHCatalogue.db` and `EN_SYSTEM.id_system` in `OPEN.db` describe different registries. Link them through established system semantics, `WHO`, frame templates, or Device/Object evidence-not through equal numeric IDs.

#### Counts are source-revision facts

Section ID: `ownkb:section:d000007:s000016`

Applicability cues: `revision`
Provenance cues: `database`, `source`

Database row counts document the canonical source revision. They are neither protocol maxima nor claims about all MyHOME products.

# Document: ownkb:document:d000008

Source path: `device-model/virgin-objects.md`
Namespace context: `contextual`
Area: `device-model`

## Virgin Objects

Section ID: `ownkb:section:d000008:s000001`

Provenance cues: `catalogue`

A Virgin Object is a catalogue template that constrains the concrete Objects available to a configurable Module. In diagnostic/programming `DIMENSION 30`, it is the Object identity reported while that Module is disabled.

â€œVirginâ€ describes catalogue capability and the disabled-Module representation used by `DIMENSION 30`, not a separate physical component.

### Catalogue identity

Section ID: `ownkb:section:d000008:s000002`

Cautions: `must not`
Provenance cues: `database`

`EN_VIRGIN_OBJECT` in `MHCatalogue.db` contains 18 definitions.

| Column | Role |
| --- | --- |
| `id_virgin_key_object` | Internal database key |
| `virgin_key_object` | Virgin Object number |
| `descr` | Virgin Object description |

The Virgin Object identifier space is distinct from `EN_KEY_OBJECT.key_object`. Equal numbers must not be treated as equivalent.

### Relationship chain

Section ID: `ownkb:section:d000008:s000003`

Applicability cues: `firmware`
Uncertainty: `may`
Provenance cues: `catalogue`

The catalogue uses three associations:

1. `AS_FIRMWARE_VIRGIN_OBJECT` connects a firmware to a Virgin Object and assigns an intermediate `id_fw_virgin_object`.
2. `EN_SLOT_KO_VIRGIN` places that firmware/Virgin-Object association at one or more `slot` positions.
3. `AS_OBJECT_VIRGIN_OBJECT` lists the concrete Objects permitted by a Virgin Object.

The resulting capability chain is:

`EN_FIRMWARE` â†’ `AS_FIRMWARE_VIRGIN_OBJECT` â†’ `EN_SLOT_KO_VIRGIN` â†’ `slot`

and:

`EN_VIRGIN_OBJECT` â†’ `AS_OBJECT_VIRGIN_OBJECT` â†’ `EN_KEY_OBJECT`

Together they answer: â€œAt this slot under this firmware, which Objects may this configurable Module become?â€

### Canonical coverage

Section ID: `ownkb:section:d000008:s000004`

Applicability cues: `firmware`
Provenance cues: `database`, `source`

The canonical database contains:

| Structure | Rows |
| --- | --- |
| Virgin Objects | 18 |
| Firmware/Virgin-Object associations | 75 |
| Slot placements | 169 |
| Virgin-Object/Object associations | 102 |

Every row in these association tables resolves to its parent record in the canonical data, although the source database does not declare all relationships as foreign keys.

### Capability, not runtime state

Section ID: `ownkb:section:d000008:s000005`

Provenance cues: `catalogue`

A Virgin Object relationship establishes that an Object is permitted by the catalogue. It does not establish that:

- an installed Module currently uses that Object
- the Object is visible in every UI context
- the user can select it under every configuration
- the Device reported that Object in `DIMENSION 30`
- the Object is enabled
- the Objectâ€™s address or parameters are valid.

Runtime state must be obtained from diagnostic responses or project configuration.

### Examples

Section ID: `ownkb:section:d000008:s000006`

#### Automation double command virgin

Section ID: `ownkb:section:d000008:s000007`

Applicability cues: `firmware`
Provenance cues: `database`

Virgin Object `500`, â€œAutomation double command virginâ€, permits five concrete Objects and is used by six firmware definitions in the canonical database.

For firmware `157`, it is placed at `slot` positions `3` and `4`, whose Object choices include:

- Light control
- Automation control
- Scheduled scenario
- Scheduled scenario PLUS.

This corresponds to the free-command portion of `64391`, `64191`, and `64192`.

#### Automation relay virgin

Section ID: `ownkb:section:d000008:s000008`

Applicability cues: `firmware`

Virgin Object `510`, â€œAutomation relay virginâ€, permits three concrete Objects and is used by five firmware definitions.

For firmware `157`, it is placed at `slot` positions `1` and `2`, corresponding to the relay/actuator Modules.

#### Dimmer actuator virgin

Section ID: `ownkb:section:d000008:s000009`

Applicability cues: `firmware`

Virgin Object `528`, â€œDimmer actuator virginâ€, permits two concrete Objects. It is placed at both `slot` positions of firmware `590`, used by `F418U2`.

#### Contact interface single virgin

Section ID: `ownkb:section:d000008:s000010`

Applicability cues: `firmware`

Virgin Object `512`, â€œContact interface single virginâ€, permits ten Objects. It is placed at both slots of firmware `129`, used by `3477`.

#### Daylight and motion sensor virgin

Section ID: `ownkb:section:d000008:s000011`

Applicability cues: `firmware`

Virgin Object `515`, â€œDaylight and motion sensor virginâ€, permits six Objects and is associated with twelve firmware definitions. This supports a family of sensor configurations but does not by itself define the Object active on a particular Device.

### Virgin Object and `DIMENSION 30`

Section ID: `ownkb:section:d000008:s000012`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`, `evidence`, `source`

`OPEN.db` defines `DIMENSION 30` with `SLOT`, `KEYO`, and `STATE`. The database describes `STATE` only as â€œconfigured or not configuredâ€.

`KEYO` uses a state-dependent external identifier namespace:

| `STATE` | Resolve `KEYO` against | Meaning |
| --- | --- | --- |
| `0` | `EN_KEY_OBJECT.key_object` | enabled Module; regular configured Object |
| `1` | `EN_VIRGIN_OBJECT.virgin_key_object` | disabled Module; Virgin Object and configurable role |

`OPEN.db` supplies the binary field and labels it only generically as â€œconfigured or not configuredâ€; that source does not by itself establish which numeric value means enabled or disabled. Controlled diagnostic/programming protocol evidence correlated with MyHOME_Suite UI behavior establishes `0 = enabled` and `1 = disabled`. Catalogue resolution independently corroborates the corresponding Object namespace.

Retain `STATE` with every `KEYO`: the two external number spaces are independent, and neither value is an internal database primary key. Once the Virgin Object of a disabled Module is resolved, intersect its permitted Objects with the selected firmware and `slot` capability before presenting choices for the regular Object that can apply when enabled.

### Conditions and visibility

Section ID: `ownkb:section:d000008:s000013`

Applicability cues: `firmware`

A permitted Object can still be constrained by:

- `AS_SLOT_CONDITION`
- `EN_CONDITION`
- `EN_CONV_RULE`
- `EN_FILTER` and `EN_FILTER_RANGE`
- firmware-scoped configuration
- MyHOME_Suite UI rules.

Consequently, `AS_OBJECT_VIRGIN_OBJECT` is a compatibility set, not a complete selection algorithm.

### Interpretation procedure

Section ID: `ownkb:section:d000008:s000014`

Applicability cues: `firmware`
Uncertainty: `may`

To determine which Objects a Module may expose:

1. identify the Physical Deviceâ€™s `EN_ITEM`;
2. select the applicable firmware;
3. select the `slot`;
4. locate the firmware/Virgin-Object association for that slot;
5. enumerate the Virgin Objectâ€™s permitted Objects;
6. intersect that set with the firmware/Object rows present at the same slot;
7. apply slot conditions, configuration filters, and observed UI constraints;
8. compare the result with diagnostic `DIMENSION 30`.

The intersection step prevents a global Virgin Object vocabulary from being applied too broadly to a particular firmware.

### Sources

Section ID: `ownkb:section:d000008:s000015`

Provenance cues: `catalogue`, `source`

Virgin Object identity and compatibility are defined by [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db). `OPEN.db` supplies the `KEYO` and binary `STATE` fields; controlled diagnostic/programming experiments correlated with MyHOME_Suite UI behavior establish the polarity, while catalogue resolution corroborates the state-dependent Object/Virgin-Object namespaces. ScenarioDevices is not a Virgin Object registry.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy.

# Document: ownkb:document:d000009

Source path: `diagnostics/README.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## Diagnostics

Section ID: `ownkb:section:d000009:s000001`

Applicability cues: `firmware`, `gateway`, `zigbee`
Provenance cues: `catalogue`, `database`, `evidence`, `source`

The diagnostic protocol discovers installed Physical Devices and reads the runtime projection of their firmware, Modules, Objects, addresses, and configuration. It uses the common OpenWebNet frame language with management-specific `WHO`, `WHAT`, `WHERE`, and `DIMENSION` values.

[OpenWebNet Scope and Architecture](../protocol/scope-and-architecture.md) defines how discovery, interview, detailed configuration reading, runtime control, and programming remain separate mechanisms even when one workflow composes them.

The Suite management model described here is not universal across transports. The ZigBee OpenWebNet source exposes separate discovery surfaces: [`WHO 1000 DIMENSION 81` neighbor discovery](../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) and [`WHO 13` scan/product-database operations](../functional/who-13-integration-gateway/zigbee-network-management.md#discovery-relationship-and-source-conflicts). These are distinct from Suite `WHO 1001 DIMENSION 13` enumeration and Physical Device interview. No inspected evidence establishes that the Suite interview sequences below apply to that interface.

Diagnostics does not expose the catalogue database directly. It reports installed state that can be interpreted against the canonical **Physical Device â†’ Firmware â†’ Module â†’ Object â†’ Configuration** model described in [`device-model/`](../device-model/).

### Reference

Section ID: `ownkb:section:d000009:s000002`

| Subject | Page |
| --- | --- |
| Diagnostic families, sessions, and model projection | [Diagnostic Architecture](architecture.md) |
| Enumeration by Device ID | [Device Discovery](device-discovery.md) |
| Discovery using an address | [Address Discovery](address-discovery.md) |
| Full Device interview | [Device Interview](device-interview.md) |
| Diagnostic `WHAT` values | [Diagnostic `WHAT` Reference](what-reference.md) |
| Diagnostic `DIMENSION` index | [Diagnostic `DIMENSION` Reference](dimension-reference.md) |
| `DIMENSION 1`: Device identity | [`DIMENSION 1`: Device Identity](dim1-device-identity.md) |
| `DIMENSION 30`: Modules and Objects | [`DIMENSION 30`: Modules and Objects](dim30-modules.md) |
| `DIMENSION 32`: Module addressing | [`DIMENSION 32`: Module Addressing](dim32-addressing.md) |
| `DIMENSION 35`: configuration parameters | [`DIMENSION 35`: Configuration Parameters](dim35-configuration.md) |

### Principal workflows

Section ID: `ownkb:section:d000009:s000003`

Applicability cues: `version`
Provenance cues: `evidence`

1. Select the diagnostic `WHO` for the managed system.
2. Discover Device IDs or identify a Device by address.
3. Start an interview by Device ID, address, or local interaction.
4. Collect identity, version, health, Module/Object, and address responses.
5. Read detailed configuration parameters where required.
6. Close the diagnostic session explicitly when the workflow requires it.

The enumeration and interview workflows are distinct. Enumeration finds installed Device instances; interview expands one selected instance into its runtime model.

MyHOME_Suite composes these operations into higher-level scenarios:

| Scenario | Sequence composition in `OPEN.db` |
| --- | --- |
| Point-to-point diagnosis by address | addressed interview â†’ detailed configuration reading â†’ close |
| Point-to-point diagnosis by Device ID | ID interview â†’ detailed configuration reading â†’ close |
| Diagnosis by local interaction | local-button interview â†’ detailed configuration reading â†’ close |
| Plant scan by address | address discovery â†’ repeated addressed interviews â†’ repeated configuration reads â†’ repeated close |
| Plant scan by Device ID | ID enumeration â†’ repeated ID interviews â†’ repeated configuration reads â†’ repeated close |

The sequence composition is implementation evidence from `EN_SCENARIO`, `AS_SCENARIO_SEQUENCE`, and `EN_SEQUENCE`. It does not imply that every Device returns every optional response.

### Diagnostic and functional namespaces

Section ID: `ownkb:section:d000009:s000004`

Provenance cues: `catalogue`, `database`

A diagnostic `WHO` is a management namespace and is not necessarily equal to the functional `WHO` used to operate the Device. Lighting and Automation, for example, use functional `WHO 1` and `WHO 2` while sharing diagnostic `WHO 1001` in the canonical implementation data.

Never infer the diagnostic family by arithmetically transforming a functional `WHO`. Use an established system mapping.

`OPEN.db` represents Lighting and Automation as one system row whose stored functional `WHO` is `1`; it contains no separate `WHO 2` row. The broader `WHO 1001` Lighting/Automation scope is established by the combined system identity, the independent functional specifications, the catalogue Object model, and observed behavior-not by a second literal database mapping. See [Diagnostic Architecture](architecture.md).

### Source roles

Section ID: `ownkb:section:d000009:s000005`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `database`, `source`

| Source | Role in this section |
| --- | --- |
| [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) | diagnostic systems, frame templates, parameter types and ranges, address rules, sequences, repetition flags, and timeouts |
| [`OpenQuery.txt`](../sources/myhome-suite/3.5.38/support/OpenQuery.txt) | the queries MyHOME_Suite uses to assemble systems, frames, sequences, address rules, and timeout behavior from `OPEN.db` |
| [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Physical Device, firmware, Module, Object, Virgin Object, and configuration interpretation |
| [Public OpenWebNet documents](../sources/openwebnet-public/) | common frame syntax and functional `WHO` behavior; they do not define the MyHOME_Suite diagnostic state machines documented here |
| ScenarioDevices databases | adjacent functional/scenario behavior; not diagnostic Object or configuration identity |
| [`rules.db3`](../sources/myhome-suite/3.5.38/databases/rules.db3) | selected Temperature Control configuration constraints; not a diagnostic frame registry |
| Observed traffic | actual ordering, repetition, values, termination, and Device-specific support |
| MyHOME_Suite UI | displayed Device descriptions, Module visibility/numbering, configuration labels, and editability |

The canonical database copies used for this section match the SHA-256 fingerprints in [`sources/manifest.yaml`](../sources/manifest.yaml).

### Evidence limits

Section ID: `ownkb:section:d000009:s000006`

Applicability cues: `firmware`
Uncertainty: `unknown`, `unresolved`
Provenance cues: `capture`, `catalogue`, `database`, `source`

Private packet captures are intentionally excluded from the repository. Capture-supported findings are documented without installation-specific traffic.

Identifier boundaries and cross-source rules are defined once in [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md). In particular, functional `WHO`, diagnostic `WHO`, database system IDs, Object numbers, internal catalogue keys, Device IDs, and functional addresses are independent namespaces unless an explicit correlation is documented.

Observed behavior does not prove universal support across all products, firmware revisions, or diagnostic families. Unknown fields and unverified equivalences remain explicitly unresolved.

### Published family-specific fault diagnostics

Section ID: `ownkb:section:d000009:s000007`

Provenance cues: `database`

[Temperature Control Fault Diagnostics](temperature-control-faults.md) documents the public `WHO 1004` central-unit and zone fault queries, automatic notifications, and active-low bit labels. This is a separate surface from the database-driven Device interview.

# Document: ownkb:document:d000010

Source path: `diagnostics/address-discovery.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## Address Discovery

Section ID: `ownkb:section:d000010:s000001`

Address discovery locates or probes a Device through a diagnostic `WHERE`. It is useful when the functional or installation address is known but the Device ID is not.

### Frames

Section ID: `ownkb:section:d000010:s000002`

Provenance cues: `database`

| Purpose | Frame |
| --- | --- |
| Scan one address | `*#[WHO]*[WHERE]*1##` |
| Identity response | `*#[WHO]*[WHERE]*1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##` |
| Start full addressed interview | `*#[WHO]*[WHERE]*0##` |

`OPEN.db` additionally defines two specialized scan templates:

| Scope | Frame | Database association |
| --- | --- | --- |
| Lighting/Automation room/area | `*#[WHO]*[A]*1##` | general Light/Automation address rule |
| Thermoregulation zone | `*#[WHO]*00[ZAZB]*1##` | general Thermoregulation address rule |

`OPEN.db` names the repeated scan workflow `ScanAddressed`. It sends the generic address scan and expects repeated `DIMENSION 1` identity responses. `ScanAreaTimeWait` gives this step an eight-second default window before advancing to the next area or zone.

The full addressed interview uses a different start frame and can return the broader diagnostic response set. In the higher-level `ScanPlant` scenario, MyHOME_Suite follows discovery with repeated addressed interviews, detailed configuration reads, and close operations.

### Interpreting `WHERE`

Section ID: `ownkb:section:d000010:s000003`

Diagnostic `WHERE` follows the address rules of the selected diagnostic family. It is not one universal integer format and it is not necessarily the only address exposed by the Device.

For Lighting and Automation, a Device can contain multiple Modules with different functional `A`/`PL` addresses. `DIMENSION 32` reports those per-`slot` addresses. The address used to find or interview the Physical Device must therefore be kept distinct from the Module addresses learned during the interview.

Observed `WHO 1001` captures suggest that the diagnostic `WHERE` commonly corresponds to the configured address of `slot` `1`. The observation is useful for implementation testing but is not sufficient to define a universal rule for every Object layout, Device, or diagnostic family.

### Scan procedure

Section ID: `ownkb:section:d000010:s000004`

Cautions: `do not`

1. Choose the diagnostic `WHO` from an established system mapping.
2. Generate only `WHERE` values valid for that familyâ€™s address rule.
3. Send `*#[WHO]*[WHERE]*1##` for each candidate.
4. Collect the `DIMENSION 1` response, if any.
5. Preserve the queried `WHERE`, returned identity fields, and raw frame together.
6. Use an ID-based interview when `DIMENSION 13` later supplies a stable Device identity.

Silence can mean no Device, an unsupported diagnostic operation, an invalid address for the selected family, transport loss, or a Device that is temporarily unavailable. Do not collapse these cases into a positive â€œaddress unusedâ€ result without retry and timeout policy.

### Address rules in `OPEN.db`

Section ID: `ownkb:section:d000010:s000005`

The diagnostic family selects the system; the system and, in several cases, the Device/Object family select the address rule.

| Diagnostic family | Target class | Virtual form | Advanced form |
| --- | --- | --- | --- |
| `1001` | Lighting/Automation general | `[A][PL]` | `[A][PL]+` |
| `1001` | F422 logic/physical extension | `[I3][I4]` | `[I3][I4]+` |
| `1004` | Thermoregulation general | `[ZA][ZB]` | `[ZAZB]` |
| `1004` | four-zone control unit | `#0#[ZA][ZB]` | `#0#[ZAZB]` |
| `1004` | actuator | `[ZA][ZB]#[N]` | `[ZAZB]#[N]` |
| `1004` | slave probe | `[SLA][ZA][ZB]` | `[SLA][ZAZB]` |
| `1004` | external probe | `[PL_N]00` | `[PL_N]00` |
| `1008` | public-riser interface | `1[I1][I2][I3][I4]` | `1[I1I2I3I4]` |
| `1013` | burglar-alarm interface | `[I4]` | `[I4]` |
| `1013` | galvanic/new physical separation | `[I4]` | `[I4]` |
| `1018` | control unit/measurement target | `5[A1][A2][A3]` | `5[A123]` |
| `1018` | actuator | `7[P1][P2]#0` | `7[P]#[PHASE]` |
| `1023` | command or virgin Device | `20` | `20` |
| `1023` | indicator | `7[R1][R2]` | `7[R1R2]` |

The table reproduces MyHOME_Suiteâ€™s address-rule vocabulary. It does not claim that every rule is valid for every Object in the family. `object_device_family`, validity conditions, and offsets further qualify several entries.

`OPEN.db` provides no system address rule for every diagnostic family named in `EN_SYSTEM`; absence of a rule is not permission to reuse `A`/`PL`.

### Range and safety

Section ID: `ownkb:section:d000010:s000006`

Cautions: `avoid`
Provenance cues: `database`

Address ranges belong to the selected system. The numeric capacity of a database parameter is not itself permission to probe every value, and the visible string grammar can include fixed prefixes, family selectors, or `#` components.

Avoid broad address sweeps on live installations unless the transport and Device behavior are understood. Prefer ID enumeration when the diagnostic family supports it, because enumeration does not require inventing candidate functional addresses.

### Identity resolution

Section ID: `ownkb:section:d000010:s000007`

Cautions: `must not`
Provenance cues: `catalogue`, `evidence`

The returned `OBJECT_MODEL`, `BRAND`, and `LINE` can be correlated with catalogue fields as documented in [`DIMENSION 1`: Device Identity](dim1-device-identity.md). `N_CONF` represents the number of physical configurator positions provided by the Device. It is a hardware-interface characteristic and must not be confused with Module count, Object identity, logical configuration parameters, or product form factor. See [`DIMENSION 1`: Device Identity](dim1-device-identity.md) for the evidence and interpretation.

Address rules come from `OPEN.db`; product identity comes from `MHCatalogue.db`. Equal internal system IDs across those databases must not be joined. See [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md).

# Document: ownkb:document:d000011

Source path: `diagnostics/architecture.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## Diagnostic Architecture

Section ID: `ownkb:section:d000011:s000001`

The diagnostic protocol is a management layer carried in OpenWebNet frames. It discovers Physical Device instances and projects selected parts of their runtime state without replacing the functional protocol used to operate them.

### Managed systems

Section ID: `ownkb:section:d000011:s000002`

Applicability cues: `firmware`
Cautions: `must not`
Provenance cues: `database`, `evidence`

A diagnostic `WHO` identifies a management family, not necessarily the diagnostic counterpart of exactly one functional `WHO`. The `EN_SYSTEM.who` field nevertheless stores only one functional `WHO` on each `OPEN.db` system record and must be reported literally before broader domain coverage is inferred.

The complete set of non-empty diagnostic mappings in `OPEN.db` is:

| Diagnostic `WHO` | Explicit `EN_SYSTEM.who` | `OPEN.db` system records | `managed` | Direct `EN_OPEN` associations |
| --- | --- | --- | --- | --- |
| `1001` | `1` | Light and Automation system; Interface AUTOM L3; Interface AUTOM L4 | `1` | `65` on the combined system |
| `1004` | `4` | Thermoregulation | `1` | `46` |
| `1008` | `8` | Video Door entry system and telephony | `1` | `1` |
| `1013` | `13` | Integration Functions | `1` | `0` |
| `1018` | `18` | Energy Management system | `1` | `65` |
| `1022` | `22` | Multimedia System | `0` | `0` |
| `1023` | `23` | Access Control | `1` | `65` |
| `1027` | `27` | Nurse Call basic level system | `0` | `9` |

For diagnostic `WHO 1001`, these are the only explicit associations in `OPEN.db`: all three rows contain `EN_SYSTEM.who = 1`. The database contains no `EN_SYSTEM` row with `who = 2`, and no other table contains a literal `1001` mapping.

The description â€œLight and Automation systemâ€ and observed protocol behavior establish that the management family extends across Lighting and Automation, whose functional protocols use `WHO 1` and `WHO 2` respectively. That broader coverage is not encoded as a second `EN_SYSTEM` mapping and must not be presented as though `OPEN.db` directly pairs `WHO 2` with `WHO 1001`.

The `managed` flag and direct frame associations are separate evidence. `WHO 1027`, for example, is marked unmanaged but has nine service/diagnostic operations; `WHO 1008` is managed but has only one directly associated service-identification template. A diagnostic-family value alone does not establish support for the common Device interview.

The 65-operation set associated with the combined Lighting/Automation system is also associated with Energy Management and Access Control. Thermoregulation shares 46 of those operations and adds a dedicated scan form. This is direct implementation evidence for a common management model across those families. It remains Device- and firmware-dependent at runtime.

The full functional namespace and association matrix is maintained in [MyHOME_Suite `OPEN.db` Coverage](../functional/open-db-coverage.md).

### Evidence layers

Section ID: `ownkb:section:d000011:s000003`

Applicability cues: `firmware`
Provenance cues: `catalogue`

| Layer | Establishes | Does not independently establish |
| --- | --- | --- |
| Public protocol | frame language, functional behavior, and explicitly published family-specific fault diagnostics | the MyHOME Suite Device-interview state machines |
| `OPEN.db` | management templates, parameters, sequences, address rules, and timeouts | installed Device values or complete catalogue semantics |
| `OpenQuery.txt` | how MyHOME_Suite reads and orders `OPEN.db` structures | semantics absent from those tables |
| `MHCatalogue.db` | supported Device/firmware/Module/Object/configuration capability | current installed state |
| Captures | actual Device responses and workflow behavior | universal support outside observed products and versions |
| UI | presentation, Module visibility, labels, and editability | wire encoding without correlation |

### Session roles

Section ID: `ownkb:section:d000011:s000004`

Applicability cues: `gateway`
Provenance cues: `catalogue`

| Role | Responsibility |
| --- | --- |
| Programmer | Starts discovery or interview, selects a Device or Module, collects responses, and closes the operation |
| Device | Responds with identity and runtime state using the selected diagnostic `WHO` |
| Gateway/transport | Carries OpenWebNet frames; it does not assign catalogue meaning to diagnostic values |

The wire protocol does not add a transaction identifier. An implementation should therefore serialize ambiguous diagnostic workflows on one connection, associate responses with the active operation, and apply the sequence timeouts defined by the implementation data.

### Session lifecycle

Section ID: `ownkb:section:d000011:s000005`

A typical workflow has four phases:

1. release prior scan state with `WHAT 12` where enumeration is used;
2. start discovery or interview;
3. collect zero or more responses, including repeated `DIMENSION` frames;
4. observe `WHAT 4` as the Device end marker or terminate with `WHAT 6` when aborting.

Enumeration by ID adds a per-Device `WHAT 11` frame so an already reported Device does not respond again during the current pass. See [Device Discovery](device-discovery.md).

### Canonical diagnostic scenarios

Section ID: `ownkb:section:d000011:s000006`

| MyHOME_Suite scenario | Ordered sequences |
| --- | --- |
| `DiagPoint2PointByAddress` | `DiagAddressed` â†’ `DiagKO` â†’ `CloseScan` |
| `DiagPoint2PointWithID` | `DiagAdvanced` â†’ `DiagKO` â†’ `CloseScan` |
| `DiagLocalButton` | `DiagLocalButton` â†’ `DiagKO` â†’ `CloseScan` |
| `ScanPlant` | `ScanAddressed` â†’ repeated `DiagAddressed` â†’ repeated `DiagKO` â†’ repeated `CloseScan` |
| `ScanByAID` | `ScanAID` â†’ repeated `DiagAID` â†’ repeated `DiagKO` â†’ repeated `CloseScan` |

`DiagAdvanced` and `DiagAID` use the same ID-start frame and response ordering. Their sequence metadata differs because `DiagAID` is the repeated interview step inside a plant scan.

### Runtime model projection

Section ID: `ownkb:section:d000011:s000007`

Applicability cues: `firmware`, `gateway`, `version`

| Diagnostic data | Device-model interpretation |
| --- | --- |
| `DIMENSION 1` | item/model identity, addressed-form physical configurator-position count (`N_CONF`), brand, and line; the empty-`WHERE` gateway form is a distinct variant |
| `DIMENSION 2` | firmware version |
| `DIMENSION 3` | hardware version |
| `DIMENSION 4`, `5` | twelve configurator values |
| `DIMENSION 6` | microcontroller version |
| `DIMENSION 7`, `8` | diagnostic bitmasks |
| `DIMENSION 13` | installed Device ID |
| `DIMENSION 30` | `slot`, enabled regular Object or disabled Virgin Object, and Module enabled/disabled state |
| `DIMENSION 32` | `slot`, system selector, encoded address |
| `DIMENSION 35` | configuration index, `slot`, value |
| `DIMENSION 310` | Object-specific parameter without a generic index |

The projection is intentionally partial. A Physical Device can expose several Modules and functional addresses, while discovery and interview operate on one Device-level identity or address selection.

### Address roles

Section ID: `ownkb:section:d000011:s000008`

Uncertainty: `hypothesis`
Provenance cues: `capture`

`WHERE` has several roles in the diagnostic protocol:

- it selects a Device for an addressed interview;
- it identifies the responding Device in many response frames;
- it can be a placeholder in an end marker;
- it does not replace the per-Module address reported by `DIMENSION 32`.

Observed `WHO 1001` traffic often correlates the ordinary diagnostic `WHERE` with the configured address of `slot` `1`. This is a capture-derived hypothesis, not a universal addressing rule.

System-specific address grammars are documented in [Address Discovery](address-discovery.md). `OPEN.db` defines distinct forms for Lighting/Automation, Thermoregulation, Video Door Entry interfaces, Integration interfaces, Energy Management, and Access Control; it defines no system address rule for every named diagnostic family.

### Timeout model

Section ID: `ownkb:section:d000011:s000009`

The canonical implementation defines these diagnostic timing values:

| Timeout | Default | Use |
| --- | --- | --- |
| `DeviceAnswerTimeOut` | `15` s | first response after addressed or ID start |
| `DeviceMoreAnswerTimeOut` | `20` s | further Device information until end marker |
| `DeviceAnswerTimeOutByButton` | `300` s | first response in local-button mode |
| `DiagTimeOut` | `600` s | maximum diagnosis duration |
| `ScanKOTimeWait` | `8` s | detailed Object/configuration response window |
| `ScanAreaTimeWait` | `8` s | delay/window before the next address/zone |
| `ScanIDWindowDiscoveryTimeWait` | `4` s | response window during massive ID discovery |
| `CloseScenarioTimeWait` | `1` s | close-sequence wait |

These are MyHOME_Suite 3.5.38 defaults, not protocol constants. `OpenQuery.txt` loads timeout actions and status transitions from `AS_TIMEOUT_OPEN_SEQUENCE` rather than hard-coding one global timer.

### Acknowledgements and errors

Section ID: `ownkb:section:d000011:s000010`

Applicability cues: `firmware`
Cautions: `must not`

The `EN_OPEN` registry contains ordinary `ACK` (`*#*1##`) and `NACK` (`*#*0##`) templates, but those rows are not direct members of the canonical diagnostic sequences. Sequence metadata separately defines `status4nack`, error, and timeout transitions. `OPEN.db` also defines structured Object and configuration errors in `DIMENSION 31`, `34`, and `39`.

An implementation must not treat every missing optional response as an error. Support varies by Device, firmware, selected Object, and diagnostic family. A positive end marker can validly follow a response set that omits unsupported optional data.

# Document: ownkb:document:d000012

Source path: `diagnostics/device-discovery.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## Device Discovery

Section ID: `ownkb:section:d000012:s000001`

Provenance cues: `documentation`

Device discovery by ID enumerates installed Device instances within one diagnostic `WHO`. The Device ID is a 32-bit transport value. This documentation displays it as exactly eight hexadecimal characters, preserving leading zeroes.

### Frames

Section ID: `ownkb:section:d000012:s000002`

| Purpose | Frame |
| --- | --- |
| Release/reset enumeration state | `*[WHO]*12*0##` |
| Request all Device IDs | `*#[WHO]*0*13##` |
| Request configured Device IDs only | `*#[WHO]*0*13#1##` |
| Request unconfigured Device IDs only | `*#[WHO]*0*13#0##` |
| Device ID response | `*#[WHO]*[WHERE]*13*[ID]##` |
| Suppress an already found Device | `*[WHO]*11#[ID]*0##` |
| Abort/close diagnosis | `*[WHO]*6*0##` |

`ID` ranges over `0..4294967295` in `OPEN.db`. The hexadecimal display form is a presentation convention; the frame field itself is the numeric transport representation used by the participating implementation.

### Enumeration algorithm

Section ID: `ownkb:section:d000012:s000003`

Provenance cues: `capture`, `database`

1. Send `*[WHO]*12*0##` to release any prior enumeration state.
2. Send the chosen `DIMENSION 13` request.
3. Collect every `DIMENSION 13` response during the response window.
4. For each newly discovered ID, send `*[WHO]*11#[ID]*0##`.
5. Repeat the same request.
6. Stop when a complete response window yields no ID response. A pass containing only previously seen IDs indicates ineffective suppression, not successful completion; bound retries and report the incomplete scan.
7. Send `*[WHO]*12*0##` to release the enumeration state.

The request-repeat-suppress behavior is present in the `OPEN.db` `ScanAID` sequence and corroborated by observed traffic. In the sequence metadata, both the ID request and the ID response/flag steps are repeatable. `ScanIDWindowDiscoveryTimeWait` assigns a default four-second discovery window to the request.

The no-response termination rule is capture-derived behavior: the canonical frame database describes repetition and its response window but does not encode a declarative â€œempty passâ€ condition.

### Example with diagnostic `WHO 1001`

Section ID: `ownkb:section:d000012:s000004`

Provenance cues: `documentation`

| Step | Example frame |
| --- | --- |
| Release prior state | `*1001*12*0##` |
| Request IDs | `*#1001*0*13##` |
| Receive one ID | `*#1001*10*13*5234376##` |
| Flag that ID | `*1001*11#5234376*0##` |
| Repeat request | `*#1001*0*13##` |
| Release after an empty pass | `*1001*12*0##` |

If the returned decimal ID is `5234376`, its documentation display is `004FDEC8`. The example illustrates conversion only; it does not identify a particular product.

### Collection rules

Section ID: `ownkb:section:d000012:s000005`

Applicability cues: `gateway`
Cautions: `do not`, `must not`
Uncertainty: `may`
Provenance cues: `catalogue`

- Deduplicate by the full 32-bit ID, not by `WHERE`.
- Preserve the raw decimal field and the normalized eight-character hexadecimal display.
- Treat `WHERE` as response context, not as the Device identity.
- Apply the configured response timeout to each pass.
- Do not assume response order is stable.
- Do not assume one Device exists at only one functional address.

If several Devices respond simultaneously, a gateway may deliver their frames in an order unrelated to catalogue order, physical topology, or Device ID.

The `WHERE` inside a `DIMENSION 13` response is governed by the diagnostic familyâ€™s address grammar. It can assist later addressed operations, but it must not replace the 32-bit Device ID as the inventory key.

### Filters

Section ID: `ownkb:section:d000012:s000006`

Cautions: `must not`
Provenance cues: `source`

The final `#1` and `#0` forms select configured and unconfigured Devices respectively according to the implementation labels in `OPEN.db`. They are concrete frame templates but are not members of the canonical `ScanAID` sequence, which uses the all-Device form.

The precise Device-side definition of â€œconfiguredâ€ is not expanded by the source. It must not be assumed to mean that every Module is configured, that every address is valid, or that no disabled Module remains.

### Scan-state operations

Section ID: `ownkb:section:d000012:s000007`

Cautions: `must not`
Provenance cues: `database`

`OPEN.db` describes `WHAT 11` as sending a flag to every Device found and `WHAT 12` as deleting previous scans from memory. Observed enumeration behavior supports the narrower operational interpretation used here:

- `WHAT 11` suppresses or marks one already reported Device during the active scan;
- `WHAT 12` releases/resets the scan state before and after enumeration.

The database does not establish persistence beyond the scan workflow. These frames must not be described as permanent configuration writes.

### Sequence and scenario boundaries

Section ID: `ownkb:section:d000012:s000008`

`ScanAID` performs enumeration only. The higher-level `ScanByAID` scenario then repeats:

1. `DiagAID` for each discovered Device;
2. `DiagKO` for detailed configuration;
3. `CloseScan` to terminate that Deviceâ€™s diagnostic session.

This separation is why receiving a `DIMENSION 13` response does not itself provide the Module list or configuration values.

### After discovery

Section ID: `ownkb:section:d000012:s000009`

Provenance cues: `catalogue`

Start a full interview with `*[WHO]*10#[ID]*0##`. This selects the installed Device instance directly and avoids relying on a potentially ambiguous functional address. See [Device Interview](device-interview.md).

Catalogue product identity is resolved later from `DIMENSION 1`; the Device ID is not a catalogue primary key, SKU, item model, Object number, or address. See [Physical Devices](../device-model/physical-devices.md).

# Document: ownkb:document:d000013

Source path: `diagnostics/device-interview.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## Device Interview

Section ID: `ownkb:section:d000013:s000001`

A Device interview reads the runtime diagnostic projection of one Physical Device. It can be started by Device ID, diagnostic address, or local interaction.

### Start and termination frames

Section ID: `ownkb:section:d000013:s000002`

| Operation | Frame |
| --- | --- |
| Start by Device ID | `*[WHO]*10#[ID]*0##` |
| Start by address | `*#[WHO]*[WHERE]*0##` |
| Start by local/general interaction | `*[WHO]*5*0##` |
| Device end marker | `*[WHO]*4*[WHERE_FAKE]##` |
| General end marker variant | `*[WHO]*4*0##` |
| Abort/close diagnosis | `*[WHO]*6*0##` |

`OPEN.db` uses `DiagAdvanced`/`DiagAID`, `DiagAddressed`, and `DiagLocalButton` for the three start modes. The Device ID form is preferred when discovery has already established the 32-bit instance identity.

`DiagAdvanced` is the point-to-point ID sequence. `DiagAID` uses the same start frame and response order as the repeated per-Device step in the `ScanByAID` scenario.

### Expected response groups

Section ID: `ownkb:section:d000013:s000003`

Applicability cues: `firmware`, `gateway`, `version`
Uncertainty: `unknown`
Provenance cues: `database`

The canonical sequences order the following response families. This page describes the ordinary per-Device interview surface; the empty-`WHERE` gateway `DIMENSION 1` identity form is a distinct service variant documented in [`DIMENSION 1`: Device Identity](dim1-device-identity.md#gateway-variant).

| Order | `DIMENSION` | Data |
| --- | --- | --- |
| 1 | `1` | item/model identity, ordinary per-Device physical configurator-position count (`N_CONF`), brand, line |
| 2 | `2` | firmware version |
| 3 | `3` | hardware version |
| 4 | `4` | configurators `1..6` |
| 5 | `5` | configurators `7..12` |
| 6 | `6` | microcontroller version |
| 7 | `7` | diagnostic bitmask A |
| 8 | `8` | diagnostic bitmask B |
| 9 | `13` | Device ID |
| 10 | `30` | repeated Module/Object records |
| 11 | `32` | repeated Module-address records |
| 12 | `31` | Object-state errors when applicable |
| 13 | - | `WHAT 4` end marker |

This is the canonical implementation order, not a guarantee that every Device returns every optional frame. In `AS_OPEN_SEQUENCE`, the start frame is mandatory; the listed Device responses are optional, and `DIMENSION 30`, `32`, and the busy `DIMENSION 31` form are repeatable. The end marker is present at the final sequence position but is not marked mandatory by the database.

Collectors should therefore accept repeated records, retain unknown additions, and prefer the explicit end marker over an assumed record count while still handling timeout and abort paths.

### Timing and completion

Section ID: `ownkb:section:d000013:s000004`

| Phase | Default in `OPEN.db` |
| --- | --- |
| Wait for the first response after address or ID start | `15` s |
| Wait for further Device information | `20` s |
| Wait for first response in local-button mode | `300` s |
| Maximum diagnostic session | `600` s |

The `20`-second further-information timer begins with `DIMENSION 1` and stops on the `WHAT 4` end marker in the canonical addressed and ID sequences. These are MyHOME_Suite defaults loaded through `OpenQuery.txt`, not wire-level constants.

### Collection state

Section ID: `ownkb:section:d000013:s000005`

Cautions: `do not`
Uncertainty: `may`

For each active interview, retain:

- diagnostic `WHO` and start mode;
- selected Device ID or `WHERE`;
- raw frames in arrival order;
- one or more values for each `DIMENSION`;
- `DIMENSION 30` and `32` grouped by `slot`;
- structured errors;
- whether `WHAT 4`, `WHAT 6`, timeout, or transport closure ended the operation.

Do not overwrite repeated frames merely because their `DIMENSION` matches. `DIMENSION 30` and `32` are naturally multi-row data, and other dimensions may repeat during retries.

### Reconstructing the Device

Section ID: `ownkb:section:d000013:s000006`

Applicability cues: `firmware`, `version`
Provenance cues: `catalogue`, `evidence`

1. Resolve `DIMENSION 1` against catalogue item, brand, and line metadata and, for this ordinary per-Device form, retain `N_CONF` as the Device's physical configurator-position count.
2. Record the reported firmware, hardware, and microcontroller versions without assuming that a version number is a catalogue primary key.
3. Build one Module record per `slot` from `DIMENSION 30`.
4. Attach `DIMENSION 32` system/address data to the matching `slot`.
5. Preserve enabled and disabled Module states from `DIMENSION 30`, resolving enabled Modules through the regular Object namespace and disabled Modules through the Virgin Object namespace.
6. Request detailed parameters only after the Module/Object layout is known.

The result is an installed-state view. Catalogue data supplies permitted capabilities; the interview supplies the choices and values currently reported by the Device.

The catalogue and runtime projections must remain distinct:

| Question | Strongest evidence |
| --- | --- |
| Which product capability is possible? | `MHCatalogue.db` item, firmware, slots, Objects, and constraints |
| Which installed Device responded? | `DIMENSION 13` plus diagnostic context |
| Which product description should be shown? | `EN_DEVICE.name` after `DIMENSION 1` resolution |
| Is a Module enabled with a regular Object or disabled with a Virgin Object? | `DIMENSION 30` |
| Which functional address is reported for that Module? | `DIMENSION 32` |
| Which indexed value is reported? | `DIMENSION 35` interpreted through the resolved Object/firmware configuration |

### Detailed configuration phase

Section ID: `ownkb:section:d000013:s000007`

Uncertainty: `unresolved`

After the initial interview, `DiagKO` is a separate detailed configuration-reading sequence. Its request, repeated `DIMENSION 35` responses, possible `DIMENSION 310` response, timeout, and unresolved `DIMENSION 38` reset/select effect are defined canonically in [`DIMENSION 35`: Configuration Parameters](dim35-configuration.md#reading-detailed-parameters). The interview does not imply that this later operation is supported or non-destructive for every target.

### Errors and abnormal termination

Section ID: `ownkb:section:d000013:s000008`

Uncertainty: `may`

`DIMENSION 31` reports Object state conditions, `DIMENSION 34` reports an address error, and `DIMENSION 39` reports a configuration-parameter error. `ACK` and `NACK` can also occur in the implementation sequences.

A timeout is not equivalent to `WHAT 4`: it leaves completion uncertain. Send `WHAT 6` when explicitly abandoning an active diagnostic operation if the transport and target support the close operation.

`CloseScan` consists of the programmer `WHAT 6` frame. The canonical implementation assigns a 600-second diagnosis timeout and a one-second close wait around this lifecycle; applications may choose different policy but should record whether completion came from `WHAT 4`, `WHAT 6`, timeout, or transport loss.

### Observed-runtime limits

Section ID: `ownkb:section:d000013:s000009`

Cautions: `do not`
Provenance cues: `database`

Observed `WHO 1001` traffic corroborates ID-based interview, repeated Module records, detailed configuration responses, and `WHAT 4` termination. It also shows product-specific response surfaces: a command-only Device can omit an observed `DIMENSION 32`, while a multi-Module sensor can expose many `slot` positions. These observations refine optionality but do not redefine the database sequence for all diagnostic families.

# Document: ownkb:document:d000014

Source path: `diagnostics/dim1-device-identity.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## `DIMENSION 1`: Device Identity

Section ID: `ownkb:section:d000014:s000001`

Provenance cues: `catalogue`

`DIMENSION 1` reports the catalogue-facing identity of a Physical Device.

### Frame

Section ID: `ownkb:section:d000014:s000002`

`*#[WHO]*[WHERE]*1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##`

| Field | Range in the addressed `OPEN.db` form | Interpretation |
| --- | --- | --- |
| `OBJECT_MODEL` | `1..65535` | item/model value |
| `N_CONF` | `0..12` | number of physical configurator positions in the ordinary addressed Device form |
| `BRAND` | `0..4` | brand code |
| `LINE` | `0..8` | product-line code |

### Catalogue correlations

Section ID: `ownkb:section:d000014:s000003`

Applicability cues: `gateway`
Cautions: `must not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `documentation`

| Diagnostic field | `MHCatalogue.db` field | Status |
| --- | --- | --- |
| `OBJECT_MODEL` | `AS_ITEM_SYSTEM.modobj` | corroborated |
| `BRAND` | `EN_BRAND.brand_modobj` | corroborated |
| `LINE` | `EN_LINE.line_modobj` | corroborated |
| `N_CONF` | no direct catalogue field identified | ordinary addressed form interpreted from `OPEN.db` wording and product documentation; gateway semantics unresolved |

The established path uses `OBJECT_MODEL` within the relevant catalogue system, then applies brand and line metadata to narrow or present the matching product identity. It must not be replaced by a numeric join to `EN_DEVICE.id_device` or `EN_ITEM.id_item`; those are independent internal identifiers.

### Resolution procedure

Section ID: `ownkb:section:d000014:s000004`

Applicability cues: `firmware`, `revision`, `version`
Cautions: `must not`
Provenance cues: `catalogue`, `evidence`, `source`

1. Select the catalogue system corresponding to the diagnostic family using established system semantics, not equal internal `id_system` values across databases.
2. Find `AS_ITEM_SYSTEM` records whose `modobj` equals `OBJECT_MODEL`.
3. Resolve the associated `EN_ITEM` capability definition.
4. Use `BRAND` and `LINE` through `EN_BRAND.brand_modobj` and `EN_LINE.line_modobj` to identify compatible `EN_DEVICE` records.
5. Retain all candidates if the source revision does not distinguish them further.
6. Use firmware/version and observed Module layout as corroborating evidence, not as an invented primary-key join.

The result can be one shared item with several branded Device/SKU records. That is expected in the catalogue model.

Use `EN_DEVICE.name` as the standard MyHOME_Suite-facing description after resolution. `EN_ITEM.descr` names the shared capability item, while `EN_KEY_OBJECT.descr` names one logical function and must not replace the Physical Device description.

### Corroborated example

Section ID: `ownkb:section:d000014:s000005`

Applicability cues: `firmware`
Provenance cues: `catalogue`

The observed Device `00C58E91` (`12947089` decimal) reported model value `107`. In the canonical catalogue:

- `AS_ITEM_SYSTEM.modobj = 107` resolves to item `1184`;
- `EN_ITEM.descr` is â€œFlush mounted actuator and free controlâ€;
- firmware definition `157` declares four `slot` positions;
- several branded SKUs, including `64391`, `64191`, and `64192`, share that item.

The example corroborates the model-to-item path while also demonstrating why `OBJECT_MODEL` alone does not uniquely identify one SKU. Brand and line values, plus project/UI context where available, are required to narrow the Device record.

### `N_CONF` and physical configurators

Section ID: `ownkb:section:d000014:s000006`

Applicability cues: `firmware`

`OPEN.db` describes `N_CONF` as â€œConfigurator numberâ€ / â€œnumber of physical configuratorâ€ and constrains the ordinary addressed form to `0..12`. Product configuration diagrams provide an independent interpretation for that addressed Device form: the value corresponds to the number of physical configurator positions provided by the Device.

Documented examples include:

| Device | `N_CONF` | Physical configuration layout |
| --- | --- | --- |
| `F420` | `2` | 2 configurator positions |
| `F429` | `3` | 3 positions: `A`, `G`, `M` |
| `H4652/3` | `7` | 7 configurator positions |

For the corroborated ordinary addressed Device form, this field therefore describes the Device's physical configuration interface. It is not a Module count, Object identifier, Virgin Object, form factor, firmware class, or indication of the Object assigned to `slot` `1`.

MyHOME Devices can alternatively use advanced configuration, which can represent values outside the limits of the physical configurator interface. Within the corroborated ordinary addressed Device form, `N_CONF` remains a hardware characteristic: it does not describe the active configuration method or the number of logical configuration parameters.

Older Devices for which configuration diagrams have not yet been located remain useful targets for further cross-checking, but the available examples support the physical-position interpretation across multiple distinct `N_CONF` values.

### Address context

Section ID: `ownkb:section:d000014:s000007`

Provenance cues: `catalogue`

`WHERE` identifies the diagnostic response context. It is not part of the catalogue identity tuple and can differ from functional addresses reported later for individual Modules.

### Gateway variant

Section ID: `ownkb:section:d000014:s000008`

Applicability cues: `gateway`, `not applicable`
Cautions: `do not`, `must not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `evidence`, `source`

`OPEN.db` also contains a gateway identity response without an ordinary `WHERE`:

`*#[WHO]**1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##`

Treat this as a distinct frame variant. Do not repair the empty field or silently convert it to the addressed form.

The addressed-form ranges and the physical-configurator interpretation of `N_CONF` above must not be imposed automatically on this gateway variant. First-hand MH202 and F454 gateway identity captures return payloads `[NETWORK_ADDRESS]` and `[NETWORK_ADDRESS]` respectively: the observed second-field value `15` and `BRAND = 5` are outside the ordinary addressed-form ranges. These observations establish that those ranges are not valid constraints for the gateway form. They do not, by themselves, establish that gateway-variant `N_CONF` has the ordinary addressed Device field's physical-configurator semantics.

Numerically, `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern. Its repeated use in both observed gateway tuples is therefore consistent with a reserved or sentinel value, but no canonical source currently establishes that interpretation or the sentinel's meaning. The evidence does not justify presenting gateway `N_CONF = 15` as a literal count of fifteen physical configurator positions, nor as a proven encoding of â€œzero configuratorsâ€ or â€œnot applicableâ€. Preserve the raw value and its unresolved semantics.

For gateway catalogue identification, preserve the returned `N_CONF` value but resolve `OBJECT_MODEL`, `BRAND`, and `LINE` through their established catalogue correlations in the applicable system context.

`OpenQuery.txt` includes this gateway variant in its gateway-connection query together with address scan and general diagnostic frames. That implementation use does not alter the identity-field mappings above.

For the complete Integration Functions gateway workflow and the MH202/F454 cases, see [Identify an OpenWebNet Gateway](../guides/identify-openwebnet-gateway.md).

# Document: ownkb:document:d000015

Source path: `diagnostics/dim30-modules.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## `DIMENSION 30`: Modules and Objects

Section ID: `ownkb:section:d000015:s000001`

Applicability cues: `firmware`

`DIMENSION 30` reports whether a firmware-exposed Module is enabled or disabled and, accordingly, the regular configured Object or Virgin Object that identifies it.

### Frame

Section ID: `ownkb:section:d000015:s000002`

Provenance cues: `documentation`, `source`

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | --- | --- |
| `SLOT` | `1..255` | numeric `slot` |
| `KEYO` | `1..65535` | Object or Virgin Object number, selected by `STATE` |
| `STATE` | `0..1` | Module enabled/disabled state |

Use **Module** for the logical container and **`slot`** for `SLOT`. `OPEN.db` uses the legacy label â€œko slotâ€; this documentation retains that wording only when quoting or naming source fields.

### Catalogue interpretation

Section ID: `ownkb:section:d000015:s000003`

Applicability cues: `revision`
Provenance cues: `catalogue`, `database`, `evidence`

| Diagnostic field | Catalogue concept | Status |
| --- | --- | --- |
| `SLOT` | `EN_SLOTS.first_slot` placement | structurally corroborated |
| `KEYO`, when `STATE = 0` | `EN_KEY_OBJECT.key_object` | regular configured Object; experimentally and behaviorally corroborated |
| `KEYO`, when `STATE = 1` | `EN_VIRGIN_OBJECT.virgin_key_object` | Virgin Object for a disabled Module; experimentally and behaviorally corroborated |
| `STATE` | installed Module enabled/disabled state | `OPEN.db` supplies the binary field and generic label; polarity is established by controlled diagnostic/programming evidence correlated with MyHOME_Suite UI behavior |

`KEYO` selects one of two external number spaces according to `STATE`. It is not the internal catalogue key `EN_KEY_OBJECT.id_key_object` or `EN_VIRGIN_OBJECT.id_virgin_key_object`, even where a particular database revision happens to assign equal numeric values.

Likewise, `SLOT` is not `EN_SLOTS.id_slot`. Diagnostic `SLOT` is a Device-local position correlated with catalogue placement such as `EN_SLOTS.first_slot`; `id_slot` identifies a database association row.

### Building the Module list

Section ID: `ownkb:section:d000015:s000004`

Cautions: `do not`
Provenance cues: `catalogue`

1. Group records by Physical Device interview.
2. Use `SLOT` as the Device-local `slot` key.
3. When `STATE = 0`, resolve `KEYO` against `EN_KEY_OBJECT.key_object`; the Module is enabled.
4. When `STATE = 1`, resolve `KEYO` against `EN_VIRGIN_OBJECT.virgin_key_object`; the Module is disabled.
5. Use the resolved Virgin Object and its catalogue associations to derive the disabled Module's functional role and permitted Object set.
6. Retain `STATE` alongside the resolved record so an Object and Virgin Object are never conflated.
7. Attach `DIMENSION 32` address data using the same `slot`.
8. Attach `DIMENSION 35` configuration values only when both Device and `slot` match.

Do not renumber `slot` positions to match a UIâ€™s visible Module numbering. MyHOME_Suite can hide or relabel slots, and observed scenario Devices show UI numbering that differs from the numeric diagnostic position.

### Enabled and disabled Modules

Section ID: `ownkb:section:d000015:s000005`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`, `evidence`

Controlled diagnostic/programming experiments correlated with direct MyHOME_Suite UI observations establish the `DIMENSION 30` polarity. `OPEN.db` describes `STATE` generically as â€œconfigured or not configuredâ€, but that label does not establish the numeric polarity by itself:

| `STATE` | Module state | `KEYO` namespace | Interpretation |
| --- | --- | --- | --- |
| `0` | enabled | `EN_KEY_OBJECT.key_object` | regular configured Object currently applying to the Module |
| `1` | disabled | `EN_VIRGIN_OBJECT.virgin_key_object` | Virgin Object representing the disabled Module's configurable role |

A disabled Module is therefore not unidentified or semantically empty. Its Virgin Object describes the configurable role retained while the regular Object is not active. `AS_OBJECT_VIRGIN_OBJECT` relates that Virgin Object to permitted regular Objects; firmware and `slot` associations further constrain availability on the resolved Physical Device.

This polarity is specific to the `STATE` field of diagnostic/programming `DIMENSION 30`. Do not transfer it to `DIMENSION 31` or to unrelated fields named `STATE` without independent evidence.

Catalogue capability and runtime state answer different questions:

| Evidence | Meaning |
| --- | --- |
| `EN_FIRMWARE.slots` | number of `slot` positions declared by a firmware definition |
| `EN_SLOTS` and `AS_OBJECT_FIRMWARE` | Objects permitted or designated at a `slot` |
| Virgin-Object associations | configurable template and allowed Object set |
| `DIMENSION 30` | enabled regular Object or disabled Virgin Object currently reported by the installed Device |
| MyHOME_Suite UI | visible numbering, enabled state, and editability in that application context |

### Evidence and interpretation

Section ID: `ownkb:section:d000015:s000006`

Provenance cues: `catalogue`, `documentation`, `evidence`

The corrected polarity comes from controlled changes of Module enablement during diagnostic/programming work, with the resulting `DIMENSION 30.STATE` and `KEYO` values correlated directly with MyHOME_Suite's enabled/disabled presentation. Catalogue lookups then corroborate which external namespace the reported `KEYO` belongs to. The catalogue alone does not define the numeric polarity.

Earlier documentation used a Device-specific example to argue the opposite mapping from a catalogue lookup. That conclusion was circular: it selected the namespace using the assumed polarity and then treated the lookup as confirmation. The corrected interpretation therefore keeps catalogue capability evidence separate from the experimentally established `STATE` polarity.

### Observed Module-shape differences

Section ID: `ownkb:section:d000015:s000007`

Applicability cues: `revision`
Cautions: `do not`, `must not`
Provenance cues: `catalogue`

- Device `007B269D` demonstrated that `slot` numbering and UI-visible Module numbering can differ: `slot` `2` was absent from the UI while later slots were renumbered for display.
- Device `08CF44BF` demonstrated a large layout with `slot` positions through `17`, consistent with the maximum `EN_SLOTS.first_slot` observed in this catalogue revision.
- Light-control-only Device `00C44420` exposed command Modules as its actual hardware function; those Objects must not be interpreted as alternate actuator modes.

These observations constrain interpretation but do not prove that every Device returns `DIMENSION 30` or uses the same optional response set.

### Errors

Section ID: `ownkb:section:d000015:s000008`

Cautions: `do not`
Provenance cues: `catalogue`, `evidence`

`DIMENSION 31` reports Object-state results for a `slot`, including busy, already configured, insufficient capacity, and unsupported Object conditions. Preserve its accompanying `STATE` value as a distinct field and do not apply the `DIMENSION 30` polarity to it without independent evidence. Do not substitute an error record for the last valid `DIMENSION 30` assignment.

See [Modules](../device-model/modules.md), [Objects](../device-model/objects.md), and [Virgin Objects](../device-model/virgin-objects.md) for the catalogue structures behind this runtime projection.

# Document: ownkb:document:d000016

Source path: `diagnostics/dim32-addressing.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## `DIMENSION 32`: Module Addressing

Section ID: `ownkb:section:d000016:s000001`

`DIMENSION 32` reports the configured system and address associated with one `slot`.

### Frame

Section ID: `ownkb:section:d000016:s000002`

`*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | --- | --- |
| `SLOT` | `1..255` | Device-local `slot` |
| `SYS` | `1..255` | system selector |
| `ADDR` | `0..65535` | encoded address value |

`32#[SLOT]` is a parameterized `DIMENSION` selector: `#` attaches `SLOT` to `DIMENSION 32`. `SYS` and `ADDR` are the ordinary response values and are separated with `*`.

### Interpretation boundary

Section ID: `ownkb:section:d000016:s000003`

Cautions: `must not`
Provenance cues: `capture`, `catalogue`

`SYS` and `ADDR` are not a complete address description in isolation. Resolve them with:

- the diagnostic family;
- the Object reported for the same `slot` by `DIMENSION 30`;
- the functional systemâ€™s addressing rules;
- catalogue configuration metadata where corroborated.

The range `0..65535` is storage capacity, not a universal set of valid functional addresses.

`SYS` is described only as â€œKeyObject systemâ€ by `OPEN.db`. It must not be equated automatically with a functional `WHO`, a diagnostic `WHO`, `OPEN.db.EN_SYSTEM.id_system`, or `MHCatalogue.db.EN_SYSTEM.id_system`. A numeric mapping requires Object/system and capture corroboration.

### Device address versus Module address

Section ID: `ownkb:section:d000016:s000004`

Cautions: `must not`
Provenance cues: `capture`

The outer `WHERE` is the diagnostic response context. `ADDR` is the configured address of the Module identified by `SLOT`. They can coincide, but they are not defined as the same field.

In observed `WHO 1001` Device interviews, the ordinary diagnostic `WHERE` often matched the `A`/`PL` address of `slot` `1`. Other Modules on the same Physical Device reported different addresses. This correlation remains capture-derived and must not be used as a universal Device-address rule.

### Lighting and Automation

Section ID: `ownkb:section:d000016:s000005`

Applicability cues: `scs`
Cautions: `do not`
Uncertainty: `not established`, `unresolved`
Provenance cues: `documentation`

For Lighting/Automation Objects, an encoded value can be rendered as `A`/`PL` only after applying the relevant address rule. Documentation should record both the raw `ADDR` and the decoded components.

Prior research records the following interpretation of one observed Device layout. The original raw address fields and decoding derivation are not preserved here; the `PL=0` entries are unresolved, not established functional point addresses:

| `slot` | Object | Interpreted `A` | Interpreted `PL` | Prior rendering, not validated `WHERE` |
| --- | --- | --- | --- | --- |
| `1` | `6` | `1` | `0` | `10` |
| `2` | `6` | `1` | `6` | `16` |
| `3` | `400` | `1` | `0` | `10` |

The repeated `10` records an equal prior rendering, not proof that both Modules have the same usable functional address. The published SCS point grammar excludes `PL=0`; do not send `WHERE 10` from this interpretation. Recover the raw `(SYS, ADDR)` tuples and Device/Object context before deciding whether this is a sentinel, a distinct encoding, or a decoding error. No interpretation is selected here.

### Physical address counterparts

Section ID: `ownkb:section:d000016:s000006`

Applicability cues: `firmware`
Provenance cues: `evidence`

After applying the Object and system-specific address rule, decoded `ADDR` components can be compared with the firmware's physical configurator positions. For Lighting/Automation Devices, `A` and `PL` commonly appear both as physical positions in the firmware definition and as the effective address components reported through `DIMENSION 32`.

This establishes that the address property has a physical-configurator counterpart; it does not establish that physical configurators supplied the reported value. An `A` or `PL` value within the physical range can also have been assigned by advanced or virtual configuration. A value outside the established physical range can exclude physical configuration for that address component.

Other physical positions such as `M`, `TYPE`, `PRE`, or `G1` are not encoded as address components merely because they occur beside `A` and `PL` on the Device. Indexed counterparts belong to `DIMENSION 35` where the Object and firmware define them.

See [Physical configuration and configuration modes](../device-model/configuration.md#physical-configuration-and-configuration-modes) for the shared evidence rules.

Observed sensor Device `08CF44BF` used diagnostic `WHERE 0015`, interpreted as `A = 0`, `PL = 15`. Retaining the raw field is important because padding and family-specific formatting can be lost by integer-only storage.

### Other systems

Section ID: `ownkb:section:d000016:s000007`

Cautions: `must not`

Temperature Control zones, CEN/CEN+ identifiers, Energy Management targets, and Access Control addresses use different grammars. For example, CEN virtual identifiers occupy `0..2047`; that domain must not be decoded as `A`/`PL`.

Keep the raw tuple `(SYS, ADDR)` whenever the system-specific decoder is unavailable.

The address-rule inventory used by MyHOME_Suite is documented in [Address Discovery](address-discovery.md). It includes zone, actuator, interface, Energy Management, and Access Control forms that cannot be decoded as `A`/`PL`.

### Missing records

Section ID: `ownkb:section:d000016:s000008`

Applicability cues: `firmware`
Provenance cues: `capture`, `evidence`

Not every Module necessarily produces `DIMENSION 32`. A missing address can indicate a disabled Module, an Object without an address, unsupported reporting, or an incomplete interview. One observed light-control-only Device returned Module data without an observed `DIMENSION 32`; that single capture does not establish the reason.

The working capture model is therefore narrower than â€œall Modules have `DIMENSION 32`â€: addressed actuator/sensor Modules have produced it, while at least one command-only layout did not. Treat availability as Object- and firmware-dependent until broader evidence is available.

### Address errors

Section ID: `ownkb:section:d000016:s000009`

Provenance cues: `database`

`DIMENSION 34` reports an address error for one `slot`:

`*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##`

`ERROR` is boolean in `OPEN.db`. The database does not enumerate finer error causes, so retain the raw flag and surrounding Module/Object context.

# Document: ownkb:document:d000017

Source path: `diagnostics/dim35-configuration.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## `DIMENSION 35`: Configuration Parameters

Section ID: `ownkb:section:d000017:s000001`

`DIMENSION 35` reports one indexed configuration value for one `slot`.

### Frame

Section ID: `ownkb:section:d000017:s000002`

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | --- | --- |
| `INDEX` | `0..255` | parameter number, labelled â€œkconf indexâ€ |
| `SLOT` | `1..255` | Device-local `slot` |
| `VAL_PAR` | `0..65535` | parameter value |

Both `#` separators are significant parts of the canonical template.

### Catalogue correlation

Section ID: `ownkb:section:d000017:s000003`

Applicability cues: `firmware`
Cautions: `must not`
Provenance cues: `catalogue`

The shared â€œkconf indexâ€ terminology and observed behavior strongly support correlating `INDEX` with `MHCatalogue.db` `EN_CONF.idx`. The databases contain no cross-file foreign key, so resolution must retain the full context:

- Physical Device and firmware;
- `slot`;
- regular configured Object reported by `DIMENSION 30` for an enabled Module; a disabled Module's Virgin Object is a role constraint, not an Object-scoped configuration owner;
- applicable Object- or firmware-scoped `EN_CONF` definition;
- filters, conditions, and conversion rules;
- raw `VAL_PAR`.

`INDEX` is not globally unique. The same number can name different properties for different Objects or firmware definitions.

`EN_CONF` uses two mutually exclusive scopes in the canonical catalogue:

| Scope | Catalogue discriminator |
| --- | --- |
| Object-scoped | valid `id_key_object`; `id_firmware = 0` |
| Firmware-scoped | `id_key_object = 0`; valid `id_firmware` |

A decoder must consider both after resolving the installed Device. It must not require both columns to resolve on one row.

### Reading detailed parameters

Section ID: `ownkb:section:d000017:s000004`

Provenance cues: `source`

`OPEN.db` defines the all-Module operation:

`*#[WHO]*0*38#0##`

and the one-Module form:

`*#[WHO]*0*38#[SLOT]##`

The `DiagKO` sequence places the all-Module operation before repeated `DIMENSION 35` responses and applicable `DIMENSION 310` responses. The source labels `DIMENSION 38` as reset/select while describing the sequence as retrieving detailed Object and configuration information. Implementations should preserve this source ambiguity and verify Device-side effects before using the operation on unfamiliar products.

`ScanKOTimeWait` assigns an eight-second response window to the all-Module command. The one-Module form exists as a frame template but is not the command used by the canonical `DiagKO` sequence.

No explicit end marker belongs to `DiagKO`; completion is therefore governed by the response window and enclosing diagnostic scenario.

### Resolving a value

Section ID: `ownkb:section:d000017:s000005`

Applicability cues: `firmware`
Provenance cues: `catalogue`

1. Resolve the Deviceâ€™s catalogue item and firmware.
2. Resolve `SLOT` from `DIMENSION 30`; proceed with Object-scoped configuration only when `STATE = 0` identifies an enabled Module and resolves a regular configured Object.
3. Find applicable `EN_CONF` rows whose `idx` equals `INDEX`.
4. Respect the exclusive Object-scoped or firmware-scoped discriminator in `EN_CONF`.
5. Apply `EN_CONF_RANGE`, `EN_FILTER`, `EN_FILTER_RANGE`, slot conditions, conversion rules, and any system-specific validation.
6. Interpret `VAL_PAR` according to the resolved configuration data type.
7. Keep the raw value when more than one definition remains possible.

Numeric equality alone is insufficient to map a parameter to a UI field.

### Physical-configurator counterparts

Section ID: `ownkb:section:d000017:s000006`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `documentation`, `evidence`

After resolving `INDEX` to an Object property, compare that property with the physical fields declared for the resolved firmware. This can establish whether the effective property can also be configured through a physical configurator.

For shutter actuator Object `218` on firmware `192`, the catalogue provides these correspondences:

| Firmware physical field | Object property | `INDEX` | Correspondence |
| --- | --- | --- | --- |
| `M` | `M` | `0` | direct symbol and semantic match |
| `TYPE` | `SHUTTER_TYPE` | `1` | semantic match; different symbols |
| `PRE` | `PRESET_NUMBER` | `8` | semantic match; different symbols |
| `G1` | `G1` | `240` | direct symbol and semantic match |

The same firmware also declares physical `A` and `PL` positions. Those are address properties with `idx = -1` on the Object and are projected through `DIMENSION 32`, not ordinary indexed `DIMENSION 35` properties.

A direct symbol match is strong catalogue evidence. A semantic match between different symbols requires filters, symbol references, conversion rules, product documentation, UI behavior, or captures to corroborate it. Even after resolving firmware and Object context, absence of a matching physical field establishes only that no counterpart was found in the inspected metadata. An advanced-only conclusion additionally requires evidence that the applicable physical interface and mappings are complete.

A physical counterpart does not identify the active configuration method, and physical and advanced forms need not share the same encoded value or permitted range. See [Physical configuration and configuration modes](../device-model/configuration.md#physical-configuration-and-configuration-modes) for the conceptual model, and [Physical-configuration resolution](../internals/catalogue-resolution.md#physical-configuration-resolution) when physical settings select Object topology before property conversion.

### Value forms

Section ID: `ownkb:section:d000017:s000007`

Cautions: `must not`
Provenance cues: `catalogue`

Depending on the configuration definition, `VAL_PAR` can represent an enum member, numeric range value, padded address, boolean, fixed value, or user-supplied value. It can also require a conversion rule before presentation.

Detailed catalogue structures are documented in [Configuration](../device-model/configuration.md). Identifier boundaries are defined in [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md).

`rules.db3` adds cross-property validation for selected Temperature Control Objects. It can refine a resolved valueâ€™s validity but is not a general `INDEX` registry. The ScenarioDevices databases define scenario-action parameters in separate namespaces and must not be used as `EN_CONF.idx` mappings.

### Runtime availability

Section ID: `ownkb:section:d000017:s000008`

Applicability cues: `firmware`
Cautions: `do not`

`OPEN.db` models `DIMENSION 35` as a repeatable detailed-configuration response, but not every Object necessarily emits it. Observed configurable command and sensor Modules support the association with editable configuration; observed absence from another Module cannot by itself prove that the Object has no configuration.

Do not infer a universal split such as â€œactuators use only `DIMENSION 32`, commands use only `DIMENSION 35`â€. A Module can have an address, indexed parameters, both, or neither depending on its Object and firmware.

### Parameter errors

Section ID: `ownkb:section:d000017:s000009`

Provenance cues: `catalogue`

`DIMENSION 39` reports a parameter error:

`*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##`

`ERROR` is boolean in `OPEN.db`. Preserve `SLOT` and `INDEX` so the error remains attached to the attempted property.

The frame identifies that a parameter error exists but does not enumerate a cause. Catalogue range violations, conditional visibility, unsupported indices, and Device state remain possible higher-level explanations rather than encoded error values.

### Special Object parameter

Section ID: `ownkb:section:d000017:s000010`

Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `evidence`

`DIMENSION 310` uses:

`*#[WHO]*[WHERE]*310*[SLOT]*[VAL_PAR]##`

It carries no `INDEX`. Do not force it into the generic `EN_CONF.idx` mapping. Its meaning is Object-specific and remains unresolved globally.

`OPEN.db` provides no `AS_OPEN_PARAM` metadata for the `DIMENSION 310` template beyond the placeholders embedded in the frame string. Its value range and semantic decoder therefore require Object-specific evidence.

### Source reconciliation

Section ID: `ownkb:section:d000017:s000011`

Provenance cues: `source`

| Source | Contribution |
| --- | --- |
| `OPEN.db` | exact `DIMENSION 35`, `38`, `39`, and `310` templates, parameter ranges, sequence repetition, and timeout |
| `OpenQuery.txt` | ordered sequence and timeout retrieval used by MyHOME_Suite |
| `MHCatalogue.db` | configuration definitions, types, ranges, filters, conditions, and conversions |
| `rules.db3` | additional selected Temperature Control dependencies |
| Captures | actual `(SLOT, INDEX, VAL_PAR)` values and Device-specific availability |
| MyHOME_Suite UI | user-facing label, visibility, editability, and decoded presentation |

# Document: ownkb:document:d000018

Source path: `diagnostics/dimension-reference.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## Diagnostic `DIMENSION` Reference

Section ID: `ownkb:section:d000018:s000001`

Diagnostic `DIMENSION` values describe identity, versions, health, Modules, addresses, and configuration. They are scoped to the selected diagnostic `WHO` even where the canonical implementation reuses one template across several families.

The tables below cover the Device interview and detailed configuration sequences. Additional system-level service diagnostics with an empty `WHERE` are listed separately because they are not part of the standard per-Device interview.

### Identity and versions

Section ID: `ownkb:section:d000018:s000002`

Applicability cues: `firmware`, `version`
Cautions: `must not`
Provenance cues: `catalogue`, `database`, `documentation`

| `DIMENSION` | Response frame | Meaning |
| --- | --- | --- |
| `1` | `*#[WHO]*[WHERE]*1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##` | Device identity; in the ordinary addressed form, `N_CONF` is the physical configurator-position count |
| `2` | `*#[WHO]*[WHERE]*2*[FW_VERSION]##` | firmware version |
| `3` | `*#[WHO]*[WHERE]*3*[HW_VERSION]##` | hardware version |
| `4` | `*#[WHO]*[WHERE]*4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##` | configurators `1..6` |
| `5` | `*#[WHO]*[WHERE]*5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##` | configurators `7..12` |
| `6` | `*#[WHO]*[WHERE]*6*[MICRO_VERSION]##` | microcontroller version |
| `7` | `*#[WHO]*[WHERE]*7*[BITMASK_DIA_A]##` | 24-bit diagnostic bitmask A |
| `8` | `*#[WHO]*[WHERE]*8*[BITMASK_DIA_B]##` | 24-bit diagnostic bitmask B |
| `13` | `*#[WHO]*[WHERE]*13*[ID]##` | 32-bit Device ID |

`OPEN.db` describes each version placeholder as version/release/build components. Its parameter rows assign `1..99` to `FW_VERSION` and `0..99` to `HW_VERSION` and `MICRO_VERSION`, and explicitly describe the expansion as `[Version]*[Release]*[Build]`. Thus each version placeholder represents three `*`-separated components, not one scalar. Preserve all three values and distinguish this protocol representation from the catalogue tuple `V.R.b`; the metadata does not establish a firmware-selection algorithm.

In the ordinary addressed form, `N_CONF` is constrained to `0..12`. Product documentation correlates that form with the number of physical configurator positions on the Device; see [`DIMENSION 1`: Device Identity](dim1-device-identity.md).

`DIMENSION 4` and `5` each carry six configurator transport fields in the range `0..255`: `C1..C6` and `C7..C12`. `OPEN.db` also places their programming forms in the `ConfConfigurators` sequence, described there as virtual configuration. In the ordinary addressed Device form, `N_CONF` describes how many physical configurator positions the Device provides; the fixed twelve-field transport capacity must not be interpreted as twelve physical positions on every Device.

`MHCatalogue.db` separately defines firmware-specific physical symbols, legal domains, conditions, and conversions. No canonical cross-database relation establishes that `C1` universally equals the firmware `EN_CONF` row with `progressive = 1`, or that every firmware-owned `EN_CONF` definition is a literal physical plug position. Keep `C1..C12`, `EN_CONF.progressive`, and `EN_CONF.idx` as separate identifiers unless an explicit correlation is established. See [Physical-configuration resolution](../internals/catalogue-resolution.md#dimension-4-and-5-are-a-transport-boundary).

`DIMENSION 7` and `8` are typed as 24-bit bitmasks. `OPEN.db` does not define individual bit meanings. The public [Temperature Control Fault Diagnostics](temperature-control-faults.md) separately establishes active-low labels for the `WHO 1004` central-unit/zone workflow; those labels must not be generalized to other families.

### Modules, addresses, and configuration

Section ID: `ownkb:section:d000018:s000003`

Cautions: `must not`

| `DIMENSION` | Frame | Meaning |
| --- | --- | --- |
| `30` | `*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##` | enabled regular Object (`STATE = 0`) or disabled Virgin Object (`STATE = 1`) by Module |
| `31` | `*#[WHO]*[WHERE]*31*[SLOT]*[CODE]*[STATE]##` | Object-state result or error |
| `32` | `*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##` | Module system and address |
| `34` | `*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##` | Module address error |
| `35` | `*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##` | indexed configuration parameter |
| `38` | `*#[WHO]*0*38#[SLOT]##` | select/reset one Module for detailed data |
| `38` | `*#[WHO]*0*38#0##` | select/reset all Modules for detailed data |
| `39` | `*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##` | parameter error |
| `310` | `*#[WHO]*[WHERE]*310*[SLOT]*[VAL_PAR]##` | Object-specific parameter without generic index |

The `#` separators before `SLOT` and `INDEX` are part of the canonical templates and must not be normalized away.

### `DIMENSION 31` codes

Section ID: `ownkb:section:d000018:s000004`

Cautions: `do not`
Provenance cues: `source`

| Code | `OPEN.db` description |
| --- | --- |
| `0` | Object not implemented/unset |
| `1` | Object busy |
| `2` | Object already configured |
| `3` | insufficient free Object capacity |
| `4` | requested Object not implemented |

The frame also carries a boolean `STATE` labelled configured/not configured. The two â€œnot implementedâ€ descriptions are preserved from distinct source entries; the source does not further clarify their boundary.

`DIMENSION 31` records have different `error_open` classifications in `OPEN.db`: codes `0`, `2`, `3`, and `4` are errors, while busy code `1` is classified as error-and-information. These implementation categories do not add wire fields.

### Value ranges

Section ID: `ownkb:section:d000018:s000005`

Provenance cues: `database`

| Field | Range in `OPEN.db` |
| --- | --- |
| Device `ID` | `0..4294967295` |
| internal `SLOT` | `1..255` |
| `KEYO` | `1..65535` |
| configured `STATE` | `0..1` |
| `SYS` | `1..255` |
| `ADDR` | `0..65535` |
| configuration `INDEX` | `0..255` |
| `VAL_PAR` | `0..65535` |
| error flag | `0..1` |

These are transport/database ranges, not claims that every Device, Object, or system accepts every value.

### General and gateway service forms

Section ID: `ownkb:section:d000018:s000006`

Applicability cues: `gateway`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `database`

`OPEN.db` contains a second diagnostic surface using an empty `WHERE` field:

| `DIMENSION` | Frame | Database meaning |
| --- | --- | --- |
| `1` | `*#[WHO]**1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##` | gateway model identity response |
| `7` | `*#[WHO]**7##` | request general diagnostic A |
| `7` | `*#[WHO]**7*[BIT]##` | diagnostic/autodiagnostic bitmask response |
| `11` | `*#[WHO]**11*[BIT]##` | automatic hardware/software diagnostic event |
| `12` | `*#[WHO]**12##` / `*#[WHO]**12*[MAC1]*[MAC2]*[MAC3]*[MAC4]*[MAC5]*[MAC6]##` | MAC-address request/response |
| `15` | `*#[WHO]**15##` / `*#[WHO]**15*[OBJECT_MODEL]##` | WebServer model request/response |

The empty-`WHERE` gateway `DIMENSION 1` form is a distinct variant. First-hand MH202 and F454 captures both return `N_CONF = 15`, outside the ordinary addressed-form `0..12` range. Numerically, `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern; this is consistent with a reserved or sentinel value, but its exact meaning is unresolved. Do not import the ordinary physical-configurator-count interpretation into the gateway form. See [`DIMENSION 1`: Device Identity](dim1-device-identity.md#gateway-variant).

The general `DIMENSION 7`, `11`, `12`, and `15` records are directly associated with the Nurse Call system in `AS_OPEN_SYSTEM`. `OpenQuery.txt` also selects the general `DIMENSION 7` frames and the gateway `DIMENSION 1` form for gateway-connection handling. This supports reuse in a gateway/service workflow but does not make these frames part of every diagnostic familyâ€™s Device interview.

### Requests and unsolicited values

Section ID: `ownkb:section:d000018:s000007`

Uncertainty: `unknown`
Provenance cues: `database`, `source`

The canonical database includes both sequence-driven responses and general diagnostic forms. `DIMENSION 7`, for example, has Device-specific and general diagnostic templates. A collector should retain unknown or unsolicited diagnostic frames and interpret them only within the selected `WHO`, active sequence, and source direction.

The `diag_open` flag in `EN_OPEN` is broader than this page: it also marks configuration, Object programming, and scenario-programming frames. Sequence membership and frame direction are required to classify an operation correctly.

### Published Temperature Control fault surface

Section ID: `ownkb:section:d000018:s000008`

The [Temperature Control Fault Diagnostics](temperature-control-faults.md) reference adds `WHO 1004` central-unit `DIMENSION 7`/`11`, zone queries `20`/`21`, automatic zone faults `22`, and fault counts `23`. These published flows are separate from the common Device interview above.

# Document: ownkb:document:d000019

Source path: `diagnostics/temperature-control-faults.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## Temperature Control Fault Diagnostics

Section ID: `ownkb:section:d000019:s000001`

Provenance cues: `specification`

The public Temperature Control specification defines a `WHO 1004` fault-reporting surface for a central unit and its zones. It complements the MyHOME Suite Device-discovery/interview model; it does not use that model's `WHAT 10` selection or require an Object interview first.

### Targets and operations

Section ID: `ownkb:section:d000019:s000002`

Provenance cues: `source`

`#0` selects the central unit. `#1..#99` select zones through the central unit. The source also lists unprefixed master-probe addresses `1..99`, but the detailed central-unit fault flows below use the prefixed forms.

| Purpose | Request | Response/report |
| --- | --- | --- |
| Central-unit diagnostics | `*#1004*#0*7##` | `*#1004*#0*7*BIT##` |
| Central-unit automatic fault notification | No request defined in this flow | `*#1004*#0*11*BIT##` |
| Zones with failures | `*#1004*#0*20##` | One or more `*#1004*#ZONE*21*BIT##` |
| One zone | `*#1004*#ZONE*21##` | `*#1004*#ZONE*21*BIT##` |
| All zones | `*#1004*#0*21##` | One or more `*#1004*#ZONE*21*BIT##` |
| Automatic zone fault notification | No request defined in this flow | `*#1004*#ZONE*22*BIT##` |
| Fault/non-response counts | `*#1004*#0*23##` | `*#1004*#0*23*NO_RESPONSE*FAULTS##` |

`ZONE` is a placeholder for `1..99`. `NO_RESPONSE` is the number of non-answering probes; `FAULTS` is the number of probes with failures. Preserve that order.

The collective flows can begin with an echo-shaped header such as `*#1004*#0*20##` or `*#1004*#0*21##`, before the zone data. A command-session sequence then terminates with `ACK` or `NACK`. The request selector need not equal every returned selector: a `DIMENSION 20` request returns `DIMENSION 21` zone records. Correlate using the complete operation, not selector equality alone.

### Central-unit bits

Section ID: `ownkb:section:d000019:s000003`

Provenance cues: `source`

For `DIMENSION 7` and `11`, the source names 24 bits and identifies the following conditions. These are **active-low**: the listed condition is present when its bit is `0`.

| Source bit number | Condition when `0` |
| --- | --- |
| `13` | Probe failure |
| `14` | Probe does not answer |
| `15` | Central-unit battery fault |
| `16` | EEPROM read/write failure |
| `21` | Generic system trouble |
| `22` | Configuration trouble |
| `23` | Hardware failure |
| `24` | Device busy |

### Zone bits

Section ID: `ownkb:section:d000019:s000004`

Cautions: `do not`
Provenance cues: `source`

For `DIMENSION 21` and `22`, the source names 16 bits. Again, `0` indicates the condition.

| Source bit number | Condition when `0` |
| --- | --- |
| `11` | Probe does not answer |
| `12` | Pump does not answer |
| `13` | EEPROM read/write failure |
| `14` | Temperature out of range |
| `15` | Slave probe does not answer |
| `16` | Actuator does not answer |

These tables preserve the source's bit numbering. The cited sections do not supply a worked numeric mask or an unambiguous serialized bit-order example. Keep `BIT` raw until the target's representation and bit-order convention are established; do not invent meanings for the unlisted bits.

### Scope and completion

Section ID: `ownkb:section:d000019:s000005`

Cautions: `must not`

These fault labels apply to the published central-unit/zone workflow. They must not be copied to `WHO 1001` or every generic `DIMENSION 7`/`8` Device response. Likewise, the `WHO 1004` zone `DIMENSION 22` is a fault mask, while functional `WHO 4 DIMENSION 22` controls split units.

An empty or failed collective request does not prove a healthy installation. Preserve the acknowledgement outcome, returned records, and timeout state. Asynchronous `DIMENSION 11` and `22` notifications report fault changes; they are not acknowledgement-terminated command transactions.

### Evidence basis

Section ID: `ownkb:section:d000019:s000006`

Applicability cues: `version`
Provenance cues: `specification`

The [Temperature Control Specification](../sources/openwebnet-public/pdf/WHO_4.pdf), version 2.0.0, pages 69â€“74, defines these targets, sequences, counts, bit labels, and polarity. See [Diagnostic Architecture](architecture.md) for the separate MyHOME Suite management model and [Temperature Control Properties](../functional/who-4-temperature-control/dimensions.md) for functional properties.

# Document: ownkb:document:d000020

Source path: `diagnostics/what-reference.md`
Namespace context: `diagnostic`
Area: `diagnostics`

## Diagnostic `WHAT` Reference

Section ID: `ownkb:section:d000020:s000001`

Diagnostic `WHAT` values control discovery and interview sessions. Their meaning is scoped to a diagnostic `WHO`; matching numeric values in a functional `WHO` are unrelated unless independently documented.

### Values

Section ID: `ownkb:section:d000020:s000002`

Provenance cues: `source`

| `WHAT` | Direction | Frame | Meaning in `OPEN.db` |
| --- | --- | --- | --- |
| `4` | Device â†’ programmer | `*[WHO]*4*[WHERE_FAKE]##` | Device end of transmission |
| `4` | Device â†’ programmer | `*[WHO]*4*0##` | end-of-transmission variant |
| `5` | Programmer â†’ Device | `*[WHO]*5*0##` | start diagnosis through local-button/general mode |
| `6` | Either diagnostic participant in source labels | `*[WHO]*6*0##` | abort/close diagnosis |
| `10` | Programmer â†’ Device | `*[WHO]*10#[ID]*0##` | start diagnosis by Device ID |
| `11` | Programmer â†’ Device | `*[WHO]*11#[ID]*0##` | mark/suppress an ID already found during enumeration |
| `12` | Programmer â†’ Device | `*[WHO]*12*0##` | release/reset Device-ID enumeration state |

These values are management operations inside the selected diagnostic family. The same numeric `WHAT` under another `WHO`, or in a programming lifecycle, can have different semantics.

### `WHAT 4`: end of transmission

Section ID: `ownkb:section:d000020:s000003`

Applicability cues: `version`
Cautions: `do not`

`WHAT 4` is the positive terminal marker for a Device interview. The main diagnostic sequences place it after identity, version, health, Module, address, and applicable error responses.

The `[WHERE_FAKE]` label is an implementation label, not a general OpenWebNet field type. Preserve the received value but do not treat it as a newly discovered functional address. `OPEN.db` also contains the `*[WHO]*4*0##` form.

The sequence metadata does not mark the end frame mandatory, even though observed interviews use it as the normal completion marker. A collector must retain timeout and abort completion states separately.

### `WHAT 5`: local/general start

Section ID: `ownkb:section:d000020:s000004`

Cautions: `do not`
Provenance cues: `database`

`WHAT 5` begins the `DiagLocalButton` sequence. The database name implies a local-button workflow, while the wire frame itself carries neither Device ID nor address. Device selection therefore depends on external/local state not represented in the frame.

Do not use this mode when several Devices could respond unless the installation procedure provides a reliable physical selection step.

### `WHAT 6`: abort or close

Section ID: `ownkb:section:d000020:s000005`

`OPEN.db` contains programmer-abort and Device-abort entries with the same frame. Treat it as a session-closing signal whose origin must be derived from transport direction and active state.

An abort does not certify that a full response set was received. Keep partial data marked incomplete.

### `WHAT 10`: interview by ID

Section ID: `ownkb:section:d000020:s000006`

`WHAT 10` selects one installed Device by its 32-bit ID and begins a full interview. It is distinct from the `DIMENSION 13` request used to enumerate IDs.

### `WHAT 11`: suppress a discovered ID

Section ID: `ownkb:section:d000020:s000007`

During ID enumeration, the programmer sends `WHAT 11` for each returned ID. The `ScanAID` sequence repeats this operation before requesting IDs again. Observed traffic supports interpreting it as suppressing or acknowledging an already enumerated Device for the current scan state.

This is scan control, not a permanent Device configuration change.

### `WHAT 12`: release enumeration state

Section ID: `ownkb:section:d000020:s000008`

Applicability cues: `applies to`

`WHAT 12` brackets ID enumeration. Send it before a new scan and after the final empty pass so Device-side scan state does not leak into the next operation.

The frame carries no Device ID and applies to the selected diagnostic `WHO` scope.

### Related programming values

Section ID: `ownkb:section:d000020:s000009`

Cautions: `must not`
Provenance cues: `database`

The same `OPEN.db` registry also contains programming operations such as `WHAT 9` for configuration by Device ID and programming-specific `WHAT 1`, `2`, `3`, `7`, `14`, `51`, and `52`. They are outside this diagnostic reference and belong under [`programming/`](../programming/). Their presence is one reason the `diag_open` database flag must not be treated as a diagnostics-only classification.

# Document: ownkb:document:d000021

Source path: `functional/README.md`
Namespace context: `contextual`
Area: `functional`

## Functional Protocol

Section ID: `ownkb:section:d000021:s000001`

Provenance cues: `database`, `evidence`, `source`, `specification`

The functional protocol reference documents OpenWebNet systems using `WHO` as the canonical protocol namespace. Each `WHO` defines the context in which its `WHAT` values, `WHERE` grammar, `DIMENSION` identifiers, parameters, and operation-specific behavior are interpreted.

Common frame syntax is defined in [Protocol](../protocol/). Reference material is organized by protocol namespace, while the indexes below provide both protocol-oriented and function-oriented navigation to the same canonical pages.

The [`Functional Source Coverage`](source-coverage.md) page records which namespaces have a dedicated public specification and which rely on narrower implementation evidence. The MyHOME_Suite [`OPEN.db` coverage matrix](open-db-coverage.md) documents what that implementation database establishes for every functional namespace: system identity, diagnostic-family mapping, management support, address rules, and concrete `EN_OPEN` frame associations where present. The broader [`cross-database functional coverage`](cross-database-coverage.md) correlates `OPEN.db` with `MHCatalogue.db`, the two ScenarioDevices databases, and `rules.db3`, including functional command templates and Device/Object applicability that are not represented in `OPEN.db` alone.

### By `WHO`

Section ID: `ownkb:section:d000021:s000002`

Applicability cues: `gateway`

| `WHO` | System | Reference |
| --- | --- | --- |
| `0` | Scenarios | [`WHO 0` - Scenarios](who-0-scenarios/) |
| `1` | Lighting | [`WHO 1` - Lighting](who-1-lighting/) |
| `2` | Automation | [`WHO 2` - Automation](who-2-automation/) |
| `3` | Load Management | [`WHO 3` - Load Management](who-3-load-management/) |
| `4` | Temperature Control | [`WHO 4` - Temperature Control](who-4-temperature-control/) |
| `5` | Alarm | [`WHO 5` - Alarm](who-5-alarm/) |
| `6` | Basic Video Door Entry | [`WHO 6` - Basic Video Door Entry](who-6-basic-video-door-entry/) |
| `7` | Multimedia / Video | [`WHO 7` - Multimedia System](who-7-multimedia-video/) |
| `8` | Video Door Entry and Telephony | [`WHO 8` - Video Door Entry and Telephony](who-8-video-door-entry-telephony/) |
| `9` | Auxiliaries | [`WHO 9` - Auxiliaries](who-9-auxiliaries/) |
| `10` | Navigation commands | [`WHO 10` - Navigation Commands](who-10-navigation/) |
| `11` | Energy distribution | [`WHO 11` - Energy Distribution](who-11-energy-distribution/) |
| `12` | Messages | [`WHO 12` - Messages](who-12-messages/) |
| `13` | Integration / Gateway functions | [`WHO 13` - Integration and Gateway Functions](who-13-integration-gateway/) |
| `14` | Special commands | [`WHO 14` - Special Commands](who-14-special-commands/) |
| `15` | Home-automation Main Unit / CEN | [`WHO 15` - CEN](who-15-cen/) |
| `16` | Sound System | [`WHO 16` - Sound System](who-16-sound-system/) |
| `17` | Scenario Management | [`WHO 17` - Scenario Management](who-17-scenario-management/) |
| `18` | Energy Management | [`WHO 18` - Energy Management](who-18-energy-management/) |
| `19` | Interface | [`WHO 19` - Interface](who-19-interface/) |
| `22` | Multimedia / Sound Diffusion | [`WHO 22` - Sound Diffusion](who-22-sound-diffusion/) |
| `23` | Access Control | [`WHO 23` - Access Control](who-23-access-control/) |
| `24` | Lighting Management | [`WHO 24` - Lighting Management](who-24-lighting-management/) |
| `25` | Transversal Functions | [`WHO 25` - Transversal Functions](who-25-transversal/) |
| `26` | UPnP multimedia command | [`WHO 26` - UPnP Multimedia](who-26-upnp-multimedia/) |
| `27` | Nurse Call basic level | [`WHO 27` - Nurse Call Basic Level](who-27-nurse-call/) |
| `99` | Service Identification | [`WHO 99` - Session and Service Identification](who-99-service-identification/) |

The table reflects the functional namespace established by the public specifications together with the MyHOME_Suite implementation data. A listed `WHO` does not imply that every semantic value is currently known.

### By function

Section ID: `ownkb:section:d000021:s000003`

Applicability cues: `gateway`

| Functional area | Protocol reference |
| --- | --- |
| Scenarios | [`WHO 0`](who-0-scenarios/), [`WHO 17`](who-17-scenario-management/) |
| Lighting | [`WHO 1`](who-1-lighting/), [`WHO 24`](who-24-lighting-management/) |
| Automation | [`WHO 2`](who-2-automation/) |
| Load and energy | [`WHO 3`](who-3-load-management/), [`WHO 11`](who-11-energy-distribution/), [`WHO 18`](who-18-energy-management/) |
| Temperature control | [`WHO 4`](who-4-temperature-control/) |
| Alarm | [`WHO 5`](who-5-alarm/) |
| Video Door Entry and multimedia | [`WHO 6`](who-6-basic-video-door-entry/), [`WHO 7`](who-7-multimedia-video/), [`WHO 8`](who-8-video-door-entry-telephony/), [`WHO 26`](who-26-upnp-multimedia/) |
| Auxiliaries | [`WHO 9`](who-9-auxiliaries/) |
| Navigation and messages | [`WHO 10`](who-10-navigation/), [`WHO 12`](who-12-messages/) |
| Integration and interface | [`WHO 13`](who-13-integration-gateway/), [`WHO 19`](who-19-interface/) |
| Special commands | [`WHO 14`](who-14-special-commands/) |
| CEN / CEN+ | [`WHO 15`](who-15-cen/), [CEN+ in `WHO 25`](who-25-transversal/cen-plus.md) |
| Sound | [`WHO 16`](who-16-sound-system/), [`WHO 22`](who-22-sound-diffusion/) |
| Access control | [`WHO 23`](who-23-access-control/) |
| Dry contacts / IR | [Dry-contact and IR functions in `WHO 25`](who-25-transversal/dry-contact-ir.md) |
| Nurse Call | [`WHO 27`](who-27-nurse-call/) |
| Protocol services | [`WHO 99`](who-99-service-identification/) |

### Evidence labels

Section ID: `ownkb:section:d000021:s000004`

Cautions: `not evidence`
Uncertainty: `unresolved`
Provenance cues: `database`, `evidence`

Each page should distinguish:

- **published protocol** - values and grammar stated by a canonical public `WHO` document;
- **implementation evidence** - MyHOME Suite database templates, address rules, or scenario capabilities;
- **observed behavior** - private captures or Device experiments;
- **unresolved** - namespace or field exists, but the current corpus does not establish its semantics.

A namespace row is not evidence for a complete vocabulary. Conversely, absence from an implementation table is not proof that a published functional operation does not exist.

### Scope

Section ID: `ownkb:section:d000021:s000005`

Provenance cues: `catalogue`, `database`, `evidence`

`WHAT` and `DIMENSION` identifiers are documented within the `WHO` that defines them. `WHERE` is likewise interpreted according to the selected `WHO`; it is not a universal address type.

Where one `WHO` contains several functional groups, those groups are divided into subordinate pages when that improves the reference while remaining under the canonical `WHO` directory. Systems with a larger established vocabulary use dedicated `WHAT`, addressing, or `DIMENSION` pages; smaller or less completely established systems keep the supported semantics together.

Diagnostic and configuration/programming operations are documented separately under `diagnostics/` and `programming/`. The [`OPEN.db` coverage matrix](open-db-coverage.md) cross-references those management capabilities without reclassifying diagnostic frames as functional `WHO` commands; the [`cross-database functional coverage`](cross-database-coverage.md) adds catalogue and scenario-engine evidence while preserving each database's independent identifier spaces.

# Document: ownkb:document:d000022

Source path: `functional/cross-database-coverage.md`
Namespace context: `contextual`
Area: `functional`

## Cross-database functional coverage

Section ID: `ownkb:section:d000022:s000001`

Cautions: `must not`
Provenance cues: `database`

The MyHOME_Suite databases describe different layers of the same implementation. They should be correlated, but their identifiers must not be joined merely because they have the same numeric value.

- `OPEN.db` describes protocol systems, address grammars, management operations, parameters, sequences, diagnostics, and programming workflows.
- `MHCatalogue.db` describes physical Devices and the Device â†’ Module â†’ Object â†’ Configuration capability model.
- `ScenarioDevices-program-files.sqlite` and `ScenarioDevices-programdata.sqlite` describe the scenario engine's functional Objects, actions, triggers, conditions, command templates, and parameter constraints.
- `rules.db3` contains additional validation/dependency data and is not a general `WHO` registry.

This page records the useful intersections without inventing database relationships that are not present.

### `MHCatalogue.db` system layer

Section ID: `ownkb:section:d000022:s000002`

Cautions: `do not`, `must not`
Provenance cues: `catalogue`

`MHCatalogue.db.EN_SYSTEM` is a catalogue namespace, not the same identifier space as `OPEN.db.EN_SYSTEM`. Its rows nevertheless establish which broad functional systems the catalogue can assign to physical items through `AS_ITEM_SYSTEM`.

| Catalogue system | `EN_SYSTEM.id_system` | `sys_modobj` | Catalogue items | Catalogue Devices | Functional relationship |
| --- | --- | --- | --- | --- | --- |
| Automation | `1` | `1` | `113` | `338` | Lighting / Automation Objects and Devices |
| Temperature control | `2` | `3` | `17` | `57` | `WHO 4` device capability |
| Burglar alarm system | `3` | `4` | `7` | `10` | `WHO 5` device capability |
| Video door entry system | `4` | `6` | `20` | `39` | Video-door-entry families |
| Sound system | `5` | `8` | `1` | `2` | Sound / multimedia capability |
| Auxiliary | `6` | `9` | `0` | `0` | Auxiliary namespace represented, no directly assigned catalogue item in this dataset |
| Energy management functions | `7` | `17` | `0` | `0` | Legacy/load-management capability namespace |
| Access control | `8` | `7` | `9` | `15` | `WHO 23` device capability |
| New energy saving and load control | `20` | `2` | `13` | `29` | Energy/load-control Devices |
| Integration function | `26` | `15` | `43` | `83` | Integration-capable Devices |
| Hospital signaling system | `29` | `5` | `0` | `0` | Nurse Call / signalling capability namespace |

The catalogue also defines interface-only systems for Automation, burglar alarm, multimedia, Access Control, eight-wire Video Door Entry, and other bus levels. These rows are useful when interpreting interface Devices, but they do not independently assign an OpenWebNet `WHO`.

`sys_modobj` is a catalogue model value. It is not a functional or diagnostic `WHO` and must not be used as one.

### ScenarioDevices functional command layer

Section ID: `ownkb:section:d000022:s000003`

Provenance cues: `database`

The two ScenarioDevices databases provide a complementary view that `OPEN.db` largely does not: concrete functional operations usable by the MyHOME_Suite scenario engine.

The program-files database contains 29 Object-system rows, 44 DeviceObjects, 157 Commands, and 42 Parameters. The program-data copy contains 27 Object-system rows, 42 DeviceObjects, 151 Commands, and 40 Parameters. Their common functional command model is substantially the same; the program-files copy additionally contains the Virtual Key Card trigger family and two Temperature Control action records.

#### Explicit OpenWebNet frame families

Section ID: `ownkb:section:d000022:s000004`

Cautions: `not evidence`
Provenance cues: `database`, `evidence`

Where ScenarioDevices supplies both `ChiOpen` and `Frame`, the following functional namespaces are explicit:

| `WHO` | Scenario-engine capability | Examples established by the database |
| --- | --- | --- |
| `0` | Scenario-module action | `*0*N*WHERE##` |
| `1` | Lighting and Lighting-like actions | OFF/ON, timed ON, 100-level dimming, controlled socket, fan, automation door lock |
| `2` | Automation | UP/DOWN/STOP, absolute position, advanced movement, step-by-step movement |
| `4` | Temperature Control | MyHOME_Suite `DIMENSION 7` operating-mode/setpoint actions plus local-control and fan-coil writes |
| `14` | Special commands | actuator lock and unlock |

This is implementation evidence for commands that MyHOME_Suite can place in scenarios. It is not evidence that the scenario engine enumerates every valid functional command for those WHOs.

#### `WHO 14` semantics recovered

Section ID: `ownkb:section:d000022:s000005`

Provenance cues: `evidence`

ScenarioDevices resolves the previously ambiguous `WHO 14` operations through the Object and command names attached to the frames:

| ScenarioDevices command | Frame | Meaning |
| --- | --- | --- |
| `miniScenarioSuite.specialCommands.actionLockUnlockActuator.lock` | `*14*0*WHERE##` | Lock actuator |
| `miniScenarioSuite.specialCommands.actionLockUnlockActuator.unlock` | `*14*1*WHERE##` | Unlock actuator |

This is direct MyHOME_Suite implementation evidence for `WHAT 0` and `WHAT 1` in the actuator lock/unlock Object context.

#### `WHO 1` target-dependent interpretation

Section ID: `ownkb:section:d000022:s000006`

Uncertainty: `unresolved`

ScenarioDevices contains a notable overlap with the published Lighting vocabulary. The command `miniScenarioSuite.automation.actionAutomationDoorLock.on` stores the template `*1*17*WHERE##`. The published Lighting summary calls `WHAT 17` 30-second timed ON, but section 3.1.9 says 30 minutes; the duration is unresolved. See the [Lighting Timing Qualification](who-1-lighting/what.md#target-dependent-myhome-suite-label-for-what-17).

The databases establish a target-specific capability label, not observed emission, actual lock behavior, or independent resolution of the timing conflict. Preserve the label, template, and unresolved timing separately.

This is an example of why `WHO` + `WHAT` alone is not always sufficient for a user-facing capability label.

#### `WHO 4` implementation-only action surface

Section ID: `ownkb:section:d000022:s000007`

ScenarioDevices provides exact MyHOME_Suite action templates using `DIMENSION 7`:

| Mode | Heat | Cool | Auto | Generic |
| --- | --- | --- | --- | --- |
| Comfort | `*#4*ZAZB*#7*1*3*##` | `*#4*ZAZB*#7*2*3*##` | `*#4*ZAZB*#7*3*3*##` | `*#4*ZAZB*#7*0*3*##` |
| Eco | `*#4*ZAZB*#7*1*4*##` | `*#4*ZAZB*#7*2*4*##` | `*#4*ZAZB*#7*3*4*##` | `*#4*ZAZB*#7*0*4*##` |
| Protection | `*#4*ZAZB*#7*1*2*##` | `*#4*ZAZB*#7*2*2*##` | `*#4*ZAZB*#7*3*2*##` | `*#4*ZAZB*#7*0*2*##` |
| Setpoint | `*#4*ZAZB*#7*1*1*c1c2c3c4##` | `*#4*ZAZB*#7*2*1*c1c2c3c4##` | `*#4*ZAZB*#7*3*1*c1c2c3c4##` | `*#4*ZAZB*#7*0*1*c1c2c3c4##` |

It also defines OFF as `*#4*ZAZB*#7*0*5*##`, local control as `*#4*ZAZB*#5*val##`, and fan-coil speed as `*#4*ZAZB*#11*val##`.

These are MyHOME_Suite implementation templates. They complement, rather than replace, the public `WHO 4` functional `DIMENSION` table.

### Scenario capabilities without explicit OpenWebNet frames

Section ID: `ownkb:section:d000022:s000008`

Cautions: `do not`
Provenance cues: `source`

ScenarioDevices also defines Alarm, Auxiliaries, hotel-room, scheduled-scenario, time, and Virtual Key Card trigger/condition/action capabilities for which the `Frame` column is null or contains a symbolic internal expression rather than a complete OpenWebNet frame.

Those rows establish application-level capabilities, but they do not justify manufacturing a `WHO`, `WHAT`, or `DIMENSION` mapping. They should be used as semantic leads only when another source establishes the wire representation.

### How the three databases complement each other

Section ID: `ownkb:section:d000022:s000009`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`, `evidence`

A useful implementation interpretation is:

| Question | Strongest database evidence |
| --- | --- |
| Which protocol system / diagnostic family does MyHOME_Suite know? | `OPEN.db.EN_SYSTEM` |
| Which `WHERE` grammar does the implementation construct? | `OPEN.db.EN_ADDRESS_RULE` and association tables |
| Which management/configuration frame does it send? | `OPEN.db.EN_OPEN` and `AS_OPEN_*` |
| Which physical Devices support a functional system? | `MHCatalogue.db.EN_DEVICE` â†’ `EN_ITEM` â†’ `AS_ITEM_SYSTEM` |
| Which Modules and Objects can a Device expose? | `MHCatalogue.db` firmware/slot/Object tables |
| Which configuration properties and ranges exist? | `MHCatalogue.db.EN_CONF`, ranges, filters, and firmware associations |
| Which functional actions can the scenario engine emit? | ScenarioDevices `Commands.Frame` / `ChiOpen` |
| Which action parameters are constrained? | ScenarioDevices `Parameters` |

The databases therefore describe **different projections of the implementation**, not redundant copies of one protocol catalogue.

### Cross-reference rule

Section ID: `ownkb:section:d000022:s000010`

Cautions: `do not`
Provenance cues: `catalogue`, `database`, `specification`

Do not numerically join `OPEN.db.EN_SYSTEM.id_system`, `MHCatalogue.db.EN_SYSTEM.id_system`, ScenarioDevices `FamilyId`, ScenarioDevices `ObjectId`, or `MHCatalogue.db.EN_KEY_OBJECT.key_object`. These are independent identifier spaces.

A cross-database relationship should be asserted only when one of the following establishes it:

1. an explicit database relationship;
2. an exact OpenWebNet frame containing the `WHO`;
3. matching implementation semantics corroborated by the protocol specification or observed traffic;
4. a Device/Object mapping already established through the MyHOME_Suite catalogue model.

This keeps implementation-derived enrichment useful without turning coincidental numeric equality into protocol semantics.

See [MyHOME_Suite `OPEN.db` Coverage](open-db-coverage.md) for the complete `OPEN.db` namespace/management matrix and [Device Model](../device-model/) for the catalogue Device â†’ Module â†’ Object â†’ Configuration model. See [Scenario Engine](../scenario-engine/) for the complete ScenarioDevices schema, category and matching model, parameter types, template rendering rules, capability coverage, and execution boundaries.

# Document: ownkb:document:d000023

Source path: `functional/open-db-coverage.md`
Namespace context: `contextual`
Area: `functional`

## MyHOME_Suite `OPEN.db` Coverage

Section ID: `ownkb:section:d000023:s000001`

Provenance cues: `database`, `evidence`

The MyHOME_Suite `OPEN.db` database provides two different kinds of evidence for functional protocol systems:

1. `EN_SYSTEM` records the system name, functional `WHO`, diagnostic `WHO`, and whether MyHOME_Suite marks the system as managed.
2. `EN_OPEN` together with `AS_OPEN_SYSTEM` records concrete frame templates for a smaller subset of systems. Most of these templates are diagnostic, configuration, calibration, scenario-programming, or service operations rather than ordinary functional `WHAT` commands.

The distinction is important. A system row establishes that MyHOME_Suite knows the namespace; it does not imply that `OPEN.db` contains its complete functional command vocabulary.

### Functional namespace registry

Section ID: `ownkb:section:d000023:s000002`

Cautions: `must not`
Provenance cues: `database`

| `WHO` | MyHOME_Suite system | `EN_SYSTEM.id_system` | Diagnostic `WHO` | `managed` | `EN_OPEN` associations | What `OPEN.db` establishes |
| --- | --- | --- | --- | --- | --- | --- |
| `0` | Scenarios | `30` | - | `0` | `0` | Namespace and system identity |
| `1` | Light and Automation system | `1` | `1001` | `1` | `65` | Shared Lighting/Automation diagnostic and programming model |
| `1` | Interface AUTOM L3 | `10` | `1001` | `1` | `0` | Namespace/interface variant; no direct operation association |
| `1` | Interface AUTOM L4 | `11` | `1001` | `1` | `0` | Namespace/interface variant; no direct operation association |
| `3` | Load Management system | `7` | - | `0` | `0` | Namespace and system identity |
| `4` | Thermoregulation | `2` | `1004` | `1` | `46` | Diagnostic/configuration workflow plus thermoregulation-specific scan and address rules |
| `5` | Alarms | `3` | - | `0` | `0` | Namespace and system identity |
| `5` | Interface AI L3 | `12` | - | `0` | `0` | Alarm-interface system variant |
| `6` | Interface Multimedia L2 | `13` | - | `0` | `0` | Multimedia interface system variant |
| `6` | Basic Video door entry system | `32` | - | `0` | `0` | Namespace and system identity |
| `7` | Multimedia | `42` | - | `0` | `0` | Namespace and system identity |
| `8` | Video Door entry system and telephony | `5` | `1008` | `1` | `1` | Managed diagnostic family and service-identification operation association |
| `9` | Auxiliaries | `6` | - | `0` | `0` | Namespace and system identity |
| `10` | Navigation command | `33` | - | `0` | `0` | Namespace and system identity |
| `11` | Energy distribution | `34` | - | `0` | `0` | Namespace and system identity |
| `12` | Messages | `39` | - | `0` | `0` | Namespace and system identity |
| `13` | Integration Functions | `26` | `1013` | `1` | `0` | Managed functional/diagnostic family and F422 interface address rules |
| `14` | Special commands | `35` | - | `0` | `0` | Namespace and system identity |
| `15` | Home automation main unit command | `36` | - | `0` | `0` | Namespace and system identity |
| `16` | Sound system | `4` | - | `0` | `0` | Namespace and system identity |
| `17` | Home automation main unit management | `37` | - | `0` | `0` | Namespace and system identity |
| `18` | Energy Management system | `20` | `1018` | `1` | `65` | Shared managed diagnostic/programming model and energy-specific address rules |
| `19` | Interface | `40` | - | `0` | `0` | Namespace and system identity |
| `22` | Multimedia System | `41` | `1022` | `0` | `0` | Functional namespace plus a diagnostic-family identifier |
| `23` | Access Control | `8` | `1023` | `1` | `65` | Shared managed diagnostic/programming model and Access Control address rules |
| `24` | Lighting Management system | `23` | - | `0` | `0` | Namespace and system identity |
| `25` | Transversal Command | `24` | - | `0` | `0` | Namespace and system identity |
| `26` | UPnP Multimedia Command | `25` | - | `0` | `0` | Namespace and system identity |
| `27` | Nurse Call basic level system | `38` | `1027` | `0` | `9` | Authentication/service identity and general diagnostic operations |
| `99` | Service Identification | `31` | - | `0` | `0` | Namespace and system identity |

`WHO 2` is intentionally absent as a separate `EN_SYSTEM` row: MyHOME_Suite groups Lighting and Automation in `id_system = 1`, whose functional `WHO` field is `1` and whose diagnostic family is `1001`. This database representation must not be interpreted as eliminating functional `WHO 2`; the functional protocol still uses `WHO 2` for Automation.

### Systems with concrete `EN_OPEN` templates

Section ID: `ownkb:section:d000023:s000003`

#### `WHO 1` / diagnostic `WHO 1001`

Section ID: `ownkb:section:d000023:s000004`

Provenance cues: `evidence`, `source`

The `Light and Automation system` is associated with 65 `EN_OPEN` records. The set registers the common managed-device workflow available to MyHOME_Suite for Lighting/Automation: identity (`DIMENSION 1`, `2`, `3`, `6`, `13`), physical configurators (`DIMENSION 4` and `5`), diagnostic masks (`7`, `8`), Module/Object discovery (`30`, `32`), configuration parameters (`35`, `38`, `39`, `310`), configuration lifecycle, discovery by address or Device ID, and scenario-programming operations. This association establishes an implementation capability surface, not support for every operation on every installed Device.

`OPEN.db` therefore provides substantial evidence about the MyHOME_Suite management plane for Lighting and Automation, but it is not the source of the ordinary `WHO 1` and `WHO 2` functional command tables.

The system-level address rules include normal Light/Automation `A`/`PL` addressing and the F422 logic/physical-extension form:

| Rule | Virtual form | Advanced form |
| --- | --- | --- |
| General Light/Automation | `[A][PL]` | `[A][PL]+` |
| F422 logic/physical extension | `[I3][I4]` | `[I3][I4]+` |

#### `WHO 4` / diagnostic `WHO 1004`

Section ID: `ownkb:section:d000023:s000005`

Provenance cues: `evidence`

Thermoregulation is associated with 46 `EN_OPEN` records. It shares the core identity, configuration, Module/Object, diagnostic, and error frames, and adds a thermoregulation-specific scan operation `*#[WHO]*00[ZAZB]*1##`.

`OPEN.db` defines several thermoregulation address classes:

| Target class | Virtual form | Advanced form |
| --- | --- | --- |
| General | `[ZA][ZB]` | `[ZAZB]` |
| Four-zone control unit | `#0#[ZA][ZB]` | `#0#[ZAZB]` |
| Actuator | `[ZA][ZB]#[N]` | `[ZAZB]#[N]` |
| Slave probe | `[SLA][ZA][ZB]` | `[SLA][ZAZB]` |
| External probe | `[PL_N]00` | `[PL_N]00` |

This is stronger implementation evidence than merely knowing that `WHO 4` exists: it establishes the target classes MyHOME_Suite itself distinguishes when constructing management traffic.

#### `WHO 8` / diagnostic `WHO 1008`

Section ID: `ownkb:section:d000023:s000006`

Provenance cues: `database`

Video Door Entry and telephony is marked `managed = 1` and assigned diagnostic `WHO 1008`. Its system-level address rule is the F422 public-riser-interface form `1[I1][I2][I3][I4]`, with advanced form `1[I1I2I3I4]`.

The only direct `AS_OPEN_SYSTEM` association is `EN_OPEN.id_open = 59`, labelled `cmd_ident`, with template `*[WHO]*[WHAT]##` and description "programmer send open identification code for the service". Because the frame is parameterized and the database does not enumerate its `WHAT` semantics here, this association establishes a service-identification operation for the system but not a complete `WHO 8` functional vocabulary.

#### `WHO 13` / diagnostic `WHO 1013`

Section ID: `ownkb:section:d000023:s000007`

Applicability cues: `gateway`

`Integration Functions` is marked `managed = 1` and assigned diagnostic `WHO 1013`. No `EN_OPEN` operation is directly associated with the system, but `AS_SYSTEM_ADDRESS_RULE` provides two concrete F422 interface modes:

| F422 mode | Virtual form | Advanced form |
| --- | --- | --- |
| Burglar alarm interface | `[I4]` | `[I4]` |
| Galvanic separation / New physical separation | `[I4]` | `[I4]` |

This shows that the MyHOME_Suite `WHO 13` model is not limited to IP-gateway clock/network information. The implementation data also treats `WHO 13` as the Integration Functions namespace used with F422 interface modes. The public Gateway API and this integration/interface role should therefore be documented as complementary capabilities of the same functional namespace rather than collapsed into transport/session behavior.

#### `WHO 18` / diagnostic `WHO 1018`

Section ID: `ownkb:section:d000023:s000008`

Provenance cues: `database`

Energy Management is marked `managed = 1`, uses diagnostic `WHO 1018`, and is associated with the same 65-record managed-device operation set as Lighting/Automation and Access Control. This associates the family with MyHOME_Suite's common Device â†’ Module â†’ Object â†’ Configuration management capability in addition to the functional energy `DIMENSION` operations. It does not establish that every installed Energy Management Device supports every registered operation.

The database defines two Energy Management address classes:

| Target class | Virtual form | Advanced form |
| --- | --- | --- |
| Control unit / measurement target | `5[A1][A2][A3]` | `5[A123]` |
| Actuator | `7[P1][P2]#0` | `7[P]#[PHASE]` |

The functional `WHO 18` reference should preserve the distinction between these implementation address rules and the higher-level meter/actuator `WHERE` forms documented by the public protocol.

#### `WHO 23` / diagnostic `WHO 1023`

Section ID: `ownkb:section:d000023:s000009`

Provenance cues: `database`, `evidence`

Access Control is marked `managed = 1`, uses diagnostic `WHO 1023`, and is associated with the same 65-record managed-device operation set. The database therefore associates Access Control with the same identity, discovery, Module/Object, configuration, error, and scenario-programming capability surface. It does not establish support for every registered operation on every installed Access Control Device.

Two Access Control address classes are explicit:

| Target class | Virtual form | Advanced form |
| --- | --- | --- |
| Command or virgin Device | `20` | `20` |
| Indicators | `7[R1][R2]` | `7[R1R2]` |

The labels come directly from the MyHOME_Suite `EN_ADDRESS_RULE` definitions. They should not be generalized into additional Access Control semantics without corroborating evidence.

#### `WHO 27` / diagnostic `WHO 1027`

Section ID: `ownkb:section:d000023:s000010`

Provenance cues: `database`

Nurse Call is unusual. `EN_SYSTEM` assigns functional `WHO 27` and diagnostic `WHO 1027`, but `managed` is `0`. Nevertheless, nine concrete `EN_OPEN` records are associated with the system:

| Operation | Frame template | Database description |
| --- | --- | --- |
| Password challenge operations | `*#[OPERATIONS]##` | Device returns logic operations to apply to the password |
| Password result | `*#[RESULT]##` | Programmer sends password result |
| General diagnostic request | `*#[WHO]**7##` | Request general diagnostic A |
| Diagnostic mask response | `*#[WHO]**7*[BIT]##` | Device returns diagnostic mask |
| Automatic diagnostic event | `*#[WHO]**11*[BIT]##` | Hardware/software problem mask |
| WebServer model request | `*#[WHO]**15##` | Request WebServer model |
| MAC request | `*#[WHO]**12##` | Request MAC address |
| WebServer model response | `*#[WHO]**15*[OBJECT_MODEL]##` | Device returns WebServer object model |
| MAC response | `*#[WHO]**12*[MAC1]*[MAC2]*[MAC3]*[MAC4]*[MAC5]*[MAC6]##` | Device returns MAC address |

These records establish a concrete Nurse Call service/diagnostic surface even though `OPEN.db` does not provide the ordinary Nurse Call functional command vocabulary.

### Namespaces represented only by `EN_SYSTEM`

Section ID: `ownkb:section:d000023:s000011`

Provenance cues: `database`, `evidence`

For `WHO 0`, `3`, `5`, `6`, `7`, `9`, `10`, `11`, `12`, `14`, `15`, `16`, `17`, `19`, `22`, `24`, `25`, `26`, and `99`, `OPEN.db` supplies a functional system identity but no direct `AS_OPEN_SYSTEM` â†’ `EN_OPEN` operation association. This is still useful evidence: it confirms the namespace name used by MyHOME_Suite and, in some cases, an interface variant or diagnostic-family assignment. It does **not** establish undocumented `WHAT`, `WHERE`, or `DIMENSION` values.

Notable additional rows are `Interface AI L3` under `WHO 5`, `Interface Multimedia L2` under `WHO 6`, and `Multimedia System` under `WHO 22` with diagnostic `WHO 1022`. These rows show that the database distinguishes interface/system variants even where it does not provide their functional frame vocabulary.

### Interpretation rule

Section ID: `ownkb:section:d000023:s000012`

Cautions: `not evidence`
Provenance cues: `evidence`, `source`

Use `OPEN.db` evidence at the narrowest level it actually establishes:

- `EN_SYSTEM` â†’ namespace/system identity and diagnostic-family association.
- `AS_SYSTEM_ADDRESS_RULE` + `EN_ADDRESS_RULE` â†’ address grammar used by MyHOME_Suite for that system.
- `AS_OPEN_SYSTEM` + `EN_OPEN` â†’ concrete frame template associated with that system.
- `AS_OPEN_PARAM` + `EN_OPEN_PARAM` â†’ parameter layout and constraints for a concrete operation.
- `AS_OPEN_SEQUENCE`, `EN_SEQUENCE`, and timeout tables â†’ workflow ordering and state-machine behavior.

Absence of an `EN_OPEN` association is not evidence that a functional command does not exist. Conversely, a generic parameterized `EN_OPEN` template is not evidence for a particular semantic value until its parameters or another source establish that value.

# Document: ownkb:document:d000024

Source path: `functional/source-coverage.md`
Namespace context: `contextual`
Area: `functional`

## Functional Source Coverage

Section ID: `ownkb:section:d000024:s000001`

Applicability cues: `firmware`, `gateway`, `version`
Cautions: `must not`
Provenance cues: `evidence`, `specification`

The functional reference combines several evidence classes. They answer different questions and must not be treated as interchangeable.

| Evidence class | Establishes | Does not establish by itself |
| --- | --- | --- |
| Public `WHO` specification | Published wire grammar, values, ranges, and examples for that namespace | Device-specific support or later implementation extensions |
| `OWN_Intro_ENG.pdf` | Common syntax, sessions, and the contemporary namespace summary | Complete semantics for every listed `WHO` |
| `OPEN.db` | MyHOME Suite namespace identity, diagnostic-family mapping, address rules, and associated management templates | Complete ordinary functional vocabulary |
| ScenarioDevices databases | Functional actions exposed by the scenario engine and their concrete frames where present | Every legal command or a universal Device capability |
| `MHCatalogue.db` | Physical Device, firmware, Module, Object, and configuration applicability | A complete functional command registry |
| Observed traffic | Behavior of the captured Device/gateway/software version | Universal behavior outside the observed conditions |

### Public specification coverage

Section ID: `ownkb:section:d000024:s000002`

Applicability cues: `gateway`, `scs`, `version`, `zigbee`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `documentation`, `evidence`, `source`, `specification`

| `WHO` | Public source in the corpus | Coverage consequence |
| --- | --- | --- |
| `0` | `WHO_0.pdf` | Dedicated scenario-module grammar |
| `1` | `WHO_1.pdf` | Dedicated Lighting grammar |
| `2` | `WHO_2.pdf` | Dedicated Automation grammar |
| `3` | `WHO_3.pdf` | Dedicated load-management grammar |
| `4` | `WHO_4.pdf` | Dedicated Temperature Control grammar |
| `5` | `WHO_5.pdf` | Dedicated Alarm grammar |
| `6` | `WHO_6_L4686SDK.pdf` | Product-specific SDK surface; not automatically a complete generic `WHO 6` specification |
| `7` | `WHO_7.pdf` | Dedicated Multimedia grammar |
| `13` | `WHO_13.pdf` | Gateway-management grammar; `OPEN.db` additionally establishes integration-interface use |
| `15`, `25` | `WHO_15-25.pdf` | CEN and CEN+ interaction grammar |
| `16` | `WHO_16.pdf` | Sound-system grammar |
| `17` | `WHO_17.pdf` | Scenario-management grammar |
| `18` | `WHO_18.pdf` | Energy Management grammar |
| `22` | `WHO_22.pdf` | Sound Diffusion / Multimedia grammar |
| `24` | `WHO_24.pdf` | Lighting Management grammar |
| `25` | `WHO_25.pdf` | Dry-contact and IR state functions |

The corpus contains no dedicated public functional specification for `WHO 8`, `9`, `10`, `11`, `12`, `14`, `19`, `23`, `26`, `27`, or `99`. Their pages must therefore distinguish namespace identity and narrow implementation evidence from a complete grammar.

The [ZigBee Interface Specification](../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0, is also relevant to Protocol, Diagnostics, Programming boundaries, and functional `WHO 1`, `2`, `4`, `13`, `18`, and `25`. It describes a particular Legrand serial interface, not a universal replacement for the SCS-oriented references. The [ZigBee Interface](../protocol/zigbee-interface.md) owns cross-cutting transport, addressing, acknowledgement, and applicability. Operation-level ZigBee references are integrated for [Lighting](who-1-lighting/zigbee-variant.md), [Automation](who-2-automation/zigbee-variant.md), [Temperature Control](who-4-temperature-control/zigbee-variant.md), [Network Management](who-13-integration-gateway/zigbee-network-management.md), [Energy Management](who-18-energy-management/zigbee-variant.md), and [Binding](who-25-transversal/zigbee-binding.md). These pages are source-bounded to the version 4.0 specification and do not establish universal product support. The source's publication status also requires the [Source Provenance Qualification](../sources/openwebnet-public/README.md). `WHO 1000 DIMENSION 81` discovery and the sections 5-6 product-inventory flows are reconciled in the [ZigBee Discovery and Inventory Reconciliation](../project/review/zigbee-discovery-inventory-reconciliation.md). The final source-to-documentation audit is recorded in the [ZigBee Final Source Completeness Certification](../project/review/zigbee-final-source-completeness-certification.md). See the [Phase 3 Source-Coverage Audit](../project/review/phase-3-source-coverage.md), [ZigBee Reconciliation Review](../project/review/zigbee-reconciliation.md), [ZigBee Functional Reconciliation](../project/review/zigbee-functional-reconciliation.md), and the Step 2 review for inspection scope, source conflicts, and rejected or unresolved claims.

### Implementation-only enrichment

Section ID: `ownkb:section:d000024:s000003`

Provenance cues: `evidence`

Notable relationships established outside the public functional PDFs include:

- `WHO 14` lock/unlock frames from ScenarioDevices;
- target-dependent ScenarioDevices labeling of `WHO 1 / WHAT 17`;
- MyHOME Suite action templates for `WHO 4 DIMENSION 7`, local control, and fan-coil writes;
- `OPEN.db` management/address models for functional families `1/2`, `4`, `8`, `13`, `18`, `23`, and `27`;
- diagnostic-family assignments such as `1001`, `1004`, `1008`, `1013`, `1018`, `1023`, and `1027`.

These additions should be labelled as implementation evidence. A diagnostic-family association does not copy diagnostic `WHAT` or `DIMENSION` semantics into the functional namespace.

### Absence rules

Section ID: `ownkb:section:d000024:s000004`

Uncertainty: `not established`
Provenance cues: `database`, `evidence`

- No public page means â€œnot established by the current public corpus,â€ not â€œthe function does not exist.â€
- No `AS_OPEN_SYSTEM` association means `OPEN.db` does not supply a concrete operation for that system; it is not proof that the system has no functional frames.
- A generic parameterized template does not establish the meaning of each substituted value.
- A ScenarioDevices row with a null or symbolic `Frame` establishes application capability, not a wire mapping.

See [MyHOME Suite `OPEN.db` Coverage](open-db-coverage.md), [Cross-database functional coverage](cross-database-coverage.md), and [Evidence and Confidence](../reverse-engineering/evidence-and-confidence.md).

# Document: ownkb:document:d000025

Source path: `functional/who-0-scenarios/README.md`
Namespace context: `who:0`
Area: `functional`

## `WHO 0` - Scenarios

Section ID: `ownkb:section:d000025:s000001`

`WHO 0` addresses stored scenarios implemented by scenario modules such as F420 and by the 3456 IR interface. The ordinary functional frame uses the selected scenario number as `WHAT` and the scenario module as `WHERE`. The published protocol also defines an F420-only programming vocabulary for recording, erasing and locking scenario storage.

### `WHAT` reference

Section ID: `ownkb:section:d000025:s000002`

Cautions: `must not`
Provenance cues: `specification`

| `WHAT` | Meaning | Availability |
| --- | --- | --- |
| `1..16` | Activate stored scenario `1..16` | F420 and 3456 |
| `17..20` | Activate stored scenario `17..20` | 3456 |
| `40#X` | Start recording scenario `X` | F420 only; `X=1..16` |
| `41#X` | End recording scenario `X` | F420 only; `X=1..16` |
| `42` | Erase all scenarios | F420 only |
| `42#X` | Erase scenario `X` | F420 only; `X=1..16` |
| `43` | Lock scenario central unit | F420 only |
| `44` | Unlock scenario central unit | F420 only |
| `45` | Scenario central unit unavailable | State/event indication |
| `46` | Scenario central-unit memory full | State/event indication |

The published specification states that F420 stores up to 16 scenarios, while the 3456 IR interface can recall up to 20. The higher scenario numbers therefore must not be assumed valid for F420 merely because they are valid `WHO 0` values.

### Scenario activation

Section ID: `ownkb:section:d000025:s000003`

The activation frame is `*0*N*WHERE##`, where `N` is the stored scenario number supported by the addressed device.

A command connection returns `ACK` when the command has been sent to the bus and `NACK` when it has not. The corresponding functional event is reported with the same `*0*N*WHERE##` form.

The MyHOME_Suite ScenarioDevices capability model also exposes `*0*N*WHERE##` as a scenario action. This confirms that the higher-level scenario engine invokes the same functional `WHO 0` operation; the trigger/condition/action model itself is not part of the `WHO 0` wire grammar.

### `WHERE`

Section ID: `ownkb:section:d000025:s000004`

The published point-to-point range is scenario control panels/modules `01..99`.

| Form | Meaning |
| --- | --- |
| `01..99` | Scenario module point to point |
| `01..99#4#I` | Scenario module on local bus through interface `I` |

The local-bus form uses the level-4 interface parameter. It is part of the address and must be preserved when routing the command; it is not a parameter of the selected scenario.

### F420 programming connection

Section ID: `ownkb:section:d000025:s000005`

The F420 recording/erase/lock operations use the commands/actions connection selected by `*99*9##` before the `WHO 0` programming frames are exchanged. These operations alter scenario storage and must be distinguished from scenario activation. The introduction separately defines `*99*0##` for programmed-scenario traffic; it is not the selector printed in these `WHO 0` command flows.

The 3456 IR interface does not support the F420 programming operations described below.

### Start recording - `WHAT 40#X`

Section ID: `ownkb:section:d000025:s000006`

`*0*40#X*WHERE##` starts recording scenario `X`, with `X=1..16` for F420. A successful command connection returns `ACK`; failure returns `NACK`. The operation is also visible on an event connection as a `WHO 0` programming event.

After recording starts, the functional commands to be stored in the scenario are issued through their respective `WHO` namespaces. `WHO 0` identifies the recording lifecycle; it does not encapsulate the recorded Lighting, Automation, or other functional frames.

### End recording - `WHAT 41#X`

Section ID: `ownkb:section:d000025:s000007`

`*0*41#X*WHERE##` ends recording of scenario `X`. The selected scenario number and scenario-module `WHERE` must correspond to the recording session being closed.

The published document contains a typographical irregularity in one event-frame rendering around this operation. The semantic operation remains `WHAT 41#X`: end programming/recording of the selected scenario.

### Erase operations - `WHAT 42`

Section ID: `ownkb:section:d000025:s000008`

`*0*42*WHERE##` erases all stored scenarios from the addressed F420.

`*0*42#X*WHERE##` erases only scenario `X`, with `X=1..16`.

The parameterized and unparameterized forms are distinct operations. Implementations should therefore parse `WHAT` together with its `#` parameter rather than normalize both to a bare numeric `42`.

### Lock and unlock - `WHAT 43` / `44`

Section ID: `ownkb:section:d000025:s000009`

`*0*43*WHERE##` locks the addressed scenario central unit; `*0*44*WHERE##` unlocks it. These are F420 management operations and use the same scenario-module `WHERE` grammar as recording and erasure.

The `WHAT` table also defines `45` for an unavailable scenario central unit and `46` for scenario-memory-full indication. They describe central-unit state rather than a stored scenario number.

### Event model

Section ID: `ownkb:section:d000025:s000010`

An event connection can report scenario activation and the F420 programming lifecycle. Published event forms include activation, start recording, end recording, erase-all and erase-single-scenario events.

A receiver should therefore distinguish three categories inside `WHO 0`:

| Category | `WHAT` |
| --- | --- |
| Stored-scenario invocation | `1..20` according to device capability |
| Scenario-storage programming | `40#X`, `41#X`, `42`, `42#X`, `43`, `44` |
| Scenario-module state | `45`, `46` |

### Relationship to `WHO 17`

Section ID: `ownkb:section:d000025:s000011`

Applicability cues: `gateway`
Cautions: `must not`

`WHO 0` operates scenario modules and stored scenario memories. [`WHO 17`](../who-17-scenario-management/) addresses scenario execution on scenario-programmer/gateway devices using Start, Stop, Enable and Disable operations. The two namespaces are related functionally but have different `WHAT` and `WHERE` models and must not be merged.

See the [functional overview](../) for navigation by `WHO` and by function, [Scenario Engine](../../scenario-engine/) for the MyHOME_Suite trigger/condition/action capability model, and [Protocol](../../protocol/) for common frame/session syntax.

# Document: ownkb:document:d000026

Source path: `functional/who-1-lighting/README.md`
Namespace context: `who:1`
Area: `functional`

## `WHO 1` - Lighting

Section ID: `ownkb:section:d000026:s000001`

Applicability cues: `scs`, `zigbee`
Cautions: `do not`
Uncertainty: `may`
Provenance cues: `catalogue`, `specification`

`WHO 1` defines the OpenWebNet Lighting system. It covers switching, discrete and fine-grained dimming, timed and blinking operation, status reporting, transition speed, temporization, and lamp operating-time information.

The published Lighting specification defines the functional command and `DIMENSION` model. The MyHOME_Suite data structures complement it with implemented address rules and functional command templates. Lighting Objects represented by the MyHOME_Suite catalogue may be command Objects, actuator Objects, dimmer Objects, or functions embedded in combined Devices; the functional `WHO 1` namespace describes their Lighting traffic rather than their physical Device class.

The supplied [ZigBee Interface](../../protocol/zigbee-interface.md) also exposes `WHO 1`, but with a different transport, `WHERE` grammar, documented command set, event surface, and `DIMENSION 1` semantics. See the [ZigBee Lighting Variant](zigbee-variant.md). SCS forms do not establish ZigBee-backed applicability merely because the namespace number is shared.

### Reference

Section ID: `ownkb:section:d000026:s000002`

Applicability cues: `zigbee`
Provenance cues: `evidence`

| Subject | Page |
| --- | --- |
| Commands, states and timed operations | [`WHAT` Reference](what.md) |
| `WHERE` forms and address scopes | [Addressing](addressing.md) |
| Level, speed, temporization and operating-time `DIMENSION` operations | [`DIMENSION` Reference](dimensions.md) |
| ZigBee-specific Lighting semantics and evidence limits | [ZigBee Lighting Variant](zigbee-variant.md) |

### Functional model

Section ID: `ownkb:section:d000026:s000003`

Applicability cues: `scs`

Ordinary command/status frames use `*1*WHAT*WHERE##`; status requests use `*#1*WHERE##`. `DIMENSION` operations use the common frame classes defined in [`DIMENSION`](../../protocol/dimensions.md).

`WHAT 0..31` provide the ordinary Lighting vocabulary, including ON/OFF, discrete dimmer levels, timed ON, blinking and relative dimming. Fine level control and other structured values are carried by Lighting-specific `DIMENSION` operations.

Lighting uses the SCS `A`/`PL` address family, with point-to-point, environment, group, general and advanced forms. Address syntax and event expansion are described in [Addressing](addressing.md).

Lighting Management is a distinct protocol namespace under [`WHO 24`](../who-24-lighting-management/). Diagnostic discovery and configuration of Lighting-capable Devices belong to the diagnostic protocol rather than to functional `WHO 1` traffic.

For the Device â†’ Module â†’ Object â†’ Configuration model, see [Device Model](../../device-model/).

# Document: ownkb:document:d000027

Source path: `functional/who-1-lighting/addressing.md`
Namespace context: `who:1`
Area: `functional`

## Addressing

Section ID: `ownkb:section:d000027:s000001`

Applicability cues: `scs`

`WHO 1` uses the SCS Lighting `A`/`PL` addressing model. `WHERE` can select an individual light point, an environment, a group, the complete Lighting system, or a point reached through an interface/extended address form.

The same broad address family is shared with Automation, but `WHERE` remains scoped to the selected `WHO`: a Lighting address identifies Lighting Objects and must be interpreted using the Lighting operation in which it occurs.

### Address scopes

Section ID: `ownkb:section:d000027:s000002`

| Scope | `WHERE` form | Role |
| --- | --- | --- |
| General | `0` | Addresses the complete Lighting system |
| Environment / area | `A` | Addresses the Lighting Objects belonging to an environment |
| Point to point | `APL` | Addresses an individual `A`/`PL` light point |
| Group | `#GR` | Addresses the Lighting Objects belonging to a group |
| Riser / level 3 | `0#3`, `A#3`, `#G#3`, or `APL#3` | Routes the corresponding scope on the riser/backbone level |
| Local bus / level 4 | `0#4#Int`, `A#4#Int`, `#G#4#Int`, or `APL#4#Int` | Routes the corresponding scope through local-bus interface `Int` |

The canonical [`A`/`PL` grammar](../../protocol/addressing.md#lighting-and-automation-apl-grammar) defines the shared base ranges and the less-common forms that differ between Lighting and Automation. Advanced forms are modeled as a base target plus a routing qualifier: `#3` for the riser/backbone level or `#4#Int` for a local bus. The published `WHO 1` material establishes these qualifiers for General, Area, Group, and point targets. `Int` is the routing-interface address; for Lighting it is `01..09` or `11..15`. Leading zeroes and `#` markers are significant; a `WHERE` must be parsed as protocol syntax before numeric conversion.

### MyHOME_Suite address rules

Section ID: `ownkb:section:d000027:s000003`

Provenance cues: `database`

The MyHOME_Suite `OPEN.db` definitions distinguish Lighting/Automation address rules rather than representing `WHERE` as one untyped integer. Relevant rules include point-to-point `[A][PL]`, environment `[A]`, and advanced forms. This confirms that the syntactic shape of the address participates in its meaning.

The same database contains system-to-address-rule associations, so an encoder or parser should select the rule from the system/operation context instead of inferring the address class solely from the number of digits.

### Scope and event reporting

Section ID: `ownkb:section:d000027:s000004`

Commands sent to a collective scope can result in state/event reporting for the individual Lighting Objects affected by the operation. Clients should therefore be prepared for a general, environment, or group command to be followed by point-specific state traffic rather than expecting only a frame that repeats the original collective `WHERE`.

This behavior is especially relevant when maintaining a live Lighting state model: the command target describes the requested scope, while subsequent events describe the resulting state of Objects within that scope.

See [`WHAT` Reference](what.md) for Lighting commands, [`DIMENSION` Reference](dimensions.md) for structured Lighting values, and [Addressing](../../protocol/addressing.md) for the common system-scoped addressing model.

# Document: ownkb:document:d000028

Source path: `functional/who-1-lighting/dimensions.md`
Namespace context: `who:1`
Area: `functional`

## `DIMENSION` Reference

Section ID: `ownkb:section:d000028:s000001`

Provenance cues: `source`

`WHO 1` uses `DIMENSION` operations for Lighting values that are more structured or precise than ordinary `WHAT` values.

| `DIMENSION` | Meaning | Published operations |
| --- | --- | --- |
| `1` | Level and transition speed | Read/report/write |
| `2` | Temporization | Read/report/write |
| `3` | Return only Lighting Objects that are ON | Read |
| `4` | 100-level dimmer status with ON/OFF speed | Identifier listed; no detailed flow in the source |
| `8` | Accumulated lamp working time | Read/report |
| `9` | Maximum lamp working time | Read/report/write |

### Value fields

Section ID: `ownkb:section:d000028:s000002`

Cautions: `must not`

| Field | Published range and encoding |
| --- | --- |
| `LEVEL100` | `100` = OFF; `101..199` = 1%..99%; `200` = maximum |
| `SPEED` | `0` = last speed; `1..254` = explicit speed; `255` = default speed |
| `HOURS` | `0..255` |
| `MINUTES` | `0..59` |
| `SECONDS` | `0..59` |
| `WORKING_TIME` | `1..100000` hours |

`LEVEL100` is offset by 100. It is not a literal percentage field and must not be decoded as `100%..200%`.

### `DIMENSION 1` - level and speed

Section ID: `ownkb:section:d000028:s000003`

Provenance cues: `documentation`, `source`

Write:

```text
*#1*WHERE*#1*LEVEL100*SPEED##
```

Request and response/report:

```text
*#1*WHERE*1##
*#1*WHERE*1*LEVEL100*SPEED##
```

The PDF prints one write example without the `*` before `#1`; this conflicts with its common write grammar and the otherwise consistent frame family. This documentation uses the structurally consistent form above and records the source inconsistency rather than treating the missing separator as a new syntax.

### `DIMENSION 2` - temporization

Section ID: `ownkb:section:d000028:s000004`

```text
*#1*WHERE*#2*HOURS*MINUTES*SECONDS##
*#1*WHERE*2##
*#1*WHERE*2*HOURS*MINUTES*SECONDS##
```

This explicit duration is distinct from fixed-duration `WHAT 11..18` commands. The published event flow after a write reports ordinary Lighting state and, for a dimmer, a fine-grained level/speed report.

### `DIMENSION 3` - only Objects that are ON

Section ID: `ownkb:section:d000028:s000005`

Applicability cues: `only for`

`*#1*WHERE*3##` is a filtered request. The server returns ordinary Lighting status frames only for addressed lights or dimmers that are ON, then terminates the sequence with `ACK`.

This is not a scalar property response and should be modeled as a query producing zero or more result frames.

### `DIMENSION 4` - 100-level status

Section ID: `ownkb:section:d000028:s000006`

Cautions: `do not`

The canonical `DIMENSION` table names `4` as 100-level dimmer status with ON/OFF speed, but the document does not provide a detailed request/write flow for it. Do not invent its payload from `DIMENSION 1` merely because their descriptions overlap.

### `DIMENSION 8` - working time

Section ID: `ownkb:section:d000028:s000007`

```text
*#1*WHERE*8##
*#1*WHERE*8*WORKING_TIME##
```

The response can also appear on the event session.

### `DIMENSION 9` - maximum working time

Section ID: `ownkb:section:d000028:s000008`

```text
*#1*WHERE*#9*WORKING_TIME##
*#1*WHERE*9##
*#1*WHERE*9*WORKING_TIME##
```

The value is expressed in hours. Read and write support still depends on the target capability.

### Capability boundary

Section ID: `ownkb:section:d000028:s000009`

Applicability cues: `firmware`
Provenance cues: `catalogue`

The global `WHO 1` vocabulary does not imply that every Lighting Object implements every operation. Validate Device/firmware/Object applicability through the catalogue model where available.

### Evidence basis

Section ID: `ownkb:section:d000028:s000010`

Provenance cues: `specification`

Identifiers, ranges, direction, and frame flows come from [`WHO 1` specification](../../sources/openwebnet-public/pdf/WHO_1.pdf). MyHOME Suite ScenarioDevices corroborates functional level-control use but does not replace the published field encodings.

See [`WHAT` Reference](what.md), [Addressing](addressing.md), and the common [`DIMENSION` model](../../protocol/dimensions.md).

# Document: ownkb:document:d000029

Source path: `functional/who-1-lighting/what.md`
Namespace context: `who:1`
Area: `functional`

## `WHAT` Reference

Section ID: `ownkb:section:d000029:s000001`

`WHAT` in `WHO 1` expresses Lighting commands and states. Ordinary frames use `*1*WHAT*WHERE##`; status requests use `*#1*WHERE##`.

### Switching and levels

Section ID: `ownkb:section:d000029:s000002`

Cautions: `must not`

| `WHAT` | Meaning |
| --- | --- |
| `0` | OFF |
| `1` | ON |
| `2..10` | `20%..100%` in ten-percent steps |
| `30` | Increase one level |
| `31` | Decrease one level |

The parameterized forms `0#SPEED` and `1#SPEED` switch OFF or ON using the requested transition speed. `30#LEVELS#SPEED` and `31#LEVELS#SPEED` change several levels at the specified speed. These forms must not be reduced to their leading numeric `WHAT`.

For the published speed field, `0` means the last speed used, `1..254` are explicit speeds, and `255` selects the default speed.

### Timed operations

Section ID: `ownkb:section:d000029:s000003`

Uncertainty: `unresolved`

| `WHAT` | ON duration |
| --- | --- |
| `11` | 1 minute |
| `12` | 2 minutes |
| `13` | 3 minutes |
| `14` | 4 minutes |
| `15` | 5 minutes |
| `16` | 15 minutes |
| `17` | Unresolved duration: summary table says 30 seconds; section 3.1.9 says 30 minutes |
| `18` | 0.5 seconds |

Timed commands switch the target ON for the encoded duration. Their event sequence can include immediate ON followed by a later status report; clients should not treat the initiating `WHAT` as the final persistent state.

#### Target-dependent MyHOME Suite label for `WHAT 17`

Section ID: `ownkb:section:d000029:s000004`

Uncertainty: `may`, `unresolved`
Provenance cues: `source`

ScenarioDevices contains `miniScenarioSuite.automation.actionAutomationDoorLock.on` with frame `*1*17*WHERE##`. This establishes a stored door-lock-specific capability label, not the duration or observed emission of the command. It does not resolve the conflict between the `WHO 1` summary table (30 seconds) and section 3.1.9 (30 minutes).

A decoder should retain timed ON with unresolved duration for `WHAT 17`; an Object-aware application may additionally present the contextual label. Establish the duration on the applicable target before relying on either source value.

### Blinking operations

Section ID: `ownkb:section:d000029:s000005`

| `WHAT` | Blink period |
| --- | --- |
| `20..29` | `0.5..5` seconds in 0.5-second increments |

### Command translation - `WHAT 1000`

Section ID: `ownkb:section:d000029:s000006`

Cautions: `do not`
Provenance cues: `specification`

The published Lighting specification defines `1000#INNER_WHAT` as a command-translation wrapper:

```text
*1*1000#INNER_WHAT*WHERE##
```

Section 3.1.21 says the command is valid for dimmers too and shows the same wrapper on the event session. This does not establish a dimmer-only restriction or support on every Lighting target. `INNER_WHAT` is a value from the Lighting `WHAT` table. Preserve both the wrapper and inner operation; do not normalize it silently to `INNER_WHAT` because the wrapper itself is observable protocol information.

### ScenarioDevices coverage

Section ID: `ownkb:section:d000029:s000007`

Cautions: `do not`

ScenarioDevices stores ordinary OFF/ON templates for Lighting Objects and for controlled-socket and fan action Objects. It also contains timed-light and 100-level dimmer actions. Several capability types therefore share a frame template; these rows do not establish which template MyHOME Suite emits for an installed Physical Device.

### Evidence basis

Section ID: `ownkb:section:d000029:s000008`

Provenance cues: `database`, `specification`

The complete value table, parameterized switching/step forms, speed values, timed and blinking operations, and `WHAT 1000` wrapper come from [`WHO 1` specification](../../sources/openwebnet-public/pdf/WHO_1.pdf). The door-lock label and scenario coverage come from the ScenarioDevices databases and are implementation-specific enrichment.

See [`DIMENSION` Reference](dimensions.md), [Addressing](addressing.md), and [Cross-database functional coverage](../cross-database-coverage.md).

# Document: ownkb:document:d000030

Source path: `functional/who-1-lighting/zigbee-variant.md`
Namespace context: `who:1`
Area: `functional`

## ZigBee Variant

Section ID: `ownkb:section:d000030:s000001`

Applicability cues: `revision`, `version`, `zigbee`
Uncertainty: `unresolved`
Provenance cues: `evidence`, `source`, `specification`

The ZigBee OpenWebNet version 4.0 specification defines a `WHO 1` Lighting variant for the Legrand serial ZigBee interface. It reuses several familiar Lighting `WHAT` values but uses the [ZigBee product-and-Unit `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing), a smaller documented command set, ZigBee-specific event values, and a variant-specific `DIMENSION 1` payload.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. Its Confidential footer and unresolved public-release provenance remain recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The material below is **specification evidence for this interface revision**, not a tested-interoperability claim or a universal `WHO 1` definition.

### Command surface

Section ID: `ownkb:section:d000030:s000002`

Applicability cues: `scs`, `version`, `zigbee`
Cautions: `not evidence`
Provenance cues: `evidence`, `source`, `specification`

The ZigBee source defines the following `WHAT` values:

| `WHAT` | ZigBee specification meaning | Relationship to the SCS-oriented reference |
| --- | --- | --- |
| `0` | OFF | Same command meaning; different `WHERE` and transport |
| `0#SPEED` | OFF at requested speed | Same command family; different `WHERE` and transport |
| `1` | ON | Same command meaning; different `WHERE` and transport |
| `1#SPEED` | ON at requested speed; the source says this drives a dimmer to 100% | Same command family; different `WHERE` and transport |
| `2..10` | `20%..100%` | Same discrete levels; different `WHERE` and transport |
| `11..16` | Timed ON from 1 minute through 15 minutes | Same timed-value meanings in the current reference |
| `17` | Timed ON for 30 seconds | Variant source is explicit; it does not resolve the separate SCS source conflict |
| `18` | Timed ON for 0.5 seconds | Same timed-value meaning in the current reference |
| `32` | Toggle | ZigBee-specific extension relative to the current SCS-oriented table |
| `34` | Movement detected | ZigBee-specific event |
| `39` | End of movement detected | ZigBee-specific event |

For `0#SPEED` and `1#SPEED`, the ZigBee source defines `0` as the last speed used, `1..254` as explicit speed values, and `255` as the default speed. It does not state a physical time unit for the explicit values.

The SCS-oriented reference also documents blinking `WHAT 20..29`, relative dimming `WHAT 30..31`, and command translation `WHAT 1000`. Their absence from the ZigBee version 4.0 command table means only that this source does not establish them for this interface. It is not evidence that no ZigBee implementation can support them.

### Command acknowledgement and state reporting

Section ID: `ownkb:section:d000030:s000003`

Applicability cues: `scs`, `zigbee`
Provenance cues: `source`

Ordinary ZigBee Lighting commands use the interface-specific acknowledgement model described in [ZigBee acknowledgement behavior](../../protocol/zigbee-interface.md#acknowledgement-behavior). `ACK` means the command was sent according to the source; `NACK` means it was not, and BUSY uses the documented BUSY/NACK retry sequence.

When Supervisor mode is enabled through ZigBee `WHO 13`, the command definitions show server-originated state frames after OFF, ON, level, and timed operations. For dimmers, the detailed OFF and timed-OFF flows can show an additional OFF report when the dimmer reaches its 0% level, while ON at a requested speed reports the 100% state as `WHAT 10`. These are interface-specific event sequences and should not be transferred to SCS sessions by analogy.

Toggle is special in the source. It states that the product replies with its resulting state even when Supervisor mode is disabled and that Supervisor mode can therefore produce duplicate state replies. The switch case returns state `0` or `1`. The dimmer cases return `0` when OFF or `2..10` when ON according to the last dimming level.

Timed-ON examples return an ON or current-level state first and a later OFF state after the selected interval. The detailed `WHAT 11` example uses one minute; the table defines the other timing values.

### Movement-detector events

Section ID: `ownkb:section:d000030:s000004`

Applicability cues: `zigbee`
Provenance cues: `source`

The source defines server-originated `WHAT 34` for movement detected and `WHAT 39` for end of movement detected. It says the detector must previously have completed a source-named "PnL" procedure with the OpenWebNet interface and points to the `WHO 25` use cases.

The movement-detector use case also shows `WHAT 32` Toggle at half of the detector's configured time while people continue to be detected. The source still labels `WHAT 32` as Toggle; the use case does not establish a separate occupancy-state meaning for that value.

The encyclopedia records only the OpenWebNet-visible dependency and events. It does not infer the underlying ZigBee commissioning or radio procedure from the term "PnL". See [ZigBee Binding](../who-25-transversal/zigbee-binding.md) for the OpenWebNet-visible `WHO 25` lifecycle.

### `DIMENSION 1` - level and speed

Section ID: `ownkb:section:d000030:s000005`

Applicability cues: `scs`, `zigbee`
Provenance cues: `source`

The ZigBee variant documents only `DIMENSION 1` in its Lighting `DIMENSION` table.

Read:

`*#1*WHERE#9*1##`

Response:

`*#1*WHERE#9*1*LEVEL*SPEED##`

Write:

`*#1*WHERE#9*#1*LEVEL*SPEED##`

The source defines `LEVEL` as `101..200`, expressed as the Lighting intensity percentage encoding. Unlike the SCS-oriented `DIMENSION 1` reference, this ZigBee section does not define `100` as OFF.

The source defines this `DIMENSION 1` `SPEED` field as `0..255`, with `0` described as immediate and `255` as the maximum delay. That wording materially differs from the SCS-oriented `DIMENSION 1` speed semantics, where `0` and `255` have different labels. The two variants must therefore not share one speed-value interpretation merely because the `DIMENSION` number is the same.

The ZigBee source does not specify a time unit for the `DIMENSION 1` speed field.

### Status request

Section ID: `ownkb:section:d000030:s000006`

Applicability cues: `scs`, `zigbee`
Provenance cues: `source`

The ZigBee Lighting state request is:

`*#1*WHERE#9##`

The response is an ordinary `WHO 1` state frame followed by `ACK`. The source defines switch state as `0` or `1`, and dimmer state as `0` or a discrete level `2..10`.

This request form belongs to the ZigBee address family. It is not an SCS `A`/`PL` request with a suffix added mechanically.

### Evidence limits

Section ID: `ownkb:section:d000030:s000007`

Applicability cues: `firmware`, `revision`, `scs`, `version`, `zigbee`
Provenance cues: `source`

The ZigBee version 4.0 Lighting section documents `DIMENSION 1` only. It does not establish the SCS-oriented `DIMENSION 2`, `3`, `4`, `8`, or `9` operations for this interface.

The source establishes the command/event semantics above for the described interface revision, but not support by every ZigBee Lighting product or Firmware.

See [`WHAT` Reference](what.md) and [`DIMENSION` Reference](dimensions.md) for the SCS-oriented Lighting model, and [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for common ZigBee transport, addressing, and acknowledgement rules.

# Document: ownkb:document:d000031

Source path: `functional/who-10-navigation/README.md`
Namespace context: `who:10`
Area: `functional`

## `WHO 10` - Navigation Commands

Section ID: `ownkb:section:d000031:s000001`

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 10` as Navigation commands.

### Corpus status

Section ID: `ownkb:section:d000031:s000002`

The namespace is established directly by the implementation model, but the integrated corpus does not yet establish a complete public or implementation-level `WHAT`, `WHERE`, and `DIMENSION` vocabulary.

### Interpretation rule

Section ID: `ownkb:section:d000031:s000003`

Cautions: `must not`
Uncertainty: `unknown`

Navigation is treated as its own protocol namespace. Numeric operations must not be borrowed from multimedia track navigation, CEN button events, or user-interface assumptions merely because those domains also contain directional concepts.

A generic decoder should preserve unknown `WHO 10` frames losslessly and expose their fields as raw values until command semantics are supported by MyHOME_Suite data or captures. This allows future refinement without having to undo speculative labels.

No dedicated `WHO 10` PDF is present in the canonical public corpus used by this repository.

# Document: ownkb:document:d000032

Source path: `functional/who-11-energy-distribution/README.md`
Namespace context: `who:11`
Area: `functional`

## `WHO 11` - Energy Distribution

Section ID: `ownkb:section:d000032:s000001`

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 11` as Energy distribution.

### Protocol boundary

Section ID: `ownkb:section:d000032:s000002`

Cautions: `must not`
Provenance cues: `evidence`

`WHO 11` is distinct from both [`WHO 3`](../who-3-load-management/) Load Management and [`WHO 18`](../who-18-energy-management/) Energy Management. These three namespaces occupy related electrical-energy domains but represent separate protocol systems.

`WHO 18` measurements such as active power, totalizers, actuator information and historical energy must not be exposed under `WHO 11` unless direct evidence establishes an equivalent operation. Likewise, `WHO 3` load-management states are not `WHO 11` values.

### Corpus status

Section ID: `ownkb:section:d000032:s000003`

Uncertainty: `unknown`
Provenance cues: `evidence`, `specification`

The implementation data establishes the Energy distribution namespace but does not yet provide a complete supported `WHAT`, `WHERE`, or `DIMENSION` table. The canonical public PDF set used by this repository does not contain a dedicated `WHO 11` functional specification.

Implementations should therefore recognize the namespace, preserve unknown frames losslessly, and add field semantics only from direct implementation or wire evidence.

# Document: ownkb:document:d000033

Source path: `functional/who-12-messages/README.md`
Namespace context: `who:12`
Area: `functional`

## `WHO 12` - Messages

Section ID: `ownkb:section:d000033:s000001`

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 12` as Messages.

### Corpus status

Section ID: `ownkb:section:d000033:s000002`

Provenance cues: `evidence`

The functional namespace is directly established, but the currently integrated evidence does not support a complete authoritative `WHAT`, `WHERE`, or `DIMENSION` reference. No dedicated `WHO 12` PDF is present in the canonical public corpus used by this repository.

### Interpretation rule

Section ID: `ownkb:section:d000033:s000003`

Uncertainty: `unknown`

The generic name â€œMessagesâ€ is not sufficient to infer payload encoding, recipient addressing, text representation, notification type, or acknowledgement behavior. Those semantics remain unknown until supported by implementation definitions or captured traffic.

OpenWebNet parsers should still recognize `WHO 12` and retain its fields losslessly. This permits later decoding while keeping unknown protocol values distinct from generic `ACK`/`NACK` frames and from application messages transported outside this `WHO` namespace.

Common frame/session concepts remain documented under [Protocol](../../protocol/).

# Document: ownkb:document:d000034

Source path: `functional/who-13-integration-gateway/README.md`
Namespace context: `who:13`
Area: `functional`

## `WHO 13` - Integration and Gateway Functions

Section ID: `ownkb:section:d000034:s000001`

Applicability cues: `gateway`, `scs`, `tcp`, `version`, `zigbee`
Cautions: `do not`
Provenance cues: `database`, `source`

`WHO 13` covers Integration / Gateway functions. The namespace has three source-scoped roles that must remain distinct:

1. the published SCS/TCP OpenWebNet External interface device API, which exposes gateway-local clock, network identity, model, software-version, and uptime information;
2. the MyHOME_Suite `OPEN.db` Integration Functions model, which associates `WHO 13` with F422 interface modes and diagnostic family `WHO 1013`;
3. the ZigBee OpenWebNet interface, which defines a separate `WHO 13` network-management, product-database, and product-property surface.

These roles share the numeric namespace but do not automatically share `WHERE` grammar, `WHAT` values, `DIMENSION` sets, transport behavior, or Device support.

### Reference

Section ID: `ownkb:section:d000034:s000002`

Applicability cues: `gateway`, `scs`, `tcp`, `zigbee`
Provenance cues: `evidence`

| Subject | Page |
| --- | --- |
| SCS/TCP gateway capabilities and frame model | [Gateway Capabilities](capabilities.md) |
| SCS/TCP `DIMENSION` values, payloads, and access modes | [`DIMENSION` Reference](dimensions.md) |
| ZigBee network management, product inventory, and properties | [ZigBee Network Management](zigbee-network-management.md) |
| Cross-namespace MyHOME_Suite `OPEN.db` evidence | [MyHOME_Suite `OPEN.db` Coverage](../open-db-coverage.md) |

### Published SCS/TCP gateway capability groups

Section ID: `ownkb:section:d000034:s000003`

Applicability cues: `firmware`, `gateway`, `version`
Uncertainty: `unknown`
Provenance cues: `evidence`, `source`

| Capability | `DIMENSION` | Access |
| --- | --- | --- |
| Time and time zone | `0` | Read / write |
| Date | `1` | Read / write |
| IP address | `10` | Read |
| Network mask | `11` | Read |
| MAC address | `12` | Read |
| Gateway model / device type | `15` | Read |
| OpenWebNet server firmware version | `16` | Read |
| Uptime | `19` | Read |
| Combined date and time | `22` | Read / write |
| Kernel version | `23` | Read |
| Distribution version | `24` | Read |

This published surface supports gateway discovery and inventory, network identification, software/firmware reporting, clock synchronisation, and operational-health information such as uptime. It is not an exhaustive ceiling for later gateway implementations: first-hand F454 and MH202 observations establish an additional readable `DIMENSION 40`, whose semantics remain unknown. See the [`DIMENSION` Reference](dimensions.md#observed-implementation-extension-dimension-40).

For gateway model identification, `DIMENSION 15` should be treated as one evidence source rather than as a guaranteed unique model discriminator. Later gateways can report values not covered by the historical model table, and distinct observed gateway models can share the same returned value. Where supported, diagnostic `WHO 1013 DIMENSION 1` provides the next identification layer.

### Integration-interface model in `OPEN.db`

Section ID: `ownkb:section:d000034:s000004`

Applicability cues: `gateway`
Provenance cues: `database`

The MyHOME_Suite `EN_SYSTEM` row `id_system = 26` names the system **Integration Functions**, assigns functional `WHO 13`, diagnostic `WHO 1013`, and marks it as managed.

`OPEN.db` does not associate ordinary `EN_OPEN` command templates directly with this system, so the database does not provide an additional functional `WHAT` or `DIMENSION` table. It does, however, associate two concrete `EN_ADDRESS_RULE` definitions with the system:

| F422 interface mode | Virtual `WHERE` form | Advanced form |
| --- | --- | --- |
| Burglar alarm interface | `[I4]` | `[I4]` |
| Galvanic separation / New physical separation | `[I4]` | `[I4]` |

This is significant: the implementation model treats `WHO 13` as more than a set of IP-gateway information registers. It is also the Integration Functions namespace used by MyHOME_Suite for F422 interface configurations. The database establishes the interface modes and address grammar, but it does not by itself establish additional command semantics for those modes.

### Scope

Section ID: `ownkb:section:d000034:s000005`

Applicability cues: `gateway`, `scs`, `tcp`, `zigbee`
Cautions: `must not`
Provenance cues: `specification`

`WHO 13` must not be conflated with the transport session used to connect to an IP gateway. TCP connection establishment, command/monitor sessions, authentication, HMAC, and generic `ACK` / `NACK` handling are common OpenWebNet transport concerns and are documented under [Protocol](../../protocol/).

It is also distinct from diagnostic `WHO 1013`. The latter is the diagnostic family assigned by MyHOME_Suite to the Integration Functions system; the numeric relationship does not make diagnostic operations part of the functional `WHO 13` vocabulary.

The published SCS/TCP `WHO 13` specification calls this system the **External interface device**. The MyHOME_Suite `OPEN.db` definitions call it **Integration Functions**. The ZigBee specification defines a third, interface-specific management role documented in [ZigBee Network Management](zigbee-network-management.md). These views remain separate where their wire grammars or applicability differ.

# Document: ownkb:document:d000035

Source path: `functional/who-13-integration-gateway/capabilities.md`
Namespace context: `who:13`
Area: `functional`

## Gateway Capabilities

Section ID: `ownkb:section:d000035:s000001`

Applicability cues: `gateway`, `scs`, `tcp`, `zigbee`

This page describes the published SCS/TCP external-interface `WHO 13` property surface and its established implementation limits. In the published interface model the target is the gateway itself and the property frames use an empty `WHERE` field. Later gateway implementations can expose additional properties not present in the historical registry; those are documented separately and never back-filled with inferred semantics.

The ZigBee OpenWebNet interface defines a different `WHO 13` management surface with additional `WHAT` values, a different `DIMENSION` set, and both empty and product-addressed `WHERE` forms. See [ZigBee Network Management](zigbee-network-management.md). Neither variant should be used to fill gaps in the other by numeric analogy.

### Functional model

Section ID: `ownkb:section:d000035:s000002`

Applicability cues: `firmware`, `gateway`

The published registry provides five main capability groups.

| Group | Operations |
| --- | --- |
| Clock and calendar | Read/write time, read/write date, read/write combined date and time, including time-zone information |
| Network identity | Read IPv4 address, network mask, and MAC address |
| Hardware/product identity | Read gateway model / device type |
| Software identity | Read OpenWebNet firmware, kernel, and distribution versions |
| Runtime state | Read elapsed uptime since the last start-up |

The detailed payload definitions are documented in [`DIMENSION` Reference](dimensions.md).

### Command-session behavior

Section ID: `ownkb:section:d000035:s000003`

Applicability cues: `gateway`

A property request is sent in a command session as:

`*#13**DIMENSION##`

The gateway answers with:

`*#13**DIMENSION*VALUE1*...*VALUEn##`

and the published examples show an `ACK` after the returned value.

For writable properties, the client sends:

`*#13**#DIMENSION*VALUE1*...*VALUEn##`

and the gateway returns `ACK` when the operation is accepted.

This follows the common OpenWebNet `DIMENSION` read/write distinction, but the available `DIMENSION` numbers and their payload schemas are specific to `WHO 13`.

### Monitor-session behavior

Section ID: `ownkb:section:d000035:s000004`

Applicability cues: `gateway`, `version`
Uncertainty: `may`
Provenance cues: `specification`

The published specification also shows the gateway value frames on a monitor session. A client may therefore encounter frames such as time, network identity, model, version, or uptime reports as server-originated monitor traffic rather than only as direct command-session replies.

A decoder should consequently treat a `WHO 13` value frame as a gateway property report independently of which session delivered it. Request/reply correlation belongs to the session layer.

### Clock management

Section ID: `ownkb:section:d000035:s000005`

Applicability cues: `gateway`
Provenance cues: `database`, `specification`

Three related properties exist:

- `DIMENSION 0` - time plus time zone;
- `DIMENSION 1` - day of week and calendar date;
- `DIMENSION 22` - complete date and time in one payload.

All three are writable. `DIMENSION 22` carries time and calendar components in one frame. This avoids two separate submissions, but the specification does not establish transactional atomicity inside the gateway.

The protocol's time-zone encoding is an hour-offset representation rather than a named time-zone database identifier. Implementations should not infer daylight-saving rules from it; it carries the offset represented by the gateway.

### Network identity

Section ID: `ownkb:section:d000035:s000006`

Applicability cues: `gateway`

`DIMENSION 10`, `11`, and `12` report the gateway's IP address, netmask, and MAC address respectively.

The payload is structured numerically: IPv4 and netmask values are four decimal octets, while the MAC address is six decimal octets. These fields should be parsed as component tuples rather than as arbitrary strings.

The published `WHO 13` interface exposes these properties as read-only. It therefore supports network identification, not IP configuration.

### Product identification

Section ID: `ownkb:section:d000035:s000007`

Applicability cues: `gateway`
Cautions: `do not`
Uncertainty: `unknown`
Provenance cues: `specification`

`DIMENSION 15` reports a numeric model identifier. The published table maps values to several historical external-interface products including MHServer, MH200, F452, F452V, MHServer2, and H4684.

This is a gateway model code, not a MyHOME Device Object ID and not the diagnostic object model returned by diagnostic `DIMENSION 1`. Implementations should keep those identifier spaces separate.

Because later gateways exist beyond the models listed in the original specification, an unknown numeric `MODEL` value should be retained as an unknown `WHO 13` model code rather than rejected.

First-hand F454 and MH202 gateway-information captures show that both can report `MODEL = 200`. A returned `DIMENSION 15` value is therefore not sufficient, by itself, to identify a later gateway uniquely. Where supported, continue gateway identification through diagnostic `WHO 1013 DIMENSION 1`; do not collapse the functional model code and diagnostic object-model value into one identifier namespace.

### Software stack identification

Section ID: `ownkb:section:d000035:s000008`

Applicability cues: `firmware`, `gateway`, `version`
Provenance cues: `specification`

Three independent version properties are defined:

| `DIMENSION` | Layer |
| --- | --- |
| `16` | Device/OpenWebNet server firmware |
| `23` | Kernel |
| `24` | Distribution |

Each uses a three-component `V*R*B` payload for version, release, and build in the published specification. Keeping these values separate is important: they describe different layers of the gateway software stack and should not be collapsed into a single firmware string.

Observed implementations can be less complete than the published payload schema. An MH202 has been observed returning an empty `DIMENSION 24` value payload. Consumers should therefore preserve the response as observed rather than manufacturing missing version components.

### Observed extension surface

Section ID: `ownkb:section:d000035:s000009`

Applicability cues: `gateway`, `scs`, `tcp`, `version`, `zigbee`
Uncertainty: `unresolved`

Later SCS/TCP gateway observations include `DIMENSION 40`, which is absent from the published classic registry. Independent F454 and MH202 information requests both returned a two-value response to that property. Its semantics remain unresolved, so it belongs in the [`DIMENSION` Reference](dimensions.md#observed-implementation-extension-dimension-40) as an observed extension rather than in the published capability table.

The ZigBee registry's `DIMENSION 17` hardware-version meaning is variant-specific, and the current canonical classic corpus does not establish a SCS/TCP meaning for `DIMENSION 20`. Numeric reuse across `WHO 13` variants is not a semantic mapping.

### Uptime

Section ID: `ownkb:section:d000035:s000010`

Applicability cues: `gateway`

`DIMENSION 19` reports elapsed days, hours, minutes, and seconds since the last gateway start-up. It provides a simple runtime-health signal and can be used to detect that a gateway has restarted between observations.

The published format is an elapsed-time tuple, not a boot timestamp. Deriving a boot time from it requires combining the value with an independently known current time and therefore belongs to application logic rather than the protocol representation.

### Relationship to transport and diagnostics

Section ID: `ownkb:section:d000035:s000011`

Applicability cues: `gateway`, `tcp`

A gateway performs several roles that must remain separate in an implementation:

| Role | Namespace / layer |
| --- | --- |
| TCP connection and OpenWebNet session establishment | Protocol/session layer |
| Authentication and HMAC | Protocol/session layer |
| Generic `ACK` / `NACK` | Protocol/session layer |
| Gateway-local properties and clock management | Functional `WHO 13` |
| Gateway/device diagnostic operations | Diagnostic families such as `WHO 1013` |
| Functional traffic forwarded to the field bus | The corresponding functional `WHO` (`1`, `2`, `4`, etc.) |

`WHO 13` therefore describes the gateway as a manageable OpenWebNet endpoint; it does not replace the common gateway transport protocol and does not subsume the diagnostic protocol.

# Document: ownkb:document:d000036

Source path: `functional/who-13-integration-gateway/dimensions.md`
Namespace context: `who:13`
Area: `functional`

## `DIMENSION` Reference

Section ID: `ownkb:section:d000036:s000001`

Applicability cues: `firmware`, `gateway`, `scs`, `tcp`, `version`, `zigbee`
Cautions: `must not`
Provenance cues: `evidence`, `specification`

This page records the **published SCS/TCP external-interface `WHO 13` `DIMENSION` registry** and separately scoped implementation observations. The published specification explicitly identifies whether each listed property is readable or writable; its registry must not be treated as proof that later gateway implementations expose no additional `DIMENSION` values.

The ZigBee OpenWebNet interface defines a separate `WHO 13` `DIMENSION` set. Some numeric IDs overlap while others differ, so the two registries must not be merged by number. See [ZigBee Network Management](zigbee-network-management.md#dimension-reference) for the ZigBee variant.

| `DIMENSION` | Property | Access | Payload |
| --- | --- | --- | --- |
| `0` | Time | R/W | `H*M*S*T` |
| `1` | Date | R/W | `W*D*M*Y` |
| `10` | IP address | R | `IP1*IP2*IP3*IP4` |
| `11` | Netmask | R | `MASK1*MASK2*MASK3*MASK4` |
| `12` | MAC address | R | `MAC1*MAC2*MAC3*MAC4*MAC5*MAC6` |
| `15` | Device type / model | R | `MODEL` |
| `16` | Firmware version | R | `V*R*B` |
| `19` | Uptime | R | `D*H*M*S` |
| `22` | Date and time | R/W | `H*M*S*T*W*D*M*Y` |
| `23` | Kernel version | R | `V*R*B` |
| `24` | Distribution version | R | `V*R*B` |

The table above is the complete `DIMENSION` registry defined by the preserved classic SCS/TCP `WHO 13` specification. It is a **published-registry boundary**, not a universal implementation ceiling. Later gateway observations are recorded below only where first-hand evidence exists.

### Read form

Section ID: `ownkb:section:d000036:s000002`

Applicability cues: `gateway`

The request uses the normal `DIMENSION` form with the gateway `WHERE` field empty:

`*#13**DIMENSION##`

The gateway returns the same `DIMENSION` followed by its values:

`*#13**DIMENSION*VALUE1*...*VALUEn##`

The published command-session examples show the response followed by `ACK`. The same value frame can also be emitted to a monitor session.

### Write form

Section ID: `ownkb:section:d000036:s000003`

Writable properties use the `#DIMENSION` form:

`*#13**#DIMENSION*VALUE1*...*VALUEn##`

The published writable set is limited to `DIMENSION 0`, `1`, and `22`.

### `DIMENSION 0` - Time

Section ID: `ownkb:section:d000036:s000004`

Payload: `H*M*S*T`.

| Field | Meaning | Encoding |
| --- | --- | --- |
| `H` | Hour | two digits, `00..23` |
| `M` | Minute | two digits, `00..59` |
| `S` | Second | two digits, `00..59` |
| `T` | Time zone | three digits, sign + hour offset |

For `T`, the first digit encodes the sign: `0` for a positive offset and `1` for a negative offset. The remaining two digits encode the hour offset. The published examples therefore interpret `001` as GMT+1 and `102` as GMT-2.

Read: `*#13**0##`.

Write: `*#13**#0*H*M*S*T##`.

### `DIMENSION 1` - Date

Section ID: `ownkb:section:d000036:s000005`

Payload: `W*D*M*Y`.

| Field | Meaning | Encoding |
| --- | --- | --- |
| `W` | Day of week | `00` Sunday through `06` Saturday |
| `D` | Day | `01..31` |
| `M` | Month | `01..12` |
| `Y` | Year | four digits |

Read: `*#13**1##`.

Write: `*#13**#1*W*D*M*Y##`.

### `DIMENSION 10` - IP address

Section ID: `ownkb:section:d000036:s000006`

Applicability cues: `gateway`

Payload: four decimal octets: `IP1*IP2*IP3*IP4`.

A gateway at `[NETWORK_ADDRESS]`, for example, reports the values as `[NETWORK_ADDRESS]` rather than as a dotted string.

### `DIMENSION 11` - Netmask

Section ID: `ownkb:section:d000036:s000007`

Payload: four decimal octets: `MASK1*MASK2*MASK3*MASK4`.

A netmask of `[NETWORK_ADDRESS]` is therefore represented as `[NETWORK_ADDRESS]`.

### `DIMENSION 12` - MAC address

Section ID: `ownkb:section:d000036:s000008`

Provenance cues: `specification`

Payload: six values: `MAC1*MAC2*MAC3*MAC4*MAC5*MAC6`.

The published specification requires the six octets to be carried as decimal values, not hexadecimal text. A parser should therefore preserve the numeric octets and format a conventional hexadecimal MAC address only at the presentation layer.

### `DIMENSION 15` - Device type

Section ID: `ownkb:section:d000036:s000009`

Applicability cues: `gateway`
Cautions: `must not`
Provenance cues: `catalogue`, `evidence`, `specification`

The published model table defines these values:

| `MODEL` | Gateway model |
| --- | --- |
| `2` | MHServer |
| `4` | MH200 |
| `6` | F452 |
| `7` | F452V |
| `11` | MHServer2 |
| `13` | H4684 |

This table describes the models defined by the published specification. It should not be treated as an exhaustive list of every later OpenWebNet gateway implementation.

First-hand gateway-information captures show that an F454 and an MH202 can both report `MODEL = 200` even though they are distinct gateway models. `DIMENSION 15` is therefore useful identification evidence, but an unlisted or non-unique value must not be converted directly into a unique product identity. Where the gateway supports the Integration Functions diagnostic family, continue identification with diagnostic `WHO 1013 DIMENSION 1` and keep its diagnostic object-model namespace distinct from the functional `DIMENSION 15` model code.

For the complete acquisition-to-catalogue workflow, see [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md).

### `DIMENSION 16` - Firmware version

Section ID: `ownkb:section:d000036:s000010`

Applicability cues: `version`
Provenance cues: `specification`

Payload: `V*R*B`, where `V` is version, `R` release, and `B` build. The specification describes this as the version of the device software implementing the OpenWebNet server.

### `DIMENSION 19` - Uptime

Section ID: `ownkb:section:d000036:s000011`

Applicability cues: `gateway`

Payload: `D*H*M*S`, representing elapsed time since the last gateway start-up.

| Field | Meaning | Published encoding |
| --- | --- | --- |
| `D` | Days | two digits, `00..31` |
| `H` | Hours | two digits, `00..23` |
| `M` | Minutes | two digits, `00..59` |
| `S` | Seconds | two digits, `00..59` |

### `DIMENSION 22` - Date and time

Section ID: `ownkb:section:d000036:s000012`

Payload: `H*M*S*T*W*D*M*Y`. It combines the complete payloads of `DIMENSION 0` and `DIMENSION 1` and is both readable and writable.

Read: `*#13**22##`.

Write: `*#13**#22*H*M*S*T*W*D*M*Y##`.

For clock synchronisation, this combined operation avoids separate time and date transactions.

### `DIMENSION 23` - Kernel version

Section ID: `ownkb:section:d000036:s000013`

Applicability cues: `firmware`, `version`

Payload: `V*R*B`, with version, release, and build components.

This is distinct from `DIMENSION 16`: `16` identifies the OpenWebNet server/device firmware, while `23` reports the underlying kernel version.

### `DIMENSION 24` - Distribution version

Section ID: `ownkb:section:d000036:s000014`

Applicability cues: `firmware`, `gateway`, `version`
Provenance cues: `evidence`

Payload: `V*R*B`, with version, release, and build components.

Together, `DIMENSION 16`, `23`, and `24` expose three distinct software layers: gateway/OpenWebNet firmware, kernel, and operating-system distribution.

A first-hand MH202 information request returned an empty value payload for this read (`*#13**24*##`) rather than the published three-component tuple. This is implementation evidence, not a redefinition of the published schema. Parsers should preserve the raw response and tolerate a gateway that cannot supply all published version components.

### Observed implementation extension: `DIMENSION 40`

Section ID: `ownkb:section:d000036:s000015`

Applicability cues: `firmware`, `gateway`, `scs`, `tcp`, `version`, `zigbee`
Uncertainty: `unknown`
Provenance cues: `evidence`, `specification`

`DIMENSION 40` is not defined by the preserved classic SCS/TCP `WHO 13` specification, the ZigBee `WHO 13` registry, or the canonical MyHOME Suite `OPEN.db` functional model.

Its **existence on later SCS/TCP gateways is nevertheless established by first-hand observation**. Independent gateway-information captures for an F454 and an MH202 both contain the read request:

`*#13**40##`

and both gateways returned:

`*#13**40*4*0##`

The evidence therefore establishes a readable gateway property with a two-value response on those observed implementations. It does **not** establish the meaning of either value, whether the pair is version-like, whether the values are independently variable, or support by other gateway models or firmware revisions. Preserve the values positionally as unknown fields until discriminating evidence exists.

### Numeric IDs not transferable across variants

Section ID: `ownkb:section:d000036:s000016`

Applicability cues: `firmware`, `gateway`, `revision`, `scs`, `tcp`, `version`, `zigbee`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `evidence`, `specification`

ZigBee `WHO 13` explicitly defines `DIMENSION 17` as hardware version. That is established for the ZigBee interface revision documented in [ZigBee Network Management](zigbee-network-management.md#dimension-16-and-17---firmware-and-hardware-versions), but numeric equality does not establish the same meaning for classic SCS/TCP gateways.

`DIMENSION 20` is likewise not assigned a classic SCS/TCP meaning on this page. The currently preserved canonical classic specification, ZigBee specification, MyHOME Suite `OPEN.db`, and the two gateway-information captures examined for this correction do not establish its SCS/TCP payload semantics. The unresolved provenance and required evidence are tracked in [Open Questions](../../reverse-engineering/open-questions.md#who-13-gateway-properties).

# Document: ownkb:document:d000037

Source path: `functional/who-13-integration-gateway/zigbee-network-management.md`
Namespace context: `who:13`
Area: `functional`

## ZigBee Network Management

Section ID: `ownkb:section:d000037:s000001`

Applicability cues: `firmware`, `gateway`, `revision`, `version`, `zigbee`
Provenance cues: `database`, `evidence`, `source`, `specification`

The Legrand ZigBee OpenWebNet specification version 4.0 defines an interface-specific `WHO 13` management surface for the ZigBee OpenWebNet interface. It manages the interface's ZigBee-network role, exposes product-database operations, and reports selected interface and radio Device properties.

This page documents only behavior represented through OpenWebNet. ZigBee radio commissioning, routing, security, and other radio-internal mechanisms are outside the encyclopedia boundary except where an OpenWebNet field exposes their result.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. The document carries Confidential footers, so its publication provenance remains qualified as recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The semantics below are **specification evidence** for this interface revision; they are not a claim of support by every ZigBee gateway, product, or firmware revision.

### `WHAT` reference

Section ID: `ownkb:section:d000037:s000002`

Applicability cues: `gateway`, `scs`, `zigbee`
Provenance cues: `source`, `specification`

The ZigBee specification defines the following `WHO 13` command values:

| `WHAT` | Source action | Principal applicability |
| --- | --- | --- |
| `12` | Boot mode | interface |
| `22` | Reset | interface |
| `30` | Create ZigBee network | interface |
| `31` | Close ZigBee network | interface and product-originated indication |
| `32` | Open ZigBee network | interface and product-originated indication |
| `33` | Join ZigBee network | interface and product-originated indication |
| `34` | Leave ZigBee network | interface or addressed product, plus product-originated indication |
| `60` | Keep connect / readiness | interface |
| `61` | Identify | addressed product |
| `65` | Scan | interface |
| `66` | Supervisor | interface command and product-originated indication |
| `67` | Supervisor remove | interface command and product-originated indication |

Gateway-directed commands use an empty `WHERE`, for example `*13*30*##` for Create and `*13*65*##` for Scan. Product-directed or product-originated frames use the [ZigBee `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing), which is distinct from SCS `A`/`PL` addressing.

#### Boot mode and reset

Section ID: `ownkb:section:d000037:s000003`

Uncertainty: `not established`
Provenance cues: `source`, `specification`

`WHAT 12` requests boot mode with `*13*12*##`. The specification describes an OpenWebNet `ACK` or `NACK` followed, on success, by the ASCII boot-mode acknowledgement `STX 03600796 ETX`, and states that subsequent communication no longer uses ordinary OpenWebNet frames. The OpenWebNet encyclopedia therefore stops at that handoff; the subsequent bootloader protocol referenced by the source is not established as OpenWebNet.

`WHAT 22` resets the interface. The source says the interface returns `ACK` before reset when the request is accepted.

### Network lifecycle

Section ID: `ownkb:section:d000037:s000004`

Applicability cues: `zigbee`
Provenance cues: `source`, `specification`

`WHAT 30` creates a ZigBee network. The source use case states that a successful Create leaves the network created and open.

`WHAT 31` closes an existing network, while `WHAT 32` opens it. The specification also defines addressed, server-originated `WHAT 31` and `WHAT 32` frames as product indications that a ZigBee product closed or opened the network. For interface-directed Open, the detailed table additionally defines `NACK` when a binding procedure is in progress.

`WHAT 33` requests that the interface join an existing network. The detailed `WHAT` definition also assigns addressed, server-originated `WHAT 33` frames to product join indications.

`WHAT 34` requests that the interface leave its network. The detailed definition additionally allows `*13*34*WHERE#9##` to request that an addressed product leave, and uses the same addressed form as a product-originated leave indication. For the client-to-product form, the table explicitly defines `ACK` when the command has been sent; it does not separately list a client-to-product `NACK` case.

#### Source inconsistencies

Section ID: `ownkb:section:d000037:s000005`

Cautions: `must not`
Provenance cues: `documentation`, `evidence`, `source`

The source contains two material inconsistencies that must not be silently normalized:

- The `WHO 13` Join use case shows `*13*33*##` followed by `ACK` and then an addressed `WHAT 32` frame, while the detailed `WHAT` table assigns addressed product join indications to `WHAT 33`. The current corpus does not establish whether the use-case frame is a documentation error or represents an additional event.
- The detailed Leave table describes both the `ACK` and `NACK` cases with wording equivalent to "has not left." The preceding Leave use case states that `ACK` accompanies a successful leave. The reference therefore treats the duplicated negative wording as a source defect rather than evidence that successful Leave has inverted acknowledgement semantics.

### Readiness and identification

Section ID: `ownkb:section:d000037:s000006`

Applicability cues: `zigbee`
Provenance cues: `source`

`WHAT 60` is the interface readiness operation. `*13*60*##` returns `ACK` when the interface is ready and `NACK` when it is not.

`WHAT 61` identifies an addressed product. The source specifies a ZigBee `WHERE` with Unit `00` and says the product's green LED blinks slowly for five minutes. `ACK` indicates that the identify command was sent; `NACK` indicates that it was not. A BUSY result follows the interface-specific BUSY/NACK handling documented under [ZigBee acknowledgement behavior](../../protocol/zigbee-interface.md#acknowledgement-behavior).

### Supervisor mode

Section ID: `ownkb:section:d000037:s000007`

Applicability cues: `zigbee`
Provenance cues: `source`, `specification`

`WHAT 66` sends the supervisor command. The specification describes this as a broadcast to active products that enables reporting of subsequent state changes to the OpenWebNet interface. The detailed definition also lists addressed server-originated `*13*66*WHERE#9##` traffic "from ZigBee product"; the source does not assign that indication a stronger meaning than the table provides. A newly joined product requires the supervisor command to be sent again before that product participates in this mode.

`WHAT 67` is the complementary Supervisor Remove operation. The source calls it the default mode and says it prevents receipt of product state changes enabled through Supervisor. Its detailed definition likewise lists addressed server-originated `*13*67*WHERE#9##` traffic from a product without defining additional payload semantics.

The source recommends only one OpenWebNet interface with supervisor mode enabled in a ZigBee network for normal operation because multiple supervisors reduce radio-network performance. This is an interface-specific ZigBee constraint, not a generic OpenWebNet session rule.

### Scan and product database

Section ID: `ownkb:section:d000037:s000008`

Provenance cues: `database`

The interface maintains an internal product database. Section 6 says the database can contain up to 175 products and is managed automatically by the interface. The database is a stored inventory, not a statement that every stored product is currently reachable.

#### Database population and persistence

Section ID: `ownkb:section:d000037:s000009`

Applicability cues: `zigbee`
Provenance cues: `database`, `source`

When the interface is present as products join a network, the source says each new joining product fills the product database. The section 6.1.1 use case shows the stored product count increasing as both routers and end Devices join.

When the interface itself joins an existing ZigBee network, section 6.1.2 says it initially does not know the existing products. The OpenWebNet user sends Scan to learn active products. Products that are not active during that process, particularly sleeping battery end Devices, require later activity described by the source before they can be added. Section 6.1.3 likewise states that a product which joins while the interface is powered off is not known to the interface at that time; its use case shows later Scan or product activity as ways the stored population can be updated.

The source explicitly says that the number of products in the database does not change across an interface power cycle. Section 6.1.4 also states that a product which leaves the ZigBee network while the interface is powered off remains in the database. The source defines no OpenWebNet command in the inspected discovery/inventory material for deleting that stale entry, no aging interval, and no automatic stale-entry pruning rule.

These rules establish that database membership and current reachability are distinct states.

#### Scan

Section ID: `ownkb:section:d000037:s000010`

Applicability cues: `zigbee`
Provenance cues: `database`, `specification`

`WHAT 65` initiates a scan with `*13*65*##`. The specification says the interface broadcasts over the ZigBee network and active routers plus awake end Devices can answer. The command returns `ACK` when sent. The documented flow then reports `DIMENSION 67` approximately 13 seconds later.

The detailed Scan definition explicitly warns that the resulting count is the number of products stored in the interface product database, not simply the number of active routers seen during that scan. A Scan can therefore contribute newly active products to the stored database without turning `DIMENSION 67` into a count of only the current responders. The detailed operation returns `NACK` when the Scan command was not sent; it does not assign a Scan-specific BUSY result.

### `DIMENSION` reference

Section ID: `ownkb:section:d000037:s000011`

Applicability cues: `firmware`, `scs`, `tcp`, `version`, `zigbee`
Cautions: `must not`
Provenance cues: `database`, `source`, `specification`

The ZigBee specification defines this `WHO 13` `DIMENSION` set:

| `DIMENSION` | Source property | Applicability |
| --- | --- | --- |
| `12` | MAC / IEEE address | interface |
| `16` | Firmware version | interface or addressed product |
| `17` | Hardware version | interface or addressed product |
| `26` | Implemented `WHO` values | interface or addressed product |
| `66` | Product information | product-database entry or addressed product |
| `67` | Number of products | interface product database |
| `71` | ZigBee channel | interface |
| `72` | Battery information | applicable battery product |
| `73` | Device MAC address by index | product-database entry |

This table is variant-specific. It must not be supplemented with SCS/TCP `WHO 13` dimensions merely because the namespace number is shared.

#### `DIMENSION 12` - Interface IEEE address

Section ID: `ownkb:section:d000037:s000012`

Provenance cues: `documentation`, `source`

The request is `*#13**12##`. The source returns the interface IEEE address as eight decimal values followed by `ACK`.

This property is protocol knowledge, but real installation identifiers are not. Documentation and tests should use symbolic or synthetic values rather than retaining a real interface address.

#### `DIMENSION 16` and `17` - Firmware and hardware versions

Section ID: `ownkb:section:d000037:s000013`

Applicability cues: `firmware`, `version`, `zigbee`

`DIMENSION 16` reports three firmware components: version, release, and build. `DIMENSION 17` reports major, minor, and release hardware-version components.

Both can address the interface with an empty `WHERE` or a ZigBee product with product-level Unit `00`. The exact request forms are `*#13**16##` or `*#13*PRODUCT00#9*16##` for firmware and `*#13**17##` or `*#13*PRODUCT00#9*17##` for hardware. Firmware responses append `VERSION*RELEASE*BUILD`; hardware responses append `MAJOR*MINOR*RELEASE`. Both operations end successfully with `ACK`, define `NACK` when the command is not sent, and use the interface-wide BUSY/NACK sequence. Availability for one target does not establish support by every product.

#### `DIMENSION 26` - Implemented `WHO` values

Section ID: `ownkb:section:d000037:s000014`

Provenance cues: `evidence`, `source`

`DIMENSION 26` reports the functional `WHO` values implemented by the selected target. The exact requests are `*#13**26##` for the interface or `*#13*PRODUCT00#9*26##` for an addressed product; the response appends one or more `WHO` values before the terminating `ACK`. The source also defines `NACK` when the command is not sent and the interface-wide BUSY/NACK sequence. The returned list is capability evidence for that target; it does not establish that every operation of every reported namespace is supported.

#### `DIMENSION 66` - Product information

Section ID: `ownkb:section:d000037:s000015`

Applicability cues: `zigbee`
Uncertainty: `may`, `not established`
Provenance cues: `catalogue`, `database`, `source`, `specification`

Product information can be requested either by a zero-based product-database index or by an addressed product:

- by index: `*#13**66#INDEX##`;
- by product: `*#13*WHERE#9*66##`, using product-level Unit `00`.

Responses use `DIMENSION 66` and identify product Units/endpoints with an index and a numeric Device-ID/type value. The specification provides this Device-ID registry:

| Device ID | Source label | Source category |
| --- | --- | --- |
| `2` | `scenario_control` | Scenario |
| `256` | `on_off_switch` | Lighting |
| `257` | `dimmer_control` | Lighting |
| `258` | `dimmer_switch` | Lighting |
| `259` | `switch_motion_detector` | Lighting |
| `260` | `daylight_sensor` | Lighting |
| `261` | `scs_on_off_switch` | Lighting |
| `262` | `scs_dimmer_control` | Lighting |
| `263` | `scs_dimmer_switch` | Lighting |
| `264` | `waterproof_1_gang_switch` | Lighting |
| `265` | `automatic_dimmer_switch` | Lighting |
| `266` | `toggle_control` | Lighting |
| `267` | `scs_toggle_control` | Lighting |
| `268` | `motion_detector` | Lighting |
| `269` | `switch_motion_detector_II` | Lighting |
| `270` | `motion_detector_II` | Lighting |
| `271` | `auxilliary_toggle_control` | Lighting |
| `272` | `scs_auxilliary_toggle_control` | Lighting |
| `273` | `multifonction_scenario_control` | Lighting |
| `274` | `on_off_control` | Lighting |
| `275` | `auxiliary_on_off_1_gang_switch` | Lighting |
| `512` | `shutter_control` | Automation |
| `513` | `shutter_switch` | Automation |
| `514` | `scs_shutter_control` | Automation |
| `515` | `scs_shutter_switch` | Automation |
| `1024` | `scs_1_System_1-4_Gateway` | Interface |
| `1025` | `scs_2_System_1-4_Gateway` | Interface |
| `1029` | `network_repeater` | Interface |
| `1030` | `OpenWebNet interface` | Interface |
| `1536` | `video_switcher` | Video |

These labels are preserved as source vocabulary. Numeric equality with catalogue or MyHOME Suite entities is not established by this table.

The source says this operation may take up to 30 seconds when a product is not reachable, for example when a battery-powered Device is sleeping. It defines a response value of `0` for an unreachable product and terminates the reported Unit sequence with `ACK`. `NACK` is defined when the command cannot be sent over ZigBee or when the requested index is beyond the interface's known range. BUSY uses the interface-wide BUSY/NACK retry sequence documented under [ZigBee acknowledgement behavior](../../protocol/zigbee-interface.md#acknowledgement-behavior).

The published parameter separator is `#INDEX`. The exploratory ZigBee branch recorded an alternate `*INDEX` form as an implementation compatibility claim, but that form is not established by this specification and is not part of the canonical grammar.

#### `DIMENSION 67` - Product count

Section ID: `ownkb:section:d000037:s000016`

Provenance cues: `database`, `source`

`*#13**67##` requests the number of products in the interface product database. The response is `*#13**67*VALUE##` followed by `ACK`; `NACK` is defined when the command is not sent.

The source uses "products discovered" in parts of the detailed description while explicitly stating that the value comes from the interface product database. The database interpretation is therefore retained as the stronger local qualification.

#### `DIMENSION 71` - ZigBee channel

Section ID: `ownkb:section:d000037:s000017`

Applicability cues: `zigbee`
Provenance cues: `source`

`*#13**71##` requests the ZigBee network channel. The published range is `11..26`; the source defines `NACK` when the interface is not inside a ZigBee network. This page records the OpenWebNet-visible value only; ZigBee RF channel-selection mechanics are outside scope.

#### `DIMENSION 72` - Battery information

Section ID: `ownkb:section:d000037:s000018`

Provenance cues: `source`

Battery information is a server-originated frame of the form `*#13*WHERE#9*72*VALUE##`. The source says this frame is visible when a sleepy end Device sends activity after its network/learn buttons are used; receiving it from the source-named applicative button requires the prior source-named "PnL" procedure with the interface. Those physical-button details describe event availability, not an additional OpenWebNet command. The source defines:

| `VALUE` | Source label |
| --- | --- |
| `0` | `CRITICAL` |
| `1` | `POWER_VALUE_33` |
| `2` | `POWER_VALUE_66` |
| `3` | `POWER_VALUE_100` |

The frame can carry a Unit-specific `WHERE`. That addressing does not by itself prove that each Unit has an independent battery.

#### `DIMENSION 73` - Product identifier by index

Section ID: `ownkb:section:d000037:s000019`

Applicability cues: `zigbee`
Cautions: `warning`
Uncertainty: `unknown`
Provenance cues: `database`, `source`

`*#13**73#INDEX##` requests the ZigBee product identifier associated with a zero-based product-database index. The response uses `*#13*WHERE#9*73#INDEX*VALUE##` with Unit `00` and classifies the stored product as:

| `VALUE` | Source meaning |
| --- | --- |
| `0` | unknown |
| `1` | mains-powered Device |
| `2` | battery-powered Device |

The detailed use case says this operation asks the interface database for the product identifier and does not send a ZigBee frame to reach the product. This makes `DIMENSION 73` a local stored-inventory lookup rather than a reachability test.

The same use-case paragraph also repeats a statement that the "product information command" could take 30 seconds when a product is unreachable. That warning conflicts with the immediately following statement that this indexed lookup does not contact the product. The 30-second reachability warning is therefore retained for `DIMENSION 66`, where it is independently defined, and is not promoted as established `DIMENSION 73` timing.

The source labels `DIMENSION 73` "Device MAC address by index," but the returned `WHERE` is the ZigBee OpenWebNet product identifier form derived from the product address model, not the eight-value interface IEEE address returned by `DIMENSION 12`. A successful indexed lookup ends with `ACK`; `NACK` is defined when the index is unknown.

### Discovery relationship and source conflicts

Section ID: `ownkb:section:d000037:s000020`

Applicability cues: `zigbee`
Cautions: `warning`
Uncertainty: `contradiction`
Provenance cues: `database`, `source`, `specification`

The specification exposes several distinct discovery mechanisms:

1. [`WHO 1000 DIMENSION 81` neighbor discovery](../../protocol/zigbee-interface.md#neighbor-discovery---who-1000-dimension-81) traverses neighbor information reported by the interface and newly discovered routers.
2. `WHO 13 WHAT 65` scans the ZigBee network and later reports the product-database count through `DIMENSION 67`.
3. `DIMENSION 73` resolves a product-database index locally to its stored ZigBee product identifier and power type.
4. `DIMENSION 66` queries Units/endpoints and numeric Device-ID/type information for an indexed or addressed product and can expose that a stored product is unreachable.

The source does not define one contradiction-free canonical sequence combining all four. Section 5.4 shows Scan followed by `DIMENSION 67` and then indexed `DIMENSION 73` requests, but its explanatory prose under those `DIMENSION 73` exchanges says that the product supplies endpoints and Device IDs. The detailed definitions later assign endpoint/Device-ID information to `DIMENSION 66` and define `DIMENSION 73` as index-to-product-identifier/power-type lookup.

Section 5.2 also shows a product-join discovery frame with command/status content but a leading `*#13` form. The detailed `WHO 13` Product Joins use case and `WHAT 33` definition use the command/status form `*13*33*WHERE#9##`. The leading `#` in section 5.2 is therefore preserved as a source inconsistency rather than promoted as an alternate join grammar.

The `DIMENSION 73` use-case paragraph contains a separate copied-looking reachability warning while also stating that the operation is a local database lookup which sends no ZigBee frame. The encyclopedia preserves that contradiction and does not assign the `DIMENSION 66` 30-second reachability behavior to `DIMENSION 73`.

The encyclopedia therefore preserves the primitives and these source inconsistencies rather than replacing them with an inferred canonical workflow.

### Evidence limits

Section ID: `ownkb:section:d000037:s000021`

Applicability cues: `applies to`, `firmware`, `version`, `zigbee`
Provenance cues: `source`, `specification`

No inspected source establishes that the MyHOME Suite diagnostic Device-interview model - including diagnostic `WHO 1001` and `DIMENSION 30`, `32`, or `35` - applies to this ZigBee interface.

The specification also does not establish the exploratory branch's firmware-version threshold for binding, alternate `DIMENSION 66` separator syntax, or old-firmware ACK workarounds. Those remain implementation claims requiring separate provenance before they can become canonical compatibility notes.

See [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for transport, addressing, acknowledgement behavior, and cross-namespace applicability.

# Document: ownkb:document:d000038

Source path: `functional/who-14-special-commands/README.md`
Namespace context: `who:14`
Area: `functional`

## `WHO 14` - Special Commands

Section ID: `ownkb:section:d000038:s000001`

Provenance cues: `evidence`, `specification`

`WHO 14` is the OpenWebNet Special Commands namespace. The canonical public PDF corpus does not contain a dedicated `WHO 14` specification, but the MyHOME_Suite ScenarioDevices capability databases provide direct implementation evidence for the operations they expose.

### Actuator lock / unlock

Section ID: `ownkb:section:d000038:s000002`

Provenance cues: `evidence`

ScenarioDevices defines an Object named `miniScenarioSuite.specialCommands.actionLockUnlockActuator.descr` with two scenario actions:

| `WHAT` | Frame | MyHOME_Suite command | Meaning |
| --- | --- | --- | --- |
| `0` | `*14*0*WHERE##` | `miniScenarioSuite.specialCommands.actionLockUnlockActuator.lock` | Lock actuator |
| `1` | `*14*1*WHERE##` | `miniScenarioSuite.specialCommands.actionLockUnlockActuator.unlock` | Unlock actuator |

This is stronger evidence than the frame templates alone: MyHOME_Suite associates the two wire operations with an explicit lock/unlock actuator capability.

### Addressing

Section ID: `ownkb:section:d000038:s000003`

Provenance cues: `database`

The ScenarioDevices records use `WhereType = 1` and substitute the selected target into the `WHERE` placeholder. The database does not define a separate `WHO 14` address grammar; the address must therefore be interpreted in the context of the selected actuator Object and the underlying system.

A decoder should preserve the literal `WHERE` rather than assume that `WHO 14` introduces a new universal address family.

### Scope of the semantics

Section ID: `ownkb:section:d000038:s000004`

Provenance cues: `evidence`

The lock/unlock labels are directly established for the MyHOME_Suite actuator lock/unlock Object. They should not be generalized to undocumented `WHO 14` values or to arbitrary target types without further evidence.

The two known commands are ordinary command frames, not `DIMENSION` operations. No additional `WHO 14` `WHAT` or `DIMENSION` vocabulary is established by `OPEN.db` or the ScenarioDevices databases in the current corpus.

### Scenario-engine relationship

Section ID: `ownkb:section:d000038:s000005`

Provenance cues: `database`

ScenarioDevices exposes `WHO 14` as an action capability, so MyHOME_Suite can place actuator lock/unlock operations in higher-level scenarios. This does not make `WHO 14` itself a scenario protocol.

Stored scenarios remain under [`WHO 0`](../who-0-scenarios/), while scenario-programmer execution and management are under [`WHO 17`](../who-17-scenario-management/).

See [Cross-database functional coverage](../cross-database-coverage.md) for the relationship between ScenarioDevices, `OPEN.db`, and `MHCatalogue.db`, and [Scenario Engine](../../scenario-engine/) for the higher-level trigger/condition/action model.

# Document: ownkb:document:d000039

Source path: `functional/who-15-cen/README.md`
Namespace context: `who:15`
Area: `functional`

## `WHO 15` - CEN

Section ID: `ownkb:section:d000039:s000001`

Applicability cues: `gateway`, `scs`
Provenance cues: `source`

`WHO 15` carries Basic and Evolved CEN button interactions. A CEN frame identifies the button through `WHAT`, the command source through `WHERE`, and - for Evolved CEN phases - the interaction phase through a parameter attached to `WHAT`.

CEN frames can originate from physical SCS commands configured in CEN mode or can be injected virtually by a client through an OpenWebNet/SCS gateway. Event-session clients receive the corresponding bus event.

### Interaction model

Section ID: `ownkb:section:d000039:s000002`

Basic CEN reports the initial pressure. Evolved CEN adds release and hold information, allowing a receiver to distinguish a short press from an extended interaction.

| Interaction | Frame form |
| --- | --- |
| Pressure | `*15*BUTTON*WHERE##` |
| Release after short pressure | `*15*BUTTON#1*WHERE##` |
| Release after extended pressure | `*15*BUTTON#2*WHERE##` |
| Extended pressure | `*15*BUTTON#3*WHERE##` |

### Button `WHAT`

Section ID: `ownkb:section:d000039:s000003`

Provenance cues: `source`

The button identifier occupies the range `00..31`. The leading zero is significant in the published examples and should be preserved when representing the canonical frame text.

| `WHAT` | Meaning |
| --- | --- |
| `00..31` | CEN button number |

The button number is not the physical address of the command device. Device/source addressing is carried separately by `WHERE`.

### `WHAT` parameters

Section ID: `ownkb:section:d000039:s000004`

| Parameter | Meaning |
| --- | --- |
| none | Initial pressure |
| `#1` | Release after short pressure |
| `#2` | Release after extended pressure |
| `#3` | Extended pressure / keep pressing |

An extended pressure begins after the button has been held for approximately 0.5 seconds. The published behavior then emits an extended-pressure frame every approximately 0.5 seconds while the button remains pressed, followed by `#2` when it is released.

This makes CEN a small interaction state machine rather than four unrelated events.

### Short interaction sequence

Section ID: `ownkb:section:d000039:s000005`

A short press produces:

`*15*BUTTON*WHERE##` â†’ `*15*BUTTON#1*WHERE##`

The first frame marks pressure; the second identifies release before the extended-pressure threshold.

### Extended interaction sequence

Section ID: `ownkb:section:d000039:s000006`

A held button produces:

`*15*BUTTON*WHERE##` â†’ one or more `*15*BUTTON#3*WHERE##` â†’ `*15*BUTTON#2*WHERE##`

Receivers should tolerate repeated `#3` frames for one physical hold. They represent continued pressure, not separate button activations.

### `WHERE` addressing

Section ID: `ownkb:section:d000039:s000007`

Provenance cues: `source`

The published CEN address table includes normal `A`/`PL` and advanced/local-bus forms.

| Form | Meaning |
| --- | --- |
| `[1-9][1-9]` | Normal area/light-point `A`/`PL` |
| `[00][01-15]` | Zone 0, advanced `A`/`PL` |
| `[10][01-15]` | Zone 10, advanced `A`/`PL` |
| `[01-09][10-15]` | Light point 10..15, advanced `A`/`PL` |
| `WHERE#3` | Private riser bus parameter |
| `WHERE#4#[01-15]` | Local bus selected by interface `I4` |

The address must be parsed according to the CEN grammar. Values such as `0001`, `22`, and local-bus forms are source addresses, not CEN+ virtual Objects.

### Action connection

Section ID: `ownkb:section:d000039:s000008`

Applicability cues: `gateway`, `scs`

A client can generate a virtual CEN interaction by writing the same functional frames on an action connection. The gateway returns `ACK` when it accepts the frame for transmission.

Published virtual operations are:

| Operation | Action frame |
| --- | --- |
| Pressure | `*15*BUTTON*WHERE##` |
| Short release | `*15*BUTTON#1*WHERE##` |
| Release after extended pressure | `*15*BUTTON#2*WHERE##` |
| Extended pressure | `*15*BUTTON#3*WHERE##` |

A corresponding frame is then visible to event-session clients when the CEN frame is read on the SCS bus.

### Event connection

Section ID: `ownkb:section:d000039:s000009`

Event frames can originate from either a physical CEN-configured command or a virtual CEN operation sent by an OpenWebNet client. The wire form does not encode that origin distinction; consumers observing an event connection receive the CEN interaction itself.

The published examples demonstrate normal, advanced and local-bus addresses, including `*15*01*0001##`, `*15*02*22##`, `*15*06*36#4#01##`, and their release/extended variants. These examples establish that the `#4#I4` suffix belongs to `WHERE`, while the `#1`/`#2`/`#3` suffix belongs to `WHAT`.

### Device configuration modes

Section ID: `ownkb:section:d000039:s000010`

Applicability cues: `scs`
Provenance cues: `source`, `specification`

The CEN specification distinguishes how a physical command obtains its source identity:

| Configuration | Bus address behavior |
| --- | --- |
| Advanced Virtual Configuration | CEN device does not use a conventional address on the SCS bus; configured Object/address is mapped to `WHERE` |
| Basic Virtual Configuration | Device uses an SCS bus address |
| Physical configurators | Device uses an SCS bus address |

This configuration distinction affects the source represented by `WHERE`; it does not change the CEN button interaction vocabulary.

### CEN versus CEN+

Section ID: `ownkb:section:d000039:s000011`

CEN+ is carried under [`WHO 25`](../who-25-transversal/cen-plus.md) and uses a different event model: `WHAT 21..24` encode the interaction phase while the pushbutton number becomes a `WHAT` parameter and `WHERE` identifies a virtual Object. Rotary-selector events are also defined there.

A parser must therefore select `WHO 15` or `WHO 25` before interpreting the numeric fields. CEN and CEN+ are related command systems but are not alternate encodings of one universal `WHAT` table.

See the [functional overview](../) for navigation by `WHO` and by function.

# Document: ownkb:document:d000040

Source path: `functional/who-16-sound-system/README.md`
Namespace context: `who:16`
Area: `functional`

## `WHO 16` - Sound System

Section ID: `ownkb:section:d000040:s000001`

`WHO 16` controls the earlier Sound System dialect: amplifiers, sources, tuner frequency, stored stations, RDS, volume, tone, balance, sleep, and Follow Me.

### `WHAT` values

Section ID: `ownkb:section:d000040:s000002`

Provenance cues: `source`

| `WHAT` | Meaning |
| --- | --- |
| `0` / `3` | ON using base-band / stereo-channel source |
| `10` / `13` | OFF using base-band / stereo-channel source |
| `20` / `23` | Cycle source, base band / stereo channel |
| `30` / `33` | Sleep on base band / stereo channel |
| `40` | Sleep OFF |
| `50` / `53` | Follow Me, base band / stereo channel |
| `100` | Source busy |
| `101` / `102` | Start / stop RDS transmission |
| `1001..1015` | Increase volume by `1..15` |
| `1101..1115` | Decrease volume by `1..15` |
| `2001..2015` | Increase high tones by `1..15` |
| `2101..2115` | Decrease high tones by `1..15` |
| `5000` | Seek next higher free frequency |
| `5001..5015` | Increase frequency by `0.05..0.75 MHz` |
| `5100` | Seek next lower free frequency |
| `5101..5115` | Decrease frequency by `0.05..0.75 MHz` |
| `6001..6015` | Advance station/track by `1..15` |
| `6101..6115` | Move back station/track by `1..15` |

The final digits carry magnitude and are part of `WHAT`.

### `WHERE`

Section ID: `ownkb:section:d000040:s000003`

Provenance cues: `source`

| Target | `WHERE` |
| --- | --- |
| All amplifiers | `0` |
| Amplifiers in environment `0..9` | `#0..#9` |
| Individual amplifier | `01..99` |
| All sources | `100` |
| Source `1..9` | `101..109` |

Amplifier and source targets share the namespace but have different ranges. Preserve leading zeroes on amplifier addresses.

### `DIMENSION` values

Section ID: `ownkb:section:d000040:s000004`

Applicability cues: `only for`
Cautions: `do not`
Provenance cues: `source`

| `DIMENSION` | Meaning | Established detail |
| --- | --- | --- |
| `1` | Volume | `0..31`; readable/reportable/writable |
| `2` | High tones | listed in the global table |
| `3` | Low tones | listed in the global table |
| `4` | Balance | listed in the global table |
| `5` | State | request returns ordinary `WHAT` state frames |
| `6` | Frequency | six decimal digits, expressed in kHz by the examples (`107000` = 107.00 MHz) |
| `7` | Stored station / track | station write range `1..5` |
| `8` | RDS | eight ASCII character codes as separate values |
| `9` | Frequency plus station/track | listed in the global table |
| `10` | Memorized station | station range `1..5` |

The source gives complete flows only for a subset. Do not invent payloads for table-only `DIMENSION` values `2`, `3`, `4`, or `9`.

### Volume

Section ID: `ownkb:section:d000040:s000005`

```text
*#16*WHERE*1##
*#16*AMPLIFIER*1*VOLUME##
*#16*WHERE*#1*VOLUME##
```

General or environment reads can return one response for each active amplifier, followed by a terminating acknowledgement.

### State

Section ID: `ownkb:section:d000040:s000006`

`*#16*WHERE*5##` returns ordinary `*16*WHAT*WHERE##` frames. Collective requests can expand to individual active amplifiers or sources. State is therefore a result sequence, not necessarily a scalar `DIMENSION 5` response.

### Frequency, station, and RDS

Section ID: `ownkb:section:d000040:s000007`

Provenance cues: `source`

Frequency request/write:

```text
*#16*SOURCE*6##
*#16*SOURCE*6*0*FREQUENCY##
*#16*SOURCE*#6*0*FREQUENCY##
```

Stored station request/write uses `DIMENSION 7`; memorized-station write uses `DIMENSION 10`. A frequency or station change can additionally emit RDS (`DIMENSION 8`) when available.

RDS text is carried as eight separate decimal ASCII codes, not as literal characters. For example, the source encodes an eight-character label as eight `*`-separated values.

### Direction and capability

Section ID: `ownkb:section:d000040:s000008`

Cautions: `do not`
Provenance cues: `source`

Relative `WHAT` operations and absolute `DIMENSION` values are complementary. Do not reconstruct authoritative volume, tone, or frequency state solely by counting relative commands when a corresponding report is available.

Support is target-dependent: amplifier addresses accept amplifier operations; source addresses accept source/tuner operations. A namespace-level identifier does not imply applicability to both.

### Relationship to `WHO 22`

Section ID: `ownkb:section:d000040:s000009`

Cautions: `must not`

`WHO 16` and [`WHO 22`](../who-22-sound-diffusion/) encode similar concepts using different commands, addresses, and properties. They are separate dialects and must not be translated by numeric coincidence.

### Evidence basis

Section ID: `ownkb:section:d000040:s000010`

Provenance cues: `specification`

Tables, ranges, and flows come from [`WHO 16` specification](../../sources/openwebnet-public/pdf/WHO_16.pdf). Where the global table lists a property without a detailed allowed-message flow, this page says so explicitly.

See the [functional overview](../) for navigation by `WHO` and by function, and [Protocol](../../protocol/) for common frame and session syntax.

# Document: ownkb:document:d000041

Source path: `functional/who-17-scenario-management/README.md`
Namespace context: `who:17`
Area: `functional`

## `WHO 17` - Scenario Management

Section ID: `ownkb:section:d000041:s000001`

Applicability cues: `gateway`

`WHO 17` controls scenes managed by scenario-programmer/gateway devices. Its published functional model consists of Start, Stop, Enable and Disable operations addressed to a scene identifier, together with status requests and event reporting.

It is distinct from [`WHO 0`](../who-0-scenarios/): `WHO 0` invokes and programs scenario-module memories, whereas `WHO 17` controls the execution state of scenes managed by a scenario programmer.

### `WHAT` reference

Section ID: `ownkb:section:d000041:s000002`

| `WHAT` | Meaning |
| --- | --- |
| `1` | Start scene |
| `2` | Stop scene |
| `3` | Enable scene |
| `4` | Disable scene |

These values are both command operations and reported scene states/events. Their interpretation is scoped to `WHO 17`.

### `WHERE`

Section ID: `ownkb:section:d000041:s000003`

Provenance cues: `specification`

| `WHERE` | Meaning |
| --- | --- |
| `0` | General |
| `1..300` | Scene number on MH200N |
| Numeric value | Scene identifier on MH202 |

The public specification intentionally gives MH202 as a numeric scene identifier rather than imposing the MH200N `1..300` range. Implementations should therefore preserve the target-device distinction instead of globally validating every `WHO 17` `WHERE` against the MH200N range.

### Start scene - `WHAT 1`

Section ID: `ownkb:section:d000041:s000004`

Applicability cues: `gateway`

Command: `*17*1*WHERE##`.

On a command connection the gateway acknowledges an accepted operation with `ACK`. The corresponding event is `*17*1*WHERE##` on the event connection.

Start changes the execution state of the addressed scene; it is not equivalent to `WHO 0` selecting a numbered slot in an F420 scenario module.

### Stop scene - `WHAT 2`

Section ID: `ownkb:section:d000041:s000005`

Command: `*17*2*WHERE##`.

The event form is the same frame on an event connection. Stop terminates execution of the addressed scene without changing whether that scene is enabled for subsequent activation.

### Enable scene - `WHAT 3`

Section ID: `ownkb:section:d000041:s000006`

Command: `*17*3*WHERE##`.

Enable controls scene availability. It is therefore orthogonal to the Start/Stop execution pair: an enabled scene can subsequently be started, while a disabled scene is not available for normal activation.

### Disable scene - `WHAT 4`

Section ID: `ownkb:section:d000041:s000007`

Command: `*17*4*WHERE##`.

The corresponding event uses the same functional frame. Disable changes availability rather than merely stopping a currently executing scene.

### Status request

Section ID: `ownkb:section:d000041:s000008`

Provenance cues: `specification`

The published status request is `*#17*WHERE##`.

The server reports scene state using the same `WHO 17` `WHAT` vocabulary and then terminates the response with `ACK`. The specification groups the possible returned states as `WHAT 1..2` and `WHAT 3..4`, reflecting the two independent aspects of scene state:

| State axis | Returned `WHAT` |
| --- | --- |
| Execution | `1` Start / running, `2` Stop / stopped |
| Availability | `3` Enabled, `4` Disabled |

A status request can therefore produce more than one functional state frame before the final `ACK`; clients should not assume a single scalar status.

### Event connection

Section ID: `ownkb:section:d000041:s000009`

The event connection reports changes with the same four normal frames:

| Event | Frame |
| --- | --- |
| Scene started | `*17*1*WHERE##` |
| Scene stopped | `*17*2*WHERE##` |
| Scene enabled | `*17*3*WHERE##` |
| Scene disabled | `*17*4*WHERE##` |

Command acknowledgement and event propagation are separate. `ACK` confirms the command transaction, while the event frame represents the functional scene state/event visible to event-session clients.

### MyHOME_Suite extended scenario-programmer operations

Section ID: `ownkb:section:d000041:s000010`

Cautions: `must not`

The MyHOME_Suite `OPEN.db` definitions contain additional scenario-programmer operations beyond the four ordinary functional commands published in the `WHO 17` document. These include starting scenario programming, resetting programming, ending programming, setting/requesting scenario state through `DIMENSION 40`, reporting scenario errors through `DIMENSION 41`, and testing scenario activation.

These definitions establish that MyHOME_Suite has a richer scenario-programmer workflow than the public Start/Stop/Enable/Disable reference. They should be interpreted in their sequence/session context rather than assigned ordinary `WHAT` semantics without the corresponding frame definitions.

In particular, the implementation data distinguishes operations for:

| Operation family | Established implementation role |
| --- | --- |
| Programming start | Enter scenario-programming workflow |
| Scenario reset | Reset scenario-programming state |
| Programming end | Finish scenario programming |
| `DIMENSION 40` | Set, request and report scenario state |
| `DIMENSION 41` | Scenario error reporting |
| Test activation | Exercise scenario activation in the programming workflow |

The public `WHO 17` functional state model remains the canonical interpretation of `WHAT 1..4`; implementation-only programming operations are complementary and must not be collapsed into that four-value table.

### Relationship to scenario systems

Section ID: `ownkb:section:d000041:s000011`

Applicability cues: `gateway`

[`WHO 0`](../who-0-scenarios/) addresses scenario modules such as F420 and their stored scenario slots. `WHO 17` addresses scenes managed by scenario-programmer/gateway devices. The MyHOME_Suite [Scenario Engine](../../scenario-engine/) is a higher-level capability model that can compose functional operations from multiple `WHO` namespaces.

See [Protocol](../../protocol/) for common command, status and event-session behavior.

The [functional overview](../) groups `WHO 0` and `WHO 17` under scenario-related functions without merging their protocol namespaces.

# Document: ownkb:document:d000042

Source path: `functional/who-18-energy-management/README.md`
Namespace context: `who:18`
Area: `functional`

## `WHO 18` - Energy Management

Section ID: `ownkb:section:d000042:s000001`

Applicability cues: `scs`, `zigbee`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `source`

`WHO 18` defines the OpenWebNet Energy Management system. It covers energy measurement, accumulated consumption, historical series, Energy Management actuators, differential-current information, Stop&Go supervision, and automatic reporting of active power.

The namespace is heterogeneous: the selected `WHERE` identifies a device family, and the valid `WHAT` and `DIMENSION` operations depend on that family. A Stop&Go address, an energy meter/central unit address, and an Energy Management actuator address therefore cannot be treated as interchangeable numeric targets.

These references follow `WHO_18.pdf`. The [ZigBee Interface](../../protocol/zigbee-interface.md) defines a separate Energy Management surface and address model, including unresolved Reset and Frequency/Energy source conflicts and a materially different `DIMENSION 1200` grammar. See the [ZigBee Energy Management Variant](zigbee-variant.md). Do not transfer SCS ranges, units, or reset semantics to that variant solely from `WHO 18` equality.

### Reference

Section ID: `ownkb:section:d000042:s000002`

Applicability cues: `zigbee`
Provenance cues: `source`

| Subject | Page |
| --- | --- |
| Commands and command parameters | [`WHAT` Reference](what.md) |
| Device families and `WHERE` grammar | [Addressing](addressing.md) |
| Measurements, totalizers, actuator state, Stop&Go and historical data | [`DIMENSION` Reference](dimensions.md) |
| ZigBee-specific Energy Management semantics and source conflicts | [ZigBee Energy Management Variant](zigbee-variant.md) |

### Device families

Section ID: `ownkb:section:d000042:s000003`

The published `WHO 18` model identifies three address families:

| Family | `WHERE` form | Published index range | Examples |
| --- | --- | --- | --- |
| Stop&Go | `1N` | `N = 1..127` | Stop&Go protection/control devices |
| Energy measurement / central unit | `5N` | `N = 1..255` | F520, F523, 3522 and corresponding Legrand devices |
| Energy Management actuator | `7N#0` | `N = 1..255` | F522, F523 and corresponding Legrand devices |

See [Addressing](addressing.md) for the implications of these forms.

### Operation classes

Section ID: `ownkb:section:d000042:s000004`

`WHO 18` uses all three principal functional frame patterns:

| Operation | General form |
| --- | --- |
| Command | `*18*WHAT*WHERE##` |
| `DIMENSION` request | `*#18*WHERE*DIMENSION##` |
| `DIMENSION` response/event | `*#18*WHERE*DIMENSION*VALUE...##` |
| `DIMENSION` setup/write | `*#18*WHERE*#DIMENSION...*VALUE...##` |

Several operations parameterize `WHAT` or `DIMENSION` using `#`. Those parameters are part of the operation grammar and must be preserved by parsers and encoders.

### Measurement model

Section ID: `ownkb:section:d000042:s000005`

Provenance cues: `specification`

Energy Management separates instantaneous values from accumulated and historical values. `DIMENSION 113` reports active power in watts. Totalizer operations expose accumulated values, while `DIMENSION 511..514` return time-series data for daily and monthly graphics. The published specification labels several accumulated values as â€œWattâ€; where the frame description explicitly identifies energy since reset it uses Wh. Implementations should preserve the published field semantics rather than silently normalizing units from the identifier alone.

### Event model

Section ID: `ownkb:section:d000042:s000006`

Many `WHO 18` values can arrive both as direct responses and as events. Actuator state, totalizer state, differential-current level, active power, and Stop&Go status all have event forms. Clients maintaining state should therefore process `DIMENSION` events independently of whether they initiated the corresponding request.

Automatic active-power reporting is configured with `DIMENSION 1200`. Historical-series commands similarly cause a sequence of `DIMENSION 511..514` event frames rather than a single scalar response.

### Relationship to other energy systems

Section ID: `ownkb:section:d000042:s000007`

`WHO 18` is distinct from [`WHO 3`](../who-3-load-management/) Load Management and [`WHO 11`](../who-11-energy-distribution/) Energy Distribution. Their `WHAT`, `WHERE`, and `DIMENSION` namespaces are not interchangeable.

For common frame syntax, see [Protocol](../../protocol/).

# Document: ownkb:document:d000043

Source path: `functional/who-18-energy-management/addressing.md`
Namespace context: `who:18`
Area: `functional`

## Addressing

Section ID: `ownkb:section:d000043:s000001`

`WHO 18` encodes the Energy Management device family in `WHERE`. Address parsing must therefore preserve the complete syntactic form rather than treating `WHERE` as an untyped device number.

### Published `WHERE` forms

Section ID: `ownkb:section:d000043:s000002`

| `WHERE` | Device family | Index |
| --- | --- | --- |
| `1N` | Stop&Go | `N = 1..127` |
| `5N` | Energy Management central unit, pulse counter, power meter | `N = 1..255` |
| `7N#0` | Energy Management actuator | `N = 1..255` |

The published examples associate the `5N` family with devices including BTicino F520/F523/3522 and the `7N#0` family with Energy Management actuators including F522/F523.

### Family-specific operations

Section ID: `ownkb:section:d000043:s000003`

The address prefix is not merely routing metadata. It constrains the operation set:

- Stop&Go addresses use automatic-reset commands and `DIMENSION 250..263` status functions.
- `5N` measurement addresses expose power, accumulated energy and historical-series operations where supported by the target.
- `7N#0` actuator addresses expose actuator commands and `DIMENSION 71..73` state/information where supported.

A decoder should therefore resolve the `WHERE` family before interpreting the complete operation.

### Actuator suffix

Section ID: `ownkb:section:d000043:s000004`

Cautions: `must not`

The actuator form includes the literal `#0` suffix: `7N#0`. The suffix is part of the published address grammar and must not be discarded by integer conversion or generic normalization.

### Discovery

Section ID: `ownkb:section:d000043:s000005`

Provenance cues: `specification`

The published `WHO 18` functional specification defines direct device addressing but does not define a general broadcast inventory request equivalent to the Lighting general-status query. Device discovery should not be invented from the existence of the `N` ranges.

The published ranges describe valid address spaces, not proof that every index is populated. Software that needs to probe functional Energy Management addresses must distinguish â€œaddress can existâ€ from â€œdevice is present.â€

See [`WHAT` Reference](what.md) for command applicability and [`DIMENSION` Reference](dimensions.md) for family-specific data operations.

# Document: ownkb:document:d000044

Source path: `functional/who-18-energy-management/dimensions.md`
Namespace context: `who:18`
Area: `functional`

## `DIMENSION` Reference

Section ID: `ownkb:section:d000044:s000001`

`WHO 18` relies heavily on `DIMENSION` operations. They cover instantaneous power, accumulated energy, historical time series, Energy Management actuator state, totalizers, differential-current information, Stop&Go state, and automatic update configuration.

### Identifier table

Section ID: `ownkb:section:d000044:s000002`

| `DIMENSION` | Meaning |
| --- | --- |
| `51` | Energy/unit totalizer |
| `52` | Energy/unit per month |
| `53` | Partial totalizer for current month |
| `54` | Partial totalizer for current day |
| `71` | Actuator information |
| `72` | Totalizers |
| `73` | Differential-current level |
| `113` | Active power |
| `250` | Complete Stop&Go status mask |
| `251` | Stop&Go open/closed |
| `252` | Stop&Go failure/no failure |
| `253` | Stop&Go blocked/not blocked |
| `254` | Stop&Go open for neutral-related short circuit |
| `255` | Stop&Go opened for ground fault |
| `256` | Stop&Go open for maximum-voltage condition |
| `257` | Stop&Go self-test disabled/enabled |
| `258` | Stop&Go automatic reset off/on |
| `259` | Stop&Go check off/on |
| `260` | Stop&Go waiting for closing |
| `261` | Stop&Go first 24 hours of opening |
| `262` | Stop&Go downstream power failure |
| `263` | Stop&Go upstream power failure |
| `511` | Daily hourly historical series |
| `512` | Monthly-average hourly historical series |
| `513` | Current-year daily monthly series |
| `514` | Previous-year daily monthly series |
| `1200` | Automatic update configuration / termination |

The value tuple and units are `DIMENSION`-specific. Numeric similarity does not imply a shared schema.

### Power and accumulated energy

Section ID: `ownkb:section:d000044:s000003`

#### `DIMENSION 113` - active power

Section ID: `ownkb:section:d000044:s000004`

Request: `*#18*WHERE*113##`

Response/event: `*#18*WHERE*113*Val##`

`Val` is active power in watts. `DIMENSION 113` is also the event payload used when automatic active-power reporting is enabled through `DIMENSION 1200`.

#### `DIMENSION 51` - energy/unit totalizer

Section ID: `ownkb:section:d000044:s000005`

Provenance cues: `specification`

Request: `*#18*WHERE*51##`

Response/event: `*#18*WHERE*51*Val##`

The published specification describes `Val` as the energy/unit totalizer value and labels its unit as Watt. This terminology is preserved rather than silently correcting the wire model from the word â€œtotalizer.â€

#### `DIMENSION 52` - monthly energy/unit totalizer

Section ID: `ownkb:section:d000044:s000006`

Request: `*#18*WHERE*52#Y#M##`

Response/event: `*#18*WHERE*52#Y#M*Val##`

`Y` is the year in two-digit `yy` form and `M` is the month.

#### `DIMENSION 53` - current-month partial totalizer

Section ID: `ownkb:section:d000044:s000007`

Request: `*#18*WHERE*53##`

Response/event: `*#18*WHERE*53*Val##`

#### `DIMENSION 54` - current-day partial totalizer

Section ID: `ownkb:section:d000044:s000008`

Request: `*#18*WHERE*54##`

Response/event: `*#18*WHERE*54*Val##`

`DIMENSION 51..54` are scalar totalizer operations. They are distinct from the multi-frame historical series under `DIMENSION 511..514`.

### Energy Management actuator information

Section ID: `ownkb:section:d000044:s000009`

#### `DIMENSION 71` - actuator status

Section ID: `ownkb:section:d000044:s000010`

Provenance cues: `source`

Request: `*#18*WHERE*71##`

Response/event: `*#18*WHERE*71*disabled*forcing*threshold*protection*phase*advanced##`

The six fields are positional.

| Field | Value | Meaning |
| --- | --- | --- |
| `disabled` | `0` | Enabled |
| `disabled` | `1` | Disabled |
| `forcing` | `0` | Not forced |
| `forcing` | `1` | Forced |
| `threshold` | `0` | Above threshold |
| `threshold` | `1` | Below threshold |
| `protection` | `0` | Not in protection |
| `protection` | `1` | Protection |
| `phase` | `0` | Disable of other phase |
| `phase` | `1` | Disable of local phase |
| `advanced` | `1` | Advanced |
| `advanced` | `2` | Basic |

The published event section contains inconsistent wording for `forcing`, while the request/response definition states `1 = Forced`, `0 = Not Forced`. The request/response definition is retained as the field semantics; the source discrepancy is not converted into a second state model.

#### `DIMENSION 72` - totalizer state

Section ID: `ownkb:section:d000044:s000011`

Request: `*#18*WHERE*72#Tot_N##`

Response/event: `*#18*WHERE*72#Tot_N*Energy*D*M*Y*H*m##`

| Field | Meaning |
| --- | --- |
| `Tot_N` | Totalizer number, `1..2` |
| `Energy` | Energy accumulated since reset, in Wh |
| `D` | Day of last reset |
| `M` | Month of last reset |
| `Y` | Year of last reset |
| `H` | Hour of last reset |
| `m` | Minute of last reset |

This operation couples the accumulated value with the timestamp of its reset boundary.

#### `DIMENSION 73` - differential-current level

Section ID: `ownkb:section:d000044:s000012`

Provenance cues: `specification`

Request: `*#18*WHERE*73##`

Response/event: `*#18*WHERE*73*level##`

The published range for `level` is `1..3`. The public specification does not assign a more detailed semantic label to each individual numeric level, so those meanings remain unspecified.

### Stop&Go status

Section ID: `ownkb:section:d000044:s000013`

Stop&Go exposes both a complete 13-bit state and individual one-bit `DIMENSION` values.

#### `DIMENSION 250` - complete status mask

Section ID: `ownkb:section:d000044:s000014`

Request: `*#18*WHERE*250##`

Response/event: `*#18*WHERE*250*MASC##`

`MASC` is a 13-bit mask ordered `b13...b1`.

| Bit | Individual `DIMENSION` | State when `1` |
| --- | --- | --- |
| `b1` | `251` | Open |
| `b2` | `252` | Failure |
| `b3` | `253` | Blocked |
| `b4` | `254` | Open for neutral-related short-circuit condition |
| `b5` | `255` | Opened for ground fault |
| `b6` | `256` | Open for maximum-voltage condition |
| `b7` | `257` | Self-test disabled |
| `b8` | `258` | Automatic reset off |
| `b9` | `259` | Check off |
| `b10` | `260` | Waiting for closing |
| `b11` | `261` | First 24 hours of opening |
| `b12` | `262` | Downstream power failure |
| `b13` | `263` | Upstream power failure |

#### Individual Stop&Go flags

Section ID: `ownkb:section:d000044:s000015`

Each `DIMENSION 251..263` can be requested independently using `*#18*WHERE*DIMENSION##` and returns one bit as `*#18*WHERE*DIMENSION*bN##`.

| `DIMENSION` | `1` | `0` |
| --- | --- | --- |
| `251` | Open | Closed |
| `252` | Failure | No failure |
| `253` | Blocked | Not blocked / closed state |
| `254` | Open for specified short-circuit condition | Closed |
| `255` | Opened for ground fault | Closed |
| `256` | Open for maximum-voltage condition | Closed |
| `257` | Self-test disabled | Self-test enabled |
| `258` | Automatic reset off | Automatic reset on |
| `259` | Check off | Check on |
| `260` | Waiting for closing | Closed |
| `261` | First 24 hours of opening | Closed |
| `262` | Downstream power failure | No downstream failure |
| `263` | Upstream power failure | No upstream failure |

A Stop&Go event can expose the complete mask and/or individual status frames. State consumers should therefore be able to merge both representations.

### Historical series

Section ID: `ownkb:section:d000044:s000016`

Historical operations return sequences of frames. The `#` parameters attached to the `DIMENSION` identify the requested period; `Tag` identifies a point within the series.

#### `DIMENSION 511` - daily hourly series

Section ID: `ownkb:section:d000044:s000017`

Provenance cues: `source`

Request: `*#18*WHERE*511#M#D##`

Data frames: `*#18*WHERE*511#M#D*Tag*Val##`

| `Tag` | Meaning |
| --- | --- |
| `1..24` | Hourly measure |
| `25` | Daily total |

The published source renders the unit as â€œWatt/hâ€; the operation represents the daily energy-history series. The same sequence can be initiated by `WHAT 57#M#D`.

#### `DIMENSION 512` - monthly-average hourly series

Section ID: `ownkb:section:d000044:s000018`

Data frame: `*#18*WHERE*512#M*Tag*Val##`

Tags `1..24` identify hourly measures averaged over the selected month. Tag `25` carries the monthly-average total/unit value defined by the published protocol. The sequence is initiated by `WHAT 58#M`.

#### `DIMENSION 513` - current-year monthly series

Section ID: `ownkb:section:d000044:s000019`

Data frame: `*#18*WHERE*513#M*Tag*Val##`

`Tag` identifies the day, `1..31`. The series represents daily values for the selected month in the current-year monthly graph model. It is initiated by `WHAT 59#M`.

#### `DIMENSION 514` - previous-year monthly series

Section ID: `ownkb:section:d000044:s000020`

Data frame: `*#18*WHERE*514#M*Tag*Val##`

`Tag` identifies the measure/day, `1..31`. The series is used for the previous-year comparison graph and is initiated by `WHAT 510#M`.

### `DIMENSION 1200` - automatic active-power updates

Section ID: `ownkb:section:d000044:s000021`

`DIMENSION 1200` configures automatic reporting.

Start/update form: `*#18*WHERE*#1200#Type*Time##`

| Field | Meaning |
| --- | --- |
| `Type` | Energy type; published value `1` = active power |
| `Time` | Update/change reporting parameter in minutes, `1..255` |

After configuration, active-power events are reported as `*#18*WHERE*113*Val##`.

The published description states that `Time` indicates after how many minutes consumption/status is sent when it changes. It should therefore be treated as the protocol's update parameter rather than generalized into an unconditional sampling interval.

Stop form: `*#18*WHERE*#1200#Type*0##`.

### Request, response and event symmetry

Section ID: `ownkb:section:d000044:s000022`

Applicability cues: `applies to`

A significant part of `WHO 18` uses the same `DIMENSION` payload for direct responses and asynchronous event traffic. This applies to active power, scalar totalizers, actuator status, totalizer state, differential-current level and Stop&Go status.

Parsers should decode these frames by `WHO`, `WHERE`, `DIMENSION` and payload shape rather than assuming that a given payload can only appear immediately after a request.

See [`WHAT` Reference](what.md) for command-driven historical transmission and actuator control, and [Addressing](addressing.md) for the device-family address grammar.

# Document: ownkb:document:d000045

Source path: `functional/who-18-energy-management/what.md`
Namespace context: `who:18`
Area: `functional`

## `WHAT` Reference

Section ID: `ownkb:section:d000045:s000001`

`WHO 18` uses ordinary and parameterized `WHAT` values for Stop&Go control, historical-series transmission, Energy Management actuator control, and totalizer reset.

### Commands

Section ID: `ownkb:section:d000045:s000002`

| `WHAT` | Meaning | Parameters / notes |
| --- | --- | --- |
| `26` | Activate automatic reset | Stop&Go |
| `27` | Deactivate automatic reset | Stop&Go |
| `57` | Start daily hourly totalizer series | `57#M#D` |
| `58` | Start monthly-average hourly series | `58#M` |
| `59` | Start current-year monthly series | `59#M` |
| `510` | Start previous-year monthly series | `510#M` |
| `71` | Enable actuator | Energy Management actuator |
| `73` | Force actuator | Optional `#Time` parameter |
| `74` | End forced actuator | Energy Management actuator |
| `75` | Reset totalizer | `75#Tot_N` |

### Stop&Go automatic reset

Section ID: `ownkb:section:d000045:s000003`

`WHAT 26` enables automatic reset and `WHAT 27` disables it. They apply to Stop&Go targets selected through the `1N` address family.

The command forms are `*18*26*WHERE##` and `*18*27*WHERE##`. Successful command processing is acknowledged with `ACK`.

Stop&Go status is read separately through `DIMENSION 250..263`; see [`DIMENSION` Reference](dimensions.md).

### Historical-series commands

Section ID: `ownkb:section:d000045:s000004`

The four commands `WHAT 57`, `58`, `59`, and `510` start transmission of data intended for graphical histories. They are an enumerated set, not the inclusive interval `57..510`. The command parameters select the requested calendar period; the returned data is carried by `DIMENSION 511..514` event frames.

| Command | Parameters | Resulting `DIMENSION` |
| --- | --- | --- |
| `57#M#D` | Month, day | `511` |
| `58#M` | Month | `512` |
| `59#M` | Month | `513` |
| `510#M` | Month | `514` |

This is a multi-frame operation. The `WHAT` command starts transmission; it does not itself carry the historical values.

#### Daily hourly series

Section ID: `ownkb:section:d000045:s000005`

`*18*57#M#D*WHERE##` starts the daily series. `DIMENSION 511` then reports tags `1..24` for the hourly measures and tag `25` for the daily total.

#### Monthly-average hourly series

Section ID: `ownkb:section:d000045:s000006`

`*18*58#M*WHERE##` starts the monthly-average series. `DIMENSION 512` uses tags `1..24` for hourly monthly averages and tag `25` for the monthly average total/unit value defined by the published protocol.

#### Current-year monthly graph

Section ID: `ownkb:section:d000045:s000007`

`*18*59#M*WHERE##` starts transmission through `DIMENSION 513`. The tag identifies the day, `1..31`.

#### Previous-year comparison

Section ID: `ownkb:section:d000045:s000008`

`*18*510#M*WHERE##` starts transmission through `DIMENSION 514`. The tag identifies the measure/day, `1..31`.

### Actuator commands

Section ID: `ownkb:section:d000045:s000009`

#### Enable

Section ID: `ownkb:section:d000045:s000010`

`*18*71*WHERE##` enables the addressed Energy Management actuator.

#### Force for a specified time

Section ID: `ownkb:section:d000045:s000011`

Cautions: `avoid`
Provenance cues: `evidence`

`*18*73#Time*WHERE##` forces the actuator for the requested duration. The published `Time` field is expressed in tens of minutes and accepts values `1..254`.

The published prose also describes the resulting interval as beginning at 10 minutes. Its stated upper-duration prose is inconsistent with a literal `1..254` ten-minute encoding; implementations should preserve the encoded range and avoid deriving a corrected maximum duration without additional evidence.

#### Force for default time

Section ID: `ownkb:section:d000045:s000012`

`*18*73*WHERE##` omits the `Time` parameter and requests the device's default forcing duration.

#### End forcing

Section ID: `ownkb:section:d000045:s000013`

`*18*74*WHERE##` ends the forced state.

The current actuator state can be read through `DIMENSION 71`.

### Reset totalizer

Section ID: `ownkb:section:d000045:s000014`

`*18*75#Tot_N*WHERE##` resets the selected totalizer. `Tot_N` is `1` or `2`.

The state of a totalizer, including accumulated energy and last-reset timestamp, is available through `DIMENSION 72#Tot_N`.

See [Addressing](addressing.md) for valid target families and [`DIMENSION` Reference](dimensions.md) for returned values.

# Document: ownkb:document:d000046

Source path: `functional/who-18-energy-management/zigbee-variant.md`
Namespace context: `who:18`
Area: `functional`

## ZigBee Variant

Section ID: `ownkb:section:d000046:s000001`

Applicability cues: `revision`, `scs`, `version`, `zigbee`
Uncertainty: `unresolved`
Provenance cues: `evidence`, `source`, `specification`

The ZigBee OpenWebNet version 4.0 specification defines an interface-specific `WHO 18` Energy Management surface for ZigBee products. Its command and `DIMENSION` vocabulary differs materially from the SCS-oriented `WHO 18` reference, despite sharing the same namespace number.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. Its Confidential footer and unresolved public-release provenance remain recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The material below is **specification evidence for this interface revision**.

The source section heading says "Automation WHO = 18", while its prose and operation labels describe Energy Management parameters. The encyclopedia preserves that editorial inconsistency in the reconciliation record rather than treating "Automation" as a second functional meaning.

### Reset command - unresolved source conflict

Section ID: `ownkb:section:d000046:s000002`

Applicability cues: `scs`, `zigbee`
Provenance cues: `evidence`, `source`

The `WHO 18` summary table lists:

| `WHAT` | Summary-table action |
| --- | --- |
| `0` | Reset |

The immediately following detailed Reset definition instead sends:

`*18*75*WHERE#9##`

and describes it as resetting the energy counter of ZigBee Devices.

The source therefore assigns two different `WHAT` values to Reset. Neither is promoted as an unqualified ZigBee reset value. The SCS-oriented use of `WHAT 75` is not independent evidence that the ZigBee detailed frame is correct because the two protocol variants cannot be equated by numeric identity.

The detailed Reset form supports both ZigBee unicast and broadcast `WHERE` forms and uses the interface-specific acknowledgement model.

### `DIMENSION` table

Section ID: `ownkb:section:d000046:s000003`

Applicability cues: `scs`, `zigbee`
Cautions: `do not`
Provenance cues: `documentation`, `evidence`, `source`

The ZigBee source defines:

| `DIMENSION` | Source action | Relationship to current SCS-oriented `WHO 18` documentation |
| --- | --- | --- |
| `11` | Voltage | ZigBee-specific identifier in the current encyclopedia |
| `17` | Current | ZigBee-specific identifier in the current encyclopedia |
| `51` | Energy | Same numeric identifier as an SCS totalizer operation, but materially different source semantics |
| `112` | Frequency | ZigBee-specific identifier in the current encyclopedia |
| `113` | Active Power | Same source label as an SCS operation; variant applicability and payload evidence remain separate |
| `114` | Active Power Total | ZigBee-specific identifier in the current encyclopedia |
| `115` | Threshold Max Active Power | ZigBee-specific identifier in the current encyclopedia |
| `117` | Reactive Power | ZigBee-specific identifier in the current encyclopedia |
| `1200` | Report Power | Same numeric identifier as an SCS reporting operation, but different documented syntax and time units |

For `DIMENSION 11`, `17`, `51`, `112`, `113`, `114`, `115`, and `117`, the request form is:

`*#18*WHERE#9*DIMENSION##`

and the response form is:

`*#18*WHERE#9*DIMENSION*VALUE##`

The detailed definitions describe `VALUE` as the named quantity "in decimal". They do not define a scale, signedness rule, or physical unit for these values. The encyclopedia therefore preserves the quantity names without importing units or scaling from the SCS-oriented `WHO 18` reference.

The detailed request tables show unicast product addressing for these measurements. The source does not establish a broadcast measurement request merely because Reset permits broadcast addressing.

### Frequency/Energy source conflict

Section ID: `ownkb:section:d000046:s000004`

Uncertainty: `contradiction`
Provenance cues: `evidence`, `source`

The use case titled "Get Frequency" on PDF page 53 sends `DIMENSION 51` and receives `DIMENSION 51`.

The `DIMENSION` table and detailed definitions on pages 54 and 55 instead define:

- `DIMENSION 51` as Energy;
- `DIMENSION 112` as Frequency.

This is a material source-internal contradiction. The encyclopedia preserves both locations. The mutually consistent table and detailed definitions are documented as their stated meanings, but the conflicting use case prevents treating the source as contradiction-free evidence for the Frequency/Energy mapping.

### `DIMENSION 1200` - Report Power

Section ID: `ownkb:section:d000046:s000005`

Applicability cues: `scs`, `zigbee`
Cautions: `must not`
Provenance cues: `source`

The ZigBee source defines the command form:

`*#18*WHERE#9*1200#TYPE*TIME##`

with:

| Field | ZigBee source definition |
| --- | --- |
| `TYPE` | `1` = active power |
| `TIME` | `0..255` seconds |

The section defines acknowledgement handling for this command but does not show the later power-report frame or explicitly state that `DIMENSION 113` is the resulting asynchronous payload. That relationship must not be inferred solely from the names "Report Power" and "Active Power".

This grammar materially differs from the SCS-oriented `DIMENSION 1200` operation, which the current encyclopedia documents with a write marker and a time value in minutes. Variant selection is therefore required before encoding or decoding `DIMENSION 1200`.

### Addressing and acknowledgements

Section ID: `ownkb:section:d000046:s000006`

Applicability cues: `scs`, `zigbee`
Provenance cues: `source`

The ZigBee Energy Management section uses the [ZigBee product-and-Unit `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing), not the SCS `1N`, `5N`, or `7N#0` Energy Management address families.

Measurement requests and Report Power use the unicast form shown by the source. Reset additionally documents broadcast addressing. `ACK`, `NACK`, and BUSY/NACK follow the common ZigBee-interface behavior.

### Evidence limits

Section ID: `ownkb:section:d000046:s000007`

Applicability cues: `scs`, `version`, `zigbee`
Provenance cues: `evidence`, `source`

The ZigBee version 4.0 section does not establish the SCS Stop&Go command family, SCS historical-series operations, SCS actuator-control model, or SCS `DIMENSION 250..263` and `511..514` surfaces for this interface. Their absence is not proof that no ZigBee implementation can expose additional operations.

The source does not provide sufficient scaling or unit information to turn the decimal measurement payloads into implementation-ready physical quantities beyond their named properties. That remains an explicit evidence gap.

See [`WHAT` Reference](what.md) and [`DIMENSION` Reference](dimensions.md) for the SCS-oriented Energy Management model, and [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for common ZigBee transport, addressing, and acknowledgement rules.

# Document: ownkb:document:d000047

Source path: `functional/who-19-interface/README.md`
Namespace context: `who:19`
Area: `functional`

## `WHO 19` - Interface

Section ID: `ownkb:section:d000047:s000001`

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 19` as Interface.

### Evidence boundary

Section ID: `ownkb:section:d000047:s000002`

Uncertainty: `unknown`
Provenance cues: `evidence`

The implementation corpus establishes the namespace, but the currently integrated evidence does not support a complete authoritative `WHAT`, `WHERE`, or `DIMENSION` vocabulary. This is a meaningful protocol result: `WHO 19` is known to exist, while the semantics of unsupported numeric fields remain unknown.

### Implementation guidance

Section ID: `ownkb:section:d000047:s000003`

Uncertainty: `unknown`
Provenance cues: `evidence`

Generic parsers should retain `WHO 19` frames losslessly even when a field is not yet decoded. Unknown `WHAT`, `WHERE`, parameters, and `DIMENSION` values should be represented as raw protocol values rather than mapped to nearby functional systems.

In particular, the name Interface does not establish that `WHO 19` uses the F422 advanced-address rules or any other specific interface-device grammar. Such a mapping requires direct implementation or wire evidence.

Future additions should distinguish direct MyHOME_Suite definitions from inferred behavior according to the repository provenance rules.

# Document: ownkb:document:d000048

Source path: `functional/who-2-automation/README.md`
Namespace context: `who:2`
Area: `functional`

## `WHO 2` - Automation

Section ID: `ownkb:section:d000048:s000001`

Applicability cues: `scs`, `zigbee`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `specification`

`WHO 2` defines the OpenWebNet Automation system. It covers movement commands, shutter state, relative and absolute positioning, priority handling, and Automation-specific addressing.

The published OpenWebNet Automation specification defines the functional command, addressing, and advanced shutter model. The MyHOME_Suite data structures complement that model with the address rules and frame forms used by the application. Device configuration is represented separately by the MyHOME_Suite catalogue model; diagnostic discovery and configuration reading belong to the diagnostic protocol rather than to `WHO 2` functional traffic.

The supplied [ZigBee Interface](../../protocol/zigbee-interface.md) also exposes `WHO 2`, but with a different transport, `WHERE` grammar, narrower position payloads, and a different `DIMENSION 11` write form. Its UP-value conflict remains unresolved. See the [ZigBee Automation Variant](zigbee-variant.md); this SCS-oriented reference does not settle the variant by namespace equality.

### Reference

Section ID: `ownkb:section:d000048:s000002`

Applicability cues: `zigbee`
Provenance cues: `source`

| Subject | Page |
| --- | --- |
| Commands, movement and priority | [`WHAT` Reference](what.md) |
| `WHERE` forms and address scopes | [Addressing](addressing.md) |
| Shutter state and absolute positioning | [`DIMENSION` Reference](dimensions.md) |
| ZigBee-specific Automation semantics and source conflicts | [ZigBee Automation Variant](zigbee-variant.md) |

### Functional model

Section ID: `ownkb:section:d000048:s000003`

Applicability cues: `scs`

Ordinary movement commands use `*2*WHAT*WHERE##`. Advanced shutter state and absolute positioning use `DIMENSION` frames under the same `WHO` namespace.

`WHO 2` must be interpreted as a system-scoped protocol namespace: the meaning of `WHAT`, `WHERE`, `DIMENSION`, and their parameters is specific to Automation. In particular, numeric values used inside `DIMENSION 10` shutter state are not automatically additional command `WHAT` values.

Automation uses the SCS `A`/`PL` addressing family also used by Lighting, but the protocol semantics remain scoped to `WHO 2`. MyHOME_Suite represents the corresponding point-to-point, environment, and advanced address forms through its `OPEN.db` address-rule definitions.

For the common OpenWebNet frame language, see [Protocol](../../protocol/). For the Device â†’ Module â†’ Object â†’ Configuration model used to describe physical Automation devices, see [Device Model](../../device-model/).

# Document: ownkb:document:d000049

Source path: `functional/who-2-automation/addressing.md`
Namespace context: `who:2`
Area: `functional`

## Addressing

Section ID: `ownkb:section:d000049:s000001`

Applicability cues: `scs`

`WHO 2` uses the SCS Automation addressing model. `WHERE` selects a general scope, environment, point-to-point light point, group, or a point reached through a local-bus interface.

### `WHERE` forms

Section ID: `ownkb:section:d000049:s000002`

| Scope | `WHERE` form | Values |
| --- | --- | --- |
| General | `0` | Entire Automation system |
| Environment | `A` | `00`, `1..9`, or `100` as defined by the published Automation grammar |
| Point to point | `APL` | Address ranges depend on `A` |
| Group | `#GR` | `GR = 1..255` |
| Local bus | `APL#4#INTERFACE` | `INTERFACE = [0-1][1-9]` (`01..09`, `11..19`) |

### Point-to-point ranges

Section ID: `ownkb:section:d000049:s000003`

Provenance cues: `source`, `specification`

The published grammar constrains `PL` according to the `A` representation:

| `A` | Allowed `PL` |
| --- | --- |
| `00` | `01..15` |
| `1..9` | `1..9` |
| `10` | `01..15` |
| `01..09` | `10..15` |

These forms preserve significant leading zeroes. An Automation address should therefore be parsed according to the applicable grammar rather than converted to an integer before its address class is known. The published `WHO 2` table explicitly defines the local-bus form for point-to-point `APL`; its `interface` field is the same routing-interface concept called `Int` by the `WHO 1` specification. Unlike the `WHO 1` Lighting material, the published Automation table does not explicitly establish `#3` variants or local-bus General, Area, or Group forms. See the [canonical addressing reference](../../protocol/addressing.md#level-4--local-bus) for the cross-source distinction.

### Event expansion

Section ID: `ownkb:section:d000049:s000004`

Commands addressed to a group, environment, or the general scope can produce event/status frames for the individual Automation Objects affected by the operation. A group command can additionally produce a frame retaining the group `WHERE` itself.

The MyHOME_Suite `OPEN.db` address-rule definitions represent the same `A`/`PL` address family through system-specific point-to-point, environment, and advanced rules.

See [`WHAT` Reference](what.md) for movement commands, [`DIMENSION` Reference](dimensions.md) for advanced shutter state/position data, and [Addressing](../../protocol/addressing.md) for the common system-scoped addressing model.

# Document: ownkb:document:d000050

Source path: `functional/who-2-automation/dimensions.md`
Namespace context: `who:2`
Area: `functional`

## `DIMENSION` Reference

Section ID: `ownkb:section:d000050:s000001`

`WHO 2` uses `DIMENSION 10` for advanced shutter state and `DIMENSION 11` for absolute positioning. The published protocol defines the payload semantics; MyHOME_Suite implementation data confirms the parameterized absolute-position operation used by the application.

| `DIMENSION` | Function | Direction |
| --- | --- | --- |
| `10` | Shutter status | Request / response / event |
| `11` | Go to level | Write |

### `DIMENSION 10` - shutter status

Section ID: `ownkb:section:d000050:s000002`

Request: `*#2*WHERE*10##`.

The status payload contains four values, in order: `shutterStatus`, `shutterLevel`, `shutterPriority`, `shutterInfo`.

The corresponding status/event form is `*#2*WHERE*10*SHUTTER_STATUS*SHUTTER_LEVEL*SHUTTER_PRIORITY*SHUTTER_INFO##`.

#### Shutter status

Section ID: `ownkb:section:d000050:s000003`

Cautions: `must not`
Provenance cues: `evidence`

| Value | Meaning |
| --- | --- |
| `10` | Stop |
| `11` | Up |
| `12` | Down |
| `13` | Step-by-step up |
| `14` | Step-by-step down |

These are `DIMENSION 10` state values. Values `13` and `14` therefore describe step-by-step shutter state and must not be promoted to ordinary `WHO 2` command functions without separate evidence.

#### Shutter level

Section ID: `ownkb:section:d000050:s000004`

Uncertainty: `unknown`

| Value | Meaning |
| --- | --- |
| `0` | Fully closed |
| `1..99` | Current position (%) |
| `100` | Fully open |
| `255` | Unknown position |

The level is the shutter's absolute position model. It is distinct from the relative shutter-step parameter used by advanced Up/Down commands.

#### Shutter priority

Section ID: `ownkb:section:d000050:s000005`

`shutterPriority` carries the encoded priority state associated with the advanced shutter. The Automation priority model distinguishes Safety, High, and Medium priority flags. The same priority model participates in advanced movement commands and the parameterized absolute-position operation; see [`WHAT` Reference](what.md).

#### Shutter information

Section ID: `ownkb:section:d000050:s000006`

| Value | Meaning |
| --- | --- |
| `0` | Normal |
| `12` | PUL + disabled |
| `13` | Disabled |
| `14` | Command not executed |
| `15` | PUL |

For general, environment, or group requests, the server can return one `DIMENSION 10` status frame for each Automation Object in the addressed scope. This expansion is part of the functional addressing behavior rather than a change to the four-value payload.

### `DIMENSION 11` - go to level

Section ID: `ownkb:section:d000050:s000007`

`DIMENSION 11` writes an absolute shutter position. The published write form is `*#2*WHERE*#11#SHUTTER_PRIORITY*SHUTTER_LEVEL##`.

The MyHOME_Suite functional data uses the same parameterized operation. A concrete application form is `*#2*WHERE*#11#001*LEVEL##`, where the parameter attached to `DIMENSION 11` carries the priority field and `LEVEL` carries the target position. The parameter must therefore be preserved by encoders rather than treating the operation as an unparameterized `DIMENSION 11` write.

#### Target level

Section ID: `ownkb:section:d000050:s000008`

Uncertainty: `unknown`

| Value | Meaning |
| --- | --- |
| `0` | Fully closed |
| `1..99` | Target position (%) |
| `100` | Fully open |

`255`, used by `DIMENSION 10` to report an unknown current position, is not a target position.

#### Resulting state traffic

Section ID: `ownkb:section:d000050:s000009`

An absolute-position operation changes shutter state over time rather than representing an instantaneous scalar assignment. Event traffic can therefore include the `DIMENSION 11` operation, `DIMENSION 10` state updates, movement events, and a final stop/state update when the requested level is reached.

The exact sequence visible to a client depends on the addressed device and event propagation; clients should use the resulting state reports rather than assuming that the write frame alone represents the final physical state.

See [Addressing](addressing.md) for scope expansion rules and [`DIMENSION`](../../protocol/dimensions.md) for the common `DIMENSION` frame classes.

# Document: ownkb:document:d000051

Source path: `functional/who-2-automation/what.md`
Namespace context: `who:2`
Area: `functional`

## `WHAT` Reference

Section ID: `ownkb:section:d000051:s000001`

Provenance cues: `specification`

`WHAT` in `WHO 2` expresses Automation movement commands. The published specification distinguishes base motor commands, advanced parameterized commands, and translated event reports.

### Base commands

Section ID: `ownkb:section:d000051:s000002`

| `WHAT` | Function | Frame |
| --- | --- | --- |
| `0` | Stop | `*2*0*WHERE##` |
| `1` | Up | `*2*1*WHERE##` |
| `2` | Down | `*2*2*WHERE##` |

Collective commands can expand into events for the addressed scope and the individual affected Objects. Up/Down movement normally produces a later Stop event when the endpoint is reached.

### Advanced commands

Section ID: `ownkb:section:d000051:s000003`

| Leading `WHAT` | Function | Parameters |
| --- | --- | --- |
| `10` | Advanced Stop | priority; set/clear selector |
| `11` | Advanced Up | optional step; priority; set/clear selector |
| `12` | Advanced Down | optional step; priority; set/clear selector |

The exact `#`-parameterized form is part of `WHAT`; parsing only the leading number loses the requested step and priority operation.

#### Step

Section ID: `ownkb:section:d000051:s000004`

`1..99` requests the corresponding relative movement. An omitted/null value or `100` means movement to the endpoint for the selected direction.

#### Priority

Section ID: `ownkb:section:d000051:s000005`

The priority payload contains a set/clear selector and Safety, High, and Medium flags. A zero flag leaves that priority unchanged. This is a bit-selection operation, not a single ordinal priority number.

### Command-translation reports - `WHAT 1000`

Section ID: `ownkb:section:d000051:s000006`

Applicability cues: `gateway`
Cautions: `do not`
Provenance cues: `source`

The published Automation flows use `1000#INNER_WHAT...` when reporting translated commands for point targets. Base operations can appear as:

```text
*2*1000#INNER_WHAT*WHERE##
```

Advanced reports preserve their parameters, for example the inner operation, priority, set/clear selector, and target `WHERE`. Some tables in the source omit `WHERE` in individual rows while later rows include it; parsers should accept only forms corroborated by the actual gateway/device family and preserve the raw frame when the source is inconsistent.

Do not mistake `1000` for a movement state. It is a wrapper around another Automation operation.

### State values are not commands

Section ID: `ownkb:section:d000051:s000007`

Uncertainty: `not established`

Values `10..14` also appear as `DIMENSION 10` shutter-state values: Stop, Up, Down, step-by-step Up, and step-by-step Down. That value table is local to the `DIMENSION` payload. In particular, `13` and `14` are not established ordinary command `WHAT` values.

### Evidence basis

Section ID: `ownkb:section:d000051:s000008`

Provenance cues: `specification`

The command table, step and priority model, collective event behavior, and translation frames come from [`WHO 2` specification](../../sources/openwebnet-public/pdf/WHO_2.pdf). MyHOME Suite ScenarioDevices corroborates ordinary movement and absolute-position capability but does not redefine the published wire grammar.

See [`DIMENSION` Reference](dimensions.md), [Addressing](addressing.md), and the common [`WHAT` model](../../protocol/what.md).

# Document: ownkb:document:d000052

Source path: `functional/who-2-automation/zigbee-variant.md`
Namespace context: `who:2`
Area: `functional`

## ZigBee Variant

Section ID: `ownkb:section:d000052:s000001`

Applicability cues: `revision`, `scs`, `version`, `zigbee`
Uncertainty: `unresolved`
Provenance cues: `evidence`, `source`, `specification`

The ZigBee OpenWebNet version 4.0 specification defines a `WHO 2` Automation variant for shutter products on the Legrand serial ZigBee interface. The variant reuses the base Stop/Up/Down command family but uses the [ZigBee product-and-Unit `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing) and defines narrower `DIMENSION 10` and `11` payloads than the SCS-oriented Automation reference.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. Its Confidential footer and unresolved public-release provenance remain recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The material below is **specification evidence for this interface revision**.

### Base commands and source conflict

Section ID: `ownkb:section:d000052:s000002`

Applicability cues: `scs`, `version`, `zigbee`
Uncertainty: `contradiction`
Provenance cues: `source`

The detailed Automation section defines:

| `WHAT` | Detailed ZigBee meaning |
| --- | --- |
| `0` | Stop |
| `1` | Up |
| `2` | Down |

The use cases and detailed definitions in sections 9.1 through 9.3 consistently use `WHAT 1` for Up and `WHAT 2` for Down. However, the general frame examples on PDF page 11 label `*2*2*WHERE#9##` as Automation Up, both for unicast and broadcast.

This is a source-internal contradiction. The encyclopedia does not rewrite the page-11 examples or use them to redefine the detailed command table. A decoder or encoder that must interoperate with a specific interface should establish the applicable behavior independently before relying on the conflicting value.

The SCS-oriented Automation reference also defines advanced `WHAT 10..12` and command-translation `WHAT 1000`. Their absence from the ZigBee version 4.0 Automation section does not establish that no ZigBee implementation can support them.

### Acknowledgement and Supervisor behavior

Section ID: `ownkb:section:d000052:s000003`

Applicability cues: `scs`, `zigbee`
Cautions: `must not`
Provenance cues: `evidence`, `source`

Stop, Up, and Down use the interface-specific `ACK`, `NACK`, and BUSY/NACK behavior described in [ZigBee acknowledgement behavior](../../protocol/zigbee-interface.md#acknowledgement-behavior).

With Supervisor mode enabled through ZigBee `WHO 13`, the detailed command definitions show a server-originated command-state frame matching Stop, Up, or Down. The detailed Stop definition then shows a `DIMENSION 10` status frame; unlike the preceding `WHAT 0` report, that status frame is not explicitly labelled as conditional on Supervisor mode. The Up use case additionally shows a later Stop report when the shutter reaches its upper limit, followed by a `DIMENSION 10` status report with level `100`.

The source does not state whether the Stop-associated `DIMENSION 10` report is universal across supported shutters, so it is retained as documented sequence evidence rather than generalized into a mandatory rule. These ZigBee-interface behaviors must not be generalized to SCS Automation event ordering.

### `DIMENSION 10` - read position

Section ID: `ownkb:section:d000052:s000004`

Applicability cues: `scs`, `zigbee`
Cautions: `must not`
Uncertainty: `unknown`
Provenance cues: `source`

Request:

`*#2*WHERE#9*10##`

Response:

`*#2*WHERE#9*10*STATUS*LEVEL*PRIORITY*INFO##`

The ZigBee variant defines:

| Field | Values |
| --- | --- |
| `STATUS` | `10` Stop; `11` Up; `12` Down |
| `LEVEL` | `0` fully closed; `1..99` current position; `100` fully open; `255` unknown |
| `PRIORITY` | source states this is always `000` |
| `INFO` | source states this is always `0` |

The source says calibrated shutters can expose their position and that an uncalibrated shutter returns `LEVEL=255` for unknown position.

The SCS-oriented `DIMENSION 10` reference defines additional status values and richer priority/information semantics. Those SCS values must not be imported into the ZigBee payload merely because the dimension number and field names overlap.

### `DIMENSION 11` - move to position

Section ID: `ownkb:section:d000052:s000005`

Applicability cues: `scs`, `version`, `zigbee`
Provenance cues: `source`

The ZigBee write form is:

`*#2*WHERE#9*#11*LEVEL##`

`LEVEL` is `0..100`. The source states that the operation can be sent when shutter calibration has been completed.

This grammar materially differs from the SCS-oriented `DIMENSION 11` form, which carries a separate priority parameter before the target level. The ZigBee version 4.0 section does not define that priority parameter for `DIMENSION 11`.

### State request

Section ID: `ownkb:section:d000052:s000006`

Applicability cues: `zigbee`
Uncertainty: `contradiction`

The ZigBee Automation state request is:

`*#2*WHERE#9##`

The server returns an ordinary `WHO 2` state frame followed by `ACK`. The detailed request section defines states `0` Stop, `1` Up, and `2` Down, subject to the separate page-11 Up-value contradiction described above.

### Evidence limits

Section ID: `ownkb:section:d000052:s000007`

Applicability cues: `scs`, `version`, `zigbee`
Provenance cues: `source`

The ZigBee version 4.0 Automation section documents `WHAT 0..2`, `DIMENSION 10`, `DIMENSION 11`, and the general state request. It does not establish the broader SCS advanced-command or priority model for this interface.

Calibration is identified by the source as relevant to position availability and position writes, but the document does not define the calibration procedure itself as an OpenWebNet `WHO 2` operation. That underlying mechanism is outside this page.

See [`WHAT` Reference](what.md) and [`DIMENSION` Reference](dimensions.md) for the SCS-oriented Automation model, and [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for common ZigBee transport, addressing, and acknowledgement rules.

# Document: ownkb:document:d000053

Source path: `functional/who-22-sound-diffusion/README.md`
Namespace context: `who:22`
Area: `functional`

## `WHO 22` - Sound Diffusion

Section ID: `ownkb:section:d000053:s000001`

Provenance cues: `source`

`WHO 22` is the later Sound Diffusion / Multimedia dialect. It uses structured source, speaker, area, and general addresses, with operation parameters embedded in `WHAT`.

### Core parameters

Section ID: `ownkb:section:d000053:s000002`

Uncertainty: `appears`
Provenance cues: `source`

| Parameter | Published domain |
| --- | --- |
| Multimedia type | `1` voice; `2` right; `3` left; `4` stereo; `11` all sources |
| Source ID | `1..4` |
| Area / speaker point | `1..9` |
| Device state | `0` OFF; `1` ON |
| Frequency step | `1..15` |
| Modulation | `1` FM; `2` AM-LW; `3` AM-MW; `4` AM-SW |
| Stored station | `1..5` for F500; `1..15` for F500N |
| Track | `1..999` |
| Volume / volume step | absolute `0..31`; step `1..31` |
| Tone / balance value | `1..63` |
| 3D level | `0..10` |
| Loudness | `0` OFF; `1` ON |
| Preset | `2` normal, `3` dance, `4` pop, `5` rock, `6` classic, `7` techno, `8` party, `9` soft, `10` full bass, `11` full treble; `16..25` user defined |

The source describes frequency steps as `50`, `100`, â€¦ `750 Hz`; this appears unusually small for radio tuning. This reference preserves the published values without silently relabelling their unit.

### `WHAT`

Section ID: `ownkb:section:d000053:s000003`

Provenance cues: `source`

| `WHAT` | Meaning |
| --- | --- |
| `0` / `1` | Turn source or speaker OFF / ON |
| `2` | Source turned on |
| `3` / `4` | Increase / decrease volume |
| `5` / `6` | Search/tune toward higher / lower frequencies |
| `9` / `10` | Next / previous station |
| `11` / `12` | Next / previous track |
| `22` | Sliding request |
| `31` / `32` | Start / stop RDS message reporting |
| `33` | Store tuned frequency as a station |
| `34` | Turn amplifier ON using Follow Me |
| `35` | Turn amplifier ON using a specified source |
| `36` / `37` | Increment / decrement low tones |
| `38` / `39` | Increment / decrement mid tones |
| `40` / `41` | Increment / decrement high tones |
| `42` / `43` | Move balance right / left |
| `55` / `56` | Next / previous preset |

Most commands are parameterized. For example, source power uses `WHAT#MULTIMEDIA_TYPE#AREA`, while the target source remains in `WHERE`. A decoder must retain the entire `WHAT` field.

#### Frequency search

Section ID: `ownkb:section:d000053:s000004`

For `WHAT 5` and `6`, an empty step parameter requests automatic search; a supplied frequency-step value requests movement by that step. The flat `WHAT` table's wording for `6` is therefore incomplete by itself; the allowed-message flow establishes both modes.

### `WHERE`

Section ID: `ownkb:section:d000053:s000005`

Provenance cues: `source`

| Target | `WHERE` form |
| --- | --- |
| Source | `2#SOURCE_ID` |
| Speaker | `3#AREA#POINT` |
| Speaker area | `4#AREA` |
| General | `5#SENDER_ADDRESS` |
| All sources | `6` |

These are tagged target classes, not decimal numbers with punctuation. Keep the structure intact.

### `DIMENSION`

Section ID: `ownkb:section:d000053:s000006`

| `DIMENSION` | Meaning |
| --- | --- |
| `1` | Volume |
| `2` | High tones |
| `3` | Medium tones |
| `4` | Low tones |
| `5` | Frequency |
| `6` | Track/station |
| `7` | Play status |
| `11` | Frequency and station |
| `12` | Device state |
| `17` | Balance |
| `18` | 3D |
| `19` | Preset |
| `20` | Loudness |

Absolute `DIMENSION` state complements relative `WHAT` operations. Prefer reported values for state caches instead of reconstructing state from increments.

#### Payloads and concrete operations

Section ID: `ownkb:section:d000053:s000007`

Provenance cues: `source`

| Dimension | Report payload following the dimension |
| --- | --- |
| `1` | `VOLUME` |
| `2`, `3`, `4` | `TONE_VALUE` |
| `5` | `MODULATION*FREQUENCY` |
| `6` | `STATION_OR_TRACK` |
| `11` | `MODULATION*FREQUENCY*STATION_OR_TRACK` |
| `12` | `DEVICE_STATE*MULTIMEDIA_TYPE` |
| `17` | `BALANCE` |
| `18` | `3D_LEVEL` |
| `19` | `PRESET` |
| `20` | `LOUDNESS` |

The detailed flows additionally show RDS text under dimension `10` and equalizer reports under `21#1`, `21#2`, and `21#3`. The equalizer selectors carry bands `1..3`, `4..6`, and `7..8` respectively, separated by `*`. The source does not supply a complete RDS text encoding or band-value domain.

Examples with unambiguous separators in the detailed flows include:

| Operation | Frame |
| --- | --- |
| Increase speaker volume | `*22*3#VOLUME_STEP*3#AREA#POINT##` |
| Decrease speaker volume | `*22*4#VOLUME_STEP*3#AREA#POINT##` |
| Follow Me | `*22*34#MULTIMEDIA_TYPE#AREA*3#AREA#POINT##` |
| Select source and turn on speaker | `*22*35#4#AREA#SOURCE_ID*3#AREA#POINT##` |
| Store tuned station | `*22*33#STATION*2#SOURCE_ID##` |
| Request source frequency | `*#22*5#2#SOURCE_ID*5##` |
| Request speaker volume | `*#22*3#AREA#POINT*1##` |
| Set speaker balance | `*#22*3#AREA#POINT*#17*BALANCE##` |
| Set speaker preset | `*#22*3#AREA#POINT*#19*PRESET##` |
| Set speaker loudness | `*#22*3#AREA#POINT*#20*LOUDNESS##` |

Source dimension requests use the general-source form `5#2#SOURCE_ID` in these flows; some responses instead use `2#SOURCE_ID`. Retain the reported address rather than requiring textual equality with the request. Status requests receive an action-session ACK while the specified state reports appear on the event session; dimension reads have their own response flows.

#### Published inconsistencies

Section ID: `ownkb:section:d000053:s000008`

Cautions: `do not`
Provenance cues: `catalogue`, `evidence`, `source`, `specification`

The detailed specification is not uniformly reliable as a copy-and-send frame catalogue. Speaker power examples omit separators that appear in the address table; speaker writes for dimensions `1..4` join the dimension marker to `WHERE` without the normal `*`; preset commands `55`/`56` contain an early `##`; and some tone-response dimension numbers disagree with the requested tone. RDS commands `31`/`32` are printed without a normal `WHERE` field. The source also shows `WHAT 21` source notifications outside its summary table.

Preserve these as source discrepancies. The ordinary frame grammar suggests possible corrections, but captures or implementation evidence are needed before treating a repaired frame as established. Occasional trailing empty fields in volume reports should be preserved by the parser. The compact tables above do not assert support for every read/write combination.

### Source and speaker semantics

Section ID: `ownkb:section:d000053:s000009`

Provenance cues: `source`

Source commands and reports use source addresses; volume/tone/balance operations generally apply to speaker endpoints or areas. `WHAT 35` carries routing intent by selecting a source while turning an amplifier on. Follow Me (`WHAT 34`) is a separate operation and should not be normalized to ordinary ON.

The same namespace includes tuner, media-track, presets, RDS, and equalization. Interpretation depends on the selected source and target class.

### Relationship to `WHO 16`

Section ID: `ownkb:section:d000053:s000010`

Cautions: `do not`

[`WHO 16`](../who-16-sound-system/) represents a different sound dialect. Similar terms do not imply compatible numeric values, address forms, or parameter layouts.

### Evidence basis

Section ID: `ownkb:section:d000053:s000011`

Provenance cues: `specification`

Parameters, identifiers, and allowed-message distinctions come from [`WHO 22` specification](../../sources/openwebnet-public/pdf/WHO_22.pdf). Where its summary table and detailed flow differ, this page records the more specific flow and notes the discrepancy.

See the [functional overview](../) for navigation by `WHO` and by function, and [Protocol](../../protocol/) for common frame and session syntax.

# Document: ownkb:document:d000054

Source path: `functional/who-23-access-control/README.md`
Namespace context: `who:23`
Area: `functional`

## `WHO 23` - Access Control

Section ID: `ownkb:section:d000054:s000001`

`WHO 23` identifies Access Control. The current corpus establishes a managed functional/diagnostic family and concrete MyHOME Suite address classes, but not a complete ordinary functional command table.

### MyHOME Suite model

Section ID: `ownkb:section:d000054:s000002`

Cautions: `do not`
Provenance cues: `evidence`

`OPEN.db` records functional `WHO 23`, diagnostic `WHO 1023`, `managed = 1`, and the same 65-record management-operation set associated with the Lighting/Automation and Energy Management families.

It defines two Access Control address classes:

| Target class | Virtual form | Advanced form |
| --- | --- | --- |
| Command or virgin Device | `20` | `20` |
| Indicators | `7[R1][R2]` | `7[R1R2]` |

These labels and forms are implementation evidence for MyHOME Suite management/address construction. They do not establish a functional `WHAT` or `DIMENSION` vocabulary.

### Protocol boundary

Section ID: `ownkb:section:d000054:s000003`

Cautions: `do not`

Do not decode Access Control using Lighting/Automation A/PL or Alarm zone/sensor rules. Diagnostic discovery and configuration use `WHO 1023` and belong under [`diagnostics/`](../../diagnostics/).

The shared 65-record management set establishes participation in the common Device â†’ Module â†’ Object â†’ Configuration infrastructure where applicable; it does not imply that every Access Control Device implements every operation.

### Evidence status

Section ID: `ownkb:section:d000054:s000004`

Uncertainty: `unknown`
Provenance cues: `database`, `source`, `specification`

The current public PDF corpus contains no dedicated `WHO 23` functional specification. Preserve unknown functional frames losslessly and add semantics only from a canonical source, an exact implementation template, or observed traffic.

See [MyHOME Suite `OPEN.db` Coverage](../open-db-coverage.md), [Cross-database functional coverage](../cross-database-coverage.md), and the [Device Model](../../device-model/).

# Document: ownkb:document:d000055

Source path: `functional/who-24-lighting-management/README.md`
Namespace context: `who:24`
Area: `functional`

## `WHO 24` - Lighting Management

Section ID: `ownkb:section:d000055:s000001`

`WHO 24` defines the OpenWebNet Lighting Management protocol system. Its frame structure and addressing are specific to this namespace and are distinct from ordinary [`WHO 1`](../who-1-lighting/) Lighting.

### Reference

Section ID: `ownkb:section:d000055:s000002`

| Subject | Page |
| --- | --- |
| Protocol and frame structure | [Protocol](protocol.md) |
| `WHAT` operations | [`WHAT` Reference](what.md) |
| Addressing and `WHERE` structure | [Addressing](addressing.md) |
| `DIMENSION` operations | [`DIMENSION` Reference](dimensions.md) |

The [functional overview](../) groups both systems under Lighting.

# Document: ownkb:document:d000056

Source path: `functional/who-24-lighting-management/addressing.md`
Namespace context: `who:24`
Area: `functional`

## Addressing

Section ID: `ownkb:section:d000056:s000001`

Provenance cues: `source`

`WHO 24` uses a structured sender/recipient `WHERE` rather than the `A`/`PL` grammar of `WHO 1`.

The complete `WHERE` contains both recipient and sender:

```text
RECIPIENT_ZONE#RECIPIENT_ENDPOINT#00#SENDER_ZONE#SENDER_ENDPOINT
```

The source writes an endpoint as `dev_type & sys_addr`. Its examples concatenate those values: `dev_type = 1` and `sys_addr = 1` become `11`; a Lighting Console (`99991`) at system address `1` becomes `999911`. The `&` is notation, **not a transmitted character**. The literal `#00#` separates recipient and sender within one `WHERE`; it is not a choice between two alternative whole-address forms.

For example, `*#24*1001#11#00#0#999911*#3*200##` writes maintained illuminance of 200 lux to zone 1 on BMNE500 system address 1, from a Lighting Console at system address 1.

Some source examples use bare special endpoint codes (`8`, `4`, or `99991`) without a separately recognizable system-address suffix. Preserve these explicitly illustrated special forms rather than requiring a suffix on every endpoint or guessing one.

### Lighting Management zone

Section ID: `ownkb:section:d000056:s000002`

| `LM_zone_num` | Meaning |
| --- | --- |
| `0` | No zones |
| `1000` | Every zone |
| `1000 + zone number` | Selected zone |

The zone encoding is therefore offset-based. A displayed zone number and its wire value are not necessarily identical.

### Device type

Section ID: `ownkb:section:d000056:s000003`

Uncertainty: `unknown`
Provenance cues: `evidence`

| `dev_type` | Meaning |
| --- | --- |
| `1` | BMNE500 / 002645 |
| `99991` | Lighting Console |
| `9991` | Virtual Configurator |
| `4` | Broadcast |
| `8` | Unknown in the published table |

`dev_type 8` remains unknown. No device role is assigned without additional evidence.

### System address

Section ID: `ownkb:section:d000056:s000004`

Applicability cues: `scs`
Cautions: `must not`

`sys_addr` uses the published range `1..9`. It is a Lighting Management system-address component and must not be interpreted as an SCS `A` or `PL` configurator.

### Sender versus recipient

Section ID: `ownkb:section:d000056:s000005`

Cautions: `do not`
Provenance cues: `source`

Represent recipient and sender as separate fields inside the decoded address. Replies reverse their communication roles; do not assume that the complete response `WHERE` equals the request `WHERE`. The source examples also vary the suffix on special endpoint codes, so preserve the raw endpoint alongside any decoded type/address.

This address grammar is one of the principal reasons `WHO 24` must remain separate from ordinary [`WHO 1`](../who-1-lighting/) Lighting.

### Evidence basis

Section ID: `ownkb:section:d000056:s000006`

Provenance cues: `specification`

The [Lighting Management Specification](../../sources/openwebnet-public/pdf/WHO_24.pdf), pages 4â€“5, gives the notation and concrete two-endpoint examples.

# Document: ownkb:document:d000057

Source path: `functional/who-24-lighting-management/dimensions.md`
Namespace context: `who:24`
Area: `functional`

## `DIMENSION` Reference

Section ID: `ownkb:section:d000057:s000001`

Provenance cues: `specification`

`WHO 24` uses `DIMENSION` operations for Lighting Management configuration and runtime state. Reads use the ordinary `DIMENSION` form; writable properties use `#DIMENSION`.

| `DIMENSION` | Property | Published value domain |
| --- | --- | --- |
| `1` | Switch-on level | `1..100` percent |
| `2` | Maximum illuminance | `1..2000` lux |
| `3` | Maintained illuminance | `0..2000` lux |
| `4` | Automatic switch ON | `0` disabled; `1` enabled |
| `5` | Switch-on delay | `0..300` seconds |
| `6` | Automatic switch OFF | `0` disabled; `1` enabled |
| `7` | Switch-off delay | `0..900` seconds |
| `8` | Delay timer | `0..3600` seconds |
| `9` | Stand-by timer | `0..900` seconds |
| `10` | Stand-by level | `0..100` percent |
| `11` | OFF level | `0..100` percent |
| `12` | Slave offset (GAP) | `0..100` percent |
| `17` | Operating state | `MOD*EXIT*H*M*S` |
| `18` | Centralised illuminance | `SENSOR*LUX*ERROR` |

The detailed specification provides writes and reads for these properties. Scalar writes use `*#24*WHERE*#D*VALUE##` and reports use `*#24*WHERE*D*VALUE##`, with `D` replaced by the selected identifier. `WHERE` contains both [recipient and sender](addressing.md).

### Read-form inconsistencies

Section ID: `ownkb:section:d000057:s000002`

Cautions: `do not`
Provenance cues: `source`

The source prints `*#24*WHERE*D##` for scalar requests `1..10`, but `*#24*WHERE*12*##` with a trailing empty value for slave offset. The state request is `*#24*WHERE*17##`. Its OFF-value request section instead repeats the write form `*#24*WHERE*#11*Off_val##`, apparently a copy error. That row does not establish a safe read command: do not send the write form when intending only to query. Confirm the OFF-value read variant on the target.

The illuminance request has a separate discrepancy, documented below. Preserve these distinctions rather than deriving every read mechanically by deleting the write marker.

### Maintained level

Section ID: `ownkb:section:d000057:s000003`

The published write form is `*#24*WHERE*#3*Maint_lev##`. `Maint_lev` is illuminance in lux, not a percentage; it should not be normalized as a `WHO 1` dimmer command.

### Timers and delays

Section ID: `ownkb:section:d000057:s000004`

`DIMENSION 5`, `7`, `8`, and `9` represent distinct timing properties: switch-on delay, switch-off delay, general delay timer, and stand-by timer. Their similar data type does not make them interchangeable.

### Stand-by and OFF values

Section ID: `ownkb:section:d000057:s000005`

`DIMENSION 10` and `11` configure values associated with stand-by and OFF behavior. They are separate from the enable/disable decisions represented by the automatic switching dimensions.

### Slave offset

Section ID: `ownkb:section:d000057:s000006`

`DIMENSION 12` carries the slave-offset/GAP value. Whether slave offset is enabled is controlled separately through parameterized `WHAT 2#[0-1]`; implementations should store both properties.

### Runtime state

Section ID: `ownkb:section:d000057:s000007`

Cautions: `do not`
Provenance cues: `source`

State request: `*#24*WHERE*17##`.

State write: `*#24*WHERE*#17*MOD*EXIT*H*M*S##`.

State response/event: `*#24*WHERE*17*MOD*EXIT*H*M*S##`.

| Field | Meaning |
| --- | --- |
| `MOD` | `0` Stop; `1` Automatic; `2` Manual |
| `EXIT` | Return-to-automatic condition: `1` TIME; `2` FOR; `3` PROFILE; `4` NORMAL; `5` NEVER |
| `H*M*S` | Time or duration for TIME/FOR, with ranges `0..23`, `0..59`, `0..59` |

The source's `TIME` placeholder expands to three `*`-separated values. Do not treat the whole state report as one enum or transmit a literal `TIME` string.

### Centralised illuminance

Section ID: `ownkb:section:d000057:s000008`

Applicability cues: `gateway`
Cautions: `do not`
Provenance cues: `source`

The detailed read table uses `*#24*WHERE*18*SENSOR##`; response/event `*#24*WHERE*18*SENSOR*LUX*ERROR##`; write `*#24*WHERE*#18*SENSOR*LUX*ERROR##`.

`ERROR` is `0` when required parameters are available, `1` when the sensor is not configured, and `2` when present but missing required parameters. `LUX` is illuminance; the detailed table does not give a numeric range for it or `SENSOR`.

Pages 4â€“5 instead show selector-qualified examples `18#65` with response values `297*0`. That differs structurally from the `18*Sensor_addr` form on pages 21â€“22 and 39â€“41. Retain both as source variants and select only a form corroborated for the gateway; do not silently move the sensor between selector and payload.

State and illuminance are distinct from the configuration threshold in `DIMENSION 2`.

Capability support is device-specific. The namespace-level table defines available operations but does not imply that every Lighting Management endpoint accepts every write.

### Evidence basis

Section ID: `ownkb:section:d000057:s000009`

Provenance cues: `specification`

Domains and frame variants come from the [Lighting Management Specification](../../sources/openwebnet-public/pdf/WHO_24.pdf), pages 6â€“41. The discrepancies above are retained because they affect safe encoding and request/response matching.

# Document: ownkb:document:d000058

Source path: `functional/who-24-lighting-management/protocol.md`
Namespace context: `who:24`
Area: `functional`

## Protocol

Section ID: `ownkb:section:d000058:s000001`

Applicability cues: `gateway`, `scs`

`WHO 24` defines Lighting Management through a Programmer Gateway. It is distinct from ordinary [`WHO 1`](../who-1-lighting/) Lighting: the namespace models management devices, zones, profiles and control parameters rather than SCS `A`/`PL` light points.

### Frame model

Section ID: `ownkb:section:d000058:s000002`

`WHO 24` uses the common OpenWebNet frame delimiters but gives `WHERE` a specialized sender/recipient grammar. The target can encode a Lighting Management zone, device type and system address. The complete address combines recipient and sender, separated by `#00#`, as documented in [Lighting Management Addressing](addressing.md).

`WHAT` operations are parameterized forms rather than a flat scalar table. `DIMENSION` operations carry configuration/state values such as maintained level, timers, stand-by/off values, operating state and centralised lux.

### Read and write operations

Section ID: `ownkb:section:d000058:s000003`

Structured values use the normal OpenWebNet `DIMENSION` distinction: reads use `DIMENSION`, while writes use `#DIMENSION`. For example, maintained-level writing follows `*#24*WHERE*#3*Maint_lev##`; a corresponding read uses the non-`#` form.

A client should preserve the value schema of each `DIMENSION`. Lux, level, timers, state and slave-offset values are different domains even though they occupy the same frame position.

### Profiles

Section ID: `ownkb:section:d000058:s000004`

Cautions: `must not`

The `WHAT 1#PROFILE_ID` family identifies a profile operation. The profile identifier is part of `WHAT` syntax and must not be moved into `WHERE` or treated as a `DIMENSION` value.

### Slave offset

Section ID: `ownkb:section:d000058:s000005`

`WHAT 2#[0-1]` controls slave-offset enable/disable behavior, while `DIMENSION 12` carries the slave-offset/GAP value. The enable state and the configured offset are therefore separate protocol properties.

### State and lux

Section ID: `ownkb:section:d000058:s000006`

`DIMENSION 17` reports the Lighting Management operating state (Automatic / Manual / Stop). `DIMENSION 18` carries the centralised lux value. These are management-system properties and are not aliases of `WHO 1` dimmer state or level.

See [`WHAT` Reference](what.md), [Addressing](addressing.md), and [`DIMENSION` Reference](dimensions.md) for the system-specific grammar.

# Document: ownkb:document:d000059

Source path: `functional/who-24-lighting-management/what.md`
Namespace context: `who:24`
Area: `functional`

## `WHAT` Reference

Section ID: `ownkb:section:d000059:s000001`

Published `WHO 24` `WHAT` forms are parameterized expressions rather than a flat scalar command table.

| `WHAT` form | Meaning | Parameter role |
| --- | --- | --- |
| `1#PROFILE_ID` | Profile frame | Selects the Lighting Management profile |
| `2#0` | Disable slave offset | Offset-enable state |
| `2#1` | Enable slave offset | Offset-enable state |

### Profile operations

Section ID: `ownkb:section:d000059:s000002`

In `1#PROFILE_ID`, the profile identifier is part of the `WHAT` field. It must remain attached to the operation when parsing, serializing, logging, or comparing frames. Treating `PROFILE_ID` as part of `WHERE` would change the grammar.

Profiles belong to Lighting Management rather than ordinary `WHO 1` Lighting scenes or levels. A profile identifier should therefore be represented as a `WHO 24` value even when applying the profile ultimately affects lighting output.

### Slave offset enable

Section ID: `ownkb:section:d000059:s000003`

`WHAT 2#0` and `2#1` control whether slave offset is disabled or enabled. The actual offset/GAP value is a separate property carried by `DIMENSION 12`. A complete configuration model must preserve both the Boolean enable state and the configured offset value.

### Namespace rule

Section ID: `ownkb:section:d000059:s000004`

These values are not aliases for `WHO 1` `WHAT` values. Their meaning follows the `WHO 24` management grammar and the structured sender/recipient address described in [Addressing](addressing.md).

# Document: ownkb:document:d000060

Source path: `functional/who-25-transversal/README.md`
Namespace context: `who:25`
Area: `functional`

## `WHO 25` - Transversal Functions

Section ID: `ownkb:section:d000060:s000001`

Applicability cues: `scs`, `zigbee`

`WHO 25` contains multiple transversal OpenWebNet functions whose grammars are selected by their `WHAT` family. The namespace includes CEN+ virtual-command events and dry-contact/IR state reporting. Sharing `WHO 25` does not make these functions one address or parameter model.

The [ZigBee Interface](../../protocol/zigbee-interface.md) also exposes a distinct binding family under `WHO 25`. Resolve the interface variant before applying the SCS virtual-Object and button rules below; the ZigBee binding lifecycle is documented separately in [ZigBee Binding](zigbee-binding.md).

### Reference

Section ID: `ownkb:section:d000060:s000002`

Applicability cues: `zigbee`

| Function | Reference | Established vocabulary |
| --- | --- | --- |
| CEN+ | [CEN+](cen-plus.md) | `WHAT 21..28`; pushbutton `0..31`; virtual Object `0..2047` |
| Dry contact / IR | [Dry Contact and IR](dry-contact-ir.md) | `WHAT 31..32`; state/event parameter `0`/`1` |
| ZigBee binding | [ZigBee Binding](zigbee-binding.md) | `WHAT 33..37`; ZigBee product-and-Unit `WHERE` |

### Function selection

Section ID: `ownkb:section:d000060:s000003`

Applicability cues: `zigbee`

A parser should resolve the OpenWebNet interface variant, `WHO 25`, and then the `WHAT` family before decoding the remaining fields. CEN+ interprets the `WHAT` parameter as a virtual pushbutton and uses a `2`-prefixed virtual Object `WHERE`. Dry-contact/IR operations instead use the parameter to distinguish requested state from event/action context and use Device-family-specific `WHERE` ranges. ZigBee binding uses the radio product-and-Unit `WHERE` grammar with family suffix `#9`.

### CEN+ relationship

Section ID: `ownkb:section:d000060:s000004`

Provenance cues: `source`

CEN+ complements Basic/Evolved CEN under [`WHO 15`](../who-15-cen/). In CEN+, the interaction phase moves into `WHAT 21..24`, the pushbutton becomes a `WHAT` parameter, and the source is represented by a virtual Object. Rotary-selector operations `25..28` extend that model further.

### Dry-contact and IR relationship

Section ID: `ownkb:section:d000060:s000005`

The dry-contact/IR family uses `WHAT 31` for ON/detection and `WHAT 32` for OFF/no detection. It remains under the canonical `WHO 25` namespace even though its address grammar is unrelated to CEN+ virtual Objects.

The [functional overview](../) provides alternate navigation by function while these pages remain organized under their canonical protocol namespace.

# Document: ownkb:document:d000061

Source path: `functional/who-25-transversal/cen-plus.md`
Namespace context: `who:25`
Area: `functional`

## CEN+

Section ID: `ownkb:section:d000061:s000001`

CEN+ is carried within `WHO 25` and provides a virtual-object command/event model for short press, extended press and rotary-selector interactions. It is related to CEN under [`WHO 15`](../who-15-cen/) but uses a different field allocation and address space.

### `WHAT` reference

Section ID: `ownkb:section:d000061:s000002`

| `WHAT` | Meaning |
| --- | --- |
| `21` | Short pressure, less than 0.5 seconds |
| `22` | Start of extended pressure, at least 0.5 seconds |
| `23` | Extended pressure / keep pressing |
| `24` | Release after an extended pressure |
| `25` | Rotary selector, slow clockwise rotation |
| `26` | Rotary selector, fast clockwise rotation |
| `27` | Rotary selector, slow counter-clockwise rotation |
| `28` | Rotary selector, fast counter-clockwise rotation |

Unlike `WHO 15`, the interaction type is encoded by `WHAT`; the virtual pushbutton number is carried as a parameter.

### Pushbutton parameter

Section ID: `ownkb:section:d000061:s000003`

Provenance cues: `source`

The parameter attached to `WHAT` identifies the virtual pushbutton and has the range `0..31`.

The general form is `*25*WHAT#PUSHBUTTON*WHERE##`.

`PUSHBUTTON` and the Object embedded in `WHERE` are independent fields: the first identifies the control on the source Object, while the second identifies the configured CEN+ virtual Object.

### `WHERE` - virtual Object

Section ID: `ownkb:section:d000061:s000004`

CEN+ uses a virtual address formed from the prefix `2` and an Object value in the range `0..2047`.

Conceptually:

`WHERE = 2 + OBJECT`

Published examples include `21` for Object 1, `20` for Object 0, `2101` for Object 101, `22010` for Object 2010, and `22047` for Object 2047. The field is therefore a protocol composition, not a decimal arithmetic addition.

A decoder should remove/interpret the CEN+ prefix according to the `WHO 25` grammar rather than parse the complete field as a Lighting/Automation `A`/`PL` address.

### Short pressure - `WHAT 21`

Section ID: `ownkb:section:d000061:s000005`

Action frame: `*25*21#PUSHBUTTON*WHERE##`.

A short interaction is complete in one event. It represents a press and release occurring before the 0.5-second extended-pressure threshold; there is no separate short-release `WHAT` analogous to CEN `WHO 15` `#1`.

The accepted virtual action is acknowledged with `ACK`, and the corresponding CEN+ frame is visible on event connections.

### Start of extended pressure - `WHAT 22`

Section ID: `ownkb:section:d000061:s000006`

Action frame: `*25*22#PUSHBUTTON*WHERE##`.

This marks that the button has reached the extended-pressure threshold. It begins the long-interaction sequence and is distinct from the periodic continued-pressure event `WHAT 23`.

### Extended pressure - `WHAT 23`

Section ID: `ownkb:section:d000061:s000007`

Uncertainty: `may`

Action frame: `*25*23#PUSHBUTTON*WHERE##`.

While a physical CEN+ button remains pressed, continued-pressure events can follow the initial `WHAT 22`. Multiple `WHAT 23` frames may therefore belong to one physical interaction.

### End of extended pressure - `WHAT 24`

Section ID: `ownkb:section:d000061:s000008`

Action frame: `*25*24#PUSHBUTTON*WHERE##`.

This marks release after an extended interaction and closes the sequence begun by `WHAT 22`.

A typical held-button event sequence is therefore:

`WHAT 22` â†’ zero or more `WHAT 23` â†’ `WHAT 24`.

The published examples show both sequences with repeated `23` frames and a sequence in which `22` is followed directly by `24` when release occurs before another continued-pressure interval is emitted.

### Rotary-selector events - `WHAT 25..28`

Section ID: `ownkb:section:d000061:s000009`

CEN+ also defines directional rotary interactions:

| Direction | Slow | Fast |
| --- | --- | --- |
| Clockwise | `25` | `26` |
| Counter-clockwise | `27` | `28` |

These operations use the same virtual Object/pushbutton addressing model. Their presence is an important difference from Basic/Evolved CEN under `WHO 15`.

### Action and event connections

Section ID: `ownkb:section:d000061:s000010`

Applicability cues: `gateway`, `scs`

CEN+ supports virtual actions and event reporting. For pushbutton interactions, a client sends the functional frame on an action connection and receives `ACK`; event-session clients receive the corresponding frame when the gateway reads the CEN+ event on the SCS bus.

The same event form can therefore represent an interaction originating from a physical CEN+ command or from a virtual action submitted through a gateway. The functional frame itself identifies the interaction, pushbutton and Object rather than its origin.

### CEN+ configuration model

Section ID: `ownkb:section:d000061:s000011`

Applicability cues: `scs`
Cautions: `do not`
Provenance cues: `documentation`, `source`

The published CEN documentation states that CEN+ devices use Advanced Virtual Configuration and do not use a conventional SCS bus address for this function. The configured virtual Object becomes the OpenWebNet `WHERE`, while the button number is represented by the `WHAT` parameter.

This is materially different from Basic/Evolved CEN, where `WHO 15` `WHERE` can represent an `A`/`PL` source address and the button numbß~öá¼­zÊ&ŠÛ^u¸Ñ¡•¥È½Ý¸…Ñ¥½¸±…‰•±Ì¸Q¡”Ý¥É”ÍÑÉÕÑÕÉ”É•µ…¥¹ÌÑ¡”Í…µ”ÑÝ¼µÙ…±Õ”%59M%=8€Ý€µ½‘•°¸((ŒŒŒ5å!=5}MÕ¥Ñ”±½…°µ½¹ÑÉ½°…¹™…¸µ½¥°ÝÉ¥Ñ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÀÙ€()M•¹…É¥½•Ù¥•Ì…±Í¼‘•™¥¹•Ìè()ð…Á…‰¥±¥ÑäðQ•µÁ±…Ñ”ð)ð€´´´ð€´´´ð)ð1½…°½¹ÑÉ½°ð€¨ŒÐ©ii¨ŒÔ©Ù…°Œ€ð)ð…¸µ½¥°ÍÁ••ð€¨ŒÐ©ii¨ŒÄÄ©Ù…°Œ€ð()Q¡•Í”…É”Í•¹…É¥¼µ•¹¥¹”…Ñ¥½¸Ñ•µÁ±…Ñ•Ì¸Q¡•¥ÈÁÉ•Í•¹”•ÍÑ…‰±¥Í¡•ÌÑ¡…Ð5å!=5}MÕ¥Ñ”…¸•µ¥ÐÑ¡”ÝÉ¥Ñ”™½É´™½ÈÑ¡•Í”½Á•É…Ñ¥½¹Ìì¥Ð‘½•Ì¹½Ð‰ä¥ÑÍ•±˜É•‘•™¥¹”•Ù•ÉäÁÕ‰±¥ŒÉ•…½ÍÑ…ÑÕÌµ•…¹¥¹œ…ÑÑ…¡•Ñ¼Ñ¡”Í…µ”%59M%=9€¹Õµ‰•È¸((ŒŒŒ%59M%=8€Á€€´µ•…ÍÕÉ•Ñ•µÁ•É…ÑÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÀÝ€()µ•…ÍÕÉ•µÑ•µÁ•É…ÑÕÉ”É•ÅÕ•ÍÐÕÍ•Ì€¨ŒÐ©]!I¨ÀŒ€ìÑ¡”É•ÍÁ½¹Í”…ÉÉ¥•ÌÑ¡”Ñ•µÁ•É…ÑÕÉ”Ù…±Õ”…™Ñ•È%59M%=8€Á€¸()AÕ‰±¥Í¡•µ•…ÍÕÉ•½ÍÑ…ÑÕÌÑ•µÁ•É…ÑÕÉ”™¥•±‘ÌÕÍ”™½ÕÈ‘•¥µ…°‘¥¥ÑÌ…¹…¸É•ÁÉ•Í•¹Ð€ÀÀÀÀ¸¸ÀÔÀÁ€€¡€À¸À¸¸ÔÀ¸Á€ƒ
Á¤Ý¥Ñ €À¸Äƒ
ÁÉ•Í½±ÕÑ¥½¸¥¸Ñ¡”‘½Õµ•¹Ñ•é½¹”µÍÑ…ÑÕÌ•á¡…¹•Ì¸Q¡¥ÌÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸¥Ì‘¥ÍÑ¥¹Ð™É½´Í•ÑÁ½¥¹ÐµÝÉ¥Ñ¥¹œ½¹ÍÑÉ…¥¹ÑÌ¸((ŒŒŒ%59M%=8€ÄÅ€€´™…¸µ½¥°ÍÁ••()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÀá€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()%59M%=8€ÄÅ€É•Á½ÉÑÌ™…¸µ½¥°ÍÁ••¥¸Ñ¡”ÁÕ‰±¥Í¡•ÍÑ…ÑÕÌµ½‘•°¸M•¹…É¥½•Ù¥•Ì…‘‘¥Ñ¥½¹…±±ä‘•™¥¹•ÌÑ¡”ÝÉ¥Ñ”Ñ•µÁ±…Ñ”€¨ŒÐ©ii¨ŒÄÄ©Ù…°Œ€°•ÍÑ…‰±¥Í¡¥¹œ„5å!=5}MÕ¥Ñ”Í•¹…É¥¼…Ñ¥½¸™½È™…¸µ½¥°ÍÁ••¸()Q¡”ÁÕ‰±¥ŒÉ•ÍÁ½¹Í”½•Ù•¹Ð™½É´¥Ì€¨ŒÐ©]!I¨ÄÄ©MA¨Œ€°¥¹±Õ‘¥¹œ„ÑÉ…¥±¥¹œ•µÁÑä™¥•±¸MA€¥Ì€Á€…ÕÑ½µ…Ñ¥Œ°€Ä¸¸Í€Ñ¡”Ñ¡É•”ÍÁ••‘Ì°½È€ÄÕ€=€¡ÁÕ‰±¥ŒÍÁ•¥™¥…Ñ¥½¸°Á…”€ÄÔ¤¸()I•……¹ÝÉ¥Ñ”™½ÉµÌÍ¡½Õ±Ñ¡•É•™½É”‰”‘¥ÍÑ¥¹Õ¥Í¡•‰ä™É…µ”‘¥É•Ñ¥½¸…¹½Á•É…Ñ¥½¸½¹Ñ•áÐÉ…Ñ¡•ÈÑ¡…¸…ÍÍÕµ¥¹œÑ¡…ÐÑ¡”¥‘•¹Ñ¥™¥•È¥Ì±½‰…±±äÉ•…µ½¹±ä¥¸Ñ¡”¥µÁ±•µ•¹Ñ…Ñ¥½¸¸((ŒŒŒ%59M%=8€ÄÉ€€´½µÁ±•Ñ”ÁÉ½‰”ÍÑ…ÑÕÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÀå€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()%59M%=8€ÄÉ€É•ÑÕÉ¹ÌÑ¡”½µÁ±•Ñ”ÁÉ½‰”ÍÑ…Ñ”°½µ‰¥¹¥¹œÑ¡”é½¹”ÌÑ…É•Ð½ÍÑ…ÑÕÌ¥¹™½Éµ…Ñ¥½¸Ý¥Ñ ¥ÑÌ½Á•É…Ñ¥¹œ½¹Ñ•áÐ¸%Ð¥ÌÑ¡”…ÁÁÉ½ÁÉ¥…Ñ”½Á•É…Ñ¥½¸Ý¡•¸„±¥•¹Ð¹••‘Ìµ½É”Ñ¡…¸Ñ¡”Í…±…Èµ•…ÍÕÉ•Ñ•µÁ•É…ÑÕÉ”É•ÑÕÉ¹•‰ä%59M%=8€Á€¸()Q¡”ÁÕ‰±¥ŒÉ•ÅÕ•ÍÐ¥Ì€¨ŒÐ©]!I¨ÄÈŒ€™½Èµ…ÍÑ•ÈµÁÉ½‰”…‘‘É•ÍÍ•Ì€Ä¸¸äå€¸Q¡”É•ÍÁ½¹Í”€¨ŒÐ©]!I¨ÄÈ©P¨ÌŒ€¥Ù•ÌÑ¡”Í•ÑÁ½¥¹Ð…™Ñ•È±½…°½™™Í•ÐèQ€É…¹•Ì½Ù•È€ÀÀÈÀ¸¸ÀÐÌÁ€¥¸€À¸Äƒ
ÁÕ¹¥ÑÌ¸Q¡”ÑÉ…¥±¥¹œ€Í€¥Ì™¥á•¥¸Ñ¡¥ÌÁÕ‰±¥Í¡•™±½ÜìÑ¡”…ÑÕ…°¡•…Ñ¥¹œ½½¹‘¥Ñ¥½¹¥¹œ½ÁÉ½Ñ•Ñ¥½¸ÍÑ…Ñ”¥Ì…±Í¼É•ÑÕÉ¹•¥¸„Í•Á…É…Ñ”€¨Ð©]!P©]!IŒ€™É…µ”¸¼¹½Ð¥¹Ñ•ÉÁÉ•ÐÑ¡”™¥¹…°€Í€…Ì„½µÁ±•Ñ”É•Á±…•µ•¹Ð™½ÈÑ¡…ÐÍÑ…Ñ”™É…µ”€¡Á…”€ÄØ¤¸((ŒŒŒ%59M%=8€ÄÍ€€´±½…°Í•Ð½™™Í•Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÄÁ€()%59M%=8€ÄÍ€É•Á½ÉÑÌÑ¡”±½…°Í•ÑÁ½¥¹Ð½™™Í•Ð…ÁÁ±¥•…ÐÑ¡”ÁÉ½‰”¸1½…°½™™Í•Ð¥ÌÍ•Á…É…Ñ”™É½´Ñ¡”•¹ÑÉ…°Ñ…É•ÐÑ•µÁ•É…ÑÕÉ”è„é½¹”…¸Ñ¡•É•™½É”¡…Ù”„•¹ÑÉ…°Í•ÑÁ½¥¹Ð…¹„ÁÉ½‰”µ±½…°…‘©ÕÍÑµ•¹ÐÍ¥µÕ±Ñ…¹•½ÕÍ±ä¸()I•ÅÕ•ÍÐ€¨ŒÐ©]!I¨ÄÌŒ€ìÉ•ÍÁ½¹Í”½•Ù•¹Ð€¨ŒÐ©]!I¨ÄÌ©=MPŒ€€¡Á…•Ì€ÄÛŠLÄÜ¤¸()ð=MQ€ð-¹½ˆÍÑ…Ñ”ð)ð€´´´ð€´´´ð)ð€ÀÁ€ð9¼½™™Í•Ðð)ð€ÀÅ€°€ÀÉ€°€ÀÍ€ð€¬Ä°€¬È°€¬Ìƒ
Áð)ð€ÄÅ€°€ÄÉ€°€ÄÍ€ð€´Ä°€´È°€´Ìƒ
Áð)ð€Ñ€ð1½…°=ð)ð€Õ€ð1½…°ÁÉ½Ñ•Ñ¥½¸ð()Q¡•Í”…É”½‘•Ì°¹½ÐÍ¥¹•‘•¥µ…°Ñ•µÁ•É…ÑÕÉ•Ì¸((ŒŒŒ%59M%=8€ÄÑ€€´Í•ÑÁ½¥¹ÐÑ•µÁ•É…ÑÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÄÅ€()%59M%=8€ÄÑ€¥ÌÉ•…‘…‰±”…¹ÝÉ¥Ñ…‰±”¸é½¹”Í•ÑÁ½¥¹ÐÝÉ¥ÑÑ•¸Ñ¡É½Õ Ñ¡”•¹ÑÉ…°Õ¹¥ÐÕÍ•Ì€¨ŒÐ¨]!I¨ŒÄÐ©P©4Œ€¸()½ÈÑ¡¥Ì½Á•É…Ñ¥½¸°Q€¥Ì•¹½‘•…Ì™½ÕÈ‘¥¥ÑÌ¥¸€ÀÀÔÀ¸¸ÀÐÀÁ€€ Ô¸À¸¸ÐÀ¸Àƒ
Á¤¥¸€À¸Ôƒ
ÁÍÑ•ÁÌ¸5€¥‘•¹Ñ¥™¥•ÌÑ¡”½Á•É…Ñ¥¹œ½¹Ñ•áÐè€Å€¡•…Ñ¥¹œ°€É€½¹‘¥Ñ¥½¹¥¹œ°€Í€•¹•É¥Œ¸()Q¡”5å!=5}MÕ¥Ñ”™Õ¹Ñ¥½¹…°Á…É…µ•Ñ•È‘•™¥¹¥Ñ¥½¹Ì±¥­•Ý¥Í”É•ÁÉ•Í•¹ÐÍ•ÑÁ½¥¹ÐÉ…¹•Ì…¹ÍÑ•ÁÌ™½ÈQ•µÁ•É…ÑÕÉ”½¹ÑÉ½°½Á•É…Ñ¥½¹ÌìÑ¡”•á…ÐÁ…É…µ•Ñ•È‘•™¥¹¥Ñ¥½¸…ÑÑ…¡•Ñ¼Ñ¡”½µµ…¹É•µ…¥¹Ì…ÕÑ¡½É¥Ñ…Ñ¥Ù”™½ÈÑ¡”¥µÁ±•µ•¹Ñ…Ñ¥½¸™½É´‰•¥¹œ•¹½‘•¸()Q¡”ÁÕ‰±¥ŒÉ•…™½É´¥Ì€¨ŒÐ©]!I¨ÄÐŒ€°Ý¥Ñ É•ÍÁ½¹Í”€¨ŒÐ©]!I¨ÄÐ©P¨ÌŒ€™½ÈÁÉ½‰”…‘‘É•ÍÍ•Ì€Ä¸¸äå€¸Q¡”É•…Ñ…‰±”ÍÁ•¥™¥•Ì€À¸Äƒ
ÁÉ•Í½±ÕÑ¥½¸½Ù•È€ÀÀÔÀ¸¸ÀÐÀÁ€ì¥Ð‘½•Ì¹½Ð¡…¹”Ñ¡”€À¸Ôƒ
ÁÍÑ•ÀÍÁ•¥™¥•™½ÈÝÉ¥Ñ•Ì€¡Á…”€Äà¤¸((ŒŒŒ%59M%=8€Äå€€´Ù…±Ù”ÍÑ…ÑÕÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÄÉ€()%59M%=8€Äå€É•Á½ÉÑÌ½½±¥¹œ´…¹¡•…Ñ¥¹œµÙ…±Ù”ÍÑ…Ñ”¸AÕ‰±¥Í¡•Ù…±Ù”½™…¸µ½¥°Ù…±Õ•Ì¥¹±Õ‘”=°=8°½Á•¹•°±½Í•°ÍÑ½À°…¹™…¸µ½¥°ÍÁ••ÍÑ…Ñ•Ì¸()I•ÅÕ•ÍÐ€¨ŒÐ©]!I¨ÄäŒ€ìÉ•ÍÁ½¹Í”½•Ù•¹Ð€¨ŒÐ©]!I¨Ää©X©!XŒ€¸Y€¥ÌÑ¡”½¹‘¥Ñ¥½¹¥¹œÙ…±Ù”…¹!Y€Ñ¡”¡•…Ñ¥¹œÙ…±Ù”°¥¸Ñ¡…Ð½É‘•È€¡Á…”€ÈÄ¤¸()ðY…±Õ”ðY…±Ù”ÍÑ…Ñ”ð)ð€´´´ð€´´´ð)ð€Á€ð=ð)ð€Å€ð=8ð)ð€É€ð=Á•¹•ð)ð€Í€ð±½Í•ð)ð€Ñ€ðMÑ½Àð)ð€Õ€ð…¸µ½¥°=ð)ð€Ù€°€Ý€°€á€ð…¸µ½¥°=8…ÐÍÁ••€Ä°€È°€Ìð()Q¡”ÁÕ‰±¥Í¡•Ñ…‰±”‘•™¥¹•ÌÙ…±Õ•Ì€À¸¸á€ì±…Ñ•È¥¹™½Éµ…Ñ¥½¸ÍÕÁÁ±¥•‰äÑ¡”5å!=5Ñ•…´‘½Õµ•¹ÑÌ…‘‘¥Ñ¥½¹…°™…¸µ½¥°=µÍÁ••ÍÑ…Ñ•Ì€ÄÑ€°€ÄÕ€°…¹€ÄÙ€¸Q¡•Í”•áÑ•¹‘•Ù…±Õ•Ì¡…Ù”‰••¸½‰Í•ÉÙ•¥¸É•…°]!<€Ñ€ÍÑ…ÑÕÌÉ•ÍÁ½¹Í•Ì…¹½µÁ±•µ•¹ÐÑ¡”½±‘•ÈÁÕ‰±¥ŒAÉ…Ñ¡•ÈÑ¡…¸¡…¹¥¹œÑ¡”%59M%=8€Äå€™É…µ”ÍÑÉÕÑÕÉ”¸((ŒŒŒ%59M%=8€ÈÁ€€´…ÑÕ…Ñ½ÈÍÑ…ÑÕÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÄÍ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()%59M%=8€ÈÁ€É•ÁÉ•Í•¹ÑÌQ•µÁ•É…ÑÕÉ”½¹ÑÉ½°…ÑÕ…Ñ½ÈÍÑ…Ñ”¸Q¡”5å!=5}MÕ¥Ñ”…‘‘É•ÍÌµ½‘•°ÍÕÁÁ½ÉÑÌ…¸…ÑÕ…Ñ½ÈÍ•±•Ñ½È…ÁÁ•¹‘•Ñ¼Ñ¡”é½¹”…‘‘É•ÍÌ€¡miumi	tm9u€¤°…±±½Ý¥¹œ…ÑÕ…Ñ½È¥¹ÍÑ…¹•ÌÑ¼‰”‘¥ÍÑ¥¹Õ¥Í¡•™É½´ÁÉ½‰”…‘‘É•ÍÍ¥¹œ¸()I•ÅÕ•ÍÐ€¨ŒÐ©h8¨ÈÀŒ€ìÉ•ÍÁ½¹Í”½•Ù•¹Ð€¨ŒÐ©h8¨ÈÀ©Y1UŒ€¸Q¡”ÁÕ‰±¥ŒÑ…É•ÐÉ…µµ…È¥¹±Õ‘•Ìh9€€¡h€ô€À¸¸äå€°8€ô€Ä¸¸å€¤°hŒÁ€™½È…±°…ÑÕ…Ñ½ÉÌ½˜„é½¹”°…¹€ÀŒÁ€™½È…±°…ÑÕ…Ñ½ÉÌ¸()Y1U€ÕÍ•ÌÑ¡”Í…µ”€À¸¸á€±…‰•±Ì…ÌÑ¡”Ù…±Ù”Ñ…‰±”…‰½Ù”°Ý¥Ñ …‘‘¥Ñ¥½¹…°€å€€ô™…¸µ½¥°=8¸%Ð¥ÌÑ¡•É•™½É”É¥¡•ÈÑ¡…¸„‰½½±•…¸=8½=Ù…±Õ”€¡Á…”€ÈÈ¤¸¥É•Ð½¹ÑÉ½°µÕÍÐ¹½Ð‰”¥¹™•ÉÉ•µ•É•±ä™É½´Ñ¡”•á¥ÍÑ•¹”½˜„ÍÑ…ÑÕÌÙ…±Õ”èÑ¡”ÁÕ‰±¥Œ™Õ¹Ñ¥½¹…°Ñ…‰±”±…ÍÍ¥™¥•Ì%59M%=8€ÈÁ€…ÌÉ•…µ½¹±ä¸((ŒŒŒ%59M%=8€ÈÉ€€´ÍÁ±¥Ð½¹ÑÉ½°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÄÑ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()%59M%=8€ÈÉ€¥ÌÑ¡”É•…½ÝÉ¥Ñ”½Á•É…Ñ¥½¸™½ÈÍÁ±¥ÐµÕ¹¥Ð½¹ÑÉ½°¸Q¡”ÁÕ‰±¥Í¡•ÁÉ½Ñ½½°‘•™¥¹•ÌÉ•ÅÕ•ÍÐ°ÝÉ¥Ñ”…¹µ½¹¥Ñ½È½ÍÑ…ÑÕÌ•á¡…¹•Ì™½ÈÍÁ±¥Ð½¹ÑÉ½°Õ¹‘•È]!<€Ñ€¸()Q¡”É•ÅÕ•ÍÐ¥Ì€¨ŒÐ¨Ìh8¨ÈÈŒ€ìÑ¡”ÝÉ¥Ñ”¥Ì€¨ŒÐ¨Ìh8¨ŒÈÈ©5=©M@©Y0©M]%9Œ€¸I•…É•ÍÁ½¹Í•ÌÕÍ”€¨ŒÐ¨Ìh8¨ÈÈ©5=©M@©Y0©M]%9Œ€¸Q¡”É•ÅÕ•ÍÐ½ÝÉ¥Ñ”Ñ…‰±•Ì‘•™¥¹”h€ô€À¸¸äå€°8€ô€Ä¸¸å€€¡Á…•Ì€ØÛŠLØà¤¸()ð¥•±ðAÕ‰±¥Í¡•Ù…±Õ•Ìð)ð€´´´ð€´´´ð)ð5=€ð€Á€=ì€Å€Ý¥¹Ñ•Èì€É€ÍÕµµ•Èì€Í€™…¸ì€Ñ€‘•¡Õµ¥‘¥™¥…Ñ¥½¸ì€Õ€…ÕÑ½µ…Ñ¥Œð)ðMA€ðQ•µÁ•É…ÑÕÉ”¥¸Ñ•¹Ñ¡Ì½˜ƒ
Á°¥¸€À¸Ôƒ
ÁÍÑ•ÁÌì•á…µÁ±•Ì€ÀÀÁ€°€ÀÀÕ€°€ÀÄÁ€Ñ¡É½Õ €ÄÈÜÁ€ð)ðY1€ð€Á€…ÕÑ½µ…Ñ¥Œì€Å€µ¥¹¥µÕ´ì€É€µ•‘¥Õ´ì€Í€µ…á¥µÕ´ì€Ñ€Í¥±•¹Ðð)ðM]%9€ð€Á€=ì€Å€=8ð()Q¡”Í½ÕÉ”…±Í¼±…‰•±Ì•… ™¥•±9U11€™½ÈÕÉÉ•¹Ð½¥¹Í¥¹¥™¥…¹ÐÙ…±Õ•Ì°Ý¥Ñ¡½ÕÐ‘•™¥¹¥¹œ„±¥Ñ•É…°Ý¥É”ÍÁ•±±¥¹œ¸¼¹½ÐÑÉ…¹Íµ¥ÐÑ¡”±•ÑÑ•ÉÌ9U11€½È…ÍÍÕµ”„¹Õµ•É¥ŒÍ•¹Ñ¥¹•°Ý¥Ñ¡½ÕÐÑ…É•ÐµÍÁ•¥™¥Œ•Ù¥‘•¹”¸Q¡”µ½¹¥Ñ½ÈÑ…‰±”½µ¥ÑÌÑ¡”•áÁ±¥¥Ð€Ì€ÁÉ•™¥à™É½´¥ÑÌ…‘‘É•ÍÌ¹½Ñ”Ý¡¥±”Ñ¡”É•ÅÕ•ÍÐ½ÝÉ¥Ñ”Ñ…‰±•Ì¥¹±Õ‘”¥ÐìÉ•Ñ…¥¸É…Ü…‘‘É•ÍÍ•ÌÝ¡•¸É•½¹¥±¥¹œÑ¡½Í”É•Á½ÉÑÌ¸Q¡”ÝÉ¥Ñ”Ñ…‰±”…±Í¼É•Ù•ÉÍ•Ì¥ÑÌ‘¥É•Ñ¥½¸…ÉÉ½Üì¥ÑÌÝÉ¥Ñ”µ…É­•È…¹Í•Ñ¥½¸Ñ¥Ñ±”•ÍÑ…‰±¥Í „±¥•¹ÐÝÉ¥Ñ”¸()Q¡”‰É½…ÁÕ‰±¥Í¡•MA€É…¹”¥Ì…¸•¹½‘¥¹œÉ…¹”°¹½Ð„±…¥´Ñ¡…Ð„Á…ÉÑ¥Õ±…ÈÍÁ±¥ÐÕ¹¥Ð…•ÁÑÌ•Ù•ÉäÑ•µÁ•É…ÑÕÉ”¸((ŒŒŒ%59M%=8€ÌÁ€€´¡½±¥‘…ä•¹()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÄÕ€()AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()Q¡”•¹ÑÉ…°Õ¹¥ÐÕÍ•ÌÍ•Á…É…Ñ”‘…Ñ”…¹Ñ¥µ”‘¥µ•¹Í¥½¹Ì€¡Á…•Ì€ÔÐ°€ÔßŠLÔà¤è()ð=Á•É…Ñ¥½¸ðI•ÅÕ•ÍÐðI•ÍÁ½¹Í”½•Ù•¹Ðð]É¥Ñ”ð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð¹‘…Ñ”ð€¨ŒÐ¨ŒÀ¨ÌÀŒ€ð€¨ŒÐ¨ŒÀ¨ÌÀ©©4©dŒ€ð€¨ŒÐ¨ŒÀ¨ŒÌÀ©©4©dŒ€ð)ð¹Ñ¥µ”ð€¨ŒÐ¨ŒÀ¨ÌÄŒ€ð€¨ŒÐ¨ŒÀ¨ÌÄ© ©5%8Œ€ð€¨ŒÐ¨ŒÀ¨ŒÌÄ© ©5%8Œ€ð()€¥Ì€ÀÄ¸¸ÌÅ€°5€¥Ì€ÀÄ¸¸ÄÉ€°e€¥Ì€ÈÀÀÀ¸¸ÈÀäå€°!€¥Ì€ÀÀ¸¸ÈÍ€°…¹5%9€¥Ì€ÀÀ¸¸Ôå€¸Y…±¥‘…Ñ”Ñ¡”…ÑÕ…°…±•¹‘…È‘…Ñ”…ÌÝ•±°…Ì¥¹‘¥Ù¥‘Õ…°™¥•±É…¹•Ì¸()%59M%=8€ÌÅ€¥Ì½µ¥ÑÑ•™É½´Ñ¡”Í½ÕÉ”ÌÍÕµµ…ÉäÑ…‰±”‰ÕÐ•áÁ±¥¥Ñ±ä‘•™¥¹•‰ä¥ÑÌ‘•Ñ…¥±•™±½ÝÌ¸M½µ”É•…•á…µÁ±•Ìµ¥ÍÑ…­•¹±ä¥¹±Õ‘”Ñ¡”ÝÉ¥Ñ”µ…É­•ÈìÑ¡”É•ÍÁ½¹Í”½±Õµ¸…¹µ½¹¥Ñ½È™½ÉµÌ•ÍÑ…‰±¥Í Ñ¡”Õ¹ÁÉ•™¥á•É•Á½ÉÐ™½É´¸Q¡•Í”½Á•É…Ñ¥½¹ÌÍ•ÐÑ¡”‘•…‘±¥¹”ÕÍ•‰äÑ¡”mQ•µÁ•É…ÑÕÉ”½¹ÑÉ½°½µµ…¹‘Ít¡Ý¡…Ð¹µ¤¸((ŒŒŒQ•µÁ•É…ÑÕÉ”™¥•±‘Ì…É”½Á•É…Ñ¥½¸µÍÁ•¥™¥Œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÄÙ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()Q•µÁ•É…ÑÕÉ”µ±½½­¥¹œÙ…±Õ•Ì¥¸]!<€Ñ€‘¼¹½Ð¡…Ù”½¹”Õ¹¥Ù•ÉÍ…°É…¹”½ÈÉ•Í½±ÕÑ¥½¸¸%¸Á…ÉÑ¥Õ±…Èè()ð½¹Ñ•áÐðAÕ‰±¥Í¡•É•ÁÉ•Í•¹Ñ…Ñ¥½¸ð)ð€´´´ð€´´´ð)ð5•…ÍÕÉ•½ÍÑ…ÑÕÌÑ•µÁ•É…ÑÕÉ”ð™½ÕÈ‘¥¥ÑÌ°ÑåÁ¥…±±ä€À¸Äƒ
ÁÉ•Í½±ÕÑ¥½¸ð)ð5…¹Õ…°é½¹”½•¹ÑÉ…°µÕ¹¥ÐÍ•ÑÁ½¥¹ÐÝÉ¥Ñ”ð€ÀÀÔÀ¸¸ÀÐÀÁ€°€À¸Ôƒ
ÁÍÑ•ÁÌð)ð5å!=5}MÕ¥Ñ”M•¹…É¥½•Ù¥•Ì%59M%=8€Ý€Í•ÑÁ½¥¹Ðð™½ÕÈµ‘¥¥ÐŒÅŒÉŒÍŒÑ€™¥•±ìÕÍ”Ñ¡”…ÍÍ½¥…Ñ•¥µÁ±•µ•¹Ñ…Ñ¥½¸Á…É…µ•Ñ•È‘•™¥¹¥Ñ¥½¸™½ÈÙ…±¥‘…Ñ¥½¸ð)ð=Ñ¡•È5å!=5}MÕ¥Ñ”½µµ…¹Á…É…µ•Ñ•ÉÌðÉ…¹”½ÍÑ•À‘•™¥¹•‰äÑ¡”…ÍÍ½¥…Ñ•Á…É…µ•Ñ•ÈÉ•½Éð()•½‘•ÉÌ…¹•¹½‘•ÉÌÍ¡½Õ±Ñ¡•É•™½É”Í•±•ÐÑ¡”Ñ•µÁ•É…ÑÕÉ”É•ÁÉ•Í•¹Ñ…Ñ¥½¸™É½´Ñ¡”%59M%=9€½½Á•É…Ñ¥½¸‘•™¥¹¥Ñ¥½¸°¹½Ð™É½´]!<€Ñ€…±½¹”¸()M•”m‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤™½Èé½¹”½ÁÉ½‰”½…ÑÕ…Ñ½È™½ÉµÌ°m]!Q€I•™•É•¹•t¡Ý¡…Ð¹µ¤™½È½Á•É…Ñ¥¹œµ½‘•Ì°mÉ½ÍÌµ‘…Ñ…‰…Í”™Õ¹Ñ¥½¹…°½Ù•É…•t ¸¸½É½ÍÌµ‘…Ñ…‰…Í”µ½Ù•É…”¹µ¤™½ÈÑ¡”¥µÁ±•µ•¹Ñ…Ñ¥½¸É½ÍÌµÉ•™•É•¹”°…¹m%59M%=9t ¸¸¼¸¸½ÁÉ½Ñ½½°½‘¥µ•¹Í¥½¹Ì¹µ¤™½ÈÑ¡”½µµ½¸%59M%=9€™É…µ”±…ÍÍ•Ì¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀØäéÌÀÀÀÀÄÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÙ•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()AÕ‰±¥Í¡•Á…å±½…‘Ì…¹Á…”É•™•É•¹•Ì…‰½Ù”½µ”™É½´Ñ¡”mQ•µÁ•É…ÑÕÉ”½¹ÑÉ½°MÁ•¥™¥…Ñ¥½¹t ¸¸¼¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½]!=|Ð¹Á‘˜¤°Ù•ÉÍ¥½¸€È¸À¸À¸M•¹…É¥½•Ù¥•Ì•áÑ•¹Í¥½¹Ì…¹É•Á½ÉÑ•±…Ñ•Èµ‘•Ù¥”‰•¡…Ù¥½ÈÉ•µ…¥¸Í•Á…É…Ñ•±ä¥‘•¹Ñ¥™¥•¸Q¡”Í…µ”A…±Í¼‘•™¥¹•ÌmQ•µÁ•É…ÑÕÉ”½¹ÑÉ½°…Õ±Ð¥…¹½ÍÑ¥Ít ¸¸¼¸¸½‘¥…¹½ÍÑ¥Ì½Ñ•µÁ•É…ÑÕÉ”µ½¹ÑÉ½°µ™…Õ±ÑÌ¹µ¤Õ¹‘•È]!<€ÄÀÀÑ€ìÑ¡½Í”…É”¹½Ð™Õ¹Ñ¥½¹…°]!<€Ñ€‘¥µ•¹Í¥½¹Ì¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜÀ()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´ÐµÑ•µÁ•É…ÑÕÉ”µ½¹ÑÉ½°½Ý¡…Ð¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èÑ€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒ]!Q€I•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÀéÌÀÀÀÀÀÅ€()]!<€Ñ€ÕÍ•Ì]!Q€‰½Ñ ™½È‘¥É•ÐQ•µÁ•É…ÑÕÉ”½¹ÑÉ½°½µµ…¹‘Ì…¹™½È½Á•É…Ñ¥¹œµÍÑ…Ñ”½•Ù•¹ÐÉ•Á½ÉÑ¥¹œ¸M•Ù•É…°Ù…±Õ•Ì•¹½‘”Ñ¡”…Ñ¥Ù”¡•…Ñ¥¹œ½½¹‘¥Ñ¥½¹¥¹œ½•¹•É¥Œµ½‘”Ñ½•Ñ¡•ÈÝ¥Ñ Ñ¡”½Á•É…Ñ¥¹œµ½‘”¸((ŒŒŒ	…Í¥Œ½Á•É…Ñ¥¹œÍÑ…Ñ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÀéÌÀÀÀÀÀÉ€()ð]!Q€ð5•…¹¥¹œð)ð€´´´ð€´´´ð)ð€Á€ð½¹‘¥Ñ¥½¹¥¹œµ½‘”ð)ð€Å€ð!•…Ñ¥¹œµ½‘”ð)ð€ÈÁ€ðI•µ½Ñ”½¹ÑÉ½°‘¥Í…‰±•ð)ð€ÈÅ€ðI•µ½Ñ”½¹ÑÉ½°•¹…‰±•ð)ð€ÈÉ€ðÐ±•…ÍÐ½¹”ÁÉ½‰”=ð)ð€ÈÍ€ðÐ±•…ÍÐ½¹”ÁÉ½‰”¥¸…¹Ñ¥™É••é”ð)ð€ÈÑ€ðÐ±•…ÍÐ½¹”ÁÉ½‰”¥¸µ…¹Õ…°µ½‘”ð)ð€ÌÁ€ð…¥±ÕÉ”‘•Ñ•Ñ•ð)ð€ÌÅ€ð•¹ÑÉ…°µÕ¹¥Ð‰…ÑÑ•Éä™…Õ±Ðð)ð€ÐÁ€ðI•±•…Í”±½…°ÁÉ½‰”…‘©ÕÍÑµ•¹Ðð((ŒŒŒAÉ½Ñ•Ñ¥½¸…¹=ÍÑ…Ñ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÀéÌÀÀÀÀÀÍ€()ð]!Q€ð5•…¹¥¹œð)ð€´´´ð€´´´ð)ð€ÄÀÉ€ð¹Ñ¥™É••é”ð)ð€ÈÀÉ€ðQ¡•Éµ…°ÁÉ½Ñ•Ñ¥½¸ð)ð€ÌÀÉ€ð•¹•É¥ŒÁÉ½Ñ•Ñ¥½¸ð)ð€ÄÀÍ€ð=€´¡•…Ñ¥¹œð)ð€ÈÀÍ€ð=€´½¹‘¥Ñ¥½¹¥¹œð)ð€ÌÀÍ€ð=€´•¹•É¥Œð()¹Ñ¥™É••é”¥ÌÑ¡”¡•…Ñ¥¹œµÍ¥‘”ÁÉ½Ñ•Ñ¥½¸ÍÑ…Ñ”ìÑ¡•Éµ…°ÁÉ½Ñ•Ñ¥½¸¥ÌÑ¡”½¹‘¥Ñ¥½¹¥¹œµÍ¥‘”ÁÉ½Ñ•Ñ¥½¸ÍÑ…Ñ”¸•¹•É¥Œ™½ÉµÌ…É”ÕÍ•Ý¡•É”Ñ¡”½Á•É…Ñ¥¹œµ½‘”¥Ì¹½ÐÍÁ•¥…±¥é•Ñ¼¡•…Ñ¥¹œ½È½¹‘¥Ñ¥½¹¥¹œ¸((ŒŒŒ5…¹Õ…°…¹ÁÉ½É…µµ•½Á•É…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÀéÌÀÀÀÀÀÑ€()ð]!Q€ð5•…¹¥¹œð)ð€´´´ð€´´´ð)ð€ÄÄÁ€ð5…¹Õ…°…‘©ÕÍÑµ•¹Ð€´¡•…Ñ¥¹œð)ð€ÈÄÁ€ð5…¹Õ…°…‘©ÕÍÑµ•¹Ð€´½¹‘¥Ñ¥½¹¥¹œð)ð€ÌÄÁ€ð5…¹Õ…°…‘©ÕÍÑµ•¹Ð€´•¹•É¥Œð)ð€ÄÄÅ€ðAÉ½É…µµ•½…ÕÑ½µ…Ñ¥Œ€´¡•…Ñ¥¹œð)ð€ÈÄÅ€ðAÉ½É…µµ•½…ÕÑ½µ…Ñ¥Œ€´½¹‘¥Ñ¥½¹¥¹œð)ð€ÌÄÅ€ðAÉ½É…µµ•½…ÕÑ½µ…Ñ¥Œ€´•¹•É¥Œð)ð€ÄÄÕ€ð…¥±ä¡½±¥‘…äÁ±…¸€´¡•…Ñ¥¹œð)ð€ÈÄÕ€ð…¥±ä¡½±¥‘…äÁ±…¸€´½¹‘¥Ñ¥½¹¥¹œð)ð€ÌÄÕ€ð…¥±ä¡½±¥‘…äÁ±…¸€´•¹•É¥Œð()é½¹”½¹ÑÉ½±±•Ñ¡É½Õ Ñ¡”•¹ÑÉ…°Õ¹¥ÐÕÍ•Ì•¹ÑÉ…°µÕ¹¥Ð…‘‘É•ÍÍ¥¹œì™½È•á…µÁ±”°…ÕÑ½µ…Ñ¥Œ•¹•É¥Œ½Á•É…Ñ¥½¸¥Ì½µµ…¹‘•Ý¥Ñ €¨Ð¨ÌÄÄ¨]!IŒ€™½ÈÑ¡”Í•±•Ñ•é½¹”¸((ŒŒŒY……Ñ¥½¸°ÁÉ½É…´…¹Í•¹…É¥¼™½ÉµÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÀéÌÀÀÀÀÀÕ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€°µÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()Q¡•Í”½Á•É…Ñ¥½¹ÌÑ…É•ÐÑ¡”•¹ÑÉ…°Õ¹¥ÐÝ¥Ñ ]!I€ô€ŒÁ€¸Q¡”‘•Ñ…¥±•™±½ÝÌ½¸Á…•Ì€ÈçŠLÔÈ•ÍÑ…‰±¥Í Ñ¡”™½±±½Ý¥¹œÙ…±Õ•ÌìÑ¡”ÍÕµµ…ÉäÑ…‰±”½¸Á…”€Ô½¹Ñ…¥¹ÌÍ¡¥™Ñ•½µ¥Íµ…Ñ¡•‘•ÍÉ¥ÁÑ¥½¹Ì…¹µÕÍÐ¹½Ð½Ù•ÉÉ¥‘”Ñ¡•´¸()ð=Á•É…Ñ¥½¸ð!•…Ñ¥¹œð½¹‘¥Ñ¥½¹¥¹œð•¹•É¥Œ½ÕÉÉ•¹Ð½¹Ñ•áÐð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð]••­±äÁÉ½É…´€Ä¸¸Í€ð€ÄÄÀÄ¸¸ÄÄÀÍ€ð€ÈÄÀÄ¸¸ÈÄÀÍ€ð€ÌÄÀÄ¸¸ÌÄÀÍ€ð)ðI•ÍÑ½É”±…ÍÐÝ••­±äÁÉ½É…´ð€´ð€´ð€ÌÄÀÁ€ð)ðM•¹…É¥¼€Ä¸¸ÄÙ€ð€ÄÈÀÄ¸¸ÄÈÄÙ€ð€ÈÈÀÄ¸¸ÈÈÄÙ€ð€ÌÈÀÄ¸¸ÌÈÄÙ€ð)ðI•ÍÑ½É”±…ÍÐÍ•¹…É¥¼ð€´ð€´ð€ÌÈÀÁ€ð)ð…¥±ä¡½±¥‘…äÁ±…¸°Ñ¡•¸É•ÑÕÉ¸Ñ¼ÁÉ½É…´ð€ÄÄÔAI=I5€ð€ÈÄÔAI=I5€ð€ÌÄÔAI=I5€ð)ðY……Ñ¥½¸™½È€‘…åÌ°Ñ¡•¸É•ÑÕÉ¸Ñ¼ÁÉ½É…´ð€ÄÍAI=I5€ð€ÈÍAI=I5€ð€ÌÍAI=I5€ð)ð…¹•°Ù……Ñ¥½¸…¹¡½½Í”Ý••­±äÁÉ½É…´ð€´ð€´ð€ÌÀÀÀAI=I5€ð)ð…¹•°Ù……Ñ¥½¸…¹É•ÍÑ½É”±…ÍÐÝ••­±äÁÉ½É…´ð€´ð€´ð€ÌÀÀÁ€ð()€¥Ì„Ñ¡É•”µ‘¥¥Ð‘…ä½Õ¹Ð¸Q¡”ÍÕµµ…ÉäÑ…‰±”±¥ÍÑÌ€ÀÀÀ¸¸ääå€°‰ÕÐÑ¡”‘•Ñ…¥±•½µµ…¹™±½ÝÌÉ•ÍÑÉ¥Ð¥ÐÑ¼€ÀÀÄ¸¸ÈÔÕ€ìÕÍ”Ñ¡…Ð¹…ÉÉ½Ý•È‘½µ…¥¸Ý¡•¸•¹½‘¥¹œÑ¡•Í”‘½Õµ•¹Ñ•½µµ…¹‘Ì¸Q¡”Ù……Ñ¥½¸•á…µÁ±•ÌÍ•¹€ÄÌÀÀÈŒÌÄÀÍ€°€ÈÌÀÀÈŒÌÄÀÍ€°½È€ÌÌÀÀÈŒÌÄÀÍ€™½ÈÑÝ¼‘…åÌ™½±±½Ý•‰äÝ••­±äÁÉ½É…´€Ì¸Q¡”Í½ÕÉ”¹½Ñ•ÌÑ¡…ÐÑ¡”É•Á½ÉÑ•É•µ…¥¹¥¹œÁ•É¥½¥¹±Õ‘•ÌÑ¡”ÕÉÉ•¹Ð‘…ä°Í¼¥ÑÌ½ÉÉ•ÍÁ½¹‘¥¹œ•Ù•¹Ð•á…µÁ±•ÌÉ•Á½ÉÐ€ÄÌÀÀÍ€°€ÈÌÀÀÍ€°½È€ÌÌÀÀÍ€ì‘¼¹½Ð‘•µ…¹‰åÑ”•ÅÕ…±¥Ñä‰•ÑÝ••¸Ñ¡”½µµ…¹…¹¥ÑÌ•Ù•¹Ð¸()½È‘…¥±ä¡½±¥‘…ä½µµ…¹‘Ì°Ñ¡”É•ÑÕÉ¸µÁÉ½É…´Á…É…µ•Ñ•È¥Ì€ÄÄÀÄ¸¸ÄÄÀÍ€™½È¡•…Ñ¥¹œ°€ÈÄÀÄ¸¸ÈÄÀÍ€™½È½¹‘¥Ñ¥½¹¥¹œ°…¹€ÌÄÀÄ¸¸ÌÄÀÍ€™½È•¹•É¥Œµ½‘”¸Q¡”µÕ±Ñ¤µ‘…äÙ……Ñ¥½¸½µµ…¹‘ÌÕÍ”€ÌÄÀÄ¸¸ÌÄÀÍ€¥¸…±°Ñ¡É•”½¹Ñ•áÑÌ¸…¥±äµ¡½±¥‘…ä•Ù•¹Ð•á…µÁ±•Ì¥¹ÍÑ•…Í¡½ÜÑ¡”Í•±•Ñ•½É‘¥¹…°…™Ñ•È€ÄÄÔ€½È€ÈÄÔ€¸I•Ñ…¥¸Ñ¡…Ð½µµ…¹½É•Á½ÉÐ‘¥ÍÑ¥¹Ñ¥½¸¸Q¡”‘•…‘±¥¹”¥ÑÍ•±˜¥ÌÍ•Ð½É•…Ý¥Ñ m¡½±¥‘…ä‘…Ñ”…¹Ñ¥µ”ÁÉ½Á•ÉÑ¥•Ít¡‘¥µ•¹Í¥½¹Ì¹µ‘¥µ•¹Í¥½¸´ÌÀ´´µ¡½±¥‘…äµ•¹¤¸()á…µÁ±”è€¨Ð¨ÌÄÀÈ¨ŒÀŒ€Í•±•ÑÌÝ••­±äÁÉ½É…´€È¥¸Ñ¡”ÕÉÉ•¹ÐÑ¡•Éµ…°½¹Ñ•áÐ¸É•Á±ä½•Ù•¹Ð…¸ÕÍ”Ñ¡”É•Í½±Ù•¡•…Ñ¥¹œ½È½¹‘¥Ñ¥½¹¥¹œÁÉ½É…´½‘”¸¸…­¹½Ý±•‘•µ•¹Ð½¹™¥ÉµÌÍÕ‰µ¥ÍÍ¥½¸°¹½ÐÑ¡…ÐÑ¡”É•ÅÕ•ÍÑ•µ½‘”Ý…ÌÁ¡åÍ¥…±±ä…ÑÑ…¥¹•¸((ŒŒŒi½¹”Í•ÑÕÀ½µµ…¹‘Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÀéÌÀÀÀÀÀÙ€()i½¹”Í•ÑÕÀ¥ÌÁ•É™½Éµ•Ñ¡É½Õ Ñ¡”•¹ÑÉ…°Õ¹¥ÐÕÍ¥¹œ]!I€™½ÉµÌ€ŒÄ¸¸Œäå€¸()ð=Á•É…Ñ¥½¸ðÉ…µ”™½É´ð)ð€´´´ð€´´´ð)ð5…¹Õ…°Í•ÑÁ½¥¹Ðð€¨ŒÐ¨]!I¨ŒÄÐ©P©4Œ€ð)ðÕÑ½µ…Ñ¥Œ½ÁÉ½É…µµ•µ½‘”ð€¨Ð¨ÌÄÄ¨]!IŒ€ð)ð=ð€¨Ð¨ÌÀÌ¨]!IŒ€ð)ð¹Ñ¥™É••é”ð€¨Ð¨ÄÀÈ¨]!IŒ€ð)ðQ¡•Éµ…°ÁÉ½Ñ•Ñ¥½¸ð€¨Ð¨ÈÀÈ¨]!IŒ€ð)ð•¹•É¥ŒÁÉ½Ñ•Ñ¥½¸ð€¨Ð¨ÌÀÈ¨]!IŒ€ð()½ÈÑ¡”µ…¹Õ…°Í•ÑÁ½¥¹Ð½Á•É…Ñ¥½¸°Q€¥Ì„™½ÕÈµ‘¥¥ÐÑ•µÁ•É…ÑÕÉ”Ù…±Õ”¥¸€ÀÀÔÀ¸¸ÀÐÀÁ€Ý¥Ñ €À¸Ôƒ
ÁÍÑ•ÁÌ¸5€¥‘•¹Ñ¥™¥•ÌÑ¡”½Á•É…Ñ¥¹œ½¹Ñ•áÐè€Å€¡•…Ñ¥¹œ°€É€½¹‘¥Ñ¥½¹¥¹œ°€Í€•¹•É¥Œ¸()ÍÕ•ÍÍ™Õ°½µµ…¹µÍ•ÍÍ¥½¸ÍÕ‰µ¥ÍÍ¥½¸¥Ì…­¹½Ý±•‘•Ý¥Ñ -€ì™…¥±ÕÉ”Ñ¼ÍÕ‰µ¥ÐÑ¡”½µµ…¹Ñ¼Ñ¡”‰ÕÌ¥ÌÉ•Á½ÉÑ•Ý¥Ñ 9-€¸()M•”m‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤™½ÈÁÉ½‰”°é½¹”…¹•¹ÑÉ…°µÕ¹¥Ð]!I€™½ÉµÌ…¹m%59M%=9€I•™•É•¹•t¡‘¥µ•¹Í¥½¹Ì¹µ¤™½ÈÑ•µÁ•É…ÑÕÉ”½ÍÑ…ÑÕÌÁ…å±½…‘Ì¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜÄ()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´ÐµÑ•µÁ•É…ÑÕÉ”µ½¹ÑÉ½°½é¥‰•”µÙ…É¥…¹Ð¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èÑ€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒi¥	•”Y…É¥…¹Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÄéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€°ÍÍ€°Ù•ÉÍ¥½¹€°é¥‰••€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡”i¥	•”=Á•¹]•‰9•ÐÙ•ÉÍ¥½¸€Ð¸ÀÍÁ•¥™¥…Ñ¥½¸‘•™¥¹•Ì„‘•±¥‰•É…Ñ•±ä¹…ÉÉ½Ü]!<€Ñ€Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°ÍÕÉ™…”™½ÈÑ¡”1•É…¹Í•É¥…°i¥	•”¥¹Ñ•É™…”¸%¸Ñ¡”¥¹ÍÁ•Ñ•Í•Ñ¥½¸°]!<€Ñ€¥ÌÕÍ•Ñ¼É••¥Ù”Ñ•µÁ•É…ÑÕÉ”É•Á½ÉÑÌ™É½´„i¥	•”ÁÉ½‰”¸%Ð‘½•Ì¹½Ð‘•™¥¹”Ñ¡”‰É½…MLé½¹”°•¹ÑÉ…°µÕ¹¥Ð°…ÑÕ…Ñ½È°Í•ÑÁ½¥¹Ð°ÁÉ½É…´°½ÈÍÁ±¥Ðµ½¹ÑÉ½°µ½‘•°‘½Õµ•¹Ñ••±Í•Ý¡•É”¥¸Ñ¡¥Ì¹…µ•ÍÁ…”¸()Q¡”Í½ÕÉ”¥Ìmi¥	•”=Á•¹]•‰9•ÐMÁ•¥™¥…Ñ¥½¹t ¸¸¼¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=Á•¹]•‰9•Ñ}i¥‰•”¹Á‘˜¤°Ù•ÉÍ¥½¸€Ð¸À‘…Ñ•€ÈÈ9½Ù•µ‰•È€ÈÀÄØ¸%ÑÌ½¹™¥‘•¹Ñ¥…°™½½Ñ•È…¹Õ¹É•Í½±Ù•ÁÕ‰±¥ŒµÉ•±•…Í”ÁÉ½Ù•¹…¹”É•µ…¥¸É•½É‘•¥¸Ñ¡”mM½ÕÉ”µ½Ù•É…”Õ‘¥Ñt ¸¸¼¸¸½ÁÉ½©•Ð½É•Ù¥•Ü½Á¡…Í”´ÌµÍ½ÕÉ”µ½Ù•É…”¹µ¤¸Q¡”µ…Ñ•É¥…°‰•±½Ü¥Ì€¨©ÍÁ•¥™¥…Ñ¥½¸•Ù¥‘•¹”™½ÈÑ¡¥Ì¥¹Ñ•É™…”É•Ù¥Í¥½¸¨¨¸((ŒŒŒ½Õµ•¹Ñ•ÍÕÉ™…”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÄéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€°é¥‰••€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”i¥	•”]!<€Ñ€Í•Ñ¥½¸½¹Ñ…¥¹Ì¹¼]!Q€•¹ÑÉ¥•Ì¸%ÑÌ%59M%=9€Ñ…‰±”‘•™¥¹•Ì½¹±äè()ð%59M%=9€ði¥	•”ÍÁ•¥™¥…Ñ¥½¸µ•…¹¥¹œð¥É•Ñ¥½¸•ÍÑ…‰±¥Í¡•‰äÑ¡”Í•Ñ¥½¸ð)ð€´´´ð€´´´ð€´´´ð)ð€Á€ðQ•µÁ•É…ÑÕÉ”±•Ù•°ðÍ•ÉÙ•ÈÑ¼±¥•¹Ðð()Q¡”É•Á½ÉÐ™½É´¥Ìè()€¨ŒÐ©]!IŒä¨À©1Y0Œ€()]!I€ÕÍ•ÌÑ¡”mi¥	•”ÁÉ½‘ÕÐµ…¹µU¹¥Ð…‘‘É•ÍÌ™…µ¥±åt ¸¸¼¸¸½ÁÉ½Ñ½½°½é¥‰•”µ¥¹Ñ•É™…”¹µÑÉ…¹ÍÁ½ÉÐµ…¹µ…‘‘É•ÍÍ¥¹œ¤°¹½ÐÑ¡”MLQ•µÁ•É…ÑÕÉ”½¹ÑÉ½°é½¹”½ÁÉ½‰”É…µµ…È¸()Q¡”Í•Ñ¥½¸‘•™¥¹•Ì¹¼]!<€Ñ€É•ÅÕ•ÍÐ™É…µ”™½ÈÑ¡¥ÌÙ…±Õ”¸±¥•¹ÐµÍ¥‘”µ•…ÍÕÉ•µÑ•µÁ•É…ÑÕÉ”É•ÅÕ•ÍÐÍÕ …ÌÑ¡”½¹”‘½Õµ•¹Ñ•™½ÈMLµÕÍÐÑ¡•É•™½É”¹½Ð‰”¥¹™•ÉÉ•™½ÈÑ¡¥Ìi¥	•”¥¹Ñ•É™…”™É½´Ñ¡”Í¡…É•%59M%=8€Á€¥‘•¹Ñ¥™¥•È¸((ŒŒŒQ•µÁ•É…ÑÕÉ”•¹½‘¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÄéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()1Y1€¥Ì™½ÕÈ‘¥¥ÑÌÅÉÍÑ€è()ð¥•±ð5•…¹¥¹œð)ð€´´´ð€´´´ð)ðÅ€ðÍ¥¸è€Á€Á½Í¥Ñ¥Ù”°€Å€¹•…Ñ¥Ù”ð)ðÉÍ€ðÝ¡½±”µÑ•µÁ•É…ÑÕÉ”Ñ•¹Ì…¹Õ¹¥ÑÌð)ðÑ€ð‘•¥µ…°‘¥¥Ð¥¸€À¸Äƒ
ÁÍÑ•ÁÌð()Q¡”Í½ÕÉ”•á…µÁ±•Ì‘•µ½¹ÍÑÉ…Ñ”‰½Ñ Á½Í¥Ñ¥Ù”…¹¹•…Ñ¥Ù”Ù…±Õ•Ì¸%Ð‘½•Ì¹½ÐÍÑ…Ñ”„½µÁ±•Ñ”Ù…±¥Ñ•µÁ•É…ÑÕÉ”É…¹”‰•å½¹Ñ¡¥Ì™¥•±ÍÑÉÕÑÕÉ”°Í¼Ñ¡”•¹å±½Á•‘¥„‘½•Ì¹½Ð¥¹™•È½¹”™É½´Ñ¡”¹Õµ‰•È½˜…Ù…¥±…‰±”‘¥¥ÑÌ¸()Q¡¥Ì•¹½‘¥¹œ¥Ìµ…Ñ•É¥…±±ä‘¥™™•É•¹Ð™É½´Ñ¡”MLµ½É¥•¹Ñ•%59M%=8€Á€É•ÁÉ•Í•¹Ñ…Ñ¥½¸‘½Õµ•¹Ñ•¥¸m%59M%=9€I•™•É•¹•t¡‘¥µ•¹Í¥½¹Ì¹µ¤¸Q¡”ÑÝ¼Á…å±½…‘ÌµÕÍÐ‰”Í•±•Ñ•‰ä¥¹Ñ•É™…”Ù…É¥…¹ÐÉ…Ñ¡•ÈÑ¡…¸‘•½‘•Ñ¡É½Õ ½¹”Í¡…É•Ñ•µÁ•É…ÑÕÉ”ÉÕ±”¸((ŒŒŒAÉ¥½ÈÁÉ½•‘ÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÄéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìèé¥‰••€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()Q¡”Í½ÕÉ”ÍÑ…Ñ•ÌÑ¡…ÐÑ¡”ÁÉ½‰”µÕÍÐÁÉ•Ù¥½ÕÍ±ä¡…Ù”½µÁ±•Ñ•„Í½ÕÉ”µ¹…µ•€‰A¹0ˆÁÉ½•‘ÕÉ”Ý¥Ñ Ñ¡”=Á•¹]•‰9•Ð¥¹Ñ•É™…”…¹Á½¥¹ÑÌÑ¼Ñ¡”]!<€ÈÕ€ÕÍ”…Í•Ì¸()Q¡¥Ì•ÍÑ…‰±¥Í¡•Ì„ÁÉ•É•ÅÕ¥Í¥Ñ”¥¸Ñ¡”Í½ÕÉ”Ìi¥	•”Ý½É­™±½Ü‰ÕÐ‘½•Ì¹½Ð•ÍÑ…‰±¥Í Ñ¡”Õ¹‘•É±å¥¹œi¥	•”É…‘¥¼ÁÉ½•‘ÕÉ”…Ì=Á•¹]•‰9•Ð¸M•”mi¥	•”	¥¹‘¥¹t ¸¸½Ý¡¼´ÈÔµÑÉ…¹ÍÙ•ÉÍ…°½é¥‰•”µ‰¥¹‘¥¹œ¹µ¤™½ÈÑ¡”=Á•¹]•‰9•ÐµÙ¥Í¥‰±”]!<€ÈÕ€±¥™•å±”¸((ŒŒŒÙ¥‘•¹”±¥µ¥ÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÄéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€°Ù•ÉÍ¥½¹€°é¥‰••€)…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()Q¡”…‰Í•¹”½˜½Ñ¡•È]!Q€…¹%59M%=9€Ù…±Õ•Ì™É½´Ñ¡¥Ìi¥	•”Í•Ñ¥½¸µ•…¹ÌÑ¡…ÐÙ•ÉÍ¥½¸€Ð¸À‘½•Ì¹½Ð•ÍÑ…‰±¥Í Ñ¡•´™½ÈÑ¡¥Ì¥¹Ñ•É™…”¸%Ð¥Ì¹½Ð„Õ¹¥Ù•ÉÍ…°ÍÑ…Ñ•µ•¹ÐÑ¡…Ð¹¼i¥	•”Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°¥µÁ±•µ•¹Ñ…Ñ¥½¸…¸•áÁ½Í”…‘‘¥Ñ¥½¹…°=Á•¹]•‰9•Ð½Á•É…Ñ¥½¹Ì¸()%¸Á…ÉÑ¥Õ±…È°Ñ¡”ML•¹ÑÉ…°µÕ¹¥Ðµ½‘•Ì°é½¹”½µµ…¹‘Ì°%59M%=8€ÄÄ¸¸ÌÅ€°…ÑÕ…Ñ½È…‘‘É•ÍÍ¥¹œ°…¹ÍÁ±¥Ðµ½¹ÑÉ½°½Á•É…Ñ¥½¹ÌµÕÍÐ¹½Ð‰”ÑÉ…¹Í™•ÉÉ•Ñ¼Ñ¡¥ÌÙ…É¥…¹Ð‰ä¹…µ•ÍÁ…”•ÅÕ…±¥Ñä¸()M•”mQ•µÁ•É…ÑÕÉ”½¹ÑÉ½±t¡I5¹µ¤™½ÈÑ¡”‰É½…‘•ÈMLµ½É¥•¹Ñ•¹…µ•ÍÁ…”…¹mi¥	•”=Á•¹]•‰9•Ð%¹Ñ•É™…•t ¸¸¼¸¸½ÁÉ½Ñ½½°½é¥‰•”µ¥¹Ñ•É™…”¹µ¤™½È½µµ½¸i¥	•”ÑÉ…¹ÍÁ½ÉÐ…¹…‘‘É•ÍÍ¥¹œ¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜÈ()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´Ôµ…±…É´½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èÕ€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒ]!<€Õ€€´±…É´()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÈéÌÀÀÀÀÀÅ€()]!<€Õ€‘•™¥¹•ÌÑ¡”=Á•¹]•‰9•Ð	ÕÉ±…È±…É´ÍåÍÑ•´¸Q¡”ÁÕ‰±¥Í¡•ÁÉ½Ñ½½°¥ÌÁÉ¥µ…É¥±ä„µ½¹¥Ñ½É¥¹œ…¹ÍÑ…Ñ”µÉ•Á½ÉÑ¥¹œ¥¹Ñ•É™…”è¥Ð•áÁ½Í•Ì•¹ÑÉ…°µÕ¹¥ÐÍÑ…Ñ”°é½¹”ÍÑ…Ñ”°…±…É´•Ù•¹ÑÌ°Á½Ý•È…¹‰…ÑÑ•Éä½¹‘¥Ñ¥½¹Ì°Ñ•¡¹¥…°…¹Í¥±•¹Ð…±…ÉµÌ°…¹„Íµ…±°Í•Ð½˜ÁÉ½É…µµ¥¹œµÉ•±…Ñ•½Á•É…Ñ¥½¹Ì¸((ŒŒŒI•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÈéÌÀÀÀÀÀÉ€()ðMÕ‰©•ÐðA…”ð)ð€´´´ð€´´´ð)ðM•ÍÍ¥½¸‰•¡…Ù¥½È…¹ÍÑ…ÑÕÌÉ•Á½ÉÑ¥¹œðmAÉ½Ñ½½±t¡ÁÉ½Ñ½½°¹µ¤ð)ðAÕ‰±¥Í¡•]!Q€Ù½…‰Õ±…Éäðm]!Q€I•™•É•¹•t¡Ý¡…Ð¹µ¤ð)ð•¹ÑÉ…°Õ¹¥Ð°é½¹”°Í•¹Í½È…¹…Õá¥±¥…Éä…‘‘É•ÍÍ¥¹œðm‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤ð((ŒŒŒMÑ…Ñ”µ½‘•°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÈéÌÀÀÀÀÀÍ€()±…É´ÑÉ…™™¥Œ¥Ì¹½ÐÉ•‘Õ¥‰±”Ñ¼½¹”…Éµ•½‘¥Í…Éµ•	½½±•…¸¸•¹ÑÉ…°µÕ¹¥ÐÍÑ…ÑÕÌÉ•ÅÕ•ÍÐ…¸ÁÉ½‘Õ”Í•Ù•É…°™É…µ•Ì‘•ÍÉ¥‰¥¹œÍåÍÑ•´µ½‘”°•¹…•µ•¹Ð°‰…ÑÑ•Éä…¹µ…¥¹Ì½¹‘¥Ñ¥½¹Ì°…Ñ¥Ù”½‘¥Ù¥‘•é½¹•Ì°…¹…±…É´½¹‘¥Ñ¥½¹Ì‰•™½É”Ñ¡”Ñ•Éµ¥¹…Ñ¥¹œ-€¸()i½¹”µÍÁ•¥™¥ŒÉ•ÅÕ•ÍÑÌÍ¥µ¥±…É±äÉ•Á½ÉÐÝ¡•Ñ¡•È„Í•±•Ñ•é½¹”¥Ì•¹…•½È‘¥Ù¥‘•¸±…É´•Ù•¹ÑÌ¥‘•¹Ñ¥™äÑ¡•¥ÈÍ½Á”Ñ¡É½Õ Ñ¡”]!<€Õ€]!I€É…µµ…È°Ý¡¥ ¥Ì¥¹‘•Á•¹‘•¹Ð½˜1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸€½A1€…‘‘É•ÍÍ¥¹œ¸()Q¡”ÁÕ‰±¥Í¡•¥¹Ñ•É™…”‘½•Ì¹½Ð‘•™¥¹”„•¹•É…°µÁÕÉÁ½Í”µ½‘•É¸Í•ÕÉ¥Ñäµ½¹ÑÉ½°A$¸%µÁ±•µ•¹Ñ…Ñ¥½¹ÌÍ¡½Õ±Ñ¡•É•™½É”•áÁ½Í”Ñ¡”‘½Õµ•¹Ñ•ÍÑ…Ñ•Ì…¹•Ù•¹ÑÌÝ¥Ñ¡½ÕÐ¥¹Ù•¹Ñ¥¹œÝÉ¥Ñ”Í•µ…¹Ñ¥Ì™½ÈÍÑ…ÑÕÌÙ…±Õ•ÌÑ¡…Ð…É”½¹±ä•ÍÑ…‰±¥Í¡•…ÌÉ•Á½ÉÑÌ¸()]!<€Õ€¥Ì‘¥ÍÑ¥¹Ð™É½´•ÍÌ½¹ÑÉ½°m]!<€ÈÍt ¸¸½Ý¡¼´ÈÌµ…•ÍÌµ½¹ÑÉ½°¼¤…¹™É½´‘¥…¹½ÍÑ¥ŒÁÉ½Ñ½½°™…µ¥±¥•Ì¸½µµ½¸™É…µ”½Í•ÍÍ¥½¸Íå¹Ñ…à¥Ì‘½Õµ•¹Ñ•Õ¹‘•ÈmAÉ½Ñ½½±t ¸¸¼¸¸½ÁÉ½Ñ½½°¼¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜÌ()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´Ôµ…±…É´½…‘‘É•ÍÍ¥¹œ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èÕ€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒ‘‘É•ÍÍ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÌéÌÀÀÀÀÀÅ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()AÕ‰±¥Í¡•]!<€Õ€]!I€Ù…±Õ•Ì¥¹±Õ‘”è()ð]!I€ð5•…¹¥¹œð)ð€´´´ð€´´´ð)ð€Å€ð½¹ÑÉ½°Á…¹•°ð)ð€ŒÀ¸¸Œá€ð•¹ÑÉ…°é½¹”€À¸¸á€ð)ð€ŒÄ¸¸Œå€ðÕá¥±¥…Éä€Ä¸¸å€€¡]!<€å€É•±…Ñ¥½¹Í¡¥À¥¸Ñ¡”ÁÕ‰±¥Í¡•Ñ…‰±”¤ð)ð€ÀÄ¸¸Á¹€ð%¹ÁÕÐµé½¹”‘•Ù¥”ð)ð€ÄÄ¸¸Å¹€ði½¹”€ÄÍ•¹Í½Èð)ð€àÄ¸¸á¹€ði½¹”€àÍ•¹Í½Èð)ð€ŒÄÉ€ði½¹”€¼U`ð)ð€ŒÄÕ€ði½¹”€¼U`ð()i½¹”€Á€¥ÌÕÍ•™½È¥¹ÁÕÑÌ…¹Ñ¡”Ñ¡É•”¥¹Ñ•É¹…°Í¥É•¹Ì¥¸Ñ¡”ÁÕ‰±¥Í¡•µ½‘•°¸±…É´…‘‘É•ÍÍ¥¹œ¥ÌÑ¡•É•™½É”¥ÑÌ½Ý¸]!<€Õ€É…µµ…È…¹µÕÍÐ¹½Ð‰”Á…ÉÍ•…Ì1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸½A0¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜÐ()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´Ôµ…±…É´½ÁÉ½Ñ½½°¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èÕ€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒAÉ½Ñ½½°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÐéÌÀÀÀÀÀÅ€()]!<€Õ€ÕÍ•Ì½É‘¥¹…Éä=Á•¹]•‰9•Ð½µµ…¹½•Ù•¹Ð™É…µ•ÌÑ½•Ñ¡•ÈÝ¥Ñ ÍÑ…ÑÕÌÉ•ÅÕ•ÍÑÌ¸Q¡”ÁÕ‰±¥Í¡•¥¹Ñ•É™…”¥ÌÍÑÉ½¹±äÍÑ…ÑÕÌµ½É¥•¹Ñ•…¹½™Ñ•¸É•ÑÕÉ¹Ì„Í•ÅÕ•¹”½˜ÍÑ…Ñ”™É…µ•Ì™½±±½Ý•‰ä-€¸((ŒŒŒ•¹ÑÉ…°µÕ¹¥ÐÍÑ…ÑÕÌÉ•ÅÕ•ÍÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÐéÌÀÀÀÀÀÉ€()•¹ÑÉ…°µÕ¹¥ÐÉ•ÅÕ•ÍÐÕÍ•Ì€¨ŒÔŒ€¸Q¡”É•ÍÁ½¹Í”…¸½¹Ñ…¥¸µÕ±Ñ¥Á±”]!<€Õ€™É…µ•Ì‰•™½É”€¨Œ¨ÄŒ€¸Q¡”ÁÕ‰±¥Í¡•É•ÍÁ½¹Í”Í•Ð½Ù•ÉÌµ…¥¹Ñ•¹…¹”½…Ñ¥Ù”ÍÑ…Ñ”°•¹…•½‘¥Í•¹…•ÍÑ…Ñ”°‰…ÑÑ•Éä½¹‘¥Ñ¥½¹Ì°µ…¥¹ÌÁÉ•Í•¹”°é½¹”•¹…•µ•¹Ð½‘¥Ù¥Í¥½¸°é½¹”…±…É´½¹‘¥Ñ¥½¹Ì°Ñ•¡¹¥…°…±…ÉµÌ…¹Í¥±•¹Ð…±…ÉµÌ¸()±¥•¹ÐµÕÍÐÑ¡•É•™½É”½±±•ÐÑ¡”½µÁ±•Ñ”É•ÍÁ½¹Í”Í•ÅÕ•¹”¸QÉ•…Ñ¥¹œÑ¡”™¥ÉÍÐÉ•ÑÕÉ¹•]!<€Õ€™É…µ”…ÌÑ¡”½µÁ±•Ñ”•¹ÑÉ…°µÕ¹¥ÐÍÑ…Ñ”±½Í•Ì¥¹‘•Á•¹‘•¹ÐÍÑ…Ñ”…á•Ì¸((ŒŒŒi½¹”ÍÑ…ÑÕÌÉ•ÅÕ•ÍÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÐéÌÀÀÀÀÀÍ€()é½¹”É•ÅÕ•ÍÐ™½±±½ÝÌ€¨ŒÔ¨8Œ€°Ý¥Ñ ÁÕ‰±¥Í¡•é½¹•Ì8€ô€Ä¸¸á€¸Q¡”É•ÍÁ½¹Í”¥‘•¹Ñ¥™¥•ÌÑ¡”é½¹”…Ì…Ñ¥Ù”½•¹…•Ý¥Ñ ]!P€ÄÅ€½È¹½¸µ…Ñ¥Ù”½‘¥Ù¥‘•Ý¥Ñ ]!P€Äá€°™½±±½Ý•‰ä-€¸()Q¡”€9€™½É´¥Ì„é½¹”Í•±•Ñ½È°¹½Ð„¹Õµ•É¥ŒÁ½¥¹ÐµÑ¼µÁ½¥¹Ð…‘‘É•ÍÌ¸M•”m‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤¸((ŒŒŒÙ•¹Ð½¹¹•Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÐéÌÀÀÀÀÀÑ€()±…É´ÍÑ…Ñ”¡…¹•Ì…É”…±Í¼•µ¥ÑÑ•…Ì•Ù•¹ÑÌ¸½¹ÍÕµ•ÉÌÍ¡½Õ±¹½Éµ…±¥é”•Ù•¹ÑÌÕÍ¥¹œÑ¡”Á…¥È€¡]!P°]!I¥€‰•…ÕÍ”Ñ¡”Í…µ”]!Q€™…µ¥±ä…¸‘•ÍÉ¥‰”•¹ÑÉ…°µÕ¹¥Ð°é½¹”°Í•¹Í½È°½È…Õá¥±¥…Éä½¹Ñ•áÐ‘•Á•¹‘¥¹œ½¸]!I€¸((ŒŒŒAÉ½É…µµ¥¹œÙ…±Õ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÐéÌÀÀÀÀÀÕ€()Q¡”ÁÕ‰±¥Í¡•Ù½…‰Õ±…Éä¥¹±Õ‘•Ì]!P€ÈÙ€…¹€ÈÝ€™½ÈÍÑ…ÉÐ½ÍÑ½ÀÁÉ½É…µµ¥¹œ¸Q¡•Í”‰•±½¹œÑ¼Ñ¡”¡¥ÍÑ½É¥…°]!<€Õ€™Õ¹Ñ¥½¹…°ÁÉ½Ñ½½°¸Q¡•ä…É”¹½ÐÑ¡”Í…µ”ÍÕ‰ÍåÍÑ•´…ÌÑ¡”5å!=5}MÕ¥Ñ”•Ù¥”½=‰©•Ð½¹™¥ÕÉ…Ñ¥½¸ÁÉ½Ñ½½°‘½Õµ•¹Ñ•Õ¹‘•ÈmAÉ½É…µµ¥¹t ¸¸¼¸¸½ÁÉ½É…µµ¥¹œ¼¤¸((ŒŒŒ]É¥Ñ”ÍÕÁÁ½ÉÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÐéÌÀÀÀÀÀÙ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()M½µ”ÁÕ‰±¥Í¡•]!Q€Ù…±Õ•Ì‘•ÍÉ¥‰”ÍåÍÑ•´ÍÑ…Ñ•ÌÉ…Ñ¡•ÈÑ¡…¸½µµ…¹‘Ì¸Q¡•¥ÈÁÉ•Í•¹”¥¸Ñ¡”Ù½…‰Õ±…ÉäµÕÍÐ¹½Ð‰”¥¹Ñ•ÉÁÉ•Ñ•…ÌÁ•Éµ¥ÍÍ¥½¸Ñ¼ÑÉ…¹Íµ¥ÐÑ¡•´…Ì½¹ÑÉ½°½Á•É…Ñ¥½¹Ì¸]¡•É”Ñ¡”½ÉÁÕÌ½¹±ä•ÍÑ…‰±¥Í¡•Ì„Ù…±Õ”¥¸É•ÍÁ½¹Í•Ì½•Ù•¹ÑÌ°Ñ¡¥ÌÉ•™•É•¹”ÑÉ•…ÑÌ¥Ð…ÌÉ•Á½ÉÐµ½¹±ä¸()M•”m]!Q€I•™•É•¹•t¡Ý¡…Ð¹µ¤™½ÈÙ…±Õ•Ì…¹m‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤™½ÈÑ…É•ÐÍå¹Ñ…à¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜÔ()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´Ôµ…±…É´½Ý¡…Ð¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èÕ€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒ]!Q€I•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÔéÌÀÀÀÀÀÅ€()ð]!Q€ð5•…¹¥¹œðQåÁ¥…°É½±”ð)ð€´´´ð€´´´ð€´´´ð)ð€Á€ð5…¥¹Ñ•¹…¹”ð•¹ÑÉ…°µÕ¹¥ÐÍÑ…Ñ”ð)ð€Å€ðÑ¥Ù…Ñ¥½¸ð•¹ÑÉ…°µÕ¹¥ÐÍÑ…Ñ”ð)ð€É€ð¥Í…Ñ¥Ù…Ñ¥½¸ðMÑ…Ñ”½•Ù•¹Ðð)ð€Í€ð•±…ä•¹ðÙ•¹Ðð)ð€Ñ€ðMåÍÑ•´‰…ÑÑ•Éä™…Õ±Ðð…Õ±ÐÍÑ…Ñ”½•Ù•¹Ðð)ð€Õ€ð	…ÑÑ•Éä=,ðMÑ…Ñ”½•Ù•¹Ðð)ð€Ù€ð9¼¹•ÑÝ½É¬ð5…¥¹Ì½¹•ÑÝ½É¬™…Õ±ÐÍÑ…Ñ”ð)ð€Ý€ð9•ÑÝ½É¬ÁÉ•Í•¹Ðð5…¥¹Ì½¹•ÑÝ½É¬ÍÑ…Ñ”ð)ð€á€ð¹…”ðMåÍÑ•´ÍÑ…Ñ”½½¹ÑÉ½°½¹Ñ•áÐð)ð€å€ð¥Í•¹…”ðMåÍÑ•´ÍÑ…Ñ”½½¹ÑÉ½°½¹Ñ•áÐð)ð€ÄÁ€ð	…ÑÑ•ÉäÕ¹±½…‘Ìð	…ÑÑ•Éä™…Õ±ÐÍÑ…Ñ”ð)ð€ÄÅ€ðÑ¥Ù”é½¹”ði½¹”ÍÑ…Ñ”ð)ð€ÄÉ€ðQ•¡¹¥…°…±…É´ð±…É´•Ù•¹Ðð)ð€ÄÍ€ðI•Í•ÐÑ•¡¹¥…°…±…É´ð±…É´•Ù•¹Ð½ÍÑ…Ñ”ð)ð€ÄÑ€ð9¼É••ÁÑ¥½¸€¼-€Á•É¥Á¡•É…°‘•Ù¥”ðA•É¥Á¡•É…°ÍÑ…Ñ”ð)ð€ÄÕ€ð%¹ÑÉÕÍ¥½¸…±…É´ð±…É´•Ù•¹Ðð)ð€ÄÙ€ð€ÈÐµ¡½ÕÈ…±…É´€¼Ñ…µÁ•É¥¹œð±…É´•Ù•¹Ðð)ð€ÄÝ€ð¹Ñ¤µÁ…¹¥Œ…±…É´ð±…É´•Ù•¹Ðð)ð€Äá€ð9½¸µ…Ñ¥Ù”é½¹”ði½¹”ÍÑ…Ñ”ð)ð€ÈÙ€ðMÑ…ÉÐÁÉ½É…µµ¥¹œðAÉ½É…µµ¥¹œ½Á•É…Ñ¥½¸ð)ð€ÈÝ€ðMÑ½ÀÁÉ½É…µµ¥¹œðAÉ½É…µµ¥¹œ½Á•É…Ñ¥½¸ð)ð€ÌÅ€ðM¥±•¹Ð…±…É´ð±…É´•Ù•¹Ðð((ŒŒŒ%¹‘•Á•¹‘•¹ÐÍÑ…Ñ”…á•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÔéÌÀÀÀÀÀÉ€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()•¹ÑÉ…°µÕ¹¥ÐÍÑ…ÑÕÌÉ•ÍÁ½¹Í”…¸½¹Ñ…¥¸Í•Ù•É…°½˜Ñ¡•Í”Ù…±Õ•Ì¥¸½¹”É•ÍÁ½¹Í”ÑÉ…¹Í…Ñ¥½¸¸½È•á…µÁ±”°ÍåÍÑ•´…Ñ¥Ù…Ñ¥½¸°•¹…•µ•¹Ð°‰…ÑÑ•ÉäÍÑ…Ñ”…¹¹•ÑÝ½É¬ÍÑ…Ñ”…É”¥¹‘•Á•¹‘•¹ÐÁÉ½Á•ÉÑ¥•ÌÉ…Ñ¡•ÈÑ¡…¸µÕÑÕ…±±ä•á±ÕÍ¥Ù”µ•µ‰•ÉÌ½˜½¹”•¹Õµ•É…Ñ¥½¸¸()i½¹”ÍÑ…Ñ”¥ÌÉ•ÁÉ•Í•¹Ñ•Í•Á…É…Ñ•±äè]!P€ÄÅ€É•Á½ÉÑÌ…¸•¹…•½…Ñ¥Ù”é½¹”…¹]!P€Äá€„‘¥Ù¥‘•½¹½¸µ…Ñ¥Ù”é½¹”¸±…É´™É…µ•ÌÍÕ …Ì€ÄÕ€°€ÄÙ€°…¹€ÄÝ€Ñ¡•¸¥‘•¹Ñ¥™ä…±…É´½¹‘¥Ñ¥½¹Ì…ÍÍ½¥…Ñ•Ý¥Ñ Ñ¡”Ñ…É•ÐÍ•±•Ñ•‰ä]!I€¸()Q¡”±…‰•±Ì™½±±½ÜÑ¡”ÁÕ‰±¥Í¡•]!<€Õ€Ù½…‰Õ±…Éä¸9¼…‘‘¥Ñ¥½¹…°¹Õµ•É¥Œµ•…¹¥¹Ì…É”…ÍÍ¥¹•Ý¥Ñ¡½ÕÐ¥µÁ±•µ•¹Ñ…Ñ¥½¸½ÈÝ¥É”•Ù¥‘•¹”¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜØ()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´Øµ‰…Í¥ŒµÙ¥‘•¼µ‘½½Èµ•¹ÑÉä½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èÙ€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒ]!<€Ù€€´	…Í¥ŒY¥‘•¼½½È¹ÑÉä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜØéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()]!<€Ù€¥‘•¹Ñ¥™¥•ÌÑ¡”	…Í¥ŒY¥‘•¼½½È¹ÑÉäÍåÍÑ•´¥¸Ñ¡”­¹½Ý¸=Á•¹]•‰9•Ð¹…µ•ÍÁ…”…Ñ…±½Õ”¸((ŒŒŒ½ÉÁÕÌÍÑ…ÑÕÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜØéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÙ•ÉÍ¥½¹€)…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡”½ÉÁÕÌ¥¹±Õ‘•ÌÑ¡”m0ÐØàÙM,MÁ•¥™¥…Ñ¥½¹t ¸¸¼¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½]!=|Ù}0ÐØàÙM,¹Á‘˜¤°Ù•ÉÍ¥½¸€Ä¸À¸À‘…Ñ•€ÄÄ•‰ÉÕ…Éä€ÈÀÀä¸%ÑÌ•¥¡ÐÁ…•Ì½¹Ñ…¥¸]!<€Ù€½µµ…¹½…‘‘É•ÍÌÑ…‰±•Ì…¹Í•¹½É••¥Ù”™±½ÝÌ™½È…µ•É…Ì°…±±Ì°±½­Ì°…¹ÍÑ…¥È±¥¡Ñ¥¹œ¸Q¡¥Ì¥ÌÁÉ½‘ÕÐµÍÁ•¥™¥ŒÁÕ‰±¥Í¡••Ù¥‘•¹”°¹½Ðµ•É•±ä„¹…µ•ÍÁ…”É•½É…¹¹½Ð„½µÁ±•Ñ”•¹•É¥ŒY¥‘•¼½½È¹ÑÉäÍÁ•¥™¥…Ñ¥½¸¸()Q¡”É•™•É•¹”‰•±½ÜÁÉ•Í•ÉÙ•ÌÑ¡”Í½ÕÉ”ÌÁÉ½‘ÕÐÍ½Á”¸Y…±Õ•Ì™É½´…‘©…•¹ÐY¥‘•¼½½È¹ÑÉäÍåÍÑ•µÌµÕÍÐ¹½Ð‰”ÍÕ‰ÍÑ¥ÑÕÑ•™½ÈÑ¡”0ÐØàÙM,•Ù¥‘•¹”¸((ŒŒŒ0ÐØàÙM,É•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜØéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€)…ÕÑ¥½¹Ìè¹½Ð•Ù¥‘•¹•€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()Q¡”½µµ…¹Ñ…‰±”…¹Í•Ñ¥½¹Ì€Ä…¹€È•ÍÑ…‰±¥Í Ñ¡•Í”™½ÉµÌ¸A±…•¡½±‘•ÉÌ…É”Íåµ‰½±¥Œ°¹½Ð…ÁÑÕÉ•Ì¸()ð=Á•É…Ñ¥½¸ðAÕ‰±¥Í¡•™½É´ðÁÁ±¥…‰¥±¥Ñäð)ð€´´´ð€´´´ð€´´´ð)ð…µ•É„=8ð€¨Ø¨À©]!IŒ€ð]!I€ô€ÐÀÀÀ¸¸ÐÀäÕ€ìÉ¥Í•È™½É´…ÁÁ•¹‘Ì€ŒÉ€Ñ¼]!I€ð)ð…µ•É„=ð€¨Ø¨äŒ€ð9¼]!I€™¥•±¥¸Ñ¡”ÁÕ‰±¥Í¡•™½É´ð)ðMÑ…¥È±¥¡Ð=€¼=8ð€¨Ø¨ÄÄ©]!IŒ€€¼€¨Ø¨ÄÈ©]!IŒ€ð0ÐØàÙM,…‘‘É•ÍÌð)ð=Á•¸±½¬ð€¨Ø¨ÄÀ©]!IŒ€ð]!I€ô€ÐÀÀÀ¸¸ÐÀäÕ€ìÉ¥Í•È™½É´…ÁÁ•¹‘Ì€ŒÉ€ð)ð…µ•É„å±¥¹œð€¨Ø¨Äà©]!IŒ€ð]!I€ô€ÐÀÀÀ¸¸ÐÀäÕ€ìÍ½ÕÉ”É•ÅÕ¥É•Ì„ÁÉ••‘¥¹œ…µ•É„=8ìÉ¥Í•È™½É´…ÁÁ•¹‘Ì€ŒÉ€ð)ð%¹½µ¥¹œ…Á…ÉÑµ•¹Ð…±°ð€¨Ø¨Ø©]!IŒ€ðI••¥Ù”Í•Ñ¥½¸è]!I€ô€À¸¸Ìääå€ð)ð%¹½µ¥¹œ‰É½…‘…ÍÐ…±°ð€¨Ø¨Ø¨ÐÄÀÀŒ€ðI••¥Ù”Í•Ñ¥½¸ìÍÁ•¥…°Ù…±Õ”½ÕÑÍ¥‘”Ñ¡”•¹‘Á½¥¹ÐÉ…¹”ð)ð=Á•¸±½¬Ý¥Ñ •áÑ•É¹…°Õ¹¥Ð¥¸½¹Ù•ÉÍ…Ñ¥½¸ð€¨Ø¨ÈÈ©]!IŒ€ðI••¥Ù”Í•Ñ¥½¸è]!I€ô€ÐÀÀÀ¸¸ÐÀäÕ€ì¹½Ð•Ù¥‘•¹”½˜„Í•¹½Á•É…Ñ¥½¸ð()½ÈÍ•¹‘¥¹œ°Ñ¡”Í½ÕÉ”‘•ÍÉ¥‰•Ì,…Ì½¹™¥Éµ…Ñ¥½¸Ñ¡…Ð„™É…µ”Ý…ÌÍ•¹Ð½¸Ñ¡”ML‰ÕÌ°9,…Ì¹½ÐÍ•¹Ð°…¹€¨Œ©àŒ€…Ì…¸•ÉÉ½ÈµÑåÁ”™½É´¸%Ð‘½•Ì¹½Ð•¹Õµ•É…Ñ”Ñ¡”á€½‘•Ì½È•ÍÑ…‰±¥Í Ñ¡”™¥¹…°Á¡åÍ¥…°•™™•Ð¸Q¡•Í”…É”ÁÉ½‘ÕÐµÍÁ•¥™¥Œ…­¹½Ý±•‘•µ•¹ÐÍ•µ…¹Ñ¥Ì¸((ŒŒŒM½ÕÉ”±¥µ¥ÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜØéÌÀÀÀÀÀÑ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€°µÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()Q¡”…‘‘É•ÍÌÑ…‰±”±…‰•±Ì€ÐÀÀÅ€…Ì•¹‘Á½¥¹Ð€È•Ù•¸Ñ¡½Õ Ñ¡”…‘©…•¹Ð•¹ÑÉ¥•ÌÍÕ•ÍÐ„‘¥™™•É•¹Ð…É¥Ñ¡µ•Ñ¥Œ½ÉÉ•ÍÁ½¹‘•¹”¸AÉ•Í•ÉÙ”€ÐÀÀÀ¸¸ÐÀäÕ€…ÌÑ¡”ÍÑ…Ñ•Ý¥É”É…¹”ì‘¼¹½Ð¥¹™•È…¸•¹‘Á½¥¹Ðµ¹Õµ‰•È½¹Ù•ÉÍ¥½¸™É½´Ñ¡¥Ì¥¹½¹Í¥ÍÑ•¹Ð±…‰•°¸()M•Ù•É…°É•ÍÁ½¹Í”½É••¥Ù”É½ÝÌÁÉ¥¹Ð…ÉÉ½ÝÌ¥¹½¹Í¥ÍÑ•¹ÐÝ¥Ñ Ñ¡•¥ÈÍ•Ñ¥½¸¡•…‘¥¹Ì…¹‘•ÍÉ¥ÁÑ¥½¹Ì¸Q¡”Ñ…‰±”…‰½Ù”É•Á½ÉÑÌÑ¡”Í•¹‘¥¹œ½É••¥Ù¥¹œÍ•Ñ¥½¸É½±•Ì°¹½Ð„É•Á…¥É•½‰Í•ÉÙ•ÑÉ…¹ÍÉ¥ÁÐ¸á…Ð‘¥É•Ñ¥½¸…¹•ÉÉ½Èµ½‘”‰•¡…Ù¥½ÈÉ•ÅÕ¥É”ÁÉ½‘ÕÐ•Ù¥‘•¹”¸…µ•É„=ÌÍ¡½ÉÐ™½É´…¹‰É½…‘…ÍÐµ…±°Í•¹Ñ¥¹•°µÕÍÐ¹½Ð‰”¹½Éµ…±¥é•¥¹Ñ¼Ñ¡”½É‘¥¹…ÉäÑ¡É•”µ™¥•±½µµ…¹É…µµ…È¸((ŒŒŒAÉ½Ñ½½°‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜØéÌÀÀÀÀÀÕ€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()]!<€Ù€°m]!<€Ýt ¸¸½Ý¡¼´ÜµµÕ±Ñ¥µ•‘¥„µÙ¥‘•¼¼¤°…¹m]!<€át ¸¸½Ý¡¼´àµÙ¥‘•¼µ‘½½Èµ•¹ÑÉäµÑ•±•Á¡½¹ä¼¤…É”É•±…Ñ•‰ä…ÁÁ±¥…Ñ¥½¸‘½µ…¥¸‰ÕÐ…É”¥¹‘•Á•¹‘•¹ÐÁÉ½Ñ½½°¹…µ•ÍÁ…•Ì¸…µ•É„½Ù¥‘•¼½Á•É…Ñ¥½¸‘½Õµ•¹Ñ•™½È]!<€Ý€°™½È•á…µÁ±”°¥Ì¹½Ð…ÕÑ½µ…Ñ¥…±±äÙ…±¥Õ¹‘•È]!<€Ù€¸()ÕÑÕÉ”Ù…±Õ•ÌÍ¡½Õ±‰”…‘‘•½¹±äÝ¡•¸ÍÕÁÁ½ÉÑ•‰äÑ¡”5å!=5}MÕ¥Ñ”¥µÁ±•µ•¹Ñ…Ñ¥½¸½ÉÁÕÌ°„…¹½¹¥…°ÍÁ•¥™¥…Ñ¥½¸°½È½‰Í•ÉÙ•Ý¥É”‰•¡…Ù¥½È¸½µµ½¸™É…µ”Íå¹Ñ…àÉ•µ…¥¹Ì‘•™¥¹•Õ¹‘•ÈmAÉ½Ñ½½±t ¸¸¼¸¸½ÁÉ½Ñ½½°¼¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜÜ()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´ÜµµÕ±Ñ¥µ•‘¥„µÙ¥‘•¼½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èÝ€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒ]!<€Ý€€´5Õ±Ñ¥µ•‘¥„MåÍÑ•´()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÜéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()]!<€Ý€½¹ÑÉ½±Ì…µ•É…Ì™É½´Ñ¡”Y¥‘•¼½½È¹ÑÉä…Ñ…±½Õ”èÙ¥‘•¼µÉ•Í½ÕÉ”…ÅÕ¥Í¥Ñ¥½¸½É•±•…Í”°¥µ…”…‘©ÕÍÑµ•¹Ð°…¹‘¥ÍÁ±…ä%0Í•±•Ñ¥½¸¸((ŒŒŒ]!Q€Ù…±Õ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÜéÌÀÀÀÀÀÉ€()ð]!Q€ðÕ¹Ñ¥½¸ð)ð€´´´ð€´´´ð)ð€Á€ðI••¥Ù”Ù¥‘•¼ð)ð€å€ðI•±•…Í”…Õ‘¥¼½Ù¥‘•¼É•Í½ÕÉ•Ìð)ð€ÄÈÁ€€¼€ÄÈÅ€ði½½´¥¸€¼½ÕÐð)ð€ÄÌÁ€€¼€ÄÌÅ€ð%¹É•…Í”€¼‘•É•…Í”é½½´µ•¹ÑÉ”`½½É‘¥¹…Ñ”ð)ð€ÄÐÁ€€¼€ÄÐÅ€ð%¹É•…Í”€¼‘•É•…Í”é½½´µ•¹ÑÉ”d½½É‘¥¹…Ñ”ð)ð€ÄÔÁ€€¼€ÄÔÅ€ð%¹É•…Í”€¼‘•É•…Í”±Õµ¥¹½Í¥Ñäð)ð€ÄØÁ€€¼€ÄØÅ€ð%¹É•…Í”€¼‘•É•…Í”½¹ÑÉ…ÍÐð)ð€ÄÜÁ€€¼€ÄÜÅ€ð%¹É•…Í”€¼‘•É•…Í”½±½ÕÈð)ð€ÄàÁ€€¼€ÄàÅ€ð%¹É•…Í”€¼‘•É•…Í”¥µ…”ÅÕ…±¥Ñäð)ð€ÍI€°Ý¥Ñ I€…¹€•… €Ä¸¸Ñ€ðM•±•Ð%0É½ÜI€°Á½Í¥Ñ¥½¸€ð()Q¡”…‘©ÕÍÑµ•¹Ð½Á•É…Ñ¥½¹Ì…É”É•±…Ñ¥Ù”¸Q¡”€ÍI€™…µ¥±ä¥ÌÍÑÉÕÑÕÉ…°èI€Í•±•ÑÌ%0É½Ü…¹€Í•±•ÑÌÁ½Í¥Ñ¥½¸°‰½Ñ €Ä¸¸Ñ€¸((ŒŒŒ…µ•É„…‘‘É•ÍÍ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÜéÌÀÀÀÀÀÍ€()AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€°Í½ÕÉ•€()Q¡”ÁÕ‰±¥Í¡•]!I€Ñ…‰±”±¥ÍÑÌ…µ•É…Ì€ÐÀÀÀ¸¸ÐÀäå€°Ý¥Ñ Ñ¡”™¥¹…°ÑÝ¼‘¥¥ÑÌ¥‘•¹Ñ¥™å¥¹œ…µ•É„€ÀÀ¸¸äå€¸()%¹‘¥Ù¥‘Õ…°½µµ…¹µ™±½ÜÑ…‰±•ÌÍÑ…Ñ”]!IõlÐÀÀÀ´ÔÀÀÁu€°Ý¡¥ ½¹™±¥ÑÌÝ¥Ñ Ñ¡”•áÁ±¥¥Ð…‘‘É•ÍÌÑ…‰±”¸Q¡¥Ì‘½Õµ•¹Ñ…Ñ¥½¸ÑÉ•…ÑÌ€ÐÀÀÀ¸¸ÐÀäå€…ÌÑ¡”•ÍÑ…‰±¥Í¡••¹Õµ•É…Ñ•É…¹”…¹É•½É‘ÌÑ¡”‰É½…‘•È½µµ…¹µ¹½Ñ”É…¹”…Ì„Í½ÕÉ”¥¹½¹Í¥ÍÑ•¹ä°¹½Ð…ÌÁÉ½½˜Ñ¡…Ð•Ù•ÉäÙ…±Õ”Ñ¡É½Õ €ÔÀÀÁ€¥Ì„…µ•É„¸((ŒŒŒÉ…µ”Í¡…Á”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÜéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”‘•‘¥…Ñ•ÍÁ•¥™¥…Ñ¥½¸ÁÉ¥¹ÑÌ½µµ…¹½•Ù•¹Ð™É…µ•ÌÝ¥Ñ „ÑÉ…¥±¥¹œ•µÁÑäÑ…œè()Ñ•áÐ(¨Ü©]!P©]!I¨ŒŒ)€()%Ð…±Í¼ÁÉ¥¹ÑÌÉ•Í½ÕÉ”É•±•…Í”…Ì€¨Ü¨ä¨¨Œ€°Ý¥Ñ ¹¼…µ•É„…‘‘É•ÍÌ¸¸¥µÁ±•µ•¹Ñ…Ñ¥½¸Ñ…É•Ñ¥¹œÑ¡¥Ì‘¥…±•ÐÍ¡½Õ±ÁÉ•Í•ÉÙ”Ñ¡”•µÁÑä™¥•±É…Ñ¡•ÈÑ¡…¸¹½Éµ…±¥é¥¹œ‰±¥¹‘±äÑ¼Ñ¡”½µµ½¸Ñ¡É•”µÑ…œ™½É´¸()Q¡”…Ñ•Ý…ä…¹ÍÝ•ÉÌ½µµ…¹‘ÌÝ¥Ñ -€½È9-€¸‘©ÕÍÑµ•¹Ð…¹%0½Á•É…Ñ¥½¹Ì…É”µ•…¹¥¹™Õ°½¹±ä¥¸Ñ¡”½¹Ñ•áÐ½˜…¸…ÅÕ¥É•½…Ñ¥Ù”Ù¥‘•¼É•Í½ÕÉ”¸((ŒŒŒI•Í½ÕÉ”±¥™•å±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÜéÌÀÀÀÀÀÕ€((Ä¸I•ÅÕ•ÍÐÙ¥‘•¼Ý¥Ñ ]!P€Á€™½ÈÑ¡”Í•±•Ñ•…µ•É„¸(È¸ÁÁ±äé½½´°Á½Í¥Ñ¥½¸°¥µ…”°½È%0½Á•É…Ñ¥½¹Ì…ÌÍÕÁÁ½ÉÑ•¸(Ì¸I•±•…Í”…Õ‘¥¼½Ù¥‘•¼É•Í½ÕÉ•ÌÝ¥Ñ ]!P€å€¸()]!P€å€¥ÌÉ•Í½ÕÉ”µ…¹…•µ•¹Ð°¹½Ð„…µ•É„=ÍÑ…Ñ”¸((ŒŒŒ9…µ•ÍÁ…”‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÜéÌÀÀÀÀÀÙ€()]!<€Ý€É•µ…¥¹Ì‘¥ÍÑ¥¹Ð™É½´	…Í¥ŒY¥‘•¼½½È¹ÑÉäm]!<€Ùt ¸¸½Ý¡¼´Øµ‰…Í¥ŒµÙ¥‘•¼µ‘½½Èµ•¹ÑÉä¼¤°Y¥‘•¼½½È¹ÑÉä½Q•±•Á¡½¹äm]!<€át ¸¸½Ý¡¼´àµÙ¥‘•¼µ‘½½Èµ•¹ÑÉäµÑ•±•Á¡½¹ä¼¤°…¹Í½Õ¹m]!<€ÄÙt ¸¸½Ý¡¼´ÄØµÍ½Õ¹µÍåÍÑ•´¼¤€¼m]!<€ÈÉt ¸¸½Ý¡¼´ÈÈµÍ½Õ¹µ‘¥™™ÕÍ¥½¸¼¤¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜÜéÌÀÀÀÀÀÝ€()AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()Y…±Õ•Ì°…‘‘É•ÍÍ•Ì°ÑÉ…¥±¥¹œµ•µÁÑäµÑ…œ™É…µ•Ì°…¹½µµ…¹Í•ÅÕ•¹•Ì½µ”™É½´m]!<€Ý€ÍÁ•¥™¥…Ñ¥½¹t ¸¸¼¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½]!=|Ü¹Á‘˜¤¸Q¡”Í½ÕÉ”Ì…‘‘É•ÍÌµÉ…¹”‘¥ÍÉ•Á…¹ä¥ÌÉ•Ñ…¥¹••áÁ±¥¥Ñ±ä¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜà()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´àµÙ¥‘•¼µ‘½½Èµ•¹ÑÉäµÑ•±•Á¡½¹ä½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èá€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒ]!<€á€€´Y¥‘•¼½½È¹ÑÉä…¹Q•±•Á¡½¹ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜàéÌÀÀÀÀÀÅ€()]!<€á€¥‘•¹Ñ¥™¥•ÌÑ¡”=Á•¹]•‰9•ÐY¥‘•¼½½È¹ÑÉä…¹Ñ•±•Á¡½¹äÍåÍÑ•´¸Q¡”ÕÉÉ•¹Ð½ÉÁÕÌ•ÍÑ…‰±¥Í¡•ÌÑ¡”¹…µ•ÍÁ…”…¹„¹…ÉÉ½Ü5å!=5MÕ¥Ñ”Í•ÉÙ¥”½Á•É…Ñ¥½¸°‰ÕÐ¹½Ð„½µÁ±•Ñ”ÁÕ‰±¥Œ™Õ¹Ñ¥½¹…°É…µµ…È¸((ŒŒŒÍÑ…‰±¥Í¡•¥µÁ±•µ•¹Ñ…Ñ¥½¸•Ù¥‘•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜàéÌÀÀÀÀÀÉ€()AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()=A8¹‘‰€É•½É‘Ìè((´™Õ¹Ñ¥½¹…°]!<€á€ì(´‘¥…¹½ÍÑ¥Œ™…µ¥±ä]!<€ÄÀÀá€ì(´µ…¹…•€ô€Å€ì(´Ñ¡”ÐÈÈÁÕ‰±¥ŒµÉ¥Í•Èµ¥¹Ñ•É™…”…‘‘É•ÍÌÉÕ±”€Åm$Åum$Éum$Íum$Ñu€°Ý¥Ñ …‘Ù…¹•™½É´€Åm$Å$É$Í$Ñu€ì(´½¹”ÍåÍÑ•´µ…ÍÍ½¥…Ñ••¹•É¥Œ¥‘•¹Ñ¥™¥…Ñ¥½¸Ñ•µÁ±…Ñ”°€©m]!=t©m]!QtŒ€°±…‰•±±•µ‘}¥‘•¹Ñ€¸()Q¡”Ñ•µÁ±…Ñ”•ÍÑ…‰±¥Í¡•ÌÑ¡…Ð5å!=5MÕ¥Ñ”…ÍÍ½¥…Ñ•Ì„Í•ÉÙ¥”µ¥‘•¹Ñ¥™¥…Ñ¥½¸½Á•É…Ñ¥½¸Ý¥Ñ Ñ¡¥ÌÍåÍÑ•´¸	•…ÕÍ”Ñ¡”‘…Ñ…‰…Í”‘½•Ì¹½Ð•¹Õµ•É…Ñ”Ñ¡”ÍÕ‰ÍÑ¥ÑÕÑ•]!Q€Í•µ…¹Ñ¥Ì¡•É”°¥Ð‘½•Ì¹½Ð©ÕÍÑ¥™ä„]!Q€Ñ…‰±”¸((ŒŒŒÙ¥‘•¹”‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜàéÌÀÀÀÀÀÍ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡”ÁÕ‰±¥Œ½ÉÁÕÌ¡…Ì¹¼‘•‘¥…Ñ•]!<€á€ÍÁ•¥™¥…Ñ¥½¸¸]!<€Ù€°]!<€Ý€°…¹]!<€á€Í¡…É”…¸…ÁÁ±¥…Ñ¥½¸‘½µ…¥¸‰ÕÐÉ•µ…¥¸¥¹‘•Á•¹‘•¹Ð¹…µ•ÍÁ…•Ì¸¼¹½ÐÉ•ÕÍ”]!<€Ý€…µ•É„½µµ…¹‘Ì½È…‘‘É•ÍÍ•ÌÕ¹‘•È]!<€á€Ý¥Ñ¡½ÕÐ‘¥É•Ð•Ù¥‘•¹”¸()¥…¹½ÍÑ¥ŒÑÉ…™™¥Œ‰•±½¹ÌÑ¼]!<€ÄÀÀá€ìÑ¡”¹Õµ•É¥ŒÉ•±…Ñ¥½¹Í¡¥À‘½•Ì¹½Ðµ…­”™Õ¹Ñ¥½¹…°…¹‘¥…¹½ÍÑ¥Œ™É…µ•Ì¥¹Ñ•É¡…¹•…‰±”¸((ŒŒŒ•½‘•ÈÕ¥‘…¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜàéÌÀÀÀÀÀÑ€()U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°ÍÁ•¥™¥…Ñ¥½¹€()I•½¹¥é”Ñ¡”¹…µ•ÍÁ…”°ÁÉ•Í•ÉÙ”Õ¹­¹½Ý¸™¥•±‘Ì±½ÍÍ±•ÍÍ±ä°…¹±…‰•°½¹±äÑ¡”…‘‘É•ÍÌ™½É´…¹•¹•É¥Œ¥‘•¹Ñ¥™¥…Ñ¥½¸½Á•É…Ñ¥½¸•ÍÑ…‰±¥Í¡•…‰½Ù”¸•Ù¥”µÍÁ•¥™¥ŒY¥‘•¼½½È¹ÑÉä‰•¡…Ù¥½ÈÉ•ÅÕ¥É•Ì„…¹½¹¥…°ÍÁ•¥™¥…Ñ¥½¸°„‘…Ñ…‰…Í”Ñ•µÁ±…Ñ”Ý¥Ñ É•Í½±Ù•Á…É…µ•Ñ•ÉÌ°½È½‰Í•ÉÙ•ÑÉ…™™¥Œ¸()M•”m5å!=5MÕ¥Ñ”=A8¹‘‰€½Ù•É…•t ¸¸½½Á•¸µ‘ˆµ½Ù•É…”¹µ¤°m]!<€Ùt ¸¸½Ý¡¼´Øµ‰…Í¥ŒµÙ¥‘•¼µ‘½½Èµ•¹ÑÉä¼¤°…¹m]!<€Ýt ¸¸½Ý¡¼´ÜµµÕ±Ñ¥µ•‘¥„µÙ¥‘•¼¼¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀÜä()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´äµ…Õá¥±¥…É¥•Ì½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èå€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒ]!<€å€€´Õá¥±¥…É¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜäéÌÀÀÀÀÀÅ€()]!<€å€‘•™¥¹•ÌÑ¡”=Á•¹]•‰9•ÐÕá¥±¥…É¥•ÌÍåÍÑ•´¸Õá¥±¥…Éä¡…¹¹•±ÌÁÉ½Ù¥‘”•¹•É…°µÁÕÉÁ½Í”‰¥¹…Éä½•Ù•¹Ð™Õ¹Ñ¥½¹ÌÑ¡…Ð…¸…±Í¼…ÁÁ•…È…ÌÉ•™•É•¹•Ì™É½´½Ñ¡•ÈÍåÍÑ•µÌ°¥¹±Õ‘¥¹œÑ¡”ÁÕ‰±¥Í¡•]!<€Õ€±…É´…‘‘É•ÍÍ¥¹œµ½‘•°¸((ŒŒŒ9…µ•ÍÁ…”Í•µ…¹Ñ¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜäéÌÀÀÀÀÀÉ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()]!Q€°]!I€°…¹…¹äÍÑÉÕÑÕÉ•Ù…±Õ•Ì…É”Í½Á•Ñ¼]!<€å€¸¸…Õá¥±¥…Éä¹Õµ‰•È¥Ì¹½Ð…¸ÕÑ½µ…Ñ¥½¸€½A1€…‘‘É•ÍÌ…¹Í¡½Õ±¹½Ð‰”¹½Éµ…±¥é•…Ì½¹”¸()Q¡”±…É´ÍÁ•¥™¥…Ñ¥½¸ÌÉ•™•É•¹•ÌÑ¼U`Ñ…É•ÑÌ‘•µ½¹ÍÑÉ…Ñ”É½ÍÌµÍåÍÑ•´ÕÍ”½˜…Õá¥±¥…Éä¡…¹¹•±Ì°‰ÕÐ‘¼¹½Ðµ…­”]!<€å€Á…ÉÐ½˜Ñ¡”±…É´¹…µ•ÍÁ…”¸%¹Ñ•É…Ñ¥½¹ÌÍ¡½Õ±ÁÉ•Í•ÉÙ”Ñ¡”½É¥¥¹…Ñ¥¹œ]!=€Ý¡•¸½ÉÉ•±…Ñ¥¹œÍÕ •Ù•¹ÑÌ¸((ŒŒŒ½ÉÁÕÌÍÑ…ÑÕÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀÜäéÌÀÀÀÀÀÍ€()U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()Q¡”ÕÉÉ•¹Ð¥¹Ñ•É…Ñ•½ÉÁÕÌ•ÍÑ…‰±¥Í¡•ÌÑ¡”Õá¥±¥…É¥•Ì¹…µ•ÍÁ…”…¹¥ÑÌÕÍ”‰ä5å!=5}MÕ¥Ñ”°‰ÕÐ‘½•Ì¹½Ð©ÕÍÑ¥™ä„½µÁ±•Ñ”¥¹‘•Á•¹‘•¹Ð]!Q€½%59M%=9€Ñ…‰±”‰•å½¹ÍÕÁÁ½ÉÑ•¥µÁ±•µ•¹Ñ…Ñ¥½¸•Ù¥‘•¹”¸U¹­¹½Ý¸Ù…±Õ•ÌÉ•µ…¥¸Õ¹ÍÁ•¥™¥•É…Ñ¡•ÈÑ¡…¸¥¹™•ÉÉ•™É½´•¹•É¥Œ‰¥¹…Éäµ½¹ÑÉ½°‰•¡…Ù¥½È¸()M•”mAÉ½Ñ½½±t ¸¸¼¸¸½ÁÉ½Ñ½½°¼¤™½È½µµ½¸™É…µ”Íå¹Ñ…à…¹m]!<€Õ€€´±…Éµt ¸¸½Ý¡¼´Ôµ…±…É´¼¤™½È±…É´µÍ¥‘”U`É•™•É•¹•Ì¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàÀ()M½ÕÉ”Á…Ñ è™Õ¹Ñ¥½¹…°½Ý¡¼´ääµÍ•ÉÙ¥”µ¥‘•¹Ñ¥™¥…Ñ¥½¸½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÝ¡¼èäå€)É•„è™Õ¹Ñ¥½¹…±€((ŒŒ]!<€äå€€´M•ÍÍ¥½¸…¹M•ÉÙ¥”%‘•¹Ñ¥™¥…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÀéÌÀÀÀÀÀÅ€()U¹•ÉÑ…¥¹Ñäè…ÁÁ•…ÉÍ€()€äå€…ÁÁ•…ÉÌ¥¸ÑÝ¼É•±…Ñ•‰ÕÐ‘¥™™•É•¹Ñ±ä•Ù¥‘•¹•É½±•Ìè((Ä¸Ñ¡”ÁÕ‰±¥Œ½¹¹•Ñ¥½¸Ý½É­™±½ÜÕÍ•Ì€¨ää©`Œ€Ñ¼Í•±•Ð…¸=Á•¹]•‰9•ÐÍ•ÍÍ¥½¸ì(È¸5å!=5MÕ¥Ñ”=A8¹‘‰€¹…µ•Ì™Õ¹Ñ¥½¹…°¹…µ•ÍÁ…”]!<€äå€€¨©M•ÉÙ¥”%‘•¹Ñ¥™¥…Ñ¥½¸¨¨¸()Q¡•Í”™…ÑÌµÕÍÐ‰”ÁÉ•Í•ÉÙ•Ý¥Ñ¡½ÕÐ¥¹Ù•¹Ñ¥¹œ„‰É½…‘•È™Õ¹Ñ¥½¹…°Ù½…‰Õ±…Éä¸((ŒŒŒAÕ‰±¥Í¡•Í•ÍÍ¥½¸Í•±•Ñ½ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÀéÌÀÀÀÀÀÉ€()ðÉ…µ”ðM•ÍÍ¥½¸ð)ð€´´´ð€´´´ð)ð€¨ää¨äŒ€ð½µµ…¹‘Ì½…Ñ¥½¹Ìð)ð€¨ää¨ÄŒ€ðÙ•¹ÑÌð)ð€¨ää¨ÀŒ€ðAÉ½É…µµ•Í•¹…É¥¼ð()Q¡•Í”™É…µ•Ì½ÕÈ‘ÕÉ¥¹œ½¹¹•Ñ¥½¸Í•ÑÕÀ…™Ñ•ÈÑ¡”Í•ÉÙ•ÈÉ••Ñ¥¹œ¸Q¡•ä½µ¥ÐÑ¡”¹½Éµ…°]!I€™¥•±…¹…É”Á…ÉÍ•‰äÑ¡”Í•ÍÍ¥½¸ÍÑ…Ñ”µ…¡¥¹”°¹½Ð‰ä…¸½É‘¥¹…ÉäÑ¡É•”µ™¥•±™Õ¹Ñ¥½¹…°‘¥ÍÁ…Ñ¡•È¸()M•”m½¹¹•Ñ¥½¸…¹M•ÍÍ¥½¹Ít ¸¸¼¸¸½ÁÉ½Ñ½½°½Í•ÍÍ¥½¹Ì¹µ¤™½ÈÑ¡”½µÁ±•Ñ”Ý½É­™±½Ü¸((ŒŒŒ=A8¹‘‰€¹…µ•ÍÁ…”•Ù¥‘•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÀéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°Í½ÕÉ•€()=A8¹‘ˆ¹9}MeMQ5€½¹Ñ…¥¹Ì„]!<€äå€É½Ü±…‰•±±•M•ÉÙ¥”%‘•¹Ñ¥™¥…Ñ¥½¸¸%Ð¡…Ì¹¼‘¥É•ÐM}=A9}MeMQ5€…ÍÍ½¥…Ñ¥½¸Ñ¼…¸9}=A9€½Á•É…Ñ¥½¸¥¸Ñ¡¥Ì‘…Ñ…‰…Í”É•Ù¥Í¥½¸¸()Q¡”‘…Ñ…‰…Í”Ñ¡•É•™½É”•ÍÑ…‰±¥Í¡•ÌÑ¡”¹…µ•ÍÁ…”±…‰•°°‰ÕÐ€¨©‘½•Ì¹½Ð¨¨•ÍÑ…‰±¥Í …¸…‘‘¥Ñ¥½¹…°Í•ÉÙ¥”µ¥‘•¹Ñ¥™¥…Ñ¥½¸]!Q€Ñ…‰±”½ÈÍ¡½ÜÑ¡…Ð•Ù•Éä€¨ää©`Œ€Ù…±Õ”¥ÌÙ…±¥¸Q¡”ÁÕ‰±¥Í¡•Í•±•Ñ½ÉÌ…‰½Ù”…É”Ñ¡”½¹É•Ñ”½Á•É…Ñ¥½¹ÌÍÕÁÁ½ÉÑ•‰äÑ¡”ÕÉÉ•¹ÐÍ½ÕÉ”½ÉÁÕÌ¸((ŒŒŒ¥ÍÑ¥¹Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÀéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()]!<€äå€Í•ÍÍ¥½¸Í•±•Ñ¥½¸¥Ì¹½Ðè((´…Ñ•Ý…ä…ÕÑ¡•¹Ñ¥…Ñ¥½¸€¡]!<€äá€‘•±…É…Ñ¥½¹Ì…¹¡…±±•¹”µÉ•ÍÁ½¹Í”¤ì(´„‘¥…¹½ÍÑ¥Œ•Ù¥”¥¹Ñ•ÉÙ¥•Üì(´…Ñ…±½Õ”¥‘•¹Ñ¥ÑäÉ•Í½±ÕÑ¥½¸ì(´™Õ¹Ñ¥½¹…°]!<€á€ÌÁ…É…µ•Ñ•É¥é•Í•ÉÙ¥”µ¥‘•¹Ñ¥™¥…Ñ¥½¸…ÍÍ½¥…Ñ¥½¸¥¸=A8¹‘‰€¸()%µÁ±•µ•¹Ñ…Ñ¥½¹ÌÍ¡½Õ±É•ÁÉ•Í•¹ÐÑ¡”É…Ü¹Õµ•É¥Œ¹…µ•ÍÁ…”Ý¡¥±”‘¥ÍÁ…Ñ¡¥¹œÑ¡”ÁÕ‰±¥Í¡•Í•±•Ñ½È™É…µ•Ì…½É‘¥¹œÑ¼½¹¹•Ñ¥½¸ÍÑ…Ñ”¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÀéÌÀÀÀÀÀÕ€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”Í•±•Ñ½È™É…µ•Ì…¹½É‘•È½µ”™É½´m=Á•¹]•‰9•Ð%¹ÑÉ½‘ÕÑ¥½¸ÍÁ•¥™¥…Ñ¥½¹t ¸¸¼¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=]9}%¹ÑÉ½}9¹Á‘˜¤¸Q¡”M•ÉÙ¥”%‘•¹Ñ¥™¥…Ñ¥½¸±…‰•°…¹…‰Í•¹”½˜…¸…ÍÍ½¥…Ñ•½¹É•Ñ”½Á•É…Ñ¥½¸½µ”™É½´=A8¹‘‰€ìÍ•”m5å!=5MÕ¥Ñ”=A8¹‘‰€½Ù•É…•t ¸¸½½Á•¸µ‘ˆµ½Ù•É…”¹µ¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàÄ()M½ÕÉ”Á…Ñ è¥¹Ñ•É¹…±Ì½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„è¥¹Ñ•É¹…±Í€((ŒŒ5å!=5MÕ¥Ñ”%¹Ñ•É¹…±Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÄéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()Q¡¥ÌÍ•Ñ¥½¸‘½Õµ•¹ÑÌÑ¡”5å!=5MÕ¥Ñ”€Ì¸Ô¸Ìà¥µÁ±•µ•¹Ñ…Ñ¥½¸‘…Ñ„Ñ¡…Ð½¹¹•ÑÌ…Ñ…±½Õ”…Á…‰¥±¥Ñä°=Á•¹]•‰9•Ðµ…¹…•µ•¹ÐÝ½É­™±½ÝÌ°Ù…±¥‘…Ñ¥½¸°…¹Í•¹…É¥¼µ•‘¥Ñ½È…Á…‰¥±¥Ñ¥•Ì¸()%Ð‘•ÍÉ¥‰•ÌÑ¡”¥µÁ±•µ•¹Ñ…Ñ¥½¸É•ÁÉ•Í•¹Ñ•‰äÑ¡”ÁÉ•Í•ÉÙ•‘…Ñ…‰…Í•Ì…¹ÍÕÁÁ½ÉÐ™¥±•Ì¸%Ð‘½•Ì¹½Ð±…¥´„½µÁ±•Ñ”Í½™ÑÝ…É”µ½µÁ½¹•¹Ð…É¡¥Ñ•ÑÕÉ”èÑ¡”…¹½¹¥…°½ÉÁÕÌ‘½•Ì¹½Ð¥¹±Õ‘”…ÁÁ±¥…Ñ¥½¸‰¥¹…É¥•Ì°‘•½µÁ¥±•½‘”°ÉÕ¹Ñ¥µ”ÑÉ…•Ì½˜‘…Ñ…‰…Í”…•ÍÌ°½ÈÑ¡”™½Éµ…ÐÕÍ•Ñ¼Á•ÉÍ¥ÍÐÕÍ•Èµ…ÕÑ¡½É•ÁÉ½©•ÑÌ…¹Í•¹…É¥½Ì¸((ŒŒŒI•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÄéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€°Í½ÕÉ•€()ðMÕ‰©•ÐðA…”ð)ð€´´´ð€´´´ð)ð%¹ÍÑ…±±•Í½ÕÉ”±½…Ñ¥½¹Ì°™¥¹•ÉÁÉ¥¹ÑÌ°…¹Ù•ÉÍ¥½¸Í½Á”ðm%¹ÍÑ…±±…Ñ¥½¸…¹M½ÕÉ”1…å½ÕÑt¡¥¹ÍÑ…±±…Ñ¥½¸µ…¹µÍ½ÕÉ”µ±…å½ÕÐ¹µ¤ð)ðI•ÍÁ½¹Í¥‰¥±¥Ñ¥•Ì…¹‰½Õ¹‘…É¥•Ì½˜•… ¥µÁ±•µ•¹Ñ…Ñ¥½¸ÍÑ½É”ðm…Ñ„MÑ½É”I•ÍÁ½¹Í¥‰¥±¥Ñ¥•Ít¡‘…Ñ„µÍÑ½É”µÉ•ÍÁ½¹Í¥‰¥±¥Ñ¥•Ì¹µ¤ð)ð!½ÜÍåÍÑ•µÌ°™É…µ•Ì°Í•ÅÕ•¹•Ì°…‘‘É•ÍÌÉÕ±•Ì°…¹Ñ¥µ•ÉÌ…É”É•ÁÉ•Í•¹Ñ•ðm=Á•¹]•‰9•ÐI•¥ÍÑÉä…¹MÑ…Ñ”5…¡¥¹•Ít¡½Á•¹Ý•‰¹•ÐµÉ•¥ÍÑÉäµ…¹µÍÑ…Ñ”µµ…¡¥¹•Ì¹µ¤ð)ð!½ÜÁÉ½‘ÕÐ¥‘•¹Ñ¥Ñä‰•½µ•Ì™¥ÉµÝ…É”°5½‘Õ±”°=‰©•Ð°…¹½¹™¥ÕÉ…Ñ¥½¸…Á…‰¥±¥Ñäðm…Ñ…±½Õ”I•Í½±ÕÑ¥½¹t¡…Ñ…±½Õ”µÉ•Í½±ÕÑ¥½¸¹µ¤ð)ð!½ÜÍ•¹…É¥¼µ•‘¥Ñ½È…Á…‰¥±¥Ñ¥•Ì…É”É•ÁÉ•Í•¹Ñ•…¹Ý¡•É”•á•ÕÑ¥½¸•Ù¥‘•¹”•¹‘ÌðmM•¹…É¥¼…Á…‰¥±¥Ñä1½…‘¥¹t¡Í•¹…É¥¼µ…Á…‰¥±¥Ñäµ±½…‘¥¹œ¹µ¤ð)ð!½Ü…Ñ…±½Õ”°ÁÉ½Ñ½½°°…¹±¥¹­•µÁÉ½Á•ÉÑä½¹ÍÑÉ…¥¹ÑÌ½µ‰¥¹”ðmY…±¥‘…Ñ¥½¸1…å•ÉÍt¡Ù…±¥‘…Ñ¥½¸µ±…å•ÉÌ¹µ¤ð)ðI•Í½ÕÉ”­•åÌ°ÍÑ½É•±…‰•±Ì°U$Ñ•Éµ¥¹½±½ä°…¹ÁÉ•Í•¹Ñ…Ñ¥½¸‰½Õ¹‘…É¥•Ìðm1½…±¥é…Ñ¥½¸…¹AÉ•Í•¹Ñ…Ñ¥½¹t¡±½…±¥é…Ñ¥½¸µ…¹µÁÉ•Í•¹Ñ…Ñ¥½¸¹µ¤ð)ðÍÑ…‰±¥Í¡•‰•¡…Ù¥½È°Í…™”¥¹™•É•¹•Ì°Õ¹­¹½Ý¹Ì°…¹¥¹Ù•ÍÑ¥…Ñ¥½¸ÁÉ¥½É¥Ñ¥•Ìðm%µÁ±•µ•¹Ñ…Ñ¥½¸	½Õ¹‘…É¥•Ít¡¥µÁ±•µ•¹Ñ…Ñ¥½¸µ‰½Õ¹‘…É¥•Ì¹µ¤ð((ŒŒŒ%µÁ±•µ•¹Ñ…Ñ¥½¸µ‘…Ñ„Á¥Á•±¥¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÄéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()5å!=5MÕ¥Ñ”½µ‰¥¹•ÌÍ•Ù•É…°µ½‘•±ÌÉ…Ñ¡•ÈÑ¡…¸É•±å¥¹œ½¸½¹”Õ¹¥Ù•ÉÍ…°‘…Ñ…‰…Í”è((Ä¸¥‘•¹Ñ¥™ä„A¡åÍ¥…°•Ù¥”…¹¥¹ÍÑ…±±•™¥ÉµÝ…É”™É½´‘¥…¹½ÍÑ¥ŒÑÉ…™™¥Œì(È¸É•Í½±Ù”ÁÉ½‘ÕÐ°5½‘Õ±”°=‰©•Ð°…¹½¹™¥ÕÉ…Ñ¥½¸…Á…‰¥±¥Ñä¥¸5!…Ñ…±½Õ”¹‘‰€ì(Ì¸Í•±•Ðµ…¹…•µ•¹Ð™É…µ•Ì°…‘‘É•ÍÌÉÕ±•Ì°Í•ÅÕ•¹•Ì°…¹Ñ¥µ•ÉÌ™É½´=A8¹‘‰€ì(Ð¸…ÁÁ±ä½¹Ñ•áÑÕ…°…Ñ…±½Õ”™¥±Ñ•ÉÌ…¹°Ý¡•É”…ÁÁ±¥…‰±”°±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì™É½´ÉÕ±•Ì¹‘ˆÍ€ì(Ô¸É•Í½±Ù”Í•¹…É¥¼µ•‘¥Ñ½È½µµ…¹‘Ì¥¹‘•Á•¹‘•¹Ñ±ä™É½´„M•¹…É¥½•Ù¥•Ì‘…Ñ…‰…Í”ì(Ø¸ÁÉ•Í•¹ÐÉ•Í½±Ù•±…‰•±Ì…¹•‘¥Ñ…‰±”™¥•±‘ÌÑ¡É½Õ Ñ¡”…ÁÁ±¥…Ñ¥½¸U$ì(Ü¸Í•¹™É…µ•Ì…¹½µÁ…É”Ñ¡”É•ÍÕ±Ñ¥¹œ¥¹ÍÑ…±±•ÍÑ…Ñ”Ý¥Ñ „¹•Ü‘¥…¹½ÍÑ¥ŒÉ•…µ‰…¬¸()… ÍÑ…”¡…Ì¥ÑÌ½Ý¸¥‘•¹Ñ¥™¥•ÉÌ¸ÅÕ…°¥¹Ñ••ÉÌ…É½ÍÌÍÑ½É•Ì…É”¹½Ð©½¥¹ÌÕ¹±•ÍÌ…¸•áÁ±¥¥ÐÉ•±…Ñ¥½¹Í¡¥À°…¸Õ¹…µ‰¥Õ½ÕÌ™É…µ”°½È¥¹‘•Á•¹‘•¹Ñ±ä½‰Í•ÉÙ•‰•¡…Ù¥½È•ÍÑ…‰±¥Í¡•ÌÑ¡”½ÉÉ•±…Ñ¥½¸¸((ŒŒŒQ¡É•”‘¥™™•É•¹Ð­¥¹‘Ì½˜ÍÑ…Ñ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÄéÌÀÀÀÀÀÑ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()ðMÑ…Ñ”ðAÉ¥¹¥Á…°•Ù¥‘•¹”ð5•…¹¥¹œð)ð€´´´ð€´´´ð€´´´ð)ð…Á…‰¥±¥Ñäð5!…Ñ…±½Õ”¹‘‰€°M•¹…É¥½•Ù¥•Ì°ÉÕ±•Ì¹‘ˆÍ€ðÝ¡…Ð…¸¥µÁ±•µ•¹Ñ…Ñ¥½¸…¸½™™•È¥¸„É•Í½±Ù•½¹Ñ•áÐð)ð]½É­™±½Üð=A8¹‘‰€…¹=Á•¹EÕ•Éä¹ÑáÑ€ðÝ¡¥ ™É…µ•Ì°ÑÉ…¹Í¥Ñ¥½¹Ì°‘¥É•Ñ¥½¹Ì°…¹Ñ¥µ•ÉÌ½µÁ½Í”…¸½Á•É…Ñ¥½¸ð)ð%¹ÍÑ…±±•ÍÑ…Ñ”ð‘¥…¹½ÍÑ¥ŒÉ•ÍÁ½¹Í•Ì…¹ÁÉ½©•Ð½U$½‰Í•ÉÙ…Ñ¥½¹ÌðÝ¡…Ð½¹”•Ù¥”ÕÉÉ•¹Ñ±äÉ•Á½ÉÑÌ½ÈÝ¡…Ð„ÁÉ½©•ÐÕÉÉ•¹Ñ±äÁÉ•Í•¹ÑÌð()½¹™ÕÍ¥¹œÑ¡•Í”±…å•ÉÌÁÉ½‘Õ•Ì½µµ½¸•ÉÉ½ÉÌ¸…Ñ…±½Õ”=‰©•Ð‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…Ð„5½‘Õ±”ÕÉÉ•¹Ñ±äÕÍ•Ì¥Ð¸¸=A8¹‘‰€Ñ•µÁ±…Ñ”‘½•Ì¹½ÐÁÉ½Ù”Õ¹¥Ù•ÉÍ…°•Ù¥”ÍÕÁÁ½ÉÐ¸Í•¹…É¥¼µ•‘¥Ñ½È…Ñ¥½¸‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…Ð•Ù•Éä¥¹ÍÑ…±±••Ù¥”…¸•á•ÕÑ”¥Ð¸((ŒŒŒM½ÕÉ”…ÕÑ¡½É¥Ñä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÄéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÙ•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°Í½ÕÉ•€()Q¡”…¹½¹¥…°™¥±•Ì…¹Ñ¡•¥ÈM!´ÈÔØ™¥¹•ÉÁÉ¥¹ÑÌ…É”É•¥ÍÑ•É•¥¸mÍ½ÕÉ•Ì½µ…¹¥™•ÍÐ¹å…µ±t ¸¸½Í½ÕÉ•Ì½µ…¹¥™•ÍÐ¹å…µ°¤¸…Ñ…‰…Í”™…ÑÌ¥¸Ñ¡¥ÌÍ•Ñ¥½¸‘•ÍÉ¥‰”Ñ¡…Ð•á…Ð5å!=5MÕ¥Ñ”€Ì¸Ô¸ÌàÍ½ÕÉ”Í•ÐìÑ¡•ä…É”¹½ÐÁÉ½Ñ½½°µ…á¥µ„½È±…¥µÌ…‰½ÕÐ±…Ñ•ÈÉ•±•…Í•Ì¸()Q¡”ÁÕ‰±¥Œ=Á•¹]•‰9•Ð‘½Õµ•¹ÑÌÉ•µ…¥¸…ÕÑ¡½É¥Ñ…Ñ¥Ù”™½ÈÁÕ‰±¥Í¡•™Õ¹Ñ¥½¹…°™É…µ”Í•µ…¹Ñ¥Ì¸5å!=5MÕ¥Ñ”¥µÁ±•µ•¹Ñ…Ñ¥½¸‘…Ñ„…‘‘ÌÕ¹ÁÕ‰±¥Í¡•µ…¹…•µ•¹ÐÍÑÉÕÑÕÉ•Ì…¹•‘¥Ñ½È…Á…‰¥±¥Ñä°‰ÕÐ‘¥™™•É•¹•ÌµÕÍÐ‰”É•Ñ…¥¹•…ÌÍ½ÕÉ”½Ù•ÉÍ¥½¸‘¥™™•É•¹•ÌÉ…Ñ¡•ÈÑ¡…¸Í¥±•¹Ñ±äÉ•½¹¥±•¸((ŒŒŒI•…‘¥¹œÉÕ±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÄéÌÀÀÀÀÀÙ€()U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()UÍ”Ñ¡”¹…ÉÉ½Ý•ÍÐÍ½ÕÉ”Ñ¡…Ð…¹ÍÝ•ÉÌÑ¡”ÅÕ•ÍÑ¥½¸è((´™Õ¹Ñ¥½¹…°™É…µ”µ•…¹¥¹œƒŠHmÕ¹Ñ¥½¹…°É•™•É•¹•t ¸¸½™Õ¹Ñ¥½¹…°¼¤ì(´½µµ½¸™É…µ”É…µµ…ÈƒŠHmAÉ½Ñ½½±t ¸¸½ÁÉ½Ñ½½°¼¤ì(´¥¹ÍÑ…±±•‘¥Í½Ù•Éä…¹É•…µ‰…¬ƒŠHm¥…¹½ÍÑ¥Ít ¸¸½‘¥…¹½ÍÑ¥Ì¼¤ì(´•Ù¥”…Á…‰¥±¥Ñä¡¥•É…É¡äƒŠHm•Ù¥”5½‘•±t ¸¸½‘•Ù¥”µµ½‘•°¼¤ì(´ÁÉ½É…µµ¥¹œÍÑ…Ñ”¡…¹•ÌƒŠHmAÉ½É…µµ¥¹t ¸¸½ÁÉ½É…µµ¥¹œ¼¤ì(´Í•¹…É¥¼µ•‘¥Ñ½ÈÙ½…‰Õ±…ÉäƒŠHmM•¹…É¥¼¹¥¹•t ¸¸½Í•¹…É¥¼µ•¹¥¹”¼¤ì(´…ÁÁ±¥…Ñ¥½¸‘…Ñ„±½…‘¥¹œ…¹‰½Õ¹‘…É¥•ÌƒŠHÑ¡¥ÌÍ•Ñ¥½¸¸()%µÁ±•µ•¹Ñ…Ñ¥½¸™…ÑÌ…É”±…‰•±±•…Ì•ÍÑ…‰±¥Í¡•°¥µÁ±•µ•¹Ñ…Ñ¥½¸µ‘•É¥Ù•°¥¹™•ÉÉ•°½ÈÕ¹­¹½Ý¸Ý¡•É”Ñ¡”‘¥ÍÑ¥¹Ñ¥½¸µ…ÑÑ•ÉÌ¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàÈ()M½ÕÉ”Á…Ñ è¥¹Ñ•É¹…±Ì½…Ñ…±½Õ”µÉ•Í½±ÕÑ¥½¸¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„è¥¹Ñ•É¹…±Í€((ŒŒ…Ñ…±½Õ”I•Í½±ÕÑ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()5!…Ñ…±½Õ”¹‘‰€¥ÌÑ¡”ÁÉ¥¹¥Á…°ÁÉ½‘ÕÐµ…Á…‰¥±¥Ñäµ½‘•°¸%Ð½¹¹•ÑÌµ…É­•Ñ••Ù¥•Ì…¹M-UÌÑ¼Í¡…É•¥Ñ•µÌ°™¥ÉµÝ…É”‘•™¥¹¥Ñ¥½¹Ì°5½‘Õ±•Ì°=‰©•ÑÌ°Y¥É¥¸=‰©•ÑÌ°½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¹Ì°…¹½¹Ñ•áÑÕ…°½¹ÍÑÉ…¥¹ÑÌ¸((ŒŒŒAÉ¥¹¥Á…°…Á…‰¥±¥ÑäÁ…Ñ ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()ðMÑ…”ðAÉ¥¹¥Á…°ÍÑÉÕÑÕÉ”ðI•ÍÕ±Ðð)ð€´´´ð€´´´ð€´´´ð)ðAÉ½‘ÕÐð9}Y%€ð‰É…¹‘••Ù¥”É•½É°ÍÑ…¹‘…É¹…µ”°…¹ÁÉ½‘ÕÐ½‘”½M-Tð)ðM¡…É•…Á…‰¥±¥Ñäð9}%Q5€ð¥Ñ•´Í¡…É•‰ä½¹”½Èµ½É”•Ù¥”É•½É‘Ìð)ðMåÍÑ•´¥‘•¹Ñ¥ÑäðM}%Q5}MeMQ5€ð…Ñ…±½Õ”ÍåÍÑ•´…ÍÍ½¥…Ñ¥½¸…¹¥Ñ•´µ±•Ù•°µ½‘½‰©€ð)ð¥ÉµÝ…É”ð9}%I5]I€°9}	U%1M€ðÙ•ÉÍ¥½¹•…Á…‰¥±¥Ñä‘•™¥¹¥Ñ¥½¸ð)ð=‰©•ÐÍÕÁÁ½ÉÐðM}=	)Q}%I5]I€ð=‰©•ÑÌÍÕÁÁ½ÉÑ•‰ä½¹”™¥ÉµÝ…É”ð)ð5½‘Õ±”Á±…•µ•¹Ðð9}M1=QM€ð=‰©•Ð…±Ñ•É¹…Ñ¥Ù•Ì…Ð•Ù¥”µ±½…°Í±½Ñ€Á½Í¥Ñ¥½¹Ìð)ð½¹™¥ÕÉ…‰±”Ñ•µÁ±…Ñ”ðY¥É¥¸µ=‰©•Ð…ÍÍ½¥…Ñ¥½¸Ñ…‰±•ÌðÁ•Éµ¥ÑÑ•=‰©•ÐÍ•Ð‰•™½É”™¥¹…°…ÍÍ¥¹µ•¹Ðð)ð½¹™¥ÕÉ…Ñ¥½¸ð9}=9€…¹É•±…Ñ•Ñ…‰±•ÌðÁÉ½Á•ÉÑ¥•Ì°‘½µ…¥¹Ì°™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¹Ì°…¹½¹Ù•ÉÍ¥½¹Ìð()Q¡”½¹•ÁÑÕ…°µ½‘•°¥Ì€¨©A¡åÍ¥…°•Ù¥”ƒŠH¥ÉµÝ…É”ƒŠH5½‘Õ±”ƒŠH=‰©•ÐƒŠH½¹™¥ÕÉ…Ñ¥½¸¨¨¸((…m…Ñ…±½Õ”¥‘•¹Ñ¥Ñä…¹…Á…‰¥±¥Ñäµ½‘•±t ¸¸½…ÍÍ•ÑÌ½‘¥…É…µÌ½…Ñ…±½Õ”µ…Á…‰¥±¥Ñä¹ÍÙœ¤()Q¡”‘¥…É…´Í¡½ÝÌ•ÍÑ…‰±¥Í¡•…Ñ…±½Õ”É•±…Ñ¥½¹Í¡¥ÁÌ…¹…ÍÍ½¥…Ñ¥½¸Ñ…‰±•Ì¸%Ð¥Ì„…Á…‰¥±¥Ñäµ½‘•°è¥¹ÍÑ…±±••Ù¥”ÍÑ…Ñ”ÍÑ¥±°½µ•Ì™É½´‘¥…¹½ÍÑ¥Ì½È„±½…‘•ÁÉ½©•Ð¸((ŒŒŒ%‘•¹Ñ¥ÑäÉ•Í½±ÕÑ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()‘¥…¹½ÍÑ¥Œ¥‘•¹Ñ¥ÑäÉ•ÍÁ½¹Í”‘½•Ì¹½ÐÉ•ÑÕÉ¸…¸9}Y%€ÁÉ¥µ…Éä­•ä¸I•Í½±ÕÑ¥½¸ÁÉ½••‘ÌÑ¡É½Õ µ•…¹¥¹œè((Ä¸É•Ñ…¥¸Ñ¡”É…Ü‘¥…¹½ÍÑ¥Œ•Ù¥”%…Ì…¸¥¹ÍÑ…±±•µ¥¹ÍÑ…¹”¥‘•¹Ñ¥™¥•Èì(È¸½ÉÉ•±…Ñ”%59M%=8€Ä¹=	)Q}5=1€Ý¥Ñ M}%Q5}MeMQ4¹µ½‘½‰©€ì(Ì¸½ÉÉ•±…Ñ”‰É…¹…¹±¥¹”Ù…±Õ•ÌÝ¥Ñ Ñ¡•¥È…Ñ…±½Õ”µ½‘•°™¥•±‘Ìì(Ð¸É•Í½±Ù”Ñ¡”Í¡…É•9}%Q5€ì(Ô¸•¹Õµ•É…Ñ”…¹‘¥‘…Ñ”9}Y%€É•½É‘Ì…¹ÁÉ½‘ÕÐ½‘•Ìì(Ø¸ÕÍ”9}Y%¹¹…µ•€…ÌÑ¡”ÍÑ…¹‘…É5å!=5MÕ¥Ñ”µ™…¥¹œ•Ù¥”‘•ÍÉ¥ÁÑ¥½¸ì(Ü¸ÕÍ”™¥ÉµÝ…É”°¡…É‘Ý…É”°U$°…¹ÁÉ½‘ÕÐ•Ù¥‘•¹”Ñ¼¹…ÉÉ½ÜÑ¡”…¹‘¥‘…Ñ”Í•Ð¸()M•Ù•É…°M-UÌ…¸Í¡…É”½¹”¥Ñ•´…¹™¥ÉµÝ…É”…Á…‰¥±¥Ñä¸AÉ•Í•ÉÙ”Ñ¡”…¹‘¥‘…Ñ”Í•ÐÕ¹±•ÍÌÑ¡”•Ù¥‘•¹”¥‘•¹Ñ¥™¥•Ì½¹”µ…É­•Ñ•ÁÉ½‘ÕÐÕ¹¥ÅÕ•±ä¸()%¸Ñ¡”½É‘¥¹…Éä…‘‘É•ÍÍ••Ù¥”™½É´°%59M%=8€Ä¹9}=9€¥ÌÑ¡”Í•½¹Á…å±½…Ù…±Õ”°¥µµ•‘¥…Ñ•±ä…™Ñ•È=	)Q}5=1€°…¹É•Á½ÉÑÌÑ¡”¹Õµ‰•È½˜Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹ÌÁÉ½Ù¥‘•‰äÑ¡”•Ù¥”¸Q¡¥Ì¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¥Ì½ÉÉ½‰½É…Ñ•‰ä=A8¹‘‰€°…Ñ…±½Õ”½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¹Ì°½‰Í•ÉÙ•É•ÍÁ½¹Í•Ì°…¹ÁÉ½‘ÕÐ‘¥…É…µÌì¥Ð¥Ì¹½Ð…¸=‰©•Ð°Y¥É¥¸=‰©•Ð°™½É´™…Ñ½È°™¥ÉµÝ…É”±…ÍÌ°½È‘…Ñ…‰…Í”­•ä¸Q¡”Í•Á…É…Ñ”•µÁÑäµ]!I€…Ñ•Ý…ä™½É´¥Ì¹½Ð½Ù•É•‰äÑ¡…Ð¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸è½‰Í•ÉÙ•5 ÈÀÈ…¹ÐÔÐ…Ñ•Ý…äÑÕÁ±•ÌÉ•ÑÕÉ¸9}=9€ô€ÄÕ€°½ÕÑÍ¥‘”Ñ¡”½É‘¥¹…Éä€À¸¸ÄÉ€É…¹”°…¹¥ÑÌ•á…Ð…Ñ•Ý…äÍ•µ…¹Ñ¥ÌÉ•µ…¥¸Õ¹É•Í½±Ù•¸M•”m%59M%=8€Å€è•Ù¥”%‘•¹Ñ¥Ñåt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´Äµ‘•Ù¥”µ¥‘•¹Ñ¥Ñä¹µ¹}½¹˜µ…¹µÁ¡åÍ¥…°µ½¹™¥ÕÉ…Ñ½ÉÌ¤¸((ŒŒŒ¥ÉµÝ…É”…¹5½‘Õ±”É•Í½±ÕÑ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()¸¥Ñ•´…¸¡…Ù”µÕ±Ñ¥Á±”™¥ÉµÝ…É”‘•™¥¹¥Ñ¥½¹Ì¸I•Í½±Ù”Ñ¡”Ñ¡É•”µ½µÁ½¹•¹ÐX¹H¹‰€¥‘•¹Ñ¥Ñä…É½ÍÌ9}%I5]I¹™¥ÉµÝ…É•}Y€°9}%I5]I¹™¥ÉµÝ…É•}I€°…¹9}	U%1L¹™¥ÉµÝ…É•}‰€¸Q¡”¥¹ÍÑ…±±•™¥ÉµÝ…É”É•ÍÁ½¹Í”…¹‘•™…Õ±Ð½±½…±¥é…Ñ¥½¸µ•Ñ…‘…Ñ„…¸¹…ÉÉ½ÜÑ¡”¡½¥”°‰ÕÐÑ¡”•á…Ð5å!=5MÕ¥Ñ”Í•±•Ñ¥½¸…±½É¥Ñ¡´¥Ì¹½ÐÁÉ•Í•¹Ð¥¸Ñ¡”…¹½¹¥…°½ÉÁÕÌ¸()¸•áÁ±¥¥Ð½µÁ½¹•¹ÐÙ…±Õ”½˜€´Å€¥ÌÍÑÉ½¹±ä½ÉÉ½‰½É…Ñ•…Ì€¨©…¹ä½ÈÕ¹ÍÁ•¥™¥•¨¨™½ÈÑ¡…Ð½µÁ½¹•¹ÐèÑ¡”…Ñ…±½Õ”½¹Ñ…¥¹Ì‰½Ñ €´Ä¸´Ä¸´Å€‘•™…Õ±ÑÌ…¹½¹É•Ñ”X¹H¸´Å€‘•™¥¹¥Ñ¥½¹Ì¸AÉ•Í•ÉÙ”Ñ¡¥Ì…Ì…¸¥¹™•ÉÉ•Ý¥±‘…É½‘•™…Õ±ÐÍ•µ…¹Ñ¥Œ°¹½Ð…Ì„ÁÉ½Ù•¸ÁÉ••‘•¹”…±½É¥Ñ¡´¸¼¹½Ð•ÅÕ…Ñ”…¸•áÁ±¥¥Ð‰Õ¥±½˜€´Å€Ý¥Ñ Ñ¡”…‰Í•¹”½˜…¸9}	U%1M€É½Ü¸M•”m¥ÉµÝ…É•t ¸¸½‘•Ù¥”µµ½‘•°½™¥ÉµÝ…É”¹µÑ¡”´´ÄµÍ•¹Ñ¥¹•°¤™½ÈÑ¡”•Ù¥‘•¹”…¹½Õ¹ÑÌ¸()=¹”™¥ÉµÝ…É”¥ÌÉ•Í½±Ù•°M}=	)Q}%I5]I€¥Ù•ÌÍÕÁÁ½ÉÑ•=‰©•ÑÌ°9}M1=QL¹™¥ÉÍÑ}Í±½Ñ€Á±…•Ì=‰©•Ð…±Ñ•É¹…Ñ¥Ù•Ì°Y¥É¥¸µ=‰©•Ð…ÍÍ½¥…Ñ¥½¹Ì‘•ÍÉ¥‰”½¹™¥ÕÉ…‰±”Ñ•µÁ±…Ñ•Ì°…¹Í±½Ð½¹‘¥Ñ¥½¹Ì…¸É•µ½Ù”…±Ñ•É¹…Ñ¥Ù•Ì¥¸„Á…ÉÑ¥Õ±…È½¹™¥ÕÉ…Ñ¥½¸¸()¼¹½Ð½Õ¹Ð9}M1=QM€É½ÝÌ…Ì5½‘Õ±•Ìè½¹”Í±½Ñ€…¸¡…Ù”Í•Ù•É…°=‰©•Ð…±Ñ•É¹…Ñ¥Ù•Ì¸((ŒŒŒIÕ¹Ñ¥µ”5½‘Õ±”ÁÉ½©•Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÀÕ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()%59M%=8€ÌÁ€Í•±•ÑÌÑ¡”µ•…¹¥¹œ½˜-e=€Ñ¡É½Õ MQQ€è()ðMQQ€ð-e=€¹…µ•ÍÁ…”ð5•…¹¥¹œð)ð€´´´ð€´´´ð€´´´ð)ð€Á€ð9}-e}=	)P¹­•å}½‰©•Ñ€ð•¹…‰±•5½‘Õ±”ìÉ•Õ±…È½¹™¥ÕÉ•=‰©•Ðð)ð€Å€ð9}Y%I%9}=	)P¹Ù¥É¥¹}­•å}½‰©•Ñ€ð‘¥Í…‰±•5½‘Õ±”ìY¥É¥¸=‰©•Ð…¹½¹™¥ÕÉ…‰±”É½±”ð()Q¡¥Ì¥Ì„ÍÑ…Ñ”µ‘•Á•¹‘•¹Ð•áÑ•É¹…°¥‘•¹Ñ¥™¥•È¸Q¡”%59M%=8€ÌÁ€Á½±…É¥Ñä¥Ì•ÍÑ…‰±¥Í¡•‰ä½¹ÑÉ½±±•‘¥…¹½ÍÑ¥Œ½ÁÉ½É…µµ¥¹œ•Ù¥‘•¹”½ÉÉ•±…Ñ•Ý¥Ñ 5å!=5}MÕ¥Ñ”U$‰•¡…Ù¥½Èì¥Ð¥Ì¹•¥Ñ¡•È9}-e}=	)P¹¥‘}­•å}½‰©•Ñ€¹½È9}Y%I%9}=	)P¹¥‘}Ù¥É¥¹}­•å}½‰©•Ñ€¸()UÍ”Ñ¡”Í…µ”Í±½Ñ€Ñ¼…ÑÑ… %59M%=8€ÌÉ€…‘‘É•ÍÌ‘…Ñ„…¹%59M%=8€ÌÕ€½¹™¥ÕÉ…Ñ¥½¸Ù…±Õ•Ì¸¼¹½ÐÉ•¹Õµ‰•ÈÁÉ½Ñ½½°Í±½ÑÌÑ¼µ…Ñ Ñ¡”U$¸((ŒŒŒ½¹™¥ÕÉ…Ñ¥½¸½Ý¹•ÉÍ¡¥À()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°¹½Ð…ÁÁ±¥…‰±•€()9}=9€ÕÍ•ÌÑÝ¼•á±ÕÍ¥Ù”½Ý¹•ÉÍ¡¥ÀÁ…ÑÑ•É¹Ìè()ðM½Á”ð-•äÁ…ÑÑ•É¸ð)ð€´´´ð€´´´ð)ð=‰©•ÐµÍ½Á•ðÉ•Í½±Ù•¥‘}­•å}½‰©•Ñ€ì¥‘}™¥ÉµÝ…É”€ô€Á€ð)ð¥ÉµÝ…É”µÍ½Á•ð¥‘}­•å}½‰©•Ð€ô€Á€ìÉ•Í½±Ù•¥‘}™¥ÉµÝ…É•€ð()Q¡”é•É¼Ù…±Õ•Ì…É”ƒŠq¹½Ð…ÁÁ±¥…‰±—ŠtÍ•¹Ñ¥¹•±Ì¸QÉ•…Ñ¥¹œ‰½Ñ ½±Õµ¹Ì…Ìµ…¹‘…Ñ½Éä™½É•¥¸­•åÌÝ½Õ±•É…Í”Ñ¡”½Ý¹•ÉÍ¡¥À‘¥ÍÉ¥µ¥¹…Ñ½È¸()½µÁ±•Ñ”ÁÉ½Á•ÉÑä‘¥Ñ¥½¹…Éä¥ÌÑ¡”Õ¹¥½¸½˜‰½Ñ Í½Á•Ì¥¸Ñ¡”É•Í½±Ù•=‰©•Ð½™¥ÉµÝ…É”½¹Ñ•áÐ¸Q¡”½¹™¥ÕÉ…Ñ¥½¸¥‘á€¥Ì¹½Ð±½‰…±±äÕ¹¥ÅÕ”ì¥Ð‰•½µ•Ì„µ•…¹¥¹™Õ°%59M%=8€ÌÔ¹%9a€½¹±ä…™Ñ•È•Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°…¹=‰©•Ð½¹Ñ•áÐ…É”­¹½Ý¸¸((ŒŒŒI•½¹ÍÑÉÕÑ•É•±…Ñ¥½¹Í¡¥ÁÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()5…¹ä…Ñ…±½Õ”É•±…Ñ¥½¹Í¡¥ÁÌ…É”¹½Ð‘•±…É•…ÌME1¥Ñ”™½É•¥¸­•åÌ¸Q¡•ä…É”ÍÕÁÁ½ÉÑ•‰ä…ÍÍ½¥…Ñ¥½¸µÑ…‰±”ÍÑÉÕÑÕÉ”°½µÁ±•Ñ”Á…É•¹Ðµ­•ä½Ù•É…”¥¸Ñ¡”…¹½¹¥…°É•Ù¥Í¥½¸°½¹Í¥ÍÑ•¹ÐÕÍ”…É½ÍÌÑ¡”…Á…‰¥±¥ÑäÉ…Á °…¹‘¥…¹½ÍÑ¥Œ½U$½ÉÉ½‰½É…Ñ¥½¸¸()½Õµ•¹ÐÑ¡•Í”…ÌÉ•½¹ÍÑÉÕÑ•É•±…Ñ¥½¹Í¡¥ÁÌ¸¼¹½Ð…±Ñ•ÈÑ¡”…¹½¹¥…°‘…Ñ…‰…Í”Ñ¼µ…­”Ñ¡•´…ÁÁ•…È‘•±…É•¸()=¹”•ÍÁ•¥…±±ä¥µÁ½ÉÑ…¹Ð•á±ÕÍ¥½¸¥Ì9}Y%¹½‘•€è¥Ð¥Ì„ÁÉ½‘ÕÐ½‘”½M-T°¹½Ð„É•™•É•¹”Ñ¼9}19U¹½‘•€¸½±Õµ¸µ¹…µ”Í¥µ¥±…É¥Ñä¥Ì¹½ÐÉ•±…Ñ¥½¹…°•Ù¥‘•¹”¸((ŒŒŒA¡åÍ¥…°µ½¹™¥ÕÉ…Ñ¥½¸É•Í½±ÕÑ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()A¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸¥Ì„™¥ÉµÝ…É”µ½¹Ñ•áÑÕ…°…Ñ…±½Õ”ÁÉ½‰±•´¸Q¡”…Ñ…±½Õ”‘½•Ì¹½ÐÁÉ½Ù¥‘”½¹”±½‰…°Ñ…‰±”Ñ¡…Ðµ…ÁÌ„É…Ü½¹™¥ÕÉ…Ñ½È¹Õµ‰•ÈÑ¼„Õ¹¥Ù•ÉÍ…°µ•…¹¥¹œ°¹½È‘½•Ì¥ÐÉ•ÅÕ¥É”„¡…¹µµ…¥¹Ñ…¥¹•Ñ½Á½±½äÑ…‰±”™½È•… ™¥ÉµÝ…É”¸((ŒŒŒŒ½¹™¥ÕÉ…Ñ¥½¸µµ½‘”‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()9}=9%}5=€É•¥ÍÑ•ÉÌ™½ÕÈ‘¥ÍÑ¥¹Ðµ½‘•Ì¥¸Ñ¡”…¹½¹¥…°…Ñ…±½Õ”è()ð¥‘}½¹™¥}µ½‘•€ð…Ñ…±½Õ”±…‰•°ð½¹™¥}µ½‘•€ð)ð€´´´ð€´´´ð€´´´ð)ð€Å€ðY¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸ð€Å€ð)ð€É€ð‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸ð€É€ð)ð€Í€ðA¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸ð€Á€ð)ð€Ñ€ðAÉ½‘ÕÐAÉ½É…µµ¥¹œð€Í€ð()M}%I5]I}=9%}5=€É•½É‘ÌÝ¡¥ …Ñ…±½Õ”µ½‘•Ì„™¥ÉµÝ…É”ÍÕÁÁ½ÉÑÌ¸¼¹½Ð½±±…ÁÍ”Y¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸…¹‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸¥¹Ñ¼½¹”…Ñ•½Éäµ•É•±ä‰•…ÕÍ”‰½Ñ …É”¹½¸µÁ¡åÍ¥…°¸()=A8¹‘‰€¡…Ì„Í•Á…É…Ñ”Í•ÅÕ•¹”Ù½…‰Õ±…Éä¸%¸Á…ÉÑ¥Õ±…È°½¹™½¹™¥ÕÉ…Ñ½ÉÍ€¥Ì‘•ÍÉ¥‰•…Ì€‰Q¼Í•Ð‘•Ù¥”½¹™¥ÕÉ…Ñ½ÉÌ°Ù¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸ˆ°Ý¡¥±”½¹™-=€¥Ì‘•ÍÉ¥‰•…Ì…‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸¸Q¡½Í”±…‰•±Ì•ÍÑ…‰±¥Í Ñ¡”ÁÕÉÁ½Í”½˜Ñ¡”É•¥ÍÑ•É•ÁÉ½É…µµ¥¹œÝ½É­™±½ÝÌ¸Q¡•ä‘¼¹½Ð•ÍÑ…‰±¥Í Ñ¡…ÐÍ•ÅÕ•¹”±…‰•±Ì°…Ñ…±½Õ”µ½‘”É•½É‘Ì°…¹5å!=5MÕ¥Ñ”U$±…‰•±Ì…É”¥¹Ñ•É¡…¹•…‰±”½¹•ÁÑÌ¸((ŒŒŒŒI•Í½±Ù•È¥¹ÁÕÑÌ…¹½ÕÑÁÕÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()Q¡”…Ñ…±½Õ”É•Í½±Ù•ÈÑ…­•Ìè((´½¹”•á…Ð9}%I5]I¹¥‘}™¥ÉµÝ…É•€ì(´„…¹‘¥‘…Ñ”Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸­•å•‰ä•á…Ð™¥ÉµÝ…É”½¹™¥ÕÉ…Ñ¥½¸Íåµ‰½±Ìì(´Ñ¡”™¥ÉµÝ…É”Ì=‰©•Ð½Í±½Ð…Á…‰¥±¥ÑäÉ½ÝÌì(´Ñ¡”ÍÑ½É•Í±½Ð½¹‘¥Ñ¥½¹Ì…¹½¹Ù•ÉÍ¥½¸ÉÕ±•Ì™½ÈÑ¡½Í”É½ÝÌ¸()%ÐÍ¡½Õ±É•ÑÕÉ¸è((´Ý¡•Ñ¡•ÈA¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸¥ÌÉ•¥ÍÑ•É•™½ÈÑ¡”™¥ÉµÝ…É”ì(´Ñ¡”É•±•Ù…¹Ð™¥ÉµÝ…É”½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¹Ì…¹Ñ¡•¥È±•…°‘½µ…¥¹Ìì(´…¹‘¥‘…Ñ”=‰©•ÑÌ‰ä¥¹Ñ•É¹…°Í±½Ñ€ì(´ÍÑ½É•½¹‘¥Ñ¥½¸‰É…¹¡•Ì…¹Ý¡•Ñ¡•È•… ¥ÌÉ•…¡…‰±”™½ÈÑ¡¥Ì™¥ÉµÝ…É”ì(´Ñ¡”=‰©•ÐÍ•±•Ñ•™½È•… ¥¹Ñ•É¹…°Í±½Ñ€°Ý¡•¸Í•±•Ñ¥½¸¥ÌÕ¹¥ÅÕ”ì(´…ÁÁ±¥…‰±”9}=9%Q%=8¹¥‘}½¹Ù}ÉÕ±•€Ù…±Õ•Ì…¹É•ÍÕ±Ñ¥¹œ=‰©•ÐµÁÉ½Á•ÉÑä½¹Ù•ÉÍ¥½¹Ì°Ý¡•É”É•Í½±Ù…‰±”ì(´•áÁ±¥¥Ðé•É¼µµ…Ñ °µÕ±Ñ¤µµ…Ñ °Õ¹ÍÕÁÁ½ÉÑ•µ•áÁÉ•ÍÍ¥½¸°…¹Õ¹É•Í½±Ù•ÍÑ…Ñ•Ì¸()Q¡¥Ì¥Ì…Ñ…±½Õ”…Á…‰¥±¥ÑäÉ•Í½±ÕÑ¥½¸¸%Ð‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…Ð…¸¥¹ÍÑ…±±••Ù¥”¥ÌÕÉÉ•¹Ñ±äÕÍ¥¹œA¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸¸((ŒŒŒŒ€Ä¸ÍÑ…‰±¥Í A¡åÍ¥…°µµ½‘”ÍÕÁÁ½ÉÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()UÍ”Ñ¡”•áÁ±¥¥Ð™¥ÉµÝ…É”µÑ¼µµ½‘”…ÍÍ½¥…Ñ¥½¸è()ÍÅ°)M1P(€€€´¹¥‘}½¹™¥}µ½‘”°(€€€´¹‘•ÍÈ°(€€€´¹½¹™¥}µ½‘”)I=4M}%I5]I}=9%}5=L™´))=%89}=9%}5=L´(€=8´¹¥‘}½¹™¥}µ½‘”€ô™´¹¥‘}½¹™¥}µ½‘”)]!I™´¹¥‘}™¥ÉµÝ…É”€ô€é™¥ÉµÝ…É•}¥)=IH	d´¹¥‘}½¹™¥}µ½‘”ì)€()A¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸¥Ì…Ñ…±½Õ”µÍÕÁÁ½ÉÑ•Ý¡•¸Ñ¡”É•ÍÕ±Ð½¹Ñ…¥¹ÌÑ¡”‘¥ÍÑ¥¹ÐA¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¹€É•½É¸5½‘”ÍÕÁÁ½ÉÐ¥Ì„™¥ÉµÝ…É”…Á…‰¥±¥Ñä°¹½Ð¥¹ÍÑ…±±•µÍÑ…Ñ”•Ù¥‘•¹”¸((ŒŒŒŒ€È¸I•Í½±Ù”•á…Ð½¹™¥ÕÉ…Ñ½È‘•™¥¹¥Ñ¥½¹Ì…¹±•…°‘½µ…¥¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹Ñäè…ÁÁ•…ÉÍ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()•µ½¹ÍÑÉ…Ñ•Á¡åÍ¥…°™¥ÉµÝ…É”™¥•±‘Ì¥¸Ñ¡”…¹½¹¥…°…Ñ…±½Õ”…É”™¥ÉµÝ…É”µÍ½Á•9}=9€É½ÝÌÝ¥Ñ ¥‘à€ô€´Å€°µ…­¥¹œÑ¡…ÐÍÑÉÕÑÕÉ”„ÕÍ•™Õ°…¹‘¥‘…Ñ”Í•Ð¸%Ð¥Ì¹½Ð„ÍÕ™™¥¥•¹ÐÁ¡åÍ¥…°µÁ½Í¥Ñ¥½¸Ñ•ÍÐèÑ¡”½µµ½¸%€½%É½Ü¥Ì…±Í¼™¥ÉµÝ…É”µÍ½Á•Ý¥Ñ ¥‘à€ô€´Å€‰ÕÐ¥Ì¹½Ð„±¥Ñ•É…°Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½È¸½ÈÑ½Á½±½äÉ•Í½±ÕÑ¥½¸°Á…ÉÍ”Ñ¡”Íåµ‰½±ÌÕÍ•‰ä•áÁ±¥¥ÐÁ¡åÍ¥…°Í±½ÐÁÉ•‘¥…Ñ•Ì…¹É•Í½±Ù”Ñ¡½Í”Íåµ‰½±ÌÑ¼Ñ¡”•á…Ð™¥ÉµÝ…É”‘•™¥¹¥Ñ¥½¹Ì¸QÉ•…Ð…‘‘¥Ñ¥½¹…°¥‘à€ô€´Å€É½ÝÌ…Ì…¹‘¥‘…Ñ”µ•Ñ…‘…Ñ„Õ¹±•ÍÌ¥¹‘•Á•¹‘•¹Ð…¹½¹¥…°•Ù¥‘•¹”•ÍÑ…‰±¥Í¡•ÌÑ¡•¥ÈÁ¡åÍ¥…°É½±”¸()I•ÑÉ¥•Ù”•… ‘•™¥¹¥Ñ¥½¸Ñ½•Ñ¡•ÈÝ¥Ñ ¥ÑÌ‘½µ…¥¸è()ÍÅ°)M1P(€€€Œ¹¥‘}½¹˜°(€€€Œ¹½¹™}¹…µ”°(€€€Œ¹‘•ÍÈ°(€€€Œ¹‘•ÍÉ}•áÐ°(€€€Œ¹¥‘}½¹™}ÑåÁ”°(€€€Ð¹‘•ÍÈL½¹™}ÑåÁ”°(€€€Œ¹¥‘}½¹™}‘…Ñ…}ÑåÁ”°(€€€‘Ð¹‘…Ñ…}ÑåÁ”°(€€€Œ¹ÁÉ½É•ÍÍ¥Ù”°(€€€Œ¹¥‘à°(€€€È¹Ù…±Õ”°(€€€È¹¹…µ”LÙ…±Õ•}¹…µ”°(€€€È¹‘•ÍÉ}•áÐLÙ…±Õ•}‘•ÍÉ¥ÁÑ¥½¸°(€€€È¸‰‘•™…Õ±ÐˆL‘•™…Õ±Ñ}Ù…±Õ”°(€€€È¹µ¥¹}Ù…±Õ”°(€€€È¹µ…á}Ù…±Õ”°(€€€È¹ÍÑ•À)I=49}=9LŒ)1P)=%89}=9}QeALÐ(€=8Ð¹¥‘}½¹™}ÑåÁ”€ôŒ¹¥‘}½¹™}ÑåÁ”)1P)=%89}=9}Q}QeAL‘Ð(€=8‘Ð¹¥‘}½¹™}‘…Ñ…}ÑåÁ”€ôŒ¹¥‘}½¹™}‘…Ñ…}ÑåÁ”)1P)=%89}=9}I9LÈ(€=8È¹¥‘}½¹˜€ôŒ¹¥‘}½¹˜)]!IŒ¹¥‘}™¥ÉµÝ…É”€ô€é™¥ÉµÝ…É•}¥(€9Œ¹¥‘}­•å}½‰©•Ð€ô€À(€9Œ¹¥‘à€ô€´Ä)=IH	dŒ¹ÁÉ½É•ÍÍ¥Ù”°È¹ÁÉ½É•ÍÍ¥Ù”°È¹¥‘}½¹™}É…¹”ì)€()%¹Ñ•ÉÁÉ•Ð„É…ÜÁ¡åÍ¥…°Ù…±Õ”½¹±äÑ¡É½Õ Ñ¡”•á…Ð9}=9¹¥‘}½¹™€Í•±•Ñ•¥¸Ñ¡”™¥ÉµÝ…É”½¹Ñ•áÐ¸½¹•ÁÑÕ…±±ä°Ñ¡”±½½­ÕÀ­•ä¥Ìè()Ñ•áÐ)™¥ÉµÝ…É”€¬•á…Ð9}=9‘•™¥¹¥Ñ¥½¸€¬É…ÜÙ…±Õ”)€()¹½Ðè()Ñ•áÐ)É…ÜÙ…±Õ”€´øÕ¹¥Ù•ÉÍ…°½¹™¥ÕÉ…Ñ½Èµ•…¹¥¹œ)€()Q¡”…¹½¹¥…°‘…Ñ„‘•µ½¹ÍÑÉ…Ñ•ÌÝ¡ä¸%¸™¥ÉµÝ…É”€ÄÐÕ€°É…Ü€ÄÑ€µ•…¹Ì5	€™½ÈÅ€…¹É€°‰ÕÐ9€™½È4Å€…¹4É€¸I…Ü€ÄÕ€µ•…¹ÌUa€½¸Ñ¡½Í”€™¥•±‘Ì…¹AU1€½¸Ñ¡”5€™¥•±‘Ì¸±Í•Ý¡•É”¥¸Ñ¡”…Ñ…±½Õ”°É…Ü€ÄÑ€…±Í¼…ÁÁ•…ÉÌ…ÌU@½=]8µ½¹½ÍÑ…‰±•€™½ÈA1€™¥•±‘Ì¸9Õµ•É¥Œ•ÅÕ…±¥ÑäÑ¡•É•™½É”…ÉÉ¥•Ì¹¼Õ¹¥Ù•ÉÍ…°½¹™¥ÕÉ…Ñ½ÈÍ•µ…¹Ñ¥Ì¸((ŒŒŒŒ€Ì¸¹Õµ•É…Ñ”=‰©•Ð½Í±½Ð…¹‘¥‘…Ñ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäè…ÁÁ•…ÉÍ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()M}=	)Q}%I5]I€ÍÕÁÁ±¥•Ì=‰©•ÑÌÍÕÁÁ½ÉÑ•‰äÑ¡”™¥ÉµÝ…É”¸9}M1=QM€Á±…•ÌÑ¡½Í”=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¹Ì…Ð•Ù¥”µ±½…°Í±½Ñ€Á½Í¥Ñ¥½¹Ìè()ÍÅ°)M1P(€€€Ì¹¥‘}Í±½Ð°(€€€Ì¹™¥ÉÍÑ}Í±½Ð°(€€€Ì¹™¥á•‘}­¼°(€€€½™Ü¹¥‘}½‰©•Ñ}™¥ÉµÝ…É”°(€€€½™Ü¹¥‘}­•å}½‰©•Ð°(€€€­¼¹­•å}½‰©•Ð°(€€€­¼¹‘•ÍÈL½‰©•Ñ}‘•ÍÉ¥ÁÑ¥½¸)I=4M}=	)Q}%I5]IL½™Ü))=%89}-e}=	)PL­¼(€=8­¼¹¥‘}­•å}½‰©•Ð€ô½™Ü¹¥‘}­•å}½‰©•Ð))=%89}M1=QLLÌ(€=8Ì¹¥‘}½‰©•Ñ}™¥ÉµÝ…É”€ô½™Ü¹¥‘}½‰©•Ñ}™¥ÉµÝ…É”)]!I½™Ü¹¥‘}™¥ÉµÝ…É”€ô€é™¥ÉµÝ…É•}¥)=IH	dÌ¹™¥ÉÍÑ}Í±½Ð°­¼¹­•å}½‰©•Ð°Ì¹¥‘}Í±½Ðì)€()Q¡•Í”É½ÝÌ…É”…¹‘¥‘…Ñ”…Á…‰¥±¥ÑäÁ±…•µ•¹ÑÌ¸M}=	)Q}%I5]I¹¥‘}­•å}½‰©•Ñ€¥ÌÑ¡”‘…Ñ…‰…Í”µ±½…°­•äì©½¥¸9}-e}=	)Q€‰•™½É”ÁÉ•Í•¹Ñ¥¹œÑ¡”•áÑ•É¹…°=‰©•Ð¹Õµ‰•È­•å}½‰©•Ñ€¸M•Ù•É…°=‰©•ÑÌ…¸Í¡…É”½¹”™¥ÉÍÑ}Í±½Ñ€¸¼¹½Ð¡½½Í”…¸=‰©•Ð‰•…ÕÍ”¥Ð…ÁÁ•…ÉÌ™¥ÉÍÐ°¡…ÌÑ¡”±½Ý•ÍÐ¥‘•¹Ñ¥™¥•È°½È¡…Ì™¥á•‘}­½€Í•Ð¸((ŒŒŒŒ€Ð¸I•ÑÉ¥•Ù”ÍÑ½É•Í•±•Ñ¥½¸‰É…¹¡•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄÑ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°Í½ÕÉ•€()ÑÑ… Ñ¡”ÍÑ½É•Í±½Ð½¹‘¥Ñ¥½¹Ìè()ÍÅ°)M1P(€€€Ì¹¥‘}Í±½Ð°(€€€Ì¹™¥ÉÍÑ}Í±½Ð°(€€€Ì¹™¥á•‘}­¼°(€€€½™Ü¹¥‘}½‰©•Ñ}™¥ÉµÝ…É”°(€€€½™Ü¹¥‘}­•å}½‰©•Ð°(€€€­¼¹­•å}½‰©•Ð°(€€€­¼¹‘•ÍÈL½‰©•Ñ}‘•ÍÉ¥ÁÑ¥½¸°(€€€ÍŒ¹¥‘}½¹‘¥Ñ¥½¸°(€€€Œ¹½¹‘¥Ñ¥½¸°(€€€Œ¹¥‘}½¹Ù}ÉÕ±”)I=4M}=	)Q}%I5]IL½™Ü))=%89}-e}=	)PL­¼(€=8­¼¹¥‘}­•å}½‰©•Ð€ô½™Ü¹¥‘}­•å}½‰©•Ð))=%89}M1=QLLÌ(€=8Ì¹¥‘}½‰©•Ñ}™¥ÉµÝ…É”€ô½™Ü¹¥‘}½‰©•Ñ}™¥ÉµÝ…É”)1P)=%8M}M1=Q}=9%Q%=8LÍŒ(€=8ÍŒ¹¥‘}Í±½Ð€ôÌ¹¥‘}Í±½Ð)1P)=%89}=9%Q%=8LŒ(€=8Œ¹¥‘}½¹‘¥Ñ¥½¸€ôÍŒ¹¥‘}½¹‘¥Ñ¥½¸)]!I½™Ü¹¥‘}™¥ÉµÝ…É”€ô€é™¥ÉµÝ…É•}¥)=IH	dÌ¹™¥ÉÍÑ}Í±½Ð°­¼¹­•å}½‰©•Ð°Œ¹¥‘}½¹‘¥Ñ¥½¸ì)€()¹½¸µ•µÁÑä9}=9%Q%=8¹½¹‘¥Ñ¥½¹€¥Ì…¸•áÁ±¥¥Ð…Ñ…±½Õ”ÁÉ•‘¥…Ñ”…ÍÍ½¥…Ñ•Ý¥Ñ …¸=‰©•Ð½Í±½Ð…¹‘¥‘…Ñ”¸%¸Ñ¡”…¹½¹¥…°‘…Ñ„°Á¡åÍ¥…°‰É…¹¡•Ì½µµ½¹±äÕÍ”Í•µ¥½±½¸µÍ•Á…É…Ñ•½¹©Õ¹Ñ¥½¹Ì½¹Ñ…¥¹¥¹œ€õ€…¹€ðù€°™½È•á…µÁ±”4Äõ8í4Èõ<½%€¸()µ…¡¥¹”É•Í½±Ù•È…¸¥µÁ±•µ•¹ÐÑ¡”½¹‘¥Ñ¥½¸™½ÉµÌ…ÑÕ…±±äÉ•ÁÉ•Í•¹Ñ•¥¸Ñ¡”Í½ÕÉ”¸%ÐµÕÍÐ™…¥°±½Í•½¸Íå¹Ñ…à¥Ð‘½•Ì¹½ÐÕ¹‘•ÉÍÑ…¹É…Ñ¡•ÈÑ¡…¸¥¹Ù•¹Ñ¥¹œ…¸¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¸()µÁÑä½¹‘¥Ñ¥½¸É½ÝÌ…¹…¹‘¥‘…Ñ•ÌÝ¥Ñ ¹¼M}M1=Q}=9%Q%=9€É½ÜÉ•µ…¥¸…Ñ…±½Õ”…Á…‰¥±¥Ñäµ•Ñ…‘…Ñ„¸Q¡•¥È±…¬½˜„ÁÉ•‘¥…Ñ”¥Ì¹½Ð°‰ä¥ÑÍ•±˜°…¸¥¹ÍÑÉÕÑ¥½¸Ñ¼…Ñ¥Ù…Ñ”Ñ¡…Ð=‰©•ÐÕ¹‘•È„Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸¸((ŒŒŒŒ€Ô¸ÁÁ±ä±•…°µ‘½µ…¥¸É•…¡…‰¥±¥Ñä‰•™½É”µ…Ñ¡¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()ÍÑ½É•½¹‘¥Ñ¥½¸¥Ì¹½Ð…ÕÑ½µ…Ñ¥…±±ä„±•…°Á¡åÍ¥…°‰É…¹ ™½ÈÑ¡”Í•±•Ñ•™¥ÉµÝ…É”¸A…ÉÍ”•Ù•ÉäÍåµ‰½°É•™•É•¹•‰ä„½¹‘¥Ñ¥½¸°É•Í½±Ù”¥ÐÑ¼Ñ¡”•á…Ð™¥ÉµÝ…É”9}=9€‘•™¥¹¥Ñ¥½¸°…¹½¹ÍÑÉ…¥¸¥Ð‰äÑ¡…Ð‘•™¥¹¥Ñ¥½¸Ì9}=9}I9€¸()‰É…¹ ¥ÌÕ¹É•…¡…‰±”Ý¡•¸¥ÑÌÁÉ•‘¥…Ñ”¡…Ì¹¼Í½±ÕÑ¥½¸¥¹Í¥‘”Ñ¡”™¥ÉµÝ…É”Ì±•…°‘½µ…¥¹Ì¸½È•á…µÁ±”°…¸•ÅÕ…±¥ÑäÑ¼„Íåµ‰½±¥ŒÙ…±Õ”Ñ¡…ÐÑ¡”•á…Ð™¥ÉµÝ…É”‘•™¥¹¥Ñ¥½¸‘½•Ì¹½ÐÁ•Éµ¥Ð¥ÌÕ¹É•…¡…‰±”•Ù•¸¥˜Ñ¡”Í¡…É•½¹‘¥Ñ¥½¸É½Ü•á¥ÍÑÌ¥¸Ñ¡”‘…Ñ…‰…Í”¸()Q¡¥Ì™¥±Ñ•É¥¹œ¥ÌÉ•ÅÕ¥É•‰•™½É”Ñ½Á½±½äÍ•±•Ñ¥½¸è()Ñ•áÐ)ÍÑ½É•½¹‘¥Ñ¥½¸(€€€€´ø±•…°™¥ÉµÝ…É”½¹™¥ÕÉ…Ñ½ÈÙ…±Õ”(€€€€´øÉ•…¡…‰±”Á¡åÍ¥…°½¹‘¥Ñ¥½¸(€€€€´øÍ•±•Ñ•=‰©•Ð½Í±½ÐÑ½Á½±½ä)€()-••ÀÕ¹É•…¡…‰±”É½ÝÌ…ÌÁÉ½Ù•¹…¹”¸¼¹½Ð‘•±•Ñ”½ÈÉ•¥¹Ñ•ÉÁÉ•ÐÑ¡•´µ•É•±ä‰•…ÕÍ”Ñ¡•ä…¹¹½Ð½ÕÈ½¸Ñ¡”™¥ÉµÝ…É”ÕÉÉ•¹Ñ±ä‰•¥¹œÉ•Í½±Ù•¸((ŒŒŒŒ€Ø¸Ù…±Õ…Ñ”Ñ¡”…¹‘¥‘…Ñ”Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄÙ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()9½Éµ…±¥é”•… ÍÕÁÁ±¥•Á¡åÍ¥…°Ù…±Õ”Ñ¡É½Õ ¥ÑÌ•á…Ð9}=9}I9€Í¼Ñ¡”É•Í½±Ù•ÈÉ•Ñ…¥¹Ì‰½Ñ É…ÜÙ…±Õ”…¹…Ñ…±½Õ”Íåµ‰½±¥Œµ•…¹¥¹œ¸Ù…±Õ…Ñ”•Ù•ÉäÉ•…¡…‰±”•áÁ±¥¥ÐÁÉ•‘¥…Ñ”……¥¹ÍÐÑ¡…Ð¹½Éµ…±¥é•½¹™¥ÕÉ…Ñ¥½¸¸()É½ÕÀÍ…Ñ¥Í™¥•‰É…¹¡•Ì‰ä9}M1=QL¹™¥ÉÍÑ}Í±½Ñ€è((´½¹”‘¥ÍÑ¥¹ÐÍ…Ñ¥Í™¥•=‰©•Ð…¹‘¥‘…Ñ”è½¹‘¥Ñ¥½¸µÍ•±•Ñ•=‰©•Ðì(´¹¼Í…Ñ¥Í™¥•=‰©•Ð…¹‘¥‘…Ñ”èé•É¼µµ…Ñ É•ÍÕ±Ðì(´µ½É”Ñ¡…¸½¹”‘¥ÍÑ¥¹ÐÍ…Ñ¥Í™¥•=‰©•Ð…¹‘¥‘…Ñ”è…µ‰¥Õ½ÕÌÉ•ÍÕ±Ðì(´Õ¹ÍÕÁÁ½ÉÑ•½¹‘¥Ñ¥½¸Íå¹Ñ…à½ÈÕ¹É•Í½±Ù•Íåµ‰½°èÕ¹É•Í½±Ù•É•ÍÕ±Ð¸()¼¹½Ð¥¹Ù•¹Ð„ÁÉ••‘•¹”ÉÕ±”Ñ¼‰É•…¬…µ‰¥Õ¥Ñä¸5Õ±Ñ¥Á±”½¹‘¥Ñ¥½¸É½ÝÌÑ¡…ÐÍ•±•ÐÑ¡”Í…µ”=‰©•Ð½Í±½Ð…ÍÍ½¥…Ñ¥½¸…É”‰É…¹ •Ù¥‘•¹”™½ÈÑ¡”Í…µ”…¹‘¥‘…Ñ”°¹½ÐÍ•Á…É…Ñ”=‰©•ÑÌ¸((ŒŒŒŒ€Ü¸M•Á…É…Ñ”Ñ½Á½±½äÍ•±•Ñ¥½¸™É½´ÁÉ½Á•ÉÑä½¹Ù•ÉÍ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€()Q½Á½±½äÍ•±•Ñ¥½¸…¹ÍÝ•ÉÌè((ø]¡¥ =‰©•Ð…±Ñ•É¹…Ñ¥Ù”¥ÌÍ•±•Ñ•…Ð•… Í±½Ñ€‰äÑ¡”Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸ü()AÉ½Á•ÉÑä½¹Ù•ÉÍ¥½¸¥Ì„±…Ñ•È½Á•É…Ñ¥½¸è((ø¥Ù•¸Ñ¡”Í•±•Ñ•=‰©•Ð…¹Á¡åÍ¥…°½¥Ñ•´Ù…±Õ•Ì°Ý¡…Ð=‰©•Ðµ±•Ù•°½¹™¥ÕÉ…Ñ¥½¸Ù…±Õ•ÌÉ•ÍÕ±Ðü()¼¹½Ðµ•É”Ñ¡•Í”½Á•É…Ñ¥½¹Ì¸()½È•… Í…Ñ¥Í™¥•½¹‘¥Ñ¥½¸Ñ¡…ÐÍÕÁÁ±¥•Ì9}=9%Q%=8¹¥‘}½¹Ù}ÉÕ±•€°É•ÑÉ¥•Ù”Ñ¡”½¹Ù•ÉÍ¥½¸É½ÝÌè()ÍÅ°)M1P(€€€¥‘}½¹Ù}ÉÕ±”°(€€€¥Ñ•µ}½¹˜°(€€€¥Ñ•µ}½¹™}Ù…±Õ”°(€€€½‰©•Ñ}½¹˜°(€€€½‰©•Ñ}½¹™}Ù…±Õ”°(€€€…±Ý…åÍ}ÑÉÕ”°(€€€©ÕµÁ}¥‘}½¹Ù}ÉÕ±”°(€€€¥)I=49}=9Y}IU1)]!I¥‘}½¹Ù}ÉÕ±”€ô€é½¹Ù}ÉÕ±•}¥)=IH	d¥ì)€()ÁÁ±ä¥Ñ•´µÍ¥‘”ÁÉ•‘¥…Ñ•Ì½¹±ä¥¸Ñ¡”•ÍÑ…‰±¥Í¡•Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸½¹Ñ•áÐ°™½±±½Ü©ÕµÁ}¥‘}½¹Ù}ÉÕ±•€…½É‘¥¹œÑ¼Ñ¡”ÍÑ½É•ÉÕ±”‘…Ñ„°…¹Ù…±¥‘…Ñ”…¹äÁÉ½‘Õ•=‰©•ÐÙ…±Õ”……¥¹ÍÐÑ¡”Í•±•Ñ•=‰©•ÐÌ•™™•Ñ¥Ù”‘½µ…¥¸¸%˜Ñ¡”Í•±•Ñ•=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸¡…Ì9}%1QI€…¹9}%1QI}I9€É½ÝÌ™½ÈÑ¡”ÁÉ½‘Õ•ÁÉ½Á•ÉÑä°…ÁÁ±äÑ¡½Í”½¹Ñ•áÑÕ…°É•ÍÑÉ¥Ñ¥½¹Ì…™Ñ•ÈÑ¡”=‰©•Ð¡…Ì‰••¸Í•±•Ñ•ìÑ¡•ä½¹ÍÑÉ…¥¸Ñ¡…Ð=‰©•Ð¥µÁ±•µ•¹Ñ…Ñ¥½¸Ì•™™•Ñ¥Ù”ÁÉ½Á•ÉÑä‘½µ…¥¸…¹…É”¹½ÐÑ½Á½±½äµÍ•±•Ñ¥½¸•‘•Ì¸()=9}Me5	=1}I€…¸ÁÉ½Ù¥‘”…¸•áÁ±¥¥Ð¥Ñ•´µÍåµ‰½°Ñ¼=‰©•ÐµÍåµ‰½°½ÉÉ•ÍÁ½¹‘•¹”™½È½¹”­•å}ÍåÍÑ•µ€…¹Í±½Ñ€è()ÍÅ°)M1P(€€€¥Ñ•µ}½¹™}Íåµ‰½°°(€€€­½}½¹™}ÍåÍµ‰½°°(€€€­•å}ÍåÍÑ•´°(€€€Í±½Ð°(€€€‘•ÍÈ)I=4=9}Me5	=1}I)]!I¥Ñ•µ}½¹™}Íåµ‰½°€ô€é¥Ñ•µ}Íåµ‰½°(€9­•å}ÍåÍÑ•´€ô€é­•å}ÍåÍÑ•´)=IH	dÍ±½Ð°¥ì)€()Q¡”Ñ…‰±”¡…Ì¹¼™¥ÉµÝ…É”½±Õµ¸¸UÍ”¥Ð½¹±äÝ¡•¸Ñ¡”ÍåÍÑ•´…¹Í±½Ð½¹Ñ•áÐ…É”¥¹‘•Á•¹‘•¹Ñ±ä•ÍÑ…‰±¥Í¡•¸%Ð¥Ì¹½Ð„±½‰…°Íåµ‰½°µ…±¥…ÌÑ…‰±”¸((ŒŒŒŒ]½É­••á…µÁ±”è™¥ÉµÝ…É”€ÄÔÝ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°ÍÍ€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€()¥ÉµÝ…É”€ÄÔÝ€‘•µ½¹ÍÑÉ…Ñ•ÌÑ¡”•¹•É¥ŒÁÉ½•‘ÕÉ”ì¥Ð¥Ì¹½Ð„™¥ÉµÝ…É”µÍÁ•¥™¥ŒÉÕ±”•µ‰•‘‘•¥¸Ñ¡”É•Í½±Ù•È¸()Q¡”…Ñ…±½Õ”É•¥ÍÑ•ÉÌ™½ÕÈÍ±½Ñ€Á½Í¥Ñ¥½¹Ì…¹…ÍÍ½¥…Ñ•ÌÑ¡¥Ì™¥ÉµÝ…É”Ý¥Ñ Y¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸°‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸°…¹A¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸¸%ÑÌÉ•±•Ù…¹Ð™¥ÉµÝ…É”µÍ½Á•Á¡åÍ¥…°‘•™¥¹¥Ñ¥½¹Ì…É”è()ðMåµ‰½°ðÁÉ½É•ÍÍ¥Ù•€ð1•…°Á¡åÍ¥…°‘½µ…¥¸ð)ð€´´´ð€´´´ð€´´´ð)ðÅ€ð€Å€ð€À¸¸å€ð)ðA0Å€ð€É€ð€À¸¸å€ð)ð4Å€ð€Í€ð€À¸¸á€ì€ä€ô<½%€ì€ÄÀ€ô=€ì€ÄÈ€ôU@½=]9€ì€ÄÌ€ôU@½=]8µ½¹½ÍÑ…‰±•€ì€ÄÐ€ô9€ì€ÄÔ€ôAU1€ð)ðÉ€ð€Ñ€ð€À¸¸å€ð)ðA0É€ð€Õ€ð€À¸¸å€ð)ð4É€ð€Ù€ðÍ…µ”ÍÑ½É•‘½µ…¥¸…Ì4Å€ð()Q¡”™¥ÉµÝ…É”…±Í¼½Ý¹Ì%€…ÐÁÉ½É•ÍÍ¥Ù”€ô€Á€¸Q¡…Ð¥Ì…¸%™¥•±°¹½Ð½¹”½˜Ñ¡”Í¥àÁ¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹Ì…‰½Ù”¸()…¹‘¥‘…Ñ”Á±…•µ•¹ÑÌ¥¹±Õ‘”=‰©•ÑÌ€Ù€°€Ý€°€ÐÀÁ€°€ÐÀÅ€°€ÐÀÑ€°…¹€ÐÀÙ€…É½ÍÌÑ¡”™½ÕÈÍ±½ÑÌ¸Q¡”•áÁ±¥¥ÐÁ¡åÍ¥…°½¹‘¥Ñ¥½¸É½ÝÌ¹…ÉÉ½ÜÑ¡½Í”…¹‘¥‘…Ñ•Ì¸()½ÈÑ¡”É•ÁÉ•Í•¹Ñ…Ñ¥Ù”Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸è()Ñ•áÐ)4Äõ8)4Èõ<½$)€()Ñ¡”µ…Ñ¡¥¹œ…¹½¹¥…°‰É…¹¡•Ì…É”è()ðÍ±½Ñ€ðM•±•Ñ•=‰©•Ðð½¹‘¥Ñ¥½¸ð¥‘}½¹Ù}ÉÕ±•€ð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð€Å€ð€Ù€ð4Äõ8í4Èõ<½%€ð€ÈÕ€ð)ð€É€ð€Ù€ð4Äõ8í4Èõ<½%€ð€ÈÕ€ð)ð€Í€ð€ÐÀÁ€ð4Äõ8í4Èõ<½%€ð€Ñ€ð)ð€Ñ€ð€ÐÀÁ€ð4Äõ8í4Èõ<½%€ð€Ñ€ð()Q¡”½¹‘¥Ñ¥½¸µÍ•±•Ñ•Ñ½Á½±½ä¥ÌÑ¡•É•™½É”lØ°€Ø°€ÐÀÀ°€ÐÀÁu€¸()M}-=}5}-=}Y€¥¹‘•Á•¹‘•¹Ñ±ä…ÍÍ½¥…Ñ•Ì­•å}½‰©•Ñ}µ€ô€ÐÀÁ€€¡­•å}½‰©•Ñ}µ‘}‘•ÍŒ€ô1¥¡Ð½Õ‰±”½µµ…¹‘€¤Ý¥Ñ ­•å}½‰©•Ñ}‘•Ø€ô€Ù€€¡­•å}½‰©•Ñ}‘•Ù}‘•ÍŒ€ôÑÕ…Ñ½ÈMÌ1¥¡ÑÍ€¤¸%¸Ñ¡”Í±½Ð…Á…‰¥±¥ÑäÉ½ÝÌ°Ñ¡”½ÉÉ•ÍÁ½¹‘¥¹œ9}-e}=	)P¹­•å}½‰©•Ñ€Ù…±Õ•Ì…É”‘•ÍÉ¥‰•…Ì1¥¡Ð½¹ÑÉ½±€…¹1¥¡Ð…ÑÕ…Ñ½É€¸-••ÀÑ¡½Í”‘•ÍÉ¥ÁÑ¥½¸™¥•±‘Ì¥¸Ñ¡•¥ÈÍ½ÕÉ”¹…µ•ÍÁ…•Ì¸Q¡”…ÍÍ½¥…Ñ¥½¸¥Ì…Ñ…±½Õ”™…µ¥±ä•Ù¥‘•¹”ì¥Ð‘½•Ì¹½Ð•¹½‘”„Á•Èµ¥¹ÍÑ…¹”½ÈÁ•ÈµÍ±½Ð•‘”ÍÕ …Ì€‰Í±½Ð€Ä¥Ì¡…Éµ±¥¹­•Ñ¼Í±½Ð€Ìˆ°Í¼¹¼ÍÕ ±¥¹­…”™½±±½ÝÌ™É½´Ñ¡¥Ì•á…µÁ±”¸()Q¡”Í…µ”™¥ÉµÝ…É”‘•µ½¹ÍÑÉ…Ñ•ÌÝ¡äÉ•…¡…‰¥±¥Ñä¥Ìµ…¹‘…Ñ½Éä¸%ÑÌÉ€‘½µ…¥¸¥Ì½¹±ä€À¸¸å€°Ý¡¥±”ÍÑ½É•Í±½Ð½¹‘¥Ñ¥½¹Ì…±Í¼½¹Ñ…¥¸‰É…¹¡•ÌÍÕ …ÌÈõ5	€°ÈõI€°Èõ9€°…¹ÈõUa€¸Q¡½Í”…É”ÍÑ½É•…Ñ…±½Õ”½¹‘¥Ñ¥½¹Ì‰ÕÐ…¹¹½Ð‰”Í…Ñ¥Í™¥•‰ä™¥ÉµÝ…É”€ÄÔÝ€Ì±•…°É€‘½µ…¥¸¸M½µ”ÍÑ½É•‰É…¹¡•Ì…±Í¼É•™•É•¹”…¸4Èõ=9€Ù…±Õ”Ñ¡…Ð¥Ì…‰Í•¹Ð™É½´™¥ÉµÝ…É”€ÄÔÝ€Ì4É€‘½µ…¥¸¸()Q¡”Í•±•Ñ•‰É…¹¡•ÌÁ½¥¹ÐÑ¼½¹Ù•ÉÍ¥½¸ÉÕ±•Ì€ÈÕ€…¹€Ñ€¸AÉ•Í•ÉÙ”Ñ¡½Í”ÉÕ±”%Ì…¹•Ù…±Õ…Ñ”Ñ¡•¥ÈÉ½ÝÌ½¹±ä…™Ñ•È=‰©•ÐÍ•±•Ñ¥½¸¸IÕ±”€Ñ€¡…Ì‘¥É•Ðµ…Ñ¡¥¹œÉ½ÝÌ™½ÈÑ¡¥Ì…¹‘¥‘…Ñ”½¹™¥ÕÉ…Ñ¥½¸è4Äõ9€ÁÉ½‘Õ•ÌÙ…±Õ•Ì€Å€…¹€É€™½ÈÑ¡”ÑÝ¼ÍÑ½É•9}	UQQ€=‰©•ÐµÁÉ½Á•ÉÑäÍåµ‰½±Ì°Ý¡¥±”4Èõ<½%€ÁÉ½‘Õ•Ì4€ô€å€¸Q¡”…¹½¹¥…°9}=9Y}IU1¹½‰©•Ñ}½¹™€ÍÑÉ¥¹Ì™½ÈÑ¡”ÑÝ¼9}	UQQ€É½ÝÌ½¹Ñ…¥¸ÑÉ…¥±¥¹œÝ¡¥Ñ•ÍÁ…”ìÁÉ•Í•ÉÙ”Ñ¡”É…ÜÍÑÉ¥¹ÌÝ¡•¸¥µÁ±•µ•¹Ñ¥¹œ•á…Ð‘…Ñ…‰…Í”µ…Ñ¡¥¹œÉ…Ñ¡•ÈÑ¡…¸Í¥±•¹Ñ±äÑÉ¥µµ¥¹œÑ¡•´¸Q¡¥ÌÍÑ¥±°‘•µ½¹ÍÑÉ…Ñ•ÌÑ¡…Ð½¹”Á¡åÍ¥…°Í•±•Ñ½È…¸½¹ÑÉ¥‰ÕÑ”Ñ¼µ½É”Ñ¡…¸½¹”É•ÍÕ±Ñ¥¹œ=‰©•ÐÁÉ½Á•ÉÑä¸()IÕ±”€ÈÕ€…±Í¼‰•±½¹ÌÑ¼Ñ¡”Í•±•Ñ•…ÑÕ…Ñ½È‰É…¹ °‰ÕÐÑ¡”…¹½¹¥…°‘…Ñ„½¹Ñ…¥¹Ì„Ñ•áÑÕ…°¥ÉÉ•Õ±…É¥ÑäèÑ¡”Á¡åÍ¥…°‘½µ…¥¸…¹½¹‘¥Ñ¥½¸ÕÍ”<½%€°Ý¡¥±”Ñ¡”É•±•Ù…¹ÐÉÕ±”µ€ÈÕ€¥Ñ•´É½ÝÌÕÍ”$½=€¸¼¹½ÐÍ¥±•¹Ñ±ä¹½Éµ…±¥é”Ñ¡½Í”Ñ½­•¹Ì½È±…¥´Ñ¡”½ÉÉ•ÍÁ½¹‘¥¹œÉÕ±”µ€ÈÕ€½ÕÑÁÕÑÌ™½ÈÑ¡¥Ì¥¹ÁÕÐÕ¹±•ÍÌ…¹½¹¥…°•Ù¥‘•¹”•ÍÑ…‰±¥Í¡•Ì•ÅÕ¥Ù…±•¹”¸((ŒŒŒŒ%59M%=8€Ñ€…¹€Õ€…É”„ÑÉ…¹ÍÁ½ÉÐ‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÄå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()=A8¹‘‰€‘•™¥¹•Ìè()Ñ•áÐ(¨m]!=t©m]!It¨Ð©mÅt©mÉt©mÍt©mÑt©mÕt©mÙtŒŒ(¨m]!=t©m]!It¨Ô©mÝt©mát©måt©mÄÁt©mÄÅt©mÄÉtŒŒ)€()… Ä¸¹ÄÉ€Á…É…µ•Ñ•È¡…ÌÑ¡”ÑÉ…¹ÍÁ½ÉÐÉ…¹”€À¸¸ÈÔÕ€¸Q¡”½¹™½¹™¥ÕÉ…Ñ½ÉÍ€Í•ÅÕ•¹”Í•¹‘ÌÑ¡”½ÉÉ•ÍÁ½¹‘¥¹œ€ŒÑ€…¹€ŒÕ€ÁÉ½É…µµ¥¹œ™½ÉµÌ…¹¥Ì‘•ÍÉ¥‰•…ÌÙ¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸¥¸=A8¹‘‰€¸()Q¡½Í”…É”…¹½¹¥…°ÑÉ…¹ÍÁ½ÉÐ™…ÑÌ¸5!…Ñ…±½Õ”¹‘‰€Í•Á…É…Ñ•±ä‘•™¥¹•Ì™¥ÉµÝ…É”µÍÁ•¥™¥ŒÍåµ‰½±Ì°±•…°‘½µ…¥¹Ì°½¹‘¥Ñ¥½¹Ì°…¹½¹Ù•ÉÍ¥½¹Ì¸()Q¡”ÑÝ¼‘…Ñ…‰…Í•Ì½¹Ñ…¥¸¹¼•áÁ±¥¥ÐÉ•±…Ñ¥½¸•ÍÑ…‰±¥Í¡¥¹œ°™½È•Ù•Éä™¥ÉµÝ…É”è()Ñ•áÐ)%59M%=8€Ð¹Ä€ô9}=9¹ÁÉ½É•ÍÍ¥Ù”€Ä)€()½È…¸•ÅÕ¥Ù…±•¹ÐÁ½Í¥Ñ¥½¹…°ÉÕ±”¸9}=9¹ÁÉ½É•ÍÍ¥Ù•€…¸É•Í•µ‰±”Á¡åÍ¥…°½É‘•É¥¹œ¥¸•á…µÁ±•Ì°‰ÕÐÑ¡…ÐÉ•Í•µ‰±…¹”¥Ì¹½Ð„É½ÍÌµ‘…Ñ…‰…Í”­•ä¸9½Ð•Ù•Éä™¥ÉµÝ…É”µ½Ý¹•9}=9€‘•™¥¹¥Ñ¥½¸É•ÁÉ•Í•¹ÑÌ„±¥Ñ•É…°Á¡åÍ¥…°Á±ÕœÁ½Í¥Ñ¥½¸¸-••ÀÑÉ…¹ÍÁ½ÉÐÁ½Í¥Ñ¥½¸…¹…Ñ…±½Õ”½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¸…ÌÍ•Á…É…Ñ”¹…µ•ÍÁ…•ÌÕ¹Ñ¥°„½ÉÉ•±…Ñ¥½¸¥Ì¥¹‘•Á•¹‘•¹Ñ±ä•ÍÑ…‰±¥Í¡•¸((ŒŒŒŒ9}A!e}Q=}Y}QI9M€‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÈÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()Q¡”…¹½¹¥…°9}A!e}Q=}Y}QI9M€Ñ…‰±”½¹Ñ…¥¹Ì½¹±äÑ¡É•”É½ÝÌ°™½È™¥ÉµÝ…É”%Ì€ÄØÁ€°€ØäÅ€°…¹€ÜÈÉ€¸¥ÉµÝ…É”€ÄÔÝ€¡…Ì¹¼É½Ü¸()Q¡¥ÌÑ…‰±”¥ÌÕÍ•™Õ°•Ù¥‘•¹”™½ÈÑ¡½Í”Ñ¡É•”É•½É‘•…Í•Ì¸%Ð¥Ì¹½ÐÑ¡”•¹•É¥ŒÁ¡åÍ¥…°µÑ¼µ…‘Ù…¹•½ÈÁ¡åÍ¥…°µÑ¼µÑ½Á½±½äµ•¡…¹¥Í´¸Q¡”Ý¥‘•È…Ñ…±½Õ”µ•¡…¹¥Í´¥ÌÉ•ÁÉ•Í•¹Ñ•‰ä™¥ÉµÝ…É”µÍÁ•¥™¥Œ9}=9€‘½µ…¥¹Ì°=‰©•Ð½Í±½Ð…¹‘¥‘…Ñ•Ì°Í±½ÐÁÉ•‘¥…Ñ•Ì°9}=9%Q%=8¹¥‘}½¹Ù}ÉÕ±•€°9}=9Y}IU1€°™¥±Ñ•ÉÌ°…¹½¹Ñ•áÑÕ…°Íåµ‰½°É•™•É•¹•Ì¸((ŒŒŒŒI•Í½±ÕÑ¥½¸ÁÍ•Õ‘½½‘”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÈéÌÀÀÀÀÈÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()Ñ•áÐ)™Õ¹Ñ¥½¸É•Í½±Ù•}Á¡åÍ¥…±}½¹™¥ÕÉ…Ñ¥½¸¡™¥ÉµÝ…É•}¥°Á¡åÍ¥…±}Ù…±Õ•Ì¤è(€€€™¥ÉµÝ…É”€ôÉ•ÅÕ¥É•}•á…Ñ}9}%I5]I¡™¥ÉµÝ…É•}¥¤((€€€µ½‘•Ì€ô±½…‘}M}%I5]I}=9%}5=¡™¥ÉµÝ…É•}¥¤(€€€¥˜A¡åÍ¥…±}½¹™¥ÕÉ…Ñ¥½¸¹½Ð¥¸µ½‘•Ìè(€€€€€€€É•ÑÕÉ¸Õ¹ÍÕÁÁ½ÉÑ•‘}Á¡åÍ¥…±}½¹™¥ÕÉ…Ñ¥½¸((€€€‘•™¥¹¥Ñ¥½¹Ì€ô±½…‘}™¥ÉµÝ…É•}9}=9}Ý¥Ñ¡}É…¹•Ì¡™¥ÉµÝ…É•}¥¤(€€€…¹‘¥‘…Ñ•Ì€ô±½…‘}M}=	)Q}%I5]I}…¹‘}9}M1=QL¡™¥ÉµÝ…É•}¥¤(€€€‰É…¹¡•Ì€ô±½…‘}M}M1=Q}=9%Q%=9}…¹‘}9}=9%Q%=8¡…¹‘¥‘…Ñ•Ì¤((€€€Á…ÉÍ•€ômt(€€€É•™•É•¹•‘}Íåµ‰½±Ì€ôÍ•Ð ¤(€€€™½È‰É…¹ ¥¸‰É…¹¡•ÌÝ¥Ñ ¹½¹•µÁÑä½¹‘¥Ñ¥½¸è(€€€€€€€…ÍÐ€ôÁ…ÉÍ•}ÍÕÁÁ½ÉÑ•‘}½¹‘¥Ñ¥½¹}É…µµ…È¡‰É…¹ ¹½¹‘¥Ñ¥½¸¤(€€€€€€€¥˜…ÍÐ¥ÌÕ¹ÍÕÁÁ½ÉÑ•è(€€€€€€€€€€€µ…É¬‰É…¹ Õ¹É•Í½±Ù•(€€€€€€€€€€€½¹Ñ¥¹Õ”(€€€€€€€Á…ÉÍ•¹…ÁÁ•¹¡‰É…¹ °…ÍÐ¤(€€€€€€€É•™•É•¹•‘}Íåµ‰½±Ì€¬ôÍåµ‰½±Ì¡…ÍÐ¤((€€€Á¡åÍ¥…±}‘•™Ì€ôíô(€€€™½ÈÍåµ‰½°¥¸É•™•É•¹•‘}Íåµ‰½±ÌÕ¹¥½¸ÍÕÁÁ±¥•‘}Íåµ‰½±Ì¡Á¡åÍ¥…±}Ù…±Õ•Ì¤è(€€€€€€€µ…Ñ¡•Ì€ô™¥ÉµÝ…É•}9}=9}‘•™¥¹¥Ñ¥½¹Í}¹…µ•¡‘•™¥¹¥Ñ¥½¹Ì°Íåµ‰½°¤(€€€€€€€¥˜½Õ¹Ð¡µ…Ñ¡•Ì¤€„ô€Äè(€€€€€€€€€€€µ…É¬Íåµ‰½°Õ¹É•Í½±Ù•(€€€€€€€€€€€½¹Ñ¥¹Õ”(€€€€€€€Á¡åÍ¥…±}‘•™ÍmÍåµ‰½±t€ôµ…Ñ¡•ÍlÁt((€€€¹½Éµ…±¥é•€ôíô(€€€™½ÈÍÕÁÁ±¥•Íåµ‰½°½Ù…±Õ”è(€€€€€€€‘•™¥¹¥Ñ¥½¸€ôÉ•ÅÕ¥É•}É•Í½±Ù•‘}‘•™¥¹¥Ñ¥½¸¡Á¡åÍ¥…±}‘•™Ì°Íåµ‰½°¤(€€€€€€€¹½Éµ…±¥é•‘mÍåµ‰½±t€ô‘•½‘•}Ý¥Ñ¡}9}=9}I9¡‘•™¥¹¥Ñ¥½¸°Ù…±Õ”¤(€€€€€€€¥˜Ù…±Õ”¹½Ð¥¸‘•™¥¹¥Ñ¥½¸¹±•…±}‘½µ…¥¸è(€€€€€€€€€€€É•ÑÕÉ¸¥¹Ù…±¥‘}Á¡åÍ¥…±}Ù…±Õ”((€€€É•…¡…‰±”€ômt(€€€™½È‰É…¹ °…ÍÐ¥¸Á…ÉÍ•è(€€€€€€€¥˜…¹äÉ•™•É•¹•Íåµ‰½°¥ÌÕ¹É•Í½±Ù•è(€€€€€€€€€€€µ…É¬‰É…¹ Õ¹É•Í½±Ù•(€€€€€€€€€€€½¹Ñ¥¹Õ”(€€€€€€€¥˜ÁÉ•‘¥…Ñ•}¡…Í}¹½}Í½±ÕÑ¥½¸¡…ÍÐ°Á¡åÍ¥…±}‘•™Ì¤è(€€€€€€€€€€€µ…É¬‰É…¹ Õ¹É•…¡…‰±”(€€€€€€€€€€€½¹Ñ¥¹Õ”(€€€€€€€É•…¡…‰±”¹…ÁÁ•¹¡‰É…¹ ¤((€€€Í•±•Ñ•€ô•Ù…±Õ…Ñ•}É•…¡…‰±•}‰É…¹¡•Ì¡É•…¡…‰±”°¹½Éµ…±¥é•¤((€€€™½È¥¹Ñ•É¹…±}Í±½Ðè(€€€€€€€‘¥ÍÑ¥¹Ñ}½‰©•ÑÌ€ôÍ•±•Ñ•½‰©•ÑÌ™½È¥¹Ñ•É¹…±}Í±½Ð(€€€€€€€¥˜½Õ¹Ð¡‘¥ÍÑ¥¹Ñ}½‰©•ÑÌ¤€ôô€Àè(€€€€€€€€€€€É•Á½ÉÐé•É¼µµ…Ñ (€€€€€€€•±Í”¥˜½Õ¹Ð¡‘¥ÍÑ¥¹Ñ}½‰©•ÑÌ¤€ø€Äè(€€€€€€€€€€€É•Á½ÉÐ…µ‰¥Õ½ÕÌ(€€€€€€€•±Í”è(€€€€€€€€€€€É•Ñ…¥¸Í•±•Ñ•=‰©•Ð…¹Í…Ñ¥Í™¥•½¹‘¥Ñ¥½¸((€€€™½ÈÍ•±•Ñ•‰É…¹ Ý¥Ñ ¥‘}½¹Ù}ÉÕ±”è(€€€€€€€•Ù…±Õ…Ñ”9}=9Y}IU1…™Ñ•È=‰©•ÐÍ•±•Ñ¥½¸(€€€€€€€ÕÍ”=9}Me5	=1}I½¹±ä¥¸µ…Ñ¡¥¹œÍåÍÑ•´½Í±½Ð½¹Ñ•áÐ(€€€€€€€É•Ù…±¥‘…Ñ”ÁÉ½‘Õ•=‰©•ÐÙ…±Õ•Ì((€€€É•ÑÕÉ¸Ñ½Á½±½ä°½¹Ù•ÉÑ•ÁÉ½Á•ÉÑ¥•Ì°ÁÉ½Ù•¹…¹”°…¹•ÉÉ½ÈÍÑ…Ñ•Ì)€()Q¡”É•Í½±Ù•ÈÍ¡½Õ±É•Ñ…¥¸…¹‘¥‘…Ñ”É½ÝÌ°É•©•Ñ•Õ¹É•…¡…‰±”‰É…¹¡•Ì°Í…Ñ¥Í™¥•ÁÉ•‘¥…Ñ•Ì°½¹Ù•ÉÍ¥½¸µÉÕ±”Á…Ñ¡Ì°…¹Õ¹É•Í½±Ù••áÁÉ•ÍÍ¥½¹Ì…ÌÁÉ½Ù•¹…¹”¸ÍÕ•ÍÍ™Õ°…Ñ…±½Õ”É•ÍÕ±ÐÉ•µ…¥¹Ì…Á…‰¥±¥Ñä•Ù¥‘•¹”É…Ñ¡•ÈÑ¡…¸ÁÉ½½˜½˜•Ù¥”ÉÕ¹Ñ¥µ”‰•¡…Ù¥½È¸()½ÈÑ¡”½¹•ÁÑÕ…°µ½‘•°°Í•”m½¹™¥ÕÉ…Ñ¥½¹t ¸¸½‘•Ù¥”µµ½‘•°½½¹™¥ÕÉ…Ñ¥½¸¹µ¤¸½È¥¹ÍÑ…±±•É•…µ‰…¬°Í•”m¥…¹½ÍÑ¥Ít ¸¸½‘¥…¹½ÍÑ¥Ì¼¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàÌ()M½ÕÉ”Á…Ñ è¥¹Ñ•É¹…±Ì½‘…Ñ„µÍÑ½É”µÉ•ÍÁ½¹Í¥‰¥±¥Ñ¥•Ì¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„è¥¹Ñ•É¹…±Í€((ŒŒ…Ñ„MÑ½É”I•ÍÁ½¹Í¥‰¥±¥Ñ¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÌéÌÀÀÀÀÀÅ€()5å!=5MÕ¥Ñ”Í•Á…É…Ñ•ÌÁÉ½‘ÕÐ…Á…‰¥±¥Ñä°ÁÉ½Ñ½½°Ý½É­™±½ÝÌ°Í•¹…É¥¼µ•‘¥Ñ½ÈÙ½…‰Õ±…Éä°…¹Í•±•Ñ•É½ÍÌµÁÉ½Á•ÉÑäÙ…±¥‘…Ñ¥½¸¥¹Ñ¼‘¥™™•É•¹ÐÍÑ½É•Ì¸9¼Í¥¹±”™¥±”¥Ì„½µÁ±•Ñ”µ½‘•°½˜Ñ¡”¥¹ÍÑ…±±…Ñ¥½¸¸((ŒŒŒI•ÍÁ½¹Í¥‰¥±¥Ñäµ…ÑÉ¥à()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÌéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()ðMÑ½É”ðMÑÉ½¹•ÍÐ•Ù¥‘•¹”ð½•Ì¹½Ð•ÍÑ…‰±¥Í …±½¹”ð)ð€´´´ð€´´´ð€´´´ð)ð5!…Ñ…±½Õ”¹‘‰€ð•Ù¥•Ì°M-UÌ°¥Ñ•µÌ°‰É…¹‘Ì°±¥¹•Ì°™¥ÉµÝ…É”°5½‘Õ±•Ì°=‰©•ÑÌ°Y¥É¥¸=‰©•ÑÌ°½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¹Ì°É…¹•Ì°™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¹Ì°…¹½¹Ù•ÉÍ¥½¹ÌðÕÉÉ•¹Ð¥¹ÍÑ…±±•ÍÑ…Ñ”°½µÁ±•Ñ”™Õ¹Ñ¥½¹…°ÁÉ½Ñ½½°°½ÈÍ•¹…É¥¼É…Á ð)ð=A8¹‘‰€ðÍåÍÑ•´É•¥ÍÑÉä°µ…¹…•µ•¹Ð™É…µ”Ñ•µÁ±…Ñ•Ì°Á…É…µ•Ñ•ÉÌ°…‘‘É•ÍÌÉÕ±•Ì°Í•¹…É¥½Ì°Í•ÅÕ•¹•Ì°‘¥É•Ñ¥½¸°É•Á•Ñ¥Ñ¥½¸°Ñ¥µ•ÉÌ°…¹ÍÑ…ÑÕÌÑÉ…¹Í¥Ñ¥½¹Ìð½µÁ±•Ñ”•Ù¥”…Ñ…±½Õ”°½É‘¥¹…Éä™Õ¹Ñ¥½¹…°½µµ…¹Ù½…‰Õ±…Éä°½È•Ù¥”µÍÁ•¥™¥ŒÍÕÁÁ½ÉÐð)ð=Á•¹EÕ•Éä¹ÑáÑ€ð¹…µ•ME0ÍÑ…Ñ•µ•¹ÑÌ¥¹Ñ•¹‘•Ñ¼…ÍÍ•µ‰±”Í•±•Ñ•=A8¹‘‰€ÍÑÉÕÑÕÉ•Ìð…ÁÁ±¥…Ñ¥½¸½¹ÑÉ½°™±½Ü‰•å½¹Ñ¡½Í”ÅÕ•É¥•Ì½ÈÍ•µ…¹Ñ¥Ì…‰Í•¹Ð™É½´Ñ¡”Í•±•Ñ•½±Õµ¹Ìð)ðM•¹…É¥½•Ù¥•Ì™¥±•ÌðÍ•¹…É¥¼µ•‘¥Ñ½È=‰©•ÐMåÍÑ•µÌ°•Ù¥”=‰©•ÑÌ°½µµ…¹‘Ì°A…É…µ•Ñ•ÉÌ°…Ñ•½É¥•Ì°µ…Ñ¡¥¹œ%Ì°…¹…Ñ¥½¸Ñ•µÁ±…Ñ•Ìð¥¹ÍÑ…±±••Ù¥”¥‘•¹Ñ¥Ñä°…Ñ…±½Õ”=‰©•Ð•ÅÕ…±¥Ñä°½ÈÁ•ÉÍ¥ÍÑ•ÕÍ•ÈÍ•¹…É¥½Ìð)ðÉÕ±•Ì¹‘ˆÍ€ð±¥¹­•µÁÉ½Á•ÉÑäÙ…±¥‘…Ñ¥½¸™½ÈÍ•±•Ñ•Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°=‰©•ÑÌð„•¹•É…°=‰©•ÐÉ•¥ÍÑÉä½ÈÕ¹¥Ù•ÉÍ…°Ù…±¥‘…Ñ¥½¸•¹¥¹”ð)ðAÕ‰±¥Œ=Á•¹]•‰9•ÐAÌðÁÕ‰±¥Í¡•™É…µ”É…µµ…È…¹™Õ¹Ñ¥½¹…°]!=€Í•µ…¹Ñ¥Ìð5å!=5MÕ¥Ñ”µ…¹…•µ•¹ÐÍÑ…Ñ”µ…¡¥¹•Ì½È…Ñ…±½Õ”¡¥•É…É¡äð)ð=‰Í•ÉÙ•ÑÉ…™™¥Œð…ÑÕ…°½É‘•É¥¹œ°Ù…±Õ•Ì°É•Á•Ñ¥Ñ¥½¸°…¹•Ù¥”‰•¡…Ù¥½Èð‰•¡…Ù¥½È½˜Õ¹½‰Í•ÉÙ•ÁÉ½‘ÕÑÌ½ÈÙ•ÉÍ¥½¹Ìð)ð5å!=5MÕ¥Ñ”U$ð‘¥ÍÁ±…å•±…‰•±Ì°Ù¥Í¥‰¥±¥Ñä°•‘¥Ñ…‰¥±¥Ñä°…¹Ý½É­™±½Ü‰•¡…Ù¥½ÈðÝ¥É”•¹½‘¥¹œÝ¥Ñ¡½ÕÐ„‘…Ñ…‰…Í”½È…ÁÑÕÉ”½ÉÉ•±…Ñ¥½¸ð((ŒŒŒ½µÁ½Í¥Ñ¥½¸°¹½Ð„±½‰…°©½¥¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÌéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()Q¡”ÍÑ½É•Ì…É”½µÁ½Í•Ñ¡É½Õ „Í•ÅÕ•¹”½˜É•Í½±Ù•µ•…¹¥¹Ìè((Ä¸„‘¥…¹½ÍÑ¥ŒÉ•ÍÁ½¹Í”¥‘•¹Ñ¥™¥•Ì…¸¥¹ÍÑ…±±••Ù¥”¥¹ÍÑ…¹”ì(È¸%59M%=8€Å€…¹Ù•ÉÍ¥½¸É•ÍÁ½¹Í•Ì¹…ÉÉ½ÜÑ¡”…Ñ…±½Õ”¥Ñ•´…¹™¥ÉµÝ…É”ì(Ì¸%59M%=8€ÌÁ€°€ÌÉ€°…¹€ÌÕ€‘•ÍÉ¥‰”¥¹ÍÑ…±±•5½‘Õ±”½=‰©•Ð½½¹™¥ÕÉ…Ñ¥½¸ÍÑ…Ñ”ì(Ð¸…Ñ…±½Õ”É•±…Ñ¥½¹Í¡¥ÁÌ‘•Ñ•Éµ¥¹”ÍÕÁÁ½ÉÑ•…±Ñ•É¹…Ñ¥Ù•Ì…¹•™™•Ñ¥Ù”Ù…±Õ”‘½µ…¥¹Ìì(Ô¸=A8¹‘‰€‘•Ñ•Éµ¥¹•ÌÑ¡”…ÁÁ±¥…‰±”µ…¹…•µ•¹ÐÝ½É­™±½Ü…¹ÑÉ…¹ÍÁ½ÉÐ™¥•±‘Ìì(Ø¸™Õ¹Ñ¥½¹…°ÍÁ•¥™¥…Ñ¥½¹Ì‘•Ñ•Éµ¥¹”Ñ¡”µ•…¹¥¹œ½˜½Á•É…Ñ¥½¹…°™É…µ•Ìì(Ü¸M•¹…É¥½•Ù¥•Ì½¹ÑÉ¥‰ÕÑ•Ì•‘¥Ñ½È…Á…‰¥±¥Ñ¥•Ì½¹±ä…™Ñ•È„™Õ¹Ñ¥½¹…°½ÉÉ•±…Ñ¥½¸¥Ì•ÍÑ…‰±¥Í¡•¸()¹Õµ•É¥Œµ…Ñ ¥Ì¹½Ð„½µÁ½Í¥Ñ¥½¸ÉÕ±”¸½È•á…µÁ±”è((´5!…Ñ…±½Õ”¹‘ˆ¹9}MeMQ4¹¥‘}ÍåÍÑ•µ€¥Ì¹½Ð=A8¹‘ˆ¹9}MeMQ4¹¥‘}ÍåÍÑ•µ€ì(´M•¹…É¥½•Ù¥•Ì=‰©•Ñ%‘€¥Ì¹½Ð…ÕÑ½µ…Ñ¥…±±ä9}-e}=	)P¹­•å}½‰©•Ñ€ì(´9}Y%¹¥‘}‘•Ù¥•€¥Ì¹½ÐÑ¡”¥¹ÍÑ…±±•€ÌÈµ‰¥Ð•Ù¥”%ì(´‘¥…¹½ÍÑ¥ŒM1=Q€¥Ì¹½Ð9}M1=QL¹¥‘}Í±½Ñ€ì(´™Õ¹Ñ¥½¹…°]!=€¥Ì¹½Ð„‘…Ñ…‰…Í”ÁÉ¥µ…Éä­•ä¸()Q¡”½µÁ±•Ñ”¥‘•¹Ñ¥™¥•ÈÁ½±¥ä¥Ìµ…¥¹Ñ…¥¹•¥¸mM½ÕÉ•Ì…¹%‘•¹Ñ¥™¥•È	½Õ¹‘…É¥•Ít ¸¸½‘•Ù¥”µµ½‘•°½Í½ÕÉ•Ìµ…¹µ¥‘•¹Ñ¥™¥•ÉÌ¹µ¤¸((ŒŒŒ…Á…‰¥±¥ÑäÙ•ÉÍÕÌ¥¹ÍÑ…¹”‘…Ñ„()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÌéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€°Í½ÕÉ•€()Q¡”ÁÉ•Í•ÉÙ•‘…Ñ…‰…Í•Ì…É”ÁÉ¥¹¥Á…±±ä…Á…‰¥±¥Ñä…¹Ý½É­™±½ÜÉ•¥ÍÑÉ¥•Ì¸Q¡•ä‘•ÍÉ¥‰”Ý¡…Ð5å!=5MÕ¥Ñ”­¹½ÝÌ¡½ÜÑ¼½™™•È½ÈÍ•¹¸()%¹ÍÑ…±±•ÍÑ…Ñ”½µ•Ì™É½´‘¥…¹½ÍÑ¥ŒÑÉ…™™¥Œ°„±½…‘•ÁÉ½©•Ð°U$½‰Í•ÉÙ…Ñ¥½¹Ì°½È…¹½Ñ¡•ÈÁ•ÉÍ¥ÍÑ•¹”Í½ÕÉ”¹½Ðå•ÐÁÉ•Í•ÉÙ•¸()ðEÕ•ÍÑ¥½¸ð½ÉÉ•Ð•Ù¥‘•¹”ð)ð€´´´ð€´´´ð)ð…¸™¥ÉµÝ…É”½™™•È=‰©•Ð€ÐÀÙ€…ÐÍ±½Ñ€€Í€üð…Ñ…±½Õ”…Á…‰¥±¥Ñäð)ð½•ÌÑ¡¥Ì¥¹ÍÑ…±±•5½‘Õ±”ÕÉÉ•¹Ñ±ä•áÁ½Í”=‰©•Ð€ÐÀÙ€üð%59M%=8€ÌÁ€½ÈÁÉ½©•ÐÍÑ…Ñ”ð)ð…¸Ñ¡¥ÌÁÉ½Á•ÉÑä…•ÁÐÙ…±Õ”€Ý€¥¸Ñ¡¥Ì½¹Ñ•áÐüð…Ñ…±½Õ”É…¹”°™¥±Ñ•È°½¹‘¥Ñ¥½¸°…¹±¥¹­•µÉÕ±”•Ù…±Õ…Ñ¥½¸ð)ð]¡¥ ™É…µ”ÝÉ¥Ñ•ÌÑ¡”Ù…±Õ”üð=A8¹‘‰€ÁÉ½É…µµ¥¹œÍ•ÅÕ•¹”ð)ð¥Ñ¡”ÝÉ¥Ñ”Ñ…­”•™™•Ðüð™É•Í ‘¥…¹½ÍÑ¥ŒÉ•…µ‰…¬ð)ð…¸Ñ¡”Í•¹…É¥¼•‘¥Ñ½ÈÉ•¹‘•È…¸…Ñ¥½¸™½È¥ÐüðM•¹…É¥½•Ù¥•ÌÁ±ÕÌ™Õ¹Ñ¥½¹…°½ÉÉ•±…Ñ¥½¸ð((ŒŒŒI•…µ½¹±ä•Ù¥‘•¹”½ÉÁÕÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÌéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè½¹±ä™½É€)AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€()Q¡”É•Á½Í¥Ñ½Éä½Á¥•Ì…É”•Ù¥‘•¹”°¹½Ð„Ý½É­¥¹œ5å!=5MÕ¥Ñ”¥¹ÍÑ…±±…Ñ¥½¸¸Q¡•äµÕÍÐ‰”½Á•¹•É•…µ½¹±ä™½È…¹…±åÍ¥Ì¸()ME1¥Ñ”™½É•¥¸µ­•ä‘•±…É…Ñ¥½¹Ì…É”¹½ÐÕ¹¥™½É´…É½ÍÌÍÑ½É•Ì¸M•¹…É¥½•Ù¥•Ì‘•±…É•Ì¥ÑÌÁÉ¥¹¥Á…°¡¥•É…É¡ä™½É•¥¸­•åÌìµ…¹ä¥µÁ½ÉÑ…¹Ð5!…Ñ…±½Õ”¹‘‰€É•±…Ñ¥½¹Í¡¥ÁÌ…É”É•½¹ÍÑÉÕÑ•™É½´½µÁ±•Ñ”­•ä½Ù•É…”…¹…ÍÍ½¥…Ñ¥½¸ÍÑÉÕÑÕÉ”¸½Õµ•¹Ñ…Ñ¥½¸µÕÍÐ‘¥ÍÑ¥¹Õ¥Í „‘•±…É•½¹ÍÑÉ…¥¹Ð™É½´„½ÉÉ½‰½É…Ñ•É•±…Ñ¥½¹Í¡¥À¸((ŒŒŒ…¥±ÕÉ”Á½±¥ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÌéÌÀÀÀÀÀÙ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€°Õ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()]¡•¸„É•ÅÕ¥É•½ÉÉ•±…Ñ¥½¸¥Ìµ¥ÍÍ¥¹œ°É•Ñ…¥¸É…Ü¥‘•¹Ñ¥™¥•ÉÌ…¹Í½ÕÉ”ÁÉ½Ù•¹…¹”°É•ÑÕÉ¸…¸…µ‰¥Õ½ÕÌ½ÈÕ¹É•Í½±Ù•É•ÍÕ±Ð°…¹‘¼¹½ÐÍ•±•ÐÑ¡”™¥ÉÍÐ•ÅÕ…°¥¹Ñ••È½ÈÝ¥‘•¸„Ù…±Õ”‘½µ…¥¸Ñ¼Ñ¡”ÁÉ½Ñ½½°ÑÉ…¹ÍÁ½ÉÐµ…á¥µÕ´¸()¥…¹½ÍÑ¥Ì…¸ÁÉ•Í•ÉÙ”Õ¹­¹½Ý¸Ù…±Õ•Ì¸AÉ½É…µµ¥¹œÍ¡½Õ±™…¥°±½Í•Õ¹Ñ¥°Ñ¡”É•ÅÕ¥É•½¹Ñ•áÐ¥ÌÉ•Í½±Ù•¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàÐ()M½ÕÉ”Á…Ñ è¥¹Ñ•É¹…±Ì½¥µÁ±•µ•¹Ñ…Ñ¥½¸µ‰½Õ¹‘…É¥•Ì¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„è¥¹Ñ•É¹…±Í€((ŒŒ%µÁ±•µ•¹Ñ…Ñ¥½¸	½Õ¹‘…É¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÐéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()Q¡¥ÌÁ…”Í•Á…É…Ñ•Ì™…ÑÌ‘¥É•Ñ±äÉ•½Ù•É…‰±”™É½´Ñ¡”…¹½¹¥…°5å!=5MÕ¥Ñ”€Ì¸Ô¸Ìà‘…Ñ„™É½´¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¹ÌÑ¡…Ð¹••ÉÕ¹Ñ¥µ”½È…ÁÁ±¥…Ñ¥½¸µ½‘”•Ù¥‘•¹”¸((ŒŒŒÙ¥‘•¹”±•Ù•±Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÐéÌÀÀÀÀÀÉ€()U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()ð1•Ù•°ðUÍ”ð)ð€´´´ð€´´´ð)ðÍÑ…‰±¥Í¡•ð‘¥É•ÐÍ¡•µ„°ÍÑ½É•Ù…±Õ”°‘•±…É•É•±…Ñ¥½¹Í¡¥À°•á…Ð™É…µ”°™¥¹•ÉÁÉ¥¹Ð°½È½‰Í•ÉÙ•‰•¡…Ù¥½Èð)ð%µÁ±•µ•¹Ñ…Ñ¥½¸µ‘•É¥Ù•ðÍÑ…‰±”µ•…¹¥¹œÉ•½Ù•É•™É½´½µÁ±•Ñ”‘…Ñ„Á…ÑÑ•É¹Ì°É•Í½ÕÉ”­•åÌ°½ÈÝ½É­™±½Ü½µÁ½Í¥Ñ¥½¸ð)ð%¹™•ÉÉ•ð‰•ÍÐ•áÁ±…¹…Ñ¥½¸½˜„½µÁ±•Ñ”Á…ÑÑ•É¸Ý¥Ñ¡½ÕÐ…¸•áÁ±¥¥Ð‘•±…É…Ñ¥½¸ð)ðU¹­¹½Ý¸ð•Ù¥‘•¹”¥Ì…‰Í•¹Ð°½¹™±¥Ñ¥¹œ°½ÈÍÕÁÁ½ÉÑÌÍ•Ù•É…°•áÁ±…¹…Ñ¥½¹Ìð()¸¥¹™•É•¹”Í¡½Õ±ÍÑ…Ñ”‰½Ñ ¥ÑÌÍÕÁÁ½ÉÑ¥¹œÁ…ÑÑ•É¸…¹Ñ¡”½‰Í•ÉÙ…Ñ¥½¸Ñ¡…Ð½Õ±‘¥ÍÁÉ½Ù”¥Ð¸((ŒŒŒÍÑ…‰±¥Í¡•‰½Õ¹‘…É¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÐéÌÀÀÀÀÀÍ€()Q¡”ÁÉ•Í•ÉÙ•½ÉÁÕÌ•ÍÑ…‰±¥Í¡•ÌÑ¡…Ð5å!=5MÕ¥Ñ”‘¥ÍÑÉ¥‰ÕÑ•ÌÍ•Ù•É…°¥¹‘•Á•¹‘•¹ÐME1¥Ñ”ÍÑ½É•Ìì=A8¹‘‰€µ½‘•±ÌÍåÍÑ•µÌ…¹Ý½É­™±½ÝÌì=Á•¹EÕ•Éä¹ÑáÑ€¹…µ•ÌÍ•±•Ñ•É•…‘Ì‰ÕÐ¥Ì¥¹½µÁ±•Ñ”ì5!…Ñ…±½Õ”¹‘‰€µ½‘•±Ì…Á…‰¥±¥Ñä…¹½¹Ñ•áÑÕ…°½¹ÍÑÉ…¥¹ÑÌìM•¹…É¥½•Ù¥•Ìµ½‘•±ÌÍ•¹…É¥¼µ•‘¥Ñ½È…Á…‰¥±¥ÑäÉ…Ñ¡•ÈÑ¡…¸½µÁ±•Ñ”Í•¹…É¥¼É…Á¡Ìì…¹ÉÕ±•Ì¹‘ˆÍ€…‘‘Ì±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì™½ÈÍ•±•Ñ•Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°=‰©•ÑÌ¸((ŒŒŒM…™”¥µÁ±•µ•¹Ñ…Ñ¥½¸µ‘•É¥Ù•½¹±ÕÍ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÐéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()Q¡”½µ‰¥¹••Ù¥‘•¹”ÍÕÁÁ½ÉÑÌÑ¡•Í”½¹±ÕÍ¥½¹ÌÝ¡•¸Ñ¡•¥ÈÍ½Á”¥ÌÉ•Ñ…¥¹•è((´=A8¹‘‰€Í•¹…É¥½Ì…¹Í•ÅÕ•¹•Ì™½É´ÍÑ…Ñ”µµ…¡¥¹”‘•™¥¹¥Ñ¥½¹Ì™½È5å!=5MÕ¥Ñ”µ…¹…•µ•¹ÐÝ½É­™±½ÝÌì(´‘¥…¹½ÍÑ¥Œ½ÁÉ½É…µµ¥¹œ%59M%=8€ÌÀ¹-e=€ÕÍ•ÌÑ¡”É•Õ±…È½¹™¥ÕÉ•=‰©•Ð¹…µ•ÍÁ…”™½È…¸•¹…‰±•5½‘Õ±”Ý¡•¸MQQ€ô€Á€…¹Ñ¡”Y¥É¥¸=‰©•Ð¹…µ•ÍÁ…”™½È„‘¥Í…‰±•5½‘Õ±”Ý¡•¸MQQ€ô€Å€ì(´½É‘¥¹…Éä…‘‘É•ÍÍ•µ™½É´9}=9€É•ÁÉ•Í•¹ÑÌÑ¡”¹Õµ‰•È½˜Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹Ì½¸½ÉÉ½‰½É…Ñ•ÁÉ½‘ÕÑÌìÑ¡”•µÁÑäµ]!I€…Ñ•Ý…äÙ…É¥…¹Ð¥ÌÍ•Á…É…Ñ”°Ý¥Ñ ½‰Í•ÉÙ•9}=9€ô€ÄÕ€½ÕÑÍ¥‘”Ñ¡”½É‘¥¹…Éä€À¸¸ÄÉ€É…¹”…¹Õ¹É•Í½±Ù••á…ÐÍ•µ…¹Ñ¥Ìì(´Ñ¡”ÑÝ¼M•¹…É¥½•Ù¥•Ì™¥±•Ì…É”‘¥ÍÑ¥¹ÐÉ•Ù¥Í¥½¹ÌÝ¡½Í”½µµ½¸Í•µ…¹Ñ¥Œ½¹Ñ•¹Ð½Ù•É±…ÁÌ‘•ÍÁ¥Ñ”Õ¹ÍÑ…‰±”±½…°%Ìì(´±¥Ñ•É…°M•¹…É¥½•Ù¥•Ì…Ñ¥½¸Ñ•µÁ±…Ñ•Ì…¸‰”É•¹‘•É•½¹±ä…™Ñ•È™Õ¹Ñ¥½¹…°…‘‘É•ÍÌ…¹A…É…µ•Ñ•ÈÙ…±¥‘…Ñ¥½¸ì(´…Ñ…±½Õ”ÁÉ½É…µµ¥¹œÙ…±¥‘…Ñ¥½¸¥Ì½¹Ñ•áÐµÍ•¹Í¥Ñ¥Ù”…¹…¹¹½Ð‰”É•‘Õ•Ñ¼=A8¹‘‰€ÑÉ…¹ÍÁ½ÉÐÉ…¹•Ì¸()Q¡•Í”½¹±ÕÍ¥½¹Ì‘¼¹½Ð•ÍÑ…‰±¥Í Õ¹¥Ù•ÉÍ…°ÍÕÁÁ½ÉÐ…É½ÍÌ…±°5å!=5É•±•…Í•Ì½È•Ù¥•Ì¸((ŒŒŒIÕ¹Ñ¥µ”ÅÕ•ÍÑ¥½¹ÌÍÑ¥±°½Á•¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÐéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()ðEÕ•ÍÑ¥½¸ðÙ¥‘•¹”¹••‘•ð)ð€´´´ð€´´´ð)ð]¡¥ M•¹…É¥½•Ù¥•Ì½Áä‘½•Ì5å!=5MÕ¥Ñ”½Á•¸°…¹Õ¹‘•ÈÝ¡…Ð½¹‘¥Ñ¥½¹Ìüð™¥±”µ…•ÍÌÑÉ…”°‘•½µÁ¥±•±½…‘•È°½È½¹ÑÉ½±±•™¥±”ÍÕ‰ÍÑ¥ÑÕÑ¥½¸ð)ðÉ”AÉ½É…´¥±•Ì…¹AÉ½É…µ…Ñ„½Á¥•ÌÍå¹¡É½¹¥é•½Èµ¥É…Ñ•üð¥¹ÍÑ…±±…Ñ¥½¸½ÕÁ‘…Ñ”ÑÉ…”…¹‰•™½É”½…™Ñ•È™¥¹•ÉÁÉ¥¹ÑÌð)ð!½Ü…É”‘…Ñ…‰…Í”É•ÍÕ±ÑÌ…¡•…¹¥¹Ù…±¥‘…Ñ•üðÁÉ½•ÍÌÑÉ…”½È…ÁÁ±¥…Ñ¥½¸½‘”ð)ð]¡¥ ½µÁ½¹•¹ÐÉ•Í½±Ù•ÌM•¹…É¥½•Ù¥•ÌÉ•Í½ÕÉ”­•åÌüðÉ•Í½ÕÉ”‰Õ¹‘±•Ì…¹…±°µÍ¥Ñ”…¹…±åÍ¥Ìð)ð]¡•É”…É”ÕÍ•Èµ…ÕÑ¡½É•ÁÉ½©•Ð…¹Í•¹…É¥¼É…Á¡ÌÁ•ÉÍ¥ÍÑ•üð½¹ÑÉ½±±•ÁÉ½©•Ð‘¥™˜½ÈÑÉ…•Í…Ù”½Á•É…Ñ¥½¸ð)ð!½Ü…É”™É…µ”µ…‰Í•¹ÐÍ•¹…É¥¼•Ù•¹ÑÌµ…ÁÁ•Ñ¼ÉÕ¹Ñ¥µ”¥¹ÁÕÐüðÉÕ¹Ñ¥µ”ÑÉ…”…¹•Ù•¹Ðµ‘¥ÍÁ…Ñ ½‘”ð)ð]¡…Ð•¹Õµ•É…Ñ¥½¹Ì‰…¬]¡•É•QåÁ•€°QåÁ•€°…¹=Á•É…Ñ½ÉQåÁ•€üð…ÁÁ±¥…Ñ¥½¸•¹Õ´‘•™¥¹¥Ñ¥½¹Ì½È•á¡…ÕÍÑ¥Ù”U$½ÉÕ¹Ñ¥µ”½ÉÉ•±…Ñ¥½¸ð)ð!½Ü¥ÌÑ¡”¥¹ÍÑ…±±•™¥ÉµÝ…É”É½ÜÍ•±•Ñ•Ý¡•¸Í•Ù•É…°…Ñ…±½Õ”É½ÝÌµ…Ñ üð½¹ÑÉ½±±••Ù¥”½Ù•ÉÍ¥½¸Ñ•ÍÑÌ½È±½…‘•È½‘”ð)ðÉ”%59M%=8€Ñ€…¹€Õ€Ù…±Õ•ÌÁÉ•Í•¹”™±…Ì°É…Ü½¹™¥ÕÉ…Ñ½È½‘•Ì°½È…¹½Ñ¡•È•¹½‘¥¹œüð…ÁÑÕÉ•Ì…É½ÍÌ­¹½Ý¸Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½È±…å½ÕÑÌð)ð!½Ü…É”Ñ¡”Í•Á…É…Ñ•±äÍ•±•Ñ•…‘‘É•ÍÌµÉÕ±”½±Õµ¹Ì½¹ÍÕµ•üðÑÉ…•ÅÕ•Éä•á•ÕÑ¥½¸…¹½¹ÍÕµ•È‰•¡…Ù¥½Èð((ŒŒŒ%¹Ù•ÍÑ¥…Ñ¥½¸ÉÕ±•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÐéÌÀÀÀÀÀÙ€()U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()™ÕÑÕÉ”¥µÁ±•µ•¹Ñ…Ñ¥½¸¥¹Ù•ÍÑ¥…Ñ¥½¸Í¡½Õ±™¥¹•ÉÁÉ¥¹ÐÑ¡”•á…ÐÉ•±•…Í”°µ½¹¥Ñ½È™¥±”½Á•¹Ì…¹ME1¥Ñ”ÍÑ…Ñ•µ•¹ÑÌÝ¥Ñ¡½ÕÐµ½‘¥™å¥¹œ•Ù¥‘•¹”°µ…­”½¹”½¹ÑÉ½±±•U$¡…¹”…Ð„Ñ¥µ”°‘¥™˜Á•ÉÍ¥ÍÑ•¹”‰•™½É”…¹…™Ñ•È°½ÉÉ•±…Ñ”ÑÉ…™™¥Œ‰äÑ¥µ•ÍÑ…µÀ…¹Í•µ…¹Ñ¥ŒÁ…Ñ °…¹É•½É¹•…Ñ¥Ù”•Ù¥‘•¹”¸()AÉ¥Ù…Ñ”…ÁÑÕÉ•Ì…¸ÍÕÁÁ½ÉÐ½¹±ÕÍ¥½¹Ì‰ÕÐÍ¡½Õ±¹½Ð‰”½µµ¥ÑÑ•‰•…ÕÍ”Ñ¡•äµ…ä½¹Ñ…¥¸¥¹ÍÑ…±±…Ñ¥½¸¥‘•¹Ñ¥™¥•ÉÌ…¹¹•ÑÝ½É¬‘•Ñ…¥±Ì¸((ŒŒŒ½Õµ•¹Ñ…Ñ¥½¸Á±…•µ•¹Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÐéÌÀÀÀÀÀÝ€()U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()ð¥¹‘¥¹œðM•Ñ¥½¸ð)ð€´´´ð€´´´ð)ðÍ¡…É•Ý¥É”É…µµ…ÈðmAÉ½Ñ½½±t ¸¸½ÁÉ½Ñ½½°¼¤ð)ð™Õ¹Ñ¥½¹…°]!=€Í•µ…¹Ñ¥ÌðmÕ¹Ñ¥½¹…°É•™•É•¹•t ¸¸½™Õ¹Ñ¥½¹…°¼¤ð)ð•Ù¥”…Á…‰¥±¥Ñä¡¥•É…É¡äðm•Ù¥”5½‘•±t ¸¸½‘•Ù¥”µµ½‘•°¼¤ð)ð‘¥Í½Ù•Éä…¹É•…µ‰…¬ðm¥…¹½ÍÑ¥Ít ¸¸½‘¥…¹½ÍÑ¥Ì¼¤ð)ðÍÑ…Ñ”µ¡…¹¥¹œÝ½É­™±½ÝÌðmAÉ½É…µµ¥¹t ¸¸½ÁÉ½É…µµ¥¹œ¼¤ð)ð½µÁ±•Ñ”•¹µÑ¼µ•¹Ñ…Í¬ðmAÉ…Ñ¥…°Õ¥‘•Ít ¸¸½Õ¥‘•Ì¼¤ð)ðÍ•¹…É¥¼µ•‘¥Ñ½È…Á…‰¥±¥ÑäðmM•¹…É¥¼¹¥¹•t ¸¸½Í•¹…É¥¼µ•¹¥¹”¼¤ð)ð…ÁÁ±¥…Ñ¥½¸‘…Ñ„±½…‘¥¹œ…¹ÉÕ¹Ñ¥µ”‰½Õ¹‘…Éäð5å!=5MÕ¥Ñ”%¹Ñ•É¹…±Ìð)ðµ•Ñ¡½°½µÁ•Ñ¥¹œ¡åÁ½Ñ¡•Í•Ì°…¹Õ¹É•Í½±Ù•É•Í•…É ð™ÕÑÕÉ”É•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½€Í•Ñ¥½¸ð()Q¡¥ÌÍ•Á…É…Ñ¥½¸ÁÉ•Ù•¹ÑÌ¥µÁ±•µ•¹Ñ…Ñ¥½¸•Ù¥‘•¹”™É½´‰•¥¹œÉ•Á•…Ñ•…ÌÑ¡½Õ ¥ÐÝ•É”„ÁÕ‰±¥ŒÁÉ½Ñ½½°Õ…É…¹Ñ•”¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàÔ()M½ÕÉ”Á…Ñ è¥¹Ñ•É¹…±Ì½¥¹ÍÑ…±±…Ñ¥½¸µ…¹µÍ½ÕÉ”µ±…å½ÕÐ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„è¥¹Ñ•É¹…±Í€((ŒŒ%¹ÍÑ…±±…Ñ¥½¸…¹M½ÕÉ”1…å½ÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÔéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÙ•ÉÍ¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()Q¡”…¹½¹¥…°5å!=5MÕ¥Ñ”Í½ÕÉ”Í•ÐÝ…Ì½Á¥•™É½´„Ù•ÉÍ¥½¸€Ì¸Ô¸Ìà¥¹ÍÑ…±±…Ñ¥½¸¸=É¥¥¹…°]¥¹‘½ÝÌÁ…Ñ¡Ì…É”•Ù¥‘•¹”½˜Á…­…¥¹œ±½…Ñ¥½¸ìÑ¡•ä‘¼¹½Ð‰äÑ¡•µÍ•±Ù•Ì•ÍÑ…‰±¥Í Ý¡¥ ½Áä¥Ì½Á•¹•™¥ÉÍÐ°Ý¡•Ñ¡•È‘…Ñ„¥Ì½Á¥•½ÈÍå¹¡É½¹¥é•…ÐÉÕ¹Ñ¥µ”°½ÈÝ¡•Ñ¡•È„™¥±”¥ÌÝÉ¥Ñ…‰±”‘ÕÉ¥¹œ¹½Éµ…°ÕÍ”¸((ŒŒŒAÉ•Í•ÉÙ•¥µÁ±•µ•¹Ñ…Ñ¥½¸™¥±•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÔéÌÀÀÀÀÀÉ€()ðI•Á½Í¥Ñ½Éä™¥±”ð=É¥¥¹…°¥¹ÍÑ…±±…Ñ¥½¸Á…Ñ ðM¥é”ðM!´ÈÔØð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð5!…Ñ…±½Õ”¹‘‰€ðéqAÉ½É…µ…Ñ…q1•É…¹‘É½ÕÁq5å!=5}MÕ¥Ñ•|ÀÌÀÕqM¡…É•‘q‰}5!…Ñ…±½Õ•q5!…Ñ…±½Õ”¹‘‰€ð€È°ØÈÔ°ÔÌØð˜ÁŒåÈÑ˜äààäÌÝÅŒàØÔÑŒÜÉˆÀÌÑ™ŒÀÉŒÝ……ˆÌÝ‘ŒÀäå‰‰ŒäÈÙ˜ÁŒÔàÌØÍ™”á”Õ€ð)ð=A8¹‘‰€ðéqAÉ½É…´¥±•Ì€¡ààØ¥q1•É…¹‘É½ÕÁq5å!=5}MÕ¥Ñ•|ÀÌÀÕq‘‰q=A8¹‘‰€ð€àÀ°àäØðàØÑ„ÐäÐÙˆÐÝŒÌØÜÅ„ÜÑ„ØàÐÑ•ŒÑ‘„ØÀÕ˜ÈÁˆÌÍ…ŒÄÑ˜ÐääÔäÜàÔÜÜá˜ÄÀÐÀÔÅ€ð)ðM•¹…É¥½•Ù¥•ÌµÁÉ½É…´µ™¥±•Ì¹ÍÅ±¥Ñ•€ðéqAÉ½É…´¥±•Ì€¡ààØ¥q1•É…¹‘É½ÕÁq5å!=5}MÕ¥Ñ•|ÀÌÀÕqM•¹…É¥½•Ù¥•Ì¹ÍÅ±¥Ñ•€ð€ÌÔ°àÐÀð€É”Ý™™”ÄÈàÙŒÌÈÐØÈÜÅ…•ÄØÀÄÄÙ™”ØØÐÐÀÝå”á™˜ÐÌÔäÕ˜ÔÀÄäÉ”ÝÉ…ŒàÔÔØå€ð)ðM•¹…É¥½•Ù¥•ÌµÁÉ½É…µ‘…Ñ„¹ÍÅ±¥Ñ•€ðéqAÉ½É…µ…Ñ…q1•É…¹‘É½ÕÁq5å!=5}MÕ¥Ñ•|ÀÌÀÕqM¡…É•‘q‰}M•¹…É¥½•Ù¥•ÍqM•¹…É¥½•Ù¥•Ì¹ÍÅ±¥Ñ•€ð€ÌÐ°àÄØðÍˆåˆØÜÄØÁ˜ÐØá‘‰ÌÀÄÌÐÌÔÝˆàÜÌÍŒØäÙ……ÕØÈÔÄÈäÈÐÁ‘™˜ÙˆÜäÈÈÑ™ŒÍ€ð)ðÉÕ±•Ì¹‘ˆÍ€ðéqAÉ½É…µ…Ñ…q1•É…¹‘É½ÕÁq5å!=5}MÕ¥Ñ•|ÀÌÀÕqM¡…É•‘q‰}-•å=Q¡•Éµ½Y…±¥‘…Ñ½ÉqÉÕ±•Ì¹‘ˆÍ€ð€ÌØ°àØÐð€ÈÍˆØÉ”Í‰ˆÝ„ÄÅ•‘”Í˜äÄÔØÅˆØÍ„Å……˜ÌäÐÐå‘„ÐÜÀÈÔØÈÙ„ÉŒÐÜÝ”äàÌÌÌÐÝˆÀÙ€ð)ð=Á•¹EÕ•Éä¹ÑáÑ€ðéqAÉ½É…´¥±•Ì€¡ààØ¥q1•É…¹‘É½ÕÁq5å!=5}MÕ¥Ñ•|ÀÌÀÕq‘‰q=Á•¹EÕ•Éä¹ÑáÑ€ð€Ì°ØØÄð€ÄÀÑ‰Œå™ÜàÀÜäå˜ÍˆÙ‰ˆàÕ˜ÈÔÄÁˆÅˆÀÐÈÐÜÐÝŒÌÁŒÌÄÕ˜Á„ÀÑŒäÍ”àá˜ÐÄØÍŒÄÁ€ð()Q¡”¥¹ÍÑ…±±•È¥Ì¹½ÐÉ•‘¥ÍÑÉ¥‰ÕÑ•¸%ÑÌÉ•¥ÍÑ•É•Í¥é”¥Ì€Ôää°ÐÌÜ°äÌØ‰åÑ•Ì…¹¥ÑÌM!´ÈÔØ¥Ì€ÜÀÝáÐÍÔÈäÙÅàÝÌÍÄÄÅäÈØåá		ÁÔÈÑÕàÝ	áÙÌÄÅ	€¸Q¡”É•½É‘•ÕÑ¡•¹Ñ¥½‘”Í¥¹…ÑÕÉ”¥ÌÙ…±¥…¹¥‘•¹Ñ¥™¥•Ì	Q%%9<L¹@¹¸…ÌÍ¥¹•È¸((ŒŒŒI•Á½Í¥Ñ½Éä¹…µ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÔéÌÀÀÀÀÀÍ€()AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()	½Ñ M•¹…É¥½•Ù¥•ÌÍ½ÕÉ”™¥±•ÌÝ•É”½É¥¥¹…±±ä¹…µ•M•¹…É¥½•Ù¥•Ì¹ÍÅ±¥Ñ•€¸Q¡•¥ÈÉ•Á½Í¥Ñ½Éä¹…µ•ÌÉ•½ÉÑ¡•¥È‘¥ÍÑ¥¹Ð½É¥¥¹Ì…¹ÁÉ•Ù•¹Ð½¹”™É½´½Ù•ÉÝÉ¥Ñ¥¹œÑ¡”½Ñ¡•È¸()Q¡”¹…µ•ÌÁÉ½É…´µ™¥±•Í€…¹ÁÉ½É…µ‘…Ñ…€…É”ÁÉ½Ù•¹…¹”±…‰•±Ì°¹½Ð…ÍÍ•ÉÑ•ÉÕ¹Ñ¥µ”É½±•Ì¸Q¡”AÉ½É…´¥±•Ì½Áä¥Ì±…É•È…¹½¹Ñ…¥¹Ì…‘‘¥Ñ¥½¹…°…Á…‰¥±¥ÑäÉ½ÝÌ°‰ÕÐÑ¡…Ð‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…Ð¥ÐÍÕÁ•ÉÍ•‘•Ì°µ¥É…Ñ•Ì°½ÈÕÁ‘…Ñ•ÌÑ¡”AÉ½É…µ…Ñ„½Áä¸((ŒŒŒ¥±”µ™½Éµ…Ð½‰Í•ÉÙ…Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÔéÌÀÀÀÀÀÑ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°‘½Õµ•¹Ñ…Ñ¥½¹€°Í½ÕÉ•€()±°™¥Ù”‘…Ñ…‰…Í”™¥±•Ì…É”ME1¥Ñ”‘…Ñ…‰…Í•Ì¸=Á•¹EÕ•Éä¹ÑáÑ€¥ÌÁÉ•Í•ÉÙ•…ÌUQ´àÝ¥Ñ „‰åÑ”µ½É‘•Èµ…É¬…¹I1±¥¹”•¹‘¥¹Ì¸()Q¡”…¹½¹¥…°µÍ½ÕÉ”Á½±¥äÉ•ÅÕ¥É•Ì‰åÑ”µ™½Èµ‰åÑ”ÁÉ•Í•ÉÙ…Ñ¥½¸¸¼¹½Ðè((´…‘¥¹™•ÉÉ•™½É•¥¸­•åÌÑ¼„…¹½¹¥…°‘…Ñ…‰…Í”ì(´¹½Éµ…±¥é”½ÈÑÉ…¹Í±…Ñ”ÍÑ½É•Ù…±Õ•Ì¥¸Á±…”ì(´É•Á±…”…¸½±‘•Èµ±½½­¥¹œM•¹…É¥½•Ù¥•Ì½ÁäÝ¥Ñ Ñ¡”±…É•È½Áäì(´¡…¹”±¥¹”•¹‘¥¹Ì½È•¹½‘¥¹œ¥¸=Á•¹EÕ•Éä¹ÑáÑ€ì(´ÍÑ½É”ÁÉ½©•ÐµÍÁ•¥™¥ŒÁ…­•Ð…ÁÑÕÉ•ÌÕ¹‘•ÈÍ½ÕÉ•Ì½€¸()•É¥Ù•Í¡•µ…Ì°É•±…Ñ¥½¹Í¡¥Àµ…ÁÌ°½µÁ…É¥Í½¸½ÕÑÁÕÐ°…¹¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¹Ì‰•±½¹œ¥¸‘½Õµ•¹Ñ…Ñ¥½¸½ÈÉ•ÁÉ½‘Õ¥‰±”…¹…±åÍ¥Ì½ÕÑÍ¥‘”Ñ¡”…¹½¹¥…°Í½ÕÉ”‘¥É•Ñ½Éä¸((ŒŒŒY•ÉÍ¥½¸‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÔéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()±°ÅÕ…¹Ñ¥Ñ…Ñ¥Ù”ÍÑ…Ñ•µ•¹ÑÌ¥¸Ñ¡¥ÌÍ•Ñ¥½¸…É”Í½Á•Ñ¼5å!=5MÕ¥Ñ”€Ì¸Ô¸Ìà¸±…Ñ•È¥¹ÍÑ…±±…Ñ¥½¸µ…ä½¹Ñ…¥¸‘¥™™•É•¹Ð•Ù¥”…¹™¥ÉµÝ…É”½Ù•É…”°É•Ù¥Í•µ…¹…•µ•¹ÐÍ•ÅÕ•¹•Ì½ÈÑ¥µ•È‘•™…Õ±ÑÌ°„‘¥™™•É•¹ÐM•¹…É¥½•Ù¥•ÌÍ¡•µ„½È…Á…‰¥±¥ÑäÍ•Ð°½È…‘‘¥Ñ¥½¹…°Ù…±¥‘…Ñ¥½¸‘…Ñ…‰…Í•Ì¸()]¡•¸½µÁ…É¥¹œÉ•±•…Í•Ì°¥‘•¹Ñ¥™äÉ½ÝÌ‰äÍÑ…‰±”Í•µ…¹Ñ¥Œ½¹Ñ•áÐÝ¡•É”Á½ÍÍ¥‰±”…¹…±Ý…åÌÁÉ•Í•ÉÙ”Ñ¡”Í½ÕÉ”™¥¹•ÉÁÉ¥¹Ð¸1½…°ME1¥Ñ”É½Ü%Ì…É”¹½ÐÉ•±•…Í”µÍÑ…‰±”¥‘•¹Ñ¥™¥•ÉÌÕ¹±•ÍÌ¥¹‘•Á•¹‘•¹Ð•Ù¥‘•¹”•ÍÑ…‰±¥Í¡•ÌÑ¡…ÐÍÑ…‰¥±¥Ñä¸((ŒŒŒ]¡…Ð¥¹ÍÑ…±±…Ñ¥½¸Á…Ñ¡Ì‘¼¹½ÐÁÉ½Ù”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÔéÌÀÀÀÀÀÙ€()AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()Q¡”…Ù…¥±…‰±”½ÉÁÕÌ‘½•Ì¹½Ð•ÍÑ…‰±¥Í ‘…Ñ…‰…Í”½Á•¸½É‘•È°ÕÁ‘…Ñ”½ÈÍå¹¡É½¹¥é…Ñ¥½¸‘¥É•Ñ¥½¸°…¡”¥¹Ù…±¥‘…Ñ¥½¸‰•¡…Ù¥½È°…ÁÁ±¥…Ñ¥½¸µµ½‘Õ±”½Ý¹•ÉÍ¡¥À°ÑÉ…¹Í…Ñ¥½¸‰½Õ¹‘…É¥•Ì™½ÈÁÉ½©•Ð•‘¥ÑÌ°½ÈÝ¡•É”ÕÍ•Èµ…ÕÑ¡½É•ÁÉ½©•Ð…¹Í•¹…É¥¼É…Á¡Ì…É”Á•ÉÍ¥ÍÑ•¸()Q¡•Í”É•µ…¥¸ÉÕ¹Ñ¥µ”ÅÕ•ÍÑ¥½¹Ì™½È„™ÕÑÕÉ”ÑÉ…•½È‘•½µÁ¥±•¥¹Ù•ÍÑ¥…Ñ¥½¸¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàØ()M½ÕÉ”Á…Ñ è¥¹Ñ•É¹…±Ì½±½…±¥é…Ñ¥½¸µ…¹µÁÉ•Í•¹Ñ…Ñ¥½¸¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„è¥¹Ñ•É¹…±Í€((ŒŒ1½…±¥é…Ñ¥½¸…¹AÉ•Í•¹Ñ…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàØéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()5å!=5MÕ¥Ñ”ÁÉ•Í•¹Ñ…Ñ¥½¸½µ‰¥¹•ÌÍÑ½É•…Ñ…±½Õ”Ñ•áÐ°É•Í½ÕÉ”­•åÌ°¥µÁ±•µ•¹Ñ…Ñ¥½¸µ•Ñ…‘…Ñ„°…¹ÉÕ¹Ñ¥µ”½U$‘•¥Í¥½¹Ì¸ÁÉ½Ñ½½°‘•½‘•ÈÍ¡½Õ±ÁÉ•Í•ÉÙ”Ñ¡½Í”±…å•ÉÌÉ…Ñ¡•ÈÑ¡…¸½±±…ÁÍ¥¹œÑ¡•´¥¹Ñ¼½¹”±…‰•°¸((ŒŒŒ1…‰•°±…ÍÍ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàØéÌÀÀÀÀÀÉ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°Í½ÕÉ•€()ð½¹•ÁÐðAÉ•™•ÉÉ•Í½ÕÉ”ð9½Ñ•Ìð)ð€´´´ð€´´´ð€´´´ð)ðA¡åÍ¥…°•Ù¥”‘•ÍÉ¥ÁÑ¥½¸ð9}Y%¹¹…µ•€ðÍÑ…¹‘…É5å!=5MÕ¥Ñ”µ™…¥¹œÁÉ½‘ÕÐ‘•ÍÉ¥ÁÑ¥½¸ð)ðAÉ½‘ÕÐ½‘”½M-Tð9}Y%¹½‘•€ðÁÉ½‘ÕÐ¥‘•¹Ñ¥Ñä°¹½Ð„±…¹Õ…”­•äð)ðM¡…É•¥Ñ•´‘•ÍÉ¥ÁÑ¥½¸ð9}%Q4¹‘•ÍÉ€ðÍ¡…É•…Á…‰¥±¥Ñä¥Ñ•´°¹½Ð¹••ÍÍ…É¥±ä„Õ¹¥ÅÕ”µ…É­•Ñ•ÁÉ½‘ÕÐð)ð=‰©•Ð‘•ÍÉ¥ÁÑ¥½¸ð9}-e}=	)P¹‘•ÍÉ€ð±½¥…°™Õ¹Ñ¥½¸½˜½¹”5½‘Õ±”ð)ðY¥É¥¸=‰©•Ð‘•ÍÉ¥ÁÑ¥½¸ð9}Y%I%9}=	)P¹‘•ÍÉ€ð½¹™¥ÕÉ…‰±”É½±”É•ÁÉ•Í•¹Ñ•™½È„‘¥Í…‰±•5½‘Õ±”¥¸%59M%=8€ÌÁ€ð)ð½¹™¥ÕÉ…Ñ¥½¸±…‰•°ð9}=9¹‘•ÍÉ€°‘•ÍÉ}•áÑ€°…¹É•±…Ñ•µ•Ñ…‘…Ñ„ðÁÉ½Á•ÉÑäÁÉ•Í•¹Ñ…Ñ¥½¸¥¸…Ñ…±½Õ”½¹Ñ•áÐð)ðM•¹…É¥¼…Á…‰¥±¥Ñä¹…µ”ðM•¹…É¥½•Ù¥•Ì9…µ•€™¥•±‘Ìð½µµ½¹±ä„±½…±¥é…Ñ¥½¸½É•Í½ÕÉ”­•ä°¹½Ð™¥¹…°‘¥ÍÁ±…äÑ•áÐð)ðAÉ½Ñ½½°½Á•É…Ñ¥½¸±…‰•°ð=A8¹‘ˆ¹9}=A8¹½Á•¹}±…‰•±€ð¥µÁ±•µ•¹Ñ…Ñ¥½¸½Á•É…Ñ¥½¸±…‰•°°¹½Ð„ÁÕ‰±¥ŒÁÉ½Ñ½½°¹…µ”ð()=¹”A¡åÍ¥…°•Ù¥”…¸¡…Ù”½¹”ÍÑ…¹‘…É•Ù¥”‘•ÍÉ¥ÁÑ¥½¸…¹Í•Ù•É…°5½‘Õ±”½=‰©•Ð‘•ÍÉ¥ÁÑ¥½¹Ì¸¥ÍÁ±…å¥¹œ…¸=‰©•Ð‘•ÍÉ¥ÁÑ¥½¸…ÌÑ¡”•Ù¥”¹…µ”±½Í•ÌÑ¡”ÁÉ½‘ÕÐµ±•Ù•°¥‘•¹Ñ¥Ñä¸((ŒŒŒI•Í½ÕÉ”­•åÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàØéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€()M•¹…É¥½•Ù¥•Ì­•åÌ•¹½‘”ÍÑÉÕÑÕÉ”ÍÕ …Ì™Õ¹Ñ¥½¹…°™…µ¥±ä°É½±”°=‰©•Ð°…¹½µµ…¹¸Q¡•ä…É”ÕÍ•™Õ°ÍÑ…‰±”•Ù¥‘•¹”Ý¥Ñ¡¥¸„Í½ÕÉ”É•Ù¥Í¥½¸°‰ÕÐÑ¡•¥ÈÑÉ…¹Í±…Ñ•ÍÑÉ¥¹Ì…É”¹½ÐÍÑ½É•¥¸Ñ¡”™½ÕÈ…Á…‰¥±¥ÑäÑ…‰±•Ì¸()ÁÉ•Í•¹Ñ…Ñ¥½¸±…å•ÈÍ¡½Õ±É•Ñ…¥¸Ñ¡”Í½ÕÉ”‘…Ñ…‰…Í”…¹É•Ù¥Í¥½¸°É…ÜÉ•Í½ÕÉ”­•ä°É•Í½±Ù•±½…±¥é•±…‰•°¥˜…Ù…¥±…‰±”°±½…±”°™…±±‰…¬±…‰•°°…¹Õ¹É•Í½±Ù•µ­•äÍÑ…ÑÕÌ¸()¼¹½Ð½µÁ…É”…Á…‰¥±¥Ñ¥•ÌÍ½±•±äÑ¡É½Õ ÑÉ…¹Í±…Ñ•ÍÑÉ¥¹Ì¸QÉ…¹Í±…Ñ¥½¸…¸¡…¹”Ý¡¥±”Ñ¡”Õ¹‘•É±å¥¹œÉ•Í½ÕÉ”­•äÉ•µ…¥¹ÌÑ¡”Í…µ”°…¹½¹”­•ä…¸½ÕÈ¥¸µÕ±Ñ¥Á±”…Ñ•½ÉäÁ…Ñ¡Ì¸((ŒŒŒU$¹Õµ‰•É¥¹œ…¹Í±½Ñ€Á½Í¥Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàØéÌÀÀÀÀÀÑ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()5å!=5MÕ¥Ñ”…¸¡¥‘”Í±½Ñ€Á½Í¥Ñ¥½¹Ì½ÈÉ•¹Õµ‰•ÈÙ¥Í¥‰±”5½‘Õ±•Ì¸Q¡”ÁÉ•Í•¹Ñ…Ñ¥½¸±…å•ÈµÕÍÐ­••ÀÑ¡”ÁÉ½Ñ½½°M1=Q€°…Ñ…±½Õ”Á±…•µ•¹Ð°U$µÙ¥Í¥‰±”5½‘Õ±”¹Õµ‰•È½È¹…µ”°…¹¡¥‘‘•¸½…‰Í•¹ÐÍÑ…Ñ”…ÌÍ•Á…É…Ñ”™¥•±‘Ì¸()9•Ù•ÈÉ•ÝÉ¥Ñ”Ñ¡”•Ù¥”µ±½…°Í±½Ñ€Ñ¼µ…Ñ Ñ¡”U$¸((ŒŒŒY¥Í¥‰¥±¥Ñä…¹•‘¥Ñ…‰¥±¥Ñä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàØéÌÀÀÀÀÀÕ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()…Ñ…±½Õ”µ•Ñ…‘…Ñ„ÍÕ …ÌÙ¥Í¥‰±•€°¡¥‘‘•¹€°É•…‘}½¹±å€°™¥á•‘}­½€°…¹½¹‘¥Ñ¥½¹Ì½¹ÑÉ¥‰ÕÑ•ÌÑ¼U$‰•¡…Ù¥½È°‰ÕÐ¹¼½¹”™±…œ¥Ì„½µÁ±•Ñ”ÁÉ•Í•¹Ñ…Ñ¥½¸ÉÕ±”¸()™¥á•=‰©•Ð…¸ÍÑ¥±°•áÁ½Í”•‘¥Ñ…‰±”½¹™¥ÕÉ…Ñ¥½¸¸¡¥‘‘•¸ÁÉ½Á•ÉÑä…¸Á…ÉÑ¥¥Á…Ñ”¥¸½¹Ù•ÉÍ¥½¹Ì¸¸=‰©•Ð…±Ñ•É¹…Ñ¥Ù”…¸•á¥ÍÐ¥¸Ñ¡”…Ñ…±½Õ”‰ÕÐ‰”ÍÕÁÁÉ•ÍÍ•‰ä„Í±½Ñ€½¹‘¥Ñ¥½¸¸Í±½Ñ€…¸•á¥ÍÐÝ¡¥±”‰•¥¹œ…‰Í•¹Ð™É½´„Á…ÉÑ¥Õ±…ÈU$Ù¥•Ü¸()UÍ”½‰Í•ÉÙ•U$‰•¡…Ù¥½È…ÌÁÉ•Í•¹Ñ…Ñ¥½¸•Ù¥‘•¹”…¹…Ñ…±½Õ”ÍÑÉÕÑÕÉ•Ì…Ì…Á…‰¥±¥Ñä•Ù¥‘•¹”¸¼¹½Ð¥¹™•ÈÝ¥É”•¹½‘¥¹œ™É½´„±…‰•°½ÈÝ¥‘•Ð…±½¹”¸((ŒŒŒQ•Éµ¥¹½±½ä¹½Éµ…±¥é…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàØéÌÀÀÀÀÀÙ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()I•Á½Í¥Ñ½ÉäÁÉ½Í”ÕÍ•Ì€¨©A¡åÍ¥…°•Ù¥”¨¨°€¨©5½‘Õ±”¨¨°€¨©Í±½Ñ€¨¨°€¨©=‰©•Ð¨¨°€¨©½¹™¥ÕÉ…Ñ¥½¸¨¨°…¹€¨©Y¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸¨¨¸…Ñ…‰…Í”¹…µ•ÌÍÕ …Ì-e=€°­¼Í±½Ñ€°…¹¥‘}­•å}½‰©•Ñ€…É”É•Ñ…¥¹•Ý¡•¸ÅÕ½Ñ¥¹œ™¥•±‘Ì°‰ÕÐ‘¼¹½ÐÉ•Á±…”É•…‘•Èµ™…¥¹œÑ•Éµ¥¹½±½ä¸((ŒŒŒU¹­¹½Ý¸±½…±¥é…Ñ¥½¸µ•¡…¹¥Í´()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàØéÌÀÀÀÀÀÝ€()Q¡”½ÉÁÕÌ•ÍÑ…‰±¥Í¡•ÌÍÑ½É•Ñ•áÐ…¹É•Í½ÕÉ”µ­•äÕÍ…”‰ÕÐ‘½•Ì¹½ÐÁÉ•Í•ÉÙ”Ñ¡”½µÁ±•Ñ”É•Í½ÕÉ”‰Õ¹‘±”½È…ÁÁ±¥…Ñ¥½¸½‘”Ñ¡…ÐÉ•Í½±Ù•Ì•Ù•Éä­•ä¸%ÐÑ¡•É•™½É”‘½•Ì¹½Ð•ÍÑ…‰±¥Í ™…±±‰…¬±½…±”½É‘•È°µ¥ÍÍ¥¹œµ­•ä‰•¡…Ù¥½È°ÉÕ¹Ñ¥µ”Õ±ÑÕÉ”Í•±•Ñ¥½¸°½È™½Éµ…ÑÑ¥¹œÉÕ±•Ì™½È½µÁ½Í•±…‰•±Ì¸()½Õµ•¹ÐÉ…Ü­•åÌÝ¡•¹•Ù•ÈÑ¡”™¥¹…°±½…±¥é•ÍÑÉ¥¹œ…¹¹½Ð‰”É•ÁÉ½‘Õ•¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàÜ()M½ÕÉ”Á…Ñ è¥¹Ñ•É¹…±Ì½½Á•¹Ý•‰¹•ÐµÉ•¥ÍÑÉäµ…¹µÍÑ…Ñ”µµ…¡¥¹•Ì¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„è¥¹Ñ•É¹…±Í€((ŒŒ=Á•¹]•‰9•ÐI•¥ÍÑÉä…¹MÑ…Ñ”5…¡¥¹•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÜéÌÀÀÀÀÀÅ€()=A8¹‘‰€¥Ì5å!=5MÕ¥Ñ—ŠeÌ¥µÁ±•µ•¹Ñ…Ñ¥½¸É•¥ÍÑÉä™½È=Á•¹]•‰9•ÐÍåÍÑ•µÌ…¹µ…¹…•µ•¹ÐÝ½É­™±½ÝÌ¸%ÐÉ•ÁÉ•Í•¹ÑÌ™É…µ”Ñ•µÁ±…Ñ•Ì…¹Ñ¡•¥È½µÁ½Í¥Ñ¥½¸ì¥Ð¥Ì¹½Ð„½µÁ±•Ñ”½Áä½˜Ñ¡”ÁÕ‰±¥Œ™Õ¹Ñ¥½¹…°ÁÉ½Ñ½½°¸((ŒŒŒI•¥ÍÑÉä±…å•ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÜéÌÀÀÀÀÀÉ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()ð1…å•ÈðAÉ¥¹¥Á…°Ñ…‰±•ÌðI½±”ð)ð€´´´ð€´´´ð€´´´ð)ðMåÍÑ•µÌð9}MeMQ5€ð™Õ¹Ñ¥½¹…°¹…µ•ÍÁ…”±…‰•°°™Õ¹Ñ¥½¹…°]!=€°‘¥…¹½ÍÑ¥Œ]!=€°…¹µ…¹…•™±…œð)ðMåÍÑ•´½Á•É…Ñ¥½¹ÌðM}=A9}MeMQ5€°9}=A9€ð½¹É•Ñ”™É…µ”Ñ•µÁ±…Ñ•Ì…ÍÍ½¥…Ñ•Ý¥Ñ Í•±•Ñ•ÍåÍÑ•µÌð)ðA…É…µ•Ñ•ÉÌðM}=A9}AI5€°9}=A9}AI5€ðÁ±…•¡½±‘•È‘•ÍÉ¥ÁÑ¥½¹Ì…¹ÑÉ…¹ÍÁ½ÉÐ½¹ÍÑÉ…¥¹ÑÌð)ð‘‘É•ÍÍ¥¹œðM}MeMQ5}IMM}IU1€°9}IMM}IU1€ðÍåÍÑ•´µÍÁ•¥™¥ŒY¥ÉÑÕ…°…¹…‘Ù…¹•…‘‘É•ÍÌÉ…µµ…ÉÌð)ðM•¹…É¥½Ìð9}M9I%=€°M}M9I%=}MEU9€ð¹…µ•¡¥ µ±•Ù•°½Á•É…Ñ¥½¹Ì½µÁ½Í•™É½´Í•ÅÕ•¹•Ìð)ðM•ÅÕ•¹•Ìð9}MEU9€°M}=A9}MEU9€ð½É‘•É•™É…µ•Ì°‘¥É•Ñ¥½¸µÍ•¹Í¥Ñ¥Ù”Ù…É¥…¹ÑÌ°É•Á•Ñ¥Ñ¥½¸°…¹ÑÉ…¹Í¥Ñ¥½¸µ•Ñ…‘…Ñ„ð)ðQ¥µ¥¹œðM}Q%5=UQ}=A9}MEU9€°9}Q%5=UQ€ðÑ¥µ•ÉÌ°‘•™…Õ±ÑÌ°ÍÑ…ÉÐ½ÍÑ½À…Ñ¥½¹Ì°…¹Ñ¥µ•½ÕÐÑÉ…¹Í¥Ñ¥½¹Ìð()¸9}MeMQ5€É½ÜÁÉ½Ù•Ì¹…µ•ÍÁ…”­¹½Ý±•‘”¸%Ð‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…Ð9}=A9€½¹Ñ…¥¹Ì•Ù•Éä™Õ¹Ñ¥½¹…°½µµ…¹™½ÈÑ¡…Ð]!=€¸((…m=A8¹‘ˆÍåÍÑ•µÌ°™É…µ•Ì°…¹Ý½É­™±½ÜÉ•¥ÍÑÉåt ¸¸½…ÍÍ•ÑÌ½‘¥…É…µÌ½½Á•¹Ý•‰¹•ÐµÉ•¥ÍÑÉä¹ÍÙœ¤()Q¡”…ÍÍ½¥…Ñ¥½¸Ñ…‰±•Ì…ÉÉä½É‘•É¥¹œ°É•Á•Ñ¥Ñ¥½¸°‘¥É•Ñ¥½¸µÍ•¹Í¥Ñ¥Ù”½µÁ½Í¥Ñ¥½¸°…¹Ñ¥µ•½ÕÐ½¹Ñ•áÐ¸Q¡½Í”ÁÉ½Á•ÉÑ¥•Ì‘¼¹½Ð‰•±½¹œÑ¼Ñ¡”™É…µ”Ñ•µÁ±…Ñ”…±½¹”¸((ŒŒŒMÑ…Ñ”µµ…¡¥¹”…ÍÍ•µ‰±ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÜéÌÀÀÀÀÀÍ€()AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()µ…¹…•µ•¹Ð½Á•É…Ñ¥½¸¥ÌÉ•Í½±Ù•¥¸ÑÝ¼ÍÑ…•Ìè((Ä¸Í•±•Ð…¸9}M9I%=€…¹½É‘•È¥ÑÌÍ•ÅÕ•¹•ÌÑ¡É½Õ M}M9I%=}MEU9¹Í•ÅÕ•¹•}½É‘•É€ì(È¸™½È•… Í•±•Ñ•9}MEU9€°½É‘•È¥ÑÌ™É…µ”‘•™¥¹¥Ñ¥½¹ÌÑ¡É½Õ M}=A9}MEU9¹½Á•¹}½É‘•É€¸()M•ÅÕ•¹”µ•Ñ…‘…Ñ„½¹ÑÉ½±ÌÝ¡•Ñ¡•È„™É…µ”¥Ìµ…¹‘…Ñ½Éä½ÈÉ•Á•…Ñ•°¥ÑÌ‘¥É•Ñ¥½¸µÍ•¹Í¥Ñ¥Ù”É•¥ÍÑÉäÉ½Ü°…¹ÍÑ…Ñ”¡…¹•Ì™½È9-€°ÍÑÉÕÑÕÉ••ÉÉ½ÉÌ°…¹Ñ¥µ•½ÕÑÌ¸()É•Á•…Ñ•Í•ÅÕ•¹”…ÍÍ½¥…Ñ¥½¸Á•Éµ¥ÑÌ…ÁÁ±¥…Ñ¥½¸µ±•Ù•°É•Á•Ñ¥Ñ¥½¸‰ÕÐ‘½•Ì¹½Ð•¹½‘”Ñ¡”¥Ñ•É…Ñ¥½¸½Õ¹Ð¸1¥­•Ý¥Í”°„É•Á•…Ñ•™É…µ”…¸½±±•Ð½È•µ¥ÐµÕ±Ñ¥Á±”É½ÝÌ°‰ÕÐÑ¡”‘…Ñ…‰…Í”‘½•Ì¹½Ð‘•Ñ•Éµ¥¹”¡½Üµ…¹ä„Á…ÉÑ¥Õ±…È•Ù¥”ÍÕÁÁ½ÉÑÌ¸((ŒŒŒÉ…µ”É•½É‘Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÜéÌÀÀÀÀÀÑ€()9}=A8¹½Á•¹}ÍÑÉ¥¹€ÍÑ½É•ÌÁ…É…µ•Ñ•É¥é•™É…µ•ÌÍÕ …Ì‘¥…¹½ÍÑ¥Œ%59M%=8€ÌÁ€°ÁÉ½É…µµ¥¹œ%59M%=8€ÌÕ€°…¹Í•ÍÍ¥½¸µ½¹ÑÉ½°]!Q€Ù…±Õ•Ì¸I•±…Ñ•™¥•±‘Ì±…ÍÍ¥™ä…‘‘É•ÍÌ…¹Á…É…µ•Ñ•ÈÁÉ•Í•¹”°‘¥É•Ñ¥½¸½ÑåÁ”°‘¥…¹½ÍÑ¥ŒÕÍ”°•ÉÉ½ÉÌ°…¹=‰©•ÐµÁÉ½É…µµ¥¹œÕÍ”¸()Q¡”Í…µ”Ñ•áÑÕ…°™É…µ”Í¡…Á”…¸…ÁÁ•…È¥¸‘¥™™•É•¹Ð‘¥É•Ñ¥½¹Ì½ÈÝ½É­™±½Ü½¹Ñ•áÑÌ¸AÉ½É…µµ•È…¹•Ù¥”…‰½ÉÑÌ°™½È•á…µÁ±”°Í¡…É”„Ý¥É”™½É´‰ÕÐ…É”‘¥ÍÑ¥¹ÐÉ•¥ÍÑÉäÉ½ÝÌ¸±Ý…åÌÉ•Ñ…¥¸Ñ¡”9}=A9€É½Ü°‘¥É•Ñ¥½¸°…Ñ¥Ù”Í•¹…É¥¼…¹Í•ÅÕ•¹”°ÕÉÉ•¹Ð•Ù¥”Í•±•Ñ½È°…¹±…ÍÐ½ÕÑÍÑ…¹‘¥¹œ½µµ…¹¸()Q¡”Ý¥É”ÁÉ½Ñ½½°¡…Ì¹¼ÑÉ…¹Í…Ñ¥½¸¥‘•¹Ñ¥™¥•ÈÑ¡…Ð…¸É•½Ù•ÈÑ¡¥Ì½¹Ñ•áÐ…™Ñ•È…µ‰¥Õ½ÕÌÁ¥Á•±¥¹¥¹œ¸((ŒŒŒ=Á•¹EÕ•Éä¹ÑáÑ€…Ì„‘…Ñ„µ…•ÍÌ½¹ÑÉ…Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÜéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°ÍÍ€()=Á•¹EÕ•Éä¹ÑáÑ€‘•™¥¹•Ì¹…µ•ME0ÍÑ…Ñ•µ•¹ÑÌ™½ÈÍ•±•Ñ•É•¥ÍÑÉäÉ•…‘Ìè()ðEÕ•Éä­•äð…Ñ„±½…‘•ð)ð€´´´ð€´´´ð)ðÍåÍÑ•µ¥ÑEÕ•Éå€ð…±°ÍåÍÑ•µÌ½É‘•É•‰ä¥¹Ñ•É¹…°ÍåÍÑ•´%ð)ðÍåÍÑ•µ…‘‘É•ÍÍÉÕ±•¥ÑEÕ•Éå€ðÍåÍÑ•´½…‘‘É•ÍÌµÉÕ±”…ÍÍ½¥…Ñ¥½¹Ì…¹ÉÕ±”™¥•±‘Ìð)ð½Á•¹™É…µ•ÉÉ¥ÑEÕ•Éå€ð™É…µ•Ìµ…É­•…Ì•ÉÉ½ÉÌð)ð½Á•¹™É…µ•…‰½ÉÑ½¹™EÕ•Éå1¥ÍÑ€ðÁÉ½É…µµ•È…‰½ÉÐÉ½ÝÌð)ð½Á•¹™É…µ•…Ñ•Ý…å½¹¹•Ñ¥½¹EÕ•Éå1¥ÍÑ€ðÍ•±•Ñ•…Ñ•Ý…äµ½¹¹•Ñ¥½¸™É…µ•Ìð)ð½Á•¹™É…µ•ÍÍ‰ÕÍEÕ•Éå€ðÑ¡”MLµ‰ÕÌ™É…µ”ð)ðÑ¥µ•½ÕÑÍÍ‰ÕÍEÕ•Éå€ðMLµ‰ÕÌÑ¥µ•½ÕÐ‘•™…Õ±Ðð)ðÍ•¹…É¥½EÕ•Éå€ðÍ•¹…É¥¼¥‘•¹Ñ¥Ñä…¹ÑåÁ”‰ä±…‰•°ð)ðÍ•¹Í•ÄÅEÕ•Éå€ð½É‘•É•Í•ÅÕ•¹”½µÁ½Í¥Ñ¥½¸ð)ð½Á•¹Í•ÄÅEÕ•Éå€ð½É‘•É•™É…µ”½µÁ½Í¥Ñ¥½¸Á±ÕÌÍ•±•Ñ•Á…É…µ•Ñ•Èµ•Ñ…‘…Ñ„ð)ð½Á•¹Ñ¥µ•½ÕÑEÕ•Éå€ðÑ¥µ•½ÕÑÌ…¹ÑÉ…¹Í¥Ñ¥½¹Ì™½È„Í•ÅÕ•¹”ð()Q¡”™¥±”É•½É‘ÌÑ¡”½±Õµ¹Ì…¹½É‘•É¥¹œ5å!=5MÕ¥Ñ”¥¹Ñ•¹‘•Ñ¼É•ÅÕ•ÍÐ¸%Ð‘½•Ì¹½ÐÁÉ½Ù”Ý¡•¸•… ÅÕ•ÉäÉÕ¹Ì°¡½ÜÉ•ÍÕ±ÑÌ…É”…¡•°½È¡½Ü…ÁÁ±¥…Ñ¥½¸±…ÍÍ•Ì¥¹Ñ•ÉÁÉ•Ð•Ù•Éä™¥•±¸((ŒŒŒ%¹½µÁ±•Ñ•¹•ÍÌÁÉ•Í•ÉÙ•¥¸Ñ¡”Í½ÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÜéÌÀÀÀÀÀÙ€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡”™¥±”¥ÑÍ•±˜É•½É‘ÌÕ¹™¥¹¥Í¡•Ý½É¬è((´…¸%Ñ…±¥…¸¹½Ñ”Í…åÌÑ¡”Í•ÅÕ•¹”µ½¹±äÁ…ÉÐÍÑ¥±°¡…Ñ¼‰”‘•™¥¹•ì(´„Í•½¹¹½Ñ”Í…åÌÅÕ•É¥•Ì¹••‘•™½ÈÍ•¹…É¥¼ÑÉ…Ù•ÉÍ…°Ý•É”ÍÑ¥±°µ¥ÍÍ¥¹œì(´½Á•¹Á…É…µÍEÕ•Éå€¥Ì±¥Ñ•É…±±äQ==€ì(´Ñ¡”½Á•É…Ñ¥½¸µÍÁ•¥™¥Œ…‘‘É•ÍÌµÉÕ±”ÅÕ•Éä¥Ì½µµ•¹Ñ•½ÕÐ¸()Q¡•Í”…É”Í½ÕÉ”™…ÑÌ¸=Á•¹EÕ•Éä¹ÑáÑ€…¹¹½Ð‰”ÑÉ•…Ñ•…Ì„½µÁ±•Ñ”Í¡•µ„µ…•ÍÌÍÁ•¥™¥…Ñ¥½¸¸()Q¡”ÁÉ•Í•ÉÙ•ÍåÍÑ•µ…‘‘É•ÍÍÉÕ±•¥ÑEÕ•Éå€Í•±•ÑÌ…È¹…‘‘É•ÍÍ}ÉÕ±•}…‘Ù€…¹…È¹±•Ù•±|É}ÉÕ±•€…ÌÍ•Á…É…Ñ”½µµ„µ‘•±¥µ¥Ñ•½±Õµ¹Ì¸¸•…É±¥•ÈÉ•Ù¥•Ü…ÑÑÉ¥‰ÕÑ•„‰¥ÑÝ¥Í”•áÁÉ•ÍÍ¥½¸Ñ¼Ñ¡¥Ì™¥±”ì‘¥É•Ð¥¹ÍÁ•Ñ¥½¸½˜Ñ¡”™¥¹•ÉÁÉ¥¹Ñ•Í½ÕÉ”‘¥ÍÁÉ½Ù•Ñ¡…Ð…ÑÑÉ¥‰ÕÑ¥½¸¸EÕ•Éä•á•ÕÑ¥½¸…¹½¹ÍÕµ•È‰•¡…Ù¥½ÈÍÑ¥±°É•ÅÕ¥É”ÉÕ¹Ñ¥µ”•Ù¥‘•¹”¸Q¡”½ÉÉ•Ñ¥½¸¥ÌÉ•½É‘•¥¸Ñ¡”mI•Ù¥•Ü1•‘•Ét ¸¸½ÁÉ½©•Ð½É•Ù¥•Ü½•Øµ•ÍœµÉ•Ù¥•Üµ±•‘•È¹µÀÌµÁÉ½Ø´ÀÀÄ´´µ¥¹½ÉÉ•Ðµ½Á•¹ÅÕ•ÉäµÍ½ÕÉ”µ…ÑÑÉ¥‰ÕÑ¥½¸¤¸((ŒŒŒIÕ¹Ñ¥µ”…±½É¥Ñ¡´()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàÜéÌÀÀÀÀÀÝ€()AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()Í…™”É•¥µÁ±•µ•¹Ñ…Ñ¥½¸Í¡½Õ±Í•±•ÐÑ¡”ÍåÍÑ•´…¹µ…¹…•µ•¹Ð™…µ¥±äÝ¥Ñ¡½ÕÐ¹Õµ•É¥…±±ä©½¥¹¥¹œ…¹½Ñ¡•È‘…Ñ…‰…Í—ŠeÌÍåÍÑ•´%ìÉ•Í½±Ù”Ñ¡”Í•¹…É¥¼‰ä±…‰•°ìÁÉ•Í•ÉÙ”Í•ÅÕ•¹”½™É…µ”½É‘•È…¹É•Á•Ñ¥Ñ¥½¸ì‰¥¹½¹±ä•ÍÑ…‰±¥Í¡•Á…É…µ•Ñ•ÉÌìÉ•…Ñ”Ñ¥µ•ÉÌ™É½´Ñ¥µ•½ÕÐ…ÍÍ½¥…Ñ¥½¹ÌìÍ•É¥…±¥é”…µ‰¥Õ½ÕÌÉ•ÅÕ•ÍÑÌì…¹±…ÍÍ¥™äÑ•Éµ¥¹…°°•ÉÉ½È°9-€°…¹Ñ¥µ•½ÕÐÑÉ…¹Í¥Ñ¥½¹ÌÍ•Á…É…Ñ•±ä¸()Q¡”½¹É•Ñ”‘¥…¹½ÍÑ¥Œ…¹ÁÉ½É…µµ¥¹œÍÑ…Ñ”µ…¡¥¹•Ì…É”‘½Õµ•¹Ñ•¥¸m¥…¹½ÍÑ¥Ít ¸¸½‘¥…¹½ÍÑ¥Ì¼¤…¹mAÉ½É…µµ¥¹t ¸¸½ÁÉ½É…µµ¥¹œ¼¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàà()M½ÕÉ”Á…Ñ è¥¹Ñ•É¹…±Ì½Í•¹…É¥¼µ…Á…‰¥±¥Ñäµ±½…‘¥¹œ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„è¥¹Ñ•É¹…±Í€((ŒŒM•¹…É¥¼…Á…‰¥±¥Ñä1½…‘¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀààéÌÀÀÀÀÀÅ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()Q¡”ÑÝ¼M•¹…É¥½•Ù¥•Ì‘…Ñ…‰…Í•Ì…É”½µÁ…Ð…Á…‰¥±¥Ñä…Ñ…±½Õ•Ì™½ÈÑ¡”5å!=5MÕ¥Ñ”Í•¹…É¥¼•‘¥Ñ½È¸Q¡•ä…É”¹½Ð¥¹Ù•¹Ñ½É¥•Ì½˜¥¹ÍÑ…±±••Ù¥•Ì…¹‘¼¹½Ð½¹Ñ…¥¸Ñ¡”½µÁ±•Ñ”É…Á ½˜„ÕÍ•Èµ…ÕÑ¡½É•Í•¹…É¥¼¸((ŒŒŒQÝ¼Í½ÕÉ”É•Ù¥Í¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀààéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()ðM½ÕÉ”ð=‰©•ÐMåÍÑ•µÌð•Ù¥”=‰©•ÑÌð½µµ…¹‘ÌðA…É…µ•Ñ•ÉÌðM¡•µ„‘¥ÍÑ¥¹Ñ¥½¸ð)ð€´´´ð€´´´ð€´´´ð€´´´ð€´´´ð€´´´ð)ðAÉ½É…´¥±•Ì½Áäð€Èäð€ÐÐð€ÄÔÜð€ÐÈð¥¹±Õ‘•Ì=‰©•ÑMåÍÑ•µÌ¹…µ¥±å%‘€ð)ðAÉ½É…µ…Ñ„½Áäð€ÈÜð€ÐÈð€ÄÔÄð€ÐÀð¹¼…µ¥±å%‘€ð()Q¡”½µµ½¸Í•µ…¹Ñ¥Œ½¹Ñ•¹Ð½˜Ñ¡”AÉ½É…µ…Ñ„½Áä¥Ì…¸•á…ÐÍÕ‰Í•Ð½˜Ñ¡”AÉ½É…´¥±•Ì½ÁäÝ¡•¸½µÁ…É•‰äÑ¡”½µÁ±•Ñ”¡¥•É…É¡ä…¹¹½¸µ±½…°™¥•±‘Ì¸1½…°É½Ü%Ì‘¥Ù•É”…™Ñ•È…‘‘•É½ÝÌ…¹µÕÍÐ¹½Ð‰”ÕÍ•…ÌÉ½ÍÌµ™¥±”¥‘•¹Ñ¥Ñ¥•Ì¸()Q¡”±…É•ÈÉ•Ù¥Í¥½¸…‘‘ÌÑÝ¼Y¥ÉÑÕ…°-•ä…É=‰©•ÐMåÍÑ•µÌ°ÑÝ¼•Ù¥”=‰©•ÑÌ°™½ÕÈY¥ÉÑÕ…°-•ä…É•Ù•¹Ð½µµ…¹‘Ì°ÑÝ¼Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°…Ñ¥½¸½µµ…¹‘Ì°…¹ÑÝ¼A…É…µ•Ñ•ÉÌ‰•±½¹¥¹œÑ¼Ñ¡½Í”…Ñ¥½¹Ì¸Q¡¥Ì‘•±Ñ„‘½•Ì¹½Ð•ÍÑ…‰±¥Í ÉÕ¹Ñ¥µ”ÁÉ••‘•¹”¸((ŒŒŒ•±…É•¡¥•É…É¡ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀààéÌÀÀÀÀÀÍ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°Í½ÕÉ•€()Q¡”™¥±•Ì‘•±…É”Ñ¡¥Ì¡¥•É…É¡äè((¨©=‰©•ÐMåÍÑ•´ƒŠH•Ù¥”=‰©•ÐƒŠH½µµ…¹ƒŠHA…É…µ•Ñ•È¨¨()ðI•±…Ñ¥½¹Í¡¥Àð•±…É•™½É•¥¸­•äð)ð€´´´ð€´´´ð)ð•Ù¥”=‰©•ÐÑ¼=‰©•ÐMåÍÑ•´ð•Ù¥•=‰©•ÑÌ¹=‰©•ÑMåÍÑ•µ}%ƒŠH=‰©•ÑMåÍÑ•µÌ¹%‘€ð)ð½µµ…¹Ñ¼•Ù¥”=‰©•Ðð½µµ…¹‘Ì¹•Ù¥•=‰©•Ñ}%ƒŠH•Ù¥•=‰©•ÑÌ¹%‘€ð)ðA…É…µ•Ñ•ÈÑ¼½µµ…¹ðA…É…µ•Ñ•ÉÌ¹½µµ…¹‘}%ƒŠH½µµ…¹‘Ì¹%‘€ð((…mM•¹…É¥½•Ù¥•Ì…Á…‰¥±¥Ñä¡¥•É…É¡åt ¸¸½…ÍÍ•ÑÌ½‘¥…É…µÌ½Í•¹…É¥¼µ…Á…‰¥±¥Ñä¹ÍÙœ¤()UÍ”±½…°É½ÜÁÉ¥µ…Éä­•åÌ½¹±ä¥¹Í¥‘”½¹”Í½ÕÉ”™¥±”¸()=‰©•Ñ%‘€°=‰©•Ñ5…Ñ¡¥¹%‘€°½µµ…¹‘%‘€°…¹½µµ…¹‘5…Ñ¡¥¹%‘€…É”Í•¹…É¥¼µ•¹¥¹”¥‘•¹Ñ¥™¥•ÉÌ¸Q¡•ä…É”¹½Ð…Ñ…±½Õ”=‰©•Ð¹Õµ‰•ÉÌ½È=Á•¹]•‰9•Ð™¥•±‘ÌÝ¥Ñ¡½ÕÐ„Í•Á…É…Ñ•±ä•ÍÑ…‰±¥Í¡•½ÉÉ•±…Ñ¥½¸¸((ŒŒŒI•Í½ÕÉ”µ­•äµ‘É¥Ù•¸ÁÉ•Í•¹Ñ…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀààéÌÀÀÀÀÀÑ€()AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()9…µ•ÌÍÕ …Ìµ¥¹¥M•¹…É¥½MÕ¥Ñ”¹…ÕÑ½µ…Ñ¥½¸¹…Ñ¥½¹€…É”±½…±¥é…Ñ¥½¸½É•Í½ÕÉ”­•åÌ¸Q¡•ä…ÉÉäÕÍ•™Õ°¥µÁ±•µ•¹Ñ…Ñ¥½¸Í•µ…¹Ñ¥Ì°¥¹±Õ‘¥¹œ™Õ¹Ñ¥½¹…°™…µ¥±ä…¹•‘¥Ñ½ÈÉ½±”°‰ÕÐÑ¡•ä…É”¹½Ð™¥¹…°U$ÍÑÉ¥¹Ì¸()½¹ÍÕµ•ÈÍ¡½Õ±É•Ñ…¥¸‰½Ñ Ñ¡”É…Ü­•ä…¹…¹äÉ•Í½±Ù•‘¥ÍÁ±…ä±…‰•°¸9•Ù•ÈÕÍ”„ÑÉ…¹Í±…Ñ•±…‰•°…Ì„‘…Ñ…‰…Í”¥‘•¹Ñ¥Ñä¸((ŒŒŒ½µµ…¹±…ÍÍ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀààéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()ð±…ÍÌðÙ¥‘•¹”ðM…™”ÑÉ•…Ñµ•¹Ðð)ð€´´´ð€´´´ð€´´´ð)ð1¥Ñ•É…°™É…µ”ðÉ…µ•€Á…ÉÍ•Ì…Ì=Á•¹]•‰9•Ð…¹…É••ÌÝ¥Ñ ¡¥=Á•¹€ðÙ…±¥‘…Ñ”…‘‘É•ÍÌ…¹A…É…µ•Ñ•ÉÌ°É•¹‘•È°Ñ¡•¸É•Á…ÉÍ”ð)ðMåµ‰½±¥Œ™É…µ”ð¹½¸µ¹Õ±°Ñ•áÐÑ¡…Ð¥Ì¹½Ð„±¥Ñ•É…°™É…µ”ðÉ•ÅÕ¥É”…¸…ÁÁ±¥…Ñ¥½¸µÍÁ•¥™¥Œµ…ÁÁ¥¹œð)ðÉ…µ”µ…‰Í•¹ÐðÉ…µ”%L9U11€ðÉ•Ñ…¥¸•‘¥Ñ½È…Á…‰¥±¥Ñäì‘¼¹½Ð¥¹Ù•¹Ð…¸¥¹½µ¥¹œ™É…µ”ð()%¸Ñ¡”±…É•ÈÉ•Ù¥Í¥½¸°€ÔÜ½µµ…¹‘Ì¡…Ù”±¥Ñ•É…°=Á•¹]•‰9•ÐµÍ¡…Á•Ñ•µÁ±…Ñ•Ì°™¥Ù”¡…Ù”Íåµ‰½±¥ŒÑ•áÐ°…¹€äÔ¡…Ù”¹¼ÍÑ½É•™É…µ”¸5½ÍÐ•Ù•¹ÑÌ…¹½¹‘¥Ñ¥½¹Ì…É”™É…µ”µ…‰Í•¹Ðì…Ñ¥½¸É½ÝÌµ½É”½™Ñ•¸½¹Ñ…¥¸É•¹‘•É…‰±”™É…µ•Ì¸()Q¡¥ÌÁÉ½Ù•ÌÑ¡…ÐM•¹…É¥½•Ù¥•Ì…±½¹”¥Ì¹½ÐÑ¡”¥¹½µ¥¹œµ•Ù•¹Ðµ…Ñ¡•È½ÈÑ¡”™Õ±°ÉÕ¹Ñ¥µ”•¹¥¹”¸((ŒŒŒ…Á…‰¥±¥ÑäÉ•Í½±ÕÑ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀààéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()Í…™”±½…‘•ÈÍ•±•ÑÌ½¹”Í½ÕÉ”É•Ù¥Í¥½¸•áÁ±¥¥Ñ±äìÁÉ•Í•ÉÙ•Ì…Ñ•½É¥•Ì…¹µ…Ñ¡¥¹œ¥‘•¹Ñ¥™¥•ÉÌì±½…‘Ì…±°½µµ…¹‘Ì…¹A…É…µ•Ñ•ÉÌì±…ÍÍ¥™¥•Ì±¥Ñ•É…°°Íåµ‰½±¥Œ°…¹™É…µ”µ…‰Í•¹ÐÉ½ÝÌìÙ…±¥‘…Ñ•Ì±¥Ñ•É…°]!=€Ù…±Õ•Ì……¥¹ÍÐ¡¥=Á•¹€ì¥¹Ñ•ÉÁÉ•ÑÌ]!I€Õ¹‘•ÈÑ¡”™Õ¹Ñ¥½¹…°]!=€ì…¹É•ÑÕÉ¹ÌÍ½ÕÉ”µ™¥±”…¹É½ÜÁÉ½Ù•¹…¹”¸()¼¹½Ð…ÁÁ±äƒŠq™¥ÉÍÐÉ½ÜÝ¥¹ÏŠtÍ•±•Ñ¥½¸¸Q¡”Í…µ”É•Í½ÕÉ”­•ä…¸½ÕÈ¥¸‘¥™™•É•¹Ð…Ñ•½Éä½¹Ñ•áÑÌ¸((ŒŒŒ5¥ÍÍ¥¹œÍ•¹…É¥¼µ¥¹ÍÑ…¹”±…å•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀààéÌÀÀÀÀÀÝ€()Q¡”™½ÕÈÑ…‰±•Ì½¹Ñ…¥¸¹¼½µÁ±•Ñ”É•ÁÉ•Í•¹Ñ…Ñ¥½¸½˜Í•¹…É¥¼¥¹ÍÑ…¹”¥‘•¹Ñ¥Ñä°¹½‘•Ì…¹•‘•Ì°‰É…¹ ½È…Ñ¥½¸½É‘•É¥¹œ°Á•ÉÍ¥ÍÑ•ÑÉ¥•È‰¥¹‘¥¹Ì°½¹‘¥Ñ¥½¸ÍÑ…Ñ”°É•ÑÉäÁ½±¥ä°Í¡•‘Õ±•Ì°½È…Ñ¥Ù”•á•ÕÑ¥½¸ÍÑ…Ñ”¸()Q¡½Í”½¹•É¹ÌÉ•ÅÕ¥É”…¹½Ñ¡•ÈÁ•ÉÍ¥ÍÑ•¹”™½Éµ…Ð½È…ÁÁ±¥…Ñ¥½¸½‘”¹½ÐÁÉ•Í•¹Ð¥¸Ñ¡”…¹½¹¥…°½ÉÁÕÌ¸()Q¡”‘•Ñ…¥±•Í¡•µ„°‘¥ÍÑÉ¥‰ÕÑ¥½¹Ì°™É…µ”É•¹‘•É¥¹œ°…¹½Á•¸ÅÕ•ÍÑ¥½¹Ì…É”‘½Õµ•¹Ñ•¥¸mM•¹…É¥¼¹¥¹•t ¸¸½Í•¹…É¥¼µ•¹¥¹”¼¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀàä()M½ÕÉ”Á…Ñ è¥¹Ñ•É¹…±Ì½Ù…±¥‘…Ñ¥½¸µ±…å•ÉÌ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„è¥¹Ñ•É¹…±Í€((ŒŒY…±¥‘…Ñ¥½¸1…å•ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàäéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()5å!=5MÕ¥Ñ”Ù…±¥‘…Ñ¥½¸ÍÁ…¹ÌÍ•Ù•É…°ÍÑ½É•Ì¸QÉ…¹ÍÁ½ÉÐÉ…¹•Ì°…Ñ…±½Õ”‘½µ…¥¹Ì°½¹Ñ•áÑÕ…°™¥±Ñ•ÉÌ°½¹Ù•ÉÍ¥½¸ÉÕ±•Ì°…¹±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì…¹ÍÝ•È‘¥™™•É•¹ÐÅÕ•ÍÑ¥½¹Ì…¹µÕÍÐ‰”…ÁÁ±¥•¥¸½É‘•È¸((ŒŒŒ½¹ÍÑÉ…¥¹Ð±…å•ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàäéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…ÁÁ±¥•ÌÑ½€°™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°Í½ÕÉ•€()ð1…å•ÈðM½ÕÉ”ðEÕ•ÍÑ¥½¸…¹ÍÝ•É•ð)ð€´´´ð€´´´ð€´´´ð)ðQÉ…¹ÍÁ½ÉÐ™¥•±ð=A8¹‘‰€Á…É…µ•Ñ•ÉÌð…¸Ñ¡”•¹½‘•Ù…±Õ”™¥ÐÑ¡”µ…¹…•µ•¹Ð™É…µ”üð)ðAÉ½Á•ÉÑä‘•™¥¹¥Ñ¥½¸ð9}=9€°9}=9}I9€ð]¡…Ð¥ÌÑ¡”ÁÉ½Á•ÉÑçŠeÌ‰…Í”ÑåÁ”…¹‘½µ…¥¸üð)ð=‰©•Ð½™¥ÉµÝ…É”½¹Ñ•áÐð9}%1QI€°9}%1QI}I9€ð]¡¥ ÍÕ‰Í•Ð…ÁÁ±¥•ÌÑ¼Ñ¡¥Ì=‰©•Ð¥µÁ±•µ•¹Ñ…Ñ¥½¸üð)ðM±½Ð…ÁÁ±¥…‰¥±¥ÑäðM}M1=Q}=9%Q%=9€°9}=9%Q%=9€°9}=9Y}IU1€ð%ÌÑ¡¥Ì=‰©•Ð½ÁÉ½Á•ÉÑä…Ñ¥Ù”°…¹¡½Ü¥Ì¥ÑÌÙ…±Õ”½¹Ù•ÉÑ•üð)ðMåµ‰½°µ…ÁÁ¥¹œð=9}Me5	=1}I€ð½•Ì…¸•áÁ±¥¥Ð¥Ñ•´½=‰©•ÐÍåµ‰½°É•±…Ñ¥½¹Í¡¥À•á¥ÍÐ¥¸Ñ¡¥Ì½¹Ñ•áÐüð)ð1¥¹­•ÁÉ½Á•ÉÑ¥•ÌðÉÕ±•Ì¹‘ˆÍ€ð¼½Ñ¡•ÈÁÉ½Á•ÉÑ¥•Ì•¹…‰±”°‘¥Í…‰±”°½È½¹ÍÑÉ…¥¸Ñ¡¥Ì½¹”üð)ðÕ¹Ñ¥½¹…°Í•µ…¹Ñ¥ÌðÁÕ‰±¥ŒÁÉ½Ñ½½°…¹½‰Í•ÉÙ•‰•¡…Ù¥½Èð½•ÌÑ¡”•¹½‘•Ù…±Õ”µ•…¸Ñ¡”¥¹Ñ•¹‘•½Á•É…Ñ¥½¸üð)ð™™•Ñ¥Ù”ÍÑ…Ñ”ð‘¥…¹½ÍÑ¥ŒÉ•…µ‰…¬ð¥Ñ¡”•Ù¥”…ÁÁ±äÑ¡”¥¹Ñ•¹‘•½¹™¥ÕÉ…Ñ¥½¸üð()Q¡”•™™•Ñ¥Ù”‘½µ…¥¸¥ÌÑ¡”¥¹Ñ•ÉÍ•Ñ¥½¸½˜…±°…ÁÁ±¥…‰±”±…å•ÉÌ¸‰É½…=A8¹‘‰€ÑÉ…¹ÍÁ½ÉÐÉ…¹”¹•Ù•È½Ù•ÉÉ¥‘•Ì„¹…ÉÉ½Ý•È…Ñ…±½Õ”ÉÕ±”¸((…m½¹™¥ÕÉ…Ñ¥½¸½Ý¹•ÉÍ¡¥À…¹Ù…±¥‘…Ñ¥½¸µ½‘•±t ¸¸½…ÍÍ•ÑÌ½‘¥…É…µÌ½½¹™¥ÕÉ…Ñ¥½¸µÙ…±¥‘…Ñ¥½¸¹ÍÙœ¤()Q¡”‘¥…É…´Í•Á…É…Ñ•ÌÁ½±åµ½ÉÁ¡¥ŒÁÉ½Á•ÉÑä½Ý¹•ÉÍ¡¥À™É½´Ñ¡”½¹Ñ•áÑÕ…°™¥±Ñ•ÉÌ°Í±½Ð½¹‘¥Ñ¥½¹Ì°…¹½¹Ù•ÉÍ¥½¹ÌÑ¡…Ð¹…ÉÉ½Ü½ÈÑÉ…¹Í™½É´Ñ¡”‰…Í”‘½µ…¥¸¸((ŒŒŒ½¹Ñ•áÐ™¥ÉÍÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàäéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()Y…±¥‘…Ñ¥½¸‰•¥¹Ì½¹±ä…™Ñ•ÈÉ•Í½±Ù¥¹œÑ¡”A¡åÍ¥…°•Ù¥”°™¥ÉµÝ…É”°Í±½Ñ€°ÕÉÉ•¹Ð=‰©•Ð½ÈY¥É¥¸=‰©•Ð°Ñ…É•Ð=‰©•Ð°…¹…ÁÁ±¥…‰±”=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸¸()]¥Ñ¡½ÕÐÑ¡…Ð½¹Ñ•áÐ°„½¹™¥ÕÉ…Ñ¥½¸¥‘á€°ÍÑ½É•¥¹Ñ••È°½È‘¥ÍÁ±…ä±…‰•°¥Ì¥¹ÍÕ™™¥¥•¹Ð¸((ŒŒŒ	…Í”…¹½¹Ñ•áÑÕ…°‘½µ…¥¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàäéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€()9}=9}I9€…¸‘•™¥¹”¹…µ•Ù…±Õ•Ì°¹Õµ•É¥Œ‰½Õ¹‘Ì°ÍÑ•ÀÍ¥é”°‘¥¥ÐÝ¥‘Ñ °½É‘•É¥¹œ°…¹‘•™…Õ±ÑÌ¸µ¥ÍÍ¥¹œÉ…¹”É½Ü‘½•Ì¹½Ð¥µÁ±ä…¸Õ¹É•ÍÑÉ¥Ñ•Ù…±Õ”¸()9}%1QI€‰¥¹‘Ì„½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¸Ñ¼…¸M}=	)Q}%I5]I€½¹Ñ•áÐ¸I•±…Ñ•9}%1QI}I9€É½ÝÌ¹…ÉÉ½ÜÑ¡”‰…Í”‘½µ…¥¸™½ÈÑ¡…Ð•á…Ð=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸¸()Í…™”•Ù…±Õ…Ñ½ÈÉ•Ñ…¥¹Ì¥‘}½¹™€…¹½Ý¹•ÉÍ¡¥ÀÍ½Á”°Ñ¡”É…Ü…¹‘¥‘…Ñ”°‰…Í”‘½µ…¥¸°Í•±•Ñ•™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¸…¹½¹Ù•ÉÍ¥½¸Á…Ñ °™¥¹…°•¹½‘•Ù…±Õ”°…¹Õ¹É•Í½±Ù•‘•Á•¹‘•¹¥•Ì¸((ŒŒŒ½¹‘¥Ñ¥½¹Ì…¹½¹Ù•ÉÍ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàäéÌÀÀÀÀÀÕ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€()M±½Ð½¹‘¥Ñ¥½¹Ì…¸‘•Á•¹½¸½Ñ¡•È¥Ñ•´µ±•Ù•°½È=‰©•Ðµ±•Ù•°Íåµ‰½±Ì¸9}=9%Q%=9€Á½¥¹ÑÌ¥¹Ñ¼½¹Ù•ÉÍ¥½¸µÉÕ±”±½¥ŒÉ•ÁÉ•Í•¹Ñ•‰ä9}=9Y}IU1€¸()¼¹½Ð•Ù…±Õ…Ñ”„ÉÕ±”Ý¥Ñ „Á…ÉÑ¥…°…¹‘¥‘…Ñ”½¹™¥ÕÉ…Ñ¥½¸¸5¥ÍÍ¥¹œ¥¹ÁÕÑÌ°…µ‰¥Õ½ÕÌ‰É…¹¡•Ì°½ÈÕ¹µ…ÁÁ•½ÕÑÁÕÐµ…­”Ñ¡”É•ÍÕ±ÐÕ¹É•Í½±Ù•¸()™Ñ•È½¹Ù•ÉÍ¥½¸°Ù…±¥‘…Ñ”Ñ¡”½ÕÑÁÕÐ……¥¸……¥¹ÍÐÑ¡”•™™•Ñ¥Ù”‘½µ…¥¸…¹™É…µ”ÑÉ…¹ÍÁ½ÉÐ™¥•±¸½¹Ù•ÉÍ¥½¸‘½•Ì¹½Ðµ…­”…¸•á±Õ‘•Ù…±Õ”Ù…±¥¸((ŒŒŒÉÕ±•Ì¹‘ˆÍ€‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàäéÌÀÀÀÀÀÙ€()AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()Q¡”…¹½¹¥…°ÉÕ±•Ì¹‘ˆÍ€½¹Ñ…¥¹Ì…‘‘¥Ñ¥½¹…°±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì™½ÈÍ•±•Ñ•Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°=‰©•ÑÌ¸I•™•É•¹•ÌÍÕ …Ì€Å€°€É€°½È€ÈÅ€…É”½¹™¥ÕÉ…Ñ¥½¸¥¹‘•á•Ì½¹±ä¥¹Í¥‘”Ñ¡”É•Í½±Ù•=‰©•Ð½¹Ñ•áÐ¸()Q¡”‘…Ñ…‰…Í”¥Ì¹½Ð„±½‰…°=‰©•ÐÉ•¥ÍÑÉä°„µ…ÁÁ¥¹œ™É½´•Ù•Éä]!=€Ñ¼½¹™¥ÕÉ…Ñ¥½¸°½È„ÍÕ‰ÍÑ¥ÑÕÑ”™½È5!…Ñ…±½Õ”¹‘‰€¸()½¹ÑÉ½±±¥¹œµÁÉ½Á•ÉÑä¡…¹”…¸‘¥Í…‰±”…¹½Ñ¡•È™¥•±Ñ¡É½Õ ¥Í…‰±•±¥¹­•‘A…É…µ•Ñ•É€‰•¡…Ù¥½È¸I•½µÁÕÑ”Ñ¡”…™™•Ñ•ÁÉ½Á•ÉÑäÍ•ÐÉ…Ñ¡•ÈÑ¡…¸Ù…±¥‘…Ñ¥¹œ½¹±äÑ¡”•‘¥Ñ•Ù…±Õ”¸((ŒŒŒI•……¹ÝÉ¥Ñ”‘¥ÍÑ¥¹Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàäéÌÀÀÀÀÀÝ€()U¹•ÉÑ…¥¹Ñäèµ…å€°Õ¹É•Í½±Ù•‘€()ÁÉ½Á•ÉÑä…¸‰”ÝÉ¥Ñ…‰±”°½¹‘¥Ñ¥½¹…±±äÝÉ¥Ñ…‰±”°™¥á•°É•…µ½¹±ä°¡¥‘‘•¸‰ÕÐÍ•µ…¹Ñ¥…±±ä…Ñ¥Ù”°Õ¹ÍÕÁÁ½ÉÑ•°½ÈÕ¹É•Í½±Ù•¸Y¥Í¥‰¥±¥Ñä¥Ì¹½ÐÁ•Éµ¥ÍÍ¥½¸¸()AÉ½É…µµ¥¹œµÕÍÐÙ…±¥‘…Ñ”Ñ¡”½µÁ±•Ñ”É•Á±…•µ•¹ÐÍÑ…Ñ”Ý¡•¸Ñ¡”Í•±•Ñ•Í•ÅÕ•¹”‰•¥¹ÌÝ¥Ñ É•Í•Ðµ…±°¸Y…±¥‘…Ñ¥¹œ½¹±äÑ¡”¡…¹•™¥•±¥ÌÕ¹Í…™”‰•…ÕÍ”½µ¥ÑÑ•5½‘Õ±•Ì½ÈÁÉ½Á•ÉÑ¥•Ìµ…ä¹½ÐÍÕÉÙ¥Ù”Ñ¡”ÑÉ…¹Í™•È¸((ŒŒŒI•ÍÕ±Ðµ½‘•°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀàäéÌÀÀÀÀÀá€()U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()ðMÑ…ÑÕÌð5•…¹¥¹œð)ð€´´´ð€´´´ð)ðÙ…±¥ð‘¥É•Ñ±ä…±±½Ý•¥¸Ñ¡”½µÁ±•Ñ”É•Í½±Ù•½¹Ñ•áÐð)ðÙ…±¥…™Ñ•È½¹Ù•ÉÍ¥½¸ð…±±½Ý•Ñ¡É½Õ …¸•ÍÑ…‰±¥Í¡•½¹Ù•ÉÍ¥½¸Á…Ñ ð)ð½¹‘¥Ñ¥½¹…±±äÙ…±¥ðÙ…±¥Ý¡¥±”ÍÑ…Ñ•‘•Á•¹‘•¹¥•Ì¡½±ð)ð™¥á•½É•…µ½¹±äðÁ…ÉÐ½˜•™™•Ñ¥Ù”ÍÑ…Ñ”‰ÕÐ¹½Ð…É‰¥ÑÉ…Éä¥¹ÁÕÐð)ð¥¹Ù…±¥ð•á±Õ‘•‰ä…¸…ÁÁ±¥…‰±”½¹ÍÑÉ…¥¹Ðð)ð…µ‰¥Õ½ÕÌðÍ•Ù•É…°¥¹½µÁ…Ñ¥‰±”É•Í½±ÕÑ¥½¹ÌÉ•µ…¥¸ð)ðÕ¹É•Í½±Ù•ðÉ•ÅÕ¥É•Í½ÕÉ”½¹Ñ•áÐ½Èµ…ÁÁ¥¹œ¥Ì…‰Í•¹Ðð()½ÈÑ¡”™Õ±°ÁÉ½É…µµ¥¹œ…±½É¥Ñ¡´°Í•”mAÉ½É…µµ¥¹œY…±¥‘…Ñ¥½¹t ¸¸½ÁÉ½É…µµ¥¹œ½Ù…±¥‘…Ñ¥½¸¹µ¤¸AÉ…Ñ¥…°ME0•á…µÁ±•Ì‰•±½¹œ¥¸mAÉ…Ñ¥…°Õ¥‘•Ít ¸¸½Õ¥‘•Ì¼¤°Ý¡•É”Ñ¡•ä…¸‰”Í¡½Ý¸¥¸…¸•¹µÑ¼µ•¹Ñ…Í¬¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀäÀ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒAÉ½É…µµ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÀéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìèé¥‰••€)U¹•ÉÑ…¥¹Ñäè¹½Ð•ÍÑ…‰±¥Í¡•‘€()Q¡”ÁÉ½É…µµ¥¹œÁÉ½Ñ½½°¡…¹•ÌÑ¡”¥¹ÍÑ…±±•½¹™¥ÕÉ…Ñ¥½¸½˜„A¡åÍ¥…°•Ù¥”°¥ÑÌ5½‘Õ±•Ì°…¹Ñ¡•¥ÈÍ•±•Ñ•=‰©•ÑÌ¸5å!=5}MÕ¥Ñ”½µ‰¥¹•Ì=Á•¹]•‰9•Ðµ…¹…•µ•¹Ð™É…µ•Ì™É½´=A8¹‘‰€Ý¥Ñ …Á…‰¥±¥Ñä…¹Ù…±¥‘…Ñ¥½¸‘…Ñ„™É½´5!…Ñ…±½Õ”¹‘‰€¸()AÉ½É…µµ¥¹œ¥Ì‘¥ÍÑ¥¹Ð™É½´‘¥…¹½ÍÑ¥Ì¸¥…¹½ÍÑ¥ÌÉ•Á½ÉÑÌ¥¹ÍÑ…±±•ÍÑ…Ñ”ìÁÉ½É…µµ¥¹œÉ•ÅÕ•ÍÑÌ„ÍÑ…Ñ”¡…¹”¸ÍÕ•ÍÍ™Õ°É•ÍÁ½¹Í”¥Ì¹½Ð„ÍÕ‰ÍÑ¥ÑÕÑ”™½ÈÙ…±¥‘…Ñ¥½¸‰•™½É”ÑÉ…¹Íµ¥ÍÍ¥½¸½È‘¥…¹½ÍÑ¥ŒÉ•…µ‰…¬…™Ñ•ÉÝ…É¸()Q¡”…¹½¹¥…°É½ÍÌµ…É•„½Ý¹•ÉÍ¡¥À½˜‘¥Í½Ù•Éä°¥¹Ñ•ÉÙ¥•Ü°½¹™¥ÕÉ…Ñ¥½¸É•…‘¥¹œ°ÉÕ¹Ñ¥µ”½¹ÑÉ½°°…¹ÁÉ½É…µµ¥¹œ¥ÌÍÕµµ…É¥é•¥¸m=Á•¹]•‰9•ÐM½Á”…¹É¡¥Ñ•ÑÕÉ•t ¸¸½ÁÉ½Ñ½½°½Í½Á”µ…¹µ…É¡¥Ñ•ÑÕÉ”¹µ¤¸()Q¡•Í”…É”ÍÑ½É•MÕ¥Ñ”µ…¹…•µ•¹ÐÝ½É­™±½ÝÌ°¹½Ð•ÍÑ…‰±¥Í¡•ÁÉ½É…µµ¥¹œÍÕÁÁ½ÉÐ½¸•Ù•Éä=Á•¹]•‰9•ÐÑÉ…¹ÍÁ½ÉÐ¸Q¡”mi¥	•”%¹Ñ•É™…•t ¸¸½ÁÉ½Ñ½½°½é¥‰•”µ¥¹Ñ•É™…”¹µ¤•áÁ½Í•ÌÍ•Á…É…Ñ”µ…¹…•µ•¹Ð…¹‰¥¹‘¥¹œµ•¡…¹¥ÍµÌì¹•¥Ñ¡•ÈÑ¡•¥È•á¥ÍÑ•¹”¹½ÈÍ¡…É•™Õ¹Ñ¥½¹…°¹…µ•ÍÁ…•Ì•ÍÑ…‰±¥Í¡•Ì½¹™-=€½µÁ…Ñ¥‰¥±¥Ñä¸((ŒŒŒI•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÀéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°Í½ÕÉ•€()ðMÕ‰©•ÐðA…”ð)ð€´´´ð€´´´ð)ðAÉ½É…µµ¥¹œ™…µ¥±¥•Ì°±…å•ÉÌ°…¹Í½ÕÉ”‰½Õ¹‘…É¥•ÌðmAÉ½É…µµ¥¹œÉ¡¥Ñ•ÑÕÉ•t¡…É¡¥Ñ•ÑÕÉ”¹µ¤ð)ðAÉ½É…µµ¥¹œÍÑ…Ñ•Ì°½É‘•É¥¹œ°…¹Ñ•Éµ¥¹…Ñ¥½¸ðmAÉ½É…µµ¥¹œM•ÍÍ¥½¸1¥™•å±•t¡Í•ÍÍ¥½¸µ±¥™•å±”¹µ¤ð)ðM•±•Ñ¥¹œ„•Ù¥”‰ä…‘‘É•ÍÌ°%°½È±½…°¥¹Ñ•É…Ñ¥½¸ðm•Ù¥”M•±•Ñ¥½¹t¡‘•Ù¥”µÍ•±•Ñ¥½¸¹µ¤ð)ðM•±•Ñ¥¹œ=‰©•ÑÌ™½È™¥ÉµÝ…É”5½‘Õ±•Ìðm=‰©•ÐAÉ½É…µµ¥¹t¡½‰©•ÐµÁÉ½É…µµ¥¹œ¹µ¤ð)ðAÉ½É…µµ¥¹œ™Õ¹Ñ¥½¹…°…‘‘É•ÍÍ•Ìðm‘‘É•ÍÌAÉ½É…µµ¥¹t¡…‘‘É•ÍÌµÁÉ½É…µµ¥¹œ¹µ¤ð)ðAÉ½É…µµ¥¹œ¥¹‘•á•½¹™¥ÕÉ…Ñ¥½¸Ù…±Õ•Ìðm½¹™¥ÕÉ…Ñ¥½¸AÉ½É…µµ¥¹t¡½¹™¥ÕÉ…Ñ¥½¸µÁÉ½É…µµ¥¹œ¹µ¤ð)ðÙ…±Õ…Ñ¥¹œ…Ñ…±½Õ”É…¹•Ì°™¥±Ñ•ÉÌ°…¹½¹‘¥Ñ¥½¹ÌðmAÉ½É…µµ¥¹œY…±¥‘…Ñ¥½¹t¡Ù…±¥‘…Ñ¥½¸¹µ¤ð)ðI•©•Ñ¥½¸°Ñ¥µ•½ÕÐ°…‰½ÉÐ°…¹É•½Ù•ÉäðmAÉ½É…µµ¥¹œÉÉ½È!…¹‘±¥¹t¡•ÉÉ½Èµ¡…¹‘±¥¹œ¹µ¤ð)ð¥…¹½ÍÑ¥ŒÉ•…µ‰…¬…¹ÍÑ…Ñ”½µÁ…É¥Í½¸ðmAÉ½É…µµ¥¹œY•É¥™¥…Ñ¥½¹t¡Ù•É¥™¥…Ñ¥½¸¹µ¤ð)ðAÉ½É…µµ¥¹œ]!Q€Ù…±Õ•ÌðmAÉ½É…µµ¥¹œ]!Q€I•™•É•¹•t¡Ý¡…ÐµÉ•™•É•¹”¹µ¤ð)ðAÉ½É…µµ¥¹œ%59M%=9€Ù…±Õ•ÌðmAÉ½É…µµ¥¹œ%59M%=9€I•™•É•¹•t¡‘¥µ•¹Í¥½¸µÉ•™•É•¹”¹µ¤ð((ŒŒŒ…¹½¹¥…°Í•¹…É¥½Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÀéÌÀÀÀÀÀÍ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()=A8¹‘‰€‘•™¥¹•ÌÑ¡É•”É•…½ÝÉ¥Ñ”ÁÉ½É…µµ¥¹œÍ•¹…É¥½Ìè()ðM•¹…É¥¼ð=É‘•É•Í•ÅÕ•¹•Ìð)ð€´´´ð€´´´ð)ð½¹™A½¥¹ÐÉA½¥¹Ñ	å‘‘É•ÍÍ€ð½¹™‘‘É•ÍÍ•‘€ƒŠH½¹™½¹™¥ÕÉ…Ñ½ÉÍ€ƒŠH±½Í•½¹™€ð)ð½¹™A½¥¹ÐÉA½¥¹Ñ]¥Ñ¡%€ð½¹™A½¥¹ÐÉA½¥¹Ñ]¥Ñ¡%€ƒŠHÉ•Á•…Ñ•½¹™-=€ƒŠH±½Í•½¹™€ð)ð½¹™1½…±	ÕÑÑ½¹€ð½¹™1½…±	ÕÑÑ½¹€ƒŠHÉ•Á•…Ñ•½¹™-=€ƒŠH½¹™½¹™¥ÕÉ…Ñ½ÉÍ€ƒŠH±½Í•½¹™€ð()Q¡”Í•¹…É¥¼¹…µ•ÌÁÉ•Í•ÉÙ”5å!=5}MÕ¥Ñ”Ñ•Éµ¥¹½±½ä¸ƒŠq%Št¥¸Í½ÕÉ”‘•ÍÉ¥ÁÑ¥½¹ÌÉ•™•ÉÌÑ¼Ñ¡”€ÌÈµ‰¥Ð¥¹ÍÑ…±±••Ù¥”%ÕÍ•‰äÑ¡”€©m]!=t¨äm%t¨ÀŒ€ÍÑ…ÉÐ™É…µ”¸()Q¡”Í•¹…É¥½Ì•áÁ½Í”ÑÝ¼ÁÉ½É…µµ¥¹œÁÉ½©•Ñ¥½¹Ìè()ðAÉ½©•Ñ¥½¸ðAÉ¥¹¥Á…°ÝÉ¥Ñ•Ìð=A8¹‘‰€‘•ÍÉ¥ÁÑ¥½¸ð)ð€´´´ð€´´´ð€´´´ð)ðY¥ÉÑÕ…°½¹™¥ÕÉ…Ñ½ÉÌð%59M%=8€Ñ€…¹€Õ€ðÍ•Ð•Ù¥”½¹™¥ÕÉ…Ñ½ÉÌð)ð‘Ù…¹•=‰©•Ð½¹™¥ÕÉ…Ñ¥½¸ð%59M%=8€ÌÁ€°€ÌÉ€°…¹€ÌÕ€ðÍ•Ð=‰©•Ð°…‘‘É•ÍÌ°…¹¥¹‘•á•Á…É…µ•Ñ•ÉÌð()Q¡•Í”ÁÉ½©•Ñ¥½¹Ì…É”¹½Ð¥¹Ñ•É¡…¹•…‰±”¸Q¡”…‘‘É•ÍÌµÍ•±•Ñ•Í•¹…É¥¼½¹Ñ…¥¹ÌÙ¥ÉÑÕ…°µ½¹™¥ÕÉ…Ñ½ÈÑÉ…¹Í™•È‰ÕÐ¹¼½¹™-=€Í•ÅÕ•¹”¸Q¡”%µÍ•±•Ñ•Í•¹…É¥¼½¹Ñ…¥¹Ì…‘Ù…¹•=‰©•ÐÑÉ…¹Í™•È‰ÕÐ¹¼½¹™½¹™¥ÕÉ…Ñ½ÉÍ€Í•ÅÕ•¹”¸Q¡”±½…°µ¥¹Ñ•É…Ñ¥½¸Í•¹…É¥¼½¹Ñ…¥¹Ì‰½Ñ ¸()Q¡•Í”¹…µ•Ì…É”=A8¹‘‰€ÁÉ½É…µµ¥¹œµÍ•ÅÕ•¹”Ñ•Éµ¥¹½±½ä¸5!…Ñ…±½Õ”¹‘‰€¥¹‘•Á•¹‘•¹Ñ±äÉ•¥ÍÑ•ÉÌY¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸…¹‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸…Ì‘¥ÍÑ¥¹Ð½¹™¥ÕÉ…Ñ¥½¸µ½‘•Ì°…±½¹œÝ¥Ñ A¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸…¹AÉ½‘ÕÐAÉ½É…µµ¥¹œ¸¼¹½ÐÕÍ”½¹”Í½ÕÉ”Ì±…‰•°…Ì…¸Õ¹‘½Õµ•¹Ñ•Õµ‰É•±±„™½ÈÑ¡”½Ñ¡•ÈÍ½ÕÉ”Ì½¹•ÁÑÌ¸((ŒŒŒM…™”Ý½É­™±½Ü()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÀéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€((Ä¸I•Í½±Ù”Ñ¡”‘¥…¹½ÍÑ¥Œ™…µ¥±ä…¹¥¹ÍÑ…±±•A¡åÍ¥…°•Ù¥”¸(È¸I•Í½±Ù”¥ÑÌ¥Ñ•´°™¥ÉµÝ…É”°5½‘Õ±•Ì°=‰©•ÑÌ°…¹Y¥É¥¸=‰©•ÑÌ¸(Ì¸Y…±¥‘…Ñ”•Ù•ÉäÑ…É•Ð=‰©•Ð°…‘‘É•ÍÌ°…¹Á…É…µ•Ñ•È¥¸Ñ¡”½µÁ±•Ñ”…Ñ…±½Õ”½¹Ñ•áÐ¸(Ð¸M•±•ÐÑ¡”•Ù¥”ÕÍ¥¹œÑ¡”Í•¹…É¥¼…ÁÁÉ½ÁÉ¥…Ñ”Ñ¼Ñ¡”½Á•É…Ñ¥½¸¸(Ô¸QÉ…¹Í™•È½¹±äÑ¡”™É…µ•Ì‰•±½¹¥¹œÑ¼Ñ¡…ÐÍ•¹…É¥¼…¹Í•ÅÕ•¹”¸(Ø¸AÉ•Í•ÉÙ”Ý…É¹¥¹Ì°•ÉÉ½ÉÌ°Ñ¥µ•½ÕÐ°…‰½ÉÐ°…¹Ñ•Éµ¥¹…°É•ÍÁ½¹Í•Ì¸(Ü¸±½Í”Ñ¡”ÁÉ½É…µµ¥¹œÍ•ÍÍ¥½¸¸(à¸MÑ…ÉÐ„¹•Ü‘¥…¹½ÍÑ¥Œ¥¹Ñ•ÉÙ¥•Ü…¹½µÁ…É”Ñ¡”•™™•Ñ¥Ù”ÍÑ…Ñ”¸()¼¹½Ð¥¹™•È„ÁÉ½É…µµ¥¹œµ•Ñ¡½™É½´„‘•Í¥É•Ù…±Õ”…±½¹”¸Ù…±Õ”µ…ä‰”É•ÁÉ•Í•¹Ñ…‰±”Ñ¡É½Õ Á¡åÍ¥…°°Ù¥ÉÑÕ…°°½È…‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸Ý¡¥±”Ñ¡”…¹½¹¥…°Í•¹…É¥½ÌÍÕÁÁ½ÉÐ‘¥™™•É•¹ÐÑÉ…¹Í™•Èµ•¡…¹¥ÍµÌ¸((ŒŒŒM½Á”‰½Õ¹‘…É¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÀéÌÀÀÀÀÀÕ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€()Q¡¥ÌÍ•Ñ¥½¸‘½Õµ•¹ÑÌÁÉ½É…µµ¥¹œÍÑ…Ñ”µ…¡¥¹•Ì…¹ÝÉ¥Ñ•Ì¸I•ÕÍ…‰±”…Á…‰¥±¥Ñä‰•±½¹ÌÕ¹‘•Èm•Ù¥”5½‘•±t ¸¸½‘•Ù¥”µµ½‘•°¼¤ì‘¥Í½Ù•Éä…¹É•…µ‰…¬‰•±½¹œÕ¹‘•Èm¥…¹½ÍÑ¥Ít ¸¸½‘¥…¹½ÍÑ¥Ì¼¤ìÍ¡…É•™É…µ”É…µµ…È‰•±½¹ÌÕ¹‘•ÈmAÉ½Ñ½½±t ¸¸½ÁÉ½Ñ½½°¼¤¸()Q¡”ÁÕ‰±¥Œ=Á•¹]•‰9•ÐAÌ‘•™¥¹”™É…µ”Íå¹Ñ…à…¹™Õ¹Ñ¥½¹…°]!=€‰•¡…Ù¥½È‰ÕÐ‘¼¹½Ð‘•™¥¹”Ñ¡•Í”5å!=5}MÕ¥Ñ”ÁÉ½É…µµ¥¹œÍÑ…Ñ”µ…¡¥¹•Ì¸Q¡”…ÕÑ¡½É¥Ñ…Ñ¥Ù”¥µÁ±•µ•¹Ñ…Ñ¥½¸ÍÑÉÕÑÕÉ”™½ÈÑ¡¥ÌÍ•Ñ¥½¸¥ÌÑ¡•É•™½É”=A8¹‘‰€Á±ÕÌ=Á•¹EÕ•Éä¹ÑáÑ€°¥¹Ñ•ÉÁÉ•Ñ•Ý¥Ñ 5!…Ñ…±½Õ”¹‘‰€°ÉÕ±•Ì¹‘ˆÍ€°½‰Í•ÉÙ•‰•¡…Ù¥½È°…¹Ñ¡”5å!=5}MÕ¥Ñ”U$¸()AÉ¥Ù…Ñ”…ÁÑÕÉ•Ì…É”¹½ÐÍÑ½É•¥¸Ñ¡”É•Á½Í¥Ñ½Éä¸…ÁÑÕÉ”µÍÕÁÁ½ÉÑ•½¹±ÕÍ¥½¹Ì…É”ÍÑ…Ñ•Ý¥Ñ¡½ÕÐ¥¹ÍÑ…±±…Ñ¥½¸µÍÁ•¥™¥ŒÑÉ…¹ÍÉ¥ÁÑÌ¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀäÄ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½…‘‘É•ÍÌµÁÉ½É…µµ¥¹œ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒ‘‘É•ÍÌAÉ½É…µµ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÄéÌÀÀÀÀÀÅ€()‘‘É•ÍÌÁÉ½É…µµ¥¹œ…ÍÍ¥¹ÌÑ¡”•™™•Ñ¥Ù”™Õ¹Ñ¥½¹…°ÍåÍÑ•´…¹…‘‘É•ÍÌ½˜½¹”½¹™¥ÕÉ•5½‘Õ±”‘ÕÉ¥¹œ…‘Ù…¹•=‰©•ÐÑÉ…¹Í™•È¸((ŒŒŒ]É¥Ñ”™É…µ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÄéÌÀÀÀÀÀÉ€()€¨m]!=t¨À¨ŒÌÈmM1=Qt©mMeMt©mItŒ€()€ŒÌÈmM1=Qu€¥ÌÑ¡”Á…É…µ•Ñ•É¥é•%59M%=9€Í•±•Ñ½È¸Q¡”±•…‘¥¹œ€€Í•±•ÑÌÑ¡”ÝÉ¥Ñ”™½É´°…¹Ñ¡”™½±±½Ý¥¹œ€€…ÑÑ…¡•ÌM1=Q€Ñ¼Ñ¡…ÐÍ•±•Ñ½È¸MeM€…¹I€…É”½É‘¥¹…Éä%59M%=9€Ù…±Õ•ÌÍ•Á…É…Ñ•Ý¥Ñ €©€¸()ð¥•±ð=A8¹‘‰€É…¹”ð5•…¹¥¹œð)ð€´´´ð€´´´ð€´´´ð)ðM1=Q€ð€Ä¸¸ÈÔÕ€ð•Ù¥”µ±½…°Í±½Ñ€ð)ðMeM€ð€Ä¸¸ÈÔÕ€ð=‰©•ÐÍåÍÑ•´Í•±•Ñ½Èð)ðI€ð€À¸¸ØÔÔÌÕ€ð•¹½‘•…‘‘É•ÍÌð()Q¡•Í”É…¹•Ì…É”ÑÉ…¹ÍÁ½ÉÐ…Á…¥Ñä°¹½ÐÕ¹¥Ù•ÉÍ…°Ù…±¥‘¥Ñä¸((ŒŒŒI•Í½±ÕÑ¥½¸ÁÉ½•‘ÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÄéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°•Ù¥‘•¹•€((Ä¸I•Í½±Ù”Ñ¡”•Ù¥”°™¥ÉµÝ…É”°Í±½Ñ€°…¹Ñ…É•Ð=‰©•Ð¸(È¸•Ñ•Éµ¥¹”Ñ¡”™Õ¹Ñ¥½¹…°ÍåÍÑ•´ÍÕÁÁ½ÉÑ•‰äÑ¡…Ð=‰©•Ð¸(Ì¸M•±•ÐÑ¡”…ÁÁ±¥…‰±”=A8¹‘‰€…‘‘É•ÍÌÉÕ±”™½ÈÑ¡”µ…¹…•µ•¹Ð™…µ¥±ä…¹=‰©•Ð½‘•Ù¥”™…µ¥±ä¸(Ð¸Y…±¥‘…Ñ”½µÁ½¹•¹ÐÙ…±Õ•Ì°™¥á•ÁÉ•™¥á•Ì°Á…‘‘¥¹œ°…‘Ù…¹•½™™Í•ÑÌ°±•Ù•°ÉÕ±•Ì°…¹Ù…±¥‘¥Ñä½¹‘¥Ñ¥½¹Ì¸(Ô¸ÍÑ…‰±¥Í Ñ¡”=‰©•ÐµÍÁ•¥™¥Œµ…ÁÁ¥¹œ™É½´Ñ¡”Í•µ…¹Ñ¥Œ…‘‘É•ÍÌÑ¼¹Õµ•É¥ŒI€¸¼¹½Ð½Áä„™Õ¹Ñ¥½¹…°]!I€½È…ÁÁ•¹É½ÕÑ¥¹œÍÕ™™¥á•Ì¥¹Ñ¼Ñ¡¥ÌÙ…±Õ”µ•É•±ä‰•…ÕÍ”…¸…‘‘É•ÍÌµÉÕ±”Ñ•µÁ±…Ñ”…¸É•¹‘•ÈÑ¡•´¸(Ø¸AÉ•Í•ÉÙ”MeM€…Ì„Í•Á…É…Ñ”™¥•±¸(Ü¸M•¹Ñ¡”…‘‘É•ÍÌ½¹±ä…™Ñ•ÈÑ¡”½ÉÉ•ÍÁ½¹‘¥¹œ=‰©•ÐÝÉ¥Ñ”¸(à¸Y•É¥™äÑ¡”•™™•Ñ¥Ù”ÑÕÁ±”Ñ¡É½Õ ‘¥…¹½ÍÑ¥Œ%59M%=8€ÌÉ€¸()MeM€¥Ì±…‰•±±•ƒŠq-•å=‰©•ÐÍåÍÑ•·Št‰ä=A8¹‘‰€¸%Ð¥Ì¹½Ð…ÕÑ½µ…Ñ¥…±±ä„™Õ¹Ñ¥½¹…°]!=€°‘¥…¹½ÍÑ¥Œ]!=€°½È¥¹Ñ•É¹…°9}MeMQ4¹¥‘}ÍåÍÑ•µ€¸¹Õµ•É¥Œµ…ÁÁ¥¹œÉ•ÅÕ¥É•Ì=‰©•Ð½ÍåÍÑ•´…¹…ÁÑÕÉ”½ÉÉ½‰½É…Ñ¥½¸¸()Õ¹Ñ¥½¹…°]!I€°µ…¹…•µ•¹ÐÍ•±•Ñ¥½¸]!I€°…¹Ñ¡”%59M%=8€ÌÈ¹I€Á…å±½……É”‘¥ÍÑ¥¹ÐÉ•ÁÉ•Í•¹Ñ…Ñ¥½¹Ì¸Q¡”ÍÑ½É•É…¹”€À¸¸ØÔÔÌÕ€‘½•Ì¹½Ð•¹½‘”„Õ¹¥Ù•ÉÍ…°½¹Ù•ÉÍ¥½¸™É½´ÍÑÉ¥¹ÌÍÕ …ÌÉ½ÕÀ½ÈÉ½ÕÑ•…‘‘É•ÍÍ•Ì¸‘‘É•ÍÌµÉÕ±”Í•±•Ñ¥½¸…¹É•¹‘•É¥¹œÉ•µ…¥¸Á…ÉÑ±äÕ¹É•Í½±Ù•ìÍÑ½À‰•™½É”„ÝÉ¥Ñ”¥˜•¥Ñ¡•ÈMeM€½ÈÑ¡”I€½¹Ù•ÉÍ¥½¸±…­Ì…ÁÁ±¥…‰±”•Ù¥‘•¹”¸((ŒŒŒ‘‘É•ÍÌ™…µ¥±¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÄéÌÀÀÀÀÀÑ€()AÉ½É…µµ¥¹œÉ•ÕÍ•ÌÍåÍÑ•´µÍÁ•¥™¥ŒÉ…µµ…ÉÌÉ…Ñ¡•ÈÑ¡…¸½¹”•¹•É¥Œ€½A1€™½É´¸Q¡”…¹½¹¥…°¥µÁ±•µ•¹Ñ…Ñ¥½¸¥¹±Õ‘•Ì°…µ½¹œ½Ñ¡•ÉÌè((´1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸Á½¥¹ÐµÑ¼µÁ½¥¹Ð…¹¥¹Ñ•É™…”™½ÉµÌì(´Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°é½¹”°…ÑÕ…Ñ½È°Í±…Ù”µÁÉ½‰”°…¹•áÑ•É¹…°µÁÉ½‰”™½ÉµÌì(´Y¥‘•¼½½È¹ÑÉä¥¹Ñ•É™…”™½ÉµÌì(´¹•Éä5…¹…•µ•¹Ð½¹ÑÉ½°µÕ¹¥Ð…¹…ÑÕ…Ñ½È™½ÉµÌì(´•ÍÌ½¹ÑÉ½°½µµ…¹…¹¥¹‘¥…Ñ½È™½ÉµÌ¸()Q¡”½µÁ±•Ñ”¥µÁ±•µ•¹Ñ…Ñ¥½¸¥¹Ù•¹Ñ½Éä¥Ìµ…¥¹Ñ…¥¹•¥¸m‘‘É•ÍÌ¥Í½Ù•Éåt ¸¸½‘¥…¹½ÍÑ¥Ì½…‘‘É•ÍÌµ‘¥Í½Ù•Éä¹µ¤¸((ŒŒŒA¡åÍ¥…°½Õ¹Ñ•ÉÁ…ÉÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÄéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()½È1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸°‘•½‘•€…¹A1€…¸½ÉÉ•ÍÁ½¹Ñ¼Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹Ì‘•±…É•‰äÑ¡”™¥ÉµÝ…É”¸Q¡…Ð½ÉÉ•ÍÁ½¹‘•¹”•ÍÑ…‰±¥Í¡•ÌÁ¡åÍ¥…°…Á…‰¥±¥Ñä°¹½ÐÑ¡”…Ñ¥Ù”ÁÉ½É…µµ¥¹œµ•Ñ¡½¸()Ù…±Õ”½ÕÑÍ¥‘”Ñ¡”•ÍÑ…‰±¥Í¡•Á¡åÍ¥…°É…¹”…¸•á±Õ‘”Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸¸Ù…±Õ”Ý¥Ñ¡¥¸¥ÐÉ•µ…¥¹Ì…µ‰¥Õ½ÕÌ‰•…ÕÍ”…‘Ù…¹•½ÈÙ¥ÉÑÕ…°ÁÉ½É…µµ¥¹œ…¸ÁÉ½‘Õ”Ñ¡”Í…µ”•™™•Ñ¥Ù”…‘‘É•ÍÌ¸()M•”mA¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸…¹½¹™¥ÕÉ…Ñ¥½¸µ½‘•Ít ¸¸½‘•Ù¥”µµ½‘•°½½¹™¥ÕÉ…Ñ¥½¸¹µÁ¡åÍ¥…°µ½¹™¥ÕÉ…Ñ¥½¸µ…¹µ½¹™¥ÕÉ…Ñ¥½¸µµ½‘•Ì¤¸((ŒŒŒ‘‘É•ÍÌ•ÉÉ½È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÄéÌÀÀÀÀÀÙ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()Q¡”•Ù¥”…¸É•Á½ÉÐè()€¨m]!=t©m]!It¨ÌÐ©mM1=Qt©mII=ItŒ€()II=I€¥Ì‰½½±•…¸¸=A8¹‘‰€ÍÕÁÁ±¥•Ì¹¼µ½É”‘•Ñ…¥±•É•…Í½¸¸AÉ•Í•ÉÙ”Ñ¡”…ÑÑ•µÁÑ•=‰©•Ð°MeM€°É…ÜI€°Í±½Ñ€°…¹…ÁÁ±¥…‰±”…‘‘É•ÍÌÉÕ±”Ý¡•¸É•Á½ÉÑ¥¹œÑ¡”™…¥±ÕÉ”¸()Q¡”…‘‘É•ÍÌÝÉ¥Ñ”¥Ì½ÁÑ¥½¹…°…¹É•Á•…Ñ…‰±”Ý¥Ñ¡¥¸½¹™-=€¸=µ¥ÍÍ¥½¸…¸‰”Ù…±¥™½È…¸=‰©•ÐÝ¥Ñ¡½ÕÐ…¸…‘‘É•ÍÌì¥ÐµÕÍÐ¹½Ð‰”ÕÍ•Ñ¼¥¹™•ÈÑ¡…Ð•Ù•ÉäÕ¹…‘‘É•ÍÍ•5½‘Õ±”¥Ì•ÉÉ½¹•½ÕÌ¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀäÈ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½…É¡¥Ñ•ÑÕÉ”¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒAÉ½É…µµ¥¹œÉ¡¥Ñ•ÑÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÈéÌÀÀÀÀÀÅ€()Q¡”ÁÉ½É…µµ¥¹œÁÉ½Ñ½½°¥Ì„µ…¹…•µ•¹Ð±…å•È…ÉÉ¥•¥¸=Á•¹]•‰9•Ð™É…µ•Ì¸%ÐÍ•±•ÑÌ½¹”¥¹ÍÑ…±±•A¡åÍ¥…°•Ù¥”°É••¥Ù•Ì…¸¥¹¥Ñ¥…°ÍÑ…Ñ”ÁÉ½©•Ñ¥½¸°ÉÕ¹ÌÁÉ½É…µµ¥¹œÍ•ÅÕ•¹•Ì±…‰•±±•Ù¥ÉÑÕ…°½È…‘Ù…¹•¥¸=A8¹‘‰€°…¹±½Í•ÌÑ¡”ÁÉ½É…µµ¥¹œÍ•ÍÍ¥½¸¸((ŒŒŒ5…¹…•ÍåÍÑ•µÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÈéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()Q¡”½µµ½¸ÁÉ½É…µµ¥¹œ½Á•É…Ñ¥½¹Ì…É”…ÍÍ½¥…Ñ•¥¸=A8¹‘‰€Ý¥Ñ Ñ¡”Í…µ”µ…¹…•ÍåÍÑ•µÌÑ¡…Ð•áÁ½Í”Ñ¡”½µµ½¸‘¥…¹½ÍÑ¥ŒÍÕÉ™…”è()ð¥…¹½ÍÑ¥Œ½ÁÉ½É…µµ¥¹œ]!=€ð=A8¹‘‰€ÍåÍÑ•´ð)ð€´´´ð€´´´ð)ð€ÄÀÀÅ€ð1¥¡Ð…¹ÕÑ½µ…Ñ¥½¸ÍåÍÑ•´ð)ð€ÄÀÀÑ€ðQ¡•Éµ½É•Õ±…Ñ¥½¸ð)ð€ÄÀÄá€ð¹•Éä5…¹…•µ•¹ÐÍåÍÑ•´ð)ð€ÄÀÈÍ€ð•ÍÌ½¹ÑÉ½°ð()ÍÍ½¥…Ñ¥½¸¥¸=A8¹‘‰€•ÍÑ…‰±¥Í¡•ÌÑ¡…ÐÑ¡”Ñ•µÁ±…Ñ•Ì‰•±½¹œÑ¼Ñ¡½Í”ÍåÍÑ•´É•½É‘Ì¸%Ð‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…Ð•Ù•Éä•Ù¥”½È™¥ÉµÝ…É”¥µÁ±•µ•¹ÑÌ•Ù•ÉäÍ•¹…É¥¼½È½ÁÑ¥½¹…°™É…µ”¸()Ì¥¸‘¥…¹½ÍÑ¥Ì°]!<€ÄÀÀÅ€½Ù•ÉÌÑ¡”‰É½…‘•È1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸µ…¹…•µ•¹Ð™…µ¥±ä•Ù•¸Ñ¡½Õ Ñ¡”±¥Ñ•É…°9}MeMQ4¹Ý¡½€Ù…±Õ”½¸Ñ¡”½µ‰¥¹•ÍåÍÑ•´É½Ü¥Ì€Å€¸¼¹½Ðµ…¹Õ™…ÑÕÉ”„Í•½¹‘…Ñ…‰…Í”…ÍÍ½¥…Ñ¥½¸™½È™Õ¹Ñ¥½¹…°]!<€É€¸((ŒŒŒA…ÉÑ¥¥Á…¹ÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÈéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()ðA…ÉÑ¥¥Á…¹ÐðI•ÍÁ½¹Í¥‰¥±¥Ñäð)ð€´´´ð€´´´ð)ðAÉ½É…µµ•ÈðÉ•Í½±Ù•Ì…Á…‰¥±¥Ñä°Í•±•ÑÌÑ¡”•Ù¥”°Ù…±¥‘…Ñ•ÌÙ…±Õ•Ì°Í•¹‘ÌÝÉ¥Ñ•Ì°…¹±½Í•Ì½È…‰½ÉÑÌð)ð•Ù¥”ðÉ•Á½ÉÑÌ¥‘•¹Ñ¥Ñä…¹¥¹ÍÑ…±±•ÍÑ…Ñ”°…•ÁÑÌ½ÈÉ•©•ÑÌÝÉ¥Ñ•Ì°…¹É•Á½ÉÑÌ½µÁ±•Ñ¥½¸ð)ð…Ñ•Ý…ä½ÑÉ…¹ÍÁ½ÉÐð…ÉÉ¥•Ì™É…µ•Ì…¹ÁÉ•Í•ÉÙ•Ì‘¥É•Ñ¥½¸ì¥Ð‘½•Ì¹½ÐÙ…±¥‘…Ñ”…Ñ…±½Õ”Í•µ…¹Ñ¥Ìð)ð…Ñ…±½Õ”É•Í½±Ù•Èðµ…ÁÌ•Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°=‰©•Ð°…‘‘É•ÍÌ°…¹½¹™¥ÕÉ…Ñ¥½¸½¹ÍÑÉ…¥¹ÑÌ‰•™½É”ÑÉ…¹Íµ¥ÍÍ¥½¸ð()Q¡”Ý¥É”ÁÉ½Ñ½½°¡…Ì¹¼ÑÉ…¹Í…Ñ¥½¸¥‘•¹Ñ¥™¥•È¸ÁÉ½É…µµ•ÈÍ¡½Õ±Í•É¥…±¥é”…µ‰¥Õ½ÕÌÁÉ½É…µµ¥¹œ½Á•É…Ñ¥½¹Ì½¸½¹”½¹¹•Ñ¥½¸…¹É•Ñ…¥¸Ñ¡”…Ñ¥Ù”]!=€°•Ù¥”Í•±•Ñ½È°Í•¹…É¥¼°Í•ÅÕ•¹”°…¹Í±½Ñ€½¹Ñ•áÐ¸((ŒŒŒQ¡É•”±…å•ÉÌ½˜ÍÑ…Ñ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÈéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()ð1…å•ÈðÍÑ…‰±¥Í¡•‰äð)ð€´´´ð€´´´ð)ð…Ñ…±½Õ”…Á…‰¥±¥Ñäð5!…Ñ…±½Õ”¹‘‰€™¥ÉµÝ…É”°Í±½ÑÌ°=‰©•ÑÌ°Y¥É¥¸=‰©•ÑÌ°½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¹Ì°™¥±Ñ•ÉÌ°…¹ÉÕ±•Ìð)ðAÉ½É…µµ¥¹œÉ•ÅÕ•ÍÐð™É…µ•ÌÍ•¹Ð‘ÕÉ¥¹œ½¹™½¹™¥ÕÉ…Ñ½ÉÍ€½È½¹™-=€ð)ð™™•Ñ¥Ù”¥¹ÍÑ…±±•ÍÑ…Ñ”ð„™É•Í ‘¥…¹½ÍÑ¥Œ¥¹Ñ•ÉÙ¥•Ü…™Ñ•ÈÁÉ½É…µµ¥¹œð()É•ÅÕ•ÍÐ…¸‰”Íå¹Ñ…Ñ¥…±±äÙ…±¥Ý¡¥±”‰•¥¹œÍ•µ…¹Ñ¥…±±ä¥¹Ù…±¥™½ÈÑ¡”É•Í½±Ù••Ù¥”¸½¹Ù•ÉÍ•±ä°„Á½Í¥Ñ¥Ù”ÁÉ½É…µµ¥¹œÉ•ÍÁ½¹Í”•ÍÑ…‰±¥Í¡•ÌÁÉ½Ñ½½°…•ÁÑ…¹”°¹½Ð¹••ÍÍ…É¥±ä½µÁ±•Ñ”‘¥…¹½ÍÑ¥ŒÙ•É¥™¥…Ñ¥½¸¸((ŒŒŒ=A8¹‘‰€Ù¥ÉÑÕ…°…¹…‘Ù…¹•ÁÉ½É…µµ¥¹œÍ•ÅÕ•¹•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÈéÌÀÀÀÀÀÕ€((ŒŒŒŒY¥ÉÑÕ…°µ½¹™¥ÕÉ…Ñ½ÈÑÉ…¹Í™•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÈéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()½¹™½¹™¥ÕÉ…Ñ½ÉÍ€ÝÉ¥Ñ•ÌÑÝ•±Ù”ÑÉ…¹ÍÁ½ÉÐÁ½Í¥Ñ¥½¹Ì¥¸ÑÝ¼™É…µ•Ìè((´€¨m]!=t¨À¨ŒÐ©mÅt©mÉt©mÍt©mÑt©mÕt©mÙtŒ€(´€¨m]!=t¨À¨ŒÔ©mÝt©mát©måt©mÄÁt©mÄÅt©mÄÉtŒ€()… Ù…±Õ”¡…ÌÑ¡”=A8¹‘‰€ÑÉ…¹ÍÁ½ÉÐÉ…¹”€À¸¸ÈÔÕ€¸9}=9€É•Á½ÉÑÌÑ¡”¹Õµ‰•È½˜Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹ÌÁÉ½Ù¥‘•‰äÑ¡”•Ù¥”°‰ÕÐ¹¼…¹½¹¥…°É•±…Ñ¥½¸µ…ÁÌÄ¸¹ÄÉ€Õ¹¥Ù•ÉÍ…±±äÑ¼™¥ÉµÝ…É”9}=9€‘•™¥¹¥Ñ¥½¹Ì½ÈÁÉ½É•ÍÍ¥Ù•€½É‘•É¥¹œ¸¼¹½Ð•ÅÕ…Ñ”„ÑÉ…¹ÍÁ½ÉÐ™¥•±Ý¥Ñ „Á¡åÍ¥…°Á±Õœ½È…Ñ…±½Õ”Á½Í¥Ñ¥½¸Ý¥Ñ¡½ÕÐ¥¹‘•Á•¹‘•¹Ð½ÉÉ•±…Ñ¥½¸¸((ŒŒŒŒ‘Ù…¹•=‰©•ÐÑÉ…¹Í™•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÈéÌÀÀÀÀÀÝ€()½¹™-=€É•‰Õ¥±‘ÌÑ¡”•Ù¥”Ì5½‘Õ±”½=‰©•ÐÁÉ½©•Ñ¥½¸ÕÍ¥¹œè((´%59M%=8€ÌÁ€™½ÈÍ±½Ñ€°•¹…‰±•½‘¥Í…‰±•5½‘Õ±”ÍÑ…Ñ”°…¹É•Õ±…È=‰©•Ð½ÈY¥É¥¸=‰©•Ðì(´%59M%=8€ÌÉ€™½ÈÍåÍÑ•´½…‘‘É•ÍÌì(´%59M%=8€ÌÕ€™½È¥¹‘•á•½¹™¥ÕÉ…Ñ¥½¸Ù…±Õ•Ì¸()Q¡”Í•ÅÕ•¹”‰•¥¹ÌÝ¥Ñ „µ…¹‘…Ñ½ÉäÉ•Í•Ðµ…±°µ=‰©•ÑÌ½µµ…¹…¹•¹‘ÌÝ¥Ñ „µ…¹‘…Ñ½ÉäÁÉ½É…µµ•È•¹µ½˜µÑÉ…¹Íµ¥ÍÍ¥½¸™É…µ”¸Q¡¥Ìµ…­•ÌÑ¡”…¹½¹¥…°Í•ÅÕ•¹”„É•Á±…•µ•¹ÐµÍÑå±”ÑÉ…¹Í™•È°¹½Ð…¸¥Í½±…Ñ•Á…Ñ ½Á•É…Ñ¥½¸¸()=A8¹‘‰€…±Í¼É•¥ÍÑ•ÉÌ„É•Í•Ðµ½¹”µÍ±½Ð½µµ…¹°‰ÕÐÑ¡”…¹½¹¥…°½¹™-=€Í•ÅÕ•¹”ÕÍ•ÌÉ•Í•Ðµ…±°¸((ŒŒŒ¥É•Ñ¥½¸…¹…­¹½Ý±•‘•µ•¹Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÈéÌÀÀÀÀÀá€()9}=A8¹½Á•¹}ÑåÁ•€‘¥ÍÑ¥¹Õ¥Í¡•ÌÁÉ½É…µµ•ÈµÑ¼µ•Ù¥”…¹•Ù¥”µÑ¼µÁÉ½É…µµ•È™É…µ•Ì¸M•ÅÕ•¹”É½ÝÌ…‘‘¥Ñ¥½¹…±±ä‘•™¥¹”µ…¹‘…Ñ½Éä°É•Á•…Ñ•°•ÉÉ½È°9-€°…¹Ñ¥µ•½ÕÐÑÉ…¹Í¥Ñ¥½¹Ì¸()=É‘¥¹…Éä-€…¹9-€Ñ•µÁ±…Ñ•Ì•á¥ÍÐ¥¸=A8¹‘‰€‰ÕÐ…É”¹½Ð±¥ÍÑ•…Ì½É‘¥¹…Éä½É‘•É•µ•µ‰•ÉÌ½˜Ñ¡”Í¥àÁÉ½É…µµ¥¹œÍ•ÅÕ•¹•Ì¸M}=A9}MEU9¹ÍÑ…ÑÕÌÑ¹…­€¹•Ù•ÉÑ¡•±•ÍÌ…ÍÍ¥¹ÌÍÑ…Ñ”ÑÉ…¹Í¥Ñ¥½¹Ì™½È9-€¸ÍÑ…Ñ”µµ…¡¥¹”¥µÁ±•µ•¹Ñ…Ñ¥½¸µÕÍÐÑ¡•É•™½É”¡…¹‘±”…­¹½Ý±•‘•µ•¹ÐÍÑ…ÑÕÌÍ•Á…É…Ñ•±ä™É½´½É‘•É•™É…µ”µ•µ‰•ÉÍ¡¥À¸((ŒŒŒM½ÕÉ”É•½¹¥±¥…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÈéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()ðM½ÕÉ”ð½¹ÑÉ¥‰ÕÑ¥½¸ð)ð€´´´ð€´´´ð)ð=A8¹‘‰€ðÍ•¹…É¥½Ì°™É…µ•Ì°‘¥É•Ñ¥½¸°Á…É…µ•Ñ•ÈÉ…¹•Ì°É•Á•Ñ¥Ñ¥½¸°•ÉÉ½ÉÌ°…¹Ñ¥µ•½ÕÑÌð)ð=Á•¹EÕ•Éä¹ÑáÑ€ðÅÕ•É¥•ÌÕÍ•Ñ¼…ÍÍ•µ‰±”Í•¹…É¥½Ì…¹ÍÑ…Ñ”µ…¡¥¹•Ìð)ð5!…Ñ…±½Õ”¹‘‰€ð•Ù¥”½™¥ÉµÝ…É”…Á…‰¥±¥Ñä…¹Ù…±Õ”½¹ÍÑÉ…¥¹ÑÌð)ðÉÕ±•Ì¹‘ˆÍ€ðÍ•±•Ñ•Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°±¥¹­•µÁ…É…µ•Ñ•ÈÉÕ±•Ìð)ðAÕ‰±¥Œ=Á•¹]•‰9•ÐAÌð½µµ½¸™É…µ”Íå¹Ñ…à…¹™Õ¹Ñ¥½¹…°ÍåÍÑ•´‰•¡…Ù¥½Èð)ð=‰Í•ÉÙ•ÑÉ…™™¥Œð…ÑÕ…°½É‘•É¥¹œ°½ÁÑ¥½¹…±¥Ñä°…¹•Ù¥”µÍÁ•¥™¥ŒÍÕÁÁ½ÉÐð)ð5å!=5}MÕ¥Ñ”U$ðÍ•±•Ñ…‰±”Ù…±Õ•Ì°Ý½É­™±½ÜÍÑ…Ñ”°…¹ÁÉ•Í•¹Ñ…Ñ¥½¸ð()=A8¹‘ˆ¹‘¥…}½Á•¹€¥Ì‰É½…‘•ÈÑ¡…¸‘¥…¹½ÍÑ¥Ìè¥Ðµ…É­ÌÑ¡•Í”ÁÉ½É…µµ¥¹œ™É…µ•Ì…ÌÝ•±°¸M•ÅÕ•¹”µ•µ‰•ÉÍ¡¥À°‘¥É•Ñ¥½¸°…¹Í•¹…É¥¼ÑåÁ”µÕÍÐ‰”ÕÍ•Ñ¼±…ÍÍ¥™ä…¸½Á•É…Ñ¥½¸¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀäÌ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½½¹™¥ÕÉ…Ñ¥½¸µÁÉ½É…µµ¥¹œ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒ½¹™¥ÕÉ…Ñ¥½¸AÉ½É…µµ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÌéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()½¹™¥ÕÉ…Ñ¥½¸ÁÉ½É…µµ¥¹œÝÉ¥Ñ•Ì¥¹‘•á•=‰©•Ð½È™¥ÉµÝ…É”ÁÉ½Á•ÉÑ¥•Ì…™Ñ•ÈÑ¡”•Ù¥”°™¥ÉµÝ…É”°Í±½Ñ€°…¹Ñ…É•Ð=‰©•Ð¡…Ù”‰••¸É•Í½±Ù•¸((ŒŒŒ]É¥Ñ”™É…µ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÌéÌÀÀÀÀÀÉ€()€¨m]!=t¨À¨ŒÌÔm%9atmM1=Qt©mY1}AItŒ€()ð¥•±ð=A8¹‘‰€É…¹”ð5•…¹¥¹œð)ð€´´´ð€´´´ð€´´´ð)ð%9a€ð€À¸¸ÈÔÕ€ð½¹™¥ÕÉ…Ñ¥½¸¥¹‘•àð)ðM1=Q€ð€Ä¸¸ÈÔÕ€ð•Ù¥”µ±½…°Í±½Ñ€ð)ðY1}AI€ð€À¸¸ØÔÔÌÕ€ð•¹½‘•Ù…±Õ”ð()%9a€½ÉÉ•±…Ñ•ÌÝ¥Ñ 9}=9¹¥‘á€‰ÕÐ¥Ì¹½Ð±½‰…±±äÕ¹¥ÅÕ”¸((ŒŒŒI•Í½±Ù¥¹œ„ÁÉ½Á•ÉÑä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÌéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€((Ä¸I•Í½±Ù”Ñ¡”¥¹ÍÑ…±±••Ù¥”…¹™¥ÉµÝ…É”¸(È¸I•Í½±Ù”M1=Q€…¹Ñ¡”Ñ…É•Ð=‰©•ÐÍ•±•Ñ••…É±¥•È¥¸Ñ¡”ÑÉ…¹Í™•È¸(Ì¸¥¹=‰©•ÐµÍ½Á•‘•™¥¹¥Ñ¥½¹ÌÝ¥Ñ Ñ¡”=‰©•ÐÌ¥‘}­•å}½‰©•Ñ€…¹¥‘}™¥ÉµÝ…É”€ô€Á€¸(Ð¸¥¹…ÁÁ±¥…‰±”™¥ÉµÝ…É”µÍ½Á•‘•™¥¹¥Ñ¥½¹ÌÝ¥Ñ ¥‘}­•å}½‰©•Ð€ô€Á€…¹Ñ¡”É•Í½±Ù•™¥ÉµÝ…É”¸(Ô¸M•±•Ð‘•™¥¹¥Ñ¥½¹ÌÝ¡½Í”¥‘á€•ÅÕ…±Ì%9a€¸(Ø¸ÁÁ±ä™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¹Ì°½¹Ù•ÉÍ¥½¹Ì°…¹Ù…±Õ”•¹½‘¥¹œ¸(Ü¸I•Ñ…¥¸Ñ¡”É•Í½±Ù•9}=9¹¥‘}½¹™€Ý¥Ñ Ñ¡”ÑÉ…¹Íµ¥ÑÑ•ÑÕÁ±”¸()¼¹½ÐÉ•ÅÕ¥É”½¹”9}=9€É½ÜÑ¼½¹Ñ…¥¸‰½Ñ „Ù…±¥=‰©•Ð…¹™¥ÉµÝ…É”­•äìÑ¡”Í½Á•Ì…É”µÕÑÕ…±±ä•á±ÕÍ¥Ù”¥¸Ñ¡”…¹½¹¥…°…Ñ…±½Õ”¸((ŒŒŒŒ=‰©•Ð…¹™¥ÉµÝ…É”Í½Á•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÌéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°¹½Ð…ÁÁ±¥…‰±•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€()9}=9€ÕÍ•Ì€Á€…Ì„ƒŠq¹½Ð…ÁÁ±¥…‰±—ŠtÍ•¹Ñ¥¹•°½¸Ñ¡”Õ¹ÕÍ•½Ý¹•ÉÍ¡¥À…á¥Ìè()ðM½Á”ð¥‘}­•å}½‰©•Ñ€ð¥‘}™¥ÉµÝ…É•€ð)ð€´´´ð€´´´ð€´´´ð)ð=‰©•ÐÁÉ½Á•ÉÑäðÉ•Í½±Ù•=‰©•Ð%ð€Á€ð)ð¥ÉµÝ…É”ÁÉ½Á•ÉÑäð€Á€ðÉ•Í½±Ù•™¥ÉµÝ…É”%ð()Q¡”é•É¼Ù…±Õ•Ì‘¼¹½Ð¥‘•¹Ñ¥™ä=‰©•Ð€À½È™¥ÉµÝ…É”€À¸Q¡•äÑ…­”Ñ¡”Á±…”½˜9U11€…¹‘¥ÍÑ¥¹Õ¥Í Ý¡¥ •¹Ñ¥Ñä½Ý¹ÌÑ¡”‘•™¥¹¥Ñ¥½¸¸ÁÁ±¥…‰±”‘•™¥¹¥Ñ¥½¹ÌµÕÍÐÑ¡•É•™½É”‰”½±±•Ñ•…ÌÑ¡”Õ¹¥½¸½˜Ñ¡”ÑÝ¼Í½Á•Ìè()ÍÅ°)M1P€¨)I=49}=9)]!I€¡¥‘}­•å}½‰©•Ð€ô€é½‰©•Ñ}¥9¥‘}™¥ÉµÝ…É”€ô€À¤(€€=H€¡¥‘}­•å}½‰©•Ð€ô€À9¥‘}™¥ÉµÝ…É”€ô€é™¥ÉµÝ…É•}¥¤)€()ÅÕ•ÉäÉ•ÅÕ¥É¥¹œ‰½Ñ É•Í½±Ù•%Ì¥¸Ñ¡”Í…µ”É½ÜÝ½Õ±µ¥ÍÌÑ¡”…¹½¹¥…°‘•™¥¹¥Ñ¥½¹Ì¸I•Í½±Ù”Ñ¡”Í½Á”‰•™½É”¥¹Ñ•ÉÁÉ•Ñ¥¹œ¥‘á€°‰•…ÕÍ”…¸¥¹‘•à¥Ì¹½Ð±½‰…±±äÕ¹¥ÅÕ”¸()Q¡¥ÌÕ¹¥½¸Í•±•ÑÌ…¹‘¥‘…Ñ”‘•™¥¹¥Ñ¥½¹Ì°¹½ÐÁ•Éµ¥ÍÍ¥½¸Ñ¼ÝÉ¥Ñ”…±°½˜Ñ¡•´¸¥ÉµÝ…É”Á¡åÍ¥…°™¥•±‘ÌÝ¥Ñ ¥‘à€ô€´Å€¡…Ù”¹¼É•ÁÉ•Í•¹Ñ…Ñ¥½¸¥¸Ñ¡”Õ¹Í¥¹•%9a€É…¹”…‰½Ù”¸ÍÑ…‰±¥Í Ñ¡”…ÁÁ±¥…‰±”ÑÉ…¹Í™•Èµ•¡…¹¥Í´…¹•¹½‘¥¹œÍ•Á…É…Ñ•±ä‰•™½É”•µ¥ÑÑ¥¹œ„ÁÉ½Á•ÉÑä¸((ŒŒŒQÉ…¹Í™•È‰•¡…Ù¥½È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÌéÌÀÀÀÀÀÕ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€°Ý…É¹¥¹€()A…É…µ•Ñ•ÈÝÉ¥Ñ•Ì…É”½ÁÑ¥½¹…°…¹É•Á•…Ñ…‰±”Ý¥Ñ¡¥¸½¹™-=€¸9-€ÑÉ…¹Í¥Ñ¥½¹ÌÑ¡”…¹½¹¥…°Í•ÅÕ•¹”Ñ¼]…É¹¥¹œÉ…Ñ¡•ÈÑ¡…¸ÉÉ½È¸()Q¡”•Ù¥”…¸É•Á½ÉÐè()€¨m]!=t©m]!It¨Ìä©mM1=Qt©m%9at©mII=ItŒ€()=A8¹‘‰€±…ÍÍ¥™¥•ÌÑ¡¥Ì…Ì•ÉÉ½Èµ…¹µ¥¹™½Éµ…Ñ¥½¸‰•…ÕÍ”„•Ù¥”…¸±•…Ù”Í½µ”Á…É…µ•Ñ•ÉÌÕ¹µ…¹…•Ý¥Ñ¡½ÕÐÍÑ½ÁÁ¥¹œÑ¡”Ý¡½±”½¹™¥ÕÉ…Ñ¥½¸¸Q¡”Í•ÅÕ•¹”µ…ÁÌ¥ÐÑ¼]…É¹¥¹œ¸AÉ•Í•ÉÙ”•… Ý…É¹¥¹œ‰äM1=Q€…¹%9a€ì‘¼¹½Ð‘¥Í…ÉÑ¡”É•ÍÐ½˜Ñ¡”…•ÁÑ•½¹™¥ÕÉ…Ñ¥½¸¸((ŒŒŒY…±Õ”™½ÉµÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÌéÌÀÀÀÀÀÙ€()•Á•¹‘¥¹œ½¸Ñ¡”É•Í½±Ù•‘•™¥¹¥Ñ¥½¸°Y1}AI€…¸•¹½‘”è((´…¸•¹Õµ•É…Ñ¥½¸ì(´„¹Õµ•É¥ŒÉ…¹”ì(´„Á…‘‘•Ù…±Õ”ì(´„‰½½±•…¸ì(´„™¥á•Ù…±Õ”ì(´„ÕÍ•ÈµÍÕÁÁ±¥•Ù…±Õ”ì(´„Ù…±Õ”É•ÅÕ¥É¥¹œ„½¹Ù•ÉÍ¥½¸ÉÕ±”¸()Q¡”ÑÉ…¹ÍÁ½ÉÐµ…á¥µÕ´‘½•Ì¹½Ð½Ù•ÉÉ¥‘”9}=9}I9€°9}%1QI}I9€°½È±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì¸((ŒŒŒA¡åÍ¥…°½Õ¹Ñ•ÉÁ…ÉÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÌéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()¸¥¹‘•á•ÁÉ½Á•ÉÑä…¸½ÉÉ•ÍÁ½¹Ñ¼„Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¸•Ù•¸Ý¡•¸Ñ¡”Íåµ‰½±Ì‘¥™™•È¸½È•á…µÁ±”°™¥ÉµÝ…É”€ÄäÉ€ÕÍ•ÌÁ¡åÍ¥…°QeA€…¹AI€Á½Í¥Ñ¥½¹ÌÝ¡¥±”Í¡ÕÑÑ•È…ÑÕ…Ñ½È=‰©•Ð€ÈÄá€ÕÍ•Ì¥¹‘•á•M!UQQI}QeA€…¹AIMQ}9U5	I€ÁÉ½Á•ÉÑ¥•Ì¸()Á¡åÍ¥…°½Õ¹Ñ•ÉÁ…ÉÐ‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…ÐÑ¡”¥¹ÍÑ…±±•Ù…±Õ”Ý…ÌÁ¡åÍ¥…±±ä½¹™¥ÕÉ•°…¹Á¡åÍ¥…°…¹…‘Ù…¹••¹½‘¥¹Ì¹••¹½ÐÕÍ”Ñ¡”Í…µ”É…¹”¸()A¡åÍ¥…°µÁÉ½Á•ÉÑä½ÉÉ•ÍÁ½¹‘•¹”¥ÌÍ•Á…É…Ñ”™É½´Á¡åÍ¥…°Ñ½Á½±½äÍ•±•Ñ¥½¸¸]¡•¸Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÙ…±Õ•Ì‘•Ñ•Éµ¥¹”Ý¡¥ =‰©•Ð•á¥ÍÑÌ¥¸„Í±½Ð°É•Í½±Ù”Ñ¡”Ñ½Á½±½ä™¥ÉÍÐÝ¥Ñ m…Ñ…±½Õ”I•Í½±ÕÑ¥½¹t ¸¸½¥¹Ñ•É¹…±Ì½…Ñ…±½Õ”µÉ•Í½±ÕÑ¥½¸¹µÁ¡åÍ¥…°µ½¹™¥ÕÉ…Ñ¥½¸µÉ•Í½±ÕÑ¥½¸¤°Ñ¡•¸•Ù…±Õ…Ñ”Ñ¡”Í•±•Ñ•=‰©•ÐÌÁÉ½Á•ÉÑä½¹Ù•ÉÍ¥½¹Ì¸()M•”m½¹™¥ÕÉ…Ñ¥½¹t ¸¸½‘•Ù¥”µµ½‘•°½½¹™¥ÕÉ…Ñ¥½¸¹µ¤°mAÉ½É…µµ¥¹œY…±¥‘…Ñ¥½¹t¡Ù…±¥‘…Ñ¥½¸¹µ¤°…¹‘¥…¹½ÍÑ¥Œm%59M%=8€ÌÕt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´ÌÔµ½¹™¥ÕÉ…Ñ¥½¸¹µ¤¸((ŒŒŒMÁ•¥…°Á…É…µ•Ñ•ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÌéÌÀÀÀÀÀá€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()¥…¹½ÍÑ¥Œ%59M%=8€ÌÄÁ€…ÉÉ¥•Ì…¸=‰©•ÐµÍÁ•¥™¥ŒÙ…±Õ”Ý¥Ñ¡½ÕÐ%9a€¸=A8¹‘‰€ÁÉ½Ù¥‘•Ì¹¼½ÉÉ•ÍÁ½¹‘¥¹œ•¹•É¥ŒÁÉ½É…µµ¥¹œÝÉ¥Ñ”¥¸½¹™-=€¸¼¹½Ð™½É”¥Ð¥¹Ñ¼%59M%=8€ÌÕ€ÁÉ½É…µµ¥¹œÝ¥Ñ¡½ÕÐ=‰©•ÐµÍÁ•¥™¥Œ•Ù¥‘•¹”¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀäÐ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½‘•Ù¥”µÍ•±•Ñ¥½¸¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒ•Ù¥”M•±•Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÐéÌÀÀÀÀÀÅ€()AÉ½É…µµ¥¹œ‰•¥¹Ì‰äÍ•±•Ñ¥¹œ½¹”¥¹ÍÑ…±±•A¡åÍ¥…°•Ù¥”Ý¥Ñ¡¥¸„µ…¹…•µ•¹Ð]!=€¸Q¡”…¹½¹¥…°Í•¹…É¥½ÌÍÕÁÁ½ÉÐÍ•±•Ñ¥½¸‰ä‘¥…¹½ÍÑ¥Œ…‘‘É•ÍÌ°‰ä€ÌÈµ‰¥Ð•Ù¥”%°½ÈÑ¡É½Õ „±½…°µ¥¹Ñ•É…Ñ¥½¸Ý½É­™±½Ü¸((ŒŒŒM•±•Ñ¥½¸™É…µ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÐéÌÀÀÀÀÀÉ€()ð5•Ñ¡½ðÉ…µ”ð¥ÉÍÐµÉ•ÍÁ½¹Í”Ý¥¹‘½Üð)ð€´´´ð€´´´ð€´´´ð)ð‘‘É•ÍÌð€©m]!=t¨Ä©m]!ItŒ€ð€ÄÔÌð)ð•Ù¥”%ð€©m]!=t¨äm%t¨ÀŒ€ð€ÄÔÌð)ð1½…°µ¥¹Ñ•É…Ñ¥½¸Í•¹…É¥¼ð€©m]!=t¨Ä©m]!ItŒ€ð€ÌÀÀÌð()Q¡”•Ù¥”%¡…ÌÑ¡”=A8¹‘‰€É…¹”€À¸¸ÐÈäÐäØÜÈäÕ€¸=‰Í•ÉÙ•¥¹Ñ•É™…•ÌÉ•¹‘•È¥Ð…Ì•¥¡Ð¡•á…‘•¥µ…°¡…É…Ñ•ÉÌìÑ¡”Ý¥É”Ñ•µÁ±…Ñ”…ÉÉ¥•ÌÑ¡”%€™¥•±Ý¥Ñ¡½ÕÐ‘•™¥¹¥¹œÑ¡…Ð‘¥ÍÁ±…äÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸¸((ŒŒŒM•±•Ñ¥¹œ‰ä•Ù¥”%()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÐéÌÀÀÀÀÀÍ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()UÍ”Ñ¡”¥¹ÍÑ…±±•¥¹ÍÑ…¹”¥‘•¹Ñ¥™¥•ÈÉ•ÑÕÉ¹•‰ä‘¥…¹½ÍÑ¥Œ%59M%=8€ÄÍ€¸¼¹½ÐÍÕ‰ÍÑ¥ÑÕÑ”è((´9}Y%¹¥‘}‘•Ù¥•€ì(´9}%Q4¹¥‘}¥Ñ•µ€ì(´=	)Q}5=1€ì(´„5½‘Õ±”…‘‘É•ÍÌì(´„…Ñ…±½Õ”M-T¸()Q¡”%µ‰…Í•Í•¹…É¥¼ÁÉ½••‘ÌÑ¼…‘Ù…¹•=‰©•Ð½¹™¥ÕÉ…Ñ¥½¸¸%Ð‘½•Ì¹½Ð¥¹±Õ‘”Ñ¡”Ù¥ÉÑÕ…°µ½¹™¥ÕÉ…Ñ½ÈÍ•ÅÕ•¹”¸((ŒŒŒM•±•Ñ¥¹œ‰ä…‘‘É•ÍÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÐéÌÀÀÀÀÀÑ€()]!I€™½±±½ÝÌÑ¡”Í•±•Ñ•µ…¹…•µ•¹Ð™…µ¥±äÌ…‘‘É•ÍÌÉ…µµ…È¸%Ð¥Ì¹½Ð½¹”Õ¹¥Ù•ÉÍ…°¥¹Ñ••È…¹µÕÍÐ‰”•¹•É…Ñ•™É½´Ñ¡”…ÁÁ±¥…‰±”=A8¹‘‰€…‘‘É•ÍÌÉÕ±”¸()A¡åÍ¥…°•Ù¥”…¸•áÁ½Í”Í•Ù•É…°5½‘Õ±•Ì…¹™Õ¹Ñ¥½¹…°…‘‘É•ÍÍ•Ì¸Q¡”‘¥…¹½ÍÑ¥Œ½ÁÉ½É…µµ¥¹œÍ•±•Ñ¥½¸…‘‘É•ÍÌµÕÍÐÑ¡•É•™½É”É•µ…¥¸‘¥ÍÑ¥¹Ð™É½´Á•Èµ5½‘Õ±”…‘‘É•ÍÍ•ÌÝÉ¥ÑÑ•¸Ñ¡É½Õ %59M%=8€ÌÉ€¸=‰Í•ÉÙ•]!<€ÄÀÀÅ€ÑÉ…™™¥Œ½™Ñ•¸½ÉÉ•±…Ñ•ÌÑ¡”•Ù¥”½¹Ñ•áÐÝ¥Ñ Í±½Ñ€€Å€°‰ÕÐÑ¡¥Ì¥Ì¹½Ð„Õ¹¥Ù•ÉÍ…°ÉÕ±”¸()Q¡”…‘‘É•ÍÌµÍ•±•Ñ•ÁÉ½É…µµ¥¹œÍ•¹…É¥¼ÁÉ½••‘ÌÑ¼Ù¥ÉÑÕ…°µ½¹™¥ÕÉ…Ñ½ÈÑÉ…¹Í™•È…¹‘½•Ì¹½Ð¥¹±Õ‘”½¹™-=€¸((ŒŒŒ1½…°µ¥¹Ñ•É…Ñ¥½¸Í•±•Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÐéÌÀÀÀÀÀÕ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()Q¡”½¹™1½…±	ÕÑÑ½¹€Í•ÅÕ•¹”ÕÍ•ÌÑ¡”Í…µ”ÍÑ…ÉÐ™É…µ”…¹É•ÍÁ½¹Í”½É‘•È…Ì½¹™‘‘É•ÍÍ•‘€‰ÕÐ…ÍÍ¥¹Ì„€ÌÀÀµÍ•½¹™¥ÉÍÐµÉ•ÍÁ½¹Í”Ý¥¹‘½Ü¸%ÑÌÍ•¹…É¥¼Ñ¡•¸Á•Éµ¥ÑÌ…‘Ù…¹•=‰©•Ð½¹™¥ÕÉ…Ñ¥½¸™½±±½Ý•‰äÙ¥ÉÑÕ…°µ½¹™¥ÕÉ…Ñ½ÈÑÉ…¹Í™•È¸()Q¡”‘…Ñ…‰…Í”¹…µ”•ÍÑ…‰±¥Í¡•Ì„±½…°µ‰ÕÑÑ½¸Ý½É­™±½ÜìÑ¡”™É…µ”‘½•Ì¹½Ð•¹½‘”Ñ¡”Á¡åÍ¥…°¥¹Ñ•É…Ñ¥½¸¸¸¥µÁ±•µ•¹Ñ…Ñ¥½¸µÕÍÐ½½É‘¥¹…Ñ”Ñ¡”¥¹ÍÑ…±±•È…Ñ¥½¸½ÕÑÍ¥‘”Ñ¡”=Á•¹]•‰9•ÐÁ…å±½……¹µÕÍÐ¹½Ð¥¹™•ÈÝ¡¥ •Ù¥”Ý…ÌÍ•±•Ñ•Í½±•±ä™É½´Ñ¡”±½¹œÑ¥µ•½ÕÐ¸((ŒŒŒ%¹¥Ñ¥…°¥‘•¹Ñ¥Ñä¡•­Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÐéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()	•™½É”ÑÉ…¹Íµ¥ÑÑ¥¹œ½¹™¥ÕÉ…Ñ¥½¸°½µÁ…É”Ñ¡”É•ÑÕÉ¹•¥¹¥Ñ¥…°ÁÉ½©•Ñ¥½¸Ý¥Ñ Ñ¡”¥¹Ñ•¹‘•Ñ…É•Ðè((´%59M%=8€Å€¥Ñ•´½µ½‘•°°Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½È½Õ¹Ð°‰É…¹°…¹±¥¹”ì(´%59M%=8€É€™¥ÉµÝ…É”Ù•ÉÍ¥½¸ì(´%59M%=8€ÄÍ€•Ù¥”%ì(´%59M%=8€ÌÁ€•¹…‰±•É•Õ±…È=‰©•Ð½È‘¥Í…‰±•Y¥É¥¸=‰©•Ð‰äÍ±½Ñ€ì(´%59M%=8€ÌÉ€ÕÉÉ•¹Ð5½‘Õ±”…‘‘É•ÍÍ•ÌÝ¡•É”É•Á½ÉÑ•¸()I•Í½±Ù”Ñ¡”•Ù¥”Ñ¡É½Õ Ñ¡”‘½Õµ•¹Ñ•…Ñ…±½Õ”Á…Ñ …¹É•Ñ…¥¸…µ‰¥Õ¥ÑäÝ¡•É”Í•Ù•É…°M-UÌÍ¡…É”…¸¥Ñ•´¸((ŒŒŒ…¥±ÕÉ”¡…¹‘±¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÐéÌÀÀÀÀÀÝ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()9-€½¸Ñ¡”µ…¹‘…Ñ½ÉäÍÑ…ÉÐ™É…µ”ÑÉ…¹Í¥Ñ¥½¹ÌÑ¡”…¹½¹¥…°ÍÑ…Ñ”Ñ¼U¹‘•™¥¹•¸9¼™¥ÉÍÐÉ•ÍÁ½¹Í”‰•™½É”Ñ¡”…ÁÁ±¥…‰±”Ñ¥µ•È…±Í¼±•…Ù•ÌÑ…É•ÐÍ•±•Ñ¥½¸Õ¹•ÍÑ…‰±¥Í¡•¸¼¹½ÐÍ•¹ÑÉ…¹Í™•È™É…µ•Ì…™Ñ•È…µ‰¥Õ½ÕÌÍ•±•Ñ¥½¸¸()]!P€Í€¥¹‘¥…Ñ•Ì•Ù¥”…‰½ÉÐ‘ÕÉ¥¹œÑ¡”•¹ÑÉäÍ•ÅÕ•¹”¸AÉ•Í•ÉÙ”…¹äÁ…ÉÑ¥…°¥‘•¹Ñ¥ÑäÉ•½É‘Ì‰ÕÐµ…É¬Ñ¡”ÁÉ½É…µµ¥¹œÍ•ÍÍ¥½¸…‰½ÉÑ•¸()M•”m•Ù¥”¥Í½Ù•Éåt ¸¸½‘¥…¹½ÍÑ¥Ì½‘•Ù¥”µ‘¥Í½Ù•Éä¹µ¤°m‘‘É•ÍÌ¥Í½Ù•Éåt ¸¸½‘¥…¹½ÍÑ¥Ì½…‘‘É•ÍÌµ‘¥Í½Ù•Éä¹µ¤°…¹m•Ù¥”%‘•¹Ñ¥Ñåt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´Äµ‘•Ù¥”µ¥‘•¹Ñ¥Ñä¹µ¤™½ÈÑ¡”É•…µ½¹±ä‘¥Í½Ù•ÉäÁÉ½•‘ÕÉ•Ì¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀäÔ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½‘¥µ•¹Í¥½¸µÉ•™•É•¹”¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒAÉ½É…µµ¥¹œ%59M%=9€I•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÀÅ€()AÉ½É…µµ¥¹œ%59M%=9€ÝÉ¥Ñ•ÌÑÉ…¹Í™•ÈÑ¡”½¹™¥ÕÉ…Ñ½È™¥•±‘ÌÕÍ•‰ä½¹™½¹™¥ÕÉ…Ñ½ÉÍ€°=‰©•Ð…ÍÍ¥¹µ•¹ÑÌ°5½‘Õ±”…‘‘É•ÍÍ•Ì°…¹¥¹‘•á•Á…É…µ•Ñ•ÉÌ¸I•±…Ñ••Ù¥”É•ÍÁ½¹Í•ÌÉ•Á½ÉÐÑ¡”ÝÉ¥ÑÑ•¸ÍÑ…Ñ”½ÈÍÑÉÕÑÕÉ••ÉÉ½ÉÌ¸((ŒŒŒ]É¥Ñ”™É…µ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÀÉ€()ð%59M%=9€ðÉ…µ”ð5•…¹¥¹œðM•ÅÕ•¹”ð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð€Ñ€ð€¨m]!=t¨À¨ŒÐ©mÅt©mÉt©mÍt©mÑt©mÕt©mÙtŒ€ðÝÉ¥Ñ”½¹™¥ÕÉ…Ñ½È™¥•±‘ÌÄ¸¹Ù€ð½¹™½¹™¥ÕÉ…Ñ½ÉÍ€ð)ð€Õ€ð€¨m]!=t¨À¨ŒÔ©mÝt©mát©måt©mÄÁt©mÄÅt©mÄÉtŒ€ðÝÉ¥Ñ”½¹™¥ÕÉ…Ñ½È™¥•±‘ÌÜ¸¹ÄÉ€ð½¹™½¹™¥ÕÉ…Ñ½ÉÍ€ð)ð€ÌÁ€ð€¨m]!=t¨À¨ŒÌÀ©mM1=Qt©m-e=tŒ€ð…ÍÍ¥¸=‰©•ÐÑ¼Í±½Ñ€ð½¹™-=€ð)ð€ÌÉ€ð€¨m]!=t¨À¨ŒÌÈmM1=Qt©mMeMt©mItŒ€ð…ÍÍ¥¸=‰©•ÐÍåÍÑ•´½…‘‘É•ÍÌð½¹™-=€ð)ð€ÌÕ€ð€¨m]!=t¨À¨ŒÌÔm%9atmM1=Qt©mY1}AItŒ€ðÝÉ¥Ñ”¥¹‘•á•½¹™¥ÕÉ…Ñ¥½¸Ù…±Õ”ð½¹™-=€ð()%59M%=8€Ñ€¥Ìµ…¹‘…Ñ½Éä¥¸½¹™½¹™¥ÕÉ…Ñ½ÉÍ€ì€Õ€¥Ì½ÁÑ¥½¹…°¸%59M%=8€ÌÁ€¥Ìµ…¹‘…Ñ½Éä…¹É•Á•…Ñ…‰±”¥¸½¹™-=€ì€ÌÉ€…¹€ÌÕ€…É”½ÁÑ¥½¹…°…¹É•Á•…Ñ…‰±”¸((ŒŒŒI•±…Ñ•É•ÍÁ½¹Í”…¹•ÉÉ½È™É…µ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÀÍ€()…ÕÑ¥½¹ÌèÝ…É¹¥¹€()ð%59M%=9€ðÉ…µ”ð5•…¹¥¹œð)ð€´´´ð€´´´ð€´´´ð)ð€Ñ€ð€¨m]!=t©m]!It¨Ð©mÅt©mÉt©mÍt©mÑt©mÕt©mÙtŒ€ð•Ù¥”½¹™¥ÕÉ…Ñ½ÈÉ•Á½ÉÐ€Ä¸¸Ù€ð)ð€Õ€ð€¨m]!=t©m]!It¨Ô©mÝt©mát©måt©mÄÁt©mÄÅt©mÄÉtŒ€ð•Ù¥”½¹™¥ÕÉ…Ñ½ÈÉ•Á½ÉÐ€Ü¸¸ÄÉ€ð)ð€ÌÁ€ð€¨m]!=t©m]!It¨ÌÀ©mM1=Qt©m-e=t©mMQQtŒ€ð½¹™¥ÕÉ•=‰©•Ð½ÈY¥É¥¸=‰©•ÐÍÑ…Ñ”ð)ð€ÌÅ€ð€¨m]!=t©m]!It¨ÌÄ©mM1=Qt©m=t©mMQQtŒ€ð=‰©•ÐÍÑ…Ñ”½•ÉÉ½Èð)ð€ÌÉ€ð€¨m]!=t©m]!It¨ÌÈmM1=Qt©mMeMt©mItŒ€ð•™™•Ñ¥Ù”5½‘Õ±”…‘‘É•ÍÌð)ð€ÌÑ€ð€¨m]!=t©m]!It¨ÌÐ©mM1=Qt©mII=ItŒ€ð…‘‘É•ÍÌ•ÉÉ½Èð)ð€ÌÕ€ð€¨m]!=t©m]!It¨ÌÔm%9atmM1=Qt©mY1}AItŒ€ð•™™•Ñ¥Ù”¥¹‘•á•Á…É…µ•Ñ•Èð)ð€Ìå€ð€¨m]!=t©m]!It¨Ìä©mM1=Qt©m%9at©mII=ItŒ€ð¥¹‘•á•Á…É…µ•Ñ•ÈÝ…É¹¥¹œ½•ÉÉ½Èð((ŒŒŒQÉ…¹ÍÁ½ÉÐÉ…¹•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÀÑ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()ð¥•±ðI…¹”¥¸=A8¹‘‰€ð)ð€´´´ð€´´´ð)ðÄ¸¹ÄÉ€ð€À¸¸ÈÔÕ€ð)ðM1=Q€ð€Ä¸¸ÈÔÕ€ð)ð-e=€ð€Ä¸¸ØÔÔÌÕ€ð)ðMeM€ð€Ä¸¸ÈÔÕ€ð)ðI€ð€À¸¸ØÔÔÌÕ€ð)ð%9a€ð€À¸¸ÈÔÕ€ð)ðY1}AI€ð€À¸¸ØÔÔÌÕ€ð)ðMQQ€°II=I€ð€À¸¸Å€ð()Q¡•Í”…É”™É…µ”µ™¥•±…Á…¥Ñ¥•Ì¸…Ñ…±½Õ”…¹…‘‘É•ÍÌÉÕ±•Ì‘•™¥¹”Ñ¡”Ù…±Õ•ÌÙ…±¥™½È„Á…ÉÑ¥Õ±…È•Ù¥”¸((ŒŒŒ%59M%=8€Ñ€…¹€Õ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()=A8¹‘‰€±…‰•±Ì•… Ä¸¹ÄÉ€™¥•±ƒŠq½¹™¥ÕÉ…Ñ½ÈÙ…±Õ—Št°½¹ÍÑÉ…¥¹Ì¥ÐÑ¼€À¸¸ÈÔÕ€°…¹‘•ÍÉ¥‰•Ì½¹™½¹™¥ÕÉ…Ñ½ÉÍ€…ÌÙ¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸¸Q¡½Í”…É”ÑÉ…¹ÍÁ½ÉÐ…¹Í•ÅÕ•¹”™…ÑÌ¸5!…Ñ…±½Õ”¹‘‰€Í•Á…É…Ñ•±ä‘•™¥¹•Ì™¥ÉµÝ…É”µÍÁ•¥™¥ŒÁ¡åÍ¥…°Íåµ‰½±Ì…¹±•…°‘½µ…¥¹Ì¸9¼…¹½¹¥…°É½ÍÌµ‘…Ñ…‰…Í”­•ä•ÍÑ…‰±¥Í¡•ÌÑ¡…ÐÅ€¥ÌÕ¹¥Ù•ÉÍ…±±äÑ¡”9}=9€‘•™¥¹¥Ñ¥½¸Ý¥Ñ ÁÉ½É•ÍÍ¥Ù”€ô€Å€°½È…¸•ÅÕ¥Ù…±•¹ÐÁ½Í¥Ñ¥½¹…°µ…ÁÁ¥¹œ¸AÉ•Í•ÉÙ”…±°ÑÝ•±Ù”É…Ü™¥•±‘Ì…¹É•Í½±Ù”…¹ä…Ñ…±½Õ”½ÉÉ•±…Ñ¥½¸Í•Á…É…Ñ•±äÑ¡É½Õ mA¡åÍ¥…°µ½¹™¥ÕÉ…Ñ¥½¸É•Í½±ÕÑ¥½¹t ¸¸½¥¹Ñ•É¹…±Ì½…Ñ…±½Õ”µÉ•Í½±ÕÑ¥½¸¹µ‘¥µ•¹Í¥½¸´Ðµ…¹´Ôµ…É”µ„µÑÉ…¹ÍÁ½ÉÐµ‰½Õ¹‘…Éä¤¸((ŒŒŒ%59M%=8€ÌÁ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…ÁÁ±¥•ÌÑ½€°™¥ÉµÝ…É•€)…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()Q¡”ÝÉ¥Ñ”…ÉÉ¥•Ì„½¹™¥ÕÉ•=‰©•Ð¹Õµ‰•È¸¥…¹½ÍÑ¥ŒÍÑ…Ñ”‘•Ñ•Éµ¥¹•Ì¡½Ü„ÁÉ•Ù¥½ÕÍ±äÉ•Á½ÉÑ•-e=€¥ÌÉ•Í½±Ù•è((´MQQ€ô€Á€è•¹…‰±•5½‘Õ±”°9}-e}=	)P¹­•å}½‰©•Ñ€ì(´MQQ€ô€Å€è‘¥Í…‰±•5½‘Õ±”°9}Y%I%9}=	)P¹Ù¥É¥¹}­•å}½‰©•Ñ€¸()Q¡¥ÌÁ½±…É¥Ñä…ÁÁ±¥•ÌÑ¼Ñ¡”MQQ€…ÉÉ¥•‰ä%59M%=8€ÌÁ€ì¥ÐµÕÍÐ¹½Ð‰”½Á¥•Ñ¼Ñ¡”Í•Á…É…Ñ”MQQ€™¥•±…ÉÉ¥•‰ä%59M%=8€ÌÅ€Ý¥Ñ¡½ÕÐ¥¹‘•Á•¹‘•¹Ð•Ù¥‘•¹”¸()Q¡”Ñ…É•ÐÝÉ¥Ñ”µÕÍÐÕÍ”„Á•Éµ¥ÑÑ•½¹™¥ÕÉ•=‰©•Ð°Ù…±¥‘…Ñ•Ñ¡É½Õ Y¥É¥¸=‰©•Ð°™¥ÉµÝ…É”°…¹Í±½Ð…ÍÍ½¥…Ñ¥½¹Ì¸((ŒŒŒ%59M%=8€ÌÉ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÀÝ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()€ŒÌÈmM1=Qu€¥ÌÑ¡”Á…É…µ•Ñ•É¥é•%59M%=9€Í•±•Ñ½ÈèÑ¡”±•…‘¥¹œ€€Í•±•ÑÌÑ¡”ÝÉ¥Ñ”™½É´…¹Ñ¡”™½±±½Ý¥¹œ€€…ÑÑ…¡•ÌM1=Q€Ñ¼Ñ¡”Í•±•Ñ½È¸MeM€…¹I€…É”½É‘¥¹…Éä%59M%=9€Ù…±Õ•ÌÍ•Á…É…Ñ•Ý¥Ñ €©€¸Q¡•äÉ•ÅÕ¥É”Ñ¡”=‰©•Ð½ÍåÍÑ•´…‘‘É•ÍÌÉÕ±”…¹µÕÍÐ¹½Ð…±°‰”‘•½‘•…Ì€½A1€¸((ŒŒŒ%59M%=8€ÌÕ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÀá€()Q¡”ÑÝ¼€€Í•Á…É…Ñ½ÉÌ‰•™½É”%9a€…¹M1=Q€…É”Í¥¹¥™¥…¹Ð¸%9a€½ÉÉ•±…Ñ•ÌÝ¥Ñ ½¹Ñ•áÐµÉ•Í½±Ù•9}=9¹¥‘á€¸ÁÁ±äÉ…¹•Ì°™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¹Ì°…¹½¹Ù•ÉÍ¥½¹Ì‰•™½É”•¹½‘¥¹œY1}AI€¸((ŒŒŒÉÉ½È‘¥µ•¹Í¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÀå€()…ÕÑ¥½¹ÌèÝ…É¹¥¹€()%59M%=8€ÌÅ€ÁÉ½Ù¥‘•Ì™¥Ù”™¥á•=‰©•ÐµÍÑ…Ñ”½‘•Ì¸%59M%=8€ÌÑ€…¹€Ìå€…ÉÉä‰½½±•…¸•ÉÉ½È™¥•±‘ÌÝ¥Ñ¡½ÕÐ•¹Õµ•É…Ñ•…ÕÍ•Ì¸()%59M%=8€Ìå€¥Ì¥¹Ñ•¹Ñ¥½¹…±±ä¹½¹™…Ñ…°¥¸Ñ¡”…¹½¹¥…°…‘Ù…¹•Í•ÅÕ•¹”è¥Ðµ…ÁÌÑ¼]…É¹¥¹œÍ¼…¸Õ¹µ…¹…•Á…É…µ•Ñ•È‘½•Ì¹½Ð¹••ÍÍ…É¥±äÉ•©•ÐÑ¡”É•ÍÐ½˜Ñ¡”ÑÉ…¹Í™•È¸((ŒŒŒM½ÕÉ”‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÔéÌÀÀÀÀÄÁ€()Q¡”Í…µ”¹Õµ•É¥Œ‘¥µ•¹Í¥½¹Ì…ÁÁ•…È¥¸‘¥…¹½ÍÑ¥Ì‰•…ÕÍ”ÁÉ½É…µµ¥¹œÝÉ¥Ñ•Ì…¹‘¥…¹½ÍÑ¥ŒÉ•…µ‰…¬ÁÉ½©•ÐÉ•±…Ñ•ÍÑ…Ñ”¸¥É•Ñ¥½¸°™É…µ”™½É´°…¹…Ñ¥Ù”Í•ÅÕ•¹”‘¥ÍÑ¥¹Õ¥Í Ñ¡•´¸M•”Ñ¡”m¥…¹½ÍÑ¥Œ%59M%=9€I•™•É•¹•t ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥µ•¹Í¥½¸µÉ•™•É•¹”¹µ¤™½ÈÉ•…µ½¹±ä¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀäØ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½•ÉÉ½Èµ¡…¹‘±¥¹œ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒAÉ½É…µµ¥¹œÉÉ½È!…¹‘±¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäØéÌÀÀÀÀÀÅ€()AÉ½É…µµ¥¹œ™…¥±ÕÉ•ÌµÕÍÐÉ•µ…¥¸…ÑÑ…¡•Ñ¼Ñ¡”…Ñ¥Ù”Í•ÍÍ¥½¸°Ñ…É•Ð•Ù¥”°ÑÉ…¹Í™•ÈÍ•ÅÕ•¹”°Í±½Ñ€°=‰©•Ð°ÁÉ½Á•ÉÑä°…¹…ÑÑ•µÁÑ•Ù…±Õ”¸((ŒŒŒQ•Éµ¥¹…°É•ÍÁ½¹Í•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäØéÌÀÀÀÀÀÉ€()ðÉ…µ”ð5•…¹¥¹œ¥¸=A8¹‘‰€ð±…ÍÍ¥™¥…Ñ¥½¸ð)ð€´´´ð€´´´ð€´´´ð)ð€©m]!=t¨ÔÄ©m]!I}-tŒ€ðÝÉ½¹œ½¹™¥ÕÉ…Ñ¥½¸ð™…Ñ…°•ÉÉ½Èð)ð€©m]!=t¨ÔÈ©m]!I}-tŒ€ð½¹™¥ÕÉ…Ñ¥½¸…•ÁÑ•ðÍÕ•ÍÍ™Õ°…‘Ù…¹•µÑÉ…¹Í™•ÈÉ•ÍÕ±Ðð)ð€©m]!=t¨Ì¨ÀŒ€ð…‰½ÉÐ½¹™¥ÕÉ…Ñ¥½¸ð‘¥É•Ñ¥½¸µ‘•Á•¹‘•¹Ð…‰½ÉÐð)ð€©m]!=t¨Ð©m]!I}-tŒ€ð•Ù¥”•¹½˜ÑÉ…¹Íµ¥ÍÍ¥½¸ð•¹ÑÉä½Ù¥ÉÑÕ…°µÑÉ…¹Í™•ÈÑ•Éµ¥¹…°µ…É­•Èð)ð€©m]!=t¨Ð¨ÀŒ€ðÁÉ½É…µµ•È•¹½˜ÑÉ…¹Íµ¥ÍÍ¥½¸ð±½Í•Ì…‘Ù…¹•ÑÉ…¹Í™•ÈÁ…å±½…ð)ð€©m]!=t¨È¨ÀŒ€ð•¹ÁÉ½É…µµ¥¹œÍ•ÍÍ¥½¸ð½ÕÑ•ÈÍ•ÍÍ¥½¸±½Í”ð()=A8¹‘‰€…±Í¼ÁÉ½Ù¥‘•Ì]!I€ô€Á€Ù…É¥…¹ÑÌ½˜]!P€ÔÅ€…¹€ÔÉ€½ÕÑÍ¥‘”Ñ¡”…¹½¹¥…°Í•ÅÕ•¹”É½ÝÌ¸AÉ•Í•ÉÙ”Ñ¡”É••¥Ù•™½É´¸((ŒŒŒMÑÉÕÑÕÉ••ÉÉ½ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäØéÌÀÀÀÀÀÍ€((ŒŒŒŒ=‰©•ÐÍÑ…Ñ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäØéÌÀÀÀÀÀÑ€()€¨m]!=t©m]!It¨ÌÄ©mM1=Qt©m=t©mMQQtŒ€()ð½‘”ð5•…¹¥¹œð½¹™-=€ÍÑ…Ñ”ð)ð€´´´ð€´´´ð€´´´ð)ð€Á€ð=‰©•Ð¹½Ð¥µÁ±•µ•¹Ñ•½Õ¹Í•ÐðÉÉ½Èð)ð€Å€ð=‰©•Ð‰ÕÍäðÉÉ½È¥¸½¹™-=€ì¥¹™½Éµ…Ñ¥½¹…°¥¸‘¥…¹½ÍÑ¥Œ½¹Ñ•áÑÌð)ð€É€ð=‰©•Ð…±É•…‘ä½¹™¥ÕÉ•ðÉÉ½Èð)ð€Í€ð¥¹ÍÕ™™¥¥•¹Ð™É•”=‰©•Ð…Á…¥ÑäðÉÉ½Èð)ð€Ñ€ðÉ•ÅÕ•ÍÑ•=‰©•Ð¹½Ð¥µÁ±•µ•¹Ñ•ðÉÉ½Èð()Q¡”Í…µ”‰ÕÍä™É…µ”…¸‰”¹½¹™…Ñ…°¥¹™½Éµ…Ñ¥½¸‘ÕÉ¥¹œ‘¥…¹½ÍÑ¥Ì…¹„ÑÉ…¹Í™•È•ÉÉ½È‘ÕÉ¥¹œÁÉ½É…µµ¥¹œ¸M•ÅÕ•¹”½¹Ñ•áÐ½¹ÑÉ½±Ì¡…¹‘±¥¹œ¸((ŒŒŒŒ‘‘É•ÍÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäØéÌÀÀÀÀÀÕ€()€¨m]!=t©m]!It¨ÌÐ©mM1=Qt©mII=ItŒ€()Q¡”‰½½±•…¸™±…œ¥‘•¹Ñ¥™¥•Ì…¸…‘‘É•ÍÌ•ÉÉ½È‰ÕÐ‘½•Ì¹½Ð•¹½‘”¥ÑÌ…ÕÍ”¸((ŒŒŒŒA…É…µ•Ñ•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäØéÌÀÀÀÀÀÙ€()…ÕÑ¥½¹ÌèÝ…É¹¥¹€()€¨m]!=t©m]!It¨Ìä©mM1=Qt©m%9at©mII=ItŒ€()Q¡¥Ì¥Ì±…ÍÍ¥™¥•…Ì•ÉÉ½Èµ…¹µ¥¹™½Éµ…Ñ¥½¸¸½¹™-=€µ…ÁÌ¥ÐÑ¼]…É¹¥¹œÍ¼Õ¹ÍÕÁÁ½ÉÑ•½Õ¹µ…¹…•Á…É…µ•Ñ•ÉÌ¹••¹½Ð¥¹Ù…±¥‘…Ñ”…±°½Ñ¡•ÈÝÉ¥Ñ•Ì¸((ŒŒŒ-€…¹9-€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäØéÌÀÀÀÀÀÝ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€°Ý…É¹¥¹€()=É‘•É•ÁÉ½É…µµ¥¹œÍ•ÅÕ•¹•Ì‘¼¹½Ð±¥ÍÐ½É‘¥¹…Éä-€½È9-€…Ìµ•µ‰•ÉÌ°‰ÕÐÍÑ…ÑÕÌÑ¹…­€‘•™¥¹•ÌÑ¡•¥ÈÍÑ…Ñ”ÑÉ…¹Í¥Ñ¥½¹Ìè((´•¹ÑÉäµ™É…µ”9-€ƒŠHU¹‘•™¥¹•ì(´Ù¥ÉÑÕ…°µ½¹™¥ÕÉ…Ñ½ÈÝÉ¥Ñ”9-€ƒŠHÉÉ½Èì(´=‰©•Ð½…‘‘É•ÍÌ½É•Í•Ð9-€ƒŠHÉÉ½Èì(´Á…É…µ•Ñ•È½ÈÁÉ½É…µµ•È•¹µ½˜µÑÉ…¹Íµ¥ÍÍ¥½¸9-€ƒŠH]…É¹¥¹œì(´±½Í”µÍ•ÍÍ¥½¸9-€ƒŠHÉÉ½È¸()!…¹‘±”9-€É•±…Ñ¥Ù”Ñ¼Ñ¡”±…ÍÐ½ÕÑÍÑ…¹‘¥¹œ½µµ…¹…¹…Ñ¥Ù”Í•ÅÕ•¹”¸¼¹½Ð¥¹Ñ•ÉÁÉ•Ð…¸Õ¹½ÉÉ•±…Ñ•9-€…™Ñ•ÈÁ¥Á•±¥¹¥¹œÍ•Ù•É…°ÝÉ¥Ñ•Ì¸((ŒŒŒQ¥µ•½ÕÐ…¹ÑÉ…¹ÍÁ½ÉÐ±½ÍÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäØéÌÀÀÀÀÀá€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()Ñ¥µ•½ÕÐ¥Ì¹½Ð„¹•…Ñ¥Ù”…­¹½Ý±•‘•µ•¹Ð…¹‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…ÐÑ¡”•Ù¥”É•©•Ñ•½ÈÉ½±±•‰…¬ÁÉ¥½ÈÝÉ¥Ñ•Ì¸5…É¬Ñ¡”É•ÍÕ±Ð¥¹‘•Ñ•Éµ¥¹…Ñ”°Í•¹ÁÉ½É…µµ•È…‰½ÉÐÝ¡•¸Í…™”…¹ÍÕÁÁ½ÉÑ•°±½Í”Ñ¡”ÑÉ…¹ÍÁ½ÉÐ…½É‘¥¹œÑ¼…ÁÁ±¥…Ñ¥½¸Á½±¥ä°…¹É•ÅÕ¥É”‘¥…¹½ÍÑ¥ŒÉ•…µ‰…¬‰•™½É”É•ÑÉä¸()	•…ÕÍ”½¹™-=€ÍÑ…ÉÑÌ‰äÉ•Í•ÑÑ¥¹œ…±°=‰©•ÑÌ°¥¹Ñ•ÉÉÕÁÑ¥½¸‘ÕÉ¥¹œ„É•Á±…•µ•¹ÐÑÉ…¹Í™•È…¸±•…Ù”Á…ÉÑ¥…°½ÈÕ¹•ÉÑ…¥¸ÍÑ…Ñ”¸¼¹½ÐÉ•ÍÕµ”…Ð…¸…É‰¥ÑÉ…Éä±…Ñ•È™É…µ”Õ¹±•ÍÌ•Ù¥”µÍÁ•¥™¥Œ‰•¡…Ù¥½È•ÍÑ…‰±¥Í¡•ÌÑ¡…ÐÑ¡¥Ì¥ÌÍ…™”¸((ŒŒŒI•½Ù•ÉäÁ½±¥ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäØéÌÀÀÀÀÀå€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€((Ä¸MÑ½ÀÍ•¹‘¥¹œ¹•ÜÝÉ¥Ñ•Ì…™Ñ•È„™…Ñ…°•ÉÉ½È½È…µ‰¥Õ½ÕÌÑ¥µ•½ÕÐ¸(È¸AÉ•Í•ÉÙ”•Ù•Éä™É…µ”…¹ÍÑ…Ñ”ÑÉ…¹Í¥Ñ¥½¸¸(Ì¸M•¹ÁÉ½É…µµ•È]!P€Í€…‰½ÉÐ¥˜Ñ¡”…Ñ¥Ù”Ý½É­™±½ÜÍÕÁÁ½ÉÑÌÉ•½Ù•Éä¸(Ð¸¹½ÈÉ”µ•ÍÑ…‰±¥Í Ñ¡”½¹¹•Ñ¥½¸¸(Ô¸A•É™½É´„™É•Í ‘¥…¹½ÍÑ¥Œ¥¹Ñ•ÉÙ¥•Ü¸(Ø¸I”µÉ•Í½±Ù”Ñ¡”•Ù¥”…¹…Ñ…±½Õ”½¹Ñ•áÐ¸(Ü¸I•‰Õ¥±Ñ¡”½µÁ±•Ñ”‘•Í¥É•½¹™¥ÕÉ…Ñ¥½¸¸(à¸MÑ…ÉÐ„¹•ÜÁÉ½É…µµ¥¹œÍ•ÍÍ¥½¸É…Ñ¡•ÈÑ¡…¸…ÍÍÕµ¥¹œÑ¡”ÁÉ•Ù¥½ÕÌÑÉ…¹Í™•ÈÁ½Í¥Ñ¥½¸¸()]!P€Ý€¥Ì±…‰•±±•…Ì‘•±•Ñ¥¹œÍÑ½É••Ù¥”½¹™¥ÕÉ…Ñ¥½¸‰ÕÐ¥Ì¹½ÐÁ…ÉÐ½˜„…¹½¹¥…°ÁÉ½É…µµ¥¹œÍ•¹…É¥¼¸¼¹½ÐÕÍ”¥Ð…Ì„•¹•É¥ŒÉ•½Ù•Éä½Á•É…Ñ¥½¸Ý¥Ñ¡½ÕÐ•Ù¥”µÍÁ•¥™¥Œ•Ù¥‘•¹”¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀäÜ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½½‰©•ÐµÁÉ½É…µµ¥¹œ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒ=‰©•ÐAÉ½É…µµ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÜéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()=‰©•ÐÁÉ½É…µµ¥¹œ…ÍÍ¥¹Ì„±½¥…°=‰©•ÐÑ¼•… ™¥ÉµÝ…É”µ•áÁ½Í•5½‘Õ±”‘ÕÉ¥¹œ…‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸¸((ŒŒŒ]É¥Ñ”™É…µ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÜéÌÀÀÀÀÀÉ€()€¨m]!=t¨À¨ŒÌÀ©mM1=Qt©m-e=tŒ€()ð¥•±ð=A8¹‘‰€É…¹”ð5•…¹¥¹œð)ð€´´´ð€´´´ð€´´´ð)ðM1=Q€ð€Ä¸¸ÈÔÕ€ð•Ù¥”µ±½…°Í±½Ñ€ð)ð-e=€ð€Ä¸¸ØÔÔÌÕ€ðÑ…É•Ð=‰©•Ð¹Õµ‰•Èð()-e=€¥ÌÑ¡”•áÑ•É¹…°9}-e}=	)P¹­•å}½‰©•Ñ€Ù…±Õ”°¹½Ð9}-e}=	)P¹¥‘}­•å}½‰©•Ñ€¸((ŒŒŒI•Á±…•µ•¹ÐµÍÑå±”ÑÉ…¹Í™•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÜéÌÀÀÀÀÀÍ€()U¹•ÉÑ…¥¹Ñäè¹½Ð•ÍÑ…‰±¥Í¡•‘€()Q¡”…¹½¹¥…°½¹™-=€Í•ÅÕ•¹”‰•¥¹ÌÝ¥Ñ è()€©m]!=t¨ÄÐŒÀ¨ÀŒ€()=A8¹‘‰€‘•ÍÉ¥‰•ÌÑ¡¥Ì…ÌÉ•Í•ÑÑ¥¹œ…±°•Ù¥”=‰©•ÑÌ¸Q¡”Í•ÅÕ•¹”Ñ¡•¸É•ÅÕ¥É•ÌÉ•Á•…Ñ•=‰©•ÐÝÉ¥Ñ•Ì…¹±…Ñ•ÈÍ•¹‘Ì…‘‘É•ÍÍ•Ì…¹Á…É…µ•Ñ•ÉÌ¸QÉ•…ÐÑ¡¥Ì…Ì„™Õ±°É•Á±…•µ•¹ÐÑÉ…¹Í™•Èè½¹ÍÑÉÕÐ…¹Ù…±¥‘…Ñ”Ñ¡”½µÁ±•Ñ”‘•Í¥É•5½‘Õ±”½=‰©•Ð±…å½ÕÐ‰•™½É”Í•¹‘¥¹œÉ•Í•Ðµ…±°¸()=A8¹‘‰€…±Í¼É•¥ÍÑ•ÉÌè()€©m]!=t¨ÄÐmM1=Qt¨ÀŒ€()™½ÈÉ•Í•ÑÑ¥¹œ½¹”Í±½Ñ€¸%Ð¥Ì¹½Ð„µ•µ‰•È½˜Ñ¡”…¹½¹¥…°½¹™-=€Í•ÅÕ•¹”°Í¼¥ÑÌÍÑ…¹‘…±½¹”±¥™•å±”…¹½µÁ±•Ñ¥½¸‰•¡…Ù¥½È…É”¹½Ð•ÍÑ…‰±¥Í¡•‰äÑ¡…ÐÍ•¹…É¥¼¸((ŒŒŒI•Í½±Ù¥¹œÑ¡”Á•Éµ¥ÑÑ•=‰©•Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÜéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€((Ä¸I•Í½±Ù”Ñ¡”A¡åÍ¥…°•Ù¥”¥Ñ•´…¹™¥ÉµÝ…É”¸(È¸I•Í½±Ù”Ñ¡”Ñ…É•ÐM1=Q€……¥¹ÍÐÑ¡”™¥ÉµÝ…É”ÌÍ±½ÐÍÑÉÕÑÕÉ•Ì¸(Ì¸•Ñ•Éµ¥¹”™É½´%59M%=8€ÌÀ¹MQQ€Ý¡•Ñ¡•ÈÑ¡”5½‘Õ±”¥Ì•¹…‰±•€¡€Á€¤Ý¥Ñ „É•Õ±…È½¹™¥ÕÉ•=‰©•Ð½È‘¥Í…‰±•€¡€Å€¤Ý¥Ñ „Y¥É¥¸=‰©•Ð¸(Ð¸%˜‘¥Í…‰±•°É•Í½±Ù”-e=€Ñ¡É½Õ 9}Y%I%9}=	)P¹Ù¥É¥¹}­•å}½‰©•Ñ€ì¥˜•¹…‰±•°É•Í½±Ù”¥ÐÑ¡É½Õ 9}-e}=	)P¹­•å}½‰©•Ñ€¸(Ô¸UÍ”M}=	)Q}Y%I%9}=	)Q€Ñ¼™¥¹=‰©•ÑÌÁ•Éµ¥ÑÑ•‰äÑ¡…ÐY¥É¥¸=‰©•Ð¸(Ø¸UÍ”M}=	)Q}%I5]I€…¹9}M1=QM€Ñ¼É•ÅÕ¥É”™¥ÉµÝ…É”…¹Í±½ÐÍÕÁÁ½ÉÐ¸(Ü¸I•ÍÁ•Ð9}M1=QL¹™¥á•‘}­½€…¹Í±½Ð½¹‘¥Ñ¥½¹Ì¸(à¸UÍ”Ñ¡”Ñ…É•Ð=‰©•ÐÌ•áÑ•É¹…°­•å}½‰©•Ñ€¥¸Ñ¡”ÁÉ½É…µµ¥¹œ™É…µ”¸()Y¥É¥¸=‰©•Ð½¹ÍÑÉ…¥¹Ì„‘¥Í…‰±•5½‘Õ±”Ì½¹™¥ÕÉ…‰±”É½±”¸%Ð¥Ì¹½Ð¥ÑÍ•±˜Ñ¡”É•Õ±…È½¹™¥ÕÉ•=‰©•ÐÑ¼Í•¹Õ¹±•ÍÌ¥¹‘•Á•¹‘•¹Ð•Ù¥‘•¹”•ÍÑ…‰±¥Í¡•ÌÑ¡…Ð„ÍÁ•¥™¥Œ•Ù¥”•áÁ•ÑÌÍÕ „ÝÉ¥Ñ”¸((ŒŒŒ¥á•…¹…‰Í•¹Ð5½‘Õ±•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÜéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()™¥á•=‰©•Ð¥Ì…Ñ…±½Õ”…Á…‰¥±¥Ñä°¹½ÐÁ•Éµ¥ÍÍ¥½¸Ñ¼½Ù•ÉÝÉ¥Ñ”¥Ð¸!¥‘‘•¸U$5½‘Õ±•Ì…¹…ÁÌ¥¸U$¹Õµ‰•É¥¹œ‘¼¹½Ð¡…¹”ÁÉ½Ñ½½°M1=Q€Ù…±Õ•Ì¸()¼¹½ÐÍå¹Ñ¡•Í¥é”5½‘Õ±•ÌÕÀÑ¼9}%I5]I¹Í±½ÑÍ€µ•É•±ä‰•…ÕÍ”Ñ¡”™¥ÉµÝ…É”‘•±…É•Ì„…Á…¥Ñä¸UÍ”Ñ¡”…ÑÕ…°Í±½Ð½=‰©•Ð…ÍÍ½¥…Ñ¥½¹Ì…¹Ñ¡”ÕÉÉ•¹Ð‘¥…¹½ÍÑ¥ŒÁÉ½©•Ñ¥½¸¸((ŒŒŒM•ÅÕ•¹”‰•¡…Ù¥½È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÜéÌÀÀÀÀÀÙ€()Q¡”=‰©•ÐÝÉ¥Ñ”¥Ì‰½Ñ µ…¹‘…Ñ½Éä…¹É•Á•…Ñ…‰±”¸%ÐÍÑ…ÉÑÌÑ¡”€ÔÀµÍ•½¹•Ù¥•-=Q¥µ•=ÕÑ€…¹„ÑÝ¼µÍ•½¹µ‘-½Y…±Õ•Q¥µ•]…¥Ñ€¸9-€ÑÉ…¹Í¥Ñ¥½¹ÌÑ¼ÉÉ½È¸()™Ñ•È…±°=‰©•Ð°…‘‘É•ÍÌ°…¹Á…É…µ•Ñ•ÈÝÉ¥Ñ•Ì°Ñ¡”ÁÉ½É…µµ•ÈÍ•¹‘Ì]!P€Ñ€•¹½˜ÑÉ…¹Íµ¥ÍÍ¥½¸¸Q¡”•Ù¥”…¸Ñ¡•¸É•ÑÕÉ¸]!P€ÔÉ€°]!P€ÔÅ€°„ÍÑÉÕÑÕÉ••ÉÉ½È°½È…‰½ÉÐ¸((ŒŒŒ=‰©•Ð•ÉÉ½ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäÜéÌÀÀÀÀÀÝ€()ð%59M%=8€ÌÅ€½‘”ð=A8¹‘‰€µ•…¹¥¹œð)ð€´´´ð€´´´ð)ð€Á€ð=‰©•Ð¹½Ð¥µÁ±•µ•¹Ñ•½Õ¹Í•Ðð)ð€Å€ð=‰©•Ð‰ÕÍäð)ð€É€ð=‰©•Ð…±É•…‘ä½¹™¥ÕÉ•ð)ð€Í€ð¥¹ÍÕ™™¥¥•¹Ð™É•”=‰©•Ð…Á…¥Ñäð)ð€Ñ€ðÉ•ÅÕ•ÍÑ•=‰©•Ð¹½Ð¥µÁ±•µ•¹Ñ•ð()½‘•Ì€Á€°€É€°€Í€°…¹€Ñ€…É”™…Ñ…°•ÉÉ½ÉÌ¥¸½¹™-=€¸	ÕÍä½‘”€Å€¥Ì±…ÍÍ¥™¥•…Ì•ÉÉ½Èµ…¹µ¥¹™½Éµ…Ñ¥½¸‰ÕÐÍÑ¥±°µ…ÁÌÑ¼ÉÉ½ÈÑ¡É½Õ ÍÑ…ÑÕÌÑ•ÉÉ½É€¥¸Ñ¡…ÐÍ•ÅÕ•¹”¸I•Ñ…¥¸Ñ¡”…½µÁ…¹å¥¹œMQQ€…¹Í±½Ñ€¸()M•”m5½‘Õ±•Ít ¸¸½‘•Ù¥”µµ½‘•°½µ½‘Õ±•Ì¹µ¤°m=‰©•ÑÍt ¸¸½‘•Ù¥”µµ½‘•°½½‰©•ÑÌ¹µ¤°mY¥É¥¸=‰©•ÑÍt ¸¸½‘•Ù¥”µµ½‘•°½Ù¥É¥¸µ½‰©•ÑÌ¹µ¤°…¹m%59M%=8€ÌÁt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´ÌÀµµ½‘Õ±•Ì¹µ¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀäà()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½Í•ÍÍ¥½¸µ±¥™•å±”¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒAÉ½É…µµ¥¹œM•ÍÍ¥½¸1¥™•å±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäàéÌÀÀÀÀÀÅ€()=A8¹‘‰€µ½‘•±ÌÁÉ½É…µµ¥¹œ…Ì„Í•¹…É¥¼½µÁ½Í•™É½´½É‘•É•Í•ÅÕ•¹•Ì¸Q¡”½ÕÑ•ÈÁÉ½É…µµ¥¹œÍ•ÍÍ¥½¸…¹Ñ¡”¥¹¹•ÈÑÉ…¹Í™•ÈÍ•ÅÕ•¹”¡…Ù”Í•Á…É…Ñ”Ñ•Éµ¥¹…°™É…µ•Ì…¹Ñ¥µ•ÉÌ¸((ŒŒŒM•¹…É¥¼½µÁ½Í¥Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäàéÌÀÀÀÀÀÉ€()AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()ðM•¹…É¥¼ð¹ÑÉäðQÉ…¹Í™•Èð±½Í”ð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð	ä…‘‘É•ÍÌð½¹™‘‘É•ÍÍ•‘€ð½¹™½¹™¥ÕÉ…Ñ½ÉÍ€ð±½Í•½¹™€ð)ð	ä•Ù¥”%ð½¹™A½¥¹ÐÉA½¥¹Ñ]¥Ñ¡%€ðÉ•Á•…Ñ•½¹™-=€ð±½Í•½¹™€ð)ð	ä±½…°¥¹Ñ•É…Ñ¥½¸ð½¹™1½…±	ÕÑÑ½¹€ðÉ•Á•…Ñ•½¹™-=€°Ñ¡•¸½¹™½¹™¥ÕÉ…Ñ½ÉÍ€ð±½Í•½¹™€ð()É•Á•…Ñ•½¹™-=€…ÍÍ½¥…Ñ¥½¸µ•…¹ÌÑ¡”Í•¹…É¥¼•¹¥¹”…¸¥¹Ù½­”Ñ¡…ÐÍ•ÅÕ•¹”É•Á•…Ñ•‘±ä¸Q¡”‘…Ñ…‰…Í”‘½•Ì¹½Ð•¹½‘”Ñ¡”…ÁÁ±¥…Ñ¥½¸µ±•Ù•°É•Á•Ñ¥Ñ¥½¸½Õ¹Ð¸((ŒŒŒ¹ÑÉä…¹¥¹¥Ñ¥…°ÁÉ½©•Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäàéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€()Q¡”•¹ÑÉäÍ•ÅÕ•¹”Í•¹‘Ì½¹”µ…¹‘…Ñ½ÉäÍÑ…ÉÐ™É…µ”è()ð5•Ñ¡½ðÉ…µ”ð)ð€´´´ð€´´´ð)ð‘‘É•ÍÌð€©m]!=t¨Ä©m]!ItŒ€ð)ð•Ù¥”%ð€©m]!=t¨äm%t¨ÀŒ€ð)ð1½…°µ¥¹Ñ•É…Ñ¥½¸Í•¹…É¥¼ð€©m]!=t¨Ä©m]!ItŒ€ð()½¹™1½…±	ÕÑÑ½¹€…¹½¹™‘‘É•ÍÍ•‘€½¹Ñ…¥¸Ñ¡”Í…µ”½É‘•É•™É…µ•Ì¸Q¡•¥È¥µÁ±•µ•¹Ñ…Ñ¥½¸‘¥™™•É•¹”¥ÌÑ¡”™¥ÉÍÐµÉ•ÍÁ½¹Í”Ñ¥µ•ÈèÑ¡”±½…°µ¥¹Ñ•É…Ñ¥½¸Í•ÅÕ•¹”ÕÍ•Ì„€ÌÀÀµÍ•½¹Ý¥¹‘½Ü¥¹ÍÑ•…½˜Ñ¡”€ÄÔµÍ•½¹…‘‘É•ÍÍ•½%Ý¥¹‘½Ü¸Q¡”™É…µ”ÍÑ¥±°½¹Ñ…¥¹Ì]!I€ì=A8¹‘‰€‘½•Ì¹½Ð•áÁ±…¥¸¡½ÜÁ¡åÍ¥…°¥¹Ñ•É…Ñ¥½¸…¹Ñ¡…ÐÙ…±Õ”…É”½½É‘¥¹…Ñ•¸()™Ñ•È•¹ÑÉä°Ñ¡”•Ù¥”…¸É•Á½ÉÐÑ¡”Í…µ”¥¹¥Ñ¥…°ÁÉ½©•Ñ¥½¸ÕÍ•‰ä‘¥…¹½ÍÑ¥Ìè((Ä¸%59M%=8€Å€¥‘•¹Ñ¥Ñäì(È¸™¥ÉµÝ…É”…¹¡…É‘Ý…É”Ù•ÉÍ¥½¹Ìì(Ì¸%59M%=8€Ñ€…¹€Õ€½¹™¥ÕÉ…Ñ½ÈÙ…±Õ•Ìì(Ð¸µ¥É½½¹ÑÉ½±±•ÈÙ•ÉÍ¥½¸ì(Ô¸‘¥…¹½ÍÑ¥Œ‰¥Ñµ…Í­Ìì(Ø¸%59M%=8€ÄÍ€•Ù¥”%ì(Ü¸É•Á•…Ñ•%59M%=8€ÌÁ€5½‘Õ±”½=‰©•ÐÍÑ…Ñ”ì(à¸É•Á•…Ñ•%59M%=8€ÌÉ€…‘‘É•ÍÍ•Ìì(ä¸É•Á•…Ñ•‰ÕÍä%59M%=8€ÌÅ€¥¹™½Éµ…Ñ¥½¸ì(ÄÀ¸]!P€Ñ€•¹½˜ÑÉ…¹Íµ¥ÍÍ¥½¸¸()=¹±äÑ¡”ÍÑ…ÉÐ™É…µ”¥Ìµ…É­•µ…¹‘…Ñ½Éä¸½±±•Ñ½ÉÌµÕÍÐÑ½±•É…Ñ”½µ¥ÑÑ•½ÁÑ¥½¹…°É•ÍÁ½¹Í•Ì…¹É•Á•…Ñ•5½‘Õ±”É•½É‘Ì¸((ŒŒŒQÉ…¹Í™•ÈÍÑ…Ñ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäàéÌÀÀÀÀÀÑ€((ŒŒŒŒY¥ÉÑÕ…°µ½¹™¥ÕÉ…Ñ½ÈÑÉ…¹Í™•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäàéÌÀÀÀÀÀÕ€()½¹™½¹™¥ÕÉ…Ñ½ÉÍ€É•ÅÕ¥É•Ì%59M%=8€Ñ€°½ÁÑ¥½¹…±±äÝÉ¥Ñ•Ì%59M%=8€Õ€°…¹…•ÁÑÌè((´]!P€ÔÅ€èÝÉ½¹œ½¹™¥ÕÉ…Ñ¥½¸ì(´]!P€Í€è•Ù¥”…‰½ÉÐì(´•¡½•½É•Á½ÉÑ•%59M%=8€Ñ€…¹€Õ€Ù…±Õ•Ìì(´•Ù¥”]!P€Ñ€è•¹½˜ÑÉ…¹Íµ¥ÍÍ¥½¸¸()Q¡”Í•ÅÕ•¹”‘½•Ì¹½Ð¥¹±Õ‘”]!P€ÔÉ€¸((ŒŒŒŒ‘Ù…¹•=‰©•ÐÑÉ…¹Í™•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäàéÌÀÀÀÀÀÙ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()½¹™-=€½É‘•ÉÌè((Ä¸µ…¹‘…Ñ½ÉäÉ•Í•Ð½˜…±°=‰©•ÑÌì(È¸µ…¹‘…Ñ½ÉäÉ•Á•…Ñ•%59M%=8€ÌÁ€=‰©•ÐÝÉ¥Ñ•Ìì(Ì¸½ÁÑ¥½¹…°É•Á•…Ñ•%59M%=8€ÌÉ€…‘‘É•ÍÌÝÉ¥Ñ•Ìì(Ð¸½ÁÑ¥½¹…°É•Á•…Ñ•%59M%=8€ÌÕ€Á…É…µ•Ñ•ÈÝÉ¥Ñ•Ìì(Ô¸µ…¹‘…Ñ½ÉäÁÉ½É…µµ•È]!P€Ñ€•¹½˜ÑÉ…¹Íµ¥ÍÍ¥½¸ì(Ø¸•Ù¥”]!P€ÔÅ€½È]!P€ÔÉ€É•ÍÕ±Ð°…ÁÁ±¥…‰±”ÍÑÉÕÑÕÉ••ÉÉ½ÉÌ°½È]!P€Í€…‰½ÉÐ¸()M}=A9}MEU9€½¹Ñ…¥¹Ì¹¼É½ÜÝ¥Ñ ½Á•¹}½É‘•È€ô€å€™½È½¹™-=€¸AÉ•Í•ÉÙ”Ñ¡”Í½ÕÉ”¹Õµ‰•É¥¹œì‘¼¹½Ð¥¹Ù•¹Ð„µ¥ÍÍ¥¹œ½Á•É…Ñ¥½¸¸()Q¡”•ÉÉ½ÈÉ½ÝÌ…É”…±Ñ•É¹…Ñ¥Ù•Ì…ÍÍ½¥…Ñ•Ý¥Ñ Ñ¡”…Ñ¥Ù”ÑÉ…¹Í™•È¸Q¡•¥È¹Õµ•É¥Œ½Á•¹}½É‘•É€Á½Í¥Ñ¥½¹Ì‘¼¹½Ðµ•…¸Ñ¡…Ð…¸•ÉÉ½È…¸½¹±ä‰”É••¥Ù•…™Ñ•È•Ù•Éä•…É±¥•È½ÁÑ¥½¹…°™É…µ”¸((ŒŒŒM•ÍÍ¥½¸±½Í”…¹…‰½ÉÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäàéÌÀÀÀÀÀÝ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()9½Éµ…°±½Í”ÕÍ•Ìè()€©m]!=t¨È¨ÀŒ€()Q¡¥Ì¥ÌÑ¡”Í½±”µ…¹‘…Ñ½Éäµ•µ‰•È½˜±½Í•½¹™€¸%ÑÌÍÑ½É•Ñ¥µ•½ÕÐ…ÍÍ½¥…Ñ¥½¹ÌÍÑ½ÀÑ¡”Ñ•¸µµ¥¹ÕÑ”½¹™¥ÕÉ…Ñ¥½¸Ñ¥µ•È…¹ÍÑ…ÉÐÑ¡”½¹”µÍ•½¹Í•¹…É¥¼µ±½Í”Ý…¥Ð¥¸Ñ¡”MÕ¥Ñ”Í•ÅÕ•¹”µ½‘•°ìÑ¡•ä‘¼¹½ÐÁÉ½Ù”•Ù¥”µÍ¥‘”½µµ¥Ð½ÈÁ•ÉÍ¥ÍÑ•¹”¸()AÉ½É…µµ•È…‰½ÉÐ…¹•Ù¥”…‰½ÉÐÍ¡…É”è()€©m]!=t¨Ì¨ÀŒ€()=A8¹‘‰€ÍÑ½É•ÌÍ•Á…É…Ñ”É½ÝÌ‘¥ÍÑ¥¹Õ¥Í¡•‰ä‘¥É•Ñ¥½¸¸Q¡”…¹½¹¥…°ÁÉ½É…µµ¥¹œÍ•ÅÕ•¹•Ì¥¹±Õ‘”Ñ¡”•Ù¥”µÑ¼µÁÉ½É…µµ•È…‰½ÉÐÉ½Üì=Á•¹EÕ•Éä¹ÑáÑ€Í•Á…É…Ñ•±ä±½…‘ÌÑ¡”ÁÉ½É…µµ•È…‰½ÉÐÑ½•Ñ¡•ÈÝ¥Ñ ‘¥…¹½ÍÑ¥Œ…‰½ÉÐ¸¥É•Ñ¥½¸…¹…Ñ¥Ù”ÍÑ…Ñ”…É”Ñ¡•É•™½É”É•ÅÕ¥É•¸((ŒŒŒQ¥µ¥¹œµ½‘•°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäàéÌÀÀÀÀÀá€()ðQ¥µ•Èð•™…Õ±ÐðI½±”ð)ð€´´´ð€´´´ð€´´´ð)ð½¹™Q¥µ•=ÕÑ€ð€ØÀÀÌðµ…á¥µÕ´½¹™¥ÕÉ…Ñ¥½¸Í•ÍÍ¥½¸ð)ð•Ù¥•¹ÍÝ•ÉQ¥µ•=ÕÑ€ð€ÄÔÌð™¥ÉÍÐ¥‘•¹Ñ¥ÑäÉ•ÍÁ½¹Í”…™Ñ•È…‘‘É•ÍÌ½%ÍÑ…ÉÐð)ð•Ù¥•¹ÍÝ•ÉQ¥µ•=ÕÑ	å	ÕÑÑ½¹€ð€ÌÀÀÌð™¥ÉÍÐÉ•ÍÁ½¹Í”¥¸±½…°µ¥¹Ñ•É…Ñ¥½¸ÁÉ½É…µµ¥¹œð)ð•Ù¥•5½É•¹ÍÝ•ÉQ¥µ•=ÕÑ€ð€ÈÀÌðÉ•µ…¥¹¥¹œ¥¹¥Ñ¥…°¥¹™½Éµ…Ñ¥½¸Õ¹Ñ¥°•Ù¥”]!P€Ñ€ð)ð•Ù¥••ÁÑQ¥µ•=ÕÑ€ð€ÈÌðÙ¥ÉÑÕ…°µ½¹™¥ÕÉ…Ñ½È…•ÁÑ…¹”Ý¥¹‘½Üð)ð•Ù¥•-=Q¥µ•=ÕÑ€ð€ÔÀÌð…‘Ù…¹•=‰©•ÐÑÉ…¹Í™•Èð)ðµ‘-½Y…±Õ•Q¥µ•]…¥Ñ€ð€ÈÌðÝ…¥Ð…ÍÍ½¥…Ñ•Ý¥Ñ =‰©•ÐÝÉ¥Ñ•Ìð)ð-=•ÁÑQ¥µ•]…¥Ñ€ð€ÌÌðÝ…¥Ð…™Ñ•È]!P€ÔÉ€‰•™½É”Í•¹…É¥¼±½Í”ð)ð±½Í•M•¹…É¥½Q¥µ•]…¥Ñ€ð€ÄÌð±½Í”µÍ•ÅÕ•¹”Ý…¥Ðð()Q¡•Í”…É”5å!=5}MÕ¥Ñ”‘•™…Õ±ÑÌ°¹½ÐÝ¥É”µ±•Ù•°½¹ÍÑ…¹ÑÌ¸((ŒŒŒ½µÁ±•Ñ¥½¸±…ÍÍ¥™¥…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀäàéÌÀÀÀÀÀå€()…ÕÑ¥½¹ÌèÝ…É¹¥¹€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()ðI•ÍÕ±ÐðÙ¥‘•¹”ð)ð€´´´ð€´´´ð)ðQÉ…¹Í™•È…•ÁÑ•ð•áÁ•Ñ••Ù¥”Ñ•Éµ¥¹…°É•ÍÁ½¹Í”™½ÈÑ¡”…Ñ¥Ù”ÑÉ…¹Í™•Èð)ðQÉ…¹Í™•ÈÉ•©•Ñ•ð]!P€ÔÅ€½È™…Ñ…°ÍÑÉÕÑÕÉ••ÉÉ½Èð)ð]…É¹¥¹œð¹½¹™…Ñ…°ÍÑÉÕÑÕÉ••ÉÉ½ÈÍÕ …Ì…¸Õ¹µ…¹…•Á…É…µ•Ñ•Èð)ð‰½ÉÑ•ð]!P€Í€™É½´•¥Ñ¡•ÈÁ…ÉÑ¥¥Á…¹Ðð)ðQ¥µ•½ÕÐð…¸…Ñ¥Ù”Ñ¥µ•È•áÁ¥É•Ý¥Ñ¡½ÕÐ¥ÑÌÍÑ½ÁÁ¥¹œÑÉ…¹Í¥Ñ¥½¸ð)ð±½Í”Í•¹ÐðÁÉ½É…µµ•ÈÑÉ…¹Íµ¥ÑÑ•]!P€É€ì•Ù¥”µÍ¥‘”±½ÍÕÉ”¥Ì¹½Ð¥¹‘•Á•¹‘•¹Ñ±ä½¹™¥Éµ•‰äÑÉ…¹Íµ¥ÍÍ¥½¸…±½¹”ð)ðY•É¥™¥•ð„±…Ñ•È‘¥…¹½ÍÑ¥Œ¥¹Ñ•ÉÙ¥•Üµ…Ñ¡•ÌÑ¡”¥¹Ñ•¹‘••™™•Ñ¥Ù”ÍÑ…Ñ”ð()±½Í¥¹œ„Í•ÍÍ¥½¸‘½•Ì¹½Ð¡…¹”„É•©•Ñ¥½¸½ÈÑ¥µ•½ÕÐ¥¹Ñ¼ÍÕ•ÍÌ¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÀää()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½Ù…±¥‘…Ñ¥½¸¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒAÉ½É…µµ¥¹œY…±¥‘…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÀÅ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()AÉ½É…µµ¥¹œÙ…±¥‘…Ñ¥½¸¡•­Ì„½µÁ±•Ñ”¥¹Ñ•¹‘•½¹™¥ÕÉ…Ñ¥½¸……¥¹ÍÐÑ¡”…Ù…¥±…‰±”•Ù¥‘•¹”™½È½¹”É•Í½±Ù•A¡åÍ¥…°•Ù¥”‰•™½É”…¹äÝÉ¥Ñ”¥ÌÍ•¹Ð¸A…ÍÍ¥¹œ…Ñ…±½Õ”…¹•¹½‘¥¹œ¡•­Ì•ÍÑ…‰±¥Í¡•Ì½¹Í¥ÍÑ•¹äÝ¥Ñ Ñ¡½Í”Í½ÕÉ•Ì°¹½ÐÁÉ½Ù•¸ÉÕ¹Ñ¥µ”…•ÁÑ…¹”°Á•ÉÍ¥ÍÑ•¹”°½È½µÁ±•Ñ”½Ù•É…”½˜•Ù¥”½¹ÍÑÉ…¥¹ÑÌ¸Q¡”¹Õµ•É¥ŒÉ…¹•Ì¥¸=A8¹‘‰€‘•ÍÉ¥‰”™É…µ”µ™¥•±…Á…¥ÑäìÑ¡•ä‘¼¹½Ð•ÍÑ…‰±¥Í Ñ¡…Ð„Ù…±Õ”°=‰©•Ð°…‘‘É•ÍÌ°½ÈÁÉ½Á•ÉÑä¥ÌÙ…±¥™½È„Á…ÉÑ¥Õ±…È•Ù¥”¸()Y…±¥‘…Ñ¥½¸¥Ì„ÍÑ…•É•Í½±Ù•È¸… µ¥±•ÍÑ½¹”½¹ÍÕµ•Ì…¸•ÍÑ…‰±¥Í¡•½¹Ñ•áÐ…¹ÁÉ½‘Õ•Ì•Ù¥‘•¹”É•ÅÕ¥É•‰äÑ¡”¹•áÐµ¥±•ÍÑ½¹”¸%˜„É•ÅÕ¥É•É•ÍÕ±Ð¥Ì…µ‰¥Õ½ÕÌ½ÈÕ¹É•Í½±Ù•°ÍÑ½À‰•™½É”ÁÉ½É…µµ¥¹œ¸((ŒŒŒI•ÅÕ¥É•¥¹ÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€°Í½ÕÉ•€()MÑ…ÉÐÝ¥Ñ …¸¥µµÕÑ…‰±”Ý½É­¥¹œÉ•½É½¹Ñ…¥¹¥¹œ…±°…Ù…¥±…‰±”¥¹ÍÑ…±±…Ñ¥½¸•Ù¥‘•¹”è()ð%¹ÁÕÐðM½ÕÉ”ð)ð€´´´ð€´´´ð)ðµ…¹…•µ•¹Ð]!=€ðÍ•±•Ñ•‘¥…¹½ÍÑ¥Œ½ÁÉ½É…µµ¥¹œ™…µ¥±äð)ð•Ù¥”Í•±•Ñ½Èð‘¥…¹½ÍÑ¥Œ]!I€…¹°Ý¡•É”…Ù…¥±…‰±”°%59M%=8€ÄÍ€•Ù¥”%ð)ð¥‘•¹Ñ¥ÑäÁÉ½©•Ñ¥½¸ð‘¥…¹½ÍÑ¥Œ%59M%=8€Å€°™¥ÉµÝ…É”Ù•ÉÍ¥½¸°…¹¡…É‘Ý…É”Ù•ÉÍ¥½¸ð)ð5½‘Õ±”ÁÉ½©•Ñ¥½¸ð•Ù•Éä%59M%=8€ÌÁ€É•½Éð)ð…‘‘É•ÍÌÁÉ½©•Ñ¥½¸ð•Ù•Éä%59M%=8€ÌÉ€É•½Éð)ðÁ…É…µ•Ñ•ÈÁÉ½©•Ñ¥½¸ð•Ù•Éä%59M%=8€ÌÕ€É•½É…¹…¹ä%59M%=8€ÌÄÁ€É•½Éð)ð¥¹Ñ•¹‘•ÍÑ…Ñ”ð½µÁ±•Ñ”‘•Í¥É•5½‘Õ±”½=‰©•Ð±…å½ÕÐ°…‘‘É•ÍÍ•Ì°…¹ÁÉ½Á•ÉÑäÙ…±Õ•Ìð()I•Ñ…¥¸É…Ü™É…µ•Ì‰•Í¥‘”‘•½‘•Ù…±Õ•Ì¸¼¹½ÐÉ•Á±…”…¸Õ¹É•Í½±Ù•™¥•±Ý¥Ñ „Õ•ÍÍ•…Ñ…±½Õ”¥‘•¹Ñ¥™¥•È¸((ŒŒŒ5¥±•ÍÑ½¹”½Ù•ÉÙ¥•Ü()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()ð5¥±•ÍÑ½¹”ð½…°ðI•ÅÕ¥É•½ÕÑÁÕÐð)ð€´´´ð€´´´ð€´´´ð)ð€ÄðI•Í½±Ù”Ñ¡”¥¹ÍÑ…±±••Ù¥”ð½¹”¥Ñ•´½™¥ÉµÝ…É”½¹Ñ•áÐ½È…¸•áÁ±¥¥Ð…µ‰¥Õ¥ÑäÍ•Ðð)ð€ÈðI•Í½±Ù”Ñ¡”5½‘Õ±”ð½¹”•Ù¥”µ±½…°Í±½Ñ€…¹¥ÑÌ…Ñ…±½Õ”Á±…•µ•¹Ðð)ð€ÌðI•Í½±Ù”Ñ¡”ÕÉÉ•¹ÐÉ½±”ð•¹…‰±•É•Õ±…È=‰©•Ð½È‘¥Í…‰±•5½‘Õ±”ÌY¥É¥¸=‰©•Ðð)ð€ÐðAÉ½Ù”Ñ¡”Ñ…É•Ð=‰©•Ð¥Ì…Ù…¥±…‰±”ð½¹”Á•Éµ¥ÑÑ•Ñ…É•Ð=‰©•Ð…¹=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸ð)ð€Ôð	Õ¥±Ñ¡”ÁÉ½Á•ÉÑä‘¥Ñ¥½¹…Éäð…ÁÁ±¥…‰±”=‰©•Ð´…¹™¥ÉµÝ…É”µÍ½Á•9}=9€‘•™¥¹¥Ñ¥½¹Ìð)ð€ØðÍÑ…‰±¥Í ÝÉ¥Ñ”•±¥¥‰¥±¥ÑäðÝÉ¥Ñ…‰±”°Ù¥Í¥‰±”°™¥á•°¡¥‘‘•¸°½È½¹‘¥Ñ¥½¹…°ÍÑ…ÑÕÌð)ð€Üð	Õ¥±Ñ¡”‰…Í”Ù…±Õ”‘½µ…¥¸ð•¹Õµ•É…Ñ•Ù…±Õ•Ì½È¹Õµ•É¥Œ‰½Õ¹‘Ì™É½´9}=9}I9€ð)ð€àðÁÁ±ä½¹Ñ•áÑÕ…°™¥±Ñ•ÉÌð=‰©•Ð½™¥ÉµÝ…É”µÍÁ•¥™¥Œ•™™•Ñ¥Ù”‘½µ…¥¸ð)ð€äðÁÁ±ä½¹‘¥Ñ¥½¹Ì…¹½¹Ù•ÉÍ¥½¹ÌðÍ•±•Ñ•‰É…¹¡•Ì…¹•¹½‘•Ù…±Õ”ð)ð€ÄÀðÁÁ±ä±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•ÌðÉ½ÍÌµÁÉ½Á•ÉÑäµÙ…±¥…¹‘¥‘…Ñ”½¹™¥ÕÉ…Ñ¥½¸ð)ð€ÄÄðY…±¥‘…Ñ”…‘‘É•ÍÍ•ÌðÙ…±¥MeM€½I€•¹½‘¥¹œ™½ÈÑ¡”É•Í½±Ù•=‰©•Ðð)ð€ÄÈð±…ÍÍ¥™äÁ¡åÍ¥…°É•ÁÉ•Í•¹Ñ…Ñ¥½¸ðÁ¡åÍ¥…±±äÉ•ÁÉ•Í•¹Ñ…‰±”°½ÕÑÍ¥‘”Ñ¡”•ÍÑ…‰±¥Í¡•Á¡åÍ¥…°‘½µ…¥¸°½ÈÕ¹É•Í½±Ù•ð)ð€ÄÌð	Õ¥±Ý¥É”Ù…±Õ•ÌðÙ…±¥‘…Ñ•-e=€°MeM€½I€°…¹%9a€½Y1}AI€ÑÕÁ±•Ìð)ð€ÄÐðY…±¥‘…Ñ”Ñ¡”½µÁ±•Ñ”ÑÉ…¹Í™•Èð¥¹Ñ•É¹…±±ä½¹Í¥ÍÑ•¹ÐÉ•Á±…•µ•¹ÐÁ…å±½……¹Ù•É¥™¥…Ñ¥½¸Á±…¸ð()Q¡”µ¥±•ÍÑ½¹•Ì…É”‘•Á•¹‘•¹¥•Ì°¹½Ðµ•É•±ä„½¹Ù•¹¥•¹Ð½É‘•È¸½È•á…µÁ±”°…¸%9a€…¹¹½Ð‰”É•Í½±Ù•Í…™•±ä‰•™½É”Ñ¡”=‰©•Ð°™¥ÉµÝ…É”°…¹Í±½Ñ€…É”­¹½Ý¸¸((ŒŒŒ€Ä¸I•Í½±Ù”Ñ¡”¥¹ÍÑ…±±••Ù¥”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÀÑ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÀÕ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()ÍÑ…‰±¥Í Ñ¡”…Ñ…±½Õ”½¹Ñ•áÐ½ÉÉ•ÍÁ½¹‘¥¹œÑ¼Ñ¡”¥¹ÍÑ…±±•A¡åÍ¥…°•Ù¥”Ý¥Ñ¡½ÕÐ½¹™ÕÍ¥¹œÁÉ½Ñ½½°Ù…±Õ•ÌÝ¥Ñ ‘…Ñ…‰…Í”ÁÉ¥µ…Éä­•åÌ¸((ŒŒŒŒAÉ½•‘ÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€((Ä¸UÍ”Ñ¡”µ…¹…•µ•¹Ð]!=€Ñ¼Í•±•ÐÑ¡”…ÁÁ±¥…‰±”‘¥…¹½ÍÑ¥Œ™…µ¥±ä¸(È¸•½‘”%59M%=8€Å€…½É‘¥¹œÑ¼Ñ¡…Ð™…µ¥±ä¸(Ì¸I•Í½±Ù”¥ÑÌ¥Ñ•´½µ½‘•°Ù…±Õ”Ñ¡É½Õ Ñ¡”‘½Õµ•¹Ñ•¥Ñ•´…¹ÍåÍÑ•´…ÍÍ½¥…Ñ¥½¹Ì¸(Ð¸I•Í½±Ù”Ñ¡”…¹‘¥‘…Ñ”A¡åÍ¥…°•Ù¥”É•½É‘Ì…¹ÕÍ”9}Y%¹¹…µ•€…ÌÑ¡”ÍÑ…¹‘…É•Ù¥”‘•ÍÉ¥ÁÑ¥½¸¸(Ô¸UÍ”Ñ¡”É•Á½ÉÑ•™¥ÉµÝ…É”Ù•ÉÍ¥½¸Ñ¼¹…ÉÉ½ÜÑ¡”…ÁÁ±¥…‰±”¥Ñ•´½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸¸AÉ•Í•ÉÙ”¡…É‘Ý…É”…¹µ¥É½½¹ÑÉ½±±•ÈÙ•ÉÍ¥½¹Ì…Ì½‰Í•ÉÙ…Ñ¥½¹ÌìÕÍ”Ñ¡•´™½ÈÍ•±•Ñ¥½¸½¹±äÝ¡•¸…¸¥¹‘•Á•¹‘•¹Ñ±ä•ÍÑ…‰±¥Í¡•µ…ÁÁ¥¹œ•á¥ÍÑÌ¸(Ø¸AÉ•Í•ÉÙ”µÕ±Ñ¥Á±”M-T…¹‘¥‘…Ñ•ÌÝ¡•¸Í•Ù•É…°…Ñ…±½Õ”¥Ñ•µÌÍ¡…É”Ñ¡”Í…µ”¥µÁ±•µ•¹Ñ…Ñ¥½¸¥‘•¹Ñ¥Ñä¸(Ü¸I•Ñ…¥¸Ñ¡”¥¹ÍÑ…±±••Ù¥”%™É½´%59M%=8€ÄÍ€Í•Á…É…Ñ•±ä™É½´•Ù•Éä…Ñ…±½Õ”¥‘•¹Ñ¥™¥•È¸()%59M%=8€Å€Y1U€È¥Ì9}=9€°Ñ¡”Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈµÁ½Í¥Ñ¥½¸½Õ¹Ð¸¼¹½ÐÕÍ”¥Ð…Ì„•Ù¥”±…ÍÌ°=‰©•Ð°Y¥É¥¸=‰©•Ð°½È™¥ÉµÝ…É”­•ä¸((ŒŒŒŒ5¥±•ÍÑ½¹”½ÕÑÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()I•½É…Ð±•…ÍÐè((´‘¥…¹½ÍÑ¥Œ™…µ¥±ä…¹]!=€ì(´É…Ü…¹‘•½‘•¥‘•¹Ñ¥ÑäÁÉ½©•Ñ¥½¸ì(´¥Ñ•´½µ½‘•°¥‘•¹Ñ¥Ñäì(´…¹‘¥‘…Ñ”M-TÍ•Ðì(´É•Í½±Ù•™¥ÉµÝ…É”É•½É…¹Ù•ÉÍ¥½¸•Ù¥‘•¹”ì(´¥¹ÍÑ…±±••Ù¥”%ì(´Õ¹É•Í½±Ù•¥‘•¹Ñ¥Ñä…µ‰¥Õ¥Ñ¥•Ì¸((ŒŒŒŒMÑ½À½¹‘¥Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()MÑ½À¥˜¹¼…Ñ…±½Õ”¥Ñ•´½È™¥ÉµÝ…É”…¸‰”©ÕÍÑ¥™¥•¸%˜Í•Ù•É…°M-UÌÉ•µ…¥¸‰ÕÐÍ¡…É”Ñ¡”Í…µ”É•±•Ù…¹Ð™¥ÉµÝ…É”…Á…‰¥±¥Ñä°Ù…±¥‘…Ñ¥½¸µ…ä½¹Ñ¥¹Õ”½¹±äÝ¥Ñ Ñ¡…Ð½µµ½¸…Á…‰¥±¥Ñäì‘¼¹½Ð±…¥´„Õ¹¥ÅÕ”M-T¸()M•”m•Ù¥”%‘•¹Ñ¥Ñåt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´Äµ‘•Ù¥”µ¥‘•¹Ñ¥Ñä¹µ¤…¹mA¡åÍ¥…°•Ù¥•t ¸¸½‘•Ù¥”µµ½‘•°½Á¡åÍ¥…°µ‘•Ù¥•Ì¹µ¤¸((ŒŒŒ€È¸I•Í½±Ù”Ñ¡”5½‘Õ±”…¹Í±½Ñ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÀå€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()	¥¹Ñ¡”¥¹Ñ•¹‘•¡…¹”Ñ¼½¹”™¥ÉµÝ…É”µ•áÁ½Í•5½‘Õ±”…¹Ñ¡”¹Õµ•É¥ŒÍ±½Ñ€…ÉÉ¥•‰äÁÉ½É…µµ¥¹œ™É…µ•Ì¸((ŒŒŒŒAÉ½•‘ÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€((Ä¸UÍ”‘¥…¹½ÍÑ¥Œ%59M%=8€ÌÀ¹M1=Q€…ÌÑ¡”•Ù¥”µ±½…°Í±½Ñ€¹Õµ‰•È¸(È¸½ÉÉ•±…Ñ”¥ÐÝ¥Ñ …Ñ…±½Õ”Á±…•µ•¹ÐÍÕ …Ì9}M1=QL¹™¥ÉÍÑ}Í±½Ñ€¸(Ì¸I•Í½±Ù”Ñ¡”É•±•Ù…¹ÐM}=	)Q}%I5]I€…¹Í±½ÐÉ•½É‘Ì™½ÈÑ¡”Í•±•Ñ•™¥ÉµÝ…É”¸(Ð¸I•Ñ…¥¸U$µÙ¥Í¥‰±”5½‘Õ±”¹Õµ‰•É¥¹œ½¹±ä…ÌÁÉ•Í•¹Ñ…Ñ¥½¸µ•Ñ…‘…Ñ„¸(Ô¸¼¹½ÐÍå¹Ñ¡•Í¥é”5½‘Õ±•Ìµ•É•±ä‰•…ÕÍ”9}%I5]I¹Í±½ÑÍ€‘•±…É•Ì„…Á…¥Ñä¸((ŒŒŒŒ5¥±•ÍÑ½¹”½ÕÑÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()AÉ½‘Õ”½¹”5½‘Õ±”½¹Ñ•áÐ½¹Ñ…¥¹¥¹œè((´¥¹ÍÑ…±±••Ù¥”…¹™¥ÉµÝ…É”ì(´ÁÉ½Ñ½½°Í±½Ñ€ì(´µ…Ñ¡¥¹œ…Ñ…±½Õ”Í±½ÐÉ•½É‘Ìì(´ÕÉÉ•¹Ð%59M%=8€ÌÁ€ÍÑ…Ñ”ì(´…ÍÍ½¥…Ñ•%59M%=8€ÌÉ€…¹€ÌÕ€É•½É‘Ìì(´™¥á•µ=‰©•Ð…¹Í±½Ðµ½¹‘¥Ñ¥½¸µ•Ñ…‘…Ñ„¸((ŒŒŒŒMÑ½À½¹‘¥Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()MÑ½À¥˜Ñ¡”Í±½Ñ€‘½•Ì¹½Ð•á¥ÍÐ™½ÈÑ¡”É•Í½±Ù•™¥ÉµÝ…É”½È¥˜Í•Ù•É…°¥¹½µÁ…Ñ¥‰±”…Ñ…±½Õ”Á±…•µ•¹ÑÌÉ•µ…¥¸¸((ŒŒŒ€Ì¸I•Í½±Ù”Ñ¡”ÕÉÉ•¹Ð=‰©•Ð½ÈY¥É¥¸=‰©•Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄÑ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄÕ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()%¹Ñ•ÉÁÉ•ÐÑ¡”ÕÉÉ•¹Ð%59M%=8€ÌÀ¹-e=€¥¸Ñ¡”½ÉÉ•Ð•áÑ•É¹…°¹Õµ‰•ÈÍÁ…”¸()ðMQQ€ðI•Í½±Ù”-e=€……¥¹ÍÐð5•…¹¥¹œð)ð€´´´ð€´´´ð€´´´ð)ð€Á€ð9}-e}=	)P¹­•å}½‰©•Ñ€ð•¹…‰±•5½‘Õ±”ìÉ•Õ±…È½¹™¥ÕÉ•=‰©•Ðð)ð€Å€ð9}Y%I%9}=	)P¹Ù¥É¥¹}­•å}½‰©•Ñ€ð‘¥Í…‰±•5½‘Õ±”ìY¥É¥¸=‰©•Ðð()9•¥Ñ¡•ÈÙ…±Õ”¥Ì…¸¥¹Ñ•É¹…°‘…Ñ…‰…Í”ÁÉ¥µ…Éä­•ä¸1¥­•Ý¥Í”°ÁÉ½Ñ½½°M1=Q€¥Ì¹½Ð9}M1=QL¹¥‘}Í±½Ñ€¸()½È„‘¥Í…‰±•5½‘Õ±”°É•Ñ…¥¸Ñ¡”Y¥É¥¸=‰©•Ð…ÌÑ¡”É½±”½¹ÍÑÉ…¥¹Ð™É½´Ý¡¥ Á•Éµ¥ÑÑ•É•Õ±…È=‰©•ÑÌÝ¥±°‰”‘•É¥Ù•¸¼¹½ÐÍ•¹¥ÑÌÙ¥É¥¹}­•å}½‰©•Ñ€…Ì„Ñ…É•Ð-e=€µ•É•±ä‰•…ÕÍ”¥ÐÝ…ÌÉ•Á½ÉÑ•‘¥…¹½ÍÑ¥…±±ä¸((ŒŒŒŒ5¥±•ÍÑ½¹”½ÕÑÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄÙ€()AÉ½‘Õ”•á…Ñ±ä½¹”½˜è((´„É•Í½±Ù•ÕÉÉ•¹ÐÉ•Õ±…È=‰©•Ð™½È…¸•¹…‰±•5½‘Õ±”ì½È(´„É•Í½±Ù•Y¥É¥¸=‰©•ÐÝ¥Ñ ¥ÑÌ™Õ¹Ñ¥½¹…°É½±”™½È„‘¥Í…‰±•5½‘Õ±”¸()MÑ½À¥˜MQQ€¥Ì…‰Í•¹Ð½È¥˜-e=€‘½•Ì¹½ÐÉ•Í½±Ù”Õ¹¥ÅÕ•±ä¥¸Ñ¡”Í•±•Ñ•¹…µ•ÍÁ…”¸()M•”m%59M%=8€ÌÁ€è5½‘Õ±•Ì…¹=‰©•ÑÍt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´ÌÀµµ½‘Õ±•Ì¹µ¤¸((ŒŒŒ€Ð¸AÉ½Ù”Ñ…É•Ð=‰©•Ð…Ù…¥±…‰¥±¥Ñä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄÝ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()I•‘Õ”Ñ¡”±½‰…°=‰©•Ð…Ñ…±½Õ”Ñ¼Ñ¡”Í•ÐÍÕÁÁ½ÉÑ•‰äÑ¡¥Ì™¥ÉµÝ…É”°5½‘Õ±”°…¹ÕÉÉ•¹Ð½¹™¥ÕÉ…‰±”É½±”¸((ŒŒŒŒAÉ½•‘ÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÄå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€((Ä¸%˜Ñ¡”5½‘Õ±”¥Ì‘¥Í…‰±•°•¹Õµ•É…Ñ”…¹‘¥‘…Ñ•ÌÉ•±…Ñ•Ñ¼¥ÑÌY¥É¥¸=‰©•ÐÑ¡É½Õ M}=	)Q}Y%I%9}=	)Q€¸(È¸%¹Ñ•ÉÍ•ÐÑ¡…ÐÍ•ÐÝ¥Ñ =‰©•ÑÌÉ•±…Ñ•Ñ¼Ñ¡”É•Í½±Ù•™¥ÉµÝ…É”Ñ¡É½Õ M}=	)Q}%I5]I€¸(Ì¸%¹Ñ•ÉÍ•Ð……¥¸Ý¥Ñ =‰©•ÑÌÁ±…•…ÐÑ¡”É•Í½±Ù•Í±½Ñ€Ñ¡É½Õ 9}M1=QM€¸(Ð¸ÁÁ±ä™¥á•‘}­½€…¹Í±½Ðµ½¹‘¥Ñ¥½¸µ•Ñ…‘…Ñ„¸(Ô¸%˜Ñ¡”5½‘Õ±”¥Ì…±É•…‘ä½¹™¥ÕÉ•°‘•Ñ•Éµ¥¹”Ý¡•Ñ¡•ÈÉ•Á±…•µ•¹Ð¥ÌÁ•Éµ¥ÑÑ•ìÕÉÉ•¹Ðµ•µ‰•ÉÍ¡¥À…±½¹”‘½•Ì¹½ÐÁÉ½Ù”ÝÉ¥Ñ…‰¥±¥Ñä¸(Ø¸M•±•ÐÑ¡”Ñ…É•Ð‰ä•áÑ•É¹…°9}-e}=	)P¹­•å}½‰©•Ñ€°‰ÕÐÉ•Ñ…¥¸¥ÑÌ¥¹Ñ•É¹…°¥‘}­•å}½‰©•Ñ€™½È…Ñ…±½Õ”©½¥¹Ì¸(Ü¸I•Ñ…¥¸Ñ¡”É•Í½±Ù•M}=	)Q}%I5]I¹¥‘}½‰©•Ñ}™¥ÉµÝ…É•€ì½¹Ñ•áÑÕ…°™¥±Ñ•ÉÌ‘•Á•¹½¸¥Ð¸()½¹•ÁÑÕ…±±äè()Ñ•áÐ)Á•Éµ¥ÑÑ•Ñ…É•ÑÌ€ô(€€€Y¥É¥¸µ=‰©•Ð…¹‘¥‘…Ñ•Ì°Ý¡•¸…ÁÁ±¥…‰±”(€ƒŠ"¤™¥ÉµÝ…É”µÍÕÁÁ½ÉÑ•=‰©•ÑÌ(€ƒŠ"¤Í±½Ñ€µÍÕÁÁ½ÉÑ•=‰©•ÑÌ(€ƒŠ"¤Í…Ñ¥Í™¥•™¥á•½½¹‘¥Ñ¥½¹…°½¹ÍÑÉ…¥¹ÑÌ)€((ŒŒŒŒ5¥±•ÍÑ½¹”½ÕÑÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()AÉ½‘Õ”è((´½¹”Ñ…É•Ð¥‘}­•å}½‰©•Ñ€ì(´¥ÑÌ•áÑ•É¹…°ÁÉ½É…µµ¥¹œ­•å}½‰©•Ñ€ì(´½¹”…ÁÁ±¥…‰±”=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸ì(´½¹”½µÁ…Ñ¥‰±”Í±½ÐÁ±…•µ•¹Ðì(´Ñ¡”•Ù¥‘•¹”Ñ¡…Ð…‘µ¥ÑÑ•¥ÐÑ¼Ñ¡”Á•Éµ¥ÑÑ•Í•Ð¸((ŒŒŒŒMÑ½À½¹‘¥Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈÅ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()I•©•ÐÑ¡”Ñ…É•Ð¥˜¥Ð‘¥Í…ÁÁ•…ÉÌ…Ð…¹ä¥¹Ñ•ÉÍ•Ñ¥½¸¸¼¹½Ð™…±°‰…¬Ñ¼Ñ¡”±½‰…°=‰©•Ð±¥ÍÐ¸()M•”m=‰©•ÐAÉ½É…µµ¥¹t¡½‰©•ÐµÁÉ½É…µµ¥¹œ¹µ¤°m=‰©•ÑÍt ¸¸½‘•Ù¥”µµ½‘•°½½‰©•ÑÌ¹µ¤°…¹mY¥É¥¸=‰©•ÑÍt ¸¸½‘•Ù¥”µµ½‘•°½Ù¥É¥¸µ½‰©•ÑÌ¹µ¤¸((ŒŒŒ€Ô¸	Õ¥±Ñ¡”…ÁÁ±¥…‰±”ÁÉ½Á•ÉÑä‘¥Ñ¥½¹…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈÉ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°¹½Ð…ÁÁ±¥…‰±•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()½±±•Ð•Ù•Éä½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¸Ñ¡…Ð…¸‘•ÍÉ¥‰”Ñ¡”É•Í½±Ù•=‰©•Ð½™¥ÉµÝ…É”½¹Ñ•áÐ¸()9}=9€ÕÍ•ÌÑÝ¼•á±ÕÍ¥Ù”½Ý¹•ÉÍ¡¥ÀÍ½Á•Ìè()ðM½Á”ðM•±•Ñ¥½¸ð)ð€´´´ð€´´´ð)ð=‰©•ÐÁÉ½Á•ÉÑäðÉ•Í½±Ù•¥‘}­•å}½‰©•Ñ€…¹¥‘}™¥ÉµÝ…É”€ô€Á€ð)ð¥ÉµÝ…É”ÁÉ½Á•ÉÑäð¥‘}­•å}½‰©•Ð€ô€Á€…¹É•Í½±Ù•¥‘}™¥ÉµÝ…É•€ð()½±±•ÐÑ¡•¥ÈÕ¹¥½¸è()ÍÅ°)M1P€¨)I=49}=9)]!I€¡¥‘}­•å}½‰©•Ð€ô€é½‰©•Ñ}¥9¥‘}™¥ÉµÝ…É”€ô€À¤(€€=H€¡¥‘}­•å}½‰©•Ð€ô€À9¥‘}™¥ÉµÝ…É”€ô€é™¥ÉµÝ…É•}¥¤)€()Q¡”é•É¼¥Ì„ƒŠq¹½Ð…ÁÁ±¥…‰±—ŠtÍ•¹Ñ¥¹•°°¹½Ð=‰©•Ð½È™¥ÉµÝ…É”%€À¸9•Ù•ÈÉ•ÅÕ¥É”‰½Ñ É•Í½±Ù•%Ì½¸Ñ¡”Í…µ”9}=9€É½Ü¸()%¹‘•àÑ¡”É•ÍÕ±Ñ¥¹œ‘¥Ñ¥½¹…Éä‰ä…Ð±•…ÍÐè((´Í½Á”ì(´9}=9¹¥‘}½¹™€ì(´¥‘á€ì(´Íåµ‰½±¥Œ¹…µ”ì(´Í•µ…¹Ñ¥ŒÑåÁ”ì(´‘…Ñ„ÑåÁ”ì(´Í±½Ñ€…¹=‰©•Ð½™¥ÉµÝ…É”½¹Ñ•áÐ¸()¸¥‘á€¥Ì¹½Ð±½‰…±±äÕ¹¥ÅÕ”¸%Ð‰•½µ•Ì„ÕÍ…‰±”%59M%=8€ÌÔ¹%9a€½¹±ä…™Ñ•ÈÑ¡¥Ì½¹Ñ•áÐ¡…Ì‰••¸É•Í½±Ù•¸()Q¡”Õ¹¥½¸¥Ì„…¹‘¥‘…Ñ”ÁÉ½Á•ÉÑä‘¥Ñ¥½¹…Éä°¹½Ð„±¥ÍÐ½˜ÝÉ¥Ñ…‰±”Á…É…µ•Ñ•ÉÌ¸%¸Á…ÉÑ¥Õ±…È°™¥ÉµÝ…É”Á¡åÍ¥…°™¥•±‘ÌÝ¥Ñ ¥‘à€ô€´Å€…¹¹½Ð‰”•µ¥ÑÑ•…Ì…¸Õ¹Í¥¹•%59M%=8€ÌÔ¹%9a€ì¹•¥Ñ¡•È„Í¡…É•Íåµ‰½°¹½È…Ñ…±½Õ”ÁÉ•Í•¹”•ÍÑ…‰±¥Í¡•ÌÑ¡•¥ÈÑÉ…¹Í™•È½Á•É…Ñ¥½¸¸((ŒŒŒŒ5¥±•ÍÑ½¹”½ÕÑÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈÑ€()AÉ½‘Õ”Ñ¡”½µÁ±•Ñ”½¹Ñ•áÐµÍÁ•¥™¥ŒÁÉ½Á•ÉÑä‘¥Ñ¥½¹…Éä…¹¥‘•¹Ñ¥™äÝ¡•Ñ¡•È•… ¥¹Ñ•¹‘•U$½ÁÉ½Á•ÉÑä½¹•ÁÐÉ•Í½±Ù•ÌÑ¼é•É¼°½¹”°½ÈÍ•Ù•É…°‘•™¥¹¥Ñ¥½¹Ì¸((ŒŒŒŒMÑ½À½¹‘¥Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈÕ€()U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°•Ù¥‘•¹•€((´é•É¼µ…Ñ¡•ÌèÕ¹É•Í½±Ù•½ÈÕ¹ÍÕÁÁ½ÉÑ•ÁÉ½Á•ÉÑäì(´½¹”µ…Ñ è½¹Ñ¥¹Õ”ì(´Í•Ù•É…°µ…Ñ¡•Ìè‘¥Í…µ‰¥Õ…Ñ”‰äÍ½Á”°Íåµ‰½°°Í•µ…¹Ñ¥ŒÑåÁ”°™¥±Ñ•È°U$‰•¡…Ù¥½È°½È…ÁÑÕÉ”•Ù¥‘•¹”‰•™½É”½¹Ñ¥¹Õ¥¹œ¸()M•”m½¹™¥ÕÉ…Ñ¥½¸AÉ½É…µµ¥¹t¡½¹™¥ÕÉ…Ñ¥½¸µÁÉ½É…µµ¥¹œ¹µ¤™½ÈÑ¡”ÝÉ¥Ñ”µ…ÁÁ¥¹œ¸((ŒŒŒ€Ø¸ÍÑ…‰±¥Í ÝÉ¥Ñ”•±¥¥‰¥±¥Ñä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈÙ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈÝ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäèµ…å€°Õ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()M•Á…É…Ñ”Ù…±Õ•ÌÑ¡…Ð•á¥ÍÐ¥¸Ñ¡”…Ñ…±½Õ”™É½´Ù…±Õ•ÌÑ¡…ÐÑ¡”ÁÉ½É…µµ•Èµ…äµ½‘¥™ä¸()½È•… É•Í½±Ù•9}=9€‘•™¥¹¥Ñ¥½¸°•Ù…±Õ…Ñ”è((´É•…‘}½¹±å€ì(´Ù¥Í¥‰±•€ì(´¡¥‘‘•¹€ì(´™¥á•µÙ…±Õ”‘…Ñ„ÑåÁ”ì(´ÁÉ½É•ÍÍ¥Ù”½½É‘•Èµ•Ñ…‘…Ñ„ì(´…ÁÁ±¥…‰±”Í±½Ð½¹‘¥Ñ¥½¹Ìì(´Ý¡•Ñ¡•ÈÑ¡”Ù…±Õ”¥Ì…±Õ±…Ñ•½È½µÁ¥±•‰ä5å!=5}MÕ¥Ñ”ì(´Ý¡•Ñ¡•È¥Ð¥ÌÉ•Á½ÉÑ•‰äÑ¡”•Ù¥”‰ÕÐ±…­Ì„•¹•É¥ŒÁÉ½É…µµ¥¹œ½Á•É…Ñ¥½¸¸()±…ÍÍ¥™äÑ¡”ÁÉ½Á•ÉÑä…Ìè()ðMÑ…ÑÕÌðAÉ½É…µµ¥¹œÑÉ•…Ñµ•¹Ðð)ð€´´´ð€´´´ð)ðÝÉ¥Ñ…‰±”ð…¹‘¥‘…Ñ”™½È„ÝÉ¥Ñ”ð)ð½¹‘¥Ñ¥½¹…°ðÝÉ¥Ñ…‰±”½¹±ä¥˜¥ÑÌ•¹…‰±¥¹œ½¹‘¥Ñ¥½¸¥ÌÍ…Ñ¥Í™¥•ð)ð™¥á•ðÁÉ•Í•ÉÙ”Ñ¡”‘•™¥¹•Ù…±Õ”ì‘¼¹½Ð½™™•È…É‰¥ÑÉ…Éä¥¹ÁÕÐð)ðÉ•…µ½¹±äð½µÁ…É”‘ÕÉ¥¹œÙ•É¥™¥…Ñ¥½¸‰ÕÐ‘¼¹½ÐÝÉ¥Ñ”ð)ð¡¥‘‘•¸ð‘¼¹½Ð…ÍÍÕµ”¥¹Ù…±¥ìÉ•Í½±Ù”Ñ¡”¡¥‘¥¹œ½¹‘¥Ñ¥½¸ð)ðÕ¹ÍÕÁÁ½ÉÑ•ð½µ¥Ð™É½´Ñ¡”Á…å±½…ð)ðÕ¹É•Í½±Ù•ð™…¥°±½Í•ð()Y¥Í¥‰¥±¥Ñä¥ÌÁÉ•Í•¹Ñ…Ñ¥½¸µ•Ñ…‘…Ñ„°¹½Ð‰ä¥ÑÍ•±˜Á•Éµ¥ÍÍ¥½¸Ñ¼ÝÉ¥Ñ”¸½¹Ù•ÉÍ•±ä°„¡¥‘‘•¸ÁÉ½Á•ÉÑä…¸ÍÑ¥±°Á…ÉÑ¥¥Á…Ñ”¥¸½¹Ù•ÉÍ¥½¹Ì½È±¥¹­•ÉÕ±•Ì¸((ŒŒŒ€Ü¸	Õ¥±Ñ¡”‰…Í”Ù…±Õ”‘½µ…¥¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈá€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÈå€()•É¥Ù”Ñ¡”Ù…±Õ•Ì…±±½Ý•‰äÑ¡”Í•±•Ñ•½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¸‰•™½É”½¹Ñ•áÑÕ…°¹…ÉÉ½Ý¥¹œ¸()UÍ”9}=9}Q}QeA€Ñ¼¡½½Í”¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸…¹9}=9}I9€Ñ¼½¹ÍÑÉÕÐÑ¡”‰…Í”‘½µ…¥¸¸((ŒŒŒŒ¹Õµ•É…Ñ•‘½µ…¥¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌÁ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()]¡•¸É…¹”É½ÝÌÁÉ½Ù¥‘”‘¥ÍÉ•Ñ”Ù…±Õ•Ì°É•Ñ…¥¸™½È•… µ•µ‰•Èè((´ÍÑ½É•Ù…±Õ”ì(´‘¥ÍÁ±…ä¹…µ”ì(´‘•™…Õ±Ð™±…œì(´½É‘•É¥¹œì(´‘¥¥ÐÝ¥‘Ñ ì(´ÍÑ•À…¹µ¥¸½µ…àµ•Ñ…‘…Ñ„Ý¡•É”ÁÉ•Í•¹Ð¸()¼¹½ÐÙ…±¥‘…Ñ”‰ä‘¥ÍÁ±…äÑ•áÐ…±½¹”ìÑ¡”Ý¥É”…ÉÉ¥•ÌÑ¡”•¹½‘•ÍÑ½É•Ù…±Õ”¸((ŒŒŒŒ9Õµ•É¥Œ‘½µ…¥¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌÅ€()]¡•¸„‘•™¥¹¥Ñ¥½¸ÍÕÁÁ±¥•Ì¹Õµ•É¥Œ‰½Õ¹‘Ì°Ù…±¥‘…Ñ”è()Ñ•áÐ)µ¥¹}Ù…±Õ”ƒŠ&…¹‘¥‘…Ñ”ƒŠ&µ…á}Ù…±Õ”(¡…¹‘¥‘…Ñ”€´µ¥¹}Ù…±Õ”¤µ½ÍÑ•À€ô€À)€()ÁÁ±äÑ¡”ÍÑ•ÀÑ•ÍÐ½¹±äÝ¡•¸„µ•…¹¥¹™Õ°¹½¹é•É¼ÍÑ•À¥Ì‘•™¥¹•¸AÉ•Í•ÉÙ”‘¥¥ÐµÝ¥‘Ñ …¹Á…‘‘¥¹œÍ•Á…É…Ñ•±ä™É½´¹Õµ•É¥ŒÙ…±¥‘¥Ñä¸((ŒŒŒŒ¥á•°	½½±•…¸°Á…‘‘•°…¹ÕÍ•ÈÙ…±Õ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌÉ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€((´	½½±•…¸ÁÉ½Á•ÉÑ¥•ÌµÕÍÐÕÍ”Ñ¡”•¹½‘•Ù…±Õ•Ì•ÍÑ…‰±¥Í¡•‰äÑ¡•¥È‘•™¥¹¥Ñ¥½¸ì‘¼¹½Ð…ÍÍÕµ”•Ù•Éä	½½±•…¸ÕÍ•Ì…É‰¥ÑÉ…Éä¹½¹é•É¼ÑÉÕÑ ¸(´¥á•Ù…±Õ•Ì…É”¹½Ð•¹•É…°¥¹ÁÕÐ‘½µ…¥¹Ì¸(´I…¹•}A…‘€Ù…±Õ•ÌÉ•ÅÕ¥É”‰½Ñ ¹Õµ•É¥ŒÙ…±¥‘…Ñ¥½¸…¹Ý¥‘Ñ µÁÉ•Í•ÉÙ¥¹œ•¹½‘¥¹œ¸(´ÕÍ•É}Ù…±Õ•€‘½•Ì¹½Ðµ•…¸Õ¹É•ÍÑÉ¥Ñ•ì™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¹Ì°…¹ÁÉ½Ñ½½°…Á…¥ÑäÍÑ¥±°…ÁÁ±ä¸()µ¥ÍÍ¥¹œ9}=9}I9€É½Ü‘½•Ì¹½Ðµ…­”Ñ¡”™Õ±°Y1}AI€ÑÉ…¹ÍÁ½ÉÐÉ…¹”Ù…±¥¸((ŒŒŒŒ5¥±•ÍÑ½¹”½ÕÑÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌÍ€()AÉ½‘Õ”„‰…Í”‘½µ…¥¸Ý¥Ñ ÁÉ½Ù•¹…¹”‰…¬Ñ¼¥‘}½¹™€…¹Ñ¡”•á…ÐÉ…¹”É½ÝÌÕÍ•¸((ŒŒŒ€à¸ÁÁ±ä=‰©•Ð½™¥ÉµÝ…É”™¥±Ñ•ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌÑ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()9…ÉÉ½ÜÑ¡”‰…Í”ÁÉ½Á•ÉÑä‘½µ…¥¸™½ÈÑ¡”Á…ÉÑ¥Õ±…È=‰©•Ð¥µÁ±•µ•¹Ñ…Ñ¥½¸½¸Ñ¡”Í•±•Ñ•™¥ÉµÝ…É”¸((Ä¸I•Í½±Ù”Ñ¡”…ÁÁ±¥…‰±”M}=	)Q}%I5]I¹¥‘}½‰©•Ñ}™¥ÉµÝ…É•€™É½´µ¥±•ÍÑ½¹”€Ð¸(È¸¥¹9}%1QI€É½ÝÌÑ¡…Ð‰¥¹Ñ¡…Ð…ÍÍ½¥…Ñ¥½¸Ñ¼Ñ¡”É•Í½±Ù•9}=9¹¥‘}½¹™€¸(Ì¸ÁÁ±äÑ¡”É•±…Ñ•9}%1QI}I9€É½ÝÌ¸(Ð¸I•ÍÁ•ÐÑ¡”™¥±Ñ•ËŠeÌÝ¡½±•}É…¹•€‰•¡…Ù¥½È…ÌÉ•ÁÉ•Í•¹Ñ•‰äÑ¡”…Ñ…±½Õ”¸(Ô¸%¹Ñ•ÉÍ•ÐÑ¡”™¥±Ñ•É•‘½µ…¥¸Ý¥Ñ Ñ¡”‰…Í”‘½µ…¥¸¸(Ø¸¼¹½Ð½µ‰¥¹”™¥±Ñ•ÉÌ‰•±½¹¥¹œÑ¼…¹½Ñ¡•È=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸¸()½¹•ÁÑÕ…±±äè()Ñ•áÐ)•™™•Ñ¥Ù”‘½µ…¥¸€ô(€€€‰…Í”9}=9}I9‘½µ…¥¸(€ƒŠ"¤É…¹•Ì…‘µ¥ÑÑ•‰äÑ¡”…ÁÁ±¥…‰±”9}%1QH½¹Ñ•áÐ)€()%˜„É•±•Ù…¹Ð™¥±Ñ•È•á¥ÍÑÌ‰ÕÐ…¹¹½Ð‰”¥¹Ñ•ÉÁÉ•Ñ•°µ…É¬Ñ¡”ÁÉ½Á•ÉÑäÕ¹É•Í½±Ù•É…Ñ¡•ÈÑ¡…¸Í¥±•¹Ñ±äÕÍ¥¹œÑ¡”‰É½…‘•È‰…Í”É…¹”¸((ŒŒŒŒ5¥±•ÍÑ½¹”½ÕÑÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌÙ€()AÉ½‘Õ”Ñ¡”•™™•Ñ¥Ù”½¹Ñ•áÐµÍÁ•¥™¥Œ‘½µ…¥¸…¹É•Ñ…¥¸Ñ¡”™¥±Ñ•È…¹™¥±Ñ•ÈµÉ…¹”¥‘•¹Ñ¥™¥•ÉÌÑ¡…ÐÁÉ½‘Õ•¥Ð¸((ŒŒŒ€ä¸ÁÁ±äÍ±½Ð½¹‘¥Ñ¥½¹Ì…¹½¹Ù•ÉÍ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌÝ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌá€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()•Ñ•Éµ¥¹”Ý¡•Ñ¡•ÈÑ¡”Ñ…É•Ð=‰©•Ð½ÁÉ½Á•ÉÑä¥Ì…Ñ¥Ù”¥¸Ñ¡¥ÌÍ±½Ð…¹½¹Ù•ÉÐÑ¡”¥¹Ñ•¹‘•Í•µ…¹Ñ¥ŒÙ…±Õ”¥¹Ñ¼¥ÑÌ…Ñ…±½Õ”½Ý¥É”É•ÁÉ•Í•¹Ñ…Ñ¥½¸¸((Ä¸1½…M}M1=Q}=9%Q%=9€™½ÈÑ¡”É•Í½±Ù•Í±½ÐÁ±…•µ•¹Ð¸(È¸I•Í½±Ù”¥ÑÌ9}=9%Q%=9€¸(Ì¸½±±½ÜÑ¡”Í•±•Ñ•9}=9Y}IU1€±½¥Œ¸(Ð¸MÕÁÁ±ä…±°É•™•É•¹•¥Ñ•´µ±•Ù•°…¹=‰©•Ðµ±•Ù•°Íåµ‰½±Ì™É½´Ñ¡”…¹‘¥‘…Ñ”½¹™¥ÕÉ…Ñ¥½¸¸(Ô¸Ù…±Õ…Ñ”•áÁ±¥¥Ð½µÁ…É¥Í½¹Ì°Õ¹½¹‘¥Ñ¥½¹…°‰É…¹¡•Ì°…¹©ÕµÁÌ¥¸Ñ¡•¥ÈÍÑ½É•½É‘•È¸(Ø¸UÍ”=9}Me5	=1}I€Ý¡•É”¥Ð•áÁ±¥¥Ñ±äÉ•±…Ñ•Ì…¸¥Ñ•´Íåµ‰½°Ñ¼…¸=‰©•ÐÍåµ‰½°™½ÈÑ¡”ÍåÍÑ•´…¹Í±½Ð¸(Ü¸I•½ÉÑ¡”‰É…¹ Ñ…­•¸…¹Ñ¡”É•ÍÕ±Ñ¥¹œÙ…±Õ”¸()½¹Ù•ÉÍ¥½¸¥Ì¹½ÐÙ…±¥µ•É•±ä‰•…ÕÍ”¥ÑÌ½ÕÑÁÕÐ™¥ÑÌ€À¸¸ØÔÔÌÕ€¸I•Ù…±¥‘…Ñ”Ñ¡”½¹Ù•ÉÑ•É•ÍÕ±Ð……¥¹ÍÐÑ¡”•™™•Ñ¥Ù”‘½µ…¥¸¸()=9}Me5	=1}I€¥ÌÍÕÁÁ½ÉÑ¥¹œµ…ÁÁ¥¹œ•Ù¥‘•¹”°¹½Ð„±½‰…°Íåµ‰½°µ…±¥…ÌÑ…‰±”¸Íåµ‰½°½ÉÉ•ÍÁ½¹‘•¹”™É½´½¹”ÍåÍÑ•´½ÈÍ±½ÐµÕÍÐ¹½Ð‰”…ÁÁ±¥•Õ¹¥Ù•ÉÍ…±±ä¸((ŒŒŒŒ5¥±•ÍÑ½¹”½ÕÑÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÌå€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()AÉ½‘Õ”è((´Í…Ñ¥Í™¥•½Õ¹Í…Ñ¥Í™¥•½¹‘¥Ñ¥½¸ÍÑ…Ñ”ì(´ÉÕ±”Á…Ñ ì(´Í•µ…¹Ñ¥Œ¥¹ÁÕÐì(´½¹Ù•ÉÑ•…Ñ…±½Õ”Ù…±Õ”ì(´•Ù¥‘•¹”™½È…¹äÍåµ‰½°½ÉÉ•ÍÁ½¹‘•¹”¸()MÑ½À½¸„µ¥ÍÍ¥¹œ‘•Á•¹‘•¹ä°…µ‰¥Õ½ÕÌ‰É…¹ °±½½À°½ÈÕ¹µ…ÁÁ•½¹Ù•ÉÍ¥½¸½ÕÑÁÕÐ¸((ŒŒŒ€ÄÀ¸ÁÁ±ä±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐÁ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐÅ€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()Y…±¥‘…Ñ”‘•Á•¹‘•¹¥•ÌÑ¡…Ð…¹¹½Ð‰”‘•¥‘•™É½´½¹”ÁÉ½Á•ÉÑä¥¸¥Í½±…Ñ¥½¸¸()½È=‰©•ÑÌ½Ù•É•‰äÉÕ±•Ì¹‘ˆÍ€è((Ä¸½¹™¥É´Ñ¡”É•Í½±Ù••áÑ•É¹…°=‰©•Ð¹Õµ‰•È¥Ì½¹”½˜Ñ¡”=‰©•ÑÌÉ•ÁÉ•Í•¹Ñ•Ñ¡•É”¸(È¸	¥¹•áÁÉ•ÍÍ¥½¹ÌÍÕ …Ì€Å€°€É€°½È€ÈÅ€Ñ¼Ñ¡”½ÉÉ•ÍÁ½¹‘¥¹œÉ•Í½±Ù•9}=9¹¥‘á€½¹±äÝ¥Ñ¡¥¸Ñ¡…Ð=‰©•Ð½¹Ñ•áÐ¸(Ì¸Ù…±Õ…Ñ”Ñ¡”ÉÕ±”ÕÍ¥¹œÑ¡”½µÁ±•Ñ”…¹‘¥‘…Ñ”½¹™¥ÕÉ…Ñ¥½¸°¹½Ð½¹±äÑ¡”¡…¹•ÁÉ½Á•ÉÑä¸(Ð¸ÁÁ±ä¥Í…‰±•±¥¹­•‘A…É…µ•Ñ•É€‰•¡…Ù¥½ÈÑ¼‘•Á•¹‘•¹ÐÁÉ½Á•ÉÑ¥•Ì¸(Ô¸I”µÉÕ¸…™™•Ñ•‘½µ…¥¹Ì…¹ÝÉ¥Ñ”µ•±¥¥‰¥±¥Ñä±…ÍÍ¥™¥…Ñ¥½¹Ì…™Ñ•È„½¹ÑÉ½±±¥¹œÙ…±Õ”¡…¹•Ì¸()Q¡”ÕÉÉ•¹ÐÉÕ±•Ì¹‘ˆÍ€•Ù¥‘•¹”¥Ì±¥µ¥Ñ•Ñ¼Í•±•Ñ•Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°=‰©•ÑÌ¸%Ð¥Ì¹½Ð„•¹•É…°=‰©•Ð°]!=€°½ÈÁ…É…µ•Ñ•ÈÉ•¥ÍÑÉä¸((ŒŒŒŒ5¥±•ÍÑ½¹”½ÕÑÁÕÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐÉ€()AÉ½‘Õ”„½µÁ±•Ñ”…¹‘¥‘…Ñ”ÁÉ½Á•ÉÑäÍ•Ð¥¸Ý¡¥ …±°É•™•É•¹•‘•Á•¹‘•¹¥•Ì¡…Ù”Ù…±Õ•Ì…¹¹¼•¹…‰±•ÉÕ±”¥ÌÙ¥½±…Ñ•¸((ŒŒŒ€ÄÄ¸Y…±¥‘…Ñ”…¸…‘‘É•ÍÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐÍ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐÑ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()AÉ½Ù”Ñ¡…Ð½¹”5½‘Õ±”…‘‘É•ÍÌ…¸‰”•¹½‘•…Ì„Ù…±¥%59M%=8€ÌÉ€ÝÉ¥Ñ”¸((Ä¸I•Í½±Ù”Ñ¡”Ñ…É•Ð=‰©•ÓŠeÌ™Õ¹Ñ¥½¹…°ÍåÍÑ•´¸(È¸M•±•ÐÑ¡”…ÁÁ±¥…‰±”=A8¹‘‰€…‘‘É•ÍÌÉÕ±”ÕÍ¥¹œÑ¡”µ…¹…•µ•¹Ð™…µ¥±ä…¹=‰©•Ð½‘•Ù¥”™…µ¥±ä¸(Ì¸I•Í½±Ù”Ñ¡”ÉÕ±—ŠeÌ½µÁ½¹•¹ÐÍÑÉÕÑÕÉ”…¹™¥á•Ù…±Õ•Ì¸(Ð¸Y…±¥‘…Ñ”•Ù•Éä½µÁ½¹•¹Ð‘½µ…¥¸…¹±•Ù•°ÉÕ±”¸(Ô¸ÁÁ±äÉ•ÅÕ¥É•ÁÉ•™¥á•Ì°Á…‘‘¥¹œ°Ù…±¥‘¥Ñä½¹‘¥Ñ¥½¹Ì°…¹…‘Ù…¹•½™™Í•ÑÌ¸(Ø¸ÍÑ…‰±¥Í Ñ¡”=‰©•ÐµÍÁ•¥™¥Œ¹Õµ•É¥ŒI€•¹½‘¥¹œ¥¹‘•Á•¹‘•¹Ñ±ä½˜Ñ¡”™Õ¹Ñ¥½¹…°½Èµ…¹…•µ•¹Ð]!I€ÍÑÉ¥¹œ¸¸…‘‘É•ÍÌµÉÕ±”Ñ•µÁ±…Ñ”…±½¹”‘½•Ì¹½Ð…ÕÑ¡½É¥é”½Áå¥¹œÉ½ÕÀµ…É­•ÉÌ½ÈÉ½ÕÑ¥¹œÍÕ™™¥á•Ì¥¹Ñ¼I€¸(Ü¸I•Í½±Ù”MeM€¥¹‘•Á•¹‘•¹Ñ±äì‘¼¹½Ð…ÍÍÕµ”¥Ð•ÅÕ…±Ì„™Õ¹Ñ¥½¹…°]!=€°‘¥…¹½ÍÑ¥Œ]!=€°½È•¥Ñ¡•È‘…Ñ…‰…Í—ŠeÌ¥¹Ñ•É¹…°ÍåÍÑ•´%¸(à¸•½‘”Ñ¡”•¹•É…Ñ•Ù…±Õ”……¥¸…¹É•ÅÕ¥É”„É½Õ¹µÑÉ¥Àµ…Ñ ¸()Q¡”É•ÍÕ±Ð¥ÌÑ¡”ÑÕÁ±”è()Ñ•áÐ(¡M1=P°MeL°É…ÜH°‘•½‘•½µÁ½¹•¹ÑÌ°…‘‘É•ÍÌµÉÕ±”¥‘•¹Ñ¥Ñä¤)€()¼¹½Ð™½É”•Ù•Éä™…µ¥±ä¥¹Ñ¼€½A1€¸Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°°8½8¬°¹•Éä5…¹…•µ•¹Ð°•ÍÌ½¹ÑÉ½°°¥¹Ñ•É™…”°É½ÕÀ°…¹•¹Ù¥É½¹µ•¹Ð™½ÉµÌÕÍ”‘¥ÍÑ¥¹ÐÉ…µµ…ÉÌ¸()M•”m‘‘É•ÍÌAÉ½É…µµ¥¹t¡…‘‘É•ÍÌµÁÉ½É…µµ¥¹œ¹µ¤…¹m‘‘É•ÍÌ¥Í½Ù•Éåt ¸¸½‘¥…¹½ÍÑ¥Ì½…‘‘É•ÍÌµ‘¥Í½Ù•Éä¹µ¤¸((ŒŒŒ€ÄÈ¸±…ÍÍ¥™äÁ¡åÍ¥…°É•ÁÉ•Í•¹Ñ…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐÕ€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€°Í½ÕÉ•€()•Ñ•Éµ¥¹”Ý¡•Ñ¡•ÈÑ¡”•™™•Ñ¥Ù”ÁÉ½Á•ÉÑä½Õ±…±Í¼‰”É•ÁÉ•Í•¹Ñ•‰äÁ¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÉÌ¸Q¡¥Ì‘½•Ì¹½Ð‘•Ñ•Éµ¥¹”Ý¡¥ ½¹™¥ÕÉ…Ñ¥½¸µ½‘”ÁÉ½‘Õ•Ñ¡”¥¹ÍÑ…±±•Ù…±Õ”¸((Ä¸½¹™¥É´Ñ¡É½Õ M}%I5]I}=9%}5=€…¹9}=9%}5=€Ñ¡…ÐÑ¡”™¥ÉµÝ…É”ÍÕÁÁ½ÉÑÌÑ¡”‘¥ÍÑ¥¹ÐA¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸µ½‘”¸(È¸¹Õµ•É…Ñ”‘•µ½¹ÍÑÉ…Ñ•Á¡åÍ¥…°™¥ÉµÝ…É”µÍ½Á•9}=9€‘•™¥¹¥Ñ¥½¹Ìì‘¼¹½ÐÑÉ•…Ð¥‘à€ô€´Å€…±½¹”…ÌÁÉ½½˜‰•…ÕÍ”Ñ¡”½µµ½¸%€½%™¥•±Í¡…É•ÌÑ¡…ÐÍÑÉÕÑÕÉ”¸(Ì¸I•Í½±Ù”•… Á¡åÍ¥…°Íåµ‰½°Ì±•…°‘½µ…¥¸Ñ¡É½Õ ¥ÑÌ•á…Ð9}=9}I9€¸(Ð¸½È…¸…‘‘É•ÍÌ°½µÁ…É”‘•½‘•%59M%=8€ÌÉ€½µÁ½¹•¹ÑÌÝ¥Ñ …ÁÁ±¥…‰±”Á¡åÍ¥…°Íåµ‰½±ÌÍÕ …Ì€…¹A1€¸(Ô¸½È…¸¥¹‘•á•ÁÉ½Á•ÉÑä°½µÁ…É”¥ÑÌÉ•Í½±Ù•=‰©•Ð‘•™¥¹¥Ñ¥½¸Ý¥Ñ …ÁÁ±¥…‰±”™¥ÉµÝ…É”Á¡åÍ¥…°Íåµ‰½±ÌÍÕ …Ì5€°QeA€°AI€°½ÈÅ€¸(Ø¸½µÁ…É”Íåµ‰½°°Í•µ…¹Ñ¥ŒÑåÁ”°‘½µ…¥¸°™¥±Ñ•ÉÌ°=9}Me5	=1}I€°½¹Ù•ÉÍ¥½¸ÉÕ±•Ì°ÍÁ…ÉÍ”9}A!e}Q=}Y}QI9M€•Ù¥‘•¹”°ÁÉ½‘ÕÐ‘½Õµ•¹Ñ…Ñ¥½¸°…¹…ÁÑÕÉ•ÌÝ¡•É”…ÁÁ±¥…‰±”¸(Ü¸ÍÑ…‰±¥Í Ñ¡”Á¡åÍ¥…°‘½µ…¥¸¥¹‘•Á•¹‘•¹Ñ±ä™É½´Ñ¡”ÁÉ½É…µµ¥¹œÑÉ…¹ÍÁ½ÉÐ‘½µ…¥¸¸()±…ÍÍ¥™äÑ¡”É•ÍÕ±Ð…Ìè()ð±…ÍÍ¥™¥…Ñ¥½¸ð5•…¹¥¹œð)ð€´´´ð€´´´ð)ð‘¥É•Ð½Õ¹Ñ•ÉÁ…ÉÐðÍåµ‰½°…¹Í•µ…¹Ñ¥Ìµ…Ñ ¥¸Ñ¡”É•Í½±Ù•½¹Ñ•áÐð)ðµ…ÁÁ•½Õ¹Ñ•ÉÁ…ÉÐð‘¥™™•É•¹ÐÍåµ‰½±Ì°‰ÕÐ„½¹Ù•ÉÍ¥½¸½È¥¹‘•Á•¹‘•¹Ñ±ä½ÉÉ½‰½É…Ñ•Í•µ…¹Ñ¥Œµ…ÁÁ¥¹œ•á¥ÍÑÌð)ðÁ¡åÍ¥…±±äÉ•ÁÉ•Í•¹Ñ…‰±”ð¥¹Ñ•¹‘••™™•Ñ¥Ù”Ù…±Õ”±¥•Ì¥¸Ñ¡”•ÍÑ…‰±¥Í¡•Á¡åÍ¥…°‘½µ…¥¸ð)ð½ÕÑÍ¥‘”•ÍÑ…‰±¥Í¡•Á¡åÍ¥…°‘½µ…¥¸ð„½Õ¹Ñ•ÉÁ…ÉÐ¥Ì•ÍÑ…‰±¥Í¡•°‰ÕÐÑ¡¥ÌÙ…±Õ”¥Ì¹½Ð¥¸¥ÑÌ±•…°Á¡åÍ¥…°‘½µ…¥¸ð)ð¹¼Á¡åÍ¥…°½Õ¹Ñ•ÉÁ…ÉÐ•ÍÑ…‰±¥Í¡•ð¥¹ÍÁ•Ñ••Ù¥‘•¹”‘½•Ì¹½Ð•ÍÑ…‰±¥Í „½Õ¹Ñ•ÉÁ…ÉÐìÑ¡¥Ì¥Ì¹½ÐÁÉ½½˜Ñ¡…Ð¹½¹”•á¥ÍÑÌð)ðÕ¹É•Í½±Ù•ðÉ•ÅÕ¥É•Á¡åÍ¥…°µ¥¹Ñ•É™…”½Èµ…ÁÁ¥¹œ•Ù¥‘•¹”¥Ì¥¹ÍÕ™™¥¥•¹Ðð()Q¡”…¹½¹¥…°…Ñ…±½Õ”É•¥ÍÑ•ÉÌY¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸…¹‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸…Ì‘¥ÍÑ¥¹Ðµ½‘•Ì¸=A8¹‘‰€Í•Á…É…Ñ•±ä±…‰•±Ì½¹™½¹™¥ÕÉ…Ñ½ÉÍ€…ÌÙ¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸…¹½¹™-=€…Ì…‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸¸¼¹½ÐÉ•Á±…”Ñ¡•Í”Í½ÕÉ”±…‰•±ÌÝ¥Ñ „Í¥¹±”Õµ‰É•±±„…Ñ•½Éä½È¥¹™•ÈÑ¡”…Ñ¥Ù”µ½‘”™É½´•™™•Ñ¥Ù”Ù…±Õ•Ì…±½¹”¸()%˜Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÙ…±Õ•Ì…É”Ñ¡•µÍ•±Ù•Ì‰•¥¹œÉ•Í½±Ù•¥¹Ñ¼„Ñ½Á½±½ä°ÕÍ”Ñ¡”‘•Ñ•Éµ¥¹¥ÍÑ¥ŒÉ•…¡…‰¥±¥Ñä…¹=‰©•ÐµÍ•±•Ñ¥½¸µ•Ñ¡½¥¸m…Ñ…±½Õ”I•Í½±ÕÑ¥½¹t ¸¸½¥¹Ñ•É¹…±Ì½…Ñ…±½Õ”µÉ•Í½±ÕÑ¥½¸¹µÁ¡åÍ¥…°µ½¹™¥ÕÉ…Ñ¥½¸µÉ•Í½±ÕÑ¥½¸¤‰•™½É”ÁÉ½Á•ÉÑäµ±•Ù•°Ù…±¥‘…Ñ¥½¸¸((ŒŒŒ€ÄÌ¸¹½‘”ÁÉ½É…µµ¥¹œÑÕÁ±•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()=¹±ä…™Ñ•ÈÍ•µ…¹Ñ¥ŒÙ…±¥‘…Ñ¥½¸Í¡½Õ±Ù…±Õ•Ì‰”½¹Ù•ÉÑ•¥¹Ñ¼™É…µ•Ì¸()ð%¹Ñ•¹‘•¡…¹”ðY…±¥‘…Ñ•½ÕÑÁÕÐð)ð€´´´ð€´´´ð)ð=‰©•ÐÍ•±•Ñ¥½¸ð€¡M1=P°9}-e}=	)P¹­•å}½‰©•Ð¥€™½È%59M%=8€ÌÁ€ð)ð5½‘Õ±”…‘‘É•ÍÌð€¡M1=P°MeL°H¥€™½È%59M%=8€ÌÉ€ð)ð¥¹‘•á•ÁÉ½Á•ÉÑäð€¡%9`°M1=P°Y1}AH¥€™½È%59M%=8€ÌÕ€ð)ð½¹™½¹™¥ÕÉ…Ñ½ÉÍ€™¥•±‘ÌðÑÝ•±Ù”É…ÜÙ…±Õ•Ì™½È%59M%=8€Ñ€…¹€Õ€°ÍÕ‰©•ÐÑ¼•Ù¥”ÍÕÁÁ½ÉÐ…¹Õ¹É•Í½±Ù•…Ñ…±½Õ”µÁ½Í¥Ñ¥½¸½ÉÉ•±…Ñ¥½¸ð()½È•… •¹½‘•Ù…±Õ”É•Ñ…¥¸è((´Í•µ…¹Ñ¥Œ¥¹Ñ•¹‘•Ù…±Õ”ì(´É…ÜÕÍ•È¥¹ÁÕÐì(´É•Í½±Ù••Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°…¹=‰©•Ðì(´¥‘}½¹™€°Í½Á”°…¹¥‘á€°Ý¡•É”…ÁÁ±¥…‰±”ì(´‰…Í”…¹™¥±Ñ•É•‘½µ…¥¹Ìì(´½¹‘¥Ñ¥½¸…¹½¹Ù•ÉÍ¥½¸Á…Ñ ì(´Á¡åÍ¥…°µÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸±…ÍÍ¥™¥…Ñ¥½¸ì(´™¥¹…°Ý¥É”Ù…±Õ”¸()A•É™½É´…¸•¹½‘”½‘•½‘”É½Õ¹ÑÉ¥ÀÝ¡•É•Ù•È„‘•½‘•È•á¥ÍÑÌ¸Q¡”É•ÍÕ±ÐµÕÍÐÉ•ÁÉ½‘Õ”Ñ¡”¥¹Ñ•¹‘•Í•µ…¹Ñ¥ŒÙ…±Õ”¥¸Ñ¡”Í…µ”½¹Ñ•áÐ¸((ŒŒŒ€ÄÐ¸Y…±¥‘…Ñ”Ñ¡”½µÁ±•Ñ”ÑÉ…¹Í™•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐá€((ŒŒŒŒ½…°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÐå€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()AÉ½Ù”Ñ¡…ÐÑ¡”•¹Ñ¥É”Á…å±½…¥Ì½¡•É•¹Ð‰•™½É”Ñ¡”…¹½¹¥…°…‘Ù…¹•Í•ÅÕ•¹”É•Í•ÑÌ…±°=‰©•ÑÌ¸()Y…±¥‘…Ñ”Ñ¡”½µÁ±•Ñ”‘•Í¥É••Ù¥”ÍÑ…Ñ”°¹½Ðµ•É•±ä¡…¹•™¥•±‘Ìè((Ä¸%¹±Õ‘”•Ù•Éä5½‘Õ±”½=‰©•Ð…ÍÍ¥¹µ•¹ÐÑ¡…ÐµÕÍÐÉ•µ…¥¸…™Ñ•ÈÉ•Í•Ðµ…±°¸(È¸I•ÅÕ¥É”Õ¹¥ÅÕ”•Ù¥”µ±½…°Í±½Ñ€Á½Í¥Ñ¥½¹Ì¸(Ì¸I•ÅÕ¥É”•Ù•Éä…‘‘É•ÍÌ…¹Á…É…µ•Ñ•ÈÑ¼É•™•É•¹”…¸=‰©•Ð¥¹±Õ‘•¥¸Ñ¡”Í…µ”…¹‘¥‘…Ñ”±…å½ÕÐ¸(Ð¸=É‘•È•… 5½‘Õ±—ŠeÌ=‰©•Ð…ÍÍ¥¹µ•¹Ð‰•™½É”¥ÑÌ…‘‘É•ÍÌ…¹Á…É…µ•Ñ•ÈÝÉ¥Ñ•Ì¸(Ô¸AÉ•Í•ÉÙ”™¥á•…¹Õ¹Ñ½Õ¡•5½‘Õ±•Ì¥¸Ñ¡”É•Á±…•µ•¹ÐÁ±…¸¸(Ø¸I”µ•Ù…±Õ…Ñ”½¹‘¥Ñ¥½¹Ì…¹±¥¹­•ÉÕ±•Ì…™Ñ•È½µ‰¥¹¥¹œ…±°…¹‘¥‘…Ñ”Ù…±Õ•Ì¸(Ü¸½¹™¥É´Ñ¡…Ð•Ù•ÉäÉ•ÅÕ¥É•Ù…±Õ”¥ÌÁÉ•Í•¹Ð…¹•Ù•Éä½µ¥ÑÑ•Ù…±Õ”¥Ì½ÁÑ¥½¹…°°™¥á•°É•…µ½¹±ä°Õ¹ÍÕÁÁ½ÉÑ•°½È‘•±¥‰•É…Ñ•±äÁÉ•Í•ÉÙ•¸(à¸½¹™¥É´…±°•¹½‘•™¥•±‘Ì™¥ÐÑ¡•¥È=A8¹‘‰€ÑÉ…¹ÍÁ½ÉÐÉ…¹•Ì¸(ä¸AÉ•Á…É”Ñ¡”•áÁ•Ñ•‘¥…¹½ÍÑ¥ŒÉ•…µ‰…¬™½È%59M%=8€ÌÁ€°€ÌÉ€°…¹€ÌÕ€¸(ÄÀ¸AÉ•Í•ÉÙ”„É•½Ù•Éä½Áä½˜Ñ¡”ÁÉ¥½È•™™•Ñ¥Ù”ÍÑ…Ñ”¸()	•…ÕÍ”½¹™-=€‰•¥¹ÌÝ¥Ñ É•Í•Ðµ…±°°Á…ÉÑ¥…°Ù…±¥‘…Ñ¥½¸¥ÌÕ¹Í…™”¸¼¹½ÐÑÉ…¹Íµ¥ÐÑ¡”É•Í•Ð™É…µ”Õ¹Ñ¥°Ñ¡¥Ìµ¥±•ÍÑ½¹”ÍÕ••‘Ì¸((ŒŒŒY…±¥‘…Ñ¥½¸É•ÍÕ±Ðµ½‘•°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÔÁ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)U¹•ÉÑ…¥¹Ñäèµ…å€°Õ¹­¹½Ý¹€°Õ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()Y…±¥‘…Ñ¥½¸Í¡½Õ±É•ÑÕÉ¸•Ù¥‘•¹”°¹½Ð½¹±ä„	½½±•…¸¸()ðI•ÍÕ±Ðð5•…¹¥¹œð)ð€´´´ð€´´´ð)ðÙ…±¥ð…±±½Ý•‰äÑ¡”¥¹ÍÁ•Ñ•½¹ÍÑÉ…¥¹ÑÌ¥¸Ñ¡”É•Í½±Ù•½¹Ñ•áÐìÉÕ¹Ñ¥µ”…•ÁÑ…¹”¹½Ðå•ÐÙ•É¥™¥•ð)ðÙ…±¥…™Ñ•È½¹Ù•ÉÍ¥½¸ð…±±½Ý•…™Ñ•È„‘½Õµ•¹Ñ•½¹Ù•ÉÍ¥½¸Á…Ñ ð)ð½¹‘¥Ñ¥½¹…±±äÙ…±¥ðÙ…±¥½¹±äÝ¡¥±”ÍÑ…Ñ•‘•Á•¹‘•¹¥•Ì¡½±ð)ðÁ¡åÍ¥…±±äÉ•ÁÉ•Í•¹Ñ…‰±”ð„Á¡åÍ¥…°½Õ¹Ñ•ÉÁ…ÉÐ…¹½µÁ…Ñ¥‰±”Á¡åÍ¥…°Ù…±Õ”•á¥ÍÐð)ð½ÕÑÍ¥‘”•ÍÑ…‰±¥Í¡•Á¡åÍ¥…°‘½µ…¥¸ðÙ…±¥¥¸Ñ¡”É•Í½±Ù•ÁÉ½É…µµ¥¹œ½¹Ñ•áÐ‰ÕÐ½ÕÑÍ¥‘”„‘•µ½¹ÍÑÉ…Ñ•Á¡åÍ¥…°½Õ¹Ñ•ÉÁ…ÉÐÌ‘½µ…¥¸ð)ð™¥á•½É•…µ½¹±äðÁ…ÉÐ½˜•™™•Ñ¥Ù”ÍÑ…Ñ”‰ÕÐ¹½Ð…¸…É‰¥ÑÉ…ÉäÝÉ¥Ñ”ð)ð¥¹Ù…±¥ð•á±Õ‘•‰ä…¸…ÁÁ±¥…‰±”…Á…‰¥±¥Ñä°‘½µ…¥¸°™¥±Ñ•È°½¹‘¥Ñ¥½¸°½ÈÉÕ±”ð)ð…µ‰¥Õ½ÕÌðµ½É”Ñ¡…¸½¹”¥¹½µÁ…Ñ¥‰±”É•Í½±ÕÑ¥½¸É•µ…¥¹Ìð)ðÕ¹É•Í½±Ù•ðÉ•ÅÕ¥É•½¹Ñ•áÐ½Èµ…ÁÁ¥¹œ¥Ì…‰Í•¹Ðð()ÕÍ•™Õ°Ù…±¥‘…Ñ¥½¸É•½É½¹Ñ…¥¹Ìè()Ñ•áÐ)ÍÑ…ÑÕÌ)É•…Í½¸)Í½ÕÉ”•Ù¥‘•¹”)É•Í½±Ù•¥‘•¹Ñ¥™¥•ÉÌ)…¹‘¥‘…Ñ”Í•µ…¹Ñ¥ŒÙ…±Õ”)•¹½‘•Ù…±Õ”)…ÁÁ±¥…‰±”‘½µ…¥¸)‘•Á•¹‘•¹¥•Ì)Ý…É¹¥¹Ì)•áÁ•Ñ•É•…µ‰…¬)€()…¥°±½Í•™½ÈÁÉ½É…µµ¥¹œÝ¡•¸Ñ¡”ÍÑ…ÑÕÌ¥Ì…µ‰¥Õ½ÕÌ½ÈÕ¹É•Í½±Ù•¸¥…¹½ÍÑ¥Ìµ…äÁÉ•Í•ÉÙ”Õ¹­¹½Ý¸Ù…±Õ•ÌìÁÉ½É…µµ¥¹œµÕÍÐ¹½ÐÑÉ…¹Íµ¥Ð…¸¥¹Ù•¹Ñ•¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¸((ŒŒŒI•Ù…±¥‘…Ñ¥½¸ÑÉ¥•ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÔÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€()I•ÍÑ…ÉÐÙ…±¥‘…Ñ¥½¸™É½´Ñ¡”•…É±¥•ÍÐ…™™•Ñ•µ¥±•ÍÑ½¹”Ý¡•¸…¹ä½˜Ñ¡•Í”¡…¹”è()ð¡…¹”ðI•ÍÑ…ÉÐ…Ðð)ð€´´´ð€´´´ð)ð•Ù¥”¥‘•¹Ñ¥Ñä½È™¥ÉµÝ…É”ð€Äð)ðÍ±½Ñ€½È5½‘Õ±”±…å½ÕÐð€Èð)ðÕÉÉ•¹ÐY¥É¥¸=‰©•Ð½ÈÑ…É•Ð=‰©•Ðð€Ìð)ð=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸ð€Ðð)ðÁÉ½Á•ÉÑä½È%9a€ð€Ôð)ð½¹ÑÉ½±±¥¹œÁÉ½Á•ÉÑäÙ…±Õ”ð€Ü½È€äð)ð™Õ¹Ñ¥½¹…°ÍåÍÑ•´½…‘‘É•ÍÌÑåÁ”ð€ÄÄð)ð½¹™¥ÕÉ…Ñ¥½¸µ•Ñ¡½ÅÕ•ÍÑ¥½¸ð€ÄÈð)ð…¹äµ•µ‰•È½˜Ñ¡”É•Á±…•µ•¹ÐÁ…å±½…ð€ÄÐð()¼¹½ÐÉ•ÕÍ”„ÁÉ•Ù¥½ÕÍ±äÙ…±¥‘…Ñ•É…¹”…™Ñ•È¡…¹¥¹œ=‰©•Ð°™¥ÉµÝ…É”°Í±½Ð°½È„½¹ÑÉ½±±¥¹œÁÉ½Á•ÉÑä¸((ŒŒŒM½ÕÉ”‰½Õ¹‘…É¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÀääéÌÀÀÀÀÔÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€°Í½ÕÉ•€()ðM½ÕÉ”ðY…±¥‘…Ñ¥½¸…ÕÑ¡½É¥Ñäð)ð€´´´ð€´´´ð)ð5!…Ñ…±½Õ”¹‘‰€ð•Ù¥”½™¥ÉµÝ…É”…Á…‰¥±¥Ñä°=‰©•ÑÌ°Í±½ÑÌ°ÁÉ½Á•ÉÑ¥•Ì°‘½µ…¥¹Ì°™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¹Ì°…¹½¹Ù•ÉÍ¥½¹Ìð)ðÉÕ±•Ì¹‘ˆÍ€ð…‘‘¥Ñ¥½¹…°‘•Á•¹‘•¹¥•Ì™½ÈÍ•±•Ñ•Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°=‰©•ÑÌð)ð=A8¹‘‰€ðÁÉ½É…µµ¥¹œ™É…µ•Ì°ÑÉ…¹ÍÁ½ÉÐÉ…¹•Ì°…‘‘É•ÍÌÉÕ±•Ì°Í•ÅÕ•¹”‰•¡…Ù¥½È°…¹•ÉÉ½ÉÌð)ð=Á•¹EÕ•Éä¹ÑáÑ€ð¥µÁ±•µ•¹Ñ…Ñ¥½¸ÅÕ•É¥•ÌÕÍ•Ñ¼…ÍÍ•µ‰±”ÁÉ½Ñ½½°Í•¹…É¥½Ìð)ðÁÕ‰±¥Œ=Á•¹]•‰9•Ð‘½Õµ•¹ÑÌðÍ¡…É•™Õ¹Ñ¥½¹…°µ•…¹¥¹œ…¹ÁÕ‰±¥Œ™É…µ”½…‘‘É•ÍÌÍå¹Ñ…àð)ðÁÉ½‘ÕÐ‘½Õµ•¹Ñ…Ñ¥½¸ðÁ¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹Ì…¹ÁÉ½‘ÕÐµÍÁ•¥™¥Œ‰•¡…Ù¥½Èð)ð½‰Í•ÉÙ•ÑÉ…™™¥ŒðÉÕ¹Ñ¥µ”ÍÕÁÁ½ÉÐ°½É‘•É¥¹œ°½ÁÑ¥½¹…°É•ÍÁ½¹Í•Ì°…¹•™™•Ñ¥Ù”Ù…±Õ•Ìð)ð5å!=5}MÕ¥Ñ”U$ð±…‰•±Ì°Í•±•Ñ…‰±”Ù…±Õ•Ì°Ù¥Í¥‰¥±¥Ñä°…¹Ý½É­™±½Ü‰•¡…Ù¥½Èð()¼¹½Ð±•Ð„±½Ý•Èµ±•Ù•°ÑÉ…¹ÍÁ½ÉÐÉ…¹”½Ù•ÉÉ¥‘”„¹…ÉÉ½Ý•È…Ñ…±½Õ”ÉÕ±”¸]¡•¸Í½ÕÉ•Ì‘¥Í…É•”°É•Ñ…¥¸Ñ¡”‘¥ÍÉ•Á…¹ä…¹Ñ¡”É…Ü•Ù¥‘•¹”É…Ñ¡•ÈÑ¡…¸Í¥±•¹Ñ±ä¡½½Í¥¹œÑ¡”±•…ÍÐÉ•ÍÑÉ¥Ñ¥Ù”¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀÀ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½Ù•É¥™¥…Ñ¥½¸¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒAÉ½É…µµ¥¹œY•É¥™¥…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÀéÌÀÀÀÀÀÅ€()Y•É¥™¥…Ñ¥½¸½µÁ…É•ÌÑ¡”¥¹Ñ•¹‘•½¹™¥ÕÉ…Ñ¥½¸Ý¥Ñ „¹•ÜÉÕ¹Ñ¥µ”ÁÉ½©•Ñ¥½¸…™Ñ•ÈÑ¡”ÁÉ½É…µµ¥¹œÍ•ÍÍ¥½¸¡…Ì•¹‘•¸((ŒŒŒ]¡äÉ•…µ‰…¬¥ÌÉ•ÅÕ¥É•()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÀéÌÀÀÀÀÀÉ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()]!P€ÔÉ€•ÍÑ…‰±¥Í¡•ÌÍÕ•ÍÍ™Õ°½µÁ±•Ñ¥½¸½˜Ñ¡”…‘Ù…¹•ÑÉ…¹Í™•È…ÌÉ•ÁÉ•Í•¹Ñ•‰ä=A8¹‘‰€¸%Ð‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…Ð•Ù•Éä½ÁÑ¥½¹…°Á…É…µ•Ñ•ÈÝ…Ìµ…¹…•°‰•…ÕÍ”%59M%=8€Ìå€Ý…É¹¥¹Ì…¸½•á¥ÍÐÝ¥Ñ ½¹Ñ¥¹Õ•½¹™¥ÕÉ…Ñ¥½¸¸()Y¥ÉÑÕ…°µ½¹™¥ÕÉ…Ñ½ÈÑÉ…¹Í™•È¡…Ì¹¼]!P€ÔÉ€µ•µ‰•È¥¸¥ÑÌ…¹½¹¥…°Í•ÅÕ•¹”¸%ÑÌ•Ù¥”•¹µ…É­•È…¹•¡½•Ù…±Õ•Ì±¥­•Ý¥Í”‘¼¹½ÐÉ•Á±…”„±…Ñ•È¥¹ÍÑ…±±•µÍÑ…Ñ”¡•¬¸((ŒŒŒY•É¥™¥…Ñ¥½¸ÁÉ½•‘ÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÀéÌÀÀÀÀÀÍ€()…ÕÑ¥½¹ÌèÝ…É¹¥¹€((Ä¸I•½ÉÝ¡•Ñ¡•ÈÑÉ…¹Í™•È•¹‘•Ý¥Ñ ÍÕ•ÍÌ°Ý…É¹¥¹œ°•ÉÉ½È°…‰½ÉÐ°½ÈÑ¥µ•½ÕÐ¸(È¸M•¹Ñ¡”½ÕÑ•ÈÍ•ÍÍ¥½¸±½Í”€©m]!=t¨È¨ÀŒ€Ý¡•¸Ñ¡”…¹½¹¥…°Ý½É­™±½ÜÉ•…¡•Ì±½Í”¸(Ì¸]…¥Ð™½ÈÑ¡”½¹™¥ÕÉ•±½Í”¥¹Ñ•ÉÙ…°¸(Ð¸MÑ…ÉÐ„¹•Ü‘¥…¹½ÍÑ¥Œ¥¹Ñ•ÉÙ¥•Ü‰ä•Ù¥”%Ý¡•¸…Ù…¥±…‰±”¸(Ô¸I•½¹™¥É´%59M%=8€Å€¥‘•¹Ñ¥Ñä…¹%59M%=8€ÄÍ€•Ù¥”%¸(Ø¸I•Í½±Ù”•Ù•Éä%59M%=8€ÌÁ€É•½É…Ì…¸•¹…‰±•É•Õ±…È=‰©•ÐÝ¡•¸MQQ€ô€Á€½È„‘¥Í…‰±•5½‘Õ±”ÌY¥É¥¸=‰©•ÐÝ¡•¸MQQ€ô€Å€¸(Ü¸½µÁ…É”%59M%=8€ÌÉ€•™™•Ñ¥Ù”ÍåÍÑ•´½…‘‘É•ÍÌÑÕÁ±•Ì¸(à¸½µÁ…É”%59M%=8€ÌÕ€¥¹‘•á•Ù…±Õ•ÌÕÍ¥¹œÑ¡”É•Í½±Ù•‘•™¥¹¥Ñ¥½¹Ì¸(ä¸AÉ•Í•ÉÙ”%59M%=8€ÌÄÁ€Í•Á…É…Ñ•±ä¸(ÄÀ¸½µÁ…É”%59M%=8€Ñ€…¹€Õ€½¹±ä…ÌÉ…Ü½¹™¥ÕÉ…Ñ½ÈÉ•Á½ÉÑÌÕ¹Ñ¥°Ñ¡•¥ÈÁÉ•¥Í”Í•µ…¹Ñ¥Ì…É”•ÍÑ…‰±¥Í¡•¸(ÄÄ¸±…ÍÍ¥™ä•… ¥¹Ñ•¹‘•¡…¹”¥¹‘•Á•¹‘•¹Ñ±ä¸((ŒŒŒI•ÍÕ±Ð±…ÍÍ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÀéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€()ðI•ÍÕ±Ðð5•…¹¥¹œð)ð€´´´ð€´´´ð)ðY•É¥™¥•ðÉ•…µ‰…¬µ…Ñ¡•ÌÑ¡”¥¹Ñ•¹‘••™™•Ñ¥Ù”ÍÑ…Ñ”ð)ðY•É¥™¥•Ý¥Ñ Ý…É¹¥¹Ìð¥¹Ñ•¹‘•ÍÑ…Ñ”µ…Ñ¡•Ì‰ÕÐÁÉ½É…µµ¥¹œÉ•Á½ÉÑ•¹½¹™…Ñ…°½µ¥ÍÍ¥½¹Ìð)ð½¹ÑÉ…‘¥Ñ•ðÉ•…µ‰…¬É•Á½ÉÑÌ„‘¥™™•É•¹Ð•™™•Ñ¥Ù”Ù…±Õ”½È=‰©•Ðð)ðU¹Ù•É¥™¥…‰±”ðÑ¡”•Ù¥”‘½•Ì¹½ÐÉ•Á½ÉÐÑ¡”É•±•Ù…¹Ð½ÁÑ¥½¹…°‘…Ñ„ð)ð%¹‘•Ñ•Éµ¥¹…Ñ”ð¥‘•¹Ñ¥Ñä°Ñ¥µ•½ÕÐ°½ÈÑÉ…¹ÍÁ½ÉÐÍÑ…Ñ”ÁÉ•Ù•¹ÑÌÉ•±¥…‰±”½µÁ…É¥Í½¸ð()¼¹½Ð½µÁ…É”½¹±ä‘¥ÍÁ±…äÍÑÉ¥¹Ì¸I•Ñ…¥¸É…Ü™É…µ•Ì°‘•½‘•Ù…±Õ•Ì°=‰©•Ð½™¥ÉµÝ…É”½¹Ñ•áÐ°…¹½¹Ù•ÉÍ¥½¸ÉÕ±•Ì¸((ŒŒŒ=‰©•ÐÉ•Á±…•µ•¹Ð¡•­Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÀéÌÀÀÀÀÀÕ€()™Ñ•È½¹™-=€°Ù•É¥™äÑ¡”•¹Ñ¥É”5½‘Õ±”±…å½ÕÐÉ…Ñ¡•ÈÑ¡…¸½¹±äÑ¡”•‘¥Ñ•Í±½Ð‰•…ÕÍ”Ñ¡”Í•ÅÕ•¹”É•Í•ÑÌ…±°=‰©•ÑÌ‰•™½É”É•‰Õ¥±‘¥¹œÑ¡•´¸½¹™¥É´Ñ¡…Ð™¥á•…¹Õ¹Ñ½Õ¡•5½‘Õ±•ÌÉ•µ…¥¸ÁÉ•Í•¹ÐÝ¥Ñ Ñ¡•¥È¥¹Ñ•¹‘•=‰©•ÑÌ…¹…‘‘É•ÍÍ•Ì¸((ŒŒŒA¡åÍ¥…°…¹…‘Ù…¹•Ù…±Õ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÀéÌÀÀÀÀÀÙ€()¥…¹½ÍÑ¥ŒÉ•…µ‰…¬É•Á½ÉÑÌ•™™•Ñ¥Ù”½¹™¥ÕÉ…Ñ¥½¸°¹½Ð¹••ÍÍ…É¥±äÑ¡”µ•Ñ¡½ÕÍ•Ñ¼É•…Ñ”¥Ð¸Ù…±Õ”½µÁ…Ñ¥‰±”Ý¥Ñ „Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½È…¹¹½ÐÁÉ½Ù”Ñ¡…Ð©ÕµÁ•ÉÌÝ•É”ÕÍ•¸Ù…±Õ”½ÕÑÍ¥‘”Ñ¡”•ÍÑ…‰±¥Í¡•Á¡åÍ¥…°É…¹”…¸•á±Õ‘”Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸™½ÈÑ¡…ÐÁÉ½Á•ÉÑä¸()M•”m•Ù¥”%¹Ñ•ÉÙ¥•Ýt ¸¸½‘¥…¹½ÍÑ¥Ì½‘•Ù¥”µ¥¹Ñ•ÉÙ¥•Ü¹µ¤°m%59M%=8€ÌÁt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´ÌÀµµ½‘Õ±•Ì¹µ¤°m%59M%=8€ÌÉt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´ÌÈµ…‘‘É•ÍÍ¥¹œ¹µ¤°…¹m%59M%=8€ÌÕt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´ÌÔµ½¹™¥ÕÉ…Ñ¥½¸¹µ¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀÄ()M½ÕÉ”Á…Ñ èÁÉ½É…µµ¥¹œ½Ý¡…ÐµÉ•™•É•¹”¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÁÉ½É…µµ¥¹€((ŒŒAÉ½É…µµ¥¹œ]!Q€I•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÄéÌÀÀÀÀÀÅ€()AÉ½É…µµ¥¹œ]!Q€Ù…±Õ•Ì½¹ÑÉ½°Í•ÍÍ¥½¸•¹ÑÉä°É•Í•Ð°ÑÉ…¹Í™•È½µÁ±•Ñ¥½¸°…•ÁÑ…¹”°…‰½ÉÐ°…¹±½Í”¸Q¡•¥Èµ•…¹¥¹œ¥ÌÍ½Á•Ñ¼Ñ¡”…Ñ¥Ù”µ…¹…•µ•¹Ð]!=€…¹ÁÉ½É…µµ¥¹œÍ•ÅÕ•¹”¸((ŒŒŒ…¹½¹¥…°Ù…±Õ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÄéÌÀÀÀÀÀÉ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()ð]!Q€ð¥É•Ñ¥½¸ðÉ…µ”ð5•…¹¥¹œð…¹½¹¥…°ÕÍ”ð)ð€´´´ð€´´´ð€´´´ð€´´´ð€´´´ð)ð€Å€ðÁÉ½É…µµ•ÈƒŠH•Ù¥”ð€©m]!=t¨Ä©m]!ItŒ€ðÍÑ…ÉÐÁÉ½É…µµ¥¹œ‰ä…‘‘É•ÍÌð…‘‘É•ÍÌ…¹±½…°µ¥¹Ñ•É…Ñ¥½¸•¹ÑÉäð)ð€É€ðÁÉ½É…µµ•ÈƒŠH•Ù¥”ð€©m]!=t¨È¨ÀŒ€ð•¹ÁÉ½É…µµ¥¹œÍ•ÍÍ¥½¸ð±½Í•½¹™€ð)ð€Í€ð•¥Ñ¡•È‘¥É•Ñ¥½¸ð€©m]!=t¨Ì¨ÀŒ€ð…‰½ÉÐÁÉ½É…µµ¥¹œð…‰½ÉÐ½•ÉÉ½ÈÁ…Ñ ð)ð€Ñ€ð•Ù¥”ƒŠHÁÉ½É…µµ•Èð€©m]!=t¨Ð©m]!I}-tŒ€ð•¹•Ù¥”ÑÉ…¹Íµ¥ÍÍ¥½¸ð•¹ÑÉä…¹Ù¥ÉÑÕ…°ÑÉ…¹Í™•Èð)ð€Ñ€ðÁÉ½É…µµ•ÈƒŠH•Ù¥”ð€©m]!=t¨Ð¨ÀŒ€ð•¹ÁÉ½É…µµ•ÈÑÉ…¹Í™•Èðµ…¹‘…Ñ½Éä•¹½˜½¹™-=€Á…å±½…ð)ð€å€ðÁÉ½É…µµ•ÈƒŠH•Ù¥”ð€©m]!=t¨äm%t¨ÀŒ€ðÍÑ…ÉÐÁÉ½É…µµ¥¹œ‰ä•Ù¥”%ð%µÍ•±•Ñ••¹ÑÉäð)ð€ÄÑ€ðÁÉ½É…µµ•ÈƒŠH•Ù¥”ð€©m]!=t¨ÄÐŒÀ¨ÀŒ€ðÉ•Í•Ð…±°=‰©•ÑÌðµ…¹‘…Ñ½ÉäÍÑ…ÉÐ½˜½¹™-=€ð)ð€ÄÑ€ðÁÉ½É…µµ•ÈƒŠH•Ù¥”ð€©m]!=t¨ÄÐmM1=Qt¨ÀŒ€ðÉ•Í•Ð½¹”=‰©•ÐÍ±½ÐðÉ•¥ÍÑ•É•°¹½Ð¥¸…¹½¹¥…°½¹™-=€ð)ð€ÔÅ€ð•Ù¥”ƒŠHÁÉ½É…µµ•Èð€©m]!=t¨ÔÄ©m]!I}-tŒ€ðÝÉ½¹œ½¹™¥ÕÉ…Ñ¥½¸ð™…Ñ…°ÑÉ…¹Í™•ÈÉ•ÍÕ±Ðð)ð€ÔÉ€ð•Ù¥”ƒŠHÁÉ½É…µµ•Èð€©m]!=t¨ÔÈ©m]!I}-tŒ€ð½¹™¥ÕÉ…Ñ¥½¸…•ÁÑ•ð…‘Ù…¹•µÑÉ…¹Í™•ÈÉ•ÍÕ±Ðð()=A8¹‘‰€…±Í¼É•¥ÍÑ•ÉÌ€©m]!=t¨Ä¨ÀŒ€…Ì„•¹•É…°ÁÉ½É…µµ¥¹œÍÑ…ÉÐ°€©m]!=t¨Ü¨ÀŒ€…Ì‘•±•Ñ¥¹œÍÑ½É•½¹™¥ÕÉ…Ñ¥½¸°…¹]!I€ô€Á€Ù…É¥…¹ÑÌ½˜]!P€ÔÅ€…¹€ÔÉ€¸Q¡•ä…É”¹½Ðµ•µ‰•ÉÌ½˜Ñ¡”Ñ¡É•”…¹½¹¥…°ÁÉ½É…µµ¥¹œÍ•¹…É¥½Ì…¹µÕÍÐ¹½Ð‰”¥¹Í•ÉÑ•¥¹Ñ¼Ñ¡½Í”™±½ÝÌÝ¥Ñ¡½ÕÐ¥¹‘•Á•¹‘•¹Ð•Ù¥‘•¹”¸((ŒŒŒ]!P€Å€èÍÑ…ÉÐ‰ä…‘‘É•ÍÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÄéÌÀÀÀÀÀÍ€()Q¡”…‘‘É•ÍÍ•…¹±½…°µ¥¹Ñ•É…Ñ¥½¸•¹ÑÉäÍ•ÅÕ•¹•ÌÕÍ”Ñ¡”Í…µ”™É…µ”¸Q¡•¥ÈÑ¥µ•ÈÁ½±¥ä‘¥ÍÑ¥¹Õ¥Í¡•ÌÑ¡”…¹½¹¥…°Í•¹…É¥½Ìè€ÄÔÍ•½¹‘Ì™½È…‘‘É•ÍÍ•Í•±•Ñ¥½¸…¹€ÌÀÀÍ•½¹‘Ì™½È±½…°¥¹Ñ•É…Ñ¥½¸¸()Q¡”Ñ…É•Ð]!I€™½±±½ÝÌÑ¡”Í•±•Ñ•µ…¹…•µ•¹Ð™…µ¥±äÌ…‘‘É•ÍÌÉÕ±•Ì¸((ŒŒŒ]!P€å€èÍÑ…ÉÐ‰ä•Ù¥”%()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÄéÌÀÀÀÀÀÑ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()%€¡…ÌÑ¡”‘…Ñ…‰…Í”É…¹”€À¸¸ÐÈäÐäØÜÈäÕ€¸%Ð¥‘•¹Ñ¥™¥•ÌÑ¡”¥¹ÍÑ…±±••Ù¥”¥¹ÍÑ…¹”…¹µÕÍÐ¹½Ð‰”É•Á±…•‰ä„…Ñ…±½Õ”¥‘•¹Ñ¥™¥•È¸((ŒŒŒ]!P€ÄÑ€èÉ•Í•Ð=‰©•Ð½¹™¥ÕÉ…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÄéÌÀÀÀÀÀÕ€()I•Í•Ðµ…±°ÁÉ••‘•Ì•Ù•Éä…¹½¹¥…°½¹™-=€Á…å±½…¸%Ð¥¹‘¥…Ñ•ÌÉ•Á±…•µ•¹ÐµÍÑå±”…‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸¸Q¡”É•¥ÍÑ•É•½¹”µÍ±½ÐÙ…É¥…¹Ð¥Ì¹½ÐÕÍ•‰äÑ¡…ÐÍ•ÅÕ•¹”¸((ŒŒŒ]!P€Ñ€èÑÝ¼‘¥É•Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÄéÌÀÀÀÀÀÙ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()Q¡”ÑÝ¼]!P€Ñ€™É…µ•Ì¡…Ù”‘¥™™•É•¹ÐÉ½±•Ìè((´•Ù¥”€©m]!=t¨Ð©m]!I}-tŒ€Ñ•Éµ¥¹…Ñ•ÌÑ¡”•Ù¥”ÌÕÉÉ•¹ÐÉ•ÍÁ½¹Í”ÍÑÉ•…´¸(´AÉ½É…µµ•È€©m]!=t¨Ð¨ÀŒ€‘•±…É•ÌÑ¡”•¹½˜…‘Ù…¹•=‰©•ÐÝÉ¥Ñ•Ì…¹ÁÉ½µÁÑÌÑ¡”™¥¹…°É•ÍÕ±Ð¸()¼¹½Ð¹½Éµ…±¥é”Ñ¡•´¥¹Ñ¼½¹”‘¥É•Ñ¥½¹±•ÍÌµ…É­•È¸((ŒŒŒ]!P€ÔÅ€…¹€ÔÉ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÄéÌÀÀÀÀÀÝ€()]!P€ÔÅ€¥Ì…¸•ÉÉ½È…¹ÍÑ½ÁÌÑ¡”…‘Ù…¹•µÑÉ…¹Í™•ÈÑ¥µ•È¸]!P€ÔÉ€ÍÑ½ÁÌÑ¡…ÐÑ¥µ•È…¹ÍÑ…ÉÑÌÑ¡”Ñ¡É•”µÍ•½¹…•ÁÑ…¹”Ý…¥Ð‰•™½É”½ÕÑ•ÈÍ•ÍÍ¥½¸±½Í”¸()½¹™½¹™¥ÕÉ…Ñ½ÉÍ€¥¹±Õ‘•Ì]!P€ÔÅ€‰ÕÐ¹½Ð]!P€ÔÉ€ì¥ÑÌÁ½Í¥Ñ¥Ù”Á…Ñ •¹‘ÌÑ¡É½Õ ½¹™¥ÕÉ…Ñ½ÈÉ•Á½ÉÑÌ…¹•Ù¥”]!P€Ñ€¸((ŒŒŒ]!P€É€…¹€Í€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÄéÌÀÀÀÀÀá€()]!P€É€±½Í•ÌÑ¡”½ÕÑ•ÈÁÉ½É…µµ¥¹œÍ•ÍÍ¥½¸…¹ÍÑ½ÁÌ½¹™Q¥µ•=ÕÑ€¸()]!P€Í€¥ÌÍÑ½É•ÑÝ¥”¥¸=A8¹‘‰€Ý¥Ñ ½ÁÁ½Í¥Ñ”‘¥É•Ñ¥½¹Ì¸=Á•¹EÕ•Éä¹ÑáÑ€•áÁ±¥¥Ñ±ä±½…‘ÌÑ¡”ÁÉ½É…µµ•È…‰½ÉÐ™É…µ”¸¥É•Ñ¥½¸…¹…Ñ¥Ù”Í•ÍÍ¥½¸ÍÑ…Ñ”‘•Ñ•Éµ¥¹”Ý¡•Ñ¡•ÈÑ¡”ÁÉ½É…µµ•È½È•Ù¥”¥¹¥Ñ¥…Ñ•Ñ•Éµ¥¹…Ñ¥½¸¸((ŒŒŒ9…µ•ÍÁ…”‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÄéÌÀÀÀÀÀå€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()ÅÕ…°]!Q€Ù…±Õ•Ì¥¸‘¥…¹½ÍÑ¥Ì½È™Õ¹Ñ¥½¹…°½¹ÑÉ½°…É”¥¹‘•Á•¹‘•¹Ð¸¥…¹½ÍÑ¥Œ]!P€Ñ€¥Ì…±Í¼…¸•¹µ…É­•È°‰ÕÐ¥ÑÌ±¥™•å±”µÕÍÐ¹½Ð‰”ÍÕ‰ÍÑ¥ÑÕÑ•™½ÈÑ¡”ÁÉ½É…µµ¥¹œÍÑ…Ñ”µ…¡¥¹”Í½±•±ä‰•…ÕÍ”Ñ¡”¹Õµ‰•Èµ…Ñ¡•Ì¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀÈ()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒAÉ½Ñ½½°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÈéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°ÑÁ€°é¥‰••€)…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()=Á•¹]•‰9•Ð¥Ì„‘•±¥µ¥Ñ•Èµ™É…µ•…ÁÁ±¥…Ñ¥½¸ÁÉ½Ñ½½°ÕÍ•Ñ¼•á¡…¹”½µµ…¹‘Ì°•Ù•¹ÑÌ°ÍÑ…Ñ”°µ•…ÍÕÉ•µ•¹ÑÌ°½¹™¥ÕÉ…Ñ¥½¸‘…Ñ„°…¹Í•ÉÙ¥”¥¹™½Éµ…Ñ¥½¸Ý¥Ñ ½µÁ…Ñ¥‰±”…Ñ•Ý…åÌ…¹ÍåÍÑ•µÌ¸()½ÈÑ¡”ÁÕ‰±¥Í¡•Q@…Ñ•Ý…äÝ½É­™±½Ü°ÑÝ¼±…å•ÉÌµÕÍÐ¹½Ð‰”½±±…ÁÍ•è((Ä¸„½¹¹•Ñ¥½¸½Í•ÍÍ¥½¸±…å•ÈÑ¡…ÐÍ•±•ÑÌ½µµ…¹‘Ì°•Ù•¹ÑÌ°½ÈÁÉ½É…µµ•µÍ•¹…É¥¼ÑÉ…™™¥Œ…¹Á•É™½ÉµÌ…ÕÑ¡•¹Ñ¥…Ñ¥½¸Ý¡•É”É•ÅÕ¥É•ì(È¸…¸…ÁÁ±¥…Ñ¥½¸µ™É…µ”±…å•È¥¸Ý¡¥ ]!=€Í•±•ÑÌ„ÍåÍÑ•´…¹Ñ¡”É•µ…¥¹¥¹œ™¥•±‘Ì…É”¥¹Ñ•ÉÁÉ•Ñ•¥¸Ñ¡…ÐÍåÍÑ•´ÌÉ…µµ…È¸()=Ñ¡•È¥¹Ñ•É™…•Ì…¸…ÉÉä=Á•¹]•‰9•ÐÝ¥Ñ¡½ÕÐÑ¡¥ÌQ@Í•ÍÍ¥½¸Í•ÑÕÀ¸Q¡”mi¥	•”%¹Ñ•É™…•t¡é¥‰•”µ¥¹Ñ•É™…”¹µ¤¡…Ì‘¥ÍÑ¥¹ÐÍ•É¥…°°…‘‘É•ÍÍ¥¹œ°…­¹½Ý±•‘•µ•¹Ð°‘¥Í½Ù•Éä°…¹µ…¹…•µ•¹ÐÉÕ±•ÌìÍ•±•Ñ¥¹œ]!=€…±½¹”¥Ì¥¹ÍÕ™™¥¥•¹ÐÑ¼•ÍÑ…‰±¥Í Ñ¡”Ù…É¥…¹ÐÉ…µµ…È¸((ŒŒŒI•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÈéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°ÍÍ€°ÑÁ€°é¥‰••€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()ðQ½Á¥ŒðAÕÉÁ½Í”ð)ð€´´´ð€´´´ð)ðmM½Á”…¹É¡¥Ñ•ÑÕÉ•t¡Í½Á”µ…¹µ…É¡¥Ñ•ÑÕÉ”¹µ¤ð¹å±½Á•‘¥„‰½Õ¹‘…Éä°¥¹Ñ•É™…”…ÁÁ±¥…‰¥±¥Ñä°µ•¡…¹¥Í´½Ý¹•ÉÍ¡¥À°…¹•¹Ñ¥Ñä±…å•ÉÌð)ðmÉ…µ”Må¹Ñ…át¡™É…µ”µÍå¹Ñ…à¹µ¤ð½µµ½¸µ•ÍÍ…”™…µ¥±¥•Ì°‘•±¥µ¥Ñ•ÉÌ°•µÁÑä™¥•±‘Ì°…¹Á…É…µ•Ñ•É¥é•Ñ…Ìð)ðm½¹¹•Ñ¥½¸…¹M•ÍÍ¥½¹Ít¡Í•ÍÍ¥½¹Ì¹µ¤ðQ@…Ñ•Ý…äÍ•ÑÕÀ°Í•ÍÍ¥½¸Í•±•Ñ½ÉÌ°…¹Í•ÍÍ¥½¸ÍÑ…Ñ”ð)ðmÕÑ¡•¹Ñ¥…Ñ¥½¹t¡…ÕÑ¡•¹Ñ¥…Ñ¥½¸¹µ¤ð=Á•¸µÉ…¹”‰•¡…Ù¥½È°±•…ä…ÕÑ¡•¹Ñ¥…Ñ¥½¸‰½Õ¹‘…Éä°…¹!5¹•½Ñ¥…Ñ¥½¸ð)ðmMÑÉ•…´A…ÉÍ¥¹t¡ÍÑÉ•…´µÁ…ÉÍ¥¹œ¹µ¤ð%¹É•µ•¹Ñ…°Á…ÉÍ¥¹œ°Ñ½­•¹¥é…Ñ¥½¸°É•ÅÕ•ÍÐ½ÉÉ•±…Ñ¥½¸°…¹‘•™•¹Í¥Ù”±¥µ¥ÑÌð)ðm‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤ð]!I€¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸…¹Ñ¡”Í¡…É•ML½A0É½ÕÑ¥¹œµ½‘•°ð)ðm]!Qt¡Ý¡…Ð¹µ¤ð½µµ…¹°ÍÑ…Ñ”°…¹•Ù•¹ÐÍ•±•Ñ½ÈÍ•µ…¹Ñ¥Ìð)ðm%59M%=9t¡‘¥µ•¹Í¥½¹Ì¹µ¤ðAÉ½Á•ÉÑäÉ•ÅÕ•ÍÐ°É•Á½ÉÐ°…¹ÝÉ¥Ñ”™½ÉµÌð)ðm­¹½Ý±•‘•µ•¹ÑÍt¡…­¹½Ý±•‘•µ•¹ÑÌ¹µ¤ð-€½9-€É½±•Ì°¥¹±Õ‘¥¹œÉ•ÍÕ±ÐµÍ•ÅÕ•¹”Ñ•Éµ¥¹…Ñ¥½¸ð)ðmi¥	•”%¹Ñ•É™…•t¡é¥‰•”µ¥¹Ñ•É™…”¹µ¤ðM½ÕÉ”µÍ½Á•Í•É¥…°Ù…É¥…¹Ð°¹…µ•ÍÁ…”…ÁÁ±¥…‰¥±¥Ñä°…¹Õ¹É•Í½±Ù•½¹™±¥ÑÌð((ŒŒŒ½É”™¥•±‘Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÈéÌÀÀÀÀÀÍ€()AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()ð½¹•ÁÐðAÕÉÁ½Í”ð)ð€´´´ð€´´´ð)ð]!=€ðM•±•ÑÌÑ¡”™Õ¹Ñ¥½¹…°°‘¥…¹½ÍÑ¥Œ°Í•ÉÙ¥”°½È½¹¹•Ñ¥½¸µ±•Ù•°¹…µ•ÍÁ…”ð)ð]!Q€ð%‘•¹Ñ¥™¥•Ì„½µµ…¹°•Ù•¹Ð°½ÈÍÑ…Ñ”Ý¥Ñ¡¥¸„]!=€ð)ð]!I€ð%‘•¹Ñ¥™¥•ÌÑ¡”‘•ÍÑ¥¹…Ñ¥½¸½ÈÍ½ÕÉ”…½É‘¥¹œÑ¼Ñ¡…Ð]!=€Ì…‘‘É•ÍÌÉ…µµ…Èð)ð%59M%=9€ð%‘•¹Ñ¥™¥•Ì„É•…‘…‰±”°É•Á½ÉÑ…‰±”°½ÈÝÉ¥Ñ…‰±”ÁÉ½Á•ÉÑäÝ¥Ñ¡¥¸„]!=€ð)ð-€€¼9-€ðI•Á½ÉÑÌ…•ÁÑ…¹”½™…¥±ÕÉ”½ÈÑ•Éµ¥¹…Ñ•Ì„µÕ±Ñ¤µ™É…µ”É•ÍÁ½¹Í”Í•ÅÕ•¹”ð()]!Q€°]!I€°…¹%59M%=9€…É”¹½Ð±½‰…±±äÕ¹¥™½É´¹…µ•ÍÁ…•Ì¸I•Í½±Ù”]!=€…¹Ñ¡”™É…µ”™…µ¥±ä‰•™½É”¥¹Ñ•ÉÁÉ•Ñ¥¹œÑ¡•´¸((ŒŒŒ½µµ½¸…ÁÁ±¥…Ñ¥½¸µ™É…µ”™…µ¥±¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÈéÌÀÀÀÀÀÑ€()ðAÕÉÁ½Í”ð½É´ð)ð€´´´ð€´´´ð)ð½µµ…¹°ÍÑ…Ñ”°½È•Ù•¹Ðð€©]!<©]!P©]!IŒ€ð)ðMÑ…ÑÕÌÉ•ÅÕ•ÍÐð€¨]!<©]!IŒ€ð)ð%59M%=9€É•ÅÕ•ÍÐð€¨]!<©]!I©%59M%=8Œ€ð)ð%59M%=9€É•ÍÁ½¹Í”½ÈÉ•Á½ÉÐð€¨]!<©]!I©%59M%=8©Y1U¸¸¸Œ€ð)ð%59M%=9€ÝÉ¥Ñ”ð€¨]!<©]!I¨%59M%=8©Y1U¸¸¸Œ€ð)ðA½Í¥Ñ¥Ù”…­¹½Ý±•‘•µ•¹Ðð€¨Œ¨ÄŒ€ð)ð9•…Ñ¥Ù”…­¹½Ý±•‘•µ•¹Ðð€¨Œ¨ÀŒ€ð()Q¡”¹½Ñ…Ñ¥½¸…‰½Ù”‘•ÍÉ¥‰•ÌÍÑÉÕÑÕÉ”°¹½Ð„½µÁ±•Ñ”É…µµ…È¸¥•±‘Ì…¸‰”•µÁÑä½ÈÁ…É…µ•Ñ•É¥é•°…¹Ù…±¥Ù…±Õ•Ì‘•Á•¹½¸Ñ¡”Í•±•Ñ•ÍåÍÑ•´¸((ŒŒŒ½¹¹•Ñ¥½¸Ý½É­™±½Ü()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÈéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°ÑÁ€)…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()½ÈÑ¡”ÁÕ‰±¥Í¡•Q@…Ñ•Ý…äÝ½É­™±½Üè((Ä¸½¹¹•ÐÑ¼Á½ÉÐ€ÈÀÀÀÁ€ì(È¸É••¥Ù”Ñ¡”Í•ÉÙ•ÈÉ••Ñ¥¹œ-€ì(Ì¸Í•±•ÐÑ¡”½µµ…¹‘Ì½…Ñ¥½¹Ì°•Ù•¹ÑÌ°½ÈÁÉ½É…µµ•µÍ•¹…É¥¼Í•ÍÍ¥½¸ì(Ð¸½µÁ±•Ñ”…ÕÑ¡•¹Ñ¥…Ñ¥½¸¥˜Ñ¡”…Ñ•Ý…äÉ•ÅÕ¥É•Ì¥Ðì(Ô¸•á¡…¹”…ÁÁ±¥…Ñ¥½¸™É…µ•Ì…½É‘¥¹œÑ¼Ñ¡”…Ñ¥Ù”Í•ÍÍ¥½¸¸()M•ÍÍ¥½¸Í•±•Ñ½ÉÌÍÕ …Ì€¨ää¨äŒ€…É”½¹¹•Ñ¥½¸µ½¹ÑÉ½°™É…µ•Ì¸Q¡•äµÕÍÐ¹½Ð‰”¥¹Ñ•ÉÁÉ•Ñ•…Ì½É‘¥¹…Éä™Õ¹Ñ¥½¹…°]!<€äå€ÑÉ…™™¥Œ¸((ŒŒŒ%¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸½É‘•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÈéÌÀÀÀÀÀÙ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()É•±¥…‰±”¥µÁ±•µ•¹Ñ…Ñ¥½¸Í¡½Õ±ÁÉ½•ÍÌ„µ•ÍÍ…”¥¸Ñ¡¥Ì½É‘•Èè((Ä¸É•½Ù•ÈÑ¡”½µÁ±•Ñ”É…Ü™É…µ”™É½´Ñ¡”‰åÑ”ÍÑÉ•…´ì(È¸É•½¹¥é”…­¹½Ý±•‘•µ•¹Ð°Í•ÍÍ¥½¸µ½¹ÑÉ½°°½È…ÁÁ±¥…Ñ¥½¸µ™É…µ”ÍÑÉÕÑÕÉ”ì(Ì¸É•Í½±Ù”]!=€ì(Ð¸Á…ÉÍ”]!Q€°]!I€°…¹%59M%=9€ÕÍ¥¹œÑ¡”Í•±•Ñ•¹…µ•ÍÁ…”ì(Ô¸Ù…±¥‘…Ñ”½Á•É…Ñ¥½¸µÍÁ•¥™¥ŒÉ…¹•Ìì(Ø¸Ý¡•É”„Á¡åÍ¥…°•Ù¥”¥Ì¥¹Ù½±Ù•°Ù…±¥‘…Ñ”Ñ¡”Ñ…É•Ð=‰©•ÐÌ…Á…‰¥±¥Ñä¸()Må¹Ñ…Ñ¥ŒÙ…±¥‘¥Ñä‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…Ð„•Ù¥”ÍÕÁÁ½ÉÑÌ…¸½Á•É…Ñ¥½¸¸Q¡”™Õ¹Ñ¥½¹…°É•™•É•¹”‘•™¥¹•ÌÝ¥É”Í•µ…¹Ñ¥ÌìÑ¡”m•Ù¥”5½‘•±t ¸¸½‘•Ù¥”µµ½‘•°¼¤…¹…Ñ…±½Õ”•Ù¥‘•¹”‘•™¥¹”•Ù¥”½=‰©•Ð…ÁÁ±¥…‰¥±¥Ñä¸((ŒŒŒI•™•É•¹”½É…¹¥é…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÈéÌÀÀÀÀÀÝ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()Q¡¥Ì‘¥É•Ñ½Éä½¹Ñ…¥¹Ìµ•¡…¹¥ÌÍ¡…É•…É½ÍÌÍåÍÑ•µÌ¸mM½Á”…¹É¡¥Ñ•ÑÕÉ•t¡Í½Á”µ…¹µ…É¡¥Ñ•ÑÕÉ”¹µ¤‘•™¥¹•ÌÑ¡”‰½Õ¹‘…Éä‰•ÑÝ••¸¥¹Ñ•É™…•Ì°ÉÕ¹Ñ¥µ”½¹ÑÉ½°°‘¥Í½Ù•Éä°¥¹Ñ•ÉÙ¥•Ü°½¹™¥ÕÉ…Ñ¥½¸É•…‘¥¹œ°ÁÉ½É…µµ¥¹œ°…¹…Ñ…±½Õ”…Á…‰¥±¥Ñä¸Õ¹Ñ¥½¹…°½µµ…¹‘Ì…¹ÁÉ½Á•ÉÑ¥•Ì…É”½É…¹¥é•‰ä]!=€Õ¹‘•Èm™Õ¹Ñ¥½¹…°½t ¸¸½™Õ¹Ñ¥½¹…°¼¤¸¥…¹½ÍÑ¥Œ…¹ÁÉ½É…µµ¥¹œÁÉ½Ñ½½±ÌÉ•ÕÍ”Ñ¡”™É…µ”±…¹Õ…”‰ÕÐ‘•™¥¹”Í•Á…É…Ñ”½Á•É…Ñ¥½¹Ì°Í•ÅÕ•¹•Ì°…¹•Ù¥‘•¹”‰½Õ¹‘…É¥•ÌÕ¹‘•Èm‘¥…¹½ÍÑ¥Ì½t ¸¸½‘¥…¹½ÍÑ¥Ì¼¤…¹mÁÉ½É…µµ¥¹œ½t ¸¸½ÁÉ½É…µµ¥¹œ¼¤¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÈéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÑÁ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡”½µµ½¸Íå¹Ñ…à…¹Q@Í•ÍÍ¥½¸µ½‘•°…É”É½Õ¹‘•¥¸m=Á•¹]•‰9•Ð%¹ÑÉ½‘ÕÑ¥½¸ÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=]9}%¹ÑÉ½}9¹Á‘˜¤¸!5‰•¡…Ù¥½È¥ÌÉ½Õ¹‘•¥¸m!µ…ŒÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½!µ…Œ¹Á‘˜¤¸MåÍÑ•´µÍÁ•¥™¥ŒÍ•µ…¹Ñ¥Ì½µ”™É½´Ñ¡”½ÉÉ•ÍÁ½¹‘¥¹œÁÕ‰±¥Œ]!=€‘½Õµ•¹Ð°5å!=5MÕ¥Ñ”¥µÁ±•µ•¹Ñ…Ñ¥½¸‘…Ñ„°½È•áÁ±¥¥Ñ±ä¥‘•¹Ñ¥™¥•½‰Í•ÉÙ•ÑÉ…™™¥ŒìÑ¡½Í”•Ù¥‘•¹”±…ÍÍ•Ì…É”¹½ÐÑÉ•…Ñ•…Ì¥¹Ñ•É¡…¹•…‰±”¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀÌ()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½…­¹½Ý±•‘•µ•¹ÑÌ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒ­¹½Ý±•‘•µ•¹ÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÌéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°ÑÁ€°é¥‰••€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€()-€…¹9-€…É”ÍÑ…¹‘…±½¹”=Á•¹]•‰9•Ð™É…µ•Ì¸Q¡•ä½¹Ñ…¥¸¹¼]!=€°]!Q€°]!I€°½È%59M%=9€™¥•±¸()ðI•ÍÕ±ÐðÉ…µ”ð)ð€´´´ð€´´´ð)ð-€ð€¨Œ¨ÄŒ€ð)ð9-€ð€¨Œ¨ÀŒ€ð()Q¡•¥Èµ•…¹¥¹œ‘•Á•¹‘Ì½¸Ñ¡”…Ñ¥Ù”½¹¹•Ñ¥½¸ÍÑ…Ñ”…¹½Á•É…Ñ¥½¸¸Q¡•ä…É”¹½Ð±½‰…±±ä•ÅÕ¥Ù…±•¹ÐÑ¼ƒŠqÑ¡”•Ù¥”¥Ì¹½Ü¥¸Ñ¡”É•ÅÕ•ÍÑ•ÍÑ…Ñ”»Št()Q¡”É½±•Ì‰•±½ÜÁÉ¥µ…É¥±ä™½±±½ÜÑ¡”Q@…Ñ•Ý…ä¥¹ÑÉ½‘ÕÑ¥½¸¸AÉ½‘ÕÐµÍÁ•¥™¥Œ•áÑ•¹Í¥½¹Ì¥¹±Õ‘”0ÐØàÙM,€¨Œ©àŒ€•ÉÉ½È™½ÉµÌ…¹Ñ¡”mi¥	•”%¹Ñ•É™…•t¡é¥‰•”µ¥¹Ñ•É™…”¹µ¤	UMd9,€¨Œ¨ØŒ€™½±±½Ý•‰ä9,¸¼¹½ÐÉ•©•Ð½È½ÉÉ•±…Ñ”Ñ¡•Í”Ñ¡É½Õ „ÑÝ¼µÙ…±Õ”…­¹½Ý±•‘•µ•¹Ðµ½‘•°Ý¥Ñ¡½ÕÐÑ¡”…ÁÁ±¥…‰±”¥¹Ñ•É™…”½¹Ñ•áÐ¸((ŒŒŒI½±•Ì½˜-€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÌéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°ÑÁ€()Q¡”…¹½¹¥…°¥¹ÑÉ½‘ÕÑ¥½¸ÕÍ•Ì-€¥¸Í•Ù•É…°É½±•Ìè((´Ñ¡”Í•ÉÙ•ÈÉ••Ñ¥¹œ…™Ñ•È„Q@½¹¹•Ñ¥½¸½Á•¹Ìì(´…•ÁÑ…¹”½˜„Í•ÍÍ¥½¸Í•±•Ñ½Èì(´…ÕÑ¡•¹Ñ¥…Ñ¥½¸¹•½Ñ¥…Ñ¥½¸½È…ÕÑ¡•¹Ñ¥…Ñ¥½¸ÍÕ•ÍÌì(´Á½Í¥Ñ¥Ù”ÁÉ½•ÍÍ¥¹œÉ•ÍÕ±Ð™½È„½µµ…¹½ÈÝÉ¥Ñ”ì(´Ñ•Éµ¥¹…Ñ¥¹œµ…É­•È…™Ñ•È½¹”½Èµ½É”ÍÑ…ÑÕÌ½È%59M%=9€É•ÍÁ½¹Í”™É…µ•Ì¸()½È„½µµ…¹½ÈÝÉ¥Ñ”°-€¥¹‘¥…Ñ•ÌÑ¡…ÐÑ¡”…Ñ•Ý…ä½¹Í¥‘•É•Ñ¡”µ•ÍÍ…”Íå¹Ñ…Ñ¥…±±ä…¹Í•µ…¹Ñ¥…±±ä…•ÁÑ…‰±”¥¸Ñ¡…Ð¥¹Ñ•É…Ñ¥½¸¸%Ð‘½•Ì¹½Ð¥¹‘•Á•¹‘•¹Ñ±äÁÉ½Ù”Ñ¡”™¥¹…°Á¡åÍ¥…°ÍÑ…Ñ”½˜…¸…ÑÕ…Ñ½È¸]¡•¸™¥¹…°ÍÑ…Ñ”µ…ÑÑ•ÉÌ°É•ÅÕ•ÍÐ½È½‰Í•ÉÙ”Ñ¡”É•±•Ù…¹ÐÍÑ…Ñ”…™Ñ•ÉÝ…É¸((ŒŒŒI½±•Ì½˜9-€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÌéÌÀÀÀÀÀÍ€()U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()9-€É•Á½ÉÑÌÑ¡…ÐÑ¡”µ•ÍÍ…”½È…Ñ¥Ù”½Á•É…Ñ¥½¸™…¥±•Í•µ…¹Ñ¥Œ½ÈÍå¹Ñ…Ñ¥ŒÁÉ½•ÍÍ¥¹œ¸Q¡”™É…µ”½¹Ñ…¥¹Ì¹¼É•…Í½¸½‘”¸()%¸„µÕ±Ñ¤µ™É…µ”ÍÑ…ÑÕÌ½È%59M%=9€É•ÍÁ½¹Í”°9-€…¸…±Í¼Ñ•Éµ¥¹…Ñ”Ñ¡”Í•ÅÕ•¹”¸Q¡”¥¹ÑÉ½‘ÕÑ½ÉäÍÁ•¥™¥…Ñ¥½¸ÍÑ…Ñ•ÌÑ¡…ÐÑ¡”±¥•¹Ðµ…ä½¹Í¥‘•È™É…µ•ÌÉ••¥Ù••…É±¥•È¥¸Ñ¡…ÐÉ•ÍÁ½¹Í”Í•ÅÕ•¹”¥¹Ù…±¥¸±¥•¹ÐÍ¡½Õ±Ñ¡•É•™½É”ÍÑ…”µÕ±Ñ¤µ™É…µ”É•ÍÕ±ÑÌÕ¹Ñ¥°¥ÐÉ••¥Ù•ÌÑ¡”Ñ•Éµ¥¹…Ñ¥¹œ…­¹½Ý±•‘•µ•¹Ð¸((ŒŒŒ½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÌéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€()=Á•¹]•‰9•Ð…­¹½Ý±•‘•µ•¹Ð™É…µ•Ì‘¼¹½Ð…ÉÉäÑÉ…¹Í…Ñ¥½¸¥‘•¹Ñ¥™¥•ÉÌ¸½ÉÉ•±…Ñ¥½¸½µ•Ì™É½´½¹¹•Ñ¥½¸ÍÑ…Ñ”…¹É•ÅÕ•ÍÐ½É‘•É¥¹œ¸()=¸„½µµ…¹Í•ÍÍ¥½¸°­••À…Ðµ½ÍÐ½¹”Õ¹É•Í½±Ù•É•ÅÕ•ÍÐÕ¹±•ÍÌÑ¡”ÍÁ•¥™¥Œ…Ñ•Ý…ä‰•¡…Ù¥½ÈÁÉ½Ù•ÌÑ¡…ÐÁ¥Á•±¥¹¥¹œ¥ÌÍÕÁÁ½ÉÑ•¸=¸…¸•Ù•¹ÐÍ•ÍÍ¥½¸°‘¼¹½Ð…ÑÑ… …¸Õ¹É•±…Ñ•…Íå¹¡É½¹½ÕÌ•Ù•¹ÐÑ¼„Á•¹‘¥¹œ½µµ…¹µ•É•±ä‰•…ÕÍ”¥Ð…ÉÉ¥Ù•Ì¹•…É‰ä¥¸Ñ¥µ”¸((ŒŒŒÉÉ½È¡…¹‘±¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÌéÌÀÀÀÀÀÕ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()]¡•¸„9-€¥ÌÉ••¥Ù•è((Ä¸±…ÍÍ¥™ä¥ÐÕÍ¥¹œÑ¡”…Ñ¥Ù”ÍÑ…Ñ”èÍ•ÍÍ¥½¸Í•±•Ñ¥½¸°…ÕÑ¡•¹Ñ¥…Ñ¥½¸°½µµ…¹½ÝÉ¥Ñ”°½ÈÉ•ÍÕ±ÐÍ•ÅÕ•¹”ì(È¸‘¥Í…É½ÈÅÕ…É…¹Ñ¥¹”¥¹½µÁ±•Ñ”É•ÍÕ±ÑÌÝ¡•É”É•ÅÕ¥É•ì(Ì¸‘¼¹½Ð¥¹Ù•¹Ð…¸•ÉÉ½ÈÉ•…Í½¸…‰Í•¹Ð…¹½Ñ¡•È™É…µ”½È¥µÁ±•µ•¹Ñ…Ñ¥½¸Í¥¹…°ì(Ð¸‘•¥‘”Ý¡•Ñ¡•ÈÑ¡”Í•ÍÍ¥½¸É•µ…¥¹ÌÕÍ…‰±”™É½´Ñ¡”½Á•É…Ñ¥½¸µÍÁ•¥™¥ŒÝ½É­™±½Üì(Ô¸±½œÑ¡”É…Ü™É…µ”…¹ÍÑ…Ñ”ÑÉ…¹Í¥Ñ¥½¸°É•‘…Ñ¥¹œ…ÕÑ¡•¹Ñ¥…Ñ¥½¸‘…Ñ„¸()½¹¹•Ñ¥½¸±½ÍÕÉ”…¸¥ÑÍ•±˜‰”Ñ¡”™…¥±ÕÉ”Í¥¹…°‘ÕÉ¥¹œ…ÕÑ¡•¹Ñ¥…Ñ¥½¸½ÈÕ¹ÍÕÁÁ½ÉÑ•¹•½Ñ¥…Ñ¥½¸¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÌéÌÀÀÀÀÀÙ€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”™É…µ”Ù…±Õ•Ì°…•ÁÑ…¹”Í•µ…¹Ñ¥Ì°…¹•¹µ½˜µÍ•ÅÕ•¹”‰•¡…Ù¥½È½µ”™É½´m=Á•¹]•‰9•Ð%¹ÑÉ½‘ÕÑ¥½¸ÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=]9}%¹ÑÉ½}9¹Á‘˜¤°Á…ÉÑ¥Õ±…É±äƒŠqA…ÉÑ¥Õ±…È=Á•¸5•ÍÍ…•ÏŠt…¹Ñ¡”ÍÑ…ÑÕÌ½%59M%=9€É•ÅÕ•ÍÐÍ•ÅÕ•¹•Ì¸M•ÍÍ¥½¸µÍÁ•¥™¥Œ…ÕÑ¡•¹Ñ¥…Ñ¥½¸‰•¡…Ù¥½È¥ÌÉ•™¥¹•‰äm!µ…ŒÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½!µ…Œ¹Á‘˜¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀÐ()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½…‘‘É•ÍÍ¥¹œ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒ‘‘É•ÍÍ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€°é¥‰••€)…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()=Á•¹]•‰9•Ð…‘‘É•ÍÍ¥¹œ¥ÌÍåÍÑ•´µÍÁ•¥™¥Œ¸]!I€¥‘•¹Ñ¥™¥•ÌÑ¡”‘•ÍÑ¥¹…Ñ¥½¸½ÈÍ½ÕÉ”½˜„™É…µ”°‰ÕÐ¥ÑÌÉ…µµ…È‘•Á•¹‘Ì½¸Ñ¡”Í•±•Ñ•]!=€…¹µÕÍÐ¹½Ð‰”¥¹Ñ•ÉÁÉ•Ñ•…Ì„Í¥¹±”Õ¹¥Ù•ÉÍ…°…‘‘É•ÍÌÑåÁ”¸()I•Í½±Ù”Ñ¡”¥¹Ñ•É™…”½Ù…É¥…¹Ð…ÌÝ•±°…Ì]!=€èÑ¡”mi¥	•”%¹Ñ•É™…•t¡é¥‰•”µ¥¹Ñ•É™…”¹µ¤ÕÍ•ÌÁÉ½‘ÕÐ½Õ¹¥Ð…‘‘É•ÍÍ•ÌÝ¥Ñ €Œå€•Ù•¸™½È¹…µ•ÍÁ…•ÌÍÕ …Ì1¥¡Ñ¥¹œ…¹ÕÑ½µ…Ñ¥½¸¸Q¡”€½A1€…¹É½ÕÑ¥¹œµ…Ñ•É¥…°‰•±½Ü½¹•É¹ÌÑ¡”MLÍ½ÕÉ•Ì¸((ŒŒŒ‘‘É•ÍÌ¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€)…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()Á…ÉÍ•ÈµÕÍÐÉ•Í½±Ù”]!=€‰•™½É”¥¹Ñ•ÉÁÉ•Ñ¥¹œ]!I€¸¥™™•É•¹ÐÍåÍÑ•µÌ…¸ÕÍ”‘¥™™•É•¹Ð…‘‘É•ÍÌ±…å½ÕÑÌ°É…¹•Ì°¡¥•É…É¡ä±•Ù•±Ì°…¹…‘Ù…¹•µ…‘‘É•ÍÌ™½ÉµÌ¸()1¥¡Ñ¥¹œ€¡]!<€Å€¤…¹ÕÑ½µ…Ñ¥½¸€¡]!<€É€¤Í¡…É”Ñ¡”ML€½A1€…‘‘É•ÍÌ™…µ¥±ä°‰ÕÐÑ¡•¥ÈÁÕ‰±¥Í¡•]!I€Ñ…‰±•Ì…É”¹½Ð¥‘•¹Ñ¥…°¸½µµ½¸Á½¥¹Ð°…É•„°É½ÕÀ°…¹•¹•É…°™½ÉµÌ…¸Ñ¡•É•™½É”‰”‘•ÍÉ¥‰•Ñ½•Ñ¡•È½¹±äÝ¡•É”‰½Ñ ÍÁ•¥™¥…Ñ¥½¹Ì…É•”ì±•ÍÌ½µµ½¸±½…°µ‰ÕÌÙ…É¥…¹ÑÌµÕÍÐÉ•µ…¥¸]!=€µÍÁ•¥™¥Œ¸()=Ñ¡•ÈÍåÍÑ•µÌ°ÍÕ …ÌQ¡•Éµ½É•Õ±…Ñ¥½¸…¹¹•Éä5…¹…•µ•¹Ð°ÕÍ”‘¥™™•É•¹ÐÉ…µµ…ÉÌ…¹µÕÍÐ¹½Ð‰”‘•½‘•Ý¥Ñ Ñ¡”€½A1€ÉÕ±•Ì‰•±½Ü¸((ŒŒŒ1¥¡Ñ¥¹œ…¹ÕÑ½µ…Ñ¥½¸½A0É…µµ…È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÀÍ€((ŒŒŒŒ½µµ½¸ÁÉ¥Ù…Ñ”µÉ¥Í•È™½ÉµÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÀÑ€()Q¡”ÁÕ‰±¥Í¡•]!<€Å€…¹]!<€É€ÍÁ•¥™¥…Ñ¥½¹Ì…É•”½¸Ñ¡•Í”‰…Í”™½ÉµÌè()ðM½Á”ð]!I€Íå¹Ñ…àðY…±¥Ù…±Õ•Ìð)ð€´´´ð€´´´ð€´´´ð)ð•¹•É…°ð€Á€ð½µÁ±•Ñ”ÍåÍÑ•´Í•±•Ñ•‰ä]!=€ð)ð¹Ù¥É½¹µ•¹Ð€¼…É•„ð€ð€ÀÁ€°€Ä¸¸å€°½È€ÄÀÁ€ð)ðA½¥¹ÐÑ¼Á½¥¹ÐðA1€ðÙ…±¥½µ‰¥¹…Ñ¥½¹Ì±¥ÍÑ•‰•±½Üð)ðÉ½ÕÀð€I€ðH€ô€Ä¸¸ÈÔÕ€ð()Q¡”±…‰•±Ì€©•¹Ù¥É½¹µ•¹Ð¨°€©…µ‰¥•¹Ð¨°…¹€©…É•„¨…É”ÕÍ•‰ä‘¥™™•É•¹ÐÍ½ÕÉ•Ì™½ÈÑ¡”Í…µ”½±±•Ñ¥Ù”€±•Ù•°¸Q¡”µ•…¹¥¹œÉ•µ…¥¹ÌÍ½Á•Ñ¼Ñ¡”Í•±•Ñ•™Õ¹Ñ¥½¹…°]!=€¸((ŒŒŒŒA½¥¹ÐµÑ¼µÁ½¥¹Ð½A0()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÀÕ€()Á½¥¹Ð…‘‘É•ÍÌ¥ÌÑ¡”½¹…Ñ•¹…Ñ¥½¸½˜¥ÑÌ€…¹A1€É•ÁÉ•Í•¹Ñ…Ñ¥½¹Ìì¥Ð¥Ì¹½Ð…¸…É‰¥ÑÉ…Éä‘•¥µ…°¥¹Ñ••È¸()ð€É•ÁÉ•Í•¹Ñ…Ñ¥½¸ðY…±¥A1€ðá…µÁ±•Ìð)ð€´´´ð€´´´ð€´´´ð)ð€Ä¸¸å€ð€Ä¸¸å€ð€ÄÅ€°€ÔÙ€°€äå€ð)ð€ÀÁ€ð€ÀÄ¸¸ÄÕ€ð€ÀÀÀÅ€°€ÀÀÄÕ€ð)ð€ÄÁ€ð€ÀÄ¸¸ÄÕ€ð€ÄÀÀÅ€°€ÄÀÄÕ€ð)ð€ÀÄ¸¸Àå€ð€ÄÀ¸¸ÄÕ€ð€ÀÄÄÁ€°€ÀäÄÕ€ð()Q¡”½É‘¥¹…ÉäÁ¡åÍ¥…°µ½¹™¥ÕÉ…Ñ½ÈÉ…¹”Ñ¡•É•™½É”ÁÉ½‘Õ•ÌÑÝ¼µ‘¥¥ÐÁ½¥¹Ð…‘‘É•ÍÍ•ÌÍÕ …Ì€ÔÙ€¸áÑ•¹‘•Ù…±Õ•ÌÁÉ½‘Õ”™½ÕÈµ‘¥¥Ð™½ÉµÌÍÕ …Ì€ÀÀÄÕ€°€ÀÌÄÅ€°½È€ÄÀÄÑ€¸Ñ¡É•”µ‘¥¥ÐÍÑÉ¥¹œ¥Ì¹½Ð„Ù…±¥É•ÁÉ•Í•¹Ñ…Ñ¥½¸½˜Ñ¡¥ÌÉ…µµ…Èè±•…‘¥¹œé•É½•Ì…É”É•ÅÕ¥É•Ñ¼­••ÀÑ¡”€½A1€‰½Õ¹‘…ÉäÕ¹…µ‰¥Õ½ÕÌ¸()½È•á…µÁ±”°€ÔÙ€¥ÌôÔ°A0ôÙ€ì€ÀÌÄÅ€¥ÌôÀÌ°A0ôÄÅ€ì…¹€ÄÀÄÑ€¥ÌôÄÀ°A0ôÄÑ€¸½¹Ù•ÉÑ¥¹œ]!I€Ñ¼…¸¥¹Ñ••È‰•™½É”Á…ÉÍ¥¹œÝ½Õ±‘•ÍÑÉ½ä¥¹™½Éµ…Ñ¥½¸É•ÅÕ¥É•Ñ¼‘¥ÍÑ¥¹Õ¥Í Ñ¡•Í”™½ÉµÌ¸((ŒŒŒŒ½±±•Ñ¥Ù”…‘‘É•ÍÍ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÀÙ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()]!IôÁ€¥ÌÑ¡”•¹•É…°…‘‘É•ÍÌ…¹Ñ…É•ÑÌÑ¡”½µÁ±•Ñ”™Õ¹Ñ¥½¹…°ÍåÍÑ•´Í•±•Ñ•‰ä]!=€¸()¸•¹Ù¥É½¹µ•¹Ð½…É•„…‘‘É•ÍÌ½¹Ñ…¥¹Ì½¹±äÑ¡”€½µÁ½¹•¹Ð¸Y…±¥™½ÉµÌ…É”€Ä¸¸å€°€ÀÁ€°…¹€ÄÀÁ€¸%¸Á…ÉÑ¥Õ±…È°€ÄÀÁ€¥ÌÑ¡”½±±•Ñ¥Ù”…‘‘É•ÍÌ™½ÈôÄÁ€ì¥Ð¥Ì¹½Ð„Á½¥¹Ð…‘‘É•ÍÌ¸()É½ÕÀ…‘‘É•ÍÌ¥Ì•áÁ±¥¥Ñ±äµ…É­•‰ä€€è€ŒÄ¸¸ŒÈÔÕ€¸Q¡”ÁÉ•™¥à¥ÌÁ…ÉÐ½˜Ñ¡”ÁÉ½Ñ½½°Íå¹Ñ…à°Í¼„É½ÕÀµÕÍÐ¹½Ð‰”É•ÁÉ•Í•¹Ñ•…ÌÑ¡”‰…É”‘•¥µ…°É½ÕÀ¹Õµ‰•È¸((ŒŒŒI½ÕÑ¥¹œÅÕ…±¥™¥•ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÀÝ€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”ÁÕ‰±¥ŒÍÁ•¥™¥…Ñ¥½¹Ì…¹5å!=5MÕ¥Ñ”¥µÁ±•µ•¹Ñ…Ñ¥½¸‘…Ñ„…É”µ½ÍÐ½¡•É•¹Ñ±äÉ•ÁÉ•Í•¹Ñ•…Ì„€¨©‰…Í”…‘‘É•ÍÌÁ±ÕÌ…¸½ÁÑ¥½¹…°É½ÕÑ¥¹œÅÕ…±¥™¥•È¨¨è()Ñ•áÐ)	M)	MŒÌ)	MŒÐ%9QI)€()	M€¥ÌÑ¡”™Õ¹Ñ¥½¹…°Ñ…É•Ðè•¹•É…°°É•„°É½ÕÀ°½ÈÁ½¥¹ÐÝ¡•É”Ñ¡…Ð½µ‰¥¹…Ñ¥½¸¥Ì‘•™¥¹•‰äÑ¡”Í•±•Ñ•]!=€¸%9QI€¥ÌÑ¡”…‘‘É•ÍÌ½˜Ñ¡”É½ÕÑ¥¹œ¥¹Ñ•É™…”¸Q¡”%¹Ñ€±…‰•°ÕÍ•‰äÑ¡”]!<€Å€ÍÁ•¥™¥…Ñ¥½¸°Ñ¡”¥¹Ñ•É™…•€±…‰•°ÕÍ•‰ä]!<€É€°…¹Ñ¡”$Í€½$Ñ€½µÁ½¹•¹ÑÌÕÍ•‰ä5å!=5MÕ¥Ñ”‘•ÍÉ¥‰”Ñ¡”Í…µ”¥¹Ñ•É™…”µ…‘‘É•ÍÌ½¹•ÁÐ¥¸Ñ¡•¥ÈÉ•ÍÁ•Ñ¥Ù”¹½Ñ…Ñ¥½¹Ì¸()€ŒÍ€Í•±•ÑÌÑ¡”É¥Í•È½‰…­‰½¹”±•Ù•°¸€ŒÐ%9QI€Í•±•ÑÌ„±½…°‰ÕÌÉ•…¡•Ñ¡É½Õ Ñ¡”ÍÁ•¥™¥•¥¹Ñ•É™…”¸Q¡•Í”ÍÕ™™¥á•Ì…É”Ñ¡•É•™½É”É½ÕÑ¥¹œÅÕ…±¥™¥…Ñ¥½¹Ì½˜„Ñ…É•Ð…‘‘É•ÍÌÉ…Ñ¡•ÈÑ¡…¸¹•ÜÁ½¥¹Ðµ…‘‘É•ÍÌ™½Éµ…ÑÌ¸((ŒŒŒŒ1•Ù•°€Ì€¼É¥Í•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÀá€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()5å!=5MÕ¥Ñ”Ì…‘‘É•ÍÌµÉÕ±”µ½‘•°½¹Ñ…¥¹ÌÍ•Á…É…Ñ”±•Ù•°µÉÕ±”™¥•±‘Ì…¹ÍÕÁÁ½ÉÑÌ„1•Ù•°´Ì½É¥Í•ÈÅÕ…±¥™¥…Ñ¥½¸±…å•È¸Ý¥É”™½É´ÍÕ …Ì	MŒÍ€°Ý¡•¸•ÍÑ…‰±¥Í¡•™½ÈÑ¡”Í•±•Ñ•ÍåÍÑ•´…¹½Á•É…Ñ¥½¸°Í¡½Õ±‰”É•Ñ…¥¹•ÍÑÉÕÑÕÉ…±±äèÑ¡”ÅÕ…±¥™¥•È¥Ì¹½ÐÁ…ÉÐ½˜€°A1€°½È„É½ÕÀ¹Õµ‰•È¸()Q¡”ÁÉ•Í•ÉÙ•ÁÕ‰±¥Œ]!<€Å€Ñ…‰±”‘•ÍÉ¥‰•ÌÕ¹ÅÕ…±¥™¥•ÁÉ¥Ù…Ñ”µÉ¥Í•ÈÑ…É•ÑÌ…¹•áÁ±¥¥Ð1•Ù•°´Ð™½ÉµÌì¥Ð‘½•Ì¹½Ð¥ÑÍ•±˜•¹Õµ•É…Ñ”	MŒÍ€Ù…É¥…¹ÑÌ¸1•Ù•°´Ì…ÁÁ±¥…‰¥±¥Ñä¥ÌÑ¡•É•™½É”¥µÁ±•µ•¹Ñ…Ñ¥½¸½…‘‘É•ÍÌµÉÕ±”•Ù¥‘•¹”¥¸Ñ¡¥Ì½ÉÁÕÌ°¹½Ð„ÁÕ‰±¥Í¡•Õ¹¥Ù•ÉÍ…°1¥¡Ñ¥¹œÉ…µµ…È¸¼¹½Ð•¹•É…Ñ”€ÀŒÍ€°ŒÍ€°€HŒÍ€°½ÈA0ŒÍ€µ•É•±ä™É½´Ñ¡”•¹•É…±¥é•µ½‘•°Ý¥Ñ¡½ÕÐÍåÍÑ•´´…¹½Á•É…Ñ¥½¸µÍÁ•¥™¥Œ•Ù¥‘•¹”¸((ŒŒŒŒ1•Ù•°€Ð€¼±½…°‰ÕÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()1½…°µ‰ÕÌ…‘‘É•ÍÍ¥¹œ¥ÌÑ¡”1•Ù•°´ÐÉ½ÕÑ¥¹œ™½É´è()Ñ•áÐ)	MŒÐ%9QI)€()%9QI€¥ÌÑ¡”É½ÕÑ¥¹œµ¥¹Ñ•É™…”…‘‘É•ÍÌ¸Q¡”ÁÕ‰±¥Í¡•ÍÁ•¥™¥…Ñ¥½¹ÌÕÍ”‘¥™™•É•¹Ð±…‰•±Ì™½ÈÑ¡”Í…µ”™¥•±è%¹Ñ€¥¸]!<€Å€…¹¥¹Ñ•É™…•€¥¸]!<€É€ì5å!=5MÕ¥Ñ”É•ÁÉ•Í•¹ÑÌ¥ÑÌ½µÁ½¹•¹ÑÌ…Ì$Í€½$Ñ€¸()Q¡”½µ‰¥¹•1¥¡Ð½ÕÑ½µ…Ñ¥½¸µ½‘•°¥¸5å!=5MÕ¥Ñ”ÍÕÁÁ½ÉÑÌ…¸¥¹™•ÉÉ•Í¡…É•MLÉ½ÕÑ¥¹œ½¹•ÁÐ°¹½ÐÁÉ½½˜½˜•Ù•Éä™Õ¹Ñ¥½¹…°½µµ…¹½µ‰¥¹…Ñ¥½¸¸Q¡”™½±±½Ý¥¹œ™½ÕÈ™½ÉµÌ…É”•áÁ±¥¥Ñ±ä•¹Õµ•É…Ñ•‰äÑ¡”1¥¡Ñ¥¹œÍ½ÕÉ”ìÑ¡”ÕÑ½µ…Ñ¥½¸Í½ÕÉ”•ÍÑ…‰±¥Í¡•Ì½¹±äÑ¡”Á½¥¹Ð™½É´è()ðM½Á”ð1•Ù•°´Ð]!I€™½É´ð)ð€´´´ð€´´´ð)ð•¹•É…°ð€ÀŒÐ%9QI€ð)ðÉ•„ðŒÐ%9QI€ð)ðÉ½ÕÀð€HŒÐ%9QI€ð)ðA½¥¹ÐÑ¼Á½¥¹ÐðA0ŒÐ%9QI€ð((ŒŒŒŒŒ%¹Ñ•É™…”…‘‘É•ÍÌ½µÁ½¹•¹ÑÌ$Í€…¹$Ñ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€)…ÕÑ¥½¹Ìè…Ù½¥‘€°‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€°Í½ÕÉ•€()%9QI€¥Ì¹½Ðµ•É•±ä…¸¥¹Ñ••È™½Éµ…ÑÑ•…ÌÑÝ¼‘•¥µ…°‘¥¥ÑÌ¸%¸Ñ¡”ML½¹™¥ÕÉ…Ñ¥½¸µ½‘•°¥Ð¥Ì™½Éµ•™É½´Ñ¡”¥¹Ñ•É™…”½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹Ì$Í€…¹$Ñ€¸½ÈÑ¡”ÐÈÈML½ML¥¹Ñ•É™…”Ñ¡•Í”Á½Í¥Ñ¥½¹Ì¥‘•¹Ñ¥™äÑ¡”¥¹Ñ•É™…”Ý¥Ñ¡¥¸Ñ¡”¥¹ÍÑ…±±…Ñ¥½¸ì¥¸µ½‘•ÌÑ¡…ÐÕÍ”…¸½A0µ±¥­”¥¹Ñ•É™…”…‘‘É•ÍÌ°Ñ¡•ä…É”…ÍÍ¥¹•Ý¥Ñ Ñ¡”Í…µ”ÍÑÉÕÑÕÉ”…ÌÑ¡”¹½Éµ…°€…¹A1€Á½Í¥Ñ¥½¹Ìè()Ñ•áÐ)$ÌƒŠ& )$ÐƒŠ& A0)%9QI€ô$Í$Ð)€()Q¡”‘¥ÍÑ¥¹Ñ¥½¸¥Ì¡¥ÍÑ½É¥…°…¹ÍÑÉÕÑÕÉ…°è$Í€…¹$Ñ€…É”Í•Á…É…Ñ”ML½¹™¥ÕÉ…Ñ¥½¸Á½Í¥Ñ¥½¹Ì°¹½Ð„ÁÉ½Ñ½½°µ±•Ù•°ÍÁ±¥Ð½˜…¸…‰ÍÑÉ…Ð‘•¥µ…°¹Õµ‰•È¥¹Ñ¼Ñ•¹Ì…¹Õ¹¥ÑÌ¸()Q¡•¥È•á…ÐÉ½±”‘•Á•¹‘Ì½¸Ñ¡”½Á•É…Ñ¥¹œµ½‘”½˜Ñ¡”¥¹Ñ•É™…”¸%¸ÐÈÈÁ¡åÍ¥…°µ•áÁ…¹Í¥½¸µ½‘”€¡5=ôÅ€¤°$Í€…¹$Ñ€‘•™¥¹”Ñ¡”€¨©Í•Á…É…Ñ¥½¸…‘‘É•ÍÌ¨¨‰•ÑÝ••¸Ñ¡”ÑÝ¼½¹¹•Ñ•‰ÕÌÍ•Ñ¥½¹Ì¸½È•á…µÁ±”°$ÌôÌ°$ÐôÉ€•ÍÑ…‰±¥Í¡•ÌÍ•Á…É…Ñ¥½¸…‘‘É•ÍÌ€ÌÉ€èÕÑ½µ…Ñ¥½¸…‘‘É•ÍÍ•Ì‰•±½ÜÑ¡…Ð‰½Õ¹‘…Éä‰•±½¹œ½¸Ñ¡”±½Ý•Èµ…‘‘É•ÍÌÍ¥‘”…¹…‘‘É•ÍÍ•Ì…‰½Ù”¥Ð½¸Ñ¡”¡¥¡•Èµ…‘‘É•ÍÌÍ¥‘”¸%¸±½¥…°µ•áÁ…¹Í¥½¸µ½‘”€¡5=ôÉ€¤°Ñ¡”¥¹Ñ•É™…”…‘‘É•ÍÌ¥Ì……¥¸…ÍÍ¥¹•ÕÍ¥¹œÑ¡”½A0µ•Ñ¡½ì‘½Õµ•¹Ñ…Ñ¥½¸…±Í¼Á•Éµ¥ÑÌ$ÌôÀ°$ÐôÄ¸¸å€Ñ¼…Ù½¥½¹ÍÕµ¥¹œ…¸½É‘¥¹…Éä€ÄÄ¸¸äå€ÕÑ½µ…Ñ¥½¸…‘‘É•ÍÌ¸()½¹Í•ÅÕ•¹Ñ±ä°„Ý¥É”Ù…±Õ”ÍÕ …Ì€ŒÐŒÀÍ€Í¡½Õ±‰”ÁÉ•Í•ÉÙ•ÍÑÉÕÑÕÉ…±±ä…Ì¥¹Ñ•É™…”…‘‘É•ÍÌ$ÌôÀ°$ÐôÍ€°É…Ñ¡•ÈÑ¡…¸¹½Éµ…±¥é•Ñ¼¥¹Ñ••È€Í€¸1•…‘¥¹œé•É½•Ì…¸Ñ¡•É•™½É”…ÉÉä…‘‘É•ÍÌµ½µÁ½¹•¹Ð¥¹™½Éµ…Ñ¥½¸©ÕÍÐ…ÌÑ¡•ä‘¼¥¸•áÑ•¹‘•½A0…‘‘É•ÍÍ¥¹œ¸()Q¡¥Ì½¹™¥ÕÉ…Ñ½Èµ±•Ù•°•áÁ±…¹…Ñ¥½¸…¹Ñ¡”=Á•¹]•‰9•ÐÉ½ÕÑ¥¹œÍå¹Ñ…à‘•ÍÉ¥‰”‘¥™™•É•¹Ð±…å•ÉÌ½˜Ñ¡”Í…µ”½¹•ÁÐè$Í€½$Ñ€‘•™¥¹”Ñ¡”ML¥¹Ñ•É™…”…‘‘É•ÍÌ°Ý¡¥±”€ŒÐ%9QI€ÕÍ•ÌÑ¡…Ð…‘‘É•ÍÌÑ¼ÅÕ…±¥™ä„™Õ¹Ñ¥½¹…°Ñ…É•Ð…Ì‰•¥¹œ½¸Ñ¡”±½…°‰ÕÌÉ•…¡•Ñ¡É½Õ Ñ¡…Ð¥¹Ñ•É™…”¸()Q¡”ÁÕ‰±¥Œ]!<€Å€µ…Ñ•É¥…°•áÁ±¥¥Ñ±ä•¹Õµ•É…Ñ•Ì…±°™½ÕÈ™½ÉµÌ¸Q¡”ÁÕ‰±¥Œ]!<€É€‘½Õµ•¹ÐÍ¡½ÝÌÑ¡”Á½¥¹Ð™½É´A0ŒÐ¥¹Ñ•É™…•€¸•¹•É…°°É•„°…¹É½ÕÀ±½…°µ‰ÕÌ½µµ…¹‘ÌÕ¹‘•È]!<€É€É•µ…¥¸Õ¹•ÍÑ…‰±¥Í¡•‰äÑ¡•Í”Í½ÕÉ•Ìì‘¼¹½Ð•¹•É…Ñ”Ñ¡•´Í½±•±ä‰ä…¹…±½äÝ¥Ñ 1¥¡Ñ¥¹œ½ÈÑ¡”Í¡…É•µ…¹…•µ•¹ÐµÍåÍÑ•´É½Ü¸()Q¡”Í½ÕÉ”‘½Õµ•¹ÑÌ‘¥™™•È¥¸Ñ¡”É…¹”Ñ¡•äÍÑ…Ñ”™½ÈÑ¡”¥¹Ñ•É™…”™¥•±èÑ¡”1¥¡Ñ¥¹œ‘½Õµ•¹Ð¥Ù•Ì€ÀÄ¸¸Àå€…¹€ÄÄ¸¸ÄÕ€°Ý¡¥±”Ñ¡”ÕÑ½µ…Ñ¥½¸‘½Õµ•¹Ð•áÁÉ•ÍÍ•Ì¥Ð…ÌlÀ´ÅulÄ´åu€€¡€ÀÄ¸¸Àå€°€ÄÄ¸¸Äå€¤¸Q¡¥Ì¥Ì„Í½ÕÉ”µ±•Ù•°½¹ÍÑÉ…¥¹Ð‘¥ÍÉ•Á…¹äÝ¥Ñ¡¥¸Ñ¡”Í¡…É•½¹•ÁÐ¸%µÁ±•µ•¹Ñ…Ñ¥½¹ÌÍ¡½Õ±ÁÉ•Í•ÉÙ”Ñ¡…Ð‘¥ÍÉ•Á…¹äÕ¹Ñ¥°•Ù¥”½¥¹Ñ•É™…”•Ù¥‘•¹”•ÍÑ…‰±¥Í¡•ÌÝ¡•Ñ¡•ÈÑ¡”‰É½…‘•ÈÉ…¹”¥ÌÕ¹¥Ù•ÉÍ…±±äÙ…±¥¸()á…µÁ±•Ì¥¹±Õ‘”€ÄÌŒÐŒÀÍ€™½ÈÁ½¥¹ÐôÄ°A0ôÍ€Ñ¡É½Õ ¥¹Ñ•É™…”€ÀÍ€°…¹€ÀÌÄÄŒÐŒÄÉ€™½È•áÑ•¹‘•Á½¥¹ÐôÀÌ°A0ôÄÅ€Ñ¡É½Õ ¥¹Ñ•É™…”€ÄÉ€¸((ŒŒŒA…ÉÍ¥¹œÉÕ±•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÄÅ€()¸¥µÁ±•µ•¹Ñ…Ñ¥½¸Í¡½Õ±ÁÉ•Í•ÉÙ”Ñ¡”É…Ü]!I€ÍÑÉ¥¹œ…¹±…ÍÍ¥™ä¥ÐÕÍ¥¹œÑ¡”É…µµ…È™½ÈÑ¡”Í•±•Ñ•]!=€¸I•Í½±Ù”Ñ¡”™Õ¹Ñ¥½¹…°ÍåÍÑ•´™¥ÉÍÐ°É•½¹¥é”ÍÑÉÕÑÕÉ…°µ…É­•ÉÌÍÕ …Ì€€‰•™½É”¹Õµ•É¥Œ½¹Ù•ÉÍ¥½¸°ÁÉ•Í•ÉÙ”±•…‘¥¹œé•É½•Ì°Ù…±¥‘…Ñ”Ñ¡”½µÁ±•Ñ”Íå¹Ñ…Ñ¥Œ™½É´…¹¥ÑÌÉ…¹•Ì°…¹½¹±äÑ¡•¸•áÁ½Í”ÍÑÉÕÑÕÉ•½µÁ½¹•¹ÑÌÍÕ …Ì€°A1€°É½ÕÀ°½È¥¹Ñ•É™…”¸()Íå¹Ñ…Ñ¥…±±äÙ…±¥…‘‘É•ÍÌ¥Ì¹½Ð¹••ÍÍ…É¥±ä…ÁÁ±¥…‰±”Ñ¼•Ù•Éä•Ù¥”½È=‰©•Ð¸•Ù¥”…Á…‰¥±¥Ñ¥•Ì°=‰©•Ð™…µ¥±ä°ÍåÍÑ•´ÉÕ±•Ì°…¹½Á•É…Ñ¥½¸µÍÁ•¥™¥ŒÉ•ÍÑÉ¥Ñ¥½¹Ì…¸™ÕÉÑ¡•È½¹ÍÑÉ…¥¸Ý¡¥ …‘‘É•ÍÍ•Ì…É”µ•…¹¥¹™Õ°¸((ŒŒŒÉ½ÍÌµÍ½ÕÉ”¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÄÉ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡É•”Í½ÕÉ”±…å•ÉÌ½¹ÑÉ¥‰ÕÑ”‘¥™™•É•¹Ð­¥¹‘Ì½˜•Ù¥‘•¹”è()ðM½ÕÉ”ð]¡…Ð¥Ð•ÍÑ…‰±¥Í¡•Ìð)ð€´´´ð€´´´ð)ðAÕ‰±¥Í¡•=Á•¹]•‰9•Ð]!<€Å€ÍÁ•¥™¥…Ñ¥½¸ð1¥¡Ñ¥¹œ]!I€É…µµ…È°¥¹±Õ‘¥¹œ•¹•É…°½É•„½É½ÕÀ½Á½¥¹Ð±½…°µ‰ÕÌÙ…É¥…¹ÑÌ…¹Ñ¡”1¥¡Ñ¥¹œ¥¹Ñ•É™…”É…¹”ð)ðAÕ‰±¥Í¡•=Á•¹]•‰9•Ð]!<€É€ÍÁ•¥™¥…Ñ¥½¸ðÕÑ½µ…Ñ¥½¸•¹•É…°½É•„½É½ÕÀ½Á½¥¹ÐÉ…µµ…È…¹¥ÑÌÁ½¥¹Ð±½…°µ‰ÕÌ½¥¹Ñ•É™…”ÉÕ±”ð)ð5å!=5MÕ¥Ñ”=A8¹‘‰€ð‘‘É•ÍÌµÉÕ±”Ñ•µÁ±…Ñ•Ì…¹…ÁÁ±¥…‰¥±¥ÑäÕÍ•‰ä5å!=5MÕ¥Ñ”µ…¹…•µ•¹ÐÝ½É­™±½ÝÌð()Q¡”ÁÕ‰±¥Œ™Õ¹Ñ¥½¹…°ÍÁ•¥™¥…Ñ¥½¹Ì…É”…ÕÑ¡½É¥Ñ…Ñ¥Ù”™½È™Õ¹Ñ¥½¹…°]!<€Å€½]!<€É€Ý¥É”Íå¹Ñ…à¸=A8¹‘‰€¥Ì½µÁ±•µ•¹Ñ…Éä¥µÁ±•µ•¹Ñ…Ñ¥½¸•Ù¥‘•¹”è9}IMM}IU1€…¹M}MeMQ5}IMM}IU1€Í¡½ÜÑ¡…Ð5å!=5MÕ¥Ñ”Í•±•ÑÌ…‘‘É•ÍÌÉÕ±•Ì‰äÍåÍÑ•´…¹°™½ÈÍ½µ”ÉÕ±•Ì°‰ä=‰©•Ð½•Ù¥”™…µ¥±ä¸()½ÈÑ¡”½µ‰¥¹•1¥¡Ð½ÕÑ½µ…Ñ¥½¸ÍåÍÑ•´°=A8¹‘‰€É•½É‘Ì„•¹•É…°Ù¥ÉÑÕ…°™½É´mumA1u€Ý¥Ñ …‘Ù…¹•™½É´mumA1t­€°Á±ÕÌÐÈÈ±½¥Œ½Á¡åÍ¥…°µ•áÑ•¹Í¥½¸™½ÉµÌm$Íum$Ñu€…¹m$Íum$Ñt­€¸Q½•Ñ¡•ÈÝ¥Ñ Ñ¡”Í•Á…É…Ñ”±•Ù•±|É}ÉÕ±•€…¹±•Ù•±|Ñ}ÉÕ±•€™¥•±‘Ì°Ñ¡¥ÌÍÕÁÁ½ÉÑÌµ½‘•±¥¹œ…‘Ù…¹•…‘‘É•ÍÍ¥¹œ…ÌÅÕ…±¥™¥…Ñ¥½¸½É½ÕÑ¥¹œ±…å•É•½¹Ñ¼„‰…Í”…‘‘É•ÍÌ¸Q¡”€­€¹½Ñ…Ñ¥½¸‰•±½¹ÌÑ¼Ñ¡”‘…Ñ…‰…Í”Ì…‘‘É•ÍÌµÉÕ±”Ù½…‰Õ±…Éäì¥ÐÍ¡½Õ±¹½Ð‰”•µ¥ÑÑ•±¥Ñ•É…±±ä…ÌÁ…ÉÐ½˜…¸=Á•¹]•‰9•Ð]!I€°…¹¥Ð‘½•Ì¹½Ð‰ä¥ÑÍ•±˜•ÍÑ…‰±¥Í Ý¡¥ ÅÕ…±¥™¥•È½µ‰¥¹…Ñ¥½¹Ì…É”±•…°™½È„Á…ÉÑ¥Õ±…È™Õ¹Ñ¥½¹…°]!=€¸()Q¡”‘…Ñ…‰…Í”…±Í¼½¹Ñ…¥¹ÌÙ…±¥‘¥Ñå}ÉÕ±•€°½‰©•Ñ}‘•Ù¥•}™…µ¥±å€°±•Ù•±|É}ÉÕ±•€°±•Ù•±|Ñ}ÉÕ±•€°…¹½™™Í•Ñ}…‘Ù€¸Q¡•Í”™¥•±‘Ì…É”•Ù¥‘•¹”Ñ¡…ÐÍå¹Ñ…Ñ¥ŒÉ…¹”Ù…±¥‘…Ñ¥½¸…±½¹”¥Ì¥¹ÍÕ™™¥¥•¹Ð™½È•Ù•Éäµ…¹…•=‰©•Ð¸]¡•É”…¸…‘‘É•ÍÌÉÕ±”¥Ì™…µ¥±äµÅÕ…±¥™¥•°¥ÑÌ½‰©•Ñ}‘•Ù¥•}™…µ¥±å€½ÉÉ•±…Ñ•ÌÝ¥Ñ Ñ¡”…Ñ…±½Õ”=‰©•Ðµ™…µ¥±äµ½‘•°ì…ÁÁ±¥…‰¥±¥ÑäÍ¡½Õ±‰”É•Í½±Ù•‰•™½É”•¹½‘¥¹œ„•Ù¥”µÍÁ•¥™¥Œµ…¹…•µ•¹Ð…‘‘É•ÍÌ¸((ŒŒŒ=Ñ¡•È]!<™…µ¥±¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÐéÌÀÀÀÀÄÍ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€()Q¡”€½A1€É…µµ…È…‰½Ù”µÕÍÐ¹½Ð‰”ÑÉ•…Ñ•…Ì„±½‰…°=Á•¹]•‰9•Ð…‘‘É•ÍÌÉ…µµ…È¸5å!=5MÕ¥Ñ”¥ÑÍ•±˜É•½É‘Ì‘¥™™•É•¹Ð…‘‘É•ÍÌµÉÕ±”ÍÑÉÕÑÕÉ•Ì™½È½Ñ¡•Èµ…¹…•™…µ¥±¥•Ì°¥¹±Õ‘¥¹œQ¡•Éµ½É•Õ±…Ñ¥½¸°Y¥‘•¼½½È¹ÑÉä°¹•Éä5…¹…•µ•¹Ð°•ÍÌ½¹ÑÉ½°°…¹¥¹Ñ•É™…”ÍåÍÑ•µÌ¸()Q¡•¥È…¹½¹¥…°™Õ¹Ñ¥½¹…°]!I€Íå¹Ñ…à‰•±½¹Ì¥¸Ñ¡”É•±•Ù…¹Ð]!=€‘½Õµ•¹Ñ…Ñ¥½¸¸Q¡”½µµ½¸ÉÕ±”¥Ì½¹±äÑ¡…Ð]!I€¥ÌÁ…ÉÍ•¥¸Ñ¡”½¹Ñ•áÐ½˜]!=€°¹½ÐÑ¡…Ð…±°ÍåÍÑ•µÌÍ¡…É”„½µµ½¸¹Õµ•É¥Œ…‘‘É•ÍÌÍÁ…”¸()M•”Ñ¡”É•±•Ù…¹Ð™Õ¹Ñ¥½¹…°]!=€…‘‘É•ÍÍ¥¹œÁ…”™½ÈÍåÍÑ•´µÍÁ•¥™¥Œ…ÁÁ±¥…‰¥±¥Ñä°mÉ…µ”Må¹Ñ…át¡™É…µ”µÍå¹Ñ…à¹µ¤™½ÈÑ¡”Á½Í¥Ñ¥½¸½˜]!I€¥¸=Á•¹]•‰9•Ð™É…µ•Ì°…¹m5å!=5MÕ¥Ñ”=A8¹‘ˆ½Ù•É…•t ¸¸½™Õ¹Ñ¥½¹…°½½Á•¸µ‘ˆµ½Ù•É…”¹µ¤™½ÈÑ¡”¥µÁ±•µ•¹Ñ…Ñ¥½¸…‘‘É•ÍÌµÉÕ±”¥¹Ù•¹Ñ½Éä¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀÔ()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½…ÕÑ¡•¹Ñ¥…Ñ¥½¸¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒÕÑ¡•¹Ñ¥…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÔéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€()=Á•¹]•‰9•Ð…ÕÑ¡•¹Ñ¥…Ñ¥½¸½ÕÉÌ…™Ñ•ÈÑ¡”±¥•¹ÐÍ•±•ÑÌ„½¹¹•Ñ¥½¸Í•ÍÍ¥½¸…¹‰•™½É”¹½Éµ…°Í•ÍÍ¥½¸ÑÉ…™™¥Œ¥Ì…•ÁÑ•¸%Ð…ÕÑ¡•¹Ñ¥…Ñ•ÌÑ¡”±¥•¹ÐÑ¼Ñ¡”=Á•¹]•‰9•ÐÍ•ÉÙ•Èì¥Ð‘½•Ì€¨©¹½Ð¨¨•¹ÉåÁÐ½È¥¹Ñ•É¥ÑäµÁÉ½Ñ•ÐÍÕ‰Í•ÅÕ•¹Ð™Õ¹Ñ¥½¹…°ÑÉ…™™¥Œ¸()…Ñ•Ý…ä…¸…±Í¼…±±½Ü½¹™¥ÕÉ•±¥•¹Ð%@…‘‘É•ÍÍ•ÌÑ¼½¹¹•ÐÝ¥Ñ¡½ÕÐ…¸=A8Á…ÍÍÝ½É¸±¥•¹ÐµÕÍÐ™½±±½ÜÑ¡”Í•ÉÙ•ÈÌÉ•ÍÁ½¹Í”É…Ñ¡•ÈÑ¡…¸…ÍÍÕµ”Ñ¡…Ð•Ù•Éä½¹¹•Ñ¥½¸•¹Ñ•ÉÌ„¡…±±•¹”¸((ŒŒŒÕÑ¡•¹Ñ¥…Ñ¥½¸Í•±•Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÔéÌÀÀÀÀÀÉ€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”!5ÍÁ•¥™¥…Ñ¥½¸…‘‘Ì…¸½ÁÑ¥½¹…°…±½É¥Ñ¡´µ‘•±…É…Ñ¥½¸™É…µ”Í•¹Ð‰äÑ¡”Í•ÉÙ•È…™Ñ•ÈÍ•ÍÍ¥½¸Í•±•Ñ¥½¸è()ðM•ÉÙ•È™É…µ”ðÕÑ¡•¹Ñ¥…Ñ¥½¸µ•Ñ¡½ð)ð€´´´ð€´´´ð)ð9¼€¨äà©dŒ€‘•±…É…Ñ¥½¸ì±•…ä¡…±±•¹”™½±±½ÝÌð1•…ä=A8Á…ÍÍÝ½É…±½É¥Ñ¡´ð)ð€¨äà¨ÄŒ€ð!5ÕÍ¥¹œM!´Äð)ð€¨äà¨ÈŒ€ð!5ÕÍ¥¹œM!´ÈÔØð()±¥•¹ÐÑ¡…ÐÍÕÁÁ½ÉÑÌÑ¡”‘•±…É•µ•Ñ¡½…¹ÍÝ•ÉÌÝ¥Ñ -€¸%˜¥Ð…¹ÍÝ•ÉÌ9-€°Ñ¡”Í•ÉÙ•È±½Í•ÌÑ¡”½¹¹•Ñ¥½¸¸%˜Ñ¡”±¥•¹ÐÌ…‘‘É•ÍÌ¥Ì¥¸Ñ¡”½¹™¥ÕÉ•½Á•¸É…¹”°…ÕÑ¡•¹Ñ¥…Ñ¥½¸…¸‰”Í­¥ÁÁ••Ù•¸Ý¡•¸!5ÍÕÁÁ½ÉÐ•á¥ÍÑÌ¸()]!<€äá€¡•É”¥Ì„½¹¹•Ñ¥½¸µ¹•½Ñ¥…Ñ¥½¸¹…µ•ÍÁ…”°¹½Ð…¸½É‘¥¹…Éä™Õ¹Ñ¥½¹…°ÍåÍÑ•´¸((ŒŒŒ1•…ä=A8…ÕÑ¡•¹Ñ¥…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÔéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”¥¹ÑÉ½‘ÕÑ½ÉäÍÁ•¥™¥…Ñ¥½¸•ÍÑ…‰±¥Í¡•ÌÑ¡…ÐÁ…ÍÍÝ½ÉµÁÉ½Ñ•Ñ•Í•ÍÍ¥½¹Ì…¸ÕÍ”Ñ¡”½±‘•È=A8¡…±±•¹”µÉ•ÍÁ½¹Í”…±½É¥Ñ¡´¸%¸Ñ¡¥Ìµ½‘”Ñ¡”Í•ÉÙ•ÈÍ•¹‘Ì…¸½Á•É…Ñ¥½¹Ì½¡…±±•¹”™É…µ”É…Ñ¡•ÈÑ¡…¸…¸!5‘•±…É…Ñ¥½¸°…¹Ñ¡”±¥•¹Ð½µÁÕÑ•ÌÑ¡”±•…äÁ…ÍÍÝ½ÉÉ•ÍÁ½¹Í”¸()Q¡”‘•Ñ…¥±•ÑÉ…¹Í™½Éµ…Ñ¥½¸¥Ì¡¥ÍÑ½É¥…±±ä‘½Õµ•¹Ñ•½ÕÑÍ¥‘”Ñ¡”…¹½¹¥…°™¥±•ÌÕÉÉ•¹Ñ±äÁÉ•Í•ÉÙ•¥¸Ñ¡¥ÌÉ•Á½Í¥Ñ½Éä¸Q¡¥ÌÉ•™•É•¹”Ñ¡•É•™½É”É•½É‘ÌÑ¡”¹•½Ñ¥…Ñ¥½¸‰½Õ¹‘…ÉäÝ¥Ñ¡½ÕÐÉ•ÁÉ½‘Õ¥¹œ…¸Õ¹Ù•É¥™¥•¥µÁ±•µ•¹Ñ…Ñ¥½¸™É½´„Ñ¡¥ÉµÁ…ÉÑä±¥‰É…Éä¸()¸¥µÁ±•µ•¹Ñ…Ñ¥½¸Í¡½Õ±­••ÀÑ¡”±•…ä…±½É¥Ñ¡´‰•¡¥¹„‘•‘¥…Ñ•½µÁ…Ñ¥‰¥±¥Ñä¥¹Ñ•É™…”…¹Ñ•ÍÐ¥Ð……¥¹ÍÐ„É•…°…Ñ•Ý…ä¸%ÐµÕÍÐ¹½Ð±½œÑ¡”¡…±±•¹”°Á…ÍÍÝ½É°½È½µÁÕÑ•É•ÍÁ½¹Í”…Ð¹½Éµ…°Ù•É‰½Í¥Ñä¸((ŒŒŒ!5M¥µÁ±”ÕÑ¡•¹Ñ¥…Ñ¥½¸5½‘”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÔéÌÀÀÀÀÀÑ€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”…¹½¹¥…°!5ÍÁ•¥™¥…Ñ¥½¸‘•™¥¹•Ì±¥•¹Ð…ÕÑ¡•¹Ñ¥…Ñ¥½¸ÕÍ¥¹œ„ÁÉ”µÍ¡…É•­•ä‘•É¥Ù•™É½´Ñ¡”=A8Á…ÍÍÝ½É¸()ðMåµ‰½°ð5•…¹¥¹œð)ð€´´´ð€´´´ð)ðI…€ðM•ÉÙ•Èµ•¹•É…Ñ•É…¹‘½´Ù…±Õ”ð)ðI‰€ð±¥•¹Ðµ•¹•É…Ñ•É…¹‘½´Ù…±Õ”ð)ð-…‰€ðA…ÍÍÝ½Éµ‘•É¥Ù•ÁÉ”µÍ¡…É•­•äð)ð€ð±¥•¹Ð¥‘•¹Ñ¥ÑäÍÑÉ¥¹œ‘•™¥¹•‰äÑ¡”ÍÁ•¥™¥…Ñ¥½¸ð)ð	€ðM•ÉÙ•È¥‘•¹Ñ¥ÑäÍÑÉ¥¹œ‘•™¥¹•‰äÑ¡”ÍÁ•¥™¥…Ñ¥½¸ð()½ÈM!´Ä°Ñ¡”É…¹‘½´Ù…±Õ•Ì°­•ä°…¹‘¥•ÍÑÌ…É”€ÄØÀ‰¥ÑÌ¸½ÈM!´ÈÔØ°Ñ¡•ä…É”€ÈÔØ‰¥ÑÌ¸-…‰€¥ÌÑ¡”M!‘¥•ÍÐ½˜Ñ¡”=A8Á…ÍÍÝ½ÉÕÍ¥¹œÑ¡”¹•½Ñ¥…Ñ•‘¥•ÍÐ™…µ¥±ä¸()Q¡”•á¡…¹”¡…ÌÑ¡É•”ÉåÁÑ½É…Á¡¥ŒÍÑ•ÁÌè((Ä¸Q¡”Í•ÉÙ•ÈÍ•¹‘ÌI…€¸(È¸Q¡”±¥•¹Ð•¹•É…Ñ•ÌI‰€…¹É•ÑÕÉ¹ÌI‰€Ý¥Ñ Ñ¡”±¥•¹ÐÁÉ½½˜½Ù•ÈI…€°I‰€°Ñ¡”ÑÝ¼É½±”¥‘•¹Ñ¥Ñ¥•Ì°…¹-…‰€¸(Ì¸Q¡”Í•ÉÙ•ÈÉ•ÑÕÉ¹Ì¥ÑÌ½¹™¥Éµ…Ñ¥½¸½Ù•ÈI…€°I‰€°…¹-…‰€¸()Q¡”±¥•¹ÐµÕÍÐÙ•É¥™äÑ¡”Í•ÉÙ•È½¹™¥Éµ…Ñ¥½¸…¹Ñ¡•¸Í•¹€¨Œ¨ÄŒ€Ñ¼™¥¹¥Í Ñ¡”ÁÕ‰±¥Í¡•¡…¹‘Í¡…­”¸Í•ÉÙ•È½¹™¥Éµ…Ñ¥½¸¥Ì¹½Ð¥ÑÍ•±˜Á•Éµ¥ÍÍ¥½¸Ñ¼Í­¥ÀÑ¡¥Ì™¥¹…°±¥•¹Ð…­¹½Ý±•‘•µ•¹Ð¸%˜…ÕÑ¡•¹Ñ¥…Ñ¥½¸™…¥±Ì°Ñ¡”½¹¹•Ñ¥½¸¥Ì±½Í•¸Q¡”ÍÁ•¥™¥…Ñ¥½¸…±±Ì™½È„€ØÀµÍ•½¹…ÕÑ¡•¹Ñ¥…Ñ¥½¸ÍÕÍÁ•¹Í¥½¸…™Ñ•ÈÑ¡É•”™…¥±•¡…¹‘Í¡…­•ÌÝ¥Ñ¡¥¸€ØÀÍ•½¹‘Ì¸((ŒŒŒ]¥É”•¹½‘¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÔéÌÀÀÀÀÀÕ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()Q¡”!5‘½Õµ•¹ÐÕÍ•Ì‘•¥µ…°¡…É…Ñ•ÉÌ™½È‰¥¹…ÉäÙ…±Õ•Ì‰•…ÕÍ”½É‘¥¹…Éä=Á•¹]•‰9•ÐÑ…Ì‘¼¹½Ð½¹Ñ…¥¸¡•á…‘•¥µ…°±•ÑÑ•ÉÌ¸… ‰¥¹…Éä‰åÑ”¥ÌÍÁ±¥Ð¥¹Ñ¼ÑÝ¼¡•á…‘•¥µ…°¹¥‰‰±•Ì°…¹•… ¹¥‰‰±”¥Ì•¹½‘•…Ì„ÑÝ¼µ‘¥¥Ð‘•¥µ…°¹Õµ‰•È¥¸€ÀÀ¸¸ÄÕ€¸()ð	åÑ”ð9¥‰‰±•Ìð=Á•¹]•‰9•ÐÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸ð)ð€´´´ð€´´´ð€´´´ð)ð€ÁàÀÅ€ð€Á€°€Å€ð€ÀÀÀÅ€ð)ð€ÁàÁ€ð€Á€°€ð€ÀÀÄÁ€ð)ð€Áá€ð€°€ð€ÄÔÄÕ€ð()€ÈÀµ‰åÑ”M!´ÄÙ…±Õ”Ñ¡•É•™½É”½ÕÁ¥•Ì€àÀ‘•¥µ…°¡…É…Ñ•ÉÌ½¸Ñ¡”Ý¥É”ì„€ÌÈµ‰åÑ”M!´ÈÔØÙ…±Õ”½ÕÁ¥•Ì€ÄÈà¸()Q¡¥ÌÑÉ…¹ÍÁ½ÉÐÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸¥Ì¹½ÐÑ¡”¥¹ÁÕÐÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸ÕÍ•‰äÑ¡”¡…Í …±Õ±…Ñ¥½¸¸%µÁ±•µ•¹Ñ…Ñ¥½¹ÌÍ¡½Õ±­••À™Õ¹Ñ¥½¹Ì™½È‰¥¹…ÉäÙ…±Õ•Ì°¡…Í µ¥¹ÁÕÐÍ•É¥…±¥é…Ñ¥½¸°…¹=Á•¹]•‰9•ÐÝ¥É”•¹½‘¥¹œÍ•Á…É…Ñ”¸((ŒŒŒAÉ½½˜…±Õ±…Ñ¥½¸…¹Í½ÕÉ”‘¥ÍÉ•Á…¹ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÔéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡”‘½Õµ•¹Ð…±±ÌÑ¡¥ÌÍ¡•µ”!5°‰ÕÐ‘•ÍÉ¥‰•Ì¥ÑÌÁÉ½½˜½Á•É…Ñ¥½¸…ÌM!´Ä½ÈM!´ÈÔØ½Ù•È½¹…Ñ•¹…Ñ•™¥•±‘Ì¸%Ð‘½•Ì¹½Ð‘•ÍÉ¥‰”Ñ¡”ÍÑ…¹‘…É­•å•!5¥¹¹•È½½ÕÑ•ÈµÁ…½¹ÍÑÉÕÑ¥½¸¸MÕ‰ÍÑ¥ÑÕÑ¥¹œ„±¥‰É…ÉäÌ•¹•É¥Œ!5¡­•ä°µ•ÍÍ…”¥€½Á•É…Ñ¥½¸¥ÌÑ¡•É•™½É”¹½Ð©ÕÍÑ¥™¥•‰äÑ¡”ÁÉ½Ñ½½°¹…µ”¸()½ÈÑ¡”¹•½Ñ¥…Ñ•¡…Í !€°Ñ¡”ÁÕ‰±¥Í¡•±…å½ÕÐ¥Ìè()Ñ•áÐ)-…ˆ€ô ¡=A9}AMM]=I¤)±¥•¹Ñ}ÁÉ½½˜€ô ¡¡•à¡I„¤ñð¡•à¡Iˆ¤ñðñðñð¡•à¡-…ˆ¤¤)Í•ÉÙ•É}ÁÉ½½˜€ô ¡¡•à¡I„¤ñð¡•à¡Iˆ¤ñð¡•à¡-…ˆ¤¤)€()!•É”¡•á€µ•…¹Ì±½Ý•É…Í”¡•á…‘•¥µ…°Ñ•áÐÝ¥Ñ ÑÝ¼¡…É…Ñ•ÉÌÁ•È‰åÑ”ìññ€µ•…¹Ì½¹…Ñ•¹…Ñ¥½¸Ý¥Ñ¡½ÕÐÍ•Á…É…Ñ½ÉÌ¸Q¡¥Ì¥ÌÑ¡”¡…Í µ¥¹ÁÕÐÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸°¹½ÐÑ¡”‘•¥µ…°µ¹¥‰‰±”ÑÉ…¹ÍÁ½ÉÐÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸¸Q¡”Á…ÍÍÝ½É¥ÌÑ¡”Á•Éµ¥ÑÑ•…±Á¡…¹Õµ•É¥Œ¡…É…Ñ•ÈÍÑÉ¥¹œ¸()Q¡”¥‘•¹Ñ¥Ñä½¹ÍÑ…¹ÑÌ¹••ÍÁ•¥…°…É”¸Q¡”Í½ÕÉ”Á…¥ÉÌÑ¡”±¥•¹Ð±…‰•°½Á•¹€Ý¥Ñ €ÜÌÙÜÀØÔÍ€…¹Ñ¡”Í•ÉÙ•È±…‰•°Í½Á•¹€Ý¥Ñ €ØÌÙÜÀØÔÍ€¸Q¡½Í”¡•àÍÑÉ¥¹Ì‘•½‘”Ñ¼Í½Á”ù€…¹½Á”ù€°É•ÍÁ•Ñ¥Ù•±ä°…¹‘¼¹½Ðµ…Ñ Ñ¡”…½µÁ…¹å¥¹œ±…‰•±Ì¸Q¡¥ÌÉ•™•É•¹”ÁÉ•Í•ÉÙ•ÌÑ¡…Ð‘¥ÍÉ•Á…¹äÉ…Ñ¡•ÈÑ¡…¸¥¹Ù•¹Ñ¥¹œ½ÉÉ•Ñ•½¹ÍÑ…¹ÑÌ¸%¹Ñ•É½Á•É…‰±”¥µÁ±•µ•¹Ñ…Ñ¥½¹Ì¹••…¸¥¹‘•Á•¹‘•¹Ñ±äÙ•É¥™¥•…Ñ•Ý…äÑÉ…¹ÍÉ¥ÁÐ½È¥µÁ±•µ•¹Ñ…Ñ¥½¸Í½ÕÉ”Ñ¼É•Í½±Ù”¥Ð¸()Q¡”ÁÕ‰±¥Í¡••á¡…¹”°Ý¥Ñ ÑÉ…¹ÍÁ½ÉÐµ•¹½‘•‰¥¹…ÉäÙ…±Õ•Ì°¥Ìè()ð¥É•Ñ¥½¸ðÉ…µ”ð)ð€´´´ð€´´´ð)ðM•ÉÙ•ÈƒŠH±¥•¹Ðð€¨I„Œ€ð)ð±¥•¹ÐƒŠHÍ•ÉÙ•Èð€¨Iˆ©1%9Q}AI==Œ€ð)ðM•ÉÙ•ÈƒŠH±¥•¹Ðð€¨MIYI}AI==Œ€ð)ð±¥•¹ÐƒŠHÍ•ÉÙ•È°…™Ñ•ÈÙ•É¥™¥…Ñ¥½¸ð€¨Œ¨ÄŒ€ð()M•”Ñ¡”…ÕÑ¡•¹Ñ¥…Ñ¥½¸ÍÁ•¥™¥…Ñ¥½¸ÌÁÉ¥¹Ñ•Á…•Ì€ËŠLÌ…¹€ßŠLà™½ÈÑ¡”ÁÉ½½˜±…å½ÕÐ…¹Í•É¥…±¥é…Ñ¥½¸¸Q¡”Õ¹É•Í½±Ù•¥‘•¹Ñ¥Ñäµ½¹ÍÑ…¹Ð‘¥ÍÉ•Á…¹äÁÉ•Ù•¹ÑÌÑÉ•…Ñ¥¹œÑ¡¥ÌÁ…”…Ì„½µÁ±•Ñ”°¥¹‘•Á•¹‘•¹Ñ±äÙ•É¥™¥•¥µÁ±•µ•¹Ñ…Ñ¥½¸É•¥Á”¸((ŒŒŒA…ÍÍÝ½É½¹ÍÑÉ…¥¹ÑÌ…¹Í•ÕÉ¥Ñä‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÔéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÑÁ€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”!5ÍÁ•¥™¥…Ñ¥½¸Á•Éµ¥ÑÌ…¸=A8Á…ÍÍÝ½É½˜ÕÀÑ¼€ÌÀ…±Á¡…¹Õµ•É¥Œ¡…É…Ñ•ÉÌ…¹±•…Ù•Ìµ¥¹¥µÕ´µ±•¹Ñ Á½±¥äÑ¼…ÁÁ±¥…Ñ¥½¹Ì¸()9•¥Ñ¡•È±•…ä¹½È!5…ÕÑ¡•¹Ñ¥…Ñ¥½¸µ…­•ÌÑ¡”±…Ñ•È½¹¹•Ñ¥½¸½¹™¥‘•¹Ñ¥…°¸•Á±½åµ•¹ÑÌÍ¡½Õ±¹½Ð•áÁ½Í”Q@Á½ÉÐ€ÈÀÀÀÁ€Ñ¼Õ¹ÑÉÕÍÑ•¹•ÑÝ½É­Ì…¹Í¡½Õ±ÕÍ”…¸•áÑ•É¹…°ÁÉ½Ñ•Ñ•ÑÉ…¹ÍÁ½ÉÐ½ÈÑÉÕÍÑ•¹•ÑÝ½É¬‰½Õ¹‘…ÉäÝ¡•É”½¹™¥‘•¹Ñ¥…±¥Ñä…¹¥¹Ñ•É¥Ñä…É”É•ÅÕ¥É•¸()¼¹½ÐÁ±…”Á…ÍÍÝ½É‘Ì°‘•É¥Ù•­•åÌ°¹½¹•Ì°ÁÉ½½™Ì°½È½µÁ±•Ñ”…ÕÑ¡•¹Ñ¥…Ñ¥½¸™É…µ•Ì¥¸±½Ì¸((ŒŒŒ%µÁ±•µ•¹Ñ…Ñ¥½¸¡•­±¥ÍÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÔéÌÀÀÀÀÀá€((´]…¥Ð™½ÈÑ¡”¥¹¥Ñ¥…°Í•ÉÙ•È-€¸(´M•±•ÐÑ¡”É•ÅÕ¥É•Í•ÍÍ¥½¸¸(´	É…¹ ½¸½Á•¸µÉ…¹”…•ÁÑ…¹”°…¸!5‘•±…É…Ñ¥½¸°½È„±•…ä¡…±±•¹”¸(´I•©•ÐÕ¹ÍÕÁÁ½ÉÑ•‘•±…É…Ñ¥½¹Ì¥¹ÍÑ•…½˜Í¥±•¹Ñ±ä¡…¹¥¹œÑ¡”‘¥•ÍÐ¸(´•¹•É…Ñ”I‰€Ý¥Ñ „ÉåÁÑ½É…Á¡¥…±±äÍ•ÕÉ”É…¹‘½´•¹•É…Ñ½È¸(´½µÁ…É”ÁÉ½½™ÌÝ¥Ñ¡½ÕÐÑ¥µ¥¹œµ‘•Á•¹‘•¹Ð•…É±ä•á¥ÐÝ¡•É”ÁÉ…Ñ¥…°¸(´	•¥¸™Õ¹Ñ¥½¹…°Á…ÉÍ¥¹œ½¹±ä…™Ñ•È…ÕÑ¡•¹Ñ¥…Ñ¥½¸ÍÕ••‘Ì¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÔéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÙ•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”!5…±½É¥Ñ¡´°‘•±…É…Ñ¥½¸™É…µ•Ì°Ù…±Õ”•¹½‘¥¹œ°Á…ÍÍÝ½É™½Éµ…Ð°…¹™…¥±ÕÉ”‰•¡…Ù¥½È½µ”™É½´m!µ…ŒÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½!µ…Œ¹Á‘˜¤°Ù•ÉÍ¥½¸€Ä¸Ä¸Q¡”½¹¹•Ñ¥½¸Á½Í¥Ñ¥½¸…¹½Á•¸µÉ…¹”•á•ÁÑ¥½¸…É”½ÉÉ½‰½É…Ñ•‰äm=Á•¹]•‰9•Ð%¹ÑÉ½‘ÕÑ¥½¸ÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=]9}%¹ÑÉ½}9¹Á‘˜¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀØ()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½‘¥µ•¹Í¥½¹Ì¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒ%59M%=9€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÀÅ€()%59M%=9€¥‘•¹Ñ¥™¥•Ì„ÁÉ½Á•ÉÑä°ÅÕ•Éä°½ÈÍÑÉÕÑÕÉ•½Á•É…Ñ¥½¸Ý¥Ñ¡¥¸…¸=Á•¹]•‰9•Ð]!=€¸%Ð…¸‰”É•ÅÕ•ÍÑ•°É•Á½ÉÑ•…Íå¹¡É½¹½ÕÍ±ä°É•ÑÕÉ¹•¥¸„É•ÍÁ½¹Í”°½ÈµÝ¡•É”•áÁ±¥¥Ñ±äÍÕÁÁ½ÉÑ•µÝÉ¥ÑÑ•¸¸()Q¡”½µÁ±•Ñ”¥‘•¹Ñ¥Ñä¥Ì¹½Ð…±Ý…åÌ©ÕÍÐ€¡]!<°%59M%=8¥€¸%59M%=9€Í•±•Ñ½È…¸½¹Ñ…¥¸€€µÍ•Á…É…Ñ•Á…É…µ•Ñ•ÉÌè()Ñ•áÐ)%59M%=8AI5QHAI5QH)€()Q¡•Í”Á…É…µ•Ñ•ÉÌÍ•±•Ð„Á…ÉÑ¥Õ±…È¥¹ÍÑ…¹”°ÍÕˆµÁÉ½Á•ÉÑä°Í±½Ñ€°ÁÉ¥½É¥Ñä½¹Ñ•áÐ°½È½Á•É…Ñ¥½¸Ù…É¥…¹Ð¸Q¡”€©€µÍ•Á…É…Ñ•™¥•±‘Ì™½±±½Ý¥¹œÑ¡”Í•±•Ñ½È…É”Ñ¡”½É‘•É•Á…å±½…Ù…±Õ•Ìè()Ñ•áÐ)%59M%=8AI5QHAI5QH©Y1U©Y1U)€()%µÁ±•µ•¹Ñ…Ñ¥½¹ÌµÕÍÐÁÉ•Í•ÉÙ”Ñ¡¥Ì‰½Õ¹‘…Éä¸M•±•Ñ½ÈÁ…É…µ•Ñ•ÉÌ…¹Á…å±½…Ù…±Õ•Ì…É”¹½Ð¥¹Ñ•É¡…¹•…‰±”¸((ŒŒŒ•¹•É…°™É…µ”™½ÉµÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÀÉ€()ð=Á•É…Ñ¥½¸ð±…ÐÍ•±•Ñ½ÈðA…É…µ•Ñ•É¥é•Í•±•Ñ½Èð)ð€´´´ð€´´´ð€´´´ð)ðI•ÅÕ•ÍÐð€¨]!<©]!I©%59M%=8Œ€ð€¨]!<©]!I©%59M%=8@Ä@ÈŒ€ð)ðI•ÍÁ½¹Í”½É•Á½ÉÐð€¨]!<©]!I©%59M%=8©XÄ©XÈŒ€ð€¨]!<©]!I©%59M%=8@Ä@È©XÄ©XÈŒ€ð)ð]É¥Ñ”ð€¨]!<©]!I¨%59M%=8©XÄ©XÈŒ€ð€¨]!<©]!I¨%59M%=8@Ä@È©XÄ©XÈŒ€ð()@Å€°@É€°XÅ€°…¹XÉ€…É”¹½Ñ…Ñ¥½¸°¹½Ð±¥Ñ•É…°Ý¥É”Ù…±Õ•Ì¸Á…ÉÑ¥Õ±…È%59M%=9€…¸‘•™¥¹”é•É¼°½¹”°½ÈÍ•Ù•É…°Í•±•Ñ½ÈÁ…É…µ•Ñ•ÉÌ…¹é•É¼°½¹”°½ÈÍ•Ù•É…°Á…å±½…Ù…±Õ•Ì¸()Q¡”…ÑÕ…°…É¥Ñä…¹µ•…¹¥¹œ…É”‘•™¥¹•‰äÑ¡”Í•±•Ñ•]!=€…¹%59M%=9€¸Q¡”Ñ…‰±”‘•ÍÉ¥‰•ÌÑ¡”É•ÕÍ…‰±”ÍÑÉÕÑÕÉ…°Á…ÑÑ•É¸°¹½ÐÁ•Éµ¥ÍÍ¥½¸Ñ¼…ÁÁ•¹…É‰¥ÑÉ…ÉäÁ…É…µ•Ñ•ÉÌ¸((ŒŒŒQ¡É•”‘¥™™•É•¹ÐÕÍ•Ì½˜€€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÀÍ€()Q¡”Í…µ”¡…É…Ñ•ÈÁ…ÉÑ¥¥Á…Ñ•Ì¥¸Í•Ù•É…°±…å•ÉÌè()ðA½Í¥Ñ¥½¸ðá…µÁ±”ð5•…¹¥¹œð)ð€´´´ð€´´´ð€´´´ð)ð	•™½É”]!=€ð€¨]!<¸¸¹€ðM•±•ÑÌÑ¡”É•ÅÕ•ÍÐ½%59M%=9€™É…µ”™…µ¥±äð)ð	•™½É”„ÝÉ¥Ñ…‰±”Í•±•Ñ½Èð€¨]!<©]!I¨%59M%=8¸¸¹€ð5…É­Ì„%59M%=9€ÝÉ¥Ñ”ð)ð%¹Í¥‘”Ñ¡”Í•±•Ñ½Èð%59M%=8@Ä@É€ðM•Á…É…Ñ•ÌÁ…É…µ•Ñ•ÉÌ‰•±½¹¥¹œÑ¼Ñ¡…ÐÍ•±•Ñ½Èð()Q¡”±•…‘¥¹œÝÉ¥Ñ”µ…É­•È…¹Í•±•Ñ½ÈÁ…É…µ•Ñ•ÉÌ…¸½ÕÈÑ½•Ñ¡•Èè()Ñ•áÐ(%59M%=8@Ä@È)€()Q¡¥Ì¥Ì½¹”µ…©½È€©€µ‘•±¥µ¥Ñ•™¥•±¸%Ð¥Ì¹½Ð„Í•É¥•Ì½˜¥¹‘•Á•¹‘•¹Ð™É…µ”™¥•±‘Ì¸((ŒŒŒM•±•Ñ½ÈÁ…É…µ•Ñ•ÉÌÙ•ÉÍÕÌÁ…å±½…Ù…±Õ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÀÑ€()½¹Í¥‘•ÈÑ¡”…‰ÍÑÉ…ÐÉ•ÍÁ½¹Í”è()Ñ•áÐ(¨]!<©]!I¨ÌÈŒÜ©MeMQ4©IMLŒŒ)€()!•É”è((´€ÌÉ€¥ÌÑ¡”%59M%=9€¥‘•¹Ñ¥™¥•Èì(´€Ý€¥Ì„Í•±•Ñ½ÈÁ…É…µ•Ñ•È°™½È•á…µÁ±”„Í±½Ñ€ì(´MeMQ5€…¹IMM€…É”Á…å±½…Ù…±Õ•Ì¸()Q¡”•ÅÕ¥Ù…±•¹ÐÍÑÉÕÑÕÉ•É•ÁÉ•Í•¹Ñ…Ñ¥½¸¥Ìè()Ñ•áÐ)Í•±•Ñ½È€ôì(€‘¥µ•¹Í¥½¸è€ˆÌÈˆ°(€Á…É…µ•Ñ•ÉÌèlˆÜ‰t)ô)Ù…±Õ•Ì€ôl‰MeMQ4ˆ°€‰IML‰t)€()%ÐÝ½Õ±‰”¥¹½ÉÉ•ÐÑ¼Á…ÉÍ”Ñ¡”™¥•±…Ì%59M%=8ôÌÉ€°Ñ¡•¸ÑÉ•…Ð€Ý€°MeMQ5€°…¹IMM€…ÌÑ¡É•”•ÅÕ¥Ù…±•¹ÐÙ…±Õ•Ì¸%ÐÝ½Õ±…±Í¼‰”¥¹½ÉÉ•ÐÑ¼‘•ÍÉ¥‰”MeMQ5€…¹IMM€…Ì€€µÍ•Á…É…Ñ•Í¥µÁ±ä‰•…ÕÍ”Ñ¡”Í•±•Ñ½È¥ÌÁ…É…µ•Ñ•É¥é•èÁ…å±½…Ù…±Õ•ÌÉ•µ…¥¸Í•Á…É…Ñ•‰ä€©€¸((ŒŒŒ½¹É•Ñ”Á…ÑÑ•É¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÀÕ€((ŒŒŒŒ±…ÐÍ•±•Ñ½ÈÝ¥Ñ µÕ±Ñ¥Á±”Ù…±Õ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÀÙ€()1¥¡Ñ¥¹œÑ•µÁ½É¥é…Ñ¥½¸ÕÍ•Ì„™±…Ð%59M%=8€É€Í•±•Ñ½È…¹Ñ¡É•”Á…å±½…Ù…±Õ•Ìè()Ñ•áÐ(¨ŒÄ©]!I¨ŒÈ©!=UIL©5%9UQL©M=9LŒŒ)€()!=UIM€°5%9UQM€°…¹M=9M€…É”Ù…±Õ•Ìì¹½¹”¥ÌÁ…ÉÐ½˜Ñ¡”Í•±•Ñ½È¸((ŒŒŒŒA…É…µ•Ñ•É¥é•ÝÉ¥Ñ”Í•±•Ñ½È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÀÝ€()‘Ù…¹•ÕÑ½µ…Ñ¥½¸…‰Í½±ÕÑ”Á½Í¥Ñ¥½¹¥¹œÕÍ•Ì„Á…É…µ•Ñ•È…ÑÑ…¡•Ñ¼Ñ¡”ÝÉ¥Ñ…‰±”Í•±•Ñ½Èè()Ñ•áÐ(¨ŒÈ©]!I¨ŒÄÄM!UQQI}AI%=I%Qd©M!UQQI}1Y0ŒŒ)€()M!UQQI}AI%=I%Qe€‰•±½¹ÌÑ¼Ñ¡”%59M%=8€ÄÅ€Í•±•Ñ½È¸M!UQQI}1Y1€¥ÌÑ¡”Á…å±½…Ù…±Õ”¸((ŒŒŒŒA…É…µ•Ñ•É¥é•‘¥…¹½ÍÑ¥ŒÍ•±•Ñ½È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÀá€()¥…¹½ÍÑ¥Œ½Á•É…Ñ¥½¹ÌÕÍ”Í•±•Ñ½ÉÌÍÕ …Ì€ÌÈM1=Q€°Ý¡•É”M1=Q€¥‘•¹Ñ¥™¥•ÌÑ¡”•Ù¥”µ±½…°Í±½Ñ€¸Q¡”™½±±½Ý¥¹œMeM€…¹I€™¥•±‘Ì…É”½É‘¥¹…Éä€©€µÍ•Á…É…Ñ•Á…å±½…Ù…±Õ•Ìè()Ñ•áÐ(¨%9=MQ%}]!<©Y%¨ÌÈM1=P©MeL©HŒŒ)€()Q¡¥Ì‘¥ÍÑ¥¹Ñ¥½¸¥Ì•ÍÍ•¹Ñ¥…°Ý¡•¸½ÉÉ•±…Ñ¥¹œ„É•ÍÁ½¹Í”Ý¥Ñ „•Ù¥”5½‘Õ±”èÑ¡”Í±½Ñ€¥Ì…‘‘É•ÍÍ¥¹œÑ¡”ÁÉ½Á•ÉÑä¥¹ÍÑ…¹”°Ý¡¥±”MeM€…¹I€‘•ÍÉ¥‰”¥ÑÌ½¹™¥ÕÉ•™Õ¹Ñ¥½¹…°…‘‘É•ÍÌ¸((ŒŒŒI•ÅÕ•ÍÑÌ°É•ÍÁ½¹Í•Ì°…¹É•Á½ÉÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÀå€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()É•ÅÕ•ÍÐÍÕÁÁ±¥•ÌÑ¡”Í•±•Ñ½È‰ÕÐ¹½Éµ…±±ä¹¼Á…å±½…è()Ñ•áÐ(¨]!<©]!I©%59M%=8@ÄŒŒ)€()É•ÍÁ½¹Í”½É‘¥¹…É¥±äÉ•Á•…ÑÌ•¹½Õ ½¹Ñ•áÐÑ¼¥‘•¹Ñ¥™äÑ¡”É•Á½ÉÑ•ÁÉ½Á•ÉÑä…¹…ÁÁ•¹‘Ì¥ÑÌÙ…±Õ•Ìè()Ñ•áÐ(¨]!<©]!I©%59M%=8@Ä©XÄ©XÈŒŒ)€()Q¡”Í…µ”É•ÍÁ½¹Í”µÍ¡…Á•™É…µ”…¸…ÁÁ•…È…Íå¹¡É½¹½ÕÍ±ä½¸…¸•Ù•¹ÑÌÍ•ÍÍ¥½¸¸¥É•Ñ¥½¸…¹Í•ÍÍ¥½¸ÍÑ…Ñ”Ñ¡•É•™½É”‘¥ÍÑ¥¹Õ¥Í „Í½±¥¥Ñ•É•ÍÁ½¹Í”™É½´…¸Õ¹Í½±¥¥Ñ•É•Á½ÉÐìÍå¹Ñ…à…±½¹”µ…ä¹½Ð¸()Q¡”É•ÅÕ•ÍÐ…¹É•ÍÁ½¹Í”Í•±•Ñ½ÉÌ¹••¹½Ð‰”•ÅÕ…°èÁÕ‰±¥Í¡•mQ•µÁ•É…ÑÕÉ”½¹ÑÉ½°…Õ±Ð¥…¹½ÍÑ¥Ít ¸¸½‘¥…¹½ÍÑ¥Ì½Ñ•µÁ•É…ÑÕÉ”µ½¹ÑÉ½°µ™…Õ±ÑÌ¹µ¤¥¹±Õ‘•Ì„%59M%=8€ÈÁ€É•ÅÕ•ÍÐÉ•ÑÕÉ¹¥¹œ%59M%=8€ÈÅ€É•½É‘Ì¸mM½Õ¹¥™™ÕÍ¥½¹t ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´ÈÈµÍ½Õ¹µ‘¥™™ÕÍ¥½¸¼¤…±Í¼ÕÍ•Ì‘¥™™•É¥¹œÉ•ÅÕ•ÍÐ…¹É•ÍÁ½¹Í”Í½ÕÉ”…‘‘É•ÍÍ•Ì¸Q¡”•¹•É¥Œ™½ÉµÌ…‰½Ù”‘¼¹½Ð½Ù•ÉÉ¥‘”Ñ¡½Í”½Á•É…Ñ¥½¸µÍÁ•¥™¥Œµ…ÁÁ¥¹Ì¸()½±±•Ñ¥Ù”É•ÅÕ•ÍÐ…¸ÁÉ½‘Õ”µÕ±Ñ¥Á±”É•ÍÁ½¹Í”™É…µ•Ì™½±±½Ý•‰ä-€¸¼¹½Ð…ÍÍÕµ”½¹”É•ÅÕ•ÍÐå¥•±‘Ì½¹”Ù…±Õ”™É…µ”¸%˜Ñ¡”Í•ÅÕ•¹”Ñ•Éµ¥¹…Ñ•Ì¥¸9-€°Ñ¡”½µµ½¸ÁÉ½Ñ½½°Á•Éµ¥ÑÌÑ¡”ÁÉ••‘¥¹œÁÉ½Ù¥Í¥½¹…°É•ÍÕ±ÑÌÑ¼‰”ÑÉ•…Ñ•…Ì¥¹Ù…±¥¸((ŒŒŒ]É¥Ñ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÄÁ€()ÝÉ¥Ñ”ÁÉ•™¥á•ÌÑ¡”½µÁ±•Ñ”Í•±•Ñ½ÈÝ¥Ñ €€è()Ñ•áÐ(¨]!<©]!I¨%59M%=8@Ä©XÄŒŒ)€()Q¡”ÝÉ¥Ñ”µ…É­•È‘½•Ì¹½ÐÉ•µ½Ù”Ñ¡”Í•±•Ñ½ÈÌ½Ý¸Á…É…µ•Ñ•ÉÌ¸Á…ÉÍ•È…¸É•ÁÉ•Í•¹ÐÑ¡¥Ì±•…¹±ä…Ìè()Ñ•áÐ)½Á•É…Ñ¥½¸€ô€‰ÝÉ¥Ñ”ˆ)‘¥µ•¹Í¥½¸€ô€‰%59M%=8ˆ)Í•±•Ñ½É}Á…É…µ•Ñ•ÉÌ€ôl‰@Ä‰t)Ù…±Õ•Ì€ôl‰XÄ‰t)€()Q¡”•á¥ÍÑ•¹”½˜„É•…‘…‰±”½ÈÉ•Á½ÉÑ…‰±”%59M%=9€‘½•Ì¹½Ð¥µÁ±äÝÉ¥Ñ”ÍÕÁÁ½ÉÐ¸I•…°É•Á½ÉÐ°…¹ÝÉ¥Ñ”…Á…‰¥±¥ÑäµÕÍÐ‰”•ÍÑ…‰±¥Í¡•Í•Á…É…Ñ•±ä™½ÈÑ¡”•á…ÐÍ•±•Ñ½È…¹Ñ…É•Ð=‰©•Ð¸((ŒŒŒÉ¥Ñä…¹ÑåÁ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÄÅ€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()9•¥Ñ¡•ÈÁ…É…µ•Ñ•È½Õ¹Ð¹½ÈÙ…±Õ”½Õ¹Ð¥Ì±½‰…±±ä™¥á•¸Q¡”…Ù…¥±…‰±”ÁÕ‰±¥ŒÍÁ•¥™¥…Ñ¥½¸•ÍÑ…‰±¥Í¡•Ì¹¼ÁÉ½Ñ½½°µÝ¥‘”µ…á¥µÕ´½Õ¹Ð™½ÈÍ•±•Ñ½ÈÁ…É…µ•Ñ•ÉÌ½ÈÁ…å±½…Ù…±Õ•Ì°…¹¥Ð‘½•Ì¹½ÐÍÁ•¥™ä„Õ¹¥Ù•ÉÍ…°µ…á¥µÕ´™É…µ”±•¹Ñ ¸Q¡¥Ì…‰Í•¹”½˜„½µµ½¸±¥µ¥Ð‘½•Ì¹½Ðµ…­”Ñ¡”…É¥ÑäÕ¹É•ÍÑÉ¥Ñ•™½È„Á…ÉÑ¥Õ±…È½Á•É…Ñ¥½¸èÑ¡”•á…Ð€¡]!<°%59M%=8°½Á•É…Ñ¥½¸¥€‘•™¥¹¥Ñ¥½¸‘•Ñ•Éµ¥¹•ÌÝ¡¥ ½Õ¹ÑÌ…É”Ù…±¥¸()MåÍÑ•´µÍÁ•¥™¥Œ‘•™¥¹¥Ñ¥½¹Ì…¸¥µÁ½Í”è((´•á…Ð½ÈÙ…É¥…‰±”Í•±•Ñ½ÈµÁ…É…µ•Ñ•È½Õ¹ÑÌì(´•á…Ð½ÈÙ…É¥…‰±”Á…å±½…½Õ¹ÑÌì(´‘•¥µ…°É…¹•Ì½È•¹Õµ•É…Ñ¥½¹Ìì(´™¥á•µÝ¥‘Ñ ÍÑÉ¥¹Ì…¹Í¥¹¥™¥…¹Ð±•…‘¥¹œé•É½•Ìì(´•¹½‘•Ñ•µÁ•É…ÑÕÉ•Ì°Ñ¥µ•Ì°µ…Í­Ì°¥‘•¹Ñ¥™¥•ÉÌ°½ÈÑ•áÐì(´É•±…Ñ¥½¹Í¡¥ÁÌ‰•ÑÝ••¸Í•±•Ñ½ÈÁ…É…µ•Ñ•ÉÌ…¹Ñ¡”¹Õµ‰•È½Èµ•…¹¥¹œ½˜Ù…±Õ•Ì¸()-••ÀÉ…Ü™¥•±‘Ì…ÌÍÑÉ¥¹ÌÕ¹Ñ¥°Ñ¡”…ÁÁ±¥…‰±”€¡]!<°%59M%=8¥€É…µµ…È¥Ì­¹½Ý¸¸AÉ•µ…ÑÕÉ”¥¹Ñ••È½¹Ù•ÉÍ¥½¸…¸‘•ÍÑÉ½ä±•…‘¥¹œé•É½•Ì°•µÁÑäÙ…±Õ•Ì°™¥á•µÝ¥‘Ñ ¥‘•¹Ñ¥™¥•ÉÌ°…¹•¹½‘•ÍÑÉÕÑÕÉ”¸((ŒŒŒM•µ…¹Ñ¥Œ¥‘•¹Ñ¥Ñä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÄÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€()½È„™±…ÐÁÉ½Á•ÉÑä°€¡]!<°%59M%=8¥€…¸‰”ÍÕ™™¥¥•¹ÐÑ¼Í•±•ÐÑ¡”Ù…±Õ”É…µµ…È¸½È„Á…É…µ•Ñ•É¥é•ÁÉ½Á•ÉÑä°ÕÍ”…Ð±•…ÍÐè()Ñ•áÐ(¡]!<°%59M%=8°M1Q=I}AI5QIL¤)€()%¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸…¸…‘‘¥Ñ¥½¹…±±ä‘•Á•¹½¸]!I€°‘¥É•Ñ¥½¸°Í•ÍÍ¥½¸°•Ù¥”™¥ÉµÝ…É”°5½‘Õ±”½=‰©•Ð…Á…‰¥±¥Ñä°…¹Ý¡•Ñ¡•ÈÑ¡”™É…µ”¥Ì„É•ÅÕ•ÍÐ°É•ÍÁ½¹Í”°É•Á½ÉÐ°½ÈÝÉ¥Ñ”¸()ÅÕ…°¹Õµ•É¥Œ%59M%=9€¥‘•¹Ñ¥™¥•ÉÌ¥¸‘¥™™•É•¹Ð]!=€¹…µ•ÍÁ…•Ì‘¼¹½Ð¥µÁ±ä•ÅÕ…°µ•…¹¥¹œ¸ÅÕ…°Í•±•Ñ½ÉÌ½¸‘¥™™•É•¹Ð•Ù¥”=‰©•ÑÌ‘¼¹½ÐÁÉ½Ù”•ÅÕ…°ÍÕÁÁ½ÉÐ½ÈÙ…±Õ”É…¹•Ì¸((ŒŒŒA…ÉÍ•Èµ½‘•°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÄÍ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()ÁÉ…Ñ¥…°Á…ÉÍ•ÈÍ¡½Õ±è((Ä¸¥‘•¹Ñ¥™äÑ¡”%59M%=9€™É…µ”™…µ¥±ä™É½´€¨]!=€ì(È¸ÍÁ±¥Ð½¹±äÑ¡”µ…©½È€©€µ‘•±¥µ¥Ñ•™¥•±‘Ì°ÁÉ•Í•ÉÙ¥¹œ•µÁÑä™¥•±‘Ìì(Ì¸‘•Ñ•Ð…¹É•µ½Ù”Ñ¡”±•…‘¥¹œÝÉ¥Ñ”µ…É­•È™É½´Ñ¡”Í•±•Ñ½È™¥•±ì(Ð¸ÍÁ±¥ÐÑ¡”É•µ…¥¹¥¹œÍ•±•Ñ½È™¥•±½¸€€¥¹Ñ¼Ñ¡”¥‘•¹Ñ¥™¥•È…¹Í•±•Ñ½ÈÁ…É…µ•Ñ•ÉÌì(Ô¸É•Ñ…¥¸Ñ¡”™½±±½Ý¥¹œµ…©½È™¥•±‘Ì…Ì½É‘•É•Á…å±½…Ù…±Õ•Ìì(Ø¸É•Í½±Ù”Ñ¡”ÍåÍÑ•´µÍÁ•¥™¥ŒÉ…µµ…È‰•™½É”½¹Ù•ÉÑ¥¹œÑåÁ•Ìì(Ü¸Ù…±¥‘…Ñ”½Á•É…Ñ¥½¸‘¥É•Ñ¥½¸…¹Ñ…É•Ð…Á…‰¥±¥ÑäÍ•Á…É…Ñ•±ä¸()¼¹½Ð±½‰…±±äÍÁ±¥ÐÑ¡”•¹Ñ¥É”™É…µ”½¸‰½Ñ €©€…¹€€ì‘½¥¹œÍ¼•É…Í•ÌÑ¡”‘¥™™•É•¹”‰•ÑÝ••¸Í•±•Ñ½ÈÁ…É…µ•Ñ•ÉÌ°Á…å±½…Ù…±Õ•Ì°…¹Á…É…µ•Ñ•É¥é•]!I€½È]!Q€™¥•±‘Ì¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀØéÌÀÀÀÀÄÑ€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()±…ÐÉ•ÅÕ•ÍÐ°É•ÍÁ½¹Í”°…¹ÝÉ¥Ñ”™½ÉµÌ½µ”™É½´m=Á•¹]•‰9•Ð%¹ÑÉ½‘ÕÑ¥½¸ÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=]9}%¹ÑÉ½}9¹Á‘˜¤¸A…É…µ•Ñ•É¥é•Í•±•Ñ½ÉÌ…É”•ÍÑ…‰±¥Í¡•‰äÑ¡”‘•‘¥…Ñ•™Õ¹Ñ¥½¹…°ÍÁ•¥™¥…Ñ¥½¹Ì…¹Ñ¡”5å!=5MÕ¥Ñ”‘¥…¹½ÍÑ¥Œ½ÁÉ½É…µµ¥¹œÑ•µÁ±…Ñ•Ì°¥¹±Õ‘¥¹œ…‘Ù…¹•ÕÑ½µ…Ñ¥½¸%59M%=8€ÄÅ€…¹‘¥…¹½ÍÑ¥ŒÍ±½ÐµÅÕ…±¥™¥•Í•±•Ñ½ÉÌ¸()M•”mÉ…µ”Må¹Ñ…át¡™É…µ”µÍå¹Ñ…à¹µ¤°mMÑÉ•…´A…ÉÍ¥¹t¡ÍÑÉ•…´µÁ…ÉÍ¥¹œ¹µ¤°m‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤°Ñ¡”É•±•Ù…¹Ð™Õ¹Ñ¥½¹…°]!=€Á…”°…¹Ñ¡”m¥…¹½ÍÑ¥Œ%59M%=9€I•™•É•¹•t ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥µ•¹Í¥½¸µÉ•™•É•¹”¹µ¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀÜ()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½™É…µ”µÍå¹Ñ…à¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒÉ…µ”Må¹Ñ…à()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÜéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()¸½É‘¥¹…Éä=Á•¹]•‰9•Ð™É…µ”¥Ì…¸M%$µ•ÍÍ…”Ñ¡…Ð‰•¥¹ÌÝ¥Ñ €©€°½¹Ñ…¥¹Ì€©€µÍ•Á…É…Ñ•Ñ…Ì°…¹•¹‘ÌÝ¥Ñ €Œ€¸()Ñ•áÐ(©Ñ…œÄ©Ñ…œÈ¨¸¸¸©Ñ…8ŒŒ)€()Q¡”¥¹ÑÉ½‘ÕÑ½ÉäÍÁ•¥™¥…Ñ¥½¸±¥µ¥ÑÌ½É‘¥¹…Éä™É…µ”¡…É…Ñ•ÉÌÑ¼‘•¥µ…°‘¥¥ÑÌ°€©€°…¹€€¸Q¡”µ•…¹¥¹œ…¹Á•Éµ¥ÑÑ•ÍÑÉÕÑÕÉ”½˜•… Ñ…œ‘•Á•¹½¸Ñ¡”™É…µ”™…µ¥±ä…¹Í•±•Ñ•]!=€¸((ŒŒŒ½µµ½¸™É…µ”™½ÉµÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÜéÌÀÀÀÀÀÉ€()ðÉ…µ”±…ÍÌðMå¹Ñ…àðAÕÉÁ½Í”ð)ð€´´´ð€´´´ð€´´´ð)ð½µµ…¹½ÍÑ…ÑÕÌ½•Ù•¹Ðð€©]!<©]!P©]!IŒ€ð½µµ…¹°É•Á½ÉÑ•ÍÑ…Ñ”°½È…Íå¹¡É½¹½ÕÌ•Ù•¹Ðð)ðMÑ…ÑÕÌÉ•ÅÕ•ÍÐð€¨]!<©]!IŒ€ðI•ÅÕ•ÍÐÕÉÉ•¹ÐÍÑ…Ñ”ð)ð%59M%=9€É•ÅÕ•ÍÐð€¨]!<©]!I©%59M%=8Œ€ðI•ÅÕ•ÍÐ„ÁÉ½Á•ÉÑäÙ…±Õ”ð)ð%59M%=9€É•ÍÁ½¹Í”½É•Á½ÉÐð€¨]!<©]!I©%59M%=8©Y1U¸¸¸Œ€ðI•ÑÕÉ¸½È…Íå¹¡É½¹½ÕÍ±äÉ•Á½ÉÐ„ÁÉ½Á•ÉÑäÙ…±Õ”ð)ð%59M%=9€ÝÉ¥Ñ”ð€¨]!<©]!I¨%59M%=8©Y1U¸¸¸Œ€ð]É¥Ñ”„ÍÕÁÁ½ÉÑ•ÁÉ½Á•ÉÑäð)ð-€ð€¨Œ¨ÄŒ€ðA½Í¥Ñ¥Ù”É•ÍÕ±Ð½ÈÍ•ÅÕ•¹”Ñ•Éµ¥¹…Ñ½Èð)ð9-€ð€¨Œ¨ÀŒ€ð9•…Ñ¥Ù”É•ÍÕ±Ð½È™…¥±•µÍ•ÅÕ•¹”Ñ•Éµ¥¹…Ñ½Èð()Y1U¸¸¹€¥Ì¹½Ñ…Ñ¥½¸ÕÍ•‰äÑ¡¥ÌÉ•™•É•¹”™½ÈÑ¡”½É‘•É•Ù…±Õ”™¥•±‘Ì‘•™¥¹•‰äÑ¡…Ð%59M%=9€ìÑ¡”•±±¥ÁÍ¥Ì¥Ì¹½ÐÑÉ…¹Íµ¥ÑÑ•¸()½¹¹•Ñ¥½¸Í•±•Ñ½ÉÌ…¹…ÕÑ¡•¹Ñ¥…Ñ¥½¸™É…µ•ÌÕÍ”Ñ¡”Í…µ”½ÕÑ•È‘•±¥µ¥Ñ•ÉÌ‰ÕÐ¡…Ù”Ñ¡•¥È½Ý¸ÍÑ…Ñ”µ‘•Á•¹‘•¹ÐÉ…µµ…ÉÌ¸M•”m½¹¹•Ñ¥½¸…¹M•ÍÍ¥½¹Ít¡Í•ÍÍ¥½¹Ì¹µ¤…¹mÕÑ¡•¹Ñ¥…Ñ¥½¹t¡…ÕÑ¡•¹Ñ¥…Ñ¥½¸¹µ¤¸((ŒŒŒ•±¥µ¥Ñ•ÉÌ…¹•µÁÑäÑ…Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÜéÌÀÀÀÀÀÍ€()ðQ½­•¸ðI½±”ð)ð€´´´ð€´´´ð)ð€©€ðMÑ…ÉÑÌ„™É…µ”…¹Í•Á…É…Ñ•Ìµ…©½ÈÑ…Ìð)ð€Œ€ðQ•Éµ¥¹…Ñ•Ì„™É…µ”ð)ð€€ðA…ÉÑ¥¥Á…Ñ•Ì¥¸„™É…µ”Ù…É¥…¹Ð½ÈÁ…É…µ•Ñ•É¥é•™¥•±…½É‘¥¹œÑ¼½¹Ñ•áÐð()Q…Ì…¸‰”•µÁÑä¸½È•á…µÁ±”°€¨ŒÄÌ¨¨ÄŒ€½¹Ñ…¥¹Ì…¸¥¹Ñ•¹Ñ¥½¹…±±ä•µÁÑä]!I€¸Ñ½­•¹¥é•ÈµÕÍÐÁÉ•Í•ÉÙ”Ñ¡…Ð•µÁÑä™¥•±É…Ñ¡•ÈÑ¡…¸½±±…ÁÍ¥¹œ…‘©…•¹ÐÍ•Á…É…Ñ½ÉÌ¸()€€¡…Ì¹¼Í¥¹±”½¹Ñ•áÐµ¥¹‘•Á•¹‘•¹Ðµ•…¹¥¹œ¸%Ð…¸¥¹ÑÉ½‘Õ”„É•ÅÕ•ÍÐ™…µ¥±ä°ÁÉ•™¥à„ÝÉ¥Ñ…‰±”%59M%=9€°µ…É¬„É½ÕÀ…‘‘É•ÍÌ°…‘É½ÕÑ¥¹œÅÕ…±¥™¥•ÉÌ°½ÈÍ•Á…É…Ñ”½Á•É…Ñ¥½¸µÍÁ•¥™¥ŒÁ…É…µ•Ñ•ÉÌ¸((ŒŒŒ½µµ…¹°ÍÑ…ÑÕÌ°…¹•Ù•¹Ð™É…µ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÜéÌÀÀÀÀÀÑ€()Q¡”™½É´€©]!<©]!P©]!IŒ€¥Ì‘¥É•Ñ¥½¸´…¹Í•ÍÍ¥½¸µ‘•Á•¹‘•¹Ðè((´¥¸„½µµ…¹‘Ì½…Ñ¥½¹ÌÍ•ÍÍ¥½¸°Ñ¡”±¥•¹ÐÕÍ•Ì¥ÐÑ¼É•ÅÕ•ÍÐ…¸…Ñ¥½¸ì(´Ñ¡”Í•ÉÙ•È…¸ÕÍ”¥ÐÑ¼…¹ÍÝ•È„ÍÑ…ÑÕÌÉ•ÅÕ•ÍÐì(´¥¸…¸•Ù•¹ÑÌÍ•ÍÍ¥½¸°¥ÐÉ•Á½ÉÑÌ…¸…Íå¹¡É½¹½ÕÌÍÑ…Ñ”¡…¹”½È•Ù•¹Ð¸()]!Q€…¹]!I€…¸•… ½¹Ñ…¥¸€€µ¥¹ÑÉ½‘Õ•Á…É…µ•Ñ•ÉÌÝ¡•¸‘•™¥¹•‰äÑ¡”Í•±•Ñ•]!=€¸A…ÉÍ”Ñ¡•´½¹±ä…™Ñ•ÈÉ•Í½±Ù¥¹œÑ¡”ÍåÍÑ•´¸((ŒŒŒMÑ…ÑÕÌÉ•ÅÕ•ÍÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÜéÌÀÀÀÀÀÕ€()ÍÑ…ÑÕÌÉ•ÅÕ•ÍÐ¡…Ì™½É´€¨]!<©]!IŒ€¸%˜]!I€¥Ì½µ¥ÑÑ•Ý¡•É”Ñ¡”ÍåÍÑ•´Á•Éµ¥ÑÌ¥Ð°Ñ¡”É•ÅÕ•ÍÐ…¸…‘‘É•ÍÌÑ¡”½µÁ±•Ñ”ÍåÍÑ•´¸()Q¡”Í•ÉÙ•È…¸É•ÑÕÉ¸½¹”½Èµ½É”¹½Éµ…°½µµ…¹½ÍÑ…ÑÕÌ™É…µ•Ì¸Q¡”É•ÍÁ½¹Í”Í•ÅÕ•¹”•¹‘ÌÝ¥Ñ -€½¸ÍÕ•ÍÌ½È9-€½¸™…¥±ÕÉ”ì¥Ð¥Ì¹½ÐÍ…™”Ñ¼…ÍÍÕµ”„Í¥¹±”É•ÍÕ±Ð™É…µ”¸((ŒŒŒ%59M%=9€½Á•É…Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÜéÌÀÀÀÀÀÙ€()AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()É•…É•ÅÕ•ÍÐ¥‘•¹Ñ¥™¥•Ì]!=€°]!I€°…¹%59M%=9€¸É•ÍÁ½¹Í”…ÉÉ¥•ÌÑ¡”½¹Ñ•áÐ½˜Ñ¡”É•Á½ÉÑ•ÁÉ½Á•ÉÑä…¹½É‘•É•Ù…±Õ•Ì°‰ÕÐ¹••¹½ÐÉ•Á•…ÐÑ¡”É•ÅÕ•ÍÐÌÍ•±•Ñ½È½È…‘‘É•ÍÌ±¥Ñ•É…±±ä¸½È•á…µÁ±”°Ñ¡”ÁÕ‰±¥Í¡•]!<€ÄÀÀÐ%59M%=8€ÈÁ€½±±•Ñ¥Ù”™…Õ±ÐÉ•ÅÕ•ÍÐÉ•ÑÕÉ¹Ì%59M%=8€ÈÅ€é½¹”É•½É‘ÌìM½Õ¹¥™™ÕÍ¥½¸…¸É•Á½ÉÐ„Í½ÕÉ”…‘‘É•ÍÌ‘¥™™•É•¹Ð™É½´¥ÑÌÉ•ÅÕ•ÍÐ…‘‘É•ÍÌ¸½ÉÉ•±…Ñ”ÕÍ¥¹œÑ¡”½Á•É…Ñ¥½¸µÍÁ•¥™¥ŒÉ•ÍÁ½¹Í”É…µµ…È¸Q¡”Í…µ”É•ÍÁ½¹Í”™½É´…¸…±Í¼…ÁÁ•…È…Íå¹¡É½¹½ÕÍ±ä½¸…¸•Ù•¹ÑÌ½¹¹•Ñ¥½¸Ý¡•¸„Ù…±Õ”¡…¹•Ì½È¥ÌÉ•Á½ÉÑ•Á•É¥½‘¥…±±ä¸()ÝÉ¥Ñ”ÁÉ•™¥á•ÌÑ¡”%59M%=9€Í•±•Ñ½ÈÝ¥Ñ €€¸Íå¹Ñ…Ñ¥…±±äÙ…±¥ÝÉ¥Ñ”‘½•Ì¹½Ð¥µÁ±äÑ¡…ÐÑ¡”Í•±•Ñ•ÁÉ½Á•ÉÑä¥ÌÝÉ¥Ñ…‰±”¸()M½µ”ÍåÍÑ•µÌÁ…É…µ•Ñ•É¥é”Ñ¡”Í•±•Ñ½È¥ÑÍ•±˜¸½È•á…µÁ±”°‘¥…¹½ÍÑ¥Œ€ÌÈM1=Q€Í•±•ÑÌ%59M%=8€ÌÉ€™½È½¹”Í±½Ñ€ìÑ¡”™½±±½Ý¥¹œMeM€…¹I€É•µ…¥¸½É‘¥¹…Éä€©€µÍ•Á…É…Ñ•Ù…±Õ•Ì¸Q¡”€€¥¹Í¥‘”Ñ¡”Í•±•Ñ½È‘½•Ì¹½ÐÉ•Á±…”Ñ¡”µ…©½Èµ™¥•±‘•±¥µ¥Ñ•È¸((ŒŒŒ¥•±Í½Á”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÜéÌÀÀÀÀÀÝ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()Q¡”Í•µ…¹Ñ¥Œ¥‘•¹Ñ¥Ñä½˜„™¥•±¥¹±Õ‘•Ì¥ÑÌ¹…µ•ÍÁ…”…¹ÍÑÉÕÑÕÉ…°É½±”è((´…¸½Á•É…Ñ¥½¸¥Ì…Ð±•…ÍÐ€¡]!<°]!P¥€Á±ÕÌ…¹ä]!Q€Á…É…µ•Ñ•ÉÌ…¹Ñ…É•Ð½¹Ñ•áÐì(´…¸…‘‘É•ÍÌ¥Ì€¡]!<°]!I¥€ì(´„ÁÉ½Á•ÉÑä¥Ì…Ð±•…ÍÐ€¡]!<°%59M%=8¥€Á±ÕÌÍ•±•Ñ½ÈÁ…É…µ•Ñ•ÉÌì(´ÕÍ•Èµ™…¥¹œµ•…¹¥¹œ…¸…‘‘¥Ñ¥½¹…±±ä‘•Á•¹½¸Ñ¡”Ñ…É•Ð=‰©•Ð¸()ÅÕ…°¹Õµ•É¥ŒÙ…±Õ•Ì¥¸‘¥™™•É•¹Ð]!=€¹…µ•ÍÁ…•Ì‘¼¹½Ð¥µÁ±ä•ÅÕ…°µ•…¹¥¹œ¸((ŒŒŒA…ÉÍ¥¹œÉ•ÅÕ¥É•µ•¹ÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÜéÌÀÀÀÀÀá€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()¼¹½ÐÁ…ÉÍ”=Á•¹]•‰9•ÐÝ¥Ñ „Í¥¹±”‘•±¥µ¥Ñ•ÈÍÁ±¥Ð…¹¥µµ•‘¥…Ñ”¥¹Ñ••È½¹Ù•ÉÍ¥½¸¸AÉ•Í•ÉÙ”Ñ¡”É…Ü™É…µ”°É•½¹¥é”Ñ¡”™…µ¥±ä°ÁÉ•Í•ÉÙ”•µÁÑäÑ…Ì…¹±•…‘¥¹œé•É½•Ì°…¹Ñ¡•¸…ÁÁ±ä™¥•±µÍÁ•¥™¥ŒÉ…µµ…ÉÌ¸()M•”mMÑÉ•…´A…ÉÍ¥¹t¡ÍÑÉ•…´µÁ…ÉÍ¥¹œ¹µ¤™½È…¸¥¹É•µ•¹Ñ…°Á…ÉÍ•Èµ½‘•°°m‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤™½È]!I€°m]!Qt¡Ý¡…Ð¹µ¤°m%59M%=9t¡‘¥µ•¹Í¥½¹Ì¹µ¤°…¹m­¹½Ý±•‘•µ•¹ÑÍt¡…­¹½Ý±•‘•µ•¹ÑÌ¹µ¤¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀÜéÌÀÀÀÀÀå€()AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡”½µµ½¸™É…µ”™½ÉµÌ°…±Á¡…‰•Ð°•µÁÑäµÑ…œÉÕ±”°É•ÅÕ•ÍÐ½É•ÍÁ½¹Í”‘¥É•Ñ¥½¸°…¹…­¹½Ý±•‘•µ•¹ÐµÑ•Éµ¥¹…Ñ•Í•ÅÕ•¹•Ì½µ”™É½´m=Á•¹]•‰9•Ð%¹ÑÉ½‘ÕÑ¥½¸ÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=]9}%¹ÑÉ½}9¹Á‘˜¤¸MåÍÑ•´µÍÁ•¥™¥Œ•áÑ•¹Í¥½¹Ì…É”‘½Õµ•¹Ñ•½¹±äÝ¡•É”Ñ¡”É•±•Ù…¹Ð]!=€Í½ÕÉ”°¥µÁ±•µ•¹Ñ…Ñ¥½¸‘…Ñ…‰…Í”°½È½‰Í•ÉÙ•Ý½É­™±½Ü•ÍÑ…‰±¥Í¡•ÌÑ¡•´¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀà()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½Í½Á”µ…¹µ…É¡¥Ñ•ÑÕÉ”¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒ=Á•¹]•‰9•ÐM½Á”…¹É¡¥Ñ•ÑÕÉ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀàéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°ÍÍ€°é¥‰••€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()Q¡”•¹å±½Á•‘¥„½Ù•ÉÌÑ•¡¹½±½¥•ÌÑ¼Ñ¡”•áÑ•¹ÐÑ¡…Ð=Á•¹]•‰9•Ð•áÁ½Í•Ì°É•ÁÉ•Í•¹ÑÌ°ÑÉ…¹ÍÁ½ÉÑÌ°½¹™¥ÕÉ•Ì°½È½¹ÑÉ½±ÌÑ¡•´¸‰ÕÌ°É…‘¥¼¹•ÑÝ½É¬°ÁÉ½‘ÕÐ…Ñ…±½Õ”°½¹™¥ÕÉ…Ñ¥½¸…ÁÁ±¥…Ñ¥½¸°½È™¥ÉµÝ…É”ÍÕ‰ÍåÍÑ•´‰•±½¹Ì¡•É”½¹±äÝ¡•É”¥Ð•ÍÑ…‰±¥Í¡•Ì…¸=Á•¹]•‰9•ÐµÙ¥Í¥‰±”¥¹Ñ•É™…”½ÈÑ¡”…ÁÁ±¥…‰¥±¥Ñä½˜Ñ¡…Ð¥¹Ñ•É™…”¸()Q¡¥Ì‰½Õ¹‘…Éä¥¹±Õ‘•ÌML…¹i¥	•”µ‰…­•‰•¡…Ù¥½ÈÑ¡…Ð¥ÌÙ¥Í¥‰±”Ñ¡É½Õ =Á•¹]•‰9•Ð¸%Ð‘½•Ì¹½Ðµ…­”•¥Ñ¡•ÈÕ¹‘•É±å¥¹œÑ•¡¹½±½äÍå¹½¹åµ½ÕÌÝ¥Ñ =Á•¹]•‰9•Ð°…¹¥Ð‘½•Ì¹½Ð•áÑ•¹Ñ¡”•¹å±½Á•‘¥„¥¹Ñ¼Õ¹É•±…Ñ•ML•±•ÑÉ¥…°‘•Í¥¸°i¥	•”É…‘¥¼¥¹Ñ•É¹…±Ì°½È„Ù•¹‘½È…ÁÁ±¥…Ñ¥½¸ÌÁÉ¥Ù…Ñ”¥µÁ±•µ•¹Ñ…Ñ¥½¸¸((ŒŒŒÉ¡¥Ñ•ÑÕÉ…°±…å•ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀàéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°é¥‰••€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()ð1…å•Èð…¹½¹¥…°ÑÉ•…Ñµ•¹Ðð	½Õ¹‘…Éäð)ð€´´´ð€´´´ð€´´´ð)ð%¹Ñ•É™…”…¹ÑÉ…¹ÍÁ½ÉÐðm½¹¹•Ñ¥½¸…¹M•ÍÍ¥½¹Ít¡Í•ÍÍ¥½¹Ì¹µ¤°mi¥	•”%¹Ñ•É™…•t¡é¥‰•”µ¥¹Ñ•É™…”¹µ¤ðÍÑ…‰±¥Í¡•Ì¡½Ü=Á•¹]•‰9•Ð™É…µ•Ì…É”…ÉÉ¥•™½È…¸…ÁÁ±¥…‰±”¥¹Ñ•É™…”ì½¹”¥¹Ñ•É™…”ÌÍ•ÑÕÀ…¹É•ÑÉäÉÕ±•Ì‘¼¹½Ð…ÕÑ½µ…Ñ¥…±±ä…ÁÁ±äÑ¼…¹½Ñ¡•È¸ð)ð½µµ½¸™É…µ”µ•¡…¹¥ÌðmÉ…µ”Må¹Ñ…át¡™É…µ”µÍå¹Ñ…à¹µ¤°m‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤°m]!Qt¡Ý¡…Ð¹µ¤°m%59M%=9t¡‘¥µ•¹Í¥½¹Ì¹µ¤°…¹m­¹½Ý±•‘•µ•¹ÑÍt¡…­¹½Ý±•‘•µ•¹ÑÌ¹µ¤ð•™¥¹•ÌÍ¡…É•ÍÑÉÕÑÕÉ”½¹±äÝ¡•É”Ñ¡”…ÁÁ±¥…‰±”Í½ÕÉ•Ì…É•”ì¥Ð‘½•Ì¹½ÐÍÕÁÁ±ä¹…µ•ÍÁ…”µÍÁ•¥™¥ŒÙ…±Õ•Ì½È•Ù¥”ÍÕÁÁ½ÉÐ¸ð)ðIÕ¹Ñ¥µ”™Õ¹Ñ¥½¹…°½¹ÑÉ½°ðm™Õ¹Ñ¥½¹…°½t ¸¸½™Õ¹Ñ¥½¹…°¼¤ð… ™Õ¹Ñ¥½¹…°]!=€½Ý¹Ì¥ÑÌ½µµ…¹°•Ù•¹Ð°ÍÑ…Ñ”°…‘‘É•ÍÌ°…¹™Õ¹Ñ¥½¹…°µÁÉ½Á•ÉÑäÍ•µ…¹Ñ¥Ì¸IÕ¹Ñ¥µ”½¹ÑÉ½°‘½•Ì¹½Ð‘¥Í½Ù•È„ÁÉ½‘ÕÐµ½‘•°½ÈÁÉ½É…´¥ÑÌÍÑ½É•½¹™¥ÕÉ…Ñ¥½¸µ•É•±ä‰•…ÕÍ”™¥•±‘Ì±½½¬Í¥µ¥±…È¸ð)ð•Ù¥”‘¥Í½Ù•Éäðm•Ù¥”¥Í½Ù•Éåt ¸¸½‘¥…¹½ÍÑ¥Ì½‘•Ù¥”µ‘¥Í½Ù•Éä¹µ¤…¹m‘‘É•ÍÌ¥Í½Ù•Éåt ¸¸½‘¥…¹½ÍÑ¥Ì½…‘‘É•ÍÌµ‘¥Í½Ù•Éä¹µ¤ð¥¹‘Ì½ÈÍ•±•ÑÌ¥¹ÍÑ…±±•A¡åÍ¥…°•Ù¥”¥¹ÍÑ…¹•Ì¸¹Õµ•É…Ñ¥½¸‘½•Ì¹½Ð½¹ÍÑ¥ÑÕÑ”„•Ù¥”¥¹Ñ•ÉÙ¥•Ü¸ð)ð•Ù¥”¥¹Ñ•ÉÙ¥•Üðm•Ù¥”%¹Ñ•ÉÙ¥•Ýt ¸¸½‘¥…¹½ÍÑ¥Ì½‘•Ù¥”µ¥¹Ñ•ÉÙ¥•Ü¹µ¤ðI•…‘Ì¥‘•¹Ñ¥Ñä°Ù•ÉÍ¥½¹Ì°¡•…±Ñ °5½‘Õ±•Ì°=‰©•ÑÌ°…¹…‘‘É•ÍÍ•ÌÉ•Á½ÉÑ•™½È½¹”Í•±•Ñ•A¡åÍ¥…°•Ù¥”¸%Ð‘½•Ì¹½Ð‰ä¥ÑÍ•±˜ÁÉ½Ù¥‘”•Ù•Éä‘•Ñ…¥±•½¹™¥ÕÉ…Ñ¥½¸Ù…±Õ”¸ð)ð•Ñ…¥±•½¹™¥ÕÉ…Ñ¥½¸É•…‘¥¹œðm%59M%=8€ÌÕ€è½¹™¥ÕÉ…Ñ¥½¸A…É…µ•Ñ•ÉÍt ¸¸½‘¥…¹½ÍÑ¥Ì½‘¥´ÌÔµ½¹™¥ÕÉ…Ñ¥½¸¹µ¤ðI•…‘ÌÑ¡”‘¥…¹½ÍÑ¥ŒÁÉ½©•Ñ¥½¸½˜¥¹‘•á•½¹™¥ÕÉ…Ñ¥½¸Ý¡•É”Ñ¡”Ñ…É•ÐÍÕÁÁ½ÉÑÌÑ¡”½Á•É…Ñ¥½¸¸Q¡”Õ¹É•Í½±Ù•%59M%=8€Ìá€•™™•Ð‰½Õ¹‘…ÉäÉ•µ…¥¹ÌÁ…ÉÐ½˜Ñ¡¥ÌÑÉ•…Ñµ•¹Ð¸ð)ðAÉ½É…µµ¥¹œðmÁÉ½É…µµ¥¹œ½t ¸¸½ÁÉ½É…µµ¥¹œ¼¤ðI•ÅÕ•ÍÑÌÍÑ½É•½¹™¥ÕÉ…Ñ¥½¸¡…¹•ÌÑ¡É½Õ Ñ¡”…ÁÁ±¥…‰±”µ…¹…•µ•¹ÐÝ½É­™±½Ü¸•ÁÑ…¹”½˜„É•ÅÕ•ÍÐ¥Ì‘¥ÍÑ¥¹Ð™É½´‘¥…¹½ÍÑ¥ŒÙ•É¥™¥…Ñ¥½¸½˜•™™•Ñ¥Ù”ÍÑ…Ñ”¸ð)ð…Ñ…±½Õ”…Á…‰¥±¥Ñäðm‘•Ù¥”µµ½‘•°½t ¸¸½‘•Ù¥”µµ½‘•°¼¤ð•ÍÉ¥‰•ÌÁÉ½‘ÕÑÌ°™¥ÉµÝ…É”‘•™¥¹¥Ñ¥½¹Ì°Á½ÍÍ¥‰±”5½‘Õ±•Ì°=‰©•ÑÌ°…¹½¹ÍÑÉ…¥¹ÑÌ¸…Ñ…±½Õ”…Á…‰¥±¥Ñä¥Ì¹½Ð¥¹ÍÑ…±±•ÉÕ¹Ñ¥µ”ÍÑ…Ñ”¸ð)ðMÕ¥Ñ”¥µÁ±•µ•¹Ñ…Ñ¥½¸ðm¥¹Ñ•É¹…±Ì½t ¸¸½¥¹Ñ•É¹…±Ì¼¤…¹mÍ•¹…É¥¼µ•¹¥¹”½t ¸¸½Í•¹…É¥¼µ•¹¥¹”¼¤ð•ÍÉ¥‰•Ì¥µÁ±•µ•¹Ñ…Ñ¥½¸…ÉÑ¥™…ÑÌ…¹…ÁÁ±¥…Ñ¥½¸…Á…‰¥±¥ÑäÝ¥Ñ¡¥¸Ñ¡•¥È‘•µ½¹ÍÑÉ…Ñ•Ù•ÉÍ¥½¹Ìì¥Ð¥Ì¹½ÐÕ¹¥Ù•ÉÍ…°ÁÉ½Ñ½½°‰•¡…Ù¥½È¸ð()Q¡•Í”±…å•ÉÌ…¸Á…ÉÑ¥¥Á…Ñ”¥¸½¹”Ý½É­™±½ÜÝ¥Ñ¡½ÕÐ‰•½µ¥¹œÑ¡”Í…µ”µ•¡…¹¥Í´¸½È•á…µÁ±”°‘¥Í½Ù•Éä…¸Í•±•Ð„A¡åÍ¥…°•Ù¥”™½È¥¹Ñ•ÉÙ¥•Ü°¥¹Ñ•ÉÙ¥•Ü…¸•ÍÑ…‰±¥Í Ñ¡”5½‘Õ±”½=‰©•Ð½¹Ñ•áÐ¹••‘•™½È„½¹™¥ÕÉ…Ñ¥½¸É•…°ÁÉ½É…µµ¥¹œ…¸É•ÅÕ•ÍÐ„¡…¹”°…¹„¹•Ü¥¹Ñ•ÉÙ¥•Ü…¸Ù•É¥™ä•™™•Ñ¥Ù”ÍÑ…Ñ”¸((ŒŒŒ%¹Ñ•É™…”…¹Ù…É¥…¹Ð…ÁÁ±¥…‰¥±¥Ñä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀàéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€°é¥‰••€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€°ÍÁ•¥™¥…Ñ¥½¹€()=Á•¹]•‰9•Ð™É…µ”‘•±¥µ¥Ñ•ÉÌ½È„Í¡…É•]!=€¹Õµ‰•È‘¼¹½Ð•ÍÑ…‰±¥Í Ñ¡…ÐÑÝ¼¥¹Ñ•É™…•ÌÕÍ”Ñ¡”Í…µ”Í•ÍÍ¥½¹Ì°]!I€É…µµ…È°…­¹½Ý±•‘•µ•¹Ð‰•¡…Ù¥½È°½Á•É…Ñ¥½¹Ì°½È•Ù¥”ÍÕÁÁ½ÉÐ¸()Q¡”MLµ½É¥•¹Ñ•ÁÕ‰±¥ŒÉ•™•É•¹•Ì…¹5å!=5MÕ¥Ñ”µ…¹…•µ•¹Ð‘…Ñ„ÍÕÁÁ½ÉÐµÕ ½˜Ñ¡”½µµ½¸…¹µ…¹…•µ•¹Ð‘½Õµ•¹Ñ…Ñ¥½¸¸Q¡”ÍÕÁÁ±¥•i¥	•”ÍÁ•¥™¥…Ñ¥½¸‘•ÍÉ¥‰•Ì„Í•Á…É…Ñ”Í•É¥…°¥¹Ñ•É™…”Ý¥Ñ ÁÉ½‘ÕÐ½Õ¹¥Ð…‘‘É•ÍÍ¥¹œ°¥¹Ñ•É™…”µÍÁ•¥™¥Œ…­¹½Ý±•‘•µ•¹Ð‰•¡…Ù¥½È°]!<€ÄÀÀÁ€‘¥Í½Ù•Éä°…¹Í•Á…É…Ñ”µ…¹…•µ•¹Ð…¹‰¥¹‘¥¹œÍÕÉ™…•Ì¸%ÑÌÉ½ÍÌµÕÑÑ¥¹œ…ÁÁ±¥…‰¥±¥Ñä¥Ì…¹½¹¥…°½¸Ñ¡”mi¥	•”%¹Ñ•É™…•t¡é¥‰•”µ¥¹Ñ•É™…”¹µ¤ì½Á•É…Ñ¥½¸Í•µ…¹Ñ¥Ì‰•±½¹œÕ¹‘•ÈÑ¡”É•±•Ù…¹Ð™Õ¹Ñ¥½¹…°]!=€½Èµ•¡…¹¥Í´Á…”Ý¡•¸•Ù¥‘•¹”ÍÕÁÁ½ÉÑÌÑ¡•´¸((ŒŒŒ¹Ñ¥Ñä…¹¥‘•¹Ñ¥Ñä‰½Õ¹‘…É¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀàéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°Í½ÕÉ•€()Q¡”…¹½¹¥…°•Ù¥”¡¥•É…É¡ä¥Ì‘•™¥¹•¥¸Ñ¡”m•Ù¥”5½‘•±t ¸¸½‘•Ù¥”µµ½‘•°¼¤¸Q¡”™½±±½Ý¥¹œÝ¥É”…¹…Ñ…±½Õ”¥‘•¹Ñ¥Ñ¥•ÌÉ•µ…¥¸‘¥ÍÑ¥¹Ðè()ð½¹•ÁÐðI½±”ð…¹½¹¥…°‰½Õ¹‘…Éäð)ð€´´´ð€´´´ð€´´´ð)ð…Ñ…±½Õ”•Ù¥”É•½É…¹M-Tð•ÍÉ¥‰•Ì„ÁÉ½‘ÕÐµ½‘•°½™™•É•‰äÑ¡”…Ñ…±½Õ”ð9½Ð…¸¥¹ÍÑ…±±•A¡åÍ¥…°•Ù¥”%½ÈÁÉ½Ñ½½°…‘‘É•ÍÌð)ðA¡åÍ¥…°•Ù¥”ð=¹”¥¹ÍÑ…±±•¡…É‘Ý…É”ÁÉ½‘ÕÐ¥¹ÍÑ…¹”ð…¸•áÁ½Í”Í•Ù•É…°5½‘Õ±•Ì°=‰©•ÑÌ°…¹™Õ¹Ñ¥½¹…°…‘‘É•ÍÍ•Ìð)ð%¹ÍÑ…±±••Ù¥”%ðM•±•ÑÌ½È¥‘•¹Ñ¥™¥•Ì…¸¥¹ÍÑ…±±•¥¹ÍÑ…¹”¥¸ÍÕÁÁ½ÉÑ•µ…¹…•µ•¹ÐÝ½É­™±½ÝÌð9½Ð9}Y%¹¥‘}‘•Ù¥•€°„M-T°…¸=‰©•Ð¹Õµ‰•È°½È„™Õ¹Ñ¥½¹…°…‘‘É•ÍÌð)ð¥…¹½ÍÑ¥Œ]!I€ðM•±•ÑÌ½È½¹Ñ•áÑÕ…±¥é•Ì„µ…¹…•µ•¹ÐÉ•ÍÁ½¹Í”…½É‘¥¹œÑ¼¥ÑÌ‘¥…¹½ÍÑ¥Œ™…µ¥±äð½•Ì¹½ÐÉ•Á±…”Ñ¡”¥¹ÍÑ…±±••Ù¥”%½È„5½‘Õ±”Ì½¹™¥ÕÉ•…‘‘É•ÍÌð)ðÕ¹Ñ¥½¹…°]!I€ðM•±•ÑÌ„ÉÕ¹Ñ¥µ”Ñ…É•Ð…½É‘¥¹œÑ¼½¹”™Õ¹Ñ¥½¹…°]!=€…¹¥¹Ñ•É™…”Ù…É¥…¹Ðð9½Ð„Õ¹¥Ù•ÉÍ…°A¡åÍ¥…°•Ù¥”¥‘•¹Ñ¥Ñäð)ð5½‘Õ±”…¹Í±½Ñ€ð5½‘Õ±”¥ÌÑ¡”™¥ÉµÝ…É”µ•áÁ½Í•±½¥…°½¹Ñ…¥¹•ÈìÍ±½Ñ€¥Ì¥ÑÌ¹Õµ•É¥ŒÁÉ½Ñ½½°½…Ñ…±½Õ”Á½Í¥Ñ¥½¸ð9•¥Ñ¡•È¥Ì„A¡åÍ¥…°•Ù¥”½È…¸=‰©•Ðð)ð=‰©•Ð…¹Y¥É¥¸=‰©•Ðð=‰©•Ð¥Ì„É•Õ±…È½¹™¥ÕÉ•±½¥…°™Õ¹Ñ¥½¸ìY¥É¥¸=‰©•Ð¥Ì„½¹™¥ÕÉ…‰±”…Á…‰¥±¥ÑäÑ•µÁ±…Ñ”…¹¥ÌÑ¡”¥‘•¹Ñ¥ÑäÕÍ•‰ä%59M%=8€ÌÁ€Ý¡¥±”„5½‘Õ±”¥Ì‘¥Í…‰±•ðQ¡•¥È•áÑ•É¹…°¹Õµ‰•ÉÌ…¹‘…Ñ…‰…Í”­•åÌÉ•µ…¥¸Í•Á…É…Ñ”¹…µ•ÍÁ…•Ìð)ð½¹™¥ÕÉ…Ñ¥½¸ð%¹ÍÑ…¹”µÍÁ•¥™¥ŒÙ…±Õ•Ì…¹…ÍÍ½¥…Ñ¥½¹Ì¥¹Ñ•ÉÁÉ•Ñ•¥¸É•Í½±Ù••Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°…¹=‰©•Ð½¹Ñ•áÐð½¹™¥ÕÉ…Ñ¥½¸¥¹‘•à¥Ì¹½Ð„™Õ¹Ñ¥½¹…°]!Q€°]!I€°½ÈÍ•¹…É¥¼Á…É…µ•Ñ•Èµ•É•±ä‰•…ÕÍ”Ù…±Õ•Ì½¥¹¥‘”ð()mM½ÕÉ•Ì…¹%‘•¹Ñ¥™¥•È	½Õ¹‘…É¥•Ít ¸¸½‘•Ù¥”µµ½‘•°½Í½ÕÉ•Ìµ…¹µ¥‘•¹Ñ¥™¥•ÉÌ¹µ¤½Ý¹ÌÑ¡”‘•Ñ…¥±•É½ÍÌµÍ½ÕÉ”¹…µ•ÍÁ…”ÉÕ±•Ì¸Õ¹Ñ¥½¹…°Á…•Ì½Ý¸ÉÕ¹Ñ¥µ”Ý¥É”Í•µ…¹Ñ¥ÌìÑ¡”•Ù¥”5½‘•°½Ý¹Ì…Ñ…±½Õ”•¹Ñ¥Ñ¥•Ìì¥…¹½ÍÑ¥Ì½Ý¹ÌÉ•Á½ÉÑ•¥¹ÍÑ…±±•ÍÑ…Ñ”ìAÉ½É…µµ¥¹œ½Ý¹ÌÝÉ¥Ñ”Ý½É­™±½ÝÌ¸((ŒŒŒ…¹½¹¥…°Á±…•µ•¹ÐÉÕ±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀàéÌÀÀÀÀÀÕ€()U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()½µµ½¸Ý¥É”µ•¡…¹¥Ì±¥Ù”Õ¹‘•ÈAÉ½Ñ½½°¸9…µ•ÍÁ…”µÍÁ•¥™¥ŒÉÕ¹Ñ¥µ”‰•¡…Ù¥½È±¥Ù•ÌÕ¹‘•È¥ÑÌ™Õ¹Ñ¥½¹…°]!=€¸¹Ñ¥Ñä‘•™¥¹¥Ñ¥½¹Ì…¹…Ñ…±½Õ”É•±…Ñ¥½¹Í¡¥ÁÌ±¥Ù”Õ¹‘•È•Ù¥”5½‘•°¸¥Í½Ù•Éä°¥¹Ñ•ÉÙ¥•Ü°…¹½¹™¥ÕÉ…Ñ¥½¸É•…‘¥¹œ±¥Ù”Õ¹‘•È¥…¹½ÍÑ¥Ì¸½¹™¥ÕÉ…Ñ¥½¸ÝÉ¥Ñ•Ì±¥Ù”Õ¹‘•ÈAÉ½É…µµ¥¹œ¸()=Ñ¡•ÈÁ…•Ìµ…äÉ•Ñ…¥¸•¹½Õ ±½…°½¹Ñ•áÐÑ¼•áÁ±…¥¸„Ý½É­™±½Ü¸MÕ‰ÍÑ…¹Ñ¥…°‘•™¥¹¥Ñ¥½¹Ì…¹É•™•É•¹”Ñ…‰±•ÌÍ¡½Õ±±¥¹¬Ñ¼Ñ¡•Í”½Ý¹•ÉÌ¸AÉ…Ñ¥…°Õ¥‘•Ìµ…äÉ•Á•…Ð½Á•É…Ñ¥½¹…°µ…Ñ•É¥…°¹••‘•™½È¥¹‘•Á•¹‘•¹Ð•á•ÕÑ¥½¸°‰ÕÐÑ¡•¥È½Á¥•ÌµÕÍÐÁÉ•Í•ÉÙ”Ñ¡”…¹½¹¥…°…ÁÁ±¥…‰¥±¥Ñä…¹Õ¹•ÉÑ…¥¹ÑäÅÕ…±¥™¥…Ñ¥½¹Ì¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÀä()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½Í•ÍÍ¥½¹Ì¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒ½¹¹•Ñ¥½¸…¹M•ÍÍ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀäéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°ÑÁ€()=Á•¹]•‰9•Ð…ÁÁ±¥…Ñ¥½¸™É…µ•Ì…É”•á¡…¹•¥¹Í¥‘”„½¹¹•Ñ¥½¸Ñ¼…¸=Á•¹]•‰9•ÐÍ•ÉÙ•È¸Q¡”ÁÕ‰±¥Œ¥¹ÑÉ½‘ÕÑ¥½¸ÍÁ•¥™¥•ÌQ@Á½ÉÐ€ÈÀÀÀÁ€™½È…¸%@…Ñ•Ý…ä…¹Í•Á…É…Ñ•Ì½¹¹•Ñ¥½¸•ÍÑ…‰±¥Í¡µ•¹Ð¥¹Ñ¼Ñ¡É•”Á¡…Í•Ìè((Ä¸•ÍÑ…‰±¥Í Ñ¡”ÑÉ…¹ÍÁ½ÉÐ½¹¹•Ñ¥½¸ì(È¸¥‘•¹Ñ¥™äÑ¡”É•ÅÕ•ÍÑ•Í•ÍÍ¥½¸…¹°Ý¡•¸É•ÅÕ¥É•°…ÕÑ¡•¹Ñ¥…Ñ”ì(Ì¸•á¡…¹”™É…µ•Ì…½É‘¥¹œÑ¼Ñ¡”Í•±•Ñ•Í•ÍÍ¥½¸¸()Q¡”™É…µ¥¹œ±…¹Õ…”¥ÌÑÉ…¹ÍÁ½ÉÐµ¥¹‘•Á•¹‘•¹Ð¥¸ÁÉ¥¹¥Á±”°‰ÕÐÑ¡”Í•ÍÍ¥½¸Í•±•Ñ½ÉÌ…¹Í•ÅÕ•¹•Ì½¸Ñ¡¥ÌÁ…”‘•ÍÉ¥‰”Ñ¡”ÁÕ‰±¥Í¡•Q@½%@…Ñ•Ý…äÝ½É­™±½Ü¸((ŒŒŒ%¹¥Ñ¥…°Í•ÉÙ•È…­¹½Ý±•‘•µ•¹Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀäéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÑÁ€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€°µÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()™Ñ•È…•ÁÑ¥¹œ„Q@½¹¹•Ñ¥½¸°Ñ¡”Í•ÉÙ•ÈÍ•¹‘Ì€¨Œ¨ÄŒ€¸Q¡”±¥•¹ÐµÕÍÐÉ••¥Ù”Ñ¡¥Ì¥¹¥Ñ¥…°-€‰•™½É”Í•±•Ñ¥¹œ„Í•ÍÍ¥½¸¸()ðM•ÍÍ¥½¸ðM•±•Ñ½Èð¥É•Ñ¥½¸…™Ñ•ÈÍ•ÑÕÀðAÕÉÁ½Í”ð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð½µµ…¹‘Ì½…Ñ¥½¹Ìð€¨ää¨äŒ€ðAÉ¥µ…É¥±ä±¥•¹ÐÑ¼Í•ÉÙ•È°Ý¥Ñ É•Á±¥•ÌðM•¹½µµ…¹‘ÌìÉ•ÅÕ•ÍÐÍÑ…ÑÕÌ½È%59M%=9€Ù…±Õ•ÌìÝÉ¥Ñ”ÍÕÁÁ½ÉÑ•%59M%=9€Ù…±Õ•Ìð)ðÙ•¹ÑÌð€¨ää¨ÄŒ€ðM•ÉÙ•ÈÑ¼±¥•¹ÐðI••¥Ù”…Íå¹¡É½¹½ÕÌ‰ÕÌ•Ù•¹ÑÌ…¹ÁÉ½Á•ÉÑäÉ•Á½ÉÑÌð)ðAÉ½É…µµ•Í•¹…É¥¼ð€¨ää¨ÀŒ€ðM•ÉÙ•ÈÑ¼±¥•¹Ð¥¸Ñ¡”ÁÕ‰±¥Í¡••á…µÁ±”ð½ÉÝ…ÉÑÉ…™™¥ŒÝ¡¥±”ÁÉ½É…µµ¥¹œ…¸ÐÈÀ¼ÀÌÔÔÄÍ•¹…É¥¼µ½‘Õ±”¥¸½¹™¥ÕÉ…Ñ¥½¸µ½‘”ð()™Ñ•ÈÑ¡”Í•±•Ñ½È°Ñ¡”Í•ÉÙ•È…¸…•ÁÐ…¸½Á•¸µÉ…¹”½¹¹•Ñ¥½¸Ý¥Ñ €¨Œ¨ÄŒ€°Í•¹„±•…ä¡…±±•¹”°½È‘•±…É”!5Ý¥Ñ €¨äà¨ÄŒ€½È€¨äà¨ÈŒ€¸¼¹½ÐÉ•ÅÕ¥É”„Í•Á…É…Ñ”Í•±•Ñ½È-€‰•™½É”…•ÁÑ¥¹œ…¸…ÕÑ¡•¹Ñ¥…Ñ¥½¸™É…µ”èÑ¡”!5ÍÁ•¥™¥…Ñ¥½¸Í¡½ÝÌÑ¡”‘•±…É…Ñ¥½¸¥µµ•‘¥…Ñ•±ä…™Ñ•ÈÑ¡”±¥•¹ÐÍ•±•Ñ½È¸9½Éµ…°ÑÉ…™™¥Œ‰•¥¹Ì½¹±ä…™Ñ•ÈÑ¡”Í•±•Ñ•Í•ÑÕÀÁ…Ñ ½µÁ±•Ñ•Ì¸()Q¡•Í”Í•±•Ñ½ÉÌ‰•±½¹œÑ¼½¹¹•Ñ¥½¸Í•ÑÕÀ¸Q¡•ä…É”¹½Ð™Õ¹Ñ¥½¹…°]!<€äå€½µµ…¹‘Ì…¹µÕÍÐ¹½Ð‰”™•Ñ¼Ñ¡”½É‘¥¹…Éä™Õ¹Ñ¥½¹…°µ™É…µ”‘¥ÍÁ…Ñ¡•È¸((ŒŒŒ½µµ…¹‘Ì½…Ñ¥½¹ÌÍ•ÍÍ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀäéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€()Q¡”½µµ…¹‘Ì½…Ñ¥½¹ÌÍ•ÍÍ¥½¸¥ÌÉ•ÅÕ•ÍÐµ½É¥•¹Ñ•¸±¥•¹Ð…¸Í•¹½µµ…¹™É…µ•Ì°ÍÑ…ÑÕÌÉ•ÅÕ•ÍÑÌ°%59M%=9€É•ÅÕ•ÍÑÌ°…¹ÍÕÁÁ½ÉÑ•%59M%=9€ÝÉ¥Ñ•Ì¸()½µµ…¹½ÈÝÉ¥Ñ”¹½Éµ…±±äÉ••¥Ù•Ì-€½È9-€¸ÍÑ…ÑÕÌ½È%59M%=9€É•ÅÕ•ÍÐ…¸ÁÉ½‘Õ”½¹”½Èµ½É”É•ÍÕ±Ð™É…µ•Ì™½±±½Ý•‰ä„Ñ•Éµ¥¹…Ñ¥¹œ…­¹½Ý±•‘•µ•¹Ð¸M•”m­¹½Ý±•‘•µ•¹ÑÍt¡…­¹½Ý±•‘•µ•¹ÑÌ¹µ¤¸()¼¹½Ð…ÍÍÕµ”½¹”É•ÍÁ½¹Í”™É…µ”Á•ÈÉ•ÅÕ•ÍÐ¸Q¡”Í•±•Ñ•]!I€°…Ñ•Ý…ä°…¹™Õ¹Ñ¥½¹…°ÍåÍÑ•´…¸…ÕÍ”„É•ÅÕ•ÍÐÑ¼•áÁ…¹¥¹Ñ¼µÕ±Ñ¥Á±”É•Á½ÉÑÌ¸((ŒŒŒÙ•¹ÑÌÍ•ÍÍ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀäéÌÀÀÀÀÀÑ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()™Ñ•È€¨ää¨ÄŒ€¥Ì…•ÁÑ•°Ñ¡”Í•ÉÙ•È™½ÉÝ…É‘Ì…Íå¹¡É½¹½ÕÌ=Á•¹]•‰9•ÐÑÉ…™™¥Œ¸Q¡”ÁÕ‰±¥Í¡••á…µÁ±”¥¹±Õ‘•Ì½É‘¥¹…Éä½µµ…¹½ÍÑ…ÑÕÌ™É…µ•Ì™É½´µ½É”Ñ¡…¸½¹”]!=€ìÑ¡”½¹¹•Ñ¥½¸¥ÌÑ¡•É•™½É”„‰ÕÌµ•Ù•¹ÐÍÑÉ•…´°¹½Ð„ÍÕ‰ÍÉ¥ÁÑ¥½¸Ñ¼½¹”™Õ¹Ñ¥½¹…°¹…µ•ÍÁ…”¸()¸•Ù•¹Ð½¹¹•Ñ¥½¸¥Ì•¹•É…±±ä±½¹œµ±¥Ù•¸±¥•¹ÐÍ¡½Õ±Á…ÉÍ”Ñ¡”‰åÑ”ÍÑÉ•…´¥¹É•µ•¹Ñ…±±ä°ÁÉ•Í•ÉÙ”…ÉÉ¥Ù…°½É‘•È°Ñ½±•É…Ñ”µÕ±Ñ¥Á±”½µÁ±•Ñ”™É…µ•Ì¥¸½¹”ÑÉ…¹ÍÁ½ÉÐÉ•…°É•Ñ…¥¸]!=€µÍÁ•¥™¥ŒÁ…ÉÍ¥¹œ™½È•… •µ¥ÑÑ•™É…µ”°…¹É•½¹¹•Ð…¹É•Á•…ÐÍ•ÍÍ¥½¸Í•±•Ñ¥½¸…™Ñ•ÈÑÉ…¹ÍÁ½ÉÐ™…¥±ÕÉ”¸()Q¡”ÁÕ‰±¥Œ¥¹ÑÉ½‘ÕÑ¥½¸‘½•Ì¹½Ð‘•™¥¹”Á•Èµ]!=€ÍÕ‰ÍÉ¥ÁÑ¥½¸™¥±Ñ•ÉÌ½È‘•±¥Ù•ÉäÕ…É…¹Ñ••Ì¸%µÁ±•µ•¹Ñ…Ñ¥½¹ÌµÕÍÐ¹½Ð¥¹™•ÈÑ¡•´¸((ŒŒŒAÉ½É…µµ•Í•¹…É¥¼Í•ÍÍ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀäéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()Q¡”Í•±•Ñ½È€¨ää¨ÀŒ€¥Ì‘½Õµ•¹Ñ•™½ÈÁÉ½É…µµ¥¹œ…¸ÐÈÀ€¡	Q¥¥¹¼¤½È€ÀÌÔÔÄ€¡1•É…¹¤Í•¹…É¥¼µ½‘Õ±”Ñ¡É½Õ Ñ¡•É¹•ÐÝ¡¥±”Ñ¡…Ðµ½‘Õ±”¥Ì¥¸½¹™¥ÕÉ…Ñ¥½¸µ½‘”¸()Q¡¥Ì¥Ì„ÍÁ•¥…±¥é•…Ñ•Ý…äÍ•ÍÍ¥½¸¸%Ð¥Ì‘¥ÍÑ¥¹Ð™É½´™Õ¹Ñ¥½¹…°Í•¹…É¥¼…Ñ¥Ù…Ñ¥½¸Ñ¡É½Õ ]!<€Á€°Í•¹…É¥¼µ…¹…•µ•¹ÐÑ¡É½Õ ]!<€ÄÝ€°Ñ¡”5å!=5MÕ¥Ñ”Í•¹…É¥¼•¹¥¹”°…¹‘¥…¹½ÍÑ¥Œ½È•Ù¥”µÁÉ½É…µµ¥¹œÝ½É­™±½ÝÌ¸()Q¡”ÁÕ‰±¥ŒÍ½ÕÉ”¥Ù•ÌÑ¡”Í•ÍÍ¥½¸‰½Õ¹‘…Éä…¹Í•±•Ñ½È‰ÕÐ¹½Ð„•¹•É…°µÁÕÉÁ½Í”ÁÉ½É…µµ¥¹œA$¸Q¡”™Õ¹Ñ¥½¹…°ÐÈÀ™É…µ•Ì…É”‘½Õµ•¹Ñ•Õ¹‘•Èm]!<€Át ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´ÀµÍ•¹…É¥½Ì¼¤¸((ŒŒŒÕÑ¡•¹Ñ¥…Ñ¥½¸‰É…¹ ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀäéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€()…Ñ•Ý…ä…¸…±±½Ü½¹™¥ÕÉ•±¥•¹Ð%@…‘‘É•ÍÍ•ÌÑ¼½¹¹•ÐÝ¥Ñ¡½ÕÐ…¸=A8Á…ÍÍÝ½É¸=Ñ¡•ÉÝ¥Í”°Í•ÍÍ¥½¸Í•±•Ñ¥½¸¥Ì™½±±½Ý•‰ä•¥Ñ¡•ÈÑ¡”±•…ä=A8¡…±±•¹”µÉ•ÍÁ½¹Í”…±½É¥Ñ¡´½ÈÑ¡”‘•±…É•!5Ý½É­™±½Ü¸()ÕÑ¡•¹Ñ¥…Ñ¥½¸•ÍÑ…‰±¥Í¡•Ì±¥•¹Ð…•ÍÌì¥Ð‘½•Ì¹½Ð•¹ÉåÁÐ±…Ñ•È=Á•¹]•‰9•ÐÑÉ…™™¥Œ¸M•”mÕÑ¡•¹Ñ¥…Ñ¥½¹t¡…ÕÑ¡•¹Ñ¥…Ñ¥½¸¹µ¤¸((ŒŒŒMÑ…Ñ”µµ…¡¥¹”É•ÅÕ¥É•µ•¹ÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀäéÌÀÀÀÀÀÝ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€()É½‰ÕÍÐ±¥•¹ÐÍ¡½Õ±•áÁ±¥¥Ñ±äµ½‘•°Ñ¡•Í”ÍÑ…Ñ•Ìè()ðMÑ…Ñ”ð•ÁÑ•¥¹ÁÕÐð)ð€´´´ð€´´´ð)ðÝ…¥Ñ¥¹œÍ•ÉÙ•ÈÉ••Ñ¥¹œð%¹¥Ñ¥…°-€ð)ðÝ…¥Ñ¥¹œÍ•ÍÍ¥½¸É•ÍÕ±Ðð=Á•¸µÉ…¹”-€°±•…ä¡…±±•¹”°!5‘•±…É…Ñ¥½¸°9-€°½È½¹¹•Ñ¥½¸±½Í”ð)ðÕÑ¡•¹Ñ¥…Ñ¥¹œðÉ…µ•Ì‰•±½¹¥¹œÑ¼Ñ¡”¹•½Ñ¥…Ñ•…ÕÑ¡•¹Ñ¥…Ñ¥½¸µ•Ñ¡½ð)ðÑ¥Ù”½µµ…¹Í•ÍÍ¥½¸ðI•ÅÕ•ÍÑÌÁ±ÕÌÑ¡•¥ÈÉ•ÍÕ±ÐÍ•ÅÕ•¹•Ìð)ðÑ¥Ù”•Ù•¹ÐÍ•ÍÍ¥½¸ðÍå¹¡É½¹½ÕÌ=Á•¹]•‰9•Ð™É…µ•Ìð)ð±½Í•½™…¥±•ðI•½¹¹•Ð™É½´Ñ¡”ÑÉ…¹ÍÁ½ÉÐ±…å•Èð()¼¹½ÐÑÉ•…Ð•Ù•Éä-€…Ì•ÅÕ¥Ù…±•¹Ð¸%ÑÌÉ½±”¥Ì‘•Ñ•Éµ¥¹•‰äÑ¡”ÕÉÉ•¹ÐÍÑ…Ñ”èÉ••Ñ¥¹œ°Í•±•Ñ½È…•ÁÑ…¹”°…ÕÑ¡•¹Ñ¥…Ñ¥½¸É•ÍÕ±Ð°½Á•É…Ñ¥½¸É•ÍÕ±Ð°½È•¹µ½˜µÍ•ÅÕ•¹”µ…É­•È¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÀäéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°ÑÁ€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”Í•ÍÍ¥½¸Í•±•Ñ½ÉÌ°Q@Á½ÉÐ°…¹‰…Í¥ŒÍ•ÅÕ•¹•Ì½µ”™É½´m=Á•¹]•‰9•Ð%¹ÑÉ½‘ÕÑ¥½¸ÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=]9}%¹ÑÉ½}9¹Á‘˜¤°Á…•Ì€ÛŠLÄÀ¸!5¹•½Ñ¥…Ñ¥½¸¥ÌÍÁ•¥™¥•Í•Á…É…Ñ•±ä¥¸m!µ…ŒÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½!µ…Œ¹Á‘˜¤¸=‰Í•ÉÙ•…Ñ•Ý…ä‰•¡…Ù¥½È…¸É•™¥¹”½µÁ…Ñ¥‰¥±¥Ñä¡…¹‘±¥¹œ°‰ÕÐÍ¡½Õ±¹½ÐÍ¥±•¹Ñ±äÉ•Á±…”Ñ¡•Í”ÁÕ‰±¥Í¡•Í•ÅÕ•¹•Ì¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄÀ()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½ÍÑÉ•…´µÁ…ÉÍ¥¹œ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒMÑÉ•…´A…ÉÍ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÀÅ€()=Á•¹]•‰9•Ð™É…µ•Ì…É”…ÁÁ±¥…Ñ¥½¸µ•ÍÍ…•Ì…ÉÉ¥•½Ù•È„ÑÉ…¹ÍÁ½ÉÐÍÑÉ•…´¸ÑÉ…¹ÍÁ½ÉÐÉ•…¥Ì¹½Ð„™É…µ”‰½Õ¹‘…Éäè½¹”É•……¸½¹Ñ…¥¸Á…ÉÐ½˜„™É…µ”°•á…Ñ±ä½¹”™É…µ”°½ÈÍ•Ù•É…°½¹Í•ÕÑ¥Ù”™É…µ•Ì¸()Á…ÉÍ•ÈÍ¡½Õ±½¹ÍÕµ”‰åÑ•Ì¥¹É•µ•¹Ñ…±±ä…¹•µ¥Ð„™É…µ”½¹±ä…™Ñ•ÈÑ¡”Ñ•Éµ¥¹…Ñ¥¹œ€Œ€¡…Ì‰••¸É••¥Ù•¸((ŒŒŒ¡…É…Ñ•ÈÍ•Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÀÉ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”¥¹ÑÉ½‘ÕÑ½ÉäÍÁ•¥™¥…Ñ¥½¸‘•™¥¹•Ì½É‘¥¹…Éä=Á•¹]•‰9•Ð™É…µ•ÌÕÍ¥¹œ‘•¥µ…°‘¥¥ÑÌ€À¸¸å€°€©€°…¹€€¸™É…µ”‰•¥¹ÌÝ¥Ñ €©€…¹•¹‘ÌÝ¥Ñ €Œ€¸5…©½ÈÑ…Ì…É”Í•Á…É…Ñ•‰ä€©€¸Ñ…œ…¸½¹Ñ…¥¸‘•¥µ…°‘¥¥ÑÌ…¹€€°…¹•µÁÑäÑ…Ì…É”Á•Éµ¥ÑÑ•¸()¼¹½Ð…ÁÁ±äÑ¡¥Ì½É‘¥¹…Éäµ™É…µ”…±Á¡…‰•Ð‰±¥¹‘±äÑ¼½Ñ¡•ÈÑÉ…¹ÍÁ½ÉÐ±…å•ÉÌ½ÈÙ•¹‘½È•áÑ•¹Í¥½¹Ì¸Y…±¥‘…Ñ”…ÐÑ¡”±…å•ÈÝ¡½Í”É…µµ…È¥Ì‰•¥¹œÁ…ÉÍ•¸((ŒŒŒ%¹É•µ•¹Ñ…°…±½É¥Ñ¡´()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÀÍ€((Ä¸¥¹€©€…ÌÑ¡”ÍÑ…ÉÐ½˜„…¹‘¥‘…Ñ”™É…µ”¸(È¸ÁÁ•¹ÍÕ‰Í•ÅÕ•¹Ð‰åÑ•ÌÑ¼„‰½Õ¹‘•‰Õ™™•È¸(Ì¸]¡•¸Ñ¡”‰Õ™™•È•¹‘Ì¥¸€Œ€°•µ¥ÐÑ¡”½µÁ±•Ñ”É…Ü™É…µ”¸(Ð¸½¹Ñ¥¹Õ”Ý¥Ñ ‰åÑ•ÌÉ•µ…¥¹¥¹œ¥¸Ñ¡”Í…µ”ÑÉ…¹ÍÁ½ÉÐÉ•…¸(Ô¸=¸±•¹Ñ °¡…É…Ñ•È°½ÈÑ¥µ•½ÕÐ™…¥±ÕÉ”°‘¥…¹½Í”Ñ¡”µ…±™½Éµ•…¹‘¥‘…Ñ”…¹É•Íå¹¡É½¹¥é”…ÐÑ¡”¹•áÐÁ±…ÕÍ¥‰±”€©€¸()AÉ•Í•ÉÙ”Ñ¡”•á…ÐÉ…Ü™É…µ”¸9Õµ•É¥Œ½¹Ù•ÉÍ¥½¸‰•±½¹ÌÑ¼±…Ñ•ÈÍ•µ…¹Ñ¥Œ‘•½‘¥¹œ¸((ŒŒŒA…ÉÍ¥¹œ±…å•ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÀÑ€()ð1…å•ÈðI•ÍÁ½¹Í¥‰¥±¥Ñäð)ð€´´´ð€´´´ð)ðMÑÉ•…´™É…µ¥¹œð¥¹Ñ¡”±•…‘¥¹œ€©€…¹Ñ•Éµ¥¹…Ñ¥¹œ€Œ€ð)ðQ…œÑ½­•¹¥é…Ñ¥½¸ðMÁ±¥Ðµ…©½È™¥•±‘Ì½¸€©€Ý¡¥±”ÁÉ•Í•ÉÙ¥¹œ•µÁÑä™¥•±‘Ìð)ðÉ…µ”µ™…µ¥±äÉ•½¹¥Ñ¥½¸ð¥ÍÑ¥¹Õ¥Í …­¹½Ý±•‘•µ•¹Ð°Í•ÍÍ¥½¸°½µµ…¹½ÍÑ…ÑÕÌ°É•ÅÕ•ÍÐ°É•ÍÁ½¹Í”°…¹ÝÉ¥Ñ”™½ÉµÌð)ð¥•±É…µµ…ÈðA…ÉÍ”Á…É…µ•Ñ•É¥é•]!Q€°]!I€°½È%59M%=9€Í•±•Ñ½ÉÌð)ðMåÍÑ•´Í•µ…¹Ñ¥Ìð%¹Ñ•ÉÁÉ•ÐÙ…±Õ•Ì½¹±ä…™Ñ•ÈÉ•Í½±Ù¥¹œ]!=€ð)ð…Á…‰¥±¥ÑäÙ…±¥‘…Ñ¥½¸ð¡•¬Ý¡•Ñ¡•ÈÑ¡”Ñ…É•Ð•Ù¥”½=‰©•ÐÍÕÁÁ½ÉÑÌÑ¡”½Á•É…Ñ¥½¸ð()Q¡¥Ì½É‘•ÈÁÉ•Ù•¹ÑÌ•ÉÉ½ÉÌÍÕ …Ì½¹Ù•ÉÑ¥¹œ„]!I€Ñ¼…¸¥¹Ñ••È‰•™½É”ÁÉ•Í•ÉÙ¥¹œ±•…‘¥¹œé•É½•Ì½ÈÍÁ±¥ÑÑ¥¹œ•Ù•Éä€€…ÌÑ¡½Õ ¥Ð¡…½¹”±½‰…°É½±”¸((ŒŒŒµÁÑäÑ…Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€()Q¡”…¹½¹¥…°Íå¹Ñ…àÁ•Éµ¥ÑÌ½µ¥ÑÑ•Ñ…Ì¸µÁÑä™¥•±‘Ì…É”Í¥¹¥™¥…¹Ð¥¸™É…µ•ÌÍÕ …Ì…Ñ•Ý…äµµ…¹…•µ•¹ÐÉ•ÅÕ•ÍÑÌÝ¡•É”]!I€¥Ì¥¹Ñ•¹Ñ¥½¹…±±ä•µÁÑä¸()½È•á…µÁ±”°Ñ½­•¹¥é¥¹œ€¨ŒÄÌ¨¨ÄŒ€µÕÍÐÉ•Ñ…¥¸Ñ¡”•µÁÑä™¥•±‰•ÑÝ••¸Ñ¡”ÑÝ¼€©€‘•±¥µ¥Ñ•ÉÌ¸I•µ½Ù¥¹œ•µÁÑäÍÑÉ¥¹ÌÍ¡¥™ÑÌ%59M%=8€Å€¥¹Ñ¼Ñ¡”ÝÉ½¹œÁ½Í¥Ñ¥½¸¸((ŒŒŒA…É…µ•Ñ•ÈÍ•Á…É…Ñ½ÉÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÀÙ€()€€¥Ì¥¹Ñ•ÉÁÉ•Ñ•¥¹Í¥‘”Ñ¡”É…µµ…È½˜¥ÑÌ•¹±½Í¥¹œ™¥•±¸%Ð…¸…ÁÁ•…È¥¸„Á…É…µ•Ñ•É¥é•]!Q€°„ÅÕ…±¥™¥•]!I€°„ÝÉ¥Ñ”Í•±•Ñ½ÈÍÕ …Ì€%59M%=9€°½È„Á…É…µ•Ñ•É¥é•‘¥…¹½ÍÑ¥ŒÍ•±•Ñ½ÈÍÕ …Ì€ÌÈM1=Q€¸%Ð¥Ì¹½Ð„Õ¹¥Ù•ÉÍ…°Í•Á…É…Ñ½È…ÐÑ¡”™É…µ”µÑ½­•¹¥é…Ñ¥½¸±…å•È¸((ŒŒŒI•ÅÕ•ÍÐ½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)…ÕÑ¥½¹Ìè…Ù½¥‘€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()½µµ…¹½¹¹•Ñ¥½¸…¸É••¥Ù”„Í¥¹±”…­¹½Ý±•‘•µ•¹Ð°½¹”½Èµ½É”É•ÍÕ±Ð™É…µ•Ì™½±±½Ý•‰ä-€°½ÈÁÉ½Ù¥Í¥½¹…°™É…µ•Ì™½±±½Ý•‰ä9-€¸()	•…ÕÍ”Ñ¡”ÁÕ‰±¥ŒÁÉ½Ñ½½°‘•™¥¹•Ì¹¼ÑÉ…¹Í…Ñ¥½¸¥‘•¹Ñ¥™¥•È°…Ù½¥½Ù•É±…ÁÁ¥¹œÉ•ÅÕ•ÍÑÌ½¸½¹”½µµ…¹Í•ÍÍ¥½¸Õ¹±•ÍÌÑ¡”…Ñ•Ý…ä…¹½Á•É…Ñ¥½¸•áÁ±¥¥Ñ±äÍÕÁÁ½ÉÐ¥Ð¸=¸„É•ÍÕ±ÐÍ•ÅÕ•¹”Ñ•Éµ¥¹…Ñ•‰ä9-€°Ñ¡”¥¹ÑÉ½‘ÕÑ½ÉäÍÁ•¥™¥…Ñ¥½¸Á•Éµ¥ÑÌÑ¡”±¥•¹ÐÑ¼É•…É•…É±¥•È™É…µ•Ì¥¸Ñ¡…ÐÍ•ÅÕ•¹”…Ì¥¹Ù…±¥¸((ŒŒŒ1¥µ¥ÑÌ…¹É•½Ù•Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè½¹±ä™½É€()Q¡”ÁÕ‰±¥Œ¥¹ÑÉ½‘ÕÑ¥½¸‘½•Ì¹½ÐÍÁ•¥™ä„Õ¹¥Ù•ÉÍ…°µ…á¥µÕ´™É…µ”±•¹Ñ °É•ÅÕ•ÍÐÑ¥µ•½ÕÐ°½ÈÉ•ÍÕ±Ð½Õ¹Ð¸UÍ”½¹™¥ÕÉ…‰±”‘•™•¹Í¥Ù”±¥µ¥ÑÌÉ…Ñ¡•ÈÑ¡…¸¥¹Ù•¹Ñ•ÁÉ½Ñ½½°½¹ÍÑ…¹ÑÌè((´‰½Õ¹Ñ¡”É••¥Ù”‰Õ™™•È…¹¥¹½µÁ±•Ñ”µ™É…µ”±¥™•Ñ¥µ”ì(´¹•Ù•È•á•ÕÑ”„Á…ÉÑ¥…°™É…µ”ì(´É•Ñ…¥¸µ…±™½Éµ•É…Ü¥¹ÁÕÐ½¹±ä™½È½ÁÐµ¥¸‘¥…¹½ÍÑ¥Ìì(´É•‘…Ð…ÕÑ¡•¹Ñ¥…Ñ¥½¸µ…Ñ•É¥…°ì(´±½Í”½ÈÉ•Íå¹¡É½¹¥é”…½É‘¥¹œÑ¼Ñ¡”½¹¹•Ñ¥½¸ÌÑÉÕÍÐ‰½Õ¹‘…Éä¸((ŒŒŒ¹½‘¥¹œµ½‘•°()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÀå€()-••ÀÁÉ½Ñ½½°Ù…±Õ•Ì…ÌÍÑÉ¥¹ÌÕ¹Ñ¥°Ñ¡•¥È™¥•±É…µµ…È¡…Ì‰••¸¥‘•¹Ñ¥™¥•¸Q¡¥ÌÁÉ•Í•ÉÙ•Ì±•…‘¥¹œé•É½•Ì°™¥á•µÝ¥‘Ñ •Ù¥”%Ì°•µÁÑä™¥•±‘Ì°É½ÕÑ¥¹œÅÕ…±¥™¥•ÉÌ°…¹•¹½‘•Ù…±Õ•ÌÑ¡…Ðµ•É•±ä±½½¬‘•¥µ…°¸()=¹±äÑ¡”ÍåÍÑ•´µÍÁ•¥™¥Œ‘•½‘•ÈÍ¡½Õ±•áÁ½Í”ÑåÁ•¥¹Ñ••ÉÌ°Ñ•µÁ•É…ÑÕÉ•Ì°‘ÕÉ…Ñ¥½¹Ì°µ…Í­Ì°½È¥‘•¹Ñ¥™¥•ÉÌ¸((ŒŒŒÙ¥‘•¹”‰…Í¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÀéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÑÁ€)AÉ½Ù•¹…¹”Õ•ÌèÍÁ•¥™¥…Ñ¥½¹€()Q¡”¡…É…Ñ•ÈÍ•Ð°‘•±¥µ¥Ñ•ÉÌ°•µÁÑäµÑ…œÉÕ±”°…¹½µµ½¸™É…µ”™…µ¥±¥•Ì½µ”™É½´m=Á•¹]•‰9•Ð%¹ÑÉ½‘ÕÑ¥½¸ÍÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=]9}%¹ÑÉ½}9¹Á‘˜¤¸Q¡”¥¹É•µ•¹Ñ…°ÑÉ…¹ÍÁ½ÉÐÕ¥‘…¹”¥Ì…¸¥µÁ±•µ•¹Ñ…Ñ¥½¸½¹Í•ÅÕ•¹”½˜‘•±¥µ¥Ñ•Èµ™É…µ•µ•ÍÍ…•Ì½Ù•ÈQ@ì¥Ð¥Ì¥‘•¹Ñ¥™¥•…ÌÁ…ÉÍ•ÈÕ¥‘…¹”É…Ñ¡•ÈÑ¡…¸„ÅÕ½Ñ•ÁÉ½Ñ½½°Õ…É…¹Ñ•”¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄÄ()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½Ý¡…Ð¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒ]!Q€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÄéÌÀÀÀÀÀÅ€()]!Q€¥‘•¹Ñ¥™¥•Ì„½µµ…¹°ÍÑ…Ñ”°½È•Ù•¹ÐÝ¥Ñ¡¥¸…¸=Á•¹]•‰9•Ð]!=€¸()]!Q€Ù…±Õ”¥Ìµ•…¹¥¹™Õ°½¹±ä¥¸Ñ¡”½¹Ñ•áÐ½˜¥ÑÌ]!=€¸Q¡”Í•µ…¹Ñ¥Œ¥‘•¹Ñ¥Ñä½˜…¸½Á•É…Ñ¥½¸¥ÌÑ¡•É•™½É”€¡]!<°]!P¥€°¹½Ð]!Q€…±½¹”¸((ŒŒŒÉ…µ”Á½Í¥Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÄéÌÀÀÀÀÀÉ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€()Q¡”¹½Éµ…°½µµ…¹½ÍÑ…ÑÕÌ™½É´¥Ì€©]!<©]!P©]!IŒ€¸()]!Q€…¸¥¹±Õ‘”Á…É…µ•Ñ•ÉÌ¥¹ÑÉ½‘Õ•Ý¥Ñ €€Ý¡•¸‘•™¥¹•‰äÑ¡”Í•±•Ñ•ÍåÍÑ•´¸A…É…µ•Ñ•ÈÍÑÉÕÑÕÉ”¥ÌÁ…ÉÐ½˜Ñ¡”]!Q€É…µµ…È™½ÈÑ¡…Ð]!=€…¹µÕÍÐ¹½Ð‰”¥¹Ñ•ÉÁÉ•Ñ•±½‰…±±ä¸((ŒŒŒM½Á”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÄéÌÀÀÀÀÀÍ€()AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€()¹Õµ•É¥Œ]!Q€Ù…±Õ”…¸¡…Ù”Õ¹É•±…Ñ•µ•…¹¥¹Ì¥¸‘¥™™•É•¹ÐÍåÍÑ•µÌ¸%µÁ±•µ•¹Ñ…Ñ¥½¹ÌÍ¡½Õ±Ñ¡•É•™½É”É•Í½±Ù”]!=€‰•™½É”¥¹Ñ•ÉÁÉ•Ñ¥¹œ]!Q€¸()MåÍÑ•´µÍÁ•¥™¥Œ]!Q€É•™•É•¹”Ñ…‰±•Ì‰•±½¹œÝ¥Ñ Ñ¡”½ÉÉ•ÍÁ½¹‘¥¹œ™Õ¹Ñ¥½¹…°½È‘¥…¹½ÍÑ¥ŒÍåÍÑ•´‘½Õµ•¹Ñ…Ñ¥½¸É…Ñ¡•ÈÑ¡…¸¥¸„±½‰…°Ù…±Õ”Ñ…‰±”¸((ŒŒŒI•±…Ñ¥½¹Í¡¥ÀÑ¼%59M%=9€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÄéÌÀÀÀÀÀÑ€()]!Q€É•ÁÉ•Í•¹ÑÌ½µµ…¹‘Ì°ÍÑ…Ñ•Ì°…¹•Ù•¹ÑÌ•áÁÉ•ÍÍ•Ñ¡É½Õ Ñ¡”¹½Éµ…°™É…µ”™…µ¥±ä¸AÉ½Á•ÉÑ¥•ÌÉ•…½ÈÝÉ¥ÑÑ•¸Ñ¡É½Õ €¨]!<¸¸¹€™É…µ•Ì…É”¥‘•¹Ñ¥™¥•‰ä%59M%=9€¥¹ÍÑ•…¸M•”m%59M%=9t¡‘¥µ•¹Í¥½¹Ì¹µ¤¸()Q¡”‘¥ÍÑ¥¹Ñ¥½¸¥ÌÍÑÉÕÑÕÉ…°É…Ñ¡•ÈÑ¡…¸ÁÕÉ•±äÍ•µ…¹Ñ¥ŒèÑ¡”Í…µ”É•…°µÝ½É±™Õ¹Ñ¥½¸…¸•áÁ½Í”½µµ…¹‰•¡…Ù¥½ÈÑ¡É½Õ ]!Q€…¹ÍÑ…Ñ”½È½¹™¥ÕÉ…Ñ¥½¸‘…Ñ„Ñ¡É½Õ ½¹”½Èµ½É”%59M%=9€¥‘•¹Ñ¥™¥•ÉÌ¸()M•”mÉ…µ”Må¹Ñ…át¡™É…µ”µÍå¹Ñ…à¹µ¤™½ÈÑ¡”½µµ½¸™É…µ”™½ÉµÌ…¹m‘‘É•ÍÍ¥¹t¡…‘‘É•ÍÍ¥¹œ¹µ¤™½È]!I€¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄÈ()M½ÕÉ”Á…Ñ èÁÉ½Ñ½½°½é¥‰•”µ¥¹Ñ•É™…”¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐèÁÉ½Ñ½½±€)É•„èÁÉ½Ñ½½±€((ŒŒi¥	•”=Á•¹]•‰9•Ð%¹Ñ•É™…”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÙ•ÉÍ¥½¹€°é¥‰••€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡¥ÌÁ…”É•½É‘ÌÑ¡”¥¹Ñ•É™…”µÍÁ•¥™¥Œ‰½Õ¹‘…Éä•ÍÑ…‰±¥Í¡•‰äÑ¡”ÍÕÁÁ±¥•1•É…¹mi¥	•”=Á•¹]•‰9•ÐMÁ•¥™¥…Ñ¥½¹t ¸¸½Í½ÕÉ•Ì½½Á•¹Ý•‰¹•ÐµÁÕ‰±¥Œ½Á‘˜½=Á•¹]•‰9•Ñ}i¥‰•”¹Á‘˜¤°Ù•ÉÍ¥½¸€Ð¸À°€ÈÈ9½Ù•µ‰•È€ÈÀÄØ¸%Ð¥ÌÍÁ•¥™¥…Ñ¥½¸•Ù¥‘•¹”°¹½Ð„Ñ•ÍÑ•¥¹Ñ•É½Á•É…‰¥±¥Ñä±…¥´¸Q¡”‘½Õµ•¹Ð…ÉÉ¥•Ì½¹™¥‘•¹Ñ¥…°™½½Ñ•ÉÌì¥ÑÌÁÕ‰±¥ŒµÉ•±•…Í”ÁÉ½Ù•¹…¹”É•µ…¥¹ÌÕ¹É•Í½±Ù•…ÌÉ•½É‘•¥¸Ñ¡”mM½ÕÉ”µ½Ù•É…”Õ‘¥Ñt ¸¸½ÁÉ½©•Ð½É•Ù¥•Ü½Á¡…Í”´ÌµÍ½ÕÉ”µ½Ù•É…”¹µ¤¸((ŒŒŒQÉ…¹ÍÁ½ÉÐ…¹…‘‘É•ÍÍ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€°ÍÍ€°ÑÁ€°é¥‰••€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€°¹½Ð•Ù¥‘•¹•€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()M•Ñ¥½¸€È¸ÌÍÁ•¥™¥•ÌÍ•É¥…°½µµÕ¹¥…Ñ¥½¸…Ð€ÄäÈÀÀ‰…Õ°•¥¡Ð‘…Ñ„‰¥ÑÌ°½¹”ÍÑ½À‰¥Ð°…¹¹¼Á…É¥Ñä™½ÈÑ¡”‘•ÍÉ¥‰•¥¹Ñ•É™…•Ì¸Q¡”Í…µ”Í•Ñ¥½¸Í…åÌÑ¡”UM¥¹Ñ•É™…”…¸¥¹É•…Í”¥ÑÌ‰…ÕÉ…Ñ”ÕÀÑ¼€ÄÄÔÈÀÀ‰…Õ°‰ÕÐ¥Ð‘•™¥¹•Ì¹¼=Á•¹]•‰9•Ð¹•½Ñ¥…Ñ¥½¸½µµ…¹°¡½ÍÐµÍ¥‘”Í•±•Ñ¥½¸ÁÉ½•‘ÕÉ”°½ÈÉ•Ù¥Í¥½¸…ÁÁ±¥…‰¥±¥Ñä™½ÈÑ¡…Ð¡¥¡•ÈÉ…Ñ”¸QÉ•…Ð€ÄäÈÀÀ‰…Õ…ÌÑ¡”‘½Õµ•¹Ñ•‰…Í”Í•ÑÑ¥¹œ…¹€ÄÄÔÈÀÀ‰…Õ…Ì„Í½ÕÉ”µÍÑ…Ñ•½ÁÑ¥½¹…°UM…Á…‰¥±¥Ñä°¹½Ð„Õ¹¥Ù•ÉÍ…°‘•™…Õ±Ð¸Q¡”Q@Í•ÍÍ¥½¸Í•±•Ñ½ÉÌ…¹…ÕÑ¡•¹Ñ¥…Ñ¥½¸Ý½É­™±½Ü‘½Õµ•¹Ñ••±Í•Ý¡•É”…É”¹½ÐÁÉ•É•ÅÕ¥Í¥Ñ•Ì•ÍÑ…‰±¥Í¡•™½ÈÑ¡¥ÌÍ•É¥…°¥¹Ñ•É™…”¸()M•Ñ¥½¸€ÌÉ•Ñ…¥¹ÌÑ¡”=Á•¹]•‰9•Ð‘•±¥µ¥Ñ•ÉÌ…¹ÁÉ¥¹¥Á…°™É…µ”±…ÍÍ•Ì‰ÕÐ‘•™¥¹•Ì¥ÑÌ½Ý¸]!I€è()ð½É´ðM½ÕÉ”µ•…¹¥¹œð)ð€´´´ð€´´´ð)ðAI=UQ}%51€€¬U9%Q€€¬€Œå€ðU¹¥…ÍÐì½¹…Ñ•¹…Ñ”Ñ¡”‘•¥µ…°É•ÁÉ•Í•¹Ñ…Ñ¥½¸½˜Ñ¡”ÁÉ½‘ÕÐÌ±…ÍÐ™½ÕÈ5µ…‘‘É•ÍÌ‰åÑ•ÌÝ¥Ñ Ñ¡”ÑÝ¼µ¡…É…Ñ•ÈÕ¹¥Ð°Ñ¡•¸…ÁÁ•¹€Œå€ð)ð€ÀU9%PŒå€ð	É½…‘…ÍÐÑ¼Ñ¡”Í•±•Ñ•Õ¹¥ÐìÕ¹¥Ð€ÀÁ€Í•±•ÑÌ…±°Õ¹¥ÑÌð)ð€€ÑÉ…¹Íµ¥ÍÍ¥½¸ÁÉ•™¥àð5Õ±Ñ¥…ÍÐµ…É­•¹½Ð¥µÁ±•µ•¹Ñ•¥¸Ñ¡¥ÌÍ½ÕÉ”É•Ù¥Í¥½¸ð()Q¡•Í”…É”Íåµ‰½±¥Œ™½ÉµÌ°¹½Ð½‰Í•ÉÙ•¥¹ÍÑ…±±…Ñ¥½¸¥‘•¹Ñ¥™¥•ÉÌ¸Q¡•ä…É”¹½ÐML€½A1€…‘‘É•ÍÍ•Ì¸Q¡”ÍÕ™™¥à¹…µ•MeM€‰äÑ¡¥Ì‘½Õµ•¹Ð¥Ì„]!I€™…µ¥±äµ…É­•Èì¥Ð¥Ì¹½Ð•Ù¥‘•¹”™½ÈÑ¡”¹Õµ•É¥ŒÁ…å±½…MeM€¥¸MÕ¥Ñ”%59M%=8€ÌÉ€¸Q¡”™½ÕÈµ‰åÑ”…‘‘É•ÍÌ½µÁ½¹•¹Ð‘½•Ì¹½Ð‰ä¥ÑÍ•±˜•ÍÑ…‰±¥Í ¥‘•¹Ñ¥ÑäÝ¥Ñ Ñ¡”MÕ¥Ñ”‘¥…¹½ÍÑ¥ŒA¡åÍ¥…°•Ù¥”%¹…µ•ÍÁ…”¸()M•Ñ¥½¸€Ì¸Ì±¥µ¥ÑÌ‰É½…‘…ÍÐÍ•¹‘¥¹œÑ¼¹¼µ½É”Ñ¡…¸½¹”Á•ÈÍ•½¹¸%ÐÝ…É¹ÌÑ¡…Ð•á••‘¥¹œÑ¡¥ÌÉ…Ñ”…¸Í…ÑÕÉ…Ñ”Ñ¡”i¥	•”¹•ÑÝ½É¬…¹…ÕÍ”ÁÉ½‘ÕÑÌÑ¼µ¥ÍÌÑÉ…™™¥Œ‘ÕÉ¥¹œÑ¡”™½±±½Ý¥¹œ•¥¡ÐÍ•½¹‘Ì¸AÉ•Í•ÉÙ”Ñ¡¥Ì¥¹Ñ•É™…”µÍÁ•¥™¥Œ½¹ÍÑÉ…¥¹Ðì‘¼¹½Ð¥¹™•È„ÁÉ½Ñ½½°µÝ¥‘”Ñ¡É½Õ¡ÁÕÐ±¥µ¥Ð¸()Q¡”Í½ÕÉ”ÁÉ•Í•¹ÑÌÑ¡”…‰ÍÑÉ…Ð™½É´€©]!<©]!P©]!I©]!8Œ€°‰ÕÐÍ•Ñ¥½¸€Ì¸Ô•áÁ±¥¥Ñ±äÍÑ…Ñ•ÌÑ¡…Ð]!9€¥Ì¹•Ù•ÈÕÍ•‰äÑ¡¥Ì¥¹Ñ•É™…”¸%ÑÌ½Á•É…Ñ¥½¹…°½µµ…¹½ÍÑ…ÑÕÌ°É•ÅÕ•ÍÐ°Á…É…µ•Ñ•É¥é•%59M%=9€°É•ÍÁ½¹Í”½É•Á½ÉÐ°…¹ÝÉ¥Ñ”™½ÉµÌ…É”¥¹ÍÑ…¹•Ì½˜Ñ¡”…¹½¹¥…°ÍÑÉÕÑÕÉ•Ì¥¸mÉ…µ”Må¹Ñ…át¡™É…µ”µÍå¹Ñ…à¹µ¤…¹m%59M%=9t¡‘¥µ•¹Í¥½¹Ì¹µ¤ìi¥	•”µÍÁ•¥™¥Œ]!I€Á…ÉÍ¥¹œÍÑ¥±°™½±±½ÝÌÑ¡”ÉÕ±•Ì…‰½Ù”¸()M•Ñ¥½¸€ÐÍÑ…Ñ•ÌÑ¡…Ð½¹±äÁÉ½‘ÕÑÌ½µÁ…Ñ¥‰±”Ý¥Ñ Ñ¡”Í½ÕÉ”Ìi¥	•”¹•ÑÝ½É¬€È¸ÄÁÉ½™¥±”…¸‰”µ…¹…•‰äÑ¡¥Ì¥¹Ñ•É™…”¸Q¡¥Ì¥Ì…¸…ÁÁ±¥…‰¥±¥Ñä±¥µ¥Ð½˜Ñ¡”‘½Õµ•¹Ñ•¥¹Ñ•É™…”É•Ù¥Í¥½¸°¹½Ð•Ù¥‘•¹”Ñ¡…Ð…±°i¥	•”ÁÉ½‘ÕÑÌ•áÁ½Í”=Á•¹]•‰9•Ð¸((ŒŒŒ­¹½Ý±•‘•µ•¹Ð‰•¡…Ù¥½È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÑÁ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()M•Ñ¥½¹Ì€Ì¸ØÑ¡É½Õ €Ì¸ä‘•™¥¹”,€ô€¨Œ¨ÄŒ€°9,€ô€¨Œ¨ÀŒ€°…¹	UMd9,€ô€¨Œ¨ØŒ€¸½ÈÑ¡¥Ì¥¹Ñ•É™…”Ñ¡”Í½ÕÉ”Í…åÌ„	UMd9,¥Ì™½±±½Ý•‰ä„9,…¹¥¹ÍÑÉÕÑÌÝ…¥Ñ¥¹œ€ÔÀÀµ¥±±¥Í•½¹‘Ì‰•™½É”É•ÑÉå¥¹œÑ¡”Í…µ”™É…µ”¸É••¥Ù•ÈµÕÍÐÉ•Ñ…¥¸Ñ¡…ÐÑÝ¼µ™É…µ”É•ÍÕ±ÐÉ…Ñ¡•ÈÑ¡…¸…ÑÑÉ¥‰ÕÑ¥¹œÑ¡”™½±±½Ý¥¹œ9,Ñ¼„¹•Ü½µµ…¹¸Q¡¥Ì¥Ì¹½Ð„•¹•É¥ŒÉ•ÑÉäÉÕ±”™½ÈQ@…Ñ•Ý…åÌ¸((ŒŒŒ9…µ•ÍÁ…”…¹µ…¹…•µ•¹Ð‰½Õ¹‘…É¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€°ÍÍ€°Ù•ÉÍ¥½¹€°é¥‰••€)…ÕÑ¥½¹Ìè¹½Ð•Ù¥‘•¹•€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€()M•Ñ¥½¸€Ì¸Ä±¥ÍÑÌ]!<€Å€°€É€°€Ñ€°€ÄÍ€°€Äá€°€ÈÕ€°…¹‘¥…¹½ÍÑ¥Œ€ÄÀÀÁ€¸Í¡…É•]!=€¹Õµ‰•È‘½•Ì¹½Ð•ÍÑ…‰±¥Í ¥‘•¹Ñ¥…°½Á•É…Ñ¥½¹Ì°É…¹•Ì°…‘‘É•ÍÍ¥¹œ°½ÈÍÕÁÁ½ÉÐÑ¼Ñ¡”MLµ½É¥•¹Ñ•É•™•É•¹•Ì¸Q¡”Í½ÕÉ”Ì±…‰•°€‰¥…¹½ÍÑ¥Œˆ™½È]!<€ÄÀÀÁ€‘½•Ì¹½Ðµ…­”¥ÑÌ¹•¥¡‰½ÈµÑ…‰±”µ•¡…¹¥Í´•ÅÕ¥Ù…±•¹ÐÑ¼Ñ¡”5å!=5MÕ¥Ñ”‘¥…¹½ÍÑ¥Œ™…µ¥±¥•Ì¸()…¹½¹¥…°ÉÕ¹Ñ¥µ”Í•µ…¹Ñ¥ÌÉ•µ…¥¸½É…¹¥é•Õ¹‘•ÈÑ¡”É•±•Ù…¹Ð™Õ¹Ñ¥½¹…°¹…µ•ÍÁ…”¸Q¡”ÕÉÉ•¹Ð½Ý¹•ÉÌ…É”m]!<€Åt ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´Äµ±¥¡Ñ¥¹œ¼¤°m]!<€Ét ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´Èµ…ÕÑ½µ…Ñ¥½¸¼¤°m]!<€Ñt ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´ÐµÑ•µÁ•É…ÑÕÉ”µ½¹ÑÉ½°¼¤°m]!<€ÄÍt ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´ÄÌµ¥¹Ñ•É…Ñ¥½¸µ…Ñ•Ý…ä¼¤°m]!<€Äát ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´Äàµ•¹•Éäµµ…¹…•µ•¹Ð¼¤°…¹m]!<€ÈÕt ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´ÈÔµÑÉ…¹ÍÙ•ÉÍ…°¼¤¸Q¡¥Ì¥¹Ñ•É™…”Á…”½Ý¹ÌÉ½ÍÌµÕÑÑ¥¹œÑÉ…¹ÍÁ½ÉÐ°…‘‘É•ÍÍ¥¹œ°…­¹½Ý±•‘•µ•¹Ð‰•¡…Ù¥½È°‘¥Í½Ù•Éä…É¡¥Ñ•ÑÕÉ”°…¹…ÁÁ±¥…‰¥±¥Ñä±¥µ¥ÑÌì¥Ð‘½•Ì¹½ÐÉ•…Ñ”„Í•½¹Í•Ð½˜™Õ¹Ñ¥½¹…°½µµ…¹‘•™¥¹¥Ñ¥½¹Ì¸()ð5•¡…¹¥Í´ðÙ¥‘•¹”…¹±¥µ¥Ðð)ð€´´´ð€´´´ð)ð9•¥¡‰½È‘¥Í½Ù•ÉäðM•Ñ¥½¸€Ô¸Ì‘•™¥¹•Ì]!<€ÄÀÀÀ%59M%=8€àÅ€…Ì„É½ÕÑ•Èµ¹•¥¡‰½ÈÑÉ…Ù•ÉÍ…°¸%ÑÌ‘•Ñ…¥±•É…µµ…È…¹•Ù¥‘•¹”±¥µ¥ÑÌ…É”‘½Õµ•¹Ñ•‰•±½Ü¸ð)ð%¹Ñ•É™…”ÁÉ½‘ÕÐ¥¹Ù•¹Ñ½ÉäðM•Ñ¥½¹Ì€Ô¸Ð°€Ø°…¹€ÄÄ‘•™¥¹”]!<€ÄÍ€M…¸…¹ÁÉ½‘ÕÐµ‘…Ñ…‰…Í”½Á•É…Ñ¥½¹Ì¸M•”mi¥	•”9•ÑÝ½É¬5…¹…•µ•¹Ñt ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´ÄÌµ¥¹Ñ•É…Ñ¥½¸µ…Ñ•Ý…ä½é¥‰•”µ¹•ÑÝ½É¬µµ…¹…•µ•¹Ð¹µ¤¸ð)ð	¥¹‘¥¹œðM•Ñ¥½¸€ÄÌ‘•™¥¹•Ì=Á•¹]•‰9•ÐµÙ¥Í¥‰±”‰¥¹‘¥¹œ½Á•É…Ñ¥½¹ÌÕ¹‘•È]!<€ÈÕ€¸M•”mi¥	•”	¥¹‘¥¹t ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´ÈÔµÑÉ…¹ÍÙ•ÉÍ…°½é¥‰•”µ‰¥¹‘¥¹œ¹µ¤ìÑ¡”MLÙ¥ÉÑÕ…°µ‰ÕÑÑ½¸É…µµ…È¥Ì¹½Ð„½µÁ±•Ñ”…½Õ¹Ð½˜Ñ¡¥ÌÙ…É¥…¹Ð¸ð)ð¥ÉµÝ…É”‰½Õ¹‘…ÉäðY•ÉÍ¥½¸É•…‘½ÕÐ…¹‰½½Ðµµ½‘”¡…¹‘½™˜…É”=Á•¹]•‰9•ÐµÙ¥Í¥‰±”ì„¡…¹‘½™˜¥Ì¹½Ð•Ù¥‘•¹”Ñ¡…ÐÑ¡”ÍÕ‰Í•ÅÕ•¹ÐÕÁ±½…ÁÉ½Ñ½½°¥Ì=Á•¹]•‰9•Ð¸ð()•Ñ…¥±•i¥	•”Í•µ…¹Ñ¥Ì™½È]!<€Å€°€É€°€Ñ€°€ÄÍ€°€Äá€°…¹€ÈÕ€…É”¥¹Ñ•É…Ñ•Õ¹‘•ÈÑ¡•¥È…¹½¹¥…°™Õ¹Ñ¥½¹…°¹…µ•ÍÁ…•Ì¸Q¡”‘¥Í½Ù•Éä…É¡¥Ñ•ÑÕÉ”…¹]!<€ÄÀÀÀ%59M%=8€àÅ€Í•µ…¹Ñ¥Ì…É”…¹½¹¥…°½¸Ñ¡¥ÌÁ…”¸((ŒŒŒ¥Í½Ù•Éä…¹ÁÉ½‘ÕÐ¥¹Ù•¹Ñ½Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÙ•ÉÍ¥½¹€°é¥‰••€)U¹•ÉÑ…¥¹Ñäè¹½Ð•ÍÑ…‰±¥Í¡•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()i¥	•”=Á•¹]•‰9•ÐÙ•ÉÍ¥½¸€Ð¸À•áÁ½Í•Ìµ½É”Ñ¡…¸½¹”Ý…äÑ¼±•…É¸…‰½ÕÐi¥	•”ÁÉ½‘ÕÑÌ¸Q¡”µ•¡…¹¥ÍµÌ…É”É•±…Ñ•‰äÑ¡”¥¹ÍÑ…±±…Ñ¥½¸Ñ¡•ä‘•ÍÉ¥‰”°‰ÕÐÑ¡”Í½ÕÉ”‘½•Ì¹½Ðµ…­”Ñ¡•¥ÈÉ•ÍÕ±ÐÍ•ÑÌ¥¹Ñ•É¡…¹•…‰±”¸()ð5•¡…¹¥Í´ð]¡…ÐÑ¡”Í½ÕÉ”•áÁ½Í•ÌðA•ÉÍ¥ÍÑ•¹”½ÈÉ•…¡…‰¥±¥Ñä•ÍÑ…‰±¥Í¡•ð)ð€´´´ð€´´´ð€´´´ð)ð]!<€ÄÀÀÀ%59M%=8€àÅ€ð¹•¥¡‰½È¥¹™½Éµ…Ñ¥½¸É•Á½ÉÑ•‰äÑ¡”¥¹Ñ•É™…”½È…¸…‘‘É•ÍÍ•i¥	•”É½ÕÑ•Èð¹•¥¡‰½ÈµÑ…‰±”™É•Í¡¹•ÍÌ°…¥¹œ°…¹Á•ÉÍ¥ÍÑ•¹”…É”¹½Ð‘•™¥¹•ð)ð]!<€ÄÌ]!P€ØÕ€Á±ÕÌ%59M%=8€ØÝ€°€ÜÍ€°…¹€ØÙ€ðM…¸Á±ÕÌÑ¡”¥¹Ñ•É™…”ÌÍÑ½É•ÁÉ½‘ÕÐ‘…Ñ…‰…Í”…¹ÁÉ½‘ÕÐµ¥¹™½Éµ…Ñ¥½¸ÅÕ•É¥•Ìð‘…Ñ…‰…Í”Á•ÉÍ¥ÍÑ•¹”…¹ÍÑ…±”µ•¹ÑÉä‰•¡…Ù¥½È…É”Á…ÉÑ±äÍÁ•¥™¥•ìÕÉÉ•¹ÐÉ•…¡…‰¥±¥Ñä¥Ì„Í•Á…É…Ñ”ÅÕ•ÍÑ¥½¸ð)ð5å!=5MÕ¥Ñ”‘¥…¹½ÍÑ¥Œ‘¥Í½Ù•Éäð‘¥…¹½ÍÑ¥Œµ™…µ¥±ä•¹Õµ•É…Ñ¥½¸…¹A¡åÍ¥…°•Ù¥”¥¹Ñ•ÉÙ¥•Ü°ÍÕ …Ì]!<€ÄÀÀÄ%59M%=8€ÄÍ€ð¹½Ð•ÍÑ…‰±¥Í¡•‰äÑ¡¥Ìi¥	•”¥¹Ñ•É™…”ÍÁ•¥™¥…Ñ¥½¸ð()Q¡”Í½ÕÉ”‘•ÍÉ¥‰•ÌÑÝ¼ÁÉ¥¹¥Á…°i¥	•”ÁÉ½‘ÕÐ…Ñ•½É¥•Ì™½ÈÑ¡¥Ì¥¹Ñ•É™…”èiI€€¡i¥	•”I½ÕÑ•È¤°‘•ÍÉ¥‰•Ñ¡•É”…Ìµ…¥¹ÌµÁ½Ý•É•°…¹i€€¡i¥	•”¹•Ù¥”¤°‘•ÍÉ¥‰•Ñ¡•É”…Ì‰…ÑÑ•ÉäµÁ½Ý•É•¸Q¡•Í”…É”Í½ÕÉ”µ‘•™¥¹•i¥	•”…Ñ•½É¥•Ì™½ÈÑ¡”¥¹Ñ•É™…”¸Q¡•ä…É”¹½Ð…±¥…Í•Ì™½ÈÑ¡”•¹å±½Á•‘¥„ÌA¡åÍ¥…°•Ù¥”°5½‘Õ±”°=‰©•Ð°½È…Ñ…±½Õ”•¹Ñ¥Ñ¥•Ì¸((ŒŒŒŒ9•¥¡‰½È‘¥Í½Ù•Éä€´]!<€ÄÀÀÀ%59M%=8€àÅ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÙ•ÉÍ¥½¹€°é¥‰••€)U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€((¨©Ù¥‘•¹”ÍÑ…ÑÕÌè¨¨ÍÁ•¥™¥…Ñ¥½¸•Ù¥‘•¹”™É½´Í•Ñ¥½¸€Ô¸Ì½˜i¥	•”=Á•¹]•‰9•ÐÙ•ÉÍ¥½¸€Ð¸À¸Q¡”Í½ÕÉ”ÁÉ½Ù¥‘•ÌÑ¡”½µÁ±•Ñ”¥±±ÕÍÑÉ…Ñ••á¡…¹”‰ÕÐ‘½•Ì¹½ÐÁÉ½Ù¥‘”„Í•Á…É…Ñ”™¥•±µ‘•™¥¹¥Ñ¥½¸Ñ…‰±”™½È%59M%=8€àÅ€¸()Q¡”‘½Õµ•¹Ñ•™¥ÉÍÐÍÑ•ÀÅÕ•É¥•ÌÑ¡”=Á•¹]•‰9•Ði¥	•”¥¹Ñ•É™…”¥ÑÍ•±˜è()Ñ•áÐ)±¥•¹Ð€´øi¥	•”¥¹Ñ•É™…”è€¨ŒÄÀÀÀ¨¨àÄŒŒ)i¥	•”¥¹Ñ•É™…”€´ø±¥•¹Ðè€¨ŒÄÀÀÀ¨¨àÄI=\©U9-9=]8©9%!	=HŒŒ)i¥	•”¥¹Ñ•É™…”€´ø±¥•¹Ðè€¨Œ¨ÄŒŒ)€()Q¡”É•ÍÁ½¹Í”™½É´¥ÌÉ•Á•…Ñ•½¹”™½È•… É•Á½ÉÑ••¹ÑÉä…¹„™¥¹…°-€Ñ•Éµ¥¹…Ñ•ÌÑ¡”Í•ÅÕ•¹”¸Q¡”Íåµ‰½±¥Œ™¥•±‘Ì…‰½Ù”É•Á±…”¥¹ÍÑ…±±…Ñ¥½¸µ‘•É¥Ù•¥‘•¹Ñ¥™¥•ÉÌ™É½´Ñ¡”Í½ÕÉ”•á…µÁ±•Ì¸()Q¡”‘½Õµ•¹Ñ•Í•½¹ÍÑ•ÀÅÕ•É¥•Ì•… ¹•Ý±ä‘¥Í½Ù•É•É½ÕÑ•ÈÑ¡É½Õ Ñ¡”¥¹Ñ•É™…”è()Ñ•áÐ)±¥•¹Ð€´øi¥	•”¥¹Ñ•É™…”è€¨ŒÄÀÀÀ©I=UQHÀÀŒä¨àÄŒŒ)i¥	•”¥¹Ñ•É™…”€´ø±¥•¹Ðè€¨ŒÄÀÀÀ©I=UQHÀÀŒä¨àÄI=\©U9-9=]8©9%!	=HŒŒ)i¥	•”¥¹Ñ•É™…”€´ø±¥•¹Ðè€¨Œ¨ÄŒŒ)€()!•É”I=UQHÀÀŒå€ÕÍ•ÌÑ¡”Í½ÕÉ”Ìi¥	•”ÁÉ½‘ÕÐµ…‘‘É•ÍÌ™½É´Ý¥Ñ U¹¥Ð€ÀÁ€¸%ÐÍ•±•ÑÌÑ¡”É½ÕÑ•ÈÝ¡½Í”¹•¥¡‰½È¥¹™½Éµ…Ñ¥½¸¥Ì‰•¥¹œÉ•ÅÕ•ÍÑ•ì¥Ð¥Ì¹½Ð„5å!=5MÕ¥Ñ”A¡åÍ¥…°•Ù¥”%¸()ðI•ÍÁ½¹Í”•±•µ•¹ÐðM½ÕÉ”µ‰½Õ¹‘•¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸ð)ð€´´´ð€´´´ð)ðÉ•ÍÁ½¹Í”]!I€ð•µÁÑäÝ¡•¸Ñ¡”¥¹Ñ•É™…”Ì½Ý¸¹•¥¡‰½ÉÌ…É”É•ÑÕÉ¹•ìÑ¡”…‘‘É•ÍÍ•É½ÕÑ•È]!I€Ý¡•¸„É½ÕÑ•È¥ÌÅÕ•É¥•ð)ðI=]€ðÑ¡”•á…µÁ±”¥¹É•µ•¹ÑÌÑ¡¥Ì™¥•±™É½´é•É¼™½ÈÍÕ•ÍÍ¥Ù”É•ÍÁ½¹Í•ÌìÑ¡”Í½ÕÉ”‘½•Ì¹½Ð¹…µ”¥Ð½È•ÍÑ…‰±¥Í ÕÉÍ½È°É•ÍÕµ”°Á•ÉÍ¥ÍÑ•¹”°½ÈÁÉ½‘ÕÐµ‘…Ñ…‰…Í”µ¥¹‘•àÍ•µ…¹Ñ¥Ìð)ðU9-9=]9€ð…¸…‘‘¥Ñ¥½¹…°¹Õµ•É¥ŒÉ•ÍÁ½¹Í”™¥•±Ý¡½Í”µ•…¹¥¹œ¥Ì¹½Ð‘•™¥¹•…¹åÝ¡•É”¥¸Ñ¡”¥¹ÍÁ•Ñ•Í½ÕÉ”ð)ð9%!	=I€ð„É•ÑÕÉ¹•i¥	•”ÁÉ½‘ÕÐµ…‘‘É•ÍÌ½µÁ½¹•¹ÐìÑ¡”Í½ÕÉ”ÕÍ•Ì„¹•Ý±ä‘¥Í½Ù•É•É½ÕÑ•ÈÙ…±Õ”Ñ¼½¹ÍÑÉÕÐÑ¡”¹•áÐÉ½ÕÑ•Èµ…‘‘É•ÍÍ•É•ÅÕ•ÍÐð)ð™¥¹…°-€ð•áÁ±¥¥Ð•¹½˜Ñ¡…Ð¹•¥¡‰½ÈÉ•ÍÁ½¹Í”Í•ÅÕ•¹”ð()…±±¥¹œÑ¡”ÁÉ½•ÍÌÉ•ÕÉÍ¥Ù”¥Ì„‘•ÍÉ¥ÁÑ¥½¸½˜Ñ¡”±¥•¹ÐÑÉ…Ù•ÉÍ…°°¹½ÐÑ•Éµ¥¹½±½äÍÕÁÁ±¥•‰äÑ¡”ÍÁ•¥™¥…Ñ¥½¸¸Q¡”Í½ÕÉ”•áÁ±¥¥Ñ±äÍ…åÌÑ¡…Ð…™Ñ•ÈÅÕ•Éå¥¹œÑ¡”¥¹Ñ•É™…”°Ñ¡”Í•½¹ÍÑ•À¥ÌÑ¼…Í¬•… ¹•Ý±ä‘¥Í½Ù•É•iI€™½È¥ÑÌ¹•¥¡‰½ÉÌ°…¹¥ÐÍÑ…Ñ•ÌÑ¡…ÐÑ¡¥ÌÍ•ÅÕ•¹”…¸½‰Ñ…¥¸Ñ¡”ÁÉ½‘ÕÑÌ½˜Ñ¡”¥¹ÍÑ…±±…Ñ¥½¸¸Q¡”‘½Õµ•¹Ñ•ÑÉ…Ù•ÉÍ…°Ñ¡•É•™½É”½¹Ñ¥¹Õ•ÌÑ¡É½Õ ¹•Ý±ä‘¥Í½Ù•É•É½ÕÑ•ÉÌ¸()Q¡”‘½Õµ•¹Ñ•ÁÉ½•‘ÕÉ”‘½•Ì¹½ÐÅÕ•Éäi€•¹ÑÉ¥•ÌÉ•ÕÉÍ¥Ù•±ä¸Q¡”Í½ÕÉ”‘½•Ì¹½ÐÍÑ…Ñ”Ñ¡…Ð„i€µÕÍÐÉ•©•Ð%59M%=8€àÅ€ìÍÕÁÁ½ÉÐ™½ÈÍÕ „É•ÅÕ•ÍÐ¥Ì€¨©U¹­¹½Ý¸¨¨¸9¼•¹µ•Ù¥”É•ÕÉÍ¥½¸Í¡½Õ±‰”¥¹™•ÉÉ•¸((ŒŒŒŒ9•¥¡‰½ÈµÑ…‰±”±¥µ¥ÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÀÝ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()Q¡”Í½ÕÉ”…±±ÌÑ¡”É•ÑÕÉ¹••¹ÑÉ¥•Ì€‰­¹½Ý¸¹•¥¡‰½ÉÌ¸ˆ%Ð‘½•Ì¹½Ð‘•™¥¹”¹•¥¡‰½ÈµÑ…‰±”™É•Í¡¹•ÍÌ°…¥¹œ°É…‘¥¼É•…¡…‰¥±¥ÑäÉ¥Ñ•É¥„°½ÈÁ•ÉÍ¥ÍÑ•¹”¸Q¡•É•™½É”%59M%=8€àÅ€¥Ì•ÍÑ…‰±¥Í¡•…Ì„Ñ½Á½±½ä½È¹•¥¡‰½ÈµÑÉ…Ù•ÉÍ…°µ•¡…¹¥Í´°‰ÕÐ¥Ð¥Ì€¨©U¹É•Í½±Ù•¨¨Ý¡•Ñ¡•È•Ù•ÉäÉ•ÑÕÉ¹••¹ÑÉä¥ÌÕÉÉ•¹Ñ±äÉ•…¡…‰±”…ÐÑ¡”¥¹ÍÑ…¹Ð½˜Ñ¡”ÅÕ•Éä¸()Q¡”Í½ÕÉ”‘½•Ì¹½Ð‘•™¥¹”„‘ÕÁ±¥…Ñ”µ•±¥µ¥¹…Ñ¥½¸ÉÕ±”¸%¸½¹”É½ÕÑ•Èµ…‘‘É•ÍÍ••á…µÁ±”°„É•ÑÕÉ¹•¹•¥¡‰½È¥‘•¹Ñ¥™¥•È¥Ì•ÅÕ…°Ñ¼Ñ¡”ÅÕ•É¥•É½ÕÑ•È¥‘•¹Ñ¥™¥•È¸Q¡”Í½ÕÉ”‘½•Ì¹½Ð•áÁ±…¥¸Ý¡•Ñ¡•ÈÑ¡…Ð¥Ì¥¹Ñ•¹‘•Í•µ…¹Ñ¥Ì°…¸•á…µÁ±”‘•™•Ð°½È•Ù¥‘•¹”…‰½ÕÐÑ¡”Õ¹¹…µ•™¥•±‘Ì¸±¥•¹ÐµÕÍÐ¹½Ð…ÍÍÕµ”Ñ¡…Ð%59M%=8€àÅ€å¥•±‘Ì„‘ÕÁ±¥…Ñ”µ™É•”É…Á Í½±•±ä™É½´Ñ¡¥ÌÍÁ•¥™¥…Ñ¥½¸¸()9¼%59M%=8€àÅ€µ…á¥µÕ´•¹ÑÉä½Õ¹Ð°Á…¥¹œÉÕ±”°É•ÅÕ•ÍÐÕÉÍ½È°½È¹Õµ•É¥ŒÑ•Éµ¥¹…Ñ¥½¸Í•¹Ñ¥¹•°¥ÌÍÁ•¥™¥•¸½µÁ±•Ñ¥½¸¥ÌÑ¡”™¥¹…°-€¸Q¡”¥¹Ñ•É™…”µÝ¥‘”9-€…¹	UMd‰•¡…Ù¥½È‘•ÍÉ¥‰•Õ¹‘•Èm­¹½Ý±•‘•µ•¹Ð‰•¡…Ù¥½Ét …­¹½Ý±•‘•µ•¹Ðµ‰•¡…Ù¥½È¤É•µ…¥¹Ì…ÁÁ±¥…‰±”…Ì•¹•É…°¥¹Ñ•É™…”Íå¹Ñ…à°‰ÕÐÍ•Ñ¥½¸€Ô¸Ì…ÍÍ¥¹Ì¹¼%59M%=8€àÅ€µÍÁ•¥™¥Œµ•…¹¥¹œÑ¼9-€½È	UMd¸()Q¡”ÁÉ½‘ÕÐ‘…Ñ…‰…Í”Ì‘½Õµ•¹Ñ•€ÄÜÔµÁÉ½‘ÕÐ…Á…¥Ñä‘½•Ì¹½Ð•ÍÑ…‰±¥Í „€ÄÜÔµ•¹ÑÉä±¥µ¥Ð™½È„¹•¥¡‰½ÈÉ•ÍÁ½¹Í”¸Q¡•Í”…É”Í•Á…É…Ñ”µ•¡…¹¥ÍµÌ¸((ŒŒŒŒI•±…Ñ¥½¹Í¡¥ÀÑ¼M…¸…¹Ñ¡”ÁÉ½‘ÕÐ‘…Ñ…‰…Í”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°é¥‰••€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()M•Ñ¥½¸€Ô¸ÐÁÉ•Í•¹ÑÌ]!<€ÄÌ]!P€ØÕ€M…¸…Ì…¹½Ñ¡•È‘¥Í½Ù•ÉäÍ•ÅÕ•¹”¸M…¸‰É½…‘…ÍÑÌ½Ù•ÈÑ¡”i¥	•”¹•ÑÝ½É¬Í¼…Ñ¥Ù”É½ÕÑ•ÉÌ…¹…Ý…­”•¹•Ù¥•Ì…¸…¹ÍÝ•È¸ÁÁÉ½á¥µ…Ñ•±ä€ÄÌÍ•½¹‘Ì…™Ñ•È…¸…•ÁÑ•M…¸°Ñ¡”¥¹Ñ•É™…”É•Á½ÉÑÌ%59M%=8€ØÝ€¸()Q¡”‘•Ñ…¥±•]!<€ÄÍ€‘•™¥¹¥Ñ¥½¸µ…­•Ì…¸¥µÁ½ÉÑ…¹Ð‘¥ÍÑ¥¹Ñ¥½¸èÑ¡”É•Á½ÉÑ•%59M%=8€ØÝ€Ù…±Õ”¥ÌÑ¡”¹Õµ‰•È½˜ÁÉ½‘ÕÑÌÍÑ½É•¥¸Ñ¡”¥¹Ñ•É™…”ÁÉ½‘ÕÐ‘…Ñ…‰…Í”°¹½Ðµ•É•±äÑ¡”¹Õµ‰•È½˜…Ñ¥Ù”É½ÕÑ•ÉÌ½‰Í•ÉÙ•‰äÑ¡…ÐM…¸¸%¹‘•á•%59M%=8€ÜÍ€É•…‘ÌÑ¡”ÍÑ½É•ÁÉ½‘ÕÐ¥‘•¹Ñ¥™¥•È…¹Á½Ý•È…Ñ•½Éä™É½´Ñ¡…Ð‘…Ñ…‰…Í”°Ý¡¥±”%59M%=8€ØÙ€…¸½¹Ñ…Ð„ÁÉ½‘ÕÐÑ¼É•ÑÉ¥•Ù”U¹¥Ð½•¹µÁ½¥¹Ð•Ù¥”µ%¥¹™½Éµ…Ñ¥½¸…¹…¸É•Á½ÉÐÑ¡…Ð„ÍÑ½É•ÁÉ½‘ÕÐ¥ÌÕ¹É•…¡…‰±”¸()Q¡•Í”Í•µ…¹Ñ¥Ì…É”…¹½¹¥…°¥¸mi¥	•”9•ÑÝ½É¬5…¹…•µ•¹Ñt ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´ÄÌµ¥¹Ñ•É…Ñ¥½¸µ…Ñ•Ý…ä½é¥‰•”µ¹•ÑÝ½É¬µµ…¹…•µ•¹Ð¹µÍ…¸µ…¹µÁÉ½‘ÕÐµ‘…Ñ…‰…Í”¤¸9•¥¡‰½È‘¥Í½Ù•Éä‘½•Ì¹½ÐÉ•Á±…”Ñ¡…Ð¥¹Ù•¹Ñ½Éäµ½‘•°°…¹ÁÉ½‘ÕÐµ‘…Ñ…‰…Í”µ•µ‰•ÉÍ¡¥À‘½•Ì¹½ÐÁÉ½Ù”ÕÉÉ•¹ÐÉ•…¡…‰¥±¥Ñä¸((ŒŒŒŒI•±…Ñ¥½¹Í¡¥ÀÑ¼MÕ¥Ñ”‘¥…¹½ÍÑ¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìèé¥‰••€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€()Q¡”5å!=5MÕ¥Ñ”‘¥…¹½ÍÑ¥ŒÝ½É­™±½ÝÌ‘½Õµ•¹Ñ•Õ¹‘•Èm¥…¹½ÍÑ¥Ít ¸¸½‘¥…¹½ÍÑ¥Ì¼¤ÕÍ”‘¥™™•É•¹Ðµ…¹…•µ•¹Ð™…µ¥±¥•Ì°¥‘•¹Ñ¥™¥•ÉÌ°•¹Õµ•É…Ñ¥½¸½Á•É…Ñ¥½¹Ì°…¹A¡åÍ¥…°•Ù¥”¥¹Ñ•ÉÙ¥•ÜÍ•µ…¹Ñ¥Ì¸%¸Á…ÉÑ¥Õ±…È°]!<€ÄÀÀÄ%59M%=8€ÄÍ€•Ù¥”µ%•¹Õµ•É…Ñ¥½¸¥Ì¹½Ð„É•¹…µ•™½É´½˜i¥	•”]!<€ÄÀÀÀ%59M%=8€àÅ€¸()9¼¥¹ÍÁ•Ñ•Í½ÕÉ”•ÍÑ…‰±¥Í¡•Ì„µ…ÁÁ¥¹œ‰•ÑÝ••¸i¥	•”ÁÉ½‘ÕÐ¥‘•¹Ñ¥™¥•ÉÌ°i¥	•”ÁÉ½‘ÕÐµ‘…Ñ…‰…Í”¥¹‘•á•Ì°…¹5å!=5MÕ¥Ñ”A¡åÍ¥…°•Ù¥”%Ì¸Q¡”Ñ¡É•”‘¥Í½Ù•Éä½¥¹Ù•¹Ñ½ÉäÍÕÉ™…•ÌµÕÍÐÉ•µ…¥¸Í•Á…É…Ñ”Õ¹±•ÍÌ™ÕÑÕÉ”•Ù¥‘•¹”•ÍÑ…‰±¥Í¡•Ì„É•±…Ñ¥½¹Í¡¥À¸((ŒŒŒAÉ•Í•ÉÙ•Í½ÕÉ”½¹™±¥ÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÈéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÍÍ€°é¥‰••€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäè½¹ÑÉ…‘¥Ñ½Éå€°Õ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()ðEÕ•ÍÑ¥½¸ð½¹™±¥Ñ¥¹œÍ½ÕÉ”±½…Ñ¥½¹ÌðÕÉÉ•¹Ð½¹±ÕÍ¥½¸ð)ð€´´´ð€´´´ð€´´´ð)ðÕÑ½µ…Ñ¥½¸U@Ù…±Õ”ðAÁ…”€ÄÄ±…‰•±Ì„]!P€É€•á…µÁ±”U@ìÁ…”€Ìà…ÍÍ¥¹ÌU@Ñ¼€Å€…¹=]8Ñ¼€É€ðAÉ•Í•ÉÙ”Ñ¡”½¹™±¥Ðì‘¼¹½ÐÕÍ”Ñ¡”•á…µÁ±”Ñ¼É•‘•™¥¹”ÕÑ½µ…Ñ¥½¸‘¥É•Ñ¥½¸¸ÁÁ±¥…‰±”¥¹Ñ•É™…”•Ù¥‘•¹”¥ÌÉ•ÅÕ¥É•¸ð)ð¹•ÉäÉ•Í•ÐÙ…±Õ”ðAÁ…”€ÔÌÍÕµµ…Éä¥Ù•Ì€Á€ìÑ¡”‘•Ñ…¥±•É•Í•Ð™É…µ”ÕÍ•Ì€ÜÕ€ðU¹É•Í½±Ù•™½ÈÑ¡¥ÌÙ…É¥…¹Ð¸ML]!P€ÜÕ€¥Ì¹½Ð¥¹‘•Á•¹‘•¹Ð½¹™¥Éµ…Ñ¥½¸½˜Ñ¡”i¥	•”½Á•É…Ñ¥½¸¸ð)ð¹•ÉäÉ•ÅÕ•¹ä½¹•Éäµ…ÁÁ¥¹œðAÁ…”€ÔÌÉ•ÅÕ•¹äÕÍ”…Í”ÕÍ•Ì%59M%=8€ÔÅ€ìÁ…•Ì€ÔÐ´ÔÔ‘•™¥¹”€ÔÅ€…Ì¹•Éä…¹€ÄÄÉ€…ÌÉ•ÅÕ•¹äðAÉ•Í•ÉÙ”Ñ¡”½¹™±¥Ð¸Q¡”‘•Ñ…¥±•Ñ…‰±”…¹‘•™¥¹¥Ñ¥½¹Ì‘¼¹½Ð•É…Í”Ñ¡”½¹ÑÉ…‘¥Ñ½ÉäÕÍ”…Í”¸ð()9¼ÁÉ¥Ù…Ñ”…‘‘É•ÍÌ™É½´Ñ¡”Í½ÕÉ”•á…µÁ±•Ì¥ÌÉ•ÁÉ½‘Õ•¡•É”¸Õ¹Ñ¥½¹…°Í•Ñ¥½¹Ì€àÑ¡É½Õ €ÄÌ¡…Ù”¹½ÜÉ••¥Ù•½Á•É…Ñ¥½¸µ±•Ù•°É•½¹¥±¥…Ñ¥½¸™½È]!<€Å€°€É€°€Ñ€°€ÄÍ€°€Äá€°…¹€ÈÕ€ìÑ¡•¥È‘•Ñ…¥±••Ù¥‘•¹”‘•¥Í¥½¹Ì…É”É•½É‘•¥¸Ñ¡”mi¥	•”Õ¹Ñ¥½¹…°I•½¹¥±¥…Ñ¥½¹t ¸¸½ÁÉ½©•Ð½É•Ù¥•Ü½é¥‰•”µ™Õ¹Ñ¥½¹…°µÉ•½¹¥±¥…Ñ¥½¸¹µ¤…¹Ñ¡”•…É±¥•Èmi¥	•”I•½¹¥±¥…Ñ¥½¸I•Ù¥•Ýt ¸¸½ÁÉ½©•Ð½É•Ù¥•Ü½é¥‰•”µÉ•½¹¥±¥…Ñ¥½¸¹µ¤¸Q¡”]!<€ÄÀÀÁ€‘¥Í½Ù•Éäµ•¡…¹¥Í´…¹Í•Ñ¥½¹Ì€Ô…¹€ØÁÉ½‘ÕÐµ¥¹Ù•¹Ñ½Éä™±½ÝÌ…É”É•½¹¥±•¥¸mi¥	•”¥Í½Ù•Éä…¹%¹Ù•¹Ñ½ÉäI•½¹¥±¥…Ñ¥½¹t ¸¸½ÁÉ½©•Ð½É•Ù¥•Ü½é¥‰•”µ‘¥Í½Ù•Éäµ¥¹Ù•¹Ñ½ÉäµÉ•½¹¥±¥…Ñ¥½¸¹µ¤¸Q¡”½µÁ±•Ñ”Í½ÕÉ”µÝ¥‘”…Õ‘¥Ð¥ÌÉ•½É‘•¥¸Ñ¡”mi¥	•”¥¹…°M½ÕÉ”½µÁ±•Ñ•¹•ÍÌ•ÉÑ¥™¥…Ñ¥½¹t ¸¸½ÁÉ½©•Ð½É•Ù¥•Ü½é¥‰•”µ™¥¹…°µÍ½ÕÉ”µ½µÁ±•Ñ•¹•ÍÌµ•ÉÑ¥™¥…Ñ¥½¸¹µ¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄÌ()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½I5¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒI•Ù•ÉÍ”¹¥¹••É¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€()Q¡¥ÌÍ•Ñ¥½¸•áÁ±…¥¹Ì¡½Ü=Á•¹]•‰9•Ð…¹5å!=5MÕ¥Ñ”É•±…Ñ¥½¹Í¡¥ÁÌ…É”É•½Ù•É•™É½´¥µÁ±•µ•¹Ñ…Ñ¥½¸‘…Ñ„°½‰Í•ÉÙ•ÑÉ…™™¥Œ°ÁÕ‰±¥ŒÍÁ•¥™¥…Ñ¥½¹Ì°ÁÉ½‘ÕÐ‘½Õµ•¹Ñ…Ñ¥½¸°…¹½¹ÑÉ½±±•…ÁÁ±¥…Ñ¥½¸‰•¡…Ù¥½È¸()%Ð¥Ì„É•ÁÉ½‘Õ¥‰±”É•Í•…É É•½É°¹½Ð„Í•½¹ÁÉ½Ñ½½°É•™•É•¹”¸MÑ…‰±”½Á•É…Ñ¥½¹…°É•ÍÕ±ÑÌ‰•±½¹œ¥¸mAÉ½Ñ½½±t ¸¸½ÁÉ½Ñ½½°¼¤°mÕ¹Ñ¥½¹…°I•™•É•¹•t ¸¸½™Õ¹Ñ¥½¹…°¼¤°m•Ù¥”5½‘•±t ¸¸½‘•Ù¥”µµ½‘•°¼¤°m¥…¹½ÍÑ¥Ít ¸¸½‘¥…¹½ÍÑ¥Ì¼¤°mAÉ½É…µµ¥¹t ¸¸½ÁÉ½É…µµ¥¹œ¼¤°mAÉ…Ñ¥…°Õ¥‘•Ít ¸¸½Õ¥‘•Ì¼¤°mM•¹…É¥¼¹¥¹•t ¸¸½Í•¹…É¥¼µ•¹¥¹”¼¤°½Èm5å!=5MÕ¥Ñ”%¹Ñ•É¹…±Ít ¸¸½¥¹Ñ•É¹…±Ì¼¤¸Q¡¥ÌÍ•Ñ¥½¸ÁÉ•Í•ÉÙ•ÌÑ¡”•Ù¥‘•¹”Á…Ñ °½¹™¥‘•¹”‰½Õ¹‘…Éä°½µÁ•Ñ¥¹œ•áÁ±…¹…Ñ¥½¹Ì°É•©•Ñ•Í¡½ÉÑÕÑÌ°…¹É•µ…¥¹¥¹œÅÕ•ÍÑ¥½¹Ì¸((ŒŒŒI•™•É•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)U¹•ÉÑ…¥¹Ñäè¡åÁ½Ñ¡•Í¥Í€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€()ðMÕ‰©•ÐðA…”ð)ð€´´´ð€´´´ð)ð¹µÑ¼µ•¹¥¹Ù•ÍÑ¥…Ñ¥½¸Ý½É­™±½Ü…¹ÁÉ½µ½Ñ¥½¸É¥Ñ•É¥„ðm5•Ñ¡½‘½±½åt¡µ•Ñ¡½‘½±½ä¹µ¤ð)ðÙ¥‘•¹”±…ÍÍ•Ì°±…¥´µ±•Ù•°½¹™¥‘•¹”°¹•…Ñ¥Ù”•Ù¥‘•¹”°…¹É•Ù¥Í¥½¸‘É¥™ÐðmÙ¥‘•¹”…¹½¹™¥‘•¹•t¡•Ù¥‘•¹”µ…¹µ½¹™¥‘•¹”¹µ¤ð)ðI•½Ù•É¥¹œÕ¹‘•±…É•‘…Ñ…‰…Í”É•±…Ñ¥½¹Í¡¥ÁÌÝ¥Ñ¡½ÕÐ…±Ñ•É¥¹œÍ½ÕÉ”•Ù¥‘•¹”ðm…Ñ…‰…Í”I•±…Ñ¥½¹Í¡¥ÀI•½¹ÍÑÉÕÑ¥½¹t¡‘…Ñ…‰…Í”µÉ•±…Ñ¥½¹Í¡¥ÀµÉ•½¹ÍÑÉÕÑ¥½¸¹µ¤ð)ð½¹Í½±¥‘…Ñ••ÍÑ…‰±¥Í¡•°¥¹™•ÉÉ•°½Á•¸°…¹Í•¹Ñ¥¹•°µ‘•Á•¹‘•¹ÐÉ•±…Ñ¥½¹Í¡¥ÁÌðmI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Ét¡É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ¤ð)ðM…™•±ä½¹¹•Ñ¥¹œÝ¥É”Ù…±Õ•Ì°…Ñ…±½Õ”…Á…‰¥±¥Ñä°Ù…±¥‘…Ñ¥½¸°…¹Í•¹…É¥¼µ½‘•±ÌðmÉ½ÍÌµ…Ñ…‰…Í”½ÉÉ•±…Ñ¥½¹t¡É½ÍÌµ‘…Ñ…‰…Í”µ½ÉÉ•±…Ñ¥½¸¹µ¤ð)ð…ÁÑÕÉ¥¹œ°Í•µ•¹Ñ¥¹œ°½ÉÉ•±…Ñ¥¹œ°…¹ÁÕ‰±¥Í¡¥¹œÉÕ¹Ñ¥µ”ÑÉ…™™¥Œðm…ÁÑÕÉ”¹…±åÍ¥Ít¡…ÁÑÕÉ”µ…¹…±åÍ¥Ì¹µ¤ð)ð•Í¥¹¥¹œ½¹ÑÉ½±±•Ñ•ÍÑÌÑ¡…Ð‘¥ÍÑ¥¹Õ¥Í ½µÁ•Ñ¥¹œ•áÁ±…¹…Ñ¥½¹Ìðm!åÁ½Ñ¡•Í¥ÌQ•ÍÑ¥¹t¡¡åÁ½Ñ¡•Í¥ÌµÑ•ÍÑ¥¹œ¹µ¤ð)ðI•©•Ñ•É•±…Ñ¥½¹Í¡¥ÁÌ°¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¹Ì°…¹É•ÕÉÉ¥¹œ…¹…±åÑ¥…°Í¡½ÉÑÕÑÌðmI•©•Ñ•I•±…Ñ¥½¹Í¡¥ÁÍt¡É•©•Ñ•µÉ•±…Ñ¥½¹Í¡¥ÁÌ¹µ¤ð)ðÕ‘¥Ñ•ÅÕ•ÍÑ¥½¹ÌÑ¡…ÐÍÑ¥±°É•ÅÕ¥É”•Ù¥‘•¹”ðm=Á•¸EÕ•ÍÑ¥½¹Ít¡½Á•¸µÅÕ•ÍÑ¥½¹Ì¹µ¤ð((ŒŒŒUÍ”Ñ¡¥ÌÍ•Ñ¥½¸‰äÑ…Í¬()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÀÍ€()U¹•ÉÑ…¥¹Ñäè¡åÁ½Ñ¡•Í¥Í€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°‘…Ñ…‰…Í•€°‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€°•áÁ•É¥µ•¹Ñ€()ð½…°ðMÑ…ÉÐÝ¥Ñ ðQ¡•¸½¹ÍÕ±Ðð)ð€´´´ð€´´´ð€´´´ð)ðÙ…±Õ…Ñ”„ÁÉ½Á½Í•‘…Ñ…‰…Í”™½É•¥¸­•äðm…Ñ…‰…Í”I•±…Ñ¥½¹Í¡¥ÀI•½¹ÍÑÉÕÑ¥½¹t¡‘…Ñ…‰…Í”µÉ•±…Ñ¥½¹Í¡¥ÀµÉ•½¹ÍÑÉÕÑ¥½¸¹µ¤ðmÙ¥‘•¹”…¹½¹™¥‘•¹•t¡•Ù¥‘•¹”µ…¹µ½¹™¥‘•¹”¹µ¤°mI•©•Ñ•I•±…Ñ¥½¹Í¡¥ÁÍt¡É•©•Ñ•µÉ•±…Ñ¥½¹Í¡¥ÁÌ¹µ¤ð)ð•½‘”„¹•Üµ…¹…•µ•¹Ð…ÁÑÕÉ”ðm…ÁÑÕÉ”¹…±åÍ¥Ít¡…ÁÑÕÉ”µ…¹…±åÍ¥Ì¹µ¤ðm¥…¹½ÍÑ¥Ít ¸¸½‘¥…¹½ÍÑ¥Ì¼¤°mI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Ét¡É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ¤ð)ð½¹¹•Ð„™É…µ”™¥•±Ñ¼„‘…Ñ…‰…Í”ðmÉ½ÍÌµ…Ñ…‰…Í”½ÉÉ•±…Ñ¥½¹t¡É½ÍÌµ‘…Ñ…‰…Í”µ½ÉÉ•±…Ñ¥½¸¹µ¤ðm5•Ñ¡½‘½±½åt¡µ•Ñ¡½‘½±½ä¹µ¤°m!åÁ½Ñ¡•Í¥ÌQ•ÍÑ¥¹t¡¡åÁ½Ñ¡•Í¥ÌµÑ•ÍÑ¥¹œ¹µ¤ð)ð•¥‘”Ý¡•Ñ¡•È„±…¥´¥ÌÉ•…‘ä™½ÈÉ•™•É•¹”‘½Õµ•¹Ñ…Ñ¥½¸ðmÙ¥‘•¹”…¹½¹™¥‘•¹•t¡•Ù¥‘•¹”µ…¹µ½¹™¥‘•¹”¹µ¤ðm5•Ñ¡½‘½±½åt¡µ•Ñ¡½‘½±½ä¹µ¤ð)ð•Í¥¸Ñ¡”¹•áÐ•Ù¥”•áÁ•É¥µ•¹Ððm!åÁ½Ñ¡•Í¥ÌQ•ÍÑ¥¹t¡¡åÁ½Ñ¡•Í¥ÌµÑ•ÍÑ¥¹œ¹µ¤ðm=Á•¸EÕ•ÍÑ¥½¹Ít¡½Á•¸µÅÕ•ÍÑ¥½¹Ì¹µ¤ð)ð¡•¬Ý¡•Ñ¡•È…¸…ÑÑÉ…Ñ¥Ù”µ…ÁÁ¥¹œÝ…Ì…±É•…‘ä‘¥ÍÁÉ½Ù•ðmI•©•Ñ•I•±…Ñ¥½¹Í¡¥ÁÍt¡É•©•Ñ•µÉ•±…Ñ¥½¹Í¡¥ÁÌ¹µ¤ðmI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Ét¡É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ¤ð)ðM•”Ñ¡”ÕÉÉ•¹ÐÍÑ…Ñ”½˜­¹½Ý±•‘”ÅÕ¥­±äðmI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Ét¡É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ¤ðm=Á•¸EÕ•ÍÑ¥½¹Ít¡½Á•¸µÅÕ•ÍÑ¥½¹Ì¹µ¤ð((ŒŒŒ½É”ÉÕ±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè¹½Ð…ÁÁ±¥…‰±•€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()9Õµ•É¥Œ•ÅÕ…±¥Ñä¥Ì„±•…°¹½Ð„É•±…Ñ¥½¹Í¡¥À¸()Ù…±Õ”…¸‰”è((´„‘…Ñ…‰…Í”µ±½…°ÁÉ¥µ…Éä­•äì(´…¸•áÑ•É¹…°…Ñ…±½Õ”¹Õµ‰•Èì(´…¸¥¹ÍÑ…±±•€ÌÈµ‰¥Ð•Ù¥”¥‘•¹Ñ¥™¥•Èì(´„•Ù¥”µ±½…°Í±½Ñ€ì(´…¸=Á•¹]•‰9•ÐÝ¥É”™¥•±ì(´½¹”½µÁ½¹•¹Ð½˜„½µÁ½Í¥Ñ”Ù•ÉÍ¥½¸½È…‘‘É•ÍÌì(´„‘¥ÍÉ¥µ¥¹…Ñ½Èµ‘•Á•¹‘•¹ÐÙ…±Õ”ì(´„Í•¹Ñ¥¹•°ÍÕ …Ì€Á€µ•…¹¥¹œƒŠq¹½Ð…ÁÁ±¥…‰±—Štì(´„…Ñ•½Éä½Èµ…Ñ¡¥¹œ¥‘•¹Ñ¥™¥•È±½…°Ñ¼½¹”…ÁÁ±¥…Ñ¥½¸µ½‘•°¸()ÕÍ…‰±”É•±…Ñ¥½¹Í¡¥ÀµÕÍÐ¥‘•¹Ñ¥™äÑ¡”¹…µ•ÍÁ…”½¸‰½Ñ Í¥‘•Ì°É•ÅÕ¥É•½¹Ñ•áÐ°…É‘¥¹…±¥Ñä°Í•¹Ñ¥¹•°ÉÕ±•Ì°•Ù¥‘•¹”°½¹™¥‘•¹”°Í½Á”°…¹™…±Í¥™¥•È¸((ŒŒŒM½ÕÉ”µ½˜µÑÉÕÑ ‰½Õ¹‘…É¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°‘½Õµ•¹Ñ…Ñ¥½¹€°Í½ÕÉ•€()9¼Í¥¹±”Í½ÕÉ”…¹ÍÝ•ÉÌ•Ù•ÉäÅÕ•ÍÑ¥½¸è()ðM½ÕÉ”ðMÑÉ½¹•ÍÐ…ÕÑ¡½É¥Ñäð)ð€´´´ð€´´´ð)ð5!…Ñ…±½Õ”¹‘‰€ðÁÉ½‘ÕÐ…¹™¥ÉµÝ…É”…Á…‰¥±¥Ñä°5½‘Õ±”½=‰©•Ð…±Ñ•É¹…Ñ¥Ù•Ì°½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¹Ì…¹½¹ÍÑÉ…¥¹ÑÌð)ð=A8¹‘‰€ð¥µÁ±•µ•¹Ñ…Ñ¥½¸™É…µ”Ñ•µÁ±…Ñ•Ì°…‘‘É•ÍÌÉ…µµ…ÉÌ°µ…¹…•µ•¹ÐÝ½É­™±½ÝÌ°…¹Ñ¥µ•½ÕÑÌð)ðÉÕ±•Ì¹‘ˆÍ€ð±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì™½È¥ÑÌÉ•ÁÉ•Í•¹Ñ•=‰©•ÑÌð)ðM•¹…É¥½•Ù¥•Ì‘…Ñ…‰…Í•ÌðÍ•¹…É¥¼µ•‘¥Ñ½È…Á…‰¥±¥Ñä…¹±¥Ñ•É…°½Íåµ‰½±¥Œ½µµ…¹Ñ•µÁ±…Ñ•Ìð)ð=Á•¹EÕ•Éä¹ÑáÑ€ð¹…µ•‘…Ñ…‰…Í”É•…‘Ì…¹Í•±•Ñ•¥µÁ±•µ•¹Ñ…Ñ¥½¸™¥•±‘Ìð)ð½‰Í•ÉÙ•ÑÉ…™™¥Œð…ÑÕ…°¥¹ÍÑ…±±•ÍÑ…Ñ”…¹•Ù¥”‰•¡…Ù¥½Èð)ð5å!=5MÕ¥Ñ”U$ðÁÉ•Í•¹Ñ…Ñ¥½¸°Ù¥Í¥‰¥±¥Ñä°•‘¥Ñ…‰¥±¥Ñä°…¹½‰Í•ÉÙ•…ÁÁ±¥…Ñ¥½¸¡½¥•Ìð)ðÁÉ½‘ÕÐ‘½Õµ•¹Ñ…Ñ¥½¸ðÁ¡åÍ¥…°¡…É‘Ý…É”°½¹™¥ÕÉ…Ñ½È±…å½ÕÐ°…¹ÍÕÁÁ½ÉÑ•¥¹ÍÑ…±±…Ñ¥½¸µ½‘•Ìð)ðÁÕ‰±¥Œ=Á•¹]•‰9•Ðµ…Ñ•É¥…°ðÁÕ‰±¥Í¡•Ý¥É”Í•µ…¹Ñ¥ÌÝ¥Ñ¡¥¸¥ÑÌÙ•ÉÍ¥½¸…¹Í½Á”ð()Q¡”…ÕÑ¡½É¥Ñ…Ñ¥Ù”½¹±ÕÍ¥½¸™½È„ÅÕ•ÍÑ¥½¸½µ•Ì™É½´Ñ¡”Í½ÕÉ”…Á…‰±”½˜…¹ÍÝ•É¥¹œ¥Ð°ÕÍÕ…±±ä½ÉÉ½‰½É…Ñ•‰ä…¹½Ñ¡•È¥¹‘•Á•¹‘•¹Ð±…ÍÌ¸((ŒŒŒ%¹Ù•ÍÑ¥…Ñ¥½¸±¥™•å±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÀÙ€()AÉ½Ù•¹…¹”Õ•Ìè•áÁ•É¥µ•¹Ñ€°Í½ÕÉ•€()Ñ•áÐ)™¥¹•ÉÁÉ¥¹ÐÍ½ÕÉ”+ŠHÁÉ•Í•ÉÙ”É…Ü½‰Í•ÉÙ…Ñ¥½¸+ŠH•¹Õµ•É…Ñ”¹…µ•ÍÁ…•Ì+ŠH™½É´½µÁ•Ñ¥¹œ•áÁ±…¹…Ñ¥½¹Ì+ŠHÑ•ÍÐ½Ù•É…”°…É‘¥¹…±¥Ñä°…¹Í•¹Ñ¥¹•±Ì+ŠHÍ••¬¥¹‘•Á•¹‘•¹Ð½ÉÉ½‰½É…Ñ¥½¸+ŠHÉÕ¸„‘¥ÍÉ¥µ¥¹…Ñ¥¹œ•áÁ•É¥µ•¹Ð+ŠH…ÍÍ¥¸±…¥´µ±•Ù•°½¹™¥‘•¹”+ŠHÁÉ½µ½Ñ”°É•Ñ…¥¸…Ì½Á•¸°½ÈÉ•©•Ð)€()Ð•… ÍÑ•À°ÁÉ•Í•ÉÙ”•¹½Õ ‘•Ñ…¥°™½È…¹½Ñ¡•È¥¹Ù•ÍÑ¥…Ñ½ÈÑ¼É•ÁÉ½‘Õ”Ñ¡”‘•¥Í¥½¸¸((ŒŒŒ±…¥´±¥™•å±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÀÝ€()AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€()¸¥¹Ù•ÍÑ¥…Ñ¥½¸¹½Éµ…±±äÁÉ½‘Õ•Ì½¹”½˜™½ÕÈ½ÕÑ½µ•Ìè()ð=ÕÑ½µ”ð½Õµ•¹Ñ…Ñ¥½¸…Ñ¥½¸ð)ð€´´´ð€´´´ð)ð=Á•É…Ñ¥½¹…±±ä•ÍÑ…‰±¥Í¡•½½ÉÉ½‰½É…Ñ•ðÁÉ½µ½Ñ”Ñ¡”É•ÍÕ±ÐÑ¼¥ÑÌÉ•™•É•¹”Í•Ñ¥½¸…¹ÕÁ‘…Ñ”Ñ¡”I•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Èð)ðMÑÉ½¹±ä¥¹™•ÉÉ•ð‘½Õµ•¹ÐÑ¡”±•…‘¥¹œµ…ÁÁ¥¹œ°µ¥ÍÍ¥¹œÁÉ½½˜°…¹‘¥ÍÉ¥µ¥¹…Ñ¥¹œÑ•ÍÐð)ðMÑ¥±°…µ‰¥Õ½ÕÌðÉ•Ñ…¥¸Ñ¡”…¹‘¥‘…Ñ•Ì…¹•Ù¥‘•¹”¹••‘•¥¸=Á•¸EÕ•ÍÑ¥½¹Ìð)ðI•©•Ñ•ðÉ•½ÉÑ¡”Ñ•µÁÑ¥¹œ¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸…¹½¹™±¥Ñ¥¹œ•Ù¥‘•¹”¥¸I•©•Ñ•I•±…Ñ¥½¹Í¡¥ÁÌð()9•Ü•Ù¥‘•¹”…¸¹…ÉÉ½ÜÍ½Á”°ÁÉ½µ½Ñ”½¹™¥‘•¹”°½ÈÉ•½Á•¸„É•©•Ñ¥½¸Ý¡•¸¥Ð‘¥É•Ñ±ä…‘‘É•ÍÍ•ÌÑ¡”É•©•Ñ¥¹œ•Ù¥‘•¹”¸((ŒŒŒ…¹½¹¥…°•á…µÁ±•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°‘…Ñ…‰…Í•€()Q¡”Í•Ñ¥½¸ÕÍ•ÌÍ•Ù•É…°É•ÕÉÉ¥¹œ•á…µÁ±•Ì‰•…ÕÍ”Ñ¡•ä•áÁ½Í”‘¥™™•É•¹Ð™…¥±ÕÉ”µ½‘•Ìè((´%59M%=8€ÌÀ¹-e=€Í¡½ÝÌ„‘¥ÍÉ¥µ¥¹…Ñ½Èµ‘•Á•¹‘•¹Ð¹…µ•ÍÁ…”Í•±•Ñ•‰äMQQ€¸(´9}=9€Í¡½ÝÌÁ½±åµ½ÉÁ¡¥Œ½Ý¹•ÉÍ¡¥ÀÍ•±•Ñ•‰äé•É¼Í•¹Ñ¥¹•±Ì¸(´9}M1=QM€Í¡½ÝÌÝ¡ä…ÍÍ½¥…Ñ¥½¸µÉ½Ü½Õ¹Ð¥Ì¹½Ð5½‘Õ±”½Õ¹Ð¸(´™¥ÉµÝ…É”X¹H¹‰€Í¡½ÝÌ½µÁ½¹•¹ÐÍ•¹Ñ¥¹•±Ì°µ¥ÍÍ¥¹œÉ½ÝÌ°‘•™…Õ±ÑÌ°…¹½¹”µÑ¼µµ…¹ä‰Õ¥±µ•Ñ…‘…Ñ„¸(´9}IMM}IU1¹½‰©•Ñ}‘•Ù¥•}™…µ¥±å€Í¡½ÝÌ„Ù…±¥É½ÍÌµ‘…Ñ…‰…Í”É•±…Ñ¥½¹Í¡¥ÀÍÕÁÁ½ÉÑ•‰ä™Õ±°½Ù•É…”…¹Í•µ…¹Ñ¥Ì¸(´%59M%=8€ÌÈ¹MeM€Í¡½ÝÌÝ¡ä„ÍÑÉ½¹œÍÑÉÕÑÕÉ…°…¹‘¥‘…Ñ”µÕÍÐÉ•µ…¥¸¥¹™•ÉÉ•Õ¹Ñ¥°„‘¥ÍÉ¥µ¥¹…Ñ¥¹œ…ÁÑÕÉ”•á¥ÍÑÌ¸(´M•¹…É¥½•Ù¥•ÌÉ•Ù¥Í¥½¹ÌÍ¡½ÜÝ¡ä±½…°ÁÉ¥µ…Éä­•åÌ…¹¹½Ð‰”…±¥¹•…É½ÍÌ™¥±•Ì¸(´9}Y%¹½‘”ƒŠH9}19U¹½‘•€Í¡½ÝÌ¡½Ü½±Õµ¸µ¹…µ”Í¥µ¥±…É¥Ñä…¸µ…¹Õ™…ÑÕÉ”„™…±Í”É•±…Ñ¥½¹Í¡¥À¸((ŒŒŒ5¥¹¥µÕ´¥¹Ù•ÍÑ¥…Ñ¥½¸É•½É()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°É•Ù¥Í¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()ÕÍ•™Õ°½¹ÑÉ¥‰ÕÑ¥½¸¥¹±Õ‘•Ìè((´•á…ÐÍ½ÕÉ”É•Ù¥Í¥½¸…¹™¥¹•ÉÁÉ¥¹Ðì(´É…ÜÙ…±Õ•Ì°™É…µ•Ì°½ÈU$½‰Í•ÉÙ…Ñ¥½¹Ìì(´•Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°…¹Í•ÍÍ¥½¸Í½Á”Ý¡•É”…ÁÁ±¥…‰±”ì(´…¹‘¥‘…Ñ”¹…µ•ÍÁ…•Ì…¹…±Ñ•É¹…Ñ¥Ù•Ìì(´•á…ÐME0°É•ÅÕ•ÍÐ°½È½¹ÑÉ½±±•…Ñ¥½¸ì(´­•ä½Ù•É…”°…É‘¥¹…±¥Ñä°Í•¹Ñ¥¹•±Ì°…¹•á•ÁÑ¥½¹Ìì(´ÍÕÁÁ½ÉÑ¥¹œ…¹½¹ÑÉ…‘¥Ñ¥¹œ•Ù¥‘•¹”ì(´½¹™¥‘•¹”…¹™…±Í¥™¥•Èì(´‘•ÍÑ¥¹…Ñ¥½¸É•™•É•¹”Á…”¸()AÉ¥Ù…Ñ”…ÁÑÕÉ•ÌÍ¡½Õ±É•µ…¥¸ÁÉ¥Ù…Ñ”Ý¡•¸Ñ¡•ä½¹Ñ…¥¸¥¹ÍÑ…±±…Ñ¥½¸¥‘•¹Ñ¥™¥•ÉÌ¸AÕ‰±¥Í „ÍÑÉÕÑÕÉ”µÁÉ•Í•ÉÙ¥¹œÉ•‘…Ñ¥½¸…¹É•Ñ…¥¸Ñ¡”½É¥¥¹…°¡…Í ½±½…Ñ¥½¸™½È…Õ‘¥Ð¸((ŒŒŒQ•Éµ¥¹½±½ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°½¹±ä™½É€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘½Õµ•¹Ñ…Ñ¥½¹€°Í½ÕÉ•€()UÍ”Ñ¡”‘½Õµ•¹Ñ…Ñ¥½¸Ì•ÍÑ…‰±¥Í¡•Ñ•ÉµÌ½¹Í¥ÍÑ•¹Ñ±äè((´€¨©A¡åÍ¥…°•Ù¥”¨¨™½ÈÑ¡”¥¹ÍÑ…±±•¡…É‘Ý…É”ì(´€¨©5½‘Õ±”¨¨™½È„™¥ÉµÝ…É”µ•áÁ½Í•±½¥…°½¹Ñ…¥¹•È½™Õ¹Ñ¥½¸Á½Í¥Ñ¥½¸ì(´€¨©Í±½Ñ€¨¨½¹±ä™½ÈÑ¡”¹Õµ•É¥Œ•Ù¥”µ±½…°Á½Í¥Ñ¥½¸…ÉÉ¥•‰ä™É…µ•Ì½È…Ñ…±½Õ”Á±…•µ•¹Ðì(´€¨©=‰©•Ð¨¨™½È9}-e}=	)Q€™Õ¹Ñ¥½¹…±¥Ñäì(´€¨©Y¥É¥¸=‰©•Ð¨¨™½È„½¹™¥ÕÉ…‰±”™Õ¹Ñ¥½¹…°Ñ•µÁ±…Ñ”°¥¹±Õ‘¥¹œÑ¡”¥‘•¹Ñ¥ÑäÉ•Á½ÉÑ•‰ä%59M%=8€ÌÁ€Ý¡¥±”„5½‘Õ±”¥Ì‘¥Í…‰±•ì(´€¨©A¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸¨¨°€¨©Y¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸¨¨°€¨©‘Ù…¹•½¹™¥ÕÉ…Ñ¥½¸¨¨°…¹€¨©AÉ½‘ÕÐAÉ½É…µµ¥¹œ¨¨™½ÈÑ¡”‘¥ÍÑ¥¹Ð…Ñ…±½Õ”µ½‘”±…‰•±ÌÝ¡•É”Ñ¡½Í”½¹•ÁÑÌ…É”µ•…¹ÐìÁÉ•Í•ÉÙ”=A8¹‘‰€Í•ÅÕ•¹”±…‰•±ÌÍ•Á…É…Ñ•±äÉ…Ñ¡•ÈÑ¡…¸ÑÉ•…Ñ¥¹œY¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸…Ì…¸Õµ‰É•±±„™½È…±°5å!=5MÕ¥Ñ”½¹™¥ÕÉ…Ñ¥½¸¸()AÉ•Í•ÉÙ”Í½ÕÉ”™¥•±¹…µ•Ì¥¸½‘”™½Éµ…ÑÑ¥¹œ•Ù•¸Ý¡•¸Ñ¡•¥È¡¥ÍÑ½É¥…°Ñ•Éµ¥¹½±½ä‘¥™™•ÉÌ¸((ŒŒŒMÕ•ÍÌÉ¥Ñ•É¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÌéÌÀÀÀÀÄÅ€()U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€°•áÁ•É¥µ•¹Ñ€()Q¡”lÄàM•ÁÑ•µ‰•È€ÈÀÈØ‘½Õµ•¹Ñ…Ñ¥½¸É•Ù¥•Ýt¡‘½Õµ•¹Ñ…Ñ¥½¸µÉ•Ù¥•Ü´ÈÀÈØ´Àä´Äà¹µ¤É•½É‘ÌÑ¡”½µÁ±•Ñ•É½ÍÌµÍ•Ñ¥½¸½¹Í¥ÍÑ•¹äÁ…ÍÌ°Ù…±¥‘…Ñ¥½¸°…¹É•µ…¥¹¥¹œ•Ù¥‘•¹”±¥µ¥ÑÌ¸()I•Ù•ÉÍ”•¹¥¹••É¥¹œ¥ÌÍÕ•ÍÍ™Õ°Ý¡•¸Õ¹•ÉÑ…¥¹Ñä‰•½µ•ÌÍµ…±±•È°•áÁ±¥¥Ð°…¹Ñ•ÍÑ…‰±”¸%Ð‘½•Ì¹½ÐÉ•ÅÕ¥É”…ÍÍ¥¹¥¹œ„½¹Ù•¹¥•¹Ðµ•…¹¥¹œÑ¼•Ù•ÉäÙ…±Õ”¸()ÁÉ•¥Í”Õ¹­¹½Ý¸Ý¥Ñ „‘¥ÍÉ¥µ¥¹…Ñ¥¹œ•áÁ•É¥µ•¹Ð¥Ì‰•ÑÑ•È‘½Õµ•¹Ñ…Ñ¥½¸Ñ¡…¸…¸Õ¹ÅÕ…±¥™¥•µ…ÁÁ¥¹œÑ¡…Ð¡…ÁÁ•¹ÌÑ¼™¥Ð½¹”…ÁÑÕÉ”¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄÐ()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½…ÁÑÕÉ”µ…¹…±åÍ¥Ì¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒ…ÁÑÕÉ”¹…±åÍ¥Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()=‰Í•ÉÙ•ÑÉ…™™¥ŒÍÕÁÁ±¥•ÌÉÕ¹Ñ¥µ”•Ù¥‘•¹”Ñ¡…ÐÍÑ…Ñ¥Œ‘…Ñ…‰…Í•Ì…¹¹½ÐÁÉ½Ù¥‘”¸%ÐµÕÍÐ‰”…¹…±åé•…Ì„‘¥É•Ñ¥½¸µÍ•¹Í¥Ñ¥Ù”Í•ÍÍ¥½¸½Ù•É¹•‰ä…¸…Ñ¥Ù”Ý½É­™±½Ü°¹½Ð…Ì…¸Õ¹½É‘•É•½±±•Ñ¥½¸½˜™É…µ”ÍÑÉ¥¹Ì¸((ŒŒŒAÉ¥Ù…ä…¹•Ù¥‘•¹”‰½Õ¹‘…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÀÉ€()AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°•Ù¥‘•¹•€()…ÁÑÕÉ•Ì…¸‘¥Í±½Í”•Ù¥”%Ì°…‘‘É•ÍÍ•Ì°¹•ÑÝ½É¬•¹‘Á½¥¹ÑÌ°…ÕÑ¡•¹Ñ¥…Ñ¥½¸ÑÉ…™™¥Œ°¥¹ÍÑ…±±…Ñ¥½¸Ñ½Á½±½ä°ÕÍ•È‰•¡…Ù¥½È°…¹½¹™¥ÕÉ•™Õ¹Ñ¥½¹Ì¸I…ÜÁÉ¥Ù…Ñ”…ÁÑÕÉ•Ì…É”¥¹Ñ•¹Ñ¥½¹…±±ä•á±Õ‘•™É½´Ñ¡”É•Á½Í¥Ñ½Éä¸()AÕ‰±¥Í¡••á…µÁ±•ÌÍ¡½Õ±‰”É•‘…Ñ•½ÈÍå¹Ñ¡•Ñ¥ŒÕ¹±•ÍÌÑ¡”¥‘•¹Ñ¥™¥•ÉÌÝ•É”‘•±¥‰•É…Ñ•±äÍÕÁÁ±¥•…Ì•Ù¥‘•¹”¸I•‘…Ñ¥½¸µÕÍÐÁÉ•Í•ÉÙ”™¥•±Ý¥‘Ñ °Í•Á…É…Ñ½ÉÌ°½É‘•É¥¹œ°•ÅÕ…±¥ÑäÉ•±…Ñ¥½¹Í¡¥ÁÌ°…¹…¹äÁÉ½Á•ÉÑäÉ•±•Ù…¹ÐÑ¼Ñ¡”½¹±ÕÍ¥½¸¸()I•½ÉÑ¡”¡…Í …¹ÁÉ¥Ù…Ñ”±½…Ñ¥½¸½˜Ñ¡”½É¥¥¹…°…ÁÑÕÉ”Í¼Ñ¡…Ð„ÁÕ‰±¥Í¡•‘•É¥Ù…Ñ¥½¸É•µ…¥¹Ì…Õ‘¥Ñ…‰±”Ý¥Ñ¡½ÕÐ½µµ¥ÑÑ¥¹œÍ•¹Í¥Ñ¥Ù”‘…Ñ„¸((ŒŒŒ…ÁÑÕÉ”Ñ¡”ÑÉ…¹ÍÁ½ÉÐ½¹Ñ•áÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€()]¡•É”Á½ÍÍ¥‰±”°É•½É‰½Ñ Ñ¡”=Á•¹]•‰9•ÐÁ…å±½……¹Ñ¡”ÑÉ…¹ÍÁ½ÉÐ•Ù•¹ÑÌ…É½Õ¹¥Ðè((´½¹¹•Ñ¥½¸½Á•¸…¹±½Í”ì(´…Ñ•Ý…ä½Í•ÍÍ¥½¸•ÍÑ…‰±¥Í¡µ•¹Ðì(´Á…å±½…‘¥É•Ñ¥½¸ì(´™É…µ”‰½Õ¹‘…É¥•Ìì(´É•ÑÉ…¹Íµ¥ÍÍ¥½¸½È‘ÕÁ±¥…Ñ”‘•±¥Ù•Éäì(´±½…°µ‰ÕÑÑ½¸½È•Ù¥”µµ½‘”ÑÉ…¹Í¥Ñ¥½¸ì(´Ñ¥µ•½ÕÐ…¹Í½­•Ð™…¥±ÕÉ”¸()¼¹½Ð¥¹™•È™É…µ”‘¥É•Ñ¥½¸™É½´Íå¹Ñ…à…±½¹”¸M•Ù•É…°µ…¹…•µ•¹Ð™É…µ•Ì¡…Ù”¥‘•¹Ñ¥…°Ñ•áÐ¥¸ÁÉ½É…µµ•ÈµÑ¼µ•Ù¥”…¹•Ù¥”µÑ¼µÁÉ½É…µµ•È½¹Ñ•áÑÌ¸((ŒŒŒ…¹½¹¥…°•Ù•¹ÐÉ•½É()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÀÑ€()U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°•Ù¥‘•¹•€()½È•Ù•Éä•Ù•¹Ð°É•Ñ…¥¸è()ð¥•±ðAÕÉÁ½Í”ð)ð€´´´ð€´´´ð)ð…ÁÑÕÉ”¥‘•¹Ñ¥™¥•ÈðÍÑ…‰±”É•™•É•¹”Ñ¼Ñ¡”½É¥¥¹…°•Ù¥‘•¹”ð)ðÑ¥µ•ÍÑ…µÀð½É‘•É¥¹œ°‘•±…ä°…¹Ñ¥µ•½ÕÐ…¹…±åÍ¥Ìð)ð‘¥É•Ñ¥½¸ð‘¥ÍÑ¥¹Õ¥Í¡•ÌÉ•ÅÕ•ÍÑÌ°É•ÍÁ½¹Í•Ì°…¹Í…µ”µÍ¡…Á•…‰½ÉÑÌð)ð½¹¹•Ñ¥½¸½Í•ÍÍ¥½¸ðÁÉ•Ù•¹ÑÌÕ¹É•±…Ñ•ÑÉ…™™¥Œ™É½´‰•¥¹œ½µ‰¥¹•ð)ðÉ…Ü™É…µ”ðÁÉ•Í•ÉÙ•Ì‘•±¥µ¥Ñ•ÉÌ°Á…‘‘¥¹œ°•µÁÑä™¥•±‘Ì°…¹Õ¹­¹½Ý¸Ù…±Õ•Ìð)ðÁ…ÉÍ•É…µµ…ÈðÍ•Á…É…Ñ•Ì]!=€°]!Q€°]!I€°%59M%=9€°…¹Ù…±Õ”™¥•±‘Ìð)ð…Ñ¥Ù”½Á•É…Ñ¥½¸ð‘¥Í½Ù•Éä°¥¹Ñ•ÉÙ¥•Ü°‘•Ñ…¥±•É•…°ÁÉ½É…µµ¥¹œ°½È™Õ¹Ñ¥½¹…°ÑÉ…™™¥Œð)ð…Ñ¥Ù”Í•ÅÕ•¹”ð•áÁ•Ñ•™É…µ•Ì…¹ÑÉ…¹Í¥Ñ¥½¸½¹Ñ•áÐ™É½´=A8¹‘‰€ð)ðÍ•±•Ñ••Ù¥”ð…‘‘É•ÍÌ°±½…°¥¹Ñ•É…Ñ¥½¸°½È•Ù¥”µ%Í•±•Ñ½Èð)ð½ÉÉ•±…Ñ¥½¸­•äðÍ±½Ñ€°½¹™¥ÕÉ…Ñ¥½¸¥¹‘•à°½È½ÕÑÍÑ…¹‘¥¹œÉ•ÅÕ•ÍÐÝ¡•É”…ÁÁ±¥…‰±”ð)ð±…ÍÍ¥™¥…Ñ¥½¸ð•áÁ•Ñ•°½ÁÑ¥½¹…°°É•Á•…Ñ•°Ñ•Éµ¥¹…°°•ÉÉ½È°Ñ¥µ•½ÕÐ°½ÈÕ¹•áÁ•Ñ•ð)ð¹½Ñ•ÌðÕ¹•ÉÑ…¥¹Ñä°É•‘…Ñ¥½¸°½ÈÑÉ…¹ÍÁ½ÉÐ…¹½µ…±äð()MÑ½É”É…Ü…¹Á…ÉÍ•™½ÉµÌÍ•Á…É…Ñ•±ä¸9•Ù•È¹½Éµ…±¥é”±•…‘¥¹œé•É½•Ì°‘•¥µ…°½¡•àÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸°€€µ½‘¥™¥•ÉÌ°•µÁÑä™¥•±‘Ì°½È€©€Í•Á…É…Ñ½ÉÌ¥¸Ñ¡”É…ÜÉ•½É¸((ŒŒŒA…ÉÍ”‰•™½É”¥¹Ñ•ÉÁÉ•Ñ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()A…ÉÍ¥¹œ…¹ÍÝ•ÉÌÝ¡•É”™¥•±‘Ì½ÕÈì¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸…¹ÍÝ•ÉÌÝ¡…ÐÑ¡•äµ•…¸¸-••ÀÑ¡”ÍÑ…•ÌÍ•Á…É…Ñ”¸((Ä¸%‘•¹Ñ¥™äÑ¡”=Á•¹]•‰9•Ð™É…µ”™…µ¥±ä™É½´‘•±¥µ¥Ñ•ÉÌ¸(È¸MÁ±¥Ð½¹±ä…½É‘¥¹œÑ¼Ñ¡”É…µµ…È™½ÈÑ¡…Ð™…µ¥±ä¸(Ì¸AÉ•Í•ÉÙ”•µÁÑä…¹½µÁ½Õ¹™¥•±‘Ì¸(Ð¸I•Í½±Ù”Ñ¡”…Ñ¥Ù”µ…¹…•µ•¹Ð]!=€…¹‘¥É•Ñ¥½¸¸(Ô¸5…Ñ …¸•á…Ð=A8¹‘ˆ¹9}=A9€Ñ•µÁ±…Ñ”Ý¡•É”…Ù…¥±…‰±”¸(Ø¸ÑÑ… Á…É…µ•Ñ•Èµ•Ñ…‘…Ñ„Ý¥Ñ¡½ÕÐÑÉ•…Ñ¥¹œ‘…Ñ…‰…Í”±…‰•±Ì…ÌÕ¹¥Ù•ÉÍ…°ÁÉ½Ñ½½°‘•™¥¹¥Ñ¥½¹Ì¸(Ü¸%¹Ñ•ÉÁÉ•ÐÙ…±Õ•Ì½¹±ä…™Ñ•È•Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°…¹Ý½É­™±½Ü½¹Ñ•áÐ¥Ì…Ù…¥±…‰±”¸()Á±…•¡½±‘•ÈÍÕ …Ìm]}YIM%=9u€…¸•áÁ…¹Ñ¼Y•ÉÍ¥½¸©I•±•…Í”©	Õ¥±‘€ì¥Ð¥Ì¹½Ð¹••ÍÍ…É¥±ä½¹”Í…±…È™¥•±µ•É•±ä‰•…ÕÍ”Ñ¡”Ñ•µÁ±…Ñ”½¹Ñ…¥¹Ì½¹”Á±…•¡½±‘•ÈÑ½­•¸¸((ŒŒŒM•µ•¹ÐÑ¡”Í•ÍÍ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÀÙ€()M•Á…É…Ñ”ÑÉ…™™¥Œ¥¹Ñ¼½Á•É…Ñ¥½¹Ì‰•™½É”½ÉÉ•±…Ñ¥¹œÉ•ÍÁ½¹Í•Ìè((´•Ù¥”•¹Õµ•É…Ñ¥½¸ì(´Á•Èµ•Ù¥”¥¹Ñ•ÉÙ¥•Üì(´‘•Ñ…¥±•=‰©•Ð½½¹™¥ÕÉ…Ñ¥½¸É•…ì(´ÁÉ½É…µµ¥¹œ•¹ÑÉä…¹É•…‘¥¹•ÍÌì(´=‰©•Ð°…‘‘É•ÍÌ°½È½¹™¥ÕÉ…Ñ½ÈÑÉ…¹Í™•Èì(´ÁÉ½É…µµ¥¹œÙ•É¥™¥…Ñ¥½¸ì(´Í•ÍÍ¥½¸±½Í”°•¹µ…É­•È°½È…‰½ÉÐì(´½É‘¥¹…Éä™Õ¹Ñ¥½¹…°ÑÉ…™™¥Œ¸()Q¡”Í…µ”µ…¹…•µ•¹Ð]!=€…¸…ÉÉäÍ•Ù•É…°½Á•É…Ñ¥½¹Ì¸]!Q€Ù…±Õ•Ì…¹%59M%=9€¹Õµ‰•ÉÌ…É”µ•…¹¥¹™Õ°½¹±ä¥¹Í¥‘”Ñ¡”…Ñ¥Ù”½Á•É…Ñ¥½¸…¹‘¥É•Ñ¥½¸¸()UÍ”=A8¹‘‰€Í•¹…É¥¼½Í•ÅÕ•¹”µ•Ñ…‘…Ñ„…Ì…¸¥µÁ±•µ•¹Ñ…Ñ¥½¸µ½‘•°è()Ñ•áÐ)Í•¹…É¥¼+ŠH½É‘•É•Í•ÅÕ•¹”+ŠH½É‘•É•™É…µ”…±Ñ•É¹…Ñ¥Ù•Ì+ŠHÉ•Á•Ñ¥Ñ¥½¸…¹µ…¹‘…Ñ½Éä™±…Ì+ŠHÑ¥µ•½ÕÐ½•ÉÉ½È½Ñ•Éµ¥¹…°ÑÉ…¹Í¥Ñ¥½¸)€()Q¡¥Ìµ½‘•°‘•ÍÉ¥‰•Ì5å!=5MÕ¥Ñ”€Ì¸Ô¸Ìà¸%Ð‘½•Ì¹½ÐÕ…É…¹Ñ•”Ñ¡…Ð•Ù•Éä•Ù¥”•µ¥ÑÌ•Ù•Éä½ÁÑ¥½¹…°É•ÍÁ½¹Í”¸((ŒŒŒ½ÉÉ•±…Ñ”É•ÅÕ•ÍÑÌ…¹É•ÍÁ½¹Í•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÀÝ€()…ÕÑ¥½¹Ìè…Ù½¥‘€()UÍ”Ñ¡”¹…ÉÉ½Ý•ÍÐ…Ù…¥±…‰±”½¹Ñ•áÐ°¥¸Ñ¡¥Ì½É‘•Èè((Ä¸ÑÉ…¹ÍÁ½ÉÐ½¹¹•Ñ¥½¸…¹µ…¹…•µ•¹Ð™…µ¥±äì(È¸…Ñ¥Ù”½Á•É…Ñ¥½¸…¹Í•ÅÕ•¹”ì(Ì¸Í•±•Ñ•A¡åÍ¥…°•Ù¥”½È…‘‘É•ÍÌì(Ð¸±…ÍÐ½ÕÑÍÑ…¹‘¥¹œÉ•ÅÕ•ÍÐì(Ô¸Í±½Ñ€°½¹™¥ÕÉ…Ñ¥½¸¥¹‘•à°½È=‰©•ÐÍ•±•Ñ½Èì(Ø¸É•Á•Ñ¥Ñ¥½¸…¹Ñ¥µ•½ÕÐÝ¥¹‘½Üì(Ü¸Ñ•Éµ¥¹…°½È•ÉÉ½ÈÑÉ…¹Í¥Ñ¥½¸¸()=Á•¹]•‰9•Ðµ…¹…•µ•¹ÐÑÉ…™™¥Œ¡…Ì¹¼•¹•É…°ÑÉ…¹Í…Ñ¥½¸¥‘•¹Ñ¥™¥•È¸Ù½¥Á¥Á•±¥¹¥¹œÉ•ÅÕ•ÍÑÌÝ¡½Í”É•ÍÁ½¹Í•ÌÝ½Õ±Í¡…É”Ñ¡”Í…µ”Í¡…Á”…¹Í•±•Ñ½È¸()%˜Á¥Á•±¥¹¥¹œ¥Ì…±É•…‘äÁÉ•Í•¹Ð°±…ÍÍ¥™ä…µ‰¥Õ½ÕÌ…ÍÍ½¥…Ñ¥½¹Ì•áÁ±¥¥Ñ±ä¥¹ÍÑ•…½˜Í•±•Ñ¥¹œÑ¡”¹•…É•ÍÐÉ•ÅÕ•ÍÐ‰äÑ¥µ•ÍÑ…µÀ¸((ŒŒŒ!…¹‘±”É•Á•Ñ¥Ñ¥½¹Ì°É•ÑÉ¥•Ì°…¹‘ÕÁ±¥…Ñ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÀá€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€()É•Á•…Ñ•É•ÍÁ½¹Í”…¸É•ÁÉ•Í•¹Ðè((´„±•¥Ñ¥µ…Ñ”µÕ±Ñ¤µÉ½ÜÉ•ÍÕ±Ð°ÍÕ …Ì½¹”É½ÜÁ•È5½‘Õ±”ì(´…¸…ÁÁ±¥…Ñ¥½¸É•ÑÉäì(´„•Ù¥”É•ÑÉ…¹Íµ¥ÍÍ¥½¸ì(´Ñ¡”Í…µ”•Ù¥”É•ÍÁ½¹‘¥¹œÑ¼„É•Á•…Ñ•‰ÕÌµÝ¥‘”É•ÅÕ•ÍÐì(´‘ÕÁ±¥…Ñ”ÑÉ…¹ÍÁ½ÉÐ…ÁÑÕÉ”¸()¼¹½Ð‘•‘ÕÁ±¥…Ñ”‰ä™É…µ”Ñ•áÐ…±½¹”¸½µÁ…É”‘¥É•Ñ¥½¸°Ñ¥µ•ÍÑ…µÁÌ°É•ÅÕ•ÍÐå±”°•Ù¥”Í•±•Ñ½È°Í•ÅÕ•¹”Á½Í¥Ñ¥½¸°…¹•áÁ•Ñ•É•Á•Ñ¥Ñ¥½¸µ•Ñ…‘…Ñ„¸()½È‘¥Í½Ù•Éä°ÁÉ•Í•ÉÙ”•… •¹Õµ•É…Ñ¥½¸É½Õ¹¸]!P€ÄÅ€ÅÕ¥•Ñ¥¹œ°É•Á•…Ñ•É•ÅÕ•ÍÑÌ°…‰Í•¹”½˜™ÕÉÑ¡•ÈÉ•Á±¥•Ì°…¹]!P€ÄÉ€É•±•…Í”…É”Á…ÉÐ½˜Ñ¡”É•ÍÕ±Ð°¹½Ð¹½¥Í”…É½Õ¹„±¥ÍÐ½˜•Ù¥”%Ì¸((ŒŒŒ	Õ¥±„ÍÑÉÕÑÕÉ••Ù¥”¥¹Ñ•ÉÙ¥•Ü()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()Q¡”¹½Éµ…±¥é••Ù¥‘•¹”µ½‘•°¥Ìè()Ñ•áÐ)A¡åÍ¥…°•Ù¥”¥¹ÍÑ…¹”+ŠRsŠR ‘¥…¹½ÍÑ¥Œ™…µ¥±ä…¹‘¥Í½Ù•ÉäÍ•±•Ñ½È+ŠRsŠR %59M%=8€Ä…Ñ…±½Õ”µ™…¥¹œ¥‘•¹Ñ¥Ñä+ŠRsŠR ™¥ÉµÝ…É”°¡…É‘Ý…É”°…¹µ¥É½½¹ÑÉ½±±•ÈX¹H¹ˆÙ…±Õ•Ì+ŠRsŠR ¥¹Ñ•É¹…°5½‘Õ±”Í±½Ð+ŠR€ƒŠRsŠR •¹…‰±•É•Õ±…È=‰©•Ð½È‘¥Í…‰±•Y¥É¥¸=‰©•Ð+ŠR€ƒŠRsŠR •¹…‰±•½‘¥Í…‰±•ÍÑ…Ñ”+ŠR€ƒŠRsŠR ÍåÍÑ•´…¹™Õ¹Ñ¥½¹…°…‘‘É•ÍÌ+ŠR€ƒŠRSŠR ¥¹‘•á•…¹=‰©•ÐµÍÁ•¥™¥Œ½¹™¥ÕÉ…Ñ¥½¸Ù…±Õ•Ì+ŠRSŠR •ÉÉ½ÉÌ°½µ¥ÍÍ¥½¹Ì°É•ÑÉ¥•Ì°…¹Ñ•Éµ¥¹…°•Ù¥‘•¹”)€()AÉ•Í•ÉÙ”ÁÉ½Ñ½½°Í±½Ð¹Õµ‰•ÉÌ•Ù•¸Ý¡•¸Ñ¡”U$É•¹Õµ‰•ÉÌÙ¥Í¥‰±”5½‘Õ±•Ì¸ÑÑ… %59M%=8€ÌÉ€…¹€ÌÕ€‘…Ñ„½¹±äÝ¥Ñ Ñ¡”Í…µ”•Ù¥”…¹Í±½Ñ€½¹Ñ•áÐ¸%59M%=8€ÌÔ¹%9a€¥Ì¹½Ð±½‰…±±äÕ¹¥ÅÕ”¸((ŒŒŒ¹…±åé”Ù•ÉÍ¥½¸É•ÍÁ½¹Í•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°É•Ù¥Í¥½¹€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()I•½É™¥ÉµÝ…É”€¡%59M%=8€É€¤°¡…É‘Ý…É”€¡€Í€¤°…¹µ¥É½½¹ÑÉ½±±•È€¡€Ù€¤…ÌÑ¡É•”É…Ü½µÁ½¹•¹ÑÌèY•ÉÍ¥½¸°I•±•…Í”½I•Ù¥Í¥½¸°…¹	Õ¥±¸()½È™¥ÉµÝ…É”½ÉÉ•±…Ñ¥½¸è((´½µÁ…É”Y€…¹I€Ý¥Ñ 9}%I5]I€ì(´½µÁ…É”‰€Ý¥Ñ …ÍÍ½¥…Ñ•9}	U%1M€É½ÝÌì(´ÁÉ•Í•ÉÙ”•áÁ±¥¥Ð€´Å€Í•¹Ñ¥¹•±ÌÍ•Á…É…Ñ•±ä™É½´µ¥ÍÍ¥¹œ‰Õ¥±É½ÝÌì(´É•Ñ…¥¸…±°…¹‘¥‘…Ñ•ÌÕ¹Ñ¥°‘•™…Õ±Ð°±½…±¥é…Ñ¥½¸°…Á…‰¥±¥Ñä°½ÈÉÕ¹Ñ¥µ”•Ù¥‘•¹”‘¥ÍÑ¥¹Õ¥Í¡•ÌÑ¡•´¸()!…É‘Ý…É”…¹µ¥É½½¹ÑÉ½±±•ÈÙ…±Õ•ÌÕÉÉ•¹Ñ±ä¡…Ù”¹¼‘¥É•Ð…Ñ…±½Õ”½±Õµ¹Ì¸-••ÀÑ¡•´…Ì¥¹ÍÑ…±±•µÍÑ…Ñ”•Ù¥‘•¹”É…Ñ¡•ÈÑ¡…¸µ…¹Õ™…ÑÕÉ¥¹œ„©½¥¸¸((ŒŒŒUÍ”‘¥™™•É•¹Ñ¥…°…ÁÑÕÉ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÄÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°•Ù¥‘•¹•€°•áÁ•É¥µ•¹Ñ€()Q¡”ÍÑÉ½¹•ÍÐ‰•¡…Ù¥½É…°•Ù¥‘•¹”¡…¹•Ì½¹”¥¹ÁÕÐÝ¡¥±”¡½±‘¥¹œÑ¡”É•ÍÐ½¹ÍÑ…¹Ð¸()½È•… •áÁ•É¥µ•¹Ðè((Ä¸…ÁÑÕÉ”„½µÁ±•Ñ”‰…Í•±¥¹”½Á•É…Ñ¥½¸ì(È¸¡…¹”½¹”Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½È°U$ÁÉ½Á•ÉÑä°5½‘Õ±”=‰©•Ð°½È…‘‘É•ÍÌì(Ì¸É•Á•…ÐÑ¡”¥‘•¹Ñ¥…°½Á•É…Ñ¥½¸ì(Ð¸…±¥¸™É…µ•Ì‰ä½Á•É…Ñ¥½¸°•Ù¥”°…¹Í±½Ðì(Ô¸É•Á½ÉÐ…‘‘•°É•µ½Ù•°…¹¡…¹•™¥•±‘Ìì(Ø¸É•ÍÑ½É”…¹É•…ÁÑÕÉ”Ñ¡”‰…Í•±¥¹”Ý¡•É”ÁÉ…Ñ¥…°¸()¼¹½Ð½µÁ…É”ÑÝ¼•Ù¥•ÌÝ¥Ñ ‘¥™™•É•¹Ð™¥ÉµÝ…É”…¹½¹™¥ÕÉ…Ñ¥½¸…ÌÑ¡½Õ ½¹”¡…¹•Ù…É¥…‰±”•áÁ±…¥¹Ì•Ù•Éä‘¥™™•É•¹”¸((ŒŒŒQÉ•…Ð•ÉÉ½ÉÌ…ÌÍÑÉÕÑÕÉ••Ù¥‘•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÄÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()I•½É9-€°ÍÑÉÕÑÕÉ•‘¥…¹½ÍÑ¥Œ•ÉÉ½ÉÌ°…‰½ÉÑÌ°‰ÕÍäÉ•ÍÕ±ÑÌ°Ñ¥µ•½ÕÑÌ°…¹Á½Í¥Ñ¥Ù”•¹µ…É­•ÉÌÍ•Á…É…Ñ•±ä¸()¸•ÉÉ½È…¸•ÍÑ…‰±¥Í è((´Ñ¡…ÐÑ¡”•Ù¥”Á…ÉÍ•„Í•±•Ñ½Èì(´Ñ¡…Ð„5½‘Õ±”½È=‰©•ÐÍÑ…Ñ”Ý…ÌÉ•…¡•ì(´Ñ¡…Ð„Ù…±Õ”Ý…Ì½ÕÑÍ¥‘”„ÍÕÁÁ½ÉÑ•‘½µ…¥¸ì(´Ñ¡…ÐÑ¡”½Á•É…Ñ¥½¸Ý…ÌÕ¹…Ù…¥±…‰±”¥¸Ñ¡”ÕÉÉ•¹ÐÍÑ…Ñ”¸()%Ð‘½•Ì¹½Ð…ÕÑ½µ…Ñ¥…±±ä•ÍÑ…‰±¥Í Ý¡¥ Ù…±¥‘…Ñ¥½¸±…å•ÈÉ•©•Ñ•Ñ¡”É•ÅÕ•ÍÐ¸QÉ…¹ÍÁ½ÉÐ‰½Õ¹‘Ì°…Ñ…±½Õ”É…¹•Ì°½¹Ñ•áÑÕ…°™¥±Ñ•ÉÌ°±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì°™¥ÉµÝ…É”‰•¡…Ù¥½È°…¹…ÁÁ±¥…Ñ¥½¸ÁÉ•Ù…±¥‘…Ñ¥½¸É•µ…¥¸‘¥ÍÑ¥¹Ð¸((ŒŒŒ%¹Ñ•ÉÁÉ•ÐÍ¥±•¹”…ÕÑ¥½ÕÍ±ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÄÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()]¡•¸‘½Õµ•¹Ñ¥¹œ…¸…‰Í•¹ÐÉ•ÍÁ½¹Í”°ÁÉ•Í•ÉÙ”Ñ¡”É•ÅÕ•ÍÐ°Í•±•Ñ½È°•Ù¥”ÍÑ…Ñ”°Ñ¥µ•½ÕÐÍ½ÕÉ”°Ñ¥µ•½ÕÐ‘ÕÉ…Ñ¥½¸°É•ÑÉä½Õ¹Ð°½¹¹•Ñ¥½¸¡•…±Ñ °…¹Ñ•Éµ¥¹…°½ÕÑ½µ”¸()M¥±•¹”…¸µ•…¸è((´Õ¹ÍÕÁÁ½ÉÑ•½ÁÑ¥½¹…°É•ÍÁ½¹Í”ì(´¥¹Ù…±¥•Ù¥”½È5½‘Õ±”Í•±•Ñ½Èì(´‘¥Í…‰±•5½‘Õ±”½ÈÕ¹É•Í½±Ù•=‰©•ÐÍÑ…Ñ”ì(´•Ù¥”‰ÕÍä½È¹½Ð¥¸Ñ¡”É•ÅÕ¥É•±½…°µ½‘”ì(´¥¹½µÁ±•Ñ”¥¹Ñ•ÉÙ¥•Üì(´ÑÉ…¹ÍÁ½ÉÐ±½ÍÌì(´¹¼µ…Ñ¡¥¹œ•Ù¥”¸()¸½µ¥ÍÍ¥½¸‰•½µ•Ì„•Ù¥”½™¥ÉµÝ…É”µÍÁ•¥™¥Œ½‰Í•ÉÙ…Ñ¥½¸‰•™½É”¥Ð‰•½µ•Ì„™…µ¥±äµÝ¥‘”ÉÕ±”¸((ŒŒŒAÕ‰±¥…Ñ¥½¸É•½É()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÐéÌÀÀÀÀÄÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°…Ñ…±½Õ•€°‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€°ÍÁ•¥™¥…Ñ¥½¹€()…ÁÑÕÉ”µ‘•É¥Ù•½¹±ÕÍ¥½¸Í¡½Õ±ÁÕ‰±¥Í è((´„É•‘…Ñ•É…Ü•á¡…¹”Ý¥Ñ ‘¥É•Ñ¥½¸ì(´Ñ¡”½Á•É…Ñ¥½¸…¹ÁÉ••‘¥¹œÉ•ÅÕ•ÍÐì(´•Ù¥”¥‘•¹Ñ¥Ñä…¹™¥ÉµÝ…É”Í½Á”ì(´•á…ÐÁ…ÉÍ¥¹œ…¹Õ¹É•Í½±Ù•™¥•±‘Ìì(´…Ñ…±½Õ”½ÍÁ•¥™¥…Ñ¥½¸½ÉÉ•±…Ñ¥½¸ì(´É•Á•Ñ¥Ñ¥½¹Ì…¹•á•ÁÑ¥½¹Ìì(´½¹™¥‘•¹”…¹™…±Í¥™¥•Èì(´Ñ¡”ÁÉ½µ½Ñ•É•™•É•¹”µÁ…”±¥¹¬¸()…ÁÑÕÉ”•Ù¥‘•¹”¥ÌÉ•…‘ä™½ÈÉ•™•É•¹”‘½Õµ•¹Ñ…Ñ¥½¸½¹±äÝ¡•¸¹¼½µÁ•Ñ¥¹œÁ…ÉÍ”¡…¹•ÌÑ¡”½Á•É…Ñ¥½¹…°½¹±ÕÍ¥½¸¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄÔ()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½É½ÍÌµ‘…Ñ…‰…Í”µ½ÉÉ•±…Ñ¥½¸¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒÉ½ÍÌµ…Ñ…‰…Í”½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()É½ÍÌµ‘…Ñ…‰…Í”…¹…±åÍ¥Ì½¹¹•ÑÌµ•…¹¥¹Ì°¹½Ð±½…°ÁÉ¥µ…Éä­•åÌ¸… 5å!=5MÕ¥Ñ”ÍÑ½É”É•ÁÉ•Í•¹ÑÌ„‘¥™™•É•¹ÐÁÉ½©•Ñ¥½¸½˜Ñ¡”ÍåÍÑ•´°…¹=Á•¹]•‰9•ÐÑÉ…™™¥ŒÉ•ÁÉ•Í•¹ÑÌ¥¹ÍÑ…±±•ÉÕ¹Ñ¥µ”ÍÑ…Ñ”¸((ŒŒŒM½ÕÉ”‰½Õ¹‘…É¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€°µÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°Í½ÕÉ•€()ðM½ÕÉ”ðAÉ¥¹¥Á…°µ½‘•°ð5ÕÍÐ¹½Ð‰”…ÍÍÕµ•Ñ¼½¹Ñ…¥¸ð)ð€´´´ð€´´´ð€´´´ð)ð5!…Ñ…±½Õ”¹‘‰€ðÁÉ½‘ÕÑÌ°¥Ñ•µÌ°¥ÉµÝ…É”…Á…‰¥±¥Ñä°5½‘Õ±•Ì°=‰©•ÑÌ°½¹™¥ÕÉ…Ñ¥½¸…¹Ù…±¥‘…Ñ¥½¸ð¥¹ÍÑ…±±••Ù¥”ÍÑ…Ñ”½È½µÁ±•Ñ”™Õ¹Ñ¥½¹…°ÁÉ½Ñ½½°ð)ð=A8¹‘‰€ðÍåÍÑ•µÌ°…‘‘É•ÍÌÉ…µµ…ÉÌ°µ…¹…•µ•¹Ð™É…µ•Ì°Í•ÅÕ•¹•Ì°Ñ¥µ•½ÕÑÌðÁÉ½‘ÕÐ…Ñ…±½Õ”…Á…‰¥±¥Ñä½È…±°™Õ¹Ñ¥½¹…°½µµ…¹‘Ìð)ðÉÕ±•Ì¹‘ˆÍ€ð±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì™½ÈÍ•±•Ñ•=‰©•ÑÌð±½‰…°½¹™¥ÕÉ…Ñ¥½¸‘¥Ñ¥½¹…Éäð)ðM•¹…É¥½•Ù¥•Ì‘…Ñ…‰…Í•ÌðÍ•¹…É¥¼µ•‘¥Ñ½È…Á…‰¥±¥Ñä¡¥•É…É¡äð¥¹ÍÑ…±±•Í•¹…É¥½Ì½È…Ñ…±½Õ”=‰©•Ð¥‘•¹Ñ¥Ñäð)ð=Á•¹EÕ•Éä¹ÑáÑ€ð¹…µ•É•…‘Ì½Ù•ÈÁ…ÉÑÌ½˜=A8¹‘‰€ð½µÁ±•Ñ”…ÁÁ±¥…Ñ¥½¸½¹ÑÉ½°™±½Üð)ð½‰Í•ÉÙ•ÑÉ…™™¥Œð¥¹ÍÑ…±±•ÍÑ…Ñ”…¹…ÑÕ…°ÉÕ¹Ñ¥µ”‰•¡…Ù¥½Èð…Ñ…±½Õ”±…‰•±Ì½ÈÕ¹½‰Í•ÉÙ•…Á…‰¥±¥Ñ¥•Ìð()¼¹½Ð‰•¥¸Ý¥Ñ „µÕ±Ñ¤µ‘…Ñ…‰…Í”©½¥¸½¸Í¥µ¥±…É±ä¹…µ•¥¹Ñ••ÉÌ¸I•Í½±Ù”•… Ù…±Õ”¥¸¥ÑÌ¹…Ñ¥Ù”¹…µ•ÍÁ…”™¥ÉÍÐ¸((ŒŒŒ½ÉÉ•±…Ñ¥½¸Í•ÅÕ•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°Í½ÕÉ•€()UÍ”ÍÑ…•É•Í½±ÕÑ¥½¸è((Ä¸¥‘•¹Ñ¥™äÑ¡”µ…¹…•µ•¹Ð™…µ¥±ä…¹¥¹ÍÑ…±±••Ù¥”Í•±•Ñ½È™É½´ÑÉ…™™¥Œì(È¸Á…ÉÍ”%59M%=8€Å€Ý¥Ñ¡½ÕÐÑÉ…¹Í±…Ñ¥¹œ¥ÑÌÙ…±Õ•ÌÁÉ•µ…ÑÕÉ•±äì(Ì¸É•Í½±Ù”Ñ¡”…Ñ…±½Õ”¥Ñ•´Ñ¡É½Õ µ½‘•°½ÍåÍÑ•´µ•…¹¥¹œì(Ð¸É•Ñ…¥¸…±°½µÁ…Ñ¥‰±”µ…É­•Ñ••Ù¥”½M-TÉ•½É‘Ìì(Ô¸É•Í½±Ù”Ñ¡”Ñ¡É•”µ½µÁ½¹•¹Ð¥ÉµÝ…É”…¹‘¥‘…Ñ”Í•Ðì(Ø¸‰Õ¥±5½‘Õ±”½=‰©•ÐÍÑ…Ñ”™É½´%59M%=8€ÌÁ€ì(Ü¸…ÑÑ… …‘‘É•ÍÍ•Ì…¹½¹™¥ÕÉ…Ñ¥½¸‰ä•Ù¥”…¹Í±½Ñ€ì(à¸É•Í½±Ù”=‰©•ÐÍåÍÑ•µÌ…¹™…µ¥±äì(ä¸Í•±•Ð…¹‘¥‘…Ñ”=A8¹‘‰€…‘‘É•ÍÌÉÕ±•Ì…¹™Õ¹Ñ¥½¹…°½¹Ñ•áÐì(ÄÀ¸…ÁÁ±ä…Ñ…±½Õ”™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¹Ì°½¹Ù•ÉÍ¥½¹Ì°…¹ÉÕ±•Ì¹‘ˆÍ€½¹±ä¥¸Ñ¡…ÐÉ•Í½±Ù•½¹Ñ•áÐì(ÄÄ¸½ÉÉ•±…Ñ”M•¹…É¥½•Ù¥•Ì‰•¡…Ù¥½ÈÑ¡É½Õ ±¥Ñ•É…°™É…µ•Ì½ÈÍ•µ…¹Ñ¥ŒÁ…Ñ¡Ì°¹•Ù•È±½…°%Ì¸()Ð•Ù•ÉäÍÑ…”°ÁÉ•Í•ÉÙ”‰½Ñ Ñ¡”É…ÜÙ…±Õ”…¹Ñ¡”É•Í½±Ù•É•½É¸((…mÉ½ÍÌµ‘…Ñ…‰…Í”½ÉÉ•±…Ñ¥½¸Á…Ñ¡t ¸¸½…ÍÍ•ÑÌ½‘¥…É…µÌ½É½ÍÌµ‘…Ñ…‰…Í”µ½ÉÉ•±…Ñ¥½¸¹ÍÙœ¤()Q¡¥Ì¥Ì„Í•µ…¹Ñ¥ŒÉ•Í½±ÕÑ¥½¸™±½Ü°¹½Ð„Í¡…É•HÍ¡•µ„¸…Í¡•É•±…Ñ¥½¹Í¡¥ÁÌÉ½ÍÌ¥¹‘•Á•¹‘•¹ÐÍ½ÕÉ”µµ½‘•°¹…µ•ÍÁ…•Ì…¹É•ÅÕ¥É”Ñ¡”½¹‘¥Ñ¥½¹Ì‘½Õµ•¹Ñ•‰•±½Ü¸((ŒŒŒ•Ù¥”¥‘•¹Ñ¥Ñä½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()%59M%=8€Å€ÁÉ½Ù¥‘•Ì™½ÕÈ…Ñ…±½Õ”µ™…¥¹œÙ…±Õ•Ìè()ð]¥É”™¥•±ð…Ñ…±½Õ”½ÉÉ•±…Ñ¥½¸ð½¹™¥‘•¹”ð)ð€´´´ð€´´´ð€´´´ð)ð=	)Q}5=1€ðM}%Q5}MeMQ4¹µ½‘½‰©€¥¸Ñ¡”É•Í½±Ù•ÍåÍÑ•´½¹Ñ•áÐð½ÉÉ½‰½É…Ñ•ð)ð½É‘¥¹…Éä…‘‘É•ÍÍ•9}=9€ð¹Õµ‰•È½˜Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹Ìð½ÉÉ½‰½É…Ñ•™½È‘½Õµ•¹Ñ•…‘‘É•ÍÍ••Ù¥•Ìð)ð…Ñ•Ý…ä9}=9€ð¹¼…Ñ…±½Õ”½ÉÉ•±…Ñ¥½¸•ÍÑ…‰±¥Í¡•ìÁÉ•Í•ÉÙ”É…ÜÙ…±Õ”ð½‰Í•ÉÙ•€ÄÕ€½¸5 ÈÀÈ…¹ÐÔÐì•á…ÐÍ•µ…¹Ñ¥ÌÕ¹É•Í½±Ù•ð)ð	I9€ð9}	I9¹‰É…¹‘}µ½‘½‰©€ð½ÉÉ½‰½É…Ñ•ð)ð1%9€ð9}1%9¹±¥¹•}µ½‘½‰©€ð½ÉÉ½‰½É…Ñ•ð()Q¡”•µÁÑäµ]!I€…Ñ•Ý…ä%59M%=8€Å€™½É´µÕÍÐ‰”­•ÁÐÍ•Á…É…Ñ”™É½´Ñ¡”½É‘¥¹…Éä…‘‘É•ÍÍ•¥‘•¹Ñ¥Ñä™½É´¸%ÑÌ½‰Í•ÉÙ•9}=9€ô€ÄÕ€±¥•Ì½ÕÑÍ¥‘”Ñ¡”½É‘¥¹…Éä€À¸¸ÄÉ€É…¹”ì…±Ñ¡½Õ €ÄÔ€ô€Áá€¥Ì½¹Í¥ÍÑ•¹ÐÝ¥Ñ „É•Í•ÉÙ•Í•¹Ñ¥¹•°°¹¼É½ÍÌµ‘…Ñ…‰…Í”É•±…Ñ¥½¸½È…¹½¹¥…°‘•™¥¹¥Ñ¥½¸•ÍÑ…‰±¥Í¡•ÌÑ¡…Ðµ•…¹¥¹œ¸()Q¡”¥¹ÍÑ…±±••Ù¥”%…¹9}Y%¹¥‘}‘•Ù¥•€…É”‘¥™™•É•¹Ð¹…µ•ÍÁ…•Ì¸()á…µÁ±”è½‰Í•ÉÙ•µ½‘•°Ù…±Õ”€ÄÀÝ€É•Í½±Ù•ÌÑ¡É½Õ M}%Q5}MeMQ4¹µ½‘½‰©€Ñ¼Í¡…É•¥Ñ•´€ÄÄàÑ€¸Q¡…Ð¥Ñ•´¥ÌÕÍ•‰äÍ•Ù•É…°µ…É­•Ñ••Ù¥•Ì°¥¹±Õ‘¥¹œ€ØÐÌäÅ€°€ØÐÄäÅ€°…¹€ØÐÄäÉ€¸Q¡”½ÉÉ•ÐÉ•ÍÕ±Ð¥ÌÑ¡•É•™½É”„…¹‘¥‘…Ñ”ÁÉ½‘ÕÐÍ•ÐÕ¹Ñ¥°‰É…¹°±¥¹”°U$½ÁÉ½©•Ð•Ù¥‘•¹”°½È…¹½Ñ¡•È‘¥™™•É•¹Ñ¥…Ñ½ÈÍ•±•ÑÌ½¹”É•½É¸()UÍ”9}Y%¹¹…µ•€…ÌÑ¡”5å!=5MÕ¥Ñ”µ™…¥¹œA¡åÍ¥…°•Ù¥”‘•ÍÉ¥ÁÑ¥½¸¸¼¹½ÐÉ•Á±…”¥ÐÝ¥Ñ …¸=‰©•Ð‘•ÍÉ¥ÁÑ¥½¸™É½´9}-e}=	)Q€¸((ŒŒŒ¥ÉµÝ…É”½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()¥…¹½ÍÑ¥Œ¥ÉµÝ…É”¥Ì„Y•ÉÍ¥½¸©I•±•…Í”©	Õ¥±‘€ÑÕÁ±”¸…Ñ…±½Õ”½ÉÉ•±…Ñ¥½¸¥Ì‘¥ÍÑÉ¥‰ÕÑ•…É½ÍÌè()Ñ•áÐ)9}%I5]I¹™¥ÉµÝ…É•}X)9}%I5]I¹™¥ÉµÝ…É•}H)9}	U%1L¹™¥ÉµÝ…É•}ˆ)€()M•±•Ñ¥½¸µÕÍÐÁÉ•Í•ÉÙ”è((´…±°9}%I5]I€É½ÝÌ‰•±½¹¥¹œÑ¼Ñ¡”É•Í½±Ù•¥Ñ•´ì(´é•É¼°½¹”°½ÈÍ•Ù•É…°9}	U%1M€É½ÝÌÁ•È¥ÉµÝ…É”‘•™¥¹¥Ñ¥½¸ì(´•áÁ±¥¥Ð€´Å€½µÁ½¹•¹ÑÌ…Ì…¹ä½Õ¹ÍÁ•¥™¥•Í•¹Ñ¥¹•±Ìì(´…‰Í•¹”½˜„‰Õ¥±É½Ü…Ì‘¥ÍÑ¥¹Ð™É½´™¥ÉµÝ…É•}ˆ€ô€´Å€ì(´]}‘•™…Õ±Ñ€°ÍÑ…ÑÕÌ°±½…±¥é…Ñ¥½¸°Í±½Ñ€±…å½ÕÐ°…¹…Á…‰¥±¥Ñä‘¥™™•É•¹•Ì¸()Q¡”‘…Ñ…‰…Í•Ì•ÍÑ…‰±¥Í Ñ¡”…¹‘¥‘…Ñ”µ½‘•°‰ÕÐ¹½Ð5å!=5MÕ¥Ñ”Ì•á…ÐÁÉ••‘•¹”…±½É¥Ñ¡´¸!…É‘Ý…É”…¹µ¥É½½¹ÑÉ½±±•ÈX¹H¹‰€É•ÍÁ½¹Í•ÌÕÉÉ•¹Ñ±ä¡…Ù”¹¼‘¥É•Ð…Ñ…±½Õ”™¥•±‘Ì¸((ŒŒŒIÕ¹Ñ¥µ”5½‘Õ±”…¹=‰©•Ð½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()%59M%=8€ÌÁ€¥Ì‘¥ÍÉ¥µ¥¹…Ñ½Èµ‘•Á•¹‘•¹Ðè()Ñ•áÐ)MQQ€ô€ÀƒŠH5½‘Õ±”•¹…‰±•ƒŠH-e<¥Ì9}-e}=	)P¹­•å}½‰©•Ð)MQQ€ô€ÄƒŠH5½‘Õ±”‘¥Í…‰±•ƒŠH-e<¥Ì9}Y%I%9}=	)P¹Ù¥É¥¹}­•å}½‰©•Ð)€()M1=Q€¥ÌÑ¡”•Ù¥”µ±½…°¥¹Ñ•É¹…°Á½Í¥Ñ¥½¸¸%Ð½ÉÉ•±…Ñ•ÌÝ¥Ñ Á±…•µ•¹ÐÑ¡É½Õ 9}M1=QL¹™¥ÉÍÑ}Í±½Ñ€…™Ñ•È¥ÉµÝ…É”É•Í½±ÕÑ¥½¸ì¥Ð¥Ì¹½Ð9}M1=QL¹¥‘}Í±½Ñ€¸()Q¡”Í…™”±½½­ÕÀ½É‘•È¥Ìè((Ä¸É•Í½±Ù”¥ÉµÝ…É”ì(È¸Í•±•ÐÑ¡”É•Á½ÉÑ•Í±½Ñ€ì(Ì¸¡½½Í”Ñ¡”•¹…‰±•É•Õ±…È=‰©•Ð½È‘¥Í…‰±•Y¥É¥¸=‰©•Ð¹…µ•ÍÁ…”™É½´MQQ€ì(Ð¸Ù•É¥™äÑ¡…ÐÑ¡”¥ÉµÝ…É”Á•Éµ¥ÑÌÑ¡…Ð=‰©•Ð½Ñ•µÁ±…Ñ”…ÐÑ¡…ÐÍ±½Ñ€ì(Ô¸É•Ñ…¥¸µ¥Íµ…Ñ¡•Ì…Ì•Ù¥‘•¹”É…Ñ¡•ÈÑ¡…¸™½É¥¹œÑ¡”¹•…É•ÍÐ…¹‘¥‘…Ñ”¸()Q¡¥Ì½É‘•ÈÁÉ•Ù•¹ÑÌ„±½‰…±±äÙ…±¥=‰©•Ð¹Õµ‰•È™É½´‰•¥¹œ…•ÁÑ•¥¸„¥ÉµÝ…É”½Í±½Ñ€Ý¡•É”¥Ð¥ÌÕ¹…Ù…¥±…‰±”¸((ŒŒŒ½¹™¥ÕÉ…Ñ¥½¸½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()%59M%=8€ÌÔ¹%9a€…¹¹½Ð‰”©½¥¹•±½‰…±±äÑ¼9}=9¹¥‘á€¸Q¡”•™™•Ñ¥Ù”±½½­ÕÀ½¹Ñ•áÐ¥Ìè()Ñ•áÐ)A¡åÍ¥…°•Ù¥”(¬™¥ÉµÝ…É”(¬Í±½Ñ€(¬½¹™¥ÕÉ•=‰©•Ð(¬=‰©•ÐµÍ½Á•½È™¥ÉµÝ…É”µÍ½Á•½Ý¹•ÉÍ¡¥À(¬%9`)€()9}=9€½¹Ñ…¥¹ÌÑÝ¼•á±ÕÍ¥Ù”½Ý¹•ÉÍ¡¥ÀÁ…ÑÑ•É¹Ìè()ðM½Á”ðI•ÅÕ¥É•Á…ÑÑ•É¸ð)ð€´´´ð€´´´ð)ð=‰©•ÐµÍ½Á•ðÉ•Í½±Ù•¥‘}­•å}½‰©•Ñ€ì¥‘}™¥ÉµÝ…É”€ô€Á€ð)ð¥ÉµÝ…É”µÍ½Á•ð¥‘}­•å}½‰©•Ð€ô€Á€ìÉ•Í½±Ù•¥‘}™¥ÉµÝ…É•€ð()™Ñ•ÈÉ•Í½±Ù¥¹œÑ¡”ÁÉ½Á•ÉÑä‘•™¥¹¥Ñ¥½¸°Ù…±¥‘…Ñ¥½¸ÁÉ½••‘ÌÑ¡É½Õ ‰…Í”É…¹•Ì°=‰©•Ð½¥ÉµÝ…É”™¥±Ñ•ÉÌ°™¥±Ñ•É•É…¹•Ì°½¹‘¥Ñ¥½¹Ì°½¹Ù•ÉÍ¥½¸ÉÕ±•Ì°…¹±¥¹­•µÁÉ½Á•ÉÑäÉÕ±•Ì¸ÑÉ…¹ÍÁ½ÉÐµÙ…±¥¹Õµ‰•È…¸ÍÑ¥±°‰”¥¹Ù…±¥¥¸Ñ¡…Ð½¹Ñ•áÐ¸((ŒŒŒ=‰©•Ðµ™…µ¥±ä…‘‘É•ÍÌµÉÕ±”É•±…Ñ¥½¹Í¡¥À()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÀá€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()±°€ÄÄ¹½¹é•É¼=A8¹‘ˆ¹9}IMM}IU1¹½‰©•Ñ}‘•Ù¥•}™…µ¥±å€Ù…±Õ•ÌÉ•Í½±Ù”Ñ¼5!…Ñ…±½Õ”¹‘ˆ¹9}=	)Q}%Q5}5%1d¹¥‘}™…µ¥±å€¸IÕ±”‘•ÍÉ¥ÁÑ¥½¹Ì°™…µ¥±ä¹…µ•Ì°…¹=‰©•Ðµ•µ‰•ÉÍ¡¥À…É•”¸()Ñ•áÐ)9}IMM}IU1¹½‰©•Ñ}‘•Ù¥•}™…µ¥±ä(€€€€À€€€€ƒŠH™…µ¥±äµÕ¹ÅÕ…±¥™¥•ÉÕ±”(€€€¹½¹é•É¼ƒŠH9}=	)Q}%Q5}5%1d¹¥‘}™…µ¥±ä(€€€€€€€€€€€€€€€€€ƒŠ@9}-e}=	)P¹¥‘}™…µ¥±ä)€()Q¡¥ÌÉ•±…Ñ¥½¹Í¡¥À¹…ÉÉ½ÝÌÑ¡”…‘‘É•ÍÌÉÕ±•Ì…ÁÁ±¥…‰±”Ñ¼„É•Í½±Ù•=‰©•Ð¸%Ð‘½•Ì¹½Ð‰ä¥ÑÍ•±˜Í•±•ÐÑ¡”…Ñ¥Ù”ÍåÍÑ•´°½¹™¥ÕÉ…Ñ¥½¸µ½‘”°½È™¥¹…°•¹½‘•È¸()Q¡”É½ÍÌµµ½‘•°¡•¬…¸‰”É•ÁÉ½‘Õ•‰ä…ÑÑ…¡¥¹œÑ¡”‘…Ñ…‰…Í•Ì¥¸„‘•É¥Ù•…¹…±åÍ¥Ì½¹¹•Ñ¥½¸è()ÍÅ°)M1P…È¹¥‘}…‘‘É•ÍÍ}ÉÕ±”°(€€€€€€…È¹½‰©•Ñ}‘•Ù¥•}™…µ¥±ä°(€€€€€€˜¹™…µ¥±å}¹…µ”)I=4½Á•¹}‘ˆ¹9}IMM}IU1L…È)1P)=%8…Ñ…±½Õ”¹9}=	)Q}%Q5}5%1dL˜(€=8˜¹¥‘}™…µ¥±ä€ô…È¹½‰©•Ñ}‘•Ù¥•}™…µ¥±ä)]!I…È¹½‰©•Ñ}‘•Ù¥•}™…µ¥±ä€ðø€À(€9˜¹¥‘}™…µ¥±ä%L9U10ì)€()Q¡”•áÁ•Ñ•É•ÍÕ±Ð™½ÈÑ¡”…¹½¹¥…°Á…¥È¥Ì•µÁÑä¸((ŒŒŒ…¹‘¥‘…Ñ”µ…ÁÁ¥¹œ™½È%59M%=8€ÌÈ¹MeM€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)U¹•ÉÑ…¥¹Ñäè¡åÁ½Ñ¡•Í¥Í€°µ…å€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()Q¡”±•…‘¥¹œ…¹‘¥‘…Ñ”¥Ì5!…Ñ…±½Õ”¹‘ˆ¹9}MeMQ4¹ÍåÍ}µ½‘½‰©€¸()ð…¹‘¥‘…Ñ”ðÍÍ•ÍÍµ•¹Ðð)ð€´´´ð€´´´ð)ð…Ñ…±½Õ”¥‘}ÍåÍÑ•µ€ð±½…°ÁÉ¥µ…Éä­•äìÁ…ÉÑ¥…°¹Õµ•É¥Œ½¥¹¥‘•¹”½¹±äð)ð=A8¹‘ˆ¹¥‘}ÍåÍÑ•µ€ð±½…°Ý½É­™±½ÜµÉ•¥ÍÑÉä­•äð)ð™Õ¹Ñ¥½¹…°]!=€ð™Õ¹Ñ¥½¹…°¹…µ•ÍÁ…”°‰ÕÐÁÉ•‘¥Ñ¥½¹Ì‘¥™™•È½ÕÑÍ¥‘”1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸ð)ð‘¥…¹½ÍÑ¥Œ]!=€ðµ…¹…•µ•¹Ð™…µ¥±ä¹Õµ‰•È°¥¹½µÁ…Ñ¥‰±”É½±”ð)ð…Ñ…±½Õ”áµ±}­•å}ÍåÍÑ•µ€ðÕÍ•™Õ°Í•µ…¹Ñ¥Œ¥‘•¹Ñ¥™¥•È‰ÕÐÑ•áÑÕ…°ð)ð…Ñ…±½Õ”ÍåÍ}µ½‘½‰©€ð¹Õµ•É¥Œ•áÑ•É¹…°½µ½‘•°™¥•±…ÍÍ½¥…Ñ•Ý¥Ñ =‰©•ÐÍåÍÑ•µÌìÍÑÉ½¹•ÍÐ…¹‘¥‘…Ñ”ð()ÍåÍ}µ½‘½‰©€½Ù•ÉÌ€À¸¸ÈÅ€¥¸Ñ¡¥ÌÉ•Ù¥Í¥½¸¸5Õ±Ñ¥Á±”ÍåÍÑ•´Ù…É¥…¹ÑÌ…¸Í¡…É”„Ù…±Õ”°…¹½¹”É•ÕÍ…‰±”=‰©•Ð…¸‰•±½¹œÑ¼Í•Ù•É…°ÍåÍÑ•µÌ¸É•Á½ÉÑ•MeM€µ…äÑ¡•É•™½É”Í•±•Ð…¸…Ñ¥Ù”ÍåÍÑ•´½¹Ñ•áÐÉ…Ñ¡•ÈÑ¡…¸¥‘•¹Ñ¥™ä½¹”‘…Ñ…‰…Í”É½Ü¸()Q¡”µ…ÁÁ¥¹œÉ•µ…¥¹ÌÍÑÉ½¹±ä¥¹™•ÉÉ•Õ¹Ñ¥°„¹½¸µ1¥¡Ñ¥¹œ…ÁÑÕÉ”‘¥ÍÑ¥¹Õ¥Í¡•ÌÑ¡”…¹‘¥‘…Ñ•Ì¸M•”m!åÁ½Ñ¡•Í¥ÌQ•ÍÑ¥¹t¡¡åÁ½Ñ¡•Í¥ÌµÑ•ÍÑ¥¹œ¹µ‘¥µ•¹Í¥½¸´ÌÉÍåÌ¤¸((ŒŒŒÉÕ±•Ì¹‘ˆÍ€½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()ÉÕ±•Ì¹‘ˆÍ€ÕÍ•Ì•áÑ•É¹…°=‰©•Ð¹Õµ‰•ÉÌ…¹Ñ•áÑÕ…°½¹™¥ÕÉ…Ñ¥½¸É•™•É•¹•Ìè((´ÉÕ±•Ì¹-=	)QM€½ÉÉ•ÍÁ½¹‘ÌÑ¼9}-e}=	)P¹­•å}½‰©•Ñ€™½È=‰©•ÑÌ€äÕ€°€äÙ€°…¹€ÄàÑ€É•ÁÉ•Í•¹Ñ•¥¸Ñ¡¥ÌÉ•Ù¥Í¥½¸ì(´€‘9€É•™•É•¹•Ì½ÉÉ•ÍÁ½¹Ñ¼9}=9¹¥‘à€ô9€½¹±ä…™Ñ•ÈÑ¡”=‰©•Ð½¹Ñ•áÐ¡…Ì‰••¸Í•±•Ñ•ì(´¹•…Ñ¥Ù”½È‘•½É…Ñ•É•™•É•¹•ÌµÕÍÐ‰”Á…ÉÍ•…½É‘¥¹œÑ¼ÉÕ±”Íå¹Ñ…àÉ…Ñ¡•ÈÑ¡…¸…ÍÐ‰±¥¹‘±äÑ¼¥¹Ñ••ÉÌ¸()Q¡¥Ì‘…Ñ…‰…Í”É•™¥¹•Ì±¥¹­•µÁÉ½Á•ÉÑäÙ…±¥‘…Ñ¥½¸™½ÈÍ•±•Ñ•=‰©•ÑÌ¸%Ð¥Ì¹½Ð„±½‰…°¥¹‘•àµÑ¼µÁÉ½Á•ÉÑäÉ•¥ÍÑÉä¸((ŒŒŒM•¹…É¥½•Ù¥•Ì½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÄÅ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()M•¹…É¥½•Ù¥•ÌÍÕÁÁ±¥•Ì•á…Ð™Õ¹Ñ¥½¹…°™É…µ•Ì™½ÈÍ•±•Ñ•½µµ…¹‘Ì…¹Í•µ…¹Ñ¥ŒÉ•Í½ÕÉ”­•åÌ™½È½Ñ¡•È…Á…‰¥±¥Ñ¥•Ì¸%ÑÌ=‰©•Ñ%‘€°=‰©•Ñ5…Ñ¡¥¹%‘€°½µµ…¹‘%‘€°…¹½µµ…¹‘5…Ñ¡¥¹%‘€É•µ…¥¸±½…°Ñ¼Ñ¡…Ðµ½‘•°¸()M…™”É½ÍÌµµ½‘•°•Ù¥‘•¹”¥¹±Õ‘•Ìè((´„±¥Ñ•É…°™É…µ”Á…ÉÍ•¥¹Ñ¼™Õ¹Ñ¥½¹…°]!=€°]!Q€°]!I€°…¹Ù…±Õ•Ìì(´…É••µ•¹Ð‰•ÑÝ••¸¡¥=Á•¹€…¹Ñ¡”±¥Ñ•É…°™É…µ”Ì]!=€ì(´„É•Í½ÕÉ”µ­•äµ•…¹¥¹œ½ÉÉ½‰½É…Ñ•‰ä™É…µ”…¹•‘¥Ñ½È…Ñ•½Éäì(´™Õ±°Í•µ…¹Ñ¥ŒµÁ…Ñ ½µÁ…É¥Í½¸‰•ÑÝ••¸Ñ¡”ÑÝ¼M•¹…É¥½•Ù¥•ÌÉ•Ù¥Í¥½¹Ì¸()¼¹½Ð•ÅÕ…Ñ”M•¹…É¥½•Ù¥•Ì=‰©•Ñ%‘€Ý¥Ñ 9}-e}=	)P¹­•å}½‰©•Ñ€½È…µ¥±å%‘€Ý¥Ñ ™Õ¹Ñ¥½¹…°]!=€¸((ŒŒŒÙ½¥¥ÉÕ±…ÈÉ•Í½±ÕÑ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÄÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()¸Õ¹Í…™”½ÉÉ•±…Ñ¥½¸±½½­Ì±¥­”Ñ¡¥Ìè((Ä¸Õ•ÍÌ…¸=‰©•Ð™É½´-e=€Ý¥Ñ¡½ÕÐ…ÁÁ±å¥¹œMQQ€ì(È¸Í•±•Ð„¥ÉµÝ…É”É½ÜÑ¡…ÐÍÕÁÁ½ÉÑÌÑ¡…Ð=‰©•Ðì(Ì¸¥Ñ”Ñ¡”Í•±•Ñ•¥ÉµÝ…É”…ÌÁÉ½½˜½˜Ñ¡”=‰©•Ðµ…ÁÁ¥¹œ¸()Q¡”½ÉÉ•ÐÁÉ½•ÍÌÕÍ•Ì…¸¥¹‘•Á•¹‘•¹Ñ±äÉ•Í½±Ù•¥Ñ•´½¥ÉµÝ…É”°Ñ¡”™É…µ”‘¥ÍÉ¥µ¥¹…Ñ½È°…¹Í±½Ñ€Á±…•µ•¹Ð¸%˜Ñ¡½Í”Í½ÕÉ•Ì‘¥Í…É•”°ÁÉ•Í•ÉÙ”Ñ¡”‘¥Í…É••µ•¹Ð¸((ŒŒŒI•ÍÕ±ÐÉ•ÁÉ•Í•¹Ñ…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÔéÌÀÀÀÀÄÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°Í½ÕÉ•€()‘ÕÉ…‰±”É½ÍÌµ‘…Ñ…‰…Í”É•ÍÕ±ÐÍ¡½Õ±É•Ñ…¥¸è()Ñ•áÐ)É…ÜÝ¥É”Ù…±Õ”…¹™É…µ”+ŠHÁ…ÉÍ•Ý¥É”¹…µ•ÍÁ…”+ŠHÍ½ÕÉ”‘…Ñ…‰…Í”…¹É•Ù¥Í¥½¸+ŠH¥¹Ñ•É¹…°É½Ü­•ä+ŠH•áÑ•É¹…°…Ñ…±½Õ”¥‘•¹Ñ¥™¥•È+ŠHÍ•µ…¹Ñ¥Œ±…‰•°+ŠHÁ…É•¹Ð½¹Ñ•áÐ…¹‘¥ÍÉ¥µ¥¹…Ñ½È+ŠH…É‘¥¹…±¥Ñä…¹…¹‘¥‘…Ñ”Í•Ð+ŠH½¹™¥‘•¹”…¹™…±Í¥™¥•È)€()½±±…ÁÍ¥¹œÑ¡•Í”±…å•ÉÌ¥¹Ñ¼½¹”¥¹Ñ••Èµ…­•Ì±…Ñ•ÈÙ…±¥‘…Ñ¥½¸°‘•‰Õ¥¹œ°…¹É•Ù¥Í¥½¸½µÁ…É¥Í½¸Õ¹É•±¥…‰±”¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄØ()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½‘…Ñ…‰…Í”µÉ•±…Ñ¥½¹Í¡¥ÀµÉ•½¹ÍÑÉÕÑ¥½¸¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒ…Ñ…‰…Í”I•±…Ñ¥½¹Í¡¥ÀI•½¹ÍÑÉÕÑ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()5å!=5MÕ¥Ñ”‘…Ñ…‰…Í•ÌÙ…Éä¥¸¡½Ü½µÁ±•Ñ•±äÑ¡•ä‘•±…É”É•±…Ñ¥½¹Í¡¥ÁÌ¸M•¹…É¥½•Ù¥•Ì‘•±…É•Ì¥ÑÌÁÉ¥¹¥Á…°¡¥•É…É¡äÝ¥Ñ ™½É•¥¸­•åÌ°Ý¡¥±”µ…¹ä•¹ÑÉ…°5!…Ñ…±½Õ”¹‘‰€É•±…Ñ¥½¹Í¡¥ÁÌ…É”•¹½‘•½¹±ä‰ä½±Õµ¸É½±•Ì°…ÍÍ½¥…Ñ¥½¸Ñ…‰±•Ì°…¹½µÁ±•Ñ”­•ä½Ù•É…”¸()I•½¹ÍÑÉÕÑ¥½¸‘½Õµ•¹ÑÌÑ¡½Í”É•±…Ñ¥½¹Í¡¥ÁÌÝ¥Ñ¡½ÕÐÉ•ÝÉ¥Ñ¥¹œÑ¡”…¹½¹¥…°•Ù¥‘•¹”¸((ŒŒŒ•±…É•°ÍÑÉÕÑÕÉ…°°…¹Í•µ…¹Ñ¥ŒÉ•±…Ñ¥½¹Í¡¥ÁÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÀÉ€()…ÕÑ¥½¹ÌèµÕÍÐ¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()-••ÀÑ¡É•”­¥¹‘Ì½˜É•±…Ñ¥½¹Í¡¥À‘¥ÍÑ¥¹Ðè()ð-¥¹ðÙ¥‘•¹”ðá…µÁ±”ð)ð€´´´ð€´´´ð€´´´ð)ð•±…É•ðME1¥Ñ”™½É•¥¸­•ä½ÈÁÉ¥µ…Éäµ­•äÍÑÉÕÑÕÉ”ðM•¹…É¥½•Ù¥•Ì½µµ…¹‘Ì¹•Ù¥•=‰©•Ñ}%ƒŠH•Ù¥•=‰©•ÑÌ¹%‘€ð)ðMÑÉÕÑÕÉ…±±äÉ•½¹ÍÑÉÕÑ•ð½µÁ±•Ñ”­•ä½Ù•É…”°½µÁ…Ñ¥‰±”…É‘¥¹…±¥Ñä°…¹Ñ…‰±”É½±”ð9}Y%¹¥‘}¥Ñ•´ƒŠH9}%Q4¹¥‘}¥Ñ•µ€ð)ðM•µ…¹Ñ¥Œ½É½ÍÌµµ½‘•°ð¥¹‘•Á•¹‘•¹Ðµ½‘•±Ì½¹¹•Ñ•‰äµ•…¹¥¹œÉ…Ñ¡•ÈÑ¡…¸„‘…Ñ…‰…Í”­•äð%59M%=8€Ä¹=	)Q}5=0ƒŠHM}%Q5}MeMQ4¹µ½‘½‰©€ð()ÍÑÉÕÑÕÉ…±±äÉ•½¹ÍÑÉÕÑ•É•±…Ñ¥½¹Í¡¥À…¸‰”Í…™”™½È…¹…±åÍ¥ÌÝ¥Ñ¡½ÕÐ‰•¥¹œ‘•±…É•‰äME1¥Ñ”¸É½ÍÌµµ½‘•°É•±…Ñ¥½¹Í¡¥À¹••‘ÌÍÑÉ½¹•ÈÍ•µ…¹Ñ¥Œ½ÉÉ½‰½É…Ñ¥½¸…¹µÕÍÐ¹½Ð‰”ÁÉ•Í•¹Ñ•…Ì„™½É•¥¸­•ä¸((ŒŒŒI•½¹ÍÑÉÕÑ¥½¸Ý½É­™±½Ü()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÀÍ€()½È•Ù•ÉäÁÉ½Á½Í•É•±…Ñ¥½¹Í¡¥Àè((Ä¸¥‘•¹Ñ¥™äÑ¡”¡¥±…¹…¹‘¥‘…Ñ”Á…É•¹Ð¹…µ•ÍÁ…•Ìì(È¸¥¹ÍÁ•ÐÑåÁ•Ì°¹Õ±±…‰¥±¥Ñä°‘•™…Õ±ÑÌ°…¹‘•±…É•½¹ÍÑÉ…¥¹ÑÌì(Ì¸•¹Õµ•É…Ñ”Í•¹Ñ¥¹•°Ù…±Õ•Ì‰•™½É”½Õ¹Ñ¥¹œ½ÉÁ¡…¹Ìì(Ð¸Ñ•ÍÐ•Ù•ÉäÁ½ÁÕ±…Ñ•¹½¸µÍ•¹Ñ¥¹•°Ù…±Õ”ì(Ô¸µ•…ÍÕÉ”…É‘¥¹…±¥Ñä…¹‘ÕÁ±¥…Ñ”Á…É•¹Ð…¹‘¥‘…Ñ•Ìì(Ø¸¥¹ÍÁ•Ð…ÍÍ½¥…Ñ¥½¸µÑ…‰±”Á…Ñ¡ÌÑ¡…Ð‘•Á•¹½¸Ñ¡”É•±…Ñ¥½¹Í¡¥Àì(Ü¸Ñ•ÍÐ½µÁ•Ñ¥¹œÁ…É•¹ÑÌ…¹Í…µ”µ¹…µ•½±Õµ¹Ìì(à¸Í••¬…¸¥¹‘•Á•¹‘•¹ÐÅÕ•Éä°™É…µ”°U$°½ÈÁÉ½‘ÕÐ¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸ì(ä¸É•½ÉÍ½Á”°•á•ÁÑ¥½¹Ì°½¹™¥‘•¹”°…¹„™…±Í¥™¥•Èì(ÄÀ¸…‘ÍÑ…‰±”É•ÍÕ±ÑÌÑ¼Ñ¡”mI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Ét¡É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ¤¸((ŒŒŒM¡•µ„…¹Í½ÕÉ”¥¹ÍÁ•Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÀÑ€()MÑ…ÉÐ™É½´Ñ¡”ÍÑ½É•Í¡•µ„°¹½Ð…¸=I4µÍÑå±”µ½‘•°¥¹™•ÉÉ•™É½´¹…µ•Ìè()ÍÅ°)M1PÑåÁ”°¹…µ”°Ñ‰±}¹…µ”°ÍÅ°)I=4ÍÅ±¥Ñ•}µ…ÍÑ•È)]!IÑåÁ”%8€ Ñ…‰±”œ°€Ù¥•Üœ°€¥¹‘•àœ°€ÑÉ¥•Èœ¤)=IH	dÑåÁ”°¹…µ”ì)€()%¹ÍÁ•Ð•… …¹‘¥‘…Ñ”Ñ…‰±”è()ÍÅ°)AI5Ñ…‰±•}¥¹™¼ 9}Y%œ¤ì)AI5™½É•¥¹}­•å}±¥ÍÐ 9}Y%œ¤ì)AI5¥¹‘•á}±¥ÍÐ 9}Y%œ¤ì)€()Q¡”…‰Í•¹”½˜„‘•±…É•™½É•¥¸­•ä¥Ì„™…Ð…‰½ÕÐ•¹™½É•µ•¹Ð°¹½ÐÁÉ½½˜Ñ¡…Ð¹¼…ÁÁ±¥…Ñ¥½¸É•±…Ñ¥½¹Í¡¥À•á¥ÍÑÌ¸((ŒŒŒM•¹Ñ¥¹•°µ…Ý…É”½ÉÁ¡…¸Ñ•ÍÑ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°¹½Ð…ÁÁ±¥…‰±•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€()¼¹½Ð±…ÍÍ¥™ä„Ù…±Õ”…Ì…¸½ÉÁ¡…¸Õ¹Ñ¥°¥ÑÌÍ•¹Ñ¥¹•°É½±”¡…Ì‰••¸Ñ•ÍÑ•¸()ÍÅ°)M1PŒ¹Á…É•¹Ñ}¥°=U9P ¨¤L½ÕÉÉ•¹•Ì)I=4¡¥±LŒ)1P)=%8Á…É•¹ÐLÀ=8À¹¥€ôŒ¹Á…É•¹Ñ}¥)]!IŒ¹Á…É•¹Ñ}¥%L9=P9U10(€9Œ¹Á…É•¹Ñ}¥€ðø€À(€9À¹¥%L9U10)I=U@	dŒ¹Á…É•¹Ñ}¥ì)€()½µµ½¸Á…ÑÑ•É¹Ì¥¸Ñ¡”½ÉÁÕÌ¥¹±Õ‘”è()ðY…±Õ”Á…ÑÑ•É¸ðÍÑ…‰±¥Í¡•ÕÍ”ð)ð€´´´ð€´´´ð)ð9U11€ð…‰Í•¹Ð½Õ¹­¹½Ý¸Ý¡•É”Ñ¡”½±Õµ¸Á•Éµ¥ÑÌ¥Ðð)ð€Á€ðƒŠq¹½Ð…ÁÁ±¥…‰±—Št‘¥ÍÉ¥µ¥¹…Ñ½È¥¸9}=9€½Ý¹•ÉÍ¡¥Àì™…µ¥±äµÕ¹ÅÕ…±¥™¥•…‘‘É•ÍÌÉÕ±”ð)ð€´Å€ð…¹ä½Õ¹ÍÁ•¥™¥•™¥ÉµÝ…É”½µÁ½¹•¹Ð¥¸ÍÑÉ½¹±ä½ÉÉ½‰½É…Ñ•X¹H¹‰€Á…ÑÑ•É¹Ìð)ð•µÁÑäÑ•áÐð‘¥ÍÑ¥¹Ð™É½´9U11€ìÍ½µ•Ñ¥µ•Ì…¸Õ¹ÕÍ••áÁÉ•ÍÍ¥½¸½È±…‰•°ð()M•¹Ñ¥¹•°µ•…¹¥¹œ¥Ì½±Õµ¸µÍÁ•¥™¥Œ¸9•Ù•ÈÉ•…Ñ”„±½‰…°ÉÕ±”Ñ¡…Ð•Ù•Éä€Á€½È€´Å€¡…ÌÑ¡”Í…µ”Í•µ…¹Ñ¥Ì¸((ŒŒŒA½±åµ½ÉÁ¡¥Œ½Ý¹•ÉÍ¡¥Àè9}=9€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()9}=9€‘•µ½¹ÍÑÉ…Ñ•ÌÝ¡ä½É‘¥¹…Éä™½É•¥¸µ­•ä…ÍÍÕµÁÑ¥½¹Ì…¸‰”‘•ÍÑÉÕÑ¥Ù”è()Ñ•áÐ)=‰©•ÐµÍ½Á•è(€€€¥‘}­•å}½‰©•ÐÉ•Í½±Ù•Ì(€€€¥‘}™¥ÉµÝ…É”€ô€À()¥ÉµÝ…É”µÍ½Á•è(€€€¥‘}­•å}½‰©•Ð€ô€À(€€€¥‘}™¥ÉµÝ…É”É•Í½±Ù•Ì)€()%¸Ñ¡”…¹½¹¥…°‘…Ñ…‰…Í”è()ð=Ý¹•ÉÍ¡¥ÀÁ…ÑÑ•É¸ðI½ÝÌð)ð€´´´ð€´´´ð)ð=‰©•ÐµÍ½Á•ð€Ä°ÐÈÀð)ð¥ÉµÝ…É”µÍ½Á•ð€Ä°ÐØÌð)ð‰½Ñ Á…É•¹ÑÌÁ½ÁÕ±…Ñ•ð€Àð)ð‰½Ñ Á…É•¹ÑÌé•É¼ð€Àð()Q¡”é•É¼¥ÌÁ…ÉÐ½˜…¸•á±ÕÍ¥Ù”‘¥ÍÉ¥µ¥¹…Ñ½È¸QÉ•…Ñ¥¹œ‰½Ñ Á…É•¹Ð½±Õµ¹Ì…Ìµ…¹‘…Ñ½ÉäÝ½Õ±µ…¹Õ™…ÑÕÉ”™…±Í”½ÉÁ¡…¹Ì…¹•É…Í”Ñ¡”‘…Ñ„µ½‘•°¸((ŒŒŒY•É¥™¥•…Ñ…±½Õ”É•±…Ñ¥½¹Í¡¥ÁÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°É•Ù¥Í¥½¹€()Q¡”™½±±½Ý¥¹œ™Õ±°µ½Ù•É…”¡•­Ì¡½±™½È5å!=5MÕ¥Ñ”€Ì¸Ô¸Ìàè()ð¡¥±É•±…Ñ¥½¹Í¡¥ÀðI½ÝÌ¡•­•ð9½¸µÍ•¹Ñ¥¹•°½ÉÁ¡…¹Ìð)ð€´´´ð€´´´ð€´´´ð)ð9}Y%¹¥‘}¥Ñ•´ƒŠH9}%Q4¹¥‘}¥Ñ•µ€ð€ÔÐÄð€Àð)ð9}Y%¹¥‘}‰É…¹ƒŠH9}	I9¹¥‘}‰É…¹‘€ð€ÔÐÄð€Àð)ð9}Y%¹¥‘}±¥¹”ƒŠH9}1%9¹¥‘}±¥¹•€ð€ÔÐÄð€Àð)ð9}%I5]I¹¥‘}¥Ñ•´ƒŠH9}%Q4¹¥‘}¥Ñ•µ€ð€ÌÄÄð€Àð)ð9}	U%1L¹¥‘}™¥ÉµÝ…É”ƒŠH9}%I5]I¹¥‘}™¥ÉµÝ…É•€ð€ÌÀàð€Àð)ðM}%Q5}MeMQ4¹¥‘}¥Ñ•´ƒŠH9}%Q4¹¥‘}¥Ñ•µ€ð€ÈÈÌð€Àð)ðM}%Q5}MeMQ4¹¥‘}ÍåÍÑ•´ƒŠH9}MeMQ4¹¥‘}ÍåÍÑ•µ€ð€ÈÈÌð€Àð)ðM}=	)Q}MeMQ4¹¥‘}­•å}½‰©•ÐƒŠH9}-e}=	)P¹¥‘}­•å}½‰©•Ñ€ð€ÈÔÄð€Àð)ðM}=	)Q}MeMQ4¹¥‘}ÍåÍÑ•´ƒŠH9}MeMQ4¹¥‘}ÍåÍÑ•µ€ð€ÈÔÄð€Àð)ðM}=	)Q}%I5]I€Ñ¼™¥ÉµÝ…É”…¹=‰©•ÐÁ…É•¹ÑÌð€àÈÜð€Àð)ð9}M1=QL¹¥‘}½‰©•Ñ}™¥ÉµÝ…É”ƒŠHM}=	)Q}%I5]I¹¥‘}½‰©•Ñ}™¥ÉµÝ…É•€ð€Ä°ÜÈÔð€Àð)ð9}-e}=	)P¹¥‘}™…µ¥±äƒŠH9}=	)Q}%Q5}5%1d¹¥‘}™…µ¥±å€ð€ÄÔàð€Àð)ðM}%I5]I}Y%I%9}=	)Q€Ñ¼‰½Ñ Á…É•¹ÑÌð€ÜÔð€Àð)ðM}=	)Q}Y%I%9}=	)Q€Ñ¼‰½Ñ Á…É•¹ÑÌð€ÄÀÈð€Àð)ð9}=9}I9¹¥‘}½¹˜ƒŠH9}=9¹¥‘}½¹™€ð€ÄÐ°ÌÐØð€Àð)ð9}%1QI€Ñ¼=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸…¹½¹™¥ÕÉ…Ñ¥½¸ð€Ä°äÀäð€Àð)ðM}M1=Q}=9%Q%=9€Ñ¼Í±½Ð…¹½¹‘¥Ñ¥½¸ð€Ä°ÀÀÀð€Àð()Q¡•Í”½Õ¹ÑÌ•ÍÑ…‰±¥Í É•Ù¥Í¥½¸µÍÁ•¥™¥ŒÍÑÉÕÑÕÉ…°¥¹Ñ•É¥Ñä¸M•µ…¹Ñ¥Ì½µ”™É½´Ñ¡”½µÁ±•Ñ”…Á…‰¥±¥ÑäÁ…Ñ¡Ì…¹Ñ¡•¥ÈÕÍ”¥¸‘¥…¹½ÍÑ¥Ì°ÁÉ½É…µµ¥¹œ°…¹U$‰•¡…Ù¥½È¸((ŒŒŒÍÍ½¥…Ñ¥½¸Á…Ñ¡Ì…¹É½Ü¥‘•¹Ñ¥Ñ¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()%µÁ½ÉÑ…¹Ð…Á…‰¥±¥ÑäÁ…Ñ¡Ì¥¹±Õ‘”è()Ñ•áÐ)•Ù¥”ƒŠHÍ¡…É•¥Ñ•´ƒŠH™¥ÉµÝ…É”ƒŠH=‰©•ÐÍÕÁÁ½ÉÐƒŠHÍ±½ÐÁ±…•µ•¹Ð)€()Ñ•áÐ)™¥ÉµÝ…É”ƒŠHY¥É¥¸=‰©•ÐÍÕÁÁ½ÉÐƒŠHÁ•Éµ¥ÑÑ•=‰©•ÐÍ•ÐƒŠHÍ±½ÐÁ±…•µ•¹Ð)€()Ñ•áÐ)½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¸+ŠH‰…Í”É…¹”+ŠH=‰©•Ð½™¥ÉµÝ…É”½¹Ñ•áÑÕ…°™¥±Ñ•È+ŠH™¥±Ñ•É•É…¹”)€()Ñ•áÐ)Í±½ÐÁ±…•µ•¹ÐƒŠH½¹‘¥Ñ¥½¸ƒŠH½¹Ù•ÉÍ¥½¸ÉÕ±”)€()… …ÍÍ½¥…Ñ¥½¸¡…Ì¥ÑÌ½Ý¸¥‘•¹Ñ¥Ñä…¹Í½Á”¸½È•á…µÁ±”è((´M}=	)Q}%I5]I¹¥‘}½‰©•Ñ}™¥ÉµÝ…É•€¥Ì¹½Ð…¸=‰©•Ð¹Õµ‰•Èì(´9}M1=QL¹¥‘}Í±½Ñ€¥Ì¹½ÐÑ¡”•Ù¥”µ±½…°Í±½Ð…ÉÉ¥•½¸Ñ¡”Ý¥É”ì(´9}-e}=	)P¹¥‘}­•å}½‰©•Ñ€¥Ì¹½Ð9}-e}=	)P¹­•å}½‰©•Ñ€ì(´…¸9}%1QH¹¥‘}™¥±Ñ•É€µÕÍÐ‰”¥¹Ñ•ÉÁÉ•Ñ•¥¸¥ÑÌ=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸½¹Ñ•áÐ¸()MÕ‰ÍÑ¥ÑÕÑ¥¹œ…¸•áÑ•É¹…°¥‘•¹Ñ¥™¥•È™½È…¸…ÍÍ½¥…Ñ¥½¸µÉ½Ü­•ä…¸ÁÉ½‘Õ”…ÁÁ…É•¹Ñ±äÙ…±¥‰ÕÐÍ•µ…¹Ñ¥…±±äÕ¹É•±…Ñ•©½¥¹Ì¸((ŒŒŒ…É‘¥¹…±¥ÑäÑ•ÍÑ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()5•…ÍÕÉ”‰½Ñ ‘¥É•Ñ¥½¹Ìè()ÍÅ°)M1P¥‘}¥Ñ•´°=U9P ¨¤L‘•Ù¥•}É½ÝÌ)I=49}Y%)I=U@	d¥‘}¥Ñ•´)=IH	d‘•Ù¥•}É½ÝÌMì)€()Q¡¥ÌÉ•Ù•…±ÌÑ¡…ÐÍ•Ù•É…°µ…É­•Ñ••Ù¥”½M-TÉ•½É‘Ì…¸Í¡…É”½¹”…Á…‰¥±¥Ñä¥Ñ•´¸Q¡”É•±…Ñ¥½¹Í¡¥À¥Ìµ…¹ä•Ù¥•ÌÑ¼½¹”¥Ñ•´°¹½Ð„Õ¹¥ÅÕ”ÁÉ½‘ÕÐ±½½­ÕÀ¸()1¥­•Ý¥Í”°½Õ¹Ð‘¥ÍÑ¥¹Ð¥¹Ñ•É¹…°Á½Í¥Ñ¥½¹ÌÍ•Á…É…Ñ•±ä™É½´…ÍÍ½¥…Ñ¥½¸É½ÝÌè()ÍÅ°)M1P½™Ü¹¥‘}™¥ÉµÝ…É”°(€€€€€€=U9P¡Ì¹¥‘}Í±½Ð¤L…ÍÍ½¥…Ñ¥½¹}É½ÝÌ°(€€€€€€=U9P¡%MQ%9PÌ¹™¥ÉÍÑ}Í±½Ð¤L¥¹Ñ•É¹…±}Í±½ÑÌ)I=4M}=	)Q}%I5]IL½™Ü))=%89}M1=QLLÌ(€=8Ì¹¥‘}½‰©•Ñ}™¥ÉµÝ…É”€ô½™Ü¹¥‘}½‰©•Ñ}™¥ÉµÝ…É”)I=U@	d½™Ü¹¥‘}™¥ÉµÝ…É”ì)€()=¹”Í±½Ð…¸½™™•ÈÍ•Ù•É…°=‰©•Ð…±Ñ•É¹…Ñ¥Ù•Ì¸=U9P¡9}M1=QLÉ½ÝÌ¥€¥ÌÑ¡•É•™½É”¹½ÐÑ¡”™¥ÉµÝ…É”5½‘Õ±”½Õ¹Ð¸((ŒŒŒ½¹‘¥Ñ¥½¹Ì…¹¥¹‘¥É•ÐÉ•±…Ñ¥½¹Í¡¥ÁÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäè…ÁÁ•…ÉÍ€()9½Ð•Ù•ÉäÉ•±…Ñ¥½¹Í¡¥À¥Ì„‘¥É•Ð•ÅÕ…±¥Ñä©½¥¸¸½¹‘¥Ñ¥½¹Ì°Íåµ‰½±Ì°…¹½¹Ù•ÉÍ¥½¸ÉÕ±•Ì…¸É•™•É•¹”½¹™¥ÕÉ…Ñ¥½¸½¹•ÁÑÌÑ•áÑÕ…±±ä½ÈÑ¡É½Õ „¡…¥¸½˜…ÍÍ½¥…Ñ¥½¹Ì¸()½ÈÑ¡•Í”…Í•Ì°É•ÅÕ¥É”è((´…¸Õ¹…µ‰¥Õ½ÕÌ½Ý¹¥¹œ™¥ÉµÝ…É”½=‰©•Ð½Í±½Ð½¹Ñ•áÐì(´„Á…ÉÍ••áÁÉ•ÍÍ¥½¸½ÈÍåµ‰½°¹…µ•ÍÁ…”ì(´É•Í½±ÕÑ¥½¸½˜•Ù•ÉäÉ•™•É•¹•ÁÉ½Á•ÉÑäì(´‘½Õµ•¹Ñ••Ù…±Õ…Ñ¥½¸½É‘•Èì(´ÉÕ¹Ñ¥µ”½U$½ÉÉ½‰½É…Ñ¥½¸Ý¡•É”‰•¡…Ù¥½È¥Ì±…¥µ•¸()¼¹½Ð½¹Ù•ÉÐÑ•áÑÕ…°É•™•É•¹•Ì¥¹Ñ¼™½É•¥¸­•åÌµ•É•±ä‰•…ÕÍ”„¹Õµ‰•È…ÁÁ•…ÉÌ¥¹Í¥‘”Ñ¡”•áÁÉ•ÍÍ¥½¸¸((ŒŒŒÉ½ÍÌµ‘…Ñ…‰…Í”É•½¹ÍÑÉÕÑ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÄÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()%¹‘•Á•¹‘•¹ÐME1¥Ñ”™¥±•Ì‘¼¹½ÐÍ¡…É”ÁÉ¥µ…Éäµ­•ä¹…µ•ÍÁ…•Ì¸É½ÍÌµ‘…Ñ…‰…Í”É•±…Ñ¥½¹Í¡¥ÀµÕÍÐÍÑ…Ñ”Ý¡•Ñ¡•È¥Ð½¹¹•ÑÌè((´…¸•áÑ•É¹…°¹Õµ‰•È¥¹Ñ•¹Ñ¥½¹…±±äÉ•ÕÍ•…É½ÍÌµ½‘•±Ìì(´„Á…ÉÍ•Ý¥É”Ù…±Õ”Ñ¼…Ñ…±½Õ”µ•Ñ…‘…Ñ„ì(´„É•Í½ÕÉ”µ­•äÍ•µ…¹Ñ¥ŒÁ…Ñ ì(´„™Õ¹Ñ¥½¹…°]!=€•áÑÉ…Ñ•™É½´„±¥Ñ•É…°™É…µ”ì(´„É•Ù¥Í¥½¸µÍÁ•¥™¥Œ‘…Ñ„Á…ÑÑ•É¸¸()½È•á…µÁ±”°…±°€ÄÄ¹½¹é•É¼=A8¹‘ˆ¹9}IMM}IU1¹½‰©•Ñ}‘•Ù¥•}™…µ¥±å€Ù…±Õ•ÌÉ•Í½±Ù”Ñ¼5!…Ñ…±½Õ”¹‘ˆ¹9}=	)Q}%Q5}5%1d¹¥‘}™…µ¥±å€°…¹Ñ¡”ÉÕ±”‘•ÍÉ¥ÁÑ¥½¹Ì…É•”Ý¥Ñ ™…µ¥±äµ•µ‰•ÉÍ¡¥À¸Q¡¥Ì¥Ì„ÍÑÉÕÑÕÉ…±±ä…¹Í•µ…¹Ñ¥…±±ä½ÉÉ½‰½É…Ñ•É½ÍÌµµ½‘•°É•±…Ñ¥½¹Í¡¥À°¹½Ð„‘•±…É•™½É•¥¸­•ä¸()M•”mÉ½ÍÌµ…Ñ…‰…Í”½ÉÉ•±…Ñ¥½¹t¡É½ÍÌµ‘…Ñ…‰…Í”µ½ÉÉ•±…Ñ¥½¸¹µ¤™½ÈÑ¡”ÍÑ…•É•Í½±ÕÑ¥½¸ÉÕ±•Ì¸((ŒŒŒI•Ù¥Í¥½¸½µÁ…É¥Í½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÄÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()9•Ù•È…±¥¸ÑÝ¼‘…Ñ…‰…Í”É•Ù¥Í¥½¹Ì‰ä±½…°É½Ü%…±½¹”¸½µÁ…É”Ñ¡”½µÁ±•Ñ”Í•µ…¹Ñ¥ŒÁ…Ñ è()Ñ•áÐ)=‰©•ÐMåÍÑ•´É•Í½ÕÉ”­•ä…¹…Ñ•½Éä+ŠH•Ù¥”=‰©•ÐÉ•Í½ÕÉ”­•ä…¹•áÑ•É¹…°¥‘•¹Ñ¥™¥•ÉÌ+ŠH½µµ…¹É•Í½ÕÉ”­•ä…¹™É…µ”Í•µ…¹Ñ¥Ì+ŠHA…É…µ•Ñ•ÈÉ•Í½ÕÉ”­•ä°‘½µ…¥¸°…¹Á±…•¡½±‘•È)€()UÍ¥¹œÑ¡¥Ìµ•Ñ¡½°Ñ¡”½µµ½¸M•¹…É¥½•Ù¥•ÌAÉ½É…µ…Ñ„½¹Ñ•¹Ð¥Ì…¸•á…ÐÍ•µ…¹Ñ¥ŒÍÕ‰Í•Ð½˜Ñ¡”AÉ½É…´¥±•Ì½Áä‘•ÍÁ¥Ñ”‘¥Ù•É•¹Ð±½…°%Ì¸()I•Á½ÉÐÉ•Ù¥Í¥½¸½µÁ…É¥Í½¸…Ì…‘‘¥Ñ¥½¹Ì°É•µ½Ù…±Ì°¡…¹•Í•µ…¹Ñ¥ŒÉ½ÝÌ°…¹Õ¹¡…¹•Í•µ…¹Ñ¥ŒÉ½ÝÌ¸¼¹½Ð‘•ÍÉ¥‰”%É•¹Õµ‰•É¥¹œ…Ì„…Á…‰¥±¥Ñä¡…¹”¸((ŒŒŒAÉ•Í•ÉÙ”Ñ¡”…¹½¹¥…°•Ù¥‘•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÄÍ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€°Ý…É¹¥¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°Í½ÕÉ•€()¼¹½Ð…‘¥¹™•ÉÉ•™½É•¥¸­•åÌÑ¼Ñ¡”‘¥ÍÑÉ¥‰ÕÑ•‘…Ñ…‰…Í•Ì¸Á…ÉÐ™É½´¡…¹¥¹œÑ¡”Í½ÕÉ”¡…Í °‘½¥¹œÍ¼…¸¥µÁ½Í”™…±Í”‘•±•Ñ¥½¸½ÕÁ‘…Ñ”‰•¡…Ù¥½È…¹µ¥Í¡…¹‘±”Í•¹Ñ¥¹•±Ì¸()%˜„‘•É¥Ù•½¹ÍÑÉ…¥¹Ðµ•¹…‰±•‘…Ñ…‰…Í”¥ÌÕÍ•™Õ°°±…‰•°¥Ð…Ì•¹•É…Ñ•…¹ÁÕ‰±¥Í è((´Í½ÕÉ”¡…Í ì(´ÑÉ…¹Í™½Éµ…Ñ¥½¸ÍÉ¥ÁÐì(´Í•¹Ñ¥¹•°½•á±ÕÍ¥½¸ÉÕ±•Ìì(´½ÉÁ¡…¸É•Á½ÉÐì(´•¹•É…Ñ•Í¡•µ„¡…Í ì(´•áÁ±¥¥ÐÝ…É¹¥¹œÑ¡…Ð¥Ð¥Ì¹½ÐÑ¡”…¹½¹¥…°5å!=5MÕ¥Ñ”™¥±”¸((ŒŒŒ…±Í”µÁ½Í¥Ñ¥Ù”•á…µÁ±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄØéÌÀÀÀÀÄÑ€()9}Y%¹½‘”ƒŠH9}19U¹½‘•€¥ÌÑ¡”…¹½¹¥…°™…¥±ÕÉ”¸Q¡”½±Õµ¹ÌÍ¡…É”Ñ¡”¹…µ”½‘•€°…¹Í•±•Ñ•Ù…±Õ•Ì…¸…ÁÁ•…È½µÁ…Ñ¥‰±”°‰ÕÐ9}Y%¹½‘•€ÍÑ½É•ÌÁÉ½‘ÕÐ½‘•Ì½M-UÌ¸Q…‰±”É½±”…¹Í•µ…¹Ñ¥ÌÉ•©•ÐÑ¡”É•±…Ñ¥½¹Í¡¥À¸()½±Õµ¸µ¹…µ”Í¥µ¥±…É¥ÑäµÕÍÐ¹•Ù•È½ÕÑÉ…¹¬¹…µ•ÍÁ…”°½Ù•É…”°…É‘¥¹…±¥Ñä°…¹…ÁÁ±¥…Ñ¥½¸µ•…¹¥¹œ¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄÜ()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½‘½Õµ•¹Ñ…Ñ¥½¸µÉ•Ù¥•Ü´ÈÀÈØ´Àä´Äà¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒ½Õµ•¹Ñ…Ñ¥½¸I•Ù¥•Ü€´€ÄàM•ÁÑ•µ‰•È€ÈÀÈØ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÜéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€()Q¡¥ÌÉ•Ù¥•Ü½¹Ñ¥¹Õ•ÌÑ¡”‘½Õµ•¹Ñ…Ñ¥½¸µÝ¥‘”Á…ÍÌ½¸•¹•É…°µ½¹”µ½Ù•É€°ÍÑ…ÉÑ¥¹œ™É½´½µµ¥ÐÅá•‘•˜ÁÅ„ØÍ•‘˜ØÌÅˆÉ‘”áÝˆÜäÜÐÀÌÄÜÁ”Í€¸Q¡”…±É•…‘äµ•É•ÁÉ½Ñ½½°É•Ù¥•Ü…¹•ÍÑ…‰±¥Í¡••Ù¥”5½‘•°°‘¥…¹½ÍÑ¥Œ°ÁÉ½É…µµ¥¹œ°…¹É•Ù•ÉÍ”µ•¹¥¹••É¥¹œ‘•¥Í¥½¹ÌÉ•µ…¥¸Ñ¡”‰…Í•±¥¹”¸((ŒŒŒM½Á”…¹½µÁ±•Ñ•½ÉÉ•Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÜéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°Í½ÕÉ•€()ðÉ•„ðI•Ù¥•ÜÉ•ÍÕ±Ðð)ð€´´´ð€´´´ð)ðAÉ½Ñ½½°ð½ÉÉ•Ñ•Í•ÍÍ¥½¸µÍ•±•Ñ¥½¸½…ÕÑ¡•¹Ñ¥…Ñ¥½¸‰É…¹¡¥¹œ°™¥¹…°±¥•¹Ð…ÕÑ¡•¹Ñ¥…Ñ¥½¸…­¹½Ý±•‘•µ•¹Ð°ÁÉ½½˜Í•É¥…±¥é…Ñ¥½¸°…¹™…¥±ÕÉ”Ñ¡É½ÑÑ±¥¹œìÉ•½É‘•Ñ¡”ÁÕ‰±¥Í¡•¥‘•¹Ñ¥Ñäµ½¹ÍÑ…¹Ð‘¥ÍÉ•Á…¹ä¸ð)ðÕ¹Ñ¥½¹…°É•™•É•¹•ÌðáÁ…¹‘•Q•µÁ•É…ÑÕÉ”½¹ÑÉ½°‘¥µ•¹Í¥½¹Ì…¹¡½±¥‘…ä½µµ…¹‘Ìì½ÉÉ•Ñ•1¥¡Ñ¥¹œ5…¹…•µ•¹Ð…‘‘É•ÍÌ½µÁ½Í¥Ñ¥½¸…¹Á…å±½…‘Ìì…‘‘•M½Õ¹¥™™ÕÍ¥½¸Á…å±½…•á…µÁ±•Ì…¹Í½ÕÉ”‘¥ÍÉ•Á…¹¥•ÌìÉ•µ½Ù•…¸Õ¹ÍÕÁÁ½ÉÑ•…Ñ½µ¥Œµ±½¬Õ…É…¹Ñ•”¸ð)ð¥…¹½ÍÑ¥Ìð‘‘•Ñ¡”ÁÕ‰±¥ŒQ•µÁ•É…ÑÕÉ”½¹ÑÉ½°™…Õ±Ðµ½‘•°°­••Á¥¹œ¥Ð‘¥ÍÑ¥¹Ð™É½´MÕ¥Ñ”•Ù¥”¥¹Ñ•ÉÙ¥•ÝÌì…±¥¹•‘¥Í½Ù•ÉäÑ•Éµ¥¹…Ñ¥½¸…¹Ù•ÉÍ¥½¸µÁ…å±½…•áÁ±…¹…Ñ¥½¹Ì¸ð)ð•Ù¥”5½‘•°ðAÉ•Í•ÉÙ•½¹™¥ÕÉ•=‰©•ÐÙ•ÉÍÕÌY¥É¥¸=‰©•ÐÉ•Í½±ÕÑ¥½¸ì½ÉÉ•Ñ•™¥ÉµÝ…É”€ÄÔÜÌÁ±…•µ•¹Ð½Õ¹ÐÑ¼€ÄÄ…±Ñ•É¹…Ñ¥Ù•Ì…É½ÍÌ™½ÕÈÍ±½Ñ€Á½Í¥Ñ¥½¹Ì¸ð)ðAÉ½É…µµ¥¹œ…¹Õ¥‘•ÌðM½Á•ÁÉ½‘ÕÐÅÕ•É¥•Ì‰ä…Ñ…±½Õ”ÍåÍÑ•´°ÁÉ•Í•ÉÙ•™¥ÉµÝ…É”…¹‘¥‘…Ñ•Ì°½ÉÉ•Ñ•Í±½Ð…¹ÉÕ±”ÅÕ•É¥•Ì°‘¥ÍÑ¥¹Õ¥Í¡•‘•¥µ…°Ý¥É”%Ì™É½´¡•á…‘•¥µ…°‘¥ÍÁ±…ä°…‘‘•±•…¹ÕÀ°…¹ÁÉ½•ÍÍ•…Ñ¥Ù”Í•ÅÕ•¹”½ÕÑ½µ•Ì‰•™½É”ÍÕ‰Í•ÅÕ•¹ÐÝÉ¥Ñ•Ì¸ð)ðM•¹…É¥¼¹¥¹”ð½ÉÉ•Ñ•Í¡…É•µÁ±…•¡½±‘•ÈÉ•¹‘•É¥¹œ…¹Ñ¡”Á…É…µ•Ñ•ÈÑ…‰±”ì¹…ÉÉ½Ý•½Á•¸ÅÕ•ÍÑ¥½¹ÌÑ¼•¹Õ¥¹•±äÕ¹É•Í½±Ù•µ…ÁÁ¥¹Ì¸ð)ð%¹Ñ•É¹…±Ì…¹É•Ù•ÉÍ”•¹¥¹••É¥¹œðAÉ•Í•ÉÙ••ÍÑ…‰±¥Í¡•¹…µ•ÍÁ…”…¹½Ý¹•ÉÍ¡¥À‰½Õ¹‘…É¥•Ìì½ÉÉ•Ñ•„¹½¹•á¥ÍÑ•¹ÐME0½±Õµ¸…¹±…É¥™¥•Ñ¡”Á½Í¥Ñ¥½¸½˜9}=9€¸ð)ð9…Ù¥…Ñ¥½¸…¹ÍÑå±”ðI•Á±…•Á…Ñ µ½¹±ä¹…Ù¥…Ñ¥½¸±…‰•±ÌÝ¥Ñ Á…”Ñ¥Ñ±•Ì°É•µ½Ù••´‘…Í¡•Ì°É•Á…¥É•…¸½‰Í½±•Ñ”…‘‘É•ÍÌ…¹¡½È°…¹¡•­•5…É­‘½Ý¸Ñ…‰±•Ì¸ð()Q¡”…•ÁÑ•¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸½˜%59M%=8€Ä¹9}=9€…Ì„Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈµÁ½Í¥Ñ¥½¸½Õ¹ÐÉ•µ…¥¹Ì¥¹Ñ…Ð¸9}Y%¹¹…µ•€É•µ…¥¹ÌÑ¡”ÁÉ•™•ÉÉ••Ù¥”‘•ÍÉ¥ÁÑ¥½¸ì5½‘Õ±”°Í±½Ñ€°=‰©•Ð°…¹‘…Ñ…‰…Í”É½Ü¥‘•¹Ñ¥ÑäÉ•µ…¥¸Í•Á…É…Ñ”½¹•ÁÑÌ¸á¥ÍÑ¥¹œ½¹”µÁ…”™Õ¹Ñ¥½¹…°É•™•É•¹•ÌÉ•µ…¥¸½¹Í½±¥‘…Ñ•¸((ŒŒŒY…±¥‘…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÜéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°Í½ÕÉ•€((´¡•­••Ù•Éä5…É­‘½Ý¸Á…”™½È±½…°±¥¹¬Ñ…É•ÑÌ…¹¡•…‘¥¹œ™É…µ•¹ÑÌ°Ñ…‰±”µ½±Õµ¸½¹Í¥ÍÑ•¹ä°…¹Ý¡¥Ñ•ÍÁ…”•ÉÉ½ÉÌ¸(´AÉ•Á…É•€ÔÄ½¹É•Ñ”ME0ÍÑ…Ñ•µ•¹ÑÌ……¥¹ÍÐÑ¡”™¥Ù”…¹½¹¥…°ME1¥Ñ”‘…Ñ…‰…Í•Ì°Ý¥Ñ Ñ¡”‘½Õµ•¹Ñ•É½ÍÌµ‘…Ñ…‰…Í”…±¥…Í•Ì¸Q¡É•”•¹•É¥ŒÁ…É•¹Ð½¡¥±Í¡•µ„•á…µÁ±•ÌÝ•É”•á±Õ‘•™É½´ÁÉ•Á…É…Ñ¥½¸‰•…ÕÍ”Ñ¡•ä¥¹Ñ•¹Ñ¥½¹…±±äÕÍ”¥±±ÕÍÑÉ…Ñ¥Ù”Ñ…‰±•Ì¸AÉ•Á…É…Ñ¥½¸¡•­ÌÍ¡•µ„…¹Íå¹Ñ…à°¹½ÐÉÕ¹Ñ¥µ”•Ù¥”‰•¡…Ù¥½È¸(´É½ÍÌµ¡•­•…Ñ…±½Õ”½Õ¹ÑÌ…¹™¥ÉµÝ…É”µÁ±…•µ•¹Ð•á…µÁ±•Ì……¥¹ÍÐÑ¡”…¹½¹¥…°‘…Ñ…‰…Í”ìÉ•Ñ…¥¹•Ý¥±‘…É°µ¥ÍÍ¥¹œµ‰Õ¥±°½Ý¹•ÉÍ¡¥À°…¹µÕ±Ñ¤µÍåÍÑ•´‘¥ÍÑ¥¹Ñ¥½¹Ì¸(´½µÁ…É•…±°€ÈÐ±½…±±ä…Ù…¥±…‰±”…¹½¹¥…°¹½¸µ5…É­‘½Ý¸Í½ÕÉ”™¥±•ÌÝ¥Ñ Ñ¡”‰…Í•±¥¹”¥Ð‰±½ˆ¡…Í¡•Ìè…±°µ…Ñ¡••á…Ñ±ä¸9¼Í½ÕÉ”‘…Ñ…‰…Í”°ÍÕÁÁ½ÉÐ™¥±”°A°½È‘¥…É…´Ý…Ì•‘¥Ñ•¸(´UÍ•Ñ¡”‰…Í•±¥¹”É•µ½Ñ”ÑÉ•”Ý¡•¸ÁÕ‰±¥Í¡¥¹œÍ¼Õ¹…Ù…¥±…‰±”Í½ÕÉ”‰¥¹…É¥•ÌÉ•µ…¥¸ÁÉ•Í•ÉÙ•¸((ŒŒŒÙ¥‘•¹”±¥µ¥ÑÌ…¹É•µ…¥¹¥¹œÉ•Í•…É ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄÜéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€°Í½ÕÉ•€()Q¡¥Ì¥Ì„‘½Õµ•¹Ñ…Ñ¥½¸…¹Í½ÕÉ”µ‘…Ñ„É•Ù¥•Ü°¹½Ð„¡…É‘Ý…É”¥¹Ñ•É½Á•É…‰¥±¥ÑäÑ•ÍÐ¸á¥ÍÑ¥¹œ…ÁÑÕÉ”µ‘•É¥Ù•™¥¹‘¥¹ÌÉ•Ñ…¥¸Ñ¡•¥ÈÍÑ…Ñ•Í½Á”ì¹¼¹•Ü•Ù¥”…ÁÑÕÉ”½ÈÁÉ½É…µµ¥¹œ½Á•É…Ñ¥½¸Ý…ÌÁ•É™½Éµ•¸()QÝ¼…¹½¹¥…°AÌ½Õ±¹½Ð‰”É•ÑÉ¥•Ù•¥¸Ñ¡¥ÌÉ•Ù¥•Ü•¹Ù¥É½¹µ•¹Ðè=Á•¹]•‰9•Ñ}i¥‰•”¹Á‘™€…¹]!=|Ù}0ÐØàÙM,¹Á‘™€¸Q¡•¥È•á¥ÍÑ¥¹œÉ•Á½Í¥Ñ½Éä‰åÑ•Ì…¹ÁÉ•Ù¥½ÕÍ±ä‘½Õµ•¹Ñ•™¥¹‘¥¹Ì…É”ÁÉ•Í•ÉÙ•°‰ÕÐÑ¡¥ÌÁ…ÍÌ‘½•Ì¹½Ð±…¥´„™É•Í Á…”µ‰äµÁ…”Ù•É¥™¥…Ñ¥½¸½˜Ñ¡½Í”™¥±•Ì¸()Q¡”m…ÕÑ¡•¹Ñ¥…Ñ¥½¸É•™•É•¹•t ¸¸½ÁÉ½Ñ½½°½…ÕÑ¡•¹Ñ¥…Ñ¥½¸¹µ¤…¹mM½Õ¹¥™™ÕÍ¥½¸É•™•É•¹•t ¸¸½™Õ¹Ñ¥½¹…°½Ý¡¼´ÈÈµÍ½Õ¹µ‘¥™™ÕÍ¥½¸¼¤¥‘•¹Ñ¥™äÍ½ÕÉ”½¹ÑÉ…‘¥Ñ¥½¹ÌÑ¡…ÐÉ•ÅÕ¥É”¥¹‘•Á•¹‘•¹Ð¥µÁ±•µ•¹Ñ…Ñ¥½¸½ÈÑÉ…™™¥Œ•Ù¥‘•¹”¸=Ñ¡•ÈÕ¹É•Í½±Ù•É•Í•…É °¥¹±Õ‘¥¹œ™¥ÉµÝ…É”µÍ•±•Ñ¥½¸ÁÉ••‘•¹”°½¹™¥ÕÉ…Ñ½ÈµÙ…±Õ”•¹½‘¥¹œ°…¹¹½¸µ1¥¡Ñ¥¹œ½¹™¥Éµ…Ñ¥½¸½˜%59M%=8€ÌÈ¹MeM€°É•µ…¥¹Ì¥¸m=Á•¸EÕ•ÍÑ¥½¹Ít¡½Á•¸µÅÕ•ÍÑ¥½¹Ì¹µ¤¸Q¡•Í”…É”•Ù¥‘•¹”‰½Õ¹‘…É¥•Ì°¹½ÐÉ•…Í½¹ÌÑ¼ÍÕ‰ÍÑ¥ÑÕÑ”ÍÁ•Õ±…Ñ¥Ù”ÁÉ½Ñ½½°‰•¡…Ù¥½È¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄà()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½•Ù¥‘•¹”µ…¹µ½¹™¥‘•¹”¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒÙ¥‘•¹”…¹½¹™¥‘•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÀÅ€()½¹™¥‘•¹”‘•ÍÉ¥‰•ÌÍÕÁÁ½ÉÐ™½È½¹”ÁÉ•¥Í•±äÍ½Á•±…¥´¸%Ð¥Ì¹½Ð„Í½É”™½È…¸•¹Ñ¥É”Á…”°Ñ…‰±”°½ÈÑ¡•½Éä°…¹¥Ð‘½•Ì¹½Ðµ•…ÍÕÉ”¡½ÜÁ±…ÕÍ¥‰±”…¸•áÁ±…¹…Ñ¥½¸Í½Õ¹‘Ì¸((ŒŒŒÙ¥‘•¹”±…ÍÍ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè±¥µ¥Ñ…Ñ¥½¹€)U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()ðÙ¥‘•¹”ðMÑÉ½¹•ÍÐ½¹ÑÉ¥‰ÕÑ¥½¸ðAÉ¥¹¥Á…°±¥µ¥Ñ…Ñ¥½¸ð)ð€´´´ð€´´´ð€´´´ð)ðM½ÕÉ”™¥¹•ÉÁÉ¥¹Ðð¥‘•¹Ñ¥™¥•ÌÑ¡”•á…Ð…ÉÑ¥™…Ð•á…µ¥¹•ðÍ…åÌ¹½Ñ¡¥¹œ…‰½ÕÐÍ•µ…¹Ñ¥Ìð)ð•±…É•Í¡•µ„ð•áÁ±¥¥Ð±½…°­•åÌ°ÑåÁ•Ì°…¹½¹ÍÑÉ…¥¹ÑÌðµ…¹ä…Ñ…±½Õ”É•±…Ñ¥½¹Í¡¥ÁÌ…É”Õ¹‘•±…É•ð)ð½µÁ±•Ñ”‘…Ñ„Á…ÑÑ•É¸ð½Ù•É…”°…É‘¥¹…±¥Ñä°Í•¹Ñ¥¹•±Ì°‘•™…Õ±ÑÌ°…¹•á•ÁÑ¥½¹Ìð…¹¹½ÐÁÉ½Ù”ÉÕ¹Ñ¥µ”‰•¡…Ù¥½È…±½¹”ð)ðÁÁ±¥…Ñ¥½¸ÅÕ•Éäð¥¹Ñ•¹‘•©½¥¹Ì°Í•±•Ñ•½±Õµ¹Ì°…¹½É‘•É¥¹œðµ…ä‰”¥¹½µÁ±•Ñ”°µ…±™½Éµ•°‘½Éµ…¹Ð°½È¥¹Ñ•ÉÁÉ•Ñ••±Í•Ý¡•É”ð)ð1¥Ñ•É…°™É…µ”Ñ•µÁ±…Ñ”ð•á…ÐÍÑ½É•Ý¥É”É…µµ…È…¹¥µÁ±•µ•¹Ñ…Ñ¥½¸½¹Ñ•áÐð‘½•Ì¹½ÐÁÉ½Ù”Ñ¡…Ð•Ù•Éä•Ù¥”¥µÁ±•µ•¹ÑÌ¥Ðð)ð]½É­™±½Üµ•Ñ…‘…Ñ„ð½É‘•É¥¹œ°É•Á•Ñ¥Ñ¥½¸°‘¥É•Ñ¥½¸°Ñ¥µ•½ÕÐ°…¹Ñ•Éµ¥¹…°‰•¡…Ù¥½Èð¥Ñ•É…Ñ¥½¸½Õ¹ÑÌ…¹•Ù¥”µÍÁ•¥™¥Œ½ÁÑ¥½¹…±¥Ñäµ…äÉ•µ…¥¸•áÑ•É¹…°ð)ðAÕ‰±¥ŒÍÁ•¥™¥…Ñ¥½¸ðÁÕ‰±¥Í¡•ÁÉ½Ñ½½°Ñ•Éµ¥¹½±½ä…¹Í•µ…¹Ñ¥Ìðµ…äÁÉ•‘…Ñ”Ñ¡”¥µÁ±•µ•¹Ñ…Ñ¥½¸½È½µ¥ÐÁÉ¥Ù…Ñ”µ…¹…•µ•¹Ð‰•¡…Ù¥½Èð)ð=‰Í•ÉÙ•ÑÉ…™™¥Œð…ÑÕ…°ÉÕ¹Ñ¥µ”½É‘•É¥¹œ…¹•Ù¥”‰•¡…Ù¥½ÈðÍ½Á•Ñ¼Ñ¡”½‰Í•ÉÙ••Ù¥”°™¥ÉµÝ…É”°ÍÑ…Ñ”°…¹ÑÉ…¹ÍÁ½ÉÐð)ð½¹ÑÉ½±±••Ù¥”¡…¹”ð…ÕÍ…°•Ù¥‘•¹”±¥¹­¥¹œ½¹”¥¹ÁÕÐÑ¼½¹”½ÕÑÁÕÐðµ…äÍÑ¥±°‰”ÁÉ½‘ÕÐµÍÁ•¥™¥Œð)ð5å!=5MÕ¥Ñ”U$ð±…‰•±Ì°Ù¥Í¥‰¥±¥Ñä°•‘¥Ñ…‰¥±¥Ñä°…¹…ÁÁ±¥…Ñ¥½¸‰•¡…Ù¥½Èð‘½•Ì¹½Ð•ÍÑ…‰±¥Í Ý¥É”½ÈÍÑ½É…”•¹½‘¥¹œ…±½¹”ð)ðAÉ½‘ÕÐ‘½Õµ•¹Ñ…Ñ¥½¸ð¡…É‘Ý…É”±…å½ÕÐ…¹ÍÕÁÁ½ÉÑ•Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸ðµ…ä¹½Ð‘•ÍÉ¥‰”…‘Ù…¹•½Y¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸½È±…Ñ•ÈÉ•Ù¥Í¥½¹Ìð()9¼Í½ÕÉ”±…ÍÌ¥ÌÕ¹¥Ù•ÉÍ…±±äÍÕÁ•É¥½È¸‘•±…É•±½…°™½É•¥¸­•ä¥Ì‘•¥Í¥Ù”™½È„‘…Ñ…‰…Í”É•±…Ñ¥½¹Í¡¥Àì¥Ð…¹¹½Ð•ÍÑ…‰±¥Í Ñ¡”µ•…¹¥¹œ½˜„‘¥…¹½ÍÑ¥Œ™¥•±¸…ÁÑÕÉ”ÁÉ½Ù•ÌÑ¡…Ð½¹”•Ù¥”•µ¥ÑÑ•„™É…µ”ì¥Ð…¹¹½Ð•ÍÑ…‰±¥Í Õ¹¥Ù•ÉÍ…°ÍÕÁÁ½ÉÐ¸((ŒŒŒ½¹™¥‘•¹”±•Ù•±Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°É•Ù¥Í¥½¹€)U¹•ÉÑ…¥¹Ñäè¡åÁ½Ñ¡•Í¥Í€°µ…å€°Õ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°•Ù¥‘•¹•€()ð1•Ù•°ð5•…¹¥¹œðÁÁÉ½ÁÉ¥…Ñ”Ý½É‘¥¹œð)ð€´´´ð€´´´ð€´´´ð)ðÍÑ…‰±¥Í¡•ð‘¥É•Ñ±ä‘•±…É•°ÍÑ½É•°™¥¹•ÉÁÉ¥¹Ñ•°½ÈÕ¹…µ‰¥Õ½ÕÍ±ä½‰Í•ÉÙ•Ý¥Ñ¡¥¸Ñ¡”ÍÑ…Ñ•Í½Á”ðƒŠq‘•™¥¹•ÏŠt°ƒŠq½¹Ñ…¥¹ÏŠt°ƒŠqÉ•ÑÕÉ¹Ì¥¸Ñ¡¥Ì…ÁÑÕÉ—Štð)ð½ÉÉ½‰½É…Ñ•ð¥¹‘•Á•¹‘•¹Ð•Ù¥‘•¹”±…ÍÍ•ÌÍÕÁÁ½ÉÐÑ¡”Í…µ”¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸…¹Ñ•ÍÑ•…Í•Ì…É•”ðƒŠq½ÉÉ•ÍÁ½¹‘ÏŠt°Ý¥Ñ Í½Á”ÍÑ…Ñ•ð)ðMÑÉ½¹±ä¥¹™•ÉÉ•ð½µÁ±•Ñ”ÍÑÉÕÑÕÉ…°•Ù¥‘•¹”ÍÑÉ½¹±ä™…Ù½ÉÌ½¹”…¹‘¥‘…Ñ”°‰ÕÐ„‘•¥Í¥Ù”½‰Í•ÉÙ…Ñ¥½¸¥Ìµ¥ÍÍ¥¹œðƒŠq±•…‘¥¹œµ…ÁÁ¥¹ŸŠt°ƒŠqÍÑÉ½¹±äÍÕÁÁ½ÉÑÏŠtð)ð!åÁ½Ñ¡•Í¥ÌðÁ±…ÕÍ¥‰±”°Ñ•ÍÑ…‰±”•áÁ±…¹…Ñ¥½¸Ý¥Ñ ¥¹½µÁ±•Ñ”½Ù•É…”½ÈÙ¥…‰±”…±Ñ•É¹…Ñ¥Ù•ÌðƒŠqµ…çŠt°ƒŠqÝ½É­¥¹œ¡åÁ½Ñ¡•Í¥ÏŠtð)ðU¹­¹½Ý¸ð…Ù…¥±…‰±”•Ù¥‘•¹”…¹¹½Ð‘¥ÍÑ¥¹Õ¥Í µ•…¹¥¹ÌðƒŠqÕ¹­¹½Ý»Štì±¥ÍÐ…¹‘¥‘…Ñ•Ì½¹±ä¥˜ÕÍ•™Õ°ð)ðI•©•Ñ•ð•Ù¥‘•¹”½¹™±¥ÑÌÝ¥Ñ Ñ¡”ÁÉ½Á½Í•É•±…Ñ¥½¹Í¡¥À½È¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸ðƒŠq‘½•Ì¹½ÓŠt°Ý¥Ñ Ñ¡”½¹™±¥Ñ¥¹œ•Ù¥‘•¹”ð(+ŠqÍÑ…‰±¥Í¡•“Št¥Ì¹•Ù•È…ÕÑ½µ…Ñ¥…±±äÕ¹¥Ù•ÉÍ…°¸É½Ü½Õ¹Ð•ÍÑ…‰±¥Í¡•™½È5å!=5MÕ¥Ñ”€Ì¸Ô¸ÌàÉ•µ…¥¹ÌÉ•Ù¥Í¥½¸µÍÁ•¥™¥Œ¸ÉÕ¹Ñ¥µ”Í•ÅÕ•¹”•ÍÑ…‰±¥Í¡•™½È½¹”™¥ÉµÝ…É”É•µ…¥¹Ì•Ù¥”´…¹™¥ÉµÝ…É”µÍ½Á•Õ¹±•ÍÌ‰É½…‘•È•Ù¥‘•¹”•á¥ÍÑÌ¸((ŒŒŒ½¹™¥‘•¹”‰•±½¹ÌÑ¼±…¥µÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÙ•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°…Ñ…±½Õ•€°•Ù¥‘•¹•€()M•Á…É…Ñ”½µÁ½Õ¹ÍÑ…Ñ•µ•¹ÑÌ‰•™½É”…ÍÍ¥¹¥¹œ½¹™¥‘•¹”¸½È•á…µÁ±”è((Ä¸%59M%=8€Í€¡…Ì„Y•ÉÍ¥½¸©I•±•…Í”©	Õ¥±‘€±½¥…°™½É´€´•ÍÑ…‰±¥Í¡•‰ä=A8¹‘‰€¸(È¸%Ð¥ÌÉ•ÑÕÉ¹•‰ä„Á…ÉÑ¥Õ±…È•Ù¥”€´•ÍÑ…‰±¥Í¡•½¹±ä‰ä„…ÁÑÕÉ”½˜Ñ¡…Ð•Ù¥”¸(Ì¸%Ðµ…ÁÌÑ¼„…Ñ…±½Õ”½±Õµ¸€´ÕÉÉ•¹Ñ±äÕ¹ÍÕÁÁ½ÉÑ•‰•…ÕÍ”¹¼¡…É‘Ý…É”µÙ•ÉÍ¥½¸½±Õµ¸•á¥ÍÑÌ¸(Ð¸5å!=5MÕ¥Ñ”ÕÍ•Ì¥Ð™½È½µÁ…Ñ¥‰¥±¥ÑäÍ•±•Ñ¥½¸€´½Á•¸ÉÕ¹Ñ¥µ”ÅÕ•ÍÑ¥½¸¸()½µ‰¥¹¥¹œÑ¡•Í”¥¹Ñ¼ƒŠq¡…É‘Ý…É”Ù•ÉÍ¥½¸¥Ì•ÍÑ…‰±¥Í¡•“ŠtÝ½Õ±¡¥‘”Ñ¡É•”‘¥™™•É•¹Ð•Ù¥‘•¹”ÍÑ…Ñ•Ì¸((ŒŒŒ±…¥´É•½É()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°É•Ù¥Í¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€()Ù•Éä¥µÁ½ÉÑ…¹Ð¥¹™•É•¹”Í¡½Õ±‰”É•½Ù•É…‰±”™É½´„½µÁ…Ð±…¥´É•½Éè()ð¥•±ðAÕÉÁ½Í”ð)ð€´´´ð€´´´ð)ð±…¥´ð½¹”ÁÉ•¥Í”°™…±Í¥™¥…‰±”ÍÑ…Ñ•µ•¹Ðð)ðM½ÕÉ”ð™¥±•Ì°Ñ…‰±•Ì°É½ÝÌ°™É…µ•Ì°…ÁÑÕÉ•Ì°U$°½È‘½Õµ•¹ÑÌð)ðI•Ù¥Í¥½¸ðÁÉ½‘ÕÐ½‘…Ñ…‰…Í”½‘½Õµ•¹Ð½™¥ÉµÝ…É”É•Ù¥Í¥½¸ð)ð9…µ•ÍÁ…”ðµ•…¹¥¹œ…¹Í½Á”½˜•Ù•Éä¥‘•¹Ñ¥™¥•È¥¹Ù½±Ù•ð)ð½¹‘¥Ñ¥½¹Ìð‘¥ÍÉ¥µ¥¹…Ñ½ÉÌ°Í•¹Ñ¥¹•±Ì°…¹ÁÉ¥½ÈÉ•Í½±ÕÑ¥½¸É•ÅÕ¥É•ð)ð…É‘¥¹…±¥Ñäð½¹”µÑ¼µ½¹”°½¹”µÑ¼µµ…¹ä°µ…¹äµÑ¼µµ…¹ä°½¹‘¥Ñ¥½¹…°°½ÈÁ½±åµ½ÉÁ¡¥Œð)ð½Ù•É…”ðÑ•ÍÑ•É½ÝÌ°•Ù¥•Ì°™…µ¥±¥•Ì°…¹•á•ÁÑ¥½¹Ìð)ðMÕÁÁ½ÉÑ¥¹œ•Ù¥‘•¹”ð½‰Í•ÉÙ…Ñ¥½¹Ì™…Ù½É¥¹œÑ¡”±…¥´ð)ð½Õ¹Ñ•É•Ù¥‘•¹”ð…¹½µ…±¥•Ì°½¹™±¥ÑÌ°½ÈÕ¹Ñ•ÍÑ•…Í•Ìð)ð±Ñ•É¹…Ñ¥Ù•Ìð½Ñ¡•ÈÙ¥…‰±”•áÁ±…¹…Ñ¥½¹Ìð)ð½¹™¥‘•¹”ð½¹”±•Ù•°™É½´Ñ¡”Ñ…‰±”…‰½Ù”ð)ð…±Í¥™¥•Èð½‰Í•ÉÙ…Ñ¥½¸Ñ¡…ÐÝ½Õ±É•©•Ð½È¹…ÉÉ½ÜÑ¡”±…¥´ð)ð•ÍÑ¥¹…Ñ¥½¸ðÉ•™•É•¹”Á…”½¹Ñ…¥¹¥¹œÑ¡”½Á•É…Ñ¥½¹…°É•ÍÕ±Ðð((ŒŒŒ]½É­•½¹™¥‘•¹”•á…µÁ±”è9}=9€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()Q¡”Í½Á•±…¥´ƒŠq¥¸Ñ¡”½É‘¥¹…Éä…‘‘É•ÍÍ••Ù¥”™½É´°%59M%=8€Ä¹9}=9€¥ÌÑ¡”¹Õµ‰•È½˜Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹ÏŠt¥Ì½ÉÉ½‰½É…Ñ•‰•…ÕÍ”è((´=A8¹‘‰€±…‰•±ÌÑ¡…Ð™¥•±…ÌÑ¡”¹Õµ‰•È½˜Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÉÌ…¹½¹ÍÑÉ…¥¹ÌÑ¡”½É‘¥¹…Éä…‘‘É•ÍÍ•™½É´Ñ¼€À¸¸ÄÉ€ì(´½‰Í•ÉÙ•…‘‘É•ÍÍ•µ™½É´9}=9€Ù…±Õ•Ì…É•”Ý¥Ñ ÁÉ½‘ÕÐ‘¥…É…µÌ™½È•Ù¥•ÌÝ¥Ñ ÑÝ¼°Ñ¡É•”°…¹Í•Ù•¸Á½Í¥Ñ¥½¹Ìì(´É•Í½±Ù•…Ñ…±½Õ”™¥ÉµÝ…É”™¥•±‘Ì¥¹‘•Á•¹‘•¹Ñ±äÁÉ½‘Õ”Ñ¡”Í…µ”½Õ¹ÑÌ¥¸Ñ¡½Í”•á…µÁ±•Ìì(´Ñ¡”™¥•±¥ÌÁ…ÉÐ½˜•Ù¥”¥‘•¹Ñ¥ÑäÉ…Ñ¡•ÈÑ¡…¸„5½‘Õ±”É•½É¸()Q¡”•µÁÑäµ]!I€…Ñ•Ý…ä™½É´ÁÉ•Ù•¹ÑÌÁÉ½µ½Ñ¥½¸½˜Ñ¡…Ð¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸Ñ¼…¸Õ¹½¹‘¥Ñ¥½¹…°%59M%=8€Å€ÉÕ±”¸=‰Í•ÉÙ•5 ÈÀÈ…¹ÐÔÐ…Ñ•Ý…ä¥‘•¹Ñ¥ÑäÉ•ÍÁ½¹Í•Ì‰½Ñ …ÉÉä9}=9€ô€ÄÕ€°½ÕÑÍ¥‘”Ñ¡”½É‘¥¹…Éä€À¸¸ÄÉ€É…¹”¸9Õµ•É¥…±±ä°€ÄÕ€¥Ì€Áá€ìÙ¥•Ý•¥¸™½ÕÈ‰¥ÑÌ°¥Ð¥Ì€ÄÄÄÅ€°…¸…±°µ½¹•ÌÁ…ÑÑ•É¸½¹Í¥ÍÑ•¹ÐÝ¥Ñ „É•Í•ÉÙ•½ÈÍ•¹Ñ¥¹•°½¹Ù•¹Ñ¥½¸‰ÕÐ¹½ÐÁÉ½½˜½˜½¹”¸…Ñ•Ý…ä9}=9€Í•µ…¹Ñ¥ÌÑ¡•É•™½É”É•µ…¥¸Õ¹É•Í½±Ù•¸()Q¡”ÍÑÉ½¹•È…‘‘É•ÍÍ•µ™½É´±…¥´ƒŠq™½È•Ù•Éä™¥ÉµÝ…É”°9}=9€•ÅÕ…±ÌÑ¡”½Õ¹Ð½˜™¥ÉµÝ…É”µÍ½Á•Á¡åÍ¥…°™¥•±‘Ì•á±Õ‘¥¹œ%ƒŠt¥Ì¹½Ðå•Ð•ÅÕ…±±äÍÕÁÁ½ÉÑ•¸½¹‘¥Ñ¥½¹…°™¥•±‘Ì…¹ÁÉ½‘ÕÑÌÝ¥Ñ¡½ÕÐ‘¥…É…µÌÁÉ•Ù•¹Ð…Ñ…±½Õ”µÝ¥‘”ÁÉ½µ½Ñ¥½¸¸Q¡¥Ì•á…µÁ±”‘•µ½¹ÍÑÉ…Ñ•ÌÝ¡ä½¹™¥‘•¹”‰•±½¹ÌÑ¼„Í½Á•±…¥´èÑ¡”…‘‘É•ÍÍ•µ™½É´¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸…¸É•µ…¥¸½ÉÉ½‰½É…Ñ•Ý¡¥±”Ñ¡”…Ñ•Ý…äÙ…É¥…¹ÐÉ•µ…¥¹ÌÕ¹É•Í½±Ù•¸((ŒŒŒ]½É­•½¹™¥‘•¹”•á…µÁ±”è%59M%=8€ÌÈ¹MeM€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÀÝ€()AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€()5!…Ñ…±½Õ”¹‘ˆ¹9}MeMQ4¹ÍåÍ}µ½‘½‰©€¥ÌÑ¡”±•…‘¥¹œ…¹‘¥‘…Ñ”‰•…ÕÍ”¥ÑÌÉ½±”°É…¹”°•áÑ•É¹…°µµ½‘•°¡…É…Ñ•È°…¹=‰©•Ð½ÍåÍÑ•´É…Á ™¥ÐÑ¡”Ý¥É”™¥•±¸!½Ý•Ù•È°½µµ½¸1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸½‰Í•ÉÙ…Ñ¥½¹Ì•ÅÕ…°€Å€°Ý¡¥ …±Í¼µ…Ñ¡•Ì½Ñ¡•È…¹‘¥‘…Ñ”¹…µ•ÍÁ…•Ì¸()Q¡”½ÉÉ•Ð½¹™¥‘•¹”¥ÌÍÑÉ½¹±ä¥¹™•ÉÉ•°¹½Ð½ÉÉ½‰½É…Ñ•¸¹½¸µ1¥¡Ñ¥¹œ…ÁÑÕÉ”Ý¡½Í”…¹‘¥‘…Ñ•ÌÁÉ•‘¥Ð‘¥™™•É•¹ÐÙ…±Õ•Ì¥ÌÑ¡”™…±Í¥™¥•È½‘¥ÍÉ¥µ¥¹…Ñ½È¸((ŒŒŒ%¹‘•Á•¹‘•¹”…¹¥ÉÕ±…É¥Ñä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÀá€()U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()Ù¥‘•¹”¥Ì¥¹‘•Á•¹‘•¹ÐÝ¡•¸¥Ð½Õ±É•…±¥ÍÑ¥…±±ä‘¥Í…É•”¸ÁÉ½‘ÕÐ‘¥…É…´…¹„‘¥…¹½ÍÑ¥Œ…ÁÑÕÉ”…É”¥¹‘•Á•¹‘•¹Ð¸QÝ¼Ñ…‰±•Ì•¹•É…Ñ•™É½´Ñ¡”Í…µ”¥¹Ñ•É¹…°µ½‘•°µ…ä¹½Ð‰”¸()]…Ñ ™½È¥ÉÕ±…ÈÉ•…Í½¹¥¹œè((Ä¸¥¹™•È…¸=‰©•Ð™É½´„™É…µ”ì(È¸ÕÍ”Ñ¡…Ð¥¹™•ÉÉ•=‰©•ÐÑ¼Í•±•Ð„‘…Ñ…‰…Í”É½Üì(Ì¸¥Ñ”Ñ¡”Í•±•Ñ•É½Ü…ÌÁÉ½½˜Ñ¡…ÐÑ¡”™É…µ”µ•…¹ÐÑ¡…Ð=‰©•Ð¸()	É•…¬Ñ¡”¥É±”Ý¥Ñ …¸¥¹‘•Á•¹‘•¹Ð¥‘•¹Ñ¥™¥•È°½¹ÑÉ½±±•¡…¹”°U$½‰Í•ÉÙ…Ñ¥½¸°‘½Õµ•¹Ñ•ÁÉ½‘ÕÐ™Õ¹Ñ¥½¸°½È„‘¥ÍÉ¥µ¥¹…Ñ¥¹œ…ÁÑÕÉ”¸((ŒŒŒ9•…Ñ¥Ù”•Ù¥‘•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÀå€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()‰Í•¹”¥Ì•Ù¥‘•¹”½¹±äÝ¡•¸Ñ¡”½‰Í•ÉÙ…Ñ¥½¸Ý¥¹‘½ÜÝ…Ì…Á…‰±”½˜Í¡½Ý¥¹œÑ¡”•áÁ•Ñ••Ù•¹Ð¸()I•½Éè((´•á…ÐÉ•ÅÕ•ÍÐ…¹Í•±•Ñ½Èì(´•Ù¥”½¹™¥ÕÉ…Ñ¥½¸…¹É•…‘¥¹•ÍÌì(´•áÁ•Ñ•É•ÍÁ½¹Í”…¹Ý¡ä¥ÐÝ…Ì•áÁ•Ñ•ì(´Ñ¥µ•½ÕÐÍ½ÕÉ”…¹‘ÕÉ…Ñ¥½¸ì(´É•ÑÉä½Õ¹Ðì(´Ñ•Éµ¥¹…°°•ÉÉ½È°½È…‰½ÉÐÍÑ…Ñ”ì(´Ý¡•Ñ¡•È½Ñ¡•ÈÑÉ…™™¥ŒÁÉ½Ù•Ñ¡”½¹¹•Ñ¥½¸É•µ…¥¹•¡•…±Ñ¡ä¸()á…µÁ±•Ì½˜Õ¹Í…™”½¹±ÕÍ¥½¹Ì¥¹±Õ‘”è((´¹¼É•ÍÁ½¹Í”…™Ñ•È…¸¥¹Ù…±¥…‘‘É•ÍÌ°Ñ¡•É•™½É”¹¼•Ù¥”•á¥ÍÑÌì(´¹¼½‰Í•ÉÙ•%59M%=8€ÌÕ€°Ñ¡•É•™½É”Ñ¡”=‰©•Ð¡…Ì¹¼½¹™¥ÕÉ…Ñ¥½¸ì(´¹¼M•¹…É¥½•Ù¥•ÌÉ½Ü°Ñ¡•É•™½É”Ñ¡”™Õ¹Ñ¥½¹…°½µµ…¹¥ÌÕ¹ÍÕÁÁ½ÉÑ•ì(´¹¼‘•±…É•™½É•¥¸­•ä°Ñ¡•É•™½É”Ñ¡”½±Õµ¹Ì…É”Õ¹É•±…Ñ•¸((ŒŒŒ½¹ÑÉ…‘¥Ñ¥½¹Ì…¹•á•ÁÑ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°É•Ù¥Í¥½¹€°Ù•ÉÍ¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()¼¹½Ð…Ù•É…”½¹™±¥Ñ¥¹œ•Ù¥‘•¹”¥¹Ñ¼„Ù…Õ”½¹™¥‘•¹”±…‰•°¸•Ñ•Éµ¥¹”Ý¡•Ñ¡•ÈÑ¡”½¹™±¥Ð¥¹‘¥…Ñ•Ìè((´„Á…ÉÍ¥¹œ•ÉÉ½Èì(´„‘¥™™•É•¹Ð¹…µ•ÍÁ…”ì(´„µ¥ÍÍ¥¹œ‘¥ÍÉ¥µ¥¹…Ñ½Èì(´™¥ÉµÝ…É”½ÈÁÉ½‘ÕÐÙ…É¥…Ñ¥½¸ì(´‘…Ñ…‰…Í”É•Ù¥Í¥½¸‘É¥™Ðì(´½¹‘¥Ñ¥½¹…°…ÁÁ±¥…Ñ¥½¸‰•¡…Ù¥½Èì(´…¸…ÑÕ…°½Õ¹Ñ•É•á…µÁ±”¸()I•½É•á•ÁÑ¥½¹Ì‰•Í¥‘”Ñ¡”±…¥´¸É•±…Ñ¥½¹Í¡¥ÀÝ¥Ñ •áÁ±¥¥Ð½¹‘¥Ñ¥½¹Ì…¸É•µ…¥¸•ÍÑ…‰±¥Í¡••Ù•¸Ý¡•¸…¸Õ¹½¹‘¥Ñ¥½¹…°Ù•ÉÍ¥½¸¥ÌÉ•©•Ñ•¸((ŒŒŒI•Ù¥Í¥½¸‘É¥™Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÄÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()]¡•¸½µÁ…É¥¹œÍ½ÕÉ”É•Ù¥Í¥½¹Ìè((´¹•Ù•È…±¥¸±½…°ÁÉ¥µ…Éä­•åÌÝ¥Ñ¡½ÕÐÁÉ½½˜½˜ÍÑ…‰¥±¥Ñäì(´½µÁ…É”Í•µ…¹Ñ¥ŒÁ…Ñ¡Ì…¹•áÑ•É¹…°¥‘•¹Ñ¥™¥•ÉÌì(´É•Á½ÉÐ…‘‘¥Ñ¥½¹Ì°É•µ½Ù…±Ì°…¹¡…¹•Ù…±Õ•ÌÍ•Á…É…Ñ•±äì(´É•Ñ…¥¸‰½Ñ Í½ÕÉ”™¥¹•ÉÁÉ¥¹ÑÌì(´‘¼¹½ÐÍ¥±•¹Ñ±ä…ÉÉä„½¹™¥‘•¹”±•Ù•°™É½´½¹”É•Ù¥Í¥½¸Ñ¼…¹½Ñ¡•È¸()Q¡”M•¹…É¥½•Ù¥•Ì‘…Ñ…‰…Í•Ì‘•µ½¹ÍÑÉ…Ñ”Ñ¡¥ÌÉ•ÅÕ¥É•µ•¹ÐèÑ¡•¥È½µµ½¸Í•µ…¹Ñ¥Œ¡¥•É…É¡ä½Ù•É±…ÁÌ•Ù•¸Ñ¡½Õ ±½…°É½Ü%Ì‘¥Ù•É”¸((ŒŒŒAÉ½µ½Ñ¥½¸°‘•µ½Ñ¥½¸°…¹É•½Á•¹¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄàéÌÀÀÀÀÄÉ€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()AÉ½µ½Ñ”„±…¥´Ý¡•¸¥ÑÌ½Á•É…Ñ¥½¹…°ÕÍ”¥Ì±•…È…¹Ñ¡”É•µ…¥¹¥¹œÕ¹•ÉÑ…¥¹Ñä¹¼±½¹•È¡…¹•ÌÑ¡…ÐÕÍ”¸•µ½Ñ”½È¹…ÉÉ½Ü¥ÐÝ¡•¸¹•Ü•Ù¥‘•¹”É•Ù•…±Ì…¸•á•ÁÑ¥½¸¸I•½Á•¸„É•©•Ñ•É•±…Ñ¥½¹Í¡¥À½¹±äÝ¡•¸¹•Ü•Ù¥‘•¹”…‘‘É•ÍÍ•ÌÑ¡”É•…Í½¸¥ÐÝ…ÌÉ•©•Ñ•¸()Ù•ÉäÁÉ½µ½Ñ¥½¸Í¡½Õ±ÕÁ‘…Ñ”è((Ä¸Ñ¡”…ÁÁÉ½ÁÉ¥…Ñ”É•™•É•¹”Á…”ì(È¸Ñ¡”mI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Ét¡É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ¤ì(Ì¸Ñ¡”É•±•Ù…¹Ð•¹ÑÉä¥¸m=Á•¸EÕ•ÍÑ¥½¹Ít¡½Á•¸µÅÕ•ÍÑ¥½¹Ì¹µ¤½ÈmI•©•Ñ•I•±…Ñ¥½¹Í¡¥ÁÍt¡É•©•Ñ•µÉ•±…Ñ¥½¹Í¡¥ÁÌ¹µ¤¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÄä()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½¡åÁ½Ñ¡•Í¥ÌµÑ•ÍÑ¥¹œ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒ!åÁ½Ñ¡•Í¥ÌQ•ÍÑ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÀÅ€()ÕÍ•™Õ°É•Ù•ÉÍ”µ•¹¥¹••É¥¹œÑ•ÍÐµ…­•Ì½µÁ•Ñ¥¹œ•áÁ±…¹…Ñ¥½¹ÌÁÉ•‘¥Ð‘¥™™•É•¹Ð½‰Í•ÉÙ…Ñ¥½¹Ì¸I•Á•…Ñ¥¹œ„™…µ¥±¥…È…Í”¥¸Ý¡¥ •Ù•Éä…¹‘¥‘…Ñ”¥Ù•ÌÑ¡”Í…µ”Ù…±Õ”¥¹É•…Í•ÌÍ…µÁ±”Í¥é”‰ÕÐ‘½•Ì¹½Ð¥‘•¹Ñ¥™äÑ¡”½ÉÉ•Ðµ½‘•°¸((ŒŒŒQ•ÍÐ‘•Í¥¸Ñ•µÁ±…Ñ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•áÁ•É¥µ•¹Ñ€()½È•Ù•Éä•áÁ•É¥µ•¹Ð°É•½Éè()ð±•µ•¹ÐðI•ÅÕ¥É•µ•¹Ðð)ð€´´´ð€´´´ð)ð±…¥´ð½¹”É•±…Ñ¥½¹Í¡¥À½ÈÍ•µ…¹Ñ¥ŒÍÑ…Ñ•µ•¹Ðð)ð±Ñ•É¹…Ñ¥Ù•Ìð…Ð±•…ÍÐ½¹”É•‘¥‰±”½µÁ•Ñ¥¹œ•áÁ±…¹…Ñ¥½¸ð)ðAÉ•‘¥Ñ¥½¹Ìð•áÁ•Ñ•É•ÍÕ±Ð™½È•… …±Ñ•É¹…Ñ¥Ù”ð)ð½¹ÑÉ½±±•Ù…É¥…‰±•Ìð•Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°½¹™¥ÕÉ…Ñ¥½¸°½¹¹•Ñ¥½¸°…¹É•ÅÕ•ÍÐð)ð¡…¹•Ù…É¥…‰±”ð•á…Ñ±ä½¹”¥¹ÁÕÐÝ¡•É”Á½ÍÍ¥‰±”ð)ð=‰Í•ÉÙ…Ñ¥½¸ðÉ…Ü™É…µ•Ì°‘…Ñ…‰…Í”É½ÝÌ°U$ÍÑ…Ñ”°…¹Ñ¥µ¥¹œð)ð•¥Í¥½¸ÉÕ±”ðÉ•ÍÕ±ÐÑ¡…Ð™…Ù½ÉÌ°É•©•ÑÌ°½È¹…ÉÉ½ÝÌ•… …¹‘¥‘…Ñ”ð)ðI•ÍÑ½É…Ñ¥½¸ð¡½ÜÑ¡”‰…Í•±¥¹”¥ÌÉ•½Ù•É•…™Ñ•È„ÍÑ…Ñ”µ¡…¹¥¹œÑ•ÍÐð)ðM½Á”ðÁÉ½‘ÕÑÌ…¹É•Ù¥Í¥½¹ÌÑ¼Ý¡¥ Ñ¡”É•ÍÕ±Ð…ÁÁ±¥•Ìð()Ñ•ÍÐ¥Ì¥¹½¹±ÕÍ¥Ù”Ý¡•¸Ñ¡”…¹‘¥‘…Ñ•ÌÁÉ•‘¥ÐÑ¡”Í…µ”É•ÍÕ±Ð½È…¸Õ¹½¹ÑÉ½±±•Ù…É¥…‰±”½Õ±•áÁ±…¥¸Ñ¡”‘¥™™•É•¹”¸((ŒŒŒ%59M%=8€ÌÈ¹MeM€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÀÍ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()½µµ½¸1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸Ù…±Õ•Ì½±±…ÁÍ”Ñ¼€Å€¸UÍ”„µ…¹…•™…µ¥±äÝ¡½Í”¥‘•¹Ñ¥™¥•ÉÌ‘¥Ù•É”è()ð¥…¹½ÍÑ¥Œ™…µ¥±äðÍåÍ}µ½‘½‰©€ÁÉ•‘¥Ñ¥½¸ð…Ñ…±½Õ”¥‘}ÍåÍÑ•µ€ÁÉ•‘¥Ñ¥½¸ð™Õ¹Ñ¥½¹…°]!=€ÁÉ•‘¥Ñ¥½¸ð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ðQ¡•Éµ½É•Õ±…Ñ¥½¸€ÄÀÀÑ€ð€Í€ð€É€ð€Ñ€ð)ð¹•Éä5…¹…•µ•¹Ð€ÄÀÄá€ð€É€ð€ÈÁ€ð€Äá€ð)ð•ÍÌ½¹ÑÉ½°€ÄÀÈÍ€ð€Ý€ð€á€ð€ÈÍ€ð)ð%¹Ñ•É…Ñ¥½¸Õ¹Ñ¥½¹Ì€ÄÀÄÍ€ð€ÄÕ€ð€ÈÙ€ð€ÄÍ€ð()AÉ½•‘ÕÉ”è((Ä¸¥‘•¹Ñ¥™ä½¹”½¹™¥ÕÉ••Ù¥”…¹5½‘Õ±”¥¸Ñ¡”Í•±•Ñ•™…µ¥±äì(È¸É•Í½±Ù”¥ÑÌ=‰©•Ð…¹…±°…Ñ…±½Õ”M}=	)Q}MeMQ5€É½ÝÌì(Ì¸ÁÉ•™•È…¸=‰©•ÐÝ¥Ñ ½¹”¹½¹é•É¼ÍåÍÑ•´…ÍÍ¥¹µ•¹Ðì(Ð¸Í•¹Ñ¡”¥¹Ñ•ÉÙ¥•ÜÉ•ÅÕ•ÍÐÑ¡…ÐÁÉ½‘Õ•Ì%59M%=8€ÌÉ€ì(Ô¸ÁÉ•Í•ÉÙ”É…ÜMeM€°I€°•Ù¥”°…¹Í±½Ñ€ì(Ø¸½µÁ…É”Ñ¡”É•ÍÕ±ÐÝ¥Ñ •Ù•ÉäÁÉ•‘¥Ñ¥½¸ì(Ü¸É•Á•…ÐÝ¥Ñ …¸=‰©•Ð…ÍÍ¥¹•Ñ¼Í•Ù•É…°ÍåÍÑ•µÌÑ¼Ñ•ÍÐ½¹Ñ•áÐÍ•±•Ñ¥½¸¸()Ù…±Õ”•ÅÕ…°Ñ¼½¹”…¹‘¥‘…Ñ”…¹‘¥™™•É•¹Ð™É½´Ñ¡”½Ñ¡•ÈÑÝ¼É•©•ÑÌÑ¡”…±Ñ•É¹…Ñ¥Ù•Ì™½ÈÑ¡…Ð½‰Í•ÉÙ…Ñ¥½¸¸5Õ±Ñ¥Á±”µÍåÍÑ•´=‰©•ÑÌÉ•µ…¥¸„Í•Á…É…Ñ”…É‘¥¹…±¥ÑäÅÕ•ÍÑ¥½¸¸((ŒŒŒ¥ÉµÝ…É”µÍ•±•Ñ¥½¸ÁÉ••‘•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()Q¡”…Ñ…±½Õ”½¹Ñ…¥¹Ì½¹É•Ñ”X¹H¹‰€É½ÝÌ°•áÁ±¥¥Ð€´Å€½µÁ½¹•¹ÑÌ°µÕ±Ñ¥Á±”‰Õ¥±É½ÝÌ°µ¥ÍÍ¥¹œ‰Õ¥±É½ÝÌ°…¹]}‘•™…Õ±Ñ€µ•Ñ…‘…Ñ„¸MÑ…Ñ¥Œ‘…Ñ„•ÍÑ…‰±¥Í¡•ÌÑ¡•Í”ÍÑ…Ñ•Ì‰ÕÐ¹½Ð±½…‘•ÈÁÉ••‘•¹”¸()M•±•Ð…¸¥Ñ•´Ñ¡…Ð•áÁ½Í•Ì½µÁ•Ñ¥¹œÉ½ÝÌ…¹É•½Éè((Ä¸…±°9}%I5]I€…¹‘¥‘…Ñ•Ì™½ÈÑ¡”¥Ñ•´ì(È¸…±°…ÍÍ½¥…Ñ•9}	U%1M€É½ÝÌì(Ì¸]}‘•™…Õ±Ñ€°ÍÑ…ÑÕÌ°±½…±¥é…Ñ¥½¸±•Ù•°°Í±½ÑÌ°…¹…Á…‰¥±¥Ñä‘¥™™•É•¹•Ìì(Ð¸Ñ¡”•Ù¥”ÌÉ•Á½ÉÑ•™¥ÉµÝ…É”X¹H¹‰€ì(Ô¸Ñ¡”™¥ÉµÝ…É”½…Á…‰¥±¥Ñä5å!=5MÕ¥Ñ”…ÑÕ…±±äÁÉ•Í•¹ÑÌì(Ø¸‰•¡…Ù¥½ÈÝ¡•¸½¹±äÑ¡”‰Õ¥±‘¥™™•ÉÌì(Ü¸‰•¡…Ù¥½È™½È„½¹É•Ñ”‰Õ¥±Ù•ÉÍÕÌX¹H¸´Å€ì(à¸‰•¡…Ù¥½ÈÝ¡•¸¹¼‰Õ¥±É½Ü•á¥ÍÑÌ¸()UÍ”É•…µ½¹±ä½‰Í•ÉÙ…Ñ¥½¸™¥ÉÍÐ¸¼¹½ÐÉ•Á±…”…Ñ…±½Õ”É½ÝÌÑ¼™½É”„Í•±•Ñ¥½¸¸ÕÍ•™Õ°É•ÍÕ±ÐµÕÍÐ‘¥ÍÑ¥¹Õ¥Í •á…Ðµ…Ñ °½µÁ½¹•¹ÐÝ¥±‘…É°‘•™…Õ±Ð™…±±‰…¬°±½…±¥é…Ñ¥½¸¡½¥”°…¹…‰Í•¹”½˜‰Õ¥±µ•Ñ…‘…Ñ„¸((ŒŒŒ!…É‘Ý…É”…¹µ¥É½½¹ÑÉ½±±•ÈÙ•ÉÍ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°É•Ù¥Í¥½¹€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°Í½ÕÉ•€()%59M%=8€Í€…¹€Ù€ÕÍ”Y•ÉÍ¥½¸©I•±•…Í”©	Õ¥±‘€°‰ÕÐÑ¡”…¹½¹¥…°‘…Ñ…‰…Í•Ì½¹Ñ…¥¸¹¼‘¥É•ÐÑ…É•Ð™¥•±‘Ì¸()Q¼‘•Ñ•Éµ¥¹”Ý¡•Ñ¡•ÈÑ¡•ä±…ÍÍ¥™äÁÉ½‘ÕÐÉ•Ù¥Í¥½¹Ìè((Ä¸½±±•ÐÍ•Ù•É…°Á¡åÍ¥…°•á…µÁ±•Ì½˜Ñ¡”Í…µ”M-T…¹™¥ÉµÝ…É”ì(È¸É•½Éµ…¹Õ™…ÑÕÉ¥¹œ‘…Ñ”½É•Ù¥Í¥½¸µ…É­¥¹ÌÝ¡•É”…Ù…¥±…‰±”ì(Ì¸…ÁÑÕÉ”™¥ÉµÝ…É”°¡…É‘Ý…É”°…¹µ¥É½½¹ÑÉ½±±•ÈÑÕÁ±•Ìì(Ð¸½µÁ…É”5½‘Õ±”±…å½ÕÐ…¹ÍÕÁÁ½ÉÑ•½¹™¥ÕÉ…Ñ¥½¸ì(Ô¸É•Á•…Ð…É½ÍÌ„­¹½Ý¸¡…É‘Ý…É”É•Ù¥Í¥½¸½ÈÉ•Á±…•µ•¹ÐÁÉ½‘ÕÐì(Ø¸½‰Í•ÉÙ”Ý¡•Ñ¡•È5å!=5MÕ¥Ñ”¡…¹•ÌÑ¡”Í•±•Ñ•…Ñ…±½Õ”•Ù¥”½È…Á…‰¥±¥Ñä¸()ÍÑ…‰±”½ÉÉ•±…Ñ¥½¸Ý¥Ñ „ÁÉ¥¹Ñ•É•Ù¥Í¥½¸¥ÌÕÍ•™Õ°•µÁ¥É¥…°µ•Ñ…‘…Ñ„ì¥Ð‘½•Ì¹½ÐÉ•…Ñ”„‘…Ñ…‰…Í”É•±…Ñ¥½¹Í¡¥ÀÕ¹±•ÍÌ„Í½ÕÉ”™¥•±¥Ì™½Õ¹¸((ŒŒŒ9}=9€…Ñ…±½Õ”µÝ¥‘”•ÅÕ¥Ù…±•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€°¹½Ð…ÁÁ±¥…‰±•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäè¡åÁ½Ñ¡•Í¥Í€°¹½Ð•ÍÑ…‰±¥Í¡•‘€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°•Ù¥‘•¹•€()½ÈÑ¡”½É‘¥¹…Éä…‘‘É•ÍÍ••Ù¥”™½É´°9}=9€¥Ì½ÉÉ½‰½É…Ñ•…ÌÑ¡”¹Õµ‰•È½˜Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹Ì¸Q¡”É•µ…¥¹¥¹œ¡åÁ½Ñ¡•Í¥Ì¥ÌÑ¡…Ð°Ý¥Ñ¡¥¸Ñ¡…Ð…‘‘É•ÍÍ•µ™½É´Í½Á”°¥Ð…±Ý…åÌ•ÅÕ…±ÌÑ¡”½Õ¹Ð½˜…ÁÁ±¥…‰±”™¥ÉµÝ…É”µÍ½Á•Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸™¥•±‘Ì…™Ñ•È•á±Õ‘¥¹œ%€¸()½È•… Ñ•ÍÐ•Ù¥”è((Ä¸½‰Ñ…¥¸„ÁÉ½‘ÕÐ‘¥…É…´Í¡½Ý¥¹œ…±°Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹Ìì(È¸…ÁÑÕÉ”%59M%=8€Ä¹9}=9€ì(Ì¸É•Í½±Ù”¥Ñ•´…¹•á…Ð™¥ÉµÝ…É”ì(Ð¸¥‘•¹Ñ¥™ä™¥ÉµÝ…É”µÍ½Á•Á¡åÍ¥…°‘•™¥¹¥Ñ¥½¹Ì°½¹™¥ÕÉ…Ñ¥½¸µ½‘•Ì°…¹½¹‘¥Ñ¥½¹Ìì(Ô¸•á±Õ‘”%€½¹±äÝ¡•¸¥Ð¥ÌÑ¡”½µµ½¸¥‘•¹Ñ¥™¥•ÈÉ…Ñ¡•ÈÑ¡…¸„Á¡åÍ¥…°Á½Í¥Ñ¥½¸ì(Ø¸½µÁ…É”‘¥…É…´°™É…µ”°…¹…ÁÁ±¥…‰±”µ™¥•±½Õ¹Ðì(Ü¸É•½É½¹‘¥Ñ¥½¹…°½È‘ÕÁ±¥…Ñ•™¥•±‘Ì¥¹ÍÑ•…½˜½Õ¹Ñ¥¹œ‰±¥¹‘±ä¸()AÉ¥½É¥Ñ¥é”•Ù¥•ÌÝ¥Ñ ½Õ¹ÑÌ½Ñ¡•ÈÑ¡…¸Í¥à…¹™¥ÉµÝ…É”Í¡…É•‰äÍ•Ù•É…°M-UÌ¸-¹½Ý¸½ÉÉ½‰½É…Ñ¥¹œ•á…µÁ±•Ì¥¹±Õ‘”ÐÈÁ€°ÐÈå€°…¹ ÐØÔÈ¼Í€¸()QÉ•…ÐÑ¡”•µÁÑäµ]!I€…Ñ•Ý…ä™½É´…Ì„Í•Á…É…Ñ”¡åÁ½Ñ¡•Í¥Ì¸=‰Í•ÉÙ•5 ÈÀÈ…¹ÐÔÐ…Ñ•Ý…ä¥‘•¹Ñ¥ÑäÉ•ÍÁ½¹Í•Ì‰½Ñ …ÉÉä9}=9€ô€ÄÕ€°½ÕÑÍ¥‘”Ñ¡”½É‘¥¹…Éä€À¸¸ÄÉ€É…¹”¸	•…ÕÍ”€ÄÔ€ô€Áá€°„É•Í•ÉÙ•½ÈÍ•¹Ñ¥¹•°¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¥ÌÁ±…ÕÍ¥‰±”°‰ÕÐ¥Ð¥Ì¹½Ð•ÍÑ…‰±¥Í¡•¸Q¼Ñ•ÍÐ¥Ð°½±±•ÐÑ¡”Í…µ”™¥•±…É½ÍÌ…Ñ•Ý…äµ½‘•±Ì…¹™¥ÉµÝ…É”É•Ù¥Í¥½¹Ì…¹Í••¬…¸…ÁÁ±¥…‰±”¥µÁ±•µ•¹Ñ…Ñ¥½¸‘•½‘•È½È…ÕÑ¡½É¥Ñ…Ñ¥Ù”‘•™¥¹¥Ñ¥½¸¸I•½É…¹äÙ…±Õ”½Ñ¡•ÈÑ¡…¸€ÄÕ€°…¹‘¼¹½Ð¥¹™•ÈƒŠqé•É¼½¹™¥ÕÉ…Ñ½ÉÏŠt½ÈƒŠq¹½Ð…ÁÁ±¥…‰±—ŠtÝ¥Ñ¡½ÕÐ•Ù¥‘•¹”Ñ¡…Ð‘¥ÍÑ¥¹Õ¥Í¡•ÌÑ¡½Í”µ•…¹¥¹Ì¸((ŒŒŒ%59M%=8€Ñ€…¹€Õ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÀÝ€()U¹•ÉÑ…¥¹Ñäè¡åÁ½Ñ¡•Í¥Í€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€()Q¡”Ý½É­¥¹œ¡åÁ½Ñ¡•Í¥Ì¥ÌÑ¡…ÐÑ¡”ÑÝ¼É½ÕÁÌ½˜Í¥àÙ…±Õ•Ì•¹½‘”Á¡åÍ¥…°µ½¹™¥ÕÉ…Ñ½ÈÍÑ…Ñ”°Á½ÍÍ¥‰±äµ…ÁÁ¥¹œÁ½Í¥Ñ¥½¹Ì€Ä¸¸Ù€…¹€Ü¸¸ÄÉ€¸()UÍ”„•Ù¥”Ý¥Ñ ‘½Õµ•¹Ñ•Á½Í¥Ñ¥½¹Ì…¹É•µ½Ù…‰±”½¹™¥ÕÉ…Ñ½ÉÌè((Ä¸É•½É„½µÁ±•Ñ”‰…Í•±¥¹”Ý¥Ñ …±°Á½Í¥Ñ¥½¹Ì•µÁÑä¥˜Ñ¡”•Ù¥”Á•Éµ¥ÑÌ¥Ðì(È¸…ÁÑÕÉ”‰½Ñ ‘¥µ•¹Í¥½¹Ì…Ð±•…ÍÐÑÝ¥”Ñ¼•ÍÑ…‰±¥Í ÍÑ…‰¥±¥Ñäì(Ì¸¥¹Í•ÉÐ½¹”­¹½Ý¸½¹™¥ÕÉ…Ñ½È¥¹Ñ¼Á½Í¥Ñ¥½¸€Å€…¹É•Á•…Ðì(Ð¸µ½Ù”Ñ¡”Í…µ”½¹™¥ÕÉ…Ñ½ÈÑ¼Í•Ù•É…°Á½Í¥Ñ¥½¹Ì°¥¹±Õ‘¥¹œ½¹”…‰½Ù”€Ù€Ý¡•¸…Ù…¥±…‰±”ì(Ô¸­••ÀÑ¡”Á½Í¥Ñ¥½¸™¥á•…¹¡…¹”½¹±äÑ¡”½¹™¥ÕÉ…Ñ½ÈÙ…±Õ”ì(Ø¸½µÁ…É”Á¡åÍ¥…°…¹Y¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸ÁÉ½‘Õ¥¹œÑ¡”Í…µ”•™™•Ñ¥Ù”ÁÉ½Á•ÉÑäì(Ü¸É•½ÉÝ¡•Ñ¡•ÈÕ¹¡…¹•Á½Í¥Ñ¥½¹ÌÉ•µ…¥¸½¹ÍÑ…¹Ð¸()Q¡¥Ìµ…ÑÉ¥à‘¥ÍÑ¥¹Õ¥Í¡•ÌÁ½Í¥Ñ¥½¸°ÁÉ•Í•¹”°É…Ü½¹™¥ÕÉ…Ñ½È½‘”°•™™•Ñ¥Ù”Ù…±Õ”°…¹½¹™¥ÕÉ…Ñ¥½¸µµ½‘”•™™•ÑÌ¸i•É¼½¹½¹é•É¼‘…Ñ„™É½´½¹”½¹™¥ÕÉ…Ñ¥½¸…¹¹½Ð•ÍÑ…‰±¥Í „ÁÉ•Í•¹”‰¥Ñµ…À¸((ŒŒŒ¥…¹½ÍÑ¥Œ½ÕÑ•È]!I€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÀá€()I•Á•…Ñ•]!<€ÄÀÀÅ€½‰Í•ÉÙ…Ñ¥½¹ÌÍÕ•ÍÐÑ¡…ÐÑ¡”½ÕÑ•È‘¥…¹½ÍÑ¥Œ]!I€½™Ñ•¸™½±±½ÝÌÑ¡”½¹™¥ÕÉ•…‘‘É•ÍÌ½˜Í±½Ñ€€Å€¸Q•ÍÐÑ¡”‰½Õ¹‘…Éä…Í•Ìè((´Í±½Ð€Å€•¹…‰±•…¹…‘‘É•ÍÍ•ì(´Í±½Ð€Å€‘¥Í…‰±•…¹É•ÁÉ•Í•¹Ñ•‰ä¥ÑÌY¥É¥¸=‰©•Ð¥¸%59M%=8€ÌÁ€ì(´Í±½Ð€Å€…ÍÍ¥¹•„½µµ…¹µ½¹±ä=‰©•Ðì(´…¹½Ñ¡•ÈÍ±½Ð…ÉÉå¥¹œÑ¡”µ…¥¸Á¡åÍ¥…°…‘‘É•ÍÌì(´Í•Ù•É…°5½‘Õ±•ÌÍ¡…É¥¹œ…¸…‘‘É•ÍÌì(´¹½¸µ1¥¡Ñ¥¹œ‘¥…¹½ÍÑ¥Œ™…µ¥±¥•Ì¸()½È•… …Í”°½µÁ…É”‘¥Í½Ù•Éä…‘‘É•ÍÌ°¥¹Ñ•ÉÙ¥•ÜÍ•±•Ñ½È°½ÕÑ•ÈÉ•ÍÁ½¹Í”]!I€°…¹•Ù•Éä%59M%=8€ÌÉ€5½‘Õ±”…‘‘É•ÍÌ¸Q¡”½…°¥ÌÑ¼É•½Ù•È„Í•±•Ñ¥½¸ÉÕ±”°¹½Ðµ•É•±ä…¹½Ñ¡•Èµ…Ñ¡¥¹œ•á…µÁ±”¸((ŒŒŒA¡åÍ¥…°µÑ¼µ…‘Ù…¹•ÁÉ½Á•ÉÑäµ…ÁÁ¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€()½È„…¹‘¥‘…Ñ”Á¡åÍ¥…°™¥•±…¹%59M%=8€ÌÉ€½È€ÌÕ€ÁÉ½Á•ÉÑäè((Ä¸É•Í½±Ù”Ñ¡”•á…Ð™¥ÉµÝ…É”°Í±½Ñ€°…¹=‰©•Ðì(È¸½µÁ…É”=9}Me5	=1}I€°Í•µ…¹Ñ¥ŒÑåÁ”°…¹Ù…±Õ”‘½µ…¥¸ì(Ì¸¥¹ÍÁ•Ð™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¹Ì°½¹Ù•ÉÍ¥½¸ÉÕ±•Ì°…¹9}A!e}Q=}Y}QI9M€ì(Ð¸¡…¹”½¹±äÑ¡”Á¡åÍ¥…°™¥•±…¹É•…‰…¬Ñ¡”•™™•Ñ¥Ù”½¹™¥ÕÉ…Ñ¥½¸ì(Ô¸É•ÍÑ½É”Ñ¡”‰…Í•±¥¹”ì(Ø¸ÁÉ½É…´Ñ¡”ÁÉ½Á½Í•Y¥ÉÑÕ…°½Õ¹Ñ•ÉÁ…ÉÐ…¹É•…‰…¬……¥¸ì(Ü¸±…ÍÍ¥™äÑ¡”É•ÍÕ±Ð…Ì‘¥É•Ð°½¹Ù•ÉÑ•°É…¹”µ±¥µ¥Ñ•°½¹‘¥Ñ¥½¸µ‘•Á•¹‘•¹Ð°½ÈÕ¹É•±…Ñ•¸()¸¥‘•¹Ñ¥…°•™™•Ñ¥Ù”Ù…±Õ”‘½•Ì¹½ÐÁÉ½Ù”¥‘•¹Ñ¥…°ÍÑ½É…”½È½¹™¥ÕÉ…Ñ¥½¸µ•Ñ¡½¸Á¡åÍ¥…°½Õ¹Ñ•ÉÁ…ÉÐ¥¹‘¥…Ñ•Ì…Á…‰¥±¥Ñä°¹½ÐÝ¡¥ µ•Ñ¡½¥Ì…Ñ¥Ù”¸((ŒŒŒ‘‘É•ÍÌµÉÕ±”Í•±•Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÄÁ€()AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()¡½½Í”„ÍåÍÑ•´Ý¥Ñ ‰½Ñ ™…µ¥±äµÕ¹ÅÕ…±¥™¥•…¹™…µ¥±äµÅÕ…±¥™¥•9}IMM}IU1€É½ÝÌ¸((Ä¸É•Í½±Ù”Ñ¡”=‰©•ÐÌ¥‘}™…µ¥±å€…¹…Ñ…±½Õ”ÍåÍÑ•µÌì(È¸É•½É•Ù•Éä…¹‘¥‘…Ñ”ÉÕ±”…¹¥ÑÌY¥ÉÑÕ…°½…‘Ù…¹•Ñ•µÁ±…Ñ”ì(Ì¸Ù…Éä½¹±äÑ¡”=‰©•Ð™…µ¥±ä½Èµ½‘”Ý¡•É”Á½ÍÍ¥‰±”ì(Ð¸½‰Í•ÉÙ”Ñ¡”…‘‘É•ÍÌ™½É´5å!=5MÕ¥Ñ”…•ÁÑÌ…¹•µ¥ÑÌì(Ô¸ÑÉ…”Ý¡•Ñ¡•ÈÙ…±¥‘¥Ñå}ÉÕ±•€°±•Ù•°™±…Ì°½È½™™Í•Ñ}…‘Ù€…É”É•…ì(Ø¸Ñ•ÍÐ„É•©•Ñ•…‘‘É•ÍÌÑ¡…Ð‘¥™™•ÉÌ…Ð½¹±ä½¹”ÉÕ±”‰½Õ¹‘…Éä¸()Q¡¥Ì…¸‘¥ÍÑ¥¹Õ¥Í ÉÕ±”Í•±•Ñ¥½¸™É½´ÉÕ±”É•¹‘•É¥¹œ…¹…ÁÁ±¥…Ñ¥½¸µÍ¥‘”ÁÉ•Ù…±¥‘…Ñ¥½¸™É½´•Ù¥”É•©•Ñ¥½¸¸((ŒŒŒM•¹…É¥¼Á•ÉÍ¥ÍÑ•¹”…¹µ…Ñ¡¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÄÅ€()Q¼™¥¹Ñ¡”µ¥ÍÍ¥¹œÍ•¹…É¥¼µ¥¹ÍÑ…¹”±…å•Èè((Ä¸™¥¹•ÉÁÉ¥¹Ð…¹‘¥‘…Ñ”ÁÉ½©•Ð…¹‘…Ñ„™¥±•Ìì(È¸ÑÉ…”™¥±”½Á•¹Ì‰•™½É”É•…Ñ¥¹œ„Í•¹…É¥¼ì(Ì¸É•…Ñ”½¹”µ¥¹¥µ…°ÑÉ¥•Èµ…Ñ¥½¸Í•¹…É¥¼ì(Ð¸Í…Ù”°±½Í”°…¹É•½Á•¸Ñ¡”…ÁÁ±¥…Ñ¥½¸ì(Ô¸‘¥™˜™¥±•Ì°ME1¥Ñ”Í¡•µ…Ì°…¹É•½É‘Ìì(Ø¸¡…¹”½¹”ÑÉ¥•È°½¹‘¥Ñ¥½¸°…Ñ¥½¸°½È½É‘•É¥¹œ•‘”¥¹‘•Á•¹‘•¹Ñ±äì(Ü¸½ÉÉ•±…Ñ”¡…¹•ÌÝ¥Ñ M•¹…É¥½•Ù¥•ÌÉ•Í½ÕÉ”­•åÌ…¹µ…Ñ¡¥¹œ%Ìì(à¸ÑÉ…”•á•ÕÑ¥½¸Í•Á…É…Ñ•±ä™É½´Á•ÉÍ¥ÍÑ•¹”¸()Q¡”M•¹…É¥½•Ù¥•Ì…Á…‰¥±¥Ñä‘…Ñ…‰…Í•ÌÍ¡½Õ±É•µ…¥¸Õ¹¡…¹•¸¡…¹•…Á…‰¥±¥Ñä™¥±”Ý½Õ±¥¹‘¥…Ñ”Íå¹¡É½¹¥é…Ñ¥½¸½Èµ¥É…Ñ¥½¸‰•¡…Ù¥½È…¹µÕÍÐ‰”¥¹Ù•ÍÑ¥…Ñ•Í•Á…É…Ñ•±ä¸((ŒŒŒMÑ½À½¹‘¥Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÄäéÌÀÀÀÀÄÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€()MÑ½À…¹±…ÍÍ¥™äÑ¡”É•ÍÕ±Ð…Ì¥¹½¹±ÕÍ¥Ù”Ý¡•¸è((´Ñ¡”•Ù¥”½È™¥ÉµÝ…É”…¹¹½Ð‰”É•Í½±Ù•Õ¹¥ÅÕ•±ä•¹½Õ ™½ÈÑ¡”±…¥´ì(´µÕ±Ñ¥Á±”Í•ÑÑ¥¹Ì¡…¹•ì(´É•ÅÕ•ÍÐ½É•ÍÁ½¹Í”‘¥É•Ñ¥½¸¥ÌÕ¹­¹½Ý¸ì(´…¹‘¥‘…Ñ•ÌÁÉ•‘¥ÐÑ¡”Í…µ”½ÕÑ½µ”ì(´Ñ¡”½Á•É…Ñ¥½¸Ñ¥µ•½ÕÐÝ¥Ñ¡½ÕÐÁÉ½½˜Ñ¡…ÐÑ¡”•Ù¥”½Õ±É•ÍÁ½¹ì(´„ÍÑ…Ñ”µ¡…¹¥¹œÑ•ÍÐ…¹¹½Ð‰”É•ÍÑ½É•Í…™•±ä¸()¸¥¹½¹±ÕÍ¥Ù”Ñ•ÍÐÍ¡½Õ±ÍÑ¥±°É•½ÉÝ¡…ÐÝ…ÌÑÉ¥•…¹¡½ÜÑ¡”¹•áÐÑ•ÍÐ…¸‰•½µ”‘¥ÍÉ¥µ¥¹…Ñ¥¹œ¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÈÀ()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½µ•Ñ¡½‘½±½ä¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒ5•Ñ¡½‘½±½ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()I•Ù•ÉÍ”•¹¥¹••É¥¹œÍ¡½Õ±É•½Ù•ÈÑ¡”¹…ÉÉ½Ý•ÍÐ•áÁ±…¹…Ñ¥½¸ÍÕÁÁ½ÉÑ•‰äÑ¡”•Ù¥‘•¹”…¹µ…­”Ñ¡…Ð•áÁ±…¹…Ñ¥½¸É•ÁÉ½‘Õ¥‰±”‰ä…¹½Ñ¡•È¥¹Ù•ÍÑ¥…Ñ½È¸Á±…ÕÍ¥‰±”±…‰•°¥Ì¹½Ð„É•ÍÕ±ÐÕ¹Ñ¥°¥ÑÌ¹…µ•ÍÁ…”°Í½Á”°½¹‘¥Ñ¥½¹Ì°…¹½Õ¹Ñ•É•á…µÁ±•Ì¡…Ù”‰••¸Ñ•ÍÑ•¸((ŒŒŒ•™¥¹”Ñ¡”ÅÕ•ÍÑ¥½¸ÁÉ•¥Í•±ä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè…Ù½¥‘€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()	•¥¸Ý¥Ñ ½¹”™…±Í¥™¥…‰±”ÅÕ•ÍÑ¥½¸¸á…µÁ±•Ì¥¹±Õ‘”è((´½•Ì%59M%=8€ÌÀ¹-e=€¡…¹”¹…µ•ÍÁ…”Ý¥Ñ MQQ€ü(´½•Ì9}IMM}IU1¹½‰©•Ñ}‘•Ù¥•}™…µ¥±å€É•™•ÈÑ¼9}=	)Q}%Q5}5%1d¹¥‘}™…µ¥±å€ü(´½•Ì…¸•áÁ±¥¥Ð™¥ÉµÝ…É”½µÁ½¹•¹Ð½˜€´Å€‰•¡…Ù”…Ì…¸…¹ä½Õ¹ÍÁ•¥™¥•Í•¹Ñ¥¹•°ü(´]¡¥ ÍÑ½É•™¥•±¥ÌÑ¡”‰•ÍÐ…¹‘¥‘…Ñ”™½È%59M%=8€ÌÈ¹MeM€ü()Ù½¥ÅÕ•ÍÑ¥½¹ÌÍÕ …ÌƒŠq]¡…Ð‘½•ÌÑ¡¥ÌÑ…‰±”µ•…¸ÿŠt	É•…¬Ñ¡•´¥¹Ñ¼±…¥µÌÑ¡…Ð…¸‰”¡•­•¥¹‘•Á•¹‘•¹Ñ±ä¸()½È•… ±…¥´°ÝÉ¥Ñ”‘½Ý¸è((Ä¸Ñ¡”ÁÉ½Á½Í•Í½ÕÉ”…¹Ñ…É•Ð¹…µ•ÍÁ…•Ìì(È¸Ñ¡”•áÁ•Ñ•…É‘¥¹…±¥Ñä…¹½¹‘¥Ñ¥½¹Ìì(Ì¸…Ð±•…ÍÐ½¹”Ù¥…‰±”…±Ñ•É¹…Ñ¥Ù”ì(Ð¸Ñ¡”½‰Í•ÉÙ…Ñ¥½¸Ñ¡…ÐÝ½Õ±‘¥ÍÑ¥¹Õ¥Í Ñ¡”…±Ñ•É¹…Ñ¥Ù•Ìì(Ô¸Ñ¡”Í½Á”¥¸Ý¡¥ Ñ¡”±…¥´¥Ì•áÁ•Ñ•Ñ¼¡½±¸((ŒŒŒ¥àÑ¡”•Ù¥‘•¹”É•Ù¥Í¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€°Ù•ÉÍ¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°Í½ÕÉ•€()I•½ÉÑ¡”ÁÉ½‘ÕÐÙ•ÉÍ¥½¸°½É¥¥¹…°Á…Ñ °‰åÑ”Í¥é”°…¹M!´ÈÔØ‰•™½É”…¹…±åÍ¥Ì¸Q¡”…¹½¹¥…°5å!=5MÕ¥Ñ”€Ì¸Ô¸ÌàÍ½ÕÉ”Í•Ð¥ÌÉ•¥ÍÑ•É•¥¸mÍ½ÕÉ•Ì½µ…¹¥™•ÍÐ¹å…µ±t ¸¸½Í½ÕÉ•Ì½µ…¹¥™•ÍÐ¹å…µ°¤¸()QÉ•…Ð•Ù•ÉäÅÕ…¹Ñ¥Ñ…Ñ¥Ù”ÍÑ…Ñ•µ•¹Ð…ÌÉ•Ù¥Í¥½¸µÍ½Á•¸ƒŠq±°€àÈÜÉ½ÝÌÉ•Í½±Ù—Štµ•…¹Ì…±°É½ÝÌ¥¸Ñ¡”™¥¹•ÉÁÉ¥¹Ñ•€Ì¸Ô¸Ìà‘…Ñ…‰…Í”°¹½Ð•Ù•Éä5å!=5É•±•…Í”¸()¼¹½Ðµ½‘¥™ä…¹½¹¥…°‘…Ñ…‰…Í•ÌÑ¼…‘¥¹™•ÉÉ•™½É•¥¸­•åÌ°¹½Éµ…±¥é”Ñ•áÐ°É•Á…¥ÈÉ½ÝÌ°½È•¹½‘”½¹±ÕÍ¥½¹Ì¸•É¥Ù•‘…Ñ…‰…Í•Ì°ÅÕ•Éä½ÕÑÁÕÐ°‘¥…É…µÌ°…¹É•Á½ÉÑÌ‰•±½¹œ½ÕÑÍ¥‘”mÍ½ÕÉ•Ì½t ¸¸½Í½ÕÉ•Ì¼¤¸()]¡•¸…¸•áÑ•É¹…°µ…¹Õ…°½ÈÁÉ½‘ÕÐÍ¡••Ð¥ÌÕÍ•°ÁÉ•Í•ÉÙ”¥ÑÌÑ¥Ñ±”°ÁÉ½‘ÕÐ½‘”°É•Ù¥Í¥½¸½‘…Ñ”°±…¹Õ…”°…¹Á…”½È‘¥…É…´¥‘•¹Ñ¥™¥•È¸±…Ñ•Èµ…¹Õ…°µ…ä‘•ÍÉ¥‰”‘¥™™•É•¹Ð¡…É‘Ý…É”¸((ŒŒŒAÉ•Í•ÉÙ”Ñ¡”É…Ü½‰Í•ÉÙ…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()%¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸µÕÍÐÉ•µ…¥¸ÑÉ…•…‰±”Ñ¼Õ¹¡…¹••Ù¥‘•¹”¸()½È‘…Ñ…‰…Í”Ý½É¬°É•Ñ…¥¸è((´‘…Ñ…‰…Í”…¹Ñ…‰±”¹…µ”ì(´Í¡•µ„…¹‘•±…É•½¹ÍÑÉ…¥¹ÑÌì(´É½Ü­•äÝ¡•É”µ•…¹¥¹™Õ°ì(´É…ÜÙ…±Õ•Ì°¥¹±Õ‘¥¹œ9U11€°•µÁÑäÑ•áÐ°€Á€°…¹¹•…Ñ¥Ù”Ù…±Õ•Ìì(´Ñ¡”•á…ÐÅÕ•ÉäÕÍ•Ñ¼ÁÉ½‘Õ”„½Õ¹Ð½È•á•ÁÑ¥½¸±¥ÍÐ¸()½ÈÁÉ½Ñ½½°Ý½É¬°É•Ñ…¥¸è((´•á…Ð™É…µ”‰åÑ•Ì½ÈÑ•áÐì(´Ñ¥µ•ÍÑ…µÀ°‘¥É•Ñ¥½¸°ÑÉ…¹ÍÁ½ÉÐ½¹¹•Ñ¥½¸°…¹Í•ÍÍ¥½¸ì(´…Ñ¥Ù”‘¥…¹½ÍÑ¥Œ°ÁÉ½É…µµ¥¹œ°½È™Õ¹Ñ¥½¹…°½Á•É…Ñ¥½¸ì(´•Ù¥”Í•±•Ñ½È…¹ÁÉ••‘¥¹œÉ•ÅÕ•ÍÐì(´™½±±½Ý¥¹œÉ•ÍÁ½¹Í”°Ñ•Éµ¥¹…°µ…É­•È°•ÉÉ½È°½ÈÑ¥µ•½ÕÐ¸()½ÈU$•Ù¥‘•¹”°É•½ÉÑ¡”•á…Ð±…‰•°°Ù…±Õ”°Ù¥Í¥‰¥±¥Ñä°•‘¥Ñ…‰¥±¥Ñä°Í•±•Ñ••Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°…¹½¹™¥ÕÉ…Ñ¥½¸µ½‘”¸½ÈÁÉ½‘ÕÐ•Ù¥‘•¹”°‘¥ÍÑ¥¹Õ¥Í …¸…ÑÕ…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¸™É½´„ÁÉ¥¹Ñ•±…‰•°°Ñ•Éµ¥¹…°°‰ÕÑÑ½¸°½È¥¹‘¥…Ñ½È¸()9•Ù•ÈÉ•Á±…”Ñ¡”É…ÜÙ…±Õ”Ý¥Ñ ¥ÑÌ¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¸MÑ½É”‰½Ñ ¸((ŒŒŒ¹Õµ•É…Ñ”¹…µ•ÍÁ…•Ì‰•™½É”©½¥¹¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°É•Ù¥Í¥½¹€)U¹•ÉÑ…¥¹Ñäèµ¥¡Ñ€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()Q¡”Í…µ”¥¹Ñ••È…¸±•¥Ñ¥µ…Ñ•±ä½ÕÈ¥¸Õ¹É•±…Ñ•¹…µ•ÍÁ…•Ì¸Ù…±Õ”‘•ÍÉ¥‰•¥¹™½Éµ…±±ä…Ì…¸=‰©•Ðµ¥¡Ðµ•…¸è((´9}-e}=	)P¹¥‘}­•å}½‰©•Ñ€°…¸¥¹Ñ•É¹…°É½Ü­•äì(´9}-e}=	)P¹­•å}½‰©•Ñ€°…¸•áÑ•É¹…°=‰©•Ð¹Õµ‰•Èì(´9}Y%I%9}=	)P¹¥‘}Ù¥É¥¹}­•å}½‰©•Ñ€°…¸¥¹Ñ•É¹…°É½Ü­•äì(´9}Y%I%9}=	)P¹Ù¥É¥¹}­•å}½‰©•Ñ€°…¸•áÑ•É¹…°Y¥É¥¸=‰©•Ð¹Õµ‰•Èì(´M•¹…É¥½•Ù¥•Ì=‰©•Ñ%‘€°±½…°Ñ¼Ñ¡”Í•¹…É¥¼•¹¥¹”ì(´„Í±½Ñ€…ÉÉ¥•‰ä„‘¥…¹½ÍÑ¥Œ™É…µ”ì(´…¸=Á•¹]•‰9•Ð]!Q€°]!I€°½È%59M%=9€Ù…±Õ”¸()	Õ¥±„¹…µ•ÍÁ…”±•‘•È‰•™½É”Ñ•ÍÑ¥¹œ•ÅÕ…±¥Ñäè()ðAÉ½Á•ÉÑäðI•½Éð)ð€´´´ð€´´´ð)ð=É¥¥¸ð™É…µ”™¥•±°Ñ…‰±”½±Õµ¸°U$™¥•±°½È‘½Õµ•¹Ð±…‰•°ð)ðI•ÁÉ•Í•¹Ñ…Ñ¥½¸ð¥¹Ñ••È°Ñ•áÐ°½µÁ½Í¥Ñ”…‘‘É•ÍÌ°‰¥Ð™¥•±°Í•¹Ñ¥¹•°ð)ðI…¹”ð‘•±…É•…¹½‰Í•ÉÙ•ð)ðM½Á”ð±½‰…°°‘…Ñ…‰…Í”µ±½…°°•Ù¥”µ±½…°°™¥ÉµÝ…É”µ±½…°°Í•ÍÍ¥½¸µ±½…°ð)ðMÑ…‰¥±¥ÑäðÁ•ÉÍ¥ÍÑ•¹Ð¥‘•¹Ñ¥Ñä°É•Ù¥Í¥½¸µ±½…°É½Ü­•ä°ÉÕ¹Ñ¥µ”Ù…±Õ”ð)ð…¹‘¥‘…Ñ”µ•…¹¥¹Ìð•Ù•ÉäÁ±…ÕÍ¥‰±”¹…µ•ÍÁ…”°¹½Ð½¹±äÑ¡”ÁÉ•™•ÉÉ•½¹”ð()9Õµ•É¥Œ•ÅÕ…±¥Ñä¥ÌÕÍ•™Õ°™½È•¹•É…Ñ¥¹œ…¹‘¥‘…Ñ•Ì¸%Ð¥Ì¹½ÐÉ•±…Ñ¥½¹…°•Ù¥‘•¹”‰ä¥ÑÍ•±˜¸((ŒŒŒQ•ÍÐÍÑÉÕÑÕÉ…°½µÁ…Ñ¥‰¥±¥Ñä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()½È„ÁÉ½Á½Í•‘…Ñ…‰…Í”É•±…Ñ¥½¹Í¡¥À°Ñ•ÍÐ…±°Á½ÁÕ±…Ñ•¹½¸µÍ•¹Ñ¥¹•°Ù…±Õ•Ì°¹½Ð„Í…µÁ±”¸()ÍÅ°)M1P¡¥±¹Á…É•¹Ñ}¥°=U9P ¨¤L½ÕÉÉ•¹•Ì)I=4¡¥±)1P)=%8Á…É•¹Ð=8Á…É•¹Ð¹¥€ô¡¥±¹Á…É•¹Ñ}¥)]!I¡¥±¹Á…É•¹Ñ}¥%L9=P9U10(€9¡¥±¹Á…É•¹Ñ}¥€ðø€À(€9Á…É•¹Ð¹¥%L9U10)I=U@	d¡¥±¹Á…É•¹Ñ}¥ì)€()Q¡•¸Ñ•ÍÐ…É‘¥¹…±¥Ñä…¹…µ‰¥Õ¥Ñäè()ÍÅ°)M1P¡¥±¹Á…É•¹Ñ}¥°=U9P ¨¤L¡¥±‘}É½ÝÌ)I=4¡¥±)]!I¡¥±¹Á…É•¹Ñ}¥%L9=P9U10)I=U@	d¡¥±¹Á…É•¹Ñ}¥)=IH	d¡¥±‘}É½ÝÌMì)€()Q¡”…Õ‘¥ÐµÕÍÐ…¹ÍÝ•Èè((Ä¸É”ÑåÁ•Ì…¹½‰Í•ÉÙ•‘½µ…¥¹Ì½µÁ…Ñ¥‰±”ü(È¸½•Ì•Ù•Éä¹½¸µÍ•¹Ñ¥¹•°¡¥±É•Í½±Ù”ü(Ì¸É”‘ÕÁ±¥…Ñ•Ì½µÁ…Ñ¥‰±”Ý¥Ñ Ñ¡”ÁÉ½Á½Í•…É‘¥¹…±¥Ñäü(Ð¸¼€Á€°9U11€°•µÁÑäÍÑÉ¥¹Ì°½È¹•…Ñ¥Ù”Ù…±Õ•Ì…Ð…Ì‘…Ñ„½ÈÍ•¹Ñ¥¹•±Ìü(Ô¸½•ÌÑ¡”É•±…Ñ¥½¹Í¡¥ÀÍÕÉÙ¥Ù”Í•±•Ñ¥½¸½˜Ñ¡”½ÉÉ•Ð™¥ÉµÝ…É”°5½‘Õ±”°=‰©•Ð°ÍåÍÑ•´°½È½¹™¥ÕÉ…Ñ¥½¸Í½Á”ü(Ø¸%ÌÑ¡•É”„½µÁ•Ñ¥¹œÑ…‰±”Ý¥Ñ •ÅÕ…°½È‰•ÑÑ•È½Ù•É…”ü()½µÁ±•Ñ”½Ù•É…”•ÍÑ…‰±¥Í¡•ÌÍÑÉÕÑÕÉ…°½µÁ…Ñ¥‰¥±¥Ñä°¹½ÐÍ•µ…¹Ñ¥Œ¥‘•¹Ñ¥Ñä¸Q…‰±”É½±”…¹¥¹‘•Á•¹‘•¹Ð•Ù¥‘•¹”…É”ÍÑ¥±°É•ÅÕ¥É•¸((ŒŒŒ5½‘•°‘¥ÍÉ¥µ¥¹…Ñ½Èµ‘•Á•¹‘•¹ÐÉ•±…Ñ¥½¹Í¡¥ÁÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€()M½µ”É•±…Ñ¥½¹Í¡¥ÁÌ…É”½ÉÉ•Ð½¹±äÝ¡•¸„‘¥ÍÉ¥µ¥¹…Ñ½È¥ÌÁ…ÉÐ½˜Ñ¡”­•ä¸½È•á…µÁ±”è()Ñ•áÐ)%59M%=8€ÌÀ¹-e<(€€€MQQ€ô€ÀƒŠH•¹…‰±•5½‘Õ±”ƒŠH9}-e}=	)P¹­•å}½‰©•Ð(€€€MQQ€ô€ÄƒŠH‘¥Í…‰±•5½‘Õ±”ƒŠH9}Y%I%9}=	)P¹Ù¥É¥¹}­•å}½‰©•Ð)€()M¥µ¥±…É±ä°9}=9€½Ý¹•ÉÍ¡¥À¥ÌÁ½±åµ½ÉÁ¡¥Œè()Ñ•áÐ)=‰©•ÐµÍ½Á•€€ƒŠH¥‘}­•å}½‰©•ÐÉ•Í½±Ù•Ì°¥‘}™¥ÉµÝ…É”€ô€À)¥ÉµÝ…É”µÍ½Á•ƒŠH¥‘}­•å}½‰©•Ð€ô€À°¥‘}™¥ÉµÝ…É”É•Í½±Ù•Ì)€()¼¹½Ð™½É”Ñ¡•Í”¥¹Ñ¼Õ¹½¹‘¥Ñ¥½¹…°™½É•¥¸­•åÌ¸I•½ÉÑ¡”‘¥ÍÉ¥µ¥¹…Ñ½È…ÌÁ…ÉÐ½˜Ñ¡”É•±…Ñ¥½¹Í¡¥À¸((ŒŒŒ½É´½µÁ•Ñ¥¹œ•áÁ±…¹…Ñ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÀá€()U¹•ÉÑ…¥¹Ñäè¡åÁ½Ñ¡•Í¥Í€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()¡åÁ½Ñ¡•Í¥Ì¥ÌÕÍ•™Õ°½¹±äÝ¡•¸…±Ñ•É¹…Ñ¥Ù•Ì…É”•áÁ±¥¥Ð¸½È%59M%=8€ÌÈ¹MeM€°É•‘¥‰±”…¹‘¥‘…Ñ•Ì¥¹±Õ‘”…Ñ…±½Õ”ÍåÍ}µ½‘½‰©€°‘…Ñ…‰…Í”µ±½…°ÍåÍÑ•´%Ì°…¹™Õ¹Ñ¥½¹…°]!=€¸1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸½‰Í•ÉÙ…Ñ¥½¸½˜€Å€‘½•Ì¹½Ð‘¥ÍÑ¥¹Õ¥Í Ñ¡•´¸()½È•… …¹‘¥‘…Ñ”°ÁÉ•‘¥Ðè((´Ù…±Õ•Ì•áÁ•Ñ•¥¸…Ð±•…ÍÐÑÝ¼½¹Ñ•áÑÌì(´É½ÝÌ½È…ÁÑÕÉ•ÌÑ¡…ÐÍ¡½Õ±¹½Ðµ…Ñ ì(´‰•¡…Ù¥½È™½ÈÍ•¹Ñ¥¹•±Ì…¹µ¥ÍÍ¥¹œ‘…Ñ„ì(´Ý¡…ÐÝ½Õ±™…±Í¥™ä½È¹…ÉÉ½ÜÑ¡”ÁÉ½Á½Í…°¸()AÉ•™•È„Ñ•ÍÐÝ¡•É”Ñ¡”ÁÉ•‘¥Ñ¥½¹Ì‘¥Ù•É”¸I•Á•…Ñ¥¹œ„…Í”¥¸Ý¡¥ …±°…¹‘¥‘…Ñ•Ì•ÅÕ…°€Å€…‘‘Ì½Ù•É…”‰ÕÐ¹½Ð‘¥ÍÉ¥µ¥¹…Ñ¥½¸¸((ŒŒŒM••¬¥¹‘•Á•¹‘•¹Ð½ÉÉ½‰½É…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÀå€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€°ÍÁ•¥™¥…Ñ¥½¹€()MÑÉ½¹œ½¹±ÕÍ¥½¹Ì¹½Éµ…±±ä½µ‰¥¹”•Ù¥‘•¹”±…ÍÍ•ÌÑ¡…Ð‘¼¹½Ðµ•É•±äÉ•Á•…ÐÑ¡”Í…µ”¥µÁ±•µ•¹Ñ…Ñ¥½¸…ÍÍÕµÁÑ¥½¸¸()ðAÉ¥µ…Éä½‰Í•ÉÙ…Ñ¥½¸ðUÍ•™Õ°¥¹‘•Á•¹‘•¹Ð½ÉÉ½‰½É…Ñ¥½¸ð)ð€´´´ð€´´´ð)ðÕ¹‘•±…É•½±Õµ¸É•±…Ñ¥½¹Í¡¥Àð…ÁÁ±¥…Ñ¥½¸ÅÕ•Éä°U$‰•¡…Ù¥½È°½È½µÁ±•Ñ”…ÍÍ½¥…Ñ¥½¸Á…Ñ ð)ð‘¥…¹½ÍÑ¥Œ™¥•±ðÁÉ½‘ÕÐ‘¥…É…´°½¹ÑÉ½±±•½¹™¥ÕÉ…Ñ¥½¸¡…¹”°½ÈÁÕ‰±¥ŒÍÁ•¥™¥…Ñ¥½¸ð)ðÉ•Í½ÕÉ”µ­•äÍ•µ…¹Ñ¥Ìð±¥Ñ•É…°™Õ¹Ñ¥½¹…°™É…µ”…¹U$Á±…•µ•¹Ðð)ð…Ñ…±½Õ”½¹‘¥Ñ¥½¸ð½‰Í•ÉÙ•Ù¥Í¥‰¥±¥Ñä½È…•ÁÑ•½É•©•Ñ•ÁÉ½É…µµ¥¹œÙ…±Õ”ð)ð‘•™…Õ±Ð½ÈÍ•¹Ñ¥¹•°Á…ÑÑ•É¸ð½µÁ•Ñ¥¹œ½¹É•Ñ”É½ÝÌ…¹ÉÕ¹Ñ¥µ”Í•±•Ñ¥½¸‰•¡…Ù¥½Èð()QÝ¼…ÍÍ½¥…Ñ¥½¸Ñ…‰±•ÌÁ½ÁÕ±…Ñ•‰äÑ¡”Í…µ”±½…‘•È…É”Ù…±Õ…‰±”ÍÑÉÕÑÕÉ…°•Ù¥‘•¹”°‰ÕÐ¹½Ð¹••ÍÍ…É¥±ä¥¹‘•Á•¹‘•¹ÐÍ•µ…¹Ñ¥Œ•Ù¥‘•¹”¸((ŒŒŒM•…É ™½È½Õ¹Ñ•É•á…µÁ±•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°É•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹Ñäèµ…å€()Q•ÍÐÑ¡”™Õ±°Á½ÁÕ±…Ñ•‘½µ…¥¸Ý¡•É”™•…Í¥‰±”°¥¹±Õ‘¥¹œè((´9U11€°€Á€°•µÁÑä°¹•…Ñ¥Ù”°…¹‘•™…Õ±ÐÉ½ÝÌì(´‘ÕÁ±¥…Ñ”•áÑ•É¹…°¥‘•¹Ñ¥™¥•ÉÌì(´=‰©•ÑÌ…ÍÍ¥¹•Ñ¼Í•Ù•É…°ÍåÍÑ•µÌì(´¥Ñ•µÌÝ¥Ñ Í•Ù•É…°™¥ÉµÝ…É”‘•™¥¹¥Ñ¥½¹Ì½È‰Õ¥±‘Ìì(´™¥á•…¹É•Á±…•…‰±”=‰©•Ð…±Ñ•É¹…Ñ¥Ù•Ìì(´•Ù¥•ÌÝ¥Ñ ‘¥™™•É•¹Ð5½‘Õ±”±…å½ÕÑÌì(´…¹½Ñ¡•È‘¥…¹½ÍÑ¥Œ™…µ¥±ä½È™¥ÉµÝ…É”É•Ù¥Í¥½¸ì(´Á½Í¥Ñ¥Ù”°¹•…Ñ¥Ù”°•ÉÉ½È°…¹Ñ¥µ•½ÕÐ½ÕÑ½µ•Ì¸()½Õ¹Ñ•É•á…µÁ±”µ…äÉ•©•Ð„±…¥´½ÈÉ•Ù•…°„µ¥ÍÍ¥¹œ½¹‘¥Ñ¥½¸¸¼¹½Ð‘¥Í…É¥Ðµ•É•±ä‰•…ÕÍ”µ½ÍÐÉ½ÝÌµ…Ñ ¸((ŒŒŒ¡…¹”½¹”Ù…É¥…‰±”…Ð„Ñ¥µ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÄÅ€()½¹ÑÉ½±±•U$…¹•Ù¥”Ñ•ÍÑÌ…É”ÍÑÉ½¹•ÍÐÝ¡•¸•á…Ñ±ä½¹”¥¹ÁÕÐ¡…¹•Ì¸I•½É„‰…Í•±¥¹”°Á•É™½É´½¹”¡…¹”°É•Á•…ÐÑ¡”Í…µ”É•ÅÕ•ÍÑÌ°…¹‘¥™˜‰½Ñ ÑÉ…™™¥Œ…¹Á•ÉÍ¥ÍÑ•ÍÑ…Ñ”¸()½ÈÍÑ…Ñ”µ¡…¹¥¹œÑ•ÍÑÌè((Ä¸É•……¹Í…Ù”Ñ¡”‰…Í•±¥¹”ì(È¸½¹™¥É´Ñ¡…ÐÑ¡”Ñ…É•Ð•Ù¥”…¹5½‘Õ±”…É”Õ¹¥ÅÕ•±ä¥‘•¹Ñ¥™¥•ì(Ì¸¡…¹”½¹”ÁÉ½Á•ÉÑäì(Ð¸É•½É…­¹½Ý±•‘•µ•¹Ð…¹Ñ•Éµ¥¹…°ÍÑ…Ñ”ì(Ô¸É•…Ñ¡”½¹™¥ÕÉ…Ñ¥½¸‰…¬ì(Ø¸É•ÍÑ½É”Ñ¡”‰…Í•±¥¹”Ý¡•¸Í…™”ì(Ü¸‘¥ÍÑ¥¹Õ¥Í …•ÁÑ•ÑÉ…¹Í™•È™É½´•™™•Ñ¥Ù”½¹™¥ÕÉ…Ñ¥½¸¸()¸-€…±½¹”¥Ì¹½ÐÙ•É¥™¥…Ñ¥½¸¸((ŒŒŒ±…ÍÍ¥™ä…¹ÁÉ½µ½Ñ”Ñ¡”É•ÍÕ±Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÄÉ€()…ÕÑ¥½¹Ìè±¥µ¥Ñ…Ñ¥½¹€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€()UÍ”Ñ¡”±•Ù•±Ì¥¸mÙ¥‘•¹”…¹½¹™¥‘•¹•t¡•Ù¥‘•¹”µ…¹µ½¹™¥‘•¹”¹µ¤¸AÉ½µ½Ñ”„É•ÍÕ±Ð¥¹Ñ¼É•™•É•¹”‘½Õµ•¹Ñ…Ñ¥½¸½¹±äÝ¡•¸è((´Ñ¡”¹…µ•ÍÁ…”…¹Í½Á”…É”•áÁ±¥¥Ðì(´­¹½Ý¸Ù…±Õ•ÌÉ•Í½±Ù”½È•á•ÁÑ¥½¹Ì…É”‘½Õµ•¹Ñ•ì(´Ù¥…‰±”…±Ñ•É¹…Ñ¥Ù•Ì¡…Ù”‰••¸Ñ•ÍÑ•ì(´Ñ¡”±…¥´…¸‰”…ÁÁ±¥•Ý¥Ñ¡½ÕÐ…•ÍÌÑ¼Ñ¡”½É¥¥¹…°¥¹Ù•ÍÑ¥…Ñ½ËŠeÌ¥¹ÑÕ¥Ñ¥½¸ì(´„™…±Í¥™¥•È½ÈÉ•µ…¥¹¥¹œ±¥µ¥Ñ…Ñ¥½¸¥ÌÉ•½É‘•¸()Q¡”É•Ù•ÉÍ”µ•¹¥¹••É¥¹œÍ•Ñ¥½¸É•Ñ…¥¹ÌÑ¡”•Ù¥‘•¹”Á…Ñ °Õ¹É•Í½±Ù•…±Ñ•É¹…Ñ¥Ù•Ì°…¹É•©•Ñ•Í¡½ÉÑÕÑÌ¸Q¡”ÍÑ…‰±”½Á•É…Ñ¥½¹…°½¹±ÕÍ¥½¸‰•±½¹Ì¥¸Ñ¡”É•±•Ù…¹ÐAÉ½Ñ½½°°•Ù¥”5½‘•°°¥…¹½ÍÑ¥Ì°AÉ½É…µµ¥¹œ°M•¹…É¥¼¹¥¹”°½È%¹Ñ•É¹…±ÌÁ…”¸((ŒŒŒI•ÁÉ½‘Õ¥‰¥±¥Ñä¡•­±¥ÍÐ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÀéÌÀÀÀÀÄÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()	•™½É”±½Í¥¹œ…¸¥¹Ù•ÍÑ¥…Ñ¥½¸°Ù•É¥™äÑ¡…Ð…¹½Ñ¡•ÈÁ•ÉÍ½¸…¸É•½Ù•ÈÑ¡”Í…µ”½¹±ÕÍ¥½¸™É½´è((´Í½ÕÉ”™¥¹•ÉÁÉ¥¹ÑÌ…¹É•Ù¥Í¥½¸ì(´•á…ÐÅÕ•É¥•Ì°É•ÅÕ•ÍÑÌ°…¹É•ÍÁ½¹Í”½¹Ñ•áÐì(´É…ÜÙ…±Õ•Ì…¹•á•ÁÑ¥½¸É½ÝÌì(´¹…µ•ÍÁ…”…¹Í•¹Ñ¥¹•°ÉÕ±•Ìì(´…É‘¥¹…±¥Ñä…¹½Ù•É…”½Õ¹ÑÌì(´ÍÕÁÁ½ÉÑ¥¹œ…¹½¹ÑÉ…‘¥Ñ¥¹œ•Ù¥‘•¹”ì(´½¹™¥‘•¹”°Í½Á”°…¹™…±Í¥™¥•Èì(´±¥¹­ÌÑ¼Ñ¡”ÁÉ½µ½Ñ•É•ÍÕ±Ð…¹Ñ¡”mI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Ét¡É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ¤¸()U¹­¹½Ý¸¥Ì„Ù…±¥½ÕÑ½µ”¸Ý•±°µ‰½Õ¹‘•Õ¹­¹½Ý¸¥Ìµ½É”ÕÍ•™Õ°Ñ¡…¸…¸…ÑÑÉ…Ñ¥Ù”‰ÕÐÕ¹Ñ•ÍÑ…‰±”µ…ÁÁ¥¹œ¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÈÄ()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½½Á•¸µÅÕ•ÍÑ¥½¹Ì¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒ=Á•¸EÕ•ÍÑ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÀÅ€()…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€()Q¡¥ÌÁ…”½¹Ñ…¥¹Ì½¹±äÅÕ•ÍÑ¥½¹ÌÑ¡…ÐÉ•µ…¥¸Õ¹É•Í½±Ù•…™Ñ•ÈÉ½ÍÌµ¡•­¥¹œÑ¡”…¹½¹¥…°5å!=5MÕ¥Ñ”€Ì¸Ô¸Ìà‘…Ñ…‰…Í•Ì°=Á•¹EÕ•Éä¹ÑáÑ€°Ñ¡”¥¹½ÉÁ½É…Ñ•…ÁÑÕÉ•Ì°ÁÉ½‘ÕÐ‘½Õµ•¹Ñ…Ñ¥½¸°…¹Ñ¡”É•±…Ñ¥½¹Í¡¥ÁÌ•ÍÑ…‰±¥Í¡••±Í•Ý¡•É”¥¸Ñ¡¥Ì‘½Õµ•¹Ñ…Ñ¥½¸¸()… •¹ÑÉäÍÑ…Ñ•ÌÑ¡”­¹½Ý¸‰½Õ¹‘…Éä‰•™½É”Ñ¡”µ¥ÍÍ¥¹œ•Ù¥‘•¹”Í¼Ñ¡…Ð±…Ñ•È¥¹Ù•ÍÑ¥…Ñ¥½¹Ì‘¼¹½ÐÉ•½Á•¸™…ÑÌÑ¡…Ð…É”…±É•…‘ä•ÍÑ…‰±¥Í¡•¸((ŒŒŒ]!<€ÄÌ…Ñ•Ý…äÁÉ½Á•ÉÑ¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÀÉ€((ŒŒŒŒ%59M%=8€ÈÁ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…Ñ•Ý…å€°ÍÍ€°ÑÁ€°Ù•ÉÍ¥½¹€°é¥‰••€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€°¹½Ð•Ù¥‘•¹•€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°•Ù¥‘•¹•€°Í½ÕÉ•€()AÉ¥½È…Ñ•Ý…äµ¥‘•¹Ñ¥™¥…Ñ¥½¸É•Í•…É ¡…Ì™±…•]!<€ÄÌ%59M%=8€ÈÁ€…Ì…¸•¹½Õ¹Ñ•É•ÁÉ½Á•ÉÑä°‰ÕÐÑ¡”ÕÉÉ•¹Ñ±äÁÉ•Í•ÉÙ••Ù¥‘•¹”¡…¥¸‘½•Ì¹½Ðå•Ð•ÍÑ…‰±¥Í ¥ÑÌ±…ÍÍ¥ŒML½Q@Í•µ…¹Ñ¥Ì¸Q¡”…¹½¹¥…°±…ÍÍ¥Œ]!=|ÄÌ¹Á‘™€É•¥ÍÑÉä‘½•Ì¹½Ð‘•™¥¹”¥Ð°Ñ¡”i¥	•”]!<€ÄÍ€É•¥ÍÑÉä‘½•Ì¹½Ð‘•™¥¹”¥Ð°…¹½¹¥…°5å!=5MÕ¥Ñ”=A8¹‘‰€ÁÉ½Ù¥‘•Ì¹¼™Õ¹Ñ¥½¹…°]!<€ÄÌ%59M%=8€ÈÁ€Ñ•µÁ±…Ñ”°…¹Ñ¡”ÁÉ•Í•ÉÙ•ÐÔÐ…¹5 ÈÀÈ…Ñ•Ý…äµ¥¹™½Éµ…Ñ¥½¸…ÁÑÕÉ•Ì•á…µ¥¹•¥¸Ñ¡”ÕÉÉ•¹Ð½ÉÉ•Ñ¥½¸‘¼¹½Ð½¹Ñ…¥¸¥Ð¸()Q¡¥Ì¥Ì„€¨©ÁÉ½Ù•¹…¹”…À¨¨°¹½Ð•Ù¥‘•¹”Ñ¡…ÐÑ¡”ÁÉ½Á•ÉÑä‘½•Ì¹½Ð•á¥ÍÐ¸AÉ½µ½Ñ¥½¸Ñ¼Ñ¡”™Õ¹Ñ¥½¹…°É•™•É•¹”É•ÅÕ¥É•ÌÑ¡”ÍÁ•¥™¥Œ…¹½¹¥…°Í½ÕÉ”½È™¥ÉÍÐµ¡…¹…ÁÑÕÉ”Ñ¡…Ð•ÍÑ…‰±¥Í¡•ÌÑ¡”É•ÅÕ•ÍÐ½É•ÍÁ½¹Í”™½É´…¹Á…å±½…°™½±±½Ý•‰äÍ•µ…¹Ñ¥Œ½ÉÉ½‰½É…Ñ¥½¸¸¼¹½Ð¥¹™•È„µ•…¹¥¹œ™É½´‘¥…¹½ÍÑ¥Œ%59M%=8€Ù€µ¥É½½¹ÑÉ½±±•ÈµÙ•ÉÍ¥½¸™¥•±‘Ì½È™É½´…¹ä¹Õµ•É¥…±±äÍ¥µ¥±…È¹…µ•ÍÁ…”¸((ŒŒŒŒ%59M%=8€ÐÁ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€°ÍÍ€°ÑÁ€°Ù•ÉÍ¥½¹€°é¥‰••€)U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€°Õ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()á¥ÍÑ•¹”¥Ì•ÍÑ…‰±¥Í¡•µ½É”ÍÑÉ½¹±äÑ¡…¸Í•µ…¹Ñ¥Ì¸%¹‘•Á•¹‘•¹Ð™¥ÉÍÐµ¡…¹ÐÔÐ…¹5 ÈÀÈ…Ñ•Ý…äµ¥¹™½Éµ…Ñ¥½¸…ÁÑÕÉ•Ì‰½Ñ Í¡½Ü€¨ŒÄÌ¨¨ÐÀŒ€…¹‰½Ñ É•ÑÕÉ¸€¨ŒÄÌ¨¨ÐÀ¨Ð¨ÀŒ€¸()]¡…ÐÉ•µ…¥¹ÌÕ¹É•Í½±Ù•¥ÌÑ¡”µ•…¹¥¹œ½˜Ñ¡”ÑÝ¼É•ÑÕÉ¹•Ù…±Õ•Ì°Ý¡•Ñ¡•È•¥Ñ¡•È™¥•±Ù…É¥•Ì¥¹‘•Á•¹‘•¹Ñ±ä°…¹Ñ¡”…ÁÁ±¥…‰¥±¥Ñä…É½ÍÌ…Ñ•Ý…äµ½‘•±Ì…¹™¥ÉµÝ…É”É•Ù¥Í¥½¹Ì¸Q¡”¹•áÐ‘¥ÍÉ¥µ¥¹…Ñ¥¹œ•Ù¥‘•¹”¥Ì„É½ÍÌµµ½‘•°½ÈÉ½ÍÌµ™¥ÉµÝ…É”½‰Í•ÉÙ…Ñ¥½¸¥¸Ý¡¥ …Ð±•…ÍÐ½¹”É•ÑÕÉ¹•Ù…±Õ”‘¥™™•ÉÌ°½È„…¹½¹¥…°¥µÁ±•µ•¹Ñ…Ñ¥½¸½ÍÁ•¥™¥…Ñ¥½¸Í½ÕÉ”¹…µ¥¹œÑ¡”™¥•±‘Ì¸U¹Ñ¥°Ñ¡•¸°ÁÉ•Í•ÉÙ”Ñ¡”É•ÍÁ½¹Í”…ÌÑÝ¼Á½Í¥Ñ¥½¹…°Õ¹­¹½Ý¸Ù…±Õ•Ì¸()Q¡”i¥	•”ÍÁ•¥™¥…Ñ¥½¸Ì%59M%=8€ÄÝ€¡…É‘Ý…É”µÙ•ÉÍ¥½¸‘•™¥¹¥Ñ¥½¸¥Ì¹½ÐÁ…ÉÐ½˜Ñ¡¥Ì½Á•¸ÅÕ•ÍÑ¥½¸èÑ¡…Ðµ•…¹¥¹œ¥Ì•ÍÑ…‰±¥Í¡•™½ÈÑ¡”i¥	•”]!<€ÄÍ€Ù…É¥…¹Ð¸]¡…ÐÉ•µ…¥¹ÌÕ¹•ÍÑ…‰±¥Í¡•¥ÌÝ¡•Ñ¡•È…¹ä±…ÍÍ¥ŒML½Q@¥µÁ±•µ•¹Ñ…Ñ¥½¸É•ÕÍ•Ì¹Õµ•É¥Œ€ÄÝ€Ý¥Ñ Ñ¡”Í…µ”Í•µ…¹Ñ¥Ì¸((ŒŒŒ¥…¹½ÍÑ¥Œ…¹ÁÉ½É…µµ¥¹œ™¥•±‘Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÀÕ€((ŒŒŒŒ%59M%=8€ÌÈ¹MeM€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÀÙ€()U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()5!…Ñ…±½Õ”¹‘ˆ¹9}MeMQ4¹ÍåÍ}µ½‘½‰©€¥ÌÑ¡”±•…‘¥¹œ…¹‘¥‘…Ñ”¸1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸½‰Í•ÉÙ…Ñ¥½¹Ì…¹¹½Ð‘¥ÍÑ¥¹Õ¥Í ¥Ð™É½´½¥¹¥‘•¹ÐÙ…±Õ•Ì¥¸½Ñ¡•È¹…µ•ÍÁ…•Ì¸()ÍÕ•ÍÍ™Õ°¹½¸µ1¥¡Ñ¥¹œÉ•ÍÁ½¹Í”¥ÌÍÑ¥±°É•ÅÕ¥É•¸Q¡”µ½ÍÐ‘¥ÍÉ¥µ¥¹…Ñ¥¹œ…Í•Ì…É”Q¡•Éµ½É•Õ±…Ñ¥½¸°¹•Éä5…¹…•µ•¹Ð°•ÍÌ½¹ÑÉ½°°…¹%¹Ñ•É…Ñ¥½¸Õ¹Ñ¥½¹Ì°Ý¡½Í”ÍåÍ}µ½‘½‰©€°‘…Ñ…‰…Í”ÍåÍÑ•´%°…¹™Õ¹Ñ¥½¹…°]!=€Ù…±Õ•Ì‘¥™™•È¸()%Ð…±Í¼É•µ…¥¹ÌÕ¹­¹½Ý¸¡½ÜMeM€Í•±•ÑÌ½¹”…Ñ¥Ù”½¹Ñ•áÐÝ¡•¸…¸=‰©•Ð‰•±½¹ÌÑ¼Í•Ù•É…°…Ñ…±½Õ”ÍåÍÑ•µÌ¸((ŒŒŒŒ%59M%=8€Ñ€…¹€Õ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()=A8¹‘‰€•ÍÑ…‰±¥Í¡•ÌÑ¡”ÑÉ…¹ÍÁ½ÉÐÍÕÉ™…”è%59M%=8€Ñ€…ÉÉ¥•ÌÄ¸¹Ù€°%59M%=8€Õ€…ÉÉ¥•ÌÜ¸¹ÄÉ€°…¹•Ù•Éä€™¥•±¡…ÌÉ…¹”€À¸¸ÈÔÕ€¸Q¡”½¹™½¹™¥ÕÉ…Ñ½ÉÍ€Í•ÅÕ•¹”Í•¹‘ÌÑ¡”½ÉÉ•ÍÁ½¹‘¥¹œÁÉ½É…µµ¥¹œ™½ÉµÌ…¹¥Ì‘•ÍÉ¥‰•Ñ¡•É”…ÌÙ¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸¸()]¡…ÐÉ•µ…¥¹ÌÕ¹É•Í½±Ù•¥ÌÑ¡”É½ÍÌµ‘…Ñ…‰…Í”½ÉÉ•±…Ñ¥½¸Ñ¼…Ñ…±½Õ”Í•µ…¹Ñ¥Ì¸9¼…¹½¹¥…°É•±…Ñ¥½¸•ÍÑ…‰±¥Í¡•ÌÑ¡…ÐÅ€•ÅÕ…±ÌÑ¡”™¥ÉµÝ…É”9}=9€É½ÜÝ¥Ñ ÁÉ½É•ÍÍ¥Ù”€ô€Å€°½È…¸•ÅÕ¥Ù…±•¹ÐÁ½Í¥Ñ¥½¹…°ÉÕ±”™½È•Ù•Éä™¥ÉµÝ…É”¸½¹ÑÉ½±±•½‰Í•ÉÙ…Ñ¥½¹Ì…É”ÍÑ¥±°¹••‘•Ñ¼‘•Ñ•Éµ¥¹”¡½ÜÄ¸¹ÄÉ€•¹½‘”Á¡åÍ¥…°½½¹™¥ÕÉ…Ñ½È½¹Ñ•¹ÑÌ¥¸•Ù¥”™…µ¥±¥•Ì…¹¡½ÜÑ¡½Í”ÑÉ…¹ÍÁ½ÉÐÁ½Í¥Ñ¥½¹Ì½ÉÉ•ÍÁ½¹°Ý¡•É”…ÁÁ±¥…‰±”°Ñ¼™¥ÉµÝ…É”µÍÁ•¥™¥ŒÍåµ‰½±ÌÍÕ …Ì€°A1€°5€°€°%€°i€°i	€°9€°Q€°…¹M€¸()Q¡¥ÌÅÕ•ÍÑ¥½¸¹¼±½¹•È½¹•É¹ÌÑ¡”•á¥ÍÑ•¹”½È¹Õµ•É¥ŒÑÉ…¹ÍÁ½ÉÐÉ…¹”½˜Ä¸¹ÄÉ€ìÑ¡½Í”…É”•ÍÑ…‰±¥Í¡•¸%Ð½¹•É¹ÌÑ¡•¥È•Ù¥”µÍÁ•¥™¥ŒÍ•µ…¹Ñ¥Œ½ÉÉ•±…Ñ¥½¸Ý¥Ñ …Ñ…±½Õ”‘•™¥¹¥Ñ¥½¹Ì…¹Á¡åÍ¥…°Á½Í¥Ñ¥½¹Ì¸((ŒŒŒŒ%59M%=8€ÌÄÁ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÀá€()%59M%=8€ÌÄÁ€…ÉÉ¥•Ì…¸=‰©•ÐµÍÁ•¥™¥ŒÙ…±Õ”Ý¥Ñ¡½ÕÐ„•¹•É¥Œ½¹™¥ÕÉ…Ñ¥½¸¥¹‘•à¸=A8¹‘‰€ÍÕÁÁ±¥•Ì¹•¥Ñ¡•È½É‘¥¹…ÉäÁ…É…µ•Ñ•Èµ•Ñ…‘…Ñ„¹½È„•¹•É…°‘•½‘•È™½È¥Ð¸()%ÑÌµ•…¹¥¹œ…¹Ù…±Õ”‘½µ…¥¸É•µ…¥¸Ñ¼‰”•ÍÑ…‰±¥Í¡•Á•È=‰©•Ð…¹•Ù¥”™…µ¥±ä¸((ŒŒŒŒ!…É‘Ý…É”…¹µ¥É½½¹ÑÉ½±±•ÈÙ•ÉÍ¥½¹Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°Ù•ÉÍ¥½¹€)U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°Í½ÕÉ•€()%59M%=8€Í€…¹€Ù€ÕÍ”Ñ¡”Í…µ”±½¥…°Y•ÉÍ¥½¸©I•±•…Í”©	Õ¥±‘€ÍÑÉÕÑÕÉ”…ÌÑ¡”™¥ÉµÝ…É”É•ÍÁ½¹Í”¸9¼½ÉÉ•ÍÁ½¹‘¥¹œ¡…É‘Ý…É”´½Èµ¥É½½¹ÑÉ½±±•ÈµÙ•ÉÍ¥½¸™¥•±‘Ì¡…Ù”‰••¸™½Õ¹¥¸Ñ¡”…¹½¹¥…°‘…Ñ…‰…Í•Ì¸()%ÐÉ•µ…¥¹ÌÕ¹­¹½Ý¸Ý¡•Ñ¡•È5å!=5MÕ¥Ñ”ÕÍ•ÌÑ¡•Í”Ù…±Õ•ÌÑ¼‘¥ÍÑ¥¹Õ¥Í ÁÉ½‘ÕÐÙ…É¥…¹ÑÌ½È½µÁ…Ñ¥‰¥±¥Ñä°…¹Ý¡•Ñ¡•È…¸Õ¹ÁÉ•Í•ÉÙ•‘…Ñ„Í½ÕÉ”µ…ÁÌÑ¡•´Ñ¼…Ñ…±½Õ”•Ù¥•Ì¸((ŒŒŒ‘‘É•ÍÌÍ•±•Ñ¥½¸…¹•¹½‘¥¹œ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄÁ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè½¹±ä™½É€°É•Ù¥Í¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()Q¡”‘…Ñ…‰…Í”•ÍÑ…‰±¥Í¡•ÌÍåÍÑ•´µÑ¼µÉÕ±”…ÍÍ½¥…Ñ¥½¹Ì°…‘‘É•ÍÌÑ•µÁ±…Ñ•Ì°…¹=‰©•Ðµ™…µ¥±äÅÕ…±¥™¥…Ñ¥½¸¸%Ð‘½•Ì¹½ÐÁÉ•Í•ÉÙ”Ñ¡”™¥¹…°Í•±•Ñ¥½¸…¹É•¹‘•É¥¹œ…±½É¥Ñ¡´¸()Q¡”É•µ…¥¹¥¹œÅÕ•ÍÑ¥½¹Ì…É”è((´!½Ü‘½•Ì5å!=5MÕ¥Ñ”¡½½Í”…µ½¹œ„ÍåÍÑ•´Ì™…µ¥±äµÅÕ…±¥™¥•…¹™…µ¥±äµÕ¹ÅÕ…±¥™¥•…‘‘É•ÍÌÉÕ±•Ìü(´!½Ü…É”±•Ù•±|É}ÉÕ±•€…¹±•Ù•±|Ñ}ÉÕ±•€½¹ÍÕµ•üQ¡•¥È¹½¹é•É¼Ù…±Õ•Ì½ÕÈ½¸Ñ¡”1¥¡Ñ¥¹œ½ÕÑ½µ…Ñ¥½¸•¹•É…°°•¹Ù¥É½¹µ•¹Ð°É½ÕÀ°…¹ÐÈÈ•áÑ•¹Í¥½¸ÉÕ±•Ì°‰ÕÐÑ¡”ÉÕ¹Ñ¥µ”½µÁ½Í¥Ñ¥½¸Ý¥Ñ Ñ¡”‘•‘¥…Ñ•±•Ù•°ÉÕ±•Ì¥Ì¹½Ð•¹½‘•¸(´!½Ü¥ÌÙ…±¥‘¥Ñå}ÉÕ±•€•Ù…±Õ…Ñ•üQ¡”½¹±ä¹½¹•µÁÑä•áÁÉ•ÍÍ¥½¸¥¸Ñ¡¥ÌÉ•Ù¥Í¥½¸¥Ì5=õM1í€½¸Ñ¡”Q¡•Éµ½É•Õ±…Ñ¥½¸Í±…Ù”µÁÉ½‰”ÉÕ±”¸(´!½Ü¥Ì½™™Í•Ñ}…‘Ù€…ÁÁ±¥•ü%Ð¥ÌÁ½ÁÕ±…Ñ•½¹±ä™½ÈÑ¡”ÑÝ¼ÐÈÈµ½‘”µÍÁ•¥™¥ŒÉÕ±•Ì°Ý¥Ñ Ù…±Õ•Ì€ÐäÙ€…¹€ÈÔÙ€¸(´U¹‘•ÈÝ¡¥ •Ù¥”±…å½ÕÑÌ‘½•ÌÑ¡”‘¥…¹½ÍÑ¥Œ½ÕÑ•È]!I€™½±±½ÜÑ¡”½¹™¥ÕÉ•…‘‘É•ÍÌ½˜Í±½Ñ€€Å€°…¹Ý¡…ÐÉÕ±”…ÁÁ±¥•ÌÝ¡•¸Í±½Ð€Å€¥Ì…‰Í•¹Ð°‘¥Í…‰±•°½È‘¥™™•É•¹Ñ±ä…‘‘É•ÍÍ•ü((ŒŒŒ…Ñ…±½Õ”‰•¡…Ù¥½È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄÅ€((ŒŒŒŒ¥ÉµÝ…É”Í•±•Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()Q¡”…Ñ…±½Õ”™¥ÉµÝ…É”¥‘•¹Ñ¥Ñä¥ÌÑ¡”Ñ¡É•”µ½µÁ½¹•¹ÐX¹H¹‰€ÑÕÁ±”‘¥ÍÑÉ¥‰ÕÑ•…É½ÍÌ9}%I5]I€…¹9}	U%1M€¸¸•áÁ±¥¥Ð€´Å€¥ÌÍÑÉ½¹±ä½ÉÉ½‰½É…Ñ•…Ì…¹ä½ÈÕ¹ÍÁ•¥™¥•™½ÈÑ¡…Ð½µÁ½¹•¹Ð°Ý¡¥±”„µ¥ÍÍ¥¹œ‰Õ¥±É½ÜÉ•µ…¥¹ÌÍÑÉÕÑÕÉ…±±ä‘¥ÍÑ¥¹Ð¸()Q¡”•á…Ð5å!=5MÕ¥Ñ”Í•±•Ñ¥½¸ÁÉ••‘•¹”É•µ…¥¹ÌÕ¹­¹½Ý¸Ý¡•¸½¹É•Ñ”½µÁ½¹•¹ÑÌ°€´Å€Í•¹Ñ¥¹•±Ì°µÕ±Ñ¥Á±”‰Õ¥±É½ÝÌ°µ¥ÍÍ¥¹œ‰Õ¥±É½ÝÌ°]}‘•™…Õ±Ñ€°…¹±½…±¥é…Ñ¥½¸µ•Ñ…‘…Ñ„½Ù•É±…À¸((ŒŒŒŒ=‰©•ÐÉ•Á±…•µ•¹Ð()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹ÑäèÕ¹­¹½Ý¹€()™¥á•‘}­½€°Ù¥Í¥‰¥±¥Ñä½•‘¥Ñ…‰¥±¥Ñäµ•Ñ…‘…Ñ„°½¹‘¥Ñ¥½¹Ì°™¥ÉµÝ…É”°Í±½Ð°…¹ÁÉ½‘ÕÐ½¹Ñ•áÐ…±°½¹ÑÉ¥‰ÕÑ”Ñ¼Ñ¡”…Ù…¥±…‰±”=‰©•ÐÍ•Ð¸()Q¡”½µÁ±•Ñ”ÉÕ±”Ñ¡…Ð‘•Ñ•Éµ¥¹•ÌÝ¡•Ñ¡•È5å!=5MÕ¥Ñ”‘¥ÍÁ±…åÌ…¹Á•Éµ¥ÑÌÉ•Á±…•µ•¹Ð½˜…¸=‰©•Ð…Ð„Á…ÉÑ¥Õ±…È5½‘Õ±”É•µ…¥¹ÌÕ¹­¹½Ý¸¸((ŒŒŒŒA¡åÍ¥…°µÑ¼µ…‘Ù…¹•…¹ÑÉ…¹ÍÁ½ÉÐ½ÉÉ•±…Ñ¥½¸()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()Q¡”…Ñ…±½Õ”µ¹…Ñ¥Ù”Á¡åÍ¥…°Ñ½Á½±½äµ•¡…¹¥Í´¥Ì¹½Ü•ÍÑ…‰±¥Í¡•™½È½¹‘¥Ñ¥½¸µÉ•ÁÉ•Í•¹Ñ•‰É…¹¡•ÌèÉ•Í½±Ù”™¥ÉµÝ…É”Á¡åÍ¥…°‘•™¥¹¥Ñ¥½¹Ì…¹±•…°‘½µ…¥¹Ì°•¹Õµ•É…Ñ”M}=	)Q}%I5]I€½9}M1=QM€…¹‘¥‘…Ñ•Ì°½¹ÍÑÉ…¥¸M}M1=Q}=9%Q%=9€½9}=9%Q%=9€‰É…¹¡•Ì‰äÉ•…¡…‰¥±¥Ñä°Í•±•ÐÑ¡”µ…Ñ¡¥¹œ=‰©•ÐÑ½Á½±½ä°…¹½¹±äÑ¡•¸•Ù…±Õ…Ñ”…ÁÁ±¥…‰±”9}=9Y}IU1€É½ÝÌ¸9}A!e}Q=}Y}QI9M€É•µ…¥¹Ì„ÍÁ…ÉÍ”ÍÕÁÁ½ÉÑ¥¹œÑ…‰±”Ý¥Ñ ½¹±äÑ¡É•”™¥ÉµÝ…É”É½ÝÌ…¹¥Ì¹½ÐÑ¡”•¹•É¥Œµ•¡…¹¥Í´¸()=Á•¸‰½Õ¹‘…É¥•ÌÉ•µ…¥¸¹…ÉÉ½Ý•Èè((´Ý¡•Ñ¡•È…¹¡½Ü%59M%=8€Ð¹Ä¸¹ÄÉ€½ÉÉ•±…Ñ”Ý¥Ñ ™¥ÉµÝ…É”9}=9€‘•™¥¹¥Ñ¥½¹Ì½ÈÁÉ½É•ÍÍ¥Ù•€½É‘•É¥¹œ™½È•… •Ù¥”™…µ¥±äì(´¡½ÜÑ¼¥¹Ñ•ÉÁÉ•Ð…Ñ…±½Õ”…¹‘¥‘…Ñ•ÌÑ¡…Ð¡…Ù”¹¼•áÁ±¥¥ÐÁ¡åÍ¥…°ÁÉ•‘¥…Ñ”Ý¡•¸É•½¹ÍÑÉÕÑ¥¹œ„½µÁ±•Ñ”Á¡åÍ¥…°Ñ½Á½±½äì(´Ý¡•Ñ¡•ÈÑ•áÑÕ…°¥ÉÉ•Õ±…É¥Ñ¥•ÌÍÕ …Ì<½%€Ù•ÉÍÕÌ$½=€¡…Ù”…¸…ÁÁ±¥…Ñ¥½¸µ±•Ù•°¹½Éµ…±¥é…Ñ¥½¸¹½ÐÉ•ÁÉ•Í•¹Ñ•¥¸Ñ¡”…¹½¹¥…°‘…Ñ…‰…Í•Ìì(´Ý¡¥ ÁÉ½Á•ÉÑäµ±•Ù•°Á¡åÍ¥…°µÑ¼µ…‘Ù…¹•½ÉÉ•ÍÁ½¹‘•¹•Ì…É”½µÁ±•Ñ”Ý¡•¸Íåµ‰½°°É…¹”°½¹Ù•ÉÍ¥½¸°½È=9}Me5	=1}I€•Ù¥‘•¹”¥Ì…‰Í•¹Ðì(´¡½ÜÑ¡”É•¥ÍÑ•É•…Ñ…±½Õ”µ½‘”±…‰•±Ì½ÉÉ•ÍÁ½¹Ñ¼•Ù•Éä5å!=5MÕ¥Ñ”U$Á…Ñ ‰•å½¹Ñ¡”•á…ÐÍ•ÅÕ•¹”±…‰•±ÌÁÉ•Í•ÉÙ•¥¸=A8¹‘‰€¸((ŒŒŒŒ…Ñ…±½Õ”µÝ¥‘”…‘‘É•ÍÍ•µ™½É´9}=9€•ÅÕ¥Ù…±•¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€()½ÈÑ¡”½É‘¥¹…Éä…‘‘É•ÍÍ••Ù¥”™½É´°Ñ¡”µ•…¹¥¹œ½˜9}=9€¥Ì½ÉÉ½‰½É…Ñ•…ÌÑ¡”¹Õµ‰•È½˜Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈÁ½Í¥Ñ¥½¹ÌÁÉ½Ù¥‘•‰äÑ¡”•Ù¥”¸I•Í½±Ù••á…µÁ±•Ì…±Í¼µ…Ñ Ñ¡”½Õ¹Ð½˜…ÁÁ±¥…‰±”™¥ÉµÝ…É”µÍ½Á•Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸™¥•±‘Ì…™Ñ•È•á±Õ‘¥¹œÑ¡”½µµ½¸%€½%™¥•±¸()]¡…ÐÉ•µ…¥¹Ì½Á•¸¥ÌÝ¡•Ñ¡•ÈÑ¡…Ð‘…Ñ…‰…Í”µ½Õ¹Ð•ÅÕ¥Ù…±•¹”¡½±‘Ì™½È•Ù•Éä…Ñ…±½Õ”™¥ÉµÝ…É”°¥¹±Õ‘¥¹œ½¹‘¥Ñ¥½¹…°™¥•±‘Ì°Í¡…É•™¥ÉµÝ…É”‘•™¥¹¥Ñ¥½¹Ì°…¹•Ù¥•ÌÝ¥Ñ¡½ÕÐ…Ù…¥±…‰±”ÁÉ½‘ÕÐ‘¥…É…µÌ¸Q¡¥ÌÅÕ•ÍÑ¥½¸‘½•Ì¹½ÐÉ•½Á•¸Ñ¡”…‘‘É•ÍÍ•µ™½É´¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¸((ŒŒŒŒ…Ñ•Ý…ä9}=9€ô€ÄÕ€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()Q¡”•µÁÑäµ]!I€…Ñ•Ý…ä¥‘•¹Ñ¥Ñä™½É´¥Ì„Í•Á…É…Ñ”…Í”¸¥ÉÍÐµ¡…¹5 ÈÀÈ…¹ÐÔÐ…ÁÑÕÉ•Ì‰½Ñ É•ÑÕÉ¸9}=9€ô€ÄÕ€°½ÕÑÍ¥‘”Ñ¡”½É‘¥¹…Éä…‘‘É•ÍÍ•µ™½É´€À¸¸ÄÉ€É…¹”¸9Õµ•É¥…±±ä°€ÄÕ€¥Ì€Áá€ìÙ¥•Ý•¥¸™½ÕÈ‰¥ÑÌ°¥Ð¥Ì€ÄÄÄÅ€°…¸…±°µ½¹•ÌÁ…ÑÑ•É¸¸É•Í•ÉÙ•½ÈÍ•¹Ñ¥¹•°¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¥ÌÑ¡•É•™½É”Á±…ÕÍ¥‰±”°‰ÕÐÑ¡”…Ù…¥±…‰±”•Ù¥‘•¹”‘½•Ì¹½Ð•ÍÑ…‰±¥Í Ý¡…ÐÑ¡”Ù…±Õ”Í¥¹¥™¥•Ì¸()Q¡”½Á•¸ÅÕ•ÍÑ¥½¸¥ÌÑ¡”•á…Ð…Ñ•Ý…äÍ•µ…¹Ñ¥Ì½˜9}=9€ô€ÄÕ€¸Ù¥‘•¹”Ñ¡…Ð½Õ±É•Í½±Ù”¥Ð¥¹±Õ‘•Ì…¸…ÁÁ±¥…‰±”5å!=5}MÕ¥Ñ”‘•½‘•È½ÈÉ•Í½ÕÉ”‘•™¥¹¥Ñ¥½¸°…¸…ÕÑ¡½É¥Ñ…Ñ¥Ù”ÁÉ½Ñ½½°‘•™¥¹¥Ñ¥½¸°½È½¹ÑÉ½±±•½‰Í•ÉÙ…Ñ¥½¹Ì…É½ÍÌ…Ñ•Ý…äµ½‘•±Ì…¹™¥ÉµÝ…É”É•Ù¥Í¥½¹ÌÑ¡…Ð‘¥ÍÑ¥¹Õ¥Í ±¥Ñ•É…°½Õ¹Ð°É•Í•ÉÙ•µÙ…±Õ”°…¹…ÁÁ±¥…‰¥±¥Ñä¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¹Ì¸((ŒŒŒM•¹…É¥¼¹¥¹”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€()Q¡”ÑÝ¼M•¹…É¥½•Ù¥•Ì‘…Ñ…‰…Í•Ì…É”…Á…‰¥±¥Ñä…Ñ…±½Õ•Ì°¹½ÐÁ•ÉÍ¥ÍÑ•Í•¹…É¥¼É…Á¡Ì¸Q¡•¥È½µµ½¸Í•µ…¹Ñ¥Œ½¹Ñ•¹Ð…¹É•Ù¥Í¥½¸‘¥™™•É•¹•Ì…É”•ÍÑ…‰±¥Í¡•ì±½…°É½Ü¥‘•¹Ñ¥™¥•ÉÌ…É”¹½ÐÍÑ…‰±”…É½ÍÌÑ¡”ÑÝ¼™¥±•Ì¸()Q¡”É•µ…¥¹¥¹œÅÕ•ÍÑ¥½¹Ì…É”è((´]¡¥ M•¹…É¥½•Ù¥•Ì½Áä‘½•Ì5å!=5MÕ¥Ñ”±½…°…¹Õ¹‘•ÈÝ¡…Ð¥¹ÍÑ…±±…Ñ¥½¸°ÕÁ‘…Ñ”°½ÈÉÕ¹Ñ¥µ”½¹‘¥Ñ¥½¹Ìü(´É”Ñ¡”AÉ½É…´¥±•Ì…¹AÉ½É…µ…Ñ„½Á¥•ÌÍå¹¡É½¹¥é•½Èµ¥É…Ñ•ü(´]¡•É”…É”ÕÍ•Èµ…ÕÑ¡½É•Í•¹…É¥¼É…Á¡Ì…¹Ñ¡•¥È¹½‘”½É‘•É¥¹œ°‰É…¹¡•Ì°‰¥¹‘¥¹Ì°…¹•á•ÕÑ¥½¸ÍÑ…Ñ”Á•ÉÍ¥ÍÑ•ü(´!½Ü…É”™É…µ”µ…‰Í•¹ÐÑÉ¥•È…¹½¹‘¥Ñ¥½¸…Á…‰¥±¥Ñ¥•Ì½¹¹•Ñ•Ñ¼ÉÕ¹Ñ¥µ”•Ù•¹ÑÌü(´]¡…Ð…ÁÁ±¥…Ñ¥½¸•¹Õµ•É…Ñ¥½¹Ì…¹U$‰•¡…Ù¥½ÉÌ‘•™¥¹”…Ñ•½Éå±…€°]¡•É•QåÁ•€°A…É…µ•Ñ•ÈQåÁ•€°…¹=Á•É…Ñ½ÉQåÁ•€üQ¡•¥ÈÍÑ½É•Ù…±Õ”‘¥ÍÑÉ¥‰ÕÑ¥½¹Ì…¹Í•µ…¹Ñ¥Œ±ÕÍÑ•ÉÌ…É”­¹½Ý¸°‰ÕÐÑ¡•¥È•á…Ð•¹Õ´½¹ÑÉ…ÑÌ…É”¹½Ð¸(´]¡…ÐÉÕ¹Ñ¥µ”µ…Ñ¡¥¹œ‰•¡…Ù¥½ÈÕÍ•Ì=‰©•Ñ5…Ñ¡¥¹%‘€…¹½µµ…¹‘5…Ñ¡¥¹%‘€ü((ŒŒŒÁÁ±¥…Ñ¥½¸¥¹Ñ•É¹…±Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄá€()AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()=Á•¹EÕ•Éä¹ÑáÑ€•ÍÑ…‰±¥Í¡•Ì„Í•Ð½˜¹…µ•É•…‘Ì…¹Ñ¡•¥ÈÍ•±•Ñ•½±Õµ¹Ì°‰ÕÐ¥Ð¥Ì¥¹½µÁ±•Ñ”…¹‘½•Ì¹½Ð¥‘•¹Ñ¥™ä…±±•ÉÌ½ÈÉÕ¹Ñ¥µ”½¹ÑÉ½°™±½Ü¸()Q¡”É•µ…¥¹¥¹œÅÕ•ÍÑ¥½¹Ì…É”è((´]¡•¸…¹¡½Ü…É”Ñ¡”‘…Ñ…‰…Í•Ì½Á•¹•°…¡•°¥¹Ù…±¥‘…Ñ•°É•™É•Í¡•°Íå¹¡É½¹¥é•°½Èµ¥É…Ñ•ü(´]¡¥ …ÁÁ±¥…Ñ¥½¸½µÁ½¹•¹ÑÌ•á•ÕÑ”•… ÅÕ•Éä¥¸=Á•¹EÕ•Éä¹ÑáÑ€°…¹…É”…±°¹…µ•ÅÕ•É¥•ÌÕÍ•ü(´!½Ü…É”Ñ¡”Í•Á…É…Ñ•±äÍ•±•Ñ•…‘‘É•ÍÌµÉÕ±”½±Õµ¹Ì½¹ÍÕµ•üQ¡”•…É±¥•È‰¥ÑÝ¥Í”µ•áÁÉ•ÍÍ¥½¸ÅÕ•ÍÑ¥½¸Ý…Ì‰…Í•½¸…¸¥¹½ÉÉ•ÐÍ½ÕÉ”…ÑÑÉ¥‰ÕÑ¥½¸ìÍ•”Ñ¡”mI•¥ÍÑÉäM½ÕÉ”½ÉÉ•Ñ¥½¹t ¸¸½¥¹Ñ•É¹…±Ì½½Á•¹Ý•‰¹•ÐµÉ•¥ÍÑÉäµ…¹µÍÑ…Ñ”µµ…¡¥¹•Ì¹µ¥¹½µÁ±•Ñ•¹•ÍÌµÁÉ•Í•ÉÙ•µ¥¸µÑ¡”µÍ½ÕÉ”¤¸(´]¡¥ É•Í½ÕÉ•Ì…¹…ÁÁ±¥…Ñ¥½¸½µÁ½¹•¹ÑÌÉ•Í½±Ù”ÍÑ½É•±½…±¥é…Ñ¥½¸­•åÌü(´]¡…Ð±½…±”µÍ•±•Ñ¥½¸°™…±±‰…¬°µ¥ÍÍ¥¹œµ­•ä°…¹½µÁ½Í•µ±…‰•°ÉÕ±•Ì…É”…ÁÁ±¥•ü((ŒŒŒÙ¥‘•¹”ÁÉ¥½É¥Ñ¥•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÄéÌÀÀÀÀÄå€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€°É•Ù¥Í¥½¹€°Ù•ÉÍ¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè‘…Ñ…‰…Í•€()Q¡”¡¥¡•ÍÐµÙ…±Õ”¹•áÐ½‰Í•ÉÙ…Ñ¥½¹Ì…É”è((Ä¸É•½Ù•ÈÑ¡”…¹½¹¥…°ÁÉ½Ù•¹…¹”™½È±…ÍÍ¥Œ]!<€ÄÌ%59M%=8€ÈÁ€…¹½‰Ñ…¥¸„‘¥ÍÉ¥µ¥¹…Ñ¥¹œ%59M%=8€ÐÁ€½‰Í•ÉÙ…Ñ¥½¸…É½ÍÌ„‘¥™™•É•¹Ð…Ñ•Ý…ä½È™¥ÉµÝ…É”É•Ù¥Í¥½¸ì(È¸½¹”ÍÕ•ÍÍ™Õ°¹½¸µ1¥¡Ñ¥¹œ%59M%=8€ÌÉ€É•ÍÁ½¹Í”Ý¡½Í”…¹‘¥‘…Ñ”MeM€Ù…±Õ•Ì‘¥™™•Èì(Ì¸½¹ÑÉ½±±•%59M%=8€Ñ€…¹€Õ€…ÁÑÕÉ•Ì…É½ÍÌ­¹½Ý¸Á¡åÍ¥…°½¹™¥ÕÉ…Ñ½È¡…¹•Ìì(Ð¸„½¹ÑÉ½±±••Ù¥”½¥Ñ•´…Í”•á•É¥Í¥¹œ½¹É•Ñ”°Ý¥±‘…É‘•°µÕ±Ñ¥Á±”°½Èµ¥ÍÍ¥¹œ™¥ÉµÝ…É”‰Õ¥±É•½É‘Ìì(Ô¸™¥±”µ…•ÍÌ°‘…Ñ…‰…Í”µÍÑ…Ñ•µ•¹Ð°…¹Í…Ù”µ½Á•É…Ñ¥½¸ÑÉ…•ÌÝ¡¥±”É•…Ñ¥¹œ½¹”µ¥¹¥µ…°Í•¹…É¥¼ì(Ø¸„ÉÕ¹Ñ¥µ”ÑÉ…”½˜…‘‘É•ÍÌµÉÕ±”Í•±•Ñ¥½¸™½È„ÍåÍÑ•´Ý¥Ñ ‰½Ñ •¹•É…°…¹™…µ¥±äµÅÕ…±¥™¥•ÉÕ±•Ìì(Ü¸¡…É‘Ý…É”…¹µ¥É½½¹ÑÉ½±±•ÈÙ•ÉÍ¥½¸½‰Í•ÉÙ…Ñ¥½¹Ì…É½ÍÌ­¹½Ý¸É•Ù¥Í¥½¹Ì½˜Ñ¡”Í…µ”ÁÉ½‘ÕÐ¸()… É•ÍÕ±ÐÍ¡½Õ±ÕÁ‘…Ñ”Ñ¡”mI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Ét¡É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ¤…¹Ñ¡•¸Ñ¡”…ÁÁÉ½ÁÉ¥…Ñ”É•™•É•¹”Í•Ñ¥½¸¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÈÈ()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½É•©•Ñ•µÉ•±…Ñ¥½¹Í¡¥ÁÌ¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒI•©•Ñ•I•±…Ñ¥½¹Í¡¥ÁÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÈéÌÀÀÀÀÀÅ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè…ÁÁ±¥•ÌÑ½€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()I•©•Ñ•¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¹Ì…É”É•Ñ…¥¹•‰•…ÕÍ”Ñ¡•ä…É”Á±…ÕÍ¥‰±”•¹½Õ Ñ¼‰”É•‘¥Í½Ù•É•™É½´¹…µ•Ì°•ÅÕ…°¥¹Ñ••ÉÌ°½È¥¹½µÁ±•Ñ”…ÁÑÕÉ•Ì¸… •¹ÑÉäÉ•½É‘ÌÝ¡äÑ¡”Í¡½ÉÑÕÐ™…¥±Ì…¹Ñ¡”Í…™•ÈÉ•Á±…•µ•¹Ð¸(+ŠqI•©•Ñ•“Št…ÁÁ±¥•ÌÑ¼Ñ¡”ÍÑ…Ñ•Õ¹½¹‘¥Ñ¥½¹…°¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¸¹…ÉÉ½Ý•ÈÉ•±…Ñ¥½¹Í¡¥À…¸‰”É•½¹Í¥‘•É•Ý¡•¸¹•Ü•Ù¥‘•¹”…‘‘É•ÍÍ•ÌÑ¡”É•©•Ñ¥¹œ•Ù¥‘•¹”¸((ŒŒŒ…Ñ…‰…Í”¥‘•¹Ñ¥Ñä…¹­•äµ¥ÍÑ…­•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÈéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€()ðI•©•Ñ•¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸ð½¹™±¥Ñ¥¹œ•Ù¥‘•¹”ðM…™”ÑÉ•…Ñµ•¹Ðð)ð€´´´ð€´´´ð€´´´ð)ð9}Y%¹½‘”ƒŠH9}19U¹½‘•€ð•Ù¥”½‘•€½¹Ñ…¥¹ÌÁÉ½‘ÕÐ½‘•Ì½M-UÌì¥‘•¹Ñ¥…°½±Õµ¸¹…µ•Ì¡…Ù”Õ¹É•±…Ñ•É½±•ÌðÑÉ•…Ð9}Y%¹½‘•€…ÌÁÉ½‘ÕÐ¥‘•¹Ñ¥Ñä…¹É•Í½±Ù”±…¹Õ…”Ñ¡É½Õ …ÑÕ…°±½…±¥é…Ñ¥½¸ÍÑÉÕÑÕÉ•Ìð)ð5!…Ñ…±½Õ”¹9}MeMQ4¹¥‘}ÍåÍÑ•´€ô=A8¹9}MeMQ4¹¥‘}ÍåÍÑ•µ€ð¥¹‘•Á•¹‘•¹ÐÉ•¥ÍÑÉ¥•ÌÍ¡½Ü½¹±äÁ…ÉÑ¥…°¹Õµ•É¥Œ½¥¹¥‘•¹”ð½ÉÉ•±…Ñ”ÍåÍÑ•µÌÑ¡É½Õ µ•…¹¥¹œ°•áÑ•É¹…°™¥•±‘Ì°™Õ¹Ñ¥½¹…°½‘¥…¹½ÍÑ¥Œ™…µ¥±¥•Ì°…¹=‰©•Ðµ•µ‰•ÉÍ¡¥Àð)ð‘¥…¹½ÍÑ¥Œ•Ù¥”%€ô9}Y%¹¥‘}‘•Ù¥•€ðÝ¥É”%¥Ì…¸¥¹ÍÑ…±±•€ÌÈµ‰¥Ð¥¹ÍÑ…¹”¥‘•¹Ñ¥™¥•Èì…Ñ…±½Õ”­•ä¥‘•¹Ñ¥™¥•Ì„ÁÉ½‘ÕÐÉ½ÜðÉ•Ñ…¥¸‰½Ñ ¥‘•¹Ñ¥™¥•ÉÌ…¹½ÉÉ•±…Ñ”Ñ¡É½Õ %59M%=8€Å€Í•µ…¹Ñ¥Ìð)ð‘¥…¹½ÍÑ¥ŒM1=P€ô9}M1=QL¹¥‘}Í±½Ñ€ðÝ¥É”Í±½Ð¥Ì•Ù¥”µ±½…°ì¥‘}Í±½Ñ€¥Ì…¸…ÍÍ½¥…Ñ¥½¸µÉ½Ü­•äð½ÉÉ•±…Ñ”Ý¥Ñ 9}M1=QL¹™¥ÉÍÑ}Í±½Ñ€…™Ñ•È™¥ÉµÝ…É”É•Í½±ÕÑ¥½¸ð)ð9}-e}=	)P¹¥‘}­•å}½‰©•Ð€ô9}-e}=	)P¹­•å}½‰©•Ñ€ð¥¹Ñ•É¹…°…¹•áÑ•É¹…°¥‘•¹Ñ¥™¥•ÉÌ…É”‘¥ÍÑ¥¹Ð½±Õµ¹Ì…¹¹½Ð•¹•É…±±ä•ÅÕ…°ð±…‰•°‰½Ñ ¹…µ•ÍÁ…•Ì•áÁ±¥¥Ñ±äð)ð½¹”9}%Q5€¥‘•¹Ñ¥™¥•Ì½¹”M-TðÍ•Ù•É…°‰É…¹‘••Ù¥”É•½É‘Ì…¸Í¡…É”½¹”¥Ñ•´ðÉ•ÑÕÉ¸Ñ¡”…¹‘¥‘…Ñ”•Ù¥”½M-TÍ•ÐÕ¹Ñ¥°‰É…¹°±¥¹”°½È•áÑ•É¹…°•Ù¥‘•¹”¹…ÉÉ½ÝÌ¥Ðð)ð½¹”9}%I5]I€É½Ü¡…Ì•á…Ñ±ä½¹”9}	U%1M€É½Üð€Ää™¥ÉµÝ…É”‘•™¥¹¥Ñ¥½¹Ì¡…Ù”¹¼‰Õ¥±É½Ü…¹€ÄÔ¡…Ù”µÕ±Ñ¥Á±”‰Õ¥±É½ÝÌðµ½‘•°™¥ÉµÝ…É”µÑ¼µ‰Õ¥±…Ìé•É¼µÑ¼µµ…¹äð)ð¹¼‰Õ¥±É½Üµ•…¹Ì™¥ÉµÝ…É•}ˆ€ô€´Å€ð…‰Í•¹”…¹•áÁ±¥¥ÐÍ•¹Ñ¥¹•°…É”ÍÑÉÕÑÕÉ…±±ä‘¥™™•É•¹ÐÍÑ…Ñ•ÌðÁÉ•Í•ÉÙ”‰½Ñ …Í•Ì¥¹‘•Á•¹‘•¹Ñ±äð)ð•Ù•Éä¹•…Ñ¥Ù”¥¹Ñ••È¥Ì…¸½ÉÁ¡…¸ð€´Å€¥ÌÍÑÉ½¹±ä½ÉÉ½‰½É…Ñ•…Ì…¹ä½Õ¹ÍÁ•¥™¥•¥¸™¥ÉµÝ…É”½µÁ½¹•¹ÑÌð‘•Ñ•Éµ¥¹”Í•¹Ñ¥¹•°Í•µ…¹Ñ¥ÌÁ•È½±Õµ¸‰•™½É”½ÉÁ¡…¸…¹…±åÍ¥Ìð((ŒŒŒ…Á…‰¥±¥Ñä…¹5½‘Õ±”µ¥ÍÑ…­•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÈéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()ðI•©•Ñ•¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸ð½¹™±¥Ñ¥¹œ•Ù¥‘•¹”ðM…™”ÑÉ•…Ñµ•¹Ðð)ð€´´´ð€´´´ð€´´´ð)ð9}%I5]I¹Í±½ÑÌ€ô=U9P¡9}M1=QLÉ½ÝÌ¥€ð½¹”Í±½Ñ€…¸½™™•ÈÍ•Ù•É…°=‰©•Ð…±Ñ•É¹…Ñ¥Ù•Ìð½Õ¹Ð‘¥ÍÑ¥¹Ð™¥ÉÍÑ}Í±½Ñ€Á½Í¥Ñ¥½¹Ì…¹¥¹Ñ•ÉÁÉ•Ð…±Ñ•É¹…Ñ¥Ù•ÌÍ•Á…É…Ñ•±äð)ð…¸9}M1=QM€É½Ü¥Ì½¹”ÉÕ¹Ñ¥µ”5½‘Õ±”ðÉ½ÝÌÉ•ÁÉ•Í•¹Ð™¥ÉµÝ…É”½=‰©•ÐÁ±…•µ•¹Ð…±Ñ•É¹…Ñ¥Ù•Ìð‰Õ¥±ÉÕ¹Ñ¥µ”5½‘Õ±•Ì™É½´%59M%=8€ÌÁ€°Ñ¡•¸Ù…±¥‘…Ñ”……¥¹ÍÐÁ±…•µ•¹Ð…Á…‰¥±¥Ñäð)ð™¥á•‘}­¼€ô€Å€…±½¹”ÁÉ½Ù•ÌÑ¡”U$™¥•±¥ÌÉ•…µ½¹±äðÙ¥Í¥‰¥±¥Ñä°½¹‘¥Ñ¥½¹Ì°ÁÉ½‘ÕÐ½¹Ñ•áÐ°…¹U$‰•¡…Ù¥½È…±Í¼½¹ÑÉ¥‰ÕÑ”ðÕÍ”™¥á•‘}­½€…Ì‘•Í¥¹…Ñ•½™¥á•…Á…‰¥±¥Ñä•Ù¥‘•¹”°¹½Ð„½µÁ±•Ñ”U$ÉÕ±”ð)ð„Y¥É¥¸=‰©•Ð¥ÌÑ¡”É•Õ±…È½¹™¥ÕÉ•=‰©•ÐðY¥É¥¸=‰©•ÑÌ‘•ÍÉ¥‰”½¹™¥ÕÉ…‰±”Ñ•µÁ±…Ñ•Ì…¹Á•Éµ¥ÑÑ•=‰©•ÐÍ•ÑÌì%59M%=8€ÌÁ€É•Á½ÉÑÌÑ¡”Y¥É¥¸=‰©•ÐÝ¡¥±”Ñ¡”5½‘Õ±”¥Ì‘¥Í…‰±•ðÕÍ”%59M%=8€ÌÀ¹MQQ€Ñ¼Í•±•ÐÑ¡”¹…µ•ÍÁ…”ð)ð•Ù•Éä=‰©•Ð…±±½Ý•‰ä„Y¥É¥¸=‰©•Ð¥ÌÍ¥µÕ±Ñ…¹•½ÕÍ±ä…Ñ¥Ù”ð…ÍÍ½¥…Ñ¥½¸¥Ì…Á…‰¥±¥Ñä°¹½ÐÉÕ¹Ñ¥µ”Í•±•Ñ¥½¸ðÉ•Í½±Ù”½¹”É•Á½ÉÑ•½¹™¥ÕÉ•=‰©•ÐÁ•È5½‘Õ±”ÍÑ…Ñ”ð((ŒŒŒAÉ½Ñ½½°¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸µ¥ÍÑ…­•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÈéÌÀÀÀÀÀÑ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€°½¹±ä™½É€°Ù•ÉÍ¥½¹€)U¹•ÉÑ…¥¹Ñäè½¹ÑÉ…‘¥Ñ€°Õ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°…Ñ…±½Õ•€°•Ù¥‘•¹•€()ðI•©•Ñ•¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸ð½¹™±¥Ñ¥¹œ•Ù¥‘•¹”ðM…™”ÑÉ•…Ñµ•¹Ðð)ð€´´´ð€´´´ð€´´´ð)ð%59M%=8€Ä¹9}=9€¥Ì…¸=‰©•Ð°±…ÍÌ°½È™½É´™…Ñ½Èð½É‘¥¹…Éä…‘‘É•ÍÍ•µ™½É´=A8¹‘‰€µ•Ñ…‘…Ñ„°ÁÉ½‘ÕÐ‘¥…É…µÌ°…¹…ÁÑÕÉ•Ì¥‘•¹Ñ¥™ä„Á¡åÍ¥…°µ½¹™¥ÕÉ…Ñ½ÈµÁ½Í¥Ñ¥½¸½Õ¹ÐìÑ¡”…Ñ•Ý…äÙ…É¥…¹Ð¥¹ÍÑ•…¡…ÌÕ¹É•Í½±Ù•Í•µ…¹Ñ¥ÌðÉ•Ñ…¥¸Ñ¡”Á¡åÍ¥…°µÁ½Í¥Ñ¥½¸¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸½¹±ä™½ÈÑ¡”½ÉÉ½‰½É…Ñ•½É‘¥¹…Éä…‘‘É•ÍÍ•™½É´ìÁÉ•Í•ÉÙ”…Ñ•Ý…ä9}=9€É…Ü…¹Õ¹É•Í½±Ù•ð)ð%59M%=8€ÌÀ¹-e=€…±Ý…åÌ¹…µ•Ì9}-e}=	)P¹­•å}½‰©•Ñ€ð‘¥Í…‰±•5½‘Õ±•Ì€¡MQQ€ô€Å€¤ÕÍ”Ñ¡”Y¥É¥¸=‰©•Ð¹…µ•ÍÁ…”ð‰É…¹ ½¸MQQ€‰•™½É”±½½­ÕÀð)ð%59M%=8€ÌÈ¹MeM€¥Ì…ÕÑ½µ…Ñ¥…±±ä„™Õ¹Ñ¥½¹…°]!=€ðÍåÍÑ•´É½ÕÁ¥¹œ…¹¹½¸µ1¥¡Ñ¥¹œ…¹‘¥‘…Ñ”Ù…±Õ•Ì‘¥™™•ÈðÉ•Ñ…¥¸ÍåÍ}µ½‘½‰©€…ÌÑ¡”±•…‘¥¹œ¥¹™•É•¹”Á•¹‘¥¹œ„‘¥ÍÉ¥µ¥¹…Ñ¥¹œ…ÁÑÕÉ”ð)ð‘¥…¹½ÍÑ¥Œ½ÕÑ•È]!I€…±Ý…åÌ•ÅÕ…±ÌÍ±½Ð€Å€…‘‘É•ÍÌð½¹±äÍ•±•Ñ•±…å½ÕÑÌ¡…Ù”‰••¸½‰Í•ÉÙ•ì‘¥Í…‰±•½…±Ñ•É¹…Ñ”±…å½ÕÑÌ…É”Õ¹Ñ•ÍÑ•ðÑÉ•…ÐÑ¡”½ÉÉ•±…Ñ¥½¸…ÌÍÑÉ½¹œ‰ÕÐ½¹‘¥Ñ¥½¹…°ð)ð•Ù•Éä5½‘Õ±”É•ÑÕÉ¹Ì%59M%=8€ÌÉ€ð½µµ…¹µ½¹±ä…¹½ÁÑ¥½¹…°µÉ•ÍÁ½¹Í”½‰Í•ÉÙ…Ñ¥½¹Ì½¹ÑÉ…‘¥ÐÕ¹¥Ù•ÉÍ…±¥Ñäðµ½‘•°…‘‘É•ÍÌÉ•ÍÁ½¹Í”…Ì=‰©•Ð½™¥ÉµÝ…É”‘•Á•¹‘•¹Ðð)ð…ÑÕ…Ñ½ÉÌÕÍ”½¹±ä%59M%=8€ÌÉ€ì½µµ…¹‘ÌÕÍ”½¹±ä€ÌÕ€ð„5½‘Õ±”…¸•áÁ½Í”…‘‘É•ÍÌ°¥¹‘•á•ÁÉ½Á•ÉÑ¥•Ì°‰½Ñ °½È¹•¥Ñ¡•Èð‘•Ñ•Éµ¥¹”…Ù…¥±…‰¥±¥Ñä™É½´=‰©•Ð½™¥ÉµÝ…É”‰•¡…Ù¥½Èð)ð%59M%=8€ÌÄÁ€¥Ì…¸½É‘¥¹…Éä9}=9¹¥‘á€É•½Éð™É…µ”¡…Ì¹¼¥¹‘•à…¹±…­Ì•¹•É¥ŒÁ…É…µ•Ñ•Èµ•Ñ…‘…Ñ„ð‘•½‘”Á•È=‰©•Ð½•Ù¥”™…µ¥±äð)ðm]}YIM%=9u€°m!]}YIM%=9u€°½Èm5%I=}YIM%=9u€¥Ì½¹”Í…±…ÈðÁ…É…µ•Ñ•È‘•ÍÉ¥ÁÑ¥½¹Ì‘•™¥¹”Y•ÉÍ¥½¸©I•±•…Í”©	Õ¥±‘€ðÁÉ•Í•ÉÙ”Ñ¡É•”½µÁ½¹•¹ÑÌ…¹Ñ¡•¥ÈÍ•Á…É…Ñ½ÉÌð)ð¡…É‘Ý…É”½Èµ¥É¼Ù•ÉÍ¥½¸µ…ÁÌÑ¼9}A-€½9}%1€Ù•ÉÍ¥½¸™¥•±‘ÌðÑ¡½Í”É½ÝÌ‘•ÍÉ¥‰”…ÍÍ½¥…Ñ•Á…­…•Ì½™¥±•Ìì¹¼¡…É‘Ý…É”½µ¥É¼…Ñ…±½Õ”™¥•±•á¥ÍÑÌðÉ•Ñ…¥¸%59M%=8€Í€½€Ù€…Ì¥¹ÍÑ…±±•µÍÑ…Ñ”•Ù¥‘•¹”ð)ð%59M%=8€Ñ€½€Õ€Ù…±Õ•Ì…É”ÁÉ½Ù•¸ÁÉ•Í•¹”‰¥ÑÌð¹¼½¹ÑÉ½±±•Á½Í¥Ñ¥½¸½Ù…±Õ”µ…ÑÉ¥à•ÍÑ…‰±¥Í¡•ÌÑ¡”•¹½‘¥¹œð­••À½¹Ñ•¹ÑÌ½ÁÉ•Í•¹”½½µ‰¥¹•…±Ñ•É¹…Ñ¥Ù•Ì½Á•¸ð)ð…¸-€ÁÉ½Ù•Ì•™™•Ñ¥Ù”½¹™¥ÕÉ…Ñ¥½¸ð…­¹½Ý±•‘•µ•¹Ð°…•ÁÑ•ÑÉ…¹Í™•È°Á•ÉÍ¥ÍÑ•¹”°…¹É•…µ‰…¬…É”‘¥ÍÑ¥¹ÐðÙ•É¥™äÑ•Éµ¥¹…°ÍÑ…Ñ”…¹‘¥…¹½ÍÑ¥ŒÉ•…µ‰…¬ð((ŒŒŒ½¹™¥ÕÉ…Ñ¥½¸…¹Ù…±¥‘…Ñ¥½¸Í¡½ÉÑÕÑÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÈéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€()ðI•©•Ñ•Í¡½ÉÑÕÐð]¡äÕ¹Í…™”ðM…™”ÑÉ•…Ñµ•¹Ðð)ð€´´´ð€´´´ð€´´´ð)ðÙ…±¥‘…Ñ”½¹±ä……¥¹ÍÐ=A8¹‘‰€É…¹”ðÑÉ…¹ÍÁ½ÉÐ…Á…¥Ñä…¸•á••…Ñ…±½Õ”…Á…‰¥±¥Ñäð…ÁÁ±äÁÉ½Á•ÉÑäÉ…¹”°½¹Ñ•áÑÕ…°™¥±Ñ•ÉÌ°½¹‘¥Ñ¥½¹Ì°½¹Ù•ÉÍ¥½¹Ì°…¹±¥¹­•ÉÕ±•Ìð)ðÑÉ•…Ð¥‘}­•å}½‰©•Ð€ô€Á€½È¥‘}™¥ÉµÝ…É”€ô€Á€…Ì„‰É½­•¸É•™•É•¹”ðé•É¼Í•±•ÑÌÑ¡”½µÁ±•µ•¹Ñ…Éä9}=9€½Ý¹•ÉÍ¡¥À‰É…¹ ðÙ…±¥‘…Ñ”Ñ¡”•á±ÕÍ¥Ù”½Ý¹•ÉÍ¡¥ÀÁ…ÑÑ•É¸ð)ðÕÍ”„±½‰…°9}=9¹¥‘á€±½½­ÕÀðÑ¡”Í…µ”¥¹‘•à…¸¹…µ”‘¥™™•É•¹ÐÁÉ½Á•ÉÑ¥•Ì…É½ÍÌ=‰©•Ð½™¥ÉµÝ…É”½¹Ñ•áÑÌðÉ•Í½±Ù”•Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°=‰©•Ð°…¹½Ý¹•ÉÍ¡¥À™¥ÉÍÐð)ðÕÍ”%59M%=8€ÌÔ¹%9a€Ý¥Ñ¡½ÕÐÍ±½Ñ€ðÉ•Á•…Ñ•¥¹‘•á•Ì…¸½ÕÈ…É½ÍÌ5½‘Õ±•Ìð¥¹±Õ‘”•Ù¥”…¹Í±½Ð¥¸Ñ¡”½ÉÉ•±…Ñ¥½¸­•äð)ðÑÉ•…Ð„Ù¥Í¥‰±”U$™¥•±…ÌÝÉ¥Ñ…‰±”ðÙ¥Í¥‰¥±¥Ñä°•‘¥Ñ…‰¥±¥Ñä°™¥á•ÍÑ…Ñ”°…¹½¹‘¥Ñ¥½¹Ì‘¥™™•Èð½ÉÉ½‰½É…Ñ”Ý¥Ñ µ•Ñ…‘…Ñ„…¹½‰Í•ÉÙ•U$‰•¡…Ù¥½Èð)ð‰…Í”É…¹”…±½¹”‘•™¥¹•Ì…±°±•…°Ù…±Õ•Ìð9}%1QI€°™¥±Ñ•É•É…¹•Ì°½¹‘¥Ñ¥½¹Ì°…¹½Ñ¡•ÈµÁÉ½Á•ÉÑäÉÕ±•Ì¹…ÉÉ½Ü¥Ðð•Ù…±Õ…Ñ”Ñ¡”½µÁ±•Ñ”Ù…±¥‘…Ñ¥½¸ÍÑ…¬ð)ðÁ¡åÍ¥…°½Õ¹Ñ•ÉÁ…ÉÐÁÉ½Ù•Ì…Ñ¥Ù”Á¡åÍ¥…°½¹™¥ÕÉ…Ñ¥½¸ð‘¥…¹½ÍÑ¥ÌÉ•Á½ÉÑÌ•™™•Ñ¥Ù”½¹™¥ÕÉ…Ñ¥½¸°¹½Ð¹••ÍÍ…É¥±ä¡½Ü¥ÐÝ…ÌÍ•Ðð‘¥ÍÑ¥¹Õ¥Í Á¡åÍ¥…°…Á…‰¥±¥Ñä™É½´…Ñ¥Ù”µ•Ñ¡½ð)ðÍ…µ”•™™•Ñ¥Ù”Á¡åÍ¥…°…¹Y¥ÉÑÕ…°Ù…±Õ”ÁÉ½Ù•Ì¥‘•¹Ñ¥…°ÍÑ½É…”ð½¹Ù•ÉÍ¥½¸µ…äÁÉ½‘Õ”Ñ¡”Í…µ”ÉÕ¹Ñ¥µ”É•ÍÕ±Ðð±…ÍÍ¥™ä‘¥É•ÐÙ•ÉÍÕÌ½¹Ù•ÉÑ•µ…ÁÁ¥¹œÑ¡É½Õ ½¹ÑÉ½±±•¡…¹•Ìð((ŒŒŒÉ½ÍÌµ‘…Ñ…‰…Í”…¹M•¹…É¥½•Ù¥•Ìµ¥ÍÑ…­•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÈéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€()ðI•©•Ñ•¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸ð½¹™±¥Ñ¥¹œ•Ù¥‘•¹”ðM…™”ÑÉ•…Ñµ•¹Ðð)ð€´´´ð€´´´ð€´´´ð)ð•ÅÕ…°±½…°ÁÉ¥µ…Éä­•åÌ…É½ÍÌ‘…Ñ…‰…Í•Ì¥‘•¹Ñ¥™äÑ¡”Í…µ”½¹•ÁÐð‘…Ñ…‰…Í•Ì¡…Ù”¥¹‘•Á•¹‘•¹Ð¹…µ•ÍÁ…•Ìð½¹¹•Ð•áÑ•É¹…°¥‘•¹Ñ¥™¥•ÉÌ½ÈÍ•µ…¹Ñ¥ŒÁ…Ñ¡Ì½¹±äð)ðM•¹…É¥½•Ù¥•Ì=‰©•Ñ%€ô9}-e}=	)P¹­•å}½‰©•Ñ€ð¹¼‘•±…É•½È½µÁ±•Ñ”Í•µ…¹Ñ¥Œµ…ÁÁ¥¹œìµ½‘•±ÌÍ•ÉÙ”‘¥™™•É•¹ÐÁÕÉÁ½Í•Ìð½ÉÉ•±…Ñ”Ñ¡É½Õ ±¥Ñ•É…°™É…µ•Ì…¹™Õ¹Ñ¥½¹…°Í•µ…¹Ñ¥Ìð)ðM•¹…É¥½•Ù¥•Ì…µ¥±å%€ô™Õ¹Ñ¥½¹…°]!=€ðÙ…±Õ•Ì…É”±½…°•‘¥Ñ½ÈÉ½ÕÁ¥¹Ì…¹‘¼¹½Ð•¹½‘”]!=€ð‘•É¥Ù”]!=€™É½´±¥Ñ•É…°™É…µ•Ì½¡¥=Á•¹€Ý¡•É”ÁÉ•Í•¹Ðð)ðM•¹…É¥½•Ù¥•ÌAÉ½É…µ…Ñ„…¹AÉ½É…´¥±•ÌÉ½ÝÌ…±¥¸‰ä%‘€ð…‘‘•É½ÝÌ…ÕÍ”±½…°%ÌÑ¼‘¥Ù•É”ð½µÁ…É”Ñ¡”½µÁ±•Ñ”Í•µ…¹Ñ¥Œ¡¥•É…É¡ä…¹¹½¸µ±½…°™¥•±‘Ìð)ðAÉ½É…µ…Ñ„¥Ì…ÕÑ½µ…Ñ¥…±±ä…ÕÑ¡½É¥Ñ…Ñ¥Ù”‰•…ÕÍ”¥Ð¥ÌÝÉ¥Ñ…‰±”ðÉ•Ù¥Í¥½¸‘•±Ñ„‘½•Ì¹½ÐÁÉ½Ù”ÉÕ¹Ñ¥µ”ÁÉ••‘•¹”ðÑÉ…”™¥±”½Á•¹Ì°Íå¹¡É½¹¥é…Ñ¥½¸°½È±½…‘•È‰•¡…Ù¥½Èð)ðÉ…µ”%L9U11€µ•…¹ÌÑ¡”Í•¹…É¥¼…Á…‰¥±¥Ñä¥ÌÕ¹ÍÕÁÁ½ÉÑ•ðµ½ÍÐ•Ù•¹ÑÌ½½¹‘¥Ñ¥½¹Ì‘•Á•¹½¸ÉÕ¹Ñ¥µ”µ…ÁÁ¥¹Ì…‰Í•¹Ð™É½´Ñ¡”…Á…‰¥±¥ÑäÉ½ÜðÁÉ•Í•ÉÙ”Ñ¡”…Á…‰¥±¥Ñä…¹µ…É¬Ñ¡”ÉÕ¹Ñ¥µ”µ…Ñ¡•ÈÕ¹É•Í½±Ù•ð)ðÍåµ‰½±¥Œ™É…µ”Ñ•áÐ¥Ì±¥Ñ•É…°=Á•¹]•‰9•ÐðÍ•Ù•É…°ÍÑ½É•ÍÑÉ¥¹Ì…É”…ÁÁ±¥…Ñ¥½¸Ñ½­•¹Ìð±…ÍÍ¥™ä±¥Ñ•É…°°Íåµ‰½±¥Œ°…¹…‰Í•¹ÐÑ•µÁ±…Ñ•Ì‰•™½É”É•¹‘•É¥¹œð)ðM•¹…É¥½•Ù¥•Ì½¹Ñ…¥¹ÌÍ…Ù•Í•¹…É¥¼É…Á¡ÌðÍ¡•µ„±…­Ì¥¹ÍÑ…¹•Ì°•‘•Ì°½É‘•É¥¹œ°…¹•á•ÕÑ¥½¸ÍÑ…Ñ”ð±½…Ñ”Ñ¡”Í•Á…É…Ñ”Á•ÉÍ¥ÍÑ•¹”±…å•Èð((ŒŒŒÙ¥‘•¹”…¹É•…Í½¹¥¹œ™…¥±ÕÉ•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÈéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)U¹•ÉÑ…¥¹Ñäèµ…å€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€°ÍÁ•¥™¥…Ñ¥½¹€()ð…¥±ÕÉ”ð]¡ä¥Ð™…¥±Ìð½ÉÉ•Ñ¥½¸ð)ð€´´´ð€´´´ð€´´´ð)ð™¥ÉÍÐµ…Ñ¡¥¹œÉ½ÜÁÉ½Ù•ÌÑ¡”É•±…Ñ¥½¹Í¡¥Àð•á•ÁÑ¥½¹Ì…¹‘ÕÁ±¥…Ñ”¹…µ•ÍÁ…•ÌÉ•µ…¥¸¥¹Ù¥Í¥‰±”ðÑ•ÍÐ•Ù•ÉäÁ½ÁÕ±…Ñ•Ù…±Õ”…¹É•Á½ÉÐ½ÉÁ¡…¹Ì½…É‘¥¹…±¥Ñäð)ðÑÝ¼µ…Ñ¡¥¹œÑ…‰±•Ì…É”¥¹‘•Á•¹‘•¹Ð½ÉÉ½‰½É…Ñ¥½¸ð‰½Ñ µ…ä‰”•¹•É…Ñ•™É½´½¹”¥¹Ñ•É¹…°µ½‘•°ðÍ••¬„…ÁÑÕÉ”°U$½‰Í•ÉÙ…Ñ¥½¸°ÁÉ½‘ÕÐ‘½Õµ•¹Ð°½ÈÍÁ•¥™¥…Ñ¥½¸ð)ðÍ¥±•¹”ÁÉ½Ù•ÌÕ¹ÍÕÁÁ½ÉÑ•‰•¡…Ù¥½ÈðÍ•±•Ñ½È°ÍÑ…Ñ”°Ñ¥µ•½ÕÐ°½ÈÑÉ…¹ÍÁ½ÉÐµ…ä‰”ÝÉ½¹œðÉ•½É½‰Í•ÉÙ…Ñ¥½¸…Á…‰¥±¥Ñä…¹Ñ•Éµ¥¹…°•Ù¥‘•¹”ð)ð„‘…Ñ…‰…Í”±…‰•°¥Ì„Õ¹¥Ù•ÉÍ…°ÁÉ½Ñ½½°‘•™¥¹¥Ñ¥½¸ð±…‰•±Ì‘•ÍÉ¥‰”½¹”¥µÁ±•µ•¹Ñ…Ñ¥½¸…¹µ…ä‰”¥¹½µÁ±•Ñ”ðÍ•Á…É…Ñ”ÍÑ½É•¥µÁ±•µ•¹Ñ…Ñ¥½¸Í•µ…¹Ñ¥Ì™É½´ÁÉ½Ñ½½°Õ…É…¹Ñ••Ìð)ð½¹”•Ù¥”…ÁÑÕÉ”‘•™¥¹•Ì„™…µ¥±äÉÕ±”ðÍÕÁÁ½ÉÐ…¹½ÁÑ¥½¹…±¥ÑäÙ…Éä‰ä™¥ÉµÝ…É”½=‰©•ÐðÍ½Á”Ñ¡”½‰Í•ÉÙ…Ñ¥½¸…¹Í••¬½¹ÑÉ…ÍÑ¥¹œÁÉ½‘ÕÑÌð)ð½ÉÉ•Ñ¥¹œ„…¹½¹¥…°‘…Ñ…‰…Í”¥µÁÉ½Ù•ÌÑ¡”•Ù¥‘•¹”ðµÕÑ…Ñ¥½¸‘•ÍÑÉ½åÌÍ½ÕÉ”™¥‘•±¥Ñä…¹µ…ä•¹½‘”™…±Í”½¹ÍÑÉ…¥¹ÑÌð•¹•É…Ñ”„Í•Á…É…Ñ”‘•É¥Ù•…ÉÑ¥™…ÐÝ¥Ñ „É•ÁÉ½‘Õ¥‰±”ÑÉ…¹Í™½Éµ…Ñ¥½¸ð((ŒŒŒI•½¹Í¥‘•É…Ñ¥½¸ÉÕ±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÈéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)…ÕÑ¥½¹Ìè‘¼¹½Ñ€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()É•©•Ñ•É•±…Ñ¥½¹Í¡¥À…¸‰”É•½Á•¹•½¹±äÝ¡•¸¹•Ü•Ù¥‘•¹”‘¥É•Ñ±ä…‘‘É•ÍÍ•Ì¥ÑÌÉ•©•Ñ¥¹œ•Ù¥‘•¹”¸()Q¡”¹•Ü±…¥´É•½ÉµÕÍÐ¥¹±Õ‘”è((Ä¸Ñ¡”•á…ÐÉ•©•Ñ•¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸‰•¥¹œ¹…ÉÉ½Ý•½ÈÉ•Á±…•ì(È¸Ñ¡”¹•ÜÍ½ÕÉ”…¹É•Ù¥Í¥½¸ì(Ì¸½µÁ±•Ñ”½Ù•É…”…¹•á•ÁÑ¥½¹Ìì(Ð¸Ñ¡”½¹‘¥Ñ¥½¸Ñ¡…Ðµ…­•ÌÑ¡”É•Ù¥Í•É•±…Ñ¥½¹Í¡¥ÀÙ…±¥ì(Ô¸„™…±Í¥™¥•Èì(Ø¸ÕÁ‘…Ñ•ÌÑ¼Ñ¡”É•™•É•¹”Á…”°mI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•Ét¡É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ¤°…¹m=Á•¸EÕ•ÍÑ¥½¹Ít¡½Á•¸µÅÕ•ÍÑ¥½¹Ì¹µ¤¸()¼¹½ÐÍ¥±•¹Ñ±ä‘•±•Ñ”„É•©•Ñ¥½¸¸AÉ•Í•ÉÙ”Ý¡äÑ¡”•…É±¥•ÈÕ¹½¹‘¥Ñ¥½¹…°±…¥´™…¥±•¸((Œ½Õµ•¹Ðè½Ý¹­ˆé‘½Õµ•¹ÐéÀÀÀÄÈÌ()M½ÕÉ”Á…Ñ èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹œ½É•±…Ñ¥½¹Í¡¥ÀµÉ•¥ÍÑ•È¹µ‘€)9…µ•ÍÁ…”½¹Ñ•áÐè½¹Ñ•áÑÕ…±€)É•„èÉ•Ù•ÉÍ”µ•¹¥¹••É¥¹€((ŒŒI•±…Ñ¥½¹Í¡¥ÀI•¥ÍÑ•È()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÌéÌÀÀÀÀÀÅ€()AÉ½Ù•¹…¹”Õ•Ìè‘½Õµ•¹Ñ…Ñ¥½¹€°•Ù¥‘•¹•€()Q¡¥ÌÉ•¥ÍÑ•È¥ÌÑ¡”½µÁ…Ð¥¹‘•à½˜É•±…Ñ¥½¹Í¡¥ÁÌÝ¡½Í”•Ù¥‘•¹”…™™•ÑÌµ½É”Ñ¡…¸½¹”‘½Õµ•¹Ñ…Ñ¥½¸Í•Ñ¥½¸¸%ÐÉ•½É‘Ì¹…µ•ÍÁ…”°½¹‘¥Ñ¥½¹Ì°½Ù•É…”°…¹½¹™¥‘•¹”ì‘•Ñ…¥±•½Á•É…Ñ¥½¹…°Í•µ…¹Ñ¥ÌÉ•µ…¥¸½¸Ñ¡”±¥¹­•É•™•É•¹”Á…•Ì¸((ŒŒŒMÑ…ÑÕÌÙ½…‰Õ±…Éä()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÌéÌÀÀÀÀÀÉ€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€()ðMÑ…ÑÕÌð5•…¹¥¹œð)ð€´´´ð€´´´ð)ð•±…É•ð•¹™½É•½È•áÁ±¥¥Ñ±äÉ•ÁÉ•Í•¹Ñ•‰äÑ¡”ÍÑ½É•Í¡•µ„ð)ðMÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð½µÁ±•Ñ”¹½¸µÍ•¹Ñ¥¹•°­•ä½Ù•É…”…¹½µÁ…Ñ¥‰±”Ñ…‰±”½…É‘¥¹…±¥ÑäÉ½±”¥¸Ñ¡¥ÌÉ•Ù¥Í¥½¸ð)ð½ÉÉ½‰½É…Ñ•ð¥¹‘•Á•¹‘•¹Ð‘…Ñ…‰…Í”°…ÁÑÕÉ”°U$°½ÈÁÉ½‘ÕÐ•Ù¥‘•¹”½¹™¥ÉµÌÑ¡”µ•…¹¥¹œð)ðMÑÉ½¹±ä¥¹™•ÉÉ•ð½¹”…¹‘¥‘…Ñ”‰•ÍÐ•áÁ±…¥¹ÌÑ¡”½µÁ±•Ñ”Á…ÑÑ•É¸°‰ÕÐ„‘¥ÍÉ¥µ¥¹…Ñ¥¹œ½‰Í•ÉÙ…Ñ¥½¸¥Ìµ¥ÍÍ¥¹œð)ð=Á•¸ð•Ù¥‘•¹”…¹¹½Ðå•Ð‘¥ÍÑ¥¹Õ¥Í Ñ¡”É•µ…¥¹¥¹œ…¹‘¥‘…Ñ•Ìð)ðI•©•Ñ•ð•Ù¥‘•¹”½¹™±¥ÑÌÝ¥Ñ Ñ¡”ÁÉ½Á½Í•É•±…Ñ¥½¹Í¡¥Àð()½Õ¹ÑÌ…É”Í½Á•Ñ¼Ñ¡”…¹½¹¥…°5å!=5MÕ¥Ñ”€Ì¸Ô¸ÌàÍ½ÕÉ•Ì¸((ŒŒŒ]¥Ñ¡¥¸5!…Ñ…±½Õ”¹‘‰€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÌéÌÀÀÀÀÀÍ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°Í½ÕÉ•€()ðM½ÕÉ”ðQ…É•Ðð½Ù•É…”½½¹‘¥Ñ¥½¹ÌðMÑ…ÑÕÌð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð9}Y%¹¥‘}¥Ñ•µ€ð9}%Q4¹¥‘}¥Ñ•µ€ð€ÔÐÄÉ½ÝÌì€À½ÉÁ¡…¹ÌðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ð9}Y%¹¥‘}‰É…¹‘€ð9}	I9¹¥‘}‰É…¹‘€ð€ÔÐÄÉ½ÝÌì€À½ÉÁ¡…¹ÌðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ð9}Y%¹¥‘}±¥¹•€ð9}1%9¹¥‘}±¥¹•€ð€ÔÐÄÉ½ÝÌì€À½ÉÁ¡…¹ÌðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ð9}%I5]I¹¥‘}¥Ñ•µ€ð9}%Q4¹¥‘}¥Ñ•µ€ð€ÌÄÄÉ½ÝÌì€À½ÉÁ¡…¹ÌðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ð9}	U%1L¹¥‘}™¥ÉµÝ…É•€ð9}%I5]I¹¥‘}™¥ÉµÝ…É•€ð€ÌÀàÉ½ÝÌì€À½ÉÁ¡…¹Ììé•É¼½µÕ±Ñ¥Á±”‰Õ¥±É½ÝÌÁ½ÍÍ¥‰±”Á•È™¥ÉµÝ…É”ðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ðM}%Q5}MeMQ5€ð¥Ñ•´…¹…Ñ…±½Õ”µÍåÍÑ•´Á…É•¹ÑÌð€ÈÈÌÉ½ÝÌì€À½ÉÁ¡…¹Ì½¸•¥Ñ¡•ÈÁ…É•¹ÐðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ðM}=	)Q}MeMQ5€ð=‰©•Ð…¹…Ñ…±½Õ”µÍåÍÑ•´Á…É•¹ÑÌð€ÈÔÄÉ½ÝÌì€À½ÉÁ¡…¹Ì½¸•¥Ñ¡•ÈÁ…É•¹ÐðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ðM}=	)Q}%I5]I€ð™¥ÉµÝ…É”…¹=‰©•ÐÁ…É•¹ÑÌð€àÈÜÉ½ÝÌì€À½ÉÁ¡…¹Ì½¸•¥Ñ¡•ÈÁ…É•¹ÐðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ðM}%I5]I}=9%}5=€ð™¥ÉµÝ…É”…¹½¹™¥ÕÉ…Ñ¥½¸µµ½‘”Á…É•¹ÑÌð™¥ÉµÝ…É”…Á…‰¥±¥Ñä…ÍÍ½¥…Ñ¥½¸ì9}=9%}5=€­••ÁÌY¥ÉÑÕ…°°‘Ù…¹•°A¡åÍ¥…°°…¹AÉ½‘ÕÐAÉ½É…µµ¥¹œ…Ì‘¥ÍÑ¥¹ÐÉ•½É‘ÌðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ð9}M1=QL¹¥‘}½‰©•Ñ}™¥ÉµÝ…É•€ðM}=	)Q}%I5]I¹¥‘}½‰©•Ñ}™¥ÉµÝ…É•€ð€Ä°ÜÈÔÉ½ÝÌìÍ•Ù•É…°=‰©•Ð…±Ñ•É¹…Ñ¥Ù•Ì…¸Í¡…É”™¥ÉÍÑ}Í±½Ñ€ðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ð9}-e}=	)P¹¥‘}™…µ¥±å€ð9}=	)Q}%Q5}5%1d¹¥‘}™…µ¥±å€ð€ÄÔàÉ½ÝÌì€À½ÉÁ¡…¹Ìì¹¼é•É¼Í•¹Ñ¥¹•°ÕÍ•ðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ðM}%I5]I}Y%I%9}=	)Q€ð™¥ÉµÝ…É”…¹Y¥É¥¸=‰©•ÐÁ…É•¹ÑÌð€ÜÔÉ½ÝÌì€À½ÉÁ¡…¹ÌðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ðM}=	)Q}Y%I%9}=	)Q€ðY¥É¥¸=‰©•Ð…¹Á•Éµ¥ÑÑ•=‰©•ÐÁ…É•¹ÑÌð€ÄÀÈÉ½ÝÌì…Á…‰¥±¥ÑäÍ•Ð°¹½ÐÉÕ¹Ñ¥µ”Í•±•Ñ¥½¸ðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ð9}=9}I9¹¥‘}½¹™€ð9}=9¹¥‘}½¹™€ð€ÄÐ°ÌÐØÉ½ÝÌì€À½ÉÁ¡…¹ÌðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ð9}%1QI€ð=‰©•Ð½™¥ÉµÝ…É”…ÍÍ½¥…Ñ¥½¸…¹½¹™¥ÕÉ…Ñ¥½¸‘•™¥¹¥Ñ¥½¸ð€Ä°äÀäÉ½ÝÌì€À½ÉÁ¡…¹Ì½¸‰½Ñ É•™•É•¹•ÌðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ðM}M1=Q}=9%Q%=9€ðÍ±½ÐµÁ±…•µ•¹ÐÉ½Ü…¹½¹‘¥Ñ¥½¸ð€Ä°ÀÀÀÉ½ÝÌì€À½ÉÁ¡…¹Ì½¸‰½Ñ É•™•É•¹•ÌðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ðÁ¡åÍ¥…°½¹‘¥Ñ¥½¸‰É…¹ ð™¥ÉµÝ…É”9}=9€½9}=9}I9€‘½µ…¥¹ÌÁ±ÕÌ9}M1=QM€½M}M1=Q}=9%Q%=9€½9}=9%Q%=9€ðÍÑ½É•½¹‘¥Ñ¥½¸µÕÍÐ‰”É•…¡…‰±”¥¸Ñ¡”•á…Ð™¥ÉµÝ…É”‘½µ…¥¸‰•™½É”¥Ð…¸Í•±•Ð…¸=‰©•Ð½Í±½Ð…¹‘¥‘…Ñ”ð…Ñ…±½Õ”µ¹…Ñ¥Ù”É•Í½±Ù•È•ÍÑ…‰±¥Í¡•™½ÈÉ•ÁÉ•Í•¹Ñ•ÁÉ•‘¥…Ñ•Ìð)ð9}=9€½Ý¹•Èð=‰©•Ð½È™¥ÉµÝ…É”ð€Ä°ÐÈÀ=‰©•ÐµÍ½Á•ì€Ä°ÐØÌ™¥ÉµÝ…É”µÍ½Á•ìÍ•±•Ñ•‰äé•É¼‘¥ÍÉ¥µ¥¹…Ñ½Èð•ÍÑ…‰±¥Í¡•Á½±åµ½ÉÁ¡¥ŒÉ•±…Ñ¥½¹Í¡¥Àð)ð9}%I5]I¹Í±½ÑÍ€ð‘¥ÍÑ¥¹Ð¥¹Ñ•É¹…°5½‘Õ±”Á½Í¥Ñ¥½¹Ìð½µÁ…É”Ý¥Ñ =U9P¡%MQ%9P9}M1=QL¹™¥ÉÍÑ}Í±½Ð¥€°¹½ÐÉ½Ü½Õ¹Ðð½ÉÉ½‰½É…Ñ•…Á…‰¥±¥ÑäÉ•±…Ñ¥½¹Í¡¥Àð()M•”m…Ñ…‰…Í”I•±…Ñ¥½¹Í¡¥ÀI•½¹ÍÑÉÕÑ¥½¹t¡‘…Ñ…‰…Í”µÉ•±…Ñ¥½¹Í¡¥ÀµÉ•½¹ÍÑÉÕÑ¥½¸¹µ¤…¹m•Ù¥”5½‘•±t ¸¸½‘•Ù¥”µµ½‘•°¼¤¸((ŒŒŒ]¥Ñ¡¥¸=A8¹‘‰€()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÌéÌÀÀÀÀÀÑ€()AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()ðM½ÕÉ”ðQ…É•Ðð½Ù•É…”½•Ù¥‘•¹”ðMÑ…ÑÕÌð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ðM}MeMQ5}IMM}IU1€ðÍåÍÑ•´…¹…‘‘É•ÍÌµÉÕ±”Á…É•¹ÑÌð€ÄØÉ½ÝÌì€À½ÉÁ¡…¹Ìì±½…‘•‰ä=Á•¹EÕ•Éä¹ÑáÑ€ð•ÍÑ…‰±¥Í¡•ð)ðM}=A9}MeMQ5€ð™É…µ”…¹ÍåÍÑ•´Á…É•¹ÑÌð€ÈÔÄÉ½ÝÌì€À½ÉÁ¡…¹Ìð•ÍÑ…‰±¥Í¡•ð)ðM}=A9}AI5€ð™É…µ”…¹Á…É…µ•Ñ•ÈÁ…É•¹ÑÌð€äÄÉ½ÝÌì€À½ÉÁ¡…¹ÌìÅÕ•É¥•‰ä=Á•¹EÕ•Éä¹ÑáÑ€ð•ÍÑ…‰±¥Í¡•ð)ðM}M9I%=}MEU9€ðÍ•¹…É¥¼…¹½É‘•É•Í•ÅÕ•¹”ð€ÌäÉ½ÝÌì€À½ÉÁ¡…¹Ìð•ÍÑ…‰±¥Í¡•ð)ðM}=A9}MEU9€ðÍ•ÅÕ•¹”…¹½É‘•É•™É…µ”ð€ÄÐÜÉ½ÝÌì€À½ÉÁ¡…¹Ìì…ÉÉ¥•Ì½É‘•È½É•Á•Ñ¥Ñ¥½¸½ÍÑ…ÑÕÌµ•Ñ…‘…Ñ„ð•ÍÑ…‰±¥Í¡•ð)ðM}Q%5=UQ}=A9}MEU9€ð™É…µ”½Í•ÅÕ•¹”½¹Ñ•áÐ…¹Ñ¥µ•½ÕÐð€ØÈÉ½ÝÌì€À½ÉÁ¡…¹Ì½¸…±°Ñ¡É•”Á…É•¹ÑÌð•ÍÑ…‰±¥Í¡•ð)ð9}=A8¹½Á•¹}ÍÑÉ¥¹€Á±…•¡½±‘•ÉÌð9}=A9}AI4¹Á…É…µ}ÍÑÉ¥¹€ð…ÍÍ½¥…Ñ¥½¸É•ÅÕ¥É•ìÁ±…•¡½±‘•ÈÑ•áÐ…±½¹”¥Ì¹½Ð„±½‰…°­•äð•ÍÑ…‰±¥Í¡•Ý¡•É”…ÍÍ½¥…Ñ•ð((ŒŒŒÉ½ÍÌÝ¥É”ÑÉ…™™¥Œ…¹…Ñ…±½Õ”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÌéÌÀÀÀÀÀÕ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•Ìè…ÁÑÕÉ•€°…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€()ðM½ÕÉ”ðQ…É•ÐðI•ÅÕ¥É•½¹Ñ•áÐðMÑ…ÑÕÌð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð%59M%=8€Ä¹=	)Q}5=1€ðM}%Q5}MeMQ4¹µ½‘½‰©€ðÉ•Í½±Ù•µ…¹…•µ•¹Ð½…Ñ…±½Õ”ÍåÍÑ•´ð½ÉÉ½‰½É…Ñ•ð)ð%59M%=8€Ä¹	I9€ð9}	I9¹‰É…¹‘}µ½‘½‰©€ðÁ…ÉÍ•¥‘•¹Ñ¥ÑäÉ•ÍÁ½¹Í”ð½ÉÉ½‰½É…Ñ•ð)ð%59M%=8€Ä¹1%9€ð9}1%9¹±¥¹•}µ½‘½‰©€ðÁ…ÉÍ•¥‘•¹Ñ¥ÑäÉ•ÍÁ½¹Í”ð½ÉÉ½‰½É…Ñ•ð)ð½É‘¥¹…Éä…‘‘É•ÍÍ•%59M%=8€Ä¹9}=9€ðÁ¡åÍ¥…°½¹™¥ÕÉ…Ñ½ÈµÁ½Í¥Ñ¥½¸½Õ¹Ðð…‘‘É•ÍÍ••Ù¥”¥‘•¹Ñ¥ÑäìÁÉ½‘ÕÐ‘¥…É…µÌ½…ÁÑÕÉ•Ìð½ÉÉ½‰½É…Ñ•™½È‘½Õµ•¹Ñ•…‘‘É•ÍÍ••Ù¥•Ìð)ð…Ñ•Ý…ä%59M%=8€Ä¹9}=9€ðÕ¹É•Í½±Ù•…Ñ•Ý…äµÙ…É¥…¹Ð™¥•±ì½‰Í•ÉÙ•Ù…±Õ”€ÄÕ€½¸5 ÈÀÈ…¹ÐÔÐð•µÁÑäµ]!I€…Ñ•Ý…ä¥‘•¹Ñ¥Ñä…ÁÑÕÉ•Ìð½‰Í•ÉÙ•ìÍ•¹Ñ¥¹•°¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¥¹™•ÉÉ•°•á…ÐÍ•µ…¹Ñ¥Ì½Á•¸ð)ð%59M%=8€É€X¹H¹‰€ð9}%I5]I€Á±ÕÌ9}	U%1M€ðÉ•Í½±Ù•¥Ñ•´ìÍ•¹Ñ¥¹•°½‘•™…Õ±Ð½‰Õ¥±¡…¹‘±¥¹œðÍÑÉÕÑÕÉ…±±ä½ÉÉ½‰½É…Ñ•ì•á…ÐÍ•±•Ñ¥½¸ÁÉ••‘•¹”½Á•¸ð)ð%59M%=8€Í€½€Ù€X¹H¹‰€ð¹¼…¹½¹¥…°…Ñ…±½Õ”™¥•±™½Õ¹ðÉ•Ñ…¥¸…Ì¥¹ÍÑ…±±•µÍÑ…Ñ”•Ù¥‘•¹”ð½Á•¸‘…Ñ…‰…Í”½ÉÉ•±…Ñ¥½¸ð)ð%59M%=8€ÌÀ¹-e=€ð9}-e}=	)P¹­•å}½‰©•Ñ€ðMQQ€ô€Á€°•¹…‰±•5½‘Õ±”°É•Í½±Ù•™¥ÉµÝ…É”…¹Í±½Ñ€ð•áÁ•É¥µ•¹Ñ…±±ä½ÉÉ½‰½É…Ñ•Ý¥Ñ U$‰•¡…Ù¥½Èð)ð%59M%=8€ÌÀ¹-e=€ð9}Y%I%9}=	)P¹Ù¥É¥¹}­•å}½‰©•Ñ€ðMQQ€ô€Å€°‘¥Í…‰±•5½‘Õ±”°É•Í½±Ù•™¥ÉµÝ…É”…¹Í±½Ñ€ð•áÁ•É¥µ•¹Ñ…±±ä½ÉÉ½‰½É…Ñ•Ý¥Ñ U$‰•¡…Ù¥½Èð)ð%59M%=8€ÌÀ¹M1=Q€ð9}M1=QL¹™¥ÉÍÑ}Í±½Ñ€Á±…•µ•¹ÐðÉ•Í½±Ù•™¥ÉµÝ…É”ì¹½Ð¥‘}Í±½Ñ€ðÍÑÉÕÑÕÉ…±±ä½ÉÉ½‰½É…Ñ•ð)ð%59M%=8€ÌÔ¹%9a€ð9}=9¹¥‘á€ð•Ù¥”°™¥ÉµÝ…É”°5½‘Õ±”°=‰©•Ð°…¹½Ý¹•ÉÍ¡¥ÀÍ½Á”ðÍÑÉ½¹±ä½ÉÉ½‰½É…Ñ•ð)ð‘¥…¹½ÍÑ¥Œ½ÕÑ•È]!I€ð½¹™¥ÕÉ•…‘‘É•ÍÌ½˜Í±½Ñ€€Å€ðÉ•Á•…Ñ•]!<€ÄÀÀÅ€½‰Í•ÉÙ…Ñ¥½¹ÌðÍÑÉ½¹±ä¥¹™•ÉÉ•ì…±Ñ•É¹…Ñ”±…å½ÕÑÌ½Á•¸ð)ð%59M%=8€ÌÈ¹MeM€ð5!…Ñ…±½Õ”¹‘ˆ¹9}MeMQ4¹ÍåÍ}µ½‘½‰©€ðÉ•Í½±Ù•=‰©•Ð½ÍåÍÑ•´½¹Ñ•áÐðÍÑÉ½¹±ä¥¹™•ÉÉ•ì¹••‘Ì‘¥ÍÉ¥µ¥¹…Ñ¥¹œ¹½¸µ1¥¡Ñ¥¹œ…ÁÑÕÉ”ð((ŒŒŒÉ½ÍÌ‘…Ñ…‰…Í”µ½‘•±Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÌéÌÀÀÀÀÀÙ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°½¹±ä™½É€°É•Ù¥Í¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°‘…Ñ…‰…Í•€°•Ù¥‘•¹•€°Í½ÕÉ•€()ðM½ÕÉ”ðQ…É•Ðð½¹‘¥Ñ¥½¹Ì½•Ù¥‘•¹”ðMÑ…ÑÕÌð)ð€´´´ð€´´´ð€´´´ð€´´´ð)ð=A8¹9}IMM}IU1¹½‰©•Ñ}‘•Ù¥•}™…µ¥±å€ð5!…Ñ…±½Õ”¹9}=	)Q}%Q5}5%1d¹¥‘}™…µ¥±å€ð…±°€ÄÄ¹½¹é•É¼Ù…±Õ•ÌÉ•Í½±Ù”ì€Á€¥ÌÕ¹ÅÕ…±¥™¥•ìÍ•µ…¹Ñ¥Ì…É•”ðÍÑÉÕÑÕÉ…±±ä…¹Í•µ…¹Ñ¥…±±ä½ÉÉ½‰½É…Ñ•ð)ðÉÕ±•Ì¹-=	)QM€ð9}-e}=	)P¹­•å}½‰©•Ñ€ð=‰©•ÑÌ€äÕ€°€äÙ€°…¹€ÄàÑ€É•ÁÉ•Í•¹Ñ•¥¸Ñ¡¥ÌÉ•Ù¥Í¥½¸ðÍÑÉ½¹±ä½ÉÉ½‰½É…Ñ•ð)ðÉÕ±•Ì¹‘ˆÍ€€‘9€É•™•É•¹”ð9}=9¹¥‘à€ô9€ðÍ•±•Ñ•=‰©•Ð½¹Ñ•áÐ…¹Á…ÉÍ•ÉÕ±”Íå¹Ñ…àðÍÑÉ½¹±ä½ÉÉ½‰½É…Ñ•ð)ðM•¹…É¥½•Ù¥•Ì¡¥=Á•¹€ð™Õ¹Ñ¥½¹…°]!=€Á…ÉÍ•™É½´±¥Ñ•É…°É…µ•€ð…±°€ÔÜ±¥Ñ•É…°Ñ•µÁ±…Ñ•Ì¥¸AÉ½É…´¥±•ÌÉ•Ù¥Í¥½¸…É•”ð•ÍÑ…‰±¥Í¡•™½È±¥Ñ•É…°Ñ•µÁ±…Ñ•Ìð)ðM•¹…É¥½•Ù¥•ÌAÉ½É…µ…Ñ„Í•µ…¹Ñ¥ŒÁ…Ñ ðAÉ½É…´¥±•ÌÍ•µ…¹Ñ¥ŒÁ…Ñ ð½µÁ…É”™Õ±°¡¥•É…É¡ä½¹½¸µ±½…°™¥•±‘Ì°¹•Ù•È±½…°É½Ü%Ìð•ÍÑ…‰±¥Í¡•ÍÕ‰Í•ÐÉ•±…Ñ¥½¹Í¡¥Àð)ðÁ¡åÍ¥…°™¥ÉµÝ…É”ÁÉ½Á•ÉÑäð…‘Ù…¹•=‰©•ÐÁÉ½Á•ÉÑäðÍåµ‰½°°Í•µ…¹Ñ¥ŒÑåÁ”°™¥±Ñ•ÉÌ°½¹Ù•ÉÍ¥½¹Ì°…¹½¹ÑÉ½±±•É•…µ‰…¬ð•ÍÑ…‰±¥Í¡•½¹±ä™½È¥¹‘¥Ù¥‘Õ…±±ä½ÉÉ½‰½É…Ñ•µ…ÁÁ¥¹Ìì•¹•É…±¥é…Ñ¥½¸½Á•¸ð)ð=A8¹‘‰€%59M%=8€Ð¼Ô¹Ä¸¹ÄÉ€ð5!…Ñ…±½Õ”¹‘‰€™¥ÉµÝ…É”9}=9€‘•™¥¹¥Ñ¥½¹Ì€¼ÁÉ½É•ÍÍ¥Ù•€ðÑÉ…¹ÍÁ½ÉÐ™¥•±‘Ì…¹…Ñ…±½Õ”½É‘•É¥¹œ½•á¥ÍÐ°‰ÕÐ¹¼•áÁ±¥¥ÐÉ½ÍÌµ‘…Ñ…‰…Í”­•ä½ÈÕ¹¥Ù•ÉÍ…°Á½Í¥Ñ¥½¹…°ÉÕ±”¥ÌÁÉ•Í•¹Ðð½Á•¸½ÉÉ•±…Ñ¥½¸ð((ŒŒŒM•¹Ñ¥¹•°…¹‘¥ÍÉ¥µ¥¹…Ñ½ÈÉÕ±•Ì()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÌéÌÀÀÀÀÀÝ€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€)U¹•ÉÑ…¥¹ÑäèÕ¹É•Í½±Ù•‘€)AÉ½Ù•¹…¹”Õ•ÌèÍ½ÕÉ•€()ð1½…Ñ¥½¸ðIÕ±”ðMÑ…ÑÕÌð)ð€´´´ð€´´´ð€´´´ð)ð9}=9¹¥‘}­•å}½‰©•Ñ€€¼¥‘}™¥ÉµÝ…É•€ð•á…Ñ±ä½¹”½Ý¹•ÈÉ•Í½±Ù•Ì…¹Ñ¡”½Ñ¡•È¥Ì€Á€ð•ÍÑ…‰±¥Í¡•ð)ð9}IMM}IU1¹½‰©•Ñ}‘•Ù¥•}™…µ¥±ä€ô€Á€ð™…µ¥±äµÕ¹ÅÕ…±¥™¥•…‘‘É•ÍÌÉÕ±”ð½ÉÉ½‰½É…Ñ•‰ä½µÁ±•Ñ”ÉÕ±”Í•Ðð)ð™¥ÉµÝ…É”½µÁ½¹•¹Ð€´Å€ð…¹ä½ÈÕ¹ÍÁ•¥™¥•™½ÈÑ¡…Ð½µÁ½¹•¹ÐðÍÑÉ½¹±ä½ÉÉ½‰½É…Ñ•‰ä€´Ä¸´Ä¸´Å€…¹½¹É•Ñ”X¹H¸´Å€É½ÝÌð)ðµ¥ÍÍ¥¹œ9}	U%1M€É½Üð‘¥ÍÑ¥¹Ð™É½´•áÁ±¥¥Ð™¥ÉµÝ…É•}ˆ€ô€´Å€ðÍÑÉÕÑÕÉ…±±ä•ÍÑ…‰±¥Í¡•ð)ð%59M%=8€ÌÀ¹MQQ€ð€Á€Í•±•ÑÌ•¹…‰±•É•Õ±…È=‰©•Ðì€Å€Í•±•ÑÌ‘¥Í…‰±•Y¥É¥¸=‰©•Ðð•áÁ•É¥µ•¹Ñ…±±ä½ÉÉ½‰½É…Ñ•Ý¥Ñ 5å!=5}MÕ¥Ñ”U$‰•¡…Ù¥½Èð)ð…Ñ•Ý…ä%59M%=8€Ä¹9}=9€ô€ÄÕ€ð€ÄÕ€¥Ì€Áá€ìÙ¥•Ý•¥¸™½ÕÈ‰¥ÑÌ°¥Ð¥Ì€ÄÄÄÅ€°…¸…±°µ½¹•ÌÁ…ÑÑ•É¸½¹Í¥ÍÑ•¹ÐÝ¥Ñ „É•Í•ÉÙ•µÍ•¹Ñ¥¹•°½¹Ù•¹Ñ¥½¸°‰ÕÐ¹¼…¹½¹¥…°Í½ÕÉ”•ÍÑ…‰±¥Í¡•ÌÑ¡”Í•¹Ñ¥¹•°µ•…¹¥¹œð½‰Í•ÉÙ•Ù…±Õ”ìÍ•¹Ñ¥¹•°¥¹Ñ•ÉÁÉ•Ñ…Ñ¥½¸¥¹™•ÉÉ•…¹Õ¹É•Í½±Ù•ð()M•¹Ñ¥¹•°µ•…¹¥¹œ¥Ì±½…°Ñ¼Ñ¡”™¥•±¸Q¡¥ÌÑ…‰±”‘½•Ì¹½Ð…ÕÑ¡½É¥é”¥¹Ñ•ÉÁÉ•Ñ¥¹œ•Ù•Éäé•É¼½È¹•…Ñ¥Ù”Ù…±Õ”Ñ¡”Í…µ”Ý…ä¸((ŒŒŒ=Á•¸É•±…Ñ¥½¹Í¡¥ÁÌ()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÌéÌÀÀÀÀÀá€()ÁÁ±¥…‰¥±¥ÑäÕ•Ìè™¥ÉµÝ…É•€°…Ñ•Ý…å€)U¹•ÉÑ…¥¹Ñäè¡åÁ½Ñ¡•Í¥Í€)AÉ½Ù•¹…¹”Õ•Ìè…Ñ…±½Õ•€°•Ù¥‘•¹•€°Í½ÕÉ•€()ðEÕ•ÍÑ¥½¸ð1•…‘¥¹œ•Ù¥‘•¹”ð•¥Í¥Ù”•Ù¥‘•¹”¹••‘•ð)ð€´´´ð€´´´ð€´´´ð)ð%59M%=8€Ñ€½€Õ€…Ñ…±½Õ”½ÉÉ•±…Ñ¥½¸ðÄ¸¹ÄÉ€ÑÉ…¹ÍÁ½ÉÐ™¥•±‘Ì…¹€À¸¸ÈÔÕ€É…¹•Ì…É”•ÍÑ…‰±¥Í¡•ì½¹™½¹™¥ÕÉ…Ñ½ÉÍ€¥Ì±…‰•±±•Ù¥ÉÑÕ…°½¹™¥ÕÉ…Ñ¥½¸ð½¹ÑÉ½±±••Ù¥”µ™…µ¥±ä½ÉÉ•±…Ñ¥½¸‰•ÑÝ••¸Ä¸¹ÄÉ€…¹™¥ÉµÝ…É”µÍÁ•¥™¥Œ9}=9€Íåµ‰½±Ì½Á½Í¥Ñ¥½¹Ìð)ð•¹•É¥Œ%59M%=8€ÌÄÀ¹Y1}AI€µ•…¹¥¹œð=‰©•ÐµÍÁ•¥™¥ŒÉ•ÍÁ½¹Í”Ý¥Ñ¡½ÕÐ•¹•É¥Œ¥¹‘•àµ•Ñ…‘…Ñ„ð=‰©•ÐµÍÁ•¥™¥Œ…ÁÑÕÉ•Ì…¹‘•½‘•È‰•¡…Ù¥½Èð)ð…Ñ…±½Õ”µÝ¥‘”…‘‘É•ÍÍ•µ™½É´9}=9€™¥•±µ½Õ¹Ð•ÅÕ¥Ù…±•¹”ð‘¥…É…µÌ°…ÁÑÕÉ•Ì°…¹É•Í½±Ù•™¥ÉµÝ…É”™¥•±‘Ì…É•”¥¸Ñ•ÍÑ•…‘‘É•ÍÍ••Ù¥•ÌðÍåÍÑ•µ…Ñ¥Œ½¹‘¥Ñ¥½¹…°µ™¥•±…Õ‘¥Ð…É½ÍÌ™¥ÉµÝ…É”ð)ð…Ñ•Ý…ä9}=9€ô€ÄÕ€µ•…¹¥¹œð5 ÈÀÈ…¹ÐÔÐ…Ñ•Ý…ä…ÁÑÕÉ•Ì‰½Ñ É•ÑÕÉ¸½ÕÐµ½˜µÉ…¹”€ÄÕ€ì€ÄÔ€ô€Áá€¥Ì½µÁ…Ñ¥‰±”Ý¥Ñ „Í•¹Ñ¥¹•°ð…¸…ÁÁ±¥…‰±”¥µÁ±•µ•¹Ñ…Ñ¥½¸‘•½‘•È°…ÕÑ¡½É¥Ñ…Ñ¥Ù”‘•™¥¹¥Ñ¥½¸°½È‘¥ÍÉ¥µ¥¹…Ñ¥¹œ…Ñ•Ý…ä½™¥ÉµÝ…É”½‰Í•ÉÙ…Ñ¥½¹ÌÑ¡…Ð•ÍÑ…‰±¥Í Ñ¡”•¹½‘•µ•…¹¥¹œð)ð™¥ÉµÝ…É”Í•±•Ñ¥½¸ÁÉ••‘•¹”ð•á…Ð°Ý¥±‘…É°‘•™…Õ±Ð°µ¥ÍÍ¥¹œ°µÕ±Ñ¥Á±”µ‰Õ¥±Á…ÑÑ•É¹Ìð½¹ÑÉ½±±•±½…‘•È½U$½‰Í•ÉÙ…Ñ¥½¸ð)ðM•¹…É¥½•Ù¥•Ìµ…Ñ¡¥¹œ%ÌðÍÑ…‰±”±½…°™¥•±‘Ì…¹Í•µ…¹Ñ¥Œ¡¥•É…É¡äðÉÕ¹Ñ¥µ”µ…Ñ¡•ÈÑÉ…”½È…ÁÁ±¥…Ñ¥½¸½‘”ð)ðM•¹…É¥½•Ù¥•ÌÍ½ÕÉ”ÁÉ••‘•¹”ðÑÝ¼É•Ù¥Í¥½¹Ì¥¸‘¥™™•É•¹Ð¥¹ÍÑ…±±…Ñ¥½¸±½…Ñ¥½¹Ìð™¥±”µ½Á•¸½ÕÁ‘…Ñ”ÑÉ…”ð)ðÍ•¹…É¥¼µ¥¹ÍÑ…¹”Á•ÉÍ¥ÍÑ•¹”ð…Á…‰¥±¥ÑäÍÑ½É•Ì±…¬É…Á ÍÑÉÕÑÕÉ”ð½¹ÑÉ½±±•Í…Ù”‘¥™˜…¹™¥±”ÑÉ…”ð()Q¡”™Õ±°É•Í•…É ‰…­±½œ…¹ÁÉ½Á½Í••áÁ•É¥µ•¹ÑÌ…É”¥¸m=Á•¸EÕ•ÍÑ¥½¹Ít¡½Á•¸µÅÕ•ÍÑ¥½¹Ì¹µ¤…¹m!åÁ½Ñ¡•Í¥ÌQ•ÍÑ¥¹t¡¡åÁ½Ñ¡•Í¥ÌµÑ•ÍÑ¥¹œ¹µ¤¸((ŒŒŒ5…¥¹Ñ•¹…¹”ÉÕ±”()M•Ñ¥½¸%è½Ý¹­ˆéÍ•Ñ¥½¸éÀÀÀÄÈÌéÌÀÀÀÀÀå€()ÁÁ±¥…‰¥±¥ÑäÕ•ÌèÉ•Ù¥Í¥½¹€)AÉ½Ù•¹…¹”Õ•Ìè•Ù¥‘•¹•€°Í½ÕÉ•€()]¡•¸•Ù¥‘•¹”¡…¹•Ì„É•±…Ñ¥½¹Í¡¥Àè((Ä¸ÕÁ‘…Ñ”Ñ¡”‘•Ñ…¥±•É•™•É•¹”Á…”ì(È¸ÕÁ‘…Ñ”Ñ¡¥ÌÉ•¥ÍÑ•ÈÌÍÑ…ÑÕÌ°½¹‘¥Ñ¥½¹Ì°…¹½Ù•É…”ì(Ì¸É•µ½Ù”½È¹…ÉÉ½ÜÑ¡”½ÉÉ•ÍÁ½¹‘¥¹œ½Á•¸ÅÕ•ÍÑ¥½¸ì(Ð¸É•Ñ…¥¸É•©•Ñ•…±Ñ•É¹…Ñ¥Ù•ÌÝ¡•¸Ñ¡•ä…É”±¥­•±äÑ¼É•ÕÈì(Ô¸É•½ÉÑ¡”Í½ÕÉ”É•Ù¥Í¥½¸…¹Ñ•ÍÐÑ¡…Ð…ÕÍ•Ñ¡”¡…¹”¸