# Special-functions control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0043` | Project identity |
| Technical description | Two-module automation control exposing special-function Object alternatives | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `H4651/2`, `L4651/2`, `AM5831/2`, `687376` | Canonical commercial records |
| Catalogue item | `1525` | Implementation evidence |
| Main catalogue system | Automation | Implementation evidence |
| Item model / `modobj` | `1` | Implementation evidence |
| Firmware definition | `147 / -1.-1.-1` | Implementation evidence |
| Declared Modules | `2` | Firmware catalogue |
| Categories | Automation, Control, Special functions | Capability model |

Two-module automation control exposing special-function Object alternatives.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4651/2` | established catalogue identity for item `1525` | canonical commercial record |
| BTicino - LivingLight | `L4651/2` | established catalogue identity for item `1525` | canonical commercial record |
| BTicino - Matix | `AM5831/2` | established catalogue identity for item `1525` | canonical commercial record |
| Legrand - Vela | `687376` | established catalogue identity for item `1525` | canonical commercial record |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME | technical/system documentation | revision/date as printed | MyHOME automation control model; exact four identities still need direct-sheet reconciliation | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product role | Bus automation control with selectable special-function topology | Canonical item/Object model |
| Declared logical modules | 2 | Canonical firmware catalogue |
| Commercial family | Four current catalogue identities | Canonical commercial records |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1525` | Implementation evidence |
| Technical item description | Special-functions control | Implementation evidence |
| Main system | Automation | Implementation evidence |
| Item model / `modobj` | `1` | Implementation evidence |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `147` | `-1` | `-1` | `-1` | `2` | catalogue default | wildcard / unspecified components retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `147` | `541, 542` | `401` Automation control | catalogue alternative |
| `147` | `543, 544` | `402` Lock/unlock actuator control | catalogue alternative |
| `147` | `545, 546` | `403` Scenario module control | catalogue alternative |
| `147` | `547, 548` | `404` Scheduled scenario | catalogue alternative |
| `147` | `549, 550` | `408` Open lock control | catalogue alternative |
| `147` | `560, 561` | `400` Light control | fixed/designated |
| `147` | `562` | `409` Sound diffusion control | catalogue alternative |

| Virgin Object status | Value |
| --- | --- |
| Associations | `501` |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `147` | Physical configuration | supported route for this Device family |
| `147` | Virtual Configuration | supported route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `147` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `147` | `A` | catalogue-defined domain | catalogue-scoped | Enviroment (0-9 GEN,GR,AMB) |
| `147` | `PL` | catalogue-defined domain | catalogue-scoped | Light Point |
| `147` | `M` | catalogue-defined domain | catalogue-scoped | Mode physical configurator (0-8, O/I,OFF,ON,SU_GIU,SU_GIU_M,PUL) |
| `147` | `SPE` | catalogue-defined domain | catalogue-scoped | Special function command control (0-9) |
| `147` | `AUX` | catalogue-defined domain | catalogue-scoped | AUX channel |

## Object configuration surfaces

### Object `400` - Light control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Standard mode means: with regulation for Point-to-point addressing, without regulation for Area, Group and General addressing |
| `ADDR_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Address (2, range `01..175`) Area (2, range `00..10`) Group (2, range 01...255) |
| `A` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Area |
| `PL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Light point |
| `G` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group |
| `INST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Installation level |
| `DEST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Destination level |
| `A_R` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | 0=no referent address |
| `PL_R` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | 0=no referent address |
| `HOURS` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for `MOD=128` |
| `MINUTES` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for `MOD=128` |
| `SECONDS` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for `MOD=128` |
| `LEVEL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for `MOD=129-134` |
| `START_S` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for `MOD=129-134` |
| `STOP_S` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for `MOD=129-134` |
| `DIMMING_S` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for `MOD=129-132` |
| `T_TIME` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Only for `MOD=1` |
| `IN_AUX_CHANNEL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Input AUX channel |

### Object `401` - Automation control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Modality |
| `ADDR_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Address (2, range `01..175`) Area (2, range `00..10`) Group (2, range `01..255`) |
| `A` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Area |
| `PL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Light point |
| `G` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group |
| `INST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Installation level |
| `DEST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Destination level |
| `A_R` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | 0= no referent |
| `PL_R` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | 0= no referent |
| `IN_AUX_CHANNEL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Input AUX channel |

### Object `402` - Lock/unlock actuator control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Modality |
| `ADDR_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Address (2, range `01..175`) Area (2, range `00..10`) Group (2, range `01..255`) |
| `A` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Area |
| `PL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Light point |
| `G` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Group |
| `INST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Installation level |
| `DEST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Destination level |
| `IN_AUX_CHANNEL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Input AUX channel |

### Object `403` - Scenario module control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Modality |
| `APL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Scenario module address |
| `INST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Installation level |
| `DEST_LEV` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Destination level |
| `SCE_BUTT_1` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Upper button scenario |
| `SCE_BUTT_2` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Lower button scenario |
| `DEL_BUTTON_1` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Activation delay for upper button |
| `DEL_BUTTON_2` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Activation delay for lower button |

### Object `404` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Area |
| `PL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Light point |
| `BUTTON_1` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Upper button |
| `BUTTON_2` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Lower button |
| `IN_AUX_CHANNEL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Input AUX channel |
| `START_DELAY` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Time of restart device (s) |

### Object `408` - Open lock control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `P` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | External unit address |
| `SEGMENT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Level |
| `IN_AUX_CHANNEL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Input AUX channel |

### Object `409` - Sound diffusion control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Addressing type |
| `A` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Area |
| `PF` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Audio point |
| `IN_AUX_CHANNEL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Input AUX channel |
| `IS_FOLLOW_ME` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Follow me |
| `SOURCE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Source |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `287`, `289`, `1709` | relation-specific restrictions; do not widen reusable Object surfaces |
| Slot conditions | `4145`, `4178`, `4182`, `4185`, `4423`, `4424`, `4425`, `4426`, `4428`, `4430`, `4593`, `4669`, `4670`, `4671`, `4672`, `4690`, `4691`, `4692`, `4693`, `4874`, `4877` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve applicable physical-to-advanced conversion through canonical resolver |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item `1525` / `modobj = 1` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `400`, `401`, `402`, `403`, `404`, `408`, `409` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Automation control functions selected through catalogue Object alternatives and physical/virtual conditions.

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
- [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)
