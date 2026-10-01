# Touch control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0094` | Project identity |
| Technical description | Touch control | Canonical catalogue |
| Commercial identities | `HC/HS4657M3_OLD` | Canonical commercial records |
| Catalogue item | `925` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `12` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Automation, Control | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS4657M3_OLD` | Established catalogue identity | canonical commercial record for item `925` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Catalogue product class | `Touch control` | canonical item description |
| Commercial variants represented | `1` | canonical commercial records |
| Declared Module count | `2` | canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `925` | Canonical catalogue |
| Technical item | Touch control | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `12` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `201` | `-1` | `-1` | `-1` | `2` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `201` | `759` | `400` Light control | catalogue firmware/Object relation |
| `201` | `760` | `401` Automation control | catalogue firmware/Object relation |
| `201` | `761` | `404` Scheduled scenario | catalogue firmware/Object relation |
| `201` | `762` | `480` User interface settings | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `201` | Physical configuration | supported configuration route for this Device family |
| `201` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `201` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `201` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `201` | `PL` | catalogue-defined domain | catalogue-scoped | PL |
| `201` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `201` | `INT` | catalogue-defined domain | catalogue-scoped | INT |

## Object configuration surfaces

### Object `400` - Light control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Addressing type |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `G` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group |
| `INST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Installation level |
| `DEST_LEV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Destination level |
| `A_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point of reference actuator |
| `PL_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point of reference actuator |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Seconds |
| `LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Level |
| `START_S` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Soft start speed |
| `STOP_S` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Soft stop speed |
| `DIMMING_S` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Dimming speed |
| `T_TIME` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Tabled time |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Input AUX channel |

### Object `401` - Automation control

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
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Input AUX channel |

### Object `404` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `BUTTON_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Upper button |
| `BUTTON_2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Lower button |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Input AUX channel |
| `START_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time of restart device (s) |

### Object `480` - User interface settings

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `STATE_OF_UNUSED_BUTTON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | State of unused button |
| `STATE_UPDATE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Feedback update |
| `LED_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | LED intensity level |
| `LED_FADE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | LED fading |
| `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Backlight intensity stand by level |
| `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is OFF, only one led can be used for the standby. |
| `BACKLIGHT_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Delay time (seconds) |
| `PROXIMITY_ENABLE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Proximity Activation |
| `SIGNBOARD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Signboard activation type |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `1710`, `3112`, `3119`, `3126`, `3134`, `3157` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `925` / `modobj = 12` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`400`, `401`, `404`, `480`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The canonical catalogue describes this technical item as Touch control. Its firmware exposes `4` distinct Object families across the declared Module topology. This definition records those surfaces without treating reusable Object vocabulary as proof of undocumented physical capabilities.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the named configuration-mode boundary. Product-programmed Devices must not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical MyHOME Suite catalogue binds `HC/HS4657M3_OLD` to technical item `925`. A dedicated retained publisher product document for this exact technical item has not yet been reconciled in the Device source archive, so external documentation discovery remains partial.

## Evidence limits and open work

- Locate and archive dedicated publisher documentation for the exact commercial references where available.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
