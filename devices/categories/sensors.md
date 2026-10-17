# Sensors

Devices and interfaces for presence, daylight, temperature or consumption sensing. Passive infrared (PIR), ultrasonic (US) and infrared (IR) command functions remain distinct; pulse interfaces and meters report external measurements.

## Devices

| Device ID | Commercial references | Description | Relevant functions |
| --- | --- | --- | --- |
| [OWN-DEV-0010](../definitions/own-dev-0010-pir-us-daylight-presence-sensor.md) | `HC/HS/HD4658`, `L/N/NT4658N`, `YD4658` and variants | PIR+US daylight and presence sensor | Passive infrared and ultrasonic presence detection, daylight regulation and catalogue IR scenario-control roles |
| [OWN-DEV-0016](../definitions/own-dev-0016-pir-flush-mounted-sensor.md) | `HC4659`, `HS4659`, `HD4659` and variants | PIR daylight and presence sensor | Passive infrared presence/daylight sensing; catalogue IR scenario-control roles |
| [OWN-DEV-0031](../definitions/own-dev-0031-pir-surface-ceiling-mounted-sensor.md) | `BMSE1001`, `048833` | Surface-mounted ceiling presence sensor | Passive infrared presence and daylight sensing; published coverage depends on mounting height |
| [OWN-DEV-0034](../definitions/own-dev-0034-radio-interface-temperature-probes.md) | `L/N/NT4577`, `HC/HS/HD4577` | Radio interface for temperature probes | Two configured radio-probe channels; temperature and lighting-sensor modes remain distinct |
| [OWN-DEV-0038](../definitions/own-dev-0038-probe-with-regulation.md) | `L/N/NT4692`, `AM5872`, `HC/HS/HD4692` and variants | Temperature probe with regulation control | Room sensing, local setpoint adjustment and normal/protection/off selection |
| [OWN-DEV-0040](../definitions/own-dev-0040-fan-coil-probe.md) | `L/N/NT4692FAN`, `HC/HS/HD4692FAN`, `573924` and variants | Fan-coil temperature probe | Room sensing, setpoint/mode selection and automatic or manual fan-speed control |
| [OWN-DEV-0041](../definitions/own-dev-0041-basic-temperature-probe.md) | `HC/HS/HD4693`, `L/N/NT4693`, `573920` and variants | Temperature probe without local selector | Master/slave room sensing and configured zone regulation; central-unit mode control |
| [OWN-DEV-0046](../definitions/own-dev-0046-display-thermostat-2-modules.md) | `H4691`, `LN4691`, `067459` and variants | Display thermostat | Temperature and fan controls; central-unit probe, hotel or standalone modes |
| [OWN-DEV-0051](../definitions/own-dev-0051-pir-ceiling-mounted-sensor.md) | `BMSE3001`, `048820` | PIR ceiling-mounted sensor | PIR presence and daylight sensing; ceiling installation |
| [OWN-DEV-0053](../definitions/own-dev-0053-ultrasonic-ceiling-sensor-ir-port.md) | `BMSE3002`, `048821` | Ultrasonic ceiling sensor with IR port | Ultrasonic presence and daylight sensing; detailed exact-product sheet gap remains explicit |
| [OWN-DEV-0054](../definitions/own-dev-0054-pir-us-ceiling-mounted-sensor.md) | `BMSE3003`, `048822` | PIR+US ceiling-mounted sensor | Combined PIR and ultrasonic presence/daylight sensing; technology-specific coverage |
| [OWN-DEV-0055](../definitions/own-dev-0055-pir-us-wall-mounted-sensor.md) | `BMSE2005`, `048823` | PIR+US wall-mounted sensor | Combined PIR and ultrasonic presence/daylight sensing; wall or ceiling installation |
| [OWN-DEV-0056](../definitions/own-dev-0056-pir-wall-mounted-sensor-straight-range.md) | `BMSE2001`, `048824` | PIR wall-mounted sensor - straight range | Wide-beam PIR movement/daylight sensing; conflicting coverage figures retained |
| [OWN-DEV-0057](../definitions/own-dev-0057-pir-wall-mounted-sensor-short-range.md) | `BMSE2002`, `048825` | PIR wall-mounted sensor - short range | Narrow-beam PIR movement/daylight sensing; source-specific coverage matrices |
| [OWN-DEV-0058](../definitions/own-dev-0058-pir-wall-mounted-sensor-dual-range.md) | `BMSE2003`, `048826` | Bidirectional narrow-beam PIR wall/ceiling sensor | Bidirectional narrow-beam PIR movement/daylight sensing; revision-specific coverage limits |
| [OWN-DEV-0061](../definitions/own-dev-0061-pir-wall-mounted-sensor-long-range.md) | `BMSE2004`, `048829` | PIR wall-mounted sensor - long range | Long-range PIR and daylight; revision-specific coverage limits |
| [OWN-DEV-0062](../definitions/own-dev-0062-daylight-sensor-room-controller-rj45.md) | `BMSE3005`, `048828` | Daylight sensor for Room Controller + RJ45 | Catalogue-established Room Controller daylight sensing; physical technical-sheet gap explicit |
| [OWN-DEV-0063](../definitions/own-dev-0063-occupancy-sensor-ir-zigbee.md) | `BMSE2007`, `048831` | Occupancy sensor + IR + ZigBee | Catalogue-established IR/ZigBee occupancy role; radio/setup evidence gap explicit |
| [OWN-DEV-0084](../definitions/own-dev-0084-ip55-pir-wall-mounted-sensor.md) | `BMSE2006`, `048830` | IP55 PIR wall mounted sensor | PIR/daylight sensing; height/sensitivity coverage and physical/remote settings |
| [OWN-DEV-0096](../definitions/own-dev-0096-pulses-counter-interface.md) | `3522`, `003554` | Pulses counter interface | SCS pulse accounting; clock-dependent history and physical multiplier matrix |
| [OWN-DEV-0120](../definitions/own-dev-0120-three-input-electricity-meter.md) | `F520`, `003555` | Three-input electricity meter | Three toroid inputs, stored energy history and distinct Firmware/address scopes |
| [OWN-DEV-0121](../definitions/own-dev-0121-load-management-central-unit.md) | `F521`, `003557` | Load management central unit | Central load priority management and stored energy history |
| [OWN-DEV-0122](../definitions/own-dev-0122-load-actuator-current-sensor.md) | `F522`, `003558` | Load actuator with current sensor | One measured relay, local totalizers and optional residual-current sensor |
| [OWN-DEV-0150](../definitions/own-dev-0150-pulse-counter-interface.md) | `003576`, `3522N` | Pulse counter interface | Meter pulse conversion, flow calculation and stored consumption history; physical/software scale limits |
| [OWN-DEV-0197](../definitions/own-dev-0197-ip55-wall-mounted-pir-sensor.md) | `048834` | IP55 wall-mounted PIR sensor | IP55 long-range PIR; sensor/IR logical roles and unresolved catalogue/threshold/timing conflicts |
| [OWN-DEV-0204](../definitions/own-dev-0204-3454-temperature-probe-external-wired-sensors.md) | `3454` | 3454 temperature probe for external wired sensors | External wired temperature interface; validated sensor choices, actuator restrictions and no internal sensor |

## Evidence and applicability

See [Category evidence and applicability](README.md#evidence-and-applicability) for reference selection, source scope and installed-state limits.

## Related material

- [Device Categories](README.md)
- [Device Index](../index.md)
- [Functional Protocol](../../functional/)
