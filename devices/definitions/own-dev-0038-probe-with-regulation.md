# Probe with regulation

## Summary

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
| BTicino Living / LivingLight | `L/N/NT4692` | established grouped identity | catalogue + `MQ00179-c-EN` |
| BTicino Matix | `AM5872` | established identity | catalogue + `MQ00179-c-EN` |
| BTicino Axolute | `HC/HS/HD4692` | established grouped identity | catalogue + `MQ00179-c-EN` |
| Legrand Arteor | `573922` | established identity | catalogue + `MQ00179-c-EN` |
| Legrand Arteor | `573923` | established identity | catalogue + `MQ00179-c-EN` |
| Legrand Céliane | `067457` | established identity | catalogue + `MQ00179-c-EN` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00179-c-EN` | Technical sheet | revision c / date not pinned | current six-record probe family; physical operation and configuration | [Archived original](../../sources/devices/documents/device-doc-probe-regulation-mq00179-c-en/MQ00179-c-EN.pdf) | [Official source](https://dar.bticino.com/asset/Documents/MQ00179_c_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 2 wiring-device modules | publisher product family data |
| Temperature measurement range | `0..40 °C` | publisher product data |
| Local setpoint adjustment | approximately `-3..+3 °C` around the central setpoint | `MQ00179-c-EN` |
| Local modes | normal regulation, antifreeze and OFF | `MQ00179-c-EN` |
| Local indicators | green/yellow status and fault LEDs | `MQ00179-c-EN` |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1854` | Implementation evidence |
| Main system | Temperature control | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `20` | Implementation evidence |
| Catalogue buses | `1`, `2` | Implementation evidence |
| Commercial records | `6` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `260` | `5` | `2` | `0` | `1` | catalogue default | earlier catalogue line |
| `184` | `6` | `0` | `0` | `1` | non-default | later catalogue line |

Both firmware lines remain part of the current canonical implementation source and share the same fixed Master probe Object.

## Module, Object, and Virgin Object model

| Firmware | Module / slot | Object | Relationship |
| --- | --- | --- | --- |
| `260` | `1` | `184` Master probe | fixed |
| `184` | `1` | `184` Master probe | fixed |

No Virgin Object relation is required for the fixed topology.

## Configuration modes

| Firmware | Mode | Meaning |
| --- | --- | --- |
| `260` | `1` | Physical configuration |
| `260` | `3` | Advanced Configuration |
| `184` | `1` | Physical configuration |
| `184` | `2` | Virtual Configuration |
| `184` | `3` | Advanced Configuration |

## Firmware-scoped configuration

| Field | Firmware `260` | Firmware `184` | Default | Meaning |
| --- | --- | --- | --- | --- |
| `AID` | Device identity | Device identity | - | implementation identity |
| `ZA` | `0..9` | `0..9` | `0` | tens digit of temperature-control zone |
| `ZB` | `0..9` | `0..9` | `1` | units digit of temperature-control zone |
| `SLA` | `0..8` | `0..9` | `0` | slave-probe selector / relationship |

The `SLA` domain differs between the `5.2.0` and `6.0.0` catalogue lines and is therefore firmware-scoped rather than normalized.

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

The Master probe Object is reusable and substantially wider than the four firmware-level physical fields. These Object fields represent software-configurable zone behavior, actuator/pump topology and regulation parameters; their existence does not mean every value is exposed by both firmware lines.

## Conditions, filters, and conversions

| Condition ID | Firmware | Slot | Predicate | Conversion |
| --- | --- | --- | --- | --- |
| `4163` | `260` | `1` | empty source condition | conversion rule `1000` |
| `4163` | `184` | `1` | empty source condition | conversion rule `1000` |

Conversion rule `1000` maps physical `ZA`/`ZB` digits into Object field `ZAZB`. For `ZA=0`, valid mappings begin at `ZB=1` and produce `01..09`; `ZA=1..9` maps `ZB=0..9` to `10..99`.

| Firmware | Object | Catalogue filter IDs | Scope |
| --- | --- | --- | --- |
| `260` | `184` | `1390`, `1391`, `1392`, `1393`, `1394`, `1395`, `1396`, `1397`, `1398`, `1399`, `1400`, `1401`, `1402`, `1403`, `1404`, `1405`, `1406`, `1407`, `1408`, `1409`, `1410`, `1411`, `1412`, `1413`, `1414`, `1415`, `1416`, `1417`, `1418`, `1419`, `1420`, `1421`, `1422`, `1424`, `1425`, `1426`, `1427`, `1428`, `1429`, `1430`, `1431`, `1432`, `1433`, `1434`, `1435`, `1436`, `1437`, `1438`, `1439`, `1440`, `1441`, `1442`, `1443`, `1444`, `1445`, `1446`, `1447`, `1448`, `1449`, `1450`, `1451`, `1452`, `1453`, `1454`, `1455`, `1916`, `2679`, `2686`, `2693`, `2700`, `2707`, `2714`, `2721`, `2728`, `2735`, `2742`, `2749`, `2756`, `2763`, `2770`, `2777`, `2784`, `2800`, `2807`, `2814`, `2821`, `2828`, `2835`, `2842`, `2849`, `2856`, `2863`, `2870`, `2877`, `2884`, `2891`, `2898`, `2905`, `2912`, `2919`, `2926`, `2933`, `2940`, `2947`, `2954` | filtered Master-probe surface for firmware `5.2.0` |
| `184` | `184` | `636`, `637`, `638`, `639`, `640`, `641`, `642`, `643`, `644`, `645`, `646`, `647`, `648`, `649`, `650`, `651`, `652`, `653`, `654`, `655`, `656`, `657`, `658`, `659`, `662`, `663`, `664`, `665`, `666`, `667`, `668`, `1915`, `2673`, `2678`, `2685`, `2692`, `2699`, `2706`, `2713`, `2720`, `2727`, `2734`, `2741`, `2748`, `2755`, `2762`, `2769`, `2776`, `2783`, `2794`, `2799`, `2806`, `2813`, `2820`, `2827`, `2834`, `2841`, `2848`, `2855`, `2862`, `2869`, `2876`, `2883`, `2890`, `2897`, `2904`, `2911`, `2918`, `2925`, `2932`, `2939`, `2946`, `2953` | filtered Master-probe surface for firmware `6.0.0` |

The filter sets constrain the reusable Object surface and must be applied per Object/Firmware relation instead of treating every Master-probe field as unconditional.

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

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained. The local control behavior and indicators are publisher-documented rather than inferred from the database.

## Programming

Programming must convert `ZA`/`ZB` into `ZAZB` using the catalogue conversion rule and apply the filter set for the installed firmware. Software must not silently widen firmware `260` `SLA=0..8` to the later `0..9` domain.

## Source reconciliation

`MQ00179-c-EN` establishes the product family, local ±3 °C adjustment, antifreeze/OFF behavior and indicator semantics. The catalogue establishes two firmware lines, one fixed Object `184`, the exact `ZA`/`ZB`/`SLA` firmware surface and the large reusable Master-probe software surface.

The main catalogue difference is `SLA`: firmware `260` stores `0..8` while firmware `184` stores `0..9`. The difference remains explicitly firmware-scoped.

## Evidence limits and open work

- Hardware-corroborate firmware selection and `DIMENSION 2` on representative 4692-family units.
- Verify the firmware-specific `SLA` limits through actual configuration reads/writes.
- Corroborate the filtered Master-probe Object surface against MyHOME Suite for both firmware lines.

## Sources

- [Device Source Index](../../sources/devices/index.md)
- [Device Database Inventory](../inventory/)
- [`MQ00179-c-EN` archived original](../../sources/devices/documents/device-doc-probe-regulation-mq00179-c-en/MQ00179-c-EN.pdf)
