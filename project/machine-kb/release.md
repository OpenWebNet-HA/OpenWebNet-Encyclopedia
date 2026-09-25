# Release Gates and Consumer Contract Status

**Status:** Pre-release. The consumer contract, schemas, privacy source gate, shared IR, deterministic build infrastructure, LLM corpus, retrieval chunks, reference registries, atomic-claim framework, and bounded initial claims for every canonical documentation area are implemented. Full drift/change-impact checks, release CI, candidate certification, and v1 publication remain pending. Consumers should not infer a released interface from these pre-release artifacts.

## Intended consumer contract

The published dataset must be usable by an independent offline consumer without Python, an LLM, MCP, FastMCP, or any network service. It must identify stable entities and records, human-readable labels, source and evidence provenance, epistemic status, applicability/version scope, namespaces, cautions, unresolved states, relationships, and privacy classification. A versioned manifest will identify artifact versions, input revision/digest, hashes, and counts. Generated ownership and compatibility rules will be explicit; source-provenance paths must be public repository-relative paths.

Schema compatibility versions are separate from content revisions recorded by Git and release tags. Never silently repurpose an ID or remove a qualification. Follow the linked Phase 1 policy; a release must verify it against the implemented schemas.

## Release checklist (gates to implement and use before v1)

- [ ] Contract and schemas are reviewed, versioned, and documented with compatibility and migration behavior.
- [ ] Allowed sources and pre-extraction sanitization are checked; prohibited/private sources never enter the IR or derived logs.
- [ ] Build runs offline, without an LLM, from a clean revision; repeated builds are byte-identical and committed artifacts are fresh.
- [ ] Schemas, vocabularies, IDs/aliases, namespaces, provenance, references, claims, and cross-artifact consistency pass validation.
- [ ] Privacy classifications are valid and every generated output passes the final privacy scan; ambiguous results block release.
- [ ] Human review confirms meaningful epistemic/applicability qualifications and representative high-risk claims; independent certification findings are resolved or expressly represented as gaps.
- [ ] Manifest hashes/counts, artifact versions, licensing, release notes, and consumer-facing examples are checked against the actual release revision.
- [ ] The [review ledger](review-ledger.md) is current; the roadmap records exact completion and remaining gaps.

Run `python check.py` for the current deterministic build, schema, referential-integrity, freshness, and privacy gates. It is not yet a release certification: the remaining roadmap phases and independent review must pass before publication or merge, and merge still requires explicit user authorization.
