# Display thermostat 2 modules

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0046` | Project identity |
| Technical description | Display thermostat 2 modules | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `H4691`, `LN4691`, `067459`, `64170` | Canonical commercial records |
| Catalogue item | `1686` | Canonical catalogue |
| Main catalogue system | Temperature control | Canonical catalogue |
| Item model / `modobj` | `6` | Canonical inventory |
| Firmware definition | `1.0.-1`; `2.0.0` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Temperature control, HVAC, Thermostat | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4691` | established catalogue identity for item `1686` | canonical commercial record |
| BTicino - LivingLight | `LN4691` | established catalogue identity for item `1686` | canonical commercial record |
| Legrand - Céliane | `067459` | established catalogue identity for item `1686` | canonical commercial record |
| Arnould - Espace Evolution | `64170` | established catalogue identity for item `1686` | canonical commercial record |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4691` | `8005543498040` | [Archived original](https://archive.openwebnet-ha.org/sha256/77/aa/77aa94ef9d3597fe6bf35915e3db596a8d09298d8f677e419e3846a9197d92fe.pdf), `H4691-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `LN4691` | `8005543498057` | [Archived original](https://archive.openwebnet-ha.org/sha256/ad/ce/adced5f1ae3272456c85abc178c0224f8867953120ba7e470b6f50b0335331b4.pdf), `LN4691-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00789_b_EN` | technical sheet | revision b; date not confirmed in retained metadata | `H4691` / `LN4691` / `067459` / `64170` thermostat functions and installation characteristics | [Archived original](https://archive.openwebnet-ha.org/sha256/ee/ad/eead45860c389c7bd4063c68bd8c1790407398b1b43e5554dfb0944f6bae7108.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00789_b_EN.pdf) |
| BTicino `H4691` catalogue page | product page | current catalogue | Current `H4691` electrical characteristics and product role | Not applicable - web page | [Official product page](https://catalogo.bticino.it/BTI-H4691-IT) |
| `H4691-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4691` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/77/aa/77aa94ef9d3597fe6bf35915e3db596a8d09298d8f677e419e3846a9197d92fe.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4691) |
| `LN4691-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4691` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/ad/ce/adced5f1ae3272456c85abc178c0224f8867953120ba7e470b6f50b0335331b4.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4691) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `27 Vdc` | Current BTicino `H4691` catalogue |
| Input current | `30 mA` | Current BTicino `H4691` catalogue |
| Width | 2 wiring-device modules | `MM00789_b_EN` / current catalogue |
| Local interfaces | Temperature probe, display, four keys, rear contact input | `MM00789_b_EN` |
| HVAC role | Probe, hotel thermostat, or residential thermostat; fan-coil speed management when applicable | `MM00789_b_EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1686` | Canonical catalogue |
| Technical item | Display thermostat 2 modules | Canonical catalogue |
| Main system | Temperature control | Canonical catalogue |
| Item model / `modobj` | `6` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `160` | `1` | `0` | `-1` | `1` | Catalogue default | Official |
| `691` | `2` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `160` | `1` | `184` Master probe | Fixed/designated metadata | `2095` | `184` | `877` |
| `160` | `1` | `95` Hotel thermostat | Candidate alternative | `877` | `542` | `553` |
| `160` | `1` | `96` Residential thermostat | Candidate alternative | `878` | `545` | `554` |
| `691` | `1` | `184` Master probe | Fixed/designated metadata | `2575` | `184` | `1194` |
| `691` | `1` | `95` Hotel thermostat | Candidate alternative | `2573` | `542` | `1192` |
| `691` | `1` | `96` Residential thermostat | Candidate alternative | `2574` | `545` | `1193` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `160` | `509` Thermostat virgin | `1` | `95`, `96`, `144`, `184`, `221` | `530` | `40` |
| `691` | `509` Thermostat virgin | `1` | `95`, `96`, `144`, `184`, `221` | `530` | `54` |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `160` | Advanced Configuration | supported configuration route for this Device family |
| `160` | Physical configuration | supported configuration route for this Device family |
| `160` | Virtual Configuration | supported configuration route for this Device family |
| `691` | Advanced Configuration | supported configuration route for this Device family |
| `691` | Physical configuration | supported configuration route for this Device family |
| `691` | Virtual Configuration | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `160` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `160` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `160` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `160` | `TYPE` | `0..2` | `0` | TYPE; 0 Master probe, 1 Hotel thermostat, 2 residential thermostat |
| `160` | `HEAT` | `0..9` | `0` | HEAT; (LOAD NOT USED: 0) (`ON`/`OFF`: 1) (Open/Close: 2) (2 pipes fan coil with on/off valve: 3) (Gateway: 4) (Fil Pilote: 5) (2 pipes fan coil with proportional valve: 6) (4 pipes fan coil with on/off valves: 7) (4 pipes fan coil with proportional valves: 8) (Proportional valve: 9) Heating actuator type (`N=1`) |
| `160` | `COOL` | `0..4`; `6..9`; `14` = `CEN` | `0` | COOL; Cooling actuator type (`N=2`) or (`N=1` if TYPE_C = `CEN`). If TYPE_C = `CEN`, TYPE_H must be different from FIL PILOTE and `OFF`. |
| `160` | `PUMP` | `0..4` | `0` | PUMP; (NO PUMP: 0) (PUMP `N=1` FOR HEATING ONLY: 1) (PUMP `N=2` FOR COOLING ONLY: 2) (PUMP `N=1` FOR HEATING, `N=2` FOR COOLING: 3) (PUMP `N=1` FOR HEATING AND COOLING: 4) |
| `160` | `IN` | `0..5` | `0` | IN; (DISABLED: 0) (OPEN --> PROTECTION, CLOSE --> BACK TO THE PREVIOUS STATE: 1) (OPEN --> `OFF`, CLOSE --> BACK TO THE PREVIOUS STATE: 2) (OPEN --> ECO, CLOSE --> BACK TO THE PREVIOUS STATE: 3) (OPEN --> COMFORT, CLOSE --> BACK TO THE PREVIOUS STATE: 4) (OPEN --> SWITCH TO HEATING, CLOSE --> SWITCH TO COOLING: 5) Contact function (same action for heating and cooling).If MOD = 0, contact must be different from 5. |
| `691` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `691` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `691` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `691` | `TYPE` | `0..2` | `0` | TYPE; 0 Master probe, 1 Hotel thermostat, 2 residential thermostat |
| `691` | `HEAT` | `0..9` | `0` | HEAT; (LOAD NOT USED: 0) (`ON`/`OFF`: 1) (Open/Close: 2) (2 pipes fan coil with on/off valve: 3) (Gateway: 4) (Fil Pilote: 5) (2 pipes fan coil with proportional valve: 6) (4 pipes fan coil with on/off valves: 7) (4 pipes fan coil with proportional valves: 8) (Proportional valve: 9) Heating actuator type (`N=1`) |
| `691` | `COOL` | `0..4`; `6..9`; `14` = `CEN` | `0` | COOL; Cooling actuator type (`N=2`) or (`N=1` if TYPE_C = `CEN`). If TYPE_C = `CEN`, TYPE_H must be different from FIL PILOTE and `OFF`. |
| `691` | `PUMP` | `0..4` | `0` | PUMP; (NO PUMP: 0) (PUMP `N=1` FOR HEATING ONLY: 1) (PUMP `N=2` FOR COOLING ONLY: 2) (PUMP `N=1` FOR HEATING, `N=2` FOR COOLING: 3) (PUMP `N=1` FOR HEATING AND COOLING: 4) |
| `691` | `IN` | `0..5` | `0` | IN; (DISABLED: 0) (OPEN --> PROTECTION, CLOSE --> BACK TO THE PREVIOUS STATE: 1) (OPEN --> `OFF`, CLOSE --> BACK TO THE PREVIOUS STATE: 2) (OPEN --> ECO, CLOSE --> BACK TO THE PREVIOUS STATE: 3) (OPEN --> COMFORT, CLOSE --> BACK TO THE PREVIOUS STATE: 4) (OPEN --> SWITCH TO HEATING, CLOSE --> SWITCH TO COOLING: 5) Contact function (same action for heating and cooling).If MOD = 0, contact must be different from 5. |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `184` - Master probe

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


### Object `95` - Hotel thermostat

Catalogue Object key `542` maps to external Object `95`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | Zone |
| `FUNCTION` | `0` = Heating; `1` = Cooling; `2` = Heating & cooling | `0` | Function type |
| `MAXIMUM_HEATING_SETPOINT` | `20..80` | `80` | Max; Maximum heating setpoint > Minimum heating setpoint Maximum cooling setpoint >= Maximum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). step 0.5 °C |
| `MINIMUM_HEATING_SETPOINT` | `6..79` | `6` | Min; Minimum heating setpoint = Minimum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). step 0.5 °C |
| `COMFORT_HEATING_SETPOINT` | `7..80` | `42` | Comfort; Comfort heating setpoint > Eco heating setpoint Comfort heating setpoint = Minimum heating setpoint. step 0.5 °C |
| `ECO_HEATING_SETPOINT` | `6..79` | `36` | Eco; Eco heating setpoint = Minimum heating setpoint. step 0.5 °C |
| `ANTIFREEZE_SETPOINT` | `6..80` | `14` | Antifreeze; step 0.5 °C |
| `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Heating fan delay; Checked only if "Heating actuator type" is set to one of values related to fan coil step 5 s |
| `HEATING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Automatic heating thresholds settings; For automatic, while checking configuration, set parameters 8, 9, 10 according to device specific settings. |
| `HEATING_REGULATION_BAND` | `1..10` | `1` | Heating setpoint allowance; Step 0.1°C |
| `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 2 threshold > Heating regulation band |
| `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 3 threshold > Heating Fan coil speed 2 threshold |
| `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to cooling; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact opening; If parameter "Heating contact opening" is set to 0, 3, 4, parameter "Heating contact opening timeout" must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact opening" = "Cooling contact opening". If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact opening must be different from 5...25. |
| `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to cooling; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact closing; If parameter "Heating contact closing" is set to 0, 3, 4, parameter "Heating contact closing timeout" must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact closing" = "Cooling contact closing" If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact closing must be different from 5...25. |
| `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact after opening; step 5s |
| `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact after closing; step 5 s |
| `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact after opening; 0 corresponds to infinite. If parameter "Heating contact opening timeout" is different from 0, "Heating contact closing timeout" must be set to 0." step 1 min |
| `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact after closing; 0 corresponds to infinite. If parameter "Heating contact closing timeout" is different from 0, "Heating contact opening timeout" must be set to 0. step 1 min |
| `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed | `0` | Heating contact pushbutton locking |
| `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Heating fancoil ventilation function |
| `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `MAXIMUM_COOLING_SETPOINT` | `7..80` | `80` | Max; Maximum cooling setpoint > Minimum cooling setpoint Maximum cooling setpoint >= Maximum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). step 0.5 °C |
| `MINIMUM_COOLING_SETPOINT` | `6..70` | `6` | Min; Minimum cooling setpoint = Minimum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). step 0.5 °C |
| `COMFORT_COOLING_SETPOINT` | `6..79` | `50` | Comfort; Comfort cooling setpoint = Minimum cooling setpoint. step 0.5 °C |
| `ECO_COOLING_SETPOINT` | `7..80` | `56` | Eco; Eco cooling setpoint > Comfort cooling setpoint Eco cooling setpoint = Minimum cooling setpoint. step 0.5 °C |
| `THERMAL_PROTECTION_SETPOINT` | `6..80` | `70` | Thermal protection; step 0.5 °C |
| `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Cooling fan delay; Checked only if "Cooling actuator type" is set to one of values related to fan coil step 5s |
| `COOLING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Cooling thresholds settings; For automatic, while checking configuration, set 28, 29, 30 according to device specific settings. |
| `COOLING_REGULATION_BAND` | `1..10` | `1` | Cooling setpoint allowance; step 0.1 °C |
| `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 2 threshold > Cooling regulation band |
| `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 3 threshold > Cooling Fan coil speed 2 threshold |
| `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to heating; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact opening; If parameter Cooling contact opening is set to 0,3,4, parameter Cooling contact opening timeout must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact opening" = "Cooling contact opening" |
| `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to heating; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact closing; If parameter Cooling contact closing is to set to 0,3,4, parameter cooling contact closing timeout must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact closing" = "Cooling contact closing" |
| `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact opening; step 5s |
| `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact closing; step 5s |
| `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter "Cooling contact opening timeout" is different from 0, "Cooling contact closing timeout" must be set to 0. step 1 min |
| `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact closing action; 0 corresponds to infinite. If parameter Cooling contact closing timeout is different from 0, Cooling contact opening timeout must be set to 0. step 1 min |
| `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed | `0` | Cooling contact pushbutton locking |
| `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Cooling fancoil continuous ventilation |
| `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `ACTUATOR_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 1 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 2 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 3 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 4 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 5 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 6 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 7 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 8 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 9 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=1_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=2_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=3_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=4_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=5_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=6_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=7_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=8_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=9_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `HEATING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Load type; The highlighted values must not be implemented into key object (they are dedicated to future use). In case of FIL PILOTE, "Automatic changeover Mode" must be set disabled. |
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
| `HEATING_PUMP_DELAY` | `0..255` | `0` | Time delay for heating pumps; step 5s |
| `COOLING_PUMP_DELAY` | `0..255` | `0` | Time delay for cooling pumps; step 5s |
| `NUMBER_OF_SLAVES` | `0..9` | `0` | Number of slave probes |
| `LED_ENABLE` | `0` = Enabled; `1` = Disabled | `0` | Led enable |
| `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit | `0` | Temperature format |
| `FUNCTION_CHANGE_BY_LOCAL_BUTTON` | `0` = Enabled; `1` = Disabled | `1` | Pushbutton "heating/cooling" change |
| `AUTOMATIC_CHANGEOVER_MODE` | `0` = Enabled; `1` = Disabled | `1` | Automatic changeover mode; Condition to check contact: - See notes contained into parameters "Heating contact opening", "Heating contact closing", "Cooling contact opening" and "Cooling contact closing". Condition to check fil pilote: - See note contained into parameter "Heating actuator type". Conditions to check for actuators and pumps: - There must be at least one actuator for heatng (actuator function set to "Heating only" or "Heating and Cooling") or at least one pump for heating (pump function set to "Heating only"). - There must be at least one actuator for cooling (actuator function set to "Cooling only" or "Heating and Cooling") or at least one pump for cooling (pump function set to "Cooling only"). - if at least one actuator function is set to "Heating and cooling", "Heating actuator type" (that must be equal to "Cooling actuator type") can only be equal to 7 or 8; if this condition related to "Heating actuator type" is not satisfied, there must be at least one pump function set to "Heating only" and one pump function set to "Cooling only". |
| `AUTOMATIC_CHANGEOVER_MODE_SWITCHING_THRESHOLD` | `20..50` | `20` | Automatic changeover mode switching threshold (step 0.1 °C); Hidden, used only during device developement. |
| `BACKLIGHT_STAND_BY_LEVEL` | `0` = `OFF`; `1` = `ON` | `1` | Backlight for display standby |
| `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED | `0` | Room temperature visualization |
| `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10; `11` = Automatic with off; `12` = Automatic without off | `10` | Backlight stand-by level |
| `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled | `0` | Disable all pushbuttons |
| `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled | `0` | Pushbutton modality change |
| `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled | `1` | Calibration procedure |
| `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled | `1` | User settings procedure |
| `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open | `0` | Windows contact icon |
| `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled | `0` | Windows contact number |
| `EXTERNAL_SENSOR_TYPE` | `0` = BTicino BT-3457; `1` = Vantage 8051 | `0` | External temperature sensor type |
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


### Object `96` - Residential thermostat

Catalogue Object key `545` maps to external Object `96`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | Zone |
| `FUNCTION` | `0` = Heating; `1` = Cooling; `2` = Heating & cooling | `0` | Function type: -Heating -Cooling -Heating & Cooling |
| `MAXIMUM_HEATING_SETPOINT` | `7..80` | `80` | Max; "Maximum heating setpoint > Minimum heating setpoint Maximum cooling setpoint >= Maximum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function)." 0,5 steps |
| `MINIMUM_HEATING_SETPOINT` | `6..79` | `6` | Min; Minimum heating setpoint = Minimum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). 0,5 steps |
| `COMFORT_HEATING_SETPOINT` | `7..80` | `42` | Comfort; Comfort heating setpoint > Eco heating setpoint Comfort heating setpoint = Minimum heating setpoint. 0,5 steps |
| `ECO_HEATING_SETPOINT` | `6..79` | `36` | Eco; Eco heating setpoint = Minimum heating setpoint. 0,5 steps |
| `ANTIFREEZE_SETPOINT` | `6..80` | `14` | Antifreeze; 0,5 steps |
| `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Heating fan delay; Checked only if "Heating actuator type" is set to one of values related to fan coil 0,5 steps |
| `HEATING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Automatic heating thresholds settings; For automatic, while checking configuration, set parameters 8, 9, 10 according to device specific settings. |
| `HEATING_REGULATION_BAND` | `1..10` | `1` | Heating setpoint allowance; Step 0.1 °C |
| `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 2 threshold > Heating regulation band Step 0.1°C |
| `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 3 threshold > Heating Fan coil speed 2 threshold Step 0,1°C |
| `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Antifreeze; `2` = Off; `3` = Switch to cooling; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact opening; If parameter "Heating contact opening" is set to 0, 3, 4, parameter "Heating contact opening timeout" must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact opening" = "Cooling contact opening". If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact opening must be different from 5...25. |
| `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Antifreeze; `2` = Off; `3` = Switch to cooling; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact closing; If parameter "Heating contact closing" is set to 0, 3, 4, parameter "Heating contact closing timeout" must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact closing" = "Cooling contact closing" If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact closing must be different from 5...25. |
| `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact opening; Step 5 s |
| `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact closing; Step 5 s |
| `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter "Heating contact opening timeout" is different from 0, "Heating contact closing timeout" must be set to 0." |
| `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter "Heating contact closing timeout" is different from 0, "Heating contact opening timeout" must be set to 0." step 1 min |
| `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed | `0` | Heating contact pushbutton locking |
| `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Heating fancoil continuous ventilation |
| `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `MAXIMUM_COOLING_SETPOINT` | `7..80` | `80` | Max; Maximum cooling setpoint > Minimum cooling setpoint Maximum cooling setpoint >= Maximum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). Step 0,5°C |
| `MINIMUM_COOLING_SETPOINT` | `6..70` | `6` | Min; Minimum cooling setpoint = Minimum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). Step 0,5°C |
| `COMFORT_COOLING_SETPOINT` | `6..79` | `50` | Comfort; Comfort cooling setpoint = Minimum cooling setpoint. Step 0,5°C |
| `ECO_COOLING_SETPOINT` | `7..80` | `56` | Eco; Eco cooling setpoint > Comfort cooling setpoint Eco cooling setpoint = Minimum cooling setpoint. Step 0,5°C |
| `THERMAL_PROTECTION_SETPOINT` | `6..80` | `70` | Thermal protection; Step 0.5°C |
| `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Cooling fan delay; Checked only if "Cooling actuator type" is set to one of values related to fan coil Step 5s |
| `COOLING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Automatic cooling thresholds settings; For automatic, while checking configuration, set 28, 29, 30 according to device specific settings. |
| `COOLING_REGULATION_BAND` | `1..10` | `1` | Cooling setpoint allowance; Step 0.1°C |
| `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 2 threshold > Cooling regulation band Step 0.1 °C |
| `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 3 threshold > Cooling Fan coil speed 2 threshold Step 0,1 °C |
| `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to heating; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact opening; If parameter Cooling contact opening is to set to 0,3,4, parameter cooling contact opening timeout must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact opening" = "Cooling contact opening" |
| `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to heating; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact closing; If parameter Cooling contact closing is to set to 0,3,4, parameter cooling contact closing timeout must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact closing" = "Cooling contact closing" |
| `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact opening; step 5s |
| `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact closing; step 5 s |
| `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter "Cooling contact opening timeout" is different from 0, "Cooling contact closing timeout" must be set to 0. step 1 min |
| `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter Cooling contact closing timeout is different from 0, Cooling contact opening timeout must be set to 0. step 1 min |
| `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed | `0` | Cooling contact pushbutton locking |
| `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Cooling fancoil continuous ventilation |
| `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `ACTUATOR_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Function actuator 1; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Function actuator 2; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Function actuator 3; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Function actuator 4; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Function actuator 5; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Function actuator 6; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Function actuator 7; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Function actuator 8; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Function actuator 9; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=1_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=2_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=3_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=4_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=5_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=6_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=7_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=8_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=9_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `HEATING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Load type; The highlighted values must not be implemented into key object (they are dedicated to future use). In case of FIL PILOTE, "Automatic changeover Mode" must be set disabled. |
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
| `HEATING_PUMP_DELAY` | `0..255` | `0` | Time delay for heating pumps; step 5s |
| `COOLING_PUMP_DELAY` | `0..255` | `0` | Time delay for cooling pump; step 5s |
| `NUMBER_OF_SLAVES` | `0..9` | `0` | Number of slave probes |
| `LED_ENABLE` | `0` = Enabled; `1` = Disabled | `0` | Led enable |
| `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit | `0` | Temperature format |
| `FUNCTION_CHANGE_BY_LOCAL_BUTTON` | `0` = Enabled; `1` = Disabled | `0` | Pushbutton "heating/cooling" change |
| `AUTOMATIC_CHANGEOVER_MODE` | `0` = Enabled; `1` = Disabled | `1` | Automatic changeover; Condition to check contact: - See notes contained into parameters "Heating contact opening", "Heating contact closing", "Cooling contact opening" and "Cooling contact closing". Condition to check fil pilote: - See note contained into parameter "Heating actuator type". Conditions to check for actuators and pumps: - There must be at least one actuator for heatng (actuator function set to "Heating only" or "Heating and Cooling") or at least one pump for heating (pump function set to "Heating only"). - There must be at least one actuator for cooling (actuator function set to "Cooling only" or "Heating and Cooling") or at least one pump for cooling (pump function set to "Cooling only"). - if at least one actuator function is set to "Heating and cooling", "Heating actuator type" (that must be equal to "Cooling actuator type") can only be equal to 7 or 8; if this condition related to "Heating actuator type" is not satisfied, there must be at least one pump function set to "Heating only" and one pump function set to "Cooling only". |
| `AUTOMATIC_CHANGEOVER_MODE_SWITCHING_THRESHOLD` | `20..50` | `20` | Automatic changeover mode switching threshold (step 0.1 °C); Hidden, used only during device developement. |
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

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `160` | `1` | `184` | `4947` | `TYPE=0` | `7204` |
| `160` | `1` | `95` | `4939` | `TYPE=1` | `7204` |
| `160` | `1` | `96` | `4943` | `TYPE=2` | `7204` |
| `691` | `1` | `184` | `4947` | `TYPE=0` | `7204` |
| `691` | `1` | `95` | `4939` | `TYPE=1` | `7204` |
| `691` | `1` | `96` | `4943` | `TYPE=2` | `7204` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `160` | `184` | `1643` | `RISC` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Winter modality |
| `160` | `184` | `1644` | `COND` | `0` = Disable; `1` = Enable (entire reusable range retained) | `0` | Summer modality |
| `160` | `184` | `1645` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Load type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1646` | `COOLING_ACTUATOR_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Load type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1647` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1648` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1649` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1650` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1651` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1652` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1653` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1654` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1655` | `ACTUATOR_N=9_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `1716` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |
| `160` | `184` | `1918` | `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED (entire reusable range retained) | `0` | Ambient temperature visualization |
| `160` | `184` | `2667` | `COMFORT_HEATING_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `7`; `8`; `9` | `42` | Comfort; reusable default `42` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `2669` | `ECO_HEATING_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `6`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `7`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `8`; `9` | `36` | Eco; reusable default `36` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `2674` | `ANTIFREEZE_SETPOINT` | `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80` | `14` | Antifreeze; reusable default `14` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `2681` | `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Heating contact pushbutton locking |
| `160` | `184` | `2688` | `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating fancoil continuous ventilation |
| `160` | `184` | `2695` | `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `160` | `184` | `2702` | `HEATING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Heating PID regulation band (°) |
| `160` | `184` | `2709` | `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Heating PID inertia |
| `160` | `184` | `2716` | `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating proportional gain (low) |
| `160` | `184` | `2723` | `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating proportional gain (high) |
| `160` | `184` | `2730` | `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Heating integrative gain low |
| `160` | `184` | `2737` | `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Heating integrative gain high |
| `160` | `184` | `2744` | `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating derivative gain low |
| `160` | `184` | `2751` | `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating derivative gain high |
| `160` | `184` | `2758` | `HEATING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Heating proportional speed 1 (%) |
| `160` | `184` | `2765` | `HEATING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Heating proportional speed 2 (%) |
| `160` | `184` | `2772` | `HEATING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Heating proportional speed 3 (%) |
| `160` | `184` | `2779` | `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Heating pushbutton fan coil automatic speed |
| `160` | `184` | `2786` | `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating anti-seizing up protection |
| `160` | `184` | `2788` | `COMFORT_COOLING_SETPOINT` | `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79` | `50` | Comfort; reusable default `50` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `2790` | `ECO_COOLING_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `7`; `8`; `9`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80` | `56` | Eco; reusable default `56` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `2795` | `THERMAL_PROTECTION_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `6`; `7`; `8`; `9` | `70` | Thermal protection; reusable default `70` is outside this subset; filter supplies no replacement default |
| `160` | `184` | `2802` | `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Cooling contact pushbutton locking |
| `160` | `184` | `2809` | `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling fancoil continuous ventilation |
| `160` | `184` | `2816` | `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `160` | `184` | `2823` | `COOLING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Cooling PID regulation band (°) |
| `160` | `184` | `2830` | `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Cooling PID inertia |
| `160` | `184` | `2837` | `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling proportional gain (low) |
| `160` | `184` | `2844` | `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling proportional gain (high) |
| `160` | `184` | `2851` | `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Cooling integrative gain low |
| `160` | `184` | `2858` | `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Cooling integrative gain high |
| `160` | `184` | `2865` | `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling derivative gain low |
| `160` | `184` | `2872` | `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling derivative gain high |
| `160` | `184` | `2879` | `COOLING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Cooling proportional speed 1 (%) |
| `160` | `184` | `2886` | `COOLING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Cooling proportional speed 2 (%) |
| `160` | `184` | `2893` | `COOLING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Cooling proportional speed 3 (%) |
| `160` | `184` | `2900` | `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Cooling pushbutton fan coil automatic speed |
| `160` | `184` | `2907` | `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling anti-seizing up protection |
| `160` | `184` | `2914` | `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 (entire reusable range retained) | `10` | Backlight stand-by level |
| `160` | `184` | `2921` | `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Disable all pushbuttons |
| `160` | `184` | `2928` | `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Pushbutton modality change |
| `160` | `184` | `2935` | `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Calibration procedure |
| `160` | `184` | `2942` | `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | User settings procedure |
| `160` | `184` | `2949` | `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open (entire reusable range retained) | `0` | Windows contact icon |
| `160` | `184` | `2956` | `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled (entire reusable range retained) | `0` | Windows contact number |
| `160` | `95` | `857` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=1_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `160` | `95` | `858` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=2_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `160` | `95` | `869` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `870` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `871` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `872` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `873` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `874` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `875` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `876` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `877` | `ACTUATOR_N=9_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `878` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Heating_actuator_type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `879` | `COOLING_ACTUATOR_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Cooling_actuator_ type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `1714` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |
| `160` | `95` | `1911` | `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED (entire reusable range retained) | `0` | Ambient temperature visualization |
| `160` | `95` | `2482` | `COMFORT_HEATING_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `7`; `8`; `9` | `42` | Comfort; reusable default `42` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `2484` | `ECO_HEATING_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `6`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `7`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `8`; `9` | `36` | Eco; reusable default `36` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `2486` | `ANTIFREEZE_SETPOINT` | `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80` | `14` | Antifreeze; reusable default `14` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `2488` | `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed (entire reusable range retained) | `0` | Heating contact pushbutton locking |
| `160` | `95` | `2490` | `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating fancoil ventilation function |
| `160` | `95` | `2497` | `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling fancoil continuous ventilation |
| `160` | `95` | `2499` | `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `160` | `95` | `2501` | `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `160` | `95` | `2503` | `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed (entire reusable range retained) | `0` | Cooling contact pushbutton locking |
| `160` | `95` | `2505` | `HEATING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Heating PID regulation band |
| `160` | `95` | `2507` | `COOLING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Cooling PID regulation band (°) |
| `160` | `95` | `2509` | `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Heating |
| `160` | `95` | `2511` | `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Cooling PID inertia |
| `160` | `95` | `2513` | `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating proportional gain (low) |
| `160` | `95` | `2515` | `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling proportional gain (low) |
| `160` | `95` | `2517` | `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating proportional gain (high) |
| `160` | `95` | `2519` | `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling proportional gain (high) |
| `160` | `95` | `2521` | `COMFORT_COOLING_SETPOINT` | `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79` | `50` | Comfort; reusable default `50` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `2523` | `ECO_COOLING_SETPOINT` | `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80`; `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `7`; `8`; `9` | `56` | Eco; reusable default `56` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `2525` | `THERMAL_PROTECTION_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `6`; `7`; `8`; `9` | `70` | Thermal protection; reusable default `70` is outside this subset; filter supplies no replacement default |
| `160` | `95` | `2527` | `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Heating integrative gain low |
| `160` | `95` | `2529` | `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Cooling integrative gain low |
| `160` | `95` | `2531` | `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Heating integrative gain high |
| `160` | `95` | `2533` | `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Cooling integrative gain high |
| `160` | `95` | `2535` | `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating derivative gain low |
| `160` | `95` | `2537` | `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling derivative gain low |
| `160` | `95` | `2539` | `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating derivative gain high |
| `160` | `95` | `2541` | `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling derivative gain high |
| `160` | `95` | `2543` | `HEATING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Heating proportional speed 1 (%) |
| `160` | `95` | `2545` | `COOLING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Cooling proportional speed 1 (%) |
| `160` | `95` | `2547` | `COOLING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Cooling proportional speed 2 (%) |
| `160` | `95` | `2549` | `HEATING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Heating proportional speed 2 (%) |
| `160` | `95` | `2551` | `HEATING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Heating proportional speed 3 (%) |
| `160` | `95` | `2553` | `COOLING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Cooling proportional speed 3 (%) |
| `160` | `95` | `2555` | `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Heating pushbutton fan coil automatic speed |
| `160` | `95` | `2557` | `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Cooling pushbutton fan coil automatic speed |
| `160` | `95` | `2559` | `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating anti-seizing up protection |
| `160` | `95` | `2561` | `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling anti-seizing up protection |
| `160` | `95` | `2563` | `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10; `11` = Automatic with off; `12` = Automatic without off (entire reusable range retained) | `10` | Backlight stand-by level |
| `160` | `95` | `2565` | `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Disable all push buttons |
| `160` | `95` | `2567` | `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Pushbutton modality change |
| `160` | `95` | `2569` | `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Calibration procedure |
| `160` | `95` | `2571` | `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | User settings procedure |
| `160` | `95` | `2573` | `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open (entire reusable range retained) | `0` | Windows contact icon |
| `160` | `95` | `2575` | `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled (entire reusable range retained) | `0` | Windows contact number |
| `160` | `95` | `3742` | `EXTERNAL_SENSOR_TYPE` | `0` = BTicino BT-3457; `1` = Vantage 8051 (entire reusable range retained) | `0` | External temperature sensor type |
| `160` | `96` | `880` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=1_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `160` | `96` | `881` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=2_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `160` | `96` | `884` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=5_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `160` | `96` | `892` | `COOLING_ACTUATOR_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Cooling_actuator_ type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `893` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Heating_actuator_type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `894` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `895` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `896` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `897` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `898` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `899` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `900` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `901` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `902` | `ACTUATOR_N=9_TYPE` | `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `1715` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |
| `160` | `96` | `1912` | `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED (entire reusable range retained) | `0` | Ambient temperature visualization |
| `160` | `96` | `2577` | `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed (entire reusable range retained) | `0` | Heating contact pushbutton locking |
| `160` | `96` | `2579` | `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating fancoil continuous ventilation |
| `160` | `96` | `2581` | `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `160` | `96` | `2583` | `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed (entire reusable range retained) | `0` | Cooling contact pushbutton locking |
| `160` | `96` | `2585` | `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling fancoil continuous ventilation |
| `160` | `96` | `2587` | `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `160` | `96` | `2589` | `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 (entire reusable range retained) | `10` | Backlight stand-by level |
| `160` | `96` | `2591` | `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Disable all pushbuttons |
| `160` | `96` | `2593` | `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Pushbutton modality change |
| `160` | `96` | `2595` | `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Calibration procedure |
| `160` | `96` | `2597` | `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | User settings procedure |
| `160` | `96` | `2599` | `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open (entire reusable range retained) | `0` | Windows contact icon |
| `160` | `96` | `2601` | `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled (entire reusable range retained) | `0` | Windows contact number |
| `160` | `96` | `2603` | `HEATING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Heating PID regulation band (°) |
| `160` | `96` | `2605` | `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Heating PID inertia |
| `160` | `96` | `2607` | `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating proportional gain (low) |
| `160` | `96` | `2609` | `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating proportional gain (high) |
| `160` | `96` | `2611` | `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Heating integrative gain low |
| `160` | `96` | `2613` | `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Heating integrative gain high |
| `160` | `96` | `2615` | `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating derivative gain low |
| `160` | `96` | `2617` | `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating derivative gain high |
| `160` | `96` | `2619` | `HEATING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Heating proportional speed 1 (%) |
| `160` | `96` | `2621` | `HEATING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Heating proportional speed 2 (%) |
| `160` | `96` | `2623` | `HEATING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Heating proportional speed 3 (%) |
| `160` | `96` | `2625` | `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Heating pushbutton fan coil automatic speed |
| `160` | `96` | `2627` | `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating anti-seizing up protection |
| `160` | `96` | `2629` | `COOLING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Cooling PID regulation band (°) |
| `160` | `96` | `2631` | `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Cooling PID inertia |
| `160` | `96` | `2633` | `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling proportional gain (low) |
| `160` | `96` | `2635` | `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling proportional gain (high) |
| `160` | `96` | `2637` | `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Cooling integrative gain low |
| `160` | `96` | `2639` | `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Cooling integrative gain high |
| `160` | `96` | `2641` | `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling derivative gain low |
| `160` | `96` | `2643` | `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling derivative gain high |
| `160` | `96` | `2645` | `COOLING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Cooling proportional speed 1 (%) |
| `160` | `96` | `2647` | `COOLING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Cooling proportional speed 2 (%) |
| `160` | `96` | `2649` | `COOLING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Cooling proportional speed 3 (%) |
| `160` | `96` | `2651` | `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Cooling pushbutton fan coil automatic speed |
| `160` | `96` | `2653` | `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling anti-seizing up protection |
| `160` | `96` | `2655` | `COMFORT_HEATING_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `7`; `8`; `9` | `42` | Comfort; reusable default `42` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `2657` | `ECO_HEATING_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `6`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `7`; `70`; `71`; `8`; `9`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79` | `36` | Eco; reusable default `36` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `2659` | `ANTIFREEZE_SETPOINT` | `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80` | `14` | Antifreeze; reusable default `14` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `2661` | `COMFORT_COOLING_SETPOINT` | `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79` | `50` | Comfort; reusable default `50` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `2663` | `ECO_COOLING_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `7`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `8`; `80`; `9` | `56` | Eco; reusable default `56` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `2665` | `THERMAL_PROTECTION_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `6`; `7`; `8`; `9`; `45`; `46`; `47`; `48`; `49` | `70` | Thermal protection; reusable default `70` is outside this subset; filter supplies no replacement default |
| `160` | `96` | `2958` | `FUNCTION_CHANGE_BY_LOCAL_BUTTON` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Pushbutton "heating/cooling" change |
| `691` | `184` | `1970` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1971` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1972` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1973` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1974` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1975` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1976` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1977` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1978` | `ACTUATOR_N=9_TYPE` | `10` = IR emitter | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1979` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter | `0` | Load type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1980` | `COOLING_ACTUATOR_TYPE` | `10` = IR emitter | `0` | Load type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `184` | `1981` | `RISC` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Winter modality |
| `691` | `184` | `1982` | `COND` | `0` = Disable; `1` = Enable (entire reusable range retained) | `0` | Summer modality |
| `691` | `184` | `2986` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |
| `691` | `95` | `1920` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1921` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1922` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1923` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1924` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1925` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1926` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1927` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1928` | `ACTUATOR_N=9_TYPE` | `10` = IR emitter | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1929` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter | `0` | Heating_actuator_type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1930` | `COOLING_ACTUATOR_TYPE` | `10` = IR emitter | `0` | Cooling_actuator_ type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `1931` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=1_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `691` | `95` | `1932` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=2_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `691` | `95` | `2984` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |
| `691` | `95` | `3089` | `ECO_COOLING_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `7`; `8`; `9` | `56` | Eco; reusable default `56` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `3437` | `BACKLIGHT_STANDBY_LEVEL` | `11` = Automatic with off; `12` = Automatic without off | `10` | Backlight stand-by level; reusable default `10` is outside this subset; filter supplies no replacement default |
| `691` | `95` | `3743` | `EXTERNAL_SENSOR_TYPE` | `0` = BTicino BT-3457; `1` = Vantage 8051 (entire reusable range retained) | `0` | External temperature sensor type |
| `691` | `96` | `1945` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1946` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1947` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1948` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1949` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1950` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1951` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1952` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1953` | `ACTUATOR_N=9_TYPE` | `10` = IR emitter | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1954` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter | `0` | Heating_actuator_type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1955` | `COOLING_ACTUATOR_TYPE` | `10` = IR emitter | `0` | Cooling_actuator_ type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `691` | `96` | `1956` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=1_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `691` | `96` | `1957` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=2_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `691` | `96` | `1960` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter | `0` | Type actuator 1 (Actuator_N=5_type); reusable default `0` is outside this subset; filter supplies no replacement default; field definition belongs to a different Object scope; do not alias it to a similarly named field |
| `691` | `96` | `2985` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7204` | `ZA/A=0` | `A` = `0` | `7204` |
| `7204` | `ZA/A=0; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=0; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=1` | `A` = `1` | `7204` |
| `7204` | `ZA/A=1; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=1; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=2` | `A` = `2` | `7204` |
| `7204` | `ZA/A=2; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=2; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=3` | `A` = `3` | `7204` |
| `7204` | `ZA/A=3; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=3; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=4` | `A` = `4` | `7204` |
| `7204` | `ZA/A=4; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=4; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=5` | `A` = `5` | `7204` |
| `7204` | `ZA/A=5; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=5; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=6` | `A` = `6` | `7204` |
| `7204` | `ZA/A=6; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=6; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=7` | `A` = `7` | `7204` |
| `7204` | `ZA/A=7; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=7; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=8` | `A` = `8` | `7204` |
| `7204` | `ZA/A=8; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=8; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |
| `7204` | `ZA/A=9` | `A` = `9` | `7204` |
| `7204` | `ZA/A=9; ZB/PL=0` | `PL` = `0` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=1` | `PL` = `1` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=2` | `PL` = `2` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=3` | `PL` = `3` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=4` | `PL` = `4` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=5` | `PL` = `5` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=6` | `PL` = `6` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=7` | `PL` = `7` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=8` | `PL` = `8` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=9` | `PL` = `9` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=10` | `PL` = `10` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=11` | `PL` = `11` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=12` | `PL` = `12` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=13` | `PL` = `13` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=14` | `PL` = `14` | `7204` → `7205` |
| `7204` | `ZA/A=9; ZB/PL=15` | `PL` = `15` | `7204` → `7205` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1686` / `modobj = 6` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`184`, `95`, `96`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Room-temperature control with locally selectable operating modes and firmware/Object-dependent heating, cooling, fan-coil, contact, pump and setpoint behavior.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

The publisher sheet directly names all four catalogue identities. Firmware 1.0.-1 and 2.0.0 share the same three Object families in the catalogue, while applicability and configuration fields remain firmware- and relation-scoped.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `H4691-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4691` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/77/aa/77aa94ef9d3597fe6bf35915e3db596a8d09298d8f677e419e3846a9197d92fe.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4691); SHA-256 `77aa94ef9d3597fe6bf35915e3db596a8d09298d8f677e419e3846a9197d92fe`.
- `LN4691-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4691` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/ad/ce/adced5f1ae3272456c85abc178c0224f8867953120ba7e470b6f50b0335331b4.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4691); SHA-256 `adced5f1ae3272456c85abc178c0224f8867953120ba7e470b6f50b0335331b4`.
