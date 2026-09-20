# Rejected Relationships

Rejected interpretations are retained because they are plausible enough to be rediscovered from names, equal integers, or incomplete captures. Each entry records why the shortcut fails and the safer replacement.

“Rejected” applies to the stated unconditional interpretation. A narrower relationship can be reconsidered when new evidence addresses the rejecting evidence.

## Database identity and key mistakes

| Rejected interpretation | Conflicting evidence | Safe treatment |
| --- | --- | --- |
| `EN_DEVICE.code → EN_LANGUAGE.code` | Device `code` contains product codes/SKUs; identical column names have unrelated roles | treat `EN_DEVICE.code` as product identity and resolve language through actual localization structures |
| `MHCatalogue.EN_SYSTEM.id_system = OPEN.EN_SYSTEM.id_system` | independent registries show only partial numeric coincidence | correlate systems through meaning, external fields, functional/diagnostic families, and Object membership |
| diagnostic Device `ID = EN_DEVICE.id_device` | wire ID is an installed 32-bit instance identifier; catalogue key identifies a product row | retain both identifiers and correlate through `DIMENSION 1` semantics |
| diagnostic `SLOT = EN_SLOTS.id_slot` | wire slot is Device-local; `id_slot` is an association-row key | correlate with `EN_SLOTS.first_slot` after firmware resolution |
| `EN_KEY_OBJECT.id_key_object = EN_KEY_OBJECT.key_object` | internal and external identifiers are distinct columns and not generally equal | label both namespaces explicitly |
| one `EN_ITEM` identifies one SKU | several branded Device records can share one item | return the candidate Device/SKU set until brand, line, or external evidence narrows it |
| one `EN_FIRMWARE` row has exactly one `EN_BUILDS` row | 19 firmware definitions have no build row and 15 have multiple build rows | model firmware-to-build as zero-to-many |
| no build row means `firmware_b = -1` | absence and explicit sentinel are structurally different states | preserve both cases independently |
| every negative integer is an orphan | `-1` is strongly corroborated as any/unspecified in firmware components | determine sentinel semantics per column before orphan analysis |

## Capability and Module mistakes

| Rejected interpretation | Conflicting evidence | Safe treatment |
| --- | --- | --- |
| `EN_FIRMWARE.slots = COUNT(EN_SLOTS rows)` | one `slot` can offer several Object alternatives | count distinct `first_slot` positions and interpret alternatives separately |
| an `EN_SLOTS` row is one runtime Module | rows represent firmware/Object placement alternatives | build runtime Modules from `DIMENSION 30`, then validate against placement capability |
| `fixed_ko = 1` alone proves the UI field is read-only | visibility, conditions, product context, and UI behavior also contribute | use `fixed_ko` as designated/fixed capability evidence, not a complete UI rule |
| a Virgin Object is the regular configured Object | Virgin Objects describe configurable templates and permitted Object sets; `DIMENSION 30` reports the Virgin Object while the Module is disabled | use `DIMENSION 30.STATE` to select the namespace |
| every Object allowed by a Virgin Object is simultaneously active | association is capability, not runtime selection | resolve one reported configured Object per Module state |

## Protocol interpretation mistakes

| Rejected interpretation | Conflicting evidence | Safe treatment |
| --- | --- | --- |
| `DIMENSION 1.N_CONF` is an Object, class, or form factor | `OPEN.db`, product diagrams, and captures identify a physical-configurator-position count | retain it as the Device-level position count |
| `DIMENSION 30.KEYO` always names `EN_KEY_OBJECT.key_object` | disabled Modules (`STATE = 1`) use the Virgin Object namespace | branch on `STATE` before lookup |
| `DIMENSION 32.SYS` is automatically a functional `WHO` | system grouping and non-Lighting candidate values differ | retain `sys_modobj` as the leading inference pending a discriminating capture |
| diagnostic outer `WHERE` always equals slot `1` address | only selected layouts have been observed; disabled/alternate layouts are untested | treat the correlation as strong but conditional |
| every Module returns `DIMENSION 32` | command-only and optional-response observations contradict universality | model address response as Object/firmware dependent |
| actuators use only `DIMENSION 32`; commands use only `35` | a Module can expose address, indexed properties, both, or neither | determine availability from Object/firmware behavior |
| `DIMENSION 310` is an ordinary `EN_CONF.idx` record | frame has no index and lacks generic parameter metadata | decode per Object/Device family |
| `[FW_VERSION]`, `[HW_VERSION]`, or `[MICRO_VERSION]` is one scalar | parameter descriptions define `Version*Release*Build` | preserve three components and their separators |
| hardware or micro version maps to `EN_PACKAGE`/`EN_FILE` version fields | those rows describe associated packages/files; no hardware/micro catalogue field exists | retain `DIMENSION 3`/`6` as installed-state evidence |
| `DIMENSION 4`/`5` values are proven presence bits | no controlled position/value matrix establishes the encoding | keep contents/presence/combined alternatives open |
| an `ACK` proves effective configuration | acknowledgement, accepted transfer, persistence, and read-back are distinct | verify terminal state and diagnostic read-back |

## Configuration and validation shortcuts

| Rejected shortcut | Why unsafe | Safe treatment |
| --- | --- | --- |
| validate only against `OPEN.db` range | transport capacity can exceed catalogue capability | apply property range, contextual filters, conditions, conversions, and linked rules |
| treat `id_key_object = 0` or `id_firmware = 0` as a broken reference | zero selects the complementary `EN_CONF` ownership branch | validate the exclusive ownership pattern |
| use a global `EN_CONF.idx` lookup | the same index can name different properties across Object/firmware contexts | resolve Device, firmware, Module, Object, and ownership first |
| use `DIMENSION 35.INDEX` without `slot` | repeated indexes can occur across Modules | include Device and slot in the correlation key |
| treat a visible UI field as writable | visibility, editability, fixed state, and conditions differ | corroborate with metadata and observed UI behavior |
| base range alone defines all legal values | `EN_FILTER`, filtered ranges, conditions, and other-property rules narrow it | evaluate the complete validation stack |
| physical counterpart proves active physical configuration | diagnostics reports effective configuration, not necessarily how it was set | distinguish physical capability from active method |
| same effective physical and Virtual value proves identical storage | conversion may produce the same runtime result | classify direct versus converted mapping through controlled changes |

## Cross-database and ScenarioDevices mistakes

| Rejected interpretation | Conflicting evidence | Safe treatment |
| --- | --- | --- |
| equal local primary keys across databases identify the same concept | databases have independent namespaces | connect external identifiers or semantic paths only |
| ScenarioDevices `ObjectId = EN_KEY_OBJECT.key_object` | no declared or complete semantic mapping; models serve different purposes | correlate through literal frames and functional semantics |
| ScenarioDevices `FamilyId = functional WHO` | values are local editor groupings and do not encode `WHO` | derive `WHO` from literal frames/`ChiOpen` where present |
| ScenarioDevices ProgramData and Program Files rows align by `Id` | added rows cause local IDs to diverge | compare the complete semantic hierarchy and non-local fields |
| ProgramData is automatically authoritative because it is writable | revision delta does not prove runtime precedence | trace file opens, synchronization, or loader behavior |
| `Frame IS NULL` means the scenario capability is unsupported | most events/conditions depend on runtime mappings absent from the capability row | preserve the capability and mark the runtime matcher unresolved |
| symbolic frame text is literal OpenWebNet | several stored strings are application tokens | classify literal, symbolic, and absent templates before rendering |
| ScenarioDevices contains saved scenario graphs | schema lacks instances, edges, ordering, and execution state | locate the separate persistence layer |

## Evidence and reasoning failures

| Failure | Why it fails | Correction |
| --- | --- | --- |
| first matching row proves the relationship | exceptions and duplicate namespaces remain invisible | test every populated value and report orphans/cardinality |
| two matching tables are independent corroboration | both may be generated from one internal model | seek a capture, UI observation, product document, or specification |
| silence proves unsupported behavior | selector, state, timeout, or transport may be wrong | record observation capability and terminal evidence |
| a database label is a universal protocol definition | labels describe one implementation and may be incomplete | separate stored implementation semantics from protocol guarantees |
| one Device capture defines a family rule | support and optionality vary by firmware/Object | scope the observation and seek contrasting products |
| correcting a canonical database improves the evidence | mutation destroys source fidelity and may encode false constraints | generate a separate derived artifact with a reproducible transformation |

## Reconsideration rule

A rejected relationship can be reopened only when new evidence directly addresses its rejecting evidence.

The new claim record must include:

1. the exact rejected interpretation being narrowed or replaced;
2. the new source and revision;
3. complete coverage and exceptions;
4. the condition that makes the revised relationship valid;
5. a falsifier;
6. updates to the reference page, [Relationship Register](relationship-register.md), and [Open Questions](open-questions.md).

Do not silently delete a rejection. Preserve why the earlier unconditional claim failed.
