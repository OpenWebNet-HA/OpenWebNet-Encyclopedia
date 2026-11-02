# MyHOMEServer1 3.87.13 Startup and Scene Registry

The scheduler's selected startup path supplies one scene registry and one time-trigger service to scene-file loading. A nested `SCENARIO` action captures that same registry. This establishes object identity between loading and selected target lookup, while actual installed entries and successful target execution remain unresolved.

The scope is [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md). [Startup and registry evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-startup/README.md) identifies the original entry, calls, ownership records and key handling.

## Entry, settings and service construction

The executable's relocation-backed entry supplies its main function to `__libc_start_main`. Selected main code chooses `argv[1]` when supplied, otherwise `./scheduling_manager/config.json`, and passes that pathname to the settings loader. A zero loader result produces a diagnostic and rejoins normal continuation; that test alone is not an exit gate or proof of usable settings.

The packaged `scenesPath` points under extra `0` to `home/bticino/cfg/extra/0/scheduling_manager`. A copied setting becomes the scene loader's directory argument. Actual command-line input, working directory, configuration parsing and scene files remain unobserved.

Main constructs a scene container and requests an owned time-service allocation. It supplies literal `1` to the selected `TimeTriggersService` constructor, so the source path includes a service-thread start request. Allocation, initialization, actual thread creation and readiness remain conditional.

## The same objects through loading and nested actions

| Object or input | Relation established by the selected source |
| --- | --- |
| Scene container | Main passes it to file loading and runner initialization |
| Time service | Main's owned service instance is passed to loading and runner initialization |
| Scene-file path | Comes from the copied `scenesPath` setting |
| Per-file scene | Its constructor receives those same container and service arguments |
| `TIME` trigger | Registration receives the supplied time-service instance |
| `SCENARIO` action | Captures the supplied scene-container pointer for target lookup |

The container has two tree-shaped regions. The insertion/lookup correspondence concerns its first tree; it does not establish a complete interpretation of the second. The nested action's key predicate and value reader operate on that first tree under valid tree, handle, lifetime and normal-return premises. A configured target, successful launch and actual action completion do not follow from pointer identity.

## Numeric IDs, insertion and duplicates

On the examined present-ID path, the scene constructor converts `id` using JsonCpp `asString` and base-10 `strtol`, retaining a `32`-bit numeric key. Original source spelling and stored key identity therefore differ. This does not define a complete accepted-ID grammar.

For an absent key, registry insertion allocates a tree node, stores the key and scene/control pair, requests rebalancing and increments the count. For an equal existing key, the selected wrapper returns `0` without replacing the stored value. The loader does not test that Boolean before handle cleanup.

This is a local no-replacement rule, not an atomic-load or directory-order policy. Scene construction and possible trigger registration precede insertion, so refusing a duplicate does not imply that no earlier side effects were requested. [Registry evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-startup/registry-report.txt) preserves the exact node and handle paths.

## Category-specific key allocation

One numeric category `2` path may change the scene key before insertion. IDs `20..32767` bypass that allocator on the selected guard. Other bit patterns call a helper whose category-`2` route starts at candidate `20` and searches occupied keys before returning a free candidate or reaching an exception boundary.

The registry key is consequently not always the untouched JSON ID. This local rule does not assign a public category meaning or universal scene-ID range. Other categories, file rewriting, filesystem success and recovery remain unresolved.

## Source ordering and remaining boundaries

The selected order is time-service thread request, file loading, per-scene runner/element construction, then registry insertion. The source does not establish boot readiness, concurrent activation, file order, target availability, later registry mutation or complete lifetime/unwind behavior.

[Time rules](myhomeserver1-3.87.13-time-scenarios.md) describe selected registration and predicates; [compiled actions](myhomeserver1-3.87.13-actions.md) describe nested launch; [cancellation](myhomeserver1-3.87.13-cancellation.md) separates cleanup and completion. Populated scene assets, referenced extras `80/81/94/95`, complete duplicate/category/ID policy and physical behavior remain unresolved.
