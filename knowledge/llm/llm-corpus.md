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

**Physical Device → Firmware → Module → Object → Configuration**

Firmware is an implementation layer between the product model and its exposed Modules. In ordinary discussion the shorter **Physical Device → Module → Object → Configuration** form remains sufficient.

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
| Physical Device | An installed hardware product instance | `EN_DEVICE` → `EN_ITEM` |
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

Applicability cues: `revision`
Provenance cues: `catalogue`

Object-scoped definitions describe reusable properties of a logical function. Examples include:

- Function type
- point-to-point address
- group membership
- mode
- delays
- setpoints
- scenario numbers
- button assignments.

In the canonical MyHOME Suite 3.5.38 catalogue, Object `406` (“Scheduled scenario PLUS”) defines this Object-scoped property layout:

| Object | Symbol | `EN_CONF.idx` | Bounded meaning |
| --- | --- | --- | --- |
| `406` | `PPT_CEN_LOW` | `0` | low component of the Scheduled scenario PLUS/CEN number |
| `406` | `PPT_CEN_HIG` | `1` | high component of the Scheduled scenario PLUS/CEN number |
| `406` | `BUTTON_1` | `2` | upper button assignment |
| `406` | `BUTTON_2` | `3` | lower button assignment |

Object `416`, another “Scheduled scenario PLUS” variant in the inspected catalogue, defines `PPT_CEN_LOW` at index `0`, `PPT_CEN_HIG` at index `1`, and `BUTTON_1` at index `2`; it has no `BUTTON_2` definition in that revision. This absence is bounded to the inspected Object and catalogue revision, not a universal rule for CEN-capable Objects.

Object `8` defines the ten group-membership symbols `G1` through `G10` at consecutive indices `240` through `249`. This series is Object-scoped, not global: another Object can define `G1` differently, so an indexed diagnostic value must be resolved through the installed Object before it is interpreted as a group position.

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

The shared “kconf index” terminology strongly supports correlating diagnostic `DIMENSION 35.INDEX` with catalogue `EN_CONF.idx`. Because the databases have no cross-file key, retain the raw frame, resolved Physical Device, firmware, `slot`, Object, and catalogue definition when documenting a mapping. `DIMENSION 310` contains no generic `INDEX` and must remain outside that correlation without Object-specific evidence.

### Address configuration

Section ID: `ownkb:section:d000002:s000018`

Addresses are configuration values scoped to the Object’s functional system. They are not one universal format.

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

`EN_DEVICE.id_item` → `EN_FIRMWARE.id_item` → selected `EN_FIRMWARE.id_firmware`

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

**`slot`** refers specifically to the numeric position used in catalogue structures and diagnostic frames. The `slot` locates the Module; it is not the Module’s functional address.

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

`EN_FIRMWARE` → `AS_OBJECT_FIRMWARE` → `EN_SLOTS`

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

`fixed_ko` must not be translated mechanically into “Function type not user modifiable”. The visible behavior can also depend on Virgin Object associations, conditions, filters, and product-specific UI rules.

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
| `SLOT` | “ko slot” | `1..255` |
| `KEYO` | “device object model” | `1..65535` |
| `STATE` | “configured or not configured” | `0..1` |

This response exposes the Device’s current Module/Object state:

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

For example, Device `[DEVICE_ID]` was observed with `slot` `1` disabled, `slot` `2` absent from the UI, and `slot` positions `3` and `4` displayed under shifted UI numbering. This demonstrates that UI position and `slot` cannot be assumed identical.

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

The IP55 PIR sensor observed as Device `[DEVICE_ID]` illustrates a large Module set: one sensor Module plus optional IR scenario-control Modules across later slots. The catalogue’s maximum observed `first_slot` of `17` is consistent with this class of Device.

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

Documentation uses **Object**, not “KO”, except when quoting database column names or source descriptions.

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

For example, `64391` is catalogued as “Flush mounted actuator and free control”. Its Modules can expose Objects including:

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

`EN_FIRMWARE` → `AS_OBJECT_FIRMWARE` → `EN_SLOTS`

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

A functional-system mapping can be made when the Object’s semantics, functional frame, or another explicit association establishes it. Numeric equality alone is not evidence.

### Diagnostic Object identity

Section ID: `ownkb:section:d000005:s000006`

Provenance cues: `catalogue`

`OPEN.db` defines:

`*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##`

`KEYO` is described as the “device object model” and has range `1..65535`. When `STATE = 0`, `EN_KEY_OBJECT.key_object` supplies the corresponding regular configured Object number for an enabled Module. When `STATE = 1`, resolve against `EN_VIRGIN_OBJECT.virgin_key_object` for the disabled Module instead; see [Virgin Objects](virgin-objects.md).

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

The observed Devices `[DEVICE_ID]`, `[DEVICE_ID]`, `[DEVICE_ID]`, `[DEVICE_ID]`, `[DEVICE_ID]`, and `[DEVICE_ID]` expose Light control functionality without light-actuator hardware.

For these Devices, a Light control Object is their actual command hardware function. It must not be described as an alternate configuration of a light actuator merely because actuator and command Objects participate in the same functional `WHO`.

### Object `406`

Section ID: `ownkb:section:d000005:s000014`

Provenance cues: `catalogue`

Object `406` is catalogued as “Scheduled scenario PLUS”. On products such as `64360` and the command Modules of `64391`, it is one of the Object choices offered at a Module.

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

A Physical Device is one installed hardware product instance. It is the root of the Device → Module → Object → Configuration model, but the catalogue describes the product model while diagnostic traffic identifies the individual installed instance.

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

Several branded products can share one `EN_ITEM` capability definition. For example, products `64391`, `64191`, and `64192` all select item `1184`, named “Flush mounted actuator and free control”. They therefore share the same firmware, Module, Object, and configuration capability model while retaining distinct catalogue Device records.

#### Preferred description

Section ID: `ownkb:section:d000006:s000004`

Cautions: `do not`
Provenance cues: `catalogue`

When identifying a scanned physical product, use `EN_DEVICE.name` as the standard Device description. Do not substitute:

- `EN_ITEM.descr`, which describes the shared capability item
- `EN_KEY_OBJECT.descr`, which describes one logical Object
- a user-interface suffix added outside the catalogue
- an inferred class derived from one Module.

This preserves the distinction between “what product is installed?” and “what functions does it expose?”.

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

`DIMENSION 1` → item/system model + brand + line → catalogue item → matching Device records

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

`OPEN.db` describes `N_CONF` as “Configurator number” and allows `0..12` for the ordinary addressed diagnostic form. Comparison with product configuration diagrams indicates that, in that addressed Device form, `N_CONF` represents the number of physical configurator positions provided by the Device.

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

The classification describes hardware composition. It does not define the Device’s diagnostic identity values.

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

SKU `64360` resolves to item `281`, “Basic control”, with two command Modules. Its catalogue Object choices include Light control, Automation control, Scheduled scenario, and Scheduled scenario PLUS. No actuator Object is exposed by this item.

#### `F411U2`

Section ID: `ownkb:section:d000006:s000013`

Applicability cues: `firmware`

SKU `F411U2` resolves to item `2115`, “2x10A actuator, 2DIN”, and firmware `659`, which declares two slots. Both slots expose actuator capability.

#### `F418U2`

Section ID: `ownkb:section:d000006:s000014`

Applicability cues: `firmware`

SKU `F418U2` resolves to item `2065`, “2x1,6A universal dimmer, 4DIN”, and firmware `590`, which declares two dimmer slots.

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

For SCS Lighting/Automation Devices, the diagnostic `WHERE` of a Physical Device can resemble an `A`/`PL` address. That resemblance does not establish that every Device uses the first Module’s configured address. The relationship must be documented per family or per verified behavior.

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

`rules.db3.rules.KOBJECTS` values `95`, `96`, and `184` align with catalogue Objects Hotel thermostat, Residential thermostat, and Master probe. Its `$N` parameter references align with those Objects’ `EN_CONF.idx` values.

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

- `EN_DEVICE.id_item` → `EN_ITEM.id_item`
- `EN_DEVICE.id_brand` → `EN_BRAND.id_brand`
- `EN_DEVICE.id_line` → `EN_LINE.id_line`
- `EN_FIRMWARE.id_item` → `EN_ITEM.id_item`
- `AS_OBJECT_FIRMWARE` → firmware and Object
- `EN_SLOTS.id_object_firmware` → `AS_OBJECT_FIRMWARE.id_object_firmware`
- firmware/Virgin-Object and Virgin-Object/Object associations
- `EN_CONF_RANGE.id_conf` → `EN_CONF.id_conf`
- `EN_FILTER` → Object/firmware association and configuration definition.

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

“Virgin” describes catalogue capability and the disabled-Module representation used by `DIMENSION 30`, not a separate physical component.

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

`EN_FIRMWARE` → `AS_FIRMWARE_VIRGIN_OBJECT` → `EN_SLOT_KO_VIRGIN` → `slot`

and:

`EN_VIRGIN_OBJECT` → `AS_OBJECT_VIRGIN_OBJECT` → `EN_KEY_OBJECT`

Together they answer: “At this slot under this firmware, which Objects may this configurable Module become?”

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
- the Object’s address or parameters are valid.

Runtime state must be obtained from diagnostic responses or project configuration.

### Examples

Section ID: `ownkb:section:d000008:s000006`

#### Automation double command virgin

Section ID: `ownkb:section:d000008:s000007`

Applicability cues: `firmware`
Provenance cues: `database`

Virgin Object `500`, “Automation double command virgin”, permits five concrete Objects and is used by six firmware definitions in the canonical database.

For firmware `157`, it is placed at `slot` positions `3` and `4`, whose Object choices include:

- Light control
- Automation control
- Scheduled scenario
- Scheduled scenario PLUS.

This corresponds to the free-command portion of `64391`, `64191`, and `64192`.

#### Automation relay virgin

Section ID: `ownkb:section:d000008:s000008`

Applicability cues: `firmware`

Virgin Object `510`, “Automation relay virgin”, permits three concrete Objects and is used by five firmware definitions.

For firmware `157`, it is placed at `slot` positions `1` and `2`, corresponding to the relay/actuator Modules.

#### Dimmer actuator virgin

Section ID: `ownkb:section:d000008:s000009`

Applicability cues: `firmware`

Virgin Object `528`, “Dimmer actuator virgin”, permits two concrete Objects. It is placed at both `slot` positions of firmware `590`, used by `F418U2`.

#### Contact interface single virgin

Section ID: `ownkb:section:d000008:s000010`

Applicability cues: `firmware`

Virgin Object `512`, “Contact interface single virgin”, permits ten Objects. It is placed at both slots of firmware `129`, used by `3477`.

#### Daylight and motion sensor virgin

Section ID: `ownkb:section:d000008:s000011`

Applicability cues: `firmware`

Virgin Object `515`, “Daylight and motion sensor virgin”, permits six Objects and is associated with twelve firmware definitions. This supports a family of sensor configurations but does not by itself define the Object active on a particular Device.

### Virgin Object and `DIMENSION 30`

Section ID: `ownkb:section:d000008:s000012`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`, `evidence`, `source`

`OPEN.db` defines `DIMENSION 30` with `SLOT`, `KEYO`, and `STATE`. The database describes `STATE` only as “configured or not configured”.

`KEYO` uses a state-dependent external identifier namespace:

| `STATE` | Resolve `KEYO` against | Meaning |
| --- | --- | --- |
| `0` | `EN_KEY_OBJECT.key_object` | enabled Module; regular configured Object |
| `1` | `EN_VIRGIN_OBJECT.virgin_key_object` | disabled Module; Virgin Object and configurable role |

`OPEN.db` supplies the binary field and labels it only generically as “configured or not configured”; that source does not by itself establish which numeric value means enabled or disabled. Controlled diagnostic/programming protocol evidence correlated with MyHOME_Suite UI behavior establishes `0 = enabled` and `1 = disabled`. Catalogue resolution independently corroborates the corresponding Object namespace.

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

1. identify the Physical Device’s `EN_ITEM`;
2. select the applicable firmware;
3. select the `slot`;
4. locate the firmware/Virgin-Object association for that slot;
5. enumerate the Virgin Object’s permitted Objects;
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

Diagnostics does not expose the catalogue database directly. It reports installed state that can be interpreted against the canonical **Physical Device → Firmware → Module → Object → Configuration** model described in [`device-model/`](../device-model/).

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
| Point-to-point diagnosis by address | addressed interview → detailed configuration reading → close |
| Point-to-point diagnosis by Device ID | ID interview → detailed configuration reading → close |
| Diagnosis by local interaction | local-button interview → detailed configuration reading → close |
| Plant scan by address | address discovery → repeated addressed interviews → repeated configuration reads → repeated close |
| Plant scan by Device ID | ID enumeration → repeated ID interviews → repeated configuration reads → repeated close |

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
2. Generate only `WHERE` values valid for that family’s address rule.
3. Send `*#[WHO]*[WHERE]*1##` for each candidate.
4. Collect the `DIMENSION 1` response, if any.
5. Preserve the queried `WHERE`, returned identity fields, and raw frame together.
6. Use an ID-based interview when `DIMENSION 13` later supplies a stable Device identity.

Silence can mean no Device, an unsupported diagnostic operation, an invalid address for the selected family, transport loss, or a Device that is temporarily unavailable. Do not collapse these cases into a positive “address unused” result without retry and timeout policy.

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

The table reproduces MyHOME_Suite’s address-rule vocabulary. It does not claim that every rule is valid for every Object in the family. `object_device_family`, validity conditions, and offsets further qualify several entries.

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

The description “Light and Automation system” and observed protocol behavior establish that the management family extends across Lighting and Automation, whose functional protocols use `WHO 1` and `WHO 2` respectively. That broader coverage is not encoded as a second `EN_SYSTEM` mapping and must not be presented as though `OPEN.db` directly pairs `WHO 2` with `WHO 1001`.

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
| `DiagPoint2PointByAddress` | `DiagAddressed` → `DiagKO` → `CloseScan` |
| `DiagPoint2PointWithID` | `DiagAdvanced` → `DiagKO` → `CloseScan` |
| `DiagLocalButton` | `DiagLocalButton` → `DiagKO` → `CloseScan` |
| `ScanPlant` | `ScanAddressed` → repeated `DiagAddressed` → repeated `DiagKO` → repeated `CloseScan` |
| `ScanByAID` | `ScanAID` → repeated `DiagAID` → repeated `DiagKO` → repeated `CloseScan` |

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

The no-response termination rule is capture-derived behavior: the canonical frame database describes repetition and its response window but does not encode a declarative “empty pass” condition.

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

The `WHERE` inside a `DIMENSION 13` response is governed by the diagnostic family’s address grammar. It can assist later addressed operations, but it must not replace the 32-bit Device ID as the inventory key.

### Filters

Section ID: `ownkb:section:d000012:s000006`

Cautions: `must not`
Provenance cues: `source`

The final `#1` and `#0` forms select configured and unconfigured Devices respectively according to the implementation labels in `OPEN.db`. They are concrete frame templates but are not members of the canonical `ScanAID` sequence, which uses the all-Device form.

The precise Device-side definition of “configured” is not expanded by the source. It must not be assumed to mean that every Module is configured, that every address is valid, or that no disabled Module remains.

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
3. `CloseScan` to terminate that Device’s diagnostic session.

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

The observed Device `[DEVICE_ID]` (`[DEVICE_ID]` decimal) reported model value `107`. In the canonical catalogue:

- `AS_ITEM_SYSTEM.modobj = 107` resolves to item `1184`;
- `EN_ITEM.descr` is “Flush mounted actuator and free control”;
- firmware definition `157` declares four `slot` positions;
- several branded SKUs, including `64391`, `64191`, and `64192`, share that item.

The example corroborates the model-to-item path while also demonstrating why `OBJECT_MODEL` alone does not uniquely identify one SKU. Brand and line values, plus project/UI context where available, are required to narrow the Device record.

### `N_CONF` and physical configurators

Section ID: `ownkb:section:d000014:s000006`

Applicability cues: `firmware`

`OPEN.db` describes `N_CONF` as “Configurator number” / “number of physical configurator” and constrains the ordinary addressed form to `0..12`. Product configuration diagrams provide an independent interpretation for that addressed Device form: the value corresponds to the number of physical configurator positions provided by the Device.

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

Numerically, `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern. Its repeated use in both observed gateway tuples is therefore consistent with a reserved or sentinel value, but no canonical source currently establishes that interpretation or the sentinel's meaning. The evidence does not justify presenting gateway `N_CONF = 15` as a literal count of fifteen physical configurator positions, nor as a proven encoding of “zero configurators” or “not applicable”. Preserve the raw value and its unresolved semantics.

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

Use **Module** for the logical container and **`slot`** for `SLOT`. `OPEN.db` uses the legacy label “ko slot”; this documentation retains that wording only when quoting or naming source fields.

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

Do not renumber `slot` positions to match a UI’s visible Module numbering. MyHOME_Suite can hide or relabel slots, and observed scenario Devices show UI numbering that differs from the numeric diagnostic position.

### Enabled and disabled Modules

Section ID: `ownkb:section:d000015:s000005`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`, `evidence`

Controlled diagnostic/programming experiments correlated with direct MyHOME_Suite UI observations establish the `DIMENSION 30` polarity. `OPEN.db` describes `STATE` generically as “configured or not configured”, but that label does not establish the numeric polarity by itself:

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

- Device `[DEVICE_ID]` demonstrated that `slot` numbering and UI-visible Module numbering can differ: `slot` `2` was absent from the UI while later slots were renumbered for display.
- Device `[DEVICE_ID]` demonstrated a large layout with `slot` positions through `17`, consistent with the maximum `EN_SLOTS.first_slot` observed in this catalogue revision.
- Light-control-only Device `[DEVICE_ID]` exposed command Modules as its actual hardware function; those Objects must not be interpreted as alternate actuator modes.

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
- the functional system’s addressing rules;
- catalogue configuration metadata where corroborated.

The range `0..65535` is storage capacity, not a universal set of valid functional addresses.

`SYS` is described only as “KeyObject system” by `OPEN.db`. It must not be equated automatically with a functional `WHO`, a diagnostic `WHO`, `OPEN.db.EN_SYSTEM.id_system`, or `MHCatalogue.db.EN_SYSTEM.id_system`. A numeric mapping requires Object/system and capture corroboration.

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

Observed sensor Device `[DEVICE_ID]` used diagnostic `WHERE 0015`, interpreted as `A = 0`, `PL = 15`. Retaining the raw field is important because padding and family-specific formatting can be lost by integer-only storage.

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

The working capture model is therefore narrower than “all Modules have `DIMENSION 32`”: addressed actuator/sensor Modules have produced it, while at least one command-only layout did not. Treat availability as Object- and firmware-dependent until broader evidence is available.

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
| `INDEX` | `0..255` | parameter number, labelled “kconf index” |
| `SLOT` | `1..255` | Device-local `slot` |
| `VAL_PAR` | `0..65535` | parameter value |

Both `#` separators are significant parts of the canonical template.

### Catalogue correlation

Section ID: `ownkb:section:d000017:s000003`

Applicability cues: `firmware`, `revision`
Cautions: `must not`
Provenance cues: `catalogue`

The shared “kconf index” terminology and observed behavior strongly support correlating `INDEX` with `MHCatalogue.db` `EN_CONF.idx`. The databases contain no cross-file foreign key, so resolution must retain the full context:

- Physical Device and firmware;
- `slot`;
- regular configured Object reported by `DIMENSION 30` for an enabled Module; a disabled Module's Virgin Object is a role constraint, not an Object-scoped configuration owner;
- applicable Object- or firmware-scoped `EN_CONF` definition;
- filters, conditions, and conversion rules;
- raw `VAL_PAR`.

`INDEX` is not globally unique. The same number can name different properties for different Objects or firmware definitions.

For Object `406` in the canonical MyHOME Suite 3.5.38 catalogue, indices `0`, `1`, `2`, and `3` resolve respectively to `PPT_CEN_LOW`, `PPT_CEN_HIG`, `BUTTON_1`, and `BUTTON_2`. Object `416` resolves indices `0`, `1`, and `2` to the first three of those symbols and has no `BUTTON_2` definition in the inspected revision. These mappings are Object-scoped and must not be inferred from the index alone.

The `LOW` and `HIG` names and their catalogue ranges support interpreting the two components as bytes. Decode a combined value as `LOW + 256 × HIG` only when that combination rule is independently established for the applicable Device family; otherwise retain both raw components and label the combined number as an inference rather than a universal protocol rule.

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

1. Resolve the Device’s catalogue item and firmware.
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

`rules.db3` adds cross-property validation for selected Temperature Control Objects. It can refine a resolved value’s validity but is not a general `INDEX` registry. The ScenarioDevices databases define scenario-action parameters in separate namespaces and must not be used as `EN_CONF.idx` mappings.

### Runtime availability

Section ID: `ownkb:section:d000017:s000008`

Applicability cues: `firmware`
Cautions: `do not`

`OPEN.db` models `DIMENSION 35` as a repeatable detailed-configuration response, but not every Object necessarily emits it. Observed configurable command and sensor Modules support the association with editable configuration; observed absence from another Module cannot by itself prove that the Object has no configuration.

Do not infer a universal split such as “actuators use only `DIMENSION 32`, commands use only `DIMENSION 35`”. A Module can have an address, indexed parameters, both, or neither depending on its Object and firmware.

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

The frame also carries a boolean `STATE` labelled configured/not configured. The two “not implemented” descriptions are preserved from distinct source entries; the source does not further clarify their boundary.

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

The general `DIMENSION 7`, `11`, `12`, and `15` records are directly associated with the Nurse Call system in `AS_OPEN_SYSTEM`. `OpenQuery.txt` also selects the general `DIMENSION 7` frames and the gateway `DIMENSION 1` form for gateway-connection handling. This supports reuse in a gateway/service workflow but does not make these frames part of every diagnostic family’s Device interview.

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

The [Temperature Control Specification](../sources/openwebnet-public/pdf/WHO_4.pdf), version 2.0.0, pages 69–74, defines these targets, sequences, counts, bit labels, and polarity. See [Diagnostic Architecture](architecture.md) for the separate MyHOME Suite management model and [Temperature Control Properties](../functional/who-4-temperature-control/dimensions.md) for functional properties.

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
| `4` | Device → programmer | `*[WHO]*4*[WHERE_FAKE]##` | Device end of transmission |
| `4` | Device → programmer | `*[WHO]*4*0##` | end-of-transmission variant |
| `5` | Programmer → Device | `*[WHO]*5*0##` | start diagnosis through local-button/general mode |
| `6` | Either diagnostic participant in source labels | `*[WHO]*6*0##` | abort/close diagnosis |
| `10` | Programmer → Device | `*[WHO]*10#[ID]*0##` | start diagnosis by Device ID |
| `11` | Programmer → Device | `*[WHO]*11#[ID]*0##` | mark/suppress an ID already found during enumeration |
| `12` | Programmer → Device | `*[WHO]*12*0##` | release/reset Device-ID enumeration state |

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
- `MHCatalogue.db` describes physical Devices and the Device → Module → Object → Configuration capability model.
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
| Which physical Devices support a functional system? | `MHCatalogue.db.EN_DEVICE` → `EN_ITEM` → `AS_ITEM_SYSTEM` |
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

See [MyHOME_Suite `OPEN.db` Coverage](open-db-coverage.md) for the complete `OPEN.db` namespace/management matrix and [Device Model](../device-model/) for the catalogue Device → Module → Object → Configuration model. See [Scenario Engine](../scenario-engine/) for the complete ScenarioDevices schema, category and matching model, parameter types, template rendering rules, capability coverage, and execution boundaries.

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

Energy Management is marked `managed = 1`, uses diagnostic `WHO 1018`, and is associated with the same 65-record managed-device operation set as Lighting/Automation and Access Control. This associates the family with MyHOME_Suite's common Device → Module → Object → Configuration management capability in addition to the functional energy `DIMENSION` operations. It does not establish that every installed Energy Management Device supports every registered operation.

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

For `WHO 0`, `3`, `5`, `6`, `7`, `9`, `10`, `11`, `12`, `14`, `15`, `16`, `17`, `19`, `22`, `24`, `25`, `26`, and `99`, `OPEN.db` supplies a functional system identity but no direct `AS_OPEN_SYSTEM` → `EN_OPEN` operation association. This is still useful evidence: it confirms the namespace name used by MyHOME_Suite and, in some cases, an interface variant or diagnostic-family assignment. It does **not** establish undocumented `WHAT`, `WHERE`, or `DIMENSION` values.

Notable additional rows are `Interface AI L3` under `WHO 5`, `Interface Multimedia L2` under `WHO 6`, and `Multimedia System` under `WHO 22` with diagnostic `WHO 1022`. These rows show that the database distinguishes interface/system variants even where it does not provide their functional frame vocabulary.

### Interpretation rule

Section ID: `ownkb:section:d000023:s000012`

Cautions: `not evidence`
Provenance cues: `evidence`, `source`

Use `OPEN.db` evidence at the narrowest level it actually establishes:

- `EN_SYSTEM` → namespace/system identity and diagnostic-family association.
- `AS_SYSTEM_ADDRESS_RULE` + `EN_ADDRESS_RULE` → address grammar used by MyHOME_Suite for that system.
- `AS_OPEN_SYSTEM` + `EN_OPEN` → concrete frame template associated with that system.
- `AS_OPEN_PARAM` + `EN_OPEN_PARAM` → parameter layout and constraints for a concrete operation.
- `AS_OPEN_SEQUENCE`, `EN_SEQUENCE`, and timeout tables → workflow ordering and state-machine behavior.

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

- No public page means “not established by the current public corpus,” not “the function does not exist.”
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

For the Device → Module → Object → Configuration model, see [Device Model](../../device-model/).

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

The generic name “Messages” is not sufficient to infer payload encoding, recipient addressing, text representation, notification type, or acknowledgement behavior. Those semantics remain unknown until supported by implementation definitions or captured traffic.

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

`*15*BUTTON*WHERE##` → `*15*BUTTON#1*WHERE##`

The first frame marks pressure; the second identifies release before the extended-pressure threshold.

### Extended interaction sequence

Section ID: `ownkb:section:d000039:s000006`

A held button produces:

`*15*BUTTON*WHERE##` → one or more `*15*BUTTON#3*WHERE##` → `*15*BUTTON#2*WHERE##`

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

Energy Management separates instantaneous values from accumulated and historical values. `DIMENSION 113` reports active power in watts. Totalizer operations expose accumulated values, while `DIMENSION 511..514` return time-series data for daily and monthly graphics. The published specification labels several accumulated values as “Watt”; where the frame description explicitly identifies energy since reset it uses Wh. Implementations should preserve the published field semantics rather than silently normalizing units from the identifier alone.

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

The published ranges describe valid address spaces, not proof that every index is populated. Software that needs to probe functional Energy Management addresses must distinguish “address can exist” from “device is present.”

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

The published specification describes `Val` as the energy/unit totalizer value and labels its unit as Watt. This terminology is preserved rather than silently correcting the wire model from the word “totalizer.”

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

The published source renders the unit as “Watt/h”; the operation represents the daily energy-history series. The same sequence can be initiated by `WHAT 57#M#D`.

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

For the common OpenWebNet frame language, see [Protocol](../../protocol/). For the Device → Module → Object → Configuration model used to describe physical Automation devices, see [Device Model](../../device-model/).

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

The source describes frequency steps as `50`, `100`, … `750 Hz`; this appears unusually small for radio tuning. This reference preserves the published values without silently relabelling their unit.

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

The shared 65-record management set establishes participation in the common Device → Module → Object → Configuration infrastructure where applicable; it does not imply that every Access Control Device implements every operation.

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

The [Lighting Management Specification](../../sources/openwebnet-public/pdf/WHO_24.pdf), pages 4–5, gives the notation and concrete two-endpoint examples.

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

Pages 4–5 instead show selector-qualified examples `18#65` with response values `297*0`. That differs structurally from the `18*Sensor_addr` form on pages 21–22 and 39–41. Retain both as source variants and select only a form corroborated for the gateway; do not silently move the sensor between selector and payload.

State and illuminance are distinct from the configuration threshold in `DIMENSION 2`.

Capability support is device-specific. The namespace-level table defines available operations but does not imply that every Lighting Management endpoint accepts every write.

### Evidence basis

Section ID: `ownkb:section:d000057:s000009`

Provenance cues: `specification`

Domains and frame variants come from the [Lighting Management Specification](../../sources/openwebnet-public/pdf/WHO_24.pdf), pages 6–41. The discrepancies above are retained because they affect safe encoding and request/response matching.

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

`WHAT 22` → zero or more `WHAT 23` → `WHAT 24`.

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

This is materially different from Basic/Evolved CEN, where `WHO 15` `WHERE` can represent an `A`/`PL` source address and the button number itself occupies `WHAT`.

### Relationship to CEN

Section ID: `ownkb:section:d000061:s000012`

Provenance cues: `source`

| Property | CEN - `WHO 15` | CEN+ - `WHO 25` |
| --- | --- | --- |
| Button number | `WHAT 00..31` | `WHAT` parameter `0..31` |
| Interaction phase | optional `WHAT` parameter `#1..#3` | `WHAT 21..24` |
| Source/target | `A`/`PL` and advanced CEN `WHERE` forms | virtual Object `0..2047` with prefix `2` |
| Rotary events | not defined in the published CEN table | `WHAT 25..28` |

The two systems should be modeled separately even when a physical command device is capable of both modes.

### Other `WHO 25` functions

Section ID: `ownkb:section:d000061:s000013`

`WHO 25` also carries dry-contact and IR functions using `WHAT 31` and `32`. Those operations use different parameters and `WHERE` grammars and are documented in [Dry Contact and IR](dry-contact-ir.md).

# Document: ownkb:document:d000062

Source path: `functional/who-25-transversal/dry-contact-ir.md`
Namespace context: `who:25`
Area: `functional`

## Dry Contact and IR

Section ID: `ownkb:section:d000062:s000001`

Dry-contact and IR functions are carried within the `WHO 25` namespace while remaining functionally distinct from CEN+.

### `WHAT`

Section ID: `ownkb:section:d000062:s000002`

| `WHAT` | Meaning |
| --- | --- |
| `31` | ON / IR detection |
| `32` | OFF / IR not detected or end of detection |

The parameter following `WHAT` distinguishes state reporting from a system event/action context:

| Parameter | Meaning |
| --- | --- |
| `0` | State returned by a request |
| `1` | State associated with an event/action |

Command/event forms therefore include `*25*31#1*WHERE##` and `*25*32#1*WHERE##`. A state request uses `*#25*WHERE##`; the response uses `*25*VALUE#0*WHERE##`, where `VALUE` is `31` for ON / IR detection or `32` for OFF / no detection.

### `WHERE`

Section ID: `ownkb:section:d000062:s000003`

Two published address forms are established:

| `WHERE` | Application |
| --- | --- |
| `1..201` | Automation dry-contact interfaces configured using Virtual Configurator Software |
| `[1-9][1-9]` | Alarm dry-contact interfaces and IR devices configured using physical `Z` and `N` configurators |

The published device families include automation dry-contact interfaces such as 3477/F428 and alarm/IR interfaces such as 3480/F482 and IR detector families.

### Functional navigation

Section ID: `ownkb:section:d000062:s000004`

Dry contacts are indexed separately in [Functional Protocol](../README.md) so readers searching by function can reach this page directly while the canonical reference remains under `WHO 25`.

# Document: ownkb:document:d000063

Source path: `functional/who-25-transversal/zigbee-binding.md`
Namespace context: `who:25`
Area: `functional`

## ZigBee Binding

Section ID: `ownkb:section:d000063:s000001`

Applicability cues: `firmware`, `gateway`, `revision`, `version`, `zigbee`
Cautions: `do not`
Provenance cues: `evidence`, `source`, `specification`

The Legrand ZigBee OpenWebNet specification version 4.0 defines a ZigBee-specific binding family under `WHO 25`. These OpenWebNet operations expose the host-visible binding lifecycle while leaving the underlying ZigBee binding tables, radio association mechanisms, and other ZigBee-internal procedures outside the encyclopedia boundary.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. The semantics below are **specification evidence** for that interface revision. They do not establish support by every gateway, product, or firmware revision.

### `WHAT` reference

Section ID: `ownkb:section:d000063:s000002`

Applicability cues: `scs`, `zigbee`
Cautions: `must not`
Provenance cues: `source`

| `WHAT` | Source action | Direction in the detailed definition |
| --- | --- | --- |
| `21` | Short Pressure | server to client |
| `33` | Binding Request | client to server |
| `34` | Unbinding Request | client to server |
| `35` | Open Binding | server to client |
| `36` | Close Binding | server to client |
| `37` | Cancel Binding | server to client |

These values share `WHO 25` with SCS CEN+ and dry-contact/IR functions, but their grammar and applicability are selected by the ZigBee interface context. A ZigBee binding `WHERE` must not be decoded as an SCS CEN+ virtual Object merely because the numeric `WHO` is the same.

### Addressing

Section ID: `ownkb:section:d000063:s000003`

Applicability cues: `zigbee`
Provenance cues: `documentation`

Binding frames use the [ZigBee product-and-Unit `WHERE` grammar](../../protocol/zigbee-interface.md#transport-and-addressing) and family suffix `#9`.

Structurally, Binding Request and Unbinding Request use `*25*WHAT*WHERE#9##`, where `WHERE` identifies the radio product and Unit. Real installation identifiers should not be reproduced in documentation examples.

### Binding lifecycle

Section ID: `ownkb:section:d000063:s000004`

Applicability cues: `zigbee`
Provenance cues: `source`

The published binding use case establishes this OpenWebNet-visible sequence:

1. The server reports `WHAT 35` when binding is opened for a product Unit.
2. The client sends `WHAT 33` to request binding for that same addressed Unit.
3. `ACK` means the Binding Request command has been sent; `NACK` means it has not. BUSY uses the ZigBee interface's ordinary BUSY/NACK sequence.
4. The server later reports `WHAT 36` when binding is closed.

`ACK` therefore acknowledges the Binding Request command according to the source. It should not be described as proof of the underlying ZigBee binding-table mutation independently of the later lifecycle indications.

### Unbinding lifecycle

Section ID: `ownkb:section:d000063:s000005`

Applicability cues: `zigbee`
Provenance cues: `source`

The published unbinding use case follows the same host-visible pattern:

1. `WHAT 35` reports an opened binding procedure.
2. The client sends `WHAT 34` to request unbinding.
3. `ACK` or `NACK` reports whether the command was sent, with BUSY handled by the interface-specific BUSY/NACK sequence.
4. `WHAT 36` reports closure of the binding procedure.

The source does not expose the underlying ZigBee operation that performs the association change. That mechanism remains outside scope.

### Cancel Binding

Section ID: `ownkb:section:d000063:s000006`

Applicability cues: `zigbee`
Provenance cues: `source`, `specification`

`WHAT 37` is server-originated in the detailed definition. The source defines two forms:

- `*25*37*WHERE#9##` when two products are leaders of the source's "PnL binding" procedure;
- `*25*37*##` when a binding was opened and remained unclosed for ten minutes.

The specification uses the term "PnL" in this context. This page does not expand that acronym into an underlying ZigBee procedure beyond what the OpenWebNet frames establish.

### Events from a bound product

Section ID: `ownkb:section:d000063:s000007`

Applicability cues: `zigbee`
Provenance cues: `specification`

The specification's binding use case shows that later button activity is reported through the functional namespace appropriate to the bound product:

- a scenario product can report `WHO 25 / WHAT 21` Short Pressure;
- a Lighting product can report `WHO 1` Toggle;
- an Automation product can report its Automation movement commands.

The ZigBee specification contains a separate internal conflict over Automation UP/DOWN numeric values. The binding reference therefore does not use the binding example to resolve that conflict or redefine the canonical Automation command table.

### No `DIMENSION` family

Section ID: `ownkb:section:d000063:s000008`

Applicability cues: `zigbee`
Provenance cues: `source`, `specification`

The ZigBee specification explicitly states that this `WHO 25` variant has no `DIMENSION` table and no `DIMENSION` IDs. Binding state in this source is represented through `WHAT` traffic, not a parallel binding `DIMENSION` registry.

### Evidence limits

Section ID: `ownkb:section:d000063:s000009`

Applicability cues: `firmware`, `gateway`, `version`, `zigbee`
Provenance cues: `specification`

The exploratory ZigBee branch recorded a minimum gateway firmware version of `1.2.3` for explicit binding commands. That threshold is not stated by the inspected ZigBee OpenWebNet specification and is not promoted here without separate implementation provenance.

Likewise, the published binding lifecycle establishes OpenWebNet-visible commands, acknowledgements, and indications; it does not establish the internal ZigBee binding-table representation or radio-layer procedure.

See [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for the interface-specific `WHERE` and acknowledgement model, and [`WHO 25` - Transversal Functions](README.md) for the other protocol families sharing this namespace.

# Document: ownkb:document:d000064

Source path: `functional/who-26-upnp-multimedia/README.md`
Namespace context: `who:26`
Area: `functional`

## `WHO 26` - UPnP Multimedia

Section ID: `ownkb:section:d000064:s000001`

The MyHOME_Suite `OPEN.db` system definitions identify `WHO 26` as a UPnP multimedia command namespace.

### Protocol position

Section ID: `ownkb:section:d000064:s000002`

Cautions: `do not`
Provenance cues: `source`

`WHO 26` belongs to the broader multimedia area but remains independent from camera/video [`WHO 7`](../who-7-multimedia-video/), Sound System [`WHO 16`](../who-16-sound-system/), and Sound Diffusion [`WHO 22`](../who-22-sound-diffusion/). Shared concepts such as media, source, playback, or navigation do not imply shared numeric encodings.

### Corpus status

Section ID: `ownkb:section:d000064:s000003`

Cautions: `must not`
Uncertainty: `unknown`
Provenance cues: `evidence`, `specification`

The current implementation corpus establishes the namespace but does not yet support a complete system-specific `WHAT`, `WHERE`, or `DIMENSION` reference. No public dedicated `WHO 26` specification is present in the canonical PDF set used by this repository.

Parsers should therefore preserve `WHO 26` traffic losslessly and expose unknown fields as raw values. Semantics from `WHO 7`, `16`, or `22` must not be copied into this namespace without direct evidence.

This page intentionally records the strongest established model rather than filling the missing vocabulary by analogy.

# Document: ownkb:document:d000065

Source path: `functional/who-27-nurse-call/README.md`
Namespace context: `who:27`
Area: `functional`

## `WHO 27` - Nurse Call Basic Level

Section ID: `ownkb:section:d000065:s000001`

MyHOME Suite `OPEN.db` identifies functional `WHO 27` as Nurse Call basic level and assigns diagnostic family `WHO 1027`.

### Evidence boundary

Section ID: `ownkb:section:d000065:s000002`

Cautions: `must not`
Provenance cues: `database`, `specification`

The current public corpus contains no dedicated `WHO 27` functional specification. `OPEN.db` marks the system `managed = 0`, so it does not establish a normal managed-Device workflow or an ordinary functional `WHAT` table.

Nevertheless, nine `EN_OPEN` records are associated with the system. They cover password challenge/result handling, general diagnostic requests and masks, automatic diagnostic events, WebServer model identification, and MAC-address retrieval.

Those records establish a concrete service/diagnostic surface. Most are parameterized by `[WHO]`; substitution and session context must be resolved from the database workflow before assigning them to functional `WHO 27` or diagnostic `WHO 1027`. They must not be presented as an invented Nurse Call functional vocabulary.

### Decoder guidance

Section ID: `ownkb:section:d000065:s000003`

Cautions: `do not`
Uncertainty: `unknown`

- Recognize `WHO 27` as Nurse Call basic level.
- Preserve unknown functional fields losslessly.
- Treat `WHO 1027` as a distinct diagnostic namespace.
- Do not infer room, bed, call-state, acknowledgement, or alarm values from the application domain.
- Use the associated service templates only in the context established by their `OPEN.db` sequence and parameter records.

### Evidence basis

Section ID: `ownkb:section:d000065:s000004`

Provenance cues: `source`

The namespace name, diagnostic-family assignment, management flag, and associated service records come from `OPEN.db`. See [MyHOME Suite `OPEN.db` Coverage](../open-db-coverage.md) for the exact templates and [Functional Source Coverage](../source-coverage.md) for the absence rule.

# Document: ownkb:document:d000066

Source path: `functional/who-3-load-management/README.md`
Namespace context: `who:3`
Area: `functional`

## `WHO 3` - Load Management

Section ID: `ownkb:section:d000066:s000001`

`WHO 3` is the published Power/Load Management namespace. It controls load-shedding priority states and reports measurements from the load-management control unit.

It predates and remains distinct from the richer Energy Management model in `WHO 18`.

### `WHAT` values

Section ID: `ownkb:section:d000066:s000002`

| `WHAT` | Meaning |
| --- | --- |
| `0` | Load disabled |
| `1` | Load enabled |
| `2` | Load forced |
| `3` | Remove forcing |

The public command flow explicitly defines `WHAT 2` as a force command. All four values can appear as monitor/event status for a priority target.

### `WHERE` values

Section ID: `ownkb:section:d000066:s000003`

Cautions: `must not`

| Target | `WHERE` |
| --- | --- |
| General | `0` |
| Control unit / measurement target | `10` |
| Load priority | `#1..#8` |

The leading `#` is part of a priority address. A priority must not be normalized to bare decimal `1..8`.

### Load forcing

Section ID: `ownkb:section:d000066:s000004`

Applicability cues: `gateway`

```text
*3*2*#PRIORITY##
```

The gateway answers with `ACK` if the command is forwarded to the bus or `NACK` if it is not. The same functional frame can appear on the event session as the resulting forced state.

### Status requests

Section ID: `ownkb:section:d000066:s000005`

General request:

```text
*#3*0##
```

The server returns one status frame for each priority, followed by a terminating acknowledgement:

```text
*3*STATE*#PRIORITY##
...
*#*1##
```

A single-priority request uses the corresponding `#PRIORITY` as `WHERE`:

```text
*#3*#PRIORITY##
```

The published text is typographically degraded in places, but the surrounding tables and repeated examples consistently establish general `0` and priority `#1..#8` targets.

### Measurement `DIMENSION` values

Section ID: `ownkb:section:d000066:s000006`

Uncertainty: `not established`
Provenance cues: `evidence`, `source`

Measurements address the control unit with `WHERE=10`.

| `DIMENSION` | Meaning | Unit stated by the source |
| --- | --- | --- |
| `0` | All measurements | ordered voltage, current, power, energy |
| `1` | Voltage | volt |
| `2` | Current | ampere |
| `3` | Power | watt |
| `4` | Energy | not specified in the source |

Request/response forms are:

```text
*#3*10*0##
*#3*10*0*VOLTAGE*CURRENT*POWER*ENERGY##

*#3*10*1##
*#3*10*1*VOLTAGE##
```

`DIMENSION 2`, `3`, and `4` use the same pattern. Successful command-session responses terminate with `ACK`; the report form can also appear on the event session.

The source does not define numeric scaling, signedness, precision, or the energy unit. Preserve raw values when those details are not established by Device evidence.

### Relationship to `WHO 18`

Section ID: `ownkb:section:d000066:s000007`

`WHO 3` provides priority-based load state and four basic measurements. `WHO 18` defines later Energy Management families, address forms, totalizers, histories, automatic updates, Stop&Go state, and actuator operations. Similar physical subject matter does not make their `WHAT`, `WHERE`, or `DIMENSION` identifiers interchangeable.

### Evidence basis

Section ID: `ownkb:section:d000066:s000008`

Applicability cues: `revision`, `version`
Provenance cues: `specification`

The value tables and frame flows come from [`WHO 3` specification](../../sources/openwebnet-public/pdf/WHO_3.pdf), version 1.0.0. The PDF's embedded text encoding is damaged, so this page was checked against rendered pages as well as extracted text. Ambiguous typography has not been used to invent additional ranges or units.

MyHOME Suite `OPEN.db` confirms the namespace name but does not associate a concrete functional operation set with it in this revision.

See the [functional overview](../) for navigation by `WHO` and by function, and [Protocol](../../protocol/) for common frame and session syntax.

# Document: ownkb:document:d000067

Source path: `functional/who-4-temperature-control/README.md`
Namespace context: `who:4`
Area: `functional`

## `WHO 4` - Temperature Control

Section ID: `ownkb:section:d000067:s000001`

Applicability cues: `scs`, `version`, `zigbee`
Provenance cues: `catalogue`, `source`, `specification`

`WHO 4` defines the OpenWebNet Temperature Control system. It covers zones and probes, central-unit operating modes, measured and target temperatures, local offsets, fan-coil speed, valve and actuator state, holiday operation, and split-unit control.

Unlike Lighting and Automation, Temperature Control uses a zone/probe-oriented `WHERE` grammar. Functional traffic can address master probes, all probes in a zone, individual slave probes, the central unit, zones through the central unit, and actuator instances.

The published OpenWebNet specification defines the functional state and command model. The MyHOME_Suite `OPEN.db` definitions complement it with implemented address rules and command templates, while the MyHOME_Suite catalogue and rule data describe the configuration capabilities of physical Temperature Control Objects. Diagnostic traffic uses the separate diagnostic namespace `WHO 1004` and is documented under [Diagnostics](../../diagnostics/).

The supplied [ZigBee Interface](../../protocol/zigbee-interface.md) also exposes a much narrower `WHO 4` surface: the version 4.0 source defines server-originated signed temperature reports through `DIMENSION 0`, not the broad SCS zone and central-unit model below. See the [ZigBee Temperature Control Variant](zigbee-variant.md).

### Reference

Section ID: `ownkb:section:d000067:s000002`

Applicability cues: `zigbee`

| Subject | Page |
| --- | --- |
| Operating modes and commands | [`WHAT` Reference](what.md) |
| Zones, probes, central unit and actuator `WHERE` forms | [Addressing](addressing.md) |
| Temperature, status and control `DIMENSION` operations | [`DIMENSION` Reference](dimensions.md) |
| ZigBee-specific temperature-reporting semantics | [ZigBee Temperature Control Variant](zigbee-variant.md) |

### Temperature representation

Section ID: `ownkb:section:d000067:s000003`

Temperature values are encoded as fixed-width decimal fields whose resolution depends on the operation. Measured/status temperatures commonly use 0.1 °C resolution, while setpoint-writing operations use the range and step defined by that operation. The frame definition must therefore determine how a temperature field is decoded; temperature-looking values are not globally interchangeable.

See [Protocol](../../protocol/) for common OpenWebNet frame classes and [Device Model](../../device-model/) for the Device → Module → Object → Configuration model.

# Document: ownkb:document:d000068

Source path: `functional/who-4-temperature-control/addressing.md`
Namespace context: `who:4`
Area: `functional`

## Addressing

Section ID: `ownkb:section:d000068:s000001`

Temperature Control uses a zone/probe-oriented `WHERE` grammar rather than the `A`/`PL` grammar used by Lighting and Automation. Leading zeroes are significant because they distinguish address classes.

### Published functional `WHERE` forms

Section ID: `ownkb:section:d000068:s000002`

| Scope | Form | Meaning |
| --- | --- | --- |
| General probes | `0` | All probes |
| Master probe | `1..99` | Master probe of zone `1..99` |
| All probes in zone | `001..099` | Master and slave probes belonging to the selected zone |
| Individual probe | `PZZ` | Probe `P` (`1..8`) of zone `ZZ` (`01..99`) |
| Central unit | `#0` | Temperature Control central unit |
| Zone via central unit | `#1..#99` | Selected zone controlled through the central unit |

Examples of individual-probe encoding include `101` for probe 1 of zone 1, `801` for probe 8 of zone 1, and `899` for probe 8 of zone 99.

The forms `1` and `001` are therefore not equivalent: `1` selects the master probe of zone 1, whereas `001` selects all probes belonging to zone 1.

### MyHOME_Suite address rules

Section ID: `ownkb:section:d000068:s000003`

Cautions: `must not`

The MyHOME_Suite `OPEN.db` address-rule definitions represent Temperature Control through several operation-specific forms:

| Form | Purpose |
| --- | --- |
| `[ZA][ZB]` | Temperature Control zone |
| `[ZAZB]` | Advanced zone form |
| `#0#[ZA][ZB]` | Four-zone central-unit form |
| `[ZA][ZB]#[N]` | Temperature Control actuator instance |

These implementation forms complement the public functional grammar. The selected operation determines which rule is valid; clients must not normalize all Temperature Control `WHERE` values to one integer zone identifier.

### Actuator addressing

Section ID: `ownkb:section:d000068:s000004`

Actuator-oriented `DIMENSION` operations can append an actuator selector to the zone address. This is distinct from addressing a probe in the same zone and is used by operations such as actuator state reported by read-only `DIMENSION 20`. The public forms are `Z#N` for actuator `N` (`1..9`) in zone `Z` (`0..99`), `Z#0` for all actuators of a zone, and `0#0` for all actuators. Split control uses the additional prefix `3#Z#N` under `DIMENSION 22`.

### Central-unit addressing

Section ID: `ownkb:section:d000068:s000005`

A leading `#` identifies central-unit scope in the published functional grammar. `#0` addresses the central unit itself; `#N` addresses zone `N` through the central unit. Central-unit commands include zone mode changes, setpoint changes, program/scenario selection, and holiday operations.

See [`WHAT` Reference](what.md) for central-unit commands, [`DIMENSION` Reference](dimensions.md) for operation-specific payloads, and [Addressing](../../protocol/addressing.md) for the common system-scoped addressing model.

# Document: ownkb:document:d000069

Source path: `functional/who-4-temperature-control/dimensions.md`
Namespace context: `who:4`
Area: `functional`

## `DIMENSION` Reference

Section ID: `ownkb:section:d000069:s000001`

`WHO 4` uses `DIMENSION` frames for measured temperature, complete probe state, local offset, setpoint, fan-coil, valve and actuator state, split-unit control, and holiday deadline data.

### Functional `DIMENSION` table

Section ID: `ownkb:section:d000069:s000002`

| `DIMENSION` | Meaning | Access |
| --- | --- | --- |
| `0` | Measured temperature | Read |
| `11` | Fan-coil speed | Read |
| `12` | Complete probe status | Read |
| `13` | Local set offset | Read |
| `14` | Setpoint temperature | Read / write |
| `19` | Valve status | Read |
| `20` | Actuator status | Read |
| `22` | Split control | Read / write |
| `30` | Holiday-scenario end date | Read / write |
| `31` | Holiday-scenario end time | Read / write |

The MyHOME_Suite ScenarioDevices capability data additionally defines Temperature Control action templates using `DIMENSION 7`, and write forms using `DIMENSION 5` and `11`. These implementation operations complement the published functional table and should be interpreted from their exact MyHOME_Suite templates rather than silently mapped onto unrelated public operations.

### MyHOME_Suite `DIMENSION 7` action model

Section ID: `ownkb:section:d000069:s000003`

ScenarioDevices defines `DIMENSION 7` actions with a two-field mode structure after the `DIMENSION` identifier. The first value selects the thermal context and the second selects the requested operating state.

#### Thermal context

Section ID: `ownkb:section:d000069:s000004`

| First value | Context |
| --- | --- |
| `0` | Generic |
| `1` | Heating |
| `2` | Cooling |
| `3` | Automatic |

#### Operating state

Section ID: `ownkb:section:d000069:s000005`

| Second value | State | Additional value |
| --- | --- | --- |
| `1` | Setpoint | four-digit `c1c2c3c4` temperature |
| `2` | Protection | none |
| `3` | Comfort | none |
| `4` | Eco | none |
| `5` | OFF | none; ScenarioDevices uses generic context `0` |

The exact MyHOME_Suite templates are:

| Operation | Generic | Heating | Cooling | Automatic |
| --- | --- | --- | --- | --- |
| Comfort | `*#4*ZAZB*#7*0*3*##` | `*#4*ZAZB*#7*1*3*##` | `*#4*ZAZB*#7*2*3*##` | `*#4*ZAZB*#7*3*3*##` |
| Eco | `*#4*ZAZB*#7*0*4*##` | `*#4*ZAZB*#7*1*4*##` | `*#4*ZAZB*#7*2*4*##` | `*#4*ZAZB*#7*3*4*##` |
| Protection | `*#4*ZAZB*#7*0*2*##` | `*#4*ZAZB*#7*1*2*##` | `*#4*ZAZB*#7*2*2*##` | `*#4*ZAZB*#7*3*2*##` |
| Setpoint | `*#4*ZAZB*#7*0*1*c1c2c3c4##` | `*#4*ZAZB*#7*1*1*c1c2c3c4##` | `*#4*ZAZB*#7*2*1*c1c2c3c4##` | `*#4*ZAZB*#7*3*1*c1c2c3c4##` |

OFF is encoded by ScenarioDevices as `*#4*ZAZB*#7*0*5*##`.

The MyHOME_Suite labels distinguish antifreeze/protection according to thermal context: heating uses antifreeze, cooling uses protection, and automatic/generic variants retain their own action labels. The wire structure remains the same two-value `DIMENSION 7` model.

### MyHOME_Suite local-control and fan-coil writes

Section ID: `ownkb:section:d000069:s000006`

ScenarioDevices also defines:

| Capability | Template |
| --- | --- |
| Local control | `*#4*ZAZB*#5*val##` |
| Fan-coil speed | `*#4*ZAZB*#11*val##` |

These are scenario-engine action templates. Their presence establishes that MyHOME_Suite can emit the write form for these operations; it does not by itself redefine every public read/status meaning attached to the same `DIMENSION` number.

### `DIMENSION 0` - measured temperature

Section ID: `ownkb:section:d000069:s000007`

A measured-temperature request uses `*#4*WHERE*0##`; the response carries the temperature value after `DIMENSION 0`.

Published measured/status temperature fields use four decimal digits and can represent `0000..0500` (`0.0..50.0` °C) with 0.1 °C resolution in the documented zone-status exchanges. This representation is distinct from setpoint-writing constraints.

### `DIMENSION 11` - fan-coil speed

Section ID: `ownkb:section:d000069:s000008`

Provenance cues: `specification`

`DIMENSION 11` reports fan-coil speed in the published status model. ScenarioDevices additionally defines the write template `*#4*ZAZB*#11*val##`, establishing a MyHOME_Suite scenario action for fan-coil speed.

The public response/event form is `*#4*WHERE*11*SPEED*##`, including a trailing empty field. `SPEED` is `0` automatic, `1..3` the three speeds, or `15` OFF (public specification, page 15).

Read and write forms should therefore be distinguished by frame direction and operation context rather than assuming that the identifier is globally read-only in the implementation.

### `DIMENSION 12` - complete probe status

Section ID: `ownkb:section:d000069:s000009`

Cautions: `do not`

`DIMENSION 12` returns the complete probe state, combining the zone's target/status information with its operating context. It is the appropriate operation when a client needs more than the scalar measured temperature returned by `DIMENSION 0`.

The public request is `*#4*WHERE*12##` for master-probe addresses `1..99`. The response `*#4*WHERE*12*T*3##` gives the setpoint after local offset: `T` ranges over `0020..0430` in 0.1 °C units. The trailing `3` is fixed in this published flow; the actual heating/conditioning/protection state is also returned in a separate `*4*WHAT*WHERE##` frame. Do not interpret the final `3` as a complete replacement for that state frame (page 16).

### `DIMENSION 13` - local set offset

Section ID: `ownkb:section:d000069:s000010`

`DIMENSION 13` reports the local setpoint offset applied at the probe. Local offset is separate from the central target temperature: a zone can therefore have a central setpoint and a probe-local adjustment simultaneously.

Request `*#4*WHERE*13##`; response/event `*#4*WHERE*13*OFFSET##` (pages 16–17).

| `OFFSET` | Knob state |
| --- | --- |
| `00` | No offset |
| `01`, `02`, `03` | +1, +2, +3 °C |
| `11`, `12`, `13` | -1, -2, -3 °C |
| `4` | Local OFF |
| `5` | Local protection |

These are codes, not signed decimal temperatures.

### `DIMENSION 14` - setpoint temperature

Section ID: `ownkb:section:d000069:s000011`

`DIMENSION 14` is readable and writable. A zone setpoint written through the central unit uses `*#4*#WHERE*#14*T*M##`.

For this operation, `T` is encoded as four digits in `0050..0400` (5.0..40.0 °C) in 0.5 °C steps. `M` identifies the operating context: `1` heating, `2` conditioning, `3` generic.

The MyHOME_Suite functional parameter definitions likewise represent setpoint ranges and steps for Temperature Control operations; the exact parameter definition attached to the command remains authoritative for the implementation form being encoded.

The public read form is `*#4*WHERE*14##`, with response `*#4*WHERE*14*T*3##` for probe addresses `1..99`. The read table specifies 0.1 °C resolution over `0050..0400`; it does not change the 0.5 °C step specified for writes (page 18).

### `DIMENSION 19` - valve status

Section ID: `ownkb:section:d000069:s000012`

`DIMENSION 19` reports cooling- and heating-valve state. Published valve/fan-coil values include OFF, ON, opened, closed, stop, and fan-coil speed states.

Request `*#4*WHERE*19##`; response/event `*#4*WHERE*19*CV*HV##`. `CV` is the conditioning valve and `HV` the heating valve, in that order (page 21).

| Value | Valve state |
| --- | --- |
| `0` | OFF |
| `1` | ON |
| `2` | Opened |
| `3` | Closed |
| `4` | Stop |
| `5` | Fan-coil OFF |
| `6`, `7`, `8` | Fan-coil ON at speed 1, 2, 3 |

The published table defines values `0..8`; later information supplied by the MyHOME team documents additional fan-coil OFF-speed states `14`, `15`, and `16`. These extended values have been observed in real `WHO 4` status responses and complement the older public PDF rather than changing the `DIMENSION 19` frame structure.

### `DIMENSION 20` - actuator status

Section ID: `ownkb:section:d000069:s000013`

Cautions: `must not`

`DIMENSION 20` represents Temperature Control actuator state. The MyHOME_Suite address model supports an actuator selector appended to the zone address (`[ZA][ZB]#[N]`), allowing actuator instances to be distinguished from probe addressing.

Request `*#4*Z#N*20##`; response/event `*#4*Z#N*20*VALUE##`. The public target grammar includes `Z#N` (`Z = 0..99`, `N = 1..9`), `Z#0` for all actuators of a zone, and `0#0` for all actuators.

`VALUE` uses the same `0..8` labels as the valve table above, with additional `9` = fan-coil ON. It is therefore richer than a boolean ON/OFF value (page 22). Direct control must not be inferred merely from the existence of a status value: the public functional table classifies `DIMENSION 20` as read-only.

### `DIMENSION 22` - split control

Section ID: `ownkb:section:d000069:s000014`

Cautions: `do not`
Provenance cues: `evidence`, `source`

`DIMENSION 22` is the read/write operation for split-unit control. The published protocol defines request, write and monitor/status exchanges for split control under `WHO 4`.

The request is `*#4*3#Z#N*22##`; the write is `*#4*3#Z#N*#22*MOD*SP*VEL*SWING##`. Read responses use `*#4*3#Z#N*22*MOD*SP*VEL*SWING##`. The request/write tables define `Z = 0..99`, `N = 1..9` (pages 66–68).

| Field | Published values |
| --- | --- |
| `MOD` | `0` OFF; `1` winter; `2` summer; `3` fan; `4` dehumidification; `5` automatic |
| `SP` | Temperature in tenths of °C, in 0.5 °C steps; examples `000`, `005`, `010` through `1270` |
| `VEL` | `0` automatic; `1` minimum; `2` medium; `3` maximum; `4` silent |
| `SWING` | `0` OFF; `1` ON |

The source also labels each field `NULL` for current/insignificant values, without defining a literal wire spelling. Do not transmit the letters `NULL` or assume a numeric sentinel without target-specific evidence. The monitor table omits the explicit `3#` prefix from its address note while the request/write tables include it; retain raw addresses when reconciling those reports. The write table also reverses its direction arrow; its write marker and section title establish a client write.

The broad published `SP` range is an encoding range, not a claim that a particular split unit accepts every temperature.

### `DIMENSION 30` - holiday end

Section ID: `ownkb:section:d000069:s000015`

Provenance cues: `source`

The central unit uses separate date and time dimensions (pages 54, 57–58):

| Operation | Request | Response/event | Write |
| --- | --- | --- | --- |
| End date | `*#4*#0*30##` | `*#4*#0*30*D*M*Y##` | `*#4*#0*#30*D*M*Y##` |
| End time | `*#4*#0*31##` | `*#4*#0*31*H*MIN##` | `*#4*#0*#31*H*MIN##` |

`D` is `01..31`, `M` is `01..12`, `Y` is `2000..2099`, `H` is `00..23`, and `MIN` is `00..59`. Validate the actual calendar date as well as individual field ranges.

`DIMENSION 31` is omitted from the source's summary table but explicitly defined by its detailed flows. Some read examples mistakenly include the write marker; the response column and monitor forms establish the unprefixed report form. These operations set the deadline used by the [Temperature Control Commands](what.md).

### Temperature fields are operation-specific

Section ID: `ownkb:section:d000069:s000016`

Cautions: `do not`
Provenance cues: `database`

Temperature-looking values in `WHO 4` do not have one universal range or resolution. In particular:

| Context | Published representation |
| --- | --- |
| Measured/status temperature | four digits, typically 0.1 °C resolution |
| Manual zone/central-unit setpoint write | `0050..0400`, 0.5 °C steps |
| MyHOME_Suite ScenarioDevices `DIMENSION 7` setpoint | four-digit `c1c2c3c4` field; use the associated implementation parameter definition for validation |
| Other MyHOME_Suite command parameters | range/step defined by the associated parameter record |

Decoders and encoders should therefore select the temperature representation from the `DIMENSION`/operation definition, not from `WHO 4` alone.

See [Addressing](addressing.md) for zone/probe/actuator forms, [`WHAT` Reference](what.md) for operating modes, [Cross-database functional coverage](../cross-database-coverage.md) for the implementation cross-reference, and [`DIMENSION`](../../protocol/dimensions.md) for the common `DIMENSION` frame classes.

### Evidence basis

Section ID: `ownkb:section:d000069:s000017`

Applicability cues: `version`
Provenance cues: `specification`

Published payloads and page references above come from the [Temperature Control Specification](../../sources/openwebnet-public/pdf/WHO_4.pdf), version 2.0.0. ScenarioDevices extensions and reported later-device behavior remain separately identified. The same PDF also defines [Temperature Control Fault Diagnostics](../../diagnostics/temperature-control-faults.md) under `WHO 1004`; those are not functional `WHO 4` dimensions.

# Document: ownkb:document:d000070

Source path: `functional/who-4-temperature-control/what.md`
Namespace context: `who:4`
Area: `functional`

## `WHAT` Reference

Section ID: `ownkb:section:d000070:s000001`

`WHO 4` uses `WHAT` both for direct Temperature Control commands and for operating-state/event reporting. Several values encode the active heating/conditioning/generic mode together with the operating mode.

### Basic operating states

Section ID: `ownkb:section:d000070:s000002`

| `WHAT` | Meaning |
| --- | --- |
| `0` | Conditioning mode |
| `1` | Heating mode |
| `20` | Remote control disabled |
| `21` | Remote control enabled |
| `22` | At least one probe OFF |
| `23` | At least one probe in antifreeze |
| `24` | At least one probe in manual mode |
| `30` | Failure detected |
| `31` | Central-unit battery fault |
| `40` | Release local probe adjustment |

### Protection and OFF states

Section ID: `ownkb:section:d000070:s000003`

| `WHAT` | Meaning |
| --- | --- |
| `102` | Antifreeze |
| `202` | Thermal protection |
| `302` | Generic protection |
| `103` | OFF - heating |
| `203` | OFF - conditioning |
| `303` | OFF - generic |

Antifreeze is the heating-side protection state; thermal protection is the conditioning-side protection state. Generic forms are used where the operating mode is not specialized to heating or conditioning.

### Manual and programmed operation

Section ID: `ownkb:section:d000070:s000004`

| `WHAT` | Meaning |
| --- | --- |
| `110` | Manual adjustment - heating |
| `210` | Manual adjustment - conditioning |
| `310` | Manual adjustment - generic |
| `111` | Programmed/automatic - heating |
| `211` | Programmed/automatic - conditioning |
| `311` | Programmed/automatic - generic |
| `115` | Daily holiday plan - heating |
| `215` | Daily holiday plan - conditioning |
| `315` | Daily holiday plan - generic |

A zone controlled through the central unit uses central-unit addressing; for example, automatic generic operation is commanded with `*4*311*#WHERE##` for the selected zone.

### Vacation, program and scenario forms

Section ID: `ownkb:section:d000070:s000005`

Cautions: `do not`, `must not`
Provenance cues: `source`

These operations target the central unit with `WHERE = #0`. The detailed flows on pages 29–52 establish the following values; the summary table on page 5 contains shifted/mismatched descriptions and must not override them.

| Operation | Heating | Conditioning | Generic/current context |
| --- | --- | --- | --- |
| Weekly program `1..3` | `1101..1103` | `2101..2103` | `3101..3103` |
| Restore last weekly program | - | - | `3100` |
| Scenario `1..16` | `1201..1216` | `2201..2216` | `3201..3216` |
| Restore last scenario | - | - | `3200` |
| Daily holiday plan, then return to program | `115#PROGRAM` | `215#PROGRAM` | `315#PROGRAM` |
| Vacation for `DDD` days, then return to program | `13DDD#PROGRAM` | `23DDD#PROGRAM` | `33DDD#PROGRAM` |
| Cancel vacation and choose weekly program | - | - | `3000#PROGRAM` |
| Cancel vacation and restore last weekly program | - | - | `3000` |

`DDD` is a three-digit day count. The summary table lists `000..999`, but the detailed command flows restrict it to `001..255`; use that narrower domain when encoding these documented commands. The vacation examples send `13002#3103`, `23002#3103`, or `33002#3103` for two days followed by weekly program 3. The source notes that the reported remaining period includes the current day, so its corresponding event examples report `13003`, `23003`, or `33003`; do not demand byte equality between the command and its event.

For daily holiday commands, the return-program parameter is `1101..1103` for heating, `2101..2103` for conditioning, and `3101..3103` for generic mode. The multi-day vacation commands use `3101..3103` in all three contexts. Daily-holiday event examples instead show the selected ordinal after `115#` or `215#`. Retain that command/report distinction. The deadline itself is set/read with [holiday date and time properties](dimensions.md#dimension-30---holiday-end).

Example: `*4*3102*#0##` selects weekly program 2 in the current thermal context. A reply/event can use the resolved heating or conditioning program code. An acknowledgement confirms submission, not that the requested mode was physically attained.

### Zone setup commands

Section ID: `ownkb:section:d000070:s000006`

Zone setup is performed through the central unit using `WHERE` forms `#1..#99`.

| Operation | Frame form |
| --- | --- |
| Manual setpoint | `*#4*#WHERE*#14*T*M##` |
| Automatic/programmed mode | `*4*311*#WHERE##` |
| OFF | `*4*303*#WHERE##` |
| Antifreeze | `*4*102*#WHERE##` |
| Thermal protection | `*4*202*#WHERE##` |
| Generic protection | `*4*302*#WHERE##` |

For the manual setpoint operation, `T` is a four-digit temperature value in `0050..0400` with 0.5 °C steps. `M` identifies the operating context: `1` heating, `2` conditioning, `3` generic.

A successful command-session submission is acknowledged with `ACK`; failure to submit the command to the bus is reported with `NACK`.

See [Addressing](addressing.md) for probe, zone and central-unit `WHERE` forms and [`DIMENSION` Reference](dimensions.md) for temperature/status payloads.

# Document: ownkb:document:d000071

Source path: `functional/who-4-temperature-control/zigbee-variant.md`
Namespace context: `who:4`
Area: `functional`

## ZigBee Variant

Section ID: `ownkb:section:d000071:s000001`

Applicability cues: `revision`, `scs`, `version`, `zigbee`
Uncertainty: `unresolved`
Provenance cues: `evidence`, `source`, `specification`

The ZigBee OpenWebNet version 4.0 specification defines a deliberately narrow `WHO 4` Temperature Control surface for the Legrand serial ZigBee interface. In the inspected section, `WHO 4` is used to receive temperature reports from a ZigBee probe. It does not define the broad SCS zone, central-unit, actuator, setpoint, program, or split-control model documented elsewhere in this namespace.

The source is [ZigBee OpenWebNet Specification](../../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0 dated 22 November 2016. Its Confidential footer and unresolved public-release provenance remain recorded in the [Source-Coverage Audit](../../project/review/phase-3-source-coverage.md). The material below is **specification evidence for this interface revision**.

### Documented surface

Section ID: `ownkb:section:d000071:s000002`

Applicability cues: `scs`, `zigbee`
Provenance cues: `specification`

The ZigBee `WHO 4` section contains no `WHAT` entries. Its `DIMENSION` table defines only:

| `DIMENSION` | ZigBee specification meaning | Direction established by the section |
| --- | --- | --- |
| `0` | Temperature level | server to client |

The report form is:

`*#4*WHERE#9*0*LEVEL##`

`WHERE` uses the [ZigBee product-and-Unit address family](../../protocol/zigbee-interface.md#transport-and-addressing), not the SCS Temperature Control zone/probe grammar.

The section defines no `WHO 4` request frame for this value. A client-side measured-temperature request such as the one documented for SCS must therefore not be inferred for this ZigBee interface from the shared `DIMENSION 0` identifier.

### Temperature encoding

Section ID: `ownkb:section:d000071:s000003`

Applicability cues: `scs`
Provenance cues: `source`

`LEVEL` is four digits `C1C2C3C4`:

| Field | Meaning |
| --- | --- |
| `C1` | sign: `0` positive, `1` negative |
| `C2C3` | whole-temperature tens and units |
| `C4` | decimal digit in 0.1 °C steps |

The source examples demonstrate both positive and negative values. It does not state a complete valid temperature range beyond this field structure, so the encyclopedia does not infer one from the number of available digits.

This encoding is materially different from the SCS-oriented `DIMENSION 0` representation documented in [`DIMENSION` Reference](dimensions.md). The two payloads must be selected by interface variant rather than decoded through one shared temperature rule.

### Prior procedure

Section ID: `ownkb:section:d000071:s000004`

Applicability cues: `zigbee`
Provenance cues: `source`

The source states that the probe must previously have completed a source-named "PnL" procedure with the OpenWebNet interface and points to the `WHO 25` use cases.

This establishes a prerequisite in the source's ZigBee workflow but does not establish the underlying ZigBee radio procedure as OpenWebNet. See [ZigBee Binding](../who-25-transversal/zigbee-binding.md) for the OpenWebNet-visible `WHO 25` lifecycle.

### Evidence limits

Section ID: `ownkb:section:d000071:s000005`

Applicability cues: `scs`, `version`, `zigbee`
Cautions: `must not`

The absence of other `WHAT` and `DIMENSION` values from this ZigBee section means that version 4.0 does not establish them for this interface. It is not a universal statement that no ZigBee Temperature Control implementation can expose additional OpenWebNet operations.

In particular, the SCS central-unit modes, zone commands, `DIMENSION 11..31`, actuator addressing, and split-control operations must not be transferred to this variant by namespace equality.

See [Temperature Control](README.md) for the broader SCS-oriented namespace and [ZigBee OpenWebNet Interface](../../protocol/zigbee-interface.md) for common ZigBee transport and addressing.

# Document: ownkb:document:d000072

Source path: `functional/who-5-alarm/README.md`
Namespace context: `who:5`
Area: `functional`

## `WHO 5` - Alarm

Section ID: `ownkb:section:d000072:s000001`

`WHO 5` defines the OpenWebNet Burglar Alarm system. The published protocol is primarily a monitoring and state-reporting interface: it exposes central-unit state, zone state, alarm events, power and battery conditions, technical and silent alarms, and a small set of programming-related operations.

### Reference

Section ID: `ownkb:section:d000072:s000002`

| Subject | Page |
| --- | --- |
| Session behavior and status reporting | [Protocol](protocol.md) |
| Published `WHAT` vocabulary | [`WHAT` Reference](what.md) |
| Central unit, zone, sensor and auxiliary addressing | [Addressing](addressing.md) |

### State model

Section ID: `ownkb:section:d000072:s000003`

Alarm traffic is not reducible to one armed/disarmed Boolean. A central-unit status request can produce several frames describing system mode, engagement, battery and mains conditions, active/divided zones, and alarm conditions before the terminating `ACK`.

Zone-specific requests similarly report whether a selected zone is engaged or divided. Alarm events identify their scope through the `WHO 5` `WHERE` grammar, which is independent of Lighting/Automation `A`/`PL` addressing.

The published interface does not define a general-purpose modern security-control API. Implementations should therefore expose the documented states and events without inventing write semantics for status values that are only established as reports.

`WHO 5` is distinct from Access Control [`WHO 23`](../who-23-access-control/) and from diagnostic protocol families. Common frame/session syntax is documented under [Protocol](../../protocol/).

# Document: ownkb:document:d000073

Source path: `functional/who-5-alarm/addressing.md`
Namespace context: `who:5`
Area: `functional`

## Addressing

Section ID: `ownkb:section:d000073:s000001`

Cautions: `must not`

Published `WHO 5` `WHERE` values include:

| `WHERE` | Meaning |
| --- | --- |
| `1` | Control panel |
| `#0..#8` | Central zone `0..8` |
| `#1..#9` | Auxiliary `1..9` (`WHO 9` relationship in the published table) |
| `01..0n` | Input-zone device |
| `11..1n` | Zone 1 sensor |
| `81..8n` | Zone 8 sensor |
| `#12` | Zone C / AUX C |
| `#15` | Zone F / AUX F |

Zone `0` is used for inputs and the three internal sirens in the published model. Alarm addressing is therefore its own `WHO 5` grammar and must not be parsed as Lighting/Automation A/PL.

# Document: ownkb:document:d000074

Source path: `functional/who-5-alarm/protocol.md`
Namespace context: `who:5`
Area: `functional`

## Protocol

Section ID: `ownkb:section:d000074:s000001`

`WHO 5` uses ordinary OpenWebNet command/event frames together with status requests. The published interface is strongly status-oriented and often returns a sequence of state frames followed by `ACK`.

### Central-unit status request

Section ID: `ownkb:section:d000074:s000002`

A central-unit request uses `*#5##`. The response can contain multiple `WHO 5` frames before `*#*1##`. The published response set covers maintenance/active state, engaged/disengaged state, battery conditions, mains presence, zone engagement/division, zone alarm conditions, technical alarms and silent alarms.

A client must therefore collect the complete response sequence. Treating the first returned `WHO 5` frame as the complete central-unit state loses independent state axes.

### Zone status request

Section ID: `ownkb:section:d000074:s000003`

A zone request follows `*#5*#N##`, with published zones `N = 1..8`. The response identifies the zone as active/engaged with `WHAT 11` or non-active/divided with `WHAT 18`, followed by `ACK`.

The `#N` form is a zone selector, not a numeric point-to-point address. See [Addressing](addressing.md).

### Event connection

Section ID: `ownkb:section:d000074:s000004`

Alarm state changes are also emitted as events. Consumers should normalize events using the pair `(WHAT, WHERE)` because the same `WHAT` family can describe central-unit, zone, sensor, or auxiliary context depending on `WHERE`.

### Programming values

Section ID: `ownkb:section:d000074:s000005`

The published vocabulary includes `WHAT 26` and `27` for start/stop programming. These belong to the historical `WHO 5` functional protocol. They are not the same subsystem as the MyHOME_Suite Device/Object configuration protocol documented under [Programming](../../programming/).

### Write support

Section ID: `ownkb:section:d000074:s000006`

Cautions: `must not`

Some published `WHAT` values describe system states rather than commands. Their presence in the vocabulary must not be interpreted as permission to transmit them as control operations. Where the corpus only establishes a value in responses/events, this reference treats it as report-only.

See [`WHAT` Reference](what.md) for values and [Addressing](addressing.md) for target syntax.

# Document: ownkb:document:d000075

Source path: `functional/who-5-alarm/what.md`
Namespace context: `who:5`
Area: `functional`

## `WHAT` Reference

Section ID: `ownkb:section:d000075:s000001`

| `WHAT` | Meaning | Typical role |
| --- | --- | --- |
| `0` | Maintenance | Central-unit state |
| `1` | Activation | Central-unit state |
| `2` | Disactivation | State/event |
| `3` | Delay end | Event |
| `4` | System battery fault | Fault state/event |
| `5` | Battery OK | State/event |
| `6` | No network | Mains/network fault state |
| `7` | Network present | Mains/network state |
| `8` | Engage | System state/control context |
| `9` | Disengage | System state/control context |
| `10` | Battery unloads | Battery fault state |
| `11` | Active zone | Zone state |
| `12` | Technical alarm | Alarm event |
| `13` | Reset technical alarm | Alarm event/state |
| `14` | No reception / `ACK` peripheral device | Peripheral state |
| `15` | Intrusion alarm | Alarm event |
| `16` | 24-hour alarm / tampering | Alarm event |
| `17` | Anti-panic alarm | Alarm event |
| `18` | Non-active zone | Zone state |
| `26` | Start programming | Programming operation |
| `27` | Stop programming | Programming operation |
| `31` | Silent alarm | Alarm event |

### Independent state axes

Section ID: `ownkb:section:d000075:s000002`

Provenance cues: `evidence`

A central-unit status response can contain several of these values in one response transaction. For example, system activation, engagement, battery state and network state are independent properties rather than mutually exclusive members of one enumeration.

Zone state is represented separately: `WHAT 11` reports an engaged/active zone and `WHAT 18` a divided/non-active zone. Alarm frames such as `15`, `16`, and `17` then identify alarm conditions associated with the target selected by `WHERE`.

The labels follow the published `WHO 5` vocabulary. No additional numeric meanings are assigned without implementation or wire evidence.

# Document: ownkb:document:d000076

Source path: `functional/who-6-basic-video-door-entry/README.md`
Namespace context: `who:6`
Area: `functional`

## `WHO 6` - Basic Video Door Entry

Section ID: `ownkb:section:d000076:s000001`

Provenance cues: `catalogue`

`WHO 6` identifies the Basic Video Door Entry system in the known OpenWebNet namespace catalogue.

### Corpus status

Section ID: `ownkb:section:d000076:s000002`

Applicability cues: `version`
Cautions: `must not`
Provenance cues: `evidence`, `source`, `specification`

The corpus includes the [L4686SDK Specification](../../sources/openwebnet-public/pdf/WHO_6_L4686SDK.pdf), version 1.0.0 dated 11 February 2009. Its eight pages contain `WHO 6` command/address tables and send/receive flows for cameras, calls, locks, and stair lighting. This is product-specific published evidence, not merely a namespace record and not a complete generic Video Door Entry specification.

The reference below preserves the source's product scope. Values from adjacent Video Door Entry systems must not be substituted for the L4686SDK evidence.

### L4686SDK reference

Section ID: `ownkb:section:d000076:s000003`

Applicability cues: `scs`
Cautions: `not evidence`
Provenance cues: `evidence`, `source`

The command table and sections 1 and 2 establish these forms. Placeholders are symbolic, not captures.

| Operation | Published form | Applicability |
| --- | --- | --- |
| Camera ON | `*6*0*WHERE##` | `WHERE = 4000..4095`; riser form appends `#2` to `WHERE` |
| Camera OFF | `*6*9##` | No `WHERE` field in the published form |
| Stair light OFF / ON | `*6*11*WHERE##` / `*6*12*WHERE##` | L4686SDK address |
| Open lock | `*6*10*WHERE##` | `WHERE = 4000..4095`; riser form appends `#2` |
| Camera cycling | `*6*18*WHERE##` | `WHERE = 4000..4095`; source requires a preceding Camera ON; riser form appends `#2` |
| Incoming apartment call | `*6*6*WHERE##` | Receive section: `WHERE = 0..3999` |
| Incoming broadcast call | `*6*6*4100##` | Receive section; special value outside the endpoint range |
| Open lock with external unit in conversation | `*6*22*WHERE##` | Receive section: `WHERE = 4000..4095`; not evidence of a send operation |

For sending, the source describes ACK as confirmation that a frame was sent on the SCS bus, NACK as not sent, and `*#*x##` as an error-type form. It does not enumerate the `x` codes or establish the final physical effect. These are product-specific acknowledgement semantics.

### Source limits

Section ID: `ownkb:section:d000076:s000004`

Cautions: `do not`, `must not`
Provenance cues: `evidence`

The address table labels `4001` as endpoint 2 even though the adjacent entries suggest a different arithmetic correspondence. Preserve `4000..4095` as the stated wire range; do not infer an endpoint-number conversion from this inconsistent label.

Several response/receive rows print arrows inconsistent with their section headings and descriptions. The table above reports the sending/receiving section roles, not a repaired observed transcript. Exact direction and error-code behavior require product evidence. Camera OFF's short form and broadcast-call sentinel must not be normalized into the ordinary three-field command grammar.

### Protocol boundary

Section ID: `ownkb:section:d000076:s000005`

Provenance cues: `specification`

`WHO 6`, [`WHO 7`](../who-7-multimedia-video/), and [`WHO 8`](../who-8-video-door-entry-telephony/) are related by application domain but are independent protocol namespaces. A camera/video operation documented for `WHO 7`, for example, is not automatically valid under `WHO 6`.

Future values should be added only when supported by the MyHOME_Suite implementation corpus, a canonical specification, or observed wire behavior. Common frame syntax remains defined under [Protocol](../../protocol/).

# Document: ownkb:document:d000077

Source path: `functional/who-7-multimedia-video/README.md`
Namespace context: `who:7`
Area: `functional`

## `WHO 7` - Multimedia System

Section ID: `ownkb:section:d000077:s000001`

Provenance cues: `catalogue`

`WHO 7` controls cameras from the Video Door Entry catalogue: video-resource acquisition/release, image adjustment, and display DIAL selection.

### `WHAT` values

Section ID: `ownkb:section:d000077:s000002`

| `WHAT` | Function |
| --- | --- |
| `0` | Receive video |
| `9` | Release audio/video resources |
| `120` / `121` | Zoom in / out |
| `130` / `131` | Increase / decrease zoom-centre X coordinate |
| `140` / `141` | Increase / decrease zoom-centre Y coordinate |
| `150` / `151` | Increase / decrease luminosity |
| `160` / `161` | Increase / decrease contrast |
| `170` / `171` | Increase / decrease colour |
| `180` / `181` | Increase / decrease image quality |
| `3RC`, with `R` and `C` each `1..4` | Select DIAL row `R`, position `C` |

The adjustment operations are relative. The `3RC` family is structural: `R` selects DIAL row and `C` selects position, both `1..4`.

### Camera addressing

Section ID: `ownkb:section:d000077:s000003`

Provenance cues: `documentation`, `source`

The published `WHERE` table lists cameras `4000..4099`, with the final two digits identifying camera `00..99`.

Individual command-flow tables state `WHERE=[4000-5000]`, which conflicts with the explicit address table. This documentation treats `4000..4099` as the established enumerated range and records the broader command-note range as a source inconsistency, not as proof that every value through `5000` is a camera.

### Frame shape

Section ID: `ownkb:section:d000077:s000004`

Applicability cues: `gateway`
Provenance cues: `specification`

The dedicated specification prints command/event frames with a trailing empty tag:

```text
*7*WHAT*WHERE*##
```

It also prints resource release as `*7*9**##`, with no camera address. An implementation targeting this dialect should preserve the empty field rather than normalizing blindly to the common three-tag form.

The gateway answers commands with `ACK` or `NACK`. Adjustment and DIAL operations are meaningful only in the context of an acquired/active video resource.

### Resource lifecycle

Section ID: `ownkb:section:d000077:s000005`

1. Request video with `WHAT 0` for the selected camera.
2. Apply zoom, position, image, or DIAL operations as supported.
3. Release audio/video resources with `WHAT 9`.

`WHAT 9` is resource management, not a camera OFF state.

### Namespace boundary

Section ID: `ownkb:section:d000077:s000006`

`WHO 7` remains distinct from Basic Video Door Entry [`WHO 6`](../who-6-basic-video-door-entry/), Video Door Entry/Telephony [`WHO 8`](../who-8-video-door-entry-telephony/), and sound [`WHO 16`](../who-16-sound-system/) / [`WHO 22`](../who-22-sound-diffusion/).

### Evidence basis

Section ID: `ownkb:section:d000077:s000007`

Provenance cues: `source`, `specification`

Values, addresses, trailing-empty-tag frames, and command sequences come from [`WHO 7` specification](../../sources/openwebnet-public/pdf/WHO_7.pdf). The source's address-range discrepancy is retained explicitly.

# Document: ownkb:document:d000078

Source path: `functional/who-8-video-door-entry-telephony/README.md`
Namespace context: `who:8`
Area: `functional`

## `WHO 8` - Video Door Entry and Telephony

Section ID: `ownkb:section:d000078:s000001`

`WHO 8` identifies the OpenWebNet Video Door Entry and telephony system. The current corpus establishes the namespace and a narrow MyHOME Suite service operation, but not a complete public functional grammar.

### Established implementation evidence

Section ID: `ownkb:section:d000078:s000002`

Provenance cues: `database`

`OPEN.db` records:

- functional `WHO 8`;
- diagnostic family `WHO 1008`;
- `managed = 1`;
- the F422 public-riser-interface address rule `1[I1][I2][I3][I4]`, with advanced form `1[I1I2I3I4]`;
- one system-associated generic identification template, `*[WHO]*[WHAT]##`, labelled `cmd_ident`.

The template establishes that MyHOME Suite associates a service-identification operation with this system. Because the database does not enumerate the substituted `WHAT` semantics here, it does not justify a `WHAT` table.

### Evidence boundary

Section ID: `ownkb:section:d000078:s000003`

Cautions: `do not`
Provenance cues: `evidence`, `specification`

The public corpus has no dedicated `WHO 8` specification. `WHO 6`, `WHO 7`, and `WHO 8` share an application domain but remain independent namespaces. Do not reuse `WHO 7` camera commands or addresses under `WHO 8` without direct evidence.

Diagnostic traffic belongs to `WHO 1008`; the numeric relationship does not make functional and diagnostic frames interchangeable.

### Decoder guidance

Section ID: `ownkb:section:d000078:s000004`

Uncertainty: `unknown`
Provenance cues: `database`, `specification`

Recognize the namespace, preserve unknown fields losslessly, and label only the address form and generic identification operation established above. Device-specific Video Door Entry behavior requires a canonical specification, a database template with resolved parameters, or observed traffic.

See [MyHOME Suite `OPEN.db` Coverage](../open-db-coverage.md), [`WHO 6`](../who-6-basic-video-door-entry/), and [`WHO 7`](../who-7-multimedia-video/).

# Document: ownkb:document:d000079

Source path: `functional/who-9-auxiliaries/README.md`
Namespace context: `who:9`
Area: `functional`

## `WHO 9` - Auxiliaries

Section ID: `ownkb:section:d000079:s000001`

`WHO 9` defines the OpenWebNet Auxiliaries system. Auxiliary channels provide general-purpose binary/event functions that can also appear as references from other systems, including the published `WHO 5` Alarm addressing model.

### Namespace semantics

Section ID: `ownkb:section:d000079:s000002`

Cautions: `do not`
Provenance cues: `specification`

`WHAT`, `WHERE`, and any structured values are scoped to `WHO 9`. An auxiliary number is not an Automation `A`/`PL` address and should not be normalized as one.

The Alarm specification's references to AUX targets demonstrate cross-system use of auxiliary channels, but do not make `WHO 9` part of the Alarm namespace. Integrations should preserve the originating `WHO` when correlating such events.

### Corpus status

Section ID: `ownkb:section:d000079:s000003`

Uncertainty: `unknown`
Provenance cues: `evidence`

The current integrated corpus establishes the Auxiliaries namespace and its use by MyHOME_Suite, but does not justify a complete independent `WHAT`/`DIMENSION` table beyond supported implementation evidence. Unknown values remain unspecified rather than inferred from generic binary-control behavior.

See [Protocol](../../protocol/) for common frame syntax and [`WHO 5` - Alarm](../who-5-alarm/) for Alarm-side AUX references.

# Document: ownkb:document:d000080

Source path: `functional/who-99-service-identification/README.md`
Namespace context: `who:99`
Area: `functional`

## `WHO 99` - Session and Service Identification

Section ID: `ownkb:section:d000080:s000001`

Uncertainty: `appears`

`99` appears in two related but differently evidenced roles:

1. the public connection workflow uses `*99*X##` to select an OpenWebNet session;
2. MyHOME Suite `OPEN.db` names functional namespace `WHO 99` **Service Identification**.

These facts must be preserved without inventing a broader functional vocabulary.

### Published session selectors

Section ID: `ownkb:section:d000080:s000002`

| Frame | Session |
| --- | --- |
| `*99*9##` | Commands/actions |
| `*99*1##` | Events |
| `*99*0##` | Programmed scenario |

These frames occur during connection setup after the server greeting. They omit the normal `WHERE` field and are parsed by the session state machine, not by an ordinary three-field functional dispatcher.

See [Connection and Sessions](../../protocol/sessions.md) for the complete workflow.

### `OPEN.db` namespace evidence

Section ID: `ownkb:section:d000080:s000003`

Applicability cues: `revision`
Provenance cues: `database`, `source`

`OPEN.db.EN_SYSTEM` contains a `WHO 99` row labelled Service Identification. It has no direct `AS_OPEN_SYSTEM` association to an `EN_OPEN` operation in this database revision.

The database therefore establishes the namespace label, but **does not** establish an additional service-identification `WHAT` table or show that every `*99*X##` value is valid. The published selectors above are the concrete operations supported by the current source corpus.

### Distinctions

Section ID: `ownkb:section:d000080:s000004`

Applicability cues: `gateway`
Provenance cues: `catalogue`

`WHO 99` session selection is not:

- gateway authentication (`WHO 98` declarations and challenge-response);
- a diagnostic Device interview;
- catalogue identity resolution;
- functional `WHO 8`'s parameterized service-identification association in `OPEN.db`.

Implementations should represent the raw numeric namespace while dispatching the published selector frames according to connection state.

### Evidence basis

Section ID: `ownkb:section:d000080:s000005`

Provenance cues: `specification`

The selector frames and order come from [OpenWebNet Introduction specification](../../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf). The Service Identification label and absence of an associated concrete operation come from `OPEN.db`; see [MyHOME Suite `OPEN.db` Coverage](../open-db-coverage.md).

# Document: ownkb:document:d000081

Source path: `internals/README.md`
Namespace context: `contextual`
Area: `internals`

## MyHOME Suite Internals

Section ID: `ownkb:section:d000081:s000001`

Provenance cues: `catalogue`, `database`

This section documents the MyHOME Suite 3.5.38 implementation data that connects catalogue capability, OpenWebNet management workflows, validation, and scenario-editor capabilities.

It describes the implementation represented by the preserved databases and support files. It does not claim a complete software-component architecture: the canonical corpus does not include application binaries, decompiled code, runtime traces of database access, or the format used to persist user-authored projects and scenarios.

### Reference

Section ID: `ownkb:section:d000081:s000002`

Applicability cues: `firmware`, `version`
Provenance cues: `catalogue`, `evidence`, `source`

| Subject | Page |
| --- | --- |
| Installed source locations, fingerprints, and version scope | [Installation and Source Layout](installation-and-source-layout.md) |
| Responsibilities and boundaries of each implementation store | [Data Store Responsibilities](data-store-responsibilities.md) |
| How systems, frames, sequences, address rules, and timers are represented | [OpenWebNet Registry and State Machines](openwebnet-registry-and-state-machines.md) |
| How product identity becomes firmware, Module, Object, and configuration capability | [Catalogue Resolution](catalogue-resolution.md) |
| How scenario-editor capabilities are represented and where execution evidence ends | [Scenario Capability Loading](scenario-capability-loading.md) |
| How catalogue, protocol, and linked-property constraints combine | [Validation Layers](validation-layers.md) |
| Resource keys, stored labels, UI terminology, and presentation boundaries | [Localization and Presentation](localization-and-presentation.md) |
| Established behavior, safe inferences, unknowns, and investigation priorities | [Implementation Boundaries](implementation-boundaries.md) |

### Implementation-data pipeline

Section ID: `ownkb:section:d000081:s000003`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`

MyHOME Suite combines several models rather than relying on one universal database:

1. identify a Physical Device and installed firmware from diagnostic traffic;
2. resolve product, Module, Object, and configuration capability in `MHCatalogue.db`;
3. select management frames, address rules, sequences, and timers from `OPEN.db`;
4. apply contextual catalogue filters and, where applicable, linked-property rules from `rules.db3`;
5. resolve scenario-editor commands independently from a ScenarioDevices database;
6. present resolved labels and editable fields through the application UI;
7. send frames and compare the resulting installed state with a new diagnostic read-back.

Each stage has its own identifiers. Equal integers across stores are not joins unless an explicit relationship, an unambiguous frame, or independently observed behavior establishes the correlation.

### Three different kinds of state

Section ID: `ownkb:section:d000081:s000004`

Provenance cues: `catalogue`, `evidence`

| State | Principal evidence | Meaning |
| --- | --- | --- |
| Capability | `MHCatalogue.db`, ScenarioDevices, `rules.db3` | what an implementation can offer in a resolved context |
| Workflow | `OPEN.db` and `OpenQuery.txt` | which frames, transitions, directions, and timers compose an operation |
| Installed state | diagnostic responses and project/UI observations | what one Device currently reports or what a project currently presents |

Confusing these layers produces common errors. A catalogue Object does not prove that a Module currently uses it. An `OPEN.db` template does not prove universal Device support. A scenario-editor action does not prove that every installed Device can execute it.

### Source authority

Section ID: `ownkb:section:d000081:s000005`

Applicability cues: `version`
Provenance cues: `database`, `source`

The canonical files and their SHA-256 fingerprints are registered in [`sources/manifest.yaml`](../sources/manifest.yaml). Database facts in this section describe that exact MyHOME Suite 3.5.38 source set; they are not protocol maxima or claims about later releases.

The public OpenWebNet documents remain authoritative for published functional frame semantics. MyHOME Suite implementation data adds unpublished management structures and editor capability, but differences must be retained as source/version differences rather than silently reconciled.

### Reading rule

Section ID: `ownkb:section:d000081:s000006`

Uncertainty: `unknown`
Provenance cues: `source`

Use the narrowest source that answers the question:

- functional frame meaning → [Functional reference](../functional/);
- common frame grammar → [Protocol](../protocol/);
- installed discovery and read-back → [Diagnostics](../diagnostics/);
- Device capability hierarchy → [Device Model](../device-model/);
- programming state changes → [Programming](../programming/);
- scenario-editor vocabulary → [Scenario Engine](../scenario-engine/);
- application data loading and boundaries → this section.

Implementation facts are labelled as established, implementation-derived, inferred, or unknown where the distinction matters.

# Document: ownkb:document:d000082

Source path: `internals/catalogue-resolution.md`
Namespace context: `contextual`
Area: `internals`

## Catalogue Resolution

Section ID: `ownkb:section:d000082:s000001`

Applicability cues: `firmware`

`MHCatalogue.db` is the principal product-capability model. It connects marketed Devices and SKUs to shared items, firmware definitions, Modules, Objects, Virgin Objects, configuration definitions, and contextual constraints.

### Principal capability path

Section ID: `ownkb:section:d000082:s000002`

Applicability cues: `firmware`
Provenance cues: `catalogue`

| Stage | Principal structure | Result |
| --- | --- | --- |
| Product | `EN_DEVICE` | branded Device record, standard name, and product code/SKU |
| Shared capability | `EN_ITEM` | item shared by one or more Device records |
| System identity | `AS_ITEM_SYSTEM` | catalogue system association and item-level `modobj` |
| Firmware | `EN_FIRMWARE`, `EN_BUILDS` | versioned capability definition |
| Object support | `AS_OBJECT_FIRMWARE` | Objects supported by one firmware |
| Module placement | `EN_SLOTS` | Object alternatives at Device-local `slot` positions |
| Configurable template | Virgin-Object association tables | permitted Object set before final assignment |
| Configuration | `EN_CONF` and related tables | properties, domains, filters, conditions, and conversions |

The conceptual model is **Physical Device → Firmware → Module → Object → Configuration**.

![Catalogue identity and capability model](../assets/diagrams/catalogue-capability.svg)

The diagram shows established catalogue relationships and association tables. It is a capability model: installed Device state still comes from diagnostics or a loaded project.

### Identity resolution

Section ID: `ownkb:section:d000082:s000003`

Applicability cues: `firmware`, `gateway`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `database`, `evidence`

A diagnostic identity response does not return an `EN_DEVICE` primary key. Resolution proceeds through meaning:

1. retain the raw diagnostic Device ID as an installed-instance identifier;
2. correlate `DIMENSION 1.OBJECT_MODEL` with `AS_ITEM_SYSTEM.modobj`;
3. correlate brand and line values with their catalogue model fields;
4. resolve the shared `EN_ITEM`;
5. enumerate candidate `EN_DEVICE` records and product codes;
6. use `EN_DEVICE.name` as the standard MyHOME Suite-facing Device description;
7. use firmware, hardware, UI, and product evidence to narrow the candidate set.

Several SKUs can share one item and firmware capability. Preserve the candidate set unless the evidence identifies one marketed product uniquely.

In the ordinary addressed Device form, `DIMENSION 1.N_CONF` is the second payload value, immediately after `OBJECT_MODEL`, and reports the number of physical configurator positions provided by the Device. This interpretation is corroborated by `OPEN.db`, catalogue configuration definitions, observed responses, and product diagrams; it is not an Object, Virgin Object, form factor, firmware class, or database key. The separate empty-`WHERE` gateway form is not covered by that interpretation: observed MH202 and F454 gateway tuples return `N_CONF = 15`, outside the ordinary `0..12` range, and its exact gateway semantics remain unresolved. See [`DIMENSION 1`: Device Identity](../diagnostics/dim1-device-identity.md#n_conf-and-physical-configurators).

### Firmware and Module resolution

Section ID: `ownkb:section:d000082:s000004`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`, `evidence`

An item can have multiple firmware definitions. Resolve the three-component `V.R.b` identity across `EN_FIRMWARE.firmware_V`, `EN_FIRMWARE.firmware_R`, and `EN_BUILDS.firmware_b`. The installed firmware response and default/localization metadata can narrow the choice, but the exact MyHOME Suite selection algorithm is not present in the canonical corpus.

An explicit component value of `-1` is strongly corroborated as **any or unspecified** for that component: the catalogue contains both `-1.-1.-1` defaults and concrete `V.R.-1` definitions. Preserve this as an inferred wildcard/default semantic, not as a proven precedence algorithm. Do not equate an explicit build of `-1` with the absence of an `EN_BUILDS` row. See [Firmware](../device-model/firmware.md#the--1-sentinel) for the evidence and counts.

Once firmware is resolved, `AS_OBJECT_FIRMWARE` gives supported Objects, `EN_SLOTS.first_slot` places Object alternatives, Virgin-Object associations describe configurable templates, and slot conditions can remove alternatives in a particular configuration.

Do not count `EN_SLOTS` rows as Modules: one `slot` can have several Object alternatives.

### Runtime Module projection

Section ID: `ownkb:section:d000082:s000005`

Cautions: `do not`
Provenance cues: `evidence`

`DIMENSION 30` selects the meaning of `KEYO` through `STATE`:

| `STATE` | `KEYO` namespace | Meaning |
| --- | --- | --- |
| `0` | `EN_KEY_OBJECT.key_object` | enabled Module; regular configured Object |
| `1` | `EN_VIRGIN_OBJECT.virgin_key_object` | disabled Module; Virgin Object and configurable role |

This is a state-dependent external identifier. The `DIMENSION 30` polarity is established by controlled diagnostic/programming evidence correlated with MyHOME_Suite UI behavior; it is neither `EN_KEY_OBJECT.id_key_object` nor `EN_VIRGIN_OBJECT.id_virgin_key_object`.

Use the same `slot` to attach `DIMENSION 32` address data and `DIMENSION 35` configuration values. Do not renumber protocol slots to match the UI.

### Configuration ownership

Section ID: `ownkb:section:d000082:s000006`

Applicability cues: `firmware`, `not applicable`

`EN_CONF` uses two exclusive ownership patterns:

| Scope | Key pattern |
| --- | --- |
| Object-scoped | resolved `id_key_object`; `id_firmware = 0` |
| Firmware-scoped | `id_key_object = 0`; resolved `id_firmware` |

The zero values are “not applicable” sentinels. Treating both columns as mandatory foreign keys would erase the ownership discriminator.

A complete property dictionary is the union of both scopes in the resolved Object/firmware context. The configuration `idx` is not globally unique; it becomes a meaningful `DIMENSION 35.INDEX` only after Device, firmware, Module, and Object context are known.

### Reconstructed relationships

Section ID: `ownkb:section:d000082:s000007`

Applicability cues: `revision`
Cautions: `do not`
Provenance cues: `catalogue`, `database`, `evidence`

Many catalogue relationships are not declared as SQLite foreign keys. They are supported by association-table structure, complete parent-key coverage in the canonical revision, consistent use across the capability graph, and diagnostic/UI corroboration.

Document these as reconstructed relationships. Do not alter the canonical database to make them appear declared.

One especially important exclusion is `EN_DEVICE.code`: it is a product code/SKU, not a reference to `EN_LANGUAGE.code`. Column-name similarity is not relational evidence.

### Physical-configuration resolution

Section ID: `ownkb:section:d000082:s000008`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Physical configuration is a firmware-contextual catalogue problem. The catalogue does not provide one global table that maps a raw configurator number to a universal meaning, nor does it require a hand-maintained topology table for each firmware.

#### Configuration-mode boundary

Section ID: `ownkb:section:d000082:s000009`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`

`EN_CONFIG_MODE` registers four distinct modes in the canonical catalogue:

| `id_config_mode` | Catalogue label | `config_mode` |
| --- | --- | --- |
| `1` | Virtual Configuration | `1` |
| `2` | Advanced Configuration | `2` |
| `3` | Physical configuration | `0` |
| `4` | Product Programming | `3` |

`AS_FIRMWARE_CONFIG_MODE` records which catalogue modes a firmware supports. Do not collapse Virtual Configuration and Advanced Configuration into one category merely because both are non-physical.

`OPEN.db` has a separate sequence vocabulary. In particular, `ConfConfigurators` is described as "To set device configurators, virtual configuration", while `ConfKO` is described as advanced configuration. Those labels establish the purpose of the registered programming workflows. They do not establish that sequence labels, catalogue mode records, and MyHOME Suite UI labels are interchangeable concepts.

#### Resolver inputs and outputs

Section ID: `ownkb:section:d000082:s000010`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `catalogue`

The catalogue resolver takes:

- one exact `EN_FIRMWARE.id_firmware`;
- a candidate physical configuration keyed by exact firmware configuration symbols;
- the firmware's Object/slot capability rows;
- the stored slot conditions and conversion rules for those rows.

It should return:

- whether Physical configuration is registered for the firmware;
- the relevant firmware configuration definitions and their legal domains;
- candidate Objects by internal `slot`;
- stored condition branches and whether each is reachable for this firmware;
- the Object selected for each internal `slot`, when selection is unique;
- applicable `EN_CONDITION.id_conv_rule` values and resulting Object-property conversions, where resolvable;
- explicit zero-match, multi-match, unsupported-expression, and unresolved states.

This is catalogue capability resolution. It does not prove that an installed Device is currently using Physical configuration.

#### 1. Establish Physical-mode support

Section ID: `ownkb:section:d000082:s000011`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `evidence`

Use the explicit firmware-to-mode association:

```sql
SELECT
    cm.id_config_mode,
    cm.descr,
    cm.config_mode
FROM AS_FIRMWARE_CONFIG_MODE AS fm
JOIN EN_CONFIG_MODE AS cm
  ON cm.id_config_mode = fm.id_config_mode
WHERE fm.id_firmware = :firmware_id
ORDER BY cm.id_config_mode;
```

Physical configuration is catalogue-supported when the result contains the distinct `Physical configuration` record. Mode support is a firmware capability, not installed-state evidence.

#### 2. Resolve exact configurator definitions and legal domains

Section ID: `ownkb:section:d000082:s000012`

Applicability cues: `firmware`
Uncertainty: `appears`
Provenance cues: `catalogue`, `evidence`

Demonstrated physical firmware fields in the canonical catalogue are firmware-scoped `EN_CONF` rows with `idx = -1`, making that structure a useful candidate set. It is not a sufficient physical-position test: the common `AID`/ID row is also firmware-scoped with `idx = -1` but is not a literal physical configurator. For topology resolution, parse the symbols used by explicit physical slot predicates and resolve those symbols to the exact firmware definitions. Treat additional `idx = -1` rows as candidate metadata unless independent canonical evidence establishes their physical role.

Retrieve each definition together with its domain:

```sql
SELECT
    c.id_conf,
    c.conf_name,
    c.descr,
    c.descr_ext,
    c.id_conf_type,
    ct.descr AS conf_type,
    c.id_conf_data_type,
    dt.data_type,
    c.progressive,
    c.idx,
    r.value,
    r.name AS value_name,
    r.descr_ext AS value_description,
    r."default" AS default_value,
    r.min_value,
    r.max_value,
    r.step
FROM EN_CONF AS c
LEFT JOIN EN_CONF_TYPE AS ct
  ON ct.id_conf_type = c.id_conf_type
LEFT JOIN EN_CONF_DATA_TYPE AS dt
  ON dt.id_conf_data_type = c.id_conf_data_type
LEFT JOIN EN_CONF_RANGE AS r
  ON r.id_conf = c.id_conf
WHERE c.id_firmware = :firmware_id
  AND c.id_key_object = 0
  AND c.idx = -1
ORDER BY c.progressive, r.progressive, r.id_conf_range;
```

Interpret a raw physical value only through the exact `EN_CONF.id_conf` selected in the firmware context. Conceptually, the lookup key is:

```text
firmware + exact EN_CONF definition + raw value
```

not:

```text
raw value -> universal configurator meaning
```

The canonical data demonstrates why. In firmware `145`, raw `14` means `AMB` for `A1` and `A2`, but `CEN` for `M1` and `M2`. Raw `15` means `AUX` on those `A` fields and `PUL` on the `M` fields. Elsewhere in the catalogue, raw `14` also appears as `UP/DOWN monostable` for `PL` fields. Numeric equality therefore carries no universal configurator semantics.

#### 3. Enumerate Object/slot candidates

Section ID: `ownkb:section:d000082:s000013`

Applicability cues: `firmware`
Cautions: `do not`
Uncertainty: `appears`
Provenance cues: `database`

`AS_OBJECT_FIRMWARE` supplies Objects supported by the firmware. `EN_SLOTS` places those Object/firmware associations at Device-local `slot` positions:

```sql
SELECT
    s.id_slot,
    s.first_slot,
    s.fixed_ko,
    ofw.id_object_firmware,
    ofw.id_key_object,
    ko.key_object,
    ko.descr AS object_description
FROM AS_OBJECT_FIRMWARE AS ofw
JOIN EN_KEY_OBJECT AS ko
  ON ko.id_key_object = ofw.id_key_object
JOIN EN_SLOTS AS s
  ON s.id_object_firmware = ofw.id_object_firmware
WHERE ofw.id_firmware = :firmware_id
ORDER BY s.first_slot, ko.key_object, s.id_slot;
```

These rows are candidate capability placements. `AS_OBJECT_FIRMWARE.id_key_object` is the database-local key; join `EN_KEY_OBJECT` before presenting the external Object number `key_object`. Several Objects can share one `first_slot`. Do not choose an Object because it appears first, has the lowest identifier, or has `fixed_ko` set.

#### 4. Retrieve stored selection branches

Section ID: `ownkb:section:d000082:s000014`

Provenance cues: `catalogue`, `source`

Attach the stored slot conditions:

```sql
SELECT
    s.id_slot,
    s.first_slot,
    s.fixed_ko,
    ofw.id_object_firmware,
    ofw.id_key_object,
    ko.key_object,
    ko.descr AS object_description,
    sc.id_condition,
    c.condition,
    c.id_conv_rule
FROM AS_OBJECT_FIRMWARE AS ofw
JOIN EN_KEY_OBJECT AS ko
  ON ko.id_key_object = ofw.id_key_object
JOIN EN_SLOTS AS s
  ON s.id_object_firmware = ofw.id_object_firmware
LEFT JOIN AS_SLOT_CONDITION AS sc
  ON sc.id_slot = s.id_slot
LEFT JOIN EN_CONDITION AS c
  ON c.id_condition = sc.id_condition
WHERE ofw.id_firmware = :firmware_id
ORDER BY s.first_slot, ko.key_object, c.id_condition;
```

A non-empty `EN_CONDITION.condition` is an explicit catalogue predicate associated with an Object/slot candidate. In the canonical data, physical branches commonly use semicolon-separated conjunctions containing `=` and `<>`, for example `M1=CEN;M2=O/I`.

A machine resolver can implement the condition forms actually represented in the source. It must fail closed on syntax it does not understand rather than inventing an interpretation.

Empty condition rows and candidates with no `AS_SLOT_CONDITION` row remain catalogue capability metadata. Their lack of a predicate is not, by itself, an instruction to activate that Object under a physical configuration.

#### 5. Apply legal-domain reachability before matching

Section ID: `ownkb:section:d000082:s000015`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `database`

A stored condition is not automatically a legal physical branch for the selected firmware. Parse every symbol referenced by a condition, resolve it to the exact firmware `EN_CONF` definition, and constrain it by that definition's `EN_CONF_RANGE`.

A branch is unreachable when its predicate has no solution inside the firmware's legal domains. For example, an equality to a symbolic value that the exact firmware definition does not permit is unreachable even if the shared condition row exists in the database.

This filtering is required before topology selection:

```text
stored condition
    -> legal firmware configurator value
    -> reachable physical condition
    -> selected Object/slot topology
```

Keep unreachable rows as provenance. Do not delete or reinterpret them merely because they cannot occur on the firmware currently being resolved.

#### 6. Evaluate the candidate physical configuration

Section ID: `ownkb:section:d000082:s000016`

Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `evidence`

Normalize each supplied physical value through its exact `EN_CONF_RANGE` so the resolver retains both raw value and catalogue symbolic meaning. Evaluate every reachable explicit predicate against that normalized configuration.

Group satisfied branches by `EN_SLOTS.first_slot`:

- one distinct satisfied Object candidate: condition-selected Object;
- no satisfied Object candidate: zero-match result;
- more than one distinct satisfied Object candidate: ambiguous result;
- unsupported condition syntax or unresolved symbol: unresolved result.

Do not invent a precedence rule to break ambiguity. Multiple condition rows that select the same Object/slot association are branch evidence for the same candidate, not separate Objects.

#### 7. Separate topology selection from property conversion

Section ID: `ownkb:section:d000082:s000017`

Applicability cues: `firmware`
Cautions: `do not`

Topology selection answers:

> Which Object alternative is selected at each `slot` by the physical configuration?

Property conversion is a later operation:

> Given the selected Object and physical/item values, what Object-level configuration values result?

Do not merge these operations.

For each satisfied condition that supplies `EN_CONDITION.id_conv_rule`, retrieve the conversion rows:

```sql
SELECT
    id_conv_rule,
    item_conf,
    item_conf_value,
    object_conf,
    object_conf_value,
    always_true,
    jump_id_conv_rule,
    id
FROM EN_CONV_RULE
WHERE id_conv_rule = :conv_rule_id
ORDER BY id;
```

Apply item-side predicates only in the established physical configuration context, follow `jump_id_conv_rule` according to the stored rule data, and validate any produced Object value against the selected Object's effective domain. If the selected Object/firmware association has `EN_FILTER` and `EN_FILTER_RANGE` rows for the produced property, apply those contextual restrictions after the Object has been selected; they constrain that Object implementation's effective property domain and are not topology-selection edges.

`CONF_SYMBOL_REF` can provide an explicit item-symbol to Object-symbol correspondence for one `key_system` and `slot`:

```sql
SELECT
    item_conf_symbol,
    ko_conf_sysmbol,
    key_system,
    slot,
    descr
FROM CONF_SYMBOL_REF
WHERE item_conf_symbol = :item_symbol
  AND key_system = :key_system
ORDER BY slot, id;
```

The table has no firmware column. Use it only when the system and slot context are independently established. It is not a global symbol-alias table.

#### Worked example: firmware `157`

Section ID: `ownkb:section:d000082:s000018`

Applicability cues: `firmware`, `scs`
Cautions: `do not`
Provenance cues: `catalogue`, `database`, `evidence`, `source`

Firmware `157` demonstrates the generic procedure; it is not a firmware-specific rule embedded in the resolver.

The catalogue registers four `slot` positions and associates this firmware with Virtual Configuration, Advanced Configuration, and Physical configuration. Its relevant firmware-scoped physical definitions are:

| Symbol | `progressive` | Legal physical domain |
| --- | --- | --- |
| `A1` | `1` | `0..9` |
| `PL1` | `2` | `0..9` |
| `M1` | `3` | `0..8`; `9 = O/I`; `10 = OFF`; `12 = UP/DOWN`; `13 = UP/DOWN monostable`; `14 = CEN`; `15 = PUL` |
| `A2` | `4` | `0..9` |
| `PL2` | `5` | `0..9` |
| `M2` | `6` | same stored domain as `M1` |

The firmware also owns `AID` at `progressive = 0`. That is an ID field, not one of the six physical configurator positions above.

Candidate placements include Objects `6`, `7`, `400`, `401`, `404`, and `406` across the four slots. The explicit physical condition rows narrow those candidates.

For the representative physical configuration:

```text
M1=CEN
M2=O/I
```

the matching canonical branches are:

| `slot` | Selected Object | Condition | `id_conv_rule` |
| --- | --- | --- | --- |
| `1` | `6` | `M1=CEN;M2=O/I` | `25` |
| `2` | `6` | `M1=CEN;M2=O/I` | `25` |
| `3` | `400` | `M1=CEN;M2=O/I` | `4` |
| `4` | `400` | `M1=CEN;M2=O/I` | `4` |

The condition-selected topology is therefore `[6, 6, 400, 400]`.

`AS_KO_CMD_KO_DEV` independently associates `key_object_cmd = 400` (`key_object_cmd_desc = Light Double Command`) with `key_object_dev = 6` (`key_object_dev_desc = Actuator Scs Lights`). In the slot capability rows, the corresponding `EN_KEY_OBJECT.key_object` values are described as `Light control` and `Light actuator`. Keep those description fields in their source namespaces. The association is catalogue family evidence; it does not encode a per-instance or per-slot edge such as "slot 1 is hard-linked to slot 3", so no such linkage follows from this example.

The same firmware demonstrates why reachability is mandatory. Its `A2` domain is only `0..9`, while stored slot conditions also contain branches such as `A2=AMB`, `A2=GR`, `A2=GEN`, and `A2=AUX`. Those are stored catalogue conditions but cannot be satisfied by firmware `157`'s legal `A2` domain. Some stored branches also reference an `M2=ON` value that is absent from firmware `157`'s `M2` domain.

The selected branches point to conversion rules `25` and `4`. Preserve those rule IDs and evaluate their rows only after Object selection. Rule `4` has direct matching rows for this candidate configuration: `M1=CEN` produces values `1` and `2` for the two stored `CEN_BUTT` Object-property symbols, while `M2=O/I` produces `M = 9`. The canonical `EN_CONV_RULE.object_conf` strings for the two `CEN_BUTT` rows contain trailing whitespace; preserve the raw strings when implementing exact database matching rather than silently trimming them. This still demonstrates that one physical selector can contribute to more than one resulting Object property.

Rule `25` also belongs to the selected actuator branch, but the canonical data contains a textual irregularity: the physical domain and condition use `O/I`, while the relevant rule-`25` item rows use `I/O`. Do not silently normalize those tokens or claim the corresponding rule-`25` outputs for this input unless canonical evidence establishes equivalence.

#### `DIMENSION 4` and `5` are a transport boundary

Section ID: `ownkb:section:d000082:s000019`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`

`OPEN.db` defines:

```text
*#[WHO]*[WHERE]*4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##
*#[WHO]*[WHERE]*5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##
```

Each `C1..C12` parameter has the transport range `0..255`. The `ConfConfigurators` sequence sends the corresponding `#4` and `#5` programming forms and is described as virtual configuration in `OPEN.db`.

Those are canonical transport facts. `MHCatalogue.db` separately defines firmware-specific symbols, legal domains, conditions, and conversions.

The two databases contain no explicit relation establishing, for every firmware:

```text
DIMENSION 4.C1 = EN_CONF.progressive 1
```

or an equivalent positional rule. `EN_CONF.progressive` can resemble physical ordering in examples, but that resemblance is not a cross-database key. Not every firmware-owned `EN_CONF` definition represents a literal physical plug position. Keep transport position and catalogue configuration definition as separate namespaces until a correlation is independently established.

#### `EN_PHY_TO_ADV_TRANS` boundary

Section ID: `ownkb:section:d000082:s000020`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `evidence`

The canonical `EN_PHY_TO_ADV_TRANS` table contains only three rows, for firmware IDs `160`, `691`, and `722`. Firmware `157` has no row.

This table is useful evidence for those three recorded cases. It is not the generic physical-to-advanced or physical-to-topology mechanism. The wider catalogue mechanism is represented by firmware-specific `EN_CONF` domains, Object/slot candidates, slot predicates, `EN_CONDITION.id_conv_rule`, `EN_CONV_RULE`, filters, and contextual symbol references.

#### Resolution pseudocode

Section ID: `ownkb:section:d000082:s000021`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `evidence`

```text
function resolve_physical_configuration(firmware_id, physical_values):
    firmware = require_exact_EN_FIRMWARE(firmware_id)

    modes = load_AS_FIRMWARE_CONFIG_MODE(firmware_id)
    if Physical_configuration not in modes:
        return unsupported_physical_configuration

    definitions = load_firmware_EN_CONF_with_ranges(firmware_id)
    candidates = load_AS_OBJECT_FIRMWARE_and_EN_SLOTS(firmware_id)
    branches = load_AS_SLOT_CONDITION_and_EN_CONDITION(candidates)

    parsed = []
    referenced_symbols = set()
    for branch in branches with nonempty condition:
        ast = parse_supported_condition_grammar(branch.condition)
        if ast is unsupported:
            mark branch unresolved
            continue
        parsed.append(branch, ast)
        referenced_symbols += symbols(ast)

    physical_defs = {}
    for symbol in referenced_symbols union supplied_symbols(physical_values):
        matches = firmware_EN_CONF_definitions_named(definitions, symbol)
        if count(matches) != 1:
            mark symbol unresolved
            continue
        physical_defs[symbol] = matches[0]

    normalized = {}
    for supplied symbol/value:
        definition = require_resolved_definition(physical_defs, symbol)
        normalized[symbol] = decode_with_EN_CONF_RANGE(definition, value)
        if value not in definition.legal_domain:
            return invalid_physical_value

    reachable = []
    for branch, ast in parsed:
        if any referenced symbol is unresolved:
            mark branch unresolved
            continue
        if predicate_has_no_solution(ast, physical_defs):
            mark branch unreachable
            continue
        reachable.append(branch)

    selected = evaluate_reachable_branches(reachable, normalized)

    for internal_slot:
        distinct_objects = selected objects for internal_slot
        if count(distinct_objects) == 0:
            report zero-match
        else if count(distinct_objects) > 1:
            report ambiguous
        else:
            retain selected Object and satisfied condition

    for selected branch with id_conv_rule:
        evaluate EN_CONV_RULE after Object selection
        use CONF_SYMBOL_REF only in matching system/slot context
        revalidate produced Object values

    return topology, converted properties, provenance, and error states
```

The resolver should retain candidate rows, rejected unreachable branches, satisfied predicates, conversion-rule paths, and unresolved expressions as provenance. A successful catalogue result remains capability evidence rather than proof of Device runtime behavior.

For the conceptual model, see [Configuration](../device-model/configuration.md). For installed read-back, see [Diagnostics](../diagnostics/).

# Document: ownkb:document:d000083

Source path: `internals/data-store-responsibilities.md`
Namespace context: `contextual`
Area: `internals`

## Data Store Responsibilities

Section ID: `ownkb:section:d000083:s000001`

MyHOME Suite separates product capability, protocol workflows, scenario-editor vocabulary, and selected cross-property validation into different stores. No single file is a complete model of the installation.

### Responsibility matrix

Section ID: `ownkb:section:d000083:s000002`

Applicability cues: `firmware`
Provenance cues: `capture`, `catalogue`, `database`, `evidence`

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

### Composition, not a global join

Section ID: `ownkb:section:d000083:s000003`

Applicability cues: `firmware`, `version`
Provenance cues: `catalogue`, `database`

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

### Capability versus instance data

Section ID: `ownkb:section:d000083:s000004`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `evidence`, `source`

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

### Read-only evidence corpus

Section ID: `ownkb:section:d000083:s000005`

Applicability cues: `only for`
Provenance cues: `documentation`, `evidence`

The repository copies are evidence, not a working MyHOME Suite installation. They must be opened read-only for analysis.

SQLite foreign-key declarations are not uniform across stores. ScenarioDevices declares its principal hierarchy foreign keys; many important `MHCatalogue.db` relationships are reconstructed from complete key coverage and association structure. Documentation must distinguish a declared constraint from a corroborated relationship.

### Failure policy

Section ID: `ownkb:section:d000083:s000006`

Cautions: `do not`
Uncertainty: `unknown`, `unresolved`
Provenance cues: `source`

When a required correlation is missing, retain raw identifiers and source provenance, return an ambiguous or unresolved result, and do not select the first equal integer or widen a value domain to the protocol transport maximum.

Diagnostics can preserve unknown values. Programming should fail closed until the required context is resolved.

# Document: ownkb:document:d000084

Source path: `internals/implementation-boundaries.md`
Namespace context: `contextual`
Area: `internals`

## Implementation Boundaries

Section ID: `ownkb:section:d000084:s000001`

Provenance cues: `evidence`

This page separates facts directly recoverable from the canonical MyHOME Suite 3.5.38 data from interpretations that need runtime or application-code evidence.

### Evidence levels

Section ID: `ownkb:section:d000084:s000002`

Uncertainty: `unknown`
Provenance cues: `evidence`

| Level | Use |
| --- | --- |
| Established | direct schema, stored value, declared relationship, exact frame, fingerprint, or observed behavior |
| Implementation-derived | stable meaning recovered from complete data patterns, resource keys, or workflow composition |
| Inferred | best explanation of a complete pattern without an explicit declaration |
| Unknown | evidence is absent, conflicting, or supports several explanations |

An inference should state both its supporting pattern and the observation that could disprove it.

### Established boundaries

Section ID: `ownkb:section:d000084:s000003`

The preserved corpus establishes that MyHOME Suite distributes several independent SQLite stores; `OPEN.db` models systems and workflows; `OpenQuery.txt` names selected reads but is incomplete; `MHCatalogue.db` models capability and contextual constraints; ScenarioDevices models scenario-editor capability rather than complete scenario graphs; and `rules.db3` adds linked-property rules for selected Temperature Control Objects.

### Safe implementation-derived conclusions

Section ID: `ownkb:section:d000084:s000004`

Applicability cues: `gateway`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `evidence`

The combined evidence supports these conclusions when their scope is retained:

- `OPEN.db` scenarios and sequences form state-machine definitions for MyHOME Suite management workflows;
- diagnostic/programming `DIMENSION 30.KEYO` uses the regular configured Object namespace for an enabled Module when `STATE = 0` and the Virgin Object namespace for a disabled Module when `STATE = 1`;
- ordinary addressed-form `N_CONF` represents the number of physical configurator positions on corroborated products; the empty-`WHERE` gateway variant is separate, with observed `N_CONF = 15` outside the ordinary `0..12` range and unresolved exact semantics;
- the two ScenarioDevices files are distinct revisions whose common semantic content overlaps despite unstable local IDs;
- literal ScenarioDevices action templates can be rendered only after functional address and Parameter validation;
- catalogue programming validation is context-sensitive and cannot be reduced to `OPEN.db` transport ranges.

These conclusions do not establish universal support across all MyHOME releases or Devices.

### Runtime questions still open

Section ID: `ownkb:section:d000084:s000005`

Applicability cues: `firmware`, `version`
Provenance cues: `catalogue`, `database`, `evidence`

| Question | Evidence needed |
| --- | --- |
| Which ScenarioDevices copy does MyHOME Suite open, and under what conditions? | file-access trace, decompiled loader, or controlled file substitution |
| Are Program Files and ProgramData copies synchronized or migrated? | installation/update trace and before/after fingerprints |
| How are database results cached and invalidated? | process trace or application code |
| Which component resolves ScenarioDevices resource keys? | resource bundles and call-site analysis |
| Where are user-authored project and scenario graphs persisted? | controlled project diff or traced save operation |
| How are frame-absent scenario events mapped to runtime input? | runtime trace and event-dispatch code |
| What enumerations back `WhereType`, `Type`, and `OperatorType`? | application enum definitions or exhaustive UI/runtime correlation |
| How is the installed firmware row selected when several catalogue rows match? | controlled Device/version tests or loader code |
| Are `DIMENSION 4` and `5` values presence flags, raw configurator codes, or another encoding? | captures across known physical configurator layouts |
| How are the separately selected address-rule columns consumed? | traced query execution and consumer behavior |

### Investigation rules

Section ID: `ownkb:section:d000084:s000006`

Uncertainty: `may`
Provenance cues: `evidence`

A future implementation investigation should fingerprint the exact release, monitor file opens and SQLite statements without modifying evidence, make one controlled UI change at a time, diff persistence before and after, correlate traffic by timestamp and semantic path, and record negative evidence.

Private captures can support conclusions but should not be committed because they may contain installation identifiers and network details.

### Documentation placement

Section ID: `ownkb:section:d000084:s000007`

Uncertainty: `unresolved`
Provenance cues: `evidence`

| Finding | Section |
| --- | --- |
| shared wire grammar | [Protocol](../protocol/) |
| functional `WHO` semantics | [Functional reference](../functional/) |
| Device capability hierarchy | [Device Model](../device-model/) |
| discovery and read-back | [Diagnostics](../diagnostics/) |
| state-changing workflows | [Programming](../programming/) |
| complete end-to-end task | [Practical Guides](../guides/) |
| scenario-editor capability | [Scenario Engine](../scenario-engine/) |
| application data loading and runtime boundary | MyHOME Suite Internals |
| method, competing hypotheses, and unresolved research | future `reverse-engineering/` section |

This separation prevents implementation evidence from being repeated as though it were a public protocol guarantee.

# Document: ownkb:document:d000085

Source path: `internals/installation-and-source-layout.md`
Namespace context: `contextual`
Area: `internals`

## Installation and Source Layout

Section ID: `ownkb:section:d000085:s000001`

Applicability cues: `version`
Cautions: `do not`
Provenance cues: `evidence`, `source`

The canonical MyHOME Suite source set was copied from a version 3.5.38 installation. Original Windows paths are evidence of packaging location; they do not by themselves establish which copy is opened first, whether data is copied or synchronized at runtime, or whether a file is writable during normal use.

### Preserved implementation files

Section ID: `ownkb:section:d000085:s000002`

| Repository file | Original installation path | Size | SHA-256 |
| --- | --- | --- | --- |
| `MHCatalogue.db` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_MHCatalogue\MHCatalogue.db` | 2,625,536 | `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5` |
| `OPEN.db` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\db\OPEN.db` | 80,896 | `d864a4946b47c3671a74a6844cec4da605cf20b33ac14f49959785778f104051` |
| `ScenarioDevices-program-files.sqlite` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\ScenarioDevices.sqlite` | 35,840 | `2ce7ffe1286c3246271aed160116fe664407d9e8ff43595f50192e7d2ac85569` |
| `ScenarioDevices-programdata.sqlite` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_ScenarioDevices\ScenarioDevices.sqlite` | 34,816 | `cd3b9b67160f468cdbd30134357b8733c696aacd5d625129240dff6b79224fc3` |
| `rules.db3` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_KeyOThermoValidator\rules.db3` | 36,864 | `23b62e3bb7a11ede3f91561b63a1aaf39449da47025626a2c477e9833347cb06` |
| `OpenQuery.txt` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\db\OpenQuery.txt` | 3,661 | `104bc9fcd780799f3b6bb85f2510b1b0424747c30c315f0a04c93e88f4163c10` |

The installer is not redistributed. Its registered size is 599,437,936 bytes and its SHA-256 is `707D8A43A5296A1EA87C33F111E9269C8BBD0FE524AC5EFE87BDEDE8B6EB311B`. The recorded Authenticode signature is valid and identifies BTICINO S.P.A. as signer.

### Repository naming

Section ID: `ownkb:section:d000085:s000003`

Provenance cues: `source`

Both ScenarioDevices source files were originally named `ScenarioDevices.sqlite`. Their repository names record their distinct origins and prevent one from overwriting the other.

The names `program-files` and `programdata` are provenance labels, not asserted runtime roles. The Program Files copy is larger and contains additional capability rows, but that does not prove that it supersedes, migrates, or updates the ProgramData copy.

### File-format observations

Section ID: `ownkb:section:d000085:s000004`

Cautions: `do not`
Provenance cues: `database`, `documentation`, `source`

All five database files are SQLite databases. `OpenQuery.txt` is preserved as UTF-8 with a byte-order mark and CRLF line endings.

The canonical-source policy requires byte-for-byte preservation. Do not:

- add inferred foreign keys to a canonical database;
- normalize or translate stored values in place;
- replace an older-looking ScenarioDevices copy with the larger copy;
- change line endings or encoding in `OpenQuery.txt`;
- store project-specific packet captures under `sources/`.

Derived schemas, relationship maps, comparison output, and interpretations belong in documentation or reproducible analysis outside the canonical source directory.

### Version boundary

Section ID: `ownkb:section:d000085:s000005`

Applicability cues: `firmware`
Uncertainty: `may`
Provenance cues: `evidence`, `source`

All quantitative statements in this section are scoped to MyHOME Suite 3.5.38. A later installation may contain different Device and firmware coverage, revised management sequences or timer defaults, a different ScenarioDevices schema or capability set, or additional validation databases.

When comparing releases, identify rows by stable semantic context where possible and always preserve the source fingerprint. Local SQLite row IDs are not release-stable identifiers unless independent evidence establishes that stability.

### What installation paths do not prove

Section ID: `ownkb:section:d000085:s000006`

Provenance cues: `database`

The available corpus does not establish database open order, update or synchronization direction, cache invalidation behavior, application-module ownership, transaction boundaries for project edits, or where user-authored project and scenario graphs are persisted.

These remain runtime questions for a future traced or decompiled investigation.

# Document: ownkb:document:d000086

Source path: `internals/localization-and-presentation.md`
Namespace context: `contextual`
Area: `internals`

## Localization and Presentation

Section ID: `ownkb:section:d000086:s000001`

Provenance cues: `catalogue`

MyHOME Suite presentation combines stored catalogue text, resource keys, implementation metadata, and runtime/UI decisions. A protocol decoder should preserve those layers rather than collapsing them into one label.

### Label classes

Section ID: `ownkb:section:d000086:s000002`

Provenance cues: `catalogue`, `source`

| Concept | Preferred source | Notes |
| --- | --- | --- |
| Physical Device description | `EN_DEVICE.name` | standard MyHOME Suite-facing product description |
| Product code/SKU | `EN_DEVICE.code` | product identity, not a language key |
| Shared item description | `EN_ITEM.descr` | shared capability item, not necessarily a unique marketed product |
| Object description | `EN_KEY_OBJECT.descr` | logical function of one Module |
| Virgin Object description | `EN_VIRGIN_OBJECT.descr` | configurable role represented for a disabled Module in `DIMENSION 30` |
| Configuration label | `EN_CONF.descr`, `descr_ext`, and related metadata | property presentation in catalogue context |
| Scenario capability name | ScenarioDevices `Name` fields | commonly a localization/resource key, not final display text |
| Protocol operation label | `OPEN.db.EN_OPEN.open_label` | implementation operation label, not a public protocol name |

One Physical Device can have one standard Device description and several Module/Object descriptions. Displaying an Object description as the Device name loses the product-level identity.

### Resource keys

Section ID: `ownkb:section:d000086:s000003`

Applicability cues: `revision`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `database`, `evidence`, `source`

ScenarioDevices keys encode structure such as functional family, role, Object, and Command. They are useful stable evidence within a source revision, but their translated strings are not stored in the four capability tables.

A presentation layer should retain the source database and revision, raw resource key, resolved localized label if available, locale, fallback label, and unresolved-key status.

Do not compare capabilities solely through translated strings. Translation can change while the underlying resource key remains the same, and one key can occur in multiple category paths.

### UI numbering and `slot` positions

Section ID: `ownkb:section:d000086:s000004`

Provenance cues: `catalogue`

MyHOME Suite can hide `slot` positions or renumber visible Modules. The presentation layer must keep the protocol `SLOT`, catalogue placement, UI-visible Module number or name, and hidden/absent state as separate fields.

Never rewrite the Device-local `slot` to match the UI.

### Visibility and editability

Section ID: `ownkb:section:d000086:s000005`

Cautions: `do not`
Provenance cues: `catalogue`, `evidence`

Catalogue metadata such as `visible`, `hidden`, `read_only`, `fixed_ko`, and conditions contributes to UI behavior, but no one flag is a complete presentation rule.

A fixed Object can still expose editable configuration. A hidden property can participate in conversions. An Object alternative can exist in the catalogue but be suppressed by a `slot` condition. A `slot` can exist while being absent from a particular UI view.

Use observed UI behavior as presentation evidence and catalogue structures as capability evidence. Do not infer wire encoding from a label or widget alone.

### Terminology normalization

Section ID: `ownkb:section:d000086:s000006`

Cautions: `do not`
Provenance cues: `database`

Repository prose uses **Physical Device**, **Module**, **`slot`**, **Object**, **Configuration**, and **Virtual configuration**. Database names such as `KEYO`, `ko slot`, and `id_key_object` are retained when quoting fields, but do not replace reader-facing terminology.

### Unknown localization mechanism

Section ID: `ownkb:section:d000086:s000007`

The corpus establishes stored text and resource-key usage but does not preserve the complete resource bundle or application code that resolves every key. It therefore does not establish fallback locale order, missing-key behavior, runtime culture selection, or formatting rules for composed labels.

Document raw keys whenever the final localized string cannot be reproduced.

# Document: ownkb:document:d000087

Source path: `internals/openwebnet-registry-and-state-machines.md`
Namespace context: `contextual`
Area: `internals`

## OpenWebNet Registry and State Machines

Section ID: `ownkb:section:d000087:s000001`

`OPEN.db` is MyHOME Suite’s implementation registry for OpenWebNet systems and management workflows. It represents frame templates and their composition; it is not a complete copy of the public functional protocol.

### Registry layers

Section ID: `ownkb:section:d000087:s000002`

Cautions: `do not`

| Layer | Principal tables | Role |
| --- | --- | --- |
| Systems | `EN_SYSTEM` | functional namespace label, functional `WHO`, diagnostic `WHO`, and managed flag |
| System operations | `AS_OPEN_SYSTEM`, `EN_OPEN` | concrete frame templates associated with selected systems |
| Parameters | `AS_OPEN_PARAM`, `EN_OPEN_PARAM` | placeholder descriptions and transport constraints |
| Addressing | `AS_SYSTEM_ADDRESS_RULE`, `EN_ADDRESS_RULE` | system-specific Virtual and advanced address grammars |
| Scenarios | `EN_SCENARIO`, `AS_SCENARIO_SEQUENCE` | named high-level operations composed from sequences |
| Sequences | `EN_SEQUENCE`, `AS_OPEN_SEQUENCE` | ordered frames, direction-sensitive variants, repetition, and transition metadata |
| Timing | `AS_TIMEOUT_OPEN_SEQUENCE`, `EN_TIMEOUT` | timers, defaults, start/stop actions, and timeout transitions |

An `EN_SYSTEM` row proves namespace knowledge. It does not prove that `EN_OPEN` contains every functional command for that `WHO`.

![OPEN.db systems, frames, and workflow registry](../assets/diagrams/openwebnet-registry.svg)

The association tables carry ordering, repetition, direction-sensitive composition, and timeout context. Those properties do not belong to the frame template alone.

### State-machine assembly

Section ID: `ownkb:section:d000087:s000003`

Provenance cues: `database`

A management operation is resolved in two stages:

1. select an `EN_SCENARIO` and order its sequences through `AS_SCENARIO_SEQUENCE.sequence_order`;
2. for each selected `EN_SEQUENCE`, order its frame definitions through `AS_OPEN_SEQUENCE.open_order`.

Sequence metadata controls whether a frame is mandatory or repeated, its direction-sensitive registry row, and state changes for `NACK`, structured errors, and timeouts.

A repeated sequence association permits application-level repetition but does not encode the iteration count. Likewise, a repeated frame can collect or emit multiple rows, but the database does not determine how many a particular Device supports.

### Frame records

Section ID: `ownkb:section:d000087:s000004`

`EN_OPEN.open_string` stores parameterized frames such as diagnostic `DIMENSION 30`, programming `DIMENSION 35`, and session-control `WHAT` values. Related fields classify address and parameter presence, direction/type, diagnostic use, errors, and Object-programming use.

The same textual frame shape can appear in different directions or workflow contexts. Programmer and Device aborts, for example, share a wire form but are distinct registry rows. Always retain the `EN_OPEN` row, direction, active scenario and sequence, current Device selector, and last outstanding command.

The wire protocol has no transaction identifier that can recover this context after ambiguous pipelining.

### `OpenQuery.txt` as a data-access contract

Section ID: `ownkb:section:d000087:s000005`

Applicability cues: `gateway`, `scs`

`OpenQuery.txt` defines named SQL statements for selected registry reads:

| Query key | Data loaded |
| --- | --- |
| `systemDictQuery` | all systems ordered by internal system ID |
| `systemaddressruleDictQuery` | system/address-rule associations and rule fields |
| `openframeErrDictQuery` | frames marked as errors |
| `openframeabortconfQueryList` | programmer abort rows |
| `openframegatewayconnectionQueryList` | selected gateway-connection frames |
| `openframescsbusQuery` | the SCS-bus frame |
| `timeoutscsbusQuery` | SCS-bus timeout default |
| `scenarioQuery` | scenario identity and type by label |
| `scenseq1Query` | ordered sequence composition |
| `openseq1Query` | ordered frame composition plus selected parameter metadata |
| `opentimeoutQuery` | timeouts and transitions for a sequence |

The file records the columns and ordering MyHOME Suite intended to request. It does not prove when each query runs, how results are cached, or how application classes interpret every field.

### Incompleteness preserved in the source

Section ID: `ownkb:section:d000087:s000006`

Provenance cues: `evidence`, `source`, `specification`

The file itself records unfinished work:

- an Italian note says the sequence-only part still had to be defined;
- a second note says queries needed for scenario traversal were still missing;
- `openparamsQuery` is literally `TODO`;
- the operation-specific address-rule query is commented out.

These are source facts. `OpenQuery.txt` cannot be treated as a complete schema-access specification.

The preserved `systemaddressruleDictQuery` selects `ar.address_rule_adv` and `ar.level_2_rule` as separate comma-delimited columns. An earlier review attributed a bitwise expression to this file; direct inspection of the fingerprinted source disproved that attribution. Query execution and consumer behavior still require runtime evidence. The correction is recorded in the [Review Ledger](../project/review/ecv-esg-review-ledger.md#p3-prov-001---incorrect-openquery-source-attribution).

### Runtime algorithm

Section ID: `ownkb:section:d000087:s000007`

Provenance cues: `database`

A safe reimplementation should select the system and management family without numerically joining another database’s system ID; resolve the scenario by label; preserve sequence/frame order and repetition; bind only established parameters; create timers from timeout associations; serialize ambiguous requests; and classify terminal, error, `NACK`, and timeout transitions separately.

The concrete diagnostic and programming state machines are documented in [Diagnostics](../diagnostics/) and [Programming](../programming/).

# Document: ownkb:document:d000088

Source path: `internals/scenario-capability-loading.md`
Namespace context: `contextual`
Area: `internals`

## Scenario Capability Loading

Section ID: `ownkb:section:d000088:s000001`

Cautions: `do not`

The two ScenarioDevices databases are compact capability catalogues for the MyHOME Suite scenario editor. They are not inventories of installed Devices and do not contain the complete graph of a user-authored scenario.

### Two source revisions

Section ID: `ownkb:section:d000088:s000002`

Applicability cues: `revision`
Cautions: `must not`
Provenance cues: `source`

| Source | Object Systems | Device Objects | Commands | Parameters | Schema distinction |
| --- | --- | --- | --- | --- | --- |
| Program Files copy | 29 | 44 | 157 | 42 | includes `ObjectSystems.FamilyId` |
| ProgramData copy | 27 | 42 | 151 | 40 | no `FamilyId` |

The common semantic content of the ProgramData copy is an exact subset of the Program Files copy when compared by the complete hierarchy and non-local fields. Local row IDs diverge after added rows and must not be used as cross-file identities.

The larger revision adds two Virtual Key Card Object Systems, two Device Objects, four Virtual Key Card event Commands, two Temperature Control action Commands, and two Parameters belonging to those actions. This delta does not establish runtime precedence.

### Declared hierarchy

Section ID: `ownkb:section:d000088:s000003`

Provenance cues: `catalogue`, `source`

The files declare this hierarchy:

**Object System → Device Object → Command → Parameter**

| Relationship | Declared foreign key |
| --- | --- |
| Device Object to Object System | `DeviceObjects.ObjectSystem_Id → ObjectSystems.Id` |
| Command to Device Object | `Commands.DeviceObject_Id → DeviceObjects.Id` |
| Parameter to Command | `Parameters.Command_Id → Commands.Id` |

![ScenarioDevices capability hierarchy](../assets/diagrams/scenario-capability.svg)

Use local row primary keys only inside one source file.

`ObjectId`, `ObjectMatchingId`, `CommandId`, and `CommandMatchingId` are scenario-engine identifiers. They are not catalogue Object numbers or OpenWebNet fields without a separately established correlation.

### Resource-key-driven presentation

Section ID: `ownkb:section:d000088:s000004`

Provenance cues: `database`

Names such as `miniScenarioSuite.automation.action` are localization/resource keys. They carry useful implementation semantics, including functional family and editor role, but they are not final UI strings.

A consumer should retain both the raw key and any resolved display label. Never use a translated label as a database identity.

### Command classes

Section ID: `ownkb:section:d000088:s000005`

Applicability cues: `revision`
Cautions: `do not`
Provenance cues: `evidence`

| Class | Evidence | Safe treatment |
| --- | --- | --- |
| Literal frame | `Frame` parses as OpenWebNet and agrees with `ChiOpen` | validate address and Parameters, render, then reparse |
| Symbolic frame | non-null text that is not a literal frame | require an application-specific mapping |
| Frame-absent | `Frame IS NULL` | retain editor capability; do not invent an incoming frame |

In the larger revision, 57 Commands have literal OpenWebNet-shaped templates, five have symbolic text, and 95 have no stored frame. Most events and conditions are frame-absent; action rows more often contain renderable frames.

This proves that ScenarioDevices alone is not the incoming-event matcher or the full runtime engine.

### Capability resolution

Section ID: `ownkb:section:d000088:s000006`

Applicability cues: `revision`
Cautions: `do not`
Provenance cues: `source`

A safe loader selects one source revision explicitly; preserves categories and matching identifiers; loads all Commands and Parameters; classifies literal, symbolic, and frame-absent rows; validates literal `WHO` values against `ChiOpen`; interprets `WHERE` under the functional `WHO`; and returns source-file and row provenance.

Do not apply “first row wins” selection. The same resource key can occur in different category contexts.

### Missing scenario-instance layer

Section ID: `ownkb:section:d000088:s000007`

The four tables contain no complete representation of scenario instance identity, nodes and edges, branch or action ordering, persisted trigger bindings, condition state, retry policy, schedules, or active execution state.

Those concerns require another persistence format or application code not present in the canonical corpus.

The detailed schema, distributions, frame rendering, and open questions are documented in [Scenario Engine](../scenario-engine/).

# Document: ownkb:document:d000089

Source path: `internals/validation-layers.md`
Namespace context: `contextual`
Area: `internals`

## Validation Layers

Section ID: `ownkb:section:d000089:s000001`

Provenance cues: `catalogue`

MyHOME Suite validation spans several stores. Transport ranges, catalogue domains, contextual filters, conversion rules, and linked-property rules answer different questions and must be applied in order.

### Constraint layers

Section ID: `ownkb:section:d000089:s000002`

Applicability cues: `applies to`, `firmware`
Provenance cues: `catalogue`, `source`

| Layer | Source | Question answered |
| --- | --- | --- |
| Transport field | `OPEN.db` parameters | Can the encoded value fit the management frame? |
| Property definition | `EN_CONF`, `EN_CONF_RANGE` | What is the property’s base type and domain? |
| Object/firmware context | `EN_FILTER`, `EN_FILTER_RANGE` | Which subset applies to this Object implementation? |
| Slot applicability | `AS_SLOT_CONDITION`, `EN_CONDITION`, `EN_CONV_RULE` | Is this Object/property active, and how is its value converted? |
| Symbol mapping | `CONF_SYMBOL_REF` | Does an explicit item/Object symbol relationship exist in this context? |
| Linked properties | `rules.db3` | Do other properties enable, disable, or constrain this one? |
| Functional semantics | public protocol and observed behavior | Does the encoded value mean the intended operation? |
| Effective state | diagnostic read-back | Did the Device apply the intended configuration? |

The effective domain is the intersection of all applicable layers. A broad `OPEN.db` transport range never overrides a narrower catalogue rule.

![Configuration ownership and validation model](../assets/diagrams/configuration-validation.svg)

The diagram separates polymorphic property ownership from the contextual filters, slot conditions, and conversions that narrow or transform the base domain.

### Context first

Section ID: `ownkb:section:d000089:s000003`

Applicability cues: `firmware`

Validation begins only after resolving the Physical Device, firmware, `slot`, current Object or Virgin Object, target Object, and applicable Object/firmware association.

Without that context, a configuration `idx`, stored integer, or display label is insufficient.

### Base and contextual domains

Section ID: `ownkb:section:d000089:s000004`

Applicability cues: `firmware`
Uncertainty: `unresolved`

`EN_CONF_RANGE` can define named values, numeric bounds, step size, digit width, ordering, and defaults. A missing range row does not imply an unrestricted value.

`EN_FILTER` binds a configuration definition to an `AS_OBJECT_FIRMWARE` context. Related `EN_FILTER_RANGE` rows narrow the base domain for that exact Object/firmware association.

A safe evaluator retains `id_conf` and ownership scope, the raw candidate, base domain, selected filters, condition and conversion path, final encoded value, and unresolved dependencies.

### Conditions and conversions

Section ID: `ownkb:section:d000089:s000005`

Cautions: `do not`
Uncertainty: `unresolved`

Slot conditions can depend on other item-level or Object-level symbols. `EN_CONDITION` points into conversion-rule logic represented by `EN_CONV_RULE`.

Do not evaluate a rule with a partial candidate configuration. Missing inputs, ambiguous branches, or unmapped output make the result unresolved.

After conversion, validate the output again against the effective domain and frame transport field. Conversion does not make an excluded value valid.

### `rules.db3` boundary

Section ID: `ownkb:section:d000089:s000006`

Provenance cues: `database`

The canonical `rules.db3` contains additional linked-property rules for selected Temperature Control Objects. References such as `$1`, `$2`, or `$21` are configuration indexes only inside the resolved Object context.

The database is not a global Object registry, a mapping from every `WHO` to configuration, or a substitute for `MHCatalogue.db`.

A controlling-property change can disable another field through `DisablelinkedParameter` behavior. Recompute the affected property set rather than validating only the edited value.

### Read and write distinctions

Section ID: `ownkb:section:d000089:s000007`

Uncertainty: `may`, `unresolved`

A property can be writable, conditionally writable, fixed, read-only, hidden but semantically active, unsupported, or unresolved. Visibility is not permission.

Programming must validate the complete replacement state when the selected sequence begins with reset-all. Validating only the changed field is unsafe because omitted Modules or properties may not survive the transfer.

### Result model

Section ID: `ownkb:section:d000089:s000008`

Uncertainty: `unresolved`
Provenance cues: `source`

| Status | Meaning |
| --- | --- |
| valid | directly allowed in the complete resolved context |
| valid after conversion | allowed through an established conversion path |
| conditionally valid | valid while stated dependencies hold |
| fixed/read-only | part of effective state but not arbitrary input |
| invalid | excluded by an applicable constraint |
| ambiguous | several incompatible resolutions remain |
| unresolved | required source context or mapping is absent |

For the full programming algorithm, see [Programming Validation](../programming/validation.md). Practical SQL examples belong in [Practical Guides](../guides/), where they can be shown in an end-to-end task.

# Document: ownkb:document:d000090

Source path: `programming/README.md`
Namespace context: `contextual`
Area: `programming`

## Programming

Section ID: `ownkb:section:d000090:s000001`

Applicability cues: `zigbee`
Uncertainty: `not established`

The programming protocol changes the installed configuration of a Physical Device, its Modules, and their selected Objects. MyHOME_Suite combines OpenWebNet management frames from `OPEN.db` with capability and validation data from `MHCatalogue.db`.

Programming is distinct from diagnostics. Diagnostics reports installed state; programming requests a state change. A successful response is not a substitute for validation before transmission or diagnostic read-back afterward.

The canonical cross-area ownership of discovery, interview, configuration reading, runtime control, and programming is summarized in [OpenWebNet Scope and Architecture](../protocol/scope-and-architecture.md).

These are stored Suite management workflows, not established programming support on every OpenWebNet transport. The [ZigBee Interface](../protocol/zigbee-interface.md) exposes separate management and binding mechanisms; neither their existence nor shared functional namespaces establishes `ConfKO` compatibility.

### Reference

Section ID: `ownkb:section:d000090:s000002`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `source`

| Subject | Page |
| --- | --- |
| Programming families, layers, and source boundaries | [Programming Architecture](architecture.md) |
| Programming states, ordering, and termination | [Programming Session Lifecycle](session-lifecycle.md) |
| Selecting a Device by address, ID, or local interaction | [Device Selection](device-selection.md) |
| Selecting Objects for firmware Modules | [Object Programming](object-programming.md) |
| Programming functional addresses | [Address Programming](address-programming.md) |
| Programming indexed configuration values | [Configuration Programming](configuration-programming.md) |
| Evaluating catalogue ranges, filters, and conditions | [Programming Validation](validation.md) |
| Rejection, timeout, abort, and recovery | [Programming Error Handling](error-handling.md) |
| Diagnostic read-back and state comparison | [Programming Verification](verification.md) |
| Programming `WHAT` values | [Programming `WHAT` Reference](what-reference.md) |
| Programming `DIMENSION` values | [Programming `DIMENSION` Reference](dimension-reference.md) |

### Canonical scenarios

Section ID: `ownkb:section:d000090:s000003`

Cautions: `do not`
Provenance cues: `source`

`OPEN.db` defines three read/write programming scenarios:

| Scenario | Ordered sequences |
| --- | --- |
| `ConfPoint2PointByAddress` | `ConfAddressed` → `ConfConfigurators` → `CloseConf` |
| `ConfPoint2PointWithID` | `ConfPoint2PointWithID` → repeated `ConfKO` → `CloseConf` |
| `ConfLocalButton` | `ConfLocalButton` → repeated `ConfKO` → `ConfConfigurators` → `CloseConf` |

The scenario names preserve MyHOME_Suite terminology. “AID” in source descriptions refers to the 32-bit installed Device ID used by the `*[WHO]*9#[ID]*0##` start frame.

The scenarios expose two programming projections:

| Projection | Principal writes | `OPEN.db` description |
| --- | --- | --- |
| Virtual configurators | `DIMENSION 4` and `5` | set Device configurators |
| Advanced Object configuration | `DIMENSION 30`, `32`, and `35` | set Object, address, and indexed parameters |

These projections are not interchangeable. The address-selected scenario contains virtual-configurator transfer but no `ConfKO` sequence. The ID-selected scenario contains advanced Object transfer but no `ConfConfigurators` sequence. The local-interaction scenario contains both.

These names are `OPEN.db` programming-sequence terminology. `MHCatalogue.db` independently registers Virtual Configuration and Advanced Configuration as distinct configuration modes, along with Physical configuration and Product Programming. Do not use one source's label as an undocumented umbrella for the other source's concepts.

### Safe workflow

Section ID: `ownkb:section:d000090:s000004`

Applicability cues: `firmware`
Cautions: `do not`
Uncertainty: `may`
Provenance cues: `catalogue`

1. Resolve the diagnostic family and installed Physical Device.
2. Resolve its item, firmware, Modules, Objects, and Virgin Objects.
3. Validate every target Object, address, and parameter in the complete catalogue context.
4. Select the Device using the scenario appropriate to the operation.
5. Transfer only the frames belonging to that scenario and sequence.
6. Preserve warnings, errors, timeout, abort, and terminal responses.
7. Close the programming session.
8. Start a new diagnostic interview and compare the effective state.

Do not infer a programming method from a desired value alone. A value may be representable through physical, virtual, or advanced configuration while the canonical scenarios support different transfer mechanisms.

### Scope boundaries

Section ID: `ownkb:section:d000090:s000005`

Cautions: `do not`
Provenance cues: `capture`

This section documents programming state machines and writes. Reusable capability belongs under [Device Model](../device-model/); discovery and read-back belong under [Diagnostics](../diagnostics/); shared frame grammar belongs under [Protocol](../protocol/).

The public OpenWebNet PDFs define frame syntax and functional `WHO` behavior but do not define these MyHOME_Suite programming state machines. The authoritative implementation structure for this section is therefore `OPEN.db` plus `OpenQuery.txt`, interpreted with `MHCatalogue.db`, `rules.db3`, observed behavior, and the MyHOME_Suite UI.

Private captures are not stored in the repository. Capture-supported conclusions are stated without installation-specific transcripts.

# Document: ownkb:document:d000091

Source path: `programming/address-programming.md`
Namespace context: `contextual`
Area: `programming`

## Address Programming

Section ID: `ownkb:section:d000091:s000001`

Address programming assigns the effective functional system and address of one configured Module during advanced Object transfer.

### Write frame

Section ID: `ownkb:section:d000091:s000002`

`*#[WHO]*0*#32#[SLOT]*[SYS]*[ADDR]##`

`#32#[SLOT]` is the parameterized `DIMENSION` selector. The leading `#` selects the write form, and the following `#` attaches `SLOT` to that selector. `SYS` and `ADDR` are ordinary `DIMENSION` values separated with `*`.

| Field | `OPEN.db` range | Meaning |
| --- | --- | --- |
| `SLOT` | `1..255` | Device-local `slot` |
| `SYS` | `1..255` | Object system selector |
| `ADDR` | `0..65535` | encoded address |

These ranges are transport capacity, not universal validity.

### Resolution procedure

Section ID: `ownkb:section:d000091:s000003`

Applicability cues: `firmware`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `capture`, `evidence`

1. Resolve the Device, firmware, `slot`, and target Object.
2. Determine the functional system supported by that Object.
3. Select the applicable `OPEN.db` address rule for the management family and Object/device family.
4. Validate component values, fixed prefixes, padding, advanced offsets, level rules, and validity conditions.
5. Establish the Object-specific mapping from the semantic address to numeric `ADDR`. Do not copy a functional `WHERE` or append routing suffixes into this value merely because an address-rule template can render them.
6. Preserve `SYS` as a separate field.
7. Send the address only after the corresponding Object write.
8. Verify the effective tuple through diagnostic `DIMENSION 32`.

`SYS` is labelled “KeyObject system” by `OPEN.db`. It is not automatically a functional `WHO`, diagnostic `WHO`, or internal `EN_SYSTEM.id_system`. A numeric mapping requires Object/system and capture corroboration.

Functional `WHERE`, management selection `WHERE`, and the `DIMENSION 32.ADDR` payload are distinct representations. The stored range `0..65535` does not encode a universal conversion from strings such as group or routed addresses. Address-rule selection and rendering remain partly unresolved; stop before a write if either `SYS` or the `ADDR` conversion lacks applicable evidence.

### Address families

Section ID: `ownkb:section:d000091:s000004`

Programming reuses system-specific grammars rather than one generic `A`/`PL` form. The canonical implementation includes, among others:

- Lighting/Automation point-to-point and interface forms;
- Temperature Control zone, actuator, slave-probe, and external-probe forms;
- Video Door Entry interface forms;
- Energy Management control-unit and actuator forms;
- Access Control command and indicator forms.

The complete implementation inventory is maintained in [Address Discovery](../diagnostics/address-discovery.md).

### Physical counterparts

Section ID: `ownkb:section:d000091:s000005`

Applicability cues: `firmware`

For Lighting/Automation, decoded `A` and `PL` can correspond to physical configurator positions declared by the firmware. That correspondence establishes physical capability, not the active programming method.

A value outside the established physical range can exclude physical configuration. A value within it remains ambiguous because advanced or virtual programming can produce the same effective address.

See [Physical configuration and configuration modes](../device-model/configuration.md#physical-configuration-and-configuration-modes).

### Address error

Section ID: `ownkb:section:d000091:s000006`

Cautions: `must not`

The Device can report:

`*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##`

`ERROR` is boolean. `OPEN.db` supplies no more detailed reason. Preserve the attempted Object, `SYS`, raw `ADDR`, `slot`, and applicable address rule when reporting the failure.

The address write is optional and repeatable within `ConfKO`. Omission can be valid for an Object without an address; it must not be used to infer that every unaddressed Module is erroneous.

# Document: ownkb:document:d000092

Source path: `programming/architecture.md`
Namespace context: `contextual`
Area: `programming`

## Programming Architecture

Section ID: `ownkb:section:d000092:s000001`

The programming protocol is a management layer carried in OpenWebNet frames. It selects one installed Physical Device, receives an initial state projection, runs programming sequences labelled virtual or advanced in `OPEN.db`, and closes the programming session.

### Managed systems

Section ID: `ownkb:section:d000092:s000002`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `database`

The common programming operations are associated in `OPEN.db` with the same managed systems that expose the common diagnostic surface:

| Diagnostic/programming `WHO` | `OPEN.db` system |
| --- | --- |
| `1001` | Light and Automation system |
| `1004` | Thermoregulation |
| `1018` | Energy Management system |
| `1023` | Access Control |

Association in `OPEN.db` establishes that the templates belong to those system records. It does not prove that every Device or firmware implements every scenario or optional frame.

As in diagnostics, `WHO 1001` covers the broader Lighting/Automation management family even though the literal `EN_SYSTEM.who` value on the combined system row is `1`. Do not manufacture a second database association for functional `WHO 2`.

### Participants

Section ID: `ownkb:section:d000092:s000003`

Applicability cues: `firmware`, `gateway`
Provenance cues: `catalogue`

| Participant | Responsibility |
| --- | --- |
| Programmer | resolves capability, selects the Device, validates values, sends writes, and closes or aborts |
| Device | reports identity and installed state, accepts or rejects writes, and reports completion |
| Gateway/transport | carries frames and preserves direction; it does not validate catalogue semantics |
| Catalogue resolver | maps Device, firmware, Module, Object, address, and configuration constraints before transmission |

The wire protocol has no transaction identifier. A programmer should serialize ambiguous programming operations on one connection and retain the active `WHO`, Device selector, scenario, sequence, and `slot` context.

### Three layers of state

Section ID: `ownkb:section:d000092:s000004`

Applicability cues: `firmware`
Provenance cues: `catalogue`

| Layer | Established by |
| --- | --- |
| Catalogue capability | `MHCatalogue.db` firmware, slots, Objects, Virgin Objects, configuration definitions, filters, and rules |
| Programming request | frames sent during `ConfConfigurators` or `ConfKO` |
| Effective installed state | a fresh diagnostic interview after programming |

A request can be syntactically valid while being semantically invalid for the resolved Device. Conversely, a positive programming response establishes protocol acceptance, not necessarily complete diagnostic verification.

### `OPEN.db` virtual and advanced programming sequences

Section ID: `ownkb:section:d000092:s000005`

#### Virtual-configurator transfer

Section ID: `ownkb:section:d000092:s000006`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`

`ConfConfigurators` writes twelve transport positions in two frames:

- `*#[WHO]*0*#4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##`
- `*#[WHO]*0*#5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##`

Each value has the `OPEN.db` transport range `0..255`. `N_CONF` reports the number of physical configurator positions provided by the Device, but no canonical relation maps `C1..C12` universally to firmware `EN_CONF` definitions or `progressive` ordering. Do not equate a transport field with a physical plug or catalogue position without independent correlation.

#### Advanced Object transfer

Section ID: `ownkb:section:d000092:s000007`

`ConfKO` rebuilds the Device's Module/Object projection using:

- `DIMENSION 30` for `slot`, enabled/disabled Module state, and regular Object or Virgin Object;
- `DIMENSION 32` for system/address;
- `DIMENSION 35` for indexed configuration values.

The sequence begins with a mandatory reset-all-Objects command and ends with a mandatory programmer end-of-transmission frame. This makes the canonical sequence a replacement-style transfer, not an isolated patch operation.

`OPEN.db` also registers a reset-one-slot command, but the canonical `ConfKO` sequence uses reset-all.

### Direction and acknowledgement

Section ID: `ownkb:section:d000092:s000008`

`EN_OPEN.open_type` distinguishes programmer-to-Device and Device-to-programmer frames. Sequence rows additionally define mandatory, repeated, error, `NACK`, and timeout transitions.

Ordinary `ACK` and `NACK` templates exist in `OPEN.db` but are not listed as ordinary ordered members of the six programming sequences. `AS_OPEN_SEQUENCE.status4nack` nevertheless assigns state transitions for `NACK`. A state-machine implementation must therefore handle acknowledgement status separately from ordered frame membership.

### Source reconciliation

Section ID: `ownkb:section:d000092:s000009`

Applicability cues: `firmware`
Provenance cues: `source`

| Source | Contribution |
| --- | --- |
| `OPEN.db` | scenarios, frames, direction, parameter ranges, repetition, errors, and timeouts |
| `OpenQuery.txt` | queries used to assemble scenarios and state machines |
| `MHCatalogue.db` | Device/firmware capability and value constraints |
| `rules.db3` | selected Temperature Control linked-parameter rules |
| Public OpenWebNet PDFs | common frame syntax and functional system behavior |
| Observed traffic | actual ordering, optionality, and Device-specific support |
| MyHOME_Suite UI | selectable values, workflow state, and presentation |

`OPEN.db.diag_open` is broader than diagnostics: it marks these programming frames as well. Sequence membership, direction, and scenario type must be used to classify an operation.

# Document: ownkb:document:d000093

Source path: `programming/configuration-programming.md`
Namespace context: `contextual`
Area: `programming`

## Configuration Programming

Section ID: `ownkb:section:d000093:s000001`

Applicability cues: `firmware`

Configuration programming writes indexed Object or firmware properties after the Device, firmware, `slot`, and target Object have been resolved.

### Write frame

Section ID: `ownkb:section:d000093:s000002`

`*#[WHO]*0*#35#[INDEX]#[SLOT]*[VAL_PAR]##`

| Field | `OPEN.db` range | Meaning |
| --- | --- | --- |
| `INDEX` | `0..255` | configuration index |
| `SLOT` | `1..255` | Device-local `slot` |
| `VAL_PAR` | `0..65535` | encoded value |

`INDEX` correlates with `EN_CONF.idx` but is not globally unique.

### Resolving a property

Section ID: `ownkb:section:d000093:s000003`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`

1. Resolve the installed Device and firmware.
2. Resolve `SLOT` and the target Object selected earlier in the transfer.
3. Find Object-scoped definitions with the Object's `id_key_object` and `id_firmware = 0`.
4. Find applicable firmware-scoped definitions with `id_key_object = 0` and the resolved firmware.
5. Select definitions whose `idx` equals `INDEX`.
6. Apply filters, conditions, conversions, and value encoding.
7. Retain the resolved `EN_CONF.id_conf` with the transmitted tuple.

Do not require one `EN_CONF` row to contain both a valid Object and firmware key; the scopes are mutually exclusive in the canonical catalogue.

#### Object and firmware scopes

Section ID: `ownkb:section:d000093:s000004`

Applicability cues: `firmware`, `not applicable`
Cautions: `do not`

`EN_CONF` uses `0` as a “not applicable” sentinel on the unused ownership axis:

| Scope | `id_key_object` | `id_firmware` |
| --- | --- | --- |
| Object property | resolved Object ID | `0` |
| Firmware property | `0` | resolved firmware ID |

The zero values do not identify Object 0 or firmware 0. They take the place of `NULL` and distinguish which entity owns the definition. Applicable definitions must therefore be collected as the union of the two scopes:

```sql
SELECT *
FROM EN_CONF
WHERE (id_key_object = :object_id AND id_firmware = 0)
   OR (id_key_object = 0 AND id_firmware = :firmware_id)
```

A query requiring both resolved IDs in the same row would miss the canonical definitions. Resolve the scope before interpreting `idx`, because an index is not globally unique.

This union selects candidate definitions, not permission to write all of them. Firmware physical fields with `idx = -1` have no representation in the unsigned `INDEX` range above. Establish the applicable transfer mechanism and encoding separately before emitting a property.

### Transfer behavior

Section ID: `ownkb:section:d000093:s000005`

Cautions: `do not`, `warning`

Parameter writes are optional and repeatable within `ConfKO`. `NACK` transitions the canonical sequence to Warning rather than Error.

The Device can report:

`*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##`

`OPEN.db` classifies this as error-and-information because a Device can leave some parameters unmanaged without stopping the whole configuration. The sequence maps it to Warning. Preserve each warning by `SLOT` and `INDEX`; do not discard the rest of the accepted configuration.

### Value forms

Section ID: `ownkb:section:d000093:s000006`

Depending on the resolved definition, `VAL_PAR` can encode:

- an enumeration;
- a numeric range;
- a padded value;
- a boolean;
- a fixed value;
- a user-supplied value;
- a value requiring a conversion rule.

The transport maximum does not override `EN_CONF_RANGE`, `EN_FILTER_RANGE`, or linked-property rules.

### Physical counterparts

Section ID: `ownkb:section:d000093:s000007`

Applicability cues: `firmware`
Provenance cues: `catalogue`

An indexed property can correspond to a physical configurator position even when the symbols differ. For example, firmware `192` uses physical `TYPE` and `PRE` positions while shutter actuator Object `218` uses indexed `SHUTTER_TYPE` and `PRESET_NUMBER` properties.

A physical counterpart does not prove that the installed value was physically configured, and physical and advanced encodings need not use the same range.

Physical-property correspondence is separate from physical topology selection. When physical configurator values determine which Object exists in a slot, resolve the topology first with [Catalogue Resolution](../internals/catalogue-resolution.md#physical-configuration-resolution), then evaluate the selected Object's property conversions.

See [Configuration](../device-model/configuration.md), [Programming Validation](validation.md), and diagnostic [`DIMENSION 35`](../diagnostics/dim35-configuration.md).

### Special parameters

Section ID: `ownkb:section:d000093:s000008`

Cautions: `do not`
Provenance cues: `evidence`

Diagnostic `DIMENSION 310` carries an Object-specific value without `INDEX`. `OPEN.db` provides no corresponding generic programming write in `ConfKO`. Do not force it into `DIMENSION 35` programming without Object-specific evidence.

# Document: ownkb:document:d000094

Source path: `programming/device-selection.md`
Namespace context: `contextual`
Area: `programming`

## Device Selection

Section ID: `ownkb:section:d000094:s000001`

Programming begins by selecting one installed Physical Device within a management `WHO`. The canonical scenarios support selection by diagnostic address, by 32-bit Device ID, or through a local-interaction workflow.

### Selection frames

Section ID: `ownkb:section:d000094:s000002`

| Method | Frame | First-response window |
| --- | --- | --- |
| Address | `*[WHO]*1*[WHERE]##` | 15 s |
| Device ID | `*[WHO]*9#[ID]*0##` | 15 s |
| Local-interaction scenario | `*[WHO]*1*[WHERE]##` | 300 s |

The Device ID has the `OPEN.db` range `0..4294967295`. Observed interfaces render it as eight hexadecimal characters; the wire template carries the `ID` field without defining that display representation.

### Selecting by Device ID

Section ID: `ownkb:section:d000094:s000003`

Cautions: `do not`
Provenance cues: `catalogue`

Use the installed instance identifier returned by diagnostic `DIMENSION 13`. Do not substitute:

- `EN_DEVICE.id_device`;
- `EN_ITEM.id_item`;
- `OBJECT_MODEL`;
- a Module address;
- a catalogue SKU.

The ID-based scenario proceeds to advanced Object configuration. It does not include the virtual-configurator sequence.

### Selecting by address

Section ID: `ownkb:section:d000094:s000004`

`WHERE` follows the selected management family's address grammar. It is not one universal integer and must be generated from the applicable `OPEN.db` address rule.

A Physical Device can expose several Modules and functional addresses. The diagnostic/programming selection address must therefore remain distinct from per-Module addresses written through `DIMENSION 32`. Observed `WHO 1001` traffic often correlates the Device context with `slot` `1`, but this is not a universal rule.

The address-selected programming scenario proceeds to virtual-configurator transfer and does not include `ConfKO`.

### Local-interaction selection

Section ID: `ownkb:section:d000094:s000005`

Cautions: `must not`
Provenance cues: `database`

The `ConfLocalButton` sequence uses the same start frame and response order as `ConfAddressed` but assigns a 300-second first-response window. Its scenario then permits advanced Object configuration followed by virtual-configurator transfer.

The database name establishes a local-button workflow; the frame does not encode the physical interaction. An implementation must coordinate the installer action outside the OpenWebNet payload and must not infer which Device was selected solely from the long timeout.

### Initial identity checks

Section ID: `ownkb:section:d000094:s000006`

Applicability cues: `firmware`, `version`
Provenance cues: `catalogue`

Before transmitting configuration, compare the returned initial projection with the intended target:

- `DIMENSION 1` item/model, physical configurator count, brand, and line;
- `DIMENSION 2` firmware version;
- `DIMENSION 13` Device ID;
- `DIMENSION 30` enabled regular Object or disabled Virgin Object by `slot`;
- `DIMENSION 32` current Module addresses where reported.

Resolve the Device through the documented catalogue path and retain ambiguity where several SKUs share an item.

### Failure handling

Section ID: `ownkb:section:d000094:s000007`

Cautions: `do not`

A `NACK` on the mandatory start frame transitions the canonical state to Undefined. No first response before the applicable timer also leaves target selection unestablished. Do not send transfer frames after ambiguous selection.

`WHAT 3` indicates Device abort during the entry sequence. Preserve any partial identity records but mark the programming session aborted.

See [Device Discovery](../diagnostics/device-discovery.md), [Address Discovery](../diagnostics/address-discovery.md), and [Device Identity](../diagnostics/dim1-device-identity.md) for the read-only discovery procedures.

# Document: ownkb:document:d000095

Source path: `programming/dimension-reference.md`
Namespace context: `contextual`
Area: `programming`

## Programming `DIMENSION` Reference

Section ID: `ownkb:section:d000095:s000001`

Programming `DIMENSION` writes transfer the configurator fields used by `ConfConfigurators`, Object assignments, Module addresses, and indexed parameters. Related Device responses report the written state or structured errors.

### Write frames

Section ID: `ownkb:section:d000095:s000002`

| `DIMENSION` | Frame | Meaning | Sequence |
| --- | --- | --- | --- |
| `4` | `*#[WHO]*0*#4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##` | write configurator fields `C1..C6` | `ConfConfigurators` |
| `5` | `*#[WHO]*0*#5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##` | write configurator fields `C7..C12` | `ConfConfigurators` |
| `30` | `*#[WHO]*0*#30*[SLOT]*[KEYO]##` | assign Object to `slot` | `ConfKO` |
| `32` | `*#[WHO]*0*#32#[SLOT]*[SYS]*[ADDR]##` | assign Object system/address | `ConfKO` |
| `35` | `*#[WHO]*0*#35#[INDEX]#[SLOT]*[VAL_PAR]##` | write indexed configuration value | `ConfKO` |

`DIMENSION 4` is mandatory in `ConfConfigurators`; `5` is optional. `DIMENSION 30` is mandatory and repeatable in `ConfKO`; `32` and `35` are optional and repeatable.

### Related response and error frames

Section ID: `ownkb:section:d000095:s000003`

Cautions: `warning`

| `DIMENSION` | Frame | Meaning |
| --- | --- | --- |
| `4` | `*#[WHO]*[WHERE]*4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##` | Device configurator report `1..6` |
| `5` | `*#[WHO]*[WHERE]*5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##` | Device configurator report `7..12` |
| `30` | `*#[WHO]*[WHERE]*30*[SLOT]*[KEYO]*[STATE]##` | configured Object or Virgin Object state |
| `31` | `*#[WHO]*[WHERE]*31*[SLOT]*[CODE]*[STATE]##` | Object state/error |
| `32` | `*#[WHO]*[WHERE]*32#[SLOT]*[SYS]*[ADDR]##` | effective Module address |
| `34` | `*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##` | address error |
| `35` | `*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##` | effective indexed parameter |
| `39` | `*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##` | indexed parameter warning/error |

### Transport ranges

Section ID: `ownkb:section:d000095:s000004`

Provenance cues: `catalogue`

| Field | Range in `OPEN.db` |
| --- | --- |
| `C1..C12` | `0..255` |
| `SLOT` | `1..255` |
| `KEYO` | `1..65535` |
| `SYS` | `1..255` |
| `ADDR` | `0..65535` |
| `INDEX` | `0..255` |
| `VAL_PAR` | `0..65535` |
| `STATE`, `ERROR` | `0..1` |

These are frame-field capacities. Catalogue and address rules define the values valid for a particular Device.

### `DIMENSION 4` and `5`

Section ID: `ownkb:section:d000095:s000005`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`

`OPEN.db` labels each `C1..C12` field “Configurator value”, constrains it to `0..255`, and describes `ConfConfigurators` as virtual configuration. Those are transport and sequence facts. `MHCatalogue.db` separately defines firmware-specific physical symbols and legal domains. No canonical cross-database key establishes that `C1` is universally the `EN_CONF` definition with `progressive = 1`, or an equivalent positional mapping. Preserve all twelve raw fields and resolve any catalogue correlation separately through [Physical-configuration resolution](../internals/catalogue-resolution.md#dimension-4-and-5-are-a-transport-boundary).

### `DIMENSION 30`

Section ID: `ownkb:section:d000095:s000006`

Applicability cues: `applies to`, `firmware`
Cautions: `must not`
Provenance cues: `evidence`

The write carries a configured Object number. Diagnostic state determines how a previously reported `KEYO` is resolved:

- `STATE = 0`: enabled Module, `EN_KEY_OBJECT.key_object`;
- `STATE = 1`: disabled Module, `EN_VIRGIN_OBJECT.virgin_key_object`.

This polarity applies to the `STATE` carried by `DIMENSION 30`; it must not be copied to the separate `STATE` field carried by `DIMENSION 31` without independent evidence.

The target write must use a permitted configured Object, validated through Virgin Object, firmware, and slot associations.

### `DIMENSION 32`

Section ID: `ownkb:section:d000095:s000007`

Cautions: `must not`

`#32#[SLOT]` is the parameterized `DIMENSION` selector: the leading `#` selects the write form and the following `#` attaches `SLOT` to the selector. `SYS` and `ADDR` are ordinary `DIMENSION` values separated with `*`. They require the Object/system address rule and must not all be decoded as `A`/`PL`.

### `DIMENSION 35`

Section ID: `ownkb:section:d000095:s000008`

The two `#` separators before `INDEX` and `SLOT` are significant. `INDEX` correlates with context-resolved `EN_CONF.idx`. Apply ranges, filters, conditions, and conversions before encoding `VAL_PAR`.

### Error dimensions

Section ID: `ownkb:section:d000095:s000009`

Cautions: `warning`

`DIMENSION 31` provides five fixed Object-state codes. `DIMENSION 34` and `39` carry boolean error fields without enumerated causes.

`DIMENSION 39` is intentionally nonfatal in the canonical advanced sequence: it maps to Warning so an unmanaged parameter does not necessarily reject the rest of the transfer.

### Source boundary

Section ID: `ownkb:section:d000095:s000010`

The same numeric dimensions appear in diagnostics because programming writes and diagnostic read-back project related state. Direction, frame form, and active sequence distinguish them. See the [Diagnostic `DIMENSION` Reference](../diagnostics/dimension-reference.md) for read-only interpretation.

# Document: ownkb:document:d000096

Source path: `programming/error-handling.md`
Namespace context: `contextual`
Area: `programming`

## Programming Error Handling

Section ID: `ownkb:section:d000096:s000001`

Programming failures must remain attached to the active session, target Device, transfer sequence, `slot`, Object, property, and attempted value.

### Terminal responses

Section ID: `ownkb:section:d000096:s000002`

| Frame | Meaning in `OPEN.db` | Classification |
| --- | --- | --- |
| `*[WHO]*51*[WHERE_FAKE]##` | wrong configuration | fatal error |
| `*[WHO]*52*[WHERE_FAKE]##` | configuration accepted | successful advanced-transfer result |
| `*[WHO]*3*0##` | abort configuration | direction-dependent abort |
| `*[WHO]*4*[WHERE_FAKE]##` | Device end of transmission | entry/virtual-transfer terminal marker |
| `*[WHO]*4*0##` | programmer end of transmission | closes advanced transfer payload |
| `*[WHO]*2*0##` | end programming session | outer session close |

`OPEN.db` also provides `WHERE = 0` variants of `WHAT 51` and `52` outside the canonical sequence rows. Preserve the received form.

### Structured errors

Section ID: `ownkb:section:d000096:s000003`

#### Object state

Section ID: `ownkb:section:d000096:s000004`

`*#[WHO]*[WHERE]*31*[SLOT]*[CODE]*[STATE]##`

| Code | Meaning | `ConfKO` state |
| --- | --- | --- |
| `0` | Object not implemented/unset | Error |
| `1` | Object busy | Error in `ConfKO`; informational in diagnostic contexts |
| `2` | Object already configured | Error |
| `3` | insufficient free Object capacity | Error |
| `4` | requested Object not implemented | Error |

The same busy frame can be nonfatal information during diagnostics and a transfer error during programming. Sequence context controls handling.

#### Address

Section ID: `ownkb:section:d000096:s000005`

`*#[WHO]*[WHERE]*34*[SLOT]*[ERROR]##`

The boolean flag identifies an address error but does not encode its cause.

#### Parameter

Section ID: `ownkb:section:d000096:s000006`

Cautions: `warning`

`*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##`

This is classified as error-and-information. `ConfKO` maps it to Warning so unsupported/unmanaged parameters need not invalidate all other writes.

### `ACK` and `NACK`

Section ID: `ownkb:section:d000096:s000007`

Cautions: `do not`, `warning`

Ordered programming sequences do not list ordinary `ACK` or `NACK` as members, but `status4nack` defines their state transitions:

- entry-frame `NACK` → Undefined;
- virtual-configurator write `NACK` → Error;
- Object/address/reset `NACK` → Error;
- parameter or programmer end-of-transmission `NACK` → Warning;
- close-session `NACK` → Error.

Handle `NACK` relative to the last outstanding command and active sequence. Do not interpret an uncorrelated `NACK` after pipelining several writes.

### Timeout and transport loss

Section ID: `ownkb:section:d000096:s000008`

Cautions: `do not`

A timeout is not a negative acknowledgement and does not prove that the Device rejected or rolled back prior writes. Mark the result indeterminate, send programmer abort when safe and supported, close the transport according to application policy, and require diagnostic read-back before retry.

Because `ConfKO` starts by resetting all Objects, interruption during a replacement transfer can leave partial or uncertain state. Do not resume at an arbitrary later frame unless Device-specific behavior establishes that this is safe.

### Recovery policy

Section ID: `ownkb:section:d000096:s000009`

Cautions: `do not`
Provenance cues: `catalogue`, `evidence`

1. Stop sending new writes after a fatal error or ambiguous timeout.
2. Preserve every frame and state transition.
3. Send programmer `WHAT 3` abort if the active workflow supports recovery.
4. End or re-establish the connection.
5. Perform a fresh diagnostic interview.
6. Re-resolve the Device and catalogue context.
7. Rebuild the complete desired configuration.
8. Start a new programming session rather than assuming the previous transfer position.

`WHAT 7` is labelled as deleting stored Device configuration but is not part of a canonical programming scenario. Do not use it as a generic recovery operation without Device-specific evidence.

# Document: ownkb:document:d000097

Source path: `programming/object-programming.md`
Namespace context: `contextual`
Area: `programming`

## Object Programming

Section ID: `ownkb:section:d000097:s000001`

Applicability cues: `firmware`

Object programming assigns a logical Object to each firmware-exposed Module during advanced configuration.

### Write frame

Section ID: `ownkb:section:d000097:s000002`

`*#[WHO]*0*#30*[SLOT]*[KEYO]##`

| Field | `OPEN.db` range | Meaning |
| --- | --- | --- |
| `SLOT` | `1..255` | Device-local `slot` |
| `KEYO` | `1..65535` | target Object number |

`KEYO` is the external `EN_KEY_OBJECT.key_object` value, not `EN_KEY_OBJECT.id_key_object`.

### Replacement-style transfer

Section ID: `ownkb:section:d000097:s000003`

Uncertainty: `not established`

The canonical `ConfKO` sequence begins with:

`*[WHO]*14#0*0##`

`OPEN.db` describes this as resetting all Device Objects. The sequence then requires repeated Object writes and later sends addresses and parameters. Treat this as a full replacement transfer: construct and validate the complete desired Module/Object layout before sending reset-all.

`OPEN.db` also registers:

`*[WHO]*14#[SLOT]*0##`

for resetting one `slot`. It is not a member of the canonical `ConfKO` sequence, so its standalone lifecycle and completion behavior are not established by that scenario.

### Resolving the permitted Object

Section ID: `ownkb:section:d000097:s000004`

Applicability cues: `firmware`
Provenance cues: `evidence`

1. Resolve the Physical Device item and firmware.
2. Resolve the target `SLOT` against the firmware's slot structures.
3. Determine from `DIMENSION 30.STATE` whether the Module is enabled (`0`) with a regular configured Object or disabled (`1`) with a Virgin Object.
4. If disabled, resolve `KEYO` through `EN_VIRGIN_OBJECT.virgin_key_object`; if enabled, resolve it through `EN_KEY_OBJECT.key_object`.
5. Use `AS_OBJECT_VIRGIN_OBJECT` to find Objects permitted by that Virgin Object.
6. Use `AS_OBJECT_FIRMWARE` and `EN_SLOTS` to require firmware and slot support.
7. Respect `EN_SLOTS.fixed_ko` and slot conditions.
8. Use the target Object's external `key_object` in the programming frame.

A Virgin Object constrains a disabled Module's configurable role. It is not itself the regular configured Object to send unless independent evidence establishes that a specific Device expects such a write.

### Fixed and absent Modules

Section ID: `ownkb:section:d000097:s000005`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`

A fixed Object is catalogue capability, not permission to overwrite it. Hidden UI Modules and gaps in UI numbering do not change protocol `SLOT` values.

Do not synthesize Modules up to `EN_FIRMWARE.slots` merely because the firmware declares a capacity. Use the actual slot/Object associations and the current diagnostic projection.

### Sequence behavior

Section ID: `ownkb:section:d000097:s000006`

The Object write is both mandatory and repeatable. It starts the 50-second `DeviceKOTimeOut` and a two-second `CmdKoValueTimeWait`. `NACK` transitions to Error.

After all Object, address, and parameter writes, the programmer sends `WHAT 4` end of transmission. The Device can then return `WHAT 52`, `WHAT 51`, a structured error, or abort.

### Object errors

Section ID: `ownkb:section:d000097:s000007`

| `DIMENSION 31` code | `OPEN.db` meaning |
| --- | --- |
| `0` | Object not implemented/unset |
| `1` | Object busy |
| `2` | Object already configured |
| `3` | insufficient free Object capacity |
| `4` | requested Object not implemented |

Codes `0`, `2`, `3`, and `4` are fatal errors in `ConfKO`. Busy code `1` is classified as error-and-information but still maps to Error through `status4error` in that sequence. Retain the accompanying `STATE` and `slot`.

See [Modules](../device-model/modules.md), [Objects](../device-model/objects.md), [Virgin Objects](../device-model/virgin-objects.md), and [`DIMENSION 30`](../diagnostics/dim30-modules.md).

# Document: ownkb:document:d000098

Source path: `programming/session-lifecycle.md`
Namespace context: `contextual`
Area: `programming`

## Programming Session Lifecycle

Section ID: `ownkb:section:d000098:s000001`

`OPEN.db` models programming as a scenario composed from ordered sequences. The outer programming session and the inner transfer sequence have separate terminal frames and timers.

### Scenario composition

Section ID: `ownkb:section:d000098:s000002`

Provenance cues: `database`

| Scenario | Entry | Transfer | Close |
| --- | --- | --- | --- |
| By address | `ConfAddressed` | `ConfConfigurators` | `CloseConf` |
| By Device ID | `ConfPoint2PointWithID` | repeated `ConfKO` | `CloseConf` |
| By local interaction | `ConfLocalButton` | repeated `ConfKO`, then `ConfConfigurators` | `CloseConf` |

A repeated `ConfKO` association means the scenario engine can invoke that sequence repeatedly. The database does not encode the application-level repetition count.

### Entry and initial projection

Section ID: `ownkb:section:d000098:s000003`

Applicability cues: `firmware`, `version`

The entry sequence sends one mandatory start frame:

| Method | Frame |
| --- | --- |
| Address | `*[WHO]*1*[WHERE]##` |
| Device ID | `*[WHO]*9#[ID]*0##` |
| Local-interaction scenario | `*[WHO]*1*[WHERE]##` |

`ConfLocalButton` and `ConfAddressed` contain the same ordered frames. Their implementation difference is the first-response timer: the local-interaction sequence uses a 300-second window instead of the 15-second addressed/ID window. The frame still contains `WHERE`; `OPEN.db` does not explain how physical interaction and that value are coordinated.

After entry, the Device can report the same initial projection used by diagnostics:

1. `DIMENSION 1` identity;
2. firmware and hardware versions;
3. `DIMENSION 4` and `5` configurator values;
4. microcontroller version;
5. diagnostic bitmasks;
6. `DIMENSION 13` Device ID;
7. repeated `DIMENSION 30` Module/Object state;
8. repeated `DIMENSION 32` addresses;
9. repeated busy `DIMENSION 31` information;
10. `WHAT 4` end of transmission.

Only the start frame is marked mandatory. Collectors must tolerate omitted optional responses and repeated Module records.

### Transfer states

Section ID: `ownkb:section:d000098:s000004`

#### Virtual-configurator transfer

Section ID: `ownkb:section:d000098:s000005`

`ConfConfigurators` requires `DIMENSION 4`, optionally writes `DIMENSION 5`, and accepts:

- `WHAT 51`: wrong configuration;
- `WHAT 3`: Device abort;
- echoed/reported `DIMENSION 4` and `5` values;
- Device `WHAT 4`: end of transmission.

The sequence does not include `WHAT 52`.

#### Advanced Object transfer

Section ID: `ownkb:section:d000098:s000006`

Cautions: `do not`
Provenance cues: `source`

`ConfKO` orders:

1. mandatory reset of all Objects;
2. mandatory repeated `DIMENSION 30` Object writes;
3. optional repeated `DIMENSION 32` address writes;
4. optional repeated `DIMENSION 35` parameter writes;
5. mandatory programmer `WHAT 4` end of transmission;
6. Device `WHAT 51` or `WHAT 52` result, applicable structured errors, or `WHAT 3` abort.

`AS_OPEN_SEQUENCE` contains no row with `open_order = 9` for `ConfKO`. Preserve the source numbering; do not invent a missing operation.

The error rows are alternatives associated with the active transfer. Their numeric `open_order` positions do not mean that an error can only be received after every earlier optional frame.

### Session close and abort

Section ID: `ownkb:section:d000098:s000007`

Cautions: `do not`

Normal close uses:

`*[WHO]*2*0##`

This is the sole mandatory member of `CloseConf`. Its stored timeout associations stop the ten-minute configuration timer and start the one-second scenario-close wait in the Suite sequence model; they do not prove Device-side commit or persistence.

Programmer abort and Device abort share:

`*[WHO]*3*0##`

`OPEN.db` stores separate rows distinguished by direction. The canonical programming sequences include the Device-to-programmer abort row; `OpenQuery.txt` separately loads the programmer abort together with diagnostic abort. Direction and active state are therefore required.

### Timing model

Section ID: `ownkb:section:d000098:s000008`

| Timer | Default | Role |
| --- | --- | --- |
| `ConfTimeOut` | 600 s | maximum configuration session |
| `DeviceAnswerTimeOut` | 15 s | first identity response after address/ID start |
| `DeviceAnswerTimeOutByButton` | 300 s | first response in local-interaction programming |
| `DeviceMoreAnswerTimeOut` | 20 s | remaining initial information until Device `WHAT 4` |
| `DeviceAcceptTimeOut` | 2 s | virtual-configurator acceptance window |
| `DeviceKOTimeOut` | 50 s | advanced Object transfer |
| `CmdKoValueTimeWait` | 2 s | wait associated with Object writes |
| `KOAcceptTimeWait` | 3 s | wait after `WHAT 52` before scenario close |
| `CloseScenarioTimeWait` | 1 s | close-sequence wait |

These are MyHOME_Suite defaults, not wire-level constants.

### Completion classification

Section ID: `ownkb:section:d000098:s000009`

Cautions: `warning`
Provenance cues: `evidence`

| Result | Evidence |
| --- | --- |
| Transfer accepted | expected Device terminal response for the active transfer |
| Transfer rejected | `WHAT 51` or fatal structured error |
| Warning | nonfatal structured error such as an unmanaged parameter |
| Aborted | `WHAT 3` from either participant |
| Timed out | an active timer expired without its stopping transition |
| Close sent | programmer transmitted `WHAT 2`; Device-side closure is not independently confirmed by transmission alone |
| Verified | a later diagnostic interview matches the intended effective state |

Closing a session does not change a rejection or timeout into success.

# Document: ownkb:document:d000099

Source path: `programming/validation.md`
Namespace context: `contextual`
Area: `programming`

## Programming Validation

Section ID: `ownkb:section:d000099:s000001`

Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `evidence`

Programming validation checks a complete intended configuration against the available evidence for one resolved Physical Device before any write is sent. Passing catalogue and encoding checks establishes consistency with those sources, not proven runtime acceptance, persistence, or complete coverage of Device constraints. The numeric ranges in `OPEN.db` describe frame-field capacity; they do not establish that a value, Object, address, or property is valid for a particular Device.

Validation is a staged resolver. Each milestone consumes an established context and produces evidence required by the next milestone. If a required result is ambiguous or unresolved, stop before programming.

### Required input

Section ID: `ownkb:section:d000099:s000002`

Applicability cues: `firmware`, `version`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `evidence`, `source`

Start with an immutable working record containing all available installation evidence:

| Input | Source |
| --- | --- |
| management `WHO` | selected diagnostic/programming family |
| Device selector | diagnostic `WHERE` and, where available, `DIMENSION 13` Device ID |
| identity projection | diagnostic `DIMENSION 1`, firmware version, and hardware version |
| Module projection | every `DIMENSION 30` record |
| address projection | every `DIMENSION 32` record |
| parameter projection | every `DIMENSION 35` record and any `DIMENSION 310` record |
| intended state | complete desired Module/Object layout, addresses, and property values |

Retain raw frames beside decoded values. Do not replace an unresolved field with a guessed catalogue identifier.

### Milestone overview

Section ID: `ownkb:section:d000099:s000003`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `catalogue`

| Milestone | Goal | Required output |
| --- | --- | --- |
| 1 | Resolve the installed Device | one item/firmware context or an explicit ambiguity set |
| 2 | Resolve the Module | one Device-local `slot` and its catalogue placement |
| 3 | Resolve the current role | enabled regular Object or disabled Module's Virgin Object |
| 4 | Prove the target Object is available | one permitted target Object and Object/firmware association |
| 5 | Build the property dictionary | applicable Object- and firmware-scoped `EN_CONF` definitions |
| 6 | Establish write eligibility | writable, visible, fixed, hidden, or conditional status |
| 7 | Build the base value domain | enumerated values or numeric bounds from `EN_CONF_RANGE` |
| 8 | Apply contextual filters | Object/firmware-specific effective domain |
| 9 | Apply conditions and conversions | selected branches and encoded value |
| 10 | Apply linked-property rules | cross-property-valid candidate configuration |
| 11 | Validate addresses | valid `SYS`/`ADDR` encoding for the resolved Object |
| 12 | Classify physical representation | physically representable, outside the established physical domain, or unresolved |
| 13 | Build wire values | validated `KEYO`, `SYS`/`ADDR`, and `INDEX`/`VAL_PAR` tuples |
| 14 | Validate the complete transfer | internally consistent replacement payload and verification plan |

The milestones are dependencies, not merely a convenient order. For example, an `INDEX` cannot be resolved safely before the Object, firmware, and `slot` are known.

### 1. Resolve the installed Device

Section ID: `ownkb:section:d000099:s000004`

#### Goal

Section ID: `ownkb:section:d000099:s000005`

Provenance cues: `catalogue`, `database`

Establish the catalogue context corresponding to the installed Physical Device without confusing protocol values with database primary keys.

#### Procedure

Section ID: `ownkb:section:d000099:s000006`

Applicability cues: `firmware`, `version`
Cautions: `do not`
Provenance cues: `catalogue`

1. Use the management `WHO` to select the applicable diagnostic family.
2. Decode `DIMENSION 1` according to that family.
3. Resolve its item/model value through the documented item and system associations.
4. Resolve the candidate Physical Device records and use `EN_DEVICE.name` as the standard Device description.
5. Use the reported firmware version to narrow the applicable item/firmware association. Preserve hardware and microcontroller versions as observations; use them for selection only when an independently established mapping exists.
6. Preserve multiple SKU candidates when several catalogue items share the same implementation identity.
7. Retain the installed Device ID from `DIMENSION 13` separately from every catalogue identifier.

`DIMENSION 1` VALUE 2 is `N_CONF`, the physical configurator-position count. Do not use it as a Device class, Object, Virgin Object, or firmware key.

#### Milestone output

Section ID: `ownkb:section:d000099:s000007`

Applicability cues: `firmware`, `version`
Uncertainty: `unresolved`
Provenance cues: `evidence`

Record at least:

- diagnostic family and `WHO`;
- raw and decoded identity projection;
- item/model identity;
- candidate SKU set;
- resolved firmware record and version evidence;
- installed Device ID;
- unresolved identity ambiguities.

#### Stop conditions

Section ID: `ownkb:section:d000099:s000008`

Applicability cues: `firmware`
Cautions: `do not`
Uncertainty: `may`
Provenance cues: `catalogue`

Stop if no catalogue item or firmware can be justified. If several SKUs remain but share the same relevant firmware capability, validation may continue only with that common capability; do not claim a unique SKU.

See [Device Identity](../diagnostics/dim1-device-identity.md) and [Physical Device](../device-model/physical-devices.md).

### 2. Resolve the Module and `slot`

Section ID: `ownkb:section:d000099:s000009`

#### Goal

Section ID: `ownkb:section:d000099:s000010`

Applicability cues: `firmware`

Bind the intended change to one firmware-exposed Module and the numeric `slot` carried by programming frames.

#### Procedure

Section ID: `ownkb:section:d000099:s000011`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`

1. Use diagnostic `DIMENSION 30.SLOT` as the Device-local `slot` number.
2. Correlate it with catalogue placement such as `EN_SLOTS.first_slot`.
3. Resolve the relevant `AS_OBJECT_FIRMWARE` and slot records for the selected firmware.
4. Retain UI-visible Module numbering only as presentation metadata.
5. Do not synthesize Modules merely because `EN_FIRMWARE.slots` declares a capacity.

#### Milestone output

Section ID: `ownkb:section:d000099:s000012`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Produce one Module context containing:

- installed Device and firmware;
- protocol `slot`;
- matching catalogue slot records;
- current `DIMENSION 30` state;
- associated `DIMENSION 32` and `35` records;
- fixed-Object and slot-condition metadata.

#### Stop conditions

Section ID: `ownkb:section:d000099:s000013`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Stop if the `slot` does not exist for the resolved firmware or if several incompatible catalogue placements remain.

### 3. Resolve the current Object or Virgin Object

Section ID: `ownkb:section:d000099:s000014`

#### Goal

Section ID: `ownkb:section:d000099:s000015`

Cautions: `do not`
Provenance cues: `database`

Interpret the current `DIMENSION 30.KEYO` in the correct external number space.

| `STATE` | Resolve `KEYO` against | Meaning |
| --- | --- | --- |
| `0` | `EN_KEY_OBJECT.key_object` | enabled Module; regular configured Object |
| `1` | `EN_VIRGIN_OBJECT.virgin_key_object` | disabled Module; Virgin Object |

Neither value is an internal database primary key. Likewise, protocol `SLOT` is not `EN_SLOTS.id_slot`.

For a disabled Module, retain the Virgin Object as the role constraint from which permitted regular Objects will be derived. Do not send its `virgin_key_object` as a target `KEYO` merely because it was reported diagnostically.

#### Milestone output

Section ID: `ownkb:section:d000099:s000016`

Produce exactly one of:

- a resolved current regular Object for an enabled Module; or
- a resolved Virgin Object with its functional role for a disabled Module.

Stop if `STATE` is absent or if `KEYO` does not resolve uniquely in the selected namespace.

See [`DIMENSION 30`: Modules and Objects](../diagnostics/dim30-modules.md).

### 4. Prove target Object availability

Section ID: `ownkb:section:d000099:s000017`

#### Goal

Section ID: `ownkb:section:d000099:s000018`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Reduce the global Object catalogue to the set supported by this firmware, Module, and current configurable role.

#### Procedure

Section ID: `ownkb:section:d000099:s000019`

Applicability cues: `firmware`
Provenance cues: `catalogue`

1. If the Module is disabled, enumerate candidates related to its Virgin Object through `AS_OBJECT_VIRGIN_OBJECT`.
2. Intersect that set with Objects related to the resolved firmware through `AS_OBJECT_FIRMWARE`.
3. Intersect again with Objects placed at the resolved `slot` through `EN_SLOTS`.
4. Apply `fixed_ko` and slot-condition metadata.
5. If the Module is already configured, determine whether replacement is permitted; current membership alone does not prove writability.
6. Select the target by external `EN_KEY_OBJECT.key_object`, but retain its internal `id_key_object` for catalogue joins.
7. Retain the resolved `AS_OBJECT_FIRMWARE.id_object_firmware`; contextual filters depend on it.

Conceptually:

```text
permitted targets =
    Virgin-Object candidates, when applicable
  ∩ firmware-supported Objects
  ∩ `slot`-supported Objects
  ∩ satisfied fixed/conditional constraints
```

#### Milestone output

Section ID: `ownkb:section:d000099:s000020`

Applicability cues: `firmware`
Provenance cues: `evidence`

Produce:

- one target `id_key_object`;
- its external programming `key_object`;
- one applicable Object/firmware association;
- one compatible slot placement;
- the evidence that admitted it to the permitted set.

#### Stop conditions

Section ID: `ownkb:section:d000099:s000021`

Cautions: `do not`

Reject the target if it disappears at any intersection. Do not fall back to the global Object list.

See [Object Programming](object-programming.md), [Objects](../device-model/objects.md), and [Virgin Objects](../device-model/virgin-objects.md).

### 5. Build the applicable property dictionary

Section ID: `ownkb:section:d000099:s000022`

#### Goal

Section ID: `ownkb:section:d000099:s000023`

Applicability cues: `firmware`, `not applicable`
Provenance cues: `catalogue`

Collect every configuration definition that can describe the resolved Object/firmware context.

`EN_CONF` uses two exclusive ownership scopes:

| Scope | Selection |
| --- | --- |
| Object property | resolved `id_key_object` and `id_firmware = 0` |
| Firmware property | `id_key_object = 0` and resolved `id_firmware` |

Collect their union:

```sql
SELECT *
FROM EN_CONF
WHERE (id_key_object = :object_id AND id_firmware = 0)
   OR (id_key_object = 0 AND id_firmware = :firmware_id)
```

The zero is a “not applicable” sentinel, not Object or firmware ID 0. Never require both resolved IDs on the same `EN_CONF` row.

Index the resulting dictionary by at least:

- scope;
- `EN_CONF.id_conf`;
- `idx`;
- symbolic name;
- semantic type;
- data type;
- `slot` and Object/firmware context.

An `idx` is not globally unique. It becomes a usable `DIMENSION 35.INDEX` only after this context has been resolved.

The union is a candidate property dictionary, not a list of writable parameters. In particular, firmware physical fields with `idx = -1` cannot be emitted as an unsigned `DIMENSION 35.INDEX`; neither a shared symbol nor catalogue presence establishes their transfer operation.

#### Milestone output

Section ID: `ownkb:section:d000099:s000024`

Produce the complete context-specific property dictionary and identify whether each intended UI/property concept resolves to zero, one, or several definitions.

#### Stop conditions

Section ID: `ownkb:section:d000099:s000025`

Uncertainty: `unresolved`
Provenance cues: `capture`, `evidence`

- zero matches: unresolved or unsupported property;
- one match: continue;
- several matches: disambiguate by scope, symbol, semantic type, filter, UI behavior, or capture evidence before continuing.

See [Configuration Programming](configuration-programming.md) for the write mapping.

### 6. Establish write eligibility

Section ID: `ownkb:section:d000099:s000026`

#### Goal

Section ID: `ownkb:section:d000099:s000027`

Cautions: `do not`
Uncertainty: `may`, `unresolved`
Provenance cues: `catalogue`

Separate values that exist in the catalogue from values that the programmer may modify.

For each resolved `EN_CONF` definition, evaluate:

- `read_only`;
- `visible`;
- `hidden`;
- fixed-value data type;
- progressive/order metadata;
- applicable slot conditions;
- whether the value is calculated or compiled by MyHOME_Suite;
- whether it is reported by the Device but lacks a generic programming operation.

Classify the property as:

| Status | Programming treatment |
| --- | --- |
| writable | candidate for a write |
| conditional | writable only if its enabling condition is satisfied |
| fixed | preserve the defined value; do not offer arbitrary input |
| read-only | compare during verification but do not write |
| hidden | do not assume invalid; resolve the hiding condition |
| unsupported | omit from the payload |
| unresolved | fail closed |

Visibility is presentation metadata, not by itself permission to write. Conversely, a hidden property can still participate in conversions or linked rules.

### 7. Build the base value domain

Section ID: `ownkb:section:d000099:s000028`

#### Goal

Section ID: `ownkb:section:d000099:s000029`

Derive the values allowed by the selected configuration definition before contextual narrowing.

Use `EN_CONF_DATA_TYPE` to choose interpretation and `EN_CONF_RANGE` to construct the base domain.

#### Enumerated domain

Section ID: `ownkb:section:d000099:s000030`

Cautions: `do not`

When range rows provide discrete values, retain for each member:

- stored value;
- display name;
- default flag;
- ordering;
- digit width;
- step and min/max metadata where present.

Do not validate by display text alone; the wire carries the encoded stored value.

#### Numeric domain

Section ID: `ownkb:section:d000099:s000031`

When a definition supplies numeric bounds, validate:

```text
min_value ≤ candidate ≤ max_value
(candidate - min_value) mod step = 0
```

Apply the step test only when a meaningful nonzero step is defined. Preserve digit-width and padding separately from numeric validity.

#### Fixed, Boolean, padded, and user values

Section ID: `ownkb:section:d000099:s000032`

Cautions: `do not`

- Boolean properties must use the encoded values established by their definition; do not assume every Boolean uses arbitrary nonzero truth.
- Fixed values are not general input domains.
- `Range_Pad` values require both numeric validation and width-preserving encoding.
- `user_value` does not mean unrestricted; filters, conditions, and protocol capacity still apply.

A missing `EN_CONF_RANGE` row does not make the full `VAL_PAR` transport range valid.

#### Milestone output

Section ID: `ownkb:section:d000099:s000033`

Produce a base domain with provenance back to `id_conf` and the exact range rows used.

### 8. Apply Object/firmware filters

Section ID: `ownkb:section:d000099:s000034`

#### Goal

Section ID: `ownkb:section:d000099:s000035`

Applicability cues: `firmware`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`

Narrow the base property domain for the particular Object implementation on the selected firmware.

1. Resolve the applicable `AS_OBJECT_FIRMWARE.id_object_firmware` from milestone 4.
2. Find `EN_FILTER` rows that bind that association to the resolved `EN_CONF.id_conf`.
3. Apply the related `EN_FILTER_RANGE` rows.
4. Respect the filter’s `whole_range` behavior as represented by the catalogue.
5. Intersect the filtered domain with the base domain.
6. Do not combine filters belonging to another Object/firmware association.

Conceptually:

```text
effective domain =
    base EN_CONF_RANGE domain
  ∩ ranges admitted by the applicable EN_FILTER context
```

If a relevant filter exists but cannot be interpreted, mark the property unresolved rather than silently using the broader base range.

#### Milestone output

Section ID: `ownkb:section:d000099:s000036`

Produce the effective context-specific domain and retain the filter and filter-range identifiers that produced it.

### 9. Apply slot conditions and conversions

Section ID: `ownkb:section:d000099:s000037`

#### Goal

Section ID: `ownkb:section:d000099:s000038`

Cautions: `must not`
Provenance cues: `catalogue`, `evidence`

Determine whether the target Object/property is active in this slot and convert the intended semantic value into its catalogue/wire representation.

1. Load `AS_SLOT_CONDITION` for the resolved slot placement.
2. Resolve its `EN_CONDITION`.
3. Follow the selected `EN_CONV_RULE` logic.
4. Supply all referenced item-level and Object-level symbols from the candidate configuration.
5. Evaluate explicit comparisons, unconditional branches, and jumps in their stored order.
6. Use `CONF_SYMBOL_REF` where it explicitly relates an item symbol to an Object symbol for the system and slot.
7. Record the branch taken and the resulting value.

A conversion is not valid merely because its output fits `0..65535`. Revalidate the converted result against the effective domain.

`CONF_SYMBOL_REF` is supporting mapping evidence, not a global symbol-alias table. A symbol correspondence from one system or slot must not be applied universally.

#### Milestone output

Section ID: `ownkb:section:d000099:s000039`

Provenance cues: `catalogue`, `evidence`

Produce:

- satisfied/unsatisfied condition state;
- rule path;
- semantic input;
- converted catalogue value;
- evidence for any symbol correspondence.

Stop on a missing dependency, ambiguous branch, loop, or unmapped conversion output.

### 10. Apply linked-property rules

Section ID: `ownkb:section:d000099:s000040`

#### Goal

Section ID: `ownkb:section:d000099:s000041`

Provenance cues: `evidence`

Validate dependencies that cannot be decided from one property in isolation.

For Objects covered by `rules.db3`:

1. Confirm the resolved external Object number is one of the Objects represented there.
2. Bind expressions such as `$1`, `$2`, or `$21` to the corresponding resolved `EN_CONF.idx` only within that Object context.
3. Evaluate the rule using the complete candidate configuration, not only the changed property.
4. Apply `DisablelinkedParameter` behavior to dependent properties.
5. Re-run affected domains and write-eligibility classifications after a controlling value changes.

The current `rules.db3` evidence is limited to selected Temperature Control Objects. It is not a general Object, `WHO`, or parameter registry.

#### Milestone output

Section ID: `ownkb:section:d000099:s000042`

Produce a complete candidate property set in which all referenced dependencies have values and no enabled rule is violated.

### 11. Validate an address

Section ID: `ownkb:section:d000099:s000043`

#### Goal

Section ID: `ownkb:section:d000099:s000044`

Cautions: `do not`
Provenance cues: `database`

Prove that one Module address can be encoded as a valid `DIMENSION 32` write.

1. Resolve the target Object’s functional system.
2. Select the applicable `OPEN.db` address rule using the management family and Object/device family.
3. Resolve the rule’s component structure and fixed values.
4. Validate every component domain and level rule.
5. Apply required prefixes, padding, validity conditions, and advanced offsets.
6. Establish the Object-specific numeric `ADDR` encoding independently of the functional or management `WHERE` string. An address-rule template alone does not authorize copying group markers or routing suffixes into `ADDR`.
7. Resolve `SYS` independently; do not assume it equals a functional `WHO`, diagnostic `WHO`, or either database’s internal system ID.
8. Decode the generated value again and require a round-trip match.

The result is the tuple:

```text
(SLOT, SYS, raw ADDR, decoded components, address-rule identity)
```

Do not force every family into `A`/`PL`. Temperature Control, CEN/CEN+, Energy Management, Access Control, interface, group, and environment forms use distinct grammars.

See [Address Programming](address-programming.md) and [Address Discovery](../diagnostics/address-discovery.md).

### 12. Classify physical representation

Section ID: `ownkb:section:d000099:s000045`

#### Goal

Section ID: `ownkb:section:d000099:s000046`

Applicability cues: `firmware`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `documentation`, `evidence`, `source`

Determine whether the effective property could also be represented by physical configurators. This does not determine which configuration mode produced the installed value.

1. Confirm through `AS_FIRMWARE_CONFIG_MODE` and `EN_CONFIG_MODE` that the firmware supports the distinct Physical configuration mode.
2. Enumerate demonstrated physical firmware-scoped `EN_CONF` definitions; do not treat `idx = -1` alone as proof because the common `AID`/ID field shares that structure.
3. Resolve each physical symbol's legal domain through its exact `EN_CONF_RANGE`.
4. For an address, compare decoded `DIMENSION 32` components with applicable physical symbols such as `A` and `PL`.
5. For an indexed property, compare its resolved Object definition with applicable firmware physical symbols such as `M`, `TYPE`, `PRE`, or `G1`.
6. Compare symbol, semantic type, domain, filters, `CONF_SYMBOL_REF`, conversion rules, sparse `EN_PHY_TO_ADV_TRANS` evidence, product documentation, and captures where applicable.
7. Establish the physical domain independently from the programming transport domain.

Classify the result as:

| Classification | Meaning |
| --- | --- |
| direct counterpart | symbol and semantics match in the resolved context |
| mapped counterpart | different symbols, but a conversion or independently corroborated semantic mapping exists |
| physically representable | intended effective value lies in the established physical domain |
| outside established physical domain | a counterpart is established, but this value is not in its legal physical domain |
| no physical counterpart established | inspected evidence does not establish a counterpart; this is not proof that none exists |
| unresolved | required physical-interface or mapping evidence is insufficient |

The canonical catalogue registers Virtual Configuration and Advanced Configuration as distinct modes. `OPEN.db` separately labels `ConfConfigurators` as virtual configuration and `ConfKO` as advanced configuration. Do not replace these source labels with a single umbrella category or infer the active mode from effective values alone.

If physical configurator values are themselves being resolved into a topology, use the deterministic reachability and Object-selection method in [Catalogue Resolution](../internals/catalogue-resolution.md#physical-configuration-resolution) before property-level validation.

### 13. Encode programming tuples

Section ID: `ownkb:section:d000099:s000047`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `catalogue`

Only after semantic validation should values be converted into frames.

| Intended change | Validated output |
| --- | --- |
| Object selection | `(SLOT, EN_KEY_OBJECT.key_object)` for `DIMENSION 30` |
| Module address | `(SLOT, SYS, ADDR)` for `DIMENSION 32` |
| indexed property | `(INDEX, SLOT, VAL_PAR)` for `DIMENSION 35` |
| `ConfConfigurators` fields | twelve raw values for `DIMENSION 4` and `5`, subject to Device support and unresolved catalogue-position correlation |

For each encoded value retain:

- semantic intended value;
- raw user input;
- resolved Device, firmware, Module, and Object;
- `id_conf`, scope, and `idx`, where applicable;
- base and filtered domains;
- condition and conversion path;
- physical-representation classification;
- final wire value.

Perform an encode/decode round trip wherever a decoder exists. The result must reproduce the intended semantic value in the same context.

### 14. Validate the complete transfer

Section ID: `ownkb:section:d000099:s000048`

#### Goal

Section ID: `ownkb:section:d000099:s000049`

Cautions: `do not`

Prove that the entire payload is coherent before the canonical advanced sequence resets all Objects.

Validate the complete desired Device state, not merely changed fields:

1. Include every Module/Object assignment that must remain after reset-all.
2. Require unique Device-local `slot` positions.
3. Require every address and parameter to reference an Object included in the same candidate layout.
4. Order each Module’s Object assignment before its address and parameter writes.
5. Preserve fixed and untouched Modules in the replacement plan.
6. Re-evaluate conditions and linked rules after combining all candidate values.
7. Confirm that every required value is present and every omitted value is optional, fixed, read-only, unsupported, or deliberately preserved.
8. Confirm all encoded fields fit their `OPEN.db` transport ranges.
9. Prepare the expected diagnostic read-back for `DIMENSION 30`, `32`, and `35`.
10. Preserve a recovery copy of the prior effective state.

Because `ConfKO` begins with reset-all, partial validation is unsafe. Do not transmit the reset frame until this milestone succeeds.

### Validation result model

Section ID: `ownkb:section:d000099:s000050`

Cautions: `must not`
Uncertainty: `may`, `unknown`, `unresolved`
Provenance cues: `evidence`, `source`

Validation should return evidence, not only a Boolean.

| Result | Meaning |
| --- | --- |
| valid | allowed by the inspected constraints in the resolved context; runtime acceptance not yet verified |
| valid after conversion | allowed after a documented conversion path |
| conditionally valid | valid only while stated dependencies hold |
| physically representable | a physical counterpart and compatible physical value exist |
| outside established physical domain | valid in the resolved programming context but outside a demonstrated physical counterpart's domain |
| fixed/read-only | part of effective state but not an arbitrary write |
| invalid | excluded by an applicable capability, domain, filter, condition, or rule |
| ambiguous | more than one incompatible resolution remains |
| unresolved | required context or mapping is absent |

A useful validation record contains:

```text
status
reason
source evidence
resolved identifiers
candidate semantic value
encoded value
applicable domain
dependencies
warnings
expected read-back
```

Fail closed for programming when the status is ambiguous or unresolved. Diagnostics may preserve unknown values; programming must not transmit an invented interpretation.

### Revalidation triggers

Section ID: `ownkb:section:d000099:s000051`

Applicability cues: `firmware`
Cautions: `do not`

Restart validation from the earliest affected milestone when any of these change:

| Change | Restart at |
| --- | --- |
| Device identity or firmware | 1 |
| `slot` or Module layout | 2 |
| current Virgin Object or target Object | 3 |
| Object/firmware association | 4 |
| property or `INDEX` | 5 |
| controlling property value | 7 or 9 |
| functional system/address type | 11 |
| configuration method question | 12 |
| any member of the replacement payload | 14 |

Do not reuse a previously validated range after changing Object, firmware, slot, or a controlling property.

### Source boundaries

Section ID: `ownkb:section:d000099:s000052`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`, `documentation`, `evidence`, `source`

| Source | Validation authority |
| --- | --- |
| `MHCatalogue.db` | Device/firmware capability, Objects, slots, properties, domains, filters, conditions, and conversions |
| `rules.db3` | additional dependencies for selected Temperature Control Objects |
| `OPEN.db` | programming frames, transport ranges, address rules, sequence behavior, and errors |
| `OpenQuery.txt` | implementation queries used to assemble protocol scenarios |
| public OpenWebNet documents | shared functional meaning and public frame/address syntax |
| product documentation | physical configurator positions and product-specific behavior |
| observed traffic | runtime support, ordering, optional responses, and effective values |
| MyHOME_Suite UI | labels, selectable values, visibility, and workflow behavior |

Do not let a lower-level transport range override a narrower catalogue rule. When sources disagree, retain the discrepancy and the raw evidence rather than silently choosing the least restrictive interpretation.

# Document: ownkb:document:d000100

Source path: `programming/verification.md`
Namespace context: `contextual`
Area: `programming`

## Programming Verification

Section ID: `ownkb:section:d000100:s000001`

Verification compares the intended configuration with a new runtime projection after the programming session has ended.

### Why read-back is required

Section ID: `ownkb:section:d000100:s000002`

Cautions: `do not`

`WHAT 52` establishes successful completion of the advanced transfer as represented by `OPEN.db`. It does not prove that every optional parameter was managed, because `DIMENSION 39` warnings can coexist with continued configuration.

Virtual-configurator transfer has no `WHAT 52` member in its canonical sequence. Its Device end marker and echoed values likewise do not replace a later installed-state check.

### Verification procedure

Section ID: `ownkb:section:d000100:s000003`

Cautions: `warning`

1. Record whether transfer ended with success, warning, error, abort, or timeout.
2. Send the outer session close `*[WHO]*2*0##` when the canonical workflow reaches close.
3. Wait for the configured close interval.
4. Start a new diagnostic interview by Device ID when available.
5. Reconfirm `DIMENSION 1` identity and `DIMENSION 13` Device ID.
6. Resolve every `DIMENSION 30` record as an enabled regular Object when `STATE = 0` or a disabled Module's Virgin Object when `STATE = 1`.
7. Compare `DIMENSION 32` effective system/address tuples.
8. Compare `DIMENSION 35` indexed values using the resolved definitions.
9. Preserve `DIMENSION 310` separately.
10. Compare `DIMENSION 4` and `5` only as raw configurator reports until their precise semantics are established.
11. Classify each intended change independently.

### Result classes

Section ID: `ownkb:section:d000100:s000004`

Applicability cues: `firmware`
Cautions: `do not`

| Result | Meaning |
| --- | --- |
| Verified | read-back matches the intended effective state |
| Verified with warnings | intended state matches but programming reported nonfatal omissions |
| Contradicted | read-back reports a different effective value or Object |
| Unverifiable | the Device does not report the relevant optional data |
| Indeterminate | identity, timeout, or transport state prevents reliable comparison |

Do not compare only display strings. Retain raw frames, decoded values, Object/firmware context, and conversion rules.

### Object replacement checks

Section ID: `ownkb:section:d000100:s000005`

After `ConfKO`, verify the entire Module layout rather than only the edited slot because the sequence resets all Objects before rebuilding them. Confirm that fixed and untouched Modules remain present with their intended Objects and addresses.

### Physical and advanced values

Section ID: `ownkb:section:d000100:s000006`

Diagnostic read-back reports effective configuration, not necessarily the method used to create it. A value compatible with a physical configurator cannot prove that jumpers were used. A value outside the established physical range can exclude physical configuration for that property.

See [Device Interview](../diagnostics/device-interview.md), [`DIMENSION 30`](../diagnostics/dim30-modules.md), [`DIMENSION 32`](../diagnostics/dim32-addressing.md), and [`DIMENSION 35`](../diagnostics/dim35-configuration.md).

# Document: ownkb:document:d000101

Source path: `programming/what-reference.md`
Namespace context: `contextual`
Area: `programming`

## Programming `WHAT` Reference

Section ID: `ownkb:section:d000101:s000001`

Programming `WHAT` values control session entry, reset, transfer completion, acceptance, abort, and close. Their meaning is scoped to the active management `WHO` and programming sequence.

### Canonical values

Section ID: `ownkb:section:d000101:s000002`

Cautions: `must not`
Provenance cues: `evidence`

| `WHAT` | Direction | Frame | Meaning | Canonical use |
| --- | --- | --- | --- | --- |
| `1` | programmer → Device | `*[WHO]*1*[WHERE]##` | start programming by address | address and local-interaction entry |
| `2` | programmer → Device | `*[WHO]*2*0##` | end programming session | `CloseConf` |
| `3` | either direction | `*[WHO]*3*0##` | abort programming | abort/error path |
| `4` | Device → programmer | `*[WHO]*4*[WHERE_FAKE]##` | end Device transmission | entry and virtual transfer |
| `4` | programmer → Device | `*[WHO]*4*0##` | end programmer transfer | mandatory end of `ConfKO` payload |
| `9` | programmer → Device | `*[WHO]*9#[ID]*0##` | start programming by Device ID | ID-selected entry |
| `14` | programmer → Device | `*[WHO]*14#0*0##` | reset all Objects | mandatory start of `ConfKO` |
| `14` | programmer → Device | `*[WHO]*14#[SLOT]*0##` | reset one Object slot | registered, not in canonical `ConfKO` |
| `51` | Device → programmer | `*[WHO]*51*[WHERE_FAKE]##` | wrong configuration | fatal transfer result |
| `52` | Device → programmer | `*[WHO]*52*[WHERE_FAKE]##` | configuration accepted | advanced-transfer result |

`OPEN.db` also registers `*[WHO]*1*0##` as a general programming start, `*[WHO]*7*0##` as deleting stored configuration, and `WHERE = 0` variants of `WHAT 51` and `52`. They are not members of the three canonical programming scenarios and must not be inserted into those flows without independent evidence.

### `WHAT 1`: start by address

Section ID: `ownkb:section:d000101:s000003`

The addressed and local-interaction entry sequences use the same frame. Their timer policy distinguishes the canonical scenarios: 15 seconds for addressed selection and 300 seconds for local interaction.

The target `WHERE` follows the selected management family's address rules.

### `WHAT 9`: start by Device ID

Section ID: `ownkb:section:d000101:s000004`

Cautions: `must not`
Provenance cues: `catalogue`, `database`

`ID` has the database range `0..4294967295`. It identifies the installed Device instance and must not be replaced by a catalogue identifier.

### `WHAT 14`: reset Object configuration

Section ID: `ownkb:section:d000101:s000005`

Reset-all precedes every canonical `ConfKO` payload. It indicates replacement-style advanced configuration. The registered one-slot variant is not used by that sequence.

### `WHAT 4`: two directions

Section ID: `ownkb:section:d000101:s000006`

Cautions: `do not`

The two `WHAT 4` frames have different roles:

- Device `*[WHO]*4*[WHERE_FAKE]##` terminates the Device's current response stream.
- Programmer `*[WHO]*4*0##` declares the end of advanced Object writes and prompts the final result.

Do not normalize them into one directionless marker.

### `WHAT 51` and `52`

Section ID: `ownkb:section:d000101:s000007`

`WHAT 51` is an error and stops the advanced-transfer timer. `WHAT 52` stops that timer and starts the three-second acceptance wait before outer session close.

`ConfConfigurators` includes `WHAT 51` but not `WHAT 52`; its positive path ends through configurator reports and Device `WHAT 4`.

### `WHAT 2` and `3`

Section ID: `ownkb:section:d000101:s000008`

`WHAT 2` closes the outer programming session and stops `ConfTimeOut`.

`WHAT 3` is stored twice in `OPEN.db` with opposite directions. `OpenQuery.txt` explicitly loads the programmer abort frame. Direction and active session state determine whether the programmer or Device initiated termination.

### Namespace boundary

Section ID: `ownkb:section:d000101:s000009`

Cautions: `must not`

Equal `WHAT` values in diagnostics or functional control are independent. Diagnostic `WHAT 4` is also an end marker, but its lifecycle must not be substituted for the programming state machine solely because the number matches.

# Document: ownkb:document:d000102

Source path: `protocol/README.md`
Namespace context: `protocol`
Area: `protocol`

## Protocol

Section ID: `ownkb:section:d000102:s000001`

Applicability cues: `gateway`, `tcp`, `zigbee`
Cautions: `must not`

OpenWebNet is a delimiter-framed application protocol used to exchange commands, events, state, measurements, configuration data, and service information with compatible gateways and systems.

For the published TCP gateway workflow, two layers must not be collapsed:

1. a connection/session layer that selects commands, events, or programmed-scenario traffic and performs authentication where required;
2. an application-frame layer in which `WHO` selects a system and the remaining fields are interpreted in that system's grammar.

Other interfaces can carry OpenWebNet without this TCP session setup. The [ZigBee Interface](zigbee-interface.md) has distinct serial, addressing, acknowledgement, discovery, and management rules; selecting `WHO` alone is insufficient to establish the variant grammar.

### Reference

Section ID: `ownkb:section:d000102:s000002`

Applicability cues: `gateway`, `scs`, `tcp`, `zigbee`
Uncertainty: `unresolved`
Provenance cues: `source`

| Topic | Purpose |
| --- | --- |
| [Scope and Architecture](scope-and-architecture.md) | Encyclopedia boundary, interface applicability, mechanism ownership, and entity layers |
| [Frame Syntax](frame-syntax.md) | Common message families, delimiters, empty fields, and parameterized tags |
| [Connection and Sessions](sessions.md) | TCP gateway setup, session selectors, and session state |
| [Authentication](authentication.md) | Open-range behavior, legacy authentication boundary, and HMAC negotiation |
| [Stream Parsing](stream-parsing.md) | Incremental parsing, tokenization, request correlation, and defensive limits |
| [Addressing](addressing.md) | `WHERE` interpretation and the shared SCS A/PL routing model |
| [`WHAT`](what.md) | Command, state, and event selector semantics |
| [`DIMENSION`](dimensions.md) | Property request, report, and write forms |
| [Acknowledgements](acknowledgements.md) | `ACK`/`NACK` roles, including result-sequence termination |
| [ZigBee Interface](zigbee-interface.md) | Source-scoped serial variant, namespace applicability, and unresolved conflicts |

### Core fields

Section ID: `ownkb:section:d000102:s000003`

Provenance cues: `source`

| Concept | Purpose |
| --- | --- |
| `WHO` | Selects the functional, diagnostic, service, or connection-level namespace |
| `WHAT` | Identifies a command, event, or state within a `WHO` |
| `WHERE` | Identifies the destination or source according to that `WHO`'s address grammar |
| `DIMENSION` | Identifies a readable, reportable, or writable property within a `WHO` |
| `ACK` / `NACK` | Reports acceptance/failure or terminates a multi-frame response sequence |

`WHAT`, `WHERE`, and `DIMENSION` are not globally uniform namespaces. Resolve `WHO` and the frame family before interpreting them.

### Common application-frame families

Section ID: `ownkb:section:d000102:s000004`

| Purpose | Form |
| --- | --- |
| Command, state, or event | `*WHO*WHAT*WHERE##` |
| Status request | `*#WHO*WHERE##` |
| `DIMENSION` request | `*#WHO*WHERE*DIMENSION##` |
| `DIMENSION` response or report | `*#WHO*WHERE*DIMENSION*VALUE...##` |
| `DIMENSION` write | `*#WHO*WHERE*#DIMENSION*VALUE...##` |
| Positive acknowledgement | `*#*1##` |
| Negative acknowledgement | `*#*0##` |

The notation above describes structure, not a complete grammar. Fields can be empty or parameterized, and valid values depend on the selected system.

### Connection workflow

Section ID: `ownkb:section:d000102:s000005`

Applicability cues: `gateway`, `tcp`
Cautions: `must not`

For the published TCP gateway workflow:

1. connect to port `20000`;
2. receive the server greeting `ACK`;
3. select the commands/actions, events, or programmed-scenario session;
4. complete authentication if the gateway requires it;
5. exchange application frames according to the active session.

Session selectors such as `*99*9##` are connection-control frames. They must not be interpreted as ordinary functional `WHO 99` traffic.

### Interpretation order

Section ID: `ownkb:section:d000102:s000006`

Provenance cues: `catalogue`, `evidence`

A reliable implementation should process a message in this order:

1. recover the complete raw frame from the byte stream;
2. recognize acknowledgement, session-control, or application-frame structure;
3. resolve `WHO`;
4. parse `WHAT`, `WHERE`, and `DIMENSION` using the selected namespace;
5. validate operation-specific ranges;
6. where a physical Device is involved, validate the target Object's capability.

Syntactic validity does not prove that a Device supports an operation. The functional reference defines wire semantics; the [Device Model](../device-model/) and catalogue evidence define Device/Object applicability.

### Reference organization

Section ID: `ownkb:section:d000102:s000007`

Provenance cues: `catalogue`, `evidence`

This directory contains mechanics shared across systems. [Scope and Architecture](scope-and-architecture.md) defines the boundary between interfaces, runtime control, discovery, interview, configuration reading, programming, and catalogue capability. Functional commands and properties are organized by `WHO` under [`functional/`](../functional/). Diagnostic and programming protocols reuse the frame language but define separate operations, sequences, and evidence boundaries under [`diagnostics/`](../diagnostics/) and [`programming/`](../programming/).

### Evidence basis

Section ID: `ownkb:section:d000102:s000008`

Applicability cues: `tcp`
Provenance cues: `evidence`, `specification`

The common syntax and TCP session model are grounded in [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf). HMAC behavior is grounded in [Hmac specification](../sources/openwebnet-public/pdf/Hmac.pdf). System-specific semantics come from the corresponding public `WHO` document, MyHOME Suite implementation data, or explicitly identified observed traffic; those evidence classes are not treated as interchangeable.

# Document: ownkb:document:d000103

Source path: `protocol/acknowledgements.md`
Namespace context: `protocol`
Area: `protocol`

## Acknowledgements

Section ID: `ownkb:section:d000103:s000001`

Applicability cues: `gateway`, `tcp`, `zigbee`
Cautions: `do not`

`ACK` and `NACK` are standalone OpenWebNet frames. They contain no `WHO`, `WHAT`, `WHERE`, or `DIMENSION` field.

| Result | Frame |
| --- | --- |
| `ACK` | `*#*1##` |
| `NACK` | `*#*0##` |

Their meaning depends on the active connection state and operation. They are not globally equivalent to “the Device is now in the requested state.”

The roles below primarily follow the TCP gateway introduction. Product-specific extensions include L4686SDK `*#*x##` error forms and the [ZigBee Interface](zigbee-interface.md) BUSY NACK `*#*6##` followed by NACK. Do not reject or correlate these through a two-value acknowledgement model without the applicable interface context.

### Roles of `ACK`

Section ID: `ownkb:section:d000103:s000002`

Applicability cues: `gateway`, `tcp`

The canonical introduction uses `ACK` in several roles:

- the server greeting after a TCP connection opens;
- acceptance of a session selector;
- authentication negotiation or authentication success;
- positive processing result for a command or write;
- terminating marker after one or more status or `DIMENSION` response frames.

For a command or write, `ACK` indicates that the gateway considered the message syntactically and semantically acceptable in that interaction. It does not independently prove the final physical state of an actuator. When final state matters, request or observe the relevant state afterward.

### Roles of `NACK`

Section ID: `ownkb:section:d000103:s000003`

Uncertainty: `may`
Provenance cues: `specification`

`NACK` reports that the message or active operation failed semantic or syntactic processing. The frame contains no reason code.

In a multi-frame status or `DIMENSION` response, `NACK` can also terminate the sequence. The introductory specification states that the client may consider frames received earlier in that response sequence invalid. A client should therefore stage multi-frame results until it receives the terminating acknowledgement.

### Correlation

Section ID: `ownkb:section:d000103:s000004`

Applicability cues: `gateway`
Cautions: `do not`
Uncertainty: `unresolved`

OpenWebNet acknowledgement frames do not carry transaction identifiers. Correlation comes from connection state and request ordering.

On a command session, keep at most one unresolved request unless the specific gateway behavior proves that pipelining is supported. On an event session, do not attach an unrelated asynchronous event to a pending command merely because it arrives nearby in time.

### Error handling

Section ID: `ownkb:section:d000103:s000005`

Cautions: `do not`

When a `NACK` is received:

1. classify it using the active state: session selection, authentication, command/write, or result sequence;
2. discard or quarantine incomplete results where required;
3. do not invent an error reason absent another frame or implementation signal;
4. decide whether the session remains usable from the operation-specific workflow;
5. log the raw frame and state transition, redacting authentication data.

Connection closure can itself be the failure signal during authentication or unsupported negotiation.

### Evidence basis

Section ID: `ownkb:section:d000103:s000006`

Provenance cues: `specification`

The frame values, acceptance semantics, and end-of-sequence behavior come from [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf), particularly “Particular Open Messages” and the status/`DIMENSION` request sequences. Session-specific authentication behavior is refined by [Hmac specification](../sources/openwebnet-public/pdf/Hmac.pdf).

# Document: ownkb:document:d000104

Source path: `protocol/addressing.md`
Namespace context: `protocol`
Area: `protocol`

## Addressing

Section ID: `ownkb:section:d000104:s000001`

Applicability cues: `scs`, `zigbee`
Cautions: `must not`
Provenance cues: `source`

OpenWebNet addressing is system-specific. `WHERE` identifies the destination or source of a frame, but its grammar depends on the selected `WHO` and must not be interpreted as a single universal address type.

Resolve the interface/variant as well as `WHO`: the [ZigBee Interface](zigbee-interface.md) uses product/unit addresses with `#9` even for namespaces such as Lighting and Automation. The `A`/`PL` and routing material below concerns the SCS sources.

### Address interpretation

Section ID: `ownkb:section:d000104:s000002`

Applicability cues: `scs`
Cautions: `must not`

A parser must resolve `WHO` before interpreting `WHERE`. Different systems can use different address layouts, ranges, hierarchy levels, and advanced-address forms.

Lighting (`WHO 1`) and Automation (`WHO 2`) share the SCS `A`/`PL` address family, but their published `WHERE` tables are not identical. Common point, area, group, and general forms can therefore be described together only where both specifications agree; less common local-bus variants must remain `WHO`-specific.

Other systems, such as Thermoregulation and Energy Management, use different grammars and must not be decoded with the `A`/`PL` rules below.

### Lighting and Automation A/PL grammar

Section ID: `ownkb:section:d000104:s000003`

#### Common private-riser forms

Section ID: `ownkb:section:d000104:s000004`

The published `WHO 1` and `WHO 2` specifications agree on these base forms:

| Scope | `WHERE` syntax | Valid values |
| --- | --- | --- |
| General | `0` | complete system selected by `WHO` |
| Environment / area | `A` | `00`, `1..9`, or `100` |
| Point to point | `APL` | valid combinations listed below |
| Group | `#GR` | `GR = 1..255` |

The labels *environment*, *ambient*, and *area* are used by different sources for the same collective `A` level. The meaning remains scoped to the selected functional `WHO`.

#### Point-to-point A/PL

Section ID: `ownkb:section:d000104:s000005`

A point address is the concatenation of its `A` and `PL` representations; it is not an arbitrary decimal integer.

| `A` representation | Valid `PL` | Examples |
| --- | --- | --- |
| `1..9` | `1..9` | `11`, `56`, `99` |
| `00` | `01..15` | `0001`, `0015` |
| `10` | `01..15` | `1001`, `1015` |
| `01..09` | `10..15` | `0110`, `0915` |

The ordinary physical-configurator range therefore produces two-digit point addresses such as `56`. Extended values produce four-digit forms such as `0015`, `0311`, or `1014`. A three-digit string is not a valid representation of this grammar: leading zeroes are required to keep the `A`/`PL` boundary unambiguous.

For example, `56` is `A=5, PL=6`; `0311` is `A=03, PL=11`; and `1014` is `A=10, PL=14`. Converting `WHERE` to an integer before parsing would destroy information required to distinguish these forms.

#### Collective addresses

Section ID: `ownkb:section:d000104:s000006`

Cautions: `must not`

`WHERE=0` is the general address and targets the complete functional system selected by `WHO`.

An environment/area address contains only the `A` component. Valid forms are `1..9`, `00`, and `100`. In particular, `100` is the collective address for `A=10`; it is not a point address.

A group address is explicitly marked by `#`: `#1..#255`. The prefix is part of the protocol syntax, so a group must not be represented as the bare decimal group number.

### Routing qualifiers

Section ID: `ownkb:section:d000104:s000007`

Provenance cues: `specification`

The public specifications and MyHOME Suite implementation data are most coherently represented as a **base address plus an optional routing qualifier**:

```text
BASE
BASE#3
BASE#4#INTERFACE
```

`BASE` is the functional target: General, Area, Group, or point where that combination is defined by the selected `WHO`. `INTERFACE` is the address of the routing interface. The `Int` label used by the `WHO 1` specification, the `interface` label used by `WHO 2`, and the `I3`/`I4` components used by MyHOME Suite describe the same interface-address concept in their respective notations.

`#3` selects the riser/backbone level. `#4#INTERFACE` selects a local bus reached through the specified interface. These suffixes are therefore routing qualifications of a target address rather than new point-address formats.

#### Level 3 / riser

Section ID: `ownkb:section:d000104:s000008`

Cautions: `do not`
Provenance cues: `evidence`

MyHOME Suite's address-rule model contains separate level-rule fields and supports a Level-3/riser qualification layer. A wire form such as `BASE#3`, when established for the selected system and operation, should be retained structurally: the qualifier is not part of `A`, `PL`, or a group number.

The preserved public `WHO 1` table describes unqualified private-riser targets and explicit Level-4 forms; it does not itself enumerate `BASE#3` variants. Level-3 applicability is therefore implementation/address-rule evidence in this corpus, not a published universal Lighting grammar. Do not generate `0#3`, `A#3`, `#GR#3`, or `APL#3` merely from the generalized model without system- and operation-specific evidence.

#### Level 4 / local bus

Section ID: `ownkb:section:d000104:s000009`

Applicability cues: `scs`
Provenance cues: `source`

Local-bus addressing is the Level-4 routing form:

```text
BASE#4#INTERFACE
```

`INTERFACE` is the routing-interface address. The published specifications use different labels for the same field: `Int` in `WHO 1` and `interface` in `WHO 2`; MyHOME Suite represents its components as `I3`/`I4`.

The combined Light/Automation model in MyHOME Suite supports an inferred shared SCS routing concept, not proof of every functional command combination. The following four forms are explicitly enumerated by the Lighting source; the Automation source establishes only the point form:

| Scope | Level-4 `WHERE` form |
| --- | --- |
| General | `0#4#INTERFACE` |
| Area | `A#4#INTERFACE` |
| Group | `#GR#4#INTERFACE` |
| Point to point | `APL#4#INTERFACE` |

##### Interface address components `I3` and `I4`

Section ID: `ownkb:section:d000104:s000010`

Applicability cues: `scs`
Cautions: `avoid`, `do not`
Provenance cues: `documentation`, `evidence`, `source`

`INTERFACE` is not merely an integer formatted as two decimal digits. In the SCS configuration model it is formed from the interface configurator positions `I3` and `I4`. For the F422 SCS/SCS interface these positions identify the interface within the installation; in modes that use an A/PL-like interface address, they are assigned with the same structure as the normal `A` and `PL` positions:

```text
I3 ≈ A
I4 ≈ PL
INTERFACE = I3I4
```

The distinction is historical and structural: `I3` and `I4` are separate SCS configuration positions, not a protocol-level split of an abstract decimal number into tens and units.

Their exact role depends on the operating mode of the interface. In F422 physical-expansion mode (`MOD=1`), `I3` and `I4` define the **separation address** between the two connected bus sections. For example, `I3=3, I4=2` establishes separation address `32`: Automation addresses below that boundary belong on the lower-address side and addresses above it on the higher-address side. In logical-expansion mode (`MOD=2`), the interface address is again assigned using the A/PL method; documentation also permits `I3=0, I4=1..9` to avoid consuming an ordinary `11..99` Automation address.

Consequently, a wire value such as `#4#03` should be preserved structurally as interface address `I3=0, I4=3`, rather than normalized to integer `3`. Leading zeroes can therefore carry address-component information just as they do in extended A/PL addressing.

This configurator-level explanation and the OpenWebNet routing syntax describe different layers of the same concept: `I3`/`I4` define the SCS interface address, while `#4#INTERFACE` uses that address to qualify a functional target as being on the local bus reached through that interface.

The public `WHO 1` material explicitly enumerates all four forms. The public `WHO 2` document shows the point form `APL#4#interface`. General, Area, and Group local-bus commands under `WHO 2` remain unestablished by these sources; do not generate them solely by analogy with Lighting or the shared management-system row.

The source documents differ in the range they state for the interface field: the Lighting document gives `01..09` and `11..15`, while the Automation document expresses it as `[0-1][1-9]` (`01..09`, `11..19`). This is a source-level constraint discrepancy within the shared concept. Implementations should preserve that discrepancy until Device/interface evidence establishes whether the broader range is universally valid.

Examples include `13#4#03` for point `A=1, PL=3` through interface `03`, and `0311#4#12` for extended point `A=03, PL=11` through interface `12`.

### Parsing rules

Section ID: `ownkb:section:d000104:s000011`

An implementation should preserve the raw `WHERE` string and classify it using the grammar for the selected `WHO`. Resolve the functional system first, recognize structural markers such as `#` before numeric conversion, preserve leading zeroes, validate the complete syntactic form and its ranges, and only then expose structured components such as `A`, `PL`, group, or interface.

A syntactically valid address is not necessarily applicable to every Device or Object. Device capabilities, Object family, system rules, and operation-specific restrictions can further constrain which addresses are meaningful.

### Cross-source interpretation

Section ID: `ownkb:section:d000104:s000012`

Provenance cues: `catalogue`, `database`, `evidence`, `source`, `specification`

Three source layers contribute different kinds of evidence:

| Source | What it establishes |
| --- | --- |
| Published OpenWebNet `WHO 1` specification | Lighting `WHERE` grammar, including General/Area/Group/point local-bus variants and the Lighting interface range |
| Published OpenWebNet `WHO 2` specification | Automation General/Area/Group/point grammar and its point local-bus/interface rule |
| MyHOME Suite `OPEN.db` | Address-rule templates and applicability used by MyHOME Suite management workflows |

The public functional specifications are authoritative for functional `WHO 1`/`WHO 2` wire syntax. `OPEN.db` is complementary implementation evidence: `EN_ADDRESS_RULE` and `AS_SYSTEM_ADDRESS_RULE` show that MyHOME Suite selects address rules by system and, for some rules, by Object/Device family.

For the combined Light/Automation system, `OPEN.db` records a general virtual form `[A][PL]` with advanced form `[A][PL]+`, plus F422 logic/physical-extension forms `[I3][I4]` and `[I3][I4]+`. Together with the separate `level_2_rule` and `level_4_rule` fields, this supports modeling advanced addressing as qualification/routing layered onto a base address. The `+` notation belongs to the database's address-rule vocabulary; it should not be emitted literally as part of an OpenWebNet `WHERE`, and it does not by itself establish which qualifier combinations are legal for a particular functional `WHO`.

The database also contains `validity_rule`, `object_device_family`, `level_2_rule`, `level_4_rule`, and `offset_adv`. These fields are evidence that syntactic range validation alone is insufficient for every managed Object. Where an address rule is family-qualified, its `object_device_family` correlates with the catalogue Object-family model; applicability should be resolved before encoding a Device-specific management address.

### Other WHO families

Section ID: `ownkb:section:d000104:s000013`

Cautions: `must not`
Provenance cues: `documentation`

The `A`/`PL` grammar above must not be treated as a global OpenWebNet address grammar. MyHOME Suite itself records different address-rule structures for other managed families, including Thermoregulation, Video Door Entry, Energy Management, Access Control, and interface systems.

Their canonical functional `WHERE` syntax belongs in the relevant `WHO` documentation. The common rule is only that `WHERE` is parsed in the context of `WHO`, not that all systems share a common numeric address space.

See the relevant functional `WHO` addressing page for system-specific applicability, [Frame Syntax](frame-syntax.md) for the position of `WHERE` in OpenWebNet frames, and [MyHOME Suite OPEN.db Coverage](../functional/open-db-coverage.md) for the implementation address-rule inventory.

# Document: ownkb:document:d000105

Source path: `protocol/authentication.md`
Namespace context: `protocol`
Area: `protocol`

## Authentication

Section ID: `ownkb:section:d000105:s000001`

Applicability cues: `gateway`

OpenWebNet authentication occurs after the client selects a connection session and before normal session traffic is accepted. It authenticates the client to the OpenWebNet server; it does **not** encrypt or integrity-protect subsequent functional traffic.

A gateway can also allow configured client IP addresses to connect without an OPEN password. A client must follow the server's response rather than assume that every connection enters a challenge.

### Authentication selection

Section ID: `ownkb:section:d000105:s000002`

Provenance cues: `specification`

The HMAC specification adds an optional algorithm-declaration frame sent by the server after session selection:

| Server frame | Authentication method |
| --- | --- |
| No `*98*Y##` declaration; legacy challenge follows | Legacy OPEN password algorithm |
| `*98*1##` | HMAC using SHA-1 |
| `*98*2##` | HMAC using SHA-256 |

A client that supports the declared method answers with `ACK`. If it answers `NACK`, the server closes the connection. If the client's address is in the configured open range, authentication can be skipped even when HMAC support exists.

`WHO 98` here is a connection-negotiation namespace, not an ordinary functional system.

### Legacy OPEN authentication

Section ID: `ownkb:section:d000105:s000003`

Applicability cues: `gateway`
Cautions: `must not`
Provenance cues: `specification`

The introductory specification establishes that password-protected sessions can use the older OPEN challenge-response algorithm. In this mode the server sends an operations/challenge frame rather than an HMAC declaration, and the client computes the legacy password response.

The detailed transformation is historically documented outside the canonical files currently preserved in this repository. This reference therefore records the negotiation boundary without reproducing an unverified implementation from a third-party library.

An implementation should keep the legacy algorithm behind a dedicated compatibility interface and test it against a real gateway. It must not log the challenge, password, or computed response at normal verbosity.

### HMAC Simple Authentication Mode

Section ID: `ownkb:section:d000105:s000004`

Provenance cues: `specification`

The canonical HMAC specification defines client authentication using a pre-shared key derived from the OPEN password.

| Symbol | Meaning |
| --- | --- |
| `Ra` | Server-generated random value |
| `Rb` | Client-generated random value |
| `Kab` | Password-derived pre-shared key |
| `A` | Client identity string defined by the specification |
| `B` | Server identity string defined by the specification |

For SHA-1, the random values, key, and digests are 160 bits. For SHA-256, they are 256 bits. `Kab` is the SHA digest of the OPEN password using the negotiated digest family.

The exchange has three cryptographic steps:

1. The server sends `Ra`.
2. The client generates `Rb` and returns `Rb` with the client proof over `Ra`, `Rb`, the two role identities, and `Kab`.
3. The server returns its confirmation over `Ra`, `Rb`, and `Kab`.

The client must verify the server confirmation and then send `*#*1##` to finish the published handshake. A server confirmation is not itself permission to skip this final client acknowledgement. If authentication fails, the connection is closed. The specification calls for a 60-second authentication suspension after three failed handshakes within 60 seconds.

### Wire encoding

Section ID: `ownkb:section:d000105:s000005`

Cautions: `do not`

The HMAC document uses decimal characters for binary values because ordinary OpenWebNet tags do not contain hexadecimal letters. Each binary byte is split into two hexadecimal nibbles, and each nibble is encoded as a two-digit decimal number in `00..15`.

| Byte | Nibbles | OpenWebNet representation |
| --- | --- | --- |
| `0x01` | `0`, `1` | `0001` |
| `0x0A` | `0`, `A` | `0010` |
| `0xFF` | `F`, `F` | `1515` |

A 20-byte SHA-1 value therefore occupies 80 decimal characters on the wire; a 32-byte SHA-256 value occupies 128.

This transport representation is not the input representation used by the hash calculation. Implementations should keep functions for binary values, hash-input serialization, and OpenWebNet wire encoding separate.

### Proof calculation and source discrepancy

Section ID: `ownkb:section:d000105:s000006`

Applicability cues: `gateway`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `source`, `specification`

The document calls this scheme HMAC, but describes its proof operation as SHA-1 or SHA-256 over concatenated fields. It does not describe the standard keyed HMAC inner/outer-pad construction. Substituting a library's generic `HMAC(key, message)` operation is therefore not justified by the protocol name.

For the negotiated hash `H`, the published layout is:

```text
Kab = H(OPEN_PASSWORD)
client_proof = H(hex(Ra) || hex(Rb) || A || B || hex(Kab))
server_proof = H(hex(Ra) || hex(Rb) || hex(Kab))
```

Here `hex` means lowercase hexadecimal text with two characters per byte; `||` means concatenation without separators. This is the hash-input representation, not the decimal-nibble transport representation. The password is the permitted alphanumeric character string.

The identity constants need special care. The source pairs the client label `copen` with `736F70653E` and the server label `sopen` with `636F70653E`. Those hex strings decode to `sope>` and `cope>`, respectively, and do not match the accompanying labels. This reference preserves that discrepancy rather than inventing corrected constants. Interoperable implementations need an independently verified gateway transcript or implementation source to resolve it.

The published exchange, with transport-encoded binary values, is:

| Direction | Frame |
| --- | --- |
| Server → client | `*#Ra##` |
| Client → server | `*#Rb*CLIENT_PROOF##` |
| Server → client | `*#SERVER_PROOF##` |
| Client → server, after verification | `*#*1##` |

See the authentication specification's printed pages 2–3 and 7–8 for the proof layout and serialization. The unresolved identity-constant discrepancy prevents treating this page as a complete, independently verified implementation recipe.

### Password constraints and security boundary

Section ID: `ownkb:section:d000105:s000007`

Applicability cues: `tcp`
Cautions: `do not`
Provenance cues: `specification`

The HMAC specification permits an OPEN password of up to 30 alphanumeric characters and leaves minimum-length policy to applications.

Neither legacy nor HMAC authentication makes the later connection confidential. Deployments should not expose TCP port `20000` to untrusted networks and should use an external protected transport or trusted network boundary where confidentiality and integrity are required.

Do not place passwords, derived keys, nonces, proofs, or complete authentication frames in logs.

### Implementation checklist

Section ID: `ownkb:section:d000105:s000008`

- Wait for the initial server `ACK`.
- Select the required session.
- Branch on open-range acceptance, an HMAC declaration, or a legacy challenge.
- Reject unsupported declarations instead of silently changing the digest.
- Generate `Rb` with a cryptographically secure random generator.
- Compare proofs without timing-dependent early exit where practical.
- Begin functional parsing only after authentication succeeds.

### Evidence basis

Section ID: `ownkb:section:d000105:s000009`

Applicability cues: `version`
Provenance cues: `specification`

The HMAC algorithm, declaration frames, value encoding, password format, and failure behavior come from [Hmac specification](../sources/openwebnet-public/pdf/Hmac.pdf), version 1.1. The connection position and open-range exception are corroborated by [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf).

# Document: ownkb:document:d000106

Source path: `protocol/dimensions.md`
Namespace context: `protocol`
Area: `protocol`

## `DIMENSION`

Section ID: `ownkb:section:d000106:s000001`

A `DIMENSION` identifies a property, query, or structured operation within an OpenWebNet `WHO`. It can be requested, reported asynchronously, returned in a response, or-where explicitly supported-written.

The complete identity is not always just `(WHO, DIMENSION)`. A `DIMENSION` selector can contain `#`-separated parameters:

```text
DIMENSION#PARAMETER#PARAMETER
```

These parameters select a particular instance, sub-property, `slot`, priority context, or operation variant. The `*`-separated fields following the selector are the ordered payload values:

```text
DIMENSION#PARAMETER#PARAMETER*VALUE*VALUE
```

Implementations must preserve this boundary. Selector parameters and payload values are not interchangeable.

### General frame forms

Section ID: `ownkb:section:d000106:s000002`

| Operation | Flat selector | Parameterized selector |
| --- | --- | --- |
| Request | `*#WHO*WHERE*DIMENSION##` | `*#WHO*WHERE*DIMENSION#P1#P2##` |
| Response/report | `*#WHO*WHERE*DIMENSION*V1*V2##` | `*#WHO*WHERE*DIMENSION#P1#P2*V1*V2##` |
| Write | `*#WHO*WHERE*#DIMENSION*V1*V2##` | `*#WHO*WHERE*#DIMENSION#P1#P2*V1*V2##` |

`P1`, `P2`, `V1`, and `V2` are notation, not literal wire values. A particular `DIMENSION` can define zero, one, or several selector parameters and zero, one, or several payload values.

The actual arity and meaning are defined by the selected `WHO` and `DIMENSION`. The table describes the reusable structural pattern, not permission to append arbitrary parameters.

### Three different uses of `#`

Section ID: `ownkb:section:d000106:s000003`

The same character participates in several layers:

| Position | Example | Meaning |
| --- | --- | --- |
| Before `WHO` | `*#WHO...` | Selects the request/`DIMENSION` frame family |
| Before a writable selector | `*#WHO*WHERE*#DIMENSION...` | Marks a `DIMENSION` write |
| Inside the selector | `DIMENSION#P1#P2` | Separates parameters belonging to that selector |

The leading write marker and selector parameters can occur together:

```text
#DIMENSION#P1#P2
```

This is one major `*`-delimited field. It is not a series of independent frame fields.

### Selector parameters versus payload values

Section ID: `ownkb:section:d000106:s000004`

Consider the abstract response:

```text
*#WHO*WHERE*32#7*SYSTEM*ADDRESS##
```

Here:

- `32` is the `DIMENSION` identifier;
- `7` is a selector parameter, for example a `slot`;
- `SYSTEM` and `ADDRESS` are payload values.

The equivalent structured representation is:

```text
selector = {
  dimension: "32",
  parameters: ["7"]
}
values = ["SYSTEM", "ADDRESS"]
```

It would be incorrect to parse the field as `DIMENSION=32`, then treat `7`, `SYSTEM`, and `ADDRESS` as three equivalent values. It would also be incorrect to describe `SYSTEM` and `ADDRESS` as `#`-separated simply because the selector is parameterized: payload values remain separated by `*`.

### Concrete patterns

Section ID: `ownkb:section:d000106:s000005`

#### Flat selector with multiple values

Section ID: `ownkb:section:d000106:s000006`

Lighting temporization uses a flat `DIMENSION 2` selector and three payload values:

```text
*#1*WHERE*#2*HOURS*MINUTES*SECONDS##
```

`HOURS`, `MINUTES`, and `SECONDS` are values; none is part of the selector.

#### Parameterized write selector

Section ID: `ownkb:section:d000106:s000007`

Advanced Automation absolute positioning uses a parameter attached to the writable selector:

```text
*#2*WHERE*#11#SHUTTER_PRIORITY*SHUTTER_LEVEL##
```

`SHUTTER_PRIORITY` belongs to the `DIMENSION 11` selector. `SHUTTER_LEVEL` is the payload value.

#### Parameterized diagnostic selector

Section ID: `ownkb:section:d000106:s000008`

Diagnostic operations use selectors such as `32#SLOT`, where `SLOT` identifies the Device-local `slot`. The following `SYS` and `ADDR` fields are ordinary `*`-separated payload values:

```text
*#DIAGNOSTIC_WHO*DEVICE*32#SLOT*SYS*ADDR##
```

This distinction is essential when correlating a response with a Device Module: the `slot` is addressing the property instance, while `SYS` and `ADDR` describe its configured functional address.

### Requests, responses, and reports

Section ID: `ownkb:section:d000106:s000009`

Cautions: `do not`
Uncertainty: `may`
Provenance cues: `source`

A request supplies the selector but normally no payload:

```text
*#WHO*WHERE*DIMENSION#P1##
```

A response ordinarily repeats enough context to identify the reported property and appends its values:

```text
*#WHO*WHERE*DIMENSION#P1*V1*V2##
```

The same response-shaped frame can appear asynchronously on an events session. Direction and session state therefore distinguish a solicited response from an unsolicited report; syntax alone may not.

The request and response selectors need not be equal: published [Temperature Control Fault Diagnostics](../diagnostics/temperature-control-faults.md) includes a `DIMENSION 20` request returning `DIMENSION 21` records. [Sound Diffusion](../functional/who-22-sound-diffusion/) also uses differing request and response source addresses. The generic forms above do not override those operation-specific mappings.

A collective request can produce multiple response frames followed by `ACK`. Do not assume one request yields one value frame. If the sequence terminates in `NACK`, the common protocol permits the preceding provisional results to be treated as invalid.

### Writes

Section ID: `ownkb:section:d000106:s000010`

A write prefixes the complete selector with `#`:

```text
*#WHO*WHERE*#DIMENSION#P1*V1##
```

The write marker does not remove the selector's own parameters. A parser can represent this cleanly as:

```text
operation = "write"
dimension = "DIMENSION"
selector_parameters = ["P1"]
values = ["V1"]
```

The existence of a readable or reportable `DIMENSION` does not imply write support. Read, report, and write capability must be established separately for the exact selector and target Object.

### Arity and typing

Section ID: `ownkb:section:d000106:s000011`

Provenance cues: `specification`

Neither parameter count nor value count is globally fixed. The available public specification establishes no protocol-wide maximum count for selector parameters or payload values, and it does not specify a universal maximum frame length. This absence of a common limit does not make the arity unrestricted for a particular operation: the exact `(WHO, DIMENSION, operation)` definition determines which counts are valid.

System-specific definitions can impose:

- exact or variable selector-parameter counts;
- exact or variable payload counts;
- decimal ranges or enumerations;
- fixed-width strings and significant leading zeroes;
- encoded temperatures, times, masks, identifiers, or text;
- relationships between selector parameters and the number or meaning of values.

Keep raw fields as strings until the applicable `(WHO, DIMENSION)` grammar is known. Premature integer conversion can destroy leading zeroes, empty values, fixed-width identifiers, and encoded structure.

### Semantic identity

Section ID: `ownkb:section:d000106:s000012`

Applicability cues: `firmware`
Cautions: `do not`

For a flat property, `(WHO, DIMENSION)` can be sufficient to select the value grammar. For a parameterized property, use at least:

```text
(WHO, DIMENSION, SELECTOR_PARAMETERS)
```

Interpretation can additionally depend on `WHERE`, direction, session, Device firmware, Module/Object capability, and whether the frame is a request, response, report, or write.

Equal numeric `DIMENSION` identifiers in different `WHO` namespaces do not imply equal meaning. Equal selectors on different Device Objects do not prove equal support or value ranges.

### Parser model

Section ID: `ownkb:section:d000106:s000013`

Cautions: `do not`

A practical parser should:

1. identify the `DIMENSION` frame family from `*#WHO`;
2. split only the major `*`-delimited fields, preserving empty fields;
3. detect and remove the leading write marker from the selector field;
4. split the remaining selector field on `#` into the identifier and selector parameters;
5. retain the following major fields as ordered payload values;
6. resolve the system-specific grammar before converting types;
7. validate operation direction and target capability separately.

Do not globally split the entire frame on both `*` and `#`; doing so erases the difference between selector parameters, payload values, and parameterized `WHERE` or `WHAT` fields.

### Evidence basis

Section ID: `ownkb:section:d000106:s000014`

Provenance cues: `specification`

Flat request, response, and write forms come from [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf). Parameterized selectors are established by the dedicated functional specifications and the MyHOME Suite diagnostic/programming templates, including advanced Automation `DIMENSION 11` and diagnostic slot-qualified selectors.

See [Frame Syntax](frame-syntax.md), [Stream Parsing](stream-parsing.md), [Addressing](addressing.md), the relevant functional `WHO` page, and the [Diagnostic `DIMENSION` Reference](../diagnostics/dimension-reference.md).

# Document: ownkb:document:d000107

Source path: `protocol/frame-syntax.md`
Namespace context: `protocol`
Area: `protocol`

## Frame Syntax

Section ID: `ownkb:section:d000107:s000001`

Provenance cues: `specification`

An ordinary OpenWebNet frame is an ASCII message that begins with `*`, contains `*`-separated tags, and ends with `##`.

```text
*tag1*tag2*...*tagN##
```

The introductory specification limits ordinary frame characters to decimal digits, `*`, and `#`. The meaning and permitted structure of each tag depend on the frame family and selected `WHO`.

### Common frame forms

Section ID: `ownkb:section:d000107:s000002`

| Frame class | Syntax | Purpose |
| --- | --- | --- |
| Command/status/event | `*WHO*WHAT*WHERE##` | Command, reported state, or asynchronous event |
| Status request | `*#WHO*WHERE##` | Request current state |
| `DIMENSION` request | `*#WHO*WHERE*DIMENSION##` | Request a property value |
| `DIMENSION` response/report | `*#WHO*WHERE*DIMENSION*VALUE...##` | Return or asynchronously report a property value |
| `DIMENSION` write | `*#WHO*WHERE*#DIMENSION*VALUE...##` | Write a supported property |
| `ACK` | `*#*1##` | Positive result or sequence terminator |
| `NACK` | `*#*0##` | Negative result or failed-sequence terminator |

`VALUE...` is notation used by this reference for the ordered value fields defined by that `DIMENSION`; the ellipsis is not transmitted.

Connection selectors and authentication frames use the same outer delimiters but have their own state-dependent grammars. See [Connection and Sessions](sessions.md) and [Authentication](authentication.md).

### Delimiters and empty tags

Section ID: `ownkb:section:d000107:s000003`

| Token | Role |
| --- | --- |
| `*` | Starts a frame and separates major tags |
| `##` | Terminates a frame |
| `#` | Participates in a frame variant or parameterized field according to context |

Tags can be empty. For example, `*#13**1##` contains an intentionally empty `WHERE`. A tokenizer must preserve that empty field rather than collapsing adjacent separators.

`#` has no single context-independent meaning. It can introduce a request family, prefix a writable `DIMENSION`, mark a group address, add routing qualifiers, or separate operation-specific parameters.

### Command, status, and event frames

Section ID: `ownkb:section:d000107:s000004`

The form `*WHO*WHAT*WHERE##` is direction- and session-dependent:

- in a commands/actions session, the client uses it to request an action;
- the server can use it to answer a status request;
- in an events session, it reports an asynchronous state change or event.

`WHAT` and `WHERE` can each contain `#`-introduced parameters when defined by the selected `WHO`. Parse them only after resolving the system.

### Status requests

Section ID: `ownkb:section:d000107:s000005`

A status request has form `*#WHO*WHERE##`. If `WHERE` is omitted where the system permits it, the request can address the complete system.

The server can return one or more normal command/status frames. The response sequence ends with `ACK` on success or `NACK` on failure; it is not safe to assume a single result frame.

### `DIMENSION` operations

Section ID: `ownkb:section:d000107:s000006`

Provenance cues: `source`

A read request identifies `WHO`, `WHERE`, and `DIMENSION`. A response carries the context of the reported property and ordered values, but need not repeat the request's selector or address literally. For example, the published `WHO 1004 DIMENSION 20` collective fault request returns `DIMENSION 21` zone records; Sound Diffusion can report a source address different from its request address. Correlate using the operation-specific response grammar. The same response form can also appear asynchronously on an events connection when a value changes or is reported periodically.

A write prefixes the `DIMENSION` selector with `#`. A syntactically valid write does not imply that the selected property is writable.

Some systems parameterize the selector itself. For example, diagnostic `32#SLOT` selects `DIMENSION 32` for one `slot`; the following `SYS` and `ADDR` remain ordinary `*`-separated values. The `#` inside the selector does not replace the major-field delimiter.

### Field scope

Section ID: `ownkb:section:d000107:s000007`

Cautions: `do not`

The semantic identity of a field includes its namespace and structural role:

- an operation is at least `(WHO, WHAT)` plus any `WHAT` parameters and target context;
- an address is `(WHO, WHERE)`;
- a property is at least `(WHO, DIMENSION)` plus selector parameters;
- user-facing meaning can additionally depend on the target Object.

Equal numeric values in different `WHO` namespaces do not imply equal meaning.

### Parsing requirements

Section ID: `ownkb:section:d000107:s000008`

Cautions: `do not`

Do not parse OpenWebNet with a single delimiter split and immediate integer conversion. Preserve the raw frame, recognize the family, preserve empty tags and leading zeroes, and then apply field-specific grammars.

See [Stream Parsing](stream-parsing.md) for an incremental parser model, [Addressing](addressing.md) for `WHERE`, [`WHAT`](what.md), [`DIMENSION`](dimensions.md), and [Acknowledgements](acknowledgements.md).

### Evidence basis

Section ID: `ownkb:section:d000107:s000009`

Provenance cues: `database`, `source`, `specification`

The common frame forms, alphabet, empty-tag rule, request/response direction, and acknowledgement-terminated sequences come from [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf). System-specific extensions are documented only where the relevant `WHO` source, implementation database, or observed workflow establishes them.

# Document: ownkb:document:d000108

Source path: `protocol/scope-and-architecture.md`
Namespace context: `protocol`
Area: `protocol`

## OpenWebNet Scope and Architecture

Section ID: `ownkb:section:d000108:s000001`

Applicability cues: `firmware`, `scs`, `zigbee`
Provenance cues: `catalogue`

The encyclopedia covers technologies to the extent that OpenWebNet exposes, represents, transports, configures, or controls them. A bus, radio network, product catalogue, configuration application, or firmware subsystem belongs here only where it establishes an OpenWebNet-visible interface or the applicability of that interface.

This boundary includes SCS and ZigBee-backed behavior that is visible through OpenWebNet. It does not make either underlying technology synonymous with OpenWebNet, and it does not extend the encyclopedia into unrelated SCS electrical design, ZigBee radio internals, or a vendor application's private implementation.

### Architectural layers

Section ID: `ownkb:section:d000108:s000002`

Applicability cues: `firmware`, `zigbee`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`

| Layer | Canonical treatment | Boundary |
| --- | --- | --- |
| Interface and transport | [Connection and Sessions](sessions.md), [ZigBee Interface](zigbee-interface.md) | Establishes how OpenWebNet frames are carried for an applicable interface; one interface's setup and retry rules do not automatically apply to another. |
| Common frame mechanics | [Frame Syntax](frame-syntax.md), [Addressing](addressing.md), [`WHAT`](what.md), [`DIMENSION`](dimensions.md), and [Acknowledgements](acknowledgements.md) | Defines shared structure only where the applicable sources agree; it does not supply namespace-specific values or Device support. |
| Runtime functional control | [`functional/`](../functional/) | Each functional `WHO` owns its command, event, state, address, and functional-property semantics. Runtime control does not discover a product model or program its stored configuration merely because fields look similar. |
| Device discovery | [Device Discovery](../diagnostics/device-discovery.md) and [Address Discovery](../diagnostics/address-discovery.md) | Finds or selects installed Physical Device instances. Enumeration does not constitute a Device interview. |
| Device interview | [Device Interview](../diagnostics/device-interview.md) | Reads identity, versions, health, Modules, Objects, and addresses reported for one selected Physical Device. It does not by itself provide every detailed configuration value. |
| Detailed configuration reading | [`DIMENSION 35`: Configuration Parameters](../diagnostics/dim35-configuration.md) | Reads the diagnostic projection of indexed configuration where the target supports the operation. The unresolved `DIMENSION 38` effect boundary remains part of this treatment. |
| Programming | [`programming/`](../programming/) | Requests stored configuration changes through the applicable management workflow. Acceptance of a request is distinct from diagnostic verification of effective state. |
| Catalogue capability | [`device-model/`](../device-model/) | Describes products, firmware definitions, possible Modules, Objects, and constraints. Catalogue capability is not installed runtime state. |
| Suite implementation | [`internals/`](../internals/) and [`scenario-engine/`](../scenario-engine/) | Describes implementation artifacts and application capability within their demonstrated versions; it is not universal protocol behavior. |

These layers can participate in one workflow without becoming the same mechanism. For example, discovery can select a Physical Device for interview, interview can establish the Module/Object context needed for a configuration read, programming can request a change, and a new interview can verify effective state.

### Interface and variant applicability

Section ID: `ownkb:section:d000108:s000003`

Applicability cues: `scs`, `zigbee`
Cautions: `do not`
Provenance cues: `documentation`, `evidence`, `specification`

OpenWebNet frame delimiters or a shared `WHO` number do not establish that two interfaces use the same sessions, `WHERE` grammar, acknowledgement behavior, operations, or Device support.

The SCS-oriented public references and MyHOME Suite management data support much of the common and management documentation. The supplied ZigBee specification describes a separate serial interface with product/unit addressing, interface-specific acknowledgement behavior, `WHO 1000` discovery, and separate management and binding surfaces. Its cross-cutting applicability is canonical on the [ZigBee Interface](zigbee-interface.md); operation semantics belong under the relevant functional `WHO` or mechanism page when evidence supports them.

### Entity and identity boundaries

Section ID: `ownkb:section:d000108:s000004`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`, `source`

The canonical Device hierarchy is defined in the [Device Model](../device-model/). The following wire and catalogue identities remain distinct:

| Concept | Role | Canonical boundary |
| --- | --- | --- |
| Catalogue Device record and SKU | Describes a product model offered by the catalogue | Not an installed Physical Device ID or protocol address |
| Physical Device | One installed hardware product instance | Can expose several Modules, Objects, and functional addresses |
| Installed Device ID | Selects or identifies an installed instance in supported management workflows | Not `EN_DEVICE.id_device`, a SKU, an Object number, or a functional address |
| Diagnostic `WHERE` | Selects or contextualizes a management response according to its diagnostic family | Does not replace the installed Device ID or a Module's configured address |
| Functional `WHERE` | Selects a runtime target according to one functional `WHO` and interface variant | Not a universal Physical Device identity |
| Module and `slot` | Module is the firmware-exposed logical container; `slot` is its numeric protocol/catalogue position | Neither is a Physical Device or an Object |
| Object and Virgin Object | Object is a regular configured logical function; Virgin Object is a configurable capability template and is the identity used by `DIMENSION 30` while a Module is disabled | Their external numbers and database keys remain separate namespaces |
| Configuration | Instance-specific values and associations interpreted in resolved Device, firmware, Module, and Object context | A configuration index is not a functional `WHAT`, `WHERE`, or scenario parameter merely because values coincide |

[Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md) owns the detailed cross-source namespace rules. Functional pages own runtime wire semantics; the Device Model owns catalogue entities; Diagnostics owns reported installed state; Programming owns write workflows.

### Canonical placement rule

Section ID: `ownkb:section:d000108:s000005`

Uncertainty: `may`
Provenance cues: `catalogue`

Common wire mechanics live under Protocol. Namespace-specific runtime behavior lives under its functional `WHO`. Entity definitions and catalogue relationships live under Device Model. Discovery, interview, and configuration reading live under Diagnostics. Configuration writes live under Programming.

Other pages may retain enough local context to explain a workflow. Substantial definitions and reference tables should link to these owners. Practical Guides may repeat operational material needed for independent execution, but their copies must preserve the canonical applicability and uncertainty qualifications.

# Document: ownkb:document:d000109

Source path: `protocol/sessions.md`
Namespace context: `protocol`
Area: `protocol`

## Connection and Sessions

Section ID: `ownkb:section:d000109:s000001`

Applicability cues: `gateway`, `tcp`

OpenWebNet application frames are exchanged inside a connection to an OpenWebNet server. The public introduction specifies TCP port `20000` for an IP gateway and separates connection establishment into three phases:

1. establish the transport connection;
2. identify the requested session and, when required, authenticate;
3. exchange frames according to the selected session.

The framing language is transport-independent in principle, but the session selectors and sequences on this page describe the published TCP/IP gateway workflow.

### Initial server acknowledgement

Section ID: `ownkb:section:d000109:s000002`

Applicability cues: `tcp`
Cautions: `do not`, `must not`
Provenance cues: `specification`

After accepting a TCP connection, the server sends `*#*1##`. The client must receive this initial `ACK` before selecting a session.

| Session | Selector | Direction after setup | Purpose |
| --- | --- | --- | --- |
| Commands/actions | `*99*9##` | Primarily client to server, with replies | Send commands; request status or `DIMENSION` values; write supported `DIMENSION` values |
| Events | `*99*1##` | Server to client | Receive asynchronous bus events and property reports |
| Programmed scenario | `*99*0##` | Server to client in the published example | Forward traffic while programming an F420/03551 scenario module in configuration mode |

After the selector, the server can accept an open-range connection with `*#*1##`, send a legacy challenge, or declare HMAC with `*98*1##` or `*98*2##`. Do not require a separate selector `ACK` before accepting an authentication frame: the HMAC specification shows the declaration immediately after the client selector. Normal traffic begins only after the selected setup path completes.

These selectors belong to connection setup. They are not functional `WHO 99` commands and must not be fed to the ordinary functional-frame dispatcher.

### Commands/actions session

Section ID: `ownkb:section:d000109:s000003`

Applicability cues: `gateway`
Cautions: `do not`

The commands/actions session is request-oriented. A client can send command frames, status requests, `DIMENSION` requests, and supported `DIMENSION` writes.

A command or write normally receives `ACK` or `NACK`. A status or `DIMENSION` request can produce one or more result frames followed by a terminating acknowledgement. See [Acknowledgements](acknowledgements.md).

Do not assume one response frame per request. The selected `WHERE`, gateway, and functional system can cause a request to expand into multiple reports.

### Events session

Section ID: `ownkb:section:d000109:s000004`

Cautions: `must not`

After `*99*1##` is accepted, the server forwards asynchronous OpenWebNet traffic. The published example includes ordinary command/status frames from more than one `WHO`; the connection is therefore a bus-event stream, not a subscription to one functional namespace.

An event connection is generally long-lived. A client should parse the byte stream incrementally, preserve arrival order, tolerate multiple complete frames in one transport read, retain `WHO`-specific parsing for each emitted frame, and reconnect and repeat session selection after transport failure.

The public introduction does not define per-`WHO` subscription filters or delivery guarantees. Implementations must not infer them.

### Programmed scenario session

Section ID: `ownkb:section:d000109:s000005`

Applicability cues: `gateway`
Provenance cues: `source`

The selector `*99*0##` is documented for programming an F420 (BTicino) or 03551 (Legrand) scenario module through Ethernet while that module is in configuration mode.

This is a specialized gateway session. It is distinct from functional scenario activation through `WHO 0`, scenario management through `WHO 17`, the MyHOME Suite scenario engine, and diagnostic or Device-programming workflows.

The public source gives the session boundary and selector but not a general-purpose programming API. The functional F420 frames are documented under [`WHO 0`](../functional/who-0-scenarios/).

### Authentication branch

Section ID: `ownkb:section:d000109:s000006`

Applicability cues: `gateway`

A gateway can allow configured client IP addresses to connect without an OPEN password. Otherwise, session selection is followed by either the legacy OPEN challenge-response algorithm or the declared HMAC workflow.

Authentication establishes client access; it does not encrypt later OpenWebNet traffic. See [Authentication](authentication.md).

### State-machine requirements

Section ID: `ownkb:section:d000109:s000007`

Cautions: `do not`

A robust client should explicitly model these states:

| State | Accepted input |
| --- | --- |
| Awaiting server greeting | Initial `ACK` |
| Awaiting session result | Open-range `ACK`, legacy challenge, HMAC declaration, `NACK`, or connection close |
| Authenticating | Frames belonging to the negotiated authentication method |
| Active command session | Requests plus their result sequences |
| Active event session | Asynchronous OpenWebNet frames |
| Closed/failed | Reconnect from the transport layer |

Do not treat every `ACK` as equivalent. Its role is determined by the current state: greeting, selector acceptance, authentication result, operation result, or end-of-sequence marker.

### Evidence basis

Section ID: `ownkb:section:d000109:s000008`

Applicability cues: `gateway`, `tcp`
Provenance cues: `specification`

The session selectors, TCP port, and basic sequences come from [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf), pages 6–10. HMAC negotiation is specified separately in [Hmac specification](../sources/openwebnet-public/pdf/Hmac.pdf). Observed gateway behavior can refine compatibility handling, but should not silently replace these published sequences.

# Document: ownkb:document:d000110

Source path: `protocol/stream-parsing.md`
Namespace context: `protocol`
Area: `protocol`

## Stream Parsing

Section ID: `ownkb:section:d000110:s000001`

OpenWebNet frames are application messages carried over a transport stream. A transport read is not a frame boundary: one read can contain part of a frame, exactly one frame, or several consecutive frames.

A parser should consume bytes incrementally and emit a frame only after the terminating `##` has been received.

### Character set

Section ID: `ownkb:section:d000110:s000002`

Cautions: `do not`
Provenance cues: `specification`

The introductory specification defines ordinary OpenWebNet frames using decimal digits `0..9`, `*`, and `#`. A frame begins with `*` and ends with `##`. Major tags are separated by `*`. A tag can contain decimal digits and `#`, and empty tags are permitted.

Do not apply this ordinary-frame alphabet blindly to other transport layers or vendor extensions. Validate at the layer whose grammar is being parsed.

### Incremental algorithm

Section ID: `ownkb:section:d000110:s000003`

1. Find `*` as the start of a candidate frame.
2. Append subsequent bytes to a bounded buffer.
3. When the buffer ends in `##`, emit the complete raw frame.
4. Continue with bytes remaining in the same transport read.
5. On length, character, or timeout failure, diagnose the malformed candidate and resynchronize at the next plausible `*`.

Preserve the exact raw frame. Numeric conversion belongs to later semantic decoding.

### Parsing layers

Section ID: `ownkb:section:d000110:s000004`

| Layer | Responsibility |
| --- | --- |
| Stream framing | Find the leading `*` and terminating `##` |
| Tag tokenization | Split major fields on `*` while preserving empty fields |
| Frame-family recognition | Distinguish acknowledgement, session, command/status, request, response, and write forms |
| Field grammar | Parse parameterized `WHAT`, `WHERE`, or `DIMENSION` selectors |
| System semantics | Interpret values only after resolving `WHO` |
| Capability validation | Check whether the target Device/Object supports the operation |

This order prevents errors such as converting a `WHERE` to an integer before preserving leading zeroes or splitting every `#` as though it had one global role.

### Empty tags

Section ID: `ownkb:section:d000110:s000005`

Applicability cues: `gateway`

The canonical syntax permits omitted tags. Empty fields are significant in frames such as gateway-management requests where `WHERE` is intentionally empty.

For example, tokenizing `*#13**1##` must retain the empty field between the two `*` delimiters. Removing empty strings shifts `DIMENSION 1` into the wrong position.

### Parameter separators

Section ID: `ownkb:section:d000110:s000006`

`#` is interpreted inside the grammar of its enclosing field. It can appear in a parameterized `WHAT`, a qualified `WHERE`, a write selector such as `#DIMENSION`, or a parameterized diagnostic selector such as `32#SLOT`. It is not a universal separator at the frame-tokenization layer.

### Request correlation

Section ID: `ownkb:section:d000110:s000007`

Applicability cues: `gateway`
Cautions: `avoid`
Provenance cues: `specification`

A command connection can receive a single acknowledgement, one or more result frames followed by `ACK`, or provisional frames followed by `NACK`.

Because the public protocol defines no transaction identifier, avoid overlapping requests on one command session unless the gateway and operation explicitly support it. On a result sequence terminated by `NACK`, the introductory specification permits the client to regard earlier frames in that sequence as invalid.

### Limits and recovery

Section ID: `ownkb:section:d000110:s000008`

Applicability cues: `only for`

The public introduction does not specify a universal maximum frame length, request timeout, or result count. Use configurable defensive limits rather than invented protocol constants:

- bound the receive buffer and incomplete-frame lifetime;
- never execute a partial frame;
- retain malformed raw input only for opt-in diagnostics;
- redact authentication material;
- close or resynchronize according to the connection's trust boundary.

### Encoding model

Section ID: `ownkb:section:d000110:s000009`

Keep protocol values as strings until their field grammar has been identified. This preserves leading zeroes, fixed-width Device IDs, empty fields, routing qualifiers, and encoded values that merely look decimal.

Only the system-specific decoder should expose typed integers, temperatures, durations, masks, or identifiers.

### Evidence basis

Section ID: `ownkb:section:d000110:s000010`

Applicability cues: `tcp`
Provenance cues: `specification`

The character set, delimiters, empty-tag rule, and common frame families come from [OpenWebNet Introduction specification](../sources/openwebnet-public/pdf/OWN_Intro_ENG.pdf). The incremental transport guidance is an implementation consequence of delimiter-framed messages over TCP; it is identified as parser guidance rather than a quoted protocol guarantee.

# Document: ownkb:document:d000111

Source path: `protocol/what.md`
Namespace context: `protocol`
Area: `protocol`

## `WHAT`

Section ID: `ownkb:section:d000111:s000001`

`WHAT` identifies a command, state, or event within an OpenWebNet `WHO`.

A `WHAT` value is meaningful only in the context of its `WHO`. The semantic identity of an operation is therefore `(WHO, WHAT)`, not `WHAT` alone.

### Frame position

Section ID: `ownkb:section:d000111:s000002`

Cautions: `must not`

The normal command/status form is `*WHO*WHAT*WHERE##`.

`WHAT` can include parameters introduced with `#` when defined by the selected system. Parameter structure is part of the `WHAT` grammar for that `WHO` and must not be interpreted globally.

### Scope

Section ID: `ownkb:section:d000111:s000003`

Provenance cues: `documentation`

A numeric `WHAT` value can have unrelated meanings in different systems. Implementations should therefore resolve `WHO` before interpreting `WHAT`.

System-specific `WHAT` reference tables belong with the corresponding functional or diagnostic system documentation rather than in a global value table.

### Relationship to `DIMENSION`

Section ID: `ownkb:section:d000111:s000004`

`WHAT` represents commands, states, and events expressed through the normal frame family. Properties read or written through `*#WHO...` frames are identified by `DIMENSION` instead. See [`DIMENSION`](dimensions.md).

The distinction is structural rather than purely semantic: the same real-world function can expose command behavior through `WHAT` and state or configuration data through one or more `DIMENSION` identifiers.

See [Frame Syntax](frame-syntax.md) for the common frame forms and [Addressing](addressing.md) for `WHERE` interpretation.

# Document: ownkb:document:d000112

Source path: `protocol/zigbee-interface.md`
Namespace context: `protocol`
Area: `protocol`

## ZigBee OpenWebNet Interface

Section ID: `ownkb:section:d000112:s000001`

Applicability cues: `version`, `zigbee`
Uncertainty: `unresolved`
Provenance cues: `evidence`, `source`, `specification`

This page records the interface-specific boundary established by the supplied Legrand [ZigBee OpenWebNet Specification](../sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf), version 4.0, 22 November 2016. It is specification evidence, not a tested interoperability claim. The document carries Confidential footers; its public-release provenance remains unresolved as recorded in the [Source-Coverage Audit](../project/review/phase-3-source-coverage.md).

### Transport and addressing

Section ID: `ownkb:section:d000112:s000002`

Applicability cues: `revision`, `scs`, `tcp`, `zigbee`
Cautions: `do not`, `not evidence`
Provenance cues: `evidence`, `source`

Section 2.3 specifies serial communication at 19200 baud, eight data bits, one stop bit, and no parity for the described interfaces. The same section says the USB interface can increase its baud rate up to 115200 baud, but it defines no OpenWebNet negotiation command, host-side selection procedure, or revision applicability for that higher rate. Treat 19200 baud as the documented base setting and 115200 baud as a source-stated optional USB capability, not a universal default. The TCP session selectors and authentication workflow documented elsewhere are not prerequisites established for this serial interface.

Section 3 retains the OpenWebNet delimiters and principal frame classes but defines its own `WHERE`:

| Form | Source meaning |
| --- | --- |
| `PRODUCT_DECIMAL` + `UNIT` + `#9` | Unicast; concatenate the decimal representation of the product's last four MAC-address bytes with the two-character unit, then append `#9` |
| `0#UNIT#9` | Broadcast to the selected unit; unit `00` selects all units |
| `#` transmission prefix | Multicast marked not implemented in this source revision |

These are symbolic forms, not observed installation identifiers. They are not SCS `A`/`PL` addresses. The suffix named `SYS` by this document is a `WHERE` family marker; it is not evidence for the numeric payload `SYS` in Suite `DIMENSION 32`. The four-byte address component does not by itself establish identity with the Suite diagnostic Physical Device ID namespace.

Section 3.3 limits broadcast sending to no more than one per second. It warns that exceeding this rate can saturate the ZigBee network and cause products to miss traffic during the following eight seconds. Preserve this interface-specific constraint; do not infer a protocol-wide throughput limit.

The source presents the abstract form `*WHO*WHAT*WHERE*WHEN##`, but section 3.5 explicitly states that `WHEN` is never used by this interface. Its operational command/status, request, parameterized `DIMENSION`, response/report, and write forms are instances of the canonical structures in [Frame Syntax](frame-syntax.md) and [`DIMENSION`](dimensions.md); ZigBee-specific `WHERE` parsing still follows the rules above.

Section 4 states that only products compatible with the source's ZigBee network 2.1 profile can be managed by this interface. This is an applicability limit of the documented interface revision, not evidence that all ZigBee products expose OpenWebNet.

### Acknowledgement behavior

Section ID: `ownkb:section:d000112:s000003`

Applicability cues: `tcp`
Provenance cues: `source`

Sections 3.6 through 3.9 define `ACK = *#*1##`, `NACK = *#*0##`, and `BUSY NACK = *#*6##`. For this interface the source says a BUSY NACK is followed by a NACK and instructs waiting 500 milliseconds before retrying the same frame. A receiver must retain that two-frame result rather than attributing the following NACK to a new command. This is not a generic retry rule for TCP gateways.

### Namespace and management boundaries

Section ID: `ownkb:section:d000112:s000004`

Applicability cues: `firmware`, `gateway`, `scs`, `version`, `zigbee`
Cautions: `not evidence`
Provenance cues: `database`, `evidence`, `source`

Section 3.1 lists `WHO 1`, `2`, `4`, `13`, `18`, `25`, and diagnostic `1000`. A shared `WHO` number does not establish identical operations, ranges, addressing, or support to the SCS-oriented references. The source's label "Diagnostic" for `WHO 1000` does not make its neighbor-table mechanism equivalent to the MyHOME Suite diagnostic families.

Canonical runtime semantics remain organized under the relevant functional namespace. The current owners are [`WHO 1`](../functional/who-1-lighting/), [`WHO 2`](../functional/who-2-automation/), [`WHO 4`](../functional/who-4-temperature-control/), [`WHO 13`](../functional/who-13-integration-gateway/), [`WHO 18`](../functional/who-18-energy-management/), and [`WHO 25`](../functional/who-25-transversal/). This interface page owns cross-cutting transport, addressing, acknowledgement behavior, discovery architecture, and applicability limits; it does not create a second set of functional command definitions.

| Mechanism | Evidence and limit |
| --- | --- |
| Neighbor discovery | Section 5.3 defines `WHO 1000 DIMENSION 81` as a router-neighbor traversal. Its detailed grammar and evidence limits are documented below. |
| Interface product inventory | Sections 5.4, 6, and 11 define `WHO 13` Scan and product-database operations. See [ZigBee Network Management](../functional/who-13-integration-gateway/zigbee-network-management.md). |
| Binding | Section 13 defines OpenWebNet-visible binding operations under `WHO 25`. See [ZigBee Binding](../functional/who-25-transversal/zigbee-binding.md); the SCS virtual-button grammar is not a complete account of this variant. |
| Firmware boundary | Version readout and boot-mode handoff are OpenWebNet-visible; a handoff is not evidence that the subsequent upload protocol is OpenWebNet. |

Detailed ZigBee semantics for `WHO 1`, `2`, `4`, `13`, `18`, and `25` are integrated under their canonical functional namespaces. The discovery architecture and `WHO 1000 DIMENSION 81` semantics are canonical on this page.

### Discovery and product inventory

Section ID: `ownkb:section:d000112:s000005`

Applicability cues: `version`, `zigbee`
Uncertainty: `not established`
Provenance cues: `catalogue`, `database`, `source`, `specification`

ZigBee OpenWebNet version 4.0 exposes more than one way to learn about ZigBee products. The mechanisms are related by the installation they describe, but the source does not make their result sets interchangeable.

| Mechanism | What the source exposes | Persistence or reachability established |
| --- | --- | --- |
| `WHO 1000 DIMENSION 81` | neighbor information reported by the interface or an addressed ZigBee router | neighbor-table freshness, aging, and persistence are not defined |
| `WHO 13 WHAT 65` plus `DIMENSION 67`, `73`, and `66` | Scan plus the interface's stored product database and product-information queries | database persistence and stale-entry behavior are partly specified; current reachability is a separate question |
| MyHOME Suite diagnostic discovery | diagnostic-family enumeration and Physical Device interview, such as `WHO 1001 DIMENSION 13` | not established by this ZigBee interface specification |

The source describes two principal ZigBee product categories for this interface: `ZR` (ZigBee Router), described there as mains-powered, and `ZED` (ZigBee End Device), described there as battery-powered. These are source-defined ZigBee categories for the interface. They are not aliases for the encyclopedia's Physical Device, Module, Object, or catalogue entities.

#### Neighbor discovery - `WHO 1000 DIMENSION 81`

Section ID: `ownkb:section:d000112:s000006`

Applicability cues: `version`, `zigbee`
Uncertainty: `unknown`
Provenance cues: `database`, `evidence`, `source`, `specification`

**Evidence status:** specification evidence from section 5.3 of ZigBee OpenWebNet version 4.0. The source provides the complete illustrated exchange but does not provide a separate field-definition table for `DIMENSION 81`.

The documented first step queries the OpenWebNet ZigBee interface itself:

```text
Client -> ZigBee interface: *#1000**81##
ZigBee interface -> Client: *#1000**81#ROW*UNKNOWN*NEIGHBOR##
ZigBee interface -> Client: *#*1##
```

The response form is repeated once for each reported entry and a final `ACK` terminates the sequence. The symbolic fields above replace installation-derived identifiers from the source examples.

The documented second step queries each newly discovered router through the interface:

```text
Client -> ZigBee interface: *#1000*ROUTER00#9*81##
ZigBee interface -> Client: *#1000*ROUTER00#9*81#ROW*UNKNOWN*NEIGHBOR##
ZigBee interface -> Client: *#*1##
```

Here `ROUTER00#9` uses the source's ZigBee product-address form with Unit `00`. It selects the router whose neighbor information is being requested; it is not a MyHOME Suite Physical Device ID.

| Response element | Source-bounded interpretation |
| --- | --- |
| response `WHERE` | empty when the interface's own neighbors are returned; the addressed router `WHERE` when a router is queried |
| `ROW` | the example increments this field from zero for successive responses; the source does not name it or establish cursor, resume, persistence, or product-database-index semantics |
| `UNKNOWN` | an additional numeric response field whose meaning is not defined anywhere in the inspected source |
| `NEIGHBOR` | a returned ZigBee product-address component; the source uses a newly discovered router value to construct the next router-addressed request |
| final `ACK` | explicit end of that neighbor response sequence |

Calling the process recursive is a description of the client traversal, not terminology supplied by the specification. The source explicitly says that after querying the interface, the second step is to ask each newly discovered `ZR` for its neighbors, and it states that this sequence can obtain the products of the installation. The documented traversal therefore continues through newly discovered routers.

The documented procedure does not query `ZED` entries recursively. The source does not state that a `ZED` must reject `DIMENSION 81`; support for such a request is **Unknown**. No end-Device recursion should be inferred.

#### Neighbor-table limits

Section ID: `ownkb:section:d000112:s000007`

Cautions: `must not`
Uncertainty: `unresolved`
Provenance cues: `database`, `evidence`, `source`, `specification`

The source calls the returned entries "known neighbors." It does not define neighbor-table freshness, aging, radio reachability criteria, or persistence. Therefore `DIMENSION 81` is established as a topology or neighbor-traversal mechanism, but it is **Unresolved** whether every returned entry is currently reachable at the instant of the query.

The source does not define a duplicate-elimination rule. In one router-addressed example, a returned neighbor identifier is equal to the queried router identifier. The source does not explain whether that is intended semantics, an example defect, or evidence about the unnamed fields. A client must not assume that `DIMENSION 81` yields a duplicate-free graph solely from this specification.

No `DIMENSION 81` maximum entry count, paging rule, request cursor, or numeric termination sentinel is specified. Completion is the final `ACK`. The interface-wide `NACK` and BUSY behavior described under [Acknowledgement behavior](#acknowledgement-behavior) remains applicable as general interface syntax, but section 5.3 assigns no `DIMENSION 81`-specific meaning to `NACK` or BUSY.

The product database's documented 175-product capacity does not establish a 175-entry limit for a neighbor response. These are separate mechanisms.

#### Relationship to Scan and the product database

Section ID: `ownkb:section:d000112:s000008`

Applicability cues: `gateway`, `zigbee`
Provenance cues: `database`

Section 5.4 presents `WHO 13 WHAT 65` Scan as another discovery sequence. Scan broadcasts over the ZigBee network so active routers and awake end Devices can answer. Approximately 13 seconds after an accepted Scan, the interface reports `DIMENSION 67`.

The detailed `WHO 13` definition makes an important distinction: the reported `DIMENSION 67` value is the number of products stored in the interface product database, not merely the number of active routers observed by that Scan. Indexed `DIMENSION 73` reads the stored product identifier and power category from that database, while `DIMENSION 66` can contact a product to retrieve Unit/end-point Device-ID information and can report that a stored product is unreachable.

These semantics are canonical in [ZigBee Network Management](../functional/who-13-integration-gateway/zigbee-network-management.md#scan-and-product-database). Neighbor discovery does not replace that inventory model, and product-database membership does not prove current reachability.

#### Relationship to Suite diagnostics

Section ID: `ownkb:section:d000112:s000009`

Applicability cues: `zigbee`
Provenance cues: `database`, `evidence`, `source`

The MyHOME Suite diagnostic workflows documented under [Diagnostics](../diagnostics/) use different management families, identifiers, enumeration operations, and Physical Device interview semantics. In particular, `WHO 1001 DIMENSION 13` Device-ID enumeration is not a renamed form of ZigBee `WHO 1000 DIMENSION 81`.

No inspected source establishes a mapping between ZigBee product identifiers, ZigBee product-database indexes, and MyHOME Suite Physical Device IDs. The three discovery/inventory surfaces must remain separate unless future evidence establishes a relationship.

### Preserved source conflicts

Section ID: `ownkb:section:d000112:s000010`

Applicability cues: `scs`, `zigbee`
Cautions: `do not`
Uncertainty: `contradictory`, `unresolved`
Provenance cues: `evidence`, `source`

| Question | Conflicting source locations | Current conclusion |
| --- | --- | --- |
| Automation UP value | PDF page 11 labels a `WHAT 2` example UP; page 38 assigns UP to `1` and DOWN to `2` | Preserve the conflict; do not use the example to redefine Automation direction. Applicable interface evidence is required. |
| Energy reset value | PDF page 53 summary gives `0`; the detailed reset frame uses `75` | Unresolved for this variant. SCS `WHAT 75` is not independent confirmation of the ZigBee operation. |
| Energy Frequency/Energy mapping | PDF page 53 Frequency use case uses `DIMENSION 51`; pages 54-55 define `51` as Energy and `112` as Frequency | Preserve the conflict. The detailed table and definitions do not erase the contradictory use case. |

No private address from the source examples is reproduced here. Functional sections 8 through 13 have now received operation-level reconciliation for `WHO 1`, `2`, `4`, `13`, `18`, and `25`; their detailed evidence decisions are recorded in the [ZigBee Functional Reconciliation](../project/review/zigbee-functional-reconciliation.md) and the earlier [ZigBee Reconciliation Review](../project/review/zigbee-reconciliation.md). The `WHO 1000` discovery mechanism and sections 5 and 6 product-inventory flows are reconciled in [ZigBee Discovery and Inventory Reconciliation](../project/review/zigbee-discovery-inventory-reconciliation.md). The complete source-wide audit is recorded in the [ZigBee Final Source Completeness Certification](../project/review/zigbee-final-source-completeness-certification.md).

# Document: ownkb:document:d000113

Source path: `reverse-engineering/README.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Reverse Engineering

Section ID: `ownkb:section:d000113:s000001`

Provenance cues: `documentation`, `evidence`

This section explains how OpenWebNet and MyHOME Suite relationships are recovered from implementation data, observed traffic, public specifications, product documentation, and controlled application behavior.

It is a reproducible research record, not a second protocol reference. Stable operational results belong in [Protocol](../protocol/), [Functional Reference](../functional/), [Device Model](../device-model/), [Diagnostics](../diagnostics/), [Programming](../programming/), [Practical Guides](../guides/), [Scenario Engine](../scenario-engine/), or [MyHOME Suite Internals](../internals/). This section preserves the evidence path, confidence boundary, competing explanations, rejected shortcuts, and remaining questions.

### Reference

Section ID: `ownkb:section:d000113:s000002`

Applicability cues: `revision`
Uncertainty: `hypothesis`
Provenance cues: `capture`, `catalogue`, `database`, `evidence`, `source`

| Subject | Page |
| --- | --- |
| End-to-end investigation workflow and promotion criteria | [Methodology](methodology.md) |
| Evidence classes, claim-level confidence, negative evidence, and revision drift | [Evidence and Confidence](evidence-and-confidence.md) |
| Recovering undeclared database relationships without altering source evidence | [Database Relationship Reconstruction](database-relationship-reconstruction.md) |
| Consolidated established, inferred, open, and sentinel-dependent relationships | [Relationship Register](relationship-register.md) |
| Safely connecting wire values, catalogue capability, validation, and scenario models | [Cross-Database Correlation](cross-database-correlation.md) |
| Capturing, segmenting, correlating, and publishing runtime traffic | [Capture Analysis](capture-analysis.md) |
| Designing controlled tests that distinguish competing explanations | [Hypothesis Testing](hypothesis-testing.md) |
| Rejected relationships, interpretations, and recurring analytical shortcuts | [Rejected Relationships](rejected-relationships.md) |
| Audited questions that still require evidence | [Open Questions](open-questions.md) |

### Use this section by task

Section ID: `ownkb:section:d000113:s000003`

Uncertainty: `hypothesis`
Provenance cues: `capture`, `database`, `documentation`, `evidence`, `experiment`

| Goal | Start with | Then consult |
| --- | --- | --- |
| Evaluate a proposed database foreign key | [Database Relationship Reconstruction](database-relationship-reconstruction.md) | [Evidence and Confidence](evidence-and-confidence.md), [Rejected Relationships](rejected-relationships.md) |
| Decode a new management capture | [Capture Analysis](capture-analysis.md) | [Diagnostics](../diagnostics/), [Relationship Register](relationship-register.md) |
| Connect a frame field to a database | [Cross-Database Correlation](cross-database-correlation.md) | [Methodology](methodology.md), [Hypothesis Testing](hypothesis-testing.md) |
| Decide whether a claim is ready for reference documentation | [Evidence and Confidence](evidence-and-confidence.md) | [Methodology](methodology.md) |
| Design the next Device experiment | [Hypothesis Testing](hypothesis-testing.md) | [Open Questions](open-questions.md) |
| Check whether an attractive mapping was already disproved | [Rejected Relationships](rejected-relationships.md) | [Relationship Register](relationship-register.md) |
| See the current state of knowledge quickly | [Relationship Register](relationship-register.md) | [Open Questions](open-questions.md) |

### Core rule

Section ID: `ownkb:section:d000113:s000004`

Applicability cues: `not applicable`, `version`
Provenance cues: `catalogue`, `database`, `evidence`

Numeric equality is a lead, not a relationship.

A value can be:

- a database-local primary key;
- an external catalogue number;
- an installed 32-bit Device identifier;
- a Device-local `slot`;
- an OpenWebNet wire field;
- one component of a composite version or address;
- a discriminator-dependent value;
- a sentinel such as `0` meaning “not applicable”;
- a category or matching identifier local to one application model.

A usable relationship must identify the namespace on both sides, required context, cardinality, sentinel rules, evidence, confidence, scope, and falsifier.

### Source-of-truth boundaries

Section ID: `ownkb:section:d000113:s000005`

Applicability cues: `firmware`, `version`
Provenance cues: `database`, `documentation`, `source`

No single source answers every question:

| Source | Strongest authority |
| --- | --- |
| `MHCatalogue.db` | product and firmware capability, Module/Object alternatives, configuration definitions and constraints |
| `OPEN.db` | implementation frame templates, address grammars, management workflows, and timeouts |
| `rules.db3` | linked-property rules for its represented Objects |
| ScenarioDevices databases | scenario-editor capability and literal/symbolic command templates |
| `OpenQuery.txt` | named database reads and selected implementation fields |
| observed traffic | actual installed state and Device behavior |
| MyHOME Suite UI | presentation, visibility, editability, and observed application choices |
| product documentation | physical hardware, configurator layout, and supported installation modes |
| public OpenWebNet material | published wire semantics within its version and scope |

The authoritative conclusion for a question comes from the source capable of answering it, usually corroborated by another independent class.

### Investigation lifecycle

Section ID: `ownkb:section:d000113:s000006`

Provenance cues: `experiment`, `source`

```text
fingerprint source
→ preserve raw observation
→ enumerate namespaces
→ form competing explanations
→ test coverage, cardinality, and sentinels
→ seek independent corroboration
→ run a discriminating experiment
→ assign claim-level confidence
→ promote, retain as open, or reject
```

At each step, preserve enough detail for another investigator to reproduce the decision.

### Claim lifecycle

Section ID: `ownkb:section:d000113:s000007`

Provenance cues: `documentation`, `evidence`

An investigation normally produces one of four outcomes:

| Outcome | Documentation action |
| --- | --- |
| Operationally established/corroborated | promote the result to its reference section and update the Relationship Register |
| Strongly inferred | document the leading mapping, missing proof, and discriminating test |
| Still ambiguous | retain the candidates and evidence needed in Open Questions |
| Rejected | record the tempting interpretation and conflicting evidence in Rejected Relationships |

New evidence can narrow scope, promote confidence, or reopen a rejection when it directly addresses the rejecting evidence.

### Canonical examples

Section ID: `ownkb:section:d000113:s000008`

Applicability cues: `firmware`
Provenance cues: `capture`, `database`

The section uses several recurring examples because they expose different failure modes:

- `DIMENSION 30.KEYO` shows a discriminator-dependent namespace selected by `STATE`.
- `EN_CONF` shows polymorphic ownership selected by zero sentinels.
- `EN_SLOTS` shows why association-row count is not Module count.
- firmware `V.R.b` shows component sentinels, missing rows, defaults, and one-to-many build metadata.
- `EN_ADDRESS_RULE.object_device_family` shows a valid cross-database relationship supported by full coverage and semantics.
- `DIMENSION 32.SYS` shows why a strong structural candidate must remain inferred until a discriminating capture exists.
- ScenarioDevices revisions show why local primary keys cannot be aligned across files.
- `EN_DEVICE.code → EN_LANGUAGE.code` shows how column-name similarity can manufacture a false relationship.

### Minimum investigation record

Section ID: `ownkb:section:d000113:s000009`

Applicability cues: `firmware`, `revision`
Provenance cues: `evidence`, `source`

A useful contribution includes:

- exact source revision and fingerprint;
- raw values, frames, or UI observations;
- Device, firmware, Module, and session scope where applicable;
- candidate namespaces and alternatives;
- exact SQL, request, or controlled action;
- key coverage, cardinality, sentinels, and exceptions;
- supporting and contradicting evidence;
- confidence and falsifier;
- destination reference page.

Private captures should remain private when they contain installation identifiers. Publish a structure-preserving redaction and retain the original hash/location for audit.

### Terminology

Section ID: `ownkb:section:d000113:s000010`

Applicability cues: `firmware`, `only for`
Provenance cues: `catalogue`, `documentation`, `source`

Use the documentation's established terms consistently:

- **Physical Device** for the installed hardware;
- **Module** for a firmware-exposed logical container/function position;
- **`slot`** only for the numeric Device-local position carried by frames or catalogue placement;
- **Object** for `EN_KEY_OBJECT` functionality;
- **Virgin Object** for a configurable functional template, including the identity reported by `DIMENSION 30` while a Module is disabled;
- **Physical configuration**, **Virtual Configuration**, **Advanced Configuration**, and **Product Programming** for the distinct catalogue mode labels where those concepts are meant; preserve `OPEN.db` sequence labels separately rather than treating Virtual configuration as an umbrella for all MyHOME Suite configuration.

Preserve source field names in code formatting even when their historical terminology differs.

### Success criterion

Section ID: `ownkb:section:d000113:s000011`

Uncertainty: `unknown`
Provenance cues: `capture`, `documentation`, `evidence`, `experiment`

The [18 September 2026 documentation review](documentation-review-2026-09-18.md) records the completed cross-section consistency pass, validation, and remaining evidence limits.

Reverse engineering is successful when uncertainty becomes smaller, explicit, and testable. It does not require assigning a convenient meaning to every value.

A precise unknown with a discriminating experiment is better documentation than an unqualified mapping that happens to fit one capture.

# Document: ownkb:document:d000114

Source path: `reverse-engineering/capture-analysis.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Capture Analysis

Section ID: `ownkb:section:d000114:s000001`

Provenance cues: `evidence`

Observed traffic supplies runtime evidence that static databases cannot provide. It must be analyzed as a direction-sensitive session governed by an active workflow, not as an unordered collection of frame strings.

### Privacy and evidence boundary

Section ID: `ownkb:section:d000114:s000002`

Provenance cues: `capture`, `evidence`

Captures can disclose Device IDs, addresses, network endpoints, authentication traffic, installation topology, user behavior, and configured functions. Raw private captures are intentionally excluded from the repository.

Published examples should be redacted or synthetic unless the identifiers were deliberately supplied as evidence. Redaction must preserve field width, separators, ordering, equality relationships, and any property relevant to the conclusion.

Record the hash and private location of the original capture so that a published derivation remains auditable without committing sensitive data.

### Capture the transport context

Section ID: `ownkb:section:d000114:s000003`

Applicability cues: `gateway`
Cautions: `do not`

Where possible, record both the OpenWebNet payload and the transport events around it:

- connection open and close;
- gateway/session establishment;
- payload direction;
- frame boundaries;
- retransmission or duplicate delivery;
- local-button or Device-mode transition;
- timeout and socket failure.

Do not infer frame direction from syntax alone. Several management frames have identical text in programmer-to-Device and Device-to-programmer contexts.

### Canonical event record

Section ID: `ownkb:section:d000114:s000004`

Uncertainty: `unknown`
Provenance cues: `capture`, `evidence`

For every event, retain:

| Field | Purpose |
| --- | --- |
| capture identifier | stable reference to the original evidence |
| timestamp | ordering, delay, and timeout analysis |
| direction | distinguishes requests, responses, and same-shaped aborts |
| connection/session | prevents unrelated traffic from being combined |
| raw frame | preserves delimiters, padding, empty fields, and unknown values |
| parsed grammar | separates `WHO`, `WHAT`, `WHERE`, `DIMENSION`, and value fields |
| active operation | discovery, interview, detailed read, programming, or functional traffic |
| active sequence | expected frames and transition context from `OPEN.db` |
| selected Device | address, local interaction, or Device-ID selector |
| correlation key | `slot`, configuration index, or outstanding request where applicable |
| classification | expected, optional, repeated, terminal, error, timeout, or unexpected |
| notes | uncertainty, redaction, or transport anomaly |

Store raw and parsed forms separately. Never normalize leading zeroes, decimal/hex representation, `#` modifiers, empty fields, or `*` separators in the raw record.

### Parse before interpreting

Section ID: `ownkb:section:d000114:s000005`

Applicability cues: `firmware`, `version`
Provenance cues: `database`

Parsing answers where fields occur; interpretation answers what they mean. Keep the stages separate.

1. Identify the OpenWebNet frame family from delimiters.
2. Split only according to the grammar for that family.
3. Preserve empty and compound fields.
4. Resolve the active management `WHO` and direction.
5. Match an exact `OPEN.db.EN_OPEN` template where available.
6. Attach parameter metadata without treating database labels as universal protocol definitions.
7. Interpret values only after Device, firmware, Module, and workflow context is available.

A placeholder such as `[FW_VERSION]` can expand to `Version*Release*Build`; it is not necessarily one scalar field merely because the template contains one placeholder token.

### Segment the session

Section ID: `ownkb:section:d000114:s000006`

Separate traffic into operations before correlating responses:

- Device enumeration;
- per-Device interview;
- detailed Object/configuration read;
- programming entry and readiness;
- Object, address, or configurator transfer;
- programming verification;
- session close, end marker, or abort;
- ordinary functional traffic.

The same management `WHO` can carry several operations. `WHAT` values and `DIMENSION` numbers are meaningful only inside the active operation and direction.

Use `OPEN.db` scenario/sequence metadata as an implementation model:

```text
scenario
→ ordered sequence
→ ordered frame alternatives
→ repetition and mandatory flags
→ timeout/error/terminal transition
```

This model describes MyHOME Suite 3.5.38. It does not guarantee that every Device emits every optional response.

### Correlate requests and responses

Section ID: `ownkb:section:d000114:s000007`

Cautions: `avoid`

Use the narrowest available context, in this order:

1. transport connection and management family;
2. active operation and sequence;
3. selected Physical Device or address;
4. last outstanding request;
5. `slot`, configuration index, or Object selector;
6. repetition and timeout window;
7. terminal or error transition.

OpenWebNet management traffic has no general transaction identifier. Avoid pipelining requests whose responses would share the same shape and selector.

If pipelining is already present, classify ambiguous associations explicitly instead of selecting the nearest request by timestamp.

### Handle repetitions, retries, and duplicates

Section ID: `ownkb:section:d000114:s000008`

Cautions: `do not`
Provenance cues: `capture`

A repeated response can represent:

- a legitimate multi-row result, such as one row per Module;
- an application retry;
- a Device retransmission;
- the same Device responding to a repeated bus-wide request;
- duplicate transport capture.

Do not deduplicate by frame text alone. Compare direction, timestamps, request cycle, Device selector, sequence position, and expected repetition metadata.

For discovery, preserve each enumeration round. `WHAT 11` quieting, repeated requests, absence of further replies, and `WHAT 12` release are part of the result, not noise around a list of Device IDs.

### Build a structured Device interview

Section ID: `ownkb:section:d000114:s000009`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `evidence`

The normalized evidence model is:

```text
Physical Device instance
├─ diagnostic family and discovery selector
├─ DIMENSION 1 catalogue-facing identity
├─ firmware, hardware, and microcontroller V.R.b values
├─ internal Module slot
│  ├─ enabled regular Object or disabled Virgin Object
│  ├─ enabled/disabled state
│  ├─ system and functional address
│  └─ indexed and Object-specific configuration values
└─ errors, omissions, retries, and terminal evidence
```

Preserve protocol slot numbers even when the UI renumbers visible Modules. Attach `DIMENSION 32` and `35` data only with the same Device and `slot` context. `DIMENSION 35.INDEX` is not globally unique.

### Analyze version responses

Section ID: `ownkb:section:d000114:s000010`

Applicability cues: `firmware`, `revision`, `version`
Provenance cues: `catalogue`, `evidence`

Record firmware (`DIMENSION 2`), hardware (`3`), and microcontroller (`6`) as three raw components: Version, Release/Revision, and Build.

For firmware correlation:

- compare `V` and `R` with `EN_FIRMWARE`;
- compare `b` with associated `EN_BUILDS` rows;
- preserve explicit `-1` sentinels separately from missing build rows;
- retain all candidates until default, localization, capability, or runtime evidence distinguishes them.

Hardware and microcontroller values currently have no direct catalogue columns. Keep them as installed-state evidence rather than manufacturing a join.

### Use differential captures

Section ID: `ownkb:section:d000114:s000011`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `capture`, `evidence`, `experiment`

The strongest behavioral evidence changes one input while holding the rest constant.

For each experiment:

1. capture a complete baseline operation;
2. change one physical configurator, UI property, Module Object, or address;
3. repeat the identical operation;
4. align frames by operation, Device, and slot;
5. report added, removed, and changed fields;
6. restore and recapture the baseline where practical.

Do not compare two Devices with different firmware and configuration as though one changed variable explains every difference.

### Treat errors as structured evidence

Section ID: `ownkb:section:d000114:s000012`

Applicability cues: `firmware`
Provenance cues: `catalogue`

Record `NACK`, structured diagnostic errors, aborts, busy results, timeouts, and positive end markers separately.

An error can establish:

- that the Device parsed a selector;
- that a Module or Object state was reached;
- that a value was outside a supported domain;
- that the operation was unavailable in the current state.

It does not automatically establish which validation layer rejected the request. Transport bounds, catalogue ranges, contextual filters, linked-property rules, firmware behavior, and application prevalidation remain distinct.

### Interpret silence cautiously

Section ID: `ownkb:section:d000114:s000013`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `source`

When documenting an absent response, preserve the request, selector, Device state, timeout source, timeout duration, retry count, connection health, and terminal outcome.

Silence can mean:

- unsupported optional response;
- invalid Device or Module selector;
- disabled Module or unresolved Object state;
- Device busy or not in the required local mode;
- incomplete interview;
- transport loss;
- no matching Device.

An omission becomes a Device/firmware-specific observation before it becomes a family-wide rule.

### Publication record

Section ID: `ownkb:section:d000114:s000014`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `capture`, `catalogue`, `documentation`, `evidence`, `specification`

A capture-derived conclusion should publish:

- a redacted raw exchange with direction;
- the operation and preceding request;
- Device identity and firmware scope;
- exact parsing and unresolved fields;
- catalogue/specification correlation;
- repetitions and exceptions;
- confidence and falsifier;
- the promoted reference-page link.

Capture evidence is ready for reference documentation only when no competing parse changes the operational conclusion.

# Document: ownkb:document:d000115

Source path: `reverse-engineering/cross-database-correlation.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Cross-Database Correlation

Section ID: `ownkb:section:d000115:s000001`

Provenance cues: `database`

Cross-database analysis connects meanings, not local primary keys. Each MyHOME Suite store represents a different projection of the system, and OpenWebNet traffic represents installed runtime state.

### Source boundaries

Section ID: `ownkb:section:d000115:s000002`

Applicability cues: `firmware`
Cautions: `do not`, `must not`
Provenance cues: `catalogue`, `database`, `source`

| Source | Principal model | Must not be assumed to contain |
| --- | --- | --- |
| `MHCatalogue.db` | products, items, Firmware capability, Modules, Objects, configuration and validation | installed Device state or complete functional protocol |
| `OPEN.db` | systems, address grammars, management frames, sequences, timeouts | product catalogue capability or all functional commands |
| `rules.db3` | linked-property rules for selected Objects | global configuration dictionary |
| ScenarioDevices databases | scenario-editor capability hierarchy | installed scenarios or catalogue Object identity |
| `OpenQuery.txt` | named reads over parts of `OPEN.db` | complete application control flow |
| observed traffic | installed state and actual runtime behavior | catalogue labels or unobserved capabilities |

Do not begin with a multi-database join on similarly named integers. Resolve each value in its native namespace first.

### Correlation sequence

Section ID: `ownkb:section:d000115:s000003`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`, `source`

Use staged resolution:

1. identify the management family and installed Device selector from traffic;
2. parse `DIMENSION 1` without translating its values prematurely;
3. resolve the catalogue item through model/system meaning;
4. retain all compatible marketed Device/SKU records;
5. resolve the three-component Firmware candidate set;
6. build Module/Object state from `DIMENSION 30`;
7. attach addresses and configuration by Device and `slot`;
8. resolve Object systems and family;
9. select candidate `OPEN.db` address rules and functional context;
10. apply catalogue filters, conditions, conversions, and `rules.db3` only in that resolved context;
11. correlate ScenarioDevices behavior through literal frames or semantic paths, never local IDs.

At every stage, preserve both the raw value and the resolved record.

![Cross-database correlation path](../assets/diagrams/cross-database-correlation.svg)

This is a semantic resolution flow, not a shared ER schema. Dashed relationships cross independent source-model namespaces and require the conditions documented below.

### Device identity correlation

Section ID: `ownkb:section:d000115:s000004`

Applicability cues: `gateway`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `database`, `evidence`

`DIMENSION 1` provides four catalogue-facing values:

| Wire field | Catalogue correlation | Confidence |
| --- | --- | --- |
| `OBJECT_MODEL` | `AS_ITEM_SYSTEM.modobj` in the resolved system context | corroborated |
| ordinary addressed `N_CONF` | number of physical configurator positions | corroborated for documented addressed Devices |
| gateway `N_CONF` | no catalogue correlation established; preserve raw value | observed `15` on MH202 and F454; exact semantics unresolved |
| `BRAND` | `EN_BRAND.brand_modobj` | corroborated |
| `LINE` | `EN_LINE.line_modobj` | corroborated |

The empty-`WHERE` gateway `DIMENSION 1` form must be kept separate from the ordinary addressed identity form. Its observed `N_CONF = 15` lies outside the ordinary `0..12` range; although `15 = 0xF` is consistent with a reserved sentinel, no cross-database relation or canonical definition establishes that meaning.

The installed Device ID and `EN_DEVICE.id_device` are different namespaces.

Example: observed model value `107` resolves through `AS_ITEM_SYSTEM.modobj` to shared item `1184`. That item is used by several marketed Devices, including `64391`, `64191`, and `64192`. The correct result is therefore a candidate product set until brand, line, UI/project evidence, or another differentiator selects one record.

Use `EN_DEVICE.name` as the MyHOME Suite-facing Physical Device description. Do not replace it with an Object description from `EN_KEY_OBJECT`.

### Firmware correlation

Section ID: `ownkb:section:d000115:s000005`

Applicability cues: `firmware`, `version`
Provenance cues: `catalogue`

Diagnostic Firmware is a `Version*Release*Build` tuple. Catalogue correlation is distributed across:

```text
EN_FIRMWARE.firmware_V
EN_FIRMWARE.firmware_R
EN_BUILDS.firmware_b
```

Selection must preserve:

- all `EN_FIRMWARE` rows belonging to the resolved item;
- zero, one, or several `EN_BUILDS` rows per Firmware definition;
- explicit `-1` components as any/unspecified sentinels;
- absence of a build row as distinct from `firmware_b = -1`;
- `FW_default`, status, localization, `slot` layout, and capability differences.

The databases establish the candidate model but not MyHOME Suite's exact precedence algorithm. Hardware and microcontroller `V.R.b` responses currently have no direct catalogue fields.

### Runtime Module and Object correlation

Section ID: `ownkb:section:d000115:s000006`

Applicability cues: `firmware`
Provenance cues: `evidence`

`DIMENSION 30` is discriminator-dependent:

```text
STATE = 0 → Module enabled → KEYO is EN_KEY_OBJECT.key_object
STATE = 1 → Module disabled → KEYO is EN_VIRGIN_OBJECT.virgin_key_object
```

`SLOT` is the Device-local internal position. It correlates with placement through `EN_SLOTS.first_slot` after Firmware resolution; it is not `EN_SLOTS.id_slot`.

The safe lookup order is:

1. resolve Firmware;
2. select the reported `slot`;
3. choose the enabled regular Object or disabled Virgin Object namespace from `STATE`;
4. verify that the Firmware permits that Object/template at that `slot`;
5. retain mismatches as evidence rather than forcing the nearest candidate.

This order prevents a globally valid Object number from being accepted in a Firmware/`slot` where it is unavailable.

### Configuration correlation

Section ID: `ownkb:section:d000115:s000007`

Applicability cues: `firmware`

`DIMENSION 35.INDEX` cannot be joined globally to `EN_CONF.idx`. The effective lookup context is:

```text
Physical Device
+ firmware
+ `slot`
+ configured Object
+ Object-scoped or firmware-scoped ownership
+ INDEX
```

`EN_CONF` contains two exclusive ownership patterns:

| Scope | Required pattern |
| --- | --- |
| Object-scoped | resolved `id_key_object`; `id_firmware = 0` |
| Firmware-scoped | `id_key_object = 0`; resolved `id_firmware` |

After resolving the property definition, validation proceeds through base ranges, Object/Firmware filters, filtered ranges, conditions, conversion rules, and linked-property rules. A transport-valid number can still be invalid in that context.

### Object-family address-rule relationship

Section ID: `ownkb:section:d000115:s000008`

Provenance cues: `catalogue`

All 11 nonzero `OPEN.db.EN_ADDRESS_RULE.object_device_family` values resolve to `MHCatalogue.db.EN_OBJECT_ITEM_FAMILY.id_family`. Rule descriptions, family names, and Object membership agree.

```text
EN_ADDRESS_RULE.object_device_family
    0     → family-unqualified rule
    nonzero → EN_OBJECT_ITEM_FAMILY.id_family
                  ← EN_KEY_OBJECT.id_family
```

This relationship narrows the address rules applicable to a resolved Object. It does not by itself select the active system, configuration mode, or final encoder.

The cross-model check can be reproduced by attaching the databases in a derived analysis connection:

```sql
SELECT ar.id_address_rule,
       ar.object_device_family,
       f.family_name
FROM open_db.EN_ADDRESS_RULE AS ar
LEFT JOIN catalogue.EN_OBJECT_ITEM_FAMILY AS f
  ON f.id_family = ar.object_device_family
WHERE ar.object_device_family <> 0
  AND f.id_family IS NULL;
```

The expected result for the canonical pair is empty.

### Candidate mapping for `DIMENSION 32.SYS`

Section ID: `ownkb:section:d000115:s000009`

Applicability cues: `revision`
Uncertainty: `hypothesis`, `may`
Provenance cues: `capture`, `catalogue`, `database`

The leading candidate is `MHCatalogue.db.EN_SYSTEM.sys_modobj`.

| Candidate | Assessment |
| --- | --- |
| catalogue `id_system` | local primary key; partial numeric coincidence only |
| `OPEN.db.id_system` | local workflow-registry key |
| functional `WHO` | functional namespace, but predictions differ outside Lighting/Automation |
| diagnostic `WHO` | management family number, incompatible role |
| catalogue `xml_key_system` | useful semantic identifier but textual |
| catalogue `sys_modobj` | numeric external/model field associated with Object systems; strongest candidate |

`sys_modobj` covers `0..21` in this revision. Multiple system variants can share a value, and one reusable Object can belong to several systems. A reported `SYS` may therefore select an active system context rather than identify one database row.

The mapping remains strongly inferred until a non-Lighting capture distinguishes the candidates. See [Hypothesis Testing](hypothesis-testing.md#dimension-32sys).

### `rules.db3` correlation

Section ID: `ownkb:section:d000115:s000010`

Applicability cues: `revision`
Provenance cues: `database`

`rules.db3` uses external Object numbers and textual configuration references:

- `rules.KOBJECTS` corresponds to `EN_KEY_OBJECT.key_object` for Objects `95`, `96`, and `184` represented in this revision;
- `$N` references correspond to `EN_CONF.idx = N` only after the Object context has been selected;
- negative or decorated references must be parsed according to rule syntax rather than cast blindly to integers.

This database refines linked-property validation for selected Objects. It is not a global index-to-property registry.

### ScenarioDevices correlation

Section ID: `ownkb:section:d000115:s000011`

Cautions: `do not`
Provenance cues: `evidence`

ScenarioDevices supplies exact functional frames for selected commands and semantic resource keys for other capabilities. Its `ObjectId`, `ObjectMatchingId`, `CommandId`, and `CommandMatchingId` remain local to that model.

Safe cross-model evidence includes:

- a literal frame parsed into functional `WHO`, `WHAT`, `WHERE`, and values;
- agreement between `ChiOpen` and the literal frame's `WHO`;
- a resource-key meaning corroborated by frame and editor category;
- full semantic-path comparison between the two ScenarioDevices revisions.

Do not equate ScenarioDevices `ObjectId` with `EN_KEY_OBJECT.key_object` or `FamilyId` with functional `WHO`.

### Avoid circular resolution

Section ID: `ownkb:section:d000115:s000012`

Applicability cues: `firmware`

An unsafe correlation looks like this:

1. guess an Object from `KEYO` without applying `STATE`;
2. select a Firmware row that supports that Object;
3. cite the selected Firmware as proof of the Object mapping.

The correct process uses an independently resolved item/Firmware, the frame discriminator, and `slot` placement. If those sources disagree, preserve the disagreement.

### Result representation

Section ID: `ownkb:section:d000115:s000013`

Applicability cues: `revision`
Provenance cues: `catalogue`, `database`, `source`

A durable cross-database result should retain:

```text
raw wire value and frame
→ parsed wire namespace
→ source database and revision
→ internal row key
→ external catalogue identifier
→ semantic label
→ parent context and discriminator
→ cardinality and candidate set
→ confidence and falsifier
```

Collapsing these layers into one integer makes later validation, debugging, and revision comparison unreliable.

# Document: ownkb:document:d000116

Source path: `reverse-engineering/database-relationship-reconstruction.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Database Relationship Reconstruction

Section ID: `ownkb:section:d000116:s000001`

Provenance cues: `evidence`

MyHOME Suite databases vary in how completely they declare relationships. ScenarioDevices declares its principal hierarchy with foreign keys, while many central `MHCatalogue.db` relationships are encoded only by column roles, association tables, and complete key coverage.

Reconstruction documents those relationships without rewriting the canonical evidence.

### Declared, structural, and semantic relationships

Section ID: `ownkb:section:d000116:s000002`

Cautions: `must not`
Provenance cues: `database`, `evidence`

Keep three kinds of relationship distinct:

| Kind | Evidence | Example |
| --- | --- | --- |
| Declared | SQLite foreign key or primary-key structure | ScenarioDevices `Commands.DeviceObject_Id → DeviceObjects.Id` |
| Structurally reconstructed | complete key coverage, compatible cardinality, and table role | `EN_DEVICE.id_item → EN_ITEM.id_item` |
| Semantic/cross-model | independent models connected by meaning rather than a database key | `DIMENSION 1.OBJECT_MODEL → AS_ITEM_SYSTEM.modobj` |

A structurally reconstructed relationship can be safe for analysis without being declared by SQLite. A cross-model relationship needs stronger semantic corroboration and must not be presented as a foreign key.

### Reconstruction workflow

Section ID: `ownkb:section:d000116:s000003`

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

### Schema and source inspection

Section ID: `ownkb:section:d000116:s000004`

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

### Sentinel-aware orphan testing

Section ID: `ownkb:section:d000116:s000005`

Applicability cues: `firmware`, `not applicable`
Cautions: `do not`
Uncertainty: `unknown`

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

### Polymorphic ownership: `EN_CONF`

Section ID: `ownkb:section:d000116:s000006`

Applicability cues: `firmware`
Provenance cues: `database`

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
| --- | --- |
| Object-scoped | 1,420 |
| Firmware-scoped | 1,463 |
| both parents populated | 0 |
| both parents zero | 0 |

The zero is part of an exclusive discriminator. Treating both parent columns as mandatory would manufacture false orphans and erase the data model.

### Verified catalogue relationships

Section ID: `ownkb:section:d000116:s000007`

Applicability cues: `firmware`, `revision`

The following full-coverage checks hold for MyHOME Suite 3.5.38:

| Child relationship | Rows checked | Non-sentinel orphans |
| --- | --- | --- |
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

### Association paths and row identities

Section ID: `ownkb:section:d000116:s000008`

Applicability cues: `firmware`

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

### Cardinality testing

Section ID: `ownkb:section:d000116:s000009`

Applicability cues: `firmware`

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

### Conditions and indirect relationships

Section ID: `ownkb:section:d000116:s000010`

Applicability cues: `firmware`
Cautions: `do not`
Uncertainty: `appears`

Not every relationship is a direct equality join. Conditions, symbols, and conversion rules can reference configuration concepts textually or through a chain of associations.

For these cases, require:

- an unambiguous owning firmware/Object/slot context;
- a parsed expression or symbol namespace;
- resolution of every referenced property;
- documented evaluation order;
- runtime/UI corroboration where behavior is claimed.

Do not convert textual references into foreign keys merely because a number appears inside the expression.

### Cross-database reconstruction

Section ID: `ownkb:section:d000116:s000011`

Applicability cues: `revision`
Cautions: `do not`
Provenance cues: `catalogue`, `database`

Independent SQLite files do not share primary-key namespaces. A cross-database relationship must state whether it connects:

- an external number intentionally reused across models;
- a parsed wire value to catalogue metadata;
- a resource-key semantic path;
- a functional `WHO` extracted from a literal frame;
- a revision-specific data pattern.

For example, all 11 nonzero `OPEN.db.EN_ADDRESS_RULE.object_device_family` values resolve to `MHCatalogue.db.EN_OBJECT_ITEM_FAMILY.id_family`, and the rule descriptions agree with family membership. This is a structurally and semantically corroborated cross-model relationship, not a declared foreign key.

See [Cross-Database Correlation](cross-database-correlation.md) for the staged resolution rules.

### Revision comparison

Section ID: `ownkb:section:d000116:s000012`

Applicability cues: `revision`
Cautions: `do not`
Provenance cues: `database`

Never align two database revisions by local row ID alone. Compare the complete semantic path:

```text
Object System resource key and category
→ Device Object resource key and external identifiers
→ Command resource key and frame semantics
→ Parameter resource key, domain, and placeholder
```

Using this method, the common ScenarioDevices ProgramData content is an exact semantic subset of the Program Files copy despite divergent local IDs.

Report revision comparison as additions, removals, changed semantic rows, and unchanged semantic rows. Do not describe ID renumbering as a capability change.

### Preserve the canonical evidence

Section ID: `ownkb:section:d000116:s000013`

Cautions: `do not`, `warning`
Provenance cues: `database`, `source`

Do not add inferred foreign keys to the distributed databases. Apart from changing the source hash, doing so can impose false deletion/update behavior and mishandle sentinels.

If a derived constraint-enabled database is useful, label it as generated and publish:

- source hash;
- transformation script;
- sentinel/exclusion rules;
- orphan report;
- generated schema hash;
- explicit warning that it is not the canonical MyHOME Suite file.

### False-positive example

Section ID: `ownkb:section:d000116:s000014`

`EN_DEVICE.code → EN_LANGUAGE.code` is the canonical failure. The columns share the name `code`, and selected values can appear compatible, but `EN_DEVICE.code` stores product codes/SKUs. Table role and semantics reject the relationship.

Column-name similarity must never outrank namespace, coverage, cardinality, and application meaning.

# Document: ownkb:document:d000117

Source path: `reverse-engineering/documentation-review-2026-09-18.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Documentation Review - 18 September 2026

Section ID: `ownkb:section:d000117:s000001`

Provenance cues: `documentation`

This review continues the documentation-wide pass on `general-once-over`, starting from commit `d1d8ecdef0d1a63edf631b2de8d7b797403170e3`. The already merged protocol review and established Device Model, diagnostic, programming, and reverse-engineering decisions remain the baseline.

### Scope and completed corrections

Section ID: `ownkb:section:d000117:s000002`

Applicability cues: `firmware`, `version`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `database`, `source`

| Area | Review result |
| --- | --- |
| Protocol | Corrected session-selection/authentication branching, final client authentication acknowledgement, proof serialization, and failure throttling; recorded the published identity-constant discrepancy. |
| Functional references | Expanded Temperature Control dimensions and holiday commands; corrected Lighting Management address composition and payloads; added Sound Diffusion payload examples and source discrepancies; removed an unsupported atomic-clock guarantee. |
| Diagnostics | Added the public Temperature Control fault model, keeping it distinct from Suite Device interviews; aligned discovery termination and version-payload explanations. |
| Device Model | Preserved configured Object versus Virgin Object resolution; corrected firmware 157's placement count to 11 alternatives across four `slot` positions. |
| Programming and guides | Scoped product queries by catalogue system, preserved firmware candidates, corrected slot and rule queries, distinguished decimal wire IDs from hexadecimal display, added cleanup, and processed active sequence outcomes before subsequent writes. |
| Scenario Engine | Corrected shared-placeholder rendering and the parameter table; narrowed open questions to genuinely unresolved mappings. |
| Internals and reverse engineering | Preserved established namespace and ownership boundaries; corrected a nonexistent SQL column and clarified the position of `N_CONF`. |
| Navigation and style | Replaced path-only navigation labels with page titles, removed em dashes, repaired an obsolete address anchor, and checked Markdown tables. |

The accepted interpretation of `DIMENSION 1.N_CONF` as a physical configurator-position count remains intact. `EN_DEVICE.name` remains the preferred Device description; Module, `slot`, Object, and database row identity remain separate concepts. Existing one-page functional references remain consolidated.

### Validation

Section ID: `ownkb:section:d000117:s000003`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`, `source`

- Checked every Markdown page for local link targets and heading fragments, table-column consistency, and whitespace errors.
- Prepared 51 concrete SQL statements against the five canonical SQLite databases, with the documented cross-database aliases. Three generic parent/child schema examples were excluded from preparation because they intentionally use illustrative tables. Preparation checks schema and syntax, not runtime Device behavior.
- Cross-checked catalogue counts and firmware-placement examples against the canonical database; retained wildcard, missing-build, ownership, and multi-system distinctions.
- Compared all 24 locally available canonical non-Markdown source files with the baseline Git blob hashes: all matched exactly. No source database, support file, PDF, or diagram was edited.
- Used the baseline remote tree when publishing so unavailable source binaries remain preserved.

### Evidence limits and remaining research

Section ID: `ownkb:section:d000117:s000004`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `capture`, `documentation`, `evidence`, `source`

This is a documentation and source-data review, not a hardware interoperability test. Existing capture-derived findings retain their stated scope; no new Device capture or programming operation was performed.

Two canonical PDFs could not be retrieved in this review environment: `OpenWebNet_Zigbee.pdf` and `WHO_6_L4686SDK.pdf`. Their existing repository bytes and previously documented findings are preserved, but this pass does not claim a fresh page-by-page verification of those files.

The [authentication reference](../protocol/authentication.md) and [Sound Diffusion reference](../functional/who-22-sound-diffusion/) identify source contradictions that require independent implementation or traffic evidence. Other unresolved research, including firmware-selection precedence, configurator-value encoding, and non-Lighting confirmation of `DIMENSION 32.SYS`, remains in [Open Questions](open-questions.md). These are evidence boundaries, not reasons to substitute speculative protocol behavior.

# Document: ownkb:document:d000118

Source path: `reverse-engineering/evidence-and-confidence.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Evidence and Confidence

Section ID: `ownkb:section:d000118:s000001`

Confidence describes support for one precisely scoped claim. It is not a score for an entire page, table, or theory, and it does not measure how plausible an explanation sounds.

### Evidence classes

Section ID: `ownkb:section:d000118:s000002`

Applicability cues: `firmware`
Cautions: `limitation`
Uncertainty: `may`
Provenance cues: `capture`, `catalogue`, `database`, `documentation`, `evidence`, `source`, `specification`

| Evidence | Strongest contribution | Principal limitation |
| --- | --- | --- |
| Source fingerprint | identifies the exact artifact examined | says nothing about semantics |
| Declared schema | explicit local keys, types, and constraints | many catalogue relationships are undeclared |
| Complete data pattern | coverage, cardinality, sentinels, defaults, and exceptions | cannot prove runtime behavior alone |
| Application query | intended joins, selected columns, and ordering | may be incomplete, malformed, dormant, or interpreted elsewhere |
| Literal frame template | exact stored wire grammar and implementation context | does not prove that every Device implements it |
| Workflow metadata | ordering, repetition, direction, timeout, and terminal behavior | iteration counts and Device-specific optionality may remain external |
| Public specification | published protocol terminology and semantics | may predate the implementation or omit private management behavior |
| Observed traffic | actual runtime ordering and Device behavior | scoped to the observed Device, firmware, state, and transport |
| Controlled Device change | causal evidence linking one input to one output | may still be product-specific |
| MyHOME Suite UI | labels, visibility, editability, and application behavior | does not establish wire or storage encoding alone |
| Product documentation | hardware layout and supported physical configuration | may not describe advanced/Virtual configuration or later revisions |

No source class is universally superior. A declared local foreign key is decisive for a database relationship; it cannot establish the meaning of a diagnostic field. A capture proves that one Device emitted a frame; it cannot establish universal support.

### Confidence levels

Section ID: `ownkb:section:d000118:s000003`

Applicability cues: `firmware`, `revision`
Uncertainty: `hypothesis`, `may`, `unknown`
Provenance cues: `capture`, `evidence`

| Level | Meaning | Appropriate wording |
| --- | --- | --- |
| Established | directly declared, stored, fingerprinted, or unambiguously observed within the stated scope | “defines”, “contains”, “returns in this capture” |
| Corroborated | independent evidence classes support the same interpretation and tested cases agree | “corresponds”, with scope stated |
| Strongly inferred | complete structural evidence strongly favors one candidate, but a decisive observation is missing | “leading mapping”, “strongly supports” |
| Hypothesis | plausible, testable explanation with incomplete coverage or viable alternatives | “may”, “working hypothesis” |
| Unknown | available evidence cannot distinguish meanings | “unknown”; list candidates only if useful |
| Rejected | evidence conflicts with the proposed relationship or interpretation | “does not”, with the conflicting evidence |

“Established” is never automatically universal. A row count established for MyHOME Suite 3.5.38 remains revision-specific. A runtime sequence established for one firmware remains Device- and firmware-scoped unless broader evidence exists.

### Confidence belongs to claims

Section ID: `ownkb:section:d000118:s000004`

Applicability cues: `version`
Provenance cues: `capture`, `catalogue`, `evidence`

Separate compound statements before assigning confidence. For example:

1. `DIMENSION 3` has a `Version*Release*Build` logical form - established by `OPEN.db`.
2. It is returned by a particular Device - established only by a capture of that Device.
3. It maps to a catalogue column - currently unsupported because no hardware-version column exists.
4. MyHOME Suite uses it for compatibility selection - open runtime question.

Combining these into “hardware version is established” would hide three different evidence states.

### Claim record

Section ID: `ownkb:section:d000118:s000005`

Applicability cues: `firmware`, `revision`
Provenance cues: `database`, `evidence`, `source`

Every important inference should be recoverable from a compact claim record:

| Field | Purpose |
| --- | --- |
| Claim | one precise, falsifiable statement |
| Source | files, tables, rows, frames, captures, UI, or documents |
| Revision | product/database/document/firmware revision |
| Namespace | meaning and scope of every identifier involved |
| Conditions | discriminators, sentinels, and prior resolution required |
| Cardinality | one-to-one, one-to-many, many-to-many, conditional, or polymorphic |
| Coverage | tested rows, Devices, families, and exceptions |
| Supporting evidence | observations favoring the claim |
| Counterevidence | anomalies, conflicts, or untested cases |
| Alternatives | other viable explanations |
| Confidence | one level from the table above |
| Falsifier | observation that would reject or narrow the claim |
| Destination | reference page containing the operational result |

### Worked confidence example: `N_CONF`

Section ID: `ownkb:section:d000118:s000006`

Applicability cues: `firmware`, `gateway`
Uncertainty: `unresolved`
Provenance cues: `catalogue`

The scoped claim “in the ordinary addressed Device form, `DIMENSION 1.N_CONF` is the number of physical configurator positions” is corroborated because:

- `OPEN.db` labels that field as the number of physical configurators and constrains the ordinary addressed form to `0..12`;
- observed addressed-form `N_CONF` values agree with product diagrams for Devices with two, three, and seven positions;
- resolved catalogue firmware fields independently produce the same counts in those examples;
- the field is part of Device identity rather than a Module record.

The empty-`WHERE` gateway form prevents promotion of that interpretation to an unconditional `DIMENSION 1` rule. Observed MH202 and F454 gateway identity responses both carry `N_CONF = 15`, outside the ordinary `0..12` range. Numerically, `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern consistent with a reserved or sentinel convention but not proof of one. Gateway `N_CONF` semantics therefore remain unresolved.

The stronger addressed-form claim “for every firmware, `N_CONF` equals the count of firmware-scoped physical fields excluding `AID`” is not yet equally supported. Conditional fields and products without diagrams prevent catalogue-wide promotion. This example demonstrates why confidence belongs to a scoped claim: the addressed-form interpretation can remain corroborated while the gateway variant remains unresolved.

### Worked confidence example: `DIMENSION 32.SYS`

Section ID: `ownkb:section:d000118:s000007`

Provenance cues: `capture`

`MHCatalogue.db.EN_SYSTEM.sys_modobj` is the leading candidate because its role, range, external-model character, and Object/system graph fit the wire field. However, common Lighting/Automation observations equal `1`, which also matches other candidate namespaces.

The correct confidence is strongly inferred, not corroborated. A non-Lighting capture whose candidates predict different values is the falsifier/discriminator.

### Independence and circularity

Section ID: `ownkb:section:d000118:s000008`

Uncertainty: `may`
Provenance cues: `capture`, `database`, `evidence`

Evidence is independent when it could realistically disagree. A product diagram and a diagnostic capture are independent. Two tables generated from the same internal model may not be.

Watch for circular reasoning:

1. infer an Object from a frame;
2. use that inferred Object to select a database row;
3. cite the selected row as proof that the frame meant that Object.

Break the circle with an independent identifier, controlled change, UI observation, documented product function, or a discriminating capture.

### Negative evidence

Section ID: `ownkb:section:d000118:s000009`

Provenance cues: `evidence`, `source`

Absence is evidence only when the observation window was capable of showing the expected event.

Record:

- exact request and selector;
- Device configuration and readiness;
- expected response and why it was expected;
- timeout source and duration;
- retry count;
- terminal, error, or abort state;
- whether other traffic proved the connection remained healthy.

Examples of unsafe conclusions include:

- no response after an invalid address, therefore no Device exists;
- no observed `DIMENSION 35`, therefore the Object has no configuration;
- no ScenarioDevices row, therefore the functional command is unsupported;
- no declared foreign key, therefore the columns are unrelated.

### Contradictions and exceptions

Section ID: `ownkb:section:d000118:s000010`

Applicability cues: `firmware`, `revision`, `version`
Cautions: `do not`
Provenance cues: `database`, `evidence`

Do not average conflicting evidence into a vague confidence label. Determine whether the conflict indicates:

- a parsing error;
- a different namespace;
- a missing discriminator;
- firmware or product variation;
- database revision drift;
- conditional application behavior;
- an actual counterexample.

Record exceptions beside the claim. A relationship with explicit conditions can remain established even when an unconditional version is rejected.

### Revision drift

Section ID: `ownkb:section:d000118:s000011`

Applicability cues: `revision`
Cautions: `do not`
Provenance cues: `source`

When comparing source revisions:

- never align local primary keys without proof of stability;
- compare semantic paths and external identifiers;
- report additions, removals, and changed values separately;
- retain both source fingerprints;
- do not silently carry a confidence level from one revision to another.

The ScenarioDevices databases demonstrate this requirement: their common semantic hierarchy overlaps even though local row IDs diverge.

### Promotion, demotion, and reopening

Section ID: `ownkb:section:d000118:s000012`

Provenance cues: `evidence`

Promote a claim when its operational use is clear and the remaining uncertainty no longer changes that use. Demote or narrow it when new evidence reveals an exception. Reopen a rejected relationship only when new evidence addresses the reason it was rejected.

Every promotion should update:

1. the appropriate reference page;
2. the [Relationship Register](relationship-register.md);
3. the relevant entry in [Open Questions](open-questions.md) or [Rejected Relationships](rejected-relationships.md).

# Document: ownkb:document:d000119

Source path: `reverse-engineering/hypothesis-testing.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Hypothesis Testing

Section ID: `ownkb:section:d000119:s000001`

A useful reverse-engineering test makes competing explanations predict different observations. Repeating a familiar case in which every candidate gives the same value increases sample size but does not identify the correct model.

### Test design template

Section ID: `ownkb:section:d000119:s000002`

Applicability cues: `firmware`
Provenance cues: `database`, `experiment`

For every experiment, record:

| Element | Requirement |
| --- | --- |
| Claim | one relationship or semantic statement |
| Alternatives | at least one credible competing explanation |
| Predictions | expected result for each alternative |
| Controlled variables | Device, firmware, Module, configuration, connection, and request |
| Changed variable | exactly one input where possible |
| Observation | raw frames, database rows, UI state, and timing |
| Decision rule | result that favors, rejects, or narrows each candidate |
| Restoration | how the baseline is recovered after a state-changing test |
| Scope | products and revisions to which the result applies |

A test is inconclusive when the candidates predict the same result or an uncontrolled variable could explain the difference.

### `DIMENSION 32.SYS`

Section ID: `ownkb:section:d000119:s000003`

Provenance cues: `catalogue`

Common Lighting/Automation values collapse to `1`. Use a managed family whose identifiers diverge:

| Diagnostic family | `sys_modobj` prediction | catalogue `id_system` prediction | functional `WHO` prediction |
| --- | --- | --- | --- |
| Thermoregulation `1004` | `3` | `2` | `4` |
| Energy Management `1018` | `2` | `20` | `18` |
| Access Control `1023` | `7` | `8` | `23` |
| Integration Functions `1013` | `15` | `26` | `13` |

Procedure:

1. identify one configured Device and Module in the selected family;
2. resolve its Object and all catalogue `AS_OBJECT_SYSTEM` rows;
3. prefer an Object with one nonzero system assignment;
4. send the interview request that produces `DIMENSION 32`;
5. preserve raw `SYS`, `ADDR`, Device, and `slot`;
6. compare the result with every prediction;
7. repeat with an Object assigned to several systems to test context selection.

A value equal to one candidate and different from the other two rejects the alternatives for that observation. Multiple-system Objects remain a separate cardinality question.

### Firmware-selection precedence

Section ID: `ownkb:section:d000119:s000004`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `catalogue`

The catalogue contains concrete `V.R.b` rows, explicit `-1` components, multiple build rows, missing build rows, and `FW_default` metadata. Static data establishes these states but not loader precedence.

Select an item that exposes competing rows and record:

1. all `EN_FIRMWARE` candidates for the item;
2. all associated `EN_BUILDS` rows;
3. `FW_default`, status, localization level, slots, and capability differences;
4. the Device's reported firmware `V.R.b`;
5. the firmware/capability MyHOME Suite actually presents;
6. behavior when only the build differs;
7. behavior for a concrete build versus `V.R.-1`;
8. behavior when no build row exists.

Use read-only observation first. Do not replace catalogue rows to force a selection. A useful result must distinguish exact match, component wildcard, default fallback, localization choice, and absence of build metadata.

### Hardware and microcontroller versions

Section ID: `ownkb:section:d000119:s000005`

Applicability cues: `firmware`, `revision`, `version`
Provenance cues: `capture`, `catalogue`, `database`, `source`

`DIMENSION 3` and `6` use `Version*Release*Build`, but the canonical databases contain no direct target fields.

To determine whether they classify product revisions:

1. collect several physical examples of the same SKU and firmware;
2. record manufacturing date/revision markings where available;
3. capture firmware, hardware, and microcontroller tuples;
4. compare Module layout and supported configuration;
5. repeat across a known hardware revision or replacement product;
6. observe whether MyHOME Suite changes the selected catalogue Device or capability.

A stable correlation with a printed revision is useful empirical metadata; it does not create a database relationship unless a source field is found.

### `N_CONF` catalogue-wide equivalence

Section ID: `ownkb:section:d000119:s000006`

Applicability cues: `firmware`, `gateway`, `not applicable`
Cautions: `do not`
Uncertainty: `hypothesis`, `not established`
Provenance cues: `capture`, `evidence`

For the ordinary addressed Device form, `N_CONF` is corroborated as the number of physical configurator positions. The remaining hypothesis is that, within that addressed-form scope, it always equals the count of applicable firmware-scoped physical configuration fields after excluding `AID`.

For each test Device:

1. obtain a product diagram showing all physical configurator positions;
2. capture `DIMENSION 1.N_CONF`;
3. resolve item and exact firmware;
4. identify firmware-scoped physical definitions, configuration modes, and conditions;
5. exclude `AID` only when it is the common identifier rather than a physical position;
6. compare diagram, frame, and applicable-field count;
7. record conditional or duplicated fields instead of counting blindly.

Prioritize Devices with counts other than six and firmware shared by several SKUs. Known corroborating examples include `F420`, `F429`, and `H4652/3`.

Treat the empty-`WHERE` gateway form as a separate hypothesis. Observed MH202 and F454 gateway identity responses both carry `N_CONF = 15`, outside the ordinary `0..12` range. Because `15 = 0xF`, a reserved or sentinel interpretation is plausible, but it is not established. To test it, collect the same field across gateway models and firmware revisions and seek an applicable implementation decoder or authoritative definition. Record any value other than `15`, and do not infer “zero configurators” or “not applicable” without evidence that distinguishes those meanings.

### `DIMENSION 4` and `5`

Section ID: `ownkb:section:d000119:s000007`

Uncertainty: `hypothesis`
Provenance cues: `capture`

The working hypothesis is that the two groups of six values encode physical-configurator state, possibly mapping positions `1..6` and `7..12`.

Use a Device with documented positions and removable configurators:

1. record a complete baseline with all positions empty if the Device permits it;
2. capture both dimensions at least twice to establish stability;
3. insert one known configurator into position `1` and repeat;
4. move the same configurator to several positions, including one above `6` when available;
5. keep the position fixed and change only the configurator value;
6. compare physical and Virtual configuration producing the same effective property;
7. record whether unchanged positions remain constant.

This matrix distinguishes position, presence, raw configurator code, effective value, and configuration-mode effects. Zero/nonzero data from one configuration cannot establish a presence bitmap.

### Diagnostic outer `WHERE`

Section ID: `ownkb:section:d000119:s000008`

Repeated `WHO 1001` observations suggest that the outer diagnostic `WHERE` often follows the configured address of `slot` `1`. Test the boundary cases:

- slot `1` enabled and addressed;
- slot `1` disabled and represented by its Virgin Object in `DIMENSION 30`;
- slot `1` assigned a command-only Object;
- another slot carrying the main physical address;
- several Modules sharing an address;
- non-Lighting diagnostic families.

For each case, compare discovery address, interview selector, outer response `WHERE`, and every `DIMENSION 32` Module address. The goal is to recover a selection rule, not merely another matching example.

### Physical-to-advanced property mapping

Section ID: `ownkb:section:d000119:s000009`

Applicability cues: `firmware`

For a candidate physical field and `DIMENSION 32` or `35` property:

1. resolve the exact firmware, `slot`, and Object;
2. compare `CONF_SYMBOL_REF`, semantic type, and value domain;
3. inspect filters, conditions, conversion rules, and `EN_PHY_TO_ADV_TRANS`;
4. change only the physical field and read back the effective configuration;
5. restore the baseline;
6. program the proposed Virtual counterpart and read back again;
7. classify the result as direct, converted, range-limited, condition-dependent, or unrelated.

An identical effective value does not prove identical storage or configuration method. A physical counterpart indicates capability, not which method is active.

### Address-rule selection

Section ID: `ownkb:section:d000119:s000010`

Provenance cues: `catalogue`

Choose a system with both family-unqualified and family-qualified `EN_ADDRESS_RULE` rows.

1. resolve the Object's `id_family` and catalogue systems;
2. record every candidate rule and its Virtual/advanced template;
3. vary only the Object family or mode where possible;
4. observe the address form MyHOME Suite accepts and emits;
5. trace whether `validity_rule`, level flags, or `offset_adv` are read;
6. test a rejected address that differs at only one rule boundary.

This can distinguish rule selection from rule rendering and application-side prevalidation from Device rejection.

### Scenario persistence and matching

Section ID: `ownkb:section:d000119:s000011`

To find the missing scenario-instance layer:

1. fingerprint candidate project and data files;
2. trace file opens before creating a scenario;
3. create one minimal trigger-action scenario;
4. save, close, and reopen the application;
5. diff files, SQLite schemas, and records;
6. change one trigger, condition, action, or ordering edge independently;
7. correlate changes with ScenarioDevices resource keys and matching IDs;
8. trace execution separately from persistence.

The ScenarioDevices capability databases should remain unchanged. A changed capability file would indicate synchronization or migration behavior and must be investigated separately.

### Stop conditions

Section ID: `ownkb:section:d000119:s000012`

Applicability cues: `firmware`
Uncertainty: `unknown`

Stop and classify the result as inconclusive when:

- the Device or firmware cannot be resolved uniquely enough for the claim;
- multiple settings changed;
- request/response direction is unknown;
- candidates predict the same outcome;
- the operation timed out without proof that the Device could respond;
- a state-changing test cannot be restored safely.

An inconclusive test should still record what was tried and how the next test can become discriminating.

# Document: ownkb:document:d000120

Source path: `reverse-engineering/methodology.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Methodology

Section ID: `ownkb:section:d000120:s000001`

Provenance cues: `evidence`

Reverse engineering should recover the narrowest explanation supported by the evidence and make that explanation reproducible by another investigator. A plausible label is not a result until its namespace, scope, conditions, and counterexamples have been tested.

### Define the question precisely

Section ID: `ownkb:section:d000120:s000002`

Applicability cues: `firmware`
Cautions: `avoid`
Provenance cues: `source`

Begin with one falsifiable question. Examples include:

- Does `DIMENSION 30.KEYO` change namespace with `STATE`?
- Does `EN_ADDRESS_RULE.object_device_family` refer to `EN_OBJECT_ITEM_FAMILY.id_family`?
- Does an explicit firmware component of `-1` behave as an any/unspecified sentinel?
- Which stored field is the best candidate for `DIMENSION 32.SYS`?

Avoid questions such as “What does this table mean?” Break them into claims that can be checked independently.

For each claim, write down:

1. the proposed source and target namespaces;
2. the expected cardinality and conditions;
3. at least one viable alternative;
4. the observation that would distinguish the alternatives;
5. the scope in which the claim is expected to hold.

### Fix the evidence revision

Section ID: `ownkb:section:d000120:s000003`

Applicability cues: `revision`, `version`
Cautions: `do not`
Uncertainty: `may`
Provenance cues: `database`, `source`

Record the product version, original path, byte size, and SHA-256 before analysis. The canonical MyHOME Suite 3.5.38 source set is registered in [`sources/manifest.yaml`](../sources/manifest.yaml).

Treat every quantitative statement as revision-scoped. “All 827 rows resolve” means all rows in the fingerprinted 3.5.38 database, not every MyHOME release.

Do not modify canonical databases to add inferred foreign keys, normalize text, repair rows, or encode conclusions. Derived databases, query output, diagrams, and reports belong outside [`sources/`](../sources/).

When an external manual or product sheet is used, preserve its title, product code, revision/date, language, and page or diagram identifier. A later manual may describe different hardware.

### Preserve the raw observation

Section ID: `ownkb:section:d000120:s000004`

Applicability cues: `firmware`
Provenance cues: `database`, `evidence`

Interpretation must remain traceable to unchanged evidence.

For database work, retain:

- database and table name;
- schema and declared constraints;
- row key where meaningful;
- raw values, including `NULL`, empty text, `0`, and negative values;
- the exact query used to produce a count or exception list.

For protocol work, retain:

- exact frame bytes or text;
- timestamp, direction, transport connection, and session;
- active diagnostic, programming, or functional operation;
- Device selector and preceding request;
- following response, terminal marker, error, or timeout.

For UI evidence, record the exact label, value, visibility, editability, selected Device, firmware, Module, and configuration mode. For product evidence, distinguish an actual configurator position from a printed label, terminal, button, or indicator.

Never replace the raw value with its interpretation. Store both.

### Enumerate namespaces before joining

Section ID: `ownkb:section:d000120:s000005`

Applicability cues: `firmware`, `revision`
Uncertainty: `might`
Provenance cues: `database`, `evidence`

The same integer can legitimately occur in unrelated namespaces. A value described informally as an Object might mean:

- `EN_KEY_OBJECT.id_key_object`, an internal row key;
- `EN_KEY_OBJECT.key_object`, an external Object number;
- `EN_VIRGIN_OBJECT.id_virgin_key_object`, an internal row key;
- `EN_VIRGIN_OBJECT.virgin_key_object`, an external Virgin Object number;
- ScenarioDevices `ObjectId`, local to the scenario engine;
- a `slot` carried by a diagnostic frame;
- an OpenWebNet `WHAT`, `WHERE`, or `DIMENSION` value.

Build a namespace ledger before testing equality:

| Property | Record |
| --- | --- |
| Origin | frame field, table column, UI field, or document label |
| Representation | integer, text, composite address, bit field, sentinel |
| Range | declared and observed |
| Scope | global, database-local, Device-local, firmware-local, session-local |
| Stability | persistent identity, revision-local row key, runtime value |
| Candidate meanings | every plausible namespace, not only the preferred one |

Numeric equality is useful for generating candidates. It is not relational evidence by itself.

### Test structural compatibility

Section ID: `ownkb:section:d000120:s000006`

Applicability cues: `firmware`
Provenance cues: `database`, `evidence`

For a proposed database relationship, test all populated non-sentinel values, not a sample.

```sql
SELECT child.parent_id, COUNT(*) AS occurrences
FROM child
LEFT JOIN parent ON parent.id = child.parent_id
WHERE child.parent_id IS NOT NULL
  AND child.parent_id <> 0
  AND parent.id IS NULL
GROUP BY child.parent_id;
```

Then test cardinality and ambiguity:

```sql
SELECT child.parent_id, COUNT(*) AS child_rows
FROM child
WHERE child.parent_id IS NOT NULL
GROUP BY child.parent_id
ORDER BY child_rows DESC;
```

The audit must answer:

1. Are types and observed domains compatible?
2. Does every non-sentinel child resolve?
3. Are duplicates compatible with the proposed cardinality?
4. Do `0`, `NULL`, empty strings, or negative values act as data or sentinels?
5. Does the relationship survive selection of the correct firmware, Module, Object, system, or configuration scope?
6. Is there a competing table with equal or better coverage?

Complete coverage establishes structural compatibility, not semantic identity. Table role and independent evidence are still required.

### Model discriminator-dependent relationships

Section ID: `ownkb:section:d000120:s000007`

Applicability cues: `firmware`
Cautions: `do not`

Some relationships are correct only when a discriminator is part of the key. For example:

```text
DIMENSION 30.KEYO
    STATE = 0 → enabled Module → EN_KEY_OBJECT.key_object
    STATE = 1 → disabled Module → EN_VIRGIN_OBJECT.virgin_key_object
```

Similarly, `EN_CONF` ownership is polymorphic:

```text
Object-scoped   → id_key_object resolves, id_firmware = 0
Firmware-scoped → id_key_object = 0, id_firmware resolves
```

Do not force these into unconditional foreign keys. Record the discriminator as part of the relationship.

### Form competing explanations

Section ID: `ownkb:section:d000120:s000008`

Uncertainty: `hypothesis`
Provenance cues: `catalogue`, `database`

A hypothesis is useful only when alternatives are explicit. For `DIMENSION 32.SYS`, credible candidates include catalogue `sys_modobj`, database-local system IDs, and functional `WHO`. A Lighting/Automation observation of `1` does not distinguish them.

For each candidate, predict:

- values expected in at least two contexts;
- rows or captures that should not match;
- behavior for sentinels and missing data;
- what would falsify or narrow the proposal.

Prefer a test where the predictions diverge. Repeating a case in which all candidates equal `1` adds coverage but not discrimination.

### Seek independent corroboration

Section ID: `ownkb:section:d000120:s000009`

Cautions: `do not`
Provenance cues: `catalogue`, `evidence`, `specification`

Strong conclusions normally combine evidence classes that do not merely repeat the same implementation assumption.

| Primary observation | Useful independent corroboration |
| --- | --- |
| undeclared column relationship | application query, UI behavior, or complete association path |
| diagnostic field | product diagram, controlled configuration change, or public specification |
| resource-key semantics | literal functional frame and UI placement |
| catalogue condition | observed visibility or accepted/rejected programming value |
| default or sentinel pattern | competing concrete rows and runtime selection behavior |

Two association tables populated by the same loader are valuable structural evidence, but not necessarily independent semantic evidence.

### Search for counterexamples

Section ID: `ownkb:section:d000120:s000010`

Applicability cues: `firmware`, `revision`
Cautions: `do not`
Uncertainty: `may`

Test the full populated domain where feasible, including:

- `NULL`, `0`, empty, negative, and default rows;
- duplicate external identifiers;
- Objects assigned to several systems;
- items with several firmware definitions or builds;
- fixed and replaceable Object alternatives;
- Devices with different Module layouts;
- another diagnostic family or firmware revision;
- positive, negative, error, and timeout outcomes.

A counterexample may reject a claim or reveal a missing condition. Do not discard it merely because most rows match.

### Change one variable at a time

Section ID: `ownkb:section:d000120:s000011`

Controlled UI and Device tests are strongest when exactly one input changes. Record a baseline, perform one change, repeat the same requests, and diff both traffic and persisted state.

For state-changing tests:

1. read and save the baseline;
2. confirm that the target Device and Module are uniquely identified;
3. change one property;
4. record acknowledgement and terminal state;
5. read the configuration back;
6. restore the baseline when safe;
7. distinguish accepted transfer from effective configuration.

An `ACK` alone is not verification.

### Classify and promote the result

Section ID: `ownkb:section:d000120:s000012`

Cautions: `limitation`
Uncertainty: `unresolved`
Provenance cues: `documentation`, `evidence`

Use the levels in [Evidence and Confidence](evidence-and-confidence.md). Promote a result into reference documentation only when:

- the namespace and scope are explicit;
- known values resolve or exceptions are documented;
- viable alternatives have been tested;
- the claim can be applied without access to the original investigator’s intuition;
- a falsifier or remaining limitation is recorded.

The reverse-engineering section retains the evidence path, unresolved alternatives, and rejected shortcuts. The stable operational conclusion belongs in the relevant Protocol, Device Model, Diagnostics, Programming, Scenario Engine, or Internals page.

### Reproducibility checklist

Section ID: `ownkb:section:d000120:s000013`

Applicability cues: `revision`
Uncertainty: `unknown`
Provenance cues: `evidence`, `source`

Before closing an investigation, verify that another person can recover the same conclusion from:

- source fingerprints and revision;
- exact queries, requests, and response context;
- raw values and exception rows;
- namespace and sentinel rules;
- cardinality and coverage counts;
- supporting and contradicting evidence;
- confidence, scope, and falsifier;
- links to the promoted result and the [Relationship Register](relationship-register.md).

Unknown is a valid outcome. A well-bounded unknown is more useful than an attractive but untestable mapping.

# Document: ownkb:document:d000121

Source path: `reverse-engineering/open-questions.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Open Questions

Section ID: `ownkb:section:d000121:s000001`

Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `documentation`, `evidence`

This page contains only questions that remain unresolved after cross-checking the canonical MyHOME Suite 3.5.38 databases, `OpenQuery.txt`, the incorporated captures, product documentation, and the relationships established elsewhere in this documentation.

Each entry states the known boundary before the missing evidence so that later investigations do not reopen facts that are already established.

### WHO 13 gateway properties

Section ID: `ownkb:section:d000121:s000002`

#### `DIMENSION 20`

Section ID: `ownkb:section:d000121:s000003`

Applicability cues: `gateway`, `scs`, `tcp`, `version`, `zigbee`
Cautions: `do not`, `not evidence`
Provenance cues: `capture`, `evidence`, `source`

Prior gateway-identification research has flagged `WHO 13 DIMENSION 20` as an encountered property, but the currently preserved evidence chain does not yet establish its classic SCS/TCP semantics. The canonical classic `WHO_13.pdf` registry does not define it, the ZigBee `WHO 13` registry does not define it, canonical MyHOME Suite `OPEN.db` provides no functional `WHO 13 DIMENSION 20` template, and the preserved F454 and MH202 gateway-information captures examined in the current correction do not contain it.

This is a **provenance gap**, not evidence that the property does not exist. Promotion to the functional reference requires the specific canonical source or first-hand capture that establishes the request/response form and payload, followed by semantic corroboration. Do not infer a meaning from diagnostic `DIMENSION 6` microcontroller-version fields or from any numerically similar namespace.

#### `DIMENSION 40`

Section ID: `ownkb:section:d000121:s000004`

Applicability cues: `firmware`, `gateway`, `scs`, `tcp`, `version`, `zigbee`
Uncertainty: `unknown`, `unresolved`
Provenance cues: `evidence`, `source`, `specification`

Existence is established more strongly than semantics. Independent first-hand F454 and MH202 gateway-information captures both show `*#13**40##` and both return `*#13**40*4*0##`.

What remains unresolved is the meaning of the two returned values, whether either field varies independently, and the applicability across gateway models and firmware revisions. The next discriminating evidence is a cross-model or cross-firmware observation in which at least one returned value differs, or a canonical implementation/specification source naming the fields. Until then, preserve the response as two positional unknown values.

The ZigBee specification's `DIMENSION 17` hardware-version definition is not part of this open question: that meaning is established for the ZigBee `WHO 13` variant. What remains unestablished is whether any classic SCS/TCP implementation reuses numeric `17` with the same semantics.

### Diagnostic and programming fields

Section ID: `ownkb:section:d000121:s000005`

#### `DIMENSION 32.SYS`

Section ID: `ownkb:section:d000121:s000006`

Uncertainty: `unknown`
Provenance cues: `catalogue`, `database`

`MHCatalogue.db.EN_SYSTEM.sys_modobj` is the leading candidate. Lighting/Automation observations cannot distinguish it from coincident values in other namespaces.

A successful non-Lighting response is still required. The most discriminating cases are Thermoregulation, Energy Management, Access Control, and Integration Functions, whose `sys_modobj`, database system ID, and functional `WHO` values differ.

It also remains unknown how `SYS` selects one active context when an Object belongs to several catalogue systems.

#### `DIMENSION 4` and `5`

Section ID: `ownkb:section:d000121:s000007`

Applicability cues: `firmware`
Uncertainty: `unresolved`
Provenance cues: `catalogue`, `database`

`OPEN.db` establishes the transport surface: `DIMENSION 4` carries `C1..C6`, `DIMENSION 5` carries `C7..C12`, and every `C` field has range `0..255`. The `ConfConfigurators` sequence sends the corresponding programming forms and is described there as virtual configuration.

What remains unresolved is the cross-database correlation to catalogue semantics. No canonical relation establishes that `C1` equals the firmware `EN_CONF` row with `progressive = 1`, or an equivalent positional rule for every firmware. Controlled observations are still needed to determine how `C1..C12` encode physical/configurator contents in Device families and how those transport positions correspond, where applicable, to firmware-specific symbols such as `A`, `PL`, `M`, `G`, `I`, `ZA`, `ZB`, `N`, `T`, and `S`.

This question no longer concerns the existence or numeric transport range of `C1..C12`; those are established. It concerns their Device-specific semantic correlation with catalogue definitions and physical positions.

#### `DIMENSION 310`

Section ID: `ownkb:section:d000121:s000008`

`DIMENSION 310` carries an Object-specific value without a generic configuration index. `OPEN.db` supplies neither ordinary parameter metadata nor a general decoder for it.

Its meaning and value domain remain to be established per Object and Device family.

#### Hardware and microcontroller versions

Section ID: `ownkb:section:d000121:s000009`

Applicability cues: `firmware`, `version`
Uncertainty: `unknown`
Provenance cues: `catalogue`, `source`

`DIMENSION 3` and `6` use the same logical `Version*Release*Build` structure as the firmware response. No corresponding hardware- or microcontroller-version fields have been found in the canonical databases.

It remains unknown whether MyHOME Suite uses these values to distinguish product variants or compatibility, and whether an unpreserved data source maps them to catalogue Devices.

### Address selection and encoding

Section ID: `ownkb:section:d000121:s000010`

Applicability cues: `only for`, `revision`
Provenance cues: `database`

The database establishes system-to-rule associations, address templates, and Object-family qualification. It does not preserve the final selection and rendering algorithm.

The remaining questions are:

- How does MyHOME Suite choose among a system's family-qualified and family-unqualified address rules?
- How are `level_2_rule` and `level_4_rule` consumed? Their nonzero values occur on the Lighting/Automation general, environment, group, and F422 extension rules, but the runtime composition with the dedicated level rules is not encoded.
- How is `validity_rule` evaluated? The only nonempty expression in this revision is `MOD=SLA;` on the Thermoregulation slave-probe rule.
- How is `offset_adv` applied? It is populated only for the two F422 mode-specific rules, with values `496` and `256`.
- Under which Device layouts does the diagnostic outer `WHERE` follow the configured address of `slot` `1`, and what rule applies when slot `1` is absent, disabled, or differently addressed?

### Catalogue behavior

Section ID: `ownkb:section:d000121:s000011`

#### Firmware selection

Section ID: `ownkb:section:d000121:s000012`

Applicability cues: `firmware`
Uncertainty: `unknown`
Provenance cues: `catalogue`

The catalogue firmware identity is the three-component `V.R.b` tuple distributed across `EN_FIRMWARE` and `EN_BUILDS`. An explicit `-1` is strongly corroborated as any or unspecified for that component, while a missing build row remains structurally distinct.

The exact MyHOME Suite selection precedence remains unknown when concrete components, `-1` sentinels, multiple build rows, missing build rows, `FW_default`, and localization metadata overlap.

#### Object replacement

Section ID: `ownkb:section:d000121:s000013`

Applicability cues: `firmware`
Uncertainty: `unknown`

`fixed_ko`, visibility/editability metadata, conditions, firmware, slot, and product context all contribute to the available Object set.

The complete rule that determines whether MyHOME Suite displays and permits replacement of an Object at a particular Module remains unknown.

#### Physical-to-advanced and transport correlation

Section ID: `ownkb:section:d000121:s000014`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `evidence`

The catalogue-native physical topology mechanism is now established for condition-represented branches: resolve firmware physical definitions and legal domains, enumerate `AS_OBJECT_FIRMWARE`/`EN_SLOTS` candidates, constrain `AS_SLOT_CONDITION`/`EN_CONDITION` branches by reachability, select the matching Object topology, and only then evaluate applicable `EN_CONV_RULE` rows. `EN_PHY_TO_ADV_TRANS` remains a sparse supporting table with only three firmware rows and is not the generic mechanism.

Open boundaries remain narrower:

- whether and how `DIMENSION 4.C1..C12` correlate with firmware `EN_CONF` definitions or `progressive` ordering for each Device family;
- how to interpret catalogue candidates that have no explicit physical predicate when reconstructing a complete physical topology;
- whether textual irregularities such as `O/I` versus `I/O` have an application-level normalization not represented in the canonical databases;
- which property-level physical-to-advanced correspondences are complete when symbol, range, conversion, or `CONF_SYMBOL_REF` evidence is absent;
- how the registered catalogue mode labels correspond to every MyHOME Suite UI path beyond the exact sequence labels preserved in `OPEN.db`.

#### Catalogue-wide addressed-form `N_CONF` equivalence

Section ID: `ownkb:section:d000121:s000015`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`

For the ordinary addressed Device form, the meaning of `N_CONF` is corroborated as the number of physical configurator positions provided by the Device. Resolved examples also match the count of applicable firmware-scoped physical configuration fields after excluding the common `AID`/ID field.

What remains open is whether that database-count equivalence holds for every catalogue firmware, including conditional fields, shared firmware definitions, and Devices without available product diagrams. This question does not reopen the addressed-form interpretation.

#### Gateway `N_CONF = 15`

Section ID: `ownkb:section:d000121:s000016`

Applicability cues: `firmware`, `gateway`
Provenance cues: `evidence`

The empty-`WHERE` gateway identity form is a separate case. First-hand MH202 and F454 captures both return `N_CONF = 15`, outside the ordinary addressed-form `0..12` range. Numerically, `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern. A reserved or sentinel interpretation is therefore plausible, but the available evidence does not establish what the value signifies.

The open question is the exact gateway semantics of `N_CONF = 15`. Evidence that could resolve it includes an applicable MyHOME_Suite decoder or resource definition, an authoritative protocol definition, or controlled observations across gateway models and firmware revisions that distinguish literal count, reserved-value, and applicability interpretations.

### Scenario Engine

Section ID: `ownkb:section:d000121:s000017`

Applicability cues: `revision`

The two ScenarioDevices databases are capability catalogues, not persisted scenario graphs. Their common semantic content and revision differences are established; local row identifiers are not stable across the two files.

The remaining questions are:

- Which ScenarioDevices copy does MyHOME Suite load, and under what installation, update, or runtime conditions?
- Are the Program Files and ProgramData copies synchronized or migrated?
- Where are user-authored scenario graphs and their node ordering, branches, bindings, and execution state persisted?
- How are frame-absent trigger and condition capabilities connected to runtime events?
- What application enumerations and UI behaviors define `CategoryFlag`, `WhereType`, Parameter `Type`, and `OperatorType`? Their stored value distributions and semantic clusters are known, but their exact enum contracts are not.
- What runtime matching behavior uses `ObjectMatchingId` and `CommandMatchingId`?

### Application internals

Section ID: `ownkb:section:d000121:s000018`

Provenance cues: `source`

`OpenQuery.txt` establishes a set of named reads and their selected columns, but it is incomplete and does not identify callers or runtime control flow.

The remaining questions are:

- When and how are the databases opened, cached, invalidated, refreshed, synchronized, or migrated?
- Which application components execute each query in `OpenQuery.txt`, and are all named queries used?
- How are the separately selected address-rule columns consumed? The earlier bitwise-expression question was based on an incorrect source attribution; see the [Registry Source Correction](../internals/openwebnet-registry-and-state-machines.md#incompleteness-preserved-in-the-source).
- Which resources and application components resolve stored localization keys?
- What locale-selection, fallback, missing-key, and composed-label rules are applied?

### Evidence priorities

Section ID: `ownkb:section:d000121:s000019`

Applicability cues: `firmware`, `gateway`, `revision`, `version`
Provenance cues: `database`

The highest-value next observations are:

1. recover the canonical provenance for classic `WHO 13 DIMENSION 20` and obtain a discriminating `DIMENSION 40` observation across a different gateway or firmware revision;
2. one successful non-Lighting `DIMENSION 32` response whose candidate `SYS` values differ;
3. controlled `DIMENSION 4` and `5` captures across known physical configurator changes;
4. a controlled Device/item case exercising concrete, wildcarded, multiple, or missing firmware build records;
5. file-access, database-statement, and save-operation traces while creating one minimal scenario;
6. a runtime trace of address-rule selection for a system with both general and family-qualified rules;
7. hardware and microcontroller version observations across known revisions of the same product.

Each result should update the [Relationship Register](relationship-register.md) and then the appropriate reference section.

# Document: ownkb:document:d000122

Source path: `reverse-engineering/rejected-relationships.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Rejected Relationships

Section ID: `ownkb:section:d000122:s000001`

Applicability cues: `applies to`
Provenance cues: `evidence`

Rejected interpretations are retained because they are plausible enough to be rediscovered from names, equal integers, or incomplete captures. Each entry records why the shortcut fails and the safer replacement.

“Rejected” applies to the stated unconditional interpretation. A narrower relationship can be reconsidered when new evidence addresses the rejecting evidence.

### Database identity and key mistakes

Section ID: `ownkb:section:d000122:s000002`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `evidence`

| Rejected interpretation | Conflicting evidence | Safe treatment |
| --- | --- | --- |
| `EN_DEVICE.code → EN_LANGUAGE.code` | Device `code` contains product codes/SKUs; identical column names have unrelated roles | treat `EN_DEVICE.code` as product identity and resolve language through actual localization structures |
| `MHCatalogue.EN_SYSTEM.id_system = OPEN.EN_SYSTEM.id_system` | independent registries show only partial numeric coincidence | correlate systems through meaning, external fields, functional/diagnostic families, and Object membership |
| diagnostic Device `ID = EN_DEVICE.id_device` | wire ID is an installed 32-bit instance identifier; catalogue key identifies a product row | retain both identifiers and correlate through `DIMENSION 1` semantics |
| diagnostic `SLOT = EN_SLOTS.id_slot` | wire slot is Device-local; `id_slot` is an association-row key | correlate with `EN_SLOTS.first_slot` after firmware resolution |
| `EN_KEY_OBJECT.id_key_object = EN_KEY_OBJECT.key_object` | internal and external identifiers are distinct columns and not generally equal | label both namespaces explicitly |
| one `EN_ITEM` identifies one SKU | several branded Device records can share one item | return the candidate Device/SKU set until brand, line, or external evidence narrows it |
| one `EN_FIRMWARE` row has exactly one `EN_BUILDS` row | 19 firmware definitions have no build row and 15 have multiple build rows | model firmware-to-build as zero-to-many |
| no build row means `firmware_b = -1` | absence and explicit sentinel are structurally different states | preserve both cases independently |
| every negative integer is an orphan | `-1` is strongly corroborated as any/unspecified in firmware components | determine sentinel semantics per column before orphan analysis |

### Capability and Module mistakes

Section ID: `ownkb:section:d000122:s000003`

Applicability cues: `firmware`
Provenance cues: `evidence`

| Rejected interpretation | Conflicting evidence | Safe treatment |
| --- | --- | --- |
| `EN_FIRMWARE.slots = COUNT(EN_SLOTS rows)` | one `slot` can offer several Object alternatives | count distinct `first_slot` positions and interpret alternatives separately |
| an `EN_SLOTS` row is one runtime Module | rows represent firmware/Object placement alternatives | build runtime Modules from `DIMENSION 30`, then validate against placement capability |
| `fixed_ko = 1` alone proves the UI field is read-only | visibility, conditions, product context, and UI behavior also contribute | use `fixed_ko` as designated/fixed capability evidence, not a complete UI rule |
| a Virgin Object is the regular configured Object | Virgin Objects describe configurable templates and permitted Object sets; `DIMENSION 30` reports the Virgin Object while the Module is disabled | use `DIMENSION 30.STATE` to select the namespace |
| every Object allowed by a Virgin Object is simultaneously active | association is capability, not runtime selection | resolve one reported configured Object per Module state |

### Protocol interpretation mistakes

Section ID: `ownkb:section:d000122:s000004`

Applicability cues: `firmware`, `gateway`, `only for`, `version`
Uncertainty: `contradict`, `unresolved`
Provenance cues: `capture`, `catalogue`, `evidence`

| Rejected interpretation | Conflicting evidence | Safe treatment |
| --- | --- | --- |
| `DIMENSION 1.N_CONF` is an Object, class, or form factor | ordinary addressed-form `OPEN.db` metadata, product diagrams, and captures identify a physical-configurator-position count; the gateway variant instead has unresolved semantics | retain the physical-position interpretation only for the corroborated ordinary addressed form; preserve gateway `N_CONF` raw and unresolved |
| `DIMENSION 30.KEYO` always names `EN_KEY_OBJECT.key_object` | disabled Modules (`STATE = 1`) use the Virgin Object namespace | branch on `STATE` before lookup |
| `DIMENSION 32.SYS` is automatically a functional `WHO` | system grouping and non-Lighting candidate values differ | retain `sys_modobj` as the leading inference pending a discriminating capture |
| diagnostic outer `WHERE` always equals slot `1` address | only selected layouts have been observed; disabled/alternate layouts are untested | treat the correlation as strong but conditional |
| every Module returns `DIMENSION 32` | command-only and optional-response observations contradict universality | model address response as Object/firmware dependent |
| actuators use only `DIMENSION 32`; commands use only `35` | a Module can expose address, indexed properties, both, or neither | determine availability from Object/firmware behavior |
| `DIMENSION 310` is an ordinary `EN_CONF.idx` record | frame has no index and lacks generic parameter metadata | decode per Object/Device family |
| `[FW_VERSION]`, `[HW_VERSION]`, or `[MICRO_VERSION]` is one scalar | parameter descriptions define `Version*Release*Build` | preserve three components and their separators |
| hardware or micro version maps to `EN_PACKAGE`/`EN_FILE` version fields | those rows describe associated packages/files; no hardware/micro catalogue field exists | retain `DIMENSION 3`/`6` as installed-state evidence |
| `DIMENSION 4`/`5` values are proven presence bits | no controlled position/value matrix establishes the encoding | keep contents/presence/combined alternatives open |
| an `ACK` proves effective configuration | acknowledgement, accepted transfer, persistence, and read-back are distinct | verify terminal state and diagnostic read-back |

### Configuration and validation shortcuts

Section ID: `ownkb:section:d000122:s000005`

Applicability cues: `firmware`
Uncertainty: `may`
Provenance cues: `catalogue`

| Rejected shortcut | Why unsafe | Safe treatment |
| --- | --- | --- |
| validate only against `OPEN.db` range | transport capacity can exceed catalogue capability | apply property range, contextual filters, conditions, conversions, and linked rules |
| treat `id_key_object = 0` or `id_firmware = 0` as a broken reference | zero selects the complementary `EN_CONF` ownership branch | validate the exclusive ownership pattern |
| use a global `EN_CONF.idx` lookup | the same index can name different properties across Object/firmware contexts | resolve Device, firmware, Module, Object, and ownership first |
| use `DIMENSION 35.INDEX` without `slot` | repeated indexes can occur across Modules | include Device and slot in the correlation key |
| treat a visible UI field as writable | visibility, editability, fixed state, and conditions differ | corroborate with metadata and observed UI behavior |
| base range alone defines all legal values | `EN_FILTER`, filtered ranges, conditions, and other-property rules narrow it | evaluate the complete validation stack |
| physical counterpart proves active physical configuration | diagnostics reports effective configuration, not necessarily how it was set | distinguish physical capability from active method |
| same effective physical and Virtual value proves identical storage | conversion may produce the same runtime result | classify direct versus converted mapping through controlled changes |

### Cross-database and ScenarioDevices mistakes

Section ID: `ownkb:section:d000122:s000006`

Applicability cues: `revision`
Cautions: `do not`
Uncertainty: `unresolved`
Provenance cues: `evidence`

| Rejected interpretation | Conflicting evidence | Safe treatment |
| --- | --- | --- |
| equal local primary keys across databases identify the same concept | databases have independent namespaces | connect external identifiers or semantic paths only |
| ScenarioDevices `ObjectId = EN_KEY_OBJECT.key_object` | no declared or complete semantic mapping; models serve different purposes | correlate through literal frames and functional semantics |
| ScenarioDevices `FamilyId = functional WHO` | values are local editor groupings and do not encode `WHO` | derive `WHO` from literal frames/`ChiOpen` where present |
| ScenarioDevices ProgramData and Program Files rows align by `Id` | added rows cause local IDs to diverge | compare the complete semantic hierarchy and non-local fields |
| ProgramData is automatically authoritative because it is writable | revision delta does not prove runtime precedence | trace file opens, synchronization, or loader behavior |
| `Frame IS NULL` means the scenario capability is unsupported | most events/conditions depend on runtime mappings absent from the capability row | preserve the capability and mark the runtime matcher unresolved |
| symbolic frame text is literal OpenWebNet | several stored strings are application tokens | classify literal, symbolic, and absent templates before rendering |
| ScenarioDevices contains saved scenario graphs | schema lacks instances, edges, ordering, and execution state | locate the separate persistence layer |

### Evidence and reasoning failures

Section ID: `ownkb:section:d000122:s000007`

Applicability cues: `firmware`
Uncertainty: `may`
Provenance cues: `capture`, `database`, `evidence`, `source`, `specification`

| Failure | Why it fails | Correction |
| --- | --- | --- |
| first matching row proves the relationship | exceptions and duplicate namespaces remain invisible | test every populated value and report orphans/cardinality |
| two matching tables are independent corroboration | both may be generated from one internal model | seek a capture, UI observation, product document, or specification |
| silence proves unsupported behavior | selector, state, timeout, or transport may be wrong | record observation capability and terminal evidence |
| a database label is a universal protocol definition | labels describe one implementation and may be incomplete | separate stored implementation semantics from protocol guarantees |
| one Device capture defines a family rule | support and optionality vary by firmware/Object | scope the observation and seek contrasting products |
| correcting a canonical database improves the evidence | mutation destroys source fidelity and may encode false constraints | generate a separate derived artifact with a reproducible transformation |

### Reconsideration rule

Section ID: `ownkb:section:d000122:s000008`

Applicability cues: `revision`
Cautions: `do not`
Provenance cues: `evidence`, `source`

A rejected relationship can be reopened only when new evidence directly addresses its rejecting evidence.

The new claim record must include:

1. the exact rejected interpretation being narrowed or replaced;
2. the new source and revision;
3. complete coverage and exceptions;
4. the condition that makes the revised relationship valid;
5. a falsifier;
6. updates to the reference page, [Relationship Register](relationship-register.md), and [Open Questions](open-questions.md).

Do not silently delete a rejection. Preserve why the earlier unconditional claim failed.

# Document: ownkb:document:d000123

Source path: `reverse-engineering/relationship-register.md`
Namespace context: `contextual`
Area: `reverse-engineering`

## Relationship Register

Section ID: `ownkb:section:d000123:s000001`

Provenance cues: `documentation`, `evidence`

This register is the compact index of relationships whose evidence affects more than one documentation section. It records namespace, conditions, coverage, and confidence; detailed operational semantics remain on the linked reference pages.

### Status vocabulary

Section ID: `ownkb:section:d000123:s000002`

Applicability cues: `revision`
Provenance cues: `capture`, `database`, `evidence`

| Status | Meaning |
| --- | --- |
| Declared | enforced or explicitly represented by the stored schema |
| Structurally established | complete non-sentinel key coverage and compatible table/cardinality role in this revision |
| Corroborated | independent database, capture, UI, or product evidence confirms the meaning |
| Strongly inferred | one candidate best explains the complete pattern, but a discriminating observation is missing |
| Open | evidence cannot yet distinguish the remaining candidates |
| Rejected | evidence conflicts with the proposed relationship |

Counts are scoped to the canonical MyHOME Suite 3.5.38 sources.

### Within `MHCatalogue.db`

Section ID: `ownkb:section:d000123:s000003`

Applicability cues: `firmware`
Provenance cues: `catalogue`, `database`, `source`

| Source | Target | Coverage/conditions | Status |
| --- | --- | --- | --- |
| `EN_DEVICE.id_item` | `EN_ITEM.id_item` | 541 rows; 0 orphans | structurally established |
| `EN_DEVICE.id_brand` | `EN_BRAND.id_brand` | 541 rows; 0 orphans | structurally established |
| `EN_DEVICE.id_line` | `EN_LINE.id_line` | 541 rows; 0 orphans | structurally established |
| `EN_FIRMWARE.id_item` | `EN_ITEM.id_item` | 311 rows; 0 orphans | structurally established |
| `EN_BUILDS.id_firmware` | `EN_FIRMWARE.id_firmware` | 308 rows; 0 orphans; zero/multiple build rows possible per firmware | structurally established |
| `AS_ITEM_SYSTEM` | item and catalogue-system parents | 223 rows; 0 orphans on either parent | structurally established |
| `AS_OBJECT_SYSTEM` | Object and catalogue-system parents | 251 rows; 0 orphans on either parent | structurally established |
| `AS_OBJECT_FIRMWARE` | firmware and Object parents | 827 rows; 0 orphans on either parent | structurally established |
| `AS_FIRMWARE_CONFIG_MODE` | firmware and configuration-mode parents | firmware capability association; `EN_CONFIG_MODE` keeps Virtual, Advanced, Physical, and Product Programming as distinct records | structurally established |
| `EN_SLOTS.id_object_firmware` | `AS_OBJECT_FIRMWARE.id_object_firmware` | 1,725 rows; several Object alternatives can share `first_slot` | structurally established |
| `EN_KEY_OBJECT.id_family` | `EN_OBJECT_ITEM_FAMILY.id_family` | 158 rows; 0 orphans; no zero sentinel used | structurally established |
| `AS_FIRMWARE_VIRGIN_OBJECT` | firmware and Virgin Object parents | 75 rows; 0 orphans | structurally established |
| `AS_OBJECT_VIRGIN_OBJECT` | Virgin Object and permitted Object parents | 102 rows; capability set, not runtime selection | structurally established |
| `EN_CONF_RANGE.id_conf` | `EN_CONF.id_conf` | 14,346 rows; 0 orphans | structurally established |
| `EN_FILTER` | Object/firmware association and configuration definition | 1,909 rows; 0 orphans on both references | structurally established |
| `AS_SLOT_CONDITION` | slot-placement row and condition | 1,000 rows; 0 orphans on both references | structurally established |
| physical condition branch | firmware `EN_CONF`/`EN_CONF_RANGE` domains plus `EN_SLOTS`/`AS_SLOT_CONDITION`/`EN_CONDITION` | stored condition must be reachable in the exact firmware domain before it can select an Object/slot candidate | catalogue-native resolver established for represented predicates |
| `EN_CONF` owner | Object or firmware | 1,420 Object-scoped; 1,463 firmware-scoped; selected by zero discriminator | established polymorphic relationship |
| `EN_FIRMWARE.slots` | distinct internal Module positions | compare with `COUNT(DISTINCT EN_SLOTS.first_slot)`, not row count | corroborated capability relationship |

See [Database Relationship Reconstruction](database-relationship-reconstruction.md) and [Device Model](../device-model/).

### Within `OPEN.db`

Section ID: `ownkb:section:d000123:s000004`

Provenance cues: `evidence`, `source`

| Source | Target | Coverage/evidence | Status |
| --- | --- | --- | --- |
| `AS_SYSTEM_ADDRESS_RULE` | system and address-rule parents | 16 rows; 0 orphans; loaded by `OpenQuery.txt` | established |
| `AS_OPEN_SYSTEM` | frame and system parents | 251 rows; 0 orphans | established |
| `AS_OPEN_PARAM` | frame and parameter parents | 91 rows; 0 orphans; queried by `OpenQuery.txt` | established |
| `AS_SCENARIO_SEQUENCE` | scenario and ordered sequence | 39 rows; 0 orphans | established |
| `AS_OPEN_SEQUENCE` | sequence and ordered frame | 147 rows; 0 orphans; carries order/repetition/status metadata | established |
| `AS_TIMEOUT_OPEN_SEQUENCE` | frame/sequence context and timeout | 62 rows; 0 orphans on all three parents | established |
| `EN_OPEN.open_string` placeholders | `EN_OPEN_PARAM.param_string` | association required; placeholder text alone is not a global key | established where associated |

### Across wire traffic and catalogue

Section ID: `ownkb:section:d000123:s000005`

Applicability cues: `firmware`, `gateway`
Uncertainty: `unresolved`
Provenance cues: `capture`, `catalogue`, `database`, `evidence`, `source`

| Source | Target | Required context | Status |
| --- | --- | --- | --- |
| `DIMENSION 1.OBJECT_MODEL` | `AS_ITEM_SYSTEM.modobj` | resolved management/catalogue system | corroborated |
| `DIMENSION 1.BRAND` | `EN_BRAND.brand_modobj` | parsed identity response | corroborated |
| `DIMENSION 1.LINE` | `EN_LINE.line_modobj` | parsed identity response | corroborated |
| ordinary addressed `DIMENSION 1.N_CONF` | physical configurator-position count | addressed Device identity; product diagrams/captures | corroborated for documented addressed Devices |
| gateway `DIMENSION 1.N_CONF` | unresolved gateway-variant field; observed value `15` on MH202 and F454 | empty-`WHERE` gateway identity captures | observed; sentinel interpretation inferred, exact semantics open |
| `DIMENSION 2` `V.R.b` | `EN_FIRMWARE` plus `EN_BUILDS` | resolved item; sentinel/default/build handling | structurally corroborated; exact selection precedence open |
| `DIMENSION 3`/`6` `V.R.b` | no canonical catalogue field found | retain as installed-state evidence | open database correlation |
| `DIMENSION 30.KEYO` | `EN_KEY_OBJECT.key_object` | `STATE = 0`, enabled Module, resolved firmware and `slot` | experimentally corroborated with UI behavior |
| `DIMENSION 30.KEYO` | `EN_VIRGIN_OBJECT.virgin_key_object` | `STATE = 1`, disabled Module, resolved firmware and `slot` | experimentally corroborated with UI behavior |
| `DIMENSION 30.SLOT` | `EN_SLOTS.first_slot` placement | resolved firmware; not `id_slot` | structurally corroborated |
| `DIMENSION 35.INDEX` | `EN_CONF.idx` | Device, firmware, Module, Object, and ownership scope | strongly corroborated |
| diagnostic outer `WHERE` | configured address of `slot` `1` | repeated `WHO 1001` observations | strongly inferred; alternate layouts open |
| `DIMENSION 32.SYS` | `MHCatalogue.db.EN_SYSTEM.sys_modobj` | resolved Object/system context | strongly inferred; needs discriminating non-Lighting capture |

### Across database models

Section ID: `ownkb:section:d000123:s000006`

Applicability cues: `firmware`, `only for`, `revision`
Provenance cues: `catalogue`, `database`, `evidence`, `source`

| Source | Target | Conditions/evidence | Status |
| --- | --- | --- | --- |
| `OPEN.EN_ADDRESS_RULE.object_device_family` | `MHCatalogue.EN_OBJECT_ITEM_FAMILY.id_family` | all 11 nonzero values resolve; `0` is unqualified; semantics agree | structurally and semantically corroborated |
| `rules.KOBJECTS` | `EN_KEY_OBJECT.key_object` | Objects `95`, `96`, and `184` represented in this revision | strongly corroborated |
| `rules.db3` `$N` reference | `EN_CONF.idx = N` | selected Object context and parsed rule syntax | strongly corroborated |
| ScenarioDevices `ChiOpen` | functional `WHO` parsed from literal `Frame` | all 57 literal templates in Program Files revision agree | established for literal templates |
| ScenarioDevices ProgramData semantic path | Program Files semantic path | compare full hierarchy/non-local fields, never local row IDs | established subset relationship |
| physical firmware property | advanced Object property | symbol, semantic type, filters, conversions, and controlled read-back | established only for individually corroborated mappings; generalization open |
| `OPEN.db` `DIMENSION 4/5.C1..C12` | `MHCatalogue.db` firmware `EN_CONF` definitions / `progressive` | transport fields and catalogue ordering coexist, but no explicit cross-database key or universal positional rule is present | open correlation |

### Sentinel and discriminator rules

Section ID: `ownkb:section:d000123:s000007`

Applicability cues: `firmware`, `gateway`
Uncertainty: `unresolved`
Provenance cues: `source`

| Location | Rule | Status |
| --- | --- | --- |
| `EN_CONF.id_key_object` / `id_firmware` | exactly one owner resolves and the other is `0` | established |
| `EN_ADDRESS_RULE.object_device_family = 0` | family-unqualified address rule | corroborated by complete rule set |
| firmware component `-1` | any or unspecified for that component | strongly corroborated by `-1.-1.-1` and concrete `V.R.-1` rows |
| missing `EN_BUILDS` row | distinct from explicit `firmware_b = -1` | structurally established |
| `DIMENSION 30.STATE` | `0` selects enabled regular Object; `1` selects disabled Virgin Object | experimentally corroborated with MyHOME_Suite UI behavior |
| gateway `DIMENSION 1.N_CONF = 15` | `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern consistent with a reserved-sentinel convention, but no canonical source establishes the sentinel meaning | observed value; sentinel interpretation inferred and unresolved |

Sentinel meaning is local to the field. This table does not authorize interpreting every zero or negative value the same way.

### Open relationships

Section ID: `ownkb:section:d000123:s000008`

Applicability cues: `firmware`, `gateway`
Uncertainty: `hypothesis`
Provenance cues: `catalogue`, `evidence`, `source`

| Question | Leading evidence | Decisive evidence needed |
| --- | --- | --- |
| `DIMENSION 4`/`5` catalogue correlation | `C1..C12` transport fields and `0..255` ranges are established; `ConfConfigurators` is labelled virtual configuration | controlled Device-family correlation between `C1..C12` and firmware-specific `EN_CONF` symbols/positions |
| generic `DIMENSION 310.VAL_PAR` meaning | Object-specific response without generic index metadata | Object-specific captures and decoder behavior |
| catalogue-wide addressed-form `N_CONF` field-count equivalence | diagrams, captures, and resolved firmware fields agree in tested addressed Devices | systematic conditional-field audit across firmware |
| gateway `N_CONF = 15` meaning | MH202 and F454 gateway captures both return out-of-range `15`; `15 = 0xF` is compatible with a sentinel | an applicable implementation decoder, authoritative definition, or discriminating gateway/firmware observations that establish the encoded meaning |
| firmware selection precedence | exact, wildcard, default, missing, multiple-build patterns | controlled loader/UI observation |
| ScenarioDevices matching IDs | stable local fields and semantic hierarchy | runtime matcher trace or application code |
| ScenarioDevices source precedence | two revisions in different installation locations | file-open/update trace |
| scenario-instance persistence | capability stores lack graph structure | controlled save diff and file trace |

The full research backlog and proposed experiments are in [Open Questions](open-questions.md) and [Hypothesis Testing](hypothesis-testing.md).

### Maintenance rule

Section ID: `ownkb:section:d000123:s000009`

Applicability cues: `revision`
Provenance cues: `evidence`, `source`

When evidence changes a relationship:

1. update the detailed reference page;
2. update this register's status, conditions, and coverage;
3. remove or narrow the corresponding open question;
4. retain rejected alternatives when they are likely to recur;
5. record the source revision and test that caused the change.

# Document: ownkb:document:d000124

Source path: `scenario-engine/README.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Scenario Engine

Section ID: `ownkb:section:d000124:s000001`

The Scenario Engine section documents the capability model used by MyHOME_Suite to expose triggers, conditions, and actions and to associate them with OpenWebNet command templates.

It is distinct from:

- functional OpenWebNet scenarios under functional `WHO 0` and `WHO 17`;
- diagnostic and programming scenarios in `OPEN.db`, which describe MyHOME_Suite communication sequences;
- the configuration of scenario-capable Physical Devices.

The canonical sources for this section are the two ScenarioDevices databases preserved under [`sources/`](../sources/myhome-suite/3.5.38/databases/):

- [`ScenarioDevices-program-files.sqlite`](../sources/myhome-suite/3.5.38/databases/ScenarioDevices-program-files.sqlite);
- [`ScenarioDevices-programdata.sqlite`](../sources/myhome-suite/3.5.38/databases/ScenarioDevices-programdata.sqlite).

### Reference

Section ID: `ownkb:section:d000124:s000002`

Applicability cues: `revision`
Provenance cues: `database`, `evidence`, `source`

| Subject | Page |
| --- | --- |
| Source provenance, evidence roles, and identifier boundaries | [Sources and Identifier Boundaries](sources-and-identifiers.md) |
| Database roles, schema, relationships, and revision differences | [Database Model](database-model.md) |
| Scenario roles and cross-role matching identifiers | [Categories and Matching](categories-and-matching.md) |
| Resolving systems, Objects, commands, and parameters | [Capability Resolution](capability-resolution.md) |
| Parameter types, operators, domains, and composite values | [Parameters](parameters.md) |
| Interpreting and rendering stored command templates | [Frame Templates](frame-templates.md) |
| Correlations with functional OpenWebNet namespaces | [Functional Correlations](functional-correlations.md) |
| Functional/category coverage and source-revision delta | [Capability Coverage](capability-coverage.md) |
| Established action pipeline and runtime boundaries | [Execution Model](execution-model.md) |
| Evidence limits and questions requiring further investigation | [Open Questions](open-questions.md) |

### Canonical hierarchy

Section ID: `ownkb:section:d000124:s000003`

Uncertainty: `may`
Provenance cues: `catalogue`

Both databases use the same principal hierarchy:

**Object System → Device Object → Command → Parameter**

| Level | Table | Role |
| --- | --- | --- |
| Object System | `ObjectSystems` | groups scenario capabilities by functional area and category |
| Device Object | `DeviceObjects` | describes a scenario-engine Object within one Object System |
| Command | `Commands` | defines a trigger, condition, or action and may provide a frame template |
| Parameter | `Parameters` | defines placeholders, domains, operators, constants, and value types for one Command |

The relationships are declared as SQLite foreign keys:

- `DeviceObjects.ObjectSystem_Id → ObjectSystems.Id`;
- `Commands.DeviceObject_Id → DeviceObjects.Id`;
- `Parameters.Command_Id → Commands.Id`.

These IDs are local to each ScenarioDevices file. They are not `WHO`, `WHAT`, catalogue `id_key_object`, external `key_object`, or Device IDs.

### Source revisions

Section ID: `ownkb:section:d000124:s000004`

Applicability cues: `revision`
Provenance cues: `source`

| Source | Object Systems | Device Objects | Commands | Parameters | Additional field |
| --- | --- | --- | --- | --- | --- |
| `ScenarioDevices-program-files.sqlite` | 29 | 44 | 157 | 42 | `ObjectSystems.FamilyId` |
| `ScenarioDevices-programdata.sqlite` | 27 | 42 | 151 | 40 | none |

The repository names distinguish two files that were both originally named `ScenarioDevices.sqlite`: one installed under `Program Files (x86)` and one under the shared `ProgramData` directory. Their canonical fingerprints and paths are recorded in [Sources and Identifier Boundaries](sources-and-identifiers.md).

The files overlap substantially but are not byte-identical or row-identical revisions. The semantic content of `programdata` is an exact subset of `program-files` when compared through the full hierarchy; local row IDs are not cross-file identifiers.

The larger `program-files` revision adds Virtual Key Card event capabilities and two Temperature Control actions absent from `programdata`. See [Capability Coverage](capability-coverage.md) for the exact delta.

### Capability path

Section ID: `ownkb:section:d000124:s000005`

To enumerate one scenario capability:

1. select an `ObjectSystems` row;
2. enumerate its `DeviceObjects`;
3. enumerate the Commands for each Device Object;
4. load zero or more Parameters for each Command;
5. interpret the Command's `Frame`, `ChiOpen`, `WherePlaceholder`, and `WhereType`;
6. substitute only validated address and parameter values;
7. correlate the rendered result with the relevant functional `WHO` reference;
8. preserve commands whose `Frame` is absent as capabilities requiring separate interpretation rather than discarding them.

### Cross-source boundaries

Section ID: `ownkb:section:d000124:s000006`

Applicability cues: `firmware`
Cautions: `do not`
Provenance cues: `database`, `source`

The ScenarioDevices databases describe scenario-editor capabilities and command templates. They do not directly identify installed Physical Devices or their current configuration.

| Question | Source |
| --- | --- |
| Which Device and Modules are installed? | [Diagnostics](../diagnostics/) |
| Which Objects can firmware expose? | [Device Model](../device-model/) |
| What does a functional frame mean? | [Functional reference](../functional/) |
| How are Devices configured? | [Programming](../programming/) |
| How does MyHOME_Suite order diagnostic/programming exchanges? | `OPEN.db`, not the ScenarioDevices hierarchy |

Equal numeric values across these sources do not establish a join. `ObjectId`, `ObjectMatchingId`, `CommandId`, and `CommandMatchingId` require independent correlation before they can be mapped to another database namespace.

### Evidence status

Section ID: `ownkb:section:d000124:s000007`

Uncertainty: `unknown`
Provenance cues: `database`, `documentation`, `source`

Established directly:

- table structures and declared foreign keys;
- stored names, IDs, category flags, templates, placeholders, ranges, steps, and constants;
- row counts in the canonical files;
- differences between the two source revisions.

Implementation-derived:

- `CategoryFlag` separates primary/start events, complementary/stop events, conditions, and actions;
- `FamilyId` groups category rows into local scenario-editor functional families;
- matching IDs correlate selected Lighting and Hotel concepts across scenario roles;
- literal templates cover functional `WHO 0`, `1`, `2`, `4`, and `14`.

Still partially interpreted or unknown:

- the exact application enumerations for `WhereType`, parameter `Type`, and `OperatorType`;
- how matching groups are used by the editor or runtime;
- the execution mapping for symbolic and frame-absent Commands;
- how MyHOME_Suite selects, synchronizes, or prioritizes the two source files.

Unknown values remain unknown until database correlations, application behavior, public documentation, or observed execution establishes their semantics.

# Document: ownkb:document:d000125

Source path: `scenario-engine/capability-coverage.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Capability Coverage

Section ID: `ownkb:section:d000125:s000001`

Applicability cues: `revision`
Provenance cues: `source`

This page summarizes the capabilities present in `ScenarioDevices-program-files.sqlite`, the larger canonical revision. Counts are descriptive of this source, not protocol limits.

### Coverage by family and category

Section ID: `ownkb:section:d000125:s000002`

| Family | Category | Device Objects | Commands | Parameters | Commands with non-null `Frame` |
| --- | --- | --- | --- | --- | --- |
| Alarm | primary event | 1 | 3 | 0 | 0 |
| Alarm | complementary event | 1 | 3 | 0 | 0 |
| Alarm | action | 1 | 1 | 0 | 1 |
| Automation | action | 7 | 23 | 6 | 23 |
| Auxiliaries | primary event | 1 | 2 | 0 | 0 |
| Auxiliaries | complementary event | 1 | 2 | 0 | 0 |
| Auxiliaries | condition | 1 | 2 | 0 | 0 |
| Delay | action | 1 | 1 | 0 | 0 |
| Hotel | primary event | 2 | 12 | 0 | 0 |
| Hotel | complementary event | 2 | 12 | 0 | 0 |
| Hotel | condition | 1 | 11 | 0 | 0 |
| Hotel | action | 1 | 4 | 0 | 4 |
| Lighting | primary event | 2 | 4 | 0 | 0 |
| Lighting | complementary event | 2 | 4 | 0 | 0 |
| Lighting | condition | 2 | 4 | 1 | 0 |
| Lighting | action | 3 | 12 | 3 | 12 |
| Scenarios | action | 1 | 1 | 1 | 1 |
| Scheduled Scenarios | primary event | 2 | 8 | 8 | 0 |
| Scheduled Scenarios | complementary event | 2 | 8 | 8 | 0 |
| Special Commands | action | 1 | 2 | 0 | 2 |
| Temperature Control | start event | 1 | 2 | 0 | 0 |
| Temperature Control | stop event | 1 | 2 | 0 | 0 |
| Temperature Control | condition | 1 | 2 | 0 | 0 |
| Temperature Control | action | 1 | 19 | 6 | 19 |
| Time | primary event | 1 | 3 | 3 | 0 |
| Time | complementary event | 1 | 3 | 3 | 0 |
| Time | condition | 1 | 3 | 3 | 0 |
| Virtual Key Card | primary event | 1 | 2 | 0 | 0 |
| Virtual Key Card | complementary event | 1 | 2 | 0 | 0 |

Repeated resource keys across primary and complementary event categories are counted as separate scenario roles.

### Frame coverage

Section ID: `ownkb:section:d000125:s000003`

| Frame classification | Commands |
| --- | --- |
| `NULL` | 95 |
| literal OpenWebNet-shaped template | 57 |
| non-null symbolic text | 5 |

Most event and condition rows have no stored frame, while action rows more often contain literal or symbolic rendering data. This asymmetry suggests that incoming event matching is not represented solely by `Commands.Frame`.

### Stored functional `WHO` evidence

Section ID: `ownkb:section:d000125:s000004`

Provenance cues: `evidence`

| `ChiOpen` | Commands | Functional area indicated by literal frames |
| --- | --- | --- |
| `NULL` | 99 | events, conditions, delays, symbolic operations, and other rows |
| `0` | 1 | Scenarios |
| `1` | 17 | Lighting |
| `2` | 19 | Automation; one delay row also stores `2` without a frame |
| `4` | 19 | Temperature Control |
| `14` | 2 | Special Commands |

`ChiOpen` aligns with the literal frame `WHO` for established OpenWebNet templates. A non-null value without a literal frame is evidence of intended functional context, not by itself a renderable command.

### Address-type distribution

Section ID: `ownkb:section:d000125:s000005`

| `WhereType` | Commands | Observed contexts |
| --- | --- | --- |
| `0` | 58 | many frame-absent events and conditions |
| `1` | 59 | Alarm symbolic action, Lighting and Automation actions, other point-address-like templates |
| `2` | 25 | Temperature Control and related zone-address templates |
| `3` | 6 | Auxiliary contact events/conditions |
| `4` | 8 | CEN+ scheduled-scenario events |
| `5` | 1 | Delay action |

The contexts are not sufficient to define a universal address grammar for each numeric type. Use the functional `WHO` and the command template.

### Revision delta

Section ID: `ownkb:section:d000125:s000006`

Provenance cues: `source`

`ScenarioDevices-program-files.sqlite` adds the following resource-key capabilities absent from `programdata`:

- two Virtual Key Card Object Systems;
- two Virtual Key Card Device Objects;
- four Virtual Key Card event Commands across the two event categories;
- Temperature Control local-control action and Parameter;
- Temperature Control fan-coil-speed action and Parameter.

That accounts for the source-count delta:

| Entity | `program-files` | `programdata` | Difference |
| --- | --- | --- | --- |
| Object Systems | 29 | 27 | +2 |
| Device Objects | 44 | 42 | +2 |
| Commands | 157 | 151 | +6 |
| Parameters | 42 | 40 | +2 |

### Scope limits

Section ID: `ownkb:section:d000125:s000007`

Applicability cues: `gateway`
Provenance cues: `evidence`

The coverage table does not establish:

- which capabilities a particular installed Device exposes;
- how a user-authored scenario graph is persisted;
- how frame-absent events are matched at runtime;
- whether every stored action is supported by every gateway;
- whether `program-files` supersedes `programdata`.

Those questions require Device Model, application, runtime, or additional persistence evidence.

# Document: ownkb:document:d000126

Source path: `scenario-engine/capability-resolution.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Capability Resolution

Section ID: `ownkb:section:d000126:s000001`

This page describes how to turn ScenarioDevices rows into a structured scenario-editor capability without assuming that every stored identifier is an OpenWebNet wire value.

### Input

Section ID: `ownkb:section:d000126:s000002`

Provenance cues: `source`

Start with one source file and, where possible:

- a desired functional area;
- a desired role such as trigger, condition, or action;
- the installed Device/Object context from diagnostics and the Device Model;
- the functional `WHO` reference needed to validate a stored frame.

### Resolution path

Section ID: `ownkb:section:d000126:s000003`

Provenance cues: `evidence`, `source`

1. Select candidate `ObjectSystems` rows by established system/category evidence.
2. Enumerate their `DeviceObjects`.
3. Retain `ObjectId` and `ObjectMatchingId` as ScenarioDevices identifiers.
4. Enumerate each Object's Commands.
5. Load all Parameters for each Command.
6. Classify the command as literal-frame, symbolic-frame, or frame-absent.
7. Validate any stored `ChiOpen` against the functional frame.
8. Resolve `WHERE` according to the functional `WHO`, not `WhereType` alone.
9. Validate parameter values against stored metadata and the functional reference.
10. Return the capability with source-file and row provenance.

### Resolve the hierarchy

Section ID: `ownkb:section:d000126:s000004`

```sql
SELECT
    os.Id AS object_system_row,
    os.Name AS object_system_name,
    os.CategoryFlag,
    d.Id AS device_object_row,
    d.ObjectId,
    d.ObjectMatchingId,
    d.Name AS device_object_name,
    c.Id AS command_row,
    c.CommandId,
    c.CommandMatchingId,
    c.Name AS command_name,
    c.WherePlaceholder,
    c.WhereType,
    c.WhereName,
    c.ChiOpen,
    c.Frame,
    p.Id AS parameter_row,
    p.Placeholder,
    p.Name AS parameter_name,
    p.Min,
    p.Max,
    p.Step,
    p.Type,
    p.OperatorType,
    p.Value
FROM ObjectSystems AS os
JOIN DeviceObjects AS d
  ON d.ObjectSystem_Id = os.Id
JOIN Commands AS c
  ON c.DeviceObject_Id = d.Id
LEFT JOIN Parameters AS p
  ON p.Command_Id = c.Id
WHERE os.Id = :object_system_id
ORDER BY d.Id, c.Id, p.Id;
```

### Reference algorithm

Section ID: `ownkb:section:d000126:s000005`

Uncertainty: `unresolved`
Provenance cues: `evidence`, `source`

```text
function resolve_capabilities(source, requested_context):
    systems = query ObjectSystems compatible with requested_context
    output = []

    for system in systems:
        for object in DeviceObjects where ObjectSystem_Id == system.Id:
            object_match = correlate_only_with_established_mapping(object)

            for command in Commands where DeviceObject_Id == object.Id:
                parameters = Parameters where Command_Id == command.Id

                capability = {
                    source file and row IDs,
                    resource keys,
                    ScenarioDevices IDs,
                    category evidence,
                    stored WHO evidence,
                    address metadata,
                    frame template,
                    parameter definitions
                }

                if command.Frame is a literal OpenWebNet template:
                    capability.rendering = parse_without_substitution(command.Frame)
                else if command.Frame is symbolic:
                    capability.rendering = unresolved symbolic operation
                else:
                    capability.rendering = no stored frame

                validate against functional reference and installed Object context
                output.append(capability with resolution status)

    return output without first-row-wins selection
```

### Category handling

Section ID: `ownkb:section:d000126:s000006`

Cautions: `do not`
Provenance cues: `evidence`

Resource keys commonly end in `.trigger`, `.condition`, or `.action`, and their `CategoryFlag` values form consistent clusters. This is strong implementation evidence, but the draft does not yet declare a universal numeric enumeration for the flags.

Present both:

- the resource-key-derived role;
- the raw `CategoryFlag`.

Do not discard a row solely because its flag is not yet interpreted. See [Categories and Matching](categories-and-matching.md) for the complete observed flag distribution and the evidence supporting the current role names.

### Installed-Device filtering

Section ID: `ownkb:section:d000126:s000007`

Cautions: `do not`
Provenance cues: `database`, `evidence`

The ScenarioDevices files contain no installed Device ID and no direct Module slot. Filtering capabilities for a real installation therefore requires a staged correlation:

1. diagnose the Device and resolve its configured Object;
2. determine the functional system and behavior supported by that Object;
3. correlate that established behavior with ScenarioDevices Object/resource keys;
4. retain ambiguity where `ObjectId` or matching IDs lack a proven mapping.

Do not write a cross-database SQL join equating `DeviceObjects.ObjectId` with `EN_KEY_OBJECT.key_object` unless independent evidence establishes that relationship for the relevant rows.

### Result

Section ID: `ownkb:section:d000126:s000008`

Provenance cues: `database`, `evidence`, `source`

Parameter rows require type-specific handling, especially where several rows share one composite placeholder. See [Parameters](parameters.md).

Return a capability record containing:

- source database and row IDs;
- Object System and Device Object resource keys;
- raw category and matching identifiers;
- Command name and identifiers;
- functional `WHO` evidence;
- address requirements;
- frame classification;
- complete parameter definitions;
- correlations and their evidence level;
- status: resolved, partial, ambiguous, symbolic, or unsupported.

# Document: ownkb:document:d000127

Source path: `scenario-engine/categories-and-matching.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Categories and Matching

Section ID: `ownkb:section:d000127:s000001`

This page documents how ScenarioDevices rows classify scenario roles and correlate related trigger, condition, and action capabilities.

### `CategoryFlag`

Section ID: `ownkb:section:d000127:s000002`

Applicability cues: `revision`
Cautions: `do not`
Provenance cues: `documentation`, `evidence`

In `ScenarioDevices-program-files.sqlite`, the observed distribution is:

| `CategoryFlag` | Object Systems | Resource-key evidence | Working interpretation |
| --- | --- | --- | --- |
| `0` | 8 | `.trigger`, `.start` | first event/trigger role |
| `1` | 8 | `.trigger`, `.stop` | complementary event/trigger role |
| `2` | 5 | `.condition`, `.if` | condition role |
| `3` | 8 | `.action` | action role |

The `programdata` revision has the same five condition and eight action systems, but only seven systems for each of flags `0` and `1` because it lacks the Virtual Key Card family.

The role correlation is exhaustive across the canonical resource keys, so the numeric classification is strong implementation evidence. The precise distinction between flags `0` and `1` is not uniform enough to rename them globally: Alarm, Auxiliaries, Hotel, Lighting, Scheduled Scenarios, Time, and Virtual Key Card reuse the same `.trigger` key for both, while Temperature Control uses `.start` and `.stop`.

Documentation should therefore retain both the raw flag and a contextual role:

- flag `0`: primary/start event category;
- flag `1`: complementary/stop event category;
- flag `2`: condition category;
- flag `3`: action category.

Do not describe flags `0` and `1` as particular wire states without resolving the contained Commands.

### Duplicate Object Systems

Section ID: `ownkb:section:d000127:s000003`

Uncertainty: `not established`

Several Object System resource keys deliberately occur twice with flags `0` and `1`. They are separate rows and have separate Device Objects and Commands even where their names are identical.

The rows preserve distinct categories. Their use to place related events in the scenario editor is inferred from the metadata; actual editor behavior is not established by the duplicate names alone.

### Object matching

Section ID: `ownkb:section:d000127:s000004`

`ObjectMatchingId` is `NULL` for most Device Objects. Non-null values occur in three semantic groups:

| Matching ID | Related Object concepts | Rows |
| --- | --- | --- |
| `1` | Lighting Light trigger/action | 3 |
| `2` | Lighting Dimmer trigger/action | 3 |
| `13` | Hotel Room trigger/action | 3 |

The three rows per group span the two event categories and the action category. This strongly supports the interpretation that `ObjectMatchingId` correlates compatible concepts across scenario roles.

It does not prove a relationship with `MHCatalogue.db`, and the matching ID is not a Device Object primary key.

### Command matching

Section ID: `ownkb:section:d000127:s000005`

Provenance cues: `evidence`

Non-null `CommandMatchingId` values likewise correlate cross-role semantics:

| Matching IDs | Area | Evidence |
| --- | --- | --- |
| `1`, `2` | Lighting Light | off/on trigger rows and off/on action rows |
| `3`, `4` | Lighting Dimmer | off/on trigger rows and dimmer off/on action rows |
| `56..59` | Hotel Room | DND and MUR trigger/action concepts |

For Light commands, `CommandId` and `CommandMatchingId` can be equal. For Dimmer and Hotel actions they differ. Therefore:

- `CommandId` identifies the command within the ScenarioDevices command namespace;
- `CommandMatchingId` links a semantic event/action concept across roles;
- equality between them is incidental for some rows, not a general rule.

### Relationship inspection

Section ID: `ownkb:section:d000127:s000006`

The following relationship query is useful because it shows the parent roles on both sides of a matching group:

```sql
SELECT
    d.ObjectMatchingId,
    c.CommandMatchingId,
    os.CategoryFlag,
    os.Name AS system_name,
    d.ObjectId,
    d.Name AS object_name,
    c.CommandId,
    c.Name AS command_name,
    c.Frame
FROM ObjectSystems AS os
JOIN DeviceObjects AS d ON d.ObjectSystem_Id = os.Id
JOIN Commands AS c ON c.DeviceObject_Id = d.Id
WHERE d.ObjectMatchingId IS NOT NULL
   OR c.CommandMatchingId IS NOT NULL
ORDER BY d.ObjectMatchingId, c.CommandMatchingId, os.CategoryFlag;
```

### Matching algorithm

Section ID: `ownkb:section:d000127:s000007`

Provenance cues: `source`

The following is a proposed inspection algorithm for finding metadata counterparts, not recovered MyHOME Suite code or an established runtime matching contract. The preference for equal `ObjectMatchingId` is an analysis policy.

```text
function find_semantic_counterparts(source_command):
    require source_command has CommandMatchingId

    candidates = Commands with the same CommandMatchingId
    candidates = candidates joined to their Device Object and Object System

    if source Device Object has ObjectMatchingId:
        prefer candidates whose Device Object has the same ObjectMatchingId

    group by CategoryFlag and preserve all rows
    return trigger/condition/action counterparts with frames and provenance
```

Matching can support editor navigation or trigger/action correlation. It does not by itself define runtime execution, event subscription, or a reversible wire mapping.

# Document: ownkb:document:d000128

Source path: `scenario-engine/database-model.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Database Model

Section ID: `ownkb:section:d000128:s000001`

The ScenarioDevices databases are compact SQLite capability catalogues used by the MyHOME_Suite scenario editor. They describe available scenario Objects and commands; they are not databases of user-authored scenario instances.

### Source files

Section ID: `ownkb:section:d000128:s000002`

Applicability cues: `revision`
Uncertainty: `not established`
Provenance cues: `database`

| File | Role established by content |
| --- | --- |
| `ScenarioDevices-program-files.sqlite` | larger capability set and the only revision with `ObjectSystems.FamilyId` |
| `ScenarioDevices-programdata.sqlite` | closely related capability set without `FamilyId` |

The repository filenames record their original installation locations: the larger file came from `Program Files (x86)`, while the smaller file came from the shared `ProgramData` database directory. The precise application selection, synchronization, or precedence rule is not established.

### Tables

Section ID: `ownkb:section:d000128:s000003`

#### `ObjectSystems`

Section ID: `ownkb:section:d000128:s000004`

Groups Device Objects into named functional/category contexts.

| Column | Notes |
| --- | --- |
| `Id` | local primary key |
| `FamilyId` | present only in `program-files`; consistently groups category rows into one local functional family |
| `Name` | localization/resource key such as `miniScenarioSuite.automation.action` |
| `CategoryFlag` | implementation-derived role category: primary/start event, complementary/stop event, condition, or action |

#### Observed `FamilyId` grouping

Section ID: `ownkb:section:d000128:s000005`

Uncertainty: `appears`
Provenance cues: `catalogue`, `database`

`FamilyId` appears only in the Program Files copy and consistently groups all category rows for one resource-key functional family:

| `FamilyId` | Resource-key family |
| --- | --- |
| `1` | Alarm |
| `2` | Automation |
| `3` | Auxiliaries |
| `4` | Delay |
| `5` | Hotel |
| `6` | Lighting |
| `7` | Scenarios |
| `8` | Scheduled Scenarios |
| `9` | Special Commands |
| `10` | Temperature Control |
| `11` | Time |
| `12` | Virtual Key Card |

This establishes `FamilyId` as a local scenario-editor family grouping. It does not establish equality with a functional `WHO`, `OPEN.db` system ID, catalogue family ID, or any other database namespace.

#### `DeviceObjects`

Section ID: `ownkb:section:d000128:s000006`

Uncertainty: `unresolved`
Provenance cues: `source`

| Column | Notes |
| --- | --- |
| `Id` | local primary key |
| `ObjectId` | scenario-engine Object identifier; not proven equal to `EN_KEY_OBJECT.key_object` |
| `ObjectMatchingId` | optional matching identifier with unresolved cross-source semantics |
| `Name` | localization/resource key |
| `ObjectSystem_Id` | declared foreign key to `ObjectSystems.Id` |

#### `Commands`

Section ID: `ownkb:section:d000128:s000007`

Provenance cues: `evidence`

| Column | Notes |
| --- | --- |
| `Id` | local primary key |
| `CommandId` | scenario-engine command identifier |
| `CommandMatchingId` | optional matching identifier |
| `Name` | localization/resource key |
| `WherePlaceholder` | address placeholder where present |
| `WhereType` | numeric address-type discriminator |
| `WhereName` | localization/resource key for the address field |
| `ChiOpen` | stored functional `WHO` evidence where present |
| `Frame` | literal or symbolic frame template; can be `NULL` |
| `DeviceObject_Id` | declared foreign key to `DeviceObjects.Id` |

#### `Parameters`

Section ID: `ownkb:section:d000128:s000008`

| Column | Notes |
| --- | --- |
| `Id` | local primary key |
| `Min`, `Max`, `Step` | numeric-domain metadata where applicable |
| `Placeholder` | text substituted into a frame or interpreted by the application |
| `Name` | localization/resource key |
| `OperatorType` | numeric operator discriminator |
| `Value` | stored constant or selector value where present |
| `Type` | numeric parameter-type discriminator |
| `Command_Id` | declared foreign key to `Commands.Id` |

### Declared relationships

Section ID: `ownkb:section:d000128:s000009`

Cautions: `do not`

```sql
SELECT
    os.Id AS object_system_row,
    os.Name AS object_system_name,
    os.CategoryFlag,
    d.Id AS device_object_row,
    d.ObjectId,
    d.ObjectMatchingId,
    d.Name AS device_object_name,
    c.Id AS command_row,
    c.CommandId,
    c.CommandMatchingId,
    c.Name AS command_name,
    c.ChiOpen,
    c.Frame,
    p.Id AS parameter_row,
    p.Placeholder,
    p.Min,
    p.Max,
    p.Step,
    p.Type,
    p.OperatorType,
    p.Value
FROM ObjectSystems AS os
JOIN DeviceObjects AS d
  ON d.ObjectSystem_Id = os.Id
JOIN Commands AS c
  ON c.DeviceObject_Id = d.Id
LEFT JOIN Parameters AS p
  ON p.Command_Id = c.Id
ORDER BY os.Id, d.Id, c.Id, p.Id;
```

Use the row primary keys for joins inside one file. Do not join the two files by `Id`: corresponding semantic rows can have different local identities or be absent.

### Compare the revisions

Section ID: `ownkb:section:d000128:s000010`

Provenance cues: `database`

Attach both files and compare a Command by its full hierarchy rather than local IDs or `Commands.Name` alone:

```sql
ATTACH DATABASE 'ScenarioDevices-program-files.sqlite' AS files_db;
ATTACH DATABASE 'ScenarioDevices-programdata.sqlite' AS data_db;

WITH files_commands AS (
    SELECT
        os.Name AS system_name,
        os.CategoryFlag,
        d.Name AS object_name,
        d.ObjectId,
        d.ObjectMatchingId,
        c.Name AS command_name,
        c.CommandId,
        c.CommandMatchingId,
        c.WherePlaceholder,
        c.WhereType,
        c.WhereName,
        c.ChiOpen,
        c.Frame
    FROM files_db.ObjectSystems AS os
    JOIN files_db.DeviceObjects AS d ON d.ObjectSystem_Id = os.Id
    JOIN files_db.Commands AS c ON c.DeviceObject_Id = d.Id
),
data_commands AS (
    SELECT
        os.Name AS system_name,
        os.CategoryFlag,
        d.Name AS object_name,
        d.ObjectId,
        d.ObjectMatchingId,
        c.Name AS command_name,
        c.CommandId,
        c.CommandMatchingId,
        c.WherePlaceholder,
        c.WhereType,
        c.WhereName,
        c.ChiOpen,
        c.Frame
    FROM data_db.ObjectSystems AS os
    JOIN data_db.DeviceObjects AS d ON d.ObjectSystem_Id = os.Id
    JOIN data_db.Commands AS c ON c.DeviceObject_Id = d.Id
)
SELECT f.*
FROM files_commands AS f
LEFT JOIN data_commands AS d
  ON d.system_name = f.system_name
 AND d.CategoryFlag = f.CategoryFlag
 AND d.object_name = f.object_name
 AND d.command_name = f.command_name
WHERE d.command_name IS NULL
   OR d.ObjectId IS NOT f.ObjectId
   OR d.ObjectMatchingId IS NOT f.ObjectMatchingId
   OR d.CommandId IS NOT f.CommandId
   OR d.CommandMatchingId IS NOT f.CommandMatchingId
   OR d.WherePlaceholder IS NOT f.WherePlaceholder
   OR d.WhereType IS NOT f.WhereType
   OR d.WhereName IS NOT f.WhereName
   OR d.ChiOpen IS NOT f.ChiOpen
   OR d.Frame IS NOT f.Frame
ORDER BY f.system_name, f.CategoryFlag, f.object_name, f.command_name;
```

The canonical comparison shows that the semantic rows in `programdata` are an exact subset of `program-files` when the full parent path and non-local fields are used. The six additional Commands are four Virtual Key Card event rows and the Temperature Control local-control and fan-coil-speed actions. The latter two have one additional Parameter each.

`Commands.Name` alone is unsafe as a comparison key because the same resource key can occur beneath primary and complementary event categories.

### Integrity checks

Section ID: `ownkb:section:d000128:s000011`

Provenance cues: `database`

```sql
PRAGMA foreign_key_check;

SELECT c.Id, c.Name
FROM Commands AS c
LEFT JOIN DeviceObjects AS d ON d.Id = c.DeviceObject_Id
WHERE d.Id IS NULL;

SELECT p.Id, p.Name
FROM Parameters AS p
LEFT JOIN Commands AS c ON c.Id = p.Command_Id
WHERE c.Id IS NULL;
```

The canonical files declare the three hierarchy foreign keys. Application-level identifiers and cross-database correlations remain outside those constraints.

# Document: ownkb:document:d000129

Source path: `scenario-engine/execution-model.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Execution Model

Section ID: `ownkb:section:d000129:s000001`

Provenance cues: `evidence`

The ScenarioDevices databases define editor capabilities, not a complete runtime state machine. This page separates the execution behavior that can be derived from stored templates from behavior that requires other evidence.

### Established pipeline

Section ID: `ownkb:section:d000129:s000002`

Applicability cues: `gateway`
Provenance cues: `evidence`

For an action with a literal OpenWebNet template, a safe application can:

1. resolve the selected Object System, Device Object, Command, and Parameters;
2. confirm the Command belongs to an action category;
3. resolve the target installed Device/Module using diagnostics and the Device Model;
4. validate the target functional address under the stored or parsed `WHO`;
5. validate and encode every Parameter;
6. render and reparse the complete frame;
7. send it through the appropriate command session, authenticated where the selected gateway requires it;
8. collect acknowledgement and functional state evidence where applicable;
9. record the action result independently from the scenario's future control flow.

Steps 1 through 6 are partly represented by ScenarioDevices. Transport/session behavior, acknowledgements, retries, scheduling, and state persistence are not defined by these tables.

### Trigger and condition model

Section ID: `ownkb:section:d000129:s000003`

Provenance cues: `database`, `evidence`

Event and condition Commands commonly have `Frame=NULL`. Their resource keys, category, IDs, matching IDs, address metadata, and Parameters still describe editor concepts, but the database does not directly provide a complete incoming-frame matcher.

Possible runtime inputs include:

- an event decoded elsewhere and identified by `CommandId`;
- application code mapping functional frames to Commands;
- a separate persistence or capability layer;
- matching identifiers linking incoming concepts with actions;
- non-bus events such as time, delay, or Virtual Key Card activity.

The current evidence does not select one universal mechanism.

### Matching semantics

Section ID: `ownkb:section:d000129:s000004`

Provenance cues: `database`

`ObjectMatchingId` and `CommandMatchingId` demonstrably group related lighting and hotel concepts across category rows. A runtime or editor can use this relationship to find semantic counterparts, but the database does not specify whether matching is used for:

- event subscription;
- condition evaluation;
- suggested action selection;
- display grouping;
- serialization compatibility.

Document the grouping; keep the runtime purpose provisional.

### Scenario graph boundary

Section ID: `ownkb:section:d000129:s000005`

Provenance cues: `catalogue`, `evidence`

The four ScenarioDevices tables contain no identified scenario-instance, node, edge, ordering, branch, schedule, or execution-history model. The inspected schemas and contents establish a capability catalogue, not a recovered persistence format for user-authored scenario graphs. This bounded finding does not prove where the application stores graphs or exclude an unexamined serialization mechanism.

A complete engine model still needs evidence for:

| Concern | Missing evidence |
| --- | --- |
| scenario identity | instance table or file format |
| graph structure | nodes, edges, branches, ordering |
| trigger bindings | mapping from runtime events to stored Commands |
| condition state | evaluation operands and persistence |
| action ordering | serial, parallel, delayed, or transactional behavior |
| error policy | retry, continue, abort, compensation |
| scheduling | clocks, recurrence, timezone, missed-event handling |
| runtime state | active executions and recovery after restart |

### Action execution algorithm

Section ID: `ownkb:section:d000129:s000006`

Cautions: `do not`

```text
function execute_literal_action(capability, target, inputs):
    require capability category is action
    require capability Frame is literal OpenWebNet syntax

    address = resolve target under functional WHO grammar
    parameters = validate and encode all capability Parameters
    frame = render placeholders atomically
    parsed = parse rendered frame

    require parsed WHO agrees with established capability context
    require parsed WHERE agrees with selected target
    require no placeholder remains

    send frame through the appropriate command transport
    collect ACK/NACK and applicable state feedback

    return transmitted frame, raw responses, and classified result
```

Do not generalize this action algorithm to triggers, conditions, symbolic frames, delay rows, or time-based rows.

### Result classification

Section ID: `ownkb:section:d000129:s000007`

Uncertainty: `unresolved`
Provenance cues: `evidence`

| Result | Meaning |
| --- | --- |
| rendered | a complete frame was produced and validated, but not sent |
| transmitted | transport accepted the outgoing bytes; Device effect not yet proven |
| acknowledged | an applicable positive acknowledgement was received |
| rejected | `NACK` or another explicit rejection was received |
| observed effective | later functional state evidence matches the intended action |
| timeout | no terminal evidence arrived within the applicable window |
| indeterminate | transport loss or ambiguous feedback prevents a conclusion |
| unresolved capability | template, address, Parameter, or symbolic mapping was insufficient |

An acknowledgement and an observed state change answer different questions and should not be collapsed into one success flag.

### Relationship to `OPEN.db`

Section ID: `ownkb:section:d000129:s000008`

Cautions: `do not`
Provenance cues: `documentation`

`OPEN.db` describes MyHOME_Suite communication scenarios for diagnostics and Device programming. It does not define the Scenario Engine graph or replace the functional meanings of ScenarioDevices action frames.

Use the common OpenWebNet session documentation for transport behavior and the functional `WHO` pages for command semantics. Do not search for ScenarioDevices row IDs in `OPEN.db` unless a separate mapping is established.

# Document: ownkb:document:d000130

Source path: `scenario-engine/frame-templates.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Frame Templates

Section ID: `ownkb:section:d000130:s000001`

`Commands.Frame` stores either a literal OpenWebNet template, a symbolic operation, or no frame. Rendering must therefore begin with classification rather than unconditional string replacement.

### Command fields

Section ID: `ownkb:section:d000130:s000002`

Provenance cues: `evidence`

| Field | Use |
| --- | --- |
| `Frame` | literal or symbolic command representation |
| `ChiOpen` | stored functional `WHO` evidence |
| `WherePlaceholder` | token representing the destination where present |
| `WhereType` | raw address-type discriminator |
| `WhereName` | address-field resource key |
| `Name` | command resource key and semantic evidence |

### Template classes

Section ID: `ownkb:section:d000130:s000003`

#### Literal OpenWebNet frame

Section ID: `ownkb:section:d000130:s000004`

Example stored value:

`*2*1*WHERE##`

This can be parsed as a functional command template. The `WHERE` token still requires the `WHO 2` address grammar and an independently selected destination.

#### Literal frame with parameter placeholders

Section ID: `ownkb:section:d000130:s000005`

A frame can contain tokens also described by `Parameters.Placeholder`. Each placeholder must be resolved from the Parameter row and validated before substitution.

#### Symbolic operation

Section ID: `ownkb:section:d000130:s000006`

Provenance cues: `source`

Example pattern:

`ResetSOS[WHERE]`

This is not a complete OpenWebNet frame. It requires an application mapping or another source before it can be transmitted.

#### Missing frame

Section ID: `ownkb:section:d000130:s000007`

Provenance cues: `database`

A `NULL` frame does not prove that the capability is non-executable. It proves only that this database row does not contain a renderable frame template.

### Safe rendering algorithm

Section ID: `ownkb:section:d000130:s000008`

Cautions: `do not`
Uncertainty: `unresolved`

```text
function render(command, selected_where, supplied_values):
    if command.Frame is NULL:
        return unresolved("no stored frame")

    if command.Frame is not syntactically an OpenWebNet template:
        return unresolved("symbolic operation")

    parsed = parse frame structure before substitution

    if command.ChiOpen is present:
        require parsed WHO agrees with established ChiOpen interpretation

    if command.WherePlaceholder is present:
        validate selected_where using the parsed WHO address grammar
        replace only the complete declared WHERE token
    else if selected_where was supplied:
        reject unused input

    groups = resolve_parameters(command), grouped by complete placeholder
    for group in groups:
        if group has no placeholder:
            retain it as editor metadata; do not substitute it
            continue
        values = supplied values or established stored constants
        validate each component using its interpreted type and domain
        encode the complete group using the established scalar/composite rule
        replace the declared placeholder once
        reject the group if its component order or encoding is unresolved

    require no unresolved placeholder remains
    serialize and parse the result again
    require serialized frame has the expected WHO and frame family

    return rendered frame plus full substitution provenance
```

### Numeric-domain validation

Section ID: `ownkb:section:d000130:s000009`

For a numeric Parameter with established numeric semantics:

```text
valid = (Min is absent or value >= Min)
    and (Max is absent or value <= Max)
    and (
        Step is absent
        or Step is zero
        or (Min is present and (value - Min) modulo Step == 0)
    )
```

If `Step` is present but `Min` is absent, this row does not establish the step-grid origin. This rule applies only after `Type` and the placeholder have been shown to represent a numeric scalar. Some parameters encode composite values such as time components and cannot be validated as one scalar range. See [Parameters](parameters.md) for the observed type and operator domains and the composite-placeholder cases.

### Security and correctness rules

Section ID: `ownkb:section:d000130:s000010`

Cautions: `do not`
Uncertainty: `contradictory`, `unresolved`
Provenance cues: `evidence`, `source`

- Never substitute unvalidated text directly into a frame.
- Match complete placeholders, not substrings.
- Reject values containing frame delimiters unless the parameter grammar explicitly requires them.
- Reparse the rendered frame before transmission.
- Validate `WHERE` under the functional `WHO`; `WhereType` alone is not a complete address grammar.
- Treat `ChiOpen` as source evidence, not permission to overwrite a contradictory literal frame.
- Preserve the stored template and rendered result together.
- Do not transmit symbolic or unresolved templates.

### Example

Section ID: `ownkb:section:d000130:s000011`

For the stored automation action:

```text
ChiOpen = 2
Frame = *2*1*WHERE##
WherePlaceholder = WHERE
```

and an independently validated `WHO 2` destination `11`, rendering produces:

`*2*1*11##`

The resulting `WHAT 1` and `WHERE 11` semantics must still be read from the [`WHO 2` functional reference](../functional/who-2-automation/). The ScenarioDevices row establishes the template offered by MyHOME_Suite; it does not replace the protocol definition.

See [Execution Model](execution-model.md) for the boundary between rendering an action frame and executing a complete scenario.

# Document: ownkb:document:d000131

Source path: `scenario-engine/functional-correlations.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Functional Correlations

Section ID: `ownkb:section:d000131:s000001`

Provenance cues: `evidence`

Literal ScenarioDevices frames provide direct implementation evidence for functional OpenWebNet operations offered by the MyHOME_Suite scenario editor.

Across `ScenarioDevices-program-files.sqlite`, 57 Commands contain OpenWebNet-shaped templates. Every one has a non-null `ChiOpen`, and the parsed frame `WHO` agrees with `ChiOpen` in all 57 rows.

### Explicit functional coverage

Section ID: `ownkb:section:d000131:s000002`

| `WHO` | Literal templates | Scenario editor coverage |
| --- | --- | --- |
| `0` | 1 | scenario-module action |
| `1` | 17 | Lighting, timed Lighting, dimming, controlled socket, fan, and an Object-contextual door-lock action |
| `2` | 18 | shutter, curtain, advanced positioning, and movement actions |
| `4` | 19 | Temperature Control modes, protection, setpoint, local control, and fan-coil speed |
| `14` | 2 | actuator lock and unlock |

`ChiOpen=2` occurs on 19 Commands because the Delay action also stores `2` while its `Frame` is `NULL`. It is not included among the 18 literal `WHO 2` templates.

### `WHO 0`: scenario action

Section ID: `ownkb:section:d000131:s000003`

The Scenario action row stores:

`*0*N*WHERE##`

The Parameter row supplies placeholder `N` with numeric metadata. Interpret `N` and `WHERE` through the [`WHO 0` reference](../functional/who-0-scenarios/) rather than treating the ScenarioDevices numeric metadata as a complete protocol grammar.

### `WHO 1`: target-dependent editor semantics

Section ID: `ownkb:section:d000131:s000004`

Provenance cues: `database`

ScenarioDevices stores ordinary Lighting actions such as:

- `*1*0*WHERE##` - OFF;
- `*1*1*WHERE##` - ON;
- `WHAT 11..16` using `*1*WHAT*WHERE##` - fixed timed actions;
- `*#1*WHERE*#2*ora*min*sec##` - parameterized timed action;
- `*#1*WHERE*#1*liv*v##` - 100-level dimming action.

It also labels `*1*17*WHERE##` as `automation.actionAutomationDoorLock.on`. Public `WHO 1` semantics still apply at the wire level; the door-lock label is an Object-contextual MyHOME_Suite presentation. This demonstrates that user-facing meaning can depend on the target Object as well as `WHO` and `WHAT`.

See the [`WHO 1` reference](../functional/who-1-lighting/) and [cross-database functional coverage](../functional/cross-database-coverage.md).

### `WHO 2`: Automation

Section ID: `ownkb:section:d000131:s000005`

The templates cover:

- UP, DOWN, and STOP;
- absolute position through `DIMENSION 11`;
- advanced movement with a step parameter;
- advanced STOP;
- step-by-step movement.

Shutter and Curtain editor Objects can emit identical wire templates with different user-facing labels. Preserve the selected Object context while decoding the frame through the [`WHO 2` reference](../functional/who-2-automation/).

### `WHO 4`: Temperature Control

Section ID: `ownkb:section:d000131:s000006`

Applicability cues: `revision`
Provenance cues: `evidence`

ScenarioDevices supplies implementation templates using functional Dimensions:

| Function | Template form |
| --- | --- |
| comfort/eco/protection modes | `*#4*ZAZB*#7*[MODE]*[FUNCTION]*##` |
| setpoint | `*#4*ZAZB*#7*[MODE]*1*c1c2c3c4##` |
| OFF | `*#4*ZAZB*#7*0*5*##` |
| local control | `*#4*ZAZB*#5*val##` |
| fan-coil speed | `*#4*ZAZB*#11*val##` |

The exact stored rows distinguish Heat, Cool, Auto, and Generic modes and Comfort, Eco, Protection, Setpoint, and OFF functions. The semantic-to-wire conversion for `c1c2c3c4` and the enumeration of `val` require the [`WHO 4` reference](../functional/who-4-temperature-control/) or additional application evidence.

The local-control and fan-coil-speed rows exist only in the Program Files revision.

### `WHO 14`: actuator lock and unlock

Section ID: `ownkb:section:d000131:s000007`

Provenance cues: `evidence`

ScenarioDevices provides direct labels for two otherwise sparsely documented operations:

| Resource-key command | Frame | Implementation meaning |
| --- | --- | --- |
| `.lock` | `*14*0*WHERE##` | lock actuator |
| `.unlock` | `*14*1*WHERE##` | unlock actuator |

This is MyHOME_Suite implementation evidence scoped to the Lock/Unlock Actuator Object. See the [`WHO 14` reference](../functional/who-14-special-commands/).

### Symbolic capabilities

Section ID: `ownkb:section:d000131:s000008`

Five non-null frames are not OpenWebNet frame strings:

- `ResetSOS[WHERE]`;
- `DND ON` and `DND OFF`;
- `MUR ON` and `MUR OFF`.

These values establish named internal operations, not complete wire frames. No `WHO` should be manufactured from them.

### Frame-absent capabilities

Section ID: `ownkb:section:d000131:s000009`

Cautions: `do not`
Provenance cues: `evidence`, `source`

Ninety-five Commands have `Frame=NULL`, including most triggers and conditions, CEN/CEN+ events, time capabilities, Virtual Key Card events, and the Delay action.

Their resource keys and Parameters are useful application evidence. They do not establish an incoming or outgoing OpenWebNet frame without another source.

### Cross-source rule

Section ID: `ownkb:section:d000131:s000010`

Provenance cues: `database`

ScenarioDevices can enrich a protocol frame with editor Object/command context. It cannot override the functional protocol grammar, prove Device applicability, or establish a cross-database Object join by numeric coincidence.

# Document: ownkb:document:d000132

Source path: `scenario-engine/open-questions.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Open Questions

Section ID: `ownkb:section:d000132:s000001`

Provenance cues: `documentation`

This page records Scenario Engine semantics that are not yet established strongly enough for normative documentation.

### Database selection

Section ID: `ownkb:section:d000132:s000002`

- Which application workflow opens `ScenarioDevices-program-files.sqlite`?
- Which workflow opens `ScenarioDevices-programdata.sqlite`?
- Are they product variants, generated and packaged revisions, or inputs to different MyHOME_Suite components?
- When both are available, which file takes precedence?

### Category and family fields

Section ID: `ownkb:section:d000132:s000003`

Cautions: `do not`
Provenance cues: `database`, `source`

- Confirm the application's own labels for `CategoryFlag 0` and `1`; the data establishes primary/start and complementary/stop event categories, but not one universal public name.
- The local editor-family grouping of `FamilyId` is established in [Database Model](database-model.md). Determine whether application code defines any additional cross-source mapping; equal values alone do not establish one.
- Confirm the runtime/editor purpose of the established primary/complementary category pairs that share a resource key.

### Matching identifiers

Section ID: `ownkb:section:d000132:s000004`

- Establish the purpose of `ObjectMatchingId` and `CommandMatchingId`.
- Determine how the application uses the established cross-role matching groups at runtime or in the editor: event binding, suggested actions, display grouping, serialization, or another purpose.
- Test whether matching identifiers are local to one file or stable across both revisions.

### Object identifiers

Section ID: `ownkb:section:d000132:s000005`

Cautions: `do not`
Provenance cues: `catalogue`, `evidence`

- Determine whether `DeviceObjects.ObjectId` maps to ScenarioDevices-only concepts, catalogue Objects, public protocol constructs, or a mixture.
- Do not infer equality with `EN_KEY_OBJECT.key_object` from numeric coincidence.
- Identify which installed Device/Object evidence MyHOME_Suite uses to filter the scenario editor's Object list.

### Command identifiers

Section ID: `ownkb:section:d000132:s000006`

Provenance cues: `source`

- Determine the namespace and stability of `Commands.CommandId`.
- Establish whether equal `CommandId` values under different Objects mean semantic equivalence.
- Correlate commands with the functional `WHAT` or `DIMENSION` reference only where the stored frame or independent source supports it.

### Address metadata

Section ID: `ownkb:section:d000132:s000007`

- Enumerate `WhereType` semantics.
- Establish how `WherePlaceholder` and `WhereName` interact with system-specific address editors.
- Determine how virtual, group, general, and multi-level addresses are represented.

### Parameter metadata

Section ID: `ownkb:section:d000132:s000008`

- Enumerate parameter `Type` values.
- Enumerate `OperatorType` values and their relationship to triggers and conditions.
- Determine when `Value` is a default, fixed selector, comparison operator operand, or enumeration key.
- Document composite placeholders whose grammar cannot be expressed by `Min`, `Max`, and `Step` alone.

### Symbolic and missing frames

Section ID: `ownkb:section:d000132:s000009`

Provenance cues: `database`

- Locate the application mapping for symbolic values such as `ResetSOS[WHERE]`.
- Determine why some trigger/condition rows have no stored frame.
- Establish whether missing frames are matched against incoming events by IDs, by another database, or by application code.

### Execution model

Section ID: `ownkb:section:d000132:s000010`

Cautions: `do not`

The databases describe capabilities but do not obviously store complete user-authored scenario graphs. Further work should identify:

- where scenario instances are persisted;
- how triggers, conditions, and actions are ordered;
- how delays, timers, and branching are represented;
- how incoming frames are matched to triggers;
- how actions are scheduled and errors handled;
- whether the engine retries, serializes, or parallelizes actions.

### Investigation method

Section ID: `ownkb:section:d000132:s000011`

Uncertainty: `hypothesis`
Provenance cues: `evidence`

For each hypothesis:

1. query both ScenarioDevices revisions;
2. preserve file and row provenance;
3. compare resource keys, parents, frames, and parameters;
4. correlate with the functional protocol reference;
5. inspect other preserved MyHOME_Suite support files where available;
6. compare with observed UI behavior or execution;
7. record counterexamples;
8. promote the interpretation only when it explains all relevant rows.

Implementation labels are evidence, not automatically public protocol terminology.

# Document: ownkb:document:d000133

Source path: `scenario-engine/parameters.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Parameters

Section ID: `ownkb:section:d000133:s000001`

Applicability cues: `revision`

`Parameters` describes additional values needed by a Command or by the scenario editor. A Command has zero, one, or two Parameter rows in the canonical `program-files` revision.

| Parameters per Command | Commands |
| --- | --- |
| 0 | 116 |
| 1 | 40 |
| 2 | 1 |

The two-parameter Command is a lighting dimmer action whose shared placeholder encodes both level and transition time.

### Field model

Section ID: `ownkb:section:d000133:s000002`

| Field | Established role | Interpretation limit |
| --- | --- | --- |
| `Id` | local row primary key | not stable across databases by declaration |
| `Command_Id` | foreign key to `Commands.Id` | local to one file |
| `Name` | localization/resource key | not necessarily unique |
| `Placeholder` | token or composite pattern used by the command/application | can be `NULL` |
| `Min`, `Max` | stored numeric bounds | meaningful only after type interpretation |
| `Step` | stored increment | not sufficient for composite values |
| `Type` | parameter editor/value-type discriminator | numeric enumeration is not published |
| `OperatorType` | operator/editor discriminator | numeric enumeration is not published |
| `Value` | stored fixed or selector value | role depends on the Parameter context |

### Observed `Type` values

Section ID: `ownkb:section:d000133:s000003`

Provenance cues: `evidence`

| Type | Rows in `program-files` | Observed contexts | Evidence-based description |
| --- | --- | --- | --- |
| `1` | 3 | time and time-range conditions | time-oriented editor/value |
| `2` | 24 | shutter levels, steps, scenario numbers, lighting level | numeric scalar |
| `3` | 4 | Temperature Control setpoints | temperature value with `0.5` step |
| `4` | 3 | time and date | time/date editor/value |
| `5` | 3 | time and days of week | time/weekday editor/value |
| `6` | 2 | dimmer level and transition value sharing `liv*v` | composite dimmer value component |
| `7` | 1 | timed-light `ora*min*sec` | composite duration |
| `8` | 1 | Temperature Control local-control enabling | enumeration or specialized selector; only in `program-files` |
| `9` | 1 | fan-coil speed | enumeration or specialized selector; only in `program-files` |

These descriptions are derived from resource keys and value shapes. Retain the numeric Type in machine-readable output.

### Observed `OperatorType` values

Section ID: `ownkb:section:d000133:s000004`

| Operator type | Rows | Observed context | Working interpretation |
| --- | --- | --- | --- |
| `0` | 38 | ordinary values and action parameters | direct/single-value editor |
| `1` | 1 | lighting dimmer condition with stored `Value=1` | condition-specific operator/value selector |
| `2` | 3 | time-range conditions | range-oriented editor |

The names above are working descriptions, not a published enumeration.

### Scalar validation

Section ID: `ownkb:section:d000133:s000005`

Cautions: `do not`

For a Parameter proven to be a numeric scalar:

```text
require Min is absent or value >= Min
require Max is absent or value <= Max
if Step is present and non-zero and Min is present:
    require (value - Min) / Step is integral within numeric tolerance
else if Step is present but Min is absent:
    do not infer the step-grid origin from this row alone
```

Do not apply that algorithm to composite Types `6` or `7`, or to time/date structures, without first expanding their grammar.

### Composite placeholders

Section ID: `ownkb:section:d000133:s000006`

#### `liv*v`

Section ID: `ownkb:section:d000133:s000007`

Two Parameter rows can target the same placeholder:

- level: `1..100`, step `1`;
- transition/time component: `1..254`, step `1`.

The placeholder contains an internal delimiter and represents a composite encoded field. Rendering must combine the two validated components according to the functional frame grammar; replacing the same token twice is incorrect.

#### `ora*min*sec`

Section ID: `ownkb:section:d000133:s000008`

This placeholder describes multiple duration components. `Min`, `Max`, and `Step` are absent, so the ScenarioDevices row alone does not define each component's domain.

#### `c1c2c3c4`

Section ID: `ownkb:section:d000133:s000009`

Temperature setpoint actions use a `3..40` semantic range with step `0.5`, while the placeholder name suggests a fixed encoded representation. The conversion from temperature to the four-character wire field must come from the functional Temperature Control definition or corroborated application behavior.

### Stored `Value` evidence

Section ID: `ownkb:section:d000133:s000010`

Seventeen Parameter rows have a non-null `Value`, and every stored value is the text `1`:

- one Lighting dimmer condition Parameter with `OperatorType=1`;
- sixteen CEN/CEN+ event Parameters across the two event categories.

The CEN/CEN+ rows also provide button-number domains: one CEN start-pressure form allows `0..99`, while the other CEN and CEN+ forms allow `0..31`.

The repeated `1` is implementation data, but the column is not declared as a default-value field. Preserve it as a stored selector/value until UI or runtime behavior establishes whether it is a default, comparison operand, or another editor setting.

### Parameters without placeholders

Section ID: `ownkb:section:d000133:s000011`

A `NULL` Placeholder can still describe editor state, comparison criteria, time structures, or fixed selections. Such Parameters are not automatically unused and should not be discarded.

### Resolution algorithm

Section ID: `ownkb:section:d000133:s000012`

Uncertainty: `unresolved`
Provenance cues: `evidence`

```text
function resolve_parameters(command):
    rows = Parameters for command ordered by Id
    group rows by Placeholder, keeping NULL rows separate

    for group in rows:
        classify Type and OperatorType only from established evidence

        if one scalar row targets one placeholder:
            build scalar domain from Min, Max, Step
        else if several rows target one placeholder:
            require an established composite encoding rule
        else if placeholder is NULL:
            retain as application/editor metadata

        attach stored Value without assuming it is a default

    return typed parameter model plus unresolved semantics
```

### Revision differences

Section ID: `ownkb:section:d000133:s000013`

`programdata` lacks Types `8` and `9` because it lacks the local-control and fan-coil-speed Commands and their Parameters. The common Types and rows otherwise substantially overlap, but correspondence should be checked by parent Command and resource key rather than primary key alone.

# Document: ownkb:document:d000134

Source path: `scenario-engine/sources-and-identifiers.md`
Namespace context: `contextual`
Area: `scenario-engine`

## Sources and Identifier Boundaries

Section ID: `ownkb:section:d000134:s000001`

Provenance cues: `source`

This section is derived from preserved MyHOME_Suite 3.5.38 sources and the repository's functional OpenWebNet reference. Each source establishes a different layer.

### Canonical ScenarioDevices files

Section ID: `ownkb:section:d000134:s000002`

Both repository files were originally named `ScenarioDevices.sqlite`; the repository names distinguish their installation locations.

| Repository file | Original installation path | SHA-256 |
| --- | --- | --- |
| `ScenarioDevices-program-files.sqlite` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\ScenarioDevices.sqlite` | `2ce7ffe1286c3246271aed160116fe664407d9e8ff43595f50192e7d2ac85569` |
| `ScenarioDevices-programdata.sqlite` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_ScenarioDevices\ScenarioDevices.sqlite` | `cd3b9b67160f468cdbd30134357b8733c696aacd5d625129240dff6b79224fc3` |

The fingerprints match [`sources/manifest.yaml`](../sources/manifest.yaml). The paths establish packaging location, not precedence or runtime selection behavior.

### Evidence roles

Section ID: `ownkb:section:d000134:s000003`

Applicability cues: `firmware`
Provenance cues: `database`, `source`

| Source | What it establishes | What it does not establish alone |
| --- | --- | --- |
| ScenarioDevices files | editor capability hierarchy, resource keys, local IDs, categories, matching IDs, templates, and Parameter metadata | installed Device support, complete runtime graph, or public protocol semantics for frame-absent rows |
| [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Physical Device, firmware, Module, Object, and configuration capability | ScenarioDevices ID equivalence |
| [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) | systems, address rules, management frames, diagnostic/programming sequences, and timeouts | Scenario Engine graph or ScenarioDevices row mapping |
| [Functional reference](../functional/) | functional `WHO`, `WHAT`, `WHERE`, and `DIMENSION` semantics | MyHOME_Suite editor coverage by itself |
| [Cross-database functional coverage](../functional/cross-database-coverage.md) | corroborated intersections among implementation databases and functional frames | undeclared numeric joins |
| observed application/runtime behavior | UI labels, filtering, persistence, matching, and execution behavior | universal support beyond observed versions and Devices |

### Identifier namespaces

Section ID: `ownkb:section:d000134:s000004`

Provenance cues: `catalogue`, `evidence`

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

### Cross-file identity

Section ID: `ownkb:section:d000134:s000005`

The common semantic content of `programdata` is an exact subset of `program-files` when compared using the full hierarchical path and non-local fields:

- Object System resource key and `CategoryFlag`;
- Device Object resource key and Object/matching identifiers;
- Command resource key and command/matching/address/frame fields;
- Parameter resource key, placeholder, domain, type, operator, and stored value.

Local primary keys differ after the additional Program Files rows, so row IDs are not cross-file identities.

### Correlation rules

Section ID: `ownkb:section:d000134:s000006`

Cautions: `do not`
Provenance cues: `catalogue`, `evidence`, `source`, `specification`

A cross-source relationship can be documented as established when supported by one or more of:

1. a declared foreign key;
2. a literal OpenWebNet frame whose `WHO` and operation parse unambiguously;
3. an explicit matching identifier inside ScenarioDevices;
4. resource-key semantics corroborated by a literal frame or functional specification;
5. independently observed MyHOME_Suite behavior.

Do not correlate values only because their integers are equal. In particular, `FamilyId`, `ObjectId`, `CommandId`, catalogue system IDs, catalogue Object IDs, and OpenWebNet fields are independent until evidence connects them.

### Evidence labels

Section ID: `ownkb:section:d000134:s000007`

Uncertainty: `unknown`

This section uses:

- **established** for direct schema/data facts or corroborated protocol mappings;
- **implementation-derived** for stable meaning recovered from resource keys and stored frames;
- **inferred** for the best explanation of a complete observed pattern without a direct declaration;
- **unknown** where competing explanations remain.
