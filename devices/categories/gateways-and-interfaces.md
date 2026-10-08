# Gateways and Interfaces

Network gateways and other interfaces used by the documented systems. OpenWebNet (OWN) access is separated from contact inputs, radio bridges, lighting interfaces and video-entry links; an Ethernet connector or a product name containing “gateway” does not by itself establish an OpenWebNet gateway.

Table abbreviations: IR = infrared; DALI = Digital Addressable Lighting Interface; HVAC = heating, ventilation and air conditioning; PSTN = public switched telephone network; GPRS = General Packet Radio Service.

## OpenWebNet gateways

The table includes published or observed gateway models and catalogue-defined Open SCS gateways. Its evidence column distinguishes these bases; catalogue membership alone does not verify a live endpoint or a complete command set. The published model table names individual references, so it is not applied automatically to every commercial variant.

| Device ID | Commercial references | Description | OpenWebNet role and evidence |
| --- | --- | --- | --- |
| [OWN-DEV-0002](../definitions/own-dev-0002-audio-video-web-server-gateway.md) | `F454`, `003598` | Audio/video web server and OpenWebNet gateway | Manufacturer documentation and observed gateway identity; catalogue Open SCS gateway Object `150` |
| [OWN-DEV-0033](../definitions/own-dev-0033-light-manager-control-unit.md) | `BMNE500` | Light Manager control unit | Manufacturer OPEN authentication/network configuration and catalogue Open SCS gateway Object `150` |
| [OWN-DEV-0080](../definitions/own-dev-0080-scenario-programmer.md) | `MH200` | Scenario programmer | MH200 is listed in the published gateway model table; manufacturer software documents OPEN authentication; [published gateway models](../../functional/who-13-integration-gateway/dimensions.md#dimension-15---device-type) |
| [OWN-DEV-0089](../definitions/own-dev-0089-webserver-audio-video-din.md) | `F453AV` | Webserver Audio/Video DIN | Manufacturer OPEN connection settings and catalogue Open SCS gateway Object `150` |
| [OWN-DEV-0090](../definitions/own-dev-0090-enhanced-webserver.md) | `F453` | Enhanced Webserver | Catalogue Open SCS gateway Object `150`; exact hardware/programming documentation remains incomplete |
| [OWN-DEV-0131](../definitions/own-dev-0131-mh200n-scenario-programmer.md) | `MH200N`, `003565` | MH200N scenario programmer | Manufacturer OPEN access configuration and catalogue Open SCS gateway Object `150` |
| [OWN-DEV-0135](../definitions/own-dev-0135-colour-touch-screen.md) | `H4684` (gateway evidence); `L4684` (same catalogue item) | Colour Touch Screen | Published gateway model table explicitly names `H4684`; this does not establish the same gateway behavior for `L4684`; [published gateway models](../../functional/who-13-integration-gateway/dimensions.md#dimension-15---device-type) |
| [OWN-DEV-0138](../definitions/own-dev-0138-open-bacnet-gateway.md) | `F450`, `003597` | OPEN and BACnet gateway | Manufacturer OPEN/BACnet bridge and catalogue Object `220`; a specialized HVAC bridge, not a universal SCS gateway |
| [OWN-DEV-0151](../definitions/own-dev-0151-mh202-scenario-programmer.md) | `003535`, `MH202` | MH202 scenario programmer | Observed MH202 gateway-information and identity responses; manufacturer OPEN authentication configuration; [observed MH202 case](../../guides/identify-openwebnet-gateway.md#7-worked-case-mh202) |
| [OWN-DEV-0152](../definitions/own-dev-0152-f455-basic-gateway.md) | `003594`, `F455` | F455 basic gateway | Manufacturer OPEN connection/authentication settings and catalogue Open SCS gateway Object `150`; application limits remain specific to F455 |
| [OWN-DEV-0185](../definitions/own-dev-0185-legrand-area-manager.md) | `002645` | Legrand Area Manager | Catalogue Open SCS gateway Object `150`; manufacturer lighting-management/network role; runtime scope uncorroborated |
| [OWN-DEV-0190](../definitions/own-dev-0190-mh201-hotel-room-scenario-manager.md) | `MH201` | MH201 hotel room scenario manager | Manufacturer room configuration gateway and catalogue Open SCS/XOpen SCS roles; hotel and trusted-IP restrictions apply |
| [OWN-DEV-0195](../definitions/own-dev-0195-arteor-573992-audio-video-web-server.md) | `573992` | Arteor 573992 audio and video web server | Catalogue Open SCS gateway Object `150` and Firmware-scoped manufacturer protocol support; exact hardware/manual gap remains |
| [OWN-DEV-0199](../definitions/own-dev-0199-myhomeserver1-home-automation-server.md) | `MyHomeServer1` | MyHOMEServer1 home automation server | Catalogue Open SCS gateway Object `150`; manufacturer commissioning/server role; installed endpoint and app/Firmware pairing uncorroborated |
| [OWN-DEV-0207](../definitions/own-dev-0207-f460-myhome-server.md) | `F460` | F460 MyHOME server | Catalogue Open SCS gateway candidate Object `150`; manufacturer server role; installed placement and runtime endpoint uncorroborated |
| [OWN-DEV-0208](../definitions/own-dev-0208-f461-myhome-server-third-party-integration.md) | `F461` | F461 MyHOME server for third-party integration | Catalogue Open SCS gateway Object `150`; manufacturer local third-party integration role; exact runtime protocol/endpoint uncorroborated |

## Other interfaces and integration devices

These devices connect system components, provide input or display functions, or perform specialized integration. Placement here means that the reviewed evidence does not establish a general OpenWebNet network gateway; it is not a claim that the device never uses OpenWebNet internally or for configuration.

| Device ID | Commercial references | Description | Relevant functions |
| --- | --- | --- | --- |
| [OWN-DEV-0029](../definitions/own-dev-0029-radio-receiver-interface.md) | `HC/HS/HD4575`, `L/N/NT4575`, `L/N/NT4575N` | Flush-mounted 868 MHz radio-to-SCS receiving interface | Radio-to-SCS bridge, sound functions, self-learning and remote F420 scenes |
| [OWN-DEV-0032](../definitions/own-dev-0032-transmitting-radio-interface.md) | `HC/HS4576`, `L/N/NT4576`, `HD4576` | SCS-to-radio transmitting interface | Configured SCS commands to compatible 868 MHz radio devices |
| [OWN-DEV-0034](../definitions/own-dev-0034-radio-interface-temperature-probes.md) | `L/N/NT4577`, `HC/HS/HD4577` | Radio interface for temperature probes | Two configured radio-probe channels; temperature and lighting-sensor modes remain distinct |
| [OWN-DEV-0035](../definitions/own-dev-0035-flush-mounted-radio-receiver-batteryless-control.md) | `HC/HS/HD4575SB`, `L/N/NT4575SB` | Receiver for batteryless radio controls | Paired wireless controls send configured lighting, shutter or scenario commands to SCS |
| [OWN-DEV-0069](../definitions/own-dev-0069-scs-dali-gateway.md) | `F429`, `002631` | SCS/DALI gateway | Eight-output SCS/DALI lighting bridge; no general OpenWebNet network gateway established |
| [OWN-DEV-0070](../definitions/own-dev-0070-din-contacts-interface.md) | `F428`, `003553` | DIN contacts interface | Two contact inputs; revision-dependent lighting, automation and scenario roles |
| [OWN-DEV-0071](../definitions/own-dev-0071-module-contacts-interface.md) | `L/N/NT4688` | Module contacts interface | Two traditional contact inputs; catalogue and physical command scopes distinguished |
| [OWN-DEV-0072](../definitions/own-dev-0072-basic-contacts-interface.md) | `3477`, `573996`, `049238` | Basic contacts interface | Two dry-contact inputs for lighting, shutters, scenes and audio; source conflicts explicit |
| [OWN-DEV-0078](../definitions/own-dev-0078-scs-scs-interface.md) | `F422`, `003562` | SCS/SCS interface | SCS bus expansion/separation and system links; distinct from a TCP gateway |
| [OWN-DEV-0085](../definitions/own-dev-0085-burglar-alarm-central-unit-with-communicator.md) | `3485` | Burglar alarm central unit with communicator | PSTN alarm integration; 3485/3485STD scope and battery compatibility |
| [OWN-DEV-0087](../definitions/own-dev-0087-gsm-burglar-alarm-central-unit.md) | `3486` | GSM burglar alarm central unit | Eight sensor zones; GSM/PSTN communication, scenarios and automations |
| [OWN-DEV-0095](../definitions/own-dev-0095-burglar-alarm-central-unit-with-communicator.md) | `067510`, `775795` | Burglar alarm central unit with communicator | PSTN alarm panel; exact USB accessory caption and missing panel manuals |
| [OWN-DEV-0096](../definitions/own-dev-0096-pulses-counter-interface.md) | `3522`, `003554` | Pulses counter interface | SCS pulse accounting; clock-dependent history and physical multiplier matrix |
| [OWN-DEV-0100](../definitions/own-dev-0100-stereo-control.md) | `L4561N`, `003586` | Stereo control | External RCA stereo source with learnt IR events; USB/COM programming |
| [OWN-DEV-0102](../definitions/own-dev-0102-multimedia-touch-screen.md) | `HC4690`, `HD4690`, `HS4690` | Multimedia Touch Screen | Multimedia home-control/video interface; OPEN-password project settings do not establish a gateway endpoint |
| [OWN-DEV-0107](../definitions/own-dev-0107-legrand-multimedia-touch-screen.md) | `067285`, `573963`, `573962` | Legrand Multimedia Touch Screen | Multimedia user interface with PC project transfer; direct TCP gateway endpoint unestablished |
| [OWN-DEV-0125](../definitions/own-dev-0125-scs-zigbee-gateway.md) | `048832`, `BMNE4000` | SCS and ZigBee gateway | SCS/ZigBee radio bridge; commissioning and profile limits apply |
| [OWN-DEV-0126](../definitions/own-dev-0126-eight-output-scs-dali-interface.md) | `002633`, `BMDI1100` | Eight-output SCS and DALI interface | Eight DALI channels and scoped all/channel addressing conversions |
| [OWN-DEV-0128](../definitions/own-dev-0128-four-channel-dali-room-controller.md) | `BMDI3101`, `048844` | Four-channel DALI room controller | Four DALI channels, supervised room control and four SCS branches |
| [OWN-DEV-0130](../definitions/own-dev-0130-four-channel-1-10v-dimming-interface.md) | `BMDI1002`, `002612` | Four-channel 1-10 V dimming interface | Four switched 1-10 V channels and mode/delay conversion boundaries |
| [OWN-DEV-0132](../definitions/own-dev-0132-burglar-alarm-pstn-communicator.md) | `573934`, `067520` | Burglar alarm unit with PSTN communicator | PSTN alarm communication, local commissioning and voice-message programming |
| [OWN-DEV-0134](../definitions/own-dev-0134-energy-data-logger.md) | `F524`, `003566` | Energy data logger | Energy history, virtual lines and web load supervision; exact OPEN diagnostics uncorroborated |
| [OWN-DEV-0136](../definitions/own-dev-0136-infrared-air-conditioning-emitter.md) | `3456`, `088301` | Infrared air-conditioning emitter | Basic/advanced IR learning and split command-set transfer |
| [OWN-DEV-0149](../definitions/own-dev-0149-hotel-ip-server.md) | `003599`, `F458` | Hotel IP server | Hotel DHCP/DNS infrastructure server; no general OpenWebNet gateway role established |
| [OWN-DEV-0150](../definitions/own-dev-0150-pulse-counter-interface.md) | `003576`, `3522N` | Pulse counter interface | Meter pulse conversion, flow calculation and stored consumption history; physical/software scale limits |
| [OWN-DEV-0159](../definitions/own-dev-0159-classe-300eos-connected-video-internal-unit.md) | `344842`, `344845` | Classe 300EOS connected video internal unit | Video-entry/MyHOME user interface; newer MyHOME roles are product/Firmware-specific, not a proven general gateway endpoint |
| [OWN-DEV-0162](../definitions/own-dev-0162-two-wire-ip-interface.md) | `346890` | Two-wire to IP interface | Two-wire/IP system interface with source-specific topology capacities and address endpoints |
| [OWN-DEV-0163](../definitions/own-dev-0163-d45-ip-interface.md) | `323011` | D45 to IP interface | D45/IP interface with distinct bus/LAN connectors and conditional supply/configuration limits |
| [OWN-DEV-0186](../definitions/own-dev-0186-vigik-single-door-access-control-unit.md) | `348040` | Vigik single-door access-control unit | One Vigik reader and managed entrances; badge/reset effects, capacities and Firmware limits |
| [OWN-DEV-0188](../definitions/own-dev-0188-vigik-gprs-interface.md) | `348330` | Vigik GPRS interface | Vigik GPRS/ACWEB remote management with periodic/forced synchronization; catalogue XOpen SCS role does not establish a generic local TCP gateway or Ethernet port |
| [OWN-DEV-0189](../definitions/own-dev-0189-346891-two-wire-ip-interface.md) | `346891` | 346891 two-wire to IP interface | Two-wire/IP video-entry integration; source-specific addressing, capacities and advanced functions |
| [OWN-DEV-0194](../definitions/own-dev-0194-pabx-288-telephone-switching-system.md) | `345829` | PABX 288 telephone switching system | PABX 288 telephone/video integration; expansions, PC transfers, modem and source-specific wiring limits |
| [OWN-DEV-0198](../definitions/own-dev-0198-f459-driver-manager.md) | `F459` | F459 Driver Manager | Driver-based MyHOME/third-party integration with OWN access settings; a generic OpenWebNet gateway interface is not established here |
| [OWN-DEV-0209](../definitions/own-dev-0209-f459t-hvac-driver-manager.md) | `F459T` | F459T HVAC Driver Manager | Catalogue-identified HVAC Driver Manager; exact integrations and operating interfaces remain documentation gaps |

## Evidence and applicability

See [Category evidence and applicability](README.md#evidence-and-applicability) for reference selection, source scope and installed-state limits.

## Related material

- [Device Categories](README.md)
- [Device Index](../index.md)
- [Functional Protocol](../../functional/)
