# Devices

This section documents actual OpenWebNet-visible products and product variants.

It complements the [Device Model](../device-model/), which defines the abstract **Physical Device → Firmware → Module → Object → Configuration** hierarchy. Pages here apply that model to identifiable real-world products and preserve the evidence needed to identify, understand, configure, and eventually represent those products in software.

## Navigation

| View | Purpose |
| --- | --- |
| [Complete Device Index](index.md) | Ctrl-F-friendly lookup of every known brand / SKU identity and synonym |
| [Database Inventory](inventory/) | Mechanically extracted catalogue backlog: all commercial records and shared technical-item clusters |
| [Work Queue](work-queue.md) | Curated review state and next actions for the 210 technical-item clusters |
| [Device Coverage](coverage.md) | Documentation and research completeness across known Device definitions |
| [Device Definitions](definitions/) | Canonical technical Device pages |
| [Categories](categories/) | Many-to-many browsing by functional category |
| [Device Definition Presentation Profile](contributing/device-definition-presentation-profile.md) | Normative presentation and information architecture for Device definitions |
| [Device Page Template](contributing/device-page-template.md) | Starting structure implementing the Device presentation profile |

## Completion policy

Device definitions are completion-oriented archival dossiers.

When a canonical implementation database, official document, or publishable observation contains Device-specific information that can be associated reliably with a Device definition, the default is to preserve that information rather than wait for independent confirmation.

Evidence status remains explicit:

- implementation-derived facts are documented as implementation evidence;
- official-document facts retain their document provenance and revision;
- observed facts link to the applicable capture or experiment;
- later corroboration adds provenance to an existing fact rather than replacing its earlier source;
- unresolved or contradictory source material is preserved visibly instead of normalized away.

A known source is not considered processed merely because it appears in the Documentation table or archive. Before a Device definition can be treated as complete for that source revision, the source must be reconciled against the dossier: Device-specific identity, configuration, operating modes, programming workflow, status/diagnostic behavior, revision constraints, contradictions, and open questions must either be incorporated or explicitly judged non-material to the Device page.

“Complete” is always scoped to the source revisions examined. A later catalogue, document revision, firmware, or capture may extend the dossier.

Do not turn Device pages into copies of generic protocol reference material. Device pages document **applicability, Device-specific values, capabilities, constraints, exceptions, and evidence**. Generic frame grammar and field semantics remain canonical under [Functional Protocol](../functional/), [Diagnostics](../diagnostics/), and [Programming](../programming/).

A raw frame belongs on a Device page when it is direct evidence, demonstrates a Device-specific irregularity, or materially improves a Device-specific worked example. Otherwise link to the canonical reference.

## Canonical Device identity

A canonical Device page represents one **technical Device definition**, not one preferred commercial SKU.

One technical Device may have several commercial identities across brands, product lines, regions, or generations. No commercial identity is designated canonical merely because it is the first one documented or because one vendor database uses it as a primary record.

Each Device definition receives a stable project-assigned Device ID. The Device ID is an Encyclopedia identity used to keep references stable; it does not claim vendor authority.

Commercial identity equivalence must be evidence-backed. Relevant evidence may include shared `modobj`, Firmware, Physical Device structure, Modules, Objects, configuration model, programming behavior, official product documentation, and observed hardware behavior.

If later evidence shows that two commercial identities previously treated as equivalent are technically distinct in an OpenWebNet-relevant way, split them into separate Device definitions while preserving the history and provenance of the earlier relationship.

## Directory structure

Keep the section root intentionally small:

```text
devices/
├── README.md
├── index.md
├── coverage.md
├── definitions/
│   ├── README.md
│   └── own-dev-0042-two-channel-din-lighting-actuator.md
├── categories/
│   └── README.md
└── contributing/
    └── device-page-template.md
```

Device definitions use a stable Device ID plus a concise technical descriptor in the filename. The identifier provides durable identity; the descriptor keeps repository browsing human-readable.

Do not put manufacturer or SKU in the canonical path merely to select one commercial identity over another.

## Device Index

[Complete Device Index](index.md) is the primary commercial lookup.

Every known brand / SKU combination gets its own searchable row, even when several rows link to the same Device definition. This makes exact printed references easy to find with Ctrl-F and avoids hiding aliases inside one cell.

## Categories

Categories are navigation views, not canonical ownership.

A Device can belong to several categories at once. Categories may evolve as Device knowledge improves without moving or renaming the canonical Device page.

## Device page scope

A Device definition should exhaust the available Device-specific knowledge needed to answer questions such as:

- Which commercial identities refer to this Device?
- How can it be identified from OpenWebNet diagnostics or implementation data?
- Which Firmware versions and hardware variants are known?
- Which Modules, Objects, Virgin Objects, and functional systems can it expose?
- Which configuration modes, parameters, legal values, filters, conditions, and conversion constraints apply?
- Which diagnostic surfaces are applicable and what Device-specific results are expected?
- Which observed behaviors corroborate or contradict source-derived knowledge?
- Which archived official documents and revisions apply?

Unknown and unresolved observations must be preserved rather than forced into the current interpretation.

Device definitions must follow the [Device Definition Presentation Profile](contributing/device-definition-presentation-profile.md). Use the [Device Page Template](contributing/device-page-template.md) as the starting structure for new definitions.

## Documentation and archival sources

Device-specific official documentation is inventoried and, where appropriate, archived under [Device Sources](../sources/devices/).

Each Device page should link directly to every applicable archived PDF or other retained original document. Preserve distinct revisions rather than replacing older documents when a newer version appears.

When a Device is only one entry within a multi-product PDF - for example a catalogue, compatibility table, or system/product guide - the Device page must identify the relevant printed page or pages and the 1-based PDF page or pages. Record both forms of pagination even when they are the same, so a reader can navigate either the printed document or a PDF viewer unambiguously.

Implementation artifacts such as `MHCatalogue.db`, `OPEN.db`, and rules databases may establish product identity, capability, or configuration facts. Those facts belong on Device pages with their evidence status and provenance; the original artifacts remain under [Sources](../sources/).

## OWN Device Library

The human-facing Device definitions are intended to become the canonical curation layer for the **OWN Device Library** release.

The Device Library will be a deterministic, runtime-oriented derivative optimized for product identification, function lookup, configuration validation, and other software use cases. Its build pipeline will remain separate from the OWN Machine KB pipeline and will have its own release cadence.

The Device Library must be derived from reviewed Encyclopedia knowledge. It must not be a mechanical redistribution or schema translation of a vendor database.
