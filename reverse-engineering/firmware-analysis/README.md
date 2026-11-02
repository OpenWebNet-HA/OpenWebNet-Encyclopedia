# Firmware Implementation Reference

Manufacturer Firmware provides build-specific evidence about how OpenWebNet commands, diagnostic data, catalogue records and scenes are processed. These references explain that implementation behavior alongside the public protocol and Device descriptions. Applicability belongs to the named product and build; shared filenames or database bytes do not establish shared features.

## Find a subject

| Question | Reference |
| --- | --- |
| Which catalogue profile and identifier context should an importer use? | [Catalogue source profiles](../../internals/mhcatalogue-source-profiles.md) |
| How do editor rules become MH202 scripts? | [ScenarioSuite generator](../../scenario-engine/scenario-suite-generator.md) and [generated-script consumers](mh202-1.0.24-generated-scenarios.md) |
| How are server scenes loaded, evaluated and completed? | [Server scene processing](../../scenario-engine/server-scene-processing.md) |
| How does MH202 separate scene control, restoration and interpreter state? | [Scenario lifecycle and routing](mh202-1.0.24-state-and-routing.md) and [record/script storage](mh202-1.0.24-record-and-script-lifecycle.md) |
| Why can a formatted message or local receipt differ from delivered behavior? | [MH202 translation](mh202-1.0.24-functional-translation.md) and [F454 energy paths](../../functional/who-18-energy-management/dimensions.md#f454-2051-direct-dh-path) |
| Which database artifacts describe capabilities, templates or runtime stores? | [Data-store responsibilities](../../internals/data-store-responsibilities.md) and [legacy database evidence](remaining-firmware-database-handoff.md) |

## Product and build references

| Product / Firmware | Implementation subjects | Reference |
| --- | --- | --- |
| F454 `2.0.51` | Gateway identity, temperature conversion, energy history, video and alarm software boundaries | [F454 implementation](f454-2.0.51.md) |
| MH202 `1.0.24` | Scene control, embedded scripts, local routing, functional translation and diagnostic construction | [MH202 implementation](mh202-1.0.24.md) |
| MyHOMEServer1 `3.87.13` | Catalogue selection, JSON-facing scenes, compiled runners, actions and lifecycle | [MyHOMEServer1 implementation](myhomeserver1-3.87.13.md) and [implementation overview](myhomeserver1-3.87.13-research-synthesis.md) |
| F460 `2.0.12` | Catalogue query ownership, scene predicates, action requests and configuration dependencies | [F460 implementation](f460-f461-knowledge-handoff.md) |
| F461 `2.0.11` | Integration configuration, module admission/lifetime and structured-message translation | [F461 implementation](f460-f461-knowledge-handoff.md) |
| F450 `2.0.10`, standard and PROD | Configuration inputs and declared database copy/open paths | [Legacy implementation profiles](f450-f453av-f455-f459-mh200n.md) |
| F459 archive `020105` / local `2.1.5` | Shared-store construction, read/write requests and watcher ownership | [Legacy database roles](remaining-firmware-database-handoff.md) |
| F453AV `3.0.14`; MH200N `1.1.8` | Own application resources and separate normal/recovery contexts | [Legacy implementation profiles](f450-f453av-f455-f459-mh200n.md) |
| F455 `1.1.2` | Retained opaque package format; processor and executable layout unresolved | [Package applicability and limits](f450-f453av-f455-f459-mh200n.md) |

Normal, recovery and separate application bundles are source views, not an assumed installed overlay. The retained package identity must be resolved before applying a finding to another build.

## Evidence and applicability

Static source establishes the inspected arguments, branches and data relationships. Isolated original-helper execution adds results for its recorded inputs and dependency models. Neither establishes complete service behavior or a Physical Device outcome. Material assumptions and unresolved state belong beside the affected claim.

Public frame grammar remains in [Protocol](../../protocol/), functional semantics in the [Functional reference](../../functional/), and product capability/topology in [Device definitions](../../devices/). These implementation references supplement those canonical treatments rather than defining competing public vocabularies.

Original fingerprints, code locators, experiments, correction histories and reviews are retained in the [supporting evidence records](../../project/review/firmware-analysis/). Manufacturer originals retain their registered private-archive policy. A source report, a reproduced helper case and a captured physical exchange have different evidential roles; see [Evidence and Confidence](../evidence-and-confidence.md).
