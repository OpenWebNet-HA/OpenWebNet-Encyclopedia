# Phase 4 Factual and Epistemic Audit

This cost-optimized GPT-6 Astra Medium pass continues `general-once-over` from `6b25b581d1a5c8189d9589ec89d8aa844adebb54`. Canonical ECV and ESG were read and used without modification. The [Review Ledger](ecv-esg-review-ledger.md) and [Phase 3 Source-Coverage Audit](phase-3-source-coverage.md) supply the existing inventory, source map and inspection history; they were not restarted.

## Scope and authority

Reasoning concentrated on ECV 1 through 10 and 15 through 20: protocol forms and correlation, namespace/variant applicability, address representation, diagnostic state and programming prerequisites, capability versus observed behavior, and preservation of uncertainty. Architecture issues were recorded only where these claims exposed drift.

Previously established source results were reused. Fresh primary-source reading was limited to the L4686SDK command/receive tables and flows, and the ZigBee serial, address, acknowledgement and neighbor-discovery sections needed for the new scoped reference. Phase 3 conflicts were not re-probed merely to rediscover them. No software consumer, gateway or Physical Device was executed; no new observation is claimed.

This is a targeted factual pass, not a certificate that every claim in every page has been independently revalidated. Unexamined portions listed in Phase 3 remain unexamined unless a finding below states otherwise. No source bytes, protocol values or canonical standards were changed to manufacture a resolution.

## Disposition by major area

| Area | Phase 4 result | Remaining boundary |
| --- | --- | --- |
| Protocol | Corrected selector/address correlation; restricted TCP universality and SCS routing generalization; added canonical ZigBee interface boundary and acknowledgement variants | HMAC constants, variant testing and unexamined detailed flows |
| Functional | Qualified Lighting timing and template authority; corrected WHO 18 enumeration; integrated scoped WHO 6 forms; exposed WHO 13/18/25 variant limits | Conflicting published literals/flows and incomplete detailed ZigBee integration |
| Device Model | Corrected stale N_CONF uncertainty and physical-counterpart absence inference | Product-diagram provenance, firmware selection precedence and complete physical mappings |
| Diagnostics | Preserved STATE-dependent Object/Virgin Object namespaces and optional support; demoted invalid PL=0 functional rendering to an unresolved historical interpretation | SYS identity, raw address decoding and DIMENSION 38 effects |
| Programming | Separated catalogue consistency from runtime proof; separated WHERE from ADDR; excluded idx=-1 from generic indexed writes; qualified close and pre-write timeout effects | Encoding/consumer evidence, persistence, safe recovery and runtime support |
| Scenario Engine | Distinguished stored templates and proposed matching logic from executed behavior; bounded graph-persistence absence claim | Loader, matching and serialization behavior |
| Internals | Used established Phase 3 query/schema authority limits; retained unavailable-consumer boundary | No new application code or trace; algorithms remain unverified |
| Practical Guides | Propagated DIMENSION 38 effect gate to seven call sites and read pseudocode; removed unchanged-Device timeout guarantee | No end-to-end validation; unavailable detail must remain unverifiable |
| Reverse Engineering | Preserved N_CONF research history and existing unknowns; retained firmware sentinel interpretation and unresolved SYS/310 boundaries | Original observation provenance and remaining derivations are not reconstructed here |

## Substantive corrections

- A response need not repeat the request's selector or address. WHO 1004 collective faults and WHO 22 source reports are explicit counterexamples.
- L4686SDK Camera OFF has no WHERE; incoming broadcast call uses special `4100`; receive-only lock notification is not promoted to a send command. Product ACK means bus transmission, not physical completion. Inconsistent endpoint labels and arrows remain visible.
- Lighting WHAT 17 is timed ON with unresolved duration: 30 seconds in the summary versus 30 minutes in section 3.1.9. A ScenarioDevices door-lock label does not settle timing.
- WHO 2 collective local-bus forms are not proven by WHO 1 or a shared management row. Functional WHERE, selection WHERE and DIMENSION 32 ADDR remain distinct; the prior PL=0 rendering cannot be used as functional WHERE 10.
- Catalogue checks, ownership unions, stored templates, sent close frames and proposed matching algorithms no longer imply runtime proof. Firmware idx=-1 fields are not generic unsigned INDEX writes.
- A missing physical counterpart is not proof of advanced-only capability. The stale N_CONF unknown label is aligned with its established interpretation without closing the diagram provenance gap.
- Historical WHO 18 commands are the four-value set `57`, `58`, `59`, `510`, not the inclusive range between them.
- Detailed-read guides now preserve DIMENSION 38 reset/select ambiguity and require applicable evidence before sending it.
- The ZigBee reference establishes serial/interface applicability, product/unit addressing, BUSY/NACK behavior and separate management/discovery scope without copying installation identifiers or unrelated radio/bootloader internals.

## Unresolved evidence and final review

The following ledger records have status `ASTRA-FINAL-REVIEW`. Their guardrails are implemented; their semantics are not declared resolved.

| Record | Exact issue | Evidence needed |
| --- | --- | --- |
| P4-FAC-002 | Lighting WHAT 17 seconds/minutes conflict | Target-scoped timing experiment or independently applicable authoritative clarification |
| P4-FAC-003 | DIMENSION 32 SYS namespace and ADDR conversion; historical PL=0 example; unsupported WHO 2 collective routing generalization | Raw tuples with exact Object/firmware context, discriminating non-Lighting responses, applicable encoder/consumer or controlled operation evidence |
| P4-FAC-005 | DIMENSION 38 retrieval role versus reset/select effect | Restore-safe before/after experiments or applicable implementation evidence defining effects and scope |
| P4-REV-001 | HMAC identity constants; ZigBee UP 1/2 and reset 0/75; retained WHO 7 address, WHO 18 duration, WHO 22 frame/tone/unit and WHO 24 read/write conflicts | Working authentication vectors; product/interface-specific tests; remaining detailed source adjudication. No repair selected from plausibility alone |

The other Phase 3 gaps remain genuine: sanitized replayable captures; exact product-diagram references; application binaries/resources and consumer traces; controlled Device/firmware/gateway/transport matrix; configurator encoding, DIMENSION 310, hardware-version mapping and firmware-selection precedence; physical-to-advanced conversion coverage; scenario loading/matching/persistence; missing dedicated namespace references and legacy authentication algorithm; ZigBee publication provenance and unexamined detailed source material. No new artifact closed these gaps in Phase 4.

## Phase 5 handoff

P4-ARC-001 records the naturally exposed architecture work for Sol:

1. Preserve the DIMENSION 38 canonical applicability caveat in independently executable guide copies; their former drift had substantive consequences.
2. Keep common SCS routing models subordinate to WHO- and variant-specific support; shared concepts are not shared permission to emit frames.
3. Keep N_CONF identity and physical-counterpart definitions canonical, with landing pages and programming classifications consuming the same epistemic state.
4. Use the ZigBee interface page for cross-cutting applicability. Add future operation details under their canonical WHO or mechanism owner, avoiding a competing full protocol reference.

These are consolidation tasks, not authority to resolve the outstanding protocol questions. Phase 2's semantic terminology/transcript questions remain outside this factual pass unless explicitly addressed by a finding.

## Verification

Verification was claim-focused: comparison with established Phase 3 results, targeted source sections, changed canonical/dependent passages and exact generated commit blobs. No routine ESG, link, terminology or full source-fingerprint sweep was rerun. The ledger records evidence, applicability, conclusion, remediation and remaining gaps for all twelve new findings. Remote commit/blob verification establishes preservation of the intended edits, not interoperability or source exhaustion.
