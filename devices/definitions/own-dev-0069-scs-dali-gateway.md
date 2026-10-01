# SCS/DALI gateway

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0069` | Project identity |
| Technical description | SCS/DALI gateway | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `F429`, `002631` | Canonical commercial records |
| Catalogue item | `71` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `138` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `8` | Canonical firmware catalogue |
| Categories | Lighting, DALI gateway, DIN interface | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F429` | Established identity | canonical commercial record for item `71` |
| Legrand | `002631` | Established identity | canonical commercial record for item `71` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U2068C` | instruction sheet | 2021-05 | `F429` SCS/DALI interface operation and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/88/80/888012e06924ff327b19eb352392050f968a9c43bd25748e9c1e278c44ca0b8a.pdf) | [Official source](https://dar.bticino.com/asset/Documents/U2068C.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Primary supply | `110..240 Vac` | `U2068C` |
| SCS interface | SCS BUS | `U2068C` |
| DALI outputs | `8` independent outputs | `U2068C` |
| Maximum DALI devices | up to `16` devices per output | `U2068C` |
| Local controls | `3` pushbuttons with corresponding LEDs | `U2068C` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `71` | Canonical catalogue |
| Technical item | SCS/DALI gateway | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `138` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `180` | `-1` | `-1` | `-1` | `8` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `180` | `612, 613, 614, 615, 616, 617, 618, 619` | `8` Dimmer actuator | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `180` | Advanced Configuration | supported configuration route for this Device family |
| `180` | Physical configuration | supported configuration route for this Device family |
| `180` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `180` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `180` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `180` | `G` | catalogue-defined domain | catalogue-scoped | G (0-9) |
| `180` | `M` | catalogue-defined domain | catalogue-scoped | Mode (0-4, sla, pul) |

## Object configuration surfaces

### Object `8` - Dimmer actuator

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `LOCAL_BUTTON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local button modality |
| `DELAYED_OFF` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Delayed OFF for Slave (s) |
| `STATE_SAVING_ON_RESET` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | State saving on reset |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Seconds |
| `MIN_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minimum level |
| `TYPE_LOAD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type of load |
| `TYPE_STANDARD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Voltage standard |
| `MIN_LEVEL_ADV` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minimum level advanced |
| `MIN_AUTO` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Enable / Disable minimum level |
| `G1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 1 |
| `G2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 2 |
| `G3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 3 |
| `G4` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 4 |
| `G5` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 5 |
| `G6` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 6 |
| `G7` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 7 |
| `G8` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 8 |
| `G9` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 9 |
| `G10` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group 10 |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `491`, `492`, `493`, `494`, `495`, `496`, `497`, `498`, `2175` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4937`, `4938`, `4956`, `4957`, `4958`, `4959`, `4961`, `4962` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `71` / `modobj = 138` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Gateway between SCS lighting control and DALI devices. It exposes eight independently addressed DALI outputs, each supporting up to sixteen DALI devices; the publisher explicitly states that DALI-2 protocol support is not guaranteed.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue maps `F429` and `002631` to one technical item. The current BTicino instruction sheet directly documents `F429`; the older Legrand reference is retained from the canonical commercial catalogue.

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
