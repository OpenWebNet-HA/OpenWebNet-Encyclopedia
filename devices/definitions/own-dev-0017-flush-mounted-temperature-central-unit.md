# Flush-mounted temperature central unit

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | OWN-DEV-0017 | Project identity |
| Technical description | Flush-mounted four-zone temperature-control central unit | Catalogue + official documentation |
| Catalogue item | 168 - Flush mounted temperature central unit | Implementation evidence |
| Main catalogue system | Temperature control | Implementation evidence |
| Item model / modobj | 48 | Implementation evidence |
| Firmware definition | 1.0 build 35 | Implementation evidence |
| Declared Modules | 1 | Implementation evidence |
| Configuration modes | Virtual, Physical, Product Programming | Implementation evidence |
| Programming connection | Serial | Implementation evidence |
| Categories | Thermoregulation, User Interface | Product and capability model |

This Device is the four-zone MyHOME temperature-control central unit sold under several BTicino and Legrand references. It provides the system-level scheduling and zone-management interface while the catalogue exposes one fixed OpenWebNet Object representing the four-zone control-unit role.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | HC/HS4695 | Shared technical item; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino Axolute | HD4695 | Shared technical item; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino L/N/NT | L/N/NT4695 | Shared technical item; 4695 family documentation applies | Catalogue + official 4695 documentation |
| BTicino Matix | AM5875 | Shared technical item | Implementation evidence; direct product sheet still desirable |
| Legrand Vela | 683090 | Shared technical item | Implementation evidence; direct product sheet still desirable |
| Legrand Vela | 687390 | Shared technical item | Implementation evidence; direct product sheet still desirable |
| Legrand Vela | 687890 | Shared technical item | Implementation evidence; direct product sheet still desirable |

Shared item membership establishes the common catalogue capability core. It does not prove that faceplate, market, hardware revision, or packaging is identical.

## Documentation

| Document | Coverage | Status |
| --- | --- | --- |
| U1809F_U_EN | 4695 user operation and temperature-control behavior | [Archived original](../../sources/devices/documents/device-doc-temp-control-u1809f-u-en/U1809F_U_EN.pdf) |
| U1809C_Installatore_UK | 4695 installation and commissioning | [Archived original](../../sources/devices/documents/device-doc-temp-control-u1809c-installatore-uk/U1809C_Installatore_UK.pdf) |
| U1809B_Software_GB | TiThermoBasic programming / firmware workflow | [Archived original](../../sources/devices/documents/device-doc-temp-control-u1809b-software-gb/U1809B_Software_GB.pdf) |
| MyHOME catalogue HPML0714 | Family-level product context and catalogue corroboration | [Archived MyHOME catalogue](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf) |

The 4695 documentation describes management of a temperature-control system with up to four zones and PC programming through TiThermoBasic. Where an official PDF could not be fetched by the archival runner, the official publisher URL is retained rather than substituting an unofficial mirror.

## Physical and product characteristics

The documented 4695 implementation is a three-module flush-mounted user interface for a four-zone temperature-control installation. The front panel provides local display and control while schedules and temperature-control parameters are managed at product level. These user-facing functions are broader than the single catalogue Object: the Object model below records the OpenWebNet capability projection, not every menu or display function.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| EN_ITEM.id_item | 168 | Implementation evidence |
| main system | thermoregulation / Temperature control | Implementation evidence |
| AS_ITEM_SYSTEM.modobj | 48 | Implementation evidence |
| family | 11 | Implementation evidence |

Installed identity should be corroborated with the canonical [Device Identity](../../diagnostics/dim1-device-identity.md) workflow on a known unit.

## Firmware and build applicability

The current catalogue has one applicable firmware definition:

| Catalogue firmware | Version | Build | Localization | Slots | Default |
| --- | --- | ---: | ---: | ---: | ---: |
| 23 | 1.0 | 35 | 0 | 1 | yes |

Catalogue applicability is not a claim that every surviving commercial variant reports this exact installed build. DIMENSION 2 remains the authoritative installed-firmware observation when the Device exposes it.

## Module and Object model

| Slot | Object | Description | Relationship |
| ---: | ---: | --- | --- |
| 1 | 90 | Temperature control 4 zones control unit | fixed |

There is no Virgin Object for this firmware. The slot carries condition record 4163 with an empty condition string and conversion-rule reference 1000 in the implementation database. Because no Device-specific predicate is expressed there, this dossier does not invent one.

## Configuration modes

The catalogue declares all three relevant configuration paths: Physical configuration, Virtual Configuration, and Product Programming. It also declares a Serial programming connection. The product documentation independently establishes the TiThermoBasic product-programming workflow; the catalogue connection label is preserved as implementation terminology rather than expanded into an unsupported connector claim.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| AID | implementation identity token | - | Device identity field |
| ZA | 0..9 | 0 | first thermoregulation zone digit |
| ZB | 0..9 | 1 | second thermoregulation zone digit |
| SLA | 0..8 | 0 | thermoregulation slave-probe selection |

The pair ZA/ZB is represented separately at firmware level. The reusable control-unit Object exposes the combined two-digit zone as ZAZB.

## Reusable Object configuration

Object 90 exposes:

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| ZAZB | 00..99 | 01 | zone |
| WARM | 0 Disable / 1 Enable | 0 | winter modality |
| COLD | 0 Disable / 1 Enable | 0 | summer modality |
| SLA | 0..8 | 0 | slave number |

These are catalogue validation domains. They should not be widened from product UI behavior or narrowed from one observed installation without evidence.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| DIMENSION 1 | identify item model / brand / line where exposed | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| DIMENSION 2 | observe installed firmware instead of assuming catalogue 1.0.35 | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| DIMENSION 30 | corroborate the single fixed control-unit Module | [Modules](../../diagnostics/dim30-modules.md) |
| DIMENSION 32 | inspect the configured thermoregulation address when exposed | [Addressing](../../diagnostics/dim32-addressing.md) |
| DIMENSION 35 | inspect ZA/ZB/SLA and Object configuration where exposed | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

The Device belongs to the temperature-control system. The catalogue and product documentation agree on a four-zone control-unit role. Generic WHO 4 frame grammar belongs in the Functional Protocol section; this page records that the role and configuration surface apply to this Device.

## Programming

Physical configuration, virtual configuration, and product programming are all catalogue-supported. TiThermoBasic is the documented PC workflow for the 4695 family. Firmware update and project-transfer details belong to the software manual; the Device-specific invariant here is that product programming exists in addition to ordinary configurator-based setup.

## Evidence limits and open work

- Obtain a sanitized DIM1/DIM2/DIM30/DIM32/DIM35 fingerprint from a known 4695-family unit.
- Locate direct official product sheets for AM5875 and the three Vela references.
- Correlate observed installed firmware with catalogue firmware 1.0 build 35.
- Clarify the implementation meaning of condition 4163 / conversion reference 1000 if a corresponding conversion record is recovered.
- Preserve later document revisions separately rather than replacing the current evidence.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
