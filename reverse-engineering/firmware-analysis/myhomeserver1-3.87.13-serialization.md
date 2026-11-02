# MyHOMEServer1 3.87.13 Serialization and Action Ownership

The scheduler transforms raw JSON-facing objects into compiled objects and stores them through several ownership mechanisms. In [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md), sparse serialization, provider conversion, control-pair transfer and deleting condition pointers are separate contracts. None alone establishes a complete JSON round trip or safe concurrent receiver lifetime.

## The raw serializer emits a sparse representation

The selected `Bn3lAction` virtual serializer receives the raw object and JSON destination separately.

| Field | Selected emission rule |
| --- | --- |
| `id` | Omit an empty string |
| `type` | Always assign; local action index `12` maps to `BN3L` |
| `delay`, `duration` | Omit unsigned zero |
| `status` | Always assign; local `-1/0/1` map to `noStatus/on/off` |
| `brightness`, `saturation`, `hue`, `temperature`, `speed` | Omit only the `-1` bit pattern; emit zero and other selected signed values |

The serializer does not preserve original member presence. Status `-1` is explicit `noStatus`, while optional numeric `-1` and zero timing fields are omitted. These are local schema rules, not physical states or accepted numeric domains.

The initializer passes that same JSON result into the raw constructor and compiled constructor. A nonzero duration has a source route through reparse to operational storage, conditional on valid objects and successful member/assignment/conversion semantics. [Serializer evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-serialization/serializer-report.txt) records the original value paths; no universal lossless round trip is established.

## Packaged JSON value conversions

The scheduler declares `libjsoncpp.so.25`; the packaged candidate resolves to `libjsoncpp.so.1.9.5`. Its exact identity and selected code are retained in the [provider evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-serialization/provider-values-report.txt). Effective loader binding remains unobserved.

On the examined valid-tree-end path, const member lookup returns a null singleton. Its type-`0` `asUInt` branch returns zero without reading the value union, providing a conditional source basis for reconstructing omitted zero delay/duration. The unsigned constructor supplies type `2`, stores the low `32`-bit argument and clears the high word; its selected predicate/getter accepts and returns that representation.

Object/key insertion, assignment, tree/string/error behavior and the complete serializer/reparse sequence are separate premises. A host JSON library is not substituted for this packaged provider.

## The compiled vector retains a concrete action/control pair

The selected `SLEEP` initialization creates a pointer/control pair with initial control counts `1/1`. Temporary copying and release adjust the strong count before append. Normal-capacity append moves the exact pair into compiled-action storage and clears its source. The selected full-capacity path also transfers the incoming pair, relocates existing pairs and replaces the raw storage/header.

These paths establish a stored owner, complementing a wait-thread state's raw receiver capture. They do not establish natural last ownership, allocation/unwind success or concurrent receiver survival. [Vector evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-serialization/vector-ownership-report-v2.txt) preserves the exact transfers.

## Scene removal and shared-reset distinction

A local caller supplies a context and numeric key to scene-registry removal. On a matching node, the selected path clears its stored scene/control pair **before** releasing the saved control, then requests keyed erasure. Prior strong count `1` requests disposal. For a loader-produced scene control, the selected disposal method reaches scene teardown, whose holder handling precedes action-handle release.

This is a concrete caller-to-release order, not proof that removal naturally follows polling, that the context is startup's registry, that it is the last owner, or that workers have completed. Whole-tree erasure delegates clearing; the non-whole-range route requests erase rebalancing, node deletion and count decrement. It removes a registry node, not an action vector through coincident offsets. [Owner-removal evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-owner-removal/README.md) retains those branches.

A separately examined constructor call writes zero to offset `72` of current stack storage holding an inline string. That assignment is not the shared action-stop flag or a different registry's mutex at the same numeric offset. No positive shared reset owner follows from that call; other aliases remain unresolved.

## Local removal argument provenance

The selected removal receiver comes from word `0` of a preserved dispatcher argument. Its original producer and equality with startup's scene container remain unresolved. The numeric key comes from parsed `params.scene_id`, separate from event-cache `params.id`.

String/range requests feed a decimal helper whose returned result becomes the removal key. The helper requests base-10 `strtol` and checks `end == start` and errno `34`. This does not establish the full accepted sign/partial-text/domain grammar, successful JSON conversion or natural invocation. [Removal context evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-removal-context/README.md) supplies the local argument chain.

## Concrete condition-pointer teardown

The scene's condition range contains four-byte compiled-object pointers, unlike trigger/action eight-byte pointer/control records. Cleanup advances by four, skips nulls and calls each nonnull condition's deleting slot, distinct from its predicate slot.

For constructed `BNCUSCENE`, the deleting destructor requests release of four member-string buffers, condition-variable destruction and sized deletion of its `192`-byte object. A condition's own inline string at offset `116` is not the scene's condition vector at offset `116`. After normal element callbacks, scene cleanup separately requests vector-storage deletion using its capacity and begin pointers. Selected action cleanup precedes this loop; trigger cleanup follows.

This establishes a disposal request path, not unique ownership, successful deletion, joins, worker completion or safe concurrency. [Condition-ownership evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-condition-ownership/README.md) retains the concrete slots and import identities.

## Candidate double-value provider contract

For the exact packaged candidate, `Value(double)` initializes type `3`, initializes its comments pointer and stores the supplied double in the value union. The selected empty-comments move path bypasses nonnull comments disposal. `type()` reads the stored type byte; the selected type-`3` `asDouble` path loads directly from that same union.

This source relation supports one scalar used by the [BNTH condition](myhomeserver1-3.87.13-event-routing.md#a-selected-nonconstant-bnth-comparison). Member construction/insertion, move assignment, lookup, parsing/reparse, actual binding and nonempty/error paths remain separate. [Double-provider evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-bnth-values/provider-report.txt) identifies the original provider and ABI.

## Isolated original scalar constructor and readback

One isolated experiment executes the packaged constructor and selected type-`3` readback for four supplied finite bit patterns: positive zero, negative zero, negative one and `1.25`. Each readback consumes the same constructor-produced `24`-byte object without reseeding its fields; a distinct register value ensures the getter must load stored data. Returned bits match, including signed zero.

This is original-helper evidence under a supplied binding, canary, storage and CPU/FP setup. It supports only those scalar cases, not a complete configured condition, JSON member/map/assignment/serialization/reparse, nonempty comments, destructors/error paths or the scheduler. The [experiment and saved execution accounting](../../project/review/firmware-analysis/myhomeserver1-3.87.13-double-isolation/README.md) retain its harness, inputs, original-byte identities and reviews.

## Evidence limits

Static ownership and provider paths must remain distinct from the isolated scalar observation. Configured scene files, effective bindings, natural owner/removal order, shared cancellation reset, complete exceptions/unwind, concurrency and physical effects remain unresolved. References to extras `80/81/94/95` do not supply their missing configured content. [Worker lifetime](myhomeserver1-3.87.13-lifetime.md), [cancellation](myhomeserver1-3.87.13-cancellation.md) and [event conditions](myhomeserver1-3.87.13-event-routing.md) describe the related concepts.
