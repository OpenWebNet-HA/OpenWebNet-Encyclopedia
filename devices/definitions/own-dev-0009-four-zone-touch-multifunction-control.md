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
| Declared Modules | 5 | Implementation evidence |
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

| Document | Type | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- |
| `LG00045-b-UK` | Technical sheet | `573904..573907` | [Archived PDF](../../sources/devices/documents/device-doc-touch-multifunction-lg00045-b-uk/LG00045_b_UK.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/LG00045_b_UK.pdf) |
| `U3300B` | Instruction sheet | `573904..573907` family | [Archived PDF](../../sources/devices/documents/device-doc-touch-multifunction-u3300b/U3300B.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/U3300B.pdf) |
| MyHOME residential automation catalogue | Product catalogue | includes `573904..573907` | [Archived PDF](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/BR%20MyHOME%20HPML0714.pdf) |
| `ST-00001031-EN` | Compatibility table | includes `067243..067245` | [Archived PDF](../../sources/devices/documents/device-doc-myhomeserver1-compatible-st00001031-en/ST-00001031-EN.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00001031-EN.pdf) |

## Physical and user-interface characteristics

For `573904..573907`, `LG00045-b-UK` establishes:

| Property | Value |
| --- | --- |
| Mounting | 2 flush-mounted modules |
| User controls | 4 capacitive touch zones |
| Feedback | two light-blue LEDs per key zone, with adjustable intensity behavior |
| SCS supply | `18..27 Vdc` |
| Maximum consumption | `25 mA` at maximum LED level; `20 mA` medium; `17 mA` minimum |
| Operating temperature | `0..40 °C` |
| Depth | `18.3 mm` |
| Physical labels | `A`, `PL`, `M`, `SPE`; rear programming/LED-intensity button `P` |

The programming pushbutton `P` is a physical user/programming control, not simply another firmware configuration value.

## Identity and firmware

| Field | Value |
| --- | --- |
| `EN_ITEM.id_item` | `1376` |
| `AS_ITEM_SYSTEM.modobj` | `17` |
| Firmware | `159` |
| Firmware applicability | `-1.-1.-1` |
| Firmware slots | `5` |
| Configuration modes | Physical, Virtual, Advanced |

Commercial brand/line values distinguish the individual records around the shared `modobj = 17` technical core.

## Module and Object model

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

## Firmware-scoped configuration

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

## Published operating modes

The technical sheet documents several physical behavior families:

- self-learning mode, cyclic or non-cyclic, where individual key functions can be learnt;
- scenario-module mode for recalling/programming scenarios;
- direct/swivelling lighting or shutter control of consecutive targets;
- CEN mode for use with a scenario programmer;
- sound-system mode when `SPE=1`;
- learned functions spanning lighting, automation, locking, staircase light, door release, floor call, camera cycling, sound diffusion, and AUX control.

It also specifies a two-minute self-calibration period after installation.

These published functions strongly corroborate the breadth of the catalogue Object set, but do not establish a one-to-one mapping between every physical mode and every database Object.

## Reusable Object configuration surfaces

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

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 17`, brand/line and installed `N_CONF` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate four command Objects plus the UI-settings Module | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | determine configured functional addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values | [Configuration](../../diagnostics/dim35-configuration.md) |

## Corroboration status and open work

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
