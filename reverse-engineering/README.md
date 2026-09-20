# Reverse Engineering

This section explains how OpenWebNet and MyHOME Suite relationships are recovered from implementation data, observed traffic, public specifications, product documentation, and controlled application behavior.

It is a reproducible research record, not a second protocol reference. Stable operational results belong in [Protocol](../protocol/), [Functional Reference](../functional/), [Device Model](../device-model/), [Diagnostics](../diagnostics/), [Programming](../programming/), [Practical Guides](../guides/), [Scenario Engine](../scenario-engine/), or [MyHOME Suite Internals](../internals/). This section preserves the evidence path, confidence boundary, competing explanations, rejected shortcuts, and remaining questions.

## Reference

| Subject | Page |
| --- | --- |
| End-to-end investigation workflow and promotion criteria | [Methodology](methodology.md) |
| Evidence classes, claim-level confidence, negative evidence, and revision drift | [Evidence and Confidence](evidence-and-confidence.md) |
| Recovering undeclared database relationships without altering source evidence | [Database Relationship Reconstruction](database-relationship-reconstruction.md) |
| Consolidated established, inferred, open, and sentinel-dependent relationships | [Relationship Register](relationship-register.md) |
| Safely connecting wire values, catalogue capability, validation, and scenario models | [Cross-Database Correlation](cross-database-correlation.md) |
| Capturing, segmenting, correlating, and publishing runtime traffic | [Capture Analysis](capture-analysis.md) |
| Designing controlled tests that distinguish competing explanations | [Hypothesis Testing](hypothesis-testing.md) |
| Rejected relationships, interpretations, and recurring analytical shortcuts | [Rejected Relationships](rejected-relationships.md) |
| Audited questions that still require evidence | [Open Questions](open-questions.md) |

## Use this section by task

| Goal | Start with | Then consult |
| --- | --- | --- |
| Evaluate a proposed database foreign key | [Database Relationship Reconstruction](database-relationship-reconstruction.md) | [Evidence and Confidence](evidence-and-confidence.md), [Rejected Relationships](rejected-relationships.md) |
| Decode a new management capture | [Capture Analysis](capture-analysis.md) | [Diagnostics](../diagnostics/), [Relationship Register](relationship-register.md) |
| Connect a frame field to a database | [Cross-Database Correlation](cross-database-correlation.md) | [Methodology](methodology.md), [Hypothesis Testing](hypothesis-testing.md) |
| Decide whether a claim is ready for reference documentation | [Evidence and Confidence](evidence-and-confidence.md) | [Methodology](methodology.md) |
| Design the next Device experiment | [Hypothesis Testing](hypothesis-testing.md) | [Open Questions](open-questions.md) |
| Check whether an attractive mapping was already disproved | [Rejected Relationships](rejected-relationships.md) | [Relationship Register](relationship-register.md) |
| See the current state of knowledge quickly | [Relationship Register](relationship-register.md) | [Open Questions](open-questions.md) |

## Core rule

Numeric equality is a lead, not a relationship.

A value can be:

- a database-local primary key;
- an external catalogue number;
- an installed 32-bit Device identifier;
- a Device-local `slot`;
- an OpenWebNet wire field;
- one component of a composite version or address;
- a discriminator-dependent value;
- a sentinel such as `0` meaning “not applicable”;
- a category or matching identifier local to one application model.

A usable relationship must identify the namespace on both sides, required context, cardinality, sentinel rules, evidence, confidence, scope, and falsifier.

## Source-of-truth boundaries

No single source answers every question:

| Source | Strongest authority |
| --- | --- |
| `MHCatalogue.db` | product and firmware capability, Module/Object alternatives, configuration definitions and constraints |
| `OPEN.db` | implementation frame templates, address grammars, management workflows, and timeouts |
| `rules.db3` | linked-property rules for its represented Objects |
| ScenarioDevices databases | scenario-editor capability and literal/symbolic command templates |
| `OpenQuery.txt` | named database reads and selected implementation fields |
| observed traffic | actual installed state and Device behavior |
| MyHOME Suite UI | presentation, visibility, editability, and observed application choices |
| product documentation | physical hardware, configurator layout, and supported installation modes |
| public OpenWebNet material | published wire semantics within its version and scope |

The authoritative conclusion for a question comes from the source capable of answering it, usually corroborated by another independent class.

## Investigation lifecycle

```text
fingerprint source
→ preserve raw observation
→ enumerate namespaces
→ form competing explanations
→ test coverage, cardinality, and sentinels
→ seek independent corroboration
→ run a discriminating experiment
→ assign claim-level confidence
→ promote, retain as open, or reject
```

At each step, preserve enough detail for another investigator to reproduce the decision.

## Claim lifecycle

An investigation normally produces one of four outcomes:

| Outcome | Documentation action |
| --- | --- |
| Operationally established/corroborated | promote the result to its reference section and update the Relationship Register |
| Strongly inferred | document the leading mapping, missing proof, and discriminating test |
| Still ambiguous | retain the candidates and evidence needed in Open Questions |
| Rejected | record the tempting interpretation and conflicting evidence in Rejected Relationships |

New evidence can narrow scope, promote confidence, or reopen a rejection when it directly addresses the rejecting evidence.

## Canonical examples

The section uses several recurring examples because they expose different failure modes:

- `DIMENSION 30.KEYO` shows a discriminator-dependent namespace selected by `STATE`.
- `EN_CONF` shows polymorphic ownership selected by zero sentinels.
- `EN_SLOTS` shows why association-row count is not Module count.
- firmware `V.R.b` shows component sentinels, missing rows, defaults, and one-to-many build metadata.
- `EN_ADDRESS_RULE.object_device_family` shows a valid cross-database relationship supported by full coverage and semantics.
- `DIMENSION 32.SYS` shows why a strong structural candidate must remain inferred until a discriminating capture exists.
- ScenarioDevices revisions show why local primary keys cannot be aligned across files.
- `EN_DEVICE.code → EN_LANGUAGE.code` shows how column-name similarity can manufacture a false relationship.

## Minimum investigation record

A useful contribution includes:

- exact source revision and fingerprint;
- raw values, frames, or UI observations;
- Device, firmware, Module, and session scope where applicable;
- candidate namespaces and alternatives;
- exact SQL, request, or controlled action;
- key coverage, cardinality, sentinels, and exceptions;
- supporting and contradicting evidence;
- confidence and falsifier;
- destination reference page.

Private captures should remain private when they contain installation identifiers. Publish a structure-preserving redaction and retain the original hash/location for audit.

## Terminology

Use the documentation's established terms consistently:

- **Physical Device** for the installed hardware;
- **Module** for a firmware-exposed logical container/function position;
- **`slot`** only for the numeric Device-local position carried by frames or catalogue placement;
- **Object** for `EN_KEY_OBJECT` functionality;
- **Virgin Object** for a configurable functional template, including the identity reported by `DIMENSION 30` while a Module is disabled;
- **Virtual configuration** for configuration performed through MyHOME Suite, contrasted with physical configurators.

Preserve source field names in code formatting even when their historical terminology differs.

## Success criterion

The [18 September 2026 documentation review](documentation-review-2026-09-18.md) records the completed cross-section consistency pass, validation, and remaining evidence limits.

Reverse engineering is successful when uncertainty becomes smaller, explicit, and testable. It does not require assigning a convenient meaning to every value.

A precise unknown with a discriminating experiment is better documentation than an unqualified mapping that happens to fit one capture.
