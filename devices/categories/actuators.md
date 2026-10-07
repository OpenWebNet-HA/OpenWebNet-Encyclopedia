# Actuators

Devices that switch, dim or regulate loads, plus the lighting-state memory module. Combined actuator/control products may also appear under Commands or Multifunction Devices.

Table abbreviations: DALI = Digital Addressable Lighting Interface.

## Devices

| Device ID | Commercial references | Description | Relevant functions |
| --- | --- | --- | --- |
| [OWN-DEV-0001](../definitions/own-dev-0001-two-channel-universal-dimmer.md) | `F418U2`, `003651` | Two-channel universal dimmer | Lighting dimmer actuator |
| [OWN-DEV-0003](../definitions/own-dev-0003-flush-mounted-actuator-free-control.md) | `64391`, `64191`, `64192` and variants | Flush-mounted two-relay actuator and free control | Two local relays with configurable commands for remote loads or scenarios |
| [OWN-DEV-0006](../definitions/own-dev-0006-two-module-zero-crossing-actuator-control.md) | `64195`, `64196`, `64393` and variants | Two-module zero-crossing actuator and control | Two zero-crossing relays; local and remote command roles depend on configuration |
| [OWN-DEV-0008](../definitions/own-dev-0008-flush-mounted-one-relay-actuator.md) | `64390`, `H4671/1`, `L4671/1` and variants | Flush-mounted one-relay actuator | Single Light actuator Module |
| [OWN-DEV-0021](../definitions/own-dev-0021-one-relay-din-actuator-16-a.md) | `F411/1N`, `003841` | DIN-rail one-relay lighting actuator with local load control | One lighting relay; load-specific ratings and Slave OFF delay |
| [OWN-DEV-0022](../definitions/own-dev-0022-two-relay-din-actuator-10-a.md) | `F411/2`, `003842` | Two-independent-relay DIN actuator for lighting, automation and paired motor loads | Two lighting relays or an interlocked motor pair |
| [OWN-DEV-0023](../definitions/own-dev-0023-four-relay-din-actuator.md) | `F411/4`, `003844` | Four-independent-relay 2-DIN actuator for lighting and paired automation/motor loads | Four lighting relays, interlocked motor pairs or sequenced rabbet shutters |
| [OWN-DEV-0025](../definitions/own-dev-0025-din-dimmer-1000-w.md) | `F414`, `003652` | One-channel DIN SCS dimmer for resistive and ferromagnetic-transformer loads | Resistive/ferromagnetic dimming; F414 mains/fuse scope |
| [OWN-DEV-0027](../definitions/own-dev-0027-flush-mounted-dimmer.md) | `H4674`, `L/N/NT4674` | Flush-mounted SCS dimmer actuator | SCS controller for up to three `4416` slave dimmers; load switching is provided by the slaves |
| [OWN-DEV-0030](../definitions/own-dev-0030-ballast-din-dimmer-1-10-v.md) | `F413` | DIN-rail 1-10 V ballast dimmer | Historical 1-10 V four-ballast dimmer |
| [OWN-DEV-0045](../definitions/own-dev-0045-shutter-actuator-bus.md) | `H4661M2`, `LN4661M2`, `AM5861M2` and variants | Advanced shutter actuator | One interlocked motor load; calibration and preset behavior depend on motor/control type |
| [OWN-DEV-0052](../definitions/own-dev-0052-ballast-din-dimmer-0-10-v.md) | `BMDI1001`, `002611` | Ballast DIN dimmer 0-10 V | One switched channel with analog ballast dimming; physical and virtual ranges distinguished |
| [OWN-DEV-0059](../definitions/own-dev-0059-basic-actuator.md) | `3475` | Basic actuator | One compact relay; same-address slave and delayed slave OFF |
| [OWN-DEV-0060](../definitions/own-dev-0060-basic-control-actuator.md) | `3476` | Basic control actuator | One compact relay and normally open pushbutton input; cyclic, separate and timed control |
| [OWN-DEV-0064](../definitions/own-dev-0064-room-controller-2-output-16-a.md) | `BMSW3002`, `048841` | Room Controller - 2 outputs 16 A | Two lighting outputs, powered local bus and combined 16 A maximum |
| [OWN-DEV-0065](../definitions/own-dev-0065-memory-module.md) | `F425`, `003552` | Lighting-state memory module | Learns and restores lighting states after a power interruption; excludes shutters |
| [OWN-DEV-0067](../definitions/own-dev-0067-four-relay-din-actuator-16-a.md) | `BMSW1003`, `002602` | 4-relay DIN actuator 16 A | Four independent relays; load classes and software/filter limits |
| [OWN-DEV-0068](../definitions/own-dev-0068-one-module-one-relay-actuator.md) | `L/N/NT4675` | 1-module 1-relay actuator | One compact relay; exact historical load classes and slave modes |
| [OWN-DEV-0069](../definitions/own-dev-0069-scs-dali-gateway.md) | `F429`, `002631` | SCS/DALI gateway | Eight independent DALI outputs; DALI2 and source-filter limits |
| [OWN-DEV-0073](../definitions/own-dev-0073-din-dimmer-1000-va.md) | `F416U1`, `002621` | DIN dimmer 1000 VA | One phase-cut dimming output; exact load classes and slave configuration |
| [OWN-DEV-0074](../definitions/own-dev-0074-din-dimmer-2x400-va.md) | `F417U2`, `002622` | DIN dimmer 2 x 400 VA | Two phase-cut dimming outputs; dual-output ratings and slave configuration |
| [OWN-DEV-0075](../definitions/own-dev-0075-room-controller-4-output-0-10-v.md) | `BMDI3002`, `048843` | Room Controller - 4 dimming outputs 0-10 V | Four analogue ballast channels and powered local bus; regional rating differences |
| [OWN-DEV-0076](../definitions/own-dev-0076-room-controller-2-universal-dimming-outputs.md) | `BMDI3301`, `048845` | Room Controller - 2 universal dimming outputs | Two independently regulated 1000 W outputs; exact regional sheet and load forcing |
| [OWN-DEV-0077](../definitions/own-dev-0077-multi-application-room-controller.md) | `BMSW3003`, `048847` | Multi-application Room Controller | One motor, one switched and two analogue channels; wiring/load conflicts explicit |
| [OWN-DEV-0079](../definitions/own-dev-0079-room-controller-2-output-0-10-v.md) | `BMDI3001`, `048842` | Room Controller - 2 dimming outputs 0-10 V | Two analogue ballast channels; shared local-bus budget and regional supply differences |
| [OWN-DEV-0081](../definitions/own-dev-0081-1-relay-din-actuator-16-a-100-240-v.md) | `BMSW1001`, `002600` | 1 relay DIN actuator 16 A 100/240 V | One switched lighting load; source-scoped state-recall and software timer settings |
| [OWN-DEV-0082](../definitions/own-dev-0082-room-controller-1-output-16-amps.md) | `BMSW3001`, `048840` | Room Controller 1 Output 16 Amps | One lighting load and local sensor bus; relay/controller Modules separated |
| [OWN-DEV-0083](../definitions/own-dev-0083-2-relay-din-actuator-16-a-100-240-v.md) | `BMSW1002`, `002601` | 2 relay DIN actuator 16 A 100/240 V | Two switched lighting loads; independent naming and state-recall settings |
| [OWN-DEV-0091](../definitions/own-dev-0091-stop-go.md) | `F80/SG` | Stop&Go | Fault-checked legacy reclosure; separate SCS accessory scope |
| [OWN-DEV-0092](../definitions/own-dev-0092-stop-go-btest.md) | `F80/SGB` | Stop&Go Btest | Legacy reclosure plus 56-day Btest; six-hour activation timing |
| [OWN-DEV-0093](../definitions/own-dev-0093-stop-go-plus.md) | `F80/SGP` | Stop&Go Plus | Fault monitoring; 30-minute recovery and 24-hour automatic-restoration limit |
| [OWN-DEV-0098](../definitions/own-dev-0098-shutter-flush-mounted-actuator.md) | `H4671/2`, `L4671/2`, `AM5851/2` | Shutter flush mounted actuator | Interlocked shutter motor control; physical timing and catalogue Module-slot discrepancy |
| [OWN-DEV-0099](../definitions/own-dev-0099-flush-mounted-leading-dimmer-300-va.md) | `L4678`, `H4678` | Flush mounted leading dimmer 300 VA | Leading-edge dimming; source-restricted incandescent/transformer load ratings |
| [OWN-DEV-0101](../definitions/own-dev-0101-eight-output-din-actuator-16-a.md) | `BMSW1005`, `002604` | Eight-output DIN `ON`/`OFF` actuator 16 A | Eight separately controlled relay outputs; historical learning and reset-state scopes |
| [OWN-DEV-0112](../definitions/own-dev-0112-myhome-lighting-command-actuator.md) | `H4672M2L`, `LN4672M2L`, `067586` | MYHOME lighting command and actuator | Two lighting actuator placements plus commands; physical ratings undocumented |
| [OWN-DEV-0113](../definitions/own-dev-0113-myhome-shutter-command-actuator.md) | `H4672M2S`, `LN4672M2S`, `067587` | MYHOME shutter command and actuator | Shutter actuator plus commands; filtered motor type and calibration fields |
| [OWN-DEV-0118](../definitions/own-dev-0118-light-now-lighting-actuator-control.md) | `Y4672M2L`, `MX5230`, `AA5230` | Light Now lighting actuator and control | Two lighting relays plus remote commands; source-specific LED and load limits |
| [OWN-DEV-0122](../definitions/own-dev-0122-load-actuator-current-sensor.md) | `F522`, `003558` | Load actuator with current sensor | One measured relay, local totalizers and optional residual-current sensor |
| [OWN-DEV-0123](../definitions/own-dev-0123-load-management-automation-actuator.md) | `F523`, `003559` | Load management and automation actuator | One unmetered relay combining load shedding and automation |
| [OWN-DEV-0124](../definitions/own-dev-0124-flush-mounted-load-management-actuator.md) | `HC/HS/HD4672N`, `L/N/NT4672N` | Flush-mounted load management actuator | Two-module flush relay with separate shedding indicator |
| [OWN-DEV-0126](../definitions/own-dev-0126-eight-output-scs-dali-interface.md) | `002633`, `BMDI1100` | Eight-output SCS and DALI interface | Eight DALI channels and scoped all/channel addressing conversions |
| [OWN-DEV-0128](../definitions/own-dev-0128-four-channel-dali-room-controller.md) | `BMDI3101`, `048844` | Four-channel DALI room controller | Four DALI channels, supervised room control and four SCS branches |
| [OWN-DEV-0130](../definitions/own-dev-0130-four-channel-1-10v-dimming-interface.md) | `BMDI1002`, `002612` | Four-channel 1-10 V dimming interface | Four switched 1-10 V channels and mode/delay conversion boundaries |
| [OWN-DEV-0133](../definitions/own-dev-0133-four-output-fil-pilote-actuator.md) | `003577`, `F430FP` | Four-output Fil Pilote actuator | Four independent pilot-wire heating outputs and local OFF/Comfort behavior |
| [OWN-DEV-0139](../definitions/own-dev-0139-led-cfl-dimmer.md) | `F418`, `003665` | LED and CFL dimmer | Phase-control dimming, physical TY/MIN selectors and load-table discrepancies |
| [OWN-DEV-0140](../definitions/own-dev-0140-normally-closed-relay-actuator.md) | `F411/1NC`, `003845` | Normally closed relay actuator | One NC changeover relay, physical slave/pushbutton modes and load-specific contact ratings |
| [OWN-DEV-0141](../definitions/own-dev-0141-two-channel-normally-closed-relay-actuator.md) | `003843`, `F411/2NC` | Two-channel normally closed relay actuator | Two NC relay loads, physical master/slave settings and source-scoped ratings |
| [OWN-DEV-0142](../definitions/own-dev-0142-1-10v-ballast-dimmer.md) | `003656`, `F413N` | 1-10 V ballast dimmer | Analogue ballast control with load/filter and ten/fifteen ballast discrepancies |
| [OWN-DEV-0143](../definitions/own-dev-0143-400va-electronic-transformer-dimmer.md) | `003653`, `F415` | 400 VA electronic-transformer dimmer | Electronic-transformer dimming with explicit historical fuse revision conflict |
| [OWN-DEV-0144](../definitions/own-dev-0144-eight-output-temperature-control-actuator.md) | `003517`, `F430R8` | Eight-output temperature-control actuator | Eight relay outputs with application-specific output grouping |
| [OWN-DEV-0145](../definitions/own-dev-0145-two-output-0-10v-valve-actuator.md) | `003518`, `F430V10` | Two-output 0-10 V valve actuator | Two proportional valve outputs and normal/OFF software paths |
| [OWN-DEV-0146](../definitions/own-dev-0146-relay-0-10v-fan-coil-actuator.md) | `003519`, `F430R3V10` | Relay and 0-10 V fan-coil actuator | Relay/proportional fan-coil control with production and Firmware boundaries |
| [OWN-DEV-0147](../definitions/own-dev-0147-two-relay-temperature-control-actuator.md) | `003579`, `F430/2` | Two-relay temperature-control actuator | Two relay loads, interlock and zone-00 pump configuration |
| [OWN-DEV-0148](../definitions/own-dev-0148-four-relay-temperature-control-actuator.md) | `003580`, `F430/4` | Four-relay temperature-control actuator | Four common-contact relay outputs with physical/software role discrepancies |
| [OWN-DEV-0153](../definitions/own-dev-0153-two-channel-10a-universal-actuator.md) | `003848`, `F411U2` | Two-channel 10 A universal actuator | Two lighting relays or interlocked shutter motor; load/formula and Virgin Object field evidence reconciled |
| [OWN-DEV-0154](../definitions/own-dev-0154-single-channel-10a-lighting-actuator.md) | `003847`, `F411U1` | Single-channel 10 A lighting actuator | Single lighting relay with source-specific resistive/lamp ratings and physical/software modes |
| [OWN-DEV-0161](../definitions/own-dev-0161-light-now-shutter-actuator-control.md) | `MX5220`, `Y4672M2S` | Light NOW shutter actuator and control | Local/remote shutter control with distinct Light NOW and Céliane indication and calibration limits |
| [OWN-DEV-0174](../definitions/own-dev-0174-six-channel-dimmer.md) | `002627` | Six-channel dimmer | Six catalogue dimmer channels with source-specific address/filter/default limits; electrical original missing |
| [OWN-DEV-0180](../definitions/own-dev-0180-f401-shutter-motor-actuator.md) | `F401` | F401 shutter motor actuator | One-motor shutter control with calibration/preset dependencies and revision/filter discrepancies |
| [OWN-DEV-0181](../definitions/own-dev-0181-f414-127-resistive-inductive-dimmer.md) | `F414/127` | F414/127 resistive and inductive dimmer | Resistive / ferromagnetic dimming with explicitly differing English and Mexican ratings |
| [OWN-DEV-0182](../definitions/own-dev-0182-f411-1-single-relay-din-actuator.md) | `F411/1` | F411/1 single-relay DIN actuator | Single relay including historical 150 W fluorescent rating; physical and conversion mode limits |
| [OWN-DEV-0183](../definitions/own-dev-0183-f411-1fl-fluorescent-relay-actuator.md) | `F411/1FL` | F411/1FL fluorescent-lamp relay actuator | Conventional fluorescent switching; source-scoped 150..500 W and 3 m cable requirement |
| [OWN-DEV-0184](../definitions/own-dev-0184-f415-127-electronic-transformer-dimmer.md) | `F415/127` | F415/127 electronic-transformer dimmer | Electronic-transformer dimming; regional load, mains and current discrepancies retained |
| [OWN-DEV-0202](../definitions/own-dev-0202-living-now-k4672m2l-light-actuator-control.md) | `K4672M2L` | Living Now K4672M2L light actuator and control | Two lighting relays and remote controls; neutral-dependent load matrix, Firmware restrictions and source conflicts |
| [OWN-DEV-0203](../definitions/own-dev-0203-living-now-k4672m2s-shutter-actuator-control.md) | `K4672M2S` | Living Now K4672M2S shutter actuator and control | Shutter actuator/control; local and remote role separation, calibration, pulse PRESET and production boundaries |
| [OWN-DEV-0205](../definitions/own-dev-0205-living-now-k8002l-light-actuator.md) | `K8002L` | Living Now K8002L light actuator | Two-channel light actuator; neutral-dependent loads, digital controls and unresolved 16 A versus 4 A classifications |
| [OWN-DEV-0206](../definitions/own-dev-0206-living-now-k8002s-shutter-actuator.md) | `K8002S` | Living Now K8002S shutter actuator | Interlocked shutter actuator; exact calibration procedure, pulse-motor filter conflict and source-scoped ratings |

## Evidence and applicability

Each Device link leads to its canonical definition, including retained manufacturer sources, catalogue relationships, Firmware applicability and evidence limits. Commercial references are selected navigation labels; combined finish codes and variant lists are expanded there.

Category membership summarizes documented or catalogue-derived roles. It does not establish the installed Configuration, simultaneous availability of alternative Objects, universal OpenWebNet command support or current availability of historical services. Missing product-specific documentation is an evidence gap, not an unresolved commercial identity.

## Related material

- [Device Categories](README.md)
- [Device Index](../index.md)
- [Functional Protocol](../../functional/)
