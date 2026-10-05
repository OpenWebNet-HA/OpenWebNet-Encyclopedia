# Device Definition Presentation Profile

This profile defines how the [Encyclopedia Style Guide](../../project/encyclopedia-style-guide.md) applies to canonical Device definitions under [`devices/definitions/`](../definitions/). It governs presentation and information architecture; truth, evidence, provenance, scope, and epistemic completeness remain governed by the [Encyclopedia Core Values](../../project/encyclopedia-core-values.md).

Device definitions should conform to this profile unless the documented Device provides a substantive reason to differ. A deviation should improve comprehension without discarding structure, provenance, applicability, or uncertainty.

## Normative presentation baseline

This written profile and the [Device Page Template](device-page-template.md) are the normative presentation baseline for every completed canonical Device definition, including the earliest `OWN-DEV` pages.

Existing Device pages are examples, not authorities. A historical page does not create an exemption from the current profile, and no Device page provides evidence for another Device.

## Core presentation rule

**Concrete enumerable facts are structured; interpretation is prose.**

Device identity, commercial references, document inventories, physical/electrical specifications, firmware definitions, configuration domains, topology, mappings, filters, conditions, conversions, and diagnostic applicability should normally use tables when multiple comparable facts exist.

Use prose for explanation, qualification, reconciliation, behavior, programming guidance, uncertainty, limitations, and implications.

The presence of factual information in prose does not satisfy this profile when the information is a structured fact inventory. Conversely, do not force explanatory material into tables merely for visual uniformity.

## Canonical section architecture

A completed Device definition normally uses this order:

1. Summary
2. Commercial identities
3. Documentation
4. Physical and electrical characteristics
5. Identity
6. Firmware and hardware
7. Module, Object, and Virgin Object model
8. Configuration modes
9. Firmware-scoped configuration
10. Object configuration surfaces
11. Conditions, filters, and conversions
12. Diagnostic applicability
13. Functional applicability
14. Observed behavior and corroboration
15. Programming
16. Source reconciliation
17. Evidence limits and open work
18. Sources

The architecture is stable, but content is evidence-driven. Do not invent data to populate a section or table.

## Summary

Begin every Device Summary with a short prose introduction **before the table**. In two or three sentences, explain what the Device is, what it does, and the supported feature or use that distinguishes it. Prefer concrete product language over catalogue or protocol machinery. Keep configuration dependencies and material evidence limits visible; a catalogue-established role may be described as such when product documentation is incomplete. Do not infer physical construction, ratings or runtime support from reusable Object names.

Follow the introduction with `Field | Value | Evidence`. Summarize technical identity and capability without reproducing the dossier. Typical rows include Device ID, technical description, commercial identities, catalogue item, main system, `modobj`, firmware definition, declared Modules, and categories. Additional prose after the table may explain identity or applicability when useful, but does not replace the introductory paragraph.

## Commercial identities

Account for every established or candidate commercial identity. Prefer:

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| | | | |

A plural `References` column is acceptable when several references share one relationship and evidence state. No SKU is canonical merely because it appears first. Use prose for commercial/package distinctions and unresolved equivalence.

### Identity evidence and documentation gaps

An explicit SKU-to-technical-item relationship in a manufacturer catalogue or database establishes a catalogue identity. Attribute that relationship to its source. Missing Device-specific PDFs are documentation-coverage gaps and must not, by themselves, downgrade the identity to candidate or unresolved. Track missing physical specifications and product-specific procedures separately. Reserve candidate or unresolved identity for an inferred relationship or a concrete ambiguity/contradiction about the same product reference in its applicable namespace. A document for a different product with a similar numerical reference is an excluded source match, not an identity contradiction.

### Commercial brand and line vocabulary

The `Brand / line` column is human-facing commercial identity, not raw catalogue metadata.

- Use `Brand - Marketed line` when a meaningful marketed line is established, for example `BTicino - Axolute`, `BTicino - LivingLight`, `BTicino - Matix`, `BTicino - Living Now`, `Legrand - Arteor`, `Legrand - Céliane`, `Legrand - Mosaic`, or `Arnould - Espace Evolution`.
- Use the brand alone when no meaningful marketed line is established. Never expose placeholders such as `Undefined`.
- Prefer the marketed line over internal catalogue group labels. Catalogue groupings such as `L/N/NT` belong in Evidence or Source reconciliation when relevant; use `BTicino - LivingLight` when that mapping is established.
- Do not use product systems or product families such as `MyHOME` or `Classe 300X` as the line unless a source establishes them as the marketed line.
- Do not put reference-shape qualifiers or reconciliation notes such as “catalogue combined code” in the line field. Put them in Relationship, Evidence, or Source reconciliation.
- When publisher terminology conflicts with the catalogue line, show the best-supported marketed line and preserve the conflicting label in Evidence or Source reconciliation.
- `Relationship` must be semantic prose such as `Established identity`, `Established commercial variant`, `Shared technical-item identity`, `Candidate identity`, or `Historical identity`. Raw implementation/database IDs belong in Evidence when useful for provenance.

## Documentation

Inventory every known applicable official revision and keep archival and publisher provenance separately visible. Prefer:

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

For a multi-product PDF, `Coverage` records both printed page and 1-based PDF page. If there is no printed pagination, state that explicitly. Listing a document is not reconciliation; its Device-specific content must also be incorporated or addressed under Source reconciliation.

## Physical and electrical characteristics

When multiple comparable product-specific properties are known, use:

| Property | Value | Evidence |
| --- | --- | --- |
| | | |

Typical properties include mounting, dimensions, supply, current draw, power consumption, channel/output count, contacts, load ratings, radio frequency, operating temperature, sensing range, coverage, local controls, indicators, and configurator positions.

Do not replace a multi-property specification inventory with a paragraph merely because the values can be written in prose. Keep revision-specific and commercial-variant differences visible.

Format exact technical literals in the Value and Evidence cells as inline code when they function as reference data rather than prose. This includes measured values with units (for example `27 Vdc`, `30 mA`, `868 MHz`, `0..40 °C`), exact dimensions/ranges, product/document identifiers, firmware/configuration tokens, and similar machine-like values. Descriptive quantities such as “2 wiring-device modules” may remain prose when the number is part of an ordinary physical description rather than a literal lookup value.

## Identity

Present multiple implementation or protocol identity facts as `Field | Value | Evidence`. Relevant facts can include `EN_ITEM.id_item`, item description/family, system mappings, `modobj`, brand/line data, commercial record counts, and Device-specific diagnostic observations. Implementation identities are not interchangeable with the project Device ID.

## Firmware and hardware

Use structured tables when firmware, build, hardware, microcontroller, or applicability facts need comparison. A common form is:

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Status |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |

Adapt columns to actual source data. Distinguish catalogue applicability from observed installed versions; wildcard and sentinel values remain implementation facts.

## Module, Object, and Virgin Object model

Exhaust the Device-specific capability topology. Use tables for repeated Firmware/Object, slot/Object, and Virgin Object relationships. Keep **Physical Device**, **Firmware**, **Module**, **Object**, **Virgin Object**, and implementation `slot` semantics distinct. Do not flatten candidate Objects into unconditional Device capability.

## Configuration modes

Use a table when several modes or associations exist, for example `Firmware | Mode | Catalogue mode | Description`. Use prose to reconcile implementation labels with product terminology. Do not infer a programming modality solely from a numeric mode identifier.

## Firmware-scoped configuration

Present the Device/firmware configuration surface semantically. Prefer:

| Field | Domain | Default | Meaning |
| --- | --- | --- | --- |
| | | | |

Add Evidence, Source, or Applicability when source differences matter. Preserve legal values, ranges, defaults, conditions, and irregularities. Do not expose raw database serialization such as storage type IDs, visibility flags, encoded range rows, or similar machinery unless it is itself relevant.

## Object configuration surfaces

Document reusable Object configuration separately from Device/firmware applicability. For small surfaces use `Field | Domain | Default | Meaning`. For larger Objects use `Surface | Fields | Meaning` and group fields by concepts such as addressing, behavior, timing/levels, scenario/UI, sensing/regulation, group membership, and Object-specific settings.

Reusable Object capability does not establish that every value applies to every Device/firmware relationship.

When a Device page includes a `Reconciled Object notes` subsection, any enumerable Object families, fields, domains, modes, or capability groupings in that subsection must be presented as a table. Prose may introduce or qualify the table, but must not replace a structured inventory.

## Conditions, filters, and conversions

Keep repeated Device-specific conditions, filters, conversion applicability, and irregularities structured. Use separate tables when conditions and filters represent different concepts. Do not reproduce generic database evaluation algorithms; link to their canonical treatment.

## Diagnostic applicability

Use:

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | | |
| `DIMENSION 2` | | |
| `DIMENSION 30` | | |
| `DIMENSION 32` | | |
| `DIMENSION 35` | | |

Keep only applicable surfaces and add others when relevant. Explain what each surface can establish for this Device; do not copy generic DIMENSION semantics.

## Functional applicability

State which functional systems or `WHO` families the Device can expose and under what topology, Object, firmware, or configuration conditions. Use concise prose, links, or a table when several relationships genuinely require comparison.

## Observed behavior and corroboration

Use this section for publishable captures, experiments, hardware observations, and other direct behavior that corroborates or challenges source-derived knowledge. Link observations to the facts they affect and do not universalize one observation without evidence.

## Programming

Use prose for Device-specific programming consequences, constraints, topology effects, and validation requirements. Tables are appropriate only when the programming information itself forms a repeated structured reference. Generic frame grammar and session mechanics remain under Programming.

## Source reconciliation

Factual tables state what sources establish; this section explains how they fit together. Reconcile agreements, revision differences, database/document mismatches, commercial relationships, capability/runtime distinctions, unresolved contradictions, and source limitations. Do not silently normalize conflicting values.

Every known applicable source revision should be incorporated or explicitly accounted for as non-material, unresolved, or pending review.

## Evidence limits and open work

List concrete remaining gaps such as missing revisions, undocumented commercial identities, unobserved variants, unresolved conflicts, uncorroborated diagnostics, and experiments/captures still needed. Do not use this section as a generic disclaimer for work that should already have been performed.

## Sources

Link canonical implementation sources, archived Device documents, observations, and relevant Encyclopedia references. Do not merely duplicate the Documentation table.

## Evidence and provenance in tables

When rows depend on materially different evidence classes, revisions, or applicability scopes, keep that distinction visible at row level through an Evidence, Source, Status, or Applicability column where useful. Do not mechanically add such a column when one source and scope unambiguously govern the entire table.

## Completeness and review

A Device definition is not presentation-complete merely because all known facts occur somewhere on the page. Presentation completeness requires those facts to use the information architecture defined here, with structured fact inventories kept structured and explanatory material kept explanatory.

A review must check both whether available Device-specific knowledge has been incorporated and whether it is presented in the appropriate form.

The [Device Page Template](device-page-template.md) implements this profile and should be the starting structure for new Device definitions.
