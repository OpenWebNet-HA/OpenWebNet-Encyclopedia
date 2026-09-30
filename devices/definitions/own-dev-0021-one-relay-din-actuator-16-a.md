# One-relay DIN actuator 16 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0021` | Project identity |
| Technical description | DIN-rail one-relay lighting actuator with local load control | Catalogue + official automation documentation |
| Catalogue item / model | `1` / `modobj 137` | Implementation evidence |
| Firmware applicability | firmware `166`, `-1.-1.-1`, one slot | Implementation evidence |
| Commercial identities | `F411/1N`, `003841` | Catalogue |
| Categories | Actuator, Lighting | Capability model |

The shared technical item covers BTicino `F411/1N` and Legrand `003841`.

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Undefined | `F411/1N` | `1` | Commercial identity of this Technical Device | Canonical catalogue |
| Legrand / Undefined | `003841` | `1706` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| MQ00274-e-EN | Technical sheet | 2014-06-07 | Whole document | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-f411-1n-mq00274-e-en/MQ00274-e-EN.pdf) |
| AUTOMATISME.pdf | MyHOME automation guide | historical publisher guide | F411 family sections; exact printed/PDF locator pending | Archived original | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) |

Multi-product guides retain an explicit page-location limitation until both printed and 1-based PDF page numbers are pinned.

## Physical and electrical characteristics

The official guide describes a 2-DIN actuator with one changeover relay and local load-control pushbutton. Its later load table gives `10 A` resistive / `2300 W` at 230 Vac, `500 W` LED, `4 A` linear-fluorescent/electronic-transformer and `4 A cosφ 0.5` ferromagnetic-transformer capability. Older catalogues use the family label 16 A and contain revision-dependent load figures, so load-specific limits are retained instead of treating 16 A as universal. Fluorescent-load guidance requires at least `3 m` between actuator and load.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1` | Canonical catalogue |
| Technical item description | 1 relay DIN actuator 16 A | Canonical catalogue |
| Item family | `2` - Actuator | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `137` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Declared slots | Default | Status |
| ---: | ---: | ---: | ---: | --- | --- |
| `166` | `-1` | `-1` | `1` | `1` | `0` |

Firmware `166` has wildcard applicability `-1.-1.-1` and declares one Module. Installed firmware/hardware remains to be corroborated.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `166` | `415` | `6` | `6` | Light actuator |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `600` | `1` | `6` | fixed | Light actuator |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The single fixed Module is Object `6`, Light actuator, on slot `1`. Firmware `166` has no Virgin Object.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `166` | `1` | `1` | Virtual Configuration |
| `166` | `2` | `2` | Advanced Configuration |
| `166` | `3` | `0` | Physical configuration |

Physical configuration, Virtual Configuration and Advanced Configuration are declared.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | 0..9 | 0 | area / environment configurator |
| `PL` | 0..9 | 0 | light-point configurator |
| `M` | 0..4 / SLA / PUL | 0 | operating / function mode |
| `G1` | 0..9 | 0 | group configurator 1 |
| `G2` | 0..9 | 0 | group configurator 2 |
| `G3` | 0..9 | 0 | group configurator 3 |

The firmware-level table describes the product configurators. The reusable Light actuator Object below has a wider software configuration surface; that wider surface is not itself a statement about physical configurator positions.

## Object configuration surfaces

### Object `6` - Light actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `STATE_RESET`, `LOAD_CONTROL_MODE`, `SUBTYPE` | operating mode and behavior selectors |
| Timing and levels | `DELAYED_OFF`, `HOURS`, `MINUTES`, `SECONDS` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; 0 means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`, `STATE_RESET`, `HOURS`, `MINUTES`, `SECONDS`, `LOAD_CONTROL_MODE`.

The tables above account for the reusable Object fields without reproducing database serialization metadata. Generic Object capability is kept distinct from the Device/firmware relationship and from physical configurator positions.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `1` | Device/Firmware topology conditions |
| Object/Firmware filters | `6` | Conditional Object configuration exposure |
| Referenced conversion rules | `1` | `1` |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `6` | `4147` | No textual predicate - conversion-driven or unconditional catalogue row | `1` |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `6` | `372` | `LOCAL_BUTTON` | Local button modality | `1` | - |
| `6` | `373` | `STATE_RESET` | Relay state on device reset | `1` | - |
| `6` | `374` | `HOURS` | Hours | `1` | - |
| `6` | `375` | `MINUTES` | Minutes | `1` | - |
| `6` | `376` | `SECONDS` | Seconds | `1` | - |
| `6` | `1861` | `LOAD_CONTROL_MODE` | Load_control_mode | `1` | - |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | Identify the Device model/family and compare it with catalogue identity. | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Record installed firmware instead of treating wildcard catalogue applicability as an observed version. | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve Module/Object topology, especially when candidates share a slot. | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Inspect addressing for the resolved Module/Object when exposed. | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Corroborate firmware/Object configuration and physical/software relationships. | [Configuration](../../diagnostics/dim35-configuration.md) |

Catalogue applicability is not itself an observed runtime result.

## Functional applicability

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/).

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact item is currently retained.

## Programming

Treat the product as one independently addressed Light actuator and preserve delayed-Slave/PUL and `G1..G3` semantics.

## Source reconciliation

The database, official automation guide and MyHOME Suite actuator documentation are reconciled. The material source tension is rating nomenclature: the item is named 16 A while published load-specific limits vary by load and revision. This dossier therefore does not infer a universal 16 A load capability.

## Evidence limits and open work

- Add a sanitized hardware fingerprint.
- Preserve historical load-table revisions explicitly.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [MQ00274-e-EN](../../sources/devices/documents/device-doc-f411-1n-mq00274-e-en/MQ00274-e-EN.pdf)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
