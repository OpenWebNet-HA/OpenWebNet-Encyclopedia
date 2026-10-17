# Room Controller - 4 dimming outputs 0-10 V

## Summary

`BMDI3002` / `048843` is a Room Controller for four lighting circuits using analogue ballast dimming. It powers compatible bus controls and sensors, provides local load buttons and automatic pairing, and exposes four dimmer Modules plus a separate controller context in the catalogue.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0075` | Project identity |
| Technical description | Room Controller - 4 dimming outputs 0-10 V | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMDI3002`, `048843` | Canonical commercial records |
| Catalogue item | `86` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `169` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `5` | Canonical firmware catalogue |
| Categories | Lighting Management, Room Controller, 0-10 V dimmer | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMDI3002` | Established identity | canonical commercial record for item `86` |
| Legrand | `048843` | Established identity | canonical commercial record for item `86` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `048843` | `3245060488437` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/0e/6a/0e6ac88b94c5057fabab84f9f4d5fd816a075cb76afa669aef633367f3077ca0.pdf), `048843-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | publisher product sheet | current catalogue export | `BMDI3002` four-output 1-10 V Room Controller; printed p. 1 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/36/26/3626218267f680903b46d190610c3a83879eb18b773d6e54a2ac4c0523a48e64.pdf) | [Official source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMDI3002) |
| `048843-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact SKU/GTIN metadata retained;technical/installation downloads examined separately below;generic ETIM attributes not adopted | [Archived HTML](https://archive.openwebnet-ha.org/sha256/0e/6a/0e6ac88b94c5057fabab84f9f4d5fd816a075cb76afa669aef633367f3077ca0.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-4-circuits-mosaic-a-fonction-variation-ballast-1v-a-10v-ou-on-et-off-avec-4-sorties-1000va) |
| `BT00309_c_IT.pdf` | Italian exact technical sheet | BT00309-c-IT;2013-11-12 | `BMDI3002`;full 3 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/a7/58/a758d94080e906901e65400ef5d8f9029e6d897948ec2d20a1f0c074641bb3c5.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/BT00309_c_IT.pdf) |
| `F01121EN-00.pdf` | English exact technical sheet | F01121EN/00;2010-09-22 | `048843`;full 3 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/1a/c2/1ac2adabf3c47611bb0853bbb126eabd34e1b70d96ef26e3593e90b02f23c354.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/F01121EN-00.pdf) |
| `F01121FR-00.pdf` | French exact technical sheet | F01121FR/00;2010-09-22 | `048843`;full 3 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/ce/0b/ce0bb4cf69eb7a9e9f345bdc5fbd4274d5766b57e792be710b2b08a6a947086f.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/F01121FR-00.pdf) |
| `LE03163AB.pdf` | Illustrated installation instructions | LE03163AB;date not printed | `048843`;full 2 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/2a/30/2a301e4d62ea054a4c55a7b4a9ff84456ae655931aaaa5db5bbd2c51ee073ae0.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/LE03163AB.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply | `100..240 Vac`, `50..60 Hz` in technical tables/export; description’s base installation says `110..230 Vac` | BT00309-c-IT, p. 1; F01121EN/FR-00, p. 1 |
| Loads at 230/110 V | Four × `4.3 A`. Linear/halogen ballast loads:`4 × 1000/500 VA`; CFL ballast loads: Italian `4 × 1000/500 VA`, Legrand 4 × 1000/`500 W` | BT00309-c-IT and F01121EN/FR-00, p. 1; LE03163AB, p. 1 |
| Bus and cable limits | Four local bus ports, `200 mA` combined; riser connection; `150 m` controller–furthest sensor, `500 m` supply–furthest product | BT00309-c-IT, pp. 1–2; F01121EN/FR-00, pp. 1–2 |
| Power/environment | `4 W` no-load; `-5..45 °C` operating, `-20..70 °C` storage; IP20, IK04; `580 g` | BT00309-c-IT and F01121EN/FR-00, p. 1 |
| Dimensions and terminals | `147 × 240 mm` body, `275 mm` including mounting extent, `50 mm` dimension arrows; screw supply `2 × 2.5 mm²`, analogue ≤`1.5 mm²` | BT00309-c-IT and F01121EN/FR-00, pp. 1–2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `86` | Canonical catalogue |
| Technical item | Room Controller - 4 dimming outputs 0-10 V | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `169` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `169` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `86` | `BMDI3002` | `1` | `5` | `BTicino_Undefined_Room Controller 4 Dim Outpu` |
| `1775` | `048843` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `209` | `-1` | `-1` | `-1` | `5` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `209` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `901` | `8` | `566` |
| `209` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `902` | `8` | `566` |
| `209` | `3` | `8` Dimmer actuator | Fixed/designated metadata | `903` | `8` | `566` |
| `209` | `4` | `8` Dimmer actuator | Fixed/designated metadata | `904` | `8` | `566` |
| `209` | `5` | `167` Room controller | Fixed/designated metadata | `900` | `167` | `565` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `209` | Physical configuration | `0` | Canonical firmware/mode association |
| `209` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `209` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `209` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `209` | `A` | `0..9` | `0` | A; Environment |
| `209` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `209` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `209` | `PL3` | `0..9` | `0` | PL3; PL3 - (0-9) |
| `209` | `PL4` | `0..9` | `0` | PL4; PL4 - (0-9) |
| `209` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `8` - Dimmer actuator

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `A`, `PL`, `G1`, `G2` | Reusable schema; apply the Device and firmware restrictions below. |
| Operation, timing and presentation | `M`, `LOCAL_BUTTON`, `DELAYED_OFF`, `STATE_SAVING_ON_RESET`, `HOURS`, `MINUTES`, `SECONDS`, `MIN_LEVEL`, `TYPE_LOAD`, `TYPE_STANDARD`, `MIN_LEVEL_ADV`, `MIN_AUTO`, `G3`, `G4`, `G5`, `G6`, `G7`, `G8`, `G9`, `G10` | Reusable schema; apply the Device and firmware restrictions below. |

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality; mode (M,S + PULL) |
| `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled | `0` | State saving on reset |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `MIN_LEVEL` | `1..100` | `1` | Minimum level |
| `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge | `0` | Type of load; Default value depends on device. |
| `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard | `0` | Voltage standard |
| `MIN_LEVEL_ADV` | `1..100` | `0` | Minimum level advanced; Default value depends on device and Type of load value |
| `MIN_AUTO` | `0` = Minimum not editable; `1` = Minimum editable | `0` | Enable / Disable minimum level |
| `G1` | `0..255` | `0` | Group 1 |
| `G2` | `0..255` | `0` | Group 2 |
| `G3` | `0..255` | `0` | Group 3 |
| `G4` | `0..255` | `0` | Group 4 |
| `G5` | `0..255` | `0` | Group 5 |
| `G6` | `0..255` | `0` | Group 6 |
| `G7` | `0..255` | `0` | Group 7 |
| `G8` | `0..255` | `0` | Group 8 |
| `G9` | `0..255` | `0` | Group 9 |
| `G10` | `0..255` | `0` | Group 10 |

### Object `167` - Room controller

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `MODE` | `0` = Stand-alone mode; `1` = Supervision mode | `0` | Modality; Mode |

### Device-specific interpretation

Firmware `209` is the wildcard catalogue default with Deprecated status, not a proven installed version or current availability. Slots `1..4` are Object `8` load contexts; slot `5` is Object `167` controller MODE (stand-alone 0 / supervision 1, default 0), not another electrical output. No Virgin, slot condition or conversion is stored. Relation filters without subset rows retain the complete reusable domains rather than proving physical support for every load enum, local-button mode or timer. The reusable MIN_LEVEL_ADV default 0 lies outside 1..100. Firmware A/PL/M and the recorded physical/virtual/advanced modes are retained, but the examined Lighting Management sheets describe automatic pairing and software/remote setup; their procedures do not establish a physical configurator socket. Symbolic SLA/PUL branches are recorded as firmware values but no conversion is supplied. The catalogue title says 0-10 V while the technical load interface is 1-10 V; wiring labels 0-10 V and reusable TYPE_STANDARD are separate evidence, not proof that every installed ballast responds down to 0 V.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `209` | `8` | `1005` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `209` | `8` | `1006` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `209` | `8` | `1007` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `209` | `8` | `1008` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `209` | `8` | `1009` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | Type of Load |
| `209` | `8` | `1010` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |
| `209` | `8` | `2184` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `86` / `modobj = 169` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`, `167`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Control | Four independent ballast outputs, local ON/OFF/dimming, automatic pairing and Zero Crossing in export | `BMDI3002` export p. 1; LE03163AB pp. 1–2 |
| Fault response | Peripheral fault on local buses: lights relight after 10 min; upstream bus connection fault: after 50 s; red LED indicates local bus capacity exceeded | BT00309-c-IT and F01121EN/FR-00, p. 1 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Wire with mains disconnected. Automatic pairing begins at power-on; BTicino distinguishes standalone and integrated bus installations and documents Plug&Go, Push&Learn and Virtual Configurator. The Legrand sheets specify remote configuration tools 88235/88230; those tool manuals and detailed sensor sheets are not incorporated. Local test buttons switch loads; holding the relevant dimming button adjusts level. The software catalogue mode associations remain distinct from these product commissioning procedures.

## Source reconciliation

The database establishes `BMDI3002`/048843. Italian BT00309-c-IT dated 12 November 2013 and Legrand F01121 EN/FR revision 00 dated 22 September 2010 agree on four lighting channels and principal ratings. CFL ballast limits use VA in the Italian sheet and W in the Legrand sheet/instruction, retained as a source discrepancy. The Italian description’s `110..230` V is narrower than its own `100..240` V table. Both languages of the Legrand technical sheet were examined; the FR version cites NF EN 50428 while EN cites IEC 60669-2-1, so historical declarations remain regional rather than current certification claims. The export names four local ports; the diagrams and LE03163AB corroborate their combined 200 mA boundary.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); these software records do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- No installed hardware observation is retained. Exact tool manuals, detailed sensor setup, Suite help, referenced drawings and broader current installation guides are unexamined; no commissioning-completion claim is made.
- Catalogue 0-10 V wording, wiring labels and reusable voltage/load settings do not by themselves establish every ballast or LED compatibility. Regional standards and load units are kept source-specific.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `048843-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `048843` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/0e/6a/0e6ac88b94c5057fabab84f9f4d5fd816a075cb76afa669aef633367f3077ca0.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-4-circuits-mosaic-a-fonction-variation-ballast-1v-a-10v-ou-on-et-off-avec-4-sorties-1000va); SHA-256 `0e6ac88b94c5057fabab84f9f4d5fd816a075cb76afa669aef633367f3077ca0`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0071-0080-2026-10-06.md#own-dev-0075)
