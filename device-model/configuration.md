# Configuration

Configuration is the set of instance-specific values applied to an Object, Module, firmware, or Device. It turns catalogue capability into an operational function within an installation.

## Configuration layers

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

## Core catalogue table

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

## Two exclusive configuration scopes

Every canonical `EN_CONF` row uses one of two patterns:

| Scope | Key pattern | Rows |
| --- | --- | ---: |
| Object-scoped | valid `id_key_object`; `id_firmware = 0` | 1,420 |
| Firmware-scoped | `id_key_object = 0`; valid `id_firmware` | 1,463 |

No canonical row resolves simultaneously to both an Object and a firmware definition.

This is a discriminator pattern, not two mandatory foreign keys. Treating both columns as unconditional references would misrepresent half the table.

### Object-scoped configuration

Object-scoped definitions describe reusable properties of a logical function. Examples include:

- Function type
- point-to-point address
- group membership
- mode
- delays
- setpoints
- scenario numbers
- button assignments.

### Firmware-scoped configuration

Firmware-scoped definitions describe properties tied to one firmware capability rather than to a reusable Object alone. These can supply product-specific behavior, shared Device settings, or values used across several Modules.

A complete configuration UI may combine both scopes.

## Physical configuration and configuration modes

The canonical catalogue represents configuration mode and physical configurator semantics separately.

`EN_CONFIG_MODE` contains distinct records for Virtual Configuration, Advanced Configuration, Physical configuration, and Product Programming. `AS_FIRMWARE_CONFIG_MODE` records which modes a firmware supports. A firmware can support both Virtual and Advanced configuration, so neither label should be used as an umbrella synonym for all non-physical configuration.

Mode support is a catalogue capability. It does not establish which mode configured an installed Device or which MyHOME Suite UI label was active for a particular operation.

### Firmware-contextual physical definitions

Physical configurator interpretation is firmware- and definition-contextual. Firmware-scoped `EN_CONF` rows with `idx = -1` contain the principal physical definitions, but that structural pattern is not sufficient by itself: the common `AID`/ID definition also has `idx = -1` and is not a literal plug position.

For a demonstrated physical definition, `EN_CONF_RANGE` supplies the legal raw values and symbolic meanings. The correct conceptual lookup is:

```text
firmware + exact EN_CONF definition + raw value
```

not a universal lookup from the raw number alone. The same raw value can carry different labels for different symbols on the same firmware and across different firmware definitions.

`EN_CONF.progressive` records ordering metadata inside the catalogue. Although it can resemble physical ordering in examples, no canonical cross-database relation makes it equivalent to `DIMENSION 4.C1`, `C2`, and so on for every firmware.

### Topology selection

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

### Property conversion

Topology selection is distinct from converting selected physical/item settings into effective Object properties. After an Object branch is selected, `EN_CONDITION.id_conv_rule` can lead to `EN_CONV_RULE`, which maps item-level configuration symbols and values into Object-level configuration.

`CONF_SYMBOL_REF` supplies additional symbol correspondence only in its recorded system and slot context. Because it has no firmware key, it is not a global symbol-alias table.

One physical selector can therefore participate in topology selection and, separately, contribute to one or more resulting Object properties. These are different catalogue operations and should not be described as one undifferentiated physical-to-advanced translation.

### Physical counterparts of effective properties

A resolved Object property can have a physical counterpart, but the counterpart must be established in the exact firmware and Object context. Useful evidence includes compatible symbols, semantic types, legal ranges, filters, conversion rules, and contextual symbol references.

A physical counterpart does not identify the active configuration mode. `DIMENSION 32` and `35` report effective installed values; a value representable physically could still have been established through another supported configuration mode.

`EN_PHY_TO_ADV_TRANS` contains only three rows in the canonical MyHOME Suite 3.5.38 catalogue, for firmware IDs `160`, `691`, and `722`. It is supporting evidence for those cases, not the generic mechanism used to resolve physical topology or property conversion.

The authoritative algorithm, parameterized SQL, reachability rules, firmware `157` worked example, and `DIMENSION 4`/`5` boundary are documented in [Catalogue Resolution](../internals/catalogue-resolution.md#physical-configuration-resolution).

## Configuration type and data type

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

## Allowed values and ranges

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

## Contextual filters

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

## `slot` conditions and conversion rules

The catalogue contains:

- 1,000 `AS_SLOT_CONDITION` rows
- 488 `EN_CONDITION` rows
- 7,899 `EN_CONV_RULE` rows.

`AS_SLOT_CONDITION` attaches a condition to a `slot`/Object assignment. `EN_CONDITION.id_conv_rule` selects the conversion-rule logic used by that condition.

`EN_CONV_RULE` can compare item-level and Object-level configuration symbols and values, mark an always-true rule, or jump to another rule. These structures affect capability selection and value conversion; they are not OpenWebNet frames.

`CONF_SYMBOL_REF` supplies explicit symbol correspondence between item configuration and Object configuration for a system and `slot`.

## Additional Temperature Control rules

[`rules.db3`](../sources/myhome-suite/3.5.38/databases/rules.db3) adds cross-property validation and linked-parameter disabling for three Object numbers:

| Object | Catalogue description | Validation rows |
| ---: | --- | ---: |
| `95` | Hotel thermostat | 149 |
| `96` | Residential thermostat | 152 |
| `184` | Master probe | 107 |

Its `rules` table references configuration indices using expressions such as `$1`, `$2`, and `$21`. Its `DisablelinkedParameter` table contains 194 dependency rows that enable, disable, or constrain related parameters.

The Object numbers and configuration indices align with `EN_KEY_OBJECT.key_object` in `MHCatalogue.db` and `EN_CONF.idx` for those Temperature Control Objects. There is no database foreign key between the files, so the correlation is semantic and structural rather than relational.

`rules.db3` is not a general Object or `WHO` registry.

## Diagnostic parameter representation

Diagnostics projects an installed configuration through `DIMENSION 32`, indexed `DIMENSION 35` values, and Object-specific `DIMENSION 310` values. The canonical frame definitions, detailed-read sequence, timeout, and unresolved `DIMENSION 38` reset/select effect are maintained in [`DIMENSION 35`: Configuration Parameters](../diagnostics/dim35-configuration.md#reading-detailed-parameters).

The shared “kconf index” terminology strongly supports correlating diagnostic `DIMENSION 35.INDEX` with catalogue `EN_CONF.idx`. Because the databases have no cross-file key, retain the raw frame, resolved Physical Device, firmware, `slot`, Object, and catalogue definition when documenting a mapping. `DIMENSION 310` contains no generic `INDEX` and must remain outside that correlation without Object-specific evidence.

## Address configuration

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

## Functional and scenario projections

The public OpenWebNet documents define runtime values such as `WHAT`, functional `DIMENSION` values, and `WHERE` grammars. Those values are not automatically configuration indices.

The ScenarioDevices databases define scenario-engine command parameters. Their `Parameters` tables establish ranges and placeholders for scenario actions, not `EN_CONF` in `MHCatalogue.db` identities.

A scenario parameter can correspond conceptually to a Device/Object configuration value while remaining a separate application-level identifier.

## Read-only and calculated values

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

## Mapping requirements

A mapping between a UI field, catalogue definition, and protocol value requires compatible UI behavior, catalogue scope and index data, protocol `slot`/value evidence and, where available, the resulting runtime behavior. Numeric equality alone is insufficient.

## Sources

Primary configuration evidence comes from [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db), with protocol structure from [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) and [`OpenQuery.txt`](../sources/myhome-suite/3.5.38/support/OpenQuery.txt). [`rules.db3`](../sources/myhome-suite/3.5.38/databases/rules.db3) adds selected Temperature Control dependencies. ScenarioDevices and the public protocol documents describe adjacent runtime layers rather than catalogue configuration identity.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy.
