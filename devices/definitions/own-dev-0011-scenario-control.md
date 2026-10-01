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
| Declared Modules | `2` | Implementation evidence |
| Categories | Command, Scenario, Multifunction | Capability model |

The Device is a four-button scenario control that can drive scenario modules, programmed CEN scenarios, and PLUS scenario representations. The canonical firmware models the four physical keys as two configurable command Modules.

## Commercial identities

The canonical catalogue contains ten Device records. Several database records combine finish variants into one code, while the official technical sheet names the printed references separately.

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - Axolute | `HS4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - Axolute | `HD4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - LivingLight | `L4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - LivingLight | `N4680` | Established identity | Catalogue cluster + official technical sheet |
| BTicino - LivingLight | `NT4680` | Established identity | Catalogue cluster + official technical sheet |
| Legrand - Arteor | `573902` | Established identity | Catalogue + official technical sheet |
| Legrand - Arteor | `573903` | Established identity | Catalogue + official technical sheet |
| Legrand - Arteor | `574503` | Established identity | Catalogue + official technical sheet |
| Legrand - Arteor | `574504` | Established identity | Catalogue + official technical sheet |
| Legrand - Céliane | `067217` | Established identity | Catalogue + official technical sheet |
| Legrand - Céliane | `067218` | Established identity | Catalogue + official technical sheet |
| Legrand - Mosaic | `078478` | Shared technical item | Implementation evidence; direct product sheet pending |
| Legrand - Mosaic | `079178` | Shared technical item | Implementation evidence; direct product sheet pending |

The count of printed identities exceeds the ten `EN_DEVICE` rows because BTicino finish variants are collapsed into combined catalogue codes such as `HC/HS/HD4680`.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00288-c-EN` | Technical sheet | revision/date not yet pinned | principal BTicino, Arteor and Céliane identities | [Archived PDF](../../sources/devices/documents/device-doc-scenario-control-mq00288-c-en/MQ00288-c-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00288-c-EN.pdf) |
| `MQ00288-c-FR` | Technical sheet | revision/date not yet pinned | scenario-control family | [Archived PDF](../../sources/devices/documents/device-doc-scenario-control-mq00288-c-fr/MQ00288-c-FR.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/MQ00288-c-FR.pdf) |
| `U3327B` | Installation/use instructions | revision/date not yet pinned | scenario-control family | [Archived PDF](../../sources/devices/documents/device-doc-scenario-control-u3327b/U3327B.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/U3327B.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | `MQ00288-c-EN` |
| User controls | 4 scenario buttons | `MQ00288-c-EN` |
| SCS nominal supply | `27 Vdc` | `MQ00288-c-EN` |
| SCS operating supply | `18..27 Vdc` | `MQ00288-c-EN` |
| Current draw | `9 mA` | `MQ00288-c-EN` |
| Primary physical configurators | `A`, `PL`, `M`, `N`, `DEL` | `MQ00288-c-EN` |

The sheet also describes an installation/destination-level configurator `I` when the control operates across an SCS/SCS interface. Firmware-scoped configuration does not contain an `I` field; reusable Object configuration carries installation and destination level fields. Preserve this as a source-model boundary rather than inventing a firmware field.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `402` | Implementation evidence |
| Main system | Lighting / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `6` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `7` | `1` | `0` | `0` | `2` | not stated | catalogue applicability |

## Module, Object, and Virgin Object model

Firmware `7` exposes two configurable Modules.

| Object | Description | Slots | Relationship |
| ---: | --- | --- | --- |
| `403` | Scenario module control | `1`, `2` | designated Object |
| `404` | Scheduled scenario | `1`, `2` | `M=CEN` alternative |
| `405` | Scenario PLUS Lighting Management | `1`, `2` | implementation selector alternative |
| `406` | Scheduled scenario PLUS | `1`, `2` | implementation selector alternative |

Virgin Object `502`, **Scene double command virgin**, applies to both slots and permits Objects `403..406`.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | product documentation + implementation evidence |
| Virtual Configuration | implementation evidence |
| Advanced Configuration | implementation evidence |

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

## Object configuration surfaces

The following subsections account for the complete reusable Object field surface present in the canonical catalogue. They preserve field identity without reproducing database serialization. Detailed Device-specific interpretation follows where available.

### Object `403` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M` | Modality |
| Addressing | `APL`, `INST_LEV`, `DEST_LEV` | Scenario module address; Installation level; Destination level |
| Scenario / button | `SCE_BUTT_1`, `SCE_BUTT_2`, `DEL_BUTTON_1`, `DEL_BUTTON_2` | Upper button scenario; Lower button scenario; Activation delay for upper button; Activation delay for lower button |

### Object `404` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | Area; Light point |
| Scenario / button | `BUTTON_1`, `BUTTON_2` | Upper button; Lower button |
| Audio / media | `IN_AUX_CHANNEL` | Input AUX channel |
| Timing | `START_DELAY` | Time of restart device (s) |

### Object `405` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Scenario / button | `PPT_SCE_1`, `PPT_SCE_2`, `DEL_BUTTON_1`, `DEL_BUTTON_2` | Delay (20); Delay (21); Only if Scenario1<>Scenario2 |
| Sensing / regulation | `TYPE_OF_REGULATION` | Only if Scenario1=Scenario2 |

### Object `406` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Scenario / button | `PPT_CEN_LOW`, `PPT_CEN_HIG`, `BUTTON_1`, `BUTTON_2` | Scheduled scenario PLUS number; Upper button; Lower button |

### Additional Device-specific interpretation

| Object | Surface | Principal fields / domains |
| --- | --- | --- |
| `403` | Scenario module control | `A`/`PL`, levels, scenario buttons, per-button delays |
| `404` | Scheduled scenario | `A`/`PL`, buttons, AUX input, start delay |
| `405` | Scenario PLUS | two scenario numbers, regulation target, per-button delays |
| `406` | Scheduled scenario PLUS | low/high scenario fields and two button fields |

#### Object `403` - Scenario module control

- mode: scenario activation+modification or activation-only;
- encoded A/PL target covering `A=0..10`, `PL=0..15`;
- installation level: private riser, local buses `1..15`, standard;
- destination level: private riser or local buses `1..15`;
- scenario buttons 1 and 2: `1..16`;
- independent delay tables for the two button positions.

The two delay tables are not byte-for-byte identical in the canonical database: one contains 63 stored enum rows and the other 56. Preserve the source data rather than normalizing them into a presumed common table.

#### Object `404` - Scheduled scenario

- `A=0..10`, `PL=0..15`;
- buttons `0..31`, defaults 1 and 2;
- AUX input `0..15`;
- start delay `0..255`, default 10.

#### Object `405` - Scenario PLUS Lighting Management

- two scenario numbers `1..255`;
- regulation target: all, lights, shutters, or stereo amplifiers;
- per-button delay tables.

#### Object `406` - Scheduled scenario PLUS

- low scenario field `0..255`;
- high scenario field `0..7`;
- two button fields `0..31`.

Together the low/high scenario fields support the published PLUS scenario-number domain, which the technical sheet describes as `1..2047`.

## Conditions, filters, and conversions

| Slot | Object | Condition | Conversion rule |
| ---: | --- | --- | ---: |
| 1 | `403` Scenario module control | `M<>CEN` | `14` |
| 2 | `403` Scenario module control | `M<>CEN` | `13` |
| 1 | `404` Scheduled scenario | `M=CEN` | `65` |
| 2 | `404` Scheduled scenario | `M=CEN` | `66` |
| `1..2` | `405` Scenario PLUS Lighting Management | `M=FAKE` | none |
| `1..2` | `406` Scheduled scenario PLUS | `M=FAKE` | none |

Generic conversion-rule evaluation belongs in [Catalogue Resolution](../../internals/catalogue-resolution.md).

### Catalogue filter references

| Filter | Object | Field | Source note |
| --- | --- | --- | --- |
| `1707` | `404` | `START_DELAY` | Start delay |

### Catalogue slot-condition references

| Condition | Slot | Object | Predicate | Conversion reference |
| --- | --- | --- | --- | --- |
| `4145` | `1` | `403` | empty source condition | `` |
| `4435` | `1` | `403` | `M<>CEN` | `14` |
| `4434` | `2` | `403` | `M<>CEN` | `13` |
| `4590` | `1` | `404` | `M=CEN` | `65` |
| `4591` | `2` | `404` | `M=CEN` | `66` |
| `4594` | `1` | `405` | `M=FAKE` | `` |
| `4594` | `2` | `405` | `M=FAKE` | `` |
| `4594` | `1` | `406` | `M=FAKE` | `` |
| `4594` | `2` | `406` | `M=FAKE` | `` |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 6`, brand/line and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | resolve the two active scenario Objects | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | obtain configured addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device participates in scenario control. Depending on the selected Object, its Modules represent scenario-module, programmed/CEN, or PLUS scenario functions. Generic scenario protocol semantics remain canonical under Functional Protocol.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

Programming must resolve the selected scenario Object per Module and preserve the contextual meaning of `M`, `N` and `DEL`. Physical CEN and PLUS representations must not be flattened into one generic scenario command.

## Source reconciliation

The scenario-control documentation has been reconciled with the two-Module catalogue model:

- the four physical buttons map to scenario groups selected by `M`, while the two catalogue Modules represent paired command positions rather than four independent Modules;
- F420-style scenario operation includes explicit scenario programming and deletion workflows with product feedback states;
- CEN/programmed-scenario use is distinct from local scenario-module use and must preserve the installation/destination-level context;
- Lighting Management software configuration can represent double-scenario, double-CEN and PLUS forms beyond the physical `M` selector;
- `N` and `DEL` are product delay selectors and are already mapped above, but their effect is tied to selected physical buttons rather than to a generic timer Object.

The remaining source gaps concern Mosaic variants and hardware corroboration.

## Evidence limits and open work

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
