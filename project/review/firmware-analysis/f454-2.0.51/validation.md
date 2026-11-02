# Initial Firmware Integration Validation

Branch: `docs/static-firmware-analysis-findings`, created from refreshed `origin/main` at `88d61b3f3bf1456a708b62b0e3de6ed2242960ee`. This is an initial curated integration with local uncommitted changes; no PR, commit, push or source-archive write was performed.

## Performed checks

| Check | Result | Scope |
| --- | --- | --- |
| Encyclopedia Style Guide checker | Pass | Mechanical headings, navigation, notation and presentation checks; advisory candidates are not semantic verdicts |
| Encyclopedia Core Values checker | Pass | Required governance files and mechanically decidable privacy checks |
| Device definition completeness | Pass, `210` definitions | Registered canonical catalogue opened read-only; source material was not written into the repository |
| Device-related unit suite | Pass, `31` tests | Queue gates, definition semantics, catalogue status and index checks |
| Excerpt provenance | Pass, `8` report identities and `8` exact line-byte excerpts | Compared with retained original research reports and excerpt SHA-256 values |
| Selected original files | Pass, `8` identities | Canonical original-image reads through the existing read-only image accessor |
| Original research index | Unchanged | Capsule's recorded index hash and `1917` entries match; no new firmware execution |
| Working diff | Pass | `git diff --check`; no changed `sources/` files |

The initial unprivileged Device test run could not use the private catalogue helper under that execution environment. The approved existing read-only helper then supplied a temporary verified catalogue copy, and Device completeness plus the entire `31`-test suite passed. This was a validation-environment dependency, not an observed firmware or documentation-semantic failure. No credential values or private catalogue data are retained here.

The [independent integration review](review.md) checks the source-to-claim scope and exact final source identities. It identified an abbreviated kernel banner, which was corrected to the exact recorded build version before completion. The alarm row also explicitly names its serializer provider so separate ELF virtual-address namespaces remain visible.

## Pending semantic acceptance

The F454 queue item remains `review-ready` with affected checks pending. Passing mechanical checks and a scoped initial-integration review do not establish that the entire new Firmware source has been reconciled. Authentication, functional matrices, energy, wider web/update/diagnostic paths and cross-reference promotion remain documented work. No full Device reacceptance, firmware coverage percentage, physical behavior or complete execution-reproduction claim is made.

No Git storage-policy result is claimed for unstaged files. The new text artifacts are below the repository's ordinary-blob size threshold; no firmware images or manufacturer binaries were added. Original archives retain their existing private-archive-only policy.
