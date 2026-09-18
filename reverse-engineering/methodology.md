# Methodology

The objective is to recover the narrowest explanation supported by the available evidence, then test whether it generalizes beyond the observation that suggested it.

## 1. Fix the source revision

Record the product version, original path, byte size, and SHA-256 before analysis. The canonical MyHOME Suite 3.5.38 source set is registered in [`sources/manifest.yaml`](../sources/manifest.yaml).

Do not modify canonical databases to add inferred foreign keys, normalize text, repair rows, or encode conclusions. Derived schemas and reports belong outside [`sources/`](../sources/).

## 2. Preserve the raw observation

For database work, preserve:

- database file and table;
- row primary key where meaningful;
- raw column values;
- schema and declared constraints.

For protocol work, preserve:

- exact frame text;
- direction;
- timestamp and connection;
- active diagnostic, programming, or functional session;
- immediately preceding request;
- following terminal, error, or timeout event.

For UI and product evidence, record the exact label, visibility, editability, selected Device/firmware context, and document revision.

## 3. Enumerate namespaces

Before joining or decoding a value, list every plausible namespace. For example, a value described as an Object could mean:

- `EN_KEY_OBJECT.id_key_object`;
- `EN_KEY_OBJECT.key_object`;
- `EN_VIRGIN_OBJECT.id_virgin_key_object`;
- `EN_VIRGIN_OBJECT.virgin_key_object`;
- ScenarioDevices `ObjectId`;
- a Device-local internal slot;
- an OpenWebNet `WHERE` or `WHAT` value.

Reject candidates that conflict with field range, context, cardinality, or observed behavior.

## 4. Test structural compatibility

For a proposed database relationship, test:

1. type and domain compatibility;
2. complete or explainable parent-key coverage;
3. cardinality;
4. duplicate values and sentinel rows;
5. whether association-table structure supports the proposal;
6. whether the relationship remains valid after selecting the correct firmware, Module, Object, or system context.

An unexplained orphan or a many-to-many expansion can disprove a supposed foreign key even when most values match.

## 5. Seek independent corroboration

Strong conclusions normally combine at least two evidence classes:

| Primary observation | Useful corroboration |
| --- | --- |
| column-name and key coverage | application query or declared foreign key |
| frame field and matching catalogue value | UI label or Device behavior |
| resource-key semantics | literal functional frame |
| product diagram | reported diagnostic value |
| scenario capability | public functional specification |

Two tables repeating the same undocumented assumption are not necessarily independent evidence.

## 6. Search for counterexamples

Test the proposal against:

- every populated value, not only the first match;
- rows with `NULL`, `0`, or negative sentinels;
- Objects belonging to several systems;
- several firmware revisions;
- Devices with different Module layouts;
- captures from another managed family where possible.

A relationship can remain useful with exceptions, but the exceptions must become explicit conditions.

## 7. Prefer discriminating tests

A useful test makes competing hypotheses predict different observations. Repeating a Lighting/Automation capture cannot distinguish several candidates for `DIMENSION 32.SYS` because they all commonly equal `1`. A Thermoregulation capture can distinguish `sys_modobj = 3`, database `id_system = 2`, and functional `WHO = 4` immediately.

See [Hypothesis Testing](hypothesis-testing.md) for current discriminating cases.

## 8. Promote or retain

Promote a conclusion into reference documentation when:

- its scope and namespace are clear;
- known values are covered or exceptions are explained;
- no stronger counterexample remains;
- the reader can apply it without relying on the original investigator’s intuition.

Retain unresolved alternatives in this section. Do not present an inference as a protocol guarantee merely because it is the most likely explanation.
