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

The Machine KB has an additional fail-closed privacy validator on its
development branch. That validator remains authoritative for generated
machine-readable artifacts and should be retained when the Machine KB is
eventually integrated with the main repository history.


## Required branch protection

To make deterministic compliance merge-blocking, configure the `main` branch
ruleset or branch protection to require these status checks before merging:

- `Mechanical ESG and ECV compliance`
- `Source integrity and reproducibility`

`Advisory epistemic review` should run on every pull request but must not be a
required factual gate. Its findings require evidence-aware adjudication and can
legitimately remain unresolved when the evidence does not support a stronger
conclusion.
