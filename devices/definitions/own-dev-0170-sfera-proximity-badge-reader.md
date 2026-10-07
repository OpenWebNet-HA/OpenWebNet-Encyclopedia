# Sfera proximity badge reader

## Summary

353200 is a Sfera RFID reader that unlocks a door when an enrolled badge is presented. It supports resident, apartment-master, manager and passepartout badges, with local or software administration. It can use the entrance-panel lock or its own relay in a standalone installation.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0170` | Project identity |
| Technical description | Sfera proximity badge reader | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `353200` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1471` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Access control | Main system association |
| Item model / `modobj` | `1` | Main association; independent of project ID |
| Firmware definition | `117`, `581`, `734` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Audio video, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Sfera | `353200` | Established catalogue identity | Manufacturer database commercial record `1471` explicitly links this SKU to item `1471` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `353200` | `8005543457580` | [353200-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/7e/da/7edac414e7cccd9c606d58a2545d7d210c2941b24561025540922aba3bc4faf3.pdf) PDF p. 1; `353200-italian-product-sheet.pdf` PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `353200` | Proximity reader module | Canonical commercial record `1471` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `RA00176AA_S_EN.pdf` | Technical Guide RA00176AA_S_EN | RA00176AA_S_EN; printed publication date not established | Earlier TiSferaDesign manual: PDF pp.6-14, 18-19, 22-35, compared against AC revision for applicable settings. Unrelated module settings outside this item. | [Archived original](https://archive.openwebnet-ha.org/sha256/14/14/1414875a0d40523aafb77d2f4947f60475d4dc1be6a27825883b0137b639d97f.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00176AA_S_EN.pdf) |
| `O1690D.pdf` | Instruction Use O1690D | O1690D; printed publication date not established | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/19/bf/19bff3e4b870837cc5848079cc9714faad45a919077a9d61fa7186aaadd2474e.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/O1690D.pdf) |
| `RA00179AA_EN.pdf` | Technical Guide RA00179AA_EN | RA00179AA_EN; printed publication date not established | 353200: printed/PDF pp. 6-7, 12-29; manager / apartment / resident / passepartout badges, configuration, deletion and reset. USB transfer/update is on p.29. | [Archived original](https://archive.openwebnet-ha.org/sha256/55/65/5565fbf438bfc4e8e3a53524d98db3816c72a451b422ca06a5bbe8cf42d860bb.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00179AA_EN.pdf) |
| `ST-00000960-EN.pdf` | Technical Sheet ST-00000960-EN | ST-00000960-EN; 03/09/2021 | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/f3/a8/f3a8fcc9927c7866ecad96dee751061fc3f75988bafceffdb6026a9d1112826e.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000960-EN.pdf) |
| `353200-publisher-product-sheet.pdf` | Exact English product export | Publisher DATASHEET; 05.10.2026 | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/7e/da/7edac414e7cccd9c606d58a2545d7d210c2941b24561025540922aba3bc4faf3.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-353200&include_technical=1) |
| `353200-italian-product-sheet.pdf` | Exact Italian product export | Product export retrieved 05/10/2026; boilerplate compliance dates are not product publication dates | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/f8/fb/f8fbbf2924f811c94a88cb3f36f5bc2e39e451ef272b8476923265840a96b93c.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-353200) |
| `RA00176AC_S_IT.pdf` | Manufacturer Italian / installation document | RA00176AC-03/24-PC; printed revision label | TiSferaDesign 2024: applicable reader pp.18-19 and credential/address-book sections pp.22-35; selected Italian mode/role cross-checks. Remaining UI walkthroughs not independently translated. | [Archived original](https://archive.openwebnet-ha.org/sha256/23/78/237891b468a5152361ad36fd432ebd52e8804aecbfb2373a0c953dd7cc98eb8b.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00176AC_S_IT.pdf) |
| `RA00179AA_IT.pdf` | Manufacturer Italian / installation document | RA00179AA_IT; printed publication date not established | 353200: printed/PDF pp. 6-7, 12-28; manager / apartment / resident / passepartout badges, configuration, deletion and reset. | [Archived original](https://archive.openwebnet-ha.org/sha256/8e/f4/8ef4d957f4e3eeb40e696321edce4580188dfc35ca7a7b86e4c54135d464d0ca.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00179AA_IT.pdf) |
| `ST_00000960_IT.pdf` | Manufacturer Italian / installation document | ST_00000960_IT; 03/09/2021 | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/85/22/8522e091fe8cc6f8a7e518ac6f156eedf5ce90928dbd3cd8593e4081a2e8731d.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000960_IT.pdf) |
| `TisferaDesign_README_v4.pdf` | Software TISFERADESIGN_README_V4 | TisferaDesign_README_v4; 14/05/2026 | PDF pp. 1-1: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/52/48/52481f4b2cb9999abf86bb870007398845f3f29a7a52fb475dbf90a880d31f65.pdf) | [Publisher original](https://assets.legrand.com/pim/AUTRE/TisferaDesign_README_v4.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1471`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `RA00176AC_S_EN.pdf` | TiSferaDesign software manual | RA00176AC; 03/24-PC | PDF pp. 6-9, 18-19, 22-35, 38-41: powered transfer, reader modes and badge/address-book management; compared with AA revision. Display settings are outside this reader. | [Archived original](https://archive.openwebnet-ha.org/sha256/7c/63/7c634fb15eebc8b90bef803b80677c9b638317d9a88c71679eece9581a796ff9.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/RA00176AC_S_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..27 Vdc` | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28 |
| Standby, backlight off / on | `75 mA / 85 mA` | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28 |
| Maximum draw | `105 mA` | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28 |
| Temperature / assembled protection | `-25..70 °C; IP54` | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28 |
| Face dimensions | `115 x 91 mm` | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28 |
| Badge technology / capacity | `Mifare Classic 1K; up to 20000 resident badges` | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28 |
| Hierarchy limits | `20 manager-master; 100 passepartout; 4000 apartment-master; 5 resident badges per apartment` | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28 |
| Relay contacts | `8 A at 30 Vdc or 30 Vac cos phi 1; 3.5 A at 30 Vac cos phi 0.4` | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28 |
| Local interface | `green granted / red denied LEDs; reset pushbutton; front mini-USB; CP/P1/P2 inputs` | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Model | `Control module` | `353200-publisher-product-sheet.pdf` PDF p. 2 |
| Installation technique | `Bus system` | `353200-publisher-product-sheet.pdf` PDF p. 2 |
| Width | `91 mm` | `353200-publisher-product-sheet.pdf` PDF p. 2 |
| Height | `115 mm` | `353200-publisher-product-sheet.pdf` PDF p. 2 |
| Depth | `27 mm` | `353200-publisher-product-sheet.pdf` PDF p. 2 |
| Number of call buttons | `0` | `353200-publisher-product-sheet.pdf` PDF p. 2 |
| Colour | `Other` | `353200-publisher-product-sheet.pdf` PDF p. 2 |
| Connected object | `No` | `353200-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1471` | Canonical catalogue |
| Technical item description | Proximity reader module | Canonical catalogue |
| Item family | Device for Access Control system; key `101` | Canonical catalogue |
| Main system | Access control; key `8` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `1` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Access control | `1` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `117` | `1` | `4` | `3` | `1` | Catalogue default | Official |
| `581` | `2` | `0` | `15` | `1` | Not catalogue default | Official |
| `734` | `2` | `1` | `11` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `117` | `201` | BTicino (key `1`) | `7` | external software | `TiSferaDesign_0102` |
| `581` | `627` | BTicino (key `1`) | `7` | external software | `TiSferaDesign_0200` |
| `734` | `1029` | BTicino (key `1`) | `7` | external software | `TiSferaDesign_0300` |

All 3 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `117` | `1` | `482` Transponder reader as Sfera VDE module | Candidate alternative | `2293` | `517` | `971` |
| `117` | `1` | `483` Proximity reader as Sfera access conrol module | Fixed / designated metadata | `2348` | `518` | `1003` |
| `581` | `1` | `482` Transponder reader as Sfera VDE module | Candidate alternative | `2369` | `517` | `1024` |
| `581` | `1` | `483` Proximity reader as Sfera access conrol module | Fixed / designated metadata | `2370` | `518` | `1025` |
| `734` | `1` | `482` Transponder reader as Sfera VDE module | Candidate alternative | `2664` | `517` | `1274` |
| `734` | `1` | `483` Proximity reader as Sfera access conrol module | Fixed / designated metadata | `2665` | `518` | `1275` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `117` | Product Programming | `3` | Canonical firmware/mode association |
| `581` | Product Programming | `3` | Canonical firmware/mode association |
| `734` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `117` | USB | Canonical firmware/connection association |
| `581` | USB | Canonical firmware/connection association |
| `734` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `M=0 / M=1` | Local manager administration / apartment-master administration; apartment master enrols its apartment residents and does not unlock the door | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `M=2, software` | Central badge management, address-book managed by SCS access-control system; central A/B and reader C fields | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Standalone A+B+C / T` | Address `000..999`; local relay timer | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Standalone T=0 /1 /2 /3 /4 /5 /6 /7` | Absent=4 s; 1 s; 10 s; 20 s; 40 s; 60 s; 90 s; 180 s | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Sfera A/B/C / T` | Unused in ordinary speaker-integrated wiring; speaker T determines lock timing | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Resident / apartment capacities` | Up to 4000 apartments, 5 resident badges each, 20000 residents total | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Manager / passepartout capacities` | 20 system-manager badges; 100 passepartout badges; separate from resident total | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Manager enrolment` | Rear programming button; green LED / beep; present manager badge within 30 s | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Manager erase / selective delete` | Rear button hold 10 s erases all managers; selective deletion through software | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Pass/apartment erase` | Present manager three times then wait 5 s in documented procedure; erases all passepartout and apartment-master badges | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Resident deletion with M=1` | Use TiSferaDesign; apartment master is an enrolment credential, not door-release authorization | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |
| `Integrated cable order` | First device on multicable after speaker/A/V module, before pushbutton modules; physical panel position may differ; do not connect reader BUS in illustrated integrated wiring | `ST-00000960-EN` printed/PDF pp. 1-3; `RA00179AA_EN` pp. 12-28; `RA00176AC_S_EN` pp. 18-19 |

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
| `117` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `117` | `AC_A` | `0..9` | `0` | A; local address hundreds configurator |
| `117` | `AC_B` | `0..9` | `0` | B; local address tenths configurator |
| `117` | `AC_C` | `0..9` | `0` | C; local address units configurator |
| `117` | `AC_M` | `0..2` | `0` | M; operating mode configurator |
| `117` | `AC_T` | `0..7` | `0` | T; local relay timing |
| `581` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `581` | `AC_A` | `0..9` | `0` | A; local address hundreds configurator |
| `581` | `AC_B` | `0..9` | `0` | B; local address tenths configurator |
| `581` | `AC_C` | `0..9` | `0` | C; local address units configurator |
| `581` | `AC_M` | `0..2` | `0` | M; operating mode configurator Local management main master only: 0) (Local management apt masters: 1) (Remote management: 2 |
| `581` | `AC_T` | `0..7` | `0` | T; local relay timing |
| `734` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `734` | `AC_A` | `0..9` | `0` | A; local address hundreds configurator |
| `734` | `AC_B` | `0..9` | `0` | B; local address tenths configurator |
| `734` | `AC_C` | `0..9` | `0` | C; local address units configurator |
| `734` | `AC_M` | `0..2` | `0` | M; operating mode configurator Local management main master only: 0) (Local management apt masters: 1) (Remote management: 2 |
| `734` | `AC_T` | `0..7` | `0` | T; local relay timing |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `482` - Transponder reader as Sfera VDE module

Catalogue Object key `517` maps to external Object `482`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_AC_SFERA` | `0` = LED_OFF; `1` = LED_ON; `2` = LED_ONLY_ERRORS | `0` | Led behaviour in Sfera access control modules |
| `BUZZER_AC_SFERA` | `0` = BUZZER_OFF; `1` = BUZZER_ON; `2` = BUZZER_ONLY_PRESSIONS | `0` | Buzzer behaviour in Sfera access control modules |
| `RELAY_TIME_AC_SFERA` | `255` = RELAY_OFF; `1` = RELAY_1S; `0` = RELAY_4S; `2` = RELAY_10S; `3` = RELAY_20S; `4` = RELAY_40S; `5` = RELAY_60S; `6` = RELAY_90S; `7` = RELAY_180S | `255` | Relay timings for Sfera access control modules |
| `BP_AC_SFERA` | `0` = BP_AS_BUTTON; `1` = BP_AS_TAMPER; `2` = BP_AS_NOTHING; `3` = BP_AND_TAMPER | `0` | Bp button behaviour in Sfera access control modules |
| `MODE_AC_SFERA` | `0` = SAVE_RESID; `1` = SAVE_APT_MASTER; `2` = AC_READER | `0` | Operating modes for Sfera access control modules |
| `AC_ADDRESS_AB` | `0..99` | `0` | "AB" side of access control device address |
| `AC_ADDRESS_C` | `0..9` | `0` | "C" side of access control device address |

### Object `483` - Proximity reader as Sfera access conrol module

Catalogue Object key `518` maps to external Object `483`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_AC_SFERA` | `0` = LED_OFF; `1` = LED_ON; `2` = LED_ONLY_ERRORS | `0` | Led behaviour in Sfera access control modules |
| `BUZZER_AC_SFERA` | `0` = BUZZER_OFF; `1` = BUZZER_ON; `2` = BUZZER_ONLY_PRESSIONS | `0` | Buzzer behaviour in Sfera access control modules |
| `RELAY_TIME_AC_SFERA` | `255` = RELAY_OFF; `1` = RELAY_1S; `0` = RELAY_4S; `2` = RELAY_10S; `3` = RELAY_20S; `4` = RELAY_40S; `5` = RELAY_60S; `6` = RELAY_90S; `7` = RELAY_180S | `255` | Relay timings for Sfera access control modules |
| `BP_AC_SFERA` | `0` = BP_AS_BUTTON; `1` = BP_AS_TAMPER; `2` = BP_AS_NOTHING; `3` = BP_AND_TAMPER | `0` | Bp button behaviour in Sfera access control modules |
| `MODE_AC_SFERA` | `0` = SAVE_RESID; `1` = SAVE_APT_MASTER; `2` = AC_READER | `0` | Operating modes for Sfera access control modules |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `117` | `1` | `482` | `4927` | No textual predicate stored | `7190` |
| `117` | `1` | `483` | `4928` | No textual predicate stored | `7178` |
| `581` | `1` | `482` | `4927` | No textual predicate stored | `7190` |
| `581` | `1` | `483` | `4928` | No textual predicate stored | `7178` |
| `734` | `1` | `482` | `4927` | No textual predicate stored | `7190` |
| `734` | `1` | `483` | `4928` | No textual predicate stored | `7178` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `117` | `482` | `1803` | `AC_ADDRESS_AB` | `0..99` (entire reusable range retained) | `0` | "AB" side of access control device address |
| `117` | `482` | `1804` | `AC_ADDRESS_C` | `0..9` (entire reusable range retained) | `0` | "C" side of access control device address |
| `581` | `482` | `1817` | `AC_ADDRESS_AB` | `0..99` (entire reusable range retained) | `0` | "AB" side of access control device address |
| `581` | `482` | `1818` | `AC_ADDRESS_C` | `0..9` (entire reusable range retained) | `0` | "C" side of access control device address |
| `734` | `482` | `2998` | `AC_ADDRESS_AB` | `0..99` (entire reusable range retained) | `0` | "AB" side of access control device address |
| `734` | `482` | `2999` | `AC_ADDRESS_C` | `0..9` (entire reusable range retained) | `0` | "C" side of access control device address |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7178` | `AC_A=0; AC_B=0` | `AC_ADDRESS_AB` = `0` | `7178` → `7179` |
| `7178` | `AC_A=0; AC_B=1` | `AC_ADDRESS_AB` = `1` | `7178` → `7179` |
| `7178` | `AC_A=0; AC_B=2` | `AC_ADDRESS_AB` = `2` | `7178` → `7179` |
| `7178` | `AC_A=0; AC_B=3` | `AC_ADDRESS_AB` = `3` | `7178` → `7179` |
| `7178` | `AC_A=0; AC_B=4` | `AC_ADDRESS_AB` = `4` | `7178` → `7179` |
| `7178` | `AC_A=0; AC_B=5` | `AC_ADDRESS_AB` = `5` | `7178` → `7179` |
| `7178` | `AC_A=0; AC_B=6` | `AC_ADDRESS_AB` = `6` | `7178` → `7179` |
| `7178` | `AC_A=0; AC_B=7` | `AC_ADDRESS_AB` = `7` | `7178` → `7179` |
| `7178` | `AC_A=0; AC_B=8` | `AC_ADDRESS_AB` = `8` | `7178` → `7179` |
| `7178` | `AC_A=0; AC_B=9` | `AC_ADDRESS_AB` = `9` | `7178` → `7179` |
| `7178` | `AC_A=1; AC_B=0` | `AC_ADDRESS_AB` = `10` | `7178` → `7180` |
| `7178` | `AC_A=1; AC_B=1` | `AC_ADDRESS_AB` = `11` | `7178` → `7180` |
| `7178` | `AC_A=1; AC_B=2` | `AC_ADDRESS_AB` = `12` | `7178` → `7180` |
| `7178` | `AC_A=1; AC_B=3` | `AC_ADDRESS_AB` = `13` | `7178` → `7180` |
| `7178` | `AC_A=1; AC_B=4` | `AC_ADDRESS_AB` = `14` | `7178` → `7180` |
| `7178` | `AC_A=1; AC_B=5` | `AC_ADDRESS_AB` = `15` | `7178` → `7180` |
| `7178` | `AC_A=1; AC_B=6` | `AC_ADDRESS_AB` = `16` | `7178` → `7180` |
| `7178` | `AC_A=1; AC_B=7` | `AC_ADDRESS_AB` = `17` | `7178` → `7180` |
| `7178` | `AC_A=1; AC_B=8` | `AC_ADDRESS_AB` = `18` | `7178` → `7180` |
| `7178` | `AC_A=1; AC_B=9` | `AC_ADDRESS_AB` = `19` | `7178` → `7180` |
| `7178` | `AC_A=2; AC_B=0` | `AC_ADDRESS_AB` = `20` | `7178` → `7181` |
| `7178` | `AC_A=2; AC_B=1` | `AC_ADDRESS_AB` = `21` | `7178` → `7181` |
| `7178` | `AC_A=2; AC_B=2` | `AC_ADDRESS_AB` = `22` | `7178` → `7181` |
| `7178` | `AC_A=2; AC_B=3` | `AC_ADDRESS_AB` = `23` | `7178` → `7181` |
| `7178` | `AC_A=2; AC_B=4` | `AC_ADDRESS_AB` = `24` | `7178` → `7181` |
| `7178` | `AC_A=2; AC_B=5` | `AC_ADDRESS_AB` = `25` | `7178` → `7181` |
| `7178` | `AC_A=2; AC_B=6` | `AC_ADDRESS_AB` = `26` | `7178` → `7181` |
| `7178` | `AC_A=2; AC_B=7` | `AC_ADDRESS_AB` = `27` | `7178` → `7181` |
| `7178` | `AC_A=2; AC_B=8` | `AC_ADDRESS_AB` = `28` | `7178` → `7181` |
| `7178` | `AC_A=2; AC_B=9` | `AC_ADDRESS_AB` = `29` | `7178` → `7181` |
| `7178` | `AC_A=3; AC_B=0` | `AC_ADDRESS_AB` = `30` | `7178` → `7182` |
| `7178` | `AC_A=3; AC_B=1` | `AC_ADDRESS_AB` = `31` | `7178` → `7182` |
| `7178` | `AC_A=3; AC_B=2` | `AC_ADDRESS_AB` = `32` | `7178` → `7182` |
| `7178` | `AC_A=3; AC_B=3` | `AC_ADDRESS_AB` = `33` | `7178` → `7182` |
| `7178` | `AC_A=3; AC_B=4` | `AC_ADDRESS_AB` = `34` | `7178` → `7182` |
| `7178` | `AC_A=3; AC_B=5` | `AC_ADDRESS_AB` = `35` | `7178` → `7182` |
| `7178` | `AC_A=3; AC_B=6` | `AC_ADDRESS_AB` = `36` | `7178` → `7182` |
| `7178` | `AC_A=3; AC_B=7` | `AC_ADDRESS_AB` = `37` | `7178` → `7182` |
| `7178` | `AC_A=3; AC_B=8` | `AC_ADDRESS_AB` = `38` | `7178` → `7182` |
| `7178` | `AC_A=3; AC_B=9` | `AC_ADDRESS_AB` = `39` | `7178` → `7182` |
| `7178` | `AC_A=4; AC_B=0` | `AC_ADDRESS_AB` = `40` | `7178` → `7183` |
| `7178` | `AC_A=4; AC_B=1` | `AC_ADDRESS_AB` = `41` | `7178` → `7183` |
| `7178` | `AC_A=4; AC_B=2` | `AC_ADDRESS_AB` = `42` | `7178` → `7183` |
| `7178` | `AC_A=4; AC_B=3` | `AC_ADDRESS_AB` = `43` | `7178` → `7183` |
| `7178` | `AC_A=4; AC_B=4` | `AC_ADDRESS_AB` = `44` | `7178` → `7183` |
| `7178` | `AC_A=4; AC_B=5` | `AC_ADDRESS_AB` = `45` | `7178` → `7183` |
| `7178` | `AC_A=4; AC_B=6` | `AC_ADDRESS_AB` = `46` | `7178` → `7183` |
| `7178` | `AC_A=4; AC_B=7` | `AC_ADDRESS_AB` = `47` | `7178` → `7183` |
| `7178` | `AC_A=4; AC_B=8` | `AC_ADDRESS_AB` = `48` | `7178` → `7183` |
| `7178` | `AC_A=4; AC_B=9` | `AC_ADDRESS_AB` = `49` | `7178` → `7183` |
| `7178` | `AC_A=5; AC_B=0` | `AC_ADDRESS_AB` = `50` | `7178` → `7184` |
| `7178` | `AC_A=5; AC_B=1` | `AC_ADDRESS_AB` = `51` | `7178` → `7184` |
| `7178` | `AC_A=5; AC_B=2` | `AC_ADDRESS_AB` = `52` | `7178` → `7184` |
| `7178` | `AC_A=5; AC_B=3` | `AC_ADDRESS_AB` = `53` | `7178` → `7184` |
| `7178` | `AC_A=5; AC_B=4` | `AC_ADDRESS_AB` = `54` | `7178` → `7184` |
| `7178` | `AC_A=5; AC_B=5` | `AC_ADDRESS_AB` = `55` | `7178` → `7184` |
| `7178` | `AC_A=5; AC_B=6` | `AC_ADDRESS_AB` = `56` | `7178` → `7184` |
| `7178` | `AC_A=5; AC_B=7` | `AC_ADDRESS_AB` = `57` | `7178` → `7184` |
| `7178` | `AC_A=5; AC_B=8` | `AC_ADDRESS_AB` = `58` | `7178` → `7184` |
| `7178` | `AC_A=5; AC_B=9` | `AC_ADDRESS_AB` = `59` | `7178` → `7184` |
| `7178` | `AC_A=6; AC_B=0` | `AC_ADDRESS_AB` = `60` | `7178` → `7185` |
| `7178` | `AC_A=6; AC_B=1` | `AC_ADDRESS_AB` = `61` | `7178` → `7185` |
| `7178` | `AC_A=6; AC_B=2` | `AC_ADDRESS_AB` = `62` | `7178` → `7185` |
| `7178` | `AC_A=6; AC_B=3` | `AC_ADDRESS_AB` = `63` | `7178` → `7185` |
| `7178` | `AC_A=6; AC_B=4` | `AC_ADDRESS_AB` = `64` | `7178` → `7185` |
| `7178` | `AC_A=6; AC_B=5` | `AC_ADDRESS_AB` = `65` | `7178` → `7185` |
| `7178` | `AC_A=6; AC_B=6` | `AC_ADDRESS_AB` = `66` | `7178` → `7185` |
| `7178` | `AC_A=6; AC_B=7` | `AC_ADDRESS_AB` = `67` | `7178` → `7185` |
| `7178` | `AC_A=6; AC_B=8` | `AC_ADDRESS_AB` = `68` | `7178` → `7185` |
| `7178` | `AC_A=6; AC_B=9` | `AC_ADDRESS_AB` = `69` | `7178` → `7185` |
| `7178` | `AC_A=7; AC_B=0` | `AC_ADDRESS_AB` = `70` | `7178` → `7186` |
| `7178` | `AC_A=7; AC_B=1` | `AC_ADDRESS_AB` = `71` | `7178` → `7186` |
| `7178` | `AC_A=7; AC_B=2` | `AC_ADDRESS_AB` = `72` | `7178` → `7186` |
| `7178` | `AC_A=7; AC_B=3` | `AC_ADDRESS_AB` = `73` | `7178` → `7186` |
| `7178` | `AC_A=7; AC_B=4` | `AC_ADDRESS_AB` = `74` | `7178` → `7186` |
| `7178` | `AC_A=7; AC_B=5` | `AC_ADDRESS_AB` = `75` | `7178` → `7186` |
| `7178` | `AC_A=7; AC_B=6` | `AC_ADDRESS_AB` = `76` | `7178` → `7186` |
| `7178` | `AC_A=7; AC_B=7` | `AC_ADDRESS_AB` = `77` | `7178` → `7186` |
| `7178` | `AC_A=7; AC_B=8` | `AC_ADDRESS_AB` = `78` | `7178` → `7186` |
| `7178` | `AC_A=7; AC_B=9` | `AC_ADDRESS_AB` = `79` | `7178` → `7186` |
| `7178` | `AC_A=8; AC_B=0` | `AC_ADDRESS_AB` = `80` | `7178` → `7187` |
| `7178` | `AC_A=8; AC_B=1` | `AC_ADDRESS_AB` = `81` | `7178` → `7187` |
| `7178` | `AC_A=8; AC_B=2` | `AC_ADDRESS_AB` = `82` | `7178` → `7187` |
| `7178` | `AC_A=8; AC_B=3` | `AC_ADDRESS_AB` = `83` | `7178` → `7187` |
| `7178` | `AC_A=8; AC_B=4` | `AC_ADDRESS_AB` = `84` | `7178` → `7187` |
| `7178` | `AC_A=8; AC_B=5` | `AC_ADDRESS_AB` = `85` | `7178` → `7187` |
| `7178` | `AC_A=8; AC_B=6` | `AC_ADDRESS_AB` = `86` | `7178` → `7187` |
| `7178` | `AC_A=8; AC_B=7` | `AC_ADDRESS_AB` = `87` | `7178` → `7187` |
| `7178` | `AC_A=8; AC_B=8` | `AC_ADDRESS_AB` = `88` | `7178` → `7187` |
| `7178` | `AC_A=8; AC_B=9` | `AC_ADDRESS_AB` = `89` | `7178` → `7187` |
| `7178` | `AC_A=9; AC_B=0` | `AC_ADDRESS_AB` = `90` | `7178` → `7188` |
| `7178` | `AC_A=9; AC_B=1` | `AC_ADDRESS_AB` = `91` | `7178` → `7188` |
| `7178` | `AC_A=9; AC_B=2` | `AC_ADDRESS_AB` = `92` | `7178` → `7188` |
| `7178` | `AC_A=9; AC_B=3` | `AC_ADDRESS_AB` = `93` | `7178` → `7188` |
| `7178` | `AC_A=9; AC_B=4` | `AC_ADDRESS_AB` = `94` | `7178` → `7188` |
| `7178` | `AC_A=9; AC_B=5` | `AC_ADDRESS_AB` = `95` | `7178` → `7188` |
| `7178` | `AC_A=9; AC_B=6` | `AC_ADDRESS_AB` = `96` | `7178` → `7188` |
| `7178` | `AC_A=9; AC_B=7` | `AC_ADDRESS_AB` = `97` | `7178` → `7188` |
| `7178` | `AC_A=9; AC_B=8` | `AC_ADDRESS_AB` = `98` | `7178` → `7188` |
| `7178` | `AC_A=9; AC_B=9` | `AC_ADDRESS_AB` = `99` | `7178` → `7188` |
| `7190` | `AC_M=0` | `MODE_AC_SFERA` = `0` | `7190` |
| `7190` | `AC_M=1` | `MODE_AC_SFERA` = `1` | `7190` |
| `7190` | `AC_M=2` | `MODE_AC_SFERA` = `2` | `7190` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `1` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `483` - Proximity reader as Sfera access conrol module | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `482` - Transponder reader as Sfera VDE module | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `483` - Proximity reader as Sfera access conrol module | Access control | `8` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `482` - Transponder reader as Sfera VDE module | No stored Object-system association | Not applicable | Absence of this relation does not remove the explicit Firmware/Object association |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| `483` | [Access control](../../functional/who-23-access-control/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

`M=0` uses manager-master enrolment of residents; `M=1` adds apartment-master delegation. Standalone A/B/C is a progressive `000..999` address and T controls the local relay; when integrated with Sfera A/B/C and T are unused and speaker timing applies. The reader must be the first multicable device connected to the speaker/A/V module, ahead of pushbutton modules, regardless of its physical position in the panel. The illustrated integrated arrangement leaves the reader’s BUS terminals unconnected; standalone use supplies those terminals. Manager enrolment begins with the programming pushbutton and badge presentation, with a 30 s programming window. Holding the programming button to the long beep after ten seconds deletes all manager badges; selective deletion uses TiSferaDesign. In `M=1`, resident deletion requires software. The printed passepartout / apartment deletion procedures can erase entire groups and must be treated as such.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

### Manufacturer credential and commissioning settings

| Setting / action | Documented behavior / boundary | Evidence |
| --- | --- | --- |
| Local relay timer T | 0 (absent): 4 s; 1: 1 s; 2: 10 s; 3: 20 s; 4: 40 s; 5: 60 s; 6: 90 s; 7: 180 s. Applies to standalone local relay; integrated speaker timing is a separate setting. | `ST-00000960-EN.pdf` p. 2 |
| PC connection | Powered module for update; mini-USB/USB, virtual COM port. Transfer and firmware update are separate operations; offline project composition does not prove connection. | `RA00176AC_S_EN.pdf` pp. 6-9; exact user manual final configuration page |
| PC auxiliary-button setting | Standalone software can enable the additional lock-release pushbutton. BP_AC_SFERA also contains tamper candidates, while CP-P2 is marked future application in the instruction; no operational tamper feature is established. | `RA00176AC_S_EN.pdf` p. 19; `O1690D.pdf` p. 1 |
| Address book / transfer | Contacts belong to houses, buildings or residential complexes; device transfer accepts contacts from one group. Import .csv/.txt and export .csv; received device contacts form a new group and update existing entries. Contact fields include name, handset address, call code, B/F/A, ringtone, householder/guest/private flags and hidden-code confirmation. Display-only fields do not become reader hardware functions. | `RA00176AC_S_EN.pdf` pp. 22-29, 35, 38-41 |
| Credential roles in software | Manager credentials program but do not unlock; passepartout and residents unlock but do not program. Duplicate badge assignments block configuration sending; badge acquisition uses a reader attached to the PC. | `RA00176AC_S_EN.pdf` pp. 30-34 |
| PC modes | Integrated and standalone software offer `M=0` resident management, `M=1` apartment-master delegation and `M=2` centrally managed access. `M=2` exposes central A/B and reader C addresses; local address book is centrally managed. | `RA00176AC_S_EN.pdf` pp. 18-19 |
| Credential capacities / initial state | 20 manager masters, 100 passepartout, 4000 apartment masters and five resident badges per apartment (20000 resident badges). Reader has no preset badges on first power-up; these are source-documented capacities, not measured counts. | `ST-00000960-EN.pdf` pp. 1-2; `RA00179AA_EN.pdf` pp. 12-19 |
| Manager enrolment / deletion | Hold concealed programming button until flashing green LED/tone; register manager badges, up to 20. Start within 30 s; exit by short button press or timeout. Holding through long beep at 10 s deletes all manager badges; selective removal uses PC software. | `RA00179AA_EN.pdf` pp. 13-15 |
| Passepartout / apartment deletion | Manager enrols passepartout badges. Three successive manager presentations trigger deletion of both passepartout and apartment-master groups, not one badge; p. 18 includes a 5 s spacing instruction. The p. 25 apartment-deletion procedure does not repeat that spacing instruction. | `RA00179AA_EN.pdf` pp. 16-18, 23-25 |
| Resident enrolment / deletion | `M=0`: manager, selected apartment on call-button/display module, then up to five residents. Local deletion confirms selected apartment with the same manager; p. 22 says all stored residents, leaving apartment versus device-wide erasure scope unclear. `M=1`: apartment master enrols residents; resident deletion requires software. | `RA00179AA_EN.pdf` pp. 19-28 |
| Complete reset | With BUS off, hold programming button while restoring power through the extended beep; all saved badges/settings are erased, red LED steady for 4 s. This is separate from manager-only and passepartout/apartment group deletion. | `RA00179AA_EN.pdf` p. 28 |

## Source reconciliation

The 2021 sheet names Mifare Classic 1K and decomposes the 20000 resident capacity as 4000 apartments times five residents. The database’s generic proximity / transponder Objects do not imply support for arbitrary badge technologies. The sheet’s integrated `M=0` wiring note says “only” residents, although its hierarchy text also describes passepartout administration; the exact mode / firmware scope of that wording remains unresolved. A standalone drawing accidentally calls 353200 a keypad; the exact reference and reader terminals establish the badge-reader role. The 2026 export’s “non-connected” classification does not prevent configured SCS operation.

The 2024 software manual exposes central badge management `M=2` with controller and reader addresses beyond the local `M=0/1` technical-sheet description. This is software-revision evidence, not proof of central-mode support on every database Firmware. An apartment-master badge authorizes enrolment and does not itself open the lock.

### Source-specific operating boundaries

The multilingual O1690D instruction, dated 07/18-01 PC, prints working frequency as 13.56 NHz and transmission field strength below 42 dBµA/m at 10 m. NHz is retained as a source-unit irregularity, not silently converted into a verified MHz specification; the 2021 sheet identifies Mifare Classic 1K without resolving that printed unit. CP-P2 tamper is explicitly a future application despite reusable BP_AC_SFERA tamper enums.

Conditions 4927/4928 contain no textual predicate; no runtime selection priority is inferred. Rule `7178` generates AC_ADDRESS_AB through 100 AC_A/AC_B branches for Object `483`, but its reusable fields contain no AB/C address fields; these exist on Object `482`. Rule `7190` maps `AC_M=0/1/2` to MODE_AC_SFERA for Object `482`. The conversion target-field asymmetry and lack of AC_C/timer conversion are explicit catalogue limits. Local physical `T=0` means 4 s, whereas reusable relay default 255 means RELAY_OFF. The export swaps dimensional orientation (width 91 / height 115) against the technical drawing’s horizontal 115 / vertical 91; do not treat this as a hardware revision. AA/AC software agrees on the reviewed credential roles and `M=0/1/2` settings.

The user manual describes a selected-apartment deletion then says all resident badges are deleted; its exact erase scope is unresolved and is not presented as safe selective deletion.

## Evidence limits and open work

The integrated `M=0` passepartout wording, badge-type compatibility beyond Classic 1K, firmware-scoped capacities and observed group deletion / diagnostic responses remain open.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Discovered sources outside this review

These publisher-linked files were identified but are not used as retained evidence in this dossier. Firmware / installers and declarations remain separate evidence families. A listed URL does not establish payload identity, installed release or tested compatibility.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `LGEGXVAPVP.PDF` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/Certif/LGEGXVAPVP.PDF) |
| `LGRP-01976-V01.01-EN.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/LGRP-01976-V01.01-EN.pdf) |
| `Sfera.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Sfera.pdf) |
| `Sfera_2011Trasponder_020115.fwz` | Firmware binary: payload, production / update applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/Sfera_2011Trasponder_020115.fwz) |
| `TiSferaDesign_040024.exe` | Software installer: payload / installed compatibility unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/TiSferaDesign_040024.exe) |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0161-0170-2026-10-07.md#own-dev-0170)
