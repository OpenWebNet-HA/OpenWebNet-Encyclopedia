# Vigik single-door access-control unit

## Summary

348040 is a Vigik access controller for one door, supplied with a T25 reading head. It checks resident badges and service credentials, operates a door relay and can integrate with two-wire video entry; administration ranges from a master badge to a portable programmer or the ACWEB service.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0186` | Project identity |
| Technical description | Vigik single-door access-control unit | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `348040` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1689` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Access control | Main system association |
| Item model / `modobj` | `195` | Main association; independent of project ID |
| Firmware definition | `97`, `585`, `726` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `348040` | Established catalogue identity | Manufacturer database commercial record `1753` explicitly links this SKU to item `1689` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `348040` | Central unit access control 1 head Vigik  | Canonical commercial record `1753` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `guide_controle_dacces_vigik.pdf` | Vigik access-control system guide | `Publication date not established` | Printed/PDF pp. 5, 7, 9, 12-19: 348040 controller, 348405 programmer and 348330 GPRS specifications, administration modes and historical service workflow. | [Archived original](https://archive.openwebnet-ha.org/sha256/21/f1/21f15d54f5aabef655f35d8c64294b6288fdf5a6e1bfa98fc2d905d6e0f05563.pdf) | [Publisher original](https://assets.legrand.com/general/mediagrp/np-ft-gt/guide_controle_dacces_vigik.pdf) |
| `RA00105AB_I_FR.pdf` | 348040 installer manual | `RA00105AB_I_FR; cover 05/14-01 PC` | Printed/PDF pp. 5, 8-21: capacities, wiring, master / resident badges, firmware update, separate resets and technical ratings; T25 rating scoped to reader. | [Archived original](https://archive.openwebnet-ha.org/sha256/69/dc/69dc2c2401d3839c68a8cfe0bdac2a1ed988f21029507d1f787ce4b1120eaa92.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00105AB_I_FR.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1689`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `RA00082AA_S_FR.pdf` | ACWEB installer portal manual | RA00082AA_S_FR; publication date unestablished | Printed/PDF pp. 14–41: local-plus/online configuration, validation, transfers, site/family/service limits and synchronisation; portal concepts are not local Objects | [Archived original](https://archive.openwebnet-ha.org/sha256/80/05/80052edcb622123171d31b6797b3ee0efb70125f285e3c30f6ce4a9afc789bd9.pdf) | [Publisher source](https://www.acweb.bticino.com/fr_FR/browser/attachments/bin/help/RA00082AA_S_FR.pdf) |
| `BT-controle-acces.pdf` | Manufacturer access-control brochure | Publication date unestablished | Printed pp. 12–13 / PDF pp. 14–15: exact controller, programmer and GPRS descriptions; supply and USB wording conflicts scoped | [Archived original](https://archive.openwebnet-ha.org/sha256/f9/bd/f9bdca3299f987ae1207b5fdeb9b4be5173038d9f448734597d819c9eeb58d3f.pdf) | [Publisher source](https://assets.legrand.com/pim/DOCUMENT/BT_controle_acces.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply alternatives | `SCS 18..27 Vdc or external 12 Vac` | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8, 21; `guide_controle_dacces_vigik.pdf` printed/PDF p. 5 |
| SCS draw, installer manual | `60 mA standby / 100 mA relay active` | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8, 21; `guide_controle_dacces_vigik.pdf` printed/PDF p. 5 |
| External 12 Vac draw, installer manual | `50 mA standby / 85 mA relay active` | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8, 21; `guide_controle_dacces_vigik.pdf` printed/PDF p. 5 |
| Guide maximum draw | `85 mA on either supply; differs from manual SCS maximum` | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8, 21; `guide_controle_dacces_vigik.pdf` printed/PDF p. 5 |
| Relay rating, guide | `24 Vdc/ac, 8 A maximum, C/NO/NC` | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8, 21; `guide_controle_dacces_vigik.pdf` printed/PDF p. 5 |
| Operating temperature / protection | `−5..+45 °C; IP44` | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8, 21; `guide_controle_dacces_vigik.pdf` printed/PDF p. 5 |
| Capacity, manual | `1 door; 32 Vigik services; 1000 residents standalone, up to 20000 with programmer or portal` | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8, 21; `guide_controle_dacces_vigik.pdf` printed/PDF p. 5 |
| Interfaces | `T25 reader; SCS/supply; door-status contact; local release input; micro-USB to programmer/PC` | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8, 21; `guide_controle_dacces_vigik.pdf` printed/PDF p. 5 |
| T25 temperature, manual / guide | `−25..+70 °C / −5..+70 °C; separate reader specification` | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8, 21; `guide_controle_dacces_vigik.pdf` printed/PDF p. 5 |

### Source-specific wiring and limits

The installer manual requires reader-to-controller RS-485 distance greater than 2 m for its Vigik installation rules (p. 7). The brochure gives SYT 8/10 two-pair cable up to 100 m and a drawing labelled 2 m minimum (printed p. 12 / PDF p. 14). The manual specifies a strict lower distance bound; the brochure gives a maximum cable run and an inclusive lower-bound label. Neither establishes a 2 m maximum. The brochure specifies 12 Vdc auxiliary supply and 50/85 mA, whereas the AB installer manual gives a switched 12 Vac mode with 50/85 mA and SCS `18..27` Vdc with 60/100 mA (pp. 8/21). Match the actual supply mode and product revision; no interchangeability of AC and DC is established. CR2032 maintains the clock, rather than serving as a controller power backup.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1689` | Canonical catalogue |
| Technical item description | Central unit access control 1 head Vigik | Canonical catalogue |
| Item family | Device for Access Control system; key `101` | Canonical catalogue |
| Main system | Access control; key `8` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `195` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Access control | `195` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `97` | `1` | `0` | `1` | `1` | Catalogue default | Official |
| `585` | `1` | `2` | `0` | `1` | Not catalogue default | Official |
| `726` | `1` | `3` | `0` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `97` | `154` | BTicino (key `1`) | `0` | Extra | `1689_1.0_BT\xml\Extra\extra.xml` |
| `97` | `156` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1689_1.0_BT\xml\Protocol\protocol.xml` |
| `585` | `844` | BTicino (key `1`) | `0` | Extra | `1689_1.2_BT\xml\Extra\extra.xml` |
| `585` | `845` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1689_1.2_BT\xml\Protocol\protocol.xml` |
| `726` | `1018` | BTicino (key `1`) | `0` | Extra | `1689_1.3_BT\xml\Extra\extra.xml` |
| `726` | `1019` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1689_1.3_BT\xml\Protocol\protocol.xml` |

All 6 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

The Vigik integration compatibility table requires 348040 controller 1.02.06 and its T25 reader 2.01.00 (guide printed/PDF p. 19). This is a minimum for the named intercom/access integration, not proof that every older catalogue release supports it. Companion requirements include 348040/T25 1.02.06/2.01.00, 348405 1.01.26 and 348330 1.00.43; exact connected-product applicability must be checked.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `97` | `1` | `222` Access control unit (one gate Vigik) | Fixed / designated metadata | `880` | `547` | `556` |
| `585` | `1` | `222` Access control unit (one gate Vigik) | Fixed / designated metadata | `2376` | `547` | `1031` |
| `726` | `1` | `222` Access control unit (one gate Vigik) | Fixed / designated metadata | `2656` | `547` | `1266` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `97` | Product Programming | `3` | Canonical firmware/mode association |
| `585` | Product Programming | `3` | Canonical firmware/mode association |
| `726` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `97` | USB | Canonical firmware/connection association |
| `585` | USB | Canonical firmware/connection association |
| `726` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Supply selector | Check SCS versus external 12 Vac before powering | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8-19; `guide_controle_dacces_vigik.pdf` pp. 12-19 |
| Administration modes | EASY master-badge learning; local programmer; local-plus portal / programmer; online GPRS portal | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8-19; `guide_controle_dacces_vigik.pdf` pp. 12-19 |
| Resident enrolment / deletion | Manual pp. 12-15; separate manager / master procedures pp. 9-11 | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8-19; `guide_controle_dacces_vigik.pdf` pp. 12-19 |
| Firmware update | PC/MyHOME Suite; micro-USB route, manual p. 16 | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8-19; `guide_controle_dacces_vigik.pdf` pp. 12-19 |
| Reset / password restoration | Distinct configuration reset, password reset and replacement-unit initialisation, manual pp. 17-19 | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8-19; `guide_controle_dacces_vigik.pdf` pp. 12-19 |
| Clock retention | CR2032 cell in controller; T25 head remains separate hardware | `RA00105AB_I_FR.pdf` printed/PDF pp. 5, 8-19; `guide_controle_dacces_vigik.pdf` pp. 12-19 |

### Managed-system capacities

| Scope | Guide evidence | Limit / discrepancy |
| --- | --- | --- |
| Easy local | Vigik guide p. 16 | 1000 residents plus 20 masters |
| Managed site | Vigik guide pp. 16–17 | 4000 apartments/families; 100 controllers; 20000 resident + service badges combined; 4000 resident + service codes combined |
| Controller entrances / events | Vigik guide p. 16 | One Vigik entrance plus up to nine others, or ten without Vigik; 10000 events per controller |
| Services / time windows | Vigik guide p. 16; AA manual pp. 30/36/39 | 32 Vigik services, seven preloaded; 64 time windows / three per family in guide; AA groups up to three profiles; ten badges/remotes per family |
| Directory screens | Vigik guide pp. 16–17 | 96 DDN on p. 16 versus 95 on p. 17; no assumed correction |

AA p. 39 states that its preloaded Vigik services are not active until associated with an entrance; preloading is not universal activation.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `97` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `97` | `AC_C1` | `0..9` | `0` | C1; local address tenths configurator |
| `97` | `AC_C0` | `0..9` | `0` | C0; local address units configurator |
| `97` | `AC_P1` | `0..10` | `0` | P1; EU address tenths configurator |
| `97` | `AC_P0` | `0..10` | `0` | P0; EU address units configurator |
| `97` | `AC_CU_M` | `0..5` | `0` | M; central unit operating mode |
| `97` | `AC_T` | `0..7` | `0` | T; local relay timing |
| `585` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `585` | `AC_C1` | `0..9` | `0` | C1; local address tenths configurator |
| `585` | `AC_C0` | `0..9` | `0` | C0; local address units configurator |
| `585` | `AC_P1` | `0..10` | `0` | P1; EU address tenths configurator |
| `585` | `AC_P0` | `0..10` | `0` | P0; EU address units configurator |
| `585` | `AC_CU_M` | `0..5` | `0` | M; central unit operating mode |
| `585` | `AC_T` | `0..7` | `0` | T; local relay timing |
| `726` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `726` | `AC_C1` | `0..9` | `0` | C1; local address tenths configurator |
| `726` | `AC_C0` | `0..9` | `0` | C0; local address units configurator |
| `726` | `AC_P1` | `0..10` | `0` | P1; EU address tenths configurator |
| `726` | `AC_P0` | `0..10` | `0` | P0; EU address units configurator |
| `726` | `AC_CU_M` | `0..5` | `0` | M; central unit operating mode |
| `726` | `AC_T` | `0..7` | `0` | T; local relay timing |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `222` - Access control unit (one gate Vigik)

Catalogue Object key `547` maps to external Object `222`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `AC_CEN_ADDR` | `0..99` | `0` | Access control central unit address |
| `AC_RELAYTIME` | `0` = 4 s; `1` = 1 s; `2` = 10 s; `3` = 20 s; `4` = 40 s; `5` = 60 s; `6` = 90 s; `7` = 180 s | `0` | Access control central unit relay timing |
| `AC_MODE` | `0` = Remote management; relay NO; `1` = Remote management; relay NC; `2` = Local management; relay NO; `3` = Local management; relay NC; `4` = N days local memorization; `5` = Restoredefault password | `0` | Access control central unit operating mode |
| `AC_EU_ADDR` | `0..96` | `96` | External unit linked to access control central unit; 0<->95: valid addressee 96: `OFF` |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `97` | `1` | `222` | `4923` | No textual predicate stored | `7040` |
| `585` | `1` | `222` | `4923` | No textual predicate stored | `7040` |
| `726` | `1` | `222` | `4923` | No textual predicate stored | `7040` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `97` | `222` | `1798` | `AC_MODE` | `5` = Restoredefault password | `0` | Access control central unit operating mode; reusable default `0` is outside this subset; filter supplies no replacement default |
| `585` | `222` | `1819` | `AC_MODE` | `5` = Restoredefault password | `0` | Access control central unit operating mode; reusable default `0` is outside this subset; filter supplies no replacement default |
| `726` | `222` | `2995` | `AC_MODE` | `5` = Restoredefault password | `0` | Access control central unit operating mode; reusable default `0` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7040` | `AC_C1=0; AC_C0=0` | `AC_CEN_ADDR` = `0` | `7040` → `7041` |
| `7040` | `AC_C1=0; AC_C0=1` | `AC_CEN_ADDR` = `1` | `7040` → `7041` |
| `7040` | `AC_C1=0; AC_C0=2` | `AC_CEN_ADDR` = `2` | `7040` → `7041` |
| `7040` | `AC_C1=0; AC_C0=3` | `AC_CEN_ADDR` = `3` | `7040` → `7041` |
| `7040` | `AC_C1=0; AC_C0=4` | `AC_CEN_ADDR` = `4` | `7040` → `7041` |
| `7040` | `AC_C1=0; AC_C0=5` | `AC_CEN_ADDR` = `5` | `7040` → `7041` |
| `7040` | `AC_C1=0; AC_C0=6` | `AC_CEN_ADDR` = `6` | `7040` → `7041` |
| `7040` | `AC_C1=0; AC_C0=7` | `AC_CEN_ADDR` = `7` | `7040` → `7041` |
| `7040` | `AC_C1=0; AC_C0=8` | `AC_CEN_ADDR` = `8` | `7040` → `7041` |
| `7040` | `AC_C1=0; AC_C0=9` | `AC_CEN_ADDR` = `9` | `7040` → `7041` |
| `7040` | `AC_C1=1; AC_C0=0` | `AC_CEN_ADDR` = `10` | `7040` → `7042` |
| `7040` | `AC_C1=1; AC_C0=1` | `AC_CEN_ADDR` = `11` | `7040` → `7042` |
| `7040` | `AC_C1=1; AC_C0=2` | `AC_CEN_ADDR` = `12` | `7040` → `7042` |
| `7040` | `AC_C1=1; AC_C0=3` | `AC_CEN_ADDR` = `13` | `7040` → `7042` |
| `7040` | `AC_C1=1; AC_C0=4` | `AC_CEN_ADDR` = `14` | `7040` → `7042` |
| `7040` | `AC_C1=1; AC_C0=5` | `AC_CEN_ADDR` = `15` | `7040` → `7042` |
| `7040` | `AC_C1=1; AC_C0=6` | `AC_CEN_ADDR` = `16` | `7040` → `7042` |
| `7040` | `AC_C1=1; AC_C0=7` | `AC_CEN_ADDR` = `17` | `7040` → `7042` |
| `7040` | `AC_C1=1; AC_C0=8` | `AC_CEN_ADDR` = `18` | `7040` → `7042` |
| `7040` | `AC_C1=1; AC_C0=9` | `AC_CEN_ADDR` = `19` | `7040` → `7042` |
| `7040` | `AC_C1=2; AC_C0=0` | `AC_CEN_ADDR` = `20` | `7040` → `7043` |
| `7040` | `AC_C1=2; AC_C0=1` | `AC_CEN_ADDR` = `21` | `7040` → `7043` |
| `7040` | `AC_C1=2; AC_C0=2` | `AC_CEN_ADDR` = `22` | `7040` → `7043` |
| `7040` | `AC_C1=2; AC_C0=3` | `AC_CEN_ADDR` = `23` | `7040` → `7043` |
| `7040` | `AC_C1=2; AC_C0=4` | `AC_CEN_ADDR` = `24` | `7040` → `7043` |
| `7040` | `AC_C1=2; AC_C0=5` | `AC_CEN_ADDR` = `25` | `7040` → `7043` |
| `7040` | `AC_C1=2; AC_C0=6` | `AC_CEN_ADDR` = `26` | `7040` → `7043` |
| `7040` | `AC_C1=2; AC_C0=7` | `AC_CEN_ADDR` = `27` | `7040` → `7043` |
| `7040` | `AC_C1=2; AC_C0=8` | `AC_CEN_ADDR` = `28` | `7040` → `7043` |
| `7040` | `AC_C1=2; AC_C0=9` | `AC_CEN_ADDR` = `29` | `7040` → `7043` |
| `7040` | `AC_C1=3; AC_C0=0` | `AC_CEN_ADDR` = `30` | `7040` → `7044` |
| `7040` | `AC_C1=3; AC_C0=1` | `AC_CEN_ADDR` = `31` | `7040` → `7044` |
| `7040` | `AC_C1=3; AC_C0=2` | `AC_CEN_ADDR` = `32` | `7040` → `7044` |
| `7040` | `AC_C1=3; AC_C0=3` | `AC_CEN_ADDR` = `33` | `7040` → `7044` |
| `7040` | `AC_C1=3; AC_C0=4` | `AC_CEN_ADDR` = `34` | `7040` → `7044` |
| `7040` | `AC_C1=3; AC_C0=5` | `AC_CEN_ADDR` = `35` | `7040` → `7044` |
| `7040` | `AC_C1=3; AC_C0=6` | `AC_CEN_ADDR` = `36` | `7040` → `7044` |
| `7040` | `AC_C1=3; AC_C0=7` | `AC_CEN_ADDR` = `37` | `7040` → `7044` |
| `7040` | `AC_C1=3; AC_C0=8` | `AC_CEN_ADDR` = `38` | `7040` → `7044` |
| `7040` | `AC_C1=3; AC_C0=9` | `AC_CEN_ADDR` = `39` | `7040` → `7044` |
| `7040` | `AC_C1=4; AC_C0=0` | `AC_CEN_ADDR` = `40` | `7040` → `7045` |
| `7040` | `AC_C1=4; AC_C0=1` | `AC_CEN_ADDR` = `41` | `7040` → `7045` |
| `7040` | `AC_C1=4; AC_C0=2` | `AC_CEN_ADDR` = `42` | `7040` → `7045` |
| `7040` | `AC_C1=4; AC_C0=3` | `AC_CEN_ADDR` = `43` | `7040` → `7045` |
| `7040` | `AC_C1=4; AC_C0=4` | `AC_CEN_ADDR` = `44` | `7040` → `7045` |
| `7040` | `AC_C1=4; AC_C0=5` | `AC_CEN_ADDR` = `45` | `7040` → `7045` |
| `7040` | `AC_C1=4; AC_C0=6` | `AC_CEN_ADDR` = `46` | `7040` → `7045` |
| `7040` | `AC_C1=4; AC_C0=7` | `AC_CEN_ADDR` = `47` | `7040` → `7045` |
| `7040` | `AC_C1=4; AC_C0=8` | `AC_CEN_ADDR` = `48` | `7040` → `7045` |
| `7040` | `AC_C1=4; AC_C0=9` | `AC_CEN_ADDR` = `49` | `7040` → `7045` |
| `7040` | `AC_C1=5; AC_C0=0` | `AC_CEN_ADDR` = `50` | `7040` → `7046` |
| `7040` | `AC_C1=5; AC_C0=1` | `AC_CEN_ADDR` = `51` | `7040` → `7046` |
| `7040` | `AC_C1=5; AC_C0=2` | `AC_CEN_ADDR` = `52` | `7040` → `7046` |
| `7040` | `AC_C1=5; AC_C0=3` | `AC_CEN_ADDR` = `53` | `7040` → `7046` |
| `7040` | `AC_C1=5; AC_C0=4` | `AC_CEN_ADDR` = `54` | `7040` → `7046` |
| `7040` | `AC_C1=5; AC_C0=5` | `AC_CEN_ADDR` = `55` | `7040` → `7046` |
| `7040` | `AC_C1=5; AC_C0=6` | `AC_CEN_ADDR` = `56` | `7040` → `7046` |
| `7040` | `AC_C1=5; AC_C0=7` | `AC_CEN_ADDR` = `57` | `7040` → `7046` |
| `7040` | `AC_C1=5; AC_C0=8` | `AC_CEN_ADDR` = `58` | `7040` → `7046` |
| `7040` | `AC_C1=5; AC_C0=9` | `AC_CEN_ADDR` = `59` | `7040` → `7046` |
| `7040` | `AC_C1=6; AC_C0=0` | `AC_CEN_ADDR` = `60` | `7040` → `7047` |
| `7040` | `AC_C1=6; AC_C0=1` | `AC_CEN_ADDR` = `61` | `7040` → `7047` |
| `7040` | `AC_C1=6; AC_C0=2` | `AC_CEN_ADDR` = `62` | `7040` → `7047` |
| `7040` | `AC_C1=6; AC_C0=3` | `AC_CEN_ADDR` = `63` | `7040` → `7047` |
| `7040` | `AC_C1=6; AC_C0=4` | `AC_CEN_ADDR` = `64` | `7040` → `7047` |
| `7040` | `AC_C1=6; AC_C0=5` | `AC_CEN_ADDR` = `65` | `7040` → `7047` |
| `7040` | `AC_C1=6; AC_C0=6` | `AC_CEN_ADDR` = `66` | `7040` → `7047` |
| `7040` | `AC_C1=6; AC_C0=7` | `AC_CEN_ADDR` = `67` | `7040` → `7047` |
| `7040` | `AC_C1=6; AC_C0=8` | `AC_CEN_ADDR` = `68` | `7040` → `7047` |
| `7040` | `AC_C1=6; AC_C0=9` | `AC_CEN_ADDR` = `69` | `7040` → `7047` |
| `7040` | `AC_C1=7; AC_C0=0` | `AC_CEN_ADDR` = `70` | `7040` → `7048` |
| `7040` | `AC_C1=7; AC_C0=1` | `AC_CEN_ADDR` = `71` | `7040` → `7048` |
| `7040` | `AC_C1=7; AC_C0=2` | `AC_CEN_ADDR` = `72` | `7040` → `7048` |
| `7040` | `AC_C1=7; AC_C0=3` | `AC_CEN_ADDR` = `73` | `7040` → `7048` |
| `7040` | `AC_C1=7; AC_C0=4` | `AC_CEN_ADDR` = `74` | `7040` → `7048` |
| `7040` | `AC_C1=7; AC_C0=5` | `AC_CEN_ADDR` = `75` | `7040` → `7048` |
| `7040` | `AC_C1=7; AC_C0=6` | `AC_CEN_ADDR` = `76` | `7040` → `7048` |
| `7040` | `AC_C1=7; AC_C0=7` | `AC_CEN_ADDR` = `77` | `7040` → `7048` |
| `7040` | `AC_C1=7; AC_C0=8` | `AC_CEN_ADDR` = `78` | `7040` → `7048` |
| `7040` | `AC_C1=7; AC_C0=9` | `AC_CEN_ADDR` = `79` | `7040` → `7048` |
| `7040` | `AC_C1=8; AC_C0=5` | `AC_CEN_ADDR` = `85` | `7040` → `7049` |
| `7040` | `AC_C1=8; AC_C0=6` | `AC_CEN_ADDR` = `86` | `7040` → `7049` |
| `7040` | `AC_C1=8; AC_C0=7` | `AC_CEN_ADDR` = `87` | `7040` → `7049` |
| `7040` | `AC_C1=8; AC_C0=8` | `AC_CEN_ADDR` = `88` | `7040` → `7049` |
| `7040` | `AC_C1=8; AC_C0=9` | `AC_CEN_ADDR` = `89` | `7040` → `7049` |
| `7040` | `AC_C1=8; AC_C0=0` | `AC_CEN_ADDR` = `80` | `7040` → `7049` |
| `7040` | `AC_C1=8; AC_C0=1` | `AC_CEN_ADDR` = `81` | `7040` → `7049` |
| `7040` | `AC_C1=8; AC_C0=2` | `AC_CEN_ADDR` = `82` | `7040` → `7049` |
| `7040` | `AC_C1=8; AC_C0=3` | `AC_CEN_ADDR` = `83` | `7040` → `7049` |
| `7040` | `AC_C1=8; AC_C0=4` | `AC_CEN_ADDR` = `84` | `7040` → `7049` |
| `7040` | `AC_C1=9; AC_C0=0` | `AC_CEN_ADDR` = `90` | `7040` → `7050` |
| `7040` | `AC_C1=9; AC_C0=1` | `AC_CEN_ADDR` = `91` | `7040` → `7050` |
| `7040` | `AC_C1=9; AC_C0=2` | `AC_CEN_ADDR` = `92` | `7040` → `7050` |
| `7040` | `AC_C1=9; AC_C0=3` | `AC_CEN_ADDR` = `93` | `7040` → `7050` |
| `7040` | `AC_C1=9; AC_C0=4` | `AC_CEN_ADDR` = `94` | `7040` → `7050` |
| `7040` | `AC_C1=9; AC_C0=5` | `AC_CEN_ADDR` = `95` | `7040` → `7050` |
| `7040` | `AC_C1=9; AC_C0=6` | `AC_CEN_ADDR` = `96` | `7040` → `7050` |
| `7040` | `AC_C1=9; AC_C0=7` | `AC_CEN_ADDR` = `97` | `7040` → `7050` |
| `7040` | `AC_C1=9; AC_C0=8` | `AC_CEN_ADDR` = `98` | `7040` → `7050` |
| `7040` | `AC_C1=9; AC_C0=9` | `AC_CEN_ADDR` = `99` | `7040` → `7050` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Effective-domain conflict

All three firmware/Object filters restrict `AC_MODE` to `5`, although reusable default `0`, item-side `AC_CU_M=0..5` and normal physical modes `0..3` remain recorded. There is no default override. Rule `7040` contains the 100 stored central-address branches `AC_CEN_ADDR = 10 × AC_C1 + AC_C0`; it does not supply an EU-address, relay-time or mode conversion. Item-side `AC_P1/P0` admit `10`, while the reusable EU address ends at `96`; do not invent decimal composition or an OFF encoding without a stored rule. The empty condition `4923` does not prove unconditional activation. Ordinary item-side `AC_T=0..7` relay timing does not encode every `M=4, T=1..9` replacement-day setting.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `195` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `222` - Access control unit (one gate Vigik) | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `222` - Access control unit (one gate Vigik) | Access control | `8` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use the manufacturer’s master-badge enrolment / deletion and resident-badge procedures (`RA00105AB_I_FR.pdf` printed/PDF pp. 9-15). The guide distinguishes EASY, local, local-plus and online administration (pp. 12-19). PC/MyHOME Suite is documented for firmware updating (manual p. 16). Resetting configuration and restoring the documented default password are separate procedures (pp. 17-19); no live credential is retained.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

### ACWEB configuration and transfer scope

The retained AA installer manual separates Local Plus (transfer through 348405) from On-line (through 348330); site and management types cannot be changed after setup (p. 14). Controllers must be associated with at least one entrance, with one Vigik reader per controller (p. 19). Validate addresses before activation; Local Plus requires confirming settings, exporting the site and transferring it through the portable programmer (pp. 21–23). On-line requires the site password and interface serial, installation diagnostics and correction of errors before management is enabled (pp. 24–28). These are setup requirements; no installation-specific credentials or serial are retained here.

Even an On-line site must add new Vigik services through 348405: export to the programmer, add the service, transfer to the controller and import the changed site back to ACWEB (p. 31). The Local Plus sequence imports the changed site before the controller transfer. AA portal notifications distinguish pending, sent/acknowledged and executed commands; GPRS connects hourly, with an immediate synchronisation option (p. 41). Portal or mobile-service availability today is unestablished.

### Badge deletion and reset effects

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Master badges | Up to 20; deleting all masters uses the 30-second indication sequence (10 slow green, 10 fast green, 10 orange flashes) | RA00105AB_I_FR pp. 9–11 |
| Resident badges | Up to 1000 in local enrolment; present the same master three times to delete all residents, rather than deleting one resident badge | RA00105AB_I_FR pp. 12–15 |
| Firmware update | Controller and T25 reader update through MyHOME Suite; may take more than four minutes and must not be interrupted | RA00105AB_I_FR p. 16 |
| Factory restore | Startup button held 10 seconds deletes badges and events, restores public default password 12345 and disables logging; Vigik services remain unchanged | RA00105AB_I_FR p. 17 |
| Password restore | `M=5` restores public default 12345 while preserving badges, events and Vigik services; restore the normal M=`0..3` selector afterwards | RA00105AB_I_FR p. 18 |
| Replacement-controller enrolment | `M=4`, T=`1..9` selects a duration in days for this special procedure; this differs from ordinary relay timing | RA00105AB_I_FR p. 19 |

## Source reconciliation

The manual and guide refer to the exact controller but disagree on SCS maximum draw (100 versus 85 mA) and T25 minimum temperature (−25 versus −5 °C). Both values are retained with their scope; the head rating is not assigned to the controller. Canonical Firmware definitions are separately listed, without assuming which revision caused a publication difference.

The exact restriction table identifies reusable defaults outside a Firmware/Object subset. These are catalogue conflicts; no replacement default is inferred.

## Evidence limits and open work

Applicable source revision, actual relay / load suitability, installed reader version and current ACWEB/Vigik service availability require corroboration. Missing current documentation does not invalidate catalogue identity.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

The official ACWEB AD HTML overview was found at [RA00082AD_S_FR-3.html](https://www.acweb.bticino.com/fr_FR/browser/attachments/bin/help/PortailACWEB-FR/RA00082AD_S_FR-3.html). Only its Local Plus / On-line overview was inspected; the complete AD revision is outside this review. The corresponding attempted PDF retrieval returned 404. AA procedures must not be represented as a complete reconciliation of AD. The older Vigik guide’s customer-screen walkthrough beyond p. 19 was not re-audited; the AA installer manual supplies the reviewed portal workflow.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0181-0190-2026-10-07.md#own-dev-0186)
