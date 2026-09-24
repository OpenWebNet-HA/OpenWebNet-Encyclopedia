# Machine KB Maintenance

## Normal change path

1. Edit the authoritative, non-guide Encyclopedia page and public provenance where a fact changes. Preserve evidence class, namespace, applicability, contradictions, and uncertainty. A guide-only fact first moves to canonical documentation.
2. Identify affected sections and dependent records. Until change-impact tooling exists, inspect relevant links and output families manually; later use the planned diff-impact check to constrain review to changed material and transitive references.
3. If reviewed structured claim or reference inputs exist, update them alongside the prose. Keep IDs stable when meaning remains stable; record aliases or retirement according to the Phase 1 contract when meaning changes. Never infer a broader rule from a narrow observation.
4. Classify source and fields, exclude private inputs, and sanitize before derivation. Do not put private values in test fixtures, record identifiers, logs, examples, or review notes. Follow the [privacy policy](../../knowledge/policy/privacy.md).
5. Regenerate all impacted outputs through the shared IR and run the full deterministic check command once available. Until then, run `python knowledge/tools/validate_privacy.py` and applicable existing repository checks. CI must remain offline and model-free.
6. Review the generated diff, provenance, relationships, applicability, and privacy classification. Request focused independent epistemic review for high-risk changes; record findings in [review-ledger.md](review-ledger.md). Commit the documentation and generated changes together after gates pass.

Generated outputs are never hand-edited. Project-control decisions and curated reviewed inputs are edited deliberately and tracked in Git. The current privacy workflow checks output patterns only; passing it does not certify source exclusion, sanitization, or schema safety. The full maintenance command and source classifications remain future work.
