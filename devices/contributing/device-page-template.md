# Technical Device description

> This page is a template. Remove this note when creating a Device definition.

## Summary

| Field | Value |
| --- | --- |
| Device ID | `OWN-DEV-xxxx` |
| Technical description | |
| Categories | |
| Documentation status | |

Provide a concise description of the physical product and its OpenWebNet-visible purpose.

## Commercial identities

List every established or candidate commercial identity for this technical Device. No SKU is canonical merely because it appears first.

| Brand | SKU / reference | Region / line | Relationship | Evidence |
| --- | --- | --- | --- | --- |
| | | | | |

Use relationship states such as **Established identity**, **Equivalent commercial identity**, **Candidate equivalent**, or **Distinct variant** where appropriate.

## Documentation

Link directly to every applicable archived document under [Device Sources](../../sources/devices/) when the original file is retained. Preserve historical revisions and language variants when they are distinct source documents.

| Document | Type | Revision / date | Language | Archived original | Source record |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Do not replace an older document link merely because a newer revision exists.

## Identification

Document every established or candidate mechanism that can tie an observed Physical Device to this technical Device definition.

| Evidence | Value | Status | Source |
| --- | --- | --- | --- |
| Catalogue / item identity | | | |
| `modobj` / system identity | | | |
| `WHO 1001` identity | | | |
| `DIMENSION 1` identity | | | |
| `N_CONF` | | | |
| Brand / line | | | |
| Other signature | | | |

Keep exact protocol and implementation values unchanged. Distinguish direct product identification from values that only narrow the candidate set.

## Firmware and hardware

Document known Firmware, build, hardware, and microcontroller versions and any applicability differences.

| Version / variant | Evidence | Notes |
| --- | --- | --- |
| | | |

Do not assume that a version present in implementation data has been observed on physical hardware.

## Functional profile

Describe the functions the Device can expose.

| Function / Object | Role | `WHO` | Module / `slot` | Notes |
| --- | --- | --- | --- | --- |
| | | | | |

A Physical Device may expose multiple Modules and Objects with different roles and functional systems. Do not reduce the Device to one address, one Object, or one `WHO`.

## Diagnostic observations

Record product-specific diagnostic behavior, including values needed for identification and fingerprinting.

| Dimension | Parameters | Values / semantics | Status | Evidence |
| --- | --- | --- | --- | --- |
| | | | | |

Previously undocumented dimensions or values should be retained as observations even when their semantics are unknown.

## Addressing and memberships

Document supported addressing forms, group membership, area or environment participation, and any product-specific constraints.

Keep installed-state examples separate from product capabilities.

## Configuration

### Configuration methods

Document the configuration methods supported by the Device, such as physical configurators, virtual configuration, or software-only configuration.

### Physical configuration

| Position / marking | Meaning | Allowed values | Constraints |
| --- | --- | --- | --- |
| | | | |

### Virtual configuration

| Parameter | Scope | Allowed values | Conditions / constraints |
| --- | --- | --- | --- |
| | | | |

Configuration constraints should be recorded precisely enough to support future machine validation. Preserve the source representation where it is necessary to understand a rule.

## Programming

Document Device-specific programming behavior only where it differs from or constrains the canonical [Programming](../../programming/) workflows.

## Observed behavior

Record Device-specific runtime behavior supported by captures or controlled experiments.

Do not generalize an observation to every Firmware or hardware revision without evidence.

## Evidence

Summarize the evidence supporting the page and the role of each source.

Use the standard evidence vocabulary:

- **Published protocol**
- **Implementation evidence**
- **Observed behavior**
- **Inferred**
- **Unresolved**

## Evidence limits

State material gaps, unverified implementation mappings, unsupported variants, conflicting evidence, or other limits that affect interpretation.

## Sources

Link to the relevant canonical entries under [Sources](../../sources/) and to official documents inventoried under [Device Sources](../../sources/devices/).

## Related material

Link to the relevant Device Model, Diagnostics, Programming, Functional Protocol, Reverse Engineering, or Practical Guide pages.
