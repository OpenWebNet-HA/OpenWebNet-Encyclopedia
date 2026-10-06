# MyHOME_Screen 10

## Summary

MyHOME_Screen 10 is a wall-mounted 10-inch touchscreen for configured home controls, video door entry and multimedia. It combines room navigation and personal profiles with lighting, shutters, temperature, scenarios, energy and sound functions, using the connected installation and configured network sources.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0047` | Project identity |
| Technical description | MyHOME_Screen 10 | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `MH4892`, `MH4893`, `067267`, `067268` | Canonical commercial records |
| Catalogue item | `1768` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `54` | Canonical inventory |
| Firmware definition | `1.0.7`; `2.0.0`; `2.1.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Integration, Touchscreen, Video door entry, Multimedia | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `MH4892` | established catalogue identity for item `1768` | canonical commercial record |
| BTicino | `MH4893` | established catalogue identity for item `1768` | canonical commercial record |
| Legrand | `067267` | established catalogue identity for item `1768` | canonical commercial record |
| Legrand | `067268` | established catalogue identity for item `1768` | canonical commercial record |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `RA00079AC_S_EN` | software manual | RA00079AC; no dated imprint established | Printed/PDF pp. 4–55; both screen models, project settings, complete function families and transfer/media procedures; feature-to-release mapping remains unestablished | [Archived original](https://archive.openwebnet-ha.org/sha256/b9/ba/b9baa0fea2deb196253f415c47e6fd83f52d1a9728b5bfe99f69a20e0bc47340.pdf) | [Official source](https://dar.bticino.com/asset/Documents/RA00079AC_S_EN.pdf) |
| BTicino `MH4892` catalogue page | product page | current catalogue | `MH4892` product characteristics and integration role | Original not retained; discovery/provenance only; substantive claims use retained originals | [Official product page](https://catalogo.bticino.it/prodotto/soluzioni-per-la-smart-home/my-home---sistema-domotico/integrazione-e-controllo/BTI-MH4892-IT) |
| `MH4892` version history | firmware history | through 2015-03-26 in identified copy | Historical `MH4892` / `MH4893` / `067267` / `067268` firmware lineage | [Archived original](https://archive.openwebnet-ha.org/sha256/ea/4c/ea4c1d9873c01cb2868edc3930f6608a5821c00d6986025a74a5f220d09042ea.pdf) | [Official source](https://myhomeswupdate.bticino.com/VersionHistory/Version_History_MH4892_20150326.pdf) |
| `MH4892-italian-product-sheet-IT.pdf` | Exact-product manufacturer export | Retrieved 2026-10-06; technical revision not printed | Printed/PDF p. 1; exact MH4892 display, supply, dimensions, mounting and media support | [Archived original](https://archive.openwebnet-ha.org/sha256/e1/bb/e1bb45c6997d72704805e4737f6dc21a7766386642bb13a6e64ef47d2eac1a8e.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-MH4892) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| MH4892 display / supply | `10 inch` 16:9 LCD; `27 Vdc` | Retained MH4892 Italian export p. 1 |
| MH4892 size / mounting | `315 × 200 × 24 mm` (W × H × D); 506E wall box | Same source |
| Connections / media | Ethernet or USB-miniUSB PC connection while bus-powered; export names USB, SD, LAN/IP media | RA00079AC_S_EN p. 4; export p. 1 |
| Variant boundary | MH4892/067267 black; MH4893/067268 white in catalogue; exact MH4892 export ratings are not separately measured ratings for all variants | Canonical commercial descriptions |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1768` | Canonical catalogue |
| Technical item | MyHOME_Screen 10 | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `54` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `54` | Yes | Canonical item/system relationship |

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
| `1806` | `MH4892` | `1` | `5` | `BTicino Multimedia Touch Screen Black` |
| `1977` | `MH4893` | `1` | `5` | `BTicino Multimedia Touch Screen White` |
| `1980` | `067267` | `2` | `5` | `Legrand Multimedia Touch Screen Black` |
| `1981` | `067268` | `2` | `5` | `Legrand-Multimedia Touch Screen White` |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `109` | `1` | `0` | `7` | `1` | Catalogue default | Official |
| `560` | `2` | `0` | `0` | `1` | Not catalogue default | Official |
| `696` | `2` | `1` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `109` | `833` | BTicino (key `1`) | `0` | SVM | `1768_1.0_BT\xml\SVM\svm.xml` |
| `109` | `834` | BTicino (key `1`) | `0` | Extra | `1768_1.0_BT\xml\Extra\extra.xml` |
| `109` | `835` | BTicino (key `1`) | `0` | Director | `1768_1.0_BT\xml\DIRECTOR\director.xml` |
| `109` | `836` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1768_1.0_BT\xml\Protocol\protocol.xml` |
| `109` | `838` | Legrand (key `2`) | `0` | SVM | `1768_1.0_LG\xml\SVM\svm.xml` |
| `109` | `839` | Legrand (key `2`) | `0` | Extra | `1768_1.0_LG\xml\Extra\extra.xml` |
| `109` | `840` | Legrand (key `2`) | `0` | Director | `1768_1.0_LG\xml\DIRECTOR\director.xml` |
| `109` | `841` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1768_1.0_LG\xml\Protocol\protocol.xml` |
| `109` | `842` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `109` | `843` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `560` | `296` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `560` | `297` | BTicino (key `1`) | `0` | SVM | `1768_2.0_BT\xml\SVM\svm.xml` |
| `560` | `298` | BTicino (key `1`) | `0` | Extra | `1768_2.0_BT\xml\Extra\extra.xml` |
| `560` | `299` | BTicino (key `1`) | `0` | Director | `1768_2.0_BT\xml\DIRECTOR\director.xml` |
| `560` | `300` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1768_2.0_BT\xml\Protocol\protocol.xml` |
| `560` | `301` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `560` | `302` | Legrand (key `2`) | `0` | SVM | `1768_2.0_LG\xml\SVM\svm.xml` |
| `560` | `303` | Legrand (key `2`) | `0` | Extra | `1768_2.0_LG\xml\Extra\extra.xml` |
| `560` | `304` | Legrand (key `2`) | `0` | Director | `1768_2.0_LG\xml\DIRECTOR\director.xml` |
| `560` | `305` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1768_2.0_LG\xml\Protocol\protocol.xml` |
| `696` | `902` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `696` | `903` | BTicino (key `1`) | `0` | SVM | `1768_2.1_BT\xml\SVM\svm.xml` |
| `696` | `904` | BTicino (key `1`) | `0` | Extra | `1768_2.1_BT\xml\Extra\extra.xml` |
| `696` | `905` | BTicino (key `1`) | `0` | Director | `1768_2.1_BT\xml\DIRECTOR\director.xml` |
| `696` | `906` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1768_2.1_BT\xml\Protocol\protocol.xml` |
| `696` | `907` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `696` | `908` | Legrand (key `2`) | `0` | SVM | `1768_2.1_LG\xml\SVM\svm.xml` |
| `696` | `909` | Legrand (key `2`) | `0` | Extra | `1768_2.1_LG\xml\Extra\extra.xml` |
| `696` | `910` | Legrand (key `2`) | `0` | Director | `1768_2.1_LG\xml\DIRECTOR\director.xml` |
| `696` | `911` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1768_2.1_LG\xml\Protocol\protocol.xml` |

All 30 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `109` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1385` | `32` | `731` |
| `560` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2345` | `32` | `1000` |
| `696` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2582` | `32` | `1201` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `109` | Product Programming | `3` | Canonical firmware/mode association |
| `560` | Product Programming | `3` | Canonical firmware/mode association |
| `696` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `109` | Ethernet | Canonical firmware/connection association |
| `109` | Ethernet over USB | Canonical firmware/connection association |
| `560` | Ethernet | Canonical firmware/connection association |
| `560` | Ethernet over USB | Canonical firmware/connection association |
| `696` | Ethernet | Canonical firmware/connection association |
| `696` | Ethernet over USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `109` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `109` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `109` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `109` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `560` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `560` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `560` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `560` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `696` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `696` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `696` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `696` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `1768` / `modobj = 54` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`32`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Automation / lighting | Normal or hold-to-run shutter control; advanced position requires advanced actuators. Timed lights, 10/100 level dimmers, stairs and general/room/group/mixed controls | RA00079AC_S_EN pp. 12–17 |
| Security / temperature | Alarm zone grouping; 99/4 zone programs and scenarios; external/uncontrolled probes; basic AC 20 stored IR commands versus advanced AC control | Same source pp. 17–27 |
| Door entry / sound | Handsets, entrance panels and cameras; ONVIF H.264 second profile max 720p with compatibility caveat; mono/multichannel amplifiers and NUVO option | Same source pp. 28–38 |
| Scenarios / energy | F420/programmer/local scenarios; local time/device conditions. Energy tariffs, thresholds/goals; load shedding requires a load central unit; advanced-actuator-only mode monitors consumption | Same source pp. 39–49 |
| Personalization / media | RSS/weather/web radio/webcam/links, experimental browser, network media; rooms/floors and up to 10 profiles; background 1024×600 and card 171×213 px at 72 dpi | Same source pp. 50–55; image sizes do not separately prove screen resolution |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Configure unique progressive address, clock/timezone, Celsius/Fahrenheit, selected SCS A/V or automation bus/level, internal-unit/entrance-panel/source addresses, network and user/OPEN authentication. Auto-composition assigns initial addresses; manually verify against installed devices. Send/receive configuration over Ethernet or USB; software can request info and update selected .fwz firmware. Do not publish real credentials (RA00079AC_S_EN pp. 4–15).

Retained history: firmware `1.0.7`/software 1.0.28 on 9 April 2013; software 1.0.36 on 10 June 2013; firmware `1.0.21`/software 1.0.40 on 25 February 2014 adds direct floor/room/profile editing and media improvements; 1.0.23 on 18 April 2014 fixes clock accuracy; 1.1.14/software 1.0.53 on 25 November 2014 adds H4691-family Eco/Comfort display and USB improvements; 1.1.15 on 26 March 2015 optimizes sound. The catalogue 2.0/2.1 records are not covered by this release history (Version_History_MH4892_20150326, all 3 PDF pages).

## Source reconciliation

The shared software manual explicitly covers both non-C and C products, but the canonical catalogue keeps items 1768 and 1898 separate. An LCD label alone does not establish resistive sensing technology; that unsupported distinction is not used. The product’s interface objects are settings in a software project, not extra catalogue Module slots. Exact export dimensions and supply replace claims relying solely on an unretained webpage.

All three records designate one Colors Touch Screen Object `32` with no associated Virgin, conditions, relation filters or conversions. Stored `FW_VER` default `3.0.0` differs from firmware tuples 1.0.7/2.0.0/2.1.0 and is not an observed release. Thirty parameter-file associations and Ethernet/USB connection associations are preserved; the software manual's many interface objects are not additional catalogue Module slots. The history ending 26March 2015 does not document the catalogue 2.x lineage.

## Evidence limits and open work

- Exact MH4893/Legrand hardware sheets and later 2.x release history remain unretained; linked install/user manuals and parameter payloads are unexamined.
- The shared manual’s ONVIF/NUVO/network service functions have no release mapping proving applicability to every older firmware tuple.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0041-0050-2026-10-06.md#own-dev-0047)
