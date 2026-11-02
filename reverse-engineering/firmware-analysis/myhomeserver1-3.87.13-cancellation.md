# MyHOMEServer1 3.87.13 Cancellation and Action Completion

A scene-stop request, a cleared scene-active flag, individual action completion and the shared action-wait cancellation flag are different states in [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md). Understanding those distinctions prevents a local cleanup or restart-eligibility result from being mistaken for completed workers or successful actions.

## Separate state and separate completion

| State | Selected source role |
| --- | --- |
| Scene stop (`+144`) | Checked after each entered action returns and after a polling sleep |
| Scene active (`+145`) | Cleared by the selected normal scene-worker cleanup |
| Action completion (`+4`) | Individual byte read by the scene poll |
| Shared action-domain flag (`+72`) | Cancellation input for selected common wait workers; separate from every scene object |

Scene stop sets its own flag and requests each compiled action's stop method. Examined common, `SLEEP` and `SCENARIO` slots reach the common method which sets the shared flag under a mutex and requests notification. Other derived methods and interruption of an entered callback remain separate questions.

For an incomplete action, the scene poll requests `nanosleep` with `(1, 0)`, nominally one second under the verified provider layout. After that request returns it tests scene stop; nonzero can leave the poll while individual completion remains zero. This is a request interval, not a measured period or cancellation deadline.

Under normal delegate/cleanup returns, the scene worker clears its active and stop bytes. It neither sets individual completion nor joins action workers at those stores. A later admitted launch can pass the active guard again, without proving a successful rerun, terminated old workers or a reset shared domain. An inline blocking `SLEEP` must return before the action-loop stop check. [Scene-stop evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-cancellation/scene-stop-report.txt) preserves these paths.

## Shared cancellation ownership remains a distinct gap

The startup initializer clears the shared action flag. Its exit registration delegates condition-variable destruction, which is separate from that flag: the examined condition-variable constructor clears its own `48` bytes, not the flag at `+72`.

Selected alias/store searches have not established another shared reset owner. This is not proof of a permanent latch, absent reset or defect. Clearing scene bytes must not be substituted for resetting shared cancellation. [Shared-domain evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-cancellation/stop-domain-report.txt) defines the examined scope.

## A concrete duration producer and second callable

`Bn3lActionRunner` copies raw duration metadata into the operational-duration word. A nonzero value leads its constructor to install a second callable. That binding differs from the selected `SLEEP` construction path, which retains duration as metadata without establishing the same operational binding.

Common execution invokes the first callable inline only when operational delay is zero, then freshly checks duration before requesting its second worker. A nonzero delay takes a worker route which does not locally chain that second phase. Constructor metadata therefore does not establish a universal two-stage action schedule. [Duration-binding evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-cancellation/action-lifecycle-report.txt) records the exact constructor and execution branches.

## Evidence limits

These are static implementation relations, not a demonstrated thread interleaving or stop/restart experiment. Effective providers, configured classes, normal-return and error behavior, shared-reset ownership, concurrent lifetime and physical outcomes remain unresolved. [Worker lifetime](myhomeserver1-3.87.13-lifetime.md) explains why detached holders and raw receiver captures require separate ownership analysis; [action execution](myhomeserver1-3.87.13-actions.md) describes the callback and wait paths.
