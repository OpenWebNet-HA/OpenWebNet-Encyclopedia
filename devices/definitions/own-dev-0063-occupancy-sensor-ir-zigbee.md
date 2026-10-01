# Occupancy sensor + IR + ZigBee

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0063` | Project identity |
| Technical description | Occupancy sensor + IR + ZigBee | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSE2007`, `048831` | Canonical commercial records |
| Catalogue item | `58` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `41` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `17` | Canonical firmware catalogue |
| Categories | Occupancy sensing, IR, ZigBee, Lighting Management | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSE2007` | Established identity | canonical commercial record for item `58` |
| Legrand | `048831` | Established identity | canonical commercial record for item `58` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite version history | software compatibility record | 2015-03-20 | Explicitly lists `BMSE2007` among products managed by MyHOME Suite | [Archived original](../../sources/devices/documents/device-doc-myhome-suite-version-history-20150320/Version_History_MyHOME_Suite_20150320.pdf) | [Official compatibility source](https://myhomeswupdate.bticino.com/VersionHistory/Version_History_MyHOME_Suite_20150320.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Sensor function | Occupancy sensing | Canonical catalogue item description |
| Local interface | IR | Canonical catalogue item description |
| Radio interface | ZigBee | Canonical catalogue item description |
| Declared module count | `17` | Canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `58` | Canonical catalogue |
| Technical item | Occupancy sensor + IR + ZigBee | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `41` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `138` | `-1` | `-1` | `-1` | `17` | catalogue default | wildcard / unspecified applicability retained |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `138` | `414` | `119` Stand alone presence sensor | catalogue firmware/Object relation |
| `138` | `415` | `128` Scenarios daylight and presence sensor | catalogue firmware/Object relation |
| `138` | `416` | `164` Scenarios daylight sensor | catalogue firmware/Object relation |
| `138` | `417` | `165` Scenarios presence sensor | catalogue firmware/Object relation |
| `138` | `418` | `166` Stand alone daylight sensor | catalogue firmware/Object relation |
| `138` | `419` | `168` Stand alone daylight and presence sensor | catalogue firmware/Object relation |
| `138` | `420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435` | `431` IR scenario control | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `138` | `515` | catalogue candidate/template association |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `138` | Advanced Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `138` | `AID` | catalogue-defined domain | catalogue-scoped | ID |

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
| Object filters | `2107`, `2122`, `2137`, `2153`, `2267`, `2284`, `2299`, `2313`, `2368`, `2394` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | none | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `58` / `modobj = 41` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`119`, `128`, `164`, `165`, `166`, `168`, `431`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Occupancy sensor whose canonical catalogue identity explicitly combines occupancy sensing, IR and ZigBee. Its firmware reuses the broad seven-Object presence/daylight/scenario model and therefore requires Device filters before exposing Object-level parameters as capabilities.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The canonical catalogue binds `BMSE2007` and `048831` to item `58`, and official MyHOME Suite history corroborates `BMSE2007` software support. No dedicated publisher technical sheet has yet been retained, so radio profile, electrical consumption and detection geometry remain open.

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
