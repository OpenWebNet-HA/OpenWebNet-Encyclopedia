# Machine KB Maintenance

## Normal change path

1. Edit the authoritative, non-guide Encyclopedia page and public provenance where a fact changes. Preserve evidence class, namespace, applicability, contradictions, and uncertainty. A guide-only fact first moves to canonical documentation.
2. Identify affected sections and dependent records with `python diff_impact.py --base <base-revision> --head <head-revision>`. Use `--head WORKTREE` for local staged/unstaged changes. The report maps canonical-document changes to stable document, section, chunk, reference, and claim IDs and follows transitive record dependencies. A reported `full_review_required` means the change touches stable identity/source topology or build/schema semantics and must not be treated as a narrow content review.
3. If reviewed structured claim or reference inputs exist, update them alongside the prose. Keep IDs stable when meaning remains stable; record aliases or retirement according to the Phase 1 contract when meaning changes. Never infer a broader rule from a narrow observation.
4. Classify source and fields, exclude private inputs, and sanitize before derivation. Do not put private values in test fixtures, record identifiers, logs, examples, or review notes. Follow the [privacy policy](../../knowledge/policy/privacy.md).
5. Regenerate all impacted outputs through the shared IR with `python build.py`, then run `python check.py`, `python knowledge/tools/validate_consistency.py --report`, and the applicable repository checks. CI must remain offline and model-free.
6. Review the generated diff, provenance, relationships, applicability, and privacy classification. Request focused independent epistemic review for high-risk changes; record findings in [review-ledger.md](review-ledger.md). Commit the documentation and generated changes together after gates pass.

Generated outputs are never hand-edited. Project-control decisions and curated reviewed inputs are edited deliberately and tracked in Git. The final privacy scan remains a last-line gate; passing it does not replace source exclusion, pre-extraction sanitization, schema validation, or referential integrity.
