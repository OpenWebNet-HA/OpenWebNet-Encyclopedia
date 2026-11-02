# Implementation Boundaries

MyHOME Suite data, application source and Device observations answer different questions. A declared field or frame template can establish an implementation representation without establishing that a particular Physical Device currently supports or executes it.

## Source authority

The [data-store responsibilities](data-store-responsibilities.md) distinguish catalogue capability, management workflows, scenario-editor vocabulary and project persistence. [Evidence and Confidence](../reverse-engineering/evidence-and-confidence.md) defines claim-level confidence and examination methods; neither a source fingerprint nor a passing mechanical check is a semantic verdict.

| Evidence | Appropriate conclusion | Additional evidence required |
| --- | --- | --- |
| Database schema and stored rows | Declared keys, values, relationships and source-specific alternatives | Effective consumer precedence and application enforcement |
| Static application/Firmware path | Inspected branches, arguments and object relationships | Natural caller state, effective dependencies and runtime outcomes |
| Isolated original helper | Recorded local result for supplied inputs and modeled dependencies | Complete process behavior and Physical Device corroboration |
| Protocol capture | Behavior of the identified Device, version and Configuration | Generalization to other variants or implementations |

## Established cross-source distinctions

- `OPEN.db` scenarios/sequences describe management communication workflows, not complete user scenes.
- `DIMENSION 30.KEYO` selects the regular configured Object namespace for an enabled Module (`STATE = 0`) and the Virgin Object namespace for a disabled Module (`STATE = 1`).
- Addressed-form `N_CONF` is a physical-configurator-position count on corroborated products. The empty-`WHERE` gateway value `15` has separate unresolved semantics.
- Same-name ScenarioDevices and ScenarioSuite files have source-specific content. Local IDs and version labels are insufficient for a cross-file join.
- Stored frame templates require contextual address/Parameter validation. Catalogue value domains cannot be replaced with transport maxima.
- Empty `MHPrj.db` and `PTDB.db` instance tables establish persistence structure, not a configured installation.

These distinctions support interpretation and tooling within the preserved source scope. They do not establish universal MyHOME release or Device support.

## Unresolved consumer behavior

| Question | Remaining evidence need |
| --- | --- |
| Which ScenarioDevices copy is selected, synchronized or migrated? | Effective file-access/loader behavior and update context |
| How are database results cached and invalidated? | Corresponding consumer and runtime state |
| Which component resolves ScenarioDevices resource keys and frame-absent events? | Resource ownership and event-dispatch relationships |
| How are populated MHPrj/PTDB projects loaded and saved? | Actual persistence consumers and a genuine configured project |
| How is a populated ScenarioSuite project compiled and deployed? | A natural caller connecting the [XML loader](../reverse-engineering/firmware-analysis/mh202-project-scenario-loader.md) to the [generator](../scenario-engine/scenario-suite-generator.md), plus emitted files and deployment |
| Which enumerations underlie `WhereType`, `Type` and `OperatorType`? | Application definitions or independently corroborated UI/runtime semantics |
| How is installed Firmware selected among catalogue alternatives? | Root owner/configuration resolution and complete selection/fallback policy |
| What do diagnostic dimensions `4` and `5` encode on each product? | Captures with known physical configurator layouts |
| How are selected management address-rule columns consumed? | Actual query/consumer behavior |

## Canonical placement

| Knowledge | Reference |
| --- | --- |
| Shared wire grammar | [Protocol](../protocol/) |
| Functional WHO semantics | [Functional reference](../functional/) |
| Device/Firmware/Module/Object model | [Device Model](../device-model/) |
| Discovery and read-back | [Diagnostics](../diagnostics/) |
| State-changing workflows | [Programming](../programming/) |
| End-to-end installation tasks | [Practical Guides](../guides/) |
| Editor capability and scenario processing | [Scenario Engine](../scenario-engine/) |
| Application-data roles and source-specific consumers | [MyHOME Suite Internals](README.md) |
| Method, competing interpretations and source-specific implementation | [Reverse Engineering](../reverse-engineering/) |

Detailed comparison tables and examination histories remain supporting evidence. Operational conclusions belong in their canonical reference, with the material uncertainty attached to the affected claim.
