# Four-zone touch multifunction control

## Summary


| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0009` | Project identity |
| Technical description | Two-module capacitive four-zone multifunction SCS control | Catalogue + official technical sheet |
| Catalogue item | `1376` - “Touch control multifunction” | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `17` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `159` | Implementation evidence |
| Declared Modules | `5` | Implementation evidence |
| Categories | Command, Multifunction, Lighting, Automation, Scenario, Audio / Video | Capability model |

The Device has four capacitive command zones plus a fifth fixed **User interface settings** Module. Its command Modules can be configured across lighting, automation, scenarios, AUX, sound-system, and video-door-entry-related roles.

## Commercial identities


The canonical catalogue contains 15 commercial records for item `1376`.

| Brand / line | References | Evidence status |
| --- | --- | --- |
| Legrand Arteor | `573904`, `573905`, `573906`, `573907` | directly documented by `LG00045-b-UK` and the MyHOME catalogue |
| Legrand Arteor | `574089`, `574589` | shared technical item; individual product-document review pending |
| Legrand Céliane | `067243`, `067244`, `067245` | catalogue + MyHOME Server compatibility documentation; minimum compatible production batch `13W05` |
| Legrand Céliane | `067273`, `067274`, `067275`, `067293`, `067294`, `067295` | shared technical item; individual product-document review pending |

The older technical sheet directly names only the four Arteor references. Shared item membership establishes a common implementation capability core, not perfect physical/package synonymy.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LG00045-b-UK` | Technical sheet | not stated in retained row | `573904..573907` | [Archived PDF](https://archive.openwebnet-ha.org/sha256/9e/18/9e18cf6694d6fcb44ee1c0964175c88d7a9f1918de4e4c4ac8c2d969b401d422.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LG00045_b_UK.pdf) |
| `U3300B` | Instruction sheet | not stated in retained row | `573904..573907` family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/bf/19/bf19dc9f2f7d44ed0714fc43e734b58428aa5320cfd30c9a8822e4530f63b9cd.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/U3300B.pdf) |
| MyHOME residential automation catalogue | Product catalogue | not stated in retained row | all `573904..573907` references on printed p. 19 / PDF p. 19; `573904` / `573905` also appear in the installation principle on printed p. 31 / PDF p. 31 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/BR%20MyHOME%20HPML0714.pdf) |
| `ST-00001031-EN` | Compatibility table | not stated in retained row | `067243..067245` occur on printed p. 2 / PDF p. 2 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/14/97/14971697bfbdbb33587b5724c7b38ac2aa6977e05e404556941291cafa589ad7.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001031-EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 flush-mounted modules | Publisher documentation cited in this section |
| User controls | 4 capacitive touch zones | Publisher documentation cited in this section |
| Feedback | two light-blue LEDs per key zone, with adjustable intensity behavior | Publisher documentation cited in this section |
| SCS supply | `18..27 Vdc` | Publisher documentation cited in this section |
| Maximum consumption | `25 mA` at maximum LED level; `20 mA` medium; `17 mA` minimum | Publisher documentation cited in this section |
| Operating temperature | `0..40 °C` | Publisher documentation cited in this section |
| Depth | `18.3 mm` | Publisher documentation cited in this section |
| Physical labels | `A`, `PL`, `M`, `SPE`; rear programming/LED-intensity button `P` | Publisher documentation cited in this section |

For `573904..573907`, `LG00045-b-UK` establishes:


The programming pushbutton `P` is a physical user/programming control, not simply another firmware configuration value.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1376` | Canonical catalogue |
| Item model / `modobj` | `17` | Canonical catalogue / retained definition |
| Main system | Lighting / Automation | Canonical catalogue / retained definition |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `159` | `-1` | `-1` | `-1` | `5` | catalogue default | wildcard / unspecified applicability |

Catalogue firmware applicability is distinct from an observed installed firmware fingerprint.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Object | Description | Relationship |
| --- | --- | --- | --- |
| `159` | `480` | User interface settings | catalogue firmware/Object relation |
| `159` | `410` | Light control | catalogue firmware/Object relation |
| `159` | `411` | Automation control | catalogue firmware/Object relation |
| `159` | `412` | Lock/unlock actuator control | catalogue firmware/Object relation |
| `159` | `413` | Scenario module control | catalogue firmware/Object relation |
| `159` | `414` | Scheduled scenario | catalogue firmware/Object relation |
| `159` | `415` | Scenario PLUS Lighting Management | catalogue firmware/Object relation |
| `159` | `416` | Scheduled scenario PLUS | catalogue firmware/Object relation |
| `159` | `417` | AUX control | catalogue firmware/Object relation |
| `159` | `418` | Open lock control | catalogue firmware/Object relation |
| `159` | `419` | Sound diffusion control | catalogue firmware/Object relation |
| `159` | `421` | Cyclic autoswitch control | catalogue firmware/Object relation |
| `159` | `426` | Staircase light control | catalogue firmware/Object relation |
| `159` | `427` | Floor call control | catalogue firmware/Object relation |
| `159` | `489` | Open lock command on session | catalogue firmware/Object relation |

### Virgin Objects

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `159` | `521` | catalogue candidate/template association |

### Reconciled topology notes


### Fixed UI Module

Slot `5` is fixed to Object `130`, **User interface settings**.

| Parameter | Domain |
| --- | --- |
| `STATE_OF_UNUSED_BUTTON` | ON / OFF |
| `STATE_UPDATE` | No / Yes |
| `LED_LEVEL` | `0..10`, default `6` |
| `LED_FADE` | `0..10`, default `5` |
| `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | OFF or levels `1..10` |
| `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | OFF or levels `1..10` |
| `BACKLIGHT_DELAY` | `0..255 s`, default `15` |
| `PROXIMITY_ENABLE` | Disable / Enable |
| `SIGNBOARD` | Off / Fixed / Chase |

The published sheet independently documents three LED intensity pairings for active/idle states: 100%/60%, 75%/30%, and 45%/off.

### Command Modules

Slots `1..4` use Virgin Object `521`, **Soft-Touch command virgin**, and can select:

| Object | Role |
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
| `462` | Open lock command on session |

Light control `410` is the designated Object on all four command slots. The canonical firmware has **no `AS_SLOT_CONDITION` rows** for these slots, so the Device page must not invent a physical-condition-to-Object mapping from the mere Object list.

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `159` | Catalogue configuration route(s) described in retained notes | retained Device-specific configuration modality |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `159` | `AID` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `159` | `A` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `159` | `PL` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `159` | `M` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |
| `159` | `SET` | catalogue-defined; preserve legal values through canonical resolver | catalogue-scoped | Device/firmware configuration field |

### Published and reconciled details


The firmware-level fields are:

| Field | Stored domain | Evidence |
| --- | --- | --- |
| `AID` | Device identity field | Implementation evidence |
| `A` | `0..9`, `GEN`, `GR`, `AMB` | Implementation evidence |
| `PL` | `0..9` | Implementation evidence |
| `M` | `0,1,2,3,5,6,O/I,UP/DOWN,UP/DOWN monostable,CEN` | Implementation evidence |
| `SET` | `0..7` | Implementation evidence |

### Database/document mapping boundary

The physical technical sheet labels the configurator housing `A / PL / M / SPE` and separately identifies programming button `P`. The database instead stores `A / PL / M / SET`.

No equivalence between database `SET` and physical `SPE` is asserted here without further implementation evidence. Preserve both source models.

## Object configuration surfaces

### Object `410` - Light control

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
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `HOURS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MINUTES` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SECONDS` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LEVEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `START_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `STOP_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DIMMING_S` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `T_TIME` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `411` - Automation control

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
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `412` - Lock/unlock actuator control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `G` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `413` - Scenario module control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `APL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `INST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEST_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SCE_BUTT_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEL_BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `414` - Scheduled scenario

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `CEN_BUTT_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MODE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `415` - Scenario PLUS Lighting Management

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PPT_SCE_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_OF_REGULATION` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `DEL_BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `416` - Scheduled scenario PLUS

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PPT_CEN_HIG` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BUTTON_1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `MODE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `417` - AUX control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `OUT_AUX_CH` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `418` - Open lock control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `P` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SEG_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `419` - Sound diffusion control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `M` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `ADDR_TYPE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `A` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PF` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `TYPE_CONTACT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IS_FOLLOW_ME` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SOURCE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SUB_SOURCE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `421` - Cyclic autoswitch control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `P` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SEG_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `426` - Staircase light control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `N1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `N2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SEG_LEV` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `427` - Floor call control

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `N1` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `N2` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SEGMENT` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `IN_AUX_CHANNEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `480` - User interface settings

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `STATE_OF_UNUSED_BUTTON` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `STATE_UPDATE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LED_LEVEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `LED_FADE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BACKLIGHT_INTENSITY_STANDBY_LEVEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SINGLE_LED_INTENSITY_STANDBY_LEVEL` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `BACKLIGHT_DELAY` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `PROXIMITY_ENABLE` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |
| `SIGNBOARD` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Object `489` - Open lock command on session

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `P` | catalogue-defined; apply Device relation filters | catalogue-scoped | reusable Object configuration field |

### Reconciled Object notes


The command Objects preserve their complete reusable parameter models in the canonical database. Principal surfaces include:

| Object family | Configuration surface |
| --- | --- |
| Light control `410` | 45 command-mode values; point/area/group/general address; installation/destination level; reference address; timed/dimming values |
| Automation control `411` | six UP/DOWN bistable/monostable variants; point/area/group/general addressing; installation/destination level |
| Lock/unlock `412` | enable/disable plus addressed target |
| Scenario module `413` | activation/edit mode, encoded A/PL, installation/destination level, scenario button `1..16`, delay table |
| Scheduled scenario `414` | A/PL, CEN button `0..31`, press/release mode |
| PLUS scenario `415/416` | scenario identifiers, regulation type, delays and button fields |
| AUX `417` | command mode plus AUX output channel `1..15` |
| Door-entry-related `418/421/426/427/462` | entrance/internal-unit identifiers, segment level, point/general selection as applicable |
| Sound diffusion `419` | ON/OFF/volume/track/source modes, audio addressing, follow-me/source/channel |

## Conditions, filters, and conversions

### Relation filters

| Scope | Filter IDs | Interpretation |
| --- | --- | --- |
| Device/Object relations | `1057`, `1061`, `1065`, `1069`, `1076`, `1077`, `1081`, `1088`, `1089`, `1093`, `1097`, `1101`, `1904`, `3114`, `3121`, `3128`, `3136`, `3159`, `4107` | apply before exposing reusable Object values |

### Slot conditions and conversions

| Scope | Condition IDs | Conversion treatment |
| --- | --- | --- |
| Device slots | none | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1376` and the installed model | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware without treating wildcard sentinels as literal installed values | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `480`, `489`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions, and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

### Existing Device-specific diagnostic notes


| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 17`, brand/line and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate four command Objects plus the UI-settings Module | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine configured functional addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability


The technical sheet documents several physical behavior families:

- self-learning mode, cyclic or non-cyclic, where individual key functions can be learnt;
- scenario-module mode for recalling/programming scenarios;
- direct/swivelling lighting or shutter control of consecutive targets;
- CEN mode for use with a scenario programmer;
- sound-system mode when `SPE=1`;
- learned functions spanning lighting, automation, locking, staircase light, door release, floor call, camera cycling, sound diffusion, and AUX control.

It also specifies a two-minute self-calibration period after installation.

These published functions strongly corroborate the breadth of the catalogue Object set, but do not establish a one-to-one mapping between every physical mode and every database Object.

## Observed behavior and corroboration

No additional publishable runtime observation is asserted beyond observations explicitly retained elsewhere on this page.

## Programming

Programming must validate firmware applicability, active Module/Object topology, relation filters, and Device-specific configuration constraints.

## Source reconciliation


The archived touch-control sources establish user/programming behavior in addition to the catalogue Object set:

- the four capacitive zones can be temporarily disabled for cleaning, with the product restoring normal touch operation after the documented cleaning interval;
- self-learning can operate in cyclic and non-cyclic forms and includes explicit learn/delete procedures rather than being a generic “scenario” capability;
- scenario-module and CEN/programmed-scenario operation have distinct product programming workflows and button/address interpretations;
- sound-system operation assigns the touch zones to product-specific audio controls rather than treating them as ordinary lighting keys;
- front LED behavior, standby/active intensity and programming feedback are product functions of the fixed UI settings Module;
- after installation the Device performs an automatic calibration interval during which touch behavior must not be treated as normal steady-state operation.

These behaviors do not resolve the implementation `SPE` versus `SET` mapping; that source-model boundary remains explicit.

## Evidence limits and open work


- Locate direct product sheets for the Céliane `067273..067295` variants and Arteor `574089/574589`.
- Determine the exact relationship between physical `SPE`, database `SET`, and Object selection.
- Add sanitized hardware fingerprints from at least one Arteor and one Céliane variant.
- Corroborate the fifth UI-settings Module and four command Modules through `DIMENSION 30`.
- Preserve production-batch constraints such as the documented `13W05` minimum for `067243..067245`.

## Sources


- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
- [Programming](../../programming/)
