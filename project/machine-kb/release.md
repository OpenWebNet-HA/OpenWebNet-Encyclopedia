# Release Gates and Consumer Contract Status

**Status:** Pre-release, independently certified candidate. The earlier Phase 14 candidate at `95c1b034104512462551adefe87c6a7c468c56f0` failed certification and remains recorded as failed. After Phase 16/16b remediation, independent Phase 15 recertification passed on 2026-09-26 for candidate `5e5dda65b6ba8d5f4da2ec69126d4a9452455c50`. MKB-R03, MKB-R06, and the remaining release checklist still block publication; no merge, tag, release, or v1 interface is implied by certification.

## Intended consumer contract

The published dataset must be usable by an independent offline consumer without Python, an LLM, MCP, FastMCP, or any network service. It must identify stable entities and records, human-readable labels, source and evidence provenance, epistemic status, applicability/version scope, namespaces, cautions, unresolved states, relationships, and privacy classification. A versioned manifest will identify artifact versions, input revision/digest, hashes, and counts. Generated ownership and compatibility rules will be explicit; source-provenance paths must be public repository-relative paths.

Schema compatibility versions are separate from content revisions recorded by Git and release tags. Never silently repurpose an ID or remove a qualification. Follow the linked Phase 1 policy; a release must verify it against the implemented schemas.

## Release checklist (gates to use before v1)

- [ ] Contract and schemas are reviewed, versioned, and documented with compatibility and migration behavior.
- [ ] Allowed sources and pre-extraction sanitization are checked; prohibited/private sources never enter the IR or derived logs.
- [ ] Build runs offline, without an LLM, from a clean revision; repeated builds are byte-identical and committed artifacts are fresh.
- [ ] Schemas, vocabularies, IDs/aliases, namespaces, provenance, references, claims, and cross-artifact consistency pass validation.
- [ ] Privacy classifications are valid and every generated output passes the final privacy scan; ambiguous results block release.
- [ ] Human review confirms meaningful epistemic/applicability qualifications and representative high-risk claims; independent certification findings are resolved or expressly represented as gaps.
- [ ] Manifest hashes/counts, artifact versions, licensing, release notes, and consumer-facing examples are checked against the actual release revision.
- [ ] The [review ledger](review-ledger.md) is current; the roadmap records exact completion and remaining gaps.

Run `python check.py` for the current deterministic build, schema, referential-integrity, freshness, and privacy gates. It is not yet a release certification: the remaining roadmap phases and independent review must pass before publication or merge, and merge still requires explicit user authorization.

## Operational maintenance machinery

Phase 13 provides dedicated Machine KB validation CI: unit tests, schema fixtures, a non-committing build-freshness check, and python check.py. The [maintenance workflow](maintenance.md#normal-contributor-workflow) and release checklist remain mandatory before v1 publication.

Green CI records deterministic/mechanical conformance only. It is not semantic, factual, epistemic, or privacy certification. Phase 16 added contextual installed-Device-ID sanitization/final scanning and context/provenance guards for reviewed claims; independent Phase 15 recertification subsequently passed for candidate `5e5dda65b6ba8d5f4da2ec69126d4a9452455c50`. Remaining release gates still apply.
