# Reverse Engineering

This section documents how relationships and protocol semantics are recovered from MyHOME Suite implementation data, public specifications, observed traffic, product documentation, and application behavior.

It is not a second protocol reference. Established results belong in the relevant [Protocol](../protocol/), [Functional](../functional/), [Device Model](../device-model/), [Diagnostics](../diagnostics/), [Programming](../programming/), [Scenario Engine](../scenario-engine/), or [Internals](../internals/) section. This section records how those results were reached, how confidence is assigned, and which questions remain unresolved.

## Reference

| Subject | Page |
| --- | --- |
| Investigation workflow and promotion criteria | [Methodology](methodology.md) |
| Evidence classes, confidence levels, and claim records | [Evidence and Confidence](evidence-and-confidence.md) |
| Reconstructing undeclared relationships safely | [Database Relationship Reconstruction](database-relationship-reconstruction.md) |
| Consolidated established and inferred relationships | [Relationship Register](relationship-register.md) |
| Rules for correlating independent database namespaces | [Cross-Database Correlation](cross-database-correlation.md) |
| Capturing, segmenting, and interpreting protocol behavior | [Capture Analysis](capture-analysis.md) |
| Designing tests that distinguish competing explanations | [Hypothesis Testing](hypothesis-testing.md) |
| Rejected relationships and recurring failure modes | [Rejected Relationships](rejected-relationships.md) |
| Questions that still require evidence | [Open Questions](open-questions.md) |

## Core rule

Numeric equality is a lead, not a relationship.

A relationship becomes usable only after its namespace, scope, conditions, cardinality, and evidence are known. A value can be:

- a local SQLite primary key;
- an external catalogue number;
- a Device-local internal slot;
- an installed Device identifier;
- an OpenWebNet wire field;
- a sentinel such as `0` meaning “not applicable”;
- a category or matching identifier local to one application model.

Equal values in different categories do not establish equivalence.

## Investigation cycle

1. Preserve and fingerprint the source evidence.
2. Record the raw observation before interpreting it.
3. Identify every possible namespace for each value.
4. propose competing explanations;
5. test key coverage, cardinality, context, and counterexamples;
6. seek an independent source such as a frame, UI observation, product diagram, or public specification;
7. classify the result and document its conditions;
8. promote stable conclusions to the appropriate reference page;
9. retain rejected alternatives so they are not rediscovered later.

## Output of an investigation

A useful result includes:

- the exact source revision and fingerprint;
- raw values or frames;
- candidate namespaces;
- proposed source and target fields;
- join or decoding conditions;
- observed cardinality and unresolved rows;
- supporting and contradicting evidence;
- confidence classification;
- the test that could disprove the conclusion.

Unknown fields remain unknown. Reverse engineering is successful when it narrows uncertainty honestly, not when every value has been assigned a convenient label.
