# Flush-mounted temperature central unit

## Summary

The 4695 is a temperature-control central unit for up to four zones, including its local zone. Its display provides heating and cooling management, with weekly programmes and manual, holiday or timed operating modes.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0017` | Project identity |
| Technical description | Flush-mounted four-zone temperature-control central unit | Catalogue + official documentation |
| Catalogue item | `168` - Flush mounted temperature central unit | Implementation evidence |
| Main catalogue system | Temperature control | Implementation evidence |
| Item model / `modobj` | `48` | Implementation evidence |
| Firmware definition | `1.0 build 35` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Configuration modes | Virtual, Physical, Product Programming | Implementation evidence |
| Programming connection | Serial | Implementation evidence |
| Categories | Thermoregulation, User Interface | Product and capability model |

This Device is the four-zone MyHOME temperature-control central unit sold under several BTicino and Legrand references. It provides the system-level scheduling and zone-management interface while the catalogue exposes one fixed OpenWebNet Object representing the four-zone control-unit role.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `HC/HS4695` | Shared technical item; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino - Axolute | `HD4695` | Shared technical item; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino - LivingLight | `L/N/NT4695` | Shared technical item; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino - Matix | `AM5875` | Shared technical item | Implementation evidence; direct product sheet still desirable |
| Legrand - Vela | `683090` | Shared technical item | Implementation evidence; direct product sheet still desirable |
| Legrand - Vela | `687390` | Shared technical item | Implementation evidence; direct product sheet still desirable |
| Legrand - Vela | `687890` | Shared technical item | Implementation evidence; direct product sheet still desirable |

Shared item membership establishes the common catalogue capability core. It does not prove that faceplate, market, hardware revision, or packaging is identical.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U1809F_U_EN` | User guide | revision/date not yet pinned | 4695 user operation and temperature-control behavior | [Archived original](https://archive.openwebnet-ha.org/sha256/f9/0c/f90c3dad042158152e3607dd461b143ea5c18d0dec917f9f411405f30a92d8b4.pdf) | publisher source not currently retained |
| `U1809C_Installatore_UK` | Installation / commissioning manual | revision/date not yet pinned | 4695 installation and commissioning | [Archived original](https://archive.openwebnet-ha.org/sha256/c4/46/c4461318739c49ab58078d75876aef57bff823dcaf7f964714a60f154f489dee.pdf) | publisher source not currently retained |
| `U1809B_Software_GB` | Software manual | revision/date not yet pinned | TiThermoBasic programming / firmware workflow | [Archived original](https://archive.openwebnet-ha.org/sha256/3d/10/3d1072e42a34c621e60cc455b94985116d4bc475ecfaca52df4de3bfe05f277e.pdf) | publisher source not currently retained |
| MyHOME catalogue `HPML0714` | Product catalogue | revision/date not yet pinned | System-level temperature-control context only; the `4695` family is not named. Related Arteor central units `573918` / `573919` occur on printed pp. 16, 24, 32 / PDF pp. 16, 24, 32 | [Archived MyHOME catalogue](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | publisher source not currently retained |

The 4695 documentation describes management of a temperature-control system with up to four zones and PC programming through TiThermoBasic. Where an official PDF could not be fetched by the archival runner, the official publisher URL is retained rather than substituting an unofficial mirror.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | 3 flush-mounted modules | 4695 installation documentation |
| User interface | local display and front-panel control | 4695 user / installation documentation |
| Managed installation | temperature-control system with up to 4 zones | 4695 user / installation documentation |
| Product programming | TiThermoBasic PC workflow | 4695 software documentation |

The product-level scheduling and zone-management interface is broader than the single fixed OpenWebNet Object.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `168` | Implementation evidence |
| Main system | thermoregulation / Temperature control | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `48` | Implementation evidence |
| Family | `11` | Implementation evidence |

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `1` | `0` | `35` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Catalogue applicability is not a claim that every surviving commercial variant reports this exact installed build. `DIMENSION 2` remains the authoritative installed-firmware observation when the Device exposes it.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `23` | `1` | `90` Temperature control 4 zones control unit | Fixed/designated metadata | `644` | `90` | `448` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

There is no Virgin Object for this firmware. The slot carries condition record `4163` with an empty condition string and conversion-rule reference `1000` in the implementation database. Because no Device-specific predicate is expressed there, this dossier does not invent one.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | catalogue + product documentation |
| Virtual Configuration | catalogue |
| Product Programming | catalogue + TiThermoBasic documentation |
| Serial programming connection | catalogue terminology |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `23` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `23` | `ZA` | `0..9` | `0` | ZA; ZA thermo zone address |
| `23` | `ZB` | `0..9` | `1` | ZB; ZB thermo zone address |
| `23` | `SLA` | `0..8` | `0` | `SLA`; Thermoregulation slave probe |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `ZA` | `0..9` | first thermoregulation zone digit |
| `ZB` | `0..9` | second thermoregulation zone digit |
| `SLA` | `0..8` | thermoregulation slave-probe selection |


The pair `ZA` / `ZB` is represented separately at firmware level. The reusable control-unit Object exposes the combined two-digit zone as `ZAZB`.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `90` - Temperature control 4 zones control unit

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | Zone |
| `WARM` | `0` = Disable; `1` = Enable | `0` | Winter modality; Winter mode |
| `COLD` | `0` = Disable; `1` = Enable | `0` | Summer modality; Summer mode |
| `SLA` | `0..8` | `0` | Slave number |


### Additional Device-specific interpretation

Object `90` exposes:

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `ZAZB` | `00..99` | `01` | zone |
| `WARM` | `0` Disable / `1` Enable | `0` | winter modality |
| `COLD` | `0` Disable / `1` Enable | `0` | summer modality |
| `SLA` | `0..8` | `0` | slave number |

These are catalogue validation domains. They should not be widened from product UI behavior or narrowed from one observed installation without evidence.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| `23` | `1` | `90` | `4163` | No textual predicate stored | `1000` |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| `1000` | `ZA=0; ZB=1..9` | `ZAZB=01..09` | Rule `1000` through branch `1001` |
| `1000` | `ZA=1..9; ZB=0..9` | `ZAZB=10..99` | Rule `1000` through branches `1002..1010` |
| `1000` | `ZA=0; ZB=0` | No `00` mapping stored | Do not widen the conversion from the reusable Object domain |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify item model / brand / line where exposed | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware instead of assuming catalogue `1.0.35` | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate the single fixed control-unit Module | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect the configured thermoregulation address when exposed | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect `ZA` / `ZB` / `SLA` and Object configuration where exposed | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device belongs to the temperature-control system. The catalogue and product documentation agree on a four-zone control-unit role. Generic `WHO 4` frame grammar belongs in the Functional Protocol section; this page records that the role and configuration surface apply to this Device.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

Physical configuration, virtual configuration, and product programming are all catalogue-supported. TiThermoBasic is the documented PC workflow for the 4695 family. Firmware update and project-transfer details belong to the software manual; the Device-specific invariant here is that product programming exists in addition to ordinary configurator-based setup.

## Source reconciliation

The three archived `4695` manuals establish that the single OpenWebNet control-unit Object represents a much richer four-zone thermoregulation product:

- the central unit manages heating and cooling operation for up to four zones, including the locally controlled zone;
- product programming provides multiple weekly programs and daily zone profiles rather than only a current setpoint;
- user operating states include Manual, Holiday/Holidays, Timed, `OFF` and the heating/cooling protection modes such as antifreeze or thermal protection;
- timed operation supports a finite duration up to the documented day-scale limit, while local operation also supports temperature offset/override behavior;
- fan-coil installations are explicitly supported by the product workflow;
- installation/setup includes zone association, probe configuration, system diagnostics/test procedures and total-reset behavior;
- TiThermoBasic handles project transfer and product programming in addition to ordinary configurator-based setup.

These are Device-level capabilities of the 4695 family. They do not create additional catalogue Modules, but they must be retained so Object `90` is not misread as the entirety of the product behavior.

## Evidence limits and open work

- Obtain a sanitized `DIMENSION 1` / `DIMENSION 2` / `DIMENSION 30` / `DIMENSION 32` / `DIMENSION 35` fingerprint from a known 4695-family unit.
- Locate direct official product sheets for `AM5875` and the three Vela references.
- Correlate observed installed firmware with catalogue firmware `1.0 build 35`.
- Corroborate the stored `ZA`/`ZB` → `ZAZB` conversion on installed hardware; the canonical conversion records are present.
- Preserve later document revisions separately rather than replacing the current evidence.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
