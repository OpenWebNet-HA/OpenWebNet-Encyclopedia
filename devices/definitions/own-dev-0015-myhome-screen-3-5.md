# MyHOME_Screen 3.5

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0015` | Project identity |
| Technical description | 3.5-inch MyHOME touchscreen user interface | Catalogue + official documentation |
| Catalogue item | `1469` - “MyHOME_Screen 3.5” | Implementation evidence |
| Main catalogue system | Integration functions | Implementation evidence |
| Item model / `modobj` | `30` | Implementation evidence |
| Firmware families | `1.0.17`, `2.0.3`, `3.0.8/9/10`, `4.0.0` | Implementation evidence |
| Declared Modules | 1 | Implementation evidence |
| Configuration mode | Product Programming | Implementation evidence |
| Programming connections | Ethernet, USB | Implementation evidence |
| Categories | User Interface, Integration, Multifunction | Product and capability model |

MyHOME_Screen 3.5 is a touchscreen user interface for multiple MyHOME systems. The catalogue represents all eight commercial records with one fixed `Colors Touch Screen` Object and several firmware applicability records.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `H4890` | Documented identity | Catalogue + archived technical sheet |
| BTicino L/N/NT | `LN4890` | Documented identity | Catalogue + archived technical sheet |
| BTicino Air | `LN4890A` | Documented identity | Catalogue + archived technical sheet |
| BTicino Eteris | `HW4890` | Documented identity | Catalogue + archived technical sheet |
| BTicino Matix | `AM4890` | Documented identity with source-label inconsistency | Catalogue + installation text in archived technical sheet |
| Legrand Arteor | `573958` | Shared technical item / software-catalogue identity | Implementation evidence |
| Legrand Céliane | `067292` | Shared technical item / software-catalogue identity | Implementation evidence |
| Legrand Mosaic | `078479` | Shared technical item / software-catalogue identity | Implementation evidence |

The archived technical sheet contains an internal reference discrepancy: its heading lists `AM5890`, while the installation/reference text uses `AM4890`, matching the canonical catalogue. Preserve the source discrepancy rather than silently rewriting the PDF.

## Documentation

| Document | Type | Coverage | Archived original |
| --- | --- | --- | --- |
| `BT00518_a_EN` | Technical sheet | BTicino MyHOME_Screen 3.5 family | [Archived PDF](../../sources/devices/documents/device-doc-myhome-screen-bt00518-a-en/BT00518_a_EN.pdf) |
| `RA00107AC_U_EN` | User guide | MyHOME_Screen 3.5 family | [Archived PDF](../../sources/devices/documents/device-doc-myhome-screen-ra00107ac-u-en/RA00107AC_U_EN.pdf) |
| `RA00107AC_S_FR` | Software manual | MyHOME_Screen 3.5 family | [Archived PDF](../../sources/devices/documents/device-doc-myhome-screen-ra00107ac-s-fr/RA00107AC_S_FR.pdf) |

Direct product sheets for the Legrand commercial variants and additional language revisions remain desirable archival sources.

## Physical and product characteristics

The archived technical sheet documents a 3.5-inch touch LCD interface capable of managing multiple MyHOME applications, including:

- automation;
- lighting;
- temperature control;
- sound diffusion;
- burglar alarm;
- energy management;
- scenarios.

The sheet describes up to 20 actuations per application. It also documents nominal `27 Vdc` SCS supply, an `18..27 Vdc` operating range, approximately `80 mA` absorption, `0..40 °C` operating temperature, USB and Ethernet interfaces, and SCS bus connection.

Programming/configuration is performed with the dedicated PC software over supported local interfaces.

## Identity and firmware

| Field | Value |
| --- | --- |
| `EN_ITEM.id_item` | `1469` |
| system | Integration functions |
| `AS_ITEM_SYSTEM.modobj` | `30` |
| slot count | 1 |
| Object | `32` Colors Touch Screen |
| configuration mode | Product Programming |
| connection modalities | Ethernet, USB |

### Catalogue firmware applicability

| Catalogue firmware | Version | Builds | Localization level | Default |
| --- | --- | --- | ---: | ---: |
| `75` | `1.0` | `17` | 1 | no |
| `8` | `2.0` | `3` | 1 | no |
| `9` | `3.0` | `8`, `9`, `10` | 1 | yes |
| `692` | `4.0` | `0` | 0 | no |

All four firmware definitions expose the same one-Object topology and the same catalogue configuration surface.

## Module and Object model

Slot `1` is fixed to Object `32`, **Colors Touch Screen**.

There are no Virgin Objects and no slot-condition rows.

## Configuration surface

Every firmware definition contains the following firmware-scoped fields:

| Field | Stored form | Meaning |
| --- | --- | --- |
| `AID` | identity value | implementation Device identity |
| `LAN_IP_ADDRESS` | IPv4-shaped user value | local network address |
| `FW_VER` | six-character firmware-version value | firmware information |
| `SYSADDRESS` | six-character “Univocal code” | product/system identifier |

Object `32` exposes the same network address, firmware-version and univocal-code fields.

These fields describe the reusable product-programming model. Actual IP addresses and installation identifiers are private installation state and must not be copied into the public Device Library from research captures.

## Functional applicability

The user interface can orchestrate several MyHOME functional systems, but the catalogue Device topology itself remains one Integration-functions Object. This is an important model boundary: a screen that controls lighting, automation, temperature and scenarios is not represented as a separate firmware Module for every UI menu.

Generic WHO semantics remain under [Functional Protocol](../../functional/).

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | identify item model `30`, brand and line | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe actual installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate one fixed Colors Touch Screen Object | [Modules](../../diagnostics/dim30-modules.md) |

Other diagnostic/programming surfaces should only be claimed after hardware observation or explicit implementation evidence.

## Programming

The catalogue declares Product Programming over Ethernet and USB. Device-specific programming data is intentionally small: network identity/address, firmware-version field and system address.

The much broader MyHOME application configuration presented in the user/software manuals belongs to product programming and UI configuration rather than to the ordinary Object configuration model.

## Corroboration status and open work

- Add sanitized hardware fingerprints across more than one product line.
- Correlate observed installed firmware with the four catalogue firmware families.
- Locate direct official product sheets for `573958`, `067292` and `078479`.
- Resolve the archived technical-sheet `AM5890` / `AM4890` discrepancy through additional revisions.
- Archive English/Italian/French software and user-document revisions where distinct.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
