# Classe 300X

## Summary

Classe 300X is a connected, hands-free two-wire video-door-entry indoor unit with a seven-inch touchscreen. Light/dark finishes and optional inductive-loop variants share the catalogue item; retained newer documentation adds Wi-Fi and Home+Security app functions whose availability cannot be assumed for an installed historical firmware.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0050` | Project identity |
| Technical description | Classe 300X | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `344742`, `344743`, `344745`, `344746` | Canonical commercial records |
| Catalogue item | `2321` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `140` | Canonical inventory |
| Firmware definition | `1.0.1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Video door entry, Wi-Fi, Indoor unit, Integration | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `344742` | established catalogue identity for item `2321` | canonical commercial record |
| BTicino | `344743` | established catalogue identity for item `2321` | canonical commercial record |
| BTicino | `344745` | established catalogue identity for item `2321` | canonical commercial record |
| BTicino | `344746` | established catalogue identity for item `2321` | canonical commercial record |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `344742` | `8005543781326` | [Archived original](https://archive.openwebnet-ha.org/sha256/f0/d9/f0d94fbeddba68f0abd383cd37d8c2492f9e73551f92ff3f6fa9f73931c8ea29.pdf), `344742-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `344743` | `8005543781388` | [Archived original](https://archive.openwebnet-ha.org/sha256/3a/60/3a60db2122dea89843ea6bc35b6d7a2f2fd1c9a15d7cddf432c8013a49eefbd5.pdf), `344743-ean-product-sheet.pdf`, printed/PDF p. 2 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino `344742` product page | product page | current product family | Current Classe 300X connected indoor-unit functions and documentation links | Original not retained; discovery/provenance only; substantive claims use retained originals | [Official product page](https://www.bticino.com/products/bt-344742) |
| `FIS_C300X_1` | Multilingual installation instructions | 11/25-01 PC (November 2025) | Family mounting and English interfaces/electrical data: printed/PDF pp. 1, 3, 7–8; Dutch teleloop-reference discrepancy at p. 7; other language repetitions not fully examined | [Archived original](https://archive.openwebnet-ha.org/sha256/23/ae/23aed16981142cc869be0c0d0e10c8589c4e1a26af20303438256cfc2cc622d6.pdf) | [Official source](https://dar.bticino.it/asset/Documents/FIS_C300X_1.pdf) |
| `ST-00002362-EN` | technical sheet |2026-02-17; printed/PDF pp.1–24 | Loop variants: printed/PDF pp. 1–24; electrical/physical, physical presets, configuration, topology examples and functions examined. Preset diagrams pp. 6–14 visually checked | [Archived original](https://archive.openwebnet-ha.org/sha256/f5/0c/f50c64daa65dd92a67193c86524aed07e0826ab8d6249b449014435ad469fd21.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00002362-EN.pdf) |
| `344742-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `344742` to EAN-13 relationship at printed/PDF p. 2. Exact SKU/EAN and applicable technical attributes examined; reference and revision limits retained; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/f0/d9/f0d94fbeddba68f0abd383cd37d8c2492f9e73551f92ff3f6fa9f73931c8ea29.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344742) |
| `344743-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `344743` to EAN-13 relationship at printed/PDF p. 2. Exact SKU/EAN and applicable technical attributes examined; reference and revision limits retained; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/3a/60/3a60db2122dea89843ea6bc35b6d7a2f2fd1c9a15d7cddf432c8013a49eefbd5.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344743) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display / dimensions | `7 inch` LCD 1024×600; `172 × 125 × 19 mm` (W × H × D) | 344742/344743 exports pp. 1–2; ST-00002362-EN p. 1 for 344745/344746 |
| Variants | 344742 Light/344743 Dark; 344745 Light/344746 Dark with inductive loop | Canonical descriptions; FIS_C300X_1 pp. 1, 7–8 |
| SCS / additional supply | `20..27 Vdc`, `22..27 Vdc` with active loop; `38 mA` standby/`550 mA` operating. Additional 1–2:`27 Vdc`, `265 mA` or `320 mA` with loop | FIS_C300X_1 p. 8; ST sheet loop variants p. 1 |
| Terminals / environment | 2×1 mm² per terminal; `5..40 °C`; floor-call input, extra ringtone 5M–1, 2-wire bus and additional supply | FIS_C300X_1 pp. 3, 8; ST pp. 1–2 |
| Network / hardware revision | Current documented `2412..2472`/`5180..5825 MHz`, 802.11 b/g/n/ac/ax, WPA/WPA2/WPA3, <`20 dBm`; USB-C update connector | FIS_C300X_1 pp. 3, 8; 2026 ST pp. 1–2; not attributed to installed firmware `1.0.1` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2321` | Canonical catalogue |
| Technical item | Classe 300X | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `140` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `140` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Multimedia | private riser | Canonical item/bus relationship |
| Video door entry system 8 wires | private riser | Canonical item/bus relationship |
| Video door entry system 8 wires | public riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `2676` | `344742` | `1` | `5` | `Classe 300X NEW White indoor unit` |
| `2677` | `344743` | `1` | `5` | `Classe 300X NEW Dark indoor unit` |
| `2678` | `344745` | `1` | `5` | `Classe 300X NEW White indoor unit with Teleloop` |
| `2679` | `344746` | `1` | `5` | `Classe 300X NEW Dark indoor unit with Teleloop` |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `892` | `1` | `0` | `1` | `2` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `892` | `1137` | BTicino (key `1`) | `0` | Extra | `2321_1.0_BT\xml\Extra\extra.xml` |
| `892` | `1138` | BTicino (key `1`) | `0` | Protocol and other device parameters | `2321_1.0_BT\xml\Protocol\protocol.xml` |

All 2 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `892` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `4506` | `32` | `2014` |
| `892` | `2` | `154` Internal Unit | Fixed/designated metadata | `4507` | `154` | `2015` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `892` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `892` | USB | Canonical firmware/connection association |
| `892` | Ethernet over USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `892` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `154` - Internal Unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N` | `0..3999` | `0` | Address |
| `P` | `0..95` | `0` | Associated external unit |
| `HAND_FREE` | `0` = Disable; `1` = Enable | `0` | HAND_FREE |
| `PRO_STUDIO` | `0` = Disable; `1` = Enable | `0` | Professional Studio |
| `DOOR_STATE` | `0` = Disable; `1` = Enable | `0` | Door state display |
| `PEOPLE_S` | `0` = No; `1` = ?; `2` = ? | `0` | PeopleSearching |
| `MENU_PRE` | `0..99` | `0` | MenuPreset |
| `RING_T_OUT` | `1..30` | `10` | RingTimeOut |
| `CALL_T_OUT` | `10..180` | `30` | Call timeout |
| `PE_T_OUT` | `3..90` | `6` | EUConnectionTimeOut |
| `PI_T_OUT` | `3..90` | `18` | IUConnectionTimeOut |
| `TEL_T_OUT` | `3..180` | `90` | TelConnectionTimeout |
| `ASS_SWITCH` | `0..95` | `0` | AssociatedSwitchboard |
| `BEEP` | `0` = Disable; `1` = Enable | `0` | BEEP |
| `IS_SLAVE` | `0` = Not slave; `1` = Slave | Not specified in source | Slave |
| `DOSA_CALL` | `0` = Enable; `1` = Disable | `0` | Forward incoming call to ethernet |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `2321` / `modobj = 140` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`32`, `154`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Door entry | Answer/close calls, lock, entrance-panel/camera switching, intercom, stairs, video answering machine and switchboard response | ST-00002362-EN pp. 1–2, 23–24 |
| Local UI / advanced schedules | Favorites, notifications, 15 ringtones; scheduled professional studio and silent mode | Same source pp. 23–24; newer revision scope |
| Remote access | Home+Security association enables answering, CALL HOME, camera/Netatmo viewing, lock and firmware updates, subject to network/service setup | Same source p. 23 |
| Inductive loop | Only 344745/344746; hearing aid T selector, recommended `25..35` cm position; `0..9` kHz, <1.005 A/m | Same source pp. 1, 24; FIS p. 8 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Use physical N/P/M or the device’s screen tutorial/settings. Physical configuration predefines objects and permits renaming, whereas screen configuration without configurators permits creation/modification. Removing existing configurators requires reset. N identifies the internal unit, P its associated entrance panel; M tens/units combine predefined intercom, camera/lock, stairs and professional-studio functions; the two digit matrices differ. The detailed matrices and address-dependent examples are in ST-00002362-EN pp. 3–16; no catalogue filter supplies those physical presets. Wait one minute before reconnecting after reconfiguration (p. 15).

Installation limits depend on cable/topology, not one universal bus length: consult the table at p. 17. Examples specify additional 346020 supply for more than 10 units, one app-connected main per apartment, and maxima 5 units in apartment-interface/single-family cases versus 3 in the two-family example (pp. 18–22). Wi-Fi placement/obstructions and service availability affect app access. Power loss makes the unit unavailable (p. 1). These are documented example scopes, not observations.

Physical M presets (ST-00002362-EN, printed/PDF pp. 3–14; diagram/table placement visually checked):

| M digit / value | Published function set |
| --- | --- |
| Units 0 / absent | Staircase light |
| Units 1–3 | Direct additional lock at P+1, P+2 or P+3 respectively |
| Units 4–6 | Direct entrance-panel activation at P+1, P+2 or P+3 respectively |
| Units 7 | General paging to all system handsets |
| Units 8 | Internal intercom to all handsets with the same address |
| Units 9 | Enable/disable professional-studio function |
| Tens 1 | Same-address intercom; entrance panel P+1; locks P+1/P+2 |
| Tens 2 | General paging; entrance panel P+1; locks P+1/P+2 |
| Tens 3 | Same-address and installation-dependent apartment intercom; entrance panel P+1; lock P+1 |
| Tens 4 | Installation-dependent apartment intercom; locks P+1/P+2 |
| Tens 5 | Intercom among apartments through interface 346850; locks P+1/P+2 |
| Tens 6 | Four installation-dependent apartment-intercom targets |
| Tens 7 | Four inter-apartment targets through interface 346850 |
| Tens 8 | Entrance panel P+1; installation-dependent apartment intercom; locks P+1/P+2 |
| Tens 9 | Four additional locks P+1 through P+4 |

The tens examples also show staircase light when the units digit is 0 or absent. Intermediate configurations combine both digit sets; for example `M=13` combines tens 1 with direct lock P+3. Apartment intercom means within an apartment when interface 346850 is present, or among apartments without that interface. The diagrams specify relative N targets and actuator alternatives: lock actuator 346210 with `MOD=5` or 346230; panel activation with 346210 `MOD=9`. The p. 13 legend instead names 346200 for the first activation example, a source discrepancy that should not silently replace the detailed p. 6/14 device number. These are published modern presets, without observed mapping to catalogue firmware `892`.

## Source reconciliation

The catalogue records the NEW four-reference family, but its 1.0.1 tuple cannot be retrospectively mapped to the 2025/2026 publisher functions. The 2026 loop sheet supplies `22..27`V/320 mA for its loop scope, while the family instructions distinguish `20..27`V/265 mA without active loop. It repeats 344742/344743 wording in some example headings although the title names 344745/344746; keep diagram scope explicit. A Dutch FIS teleloop line names 344845 while English/Italian and the canonical four SKUs specify 344745/344746; that stray number is not a new established identity. Exact exports differ in recycled-material wording (>25%chemical for 344742, >80%mechanical for 344743); this commercial variant claim is not normalized into a shared hardware specification.

Firmware `892` designates two slots: Colors Touch Screen 32 and Internal Unit 154. Only product programming is associated; canonical Ethernet/USB connection labels do not establish a physical Ethernet socket on this Wi-Fi/2-wire product. No Virgin, slot conditions, filters or conversions are stored. Reusable Object `32` `FW_VER` default `3.0.0` does not equal the firmware `1.0.1` tuple. Internal Unit 154 N`0..3999`/P`0..95` and DOSA_CALL ethernet wording are generic schemas, not complete physical N/P/M programming instructions. PEOPLE_S values 1/2 have unknown labels and IS_SLAVE has no stored default; both uncertainties remain explicit. Two linked parameter payloads remain unexamined. New 2025/2026 hardware/network/app documentation cannot establish feature availability in installed firmware `1.0.1`.

## Evidence limits and open work

- Full use/install manual, app/service documentation, firmware release mapping and parameter payloads remain unexamined; the physical preset matrices are referenced for their detailed combinations.
- Canonical Ethernet connection labels do not establish a wired Ethernet connector; physical modern source hardware is Wi-Fi/2-wire with USB-C. Generic PeopleSearching values remain unknown.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `344742-ean-product-sheet.pdf`, printed/PDF p. 2: exact `344742` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/f0/d9/f0d94fbeddba68f0abd383cd37d8c2492f9e73551f92ff3f6fa9f73931c8ea29.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344742); SHA-256 `f0d94fbeddba68f0abd383cd37d8c2492f9e73551f92ff3f6fa9f73931c8ea29`.
- `344743-ean-product-sheet.pdf`, printed/PDF p. 2: exact `344743` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/3a/60/3a60db2122dea89843ea6bc35b6d7a2f2fd1c9a15d7cddf432c8013a49eefbd5.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344743); SHA-256 `3a60db2122dea89843ea6bc35b6d7a2f2fd1c9a15d7cddf432c8013a49eefbd5`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0041-0050-2026-10-06.md#own-dev-0050)
