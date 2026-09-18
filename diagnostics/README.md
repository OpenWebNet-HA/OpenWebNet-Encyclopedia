# Diagnostics

The diagnostic protocol discovers installed Physical Devices and reads the runtime projection of their firmware, Modules, Objects, addresses, and configuration. It uses the common OpenWebNet frame language with management-specific `WHO`, `WHAT`, `WHERE`, and `DIMENSION` values.

Diagnostics does not expose the catalogue database directly. It reports installed state that can be interpreted against the canonical **Physical Device → Firmware → Module → Object → Configuration** model described in [`device-model/`](../device-model/).

## Reference

| Subject | Page |
| --- | --- |
| Diagnostic families, sessions, and model projection | [Diagnostic Architecture](architecture.md) |
| Enumeration by Device ID | [Device Discovery](device-discovery.md) |
| Discovery using an address | [Address Discovery](address-discovery.md) |
| Full Device interview | [Device Interview](device-interview.md) |
| Diagnostic `WHAT` values | [Diagnostic `WHAT` Reference](what-reference.md) |
| Diagnostic `DIMENSION` index | [Diagnostic `DIMENSION` Reference](dimension-reference.md) |
| `DIMENSION 1`: Device identity | [`DIMENSION 1`: Device Identity](dim1-device-identity.md) |
| `DIMENSION 30`: Modules and Objects | [`DIMENSION 30`: Modules and Objects](dim30-modules.md) |
| `DIMENSION 32`: Module addressing | [`DIMENSION 32`: Module Addressing](dim32-addressing.md) |
| `DIMENSION 35`: configuration parameters | [`DIMENSION 35`: Configuration Parameters](dim35-configuration.md) |

## Principal workflows

1. Select the diagnostic `WHO` for the managed system.
2. Discover Device IDs or identify a Device by address.
3. Start an interview by Device ID, address, or local interaction.
4. Collect identity, version, health, Module/Object, and address responses.
5. Read detailed configuration parameters where required.
6. Close the diagnostic session explicitly when the workflow requires it.

The enumeration and interview workflows are distinct. Enumeration finds installed Device instances; interview expands one selected instance into its runtime model.

MyHOME_Suite composes these operations into higher-level scenarios:

| Scenario | Sequence composition in `OPEN.db` |
| --- | --- |
| Point-to-point diagnosis by address | addressed interview → detailed configuration reading → close |
| Point-to-point diagnosis by Device ID | ID interview → detailed configuration reading → close |
| Diagnosis by local interaction | local-button interview → detailed configuration reading → close |
| Plant scan by address | address discovery → repeated addressed interviews → repeated configuration reads → repeated close |
| Plant scan by Device ID | ID enumeration → repeated ID interviews → repeated configuration reads → repeated close |

The sequence composition is implementation evidence from `EN_SCENARIO`, `AS_SCENARIO_SEQUENCE`, and `EN_SEQUENCE`. It does not imply that every Device returns every optional response.

## Diagnostic and functional namespaces

A diagnostic `WHO` is a management namespace and is not necessarily equal to the functional `WHO` used to operate the Device. Lighting and Automation, for example, use functional `WHO 1` and `WHO 2` while sharing diagnostic `WHO 1001` in the canonical implementation data.

Never infer the diagnostic family by arithmetically transforming a functional `WHO`. Use an established system mapping.

`OPEN.db` represents Lighting and Automation as one system row whose stored functional `WHO` is `1`; it contains no separate `WHO 2` row. The broader `WHO 1001` Lighting/Automation scope is established by the combined system identity, the independent functional specifications, the catalogue Object model, and observed behavior-not by a second literal database mapping. See [Diagnostic Architecture](architecture.md).

## Source roles

| Source | Role in this section |
| --- | --- |
| [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) | diagnostic systems, frame templates, parameter types and ranges, address rules, sequences, repetition flags, and timeouts |
| [`OpenQuery.txt`](../sources/myhome-suite/3.5.38/support/OpenQuery.txt) | the queries MyHOME_Suite uses to assemble systems, frames, sequences, address rules, and timeout behavior from `OPEN.db` |
| [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db) | Physical Device, firmware, Module, Object, Virgin Object, and configuration interpretation |
| [Public OpenWebNet documents](../sources/openwebnet-public/) | common frame syntax and functional `WHO` behavior; they do not define the MyHOME_Suite diagnostic state machines documented here |
| ScenarioDevices databases | adjacent functional/scenario behavior; not diagnostic Object or configuration identity |
| [`rules.db3`](../sources/myhome-suite/3.5.38/databases/rules.db3) | selected Temperature Control configuration constraints; not a diagnostic frame registry |
| Observed traffic | actual ordering, repetition, values, termination, and Device-specific support |
| MyHOME_Suite UI | displayed Device descriptions, Module visibility/numbering, configuration labels, and editability |

The canonical database copies used for this section match the SHA-256 fingerprints in [`sources/manifest.yaml`](../sources/manifest.yaml).

## Evidence limits

Private packet captures are intentionally excluded from the repository. Capture-supported findings are documented without installation-specific traffic.

Identifier boundaries and cross-source rules are defined once in [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md). In particular, functional `WHO`, diagnostic `WHO`, database system IDs, Object numbers, internal catalogue keys, Device IDs, and functional addresses are independent namespaces unless an explicit correlation is documented.

Observed behavior does not prove universal support across all products, firmware revisions, or diagnostic families. Unknown fields and unverified equivalences remain explicitly unresolved.

## Published family-specific fault diagnostics

[Temperature Control Fault Diagnostics](temperature-control-faults.md) documents the public `WHO 1004` central-unit and zone fault queries, automatic notifications, and active-low bit labels. This is a separate surface from the database-driven Device interview.
