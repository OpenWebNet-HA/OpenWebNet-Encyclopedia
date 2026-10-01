# PIR+US ceiling-mounted sensor

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0054` | Project identity |
| Technical description | PIR+US ceiling-mounted sensor | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE3003`, `048822` | Canonical commercial records |
| Catalogue item | `49` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `34` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Presence sensing, Daylight sensing, Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE3003` | Established identity | canonical commercial record for item `49` |
| Legrand | `048822` | Established identity | canonical commercial record for item `49` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE10699AA-FR` | technical/system guide | publisher guide | `048822` / `BMSE3003` physical characteristics and PIR+US detection coverage | [Archived original](../../sources/devices/documents/device-doc-scs-sensor-guide-le10699aa-fr/le10699aa-fr.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/le10699aa-fr.pdf) |
| `LE02817AD` | instruction sheet | publisher revision AD | `048820` / `048821` / `048822` installation and sensor-type characteristics | [Archived original](../../sources/devices/documents/device-doc-ceiling-sensors-le02817ad/LE02817AD.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LE02817AD.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` | `LE10699AA-FR` |
| Idle consumption | `17 mA` | `LE10699AA-FR` |
| Detection | PIR + ultrasonic, 360° ceiling detection | `LE10699AA-FR` |
| Ceiling cut-out | `65 mm` without box; `68 mm` with box | `LE10699AA-FR` |
| Protection | `IP20`; `IK04` | `LE10699AA-FR` |
| Operating temperature | `-5..45 °C` | `LE10699AA-FR` |
| Storage temperature | `-20..70 °C` | `LE10699AA-FR` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `49` | Canonical catalogue |
| Technical item | PIR+US ceiling-mounted sensor | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `34` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `141` | `-1` | `-1` | `-1` | `17` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `141` | `478` | `119` Stand alone presence sensor | catalogue firmware/Object relation |
| `141` | `479` | `128` Scenarios daylight and presence sensor | catalogue firmware/Object relation |
| `141` | `480` | `164` Scenarios daylight sensor | catalogue firmware/Object relation |
| `141` | `481` | `165` Scenarios presence sensor | catalogue firmware/Object relation |
| `141` | `482` | `166` Stand alone daylight sensor | catalogue firmware/Object relation |
| `141` | `483` | `168` Stand alone daylight and presence sensor | catalogue firmware/Object relation |
| `141` | `484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499` | `431` IR scenario control | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `141` | `515` | catalogue candidate/template association |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `141` | Advanced Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `141` | `AID` | catalogue-defined domain | catalogue-scoped | ID |

## Object configuration surfaces

### Object `119` - Stand alone presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Addressing type |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `G` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group number |
| `A_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Referent area address |
| `PL_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Referent light point address |
| `MAIN_GROUP` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Enable secondary groups |
| `G1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Secondary group 1 |
| `G2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Secondary group 2 |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Seconds |
| `FUNC_MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Operating mode |
| `PIR` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | PIR sensitivity |
| `US` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | US sensitivity |
| `INITIAL_OCCUPANCY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Initial occupancy |
| `MAINTAIN_OCCUPANCY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Maintain detection |
| `RETRIGGER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Retrigger |
| `ALERT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Alert |
| `ENABLE_LOAD_CONTROL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Enable load control |

### Object `128` - Scenarios daylight and presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay - Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay - Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay - Seconds |
| `SCHEMA` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Detection scheme |
| `PIR` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | PIR sensitivity |
| `US` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | US sensitivity |

### Object `164` - Scenarios daylight sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |

### Object `165` - Scenarios presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay - Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay - Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay - Seconds |
| `SCHEMA` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Detection scheme |
| `PIR` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | PIR sensitivity |
| `US` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | US sensitivity |

### Object `166` - Stand alone daylight sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Addressing type |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `G` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group number |
| `A_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area of reference actuator |
| `PL_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point of reference actuator |
| `TYPE_LOOP` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Loop type |
| `GD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Daylight cell group |
| `DAYLIGHT_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Provision of light (Lux) |
| `FUNC_MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Operating mode |
| `LIGHTING_REGULATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Lighting regulation |
| `DAYLIGHT_FACTOR` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Daylight factor |
| `NATURAL_LIGHT_FACTOR` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Natural light factor |
| `DAYLIGHT_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Daylight level |

### Object `168` - Stand alone daylight and presence sensor

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Addressing type |
| `A` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Area |
| `PL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Light point |
| `G` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Group number |
| `A_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Referent area address |
| `PL_R` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Referent light point address |
| `MAIN_GROUP` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Enable secondary groups |
| `G1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Sensor group 1 |
| `G2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Sensor group 2 |
| `TYPE_LOOP` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Loop type |
| `GD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Daylight cell group |
| `DAYLIGHT_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Daylight setpoint (Lux) |
| `PROVISION_OF_LIGHT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Provision of light (Lux) |
| `HOURS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Hours |
| `MINUTES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Minutes |
| `SECONDS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Seconds |
| `FUNC_MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Operating mode |
| `PIR` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | PIR sensitivity |
| `US` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | US sensitivity |
| `INITIAL_OCC` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Initial detection |
| `MAINTAIN_OCC` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Maintain detection |
| `RE-TRIGGER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Re-trigger |
| `ALERT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Alert |
| `LOAD_CONTROL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Enable load control |
| `LIGHTING_REGULATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Lighting regulation |
| `NATURAL_LIGHT_FACTOR` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Natural light factor |
| `DAYLIGHT_FACTOR` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Daylight factor |
| `DAYLIGHT_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Daylight level |

### Object `431` - IR scenario control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Scenario number |
| `TYPE_OF_REGULATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Regulation type |
| `ID1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | ID1 |
| `ID2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | ID2 |
| `ID3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | ID3 |
| `UNIT_NUMBER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Push button number |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `2110`, `2125`, `2140`, `2156`, `2331`, `2332`, `2333`, `2371`, `2391`, `2452`, `2464` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4439`, `4461`, `4477`, `4491`, `4505` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `49` / `modobj = 34` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

BUS-powered ceiling presence/daylight sensor using combined PIR and ultrasonic detection. It exposes reusable presence, daylight, combined-sensor, scenario-sensor and regulation Object families with Device-specific filters.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue binds `BMSE3003` and `048822`. Publisher documentation directly identifies the product as the dual-technology PIR+US ceiling sensor and documents its electrical and detection characteristics.

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
