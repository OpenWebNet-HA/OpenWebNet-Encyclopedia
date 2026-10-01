# Shutter control bus

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0044` | Project identity |
| Technical description | Dedicated advanced shutter control with preset and reference-actuator support | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `H4660M2`, `LN4660M2`, `AM5860M2`, `067558` | Canonical commercial records |
| Catalogue item | `1579` | Implementation evidence |
| Main catalogue system | Automation | Implementation evidence |
| Item model / `modobj` | `46` | Implementation evidence |
| Firmware definition | `205 / -1.-1.-1` | Implementation evidence |
| Declared Modules | `1` | Firmware catalogue |
| Categories | Automation, Shutters, Control | Capability model |

Dedicated advanced shutter control with preset and reference-actuator support.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `H4660M2` | established catalogue identity for item `1579` | canonical commercial record |
| BTicino L/N/NT | `LN4660M2` | established catalogue identity for item `1579` | canonical commercial record |
| BTicino Matix | `AM5860M2` | established catalogue identity for item `1579` | canonical commercial record |
| Legrand Céliane | `067558` | established catalogue identity for item `1579` | canonical commercial record |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME | technical/system documentation | revision/date as printed | Advanced shutter control including H/LN4660M2 and AM5860M2 | [Archived original](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Physical configurator positions | A, PL, Ar, PLr, M, Pre | Published installation documentation / physical-device reconstruction |
| Actuator output | None - dedicated control Device | Catalogue Object model and publisher guide |
| Advanced behavior | Reference-actuator synchronization and preset-position control | Publisher guide |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1579` | Implementation evidence |
| Technical item description | Shutter control bus | Implementation evidence |
| Main system | Automation | Implementation evidence |
| Item model / `modobj` | `46` | Implementation evidence |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `205` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified components retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `205` | `663` | `529` Shutter control | fixed/designated |

| Virgin Object status | Value |
| --- | --- |
| Associations | none for selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `205` | Physical configuration | supported route for this Device family |
| `205` | Virtual Configuration | supported route for this Device family |
| `205` | Advanced Configuration | supported route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `205` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `205` | `A` | catalogue-defined domain | catalogue-scoped | Enviroment (0-9 GEN,GR,AMB) |
| `205` | `PL` | catalogue-defined domain | catalogue-scoped | Light Point |
| `205` | `M` | catalogue-defined domain | catalogue-scoped | Mode (SU_GIU, Su_GIU_M, 1,2) |
| `205` | `PRE` | catalogue-defined domain | catalogue-scoped | Shutter management preset number |
| `205` | `AR` | catalogue-defined domain | catalogue-scoped | Enviroment referent address |
| `205` | `PLR` | catalogue-defined domain | catalogue-scoped | Light Point referent address |

## Object configuration surfaces

### Object `529` - Shutter control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Mode (0,1,2,3) |
| `ADDR_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | See Automation System Addressing |
| `A` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | See Automation System Addressing |
| `PL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | See Automation System Addressing |
| `G1` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | See Automation System Addressing |
| `INST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | See Automation System Addressing |
| `DEST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | See Automation System Addressing |
| `A_R` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Area of reference actuator |
| `PL_R` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Light point of reference actuator |
| `PRIORITY` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Shutter management command priority |
| `PRE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Shutter management preset number |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `581` | relation-specific restrictions; do not widen reusable Object surfaces |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve applicable physical-to-advanced conversion through canonical resolver |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item `1579` / `modobj = 46` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `529` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Advanced shutter control with reference-actuator and preset support; no local motor output.

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
- [Archived original](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
