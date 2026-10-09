# Thermoregulation

Temperature sensors, local controls, central units, thermal actuators and integration interfaces. Sensor inputs, regulation decisions and load outputs are distinct roles; combined devices can appear in several categories.

Table abbreviations: IR = infrared; HVAC = heating, ventilation and air conditioning.

## Devices

| Device ID | Commercial references | Description | Relevant functions |
| --- | --- | --- | --- |
| [OWN-DEV-0017](../definitions/own-dev-0017-flush-mounted-temperature-central-unit.md) | `HC/HS4695`, `HD4695`, `L/N/NT4695` and variants | Four-zone temperature central unit | Scheduling, four-zone control and thermoregulation configuration |
| [OWN-DEV-0018](../definitions/own-dev-0018-local-display.md) | `HC/HS/HD4685`, `L/N/NT4685`, `573916` and variants | Local Display | `FUN`-selected local temperature-probe role |
| [OWN-DEV-0034](../definitions/own-dev-0034-radio-interface-temperature-probes.md) | `L/N/NT4577`, `HC/HS/HD4577` | Radio interface for temperature probes | Two configured radio-probe channels; temperature and lighting-sensor modes remain distinct |
| [OWN-DEV-0038](../definitions/own-dev-0038-probe-with-regulation.md) | `L/N/NT4692`, `AM5872`, `HC/HS/HD4692` and variants | Temperature probe with regulation control | Room sensing, local setpoint adjustment and normal/protection/off selection |
| [OWN-DEV-0040](../definitions/own-dev-0040-fan-coil-probe.md) | `L/N/NT4692FAN`, `HC/HS/HD4692FAN`, `573924` and variants | Fan-coil temperature probe | Room sensing, setpoint/mode selection and automatic or manual fan-speed control |
| [OWN-DEV-0041](../definitions/own-dev-0041-basic-temperature-probe.md) | `HC/HS/HD4693`, `L/N/NT4693`, `573920` and variants | Temperature probe without local selector | Master/slave room sensing and configured zone regulation; central-unit mode control |
| [OWN-DEV-0042](../definitions/own-dev-0042-temperature-control-central-unit.md) | `3550`, `067456`, `573918` and variants | 99-zone temperature-control central unit | Heating/cooling schedules, zone settings, scenarios and holiday modes |
| [OWN-DEV-0046](../definitions/own-dev-0046-display-thermostat-2-modules.md) | `H4691`, `LN4691`, `067459` and variants | Display thermostat | Temperature and fan controls; central-unit probe, hotel or standalone modes |
| [OWN-DEV-0109](../definitions/own-dev-0109-living-now-thermostat-with-display.md) | `KM4691`, `KG4691`, `KW4691` | Living Now thermostat with display | Local and configured temperature control; scaled fields and source-specific restrictions |
| [OWN-DEV-0133](../definitions/own-dev-0133-four-output-fil-pilote-actuator.md) | `003577`, `F430FP` | Four-output Fil Pilote actuator | Four independent pilot-wire heating outputs and local OFF/Comfort behavior |
| [OWN-DEV-0136](../definitions/own-dev-0136-infrared-air-conditioning-emitter.md) | `3456`, `088301` | Infrared air-conditioning emitter | Basic/advanced IR learning and split command-set transfer |
| [OWN-DEV-0138](../definitions/own-dev-0138-open-bacnet-gateway.md) | `F450`, `003597` | OPEN and BACnet gateway | OPEN/BACnet HVAC bridge with edition-specific software classes |
| [OWN-DEV-0144](../definitions/own-dev-0144-eight-output-temperature-control-actuator.md) | `003517`, `F430R8` | Eight-output temperature-control actuator | Eight relay outputs with application-specific output grouping |
| [OWN-DEV-0145](../definitions/own-dev-0145-two-output-0-10v-valve-actuator.md) | `003518`, `F430V10` | Two-output 0-10 V valve actuator | Two proportional valve outputs and normal/OFF software paths |
| [OWN-DEV-0146](../definitions/own-dev-0146-relay-0-10v-fan-coil-actuator.md) | `003519`, `F430R3V10` | Relay and 0-10 V fan-coil actuator | Relay/proportional fan-coil control with production and Firmware boundaries |
| [OWN-DEV-0147](../definitions/own-dev-0147-two-relay-temperature-control-actuator.md) | `003579`, `F430/2` | Two-relay temperature-control actuator | Two relay loads, interlock and zone-00 pump configuration |
| [OWN-DEV-0148](../definitions/own-dev-0148-four-relay-temperature-control-actuator.md) | `003580`, `F430/4` | Four-relay temperature-control actuator | Four common-contact relay outputs with physical/software role discrepancies |
| [OWN-DEV-0204](../definitions/own-dev-0204-3454-temperature-probe-external-wired-sensors.md) | `3454` | 3454 temperature probe for external wired sensors | External wired temperature interface; validated sensor choices, actuator restrictions and no internal sensor |
| [OWN-DEV-0209](../definitions/own-dev-0209-f459t-hvac-driver-manager.md) | `F459T` | F459T HVAC Driver Manager | Catalogue-identified HVAC integration manager; exact supported systems remain documentation gaps |

## Evidence and applicability

See [Category evidence and applicability](README.md#evidence-and-applicability) for reference selection, source scope and installed-state limits.

## Related material

- [Device Categories](README.md)
- [Device Index](../index.md)
- [Functional Protocol](../../functional/)
