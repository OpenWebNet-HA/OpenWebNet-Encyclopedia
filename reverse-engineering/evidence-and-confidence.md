# Evidence and Confidence

Confidence describes support for one precisely scoped claim. It is not a score for an entire page, table, or theory, and it does not measure how plausible an explanation sounds.

## Evidence classes

| Evidence | Strongest contribution | Principal limitation |
| --- | --- | --- |
| Source fingerprint | identifies the exact artifact examined | says nothing about semantics |
| Declared schema | explicit local keys, types, and constraints | many catalogue relationships are undeclared |
| Complete data pattern | coverage, cardinality, sentinels, defaults, and exceptions | cannot prove runtime behavior alone |
| Application query | intended joins, selected columns, and ordering | may be incomplete, malformed, dormant, or interpreted elsewhere |
| Literal frame template | exact stored wire grammar and implementation context | does not prove that every Device implements it |
| Workflow metadata | ordering, repetition, direction, timeout, and terminal behavior | iteration counts and Device-specific optionality may remain external |
| Public specification | published protocol terminology and semantics | may predate the implementation or omit private management behavior |
| Observed traffic | actual runtime ordering and Device behavior | scoped to the observed Device, firmware, state, and transport |
| Controlled Device change | causal evidence linking one input to one output | may still be product-specific |
| MyHOME Suite UI | labels, visibility, editability, and application behavior | does not establish wire or storage encoding alone |
| Product documentation | hardware layout and supported physical configuration | may not describe advanced/Virtual configuration or later revisions |

No source class is universally superior. A declared local foreign key is decisive for a database relationship; it cannot establish the meaning of a diagnostic field. A capture proves that one Device emitted a frame; it cannot establish universal support.

## Confidence levels

| Level | Meaning | Appropriate wording |
| --- | --- | --- |
| Established | directly declared, stored, fingerprinted, or unambiguously observed within the stated scope | “defines”, “contains”, “returns in this capture” |
| Corroborated | independent evidence classes support the same interpretation and tested cases agree | “corresponds”, with scope stated |
| Strongly inferred | complete structural evidence strongly favors one candidate, but a decisive observation is missing | “leading mapping”, “strongly supports” |
| Hypothesis | plausible, testable explanation with incomplete coverage or viable alternatives | “may”, “working hypothesis” |
| Unknown | available evidence cannot distinguish meanings | “unknown”; list candidates only if useful |
| Rejected | evidence conflicts with the proposed relationship or interpretation | “does not”, with the conflicting evidence |

“Established” is never automatically universal. A row count established for MyHOME Suite 3.5.38 remains revision-specific. A runtime sequence established for one firmware remains Device- and firmware-scoped unless broader evidence exists.

## Confidence belongs to claims

Separate compound statements before assigning confidence. For example:

1. `DIMENSION 3` has a `Version*Release*Build` logical form — established by `OPEN.db`.
2. It is returned by a particular Device — established only by a capture of that Device.
3. It maps to a catalogue column — currently unsupported because no hardware-version column exists.
4. MyHOME Suite uses it for compatibility selection — open runtime question.

Combining these into “hardware version is established” would hide three different evidence states.

## Claim record

Every important inference should be recoverable from a compact claim record:

| Field | Purpose |
| --- | --- |
| Claim | one precise, falsifiable statement |
| Source | files, tables, rows, frames, captures, UI, or documents |
| Revision | product/database/document/firmware revision |
| Namespace | meaning and scope of every identifier involved |
| Conditions | discriminators, sentinels, and prior resolution required |
| Cardinality | one-to-one, one-to-many, many-to-many, conditional, or polymorphic |
| Coverage | tested rows, Devices, families, and exceptions |
| Supporting evidence | observations favoring the claim |
| Counterevidence | anomalies, conflicts, or untested cases |
| Alternatives | other viable explanations |
| Confidence | one level from the table above |
| Falsifier | observation that would reject or narrow the claim |
| Destination | reference page containing the operational result |

## Worked confidence example: `N_CONF`

The claim “`DIMENSION 1.N_CONF` is the number of physical configurator positions” is corroborated because:

- `OPEN.db` labels it as the number of physical configurators and constrains it to `0`–`12`;
- observed `N_CONF` values agree with product diagrams for Devices with two, three, and seven positions;
- resolved catalogue firmware fields independently produce the same counts in those examples;
- the field is part of Device identity rather than a Module record.

The stronger claim “for every firmware, `N_CONF` equals the count of firmware-scoped physical fields excluding `AID`” is not yet equally supported. Conditional fields and products without diagrams prevent catalogue-wide promotion. The first claim is corroborated; the second remains a strong, testable generalization.

## Worked confidence example: `DIMENSION 32.SYS`

`MHCatalogue.db.EN_SYSTEM.sys_modobj` is the leading candidate because its role, range, external-model character, and Object/system graph fit the wire field. However, common Lighting/Automation observations equal `1`, which also matches other candidate namespaces.

The correct confidence is strongly inferred, not corroborated. A non-Lighting capture whose candidates predict different values is the falsifier/discriminator.

## Independence and circularity

Evidence is independent when it could realistically disagree. A product diagram and a diagnostic capture are independent. Two tables generated from the same internal model may not be.

Watch for circular reasoning:

1. infer an Object from a frame;
2. use that inferred Object to select a database row;
3. cite the selected row as proof that the frame meant that Object.

Break the circle with an independent identifier, controlled change, UI observation, documented product function, or a discriminating capture.

## Negative evidence

Absence is evidence only when the observation window was capable of showing the expected event.

Record:

- exact request and selector;
- Device configuration and readiness;
- expected response and why it was expected;
- timeout source and duration;
- retry count;
- terminal, error, or abort state;
- whether other traffic proved the connection remained healthy.

Examples of unsafe conclusions include:

- no response after an invalid address, therefore no Device exists;
- no observed `DIMENSION 35`, therefore the Object has no configuration;
- no ScenarioDevices row, therefore the functional command is unsupported;
- no declared foreign key, therefore the columns are unrelated.

## Contradictions and exceptions

Do not average conflicting evidence into a vague confidence label. Determine whether the conflict indicates:

- a parsing error;
- a different namespace;
- a missing discriminator;
- firmware or product variation;
- database revision drift;
- conditional application behavior;
- an actual counterexample.

Record exceptions beside the claim. A relationship with explicit conditions can remain established even when an unconditional version is rejected.

## Revision drift

When comparing source revisions:

- never align local primary keys without proof of stability;
- compare semantic paths and external identifiers;
- report additions, removals, and changed values separately;
- retain both source fingerprints;
- do not silently carry a confidence level from one revision to another.

The ScenarioDevices databases demonstrate this requirement: their common semantic hierarchy overlaps even though local row IDs diverge.

## Promotion, demotion, and reopening

Promote a claim when its operational use is clear and the remaining uncertainty no longer changes that use. Demote or narrow it when new evidence reveals an exception. Reopen a rejected relationship only when new evidence addresses the reason it was rejected.

Every promotion should update:

1. the appropriate reference page;
2. the [Relationship Register](relationship-register.md);
3. the relevant entry in [Open Questions](open-questions.md) or [Rejected Relationships](rejected-relationships.md).
