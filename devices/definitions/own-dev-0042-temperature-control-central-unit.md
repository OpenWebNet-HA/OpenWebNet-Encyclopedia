# Temperature control central unit

## Summary

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
| Legrand Céliane | `067456` | established catalogue identity for item `291` | canonical commercial record |
| Legrand | `573918` | established catalogue identity for item `291` | canonical commercial record |
| Legrand | `573919` | established catalogue identity for item `291` | canonical commercial record |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BR-MyHOME-HPML0714 | product catalogue | 2014 | 573918 / 573919 temperature-control context: printed pp. 16, 24, 32 / PDF pp. 16, 24, 32 | [Archived original](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/BR%20MyHOME%20HPML0714.pdf) |
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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `3` | `0` | `0` | `1` | catalogue default | concrete catalogue applicability |
| `25` | `2` | `0` | `15` | `1` | non-default | concrete catalogue applicability |
| `26` | `1` | `1` | `6` | `1` | non-default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `24` | `912` | `35` Temperature control 99 zones control unit | fixed/designated |
| `25` | `913` | `35` Temperature control 99 zones control unit | fixed/designated |
| `26` | `914` | `35` Temperature control 99 zones control unit | fixed/designated |

| Virgin Object status | Value |
| --- | --- |
| Associations | none for selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `24` | Product Programming | supported route for this Device family |
| `25` | Product Programming | supported route for this Device family |
| `26` | Product Programming | supported route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `24` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `24` | `WARM` | catalogue-defined domain | catalogue-scoped | Winter mode |
| `24` | `COLD` | catalogue-defined domain | catalogue-scoped | Summer mode |
| `25` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `25` | `WARM` | catalogue-defined domain | catalogue-scoped | Winter mode |
| `25` | `COLD` | catalogue-defined domain | catalogue-scoped | Summer mode |
| `26` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `26` | `WARM` | catalogue-defined domain | catalogue-scoped | Winter mode |
| `26` | `COLD` | catalogue-defined domain | catalogue-scoped | Summer mode |

## Object configuration surfaces

### Object `35` - Temperature control 99 zones control unit

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `COLD` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Summer mode |
| `WARM` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Winter mode |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | none | relation-specific restrictions; do not widen reusable Object surfaces |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve applicable physical-to-advanced conversion through canonical resolver |

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
- [Archived original](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf)
