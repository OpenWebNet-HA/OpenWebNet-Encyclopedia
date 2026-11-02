# F460 and F461 implementation models

F460 and F461 share catalogue content and platform material while serving different integration roles. Their application source explains why catalogue equality, parser acceptance, local completion and physical operation must remain separate when interpreting these builds. The [detailed behavior reference](f460-f461-deep-analysis.md) provides the individual contracts.

## Exact scope and product roles

| Product/build | Role | Relevant implementation |
| --- | --- | --- |
| [F460 `2.0.12`](../../devices/definitions/own-dev-0207-f460-myhome-server.md) | Home + Project/Home + Control | Catalogue consumer and compiled scene processing |
| [F461 `2.0.11`](../../devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md) | Third-party integration | Local configuration/module management and selected translation |

The [package reference](f460-2.0.12-and-f461-2.0.11.md) identifies the exact AArch64 sources. Shared catalogue rows, class names and device-tree bytes do not transfer product capabilities, F454 alarm/AV hardware or MyHOMEServer1 layouts.

## What the evidence changes

| Area | Established implementation distinction | Consequence |
| --- | --- | --- |
| Catalogue | Shared F46 data and a selected F460 reader are separate evidence | Keep generation, owner and query-key context; do not infer an F461 reader or installed support |
| Scenes | Raw objects, compiled runners, conditions and action control pairs have distinct layouts/consumers | Use actual object/caller relationships rather than names or repeated offsets |
| Completion | Callback return, marker, cleanup and actual delay are different events | A local completion flag cannot certify every action or elapsed time |
| Plugins | Directory selection, admission, retained handle and removal request have separate stages | Loader traversal is not module activation or safe unload |
| Translation | Route, direction, criterion, record kind and formatted text are different namespaces | Structured-object formatting is not accepted public grammar or delivery |

### F460: catalogue parameters belong to a supplied owner

The selected F460 reader has an actual SQL producer and an indirect registry/adapter path. Key 89 selects its constructor; values from the same supplied owner feed `modobj`, `line_modobj` and `brand_modobj`. That local query/class key is not a Device ID or WHO. Slots/system-ID columns are reader outputs, not automatically active capabilities.

The reader permits repeated rows to overwrite destination fields, and its inspected path does not prove a first-row or null-text guard. Root owner construction, supplied values, complete selection/fallback and functioning providers remain unresolved. [Catalogue profiles](../../internals/mhcatalogue-source-profiles.md#f460-catalogue-consumer) place this evidence beside the distinct MHS/Suite ownership comparison.

### F460: a scene request is several separate contracts

One construction path identifies a SceneRunner receiver later captured as a raw pointer. Thread-start/detach requests do not prove owning capture or safe lifetime. Condition pointers and action pointer/control pairs have different representations.

`BNIL` state-trigger admission, `BNCUSCENE` enabled-byte inversion and `BNLD` signed threshold comparison are different local contracts. Numeric serializer spellings and actual operand order must be used together. They do not form a complete JSON schema or public operator/physical-unit map.

A SLEEP marker can follow a normal callback return after a non-retry wait error. Scene polling can reach cleanup after a different control flag becomes nonzero, without a fresh true action marker. Neither event proves elapsed waiting or completion of every action. A separate positive control writer remains unjoined to a natural caller and receiver class. See [scene predicates and execution](f460-f461-deep-analysis.md#f460-state-trigger-construction-and-local-admission) and the [configured-input boundary](myhomeserver1-f460-f461-input-admission.md).

### F461: configuration and module requests are connected locally

Nonnull option-produced directories take local precedence over selected key reads; a missing plugin directory can fall back to the configuration file's parent. The loader checks names and both required symbols, stores the path/handle entry before requesting initialization, and can finish traversal after skipped/failed entries. These rules explain local inputs and ordering, not actual command-line values, active modules or successful initialization.

A directory-monitor callback retains the same manager. One event/suffix path can request stop, remove bookkeeping and request handle closure/freeing. Actual callback delivery, provider ABI, stop outcome, unload and safe concurrent lifetime remain unresolved. See [configuration selection](f460-f461-deep-analysis.md#f461-main-selects-configuration-pointers-before-module-registration-requests) and [module lifetime requests](f460-f461-deep-analysis.md#f461-monitor-registration-to-a-retained-module-entry-consumer).

### F461: translation and time retain their own namespaces

The matcher uses a complete 64-bit field route and separate direction/criterion tests. Selected typed-object branches derive payload/address strings and copy an existing ID into an output record. This does not establish public WHO meaning, raw admission, a new unique ID, output acknowledgement or physical topology.

Deferred dispatch uses separate real-time input and monotonic timer contracts. The message defer-time producer/coordinate remains unproved; constructor and unrelated private fields at similar offsets cannot substitute for it. [Routing/translation](f460-f461-deep-analysis.md#f461-field-registration-and-complete-route-identity) and [deferred records](f460-f461-deep-analysis.md#f461-deferred-records-to-a-timer-request-and-same-owner-re-entry) retain those distinctions.

## Evidence

The [source evidence catalogue](../../project/review/firmware-analysis/f460-f461-final-2026-11-01/README.md) retains exact original identities, code locators, report versions and independent reviews. These F46 findings are static implementation evidence, separate from original-helper experiments on other products. No complete F46 runtime or Physical Device observation supports them.

## Evidence limits

Concrete gaps are genuine configured scenes/module instances, natural callers, query record type/ID/freshness, defer-time production, effective provider binding, complete input grammars, error/unwind and ownership/concurrency. Platform names and component-local values do not establish installed identity, boot selection or readiness. Runtime and physical corroboration must retain their own Device, build and Configuration scope.
