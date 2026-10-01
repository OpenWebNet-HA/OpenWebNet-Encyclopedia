# Audio/video web server and OpenWebNet gateway

## Summary


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

The F454 is a MyHOME audio/video Web Server and integration gateway. BTicino's firmware-history document explicitly identifies the product as “F454 - 003598”, so those commercial references belong to the same technical Device definition.

## Commercial identities


| Brand / range | SKU / reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F454` | Established commercial identity | Catalogue + vendor documentation + observed gateway identity |
| Legrand | `0 035 98` / `003598` | Equivalent commercial reference | Vendor firmware history + same catalogue item |

F453 and F453AV are predecessor products named by vendor documentation. They are not synonyms and remain separate technical Devices.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00519-c-EN` | Technical sheet | not stated in retained row | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/5f/36/5f36d8d5985f516f393c19ed4fbacdf2c40ca40c08cf023d08fd45baf36fe8f6.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00519-c-EN.pdf) |
| `O1755J_U_EN` | User manual | not stated in retained row | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/34/17/3417dbd9acbff4c2feb329a722e8e24cc2c313ad3af85e1ea30b8ff44343cd08.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1755J_U_EN.pdf) |
| `O1755H_S_EN` | Software manual | not stated in retained row | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/41/8c/418cd9a3e38720b4c5660e07a8f24970253ace23a4a825d597c4489b6c8282f5.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1755H_S_EN.pdf) |
| `O1754E` | Instruction sheet | not stated in retained row | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/d4/7f/d47faf013abb6f55e08f149365f3b98d86240b34b30f24c9eeea1de1505e3ff6.pdf) | [Official source](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileName=O1754E.pdf&fileId=58107.23188.62294.22284) |
| `Version_History_F454_20170508` | Firmware version history | not stated in retained row | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/c9/60/c960937a4d19e52342c1af618782e715e75e1e181a7804d012096afec99834a3.pdf) | [Official source](https://www.homesystems-legrandgroup.com/documents/2416083/2422856/Version_History_F454_20170508.pdf/1f3644de-73a3-5332-3ff3-b12596cc53df?t=1595605650159) |
| `O1755G_U_EN` | Earlier English user manual revision | not stated in retained row | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/f1/d4/f1d437d369f5a217c4094128c8841f3d2171381ba0f321f0dfa52e30177e2460.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1755G_U_EN.pdf) |
| `O1755G_S_EN` | Earlier English software manual revision | not stated in retained row | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/bc/d6/bcd66d983153fc8911022f52c6dd78605fb9533846e5bca05b46c4ac118a8bea.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1755G_S_EN.pdf) |
| `O1754C` | Additional instruction-sheet revision | not stated in retained row | Device/family coverage described by retained source | [Archived original](https://archive.openwebnet-ha.org/sha256/8b/e3/8be3d653dbd0cf01cb4ac1de7976100c355719a5851cc6e0ed03c07d4a6856ff.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/O1754C.pdf) |
| `F454_020051.fwz` | Firmware package | not stated in retained row | Device/family coverage described by retained source | - | [Vendor archive](https://www.homesystems-legrandgroup.com/home/-/productsheets/2463476) |

The historical vendor archive currently exposes a useful set of original F454 material:


Language variants should be retained separately when their bytes or content differ.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Width | 6 DIN modules | Vendor technical sheet |
| Supply | `18..27 Vdc` | Vendor technical sheet |
| Maximum absorption | `125 mA` | Vendor technical sheet |
| Operating temperature | `5..35 °C` | Vendor technical sheet |
| Ethernet | RJ45, `10/100 Mbit/s` | Vendor technical sheet |
| USB | configuration and firmware update | Vendor technical sheet |
| RS232 | present | Vendor technical sheet |
| SCS | Audio/Video and Automation/Integration bus connections documented | Vendor technical sheet |
| Configuration | MyHOME Suite product programming | Vendor documentation + catalogue |

Vendor technical documentation establishes:


The catalogue independently associates both firmware definitions with Ethernet and USB connection modalities.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1455` | Canonical catalogue |
| Item model / `modobj` | `51` | Canonical catalogue / retained definition |
| Main system | Integration functions (`id_system = 26`) | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `6` | `1` | `0` | `37` | `2` | non-default | catalogue applicability |
| `101` | `2` | `0` | `1` | `2` | catalogue default | catalogue applicability |

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Object | Description | Relationship |
| --- | --- | --- | --- |
| `6` | `150` | Gateway Open SCS | catalogue firmware/Object relation |
| `6` | `512` | Enhanced Web Server Audio/Video 2 Wires (F454) | catalogue firmware/Object relation |
| `101` | `150` | Gateway Open SCS | catalogue firmware/Object relation |
| `101` | `512` | Enhanced Web Server Audio/Video 2 Wires (F454) | catalogue firmware/Object relation |

### Virgin Objects

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

### Reconciled topology notes


Both catalogue firmware definitions expose the same two fixed Modules:

| Slot | Object | Description | Evidence |
| ---: | ---: | --- | --- |
| `1` | `216` | Enhanced Web Server Audio/Video 2 Wires (F454) | Implementation evidence |
| `2` | `150` | Gateway Open SCS | Implementation evidence |

This two-Module catalogue model is separate from the gateway's network interfaces and from ordinary addressed actuator Modules.

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `6` | Product Programming | retained Device-specific configuration modality |
| `101` | Product Programming | retained Device-specific configuration modality |


Both firmware definitions declare:

- **Product Programming** configuration mode;
- **Ethernet** connection;
- **USB** connection.

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `6` | `AID` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `6` | `IS_GATEWAY` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `6` | `FW_VER` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `6` | `VCD_PORT` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `6` | `CMD_PORT` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `6` | `LAN_IP_ADDRESS` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `6` | `LAN_IP_ADDR_TYPE` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `6` | `IP_ADDRESS` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `6` | `CONNECTION_METHOD` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `6` | `S_VCT` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `AID` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `IS_GATEWAY` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `FW_VER` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `VCD_PORT` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `CMD_PORT` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `LAN_IP_ADDRESS` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `LAN_IP_ADDR_TYPE` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `IP_ADDRESS` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `CONNECTION_METHOD` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `101` | `S_VCT` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |

### Published and reconciled details


The two catalogue firmware definitions expose the same field names and domains. Defaults that differ between records are preserved rather than normalized.

| Field | Domain / template | Firmware `1.0.37` default | Firmware `2.0.1` default | Evidence |
| --- | --- | --- | --- | --- |
| `AID` | Device ID user value | - | - | Implementation evidence |
| `IS_GATEWAY` | `0=Disable`, `1=Enable` | `0` | `0` | Implementation evidence |
| `FW_VER` | firmware-version user value | `3.0.0` | `2.0.0` | Implementation evidence |
| `VCD_PORT` | 5-digit user value | `10000` | `10000` | Implementation evidence |
| `CMD_PORT` | 5-digit user value | `20000` | `20000` | Implementation evidence |
| `LAN_IP_ADDRESS` | IPv4 template user value | `192.168.1.35` | `192.168.1.35` | Implementation evidence |
| `LAN_IP_ADDR_TYPE` | `0=Static IP`, `1=Dynamic IP (DHCP)` | `0` | `0` | Implementation evidence |
| `IP_ADDRESS` | IPv4 template user value | `192.168.1.35` | `192.168.1.35` | Implementation evidence |
| `CONNECTION_METHOD` | `0=Dynamic IP (DHCP)`, `1=Static IP`, `2=Web active connections` | stored enum | stored enum | Implementation evidence |
| `S_VCT` | `0=Disable`, `1=Enable` | `0` | `0` | Implementation evidence |

The `FW_VER` defaults are configuration-template data and do not correspond cleanly to the enclosing catalogue firmware definitions. In particular, the `1.0.37` capability record contains a `FW_VER` default of `3.0.0`. Preserve this implementation irregularity and do not reinterpret it as a literal firmware applicability statement.

## Object configuration surfaces

### Object `150` - Gateway Open SCS

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LAN_IP_ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IS_GATEWAY` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SYSADDRESS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `512` - Enhanced Web Server Audio/Video 2 Wires (F454)

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `IS_GATEWAY` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LAN_IP_ADDRESS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LAN_IP_ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IP_ADDRESS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `CONNECTION_METHOD` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `CMD_PORT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `VCD_PORT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `FW_VER` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `S_VCT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SYSADDRESS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Reconciled Object notes


### Object `150` - Gateway Open SCS

| Parameter | Domain / default | Evidence |
| --- | --- | --- |
| `LAN_IP_ADDRESS` | IPv4 template, default `192.168.1.35` | Implementation evidence |
| `LAN_IP_ADDR_TYPE` | Static / DHCP, default Static | Implementation evidence |
| `IS_GATEWAY` | Disable / Enable, default Disable | Implementation evidence |
| `SYSADDRESS` | six-digit “Univocal code”, default `1` | Implementation evidence |

### Object `216` - Enhanced Web Server Audio/Video 2 Wires

| Parameter | Domain / default | Evidence |
| --- | --- | --- |
| `IS_GATEWAY` | Disable / Enable | Implementation evidence |
| `LAN_IP_ADDRESS` | IPv4 template, default `192.168.1.35` | Implementation evidence |
| `LAN_IP_ADDR_TYPE` | Static / DHCP | Implementation evidence |
| `IP_ADDRESS` | IPv4 template, default `192.168.1.35` | Implementation evidence |
| `CONNECTION_METHOD` | Dynamic IP / Static IP / Web active connections | Implementation evidence |
| `CMD_PORT` | default `20000` | Implementation evidence |
| `VCD_PORT` | default `10000` | Implementation evidence |
| `FW_VER` | user value; Object definition default `3.0.0` | Implementation evidence |
| `S_VCT` | Disable / Enable | Implementation evidence |
| `SYSADDRESS` | six-digit “Univocal code”, default `1` | Implementation evidence |

These are catalogue configuration fields. Actual IP addresses, ports, credentials, and installation identifiers belong to private installation state, not to the public Device definition.

## Conditions, filters, and conversions

### Relation filters

| Scope | Filter IDs | Interpretation |
| --- | --- | --- |
| Device/Object relations | none | apply before exposing reusable Object values |

### Slot conditions and conversions

| Scope | Condition IDs | Conversion treatment |
| --- | --- | --- |
| Device slots | none | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1455` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`150`, `512`) | [Modules](../../diagnostics/dim30-modules.md) |
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

Generic gateway frame grammar stays in the linked references. The raw identity exchange is retained above because it is direct evidence for this product.

## Functional applicability


The archived English user and software manuals establish the product-level application surface that sits above the two catalogue Modules.

- The web interface exposes Lighting, Automation, Temperature control, Video door entry, Burglar alarm, Energy Management and Scenarios, plus rooms/favourites and user settings.
- Video-door-entry support includes camera/video functions and the associated answering-machine workflow where configured.
- The web server supports both local and remote connection modes. MyHOME_Web configuration distinguishes fixed IP, dynamic IP and active Web Server connection (`WAC`) modes.
- Administrative functions include user/profile management, e-mail/notification settings, IP-range controls, video-streaming settings and Device diagnostics.
- OPEN authentication can use the numeric OPEN password or HMAC authentication. The manuals explicitly warn that some older clients may not support HMAC, and dynamic-IP MyHOME_Web operation uses OPEN-password authentication.
- Product programming can send/receive the project, update Firmware and request Device information over mini-USB or Ethernet while the F454 is powered from the SCS bus.
- LAN configuration includes static/DHCP addressing, router and DNS settings needed by outgoing services such as e-mail.
- Remote access can itself be enabled/disabled through a configured AUX channel, optionally with an Automation actuator used as a status indication.

These are F454 application/configuration capabilities, not extra OpenWebNet Modules. The two catalogue Objects remain the implementation projection used by MyHOME Suite.

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
- F454-dependent F418U2 behavior, including the observed OFF-state `DIMENSION 1` request returning a `DIMENSION 4` frame and one non-effective positive `DIMENSION 4` write, is gateway-path evidence rather than a generic dimmer rule.

The identified English F454 PDF set is now archived byte-for-byte and reconciled, including current/earlier user and software manuals, the technical sheet, two instruction-sheet revisions and the firmware history. The separate `F454_020051.fwz` firmware package remains a non-PDF archival task; it does not block reconciliation of the PDF documentation.

## Evidence limits and open work


- Archive the `2.0.51` firmware package and retain non-English manual variants separately when they provide content beyond translation of the reconciled English revisions.
- Add hashes and supersession relationships to the source manifest.
- Preserve observed firmware/hardware values from sanitized captures and associate them with the matching vendor release record where justified.
- Resolve the exact semantics of gateway `N_CONF = 15`.
- Resolve `WHO 13 DIMENSION 40`.
- Determine how MyHOME Suite chooses between the two catalogue capability records and firmware versions outside `1.0.37` / `2.0.1`.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md)
- [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md)
- [`DIMENSION 1` Device Identity](../../diagnostics/dim1-device-identity.md)
