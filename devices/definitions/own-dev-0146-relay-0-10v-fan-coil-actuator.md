# Relay and 0-10 V fan-coil actuator

## Summary

F430R3V10 controls fan-coils using three relay outputs and two 0–10 V analogue outputs. Depending on its mode, it combines three-speed fans with proportional valves, or on/off valves with proportional fan speed. The latter modes require a documented production revision.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0146` | Project identity |
| Technical description | Relay and 0-10 V fan-coil actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003519`, `F430R3V10` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1685` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Temperature control | Main system association |
| Item model / `modobj` | `5` | Main association; independent of project ID |
| Firmware definition | `156`, `723` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators, Thermoregulation, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003519` | Established catalogue identity | Manufacturer database commercial record `2113` explicitly links this SKU to item `1685` |
| BTicino | `F430R3V10` | Established catalogue identity | Manufacturer database commercial record `1745` explicitly links this SKU to item `1685` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F430R3V10` | `8005543502846` | [F430R3V10-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/d1/5b/d15bfac1531aeb6aa66688805f5eaaba9a22d87540ec980c4e73e0af36595fb8.pdf) PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F430R3V10` | Actuator DIN with 3 relays and 2 outputs 0-10V | Canonical commercial record `1745` |
| `003519` | Actuator DIN with 3 relays and 2 outputs 0-10V | Canonical commercial record `2113` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000906-EN.pdf` | Technical Sheet ST-00000906-EN | `ST-00000906-EN; 23/03/2021` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/df/6e/df6ee00b6d2001ee97f6819434dccbc0d9ce6b0fdb398722363368e2a0383e04.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000906-EN.pdf) |
| `F430R3V10-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/d1/5b/d15bfac1531aeb6aa66688805f5eaaba9a22d87540ec980c4e73e0af36595fb8.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F430R3V10&include_technical=1) |
| `MM00781_b_IT.pdf` | Legacy manufacturer technical documentation | `MM00781_b_IT; 14/04/2016` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/b8/6b/b86b2b6850fcd6063724e19b76a4628c934bc6c850cec338610626604b0e32be.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MM00781_b_IT.pdf) |
| `ST_00000906_IT.pdf` | Legacy manufacturer technical documentation | `ST_00000906_IT; 23/03/2021` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/4a/48/4a48a05cf236c8897e1c53a7781c9bb43bfa3e7c1e0f9a8bab8d7d90fb5c3e66.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/ST_00000906_IT.pdf) |
| `ST_00000906_EN.pdf` | English counterpart of manufacturer-linked document | `ST_00000906_EN; 23/03/2021` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/df/6e/df6ee00b6d2001ee97f6819434dccbc0d9ce6b0fdb398722363368e2a0383e04.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/ST_00000906_EN.pdf) |
| `ST-00002703-EN.pdf` | Technical Sheet ST-00002703-EN | `ST-00002703-EN; 16/06/2026` | PDF p. 9: exact-reference ecosystem compatibility rows and minimum production batches; other EOS functions and wiring are outside this review. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1685`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `MyHOME-Suite-thermoregulation-actuator-functions-IT.html` | Manufacturer Suite function help | Publication date unstated | Exact F430R3V10 function inventory; not an installed application or allocation algorithm | [Archived original](https://archive.openwebnet-ha.org/sha256/bc/cc/bccc3ce223a0e3536f2e76e28ed010ec664397e14ab6fc7a14a30eb7dc7f5413.pdf) | [Publisher source](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/IT_MHS_function_0304/attuatori_termo.html) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS operating supply | `18..27 Vdc` | `ST-00000906-EN` printed/PDF pp. 1-4 |
| Standby / maximum draw | `20 mA / 60 mA` | `ST-00000906-EN` printed/PDF pp. 1-4 |
| Temperature / size | `5..40 °C; 4 DIN modules` | `ST-00000906-EN` printed/PDF pp. 1-4 |
| Relay ratings | `4 A resistive / 1 A inductive per relay` | `ST-00000906-EN` printed/PDF pp. 1-4 |
| Analogue outputs | `two 0..10 V signals; maximum 1 mA each` | `ST-00000906-EN` printed/PDF pp. 1-4 |
| Proportional fan-speed modes | `only from production batch 16W09` | `ST-00000906-EN` printed/PDF pp. 1-4 |
| Local interface | `manual controls and LEDs for the three relays and two analogue outputs` | `ST-00000906-EN` printed/PDF pp. 1-4 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. A negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `DRA (DIN-rail adaptor)` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `4` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Local operation/hand operation | `Yes` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `Yes` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Number of digital inputs | `0` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Suitable for C-load | `No` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Max. number of switching contacts | `3` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Rated current | `4 A` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Rated operating voltage (Min- Max) | `240-240 V` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Different phases connectable | `No` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `Yes` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Modular expandability | `No` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP20` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Connected object | `No` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |
| Product use function | `Thermal comfort management` | `F430R3V10-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1685` | Canonical catalogue |
| Technical item description | Actuator DIN with 3 relays and 2 outputs 0-10V | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Temperature control; key `2` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `5` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Temperature control | `5` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `156` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |
| `723` | `2` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `156` | `1` | `88` Temperature control 2 pipes fan coil actuator with 0-10V valve | Fixed/designated metadata | `2251` | `538` | `935` |
| `156` | `1` | `94` Temperature control 4 pipes fan coil actuator with 0-10V valves | Candidate alternative | `876` | `541` | `552` |
| `723` | `1` | `88` Temperature control 2 pipes fan coil actuator with 0-10V valve | Candidate alternative | `2651` | `538` | `1261` |
| `723` | `1` | `94` Temperature control 4 pipes fan coil actuator with 0-10V valves | Fixed/designated metadata | `2652` | `541` | `1262` |
| `723` | `1` | `139` Temperature control 2 pipes fan coil actuator with 0-10V speed | Candidate alternative | `2646` | `638` | `1256` |
| `723` | `1` | `140` Temperature control 4 pipes fan coil actuator with 0-10V speed | Candidate alternative | `2647` | `639` | `1257` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `156` | `504` Thermoregulation fan coil actuator with 0-10V valve virgin | `1` | `88`, `94`, `139`, `140` | `528` | `30` |
| `723` | `504` Thermoregulation fan coil actuator with 0-10V valve virgin | `1` | `88`, `94`, `139`, `140` | `528` | `61` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `156` | Physical configuration | `0` | Canonical firmware/mode association |
| `156` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `156` | Advanced Configuration | `2` | Canonical firmware/mode association |
| `723` | Physical configuration | `0` | Canonical firmware/mode association |
| `723` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `723` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `ZA / ZB / N` | zone `01..99` / progressive number `1..9` | `ST-00000906-EN` printed/PDF pp. 1-4 |
| `LOAD=0` | three-speed relay fan; analogue heating and cooling valves | `ST-00000906-EN` printed/PDF pp. 1-4 |
| `LOAD=1` | three-speed relay fan; one common analogue valve | `ST-00000906-EN` printed/PDF pp. 1-4 |
| `LOAD=2` | on/off heating/cooling relays; E/I reference; one common analogue fan speed | `ST-00000906-EN` printed/PDF pp. 1-4 |
| `LOAD=3` | on/off heating/cooling relays; separate analogue heating/cooling fan speeds | `ST-00000906-EN` printed/PDF pp. 1-4 |
| `LOAD=4` | one on/off valve / one analogue fan speed; printed table label conflicts with drawing | `ST-00000906-EN` printed/PDF pp. 1-4 |
| `Production / software scope` | speed modes >=16W09; Suite >=3.2 only without physical selectors | `ST-00000906-EN` printed/PDF pp. 1-4 |

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| `LOAD=0` | Relays 1/2/3: fan speeds 1/2/3; analogue 1: heating valve; analogue 2: cooling valve | 2021 EN/IT p. 2 |
| `LOAD=1` | Relays 1/2/3: fan speeds 1/2/3; analogue 1: shared valve; analogue 2: unused | 2021 EN/IT p. 2 |
| `LOAD=2` | Relays 1/2: heating/cooling valves; relay 3: E/I reference; analogue 1: shared speed; analogue 2: unused | 2021 EN/IT pp. 2, 4 |
| `LOAD=3` | Relays 1/2: heating/cooling valves; relay 3: unused; analogue 1/2: heating/cooling speeds | 2021 EN/IT pp. 2–3 |
| `LOAD=4` | Relay 1: shared valve; relays 2/3: unused; analogue 1: shared speed; analogue 2: unused | 2016/2021 IT p. 2; EN label defect reconciled below |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `156` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `156` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `156` | `ZB` | `0..9` | `0` | ZB; ZB thermo zone address |
| `156` | `N` | `0..9` | `0` | N; Thermoregulation zone device number N |
| `156` | `TYPE` | `0..2` | `0` | TYPE; Name : Fan coil a 4 tubi e 2 valvole 0V-10V - Value : 0 Fan coil a 2 tubi e valvola 0V-10V - Value : 1 |
| `723` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `723` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `723` | `ZB` | `0..9` | `0` | ZB; ZB thermo zone address |
| `723` | `N` | `0..9` | `0` | N; Thermoregulation zone device number N |
| `723` | `LOAD` | `0..4` | `0` | LOAD |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `88` - Temperature control 2 pipes fan coil actuator with 0-10V valve

Catalogue Object key `538` maps to external Object `88`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |

### Object `94` - Temperature control 4 pipes fan coil actuator with 0-10V valves

Catalogue Object key `541` maps to external Object `94`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |

### Object `139` - Temperature control 2 pipes fan coil actuator with 0-10V speed

Catalogue Object key `638` maps to external Object `139`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Device number |

### Object `140` - Temperature control 4 pipes fan coil actuator with 0-10V speed

Catalogue Object key `639` maps to external Object `140`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Device number |
| `NUMBER_OF_0-10V_OUTPUTS` | `1..2` | `2` | Number of 0-10V outputs |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `723` | `1` | `88` | `4964` | `LOAD=1` | None |
| `723` | `1` | `94` | `4963` | `LOAD=0` | None |
| `723` | `1` | `139` | `4967` | `LOAD=4` | None |
| `723` | `1` | `140` | `4965` | `LOAD=2` | `7215` |
| `723` | `1` | `140` | `4966` | `LOAD=3` | `7215` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `7215` | `LOAD=2` | `NUMBER_OF_0-10V_OUTPUTS` = `1` | `7215` |
| `7215` | `LOAD=3` | `NUMBER_OF_0-10V_OUTPUTS` = `2` | `7215` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `5` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `94` - Temperature control 4 pipes fan coil actuator with 0-10V valves | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `88` - Temperature control 2 pipes fan coil actuator with 0-10V valve | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `139` - Temperature control 2 pipes fan coil actuator with 0-10V speed | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `140` - Temperature control 4 pipes fan coil actuator with 0-10V speed | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Physical ZA/ZB selects zone `01..99`, N selects progressive number `1..9`, and LOAD selects the application. `LOAD=0`: three fan-speed relays, analogue 1 heating valve and analogue 2 cooling valve. `LOAD=1`: three fan-speed relays, analogue 1 common heat/cool valve, analogue 2 unused. `LOAD=2`: relay 1 heating valve, relay 2 cooling valve, relay 3 E/I mode reference, analogue 1 common fan speed, analogue 2 unused. `LOAD=3`: relay 1 heating valve, relay 2 cooling valve, relay 3 unused, analogue 1 heating speed and analogue 2 cooling speed. `LOAD=4`: single on/off valve with one analogue fan-speed signal; see the printed table discrepancy below. Suite 3.2 or later supports virtual configuration only without physical configurators. `LOAD=1`’s single valve connects to terminals 5–6; `LOAD=4`’s single valve connects to terminal 2 in the drawing. Use the fan-coil manufacturer’s wiring diagram and the shown 10 A protective breaker.

Apply the exact firmware restrictions above. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

Both the 2016 MM00781_b Italian sheet and the 2021 EN/IT sheets document proportional-valve and proportional-speed applications, with speed functions restricted to production batch 16W09 onward. The database likewise has separate firmware definitions and Object candidates; no arbitrary equivalence between firmware ID and production batch is established. `LOAD=4` is titled as proportional speed, and the drawing uses the analogue signal for fan speed, but its table labels analogue 1 “Heating / cooling valve”. The 2016 and 2021 Italian tables explicitly identify analogue output 1 as heating/cooling fan speed, agreeing with the English drawing and application title; the conflicting English table label is a translation defect. EOS compatibility lists F430R3V10/003519 with software configuration required. The database brand label Legrand BTicino groups both commercial records. Human-facing identities use the manufacturer’s separately established BTicino and Legrand reference families; the raw grouping is preserved here as catalogue terminology.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `ST-00000906-EN.pdf` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `F430R3V10-publisher-product-sheet.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `MM00781_b_IT.pdf` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `ST_00000906_IT.pdf` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `ST_00000906_EN.pdf` | PDF pp. 1-4: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `ST-00002703-EN.pdf` | PDF p. 9: exact-reference ecosystem compatibility rows and minimum production batches; other EOS functions and wiring are outside this review. Source conflicts and limits are reconciled above. |

### Semantic review findings

Firmware `156` (wildcard/default) directly offers Objects 88/94; firmware `723` (2.0.0/nondefault) directly offers 88/94/139/140. Both share Virgin `504` permitting all four, so Virgin admission is not proof of legacy direct placement or speed hardware. Legacy TYPE `0..2` has only two described applications; no third behavior is invented. Firmware `723` LOAD predicates 0/1/2/3/4 select 94/88/140/140/139, and conversion `7215` sets one/two speed outputs for LOAD 2/3. No relation filters, parameters or packages are stored. Firmware `N=0` differs from reusable `N=1` and speed Object `N=1..9`. All five relay/analogue assignment matrices are retained. Both 2016 and 2021 Italian revisions already document speed modes from 16W09, correcting the former implication that 2021 introduced them. Italian `LOAD=4` speed labels resolve the English valve-label defect without hiding it. Suite 3.2 and production 16W09 are distinct from catalogue firmware IDs. The 10 A protective breaker is not a relay rating. The archived Suite help corroborates exact family roles only; linked broader guide remains unexamined.

## Evidence limits and open work

The `LOAD=4` label defect, installed production batch, exact firmware-to-mode applicability, output timing and feedback require corroboration.

No installed hardware revision or microcontroller fingerprint is retained for this cluster. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Canonical catalogue extraction and reconciliation are complete for the retained evidence; further documentation discovery, runtime corroboration and final evidence closure remain partial.

### Discovered sources outside this review

These publisher-linked sources were identified but were not retained or used as evidence. Their presence is not evidence of installed firmware, a certified test result or additional capability.

| Source | Remaining scope | Publisher provenance |
| --- | --- | --- |
| `Brochure Living_NOW 2M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure Living_NOW 2M.pdf) |
| `Brochure Living_NOW 3M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure Living_NOW 3M.pdf) |
| `Brochure MyHOME.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Brochure MyHOME.pdf) |
| `Catalogue Living_NOW 2M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue Living_NOW 2M.pdf) |
| `Catalogue Living_NOW 3M.pdf` | Software licence, declaration or ancillary document; not used for product specifications here | [Publisher listing](https://assets.legrand.com/pim/DOCUMENT/Catalogue Living_NOW 3M.pdf) |

Known earlier EOS system editions RA00215AC_I_EN.pdf and ST-00001816-EN.pdf were discovered but not examined in this batch; no earlier-edition capability is transferred. The reviewed EOS compatibility evidence is the 16/06/2026 edition only.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0141-0150-2026-10-06.md#own-dev-0146)
