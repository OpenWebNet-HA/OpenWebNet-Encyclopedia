# Devices

This section documents actual OpenWebNet-visible products and product variants.

It complements the [Device Model](../device-model/), which defines the abstract **Physical Device → Firmware → Module → Object → Configuration** hierarchy. Pages here apply that model to identifiable real-world products and preserve the evidence needed to identify, understand, configure, and eventually represent those products in software.

## Scope

A Device page should gather the product-specific knowledge needed to answer questions such as:

- What product or SKU is this?
- How can it be identified from OpenWebNet diagnostics or implementation data?
- Which Firmware versions and hardware variants are known?
- Which Modules, Objects, functional systems, and `WHO` values can it expose?
- Which diagnostic dimensions and values have been observed?
- How can it be configured physically or virtually?
- Which configuration values and constraints apply?
- Which behaviors are documented, implementation-derived, observed, inferred, or unresolved?

The page should preserve unknown and unresolved observations rather than forcing them into the current interpretation.

## Page granularity

The normal unit is an identifiable or orderable product SKU.

Closely related variants may share a page when the available evidence does not justify separate treatment or when their differences are fully captured as explicit variants. Distinct products should not be merged merely because they expose similar OpenWebNet behavior.

Use manufacturer directories and normalized SKU filenames, for example:

```text
devices/
    bticino/
        h4652-3.md
        f411u2.md
    legrand/
        067250.md
```

The visible page title and links must use the real manufacturer and SKU, not the normalized filename.

## Device page structure

Use the [Device Page Template](device-page-template.md) as the starting point for new product pages. Sections may be omitted when no evidence exists yet, but unknown or incomplete areas should be made explicit when they are relevant to identification, capability, or configuration.

Important product facts should retain visible provenance and evidence status in accordance with the [Encyclopedia Core Values](../project/encyclopedia-core-values.md).

## Device coverage

[Device Coverage](coverage.md) tracks which products are known and how complete their documentation currently is. It is a research backlog, not a claim that undocumented products are unsupported by OpenWebNet.

## Sources

Device-specific official documentation is inventoried under [Device Sources](../sources/devices/). Product pages should link to the relevant canonical source records rather than duplicate source material.

Implementation artifacts such as `MHCatalogue.db`, `OPEN.db`, and rules databases may establish product identity, capability, or configuration facts. Those facts belong on the Device page with their evidence status and provenance; the original artifacts remain under [Sources](../sources/).

## OWN Device Library

The human-facing Device pages are intended to become the canonical curation layer for a future **OWN Device Library** release.

The Device Library will be a deterministic, runtime-oriented derivative optimized for product identification, function lookup, configuration validation, and other software use cases. Its build pipeline will remain separate from the OWN Machine KB pipeline.

The Device Library must be derived from reviewed Encyclopedia knowledge. It must not be a mechanical redistribution or schema translation of a vendor database.
