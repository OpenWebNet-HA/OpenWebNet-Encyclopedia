# Legrand Multimedia Touch Screen

## Summary

This Legrand 10-inch multimedia touchscreen brings configured lighting, automation, scenarios, sound and video-door-entry functions into one wall interface. Its programmed menus and media connections support a shared control point, subject to the installed systems and the documented accessory limits.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0107` | Project identity |
| Technical description | Legrand Multimedia Touch Screen | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `067285`, `573963`, `573962` | All three catalogue commercial records; confidence scoped below |
| Catalogue item | `1809` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Integration functions | Main system association |
| Item model / `modobj` | `48` | Main association; independent of project ID |
| Firmware definition | `123`, `665`, `666`, `667` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Audio video, Multifunction devices | Source-derived roles |

Catalogue item `1809`, main model `48`, is separate from the BTicino item `1340`, model `41`. They share reusable Object `32`; this does not make their commercial identity, firmware or hardware interchangeable.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `067285` | Established commercial variant | Catalogue record `1950`; published family/variant scope reconciled below |
| Legrand - Arteor | `573963` | Established commercial variant | Catalogue record `1949`; published family/variant scope reconciled below |
| Legrand - Arteor | `573962` | Established commercial variant | Catalogue record `1951`; published family/variant scope reconciled below |

Both installer covers print `672 85`, establishing catalogue `067285`. The user-manual version illustration prints `573962/63`, supporting both Arteor references; it is not a hardware capture. All three catalogue records use Arteor, but the retained manuals do not establish the marketed line of `067285`; the human-facing row therefore uses Legrand alone. Catalogue colours are Titanium, Magnesium and White respectively; accessory plates are separate identities.

### Complete catalogue commercial metadata

| Record | Reference | Catalogue name | Brand key | Line key | Visible | Visibility type | Dependent | Gateway | Catalogue description |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `1949` | `573963` | `Multimedia Touch Screen` | `2` | `11` | `1` | Empty | `0` | `0` | `Multimedia Touch Screen Magnesium` |
| `1950` | `067285` | `Multimedia Touch Screen` | `2` | `11` | `1` | Empty | `0` | `0` | `Multimedia Touch Screen Titanium` |
| `1951` | `573962` | `Multimedia Touch Screen` | `2` | `11` | `1` | Empty | `0` | `0` | `Multimedia Touch Screen White` |

Empty catalogue values are retained as empty metadata; none is an installed-state or market-availability observation.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U3970A.pdf` | French / English user manual | `U3970A; 10/09-01 PC` | Cover 672 85; settings screenshot 573962/63 p. 129. French pp. 3-65 and English pp. 67-129; applications pp. 78-119; settings pp. 122-129. Printed pages equal PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/54/1c/541cd82ee7bc13dfb3f7c959b52eae598f6b47b80cf29c4da270918555a7c065.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-fr/np-ft-gt/u3970a.pdf) |
| `U3971A.pdf` | French / English installation manual | `U3971A; 10/09-01 PC` | Cover 672 85; English pp. 15-26: interfaces pp. 17-18, mounting pp. 19-22, battery p. 23, software/PC pp. 24-25, specifications p. 26. Printed pages equal PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/5a/87/5a87da8c493ac9acc149494d6267a1ac9ae3e00415bb6a9f20730674c6a46076.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-fr/np-ft-gt/u3971a.pdf) |
| `U3971B.pdf` | Multilingual installation manual | `U3971B; 12/10-01 PC` | Cover 672 85; interfaces pp. 6-13; plates/mounting pp. 14-18; battery p. 19; software/PC pp. 20-21; specifications pp. 22-23; dimensions p. 24. Printed pages equal PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/b1/7f/b17fc56132562fb71a7f0a3e6e521f4965547ed90f004cc6705597225586c4b3.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-fr/np-ft-gt/u3971b.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1809`: all firmware/commercial/system/Object/Module/Virgin/field/filter/mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `U3972D_S_FR.pdf` | Exact Legrand MultimediaTouchScreenConfig software manual, French | D / G from document identifier; full publication date not located | 67285 cover; all substantive configuration and transfer chapters examined. D pp. 4-67; G pp. 4-74; printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/cb/f1/cbf16a2673a9e8329795c38eb8899c841cdc435658c21cca4039fce3d2ef41aa.pdf) | [Publisher source](https://assets.legrand.com/general/legrand-fr/np-ft-gt/u3972d_s_fr.pdf) |
| `U3972G_Software_FR.pdf` | Exact Legrand MultimediaTouchScreenConfig software manual, French | D / G from document identifier; full publication date not located | 67285 cover; all substantive configuration and transfer chapters examined. D pp. 4-67; G pp. 4-74; printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/2a/b2/2ab25e7e880b7c3b546f25d4f69545e345457c239d5b4a5b2d338084621b3152.pdf) | [Publisher source](https://assets.legrand.com/general/legrand-fr/np-ft-gt/u3972g_software_fr.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | `10 inch`, `16:9` LCD touch screen | `U3970A`, printed/PDF p. 70 |
| Mounting and size | Wall bracket supplied; `305 x 228 x 17 mm` | `U3971A` pp. 19-22, 26; `U3971B` pp. 14-18, 24 |
| Supplies | SCS and mandatory separate `1-2` supply, each `18..27 Vdc`; preserve local polarity | A pp. 21, 26; B pp. 16, 22 |
| Maximum current | Local `600 mA`; SCS `50 mA` | A p. 26; B pp. 22-23 |
| Operating temperature | `5..45 °C` | Both exact 67285 installation revisions; A p. 26, B p. 23 |
| Front interfaces | Microphone; USB media; Mini-USB PC; SD slot; USB webcam and Wi-Fi dongle labelled future applications | A p. 17; B pp. 6-8 |
| Media-card limit | SD maximum `2 GB`; HC-SD unsupported; do not insert two USB drives simultaneously in revision B | A p. 17; B pp. 6-8 |
| Bundled card by revision | A: `512 MB`; B: `2 GB` installed | A p. 16; B p. 8 |
| Rear interfaces | SCS audio-source output; RJ45 Ethernet with link LEDs; 2-wire video SCS; `1-2` supply; termination switch; stereo speakers; factory-reset key; battery compartment; RS232 PC | A p. 18; B pp. 9-13 |
| PSTN | Rear port labelled future application | A p. 18; B p. 10 |
| Battery | NiMH `7.2 V`, `160 mAh` | A p. 23; B p. 19 |
| Accessories / PC | Plates `69309`, `69319`, `69349`; serial PC cable `49234` | A pp. 19, 25; B pp. 14, 21 |
| Installation scope | Indoors, Legrand digital 2-wire system; end-of-line switch `ON` if last device | A pp. 16, 21; B pp. 3, 17 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1809` | Canonical catalogue |
| Technical item description | Multimedia Touch Screen | Canonical catalogue |
| Item family | 0; key `100` | Canonical catalogue |
| Main system | Integration functions; key `26` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `48` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Integration function | `48` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Burglar alarm | private riser | Canonical item/bus relationship |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |
| Network | LAN | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `123` | `4` | `0` | `0` | `1` | Catalogue default | Official |
| `665` | `3` | `0` | `0` | `1` | Not catalogue default | Official |
| `666` | `2` | `0` | `0` | `1` | Not catalogue default | Official |
| `667` | `1` | `1` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Associated firmware packages

| Firmware | Package key | Package label | Package tuple |
| --- | --- | --- | --- |
| `123` | `12` | GL1 | `4.0.0` |
| `123` | `13` | GL21 | `4.0.0` |
| `123` | `14` | GL31 | `4.0.0` |
| `123` | `15` | GL42 | `4.0.0` |
| `123` | `16` | GL51 | `4.0.0` |

Package labels are source metadata; package applicability does not establish the installed tuple.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `123` | `236` | Legrand (key `2`) | `2` | SDC | `xml\SDC\sdc.xml` |
| `123` | `237` | Legrand (key `2`) | `2` | SVM | `1809_4.0_LG\xml\SVM\svm.xml` |
| `123` | `238` | Legrand (key `2`) | `2` | Extra | `1809_4.0_LG\xml\Extra\extra.xml` |
| `123` | `239` | Legrand (key `2`) | `2` | Director | `1809_4.0_LG\xml\DIRECTOR\director.xml` |
| `123` | `240` | Legrand (key `2`) | `2` | Protocol and other device parameters | `1809_4.0_LG\xml\Protocol\protocol.xml` |
| `665` | `710` | Legrand (key `2`) | `2` | external software | `MultimediaTouchScreenConfig_0300` |
| `666` | `711` | Legrand (key `2`) | `2` | external software | `MultimediaTouchScreenConfig_0200` |
| `667` | `712` | Legrand (key `2`) | `2` | external software | `MultimediaTouchScreenConfig_0101` |

All 8 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

| Firmware | Package record | Name | GL | Version | Release | Build | Unicode set | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `123` | `12` | `GL1` | `1` | `4` | `0` | `0` | `1` | Canonical package metadata |
| `123` | `13` | `GL21` | `21` | `4` | `0` | `0` | `2` | Canonical package metadata |
| `123` | `14` | `GL31` | `31` | `4` | `0` | `0` | `3` | Canonical package metadata |
| `123` | `15` | `GL42` | `42` | `4` | `0` | `0` | `4` | Canonical package metadata |
| `123` | `16` | `GL51` | `51` | `4` | `0` | `0` | `5` | Canonical package metadata |

These are catalogue package metadata; package payloads have not been inspected.

| Unicode set | Catalogue notes |
| --- | --- |
| `1` | GL1 |
| `2` | GL21 |
| `3` | GL31 |
| `4` | GL42 |
| `5` | GL51 |

The five package Unicode sets and all 4534 stored set/range associations were extracted and their hexadecimal bounds checked. [Complete canonical Unicode-set and range inventory](../inventory/touch-screen-package-unicode-ranges.json) retains each association key and minimum/maximum. These package text ranges do not define the allowed characters of firmware identity or network masks. Package payloads remain unexamined.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `123` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `1386` | `32` | `732` |
| `665` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2494` | `32` | `1144` |
| `666` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2495` | `32` | `1145` |
| `667` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `2496` | `32` | `1146` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `123` | Product Programming | `3` | Canonical firmware/mode association ; association mode key `4` |
| `665` | Product Programming | `3` | Canonical firmware/mode association ; association mode key `4` |
| `666` | Product Programming | `3` | Canonical firmware/mode association ; association mode key `4` |
| `667` | Product Programming | `3` | Canonical firmware/mode association ; association mode key `4` |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `123` | Ethernet | Canonical firmware/connection association ; connection key `2` |
| `123` | USB | Canonical firmware/connection association ; connection key `3` |
| `665` | Ethernet | Canonical firmware/connection association ; connection key `2` |
| `665` | USB | Canonical firmware/connection association ; connection key `3` |
| `666` | Ethernet | Canonical firmware/connection association ; connection key `2` |
| `666` | USB | Canonical firmware/connection association ; connection key `3` |
| `667` | Ethernet | Canonical firmware/connection association ; connection key `2` |
| `667` | USB | Canonical firmware/connection association ; connection key `3` |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `123` | `2` | `2` | `xml\SDC\sdc.xml` | Parameter type `1`; payload not inspected |
| `123` | `2` | `2` | `1809_4.0_LG\xml\SVM\svm.xml` | Parameter type `2`; payload not inspected |
| `123` | `2` | `2` | `1809_4.0_LG\xml\Extra\extra.xml` | Parameter type `4`; payload not inspected |
| `123` | `2` | `2` | `1809_4.0_LG\xml\DIRECTOR\director.xml` | Parameter type `5`; payload not inspected |
| `123` | `2` | `2` | `1809_4.0_LG\xml\Protocol\protocol.xml` | Parameter type `6`; payload not inspected |
| `665` | `2` | `2` | `MultimediaTouchScreenConfig_0300` | Parameter type `7`; payload not inspected |
| `666` | `2` | `2` | `MultimediaTouchScreenConfig_0200` | Parameter type `7`; payload not inspected |
| `667` | `2` | `2` | `MultimediaTouchScreenConfig_0101` | Parameter type `7`; payload not inspected |

Brand/line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

`U3971A` pp. 24-25 and `U3971B` pp. 20-21 document MultimediaTouchScreenConfig transfer/update via USB, Ethernet and serial cable `49234`. Catalogue associations retain Ethernet and USB only; serial support is publisher evidence, not an absent-table negation. Software application/project settings are distinct from three reusable Object fields.

### Published Legrand project configuration

| Surface | Published settings / limits | Exact source |
| --- | --- | --- |
| Project and transfer | Create/save `.prj`, receive an existing project, edit and send; firmware update uses `.fwz`; device-info query; D marks `.mhz` import future and exports CSV | D pp. 5-7, 63-67; G pp. 5, 8-9 |
| Network/security | Project name, progressive screen address, IP acquisition/address/mask/router, primary/secondary DSN (printed spelling), OPEN password; no credential copied into the dossier | D p. 9; G p. 74 |
| Clock and system | Clock Master and conditional update frequency; date formats, zone, Celsius/Fahrenheit; Multimedia/Automation bus, riser/local bus, video enabled/type SCS/IP, internal-unit address, source/amplifier address; G adds decimal separator and UI language | D p. 12; G p. 10 |
| Automation/lighting | Normal (hold to move) or advanced (start/Stop) control; A/PL and level 3 private riser or 4 local bus plus conditional interface; lock uses video address or A/PL by bus; PUL option, point/group/room/general associations, hours/minutes/seconds for supported timed loads and staircase control | D pp. 15-19; G pp. 14-18 |
| Alarm and supervision | Eight alarm-zone entries (source calls them sources); up to 20 Stop&Go entries, address `1..127`; load diagnostics `1..64` | D pp. 20-23; G pp. 19-22 |
| Energy and load control | Electricity/water/gas/DHW/heating-cooling/custom; up to 20 line entries, address `1..255`, kW/€ labels, economic valuation and consumption/production; advanced load priority `1..255`, controller-dependent mode/counters; G adds monthly objectives/graph and thresholds 1/2 | D pp. 24-27; G pp. 23-27 |
| Temperature | One controller type, external-probe category, unmanaged-zone category and AC category; four-zone controller bounds zones to four; five program entries and seasonal/scenario selection; external sensor address and unmanaged ZA/ZB/N | D/G pp. 28-33 |
| Air conditioning | 88301 interface, 20 stored commands in base mode; advanced direct control plus stored commands; A/PL/level/interface or ZA/ZB/N `0..9`, OFF command/group, optional slave `1..8`, minimum/maximum temperature, step 0.5/1 °C, auto/high/medium/low/silent fan, swing | D/G pp. 34-38 |
| Sound | Up to eight sources, Radio/Aux/Multimedia; do not duplicate this screen’s source address; room/group/general amplifier PF addresses and custom power-amplifier adjustment option | D/G pp. 39-41 |
| Scenarios | A/PL/level/interface, button, module scenario selection (16 stored by scenario module), Scenario Plus address; advanced time/device condition and generated OPEN action; programmed CEN Start/Stop/Enable/Disable must match programmer assignments | D/G pp. 42-47 |
| Video and media | Camera/entrance-panel address; internal/external intercom `1..3999`; USB/SD need no project address, Web radio streaming URL (not browser page), RSS/category and webcam URLs; Favorites with PUL and lighting/automation addresses | D/G pp. 48-56 |
| Home tools and UI | Options cannot be removed; temperature/radio/webcam home tools; beep, date/time, numeric local password, volume/ringing/version/network/video, brightness and calibration. Cleaning 10 s..1 min; screensaver none/time/text/photo, display off 30 s..5 min, activation 30 s..2 min, image interval `2..60` s | D pp. 57-62; G pp. 57-63 |
| Later notification/alarm/video | G: energy threshold beep and first-day-of-month consumption popup at selected time; alarm beep default or sound system, enable without losing settings, days/time; hands-free, ringing exclusion, Office and matching Tele Loop mode | G pp. 60, 64-67 |
| Later ringtone and tariff setup | G: at most ten ringtones, choose/import MP3/WAV/PCM, trim to maximum 30 s and save/reuse; currency, tariff and decimal digits | G pp. 68-74 |

These are product-project settings, separate from three protocol Object fields. The retained older U3970A user revision does not describe every feature added by the D/G software revisions.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `123` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `123` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address  Published example default, not an installed address |
| `123` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `123` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `665` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `665` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address  Published example default, not an installed address |
| `665` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `665` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `666` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `666` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address  Published example default, not an installed address |
| `666` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `666` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |
| `667` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `667` | `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address  Published example default, not an installed address |
| `667` | `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `667` | `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` | Local IP address  Published example default, not an installed address |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |

### Published application limits

| Surface | Published limit / behavior | Printed/PDF page |
| --- | --- | --- |
| Favourites | Four always-visible configured controls | U3970A p. 71 |
| Scheduled scenarios | Up to `20` of the programmer’s `300`; enable/disable differs from forced start/stop | p. 86 |
| Advanced scenarios | Up to `20`; time plus light/dimmer/temperature/amplifier condition; enable/disable and force start | pp. 87-88 |
| Dimmer condition | `OFF` or `20..100 %` in `20 %` steps | p. 87 |
| Temperature condition | `-5..50 °C`, `0.5 °C` increments | p. 88 |
| Audio condition | Printed `0..100 %`, with “20% and 30% increases”; nonuniform wording unresolved | p. 88 |
| Audio file | `.mp3` | p. 94 |
| Video file | `.mp4`, at most `320 x 240 px` | p. 94 |
| Images | `.jpg`, maximum `10 Mb` as printed; byte/bit notation unresolved; may be chosen for screensaver | p. 94 |
| Temperature programmes/scenarios | Control-unit `3` summer / `3` winter programmes; `16` summer / `16` winter scenarios | pp. 111, 113 |
| Temperature adjustment | Manual `0.5 °C` increments; remote-control enabled at control unit; sensor dial protection/`OFF` prevents local override | pp. 110-114 |
| Alarm history | Intrusion, tamper, panic and technical events with date/time/zone | p. 108 |
| Local settings | Brightness, calibration, cleaning lock, screensaver; date/time; speaker/mic volume; event ringtones; optional five-digit menu password | pp. 122-129 |
| Cleaning lock | Default `20 s`, software-customizable | p. 124 |
| Version view | Model/firmware/kernel/IP/netmask; illustrated `573962/63`, `1.1.3`, `2.3.3`, `192.168.1.110` are examples, not defaults or observations | p. 129  Published example default, not an installed address |

### Semantic review findings

The Legrand item 1809/model 48 remains separate from BTicino item 1340/model 41. Four firmware definitions expose Object `32`; UI applications are project content. Installer revisions change bundled SD capacity; the user manual also prohibits two simultaneous USB drives. Exact Legrand D/G software manuals now supply the project procedures; executable/parameter payloads remain unexamined.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `48` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Function family | Published applicability | Canonical reference / evidence |
| --- | --- | --- |
| Lighting | Individual/group on/off, individual/group dimming, configured timed light, video-entry staircase light | [`WHO 1`](../../functional/who-1-lighting/); U3970A pp. 82-83 |
| Automation | Blinds, gates, garage, irrigation, controlled sockets, fans, door locks; safe hold-to-run or standard start/stop configuration | [`WHO 2`](../../functional/who-2-automation/); pp. 79-81 |
| Scenarios | Stored scenarios with module programming/deletion; advanced time-and-device conditions; scheduled enable/disable/start/stop | [`WHO 15`](../../functional/who-15-cen/); actual host/device configuration required; pp. 84-88 |
| Sound | Source choice, radio tuning/stored stations, amplifier/group volume, per-room and multi-room/general control, local media as a source | [`WHO 16`](../../functional/who-16-sound-system/); pp. 89-92 |
| Alarm | Arm/disarm by alarm-unit user code; zone exclusion only while disarmed; alarm history/types/time/zone and deletion | [`WHO 5`](../../functional/who-5-alarm/); pp. 107-108 |
| Thermoregulation | Control-unit/zone commands, summer/winter, programmes, scenarios, manual/protection/off, holiday/weekend profiles and fancoil speed | [`WHO 4`](../../functional/who-4-temperature-control/); pp. 109-115 |
| Video entry | Answer, door release, staircase light, camera display/pan-tilt where present, intercom and bell exclusion | [`WHO 6`](../../functional/who-6-basic-video-door-entry/), [`WHO 7`](../../functional/who-7-multimedia-video/); pp. 74-76, 116-119 |
| Local/network media | USB/SD audio/video/images; configured web radio, RSS/weather, webcam views over broadband LAN | U3970A pp. 93-106; no evidence of current third-party service availability |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use MultimediaTouchScreenConfig to compose and transfer the project; use the registered brand/line parameter scope and actual firmware generation. The physical PC routes above come from the installer revisions. Rear reset is documented as restoring factory settings, without an exact hold time or preserved-data inventory. End-of-line termination and mandatory polarized local power are installation constraints. Mount the supplied bracket, position its nut at the lower end and secure the underside screw anticlockwise as the published diagrams specify.

U3970A distinguishes runtime controls from project composition. Locked scenario modules omit programming controls; scenario creation records actions then ends learning, while deletion is a separate confirmation flow. Temperature control requires the controller’s remote-control function; protected/`OFF` local sensor dials prevent overriding from the screen. Intercom/camera commands wait for a free audio/video channel; entrance-panel calls interrupt these uses. Touch cleaning/calibration changes input handling and must not be treated as protocol Object reconfiguration. Media forwarding requires the installed sound-system amplifiers and configuration.

The D software manual pp. 64-66 shows Ethernet, Serial and USB in the transfer wizard: save the project, select Download/send, set date/time, choose the actual connection and transfer; Receive loads the existing configuration for inspection/editing. D describes serial cable `49234`, crossed LAN cable and remote IP/OPEN-password use with compatible PC/device IPs. G pp. 8-9 retains send/receive, device information and `.fwz` update workflows. No firmware recovery/rollback compatibility or direct TCP endpoint is inferred.

## Source reconciliation

Installer revisions A and B agree on supply, current, `5..45 °C`, metric dimensions, battery and physical PC routes. B changes the bundled card from `512 MB` to `2 GB`, states the simultaneous-USB prohibition and expands languages; U3970A also prohibits simultaneous pen drives. Both still label USB webcam, Wi-Fi dongle and PSTN as future applications; U3970A network webcam viewing is a separate configured LAN service. No shipped USB webcam/Wi-Fi/PSTN support is inferred.

| Issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Identity and model | 67285 cover and 573962/63 screenshot support the Legrand cluster. Catalogue line Arteor for `067285` remains unresolved; no identity transfer from the BTicino model-41 dossier | Exact Legrand manuals; item `1809` |
| Firmware values | Applicability `4.0.0/3.0.0/2.0.0/1.1.0` differs from firmware-scoped FW_VER default `3.0.0` and user-manual example `1.1.3`; these are distinct metadata/example contexts | Firmware table, fields; U3970A p. 129 |
| IP defaults | Catalogue default `192.168.1.35` differs from screenshot `192.168.1.110`; screenshot is illustrative | Object `32`; U3970A p. 129 |
| PC connections | Serial is physically documented, although only Ethernet/USB have catalogue connection associations | Both installers; connection table |
| Multimedia/UI limits | Advanced audio increment wording and image Mb notation remain unresolved; no normalized byte size or uniform audio step invented | U3970A pp. 88, 94 |
| Software dossier scope | Exact Legrand French software revisions D and G are now retained and incorporated; later English user candidate 20121113_70351_1.pdf returned HTTP 403. BTicino software content is not substituted | Research `2026-10-03` |

D and G software covers name `67285`. G repeats “Local Display” in introductory/currency text despite its MultimediaTouchScreenConfig cover, so this wording does not merge products. Both French revisions use Celsius `°C` and slave addresses `1..8`; the different BTicino translation’s °F/Slave 9 errors are not imported. Both still describe an obligatory time condition at p. 44 and a conditional one at p. 45. Five software program entries differ from the older user’s three seasonal programs; software screensaver four choices differ from U3970A’s No/Default menu. G adds objectives/thresholds, notifications, alarm/video settings and ringtone authoring beyond D/older-user coverage. Serial is explicit in D’s transfer wizard, though absent from canonical connection associations. General warranty/contact text and historical PC requirements remain available in the retained originals; they do not establish current software support.

## Evidence limits and open work

- Obtain and compare newer Legrand user revisions (the Belgian publisher candidate returned HTTP 403); confirm `067285` marketed line and Arteor variant-specific installer details.
- Resolve audio condition steps, image-size notation, reset data preservation and optional port support for each firmware.
- Inspect associated parameter/package payloads and corroborate installed Object, address/configuration responses and project transfer on all three variants.
- Historical Internet services and example network/version values have no verified current service or installed-state evidence.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0101-0110-2026-10-06.md#own-dev-0107)
