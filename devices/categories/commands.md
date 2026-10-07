# Commands

Controls and input interfaces that send configured commands to other system devices. A command role does not imply a local load output; combined products are also listed under Actuators.

Table abbreviations: UI = user interface; IR = infrared; RFID = radio-frequency identification; AUX = auxiliary.

## Devices

| Device ID | Commercial references | Description | Relevant functions |
| --- | --- | --- | --- |
| [OWN-DEV-0003](../definitions/own-dev-0003-flush-mounted-actuator-free-control.md) | `64391`, `64191`, `64192` and variants | Flush-mounted two-relay actuator and free control | Two local relays with configurable commands for remote loads or scenarios |
| [OWN-DEV-0004](../definitions/own-dev-0004-two-module-basic-control.md) | `H4652/2`, `L4652/2`, `AM5832/2` and variants | Two-module basic control | Lighting, automation, scenario, PLUS scenario, AUX command roles |
| [OWN-DEV-0005](../definitions/own-dev-0005-two-module-special-control.md) | `H4651M2`, `L4651M2`, `AM5831M2` and variants | Two-module special control | Lighting, automation, locking, scenario, video-door-entry, sound, AUX roles |
| [OWN-DEV-0006](../definitions/own-dev-0006-two-module-zero-crossing-actuator-control.md) | `64195`, `64196`, `64393` and variants | Two-module zero-crossing actuator and control | Two zero-crossing relays; local and remote command roles depend on configuration |
| [OWN-DEV-0007](../definitions/own-dev-0007-three-module-basic-control.md) | `H4652/3`, `L4652/3`, `AM5832/3` and variants | Three-module basic control | Three button pairs with independently configured lighting, shutter or scenario roles |
| [OWN-DEV-0009](../definitions/own-dev-0009-four-zone-touch-multifunction-control.md) | `573904`, `573905`, `573906` and variants | Four-zone touch multifunction control | Four touch zones with configurable lighting, shutter, scenario, sound or door-entry roles |
| [OWN-DEV-0011](../definitions/own-dev-0011-scenario-control.md) | `HC4680`, `HS4680`, `HD4680` and variants | Scenario control | Scenario Module, CEN and PLUS scenario commands |
| [OWN-DEV-0012](../definitions/own-dev-0012-four-channel-ir-receiver.md) | `HC4654`, `HS4654`, `HD4654` and variants | Four-channel IR receiver | Four infrared command channels with mode-dependent lighting, shutter, scenario or sound functions |
| [OWN-DEV-0014](../definitions/own-dev-0014-extended-control.md) | `H4655`, `L4655`, `078466` and variants | Extended control | Configured remote commands across local and expanded bus domains |
| [OWN-DEV-0019](../definitions/own-dev-0019-three-module-touch-control.md) | `HC/HS4657M3`, `HD4657M3`, `573912` and variants | Three-module touch control | Six capacitive buttons for configured lighting, shutters, scenarios, sound or door entry |
| [OWN-DEV-0024](../definitions/own-dev-0024-two-module-soft-touch-control.md) | `HC/HS4653/2`, `HD4653M2` | Two-module capacitive Soft Touch SCS command with configurable function and UI settings | Configured lighting, scenarios, sound and door-entry command roles; separate UI settings |
| [OWN-DEV-0028](../definitions/own-dev-0028-rotary-regulation-control.md) | `HC/HS/HD4563`, `L/N/NT4563` | Flush-mounted rotary SCS control | Advanced dimmer adjustment and sound volume/source controls; mode-specific settings |
| [OWN-DEV-0035](../definitions/own-dev-0035-flush-mounted-radio-receiver-batteryless-control.md) | `HC/HS/HD4575SB`, `L/N/NT4575SB` | Receiver for batteryless radio controls | Paired wireless controls send configured lighting, shutter or scenario commands to SCS |
| [OWN-DEV-0036](../definitions/own-dev-0036-key-card-switch.md) | `H4649`, `LN4649`, `572735` and variants | Key-card switch | Separate card-insertion and removal actions for configured scenarios or groups |
| [OWN-DEV-0039](../definitions/own-dev-0039-key-card-switch-rfid.md) | `H4648`, `LN4648`, `067566` and variants | RFID key-card switch | Card recognition with separately programmed insertion and removal actions |
| [OWN-DEV-0043](../definitions/own-dev-0043-special-functions-control.md) | `H4651/2`, `L4651/2`, `AM5831/2` and variants | Two-module special-function control | Configured lighting, shutter, timed, scenario, sound and door-entry commands |
| [OWN-DEV-0044](../definitions/own-dev-0044-shutter-control-bus.md) | `H4660M2`, `LN4660M2`, `AM5860M2` and variants | Advanced shutter control | Up/down/stop, position feedback and preset recall with compatible advanced actuators |
| [OWN-DEV-0060](../definitions/own-dev-0060-basic-control-actuator.md) | `3476` | Basic control actuator | One compact relay and normally open pushbutton input; cyclic, separate and timed control |
| [OWN-DEV-0070](../definitions/own-dev-0070-din-contacts-interface.md) | `F428`, `003553` | DIN contacts interface | Two contact inputs; revision-dependent lighting, automation and scenario roles |
| [OWN-DEV-0071](../definitions/own-dev-0071-module-contacts-interface.md) | `L/N/NT4688` | Module contacts interface | Two traditional contact inputs; catalogue and physical command scopes distinguished |
| [OWN-DEV-0072](../definitions/own-dev-0072-basic-contacts-interface.md) | `3477`, `573996`, `049238` | Basic contacts interface | Two dry-contact inputs for lighting, shutters, scenes and audio; source conflicts explicit |
| [OWN-DEV-0094](../definitions/own-dev-0094-touch-control.md) | `HC/HS4657M3_OLD` | Touch control | Historical selectable lighting/shutter/scenario control plus UI; OLD revision boundaries |
| [OWN-DEV-0103](../definitions/own-dev-0103-eight-key-multifunction-control.md) | `H4652`, `LN4652`, `067592` | Eight-key multifunction control | Eight command keys and separate UI Module; mode-specific command learning |
| [OWN-DEV-0104](../definitions/own-dev-0104-do-not-disturb-make-up-room-control.md) | `H4653`, `LN4653`, `067593` | Do Not Disturb / Make Up Room control | Do Not Disturb / Make Up Room status control; mode-specific covers and system wiring requirements |
| [OWN-DEV-0106](../definitions/own-dev-0106-rfid-reader-and-outside-door-indicator.md) | `H4651`, `LN4651`, `067591` | RFID reader and outside-door Do Not Disturb / Make Up Room indicator | RFID access commands and room indication; lot-specific compatibility |
| [OWN-DEV-0110](../definitions/own-dev-0110-two-module-myhome-unified-control.md) | `H4652M2`, `LN4652M2`, `067584` | Two-module MYHOME unified control | Catalogue command and shutter candidates; direct versus Virgin Object applicability |
| [OWN-DEV-0111](../definitions/own-dev-0111-three-module-myhome-unified-control.md) | `H4652M3`, `LN4652M3`, `067585` | Three-module MYHOME unified control | Three command positions plus UI; shared mode and scoped multi-slot functions |
| [OWN-DEV-0112](../definitions/own-dev-0112-myhome-lighting-command-actuator.md) | `H4672M2L`, `LN4672M2L`, `067586` | MYHOME lighting command and actuator | Two lighting actuator placements plus commands; physical ratings undocumented |
| [OWN-DEV-0113](../definitions/own-dev-0113-myhome-shutter-command-actuator.md) | `H4672M2S`, `LN4672M2S`, `067587` | MYHOME shutter command and actuator | Shutter actuator plus commands; filtered motor type and calibration fields |
| [OWN-DEV-0114](../definitions/own-dev-0114-living-now-light-digital-control.md) | `KW8010`, `KM8010`, `KG8010` | Living Now LIGHT digital control | One digital lighting control; two command functions and separate brightness |
| [OWN-DEV-0115](../definitions/own-dev-0115-living-now-full-digital-control.md) | `KW8011`, `KM8011`, `KG8011` | Living Now FULL digital control | Three touch areas with icons/proximity; one-slot or three-slot role boundaries |
| [OWN-DEV-0116](../definitions/own-dev-0116-living-now-alexa-voice-control.md) | `KW8013`, `KM8013`, `KG8013` | Living Now Alexa voice control | Alexa voice/account service plus local touch lights; source-specific setup |
| [OWN-DEV-0117](../definitions/own-dev-0117-two-module-light-now-multifunction-control.md) | `Y4652M2`, `MX5222`, `AA5222` | Two-module Light Now multifunction control | Two-module multifunction control; physical mode matrix and qualified feedback |
| [OWN-DEV-0118](../definitions/own-dev-0118-light-now-lighting-actuator-control.md) | `Y4672M2L`, `MX5230`, `AA5230` | Light Now lighting actuator and control | Two lighting relays plus remote commands; source-specific LED and load limits |
| [OWN-DEV-0119](../definitions/own-dev-0119-three-module-light-now-multifunction-control.md) | `Y4652M3`, `MX5223`, `AA5223` | Three-module Light Now multifunction control | Three-module multifunction control; functions selected by a shared physical mode selector |
| [OWN-DEV-0137](../definitions/own-dev-0137-three-module-soft-touch-control.md) | `HC/HS4653/3`, `HD4653M3` | Three-module Soft Touch control | Capacitive control with alternative functions, UI settings and scoped Virgin Object candidates |
| [OWN-DEV-0200](../definitions/own-dev-0200-living-now-k4652m2-multifunction-control.md) | `K4652M2` | Living Now K4652M2 multifunction control | Living Now multifunction control; physical/virtual controls, roles exposed through Virgin Object associations and production/source restrictions |
| [OWN-DEV-0201](../definitions/own-dev-0201-living-now-k4652m3-three-function-control.md) | `K4652M3` | Living Now K4652M3 three-function control | Three-function SCS command; independent roles, physical/virtual settings and production-dependent group feedback |
| [OWN-DEV-0202](../definitions/own-dev-0202-living-now-k4672m2l-light-actuator-control.md) | `K4672M2L` | Living Now K4672M2L light actuator and control | Two lighting relays and remote controls; neutral-dependent load matrix, Firmware restrictions and source conflicts |
| [OWN-DEV-0203](../definitions/own-dev-0203-living-now-k4672m2s-shutter-actuator-control.md) | `K4672M2S` | Living Now K4672M2S shutter actuator and control | Shutter actuator/control; local and remote role separation, calibration, pulse PRESET and production boundaries |

## Evidence and applicability

Each Device link leads to its canonical definition, including retained manufacturer sources, catalogue relationships, Firmware applicability and evidence limits. Commercial references are selected navigation labels; combined finish codes and variant lists are expanded there.

Category membership summarizes documented or catalogue-derived roles. It does not establish the installed Configuration, simultaneous availability of alternative Objects, universal OpenWebNet command support or current availability of historical services. Missing product-specific documentation is an evidence gap, not an unresolved commercial identity.

## Related material

- [Device Categories](README.md)
- [Device Index](../index.md)
- [Functional Protocol](../../functional/)
