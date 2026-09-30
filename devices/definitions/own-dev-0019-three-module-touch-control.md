# Three-module touch control

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0019` | Project identity |
| Technical description | Six-button capacitive multifunction command with configurable button roles | Catalogue + official technical sheet |
| Catalogue item | 1190 - Touch control | Implementation evidence |
| Main catalogue system | Lighting / Automation | Implementation evidence |
| Item model / `modobj` | `27` | Implementation evidence |
| Firmware definition | wildcard `-1.-1` | Implementation evidence |
| Declared slots | `7` | Implementation evidence |
| Configuration modes | Advanced, Physical, Virtual | Implementation evidence |
| Direct / candidate Objects | `12` / `15` | Implementation evidence |
| Virgin Object | Soft-Touch command virgin (`521`) | Implementation evidence |
| Categories | Commands, Multifunction, User Interface, Scenarios | Product and capability model |

This definition covers the three-module touch-control cluster, not the four-module sibling. The product has six capacitive command zones plus a separate user-interface-settings slot. Each command zone can take one of a broad set of command roles; the catalogue models that flexibility through direct reusable Objects plus a Soft-Touch Virgin Object candidate set.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino Axolute | `HC/HS4657M3` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| BTicino Axolute | `HD4657M3` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| Legrand Arteor | `573912` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| Legrand Arteor | `573913` | Documented commercial identity | Catalogue + `MQ00110` technical sheet |
| Legrand Arteor | `574091` | Shared technical item | Implementation evidence; direct sheet correlation pending |
| Legrand Arteor | `574591` | Shared technical item | Implementation evidence; direct sheet correlation pending |

## Documentation

| Document | Coverage | Status |
| --- | --- | --- |
| `MQ00110_f_EN` | 4657M3/M4 and Arteor touch-control family | [Archived original](../../sources/devices/documents/device-doc-touch-control-mq00110-f-en/MQ00110_f_EN.pdf) |
| MyHOME catalogue `HPML0714` | `573912` / `573913` occur on printed pp. 16, 19 / PDF pp. 16, 19 | [Archived MyHOME catalogue](../../sources/devices/documents/device-doc-myhome-catalogue-hpml0714/BR-MyHOME-HPML0714.pdf) |

The technical sheet distinguishes the three-module version by its six capacitive buttons. It documents physical and MyHOME_Suite configuration and a multifunction command set spanning lighting, automation, locking, scenarios, video-door-entry and sound functions.

## Physical and electrical characteristics

For the three-module family, `MQ00110` documents six capacitive buttons with blue indication. The BTicino HC/HS/`HD4657M3` variants are specified at a lower maximum SCS current than the `573912`/`573913` Arteor variants in the same sheet. These product-level electrical differences do not change the shared catalogue item but are a reminder that shared OpenWebNet capability does not imply identical hardware construction.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1190` | Implementation evidence |
| main system | lighting_automation / Automation | Implementation evidence |
| `AS_ITEM_SYSTEM.modobj` | `27` | Implementation evidence |
| family | `1` | Implementation evidence |

## Firmware and slot model

The catalogue uses wildcard firmware version/revision `-1.-1` for firmware id `154` and declares seven slots. Wildcard means applicability is not constrained to one concrete reported version; it must not be rendered as a literal installed firmware version.

Slots `1..6` correspond to the six command positions. Slot `7` is the fixed User interface settings Object (`480`).

## Direct Objects and Virgin Object candidates

Direct catalogue Objects include:

| Object | Role | Slots |
| ---: | --- | --- |
| `410` | Light control | `1..6` |
| `411` | Automation control | `1..6` |
| `412` | Lock/unlock actuator control | `1..6` |
| `413` | Scenario module control | `1..6` |
| `414` | Scheduled scenario | `1..6` |
| `415` | Scenario PLUS Lighting Management | `1..6` |
| `416` | Scheduled scenario PLUS | `1..6` |
| `418` | Open lock control | `1..6` |
| `419` | Sound diffusion control | `1..6` |
| `426` | Staircase light control | `1..6` |
| `427` | Floor call control | `1..6` |
| `480` | User interface settings | `7` |

Virgin Object `521`, Soft-Touch command virgin, allows these command roles:

| Object | Candidate role |
| ---: | --- |
| `410` | Light control |
| `411` | Automation control |
| `412` | Lock/unlock actuator control |
| `413` | Scenario module control |
| `414` | Scheduled scenario |
| `415` | Scenario PLUS Lighting Management |
| `416` | Scheduled scenario PLUS |
| `417` | AUX control |
| `418` | Open lock control |
| `419` | Sound diffusion control |
| `421` | Cyclic autoswitch control |
| `426` | Staircase light control |
| `427` | Floor call control |
| `489` | Open lock command on session |

Combining the direct set with Virgin-only roles yields 15 distinct candidate Objects. The catalogue contains empty slot-condition records on some direct Light-control and Floor-call rows; because the condition text is empty, this definition treats them as source artifacts rather than as hidden semantic predicates.

## Firmware-scoped physical configuration

| Field | Domain | Meaning |
| --- | --- | --- |
| `AID` | implementation identity token | Device identity |
| `A` | `0..9` plus `GEN` / `GR` / `AMB` forms | environment / area selector |
| `PL` | physical light-point domain | light point |
| `M` | `0`, `1`, `3`, `4`, `6`, `O/I`, `SU_GIU`, `SU_GIU_M`, `CEN` | physical mode selector |
| `SET` | `0..7` | user-interface settings configurator |

The physical sheet and catalogue agree that the Device can be configured physically or through software. Software configuration should preserve the richer reusable Object model rather than reducing every button to the physical `A` / `PL` / `M` shorthand.

## Reusable Object configuration surfaces

The candidate roles expose different schemas:

| Role | Principal configuration fields |
| --- | --- |
| Light control | modality; addressing type; `A` / `PL` / `G`; installation/destination levels; reference actuator; contact type; optional timing, level and dimming parameters |
| Automation control | UP/DOWN modality; addressing; `A` / `PL` / `G`; installation/destination levels; reference actuator; contact type |
| Lock/unlock control | D/E modality; addressing; `A` / `PL` / `G`; installation/destination levels; contact type |
| Scenario module control | modality; scenario-module address; installation/destination levels; contact type; scenario number; activation delay |
| Scheduled scenario | `A` / `PL`; `CEN` button; Lighting Management mode; contact type |
| Scenario PLUS | ON/OFF regulation mode; scenario number; regulation type; contact type; delay |
| Scheduled scenario PLUS | low/high scenario number; button; Lighting Management mode; contact type |
| AUX control | cyclic/off/on/pulse/up/down family of modes; AUX channel; contact type |
| Open lock control | external-unit P; segment level |
| Sound diffusion control | VOL/ON_OFF; addressing type; `A` / `PF`; follow-me; source/sub-source; channel; contact type |
| Cyclic autoswitch | external-unit P; segment |
| Staircase light | internal-unit `N1` / `N2`; segment |
| Floor call | call type; `N1` / `N2`; segment; input AUX channel |
| Open lock on session | external-unit P |
| User interface settings | unused-button state; feedback update; LED level/fade; standby backlight; backlight delay; proximity enable; signboard behavior |

The Light-control address type explicitly supports address `01..175`, area `00..10` and group `01..255` in the reusable catalogue Object. Other role-specific ranges remain those of their canonical reusable Objects.

## Configuration modes and programming

The catalogue declares Advanced Configuration, Physical configuration and Virtual Configuration. `MQ00110` documents physical configuration and MyHOME_Suite configuration. It also describes self-learning/scenario-oriented behavior at product level. The important representation rule is that one Physical Device owns six independently configurable command slots plus one UI-settings slot.

## Diagnostic applicability

| Surface | Device-specific use | Reference |
| --- | --- | --- |
| `DIMENSION 1` | identify `modobj` 27 and product family | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | observe concrete installed firmware despite wildcard applicability | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | enumerate six command Modules plus UI settings where exposed | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | inspect each configured command address | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | identify selected candidate Object and its configuration | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

Depending on selected Object, individual buttons can participate in lighting, automation, scenario, AUX, sound and video-door-entry functions. The official sheet corroborates this multifunction character. Generic `WHO` frame semantics remain canonical in Functional Protocol.

## Source reconciliation

`MQ00110_f_EN` has been reconciled into the six-command-slot plus UI-settings model:

- self-learning and cyclic self-learning have explicit product programming/deletion procedures and are not merely generic Object alternatives;
- F420/scenario and CEN/MH200N-style functions have product-specific button/address mappings;
- the touch UI supports Device-level LED/status behavior selected by `SET=0..7`, including different feedback/fade/standby arrangements;
- the product provides a temporary cleaning/command-inhibit behavior for the touch surface;
- after installation/power-up the Device performs an automatic calibration interval of roughly two minutes, during which commands/feedback must not be interpreted as normal steady-state behavior;
- installation/destination-level semantics remain part of the selected function family when the Device works across interfaces.

The empty catalogue condition rows remain source artifacts requiring runtime clarification, but the principal published touch-control behavior is now explicit on the Device page.

## Evidence limits and open work

- Obtain a sanitized fingerprint showing all six button slots plus UI slot `7`.
- Correlate `DIMENSION 30` Virgin-Object identifiers with software-selected roles on real hardware.
- Locate direct official documentation for `574091` and `574591`.
- Determine whether the empty condition 4145 rows have any runtime significance.
- Correlate wildcard catalogue applicability with observed firmware versions.

## Sources

- [Device Sources](../../sources/devices/)
- [Canonical MyHOME Suite source set](../../sources/myhome-suite/3.5.38/)
- [Device Database Inventory](../inventory/)
- [Diagnostics](../../diagnostics/)
