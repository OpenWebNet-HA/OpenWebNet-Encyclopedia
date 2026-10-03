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
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | 4674 family identity/catalogue: printed p. 41 / PDF p. 43; load table printed pp. 159-160 / PDF pp. 161-162 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `198` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `198` is wildcard `-1.-1.-1` and declares one Module. Installed hardware remains to be corroborated.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `198` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `668` | `8` | `463` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The single Module resolves to Object `8`, **Dimmer actuator**. Object `8` is also associated with Virgin Object `532` elsewhere in the catalogue; this firmware itself has no Device-specific Virgin Object row.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `198` | `1` | `1` | Virtual Configuration |
| `198` | `3` | `0` | Physical configuration |

Physical Configuration and Virtual Configuration are declared.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `198` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `198` | `A` | `0..9` | `0` | A; Environment |
| `198` | `PL` | `0..9` | `0` | PL; Light Point |
| `198` | `M` | `0`; `9` = `O/I` | `0` | M; mode (0,I/O) |
| `198` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | area / environment configurator |
| `PL` | `0..9` | light-point configurator |
| `M` | `0` / `O/I` | operating / function mode |
| `G1` | `0..9` | group configurator 1 |


Firmware 198 exposes the physical addressing/mode fields. Advanced dimmer settings are reusable Object parameters and must not be confused with physical configurators.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
| `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard | `0` | Voltage standard |
| `MIN_LEVEL_ADV` | `1..100` | `0` | Minimum level advanced; Default value depends on device and Type of load value |
| `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable | `0` | Enable / Disable minimum level |
| `G1` | `0..255` | `0` | Group 1 |
| `G2` | `0..255` | `0` | Group 2 |
| `G3` | `0..255` | `0` | Group 3 |
| `G4` | `0..255` | `0` | Group 4 |
| `G5` | `0..255` | `0` | Group 5 |
| `G6` | `0..255` | `0` | Group 6 |
| `G7` | `0..255` | `0` | Group 7 |
| `G8` | `0..255` | `0` | Group 8 |
| `G9` | `0..255` | `0` | Group 9 |
| `G10` | `0..255` | `0` | Group 10 |


### Product interpretation and source differences

**Object `8` - Dimmer actuator - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `MIN_LEVEL_ADV`, `MIN_AUTO`, `STATE_SAVING_ON_RESET`. The catalogue relation restricts `TYPE_LOAD`: Auto detect inductive (`1`), LED trailing edge / electronic transformers (`11`), LED leading edge (`12`), Forced capacitive (`2`), Forced inductive (`3`), Discharge lamps (`7`), Dali standard (`8`), DSI (`9`).

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `198` | `1` | `8` | `4145` | No textual predicate stored | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `198` | `8` | `594` | `MIN_LEVEL_ADV` | `1..100` (entire reusable range retained) | `0` | Minimum level advanced |
| `198` | `8` | `595` | `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable (entire reusable range retained) | `0` | enable disable minimum level |
| `198` | `8` | `596` | `TYPE_LOAD` | `1` = Auto detect inductive; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `2` = Forced capacitive; `3` = Forced inductive; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI | `0` | Type of Load; reusable default `0` is outside this subset; filter supplies no replacement default |
| `198` | `8` | `2180` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

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

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)
