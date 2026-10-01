# One-relay DIN actuator 16 A

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0021` | Project identity |
| Technical description | DIN-rail one-relay lighting actuator with local load control | Catalogue + official documentation |
| Commercial identities | `F411/1N`, `003841` | Catalogue |
| Catalogue item | `1` - “1 relay DIN actuator 16 A” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `137` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `166` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Actuator, Lighting | Capability model |

The shared technical item covers BTicino `F411/1N` and Legrand `003841`.

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino | `F411/1N` | Established identity | canonical commercial record `1`; Commercial identity of this Technical Device | Canonical catalogue |
| Legrand | `003841` | Established identity | canonical commercial record `1706`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00274-e-EN` | Technical sheet | 2014-06-07 | `F411/1N` family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/4b/79/4b79903469f72ff4befecc79f211d428fbbbe385ebc038d2b7b0353fce83744d.pdf) | [Publisher PDF](https://dar.bticino.com/asset/Documents/MQ00274_e_EN.pdf) |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | F411 family sections; printed page unresolved / 1-based PDF page unresolved | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

For the multi-product guide, the printed and 1-based PDF page locators remain unresolved and are retained explicitly as an evidence gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 DIN modules | `MQ00274-e-EN` / publisher automation documentation |
| Outputs | 1 changeover relay | Publisher technical documentation |
| Local interface | load-control pushbutton | Publisher technical documentation |
| Resistive load at 230 Vac | `10 A` / `2300 W` | Later publisher load table |
| LED load | `500 W` | Later publisher load table |
| Linear fluorescent / electronic transformer | `4 A` | Later publisher load table |
| Ferromagnetic transformer | `4 A`, cos φ `0.5` | Later publisher load table |
| Fluorescent-load wiring guidance | minimum `3 m` between actuator and load | Publisher technical documentation |

The catalogue/family name retains “16 A”, while later publisher load tables give load-specific limits. The dossier therefore keeps the name and the electrical limits source-scoped instead of treating `16 A` as a universal switching rating.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1` | Canonical catalogue |
| Technical item description | 1 relay DIN actuator 16 A | Canonical catalogue |
| Item family | `2` - Actuator | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `137` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `166` | `-1` | `-1` | `-1` | `1` | not stated | wildcard applicability |

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
| `A` | `0..9` | `0` | area / environment configurator |
| `PL` | `0..9` | `0` | light-point configurator |
| `M` | `0..4` / `SLA` / `PUL` | `0` | operating / function mode |
| `G1` | `0..9` | `0` | group configurator 1 |
| `G2` | `0..9` | `0` | group configurator 2 |
| `G3` | `0..9` | `0` | group configurator 3 |

The firmware-level table describes the product configurators. The reusable Light actuator Object below has a wider software configuration surface; that wider surface is not itself a statement about physical configurator positions.

## Object configuration surfaces

### Object `6` - Light actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `STATE_RESET`, `LOAD_CONTROL_MODE`, `SUBTYPE` | operating mode and behavior selectors |
| Timing and levels | `DELAYED_OFF`, `HOURS`, `MINUTES`, `SECONDS` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`, `STATE_RESET`, `HOURS`, `MINUTES`, `SECONDS`, `LOAD_CONTROL_MODE`.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

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

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 137`, commercial identity and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single Light-actuator Module/Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured lighting address for the actuator | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M`, `G1`, `G2`, `G3` and reusable Light-actuator configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

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
- [MQ00274-e-EN](https://archive.openwebnet-ha.org/sha256/4b/79/4b79903469f72ff4befecc79f211d428fbbbe385ebc038d2b7b0353fce83744d.pdf)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)
