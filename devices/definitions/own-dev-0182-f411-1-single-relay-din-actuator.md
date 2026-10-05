# F411/1 single-relay DIN actuator

## Summary

F411/1 is a single-load SCS relay actuator for DIN installation. It provides local load control and can follow a master actuator, serve a bell pushbutton function or delay a slave’s switch-off.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0182` | Project identity |
| Technical description | F411/1 single-relay DIN actuator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `F411/1` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1594` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Automation | Main system association |
| Item model / `modobj` | `128` | Main association; independent of project ID |
| Firmware definition | `171` | Catalogue firmware IDs; version / build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | Actuators | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `F411/1` | Established catalogue identity | Manufacturer database commercial record `1594` explicitly links this SKU to item `1594` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `bticino-historical-comfort-manufacturer-guide.pdf` | BTicino technical guide on educational mirror | `Publication date and original publisher download URL unestablished` | Printed pp. 60-61 / PDF pp. 61-62: exact F411/1 and F411/1FL ratings, relay roles and physical selector modes; intact manufacturer guide from an educational mirror. | [Archived original](https://archive.openwebnet-ha.org/sha256/ef/56/ef567b87586483244a5c076aba822ffcf81c77ccedde472de94cf7eb843d4448.pdf) | [Manufacturer guide on educational mirror](https://leonardocanducci.org/wiki/tp3/_media/guida_myhome_bticino.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | Item `1594`: all firmware / commercial / system/Object/Module/Virgin / field / filter / mode associations | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply | `27 Vdc` | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |
| Maximum current draw | `13.5 mA` | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |
| Historical load rating | `6 A resistive or incandescent; 2 A cosφ 0.5 ferromagnetic transformers` | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |
| Relay | `One two-way relay` | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |
| Mounting | `2 DIN modules` | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |
| Controls / groups | `Local micro-button and LED; G1/G2/G3 sockets; text describes two or three groups` | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1594` | Canonical catalogue |
| Technical item description | Actuator with 1 relay DIN | Canonical catalogue |
| Item family | Source placeholder description `0`; key `2` | Canonical catalogue |
| Main system | Automation; key `1` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `128` | `AS_ITEM_SYSTEM` |
| Commercial record count | `1` | `EN_DEVICE` |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `171` | `-1` | `-1` | `-1` | `1` | Catalogue default | Official |

Version / revision / build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `171` | `1` | `6` Light actuator | Fixed / designated metadata | `602` | `6` | `417` |

Module slot is the Device-local placement, not a database row identifier. Fixed / designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `171` | Virtual Configuration | `1` | Association key `1` |
| `171` | Physical configuration | `0` | Association key `3` |

No connection associations are stored for these firmware definitions. This does not negate a documented route through an external gateway.

### Published settings and procedures

Physical selectors, application limits and procedures are tied to the cited document generation. They do not replace the Firmware-specific canonical domains below. A reusable field is not a physical selector.

| Setting / operation | Published meaning or limit | Evidence |
| --- | --- | --- |
| `M=SLA` | Slave receives same-address master commands | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |
| `M=PUL` | Bell-pushbutton role; ignores room / general commands | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |
| `M=1` / 2 / 3 / 4 | Slave `OFF` delay 1 / 2 / 3 / 4 minutes; master switches off immediately | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |
| Local micro-button | Local load command or test | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |
| G sockets | F411/1: G1/G2/G3; F411/1FL prose / front view: G1/G2; mode diagram additionally labels G3 | `bticino-historical-comfort-manufacturer-guide.pdf` printed p. 60 / PDF p. 61 |

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `171` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `171` | `A` | `0..9` | `0` | A; Enviroment |
| `171` | `PL` | `0..9` | `0` | PL; Light Point |
| `171` | `M` | `0..4`; `11` = `SLA`; `15` = `PUL` | `0` | M; Mode (1-4, Pul, Sla) |
| `171` | `G1` | `0..9` | `0` | G1; G1 - (0-9) |
| `171` | `G2` | `0..9` | `0` | G2; G2 - (0-9) |
| `171` | `G3` | `0..9` | `0` | G3; G3 - (0-9) |

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

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `171` | `1` | `6` | `4147` | No textual predicate stored | `1` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `171` | `6` | `383` | `STATE_RESET` | `0` = Restore last value; `1` = Closed; `2` = Open (entire reusable range retained) | `0` | Per energy management (State on Reset) |
| `171` | `6` | `1863` | `LOAD_CONTROL_MODE` | `0` = With zero crossing; `1` = Without zero crossing (entire reusable range retained) | `0` | Load_control_mode |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1` | `M=0` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=1` | `DELAYED_OFF` = `60`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=2` | `DELAYED_OFF` = `120`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=3` | `DELAYED_OFF` = `180`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=4` | `DELAYED_OFF` = `240`; `LOCAL_BUTTON` = `0`; `M` = `0` | `1` |
| `1` | `M=I/O` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `9`; `M` = `0` | `1` |
| `1` | `M=PUL` | `DELAYED_OFF` = `0`; `LOCAL_BUTTON` = `0`; `M` = `15` | `1` |
| `1` | `M=SLA` | `LOCAL_BUTTON` = `0`; `M` = `11` | `1` |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `128` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
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
| `6` - Light actuator | Only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue association |

These are alternative catalogue-derived roles, not proof that every candidate is simultaneously configured. A user interface may control remote subsystems without instantiating their Objects locally. Main system / model mappings are not WHO values; diagnostic transport and exact runtime support remain uncorroborated. See [Functional Protocol](../../functional/) for canonical semantics.

### Reusable Object-system associations

These are complete explicit catalogue associations for the candidate Objects. Multiple system rows are reusable metadata; they do not establish that the installed product has every corresponding subsystem. Catalogue system keys are independent of functional `WHO` values.

| External Object / role | Catalogue system | Catalogue system key | Scope |
| --- | --- | --- | --- |
| `6` - Light actuator | Automation | `1` | Reusable `AS_OBJECT_SYSTEM` relationship; active Firmware/Object remains independently resolved |

No `AS_OBJECT_FUNCTION` special-function association is stored for these Objects.

### Related functional reference families

The correspondence below is a semantic cross-reference based on the named role and the canonical functional reference; it does not assert captured frames or support for every operation.

| Catalogue role | Related canonical reference | Evidence limit |
| --- | --- | --- |
| `6` | [Lighting](../../functional/who-1-lighting/) | Related canonical semantics for the named role; exact configured operation and runtime transport remain to be corroborated |

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

The historical manufacturer guide documents physical `A`, `PL`, `M` and group sockets. A slave uses `M=SLA` and the master’s address. `M=PUL` supplies the bell pushbutton function and ignores room / general commands. Physical `M=1,2,3,4` delays the corresponding slave `OFF` by 1, 2, 3, 4 minutes while the master turns off immediately. A single relay cannot implement the two-relay interlocked mode. Software capability is separately established by the canonical Firmware modes, not retrospectively attributed to this historical guide.

Physical selectors and software domains are separate evidence. Apply the exact Firmware restrictions in the catalogue tables; a reusable default outside a filter remains an explicit catalogue inconsistency, without an inferred replacement. Registered paths and package labels are source associations, not verified payload encoding. The generic session / validation method remains in [Programming](../../programming/).

## Source reconciliation

The retained document is an intact BTicino manufacturer guide obtained from an educational mirror; its original publisher download URL and publication date are not established. The exact F411/1 page specifies 6 A resistive, unlike later F411/1N and F411/1NC references. Their 16 A ratings are not transferred to this SKU. Historical physical settings and the later software catalogue are separate evidence scopes.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `bticino-historical-comfort-manufacturer-guide.pdf` | Printed pp. 60-61 / PDF pp. 61-62: exact F411/1 and F411/1FL ratings, relay roles and physical selector modes; intact manufacturer guide from an educational mirror. |

## Evidence limits and open work

A current exact-product sheet, production-specific ratings, terminal capacity, temperature and enclosure protection remain documentation gaps. The SKU identity is established by the explicit catalogue record.

No installed hardware revision or microcontroller fingerprint is retained. Diagnostic candidates and manufacturer operating descriptions are source evidence, not measured responses. Catalogue extraction is complete for this item; further source discovery and runtime corroboration remain partial.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial / system / firmware / build associations, reusable fields and their ranges / defaults, slot/Object/Virgin relationships, every attached filter / condition / conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

### Retained original fingerprints

All incorporated originals were checked against the public archive by SHA-256 and byte length. Their manifest registrations were pushed on main before incorporation; previously registered originals were reused by fingerprint.

| Original | SHA-256 | Retention / size |
| --- | --- | --- |
| `bticino-historical-comfort-manufacturer-guide.pdf` | `ef567b87586483244a5c076aba822ffcf81c77ccedde472de94cf7eb843d4448` | 4331445 bytes; [archived original](https://archive.openwebnet-ha.org/sha256/ef/56/ef567b87586483244a5c076aba822ffcf81c77ccedde472de94cf7eb843d4448.pdf) |
