# Sfera audio speaker module

## Summary

351100 is the Sfera audio module that handles entrance-panel calls and directly releases the associated door lock. It can serve up to 100 pushbutton calls and can be combined with the separate Night & Day camera for video.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0166` | Project identity |
| Technical description | Sfera audio speaker module | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `351100` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1459` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Video door entry system | Main system association |
| Item model / `modobj` | `34` | Main association; independent of project ID |
| Firmware definition | `111`, `635` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Audio video | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Sfera | `351100` | Established catalogue identity | Manufacturer database commercial record `1459` explicitly links this SKU to item `1459` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `351100` | `8005543441558` | `351100-publisher-product-sheet.pdf` PDF p. 1; `351100-italian-product-sheet.pdf` PDF p. 1 |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00596-c-EN.pdf` | Technical Sheet BT00596-C-EN | BT00596-c-EN; 15/05/2017 | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/f0/2d/f02d32f4a01c2fe7d2def721ddcc0f63519c52e2cf3a206d80a002e3e2fb0856.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/BT00596-c-EN.pdf) |
| `O1678E.pdf` | Instruction Use O1678E | O1678E; printed publication date not established | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/83/fe/83fe4fb03c231f18ee940a767196a052b543b7118f93300003413d3400b7cc0c.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/O1678E.pdf) |
| `RA00176AA_S_EN.pdf` | Technical Guide RA00176AA_S_EN | RA00176AA_S_EN; printed publication date not established | Earlier TiSferaDesign manual: device transfer, composition and module configuration sections reviewed against AC revision; retains historical software workflow. | [Archived original](https://archive.openwebnet-ha.org/sha256/14/14/1414875a0d40523aafb77d2f4947f60475d4dc1be6a27825883b0137b639d97f.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/RA00176AA_S_EN.pdf) |
| `351100-publisher-product-sheet.pdf` | Exact English product export | Publisher DATASHEET; 05.10.2026 | PDF pp. 1-5: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/df/ac/dfaca8b563dd70c9dee9dd7b2772ea7f8a5c76885f3914a6f3a70097b95cc02e.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-351100&include_technical=1) |
| `351100-italian-product-sheet.pdf` | Exact Italian product export | Product export retrieved 05/10/2026; boilerplate compliance dates are not product publication dates | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/84/27/84273aa0daad1830f6a2365eb5143217b64bc22456023c992c4b5ae09d99d02f.pdf) | [Publisher original](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-351100) |
| `RA00176AC_S_IT.pdf` | Manufacturer Italian / installation document | RA00176AC-03/24-PC; printed revision label | TiSferaDesign 2024: printed/PDF pp. 4-21, 22-42; device transfer, updates, speaker / keypad / reader / display settings and address-book management, scoped by module. | [Archived original](https://archive.openwebnet-ha.org/sha256/23/78/237891b468a5152361ad36fd432ebd52e8804aecbfb2373a0c953dd7cc98eb8b.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/RA00176AC_S_IT.pdf) |
| `TisferaDesign_README_v4.pdf` | Software TISFERADESIGN_README_V4 | TisferaDesign_README_v4; 14/05/2026 | PDF pp. 1-1: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/52/48/52481f4b2cb9999abf86bb870007398845f3f29a7a52fb475dbf90a880d31f65.pdf) | [Publisher original](https://assets.legrand.com/pim/AUTRE/TisferaDesign_README_v4.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1459`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `18..27 Vdc` | `BT00596-c-EN` printed/PDF pp. 1-3; `RA00176AC_S_EN` pp. 6-14 |
| Standby, backlighting off / on | `10 mA / 15 mA` | `BT00596-c-EN` printed/PDF pp. 1-3; `RA00176AC_S_EN` pp. 6-14 |
| Maximum draw | `65 mA` | `BT00596-c-EN` printed/PDF pp. 1-3; `RA00176AC_S_EN` pp. 6-14 |
| Temperature / assembled protection | `-25..70 °C; IP54 for assembled entrance panel` | `BT00596-c-EN` printed/PDF pp. 1-3; `RA00176AC_S_EN` pp. 6-14 |
| Face dimensions | `115 x 91 mm` | `BT00596-c-EN` printed/PDF pp. 1-3; `RA00176AC_S_EN` pp. 6-14 |
| Direct lock output | `18 V, 4 A impulse / 250 mA holding; maximum 30 ohm` | `BT00596-c-EN` printed/PDF pp. 1-3; `RA00176AC_S_EN` pp. 6-14 |
| Call capacity | `100 pushbutton calls` | `BT00596-c-EN` printed/PDF pp. 1-3; `RA00176AC_S_EN` pp. 6-14 |
| Local controls | `speaker/microphone level; PL door-release input; status LEDs` | `BT00596-c-EN` printed/PDF pp. 1-3; `RA00176AC_S_EN` pp. 6-14 |
| Additional supply | `1–2 input; enabled when J2 disconnected` | `BT00596-c-EN` printed/PDF pp. 1-3; `RA00176AC_S_EN` pp. 6-14 |

| Night backlighting | `Integrated optical sensor; automatic night-backlight activation` | `351100-publisher-product-sheet.pdf` p.1 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Number of call buttons | `2` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Material call buttons | `Plastic` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Material front | `Other` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Front plate height | `91 mm` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Front plate width | `115 mm` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Built-in depth | `20 mm` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Mounting method | `Surface mounted` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Installation technique | `Bus system` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Colour | `Other` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Degree of protection (IP) | `IP54` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| degree of impact strength (IK) | `IK07` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Operating / setting temperature (Min-Max) | `-15-50 °C` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Storage temperature (Min-Max) | `-20-70 °C` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Voltage type | `AC/DC` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Nominal voltage (Min-Max) | `18-240 V` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Supply current (Min-Max) | `0.04-1 A` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Frequency (Min-Max) | `50-60 Hz` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Sound level | `80 dB` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Standby consumption | `40 mA` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Cable nature for connection | `Flexible` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Cable section (Min-Max) | `1-2.5 mm²` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Label space / information surface | `Yes` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Fitted with rainproof plate protection | `Yes` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| With complemantary luminous signal | `No` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Control mode | `Wired` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Contains Batteries | `No` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Hands free | `Yes` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Loudness setting | `Yes` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Addressable | `No` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Door entry system with mobile application | `Yes` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Remote opening of gate / Electric door opener | `Yes` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Camera type | `Adjustable` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Video recorder angle | `100 °` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Max distance between internal and external unit | `150 m` | `351100-publisher-product-sheet.pdf` PDF p. 3 |
| Communication rank type | `Other` | `351100-publisher-product-sheet.pdf` PDF p. 4 |
| Connected object | `No` | `351100-publisher-product-sheet.pdf` PDF p. 4 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1459` | Canonical catalogue |
| Technical item description | Audio module | Canonical catalogue |
| Item family | Source placeholder description `0`; key `20` | Canonical catalogue |
| Main system | Video door entry system; key `4` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `34` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `111` | `1` | `1` | `4` | `1` | Catalogue default | Official |
| `635` | `1` | `2` | `25` | `1` | Not catalogue default | Official |
| `635` | `1` | `2` | `30` | `1` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `111` | `1` | `155` External unit | Fixed / designated metadata | `745` | `155` | `507` |
| `111` | `1` | `420` Call Push button | Candidate alternative | `746` | `420` | `508` |
| `111` | `1` | `426` Staircase light control | Candidate alternative | `747` | `426` | `509` |
| `111` | `1` | `465` Switchboard call push button | Candidate alternative | `748` | `497` | `510` |
| `635` | `1` | `155` External unit | Fixed / designated metadata | `2450` | `155` | `1102` |
| `635` | `1` | `420` Call Push button | Candidate alternative | `2451` | `420` | `1103` |
| `635` | `1` | `426` Staircase light control | Candidate alternative | `2452` | `426` | `1104` |
| `635` | `1` | `465` Switchboard call push button | Candidate alternative | `2453` | `497` | `1105` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `111` | `505` Internal unit virgin pushbuttons | `1` | `418`, `421`, `422`, `423`, `424`, `425`, `426`, `429` | `505` | `38` |
| `635` | `505` Internal unit virgin pushbuttons | `1` | `418`, `421`, `422`, `423`, `424`, `425`, `426`, `429` | `505` | `49` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `111` | Product Programming | `3` | Association key `4` |
| `635` | Product Programming | `3` | Association key `4` |

| Firmware | Connection label | Connection key |
| --- | --- | --- |
| `111` | USB | `3` |
| `635` | USB | `3` |

### Associated parameter definitions

| Firmware | Brand model | Line model | Registered parameter path | Scope / limit |
| --- | --- | --- | --- | --- |
| `111` | `1` | `7` | `TiSferaDesign_0102` | Parameter type `7`; payload not inspected |
| `635` | `1` | `7` | `TiSferaDesign_0300` | Parameter type `7`; payload not inspected |

Brand / line model codes in parameter associations are independent of commercial record keys. Paths are catalogue evidence; their XML payloads and wire encoding remain unexamined.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `P / N` | Entrance panel P from 0, `P=0` common / main; first called internal-unit N, normally 1 for common pushbuttons | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |
| `S=0 /1 /2 /3` | SPRINT call-frequency pairs 1200/600, 1200/0, 1200/2400, 1200 Hz; compatible later Classe handsets choose among 16 melodies; `S=9` general call in one-family system | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |
| `T=0 /1 /2 /3 /4 /5 /6 /7` | Absent=4 s; 1 s; 2 s; 3 s; while key pressed(max10 s); 6 s; 8 s; 10 s; longer timing requires 346210 `MOD=5` | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |
| `M=0 /1 /2 /3` | Call and lock tones on / lock tone off / call tone off / both tones off | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |
| `M=4 /5 /6 /7` | Same four tone combinations, with night backlighting always on | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |
| `J1 fitted / removed` | Right button column only / both columns | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |
| `J2 fitted / removed` | Auxiliary supply disabled / enabled | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |
| `Advanced P / lock timing` | `P=0..99`; lock `1..10` s or while release button held; software timing distinct from physical T map | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |
| `Software pushbutton roles` | Disabled by default; handset point / general call, stair lights or switchboard call; handset `0..3999`, switchboard `0..15` | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |
| `Transfer / update` | Powered module; remove physical configurators and J1 for advanced software transfer; front mini-USB | `BT00596-c-EN` printed/PDF pp. 2-3; `RA00176AC_S_EN` pp. 6-14 |

### Commissioning software prerequisites

These are the retained readme requirements, separate from product electrical ratings and current operating-system compatibility.

| Property | Published value | Evidence |
| --- | --- | --- |
| Windows / framework | `10 or11,64-bit;.NET4.8 or higher` | `TisferaDesign_README_v4` p.1 |
| CPU / RAM | `10th-generation i5 or equivalent;8 GB minimum,16 GB recommended` | `TisferaDesign_README_v4` p.1 |
| Disk / display | `500 MB;1366x768 minimum,1920x1080 recommended` | `TisferaDesign_README_v4` p.1 |
| Market scope | `TiSferaDesign_es_04.xx.xx for Spanish market only` | `TisferaDesign_README_v4` p.1 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `111` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `111` | `P2` | `0..9` | `0` | P2; Configurator P2 |
| `111` | `P1` | `0..6` | `0` | P1; Configurator P1 |
| `111` | `N2` | `0..39` | `0` | N2; AssInternalUnitAddrHundreds |
| `111` | `N1` | `0..99` | `0` | N1; AssInternalUnitAddrUnits |
| `111` | `S` | `0..4` | `0` | S; Configurator S (0-4) |
| `111` | `T` | `0..7` | `0` | T; Configurator T (time) - (0-7) |
| `111` | `M` | `0..7` | `0` | M; Mode 0-7 |
| `635` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `635` | `P2` | `0..9` | `0` | P2; Configurator P2 |
| `635` | `P1` | `0..6` | `0` | P1; Configurator P1 |
| `635` | `N2` | `0..39` | `0` | N2; AssInternalUnitAddrHundreds |
| `635` | `N1` | `0..99` | `0` | N1; AssInternalUnitAddrUnits |
| `635` | `S` | `0..4` | `0` | S; Configurator S (0-4) |
| `635` | `T` | `0..7` | `0` | T; Configurator T (time) - (0-7) |
| `635` | `M` | `0..7` | `0` | M; Mode 0-7 |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `155` - External unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | Address |
| `N` | `0..99` | `0` | Associated Internal Unit address - units |
| `M` | `0..39` | `0` | Associated Internal Unit address - hundreds |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `RING_T_OUT` | `1..3` | `10` | RingTIMEOUT |
| `CALL_T_OUT` | `10..180` | `30` | Call timeout |
| `CONN_T_OUT` | `3..90` | `6` | ConnectionTimeOut |
| `ASS_SWITCH` | `0..95` | `0` | AssociatedSwitchboard |
| `ASSOCIATEDSWITCHBOARDADDRESSBOOK` | `0..15` | `0` | Switchboard associated to the device for the Video door-entry address book |
| `BEEP_LOCK` | `0` = Disable; `1` = Enable | `1` | Beep on lock |
| `BEEP_BUTT` | `0` = Disable; `1` = Enable | `1` | Beep on push button |
| `BEEP_SES` | `0` = Disable; `1` = Enable | `1` | Beep on session change |
| `NEXT_PE` | `0..95` | `0` | NextExtUnitInSliding |
| `CAM` | `0..96` | `96` | AssociatedCamera |
| `SPEECH_SYNT` | `0` = Disable; `1` = Enable | `0` | Speech sintesys |
| `IS_VIDEO` | `0` = Undefined; `1` = Video; `2` = Audio | `0` | IS_VIDEO |

### Object `420` - Call Push button

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..99` | `0` | Associated Internal Unit address - units |
| `N2` | `0..39` | `0` | Associated Internal Unit address - hundreds |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `RING_TONE` | `0..3` | `0` | RingToneRequired |

### Object `426` - Staircase light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `465` - Switchboard call push button

Catalogue Object key `497` maps to external Object `465`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `CDP_ADDRESS` | `0..15` | `0` | Address |
| `RING_TONE` | `0..3` | `0` | RingToneRequired |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `111` | `155` | `726` | `TO_ALL` | `0` = Point to point; `1` = General (entire reusable range retained) | `1` | Type of call |
| `111` | `420` | `727` | `TO_ALL` | `0` = Point to point; `1` = General (entire reusable range retained) | `1` | Type of call |
| `111` | `426` | `4103` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `635` | `155` | `1841` | `TO_ALL` | `0` = Point to point; `1` = General (entire reusable range retained) | `1` | Type of call |
| `635` | `420` | `1842` | `TO_ALL` | `0` = Point to point; `1` = General (entire reusable range retained) | `1` | Type of call |
| `635` | `426` | `4112` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `34` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `155` - External unit | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `420` - Call Push button | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `426` - Staircase light control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `465` - Switchboard call push button | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `155` - External unit | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `420` - Call Push button | No stored Object-system association | Not applicable | Absence of this relation does not remove the explicit Firmware/Object association |
| `426` - Staircase light control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `426` - Staircase light control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `426` - Staircase light control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `426` - Staircase light control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `465` - Switchboard call push button | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Physical P numbers entrance panels from 0, with `P=0` reserved for the common / main panel. N assigns the first called internal unit; common pushbutton panels use `N=1`. S sets handset ringtone behavior and `S=9` gives the general call in one-family systems. T sets lock timing; M sets tone suppression and always-on backlighting. J1 connected enables the right button column; disconnected enables both columns. J2 disconnected enables additional supply. Advanced TiSferaDesign transfer requires removal of J1 and physical configurators, with the module powered. The 2024 software manual allows `P=0..99`, individual / general calls, stair-light and switchboard functions, handset `0..3999` and switchboard `0..15` destinations. These are software domains; apply the exact firmware filters below. The front mini-USB also supports firmware updates. Hierarchical 346310 operation is documented from firmware 01.02.31.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact sheet and exports establish this assembly independently of other Sfera speaker / camera products. Covers, assembled IP protection and impact ratings depend on the selected Sfera New/Robur front plate; a cover rating does not rate the uncovered electronics. Database External unit and pushbutton Objects are conditional configuration roles, not additional physical call keys. AA and AC TiSferaDesign manuals are retained as distinct revisions; the 2026 V4 readme requires 64-bit Windows 10/11 and .NET 4.8, not the older software prerequisite set. The audio module supports the separate 352400 camera, but does not contain a camera. The English sheet allows 100 pushbutton calls; the A/V sheets state 98 for their own assemblies.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `BT00596-c-EN.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |
| `O1678E.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |
| `RA00176AA_S_EN.pdf` | Earlier TiSferaDesign manual: device transfer, composition and module configuration sections reviewed against AC revision; retains historical software workflow. |
| `351100-publisher-product-sheet.pdf` | PDF pp. 1-5: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |
| `351100-italian-product-sheet.pdf` | PDF pp. 1-2: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |
| `RA00176AC_S_IT.pdf` | TiSferaDesign 2024: printed/PDF pp. 4-21, 22-42; device transfer, updates, speaker / keypad / reader / display settings and address-book management, scoped by module. |
| `TisferaDesign_README_v4.pdf` | PDF pp. 1-1: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. |

The exact restriction table identifies reusable defaults outside a Firmware/Object subset. These are catalogue conflicts; no replacement default is inferred.

## Evidence limits and open work

The production / firmware boundary for current exports, full assembled-panel electrical budget and measured call, lock and diagnostic behavior remain open.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Discovered sources outside this review

These publisher-linked files were identified but are not used as retained evidence in this dossier. Firmware / installers and declarations remain separate evidence families. A listed URL does not establish payload identity, installed release or tested compatibility.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `LGRP-01109-V01.01-EN.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/LGRP-01109-V01.01-EN.pdf) |
| `LGRP-2015-159-V1-EN.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/LGRP-2015-159-V1-EN.pdf) |
| `Sfera.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Sfera.pdf) |
| `Sfera_2011A_010234.fwz` | Firmware binary: payload, production / update applicability unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/Sfera_2011A_010234.fwz) |
| `TiSferaDesign_040024.exe` | Software installer: payload / installed compatibility unexamined | [Publisher listing](https://assets.legrand.com/pim/AUTRE/TiSferaDesign_040024.exe) |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)
