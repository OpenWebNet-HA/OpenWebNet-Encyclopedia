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

## Physical-configurator counterparts

A configuration property can have both a physical representation on the Device and an advanced or virtual representation in the catalogue and diagnostic protocol. This is a correspondence between ways of configuring one effective property, not a separate Object or parameter variant.

For firmware definitions corroborated against product documentation, the physical configurator positions appear as firmware-scoped `EN_CONF` rows with `idx = -1`. The common `AID`/ID row is not a physical position and is excluded. `AS_FIRMWARE_CONFIG_MODE` and `EN_CONFIG_MODE` establish whether the firmware supports physical configuration.

To check whether a reported property has a physical-configurator counterpart:

1. resolve the Physical Device, firmware, internal slot, and configured Object;
2. confirm that the firmware supports physical configuration;
3. enumerate the firmware-scoped physical `EN_CONF` fields, excluding `AID`;
4. resolve the effective property from decoded `DIMENSION 32` addressing or the `DIMENSION 35` configuration index;
5. compare symbols, semantic types, ranges, filters, symbol references, and conversion rules;
6. use product documentation, UI behavior, or captures where the physical and advanced symbols differ.

| Diagnostic projection | Possible physical counterpart |
| --- | --- |
| decoded `DIMENSION 32.ADDR` component | address positions such as `A` and `PL` |
| `DIMENSION 35.INDEX` property | positions such as `M`, `TYPE`, `PRE`, or `G1` |
| property with no matching physical field | advanced-only unless another mapping source establishes a correspondence |

An identical symbol and compatible meaning provide a direct correspondence. Different symbols can still represent the same property, but require semantic corroboration; for example, a firmware position named `TYPE` can correspond to an Object property named `SHUTTER_TYPE`.

The correspondence does not reveal the active configuration method. `DIMENSION 32` and `35` report effective values. A value representable by a physical configurator could still have been assigned through advanced or virtual configuration. A value outside the physical representation can exclude physical configuration for that property, provided the applicable physical range is established.

`EN_PHY_TO_ADV_TRANS` contains conversion data for only three firmware definitions in this catalogue revision. It can support those cases but is not a general physical-to-advanced mapping registry.

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
2. select internal slot and Object;
3. collect applicable Object- and firmware-scoped configuration definitions;
4. locate the corresponding Object/firmware association;
5. apply `EN_FILTER`;
6. apply `EN_FILTER_RANGE`;
7. apply conditions and cross-property rules.

## Slot conditions and conversion rules

The catalogue contains:

- 1,000 `AS_SLOT_CONDITION` rows
- 488 `EN_CONDITION` rows
- 7,899 `EN_CONV_RULE` rows.

`AS_SLOT_CONDITION` attaches a condition to a slot/Object assignment. `EN_CONDITION.id_conv_rule` selects the conversion-rule logic used by that condition.

`EN_CONV_RULE` can compare item-level and Object-level configuration symbols and values, mark an always-true rule, or jump to another rule. These structures affect capability selection and value conversion; they are not OpenWebNet frames.

`CONF_SYMBOL_REF` supplies explicit symbol correspondence between item configuration and Object configuration for a system and slot.

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

`OPEN.db` defines the normal parameter response as:

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

| Field | Database description | Range |
| --- | --- | ---: |
| `INDEX` | “Parameter number (also known as kconf index)” | `0`–`255` |
| `SLOT` | “ko slot” | `1`–`255` |
| `VAL_PAR` | Parameter value | `0`–`65535` |

The shared “kconf index” terminology strongly supports correlating diagnostic `INDEX` with catalogue `EN_CONF.idx`. Because the databases have no cross-file key, retain the raw frame and resolved catalogue definition when documenting a mapping.

### Parameter request/reset

`OPEN.db` defines:

| Purpose | Frame |
| --- | --- |
| Select/reset one internal slot | `*#[WHO]*0*38#[SLOT]##` |
| Select/reset all slots | `*#[WHO]*0*38#0##` |

The database labels use “reset keyo”, while the `DiagKO` sequence describes the operation as obtaining detailed Object and configuration information. This wording difference should be preserved until runtime behavior is fully characterized.

### Special parameter response

`OPEN.db` defines:

`*#[WHO]*[WHERE]*310*[SLOT]*[VAL_PAR]##`

It labels this as the Device response for a special Object parameter. The template does not include an `INDEX`, so its value must not be forced into the ordinary `EN_CONF.idx` model without Object-specific evidence.

## Sequence context

The `OPEN.db` sequence `DiagKO` is described as “To get keyobject and kconf detailed info”. It orders:

1. the all-slot `DIMENSION 38` operation;
2. repeated `DIMENSION 35` parameter responses;
3. the special `DIMENSION 310` response where applicable.

Other diagnostic and configuration sequences include repeated `DIMENSION 30` and `32` responses before detailed parameter retrieval.

[`OpenQuery.txt`](../sources/myhome-suite/3.5.38/support/OpenQuery.txt) shows how MyHOME_Suite retrieves sequence membership, parameterized frames, address rules, and timeout behavior from `OPEN.db`.

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

A mapping between a UI field, catalogue definition, and protocol value requires compatible UI behavior, catalogue scope and index data, protocol slot/value evidence, and-where available-the resulting runtime behavior. Numeric equality alone is insufficient.

## Sources

Primary configuration evidence comes from [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db), with protocol structure from [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) and [`OpenQuery.txt`](../sources/myhome-suite/3.5.38/support/OpenQuery.txt). [`rules.db3`](../sources/myhome-suite/3.5.38/databases/rules.db3) adds selected Temperature Control dependencies. ScenarioDevices and the public protocol documents describe adjacent runtime layers rather than catalogue configuration identity.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy.
