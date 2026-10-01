# PIR wall-mounted sensor - dual range

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0058` | Project identity |
| Technical description | PIR wall-mounted sensor - dual range | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE2003`, `048826` | Canonical commercial records |
| Catalogue item | `53` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `38` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Presence sensing, Daylight sensing, Automation | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE2003` | Established identity | canonical commercial record for item `53` |
| Legrand | `048826` | Established identity | canonical commercial record for item `53` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino/Legrand residential catalogue | product catalogue | historical publisher catalogue | `BMSE2003` wall-mounted PIR family and dimensional context; printed p. 159 / PDF p. 159 | [Archived original](https://archive.openwebnet-ha.org/sha256/9f/e5/9fe511c3ac12d861dff7d8d28ddec3b3612a27e99a804afbed89877c73a6b4ed.pdf) | [Official source](https://assets.legrand.com/webf/ch/ch_de_katalog_wohnbau.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Sensor technology | PIR | Canonical catalogue |
| Mounting | Wall/ceiling mounted PIR sensor | BTicino/Legrand residential catalogue, printed p. 159 / PDF p. 159 |
| Dimensions | `91 x 115.86 x 69.6 mm` | BTicino/Legrand residential catalogue, printed p. 159 / PDF p. 159 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `53` | Canonical catalogue |
| Technical item | PIR wall-mounted sensor - dual range | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `38` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `134` | `-1` | `-1` | `-1` | `17` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `134` | `326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341` | `431` IR scenario control | catalogue firmware/Object relation |
| `134` | `342` | `119` Stand alone presence sensor | catalogue firmware/Object relation |
| `134` | `343` | `128` Scenarios daylight and presence sensor | catalogue firmware/Object relation |
| `134` | `344` | `164` Scenarios daylight sensor | catalogue firmware/Object relation |
| `134` | `345` | `165` Scenarios presence sensor | catalogue firmware/Object relation |
| `134` | `346` | `166` Stand alone daylight sensor | catalogue firmware/Object relation |
| `134` | `347` | `168` Stand alone daylight and presence sensor | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `134` | `515` | catalogue candidate/template association |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `134` | Advanced Configuration | supported configuration route for this Device family |
| `134` | Physical configuration | supported configuration route for this Device family |
| `134` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `134` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `134` | `A` | catalogue-defined domain | catalogue-scoped | A |
| `134` | `PL` | catalogue-defined domain | catalogue-scoped | PL |
| `134` | `M` | catalogue-defined domain | catalogue-scoped | M |
| `134` | `S` | catalogue-defined domain | catalogue-scoped | S |
| `134` | `T` | catalogue-defined domain | catalogue-scoped | T |
| `134` | `D` | catalogue-defined domain | catalogue-scoped | D |

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
| Object filters | `135`, `136`, `137`, `138`, `139`, `140`, `141`, `142`, `143`, `144`, `145`, `146`, `2103`, `2118`, `2133`, `2149`, `2340`, `2341`, `2364`, `2397`, `2447`, `2459` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4439`, `4461`, `4477`, `4491`, `4505` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `53` / `modobj = 38` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Dual-range wall-mounted PIR/daylight sensor represented by the same seven reusable sensor Object families as the related BMSE2001/2002 devices. Physical and virtual configuration are both declared by the canonical catalogue.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue binds `BMSE2003` and `048826` to item `53`. The retained publisher catalogue corroborates the BMSE2003 wall-mounted sensor family and dimensions, but a dedicated BMSE2003 technical sheet has not yet been located; electrical and detection-range details are therefore not inferred from adjacent models.

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
