# Video Display

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0013` | Project identity |
| Technical description | Video-door-entry internal unit with display and configurable auxiliary controls | Catalogue + official documentation |
| Catalogue item | `1076` - “Video Display” | Implementation evidence |
| Main catalogue system | Video door entry system | Implementation evidence |
| Item model / `modobj` | `145` | Implementation evidence |
| Firmware definition | `5.0.0` and `6.0.1` | Implementation evidence |
| Declared Modules | `5` | Implementation evidence |
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

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `O1421A_I_EN` | Installation manual | revision/date not yet pinned | `344400`, `344401` Video Display | [Archived PDF](../../sources/devices/documents/device-doc-video-display-o1421a-i-en/O1421A_I_EN.pdf) | publisher source not currently retained |
| `O1421A_U_EN` | User guide | revision/date not yet pinned | `344400`, `344401` Video Display | [Archived PDF](../../sources/devices/documents/device-doc-video-display-o1421a-u-en/O1421A_U_EN.pdf) | publisher source not currently retained |
| `O1421A_S_EN` | TiLivingLightDisplay software manual | revision/date not yet pinned | `344400`, `344401` Video Display | [Archived PDF](../../sources/devices/documents/device-doc-video-display-o1421a-s-en/O1421A_S_EN.pdf) | publisher source not currently retained |
| MyHOME Automation guide | System / product guide | revision/date not yet pinned | Axolute Video Display references `349311` and `349312` occur on printed pp. 24, 25 / PDF pp. 26, 27 | [Archived PDF](../../sources/devices/documents/device-doc-myhome-automation-guide/MH_Guide_Automatisme.pdf) | publisher source not currently retained |

All retained files are byte-for-byte originals registered in the source manifest.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Mounting | flush-mounted Video Display | `O1421A_I_EN` |
| Display | 2.5-inch LCD | `O1421A_I_EN` |
| Local interface | navigation and function keys | `O1421A_I_EN` |
| SCS interface | SCS connection | `O1421A_I_EN` |
| Programming interface | mini-USB for advanced programming and firmware-related operations | `O1421A_I_EN` |

The user-facing function set is broader than the five catalogue Modules. Product UI functions do not imply one OpenWebNet Module per menu entry.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1076` | Implementation evidence |
| Main system | Video door entry system | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `145` | Implementation evidence |
| BTicino brand / line | brand `1`; L/N/NT line `1`; Axolute line `3` | Implementation evidence |
| Legrand Arteor | brand `2`; line `2` | Implementation evidence |

## Firmware and hardware

The current canonical catalogue has two firmware capability definitions:

| Catalogue firmware | Version | Build | Localization level | Slots | Default |
| --- | --- | ---: | ---: | ---: | ---: |
| `616` | `5.0` | `0` | 0 | 5 | no |
| `27` | `6.0` | `1` | 1 | 5 | yes |

Both definitions expose the same five fixed Objects, Product Programming mode, USB programming connection and firmware-scoped configuration fields.

Catalogue applicability does not prove the firmware installed on every commercial variant.

## Module, Object, and Virgin Object model

| Slot | Object | Description | Relationship |
| ---: | ---: | --- | --- |
| `1` | `154` | Internal Unit | fixed |
| `2` | `418` | Open lock control | fixed |
| `3` | `422` | Addressed autoswitch control | fixed |
| `4` | `426` | Staircase light control | fixed |
| `5` | `429` | Paging button | fixed |

There are no Virgin Objects and no slot-condition rows for either firmware definition.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Product Programming | implementation evidence; TiLivingLightDisplay workflow |
| USB programming connection | implementation evidence + installation/software documentation |

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| `AID` | Device identity | - | implementation identity field |
| `N_1` | `0..9` | - | first digit of physical `N` address |
| `N_2` | `0..9` | - | second digit of physical `N` address |
| `P` | `0..9` | - | associated entrance-panel / external-unit configurator |
| `M` | `0..6` | - | physical operating / menu mode selector |

Physical quick configuration is a two-digit `N` plus `P` and `M`. Advanced configuration is performed with the PC software.

## Object configuration surfaces

The following subsections account for the complete reusable Object field surface present in the canonical catalogue. They preserve field identity without reproducing database serialization. Detailed Device-specific interpretation follows where available.

### Object `154` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `N`, `P` | Address; Associated external unit |
| Mode / behavior | `HAND_FREE`, `PRO_STUDIO`, `DOOR_STATE`, `IS_SLAVE` | HAND_FREE; Professional Studio; Door state display; Slave |
| Object-specific | `PEOPLE_S`, `ASS_SWITCH`, `DOSA_CALL` | PeopleSearching; AssociatedSwitchboard; Forward incoming call to ethernet |
| User interface | `MENU_PRE`, `BEEP` | MenuPreset; BEEP |
| Timing | `RING_T_OUT`, `CALL_T_OUT`, `PE_T_OUT`, `PI_T_OUT`, `TEL_T_OUT` | RingTimeOut; Call timeout; EUConnectionTimeOut; IUConnectionTimeOut; TelConnectionTimeout |

### Object `418` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `P` | External unit address |
| Object-specific | `SEG_LEV` | Level |

### Object `422` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `P` | External unit address |
| Object-specific | `SEG_LEV` | Segment |

### Object `426` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | `N1`, `N2` | Internal unit address |
| Object-specific | `SEG_LEV` | Segment |

### Object `429` - catalogue configuration

| Surface | Fields | Meaning |
| --- | --- | --- |
| Object-specific | `M` | mode(Base,Advanced) |
| Addressing | `AMPL_AREA`, `AMPL_UNIT`, `ADDR_TYPE` | Amplifier area; Amplifier unit; Addressing type |

### Additional Device-specific interpretation

| Object | Role | Principal configuration |
| --- | --- | --- |
| `154` | Internal Unit | N/P addressing, flags, menu preset, timeouts, switchboard |
| `418` | Open lock control | external-unit `P` and segment level |
| `422` | Addressed autoswitch control | external-unit `P` and segment level |
| `426` | Staircase light control | `N1`/`N2` and segment |
| `429` | Paging button | mode, amplifier area/unit and addressing type |

#### Object `154` - Internal Unit

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

#### Object `418` - Open lock control

- external-unit address `P=0..95`;
- segment level: same level, riser, building, or backbone.

#### Object `422` - Addressed autoswitch control

- external-unit address `P=0..95`;
- segment level: same, riser, building, or backbone.

#### Object `426` - Staircase light control

- internal-unit address split across `N1=0..255` and `N2=0..15`;
- segment: same, riser, building, or backbone.

#### Object `429` - Paging button

- mode `1=Base`, `2=Advanced`;
- amplifier area `0..99`;
- amplifier unit `0..39`;
- addressing type: General, Ambient, or Point-to-point.

## Conditions, filters, and conversions

| Surface | Status | Evidence |
| --- | --- | --- |
| Slot conditions | none for either catalogue firmware | implementation evidence |
| Virgin Object | none | implementation evidence |
| Topology | five fixed Objects for both catalogue firmware definitions | implementation evidence |

### Catalogue filter references

| Filter | Object | Field | Source note |
| --- | --- | --- | --- |
| `2003` | `154` | `DOSA_CALL` | Forward incoming call to ethernet |
| `2019` | `154` | `DOSA_CALL` | Forward incoming call to ethernet |
| `4110` | `426` | `N1` | Internal unit address |
| `4111` | `426` | `N1` | Internal unit address |

### Catalogue slot-condition references

No slot-condition rows are associated with this Device firmware in the canonical catalogue.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | identify item model `145`, brand and line | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe installed firmware rather than assume catalogue applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate the five fixed Modules | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect configured Module addresses where exposed | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect configuration values where exposed | [Configuration](../../diagnostics/dim35-configuration.md) |

Generic diagnostic frame grammar belongs in the linked references.

## Functional applicability

The primary role is video door entry. The product UI can also expose intercom/camera activation, scenarios, alarms, sound, temperature-control and multimedia functions without creating one firmware Module per UI function.

## Observed behavior and corroboration

No publishable hardware observation has yet been incorporated as canonical corroboration for this Device definition. Outstanding runtime and hardware checks are listed under Evidence limits and open work.

## Programming

This Device uses Product Programming rather than ordinary physical/virtual Object programming in the catalogue. The USB-connected TiLivingLightDisplay workflow and the firmware-scoped quick-configuration fields are Device-specific evidence.

A future Device Library representation should keep the five-Module topology, both catalogue firmware applicability definitions and the reusable Object parameter domains, while keeping installation-specific addresses private.

## Source reconciliation

The archived Video Display installation, user and TiLivingLightDisplay manuals add substantial product behavior beyond the five fixed catalogue Objects:

- physical configuration exposes predefined `M=0..6` menu/application arrangements rather than one generic configuration;
- the `P` address participates in camera/activation behavior relative to the entrance-panel address and must be interpreted in the video-door-entry context;
- the product has a line-termination control and documented auxiliary-supply wiring options that affect installation but not the OpenWebNet Module count;
- quick/physical configuration has documented restrictions in systems using interface `346850`;
- software configuration can add/arrange applications and transfer projects/firmware through the product tooling rather than only setting the catalogue Object parameters;
- Master/Slave and menu/application limitations are product-level constraints and must remain distinct from generic WHO semantics;
- reset and user-menu behavior are part of the Device operational model, not additional Objects.

The dossier now treats the five Objects as the OpenWebNet projection of a richer video-door-entry user interface rather than as the whole product.

## Evidence limits and open work

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
