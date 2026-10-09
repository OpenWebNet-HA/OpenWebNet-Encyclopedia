# Audio/video web server and OpenWebNet gateway

## Summary

The F454 is a MyHOME audio/video web server and OpenWebNet gateway. It brings configured home controls and video-door-entry functions into a web interface, with Ethernet access and separate SCS connections for automation and audio/video systems.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0002` | Project identity |
| Technical description | Audio/video web server and OpenWebNet gateway | Catalogue + vendor documentation |
| Commercial identities | BTicino `F454`; Legrand `0 035 98` / catalogue `003598` | Catalogue + vendor documentation |
| Catalogue item | `1455` - “Web Server A/V Bus” | Implementation evidence |
| Main catalogue system | Integration functions (`id_system = 26`) | Implementation evidence |
| Item model / `modobj` | `51` | Implementation evidence |
| Catalogue brand / line | `BRAND = 5`; `LINE = 0` | Implementation evidence |
| Firmware definition | `1.0.37`, `2.0.1` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Gateway, Interface, Audio / Video | Catalogue + vendor documentation |

## Commercial identities

| Brand / range | SKU / reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F454` | Established commercial identity | Catalogue + vendor documentation + observed gateway identity |
| Legrand | `0 035 98` / `003598` | Equivalent commercial reference | Vendor firmware history + same catalogue item |

F453 and F453AV are predecessor products named by vendor documentation. They are not synonyms and remain separate technical Devices.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00519-c-EN` | Technical sheet | 06/05/2015; printed p. 499 / PDF p. 1 | Whole Device-specific document, PDF pp. 1-1; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/5f/36/5f36d8d5985f516f393c19ed4fbacdf2c40ca40c08cf023d08fd45baf36fe8f6.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00519-c-EN.pdf) |
| `O1755J_U_EN` | User manual | No dated imprint established in the inspected original | Whole Device-specific document, PDF pp. 1-80; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/34/17/3417dbd9acbff4c2feb329a722e8e24cc2c313ad3af85e1ea30b8ff44343cd08.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1755J_U_EN.pdf) |
| `O1755H_S_EN` | Software manual | No dated imprint established in the inspected original | Whole Device-specific document, PDF pp. 1-56; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/41/8c/418cd9a3e38720b4c5660e07a8f24970253ace23a4a825d597c4489b6c8282f5.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1755H_S_EN.pdf) |
| `O1754E` | Instruction sheet | Printed `O1754E-01PC-17W15` | Whole Device-specific document, PDF pp. 1-2; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/d4/7f/d47faf013abb6f55e08f149365f3b98d86240b34b30f24c9eeea1de1505e3ff6.pdf) | [Official source](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileName=O1754E.pdf&fileId=58107.23188.62294.22284) |
| `Version_History_F454_20170508` | Firmware version history | Latest listed release 08/05/2017 | Whole Device-specific document, PDF pp. 1-2; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/c9/60/c960937a4d19e52342c1af618782e715e75e1e181a7804d012096afec99834a3.pdf) | [Official source](https://www.homesystems-legrandgroup.com/documents/2416083/2422856/Version_History_F454_20170508.pdf/1f3644de-73a3-5332-3ff3-b12596cc53df?t=1595605650159) |
| `O1755G_U_EN` | Earlier English user manual revision | No dated imprint established in the inspected original | Whole Device-specific document, PDF pp. 1-50; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/f1/d4/f1d437d369f5a217c4094128c8841f3d2171381ba0f321f0dfa52e30177e2460.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1755G_U_EN.pdf) |
| `O1755G_S_EN` | Earlier English software manual revision | No dated imprint established in the inspected original | Whole Device-specific document, PDF pp. 1-46; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/bc/d6/bcd66d983153fc8911022f52c6dd78605fb9533846e5bca05b46c4ac118a8bea.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1755G_S_EN.pdf) |
| `O1754C` | Additional instruction-sheet revision | No dated imprint established in the inspected original | Whole Device-specific document, PDF pp. 1-2; applies to this documented product family | [Archived original](https://archive.openwebnet-ha.org/sha256/8b/e3/8be3d653dbd0cf01cb4ac1de7976100c355719a5851cc6e0ed03c07d4a6856ff.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1754C.pdf) |
| `F454_020051.fwz` | Firmware package | `2.0.51`; release 08/05/2017 | Firmware binary; privately archived, payload not inspected in this review | Private archive; `firmware-f454-020051` in [artifact manifest](../../sources/artifact-manifest.yaml) | [Vendor archive](https://www.homesystems-legrandgroup.com/home/-/productsheets/2463476) |

Language variants should be retained separately when their bytes or content differ.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Width | 6 DIN modules | `MQ00519-c-EN`, printed p. 499 / PDF p. 1 |
| Supply | `18..27 Vdc` | `MQ00519-c-EN`, printed p. 499 / PDF p. 1 |
| Maximum absorption | `125 mA` | `MQ00519-c-EN`, printed p. 499 / PDF p. 1 |
| Operating temperature | `5..35 °C` | `MQ00519-c-EN`, printed p. 499 / PDF p. 1 |
| Ethernet | RJ45, `10/100 Mbit/s` | `MQ00519-c-EN`, printed p. 499 / PDF p. 1 |
| USB | configuration and firmware update | `MQ00519-c-EN`, printed p. 499 / PDF p. 1 |
| RS232 | present | `MQ00519-c-EN`, printed p. 499 / PDF p. 1 |
| SCS | Connectors labelled `SCS AV` and `SCS AI`; publisher legends describe video-door-entry/automation and burglar-alarm connections | `MQ00519-c-EN`, printed p. 499 / PDF p. 1 |
| Configuration | MyHOME Suite product programming | Vendor documentation + catalogue |

The catalogue independently associates both firmware definitions with Ethernet and USB connection modalities.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1455` | Canonical catalogue |
| Item model / `modobj` | `51` | Canonical catalogue / retained definition |
| Main system | Integration functions (`id_system = 26`) | Canonical catalogue / retained definition |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `51` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Burglar alarm | private riser | Canonical item/bus relationship |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |

These are software applicability associations, not an inventory of physical ports or proof of every functional service.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `6` | `1` | `0` | `37` | `2` | Not catalogue default | Official |
| `101` | `2` | `0` | `1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

### Parameter and package associations

| Firmware | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- |
| `6` | BTicino (catalogue key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `6` | BTicino (catalogue key `1`) | `0` | SVM | `1455_1.0_BT\xml\SVM\svm.xml` |
| `6` | BTicino (catalogue key `1`) | `0` | Extra | `1455_1.0_BT\xml\Extra\extra.xml` |
| `6` | BTicino (catalogue key `1`) | `0` | Director | `1455_1.0_BT\xml\DIRECTOR\director.xml` |
| `6` | BTicino (catalogue key `1`) | `0` | Protocol and other device parameters | `1455_1.0_BT\xml\Protocol\protocol.xml` |
| `6` | Legrand (catalogue key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `6` | Legrand (catalogue key `2`) | `0` | SVM | `1455_1.0_LG\xml\SVM\svm.xml` |
| `6` | Legrand (catalogue key `2`) | `0` | Extra | `1455_1.0_LG\xml\Extra\extra.xml` |
| `6` | Legrand (catalogue key `2`) | `0` | Director | `1455_1.0_LG\xml\DIRECTOR\director.xml` |
| `6` | Legrand (catalogue key `2`) | `0` | Protocol and other device parameters | `1455_1.0_LG\xml\Protocol\protocol.xml` |
| `6` | Unspecified brand (catalogue key `5`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `6` | Unspecified brand (catalogue key `5`) | `0` | SVM | `1455_1.0_LGG\xml\SVM\svm.xml` |
| `6` | Unspecified brand (catalogue key `5`) | `0` | Extra | `1455_1.0_LGG\xml\Extra\extra.xml` |
| `6` | Unspecified brand (catalogue key `5`) | `0` | Director | `1455_1.0_LGG\xml\DIRECTOR\director.xml` |
| `6` | Unspecified brand (catalogue key `5`) | `0` | Protocol and other device parameters | `1455_1.0_LGG\xml\Protocol\protocol.xml` |
| `101` | Legrand (catalogue key `2`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `101` | BTicino (catalogue key `1`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `101` | BTicino (catalogue key `1`) | `0` | SVM | `1455_2.0_BT\xml\SVM\svm.xml` |
| `101` | BTicino (catalogue key `1`) | `0` | Extra | `1455_2.0_BT\xml\Extra\extra.xml` |
| `101` | BTicino (catalogue key `1`) | `0` | Director | `1455_2.0_BT\xml\DIRECTOR\director.xml` |
| `101` | BTicino (catalogue key `1`) | `0` | Protocol and other device parameters | `1455_2.0_BT\xml\Protocol\protocol.xml` |
| `101` | Legrand (catalogue key `2`) | `0` | SVM | `1455_2.0_LG\xml\SVM\svm.xml` |
| `101` | Legrand (catalogue key `2`) | `0` | Extra | `1455_2.0_LG\xml\Extra\extra.xml` |
| `101` | Legrand (catalogue key `2`) | `0` | Director | `1455_2.0_LG\xml\DIRECTOR\director.xml` |
| `101` | Legrand (catalogue key `2`) | `0` | Protocol and other device parameters | `1455_2.0_LG\xml\Protocol\protocol.xml` |
| `101` | Unspecified brand (catalogue key `5`) | `0` | SDC | `xml\SDC\sdc.xml` |
| `101` | Unspecified brand (catalogue key `5`) | `0` | SVM | `1455_2.0_LGG\xml\SVM\svm.xml` |
| `101` | Unspecified brand (catalogue key `5`) | `0` | Extra | `1455_2.0_LGG\xml\Extra\extra.xml` |
| `101` | Unspecified brand (catalogue key `5`) | `0` | Director | `1455_2.0_LGG\xml\DIRECTOR\director.xml` |
| `101` | Unspecified brand (catalogue key `5`) | `0` | Protocol and other device parameters | `1455_2.0_LGG\xml\Protocol\protocol.xml` |

All 30 `AS_FIRMWARE_PARAMETERS` associations are shown. Brand keys here are database keys, not diagnostic `BRAND` numbers. The referenced XML payloads are not present in the retained catalogue extraction and have not been inspected; no field or behavior is inferred from their path names.

No `AS_FW_PACKAGE` association is stored for these firmware definitions. This is a catalogue coverage statement, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `6` | `1` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed/designated metadata | `629` | `512` | `435` |
| `6` | `2` | `150` Gateway Open SCS | Fixed/designated metadata | `627` | `150` | `433` |
| `101` | `1` | `216` Enhanced Web Server Audio/Video 2 Wires (F454) | Fixed/designated metadata | `630` | `512` | `436` |
| `101` | `2` | `150` Gateway Open SCS | Fixed/designated metadata | `628` | `150` | `434` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

This two-Module catalogue model is separate from the gateway's network interfaces and from ordinary addressed actuator Modules.

## Configuration modes

| Firmware | Mode | Catalogue mode | Applicability |
| --- | --- | --- | --- |
| `6` | Product Programming | `3` | Canonical catalogue association; not proof of installed state |
| `101` | Product Programming | `3` | Canonical catalogue association; not proof of installed state |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `101` | Ethernet | Canonical connection association |
| `101` | USB | Canonical connection association |
| `6` | Ethernet | Canonical connection association |
| `6` | USB | Canonical connection association |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `6` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `6` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway; Boolean flag for Gateway device |
| `6` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `6` | `VCD_PORT` | `#####` = Video port | `10000` | Video port; VIdeo port |
| `6` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `6` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `6` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `6` | `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `6` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity; Public Dynamic IP |
| `6` | `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos; Voice Box Vds |
| `101` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `101` | `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway; Boolean flag for Gateway device |
| `101` | `FW_VER` | `######` = Firmware version | `2.0.0` | Firmware version |
| `101` | `VCD_PORT` | `#####` = Video port | `10000` | Video port; VIdeo port |
| `101` | `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `101` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `101` | `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity; Local Dynamic IP |
| `101` | `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `101` | `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | Not specified in source | Public IP dynamicity; Public Dynamic IP |
| `101` | `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos; Voice Box Vds |

### Configuration-template version irregularity

`FW_VER` defaults (`3.0.0` for firmware `6`, `2.0.0` for firmware `101`) differ from their enclosing capability versions (`1.0.37`, `2.0.1`). They remain template data, not firmware applicability or observed installed versions. The source leaves firmware `101`'s `CONNECTION_METHOD` default unspecified; the earlier repeated overview obscured that absence.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `150` - Gateway Open SCS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Object `216` - Enhanced Web Server Audio/Video 2 Wires (F454)

Catalogue Object key `512` maps to external Object `216`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `LAN_IP_ADDR_TYPE` | `0` = Static IP; `1` = Dynamic IP (DHCP) | `0` | Local IP dynamicity |
| `IP_ADDRESS` | `###.###.###.###` = Public IP address | `192.168.1.35` (publisher catalogue documentation default) | Public IP address |
| `CONNECTION_METHOD` | `0` = Dynamic IP (DHCP); `1` = Static IP; `2` = Web active connections | `0` | Public IP dynamicity |
| `CMD_PORT` | `#####` = Commands port | `20000` | Commands port |
| `VCD_PORT` | `#####` = Video port | `10000` | Video port |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `S_VCT` | `0` = Disable; `1` = Enable | `0` | Voice box videos |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Applicability interpretation

The reusable Object fields describe configuration templates. Network addresses, credentials and installation identifiers remain private installation state. Catalogue Object key `512` is external Object `216`.

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
| `DIMENSION 1` | corroborate technical identity for catalogue item `1455` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`150`, `216`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes

| Surface | F454-specific knowledge | Canonical reference |
| --- | --- | --- |
| `WHO 13 DIMENSION 15` | observed `MODEL = 200`; not unique | [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md#dimension-15---device-type) |
| `WHO 13 DIMENSION 16` | gateway firmware reporting | [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md#dimension-16---firmware-version) |
| `WHO 13 DIMENSION 23` | kernel version reporting | [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md) |
| `WHO 13 DIMENSION 24` | distribution version reporting | [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md) |
| `WHO 13 DIMENSION 40` | observed response `4*0`; semantics unresolved | [Observed Extension](../../functional/who-13-integration-gateway/dimensions.md#observed-implementation-extension-dimension-40) |
| diagnostic `WHO 1013 DIMENSION 1` | observed tuple `51*15*5*0` | [Gateway Identification](../../guides/identify-openwebnet-gateway.md) |

Generic gateway frame grammar stays in the linked references. The sanitized F454 exchange is retained in the linked gateway-identification worked case; no raw exchange is reproduced on this page.
## Functional applicability

The archived English user and software manuals establish the product-level application surface that sits above the two catalogue Modules.

| Documented application / configuration | Evidence |
| --- | --- |
| The web interface exposes Lighting, Automation, Temperature control, Video door entry, Burglar alarm, Energy Management and Scenarios, plus rooms/favourites and user settings. | `O1755H_S_EN`, pp. 4–24, 30–54; `O1755J_U_EN`, pp. 29–79, source-specific dependencies below |
| Video-door-entry support includes camera/video functions and the associated answering-machine workflow where configured. | `O1755H_S_EN`, pp. 4–24, 30–54; `O1755J_U_EN`, pp. 29–79, source-specific dependencies below |
| The web server supports both local and remote connection modes. MyHOME_Web configuration distinguishes fixed IP, dynamic IP and active Web Server connection (`WAC`) modes. | `O1755H_S_EN`, pp. 4–24, 30–54; `O1755J_U_EN`, pp. 29–79, source-specific dependencies below |
| Administrative functions include user/profile management, e-mail/notification settings, IP-range controls, video-streaming settings and Device diagnostics. | `O1755H_S_EN`, pp. 4–24, 30–54; `O1755J_U_EN`, pp. 29–79, source-specific dependencies below |
| OPEN authentication can use the numeric OPEN password or HMAC authentication. The manuals explicitly warn that some older clients may not support HMAC, and dynamic-IP MyHOME_Web operation uses OPEN-password authentication. | `O1755H_S_EN`, pp. 4–24, 30–54; `O1755J_U_EN`, pp. 29–79, source-specific dependencies below |
| Product programming can send/receive the project, update Firmware and request Device information over mini-USB or Ethernet while the F454 is powered from the SCS bus. | `O1755H_S_EN`, pp. 4–24, 30–54; `O1755J_U_EN`, pp. 29–79, source-specific dependencies below |
| LAN configuration includes static/DHCP addressing, router and DNS settings needed by outgoing services such as e-mail. | `O1755H_S_EN`, pp. 4–24, 30–54; `O1755J_U_EN`, pp. 29–79, source-specific dependencies below |
| Remote access can itself be enabled/disabled through a configured `AUX` channel, optionally with an Automation actuator used as a status indication. | `O1755H_S_EN`, pp. 4–24, 30–54; `O1755J_U_EN`, pp. 29–79, source-specific dependencies below |

These are F454 application/configuration capabilities, not extra OpenWebNet Modules. The two catalogue Objects remain the implementation projection used by MyHOME Suite.

The later software manual `O1755H_S_EN`, pp. 17–20, documents a maximum of 20 blocked OPEN commands and excludes some pre-2012 entrance panels, MINISFERA and LINEA 2000 from the answering-machine function. These dependencies qualify the application list; the list does not establish support for every attached product.

## Observed behavior and corroboration

The observed F454 identity tuple independently corroborates the database mapping `modobj = 51`, `BRAND = 5`, `LINE = 0`.

A first-hand F454 gateway-information capture also establishes readable `WHO 13 DIMENSION 40 = 4*0`. Its two returned values remain semantically unknown.

F454 has additionally been part of controlled F418U2 tests in which gateway-dependent handling of functional dimmer dimensions was observed. Those results belong primarily to the F418U2 / gateway-path evidence and are linked from [`WHO 1` Dimensions](../../functional/who-1-lighting/dimensions.md).

## Programming

F454 uses Product Programming rather than ordinary physical/virtual Object programming. Generic programming-session mechanics belong in [Programming](../../programming/). Device-specific fields and their catalogue domains are preserved above.

A future OWN Device Library representation should keep network configuration fields but must never populate them with installation-specific values from research captures.

## Source reconciliation

The known F454 vendor material and first-hand gateway captures add Device-specific behavior beyond the catalogue fields:

- the physical interface includes RESET and front status indicators for speed/link/system state; those indicators describe the gateway appliance and are not additional OpenWebNet Objects;
- firmware release history is a product release history and must remain separate from the two MyHOME Suite capability records;
- gateway identity `N_CONF = 15` remains an observed out-of-range gateway value with unresolved semantics;
- `WHO 13 DIMENSION 40` is first-hand observed on F454 as `4*0`, with semantics still unresolved;
- prior research also encountered a possible `WHO 13 DIMENSION 20` property, but the preserved F454/MH202 captures and canonical registries currently examined do not establish it. It remains a research question and must not be represented as an F454 capability;
- F454-dependent F418U2 behavior, including the observed `OFF`-state `DIMENSION 1` request returning a `DIMENSION 4` frame and one non-effective positive `DIMENSION 4` write, is gateway-path evidence rather than a generic dimmer rule.

All eight identified English PDF revisions are accounted for. Earlier G user/software manuals describe the older page-oriented interface and user/administrator logins; H/J describe profiles, rooms/favourites and HMAC. The manufacturer history places new web pages, profile management and optional HMAC at release `2.0.46` (28 October 2015), and the thermoregulation-probe web-status fix at `2.0.51` (8 May 2017). These release features must not be attributed unconditionally to the catalogue's `1.0.37` record. The history prints `1.0.45` as 12 February 2013 and `1.0.37` as 17 June 2013; that version/date ordering is preserved as a source irregularity.

G software p. 10 offers DHCP but also says a static address is needed for correct operation. H software p. 11 offers both without that extra sentence; no universal static-IP requirement is inferred. J user pp. 19/69 specifically limits dynamic-IP MyHOME_Web operation to OPEN-password authentication. Product manuals describe historical services; their continued availability is not established here.

The `F454_020051.fwz` package was already registered with SHA-256 `15f80bc673e53fa105a68725b5a6d3ccf06767d1bae0e6139803de34e485f0f3`; see the manifest for its authoritative full fingerprint and private-archive-only status. The package payload has not been inspected and no claim is derived from it. The catalogue's parameter XML associations are now fully listed, with their unexamined payloads explicitly bounded.

The technical and instruction-sheet connector legends are retained literally. A bus label or catalogue association is not proof of an interchangeable wiring topology.

## Evidence limits and open work

- Referenced catalogue parameter XML payloads are not retained in this extraction; their inner schemas, defaults and programming semantics remain unexamined.
- The registered `2.0.51` firmware original is private-archive-only and its contents were not inspected. No public redistribution or payload-level equivalence is asserted.
- Non-English manual variants have not been incorporated; no claim is made that the English revision set exhausts regional material.
- Gateway `N_CONF=15` and `WHO 13 DIMENSION 40=4*0` remain observed values with unresolved semantics.
- Selection of catalogue capability records for installed firmware outside `1.0.37` / `2.0.1` remains unestablished. Historical portal/e-mail services are not certified currently available.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md)
- [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md)
- [`DIMENSION 1` Device Identity](../../diagnostics/dim1-device-identity.md)

- [Semantic review record, 5 October 2026](../../project/review/device-reviews-0001-0010-2026-10-05.md#own-dev-0002)
