# `DIMENSION 1`: Device Identity

`DIMENSION 1` reports the catalogue-facing identity of a Physical Device.

## Frame

`*#[WHO]*[WHERE]*1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##`

| Field | Range in `OPEN.db` | Interpretation |
| --- | ---: | --- |
| `OBJECT_MODEL` | `1`–`65535` | item/model value |
| `N_CONF` | `0`–`12` | number of physical configurator positions |
| `BRAND` | `0`–`4` | brand code |
| `LINE` | `0`–`8` | product-line code |

## Catalogue correlations

| Diagnostic field | `MHCatalogue.db` field | Status |
| --- | --- | --- |
| `OBJECT_MODEL` | `AS_ITEM_SYSTEM.modobj` | corroborated |
| `BRAND` | `EN_BRAND.brand_modobj` | corroborated |
| `LINE` | `EN_LINE.line_modobj` | corroborated |
| `N_CONF` | no direct catalogue field identified | interpreted from `OPEN.db` wording and product documentation |

The established path uses `OBJECT_MODEL` within the relevant catalogue system, then applies brand and line metadata to narrow or present the matching product identity. It must not be replaced by a numeric join to `EN_DEVICE.id_device` or `EN_ITEM.id_item`; those are independent internal identifiers.

## Resolution procedure

1. Select the catalogue system corresponding to the diagnostic family using established system semantics, not equal internal `id_system` values across databases.
2. Find `AS_ITEM_SYSTEM` records whose `modobj` equals `OBJECT_MODEL`.
3. Resolve the associated `EN_ITEM` capability definition.
4. Use `BRAND` and `LINE` through `EN_BRAND.brand_modobj` and `EN_LINE.line_modobj` to identify compatible `EN_DEVICE` records.
5. Retain all candidates if the source revision does not distinguish them further.
6. Use firmware/version and observed Module layout as corroborating evidence, not as an invented primary-key join.

The result can be one shared item with several branded Device/SKU records. That is expected in the catalogue model.

Use `EN_DEVICE.name` as the standard MyHOME_Suite-facing description after resolution. `EN_ITEM.descr` names the shared capability item, while `EN_KEY_OBJECT.descr` names one logical function and must not replace the Physical Device description.

## Corroborated example

The observed Device `00C58E91` (`12947089` decimal) reported model value `107`. In the canonical catalogue:

- `AS_ITEM_SYSTEM.modobj = 107` resolves to item `1184`;
- `EN_ITEM.descr` is “Flush mounted actuator and free control”;
- firmware definition `157` declares four internal slots;
- several branded SKUs, including `64391`, `64191`, and `64192`, share that item.

The example corroborates the model-to-item path while also demonstrating why `OBJECT_MODEL` alone does not uniquely identify one SKU. Brand and line values, plus project/UI context where available, are required to narrow the Device record.

## `N_CONF` and physical configurators

`OPEN.db` describes `N_CONF` as “Configurator number” / “number of physical configurator” and constrains it to `0`–`12`. Product configuration diagrams provide an independent interpretation: the value corresponds to the number of physical configurator positions provided by the Device.

Documented examples include:

| Device | `N_CONF` | Physical configuration layout |
| --- | ---: | --- |
| `F420` | `2` | 2 configurator positions |
| `F429` | `3` | 3 positions: `A`, `G`, `M` |
| `H4652/3` | `7` | 7 configurator positions |

This field therefore describes the Device's physical configuration interface. It is not a Module count, Object identifier, Virgin Object, form factor, firmware class, or indication of the Object assigned to internal slot `1`.

MyHOME Devices can alternatively use advanced configuration, which can represent values outside the limits of the physical configurator interface. `N_CONF` remains a hardware characteristic: it does not describe the active configuration method or the number of logical configuration parameters.

Older Devices for which configuration diagrams have not yet been located remain useful targets for further cross-checking, but the available examples support the physical-position interpretation across multiple distinct `N_CONF` values.

## Address context

`WHERE` identifies the diagnostic response context. It is not part of the catalogue identity tuple and can differ from functional addresses reported later for individual Modules.

## Gateway variant

`OPEN.db` also contains a gateway identity response without an ordinary `WHERE`:

`*#[WHO]**1*[OBJECT_MODEL]*[N_CONF]*[BRAND]*[LINE]##`

Treat this as a distinct frame variant. Do not repair the empty field or silently convert it to the addressed form.

`OpenQuery.txt` includes this gateway variant in its gateway-connection query together with address scan and general diagnostic frames. That implementation use does not alter the identity-field mappings above.
