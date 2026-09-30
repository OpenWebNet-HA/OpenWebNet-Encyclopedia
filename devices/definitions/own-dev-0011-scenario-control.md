# Scenario control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0011` | Project identity |
| Technical description | Two-module four-button scenario control | Catalogue + official technical sheet |
| Catalogue item | `402` - “Scenario control” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `6` | Implementation evidence |
| Firmware definition | `1.0.0`, firmware `7` | Implementation evidence |
| Declared Modules | 2 | Implementation evidence |
| Categories | Command, Scenario, Multifunction | Capability model |

The Device is a four-button scenario control that can drive scenario modules, programmed CEN scenarios, and PLUS scenario representations. The canonical firmware models the four physical keys as two configurable command Modules.

## Commercial identities

The canonical catalogue contains ten Device records. Several database records combine finish variants into one code, while the official technical sheet names the printed references separately.

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `HC4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino Axolute | `HS4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino Axolute | `HD4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino L/N/NT | `L4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino L/N/NT | `N4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino L/N/NT | `NT4680` | Established identity | Catalogue cluster + official technical sheet |
| Legrand Arteor | `573902` | Established identity | Catalogue + official technical sheet |
| Legrand Arteor | `573903` | Established identity | Catalogue + official technical sheet |
| Legrand Arteor | `574503` | Established identity | Catalogue + official technical sheet |
| Legrand Arteor | `574504` | Established identity | Catalogue + official technical sheet |
| Legrand Céliane | `067217` | Established identity | Catalogue + official technical sheet |
| Legrand Céliane | `067218` | Established identity | Catalogue + official technical sheet |
| Legrand Mosaic | `078478` | Shared technical item | Implementation evidence; direct product sheet pending |
| Legrand Mosaic | `079178` | Shared technical item | Implementation evidence; direct product sheet pending |

The count of printed identities exceeds the ten `EN_DEVICE` rows because BTicino finish variants are collapsed into combined catalogue codes such as `HC/HS/HD4680`.

## Documentation

| Document | Type | Coverage | Archived original | Publisher |
| --- | --- | --- | --- | --- |
| `MQ00288-c-EN` | Technical sheet | principal BTicino, Arteor and Céliane identities | [Archived PDF](../../sources/devices/documents/device-doc-scenario-control-mq00288-c-en/MQ00288-c-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00288-c-EN.pdf) |
| `MQ00288-c-FR` | Technical sheet | scenario-control family | [Archived PDF](../../sources/devices/documents/device-doc-scenario-control-mq00288-c-fr/MQ00288-c-FR.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00288-c-FR.pdf) |
| `U3327B` | Installation/use instructions | scenario-control family | [Archived PDF](../../sources/devices/documents/device-doc-scenario-control-u3327b/U3327B.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/U3327B.pdf) |

## Physical characteristics

The 2014 English technical sheet establishes:

| Property | Value |
| --- | --- |
| Mounting | 2 flush-mounted modules |
| User controls | 4 scenario buttons |
| SCS nominal supply | `27 Vdc` |
| SCS operating supply | `18..27 Vdc` |
| Current draw | `9 mA` |
| Primary physical configurators | `A`, `PL`, `M`, `N`, `DEL` |

The sheet also describes an installation/destination-level configurator `I` when the control operates across an SCS/SCS interface. The firmware-scoped configuration table does not contain an `I` field; the reusable Object model instead carries installation and destination level fields. Preserve this as a source-model boundary rather than inventing a firmware field.

## Identity and firmware

| Field | Value |
| --- | --- |
| `EN_ITEM.id_item` | `402` |
| `AS_ITEM_SYSTEM.modobj` | `6` |
| Firmware | `7` |
| Firmware applicability | `1.0.0` |
| Firmware slots | `2` |
| Configuration modes | Physical, Virtual, Advanced |

## Module and Object model

Firmware `7` exposes two configurable Modules.

| Object | Description | Slots | Relationship |
| ---: | --- | --- | --- |
| `403` | Scenario module control | `1`, `2` | designated Object |
| `404` | Scheduled scenario | `1`, `2` | `M=CEN` alternative |
| `405` | Scenario PLUS Lighting Management | `1`, `2` | implementation selector alternative |
| `406` | Scheduled scenario PLUS | `1`, `2` | implementation selector alternative |

Virgin Object `502`, **Scene double command virgin**, applies to both slots and permits Objects `403..406`.

## Firmware-scoped configuration

| Field | Domain | Published meaning |
| --- | --- | --- |
| `AID` | Device identity | not a physical configurator |
| `A` | `0..9` | environment/address |
| `PL` | `0..9` | light point / scenario-module address component |
| `M` | `0..4`, `CEN` | physical scenario/CEN mode |
| `N` | `0..5` | selects which physical key delay applies to |
| `DEL` | `0..9` | delay preset |

### Published `M` mapping

The technical sheet documents:

| `M` | Physical keys activate |
| ---: | --- |
| `1` | scenarios `1..4` |
| `2` | scenarios `5..8` |
| `3` | scenarios `9..12` |
| `4` | scenarios `13..16` |
| `CEN` | CEN/programmed scenario mode |

With no CEN selector, the catalogue selects Scenario module Object `403`; with `M=CEN`, it selects Scheduled scenario Object `404`.

Implementation-only `M=FAKE` conditions expose PLUS Objects `405` and `406`; `FAKE` is not part of the physical `M` enum.

### Published delay mapping

| `N` | Delayed key(s) |
| ---: | --- |
| `0` | none |
| `1` | key 1 |
| `2` | key 2 |
| `3` | key 3 |
| `4` | key 4 |
| `5` | all four |

| `DEL` | Delay |
| ---: | --- |
| `0` | none |
| `1` | 1 min |
| `2` | 2 min |
| `3` | 3 min |
| `4` | 4 min |
| `5` | 5 min |
| `6` | 10 min |
| `7` | 15 min |
| `8` | 15 s |
| `9` | 30 s |

## Condition-selected topology

| Slot | Object | Condition | Conversion rule |
| ---: | --- | --- | ---: |
| 1 | `403` Scenario module control | `M<>CEN` | `14` |
| 2 | `403` Scenario module control | `M<>CEN` | `13` |
| 1 | `404` Scheduled scenario | `M=CEN` | `65` |
| 2 | `404` Scheduled scenario | `M=CEN` | `66` |
| `1..2` | `405` Scenario PLUS Lighting Management | `M=FAKE` | none |
| `1..2` | `406` Scheduled scenario PLUS | `M=FAKE` | none |

Generic conversion-rule evaluation belongs in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Reusable Object configuration

### Object `403` - Scenario module control

- mode: scenario activation+modification or activation-only;
- encoded A/PL target covering `A=0..10`, `PL=0..15`;
- installation level: private riser, local buses `1..15`, standard;
- destination level: private riser or local buses `1..15`;
- scenario buttons 1 and 2: `1..16`;
- independent delay tables for the two button positions.

The two delay tables are not byte-for-byte identical in the canonical database: one contains 63 stored enum rows and the other 56. Preserve the source data rather than normalizing them into a presumed common table.

### Object `404` - Scheduled scenario

- `A=0..10`, `PL=0..15`;
- buttons `0..31`, defaults 1 and 2;
- AUX input `0..15`;
- start delay `0..255`, default 10.

### Object `405` - Scenario PLUS Lighting Management

- two scenario numbers `1..255`;
- regulation target: all, lights, shutters, or stereo amplifiers;
- per-button delay tables.

### Object `406` - Scheduled scenario PLUS

- low scenario field `0..255`;
- high scenario field `0..7`;
- two button fields `0..31`.

Together the low/high scenario fields support the published PLUS scenario-number domain, which the technical sheet describes as `1..2047`.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 6`, brand/line and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | resolve the two active scenario Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | obtain configured addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Source reconciliation

The scenario-control documentation has been reconciled with the two-Module catalogue model:

- the four physical buttons map to scenario groups selected by `M`, while the two catalogue Modules represent paired command positions rather than four independent Modules;
- F420-style scenario operation includes explicit scenario programming and deletion workflows with product feedback states;
- CEN/programmed-scenario use is distinct from local scenario-module use and must preserve the installation/destination-level context;
- Lighting Management software configuration can represent double-scenario, double-CEN and PLUS forms beyond the physical `M` selector;
- `N` and `DEL` are product delay selectors and are already mapped above, but their effect is tied to selected physical buttons rather than to a generic timer Object.

The remaining source gaps concern Mosaic variants and hardware corroboration.

## Corroboration status and open work

- Locate direct product documentation for Mosaic `078478` and `079178`.
- Add a sanitized hardware fingerprint and corroborate firmware, configurator count, two-Module projection, addresses and configuration.
- Resolve the exact relationship between physical interface-level configurator `I` and reusable Object `INST_LEV/DEST_LEV` values.
- Preserve any package/finish differences between the several printed BTicino references.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
