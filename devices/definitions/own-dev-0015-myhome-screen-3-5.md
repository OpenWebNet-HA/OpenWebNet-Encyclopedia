# MyHOME_Screen 3.5

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0015` | Project identity |
| Technical description | 3.5-inch MyHOME touchscreen user interface | Catalogue + official documentation |
| Catalogue item | `1469` - “MyHOME_Screen 3.5” | Implementation evidence |
| Main catalogue system | Integration functions | Implementation evidence |
| Item model / `modobj` | `30` | Implementation evidence |
| Firmware definition | `1.0.17`, `2.0.3`, `3.0.8/9/10`, `4.0.0` | Implementation evidence |
| Declared Modules | `1` | Implementation evidence |
| Configuration mode | Product Programming | Implementation evidence |
| Programming connections | Ethernet, USB | Implementation evidence |
| Categories | User Interface, Integration, Multifunction | Product and capability model |

MyHOME_Screen 3.5 is a touchscreen user interface for multiple MyHOME systems. The catalogue represents all eight commercial records with one fixed `Colors Touch Screen` Object and several firmware applicability records.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `H4890` | Documented identity | Catalogue + archived technical sheet |
| BTicino - LivingLight | `LN4890` | Documented identity | Catalogue + archived technical sheet |
| BTicino - Air | `LN4890A` | Documented identity | Catalogue + archived technical sheet |
| BTicino - Eteris | `HW4890` | Documented identity | Catalogue + archived technical sheet |
| BTicino - Matix | `AM4890` | Documented identity with source-label inconsistency | Catalogue + installation text in archived technical sheet |
| Legrand - Arteor | `573958` | Shared technical item / software-catalogue identity | Implementation evidence |
| Legrand - Céliane | `067292` | Shared technical item / software-catalogue identity | Implementation evidence |
| Legrand - Mosaic | `078479` | Shared technical item / software-catalogue identity | Implementation evidence |

The archived technical sheet contains an internal reference discrepancy: its heading lists `AM5890`, while the installation/reference text uses `AM4890`, matching the canonical catalogue. Preserve the source discrepancy rather than silently rewriting the PDF.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `BT00518_a_EN` | Technical sheet | revision/date not yet pinned | BTicino MyHOME_Screen 3.5 family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/43/61/4361119dc3e9e028cacb247fcb8b8faae15acad73c0bd2fd73bcfb65b90924c9.pdf) | publisher source not currently retained |
| `RA00107AC_U_EN` | User guide | revision/date not yet pinned | MyHOME_Screen 3.5 family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/28/33/2833c50e275c23816dfaad7ddb25571e97c73097652c61e5df5eb43e8d7bce23.pdf) | publisher source not currently retained |
| `RA00107AC_S_FR` | Software manual | revision/date not yet pinned | MyHOME_Screen 3.5 family | [Archived PDF](https://archive.openwebnet-ha.org/sha256/06/fd/06fd9db38da00c9f208531163142a19bafd6b8801e255cb48a876adedc7bcfa5.pdf) | publisher source not currently retained |

Direct product sheets for the Legrand commercial variants and additional language revisions remain desirable archival sources.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Display | 3.5-inch touch LCD | `BT00518_a_EN` |
| Mounting | documented `3+3` module arrangement | `BT00518_a_EN` + Source reconciliation |
| SCS nominal supply | `27 Vdc` | `BT00518_a_EN` |
| SCS operating supply | `18..27 Vdc` | `BT00518_a_EN` |
| Current draw | approximately `80 mA` | `BT00518_a_EN` |
| Operating temperature | `0..40 °C` | `BT00518_a_EN` |
| Interfaces | SCS bus, USB and Ethernet | `BT00518_a_EN` |

Programming/configuration is performed with dedicated PC software over the supported local interfaces.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1469` | Implementation evidence |
| Main system | Integration functions | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `30` | Implementation evidence |

## Firmware and hardware

| Catalogue firmware | Version | Builds | Localization level | Default |
| --- | --- | --- | ---: | ---: |
| `75` | `1.0` | `17` | 1 | no |
| `8` | `2.0` | `3` | 1 | no |
| `9` | `3.0` | `8`, `9`, `10` | 1 | yes |
| `692` | `4.0` | `0` | 0 | no |

All four firmware definitions expose the same one-Object topology and the same catalogue configuration surface.

Catalogue applicability does not prove the firmware installed on every commercial variant.

## Module, Object, and Virgin Object model

| Slot | Object | Description | Relationship |
| ---: | ---: | --- | --- |
| `1` | `32` | Colors Touch Screen | fixed |

There is no Virgin Object and no slot-condition row.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Product Programming | implementation evidence + product software documentation |
| Ethernet programming connection | implementation evidence |
| USB programming connection | implementation evidence |

## Firmware-scoped configuration

| Field | Domain / stored form | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | identity value | - | implementation Device identity |
| `LAN_IP_ADDRESS` | IPv4-shaped user value | - | local network address |
| `FW_VER` | six-character firmware-version value | - | firmware information |
| `SYSADDRESS` | six-character Univocal code | - | product/system identifier |

Actual IP addresses and installation identifiers are private installation state and must not be copied into the public Device Library from research captures.

## Object configuration surfaces

The following subsections account for the complete reusable Object field surface present in the canonical catalogue. They preserve field identity without reproducing database serialization. Detailed Device-specific interpretation follows where available.

### Object `32` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `LAN_IP_ADDRESS`, `SYSADDRESS` | Local IP address; Univocal code |
| Object-specific | `FW_VER` | Firmware version |

### Additional Device-specific interpretation

| Field | Domain / stored form | Meaning |
| --- | --- | --- |
| `LAN_IP_ADDRESS` | IPv4-shaped user value | network address |
| `FW_VER` | six-character firmware-version value | firmware information |
| `SYSADDRESS` | six-character Univocal code | product/system identifier |

Object `32` exposes the same product-programming identity/network surface except for the firmware-level `AID` identity token.

## Conditions, filters, and conversions

| Surface | Status | Evidence |
| --- | --- | --- |
| Slot conditions | none across the fixed topology | implementation evidence |
| Virgin Object | none | implementation evidence |
| Object selection | slot `1` fixed to Object `32` | implementation evidence |

### Catalogue filter references

No filter rows are associated with this Device firmware in the canonical catalogue.

### Catalogue slot-condition references

No slot-condition rows are associated with this Device firmware in the canonical catalogue.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify item model `30`, brand and line | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe actual installed firmware | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate one fixed Colors Touch Screen Object | [Modules](../../diagnostics/dim30-modules.md) |

Other diagnostic/programming surfaces should only be claimed after hardware observation or explicit implementation evidence.

## Functional applicability

The user interface can orchestrate several MyHOME functional systems, but the catalogue Device topology itself remains one Integration-functions Object. This is an important model boundary: a screen that controls lighting, automation, temperature and scenarios is not represented as a separate firmware Module for every UI menu.

Generic WHO semantics remain under [Functional Protocol](../../functional/).

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

The catalogue declares Product Programming over Ethernet and USB. Device-specific programming data is intentionally small: network identity/address, firmware-version field and system address.

The much broader MyHOME application configuration presented in the user/software manuals belongs to product programming and UI configuration rather than to the ordinary Object configuration model.

## Source reconciliation

The MyHOME_Screen 3.5 technical/user/software documents establish product details beyond its fixed catalogue role:

- the product occupies a `3+3` module mounting arrangement and uses different installation accessories/boxes depending on the variant, including the documented `506E` versus `528W` context;
- PC programming/transfer paths include the documented RS232 lead `335919`, USB accessory `3559`, or Ethernet depending on the commercial variant;
- TiTouchScreen project configuration includes conditional scenarios, date/time presentation, password protection and configurable graphical/icon content;
- these user-interface/project functions are product-programming capabilities and must not be mistaken for extra OpenWebNet Modules.

The remaining completeness issues concern direct Legrand-variant documentation, the `AM4890`/`AM5890` source discrepancy and hardware fingerprints.

## Evidence limits and open work

- Add sanitized hardware fingerprints across more than one product line.
- Correlate observed installed firmware with the four catalogue firmware families.
- Locate direct official product sheets for `573958`, `067292` and `078479`.
- Resolve the archived technical-sheet `AM5890` / `AM4890` discrepancy through additional revisions.
- Archive English/Italian/French software and user-document revisions where distinct.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
