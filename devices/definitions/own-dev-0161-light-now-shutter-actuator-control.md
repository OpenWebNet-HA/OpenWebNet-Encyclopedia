# Light NOW shutter actuator and control

## Summary

This shutter actuator and control, marketed as Light NOW or Céliane MyHOME, combines a shutter motor actuator with a local control and can also command a remote actuator. The documented Y4672M2S variant supports up / down operation and a stored preset position. Its detachable control and actuator parts are joined through the connector shown in the installation sheet.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0161` | Project identity |
| Technical description | Light NOW shutter actuator and control | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `MX5220`, `Y4672M2S` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `2310` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `144` | Main association; independent of project ID |
| Firmware definition | `870` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `6` | Firmware metadata |
| Categories | Actuators, User interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand - Céliane | `MX5220` | Established catalogue identity | Manufacturer database commercial record `2666` explicitly links this SKU to item `2310` |
| BTicino - Light NOW | `Y4672M2S` | Established catalogue identity | Manufacturer database commercial record `2665` explicitly links this SKU to item `2310` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `Y4672M2S` | `8005543762295` | [Retained Y4672M2S export](https://archive.openwebnet-ha.org/sha256/72/3c/723c29312a905e9179b26c8a4edde561f49a0a1a78260c447fe3b867e034645f.pdf), PDF p.1 |
| `MX5220` | `3414972808781` | [Retained MX5220 manufacturer record](https://archive.openwebnet-ha.org/sha256/97/7b/977b6da48095c8ed427f559ecbaeec83eb3acab4f71844838826937a960430ab.pdf), EAN/Gencode field |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `Y4672M2S` | Acutator/Command Shutter Light Now | Canonical commercial record `2665` |
| `MX5220` | Acutator/Command Shutter Light Now | Canonical commercial record `2666` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `LE14827AA.pdf` | Instruction Use LE14827AA | LE14827AA; 07/24-02 PC | PDF pp. 1-4: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/27/1f/271f1d6f9656bde96bc80ee6e3717e54248bb9c8446940e9f6aded656fc371a2.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/LE14827AA.pdf) |
| `Y4672M2S-publisher-product-sheet.pdf` | Exact English product export | Publisher DATASHEET; 05.10.2026 | PDF pp. 1-5: exact-reference specifications, configuration or wiring. Printed pagination coincides where numbered; product exports use PDF pages. | [Archived original](https://archive.openwebnet-ha.org/sha256/72/3c/723c29312a905e9179b26c8a4edde561f49a0a1a78260c447fe3b867e034645f.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-Y4672M2S&include_technical=1) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `2310`: complete extracted catalogue associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `LE14826AC.pdf` | Exact MX5220 multilingual installation notice | LE14826AC; 05/26-01 PC | Printed/PDF pp.1-2 mounting variants; p.3 indication and adjustment controls; p.4 wiring, SCS supply and shutter-specific motor column. MX5230 lighting and MX5220C packaging references are separate scopes. | [Archived original](https://archive.openwebnet-ha.org/sha256/78/ca/78ca31a67be1a93dc933574dd7d0cf30ddff259881e23c050fe49e3d565c5660.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/LE14826AC.pdf) |
| `MX5220-ean-publisher-page.html` | Exact French publisher product record | Retrieved 7 October 2026; live publisher record, no printed revision | MX5220 Céliane identity, EAN, shutter capabilities, dimensions, classification attributes and linked installation original. | [Archived original](https://archive.openwebnet-ha.org/sha256/97/7b/977b6da48095c8ed427f559ecbaeec83eb3acab4f71844838826937a960430ab.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/actionneur-bus-celiane-myhome-avec-commande-integree-pour-volet-roulant-460w-230v-2-modules) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Y4672M2S SCS supply | `18..27 Vdc in installation sheet; 27 Vdc nominal in export` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| Y4672M2S current draw at maximum LED intensity | `9 mA standby; 17 mA maximum shutter operation` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| Y4672M2S motor load | `460 W at 230 Vac; 250 W at 110 Vac` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| Y4672M2S operating temperature | `0..40 °C in installation sheet; export says -5..36 °C` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| Load supply / terminals | `110..230 Vac, 50/60 Hz; printed terminal capacity 2 x 1.5 m² or 1 x 2.5 m² has unit typo; unit is not silently corrected` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| Y4672M2S motor contact marking | `2 A; 110..230 Vac on installation marking; export description says 250 Vac relay` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| Y4672M2S dimensions | `45 x 45 x 40 mm; minimum box depth 43 mm; 2 wiring-device modules` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| Control configurators | `A1, PL1, M1, A2, PL2, M2` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| Local indication | `steady blue load ON; steady white load OFF; flashing blue Object not configured` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| LED brightness cycle | `60% default; 30%; 0%; 100%; hold LED pushbutton more than 2 s` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |
| Circuit protection | `10 A thermal magnetic circuit breaker in wiring diagram` | `LE14827AA` PDF pp. 1-4; `Y4672M2S-publisher-product-sheet` PDF pp. 1-5 |

| Completion / packaging | `1- or2-module key covers,support frames and plates; publisher says plastic-free paper packaging` | `Y4672M2S-publisher-product-sheet.pdf` pp. 1-2 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. Frequency classifications and a negative connected-object classification do not establish the runtime transport or exclude control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system KNX-RF (Radio Frequency) | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system KNX Secure | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system KNX Secure-RF (Radio Frequency) | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system radio frequency | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system LON | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus system Powernet | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Other bus systems | `Other` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Radio frequency bidirectional | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Number of linkable devices | `1` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Mounting method | `Flush-mounted` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Width in number of modular spacings | `2` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Local operation / hand operation | `Yes` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| With LED indication | `Yes` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Number of digital inputs | `3` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Suitable for C-load | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Max. number of switching contacts | `2` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Max. switching current | `2 A` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Rated operating voltage (Min- Max) | `110-230 V` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Different phases connectable | `Yes` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| With bus connection | `Yes` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Bus module detachable | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Min. depth of built-in installation box | `43 mm` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Modular expandability | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Degree of protection (IP) | `IP20` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Width | `45 mm` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Height | `45 mm` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Depth | `40 mm` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| degree of impact strength (IK) | `IK04` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Operating / setting temperature (Min-Max) | `-5-36 °C` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Storage temperature (Min-Max) | `-10-71 °C` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Voltage type | `AC` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Terminal marking indication | `Yes` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Type of load | `Universal and LED Retrofit` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 3 |
| Connection type | `Screwed terminal` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Number of distribution blocks | `4` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Terminals capacity (Min-Max) | `0.34-2.5 mm²` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Connection type | `Not applicable` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Label space / information surface | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Fitted with USB plug | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Addressable | `Yes` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Connected object | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| With voice command | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Programmable | `Yes` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Interoperable connection Protocol | `Yes` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Connectable by Internet box | `No` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |
| Product use function | `Lighting management` | `Y4672M2S-publisher-product-sheet.pdf` PDF p. 4 |

| Property | MX5220 value | Evidence |
| --- | --- | --- |
| SCS supply / motor load | `18..27 Vdc`; `460 W at 230 Vac`, `250 W at 110 Vac` | LE14826AC printed/PDF p.4; exact shutter column |
| Notice current at maximum LED intensity | `9 mA` standby; `17 mA` shutter operation | LE14826AC printed/PDF p.4; `26 mA` concerns two lights on MX5230 |
| Operating supply / temperature | `110..230 Vac`, `50/60 Hz`; `0..40 °C` | LE14826AC printed/PDF p.4 |
| Dimensions / built-in depth | `45 x 45 x 39.9 mm`; `33 mm` built-in depth | [Retained MX5220 manufacturer record](https://archive.openwebnet-ha.org/sha256/97/7b/977b6da48095c8ed427f559ecbaeec83eb3acab4f71844838826937a960430ab.pdf) |
| Protection / publisher standby | `IP20`; `7 mA` standby; LED-intensity context unstated | [Retained MX5220 manufacturer record](https://archive.openwebnet-ha.org/sha256/97/7b/977b6da48095c8ed427f559ecbaeec83eb3acab4f71844838826937a960430ab.pdf) |
| Assembly accessories | Cover, ring, support and finish plate; Céliane and Arteor/Seano drawings are distinct mounting examples | LE14826AC pp.1-2; [Retained MX5220 manufacturer record](https://archive.openwebnet-ha.org/sha256/97/7b/977b6da48095c8ed427f559ecbaeec83eb3acab4f71844838826937a960430ab.pdf) |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2310` | Canonical catalogue |
| Technical item description | Acutator/Command Shutter Light Now | Canonical catalogue |
| Item family | Source placeholder description `0`; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `144` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `144` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `870` | `1` | `0` | `0` | `6` | Not catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `870` | `1` | `218` Shutter actuator | Fixed / designated metadata | `4378` | `514` | `1970` |
| `870` | `2` | `410` Light control | Fixed / designated metadata | `4374` | `410` | `1969` |
| `870` | `2` | `411` Automation control | Candidate alternative | `3844` | `411` | `1826` |
| `870` | `2` | `412` Lock / unlock actuator control | Candidate alternative | `3848` | `412` | `1827` |
| `870` | `2` | `416` Scheduled scenario PLUS | Candidate alternative | `3852` | `416` | `1828` |
| `870` | `2` | `418` Open lock control | Candidate alternative | `3860` | `418` | `1830` |
| `870` | `2` | `426` Staircase light control | Candidate alternative | `3864` | `426` | `1831` |
| `870` | `2` | `427` Floor call control | Candidate alternative | `3868` | `427` | `1832` |
| `870` | `2` | `463` Load control actuator visualization | Candidate alternative | `3876` | `492` | `1834` |
| `870` | `3` | `410` Light control | Fixed / designated metadata | `4375` | `410` | `1969` |
| `870` | `3` | `411` Automation control | Candidate alternative | `3845` | `411` | `1826` |
| `870` | `3` | `412` Lock / unlock actuator control | Candidate alternative | `3849` | `412` | `1827` |
| `870` | `3` | `416` Scheduled scenario PLUS | Candidate alternative | `3853` | `416` | `1828` |
| `870` | `3` | `418` Open lock control | Candidate alternative | `3861` | `418` | `1830` |
| `870` | `3` | `426` Staircase light control | Candidate alternative | `3865` | `426` | `1831` |
| `870` | `3` | `427` Floor call control | Candidate alternative | `3869` | `427` | `1832` |
| `870` | `3` | `463` Load control actuator visualization | Candidate alternative | `3877` | `492` | `1834` |
| `870` | `3` | `174` Shutter control (3 slots) | Candidate alternative | `3839` | `665` | `1824` |
| `870` | `4` | `410` Light control | Fixed / designated metadata | `4376` | `410` | `1969` |
| `870` | `4` | `411` Automation control | Candidate alternative | `3846` | `411` | `1826` |
| `870` | `4` | `412` Lock / unlock actuator control | Candidate alternative | `3850` | `412` | `1827` |
| `870` | `4` | `416` Scheduled scenario PLUS | Candidate alternative | `3854` | `416` | `1828` |
| `870` | `4` | `418` Open lock control | Candidate alternative | `3862` | `418` | `1830` |
| `870` | `4` | `426` Staircase light control | Candidate alternative | `3866` | `426` | `1831` |
| `870` | `4` | `427` Floor call control | Candidate alternative | `3870` | `427` | `1832` |
| `870` | `4` | `463` Load control actuator visualization | Candidate alternative | `3878` | `492` | `1834` |
| `870` | `5` | `410` Light control | Fixed / designated metadata | `4377` | `410` | `1969` |
| `870` | `5` | `411` Automation control | Candidate alternative | `3847` | `411` | `1826` |
| `870` | `5` | `412` Lock / unlock actuator control | Candidate alternative | `3851` | `412` | `1827` |
| `870` | `5` | `416` Scheduled scenario PLUS | Candidate alternative | `3855` | `416` | `1828` |
| `870` | `5` | `418` Open lock control | Candidate alternative | `3863` | `418` | `1830` |
| `870` | `5` | `426` Staircase light control | Candidate alternative | `3867` | `426` | `1831` |
| `870` | `5` | `427` Floor call control | Candidate alternative | `3871` | `427` | `1832` |
| `870` | `5` | `463` Load control actuator visualization | Candidate alternative | `3879` | `492` | `1834` |
| `870` | `6` | `143` User interface settings for command | Fixed / designated metadata | `4373` | `644` | `1968` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `870` | `521` Soft-Touch command virgin | `2`, `3`, `4`, `5` | `410`, `411`, `412`, `413`, `414`, `415`, `416`, `417`, `418`, `419`, `421`, `426`, `427`, `462` | `521` | `156` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `870` | Physical configuration | `0` | Canonical firmware/mode association |
| `870` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `870` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating settings

Published product selectors and software settings are separate from catalogue mode IDs. Their domains, defaults and topology limits do not replace Firmware-specific filters.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `A1/PL1/M1; A2/PL2/M2` | Separate configuration sockets shown on control; full selector mode matrix deferred by original to application documentation | `LE14827AA` PDF pp. 1, 3-4 |
| `Blue steady / white steady / blue flashing` | Load on / load off / Object unconfigured; indication is published, not captured feedback | `LE14827AA` PDF pp. 1, 3-4 |
| `Brightness hold >2 s` | 60% default →30%→0%→100% | `LE14827AA` PDF pp. 1, 3-4 |
| `App prerequisites, July 2024 sheet` | Android ≥5.0 with Google Play; iPhone iOS ≥12.0; these are sheet prerequisites, not current app-store compatibility | `LE14827AA` PDF pp. 1, 3-4 |

| MX5220 control / indication | Published setting | Evidence |
| --- | --- | --- |
| LED indication | Magenta steady = load ON; blue steady = load OFF; flashing magenta = Object unconfigured | LE14826AC printed/PDF p.3 |
| LED intensity button | Hold `>5 s` for shutter brightness; `60%` default → `30%` → `0%` → `100%`. The `>2 s` instruction is for MX5230 lights. | LE14826AC printed/PDF p.3 |
| Shutter adjustment button | Hold `>3 s`; notice directs detailed adjustment to online catalogue. This alone does not specify the full calibration sequence. | LE14826AC printed/PDF p.3 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `870` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `870` | `A1` | `0..9` | `0` | Configurator A1 (0-9) |
| `870` | `PL1` | `0..9` | `0` | PL1 - (0-9) |
| `870` | `M1` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `14` = `CEN`; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`, SU_GIU, SU_GIU_M,`CEN`,`PUL`) |
| `870` | `A2` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | Automation A addressing space (for configurator A2) |
| `870` | `PL2` | `0..9` | `0` | PL2 - (0-9) |
| `870` | `M2` | `0..8`; `9` = `O/I`; `10` = `OFF`; `11` = `ON`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable; `15` = `PUL` | `0` | Modality; Mode physical configurator (0-8, `O/I`,`OFF`,`ON`, SU_GIU, SU_GIU_M,`CEN`,`PUL`) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `410` - Light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Toggle; `1` = Timed `ON`; `2` = Toggle dimmer; `4` = Toggle `ON`/`OFF`; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `20` = `ON` and point to point dimmer; `21` = `OFF` and point to point dimmer; `22` = `ON` and Dimmer; `23` = `OFF` and Dimmer; `32` = Blinking 0.5 s; `33` = Blinking 1 s; `34` = Blinking 1.5 s; `35` = Blinking 2 s; `36` = Blinking 2.5 s; `37` = Blinking 3 s; `38` = Blinking 3.5 s; `39` = Blinking 4 s; `40` = Blinking 4.5 s; `41` = Blinking 5 s; `42` = Blinking 5.5 s; `43` = Blinking 6 s; `44` = Blinking 6.5 s; `45` = Blinking 7 s; `46` = Blinking 7.5 s; `47` = Blinking 8 s; `49` = `ON` dimmer 10%; `50` = `ON` dimmer 20%; `51` = `ON` dimmer 30%; `52` = `ON` dimmer 40%; `53` = `ON` dimmer 50%; `54` = `ON` dimmer 60%; `55` = `ON` dimmer 70%; `56` = `ON` dimmer 80%; `57` = `ON` dimmer 90%; `128` = Customized timed `ON`; `129` = Customized toggle and point to point dimmer; `131` = Customized toggle dimmer; `133` = Customized toggle dimmer without regulation; `135` = Customized `ON` and dimmer without regulation; `136` = Customized `OFF` and dimmer without regulation; `137` = Customized `ON` and dimmer with regulation; `138` = Customized `OFF` and dimmer with regulation | `0` | Modality; Mode (MODE+`ON`/`OFF`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `HOURS` | `0..255` | `0` | Hours; Only for `MOD=128` |
| `MINUTES` | `0..59` | `0` | Minutes; Only for `MOD=128` |
| `SECONDS` | `0..59` | `30` | Seconds; Only for `MOD=128` |
| `LEVEL` | `0..100` | `100` | Level; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `START_S` | `0..255` | `255` | Soft start speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `STOP_S` | `0..255` | `255` | Soft stop speed; Only for `MOD=129`, 131, 133, 135, 136, 137, 138 |
| `DIMMING_S` | `0..255` | `255` | Dimming speed; Only for `MOD=129`, 131 |
| `T_TIME` | `1` = 1 min; `2` = 2 min; `3` = 3 min; `4` = 4 min; `5` = 5 min; `6` = 15 min; `7` = 30 s; `8` = 0.5 s; `9` = 2 s; `10` = 10 min | `1` | Tabled time; Only for `MOD=1` |

### Object `411` - Automation control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = UP bistable control; `1` = DOWN bistable control; `2` = UP monostable control; `3` = DOWN monostable control; `4` = UP monostable and bistable control; `5` = DOWN monostable and bistable control | `0` | Modality; mode (`UP/DOWN`) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `A_R` | `0..10` | `0` | Area of reference actuator; 0= no referent |
| `PL_R` | `0..15` | `0` | Light point of reference actuator; 0= no referent |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `412` - Lock / unlock actuator control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Disable; `2` = Enable | `1` | Modality; mode (D/E) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; Address  Area  Group  |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `G` | `1..255` | `1` | Group |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = All systems | `0` | Destination level |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `416` - Scheduled scenario PLUS

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PPT_CEN_LOW` | `0..255` | `1` | Scheduled scenario PLUS number |
| `PPT_CEN_HIG` | `0..7` | `0` | Scheduled scenario PLUS number |
| `BUTTON_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press / release only; `1` = Press / hold / release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `418` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |

### Object `426` - Staircase light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `427` - Floor call control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `TO_ALL` | `0` = Point to point; `1` = General | `1` | Type of call |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEGMENT` | `0` = The same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |
| `IN_AUX_CHANNEL` | `0..15` | `0` | Input `AUX` channel |

### Object `463` - Load control actuator visualization

Catalogue Object key `492` maps to external Object `463`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `PRIORITY` | `0..63` | `1` | Priority |
| `PHASE` | `0` = Single phase; `1` = Phase 1; `2` = Phase 2; `3` = Phase 3 | `0` | Phase |

### Object `218` - Shutter actuator

Catalogue Object key `514` maps to external Object `218`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master standard mode; `11` = Slave standard mode; `15` = `PUL` mode master; `16` = `PUL` mode slave | `0` | Modality; Mode shutter actuator |
| `SHUTTER_TYPE` | `0` = Standard automatic without slats; `1` = Standard without slats; `2` = Pulse without slats; `3` = Standard with slats | `0` | Motor type; Shutter type |
| `STOP_PULSE_DURATION` | `1` = 0.1 s; `2` = 0.2 s; `3` = 0.3 s; `4` = 0.4 s; `5` = 0.5 s; `6` = 0.6 s; `7` = 0.7 s; `8` = 0.8 s; `9` = 0.9 s; `10` = 1 s; `11` = 1.1 s; `12` = 1.2 s; `13` = 1.3 s; `14` = 1.4 s; `15` = 1.5 s; `16` = 1.6 s; `17` = 1.7 s; `18` = 1.8 s; `19` = 1.9 s; `20` = 2 s; `21` = 2.1 s; `22` = 2.2 s; `23` = 2.3 s; `24` = 2.4 s; `25` = 2.5 s; `26` = 2.6 s; `27` = 2.7 s; `28` = 2.8 s; `29` = 2.9 s; `30` = 3 s; `31` = 3.1 s; `32` = 3.2 s; `33` = 3.3 s; `34` = 3.4 s; `35` = 3.5 s; `36` = 3.6 s; `37` = 3.7 s; `38` = 3.8 s; `39` = 3.9 s; `40` = 4 s; `41` = 4.1 s; `42` = 4.2 s; `43` = 4.3 s; `44` = 4.4 s; `45` = 4.5 s; `46` = 4.6 s; `47` = 4.7 s; `48` = 4.8 s; `49` = 4.9 s; `50` = 5 s; `51` = 5.1 s; `52` = 5.2 s; `53` = 5.3 s; `54` = 5.4 s; `55` = 5.5 s; `56` = 5.6 s; `57` = 5.7 s; `58` = 5.8 s; `59` = 5.9 s; `60` = 6 s; `61` = 6.1 s; `62` = 6.2 s; `63` = 6.3 s; `64` = 6.4 s; `65` = 6.5 s; `66` = 6.6 s; `67` = 6.7 s; `68` = 6.8 s; `69` = 6.9 s; `70` = 7 s; `71` = 7.1 s; `72` = 7.2 s; `73` = 7.3 s; `74` = 7.4 s; `75` = 7.5 s; `76` = 7.6 s; `77` = 7.7 s; `78` = 7.8 s; `79` = 7.9 s; `80` = 8 s; `81` = 8.1 s; `82` = 8.2 s; `83` = 8.3 s; `84` = 8.4 s; `85` = 8.5 s; `86` = 8.6 s; `87` = 8.7 s; `88` = 8.8 s; `89` = 8.9 s; `90` = 9 s; `91` = 9.1 s; `92` = 9.2 s; `93` = 9.3 s; `94` = 9.4 s; `95` = 9.5 s; `96` = 9.6 s; `97` = 9.7 s; `98` = 9.8 s; `99` = 9.9 s; `100` = 10 s | `1` | Stop pulse duration; Duration pulse of stop |
| `UP_OR_DOWN_PULSE_DURATION` | `1` = 0.1 s; `2` = 0.2 s; `3` = 0.3 s; `4` = 0.4 s; `5` = 0.5 s; `6` = 0.6 s; `7` = 0.7 s; `8` = 0.8 s; `9` = 0.9 s; `10` = 1 s; `11` = 1.1 s; `12` = 1.2 s; `13` = 1.3 s; `14` = 1.4 s; `15` = 1.5 s; `16` = 1.6 s; `17` = 1.7 s; `18` = 1.8 s; `19` = 1.9 s; `20` = 2 s; `21` = 2.1 s; `22` = 2.2 s; `23` = 2.3 s; `24` = 2.4 s; `25` = 2.5 s; `26` = 2.6 s; `27` = 2.7 s; `28` = 2.8 s; `29` = 2.9 s; `30` = 3 s; `31` = 3.1 s; `32` = 3.2 s; `33` = 3.3 s; `34` = 3.4 s; `35` = 3.5 s; `36` = 3.6 s; `37` = 3.7 s; `38` = 3.8 s; `39` = 3.9 s; `40` = 4 s; `41` = 4.1 s; `42` = 4.2 s; `43` = 4.3 s; `44` = 4.4 s; `45` = 4.5 s; `46` = 4.6 s; `47` = 4.7 s; `48` = 4.8 s; `49` = 4.9 s; `50` = 5 s; `51` = 5.1 s; `52` = 5.2 s; `53` = 5.3 s; `54` = 5.4 s; `55` = 5.5 s; `56` = 5.6 s; `57` = 5.7 s; `58` = 5.8 s; `59` = 5.9 s; `60` = 6 s; `61` = 6.1 s; `62` = 6.2 s; `63` = 6.3 s; `64` = 6.4 s; `65` = 6.5 s; `66` = 6.6 s; `67` = 6.7 s; `68` = 6.8 s; `69` = 6.9 s; `70` = 7 s; `71` = 7.1 s; `72` = 7.2 s; `73` = 7.3 s; `74` = 7.4 s; `75` = 7.5 s; `76` = 7.6 s; `77` = 7.7 s; `78` = 7.8 s; `79` = 7.9 s; `80` = 8 s; `81` = 8.1 s; `82` = 8.2 s; `83` = 8.3 s; `84` = 8.4 s; `85` = 8.5 s; `86` = 8.6 s; `87` = 8.7 s; `88` = 8.8 s; `89` = 8.9 s; `90` = 9 s; `91` = 9.1 s; `92` = 9.2 s; `93` = 9.3 s; `94` = 9.4 s; `95` = 9.5 s; `96` = 9.6 s; `97` = 9.7 s; `98` = 9.8 s; `99` = 9.9 s; `100` = 10 s | `1` | UP or DOWN pulse duration; Pulse duration of UP or Down |
| `TILTING` | `1..100` | `70` | Tilting to rolling switch pulse duration; Only for pulse mode. |
| `ROLLING` | `1..100` | `70` | Rolling to tilting switch pulse duration; Only for pulse mode. |
| `LOCAL_BUTTON` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and Bistable; `3` = Bistable and blades control | `0` | Modality; Local button mode for Shutter managemant 4661M2 |
| `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety | `1` | Priority; Shutter management command priority |
| `PRESET_NUMBER` | `1..10`; `0` = None | `0` | Preset; Shutter management preset number |
| `P1` | `0..100` | `10` | Preset of position P1 |
| `P2` | `0..100` | `20` | Preset of position P2 |
| `P3` | `0..100` | `30` | Preset of position P3 |
| `P4` | `0..100` | `40` | Preset of position P4 |
| `P5` | `0..100` | `50` | Preset of position P5 |
| `P6` | `0..100` | `60` | Preset of position P6 |
| `P7` | `0..100` | `70` | Preset of position P7 |
| `P8` | `0..100` | `80` | Preset of position P8 |
| `P9` | `0..100` | `90` | Preset of position P9 |
| `P10` | `0..100` | `100` | Preset of position P10 |
| `UP_SHUTTER_TIME_MINUTES` | `0..9` | `0` | UP shutter calbration time (m) |
| `UP_SHUTTER_TIME_SECONDS` | `0..59` | `0` | UP shutter calbration time (s) |
| `DOWN_SHUTTER_TIME_MINUTES` | `0..9` | `0` | DOWN shutter calbration time (m) |
| `DOWN_SHUTTER_TIME_SECONDS` | `0..59` | `0` | DOWN shutter calbration time (s) |
| `SLATS_ROTATION_TIME_DOWN_H` | `0..27` | `0` | SLATS ROTATION calibration time when shutter is all the way down - HIGH BYTE (ms) |
| `SLATS_ROTATION_TIME_DOWN_L` | `0..255` | `0` | SLATS ROTATION calibration time when shutter is all the way down - LOW BYTE (ms) |
| `SLATS_ROTATION_TIME_MIDDLE_H` | `0..27` | `0` | SLATS ROTATION calibration time when shutter is in middle position - HIGH BYTE (ms); If not intentionally modified, par 0x20 = par 30 |
| `SLATS_ROTATION_TIME_MIDDLE_L` | `0..255` | `0` | SLATS ROTATION calibration time when shutter is in middle position - LOW BYTE (ms); If not intentionally modified, par 0x21 = par 31 |
| `SLATS_ROTATION_STEP_NUMBER` | `3..100` | `4` | SLATS ROTATION step number |
| `G1` | `0..255` | `0` | Group 1; Group = 0 means no group |
| `G2` | `0..255` | `0` | Group 2; Group = 0 means no group |
| `G3` | `0..255` | `0` | Group 3; Group = 0 means no group |
| `G4` | `0..255` | `0` | Group 4; Group = 0 means no group |
| `G5` | `0..255` | `0` | Group 5; Group = 0 means no group |
| `G6` | `0..255` | `0` | Group 6; Group = 0 means no group |
| `G7` | `0..255` | `0` | Group 7; Group = 0 means no group |
| `G8` | `0..255` | `0` | Group 8; Group = 0 means no group |
| `G9` | `0..255` | `0` | Group 9; Group = 0 means no group |
| `G10` | `0..255` | `0` | Group 10; Group = 0 means no group |

### Object `143` - User interface settings for command

Catalogue Object key `644` maps to external Object `143`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LED_LEVEL_COMMANDS` | `0` = `OFF`; `1` = Minimum level; `2` = Medium level; `3` = Maximum level | `2` | LED intensity level |
| `ENABLE_DISABLE_LED_COMMAND` | `0` = All Led Enabled; `1` = Presence Led Enabled - State Update Led Disable; `2` = Presence Led Disable - State Update Led Enable; `3` = All Led Disable | `0` | Enable-Disable LED |
| `PRESENCE_LED_INTENSITY_LEVEL_COMMAND` | `0` = Standard level; `1` = High intensity level | `0` | Presence LED intensity level |

### Object `174` - Shutter control (3 slots)

Catalogue Object key `665` maps to external Object `174`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and bistable; `3` = Bistable and blades control | `0` | Modality; Mode (0, 1, 2, 3) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; See Automation System Addressing |
| `A` | `0..10` | `0` | Area; See Automation System Addressing |
| `PL` | `0..15` | `0` | Light point; See Automation System Addressing |
| `G1` | `1..255` | `1` | Group 1; See Automation System Addressing |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level; See Automation System Addressing |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems | `0` | Destination level; See Automation System Addressing |
| `A_R` | `0..10` | `0` | Area of reference actuator |
| `PL_R` | `0..15` | `0` | Light point of reference actuator |
| `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety | `1` | Priority; Shutter management command priority |
| `PRE` | `1..9`; `0` = None | `0` | Preset; Shutter management preset number |

### Object `413` - Scenario module control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Scenario activation and modification; `1` = Scenario activation | `0` | Modality |
| `APL` | `0..175`; encoded by `APL=16*A+PL`, with `A=0..10` and `PL=0..15` | `0` | Scenario module address |
| `INST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15; `16` = Standard | `16` | Installation level |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `14` = Local bus 14; `15` = Local bus 15 | `0` | Destination level; Destination level (`0..15`) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `SCE_BUTT_1` | `1..16` | `1` | Scenario number |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay of scenario number |

### Object `414` - Scheduled scenario (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `CEN_BUTT_1` | `0..31` | `1` | Button |
| `MODE` | `0` = Press/release only; `1` = Press/hold/release | `0` | Modality; Mode (Lighting management) |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |

### Object `415` - Scenario PLUS Lighting Management (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`; `1` = `OFF`; `2` = `ON` with regulation; `3` = `OFF` with regulation | `0` | Modality; Mode (ON/OFF regulation) |
| `PPT_SCE_1` | `0..255` | `1` | Upper button scenario |
| `TYPE_OF_REGULATION` | `0` = Regulate all; `1` = Lights only; `2` = Shutters only; `3` = Stereo amplifiers only | `0` | Regulation type |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `DEL_BUTTON_1` | `0` = None; `1` = 1 s; `2` = 2 s; `3` = 3 s; `4` = 4 s; `5` = 5 s; `6` = 6 s; `7` = 7 s; `8` = 8 s; `9` = 9 s; `10` = 10 s; `11` = 11 s; `12` = 12 s; `13` = 13 s; `14` = 14 s; `15` = 15 s; `16` = 16 s; `17` = 17 s; `18` = 18 s; `19` = 19 s; `20` = 20 s; `21` = 21 s; `22` = 22 s; `23` = 23 s; `24` = 24 s; `25` = 25 s; `26` = 26 s; `27` = 27 s; `28` = 28 s; `29` = 29 s; `30` = 30 s; `31` = 31 s; `32` = 32 s; `33` = 33 s; `34` = 34 s; `35` = 35 s; `36` = 36 s; `37` = 37 s; `38` = 38 s; `39` = 39 s; `40` = 40 s; `41` = 41 s; `42` = 42 s; `43` = 43 s; `44` = 44 s; `45` = 45 s; `46` = 46 s; `47` = 47 s; `48` = 48 s; `49` = 49 s; `50` = 50 s; `51` = 51 s; `52` = 52 s; `53` = 53 s; `54` = 54 s; `55` = 55 s; `56` = 56 s; `57` = 57 s; `58` = 58 s; `59` = 59 s; `60` = 60 s; `61` = 1 min 30 s; `62` = 2 min; `63` = 3 min; `64` = 4 min; `65` = 5 min; `66` = 6 min; `67` = 7 min; `68` = 8 min; `69` = 9 min; `70` = 10 min; `71` = 15 min | `0` | Activation delay for upper button |

### Object `417` - AUX control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Cyclical; `10` = `OFF`; `11` = `ON`; `15` = `PUL`; `17` = DOWN Shutter bistable command; `18` = UP shutter monostable command; `4` = Reset BI; `5` = Reset TRI; `6` = Reset `GEN`; `1` = Disable; `2` = Enable; `16` = UP shutter bistable command; `19` = DOWN Shutter monostable command | `0` | Modality; mode(Cyclical,off,on,pul,up,down,...) |
| `OUT_AUX_CH` | `1..15` | `1` | AUX channel |
| `TYPE_CONTACT` | No legal values specified in source | `0` | Contact type |

### Object `419` - Sound diffusion control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = `ON`/volume +; `1` = `OFF`/volume -; `2` = Change track; `3` = Switch source; `4` = Toggle `ON`/`OFF` | `0` | Modality; Mode (VOL,ON_OFF) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `3` = General | `0` | Addressing type |
| `A` | `0..9` | `0` | Area |
| `PF` | `0..9` | `0` | Audio point |
| `TYPE_CONTACT` | `0` = Normally open; `1` = Normally closed | `0` | Contact type |
| `IS_FOLLOW_ME` | `0` = No; `1` = Yes | `1` | Follow me |
| `SOURCE` | `1..9` | `1` | Source |
| `SUB_SOURCE` | `0..255` | `0` | Sub source |
| `CHANNEL` | `0` = Base Band; `1` = Left; `2` = Right; `3` = Stereo; `8` = Base Band and Video; `9` = Left and video; `10` = Right and video; `11` = Left and video | `3` | Channel (BB-Stereo) |

### Object `421` - Cyclic autoswitch control (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |

### Object `462` - Open lock command on session (Virgin-only candidate)

No direct firmware/Object association establishes reachability.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `870` | `218` | `4449` | `UP_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | UP shutter calbration time (m) |
| `870` | `218` | `4462` | `UP_SHUTTER_TIME_SECONDS` | `0..59` (entire reusable range retained) | `0` | UP shutter calbration time (s) |
| `870` | `218` | `4475` | `DOWN_SHUTTER_TIME_MINUTES` | `0..9` (entire reusable range retained) | `0` | DOWN shutter calbration time (m) |
| `870` | `218` | `4488` | `SLATS_ROTATION_TIME_DOWN_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - HIGH BYTE (ms) |
| `870` | `218` | `4501` | `SLATS_ROTATION_TIME_DOWN_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is all the way down - LOW BYTE (ms) |
| `870` | `218` | `4514` | `SLATS_ROTATION_TIME_MIDDLE_H` | `0..27` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - HIGH BYTE (ms) |
| `870` | `218` | `4527` | `SLATS_ROTATION_TIME_MIDDLE_L` | `0..255` (entire reusable range retained) | `0` | SLATS ROTATION calibration time when shutter is in middle position - LOW BYTE (ms) |
| `870` | `218` | `4540` | `SLATS_ROTATION_STEP_NUMBER` | `3..100` (entire reusable range retained) | `4` | SLATS ROTATION step number |
| `870` | `218` | `4620` | `SHUTTER_TYPE` | `3` = Standard with slats | `0` | Motor type; reusable default `0` is outside this subset; filter supplies no replacement default |
| `870` | `174` | `4092` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `144` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `174` - Shutter control (3 slots) | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `411` - Automation control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `412` - Lock / unlock actuator control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `416` - Scheduled scenario PLUS | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `418` - Open lock control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `426` - Staircase light control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `427` - Floor call control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `463` - Load control actuator visualization | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `143` - User interface settings for command | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `410` - Light control | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `218` - Shutter actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `174` - Shutter control (3 slots) | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `411` - Automation control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `411` - Automation control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `411` - Automation control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `411` - Automation control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `412` - Lock / unlock actuator control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `416` - Scheduled scenario PLUS | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `416` - Scheduled scenario PLUS | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `416` - Scheduled scenario PLUS | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `416` - Scheduled scenario PLUS | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `418` - Open lock control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `418` - Open lock control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `418` - Open lock control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `418` - Open lock control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `426` - Staircase light control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `426` - Staircase light control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `426` - Staircase light control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `426` - Staircase light control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `427` - Floor call control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `463` - Load control actuator visualization | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `463` - Load control actuator visualization | New energy saving and load control | `20` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `143` - User interface settings for command | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `143` - User interface settings for command | New energy saving and load control | `20` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `410` - Light control | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `410` - Light control | Burglar alarm system | `3` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `410` - Light control | Video door entry system | `4` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `410` - Light control | Sound system | `5` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |
| `218` - Shutter actuator | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| `410` | [Lighting](../../functional/who-1-lighting/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| `174`, `218`, `411` | [Automation](../../functional/who-2-automation/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| `412` | [Actuator locking](../../functional/who-14-special-commands/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| `416` | [CEN+ scenario triggers](../../functional/who-25-transversal/cen-plus.md) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| `463` | [Energy and load management](../../functional/who-18-energy-management/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |
| Video-entry-related roles | [Basic video entry](../../functional/who-6-basic-video-door-entry/);[Video entry and telephony](../../functional/who-8-video-door-entry-telephony/) | Related canonical families; which namespace and operation applies to each installed component is not established by the product manual alone |

| MX5220 published capability | Scope / distinction | Evidence |
| --- | --- | --- |
| Motor control | Logical relay interlock or pulse control; up, down, stop, opening percentage, stored-position recall | Exact MX5220 publisher record; documented capability, no captured frames |
| Position feedback / memorization | Closed, open or intermediate-position indication; direct self-learning of a stored opening level | Exact MX5220 publisher record; transport and procedure not established by this listing |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Use the shutter wiring labelled Y4672M2S; the shared sheet also covers Y4672M2L lighting outputs, whose lamp-load columns are separate from the Y4672M2S motor column. Configure the command and actuator roles separately according to the catalogue Firmware/Module filters. The sheet directs detailed application setup to the manufacturer app / documentation; it does not supply a complete physical M1/M2 mode matrix. Stored preset behavior is explicitly stated in the Y4672M2S export, while calibration and the complete preset procedure are not established in this original. Local control status and brightness adjustment are documented independently of OpenWebNet feedback.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

MX5220 and Y4672M2S are explicit database members of one technical item. The retained Y4672M2S originals and the separately retained MX5220 notice and product record establish variant-scoped specifications. MX5220 is marketed as Céliane, while the shared database description still says Light Now. The database description says “Light Now”, while the exact current export markets Light NOW. The export labels the bus module non-detachable, whereas the installation drawing distinguishes control and actuator assemblies: a classification label does not erase the physical connector. The export’s `110..230` V operating range and 250 Vac contact label describe different properties. Its temperature classification (`-5..36 °C`) conflicts with the installation sheet’s `0..40` °C. The lighting-oriented load / use classifications in the shutter export are preserved separately from the exact motor column. The installation terminal-capacity unit is printed m²; this appears malformed, but no alternate literal is invented.

The exact restriction table identifies reusable defaults outside a Firmware/Object subset. These are catalogue conflicts; no replacement default is inferred.

### Reviewed source boundaries

The exact notices and product records are reconciled above. The five linked Light NOW brochures/catalogues remain unexamined marketing/composition sources; no calibration, electrical-rating or transport claim is derived from them. The MX5220 page also links catalogue page p.78 (2024), the connected-home guide and Céliane brochure; these remain unexamined regional marketing/accessory sources. Firmware `870`’s `SHUTTER_TYPE=3` filter excludes reusable default `0`; no replacement is inferred. Object `174` omits destination level `14`; retain that hole rather than extending an apparent range.

The MX5220 listing describes an addressable SCS control in its functional text but marks its classification “Addressable: No”; that field is retained as a publisher classification discrepancy. Its `7 mA` standby value and the notice’s `9 mA` at maximum LED intensity have different stated measurement contexts. The MX5220 LED colours and shutter adjustment thresholds must not be copied to Y4672M2S. LE14826AC includes separate MX5230 lighting columns and MX5220C references; neither expands this dossier’s established catalogue identities.

## Evidence limits and open work

The full application configuration / calibration procedure, the MX5220C packaging relationship beyond its inclusion in the notice, and applicability of preset behavior to all catalogue releases remain documentation gaps. All catalogue identities remain established.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

### Discovered sources outside this review

These publisher-linked files were identified but are not used as retained evidence in this dossier. Firmware / installers and declarations remain separate evidence families. A listed URL does not establish payload identity, installed release or tested compatibility.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `Brochure_LHNOW_2M.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure_LHNOW_2M.pdf) |
| `Brochure_LHNOW_3M.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure_LHNOW_3M.pdf) |
| `Catalogue_LHNOW_2M.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue_LHNOW_2M.pdf) |
| `Catalogue_LHNOW_3M.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue_LHNOW_3M.pdf) |
| `Presentation_LHNOW.pdf` | Publisher-linked document not retained; its exact-product content remains unexamined | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Presentation_LHNOW.pdf) |

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0161-0170-2026-10-07.md#own-dev-0161)
