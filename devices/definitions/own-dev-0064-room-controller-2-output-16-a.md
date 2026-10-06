# Room Controller - 2 outputs 16 A

## Summary

This Room Controller combines two lighting relay outputs with a supply for local bus devices. It supports automatic Plug&Go or configured Lighting Management operation, and the two outputs share a 16 A total maximum.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0064` | Project identity |
| Technical description | Room Controller - 2 outputs 16 A | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `BMSW3002`, `048841` | Canonical commercial records |
| Catalogue item | `59` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `167` | Canonical inventory |
| Firmware definition | `-1.-1.-1` | Canonical firmware catalogue |
| Declared Modules | `3` | Canonical firmware catalogue |
| Categories | Lighting Management, Room Controller, Relay actuator | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `BMSW3002` | Established identity | Catalogue item `59`; named in `U3773B`, PDF p. 1 |
| Legrand | `048841` | Established identity | canonical commercial record for item `59` |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `048841` | `3245060488413` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/e9/4b/e94ba3f62fc768aa3ba3ce0563ef00b829729725158ad16e8b0a225d824ace9a.pdf), `048841-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino General Catalogue product sheet | catalogue product sheet | current publisher catalogue | `BMSW3002` Room Controller functional and electrical summary | Original not retained; discovery/provenance only; substantive claims use retained originals | [Official product page](https://catalogo.bticino.it/prodotto/soluzioni-per-lefficienza-energetica/lighting-control---sistema-filare-bus-scs/attuatori/BTI-BMSW3002-IT) |
| `U3773B.pdf` | installation instruction sheet | U3773B01SY-09W51 | PDF pp. 1–2; first printed page marked 1/4; retained fragment covers ratings, load classes, 16 A combined diagram and 150 m bus reach; nominal pages 3–4 not retained | [Archived original](https://archive.openwebnet-ha.org/sha256/60/ae/60ae6cf3046778b4d5fcb59b99f9d59f24bfb86d9a7a2ffdd0eb1142b2e9e8c3.pdf) | [Publisher original](https://dar.bticino.com/asset/Documents/U3773B.pdf) |
| `048841-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact SKU/GTIN metadata examined; other ETIM attributes, linked downloads and prices outside the reviewed scope | [Archived HTML](https://archive.openwebnet-ha.org/sha256/e9/4b/e94ba3f62fc768aa3ba3ce0563ef00b829729725158ad16e8b0a225d824ace9a.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-2-circuits-mosaic-a-fonction-on-off-avec-2-sorties-16a) |
| `BT00308_c_IT.pdf` | Exact-product technical sheet | BT00308-c-IT; 2013-11-12 | Printed/PDF pp. 1–3; complete ratings, load classes, dimensions, setup routes and combined-load wiring | [Archived original](https://archive.openwebnet-ha.org/sha256/df/9a/df9af98f2aee6e52acbef8bd95c55f0dce667375d37e044c262085eaed50e687.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/BT00308_c_IT.pdf) |
| `BMSW3002-italian-product-sheet-IT.pdf` | Exact-product Italian catalogue export | Retrieved 2026-10-06; undated export | Printed/PDF p. 1; complete technical attributes, powered bus ports, total output current and setup; prices excluded | [Archived original](https://archive.openwebnet-ha.org/sha256/7d/2e/7d2eab5aba284f94e550587e88b1495448d204e6cf656e392895cd9862fcbfe5.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-BMSW3002) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / standby | `110..230 Vac`, `50/60 Hz`; `1.8 W` standby | BT00308-c-IT, printed/PDF pp. 1–3 |
| Environment / protection | `+5..45 °C`; IP20; IK04 | BT00308-c-IT, printed/PDF pp. 1–3 |
| Outputs / total limit | Two switched outputs; headline (1+1) × `16 A`, with wiring diagram combined `I_L1+I_L2=16 A` maximum | BT00308-c-IT, printed/PDF pp. 1–3 |
| Local-bus supply / connection | `200 mA` maximum; RJ45; supply terminals `2 × 2.5 mm²` | BT00308-c-IT, printed/PDF pp. 1–3 |
| Dimensions / mounting | `207 × 70.5 × 49 mm`; trunking, cable basket clips or false ceiling | BT00308-c-IT, printed/PDF pp. 1–3 |
| Incandescent / halogen at 230 / 110 V | `3680 / 1760 W`; `16 A` | BT00308-c-IT, printed/PDF pp. 1–3 |
| Linear fluorescent at 230 / 110 V | 10 × (`2 × 36 W`) / 5 × (`2 × 36 W`); `4.3 A` | BT00308-c-IT, printed/PDF pp. 1–3 |
| Electronic / ferromagnetic transformers at 230 / 110 V | `3680 / 1760 W` as printed; `16 A` | BT00308-c-IT, printed/PDF pp. 1–3 |
| Compact fluorescent at 230 / 110 V | `1150 / 550 VA`; `5 A` | BT00308-c-IT, printed/PDF pp. 1–3 |
| `LED` at 230 / 110 V | `1 × 500 / 1 × 250 VA`; `2.1 A` | BT00308-c-IT, printed/PDF pp. 1–3 |
| Local-bus wiring reach | `150 m` in p. 3 diagram | BT00308-c-IT, printed/PDF pp. 1–3 |
| Earlier supply / environment / transformer units | `100..240 Vac`, `50/60 Hz`; `−5..45 °C`; transformer rating `3680/1760 VA`, rather than W in BT00308-c-IT | U3773B, printed p. 1/4 / PDF p. 1 |
| Current export supply / ports | `100..240 Vac`; two local-bus ports (terminal/RJ45) sharing `200 mA` and one riser connection (terminal/RJ45); two outputs share total `16 A` at `230 Vac` | `BMSW3002`-italian-product-sheet-IT.pdf, printed/PDF p. 1 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `59` | Canonical catalogue |
| Technical item | Room Controller - 2 outputs 16 A | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `167` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `167` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `59` | `BMSW3002` | `1` | `5` | Empty in source |
| `1789` | `048841` | `2` | `5` | Empty in source |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `281` | `-1` | `-1` | `-1` | `3` | Catalogue default | Deprecated |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `281` | `1` | `6` Light actuator | Fixed/designated metadata | `994` | `6` | `600` |
| `281` | `2` | `6` Light actuator | Fixed/designated metadata | `995` | `6` | `600` |
| `281` | `3` | `167` Room controller | Fixed/designated metadata | `996` | `167` | `601` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `281` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `281` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `6` - Light actuator

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0..10` | `0` | Area |
| `PL` | `0..15` | `0` | Light point |
| `M` | `0` = Master; `11` = Slave; `15` = Master `PUL`; `16` = Slave and `PUL` | `0` | Modality |
| `LOCAL_BUTTON` | `0` = Toggle; `1` = `ON`/`OFF`; `9` = `ON` - `OFF`; `15` = Pushbutton; `18` = Timed `ON` | `0` | Local button modality |
| `DELAYED_OFF` | `0..255` | `0` | Delayed `OFF` for Slave (s) |
| `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open | `0` | Relay state on device reset |
| `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing | `0` | Load control mode |
| `HOURS` | `0..255` | `0` | Hours |
| `MINUTES` | `0..59` | `0` | Minutes |
| `SECONDS` | `0..59` | `30` | Seconds |
| `SUBTYPE` | `11` = Actuator; `1` = Lamp; `10` = Valve; `15` = Differential restart; `6` = Fan; `7` = Watering; `8` = Controlled socket; `9` = Lock | `11` | Type of load |
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

### Object `167` - Room controller

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `MODE` | `0` = Stand-alone mode; `1` = Supervision mode | `0` | Modality; Mode |

### Device-specific interpretation

Firmware `281` declares three software Modules: Light actuator 6 in slots 1/2 and Room Controller 167 in slot `3`. This agrees with two physical outputs plus a controller role, not three load channels. Object `167` `MODE=0` standalone/1 supervision defaults to 0; no slot predicates, Virgin or conversions are stored. Firmware contains only `AID` and Advanced Configuration. `STATE_RESET=0` last value/1 closed/2 open and `LOAD_CONTROL_MODE=0` with zero crossing/1 without retain their whole reusable domains. The export documents zero-crossing hardware, but these fields do not establish installed mode or a production revision.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `281` | `6` | `1104` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Relay state on device reset |
| `281` | `6` | `1871` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `59` / `modobj = 167` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`6`, `167`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Control | Two lighting outputs and local-bus supply; local buttons test the outputs | BT00308-c-IT, printed/PDF pp. 1–3 |
| Setup | Plug&Go, Push&Learn and Virtual Configurator in Lighting Management; setup procedures referenced rather than reproduced | BT00308-c-IT, printed/PDF pp. 1–3 |
| Combined-load constraint | Individual load-class limits remain subject to the combined 16 A maximum | BT00308-c-IT, printed/PDF pp. 1–3 |
| Switching technology | Zero Crossing is explicitly named in the current export | `BMSW3002`-italian-product-sheet-IT.pdf, p. 1 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

BT00308-c-IT p. 2 distinguishes the two local test buttons from setup. Use Plug&Go for the Room Controller’s automatic association, Push&Learn for learned groups or Virtual Configurator for software setup; the referenced complete commissioning guides have not been independently examined. The catalogue controller Object `MODE` is a software role field, not a substitute for those procedures. Wiring (p. 3) separates the mains loads, riser and powered local bus; the displayed 150 m bus reach and combined load limit are installation-specific manufacturer constraints.

## Source reconciliation

The exact technical sheet, U3773B and current export agree on two outputs and 200 mA local-bus supply. The c sheet specifies `110..230` Vac and `+5..45 °C`; U3773B/export specify `100..240` Vac, and U3773B says `−5..45` °C. Transformer units are W in the c sheet and VA in U3773B. These differences have no documented production/revision mapping. The combined 16 A diagram and current export resolve the earlier ambiguous per-output headline: two 16 A load classes cannot be treated as 32 A aggregate. The retained `048841` HTML supports its exact GTIN only; its other ETIM fields and linked documents are outside the examined scope.

Catalogue-specific scope, selectors, defaults and filter/conversion irregularities are detailed under [Object configuration surfaces](#object-configuration-surfaces). Those software relations do not establish additional physical capabilities or installed behavior.

## Evidence limits and open work

- Supply, temperature and transformer-unit differences remain unresolved between applicable originals.
- The Legrand identity is explicit catalogue evidence; independently examined `048841` physical sheet and release-to-hardware mapping remain unavailable.
- Linked DWG, commissioning, Push&Learn and Virtual Configurator guides are known but unexamined.
- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

- U3773B is retained as a two-PDF-page fragment whose first sheet is marked 1/4; nominal missing pages 3–4 are not claimed to have been examined. The new complete BT00308-c-IT technical sheet supplies the separate setup and installation evidence.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [`BMSW3001`/`BMSW3002` installation instruction sheet, archived original](https://archive.openwebnet-ha.org/sha256/60/ae/60ae6cf3046778b4d5fcb59b99f9d59f24bfb86d9a7a2ffdd0eb1142b2e9e8c3.pdf)

- `048841-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `048841` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/e9/4b/e94ba3f62fc768aa3ba3ce0563ef00b829729725158ad16e8b0a225d824ace9a.pdf); [publisher source](https://www.legrand.fr/pro/catalogue-archives/controleurs-faux-plafond-pour-2-circuits-mosaic-a-fonction-on-off-avec-2-sorties-16a); SHA-256 `e94ba3f62fc768aa3ba3ce0563ef00b829729725158ad16e8b0a225d824ace9a`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0061-0070-2026-10-06.md#own-dev-0064)
