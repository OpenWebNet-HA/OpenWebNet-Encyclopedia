# MyHOME_Screen 10 Capacitive

## Summary

MyHOME_Screen 10C is a 10-inch capacitive wall touchscreen for configured MyHOME, video-door-entry and multimedia functions. Room navigation and up to ten personal profiles organize the installation’s controls; its hardware identity and firmware records remain separate from the non-C screen.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0049` | Project identity |
| Technical description | MyHOME_Screen 10 Capacitive | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `MH4892C`, `MH4893C`, `067228`, `067219` | Canonical commercial records |
| Catalogue item | `1898` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Firmware definition | `2.0.0`; `2.1.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Integration, Touchscreen, Video door entry, Multimedia | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `MH4892C` | established catalogue identity for item `1898` | canonical commercial record |
| BTicino | `MH4893C` | established catalogue identity for item `1898` | canonical commercial record |
| Legrand | `067228` | established catalogue identity for item `1898` | canonical commercial record |
| Legrand | `067219` | established catalogue identity for item `1898` | canonical commercial record |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `RA00079AC_S_EN` | software manual | RA00079AC; no dated imprint established | Printed/PDF pp. 4–55; both screen models, project settings, complete function families and transfer/media procedures; feature-to-release mapping remains unestablished | [Archived original](https://archive.openwebnet-ha.org/sha256/b9/ba/b9baa0fea2deb196253f415c47e6fd83f52d1a9728b5bfe99f69a20e0bc47340.pdf) | [Official source](https://dar.bticino.com/asset/Documents/RA00079AC_S_EN.pdf) |
| BTicino `MH4892C` catalogue page | product page | current catalogue | `MH4892C` product characteristics and capacitive-screen variant | Original not retained; discovery/provenance only; substantive claims use retained originals | [Official product page](https://catalogue.bticino.com/product/smart-home-solutions/my-home---home-automation-system/integration-and-control/BTI-MH4892C-EN) |
| `MH4892C-italian-product-sheet-IT.pdf` | Exact-product manufacturer export | Retrieved 2026-10-06; technical revision not printed | Printed/PDF p. 1; exact MH4892C capacitive display, supply, dimensions, mounting and media support | [Archived original](https://archive.openwebnet-ha.org/sha256/b8/3c/b83ca41a78ecd8dd7299d8b831150b07438d0601c657e914a133a4fb17d7b256.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-MH4892C) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| MH4892C display / supply | `10 inch` 16:9 capacitive display; `27 Vdc` | Retained MH4892C Italian export p. 1 |
| MH4892C size / mounting | `315 × 200 × 24 mm` (W × H × D); 506E wall box | Same source |
| Connections / media | Ethernet or USB-miniUSB PC connection while bus-powered; export names USB, SD, LAN/IP media | RA00079AC_S_EN p. 4; export p. 1 |
| Variant boundary | MH4892C/067228 black; MH4893C/067219 white in catalogue; exact MH4892C ratings are not independently measured for every variant | Canonical commercial descriptions |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1898` | Canonical catalogue |
| Technical item | MyHOME_Screen 10 Capacitive | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `55` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Burglar alarm | private riser | Canonical item/bus relationship |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `2420` | `MH4892C` | `1` | `5` | `MyHOME_Screen 10 C black bus` |
| `2421` | `MH4893C` | `1` | `5` | `MyHOME_Screen 10 C white bus` |
| `2422` | `067228` | `2` | `5` | `MyHOME_Screen 10 C black bus` |
| `2423` | `067219` | `2` | `5` | `MyHOME_Screen 10 C white bus` |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `558` | `2` | `0` | `0` | `1` | Not catalogue default | Official |
| `697` | `2` | `1` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `558` | `714` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `558` | `715` | BTicino (key `1`) | `0` | SVM | `1898_2.0_BT\xml\SVM\svm.xml` |
| `558` | `716` | BTicino (key `1`) | `0` | Extra | `1898_2.0_BT\xml\Extra\extra.xml` |
| `558` | `717` | BTicino (key `1`) | `0` | Director | `1898_2.0_BT\xml\DIRECTOR\director.xml` |
| `558` | `718` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1898_2.0_BT\xml\Protocol\protocol.xml` |
| `558` | `776` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `558` | `777` | Legrand (key `2`) | `0` | SVM | `1898_2.0_LG\xml\SVM\svm.xml` |
| `558` | `778` | Legrand (key `2`) | `0` | Extra | `1898_2.0_LG\xml\Extra\extra.xml` |
| `558` | `779` | Legrand (key `2`) | `0` | Director | `1898_2.0_LG\xml\DIRECTOR\director.xml` |
| `558` | `780` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1898_2.0_LG\xml\Protocol\protocol.xml` |
| `697` | `912` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `697` | `913` | BTicino (key `1`) | `0` | SVM | `1898_2.1_BT\xml\SVM\svm.xml` |
| `697` | `914` | BTicino (key `1`) | `0` | Extra | `1898_2.1_BT\xml\Extra\extra.xml` |
| `697` | `915` | BTicino (key `1`) | `0` | Director | `1898_2.1_BT\xml\DIRECTOR\director.xml` |
| `697` | `916` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1898_2.1_BT\xml\Protocol\protocol.xml` |
| `697` | `917` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `697` | `918` | Legrand (key `2`) | `0` | SVM | `1898_2.1_LG\xml\SVM\svm.xml` |
| `697` | `919` | Legrand (key `2`) | `0` | Extra | `1898_2.1_LG\xml\Extra\extra.xml` |
| `697` | `920` | Legrand (key `2`) | `0` | Director | `1898_2.1_LG\xml\DIRECTOR\director.xml` |
| `697` | `921` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1898_2.1_LG\xml\Protocol\protocol.xml` |

All 20 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `558` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2431` | `32` | `1083` |
| `697` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2583` | `32` | `1202` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `558` | Product Programming | `3` | Canonical firmware/mode association |
| `697` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `558` | Ethernet | Canonical firmware/connection association |
| `558` | Ethernet over USB | Canonical firmware/connection association |
| `697` | Ethernet | Canonical firmware/connection association |
| `697` | Ethernet over USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `558` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `558` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `558` | `FW_VER` | `######` = Firmware version | `2.0.0` | Firmware version |
| `558` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `697` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `697` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `697` | `FW_VER` | `######` = Firmware version | `2.0.0` | Firmware version |
| `697` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `1898` / `modobj = 55` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`32`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Automation / lights | Normal/hold-to-run control, advanced positions with advanced actuators, timed lighting and 10/100 level dimmers, general/room/group/mixed controls | RA00079AC_S_EN pp. 12–17 |
| Alarm / HVAC | Zone groups; 99/4 zone programs/scenarios, external/uncontrolled probes and basic 20 command/advanced AC roles | Same source pp. 17–27 |
| Door entry / sound | Handsets, entrance panels, cameras; ONVIF H.264 second profile up to 720p with compatibility caveat; mono/multichannel and NUVO option | Same source pp. 28–38 |
| Scenarios / energy | Central/local scenarios and time/device conditions; consumption tariffs/goals/thresholds; shedding requires central unit, otherwise advanced actuators supply consumption only | Same source pp. 39–49 |
| Media / personal UI | RSS, web radio, webcams, experimental browser, network media; rooms/floors, up to 10 profiles; 1024×600 backgrounds and 171×213 cards at 72 dpi | Same source pp. 50–55; image formats, not separate screen measurement |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Configure unique address, clock/timezone, temperature format, selected SCS A/V or automation bus/level, video-door-entry/source addresses, Ethernet and authentication. Compose/check interface objects and groups, then send or receive configuration via Ethernet/USB. Software selects .fwz firmware and queries device information (RA00079AC_S_EN pp. 4–15).

Configure scenario, HVAC, measurement and load roles only when the installed companion system supports them; for example an advanced actuator’s position display is not generic support for every shutter. Twenty parameter payload associations are shown but not inspected. Do not import the non-C version-history chronology into this C item.

## Source reconciliation

The shared software manual names both screen families; exact C export establishes capacitive hardware. Catalogue firmware `FW_VER` default `2.0.0` differs from reusable Object `32` default 3.0.0; neither determines observed state. No catalogue default firmware is marked for this item. Linked publisher hardware/download documentation remains distinct from the examined common software procedures.

Both firmware records designate Colors Touch Screen 32 in one slot and neither is catalogue default. No Virgin, conditions, relation filters or conversions are associated. Firmware FW_VER defaults 2.0.0, while reusable Object `32` defaults 3.0.0; preserve firmware scope. Twenty parameter associations and Ethernet/USB connections are shown; payloads remain unexamined. Shared software documentation establishes common interface workflows, not shared hardware, release history or item identity with 1768.

## Evidence limits and open work

- ExactMH4893C/Legrand hardware sheets, C-specific release history and linked user/install manuals remain unexamined; parameter payloads are not available in the extraction.
- No release mapping or hardware capture verifies every shared-manual function against firmware `558`/697.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0041-0050-2026-10-06.md#own-dev-0049)
