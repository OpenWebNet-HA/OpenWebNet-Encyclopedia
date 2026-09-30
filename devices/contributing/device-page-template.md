# Technical Device description

> This page is a template. Remove this note when creating a Device definition.

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-xxxx` | Project identity |
| Technical description | | |
| Commercial identities | | |
| Catalogue item / model | | |
| Firmware applicability | | |
| Categories | | |

Provide a concise description of the Physical Device and its OpenWebNet-visible purpose.

## Commercial identities

List every established or candidate commercial identity for this technical Device. No SKU is canonical merely because it appears first.

| Brand / line | SKU / reference | Relationship | Evidence |
| --- | --- | --- | --- |
| | | | |

## Documentation

Inventory every known applicable official document revision. Link to the archived original under [Device Sources](../../sources/devices/) when retained.

For a multi-product PDF such as a catalogue, compatibility table, or system/product guide, record the exact Device location using both the printed page number and the 1-based PDF page number. Keep both even when they are identical; if the document has no printed pagination, say so explicitly.

| Document | Type | Revision / date | Relevant pages | Status | Source |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Physical and electrical characteristics

Extract product-specific specifications from official documentation. Keep revision-specific differences visible.

## Identity

Record all implementation and protocol identity facts, including item/model, `modobj`, brand, line, and known diagnostic observations.

Do not repeat generic diagnostic frame grammar. Link to [Diagnostics](../../diagnostics/) and retain raw frames only when they are evidence for this Device.

## Firmware and hardware

Record every firmware definition/build and known hardware/microcontroller variant. Distinguish catalogue applicability from observed installed versions.

## Module, Object, and Virgin Object model

Exhaust the Device-specific capability topology from canonical implementation sources. Preserve fixed Objects, alternatives, slot positions, Virgin Objects, and permitted Objects.

## Configuration modes

Record every supported configuration mode and connection/programming modality.

## Firmware-scoped configuration

Extract the complete Device/firmware parameter set, legal values/ranges, defaults, conditions, and known source irregularities.

## Object configuration surfaces

Extract the reusable Object configuration fields applicable to the Device, while distinguishing candidate reusable Object values from Device-specific applicability.

## Conditions, filters, and conversions

Preserve Device-specific conditions, filters, conversion-rule applicability, and irregularities. Link generic evaluation semantics to the appropriate [Device Model](../../device-model/), [Programming](../../programming/), or [MyHOME Suite Internals](../../internals/) reference instead of copying generic algorithms.

## Diagnostic applicability

Use a Device-specific applicability table linking each relevant diagnostic surface to its canonical reference.

## Functional applicability

Describe which functional systems/WHOs can be exposed by this Device and link to their canonical reference pages.

## Observed behavior and corroboration

Link observations to the facts they corroborate or challenge. A capture adds evidence; it does not erase implementation/document provenance.

## Programming

Document Device-specific validation requirements, topology effects, and constraints. Generic frame grammar and session mechanics belong under [Programming](../../programming/).

## Source reconciliation

For every known applicable source revision, record the Device-specific facts that were incorporated and any material discrepancies or questions it raised. A source listed under Documentation is not considered processed until this reconciliation is complete.

## Evidence limits and open work

List missing documents, unobserved variants, unresolved source conflicts, and experiments needed to increase confidence.

## Sources

Link the canonical source set, archived Device documents, and relevant Encyclopedia reference pages.
