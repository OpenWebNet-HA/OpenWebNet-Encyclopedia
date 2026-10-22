# Encyclopedia Compliance Checks

This directory contains deterministic and advisory checks used to maintain the
OpenWebNet Encyclopedia.

The governing policies remain the
[Encyclopedia Core Values](../../encyclopedia-core-values.md) and the
[Encyclopedia Style Guide](../../encyclopedia-style-guide.md). These scripts do
not replace review of evidence, applicability, contradictions, or source
authority.

## Hard-fail checks

`check_esg.py` enforces objective presentation and structure rules from the
Encyclopedia Style Guide.

`check_ecv.py` enforces only ECV-derived rules that can be decided
mechanically with high confidence. Its current hard-fail surface is deliberately
narrow and includes required governance files plus concrete privacy-risk values
in human-facing documentation when they are not explicitly identified as
synthetic examples or placeholders.

`audit_source_coverage.py` verifies the canonical source manifest,
cryptographic fingerprints, source availability, and database integrity while
also emitting reproducible evidence probes.

These checks are suitable as required continuous-integration status checks.

## Git storage policy

`check_git_storage.py` rejects ordinary Git blobs larger than 5 MiB and requires
every tracked TSV under `project/review/` to be stored as a canonical Git LFS
pointer. It examines Git objects, so hydrated LFS payloads may exceed the limit.
The staged index is checked by default; changing only the working file or
adding an LFS attribute without staging the conversion cannot satisfy the guard.

The reviewed [legacy baseline](git-storage-baseline.json) records nine existing
large KB files at their exact paths and Git object IDs. These unchanged bytes
are retained to keep this migration bounded. A new version or copy at another
path receives no exemption and must use appropriate storage. Review changes to
this baseline as storage-policy changes, not routine generated updates.

After staging changes, run:

```text
python project/review/checks/check_git_storage.py --base origin/main
python -m unittest discover -s project/review/checks/tests -p test_git_storage.py -v
```

For a committed candidate, add `--head HEAD`. CI checks both the final tree and
new objects reachable between the PR base and its merge checkout, or between
the previous and current pushed commit. Adding a large blob and deleting it in
a later commit still fails. Existing history is not rescanned as new material.
The standalone CI job needs Git objects and comparison history, not LFS payloads.
It does not rewrite history, change tags, or verify remote LFS payload availability.

Use Git LFS for review tables and other large public text artifacts. Retain
private and manufacturer archives in their established external storage. Before
examining review TSV evidence, hydrate it with `git lfs pull`; an LFS pointer is
not the table. The TSV migration preserves paths and exact bytes, including
line endings. Existing large historical blobs remain reachable; new oversized
ordinary blobs are blocked without changing published history or tags.

## Advisory review checks

`audit_epistemic_drift.py` searches for candidates that may indicate
epistemic drift, contradiction, over-generalization, or duplicated protocol
claims.

Its output is a review queue, not a factual verdict. The script intentionally
returns success because the ECV requires semantic questions to be adjudicated
against evidence rather than converted into regex-based truth tests.

`check_ecv.py --show-candidates` also reports possible credential and
installation-identifier material that requires contextual review but is not
safe to reject mechanically.

## Running locally

From the repository root:

```text
python project/review/checks/check_esg.py .
python project/review/checks/check_ecv.py .
python project/review/checks/check_ecv.py . --show-candidates
python project/review/checks/audit_epistemic_drift.py . --show-candidates
python project/review/checks/audit_source_coverage.py
```

The source-coverage audit requires PyYAML.

## GitHub Actions policy

The repository workflow separates required mechanical checks from advisory
epistemic review.

A passing CI run establishes only that the configured deterministic checks
passed. It does not certify that every factual claim is true, complete,
universally applicable, or free of unresolved contradiction.

The hosted source-integrity job verifies the trusted maintainer's exact-commit
`Device catalogue validation` status. The local gate must pass the complete
canonical-source audit and Device/catalogue checks before publishing success.
The status digest covers their tools, manifests, registered local public source
bytes and workflows; changed inputs require another audit. Hosted CI retains
only public status metadata, without private archive probes or credentials.
See [Private catalogue CI result](../../machine-kb/maintenance.md#private-catalogue-ci-result).

The Machine KB has an additional fail-closed privacy validator on its
development branch. That validator remains authoritative for generated
machine-readable artifacts and should be retained when the Machine KB is
eventually integrated with the main repository history.


## Required branch protection

To make deterministic compliance merge-blocking, configure the `main` branch
ruleset or branch protection to require these status checks before merging:

- `Mechanical ESG and ECV compliance`
- `Source integrity and reproducibility`
- `Git storage policy`

`Advisory epistemic review` should run on every pull request but must not be a
required factual gate. Its findings require evidence-aware adjudication and can
legitimately remain unresolved when the evidence does not support a stronger
conclusion.
