# Two-wire concierge switchboard

## Summary

346310 is a concierge switchboard for two-wire audio / video entry systems. Its handset, handsfree audio, 7-inch screen and keypad support calls, door release, camera selection and apartment alarm handling. Master and hierarchical backbone / riser roles determine which calls it manages.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0165` | Project identity |
| Technical description | Two-wire concierge switchboard | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `346310` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1440` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Video door entry system | Main system association |
| Item model / `modobj` | `167` | Main association; independent of project ID |
| Firmware definition | `74` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Audio video, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `346310` | Established catalogue identity | Manufacturer database commercial record `1440` explicitly links this SKU to item `1440` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `346310` | `8005543408025` | [346310-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/7f/02/7f02c13020a67b42159b38475f922e1cc34cda46fd28debb9a908843a6fbca19.pdf) PDF p. 1; `346310-italian-product-sheet.pdf` PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `346310` | Management Center 2Wires | Canonical commercial record `1440` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00680-c-EN.pdf` | Technical Sheet BT00680-C-EN | BT00680-c-EN; 03/10/2016 | Printed/PDF pp. 1-2 exact specifications / roles; pp.3-9 topology examples; pp.10-11 external audible notification and relay application. Examples do not establish unrestricted accessory compatibility. | [Archived original](https://archive.openwebnet-ha.org/sha256/0d/68/0d6806e6d5d5a50226916ebe0fc87cfcfb964a7574f1192ceb7d056927c4f376.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/BT00680-c-EN.pdf) |
| `O1224E_I_EN.pdf` | Technical Guide O1224E_I_EN | O1224E_I_EN; printed publication date not established | 346310 installation: printed/PDF pp. 5-15, 16-49; topology, MASTER / backbone / riser roles, connections and setup. | [Archived original](https://archive.openwebnet-ha.org/sha256/37/d6/37d6ab4b75d546fdc92ea2e0f3a26a4a4247603e03deb4c3730601d5670b589e.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/O1224E_I_EN.pdf) |
| `O1224E_S_EN.pdf` | Technical Guide O1224E_S_EN | O1224E_S_EN; printed publication date not established | 346310 software: printed/PDF pp. 4-10, 11-48; transfer / update, identity / address book, service internal unit, modes and alarm / automation settings. | [Archived original](https://archive.openwebnet-ha.org/sha256/f3/92/f3922fddcdaef45210ce19bbb8131133598fc10fff13fc688d25807c8dd0980b.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/O1224E_S_EN.pdf) |
| `O1224E_U_EN.pdf` | Technical Guide O1224E_U_EN | O1224E_U_EN; printed publication date not established | 346310 user operations: printed/PDF pp. 4-25, 26-55; calls, door / camera, alarms and operator settings. | [Archived original](https://archive.openwebnet-ha.org/sha256/2b/07/2b0705eea624af872819807901ced9de4e5677e23e87568f8045e520fef7d5da.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/O1224E_U_EN.pdf) |
| `346310-publisher-product-sheet.pdf` | Exact English product export | Publisher DATASHEET; 05.10.2026 | PDF pp. 1-4: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/7f/02/7f02c13020a67b42159b38475f922e1cc34cda46fd28debb9a908843a6fbca19.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-346310&include_technical=1) |
| `346310-italian-product-sheet.pdf` | Exact Italian product export | Product export retrieved 05/10/2026; boilerplate compliance dates are not product publication dates | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/88/5a/885ae01d3dfe490c26d707fe44d0c418792849442dada4eeedfadcd6d905ffdc.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-346310) |
| `BT00680_c_IT.pdf` | Manufacturer Italian / installation document | BT00680_c_IT; 03/10/2016 | Printed/PDF pp. 1-2 exact specifications / roles; pp.3-9 topology examples; pp.10-11 external audible notification and relay application. Examples do not establish unrestricted accessory compatibility. | [Archived original](https://archive.openwebnet-ha.org/sha256/13/81/13810bd6cee5be8633084bc3ec6c5ac81f53dfadd8534fe2de1dac71584a4598.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/BT00680_c_IT.pdf) |
| `O1224E_I_IT.pdf` | Manufacturer Italian / installation document | O1224E_I_IT; printed publication date not established | 346310 installation: printed/PDF pp. 5-15, 16-49; topology, MASTER / backbone / riser roles, connections and setup. | [Archived original](https://archive.openwebnet-ha.org/sha256/14/36/14360ab68ff7d3f4ec3669890ece291e0e6d683026d8bfd15e3c40ade2e9d2e2.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/O1224E_I_IT.pdf) |
| `O1224E_S_IT.pdf` | Manufacturer Italian / installation document | O1224E_S_IT; printed publication date not established | 346310 software: printed/PDF pp. 4-10, 11-48; transfer / update, identity / address book, service internal unit, modes and alarm / automation settings. | [Archived original](https://archive.openwebnet-ha.org/sha256/66/6e/666e40dacb594dbfce8ff1e403d104c2d54f46c1ed0b02b273a81a5b3567fbab.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/O1224E_S_IT.pdf) |
| `O1224E_U_IT.pdf` | Manufacturer Italian / installation document | O1224E_U_IT; printed publication date not established | 346310 user operations: printed/PDF pp. 4-25, 26-55; calls, door / camera, alarms and operator settings. | [Archived original](https://archive.openwebnet-ha.org/sha256/77/8e/778eb83ef3e40b5cebeda7fb1cebbe9fa66984977a0ddad85426c18a59ca68be.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/O1224E_U_IT.pdf) |
| `TiSwitchboardDevice_README_v1.pdf` | Software TISWITCHBOARDDEVICED_README_V1 | TiSwitchboardDevice_README_v1; 23/07/2025 | PDF pp. 1-1: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/66/98/6698c8c7844cfaa4fb54125ae9d1279bbbfa1706b242cbb7775c6c65195eac6f.pdf) | [Publisher original](https://assets.legrand.com/pim/AUTRE/TiSwitchboardDevice_README_v1.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1440`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `19..27 Vdc` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |
| BUS draw without additional supply | `35 mA standby / 450 mA maximum` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |
| BUS draw with additional supply | `5 mA standby / 20 mA maximum` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |
| Temperature | `5..40 °C` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |
| Dimensions | `290 x 210 x 170 mm as drawing` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |
| Display / mounting | `7-inch colour LCD; integrated table support` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |
| Relay output | `24 Vac / 24 Vdc, 3 A, cos phi 1` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |
| System maximum | `16 switchboards, addresses 0..15` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |
| Hierarchical Sfera requirements | `351100/351200/351300 firmware ≥01.02.31; 351000 batch ≥16W18; 346851 batch ≥16W28` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |
| IP-interface exclusion | `cannot be used in systems with 346890` | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_I_EN` pp. 5-15; `O1224E_U_EN` pp. 4-25 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Model | `Substation` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Type of communication | `Half-duplex` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Type of system | `Hybrid` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Single call function | `Yes` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| General call function | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Installation technique | `Bus system` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Mounting method | `Desktop device` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Degree of protection (IP) | `Other` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Compatible with Apple HomeKit | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Compatible with Google Assistant | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Compatible with Amazon Alexa | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| IFTTT support available | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| degree of impact strength (IK) | `Not applicable` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Storage temperature (Min-Max) | `-10-70 °C` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Voltage type | `DC` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Nominal voltage (Min-Max) | `18-27 V` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Supply current (Min-Max) | `0.005-0.05 A` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Frequency (Min-Max) | `0-0 Hz` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Sound level | `82 dB` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Standby consumption | `5 mA` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Antimicrobial treatment | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Cable nature for connection | `Flexible` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Cable section (Min-Max) | `0.1-2.5 mm²` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Label space / information surface | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Control mode | `Wired` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Hands free | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Loudness setting | `Yes` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Addressable | `Yes` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Door entry system with mobile application | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Remote opening of gate / Electric door opener | `Yes` | `346310-publisher-product-sheet.pdf` PDF p. 3 |
| Connected object | `No` | `346310-publisher-product-sheet.pdf` PDF p. 3 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1440` | Canonical catalogue |
| Technical item description | Management Center 2Wires | Canonical catalogue |
| Item family | Source placeholder description `0`; key `20` | Canonical catalogue |
| Main system | Video door entry system; key `4` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `167` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Video door entry system | `167` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Multimedia | private riser | Canonical item/bus relationship |
| Multimedia | public riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `74` | `1` | `0` | `16` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `74` | `69` | BTicino (key `1`) | `0` | external software | `TiSwitchboardDevice_0100` |

The one parameter-file association is shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `74` | `1` | `115` Management Center 2Wires | Fixed / designated metadata | `2390` | `620` | `1045` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `74` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `74` | USB | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `Switchboard / associated EP address` | Switchboard `0..15`; associated entrance panel `1..80` in technical-sheet configuration | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_S_EN` pp. 12-18 |
| `MASTER / SLAVE` | Single hierarchy; DAY calls routed via operator; NIGHT directly to resident; first answering master / slave takes call | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_S_EN` pp. 12-18 |
| `BACKBONE / RISER` | Riser first, backbone second, apartment last when preceding operators are out of service; backbone entrance calls go to backbone first | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_S_EN` pp. 12-18 |
| `Hierarchical production limits` | Sfera 351100/200/300 firmware ≥01.02.31; 351000 ≥16W18; 346851 ≥16W28 | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_S_EN` pp. 12-18 |
| `Alarm topology, exact examples` | All apartment / common alarms handled by main switchboard address 0; common contacts through F422, maximum 9 interfaces in illustrated topology | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_S_EN` pp. 12-18 |
| `Configuration / transfer` | Icon menu or TiSwitchboardDevice; address-book compilation and ringtone management require PC; transfer / update with powered device over mini-USB | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_S_EN` pp. 12-18 |
| `Rear termination / auxiliary supply` | `ON`/`OFF` termination switch; BUS; 1-2 extra supply; separate optional audible-notification terminal | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_S_EN` pp. 12-18 |
| `Status indicator` | Steady: standby; fast flashing: call; slow flashing: conversation | `BT00680-c-EN` printed/PDF pp. 1-11; `O1224E_S_EN` pp. 12-18 |

### Commissioning software prerequisites

These are the retained readme requirements, separate from product electrical ratings and current operating-system compatibility.

| Property | Published value | Evidence |
| --- | --- | --- |
| Windows | `10` | `TiSwitchboardDevice_README_v1` p.1 |
| Framework | `.NET 3.5 SP1 or higher` | `TiSwitchboardDevice_README_v1` p.1 |
| CPU / RAM | `1 GHz;1 GB(32-bit) or2 GB(64-bit)` | `TiSwitchboardDevice_README_v1` p.1 |
| Disk / display | `1 GB;1024x768` | `TiSwitchboardDevice_README_v1` p.1 |

### Documented operator and commissioning settings

| Setting / role | Documented value or consequence | Retained manufacturer source (printed/PDF pages) |
| --- | --- | --- |
| Backbone address / alarms | Hierarchical backbone is unique, address `0`; riser `1..15` cannot receive technical alarms. Non-hierarchical Master `0..15`, but alarms require address `0`. | O1224E_I_EN pp.38,40-41; O1224E_S_EN pp.18-19 |
| Slave address / association | Local `1..15`; associated Switchboard `0..15`; main entrance panel `1..80`; reproduces associated Master/backbone/riser function. | O1224E_I_EN pp.40-41 |
| Hierarchy routing | Day calls can target backbone alone, or backbone plus riser; never riser alone. Riser `0` in the software list denotes backbone wiring. | O1224E_S_EN pp.20-21 |
| Hierarchy transfer prerequisites | All entrance panels and Switchboards must be connected and working when sending hierarchy configuration. | O1224E_I_EN p.42 |
| Service internal unit priority | Temporary forwarding to configured internal unit; Night entrance-panel routing has priority and bypasses both Switchboard and service unit. | O1224E_I_EN pp.17,29 |
| Multiple service Switchboards | On the same stretch, all but one require additional supply when service forwarding is enabled; associated internal units need different addresses. | O1224E_I_EN p.29 |
| Internal-unit day/night disabled | Riser forwards to backbone; backbone/Master forwards to associated main entrance panel. Enabled mode follows manual/automatic day/night setting. | O1224E_I_EN p.28 |
| Day/night scheduling | Installer menu: up to `6` change times per weekday. PC software: maximum `3` day/night bands per day; weekday entries copied Monday-Friday, Saturday/Sunday separate. | O1224E_I_EN pp.33-34; O1224E_S_EN pp.32-35 |
| Entrance-panel day/night scope | All, main or selected list; list choice is Master-only; hierarchy uses the separate hierarchy table. | O1224E_S_EN pp.32-33 |
| Riser presence | Present/absent applies to riser; absent calls pass to backbone and follow its day/night status. | O1224E_U_EN p.41 |
| Door lock / automation entries | Up to `12` entries with address, description and riser; riser `0` denotes backbone. | O1224E_I_EN p.35; O1224E_S_EN p.26 |
| Relay call behavior | Local or external relay independently enabled for call/alarm. Call repeats `5 s` ON, `5 s` OFF until call ends; alarm stays ON until silenced/acknowledged. | O1224E_S_EN p.29; O1224E_I_EN p.21 |
| Remote notification example | 346210 `MOD=8`; `N/P` encodes associated Switchboard address; do not customize `T` in this example. Output follows Switchboard call/alarm timing. | BT00680-c-EN / BT00680_c_IT p.10 |
| Associated camera | Enable camera and give it the Switchboard local address in `P`; permits caller to see operator. Backbone does not display riser entrance-panel video; main entrance panels remain audio/video. | O1224E_I_EN pp.13,44; BT00680-c-EN pp.8,11 |
| Alarm / notification setup | Enable/disable alarms, with optional Day-only reception; notifications require alarms and include mains lost/restored, low alarm-system battery and door status via `346260`. | O1224E_I_EN p.38; O1224E_S_EN p.27 |
| Alarm status handling | Red = active, yellow = acknowledged, green = solved; acknowledgement and resolution are distinct operator actions. User Alarm Log is presented as backbone-only. | O1224E_U_EN pp.21-23,39-40 |
| Technical alarm types | Flooding, freezer, emergency, gas leak, fire, intrusion, tampering, panic and technical alarm; these are documented UI categories, not verified wire event codes. | O1224E_U_EN p.40 |
| Address-book call modes | Alphanumeric call code or block/floor/apartment. Each component at most `5` characters/digits as stated by installer manual; total `1..8` in software; must match Sfera entrance-panel mode. Changing mode requires clearing saved contacts. | O1224E_I_EN p.45; O1224E_S_EN pp.30-31 |
| Repeated call rings | `1..5` | O1224E_I_EN p.47; O1224E_S_EN pp.30-31 |
| Installer authentication | Numeric `5`-digit password, `0..99999` in software; manufacturer documentation default `12345`; manual recommends customization. Not an installation credential. | O1224E_I_EN pp.27,48; O1224E_S_EN p.22 |
| PC project contents | Select/add localization package, save configuration, configure ringtones and contacts; send them together as the complete project. Firmware update uses `.fwz`; Request Device Info shows hardware/software features. | O1224E_S_EN pp.4-9,43-48 |
| Ringtone authoring | Import `.mp3`, `.wav` or `.pcm`; trim to maximum `5 s`; associate to events. Ringtone and contact sections follow project-saving prerequisites. | O1224E_S_EN pp.37-44 |
| Contact fields | Apartment, entrance panel or Switchboard type; name/surname, call code, SCS address and BFA fields when selected. Add/delete/filter are software operations; no numeric contact maximum established by text. | O1224E_S_EN pp.44-48 |
| Call log | All, missed, received and sent calls; delete log; slow-flashing status LED can also signify missed calls. | O1224E_U_EN pp.28,36-38 |
| Operator controls | Separate speaker/microphone/ringtone adjustments, day/night display brightness/contrast/colour, date/time, keypad beep, information and menu language. Screenshot values do not establish defaults or full numerical domains. | O1224E_I_EN pp.22-26,46; O1224E_U_EN pp.24-25,49-53 |

### Twelve programmable function keys

| Assignable function | Documented action |
| --- | --- |
| Door lock `1..12` | Selected configured entrance-panel lock or actuator |
| IU / EP day-night toggle | Separate call-routing states for internal units and entrance panels |
| Presence / service IU toggle | Riser presence or temporary service forwarding |
| Staircase light | Staircase light activation |
| IU / EP / Switchboard call | Call selected endpoint |
| Local call / alarm siren | Toggle local call or alarm repetition |
| External call / alarm siren | Toggle remote actuator repetition |
| BFA letter | Associate a character to the block/floor/apartment call code |

All function families listed in O1224E_I_EN printed/PDF pp.36-37 and O1224E_S_EN pp.23-24 are represented here. These assignments do not add local catalogue Objects.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `74` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `115` - Management Center 2Wires

Catalogue Object key `620` maps to external Object `115`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `CDP_ADDRESS` | `0..15` | `0` | Address |
| `PE_ADDRESS` | `1..80` | `1` | External Panel Address |
| `PI_ADDRESS` | `0..3999` | `0` | Internal Panel Address |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `167` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Catalogue Object / role | Applicability | Evidence |
| --- | --- | --- |
| `115` - Management Center 2Wires | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `115` - Management Center 2Wires | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use device menus or TiSwitchboardDevice to set identity, service internal unit, contact / address book, entrance panels, day / night behavior, alarms and automation. A MASTER manages its system; backbone / riser operation requires the documented hierarchical topology and compatible entrance panels. Riser entrance panels downstream of 346851 are supported; apartment entrance panels downstream of 346850 are not managed by this switchboard. Additional 346020 supply is recommended and changes BUS draw; keep supply sizing distinct from the output relay rating. PC transfer / update uses the documented USB connection and powered switchboard. User operations include direct and address-book calls, call transfer, camera cycling, door and staircase-light control and alarm management. The 2025 software readme lists BT-346310 and Windows 10 / .NET 3.5 SP1 requirements; it does not establish support on all newer operating systems.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

English and Italian installation, software and user manuals have separate roles and are retained individually. Hierarchical support is firmware / production-scoped, while the single database Management Center Object is a capability definition. The product export’s current classifications do not remove the technical sheet’s 346890 exclusion or apartment-entrance-panel limit. Software address-book and alarm setup does not establish measured support for every optional field or external accessory.

The installation / software hierarchy paragraph prints interface `346581`, whereas the exact switchboard technical sheet and diagrams name `346851`. The transposed reference is preserved as a source discrepancy; no relationship to a separate `346581` product is inferred.

The current publisher export excludes `346891`, whereas both 2016 technical sheets exclude `346890`; both reference-specific exclusions are retained without inferring interchangeability. The export lists `18..27 V`, `5..50 mA` and “Hands free: No”; the technical sheet specifies `19..27 V` and separate supplied/unsupplied currents, while the manuals explicitly document handsfree operation. These are publisher-classification discrepancies, not grounds to discard the exact operating manuals. Its hierarchy list adds Sfera Robur and omits Minisfera from the older list; applicability must follow the named source and Firmware/production limits.

Six installer-menu change times and three software day/night bands use different units of scheduling: they can represent three paired day/night intervals, but their complete equivalence has not been tested. The installer manual describes a maximum five-digit new password while software specifies five numeric digits; leading-zero handling is uncorroborated. The user manual presents Alarm Log as backbone-only, while setup software also allows an address-zero Master to receive alarms; the corresponding non-hierarchical UI availability remains unconfirmed.

## Evidence limits and open work

Exact installed firmware, compatibility of later Sfera generations, external relay use and observed calls / alarms / diagnostics remain uncorroborated.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Discovered sources outside this review

These publisher-linked files were identified but are not used as retained evidence in this dossier. Firmware / installers and declarations remain separate evidence families. A listed URL does not establish payload identity, installed release or tested compatibility.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `Switchboard_030003.fwz` | Firmware binary: payload, production / update applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/Switchboard_030003.fwz) |
| `TiSwitchboardDevice_030015.exe` | Software installer: payload / installed compatibility unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/TiSwitchboardDevice_030015.exe) |

The retained English operating/setup/settings sections, exact technical sheets and export/readme are reconciled for this Device. Italian manuals provide parallel source roles and checked topology/alarm/relay/password boundaries; their remaining UI walk-through pages have not been independently translated line by line. Generic editing gestures, demonstration contacts and screenshot dates do not establish configuration defaults. Firmware `Switchboard_030003.fwz`, installer `TiSwitchboardDevice_030015.exe`, localization payloads and the historical catalogue parameter file remain unexamined; no relation from their filenames to Firmware `74` is inferred.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0161-0170-2026-10-07.md#own-dev-0165)
