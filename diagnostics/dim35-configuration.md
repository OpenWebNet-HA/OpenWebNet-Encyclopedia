# `DIMENSION 35`: Configuration Parameters

`DIMENSION 35` reports one indexed configuration value for one `slot`.

## Frame

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | ---: | --- |
| `INDEX` | `0..255` | parameter number, labelled “kconf index” |
| `SLOT` | `1..255` | Device-local `slot` |
| `VAL_PAR` | `0..65535` | parameter value |

Both `#` separators are significant parts of the canonical template.

## Catalogue correlation

The shared “kconf index” terminology and observed behavior strongly support correlating `INDEX` with `MHCatalogue.db` `EN_CONF.idx`. The databases contain no cross-file foreign key, so resolution must retain the full context:

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

## Reading detailed parameters

`OPEN.db` defines the all-Module operation:

`*#[WHO]*0*38#0##`

and the one-Module form:

`*#[WHO]*0*38#[SLOT]##`

The `DiagKO` sequence places the all-Module operation before repeated `DIMENSION 35` responses and applicable `DIMENSION 310` responses. The source labels `DIMENSION 38` as reset/select while describing the sequence as retrieving detailed Object and configuration information. Implementations should preserve this source ambiguity and verify Device-side effects before using the operation on unfamiliar products.

`ScanKOTimeWait` assigns an eight-second response window to the all-Module command. The one-Module form exists as a frame template but is not the command used by the canonical `DiagKO` sequence.

No explicit end marker belongs to `DiagKO`; completion is therefore governed by the response window and enclosing diagnostic scenario.

## Resolving a value

1. Resolve the Device’s catalogue item and firmware.
2. Resolve `SLOT` from `DIMENSION 30`; proceed with Object-scoped configuration only when `STATE = 0` identifies an enabled Module and resolves a regular configured Object.
3. Find applicable `EN_CONF` rows whose `idx` equals `INDEX`.
4. Respect the exclusive Object-scoped or firmware-scoped discriminator in `EN_CONF`.
5. Apply `EN_CONF_RANGE`, `EN_FILTER`, `EN_FILTER_RANGE`, slot conditions, conversion rules, and any system-specific validation.
6. Interpret `VAL_PAR` according to the resolved configuration data type.
7. Keep the raw value when more than one definition remains possible.

Numeric equality alone is insufficient to map a parameter to a UI field.

## Physical-configurator counterparts

After resolving `INDEX` to an Object property, compare that property with the physical fields declared for the resolved firmware. This can establish whether the effective property can also be configured through a physical configurator.

For shutter actuator Object `218` on firmware `192`, the catalogue provides these correspondences:

| Firmware physical field | Object property | `INDEX` | Correspondence |
| --- | --- | ---: | --- |
| `M` | `M` | `0` | direct symbol and semantic match |
| `TYPE` | `SHUTTER_TYPE` | `1` | semantic match; different symbols |
| `PRE` | `PRESET_NUMBER` | `8` | semantic match; different symbols |
| `G1` | `G1` | `240` | direct symbol and semantic match |

The same firmware also declares physical `A` and `PL` positions. Those are address properties with `idx = -1` on the Object and are projected through `DIMENSION 32`, not ordinary indexed `DIMENSION 35` properties.

A direct symbol match is strong catalogue evidence. A semantic match between different symbols requires filters, symbol references, conversion rules, product documentation, UI behavior, or captures to corroborate it. Even after resolving firmware and Object context, absence of a matching physical field establishes only that no counterpart was found in the inspected metadata. An advanced-only conclusion additionally requires evidence that the applicable physical interface and mappings are complete.

A physical counterpart does not identify the active configuration method, and physical and advanced forms need not share the same encoded value or permitted range. See [Physical configuration and configuration modes](../device-model/configuration.md#physical-configuration-and-configuration-modes) for the conceptual model, and [Physical-configuration resolution](../internals/catalogue-resolution.md#physical-configuration-resolution) when physical settings select Object topology before property conversion.

## Value forms

Depending on the configuration definition, `VAL_PAR` can represent an enum member, numeric range value, padded address, boolean, fixed value, or user-supplied value. It can also require a conversion rule before presentation.

Detailed catalogue structures are documented in [Configuration](../device-model/configuration.md). Identifier boundaries are defined in [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md).

`rules.db3` adds cross-property validation for selected Temperature Control Objects. It can refine a resolved value’s validity but is not a general `INDEX` registry. The ScenarioDevices databases define scenario-action parameters in separate namespaces and must not be used as `EN_CONF.idx` mappings.

## Runtime availability

`OPEN.db` models `DIMENSION 35` as a repeatable detailed-configuration response, but not every Object necessarily emits it. Observed configurable command and sensor Modules support the association with editable configuration; observed absence from another Module cannot by itself prove that the Object has no configuration.

Do not infer a universal split such as “actuators use only `DIMENSION 32`, commands use only `DIMENSION 35`”. A Module can have an address, indexed parameters, both, or neither depending on its Object and firmware.

## Parameter errors

`DIMENSION 39` reports a parameter error:

`*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##`

`ERROR` is boolean in `OPEN.db`. Preserve `SLOT` and `INDEX` so the error remains attached to the attempted property.

The frame identifies that a parameter error exists but does not enumerate a cause. Catalogue range violations, conditional visibility, unsupported indices, and Device state remain possible higher-level explanations rather than encoded error values.

## Special Object parameter

`DIMENSION 310` uses:

`*#[WHO]*[WHERE]*310*[SLOT]*[VAL_PAR]##`

It carries no `INDEX`. Do not force it into the generic `EN_CONF.idx` mapping. Its meaning is Object-specific and remains unresolved globally.

`OPEN.db` provides no `AS_OPEN_PARAM` metadata for the `DIMENSION 310` template beyond the placeholders embedded in the frame string. Its value range and semantic decoder therefore require Object-specific evidence.

## Source reconciliation

| Source | Contribution |
| --- | --- |
| `OPEN.db` | exact `DIMENSION 35`, `38`, `39`, and `310` templates, parameter ranges, sequence repetition, and timeout |
| `OpenQuery.txt` | ordered sequence and timeout retrieval used by MyHOME_Suite |
| `MHCatalogue.db` | configuration definitions, types, ranges, filters, conditions, and conversions |
| `rules.db3` | additional selected Temperature Control dependencies |
| Captures | actual `(SLOT, INDEX, VAL_PAR)` values and Device-specific availability |
| MyHOME_Suite UI | user-facing label, visibility, editability, and decoded presentation |
