# Room Controller - 2 dimming outputs 0-10 V

## Summary

`BMDI3001` / `048842` controls two lighting circuits through analogue ballast dimming and supplies compatible SCS controls or sensors from its local bus ports. It supports automatic pairing, local load tests and integrated bus operation; its two dimmer Modules are accompanied by a separate controller Module.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0079` | Project identity |
| Technical description | Room Controller - 2 dimming outputs 0-10 V | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMDI3001`, `048842` | Canonical commercial records |
| Catalogue item | `94` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `168` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `3` | Canonical firmware catalogue |
| Categories | Lighting Management, Room Controller, 0-10 V dimmer | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMDI3001` | Established identity | canonical commercial record for item `94` |
| Legrand | `048842` | Established identity | canonical commercial record for item `94` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `048842` | `3245060488420` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/9d/13/9d13d4580b63376b05737629165b360c5fa6d874d0a7e08815b210599bea706f.pdf), `048842-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | publisher product sheet | current catalogue export | `BMDI3001` two-output 1-10 V Room Controller; printed p. 1 / PDF p. 1 | [Archived original](https://archive.openwebnet-ha.org/sha256/47/95/47959cd888b93d2c1a5329cc1b5652eb72bbc3851b8b8b5dcec98c77734bf91d.pdf) | [Official source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMDI3001) |
| `048842-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact SKU/GTIN metadata retained;technical/installation downloads examined separately below;generic ETIM attributes not adopted | [Archived HTML](https://archive.openwebnet-ha.org/sha256/9d/13/9d13d4580b63376b05737629165b360c5fa6d874d0a7e08815b210599bea706f.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-2-circuits-mosaic-a-fonction-variation-ballast-1v-a-10v-avec-2-sorties-1000va-maximum) |
| `BT00497_c_IT.pdf` | Italian exact technical sheet | BT00497-c-IT;2013-11-12 | `BMDI3001`;full 3 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/41/7b/417b3e0b25fbb7e62b61ff376d0504e615f47095cee0c59094d0c2f155a6549a.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/BT00497_c_IT.pdf) |
| `F01120EN-00.pdf` | English exact technical sheet | F01120EN/00;2010-09-08 | `048842`;full 3 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/3a/75/3a751d6641f23bde1f177249ef92d837bf7a1656f6cbadd0e8a0800167afab2d.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/F01120EN-00.pdf) |
| `F01120FR-00.pdf` | French exact technical sheet | F01120FR/00;2010-09-08 | `048842`;full 3 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/8d/27/8d27b35aec620712a40f3a868252cc6cf4dc0a71742c2f864b8b3ccb0c33026e.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/F01120FR-00.pdf) |
| `LE02801AB.pdf` | Illustrated installation instructions | LE02801AB;date not printed | `048842`;full 2 pages | [Archived original](https://archive.openwebnet-ha.org/sha256/7c/33/7c33472b2c51095c6014530b7a8e16a79f4dcbd93f9f420f7d6cf01bf5bd9986.pdf) | [Publisher source](https://assets.legrand.com/pim/NP-FT-GT/LE02801AB.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply and power discrepancy | Italian technical sheet `110..230` Vac `50..60 Hz`; export and Legrand `100..240` Vac `50..60 Hz`; `3 W` standby/no-load | BT00497-c-IT, p. 1; F01120EN/FR-00, p. 1; `BMDI3001` export, p. 1 |
| Load limits at 230/110 V | Two × `4.3 A`; linear/halogen ballast `2× 1000/500 VA`; CFL ballast 2× 1000/`500 W` | BT00497-c-IT and F01120EN/FR-00, p. 1; LE02801AB, p. 1 |
| Combined limit and bus | Italian wiring explicitly IL1+IL2=`16 A` max, separate from each `4.3 A` limit; two local bus ports `200 mA` combined, upstream bus separate | BT00497-c-IT, p. 3 and export, p. 1; Legrand technical/instruction, p. 1 |
| Environment and body | `-5..45 °C`; IP20, IK04. Legrand: storage`-20..70 °C`, `330 g`; `95.5 × 172 mm` body, `207 mm` mounting extent, 49/`50 mm` dimension arrows | BT00497-c-IT, pp. 1–2; F01120EN/FR-00, pp. 1–2 |
| Wiring | Screw `2× 2.5 mm²`; Legrand analogue ≤ `1.5 mm²`, RJ45; `150 m` controller–furthest sensor, `500 m` supply–furthest product | BT00497-c-IT, pp. 1, 3; F01120EN/FR-00, pp. 1–2 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `94` | Canonical catalogue |
| Technical item | Room Controller - 2 dimming outputs 0-10 V | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `168` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `168` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `94` | `BMDI3001` | `1` | `5` | `BTicino_Undefined_Room Controller 2 Dim Outpu` |
| `1774` | `048842` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `208` | `-1` | `-1` | `-1` | `3` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `208` | `1` | `8` Dimmer actuator | Fixed/designated metadata | `895` | `8` | `561` |
| `208` | `2` | `8` Dimmer actuator | Fixed/designated metadata | `896` | `8` | `561` |
| `208` | `3` | `167` Room controller | Fixed/designated metadata | `897` | `167` | `562` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `208` | Physical configuration | `0` | Canonical firmware/mode association |
| `208` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `208` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `208` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `208` | `A` | `0..9` | `0` | A; Environment |
| `208` | `PL1` | `0..9` | `0` | PL1; PL1 - (0-9) |
| `208` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `208` | `PL2` | `0..9` | `0` | PL2; PL2 - (0-9) |
| `208` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |
| `208` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (0-4, Pul, Sla) |

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

Firmware `208` is the wildcard catalogue default with Deprecated status, not a proven installed version or current availability. Slots `1..2` are Object `8` load contexts; slot `3` is Object `167` controller MODE (stand-alone 0 / supervision 1, default 0), not another electrical output. No Virgin, slot condition or conversion is stored. Relation filters without subset rows retain the complete reusable domains rather than proving physical support for every load enum, local-button mode or timer. The reusable MIN_LEVEL_ADV default 0 lies outside 1..100. Firmware A/PL/M and the recorded physical/virtual/advanced modes are retained, but the examined Lighting Management sheets describe automatic pairing and software/remote setup; their procedures do not establish a physical configurator socket. Symbolic SLA/PUL branches are recorded as firmware values but no conversion is supplied. The catalogue title says 0-10 V while the technical load interface is 1-10 V; wiring labels 0-10 V and reusable TYPE_STANDARD are separate evidence, not proof that every installed ballast responds down to 0 V.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `208` | `8` | `981` | `HOURS` | `0..255` (entire reusable range retained) | `0` | Hours |
| `208` | `8` | `982` | `LOCAL_BUTTON` | `0` = Toggle; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` (entire reusable range retained) | `0` | Local button modality |
| `208` | `8` | `983` | `MINUTES` | `0..59` (entire reusable range retained) | `0` | Minutes |
| `208` | `8` | `984` | `SECONDS` | `0..59` (entire reusable range retained) | `30` | Seconds |
| `208` | `8` | `985` | `TYPE_LOAD` | `0` = Auto detect capacitive; `1` = Auto detect inductive; `2` = Forced capacitive; `3` = Forced inductive; `5` = Fluorescent lamps; `6` = Led lamps; `7` = Discharge lamps; `8` = Dali standard; `9` = DSI; `10` = Halogen lamp; `11` = LED trailing edge / electronic transformers; `12` = LED leading edge; `13` = CFL trailing edge; `14` = CFL leading edge (entire reusable range retained) | `0` | Type of Load |
| `208` | `8` | `986` | `TYPE_STANDARD` | `0` = 1-10V standard; `1` = 0-10V standard (entire reusable range retained) | `0` | Voltage standard |
| `208` | `8` | `2183` | `STATE_SAVING_ON_RESET` | `0` = Disabled; `1` = Enabled (entire reusable range retained) | `0` | State saving on reset |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `94` / `modobj = 168` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`8`, `167`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Local test and automatic pairing | L1/L2 buttons switch and long press adjusts load; Plug&Go at power-on, Push&Learn/software integrated setup | BT00497-c-IT, pp. 1–2; LE02801AB, p. 2 |
| Fault response | Legrand:local peripheral fault relights after 10 min; upstream bus connection fault after 50 s; capacity LED | F01120EN/FR-00, p. 1 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Wire with mains disconnected. Automatic pairing begins at power-on; BTicino distinguishes standalone and integrated bus installations and documents Plug&Go, Push&Learn and Virtual Configurator. The Legrand sheets specify remote configuration tools 88235/88230; those tool manuals and detailed sensor sheets are not incorporated. Local test buttons switch loads; holding the relevant dimming button adjusts level. The software catalogue mode associations remain distinct from these product commissioning procedures.

## Source reconciliation

Canonical mapping establishes `BMDI3001`/048842; BT00497-c-IT dated 12 November 2013 and F01120EN/FR-00 dated 8 September 2010 provide direct exact-product evidence for both references. The Italian sheet’s `110..230` V differs from the `100..240` V export/Legrand technical range and is kept scoped. Its 3-page wiring gives a 16 A aggregate label, which does not increase each 4.3 A channel limit. Catalogue “0-10 V” wording and illustrated 0-10 V terminals coexist with 1-10 V ballast interfaces. The Legrand FR/EN ratings agree; historical FR NF EN 50428 and EN IEC 60669-2-1 declarations differ and are not presented as present-day certifications. The retained HTML remains exact-SKU/GTIN evidence; generic output-power attributes do not override the load-class tables.

Catalogue interpretation is detailed under [Object configuration surfaces](#object-configuration-surfaces); these software records do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- No installed hardware observation is retained. Exact tool manuals, detailed sensor setup, Suite help, referenced drawings and broader current installation guides are unexamined; no commissioning-completion claim is made.
- Catalogue 0-10 V wording, wiring labels and reusable voltage/load settings do not by themselves establish every ballast or LED compatibility. Regional standards and load units are kept source-specific.
- Supply-range and dimension-arrow differences are preserved; no physical revision is assumed to resolve them.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `048842-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `048842` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/9d/13/9d13d4580b63376b05737629165b360c5fa6d874d0a7e08815b210599bea706f.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-2-circuits-mosaic-a-fonction-variation-ballast-1v-a-10v-avec-2-sorties-1000va-maximum); SHA-256 `9d13d4580b63376b05737629165b360c5fa6d874d0a7e08815b210599bea706f`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0071-0080-2026-10-06.md#own-dev-0079)
