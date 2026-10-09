# Eight-output temperature-control actuator

## Summary

F430R8 provides eight relay outputs for temperature-control loads. It can switch separate valves, drive paired open/close valves or control fan-coils with several fan speeds. The selected role determines which outputs operate together and which remain available.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0144` | Project identity |
| Technical description | Eight-output temperature-control actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `003517`, `F430R8` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1683` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Temperature control | Main system association |
| Item model / `modobj` | `3` | Main association; independent of project ID |
| Firmware definition | `155` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `8` | Firmware metadata |
| Categories | Actuators, Thermoregulation | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand | `003517` | Established catalogue identity | Manufacturer database commercial record `2123` explicitly links this SKU to item `1683` |
| BTicino | `F430R8` | Established catalogue identity | Manufacturer database commercial record `1743` explicitly links this SKU to item `1683` |

### EAN-13 commercial identifiers

EANs identify the named commercial variant, not the configured physical device or its diagnostic identity.

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `F430R8` | `8005543501771` | [F430R8-publisher-product-sheet.pdf](https://archive.openwebnet-ha.org/sha256/a0/1f/a01f9ea0b1c9b7bf665e6a944b829ee639bd0b08af97369eb4a57d03116234b2.pdf) PDF p. 1 |

### Catalogue labels

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `F430R8` | Actuator DIN with 8 outputs | Canonical commercial record `1743` |
| `003517` | Actuator DIN with 8 outputs | Canonical commercial record `2123` |

These labels describe the retained historical catalogue; they do not establish installed state or present-day market availability.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `ST-00000914-EN.pdf` | Technical Sheet ST-00000914-EN | `ST-00000914-EN; 15/04/2021` | Exact English 2021 sheet; PDF pp. 1–2 examined in full; introduction omits one relay count | [Archived original](https://archive.openwebnet-ha.org/sha256/8d/f7/8df7f135a9b4d26382d3cd32b278fa6a4ae5de82752fac999b81ef6608fd2596.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00000914-EN.pdf) |
| `F430R8-publisher-product-sheet.pdf` | Exact English product export | `Publisher DATASHEET; 05.10.2026` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. | [Archived original](https://archive.openwebnet-ha.org/sha256/a0/1f/a01f9ea0b1c9b7bf665e6a944b829ee639bd0b08af97369eb4a57d03116234b2.pdf) | [Publisher original](https://www.bticino.com/products/pdf?sku=BT-F430R8&include_technical=1) |
| `MM00779_b_IT.pdf` | Legacy manufacturer technical documentation | `MM00779_b_IT; 05/04/2016` | Exact Italian 2016 b sheet; PDF pp. 1–2 examined in full; five-relay four-pipe count explicit | [Archived original](https://archive.openwebnet-ha.org/sha256/f2/46/f246af2706f2a77c36aa55565ea66f4bf8049ba2370b5efc611b1dce9da27a90.pdf) | [Publisher original](https://dar.bticino.it/asset/Documents/MM00779_b_IT.pdf) |
| `ST-00002703-EN.pdf` | Technical Sheet ST-00002703-EN | `ST-00002703-EN; 16/06/2026` | PDF p. 9: exact-reference ecosystem compatibility rows and minimum production batches; other EOS functions and wiring are outside this review. | [Archived original](https://archive.openwebnet-ha.org/sha256/b2/f5/b2f5090b601e33cdef9ba666108848ff4d9800792ccd5b7c14385da300bf0ffa.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/ST-00002703-EN.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1683`: complete extracted Device/firmware/Object/configuration associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |
| `MyHOME-Suite-thermoregulation-actuator-functions-IT.html` | Italian manufacturer Suite function help | MHS_function_0304b / IT_MHS_function_0304; page publication date not stated | Exact F430R8 function-family inventory examined; linked navigation/image assets are not independent evidence or an output-allocation algorithm | [Archived original](https://archive.openwebnet-ha.org/sha256/bc/cc/bccc3ce223a0e3536f2e76e28ed010ec664397e14ab6fc7a14a30eb7dc7f5413.pdf) | [Publisher source](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/IT_MHS_function_0304/attuatori_termo.html) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS operating supply | `18..27 Vdc` | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |
| Standby / maximum draw | `15 mA / 100 mA` | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |
| Temperature / size | `5..40 °C; 4 DIN modules` | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |
| Relay ratings | `4 A resistive / 1 A inductive per output` | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |
| Capacity | `8 on/off valves or 4 open/close or three-point valves` | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |
| Fan-coil applications | `two 2-pipe on/off units; one 2-pipe three-point, 4-pipe on/off or 4-pipe three-point unit` | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |

### Publisher export attributes

These are the complete captured publisher classification values for the named variants. They do not replace technical-sheet load ratings or establish runtime protocol support. A negative connected-object classification does not exclude remote control through another system device.

| Property | Publisher value | Variant / source |
| --- | --- | --- |
| Bus system KNX | `No` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system KNX-RF (Radio Frequency) | `No` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system radio frequency | `No` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system LON | `No` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Bus system Powernet | `No` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Other bus systems | `Other` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Mounting method | `DRA (DIN-rail adaptor)` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Width in number of modular spacings | `4` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Local operation/hand operation | `Yes` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| With LED indication | `Yes` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Number of digital inputs | `0` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Suitable for C-load | `No` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Max. number of switching contacts | `8` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Rated current | `4 A` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Rated operating voltage (Min- Max) | `240-240 V` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Different phases connectable | `No` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| With bus connection | `Yes` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Modular expandability | `No` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Degree of protection (IP) | `IP20` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Connected object | `No` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |
| Product use function | `Thermal comfort management` | `F430R8-publisher-product-sheet.pdf` PDF p. 2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1683` | Canonical catalogue |
| Technical item description | Actuator DIN with 8 outputs | Canonical catalogue |
| Item family | 0; key `2` | Canonical catalogue |
| Main system | Temperature control; key `2` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `3` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Temperature control | `3` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `155` | `-1` | `-1` | `-1` | `8` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `155` | `1` | `169` Temperature control on/off actuator | Fixed/designated metadata | `2107` | `169` | `880` |
| `155` | `1` | `170` Temperature control open/close actuator | Candidate alternative | `2100` | `170` | `879` |
| `155` | `1` | `171` 2 pipes fan coil actuator with `ON`-`OFF` valve | Candidate alternative | `848` | `171` | `546` |
| `155` | `1` | `52` Temperature control pump actuator | Candidate alternative | `853` | `533` | `547` |
| `155` | `1` | `86` Temperature control 3 points valve actuator | Candidate alternative | `861` | `536` | `548` |
| `155` | `1` | `87` Temperature control 2 pipes fan coil actuator with 3 points valve | Candidate alternative | `868` | `537` | `549` |
| `155` | `1` | `89` Temperature control 4 pipes fan coil actuator with `ON`/`OFF` valves | Candidate alternative | `2096` | `539` | `878` |
| `155` | `1` | `93` Temperature control 4 pipes fan coil actuator with 3 points valve | Candidate alternative | `872` | `540` | `550` |
| `155` | `2` | `169` Temperature control on/off actuator | Fixed/designated metadata | `2108` | `169` | `880` |
| `155` | `2` | `170` Temperature control open/close actuator | Candidate alternative | `2101` | `170` | `879` |
| `155` | `2` | `171` 2 pipes fan coil actuator with `ON`-`OFF` valve | Candidate alternative | `849` | `171` | `546` |
| `155` | `2` | `52` Temperature control pump actuator | Candidate alternative | `854` | `533` | `547` |
| `155` | `2` | `86` Temperature control 3 points valve actuator | Candidate alternative | `862` | `536` | `548` |
| `155` | `2` | `87` Temperature control 2 pipes fan coil actuator with 3 points valve | Candidate alternative | `869` | `537` | `549` |
| `155` | `2` | `89` Temperature control 4 pipes fan coil actuator with `ON`/`OFF` valves | Candidate alternative | `2097` | `539` | `878` |
| `155` | `2` | `93` Temperature control 4 pipes fan coil actuator with 3 points valve | Candidate alternative | `873` | `540` | `550` |
| `155` | `3` | `169` Temperature control on/off actuator | Fixed/designated metadata | `2109` | `169` | `880` |
| `155` | `3` | `170` Temperature control open/close actuator | Candidate alternative | `2102` | `170` | `879` |
| `155` | `3` | `171` 2 pipes fan coil actuator with `ON`-`OFF` valve | Candidate alternative | `850` | `171` | `546` |
| `155` | `3` | `52` Temperature control pump actuator | Candidate alternative | `855` | `533` | `547` |
| `155` | `3` | `86` Temperature control 3 points valve actuator | Candidate alternative | `863` | `536` | `548` |
| `155` | `3` | `87` Temperature control 2 pipes fan coil actuator with 3 points valve | Candidate alternative | `870` | `537` | `549` |
| `155` | `3` | `89` Temperature control 4 pipes fan coil actuator with `ON`/`OFF` valves | Candidate alternative | `2098` | `539` | `878` |
| `155` | `4` | `169` Temperature control on/off actuator | Fixed/designated metadata | `2110` | `169` | `880` |
| `155` | `4` | `170` Temperature control open/close actuator | Candidate alternative | `2103` | `170` | `879` |
| `155` | `4` | `171` 2 pipes fan coil actuator with `ON`-`OFF` valve | Candidate alternative | `851` | `171` | `546` |
| `155` | `4` | `52` Temperature control pump actuator | Candidate alternative | `856` | `533` | `547` |
| `155` | `4` | `86` Temperature control 3 points valve actuator | Candidate alternative | `864` | `536` | `548` |
| `155` | `4` | `87` Temperature control 2 pipes fan coil actuator with 3 points valve | Candidate alternative | `871` | `537` | `549` |
| `155` | `4` | `89` Temperature control 4 pipes fan coil actuator with `ON`/`OFF` valves | Candidate alternative | `2099` | `539` | `878` |
| `155` | `5` | `169` Temperature control on/off actuator | Fixed/designated metadata | `2111` | `169` | `880` |
| `155` | `5` | `170` Temperature control open/close actuator | Candidate alternative | `2104` | `170` | `879` |
| `155` | `5` | `171` 2 pipes fan coil actuator with `ON`-`OFF` valve | Candidate alternative | `852` | `171` | `546` |
| `155` | `5` | `52` Temperature control pump actuator | Candidate alternative | `857` | `533` | `547` |
| `155` | `5` | `86` Temperature control 3 points valve actuator | Candidate alternative | `865` | `536` | `548` |
| `155` | `6` | `169` Temperature control on/off actuator | Fixed/designated metadata | `2112` | `169` | `880` |
| `155` | `6` | `170` Temperature control open/close actuator | Candidate alternative | `2105` | `170` | `879` |
| `155` | `6` | `52` Temperature control pump actuator | Candidate alternative | `858` | `533` | `547` |
| `155` | `6` | `86` Temperature control 3 points valve actuator | Candidate alternative | `866` | `536` | `548` |
| `155` | `7` | `169` Temperature control on/off actuator | Fixed/designated metadata | `2113` | `169` | `880` |
| `155` | `7` | `170` Temperature control open/close actuator | Candidate alternative | `2106` | `170` | `879` |
| `155` | `7` | `52` Temperature control pump actuator | Candidate alternative | `859` | `533` | `547` |
| `155` | `7` | `86` Temperature control 3 points valve actuator | Candidate alternative | `867` | `536` | `548` |
| `155` | `8` | `169` Temperature control on/off actuator | Fixed/designated metadata | `2114` | `169` | `880` |
| `155` | `8` | `52` Temperature control pump actuator | Candidate alternative | `860` | `533` | `547` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| `155` | `519` Thermoregulation relay virgin | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8` | `52`, `86`, `87`, `89`, `93`, `169`, `170`, `171` | `519` | `29` |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `155` | Physical configuration | `0` | Canonical firmware/mode association |
| `155` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `155` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

### Manufacturer configuration and operating modes

These published settings are independent of catalogue programming-mode IDs. Revision/variant limitations are reconciled in Programming and Source reconciliation.

| Selector / setting | Published role or value | Evidence |
| --- | --- | --- |
| `ZA / ZB / N` | zone tens / units / progressive actuator number | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |
| `LOAD=0` | OUT`1..3` fan speeds; OUT4 heating valve; OUT5 cooling valve; OUT`6..8` unused | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |
| `LOAD=1` | OUT`1..3` fan speeds; OUT4/5 valve open/close; OUT`6..8` unused | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |
| `LOAD=2` | OUT`1..3` fan speeds; OUT4/5 heating open/close; OUT6/7 cooling open/close; OUT8 unused | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |
| `Other applications` | complete software configuration; Suite >=1.3; output reuse scoped to application | `ST-00000914-EN` printed/PDF pp. 1-2; `F430R8-publisher-product-sheet` PDF p. 2 |

### Physical output allocation

| Output | `LOAD=0`: four-pipe on/off | `LOAD=1`: two-pipe three-point | `LOAD=2`: four-pipe three-point |
| --- | --- | --- | --- |
| 1 | Fan speed 1 | Fan speed 1 | Fan speed 1 |
| 2 | Fan speed 2 | Fan speed 2 | Fan speed 2 |
| 3 | Fan speed 3 | Fan speed 3 | Fan speed 3 |
| 4 | Heating valve | Valve opening | Heating valve opening |
| 5 | Cooling valve | Valve closure | Heating valve closure |
| 6 | Unused | Unused | Cooling valve opening |
| 7 | Unused | Unused | Cooling valve closure |
| 8 | Unused | Unused | Unused |

Exact ST-00000914-EN and MM00779_b_IT PDF p. 1. Software-only output reuse is outside this physical matrix.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `155` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `155` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `155` | `ZB` | `0..9` | `0` | ZB; ZB thermo zone address |
| `155` | `N` | `0..9` | `0` | N; Thermoregulation zone device number N |
| `155` | `TYPE` | `0..2` | `0` | TYPE; Fan coil a 4 tubi e 2 valvole di `ON`/`OFF` - Value : 0 Fan coil a 2 tubi e valvola a 3 punti - Value : 1 Fan coil a 4 tubi e 2 valvole a 3 punti - Value : 2 |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `169` - Temperature control on/off actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Device number |
| `SUBTYPE` | `16` = Valve on/off; `17` = Pump | `16` | Type of load |

### Object `170` - Temperature control open/close actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Device number |
| `SUBTYPE` | `16` = Valve on/off; `17` = Pump | `16` | Type of load |

### Object `171` - 2 pipes fan coil actuator with `ON`-`OFF` valve

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `1..9` | `1` | Device number |

### Object `52` - Temperature control pump actuator

Catalogue Object key `533` maps to external Object `52`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00` | `00` | Zone |
| `N` | `1..9` | `1` | Device number |

### Object `86` - Temperature control 3 points valve actuator

Catalogue Object key `536` maps to external Object `86`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |
| `VALVE_TIME_LOW` | `0..255` | `60` | Valve time low; Valve_time_low (Valve time in seconds, over 2 bytes (0...767s)) |
| `VALVE_TIME_HIGH` | `0..2` | `0` | Valve time high; Valve_time_high (Valve time in seconds, over 2 bytes (0...767s)) |

### Object `87` - Temperature control 2 pipes fan coil actuator with 3 points valve

Catalogue Object key `537` maps to external Object `87`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |
| `VALVE_TIME_LOW` | `0..255` | `60` | Valve time low; Valve_time_low (Valve time in seconds, over 2 bytes (0...767s)) |
| `VALVE_TIME_HIGH` | `0..2` | `0` | Valve time high; Valve_time_high (Valve time in seconds, over 2 bytes (0...767s)) |

### Object `89` - Temperature control 4 pipes fan coil actuator with `ON`/`OFF` valves

Catalogue Object key `539` maps to external Object `89`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |

### Object `93` - Temperature control 4 pipes fan coil actuator with 3 points valve

Catalogue Object key `540` maps to external Object `93`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `01..99` | `01` | Zone |
| `N` | `0..9` | `1` | Device number |
| `HEATING_VALVE_TIME_LOW` | `0..255` | `60` | Heating valve time low; (Valve time in seconds, over 2 bytes (0...767s)) |
| `HEATING_VALVE_TIME_HIGH` | `0..2` | `0` | Heating valve time high; (Valve time in seconds, over 2 bytes (0...767s)) |
| `COOLING_VALVE_TIME_LOW` | `0..255` | `60` | Cooling valve time low; (Valve time in seconds, over 2 bytes (0...767s)) |
| `COOLING_VALVE_TIME_HIGH` | `0..2` | `0` | Cooling valve time high; (Valve time in seconds, over 2 bytes (0...767s)) |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `155` | `169` | `1670` | `SUBTYPE` | `16` = Valve on/off; `17` = Pump (entire reusable range retained) | `16` | Type of load |
| `155` | `170` | `1662` | `SUBTYPE` | `16` = Valve on/off; `17` = Pump (entire reusable range retained) | `16` | Type of load |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution remains in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `3` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `171` - 2 pipes fan coil actuator with `ON`-`OFF` valve | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `52` - Temperature control pump actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `86` - Temperature control 3 points valve actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `87` - Temperature control 2 pipes fan coil actuator with 3 points valve | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `93` - Temperature control 4 pipes fan coil actuator with 3 points valve | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `89` - Temperature control 4 pipes fan coil actuator with `ON`/`OFF` valves | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `170` - Temperature control open/close actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |
| `169` - Temperature control on/off actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system/model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Physical ZA/ZB selects the zone and N the progressive actuator number. `LOAD=0` selects a four-pipe on/off fan-coil: OUT1/2/3 are low/medium/high fan speed, OUT4 heating valve and OUT5 cooling valve; OUT`6..8` unused. `LOAD=1` uses OUT`1..3` for fan speeds and OUT4/5 for valve opening/closing; OUT`6..8` unused. `LOAD=2` uses OUT`1..3` for fan speeds, OUT4/5 heating opening/closing, OUT6/7 cooling opening/closing and OUT8 unused. Other applications require MyHOME_Suite 1.3 or later; the complete application must then be configured in software, which can assign otherwise unused outputs. Local override buttons and LEDs identify outputs. The two-pipe on/off software-only wiring note uses the single valve on terminal 5. Protect the illustrated mains circuit with the specified 10 A breaker; this is separate from the relay rating.

Apply the exact firmware restrictions above. The generic session/validation method remains in [Programming](../../programming/).

## Source reconciliation

The exact 2021 sheet and older Italian sheet distinguish eight on/off channels from paired valve and fan-coil roles. The introductory four-pipe on/off relay count is missing in print; its explicit `LOAD=0` mapping uses five outputs. The software-only two-pipe note’s terminal 5 is retained separately from physical `LOAD=0` heating output 4. Multiple Objects in the database are alternate Module placements, not eight simultaneously active fan-coil Objects. The current EOS sheet explicitly lists F430R8 and 003517, with software configuration required. The database brand label Legrand BTicino groups both commercial records. Human-facing identities use the manufacturer’s separately established BTicino and Legrand reference families; the raw grouping is preserved here as catalogue terminology.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `ST-00000914-EN.pdf` | Exact English 2021 sheet; PDF pp. 1–2 examined in full; introduction omits one relay count Source conflicts and limits are reconciled above. |
| `F430R8-publisher-product-sheet.pdf` | PDF pp. 1-3: exact-reference specifications, configuration or wiring as applicable. Printed and PDF pagination coincide where numbered. Source conflicts and limits are reconciled above. |
| `MM00779_b_IT.pdf` | Exact Italian 2016 b sheet; PDF pp. 1–2 examined in full; five-relay four-pipe count explicit Source conflicts and limits are reconciled above. |
| `ST-00002703-EN.pdf` | PDF p. 9: exact-reference ecosystem compatibility rows and minimum production batches; other EOS functions and wiring are outside this review. Source conflicts and limits are reconciled above. |

### Semantic review findings

Firmware `155` declares eight slots with progressively fewer legal candidates toward the final outputs; Virgin `519` permits eight reusable function types, not eight simultaneous complete fan-coils. No slot predicates, filters, conversions or parameter/package associations establish automatic relay allocation. Pump Object `52` uses `ZAZB=00` whereas ordinary zone Objects use `01..99`; firmware ZA/ZB/N defaults 0 cannot be treated as every reusable default. The exact Italian 2016 sheet fills the five-relay count missing from the English 2021 introduction and agrees on the `LOAD=0/1/2` wiring matrix. Software 1.3+ configures the entire application and unused outputs; two-pipe on/off uses terminal 5, distinct from the four-pipe physical matrix. English 2021 adds the 10 A protective breaker note; the product relays remain 4 A resistive/1 A inductive. The archived Suite function inventory independently lists the exact product's supported families but is not an installed configuration or output-allocation algorithm. Linked GUI-MHOME and broader brochures remain unexamined.

## Evidence limits and open work

Output reuse in each installed firmware, two-pipe software mapping, valve timing and actual feedback/diagnostics remain uncorroborated.

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

The current product export links installation guide GUI-MHOME as well as commercial brochures; those linked originals were not examined here. The retained Suite help provides a function-family inventory, with publication/installed-software applicability still unestablished.

Known earlier EOS system editions RA00215AC_I_EN.pdf and ST-00001816-EN.pdf were discovered but not examined in this batch; no earlier-edition capability is transferred. The reviewed EOS compatibility evidence is the 16/06/2026 edition only.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 7 October 2026](../../project/review/device-reviews-0141-0150-2026-10-06.md#own-dev-0144)
