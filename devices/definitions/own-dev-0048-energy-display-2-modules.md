# Energy display 2 modules

## Summary

This two-module energy display shows consumption readings from external meters and the state of configured load-management actuators. Its 1.6-inch screen can combine or convert several readings and force eligible loads; it contains nine configurable display pages plus a separate settings Module in the catalogue.

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
| `MQ01014_a_EN` | technical sheet | MQ01014-a-EN;2014-12-02; printed/PDF pp.1–36; final three pages have MQ00XYZ-a-EN placeholder footers | Energy display functions, pages and measuring/load-management relationships | [Archived original](https://archive.openwebnet-ha.org/sha256/c7/82/c78272e5498b209f754eafad60625450f0d87572a559c5ee6f5c13dfa59fdd9c.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ01014_a_EN.pdf) |
| BTicino `H4710` catalogue page | product page | current catalogue | Current `H4710` electrical characteristics and product role | Original not retained; discovery/provenance only; substantive claims use retained originals | [Official product page](https://catalogue.bticino.com/product/smart-home-solutions/my-home---home-automation-system/consumption-display/BTI-H4710-EN) |
| `H4710-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4710` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined; reference and revision limits retained; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/b7/40/b740bdfc8f4df2e86540725e6e2d23f9fc24347b41c1144f1736cf7e1c5c02be.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4710) |
| `LN4710-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4710` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined; reference and revision limits retained; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/3f/fa/3ffacdc3ebb495b79006fb3b7943a0484956b5bede3381e68e8d90adff808eb4.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4710) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current | Nominal `27 Vdc`; operating `18..27 Vdc`; `33 mA` maximum backlight, `21 mA` standby backlight, `18 mA` backlight off | MQ01014-a-EN p. 1 |
| Environment / size | `5..35 °C`; two flush-mounted modules | Same source |
| Screen / interface | `1.6 inch` screen, line-selection/navigation keys, energy/unit/time/date and disabled/forced-load indicators; rear M1/M2 and bus | Same source |
| Measurement boundary | Receives meter data; power readings on load-control pages require F522; original 3522 pulse interface incompatible | Same source; 3522N appears in wiring examples |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1884` | Canonical catalogue |
| Technical item | Energy display 2 modules | Canonical catalogue |
| Main system | New energy saving and load control | Canonical catalogue |
| Item model / `modobj` | `14` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| New energy saving and load control | `14` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `2181` | `H4710` | `1` | `2` | `BTicino_Axolute_Energy Display 2M bus` |
| `2182` | `LN4710` | `1` | `4` | `BTicino_L/N/NT_Energy Display 2M bus` |
| `2183` | `067205` | `2` | `13` | `Legrand_Celiane_Energy Display 2M bus` |
| `2184` | `64171` | `7` | `18` | `Arnould_Espace Evolution_Energy Display 2M bu` |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `405` | `1` | `0` | `-1` | `10` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

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

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `405` | Physical configuration | `0` | Canonical firmware/mode association |
| `405` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `405` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

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

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Consumption / threshold | Instantaneous and daily/monthly/yearly values; local threshold menu unavailable in `M1=8` and `M2=6` | MQ01014-a-EN p. 1 |
| M1 presets | 1 heat+hot-water volume; 2 hot-water energy estimate; 3 heat+hot-water heat meters; 4 electric heating/hot water; 5 gas heat; 6 shared electric split; 7 shared gas split; 8 Energy Data Logger. Other M2 must be 0 | Same source pp. 2–19; each also supplies electric/socket/cooling and supported volume pages |
| M2 presets | 1 total electric+loads; 2 adds three electric lines; 3 total/cooling/water/heat+loads; 4 photovoltaic balance/water+loads; 5 seven electric lines/water/heat; 6 three-phase total/cooling/water/heat. Other M1 must be 0 | Same source pp. 21–33 |
| Meter arithmetic | Preset meter addresses must match tables; absent meters suppress associated pages. Sockets sum 002+003; ‘other’ subtracts measured branches from total. `M1=6` shares meter 004 with percentages summing 1; `M1=7` splits gas using supplier coefficient | Same source pp. 5–19; setup-specific examples, not installed values |
| Software pages | Up to 9 page Modules; `1..9` measurement/load display and 10 settings. Six signed/add/subtract inputs, coefficient, icon/unit; load pages specify actuator priority and single/three-phase selection | Same source pp. 34–36 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Physical M1 and M2 select the separate published preset tables; never activate both preset matrices simultaneously. `M1=9` exists in firmware but has no retained physical procedure. For pulse conversion, normalize meter pulses through 3522N according to its own instructions, which are unexamined here; volume-to-energy coefficients 0.01..100(default 1) require supplier/system data (MQ01014-a-EN pp. 5–19).

In Suite, enable pages, select Measurement or Load display, assign first signed value and up to five further additions/subtractions; require at least one active operation. Set coefficient use/value, icon and unit or load priority/phase. Slot `10` enables settings. The source’s circuit/component labels contain copy errors: several legends shift interface/display descriptions and ‘F22’ appears where the prose identifies F522. Consult the exact component instructions rather than wiring from those label errors (pp. 23–36).

## Source reconciliation

The source prints Arnould 064171 while catalogue 64171 lacks the leading zero; identity remains established with the formatting difference visible. Its final three pages use the placeholder MQ00XYZ-a-EN footer, yet continue the same dated product sheet. Firmware 10Modules agree with source nine display pages plus settings. Generic K byte range and physical decimal coefficient are preserved separately without inventing a conversion rule.

Firmware `405` declares ten Modules: slots `1..9` offer Measurement 104 and Load 463 alternatives; slot `10` designates Settings 106. Virgin `524` covers slots `1..9` only. No slot selectors or conversions are stored. Firmware M 1 permits `0..9`, but the published physical table enumerates `1..8`; M 1=9 remains undocumented. M 2 permits `0..6` and the sheet enumerates 1..6. Measurement 104 permits six signed/added/subtracted input addresses, with at least one operation enabled. K high/low form `1..10000` with boundary-byte constraints; defaults 0/100 encode 100, whereas the sheet describes a physical coefficient 1 and range 0.01..100. A scaling relationship is suggested but not established by a stored conversion. Settings threshold high/low combine `0..65535`; zero meansOFF in the reusable schema even though THRESHOLD_USE defaults enabled. Do not infer nine physical sensors or automatic Object selection from nine page slots.

## Evidence limits and open work

- The exact 3522N calibration, Energy Data Logger and load-central-unit instructions and energy display user manual remain unexamined.
- `M1=9`, runtime page/Object selection and coefficient scaling need the applicable software implementation; no observation supplies them.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `H4710-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4710` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/b7/40/b740bdfc8f4df2e86540725e6e2d23f9fc24347b41c1144f1736cf7e1c5c02be.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4710); SHA-256 `b740bdfc8f4df2e86540725e6e2d23f9fc24347b41c1144f1736cf7e1c5c02be`.
- `LN4710-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4710` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/3f/fa/3ffacdc3ebb495b79006fb3b7943a0484956b5bede3381e68e8d90adff808eb4.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4710); SHA-256 `3ffacdc3ebb495b79006fb3b7943a0484956b5bede3381e68e8d90adff808eb4`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0041-0050-2026-10-06.md#own-dev-0048)
