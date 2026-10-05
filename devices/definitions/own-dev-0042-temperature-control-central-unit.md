# Temperature control central unit

## Summary

This temperature-control central unit supervises and programmes a system of up to 99 zones. It provides central operating-mode control and zone management, bringing a larger heating and cooling installation under one control point.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0042` | Project identity |
| Technical description | Temperature-control central unit and supervisory programmer | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `3550`, `067456`, `573918`, `573919` | Canonical commercial records |
| Catalogue item | `291` | Implementation evidence |
| Main catalogue system | Temperature control | Implementation evidence |
| Item model / `modobj` | `2` | Implementation evidence |
| Firmware definition | `24 / 3.0.0`; `25 / 2.0.15`; `26 / 1.1.6` | Implementation evidence |
| Declared Modules | `1` | Firmware catalogue |
| Categories | Temperature control, HVAC, Central unit, Programming | Capability model |

Temperature-control central unit and supervisory programmer.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3550` | established catalogue identity for item `291` | canonical commercial record |
| Legrand - Céliane | `067456` | established catalogue identity for item `291` | canonical commercial record |
| Legrand | `573918` | established catalogue identity for item `291` | canonical commercial record |
| Legrand | `573919` | established catalogue identity for item `291` | canonical commercial record |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BR-MyHOME-HPML0714 | product catalogue | 2014 | 573918 / 573919 temperature-control context: printed pp. 16, 24, 32 / PDF pp. 16, 24, 32 | [Archived original](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/BR%20MyHOME%20HPML0714.pdf) |
| U0256E_U_EN | user manual | publisher revision not pinned | 3550 operation, diagnostics, local probe and programming | - | [Official source](https://dar.bticino.com/asset/Documents/U0256E_U_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| System capacity | Up to 99 temperature-control zones | 3550 publisher manual |
| Product role | Central supervision, operating-mode control and programming | 3550 publisher manual |
| Declared logical modules | 1 | Canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `291` | Implementation evidence |
| Technical item description | Temperature control central unit | Implementation evidence |
| Main system | Temperature control | Implementation evidence |
| Item model / `modobj` | `2` | Implementation evidence |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `3` | `0` | `0` | `1` | Catalogue default | Official |
| `25` | `2` | `0` | `15` | `1` | Not catalogue default | Official |
| `26` | `1` | `1` | `6` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `1` | `35` Temperature control 99 zones control unit | Fixed/designated metadata | `912` | `35` | `571` |
| `25` | `1` | `35` Temperature control 99 zones control unit | Fixed/designated metadata | `913` | `35` | `572` |
| `26` | `1` | `35` Temperature control 99 zones control unit | Fixed/designated metadata | `914` | `35` | `573` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `24` | Product Programming | supported route for this Device family |
| `25` | Product Programming | supported route for this Device family |
| `26` | Product Programming | supported route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `24` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `24` | `WARM` | `0` = Disable; `1` = Enable | `0` | WARM; Winter mode |
| `24` | `COLD` | `0` = Disable; `1` = Enable | `0` | COLD; Summer mode |
| `25` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `25` | `WARM` | `0` = Disable; `1` = Enable | `0` | WARM; Winter mode |
| `25` | `COLD` | `0` = Disable; `1` = Enable | `0` | COLD; Summer mode |
| `26` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `26` | `WARM` | `0` = Disable; `1` = Enable | `0` | WARM; Winter mode |
| `26` | `COLD` | `0` = Disable; `1` = Enable | `0` | COLD; Summer mode |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `35` - Temperature control 99 zones control unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `COLD` | `0` = Disable; `1` = Enable | `0` | Summer modality; Summer mode |
| `WARM` | `0` = Disable; `1` = Enable | `0` | Winter modality; Winter mode |

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
| `DIMENSION 1` | resolve item `291` / `modobj = 2` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `35` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Temperature-control central supervision, diagnostics, programming and zone management.

## Observed behavior and corroboration

No sanitized hardware fingerprint or Device-specific protocol capture is currently retained for this exact technical item.

## Programming

Programming must select installed firmware applicability, resolve slot/Object alternatives through catalogue conditions, apply relation filters, and preserve configuration-mode boundaries.

## Source reconciliation

The canonical catalogue establishes the commercial records, firmware applicability, topology, configuration fields, filters and conditions. Publisher sources above are used only for behaviors they directly document; missing dedicated sheets remain explicit gaps.

## Evidence limits and open work

- Recover any missing dedicated publisher sheets for the exact identities.
- Capture a sanitized hardware fingerprint covering identity, firmware, modules, addressing and configuration.
- Corroborate condition/filter behavior through MyHOME Suite and controlled configuration changes.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Archived original](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf)
