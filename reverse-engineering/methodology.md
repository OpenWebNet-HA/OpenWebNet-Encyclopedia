# Methodology

Reverse engineering should recover the narrowest explanation supported by the evidence and make that explanation reproducible by another investigator. A plausible label is not a result until its namespace, scope, conditions, and counterexamples have been tested.

## Define the question precisely

Begin with one falsifiable question. Examples include:

- Does `DIMENSION 30.KEYO` change namespace with `STATE`?
- Does `EN_ADDRESS_RULE.object_device_family` refer to `EN_OBJECT_ITEM_FAMILY.id_family`?
- Does an explicit firmware component of `-1` behave as an any/unspecified sentinel?
- Which stored field is the best candidate for `DIMENSION 32.SYS`?

Avoid questions such as “What does this table mean?” Break them into claims that can be checked independently.

For each claim, write down:

1. the proposed source and target namespaces;
2. the expected cardinality and conditions;
3. at least one viable alternative;
4. the observation that would distinguish the alternatives;
5. the scope in which the claim is expected to hold.

## Fix the evidence revision

Record the product version, original path, byte size, and SHA-256 before analysis. The canonical MyHOME Suite 3.5.38 source set is registered in [`sources/manifest.yaml`](../sources/manifest.yaml).

Treat every quantitative statement as revision-scoped. “All 827 rows resolve” means all rows in the fingerprinted 3.5.38 database, not every MyHOME release.

Do not modify canonical databases to add inferred foreign keys, normalize text, repair rows, or encode conclusions. Derived databases, query output, diagrams, and reports belong outside [`sources/`](../sources/).

When an external manual or product sheet is used, preserve its title, product code, revision/date, language, and page or diagram identifier. A later manual may describe different hardware.

## Preserve the raw observation

Interpretation must remain traceable to unchanged evidence.

For database work, retain:

- database and table name;
- schema and declared constraints;
- row key where meaningful;
- raw values, including `NULL`, empty text, `0`, and negative values;
- the exact query used to produce a count or exception list.

For protocol work, retain:

- exact frame bytes or text;
- timestamp, direction, transport connection, and session;
- active diagnostic, programming, or functional operation;
- Device selector and preceding request;
- following response, terminal marker, error, or timeout.

For UI evidence, record the exact label, value, visibility, editability, selected Device, firmware, Module, and configuration mode. For product evidence, distinguish an actual configurator position from a printed label, terminal, button, or indicator.

Never replace the raw value with its interpretation. Store both.

## Enumerate namespaces before joining

The same integer can legitimately occur in unrelated namespaces. A value described informally as an Object might mean:

- `EN_KEY_OBJECT.id_key_object`, an internal row key;
- `EN_KEY_OBJECT.key_object`, an external Object number;
- `EN_VIRGIN_OBJECT.id_virgin_key_object`, an internal row key;
- `EN_VIRGIN_OBJECT.virgin_key_object`, an external Virgin Object number;
- ScenarioDevices `ObjectId`, local to the scenario engine;
- a `slot` carried by a diagnostic frame;
- an OpenWebNet `WHAT`, `WHERE`, or `DIMENSION` value.

Build a namespace ledger before testing equality:

| Property | Record |
| --- | --- |
| Origin | frame field, table column, UI field, or document label |
| Representation | integer, text, composite address, bit field, sentinel |
| Range | declared and observed |
| Scope | global, database-local, Device-local, firmware-local, session-local |
| Stability | persistent identity, revision-local row key, runtime value |
| Candidate meanings | every plausible namespace, not only the preferred one |

Numeric equality is useful for generating candidates. It is not relational evidence by itself.

## Test structural compatibility

For a proposed database relationship, test all populated non-sentinel values, not a sample.

```sql
SELECT child.parent_id, COUNT(*) AS occurrences
FROM child
LEFT JOIN parent ON parent.id = child.parent_id
WHERE child.parent_id IS NOT NULL
  AND child.parent_id <> 0
  AND parent.id IS NULL
GROUP BY child.parent_id;
```

Then test cardinality and ambiguity:

```sql
SELECT child.parent_id, COUNT(*) AS child_rows
FROM child
WHERE child.parent_id IS NOT NULL
GROUP BY child.parent_id
ORDER BY child_rows DESC;
```

The audit must answer:

1. Are types and observed domains compatible?
2. Does every non-sentinel child resolve?
3. Are duplicates compatible with the proposed cardinality?
4. Do `0`, `NULL`, empty strings, or negative values act as data or sentinels?
5. Does the relationship survive selection of the correct firmware, Module, Object, system, or configuration scope?
6. Is there a competing table with equal or better coverage?

Complete coverage establishes structural compatibility, not semantic identity. Table role and independent evidence are still required.

## Model discriminator-dependent relationships

Some relationships are correct only when a discriminator is part of the key. For example:

```text
DIMENSION 30.KEYO
    STATE = 0 → enabled Module → EN_KEY_OBJECT.key_object
    STATE = 1 → disabled Module → EN_VIRGIN_OBJECT.virgin_key_object
```

Similarly, `EN_CONF` ownership is polymorphic:

```text
Object-scoped   → id_key_object resolves, id_firmware = 0
Firmware-scoped → id_key_object = 0, id_firmware resolves
```

Do not force these into unconditional foreign keys. Record the discriminator as part of the relationship.

## Form competing explanations

A hypothesis is useful only when alternatives are explicit. For `DIMENSION 32.SYS`, credible candidates include catalogue `sys_modobj`, database-local system IDs, and functional `WHO`. A Lighting/Automation observation of `1` does not distinguish them.

For each candidate, predict:

- values expected in at least two contexts;
- rows or captures that should not match;
- behavior for sentinels and missing data;
- what would falsify or narrow the proposal.

Prefer a test where the predictions diverge. Repeating a case in which all candidates equal `1` adds coverage but not discrimination.

## Seek independent corroboration

Strong conclusions normally combine evidence classes that do not merely repeat the same implementation assumption.

| Primary observation | Useful independent corroboration |
| --- | --- |
| undeclared column relationship | application query, UI behavior, or complete association path |
| diagnostic field | product diagram, controlled configuration change, or public specification |
| resource-key semantics | literal functional frame and UI placement |
| catalogue condition | observed visibility or accepted/rejected programming value |
| default or sentinel pattern | competing concrete rows and runtime selection behavior |

Two association tables populated by the same loader are valuable structural evidence, but not necessarily independent semantic evidence.

## Search for counterexamples

Test the full populated domain where feasible, including:

- `NULL`, `0`, empty, negative, and default rows;
- duplicate external identifiers;
- Objects assigned to several systems;
- items with several firmware definitions or builds;
- fixed and replaceable Object alternatives;
- Devices with different Module layouts;
- another diagnostic family or firmware revision;
- positive, negative, error, and timeout outcomes.

A counterexample may reject a claim or reveal a missing condition. Do not discard it merely because most rows match.

## Change one variable at a time

Controlled UI and Device tests are strongest when exactly one input changes. Record a baseline, perform one change, repeat the same requests, and diff both traffic and persisted state.

For state-changing tests:

1. read and save the baseline;
2. confirm that the target Device and Module are uniquely identified;
3. change one property;
4. record acknowledgement and terminal state;
5. read the configuration back;
6. restore the baseline when safe;
7. distinguish accepted transfer from effective configuration.

An `ACK` alone is not verification.

## Classify and promote the result

Use the levels in [Evidence and Confidence](evidence-and-confidence.md). Promote a result into reference documentation only when:

- the namespace and scope are explicit;
- known values resolve or exceptions are documented;
- viable alternatives have been tested;
- the claim can be applied without access to the original investigator’s intuition;
- a falsifier or remaining limitation is recorded.

The reverse-engineering section retains the evidence path, unresolved alternatives, and rejected shortcuts. The stable operational conclusion belongs in the relevant Protocol, Device Model, Diagnostics, Programming, Scenario Engine, or Internals page.

## Reproducibility checklist

Before closing an investigation, verify that another person can recover the same conclusion from:

- source fingerprints and revision;
- exact queries, requests, and response context;
- raw values and exception rows;
- namespace and sentinel rules;
- cardinality and coverage counts;
- supporting and contradicting evidence;
- confidence, scope, and falsifier;
- links to the promoted result and the [Relationship Register](relationship-register.md).

Unknown is a valid outcome. A well-bounded unknown is more useful than an attractive but untestable mapping.
