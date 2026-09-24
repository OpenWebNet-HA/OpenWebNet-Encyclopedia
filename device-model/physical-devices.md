# Physical Devices

A Physical Device is one installed hardware product instance. It is the root of the Device → Module → Object → Configuration model, but the catalogue describes the product model while diagnostic traffic identifies the individual installed instance.

## Catalogue identity

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

### Device, item, and SKU

`EN_DEVICE.code` is the product code presented in the catalogue. It is not a language code. All 541 canonical Device rows contain a distinct non-null product code. Treating this column as a reference to `EN_LANGUAGE.code` would destroy valid SKU data.

Several branded products can share one `EN_ITEM` capability definition. For example, products `64391`, `64191`, and `64192` all select item `1184`, named “Flush mounted actuator and free control”. They therefore share the same firmware, Module, Object, and configuration capability model while retaining distinct catalogue Device records.

### Preferred description

When identifying a scanned physical product, use `EN_DEVICE.name` as the standard Device description. Do not substitute:

- `EN_ITEM.descr`, which describes the shared capability item
- `EN_KEY_OBJECT.descr`, which describes one logical Object
- a user-interface suffix added outside the catalogue
- an inferred class derived from one Module.

This preserves the distinction between “what product is installed?” and “what functions does it expose?”.

## Catalogue systems and model identity

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

## Installed-instance identity

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

## Diagnostic identity dimensions

The implementation database defines these Device-level identity responses:

| `DIMENSION` | Frame values | Scope |
| ---: | --- | --- |
| `1` | `OBJECT_MODEL`, `N_CONF`, `BRAND`, `LINE` | Catalogue/model identity |
| `2` | `FW_VERSION` | Firmware version |
| `3` | `HW_VERSION` | Hardware version |
| `6` | `MICRO_VERSION` | Microcontroller version |
| `13` | `ID` | Installed-instance identifier |

`OPEN.db` describes `N_CONF` as “Configurator number” and allows `0..12` for the ordinary addressed diagnostic form. Comparison with product configuration diagrams indicates that, in that addressed Device form, `N_CONF` represents the number of physical configurator positions provided by the Device.

### `N_CONF` and physical configurators

The interpretation is supported by Devices whose physical configuration layouts are documented independently:

| Device | `N_CONF` | Documented physical positions |
| --- | ---: | --- |
| `F420` | `2` | 2 |
| `F429` | `3` | 3 (`A`, `G`, `M`) |
| `H4652/3` | `7` | 7 |

The correspondence across Devices with different values argues against interpreting ordinary addressed-form `N_CONF` as a Module count or general Device classification. In that corroborated scope, it describes the size of the Device's physical configurator interface.

The catalogue registers Physical configuration, Virtual Configuration, Advanced Configuration, and Product Programming as distinct modes, and a firmware can support more than one of them. Physical configuration constrains values to those representable by the firmware's demonstrated physical definitions. In the ordinary addressed Device form, `N_CONF` describes the physical configurator positions provided by the hardware, not the number of logical configuration parameters or the active configuration mode.

The empty-`WHERE` gateway identity form is a separate variant. Observed MH202 and F454 responses both carry `N_CONF = 15`, which is outside the ordinary addressed-form `0..12` range. Numerically, `15` is `0xF`; viewed in four bits, it is `1111`, an all-ones pattern, so a reserved or sentinel interpretation is plausible; its exact meaning is unresolved. Do not treat that gateway value as a proven physical-position count. See [`DIMENSION 1`: Device Identity](../diagnostics/dim1-device-identity.md#gateway-variant).

The ordinary addressed-form interpretation remains to be checked against additional Devices, particularly older products for which configuration diagrams are less readily available.

## Physical composition

Physical form and logical composition are separate properties. The recurring Device classes used by this reference are:

| Class | Characteristic | Examples |
| --- | --- | --- |
| Actuator-only | Hardware outputs without independently configurable command Modules | `F411U2` |
| Dimmer-only | Dimming outputs without independent command Modules | `F418U2` |
| Command-only | Input hardware exposing command Objects but no actuator hardware | `64360` |
| Combined actuator and free command | Actuator Modules plus independently configurable command Modules | `64391`, `64191`, `64192` |
| Actuator with hard-linked controls | Local buttons always operate built-in outputs | `H4661M2` |

The classification describes hardware composition. It does not define the Device’s diagnostic identity values.

## Worked catalogue examples

### `64391`, `64191`, and `64192`

These three SKUs share item `1184`, item model `107`, and firmware `157`. The firmware declares four `slot` positions:

| Slots | Capability |
| --- | --- |
| `1..2` | actuator Object candidates |
| `3..4` | command/scenario Object candidates |

The exact Object selected in each slot can depend on physical configurator conditions. For example, `M1=CEN;M2=O/I` resolves to Objects `[6, 6, 400, 400]`; other reachable condition branches must be evaluated from the firmware's legal configurator domains. This is a combined Device, but the per-configuration topology should be derived rather than stored as an unconditional four-Module rule.

### `64360`

SKU `64360` resolves to item `281`, “Basic control”, with two command Modules. Its catalogue Object choices include Light control, Automation control, Scheduled scenario, and Scheduled scenario PLUS. No actuator Object is exposed by this item.

### `F411U2`

SKU `F411U2` resolves to item `2115`, “2x10A actuator, 2DIN”, and firmware `659`, which declares two slots. Both slots expose actuator capability.

### `F418U2`

SKU `F418U2` resolves to item `2065`, “2x1,6A universal dimmer, 4DIN”, and firmware `590`, which declares two dimmer slots.

### `3476` and `3477`

SKU `3476` is a one-slot Basic control actuator. SKU `3477` is a two-slot Basic contacts interface whose Modules can expose contact-state and command functions. Similar physical installation style therefore does not imply the same logical composition.

## Dependent Devices and interfaces

The catalogue contains additional Device-level associations:

- `AS_DEPENDENT_DEVICES` links master and dependent Device records.
- `AS_BUS_ITEM`, `AS_BUS_SYSTEM`, and `AS_BUS_INTERFACE` describe bus compatibility and interface roles.
- `AS_DEVICE_PICTURE` associates Device records with catalogue imagery.
- `EN_DEVICE.is_gateway` distinguishes gateway products.
- `EN_DEVICE.dependent` identifies dependent products.

These tables describe catalogue relationships. They do not by themselves establish diagnostic enumeration behavior.

## Address boundaries

A Device can carry several kinds of address:

1. a Device-level address used for discovery or interview;
2. configured functional addresses belonging to individual Modules/Objects;
3. installation-wide groups, environments, zones, CEN identifiers, or other system-specific associations.

For SCS Lighting/Automation Devices, the diagnostic `WHERE` of a Physical Device can resemble an `A`/`PL` address. That resemblance does not establish that every Device uses the first Module’s configured address. The relationship must be documented per family or per verified behavior.

## Sources

[`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) defines Device, item, brand, line, dependency, and bus records. [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) defines Device-identity frames and parameter ranges. Observed traffic and MyHOME_Suite behavior establish installed-instance values and displayed Device descriptions. Product configuration diagrams provide independent evidence for the physical configurator layouts used to interpret ordinary addressed-form `N_CONF`.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy and [`sources/manifest.yaml`](../sources/manifest.yaml) for provenance.
