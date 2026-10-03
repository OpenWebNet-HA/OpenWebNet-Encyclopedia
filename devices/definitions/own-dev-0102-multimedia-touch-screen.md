# Multimedia Touch Screen

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0102` | Project identity |
| Technical description | 10-inch multimedia touchscreen for configured MyHOME controls and video door entry | Publisher manuals; canonical catalogue |
| Commercial identities | `HC4690`, `HD4690`, `HS4690` | Catalogue item `1340`; installer/user/software manual covers |
| Catalogue item | `1340` | Canonical MyHOME Suite `3.5.38` catalogue |
| Main catalogue system | Integration functions | Canonical catalogue |
| Item model / `modobj` | `41` | Canonical inventory |
| Firmware definition | `4.0.0`, `3.0.0`, `2.0.0`, `1.1.0` | Canonical firmware/build catalogue |
| Declared Modules | `1` for every listed firmware | Canonical catalogue |
| Categories | User interface, Audio/video, Multifunction device | Published applications and catalogue model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC4690` | Established commercial variant | Catalogue item `1340`, Clear label; `U3567E` / `U3569H` covers |
| BTicino - Axolute | `HD4690` | Established commercial variant | Catalogue item `1340`, White label; `U3567E` / `U3569H` covers |
| BTicino - Axolute | `HS4690` | Established commercial variant | Catalogue item `1340`, Dark label; `U3567E` / `U3569H` covers |

Finish labels above are catalogue descriptions. The `HA4690...` surround plates are accessories, not additional Device identities. The separate Legrand Multimedia Touch Screen cluster, item `1809` / `modobj = 48`, is not merged into this `modobj = 41` dossier merely because its description and firmware tuples resemble it.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00635_a_EN.pdf` | technical sheet | `BT00635-a-EN`; no publication date printed | `HC/HS4690`; description/specifications/interfaces printed p. 1 / PDF p. 1; PC connection printed p. 2 / PDF p. 2; wiring printed p. 3 / PDF p. 3; installation printed p. 4 / PDF p. 4 | [Archived original](https://archive.openwebnet-ha.org/sha256/1b/40/1b40e0a32a0a8de274874f966c8aa1a91674c5d2fc3af965fdc4e5a062a8242f.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/BT00635_a_EN.pdf) |
| `U3567E.pdf` | installation manual | `U3567E`, `06/11-01 PC` | `HC/HS/HD4690`; English warnings printed p. 3 / PDF p. 3; interfaces printed pp. 7, 10-12 / PDF pp. 7, 10-12; installation printed pp. 17-25 / PDF pp. 17-25; PC setup printed pp. 26-27 / PDF pp. 26-27; specifications/dimensions printed pp. 28-30 / PDF pp. 28-30 | [Archived original](https://archive.openwebnet-ha.org/sha256/fd/2a/fd2a62023b9360f5f0d01232ea4a773ae75c8251111838787e195652ba24ca4c.pdf) | [Publisher original](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileName=U3567E.pdf&fileId=58107.23188.9117.39299) |
| `U3569H_Software_EN.pdf` | software manual | `U3569H`, `09/12-01 PC` | `HC/HS/HD4690`; transfer/update/info printed pp. 4-9 / PDF pp. 4-9; project settings/applications printed pp. 10-74 / PDF pp. 10-74 | [Archived original](https://archive.openwebnet-ha.org/sha256/51/90/5190144970bca74a7b6c77cf66f53a8c07e420f8ef93c75228eb17ea337f03d3.pdf) | [Publisher original](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileName=U3569H_Software_EN.pdf&fileId=58107.23188.9117.39299) |
| `U3569H_Utente_EN.pdf` | user manual | `U3569H`, `09/12-01 PC` | `HC/HS/HD4690`; interfaces/navigation/calls printed pp. 6-12 / PDF pp. 6-12; applications printed pp. 15-78 / PDF pp. 15-78; local settings printed pp. 80-89 / PDF pp. 80-89 | [Archived original](https://archive.openwebnet-ha.org/sha256/21/3d/213d5d6d32c1f080e2b85c3a77a2c9c97876e4f0738d801e1b76e54ad1b86657.pdf) | [Publisher original](https://www.homesystems-legrandgroup.com/MatrixENG/liferay/bt_mxLiferayCheckout.jsp?fileFormat=generic&fileName=U3569H_Utente_EN.pdf&fileId=58107.23188.9117.39299) |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | Item `1340`; commercial, firmware, Module/Object, configuration and software association records | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | 10-inch colour LCD, aspect ratio `16:9`; technical-sheet legend says LED, see reconciliation | `BT00635-a-EN`, printed p. 1 / PDF p. 1; `U3569H User EN`, printed p. 6 / PDF p. 6 |
| Published LCD note | Up to `5` small dark/coloured dots may occur without indicating a malfunction | `U3569H User EN`, printed p. 6 / PDF p. 6 |
| Dimensions | `305 x 228 x 17 mm` (width x height x depth) | `U3567E`, printed p. 30 / PDF p. 30; HC/HS also `BT00635-a-EN`, printed p. 1 / PDF p. 1 |
| SCS BUS supply | `18..27 Vdc` | `U3567E`, printed p. 28 / PDF p. 28 |
| Additional local supply, terminals `1-2` | `18..27 Vdc`; required, observe polarity | `U3567E`, printed p. 19 / PDF p. 19; `U3567E`, printed p. 28 / PDF p. 28 |
| Maximum local current | `600 mA` from terminals `1-2` | `U3567E`, printed p. 28 / PDF p. 28 |
| Maximum SCS BUS current | `50 mA` | `U3567E`, printed p. 29 / PDF p. 29 |
| Operating temperature | `5..45 °C` | `U3567E`, printed p. 29 / PDF p. 29 |
| Installation | Indoors; supplied metal wall bracket and `HA4690...` surround; protect from dripping/splashing water | `U3567E`, printed p. 3 / PDF p. 3; printed pp. 17-23 / PDF pp. 17-23 |
| Listed accessories | Supply `346020`; plates `HA4690XC`, `HA4690VBB`, `HA4690LTK`, `HA4690VNB`, `HA4690VSW` | HC/HS scope; `BT00635-a-EN`, printed p. 1 / PDF p. 1 |
| Front interfaces | Microphone; USB ports; mini-USB PC connection; SD-card port | `U3567E`, printed p. 7 / PDF p. 7 |
| SD storage | Maximum `2 GB`; do not use HC-SD cards; publisher says `2 GB` card supplied | `U3567E`, printed p. 7 / PDF p. 7; `U3567E`, printed p. 10 / PDF p. 10; `U3569H User EN`, printed p. 8 / PDF p. 8 |
| USB storage limitation | Do not insert two USB pen drives simultaneously | `U3567E`, printed p. 7 / PDF p. 7; `U3569H User EN`, printed p. 8 / PDF p. 8 |
| Future-application interfaces | USB webcam port, Wi-Fi dongle use and PSTN telephone port marked future application | `U3567E`, printed p. 7 / PDF p. 7; `U3567E`, printed p. 12 / PDF p. 12 |
| Rear connections | Sound-source output, Ethernet RJ45 with LAN LEDs, video two-wire SCS BUS, supply `1-2`, RS232 PC connection | `U3567E`, printed p. 12 / PDF p. 12 |
| Rear controls / audio | End-of-line `ON`/`OFF` switch, speakers, factory-settings reset button, battery compartment | `U3567E`, printed p. 12 / PDF p. 12 |
| Battery rating | HC/HS: NiMH `7.2 V`, `160 mAh`; HD rating not separately established | `BT00635-a-EN`, printed p. 1 / PDF p. 1; family replacement illustration `U3567E`, printed p. 25 / PDF p. 25 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1340` | Canonical catalogue |
| Technical item | Multimedia Touch Screen | Canonical catalogue |
| Item family | Other devices (`100`) | Canonical catalogue |
| Main system | Integration functions | `AS_ITEM_SYSTEM` main association |
| Item model / `modobj` | `41` | Main item/system association |
| Brand / line metadata | BTicino; Axolute; brand model `1`, line model `3` | Commercial records and model fields; line database key `2` is separate |
| Commercial records | `3` | Canonical catalogue |
| Catalogue gateway flag | Not marked as a gateway for all three records | Commercial metadata; does not negate the software manual's remote-control password setting |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `1` | `4` | `0` | `0` | `1` | Catalogue default | Official |
| `662` | `3` | `0` | `0` | `1` | Not catalogue default | Official |
| `663` | `2` | `0` | `0` | `1` | Not catalogue default | Official |
| `664` | `1` | `1` | `0` | `1` | Not catalogue default | Official |

Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

The publisher download page separately labels firmware packages `MMT_040006.fwz` (`4.0.6`) and `MMT_040013.fwz` (`4.0.13`). These labels extend the release inventory; they do not create new catalogue Module/Object rows or establish an installed version. Package contents and hardware compatibility have not been independently examined.

| Catalogue firmware | Software association | Scope / limitation |
| --- | --- | --- |
| `1` (`4.0.0`) | `xml\SDC\sdc.xml`; `1340_4.0_BT\xml\SVM\svm.xml`; `1340_4.0_BT\xml\Extra\extra.xml`; `1340_4.0_BT\xml\DIRECTOR\director.xml`; `1340_4.0_BT\xml\Protocol\protocol.xml` | Registered parameter paths; payloads not inspected here |
| `662` (`3.0.0`) | `TiMultimediaTouchScreen_0300` | Product-tool association; executable not examined |
| `663` (`2.0.0`) | `TiMultimediaTouchScreen_0200` | Product-tool association; executable not examined |
| `664` (`1.1.0`) | `TiMultimediaTouchScreen_0101` | Product-tool association; executable not examined |
| `1` (`4.0.0`) | Language packages `GL1`, `GL21`, `GL31`, `GL42`, `GL51`, each tuple `4.0.0` | Catalogue package membership; associated `2.xtz` / `3.xtz` payloads not examined |

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1387` | `32` | `733` |
| `662` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2491` | `32` | `1141` |
| `663` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2492` | `32` | `1142` |
| `664` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2493` | `32` | `1143` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue connection routes | Product-source reconciliation |
| --- | --- | --- | --- |
| `1` | Product Programming | Ethernet, USB | Catalogue mode/connection associations; publisher also describes serial `3559` |
| `662` | Product Programming | Ethernet, USB | Catalogue mode/connection associations; publisher also describes serial `3559` |
| `663` | Product Programming | Ethernet, USB | Catalogue mode/connection associations; publisher also describes serial `3559` |
| `664` | Product Programming | Ethernet, USB | Catalogue mode/connection associations; publisher also describes serial `3559` |

`Product Programming` means a configured product project in this catalogue. The application icons described in the software manual are project objects; they are not additional protocol Objects or Modules. The manuals describe serial, USB and Ethernet PC connections (installer printed pp. 26-27 / PDF pp. 26-27; software printed p. 7 / PDF p. 7), while the retained send wizard shows only Ethernet and USB (software printed p. 8 / PDF p. 8).

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped. Templates are stored string masks, not complete legal numeric/IP domains or installed values.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `1` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `1` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `1` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `1` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `662` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `662` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `662` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `662` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `663` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `663` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `663` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `663` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `664` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `664` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `664` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `664` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

The source stores `FW_VER` default `3.0.0` for all four firmware definitions, including `4.0.0`, `2.0.0` and `1.1.0`. Preserve that reusable metadata discrepancy rather than replacing it with each firmware tuple. `AID` has template `********` and no source default; permitted character sets are not established by these range rows.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

Object `32`'s string masks have no stored numeric minimum/maximum. Its defaults are reusable catalogue metadata; the IP address is a published catalogue default, not a retained installation address. The fuller project settings below are product-software evidence with no established mapping to these three reusable fields.

### Published project parameters

| Setting / surface | Published values, domain or constraint | Evidence |
| --- | --- | --- |
| Clock | Master/Slave role; update interval active only for Master; date format, time zone | `U3569H Software EN`, printed p. 10 / PDF p. 10 |
| Temperature format | Celsius or Fahrenheit; source unit-symbol inconsistency retained | `U3569H Software EN`, printed p. 10 / PDF p. 10 |
| Installation type | Multimedia for multichannel matrix; Automation for SCS BUS; private-riser/local-BUS level | `U3569H Software EN`, printed p. 10 / PDF p. 10 |
| Video door entry | Enable according to wiring; SCS/IP type for multimedia; associated handset H address | `U3569H Software EN`, printed p. 10 / PDF p. 10 |
| Multimedia addresses | Touchscreen as sound source and amplifier; source address must not duplicate another source | `U3569H Software EN`, printed p. 10 / PDF p. 10; `U3569H Software EN`, printed p. 39 / PDF p. 39 |
| Culture / language | Decimal separator full stop/comma; graphic-interface language | `U3569H Software EN`, printed p. 10 / PDF p. 10 |
| Project / network / security | Project name; progressive touchscreen address; IP acquisition, address, mask, router, primary/secondary DNS; OPEN remote-control password | Software printed p. 74 / PDF p. 74; source spells DNS as DSN |
| Home page | Application/subpage objects with configured properties; Settings icon cannot be removed | `U3569H Software EN`, printed p. 13 / PDF p. 13; `U3569H Software EN`, printed p. 57 / PDF p. 57 |
| Automation / lighting addressing | A/PL of target; private riser level `3`, local BUS level `4`; expansion-interface address for local BUS; lock target follows video or automation wiring | Software printed pp. 14-18 / PDF pp. 14-18 |
| Movement mode | Safe: movement only while held; Normal/Standard: start on touch, explicit stop | `U3569H Software EN`, printed p. 14 / PDF p. 14; `U3569H User EN`, printed p. 16 / PDF p. 16 |
| Lighting | Lamp/dimmer PUL selection must match target configuration; point, room, group/general and grouped-dimmer controls; fixed timer requires a target supporting virtual configuration | Software printed pp. 16-18 / PDF pp. 16-18 |
| Burglar-alarm entries | Maximum `8`; addresses and zone descriptions; source calls them sources | `U3569H Software EN`, printed p. 19 / PDF p. 19 |
| STOP&GO supervision | Maximum `20` devices; target addresses `1..127`; Stop&Go / Plus / BTest | `U3569H Software EN`, printed p. 21 / PDF p. 21 |
| Load diagnostics | Target address `1..64`; published leakage-current monitoring role | `U3569H Software EN`, printed p. 22 / PDF p. 22 |
| Consumption/production | Electricity, water, gas, domestic hot water, heating/cooling and customized; maximum `20` electricity Line objects; line address `1..255` | Software printed pp. 23-24 / PDF pp. 23-24 |
| Energy presentation | Consumption/production type; economic evaluation and tariffs; monthly target values; one/two warning thresholds; economic evaluation indicative | `U3569H Software EN`, printed p. 24 / PDF p. 24; `U3569H Software EN`, printed p. 25 / PDF p. 25; `U3569H Software EN`, printed p. 73 / PDF p. 73 |
| Load management | Priority `1..255`; with/without load central unit; advanced actuators provide current/consumption meters | `U3569H Software EN`, printed p. 26 / PDF p. 26; `U3569H Software EN`, printed p. 27 / PDF p. 27 |
| Temperature project | One central-unit type, one external-probe object, one non-controlled-zone object and one air-conditioning object; nested zone/page setup, fan-coil option | Software printed pp. 28-33 / PDF pp. 28-33 |
| Thermoregulation programs/scenarios | Software page says `5` programs; separate summer/winter program and scenario selections; user manual states `3` seasonal programs and `16` seasonal scenarios | Software printed pp. 30-31 / PDF pp. 30-31; user printed pp. 51, 53 / PDF pp. 51, 53; scope/count discrepancy unresolved |
| Non-controlled-zone address | Target ZA, ZB and N; follow target configuration; legal numeric domains not enumerated | `U3569H Software EN`, printed p. 33 / PDF p. 33 |
| Air conditioning, basic | Uses `20` commands saved in interface `3456`; A/PL, level/interface, saved OFF command, optional Slave-probe address and group OFF | Software printed pp. 34-35 / PDF pp. 34-35 |
| Air conditioning, advanced | ZA/ZB, N `0..9`; Slave probe, OFF control, minimum/maximum temperature; temperature step `0.5 °C` or `1 °C`; operating/fan/swing options depend on splitter | Software printed pp. 36-38 / PDF pp. 36-38; Slave address wording conflicts |
| Audio | Maximum `8` sources; Radio, Aux or multimedia touchscreen; PF target addresses, room/special-zone amplifier groups, power-amplifier presets | Software printed pp. 39-41 / PDF pp. 39-41 |
| Stored scenarios | A/PL, level/interface and scenario/pushbutton number; scenario module supports up to `16`; Scenario Plus address | Software printed pp. 42-43 / PDF pp. 42-43 |
| Advanced scenarios | Time condition and optional Device condition; light, dimmer, temperature, amplifier or auxiliary; generate the OPEN action by family, object, control, address and action | Software printed pp. 44-46 / PDF pp. 44-46; time-condition necessity wording inconsistent |
| Programmed scenarios | Start, Stop, Enable, Disable CEN controls must match the external Scenario Programmer; A/PL and level/interface | `U3569H Software EN`, printed p. 47 / PDF p. 47 |
| Video targets | Entrance-panel/camera address; internal/external intercom handset address `1..3999`; call exclusion | Software printed pp. 48-50 / PDF pp. 48-50 |
| Multimedia / favourites | USB/SD objects need no configuration; stream URL for web radio, RSS URL/category/preview, webcam URL; favourites reuse control addressing/PUL | Software printed pp. 51-56 / PDF pp. 51-56 |
| Screen / screensaver | Cleaning interval `10 s..1 min`; screensaver none/time/text/photos; screen-off delay `30 s..5 min`; screensaver wait `30 s..2 min`; image interval `2..60 s` | Software printed pp. 62-63 / PDF pp. 62-63 |
| Local menu password | Numeric password; user manual specifies five digits, requested at power-on or standby wake when protection enabled | `U3569H Software EN`, printed p. 58 / PDF p. 58; `U3569H User EN`, printed p. 86 / PDF p. 86 |
| Alarm clock | Beep or sound-system source; enable preserves settings; days, hour/minute; configured source and rooms | Software printed pp. 64-65 / PDF pp. 64-65; `U3569H User EN`, printed p. 88 / PDF p. 88 |
| Door-entry options | Hands free, ring exclusion, Professional Studio and Teleloop mode matching associated device | Software printed pp. 66-67 / PDF pp. 66-67; `U3569H User EN`, printed p. 89 / PDF p. 89 |
| Ringtones | Maximum `10`; import `.mp3`, `.wav`, `.pcm`; select/edit a maximum `5 s` extract; save and add to project | Software printed pp. 68-72 / PDF pp. 68-72 |
| Energy notifications | Warning beep enable; monthly previous-consumption window and display time in software; user manual separately describes threshold popup | Software printed p. 60 / PDF p. 60; user printed p. 89 / PDF p. 89; trigger scope unresolved |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item `1340`, main model `41`; distinguish the Legrand item `1809` / model `48` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Corroborate applicable firmware/build; do not substitute stored `FW_VER` default for observed tuple | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Corroborate one declared Module with external Object `32`; application count is unrelated | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Inspect addressing in the resolved integration-Object context | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare reported configuration with firmware/Object masks; product-project serialization remains uncorroborated | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The catalogue associates external Object `32` (Colors Touch Screen) with Integration functions. The published applications below depend on the installed system and the configured product project. Their icons and product-software objects do not imply additional protocol Modules or dedicated externally exposed Objects. Canonical command families remain under [Functional Protocol](../../functional/); the manuals do not establish a universal remote command list or gateway-session behavior.

| Application / function | Published behavior and boundary | Evidence |
| --- | --- | --- |
| Movement controls | Blinds, shutters, gate and garage door; Safe mode stops on release, Standard mode requires Stop; groups can move several targets | User printed pp. 15-16 / PDF pp. 15-16 |
| Other automation | Fan, controlled socket and irrigation on/off with state indication; contact open/closed indication; lock acts while pressed, or follows video-door-lock timing | `U3569H User EN`, printed p. 17 / PDF p. 17 |
| Lighting / dimmers | Individual/group lights; dimmer level display in `10` or `100` levels; broken-bulb indication if lamp is disconnected/faulty; grouped dimmers adjust from their existing relative levels | User printed pp. 18-19 / PDF pp. 18-19 |
| Lighting timers | Preset timed light; software-set fixed duration with remaining-time indication; video-door-entry staircase light | `U3569H User EN`, printed p. 19 / PDF p. 19 |
| Stored scenarios | Run central-unit or module scenarios; module programming/deletion available only when its programming controls are unlocked | User printed pp. 20-21 / PDF pp. 20-21 |
| Programmed scenarios | Display/control up to `20` of the external programmer's `300` scenarios; Enable/Disable changes eligibility, Start/Stop forces execution control | `U3569H User EN`, printed p. 22 / PDF p. 22 |
| Advanced scenarios | Up to `20` advanced scenarios; Enable/Disable and Start; time plus optional Device-state condition; combined list also described as maximum `20` | User printed pp. 22-24 / PDF pp. 22-24; aggregate limit not reconciled with separate maxima |
| Advanced scenario conditions | Light `ON`/`OFF`; dimmer `OFF` or `20..100 %` in `20 %` steps; temperature `-5..50 °C` in `0.5 °C` steps; audio `0..100 %`, source says increments `20 %` and `30 %` | User printed pp. 23-24 / PDF pp. 23-24; audio progression unresolved |
| Sound system | Radio tuning/preset storage, external source or touchscreen multimedia source; individual/group amplifier power and volume; multi-channel room/special-zone controls | User printed pp. 25-29 / PDF pp. 25-29 |
| Power amplifier | Equalizer preset, bass/treble `-10..10`, left/right balance and Loudness; target must be an applicable power amplifier | `U3569H User EN`, printed p. 27 / PDF p. 27 |
| USB / SD playback | Audio `.mp3`; video `.mp4` maximum `320 x 240 pixels`; images `.jpg`, source size limit `10 Mb` with unit ambiguity; local playback and image slideshow/screensaver | User printed pp. 30-37 / PDF pp. 30-37 |
| Storage state / removal | Inserted USB/SD icon becomes active; software eject disables media; remove/reinsert to re-enable | `U3569H User EN`, printed p. 9 / PDF p. 9; `U3569H User EN`, printed p. 31 / PDF p. 31 |
| Audio routing | Send local tracks or internet-radio playback to a selected sound-system room/amplifier | User printed pp. 32-33, 38-39 / PDF pp. 32-33, 38-39 |
| Internet multimedia | Configured radio-stream URLs, RSS news/weather and remote webcam images require broadband LAN access; station/feed availability is external | User printed pp. 38-43 / PDF pp. 38-43; software printed pp. 52-55 / PDF pp. 52-55 |
| Media Client | Browse music on PCs on the same Ethernet network and play `.mp3` tracks, including sound-system routing; no network-sharing protocol specified | User printed pp. 44-46 / PDF pp. 44-46 |
| Burglar alarm | Armed/disarmed indication; change active zones only while disarmed; zone confirmation and arming/disarming require the alarm central unit's user code | User printed pp. 47-48 / PDF pp. 47-48 |
| Alarm history | Intrusion, tamper, panic and technical alarm indications with time/date/zone; view/delete listed events | `U3569H User EN`, printed p. 48 / PDF p. 48 |
| Thermoregulation prerequisites | Applicable `4`-zone or `99`-zone central unit; remote control must be enabled on that unit; local sensor at antifreeze/protection or OFF blocks touchscreen adjustment | User printed pp. 49-54 / PDF pp. 49-54 |
| Thermoregulation modes | Summer/Winter; seasonal program, holiday, weekend, manual, OFF and antifreeze; `4`-zone timed manual mode; `99`-zone seasonal scenarios; `0.5 °C` manual adjustment | User printed pp. 50-53 / PDF pp. 50-53 |
| Zones / probes / air conditioning | Zone temperature/offset and applicable fan-coil speeds; measurement-only/external probes; basic or advanced splitter control according to target/configuration; `0.5 °C` or `1 °C` temperature step | User printed pp. 54-58 / PDF pp. 54-58 |
| STOP&GO supervision | Device closed/open/fault/block indicators; automatic-rearm enable; Plus check/rearm controls; BTest autotest enable and interval setting | User printed pp. 59-62 / PDF pp. 59-62 |
| Load diagnostic | Published leakage-current status as normal, near limit or over limit; this is target-dependent product monitoring, not a measurement made by the touchscreen | `U3569H User EN`, printed p. 62 / PDF p. 62 |
| Consumption / production | Electricity plus pulse-meter water, gas, hot water and heating/cooling; targets, thresholds, economic display, charts/tables; day/month/last-12-month views and six-month overview | User printed pp. 63-69 / PDF pp. 63-69 |
| Load control | With central unit: priority shedding and temporary force-on; advanced actuators add instantaneous consumption/resettable meters; without central unit: advanced-actuator monitoring | User printed pp. 70-72 / PDF pp. 70-72 |
| Force-on duration | Overload-page action described as default `4 h`; detail-page forcing described as default `2 h 30 min`; contexts differ and no equivalence established | User printed pp. 70-71 / PDF pp. 70-71 |
| Door-entry calls | Answer/end, microphone mute, incoming volume, staircase light, lock and camera selection; video brightness/contrast/colour and full-screen; pan/tilt only on a supporting camera | User printed pp. 10-12 / PDF pp. 10-12 |
| CCTV / intercom | Internal/external intercom and camera viewing; busy shared audio/video channel prevents connection; entrance-panel call interrupts viewing/conversation; bell enable/exclusion | User printed pp. 73-76 / PDF pp. 73-76 |
| Messages | Read received messages with timestamp; scroll long text; delete one/all; sending mechanism and memory capacity not established | User printed pp. 77-78 / PDF pp. 77-78 |
| User settings | Brightness, touch calibration, temporary cleaning lock, screensaver, clock, microphone/speaker volume, beep, event ringtones, password, version/network view, alarm clock and energy alerts | User printed pp. 80-89 / PDF pp. 80-89 |
| Cleaning / calibration | Published cleaning-lock default `20 s`; configurable in software; calibrate displayed cross positions then confirm corners; incorrect calibration can prevent correct touch interpretation | User printed pp. 82-83 / PDF pp. 82-83 |
| Version / network view | Model, firmware/kernel and network information; network page can enable/disable the interface; illustrated addresses/versions are examples, not an observed installation | `U3569H User EN`, printed p. 87 / PDF p. 87 |
| Door-entry options | Hands-free and Professional Studio on/off; Teleloop association; active options shown in status bar | `U3569H User EN`, printed p. 89 / PDF p. 89 |

## Observed behavior and corroboration

No sanitized hardware fingerprint, OpenWebNet capture or controlled commissioning observation is retained for this exact technical item. The manual screenshots and example values are publisher illustrations; they are not observations of a Physical Device held by the project.

## Programming

Use the applicable TiMultimediaTouchScreen project and firmware association. Product project editing, transfer, firmware update, local settings and OpenWebNet runtime control are separate operations.

### Installation and commissioning

| Stage | Documented procedure / constraint | Evidence |
| --- | --- | --- |
| Mechanical installation | Fit the `HA4690...` surround before mounting; attach supplied metal bracket and connect the screen; final screw direction differs between sources | Installer printed pp. 17-23 / PDF pp. 17-23; technical sheet printed p. 4 / PDF p. 4 |
| Power and wiring | Required extra supply on terminals `1-2`, with correct polarity; illustrated Ethernet, video/audio SCS and sound-source connections | Installer printed pp. 19-20 / PDF pp. 19-20; technical sheet printed p. 3 / PDF p. 3 |
| End-of-line termination | Set rear micro-switch to `ON` if the screen is last on the line; verify bracket nut position | `U3567E`, printed p. 21 / PDF p. 21 |
| Battery service | Remove cover and follow battery insertion/connection illustration; no backup-duration specification | `U3567E`, printed p. 25 / PDF p. 25 |
| Project creation | Create a project matching wiring, device addresses and required applications; configure selected-item properties and inspect reported configuration errors | Software printed pp. 4-6, 10-13 / PDF pp. 4-6, 10-13 |
| PC connection | USB-miniUSB, serial cable `3559` or Ethernet described; send wizard documents Ethernet/USB choices | Software printed pp. 7-8 / PDF pp. 7-8 |
| Send project | Connect PC, choose Tools / Send configuration, advance, select displayed connection mode, then advance to transfer | `U3569H Software EN`, printed p. 8 / PDF p. 8 |
| Receive / edit / resend | Tools / Receive configuration reads the existing project; edit/save or resend using the transfer workflow | `U3569H Software EN`, printed p. 9 / PDF p. 9 |
| Firmware update | Tools / Update the firmware opens a `.fwz` compressed package; select applicable package and continue through connection workflow; rollback/recovery not documented | `U3569H Software EN`, printed p. 9 / PDF p. 9 |
| Device information | Tools / Request device info and advance to hardware/software information; inspect local Version/Network views for contextual comparison | `U3569H Software EN`, printed p. 9 / PDF p. 9; `U3569H User EN`, printed p. 87 / PDF p. 87 |
| Local recovery boundary | Rear button is identified as factory-settings reset; no hold time, precise erase scope or complete recovery sequence in these manuals | `U3567E`, printed p. 12 / PDF p. 12 |

### Authoring and local-access constraints

| Surface | Published requirements / limits | Evidence |
| --- | --- | --- |
| Historical software environment | Windows XP SP2 (`32 bit`), Vista or Windows 7 (`32/64 bit`), processor above `2 GHz`, `.NET 3.5 SP1`, `500 MB` free disk; source states XP RAM `1 MB`, an unresolved requirement irregularity | `U3569H Software EN`, printed p. 4 / PDF p. 4 |
| Application update | Software checks for newer versions online and offers to save an updated executable; current version may continue in use | `U3569H Software EN`, printed p. 4 / PDF p. 4 |
| Project objects | Configure descriptions and target addresses without treating screen pages/icons as protocol Modules; Settings icon always present | Software printed pp. 6, 11-13, 57 / PDF pp. 6, 11-13, 57 |
| Menu password | Five-digit local menu password, when enabled, is requested at startup and after standby; distinct from alarm-central-unit user code and OPEN remote-control password | `U3569H User EN`, printed p. 86 / PDF p. 86; `U3569H User EN`, printed p. 48 / PDF p. 48; `U3569H Software EN`, printed p. 74 / PDF p. 74 |
| Source limits | Browser minima and PC screenshots describe the historical software environment; no present-day OS/browser compatibility or online-service availability established | Software printed p. 4 / PDF p. 4; dated retained source scope |

## Source reconciliation

The catalogue groups `HC4690`, `HD4690` and `HS4690` under item `1340` with main `modobj = 41`. The covers of `U3567E` and both `U3569H` manuals name all three references, independently supporting the family association. `BT00635-a-EN` names only HC/HS: use the all-family installation manual for shared supply, current, temperature and dimensions, while the sheet-only battery rating remains HC/HS-scoped. Clear/White/Dark finish labels are catalogue evidence. `HA4690...` plates are accessories. The Legrand item `1809`, with model `48`, remains a separate technical cluster.

The four firmware definitions each register one Module slot and Object `32`; the three reusable Object fields repeat firmware-level string-mask information. A product application, screen page or software project object is not an additional protocol Object. Catalogue default `FW_VER = 3.0.0` persists across different firmware tuples and is not an installed-version report. Publisher release labels `4.0.6` and `4.0.13` are separate from the catalogue's `4.0.0` definition.

### Preserved source discrepancies

| Source issue | Reconciliation / unresolved limit | Source locations |
| --- | --- | --- |
| Display terminology | Sheet description and user manual say LCD; sheet legend says LED. The dossier records the conflict without inferring a backlight technology | `BT00635-a-EN`, printed p. 1 / PDF p. 1; `U3569H User EN`, printed p. 6 / PDF p. 6 |
| Mounting screw | Technical sheet says clockwise; installer `U3567E` says anticlockwise. No verified hardware/revision explanation establishes equivalence | `BT00635-a-EN`, printed p. 4 / PDF p. 4; `U3567E`, printed p. 23 / PDF p. 23 |
| Software target naming | Manual cover and product-specific chapters name the Multimedia Touch Screen, but introductory/currency text calls it Local Display. This is retained as inconsistent source wording, not identity equivalence | `U3569H Software EN`, printed p. 4 / PDF p. 4; `U3569H Software EN`, printed p. 73 / PDF p. 73 |
| Temperature-unit symbol | Software prose assigns `°F` to Celsius as well as Fahrenheit; its screenshot labels Celsius `°C`. Preserve discrepancy while keeping the named format choices | `U3569H Software EN`, printed p. 10 / PDF p. 10 |
| Slave address bound | Software text pairs range `1..9` with endpoint label Slave `8`; no unique legal Slave domain inferred | `U3569H Software EN`, printed p. 37 / PDF p. 37 |
| Advanced scenario time condition | Software p. 44 describes a required time condition; p. 45 calls it present conditionally. No missing precedence rule invented | Software printed pp. 44-45 / PDF pp. 44-45 |
| Scenario capacities | Combined advanced/programmed list maximum `20`, separately up to `20` advanced and `20` selected programmed scenarios; overall aggregation remains unresolved | User printed pp. 22-23 / PDF pp. 22-23 |
| Seasonal programs | Software mentions `5` programs; user manual states `3` summer and `3` winter programs. UI/context difference not resolved | Software printed p. 30 / PDF p. 30; user printed p. 51 / PDF p. 51 |
| Load forcing | Defaults `4 h` and `2 h 30 min` described on different UI paths; neither promoted to universal duration | User printed pp. 70-71 / PDF pp. 70-71 |
| Audio-condition progression | Range `0..100 %` accompanied by `20 %` and `30 %` increments; exact selectable sequence unresolved | `U3569H User EN`, printed p. 24 / PDF p. 24 |
| Image-size unit | Literal limit `10 Mb`; byte/bit interpretation not established by the printed text | `U3569H User EN`, printed p. 31 / PDF p. 31 |
| Energy notification trigger | Software describes first-of-month prior-consumption popup; user manual describes threshold popup. Record both paths without assuming identical triggers | `U3569H Software EN`, printed p. 60 / PDF p. 60; `U3569H User EN`, printed p. 89 / PDF p. 89 |
| Serial programming route | Three cable routes in instructions; catalogue and send wizard list Ethernet/USB. Serial workflow beyond the connection drawing remains unresolved | Software printed pp. 7-8 / PDF pp. 7-8; firmware connection catalogue |
| Future versus remote webcam | USB webcam, Wi-Fi dongle and PSTN functions marked future; LAN webcam viewing documented separately. Neither the port labels nor LAN functions prove working USB webcam/PSTN features | Installer printed pp. 7, 12 / PDF pp. 7, 12; user printed pp. 30, 42-43 / PDF pp. 30, 42-43 |

The English technical sheet was fetched from both the BTicino document server and the manufacturer product-page download endpoint; both return the same SHA-256 bytes despite underscore/hyphen filename differences. The older indexed installer revision `U3567C` could not be retrieved from the tested publisher endpoints and is not substituted for the retained `U3567E`. The Italian technical-sheet link remains a known translation not independently reconciled. Firmware-package labels and software parameter/package associations are retained as metadata; their payloads are not examined here. General warranty text, vendor contact details and historical browser examples have no additional Device-specific protocol semantics; they remain available in the archived originals.

## Evidence limits and open work

- Retrieve and compare the older installer `U3567C` and the known Italian technical-sheet translation; current source review is limited to the four archived documents listed above.
- Resolve the mounting direction, seasonal/scenario capacities, Slave-address endpoint, audio-condition progression, image-size unit, energy-alert triggers and force-on defaults with exact software/hardware evidence.
- Examine referenced product-parameter XML, language-package and firmware-package payloads before asserting serialization, update compatibility, recovery or additional field domains.
- Establish the HD4690 battery rating, backup duration and exact reset-button timing/erase scope from directly applicable specifications.
- Corroborate Module/Object identity, firmware, addressing, project transfer and local/OPEN/alarm credential boundaries using sanitized hardware observations.
- Validate any required remote gateway/session behavior separately; an OPEN-password project field does not establish a TCP endpoint or universal runtime access.
- Check current online-feed, radio and remote-image availability only when operational use is required; these dated manuals establish the product feature, not service continuity.

## Sources

- [Device Database Inventory](../inventory/)
- [Canonical MyHOME Suite database metadata](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Manufacturer Multimedia Touch Screen downloads](https://www.homesystems-legrandgroup.com/product-detail/-/asset_publisher/X3IM65oMk1p1/content/multimedia-touch-screen)
- [BTicino HC4690 catalogue page](https://catalogo.bticino.it/prodotto/soluzioni-per-la-smart-home/my-home---sistema-domotico/integrazione-e-controllo/BTI-HC4690-IT)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Product Programming](../../programming/)
