# MyHOMEServer1 3.87.13 Local Event Routing and Conditions

The scheduler maintains typed local records and uses them in selected trigger and condition paths. Record classification, configured IDs, local trigger/condition indices and public OpenWebNet namespaces remain distinct. This reference applies to [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md); physical measurements and external input acceptance are not established by these private class names.

## Selected local route

A selected classifier reads a prefix before the first dot. Its `light` row produces local event code `0`; a separate params-object conversion must supply a nonempty ID. Only the selected processing return `1`, followed by normal cleanup, permits the later second-table lookup of a string-keyed registry record. Raw trigger type `1` uses a different table to reach the [BNIL caller](myhomeserver1-3.87.13-event-trigger.md#local-event-admission), which correlates raw and compiled entries by index, casts the receiver, matches its ID and supplies the record's state string.

Classifier row `1`, event code `0`, trigger type `1` and record discriminator are separate namespaces. Earlier parsing/delegates, active registry state and continued receiver lifetime remain premises. [Routing evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-event-routing/routing-report.txt) identifies the selected joins.

## Concrete record producer

| Selected branch | Constructed record | Relevant value representation |
| --- | --- | --- |
| Missing record or existing discriminator `0` | `ItemStatusLight` | Optional status string at `+8`; optional integer level at `+32` |
| Alternate existing-type route | `ItemStatusLoad`, discriminator `10` | Optional status string at `+20`; not the Light layout |
| Local event code `3` | `ItemStatusThermostat`, discriminator `3` | Setpoint double at `+32`; distinct from Light's integer at `+32` |

The Light record is embedded at control-allocation offset `12`; the Thermostat record at offset `16`. Selected map storage and getters identify the same string-keyed registry used at the trigger/query boundary. A record layout, type, matching ID, valid handle and normal provider behavior must hold before a consumer's field access can be interpreted. [Record evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-event-routing/record-report.txt) supplies the construction/storage proof.

## Distinct BNLD condition

Condition row `2` constructs raw `BnldCondition` (`48` bytes) and compiled `BnldConditionRunner` (`152` bytes), independently of the numeric trigger.

| Field | Raw offset | Compiled offset |
| --- | ---: | ---: |
| Enabled | `28` | `132` |
| Local type / operator | `32` / `36` | `136` / `140` |
| Configured status / level | `40` / `44` | `144` / `148` |

A present `status` member selects string conversion and leaves level `-1`. Only absent status selects level conversion. Explicit `noStatus` therefore differs from absence, and a level supplied alongside a present status is ignored on this constructor path.

The predicate returns `1` when disabled and `0` for its selected null query result. For suitable nonnull records, exact `on`, `off`, `noStatus` become local `0`, `1`, `-1`.

| Configuration branch | Selected predicate behavior |
| --- | --- |
| Status other than `-1` | Operator `2` tests equality; `3` tests difference; other words return `0` |
| Status `-1` | Require exact record `on`, then compare observed integer level with configured level |
| Numeric operators `0/1/2/3` | Configured `<` observed, configured `>` observed, equal, different respectively |

The query is a different helper from event lookup. Record type, freshness/readiness and suitable fields remain premises; no physical brightness unit or complete threshold domain follows. [Condition evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-event-routing/condition-report.txt) retains the operand directions and actual consumer.

## Serialization and query-cache behavior

The condition's own decoder maps `noOperator/higher/lower/equal/different` to `-1/0/1/2/3`. Its base serializer omits operator `-1` and empty ID, and emits enabled/type. The derived serializer emits `on`/`off` for raw status `0/1`; raw status `-1` instead emits signed level unconditionally, including `-1`.

Under ordinary fresh-JSON/member/conversion semantics, this can retain the selected scalar pair while changing member presence: explicit `noStatus` can become `level=-1`. It is not a universal lossless round trip. [Serializer/query evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-condition-query/README.md) preserves the final/raw-base distinction and exact value paths.

The larger query first attempts ordinary lookup. On the selected cache-hit branch, it copies a nonnull cached pair to the caller before later selector, discriminator or response-length checks. This does not prove a stale/unsuitable record or global absence of validation; later field interpretation still requires a suitable live record.

A cache miss clears response-string length and a byte through its response pointer. Selected selector `0` reaches opaque call boundaries and, after normal returns/cleanup, a mutex/condition-variable loop waiting on nonempty response length. This registry's mutex at `+72` is not the shared action-stop byte with the same offset in a different object. Provider tick units and an overall deadline remain unresolved. Nonempty data after the comparison deadline can still reach response processing; a selected zero-length continuation clears both output words, while nonempty processing reaches the imported JSON parse boundary. Response production/notification, ID correlation, reconstructed type and full errors/concurrency remain unresolved.

## A distinct BNCUSCENE condition

Condition row `17` produces `BncuSceneCondition` (`88` bytes) and `BncuSceneConditionRunner` (`192` bytes). Base and derived ID/name strings are separate members, without a target-scene lookup established by their names.

The compiled constructor copies enabled to its own byte `132`. Its complete predicate reads that byte, XORs it with `1` and returns. For ordinary Boolean construction, disabled `0` returns `1` and enabled `1` returns `0`; arbitrary byte values are an unsigned XOR, not a universal logical-negation contract. The predicate performs no local ID/name/state lookup, timer or provider call.

The same primary pointer enters the scene's four-byte condition range. The generic worker calls its predicate slot and treats zero as failure. Thus an enabled object selected under those premises supplies a failing local result. Actual configured admission, other methods/mutations, intended feature meaning and physical consequences remain unresolved; no product-wide unsupported-feature or defect conclusion follows. [BNCUSCENE evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-removal-context/README.md) and [storage clarification](../../project/review/firmware-analysis/myhomeserver1-3.87.13-removal-context/condition-storage-refinement.txt) distinguish condition pointers from trigger/action control pairs.

## A selected nonconstant BNTH comparison

Condition row `11` constructs `BnthCondition` (`80` bytes) and `BnthConditionRunner` (`184` bytes). On the selected schema route, `mode` and `status` must be absent before present `setpoint` supplies `asDouble`. The constructor stores selector `2` and the configured double; compilation copies them to its own fields.

The enabled predicate looks up its ID in the local registry. With a suitable nonnull cached record, selector `2` and operator `2` compare the configured double with record double `+32`, returning `1` on equality and `0` otherwise under the selected finite-double/provider/cleanup premises. The same compiled pointer reaches the generic condition worker. Other schema/operator branches, exceptional floating-point behavior and configured execution remain unresolved. [BNTH condition evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-condition-ownership/distinct-condition-report.txt) derives this path independently of BNCUSCENE.

## BNTH value source on both sides of the comparison

The raw selector-`2` serializer emits its configured double under `setpoint` without a local zero/sentinel suppression. On the ordinary fresh-object route, base JSON adds ID/enabled/type/operator, without introducing mode/status members which would preempt setpoint reparse. The same JSON destination is passed to the raw constructor before compilation.

The selected event-code-`3` producer requests `asDouble` for a present setpoint and supplies double `0.0` when that member is absent, then stores it at Thermostat record `+32`. That default is a software value, not a physical zero or missing-device diagnosis. The record pair and local `params.id` reach the same registry. A matching discriminator-`3` update compares incoming/current doubles and copies the incoming value on its selected NE branch.

Under matching ID/type, valid ownership, normal providers and appropriate freshness, the predicate can therefore consume this producer's value. No physical thermostat unit, supported setpoint domain, public WHO meaning or natural transaction is established. [BNTH value evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-bnth-values/README.md) distinguishes those two source roles. The [scalar-provider contract](myhomeserver1-3.87.13-serialization.md#candidate-double-value-provider-contract) is narrower than full JSON member/map/reparse semantics.

## Evidence and limits

The source establishes selected local record, cache, callback and predicate relations. Complete external subscription/input admission, configured scenes, query/response correlation, valid current records, JSON coherence, ownership/unwind, concurrent lifetime and physical outcomes remain unresolved. Event `params.id` also differs from the removal path's [`params.scene_id`](myhomeserver1-3.87.13-serialization.md#local-removal-argument-provenance). No complete event-to-physical-action transaction is demonstrated.
