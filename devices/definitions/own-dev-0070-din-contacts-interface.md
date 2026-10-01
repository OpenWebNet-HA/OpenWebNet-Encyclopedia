# DIN contacts interface

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0070` | Project identity |
| Technical description | DIN contacts interface | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F428`, `003553` | Canonical commercial records |
| Catalogue item | `79` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `149` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Automation, Contact interface, DIN | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F428` | Established identity | canonical commercial record for item `79` |
| Legrand | `003553` | Established identity | canonical commercial record for item `79` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00002001-EN` | technical sheet | 2024-11-13 | `F428` two-contact DIN interface characteristics and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/68/e4/68e473ba614f1a24993302ab11a82bf9a272c78c58fe9861340178f6a3d89ebf.pdf) | [Official source](https://dar.bticino.com/asset/Documents/ST-00002001-EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` SCS BUS | `ST-00002001-EN` |
| Rated current | `9 mA` | `ST-00002001-EN` |
| Inputs | `2` independent contact inputs | `ST-00002001-EN` |
| Width | `2 DIN modules` | `ST-00002001-EN` |
| Protection | `IP20` | `ST-00002001-EN` |
| Maximum generic-cable contact distance | `50 m` | `ST-00002001-EN` |
| Maximum distance with specified BUS cable | up to `200 m` | `ST-00002001-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `79` | Canonical catalogue |
| Technical item | DIN contacts interface | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `149` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `144` | `-1` | `-1` | `-1` | `2` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `144` | `515, 516` | `181` Contact state | catalogue firmware/Object relation |
| `144` | `517, 518` | `410` Light control | catalogue firmware/Object relation |
| `144` | `519, 520` | `411` Automation control | catalogue firmware/Object relation |
| `144` | `521, 522` | `412` Lock/unlock actuator control | catalogue firmware/Object relation |
| `144` | `523, 524` | `413` Scenario module control | catalogue firmware/Object relation |
| `144` | `525, 526` | `414` Scheduled scenario | catalogue firmware/Object relation |
| `144` | `527, 528` | `415` Scenario PLUS Lighting Management | catalogue firmware/Object relation |
| `144` | `529, 530` | `416` Scheduled scenario PLUS | catalogue firmware/Object relation |
| `144` | `531, 532` | `419` Sound diffusion control | catalogue firmware/Object relation |
| `144` | `1366, 1367` | `417` AUX control | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `144` | `512` | catalogue candidate/template association |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `144` | Advanced Configuration | supported configuration route for this Device family |
| `144` | Physical configuration | supported configuration route for this Device family |
| `144` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `144` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `144` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `144` | `PL1` | catalogue-defined domain | catalogue-scoped | PL1 |
| `144` | `PL2` | catalogue-defined domain | catalogue-scoped | PL2 |
| `144` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `144` | `SPE` | catalogue-defined domain | catalogue-scoped | SPE |

## Object configuration surfaces

### Object `181` - Contact state

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `CONTACT_NUMBER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Number of contact |

### Object `410` - Light control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Addressing type |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `G` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group |
| `INST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Installation level |
| `DEST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Destination level |
| `A_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area of reference actuator |
| `PL_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point of reference actuator |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Contact type |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Seconds |
| `LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Level |
| `START_S` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Soft start speed |
| `STOP_S` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Soft stop speed |
| `DIMMING_S` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Dimming speed |
| `T_TIME` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Tabled time |

### Object `411` - Automation control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Addressing type |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `G` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group |
| `INST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Installation level |
| `DEST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Destination level |
| `A_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area of reference actuator |
| `PL_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point of reference actuator |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Contact type |

### Object `412` - Lock/unlock actuator control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Addressing type |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `G` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group |
| `INST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Installation level |
| `DEST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Destination level |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Contact type |

### Object `413` - Scenario module control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `APL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Scenario module address |
| `INST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Installation level |
| `DEST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Destination level |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Contact type |
| `SCE_BUTT_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Scenario number |
| `DEL_BUTTON_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay of scenario number |

### Object `414` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `CEN_BUTT_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Button |
| `MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Contact type |

### Object `415` - Scenario PLUS Lighting Management

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `PPT_SCE_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Upper button scenario |
| `TYPE_OF_REGULATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Regulation type |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Contact type |
| `DEL_BUTTON_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for upper button |

### Object `416` - Scheduled scenario PLUS

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Scheduled scenario PLUS number |
| `BUTTON_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Button |
| `MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Contact type |

### Object `417` - AUX control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `OUT_AUX_CH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | AUX channel |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Contact type |

### Object `419` - Sound diffusion control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Addressing type |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PF` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Audio point |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Contact type |
| `IS_FOLLOW_ME` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Follow me |
| `SOURCE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Source |
| `SUB_SOURCE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Sub source |
| `CHANNEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Channel (BB-Stereo) |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `246`, `247`, `250`, `251`, `1838` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4145`, `4711`, `4718`, `4723`, `4728`, `4729`, `4734`, `4735`, `4736`, `4737`, `4739`, `4740`, `4744`, `4745`, `4754`, `4757`, `4760`, `4765`, `4766`, `4777`, `4778`, `4799`, `4807`, `4815`, `4816`, `4834`, `4838`, `4839`, `4843`, `4845`, `4847`, `4848`, `4851`, `4852`, `4853`, `4854`, `4855`, `4856`, `4858`, `4861`, `4867`, `4868`, `4871`, `4876` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `79` / `modobj = 149` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`181`, `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `419`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

DIN interface integrating two conventional dry-contact controls into the SCS system. The two contact channels can address independent single loads, a double-function motor load, or scenario commands depending on configuration.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue maps `F428` and `003553`. The current publisher sheet directly documents `F428`; the archived MyHOME catalogue corroborates the historical `003553` commercial reference.

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
