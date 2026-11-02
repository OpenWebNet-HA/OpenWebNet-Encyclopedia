# Firmware Analysis

This section records build-specific implementation findings recovered from manufacturer Firmware packages. It distinguishes static inspection from bounded execution of original helpers, complete process execution and Physical Device observations. The section is designed to retain separate evidence for multiple products and releases.

## Reference

| Firmware | Artifact identity | Methods incorporated | Coverage |
| --- | --- | --- | --- |
| [F454 2.0.51](f454-2.0.51.md) | `firmware-f454-020051`; SHA-256 recorded in the analysis | Static inspection and selected original ARM helper execution | Initial curated integration, [targeted static follow-up](f454-2.0.51-follow-up.md), [dataflow continuation](f454-2.0.51-continuation.md) and [final static pass](f454-2.0.51-final-pass.md); broader reconciliation remains open |
| [MH202 1.0.24](mh202-1.0.24.md) | `firmware-mh202-010024`; exact SHA-256 recorded in the analysis | Static inspection and seven bounded original ARM helper corpora | Overnight examination in progress; reviewed state/routing, scenario, protocol, web and platform continuations with runtime/physical limits |

## Evidence record

Each analysis identifies the exact archive, applicable Device, original file hashes, implementation paths or virtual addresses, examination method and retained evidence. A new release receives its own entry even when filenames or shared functions match an existing release. Whole-file equality, matching code sections and observed runtime equivalence are different claims.

The [review capsules](../../project/review/firmware-analysis/) retain selected analysis excerpts and fingerprints. Original manufacturer packages remain subject to their existing archive/redistribution policy. An excerpt or a hash identifies the basis of a finding; it is not automatically a self-contained execution harness.

| Method | Documentable result | Required boundary |
| --- | --- | --- |
| Static artifact inspection | Contents, configured values and inspected code branches | Deployment, reachability and real service activation remain separate |
| Bounded original-helper execution | Results of the identified instructions with recorded fixtures | Preserve provider, memory, I/O, state and continuation primitives |
| Complete runtime execution | Results under the recorded startup and dependency environment | Emulator/peripheral and scheduling assumptions remain visible |
| Physical Device observation | Captured behavior of the identified Device and Configuration | Do not generalize across products, releases or installations |

## Promotion into reference pages

Firmware analyses preserve implementation evidence and unresolved boundaries. Stable operational semantics belong in the applicable Protocol, Functional Reference, Diagnostics or Programming page. Device-specific build composition, applicability, exceptions and revision evidence belong in the Device definition. These destinations should link back to the applicable analysis rather than duplicate a generic implementation description.

The [Evidence and Confidence policy](../evidence-and-confidence.md) governs promotion. A successful parser, local acknowledgement, recorded write or normal return must not be promoted to physical actuation, delivery or durable installation without evidence for that layer. Reused setup and several reports about the same code are not independent corroboration.

## Remaining work

The first F454 entry incorporates selected findings, not the whole research dossier. Further integration should reconcile the remaining claim groups against existing canonical pages and existing hardware/oracle evidence. Future packages should reuse this evidence structure while retaining their own artifact and runtime scope.

The MH202 continuation now also records a second isolated original helper (packaged copy routine), selected COSO feedback/key-to-pending-state joins, diagnostic WHO/WHERE and final-builder boundaries, and marker/watchdog request policy. These remain build-specific software evidence; complete runtime and physical behavior are unproved.

The later MH202 batch adds UTC calendar comparison, an executed normalizer body with supplied parser fields, prepared diagnostic suffix helpers and a concrete application marker producer. Whole parser/runtime/physical boundaries remain open.

The MH202 continuation further joins numeric-record condition/action prefixes, executes a full selected normal builder/parser-object path, narrows special DIM1 constructor write ownership and adds selected lighting translation. These remain scoped implementation evidence.

The latest MH202 continuation links native common parsing to ordinary normalization, separates IIF operand extraction from line rewriting, identifies diagnostic output/no-data policy and narrows reverse lighting WHAT-prefix construction.

The MH202 component audit distinguishes packaged PHP CLI5.2.13 from Apache module5.1.6 and preserves normal/recovery path identities; later native bracket/level normalization, selected logical folding and lighting pending-state evidence retain their runtime limits.
