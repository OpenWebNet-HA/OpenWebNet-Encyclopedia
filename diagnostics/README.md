# Diagnostics

The diagnostic protocol discovers installed Physical Devices and reads the runtime projection of their firmware, Modules, Objects, addresses, and configuration. It uses ordinary OpenWebNet frame syntax with management-specific `WHO`, `WHAT`, `WHERE`, and `DIMENSION` values.

Diagnostics does not expose the catalogue database directly. It reports instance state that can be interpreted against the canonical **Physical Device → Firmware → Module → Object → Configuration** model described in [`device-model/`](../device-model/).

## Reference

| Subject | Page |
| --- | --- |
| Diagnostic families, sessions, and model projection | [`architecture.md`](architecture.md) |
| Enumeration by Device ID | [`device-discovery.md`](device-discovery.md) |
| Discovery using an address | [`address-discovery.md`](address-discovery.md) |
| Full Device interview | [`device-interview.md`](device-interview.md) |
| Diagnostic `WHAT` values | [`what-reference.md`](what-reference.md) |
| Diagnostic `DIMENSION` index | [`dimension-reference.md`](dimension-reference.md) |
| `DIMENSION 1`: Device identity | [`dim1-device-identity.md`](dim1-device-identity.md) |
| `DIMENSION 30`: Modules and Objects | [`dim30-modules.md`](dim30-modules.md) |
| `DIMENSION 32`: Module addressing | [`dim32-addressing.md`](dim32-addressing.md) |
| `DIMENSION 35`: configuration parameters | [`dim35-configuration.md`](dim35-configuration.md) |

## Principal workflows

1. Select the diagnostic `WHO` for the managed system.
2. Discover Device IDs or identify a Device by address.
3. Start an interview by Device ID, address, or local interaction.
4. Collect identity, version, health, Module/Object, and address responses.
5. Read detailed configuration parameters where required.
6. Close the diagnostic session explicitly when the workflow requires it.

The enumeration and interview workflows are distinct. Enumeration finds installed Device instances; interview expands one selected instance into its runtime model.

## Diagnostic and functional namespaces

A diagnostic `WHO` is a management namespace and is not necessarily equal to the functional `WHO` used to operate the Device. Lighting and Automation, for example, use functional `WHO 1` and `WHO 2` while sharing diagnostic `WHO 1001` in the canonical implementation data.

Never infer the diagnostic family by arithmetically transforming a functional `WHO`. Use an established system mapping.

## Evidence and limits

The frame templates, parameter ranges, sequence membership, and managed-system mappings in this section come primarily from [`OPEN.db`](../sources/myhome-suite/3.5.38/databases/OPEN.db) and [`OpenQuery.txt`](../sources/myhome-suite/3.5.38/support/OpenQuery.txt). Runtime repetition and termination behavior is additionally corroborated by observed traffic.

Catalogue interpretation comes from [`MHCatalogue.db`](../sources/myhome-suite/3.5.38/databases/MHCatalogue.db). Identifier boundaries and cross-source rules are defined once in [Sources and Identifier Boundaries](../device-model/sources-and-identifiers.md).

Observed behavior does not prove universal support across all products, firmware revisions, or diagnostic families. Unknown fields and unverified equivalences remain explicitly unresolved.
