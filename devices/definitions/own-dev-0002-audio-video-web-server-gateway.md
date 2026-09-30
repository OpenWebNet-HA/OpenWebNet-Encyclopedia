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
| Catalogue firmware definitions | `1.0.37`, `2.0.1` | Implementation evidence |
| Declared Modules | 2 | Implementation evidence |
| Categories | Gateway, Interface, Audio / Video | Catalogue + vendor documentation |

The F454 is a MyHOME audio/video Web Server and integration gateway. BTicino's firmware-history document explicitly identifies the product as “F454 - 003598”, so those commercial references belong to the same technical Device definition.

## Commercial identities

| Brand / range | SKU / reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F454` | Established commercial identity | Catalogue + vendor documentation + observed gateway identity |
| Legrand | `0 035 98` / `003598` | Equivalent commercial reference | Vendor firmware history + same catalogue item |

F453 and F453AV are predecessor products named by vendor documentation. They are not synonyms and remain separate technical Devices.

## Documentation and firmware archive

The historical vendor archive currently exposes a useful set of original F454 material:

| Document / artifact | Type | Status | Source |
| --- | --- | --- | --- |
| `MQ00519-c-EN` | Technical sheet | Official source identified, archival copy pending | [Vendor archive](https://www.homesystems-legrandgroup.com/home/-/productsheets/2463476) |
| `O1755J_U_EN` | User manual | Official source identified, archival copy pending | [Vendor archive](https://www.homesystems-legrandgroup.com/home/-/productsheets/2463476) |
| `O1755H_S_EN` | Software manual | Official source identified, archival copy pending | [Vendor archive](https://www.homesystems-legrandgroup.com/home/-/productsheets/2463476) |
| `O1754E` | Instruction sheet | Official source identified, archival copy pending | [Vendor archive](https://www.homesystems-legrandgroup.com/home/-/productsheets/2463476) |
| `Version_History_F454_20170508` | Firmware version history | Official source identified, archival copy pending | [PDF](https://www.homesystems-legrandgroup.com/documents/2416083/2422856/Version_History_F454_20170508.pdf/1f3644de-73a3-5332-3ff3-b12596cc53df?t=1595605650159) |
| `F454_020051.fwz` | Firmware package | Official source identified, archival copy pending | [Vendor archive](https://www.homesystems-legrandgroup.com/home/-/productsheets/2463476) |

Language variants should be retained separately when their bytes or content differ.

## Physical and connection characteristics

Vendor technical documentation establishes:

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

The catalogue independently associates both firmware definitions with Ethernet and USB connection modalities.

## Identity

### Catalogue identity

| Field | Value | Evidence state |
| --- | --- | --- |
| `EN_DEVICE.code` | `F454` / sibling `003598` | Implementation evidence |
| `EN_ITEM.id_item` | `1455` | Implementation evidence |
| `EN_ITEM.descr` | “Web Server A/V Bus” | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `51` | Implementation evidence |
| `EN_BRAND.brand_modobj` | `5` | Implementation evidence |
| `EN_LINE.line_modobj` | `0` | Implementation evidence |
| `is_gateway` | `1` | Implementation evidence |

### Observed gateway identity

A first-hand F454 capture establishes the gateway-specific identity path:

```text
Client -> Gateway: *#13**15##
Gateway -> Client: *#13**15*200##

Client -> Gateway: *#1013**1##
Gateway -> Client: *#1013**1*51*15*5*0##
```

The observed diagnostic tuple is:

| Field | Value | Status |
| --- | ---: | --- |
| `OBJECT_MODEL` | `51` | observed and catalogue-correlated |
| gateway `N_CONF` | `15` | observed; exact semantics unresolved |
| `BRAND` | `5` | observed and catalogue-correlated |
| `LINE` | `0` | observed and catalogue-correlated |
| functional `WHO 13 DIMENSION 15.MODEL` | `200` | observed; not unique to F454 |

The `51*15*5*0` tuple corroborates the catalogue identity. The same functional model code `200` has also been observed on MH202, so it must not be used as a unique product discriminator.

See [Identify an OpenWebNet Gateway](../../guides/identify-openwebnet-gateway.md) and [`DIMENSION 1` Device Identity](../../diagnostics/dim1-device-identity.md) for the generic identification procedure.

## Firmware

### Catalogue firmware definitions

| Catalogue firmware | Version | Build | Slots | Default | Evidence |
| --- | --- | --- | ---: | ---: | --- |
| `6` | `1.0` | `37` | 2 | 0 | `MHCatalogue.db` |
| `101` | `2.0` | `1` | 2 | 1 | `MHCatalogue.db` |

These are MyHOME Suite capability-selection definitions, not an exhaustive firmware release history.

### Vendor firmware history

The official F454 history currently preserved by the vendor lists:

| Firmware | Printed date | Vendor note summary |
| --- | --- | --- |
| `1.0.26` | 29 February 2012 | first release |
| `1.0.32` | 30 July 2012 | security improvement and burglar-alarm fixes |
| `1.0.45` | 12 February 2013 | translations, video streaming, minor fixes |
| `1.0.37` | 17 June 2013 | virtual-configuration performance and optimizations |
| `1.0.51` | 18 November 2014 | MyHome portal improvements |
| `2.0.46` | 28 October 2015 | new web/profile UI, MyHome_Web App, burglar-alarm control, HMAC option and other improvements |
| `2.0.48` | 26 January 2016 | optimization and minor fixes |
| `2.0.50` | 16 May 2016 | real-time image fix and optimizations |
| `2.0.51` | 8 May 2017 | thermoregulation probe web-page fix |

The vendor document prints `1.0.45` with a February 2013 date and `1.0.37` with a June 2013 date. Preserve that source ordering/data as published rather than silently “fixing” it.

The archive also exposes firmware package `2.0.51`.

## Module and Object model

Both catalogue firmware definitions expose the same two fixed Modules:

| Slot | Object | Description | Evidence |
| ---: | ---: | --- | --- |
| `1` | `216` | Enhanced Web Server Audio/Video 2 Wires (F454) | Implementation evidence |
| `2` | `150` | Gateway Open SCS | Implementation evidence |

This two-Module catalogue model is separate from the gateway's network interfaces and from ordinary addressed actuator Modules.

## Configuration mode and connection modalities

Both firmware definitions declare:

- **Product Programming** configuration mode;
- **Ethernet** connection;
- **USB** connection.

## Firmware-scoped configuration

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

## Object configuration surface

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

## Functional and diagnostic applicability

| Surface | F454-specific knowledge | Canonical reference |
| --- | --- | --- |
| `WHO 13 DIMENSION 15` | observed `MODEL = 200`; not unique | [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md#dimension-15---device-type) |
| `WHO 13 DIMENSION 16` | gateway firmware reporting | [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md#dimension-16---firmware-version) |
| `WHO 13 DIMENSION 23` | kernel version reporting | [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md) |
| `WHO 13 DIMENSION 24` | distribution version reporting | [Gateway Dimensions](../../functional/who-13-integration-gateway/dimensions.md) |
| `WHO 13 DIMENSION 40` | observed response `4*0`; semantics unresolved | [Observed Extension](../../functional/who-13-integration-gateway/dimensions.md#observed-implementation-extension-dimension-40) |
| diagnostic `WHO 1013 DIMENSION 1` | observed tuple `51*15*5*0` | [Gateway Identification](../../guides/identify-openwebnet-gateway.md) |

Generic gateway frame grammar stays in the linked references. The raw identity exchange is retained above because it is direct evidence for this product.

## Observed behavior and corroboration

The observed F454 identity tuple independently corroborates the database mapping `modobj = 51`, `BRAND = 5`, `LINE = 0`.

A first-hand F454 gateway-information capture also establishes readable `WHO 13 DIMENSION 40 = 4*0`. Its two returned values remain semantically unknown.

F454 has additionally been part of controlled F418U2 tests in which gateway-dependent handling of functional dimmer dimensions was observed. Those results belong primarily to the F418U2 / gateway-path evidence and are linked from [`WHO 1` Dimensions](../../functional/who-1-lighting/dimensions.md).

## Programming

F454 uses Product Programming rather than ordinary physical/virtual Object programming. Generic programming-session mechanics belong in [Programming](../../programming/). Device-specific fields and their catalogue domains are preserved above.

A future OWN Device Library representation should keep network configuration fields but must never populate them with installation-specific values from research captures.

## Evidence limits and open work

- Archive all known F454 manuals, technical sheets, instruction sheets, language variants, firmware packages, and version-history revisions.
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
