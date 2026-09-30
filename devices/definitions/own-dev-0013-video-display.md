# Video Display

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0013` | Project identity |
| Technical description | Video-door-entry internal unit with display and configurable auxiliary controls | Catalogue + official documentation |
| Catalogue item | `1076` - “Video Display” | Implementation evidence |
| Main catalogue system | Video door entry system | Implementation evidence |
| Item model / `modobj` | `145` | Implementation evidence |
| Firmware definitions | `5.0.0` and `6.0.1` | Implementation evidence |
| Declared Modules | 5 | Implementation evidence |
| Configuration mode | Product Programming | Implementation evidence |
| Programming connection | USB | Implementation evidence |
| Categories | Audio / Video, User Interface, Multifunction | Product and capability model |

The Video Display is a MyHOME video-door-entry internal unit that combines the primary internal-unit function with four fixed auxiliary control Modules. The catalogue capability model is shared by eight commercial records across BTicino and Legrand ranges.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino L/N/NT | `344400` | Documented commercial identity | Catalogue + archived installation/user/software manuals |
| BTicino L/N/NT | `344401` | Documented commercial identity | Catalogue + archived installation/user/software manuals |
| BTicino Axolute | `349311` | Documented commercial identity | Catalogue + archived MyHOME Automation guide |
| BTicino Axolute | `349312` | Documented commercial identity | Catalogue + archived MyHOME Automation guide |
| BTicino Axolute | `349313` | Shared technical item | Implementation evidence; direct product-document review pending |
| BTicino Axolute | `349340` | Shared technical item | Implementation evidence; direct product-document review pending |
| Legrand Arteor | `573950` | Shared technical item | Implementation evidence; direct product-document review pending |
| Legrand Arteor | `573951` | Shared technical item | Implementation evidence; direct product-document review pending |

Shared item membership establishes the common catalogue capability core. It does not erase possible finish, package, market, or hardware differences between commercial references.

## Documentation

| Document | Type | Coverage | Archived original |
| --- | --- | --- | --- |
| `O1421A_I_EN` | Installation manual | `344400`, `344401` Video Display | [Archived PDF](../../sources/devices/documents/device-doc-video-display-o1421a-i-en/O1421A_I_EN.pdf) |
| `O1421A_U_EN` | User guide | `344400`, `344401` Video Display | [Archived PDF](../../sources/devices/documents/device-doc-video-display-o1421a-u-en/O1421A_U_EN.pdf) |
| `O1421A_S_EN` | TiLivingLightDisplay software manual | `344400`, `344401` Video Display | [Archived PDF](../../sources/devices/documents/device-doc-video-display-o1421a-s-en/O1421A_S_EN.pdf) |
| MyHOME Automation guide | System / product guide | Includes Axolute Video Display references `349311` and `349312` | [Archived PDF](../../sources/devices/documents/device-doc-myhome-automation-guide/MH_Guide_Automatisme.pdf) |

All retained files are byte-for-byte originals registered in the source manifest.

## Physical and product characteristics

The archived installation manual documents the `344400/344401` implementation as a flush-mounted Video Display with a 2.5-inch LCD, local navigation and function keys, SCS connection, and mini-USB connection for advanced programming and firmware-related operations.

The user-facing function set includes video-door-entry functions together with configurable access to intercom/camera activation, scenarios, alarms, sound, temperature-control and multimedia functions. These are product-level functions; the five catalogue Modules below describe the fixed OpenWebNet-facing capability projection rather than the complete UI menu.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1076` | Implementation evidence |
| main system | Video door entry system | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `145` | Implementation evidence |
| BTicino brand / line values | brand `1`; L/N/NT line `1`; Axolute line `3` | Implementation evidence |
| Legrand Arteor values | brand `2`; line `2` | Implementation evidence |

Installed identity values should be corroborated through the canonical [Device Identity](../../diagnostics/dim1-device-identity.md) workflow when a known physical unit is available.

## Firmware

The current canonical catalogue has two firmware capability definitions:

| Catalogue firmware | Version | Build | Localization level | Slots | Default |
| --- | --- | ---: | ---: | ---: | ---: |
| `616` | `5.0` | `0` | 0 | 5 | no |
| `27` | `6.0` | `1` | 1 | 5 | yes |

Both definitions expose the same five fixed Objects, Product Programming mode, USB programming connection and firmware-scoped configuration fields.

Catalogue applicability does not prove the firmware installed on every commercial variant.

## Module and Object model

| Slot | Object | Description | Relationship |
| ---: | ---: | --- | --- |
| `1` | `154` | Internal Unit | fixed |
| `2` | `418` | Open lock control | fixed |
| `3` | `422` | Addressed autoswitch control | fixed |
| `4` | `426` | Staircase light control | fixed |
| `5` | `429` | Paging button | fixed |

There are no Virgin Objects and no slot-condition rows for either firmware definition.

## Firmware-scoped configuration

| Field | Stored domain | Meaning |
| --- | --- | --- |
| `AID` | Device identity | implementation identity field |
| `N_1` | `0..9` | first digit of physical `N` address |
| `N_2` | `0..9` | second digit of physical `N` address |
| `P` | `0..9` | associated entrance-panel / external-unit configurator |
| `M` | `0..6` | physical operating / menu mode selector |

The installation manual presents the physical quick-configuration surface as a two-digit `N` plus `P` and `M`. It also states that a physically configured unit cannot edit the corresponding configuration through the display menu, while advanced configuration is performed with the PC software.

## Reusable Object configuration

### Object `154` - Internal Unit

The reusable Internal Unit model exposes:

- `N=0..3999`;
- associated external unit `P=0..95`;
- hands-free, professional-studio, door-state, beep, slave and Ethernet-call-forwarding flags;
- menu preset `0..99`;
- ring timeout `1..30`;
- call timeout `10..180`;
- external-unit timeout `3..90`;
- internal-unit timeout `3..90`;
- telephone timeout `3..180`;
- associated switchboard `0..95`.

The source contains two unresolved labels for `PEOPLE_S` values `1` and `2`; preserve them as unknown rather than inventing names.

### Object `418` - Open lock control

- external-unit address `P=0..95`;
- segment level: same level, riser, building, or backbone.

### Object `422` - Addressed autoswitch control

- external-unit address `P=0..95`;
- segment level: same, riser, building, or backbone.

### Object `426` - Staircase light control

- internal-unit address split across `N1=0..255` and `N2=0..15`;
- segment: same, riser, building, or backbone.

### Object `429` - Paging button

- mode `1=Base`, `2=Advanced`;
- amplifier area `0..99`;
- amplifier unit `0..39`;
- addressing type: General, Ambient, or Point-to-point.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | identify item model `145`, brand and line | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware rather than assume catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate the five fixed Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect configured Module addresses where exposed | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values where exposed | [Configuration](../../diagnostics/dim35-configuration.md) |

Generic diagnostic frame grammar belongs in the linked references.

## Programming

This Device uses Product Programming rather than ordinary physical/virtual Object programming in the catalogue. The USB-connected TiLivingLightDisplay workflow and the firmware-scoped quick-configuration fields are Device-specific evidence.

A future Device Library representation should keep the five-Module topology, both catalogue firmware applicability definitions and the reusable Object parameter domains, while keeping installation-specific addresses private.

## Corroboration status and open work

- Obtain sanitized fingerprints for at least one `344400/344401` unit and one Axolute/Arteor variant.
- Locate direct official documentation for `349313`, `349340`, `573950` and `573951`.
- Correlate observed firmware versions to catalogue firmware `5.0.0` and `6.0.1`.
- Determine the meaning of the unresolved `PEOPLE_S` enum values.
- Search for older and language-specific document revisions.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
