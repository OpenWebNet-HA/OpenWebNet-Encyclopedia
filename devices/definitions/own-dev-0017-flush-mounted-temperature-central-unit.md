# Flush-mounted temperature central unit

## Summary

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
| BTicino Axolute | `HC/HS4695` | Shared technical item; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino Axolute | `HD4695` | Shared technical item; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino L/N/NT | `L/N/NT4695` | Shared technical item; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino Matix | `AM5875` | Shared technical item | Implementation evidence; direct product sheet still desirable |
| Legrand Vela | `683090` | Shared technical item | Implementation evidence; direct product sheet still desirable |
| Legrand Vela | `687390` | Shared technical item | Implementation evidence; direct product sheet still desirable |
| Legrand Vela | `687890` | Shared technical item | Implementation evidence; direct product sheet still desirable |

Shared item membership establishes the common catalogue capability core. It does not prove that faceplate, market, hardware revision, or packaging is identical.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `U1809F_U_EN` | User guide | revision/date not yet pinned | 4695 user operation and temperature-control behavior | [Archived original](../../sources/devices/documents/device-doc-temp-control-u1809f-u-en/U1809F_U_EN.pdf) | publisher source not currently retained |
| `U1809C_Installatore_UK` | Installation / commissioning manual | revision/date not yet pinned | 4695 installation and commissioning | [Archived original](../../sources/devices/documents/device-doc-temp-control-u1809c-installatore-uk/U1809C_Installatore_UK.pdf) | publisher source not currently retained |
| `U1809B_Software_GB` | Software manual | revision/date not yet pinned | TiThermoBasic programming / firmware workflow | [Archived original](../../sources/devices/documents/device-doc-temp-control-u1809b-software-gb/U1809B_Software_GB.pdf) | publisher source not currently retained |
| MyHOME catalogue `HPML0714` | Product catalogue | revision/date not yet pinned | System-level temperature-control context only; the `4695` family is not named. Related Arteor central units `573918` / `573919` occur on printed pp. 16, 24, 32 / PDF pp. 16, 24, 32 | [Archived MyHOME catalogue](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf) | publisher source not currently retained |

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

The current catalogue has one applicable firmware definition:

| Catalogue firmware | Version | Build | Localization | Slots | Default |
| --- | --- | ---: | ---: | ---: | ---: |
| `23` | `1.0` | `35` | `0` | `1` | yes |

Catalogue applicability is not a claim that every surviving commercial variant reports this exact installed build. `DIMENSION 2` remains the authoritative installed-firmware observation when the Device exposes it.

## Module, Object, and Virgin Object model

| Slot | Object | Description | Relationship |
| ---: | ---: | --- | --- |
| `1` | `90` | Temperature control 4 zones control unit | fixed |

There is no Virgin Object for this firmware. The slot carries condition record `4163` with an empty condition string and conversion-rule reference `1000` in the implementation database. Because no Device-specific predicate is expressed there, this dossier does not invent one.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Physical configuration | catalogue + product documentation |
| Virtual Configuration | catalogue |
| Product Programming | catalogue + TiThermoBasic documentation |
| Serial programming connection | catalogue terminology |

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | implementation identity token | - | Device identity field |
| `ZA` | `0..9` | `0` | first thermoregulation zone digit |
| `ZB` | `0..9` | `1` | second thermoregulation zone digit |
| `SLA` | `0..8` | `0` | thermoregulation slave-probe selection |

The pair `ZA` / `ZB` is represented separately at firmware level. The reusable control-unit Object exposes the combined two-digit zone as `ZAZB`.

## Object configuration surfaces

The following subsections account for the complete reusable Object field surface present in the canonical catalogue. They preserve field identity without reproducing database serialization. Detailed Device-specific interpretation follows where available.

### Object `90` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `ZAZB` | Zone |
| Sensing / regulation | `WARM`, `COLD` | Winter mode; Summer mode |
| Object-specific | `SLA` | Slave number |

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

| Surface | Condition / reference | Interpretation |
| --- | --- | --- |
| Slot `1` | condition record `4163` with empty condition | no Device-specific predicate expressed |
| Conversion | reference `1000` | implementation reference remains unresolved unless matching rule is recovered |

### Catalogue filter references

No filter rows are associated with this Device firmware in the canonical catalogue.

### Catalogue slot-condition references

| Condition | Slot | Object | Predicate | Conversion reference |
| --- | --- | --- | --- | --- |
| `4163` | `1` | `90` | empty source condition | `1000` |

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
- user operating states include Manual, Holiday/Holidays, Timed, OFF and the heating/cooling protection modes such as antifreeze or thermal protection;
- timed operation supports a finite duration up to the documented day-scale limit, while local operation also supports temperature offset/override behavior;
- fan-coil installations are explicitly supported by the product workflow;
- installation/setup includes zone association, probe configuration, system diagnostics/test procedures and total-reset behavior;
- TiThermoBasic handles project transfer and product programming in addition to ordinary configurator-based setup.

These are Device-level capabilities of the 4695 family. They do not create additional catalogue Modules, but they must be retained so Object `90` is not misread as the entirety of the product behavior.

## Evidence limits and open work

- Obtain a sanitized `DIMENSION 1` / `DIMENSION 2` / `DIMENSION 30` / `DIMENSION 32` / `DIMENSION 35` fingerprint from a known 4695-family unit.
- Locate direct official product sheets for `AM5875` and the three Vela references.
- Correlate observed installed firmware with catalogue firmware `1.0 build 35`.
- Clarify the implementation meaning of condition 4163 / conversion reference `1000` if a corresponding conversion record is recovered.
- Preserve later document revisions separately rather than replacing the current evidence.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
