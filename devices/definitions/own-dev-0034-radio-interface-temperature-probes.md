# Radio interface for temperature probes

## Summary

This radio interface brings compatible wireless temperature probes into the SCS installation. It provides two configurable channel positions, whose selected modes can represent temperature sensing or lighting-sensor functions.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0034` | Project identity |
| Technical description | Two-channel radio receiving interface for wireless temperature probes | Catalogue + official documentation |
| Commercial identities | `HC/HS/HD4577`, `L/N/NT4577` | Catalogue |
| Catalogue item | `39` - “Radio interface for temperature probes” | Implementation evidence |
| Main catalogue system | Thermoregulation / Temperature control (`id_system = 2`) | Implementation evidence |
| Additional catalogue system | Lighting / Automation (`id_system = 1`) | Implementation evidence |
| Item model / `modobj` | `23` | Implementation evidence |
| Firmware definition | `-1.-1.-1` wildcard / unspecified, firmware `239` | Implementation evidence |
| Declared Modules | `2` | Implementation evidence |
| Categories | Radio interface, Temperature control, Sensor bridge | Capability model |

## Commercial identities

| Brand / line | Reference | Catalogue record | Relationship | Evidence |
| --- | --- | ---: | --- | --- |
| BTicino - LivingLight | `L/N/NT4577` | Established identity | canonical commercial record `39`; Commercial identity of this Technical Device | Canonical catalogue |
| BTicino - Axolute | `HC/HS/HD4577` | Established identity | canonical commercial record `1966`; Commercial identity of this Technical Device | Canonical catalogue |

All listed commercial records map to the same Technical Device; catalogue ordering does not make any SKU canonical.

### EAN-13 commercial identifiers

| Reference | EAN-13 | Evidence |
| --- | --- | --- |
| `L4577` | `8012199848983` | [Archived original](https://archive.openwebnet-ha.org/sha256/4f/ae/4fae495303a9b2368b081ab504e7c2ce62f8fc8b5390a66bf6afd7bce1f2ec9a.pdf), `L4577-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `N4577` | `8012199848990` | [Archived original](https://archive.openwebnet-ha.org/sha256/88/b9/88b93a6a6b99cf9900f911f16ce97b24314a16b1e1f5c9d8589170fe65459288.pdf), `N4577-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `NT4577` | `8012199849003` | [Archived original](https://archive.openwebnet-ha.org/sha256/75/dd/75dd70f0c92e380e18effbd58454af313992f3d0511a6d37a257078c1cd4f79e.pdf), `NT4577-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HC4577` | `8012199849027` | [Archived original](https://archive.openwebnet-ha.org/sha256/8a/bb/8abb0709a13b0efc4cb996ba5154173d7e5d7fa222aed0359c30d5f0302b92ce.pdf), `HC4577-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HS4577` | `8012199849010` | [Archived original](https://archive.openwebnet-ha.org/sha256/71/27/712769ad54075bc127e09bd927f33b6afee8b415084e6c7c059d7d2097c62433.pdf), `HS4577-ean-product-sheet.pdf`, printed/PDF p. 1 |
| `HD4577` | `8012199987668` | [Archived original](https://archive.openwebnet-ha.org/sha256/f7/c7/f7c7687b4520a4b8b09f83dbee5a281eb1573c11b391ceb50b3d8f381dec54b7.pdf), `HD4577-ean-product-sheet.pdf`, printed/PDF p. 1 |

Each EAN is tied to the exact commercial reference in the cited manufacturer record. Grouped catalogue codes are expanded only into their named physical references. These source-specific commercial identifiers do not establish the installed hardware or firmware revision.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `MQ00183-c-EN` | Technical sheet | publisher revision as archived | whole document | [Archived PDF](https://archive.openwebnet-ha.org/sha256/2d/34/2d34fb8c90385159e620c4f9515267dc8b8fa3acda9471f0cc226558fab7f03c.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/MQ00183-c-EN.pdf) |
| `U1870C` | Instruction sheet | publisher revision as archived | whole document | [Archived PDF](https://archive.openwebnet-ha.org/sha256/a6/10/a610f6d8fd4aa811944d0e2c05adacda5b459571814108ee504e5074adcece9c.pdf) | [Publisher PDF](https://assets.legrand.com/pim/NP-FT-GT/U1870C.pdf) |
| BTicino `L4577` product record | Current product record | current | whole product page | - | [Publisher page](https://www.bticino.com/products/bt-l4577) |
| `L4577-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `L4577` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/4f/ae/4fae495303a9b2368b081ab504e7c2ce62f8fc8b5390a66bf6afd7bce1f2ec9a.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4577) |
| `N4577-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `N4577` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/88/b9/88b93a6a6b99cf9900f911f16ce97b24314a16b1e1f5c9d8589170fe65459288.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4577) |
| `NT4577-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `NT4577` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/75/dd/75dd70f0c92e380e18effbd58454af313992f3d0511a6d37a257078c1cd4f79e.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4577) |
| `HC4577-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HC4577` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/8a/bb/8abb0709a13b0efc4cb996ba5154173d7e5d7fa222aed0359c30d5f0302b92ce.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4577) |
| `HS4577-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HS4577` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/71/27/712769ad54075bc127e09bd927f33b6afee8b415084e6c7c059d7d2097c62433.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4577) |
| `HD4577-ean-product-sheet.pdf` | Italian manufacturer product export | Retrieved `2026-10-05`; printed record date/edition remains source-scoped | Exact `HD4577` to EAN-13 relationship at printed/PDF p. 1. Commercial-identifier scope for this update; other attributes and prices are not incorporated. | [Archived original](https://archive.openwebnet-ha.org/sha256/f7/c7/f7c7687b4520a4b8b09f83dbee5a281eb1573c11b391ceb50b3d8f381dec54b7.pdf) | [Publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4577) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `27 Vdc` | `MQ00183-c-EN` / current publisher product data |
| Current draw | `33 mA` | Current publisher product data |
| Radio frequency | `868 MHz` | Current publisher product data |
| Mounting | 2 flush-mounted modules | Current publisher product data |
| Probe channels | 2 configured channel positions | Catalogue topology + publisher family documentation |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `39` | Canonical catalogue |
| Technical item description | Radio interface for temperature probes | Canonical catalogue |
| Item family | `27` - Radio device | Canonical catalogue |
| Additional system | `1` - lighting_automation; `modobj` `23` | AS_ITEM_SYSTEM |
| Main system | `2` - thermoregulation; `modobj` `23` | AS_ITEM_SYSTEM |
| Commercial records | `2` | EN_DEVICE |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `239` | `-1` | `-1` | `-1` | `2` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `239` | `1` | `124` Radio interface for sensors (measurer T) | Fixed/designated metadata | `1333` | `124` | `693` |
| `239` | `2` | `124` Radio interface for sensors (measurer T) | Fixed/designated metadata | `1334` | `124` | `693` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

Slots `1` and `2` are both fixed Object `124`, Radio interface for sensors (measurer T). This is a two-slot instance of the same temperature-sensor-interface Object.

## Configuration modes

| Firmware | Mode ID | Catalogue mode | Description |
| ---: | ---: | ---: | --- |
| `239` | `1` | `1` | Virtual Configuration |
| `239` | `3` | `0` | Physical configuration |

The catalogue declares configuration modes 1 and 3.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `239` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `239` | `A` | `0..9` | `0` | A; Configurator A1 (0-9) |
| `239` | `PL1/N1` | `0..9` | `0` | PL1/N1; Configurator with range (0-9) PL1N1 |
| `239` | `M1` | `0..1`; `6` | `0` | M1; mode M1 not configured - Value : 0 temperature sensor - Value : 1 lighting sensor - Value : 6 |
| `239` | `A2/-` | `0..9` | `0` | A2/-; Configurator A2 (0-9) |
| `239` | `PL2/N2` | `0..9` | `0` | PL2/N2; Configurator with range (0-9) PL2N2 |
| `239` | `M2` | `0..1`; `6` | `0` | M2; mode M2 not configured - Value : 0 temperature sensor - Value : 1 lighting sensor - Value : 6 |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `A` | `0..9` | area / environment configurator |
| `PL1/N1` | `0..9` | channel 1 point / zone selector |
| `M1` | `0` / `1` / `6` | channel 1 operating mode |
| `A2/-` | `0..9` | channel 2 area selector / disabled position |
| `PL2/N2` | `0..9` | channel 2 point / zone selector |
| `M2` | `0` / `1` / `6` | channel 2 operating mode |


For each channel, `M=0` means not configured, `M=1` selects a temperature sensor and `M=6` selects a lighting sensor. The latter is retained as implementation evidence despite the product name.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `124` - Radio interface for sensors (measurer T)

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `A` | `0` | `0` | Area |
| `PL_N` | `0..9` | `0` | Light point N |
| `M` | `1`; `0` = None | `1` | Modality |


### Product interpretation and source differences

**Object `124` - Radio interface for sensors (measurer T) - product interpretation.**

**Firmware relationship.** No additional Object/Firmware range filter in the catalogue.

These are reusable Object fields; Device applicability remains governed by the firmware relationship above.

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
| `DIMENSION 1` | resolve `modobj = 23`, commercial family and dual-system mapping | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware rather than assuming wildcard catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | confirm the two fixed Object `124` sensor-interface Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | read the two configured channel addresses | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect channel `A` / `PL` / `M` selectors and preserve temperature-versus-lighting-sensor mode semantics | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Thermoregulation is the main catalogue system for the Device; the item is also associated with lighting/automation. The configured channel mode determines whether a slot represents temperature or lighting-sensor use.

## Observed behavior and corroboration

No sanitized hardware fingerprint for this exact technical item is currently retained.

## Programming

Program and validate both channel positions independently. Preserve `M` values 0/1/6 semantics and the dual-system applicability.

## Source reconciliation

Official product documentation corroborates the 4577/3455 radio-temperature role, 27 Vdc BUS supply and two-module form. The database adds two fixed Object slots and explicitly permits `M` value 6 lighting-sensor mode, which broadens the implementation model beyond the product headline.

## Evidence limits and open work

- Hardware-corroborate both slot identities and `M` value 6 behavior.
- Capture representative radio-probe traffic without retaining private installation identifiers.

## Sources

- [Device Sources](../../sources/devices/)
- [Device Database Inventory](../inventory/)
- [MQ00183-c-EN](https://archive.openwebnet-ha.org/sha256/2d/34/2d34fb8c90385159e620c4f9515267dc8b8fa3acda9471f0cc226558fab7f03c.pdf)
- [U1870C](https://archive.openwebnet-ha.org/sha256/a6/10/a610f6d8fd4aa811944d0e2c05adacda5b459571814108ee504e5074adcece9c.pdf)
- [BTicino L4577](https://www.bticino.com/products/bt-l4577)

- `L4577-ean-product-sheet.pdf`, printed/PDF p. 1: exact `L4577` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/4f/ae/4fae495303a9b2368b081ab504e7c2ce62f8fc8b5390a66bf6afd7bce1f2ec9a.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-L4577); SHA-256 `4fae495303a9b2368b081ab504e7c2ce62f8fc8b5390a66bf6afd7bce1f2ec9a`.
- `N4577-ean-product-sheet.pdf`, printed/PDF p. 1: exact `N4577` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/88/b9/88b93a6a6b99cf9900f911f16ce97b24314a16b1e1f5c9d8589170fe65459288.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-N4577); SHA-256 `88b93a6a6b99cf9900f911f16ce97b24314a16b1e1f5c9d8589170fe65459288`.
- `NT4577-ean-product-sheet.pdf`, printed/PDF p. 1: exact `NT4577` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/75/dd/75dd70f0c92e380e18effbd58454af313992f3d0511a6d37a257078c1cd4f79e.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-NT4577); SHA-256 `75dd70f0c92e380e18effbd58454af313992f3d0511a6d37a257078c1cd4f79e`.
- `HC4577-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HC4577` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/8a/bb/8abb0709a13b0efc4cb996ba5154173d7e5d7fa222aed0359c30d5f0302b92ce.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HC4577); SHA-256 `8abb0709a13b0efc4cb996ba5154173d7e5d7fa222aed0359c30d5f0302b92ce`.
- `HS4577-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HS4577` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/71/27/712769ad54075bc127e09bd927f33b6afee8b415084e6c7c059d7d2097c62433.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HS4577); SHA-256 `712769ad54075bc127e09bd927f33b6afee8b415084e6c7c059d7d2097c62433`.
- `HD4577-ean-product-sheet.pdf`, printed/PDF p. 1: exact `HD4577` / EAN-13 pair. [Archived original](https://archive.openwebnet-ha.org/sha256/f7/c7/f7c7687b4520a4b8b09f83dbee5a281eb1573c11b391ceb50b3d8f381dec54b7.pdf); [publisher source](https://catalogo.bticino.it/pdf/scheda-prodotto/BTI-HD4577); SHA-256 `f7c7687b4520a4b8b09f83dbee5a281eb1573c11b391ceb50b3d8f381dec54b7`.
