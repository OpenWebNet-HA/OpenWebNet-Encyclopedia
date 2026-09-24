# Release Gates and Consumer Contract Status

**Status:** Pre-release. The [Phase 1 consumer contract](consumer-contract.md) and [version policy](schema-versioning.md) are approved for implementation; there is no complete generated Machine KB or published v1 contract yet. Phase 2 must implement and test schemas and finalize exact reference filenames and record shapes. Consumers should not infer a released interface from the current empty output directories.

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

Run the planned `python knowledge/tools/check.py` as the release gate when implemented. Today only the initial `python knowledge/tools/validate_privacy.py` exists for Machine KB outputs, and output directories contain no generated records; a passing scan is not release certification. Publish or merge only after the actual gates pass and the user requests that step.
