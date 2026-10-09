# Multifunction Devices

Devices that combine functional roles or offer a choice of configured applications. Alternative catalogue Objects are not necessarily active together, and a screen controlling a remote load is not itself its actuator.

Table abbreviations: UI = user interface; IR = infrared; PIR = passive infrared; DALI = Digital Addressable Lighting Interface; HVAC = heating, ventilation and air conditioning; PSTN = public switched telephone network; AUX = auxiliary.

## Devices

| Device ID | Commercial references | Description | Relevant functions |
| --- | --- | --- | --- |
| [OWN-DEV-0003](../definitions/own-dev-0003-flush-mounted-actuator-free-control.md) | `64391`, `64191`, `64192` and variants | Flush-mounted two-relay actuator and free control | Two local relays with configurable commands for remote loads or scenarios |
| [OWN-DEV-0004](../definitions/own-dev-0004-two-module-basic-control.md) | `H4652/2`, `L4652/2`, `AM5832/2` and variants | Two-module basic control | Configurable lighting, automation, scenario and AUX Objects |
| [OWN-DEV-0005](../definitions/own-dev-0005-two-module-special-control.md) | `H4651M2`, `L4651M2`, `AM5831M2` and variants | Two-module special control | Broad configurable command roles spanning several functional systems |
| [OWN-DEV-0006](../definitions/own-dev-0006-two-module-zero-crossing-actuator-control.md) | `64195`, `64196`, `64393` and variants | Two-module zero-crossing actuator and control | Two zero-crossing relays; local and remote command roles depend on configuration |
| [OWN-DEV-0007](../definitions/own-dev-0007-three-module-basic-control.md) | `H4652/3`, `L4652/3`, `AM5832/3` and variants | Three-module basic control | Three button pairs with independently configured lighting, shutter or scenario roles |
| [OWN-DEV-0009](../definitions/own-dev-0009-four-zone-touch-multifunction-control.md) | `573904`, `573905`, `573906` and variants | Four-zone touch multifunction control | Four touch zones with configurable lighting, shutter, scenario, sound or door-entry roles |
| [OWN-DEV-0012](../definitions/own-dev-0012-four-channel-ir-receiver.md) | `HC4654`, `HS4654`, `HD4654` and variants | Four-channel IR receiver | Four infrared command channels with mode-dependent lighting, shutter, scenario or sound functions |
| [OWN-DEV-0014](../definitions/own-dev-0014-extended-control.md) | `H4655`, `L4655`, `078466` and variants | Extended control | Configured remote commands across local and expanded bus domains |
| [OWN-DEV-0015](../definitions/own-dev-0015-myhome-screen-3-5.md) | `H4890`, `LN4890`, `LN4890A` and variants | MyHOME_Screen 3.5 | Multi-system touchscreen interface |
| [OWN-DEV-0016](../definitions/own-dev-0016-pir-flush-mounted-sensor.md) | `HC4659`, `HS4659`, `HD4659` and variants | PIR daylight and presence sensor | Passive infrared presence/daylight sensing; catalogue IR scenario-control roles |
| [OWN-DEV-0018](../definitions/own-dev-0018-local-display.md) | `HC/HS/HD4685`, `L/N/NT4685`, `573916` and variants | Local Display | Conditional scenario, sound-diffusion and temperature-probe roles |
| [OWN-DEV-0019](../definitions/own-dev-0019-three-module-touch-control.md) | `HC/HS4657M3`, `HD4657M3`, `573912` and variants | Three-module touch control | Six capacitive buttons for configured lighting, shutters, scenarios, sound or door entry |
| [OWN-DEV-0033](../definitions/own-dev-0033-light-manager-control-unit.md) | `BMNE500` | Light Manager control unit | Lighting supervision, scheduling, scenarios and Open SCS gateway |
| [OWN-DEV-0037](../definitions/own-dev-0037-local-display-1-2-bus.md) | `L/N/NT4891`, `HC/HS/HD4891`, `067271` and variants | Local Display 1.2 | Configured scenario, temperature, sound, consumption and load-management pages |
| [OWN-DEV-0043](../definitions/own-dev-0043-special-functions-control.md) | `H4651/2`, `L4651/2`, `AM5831/2` and variants | Two-module special-function control | Configured lighting, shutter, timed, scenario, sound and door-entry commands |
| [OWN-DEV-0047](../definitions/own-dev-0047-myhome-screen-10.md) | `MH4892`, `MH4893`, `067267` and variants | MyHOME_Screen 10 | Configured home controls, video entry and multimedia; room navigation and profiles |
| [OWN-DEV-0049](../definitions/own-dev-0049-myhome-screen-10-capacitive.md) | `MH4892C`, `MH4893C`, `067228` and variants | MyHOME_Screen 10C | Capacitive home-control/video interface; separate hardware and Firmware identity from Screen 10 |
| [OWN-DEV-0064](../definitions/own-dev-0064-room-controller-2-output-16-a.md) | `BMSW3002`, `048841` | Room Controller - 2 outputs 16 A | Two lighting outputs, powered local bus and combined 16 A maximum |
| [OWN-DEV-0070](../definitions/own-dev-0070-din-contacts-interface.md) | `F428`, `003553` | DIN contacts interface | Two contact inputs; revision-dependent lighting, automation and scenario roles |
| [OWN-DEV-0075](../definitions/own-dev-0075-room-controller-4-output-0-10-v.md) | `BMDI3002`, `048843` | Room Controller - 4 dimming outputs 0-10 V | Four analogue ballast channels and powered local bus; regional rating differences |
| [OWN-DEV-0076](../definitions/own-dev-0076-room-controller-2-universal-dimming-outputs.md) | `BMDI3301`, `048845` | Room Controller - 2 universal dimming outputs | Two independently regulated 1000 W outputs; exact regional sheet and load forcing |
| [OWN-DEV-0077](../definitions/own-dev-0077-multi-application-room-controller.md) | `BMSW3003`, `048847` | Multi-application Room Controller | One motor, one switched and two analogue channels; wiring/load conflicts explicit |
| [OWN-DEV-0079](../definitions/own-dev-0079-room-controller-2-output-0-10-v.md) | `BMDI3001`, `048842` | Room Controller - 2 dimming outputs 0-10 V | Two analogue ballast channels; shared local-bus budget and regional supply differences |
| [OWN-DEV-0082](../definitions/own-dev-0082-room-controller-1-output-16-amps.md) | `BMSW3001`, `048840` | Room Controller 1 Output 16 Amps | One lighting load and local sensor bus; relay/controller Modules separated |
| [OWN-DEV-0087](../definitions/own-dev-0087-gsm-burglar-alarm-central-unit.md) | `3486` | GSM burglar alarm central unit | Eight sensor zones; GSM/PSTN communication, scenarios and automations |
| [OWN-DEV-0088](../definitions/own-dev-0088-flush-mounted-alarm-central-unit.md) | `HC/HS/HD4601`, `L/N/NT4601` | Flush mounted alarm central unit | Four sensor zones; local contact/relay, learning and TiSecurityBasic programming |
| [OWN-DEV-0089](../definitions/own-dev-0089-webserver-audio-video-din.md) | `F453AV` | Webserver Audio/Video DIN | Web supervision, CCTV/answering services; PC/handheld limits and command confirmation |
| [OWN-DEV-0097](../definitions/own-dev-0097-video-station.md) | `349320`, `349321` | Video Station | Video entry and configurable MyHOME menus; USB projects, ringing and reset |
| [OWN-DEV-0102](../definitions/own-dev-0102-multimedia-touch-screen.md) | `HC4690`, `HD4690`, `HS4690` | Multimedia Touch Screen | Configured automation, media and energy projects; shared family battery evidence |
| [OWN-DEV-0103](../definitions/own-dev-0103-eight-key-multifunction-control.md) | `H4652`, `LN4652`, `067592` | Eight-key multifunction control | Eight command keys and separate UI Module; mode-specific command learning |
| [OWN-DEV-0107](../definitions/own-dev-0107-legrand-multimedia-touch-screen.md) | `067285`, `573963`, `573962` | Legrand Multimedia Touch Screen | Legrand multimedia and home control; D/G software settings and revision changes |
| [OWN-DEV-0110](../definitions/own-dev-0110-two-module-myhome-unified-control.md) | `H4652M2`, `LN4652M2`, `067584` | Two-module MYHOME unified control | Catalogue command and shutter candidates; direct versus Virgin Object applicability |
| [OWN-DEV-0111](../definitions/own-dev-0111-three-module-myhome-unified-control.md) | `H4652M3`, `LN4652M3`, `067585` | Three-module MYHOME unified control | Three command positions plus UI; shared mode and scoped multi-slot functions |
| [OWN-DEV-0112](../definitions/own-dev-0112-myhome-lighting-command-actuator.md) | `H4672M2L`, `LN4672M2L`, `067586` | MYHOME lighting command and actuator | Two lighting actuator placements plus commands; physical ratings undocumented |
| [OWN-DEV-0113](../definitions/own-dev-0113-myhome-shutter-command-actuator.md) | `H4672M2S`, `LN4672M2S`, `067587` | MYHOME shutter command and actuator | Shutter actuator plus commands; filtered motor type and calibration fields |
| [OWN-DEV-0115](../definitions/own-dev-0115-living-now-full-digital-control.md) | `KW8011`, `KM8011`, `KG8011` | Living Now FULL digital control | Three touch areas with icons/proximity; one-slot or three-slot role boundaries |
| [OWN-DEV-0116](../definitions/own-dev-0116-living-now-alexa-voice-control.md) | `KW8013`, `KM8013`, `KG8013` | Living Now Alexa voice control | Alexa voice/account service plus local touch lights; source-specific setup |
| [OWN-DEV-0117](../definitions/own-dev-0117-two-module-light-now-multifunction-control.md) | `Y4652M2`, `MX5222`, `AA5222` | Two-module Light Now multifunction control | Two-module multifunction control; physical mode matrix and qualified feedback |
| [OWN-DEV-0118](../definitions/own-dev-0118-light-now-lighting-actuator-control.md) | `Y4672M2L`, `MX5230`, `AA5230` | Light Now lighting actuator and control | Two lighting relays plus remote commands; source-specific LED and load limits |
| [OWN-DEV-0119](../definitions/own-dev-0119-three-module-light-now-multifunction-control.md) | `Y4652M3`, `MX5223`, `AA5223` | Three-module Light Now multifunction control | Three-module multifunction control; functions selected by a shared physical mode selector |
| [OWN-DEV-0121](../definitions/own-dev-0121-load-management-central-unit.md) | `F521`, `003557` | Load management central unit | Central load priority management and stored energy history |
| [OWN-DEV-0122](../definitions/own-dev-0122-load-actuator-current-sensor.md) | `F522`, `003558` | Load actuator with current sensor | One measured relay, local totalizers and optional residual-current sensor |
| [OWN-DEV-0123](../definitions/own-dev-0123-load-management-automation-actuator.md) | `F523`, `003559` | Load management and automation actuator | One unmetered relay combining load shedding and automation |
| [OWN-DEV-0124](../definitions/own-dev-0124-flush-mounted-load-management-actuator.md) | `HC/HS/HD4672N`, `L/N/NT4672N` | Flush-mounted load management actuator | Two-module flush relay with separate shedding indicator |
| [OWN-DEV-0127](../definitions/own-dev-0127-iryde-touch-phone.md) | `345020`, `345021` | Iryde Touch Phone | Touchscreen telephone with subsystem menus and USB/COM configuration |
| [OWN-DEV-0128](../definitions/own-dev-0128-four-channel-dali-room-controller.md) | `BMDI3101`, `048844` | Four-channel DALI room controller | Four DALI channels, supervised room control and four SCS branches |
| [OWN-DEV-0129](../definitions/own-dev-0129-polyx-memory-display.md) | `344163`, `067546` | Polyx Memory Display | Video handset, answering memory and physically selected preset menus |
| [OWN-DEV-0131](../definitions/own-dev-0131-mh200n-scenario-programmer.md) | `MH200N`, `003565` | MH200N scenario programmer | Scenario execution, clock/network access and OpenSCS gateway |
| [OWN-DEV-0132](../definitions/own-dev-0132-burglar-alarm-pstn-communicator.md) | `573934`, `067520` | Burglar alarm unit with PSTN communicator | PSTN alarm communication, local commissioning and voice-message programming |
| [OWN-DEV-0134](../definitions/own-dev-0134-energy-data-logger.md) | `F524`, `003566` | Energy data logger | Energy history, virtual lines and source-specific load forcing/reset workflows |
| [OWN-DEV-0135](../definitions/own-dev-0135-colour-touch-screen.md) | `H4684`, `L4684` | Colour Touch Screen | Colour touchscreen subsystem control and historical software editions |
| [OWN-DEV-0136](../definitions/own-dev-0136-infrared-air-conditioning-emitter.md) | `3456`, `088301` | Infrared air-conditioning emitter | Basic/advanced IR learning and split command-set transfer |
| [OWN-DEV-0137](../definitions/own-dev-0137-three-module-soft-touch-control.md) | `HC/HS4653/3`, `HD4653M3` | Three-module Soft Touch control | Capacitive control with alternative functions, UI settings and scoped Virgin Object candidates |
| [OWN-DEV-0144](../definitions/own-dev-0144-eight-output-temperature-control-actuator.md) | `003517`, `F430R8` | Eight-output temperature-control actuator | Eight relay outputs with application-specific output grouping |
| [OWN-DEV-0146](../definitions/own-dev-0146-relay-0-10v-fan-coil-actuator.md) | `003519`, `F430R3V10` | Relay and 0-10 V fan-coil actuator | Relay/proportional fan-coil control with production and Firmware boundaries |
| [OWN-DEV-0151](../definitions/own-dev-0151-mh202-scenario-programmer.md) | `003535`, `MH202` | MH202 scenario programmer | 300 scenarios with trigger/condition/action limits and Firmware-specific configuration |
| [OWN-DEV-0153](../definitions/own-dev-0153-two-channel-10a-universal-actuator.md) | `003848`, `F411U2` | Two-channel 10 A universal actuator | Two lighting relays or interlocked shutter motor; load/formula and Virgin Object field evidence reconciled |
| [OWN-DEV-0155](../definitions/own-dev-0155-classe-300x13e-connected-video-internal-unit.md) | `344642`, `344643` | Classe 300X13E connected video internal unit | Connected video entry with physical/advanced setup, recording and camera limits |
| [OWN-DEV-0156](../definitions/own-dev-0156-hometouch-home-automation-video-entry-display.md) | `067259`, `3488` | HOMETOUCH home automation and video-entry display | HOMETOUCH video/MyHOME control with mandatory supply and explicit server/alarm/load prerequisites |
| [OWN-DEV-0158](../definitions/own-dev-0158-easy-kit-connected-video-entry-kit.md) | `318011`, `369420` | Easy Kit Connected video-entry kit | 369420 kit wiring/expansion/reset scope with `318011` catalogue identity and documentation limits |
| [OWN-DEV-0159](../definitions/own-dev-0159-classe-300eos-connected-video-internal-unit.md) | `344842`, `344845` | Classe 300EOS connected video internal unit | EOS video/MyHOME commissioning, source-dependent recording/compatibility and hearing variant scope |
| [OWN-DEV-0161](../definitions/own-dev-0161-light-now-shutter-actuator-control.md) | `MX5220`, `Y4672M2S` | Light NOW shutter actuator and control | Local/remote shutter control with distinct Light NOW and Céliane indication and calibration limits |
| [OWN-DEV-0164](../definitions/own-dev-0164-axolute-eight-zone-touch-control.md) | `HC/HS/HD4657M4` | Axolute eight-zone touch control | Eight touch keys plus catalogue UI Module; SET modes, calibration and system batch prerequisites |
| [OWN-DEV-0165](../definitions/own-dev-0165-two-wire-concierge-switchboard.md) | `346310` | Two-wire concierge switchboard | Concierge call routing, hierarchical alarms, service priority and programmable keys |
| [OWN-DEV-0169](../definitions/own-dev-0169-sfera-keypad-module.md) | `353000` | Sfera keypad module | Standalone/Sfera keypad with explicit credential roles, central modes and group deletion |
| [OWN-DEV-0170](../definitions/own-dev-0170-sfera-proximity-badge-reader.md) | `353200` | Sfera proximity badge reader | Mifare Classic 1K reader with delegation, central mode and distinct deletion/reset scopes |
| [OWN-DEV-0175](../definitions/own-dev-0175-matix-colour-touchscreen.md) | `AM5864` | Matix colour touchscreen | Matix central MyHOME control with source-specific TiDisplay Color transfer and interface scopes |
| [OWN-DEV-0176](../definitions/own-dev-0176-livinglight-air-colour-touchscreen.md) | `LN4684A` | LivingLight Air colour touchscreen | LivingLight Air colour system-control interface; exact historical display/plate scope |
| [OWN-DEV-0177](../definitions/own-dev-0177-axolute-eteris-colour-touchscreen.md) | `HW4684` | Axolute Etèris colour touchscreen | Etèris monobloc central control with visually verified box/plate mounting branches |
| [OWN-DEV-0178](../definitions/own-dev-0178-mosaic-colour-touchscreen.md) | `078474` | Mosaic colour touchscreen | Mosaic lighting/blind local, zone, timed and locking control; separate finishing plates |
| [OWN-DEV-0179](../definitions/own-dev-0179-celiane-colour-touchscreen.md) | `067283` | Céliane colour touchscreen | Céliane central MyHOME control and documented network-media role; exact software/integration scopes |
| [OWN-DEV-0185](../definitions/own-dev-0185-legrand-area-manager.md) | `002645` | Legrand Area Manager | Lighting/scenario management with Ethernet and serial maintenance; separate auxiliary and SCS draws |
| [OWN-DEV-0186](../definitions/own-dev-0186-vigik-single-door-access-control-unit.md) | `348040` | Vigik single-door access-control unit | One Vigik reader and managed entrances; badge/reset effects, capacities and Firmware limits |
| [OWN-DEV-0190](../definitions/own-dev-0190-mh201-hotel-room-scenario-manager.md) | `MH201` | MH201 hotel room scenario manager | Hotel room gateway/scenarios; access/contact conditions, STOP behavior and trusted-IP scope |
| [OWN-DEV-0191](../definitions/own-dev-0191-3485std-burglar-alarm-local-contacts.md) | `3485STD` | 3485STD burglar-alarm unit with local contacts | Burglar-alarm control and PSTN reporting; local-contact, serial-maintenance and source-scoped supply/depth limits |
| [OWN-DEV-0192](../definitions/own-dev-0192-687408-colour-touchscreen.md) | `687408` | 687408 colour touchscreen | Catalogue colour touchscreen; two Firmware releases and Firmware-specific configuration fields; bounded exact-manual gap |
| [OWN-DEV-0193](../definitions/own-dev-0193-arteor-573960-colour-touchscreen.md) | `573960` | Arteor 573960 colour touchscreen | Arteor colour touchscreen; three Firmware releases; exact identity separated from adjacent mounting specifications |
| [OWN-DEV-0195](../definitions/own-dev-0195-arteor-573992-audio-video-web-server.md) | `573992` | Arteor 573992 audio and video web server | Audio/video web server and Open SCS gateway; Firmware-specific protocol applicability; bounded electrical/manual gap |
| [OWN-DEV-0198](../definitions/own-dev-0198-f459-driver-manager.md) | `F459` | F459 Driver Manager | Driver Manager; Nuvo association, driver lifecycle, access configuration and exporter discrepancies |
| [OWN-DEV-0199](../definitions/own-dev-0199-myhomeserver1-home-automation-server.md) | `MyHomeServer1` | MyHOMEServer1 home automation server | MyHOME server; app-generation capacities, Firmware requirements, network templates and scoped commissioning procedures |
| [OWN-DEV-0200](../definitions/own-dev-0200-living-now-k4652m2-multifunction-control.md) | `K4652M2` | Living Now K4652M2 multifunction control | Living Now multifunction control; physical/virtual controls, roles exposed through Virgin Object associations and production/source restrictions |
| [OWN-DEV-0201](../definitions/own-dev-0201-living-now-k4652m3-three-function-control.md) | `K4652M3` | Living Now K4652M3 three-function control | Three-function SCS command; independent roles, physical/virtual settings and production-dependent group feedback |
| [OWN-DEV-0202](../definitions/own-dev-0202-living-now-k4672m2l-light-actuator-control.md) | `K4672M2L` | Living Now K4672M2L light actuator and control | Two lighting relays and remote controls; neutral-dependent load matrix, Firmware restrictions and source conflicts |
| [OWN-DEV-0203](../definitions/own-dev-0203-living-now-k4672m2s-shutter-actuator-control.md) | `K4672M2S` | Living Now K4672M2S shutter actuator and control | Shutter actuator/control; local and remote role separation, calibration, pulse PRESET and production boundaries |
| [OWN-DEV-0204](../definitions/own-dev-0204-3454-temperature-probe-external-wired-sensors.md) | `3454` | 3454 temperature probe for external wired sensors | External wired temperature interface; validated sensor choices, actuator restrictions and no internal sensor |
| [OWN-DEV-0207](../definitions/own-dev-0207-f460-myhome-server.md) | `F460` | F460 MyHOME server | MyHOME server; branch capacity, commissioning, app/release boundaries and backup ownership/exclusions |
| [OWN-DEV-0208](../definitions/own-dev-0208-f461-myhome-server-third-party-integration.md) | `F461` | F461 MyHOME server for third-party integration | MyHOME server for third-party applications; shared commissioning, source row/application/dimension conflicts |
| [OWN-DEV-0209](../definitions/own-dev-0209-f459t-hvac-driver-manager.md) | `F459T` | F459T HVAC Driver Manager | HVAC Driver Manager catalogue identity; dual builds and full configuration metadata; exact-product documentation gap |

## Evidence and applicability

See [Category evidence and applicability](README.md#evidence-and-applicability) for reference selection, source scope and installed-state limits.

## Related material

- [Device Categories](README.md)
- [Device Index](../index.md)
- [Functional Protocol](../../functional/)
