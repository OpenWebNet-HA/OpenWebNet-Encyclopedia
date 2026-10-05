# Classe 300X

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0050` | Project identity |
| Technical description | Classe 300X | Canonical catalogue plus reconciled publisher sources |
| Commercial identities | `344742`, `344743`, `344745`, `344746` | Canonical commercial records |
| Catalogue item | `2321` | Canonical catalogue |
| Main catalogue system | Integration function | Canonical catalogue |
| Item model / `modobj` | `140` | Canonical inventory |
| Firmware definition | `1.0.1` | Canonical firmware catalogue |
| Declared Modules | `2` | Canonical firmware catalogue |
| Categories | Video door entry, Wi-Fi, Indoor unit, Integration | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `344742` | established catalogue identity for item `2321` | canonical commercial record |
| BTicino | `344743` | established catalogue identity for item `2321` | canonical commercial record |
| BTicino | `344745` | established catalogue identity for item `2321` | canonical commercial record |
| BTicino | `344746` | established catalogue identity for item `2321` | canonical commercial record |

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `344742` | `8005543781326` | [Archived original](https://archive.openwebnet-ha.org/sha256/f0/d9/f0d94fbeddba68f0abd383cd37d8c2492f9e73551f92ff3f6fa9f73931c8ea29.pdf), `344742-ean-product-sheet.pdf`, printed/PDF p. 2 |
| `344743` | `8005543781388` | [Archived original](https://archive.openwebnet-ha.org/sha256/3a/60/3a60db2122dea89843ea6bc35b6d7a2f2fd1c9a15d7cddf432c8013a49eefbd5.pdf), `344743-ean-product-sheet.pdf`, printed/PDF p. 2 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| BTicino `344742` product page | product page | current product family | Current Classe 300X connected indoor-unit functions and documentation links | Not applicable - web page | [Official product page](https://www.bticino.com/products/bt-344742) |
| `FIS_C300X_1` | technical data sheet | current publisher copy | `344742` / `344743` / `344745` / `344746` supply, Wi-Fi and teleloop electrical data | [Archived original](https://archive.openwebnet-ha.org/sha256/23/ae/23aed16981142cc869be0c0d0e10c8589c4e1a26af20303438256cfc2cc622d6.pdf) | [Official source](https://dar.bticino.it/asset/Documents/FIS_C300X_1.pdf) |
| `ST-00002362-EN` | technical sheet | current publisher copy | `344745` / `344746` connected video internal units with inductive loop | [Archived original](https://archive.openwebnet-ha.org/sha256/f5/0c/f50c64daa65dd92a67193c86524aed07e0826ab8d6249b449014435ad469fd21.pdf) | [Official source](https://assets.legrand.com/pim/NP-FT-GT/ST-00002362-EN.pdf) |
| `344742-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `344742` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/f0/d9/f0d94fbeddba68f0abd383cd37d8c2492f9e73551f92ff3f6fa9f73931c8ea29.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344742) |
| `344743-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `344743` to EAN-13 relationship at printed/PDF p. 2. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/3a/60/3a60db2122dea89843ea6bc35b6d7a2f2fd1c9a15d7cddf432c8013a49eefbd5.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344743) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | `7 inch` horizontal LCD touchscreen, `1024 x 600` | Current BTicino Classe 300X product documentation |
| SCS supply | `20..27 Vdc`; `22..27 Vdc` with active inductive loop | `FIS_C300X_1` |
| Wi-Fi | `2.4 GHz` and `5 GHz`; `802.11 b/g/n/ac/ax` in current product documentation | `FIS_C300X_1` |
| Variants | `344742` light, `344743` dark, `344745` light with teleloop, `344746` dark with teleloop | Current BTicino/Legrand product documentation |
| System role | Connected 2-wire hands-free video internal unit with remote/app functions | Current BTicino product page |
| SCS standby / operation absorption | Maximum `38 mA` / `550 mA` | `FIS_C300X_1`, PDF p. 8 |
| Additional supply, terminals `1-2` | `27 Vdc` | Same source, PDF p. 8 |
| Additional-supply absorption | Maximum `265 mA`; `320 mA` with active inductive loop | Same source, PDF p. 8; inductive-loop variants `344745` / `344746` |
| Terminal cable capacity | `2 x 1 mm²` per terminal | Same source, PDF p. 8 |
| Operating temperature | `5..40 °C` | Same source, PDF p. 8 |
| Wi-Fi security | WPA / WPA2 / WPA3 | Same source, PDF p. 8; source revision scope retained |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `2321` | Canonical catalogue |
| Technical item | Classe 300X | Canonical catalogue |
| Main system | Integration function | Canonical catalogue |
| Item model / `modobj` | `140` | Canonical inventory |
| Commercial records | `4` | Canonical catalogue |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `892` | `1` | `0` | `1` | `2` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `892` | `1` | `32` Colors Touch Screen | Fixed/designated metadata | `4506` | `32` | `2014` |
| `892` | `2` | `154` Internal Unit | Fixed/designated metadata | `4507` | `154` | `2015` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue interpretation |
| --- | --- | --- |
| `892` | Product Programming | supported configuration route for this Device family |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `892` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `32` - Colors Touch Screen

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `LAN_IP_ADDRESS` | `###.###.###.###` = Local IP address | `192.168.1.35` (publisher catalogue documentation default) | Local IP address |
| `FW_VER` | `######` = Firmware version | `3.0.0` | Firmware version |
| `SYSADDRESS` | `######` = Univocal code | `1` | Univocal code |


### Object `154` - Internal Unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N` | `0..3999` | `0` | Address |
| `P` | `0..95` | `0` | Associated external unit |
| `HAND_FREE` | `0` = Disable; `1` = Enable | `0` | HAND_FREE |
| `PRO_STUDIO` | `0` = Disable; `1` = Enable | `0` | Professional Studio |
| `DOOR_STATE` | `0` = Disable; `1` = Enable | `0` | Door state display |
| `PEOPLE_S` | `0` = No; `1` = ?; `2` = ? | `0` | PeopleSearching |
| `MENU_PRE` | `0..99` | `0` | MenuPreset |
| `RING_T_OUT` | `1..30` | `10` | RingTimeOut |
| `CALL_T_OUT` | `10..180` | `30` | Call timeout |
| `PE_T_OUT` | `3..90` | `6` | EUConnectionTimeOut |
| `PI_T_OUT` | `3..90` | `18` | IUConnectionTimeOut |
| `TEL_T_OUT` | `3..180` | `90` | TelConnectionTimeout |
| `ASS_SWITCH` | `0..95` | `0` | AssociatedSwitchboard |
| `BEEP` | `0` = Disable; `1` = Enable | `0` | BEEP |
| `IS_SLAVE` | `0` = Not slave; `1` = Slave | Not specified in source | Slave |
| `DOSA_CALL` | `0` = Enable; `1` = Disable | `0` | Forward incoming call to ethernet |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `2321` / `modobj = 140` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`32`, `154`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Connected video-door-entry indoor unit with SCS/2-wire and network-facing functions. Canonical firmware/Object applicability on this page remains tied to the catalogue snapshot, not inferred from newer current-product firmware.

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

Programming must select the applicable firmware, resolve active Module/Object relationships through catalogue conditions and filters, and preserve the documented configuration-mode boundary. Product-programmed Devices should not be reduced to generic physical-configurator semantics.

## Source reconciliation

Current publisher material confirms the four commercial references and differentiates the teleloop variants. Because current Classe 300X documentation postdates the canonical MyHOME Suite catalogue snapshot, current electrical/product facts are kept separate from the catalogue's firmware 1.0.1 and Object model.

## Evidence limits and open work

- Archive the identified publisher documents locally where licensing and repository policy allow.
- Capture a sanitized hardware fingerprint covering identity, firmware, Modules, addressing and configuration.
- Corroborate relation filters and condition-selected topology against MyHOME Suite and controlled hardware observations.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- `344742-ean-product-sheet.pdf`, printed/PDF p. 2: exact `344742` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/f0/d9/f0d94fbeddba68f0abd383cd37d8c2492f9e73551f92ff3f6fa9f73931c8ea29.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344742); SHA-256 `f0d94fbeddba68f0abd383cd37d8c2492f9e73551f92ff3f6fa9f73931c8ea29`.
- `344743-ean-product-sheet.pdf`, printed/PDF p. 2: exact `344743` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/3a/60/3a60db2122dea89843ea6bc35b6d7a2f2fd1c9a15d7cddf432c8013a49eefbd5.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-344743); SHA-256 `3a60db2122dea89843ea6bc35b6d7a2f2fd1c9a15d7cddf432c8013a49eefbd5`.
