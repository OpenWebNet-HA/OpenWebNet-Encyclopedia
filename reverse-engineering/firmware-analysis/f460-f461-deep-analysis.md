# F460 and F461 application behavior

F460 `2.0.12` and F461 `2.0.11` implement different application paths on a related AArch64 platform. F460 findings concern catalogue selection and compiled scenarios; F461 findings concern integration-module selection, routing and translation. The [package reference](f460-2.0.12-and-f461-2.0.11.md) identifies the originals, and the [implementation overview](f460-f461-knowledge-handoff.md) relates these contracts to tooling.

The evidence is source inspection, not an executed configured installation. A local request establishes its arguments and control flow under the stated object/provider premises; it does not establish successful operating-system work, delivery or physical effects. Exact code, layouts and independent reviews are linked with each subject.

## F460 catalogue and scene processing

### F460: catalogue opening, SQL producer and selected reader
`matrix_mx` connects a catalogue path, opening request and 15-column SQL producer to a selected reader. Constructor-supplied substitutions reach the SQL member consumed by that reader. Columns 13/14 are `EN_KEY_OBJECT.slots` and `AS_OBJECT_SYSTEM.id_system`; the reader obtains text and requests decimal conversion into its destinations.

This establishes a concrete consumer, not executed SQL or complete Device/Firmware selection, fallback or Prototype/RC policy. Valid rows, filesystem/string/SQLite providers and conversion results remain prerequisites. [Reader evidence](../../project/review/firmware-analysis/f460-f461-run04-2026-11-01/README.md) and [catalogue source profiles](../../internals/mhcatalogue-source-profiles.md#f460-catalogue-consumer) distinguish the F460 reader from shared database bytes; no F461 consumer follows from equality alone.

### F460: indirect selector and supplied parameter ownership
A stored constructor callback is copied into a global registry and selected through an adapter. For local key `89`, three getters read 32-bit values from the same supplied owner; the adapter forwards their dereferenced arguments as SQL `$modobj$`, `$line_modobj$` and `$brand_modobj$` substitutions. The constructor separately supplies `$key_object$=89`.

These are SQL-placeholder roles, not observed configuration values or Device/WHO identifiers. The returned inner/control pair is retained on an available-capacity owner-vector path. Registry initialization, cache-miss selection, valid callables/containers/providers and normal returns are prerequisites. Owner construction/type, actual values, key-list provenance and full selection/lifetime remain unresolved. [Selector evidence](../../project/review/firmware-analysis/f460-f461-run05-2026-11-01/README.md) identifies the indirect call and ownership premises.

### F460: state-trigger construction and local admission
The private `BNIL` raw trigger and compiled trigger use separate factories and layouts. The initializer obtains a virtual JSON result, reparses that same result and copies enabled/operator/status values. Complete serializer/value coherence and provider outcomes remain conditional.

The compiled handler requires enabled and maps exact `on`, `off` and `noStatus` strings to local integers `0`, `1` and `-1`. Operator word `2` selects equality and `3` selects inequality; other numeric words can reach a callback after recognized state. This local control flow is not an external operator grammar or physical on/off mapping.

An actual caller supplies a record string under ID and method-identity guards. Cast-result validity remains a premise: no post-cast nonnull guard is proved. The callback captures the initializer receiver as a raw pointer, without owning-lifetime or natural event-subscription proof. [Trigger evidence](../../project/review/firmware-analysis/f460-f461-run06-2026-11-01/README.md) preserves the own-build factories and caller.

### F460: captured receiver to conditional condition-worker request
One construction path identifies an in-place `SceneRunner` and passes its inner destination through the constructor to the trigger initializer. The control-block table is distinct from the inner primary vtable. This supplies one receiver context, not proof that every capture has it or remains alive.

The local handoff tests receiver byte 113 and acquire-loads byte 249. Its nonzero/zero path changes flags and requests a thread state containing the same raw receiver, thread start and normal-path detach. The numeric fields have no established public enabled/stop/active meanings. The worker loads the same receiver's condition range, whose entries are 8-byte pointers rather than 16-byte trigger inner/control pairs. A selected final condition's predicate low byte controls a subsequent local request. Successful thread creation, exclusion, complete condition policy and lifetime remain unresolved. [Receiver/worker evidence](../../project/review/firmware-analysis/f460-f461-run07-2026-11-01/README.md) retains the construction and callback link.

### F460: one concrete condition pointer and its complete predicate
Local condition `BNCUSCENE` is constructed and published as the same pointer in the condition vector. Its common parser reads `enabled`; compiled construction copies that byte. The entire installed predicate loads the byte, XORs with one and returns. For ordinary Boolean `0/1` construction, successful copy and no mutation, that is inversion; arbitrary bytes are only unsigned XOR-one, not universal logical negation.

The predicate body performs no target-scene lookup. Its class name does not prove a scene-status feature or a missing/unsupported function. Same-object publication, valid range and worker lifetime are required to compose it with the predicate caller. Serializer value coherence and actual configured inclusion remain unresolved. [Condition evidence](../../project/review/firmware-analysis/f460-f461-run09-2026-11-01/README.md) preserves the complete local body and own factory context.

### F460: a concrete numeric condition and its operand order
The `BNLD` condition has its own raw factory, JSON reparse and compiled allocation. Enabled, operator, status selector and threshold are its own fields rather than another Firmware's same-named layout. The predicate requires enabled, a suitable nonnull query record, exact record status `on` and configured selector `-1`.

| Local operator word | Comparison |
| --- | --- |
| `0` | Configured threshold less than observed record integer, signed |
| `1` | Configured threshold greater than observed record integer, signed |
| `2` | Equality |
| `3` | Inequality |

Query type, readiness, freshness and valid cleanup remain prerequisites. The raw operator spelling is a separate serialization relation; these comparisons do not identify physical units, public grammar or configured values. [Numeric-condition evidence](../../project/review/firmware-analysis/f460-f461-run14-2026-11-01/README.md) pins the own-build predicate and consumer.

### F460: selected numeric serializer and operator spellings
The selected common serializer and parser have these local associations:

| Operator word | Serialized spelling |
| --- | --- |
| `0` | `higher` |
| `1` | `lower` |
| `2` | `equal` |
| `3` | `different` |
| `-1` | Operator emission skipped |

These spellings must be read with the predicate's actual operand order above; an English label alone is not its comparison definition. On raw status `-1`, the serializer assigns the signed raw level as `level` in the same result and requests no status assignment. There is no direct zero/level-sentinel omission test on that branch.

For a fresh unchanged JSON result, ordinary member/string/move/int/asInt providers and no extra status member, reparse carries this level into the compiled threshold while retaining status `-1` and the chosen operator. This is selected value coherence, not a universal lossless JSON roundtrip or accepted external schema. [Serializer evidence](../../project/review/firmware-analysis/f460-f461-run15-2026-11-01/README.md) preserves the original ABI and exact branch.

### F460: SLEEP request units and completion are separate contracts
The `SLEEP` callable captures a 32-bit value. Zero skips the wait request; nonzero forms two 64-bit words, zero-extended value followed by zero, and supplies the same storage as request and remaining duration to `nanosleep`. Under the ordinary Linux LP64 `timespec` contract this means seconds and zero nanoseconds. Only return `-1` with error number `4` retries, corresponding to interruption under ordinary Linux/POSIX semantics. Other wait errors can leave through normal callback return.

The common action caller clears completion, invokes the callable on its selected zero-delay/stored-manager path, then tests a separate operational word before setting completion. Completion can therefore follow a normally returning callback that left on a non-retry wait error. It does not certify elapsed duration. Actual configured values, effective binding, operating-system behavior and lifetime remain unresolved. [Wait and completion evidence](../../project/review/firmware-analysis/f460-f461-run03-2026-11-01/README.md) records the source and ABI premises.

### F460: action dispatch, marker polling and scene-byte cleanup
Selected actions enter the scene range as 16-byte pointer/control pairs, distinct from 8-byte condition pointers. The executor requests an action's primary slot 0 and then checks scene byte 248 before continuing; it can leave before dispatching every entry.

In the selected polling path, action byte 8 can lead to cleanup when nonzero. With that marker zero, the wait/recheck route can still reach cleanup after scene byte 248 becomes nonzero, without a fresh true-marker read. Normal cleanup later clears scene bytes 249/248. Cleanup therefore does not certify that every action completed, just as the SLEEP marker does not certify elapsed waiting. Full control policy, action effects, owning lifetime and concurrency remain unresolved. [Dispatch/poll evidence](../../project/review/firmware-analysis/f460-f461-run10-2026-11-01/README.md) retains the separate state fields and ordering.

### F460: a local control writer with an unresolved caller
A local method writes `1` to supplied receiver byte 248, then traverses its 16-byte-entry range and requests primary slot 8 through each first pointer. Only if that receiver is the same valid scene object does it supply the earlier executor's nonzero scene field. Its caller and receiver class remain unproved; equal offsets are insufficient to join them.

No public cancellation meaning, successful stop, general restart, ownership or concurrency guarantee follows. The selected virtual target remains opaque. [Writer evidence](../../project/review/firmware-analysis/f460-f461-run11-2026-11-01/README.md) preserves the positive local store and unresolved join.

## F461 integration modules and structured messages

### F461: main selects configuration pointers before module-registration requests
On the selected successful option-parse path, absent configuration filename receives relative default `cfg/coso_cfg`. Key-file directory reads occur only while their corresponding option slots are null; nonnull option pointers therefore take local precedence. A still-missing plugin-configuration directory is derived from the selected configuration filename's parent.

The chosen library/configuration directories reach the same manager initializer, which copies them into a separate holder before monitor and registration requests. The manager's holder pointer and that holder's copied-directory fields are different objects. These are argument-selection rules, not proof of usable paths, runtime values, active modules or readiness. [Configuration evidence](../../project/review/firmware-analysis/f460-f461-run11-2026-11-01/README.md) retains the option/key/fallback guards.

### F461: module admission and handle recording before initialization
The selected loader enumerates the supplied library directory, selects names with prefix `lib` and suffix `.so`, constructs a path and requests a module handle. Both `init_plugin` and `stop_plugin` lookup results must be nonzero. Failed symbol checks request closure and continue under normal provider returns; that check does not invoke the stop function.

A selected successful path appends a path/handle entry before requesting initialization with the separate configuration directory. The inspected continuation does not test the initializer's returned machine value before its next helper/enumeration; this is not a known full return ABI or a global validation-absence claim. Local traversal return 0 can include skipped or failed entries, so it does not prove any plugin initialized. [Module-admission evidence](../../project/review/firmware-analysis/f460-f461-run14-2026-11-01/README.md) retains support/directory gates and local return paths. Provider ABI, activation, ownership and readiness remain unresolved.

### F461: monitor registration to a retained module-entry consumer
The selected main path registers the actual directory-monitor `changed` callback with the same manager as userdata. Its callback obtains the retained entry list and file path; numeric event 0 plus a nonzero delegated suffix match against the stored path selects an entry. A suffix relation is not canonical file identity or a complete event policy.

Successful stop-symbol lookup leads to a callable request. Under normal returns, list removal/head storage precede path-free, handle-close and entry-free requests; failed lookup can skip the callable and still reach bookkeeping. This establishes request ordering, not successful stopping, completed unloading, safe ownership or concurrent shutdown. [Module-removal evidence](../../project/review/firmware-analysis/f460-f461-run15-2026-11-01/README.md) retains callback/entry identity and the precise load/store/free ordering.

### F461: field registration and complete route identity
The SCS plugin conditionally registers a field descriptor into the manager's field list, distinct from its translation list. A configuration-directory argument reaches its initializer. Packaged `SCSEnable=1`/`SCSAIEnable=0` differs from local fallback globals initially equal to one for both, so the selected registration depends on load success and effective settings.

A generic message constructor sets a 64-bit route with low/high 32 words `(1,0)`. The command wrapper produces `(1,1)`; another produces `(1,2)`. The matcher uses the complete route for field matching and separately its low word for direction. Matching only the low word would merge distinct routes. Same-manager, valid-object, due/criterion and provider premises remain necessary; names/settings do not establish public grammar, installed activity or F454-style alarm hardware. [Field/route evidence](../../project/review/firmware-analysis/f460-f461-run04-2026-11-01/README.md) retains these distinct contexts.

### F461: registered descriptor to actual translator call
The selected `coso` caller obtains a manager and traverses its field-descriptor and translation-descriptor lists. It matches a field against the message, checks descriptor direction words, selects a criterion list and compares a criterion with the message's numeric field before invoking the translator slot.

For the selected automation case, the second criterion list leads to arguments `(2,1)`, with the same message, output-list address and descriptor. Composition requires the same initialized manager and valid unchanged list objects. Criterion conversion from a supplied parsed decimal string does not identify a public WHO. The returned value controls iteration/cleanup; further descriptors may be processed, so global first-match exclusivity is not established. [Matcher evidence](../../project/review/firmware-analysis/f460-f461-run03-2026-11-01/README.md) retains the exact guards. A local zero return is not delivery acknowledgement.

### F461: one typed-object payload and output-record contract
One selected converter branch derives conditional ASCII normal form `B1001208` from original literals and formatter order under its direction, representation, parsed-kind, scalar/string, null-field and private-selector premises. This is not an accepted raw OPEN command or observed bus payload.

A requested 72-byte output record receives that string, selected metadata, two copied 16-byte source regions, a status word and the existing 64-bit ID, then enters the caller's list. Unwritten fields are not proved initialized. Copying an ID does not establish uniqueness or a new-ID producer. Temporary-string cleanup on normal return does not prove output delivery or complete ownership. [Payload and record evidence](../../project/review/firmware-analysis/f460-f461-run05-2026-11-01/README.md) retains the exact branch constraints.

### F461: address shape and selected prefix normalization
A packaged automation helper excludes exact `0`, strings beginning with `#`, exact `00` and exact `100`, then uses UTF-8 character count; remaining lengths two or four select local class `4`. The plugin passes the same parsed-object field to that helper. On its selected length-two route, it starts a `D1` string, reads bytes 0/1, delegates digit conversions and appends the two integer results in order.

UTF-8 character count, byte position and ASCII digit validity are different properties. This path is not a complete decimal-address validator or public topology. The local class is also separate from plugin-private selectors, parsed kinds and WHO. [Address classification evidence](../../project/review/firmware-analysis/f460-f461-run06-2026-11-01/README.md) retains exact exclusions and valid-object/provider premises.

### F461: typed context to an exact address suffix and local formatter
A selected typed-object path has a string field equal to `4`, a private selector not equal to `4`, decimal conversion of another supplied string and low 32-bit uppercase hexadecimal context formatting. With its explicit zero local flag, the suffix format `%s1%s` uses that context, literal `1` and character `4`. The alternative character `3` requires both context `F` and nonzero flag.

The same address string supplies an argument to a later four-string formatter, whose returned pointer is stored through a local output record. A subsequent frame-preparation import is outside this contract. These conditional components do not establish a public address domain, accepted grammar or physical topology. [Suffix evidence](../../project/review/firmware-analysis/f460-f461-run10-2026-11-01/README.md) retains the exact instruction-flag interpretation, prior field premises and formatter order.

### F461: deferred records to a timer request and same-owner re-entry
The selected dispatcher compares message field 32 against a real-time clock return plus 10, using unsigned 64 arithmetic. A not-due path tracks a minimum; a nonzero candidate causes a fresh clock sample, subtraction interpreted as signed, division by 1000 and a timeout request from the low 32 bits. The first comparison does not guarantee a positive/nonoverflowing later delta.

Candidate GLib source computes real time from `gettimeofday` words under the ordinary successful AArch64 ABI. Timeout source calculation separately uses a monotonic clock. Real-time record coordinates, monotonic ready time and elapsed duration must not be merged.

The registered callback retains the same owner and requests dispatcher re-entry through its list field. Activation, binding, list lifetime and normal providers remain prerequisites. The nonzero field 32 producer is unproved; constructor timestamp field 24 is different. [Clock/defer evidence](../../project/review/firmware-analysis/f460-f461-run12-2026-11-01/README.md) supplies exact arithmetic and callback context, without a timing observation.

### F461: deadline provenance remains open after object-role checks
Neither a plugin-private GList field at offset 32 nor a parsed object's string field at offset 32 establishes the message's numeric defer-time producer. These are different objects and types. A finite direct-store query did not identify that producer; it was not whole-image alias analysis or proof of absence. [Object-role evidence](../../project/review/firmware-analysis/f460-f461-run13-2026-11-01/README.md) retains the candidate exclusions. The message's time coordinate and natural scheduling remain unresolved.

## Supporting component evidence

The following records concern packaged OS/component behavior. They provide source provenance or environment context; none establishes an OpenWebNet-visible update, log-restoration or hardware-identity contract. Their algorithms and low-level file/state details remain in supporting evidence rather than forming independent reference topics here.

| Component context | Retained evidence |
| --- | --- |
| Conditional HAL identity strings | [HAL getter source](../../project/review/firmware-analysis/f460-f461-run07-2026-11-01/README.md) |
| Manifest selection and log-persistence requests | [Updater/logging source](../../project/review/firmware-analysis/f460-f461-run08-2026-11-01/README.md) |
| Cached platform-file selector | [Platform source](../../project/review/firmware-analysis/f460-f461-run09-2026-11-01/README.md) |
| Updater staged-list consumer | [Staging source](../../project/review/firmware-analysis/f460-f461-run12-2026-11-01/README.md) |
| Working-mode/profile value forwarded to a state machine | [Profile source](../../project/review/firmware-analysis/f460-f461-run13-2026-11-01/README.md) |

## Evidence limits
The [evidence catalogue](../../project/review/firmware-analysis/f460-f461-final-2026-11-01/README.md) retains original source identities, selected code, exact report versions and reviews. Source inspection supports the local branches and arguments described here; it supplies no complete Firmware execution or physical observation.

Important open relationships are natural configured objects/callers, F460 control-writer class/caller, actual query type/ID/freshness, F461 defer-time producer/coordinate, effective module/provider binding, complete JSON/XML/SQL behavior and error/unwind/ownership/concurrency. Updater and platform context do not establish OpenWebNet-visible installation or identity behavior. Shared names, bytes and offsets cannot replace those missing relationships.
