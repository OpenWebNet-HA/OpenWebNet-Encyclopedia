# MyHOME_Screen 10 Capacitive

## Summary

MyHOME_Screen 10 Capacitive is a 10-inch wall touchscreen for configured MyHOME, video-door-entry and multimedia functions. Its capacitive interface includes room navigation and profile customization, bringing the installation's selected controls into a personalized screen layout.

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
| `RA00079AC_S_EN` | software manual | publisher copy | MyHOME_Screen10 and MyHOME_Screen10 C configuration, system functions and programming workflow | [Archived original](https://archive.openwebnet-ha.org/sha256/b9/ba/b9baa0fea2deb196253f415c47e6fd83f52d1a9728b5bfe99f69a20e0bc47340.pdf) | [Official source](https://dar.bticino.com/asset/Documents/RA00079AC_S_EN.pdf) |
| BTicino `MH4892C` catalogue page | product page | current catalogue | `MH4892C` product characteristics and capacitive-screen variant | Not applicable - web page | [Official product page](https://catalogue.bticino.com/product/smart-home-solutions/my-home---home-automation-system/integration-and-control/BTI-MH4892C-EN) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | `10 inch` 16:9 capacitive touchscreen | Current `MH4892C` catalogue |
| Supply | `27 Vdc` | Current BTicino catalogue |
| Dimensions | `315 x 200 x 24 mm` | Current BTicino catalogue |
| Mounting | Wall mounted with `506E` flush-mounted box | Current BTicino catalogue |
| Managed functions | MyHOME, video door entry and multimedia functions with room navigation and profile customization | Current catalogue / `RA00079AC_S_EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1898` | Canonical catalogue |
| Technical item | MyHOME_Screen 10 Capacitive | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `55` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `558` | `2` | `0` | `0` | `1` | Not catalogue default | Official |
| `697` | `2` | `1` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

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

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `558` | Product Programming | supported configuration route for this Device family |
| `697` | Product Programming | supported configuration route for this Device family |

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

Capacitive MyHOME touchscreen for integrated automation, video door entry and multimedia functions, programmed through MyHOME Suite/product programming.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The shared software manual intentionally covers both resistive and capacitive MyHOME_Screen10 families. The catalogue distinguishes this capacitive family as item 1898 with firmware 2.0.0 and 2.1.0.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
