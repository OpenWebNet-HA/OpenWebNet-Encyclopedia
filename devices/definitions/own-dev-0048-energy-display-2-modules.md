# Energy display 2 modules

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0048` | Project identity |
| Technical description | Energy display 2 modules | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `H4710`, `LN4710`, `067205`, `64171` | Canonical commercial records |
| Catalogue item | `1884` | Canonical catalogue |
| Main catalogue system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `14` | Canonical inventory |
| Firmware definition | `1.0.-1` | Canonical firmware catalogue |
| Declared Modules | `10` | Canonical firmware catalogue |
| Categories | Energy management, Display, Load control | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4710` | established catalogue identity for item `1884` | canonical commercial record |
| BTicino - LivingLight | `LN4710` | established catalogue identity for item `1884` | canonical commercial record |
| Legrand - Céliane | `067205` | established catalogue identity for item `1884` | canonical commercial record |
| Arnould - Espace Evolution | `64171` | established catalogue identity for item `1884` | canonical commercial record |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4710` | `8005543515945` | [Archived original](https://archive.openwebnet-ha.org/sha256/b7/40/b740bdfc8f4df2e86540725e6e2d23f9fc24347b41c1144f1736cf7e1c5c02be.pdf), `H4710-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `LN4710` | `8005543515952` | [Archived original](https://archive.openwebnet-ha.org/sha256/3f/fa/3ffacdc3ebb495b79006fb3b7943a0484956b5bede3381e68e8d90adff808eb4.pdf), `LN4710-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ01014_a_EN` | technical sheet | revision a | Energy display functions, pages and measuring/load-management relationships | [Archived original](https://archive.openwebnet-ha.org/sha256/c7/82/c78272e5498b209f754eafad60625450f0d87572a559c5ee6f5c13dfa59fdd9c.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ01014_a_EN.pdf) |
| BTicino `H4710` catalogue page | product page | current catalogue | Current `H4710` electrical characteristics and product role | Not applicable - web page | [Official product page](https://catalogue.bticino.com/product/smart-home-solutions/my-home---home-automation-system/consumption-display/BTI-H4710-EN) |
| `H4710-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4710` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/b7/40/b740bdfc8f4df2e86540725e6e2d23f9fc24347b41c1144f1736cf7e1c5c02be.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4710) |
| `LN4710-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4710` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/3f/fa/3ffacdc3ebb495b79006fb3b7943a0484956b5bede3381e68e8d90adff808eb4.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4710) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | `1.6 inch` consumption/load-control display | `MQ01014_a_EN` / current catalogue |
| Supply | `27 Vdc` | Current BTicino `H4710` catalogue |
| Input current | `33 mA` | Current BTicino `H4710` catalogue |
| Width | 2 wiring-device modules | Current BTicino `H4710` catalogue |
| System role | Displays energy data and can control load-management actuators | `MQ01014_a_EN` / current catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1884` | Canonical catalogue |
| Technical item | Energy display 2 modules | Canonical catalogue |
| Main system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `14` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `405` | `1` | `0` | `-1` | `10` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `405` | `1` | `463` Load control actuator visualization | Candidate alternative | `2324` | `492` | `987` |
| `405` | `1` | `104` Measurement data visualization | Fixed/designated metadata | `2315` | `606` | `986` |
| `405` | `2` | `463` Load control actuator visualization | Candidate alternative | `2325` | `492` | `987` |
| `405` | `2` | `104` Measurement data visualization | Fixed/designated metadata | `2316` | `606` | `986` |
| `405` | `3` | `463` Load control actuator visualization | Candidate alternative | `2326` | `492` | `987` |
| `405` | `3` | `104` Measurement data visualization | Fixed/designated metadata | `2317` | `606` | `986` |
| `405` | `4` | `463` Load control actuator visualization | Candidate alternative | `2327` | `492` | `987` |
| `405` | `4` | `104` Measurement data visualization | Fixed/designated metadata | `2318` | `606` | `986` |
| `405` | `5` | `463` Load control actuator visualization | Candidate alternative | `2328` | `492` | `987` |
| `405` | `5` | `104` Measurement data visualization | Fixed/designated metadata | `2319` | `606` | `986` |
| `405` | `6` | `463` Load control actuator visualization | Candidate alternative | `2329` | `492` | `987` |
| `405` | `6` | `104` Measurement data visualization | Fixed/designated metadata | `2320` | `606` | `986` |
| `405` | `7` | `463` Load control actuator visualization | Candidate alternative | `2330` | `492` | `987` |
| `405` | `7` | `104` Measurement data visualization | Fixed/designated metadata | `2321` | `606` | `986` |
| `405` | `8` | `463` Load control actuator visualization | Candidate alternative | `2331` | `492` | `987` |
| `405` | `8` | `104` Measurement data visualization | Fixed/designated metadata | `2322` | `606` | `986` |
| `405` | `9` | `463` Load control actuator visualization | Candidate alternative | `2332` | `492` | `987` |
| `405` | `9` | `104` Measurement data visualization | Fixed/designated metadata | `2323` | `606` | `986` |
| `405` | `10` | `106` Energy display settings | Fixed/designated metadata | `2333` | `608` | `988` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `405` | `524` Energy data display virgin | `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `1` | `104`, `463` | `531` | `47` |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `405` | Advanced Configuration | supported configuration route for this Device family |
| `405` | Physical configuration | supported configuration route for this Device family |
| `405` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `405` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `405` | `M1` | `0..9` | `0` | Energy display basic mode for installation in France; Basic mode 1 (0-9, with `M2=0`) |
| `405` | `M2` | `0..6` | `0` | Energy display basic mode for installation in Italy; Basic mode 2 (0-6, with `M1=0`) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `463` - Load control actuator visualization

Catalogue Object key `492` maps to external Object `463`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | `0..63` | `1` | Priority |
| `PHASE` | `0` = Single phase; `1` = Phase 1; `2` = Phase 2; `3` = Phase 3 | `0` | Phase |


### Object `104` - Measurement data visualization

Catalogue Object key `606` maps to external Object `104`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LINE_1_OPERATION` | `0` = Disabled; `1` = Positive; `2` = Negative | `1` | Value of the first address; At least one of the parameters "Line 1 operation" - "Line 6 operation" must be different from 0. |
| `LINE_1_ADDRESS` | `0..127` | `1` | First address |
| `LINE_2_OPERATION` | `0` = None; `1` = Addition; `2` = Subtraction | `0` | Operation with the second address; At least one of the parameters "Line 1 operation" - "Line 6 operation" must be different from 0. |
| `LINE_2_ADDRESS` | `0..127` | `2` | Second address |
| `LINE_3_OPERATION` | `0` = None; `1` = Addition; `2` = Subtraction | `0` | Operation with the third address; At least one of the parameters "Line 1 operation" - "Line 6 operation" must be different from 0. |
| `LINE_3_ADDRESS` | `0..127` | `3` | Third address |
| `LINE_4_OPERATION` | `0` = None; `1` = Addition; `2` = Subtraction | `0` | Operation with the fourth address; At least one of the parameters "Line 1 operation" - "Line 6 operation" must be different from 0. |
| `LINE_4_ADDRESS` | `0..127` | `4` | Fourth address |
| `LINE_5_OPERATION` | `0` = None; `1` = Addition; `2` = Subtraction | `0` | Operation with the fifth address; At least one of the parameters "Line 1 operation" - "Line 6 operation" must be different from 0. |
| `LINE_5_ADDRESS` | `0..127` | `5` | Fifth address |
| `LINE_6_OPERATION` | `0` = None; `1` = Addition; `2` = Subtraction | `0` | Operation with the sixth address; At least one of the parameters "Line 1 operation" - "Line 6 operation" must be different from 0. |
| `LINE_6_ADDRESS` | `0..127` | `6` | Sixth address |
| `COEFFICIENT_K_USE` | `0` = Disabled; `1` = Enabled | `0` | State of multiplication factor (for all the lines); "Coefficient K_L" and "Coefficient K_H" are shown and can be modified only if "Coefficient K use" is set to 1. Otherwise, they are not shown and are set to the default values. |
| `COEFFICIENT_K_L` | `0..255` | `100` | Multiplication factor (low); The combination of parameters 26 and 27 defines a range from 1 to 10000 (from 0x0001 to 0x2710) for Coefficient K: if K_H = 0 (0x00), K_L must be in the range: 1-255 (0x01-0xFF); if K_H = 39 (0x27), K_L must be in the range: 0-16 (0x00-0x10). |
| `COEFFICIENT_K_H` | `0..39` | `0` | Multiplication factor (high); The combination of parameters 26 and 27 defines a range from 1 to 10000 (from 0x0001 to 0x2710) for Coefficient K: if K_H = 0 (0x00), K_L must be in the range: 1-255 (0x01-0xFF); if K_H = 39 (0x27), K_L must be in the range: 0-16 (0x00-0x10). |
| `ICON` | `0` = None; `1` = Electricity; `2` = Heating; `3` = Cooling; `4` = Water; `5` = Socket | `1` | Icon |
| `MEASUREMENT_UNIT` | `0` = None; `1` = Watt; `2` = Litre; `3` = Cubic meter - no decimal places; `4` = Cubic meter - 1 decimal place; `5` = Cubic meter - 2 decimal places; `6` = Cubic meter - 3 decimal places | `1` | Measurement unit |


### Object `106` - Energy display settings

Catalogue Object key `608` maps to external Object `106`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `BACKLIGHT_LEVEL` | `0` = `OFF`; `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 | `10` | Display backlight level |
| `BUZZER` | `0` = Disabled; `1` = Enabled | `1` | Enable/Disable beep |
| `DATE_FORMAT` | `0` = DD/MM/YYYY; `1` = MM/DD/YYYY | `0` | Display date format |
| `THRESHOLD_USE` | `0` = Disabled; `1` = Enabled | `1` | Threshold use; Threshold address (5), Threshold value L (6) and Threshold value H (7) |
| `THRESHOLD_ADDRESS` | `0..127` | `1` | Threshold address |
| `THRESHOLD_VALUE_L` | `0..255` | `0` | Threshold value L; The combination of parameters 6 and 7 defines a range from 0 (`OFF`) to 65535 (from 0x0000 to 0xFFFF) for Threshold value. |
| `THRESHOLD_VALUE_H` | `0..255` | `0` | Threshold value H; The combination of parameters 6 and 7 defines a range from 0 (`OFF`) to 65535 (from 0x0000 to 0xFFFF) for Threshold value. |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `405` | `106` | `1907` | `THRESHOLD_USE` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `1` | Threshold use |
| `405` | `106` | `1908` | `THRESHOLD_ADDRESS` | `0..127` (entire reusable range retained) | `1` | Threshold address |
| `405` | `106` | `1909` | `THRESHOLD_VALUE_L` | `0..255` (entire reusable range retained) | `0` | Threshold value L |
| `405` | `106` | `1910` | `THRESHOLD_VALUE_H` | `0..255` (entire reusable range retained) | `0` | Threshold value H |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1884` / `modobj = 14` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`463`, `104`, `106`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Energy-consumption visualization and load-management control with up to ten declared logical Modules and catalogue-selected energy/load-control Object families.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The technical sheet names H4710, 067205 and LN4710 and prints the Arnould reference as 064171; the canonical catalogue records 64171. The reference-format discrepancy is retained rather than silently normalized.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `H4710-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4710` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/b7/40/b740bdfc8f4df2e86540725e6e2d23f9fc24347b41c1144f1736cf7e1c5c02be.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4710); SHA-256 `b740bdfc8f4df2e86540725e6e2d23f9fc24347b41c1144f1736cf7e1c5c02be`.
- `LN4710-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4710` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/3f/fa/3ffacdc3ebb495b79006fb3b7943a0484956b5bede3381e68e8d90adff808eb4.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4710); SHA-256 `3ffacdc3ebb495b79006fb3b7943a0484956b5bede3381e68e8d90adff808eb4`.
