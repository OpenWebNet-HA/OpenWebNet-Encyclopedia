# MyHOME_Screen 3.5

## Summary

MyHOME_Screen 3.5 is a wall touchscreen for controlling configured lighting, automation, temperature and scenarios. Its 3.5-inch display brings several MyHOME functions into one interface, programmed through dedicated PC software.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0015` | Project identity |
| Technical description | 3.5-inch MyHOME touchscreen user interface | Catalogue + official documentation |
| Catalogue item | `1469` - “MyHOME_Screen 3.5” | Implementation evidence |
| Main catalogue system | Integration functions | Implementation evidence |
| Item model / `modobj` | `30` | Implementation evidence |
| Firmware definition | `1.0.17`, `2.0.3`, `3.0.8/9/10`, `4.0.0` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Configuration mode | Product Programming | Implementation evidence |
| Programming connections | Ethernet, USB | Implementation evidence |
| Categories | User Interface, Integration, Multifunction | Product and capability model |

MyHOME_Screen 3.5 is a touchscreen user interface for multiple MyHOME systems. The catalogue represents all eight commercial records with one fixed `Colors Touch Screen` Object and several firmware applicability records.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4890` | Established identity | Catalogue + archived technical sheet |
| BTicino - LivingLight | `LN4890` | Established identity | Catalogue + archived technical sheet |
| BTicino - Air | `LN4890A` | Established identity | Catalogue + archived technical sheet |
| BTicino - Eteris | `HW4890` | Established identity | Catalogue + archived technical sheet |
| BTicino - Matix | `AM4890` | Established identity with source-label inconsistency | Catalogue + installation text in archived technical sheet |
| Legrand - Arteor | `573958` | Established catalogue identity | Implementation evidence |
| Legrand - Céliane | `067292` | Established catalogue identity | Implementation evidence |
| Legrand - Mosaic | `078479` | Established catalogue identity | Implementation evidence |

The archived technical sheet contains an internal reference discrepancy: its heading lists `AM5890`, while the installation/reference text uses `AM4890`, matching the canonical catalogue. Preserve the source discrepancy rather than silently rewriting the PDF.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `LN4890` | `8005543450161` | [Archived original](https://archive.openwebnet-ha.org/sha256/5f/69/5f69dfbb60aca1ce1a1e6365be201d3697604de49cd5fc004a4ed2cf66539c86.pdf), `LN4890-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `078479` | `3245060784799` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/78/3e/783e8b0f78202d1816ad4f7062b96a4cb8826730c8b475ecd8a6fa1db91d1720.pdf), `078479-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00518_a_EN` | Technical sheet | No dated imprint established in inspected original | BTicino MyHOME_Screen 3.5 family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/43/61/4361119dc3e9e028cacb247fcb8b8faae15acad73c0bd2fd73bcfb65b90924c9.pdf) | publisher source not currently retained |
| `RA00107AC_U_EN` | User guide | No dated imprint established in inspected original | MyHOME_Screen 3.5 family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/28/33/2833c50e275c23816dfaad7ddb25571e97c73097652c61e5df5eb43e8d7bce23.pdf) | publisher source not currently retained |
| `RA00107AC_S_FR` | Software manual | No dated imprint established in inspected original | MyHOME_Screen 3.5 family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/06/fd/06fd9db38da00c9f208531163142a19bafd6b8801e255cb48a876adedc7bcfa5.pdf) | publisher source not currently retained |
| `LN4890-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4890` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/5f/69/5f69dfbb60aca1ce1a1e6365be201d3697604de49cd5fc004a4ed2cf66539c86.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4890) |
| `078479-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `078479` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/78/3e/783e8b0f78202d1816ad4f7062b96a4cb8826730c8b475ecd8a6fa1db91d1720.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/commande-tactile-mosaic-multiscenarios-pour-eclairage-ouvrant-et-multimedias) |

Direct product sheets for the Legrand commercial variants and additional language revisions remain desirable archival sources.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | 3.5-inch touch LCD | `BT00518_a_EN` |
| Mounting | documented `3+3` module arrangement | `BT00518_a_EN` + Source reconciliation |
| SCS nominal supply | `27 Vdc` | `BT00518_a_EN` |
| SCS operating supply | `18..27 Vdc` | `BT00518_a_EN` |
| Current draw | `80 mA` | `BT00518_a_EN` |
| Operating temperature | `0..40 °C` | `BT00518_a_EN` |
| Interfaces by named variant | USB-miniUSB and SCS; Ethernet illustrated for H4890/LN4890/LN4890A/AM4890, while HW4890 diagram shows USB | `BT00518_a_EN`, pp. 1–2 |

Programming/configuration is performed with dedicated PC software over the supported local interfaces.

| Property | Value | Evidence |
| --- | --- | --- |
| Flush box | `506E` for AM4890/LN4890/LN4890A/H4890; `528W` for HW4890 | BT00518_a_EN, p. 1 |
| Historical cable choices | 335919 RS232 or 3559 USB interface, or Ethernet, stated in the general TiTouchScreen paragraph | Same source, p. 2; not proof all variants have RS232/Ethernet ports |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1469` | Implementation evidence |
| Main system | Integration functions | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `30` | Implementation evidence |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `30` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Burglar alarm | private riser | Canonical item/bus relationship |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `8` | `2` | `0` | `3` | `1` | Not catalogue default | Official |
| `9` | `3` | `0` | `8` | `1` | Catalogue default | Official |
| `9` | `3` | `0` | `9` | `1` | Catalogue default | Official |
| `9` | `3` | `0` | `10` | `1` | Catalogue default | Official |
| `75` | `1` | `0` | `17` | `1` | Not catalogue default | Official |
| `692` | `4` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue applicability does not prove the firmware installed on every commercial variant.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `8` | `78` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `8` | `80` | BTicino (key `1`) | `0` | Extra | `1469_2.0_BT\xml\Extra\extra.xml` |
| `8` | `81` | BTicino (key `1`) | `0` | Director | `1469_2.0_BT\xml\DIRECTOR\director.xml` |
| `8` | `82` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1469_2.0_BT\xml\Protocol\protocol.xml` |
| `8` | `132` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `8` | `134` | Legrand (key `2`) | `0` | Extra | `1469_2.0_LG\xml\Extra\extra.xml` |
| `8` | `135` | Legrand (key `2`) | `0` | Director | `1469_2.0_LG\xml\DIRECTOR\director.xml` |
| `8` | `136` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1469_2.0_LG\xml\Protocol\protocol.xml` |
| `8` | `157` | BTicino (key `1`) | `0` | BS | `1469_2.0_BT\xml\BS` |
| `8` | `158` | Legrand (key `2`) | `0` | BS | `1469_2.0_LG\xml\BS` |
| `8` | `254` | BTicino (key `1`) | `0` | SVM | `1469_2.0_BT\xml\SVM\svm.xml` |
| `8` | `256` | Legrand (key `2`) | `0` | SVM | `1469_2.0_LG\xml\SVM\svm.xml` |
| `9` | `88` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `9` | `90` | BTicino (key `1`) | `0` | Extra | `1469_3.0_BT\xml\Extra\extra.xml` |
| `9` | `91` | BTicino (key `1`) | `0` | Director | `1469_3.0_BT\xml\DIRECTOR\director.xml` |
| `9` | `92` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1469_3.0_BT\xml\Protocol\protocol.xml` |
| `9` | `137` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `9` | `139` | Legrand (key `2`) | `0` | Extra | `1469_3.0_LG\xml\Extra\extra.xml` |
| `9` | `140` | Legrand (key `2`) | `0` | Director | `1469_3.0_LG\xml\DIRECTOR\director.xml` |
| `9` | `141` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1469_3.0_LG\xml\Protocol\protocol.xml` |
| `9` | `159` | BTicino (key `1`) | `0` | BS | `1469_3.0_BT\xml\BS` |
| `9` | `160` | Legrand (key `2`) | `0` | BS | `1469_3.0_LG\xml\BS` |
| `9` | `255` | BTicino (key `1`) | `0` | SVM | `1469_3.0_BT\xml\SVM\svm.xml` |
| `9` | `257` | Legrand (key `2`) | `0` | SVM | `1469_3.0_LG\xml\SVM\svm.xml` |
| `75` | `20` | BTicino (key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `75` | `22` | BTicino (key `1`) | `0` | Extra | `1469_1.0_BT\xml\Extra\extra.xml` |
| `75` | `23` | BTicino (key `1`) | `0` | Director | `1469_1.0_BT\xml\DIRECTOR\director.xml` |
| `75` | `24` | BTicino (key `1`) | `0` | Protocol and other device parameters | `1469_1.0_BT\xml\Protocol\protocol.xml` |
| `75` | `127` | Legrand (key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `75` | `129` | Legrand (key `2`) | `0` | Extra | `1469_1.0_LG\xml\Extra\extra.xml` |
| `75` | `130` | Legrand (key `2`) | `0` | Director | `1469_1.0_LG\xml\DIRECTOR\director.xml` |
| `75` | `131` | Legrand (key `2`) | `0` | Protocol and other device parameters | `1469_1.0_LG\xml\Protocol\protocol.xml` |
| `75` | `253` | BTicino (key `1`) | `0` | SVM | `1469_1.0_BT\xml\SVM\svm.xml` |
| `75` | `258` | Legrand (key `2`) | `0` | SVM | `1469_1.0_LG\xml\SVM\svm.xml` |
| `692` | `846` | BTicino (key `1`) | `3` | SDC | `xml\SDC\sdc.xml` |
| `692` | `847` | BTicino (key `1`) | `3` | SVM | `1469_4.0_BT\xml\SVM\svm.xml` |
| `692` | `848` | BTicino (key `1`) | `3` | Extra | `1469_4.0_BT\xml\Extra\extra.xml` |
| `692` | `849` | BTicino (key `1`) | `3` | Director | `1469_4.0_BT\xml\DIRECTOR\director.xml` |
| `692` | `850` | BTicino (key `1`) | `3` | Protocol and other device parameters | `1469_4.0_BT\xml\Protocol\protocol.xml` |
| `692` | `851` | BTicino (key `1`) | `3` | BS | `1469_4.0_BT\xml\BS` |
| `692` | `852` | BTicino (key `1`) | `1` | SDC | `xml\SDC\sdc.xml` |
| `692` | `853` | BTicino (key `1`) | `1` | SVM | `1469_4.0_BT\xml\SVM\svm.xml` |
| `692` | `854` | BTicino (key `1`) | `1` | Extra | `1469_4.0_BT\xml\Extra\extra.xml` |
| `692` | `855` | BTicino (key `1`) | `1` | Director | `1469_4.0_BT\xml\DIRECTOR\director.xml` |
| `692` | `856` | BTicino (key `1`) | `1` | Protocol and other device parameters | `1469_4.0_BT\xml\Protocol\protocol.xml` |
| `692` | `857` | BTicino (key `1`) | `1` | BS | `1469_4.0_BT\xml\BS` |
| `692` | `858` | BTicino (key `1`) | `2` | SDC | `xml\SDC\sdc.xml` |
| `692` | `859` | BTicino (key `1`) | `2` | SVM | `1469_4.0_BT\xml\SVM\svm.xml` |
| `692` | `860` | BTicino (key `1`) | `2` | Extra | `1469_4.0_BT\xml\Extra\extra.xml` |
| `692` | `861` | BTicino (key `1`) | `2` | Director | `1469_4.0_BT\xml\DIRECTOR\director.xml` |
| `692` | `862` | BTicino (key `1`) | `2` | Protocol and other device parameters | `1469_4.0_BT\xml\Protocol\protocol.xml` |
| `692` | `863` | BTicino (key `1`) | `2` | BS | `1469_4.0_BT\xml\BS` |
| `692` | `864` | Legrand (key `2`) | `2` | SDC | `xml\SDC\sdc.xml` |
| `692` | `865` | Legrand (key `2`) | `2` | SVM | `1469_4.0_LG\xml\SVM\svm.xml` |
| `692` | `866` | Legrand (key `2`) | `2` | Extra | `1469_4.0_LG\xml\Extra\extra.xml` |
| `692` | `867` | Legrand (key `2`) | `2` | Director | `1469_4.0_LG\xml\DIRECTOR\director.xml` |
| `692` | `868` | Legrand (key `2`) | `2` | Protocol and other device parameters | `1469_4.0_LG\xml\Protocol\protocol.xml` |
| `692` | `869` | Legrand (key `2`) | `2` | BS | `1469_4.0_LG\xml\BS` |
| `692` | `870` | Legrand (key `2`) | `4` | SDC | `xml\SDC\sdc.xml` |
| `692` | `871` | Legrand (key `2`) | `4` | SVM | `1469_4.0_LG\xml\SVM\svm.xml` |
| `692` | `872` | Legrand (key `2`) | `4` | Extra | `1469_4.0_LG\xml\Extra\extra.xml` |
| `692` | `873` | Legrand (key `2`) | `4` | Director | `1469_4.0_LG\xml\DIRECTOR\director.xml` |
| `692` | `874` | Legrand (key `2`) | `4` | Protocol and other device parameters | `1469_4.0_LG\xml\Protocol\protocol.xml` |
| `692` | `875` | Legrand (key `2`) | `4` | BS | `1469_4.0_LG\xml\BS` |
| `692` | `876` | Legrand (key `2`) | `3` | SDC | `xml\SDC\sdc.xml` |
| `692` | `877` | Legrand (key `2`) | `3` | SVM | `1469_4.0_LG\xml\SVM\svm.xml` |
| `692` | `878` | Legrand (key `2`) | `3` | Extra | `1469_4.0_LG\xml\Extra\extra.xml` |
| `692` | `879` | Legrand (key `2`) | `3` | Director | `1469_4.0_LG\xml\DIRECTOR\director.xml` |
| `692` | `880` | Legrand (key `2`) | `3` | Protocol and other device parameters | `1469_4.0_LG\xml\Protocol\protocol.xml` |
| `692` | `881` | Legrand (key `2`) | `3` | BS | `1469_4.0_LG\xml\BS` |
| `692` | `882` | BTicino (key `1`) | `9` | SDC | `xml\SDC\sdc.xml` |
| `692` | `883` | BTicino (key `1`) | `9` | SVM | `1469_4.0_BT\xml\SVM\svm.xml` |
| `692` | `884` | BTicino (key `1`) | `9` | Extra | `1469_4.0_BT\xml\Extra\extra.xml` |
| `692` | `885` | BTicino (key `1`) | `9` | Director | `1469_4.0_BT\xml\DIRECTOR\director.xml` |
| `692` | `886` | BTicino (key `1`) | `9` | Protocol and other device parameters | `1469_4.0_BT\xml\Protocol\protocol.xml` |
| `692` | `887` | BTicino (key `1`) | `9` | BS | `1469_4.0_BT\xml\BS` |
| `692` | `888` | BTicino (key `1`) | `10` | SDC | `xml\SDC\sdc.xml` |
| `692` | `889` | BTicino (key `1`) | `10` | SVM | `1469_4.0_BT\xml\SVM\svm.xml` |
| `692` | `890` | BTicino (key `1`) | `10` | Extra | `1469_4.0_BT\xml\Extra\extra.xml` |
| `692` | `891` | BTicino (key `1`) | `10` | Director | `1469_4.0_BT\xml\DIRECTOR\director.xml` |
| `692` | `892` | BTicino (key `1`) | `10` | Protocol and other device parameters | `1469_4.0_BT\xml\Protocol\protocol.xml` |
| `692` | `893` | BTicino (key `1`) | `10` | BS | `1469_4.0_BT\xml\BS` |

All 82 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

| Firmware | GL | Version | Release | Build | Unicode set | Name | Package record |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `8` | `1` | `2` | `0` | `0` | `1` | `GL1` | `20` |
| `8` | `21` | `2` | `0` | `0` | `2` | `GL21` | `21` |
| `8` | `31` | `2` | `0` | `0` | `3` | `GL31` | `22` |
| `8` | `42` | `2` | `0` | `0` | `4` | `GL42` | `23` |
| `8` | `51` | `2` | `0` | `0` | `5` | `GL51` | `24` |
| `9` | `1` | `3` | `0` | `0` | `1` | `GL1` | `25` |
| `9` | `21` | `3` | `0` | `0` | `2` | `GL21` | `26` |
| `9` | `31` | `3` | `0` | `0` | `3` | `GL31` | `27` |
| `9` | `42` | `3` | `0` | `0` | `4` | `GL42` | `28` |
| `9` | `51` | `3` | `0` | `0` | `5` | `GL51` | `29` |
| `75` | `1` | `1` | `1` | `0` | `1` | `GL1` | `7` |
| `75` | `21` | `1` | `1` | `0` | `2` | `GL21` | `8` |
| `75` | `31` | `1` | `1` | `0` | `3` | `GL31` | `9` |
| `75` | `42` | `1` | `1` | `0` | `4` | `GL42` | `10` |
| `75` | `51` | `1` | `1` | `0` | `5` | `GL51` | `11` |
| `692` | `1` | `4` | `0` | `0` | `1` | `GL1` | `39` |
| `692` | `21` | `4` | `0` | `0` | `2` | `GL21` | `40` |
| `692` | `31` | `4` | `0` | `0` | `3` | `GL31` | `41` |
| `692` | `42` | `4` | `0` | `0` | `4` | `GL42` | `42` |
| `692` | `51` | `4` | `0` | `0` | `5` | `GL51` | `43` |

These are catalogue package metadata; package payloads and Unicode-set contents have not been inspected.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `8` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1311` | `32` | `671` |
| `9` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1312` | `32` | `672` |
| `75` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1313` | `32` | `673` |
| `692` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2576` | `32` | `1195` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

There is no Virgin Object and no slot-condition row.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `8` | Product Programming | `3` | Canonical firmware/mode association |
| `9` | Product Programming | `3` | Canonical firmware/mode association |
| `75` | Product Programming | `3` | Canonical firmware/mode association |
| `692` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `8` | Ethernet | Canonical firmware/connection association |
| `8` | USB | Canonical firmware/connection association |
| `9` | Ethernet | Canonical firmware/connection association |
| `9` | USB | Canonical firmware/connection association |
| `75` | Ethernet | Canonical firmware/connection association |
| `75` | USB | Canonical firmware/connection association |
| `692` | Ethernet | Canonical firmware/connection association |
| `692` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `8` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `8` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `8` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `8` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `9` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `9` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `9` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `9` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `75` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `75` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `75` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `75` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `692` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `692` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `692` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `692` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

Actual IP addresses and installation identifiers are private installation state and must not be copied into the public Device Library from research captures.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Device-specific interpretation

The single Colors Touch Screen Object holds product identity/network configuration, rather than enumerating all UI functions. Template `FW_VER=3.0.0` on all four firmware definitions differs from the enclosing versions and is not an installed-version observation. Physical interfaces remain commercial-variant scoped.

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
| `DIMENSION 1` | identify item model `30`, brand and line | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe actual installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate one fixed Colors Touch Screen Object | [Modules](../../diagnostics/dim30-modules.md) |

Other diagnostic/programming surfaces should only be claimed after hardware observation or explicit implementation evidence.

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Lighting / automation | Individual/group/general commands, timed lighting, 10/100-level dimmers, PUL targets, shutter/door movement; advanced actuator position where supported | RA00107AC_S_FR, pp. 21–24; RA00107AC_U_EN, pp. 9–15 |
| Thermoregulation | 4/99-zone central units, zone setpoints, season programs, 99-zone scenarios, fan-coil, external/measured-only probes | Software pp. 25–28; User pp. 23–42 |
| Air conditioning / HVAC | 3456 Basic saved commands (`1..20`) or Advanced controls with feature-dependent temperature step 0.5/1 °C; F450/BACnet gateway path | Software pp. 9, 29–36 |
| Burglar alarm | Eight-zone display and user-code-protected arming/disarming/zone exclusion where configured | Software p. 25; User pp. 43–45 |
| Sound / multimedia | Single/multichannel sources/amplifiers, multimedia source with 3496, configured IP radio/media servers; NuVo requires that system | Software pp. 8, 38–42; User pp. 46–59 |
| Video door entry | Configured lock/stair-light controls; depends on wiring to automation or video bus and associated handset address | Software pp. 8, 21–22, 37; User p. 60 |
| Scenarios | F420 up to sixteen; local advanced condition/time actions; programmed CEN/CEN PLUS Start/Stop and Enable/Disable | Software pp. 43–45; User pp. 16–22 |
| Energy / loads | Electricity/gas/water/heating/hot-water display; load priorities `1..63`; central-unit shedding differs from consumption-only control without a central unit | Software pp. 46–51; User pp. 61–73 |
| System supervision | Configured Stop&Go address `1..127` (up to twenty devices); load earth-leakage diagnostics address `1..63` | Software pp. 47–48; User pp. 62–65 |

These application capabilities belong to the RA00107AC manual/software scope; no minimum firmware build for each feature is established. The earlier technical sheet gives up to twenty actuations per application. Neither count expands the catalogue’s single Object `32` into extra protocol Modules.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

The historical sheet names TiTouchScreen and RS232/USB/Ethernet transfer choices; the RA00107AC software manual describes USB-miniUSB or Ethernet with the Screen connected to the bus. Keep physical commercial interfaces scoped as above rather than inferring all ports from firmware connection associations.

The software project controls clock-master role, temperature unit, automation bus level/interface, video-door-entry wiring/handset association, multimedia address, optional F450 gateway and standby landing page (pp. 8–15). Its level labels use private riser=3/local bus=4, which must not be substituted for another namespace’s encodings. Send/receive configuration and firmware update are product workflows, distinct from Object `32`’s small network/identity surface. Actual addresses, credentials and installation names remain private state.

UI customization includes clean-screen inhibit 10 seconds to 1 minute, touch calibration, standby brightness/screensaver, transition effects, alarm-clock sound-system targets and Favorites (software pp. 16–20, 52–53; user pp. 74–83). The local UI password has five digits; it is separate from the OPEN remote-access password configured in software. No installation password is reproduced here.

## Source reconciliation

The MyHOME_Screen 3.5 technical/user/software documents establish product details beyond its fixed catalogue role:

- the product occupies a `3+3` module mounting arrangement and uses different installation accessories/boxes depending on the variant, including the documented `506E` versus `528W` context;
- PC programming/transfer paths include the documented RS232 lead `335919`, USB accessory `3559`, or Ethernet depending on the commercial variant;
- TiTouchScreen project configuration includes conditional scenarios, date/time presentation, password protection and configurable graphical/icon content;
- these user-interface/project functions are product-programming capabilities and must not be mistaken for extra OpenWebNet Modules.

The remaining completeness issues concern direct Legrand-variant documentation, the `AM4890`/`AM5890` source discrepancy and hardware fingerprints.

BT00518_a_EN is internally labelled BT00518-a-UK and has no established dated imprint. Its heading AM5890 conflicts with installation text AM4890 and the catalogue. Its general programming paragraph includes historical RS232 cables, while the connection drawings distinguish HW4890 from the Ethernet-capable illustrated variants. The RA00107AC software/user manuals describe expanded applications without mapping each to catalogue firmware/builds. Their feature availability is therefore manual-scoped, not backdated to every 1.0.17 unit.

The French software Automation paragraph says Normal movement stops on release but also requires Stop; Safe mode unambiguously follows the held key. That internal wording conflict remains unresolved. The English user load-management pages state four hours for reactivation (p. 71) and 2 h 30 min in the details screen (p. 72); these are preserved as different UI/source contexts, not one normalized default. Energy tariff values are indicative, not billing measurements. The template FW_VER value and physical interface differences remain explicit.

## Evidence limits and open work

- Add sanitized hardware fingerprints across more than one product line.
- Correlate observed installed firmware with the four catalogue firmware families.
- Locate direct official product sheets for `573958`, `067292` and `078479`.
- Resolve the archived technical-sheet `AM5890` / `AM4890` discrepancy through additional revisions.
- Archive English/Italian/French software and user-document revisions where distinct.
- Establish feature-to-firmware applicability for the RA00107AC application set, including NuVo/BACnet/energy additions. Resolve the Normal-mode release/Stop wording and load-forcing UI default discrepancy.
- Inspect the referenced parameter and package payloads before inferring content from the 82 parameter associations or package names.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)

- `LN4890-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4890` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/5f/69/5f69dfbb60aca1ce1a1e6365be201d3697604de49cd5fc004a4ed2cf66539c86.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4890); SHA-256 `5f69dfbb60aca1ce1a1e6365be201d3697604de49cd5fc004a4ed2cf66539c86`.

- `078479-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `078479` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/78/3e/783e8b0f78202d1816ad4f7062b96a4cb8826730c8b475ecd8a6fa1db91d1720.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/commande-tactile-mosaic-multiscenarios-pour-eclairage-ouvrant-et-multimedias); SHA-256 `783e8b0f78202d1816ad4f7062b96a4cb8826730c8b475ecd8a6fa1db91d1720`.

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0011-0020-2026-10-05.md#own-dev-0015)
