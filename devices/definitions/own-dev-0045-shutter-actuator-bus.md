# Shutter actuator bus

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0045` | Project identity |
| Technical description | Flush-mounted bus shutter actuator with position and preset management | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `H4661M2`, `LN4661M2`, `AM5861M2`, `067557` | Canonical commercial records |
| Catalogue item | `1586` | Implementation evidence |
| Main catalogue system | Automation | Implementation evidence |
| Item model / `modobj` | `48` | Implementation evidence |
| Firmware definition | `192 / -1.-1.-1` | Implementation evidence |
| Declared Modules | `1` | Firmware catalogue |
| Categories | Automation, Shutters, Actuator | Capability model |

Flush-mounted bus shutter actuator with position and preset management.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `H4661M2` | established catalogue identity for item `1586` | canonical commercial record |
| BTicino L/N/NT | `LN4661M2` | established catalogue identity for item `1586` | canonical commercial record |
| BTicino Matix | `AM5861M2` | established catalogue identity for item `1586` | canonical commercial record |
| Legrand Céliane | `067557` | established catalogue identity for item `1586` | canonical commercial record |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME | technical/system documentation | revision/date as printed | Advanced shutter actuator family and preset behavior | [Archived original](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| ST-00000900-EN | technical sheet | 2021-03-23 | H4661M2 / LN4661M2 / 067557 / AM5861M2; addressing, motor type, calibration and modes | - | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00000900-EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Controlled load | One shutter motor channel | ST-00000900-EN |
| Motor models | Standard motor with manual calibration or pulse operation | ST-00000900-EN |
| Position management | After endpoint acquisition, supports 100 positions and preset operation | ST-00000900-EN |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1586` | Implementation evidence |
| Technical item description | Shutter actuator bus | Implementation evidence |
| Main system | Automation | Implementation evidence |
| Item model / `modobj` | `48` | Implementation evidence |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `192` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified components retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `192` | `669` | `514` Shutter actuator | fixed/designated |

| Virgin Object status | Value |
| --- | --- |
| Associations | none for selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `192` | Physical configuration | supported route for this Device family |
| `192` | Virtual Configuration | supported route for this Device family |
| `192` | Advanced Configuration | supported route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `192` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `192` | `A` | catalogue-defined domain | catalogue-scoped | Enviroment |
| `192` | `PL` | catalogue-defined domain | catalogue-scoped | Light Point |
| `192` | `M` | catalogue-defined domain | catalogue-scoped | Mode (SU_GIU, Su_GIU_M, 1,2, PUL, SLA) |
| `192` | `TYPE` | catalogue-defined domain | catalogue-scoped | Shutter type
 Standard - Value : 1
 Pulse - Value : 2 |
| `192` | `PRE` | catalogue-defined domain | catalogue-scoped | Shutter management preset number |
| `192` | `G1` | catalogue-defined domain | catalogue-scoped | Group 1 |

## Object configuration surfaces

### Object `514` - Shutter actuator

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Area |
| `PL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Light point |
| `M` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Mode shutter actuator |
| `SHUTTER_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Shutter type |
| `STOP_PULSE_DURATION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Duration pulse of stop |
| `UP_OR_DOWN_PULSE_DURATION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Pulse duration of UP or Down |
| `TILTING` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for pulse mode. |
| `ROLLING` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for pulse mode. |
| `LOCAL_BUTTON` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Local button mode for Shutter managemant 4661M2 |
| `PRIORITY` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Shutter management command priority |
| `PRESET_NUMBER` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Shutter management preset number |
| `P1` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P1 |
| `P2` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P2 |
| `P3` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P3 |
| `P4` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P4 |
| `P5` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P5 |
| `P6` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P6 |
| `P7` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P7 |
| `P8` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P8 |
| `P9` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P9 |
| `P10` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Preset of position P10 |
| `UP_SHUTTER_TIME_MINUTES` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | UP shutter calbration time (m) |
| `UP_SHUTTER_TIME_SECONDS` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | UP shutter calbration time (s) |
| `DOWN_SHUTTER_TIME_MINUTES` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | DOWN shutter calbration time (m) |
| `DOWN_SHUTTER_TIME_SECONDS` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | DOWN shutter calbration time (s) |
| `SLATS_ROTATION_TIME_DOWN_H` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | SLATS ROTATION calibration time when shutter is all the way down - HIGH BYTE (ms) |
| `SLATS_ROTATION_TIME_DOWN_L` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | SLATS ROTATION calibration time when shutter is all the way down - LOW BYTE (ms) |
| `SLATS_ROTATION_TIME_MIDDLE_H` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If not intentionally modified, par 0x20 = par 30 |
| `SLATS_ROTATION_TIME_MIDDLE_L` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If not intentionally modified, par 0x21 = par 31 |
| `SLATS_ROTATION_STEP_NUMBER` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | SLATS ROTATION step number |
| `G1` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |
| `G2` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |
| `G3` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |
| `G4` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |
| `G5` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |
| `G6` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |
| `G7` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |
| `G8` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |
| `G9` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |
| `G10` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group = 0 means no group |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `597`, `598`, `599`, `600`, `601`, `602`, `4440`, `4453`, `4466`, `4479`, `4492`, `4505`, `4518`, `4531` | relation-specific restrictions; do not widen reusable Object surfaces |
| Slot conditions | `4911` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve applicable physical-to-advanced conversion through canonical resolver |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item `1586` / `modobj = 48` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `514` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Advanced shutter actuation with calibrated position/preset behavior; configuration selects addressing, mode and motor type.

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
