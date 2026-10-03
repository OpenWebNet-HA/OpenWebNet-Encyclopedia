# Living Now thermostat with display

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0109` | Project identity |
| Technical description | Living Now thermostat with display | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `KM4691`, `KG4691`, `KW4691` | All three catalogue commercial records; confidence scoped below |
| Catalogue item | `2242` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Thermoregulation | Main system association |
| Item model / `modobj` | `9` | Main association; independent of project ID |
| Firmware definition | `771` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Thermoregulation, User interfaces | Source-derived roles |

One protocol Module exposes reusable Hotel thermostat Object `95`. The published product also supports residential operation. This SCS thermostat manages external actuators; catalogue reusable capability, firmware-specific filters and the published system/actuator requirements must be reconciled separately.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Living Now | `KM4691` | Established commercial variant | Catalogue record `2586`; published family/variant scope reconciled below |
| BTicino - Living Now | `KG4691` | Established commercial variant | Catalogue record `2587`; published family/variant scope reconciled below |
| BTicino - Living Now | `KW4691` | Established commercial variant | Catalogue record `2588`; published family/variant scope reconciled below |

KW/KG/`KM4691` are named together in the exact manuals and 2018/2020 sheets. The current 2026 sheet adds KB/KC/KS4691, but none is attached to item `2242` in the canonical snapshot, so they are not silently added to this Device’s commercial cluster. `KW4691`’s manufacturer export independently identifies Living Now. Catalogue labels/colour suffixes do not establish an electrical or firmware difference.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000215-EN.pdf` | Russian technical sheet with EN filename | `ST-00000215-EN; 31/07/2018` | KW/KG/`KM4691`; physical legend p. 1, configuration and interaction matrix p. 2. Printed/PDF pages coincide. Ratings on p. 1 verified visually because text extraction omits them. | [Archived original](https://archive.openwebnet-ha.org/sha256/30/71/3071dce26961993f25efb65c8ee2ecf64f994920469c4bb1d8fe3a28e14a25ea.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000215-EN.pdf) |
| `ST-00000849-EN.pdf` | English technical sheet | `ST-00000849-EN; 05/11/2020` | KW/KG/`KM4691`; specifications, humidity/actuator support p. 1; configuration and interaction matrix p. 2. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/b8/7c/b87c86f14520aff3189a2f2bb72e4cc5d8d7da9862dd0574aa58a9912ac11f07.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000849-EN.pdf) |
| `ST-00002496-EN.pdf` | Current English technical sheet | `ST-00002496-EN; 15/05/2026` | KW/KG/KM and added KB/KC/KS4691; ratings, humidity, mounting exclusions p. 1; Home + Project / MyHOME Suite and function matrix p. 2. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/cb/23/cb23ea63cb843bb02be84904181083c22d8e1086a1c94e47d2ae4ef7dbd03413.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002496-EN.pdf) |
| `LE10329AC.pdf` | Multilingual mounting/wiring instructions | `LE10329AC; 12/22-01 PC` | KW/KG/`KM4691`; paired base/front and mounting PDF p. 1 (unprinted); anti-removal, SCS and local contact pp. 2-3; installation precautions pp. 4-6. Subsequent printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/e2/86/e286252d0501a5945979513a770ab6b4ecf6137da26b9aa7ed377b4fad46155e.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE10329AC.pdf) |
| `RA00165AA_I_EN.pdf` | Thermostat installation manual | `RA00165AA; revision from publisher filename; no publication date located` | KW/KG/`KM4691`; physical/defaults pp. 5-10; control/changeover pp. 11-14; complete method matrix p. 16; configuration pp. 17-62; operation pp. 63-82; errors pp. 83-85. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/86/ac/86ac22d76c82cedb132ac51bcb0288d030d68e02ffb2fc0e8b9607117b5226e6.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00165AA_I_EN.pdf) |
| `RA00165AA_U_EN.pdf` | Thermostat user manual | `RA00165AA; revision from publisher filename; no publication date located` | KW/KG/`KM4691`; roles and local controls pp. 4-15; app/hotel/HOMETOUCH pp. 16-27; messages/errors pp. 28-30. Printed/PDF pages coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/24/28/2428d40d525f7034a5a5fa93c211b576ef6f37184afe0ca93442681b71baff31.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00165AA_U_EN.pdf) |
| `KW4691-publisher-product-sheet.pdf` | Manufacturer product export | `DATASHEET; 03.10.2026` | `KW4691` only; description, exact marketed line and source-specific technical attributes; printed/PDF pp. 1-3 coincide. | [Archived original](https://archive.openwebnet-ha.org/sha256/be/80/be8098ab422a7ed9b2cf4ff35c4b5979792350d1f6e666fa80c00da7ffd4cfc5.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-KW4691&include_technical=1) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2242`: all firmware/commercial/system/Object/Module/Virgin/field/filter/mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | Two flush-mounted wiring-device modules; recommended height `150 cm`, indoor location away from heat/cold sources or outlets | RA00165AA_I_EN pp. 4, 7-9; LE10329AC PDF p. 1 |
| Supply | `18..27 Vdc` from SCS BUS | 2020/2026 sheets p. 1; installer p. 7 |
| Current by operating condition | `60 mA` maximum while keys used at maximum display; `30 mA` standby at display level `10`; `15 mA` display off | Installer p. 7; sheets publish maximum `60 mA` |
| Temperature limits | Sheets/installer operating `0..40 °C`; published set-point `3..40 °C`, `0.5 °C` increments | 2020/2026 sheets p. 1; installer pp. 5, 7 |
| `KW4691` export temperature attributes | Measuring `0..40 °C`; operating/setting `-5..35 °C`; storage `-10..70 °C` | Original KW export p. 2; distinct from technical-sheet operating limits |
| `KW4691` export dimensions/protection | `45 x 90 x 10 mm`, `IP20`, `IK04` | KW export p. 2; no assumption about which assembly/depth was measured |
| `KW4691` export wiring attributes | Flexible/rigid wire; connection cable length `500 m`; rated current `0.06 A` | KW export p. 2; cable type/topology not specified by that length attribute |
| Local control/display | Four capacitive keys: fan, `ON`/`OFF`/protection, temperature down/up; LED display, ambient-light sensor | Sheets p. 1; installer p. 6 |
| Rear interfaces | SCS terminals and local contact input marked Remote; base/front from the same individual package must stay together | LE10329AC PDF pp. 1, 3 |
| Optional securing | Anti-removal/tamper screw; mounting/disassembly diagram | LE10329AC p. 2; installer p. 9 |
| Supported loads | On/off, open/close, 3-point and `0..10 V` valves; 2/4-tube fan-coils, including proportional speed; gateway | 2020/2026 sheet p. 1; output requires compatible external actuator |
| Specified actuators | `F430/2`, `F430/4`, `F430R8`, `F430R3V10`, `F430V10` | All three sheets p. 1 |
| Excluded control units | Not compatible with `L/N/NT/HC/HD/HS4695` and `3550`, the 4-to-99-zone controllers | 2020/2026 sheets p. 1 |
| Humidity | 2020: embedded humidity probe for third-party integration via `F459`; 2026 adds native humidity logic with F460/Classe 300EOS and Home + Project | 2020/2026 p. 1; humidity precision/range not published |
| Current compatible boxes | `502E`, `503E`, `504E`, `506L`, `PB502N`, `PB503N`, `PB504N`, `PB506N` | 2026 sheet p. 1 |
| Current incompatible accessories | `502EF`, `503EF`, `504EF`, `506EF`, `PB502NNF`, `PB503NNF`, `PB504NNF`, `PB506NNF` | 2026 sheet p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2242` | Canonical catalogue |
| Technical item description | Add-on SCS thermostat | Canonical catalogue |
| Item family | 0; key `11` | Canonical catalogue |
| Main system | Thermoregulation; key `2` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `9` | `AS_ITEM_SYSTEM` |
| Commercial record count | `3` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `771` | `1` | `0` | No build row | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `771` | `1` | `95` Hotel thermostat | Fixed/designated metadata | `2933` | `542` | `1395` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `771` | Advanced Configuration | `2` | Association key `2` |


No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

Firmware `771` associates Advanced Configuration only. The installer explicitly describes virtual configuration through a gateway with MyHOME Suite, MyHOME Up or HotelSupervision, and no physical configurator setup. The term “virtual” in the manual does not create a missing catalogue mode association. Early 2018/2020 sheets require MyHOME Up firmware `2.1` or later, app after `2.2`, and MyHOME Suite higher than `03.03.73`; these are system/software prerequisites, not this thermostat’s installed firmware. The 2026 sheet names Home + Project and retains MyHOME Suite.

The historical MyHOME Up route uses a networked MyHOMEServer1 and smartphone; MyHOME Suite uses PC Ethernet or USB through a gateway; HotelSupervision uses server/client PCs. None establishes direct thermostat Ethernet, USB or Wi-Fi hardware.

### Complete historical configuration-method matrix

| Setting | MyHOME Suite | MyHOME Up | HotelSupervision |
| --- | --- | --- | --- |
| Heating/cooling/both | Yes | Yes | Yes |
| Temperature range | Yes | Yes | Yes |
| Protection setpoints | Yes | Yes | Yes |
| Temperature format | Yes | Yes | Yes |
| Disable all keys | Yes | Yes | Yes |
| Automatic switching | Yes | Yes | No |
| Pump delay | Yes | Yes | No |
| Automatic threshold | Yes | Yes | No |
| Regulation band | Yes | Yes | No |
| Fan-coil speed thresholds | Yes | Yes | No |
| Fan-coil valve advance | Yes | Yes | No |
| Local contact number | Yes | Yes | No |
| Contact action delay | Yes | Yes | No |
| Contact opening scenario | Yes | Yes | No |
| Contact action timeout | Yes | Yes | No |
| Backlighting | Yes | Yes | No |
| Window symbol | Yes | Yes | No |
| Eco setpoint | Yes | No | Yes |
| Comfort setpoint | Yes | No | Yes |
| Continuous ventilation | Yes | No | No |
| Proportional speed percentages | Yes | No | No |
| Anti-block protection | Yes | No | No |
| Fan delay | Yes | No | No |
| PID band | Yes | No | No |
| PID inertia | Yes | No | No |
| Contact preset | Yes | No | No |
| Measured temperature visibility | Yes | No | No |
| Heating/cooling contact key lock | Yes | No | No |
| Automatic fan-speed key | Yes | No | No |
| Mode-change key | Yes | No | No |
| Contact opening/closing action | Yes | Protection or Manual only | No |

The preceding matrix reproduces every setting of RA00165AA_I_EN printed p. 16 / PDF p. 16. It describes that historical software revision, not a promise that every catalogue filter or newer Home + Project workflow accepts the same settings.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `771` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `95` - Hotel thermostat

Catalogue Object key `542` maps to external Object `95`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | Zone |
| `FUNCTION` | `0` = Heating; `1` = Cooling; `2` = Heating & cooling | `0` | Function type |
| `MAXIMUM_HEATING_SETPOINT` | `20..80` | `80` | Max; Maximum heating setpoint > Minimum heating setpoint Maximum cooling setpoint >= Maximum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). step 0.5 °C |
| `MINIMUM_HEATING_SETPOINT` | `6..79` | `6` | Min; Minimum heating setpoint < Maximum heating setpoint Minimum cooling setpoint >= Minimum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). step 0.5 °C |
| `COMFORT_HEATING_SETPOINT` | `7..80` | `42` | Comfort; Comfort heating setpoint > Eco heating setpoint Comfort heating setpoint <= Maximum heating setpoint Comfort heating setpoint >= Minimum heating setpoint. step 0.5 °C |
| `ECO_HEATING_SETPOINT` | `6..79` | `36` | Eco; Eco heating setpoint < Comfort heating setpoint Eco heating setpoint <= Maximum heating setpoint Eco heating setpoint >= Minimum heating setpoint. step 0.5 °C |
| `ANTIFREEZE_SETPOINT` | `6..80` | `14` | Antifreeze; step 0.5 °C |
| `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Heating fan delay; Checked only if "Heating actuator type" is set to one of values related to fan coil step 5 s |
| `HEATING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Automatic heating thresholds settings; For automatic, while checking configuration, set parameters 8, 9, 10 according to device specific settings. |
| `HEATING_REGULATION_BAND` | `1..10` | `1` | Heating setpoint allowance; Step 0.1°C |
| `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 2 threshold > Heating regulation band |
| `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 3 threshold > Heating Fan coil speed 2 threshold |
| `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to cooling; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact opening; If parameter "Heating contact opening" is set to 0, 3, 4, parameter "Heating contact opening timeout" must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact opening" = "Cooling contact opening". If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact opening must be different from 5...25. |
| `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to cooling; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact closing; If parameter "Heating contact closing" is set to 0, 3, 4, parameter "Heating contact closing timeout" must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact closing" = "Cooling contact closing" If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact closing must be different from 5...25. |
| `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact after opening; step 5s |
| `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact after closing; step 5 s |
| `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact after opening; 0 corresponds to infinite. If parameter "Heating contact opening timeout" is different from 0, "Heating contact closing timeout" must be set to 0." step 1 min |
| `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact after closing; 0 corresponds to infinite. If parameter "Heating contact closing timeout" is different from 0, "Heating contact opening timeout" must be set to 0. step 1 min |
| `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed | `0` | Heating contact pushbutton locking |
| `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Heating fancoil ventilation function |
| `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `MAXIMUM_COOLING_SETPOINT` | `7..80` | `80` | Max; Maximum cooling setpoint > Minimum cooling setpoint Maximum cooling setpoint >= Maximum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). step 0.5 °C |
| `MINIMUM_COOLING_SETPOINT` | `6..70` | `6` | Min; Minimum cooling setpoint < Maximum cooling setpoint Minimum cooling setpoint >= Minimum heating setpoint This control (cross control between heating and cooling parameters) has to be done only if both heating and cooling function are configured (at least one actuator or one pump for each function). step 0.5 °C |
| `COMFORT_COOLING_SETPOINT` | `6..79` | `50` | Comfort; Comfort cooling setpoint < Eco cooling setpoint Comfort cooling setpoint <= Maximum cooling setpoint Comfort cooling setpoint >= Minimum cooling setpoint. step 0.5 °C |
| `ECO_COOLING_SETPOINT` | `7..80` | `56` | Eco; Eco cooling setpoint > Comfort cooling setpoint Eco cooling setpoint <= Maximum cooling setpoint Eco cooling setpoint >= Minimum cooling setpoint. step 0.5 °C |
| `THERMAL_PROTECTION_SETPOINT` | `6..80` | `70` | Thermal protection; step 0.5 °C |
| `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Cooling fan delay; Checked only if "Cooling actuator type" is set to one of values related to fan coil step 5s |
| `COOLING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Cooling thresholds settings; For automatic, while checking configuration, set 28, 29, 30 according to device specific settings. |
| `COOLING_REGULATION_BAND` | `1..10` | `1` | Cooling setpoint allowance; step 0.1 °C |
| `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 2 threshold > Cooling regulation band |
| `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 3 threshold > Cooling Fan coil speed 2 threshold |
| `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to heating; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact opening; If parameter Cooling contact opening is set to 0,3,4, parameter Cooling contact opening timeout must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact opening" = "Cooling contact opening" |
| `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `3` = Switch to heating; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact closing; If parameter Cooling contact closing is to set to 0,3,4, parameter cooling contact closing timeout must be set to 0. If automatic changeover mode: - Only values 0, 1, 2, 4, 26, 27 are accepted - "Heating contact closing" = "Cooling contact closing" |
| `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact opening; step 5s |
| `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact closing; step 5s |
| `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter "Cooling contact opening timeout" is different from 0, "Cooling contact closing timeout" must be set to 0. step 1 min |
| `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact closing action; 0 corresponds to infinite. If parameter Cooling contact closing timeout is different from 0, Cooling contact opening timeout must be set to 0. step 1 min |
| `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled_contact_open; `2` = Enabled_contact_closed | `0` | Cooling contact pushbutton locking |
| `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Cooling fancoil continuous ventilation |
| `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `ACTUATOR_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 1 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 2 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 3 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 4 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 5 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 6 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 7 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 8 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 9 function; If this parameter is set to "Heating and cooling", it must be checked that: - "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=1_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=2_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=3_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=4_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=5_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=6_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=7_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=8_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=9_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `HEATING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Load type; The highlighted values must not be implemented into key object (they are dedicated to future use). In case of FIL PILOTE, "Automatic changeover Mode" must be set disabled. |
| `COOLING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Load type; The highlighted values must not be implemented into key object (they are dedicated to future use). |
| `PUMP_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 1 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 2 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 3 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 4 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 5 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 6 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 7 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 8 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `PUMP_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Pump 9 function; If "Heating actuator type" is set to FIL PILOTE, this parameter must be assigned to Not installed or to Cooling only. If "Heating actuator type" is set to GATEWAY, and this parameter is set to "Heating only" or to "Heating and cooling", there must be at least one actuator function set to "Heating only" or to "Heating and cooling". If "Cooling actuator type" is set to GATEWAY, and this parameter is set to "Cooling only" or to "Heating and cooling", there must be at least one actuator function set to "Cooling only" or to "Heating and cooling". |
| `HEATING_PUMP_DELAY` | `0..255` | `0` | Time delay for heating pumps; step 5s |
| `COOLING_PUMP_DELAY` | `0..255` | `0` | Time delay for cooling pumps; step 5s |
| `NUMBER_OF_SLAVES` | `0..9` | `0` | Number of slave probes |
| `LED_ENABLE` | `0` = Enabled; `1` = Disabled | `0` | Led enable |
| `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit | `0` | Temperature format |
| `FUNCTION_CHANGE_BY_LOCAL_BUTTON` | `0` = Enabled; `1` = Disabled | `1` | Pushbutton "heating/cooling" change |
| `AUTOMATIC_CHANGEOVER_MODE` | `0` = Enabled; `1` = Disabled | `1` | Automatic changeover mode; Condition to check contact: - See notes contained into parameters "Heating contact opening", "Heating contact closing", "Cooling contact opening" and "Cooling contact closing". Condition to check fil pilote: - See note contained into parameter "Heating actuator type". Conditions to check for actuators and pumps: - There must be at least one actuator for heatng (actuator function set to "Heating only" or "Heating and Cooling") or at least one pump for heating (pump function set to "Heating only"). - There must be at least one actuator for cooling (actuator function set to "Cooling only" or "Heating and Cooling") or at least one pump for cooling (pump function set to "Cooling only"). - if at least one actuator function is set to "Heating and cooling", "Heating actuator type" (that must be equal to "Cooling actuator type") can only be equal to 7 or 8; if this condition related to "Heating actuator type" is not satisfied, there must be at least one pump function set to "Heating only" and one pump function set to "Cooling only". |
| `AUTOMATIC_CHANGEOVER_MODE_SWITCHING_THRESHOLD` | `20..50` | `20` | Automatic changeover mode switching threshold (step 0.1 °C); Hidden, used only during device developement. |
| `BACKLIGHT_STAND_BY_LEVEL` | `0` = `OFF`; `1` = `ON` | `1` | Backlight for display standby |
| `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED | `0` | Room temperature visualization |
| `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10; `11` = Automatic with off; `12` = Automatic without off | `10` | Backlight stand-by level |
| `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled | `0` | Disable all pushbuttons |
| `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled | `0` | Pushbutton modality change |
| `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled | `1` | Calibration procedure |
| `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled | `1` | User settings procedure |
| `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open | `0` | Windows contact icon |
| `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled | `0` | Windows contact number |
| `EXTERNAL_SENSOR_TYPE` | `0` = BTicino BT-3457; `1` = Vantage 8051 | `0` | External temperature sensor type |
| `HEATING_PID_REGULATION_BAND` | `6..30` | `16` | Heating PID regulation band (°) |
| `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia | `1` | Heating PID inertia |
| `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` | `100` | Heating proportional gain (low) |
| `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` | `0` | Heating proportional gain (high) |
| `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` | `5` | Heating integrative gain low |
| `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` | `0` | Heating integrative gain high |
| `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` | `100` | Heating derivative gain low |
| `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` | `0` | Heating derivative gain high |
| `HEATING_PROPORTIONAL_SPEED_1` | `1..98` | `33` | Heating proportional speed 1 (%) |
| `HEATING_PROPORTIONAL_SPEED_2` | `2..99` | `67` | Heating proportional speed 2 (%) |
| `HEATING_PROPORTIONAL_SPEED_3` | `3..100` | `100` | Heating proportional speed 3 (%) |
| `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled | `0` | Heating pushbutton fan coil automatic speed |
| `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled | `1` | Heating anti-seizing up protection |
| `COOLING_PID_REGULATION_BAND` | `6..30` | `16` | Cooling PID regulation band (°) |
| `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia | `1` | Cooling PID inertia |
| `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` | `100` | Cooling proportional gain (low) |
| `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` | `0` | Cooling proportional gain (high) |
| `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` | `5` | Cooling integrative gain low |
| `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` | `0` | Cooling integrative gain high |
| `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` | `100` | Cooling derivative gain low |
| `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` | `0` | Cooling derivative gain high |
| `COOLING_PROPORTIONAL_SPEED_1` | `1..98` | `33` | Cooling proportional speed 1 (%) |
| `COOLING_PROPORTIONAL_SPEED_2` | `2..99` | `67` | Cooling proportional speed 2 (%) |
| `COOLING_PROPORTIONAL_SPEED_3` | `3..100` | `100` | Cooling proportional speed 3 (%) |
| `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled | `0` | Cooling pushbutton fan coil automatic speed |
| `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled | `1` | Cooling anti-seizing up protection |

### Published defaults and interpretation

| Surface | Published value / constraint | Evidence |
| --- | --- | --- |
| Heating/cooling selectable range | `3..40 °C` | Installer p. 5 |
| Comfort | Heating `21 °C`; cooling `25 °C` | Installer p. 5; user p. 4 |
| Eco | Heating `18 °C`; cooling `28 °C` | Installer p. 5; user p. 4 |
| Protection | Antifreeze `7 °C`; heat protection `35 °C`; installer-adjustable | Installer p. 5; user p. 5 |
| Catalogue set-point scale | Stored values/defaults are retained verbatim; step `0.5 °C` and defaults 42/50, 36/56, 14/70 align with twice the Celsius values above. Scale interpretation is inferred; wire representation not captured | Object `95` range text plus installer defaults |
| Automatic changeover | Between setpoint ± threshold: keep function; above upper bound: cooling; below lower bound: heating; illustrated threshold `2 °C` | Installer pp. 12-14; configurable threshold, not universal fixed default |
| Slave probes | Up to `9` compatible no-knob SLAVE probes averaged; actuator/pump allocation numbers `1..9` | Installer pp. 30, 51-52 |
| Thresholds | Automatic regulation band `0.1 °C`; manual fan-coil band `0.1..1 °C`, other loads `0.1..0.5 °C` | Installer pp. 27, 54-55 |
| PID inertia presets | Low: fan-coil; medium: heating radiator / cooling panel; high: floor; custom parameters possible | Installer p. 54 |
| Continuous fan | Auto speed duration `1..254 min` or infinite; selected speed duration infinite; continuous mode excludes fan delay | Installer p. 53 |
| Anti-blocking | Zone valve operated `2 min` weekly after inactivity | Installer p. 53 |
| Contact action | Separate heating/cooling opening/closing action, activation delay, timeout and contact-number scenario trigger through MH202 | Installer pp. 28-29, 56-57 |
| Display/buttons | Software backlight levels/automatic light-based setting, Celsius/Fahrenheit, measured-temperature visibility, window symbol and key locks | Installer pp. 58-59; scale mismatch reconciled below |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `771` | `95` | `3308` | `HEATING_CONTACT_PUSHBTN_LOCK` | `2` = Enabled_contact_closed | `0` | Heating contact pushbutton locking; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3309` | `COOLING_CONTACT_PUSHBTN_LOCK` | `2` = Enabled_contact_closed | `0` | Cooling contact pushbutton locking; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3310` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3311` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3312` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3313` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3314` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3315` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3316` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3317` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3318` | `ACTUATOR_N=9_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3319` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter; `5` = Fil Pilote | `0` | Load type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3320` | `COOLING_ACTUATOR_TYPE` | `10` = IR emitter | `0` | Load type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3321` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |
| `771` | `95` | `3322` | `FUNCTION_CHANGE_BY_LOCAL_BUTTON` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Pushbutton "heating/cooling" change |
| `771` | `95` | `3323` | `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Calibration procedure |
| `771` | `95` | `3324` | `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | User settings procedure |
| `771` | `95` | `3325` | `WINDOWS_CONTACT_ICON` | `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open | `0` | Windows contact icon; reusable default `0` is outside this subset; filter supplies no replacement default |
| `771` | `95` | `3668` | `BACKLIGHT_STANDBY_LEVEL` | `10` = Level 10; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9 | `10` | Backlight stand-by level |
| `771` | `95` | `3748` | `EXTERNAL_SENSOR_TYPE` | `0` = BTicino BT-3457; `1` = Vantage 8051 (entire reusable range retained) | `0` | External temperature sensor type |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion reference is attached to these slot rows. Resolve the active Object and apply its firmware-specific domain restrictions separately. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `9` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Function | Applicability | Evidence / reference |
| --- | --- | --- |
| Thermoregulation | Heating, cooling, seasonal selection or enabled automatic changeover; actuator type and independent heat/cold circuits constrain operation | [`WHO 4`](../../functional/who-4-temperature-control/); Object `95`; installer pp. 11-14 |
| Local operation | Programmed temperature, protection and manual/automatic three-speed fan; disabled options ignore their key | Installer pp. 6, 63-70; user pp. 6-15 |
| Residential control | MyHOME Up and HOMETOUCH can set temperature/protection/fan and heat/cold selection; last remote change overrides local setting | Installer pp. 71-82; user pp. 9, 16-18, 22-27 |
| Hotel control | HotelSupervision additionally activates Comfort/Eco and true thermostat `OFF`, manages system mode and disables local keys | Installer pp. 74-76; user pp. 19-21 |
| Contact integration | Window opening/closing indication and configured action, including true `OFF` and scenario trigger; action is installer-selected | Installer pp. 56-57, 70, 83 |
| Humidity/system integration | Source-specific 2020 F459 and 2026 F460/Classe 300EOS/Home + Project logic; no humidity Object added to catalogue item2242 | Respective sheets p. 1 |

### Published interaction matrix (2018/2020 and manuals)

| Function | Thermostat | MyHOME Up | HotelSupervision | HOMETOUCH |
| --- | --- | --- | --- | --- |
| Programmed temperature | Yes | Yes | Yes | Yes |
| Protection activation | Yes | Yes | Yes | Yes |
| Comfort activation | No | No | Yes | No |
| Eco activation | No | No | Yes | No |
| True `OFF` | No | No | Yes | No |
| Fan adjustment | Yes | Yes | Yes | Yes |
| Summer/winter selection | No | Yes | Yes | Yes (2020 sheet) |

The 2018 sheet/manual interaction table omits a summer/winter row; the 2020 sheet adds it. The 2026 sheet retains the same first six functions but lists Thermostat/MyHOME/HotelSupervision and omits the HOMETOUCH column. The manuals still document HOMETOUCH; column omission alone does not prove support was removed. The local `ON`/`OFF` key and MyHOME Up’s `OFF` control select protection, whereas HotelSupervision’s true `OFF` stops regulation. Local-contact programming can also issue true `OFF`.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Configure the thermostat through the appropriate gateway/system route and identify the Physical Device by its actual ID; do not treat example IDs in manuals as values. The base and front from each individual pack must stay paired. Select type/function/zone, compatible load actuators and pumps, and any slave probes before thresholds and contact behavior. The wizard identifies reachable devices by key press or scan, then selects an unoccupied channel. Reset and reassociate an already-configured thermostat deliberately; reused actuator channels trigger a conflict, not a second independent allocation.

Validate temperature ordering: minimum below maximum; heating Comfort above Eco; cooling Comfort below Eco; all within the selected minimum/maximum. Cross heating/cooling limits apply only when both functions have at least one actuator or pump; the catalogue field prose carries these dependencies. Publisher software rejects conflicting setpoints. Automatic changeover is for compatible independent heating/cooling circuits such as four-pipe fan-coils. Use PID settings for proportional loads; keep increasing speed thresholds above the regulation band. Pump delay permits valves to open before circulation; fan advance/delay prevents undesired initial cold airflow. Continuous ventilation and fan delay are mutually exclusive in the manual.

Contact action delay is cancelled if the contact returns before the delay; action timeout limits its duration even if the contact remains open. Local key disabling may be global or contact-dependent. Window indication does not alone specify an actuator action. Temperature changes save after the flashing ends; subsequent remote changes prevail. After first installation or ER4/suspect temperature, the manuals say wait at least `5 h` before rechecking/calibrating, while sheets say a few minutes; the source difference remains explicit.

| Displayed state / error | Published consequence | Evidence |
| --- | --- | --- |
| Slow configuration flash | Configuration in progress | Installer p. 83; user p. 28 |
| Fast configuration flash | Not configured | Installer p. 84; user p. 29 |
| `Er1` | Pump not responding | Installer p. 85 |
| `Er2` | Actuator not responding | Installer p. 85 |
| `Er3` | Slave probe not responding | Installer p. 85 |
| `Er4` | Temperature-sensor fault; thermostat `OFF`, local actions disabled | Installer p. 85 |
| `Er5` | Internal fault; thermostat `OFF`, local actions disabled | Installer p. 85 |
| `Er6` | Capacitive key-sensor fault | Installer p. 85 |
| `Er1/2/3/6` handling | Current mode maintained; any-key error reset; recurrence after `15 min` if fault persists | Installer p. 85 |

## Source reconciliation

The retained exact-product revisions are separately accounted for. The `ST-00000215-EN` filename contains Russian text and its ratings require visual inspection: supply `18..27 Vdc`, maximum `60 mA`, operating `0..40 °C` and setpoint `3..40 °C` in `0.5 °C` steps agree with later sheets. Its 2018 function/method tables agree with the historical manuals. The English 2020 sheet adds humidity/F459, controller incompatibility and summer/winter row. The 2026 sheet adds KB/KC/KS, native humidity logic, compatible/excluded mounting boxes and Home + Project; it retains core ratings and MyHOME Suite. LE10329AC adds package pairing and optional anti-removal instructions. The tested older LE10329AA URL returns byte-identical AC data, so it provides no retained AA revision.

| Issue | Reconciliation / unresolved limit | Evidence |
| --- | --- | --- |
| Operating temperature | Sheet/manual `0..40 °C`, current KW export `-5..35 °C`; measuring-range attribute is another scope. No one rating silently replaces another | 2020/2026 sheets; installer p. 7; KW export p. 2 |
| Geometry | Two-module mounting and export `45 x 90 x 10 mm` have no assembly/depth explanation; not converted into installed overall size | Sheets; KW export |
| Actuator filters | Firmware `771` filters permit IR emitter/Fil Pilote for the nine ACTUATOR_TYPE fields and heating type, only IR for cooling. Published sheets specify F430 relay/proportional actuators; restrictions also exclude reusable default0. Stored subsets retained, unresolved, not rewritten as excluded values | Filters `3310..3320`; exact sheets p. 1 |
| Contact key lock | Firmware filters `3308/3309` admit only `2`=Enabled_contact_closed, exclude default0; manual describes disabled or enabled when open. No polarity correction guessed | Object `95`/filter table; installer p. 59 |
| Window symbol | Filter `3325` admits `2/3/4`, excludes default0; manual describes several indication choices, with no proven mapping | Object `95`/filter table; installer p. 58 |
| Backlight scale | Installer says five levels/automatic; illustration and current text also use display level10; catalogue EN_CONF range preserves its own named scale. No five-to-ten conversion established | Installer pp. 7, 27, 58; Object `95` |
| `OFF` wording | Local `ON`/`OFF` and app `OFF` mean protection; true `OFF` belongs to HotelSupervision or configured contact. Introductory user prose says setpoints can be activated by MyHOME Up, but its explicit table excludes Eco/Comfort | User pp. 4-5, 8, 17, 21, 28; sheets |
| Stabilisation | Sheets say a few minutes; installer/user say at least5h after first installation, ER4 or suspect measurement. Calibration procedure beyond that note is not specified | Sheets p. 2; installer p. 85; user p. 30 |
| Catalogue maturity | Missing build row is unknown; no physical configurator fields beyond AID; Hotel thermostat Object is reused for a residential product | Firmware `771`; exact manuals |
| Export classifications | KW export says Programmable No / Interoperability No despite documented configuration and system integration. These attributes are not a negation of the product-specific procedures | Export p. 2; current sheet p. 2 |

## Evidence limits and open work

- Resolve the actuator, contact-lock and window-symbol filters against actual MyHOME Suite parameter behavior and sanitized runtime configuration.
- Resolve source temperature/geometry/backlight-scale differences, measured humidity specifications and stabilisation/calibration instructions.
- Corroborate one active Object `95` Module, half-degree/scaled fields, errors and accepted actuator/pump configurations on all three variants; installed hardware/build remains unknown.
- The known French installer translation and broader Living Now catalogues are not independently reconciled here; the full English installer/user and three dated technical sheets define this dossier’s retained revision scope. Added KB/KC/KS identities require separate catalogue mapping.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
