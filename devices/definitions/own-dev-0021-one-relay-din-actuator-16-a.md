# One-relay DIN actuator 16 A

## Summary

This DIN-mounted SCS lighting actuator switches one load through a changeover relay. A local pushbutton provides direct load control, while the supported current and power depend on the connected load type.

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
| `MQ00274-e-EN` | Technical sheet | 2018-09-20 | `F411/1N` family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/4b/79/4b79903469f72ff4befecc79f211d428fbbbe385ebc038d2b7b0353fce83744d.pdf) | [Publisher PDF](https://dar.bticino.com/asset/Documents/MQ00274_e_EN.pdf) |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | F411/1N configuration: printed p. 120 / PDF p. 122; load/specification tables: printed pp. 157-160 / PDF pp. 159-162 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

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
| Nominal SCS supply | `27 Vdc` | `MQ00274-e-EN`, printed p. 1 / PDF p. 1 |
| Operating SCS supply | `18..27 Vdc` | Same sheet, p. 1 |
| SCS current draw | `22 mA` | Same sheet, p. 1 |
| Dissipated power at maximum load | `1.5 W` | Same sheet, p. 1 |
| Operating temperature | `-5..45 °C` | Same sheet, p. 1 |
| LED lamp-count limit | Maximum `10` lamps within the `500 W` load limit | Same sheet, p. 1 |
| Local button condition | Active only after the actuator is configured | Same sheet, Description, p. 1 |

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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `166` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Firmware `166` has wildcard applicability `-1.-1.-1` and declares one Module. Installed firmware/hardware remains to be corroborated.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `166` | `1` | `6` Light actuator | Fixed/designated metadata | `600` | `6` | `415` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

The single fixed Module is Object `6`, Light actuator, on slot `1`. Firmware `166` has no Virgin Object.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `166` | `1` | `1` | Virtual Configuration |
| `166` | `2` | `2` | Advanced Configuration |
| `166` | `3` | `0` | Physical configuration |

Physical configuration, Virtual Configuration and Advanced Configuration are declared.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `166` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `166` | `A` | `0..9` | `0` | A; Environment |
| `166` | `PL` | `0..9` | `0` | PL; Light Point |
| `166` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (1-4, Pul, Sla) |
| `166` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `166` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |
| `166` | `G3` | `0..9` | `0` | G3; G3 - (0-9) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | area / environment configurator |
| `PL` | `0..9` | light-point configurator |
| `M` | `0..4` / `SLA` / `PUL` | operating / function mode |
| `G1` | `0..9` | group configurator 1 |
| `G2` | `0..9` | group configurator 2 |
| `G3` | `0..9` | group configurator 3 |


The firmware-level table describes the product configurators. The reusable Light actuator Object below has a wider software configuration surface; that wider surface is not itself a statement about physical configurator positions.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open | `0` | Relay state on device reset |
| `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing | `0` | Load control mode |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `SUBTYPE` | `11` = Actuator; `1` = Lamp; `10` = Valve; `15` = Differential restart; `6` = Fan; `7` = Watering; `8` = Controlled socket; `9` = Lock | `11` | Type of load |
| `G1` | `0..255` | `0` | Group 1; Group = 0 means no group |
| `G2` | `0..255` | `0` | Group 2; Group = 0 means no group |
| `G3` | `0..255` | `0` | Group 3; Group = 0 means no group |
| `G4` | `0..255` | `0` | Group 4; Group = 0 means no group |
| `G5` | `0..255` | `0` | Group 5; Group = 0 means no group |
| `G6` | `0..255` | `0` | Group 6; Group = 0 means no group |
| `G7` | `0..255` | `0` | Group 7; Group = 0 means no group |
| `G8` | `0..255` | `0` | Group 8; Group = 0 means no group |
| `G9` | `0..255` | `0` | Group 9; Group = 0 means no group |
| `G10` | `0..255` | `0` | Group 10; Group = 0 means no group |


### Product interpretation and source differences

**Object `6` - Light actuator - product interpretation.**

**Firmware relationship.** The catalogue relation explicitly exposes `LOCAL_BUTTON`, `STATE_RESET`, `HOURS`, `MINUTES`, `SECONDS`, `LOAD_CONTROL_MODE`.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `166` | `1` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `166` | `6` | `372` | `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `166` | `6` | `373` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Relay state on device reset |
| `166` | `6` | `374` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `166` | `6` | `375` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `166` | `6` | `376` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `166` | `6` | `1861` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `1` |
| `1` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `1` |
| `1` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `1` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

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

Treat the product as one independently addressed Light actuator and preserve delayed-Slave/`PUL` and `G1..G3` semantics.

For Lighting Management installations, `MQ00274-e-EN` printed p. 1 / PDF p. 1 documents Plug&Go and Project&Download as distinct product procedures. Keep these separate from physical configurators and MyHOME Suite software configuration; the local load button is active only when the actuator is configured.

## Source reconciliation

The database, official automation guide and MyHOME Suite actuator documentation are reconciled. The material source tension is rating nomenclature: the item is named 16 A while published load-specific limits vary by load and revision. This dossier therefore does not infer a universal 16 A load capability.

## Evidence limits and open work

- Add a sanitized hardware fingerprint.
- Preserve historical load-table revisions explicitly.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [MQ00274-e-EN](https://archive.openwebnet-ha.org/sha256/4b/79/4b79903469f72ff4befecc79f211d428fbbbe385ebc038d2b7b0353fce83744d.pdf)
- [AUTOMATISME.pdf](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)
