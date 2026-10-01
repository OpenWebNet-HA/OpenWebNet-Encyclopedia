# Basic control actuator

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0060` | Project identity |
| Technical description | Basic control actuator | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `3476` | Canonical commercial records |
| Catalogue item | `55` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `105` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Lighting, Actuator, Local control, Flush-mounted | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `3476` | Established identity | canonical commercial record for item `55` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST_00000915_EN` | technical sheet | publisher sheet | `3476` Basic Control Actuator electrical characteristics, local input and configuration | [Archived original](../../sources/devices/documents/device-doc-3476-st00000915-en/ST_00000915_EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/ST_00000915_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` from SCS BUS; operating `18..27 Vdc` | `ST_00000915_EN` |
| Consumption | `13 mA` | `ST_00000915_EN` |
| External input | Traditional N/O pushbutton via dedicated input leads | `ST_00000915_EN` |
| Output | Single relay contact for load control | `ST_00000915_EN` |
| Installation | Flush box, junction box, shutter box or duct | `ST_00000915_EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `55` | Canonical catalogue |
| Technical item | Basic control actuator | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `105` | Canonical inventory |
| Commercial records | `1` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `194` | `-1` | `-1` | `-1` | `1` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `194` | `690` | `6` Light actuator | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| all | - | no Virgin Object association in selected firmware rows |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `194` | Advanced Configuration | supported configuration route for this Device family |
| `194` | Physical configuration | supported configuration route for this Device family |
| `194` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `194` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `194` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `194` | `PL` | catalogue-defined domain | catalogue-scoped | PL |
| `194` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `194` | `G1` | catalogue-defined domain | catalogue-scoped | G1 |

## Object configuration surfaces

### Object `6` - Light actuator

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `M` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Modality |
| `LOCAL_BUTTON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local button modality |
| `DELAYED_OFF` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Delayed OFF for Slave (s) |
| `STATE_RESET` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Relay state on device reset |
| `LOAD_CONTROL_MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Load control mode |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Seconds |
| `SUBTYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type of load |
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
| Object filters | `683`, `1868`, `1898` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4145` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `55` / `modobj = 105` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Compact SCS actuator with local traditional pushbutton input and one relay load output. It exposes one actuator Object and supports advanced, physical and virtual configuration.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The dedicated publisher sheet directly identifies `3476` as the Basic Control Actuator. Current MyHOME Server compatibility documentation lists it as a one-channel supported device from production batch `12W39`.

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
