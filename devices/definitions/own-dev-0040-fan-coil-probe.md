# Fan-coil probe

## Summary

This room-temperature probe is designed for fan-coil zones, with local setpoint adjustment and operating-mode selection. It also lets the user choose automatic or manual fan speed, including minimum, medium and maximum settings.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0040` | Project identity |
| Technical description | SCS master temperature probe with local fan-coil speed and setpoint control | Catalogue + `MQ00181-c-EN` |
| Commercial identities | `L/N/NT4692FAN`, `573924`, `573925`, `HC/HS/HD4692FAN`, `067455` | Catalogue + official documentation |
| Catalogue item | `1856` | Implementation evidence |
| Main catalogue system | Temperature control | Implementation evidence |
| Item model / `modobj` | `19` | Implementation evidence |
| Firmware definition | `261` / `5.2.-1` and `185` / `6.0.0` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Temperature control, HVAC, Fan coil, Sensor, Regulation | Capability model |

The Device is a master temperature probe specialized for fan-coil installations. Its reusable Object is the same Master probe model used by the regulation probe, but the product adds local fan-speed interaction.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `L/N/NT4692FAN` | established grouped identity | catalogue + `MQ00181-c-EN` |
| BTicino - Axolute | `HC/HS/HD4692FAN` | established grouped identity | catalogue + `MQ00181-c-EN` |
| Legrand - Arteor | `573924` | established identity | catalogue + `MQ00181-c-EN` |
| Legrand - Arteor | `573925` | established identity | catalogue + `MQ00181-c-EN` |
| Legrand - Céliane | `067455` | established identity | catalogue + `MQ00181-c-EN` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `L4692FAN` | `8012199784526` | [Archived original](https://archive.openwebnet-ha.org/sha256/06/a1/06a19f989189cb0fac3e1904848bbce38337ce2870ee1d4298cde6afb4f419a5.pdf), `L4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `N4692FAN` | `8012199784533` | [Archived original](https://archive.openwebnet-ha.org/sha256/b8/33/b833c91f0184f022477f301ccf18670c09624c8316930c8a641a0d22e19988ed.pdf), `N4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `NT4692FAN` | `8012199784540` | [Archived original](https://archive.openwebnet-ha.org/sha256/11/d8/11d8149fa99f3c264bd65cd20ad36c5b5e26eca1cfa8370dce1280ab0f0178e2.pdf), `NT4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HC4692FAN` | `8012199823096` | [Archived original](https://archive.openwebnet-ha.org/sha256/77/0b/770b9d07a8147d1a9fad5b3311bb1f3411748d4e338dfa9522a8d17178aec1af.pdf), `HC4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HS4692FAN` | `8012199823102` | [Archived original](https://archive.openwebnet-ha.org/sha256/03/10/03102f25ebccdbcadc5f31e1dbb5085be9cda233c07805eade769c16b8b1e745.pdf), `HS4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HD4692FAN` | `8012199987705` | [Archived original](https://archive.openwebnet-ha.org/sha256/13/b0/13b0e73e25b05e2f052d1b31376ac1538d8ecaa2eadc9ce8a91c5614bbc91681.pdf), `HD4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `067455` | `3245060674557` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/7f/92/7f9289d93a1d5a56473acde0a651ba5c216b59b9814e163c0962d511d68c6eb3.pdf), `067455-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00181-c-EN` | Technical sheet | revision c / 2014-04-29 | all five current identity groups; fan-coil operation and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/05/d1/05d165146138f9a01bb959ab13afc5cda85ada4cca98deb57a92bb3c15a6d1dc.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/mq00181-c-en.pdf) |
| `L4692FAN-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4692FAN` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/06/a1/06a19f989189cb0fac3e1904848bbce38337ce2870ee1d4298cde6afb4f419a5.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4692FAN) |
| `N4692FAN-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `N4692FAN` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/b8/33/b833c91f0184f022477f301ccf18670c09624c8316930c8a641a0d22e19988ed.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4692FAN) |
| `NT4692FAN-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `NT4692FAN` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/11/d8/11d8149fa99f3c264bd65cd20ad36c5b5e26eca1cfa8370dce1280ab0f0178e2.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4692FAN) |
| `HC4692FAN-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HC4692FAN` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/77/0b/770b9d07a8147d1a9fad5b3311bb1f3411748d4e338dfa9522a8d17178aec1af.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4692FAN) |
| `HS4692FAN-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HS4692FAN` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/03/10/03102f25ebccdbcadc5f31e1dbb5085be9cda233c07805eade769c16b8b1e745.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4692FAN) |
| `HD4692FAN-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HD4692FAN` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/13/b0/13b0e73e25b05e2f052d1b31376ac1538d8ecaa2eadc9ce8a91c5614bbc91681.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4692FAN) |
| `067455-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067455` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Exact SKU/EAN metadata examined; other technical attributes, linked downloads and prices are outside this review scope. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/7f/92/7f9289d93a1d5a56473acde0a651ba5c216b59b9814e163c0962d511d68c6eb3.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/sonde-avec-commande-pour-ventilo-convecteur-myhome-up-celiane) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | publisher product family data |
| Local setpoint adjustment | `-3..+3 °C` around the central setpoint | `MQ00181-c-EN` |
| Local modes | normal regulation, antifreeze / thermal protection and `OFF` | `MQ00181-c-EN` |
| Fan control | automatic or manual fan-speed selection, including minimum / medium / maximum | `MQ00181-c-EN` |
| Local indicators | green/yellow status LEDs | `MQ00181-c-EN` |
| Zone capability | up to `9` same-type actuators and `8` slave probes in documented master configuration | `MQ00181-c-EN` |

| Property | Value | Evidence |
| --- | --- | --- |
| Nominal SCS supply / current | `27 Vdc` / `6 mA` | Retained L/N/NT/HC/HS/HD4692FAN individual exports, printed/PDF p. 1 |
| Additional fan indicators | Red automatic/manual mode LED and three red speed LEDs | `MQ00181-c-EN`, printed/PDF pp. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1856` | Implementation evidence |
| Main system | Temperature control | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `19` | Implementation evidence |
| Catalogue buses | `1`, `2` | Implementation evidence |
| Commercial records | `5` | Implementation evidence |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Temperature control | `19` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `185` | `6` | `0` | `0` | `1` | Not catalogue default | Official |
| `261` | `5` | `2` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No AS_FW_PACKAGE association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `185` | `1` | `184` Master probe | Fixed/designated metadata | `635` | `184` | `441` |
| `261` | `1` | `184` Master probe | Fixed/designated metadata | `1374` | `184` | `725` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

No Virgin Object relation is required for the fixed topology.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `185` | Physical configuration | `0` | Canonical firmware/mode association |
| `185` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `185` | Advanced Configuration | `2` | Canonical firmware/mode association |
| `261` | Physical configuration | `0` | Canonical firmware/mode association |
| `261` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `185` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `185` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `185` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `185` | `SLA` | `0..9` | `0` | `SLA`; Thermoregulation slave probe |
| `261` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `261` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `261` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `261` | `SLA` | `0..8` | `0` | `SLA`; Thermoregulation slave probe |

The default firmware `261` uses wildcard build `-1` and a narrower `SLA` domain than firmware `185`.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `184` - Master probe

| Surface | Fields | Meaning |
| --- | --- | --- |
| Sensing and operation | `FUNCTION`, `COND`, `RISC`, `NUMBER_OF_SLAVES`, `LED_ENABLE`, `TEMPERATURE_FORMAT`, `BACKLIGHT_STAND_BY_LEVEL`, `AMBIENT_TEMPERATURE_VISUALIZATION`, `BACKLIGHT_STANDBY_LEVEL`, `PUSHBUTTON_MANAGEMENT`, `PUSHBUTTON_MODALITY_CHANGE`, `CALIBRATION_PROCEDURE`, `USER_SETTINGS_PROCEDURE`, `WINDOWS_CONTACT_ICON`, `WINDOWS_CONTACT_NUMBER` | Reusable sensing, mode and presentation settings; presence in this schema is not proof of physical capability. |
| Addressing and membership | `ZAZB`, `ZAZB_CENTRAL` | Reusable addressing and group/zone scope; apply Device firmware restrictions. |
| Heating regulation | `COMFORT_HEATING_SETPOINT`, `ECO_HEATING_SETPOINT`, `ANTIFREEZE_SETPOINT`, `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL`, `HEATING_THRESHOLDS_SETTINGS`, `HEATING_REGULATION_BAND`, `HEATING_FAN_COIL_SPEED_2_THRESHOLD`, `HEATING_FAN_COIL_SPEED_3_THRESHOLD`, `HEATING_CONTACT_OPENING`, `HEATING_CONTACT_CLOSING`, `HEATING_CONTACT_OPENING_ACTIVATION_DELAY`, `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY`, `HEATING_CONTACT_OPENING_TIMEOUT`, `HEATING_CONTACT_CLOSING_TIMEOUT`, `HEATING_CONTACT_PUSHBTN_LOCK`, `HEATING_FANCOIL_VENTILATION_FUNCTION`, `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT`, `HEATING_ACTUATOR_TYPE`, `HEATING_PUMP_DELAY`, `HEATING_PID_REGULATION_BAND`, `HEATING_PID_INERTIA`, `HEATING_PROPORTIONAL_GAIN_LOW`, `HEATING_PROPORTIONAL_GAIN_HIGH`, `HEATING_INTEGRATIVE_GAIN_LOW`, `HEATING_INTEGRATIVE_GAIN_HIGH`, `HEATING_DERIVATIVE_GAIN_LOW`, `HEATING_DERIVATIVE_GAIN_HIGH`, `HEATING_PROPORTIONAL_SPEED_1`, `HEATING_PROPORTIONAL_SPEED_2`, `HEATING_PROPORTIONAL_SPEED_3`, `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED`, `HEATING_ANTI_SEIZING_UP_PROTECTION` | Heating setpoints, timing, thresholds and regulation controls; values retain their encoded units. |
| Cooling regulation | `COMFORT_COOLING_SETPOINT`, `ECO_COOLING_SETPOINT`, `THERMAL_PROTECTION_SETPOINT`, `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL`, `COOLING_THRESHOLDS_SETTINGS`, `COOLING_REGULATION_BAND`, `COOLING_FAN_COIL_SPEED_2_THRESHOLD`, `COOLING_FAN_COIL_SPEED_3_THRESHOLD`, `COOLING_CONTACT_OPENING`, `COOLING_CONTACT_CLOSING`, `COOLING_CONTACT_OPENING_ACTIVATION_DELAY`, `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY`, `COOLING_CONTACT_OPENING_TIMEOUT`, `COOLING_CONTACT_CLOSING_TIMEOUT`, `COOLING_CONTACT_PUSHBTN_LOCK`, `COOLING_FANCOIL_VENTILATION_FUNCTION`, `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT`, `COOLING_ACTUATOR_TYPE`, `COOLING_PUMP_DELAY`, `COOLING_PID_REGULATION_BAND`, `COOLING_PID_INERTIA`, `COOLING_PROPORTIONAL_GAIN_LOW`, `COOLING_PROPORTIONAL_GAIN_HIGH`, `COOLING_INTEGRATIVE_GAIN_LOW`, `COOLING_INTEGRATIVE_GAIN_HIGH`, `COOLING_DERIVATIVE_GAIN_LOW`, `COOLING_DERIVATIVE_GAIN_HIGH`, `COOLING_PROPORTIONAL_SPEED_1`, `COOLING_PROPORTIONAL_SPEED_2`, `COOLING_PROPORTIONAL_SPEED_3`, `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED`, `COOLING_ANTI_SEIZING_UP_PROTECTION` | Cooling setpoints, timing, thresholds and regulation controls; values retain their encoded units. |
| Actuators and pumps | `ACTUATOR_N=1_FUNCTION`, `ACTUATOR_N=2_FUNCTION`, `ACTUATOR_N=3_FUNCTION`, `ACTUATOR_N=4_FUNCTION`, `ACTUATOR_N=5_FUNCTION`, `ACTUATOR_N=6_FUNCTION`, `ACTUATOR_N=7_FUNCTION`, `ACTUATOR_N=8_FUNCTION`, `ACTUATOR_N=9_FUNCTION`, `ACTUATOR_N=1_TYPE`, `ACTUATOR_N=2_TYPE`, `ACTUATOR_N=3_TYPE`, `ACTUATOR_N=4_TYPE`, `ACTUATOR_N=5_TYPE`, `ACTUATOR_N=6_TYPE`, `ACTUATOR_N=7_TYPE`, `ACTUATOR_N=8_TYPE`, `ACTUATOR_N=9_TYPE`, `PUMP_N=1_FUNCTION`, `PUMP_N=2_FUNCTION`, `PUMP_N=3_FUNCTION`, `PUMP_N=4_FUNCTION`, `PUMP_N=5_FUNCTION`, `PUMP_N=6_FUNCTION`, `PUMP_N=7_FUNCTION`, `PUMP_N=8_FUNCTION`, `PUMP_N=9_FUNCTION` | Logical associations and load classes, with cross-field validity requirements retained below. |

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `FUNCTION` | `0` = Heating; `1` = Cooling; `2` = Heating & cooling | `0` | Function type |
| `ZAZB` | `00..99` | `01` | Zone |
| `COND` | `0` = Disable; `1` = Enable | `0` | Summer modality |
| `RISC` | `0` = Disable; `1` = Enable | `1` | Winter modality |
| `ZAZB_CENTRAL` | `00..99` | `01` | Temperature Control unit address |
| `COMFORT_HEATING_SETPOINT` | `7..80` | `42` | Comfort; Comfort heating setpoint > Eco heating setpoint |
| `ECO_HEATING_SETPOINT` | `6..79` | `36` | Eco; Eco heating setpoint < Comfort heating setpoint |
| `ANTIFREEZE_SETPOINT` | `6..80` | `14` | Antifreeze |
| `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Heating fan delay; checked only if "Heating actuator type" is set to one of values related to fan coil |
| `HEATING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Automatic heating thresholds settings; For automatic, while checking configuration, set parameters 8, 9, 10 according to device specific settings. |
| `HEATING_REGULATION_BAND` | `1..10` | `1` | Heating setpoint allowance |
| `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 2 threshold > Heating regulation band |
| `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 3 threshold > Heating Fan coil speed 2 threshold |
| `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact opening; If parameter "Heating contact opening" is set to 0, 4, parameter "Heating contact opening timeout" must be set to 0." If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact opening must be different from 5...25. |
| `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact closing; If parameter "Heating contact closing" is set to 0, 4, parameter "Heating contact closing timeout" must be set to 0." If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact closing must be different from 5...25. |
| `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact opening |
| `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact closing |
| `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter "Heating contact opening timeout" is different from 0, "Heating contact closing timeout" must be set to 0. |
| `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact closing action; 0 corresponds to infinite. If parameter "Heating contact closing timeout" is different from 0, "Heating contact opening timeout" must be set to 0." |
| `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed | `0` | Heating contact pushbutton locking |
| `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Heating fancoil continuous ventilation |
| `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `COMFORT_COOLING_SETPOINT` | `6..79` | `50` | Comfort; Comfort cooling setpoint < Eco cooling setpoint |
| `ECO_COOLING_SETPOINT` | `7..80` | `56` | Eco; Eco cooling setpoint > Comfort cooling setpoint |
| `THERMAL_PROTECTION_SETPOINT` | `6..80` | `70` | Thermal protection |
| `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Cooling fan delay; Checked only if "Cooling actuator type" is set to one of values related to fan coil |
| `COOLING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Automatic cooling thresholds settings; For automatic, while checking configuration, set 28, 29, 30 according to device specific settings. |
| `COOLING_REGULATION_BAND` | `1..10` | `1` | Cooling setpoint allowance |
| `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 2 threshold > Cooling regulation band |
| `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 3 threshold > Cooling Fan coil speed 2 threshold |
| `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact opening; If parameter Cooling contact opening is set to 0, 4, parameter Cooling contact opening timeout must be set to 0. |
| `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact closing; If parameter "Cooling contact closing" is set to 0, 4, parameter "Cooling contact closing timeout" must be set to 0. |
| `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Timeout for local contact opening action |
| `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Timeout for local contact closing action |
| `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter "Cooling contact opening timeout" is different from 0, "Cooling contact closing timeout" must be set to 0. |
| `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact closing action; 0 corresponds to infinite. If parameter Cooling contact closing timeout is different from 0, Cooling contact opening timeout must be set to 0. |
| `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed | `0` | Cooling contact pushbutton locking |
| `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Cooling fancoil continuous ventilation |
| `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `ACTUATOR_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 1 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 2 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 3 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 4 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 5 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 6 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 7 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 8 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 9 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=1_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=2_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=3_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=4_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=5_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=6_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=7_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=8_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=9_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `HEATING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Load type; The highlighted values must not be implemented into key object (they are dedicated to future use). |
| `COOLING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Load type; The highlighted values must not be implemented into key object (they are dedicated to future use). |
| `PUMP_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 1 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 2 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 3 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 4 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 5 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 6 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 7 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 8 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 9 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `HEATING_PUMP_DELAY` | `0..255` | `0` | Time delay for heating pumps |
| `COOLING_PUMP_DELAY` | `0..255` | `0` | Time delay for cooling pumps |
| `NUMBER_OF_SLAVES` | `0..9` | `0` | Number of slave probes |
| `LED_ENABLE` | `0` = Enabled; `1` = Disabled | `0` | Led enable |
| `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit | `0` | Temperature format |
| `BACKLIGHT_STAND_BY_LEVEL` | `0` = `OFF`; `1` = `ON` | `1` | Display standby backlight |
| `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED | `0` | Ambient temperature visualization |
| `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 | `10` | Backlight stand-by level |
| `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled | `0` | Disable all pushbuttons |
| `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled | `0` | Pushbutton modality change |
| `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled | `0` | Calibration procedure |
| `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled | `0` | User settings procedure |
| `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open | `0` | Windows contact icon |
| `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled | `0` | Windows contact number |
| `HEATING_PID_REGULATION_BAND` | `6..30` | `16` | Heating PID regulation band (°) |
| `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia | `1` | Heating PID inertia |
| `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` | `100` | Heating proportional gain (low) |
| `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` | `0` | Heating proportional gain (high) |
| `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` | `5` | Heating integrative gain low |
| `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` | `0` | Heating integrative gain high |
| `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` | `100` | Heating derivative gain low |
| `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` | `0` | Heating derivative gain high |
| `HEATING_PROPORTIONAL_SPEED_1` | `1..98` | `33` | Heating proportional speed 1 (%) |
| `HEATING_PROPORTIONAL_SPEED_2` | `2..99` | `67` | Heating proportional speed 2 (%) |
| `HEATING_PROPORTIONAL_SPEED_3` | `3..100` | `100` | Heating proportional speed 3 (%) |
| `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled | `0` | Heating pushbutton fan coil automatic speed |
| `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled | `1` | Heating anti-seizing up protection |
| `COOLING_PID_REGULATION_BAND` | `6..30` | `16` | Cooling PID regulation band (°) |
| `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia | `1` | Cooling PID inertia |
| `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` | `100` | Cooling proportional gain (low) |
| `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` | `0` | Cooling proportional gain (high) |
| `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` | `5` | Cooling integrative gain low |
| `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` | `0` | Cooling integrative gain high |
| `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` | `100` | Cooling derivative gain low |
| `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` | `0` | Cooling derivative gain high |
| `COOLING_PROPORTIONAL_SPEED_1` | `1..98` | `33` | Cooling proportional speed 1 (%) |
| `COOLING_PROPORTIONAL_SPEED_2` | `2..99` | `67` | Cooling proportional speed 2 (%) |
| `COOLING_PROPORTIONAL_SPEED_3` | `3..100` | `100` | Cooling proportional speed 3 (%) |
| `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled | `0` | Cooling pushbutton fan coil automatic speed |
| `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled | `1` | Cooling anti-seizing up protection |

### Device-specific interpretation

Firmware `185` restricts `ZAZB` and `ZAZB_CENTRAL` to `0`, conflicting with rule `1000`, which maps only `01..99`, and their reusable defaults `01`. Its antifreeze subset `41..80` excludes default `14`, thermal-protection subset `6..49` excludes default `70`, and actuator-type subsets exclude ON/OFF default `0`. No replacement defaults are stored. Firmware `261` retains broader reusable ranges and `SLA=0..8`; firmware `185` permits `0..9` despite the published eight-slave limit. Validate the installed firmware and its restricted domains before presenting these values as usable configuration.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `185` | `1` | `184` | `4163` | No textual predicate stored | `1000` |
| `261` | `1` | `184` | `4163` | No textual predicate stored | `1000` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `185` | `184` | `507` | `COMFORT_HEATING_SETPOINT` | `7..80` (entire reusable range retained) | `42` | Comfort heating setpoint temperature (step 0,5°C) |
| `185` | `184` | `508` | `ECO_HEATING_SETPOINT` | `6..79` (entire reusable range retained) | `36` | Eco heating setpoint temperature (step 0,5°C) |
| `185` | `184` | `509` | `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact opening |
| `185` | `184` | `510` | `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact closing |
| `185` | `184` | `511` | `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact activation (step 5s) |
| `185` | `184` | `512` | `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact (step 1min) |
| `185` | `184` | `513` | `ECO_COOLING_SETPOINT` | `7..80` (entire reusable range retained) | `56` | Eco cooling setpoint temperature (step 0,5°C) |
| `185` | `184` | `514` | `COMFORT_COOLING_SETPOINT` | `6..79` (entire reusable range retained) | `50` | Comfort cooling setpoint temperature (step 0,5°C) |
| `185` | `184` | `515` | `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact opening |
| `185` | `184` | `516` | `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact closing |
| `185` | `184` | `517` | `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for cooling contact activation (step 5s) |
| `185` | `184` | `518` | `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for cooling contact (step 1min) |
| `185` | `184` | `519` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `520` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `521` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `522` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `523` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `524` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `525` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `526` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `527` | `ACTUATOR_N=9_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `528` | `COOLING_ACTUATOR_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Cooling_actuator_ type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `529` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Heating_actuator_type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `530` | `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit (entire reusable range retained) | `0` | Temperature Format |
| `185` | `184` | `531` | `ZAZB` | `0` | `01` | Thermoregulation Zone; reusable default `01` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `532` | `ZAZB_CENTRAL` | `0` | `01` | Thermoregolation control unit address; reusable default `01` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `533` | `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact closing activation (step 5s) |
| `185` | `184` | `534` | `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact closing (step 1min) |
| `185` | `184` | `535` | `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for Cooling contact closing activation (step 5s) |
| `185` | `184` | `536` | `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for Cooling contact closing (step 1min) |
| `185` | `184` | `537` | `BACKLIGHT_STAND_BY_LEVEL` | `0` = `OFF`; `1` = `ON` (entire reusable range retained) | `1` | Backlight stand-by level |
| `185` | `184` | `538` | `RISC` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Winter modality |
| `185` | `184` | `539` | `COND` | `0` = Disable; `1` = Enable (entire reusable range retained) | `0` | Summer modality |
| `185` | `184` | `1913` | `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED (entire reusable range retained) | `0` | Ambient temperature visualization |
| `185` | `184` | `2671` | `ANTIFREEZE_SETPOINT` | `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80` | `14` | Antifreeze; reusable default `14` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `2676` | `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Heating contact pushbutton locking |
| `185` | `184` | `2683` | `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating fancoil continuous ventilation |
| `185` | `184` | `2690` | `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `185` | `184` | `2697` | `HEATING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Heating PID regulation band (°) |
| `185` | `184` | `2704` | `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Heating PID inertia |
| `185` | `184` | `2711` | `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating proportional gain (low) |
| `185` | `184` | `2718` | `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating proportional gain (high) |
| `185` | `184` | `2725` | `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Heating integrative gain low |
| `185` | `184` | `2732` | `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Heating integrative gain high |
| `185` | `184` | `2739` | `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating derivative gain low |
| `185` | `184` | `2746` | `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating derivative gain high |
| `185` | `184` | `2753` | `HEATING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Heating proportional speed 1 (%) |
| `185` | `184` | `2760` | `HEATING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Heating proportional speed 2 (%) |
| `185` | `184` | `2767` | `HEATING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Heating proportional speed 3 (%) |
| `185` | `184` | `2774` | `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Heating pushbutton fan coil automatic speed |
| `185` | `184` | `2781` | `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating anti-seizing up protection |
| `185` | `184` | `2792` | `THERMAL_PROTECTION_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `6`; `7`; `8`; `9` | `70` | Thermal protection; reusable default `70` is outside this subset; filter supplies no replacement default |
| `185` | `184` | `2797` | `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Cooling contact pushbutton locking |
| `185` | `184` | `2804` | `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling fancoil continuous ventilation |
| `185` | `184` | `2811` | `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `185` | `184` | `2818` | `COOLING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Cooling PID regulation band (°) |
| `185` | `184` | `2825` | `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Cooling PID inertia |
| `185` | `184` | `2832` | `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling proportional gain (low) |
| `185` | `184` | `2839` | `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling proportional gain (high) |
| `185` | `184` | `2846` | `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Cooling integrative gain low |
| `185` | `184` | `2853` | `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Cooling integrative gain high |
| `185` | `184` | `2860` | `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling derivative gain low |
| `185` | `184` | `2867` | `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling derivative gain high |
| `185` | `184` | `2874` | `COOLING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Cooling proportional speed 1 (%) |
| `185` | `184` | `2881` | `COOLING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Cooling proportional speed 2 (%) |
| `185` | `184` | `2888` | `COOLING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Cooling proportional speed 3 (%) |
| `185` | `184` | `2895` | `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Cooling pushbutton fan coil automatic speed |
| `185` | `184` | `2902` | `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling anti-seizing up protection |
| `185` | `184` | `2909` | `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 (entire reusable range retained) | `10` | Backlight stand-by level |
| `185` | `184` | `2916` | `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Disable all pushbuttons |
| `185` | `184` | `2923` | `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Pushbutton modality change |
| `185` | `184` | `2930` | `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Calibration procedure |
| `185` | `184` | `2937` | `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | User settings procedure |
| `185` | `184` | `2944` | `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open (entire reusable range retained) | `0` | Windows contact icon |
| `185` | `184` | `2951` | `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled (entire reusable range retained) | `0` | Windows contact number |
| `261` | `184` | `1456` | `ANTIFREEZE_SETPOINT` | `6..80` (entire reusable range retained) | `14` | Antifreeze setpoint temperature (step 0,5°C) |
| `261` | `184` | `1457` | `BACKLIGHT_STAND_BY_LEVEL` | `0` = `OFF`; `1` = `ON` (entire reusable range retained) | `1` | Backlight stand-by level |
| `261` | `184` | `1458` | `COMFORT_COOLING_SETPOINT` | `6..79` (entire reusable range retained) | `50` | Comfort cooling setpoint temperature (step 0,5°C) |
| `261` | `184` | `1459` | `COMFORT_HEATING_SETPOINT` | `7..80` (entire reusable range retained) | `42` | Comfort heating setpoint temperature (step 0,5°C) |
| `261` | `184` | `1460` | `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` (entire reusable range retained) | `6` | Cooling Fan coil speed 2 threshold (step 0,1°C) |
| `261` | `184` | `1461` | `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` (entire reusable range retained) | `10` | Cooling Fan coil speed 3 threshold (step 0,1°C) |
| `261` | `184` | `1462` | `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact closing |
| `261` | `184` | `1463` | `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact opening |
| `261` | `184` | `1464` | `COOLING_REGULATION_BAND` | `1..10` (entire reusable range retained) | `1` | Cooling regulation band (step 0,1°C) |
| `261` | `184` | `1465` | `COOLING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting (entire reusable range retained) | `0` | Cooling thresholds settings |
| `261` | `184` | `1466` | `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` (entire reusable range retained) | `0` | Cooling time lag for fan coil (step 5s) |
| `261` | `184` | `1467` | `COOLING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Cooling_actuator_ type |
| `261` | `184` | `1468` | `ECO_COOLING_SETPOINT` | `7..80` (entire reusable range retained) | `56` | Eco cooling setpoint temperature (step 0,5°C) |
| `261` | `184` | `1469` | `ECO_HEATING_SETPOINT` | `6..79` (entire reusable range retained) | `36` | Eco heating setpoint temperature (step 0,5°C) |
| `261` | `184` | `1470` | `ACTUATOR_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 1 |
| `261` | `184` | `1471` | `ACTUATOR_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 2 |
| `261` | `184` | `1472` | `ACTUATOR_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 3 |
| `261` | `184` | `1473` | `ACTUATOR_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 4 |
| `261` | `184` | `1474` | `ACTUATOR_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 5 |
| `261` | `184` | `1475` | `ACTUATOR_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 6 |
| `261` | `184` | `1476` | `ACTUATOR_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 7 |
| `261` | `184` | `1477` | `ACTUATOR_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 8 |
| `261` | `184` | `1478` | `ACTUATOR_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 9 |
| `261` | `184` | `1479` | `FUNCTION` | `0` = Heating; `1` = Cooling; `2` = Heating & cooling (entire reusable range retained) | `0` | Function type: -Heating -Cooling -Heating & Cooling |
| `261` | `184` | `1480` | `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` (entire reusable range retained) | `6` | Heating Fan coil speed 2 threshold (step 0,1°C) |
| `261` | `184` | `1481` | `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` (entire reusable range retained) | `10` | Heating Fan coil speed 3 threshold (step 0,1°C) |
| `261` | `184` | `1482` | `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact closing |
| `261` | `184` | `1483` | `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact opening |
| `261` | `184` | `1484` | `HEATING_REGULATION_BAND` | `1..10` (entire reusable range retained) | `1` | Heating regulation band (step 0,1°C) |
| `261` | `184` | `1485` | `HEATING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting (entire reusable range retained) | `0` | Heating thresholds settings |
| `261` | `184` | `1486` | `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` (entire reusable range retained) | `0` | Heating time lag for fan coil (step 5s) |
| `261` | `184` | `1487` | `HEATING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Heating_actuator_type |
| `261` | `184` | `1488` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |
| `261` | `184` | `1489` | `PUMP_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 1 |
| `261` | `184` | `1490` | `PUMP_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 2 |
| `261` | `184` | `1491` | `PUMP_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 3 |
| `261` | `184` | `1492` | `PUMP_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 4 |
| `261` | `184` | `1493` | `PUMP_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 5 |
| `261` | `184` | `1494` | `PUMP_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 6 |
| `261` | `184` | `1495` | `PUMP_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 7 |
| `261` | `184` | `1496` | `PUMP_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 8 |
| `261` | `184` | `1497` | `PUMP_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 9 |
| `261` | `184` | `1498` | `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit (entire reusable range retained) | `0` | Temperature Format |
| `261` | `184` | `1499` | `THERMAL_PROTECTION_SETPOINT` | `6..80` (entire reusable range retained) | `70` | Thermal protection setpoint temperature (step 0,5°C) |
| `261` | `184` | `1500` | `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for cooling contact closing activation (step 5s) |
| `261` | `184` | `1501` | `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for cooling contact opening activation (step 5s) |
| `261` | `184` | `1502` | `COOLING_PUMP_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for cooling pump (step 5s) |
| `261` | `184` | `1503` | `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact closing activation (step 5s) |
| `261` | `184` | `1504` | `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact opening activation (step 5s) |
| `261` | `184` | `1505` | `HEATING_PUMP_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating pump (step 5s) |
| `261` | `184` | `1506` | `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for cooling contact closing (step 1min) |
| `261` | `184` | `1507` | `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for cooling contact opening (step 1min) |
| `261` | `184` | `1508` | `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact closing (step 1min) |
| `261` | `184` | `1509` | `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact opening (step 1min) |
| `261` | `184` | `1510` | `ACTUATOR_N=1_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 1 |
| `261` | `184` | `1511` | `ACTUATOR_N=2_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 2 |
| `261` | `184` | `1512` | `ACTUATOR_N=3_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 3 |
| `261` | `184` | `1513` | `ACTUATOR_N=4_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 4 |
| `261` | `184` | `1514` | `ACTUATOR_N=5_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 5 |
| `261` | `184` | `1515` | `ACTUATOR_N=6_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 6 |
| `261` | `184` | `1516` | `ACTUATOR_N=7_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 7 |
| `261` | `184` | `1517` | `ACTUATOR_N=8_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 8 |
| `261` | `184` | `1518` | `ACTUATOR_N=9_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 9 |
| `261` | `184` | `1520` | `RISC` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Winter modality |
| `261` | `184` | `1521` | `COND` | `0` = Disable; `1` = Enable (entire reusable range retained) | `0` | Summer modality |
| `261` | `184` | `1917` | `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED (entire reusable range retained) | `0` | Ambient temperature visualization |
| `261` | `184` | `2680` | `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Heating contact pushbutton locking |
| `261` | `184` | `2687` | `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating fancoil continuous ventilation |
| `261` | `184` | `2694` | `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `261` | `184` | `2701` | `HEATING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Heating PID regulation band (°) |
| `261` | `184` | `2708` | `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Heating PID inertia |
| `261` | `184` | `2715` | `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating proportional gain (low) |
| `261` | `184` | `2722` | `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating proportional gain (high) |
| `261` | `184` | `2729` | `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Heating integrative gain low |
| `261` | `184` | `2736` | `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Heating integrative gain high |
| `261` | `184` | `2743` | `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating derivative gain low |
| `261` | `184` | `2750` | `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating derivative gain high |
| `261` | `184` | `2757` | `HEATING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Heating proportional speed 1 (%) |
| `261` | `184` | `2764` | `HEATING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Heating proportional speed 2 (%) |
| `261` | `184` | `2771` | `HEATING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Heating proportional speed 3 (%) |
| `261` | `184` | `2778` | `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Heating pushbutton fan coil automatic speed |
| `261` | `184` | `2785` | `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating anti-seizing up protection |
| `261` | `184` | `2801` | `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Cooling contact pushbutton locking |
| `261` | `184` | `2808` | `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling fancoil continuous ventilation |
| `261` | `184` | `2815` | `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `261` | `184` | `2822` | `COOLING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Cooling PID regulation band (°) |
| `261` | `184` | `2829` | `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Cooling PID inertia |
| `261` | `184` | `2836` | `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling proportional gain (low) |
| `261` | `184` | `2843` | `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling proportional gain (high) |
| `261` | `184` | `2850` | `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Cooling integrative gain low |
| `261` | `184` | `2857` | `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Cooling integrative gain high |
| `261` | `184` | `2864` | `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling derivative gain low |
| `261` | `184` | `2871` | `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling derivative gain high |
| `261` | `184` | `2878` | `COOLING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Cooling proportional speed 1 (%) |
| `261` | `184` | `2885` | `COOLING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Cooling proportional speed 2 (%) |
| `261` | `184` | `2892` | `COOLING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Cooling proportional speed 3 (%) |
| `261` | `184` | `2899` | `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Cooling pushbutton fan coil automatic speed |
| `261` | `184` | `2906` | `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling anti-seizing up protection |
| `261` | `184` | `2913` | `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 (entire reusable range retained) | `10` | Backlight stand-by level |
| `261` | `184` | `2920` | `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Disable all pushbuttons |
| `261` | `184` | `2927` | `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Pushbutton modality change |
| `261` | `184` | `2934` | `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Calibration procedure |
| `261` | `184` | `2941` | `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | User settings procedure |
| `261` | `184` | `2948` | `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open (entire reusable range retained) | `0` | Windows contact icon |
| `261` | `184` | `2955` | `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled (entire reusable range retained) | `0` | Windows contact number |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1000` | `ZA=0; ZB=1..9` | `ZAZB=01..09` | Rule `1000` through branch `1001` |
| `1000` | `ZA=1..9; ZB=0..9` | `ZAZB=10..99` | Rule `1000` through branches `1002..1010` |
| `1000` | `ZA=0; ZB=0` | No `00` mapping stored | Do not widen the conversion from the reusable Object domain |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve `modobj = 19` and fan-coil probe identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | distinguish installed `5.2` versus `6.0` firmware and wildcard build applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm fixed Object `184` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate converted zone address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration and firmware-specific fan-coil/`SLA` constraints | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device participates in temperature-control functions for fan-coil zones. The publisher additionally documents local automatic/manual fan-speed control and master operation with multiple actuators and slave probes.

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| OFF priority | OFF has highest priority and must be released by the device that set it; local OFF also prevails if central unit fails. | `MQ00181-c-EN`, printed/PDF pp. 1 |
| Protection / central-unit fault | Heating selects antifreeze, cooling thermal protection; on central-unit fault retains last received temperature/season settings. | `MQ00181-c-EN`, printed/PDF pp. 1 |
| Master zone | Up to nine same-type actuators and eight slave probes; master averages its own measurement and those of slaves. | `MQ00181-c-EN`, printed/PDF pp. 1–2 |
| Load classes in this sheet | Heating, cooling or combined; ON/OFF, OPEN/CLOSE, 3-speed fan-coil and GATEWAY; specifically 3-speed/Climaveneta fan-coil management. Reusable classes wider than these remain catalogue evidence. | `MQ00181-c-EN`, printed/PDF pp. 2 |

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained. Fan-speed behavior, local setpoint adjustment and master-zone capability are publisher-documented and still need protocol-level corroboration.

## Programming

Programming must apply the installed firmware's filter set, convert `ZA`/`ZB` to `ZAZB` and preserve the `SLA` difference between firmware lines. Fan-coil controls should be exposed only where their relation-specific filters permit them.

Configure ZA/ZB to match the zone and its actuators; physical SLA `0..8` counts slaves. The knob probe operates as master, with probe family `4693` as slave. Slave numbering starts at `1` with no gaps. Virtual configuration is documented with Virtual Configurator `2.1` when physical configurators are absent (printed/PDF p. 2).

Set heating/cooling load types, zone/pump associations and pump mode through the central unit’s Maintenance menus. The fan probe sheet permits a pump start delay but does not give a numeric limit. Calibration uses the central unit after probes have been powered for at least `2 h` with the hydraulic system OFF and stable room temperature, compared against a calibrated thermometer (printed/PDF p. 3).

Reusable thermostat fields contain actuator/pump compatibility rules: combined actuator functions require matching heating/cooling types; fan thresholds must increase above regulation band; local opening/closing timeouts cannot both be active; zero timeout has the documented infinite meaning. Fil Pilote and gateway pump restrictions and reserved load values remain scoped to the catalogue schema, not proof of physical functionality on this knob probe.

## Source reconciliation

`MQ00181-c-EN` establishes the fan-coil product family, local ±3 °C setpoint adjustment, fan-speed controls, indicators and master-zone capabilities. The catalogue establishes the two firmware lines, fixed Object `184`, `ZA`/`ZB`/`SLA` surface, zone conversion and relation-specific filtered Master-probe configuration.

As with the non-fan probe, `SLA` differs by firmware: `0..8` on firmware `261` and `0..9` on firmware `185`. Firmware `261` also uses build sentinel `-1` rather than a concrete build number.

The fan sheet has no electrical or environmental technical-data table: nominal supply/current are instead supported by the retained exact-reference exports. The previously stated measurement range was unsupported and has been removed. The sheet’s physical eight-slave limit agrees with the older `5.2.x` firmware but not the `6.0.0` SLA enum reaching nine. Reusable Object `184` also includes display/UI, contact, advanced proportional/IR and PID fields not certified as physical features by the product sheet. Firmware restrictions and excluded defaults remain explicit.

## Evidence limits and open work

- Hardware-corroborate automatic/manual fan-speed behavior and the exposed Object fields.
- Confirm installed build reporting for firmware `261` rather than interpreting catalogue `-1` as a runtime value.
- Verify `SLA` limits and relation-specific fan-coil filters through configuration reads/writes.

- The linked central-unit installation/calibration manual and Virtual Configurator/Suite help were not inspected for this batch; procedures here are bounded to this probe sheet.
- No retained runtime data establishes the ninth-slave case, reserved reusable actuator types or physical contact/display features. An exact fan-probe environmental operating/measurement range is not established by the examined sheets.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MQ00181-c-EN` archived original](https://archive.openwebnet-ha.org/sha256/05/d1/05d165146138f9a01bb959ab13afc5cda85ada4cca98deb57a92bb3c15a6d1dc.pdf)

- `L4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1: exact `L4692FAN` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/06/a1/06a19f989189cb0fac3e1904848bbce38337ce2870ee1d4298cde6afb4f419a5.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4692FAN); SHA-256 `06a19f989189cb0fac3e1904848bbce38337ce2870ee1d4298cde6afb4f419a5`.
- `N4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1: exact `N4692FAN` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/b8/33/b833c91f0184f022477f301ccf18670c09624c8316930c8a641a0d22e19988ed.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4692FAN); SHA-256 `b833c91f0184f022477f301ccf18670c09624c8316930c8a641a0d22e19988ed`.
- `NT4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1: exact `NT4692FAN` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/11/d8/11d8149fa99f3c264bd65cd20ad36c5b5e26eca1cfa8370dce1280ab0f0178e2.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4692FAN); SHA-256 `11d8149fa99f3c264bd65cd20ad36c5b5e26eca1cfa8370dce1280ab0f0178e2`.
- `HC4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HC4692FAN` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/77/0b/770b9d07a8147d1a9fad5b3311bb1f3411748d4e338dfa9522a8d17178aec1af.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4692FAN); SHA-256 `770b9d07a8147d1a9fad5b3311bb1f3411748d4e338dfa9522a8d17178aec1af`.
- `HS4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HS4692FAN` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/03/10/03102f25ebccdbcadc5f31e1dbb5085be9cda233c07805eade769c16b8b1e745.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4692FAN); SHA-256 `03102f25ebccdbcadc5f31e1dbb5085be9cda233c07805eade769c16b8b1e745`.
- `HD4692FAN-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HD4692FAN` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/13/b0/13b0e73e25b05e2f052d1b31376ac1538d8ecaa2eadc9ce8a91c5614bbc91681.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4692FAN); SHA-256 `13b0e73e25b05e2f052d1b31376ac1538d8ecaa2eadc9ce8a91c5614bbc91681`.

- `067455-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067455` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/7f/92/7f9289d93a1d5a56473acde0a651ba5c216b59b9814e163c0962d511d68c6eb3.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/sonde-avec-commande-pour-ventilo-convecteur-myhome-up-celiane); SHA-256 `7f9289d93a1d5a56473acde0a651ba5c216b59b9814e163c0962d511d68c6eb3`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0031-0040-2026-10-06.md#own-dev-0040)
