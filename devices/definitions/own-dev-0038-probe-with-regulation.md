# Probe with regulation

## Summary

This zone temperature probe measures room temperature and provides local adjustment around the central setpoint. Its controls also select normal regulation, antifreeze or off, giving the user limited local control within the configured temperature system.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0038` | Project identity |
| Technical description | SCS master temperature probe with local setpoint regulation | Catalogue + `MQ00179-c-EN` |
| Commercial identities | `L/N/NT4692`, `AM5872`, `573922`, `573923`, `HC/HS/HD4692`, `067457` | Catalogue + official documentation |
| Catalogue item | `1854` | Implementation evidence |
| Main catalogue system | Temperature control | Implementation evidence |
| Item model / `modobj` | `20` | Implementation evidence |
| Firmware definition | `260` / `5.2.0` and `184` / `6.0.0` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Categories | Temperature control, HVAC, Sensor, Regulation | Capability model |

The Device is a master zone probe whose front control adjusts the zone setpoint around the central value. Both catalogue firmware lines project one fixed Master probe Object.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - LivingLight | `L/N/NT4692` | established grouped identity | catalogue + `MQ00179-c-EN` |
| BTicino - Matix | `AM5872` | established identity | catalogue + `MQ00179-c-EN` |
| BTicino - Axolute | `HC/HS/HD4692` | established grouped identity | catalogue + `MQ00179-c-EN` |
| Legrand - Arteor | `573922` | established identity | catalogue + `MQ00179-c-EN` |
| Legrand - Arteor | `573923` | established identity | catalogue + `MQ00179-c-EN` |
| Legrand - Céliane | `067457` | established identity | catalogue + `MQ00179-c-EN` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `L4692` | `8012199662084` | [Archived original](https://archive.openwebnet-ha.org/sha256/43/ec/43ec058c540f45cf0dd138ed4a2fc83b19ef6d8a9bc6062d799e601a610c42fe.pdf), `L4692-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `N4692` | `8012199662091` | [Archived original](https://archive.openwebnet-ha.org/sha256/3f/5d/3f5d4cbb4ca476461a381b4823aefed3b1ae7d57b4a4789bd7100bf7ac7abdc4.pdf), `N4692-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `NT4692` | `8012199662107` | [Archived original](https://archive.openwebnet-ha.org/sha256/42/83/4283b06329aa81ccee35beb66c6598211159b7e2eeb66c6fe5e458b8b1c43628.pdf), `NT4692-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `AM5872` | `8012199944524` | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/5e/d25ecb1f5e50bc0363c336a1e632b86d9955e9ed671bbe2b204d708e1d9e05ba.pdf), `AM5872-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HC4692` | `8012199745732` | [Archived original](https://archive.openwebnet-ha.org/sha256/00/65/00651d6923ecf5259f403bab5c512d7949c9561825e66bab439e55d4f208fe07.pdf), `HC4692-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HS4692` | `8012199745749` | [Archived original](https://archive.openwebnet-ha.org/sha256/70/bf/70bfbfe82c807a3cd7a6b4770a6dda4c4248ce6a0980191a2c6033a70e712e55.pdf), `HS4692-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HD4692` | `8012199987699` | [Archived original](https://archive.openwebnet-ha.org/sha256/00/8a/008a89f040f91eb9a7246fcc591307e24b8cad790adcd3b24f4f20873cd3136f.pdf), `HD4692-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `067457` | `3245060674571` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/d5/65/d5650667ed355f3a29ff01c7a38ee575a321b4e61249c9d60a5da13c15fe7423.pdf), `067457-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00179-c-EN` | Technical sheet | revision c / 2014-05-21 | current six-record probe family; physical operation and configuration | [Archived original](https://archive.openwebnet-ha.org/sha256/08/98/0898672f2b160b86e4c760bb696f5bda73be69ea59fc9cf33ed7694d62dd83d9.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00179_c_EN.pdf) |
| `L4692-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4692` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/43/ec/43ec058c540f45cf0dd138ed4a2fc83b19ef6d8a9bc6062d799e601a610c42fe.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4692) |
| `N4692-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `N4692` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/3f/5d/3f5d4cbb4ca476461a381b4823aefed3b1ae7d57b4a4789bd7100bf7ac7abdc4.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4692) |
| `NT4692-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `NT4692` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/42/83/4283b06329aa81ccee35beb66c6598211159b7e2eeb66c6fe5e458b8b1c43628.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4692) |
| `AM5872-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `AM5872` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/5e/d25ecb1f5e50bc0363c336a1e632b86d9955e9ed671bbe2b204d708e1d9e05ba.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5872) |
| `HC4692-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HC4692` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/00/65/00651d6923ecf5259f403bab5c512d7949c9561825e66bab439e55d4f208fe07.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4692) |
| `HS4692-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HS4692` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/70/bf/70bfbfe82c807a3cd7a6b4770a6dda4c4248ce6a0980191a2c6033a70e712e55.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4692) |
| `HD4692-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HD4692` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined in this review; electrical/temperature claims remain reference- and revision-scoped; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/00/8a/008a89f040f91eb9a7246fcc591307e24b8cad790adcd3b24f4f20873cd3136f.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4692) |
| `067457-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067457` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Exact SKU/EAN metadata examined; other technical attributes, linked downloads and prices are outside this review scope. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/d5/65/d5650667ed355f3a29ff01c7a38ee575a321b4e61249c9d60a5da13c15fe7423.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/sonde-celiane-avec-commande-de-derogation-myhome-up) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | publisher product family data |
| Local setpoint adjustment | `-3..+3 °C` around the central setpoint | `MQ00179-c-EN` |
| Local modes | normal regulation, antifreeze and `OFF` | `MQ00179-c-EN` |
| Local indicators | green/yellow status and fault LEDs | `MQ00179-c-EN` |

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply / absorption | Nominal `27 Vdc`; operating `18..27 Vdc`; `6 mA` | `MQ00179-c-EN`, printed/PDF pp. 1–3 |
| Operating temperature | `0..40 °C`; an environmental operating limit, not a verified measurement range | `MQ00179-c-EN`, printed/PDF pp. 1–3 |
| Installation height typo | The sheet literally prints `1500 m`; an apparent unit error, not a usable installation height | `MQ00179-c-EN`, printed/PDF pp. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1854` | Implementation evidence |
| Main system | Temperature control | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `20` | Implementation evidence |
| Catalogue buses | `1`, `2` | Implementation evidence |
| Commercial records | `6` | Implementation evidence |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Temperature control | `20` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `184` | `6` | `0` | `0` | `1` | Not catalogue default | Official |
| `260` | `5` | `2` | `0` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Both firmware lines remain part of the current canonical implementation source and share the same fixed Master probe Object.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No AS_FW_PACKAGE association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `184` | `1` | `184` Master probe | Fixed/designated metadata | `671` | `184` | `466` |
| `260` | `1` | `184` Master probe | Fixed/designated metadata | `1373` | `184` | `724` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

No Virgin Object relation is required for the fixed topology.

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `184` | Physical configuration | `0` | Canonical firmware/mode association |
| `184` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `184` | Advanced Configuration | `2` | Canonical firmware/mode association |
| `260` | Physical configuration | `0` | Canonical firmware/mode association |
| `260` | Virtual Configuration | `1` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `184` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `184` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `184` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `184` | `SLA` | `0..9` | `0` | `SLA`; Thermoregulation slave probe |
| `260` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `260` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `260` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `260` | `SLA` | `0..8` | `0` | `SLA`; Thermoregulation slave probe |

The `SLA` domain differs between the `5.2.0` and `6.0.0` catalogue lines and is therefore firmware-scoped rather than normalized.

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

Condition `4163` has no textual predicate. Rule `1000` translates zone digits `01..99` but has no `00` branch, although reusable `ZAZB` permits zero. Firmware `260` permits `SLA=0..8`, matching the sheet; firmware `184` permits `0..9`, exceeding its eight-slave limit. On firmware `184`, actuator-type subsets exclude ON/OFF default `0`, antifreeze values `41..80` exclude default `14`, and thermal-protection values `6..49` exclude default `70`. No replacement defaults are stored. Apply the actual restrictions; reusable display, contact, IR, proportional and PID fields do not certify physical interfaces.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `184` | `1` | `184` | `4163` | No textual predicate stored | `1000` |
| `260` | `1` | `184` | `4163` | No textual predicate stored | `1000` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `184` | `184` | `636` | `COMFORT_HEATING_SETPOINT` | `7..80` (entire reusable range retained) | `42` | Comfort heating setpoint temperature (step 0,5°C) |
| `184` | `184` | `637` | `ECO_HEATING_SETPOINT` | `6..79` (entire reusable range retained) | `36` | Eco heating setpoint temperature (step 0,5°C) |
| `184` | `184` | `638` | `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact opening |
| `184` | `184` | `639` | `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact closing |
| `184` | `184` | `640` | `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact (step 1min) |
| `184` | `184` | `641` | `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact activation (step 5s) |
| `184` | `184` | `642` | `ECO_COOLING_SETPOINT` | `7..80` (entire reusable range retained) | `56` | Eco cooling setpoint temperature (step 0,5°C) |
| `184` | `184` | `643` | `COMFORT_COOLING_SETPOINT` | `6..79` (entire reusable range retained) | `50` | Comfort cooling setpoint temperature (step 0,5°C) |
| `184` | `184` | `644` | `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact opening |
| `184` | `184` | `645` | `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact closing |
| `184` | `184` | `646` | `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for cooling contact activation (step 5s) |
| `184` | `184` | `647` | `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for cooling contact (step 1min) |
| `184` | `184` | `648` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `649` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `650` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `651` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `652` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `653` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `654` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `655` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `656` | `ACTUATOR_N=9_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `657` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Heating_actuator_type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `658` | `COOLING_ACTUATOR_TYPE` | `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Cooling_actuator_ type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `659` | `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit (entire reusable range retained) | `0` | Temperature Format |
| `184` | `184` | `662` | `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact closing activation (step 5s) |
| `184` | `184` | `663` | `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact closing (step 1min) |
| `184` | `184` | `664` | `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for Cooling contact closing activation (step 5s) |
| `184` | `184` | `665` | `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for Cooling contact closing (step 1min) |
| `184` | `184` | `666` | `BACKLIGHT_STAND_BY_LEVEL` | `0` = `OFF`; `1` = `ON` (entire reusable range retained) | `1` | Backlight stand-by level |
| `184` | `184` | `667` | `RISC` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Winter modality |
| `184` | `184` | `668` | `COND` | `0` = Disable; `1` = Enable (entire reusable range retained) | `0` | Summer modality |
| `184` | `184` | `1915` | `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED (entire reusable range retained) | `0` | Ambient temperature visualization |
| `184` | `184` | `2673` | `ANTIFREEZE_SETPOINT` | `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80` | `14` | Antifreeze; reusable default `14` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `2678` | `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Heating contact pushbutton locking |
| `184` | `184` | `2685` | `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating fancoil continuous ventilation |
| `184` | `184` | `2692` | `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `184` | `184` | `2699` | `HEATING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Heating PID regulation band (°) |
| `184` | `184` | `2706` | `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Heating PID inertia |
| `184` | `184` | `2713` | `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating proportional gain (low) |
| `184` | `184` | `2720` | `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating proportional gain (high) |
| `184` | `184` | `2727` | `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Heating integrative gain low |
| `184` | `184` | `2734` | `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Heating integrative gain high |
| `184` | `184` | `2741` | `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating derivative gain low |
| `184` | `184` | `2748` | `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating derivative gain high |
| `184` | `184` | `2755` | `HEATING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Heating proportional speed 1 (%) |
| `184` | `184` | `2762` | `HEATING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Heating proportional speed 2 (%) |
| `184` | `184` | `2769` | `HEATING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Heating proportional speed 3 (%) |
| `184` | `184` | `2776` | `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Heating pushbutton fan coil automatic speed |
| `184` | `184` | `2783` | `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating anti-seizing up protection |
| `184` | `184` | `2794` | `THERMAL_PROTECTION_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `6`; `7`; `8`; `9`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49` | `70` | Thermal protection; reusable default `70` is outside this subset; filter supplies no replacement default |
| `184` | `184` | `2799` | `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Cooling contact pushbutton locking |
| `184` | `184` | `2806` | `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling fancoil continuous ventilation |
| `184` | `184` | `2813` | `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `184` | `184` | `2820` | `COOLING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Cooling PID regulation band (°) |
| `184` | `184` | `2827` | `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Cooling PID inertia |
| `184` | `184` | `2834` | `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling proportional gain (low) |
| `184` | `184` | `2841` | `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling proportional gain (high) |
| `184` | `184` | `2848` | `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Cooling integrative gain low |
| `184` | `184` | `2855` | `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Cooling integrative gain high |
| `184` | `184` | `2862` | `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling derivative gain low |
| `184` | `184` | `2869` | `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling derivative gain high |
| `184` | `184` | `2876` | `COOLING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Cooling proportional speed 1 (%) |
| `184` | `184` | `2883` | `COOLING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Cooling proportional speed 2 (%) |
| `184` | `184` | `2890` | `COOLING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Cooling proportional speed 3 (%) |
| `184` | `184` | `2897` | `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Cooling pushbutton fan coil automatic speed |
| `184` | `184` | `2904` | `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling anti-seizing up protection |
| `184` | `184` | `2911` | `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 (entire reusable range retained) | `10` | Backlight stand-by level |
| `184` | `184` | `2918` | `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Disable all pushbuttons |
| `184` | `184` | `2925` | `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Pushbutton modality change |
| `184` | `184` | `2932` | `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Calibration procedure |
| `184` | `184` | `2939` | `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | User settings procedure |
| `184` | `184` | `2946` | `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open (entire reusable range retained) | `0` | Windows contact icon |
| `184` | `184` | `2953` | `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled (entire reusable range retained) | `0` | Windows contact number |
| `260` | `184` | `1390` | `ANTIFREEZE_SETPOINT` | `6..80` (entire reusable range retained) | `14` | Antifreeze setpoint temperature (step 0,5°C) |
| `260` | `184` | `1391` | `BACKLIGHT_STAND_BY_LEVEL` | `0` = `OFF`; `1` = `ON` (entire reusable range retained) | `1` | Backlight stand-by level |
| `260` | `184` | `1392` | `COMFORT_COOLING_SETPOINT` | `6..79` (entire reusable range retained) | `50` | Comfort cooling setpoint temperature (step 0,5°C) |
| `260` | `184` | `1393` | `COMFORT_HEATING_SETPOINT` | `7..80` (entire reusable range retained) | `42` | Comfort heating setpoint temperature (step 0,5°C) |
| `260` | `184` | `1394` | `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` (entire reusable range retained) | `6` | Cooling Fan coil speed 2 threshold (step 0,1°C) |
| `260` | `184` | `1395` | `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` (entire reusable range retained) | `10` | Cooling Fan coil speed 3 threshold (step 0,1°C) |
| `260` | `184` | `1396` | `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact closing |
| `260` | `184` | `1397` | `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact opening |
| `260` | `184` | `1398` | `COOLING_REGULATION_BAND` | `1..10` (entire reusable range retained) | `1` | Cooling regulation band (step 0,1°C) |
| `260` | `184` | `1399` | `COOLING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting (entire reusable range retained) | `0` | Cooling thresholds settings |
| `260` | `184` | `1400` | `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` (entire reusable range retained) | `0` | Cooling time lag for fan coil (step 5s) |
| `260` | `184` | `1401` | `COOLING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Cooling_actuator_ type |
| `260` | `184` | `1402` | `ECO_COOLING_SETPOINT` | `7..80` (entire reusable range retained) | `56` | Eco cooling setpoint temperature (step 0,5°C) |
| `260` | `184` | `1403` | `ECO_HEATING_SETPOINT` | `6..79` (entire reusable range retained) | `36` | Eco heating setpoint temperature (step 0,5°C) |
| `260` | `184` | `1404` | `ACTUATOR_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 1 |
| `260` | `184` | `1405` | `ACTUATOR_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 2 |
| `260` | `184` | `1406` | `ACTUATOR_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 3 |
| `260` | `184` | `1407` | `ACTUATOR_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 4 |
| `260` | `184` | `1408` | `ACTUATOR_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 5 |
| `260` | `184` | `1409` | `ACTUATOR_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 6 |
| `260` | `184` | `1410` | `ACTUATOR_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 7 |
| `260` | `184` | `1411` | `ACTUATOR_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 8 |
| `260` | `184` | `1412` | `ACTUATOR_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Function actuator 9 |
| `260` | `184` | `1413` | `FUNCTION` | `0` = Heating; `1` = Cooling; `2` = Heating & cooling (entire reusable range retained) | `0` | Function type: -Heating -Cooling -Heating & Cooling |
| `260` | `184` | `1414` | `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` (entire reusable range retained) | `6` | Heating Fan coil speed 2 threshold (step 0,1°C) |
| `260` | `184` | `1415` | `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` (entire reusable range retained) | `10` | Heating Fan coil speed 3 threshold (step 0,1°C) |
| `260` | `184` | `1416` | `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact closing |
| `260` | `184` | `1417` | `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact opening |
| `260` | `184` | `1418` | `HEATING_REGULATION_BAND` | `1..10` (entire reusable range retained) | `1` | Heating regulation band (step 0,1°C) |
| `260` | `184` | `1419` | `HEATING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting (entire reusable range retained) | `0` | Heating thresholds settings |
| `260` | `184` | `1420` | `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` (entire reusable range retained) | `0` | Heating time lag for fan coil (step 5s) |
| `260` | `184` | `1421` | `HEATING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Heating_actuator_type |
| `260` | `184` | `1422` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |
| `260` | `184` | `1424` | `PUMP_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 1 |
| `260` | `184` | `1425` | `PUMP_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 2 |
| `260` | `184` | `1426` | `PUMP_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 3 |
| `260` | `184` | `1427` | `PUMP_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 4 |
| `260` | `184` | `1428` | `PUMP_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 5 |
| `260` | `184` | `1429` | `PUMP_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 6 |
| `260` | `184` | `1430` | `PUMP_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 7 |
| `260` | `184` | `1431` | `PUMP_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 8 |
| `260` | `184` | `1432` | `PUMP_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling (entire reusable range retained) | `0` | Pump number 9 |
| `260` | `184` | `1433` | `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit (entire reusable range retained) | `0` | Temperature Format |
| `260` | `184` | `1434` | `THERMAL_PROTECTION_SETPOINT` | `6..80` (entire reusable range retained) | `70` | Thermal protection setpoint temperature (step 0,5°C) |
| `260` | `184` | `1435` | `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for cooling contact closing activation (step 5s) |
| `260` | `184` | `1436` | `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for cooling contact opening activation (step 5s) |
| `260` | `184` | `1437` | `COOLING_PUMP_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for cooling pump (step 5s) |
| `260` | `184` | `1438` | `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact closing activation (step 5s) |
| `260` | `184` | `1439` | `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact opening activation (step 5s) |
| `260` | `184` | `1440` | `HEATING_PUMP_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating pump (step 5s) |
| `260` | `184` | `1441` | `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for cooling contact closing (step 1min) |
| `260` | `184` | `1442` | `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for cooling contact opening (step 1min) |
| `260` | `184` | `1443` | `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact closing (step 1min) |
| `260` | `184` | `1444` | `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact opening (step 1min) |
| `260` | `184` | `1445` | `ACTUATOR_N=1_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 1 |
| `260` | `184` | `1446` | `ACTUATOR_N=2_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 2 |
| `260` | `184` | `1447` | `ACTUATOR_N=3_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 3 |
| `260` | `184` | `1448` | `ACTUATOR_N=4_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 4 |
| `260` | `184` | `1449` | `ACTUATOR_N=5_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 5 |
| `260` | `184` | `1450` | `ACTUATOR_N=6_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 6 |
| `260` | `184` | `1451` | `ACTUATOR_N=7_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 7 |
| `260` | `184` | `1452` | `ACTUATOR_N=8_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 8 |
| `260` | `184` | `1453` | `ACTUATOR_N=9_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control (entire reusable range retained) | `0` | Type actuator 9 |
| `260` | `184` | `1454` | `RISC` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Winter modality |
| `260` | `184` | `1455` | `COND` | `0` = Disable; `1` = Enable (entire reusable range retained) | `0` | Summer modality |
| `260` | `184` | `1916` | `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED (entire reusable range retained) | `0` | Ambient temperature visualization |
| `260` | `184` | `2679` | `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Heating contact pushbutton locking |
| `260` | `184` | `2686` | `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating fancoil continuous ventilation |
| `260` | `184` | `2693` | `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `260` | `184` | `2700` | `HEATING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Heating PID regulation band (°) |
| `260` | `184` | `2707` | `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Heating PID inertia |
| `260` | `184` | `2714` | `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating proportional gain (low) |
| `260` | `184` | `2721` | `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating proportional gain (high) |
| `260` | `184` | `2728` | `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Heating integrative gain low |
| `260` | `184` | `2735` | `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Heating integrative gain high |
| `260` | `184` | `2742` | `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating derivative gain low |
| `260` | `184` | `2749` | `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating derivative gain high |
| `260` | `184` | `2756` | `HEATING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Heating proportional speed 1 (%) |
| `260` | `184` | `2763` | `HEATING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Heating proportional speed 2 (%) |
| `260` | `184` | `2770` | `HEATING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Heating proportional speed 3 (%) |
| `260` | `184` | `2777` | `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Heating pushbutton fan coil automatic speed |
| `260` | `184` | `2784` | `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating anti-seizing up protection |
| `260` | `184` | `2800` | `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Cooling contact pushbutton locking |
| `260` | `184` | `2807` | `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling fancoil continuous ventilation |
| `260` | `184` | `2814` | `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `260` | `184` | `2821` | `COOLING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Cooling PID regulation band (°) |
| `260` | `184` | `2828` | `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Cooling PID inertia |
| `260` | `184` | `2835` | `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling proportional gain (low) |
| `260` | `184` | `2842` | `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling proportional gain (high) |
| `260` | `184` | `2849` | `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Cooling integrative gain low |
| `260` | `184` | `2856` | `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Cooling integrative gain high |
| `260` | `184` | `2863` | `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling derivative gain low |
| `260` | `184` | `2870` | `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling derivative gain high |
| `260` | `184` | `2877` | `COOLING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Cooling proportional speed 1 (%) |
| `260` | `184` | `2884` | `COOLING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Cooling proportional speed 2 (%) |
| `260` | `184` | `2891` | `COOLING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Cooling proportional speed 3 (%) |
| `260` | `184` | `2898` | `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Cooling pushbutton fan coil automatic speed |
| `260` | `184` | `2905` | `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling anti-seizing up protection |
| `260` | `184` | `2912` | `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 (entire reusable range retained) | `10` | Backlight stand-by level |
| `260` | `184` | `2919` | `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Disable all pushbuttons |
| `260` | `184` | `2926` | `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Pushbutton modality change |
| `260` | `184` | `2933` | `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Calibration procedure |
| `260` | `184` | `2940` | `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | User settings procedure |
| `260` | `184` | `2947` | `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open (entire reusable range retained) | `0` | Windows contact icon |
| `260` | `184` | `2954` | `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled (entire reusable range retained) | `0` | Windows contact number |

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
| `DIMENSION 1` | resolve `modobj = 20` and probe identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | distinguish installed `5.2.0` from `6.0.0` firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm fixed Object `184` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate the converted temperature-control zone address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration and firmware-specific `SLA` behavior | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device participates in temperature-control functions as a master zone probe. The reusable Object includes heating, cooling, mixed-mode, actuator, pump and fan-coil regulation surfaces; actual availability is firmware/filter scoped.

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| OFF priority | OFF has highest priority and must be released by the device that set it; local OFF also prevails if central unit fails. | `MQ00179-c-EN`, printed/PDF pp. 1 |
| Protection / central-unit fault | Heating selects antifreeze, cooling thermal protection; on central-unit fault retains last received temperature/season settings. | `MQ00179-c-EN`, printed/PDF pp. 1 |
| Master zone | Up to nine same-type actuators and eight slave probes; master averages its own measurement and those of slaves. | `MQ00179-c-EN`, printed/PDF pp. 1–2 |
| Load classes in this sheet | Heating, cooling or combined; ON/OFF, OPEN/CLOSE, 3-speed fan-coil. Reusable classes wider than these remain catalogue evidence. | `MQ00179-c-EN`, printed/PDF pp. 2 |

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained. The local control behavior and indicators are publisher-documented rather than inferred from the database.

## Programming

Programming must convert `ZA`/`ZB` into `ZAZB` using the catalogue conversion rule and apply the filter set for the installed firmware. Software must not silently widen firmware `260` `SLA=0..8` to the later `0..9` domain.

Configure ZA/ZB to match the zone and its actuators; physical SLA `0..8` counts slaves. The knob probe operates as master, with probe family `4693` as slave. Slave numbering starts at `1` with no gaps. Virtual configuration is documented with Virtual Configurator `2.1` when physical configurators are absent (printed/PDF p. 2).

Set heating/cooling load types, zone/pump associations and pump mode through the central unit’s Maintenance menus. The non-fan probe sheet permits pump start delay up to `9 min` according to valve opening time. Calibration uses the central unit after probes have been powered for at least `2 h` with the hydraulic system OFF and stable room temperature, compared against a calibrated thermometer (printed/PDF p. 3).

Reusable thermostat fields contain actuator/pump compatibility rules: combined actuator functions require matching heating/cooling types; fan thresholds must increase above regulation band; local opening/closing timeouts cannot both be active; zero timeout has the documented infinite meaning. Fil Pilote and gateway pump restrictions and reserved load values remain scoped to the catalogue schema, not proof of physical functionality on this knob probe.

## Source reconciliation

`MQ00179-c-EN` establishes the product family, local ±3 °C adjustment, antifreeze/`OFF` behavior and indicator semantics. The catalogue establishes two firmware lines, one fixed Object `184`, the exact `ZA`/`ZB`/`SLA` firmware surface and the large reusable Master-probe software surface.

The main catalogue difference is `SLA`: firmware `260` stores `0..8` while firmware `184` stores `0..9`. The difference remains explicitly firmware-scoped.

The sheet records removal of P/MOD/DEL sockets compared with a prior version; the exact prior revision is not retained. Its installation-height “1500 m” appears erroneous and is preserved as a source error without guessing a correction. The sheet’s physical eight-slave limit agrees with the older `5.2.x` firmware but not the `6.0.0` SLA enum reaching nine. Reusable Object `184` also includes display/UI, contact, advanced proportional/IR and PID fields not certified as physical features by the product sheet. Firmware restrictions and excluded defaults remain explicit.

## Evidence limits and open work

- Hardware-corroborate firmware selection and `DIMENSION 2` on representative 4692-family units.
- Verify the firmware-specific `SLA` limits through actual configuration reads/writes.
- Corroborate the filtered Master-probe Object surface against MyHOME Suite for both firmware lines.

- The linked central-unit installation/calibration manual and Virtual Configurator/Suite help were not inspected for this batch; procedures here are bounded to this probe sheet.
- No retained runtime data establishes the ninth-slave case, reserved reusable actuator types or physical contact/display features. An accurate installation-height revision and the earlier P/MOD/DEL hardware sheet remain unretained.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MQ00179-c-EN` archived original](https://archive.openwebnet-ha.org/sha256/08/98/0898672f2b160b86e4c760bb696f5bda73be69ea59fc9cf33ed7694d62dd83d9.pdf)

- `L4692-ean-product-sheet.pdf`, printed/PDF p. 1: exact `L4692` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/43/ec/43ec058c540f45cf0dd138ed4a2fc83b19ef6d8a9bc6062d799e601a610c42fe.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4692); SHA-256 `43ec058c540f45cf0dd138ed4a2fc83b19ef6d8a9bc6062d799e601a610c42fe`.
- `N4692-ean-product-sheet.pdf`, printed/PDF p. 1: exact `N4692` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/3f/5d/3f5d4cbb4ca476461a381b4823aefed3b1ae7d57b4a4789bd7100bf7ac7abdc4.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4692); SHA-256 `3f5d4cbb4ca476461a381b4823aefed3b1ae7d57b4a4789bd7100bf7ac7abdc4`.
- `NT4692-ean-product-sheet.pdf`, printed/PDF p. 1: exact `NT4692` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/42/83/4283b06329aa81ccee35beb66c6598211159b7e2eeb66c6fe5e458b8b1c43628.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4692); SHA-256 `4283b06329aa81ccee35beb66c6598211159b7e2eeb66c6fe5e458b8b1c43628`.
- `AM5872-ean-product-sheet.pdf`, printed/PDF p. 1: exact `AM5872` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/d2/5e/d25ecb1f5e50bc0363c336a1e632b86d9955e9ed671bbe2b204d708e1d9e05ba.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5872); SHA-256 `d25ecb1f5e50bc0363c336a1e632b86d9955e9ed671bbe2b204d708e1d9e05ba`.
- `HC4692-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HC4692` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/00/65/00651d6923ecf5259f403bab5c512d7949c9561825e66bab439e55d4f208fe07.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4692); SHA-256 `00651d6923ecf5259f403bab5c512d7949c9561825e66bab439e55d4f208fe07`.
- `HS4692-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HS4692` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/70/bf/70bfbfe82c807a3cd7a6b4770a6dda4c4248ce6a0980191a2c6033a70e712e55.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4692); SHA-256 `70bfbfe82c807a3cd7a6b4770a6dda4c4248ce6a0980191a2c6033a70e712e55`.
- `HD4692-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HD4692` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/00/8a/008a89f040f91eb9a7246fcc591307e24b8cad790adcd3b24f4f20873cd3136f.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4692); SHA-256 `008a89f040f91eb9a7246fcc591307e24b8cad790adcd3b24f4f20873cd3136f`.

- `067457-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067457` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/d5/65/d5650667ed355f3a29ff01c7a38ee575a321b4e61249c9d60a5da13c15fe7423.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/sonde-celiane-avec-commande-de-derogation-myhome-up); SHA-256 `d5650667ed355f3a29ff01c7a38ee575a321b4e61249c9d60a5da13c15fe7423`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0031-0040-2026-10-06.md#own-dev-0038)
