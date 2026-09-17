# Diagnostic Architecture

The diagnostic protocol is a management layer carried in OpenWebNet frames. It discovers Physical Device instances and projects selected parts of their runtime state without replacing the functional protocol used to operate them.

## Managed systems

A diagnostic `WHO` identifies a management family, not the diagnostic counterpart of exactly one functional `WHO`. In particular, diagnostic `WHO 1001` covers the Lighting and Automation domain: functional `WHO 1` controls Lighting and functional `WHO 2` controls Automation.

The complete set of non-empty diagnostic mappings in `OPEN.db` is:

| Diagnostic `WHO` | Functional domain or protocols | `OPEN.db` system records | `managed` |
| ---: | --- | --- | --- |
| `1001` | Lighting (`WHO 1`) and Automation (`WHO 2`) | Light and Automation system; Interface AUTOM L3; Interface AUTOM L4 | yes |
| `1004` | Temperature Control (`WHO 4`) | Thermoregulation | yes |
| `1008` | Video Door Entry and telephony (`WHO 8`) | Video Door entry system and telephony | yes |
| `1013` | Integration Functions (`WHO 13`) | Integration Functions | yes |
| `1018` | Energy Management (`WHO 18`) | Energy Management system | yes |
| `1022` | Multimedia (`WHO 22`) | Multimedia System | no |
| `1023` | Access Control (`WHO 23`) | Access Control | yes |
| `1027` | Nurse Call (`WHO 27`) | Nurse Call basic level system | no |

The “Functional domain or protocols” column documents the functional namespaces covered by the management family; it is not a one-to-one database join. `OPEN.db` records `WHO 1` on its combined “Light and Automation system” row and on both Automation interface rows, but that implementation shortcut does not erase functional `WHO 2` or redefine Automation as Lighting.

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
