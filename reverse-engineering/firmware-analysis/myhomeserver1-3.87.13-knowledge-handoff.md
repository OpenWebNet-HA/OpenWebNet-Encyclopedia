# MyHOMEServer1 3.87.13 Tooling Boundaries

Catalogue importers and scenario-analysis tools can use selected implementation findings from MyHOMEServer1 Firmware `3.87.13`, provided they preserve source ownership, representation and state boundaries. The [implementation overview](myhomeserver1-3.87.13-research-synthesis.md) explains the engine; this page describes consequences for using that knowledge.

## Catalogue importers

Treat the embedded `MHCatalogue.db` and MyHOME Suite's catalogue as separate source profiles. Equal table definitions, filenames or version labels do not establish interchangeable rows or stable IDs. An importer should retain artifact identity, owner context, NULL/type distinctions and duplicate multiplicity.

The [catalogue comparison](../../internals/mhcatalogue-source-profiles.md) distinguishes reused Configuration IDs from equivalent fields moved to another ID and genuine metadata changes. Those mappings are scoped to the compared sources, not a general migration algorithm. An omitted row does not establish incompatibility, and the embedded profile is not a complete self-capability description.

`matrix_mx` has a concrete compiled catalogue consumer: the selected class receives a `15`-column query, with columns `13/14` supplying slots/system ID. [Consumers](myhomeserver1-3.87.13-consumers.md) and [query ownership](myhomeserver1-3.87.13-factories.md) describe the relationship. Full selection/fallback and Prototype/RC handling remain unresolved; stored catalogue status is not a release or tested-compatibility guarantee.

## Scene and state tools

| Distinction to preserve | Consequence for a tool |
| --- | --- |
| Raw schema object / compiled runner | Follow serializer/reparse and setters before assigning operational meaning to a field |
| Trigger / condition / action | Keep their type tables, operator rules and storage separate |
| BNLD trigger / BNLD condition | Use their independently derived handlers and callers rather than a shared-name dispatch |
| Integer level / double setpoint | Type a field from its actual producer/record, not its numeric offset |
| Outer request `id` / `params.id` | Preserve request-correlation and configured-target identities separately |
| Scene state / action completion / shared cancellation | A cleaned scene does not prove completed workers or a reset cancellation domain |
| Stored owner / raw capture / detached holder | A disposal request or cleared holder is not proof of finished work or live receivers |

Selected schemas, callbacks and predicates support offline inspection, but do not form a complete accepted-input grammar. No genuine populated scene or configured export was available. A future generator or validator must not turn local member accesses, metadata names or one construction path into universal required fields, supported commands or safe numeric domains.

The [numeric trigger](myhomeserver1-3.87.13-event-trigger.md#bnld-numeric-trigger) has signed comparison source and a caller with ID/status/value guards. Crossing detection, deduplication, physical units and natural delivery remain unresolved. Likewise, BNCUSCENE's enabled-only predicate is a local result rather than a product-wide capability or defect declaration.

The [action interface](myhomeserver1-3.87.13-action-output.md), [request fields](myhomeserver1-3.87.13-action-request-values.md) and [retained state](myhomeserver1-3.87.13-action-retained-state.md) support selected `2.0` / `light.setStatus` construction relationships. They are insufficient to claim a complete payload, supported speed domain, fresh same-ID state, natural paired invocation, delivery or physical restoration.

## Product applicability

[MyHOMEServer1](../../devices/definitions/own-dev-0199-myhomeserver1-home-automation-server.md) has its own SCS/Ethernet home-control and app-commissioning role. F454's AV/alarm hardware and MH202's script scheduler have separate product and implementation evidence. Shared class labels or catalogue Objects do not transfer those roles, Firmware layouts or protocol support.

## Evidence classes

| Evidence level | Supported use |
| --- | --- |
| Archived data and declared metadata | Identify sources and compare stored records/relationships within their revisions |
| Static implementation | Follow selected constructions, guards, callbacks and ownership requests under object/provider/configuration premises |
| Isolated scalar helper | Use four original JsonCpp constructor/readback cases as narrow corroboration of that provider path |
| Configured runtime and Physical Device behavior | No complete MyHOMEServer1 scene or physical installation was exercised by these findings |

The [evidence collection](../../project/review/firmware-analysis/myhomeserver1-3.87.13-final-review/README.md) retains source reports and exact method/experiment history. The [scalar reference](myhomeserver1-3.87.13-serialization.md#isolated-original-scalar-constructor-and-readback) defines the four supplied values and its limits; it does not validate complete JSON operations or the scheduler.

## Unresolved implementation requirements

| Evidence needed | Question it would address |
| --- | --- |
| Genuine scene/generator asset | Exact configured member/value relationships and a natural loader-to-runtime path |
| Effective provider/type/ID/freshness evidence | Whether selected request and cached-record contracts compose in an installation |
| Positive shared-reset owner | How the common action cancellation domain is reinitialized |
| Natural owner/poll/removal sequence | Receiver survival and worker completion beyond local retain/release requests |
| Controlled runtime/physical observation | Scheduling, delivery and actual Device effects |

Missing extras `80/81/94/95` cannot be supplied by defaults or similarly named files. These are evidence requirements; the source descriptions alone do not establish actual provider, runtime or physical outcomes.
