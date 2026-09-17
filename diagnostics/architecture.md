# Diagnostic Architecture

The diagnostic protocol is a management layer carried in OpenWebNet frames. It discovers Physical Device instances and projects selected parts of their runtime state without replacing the functional protocol used to operate them.

## Managed systems

A diagnostic `WHO` identifies a management family, not necessarily the diagnostic counterpart of exactly one functional `WHO`. The `EN_SYSTEM.who` field nevertheless stores only one functional `WHO` on each `OPEN.db` system record and must be reported literally before broader domain coverage is inferred.

The complete set of non-empty diagnostic mappings in `OPEN.db` is:

| Diagnostic `WHO` | Explicit `EN_SYSTEM.who` | `OPEN.db` system records | `managed` |
| ---: | --- | --- | --- |
| `1001` | `1` | Light and Automation system; Interface AUTOM L3; Interface AUTOM L4 | yes |
| `1004` | `4` | Thermoregulation | yes |
| `1008` | `8` | Video Door entry system and telephony | yes |
| `1013` | `13` | Integration Functions | yes |
| `1018` | `18` | Energy Management system | yes |
| `1022` | `22` | Multimedia System | no |
| `1023` | `23` | Access Control | yes |
| `1027` | `27` | Nurse Call basic level system | no |

For diagnostic `WHO 1001`, these are the only explicit associations in `OPEN.db`: all three rows contain `EN_SYSTEM.who = 1`. The database contains no `EN_SYSTEM` row with `who = 2`, and no other table contains a literal `1001` mapping.

The description “Light and Automation system” and observed protocol behavior establish that the management family extends across Lighting and Automation, whose functional protocols use `WHO 1` and `WHO 2` respectively. That broader coverage is not encoded as a second `EN_SYSTEM` mapping and must not be presented as though `OPEN.db` directly pairs `WHO 2` with `WHO 1001`.

The `managed` flag separately records whether MyHOME_Suite treats the system as managed in this source revision. Rows with diagnostic `WHO 1022` and `1027` therefore establish named diagnostic families without claiming that MyHOME_Suite implements their complete management workflow.

The common mechanics documented here form the implementation model shared by these diagnostic families. A mapping in `OPEN.db` is not proof that every Device implements every operation or `DIMENSION`.

## Session roles

| Role | Responsibility |
| --- | --- |
| Programmer | Starts discovery or interview, selects a Device or Module, collects responses, and closes the operation |
| Device | Responds with identity and runtime state using the selected diagnostic `WHO` |
| Gateway/transport | Carries OpenWebNet frames; it does not assign catalogue meaning to diagnostic values |

The wire protocol does not add a transaction identifier. An implementation should therefore serialize ambiguous diagnostic workflows on one connection, associate responses with the active operation, and apply the sequence timeouts defined by the implementation data.

## Session lifecycle

A typical workflow has four phases:

1. release prior scan state with `WHAT 12` where enumeration is used;
2. start discovery or interview;
3. collect zero or more responses, including repeated `DIMENSION` frames;
4. observe `WHAT 4` as the Device end marker or terminate with `WHAT 6` when aborting.

Enumeration by ID adds a per-Device `WHAT 11` frame so an already reported Device does not respond again during the current pass. See [Device Discovery](device-discovery.md).

## Runtime model projection

| Diagnostic data | Device-model interpretation |
| --- | --- |
| `DIMENSION 1` | item/model identity, unresolved `N_CONF`, brand, and line |
| `DIMENSION 2` | firmware version |
| `DIMENSION 3` | hardware version |
| `DIMENSION 4`, `5` | twelve configurator values |
| `DIMENSION 6` | microcontroller version |
| `DIMENSION 7`, `8` | diagnostic bitmasks |
| `DIMENSION 13` | installed Device ID |
| `DIMENSION 30` | internal slot, Object number, configured state |
| `DIMENSION 32` | internal slot, system selector, encoded address |
| `DIMENSION 35` | configuration index, internal slot, value |
| `DIMENSION 310` | Object-specific parameter without a generic index |

The projection is intentionally partial. A Physical Device can expose several Modules and functional addresses, while discovery and interview operate on one Device-level identity or address selection.

## Address roles

`WHERE` has several roles in the diagnostic protocol:

- it selects a Device for an addressed interview;
- it identifies the responding Device in many response frames;
- it can be a placeholder in an end marker;
- it does not replace the per-Module address reported by `DIMENSION 32`.

Observed `WHO 1001` traffic often correlates the ordinary diagnostic `WHERE` with the configured address of internal slot `1`. This is a capture-derived hypothesis, not a universal addressing rule.

## Acknowledgements and errors

The canonical implementation includes ordinary `ACK` (`*#*1##`) and `NACK` (`*#*0##`) frames in diagnostic sequence definitions. It also defines structured Object and configuration errors in `DIMENSION 31`, `34`, and `39`.

An implementation must not treat every missing optional response as an error. Support varies by Device, firmware, selected Object, and diagnostic family. A positive end marker can validly follow a response set that omits unsupported optional data.
