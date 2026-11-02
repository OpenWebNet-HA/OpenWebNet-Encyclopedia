# MyHOMEServer1 3.87.13 TIME Scenarios

`TIME` triggers request scene launch through a time service, while `TIME` conditions gate a launch by day and local-time boundaries. They are separate raw and compiled classes in [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md), with their own enum positions and serializers. The implementation describes selected requests and predicates, not measured scheduling or a complete accepted scene grammar.

## Concrete trigger and condition schema

| Element | Selected fields | Representation |
| --- | --- | --- |
| `TIME` trigger | `time`, `days`, inherited `enabled`, `id`, type/operator | Raw `TimeTrigger` (`68` bytes), compiled `TimeTriggerRunner` in an owned allocation |
| `TIME` condition | `from`, `to`, `days`, inherited enabled/type metadata | Raw `TimeCondition` (`92` bytes), compiled `TimeConditionRunner` (`200` bytes) |

Trigger index `0` has a special factory route; condition index `1` uses its separate adjusted dispatch. A type's presence in either table does not establish a general support declaration.

Both examined day parsers inspect at most seven characters and require each inspected character to be `0` or `1`. Serializers emit seven characters from bit `6` to bit `0`. Registered maps pair weekdays with bits `(0,0),(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)`. Under the ordinary [Linux weekday convention](https://man7.org/linux/man-pages/man3/tm.3type.html), the normalized seven-character form runs **Monday through Sunday**. Short prefixes, failed conversions and complete accepted JSON behavior remain unresolved.

## Trigger registration, deadline and firing

The initializer stores a compiled-trigger handle in the scene and registers that same handle with the supplied time-service instance. On the selected normal-capacity path, registration appends under a mutex and requests notification. [Startup](myhomeserver1-3.87.13-startup.md) supplies that service instance and a literal nonzero thread-start flag. Actual thread creation, queue readiness, mutation and handle lifetime remain conditional.

Trigger preparation requests current local time, parses exact `%H:%M`, replaces hour/minute, clears seconds and calls `mktime`. It converts the result to the system-clock scale and adds `86,400,000,000,000` once if it is strictly earlier than a fresh current-time reading. The packaged clock conversion supports nanosecond units under ordinary successful APIs; actual timezone, input validity and clock success remain unobserved.

The selected service route waits on a stored deadline, checks that one clock reading has reached it, then checks a second reading's absolute difference against `30,000,000,000`. Only the examined live-object continuation invokes the trigger. The trigger in turn requires its own enabled byte and current weekday bit before requesting its captured scene callback.

After a normally returning selected invocation, the service adds `86,400,000,000,000` to the stored deadline. Fixed arithmetic does not establish next-local-calendar-day/DST behavior or a `30`-second delivery guarantee. Queue ordering, expired entries, catch-up, missed firings and clock-change handling remain unresolved. [Trigger evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-triggers/time-trigger-report.txt) and [service evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-triggers/service-report.txt) retain the exact branches and API boundaries.

## Condition evaluation and action launch

A captured trigger callback reaches the scene's normal launch, with separate scene-enabled and scene-active guards. The requested condition worker traverses the scene's compiled condition pointers and invokes each predicate.

| TIME-condition branch | Selected result |
| --- | --- |
| Disabled | True, before day/clock checks |
| Enabled, wrong weekday | Fails the selected day test |
| Equal `from` / `to` boundaries | True after the weekday check |
| Distinct boundaries | Require strict `from < now < to`; endpoints are false |
| Reversed boundaries | No transformation into an overnight wrapping interval in this predicate |

Boundary helpers use current-date local-time values. A fixed `2021` date in a parsing string is scaffolding: only parsed clock fields are copied into the current calendar result. Parsing and ordinary time-provider returns remain premises.

The generic condition caller short-circuits on the first zero result, then clears the scene active/stop bytes on its normal failure path. All nonzero predicates, or an empty condition range, reach the [action worker](myhomeserver1-3.87.13-actions.md). Those scene bytes are not the shared action-wait stop flag. [Condition evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-triggers/time-condition-report.txt) identifies the original boundaries and calls.

## Evidence limits

Configured scene input, complete parsing/error rules, effective clock/timezone providers, DST/clock changes, queue/lifetime/concurrency and actual scheduling remain unresolved. No satisfied real scene or physical action follows from a registration or callback request. Catalogue names and the MH202 script language do not define this engine's time policy.
