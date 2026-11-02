# MyHOMEServer1 3.87.13 Catalogue and Scene Consumers

The `matrix_mx` catalogue reader and `scheduling_manager` scene loader consume different kinds of data. The former obtains source-owned catalogue properties from SQLite; the latter parses scene JSON and constructs executable representations. A third provider, `libjsonmsg`, creates local receipt objects. Those roles are separate from accepted OpenWebNet input or successful physical actions.

## Reference and scope

These findings apply to [MyHOMEServer1 Firmware 3.87.13](myhomeserver1-3.87.13.md). The [source evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-consumers/README.md) identifies `matrix_mx`, `scheduling_manager` and `libjsonmsg`, their selected code and API boundaries. Catalogue content is documented under [source profiles](../../internals/mhcatalogue-source-profiles.md); the following sections describe its compiled consumers.

## Catalogue opening and selected row consumer

A `matrix_mx` helper requests two opens of the packaged `MHCatalogue.db` path into separate slots of the same context. Both API results must be zero for its local return `1`; its caller tests that return before another setup request. Error paths request diagnostics and cleanup and return `0`. This identifies a compiled consumer without demonstrating filesystem success or complete handle ownership.

A separate reader requests `stat`, then `sqlite3_open_v2` with flags `1` and a null VFS argument. After its open/handle guards, it prepares SQL stored on its own input object. The [query owner](myhomeserver1-3.87.13-factories.md#catalogue-reader-sql-and-concrete-owner) supplies the actual `15`-column template. Selected zero-based columns `13` and `14` are converted by base-10 `strtol` into slots and system-ID fields. Each later selected row can overwrite the destinations: a unique row, first-row policy and stable ordering are not established.

The first step test compares with `101`, while the loop-back test requires `100`. Ordinary exit requests statement finalization and handle closure. These code guards do not demonstrate returned rows or define a general Boolean success API. [Catalogue consumer evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-consumers/catalogue-report.txt) retains exact call sites, handles and result tests.

A separately registered initializer constructs this query:

```sql
SELECT AS_ITEM_SYSTEM.id_item, AS_ITEM_SYSTEM.id_system
FROM AS_ITEM_SYSTEM WHERE AS_ITEM_SYSTEM.main=1
```

It has not been connected to that reader's SQL slot. Its two columns must not be substituted for a reader accessing columns `13` and `14`.

## Scenario directory to parsed scene factories

| Stage | Selected implementation behavior |
| --- | --- |
| Settings | Read `scenesPath` and store its string; startup passes the getter's result to the loader |
| File selection | Iterate the directory, select `.json` paths and exclude exact `twiligts_times.json` and `action_schedule.json` names |
| Parsing | Open a C++ file stream, request JsonCpp `parseFromStream` and test its result |
| Scene construction | Pass the same parsed root to the same scene object's constructor |
| Element construction | Dispatch `triggers`, `conditions` and `actions` to separate factories |
| Runtime representation | Initialize the compiled runner from those raw objects; see [factories](myhomeserver1-3.87.13-factories.md) and [startup](myhomeserver1-3.87.13-startup.md) |

The configured directory is under extra `0`, at the image-relative `home/bticino/cfg/extra/0/scheduling_manager` path. Neither examined image manifest contains a regular file below that prefix. This limits available configured examples; it does not establish the state of a running installation. The excluded filenames retain their source spelling, and this loader's exclusion does not imply that another component never uses them.

The scene constructor handles `name`, `hidden`, `customizable`, `editable`, `has_button_trigger`, `id` and `enabled`. Missing `enabled` selects a stored true value; a present member supplies its converted value. The [launch functions](myhomeserver1-3.87.13-factories.md#enabled-gate-compiled-actions-and-stop-requests) consume that scene-enabled field. File selection and these local member accesses are not a complete accepted-input grammar. [Scene-loader evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-consumers/scheduler-report.txt) supplies exact fields, guards and exceptions.

## Separate JSON data and local receipt contracts

The scheduler uses C++ JsonCpp. `matrix_mx` declares the separate C `libjsonmsg` provider, which uses JSON-GLib/GObject/GLib. A provider declaration does not determine effective runtime binding.

| C-provider operation | Selected local contract |
| --- | --- |
| `new_json_msg` | Request a zeroed `20`-byte message and a separate `32`-byte root node; retain version string `2.0` and the root pointer |
| `generate_json_ack` | Duplicate the supplied identifier and request Boolean member `result=true` |
| `is_json_ack` | Read the selected Boolean result node's stored value |
| `is_json_response` | Require a different node-kind condition; the generated Boolean ACK is not automatically classified as this response form |

For the examined helpers, the normal generated Boolean node has kind `2` and value type `20`, whereas `is_json_response` requires kind `0`. Missing, wrong-type and false cases can share return `0`; the helper names are not a complete JSON protocol specification. [Provider evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13-consumers/providers-report-v2.txt) distinguishes static source from synthetic resolved-node examples.

A local receipt object is not an OpenWebNet ACK or evidence that an action succeeded, a response was sent, or a Physical Device acted. These C structures also differ from the C OPEN parser and C++ scene objects.

## Evidence limits

The opening, SQL ownership, parse-to-constructor and factory relations are source-supported. Full catalogue selection/fallback, complete scene validation, configured files, effective provider/type state and error/unwind behavior remain unresolved. Scheduling, concurrent lifetime, delivery and physical outcomes require evidence beyond these local calls.
