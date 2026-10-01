# Flush-mounted dimmer

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0027` | Project identity |
| Technical description | Flush-mounted SCS dimmer actuator | Catalogue + official documentation |
| Commercial identities | `H4674`, `L/N/NT4674` | Catalogue |
| Catalogue item | `23` - “Flush mounted dimmer” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `5` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `198` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Dimmer, Lighting | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino - LivingLight | `L/N/NT4674` | Established identity | canonical commercial record `23`; Commercial identity of this Technical Device | Canonical catalogue |
| BTicino - Axolute | `H4674` | Established identity | canonical commercial record `1731`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | 4674 dimmer-actuator sections; printed page unresolved / 1-based PDF page unresolved | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

The printed and 1-based PDF page locators remain unresolved and are retained explicitly as an evidence gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | Publisher `AUTOMATISME.pdf` |
| SCS supply | `27 Vdc` | Publisher `AUTOMATISME.pdf` |
| Maximum current draw | `5 mA` | Publisher `AUTOMATISME.pdf` |
| Local interface | upper/lower pushbuttons with indicator LED | Publisher `AUTOMATISME.pdf` |
| Supported slave dimmers | up to 3 `L/N/NT4416` units | Publisher `AUTOMATISME.pdf` |
| Associated published load range | `60..500 W` through the slave-dimmer arrangement | Publisher `AUTOMATISME.pdf` |
| Physical configurator positions | `A`, `PL`, `M`, `G` | Publisher `AUTOMATISME.pdf` |

The 4674 is the BUS actuator/controller for the slave-dimmer arrangement; the published load is handled through the associated slave dimmer rather than as a stand-alone internal power stage.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `23` | Canonical catalogue |
| Technical item description | Flush mounted dimmer | Canonical catalogue |
| Item family | `4` - Dimmer | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `5` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `198` | `-1` | `-1` | `-1` | `1` | not stated | wildcard applicability |

Firmware `198` is wildcard `-1.-1.-1` and declares one Module. Installed hardware remains to be corroborated.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `198` | `463` | `8` | `8` | Dimmer actuator |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `668` | `1` | `8` | fixed | Dimmer actuator |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The single Module resolves to Object `8`, **Dimmer actuator**. Object `8` is also associated with Virgin Object `532` elsewhere in the catalogue; this firmware itself has no Device-specific Virgin Object row.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `198` | `1` | `1` | Virtual Configuration |
| `198` | `3` | `0` | Physical configuration |

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | `0..9` | `0` | area / environment configurator |
| `PL` | `0..9` | `0` | light-point configurator |
| `M` | `0` / `O/I` | `0` | operating / function mode |
| `G1` | `0..9` | `0` | group configurator 1 |

Firmware 198 exposes the physical addressing/mode fields. Advanced dimmer settings are reusable Object parameters and must not be confused with physical configurators.

## Object configuration surfaces

### Object `8` - Dimmer actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `STATE_SAVING_ON_RESET`, `TYPE_LOAD`, `TYPE_STANDARD`, `MIN_AUTO` | operating mode and behavior selectors |
| Timing and levels | `DELAYED_OFF`, `HOURS`, `MINUTES`, `SECONDS`, `MIN_LEVEL`, `MIN_LEVEL_ADV` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `MIN_LEVEL_ADV`, `MIN_AUTO`, `STATE_SAVING_ON_RESET`. The catalogue relation restricts `TYPE_LOAD`: Auto detect inductive (`1`), LED trailing edge / electronic transformers (`11`), LED leading edge (`12`), Forced capacitive (`2`), Forced inductive (`3`), Discharge lamps (`7`), Dali standard (`8`), DSI (`9`).

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `1` | Device/Firmware topology conditions |
| Object/Firmware filters | `4` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `8` | `4145` | No textual predicate - conversion-driven or unconditional catalogue row | - |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `8` | `594` | `MIN_LEVEL_ADV` | Minimum level advanced | `1` | - |
| `8` | `595` | `MIN_AUTO` | enable disable minimum level | `1` | - |
| `8` | `596` | `TYPE_LOAD` | Type of Load | `0` | `1` - Auto detect inductive<br>`11` - LED trailing edge / electronic transformers<br>`12` - LED leading edge<br>`2` - Forced capacitive<br>`3` - Forced inductive<br>`7` - Discharge lamps<br>`8` - Dali standard<br>`9` - DSI |
| `8` | `2180` | `STATE_SAVING_ON_RESET` | State saving on reset | `1` | - |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 5` and the 4674 dimmer-actuator family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single dimmer Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured dimmer address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M`, `G1` and reusable dimmer parameters without confusing them with the slave power stage | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/).

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact item is currently retained.

## Programming

Treat the product as one addressed dimmer Module. Do not infer modern universal-dimmer load-selection semantics merely because they exist on the shared Object `8` surface.

## Source reconciliation

The catalogue establishes one Dimmer actuator Module and the two commercial identities. The archived automation documentation corroborates the 4674 family role. Shared Object `8` contains fields used by newer dimmers as well, so this dossier deliberately distinguishes Object capability from firmware-applicable configuration.

## Evidence limits and open work

- Recover and archive a dedicated H4674/L4674 technical-sheet revision if a publisher original is located.
- Add a sanitized hardware fingerprint.
- Resolve the single catalogue condition into a human-readable Device-specific rule.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
