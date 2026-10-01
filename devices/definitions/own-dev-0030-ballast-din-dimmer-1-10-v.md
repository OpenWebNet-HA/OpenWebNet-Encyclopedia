# Ballast DIN dimmer 1-10 V

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0030` | Project identity |
| Technical description | DIN-rail 1-10 V ballast dimmer | Catalogue + official documentation |
| Commercial identities | `F413` | Catalogue |
| Catalogue item | `31` - “Ballast DIN dimmer 1-10 V” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `7` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `174` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Dimmer, Lighting | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino / Undefined | `F413` | `31` | Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | F413 ballast-dimmer technical-data and configuration sections; printed page unresolved / 1-based PDF page unresolved | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

The printed and 1-based PDF page locators remain unresolved and are retained explicitly as an evidence gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 DIN modules | Publisher `AUTOMATISME.pdf` |
| SCS supply | `27 Vdc` | Publisher `AUTOMATISME.pdf` |
| Maximum current draw | `30 mA` | Publisher `AUTOMATISME.pdf` |
| Control output | `1..10 V` ballast-control signal | Publisher `AUTOMATISME.pdf` |
| Maximum connected ballasts | `4` | Publisher `AUTOMATISME.pdf` |
| Published ballast families | T8, T5 and energy-saving ballast types | Publisher `AUTOMATISME.pdf` |
| Local interface | load-control pushbutton and status LED | Publisher `AUTOMATISME.pdf` |

The publisher guide requires the controlled ballasts to be earthed; absence of the earth connection is documented as a possible cause of malfunction.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `31` | Canonical catalogue |
| Technical item description | Ballast DIN dimmer 1-10 V | Canonical catalogue |
| Item family | `4` - Dimmer | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `7` | AS_ITEM_SYSTEM |
| Commercial records | `1` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `174` | `-1` | `-1` | `-1` | `1` | not stated | wildcard applicability |

Firmware `174` is wildcard `-1.-1.-1` and declares one Module.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `174` | `420` | `8` | `8` | Dimmer actuator |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `606` | `1` | `8` | fixed | Dimmer actuator |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| - | - | - | - | No firmware-scoped Virgin Object | - | - |

The Module resolves to Object `8`, **Dimmer actuator**. Firmware `174` has no Device-specific Virgin Object row. Any broader Virgin-Object association of reusable Object `8` belongs to the shared catalogue Object model and is not a firmware-scoped capability claim for this Device.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `174` | `1` | `1` | Virtual Configuration |
| `174` | `2` | `2` | Advanced Configuration |
| `174` | `3` | `0` | Physical configuration |

Advanced Configuration, Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | `0..9` | `0` | area / environment configurator |
| `PL` | `0..9` | `0` | light-point configurator |
| `M` | `0..4` / `SLA` / `PUL` | `0` | operating / function mode |
| `G1` | `0..9` | `0` | group configurator 1 |

Firmware 174 exposes the physical addressing/mode/group fields. Generic Dimmer Object capabilities are kept separate below.

## Object configuration surfaces

### Object `8` - Dimmer actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `LOCAL_BUTTON`, `STATE_SAVING_ON_RESET`, `TYPE_LOAD`, `TYPE_STANDARD`, `MIN_AUTO` | operating mode and behavior selectors |
| Timing and levels | `DELAYED_OFF`, `HOURS`, `MINUTES`, `SECONDS`, `MIN_LEVEL`, `MIN_LEVEL_ADV` | timers, delays, levels and transition parameters |
| Group membership | `G1`, `G2`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | reusable group memberships; `0` means no group |

**Firmware relationship.** The catalogue relation explicitly exposes `MIN_LEVEL_ADV`, `MIN_AUTO`, `STATE_SAVING_ON_RESET`. The catalogue relation restricts `TYPE_LOAD`: Auto detect capacitive (`0`), Auto detect inductive (`1`), Alogen lamp (`10`), LED trailing edge / electronic transformers (`11`), LED leading edge (`12`), CFL trailing edge (`13`), CFL leading edge (`14`), Forced capacitive (`2`), Forced inductive (`3`), Discharge lamps (`7`), Dali standard (`8`), DSI (`9`).

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `1` | Device/Firmware topology conditions |
| Object/Firmware filters | `4` | Conditional Object configuration exposure |
| Referenced conversion rules | `1` | `3` |

### Slot conditions

| Slot | Object | Condition ID | Condition expression | Conversion rule |
| ---: | ---: | ---: | --- | ---: |
| `1` | `8` | `4149` | No textual predicate - conversion-driven or unconditional catalogue row | `3` |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `8` | `393` | `MIN_LEVEL_ADV` | Minimum level advanced | `1` | - |
| `8` | `394` | `MIN_AUTO` | enable disable minimum level | `1` | - |
| `8` | `395` | `TYPE_LOAD` | Type of Load | `0` | `0` - Auto detect capacitive<br>`1` - Auto detect inductive<br>`10` - Alogen lamp<br>`11` - LED trailing edge / electronic transformers<br>`12` - LED leading edge<br>`13` - CFL trailing edge<br>`14` - CFL leading edge<br>`2` - Forced capacitive<br>`3` - Forced inductive<br>`7` - Discharge lamps<br>`8` - Dali standard<br>`9` - DSI |
| `8` | `2170` | `STATE_SAVING_ON_RESET` | State saving on reset | `1` | - |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 7` and the F413 ballast-dimmer family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the single Dimmer Object | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the configured ballast-dimmer address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M`, `G1` and load/minimum-level configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device participates in [`WHO 1` - Lighting](../../functional/who-1-lighting/), with dimming applied through its 1-10 V ballast-control role.

## Observed behavior and corroboration

No sanitized F413 hardware fingerprint is currently retained.

## Programming

Preserve the classic `M` mode and group semantics. Do not substitute current F413N electrical specifications or configuration behavior unless the hardware identity has been established.

## Source reconciliation

The canonical database establishes F413 as a one-slot Dimmer actuator with physical, virtual and advanced configuration. Publisher material confirms the 1-10 V family role, while the currently published F413N material represents a later/current reference. The dossier therefore keeps historical F413 identity separate from successor specifications.

## Evidence limits and open work

- Recover and archive a publisher-original F413-specific technical sheet.
- Resolve the recorded condition and conversion rule into human-readable behavior.
- Add a sanitized hardware fingerprint and establish F413 versus F413N revision continuity.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
