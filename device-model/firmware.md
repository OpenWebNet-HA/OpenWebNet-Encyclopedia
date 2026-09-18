# Firmware

Firmware is the catalogue layer that projects an item into a concrete set of Modules, supported Objects, configuration properties, and connection modes.

## Catalogue representation

`EN_FIRMWARE` in `MHCatalogue.db` contains 311 firmware definitions.

| Column | Role |
| --- | --- |
| `id_firmware` | Internal firmware-definition identifier |
| `id_item` | Item to which the firmware belongs |
| `firmware_V` | Version component |
| `firmware_R` | Release/revision component (`R`) |
| `slots` | Number of internal slots declared by the firmware |
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

## Firmware selection

A shared item can have one or several firmware definitions. Device capabilities must therefore be resolved through the firmware selected for the installed product, not from the item alone.

The catalogue path is:

`EN_DEVICE.id_item` → `EN_FIRMWARE.id_item` → selected `EN_FIRMWARE.id_firmware`

The exact selection rule can depend on all three reported components, default flags, localization metadata, and MyHOME Suite behavior. A row being marked `FW_default` does not prove that every installed Device of that item runs that firmware.

### The `-1` sentinel

Negative components are implementation sentinels and must not be rendered as literal negative firmware versions. The canonical data provides strong evidence that `-1` means **any or unspecified value** for that component:

- all 101 firmware definitions with `firmware_V = -1` and `firmware_R = -1` have an associated `firmware_b = -1`, producing `-1.-1.-1`;
- all 101 of those definitions have `FW_default = 1`;
- another five definitions retain concrete version and release values but use `firmware_b = -1`: four are `1.0.-1`, and one is `5.2.-1`;
- an explicit `firmware_b = -1` is structurally different from having no `EN_BUILDS` row.

The mixed forms are particularly important: `1.0.-1` and `5.2.-1` show that the build sentinel can apply independently, rather than `-1.-1.-1` being only a malformed whole-version value.

The evidence therefore supports interpreting `-1.-1.-1` as a version-independent default or fallback and `V.R.-1` as any or unspecified build for a particular version and release. This is a **strongly corroborated interpretation of the data**, not a recovered MyHOME Suite comparison algorithm. Implementations should retain the raw components and must not claim that the precise wildcard-selection precedence is proven.

## Diagnostic firmware identity

`OPEN.db` defines:

`*#[WHO]*[WHERE]*2*[FW_VERSION]##`

Its parameter description gives the logical form `Version*Release*Build`. In this documentation, the equivalent catalogue tuple is written `V.R.b` to distinguish the three stored numeric components from the `*` separators used by OpenWebNet frames.

This response can be used to select or corroborate a catalogue firmware definition, but the databases do not contain a direct cross-database key between `FW_VERSION` in `OPEN.db` and `id_firmware` in `MHCatalogue.db`.

Related Device-level responses are:

- `DIMENSION 3`: hardware version
- `DIMENSION 6`: microcontroller version.

These values identify implementation revisions. They are not Object or Module identifiers.

## Capability projection

Once a firmware definition is selected, its capabilities are assembled through several associations:

| Association | Capability |
| --- | --- |
| `AS_OBJECT_FIRMWARE` | Objects supported by the firmware |
| `EN_SLOTS` | Internal slots at which each firmware/Object association is available |
| `AS_FIRMWARE_VIRGIN_OBJECT` | Virgin Object templates supported by the firmware |
| `EN_SLOT_KO_VIRGIN` | Internal slots to which those templates apply |
| firmware-scoped `EN_CONF` rows | Configuration properties belonging to the firmware rather than one Object |
| `AS_FIRMWARE_CONFIG_MODE` | Supported configuration modes |
| `AS_CONNECTION_FIRMWARE` | Supported connection modalities |
| `AS_FIRMWARE_PARAMETERS` | Parameter-file associations |
| `AS_FW_PACKAGE` | Firmware package associations |
| `EN_PHY_TO_ADV_TRANS` | Physical-to-advanced address translation data |

All 827 `AS_OBJECT_FIRMWARE` rows resolve to both a firmware definition and an Object. All 1,725 `EN_SLOTS` rows resolve to an `AS_OBJECT_FIRMWARE` row.

## Declared slots and Object alternatives

`EN_FIRMWARE.slots` is the declared count of internal slots. It must not be compared directly with the number of `EN_SLOTS` rows: one internal slot can have several supported Object alternatives.

For example, firmware `157` declares four slots but has ten slot/Object rows:

| Internal slot | Objects offered |
| ---: | --- |
| `1` | Light actuator; Automation actuator |
| `2` | Light actuator |
| `3` | Light control; Automation control; Scheduled scenario; Scheduled scenario PLUS |
| `4` | Light control; Automation control; Scheduled scenario; Scheduled scenario PLUS |

The Module count is four; the Object-option count is ten.

## Firmware-scoped configuration

`EN_CONF` contains both Object-scoped and firmware-scoped definitions. Firmware-scoped rows use:

- `id_key_object = 0`
- an `id_firmware` resolving to `EN_FIRMWARE`.

The canonical database contains 1,463 such rows. They represent configuration that cannot be attributed solely to a reusable Object definition.

Object-scoped rows use the complementary pattern described in [`configuration.md`](configuration.md).

## Default and fixed capability

`EN_SLOTS.fixed_ko` distinguishes one Object association from alternatives at a slot. In many firmware definitions exactly one association per slot carries `fixed_ko = 1`.

The database column name is evidence for a fixed/designated Object relationship. It is not, by itself, sufficient to decide every user-interface behavior:

- whether Function type is visible
- whether the user can change it
- whether another Object is selected automatically
- whether a Device variant hides alternatives.

Those behaviors require catalogue conditions, filters, and observed UI behavior.

## Firmware example

Firmware `157`, used by `64391`, `64191`, and `64192`, declares four internal slots. Its slot/Object rows expose two actuator Modules and two independently configurable command Modules. The product-level examples are collected in [Physical Devices](physical-devices.md).

## Sources

[`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) defines Firmware capabilities. [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) defines the diagnostic firmware-version response; observed traffic supplies the version returned by an installed Device. These values are correlated only when the selection is corroborated.

See [Sources and Identifier Boundaries](sources-and-identifiers.md) for the cross-source policy.
