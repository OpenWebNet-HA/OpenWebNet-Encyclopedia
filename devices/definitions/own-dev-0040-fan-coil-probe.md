# Fan-coil probe

## Summary

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
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00181-c-EN` | Technical sheet | revision c / 2014-04-29 | all five current identity groups; fan-coil operation and configuration | [Archived original](../../sources/devices/documents/device-doc-fancoil-probe-mq00181-c-en/MQ00181-c-EN.pdf) | [Official source](https://assets.legrand.com/general/mediagrp/np-ft-gt/mq00181-c-en.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | publisher product family data |
| Temperature measurement range | `0..40 °C` | publisher product data |
| Local setpoint adjustment | approximately `-3..+3 °C` around the central setpoint | `MQ00181-c-EN` |
| Local modes | normal regulation, antifreeze / thermal protection and OFF | `MQ00181-c-EN` |
| Fan control | automatic or manual fan-speed selection, including minimum / medium / maximum | `MQ00181-c-EN` |
| Local indicators | green/yellow status LEDs | `MQ00181-c-EN` |
| Zone capability | up to `9` same-type actuators and `8` slave probes in documented master configuration | `MQ00181-c-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1856` | Implementation evidence |
| Main system | Temperature control | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `19` | Implementation evidence |
| Catalogue buses | `1`, `2` | Implementation evidence |
| Commercial records | `5` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `261` | `5` | `2` | `-1` | `1` | catalogue default | build wildcard / unspecified |
| `185` | `6` | `0` | `0` | `1` | non-default | later catalogue line |

## Module, Object, and Virgin Object model

| Firmware | Module / slot | Object | Relationship |
| --- | --- | --- | --- |
| `261` | `1` | `184` Master probe | fixed |
| `185` | `1` | `184` Master probe | fixed |

No Virgin Object relation is required for the fixed topology.

## Configuration modes

| Firmware | Mode | Meaning |
| --- | --- | --- |
| `261` | `1` | Physical configuration |
| `261` | `3` | Advanced Configuration |
| `185` | `1` | Physical configuration |
| `185` | `2` | Virtual Configuration |
| `185` | `3` | Advanced Configuration |

## Firmware-scoped configuration

| Field | Firmware `261` | Firmware `185` | Default | Meaning |
| --- | --- | --- | --- | --- |
| `AID` | Device identity | Device identity | - | implementation identity |
| `ZA` | `0..9` | `0..9` | `0` | tens digit of temperature-control zone |
| `ZB` | `0..9` | `0..9` | `1` | units digit of temperature-control zone |
| `SLA` | `0..8` | `0..9` | `0` | slave-probe selector / relationship |

The default firmware `261` uses wildcard build `-1` and a narrower `SLA` domain than firmware `185`.

## Object configuration surfaces

### Object `184` - Master probe

| Surface | Fields | Meaning |
| --- | --- | --- |
| Zone and operating mode | `FUNCTION`, `ZAZB`, `COND`, `RISC`, `ZAZB_CENTRAL` | zone identity, heating/cooling operating role and central-unit relationship |
| Heating setpoints | `COMFORT_HEATING_SETPOINT`, `ECO_HEATING_SETPOINT`, `ANTIFREEZE_SETPOINT` | comfort, eco and antifreeze heating targets |
| Cooling setpoints | `COMFORT_COOLING_SETPOINT`, `ECO_COOLING_SETPOINT`, `THERMAL_PROTECTION_SETPOINT` | comfort, eco and thermal-protection cooling targets |
| Heating regulation and fan-coil | `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL`, `HEATING_THRESHOLDS_SETTINGS`, `HEATING_REGULATION_BAND`, `HEATING_FAN_COIL_SPEED_2_THRESHOLD`, `HEATING_FAN_COIL_SPEED_3_THRESHOLD`, `HEATING_FANCOIL_VENTILATION_FUNCTION`, `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT`, `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | heating regulation bands, thresholds, fan timing and ventilation behavior |
| Cooling regulation and fan-coil | `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL`, `COOLING_THRESHOLDS_SETTINGS`, `COOLING_REGULATION_BAND`, `COOLING_FAN_COIL_SPEED_2_THRESHOLD`, `COOLING_FAN_COIL_SPEED_3_THRESHOLD`, `COOLING_FANCOIL_VENTILATION_FUNCTION`, `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT`, `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | cooling regulation bands, thresholds, fan timing and ventilation behavior |
| Local contacts | `HEATING_CONTACT_OPENING`, `HEATING_CONTACT_CLOSING`, `HEATING_CONTACT_OPENING_ACTIVATION_DELAY`, `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY`, `HEATING_CONTACT_OPENING_TIMEOUT`, `HEATING_CONTACT_CLOSING_TIMEOUT`, `HEATING_CONTACT_PUSHBTN_LOCK`, `COOLING_CONTACT_OPENING`, `COOLING_CONTACT_CLOSING`, `COOLING_CONTACT_OPENING_ACTIVATION_DELAY`, `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY`, `COOLING_CONTACT_OPENING_TIMEOUT`, `COOLING_CONTACT_CLOSING_TIMEOUT`, `COOLING_CONTACT_PUSHBTN_LOCK`, `WINDOWS_CONTACT_ICON`, `WINDOWS_CONTACT_NUMBER` | local opening/closing actions, delays, timeouts and locks |
| Actuator topology | `ACTUATOR_N=1_FUNCTION`, `ACTUATOR_N=2_FUNCTION`, `ACTUATOR_N=3_FUNCTION`, `ACTUATOR_N=4_FUNCTION`, `ACTUATOR_N=5_FUNCTION`, `ACTUATOR_N=6_FUNCTION`, `ACTUATOR_N=7_FUNCTION`, `ACTUATOR_N=8_FUNCTION`, `ACTUATOR_N=9_FUNCTION`, `ACTUATOR_N=1_TYPE`, `ACTUATOR_N=2_TYPE`, `ACTUATOR_N=3_TYPE`, `ACTUATOR_N=4_TYPE`, `ACTUATOR_N=5_TYPE`, `ACTUATOR_N=6_TYPE`, `ACTUATOR_N=7_TYPE`, `ACTUATOR_N=8_TYPE`, `ACTUATOR_N=9_TYPE`, `HEATING_ACTUATOR_TYPE`, `COOLING_ACTUATOR_TYPE` | functions and types for the numbered zone actuators |
| Pump topology | `PUMP_N=1_FUNCTION`, `PUMP_N=2_FUNCTION`, `PUMP_N=3_FUNCTION`, `PUMP_N=4_FUNCTION`, `PUMP_N=5_FUNCTION`, `PUMP_N=6_FUNCTION`, `PUMP_N=7_FUNCTION`, `PUMP_N=8_FUNCTION`, `PUMP_N=9_FUNCTION`, `HEATING_PUMP_DELAY`, `COOLING_PUMP_DELAY` | pump functions and activation timing |
| PID and proportional control | `HEATING_PID_REGULATION_BAND`, `HEATING_PID_INERTIA`, `HEATING_PROPORTIONAL_GAIN_LOW`, `HEATING_PROPORTIONAL_GAIN_HIGH`, `HEATING_INTEGRATIVE_GAIN_LOW`, `HEATING_INTEGRATIVE_GAIN_HIGH`, `HEATING_DERIVATIVE_GAIN_LOW`, `HEATING_DERIVATIVE_GAIN_HIGH`, `HEATING_PROPORTIONAL_SPEED_1`, `HEATING_PROPORTIONAL_SPEED_2`, `HEATING_PROPORTIONAL_SPEED_3`, `COOLING_PID_REGULATION_BAND`, `COOLING_PID_INERTIA`, `COOLING_PROPORTIONAL_GAIN_LOW`, `COOLING_PROPORTIONAL_GAIN_HIGH`, `COOLING_INTEGRATIVE_GAIN_LOW`, `COOLING_INTEGRATIVE_GAIN_HIGH`, `COOLING_DERIVATIVE_GAIN_LOW`, `COOLING_DERIVATIVE_GAIN_HIGH`, `COOLING_PROPORTIONAL_SPEED_1`, `COOLING_PROPORTIONAL_SPEED_2`, `COOLING_PROPORTIONAL_SPEED_3` | PID/proportional tuning and staged fan-speed control |
| User interface and local behavior | `NUMBER_OF_SLAVES`, `LED_ENABLE`, `TEMPERATURE_FORMAT`, `BACKLIGHT_STAND_BY_LEVEL`, `AMBIENT_TEMPERATURE_VISUALIZATION`, `BACKLIGHT_STANDBY_LEVEL`, `PUSHBUTTON_MANAGEMENT`, `PUSHBUTTON_MODALITY_CHANGE`, `CALIBRATION_PROCEDURE`, `USER_SETTINGS_PROCEDURE` | display, LED, pushbutton, calibration and local interaction settings |
| Other validated settings | `HEATING_ANTI_SEIZING_UP_PROTECTION`, `COOLING_ANTI_SEIZING_UP_PROTECTION` | remaining reusable Master-probe settings not covered by the groups above |

For this Device, the fan-coil, ventilation, threshold and fan-speed settings are especially relevant. The same reusable Master probe Object also contains generic actuator, pump, contact, PID and setpoint surfaces; applicability remains filter- and firmware-scoped.

## Conditions, filters, and conversions

| Condition ID | Firmware | Slot | Predicate | Conversion |
| --- | --- | --- | --- | --- |
| `4163` | `261` | `1` | empty source condition | conversion rule `1000` |
| `4163` | `185` | `1` | empty source condition | conversion rule `1000` |

Conversion rule `1000` combines `ZA`/`ZB` into Object field `ZAZB`, producing zone `01..99` without a `00` mapping.

| Firmware | Object | Catalogue filter IDs | Scope |
| --- | --- | --- | --- |
| `261` | `184` | `1456`, `1457`, `1458`, `1459`, `1460`, `1461`, `1462`, `1463`, `1464`, `1465`, `1466`, `1467`, `1468`, `1469`, `1470`, `1471`, `1472`, `1473`, `1474`, `1475`, `1476`, `1477`, `1478`, `1479`, `1480`, `1481`, `1482`, `1483`, `1484`, `1485`, `1486`, `1487`, `1488`, `1489`, `1490`, `1491`, `1492`, `1493`, `1494`, `1495`, `1496`, `1497`, `1498`, `1499`, `1500`, `1501`, `1502`, `1503`, `1504`, `1505`, `1506`, `1507`, `1508`, `1509`, `1510`, `1511`, `1512`, `1513`, `1514`, `1515`, `1516`, `1517`, `1518`, `1520`, `1521`, `1917`, `2680`, `2687`, `2694`, `2701`, `2708`, `2715`, `2722`, `2729`, `2736`, `2743`, `2750`, `2757`, `2764`, `2771`, `2778`, `2785`, `2801`, `2808`, `2815`, `2822`, `2829`, `2836`, `2843`, `2850`, `2857`, `2864`, `2871`, `2878`, `2885`, `2892`, `2899`, `2906`, `2913`, `2920`, `2927`, `2934`, `2941`, `2948`, `2955` | filtered Master-probe/fan-coil surface for firmware `5.2.-1` |
| `185` | `184` | `507`, `508`, `509`, `510`, `511`, `512`, `513`, `514`, `515`, `516`, `517`, `518`, `519`, `520`, `521`, `522`, `523`, `524`, `525`, `526`, `527`, `528`, `529`, `530`, `531`, `532`, `533`, `534`, `535`, `536`, `537`, `538`, `539`, `1913`, `2671`, `2676`, `2683`, `2690`, `2697`, `2704`, `2711`, `2718`, `2725`, `2732`, `2739`, `2746`, `2753`, `2760`, `2767`, `2774`, `2781`, `2792`, `2797`, `2804`, `2811`, `2818`, `2825`, `2832`, `2839`, `2846`, `2853`, `2860`, `2867`, `2874`, `2881`, `2888`, `2895`, `2902`, `2909`, `2916`, `2923`, `2930`, `2937`, `2944`, `2951` | filtered Master-probe/fan-coil surface for firmware `6.0.0` |

The filter sets include fan-coil timing/thresholds, actuator and pump functions, local-contact behavior, display settings and PID/proportional control. They are relation-specific constraints, not standalone universal Object defaults.

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

## Observed behavior and corroboration

No sanitized hardware fingerprint is currently retained. Fan-speed behavior, local setpoint adjustment and master-zone capability are publisher-documented and still need protocol-level corroboration.

## Programming

Programming must apply the installed firmware's filter set, convert `ZA`/`ZB` to `ZAZB` and preserve the `SLA` difference between firmware lines. Fan-coil controls should be exposed only where their relation-specific filters permit them.

## Source reconciliation

`MQ00181-c-EN` establishes the fan-coil product family, local ±3 °C setpoint adjustment, fan-speed controls, indicators and master-zone capabilities. The catalogue establishes the two firmware lines, fixed Object `184`, `ZA`/`ZB`/`SLA` surface, zone conversion and relation-specific filtered Master-probe configuration.

As with the non-fan probe, `SLA` differs by firmware: `0..8` on firmware `261` and `0..9` on firmware `185`. Firmware `261` also uses build sentinel `-1` rather than a concrete build number.

## Evidence limits and open work

- Hardware-corroborate automatic/manual fan-speed behavior and the exposed Object fields.
- Confirm installed build reporting for firmware `261` rather than interpreting catalogue `-1` as a runtime value.
- Verify `SLA` limits and relation-specific fan-coil filters through configuration reads/writes.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MQ00181-c-EN` archived original](../../sources/devices/documents/device-doc-fancoil-probe-mq00181-c-en/MQ00181-c-EN.pdf)
