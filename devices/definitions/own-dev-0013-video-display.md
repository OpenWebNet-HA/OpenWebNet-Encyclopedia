# Video Display

## Summary

Video Display is a flush-mounted video-door-entry indoor unit with a 2.5-inch LCD and navigation keys. Alongside answering calls and operating entry functions, its configured menus can provide access to scenarios, sound, alarms and temperature control.

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
| BTicino - LivingLight | `344400` | Documented commercial identity | Catalogue + archived installation/user/software manuals |
| BTicino - LivingLight | `344401` | Documented commercial identity | Catalogue + archived installation/user/software manuals |
| BTicino - Axolute | `349311` | Documented commercial identity | Catalogue + archived MyHOME Automation guide |
| BTicino - Axolute | `349312` | Documented commercial identity | Catalogue + archived MyHOME Automation guide |
| BTicino - Axolute | `349313` | Shared technical item | Implementation evidence; direct product-document review pending |
| BTicino - Axolute | `349340` | Shared technical item | Implementation evidence; direct product-document review pending |
| Legrand - Arteor | `573950` | Shared technical item | Implementation evidence; direct product-document review pending |
| Legrand - Arteor | `573951` | Shared technical item | Implementation evidence; direct product-document review pending |

Shared item membership establishes the common catalogue capability core. It does not erase possible finish, package, market, or hardware differences between commercial references.
## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `O1421A_I_EN` | Installation manual | revision/date not yet pinned | `344400`, `344401` Video Display | [Archived PDF](https://archive.openwebnet-ha.org/sha256/39/ab/39ab54625c817d9c3b49c5c7283698dc918a38b399a6462c14b23204413745a4.pdf) | publisher source not currently retained |
| `O1421A_U_EN` | User guide | revision/date not yet pinned | `344400`, `344401` Video Display | [Archived PDF](https://archive.openwebnet-ha.org/sha256/34/3b/343bd9b36ddc436084b47b34a9c6cc4079ee63ef216a87046c49c19eab33ef27.pdf) | publisher source not currently retained |
| `O1421A_S_EN` | TiLivingLightDisplay software manual | revision/date not yet pinned | `344400`, `344401` Video Display | [Archived PDF](https://archive.openwebnet-ha.org/sha256/32/76/32767ea509c1d8d439ffb4c1f3c4be28a4a9443f1f98aba8f0219d2200f03771.pdf) | publisher source not currently retained |
| MyHOME Automation guide | System / product guide | revision/date not yet pinned | Axolute Video Display references `349311` and `349312` occur on printed pp. 24, 25 / PDF pp. 26, 27 | [Archived PDF](https://archive.openwebnet-ha.org/sha256/80/6a/806a55bffb924f5ef7b25398432c0a86ab210722adc30b81f33558c6ec36f561.pdf) | publisher source not currently retained |

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

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `27` | `6` | `0` | `1` | `5` | Catalogue default | Official |
| `616` | `5` | `0` | `0` | `5` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

Both definitions expose the same five fixed Objects, Product Programming mode, USB programming connection and firmware-scoped configuration fields.
Catalogue applicability does not prove the firmware installed on every commercial variant.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `27` | `1` | `154` Internal Unit | Fixed/designated metadata | `2265` | `154` | `943` |
| `27` | `2` | `418` Open lock control | Fixed/designated metadata | `2266` | `418` | `944` |
| `27` | `3` | `422` Addressed autoswitch control | Fixed/designated metadata | `2267` | `422` | `945` |
| `27` | `4` | `426` Staircase light control | Fixed/designated metadata | `2268` | `426` | `946` |
| `27` | `5` | `429` Paging button | Fixed/designated metadata | `2269` | `429` | `947` |
| `616` | `1` | `154` Internal Unit | Fixed/designated metadata | `2426` | `154` | `1078` |
| `616` | `2` | `418` Open lock control | Fixed/designated metadata | `2427` | `418` | `1079` |
| `616` | `3` | `422` Addressed autoswitch control | Fixed/designated metadata | `2428` | `422` | `1080` |
| `616` | `4` | `426` Staircase light control | Fixed/designated metadata | `2429` | `426` | `1081` |
| `616` | `5` | `429` Paging button | Fixed/designated metadata | `2430` | `429` | `1082` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

There are no Virgin Objects and no slot-condition rows for either firmware definition.

## Configuration modes

| Mode / modality | Evidence |
| --- | --- |
| Product Programming | implementation evidence; TiLivingLightDisplay workflow |
| USB programming connection | implementation evidence + installation/software documentation |

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `27` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `27` | `N_1` | `0..9` | `0` | N; Configurator N(0-9) |
| `27` | `N_2` | `0..9` | `0` | N; Configurator N(0-9) |
| `27` | `P` | `0..9` | `0` | P; Configurator P |
| `27` | `M` | `0..6` | Not specified in source | M; (0-6) |
| `616` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `616` | `N_1` | `0..9` | `0` | N; Configurator N(0-9) |
| `616` | `N_2` | `0..9` | `0` | N; Configurator N(0-9) |
| `616` | `P` | `0..9` | `0` | P; Configurator P |
| `616` | `M` | `0..6` | Not specified in source | M; (0-6) |


### Previously reconciled configuration scopes

| Field | Domain | Meaning |
| --- | --- | --- |
| `N_1` | `0..9` | first digit of physical `N` address |
| `N_2` | `0..9` | second digit of physical `N` address |
| `P` | `0..9` | associated entrance-panel / external-unit configurator |
| `M` | `0..6` | physical operating / menu mode selector |


Physical quick configuration is a two-digit `N` plus `P` and `M`. Advanced configuration is performed with the PC software.

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

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


### Object `418` - Open lock control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same level; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Level |


### Object `422` - Addressed autoswitch control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `P` | `0..95` | `0` | External unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |


### Object `426` - Staircase light control

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `N1` | `0..255` | `0` | Internal unit address |
| `N2` | `0..15` | `0` | Internal unit address |
| `SEG_LEV` | `0` = Same; `1` = Riser; `2` = Building; `3` = Backbone | `0` | Segment |


### Object `429` - Paging button

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `M` | `1` = Base; `2` = Advanced | `2` | Modality; mode(Base,Advanced) |
| `AMPL_AREA` | `0..99` | `0` | Amplifier area |
| `AMPL_UNIT` | `0..39` | `0` | Amplifier unit |
| `ADDR_TYPE` | `0` = General; `1` = Ambient; `2` = Point to point | `0` | Addressing type |


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

| Topic | Source-derived detail |
| --- | --- |
| Published fact | `N=0..3999` |
| Published fact | associated external unit `P=0..95` |
| Published fact | hands-free, professional-studio, door-state, beep, slave and Ethernet-call-forwarding flags |
| Published fact | menu preset `0..99` |
| Published fact | ring timeout `1..30` |
| Published fact | call timeout `10..180` |
| Published fact | external-unit timeout `3..90` |
| Published fact | internal-unit timeout `3..90` |
| Published fact | telephone timeout `3..180` |
| Published fact | associated switchboard `0..95`. |

The source contains two unresolved labels for `PEOPLE_S` values `1` and `2`; preserve them as unknown rather than inventing names.

#### Object `418` - Open lock control

| Topic | Source-derived detail |
| --- | --- |
| Published fact | external-unit address `P=0..95` |
| segment level | same level, riser, building, or backbone. |

#### Object `422` - Addressed autoswitch control

| Topic | Source-derived detail |
| --- | --- |
| Published fact | external-unit address `P=0..95` |
| segment level | same, riser, building, or backbone. |

#### Object `426` - Staircase light control

| Topic | Source-derived detail |
| --- | --- |
| Published fact | internal-unit address split across `N1=0..255` and `N2=0..15` |
| segment | same, riser, building, or backbone. |

#### Object `429` - Paging button

| Topic | Source-derived detail |
| --- | --- |
| Published fact | mode `1=Base`, `2=Advanced` |
| Published fact | amplifier area `0..99` |
| Published fact | amplifier unit `0..39` |
| addressing type | General, Ambient, or Point-to-point. |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| `27` | `154` | `2003` | `DOSA_CALL` | `0` = Enable; `1` = Disable (entire reusable range retained) | `0` | Forward incoming call to ethernet |
| `27` | `426` | `4110` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |
| `616` | `154` | `2019` | `DOSA_CALL` | `0` = Enable; `1` = Disable (entire reusable range retained) | `0` | Forward incoming call to ethernet |
| `616` | `426` | `4111` | `N1` | `100`; `101`; `102`; `103`; `104`; `105`; `106`; `107`; `108`; `109`; `110`; `111`; `112`; `113`; `114`; `115`; `116`; `117`; `118`; `119`; `120`; `121`; `122`; `123`; `124`; `125`; `126`; `127`; `128`; `129`; `130`; `131`; `132`; `133`; `134`; `135`; `136`; `137`; `138`; `139`; `140`; `141`; `142`; `143`; `144`; `145`; `146`; `147`; `148`; `149`; `150`; `151`; `152`; `153`; `154`; `155`; `156`; `157`; `158`; `159`; `160`; `161`; `162`; `163`; `164`; `165`; `166`; `167`; `168`; `169`; `170`; `171`; `172`; `173`; `174`; `175`; `176`; `177`; `178`; `179`; `180`; `181`; `182`; `183`; `184`; `185`; `186`; `187`; `188`; `189`; `190`; `191`; `192`; `193`; `194`; `195`; `196`; `197`; `198`; `199`; `200`; `201`; `202`; `203`; `204`; `205`; `206`; `207`; `208`; `209`; `210`; `211`; `212`; `213`; `214`; `215`; `216`; `217`; `218`; `219`; `220`; `221`; `222`; `223`; `224`; `225`; `226`; `227`; `228`; `229`; `230`; `231`; `232`; `233`; `234`; `235`; `236`; `237`; `238`; `239`; `240`; `241`; `242`; `243`; `244`; `245`; `246`; `247`; `248`; `249`; `250`; `251`; `252`; `253`; `254`; `255` | `0` | Internal unit address; reusable default `0` is outside this subset; filter supplies no replacement default |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

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
