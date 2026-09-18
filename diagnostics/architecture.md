# Diagnostic Architecture

The diagnostic protocol is a management layer carried in OpenWebNet frames. It discovers Physical Device instances and projects selected parts of their runtime state without replacing the functional protocol used to operate them.

## Managed systems

A diagnostic `WHO` identifies a management family, not necessarily the diagnostic counterpart of exactly one functional `WHO`. The `EN_SYSTEM.who` field nevertheless stores only one functional `WHO` on each `OPEN.db` system record and must be reported literally before broader domain coverage is inferred.

The complete set of non-empty diagnostic mappings in `OPEN.db` is:

| Diagnostic `WHO` | Explicit `EN_SYSTEM.who` | `OPEN.db` system records | `managed` | Direct `EN_OPEN` associations |
| ---: | --- | --- | ---: | ---: |
| `1001` | `1` | Light and Automation system; Interface AUTOM L3; Interface AUTOM L4 | `1` | `65` on the combined system |
| `1004` | `4` | Thermoregulation | `1` | `46` |
| `1008` | `8` | Video Door entry system and telephony | `1` | `1` |
| `1013` | `13` | Integration Functions | `1` | `0` |
| `1018` | `18` | Energy Management system | `1` | `65` |
| `1022` | `22` | Multimedia System | `0` | `0` |
| `1023` | `23` | Access Control | `1` | `65` |
| `1027` | `27` | Nurse Call basic level system | `0` | `9` |

For diagnostic `WHO 1001`, these are the only explicit associations in `OPEN.db`: all three rows contain `EN_SYSTEM.who = 1`. The database contains no `EN_SYSTEM` row with `who = 2`, and no other table contains a literal `1001` mapping.

The description “Light and Automation system” and observed protocol behavior establish that the management family extends across Lighting and Automation, whose functional protocols use `WHO 1` and `WHO 2` respectively. That broader coverage is not encoded as a second `EN_SYSTEM` mapping and must not be presented as though `OPEN.db` directly pairs `WHO 2` with `WHO 1001`.

The `managed` flag and direct frame associations are separate evidence. `WHO 1027`, for example, is marked unmanaged but has nine service/diagnostic operations; `WHO 1008` is managed but has only one directly associated service-identification template. A diagnostic-family value alone does not establish support for the common Device interview.

The 65-operation set associated with the combined Lighting/Automation system is also associated with Energy Management and Access Control. Thermoregulation shares 46 of those operations and adds a dedicated scan form. This is direct implementation evidence for a common management model across those families. It remains Device- and firmware-dependent at runtime.

The full functional namespace and association matrix is maintained in [MyHOME_Suite `OPEN.db` Coverage](../functional/open-db-coverage.md).

## Evidence layers

| Layer | Establishes | Does not independently establish |
| --- | --- | --- |
| Public protocol | frame language, functional behavior, and explicitly published family-specific fault diagnostics | the MyHOME Suite Device-interview state machines |
| `OPEN.db` | management templates, parameters, sequences, address rules, and timeouts | installed Device values or complete catalogue semantics |
| `OpenQuery.txt` | how MyHOME_Suite reads and orders `OPEN.db` structures | semantics absent from those tables |
| `MHCatalogue.db` | supported Device/firmware/Module/Object/configuration capability | current installed state |
| Captures | actual Device responses and workflow behavior | universal support outside observed products and versions |
| UI | presentation, Module visibility, labels, and editability | wire encoding without correlation |

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

## Canonical diagnostic scenarios

| MyHOME_Suite scenario | Ordered sequences |
| --- | --- |
| `DiagPoint2PointByAddress` | `DiagAddressed` → `DiagKO` → `CloseScan` |
| `DiagPoint2PointWithID` | `DiagAdvanced` → `DiagKO` → `CloseScan` |
| `DiagLocalButton` | `DiagLocalButton` → `DiagKO` → `CloseScan` |
| `ScanPlant` | `ScanAddressed` → repeated `DiagAddressed` → repeated `DiagKO` → repeated `CloseScan` |
| `ScanByAID` | `ScanAID` → repeated `DiagAID` → repeated `DiagKO` → repeated `CloseScan` |

`DiagAdvanced` and `DiagAID` use the same ID-start frame and response ordering. Their sequence metadata differs because `DiagAID` is the repeated interview step inside a plant scan.

## Runtime model projection

| Diagnostic data | Device-model interpretation |
| --- | --- |
| `DIMENSION 1` | item/model identity, physical configurator-position count (`N_CONF`), brand, and line |
| `DIMENSION 2` | firmware version |
| `DIMENSION 3` | hardware version |
| `DIMENSION 4`, `5` | twelve configurator values |
| `DIMENSION 6` | microcontroller version |
| `DIMENSION 7`, `8` | diagnostic bitmasks |
| `DIMENSION 13` | installed Device ID |
| `DIMENSION 30` | internal slot, configured Object or unconfigured Virgin Object, and configured state |
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

System-specific address grammars are documented in [Address Discovery](address-discovery.md). `OPEN.db` defines distinct forms for Lighting/Automation, Thermoregulation, Video Door Entry interfaces, Integration interfaces, Energy Management, and Access Control; it defines no system address rule for every named diagnostic family.

## Timeout model

The canonical implementation defines these diagnostic timing values:

| Timeout | Default | Use |
| --- | ---: | --- |
| `DeviceAnswerTimeOut` | `15` s | first response after addressed or ID start |
| `DeviceMoreAnswerTimeOut` | `20` s | further Device information until end marker |
| `DeviceAnswerTimeOutByButton` | `300` s | first response in local-button mode |
| `DiagTimeOut` | `600` s | maximum diagnosis duration |
| `ScanKOTimeWait` | `8` s | detailed Object/configuration response window |
| `ScanAreaTimeWait` | `8` s | delay/window before the next address/zone |
| `ScanIDWindowDiscoveryTimeWait` | `4` s | response window during massive ID discovery |
| `CloseScenarioTimeWait` | `1` s | close-sequence wait |

These are MyHOME_Suite 3.5.38 defaults, not protocol constants. `OpenQuery.txt` loads timeout actions and status transitions from `AS_TIMEOUT_OPEN_SEQUENCE` rather than hard-coding one global timer.

## Acknowledgements and errors

The `EN_OPEN` registry contains ordinary `ACK` (`*#*1##`) and `NACK` (`*#*0##`) templates, but those rows are not direct members of the canonical diagnostic sequences. Sequence metadata separately defines `status4nack`, error, and timeout transitions. `OPEN.db` also defines structured Object and configuration errors in `DIMENSION 31`, `34`, and `39`.

An implementation must not treat every missing optional response as an error. Support varies by Device, firmware, selected Object, and diagnostic family. A positive end marker can validly follow a response set that omits unsupported optional data.
