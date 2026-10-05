# Shutter control bus

## Summary

This dedicated SCS shutter control sends movement and preset commands to a separate shutter actuator. Reference-actuator synchronization lets its controls follow the configured shutter, including advanced preset-position operation.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0044` | Project identity |
| Technical description | Dedicated advanced shutter control with preset and reference-actuator support | Canonical catalogue plus reconciled Device sources |
| Commercial identities | `H4660M2`, `LN4660M2`, `AM5860M2`, `067558` | Canonical commercial records |
| Catalogue item | `1579` | Implementation evidence |
| Main catalogue system | Automation | Implementation evidence |
| Item model / `modobj` | `46` | Implementation evidence |
| Firmware definition | `205 / -1.-1.-1` | Implementation evidence |
| Declared Modules | `1` | Firmware catalogue |
| Categories | Automation, Shutters, Control | Capability model |

Dedicated advanced shutter control with preset and reference-actuator support.

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
| `H4660M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `H4660M2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/3a/8b/3a8bdf20830b5d0ffc171af349457b46f8be2701fa29b785b45257879093da03.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4660M2) |
| `LN4660M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `LN4660M2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/5f/c1/5fc1b27784f5ac3fe531a5cfc84e6267485f99051bf5fec044516240bdc8eb56.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4660M2) |
| `AM5860M2-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `AM5860M2` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/77/ae/77aeb8583854b8350a6bbd571052568a55ec703063d9c4a3d3dd93ef85e7d5f6.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5860M2) |
| `067558-ean-publisher-page.html` | Original manufacturer HTML commercial record | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `067558` to EAN-13 relationship at HTML product record, SKU/GTIN metadata and EAN/Gencode field. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived HTML](https://archive.openwebnet-ha.org/sha256/8f/3b/8f3b48ee90ef8ea6256908796297009d83e98564277bb45fbdcbeea9f1337c08.pdf) | [Publisher source](https://www.legrand.fr/pro/catalogue/commande-myhome-up-celiane-specifique-pour-gestion-avancee-de-moteurs) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Physical configurator positions | A, PL, Ar, PLr, M, Pre | Published installation documentation / physical-device reconstruction |
| Actuator output | None - dedicated control Device | Catalogue Object model and publisher guide |
| Advanced behavior | Reference-actuator synchronization and preset-position control | Publisher guide |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1579` | Implementation evidence |
| Technical item description | Shutter control bus | Implementation evidence |
| Main system | Automation | Implementation evidence |
| Item model / `modobj` | `46` | Implementation evidence |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `205` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

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

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `205` | Physical configuration | supported route for this Device family |
| `205` | Virtual Configuration | supported route for this Device family |
| `205` | Advanced Configuration | supported route for this Device family |

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

Advanced shutter control with reference-actuator and preset support; no local motor output.

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
- [Archived original](https://archive.openwebnet-ha.org/sha256/dc/0a/dc0ab523bbdba359aa2c2bb56a0e581755ff51476c0e21cef8e866310cf16092.pdf)

- `H4660M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `H4660M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/3a/8b/3a8bdf20830b5d0ffc171af349457b46f8be2701fa29b785b45257879093da03.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-H4660M2); SHA-256 `3a8bdf20830b5d0ffc171af349457b46f8be2701fa29b785b45257879093da03`.
- `LN4660M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `LN4660M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/5f/c1/5fc1b27784f5ac3fe531a5cfc84e6267485f99051bf5fec044516240bdc8eb56.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-LN4660M2); SHA-256 `5fc1b27784f5ac3fe531a5cfc84e6267485f99051bf5fec044516240bdc8eb56`.
- `AM5860M2-ean-product-sheet.pdf`, printed/PDF p. 1: exact `AM5860M2` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/77/ae/77aeb8583854b8350a6bbd571052568a55ec703063d9c4a3d3dd93ef85e7d5f6.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-AM5860M2); SHA-256 `77aeb8583854b8350a6bbd571052568a55ec703063d9c4a3d3dd93ef85e7d5f6`.

- `067558-ean-publisher-page.html`, HTML product record, SKU/GTIN metadata and EAN/Gencode field: exact `067558` / EAN-13 pair. [Archived HTML](https://archive.openwebnet-ha.org/sha256/8f/3b/8f3b48ee90ef8ea6256908796297009d83e98564277bb45fbdcbeea9f1337c08.pdf); [publisher source](https://www.legrand.fr/pro/catalogue/commande-myhome-up-celiane-specifique-pour-gestion-avancee-de-moteurs); SHA-256 `8f3b48ee90ef8ea6256908796297009d83e98564277bb45fbdcbeea9f1337c08`.
