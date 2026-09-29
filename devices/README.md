# Devices

This section documents actual OpenWebNet-visible products and product variants.

It complements the [Device Model](../device-model/), which defines the abstract **Physical Device → Firmware → Module → Object → Configuration** hierarchy. Pages here apply that model to identifiable real-world products and preserve the evidence needed to identify, understand, configure, and eventually represent those products in software.

## Navigation

| View | Purpose |
| --- | --- |
| [Complete Device Index](index.md) | Ctrl-F-friendly lookup of every known brand / SKU identity and synonym |
| [Device Coverage](coverage.md) | Documentation and research completeness across known Device definitions |
| [Device Definitions](definitions/) | Canonical technical Device pages |
| [Categories](categories/) | Many-to-many browsing by functional category |
| [Device Page Template](contributing/device-page-template.md) | Starting structure for new Device definitions |

## Canonical Device identity

A canonical Device page represents one **technical Device definition**, not one preferred commercial SKU.

One technical Device may have several commercial identities across brands, product lines, regions, or generations. No commercial identity is designated canonical merely because it is the first one documented or because one vendor database uses it as a primary record.

Each Device definition receives a stable project-assigned Device ID. The Device ID is an Encyclopedia identity used to keep references stable; it does not claim vendor authority.

Commercial identity equivalence must be evidence-backed. Relevant evidence may include shared `modobj`, Firmware, Physical Device structure, Modules, Objects, configuration model, programming behavior, and observed hardware behavior.

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
│   └── odl-0042-two-channel-din-lighting-actuator.md
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

A Device can belong to several categories at once, for example **Command**, **Multifunction**, **Lighting**, and **Automation**. Categories may evolve as Device knowledge improves without moving or renaming the canonical Device page.

Likely categories include actuators, commands, multifunction Devices, sensors, thermoregulation, burglar alarm, gateways and interfaces, energy management, scenarios, and audio/video.

## Device page scope

A Device definition should gather the product-specific knowledge needed to answer questions such as:

- Which commercial identities refer to this Device?
- How can it be identified from OpenWebNet diagnostics or implementation data?
- Which Firmware versions and hardware variants are known?
- Which Modules, Objects, functional systems, and `WHO` values can it expose?
- Which diagnostic dimensions and values have been observed?
- How can it be configured physically or virtually?
- Which configuration values and constraints apply?
- Which behaviors are documented, implementation-derived, observed, inferred, or unresolved?
- Which archived official documents apply to it?

Unknown and unresolved observations must be preserved rather than forced into the current interpretation.

Use the [Device Page Template](contributing/device-page-template.md) as the starting point for new definitions.

## Documentation and archival sources

Device-specific official documentation is inventoried and, where appropriate, archived under [Device Sources](../sources/devices/).

Each Device page should link directly to every applicable archived PDF or other retained original document. Preserve distinct revisions rather than replacing older documents when a newer version appears.

Implementation artifacts such as `MHCatalogue.db`, `OPEN.db`, and rules databases may establish product identity, capability, or configuration facts. Those facts belong on Device pages with their evidence status and provenance; the original artifacts remain under [Sources](../sources/).

## OWN Device Library

The human-facing Device definitions are intended to become the canonical curation layer for the **OWN Device Library** release.

The Device Library will be a deterministic, runtime-oriented derivative optimized for product identification, function lookup, configuration validation, and other software use cases. Its build pipeline will remain separate from the OWN Machine KB pipeline and will have its own release cadence.

The Device Library must be derived from reviewed Encyclopedia knowledge. It must not be a mechanical redistribution or schema translation of a vendor database.
