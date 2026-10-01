# Extended control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0014` | Project identity |
| Technical description | Two-module extended configurable command | Catalogue + official MyHOME documentation |
| Catalogue item | `1104` - “Extended control item” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `9` | Implementation evidence |
| Firmware definition | wildcard `-1.-1.-1`, firmware `153` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Configuration modes | Physical, Virtual | Implementation evidence |
| Categories | Command, Multifunction | Capability model |

The Extended control is a two-Module configurable command whose catalogue capability model spans lighting, automation, locking, scenario, AUX, video-door-entry and sound-diffusion roles. It is therefore best treated as a multifunction command platform rather than as one fixed functional button.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4655` | Documented commercial identity | Catalogue + archived MyHOME Automation guide |
| BTicino - LivingLight | `L4655` | Documented commercial identity | Catalogue + archived MyHOME Automation guide |
| Legrand - Mosaic | `078466` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `078467` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `078469` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `079266` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `079267` | Shared technical item | Implementation evidence; direct product document pending |
| Legrand - Mosaic | `079269` | Shared technical item | Implementation evidence; direct product document pending |

The archived MyHOME Automation guide also associates the extended-control function with historical catalogue references used in older ranges. Those references should be added to the commercial index only after the exact printed-reference relationship has been checked against the corresponding catalogue revision.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Automation guide | System / product guide | revision/date not yet pinned | `H4655` / `L4655`: index on printed p. 2 / PDF p. 4; substantive mentions on printed pp. 36, 58, 61, 70, 87, 88, 91, 133, 160 / PDF pp. 38, 60, 63, 72, 89, 90, 93, 135, 162 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/80/6a/806a55bffb924f5ef7b25398432c0a86ab210722adc30b81f33558c6ec36f561.pdf) | publisher source not currently retained |

The guide documents cross-bus / extended-control use cases. Direct sheets for the six Mosaic references remain a documentation gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2-module configurable command | Catalogue + archived MyHOME Automation guide |
| Physical configuration surface | `A`, `PL`, `M`, `LIV1`, `LIV2`, `SPE`, `I` | Archived MyHOME Automation guide + implementation evidence |
| Installation-level selector | `I` distinguishes local section, logical-expansion buses and main riser | Archived MyHOME Automation guide |

These physical/configuration facts describe the command surface. Electrical ratings not established in the retained source set remain an evidence gap rather than being inferred.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1104` | Implementation evidence |
| Main system | Lighting / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `9` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `153` | `-1` | `-1` | `-1` | `2` | not stated | wildcard applicability |

Wildcard values are catalogue applicability sentinels, not claims about an installed firmware version.

## Module, Object, and Virgin Object model

The firmware provides two configurable Modules. Direct firmware/Object associations are:

| Object | Description | Slots | Stored selection condition |
| ---: | --- | --- | --- |
| `400` | Light control | 1, 2 | blank/default association |
| `401` | Automation control | 1, 2 | `M=SU_GIU;SPE=0;AUX=0` |
| `402` | Lock/unlock actuator control | 1, 2 | `M<>0;SPE=1;AUX=0` |
| `403` | Scenario module control | 1, 2 | `M<>0;SPE=4;AUX=0` |
| `404` | Scheduled scenario | 1, 2 | `M<>0;SPE=6;AUX=0` |
| `407` | AUX control | 1, 2 | `M=0;SPE=0;AUX<>0` |
| `408` | Open lock control | 1, 2 | `M<>0;SPE=8;AUX=0` |
| `409` | Sound diffusion control | 1 only | `M<>0;SPE=9;AUX=0` |

Virgin Object `501`, **Special double command virgin**, applies to both slots and permits the direct Objects above plus:

- `405` Scenario PLUS Lighting Management;
- `406` Scheduled scenario PLUS;
- `427` Floor call control;
- `430` Staircase light control.

This gives 12 candidate Object roles across the two Modules.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | product documentation + implementation evidence |
| Virtual Configuration | implementation evidence |

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | identity field | - | not a physical configurator |
| `A` | `0..9`, `GEN`, `GR`, `AMB` | - | stored values `12..14` for symbolic scopes |
| `PL` | `0..9` | - | point / function target |
| `M` | `0..8`, `O/I`, `OFF`, `ON`, `UP/DOWN`, `UP/DOWN monostable`, `CEN`, `PUL` | - | multifunction mode |
| `LIV1` | `0..99` | - | level/configuration field |
| `LIV2` | `0..9` | - | level/configuration field |
| `SPE` | `0..9` | - | special-function selector |
| `I` | `0..9`, `CEN` | - | interface / destination-related selector |

### Source-model irregularity: `AUX`

Several slot-condition rows explicitly reference an `AUX` variable, but firmware `153` contains no firmware-scoped configuration field named `AUX`.

This must remain an unresolved source-model fact. Do not silently map `AUX` to `I`, an Object AUX channel, or another field without independent evidence.

## Object configuration surfaces

The following subsections account for the complete reusable Object field surface present in the canonical catalogue. They preserve field identity without reproducing database serialization. Detailed Device-specific interpretation follows where available.

### Object `400` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M`, `A_R`, `PL_R`, `LEVEL`, `START_S`, `STOP_S`, `DIMMING_S` | Standard mode means: with regulation for Point-to-point addressing, without regulation for Area, Group and General addressing; 0=no referent address; Only for `MOD=129-134`; Only for `MOD=129-132` |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `INST_LEV`, `DEST_LEV` | Address (2, range `01..175`) Area (2, range `00..10`) Group (2, range 01...255); Area; Light point; Group; Installation level; Destination level |
| Timing | `HOURS`, `MINUTES`, `SECONDS`, `T_TIME` | Only for `MOD=128`; Only for `MOD=1` |
| Audio / media | `IN_AUX_CHANNEL` | Input `AUX` channel |

### Object `401` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M`, `A_R`, `PL_R` | Modality; 0= no referent |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `INST_LEV`, `DEST_LEV` | Address (2, range `01..175`) Area (2, range `00..10`) Group (2, range `01..255`); Area; Light point; Group; Installation level; Destination level |
| Audio / media | `IN_AUX_CHANNEL` | Input `AUX` channel |

### Object `402` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M` | Modality |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `INST_LEV`, `DEST_LEV` | Address (2, range `01..175`) Area (2, range `00..10`) Group (2, range `01..255`); Area; Light point; Group; Installation level; Destination level |
| Audio / media | `IN_AUX_CHANNEL` | Input `AUX` channel |

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
| Audio / media | `IN_AUX_CHANNEL` | Input `AUX` channel |
| Timing | `START_DELAY` | Time of restart device (s) |

### Object `407` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M`, `OUT_AUX_CH` | Modality; `AUX` channel |
| Audio / media | `IN_AUX_CHANNEL` | Input `AUX` channel |

### Object `408` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `P` | External unit address |
| Object-specific | `SEGMENT` | Level |
| Audio / media | `IN_AUX_CHANNEL` | Input `AUX` channel |

### Object `409` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PF` | Addressing type; Area; Audio point |
| Audio / media | `IN_AUX_CHANNEL`, `IS_FOLLOW_ME`, `SOURCE` | Input `AUX` channel; Follow me; Source |

### Additional Device-specific interpretation

| Role / Object | Principal configuration fields | Device applicability note |
| --- | --- | --- |
| `400` Light control | modes; address scope; `A`/`PL`/`G`; levels; timing; `AUX` | direct candidate |
| `401` Automation control | modes; address scope; levels; referent; `AUX` | direct candidate |
| `402`/`407`/`408` lock/`AUX`/door-entry | role-specific address and `AUX` surfaces | direct candidates; published reachability differs |
| `403`..`406` scenario roles | scenario target, levels, buttons, delays, PLUS scenario fields | direct and Virgin-only candidates |
| `409` Sound diffusion | addressing, source, follow-me, `AUX` | direct candidate on slot 1 |
| `427`/`430` | floor-call / staircase-light fields | Virgin-only candidates requiring reachability proof |

The complete candidate surface is large because the firmware reuses generic command Objects. The Device-specific dossier preserves the reachable Object set while the detailed reusable parameter semantics remain canonical in the Device Model and programming material.

### Lighting and automation

Object `400` exposes 42 stored command modes including toggle, timed ON, dimming, blinking, fixed-level and customized command forms; point/area/group/general addressing; installation/destination levels; referent address; timing components; level/ramp parameters; and `AUX` input.

Object `401` exposes bistable, monostable and blades-control modes with point/area/group/general addressing, installation/destination levels, referent address and `AUX` input.

### Lock, `AUX` and door-entry roles

- Object `402`: disable/enable lock modes, broad address scopes and `AUX` input.
- Object `407`: `AUX` command mode, output `AUX` channel `1..15`, input `AUX` channel `0..15`.
- Object `408`: external-unit address `0..95`, segment scope and `AUX` input.
- Object `427`: point-to-point/general floor call, internal-unit address split across `N1/N2`, segment scope and `AUX` input.
- Object `430`: staircase-light control with internal-unit address, segment scope and `AUX` input.

### Scenario roles

Object `403` provides scenario activation / modification, full A/PL scenario-module target encoding, installation/destination levels, two scenario-button selections and independent delay tables.

Object `404` provides A/PL, two button numbers, `AUX` input and start delay.

Virgin-only Object `405` provides two scenario numbers, regulation target and independent button delays. Object `406` provides the split low/high PLUS scenario number and two button fields.

### Sound diffusion

Object `409` provides point/area/general addressing, area and audio point, source selection, follow-me flag and `AUX` input.

## Conditions, filters, and conversions

| Surface | Condition / issue | Interpretation |
| --- | --- | --- |
| Object selection | `M`/`SPE`/`AUX` predicates in implementation rows | selects role candidates per Module |
| `AUX` condition variable | referenced by slot conditions but absent from firmware-scoped fields | Unresolved - do not map to `I` or an Object AUX field without evidence |
| Published reachability | guide excludes video-door-entry and AUX from Special-control functions | Virgin-only candidate reachability requires independent proof |

### Catalogue filter references

| Filter | Object | Field | Source note |
| --- | --- | --- | --- |
| `1703` | `404` | `START_DELAY` | Start delay |

### Catalogue slot-condition references

| Condition | Slot | Object | Predicate | Conversion reference |
| --- | --- | --- | --- | --- |
| `4145` | `1` | `400` | empty source condition | `` |
| `4145` | `2` | `400` | empty source condition | `` |
| `4673` | `1` | `401` | `M=SU_GIU;SPE=0;AUX=0` | `` |
| `4673` | `2` | `401` | `M=SU_GIU;SPE=0;AUX=0` | `` |
| `4427` | `1` | `402` | `M<>0;SPE=1;AUX=0` | `` |
| `4427` | `2` | `402` | `M<>0;SPE=1;AUX=0` | `` |
| `4429` | `1` | `403` | `M<>0;SPE=4;AUX=0` | `` |
| `4429` | `2` | `403` | `M<>0;SPE=4;AUX=0` | `` |
| `4431` | `1` | `404` | `M<>0;SPE=6;AUX=0` | `` |
| `4431` | `2` | `404` | `M<>0;SPE=6;AUX=0` | `` |
| `4460` | `1` | `407` | `M=0;SPE=0;AUX<>0` | `` |
| `4460` | `2` | `407` | `M=0;SPE=0;AUX<>0` | `` |
| `4432` | `1` | `408` | `M<>0;SPE=8;AUX=0` | `` |
| `4432` | `2` | `408` | `M<>0;SPE=8;AUX=0` | `` |
| `4433` | `1` | `409` | `M<>0;SPE=9;AUX=0` | `` |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item model `9`, brand/line and installed configurator count | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 30` | determine active Object for each of the two Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine configured system/address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration and physical-configurability information | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on selected Object, this Device can participate in lighting, automation, scenario, AUX, video-door-entry and sound-diffusion functions.

The Device page establishes the available hardware/Object projection. Generic WHO command syntax belongs under [Functional Protocol](../../functional/).

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

A correct programmer must resolve the selected Object per Module before validating Object-scoped parameters. It must also preserve the unresolved `AUX` condition variable rather than inventing a conversion.

See [Object Programming](../../programming/object-programming.md), [Configuration Programming](../../programming/configuration-programming.md), and [Programming Validation](../../programming/validation.md).

## Source reconciliation

The archived MyHOME automation guide materially narrows the Extended control interpretation:

- physical configurator `I` selects the installation level: `1..9` address another logical-expansion bus, `0` selects the local section, and `CEN` selects the main riser in the documented architecture;
- the published architecture uses this mechanism to extend addressable automation/light-control scope across interfaces;
- `LIV1` / `LIV2` participate in the published extended dimmer/control functions and therefore require the selected function context;
- importantly, the product guide describes Extended control as providing the Special-control functions **except** video-door-entry and AUX functions.

That last point conflicts with the broader reusable/Virgin-Object candidate surface in the implementation database. The Device page therefore treats AUX and video-door-entry-related Virgin-only candidates as implementation evidence requiring independent reachability proof, not as established published product capabilities.

## Evidence limits and open work

- Locate official product sheets for all six Mosaic references.
- Obtain a sanitized H4655 or L4655 hardware fingerprint.
- Determine the runtime/physical meaning of the condition variable `AUX`.
- Establish whether Virgin-only Objects `405`, `406`, `427` and `430` are reachable through current physical or virtual configuration on this firmware.
- Archive additional language/revision variants of the extended-control documentation.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
