# Firmware Analysis

This section records build-specific implementation findings recovered from manufacturer Firmware packages. It distinguishes static inspection from bounded execution of original helpers, complete process execution and Physical Device observations. The section is designed to retain separate evidence for multiple products and releases.

## Reference

| Firmware | Artifact identity | Methods incorporated | Coverage |
| --- | --- | --- | --- |
| [F454 2.0.51](f454-2.0.51.md) | `firmware-f454-020051`; SHA-256 recorded in the analysis | Static inspection and selected original ARM helper execution | Initial curated integration; further dossier reconciliation remains open |

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
