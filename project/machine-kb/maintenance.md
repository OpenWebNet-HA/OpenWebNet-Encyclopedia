# Machine KB Maintenance

## Normal contributor workflow

1. Edit authoritative, non-guide Encyclopedia documentation and public provenance. Promote a guide-only fact to canonical documentation first.
2. Run python build.py. Generated outputs are never hand-edited.
3. Inspect the complete generated diff, including provenance, relationships, applicability, and privacy classification.
4. Run the single check command: python check.py. It verifies deterministic rebuilds, schemas, freshness, referential integrity, claim consistency, cross-artifact consistency, and privacy.
5. Review affected claims and records with python diff_impact.py --base <base-revision> --head WORKTREE. Treat full_review_required as a full review requirement.
6. Commit authoritative documentation and generated changes together after all checks pass. CI never commits generated artifacts.

CI remains offline and model-free. Follow the [privacy policy](../../knowledge/policy/privacy.md): exclude private inputs and sanitize publishable-sensitive material before derivation; never put private values in fixtures, IDs, logs, examples, or review notes.
