# Technical Device description

> This page is a template. Remove this note when creating a Device definition.
>
> This template implements the [Device Definition Presentation Profile](device-definition-presentation-profile.md). Follow that profile when deciding whether information belongs in tables or prose.

## Summary

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-xxxx` | Project identity |
| Technical description | | |
| Commercial identities | | |
| Catalogue item | | |
| Main catalogue system | | |
| Item model / `modobj` | | |
| Firmware definition | | |
| Declared Modules | | |
| Categories | | |

Keep only supported rows. Add Device-specific identity rows when they materially improve identification. Follow with concise explanatory prose when useful.

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino - Axolute | `...` | Established identity | ... |
| Legrand - Céliane | `...` | Established identity | ... |

Use `Brand - Marketed line` when a meaningful marketed line is established, and the brand alone otherwise. Do not expose catalogue placeholders such as `Undefined`, internal line-group labels such as `L/N/NT`, product-family names in place of lines, or raw database IDs in Relationship. List every established or candidate identity. Use prose for package distinctions, source-version naming differences, or unresolved equivalence.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

For multi-product PDFs, record both printed and 1-based PDF pages in Coverage. Link the archived original when retained and keep publisher provenance separately visible.

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| | | |

Use this table when multiple comparable specifications are known. Keep revision/variant differences visible. Use prose for interpretation or an isolated fact that would not benefit from a table.

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | | Implementation evidence |
| Technical item description | | Implementation evidence |
| Item family | | Implementation evidence |
| Main system | | Implementation evidence |
| Item model / `modobj` | | Implementation evidence |

Adapt rows to actual evidence. Do not repeat generic diagnostic frame grammar.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

Remove unsupported columns and add hardware/microcontroller columns where relevant. Distinguish catalogue applicability from observed installed versions.

## Module, Object, and Virgin Object model

### Objects

| Firmware | Relation | Object | Description |
| --- | --- | --- | --- |
| | | | |

### Module / slot relationships

| Slot | Object | Relationship | Description |
| --- | --- | --- | --- |
| | | | |

### Virgin Objects

| Firmware | Relation | Virgin Object | Description | Associated Objects |
| --- | --- | --- | --- | --- |
| | | | | |

Adapt columns when keys, conditions, candidates, or slot relationships matter. Remove empty subsections that do not apply.

## Configuration modes

| Firmware | Mode | Catalogue mode | Description |
| --- | --- | --- | --- |
| | | | |

Use prose to reconcile implementation labels with official terminology. Do not infer programming modality solely from numeric IDs.

## Firmware-scoped configuration

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| | | | |

Add Evidence, Source, or Applicability when needed. Preserve complete legal values, defaults, conditions, and irregularities. Do not expose raw serialization.

## Object configuration surfaces

For a small Object:

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| | | | |

For a larger Object:

| Surface | Fields | Meaning |
| --- | --- | --- |
| Addressing | | |
| Mode and behavior | | |
| Timing and levels | | |
| Scenario / UI | | |
| Sensing / regulation | | |
| Group membership | | |
| Object-specific | | |

Use whichever representation best preserves semantics. State Device/firmware restrictions separately from generic Object capability.

## Conditions, filters, and conversions

### Conditions and conversions

| Slot | Object | Condition | Conversion rule |
| --- | --- | --- | --- |
| | | | |

### Filters

| Object | Field | Filter / allowed subset | Evidence |
| --- | --- | --- | --- |
| | | | |

Remove tables that do not apply. Link generic evaluation semantics to their canonical reference.

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | | [Configuration](../../diagnostics/dim35-configuration.md) |

Keep only applicable surfaces and add others when Device-specific evidence makes them relevant.

## Functional applicability

Describe applicable functional systems or `WHO` families and the conditions under which they apply. Link canonical functional references rather than copying generic protocol semantics.

## Observed behavior and corroboration

Document publishable captures, experiments, and hardware observations that corroborate or challenge source-derived knowledge. Link each observation to the facts it affects.

## Programming

Document Device-specific validation requirements, topology effects, constraints, and programming consequences. Keep generic frame grammar, session mechanics, and algorithms under [Programming](../../programming/).

## Source reconciliation

Reconcile every known applicable source revision. Explain agreements, revision differences, database/document mismatches, commercial relationships, capability/runtime distinctions, unresolved contradictions, and source limitations. Do not silently normalize conflicts.

## Evidence limits and open work

List concrete missing documents, unobserved variants, unresolved conflicts, uncorroborated diagnostics, and experiments still needed. Do not use this as a generic disclaimer.

## Sources

Link canonical implementation sources, archived Device documents, observations, and relevant Encyclopedia references. Do not merely duplicate the Documentation table.
