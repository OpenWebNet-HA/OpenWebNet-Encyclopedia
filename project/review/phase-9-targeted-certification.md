# Phase 9 Targeted Certification

## Decision and scope

Ready for Phase 10 after the bounded corrections recorded here. No systemic failure was detected in this sample. This is a targeted final ECV/ESG certification, not an exhaustive review or an interoperability certification.

The independent fresh-context reviewer read the canonical ECV and ESG, the Phase 9 packet, relevant ledger records, and only the named canonical pages and their directly relevant source evidence. The verified starting branch head was `db0dc893d569b9b0ad72796b063e92ac8fd4dacc` on `general-once-over`. No earlier certifier summary was used as authority. No routine prose polish, mechanical ESG/link audit, low-risk-page pass, runtime test or new source acquisition was performed.

## Astra adjudications

All four records move from `ASTRA-FINAL-REVIEW` to `Accepted evidence gap`. This closes the review queue, not the underlying factual questions.

| Record | Independent conclusion | Evidence required to resolve the question |
| --- | --- | --- |
| P4-FAC-002 | WHO_1 summary and dimmer section 3.2.20 say 30 seconds; section 3.1.9 says 30 minutes. Both ScenarioDevices copies store the door-lock label and frame but no independent timing proof. Preserve unresolved duration. | Target/Firmware/gateway-specific timing experiment and independently applicable clarification. |
| P4-FAC-003 | OPEN.db labels SYS only as KeyObject system and bounds ADDR to 0..65535. This does not establish namespace equality, functional WHERE conversion or PL=0 meaning. WHO_2 establishes only the local-bus point form. Existing tuple preservation and write gates are necessary. | Original raw tuples and Object/Firmware context; discriminating non-Lighting responses; validated applicable encoder/consumer and controlled operation evidence. |
| P4-FAC-005 | OPEN.db places reset-labelled commands in a retrieval sequence. Neither non-destructive nor destructive behavior follows from that alone. Seven prose gates are intact; three algorithm copies needed an explicit stop branch and were corrected. | Restore-safe before/after experiments or applicable implementation evidence defining effects, scope and repetition. |
| P4-REV-001 | HMAC labels do not match their hex literals. ZigBee UP and reset conflicts persist. WHO_7 camera bounds, WHO_18 forcing duration, WHO_22 malformed frames/tone/unit discrepancies and WHO_24 read/write variants remain source discrepancies. No plausible repair becomes an established frame. | Working authentication vectors; exact product/interface tests and independently applicable source-specific corroboration. |

For P4-REV-001, the more detailed table is not automatically stronger evidence of runtime behavior. The WHO_7 enumerated camera range remains the explicitly documented subset, not proof that the conflicting wider range is impossible. WHO_18's encoded domain remains a published field domain, not a resolved maximum duration. WHO_24's duplicated write-form OFF request remains unsafe to adopt as a read. Generic grammar and SCS values cannot settle the retained ZigBee or malformed-frame questions.

## Exact documentation sample

The following page sections were read for the queue and high-risk sample; unlisted portions or pages are not certified by implication.

| Surface | Exact pages and sampled claims |
| --- | --- |
| Lighting timing and capability | `functional/who-1-lighting/what.md`: timing, door-lock label and command translation; `functional/cross-database-coverage.md`: WHO 1 target-dependent interpretation. |
| Address namespaces and routing | `diagnostics/dim32-addressing.md`; `protocol/addressing.md`: namespace boundary, A/PL grammar and WHO-specific routing; `programming/address-programming.md`; `programming/validation.md`: SYS/ADDR and stop-before-write gates; `reverse-engineering/open-questions.md`: SYS and address-encoding questions. |
| Detailed-read effects | `diagnostics/dim35-configuration.md`: detailed-read sequence and physical-counterpart boundary; all DIM38 prose/algorithm call sites in `guides/program-device.md`, `guides/read-device-configuration.md`, `guides/retrieve-actuator-group-memberships.md`, `guides/retrieve-configured-cen-buttons.md`, `guides/validate-configuration-value.md`, `guides/verify-programming.md`, `guides/troubleshoot-diagnostics.md`. |
| Authentication and variant conflicts | `protocol/authentication.md`: proof layout/identity discrepancy; `protocol/zigbee-interface.md`: scoped transport/address/BUSY boundary and conflict table. |
| Functional discrepancies | `functional/who-7-multimedia-video/README.md`: DIAL set and camera range; `functional/who-18-energy-management/what.md`: historical enumeration and forcing duration; `functional/who-22-sound-diffusion/README.md`: published inconsistencies and source reply addressing; `functional/who-24-lighting-management/dimensions.md`: OFF read and illuminance variants. |
| Correlation and product-specific grammar | `protocol/frame-syntax.md`: selector/address correlation; `functional/who-6-basic-video-door-entry/README.md`: camera OFF, receive-only operations, 4100 sentinel and ACK scope. |
| Capability versus installed behavior | `programming/session-lifecycle.md`: Close sent and persistence limit; `programming/configuration-programming.md`: candidate union and idx=-1; `programming/validation.md`: catalogue consistency versus runtime proof and physical representation; `device-model/configuration.md`: absent physical counterpart; `scenario-engine/execution-model.md`: templates versus runtime and bounded graph-schema absence. |

Representative resolved contradictions independently challenged were request/reply selector and address inequality; WHO_18's four-command enumeration; absent physical match versus advanced-only support; stored capability versus runtime behavior; DIM38 gate propagation; and the L4686SDK send/receive/sentinel/ACK distinctions. N_CONF's physical meaning was not re-certified: the packet already identifies unavailable original hardware diagrams, and this sample did not claim to reproduce them.

## Primary evidence checked

- `WHO_1.pdf`: WHAT summary, address table, sections 3.1.9, 3.1.21 and 3.2.20; `WHO_2.pdf`: WHERE table. No source-table repetition resolves the timing conflict or establishes a management address encoder.
- Both ScenarioDevices databases: `Commands.Name` and `Frame` for the door-lock action. These directly reproduce the label/template claim without demonstrating emission.
- `OPEN.db`: `EN_OPEN` rows 22, 30, 25 and 83; `EN_OPEN_PARAM` SYS/ADDR rows 27/28; `EN_SEQUENCE` DiagKO row 11 and ordered `AS_OPEN_SEQUENCE` members. The reset description and retrieval role genuinely coexist.
- `Hmac.pdf`: A/B definition literals; `OpenWebNet_Zigbee.pdf`: conflicting UP examples and section 9.2/9.3 values, and reset sections 12.2/12.3. Hex literals decode to sope> and cope>, not their accompanying copen/sopen labels.
- `WHO_7.pdf`: printed pages 3-4 WHAT/WHERE tables and the wider camera-flow range; `WHO_18.pdf`: section 3 enumeration and section 5.1.4's 1..254 tens-of-minutes versus 10m to 2h20m prose.
- `WHO_22.pdf`: frequency-step Hz text, preset 55/56 early terminators, speaker-write separators, source read/report forms, and high/low-tone response flows; `WHO_24.pdf`: selector-qualified illuminance examples versus payload form, repeated OFF-value write-form request, and trailing-empty slave-offset request.
- `WHO_4.pdf`: collective fault selector 20 with zone selector 21 reports; `WHO_6_L4686SDK.pdf`: sections 1-2 and address table, including the 4100 receive sentinel and product-scoped acknowledgement meaning.

Primary PDF text was read from the local extracted source text. No diagrams outside these textual claim locations were certified. Existing research-derived observations remain explicitly unreplayed; logical limits on missing metadata do not require inventing a new hardware observation.

## Corrections and systemic-failure assessment

Two factual corrections were necessary: WHAT1000 is not established as dimmer-only, and the WHO_7 DIAL family is `3RC` with each variable digit 1..4, not every integer 311..344. These are recorded as Verified Substantive findings P9-FAC-001 and P9-FAC-002.

Three reference algorithms now return unresolved/unverifiable without sending DIM38 when target effects are unestablished. This completes the known P4-FAC-005 gate requirement within its exact existing call sites and corrects the earlier verification's overstatement. The surrounding seven prose gates already stated the proper boundary.

These defects are bounded to the inspected claims and repeated algorithms. The sampled Phase 4 corrections preserve namespace separation, variant applicability, uncertainty, provenance and capability/runtime distinctions; primary-source counterexamples support their reasoning. No systemic failure requiring a broader certification was detected. This is a sample-based conclusion, not proof of absence of defects elsewhere. No unlimited reread was undertaken.

## Remaining issues and Phase 10 handoff

- Remaining actionable Blocking: 0.
- Remaining actionable Substantive: 0 after the five page corrections.
- New Editorial findings: 0; no routine polish undertaken.
- Remaining Astra queue: 0. Four adjudications are accepted genuine evidence gaps; their original Substantive severity remains in the ledger as history and risk context.
- Genuine gaps include the four adjudicated questions, unavailable sanitized primary captures/controlled tests, application consumers and persistence behavior, exact hardware-document provenance, and the other previously accepted coverage gaps listed in the packet. They are not silently upgraded to established behavior.

Phase 10 may proceed with these explicit limits. It must not represent this targeted review as exhaustive source coverage, tested interoperability, or resolution of the accepted protocol questions. The Phase 8 review packet remains a historical entry-state record; this report and the updated ledger are the Phase 9 exit state.
