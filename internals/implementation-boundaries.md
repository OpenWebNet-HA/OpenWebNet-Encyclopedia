# Implementation Boundaries

This page separates facts directly recoverable from the canonical MyHOME Suite 3.5.38 data from interpretations that need runtime or application-code evidence.

## Evidence levels

| Level | Use |
| --- | --- |
| Established | direct schema, stored value, declared relationship, exact frame, fingerprint, or observed behavior |
| Implementation-derived | stable meaning recovered from complete data patterns, resource keys, or workflow composition |
| Inferred | best explanation of a complete pattern without an explicit declaration |
| Unknown | evidence is absent, conflicting, or supports several explanations |

An inference should state both its supporting pattern and the observation that could disprove it.

## Established boundaries

The preserved corpus establishes that MyHOME Suite distributes several independent SQLite stores; `OPEN.db` models systems and workflows; `OpenQuery.txt` names selected reads but is incomplete; `MHCatalogue.db` models capability and contextual constraints; ScenarioDevices models scenario-editor capability rather than complete scenario graphs; and `rules.db3` adds linked-property rules for selected Temperature Control Objects.

## Safe implementation-derived conclusions

The combined evidence supports these conclusions when their scope is retained:

- `OPEN.db` scenarios and sequences form state-machine definitions for MyHOME Suite management workflows;
- diagnostic/programming `DIMENSION 30.KEYO` uses the regular configured Object namespace for an enabled Module when `STATE = 0` and the Virgin Object namespace for a disabled Module when `STATE = 1`;
- ordinary addressed-form `N_CONF` represents the number of physical configurator positions on corroborated products; the empty-`WHERE` gateway variant is separate, with observed `N_CONF = 15` outside the ordinary `0..12` range and unresolved exact semantics;
- the two ScenarioDevices files are distinct revisions whose common semantic content overlaps despite unstable local IDs;
- literal ScenarioDevices action templates can be rendered only after functional address and Parameter validation;
- catalogue programming validation is context-sensitive and cannot be reduced to `OPEN.db` transport ranges.

These conclusions do not establish universal support across all MyHOME releases or Devices.

## Runtime questions still open

| Question | Evidence needed |
| --- | --- |
| Which ScenarioDevices copy does MyHOME Suite open, and under what conditions? | file-access trace, decompiled loader, or controlled file substitution |
| Are Program Files and ProgramData copies synchronized or migrated? | installation/update trace and before/after fingerprints |
| How are database results cached and invalidated? | process trace or application code |
| Which component resolves ScenarioDevices resource keys? | resource bundles and call-site analysis |
| Where are user-authored project and scenario graphs persisted? | controlled project diff or traced save operation |
| How are frame-absent scenario events mapped to runtime input? | runtime trace and event-dispatch code |
| What enumerations back `WhereType`, `Type`, and `OperatorType`? | application enum definitions or exhaustive UI/runtime correlation |
| How is the installed firmware row selected when several catalogue rows match? | controlled Device/version tests or loader code |
| Are `DIMENSION 4` and `5` values presence flags, raw configurator codes, or another encoding? | captures across known physical configurator layouts |
| How are the separately selected address-rule columns consumed? | traced query execution and consumer behavior |

## Investigation rules

A future implementation investigation should fingerprint the exact release, monitor file opens and SQLite statements without modifying evidence, make one controlled UI change at a time, diff persistence before and after, correlate traffic by timestamp and semantic path, and record negative evidence.

Private captures can support conclusions but should not be committed because they may contain installation identifiers and network details.

## Documentation placement

| Finding | Section |
| --- | --- |
| shared wire grammar | [Protocol](../protocol/) |
| functional `WHO` semantics | [Functional reference](../functional/) |
| Device capability hierarchy | [Device Model](../device-model/) |
| discovery and read-back | [Diagnostics](../diagnostics/) |
| state-changing workflows | [Programming](../programming/) |
| complete end-to-end task | [Practical Guides](../guides/) |
| scenario-editor capability | [Scenario Engine](../scenario-engine/) |
| application data loading and runtime boundary | MyHOME Suite Internals |
| method, competing hypotheses, and unresolved research | future `reverse-engineering/` section |

This separation prevents implementation evidence from being repeated as though it were a public protocol guarantee.
