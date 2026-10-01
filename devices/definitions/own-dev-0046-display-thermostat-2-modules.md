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
| BTicino Axolute | `H4691` | established catalogue identity for item `1686` | canonical commercial record |
| BTicino L/N/NT | `LN4691` | established catalogue identity for item `1686` | canonical commercial record |
| Legrand Céliane | `067459` | established catalogue identity for item `1686` | canonical commercial record |
| Arnould Espace Evolution | `64170` | established catalogue identity for item `1686` | canonical commercial record |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MM00789_b_EN` | technical sheet | revision b; date not confirmed in retained metadata | `H4691` / `LN4691` / `067459` / `64170` thermostat functions and installation characteristics | [Archived original](../../sources/devices/documents/device-doc-display-thermostat-mm00789-b-en/MM00789_b_EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MM00789_b_EN.pdf) |
| BTicino `H4691` catalogue page | product page | current catalogue | Current `H4691` electrical characteristics and product role | Not applicable - web page | [Official product page](https://catalogo.bticino.it/BTI-H4691-IT) |

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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `160` | `1` | `0` | `-1` | `1` | catalogue default | wildcard / unspecified applicability retained |
| `691` | `2` | `0` | `0` | `1` | non-default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `160` | `877` | `542` Hotel thermostat | catalogue firmware/Object relation |
| `160` | `878` | `545` Residential thermostat | catalogue firmware/Object relation |
| `160` | `2095` | `184` Master probe | catalogue firmware/Object relation |
| `691` | `2573` | `542` Hotel thermostat | catalogue firmware/Object relation |
| `691` | `2574` | `545` Residential thermostat | catalogue firmware/Object relation |
| `691` | `2575` | `184` Master probe | catalogue firmware/Object relation |

| Firmware | Virgin Object | Relationship |
| --- | --- | --- |
| `160` | `530` | catalogue candidate/template association |
| `691` | `530` | catalogue candidate/template association |

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

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `160` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `160` | `ZA` | catalogue-defined domain | catalogue-scoped | ZA |
| `160` | `ZB` | catalogue-defined domain | catalogue-scoped | ZB |
| `160` | `TYPE` | catalogue-defined domain | catalogue-scoped | TYPE |
| `160` | `HEAT` | catalogue-defined domain | catalogue-scoped | HEAT |
| `160` | `COOL` | catalogue-defined domain | catalogue-scoped | COOL |
| `160` | `PUMP` | catalogue-defined domain | catalogue-scoped | PUMP |
| `160` | `IN` | catalogue-defined domain | catalogue-scoped | IN |
| `691` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `691` | `ZA` | catalogue-defined domain | catalogue-scoped | ZA |
| `691` | `ZB` | catalogue-defined domain | catalogue-scoped | ZB |
| `691` | `TYPE` | catalogue-defined domain | catalogue-scoped | TYPE |
| `691` | `HEAT` | catalogue-defined domain | catalogue-scoped | HEAT |
| `691` | `COOL` | catalogue-defined domain | catalogue-scoped | COOL |
| `691` | `PUMP` | catalogue-defined domain | catalogue-scoped | PUMP |
| `691` | `IN` | catalogue-defined domain | catalogue-scoped | IN |

## Object configuration surfaces

### Object `184` - Master probe

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function type |
| `ZAZB` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Zone |
| `COND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Summer modality |
| `RISC` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Winter modality |
| `ZAZB_CENTRAL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Temperature Control unit address |
| `COMFORT_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Comfort |
| `ECO_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Eco |
| `ANTIFREEZE_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Antifreeze |
| `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating fan delay |
| `HEATING_THRESHOLDS_SETTINGS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automatic heating thresholds settings |
| `HEATING_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating setpoint allowance |
| `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | First speed threshold for fancoils |
| `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Second speed threshold for fancoils |
| `HEATING_CONTACT_OPENING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact opening |
| `HEATING_CONTACT_CLOSING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact closing |
| `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact opening |
| `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact closing |
| `HEATING_CONTACT_OPENING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact opening action |
| `HEATING_CONTACT_CLOSING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact closing action |
| `HEATING_CONTACT_PUSHBTN_LOCK` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating contact pushbutton locking |
| `HEATING_FANCOIL_VENTILATION_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating fancoil continuous ventilation |
| `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating fan coil continuous ventilation timeout (minutes) |
| `COMFORT_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Comfort |
| `ECO_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Eco |
| `THERMAL_PROTECTION_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Thermal protection |
| `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling fan delay |
| `COOLING_THRESHOLDS_SETTINGS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automatic cooling thresholds settings |
| `COOLING_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling setpoint allowance |
| `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | First speed threshold for fancoils |
| `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Second speed threshold for fancoils |
| `COOLING_CONTACT_OPENING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact opening |
| `COOLING_CONTACT_CLOSING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact closing |
| `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact opening action |
| `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact closing action |
| `COOLING_CONTACT_OPENING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact opening action |
| `COOLING_CONTACT_CLOSING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact closing action |
| `COOLING_CONTACT_PUSHBTN_LOCK` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling contact pushbutton locking |
| `COOLING_FANCOIL_VENTILATION_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling fancoil continuous ventilation |
| `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling fan coil continuous ventilation timeout (minutes) |
| `ACTUATOR_N=1_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 1 function |
| `ACTUATOR_N=2_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 2 function |
| `ACTUATOR_N=3_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 3 function |
| `ACTUATOR_N=4_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 4 function |
| `ACTUATOR_N=5_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 5 function |
| `ACTUATOR_N=6_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 6 function |
| `ACTUATOR_N=7_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 7 function |
| `ACTUATOR_N=8_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 8 function |
| `ACTUATOR_N=9_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 9 function |
| `ACTUATOR_N=1_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 1 |
| `ACTUATOR_N=2_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 2 |
| `ACTUATOR_N=3_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 3 |
| `ACTUATOR_N=4_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 4 |
| `ACTUATOR_N=5_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 5 |
| `ACTUATOR_N=6_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 6 |
| `ACTUATOR_N=7_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 7 |
| `ACTUATOR_N=8_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 8 |
| `ACTUATOR_N=9_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 9 |
| `HEATING_ACTUATOR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Load type |
| `COOLING_ACTUATOR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Load type |
| `PUMP_N=1_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 1 function |
| `PUMP_N=2_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 2 function |
| `PUMP_N=3_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 3 function |
| `PUMP_N=4_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 4 function |
| `PUMP_N=5_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 5 function |
| `PUMP_N=6_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 6 function |
| `PUMP_N=7_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 7 function |
| `PUMP_N=8_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 8 function |
| `PUMP_N=9_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 9 function |
| `HEATING_PUMP_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay for heating pumps |
| `COOLING_PUMP_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay for cooling pumps |
| `NUMBER_OF_SLAVES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Number of slave probes |
| `LED_ENABLE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Led enable |
| `TEMPERATURE_FORMAT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Temperature format |
| `BACKLIGHT_STAND_BY_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Display standby backlight |
| `AMBIENT_TEMPERATURE_VISUALIZATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Ambient temperature visualization |
| `BACKLIGHT_STANDBY_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Backlight stand-by level |
| `PUSHBUTTON_MANAGEMENT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Disable all pushbuttons |
| `PUSHBUTTON_MODALITY_CHANGE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pushbutton modality change |
| `CALIBRATION_PROCEDURE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Calibration procedure |
| `USER_SETTINGS_PROCEDURE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | User settings procedure |
| `WINDOWS_CONTACT_ICON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Windows contact icon |
| `WINDOWS_CONTACT_NUMBER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Windows contact number |
| `HEATING_PID_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating PID regulation band (°) |
| `HEATING_PID_INERTIA` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating PID inertia |
| `HEATING_PROPORTIONAL_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional gain (low) |
| `HEATING_PROPORTIONAL_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional gain (high) |
| `HEATING_INTEGRATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating integrative gain low |
| `HEATING_INTEGRATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating integrative gain high |
| `HEATING_DERIVATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating derivative gain low |
| `HEATING_DERIVATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating derivative gain high |
| `HEATING_PROPORTIONAL_SPEED_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional speed 1 (%) |
| `HEATING_PROPORTIONAL_SPEED_2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional speed 2 (%) |
| `HEATING_PROPORTIONAL_SPEED_3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional speed 3 (%) |
| `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating pushbutton fan coil automatic speed |
| `HEATING_ANTI_SEIZING_UP_PROTECTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating anti-seizing up protection |
| `COOLING_PID_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling PID regulation band (°) |
| `COOLING_PID_INERTIA` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling PID inertia |
| `COOLING_PROPORTIONAL_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional gain (low) |
| `COOLING_PROPORTIONAL_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional gain (high) |
| `COOLING_INTEGRATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling integrative gain low |
| `COOLING_INTEGRATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling integrative gain high |
| `COOLING_DERIVATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling derivative gain low |
| `COOLING_DERIVATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling derivative gain high |
| `COOLING_PROPORTIONAL_SPEED_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional speed 1 (%) |
| `COOLING_PROPORTIONAL_SPEED_2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional speed 2 (%) |
| `COOLING_PROPORTIONAL_SPEED_3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional speed 3 (%) |
| `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling pushbutton fan coil automatic speed |
| `COOLING_ANTI_SEIZING_UP_PROTECTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling anti-seizing up protection |

### Object `542` - Hotel thermostat

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Zone |
| `FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function type |
| `MAXIMUM_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Max |
| `MINIMUM_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Min |
| `COMFORT_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Comfort |
| `ECO_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Eco |
| `ANTIFREEZE_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Antifreeze |
| `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating fan delay |
| `HEATING_THRESHOLDS_SETTINGS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automatic heating thresholds settings |
| `HEATING_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating setpoint allowance |
| `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | First speed threshold for fancoils |
| `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Second speed threshold for fancoils |
| `HEATING_CONTACT_OPENING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact opening |
| `HEATING_CONTACT_CLOSING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact closing |
| `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact after opening |
| `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact after closing |
| `HEATING_CONTACT_OPENING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact after opening |
| `HEATING_CONTACT_CLOSING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact after closing |
| `HEATING_CONTACT_PUSHBTN_LOCK` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating contact pushbutton locking |
| `HEATING_FANCOIL_VENTILATION_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating fancoil ventilation function |
| `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating fan coil continuous ventilation timeout (minutes) |
| `MAXIMUM_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Max |
| `MINIMUM_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Min |
| `COMFORT_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Comfort |
| `ECO_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Eco |
| `THERMAL_PROTECTION_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Thermal protection |
| `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling fan delay |
| `COOLING_THRESHOLDS_SETTINGS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling thresholds settings |
| `COOLING_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling setpoint allowance |
| `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | First speed threshold for fancoils |
| `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Second speed threshold for fancoils |
| `COOLING_CONTACT_OPENING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact opening |
| `COOLING_CONTACT_CLOSING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact closing |
| `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact opening |
| `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact closing |
| `COOLING_CONTACT_OPENING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact opening action |
| `COOLING_CONTACT_CLOSING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact closing action |
| `COOLING_CONTACT_PUSHBTN_LOCK` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling contact pushbutton locking |
| `COOLING_FANCOIL_VENTILATION_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling fancoil continuous ventilation |
| `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling fan coil continuous ventilation timeout (minutes) |
| `ACTUATOR_N=1_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 1 function |
| `ACTUATOR_N=2_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 2 function |
| `ACTUATOR_N=3_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 3 function |
| `ACTUATOR_N=4_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 4 function |
| `ACTUATOR_N=5_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 5 function |
| `ACTUATOR_N=6_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 6 function |
| `ACTUATOR_N=7_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 7 function |
| `ACTUATOR_N=8_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 8 function |
| `ACTUATOR_N=9_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Actuator 9 function |
| `ACTUATOR_N=1_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 1 |
| `ACTUATOR_N=2_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 2 |
| `ACTUATOR_N=3_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 3 |
| `ACTUATOR_N=4_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 4 |
| `ACTUATOR_N=5_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 5 |
| `ACTUATOR_N=6_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 6 |
| `ACTUATOR_N=7_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 7 |
| `ACTUATOR_N=8_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 8 |
| `ACTUATOR_N=9_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 9 |
| `HEATING_ACTUATOR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Load type |
| `COOLING_ACTUATOR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Load type |
| `PUMP_N=1_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 1 function |
| `PUMP_N=2_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 2 function |
| `PUMP_N=3_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 3 function |
| `PUMP_N=4_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 4 function |
| `PUMP_N=5_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 5 function |
| `PUMP_N=6_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 6 function |
| `PUMP_N=7_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 7 function |
| `PUMP_N=8_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 8 function |
| `PUMP_N=9_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 9 function |
| `HEATING_PUMP_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay for heating pumps |
| `COOLING_PUMP_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay for cooling pumps |
| `NUMBER_OF_SLAVES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Number of slave probes |
| `LED_ENABLE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Led enable |
| `TEMPERATURE_FORMAT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Temperature format |
| `FUNCTION_CHANGE_BY_LOCAL_BUTTON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pushbutton "heating/cooling" change |
| `AUTOMATIC_CHANGEOVER_MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automatic changeover mode |
| `AUTOMATIC_CHANGEOVER_MODE_SWITCHING_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automatic changeover mode switching threshold (step 0.1 °C) |
| `BACKLIGHT_STAND_BY_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Backlight for display standby |
| `AMBIENT_TEMPERATURE_VISUALIZATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Room temperature visualization |
| `BACKLIGHT_STANDBY_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Backlight stand-by level |
| `PUSHBUTTON_MANAGEMENT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Disable all pushbuttons |
| `PUSHBUTTON_MODALITY_CHANGE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pushbutton modality change |
| `CALIBRATION_PROCEDURE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Calibration procedure |
| `USER_SETTINGS_PROCEDURE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | User settings procedure |
| `WINDOWS_CONTACT_ICON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Windows contact icon |
| `WINDOWS_CONTACT_NUMBER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Windows contact number |
| `EXTERNAL_SENSOR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | External temperature sensor type |
| `HEATING_PID_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating PID regulation band (°) |
| `HEATING_PID_INERTIA` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating PID inertia |
| `HEATING_PROPORTIONAL_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional gain (low) |
| `HEATING_PROPORTIONAL_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional gain (high) |
| `HEATING_INTEGRATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating integrative gain low |
| `HEATING_INTEGRATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating integrative gain high |
| `HEATING_DERIVATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating derivative gain low |
| `HEATING_DERIVATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating derivative gain high |
| `HEATING_PROPORTIONAL_SPEED_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional speed 1 (%) |
| `HEATING_PROPORTIONAL_SPEED_2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional speed 2 (%) |
| `HEATING_PROPORTIONAL_SPEED_3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional speed 3 (%) |
| `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating pushbutton fan coil automatic speed |
| `HEATING_ANTI_SEIZING_UP_PROTECTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating anti-seizing up protection |
| `COOLING_PID_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling PID regulation band (°) |
| `COOLING_PID_INERTIA` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling PID inertia |
| `COOLING_PROPORTIONAL_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional gain (low) |
| `COOLING_PROPORTIONAL_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional gain (high) |
| `COOLING_INTEGRATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling integrative gain low |
| `COOLING_INTEGRATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling integrative gain high |
| `COOLING_DERIVATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling derivative gain low |
| `COOLING_DERIVATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling derivative gain high |
| `COOLING_PROPORTIONAL_SPEED_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional speed 1 (%) |
| `COOLING_PROPORTIONAL_SPEED_2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional speed 2 (%) |
| `COOLING_PROPORTIONAL_SPEED_3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional speed 3 (%) |
| `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling pushbutton fan coil automatic speed |
| `COOLING_ANTI_SEIZING_UP_PROTECTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling anti-seizing up protection |

### Object `545` - Residential thermostat

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Zone |
| `FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function type: -Heating -Cooling -Heating & Cooling |
| `MAXIMUM_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Max |
| `MINIMUM_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Min |
| `COMFORT_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Comfort |
| `ECO_HEATING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Eco |
| `ANTIFREEZE_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Antifreeze |
| `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating fan delay |
| `HEATING_THRESHOLDS_SETTINGS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automatic heating thresholds settings |
| `HEATING_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating setpoint allowance |
| `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | First speed threshold for fancoils |
| `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Second speed threshold for fancoils |
| `HEATING_CONTACT_OPENING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact opening |
| `HEATING_CONTACT_CLOSING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact closing |
| `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact opening |
| `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact closing |
| `HEATING_CONTACT_OPENING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact opening action |
| `HEATING_CONTACT_CLOSING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact opening action |
| `HEATING_CONTACT_PUSHBTN_LOCK` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating contact pushbutton locking |
| `HEATING_FANCOIL_VENTILATION_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating fancoil continuous ventilation |
| `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating fan coil continuous ventilation timeout (minutes) |
| `MAXIMUM_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Max |
| `MINIMUM_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Min |
| `COMFORT_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Comfort |
| `ECO_COOLING_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Eco |
| `THERMAL_PROTECTION_SETPOINT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Thermal protection |
| `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling fan delay |
| `COOLING_THRESHOLDS_SETTINGS` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automatic cooling thresholds settings |
| `COOLING_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling setpoint allowance |
| `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | First speed threshold for fancoils |
| `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Second speed threshold for fancoils |
| `COOLING_CONTACT_OPENING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact opening |
| `COOLING_CONTACT_CLOSING` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Local contact closing |
| `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact opening |
| `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Activation delay for local contact closing |
| `COOLING_CONTACT_OPENING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact opening action |
| `COOLING_CONTACT_CLOSING_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Timeout for local contact opening action |
| `COOLING_CONTACT_PUSHBTN_LOCK` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling contact pushbutton locking |
| `COOLING_FANCOIL_VENTILATION_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling fancoil continuous ventilation |
| `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling fan coil continuous ventilation timeout (minutes) |
| `ACTUATOR_N=1_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function actuator 1 |
| `ACTUATOR_N=2_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function actuator 2 |
| `ACTUATOR_N=3_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function actuator 3 |
| `ACTUATOR_N=4_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function actuator 4 |
| `ACTUATOR_N=5_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function actuator 5 |
| `ACTUATOR_N=6_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function actuator 6 |
| `ACTUATOR_N=7_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function actuator 7 |
| `ACTUATOR_N=8_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function actuator 8 |
| `ACTUATOR_N=9_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Function actuator 9 |
| `ACTUATOR_N=1_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 1 |
| `ACTUATOR_N=2_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 2 |
| `ACTUATOR_N=3_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 3 |
| `ACTUATOR_N=4_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 4 |
| `ACTUATOR_N=5_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 5 |
| `ACTUATOR_N=6_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 6 |
| `ACTUATOR_N=7_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 7 |
| `ACTUATOR_N=8_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 8 |
| `ACTUATOR_N=9_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Type actuator 9 |
| `HEATING_ACTUATOR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Load type |
| `COOLING_ACTUATOR_TYPE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Load type |
| `PUMP_N=1_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 1 function |
| `PUMP_N=2_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 2 function |
| `PUMP_N=3_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 3 function |
| `PUMP_N=4_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 4 function |
| `PUMP_N=5_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 5 function |
| `PUMP_N=6_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 6 function |
| `PUMP_N=7_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 7 function |
| `PUMP_N=8_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 8 function |
| `PUMP_N=9_FUNCTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pump 9 function |
| `HEATING_PUMP_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay for heating pumps |
| `COOLING_PUMP_DELAY` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Time delay for cooling pump |
| `NUMBER_OF_SLAVES` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Number of slave probes |
| `LED_ENABLE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Led enable |
| `TEMPERATURE_FORMAT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Temperature format |
| `FUNCTION_CHANGE_BY_LOCAL_BUTTON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pushbutton "heating/cooling" change |
| `AUTOMATIC_CHANGEOVER_MODE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automatic changeover |
| `AUTOMATIC_CHANGEOVER_MODE_SWITCHING_THRESHOLD` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Automatic changeover mode switching threshold (step 0.1 °C) |
| `BACKLIGHT_STAND_BY_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Display standby backlight |
| `AMBIENT_TEMPERATURE_VISUALIZATION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Ambient temperature visualization |
| `BACKLIGHT_STANDBY_LEVEL` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Backlight stand-by level |
| `PUSHBUTTON_MANAGEMENT` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Disable all pushbuttons |
| `PUSHBUTTON_MODALITY_CHANGE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Pushbutton modality change |
| `CALIBRATION_PROCEDURE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Calibration procedure |
| `USER_SETTINGS_PROCEDURE` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | User settings procedure |
| `WINDOWS_CONTACT_ICON` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Windows contact icon |
| `WINDOWS_CONTACT_NUMBER` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Windows contact number |
| `HEATING_PID_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating PID regulation band (°) |
| `HEATING_PID_INERTIA` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating PID inertia |
| `HEATING_PROPORTIONAL_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional gain (low) |
| `HEATING_PROPORTIONAL_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional gain (high) |
| `HEATING_INTEGRATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating integrative gain low |
| `HEATING_INTEGRATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating integrative gain high |
| `HEATING_DERIVATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating derivative gain low |
| `HEATING_DERIVATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating derivative gain high |
| `HEATING_PROPORTIONAL_SPEED_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional speed 1 (%) |
| `HEATING_PROPORTIONAL_SPEED_2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional speed 2 (%) |
| `HEATING_PROPORTIONAL_SPEED_3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating proportional speed 3 (%) |
| `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating pushbutton fan coil automatic speed |
| `HEATING_ANTI_SEIZING_UP_PROTECTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Heating anti-seizing up protection |
| `COOLING_PID_REGULATION_BAND` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling PID regulation band (°) |
| `COOLING_PID_INERTIA` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling PID inertia |
| `COOLING_PROPORTIONAL_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional gain (low) |
| `COOLING_PROPORTIONAL_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional gain (high) |
| `COOLING_INTEGRATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling integrative gain low |
| `COOLING_INTEGRATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling integrative gain high |
| `COOLING_DERIVATIVE_GAIN_LOW` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling derivative gain low |
| `COOLING_DERIVATIVE_GAIN_HIGH` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling derivative gain high |
| `COOLING_PROPORTIONAL_SPEED_1` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional speed 1 (%) |
| `COOLING_PROPORTIONAL_SPEED_2` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional speed 2 (%) |
| `COOLING_PROPORTIONAL_SPEED_3` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling proportional speed 3 (%) |
| `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling pushbutton fan coil automatic speed |
| `COOLING_ANTI_SEIZING_UP_PROTECTION` | catalogue-defined; apply Device relation filters and conditions | catalogue-scoped | Cooling anti-seizing up protection |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `857`, `858`, `869`, `870`, `871`, `872`, `873`, `874`, `875`, `876`, `877`, `878`, `879`, `880`, `881`, `884`, `892`, `893`, `894`, `895`, `896`, `897`, `898`, `899`, `900`, `901`, `902`, `1643`, `1644`, `1645`, `1646`, `1647`, `1648`, `1649`, `1650`, `1651`, `1652`, `1653`, `1654`, `1655`, `1714`, `1715`, `1716`, `1911`, `1912`, `1918`, `1920`, `1921`, `1922`, `1923`, `1924`, `1925`, `1926`, `1927`, `1928`, `1929`, `1930`, `1931`, `1932`, `1945`, `1946`, `1947`, `1948`, `1949`, `1950`, `1951`, `1952`, `1953`, `1954`, `1955`, `1956`, `1957`, `1960`, `1970`, `1971`, `1972`, `1973`, `1974`, `1975`, `1976`, `1977`, `1978`, `1979`, `1980`, `1981`, `1982`, `2482`, `2484`, `2486`, `2488`, `2490`, `2497`, `2499`, `2501`, `2503`, `2505`, `2507`, `2509`, `2511`, `2513`, `2515`, `2517`, `2519`, `2521`, `2523`, `2525`, `2527`, `2529`, `2531`, `2533`, `2535`, `2537`, `2539`, `2541`, `2543`, `2545`, `2547`, `2549`, `2551`, `2553`, `2555`, `2557`, `2559`, `2561`, `2563`, `2565`, `2567`, `2569`, `2571`, `2573`, `2575`, `2577`, `2579`, `2581`, `2583`, `2585`, `2587`, `2589`, `2591`, `2593`, `2595`, `2597`, `2599`, `2601`, `2603`, `2605`, `2607`, `2609`, `2611`, `2613`, `2615`, `2617`, `2619`, `2621`, `2623`, `2625`, `2627`, `2629`, `2631`, `2633`, `2635`, `2637`, `2639`, `2641`, `2643`, `2645`, `2647`, `2649`, `2651`, `2653`, `2655`, `2657`, `2659`, `2661`, `2663`, `2665`, `2667`, `2669`, `2674`, `2681`, `2688`, `2695`, `2702`, `2709`, `2716`, `2723`, `2730`, `2737`, `2744`, `2751`, `2758`, `2765`, `2772`, `2779`, `2786`, `2788`, `2790`, `2795`, `2802`, `2809`, `2816`, `2823`, `2830`, `2837`, `2844`, `2851`, `2858`, `2865`, `2872`, `2879`, `2886`, `2893`, `2900`, `2907`, `2914`, `2921`, `2928`, `2935`, `2942`, `2949`, `2956`, `2958`, `2984`, `2985`, `2986`, `3089`, `3437`, `3742`, `3743` | relation-specific restrictions; apply before exposing reusable Object values |
| Slot conditions | `4939`, `4943`, `4947` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve canonical condition/conversion evaluation; do not infer unconditional capability |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1686` / `modobj = 6` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`184`, `542`, `545`) | [Modules](../../diagnostics/dim30-modules.md) |
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
