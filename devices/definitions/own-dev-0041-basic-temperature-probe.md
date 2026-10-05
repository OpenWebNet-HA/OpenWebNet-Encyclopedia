# Basic temperature probe

## Summary

This basic temperature probe provides room-temperature sensing for a configured zone in the SCS temperature-control system. Its heating and cooling role depends on the selected configuration; additional physical specifications remain undocumented in the retained sources.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0041` | Project identity |
| Technical description | SCS basic temperature probe for zone sensing | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `HC/HS/HD4693`, `L/N/NT4693`, `573920`, `573921`, `067458` | Canonical commercial records |
| Catalogue item | `1862` | Implementation evidence |
| Main catalogue system | Temperature control | Implementation evidence |
| Item model / `modobj` | `21` | Implementation evidence |
| Firmware definition | `152 / 6.0.0`; `165 / 5.2.0` | Implementation evidence |
| Declared Modules | `1` | Firmware catalogue |
| Categories | Temperature control, HVAC, Sensor | Capability model |

SCS basic temperature probe for zone sensing.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS/HD4693` | established catalogue identity for item `1862` | canonical commercial record |
| BTicino - LivingLight | `L/N/NT4693` | established catalogue identity for item `1862` | canonical commercial record |
| Legrand - Arteor | `573920` | established catalogue identity for item `1862` | canonical commercial record |
| Legrand - Arteor | `573921` | established catalogue identity for item `1862` | canonical commercial record |
| Legrand - Céliane | `067458` | established catalogue identity for item `1862` | canonical commercial record |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `HC4693` | `8012199806570` | [Archived original](https://archive.openwebnet-ha.org/sha256/7d/cc/7dcc11f63cea1c35a1e5512948b1fa668b237c86124da64c594edc83eb77a76f.pdf), `HC4693-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HS4693` | `8012199806587` | [Archived original](https://archive.openwebnet-ha.org/sha256/ca/6f/ca6f3844bfe681b0eaa5ba4bdc58f66d9073a20fcebfe0314ce91cfc44581f82.pdf), `HS4693-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HD4693` | `8012199987712` | [Archived original](https://archive.openwebnet-ha.org/sha256/e4/94/e4947e9d4763e975170ce126e13aa1fe3697b2d99bb1d2afdfa94f50b26064d0.pdf), `HD4693-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `L4693` | `8012199800820` | [Archived original](https://archive.openwebnet-ha.org/sha256/95/27/9527722ea016b62620ccc04332dd49ccacfda724e448c4b590dcfca9c9157dcb.pdf), `L4693-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `N4693` | `8012199800837` | [Archived original](https://archive.openwebnet-ha.org/sha256/5b/f4/5bf4047d1b33701f0abc2d4bb78d888334513f5f2e0d4f03dc51ab15e3c99227.pdf), `N4693-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `NT4693` | `8012199801155` | [Archived original](https://archive.openwebnet-ha.org/sha256/df/9a/df9a54968b961543af72bc5b75cb78e0a70d804ffa40680f4e1a7ef4d9c9b1dd.pdf), `NT4693-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `067458` | `3245060674588` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/2d/96/2d96d2e66e3f7dbf0e8b27849636178c6919f019755809a2e9c3397d63f24dda.pdf), `067458-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| No dedicated Device-specific publisher source currently archived | source gap | current review | Catalogue extraction complete; direct product documentation remains to be recovered | - | - |
| `HC4693-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HC4693` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/7d/cc/7dcc11f63cea1c35a1e5512948b1fa668b237c86124da64c594edc83eb77a76f.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4693) |
| `HS4693-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HS4693` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/ca/6f/ca6f3844bfe681b0eaa5ba4bdc58f66d9073a20fcebfe0314ce91cfc44581f82.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4693) |
| `HD4693-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HD4693` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/e4/94/e4947e9d4763e975170ce126e13aa1fe3697b2d99bb1d2afdfa94f50b26064d0.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4693) |
| `L4693-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4693` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/95/27/9527722ea016b62620ccc04332dd49ccacfda724e448c4b590dcfca9c9157dcb.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4693) |
| `N4693-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `N4693` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/5b/f4/5bf4047d1b33701f0abc2d4bb78d888334513f5f2e0d4f03dc51ab15e3c99227.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4693) |
| `NT4693-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `NT4693` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/df/9a/df9a54968b961543af72bc5b75cb78e0a70d804ffa40680f4e1a7ef4d9c9b1dd.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4693) |
| `067458-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067458` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/2d/96/2d96d2e66e3f7dbf0e8b27849636178c6919f019755809a2e9c3397d63f24dda.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/sonde-pour-gestion-de-temperature-myhome-up-celiane) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Product role | Zone temperature sensing probe | Catalogue item and system mapping |
| Declared logical modules | 1 | Canonical firmware catalogue |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1862` | Implementation evidence |
| Technical item description | Basic temperature probe | Implementation evidence |
| Main system | Temperature control | Implementation evidence |
| Item model / `modobj` | `21` | Implementation evidence |
| Commercial records | `5` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `152` | `6` | `0` | `0` | `1` | Not catalogue default | Official |
| `165` | `5` | `2` | `0` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `152` | `1` | `184` Master probe | Fixed/designated metadata | `670` | `184` | `465` |
| `152` | `1` | `221` Slave probe | Candidate alternative | `1335` | `546` | `694` |
| `165` | `1` | `36` Temperature control probe | Fixed/designated metadata | `1383` | `36` | `729` |
| `165` | `1` | `221` Slave probe | Candidate alternative | `1384` | `546` | `730` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `152` | `508` Thermoregulation probe virgin | `1` | `36`, `184`, `221` | `529` | `26` |
| `165` | `508` Thermoregulation probe virgin | `1` | `36`, `184`, `221` | `529` | `45` |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `152` | Physical configuration | supported route for this Device family |
| `152` | Virtual Configuration | supported route for this Device family |
| `152` | Advanced Configuration | supported route for this Device family |
| `165` | Physical configuration | supported route for this Device family |
| `165` | Virtual Configuration | supported route for this Device family |
| `165` | Advanced Configuration | supported route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `152` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `152` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `152` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `152` | `SLA` | `0..9` | `0` | `SLA`; Thermoregulation slave probe |
| `152` | `MOD` | `0`; `11` = `SLA` | `0` | MOD; Mode (Master,Slave) |
| `165` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `165` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `165` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `165` | `SLA` | `0..8` | `0` | `SLA`; Thermoregulation slave probe |
| `165` | `MOD` | `11` = `SLA`; `0` = `CEN` | `0` | MOD; Mode (Master,Slave) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `36` - Temperature control probe

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | Zone |
| `N` | `0..9` | `0` | Device number |
| `P` | `0`; `CEN` = Master | `0` | Master modality; Thermoregulation master mode |
| `MOD` | `11` = `SLA`; `0` = `CEN` | `0` | Modality; Mode (`SLA`,`CEN`) |
| `SLA` | `0..8` | `0` | Slave number |
| `RISC` | `0` = Disable; `1` = Enable | `1` | Winter modality; Winter mode |
| `COND` | `0` = Disable; `1` = Enable | `0` | Summer modality; Summer mode |
| `ZAZB_CENTRALE` | `01..99` | `01` | Control unit address |


### Object `184` - Master probe

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `FUNCTION` | `0` = Heating; `1` = Cooling; `2` = Heating & cooling | `0` | Function type |
| `ZAZB` | `00..99` | `01` | Zone |
| `COND` | `0` = Disable; `1` = Enable | `0` | Summer modality |
| `RISC` | `0` = Disable; `1` = Enable | `1` | Winter modality |
| `ZAZB_CENTRAL` | `00..99` | `01` | Temperature Control unit address |
| `COMFORT_HEATING_SETPOINT` | `7..80` | `42` | Comfort; Comfort heating setpoint > Eco heating setpoint |
| `ECO_HEATING_SETPOINT` | `6..79` | `36` | Eco; Eco heating setpoint < Comfort heating setpoint |
| `ANTIFREEZE_SETPOINT` | `6..80` | `14` | Antifreeze |
| `HEATING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Heating fan delay; checked only if "Heating actuator type" is set to one of values related to fan coil |
| `HEATING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Automatic heating thresholds settings; For automatic, while checking configuration, set parameters 8, 9, 10 according to device specific settings. |
| `HEATING_REGULATION_BAND` | `1..10` | `1` | Heating setpoint allowance |
| `HEATING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 2 threshold > Heating regulation band |
| `HEATING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Heating actuator type" is set to one of values related to fan coil and if "Heating thresholds settings" is set to Manual setting: Heating Fan coil speed 3 threshold > Heating Fan coil speed 2 threshold |
| `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact opening; If parameter "Heating contact opening" is set to 0, 4, parameter "Heating contact opening timeout" must be set to 0." If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact opening must be different from 5...25. |
| `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort | `0` | Local contact closing; If parameter "Heating contact closing" is set to 0, 4, parameter "Heating contact closing timeout" must be set to 0." If parameter Heating actuator type is set to 5 (FIL PILOTE), parameter Heating contact closing must be different from 5...25. |
| `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact opening |
| `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Activation delay for local contact closing |
| `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter "Heating contact opening timeout" is different from 0, "Heating contact closing timeout" must be set to 0. |
| `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact closing action; 0 corresponds to infinite. If parameter "Heating contact closing timeout" is different from 0, "Heating contact opening timeout" must be set to 0." |
| `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed | `0` | Heating contact pushbutton locking |
| `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Heating fancoil continuous ventilation |
| `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `COMFORT_COOLING_SETPOINT` | `6..79` | `50` | Comfort; Comfort cooling setpoint < Eco cooling setpoint |
| `ECO_COOLING_SETPOINT` | `7..80` | `56` | Eco; Eco cooling setpoint > Comfort cooling setpoint |
| `THERMAL_PROTECTION_SETPOINT` | `6..80` | `70` | Thermal protection |
| `COOLING_VALVE_ADVANCE_TIME_FOR_FAN_COIL` | `0..255` | `0` | Cooling fan delay; Checked only if "Cooling actuator type" is set to one of values related to fan coil |
| `COOLING_THRESHOLDS_SETTINGS` | `0` = Automatic; `1` = Manual setting | `0` | Automatic cooling thresholds settings; For automatic, while checking configuration, set 28, 29, 30 according to device specific settings. |
| `COOLING_REGULATION_BAND` | `1..10` | `1` | Cooling setpoint allowance |
| `COOLING_FAN_COIL_SPEED_2_THRESHOLD` | `2..20` | `6` | First speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 2 threshold > Cooling regulation band |
| `COOLING_FAN_COIL_SPEED_3_THRESHOLD` | `3..30` | `10` | Second speed threshold for fancoils; Checked only if "Cooling actuator type" is set to one of values related to fan coil and if "Cooling thresholds settings" is set to Manual setting: Cooling Fan coil speed 3 threshold > Cooling Fan coil speed 2 threshold |
| `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact opening; If parameter Cooling contact opening is set to 0, 4, parameter Cooling contact opening timeout must be set to 0. |
| `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort | `0` | Local contact closing; If parameter "Cooling contact closing" is set to 0, 4, parameter "Cooling contact closing timeout" must be set to 0. |
| `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` | `0` | Timeout for local contact opening action |
| `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` | `0` | Timeout for local contact closing action |
| `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` | `0` | Timeout for local contact opening action; 0 corresponds to infinite. If parameter "Cooling contact opening timeout" is different from 0, "Cooling contact closing timeout" must be set to 0. |
| `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` | `0` | Timeout for local contact closing action; 0 corresponds to infinite. If parameter Cooling contact closing timeout is different from 0, Cooling contact opening timeout must be set to 0. |
| `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed | `0` | Cooling contact pushbutton locking |
| `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled | `1` | Cooling fancoil continuous ventilation |
| `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `ACTUATOR_N=1_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 1 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=2_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 2 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=3_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 3 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=4_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 4 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=5_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 5 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=6_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 6 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=7_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 7 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=8_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 8 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=9_FUNCTION` | `0` = Not installed; `1` = Heating only; `2` = Cooling only; `3` = Heating and cooling | `0` | Actuator 9 function; If this parameter is set to "Heating and cooling", it must be checked that "Heating actuator type" and "Cooling actuator type" are equal. |
| `ACTUATOR_N=1_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=2_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=3_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=4_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=5_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=6_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=7_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=8_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `ACTUATOR_N=9_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; The highlighted values must not be implemented into key object (they are dedicated to future use). This parameter has not to be shown. In the final check, this parameter must be assigned to: - "Heating actuator type" if "Actuator function" is set to Heating only. - "Cooling actuator type" if "Actuator function" is set to Cooling only. - "Heating actuator type" or "Cooling actuator type" if "Actuator function" is set to Heating and cooling or is set to Not installed. |
| `HEATING_ACTUATOR_TYPE` | `0` = `ON`/`OFF`; `1` = Open/Close; `2` = 2 pipes fan coil with on/off valve; `4` = Gateway; `5` = Fil Pilote; `6` = 2 pipes fan coil with proportional valve; `7` = 4 pipes fan coil with on/off valves; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `10` = IR emitter; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Load type; The highlighted values must not be implemented into key object (they are dedicated to future use). |
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
| `HEATING_PUMP_DELAY` | `0..255` | `0` | Time delay for heating pumps |
| `COOLING_PUMP_DELAY` | `0..255` | `0` | Time delay for cooling pumps |
| `NUMBER_OF_SLAVES` | `0..9` | `0` | Number of slave probes |
| `LED_ENABLE` | `0` = Enabled; `1` = Disabled | `0` | Led enable |
| `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit | `0` | Temperature format |
| `BACKLIGHT_STAND_BY_LEVEL` | `0` = `OFF`; `1` = `ON` | `1` | Display standby backlight |
| `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED | `0` | Ambient temperature visualization |
| `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 | `10` | Backlight stand-by level |
| `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled | `0` | Disable all pushbuttons |
| `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled | `0` | Pushbutton modality change |
| `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled | `0` | Calibration procedure |
| `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled | `0` | User settings procedure |
| `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open | `0` | Windows contact icon |
| `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled | `0` | Windows contact number |
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


### Object `221` - Slave probe

Catalogue Object key `546` maps to external Object `221`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | Zone |
| `SLA` | `1..9` | `1` | Slave number |
| `LED_ENABLE` | `0` = Enabled; `1` = Disabled | `0` | Led enable |
| `EXTERNAL_SENSOR_TYPE` | `0` = BTicino 3457; `1` = Vantage 8051 | `0` | External temperature sensor type |
| `RISC` | `0` = Disable; `1` = Enable | `1` | Winter modality; Winter mode |
| `COND` | `0` = Disable; `1` = Enable | `0` | Summer modality; Summer mode |
| `ZAZB_CENTRALE` | `00..99` | `01` | Temperature Control unit address |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `152` | `1` | `184` | `4918` | `MOD=0` | `1000` |
| `152` | `1` | `221` | `4917` | `MOD=11` | `1000` |
| `165` | `1` | `36` | `4918` | `MOD=0` | `1000` |
| `165` | `1` | `221` | `4917` | `MOD=11` | `1000` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `152` | `184` | `603` | `COMFORT_HEATING_SETPOINT` | `7..80` (entire reusable range retained) | `42` | Comfort heating setpoint temperature (step 0,5°C) |
| `152` | `184` | `604` | `ECO_HEATING_SETPOINT` | `6..79` (entire reusable range retained) | `36` | Eco heating setpoint temperature (step 0,5°C) |
| `152` | `184` | `605` | `HEATING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact closing |
| `152` | `184` | `606` | `HEATING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Heating eco; `27` = Heating comfort (entire reusable range retained) | `0` | Heating contact opening |
| `152` | `184` | `607` | `HEATING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact activation (step 5s) |
| `152` | `184` | `608` | `HEATING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact (step 1min) |
| `152` | `184` | `609` | `ECO_COOLING_SETPOINT` | `7..80` (entire reusable range retained) | `56` | Eco cooling setpoint temperature (step 0,5°C) |
| `152` | `184` | `610` | `COMFORT_COOLING_SETPOINT` | `6..79` (entire reusable range retained) | `50` | Comfort cooling setpoint temperature (step 0,5°C) |
| `152` | `184` | `611` | `COOLING_CONTACT_CLOSING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact closing |
| `152` | `184` | `612` | `COOLING_CONTACT_OPENING` | `0` = No action; `1` = Protection; `2` = Off; `4` = Previous state; `5` = Manual 10°; `6` = Manual 11°; `7` = Manual 12°; `8` = Manual 13°; `9` = Manual 14°; `10` = Manual 15°; `11` = Manual 16°; `12` = Manual 17°; `13` = Manual 18°; `14` = Manual 19°; `15` = Manual 20°; `16` = Manual 21°; `17` = Manual 22°; `18` = Manual 23°; `19` = Manual 24°; `20` = Manual 25°; `21` = Manual 26°; `22` = Manual 27°; `23` = Manual 28°; `24` = Manual 29°; `25` = Manual 30°; `26` = Cooling eco; `27` = Cooling comfort (entire reusable range retained) | `0` | Cooling contact opening |
| `152` | `184` | `613` | `COOLING_CONTACT_OPENING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for cooling contact activation (step 5s) |
| `152` | `184` | `614` | `COOLING_CONTACT_OPENING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for cooling contact (step 1min) |
| `152` | `184` | `615` | `ACTUATOR_N=1_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 1; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `616` | `ACTUATOR_N=2_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 2; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `617` | `ACTUATOR_N=3_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 3; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `618` | `ACTUATOR_N=4_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 4; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `619` | `ACTUATOR_N=5_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 5; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `620` | `ACTUATOR_N=6_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 6; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `621` | `ACTUATOR_N=7_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 7; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `622` | `ACTUATOR_N=8_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 8; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `623` | `ACTUATOR_N=9_TYPE` | `6` = 2 pipes fan coil with proportional valve; `10` = IR emitter; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Type actuator 9; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `624` | `HEATING_ACTUATOR_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Heating_actuator_type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `625` | `COOLING_ACTUATOR_TYPE` | `10` = IR emitter; `6` = 2 pipes fan coil with proportional valve; `8` = 4 pipes fan coil with proportional valves; `9` = Proportional valve; `11` = 2 pipes fan coil with proportional speed control; `12` = 4 pipes fan coil with proportional speed control | `0` | Cooling_actuator_ type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `626` | `TEMPERATURE_FORMAT` | `0` = Celsius; `1` = Fahrenheit (entire reusable range retained) | `0` | Temperature Format |
| `152` | `184` | `629` | `HEATING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for heating contact closing activation (step 5s) |
| `152` | `184` | `630` | `HEATING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for heating contact closing (step 1min) |
| `152` | `184` | `631` | `COOLING_CONTACT_CLOSING_ACTIVATION_DELAY` | `0..255` (entire reusable range retained) | `0` | Time delay for Cooling contact closing activation (step 5s) |
| `152` | `184` | `632` | `COOLING_CONTACT_CLOSING_TIMEOUT` | `0..255` (entire reusable range retained) | `0` | Timeout for Cooling contact closing (step 1min) |
| `152` | `184` | `633` | `BACKLIGHT_STAND_BY_LEVEL` | `0` = `OFF`; `1` = `ON` (entire reusable range retained) | `1` | Backlight stand-by level |
| `152` | `184` | `634` | `RISC` | `0` = Disable; `1` = Enable (entire reusable range retained) | `1` | Winter modality |
| `152` | `184` | `635` | `COND` | `0` = Disable; `1` = Enable (entire reusable range retained) | `0` | Summer modality |
| `152` | `184` | `1914` | `AMBIENT_TEMPERATURE_VISUALIZATION` | `0` = ENABLED; `1` = DISABLED (entire reusable range retained) | `0` | Ambient temperature visualization |
| `152` | `184` | `2672` | `ANTIFREEZE_SETPOINT` | `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `50`; `51`; `52`; `53`; `54`; `55`; `56`; `57`; `58`; `59`; `60`; `61`; `62`; `63`; `64`; `65`; `66`; `67`; `68`; `69`; `70`; `71`; `72`; `73`; `74`; `75`; `76`; `77`; `78`; `79`; `80` | `14` | Antifreeze; reusable default `14` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `2677` | `HEATING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Heating contact pushbutton locking |
| `152` | `184` | `2684` | `HEATING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating fancoil continuous ventilation |
| `152` | `184` | `2691` | `HEATING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Heating fan coil continuous ventilation timeout (minutes) |
| `152` | `184` | `2698` | `HEATING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Heating PID regulation band (°) |
| `152` | `184` | `2705` | `HEATING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Heating PID inertia |
| `152` | `184` | `2712` | `HEATING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating proportional gain (low) |
| `152` | `184` | `2719` | `HEATING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating proportional gain (high) |
| `152` | `184` | `2726` | `HEATING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Heating integrative gain low |
| `152` | `184` | `2733` | `HEATING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Heating integrative gain high |
| `152` | `184` | `2740` | `HEATING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Heating derivative gain low |
| `152` | `184` | `2747` | `HEATING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Heating derivative gain high |
| `152` | `184` | `2754` | `HEATING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Heating proportional speed 1 (%) |
| `152` | `184` | `2761` | `HEATING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Heating proportional speed 2 (%) |
| `152` | `184` | `2768` | `HEATING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Heating proportional speed 3 (%) |
| `152` | `184` | `2775` | `HEATING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Heating pushbutton fan coil automatic speed |
| `152` | `184` | `2782` | `HEATING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Heating anti-seizing up protection |
| `152` | `184` | `2793` | `THERMAL_PROTECTION_SETPOINT` | `10`; `11`; `12`; `13`; `14`; `15`; `16`; `17`; `18`; `19`; `20`; `21`; `22`; `23`; `24`; `25`; `26`; `27`; `28`; `29`; `30`; `31`; `32`; `33`; `34`; `35`; `36`; `37`; `38`; `39`; `40`; `41`; `42`; `43`; `44`; `45`; `46`; `47`; `48`; `49`; `6`; `7`; `8`; `9` | `70` | Thermal protection; reusable default `70` is outside this subset; filter supplies no replacement default |
| `152` | `184` | `2798` | `COOLING_CONTACT_PUSHBTN_LOCK` | `0` = Disabled; `1` = Enabled when contact is open; `2` = Enabled when contact is closed (entire reusable range retained) | `0` | Cooling contact pushbutton locking |
| `152` | `184` | `2805` | `COOLING_FANCOIL_VENTILATION_FUNCTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling fancoil continuous ventilation |
| `152` | `184` | `2812` | `COOLING_FANCOIL_VENTILATION_FUNCTION_TIMEOUT` | `0..254`; `255` = Infinite (entire reusable range retained) | `0` | Cooling fan coil continuous ventilation timeout (minutes) |
| `152` | `184` | `2819` | `COOLING_PID_REGULATION_BAND` | `6..30` (entire reusable range retained) | `16` | Cooling PID regulation band (°) |
| `152` | `184` | `2826` | `COOLING_PID_INERTIA` | `0` = Low inertia; `1` = Medium inertia; `2` = High inertia; `3` = Custom inertia (entire reusable range retained) | `1` | Cooling PID inertia |
| `152` | `184` | `2833` | `COOLING_PROPORTIONAL_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling proportional gain (low) |
| `152` | `184` | `2840` | `COOLING_PROPORTIONAL_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling proportional gain (high) |
| `152` | `184` | `2847` | `COOLING_INTEGRATIVE_GAIN_LOW` | `0..100` (entire reusable range retained) | `5` | Cooling integrative gain low |
| `152` | `184` | `2854` | `COOLING_INTEGRATIVE_GAIN_HIGH` | `0` (entire reusable range retained) | `0` | Cooling integrative gain high |
| `152` | `184` | `2861` | `COOLING_DERIVATIVE_GAIN_LOW` | `0..255` (entire reusable range retained) | `100` | Cooling derivative gain low |
| `152` | `184` | `2868` | `COOLING_DERIVATIVE_GAIN_HIGH` | `0..3` (entire reusable range retained) | `0` | Cooling derivative gain high |
| `152` | `184` | `2875` | `COOLING_PROPORTIONAL_SPEED_1` | `1..98` (entire reusable range retained) | `33` | Cooling proportional speed 1 (%) |
| `152` | `184` | `2882` | `COOLING_PROPORTIONAL_SPEED_2` | `2..99` (entire reusable range retained) | `67` | Cooling proportional speed 2 (%) |
| `152` | `184` | `2889` | `COOLING_PROPORTIONAL_SPEED_3` | `3..100` (entire reusable range retained) | `100` | Cooling proportional speed 3 (%) |
| `152` | `184` | `2896` | `COOLING_PUSHBTN_FAN_COIL_AUTO_SPEED` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Cooling pushbutton fan coil automatic speed |
| `152` | `184` | `2903` | `COOLING_ANTI_SEIZING_UP_PROTECTION` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `1` | Cooling anti-seizing up protection |
| `152` | `184` | `2910` | `BACKLIGHT_STANDBY_LEVEL` | `1` = Level 1; `2` = Level 2; `3` = Level 3; `4` = Level 4; `5` = Level 5; `6` = Level 6; `7` = Level 7; `8` = Level 8; `9` = Level 9; `10` = Level 10 (entire reusable range retained) | `10` | Backlight stand-by level |
| `152` | `184` | `2917` | `PUSHBUTTON_MANAGEMENT` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Disable all pushbuttons |
| `152` | `184` | `2924` | `PUSHBUTTON_MODALITY_CHANGE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Pushbutton modality change |
| `152` | `184` | `2931` | `CALIBRATION_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Calibration procedure |
| `152` | `184` | `2938` | `USER_SETTINGS_PROCEDURE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | User settings procedure |
| `152` | `184` | `2945` | `WINDOWS_CONTACT_ICON` | `0` = Always `OFF`; `1` = `ON` when open, `OFF` when closed; `2` = Blinking when open, `OFF` when closed; `3` = `ON` when closed, `OFF` when open; `4` = Blinking when closed, `OFF` when open (entire reusable range retained) | `0` | Windows contact icon |
| `152` | `184` | `2952` | `WINDOWS_CONTACT_NUMBER` | `1..201`; `0` = Disabled (entire reusable range retained) | `0` | Windows contact number |
| `152` | `221` | `3753` | `EXTERNAL_SENSOR_TYPE` | `0` = BTicino 3457; `1` = Vantage 8051 (entire reusable range retained) | `0` | External temperature sensor type |
| `165` | `221` | `1522` | `LED_ENABLE` | `0` = Enabled; `1` = Disabled (entire reusable range retained) | `0` | Led enable |
| `165` | `221` | `3754` | `EXTERNAL_SENSOR_TYPE` | `0` = BTicino 3457; `1` = Vantage 8051 (entire reusable range retained) | `0` | External temperature sensor type |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1000` | `ZA=0; ZB=1..9` | `ZAZB=01..09` | Rule `1000` through branch `1001` |
| `1000` | `ZA=1..9; ZB=0..9` | `ZAZB=10..99` | Rule `1000` through branches `1002..1010` |
| `1000` | `ZA=0; ZB=0` | No `00` mapping stored | Do not widen the conversion from the reusable Object domain |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item `1862` / `modobj = 21` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `36`, `184`, `221` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Temperature-control zone sensing; exact heating/cooling behavior remains firmware/Object-filter scoped.

## Observed behavior and corroboration

No sanitized hardware fingerprint or Device-specific protocol capture is currently retained for this exact technical item.

## Programming

Programming must select installed firmware applicability, resolve slot/Object alternatives through catalogue conditions, apply relation filters, and preserve configuration-mode boundaries.

## Source reconciliation

The canonical catalogue establishes the commercial records, firmware applicability, topology, configuration fields, filters and conditions. Publisher sources above are used only for behaviors they directly document; missing dedicated sheets remain explicit gaps.

## Evidence limits and open work

- Recover any missing dedicated publisher sheets for the exact identities.
- Capture a sanitized hardware fingerprint covering identity, firmware, modules, addressing and configuration.
- Corroborate condition/filter behavior through MyHOME Suite and controlled configuration changes.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `HC4693-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HC4693` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/7d/cc/7dcc11f63cea1c35a1e5512948b1fa668b237c86124da64c594edc83eb77a76f.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4693); SHA-256 `7dcc11f63cea1c35a1e5512948b1fa668b237c86124da64c594edc83eb77a76f`.
- `HS4693-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HS4693` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/ca/6f/ca6f3844bfe681b0eaa5ba4bdc58f66d9073a20fcebfe0314ce91cfc44581f82.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4693); SHA-256 `ca6f3844bfe681b0eaa5ba4bdc58f66d9073a20fcebfe0314ce91cfc44581f82`.
- `HD4693-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HD4693` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/e4/94/e4947e9d4763e975170ce126e13aa1fe3697b2d99bb1d2afdfa94f50b26064d0.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4693); SHA-256 `e4947e9d4763e975170ce126e13aa1fe3697b2d99bb1d2afdfa94f50b26064d0`.
- `L4693-ean-product-sheet.pdf`, printed/PDF p. 1: exact `L4693` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/95/27/9527722ea016b62620ccc04332dd49ccacfda724e448c4b590dcfca9c9157dcb.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4693); SHA-256 `9527722ea016b62620ccc04332dd49ccacfda724e448c4b590dcfca9c9157dcb`.
- `N4693-ean-product-sheet.pdf`, printed/PDF p. 1: exact `N4693` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/5b/f4/5bf4047d1b33701f0abc2d4bb78d888334513f5f2e0d4f03dc51ab15e3c99227.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4693); SHA-256 `5bf4047d1b33701f0abc2d4bb78d888334513f5f2e0d4f03dc51ab15e3c99227`.
- `NT4693-ean-product-sheet.pdf`, printed/PDF p. 1: exact `NT4693` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/df/9a/df9a54968b961543af72bc5b75cb78e0a70d804ffa40680f4e1a7ef4d9c9b1dd.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4693); SHA-256 `df9a54968b961543af72bc5b75cb78e0a70d804ffa40680f4e1a7ef4d9c9b1dd`.

- `067458-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067458` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/2d/96/2d96d2e66e3f7dbf0e8b27849636178c6919f019755809a2e9c3397d63f24dda.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/sonde-pour-gestion-de-temperature-myhome-up-celiane); SHA-256 `2d96d2e66e3f7dbf0e8b27849636178c6919f019755809a2e9c3397d63f24dda`.
