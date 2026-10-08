# Scenarios

Scenario storage/execution devices and controls with documented or catalogue-defined scenario-command roles. Recall controls, stored-scenario Modules and programmable schedulers perform different roles; a catalogue infrared (IR) scenario-control projection is not proof that the sensor stores scenarios.

Table abbreviations: UI = user interface; IR = infrared; PIR = passive infrared; US = ultrasonic; RFID = radio-frequency identification.

## Devices

| Device ID | Commercial references | Description | Relevant functions |
| --- | --- | --- | --- |
| [OWN-DEV-0010](../definitions/own-dev-0010-pir-us-daylight-presence-sensor.md) | `HC/HS/HD4658`, `L/N/NT4658N`, `YD4658` and variants | PIR+US daylight and presence sensor | Passive infrared and ultrasonic presence detection, daylight regulation and catalogue IR scenario-control roles |
| [OWN-DEV-0011](../definitions/own-dev-0011-scenario-control.md) | `HC4680`, `HS4680`, `HD4680` and variants | Scenario control | Scenario Module, CEN and PLUS scenario command roles |
| [OWN-DEV-0016](../definitions/own-dev-0016-pir-flush-mounted-sensor.md) | `HC4659`, `HS4659`, `HD4659` and variants | PIR daylight and presence sensor | Passive infrared presence/daylight sensing; catalogue IR scenario-control roles |
| [OWN-DEV-0018](../definitions/own-dev-0018-local-display.md) | `HC/HS/HD4685`, `L/N/NT4685`, `573916` and variants | Local Display | `FUN=1` scenario-Module control role |
| [OWN-DEV-0019](../definitions/own-dev-0019-three-module-touch-control.md) | `HC/HS4657M3`, `HD4657M3`, `573912` and variants | Three-module touch control | Six capacitive buttons for configured lighting, shutters, scenarios, sound or door entry |
| [OWN-DEV-0026](../definitions/own-dev-0026-four-scenario-control-unit.md) | `N4681` | Flush-mounted four-scenario control and storage unit | Four stored scenarios; master/slave, learn and erase |
| [OWN-DEV-0033](../definitions/own-dev-0033-light-manager-control-unit.md) | `BMNE500` | Light Manager control unit | Lighting supervision, scheduling, scenarios and Open SCS gateway |
| [OWN-DEV-0036](../definitions/own-dev-0036-key-card-switch.md) | `H4649`, `LN4649`, `572735` and variants | Key-card switch | Separate card-insertion and removal actions for configured scenarios or groups |
| [OWN-DEV-0039](../definitions/own-dev-0039-key-card-switch-rfid.md) | `H4648`, `LN4648`, `067566` and variants | RFID key-card switch | Card recognition with separately programmed insertion and removal actions |
| [OWN-DEV-0066](../definitions/own-dev-0066-scenario-module.md) | `F420`, `003551` | Scenario Module | Sixteen stored scenarios; revision-specific learning timeout and current limits |
| [OWN-DEV-0080](../definitions/own-dev-0080-scenario-programmer.md) | `MH200` | Scenario programmer | Programmable scenario collections; software/editor limits and evidence scope |
| [OWN-DEV-0094](../definitions/own-dev-0094-touch-control.md) | `HC/HS4657M3_OLD` | Touch control | Historical selectable lighting/shutter/scenario control plus UI; OLD revision boundaries |
| [OWN-DEV-0103](../definitions/own-dev-0103-eight-key-multifunction-control.md) | `H4652`, `LN4652`, `067592` | Eight-key multifunction control | Eight command keys and separate UI Module; mode-specific command learning |
| [OWN-DEV-0110](../definitions/own-dev-0110-two-module-myhome-unified-control.md) | `H4652M2`, `LN4652M2`, `067584` | Two-module MYHOME unified control | Catalogue command and shutter candidates; direct versus Virgin Object applicability |
| [OWN-DEV-0111](../definitions/own-dev-0111-three-module-myhome-unified-control.md) | `H4652M3`, `LN4652M3`, `067585` | Three-module MYHOME unified control | Three command positions plus UI; shared mode and scoped multi-slot functions |
| [OWN-DEV-0115](../definitions/own-dev-0115-living-now-full-digital-control.md) | `KW8011`, `KM8011`, `KG8011` | Living Now FULL digital control | Three touch areas with icons/proximity; one-slot or three-slot role boundaries |
| [OWN-DEV-0117](../definitions/own-dev-0117-two-module-light-now-multifunction-control.md) | `Y4652M2`, `MX5222`, `AA5222` | Two-module Light Now multifunction control | Two-module multifunction control; physical mode matrix and qualified feedback |
| [OWN-DEV-0119](../definitions/own-dev-0119-three-module-light-now-multifunction-control.md) | `Y4652M3`, `MX5223`, `AA5223` | Three-module Light Now multifunction control | Three-module multifunction control; functions selected by a shared physical mode selector |
| [OWN-DEV-0131](../definitions/own-dev-0131-mh200n-scenario-programmer.md) | `MH200N`, `003565` | MH200N scenario programmer | Scenario execution, clock/network access and OpenSCS gateway |
| [OWN-DEV-0137](../definitions/own-dev-0137-three-module-soft-touch-control.md) | `HC/HS4653/3`, `HD4653M3` | Three-module Soft Touch control | Capacitive control with alternative functions, UI settings and scoped Virgin Object candidates |
| [OWN-DEV-0151](../definitions/own-dev-0151-mh202-scenario-programmer.md) | `003535`, `MH202` | MH202 scenario programmer | 300 scenarios with trigger/condition/action limits and Firmware-specific configuration |
| [OWN-DEV-0200](../definitions/own-dev-0200-living-now-k4652m2-multifunction-control.md) | `K4652M2` | Living Now K4652M2 multifunction control | Living Now multifunction control; physical/virtual controls, roles exposed through Virgin Object associations and production/source restrictions |
| [OWN-DEV-0201](../definitions/own-dev-0201-living-now-k4652m3-three-function-control.md) | `K4652M3` | Living Now K4652M3 three-function control | Three-function SCS command; independent roles, physical/virtual settings and production-dependent group feedback |

## Evidence and applicability

See [Category evidence and applicability](README.md#evidence-and-applicability) for reference selection, source scope and installed-state limits.

## Related material

- [Device Categories](README.md)
- [Device Index](../index.md)
- [Functional Protocol](../../functional/)
