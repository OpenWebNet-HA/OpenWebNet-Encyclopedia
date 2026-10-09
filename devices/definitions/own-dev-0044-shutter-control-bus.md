# Shutter control bus

## Summary

This SCS shutter control provides UP, DOWN and STOP keys, position feedback and preset recall when paired with the documented advanced shutter actuators. It supports single-actuator, room, group and general commands, with a reference actuator providing feedback for collective control.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0044` | Project identity |
| Technical description | Dedicated advanced shutter control with preset and reference-actuator support | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `H4660M2`, `LN4660M2`, `AM5860M2`, `067558` | Canonical commercial records |
| Catalogue item | `1579` | Canonical catalogue |
| Main catalogue system | Automation | Canonical catalogue |
| Item model / `modobj` | `46` | Canonical catalogue |
| Firmware definition | `205 / -1.-1.-1` | Canonical catalogue |
| Declared Modules | `1` | Firmware catalogue |
| Categories | Automation, Shutters, Control | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4660M2` | established catalogue identity for item `1579` | canonical commercial record |
| BTicino - LivingLight | `LN4660M2` | established catalogue identity for item `1579` | canonical commercial record |
| BTicino - Matix | `AM5860M2` | established catalogue identity for item `1579` | canonical commercial record |
| Legrand - Céliane | `067558` | established catalogue identity for item `1579` | canonical commercial record |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `H4660M2` | `8005543478264` | [Archived original](https://archive.openwebnet-ha.org/sha256/3a/8b/3a8bdf20830b5d0ffc171af349457b46f8be2701fa29b785b45257879093da03.pdf), `H4660M2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `LN4660M2` | `8005543478257` | [Archived original](https://archive.openwebnet-ha.org/sha256/5f/c1/5fc1b27784f5ac3fe531a5cfc84e6267485f99051bf5fec044516240bdc8eb56.pdf), `LN4660M2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `AM5860M2` | `8005543477946` | [Archived original](https://archive.openwebnet-ha.org/sha256/77/ae/77aeb8583854b8350a6bbd571052568a55ec703063d9c4a3d3dd93ef85e7d5f6.pdf), `AM5860M2-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `067558` | `3245060675585` | [Archived HTML](https://archive.openwebnet-ha.org/sha256/8f/3b/8f3b48ee90ef8ea6256908796297009d83e98564277bb45fbdcbeea9f1337c08.pdf), `067558-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| AUTOMATISME | technical/system documentation | revision/date as printed | Advanced shutter control including H/LN4660M2 and AM5860M2 | [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/AUTOMATISME.pdf) |
| `H4660M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4660M2` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined; reference and revision limits retained; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/3a/8b/3a8bdf20830b5d0ffc171af349457b46f8be2701fa29b785b45257879093da03.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4660M2) |
| `LN4660M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4660M2` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined; reference and revision limits retained; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/5f/c1/5fc1b27784f5ac3fe531a5cfc84e6267485f99051bf5fec044516240bdc8eb56.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4660M2) |
| `AM5860M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `AM5860M2` to EAN-13 relationship at printed/PDF p. 1. Exact SKU/EAN and applicable technical attributes examined; reference and revision limits retained; prices not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/77/ae/77aeb8583854b8350a6bbd571052568a55ec703063d9c4a3d3dd93ef85e7d5f6.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5860M2) |
| `067558-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067558` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Exact SKU/GTIN metadata examined; other technical attributes, linked downloads and prices are outside this review scope. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/8f/3b/8f3b48ee90ef8ea6256908796297009d83e98564277bb45fbdcbeea9f1337c08.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/commande-myhome-up-celiane-specifique-pour-gestion-avancee-de-moteurs) |
| `MQ00591_c_EN.pdf` | Exact-product technical sheet | MQ00591-c-EN; 2014-06-09 | Printed/PDF pp. 1–3; all four variants, addressing/modes, preset and LED adjustment | [Archived original](https://archive.openwebnet-ha.org/sha256/ac/33/ac33204e4e677fd8178fcb01cfa8c6a2253819b273bfa956c3916a9d95e5a567.pdf) | [Publisher source](https://dar.bticino.com/asset/Documents/MQ00591_c_EN.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Supply / current / environment | Nominal `27 Vdc`; operating `18..27 Vdc`; maximum standby `7 mA`; `0..40 °C` | MQ00591-c-EN p. 1 |
| Size / interface | Two flush-mounted modules; three front keys and three bicolor LEDs, rear configuration key and bus | Same source |
| Compatibility | Dedicated to F401, H/LN4661M2 and AM5861M2 advanced actuators | Same source; no motor-output relay rating inferred for this control |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1579` | Canonical catalogue |
| Technical item description | Shutter control bus | Canonical catalogue |
| Main system | Automation | Canonical catalogue |
| Item model / `modobj` | `46` | Canonical catalogue |
| Commercial records | `4` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Automation | `46` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Automation | private riser | Canonical item/bus relationship |
| Automation | local bus | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `1624` | `H4660M2` | `1` | `2` | `Shutter management command` |
| `1845` | `LN4660M2` | `1` | `4` | Empty in source |
| `1846` | `AM5860M2` | `1` | `3` | Empty in source |
| `1919` | `067558` | `2` | `13` | `Legrand_Celiane_Shutter management command` |

All these records are visible, non-dependent and not marked as gateways; visibility_type is empty. These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `205` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

No firmware parameter-file association is stored for this item.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `205` | `1` | `37` Shutter control | Fixed/designated metadata | `663` | `529` | `459` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `205` | Physical configuration | `0` | Canonical firmware/mode association |
| `205` | Virtual Configuration | `1` | Canonical firmware/mode association |
| `205` | Advanced Configuration | `2` | Canonical firmware/mode association |

No firmware/connection association is stored; this does not imply that the physical Device lacks a bus connector.
Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `205` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `205` | `A` | `0..9`; `12` = `GEN`; `13` = `GR`; `14` = `AMB` | `0` | A; Environment (0-9 `GEN`,`GR`,`AMB`) |
| `205` | `PL` | `0..9` | `0` | PL; Light Point |
| `205` | `M` | `0..2`; `12` = `UP/DOWN`; `13` = `UP/DOWN` monostable | `0` | M; Mode (SU_GIU, Su_GIU_M, 1,2) |
| `205` | `PRE` | `0..9` | `0` | PRE; Shutter management preset number |
| `205` | `AR` | `0..9` | `0` | Ar; Environment referent address |
| `205` | `PLR` | `0..9` | `0` | PLr; Light Point referent address |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `37` - Shutter control

Catalogue Object key `529` maps to external Object `37`.

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `0` = Bistable control; `1` = Monostable control; `2` = Blades control and bistable; `3` = Bistable and blades control | `0` | Modality; Mode (0,1,2,3) |
| `ADDR_TYPE` | `0` = Point to point; `1` = Area; `2` = Group; `3` = General | `0` | Addressing type; See Automation System Addressing |
| `A` | `0..10` | `0` | Area; See Automation System Addressing |
| `PL` | `0..15` | `0` | Light point; See Automation System Addressing |
| `G1` | `1..255` | `1` | Group 1; See Automation System Addressing |
| `INST_LEV` | `0` = Private riser; `1..15` = Local bus with matching number; `16` = Standard | `16` | Installation level; See Automation System Addressing |
| `DEST_LEV` | `0` = Private riser; `1` = Local bus 1; `2` = Local bus 2; `3` = Local bus 3; `4` = Local bus 4; `5` = Local bus 5; `6` = Local bus 6; `7` = Local bus 7; `8` = Local bus 8; `9` = Local bus 9; `10` = Local bus 10; `11` = Local bus 11; `12` = Local bus 12; `13` = Local bus 13; `15` = Local bus 15; `16` = All systems | `0` | Destination level; See Automation System Addressing |
| `A_R` | `0..10` | `0` | Area of reference actuator |
| `PL_R` | `0..15` | `0` | Light point of reference actuator |
| `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety | `1` | Priority; Shutter management command priority |
| `PRE` | `1..9`; `0` = None | `0` | Preset; Shutter management preset number |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `205` | `37` | `581` | `PRIORITY` | `0` = Low; `1` = Medium; `2` = High; `3` = Safety (entire reusable range retained) | `1` | Priority |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | resolve item `1579` / `modobj = 46` identity | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate applicable firmware tuple while preserving wildcard sentinels | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate item-specific Module/Object topology `37` | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after active Object/system context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration against firmware/Object filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| Addressing | Physical point `A/PL=1..9`; software `A=0..10` / `PL=0..15`. Room AMB, group GR and general GEN; reference Ar/PLr for feedback/preset on multi-actuator control | MQ00591-c-EN p. 2 |
| Operation | Arrow bistable; arrow-M monostable; M1 blade then bistable for hold>1.5 s; M2 bistable then blade for hold>1.5 s | Same source |
| Preset | Pre `1..9` recalls `10..90`% opening; absent disables preset. STOP recalls preset at rest and stops movement in motion | Same source pp. 1–3 |
| Levels / groups | Software installation local `1..15`, private riser or standard; physical destination `I=1..9/CEN/0` means local/riser/whole system; `G1=1..9` physical / `1..255` software membership | Same source p. 2; catalogue omissions reconciled below |

## Observed behavior and corroboration

No sanitized hardware fingerprint or Device-specific protocol capture is currently retained for this exact technical item.

## Programming

To save a custom preset, move to the required opening with UP/DOWN, then hold STOP for at least 10 seconds; the actuator stores it and UP/DOWN LEDs confirm for 2 seconds. Preset feedback for a collective command requires the configured reference actuator (MQ00591-c-EN pp. 2–3).

For LED brightness, hold the configuration key at least 2 seconds; the levels cycle every 2 seconds through 30%, 60% default, 0%, 100%; release at the chosen level (p. 3). The sheet’s Type 2/Pre 9 third-limit discussion applies to the paired actuator, not a new control TYPE socket.

## Source reconciliation

The exact technical sheet establishes the control/actuator boundary and published software/physical address differences. Existing exact Italian exports corroborate nominal 27V, 7 mA and two modules. The catalogue has no relation-specific conversion reconciling raw M to Object `37` M; numerical similarity cannot replace that missing map.

Firmware `205` M encodes 12/13 for arrow bistable/monostable and 1/2 for combined blade modes, while Object `37` M uses 0/1/2/3; no stored conversion establishes the correspondence. Firmware A/PL/AR/PLR`0..9` is narrower than reusable area `0..10`/lightpoint `0..15` and the sheet's software domains. Object `37` DEST_LEV omits 14 although the installation-level enum includes it; do not fill the hole. Catalogue stores no firmware G1 or I physical socket despite publisher configuration entries. Filter `581` preserves four priorities. The control sheet's Type 2/Pre 9 discussion concerns the associated actuator; this control has no TYPE socket.

## Evidence limits and open work

- Applicable Suite function-help revisions and the missing destination 14 enum mapping remain unexamined/unresolved.
- No retained capture verifies feedback, preset selection or command priority behavior.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)

- `H4660M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4660M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/3a/8b/3a8bdf20830b5d0ffc171af349457b46f8be2701fa29b785b45257879093da03.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4660M2); SHA-256 `3a8bdf20830b5d0ffc171af349457b46f8be2701fa29b785b45257879093da03`.
- `LN4660M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4660M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/5f/c1/5fc1b27784f5ac3fe531a5cfc84e6267485f99051bf5fec044516240bdc8eb56.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4660M2); SHA-256 `5fc1b27784f5ac3fe531a5cfc84e6267485f99051bf5fec044516240bdc8eb56`.
- `AM5860M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `AM5860M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/77/ae/77aeb8583854b8350a6bbd571052568a55ec703063d9c4a3d3dd93ef85e7d5f6.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5860M2); SHA-256 `77aeb8583854b8350a6bbd571052568a55ec703063d9c4a3d3dd93ef85e7d5f6`.

- `067558-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067558` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/8f/3b/8f3b48ee90ef8ea6256908796297009d83e98564277bb45fbdcbeea9f1337c08.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/commande-myhome-up-celiane-specifique-pour-gestion-avancee-de-moteurs); SHA-256 `8f3b48ee90ef8ea6256908796297009d83e98564277bb45fbdcbeea9f1337c08`.

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0041-0050-2026-10-06.md#own-dev-0044)
