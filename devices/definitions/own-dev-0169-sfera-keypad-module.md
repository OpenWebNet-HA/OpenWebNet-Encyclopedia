# Sfera keypad module

## Summary

353000 is a numeric keypad that releases a door lock using a programmed code. It can operate independently or form part of a Sfera entrance panel, where selected modes also allow direct calls to residents. Its local relay and the speaker module’s door output are separate controlled locks.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0169` | Project identity |
| Technical description | Sfera keypad module | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `353000` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1470` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Access control | Main system association |
| Item model / `modobj` | `0` | Main association; independent of project ID |
| Firmware definition | `116`, `640`, `732` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Audio video, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Sfera | `353000` | Established catalogue identity | Manufacturer database commercial record `1470` explicitly links this SKU to item `1470` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `353000` | `8005543461884` | [353000-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/c2/c4/c2c472eb41bf22b61752af44635534a2471c2497545dda7524a8dd0ed6377ea1.pdf) PDF p. 1; `353000-italian-product-sheet.pdf` PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `353000` | Keypad module | Canonical commercial record `1470` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `RA00176AA_S_EN.pdf` | Technical Guide RA00176AA_S_EN | RA00176AA_S_EN; printed publication date not established | Earlier TiSferaDesign manual: PDF pp.6-14, 15-17, 22-35, compared against AC revision for applicable settings. Unrelated module settings outside this item. | [Archived original](https://archive.openwebnet-ha.org/sha256/14/14/1414875a0d40523aafb77d2f4947f60475d4dc1be6a27825883b0137b639d97f.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00176AA_S_EN.pdf) |
| `O1688A.pdf` | Instruction Use O1688A | O1688A; printed publication date not established | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/e5/96/e596e600c46963e74b25661c638dcf4f671c8c7e94d4e6e530159a19b1bb9904.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/O1688A.pdf) |
| `RA00176AC_S_EN.pdf` | Technical Guide RA00176AC_S_EN | RA00176AC-03/24-PC; printed revision label | PDF pp.6-9, 15-17, 22-35, 38-41: USB transfer, standalone/integrated keypad modes, address book and credential programming. Display-only settings outside this item. | [Archived original](https://archive.openwebnet-ha.org/sha256/7c/63/7c634fb15eebc8b90bef803b80677c9b638317d9a88c71679eece9581a796ff9.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00176AC_S_EN.pdf) |
| `RA00177AC_EN.pdf` | Technical Guide RA00177AC_EN | RA00177AC_EN; printed publication date not established | 353000: printed/PDF pp. 6-7, 12-32; wiring role, code management, relay / direct-call operation and reset. | [Archived original](https://archive.openwebnet-ha.org/sha256/49/45/4945a0c88f29312cae7a605b2386f1fef00278107844cdda137e11b07afc6b0c.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00177AC_EN.pdf) |
| `ST-00000684-EN.pdf` | Technical Sheet ST-00000684-EN | ST-00000684-EN; 19/06/2020 | PDF pp. 1-4: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/63/05/630526f13a9a76f90a1be5af74f64bdff012d6b80f8735f0543aebfa64c74655.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000684-EN.pdf) |
| `353000-publisher-product-sheet.pdf` | Exact English product export | Publisher DATASHEET; 05.10.2026 | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/c2/c4/c2c472eb41bf22b61752af44635534a2471c2497545dda7524a8dd0ed6377ea1.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-353000&include_technical=1) |
| `353000-italian-product-sheet.pdf` | Exact Italian product export | Product export retrieved 05/10/2026; boilerplate compliance dates are not product publication dates | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/06/4e/064e8896e93f149ea55ff5b0f767a8d21e4d55ac9728faa3635e813ceb5759ac.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-353000) |
| `RA00176AC_S_IT.pdf` | Manufacturer Italian / installation document | RA00176AC-03/24-PC; printed revision label | TiSferaDesign 2024: applicable keypad pp.15-17 and credential/address-book sections pp.22-35; selected Italian mode/role cross-checks. Remaining UI walkthroughs not independently translated. | [Archived original](https://archive.openwebnet-ha.org/sha256/23/78/237891b468a5152361ad36fd432ebd52e8804aecbfb2373a0c953dd7cc98eb8b.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00176AC_S_IT.pdf) |
| `RA00177AC_IT.pdf` | Manufacturer Italian / installation document | RA00177AC_IT; printed publication date not established | 353000: printed/PDF pp. 6-7, 12-32; wiring role, code management, relay / direct-call operation and reset. | [Archived original](https://archive.openwebnet-ha.org/sha256/5e/3c/5e3c8793a5a5bc8327467681678a9e1f4f2d8f6c3327e8532c4a7b88053b6d10.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00177AC_IT.pdf) |
| `ST_00000684_IT.pdf` | Manufacturer Italian / installation document | ST_00000684_IT; 19/06/2020 | PDF pp. 1-4: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/50/36/5036b9575228f57f9ac4217ef10ec3b2ca832638f36698e4edc7e6e83b0c2977.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000684_IT.pdf) |
| `TisferaDesign_README_v4.pdf` | Software TISFERADESIGN_README_V4 | TisferaDesign_README_v4; 14/05/2026 | PDF pp. 1-1: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/52/48/52481f4b2cb9999abf86bb870007398845f3f29a7a52fb475dbf90a880d31f65.pdf) | [Publisher original](https://assets.legrand.com/pim/AUTRE/TisferaDesign_README_v4.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1470`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..27 Vdc` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| Standby, backlight off / on | `10 mA / 25 mA` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| Maximum draw | `45 mA` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| Temperature / assembled protection | `-25..70 °C; IP54` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| Face dimensions | `115 x 91 mm` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| Local relay | `C / NC / NO; 8 A at 30 Vdc or 30 Vac cos phi 1; 3.5 A at 30 Vac cos phi 0.4` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| Local inputs | `CP / P1 / P2 local door-release pushbutton terminals; no generic tamper-input role established` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| PC interface | `front mini-USB; TiSferaDesign` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| Operating roles | `standalone; Sfera door release; direct call; French HEXACT/Vigik access control` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| Code length | `4..9 digits for opening; call code 1..4 digits, address 0..3999` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |
| Manual code capacities | `20 administrators; 100 passepartout; 4000 resident codes, one per apartment in compatible pushbutton-panel installation` | `ST-00000684-EN` printed/PDF pp. 1-4; `RA00177AC_EN` pp. 12-32 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Model | `Speak/ring` | `353000-publisher-product-sheet.pdf` PDF p. 2 |
| Installation technique | `Bus system` | `353000-publisher-product-sheet.pdf` PDF p. 2 |
| Width | `115 mm` | `353000-publisher-product-sheet.pdf` PDF p. 2 |
| Height | `91 mm` | `353000-publisher-product-sheet.pdf` PDF p. 2 |
| Depth | `26.9 mm` | `353000-publisher-product-sheet.pdf` PDF p. 2 |
| Number of call buttons | `3999` | `353000-publisher-product-sheet.pdf` PDF p. 2 |
| Colour | `Other` | `353000-publisher-product-sheet.pdf` PDF p. 2 |
| Connected object | `No` | `353000-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1470` | Canonical catalogue |
| Technical item description | Keypad module | Canonical catalogue |
| Item family | Device for Access Control system; key `101` | Canonical catalogue |
| Main system | Access control; key `8` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `0` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Access control | `0` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `116` | `1` | `2` | `5` | `1` | Catalogue default | Official |
| `640` | `2` | `0` | `15` | `1` | Not catalogue default | Official |
| `732` | `2` | `1` | `11` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `116` | `200` | BTicino (key `1`) | `7` | external software | `TiSferaDesign_0102` |
| `640` | `626` | BTicino (key `1`) | `7` | external software | `TiSferaDesign_0200` |
| `732` | `1024` | BTicino (key `1`) | `7` | external software | `TiSferaDesign_0300` |

All 3 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `116` | `1` | `480` Keypad as Sfera video door entry module | Candidate alternative | `2291` | `515` | `969` |
| `116` | `1` | `481` Keypad as Sfera access control module | Fixed / designated metadata | `2347` | `516` | `1002` |
| `640` | `1` | `480` Keypad as Sfera video door entry module | Candidate alternative | `2464` | `515` | `1116` |
| `640` | `1` | `481` Keypad as Sfera access control module | Fixed / designated metadata | `2465` | `516` | `1117` |
| `732` | `1` | `480` Keypad as Sfera video door entry module | Candidate alternative | `2661` | `515` | `1271` |
| `732` | `1` | `481` Keypad as Sfera access control module | Fixed / designated metadata | `2662` | `516` | `1272` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `116` | Product Programming | `3` | Canonical firmware/mode association |
| `640` | Product Programming | `3` | Canonical firmware/mode association |
| `732` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `116` | USB | Canonical firmware/connection association |
| `640` | USB | Canonical firmware/connection association |
| `732` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Standalone A+B+C / M` | Address `000..999`; physical M unused in ordinary standalone configuration | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |
| `Standalone T=0 /1 /2 /3 /4 /5 /6 /7` | Absent=4 s; 1 s; 10 s; 20 s; 40 s; 60 s; 90 s; 180 s | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |
| `Sfera M=0 / M=3` | Speaker lock only / speaker and local second lock; local relay fixed 4 s in `M=3`; A/B/C and T unused | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |
| `Sfera M=20 / M=23` | Adds direct internal-unit calling to `M=0` /3; A unused; B/C riser `01..39` when needed | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |
| `Central M=2 / M=22` | Access-controller-managed lock and directory; `M=22` adds direct call, excluded on risers; relay timing centrally managed | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |
| `Central physical / software addressing` | Standalone physical A+B addresses 348500, C unused; software central-address A/B and reader-address C fields exist; these are distinct configuration routes | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |
| `Opening code / call code` | Opening `4..9` digits; software maximum length default 9; calling `1..4` digits for `0..3999` | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |
| `Administrator / passepartout / resident capacity` | 20 /100 /4000; one resident code per apartment in documented speaker +352000/352100 pushbutton installation | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |
| `Display-combined programming` | When paired with 352500, use display manual for code administration; do not equate its 20 visitor codes with all keypad capacities | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |
| `Deletion / reset` | Administrator or passepartout erase procedures remove their full class; power-on button reset removes all stored codes / restores defaults; paired speaker / keypad wait ≥1 min before re-enrolment | `ST-00000684-EN` printed/PDF pp. 2-4; `RA00177AC_EN` pp. 12-32; `RA00176AC_S_EN` pp. 15-17 |

### Commissioning software prerequisites

These are the retained readme requirements, separate from product electrical ratings and current operating-system compatibility.

| Property | Published value | Evidence |
| --- | --- | --- |
| Windows / framework | `10 or11,64-bit;.NET4.8 or higher` | `TisferaDesign_README_v4` p.1 |
| CPU / RAM | `10th-generation i5 or equivalent;8 GB minimum,16 GB recommended` | `TisferaDesign_README_v4` p.1 |
| Disk / display | `500 MB;1366x768 minimum,1920x1080 recommended` | `TisferaDesign_README_v4` p.1 |
| Market scope | `TiSferaDesign_es_04.xx.xx for Spanish market only` | `TisferaDesign_README_v4` p.1 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `116` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `116` | `AC_A` | `0..9` | `0` | A; local address hundreds configurator |
| `116` | `AC_B` | `0..9` | `0` | B; local address tenths configurator |
| `116` | `AC_C` | `0..9` | `0` | C; local address units configurator |
| `116` | `AC_M` | `0`; `2` | `0` | M; operating mode configurator (Local management: 0) (Remote management: 2) |
| `116` | `AC_T` | `0..7` | `0` | T; local relay timing |
| `640` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `640` | `AC_A` | `0..9` | `0` | A; local address hundreds configurator |
| `640` | `AC_B` | `0..9` | `0` | B; local address tenths configurator |
| `640` | `AC_C` | `0..9` | `0` | C; local address units configurator |
| `640` | `AC_M` | `0`; `2` | `0` | M; operating mode configurator (Local management: 0) (Remote management: 2) |
| `640` | `AC_T` | `0..7` | `0` | T; local relay timing |
| `732` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `732` | `AC_A` | `0..9` | `0` | A; local address hundreds configurator |
| `732` | `AC_B` | `0..9` | `0` | B; local address tenths configurator |
| `732` | `AC_C` | `0..9` | `0` | C; local address units configurator |
| `732` | `AC_M` | `0`; `2` | `0` | M; operating mode configurator (Local management: 0) (Remote management: 2) |
| `732` | `AC_T` | `0..7` | `0` | T; local relay timing |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `480` - Keypad as Sfera video door entry module

Catalogue Object key `515` maps to external Object `480`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_AC_SFERA` | `0` = LED_OFF; `1` = LED_ON; `2` = LED_ONLY_ERRORS | `0` | Led behaviour in Sfera access control modules |
| `BUZZER_AC_SFERA` | `0` = BUZZER_OFF; `1` = BUZZER_ON; `2` = BUZZER_ONLY_PRESSIONS | `0` | Buzzer behaviour in Sfera access control modules |
| `MULTICH_EXT_RELAY_AC_SFERA` | `0` = MultiCH_Relay_OFF; `1` = MultiCH_Relay_ON | `0` | External relay for Sfera keypad access control module |
| `RELAY_TIME_AC_SFERA` | `255` = RELAY_OFF; `1` = RELAY_1S; `0` = RELAY_4S; `2` = RELAY_10S; `3` = RELAY_20S; `4` = RELAY_40S; `5` = RELAY_60S; `6` = RELAY_90S; `7` = RELAY_180S | `255` | Relay timings for Sfera access control modules |
| `BP_AC_SFERA` | `0` = BP_AS_BUTTON; `1` = BP_AS_TAMPER; `2` = BP_AS_NOTHING; `3` = BP_AND_TAMPER | `0` | Bp button behaviour in Sfera access control modules |
| `MODE_AC_SFERA` | `0` = SAVE_RESID; `2` = AC_READER | `0` | Operating modes for Sfera access control modules |
| `AC_ADDRESS_AB` | `0..99` | `0` | "AB" side of access control device address |
| `AC_ADDRESS_C` | `0..9` | `0` | "C" side of access control device address |

### Object `481` - Keypad as Sfera access control module

Catalogue Object key `516` maps to external Object `481`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_AC_SFERA` | `0` = LED_OFF; `1` = LED_ON; `2` = LED_ONLY_ERRORS | `0` | Led behaviour in Sfera access control modules |
| `BUZZER_AC_SFERA` | `0` = BUZZER_OFF; `1` = BUZZER_ON; `2` = BUZZER_ONLY_PRESSIONS | `0` | Buzzer behaviour in Sfera access control modules |
| `MULTICH_EXT_RELAY_AC_SFERA` | `0` = MultiCH_Relay_OFF; `1` = MultiCH_Relay_ON | `0` | External relay for Sfera keypad access control module |
| `RELAY_TIME_AC_SFERA` | `255` = RELAY_OFF; `1` = RELAY_1S; `0` = RELAY_4S; `2` = RELAY_10S; `3` = RELAY_20S; `4` = RELAY_40S; `5` = RELAY_60S; `6` = RELAY_90S; `7` = RELAY_180S | `255` | Relay timings for Sfera access control modules |
| `BP_AC_SFERA` | `0` = BP_AS_BUTTON; `1` = BP_AS_TAMPER; `2` = BP_AS_NOTHING; `3` = BP_AND_TAMPER | `0` | Bp button behaviour in Sfera access control modules |
| `MODE_AC_SFERA` | `0` = SAVE_RESID; `2` = AC_READER | `0` | Operating modes for Sfera access control modules |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `116` | `1` | `480` | `4925` | No textual predicate stored | `7166` |
| `116` | `1` | `481` | `4926` | No textual predicate stored | `7154` |
| `640` | `1` | `480` | `4925` | No textual predicate stored | `7166` |
| `640` | `1` | `481` | `4926` | No textual predicate stored | `7154` |
| `732` | `1` | `480` | `4925` | No textual predicate stored | `7166` |
| `732` | `1` | `481` | `4926` | No textual predicate stored | `7154` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `116` | `481` | `1810` | `MODE_AC_SFERA` | `0` = SAVE_RESID; `2` = AC_READER (entire reusable range retained) | `0` | Operating modes for Sfera access control modules |
| `640` | `481` | `1847` | `MODE_AC_SFERA` | `0` = SAVE_RESID; `2` = AC_READER (entire reusable range retained) | `0` | Operating modes for Sfera access control modules |
| `732` | `481` | `2997` | `MODE_AC_SFERA` | `0` = SAVE_RESID; `2` = AC_READER (entire reusable range retained) | `0` | Operating modes for Sfera access control modules |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7154` | `AC_A=0; AC_B=0` | `AC_ADDRESS_AB` = `0` | `7154` → `7155` |
| `7154` | `AC_A=0; AC_B=1` | `AC_ADDRESS_AB` = `1` | `7154` → `7155` |
| `7154` | `AC_A=0; AC_B=2` | `AC_ADDRESS_AB` = `2` | `7154` → `7155` |
| `7154` | `AC_A=0; AC_B=3` | `AC_ADDRESS_AB` = `3` | `7154` → `7155` |
| `7154` | `AC_A=0; AC_B=4` | `AC_ADDRESS_AB` = `4` | `7154` → `7155` |
| `7154` | `AC_A=0; AC_B=5` | `AC_ADDRESS_AB` = `5` | `7154` → `7155` |
| `7154` | `AC_A=0; AC_B=6` | `AC_ADDRESS_AB` = `6` | `7154` → `7155` |
| `7154` | `AC_A=0; AC_B=7` | `AC_ADDRESS_AB` = `7` | `7154` → `7155` |
| `7154` | `AC_A=0; AC_B=8` | `AC_ADDRESS_AB` = `8` | `7154` → `7155` |
| `7154` | `AC_A=0; AC_B=9` | `AC_ADDRESS_AB` = `9` | `7154` → `7155` |
| `7154` | `AC_A=1; AC_B=0` | `AC_ADDRESS_AB` = `10` | `7154` → `7156` |
| `7154` | `AC_A=1; AC_B=1` | `AC_ADDRESS_AB` = `11` | `7154` → `7156` |
| `7154` | `AC_A=1; AC_B=2` | `AC_ADDRESS_AB` = `12` | `7154` → `7156` |
| `7154` | `AC_A=1; AC_B=3` | `AC_ADDRESS_AB` = `13` | `7154` → `7156` |
| `7154` | `AC_A=1; AC_B=4` | `AC_ADDRESS_AB` = `14` | `7154` → `7156` |
| `7154` | `AC_A=1; AC_B=5` | `AC_ADDRESS_AB` = `15` | `7154` → `7156` |
| `7154` | `AC_A=1; AC_B=6` | `AC_ADDRESS_AB` = `16` | `7154` → `7156` |
| `7154` | `AC_A=1; AC_B=7` | `AC_ADDRESS_AB` = `17` | `7154` → `7156` |
| `7154` | `AC_A=1; AC_B=8` | `AC_ADDRESS_AB` = `18` | `7154` → `7156` |
| `7154` | `AC_A=1; AC_B=9` | `AC_ADDRESS_AB` = `19` | `7154` → `7156` |
| `7154` | `AC_A=2; AC_B=0` | `AC_ADDRESS_AB` = `20` | `7154` → `7157` |
| `7154` | `AC_A=2; AC_B=1` | `AC_ADDRESS_AB` = `21` | `7154` → `7157` |
| `7154` | `AC_A=2; AC_B=2` | `AC_ADDRESS_AB` = `22` | `7154` → `7157` |
| `7154` | `AC_A=2; AC_B=3` | `AC_ADDRESS_AB` = `23` | `7154` → `7157` |
| `7154` | `AC_A=2; AC_B=4` | `AC_ADDRESS_AB` = `24` | `7154` → `7157` |
| `7154` | `AC_A=2; AC_B=5` | `AC_ADDRESS_AB` = `25` | `7154` → `7157` |
| `7154` | `AC_A=2; AC_B=6` | `AC_ADDRESS_AB` = `26` | `7154` → `7157` |
| `7154` | `AC_A=2; AC_B=7` | `AC_ADDRESS_AB` = `27` | `7154` → `7157` |
| `7154` | `AC_A=2; AC_B=8` | `AC_ADDRESS_AB` = `28` | `7154` → `7157` |
| `7154` | `AC_A=2; AC_B=9` | `AC_ADDRESS_AB` = `29` | `7154` → `7157` |
| `7154` | `AC_A=3; AC_B=0` | `AC_ADDRESS_AB` = `30` | `7154` → `7158` |
| `7154` | `AC_A=3; AC_B=1` | `AC_ADDRESS_AB` = `31` | `7154` → `7158` |
| `7154` | `AC_A=3; AC_B=2` | `AC_ADDRESS_AB` = `32` | `7154` → `7158` |
| `7154` | `AC_A=3; AC_B=3` | `AC_ADDRESS_AB` = `33` | `7154` → `7158` |
| `7154` | `AC_A=3; AC_B=4` | `AC_ADDRESS_AB` = `34` | `7154` → `7158` |
| `7154` | `AC_A=3; AC_B=5` | `AC_ADDRESS_AB` = `35` | `7154` → `7158` |
| `7154` | `AC_A=3; AC_B=6` | `AC_ADDRESS_AB` = `36` | `7154` → `7158` |
| `7154` | `AC_A=3; AC_B=7` | `AC_ADDRESS_AB` = `37` | `7154` → `7158` |
| `7154` | `AC_A=3; AC_B=8` | `AC_ADDRESS_AB` = `38` | `7154` → `7158` |
| `7154` | `AC_A=3; AC_B=9` | `AC_ADDRESS_AB` = `39` | `7154` → `7158` |
| `7154` | `AC_A=4; AC_B=0` | `AC_ADDRESS_AB` = `40` | `7154` → `7159` |
| `7154` | `AC_A=4; AC_B=1` | `AC_ADDRESS_AB` = `41` | `7154` → `7159` |
| `7154` | `AC_A=4; AC_B=2` | `AC_ADDRESS_AB` = `42` | `7154` → `7159` |
| `7154` | `AC_A=4; AC_B=3` | `AC_ADDRESS_AB` = `43` | `7154` → `7159` |
| `7154` | `AC_A=4; AC_B=4` | `AC_ADDRESS_AB` = `44` | `7154` → `7159` |
| `7154` | `AC_A=4; AC_B=5` | `AC_ADDRESS_AB` = `45` | `7154` → `7159` |
| `7154` | `AC_A=4; AC_B=6` | `AC_ADDRESS_AB` = `46` | `7154` → `7159` |
| `7154` | `AC_A=4; AC_B=7` | `AC_ADDRESS_AB` = `47` | `7154` → `7159` |
| `7154` | `AC_A=4; AC_B=8` | `AC_ADDRESS_AB` = `48` | `7154` → `7159` |
| `7154` | `AC_A=4; AC_B=9` | `AC_ADDRESS_AB` = `49` | `7154` → `7159` |
| `7154` | `AC_A=5; AC_B=0` | `AC_ADDRESS_AB` = `50` | `7154` → `7160` |
| `7154` | `AC_A=5; AC_B=1` | `AC_ADDRESS_AB` = `51` | `7154` → `7160` |
| `7154` | `AC_A=5; AC_B=2` | `AC_ADDRESS_AB` = `52` | `7154` → `7160` |
| `7154` | `AC_A=5; AC_B=3` | `AC_ADDRESS_AB` = `53` | `7154` → `7160` |
| `7154` | `AC_A=5; AC_B=4` | `AC_ADDRESS_AB` = `54` | `7154` → `7160` |
| `7154` | `AC_A=5; AC_B=5` | `AC_ADDRESS_AB` = `55` | `7154` → `7160` |
| `7154` | `AC_A=5; AC_B=6` | `AC_ADDRESS_AB` = `56` | `7154` → `7160` |
| `7154` | `AC_A=5; AC_B=7` | `AC_ADDRESS_AB` = `57` | `7154` → `7160` |
| `7154` | `AC_A=5; AC_B=8` | `AC_ADDRESS_AB` = `58` | `7154` → `7160` |
| `7154` | `AC_A=5; AC_B=9` | `AC_ADDRESS_AB` = `59` | `7154` → `7160` |
| `7154` | `AC_A=6; AC_B=0` | `AC_ADDRESS_AB` = `60` | `7154` → `7161` |
| `7154` | `AC_A=6; AC_B=1` | `AC_ADDRESS_AB` = `61` | `7154` → `7161` |
| `7154` | `AC_A=6; AC_B=2` | `AC_ADDRESS_AB` = `62` | `7154` → `7161` |
| `7154` | `AC_A=6; AC_B=3` | `AC_ADDRESS_AB` = `63` | `7154` → `7161` |
| `7154` | `AC_A=6; AC_B=4` | `AC_ADDRESS_AB` = `64` | `7154` → `7161` |
| `7154` | `AC_A=6; AC_B=5` | `AC_ADDRESS_AB` = `65` | `7154` → `7161` |
| `7154` | `AC_A=6; AC_B=6` | `AC_ADDRESS_AB` = `66` | `7154` → `7161` |
| `7154` | `AC_A=6; AC_B=7` | `AC_ADDRESS_AB` = `67` | `7154` → `7161` |
| `7154` | `AC_A=6; AC_B=8` | `AC_ADDRESS_AB` = `68` | `7154` → `7161` |
| `7154` | `AC_A=6; AC_B=9` | `AC_ADDRESS_AB` = `69` | `7154` → `7161` |
| `7154` | `AC_A=7; AC_B=0` | `AC_ADDRESS_AB` = `70` | `7154` → `7162` |
| `7154` | `AC_A=7; AC_B=1` | `AC_ADDRESS_AB` = `71` | `7154` → `7162` |
| `7154` | `AC_A=7; AC_B=2` | `AC_ADDRESS_AB` = `72` | `7154` → `7162` |
| `7154` | `AC_A=7; AC_B=3` | `AC_ADDRESS_AB` = `73` | `7154` → `7162` |
| `7154` | `AC_A=7; AC_B=4` | `AC_ADDRESS_AB` = `74` | `7154` → `7162` |
| `7154` | `AC_A=7; AC_B=5` | `AC_ADDRESS_AB` = `75` | `7154` → `7162` |
| `7154` | `AC_A=7; AC_B=6` | `AC_ADDRESS_AB` = `76` | `7154` → `7162` |
| `7154` | `AC_A=7; AC_B=7` | `AC_ADDRESS_AB` = `77` | `7154` → `7162` |
| `7154` | `AC_A=7; AC_B=8` | `AC_ADDRESS_AB` = `78` | `7154` → `7162` |
| `7154` | `AC_A=7; AC_B=9` | `AC_ADDRESS_AB` = `79` | `7154` → `7162` |
| `7154` | `AC_A=8; AC_B=0` | `AC_ADDRESS_AB` = `80` | `7154` → `7163` |
| `7154` | `AC_A=8; AC_B=1` | `AC_ADDRESS_AB` = `81` | `7154` → `7163` |
| `7154` | `AC_A=8; AC_B=2` | `AC_ADDRESS_AB` = `82` | `7154` → `7163` |
| `7154` | `AC_A=8; AC_B=3` | `AC_ADDRESS_AB` = `83` | `7154` → `7163` |
| `7154` | `AC_A=8; AC_B=4` | `AC_ADDRESS_AB` = `84` | `7154` → `7163` |
| `7154` | `AC_A=8; AC_B=5` | `AC_ADDRESS_AB` = `85` | `7154` → `7163` |
| `7154` | `AC_A=8; AC_B=6` | `AC_ADDRESS_AB` = `86` | `7154` → `7163` |
| `7154` | `AC_A=8; AC_B=7` | `AC_ADDRESS_AB` = `87` | `7154` → `7163` |
| `7154` | `AC_A=8; AC_B=8` | `AC_ADDRESS_AB` = `88` | `7154` → `7163` |
| `7154` | `AC_A=8; AC_B=9` | `AC_ADDRESS_AB` = `89` | `7154` → `7163` |
| `7154` | `AC_A=9; AC_B=0` | `AC_ADDRESS_AB` = `90` | `7154` → `7164` |
| `7154` | `AC_A=9; AC_B=1` | `AC_ADDRESS_AB` = `91` | `7154` → `7164` |
| `7154` | `AC_A=9; AC_B=2` | `AC_ADDRESS_AB` = `92` | `7154` → `7164` |
| `7154` | `AC_A=9; AC_B=3` | `AC_ADDRESS_AB` = `93` | `7154` → `7164` |
| `7154` | `AC_A=9; AC_B=4` | `AC_ADDRESS_AB` = `94` | `7154` → `7164` |
| `7154` | `AC_A=9; AC_B=5` | `AC_ADDRESS_AB` = `95` | `7154` → `7164` |
| `7154` | `AC_A=9; AC_B=6` | `AC_ADDRESS_AB` = `96` | `7154` → `7164` |
| `7154` | `AC_A=9; AC_B=7` | `AC_ADDRESS_AB` = `97` | `7154` → `7164` |
| `7154` | `AC_A=9; AC_B=8` | `AC_ADDRESS_AB` = `98` | `7154` → `7164` |
| `7154` | `AC_A=9; AC_B=9` | `AC_ADDRESS_AB` = `99` | `7154` → `7164` |
| `7166` | `AC_M=0` | `MODE_AC_SFERA` = `0` | `7166` |
| `7166` | `AC_M=2` | `MODE_AC_SFERA` = `2` | `7166` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `0` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Catalogue Object / role | Applicability | Evidence |
| --- | --- | --- |
| `481` - Keypad as Sfera access control module | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `480` - Keypad as Sfera video door entry module | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `481` - Keypad as Sfera access control module | Access control | `8` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `480` - Keypad as Sfera video door entry module | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| `481` | [Access control](../../functional/who-23-access-control/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

In standalone use A/B/C assigns address `000..999` and T selects local relay time. In Sfera use A/B/C is normally unused; `M=0` releases the speaker lock, `M=3` also controls the local second lock with fixed 4 s delay. Add 20 for direct-call modes: `M=20/23`, with B/C giving the riser `01..39` where applicable. Access-control `M=2` and `M=22` are separate centrally managed roles; `M=22` is excluded on risers. The installation manual separates administrator, passepartout and resident-code management from relay timing. Codes must be enrolled with the appropriate administrator context; direct calling uses the resident address and confirmation. Local reset / deletion procedures can remove multiple records; do not interpret a reset as deletion of only one code. TiSferaDesign supplies named-device settings and address-book association. The user manual gives opening codes of `4..9` digits and direct-call addresses `0..3999`, with up to 20 administrator, 100 passepartout and 4000 resident codes; the resident procedure explicitly requires compatible speaker and pushbutton modules. A shorter-than-maximum opening code needs confirmation, while full-length completion follows the illustrated role-specific sequence. A power-on reset with the programming button held deletes all stored codes and restores defaults; the manual requires a one-minute wait before reprogramming a paired speaker / keypad installation.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

### Manufacturer credential and commissioning settings

| Setting / action | Documented behavior / boundary | Evidence |
| --- | --- | --- |
| Local relay timer T | 0 (absent): 4 s; 1: 1 s; 2: 10 s; 3: 20 s; 4: 40 s; 5: 60 s; 6: 90 s; 7: 180 s. Applies to standalone local relay; integrated speaker timing is a separate setting. | `ST-00000684-EN.pdf` p. 2 |
| PC connection | Powered module for update; mini-USB/USB, virtual COM port. Transfer and firmware update are separate operations; offline project composition does not prove connection. | `RA00176AC_S_EN.pdf` pp. 6-9; exact user manual final configuration page |
| PC auxiliary-button setting | Standalone software can enable the additional lock-release pushbutton. BP_AC_SFERA also contains tamper candidates, while CP-P2 is marked future application in the instruction; no operational tamper feature is established. | `RA00176AC_S_EN.pdf` p. 17; `O1688A.pdf` p. 1 |
| Address book / transfer | Contacts belong to houses, buildings or residential complexes; device transfer accepts contacts from one group. Import .csv/.txt and export .csv; received device contacts form a new group and update existing entries. Contact fields include name, handset address, call code, B/F/A, ringtone, householder/guest/private flags and hidden-code confirmation. Display-only fields do not become reader hardware functions. | `RA00176AC_S_EN.pdf` pp. 22-29, 35, 38-41 |
| Credential roles in software | Manager credentials program but do not unlock; passepartout and residents unlock but do not program. Duplicate badge assignments block configuration sending; badge acquisition uses a reader attached to the PC. | `RA00176AC_S_EN.pdf` pp. 30-34 |
| Opening sequence | Standalone relay or integrated speaker lock: lock key, code, then lock key to confirm when shorter than the configured maximum; a full-length code completes without the final confirmation. Integrated second lock: two lock-key presses before code, with the same short/full-length rule; requires `M=3` or `M=23` and has fixed 4 s local relay timing. | `RA00177AC_EN.pdf` p. 12, visually checked illustrated table |
| Direct call | `1..4`-digit internal-unit address `0..3999` followed by the call key. The local-mode illustration requires `M=20` or `M=23`; central `M=22` is a separate software/technical-sheet mode. | `RA00177AC_EN.pdf` p. 13; `RA00176AC_S_EN.pdf` p. 16 |
| PC modes and code length | Integrated `M=0/2/3/20/22/23`. Central `M=2/22` disables keypad and speaker relays and uses the central unit contact; its address book is managed centrally. `M=22` calling is unavailable on risers. Standalone software offers `M=0/2`. Maximum code length `4..9`, default 9. | `RA00176AC_S_EN.pdf` pp. 15-17 |
| Administrator / passepartout | 20 administrator codes, programming rights only; 100 passepartout codes, access only. Administrator enrolment starts at the concealed programming button and requires code confirmation. Passepartout enrolment requires an administrator. | `RA00177AC_EN.pdf` pp. 14-20 |
| Resident codes | Up to 4000, one per apartment. Local enrolment and deletion select the apartment using compatible speaker and 352000/352100 call-button modules. Display-linked programming is referred to the 352500 manual; standalone resident capability is not inferred from aggregate capacity. | `RA00177AC_EN.pdf` pp. 12, 24-28 |
| Timing / deletion boundaries | Programming starts within 30 s and key presses are no more than 2 s apart. Hold programming button through long beep at 10 s to erase all administrators; selective deletion uses software. Enter administrator three times to erase all passepartout codes (p. 21 heading incorrectly says administrators). Resident deletion confirms the selected apartment using the administrator again. | `RA00177AC_EN.pdf` pp. 16-17, 20-21, 27-28 |
| Replacement / complete reset | The code-replacement key begins replacement of an existing passepartout/resident code, followed by old code, new code and confirmation. Power-on reset while holding programming button erases all stored codes and restores defaults; red LED lasts 4 s. Wait at least 1 minute before reprogramming a paired speaker/keypad installation. | `RA00177AC_EN.pdf` pp. 22-23, 29-31 |

## Source reconciliation

The exact sheet distinguishes local relay C/NC/NO from the speaker module’s 18 V lock output; neither rating is substituted for the other. The current manual and AC software manual add role-specific code and direct-call procedures, while French HEXACT/Vigik modes remain market-scoped. Database video-entry and access-control Objects 480/481 are alternate roles. The current export reports product classification separately from technical-sheet configuration and does not establish firmware parity across the three database releases.

### Source-specific operating boundaries

The firmware AC_M domain is only 0 or 2 on all three catalogue releases, although manufacturer software and physical instructions describe integrated 3/20/22/23 as well. These missing mode values are a catalogue coverage limit, not a reason to discard the manufacturer instructions.

Conditions 4925/4926 have no textual selection predicate; fixed placement does not establish priority. Rule `7154` combines AC_A and AC_B through 100 branches into AC_ADDRESS_AB=`0..99` for access-control Object `481`, although that Object has no reusable AC_ADDRESS_AB field; those fields belong to Object `480`. Rule `7166` maps `AC_M=0/2` to MODE_AC_SFERA for Object `480`. This target-field asymmetry remains unresolved. Neither referenced rule supplies a conversion for AC_C or relay timing. Catalogue relay default 255 means RELAY_OFF, whereas the physical absent-T selector means 4 s; these are different source scopes.

English p. 21 has an administrator-deletion heading over a procedure that deletes passepartout codes; the action text governs the description. In the 2024 software central modes, both local relays are disabled; the 2020 physical sheet says central timing controls the relay. Do not combine these into an unqualified local-relay operation. AA/AC software revisions agree on reviewed local modes and credential roles; their exact binary payloads are not inspected.

## Evidence limits and open work

Installed code capacity by firmware, software-file storage / transfer encoding, French access-control integration and observed reset / call / relay behavior remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Discovered sources outside this review

These publisher-linked files were identified but are not used as retained evidence in this dossier. Firmware / installers and declarations remain separate evidence families. A listed URL does not establish payload identity, installed release or tested compatibility.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `LGRP-01976-V01.01-EN.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/LGRP-01976-V01.01-EN.pdf) |
| `Sfera.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Sfera.pdf) |
| `Sfera2011Keypad_04_00_01.fwz` | Firmware binary: payload, production / update applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/Sfera2011Keypad_04_00_01.fwz) |
| `TiSferaDesign_040024.exe` | Software installer: payload / installed compatibility unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/TiSferaDesign_040024.exe) |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0161-0170-2026-10-07.md#own-dev-0169)
