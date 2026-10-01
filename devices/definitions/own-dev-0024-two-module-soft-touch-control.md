# Two-module Soft Touch control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0024` | Project identity |
| Technical description | Two-module capacitive Soft Touch SCS command with configurable function and UI settings | Catalogue + official documentation |
| Commercial identities | `HC/HS4653/2`, `HD4653M2` | Catalogue |
| Catalogue item | `12` - “Soft touch control” | Implementation evidence |
| Main catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `8` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `149` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Command, Lighting, Automation, Scenario, Sound, Access | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino - Axolute | `HC/HS4653/2` | Established identity | canonical commercial record `12`; Commercial identity of this Technical Device | Canonical catalogue |
| BTicino - Axolute | `HD4653M2` | Established identity | canonical commercial record `1553`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `AUTOMATISME.pdf` | MyHOME automation guide | historical publisher guide | Soft Touch / 4653 family sections; printed page unresolved / 1-based PDF page unresolved | [Archived PDF](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |

The printed and 1-based PDF page locators remain unresolved and are retained explicitly as an evidence gap.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | Publisher automation documentation |
| SCS nominal supply | `27 Vdc` | Publisher data |
| SCS operating range | `18..27 Vdc` | Publisher data |
| Maximum current draw | `18 mA` | Publisher data |
| Operating temperature | `5..35 °C` | Publisher data |
| User interface | capacitive Soft Touch surface | Publisher automation documentation |
| LED indication | intensity adjustable | Publisher automation documentation |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `12` | Canonical catalogue |
| Technical item description | Soft touch control | Canonical catalogue |
| Item family | `1` - Control | Canonical catalogue |
| Main system | `1` - lighting_automation; `modobj` `8` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `149` | `-1` | `-1` | `-1` | `2` | not stated | wildcard applicability |

Firmware `149` is wildcard `-1.-1.-1` and declares two Modules.

## Module, Object, and Virgin Object model

### Firmware Object relations

| Firmware | Relation | Object | Key | Description |
| ---: | ---: | ---: | ---: | --- |
| `149` | `382` | `410` | `410` | Light control |
| `149` | `383` | `411` | `411` | Automation control |
| `149` | `384` | `412` | `412` | Lock/unlock actuator control |
| `149` | `385` | `413` | `413` | Scenario module control |
| `149` | `386` | `414` | `414` | Scheduled scenario |
| `149` | `387` | `415` | `415` | Scenario PLUS Lighting Management |
| `149` | `388` | `416` | `416` | Scheduled scenario PLUS |
| `149` | `389` | `418` | `418` | Open lock control |
| `149` | `390` | `419` | `419` | Sound diffusion control |
| `149` | `391` | `427` | `427` | Floor call control |
| `149` | `392` | `426` | `426` | Staircase light control |
| `149` | `393` | `480` | `130` | User interface settings |

### Slot applicability

| Slot row | Slot | Object | Relationship | Description |
| ---: | ---: | ---: | --- | --- |
| `563` | `1` | `410` | fixed | Light control |
| `564` | `1` | `411` | candidate / non-fixed | Automation control |
| `565` | `1` | `412` | candidate / non-fixed | Lock/unlock actuator control |
| `566` | `1` | `413` | candidate / non-fixed | Scenario module control |
| `567` | `1` | `414` | candidate / non-fixed | Scheduled scenario |
| `568` | `1` | `415` | candidate / non-fixed | Scenario PLUS Lighting Management |
| `569` | `1` | `416` | candidate / non-fixed | Scheduled scenario PLUS |
| `570` | `1` | `418` | candidate / non-fixed | Open lock control |
| `571` | `1` | `419` | candidate / non-fixed | Sound diffusion control |
| `572` | `1` | `427` | candidate / non-fixed | Floor call control |
| `573` | `1` | `426` | candidate / non-fixed | Staircase light control |
| `574` | `2` | `480` | fixed | User interface settings |

### Virgin Object reachability

| Firmware | Relation | Virgin Object | Key | Description | Associated Objects | Slot rows |
| ---: | ---: | ---: | ---: | --- | --- | --- |
| `149` | `23` | `521` | `521` | Soft-Touch command virgin | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `489` | `1` |

Slot `1` is the configurable command surface. Direct candidates are Objects `410`, `411`, `412`, `413`, `414`, `415`, `416`, `418`, `419`, `426`, and `427`. Virgin Object `521`, Soft-Touch command virgin, additionally permits AUX `417`, cyclic autoswitch `421`, and Open-lock-on-session `462`. Slot `2` is fixed Object `130`, User interface settings. It is not a second command channel.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `149` | `1` | `1` | Virtual Configuration |
| `149` | `2` | `2` | Advanced Configuration |
| `149` | `3` | `0` | Physical configuration |

Physical configuration, Virtual Configuration and Advanced Configuration.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | MyHOME Suite / catalogue identity field - not a physical configurator |
| `A` | `0..9` / `GEN` / `GR` / `AMB` / `AUX` | `0` | area / environment configurator |
| `PL` | `0..9` | `0` | light-point configurator |
| `M` | `0..9` / `CEN` / `OFF` / `ON` / `PUL` | `0` | operating / function mode |
| `M2` | `0..9` | `0` | channel 2 operating mode |
| `SPE` | `0` / `1` / `2` / `3` / `4` / `6` / `7` / `8` / `9` | `0` | special-function selector |
| `INT` | `0` / `1` / `OFF` | `0` | interface-function selector |

These are the Soft Touch device configurators. Their values select among the candidate control Objects; the much larger reusable Object schemas are summarized separately rather than flattened into this table.

## Object configuration surfaces

### Object `410` - Light control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `A_R`, `PL_R` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `TYPE_CONTACT` | operating mode and behavior selectors |
| Timing and levels | `HOURS`, `MINUTES`, `SECONDS`, `LEVEL`, `START_S`, `STOP_S`, `DIMMING_S`, `T_TIME` | timers, delays, levels and transition parameters |
| Object-specific | `INST_LEV`, `DEST_LEV` | additional reusable fields defined by this Object |

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`.

### Object `411` - Automation control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `A_R`, `PL_R` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `TYPE_CONTACT` | operating mode and behavior selectors |
| Object-specific | `INST_LEV`, `DEST_LEV` | additional reusable fields defined by this Object |

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`. The catalogue relation restricts `M`: UP mono+bistable control (`4`), DOWN mono+bistable control (`5`).

### Object `412` - Lock/unlock actuator control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | Disable / Enable | `1` | Modality |
| `ADDR_TYPE` | point-to-point / area / group / general | `0` | Addressing type |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | private riser / local bus `1..15` / standard | `16` | Installation level |
| `DEST_LEV` | private riser / local bus `1..15` / all systems | `0` | Destination level |
| `TYPE_CONTACT` | Normally open / Normally closed | `0` | Contact type |

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`.

### Object `413` - Scenario module control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | Scenario activation and modification / Scenario activation | `0` | Modality |
| `APL` | `A`: `0..10`; `PL`: `0..15` (catalogue-composed address) | `0` | Scenario module address |
| `INST_LEV` | private riser / local bus `1..15` / standard | `16` | Installation level |
| `DEST_LEV` | private riser / local bus `1..15` / all systems | `0` | Destination level |
| `TYPE_CONTACT` | Normally open / Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | none / catalogue delay scale from seconds to minutes | `0` | Activation delay of scenario number |

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`.

### Object `414` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `CEN_BUTT_1` | `0..31` | `1` | Button |
| `MODE` | Press/release only / Press/hold/release | `0` | Modality |
| `TYPE_CONTACT` | Normally open / Normally closed | `0` | Contact type |

**Firmware relationship.** The catalogue relation explicitly exposes `MODE`, `TYPE_CONTACT`.

### Object `415` - Scenario PLUS Lighting Management

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | `ON` / `OFF` / `ON` with regulation / `OFF` with regulation | `0` | Modality |
| `PPT_SCE_1` | `0..255` | `1` | Upper button scenario |
| `TYPE_OF_REGULATION` | Regulate all / Lights only / Shutters only / Stereo amplifiers only | `0` | Regulation type |
| `TYPE_CONTACT` | Normally open / Normally closed | `0` | Contact type |
| `DEL_BUTTON_1` | none / catalogue delay scale from seconds to minutes | `0` | Activation delay for upper button |

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`, `M`, `TYPE_OF_REGULATION`.

### Object `416` - Scheduled scenario PLUS

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Button |
| `MODE` | Press/release only / Press/hold/release | `0` | Modality |
| `TYPE_CONTACT` | Normally open / Normally closed | `0` | Contact type |

**Firmware relationship.** The catalogue relation explicitly exposes `MODE`, `TYPE_CONTACT`.

### Object `418` - Open lock control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | Same level / Riser / Building / Backbone | `0` | Level |

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

### Object `419` - Sound diffusion control

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ADDR_TYPE`, `A`, `PF` | target, group, installation-level or network addressing |
| Mode and behavior | `M`, `TYPE_CONTACT`, `IS_FOLLOW_ME` | operating mode and behavior selectors |
| Object-specific | `SOURCE`, `SUB_SOURCE`, `CHANNEL` | additional reusable fields defined by this Object |

**Firmware relationship.** The catalogue relation explicitly exposes `TYPE_CONTACT`, `SUB_SOURCE`, `CHANNEL`.

### Object `427` - Floor call control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | Point to point / General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEGMENT` | The same / Riser / Building / Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input AUX channel |

**Firmware relationship.** The catalogue relation explicitly exposes `IN_AUX_CHANNEL`, `SEGMENT`. The catalogue relation restricts `TO_ALL`: General (`1`).

### Object `426` - Staircase light control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEG_LEV` | Same / Riser / Building / Backbone | `0` | Segment |

**Firmware relationship.** The catalogue relation explicitly exposes `SEG_LEV`. The catalogue relation restricts `N1` to `100..255`.

### Object `480` - User interface settings

| Surface | Fields | Meaning |
| --- | --- | --- |
| Timing and levels | `LED_LEVEL`, `LED_FADE`, `BACKLIGHT_INTENSITY_STANDBY_LEVEL`, `SINGLE_LED_INTENSITY_STANDBY_LEVEL`, `BACKLIGHT_DELAY` | timers, delays, levels and transition parameters |
| Scenario / UI | `STATE_OF_UNUSED_BUTTON`, `STATE_UPDATE`, `PROXIMITY_ENABLE`, `SIGNBOARD` | scenario assignment and user-interface behavior |

**Firmware relationship.** The catalogue relation explicitly exposes `STATE_OF_UNUSED_BUTTON`, `BACKLIGHT_INTENSITY_STANDBY_LEVEL`, `PROXIMITY_ENABLE`, `SIGNBOARD`, `SINGLE_LED_INTENSITY_STANDBY_LEVEL`, `BACKLIGHT_DELAY`.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

## Conditions, filters, and conversions

| Surface | Catalogue rows | Interpretation |
| --- | ---: | --- |
| Slot conditions | `0` | Device/Firmware topology conditions |
| Object/Firmware filters | `26` | Conditional Object configuration exposure |
| Referenced conversion rules | `0` | None |

### Object/Firmware filters

| Object | Filter ID | Field | Note | Whole range | Filter ranges |
| ---: | ---: | --- | --- | --- | --- |
| `410` | `311` | `TYPE_CONTACT` | Contact type | `1` | - |
| `411` | `312` | `TYPE_CONTACT` | Contact type | `1` | - |
| `411` | `313` | `M` | Modality | `0` | `4` - UP mono+bistable control<br>`5` - DOWN mono+bistable control |
| `412` | `314` | `TYPE_CONTACT` | Contact type | `1` | - |
| `413` | `315` | `TYPE_CONTACT` | Contact type | `1` | - |
| `414` | `316` | `MODE` | Mode for CEN command | `1` | - |
| `414` | `317` | `TYPE_CONTACT` | Contact type | `1` | - |
| `415` | `318` | `TYPE_CONTACT` | Contact type | `1` | - |
| `415` | `319` | `M` | Mode (ON/OFF regulation) | `1` | - |
| `415` | `320` | `TYPE_OF_REGULATION` | REG_TYPE | `1` | - |
| `416` | `321` | `MODE` | Mode for CEN command | `1` | - |
| `416` | `322` | `TYPE_CONTACT` | Contact type | `1` | - |
| `419` | `323` | `TYPE_CONTACT` | Contact type | `1` | - |
| `419` | `324` | `SUB_SOURCE` | `SUB_SOURCE` | `1` | - |
| `419` | `325` | `CHANNEL` | Channel (BB-Stereo) | `1` | - |
| `426` | `329` | `SEG_LEV` | Segment | `1` | - |
| `426` | `4101` | `N1` | Internal unit address | `0` | `100`<br>`101`<br>`102`<br>`103`<br>`104`<br>`105`<br>`106`<br>`107`<br>`108`<br>`109`<br>`110`<br>`111`<br>`112`<br>`113`<br>`114`<br>`115`<br>`116`<br>`117`<br>`118`<br>`119`<br>`120`<br>`121`<br>`122`<br>`123`<br>`124`<br>`125`<br>`126`<br>`127`<br>`128`<br>`129`<br>`130`<br>`131`<br>`132`<br>`133`<br>`134`<br>`135`<br>`136`<br>`137`<br>`138`<br>`139`<br>`140`<br>`141`<br>`142`<br>`143`<br>`144`<br>`145`<br>`146`<br>`147`<br>`148`<br>`149`<br>`150`<br>`151`<br>`152`<br>`153`<br>`154`<br>`155`<br>`156`<br>`157`<br>`158`<br>`159`<br>`160`<br>`161`<br>`162`<br>`163`<br>`164`<br>`165`<br>`166`<br>`167`<br>`168`<br>`169`<br>`170`<br>`171`<br>`172`<br>`173`<br>`174`<br>`175`<br>`176`<br>`177`<br>`178`<br>`179`<br>`180`<br>`181`<br>`182`<br>`183`<br>`184`<br>`185`<br>`186`<br>`187`<br>`188`<br>`189`<br>`190`<br>`191`<br>`192`<br>`193`<br>`194`<br>`195`<br>`196`<br>`197`<br>`198`<br>`199`<br>`200`<br>`201`<br>`202`<br>`203`<br>`204`<br>`205`<br>`206`<br>`207`<br>`208`<br>`209`<br>`210`<br>`211`<br>`212`<br>`213`<br>`214`<br>`215`<br>`216`<br>`217`<br>`218`<br>`219`<br>`220`<br>`221`<br>`222`<br>`223`<br>`224`<br>`225`<br>`226`<br>`227`<br>`228`<br>`229`<br>`230`<br>`231`<br>`232`<br>`233`<br>`234`<br>`235`<br>`236`<br>`237`<br>`238`<br>`239`<br>`240`<br>`241`<br>`242`<br>`243`<br>`244`<br>`245`<br>`246`<br>`247`<br>`248`<br>`249`<br>`250`<br>`251`<br>`252`<br>`253`<br>`254`<br>`255` |
| `427` | `326` | `IN_AUX_CHANNEL` | Input AUX channel | `1` | - |
| `427` | `327` | `TO_ALL` | Type of call | `0` | `1` - General |
| `427` | `1900` | `SEGMENT` | Segment | `1` | - |
| `480` | `330` | `STATE_OF_UNUSED_BUTTON` | State of unused button | `1` | - |
| `480` | `3110` | `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | Backlight intensity stand by level | `1` | - |
| `480` | `3117` | `PROXIMITY_ENABLE` | Proximity Activation | `1` | - |
| `480` | `3124` | `SIGNBOARD` | Signboard activation type | `1` | - |
| `480` | `3132` | `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | when `BACKLIGHT_INTENSITY_STANDBY_LEVEL` is `OFF`, only one LED can be used for standby. | `1` | - |
| `480` | `3155` | `BACKLIGHT_DELAY` | Delay time (seconds) | `1` | - |

Generic condition/conversion evaluation remains canonical in [Catalogue Resolution](../../internals/catalogue-resolution.md); these tables preserve this Device's exact applicability records.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 8` and the Soft Touch commercial family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | record installed firmware rather than assuming wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | resolve the configurable command Object plus the separate UI-settings Module | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the address of the resolved command role | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `A`, `PL`, `M`, `M2`, `SPE`, `INT` plus Device-specific UI/backlight settings | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on configuration, the control participates in lighting, automation, scenarios, sound diffusion and access/door-entry command functions.

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained.

## Programming

Treat the Device as one configurable command surface plus one UI-settings Module, not two independent commands.

## Source reconciliation

Official documentation establishes touch operation, adjustable LED intensity, actuator/scenario use and sound-system ON/OFF/volume use. The database expands the same command surface to the full Virgin-Object candidate set and explicitly separates UI settings into slot `2`.

## Evidence limits and open work

- Archive a dedicated Soft Touch technical sheet with explicit `HD4653M2` coverage.
- Publish the exact physical `M/M2/SPE/INT` function matrix.
- Hardware-corroborate active Object and UI-settings behavior.
- Pin exact printed and 1-based PDF page locations for each applicable multi-product guide citation.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [AUTOMATISME.pdf](../../sources/devices/documents/device-doc-automation-guide/AUTOMATISME.pdf)
