# `DIMENSION 35`: Configuration Parameters

`DIMENSION 35` reports one indexed configuration value for one internal slot.

## Frame

`*#[WHO]*[WHERE]*35#[INDEX]#[SLOT]*[VAL_PAR]##`

| Field | Range in `OPEN.db` | Meaning |
| --- | ---: | --- |
| `INDEX` | `0`–`255` | parameter number, labelled “kconf index” |
| `SLOT` | `1`–`255` | Device-local internal slot |
| `VAL_PAR` | `0`–`65535` | parameter value |

Both `#` separators are significant parts of the canonical template.

## Catalogue correlation

The shared “kconf index” terminology and observed behavior strongly support correlating `INDEX` with `MHCatalogue.db` `EN_CONF.idx`. The databases contain no cross-file foreign key, so resolution must retain the full context:

- Physical Device and firmware;
- internal slot;
- Object selected in `DIMENSION 30`;
- applicable Object- or firmware-scoped `EN_CONF` definition;
- filters, conditions, and conversion rules;
- raw `VAL_PAR`.

`INDEX` is not globally unique. The same number can name different properties for different Objects or firmware definitions.

## Reading detailed parameters

`OPEN.db` defines the all-Module operation:

`*#[WHO]*0*38#0##`

and the one-Module form:

`*#[WHO]*0*38#[SLOT]##`

The `DiagKO` sequence places the all-Module operation before repeated `DIMENSION 35` responses and applicable `DIMENSION 310` responses. The source labels `DIMENSION 38` as reset/select while describing the sequence as retrieving detailed Object and configuration information. Implementations should preserve this source ambiguity and verify Device-side effects before using the operation on unfamiliar products.

## Resolving a value

1. Resolve the Device’s catalogue item and firmware.
2. Resolve `SLOT` and its selected Object from `DIMENSION 30`.
3. Find applicable `EN_CONF` rows whose `idx` equals `INDEX`.
4. Respect the exclusive Object-scoped or firmware-scoped discriminator in `EN_CONF`.
5. Apply `EN_CONF_RANGE`, `EN_FILTER`, `EN_FILTER_RANGE`, slot conditions, conversion rules, and any system-specific validation.
6. Interpret `VAL_PAR` according to the resolved configuration data type.
7. Keep the raw value when more than one definition remains possible.

Numeric equality alone is insufficient to map a parameter to a UI field.

## Value forms

Depending on the configuration definition, `VAL_PAR` can represent an enum member, numeric range value, padded address, boolean, fixed value, or user-supplied value. It can also require a conversion rule before presentation.

Detailed catalogue structures are documented in [Configuration](../device-model/configuration.md). Identifier boundaries are defined in [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md).

## Parameter errors

`DIMENSION 39` reports a parameter error:

`*#[WHO]*[WHERE]*39*[SLOT]*[INDEX]*[ERROR]##`

`ERROR` is boolean in `OPEN.db`. Preserve `SLOT` and `INDEX` so the error remains attached to the attempted property.

## Special Object parameter

`DIMENSION 310` uses:

`*#[WHO]*[WHERE]*310*[SLOT]*[VAL_PAR]##`

It carries no `INDEX`. Do not force it into the generic `EN_CONF.idx` mapping. Its meaning is Object-specific and remains unresolved globally.
