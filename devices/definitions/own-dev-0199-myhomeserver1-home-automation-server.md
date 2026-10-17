# MyHOMEServer1 home automation server

## Summary

MyHOMEServer1 connects a MyHOME SCS installation to an Ethernet network and app-based control. It commissions compatible lighting, automation and temperature-control devices, supports other configured MyHOME functions and scenarios, and spans several catalogue firmware generations with different app workflows.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0199` | Project identity |
| Technical description | MyHOMEServer1 home automation server | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `MyHomeServer1` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2198` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration function | Main system association |
| Item model / `modobj` | `67` | Main association; independent of project ID |
| Firmware definition | `729`, `812`, `813`, `814`, `815`, `816`, `817`, `818`, `821`, `825`, `831`, `836`, `839` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `2` | Firmware metadata |
| Categories | Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `MyHomeServer1` | Established catalogue identity | Manufacturer database commercial record `2552` explicitly links this SKU to item `2198` |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `MyHomeServer1` | MyHomeServer | Canonical commercial record `2552` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `RA00149AH_I_EN.pdf` | MyHOME_Up installation manual | `RA00149AH_I_EN; printed publication date not established` | Printed/PDF pp. 7, 11 and commissioning / app / object / scenario sections: limits, historical network-service table, interfaces, users and object association. AH workflow not mapped to catalogue firmware by assumption. | [Archived original](https://archive.openwebnet-ha.org/sha256/65/bb/65bbf9b09ee9236f1e8041178b7cd474ff86225327a92979b09f24d8be836f78.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00149AH_I_EN.pdf) |
| `RA00211AA_I_EN.pdf` | Home+Project installation / configuration manual | `RA00211AA_I-06/22-PC` | Printed/PDF pp. 6, 10-11 and app / commissioning sections: limits, network services, controls / thermostats, account / cloud / system / object / scenario setup; AA generation. | [Archived original](https://archive.openwebnet-ha.org/sha256/8a/4f/8a4fb3fda043ba7c1779b58ecdde1c4eb73c9dd9730825563d5a429617327a1b.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/RA00211AA_I_EN.pdf) |
| `RA00211AB_I_EN.pdf` | Home+Project installation / configuration manual | `RA00211AB_I-06/23-PC` | Printed/PDF pp. 6, 10-11, 35 and app / commissioning sections: limits, network services and local plant creation / management; AB generation; not assigned retroactively to AH. | [Archived original](https://archive.openwebnet-ha.org/sha256/6c/48/6c48f2de37df21782b9f762f60b4260f60b8d5c8e2ebddbdd7410d7c19f7b601.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/RA00211AB_I_EN.pdf) |
| `ST-00001033-EN.pdf` | Classe300EOS external compatibility evidence | `ST-00001033-EN; 04/10/2022` | Printed/PDF p. 8 only: exact MyHOMEServer1, 048834 and K4652M2 entries in another product’s compatibility table; no electrical ratings transferred. | [Archived original](https://archive.openwebnet-ha.org/sha256/e8/54/e854cdd3edff2d77efb06d28600565bbe4c691ef760b6aca7ff16b2cfa8576eb.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00001033-EN.pdf) |
| `legrand-living-now-historical.pdf` | Historical Living Now/MyHOME catalogue | `Printed publication date not established` | Printed/PDF pp. 35, 92, 94-95, 98: exact MyHOMEServer1, F459, K4652M2 and 048834 catalogue descriptions; p. 98 PIR settings and internal threshold / timing discrepancy. | [Archived original](https://archive.openwebnet-ha.org/sha256/f7/2a/f72ab15db14eea29dd1693203fa242c32213717b596bcee9fd2ee96ce7d53e71.pdf) | [Publisher original](https://assets.legrand.com/webf/bg/bg_en_Living_NOW_catalogue.pdf) |
| `ST-00001031-EN.pdf` | Previously archived MyHOME Server technical sheet | `ST-00001031-EN; 30/05/2022` | Printed/PDF pp. 1-4: exact MyHOMEServer1 electrical / interface and system limits; p. 3 explicitly lists 048834 and K4652M2 compatibility. Original publisher URL absent from legacy archival record. | [Archived original](https://archive.openwebnet-ha.org/sha256/14/97/14971697bfbdbb33587b5724c7b38ac2aa6977e05e404556941291cafa589ad7.pdf) | [Previously archived original](https://archive.openwebnet-ha.org/sha256/14/97/14971697bfbdbb33587b5724c7b38ac2aa6977e05e404556941291cafa589ad7.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2198`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `Home-Project-functions-2024-EN.pdf` | Manufacturer Home + Project feature matrix, 2024 edition | Filename labels 2024 REV_5; published URL directory 2025-03; no standalone printed issue date established | Printed/PDF pp. 3–4: exact MyHOMEServer1 2.32.9 minimum and revision-specific feature matrix; compared with later edition | [Archived original](https://archive.openwebnet-ha.org/sha256/fd/53/fd533693372a2afc9d29d1a9fe33df0dcb81932559880b0acda9cb07ff29d490.pdf) | [Publisher source](https://www.bticino.com/sites/default/files/2025-03/NUOVE%20FUNZIONI%20HOME%20%2B%20PROJECT%202024_REV_5_GB.pdf) |
| `Home-Project-functions-2025-EN.pdf` | Manufacturer Home + Project feature matrix, 2025 edition | Filename labels 2025; published URL directory 2025-05; no standalone printed issue date established | Printed/PDF pp. 3–11, 21–22: minimum firmware, visually checked full matrix and backup/offline/update/test/calibration/acquisition/overwrite limits; remaining feature-detail pages outside examined scope | [Archived original](https://archive.openwebnet-ha.org/sha256/97/17/9717ae640f96a24fd8bce8a35cfd12b30f9d5d4a1eafda43a7c99ffd8acbe23e.pdf) | [Publisher source](https://www.bticino.com/sites/default/files/2025-05/NEW%20FUNCTIONS%20HOME%20%2B%20PROJECT%202025_GB.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS / optional auxiliary supply | `18..27 Vdc` | `ST-00001031-EN.pdf` printed/PDF p. 1, retained original dated 30/05/2022 |
| SCS draw without / with auxiliary | `130 mA maximum / 3 mA maximum` | `ST-00001031-EN.pdf` printed/PDF p. 1, retained original dated 30/05/2022 |
| Auxiliary-supply draw | `160 mA maximum` | `ST-00001031-EN.pdf` printed/PDF p. 1, retained original dated 30/05/2022 |
| Operating temperature / mounting | `5..35 °C; 6 DIN modules` | `ST-00001031-EN.pdf` printed/PDF p. 1, retained original dated 30/05/2022 |
| Interfaces / indicators | `Ethernet 10/100; automation SCS; auxiliary supply; USB; RS232; restart; SPEED/LINK/SYSTEM` | `ST-00001031-EN.pdf` printed/PDF p. 1, retained original dated 30/05/2022 |
| System topology limit, sheet | `175 channels; private automation riser level 3; no logical expansion` | `ST-00001031-EN.pdf` printed/PDF p. 1, retained original dated 30/05/2022 |
| Living Now condition, sheet | `Firmware after 2.1 or app after 2.2; wording preserved` | `ST-00001031-EN.pdf` printed/PDF p. 1, retained original dated 30/05/2022 |
| Scenario limits, AA/AB manuals | `50 scenarios; 100 actions and 50 start conditions per scenario` | `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` p. 6 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2198` | Canonical catalogue |
| Technical item description | MyHomeServer | Canonical catalogue |
| Item family | Source placeholder description `0`; key `8` | Canonical catalogue |
| Main system | Integration function; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `67` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `67` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `729` | `1` | `0` | `1` | `2` | Not catalogue default | Official |
| `812` | `1` | `1` | `0` | `2` | Not catalogue default | Official |
| `812` | `1` | `1` | `1` | `2` | Not catalogue default | Official |
| `813` | `1` | `2` | `0` | `2` | Not catalogue default | Official |
| `813` | `1` | `2` | `1` | `2` | Not catalogue default | Official |
| `814` | `2` | `0` | `0` | `2` | Not catalogue default | Official |
| `814` | `2` | `0` | `1` | `2` | Not catalogue default | Official |
| `815` | `2` | `1` | `0` | `2` | Not catalogue default | Official |
| `815` | `2` | `1` | `1` | `2` | Not catalogue default | Official |
| `816` | `2` | `2` | `0` | `2` | Not catalogue default | Official |
| `816` | `2` | `2` | `1` | `2` | Not catalogue default | Official |
| `817` | `2` | `14` | `0` | `2` | Not catalogue default | Official |
| `817` | `2` | `14` | `1` | `2` | Not catalogue default | Official |
| `818` | `2` | `20` | `0` | `2` | Not catalogue default | Official |
| `818` | `2` | `20` | `1` | `2` | Not catalogue default | Official |
| `821` | `2` | `30` | `0` | `2` | Not catalogue default | Official |
| `825` | `2` | `31` | `0` | `2` | Not catalogue default | Official |
| `831` | `2` | `32` | `0` | `2` | Not catalogue default | Official |
| `836` | `3` | `0` | `0` | `2` | Not catalogue default | Official |
| `839` | `2` | `60` | `0` | `2` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `729` | `1054` | Undefined (key `5`) | `0` | Extra | `2198_1.0_LGG\xml\Extra\extra.xml` |
| `729` | `1055` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_1.0_LGG\xml\Protocol\protocol.xml` |
| `812` | `1056` | Undefined (key `5`) | `0` | Extra | `2198_1.1_LGG\xml\Extra\extra.xml` |
| `812` | `1057` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_1.1_LGG\xml\Protocol\protocol.xml` |
| `813` | `1058` | Undefined (key `5`) | `0` | Extra | `2198_1.2_LGG\xml\Extra\extra.xml` |
| `813` | `1059` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_1.2_LGG\xml\Protocol\protocol.xml` |
| `814` | `1060` | Undefined (key `5`) | `0` | Extra | `2198_2.0_LGG\xml\Extra\extra.xml` |
| `814` | `1061` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_2.0_LGG\xml\Protocol\protocol.xml` |
| `815` | `1062` | Undefined (key `5`) | `0` | Extra | `2198_2.1_LGG\xml\Extra\extra.xml` |
| `815` | `1063` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_2.1_LGG\xml\Protocol\protocol.xml` |
| `816` | `1064` | Undefined (key `5`) | `0` | Extra | `2198_2.2_LGG\xml\Extra\extra.xml` |
| `816` | `1065` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_2.2_LGG\xml\Protocol\protocol.xml` |
| `817` | `1066` | Undefined (key `5`) | `0` | Extra | `2198_2.14_LGG\xml\Extra\extra.xml` |
| `817` | `1067` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_2.14_LGG\xml\Protocol\protocol.xml` |
| `818` | `1068` | Undefined (key `5`) | `0` | Extra | `2198_2.20_LGG\xml\Extra\extra.xml` |
| `818` | `1069` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_2.20_LGG\xml\Protocol\protocol.xml` |
| `821` | `1074` | Undefined (key `5`) | `0` | Extra | `2198_2.30_LGG\xml\Extra\extra.xml` |
| `821` | `1075` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_2.30_LGG\xml\Protocol\protocol.xml` |
| `825` | `1097` | Undefined (key `5`) | `0` | Extra | `2198_2.31_LGG\xml\Extra\extra.xml` |
| `825` | `1098` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_2.31_LGG\xml\Protocol\protocol.xml` |
| `831` | `1099` | Undefined (key `5`) | `0` | Extra | `2198_2.32_LGG\xml\Extra\extra.xml` |
| `831` | `1100` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_2.32_LGG\xml\Protocol\protocol.xml` |
| `836` | `1107` | Undefined (key `5`) | `0` | Extra | `2198_3.0_LGG\xml\Extra\extra.xml` |
| `836` | `1108` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_3.0_LGG\xml\Protocol\protocol.xml` |
| `839` | `1109` | Undefined (key `5`) | `0` | Extra | `2198_2.60_LGG\xml\Extra\extra.xml` |
| `839` | `1110` | Undefined (key `5`) | `0` | Protocol and other device parameters | `2198_2.60_LGG\xml\Protocol\protocol.xml` |

All 26 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

There are 13 firmware definitions and 20 retained build rows, all Official with no catalogue-default flag. Every definition places Gateway Object `150` in slot `1` and external Object `216` (database key `512`) in slot `2`. The Object label mentioning F454 is reusable metadata, not a commercial alias or proof of every F454 audiovisual feature. Item fields contain only AID; the network/port/voice fields are reusable Object data, with no attached filters or conversions. All 26 Extra/Protocol parameter associations and their brand key 5 / line key 0 are shown separately. No package payload is present.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `729` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3406` | `150` | `1660` |
| `729` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3407` | `512` | `1661` |
| `812` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3405` | `150` | `1659` |
| `812` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3408` | `512` | `1662` |
| `813` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3404` | `150` | `1658` |
| `813` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3409` | `512` | `1663` |
| `814` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3403` | `150` | `1657` |
| `814` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3410` | `512` | `1664` |
| `815` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3402` | `150` | `1656` |
| `815` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3401` | `512` | `1655` |
| `816` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3399` | `150` | `1653` |
| `816` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3400` | `512` | `1654` |
| `817` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3398` | `150` | `1652` |
| `817` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3397` | `512` | `1651` |
| `818` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3395` | `150` | `1649` |
| `818` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3396` | `512` | `1650` |
| `821` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3413` | `150` | `1667` |
| `821` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3414` | `512` | `1668` |
| `825` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3418` | `150` | `1672` |
| `825` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3419` | `512` | `1673` |
| `831` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3429` | `150` | `1683` |
| `831` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3430` | `512` | `1684` |
| `836` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3437` | `150` | `1691` |
| `836` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3438` | `512` | `1692` |
| `839` | `1` | `150` Gateway Open SCS | Fixed / designated metadata | `3441` | `150` | `1695` |
| `839` | `2` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed / designated metadata | `3442` | `512` | `1696` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `729` | Product Programming | `3` | Canonical firmware/mode association |
| `812` | Product Programming | `3` | Canonical firmware/mode association |
| `813` | Product Programming | `3` | Canonical firmware/mode association |
| `814` | Product Programming | `3` | Canonical firmware/mode association |
| `815` | Product Programming | `3` | Canonical firmware/mode association |
| `816` | Product Programming | `3` | Canonical firmware/mode association |
| `817` | Product Programming | `3` | Canonical firmware/mode association |
| `818` | Product Programming | `3` | Canonical firmware/mode association |
| `821` | Product Programming | `3` | Canonical firmware/mode association |
| `825` | Product Programming | `3` | Canonical firmware/mode association |
| `831` | Product Programming | `3` | Canonical firmware/mode association |
| `836` | Product Programming | `3` | Canonical firmware/mode association |
| `839` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `729` | Ethernet | Canonical firmware/connection association |
| `729` | Ethernet over USB | Canonical firmware/connection association |
| `812` | Ethernet | Canonical firmware/connection association |
| `812` | Ethernet over USB | Canonical firmware/connection association |
| `813` | Ethernet | Canonical firmware/connection association |
| `813` | Ethernet over USB | Canonical firmware/connection association |
| `814` | Ethernet | Canonical firmware/connection association |
| `814` | Ethernet over USB | Canonical firmware/connection association |
| `815` | Ethernet | Canonical firmware/connection association |
| `815` | Ethernet over USB | Canonical firmware/connection association |
| `816` | Ethernet | Canonical firmware/connection association |
| `816` | Ethernet over USB | Canonical firmware/connection association |
| `817` | Ethernet | Canonical firmware/connection association |
| `817` | Ethernet over USB | Canonical firmware/connection association |
| `818` | Ethernet | Canonical firmware/connection association |
| `818` | Ethernet over USB | Canonical firmware/connection association |
| `821` | Ethernet | Canonical firmware/connection association |
| `821` | Ethernet over USB | Canonical firmware/connection association |
| `825` | Ethernet | Canonical firmware/connection association |
| `825` | Ethernet over USB | Canonical firmware/connection association |
| `831` | Ethernet | Canonical firmware/connection association |
| `831` | Ethernet over USB | Canonical firmware/connection association |
| `836` | Ethernet | Canonical firmware/connection association |
| `836` | Ethernet over USB | Canonical firmware/connection association |
| `839` | Ethernet | Canonical firmware/connection association |
| `839` | Ethernet over USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| Firmware scope | 13 canonical definitions; document generations not mapped by assumption | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| App generation | AH: MyHOME_Up; AA/AB: Home+Project and Home+Control | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| Topology | Private automation riser level 3; 175 channel / address limit in named source contexts; no logical expansion | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| Restart / DHCP | 1 s press restarts; 10 s selects dynamic IP; 2 slow/2 fast flashes | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| Fixed IP, technical sheet | 192.168.0.55; public documentation value, not an observed installation | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| AH capacities | 10 areas; 30 rooms per area; 50 objects per room; 50 controls per actuator; 50 favourites; 50 scenarios | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| AH users | 25 accounts; 7 simultaneous local and 4 remote users; 25 saved app connections | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| AA/AB capacities | 30 rooms; AB additionally lists 30 zones per room; 50 objects per room; 50 controls per actuator; 50 scenarios | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| AA/AB installers | 15 installer accounts; 1 simultaneous installer connection | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| Scenario limits | 100 actions and 50 start conditions per scenario in AH/AA/AB | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| AB local mode | Local plant creation / management added; do not assign to AH by inference | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |
| USB descriptions | AH future use; newer sources firmware update; revision-scoped wording | `ST-00001031-EN.pdf` pp. 1-4; `RA00149AH_I_EN.pdf` pp. 7, 11; `RA00211AA_I_EN.pdf` and `RA00211AB_I_EN.pdf` pp. 6, 10-11 |

### Published network services by document generation

These are public documentation values, not observed installation endpoints. Availability and installed network traffic remain uncorroborated. The AH weather-version inequalities are preserved as printed.

| Service | Published endpoint | Port | Protocol | Source generation |
| --- | --- | --- | --- | --- |
| Main server | `myhomeup.bticino.com` | `8000` | `https, wss` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Slave server | `193.178.246.170, 193.178.246.164` | `22` | `ssh` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| NTP | `pool.ntp.org (editable default)` | `123` | `ntp` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Log | `log.bs.iotleg.com` | `5001` | `syslog` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Update | `dispatchregistration.legrand.com` | `443` | `https` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Download | `prodlegrandressourcespkg.blob.core.windows.net` | `443` | `https` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Weather <2.2.X | `api.wunderground.com` | `443` | `https` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Weather >2.1.X | `api.openweathermap.org` | `443` | `https` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Apple push | `api.push.apple.com` | `443` | `https` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Google push | `android.googleapis.com` | `443` | `https` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Email | `User configuration` | `Not specified` | `Not specified` | `RA00149AH_I_EN.pdf` printed/PDF p. 7 |
| Main server | `nv2-bncx.netatmo.net` | `25050` | `tcp` | `RA00211AA_I_EN.pdf` printed/PDF p. 6 |
| NTP | `pool.ntp.org (editable default)` | `123` | `ntp` | `RA00211AA_I_EN.pdf` printed/PDF p. 6 |
| Log | `log.bs.iotleg.com` | `5001` | `syslog` | `RA00211AA_I_EN.pdf` printed/PDF p. 6 |
| Download | `n3tfw.blob.core.windows.net` | `443` | `https` | `RA00211AA_I_EN.pdf` printed/PDF p. 6 |
| Email | `User configuration` | `Not specified` | `Not specified` | `RA00211AA_I_EN.pdf` printed/PDF p. 6 |
| Main server | `nv2-bncx.netatmo.net` | `25050` | `tcp` | `RA00211AB_I_EN.pdf` printed/PDF p. 6 |
| NTP | `pool.ntp.org (editable default)` | `123` | `ntp` | `RA00211AB_I_EN.pdf` printed/PDF p. 6 |
| Log | `log.bs.iotleg.com` | `5001` | `syslog` | `RA00211AB_I_EN.pdf` printed/PDF p. 6 |
| Download | `n3tfw.blob.core.windows.net` | `443` | `https` | `RA00211AB_I_EN.pdf` printed/PDF p. 6 |
| Email | `User configuration` | `Not specified` | `Not specified` | `RA00211AB_I_EN.pdf` printed/PDF p. 6 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `729` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `812` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `813` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `814` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `815` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `816` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `817` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `818` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `821` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `825` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `831` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `836` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `839` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `216` - Enhanced Web Server Audio/Video 2 Wires (F454)

Catalogue Object key `512` maps to external Object `216`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address; public documentation value, not an observed installation |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` | Public IP address; public documentation value, not an observed installation |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `VCD_PORT` | `#####` = Video port | `10000` | Video port |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `67` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `150` - Gateway Open SCS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `216` - Enhanced Web Server Audio/Video 2 Wires (F454) | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `150` - Gateway Open SCS | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `216` - Enhanced Web Server Audio/Video 2 Wires (F454) | Integration function | `26` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Later app / server revision requirements

Both retained feature documents require MyHOMEServer1 firmware `2.32.9` or later for Home + Project (p. 3). The 2025 p. 4 matrix gives the following exact MyHOMEServer1/app entries; dashes are unassigned matrix values, not a supported/unsupported conclusion. These later releases are absent from the canonical snapshot and are not retroactively assigned to `831: 2.32.0` or `836: 3.0.0`.

| Feature | Published server firmware | Published Home + Project app |
| --- | --- | --- |
| Backup / restore | 3.83.3 | 1.0.37 |
| System function test | 3.82.10 | 1.0.35 |
| Device-address export | Not specified (dash) | 1.0.35 |
| Offline configuration | Not specified (dash) | 1.0.21 |
| App firmware update | 3.71.11 | 1.0.20 |
| Identify loads | 3.71.31 | 1.0.24 |
| Temperature probe calibration | 2/3.81.x | 1.0.32 |
| Multiple controls per actuator | Not specified (dash) | 1.0.40 |
| Automatic control/actuator association | Not specified (dash) | 1.0.40 |
| Connection stability | Not specified (dash) | 1.0.40 |
| Tablet compatibility | Not specified (dash) | 1.0.41 |
| Device replacement | Not specified (dash) | 1.0.42 |
| Control/energy-display configuration | Not specified (dash) | Not specified (dash) |
| App evaluation pop-up | Not specified (dash) | 1.0.45 |
| Quick device identification | Not specified (dash) | 1.0.45 |
| New advanced MyHOME functions | Not specified (dash) | Not specified (dash) |
| Acquire existing plant configuration | 3.84.5 | 1.1.12 |
| Overwrite control/actuator association | 3.84.9 | 1.1.16 |
| DALI2 colour definition | Not specified (dash) | Not specified (dash) |

The 2024 matrix agrees on the first 15 entries. The 2025 matrix adds later features and separate F460/461 columns, which were visually checked to avoid transferring their requirements. Feature 17 prose describes acquisition using F460/Classe300EOS, while its matrix also supplies a MyHOMEServer1 version; that wording difference remains explicit and is not a verified migration/support guarantee.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The older `RA00149AH_I_EN.pdf` documents MyHOME_Up commissioning, users, rooms, object association and scenarios; `RA00211AA_I_EN.pdf` (06/22) and `RA00211AB_I_EN.pdf` (06/23) describe Home+Project/Home+Control. AB adds local plant creation / management; do not assume one app workflow applies to all 13 catalogue Firmware definitions. The retained sheet states firmware update via MyHOME Suite/USB. Short restart press is 1 second; long 10-second press selects DHCP, with two slow / two fast LED flashes. The public sheet’s fixed address is `192.168.0.55`: public documentation value, not an observed installation.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

The newer feature guide limits backup to plants configured with Home + Project and excludes user-created temperature programmes, scenarios, notifications and scheduled automations from that backup (2025 p. 5). Offline configuration stores data for later cloud synchronisation; the AB manual additionally warns that prior desktop work is not recovered unless synchronised through the app (AB p. 35; 2025 p. 8). Firmware update downloads from cloud to the phone, then transfers locally to the server, including offline transfer (2025 p. 9). Device association overwrite excludes dehumidification and season-change actuators because they are functions rather than logical objects (2025 p. 22). These procedures depend on the stated app/server versions; their availability is not inferred from old catalogue Objects.

## Source reconciliation

The already archived 2022 exact technical sheet was reused by verified fingerprint. The old MyHOME_Up manual names 10 areas and 30 rooms per area; AA lists 30 rooms; AB additionally lists 30 zones per room, with 15 installer accounts and one installer connection. Their network-service tables and app workflows differ by document generation. USB is “future uses” in AH but firmware update in the newer manuals / sheet. These changes are revision-scoped and not retroactively mapped to a particular catalogue Firmware without evidence. The Classe300EOS compatibility sheet names the server as an integration component but does not replace its own technical sheet.

The exact 2022 technical sheet gives public documentation fixed IP `192.168.0.55`; reusable Objects 150/216 instead default to `192.168.1.35`. These are source-specific documentation templates, not observed endpoints, and no firmware applicability mapping resolves them. AA (06/22) lists 30 rooms, but the 30-zones-per-room limit is added in AB (06/23); the previous combined capacity statement incorrectly assigned it to AA as well. Historical network service tables remain edition-scoped rather than instructions for present-day firewall setup.

## Evidence limits and open work

Installed app/Firmware pairing, mapping of all catalogue tuples to document generations, exact cloud-service behavior, network endpoints and available third-party integrations remain to be corroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

The later 2024/2025 feature matrices establish explicit app-version requirements but not installed state or payload behavior. Feature-detail pages 12–20 and 23 beyond the inspected matrix remain outside this review scope. The old exact-product export lead redirected to an unavailable product URL (HTTP 404); its search-only EAN was not adopted. Current firmware binaries and parameter payloads were not examined.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0191-0200-2026-10-07.md#own-dev-0199)
