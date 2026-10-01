# Basic temperature probe

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0041` | Project identity |
| Technical description | SCS basic temperature probe for zone sensing | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `HC/HS/HD4693`, `L/N/NT4693`, `573920`, `573921`, `067458` | Canonical commercial records |
| Catalogue item | `1862` | Implementation evidence |
| Main catalogue system | Temperature control | Implementation evidence |
| Item model / `modobj` | `21` | Implementation evidence |
| Firmware definition | `152 / 6.0.0`; `165 / 5.2.0` | Implementation evidence |
| Declared Modules | `1` | Firmware catalogue |
| Categories | Temperature control, HVAC, Sensor | Capability model |

SCS basic temperature probe for zone sensing.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `HC/HS/HD4693` | established catalogue identity for item `1862` | canonical commercial record |
| BTicino L/N/NT | `L/N/NT4693` | established catalogue identity for item `1862` | canonical commercial record |
| Legrand Arteor | `573920` | established catalogue identity for item `1862` | canonical commercial record |
| Legrand Arteor | `573921` | established catalogue identity for item `1862` | canonical commercial record |
| Legrand Céliane | `067458` | established catalogue identity for item `1862` | canonical commercial record |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| No dedicated Device-specific publisher source currently archived | source gap | current review | Catalogue extraction complete; direct product documentation remains to be recovered | - | - |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product role | Zone temperature sensing probe | Catalogue item and system mapping |
| Declared logical modules | 1 | Canonical firmware catalogue |
| Commercial family | Wiring-device probe family across five catalogue identities | Canonical commercial records |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1862` | Implementation evidence |
| Technical item description | Basic temperature probe | Implementation evidence |
| Main system | Temperature control | Implementation evidence |
| Item model / `modobj` | `21` | Implementation evidence |
| Commercial records | `5` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `152` | `6` | `0` | `0` | `1` | non-default | concrete catalogue applicability |
| `165` | `5` | `2` | `0` | `1` | catalogue default | concrete catalogue applicability |

No sanitized installed-hardware firmware fingerprint is currently retained for this exact technical item.

## Module, Object, and Virgin Object model

| Firmware | Slot(s) | Object | Relationship |
| --- | --- | --- | --- |
| `152` | `670` | `184` Master probe | fixed/designated |
| `152` | `1335` | `546` Slave probe | catalogue alternative |
| `165` | `1383` | `36` Temperature control probe | fixed/designated |
| `165` | `1384` | `546` Slave probe | catalogue alternative |

| Virgin Object status | Value |
| --- | --- |
| Associations | `529`, `529` |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `152` | Physical configuration | supported route for this Device family |
| `152` | Virtual Configuration | supported route for this Device family |
| `152` | Advanced Configuration | supported route for this Device family |
| `165` | Physical configuration | supported route for this Device family |
| `165` | Virtual Configuration | supported route for this Device family |
| `165` | Advanced Configuration | supported route for this Device family |

## Firmware-scoped configuration

| Firmware | Field | Domain | Default | Meaning |
| --- | --- | --- | --- | --- |
| `152` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `152` | `ZA` | catalogue-defined domain | catalogue-scoped | ZA thermo zone address |
| `152` | `ZB` | catalogue-defined domain | catalogue-scoped | ZB thermo zone address |
| `152` | `SLA` | catalogue-defined domain | catalogue-scoped | Thermoregulation slave probe |
| `152` | `MOD` | catalogue-defined domain | catalogue-scoped | Mode (Master,Slave) |
| `165` | `AID` | catalogue-defined domain | catalogue-scoped | ID |
| `165` | `ZA` | catalogue-defined domain | catalogue-scoped | ZA thermo zone address |
| `165` | `ZB` | catalogue-defined domain | catalogue-scoped | ZB thermo zone address |
| `165` | `SLA` | catalogue-defined domain | catalogue-scoped | Thermoregulation slave probe |
| `165` | `MOD` | catalogue-defined domain | catalogue-scoped | Mode (Master,Slave) |

## Object configuration surfaces

### Object `36` - Temperature control probe

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Zone |
| `N` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Device number |
| `P` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Thermoregulation master mode |
| `MOD` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Mode (SLA,CEN) |
| `SLA` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Slave number |
| `RISC` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Winter mode |
| `COND` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Summer mode |
| `ZAZB_CENTRALE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Control unit address |

### Object `184` - Master probe

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Function type |
| `ZAZB` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Zone |
| `COND` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Summer modality |
| `RISC` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Winter modality |
| `ZAZB_CENTRAL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Temperature Control unit address |
| `COMFORT_HEATING_SETPOINT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Comfort heating setpoint > Eco heating setpoint |
| `ECO_HEATING_SETPOINT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Eco heating setpoint < Comfort heating setpoint |
| `ANTIFREEZE_SETPOINT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Antifreeze |
| `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | checked only if "Heating actuator type" is set to one of values related to fan coil |
| `HEATING_THRESHOLDS_SETTINGS` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | For automatic, while checking configuration, set parameters 8, 9, 10 according to device specific settings. |
| `HEATING_REGULATION_BAND` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating setpoint allowance |
| `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 2 threshold > Heating regulation band |
| `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 3 threshold > Heating Fan coil speed 2 threshold |
| `HEATING_CONTACT_OPENING` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If parameter "Heating contact opening" is set to 0, 4, parameter "Heating contact opening timeout" must be set to 0." If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact opening must be different from 5...25. |
| `HEATING_CONTACT_CLOSING` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If parameter "Heating contact closing" is set to 0, 4, parameter "Heating contact closing timeout" must be set to 0." If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact closing must be different from 5...25. |
| `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Activation delay for local contact opening |
| `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Activation delay for local contact closing |
| `HEATING_CONTACT_OPENING_TIMEOUT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | 0 corresponds to infinite. If parameter "Heating contact opening timeout" is different from 0, "Heating contact closing timeout" must be set to 0. |
| `HEATING_CONTACT_CLOSING_TIMEOUT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | 0 corresponds to infinite. If parameter "Heating contact closing timeout" is different from 0, "Heating contact opening timeout" must be set to 0." |
| `HEATING_CONTACT_PUSHBTN_LOCK` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating contact pushbutton locking |
| `HEATING_FANCOIL_VENTILATION_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating fancoil continuous ventilation |
| `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating fan coil continuous ventilation timeout (minutes) |
| `COMFORT_COOLING_SETPOINT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Comfort cooling setpoint < Eco cooling setpoint |
| `ECO_COOLING_SETPOINT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Eco cooling setpoint > Comfort cooling setpoint |
| `THERMAL_PROTECTION_SETPOINT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Thermal protection |
| `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Checked only if "Cooling actuator type" is set to one of values related to fan coil |
| `COOLING_THRESHOLDS_SETTINGS` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | For automatic, while checking configuration, set 28, 29, 30 according to device specific settings. |
| `COOLING_REGULATION_BAND` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling setpoint allowance |
| `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 2 threshold > Cooling regulation band |
| `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 3 threshold > Cooling Fan coil speed 2 threshold |
| `COOLING_CONTACT_OPENING` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If parameter Cooling contact opening  is set to 0, 4, parameter Cooling contact opening timeout must be set to 0. |
| `COOLING_CONTACT_CLOSING` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If parameter "Cooling contact closing" is set to 0, 4, parameter "Cooling contact closing timeout" must be set to 0. |
| `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Timeout for local contact opening action |
| `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Timeout for local contact closing action |
| `COOLING_CONTACT_OPENING_TIMEOUT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | 0 corresponds to infinite. If parameter "Cooling contact opening timeout" is different from 0, "Cooling contact closing timeout" must be set to 0. |
| `COOLING_CONTACT_CLOSING_TIMEOUT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | 0 corresponds to infinite. If parameter Cooling contact closing timeout is different from 0, Cooling contact opening timeout must be set to 0. |
| `COOLING_CONTACT_PUSHBTN_LOCK` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling contact pushbutton locking |
| `COOLING_FANCOIL_VENTILATION_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling fancoil continuous ventilation |
| `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling fan coil continuous ventilation timeout (minutes) |
| `ACTUATOR_N=1_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=2_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=3_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=4_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=5_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=6_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=7_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=8_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=9_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=1_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=2_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=3_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=4_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=5_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=6_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=7_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=8_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=9_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `HEATING_ACTUATOR_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). |
| `COOLING_ACTUATOR_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | The highlighted values must not be implemented into key object (they are dedicated to future use). |
| `PUMP_N=1_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=2_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=3_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=4_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=5_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=6_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=7_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=8_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=9_FUNCTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `HEATING_PUMP_DELAY` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Time delay for heating pumps |
| `COOLING_PUMP_DELAY` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Time delay for cooling pumps |
| `NUMBER_OF_SLAVES` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Number of slave probes |
| `LED_ENABLE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Led enable |
| `TEMPERATURE_FORMAT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Temperature format |
| `BACKLIGHT_STAND_BY_LEVEL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Display standby backlight |
| `AMBIENT_TEMPERATURE_VISUALIZATION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Ambient temperature visualization |
| `BACKLIGHT_STANDBY_LEVEL` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Backlight stand-by level |
| `PUSHBUTTON_MANAGEMENT` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Disable all pushbuttons |
| `PUSHBUTTON_MODALITY_CHANGE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Pushbutton modality change |
| `CALIBRATION_PROCEDURE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Calibration procedure |
| `USER_SETTINGS_PROCEDURE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | User settings procedure |
| `WINDOWS_CONTACT_ICON` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Windows contact icon |
| `WINDOWS_CONTACT_NUMBER` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Windows contact number |
| `HEATING_PID_REGULATION_BAND` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating PID regulation band (°) |
| `HEATING_PID_INERTIA` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating PID inertia |
| `HEATING_PROPORTIONAL_GAIN_LOW` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating proportional gain (low) |
| `HEATING_PROPORTIONAL_GAIN_HIGH` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating proportional gain (high) |
| `HEATING_INTEGRATIVE_GAIN_LOW` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating integrative gain low |
| `HEATING_INTEGRATIVE_GAIN_HIGH` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating integrative gain high |
| `HEATING_DERIVATIVE_GAIN_LOW` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating derivative gain low |
| `HEATING_DERIVATIVE_GAIN_HIGH` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating derivative gain high |
| `HEATING_PROPORTIONAL_SPEED_1` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating proportional speed 1 (%) |
| `HEATING_PROPORTIONAL_SPEED_2` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating proportional speed 2 (%) |
| `HEATING_PROPORTIONAL_SPEED_3` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating proportional speed 3 (%) |
| `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating pushbutton fan coil automatic speed |
| `HEATING_ANTI_SEIZING_UP_PROTECTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Heating anti-seizing up protection |
| `COOLING_PID_REGULATION_BAND` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling PID regulation band (°) |
| `COOLING_PID_INERTIA` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling PID inertia |
| `COOLING_PROPORTIONAL_GAIN_LOW` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling proportional gain (low) |
| `COOLING_PROPORTIONAL_GAIN_HIGH` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling proportional gain (high) |
| `COOLING_INTEGRATIVE_GAIN_LOW` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling integrative gain low |
| `COOLING_INTEGRATIVE_GAIN_HIGH` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling integrative gain high |
| `COOLING_DERIVATIVE_GAIN_LOW` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling derivative gain low |
| `COOLING_DERIVATIVE_GAIN_HIGH` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling derivative gain high |
| `COOLING_PROPORTIONAL_SPEED_1` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling proportional speed 1 (%) |
| `COOLING_PROPORTIONAL_SPEED_2` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling proportional speed 2 (%) |
| `COOLING_PROPORTIONAL_SPEED_3` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling proportional speed 3 (%) |
| `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling pushbutton fan coil automatic speed |
| `COOLING_ANTI_SEIZING_UP_PROTECTION` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Cooling anti-seizing up protection |

### Object `546` - Slave probe

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Zone |
| `SLA` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Slave number |
| `LED_ENABLE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Led enable |
| `EXTERNAL_SENSOR_TYPE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | External temperature sensor type |
| `RISC` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Winter mode |
| `COND` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Summer mode |
| `ZAZB_CENTRALE` | catalogue-defined; validate through ranges and relation filters | catalogue-scoped | Temperature Control unit address |

## Conditions, filters, and conversions

| Surface | IDs / scope | Device-specific interpretation |
| --- | --- | --- |
| Object filters | `603`, `604`, `605`, `606`, `607`, `608`, `609`, `610`, `611`, `612`, `613`, `614`, `615`, `616`, `617`, `618`, `619`, `620`, `621`, `622`, `623`, `624`, `625`, `626`, `629`, `630`, `631`, `632`, `633`, `634`, `635`, `1522`, `1914`, `2672`, `2677`, `2684`, `2691`, `2698`, `2705`, `2712`, `2719`, `2726`, `2733`, `2740`, `2747`, `2754`, `2761`, `2768`, `2775`, `2782`, `2793`, `2798`, `2805`, `2812`, `2819`, `2826`, `2833`, `2840`, `2847`, `2854`, `2861`, `2868`, `2875`, `2882`, `2889`, `2896`, `2903`, `2910`, `2917`, `2924`, `2931`, `2938`, `2945`, `2952`, `3753`, `3754` | relation-specific restrictions; do not widen reusable Object surfaces |
| Slot conditions | `4917`, `4918` | resolve Object/slot applicability before programming |
| Conversion rules | catalogue-scoped | preserve applicable physical-to-advanced conversion through canonical resolver |

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item `1862` / `modobj = 21` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `36`, `184`, `546` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Temperature-control zone sensing; exact heating/cooling behavior remains firmware/Object-filter scoped.

## Observed behavior and corroboration

No sanitized hardware fingerprint or Device-specific protocol capture is currently retained for this exact technical item.

## Programming

Programming must select installed firmware applicability, resolve slot/Object alternatives through catalogue conditions, apply relation filters, and preserve configuration-mode boundaries.

## Source reconciliation

The canonical catalogue establishes the commercial records, firmware applicability, topology, configuration fields, filters and conditions. Publisher sources above are used only for behaviors they directly document; missing dedicated sheets remain explicit gaps.

## Evidence limits and open work

- Recover any missing dedicated publisher sheets for the exact identities.
- Capture a sanitized hardware fingerprint covering identity, firmware, modules, addressing and configuration.
- Corroborate condition/filter behavior through MyHOME Suite and controlled configuration changes.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
