# `DIMENSION 1`: Device Identity

`DIMENSION 1` reports the catalogue-facing identity of a Physical Device.

## Frame

`*#[WHO]*[WHERE]*1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##`

| Field | Range in `OPEN.db` | Interpretation |
| --- | ---: | --- |
| `OBJECT_MODEL` | `1`–`65535` | item/model value |
| `N_CONF` | `0`–`12` | labelled “Configurator number”; broader meaning unresolved |
| `BRAND` | `0`–`4` | brand code |
| `LINE` | `0`–`8` | product-line code |

## Catalogue correlations

| Diagnostic field | `MHCatalogue.db` field | Status |
| --- | --- | --- |
| `OBJECT_MODEL` | `AS_ITEM_SYSTEM.modobj` | corroborated |
| `BRAND` | `EN_BRAND.brand_modobj` | corroborated |
| `LINE` | `EN_LINE.line_modobj` | corroborated |
| `N_CONF` | no established catalogue field | unresolved |

The established path uses `OBJECT_MODEL` within the relevant catalogue system, then applies brand and line metadata to narrow or present the matching product identity. It must not be replaced by a numeric join to `EN_DEVICE.id_device` or `EN_ITEM.id_item`; those are independent internal identifiers.

## Resolution procedure

1. Select the catalogue system corresponding to the diagnostic family using established system semantics, not equal internal `id_system` values across databases.
2. Find `AS_ITEM_SYSTEM` records whose `modobj` equals `OBJECT_MODEL`.
3. Resolve the associated `EN_ITEM` capability definition.
4. Use `BRAND` and `LINE` through `EN_BRAND.brand_modobj` and `EN_LINE.line_modobj` to identify compatible `EN_DEVICE` records.
5. Retain all candidates if the source revision does not distinguish them further.
6. Use firmware/version and observed Module layout as corroborating evidence, not as an invented primary-key join.

The result can be one shared item with several branded Device/SKU records. That is expected in the catalogue model.

## `N_CONF` remains unresolved

`OPEN.db` calls `N_CONF` a configurator number and constrains it to `0`–`12`. Current evidence does not establish that it identifies:

- an Object or Virgin Object;
- a Module count or internal slot;
- a form factor or product platform;
- a firmware class;
- the Object assigned to internal slot `1`.

Do not attach one of these meanings because a sample value happens to correlate. Preserve the raw value and source label until catalogue, UI, and traffic evidence establish a stable interpretation.

## Address context

`WHERE` identifies the diagnostic response context. It is not part of the catalogue identity tuple and can differ from functional addresses reported later for individual Modules.

## Gateway variant

`OPEN.db` also contains a gateway identity response without an ordinary `WHERE`:

`*#[WHO]**1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##`

Treat this as a distinct frame variant. Do not repair the empty field or silently convert it to the addressed form.
