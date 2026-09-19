# Phase 5 Architecture and Canonicality Audit

This GPT-5.6 Sol High pass continues `general-once-over` from Phase 4 commit `694da72957f584e0c744613a80543ab069767462`. It applies ECV 11 through 16 and 19 to the architecture issues exposed by the Phase 4 factual review. Phase 4 remains the factual authority; no source conflict or ambiguous protocol interpretation was re-adjudicated.

## Scope and method

The pass used the existing inventory, canonical-placement map, Phase 3 source assessment, Phase 4 report, and all Phase 4 ledger findings. Inspection was limited to the pages needed to trace the Phase 4 architecture handoff and the requested boundaries:

- OpenWebNet scope and SCS/ZigBee interface applicability;
- runtime functional control, discovery, interview, detailed configuration reading, and programming;
- Physical Device, Firmware, Module, Object, Virgin Object, Configuration, identities, and addresses;
- catalogue/database entities versus protocol entities;
- canonical placement and substantial duplicate definitions.

No source corpus was re-examined, no new protocol semantics were selected, and no routine factual or mechanical review was repeated.

## Canonical ownership after remediation

| Subject | Canonical owner | Dependent-page rule |
| --- | --- | --- |
| OpenWebNet boundary and cross-area architecture | [OpenWebNet Scope and Architecture](../../protocol/scope-and-architecture.md) | Landing pages link to the shared map rather than redefining the complete architecture. |
| Interface-wide ZigBee applicability | [ZigBee Interface](../../protocol/zigbee-interface.md) | Functional semantics remain under their `WHO`; shared namespace numbers do not import SCS behavior. |
| Runtime commands, events, state, addresses, and functional properties | Relevant [`WHO` directory](../../functional/) | Protocol and interface pages provide context and links, not parallel command tables. |
| Physical Device, Firmware, Module, Object, Virgin Object, and Configuration | [Device Model](../../device-model/) | Diagnostics and Programming consume these definitions without turning database keys into protocol identities. |
| Identifier and cross-source namespace boundaries | [Sources and Identifier Boundaries](../../device-model/sources-and-identifiers.md) | Local pages may state the relevant distinction and link to the complete policy. |
| Discovery and interview | [Diagnostics](../../diagnostics/) | Enumeration, address probing, and one-Device interview remain separate operations. |
| Detailed configuration reading and `DIMENSION 38` uncertainty | [`DIMENSION 35`: Configuration Parameters](../../diagnostics/dim35-configuration.md#reading-detailed-parameters) | Device Model summarizes the catalogue correlation; guides retain executable context and the canonical safety qualification. |
| Configuration writes | [Programming](../../programming/) | Acceptance remains distinct from a fresh diagnostic read-back of effective state. |

## Resolved architecture issues

1. Added one cross-area architecture page defining the encyclopedia boundary, interface/variant scope, mechanism separation, identity/address distinctions, and canonical placement.
2. Linked the root, Protocol, Device Model, Diagnostics, and Programming landing pages to that owner.
3. Removed the duplicate `DIMENSION 38` frame table and `DiagKO` sequence definition from Device Model. The page now retains only the catalogue correlation and links to Diagnostics.
4. Replaced the duplicate detailed-read definition in Device Interview with the workflow boundary and a canonical link.
5. Preserved operational `DIMENSION 38` instructions in Practical Guides while linking their effect qualification to the canonical diagnostic treatment.
6. Linked the ZigBee interface boundary to the six functional namespace owners and added bounded applicability notices to the previously unlinked `WHO 1`, `2`, and `4` landing pages.
7. Updated the functional source-coverage wording to reflect the bounded Phase 4 integration while retaining the incomplete detailed-operation boundary.

The short entity definitions on the individual Physical Device, Firmware, Module, Object, Virgin Object, and Configuration pages remain. They provide local context and agree with the Device Model landing page; they are not competing substantial definitions.

## ECV 19 boundary

No Machine KB representation exists on this branch. Human-to-machine consistency therefore cannot be evaluated or remediated in this pass. The canonical ownership map created here is the required input boundary for a future Machine KB, but it is not evidence that such a representation exists or is synchronized.

## Astra final-review queue

Phase 5 does not change the disposition of any issue requiring competing evidence to be weighed:

| Record | Retained issue |
| --- | --- |
| `P4-FAC-002` | Lighting `WHAT 17` seconds/minutes conflict |
| `P4-FAC-003` | `DIMENSION 32.SYS`, `ADDR` conversion, historical `PL=0`, and unsupported Automation collective routing combinations |
| `P4-FAC-005` | `DIMENSION 38` retrieval role versus reset/select effect |
| `P4-REV-001` | HMAC constants; ZigBee UP and reset conflicts; retained `WHO 7`, `18`, `22`, and `24` contradictions |

All qualifications and guardrails remain in the canonical pages. Phase 5 changed ownership and navigation around them, not their factual status.

## Verification

Verification consists of post-edit internal-link and fragment checks, the deterministic ESG checker, targeted searches for `DIMENSION 38` ownership and ZigBee cross-links, and inspection of all changed passages. These checks establish documentation integrity and canonical placement; they do not close the Phase 3 evidence gaps or certify interoperability.
