# Two-module special control

## Summary


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0005` | Project identity |
| Technical description | Two-module configurable special-function SCS control | Catalogue + official technical sheet |
| Catalogue item | `1524` - “Special control” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `16` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `146` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Command, Multifunction, Lighting, Automation, Scenario, Audio / Video | Capability model |

This technical definition covers the shared catalogue capability core used by 13 commercial Device records. The official `MQ00285-d-EN` technical sheet directly covers `067553`, `H4651M2`, `L4651M2`, and `AM5831M2`. The other records remain catalogue-correlated commercial identities pending individual document review.

## Commercial identities


### Directly documented references

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4651M2` | Established identity | Catalogue + `MQ00285-d-EN` |
| BTicino - LivingLight | `L4651M2` | Established identity | Catalogue + `MQ00285-d-EN` |
| BTicino - Matix | `AM5831M2` | Established identity | Catalogue + `MQ00285-d-EN` |
| Legrand - Céliane | `067553` | Established identity | Catalogue + `MQ00285-d-EN` |

### Additional commercial records sharing item 1524

| Brand / line | References | Status |
| --- | --- | --- |
| Arnould Espace Evolution | `64162`, `64362` | Shared technical item; individual product-document review pending |
| Legrand Arteor | `571849`, `573987` | Shared technical item; individual product-document review pending |
| Legrand Céliane | `067242` | Shared technical item; individual product-document review pending |
| Legrand Mosaic | `078472`, `078475`, `079172`, `079175` | Shared technical item; individual product-document review pending |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00285-d-EN` - Special control | Technical sheet | 09/06/2014 | `067553`, `H4651M2`, `L4651M2`, `AM5831M2` | [Archived original](https://archive.openwebnet-ha.org/sha256/03/f5/03f5093d833c675ac3fdf10c2e3b21e38e494bc3b3637d2838454e9a85b81cab.pdf) | [Official PDF](https://assets.legrand.com/pim/NP-FT-GT/MQ00285-d-EN.pdf) |

The nine-page sheet is unusually valuable because it documents several otherwise unrelated functional systems exposed by the same configurable control.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting size | 2 flush-mounted modules | Official technical sheet |
| Controls | 4 buttons | Official technical sheet |
| Indicators | two-colour LEDs with local brightness/off adjustment | Official technical sheet |
| SCS nominal supply | `27 Vdc` | Official technical sheet |
| SCS operating supply | `18..27 Vdc` | Official technical sheet |
| Maximum LED-brightness current | `6 mA` H4651M2; `7.5 mA` 067553; `8.5 mA` L4651M2 and AM5831M2 | Official technical sheet |
| Operating temperature | `5..35 °C` | Official technical sheet |
| Physical configurator positions | `A`, `PL/PF`, `M`, `LIV1/AUX`, `LIV2`, `SPE`, `I` | Official technical sheet |

For the four named references, the official sheet establishes:


The seven documented configurator positions strongly support the ordinary diagnostic interpretation `N_CONF = 7`, but a known-hardware observation is still required before marking that value as corroborated.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1524` | Canonical catalogue |
| Item model / `modobj` | `16` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `146` | `-1` | `-1` | `-1` | `2` | catalogue default | wildcard / unspecified applicability |

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Object | Description | Relationship |
| --- | --- | --- | --- |
| `146` | `400` | Light control | catalogue firmware/Object relation |
| `146` | `401` | Automation control | catalogue firmware/Object relation |
| `146` | `402` | Lock/unlock actuator control | catalogue firmware/Object relation |
| `146` | `403` | Scenario module control | catalogue firmware/Object relation |
| `146` | `404` | Scheduled scenario | catalogue firmware/Object relation |
| `146` | `405` | Scenario PLUS Lighting Management | catalogue firmware/Object relation |
| `146` | `408` | Open lock control | catalogue firmware/Object relation |
| `146` | `409` | Sound diffusion control | catalogue firmware/Object relation |
| `146` | `427` | Floor call control | catalogue firmware/Object relation |
| `146` | `430` | Staircase light control | catalogue firmware/Object relation |
| `146` | `406` | Scheduled scenario PLUS | catalogue firmware/Object relation |

### Virgin Objects

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `146` | `501` | catalogue candidate/template association |

### Reconciled topology notes


Firmware `146` exposes two configurable Modules and a broad set of Object alternatives.

| Object | Description | Slots |
| ---: | --- | --- |
| `400` | Light control | `1`, `2` |
| `401` | Automation control | `1`, `2` |
| `402` | Lock/unlock actuator control | `1`, `2` |
| `403` | Scenario module control | `1`, `2` |
| `404` | Scheduled scenario | `1`, `2` |
| `405` | Scenario PLUS Lighting Management | `1`, `2` |
| `406` | Scheduled scenario PLUS | `1`, `2` |
| `408` | Open lock control | `1`, `2` |
| `409` | Sound diffusion control | `1` |
| `427` | Floor call control | `1`, `2` |
| `430` | Staircase light control | `1`, `2` |

Virgin Object `501`, **Special double command virgin**, applies to both slots and permits all Objects above plus Object `407` AUX control.

The broad Object set explains why this Device belongs to several functional categories despite being one Physical Device.

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `146` | Physical configuration | retained Device-specific configuration modality |
| `146` | Virtual Configuration | retained Device-specific configuration modality |
| `146` | Advanced Configuration | retained Device-specific configuration modality |


The catalogue declares:

- Physical configuration
- Virtual Configuration
- Advanced Configuration

The official sheet independently documents physical configuration and MyHOME Suite virtual configuration.

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `146` | `AID` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `146` | `A` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `146` | `PL/PF` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `146` | `M` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `146` | `LIV1/AUX` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `146` | `LIV2` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `146` | `SPE` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `146` | `I` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |

### Published and reconciled details


| Field | Catalogue domain | Purpose |
| --- | --- | --- |
| `AID` | Device identity field | not a physical configurator |
| `A` | `0..9`, `GEN=12`, `GR=13`, `AMB=14`, `AUX=15` | environment/address scope |
| `PL/PF` | `0..9` | lighting/audio point |
| `M` | `0..8`, `O/I=9`, `OFF=10`, `ON=11`, `UP/DOWN=12`, `UP/DOWN monostable=13`, `CEN=14`, `PUL=15`, plus a second stored literal `9` entry | base mode |
| `LIV1/AUX` | `0..9` | level / AUX physical field |
| `LIV2` | `0..9` | second level field |
| `SPE` | `0,1,2,3,6,8,9,ON(11)` | special-function selector |
| `I` | `0..9` | automation interface address |

The duplicate stored `M` value `9` - one row labelled `O/I` and another labelled `9` - is retained as a canonical database irregularity. It must not be silently deduplicated without context.

The official sheet uses `A=1..9` and `PL=1..9` for ordinary physical point-to-point addressing while virtual configuration extends the logical ranges.

## Object configuration surfaces

### Object `400` - Light control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LEVEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `START_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `STOP_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DIMMING_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `T_TIME` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `401` - Automation control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL_R` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `402` - Lock/unlock actuator control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `403` - Scenario module control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `APL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SCE_BUTT_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SCE_BUTT_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEL_BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEL_BUTTON_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `404` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `START_DELAY` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `405` - Scenario PLUS Lighting Management

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PPT_SCE_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PPT_SCE_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_OF_REGULATION` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEL_BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEL_BUTTON_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `406` - Scheduled scenario PLUS

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PPT_CEN_HIG` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `408` - Open lock control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `P` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SEGMENT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `409` - Sound diffusion control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PF` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IS_FOLLOW_ME` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SOURCE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `427` - Floor call control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `N1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `N2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SEGMENT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `430` - Staircase light control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `N1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `N2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SEGMENT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Reconciled Object notes


The reachable Objects expose the following major reusable parameter groups:

| Object | Principal configuration surface |
| ---: | --- |
| `400` Light control | mode; point/area/group/general address; installation/destination level; reference address; timed/dimmer parameters; AUX input |
| `401` Automation control | bistable/monostable/blades mode; address scope; installation/destination level; reference address; AUX input |
| `402` Lock/unlock actuator control | disable/enable mode; address scope; installation/destination level; AUX input |
| `403` Scenario module control | activation/edit mode and encoded scenario-module address |
| `404` Scheduled scenario | `A`, `PL`, button `0..31`, AUX input, restart delay |
| `405` Scenario PLUS Lighting Management | two scenario/delay fields, regulation type, per-button delay values |
| `406` Scheduled scenario PLUS | scenario number low/high fields and two button numbers |
| `407` AUX control | command mode, AUX output `1..15`, AUX input `0..15` |
| `408` Open lock control | external-unit address `0..95`, segment, AUX input |
| `409` Sound diffusion control | point/area/general address, audio point, follow-me, source, AUX input |
| `427` Floor call control | point/general call type, internal-unit address, segment, AUX input |
| `430` Staircase light control | internal-unit address, segment, AUX input |

Large enumerations such as encoded scenario addresses and delay tables remain machine-extractable from the canonical database. The Device page records their complete semantic domains without duplicating hundreds of mechanically repetitive rows.

## Conditions, filters, and conversions

### Relation filters

| Scope | Filter IDs | Interpretation |
| --- | --- | --- |
| Device/Object relations | `697`, `698`, `701`, `704`, `706`, `708`, `709`, `712`, `716`, `717`, `1708`, `1797`, `1902`, `4120`, `4133` | apply before exposing reusable Object values |

### Slot conditions and conversions

| Scope | Condition IDs | Conversion treatment |
| --- | --- | --- |
| Device slots | `4145`, `4177`, `4181`, `4184`, `4585`, `4586`, `4594`, `4606`, `4608`, `4609`, `4620`, `4622`, `4623`, `4634`, `4636`, `4637`, `4648`, `4649`, `4651`, `4652`, `4664`, `4665`, `4667`, `4668`, `4685`, `4686`, `4688`, `4689`, `4800`, `4801`, `4805`, `4806`, `4808`, `4809`, `4813`, `4814`, `4817`, `4818`, `4822`, `4823`, `4833`, `4837`, `4842`, `4844`, `4846`, `4849`, `4850`, `4859`, `4860`, `4864`, `4865`, `4866`, `4875`, `4878`, `4879`, `4880`, `4881` | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1524` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`400`, `401`, `402`, `403`, `404`, `405`, `406`, `408`, `409`, `427`, `430`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 16`, brand, line, and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe physical firmware despite wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3`, `6`, `13` | hardware, microcontroller, Device ID when supported | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | determine selected Objects on the two Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine Module system/address configuration | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability


Depending on configuration, this Device crosses multiple OpenWebNet domains. The Device definition establishes that those roles can exist on this hardware; the linked functional references remain authoritative for wire semantics.

- [`WHO 1` - Lighting](../../functional/who-1-lighting/)
- [`WHO 2` - Automation](../../functional/who-2-automation/)
- scenario/CEN behavior
- sound diffusion
- video door-entry related control
- AUX/transversal control

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming


A correct programmer must evaluate `SPE`, `M`, address-scope fields, level/interface fields, and the associated condition/conversion graph before selecting an Object. It must not treat “Special control” as one fixed Object.

See [Configuration Programming](../../programming/configuration-programming.md) and [Programming Validation](../../programming/validation.md).

## Source reconciliation


The nine-page `MQ00285-d-EN` sheet has been reconciled as a Device-specific function map rather than only as a list of reusable Objects:

- lighting functions include simple, timed, dimming and special light-control variants selected through `M`, `SPE` and the level fields;
- `LIV1` / `LIV2` participate in published dimming/special-function selection and must not be treated as generic numeric fields without the surrounding mode;
- automation, Device lock/unlock, scenario-module, programmed-scenario, PLUS-scenario, video-door-entry, staircase/floor-call, sound-system and AUX roles share the same Physical Device but use different button/address semantics;
- the sheet documents programming/editing behavior for scenario functions, including product-level activation/programming distinctions that are not visible from Object identity alone;
- operation across SCS/SCS interfaces uses installation/destination-level concepts that correspond to reusable `INST_LEV` / `DEST_LEV` fields;
- audio/video and sound roles reuse `PL/PF`, level and special-function fields contextually, so a validator must interpret them only after resolving the selected function family.

This source is now represented as a product-specific selector/function model. Remaining gaps are commercial variants, exact package relationships and hardware corroboration, not omission of the principal published function families.

## Evidence limits and open work


- Archive and hash `MQ00285-d-EN`, language variants, and any earlier/later revisions.
- Locate authoritative product sheets for the other nine records sharing item `1524`.
- Capture known hardware to corroborate `modobj`, expected physical configurator count, firmware, Object projection, addressing, and configuration.
- Review every condition/conversion branch against the published function tables, preserving mismatches or implementation-only branches.
- Determine the exact commercial/package relationships across Arnould, BTicino, Legrand Arteor, Céliane, and Mosaic records.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
