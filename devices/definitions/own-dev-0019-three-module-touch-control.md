# Three-module touch control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0019` | Project identity |
| Technical description | Six-button capacitive multifunction command with configurable button roles | Catalogue + official technical sheet |
| Catalogue item | `1190` - Touch control | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `27` | Implementation evidence |
| Firmware definition | wildcard `-1.-1` | Implementation evidence |
| Declared Modules | `7` | Implementation evidence |
| Configuration modes | Advanced, Physical, Virtual | Implementation evidence |
| Direct / candidate Objects | `12` / `15` | Implementation evidence |
| Virgin Object | Soft-Touch command virgin (`521`) | Implementation evidence |
| Categories | Commands, Multifunction, User Interface, Scenarios | Product and capability model |

This definition covers the three-module touch-control cluster, not the four-module sibling. The product has six capacitive command zones plus a separate user-interface-settings slot. Each command zone can take one of a broad set of command roles; the catalogue models that flexibility through direct reusable Objects plus a Soft-Touch Virgin Object candidate set.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS4657M3` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| BTicino - Axolute | `HD4657M3` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| Legrand - Arteor | `573912` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| Legrand - Arteor | `573913` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| Legrand - Arteor | `574091` | Shared technical item | Implementation evidence; direct sheet correlation pending |
| Legrand - Arteor | `574591` | Shared technical item | Implementation evidence; direct sheet correlation pending |
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00110_f_EN` | Technical sheet | revision/date not yet pinned | 4657M3/M4 and Arteor touch-control family | [Archived original](../../sources/devices/documents/device-doc-touch-control-mq00110-f-en/MQ00110_f_EN.pdf) | publisher source not currently retained |
| MyHOME catalogue `HPML0714` | Product catalogue | revision/date not yet pinned | `573912` / `573913` occur on printed pp. 16, 19 / PDF pp. 16, 19 | [Archived MyHOME catalogue](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf) | publisher source not currently retained |

The technical sheet distinguishes the three-module version by its six capacitive buttons. It documents physical and MyHOME_Suite configuration and a multifunction command set spanning lighting, automation, locking, scenarios, video-door-entry and sound functions.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 3-module family | `MQ00110_f_EN` |
| User controls | 6 capacitive buttons | `MQ00110_f_EN` |
| Indication | blue indication | `MQ00110_f_EN` |
| SCS current by commercial variant | BTicino variants are specified below the Arteor `573912`/`573913` variants; retain revision/variant scope | `MQ00110_f_EN` |

The current source set establishes a commercial-variant electrical difference without a single shared current figure. Preserve that distinction rather than inventing a universal value.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1190` | Implementation evidence |
| Main system | lighting_automation / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `27` | Implementation evidence |
| Family | `1` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `154` | `-1` | `-1` | not specified | `7` | not stated | wildcard applicability |

Wildcard values are catalogue applicability sentinels, not claims about an installed firmware version.

## Module, Object, and Virgin Object model

Direct catalogue Objects include:

| Object | Role | Slots |
| ---: | --- | --- |
| `410` | Light control | `1..6` |
| `411` | Automation control | `1..6` |
| `412` | Lock/unlock actuator control | `1..6` |
| `413` | Scenario module control | `1..6` |
| `414` | Scheduled scenario | `1..6` |
| `415` | Scenario PLUS Lighting Management | `1..6` |
| `416` | Scheduled scenario PLUS | `1..6` |
| `418` | Open lock control | `1..6` |
| `419` | Sound diffusion control | `1..6` |
| `426` | Staircase light control | `1..6` |
| `427` | Floor call control | `1..6` |
| `480` | User interface settings | `7` |

Virgin Object `521`, Soft-Touch command virgin, allows these command roles:

| Object | Candidate role |
| ---: | --- |
| `410` | Light control |
| `411` | Automation control |
| `412` | Lock/unlock actuator control |
| `413` | Scenario module control |
| `414` | Scheduled scenario |
| `415` | Scenario PLUS Lighting Management |
| `416` | Scheduled scenario PLUS |
| `417` | AUX control |
| `418` | Open lock control |
| `419` | Sound diffusion control |
| `421` | Cyclic autoswitch control |
| `426` | Staircase light control |
| `427` | Floor call control |
| `489` | Open lock command on session |

Combining the direct set with Virgin-only roles yields 15 distinct candidate Objects. The catalogue contains empty slot-condition records on some direct Light-control and Floor-call rows; because the condition text is empty, this definition treats them as source artifacts rather than as hidden semantic predicates.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | `MQ00110_f_EN` + implementation evidence |
| Virtual Configuration | `MQ00110_f_EN` + implementation evidence |
| Advanced Configuration | implementation evidence |

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | Device identity |
| `A` | `0..9` plus `GEN` / `GR` / `AMB` forms | - | environment / area selector |
| `PL` | physical light-point domain | - | light point |
| `M` | `0`, `1`, `3`, `4`, `6`, `O/I`, `SU_GIU`, `SU_GIU_M`, `CEN` | - | physical mode selector |
| `SET` | `0..7` | - | user-interface settings configurator |

The physical sheet and catalogue agree that the Device can be configured physically or through software. Software configuration should preserve the richer reusable Object model rather than reducing every button to the physical `A` / `PL` / `M` shorthand.

## Object configuration surfaces

The following subsections account for the complete reusable Object field surface present in the canonical catalogue. They preserve field identity without reproducing database serialization. Detailed Device-specific interpretation follows where available.

### Object `410` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M`, `A_R`, `PL_R`, `LEVEL`, `START_S`, `STOP_S`, `DIMMING_S` | Mode (MODE+ON/OFF); 0= no referent; Only for `MOD=129`, 131, 133, 135, 136, 137, 138; Only for `MOD=129`, 131 |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `INST_LEV`, `DEST_LEV` | Address (2, range `01..175`) Area (2, range `00..10`) Group (2, range `01..255`); Area; Light point; Group; Installation level; Destination level |
| Mode / behavior | `TYPE_CONTACT` | Contact type |
| Timing | `HOURS`, `MINUTES`, `SECONDS`, `T_TIME` | Only for `MOD=128`; Only for `MOD=1` |

### Object `411` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M`, `A_R`, `PL_R` | mode (UP/DOWN); 0= no referent |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `INST_LEV`, `DEST_LEV` | Address (2, range `01..175`) Area (2, range `00..10`) Group (2, range `01..255`); Area; Light point; Group; Installation level; Destination level |
| Mode / behavior | `TYPE_CONTACT` | Contact type |

### Object `412` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M` | mode (D/E) |
| Addressing | `ADDR_TYPE`, `A`, `PL`, `G`, `INST_LEV`, `DEST_LEV` | Address (2, range `01..175`) Area (2, range `00..10`) Group (2, range `01..255`); Area; Light point; Group; Installation level; Destination level |
| Mode / behavior | `TYPE_CONTACT` | Contact type |

### Object `413` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M` | Modality |
| Addressing | `APL`, `INST_LEV`, `DEST_LEV` | Scenario module address; Installation level; Destination level (`0..15`) |
| Mode / behavior | `TYPE_CONTACT` | Contact type |
| Scenario / button | `SCE_BUTT_1`, `DEL_BUTTON_1` | Scenario number; Activation delay of scenario number |

### Object `414` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL` | Area; Light point |
| Scenario / button | `CEN_BUTT_1` | Button |
| Mode / behavior | `MODE`, `TYPE_CONTACT` | Mode (Lighting management); Contact type |

### Object `415` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M` | Mode (ON/OFF regulation) |
| Scenario / button | `PPT_SCE_1`, `DEL_BUTTON_1` | Upper button scenario; Activation delay for upper button |
| Sensing / regulation | `TYPE_OF_REGULATION` | Regulation type |
| Mode / behavior | `TYPE_CONTACT` | Contact type |

### Object `416` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Scenario / button | `PPT_CEN_LOW`, `PPT_CEN_HIG`, `BUTTON_1` | Scheduled scenario PLUS number; Button |
| Mode / behavior | `MODE`, `TYPE_CONTACT` | Mode (Lighting management); Contact type |

### Object `418` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `P` | External unit address |
| Object-specific | `SEG_LEV` | Level |

### Object `419` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M` | Mode (VOL,ON_OFF) |
| Addressing | `ADDR_TYPE`, `A`, `PF` | Addressing type; Area; Audio point |
| Mode / behavior | `TYPE_CONTACT` | Contact type |
| Audio / media | `IS_FOLLOW_ME`, `SOURCE`, `SUB_SOURCE`, `CHANNEL` | Follow me; Source; Sub source; Channel (BB-Stereo) |

### Object `426` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `N1`, `N2` | Internal unit address |
| Object-specific | `SEG_LEV` | Segment |

### Object `427` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `TO_ALL`, `SEGMENT` | Type of call; Segment |
| Addressing | `N1`, `N2` | Internal unit address |
| Audio / media | `IN_AUX_CHANNEL` | Input `AUX` channel |

### Object `480` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Scenario / button | `STATE_OF_UNUSED_BUTTON` | Default depends on device |
| Mode / behavior | `STATE_UPDATE` | Default depends on device |
| User interface | `LED_LEVEL`, `LED_FADE`, `BACKLIGHT_INTENSITY_STANDBY_LEVEL`, `SINGLE_LED_INTENSITY_STANDBY_LEVEL`, `PROXIMITY_ENABLE`, `SIGNBOARD` | Default, minimum level (0), maximum level (10) and distribution of intermediate levels depend on device; Backlight intensity stand by level; when BACKLIGHT_INTENSITY_STANDBY_LEVEL is OFF, only one led can be used for the standby.; Proximity Activation; Sign... |
| Timing | `BACKLIGHT_DELAY` | Time en second to light off the backlight |

### Additional Device-specific interpretation

The candidate roles expose different schemas:

| Role | Principal configuration fields |
| --- | --- |
| Light control | modality; addressing type; `A` / `PL` / `G`; installation/destination levels; reference actuator; contact type; optional timing, level and dimming parameters |
| Automation control | UP/DOWN modality; addressing; `A` / `PL` / `G`; installation/destination levels; reference actuator; contact type |
| Lock/unlock control | D/E modality; addressing; `A` / `PL` / `G`; installation/destination levels; contact type |
| Scenario module control | modality; scenario-module address; installation/destination levels; contact type; scenario number; activation delay |
| Scheduled scenario | `A` / `PL`; `CEN` button; Lighting Management mode; contact type |
| Scenario PLUS | ON/OFF regulation mode; scenario number; regulation type; contact type; delay |
| Scheduled scenario PLUS | low/high scenario number; button; Lighting Management mode; contact type |
| `AUX` control | cyclic/off/on/pulse/up/down family of modes; `AUX` channel; contact type |
| Open lock control | external-unit P; segment level |
| Sound diffusion control | VOL/ON_OFF; addressing type; `A` / `PF`; follow-me; source/sub-source; channel; contact type |
| Cyclic autoswitch | external-unit P; segment |
| Staircase light | internal-unit `N1` / `N2`; segment |
| Floor call | call type; `N1` / `N2`; segment; input `AUX` channel |
| Open lock on session | external-unit P |
| User interface settings | unused-button state; feedback update; LED level/fade; standby backlight; backlight delay; proximity enable; signboard behavior |

The Light-control address type explicitly supports address `01..175`, area `00..10` and group `01..255` in the reusable catalogue Object. Other role-specific ranges remain those of their canonical reusable Objects.

## Conditions, filters, and conversions

| Surface | Source state | Interpretation |
| --- | --- | --- |
| Direct Light-control rows | empty condition records occur | treat as source artifacts, not hidden predicates |
| Direct Floor-call rows | empty condition records occur | treat as source artifacts, not hidden predicates |
| Virgin Object `521` | permits additional candidate roles | candidate capability does not establish runtime selection |

### Catalogue filter references

| Filter | Object | Field | Source note |
| --- | --- | --- | --- |
| `738` | `410` | `TYPE_CONTACT` | catalogue filter |
| `749` | `411` | `TYPE_CONTACT` | Contact type |
| `756` | `412` | `TYPE_CONTACT` | Contact type |
| `762` | `413` | `TYPE_CONTACT` | Contact type |
| `773` | `414` | `TYPE_CONTACT` | Contact type |
| `774` | `414` | `MODE` | Mode for CEN command |
| `780` | `415` | `TYPE_CONTACT` | Contact type |
| `791` | `416` | `TYPE_CONTACT` | Contact type |
| `792` | `416` | `MODE` | Mode for CEN command |
| `808` | `419` | `TYPE_CONTACT` | Contact type |
| `809` | `419` | `CHANNEL` | Channel (BB-Stereo) |
| `810` | `419` | `SUB_SOURCE` | SUB_SOURCE |
| `822` | `426` | `SEG_LEV` | Segment |
| `843` | `427` | `DEST_LEV` | Destination level |
| `844` | `427` | `IN_AUX_CHANNEL` | Input AUX channel |
| `845` | `427` | `IN_AUX_CHANNEL` | Input AUX channel |
| `846` | `427` | `TO_ALL` | Type of call |
| `1903` | `427` | `SEGMENT` | Segment |
| `3113` | `480` | `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | Backlight intensity stand by level |
| `3120` | `480` | `PROXIMITY_ENABLE` | Proximity Activation |
| `3127` | `480` | `SIGNBOARD` | Signboard activation type |
| `3135` | `480` | `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | when BACKLIGHT_INTENSITY_STANDBY_LEVEL is OFF, only one led can be used for the standby. |
| `3158` | `480` | `BACKLIGHT_DELAY` | Delay time (seconds) |
| `4106` | `426` | `N1` | Internal unit address |

### Catalogue slot-condition references

| Condition | Slot | Object | Predicate | Conversion reference |
| --- | --- | --- | --- | --- |
| `4145` | `1` | `410` | empty source condition | `` |
| `4145` | `2` | `410` | empty source condition | `` |
| `4145` | `3` | `410` | empty source condition | `` |
| `4145` | `4` | `410` | empty source condition | `` |
| `4145` | `5` | `410` | empty source condition | `` |
| `4145` | `6` | `410` | empty source condition | `` |
| `4145` | `1` | `427` | empty source condition | `` |
| `4145` | `2` | `427` | empty source condition | `` |
| `4145` | `3` | `427` | empty source condition | `` |
| `4145` | `4` | `427` | empty source condition | `` |
| `4145` | `5` | `427` | empty source condition | `` |
| `4145` | `6` | `427` | empty source condition | `` |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify `modobj` 27 and product family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe concrete installed firmware despite wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate six command Modules plus UI settings where exposed | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect each configured command address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | identify selected candidate Object and its configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on selected Object, individual buttons can participate in lighting, automation, scenario, AUX, sound and video-door-entry functions. The official sheet corroborates this multifunction character. Generic `WHO` frame semantics remain canonical in Functional Protocol.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

Programming must preserve six independently configurable command positions plus the fixed UI-settings slot. Physical `A`/`PL`/`M` configuration and software-selected reusable Object roles are separate layers; self-learning/scenario workflows remain product behavior.

## Source reconciliation

`MQ00110_f_EN` has been reconciled into the six-command-slot plus UI-settings model:

- self-learning and cyclic self-learning have explicit product programming/deletion procedures and are not merely generic Object alternatives;
- F420/scenario and CEN/MH200N-style functions have product-specific button/address mappings;
- the touch UI supports Device-level LED/status behavior selected by `SET=0..7`, including different feedback/fade/standby arrangements;
- the product provides a temporary cleaning/command-inhibit behavior for the touch surface;
- after installation/power-up the Device performs an automatic calibration interval of roughly two minutes, during which commands/feedback must not be interpreted as normal steady-state behavior;
- installation/destination-level semantics remain part of the selected function family when the Device works across interfaces.

The empty catalogue condition rows remain source artifacts requiring runtime clarification, but the principal published touch-control behavior is now explicit on the Device page.

## Evidence limits and open work

- Obtain a sanitized fingerprint showing all six button slots plus UI slot `7`.
- Correlate `DIMENSION 30` Virgin-Object identifiers with software-selected roles on real hardware.
- Locate direct official documentation for `574091` and `574591`.
- Determine whether the empty condition 4145 rows have any runtime significance.
- Correlate wildcard catalogue applicability with observed firmware versions.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
