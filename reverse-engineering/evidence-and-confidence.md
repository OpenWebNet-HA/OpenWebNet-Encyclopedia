# Evidence and Confidence

Confidence describes the support for a claim in its stated scope. It does not describe how plausible the claim sounds.

## Evidence classes

| Evidence | Strongest contribution | Principal limitation |
| --- | --- | --- |
| Declared schema | explicit local keys and constraints | many catalogue relationships are undeclared |
| Complete data pattern | coverage, cardinality, sentinels, and revision-specific facts | cannot prove application behavior alone |
| Application query | intended joins, selected columns, and ordering | may be incomplete or unused |
| Literal frame template | exact wire grammar and stored functional context | does not prove Device support |
| Public specification | published protocol meaning | may predate implementation behavior |
| Observed traffic | actual ordering and Device behavior | scoped to observed products and versions |
| MyHOME Suite UI | labels, visibility, and editability | does not establish wire encoding alone |
| Product documentation | hardware layout and physical configuration | may not describe Virtual behavior |

## Confidence levels

| Level | Meaning |
| --- | --- |
| Established | direct stored fact, declared relationship, exact source fingerprint, or unambiguous frame |
| Corroborated | independent evidence supports one interpretation and tested values agree |
| Strongly inferred | complete structural pattern strongly favors one explanation, but a decisive observation is missing |
| Hypothesis | plausible explanation with incomplete coverage or viable alternatives |
| Unknown | evidence cannot distinguish the candidates |
| Rejected | tested interpretation conflicts with schema, coverage, range, or observed behavior |

“Established” remains revision-scoped. A row count established for MyHOME Suite 3.5.38 is not a universal MyHOME limit.

## Claim record

Each important inference should record:

| Field | Purpose |
| --- | --- |
| Claim | precise relationship or semantic statement |
| Source | originating files, tables, frames, or observations |
| Scope | version, Device class, firmware, system, and session context |
| Conditions | discriminators, sentinels, or prior resolution required |
| Cardinality | one-to-one, one-to-many, conditional, or polymorphic |
| Supporting evidence | positive observations |
| Counterevidence | exceptions or conflicts |
| Confidence | one level from the table above |
| Falsifier | observation that would disprove or narrow the claim |
| Destination | reference page containing the promoted result |

## Conditional relationships

Some of the strongest recovered relationships are conditional rather than ordinary foreign keys.

For example:

```text
DIMENSION 30.KEYO
    STATE = 1 → EN_KEY_OBJECT.key_object
    STATE = 0 → EN_VIRGIN_OBJECT.virgin_key_object
```

The discriminator is part of the relationship. Omitting it converts a correct polymorphic mapping into an incorrect unconditional join.

Likewise, `EN_CONF` ownership depends on zero sentinels, and `DIMENSION 35.INDEX` becomes meaningful only after Device, firmware, internal slot, Object, and ownership scope have been resolved.

## Negative evidence

Absence can narrow a hypothesis only when the observation window was capable of showing the expected event.

- No response after an invalid address does not prove that no Device exists.
- No `DIMENSION 35` in one interview does not prove that the Object has no configuration.
- No matching row in ScenarioDevices does not prove that the functional command is unsupported.
- No declared foreign key does not prove that two catalogue tables are unrelated.

Record the operation, timeout, Device state, and expected visibility before treating absence as evidence.
