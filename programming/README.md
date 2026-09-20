# Programming

The programming protocol changes the installed configuration of a Physical Device, its Modules, and their selected Objects. MyHOME_Suite combines OpenWebNet management frames from `OPEN.db` with capability and validation data from `MHCatalogue.db`.

Programming is distinct from diagnostics. Diagnostics reports installed state; programming requests a state change. A successful response is not a substitute for validation before transmission or diagnostic read-back afterward.

The canonical cross-area ownership of discovery, interview, configuration reading, runtime control, and programming is summarized in [OpenWebNet Scope and Architecture](../protocol/scope-and-architecture.md).

These are stored Suite management workflows, not established programming support on every OpenWebNet transport. The [ZigBee Interface](../protocol/zigbee-interface.md) exposes separate management and binding mechanisms; neither their existence nor shared functional namespaces establishes `ConfKO` compatibility.

## Reference

| Subject | Page |
| --- | --- |
| Programming families, layers, and source boundaries | [Programming Architecture](architecture.md) |
| Programming states, ordering, and termination | [Programming Session Lifecycle](session-lifecycle.md) |
| Selecting a Device by address, ID, or local interaction | [Device Selection](device-selection.md) |
| Selecting Objects for firmware Modules | [Object Programming](object-programming.md) |
| Programming functional addresses | [Address Programming](address-programming.md) |
| Programming indexed configuration values | [Configuration Programming](configuration-programming.md) |
| Evaluating catalogue ranges, filters, and conditions | [Programming Validation](validation.md) |
| Rejection, timeout, abort, and recovery | [Programming Error Handling](error-handling.md) |
| Diagnostic read-back and state comparison | [Programming Verification](verification.md) |
| Programming `WHAT` values | [Programming `WHAT` Reference](what-reference.md) |
| Programming `DIMENSION` values | [Programming `DIMENSION` Reference](dimension-reference.md) |

## Canonical scenarios

`OPEN.db` defines three read/write programming scenarios:

| Scenario | Ordered sequences |
| --- | --- |
| `ConfPoint2PointByAddress` | `ConfAddressed` → `ConfConfigurators` → `CloseConf` |
| `ConfPoint2PointWithID` | `ConfPoint2PointWithID` → repeated `ConfKO` → `CloseConf` |
| `ConfLocalButton` | `ConfLocalButton` → repeated `ConfKO` → `ConfConfigurators` → `CloseConf` |

The scenario names preserve MyHOME_Suite terminology. “AID” in source descriptions refers to the 32-bit installed Device ID used by the `*[WHO]*9#[ID]*0##` start frame.

The scenarios expose two programming projections:

| Projection | Principal writes | `OPEN.db` description |
| --- | --- | --- |
| Virtual configurators | `DIMENSION 4` and `5` | set Device configurators |
| Advanced Object configuration | `DIMENSION 30`, `32`, and `35` | set Object, address, and indexed parameters |

These projections are not interchangeable. The address-selected scenario contains virtual-configurator transfer but no `ConfKO` sequence. The ID-selected scenario contains advanced Object transfer but no `ConfConfigurators` sequence. The local-interaction scenario contains both.

These names are `OPEN.db` programming-sequence terminology. `MHCatalogue.db` independently registers Virtual Configuration and Advanced Configuration as distinct configuration modes, along with Physical configuration and Product Programming. Do not use one source's label as an undocumented umbrella for the other source's concepts.

## Safe workflow

1. Resolve the diagnostic family and installed Physical Device.
2. Resolve its item, firmware, Modules, Objects, and Virgin Objects.
3. Validate every target Object, address, and parameter in the complete catalogue context.
4. Select the Device using the scenario appropriate to the operation.
5. Transfer only the frames belonging to that scenario and sequence.
6. Preserve warnings, errors, timeout, abort, and terminal responses.
7. Close the programming session.
8. Start a new diagnostic interview and compare the effective state.

Do not infer a programming method from a desired value alone. A value may be representable through physical, virtual, or advanced configuration while the canonical scenarios support different transfer mechanisms.

## Scope boundaries

This section documents programming state machines and writes. Reusable capability belongs under [Device Model](../device-model/); discovery and read-back belong under [Diagnostics](../diagnostics/); shared frame grammar belongs under [Protocol](../protocol/).

The public OpenWebNet PDFs define frame syntax and functional `WHO` behavior but do not define these MyHOME_Suite programming state machines. The authoritative implementation structure for this section is therefore `OPEN.db` plus `OpenQuery.txt`, interpreted with `MHCatalogue.db`, `rules.db3`, observed behavior, and the MyHOME_Suite UI.

Private captures are not stored in the repository. Capture-supported conclusions are stated without installation-specific transcripts.
