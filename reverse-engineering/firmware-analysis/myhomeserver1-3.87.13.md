# MyHOMEServer1 3.87.13 Firmware

MyHOMEServer1 Firmware `3.87.13` combines an OpenWebNet/SCS core with a separate C++ application layer for home automation. Its scenario engine loads JSON descriptions into compiled trigger, condition and action objects; its catalogue consumer uses a database profile distinct from MyHOME Suite's catalogue. These are implementation findings for the identified build, with no complete configured scene or Physical Device behavior demonstrated.

The [MyHOMEServer1 Device definition](../../devices/definitions/own-dev-0199-myhomeserver1-home-automation-server.md) supplies product specifications and documented applicability. The [scenario-engine overview](myhomeserver1-3.87.13-research-synthesis.md) connects the implementation topics below; [tooling implications](myhomeserver1-3.87.13-knowledge-handoff.md) explain which distinctions an importer or scene-analysis tool must preserve.

## Reference

| Property | Source-scoped value |
| --- | --- |
| Manufacturer package | [SMARTGW_038713.fwz](https://assets.legrand.com/pim/AUTRE/SMARTGW_038713.fwz), `183381241` bytes |
| Package SHA-256 | `4ca1bcc70c1616270cb4c1f4b3ceb3c01c941797e437c3544d7d3d11b159c603` |
| Update declaration | `MyHomeServer1`, Firmware `3.87.13`, XML `3.1`, Object model `5.0.67` |
| Application architecture | Examined applications and core providers use ARM32 EABI5 hard-float; `matrix_mx` has a Thumb entry and position-independent executable layout |
| Implementation topics | [Catalogue and scene loading](myhomeserver1-3.87.13-consumers.md), [factories](myhomeserver1-3.87.13-factories.md), [startup registry](myhomeserver1-3.87.13-startup.md), [actions](myhomeserver1-3.87.13-actions.md), [time rules](myhomeserver1-3.87.13-time-scenarios.md), [local events](myhomeserver1-3.87.13-event-routing.md) |
| Evidence | [Package, source identities and method records](../../project/review/firmware-analysis/myhomeserver1-3.87.13/README.md) |

The package's model declaration is not an executed diagnostic response. MyHOMEServer1's home-control role does not acquire F454 AV/alarm hardware or the MH202 script engine through shared names or catalogue Objects.

## Application structure

The application layer includes `matrix_mx`, `scheduling_manager`, `alarm_manager`, `backup_manager`, `gateway_manager`, `energy_manager`, `player_manager` and `bt_smart_home_manager`. An executable name identifies a component; ownership of a complete product function requires its callers and consumers to be traced. Normal and recovery images share substantial file content but retain separate startup environments and selected differences.

The independently derived ARM hard-float layouts matter when following C++ objects and hidden return arguments. Older Firmware layouts cannot be transferred by filename. The [structural evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13/inventory-report.txt) identifies the examined components and original image files.

## Startup and configured ownership

The packaged SysVinit setup selects runlevel `5` and a vendor wrapper. The normal wrapper sets the library search path, changes to the application root and requests `bin/bt_daemon`. A user-library directory precedes packaged providers, so declared dependencies alone do not fix effective runtime binding.

Normal and recovery `stack_open.xml` copies declare the same `25` processes. The daemon stores the `working_mode` field, but its selected launch filter skips zero-mode records only when a separate global status equals `2`; the packaged `normal_status` is `4`. These are distinct local values, without inherited mode semantics from older Firmware. Eligible records reach a constructed `nice` command and child-launch request; actual launch and readiness remain unobserved.

| Packaged declaration | Interpretation |
| --- | --- |
| `scheduling_manager` scenes path under extra `0` | Configuration storage consumed by the [JSON scene loader](myhomeserver1-3.87.13-consumers.md#scenario-directory-to-parsed-scene-factories) |
| Alarm data path and sensor/partition filenames under extra `0` | Application-data declarations, without a dedicated alarm-bus topology established by this source |
| `scsserver`, `/dev/ttymxc2`, `bus_type=0` | One configured SCS lane; physical connector and global UART mapping remain unresolved |
| D-Bus and Redis startup scripts | Packaged service-start requests, without active-state or readiness observations |
| Recovery wrapper | Requests a converter and creates an extra `95` feature marker; the normal wrapper removes that marker |

The kernel image names Linux `5.10.35+gd50c7a7404d5+p0`. The selected normal device tree declares Linda-board, `fsl,imx6dl` and Cortex-A9 metadata. Actual board revision and selected boot tree remain unobserved. [Boot evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13/boot-report.txt) preserves the source locations and declarations.

## Embedded catalogue

The normal and recovery images contain identical `matrix_mx/MHCatalogue.db` payloads. The embedded database is `2233344` bytes, SHA-256 `79fcf2e2580dfe23349ead3d3e385ad8210cf44dddff3179a9c021644a7d1edb`. Its table definitions match MyHOME Suite `3.5.38`, while its complete schema and data differ. The [catalogue source profiles](../../internals/mhcatalogue-source-profiles.md) provide the canonical comparison, including reused Configuration IDs and equivalent fields with changed IDs.

`matrix_mx` has compiled opening calls and a selected `15`-column reader for that database. The corresponding [query and factory](myhomeserver1-3.87.13-factories.md#catalogue-reader-sql-and-concrete-owner) identify catalogue slots and system IDs. The complete selection/fallback policy and effective supplied values remain unresolved.

The embedded profile omits MyHOMEServer1's own catalogue item in the examined lookups. Its contents therefore cannot be treated as a complete self-capability declaration. Database version and export-date literals describe the source; they are not independently verified build or deployment dates. The file-prefix survey does not exclude other embedded formats or runtime-created stores.

## Separate OPEN implementations

The selected `bt_device` dependency family uses C++ `libopen`/`libdiag`/`libwhere` providers. `openserver` and COSO declare the C `libopenmsg` family. Definitions repeated in `libcommon` do not settle dynamic lookup.

In the packaged C parser, `new_open_msg` requests a zeroed `56`-byte object with a discriminator at offset `52`; the selected ordinary parser branch stores discriminator `1`. MH202's separately examined pointer parser uses a `48`-byte object and discriminator `44`. Neither is a common C++ object layout.

The auxiliary and automation plugins have distinct registration criteria and callbacks. Auxiliary criteria use `9` in both directional lists; automation uses reverse criterion `1` and forward criterion `2`. These local criteria, parser kinds, envelope representations, callback directions and public WHO values remain separate namespaces. The [protocol evidence](../../project/review/firmware-analysis/myhomeserver1-3.87.13/protocol-report.txt) records selected four-byte auxiliary body construction and a separate reverse WHO `9` formatter; its synthetic host examples are not an observed round trip. The examined seven-file COSO directory does not establish implementations for every exported descriptor name.

## Evidence limits

Static source inspection establishes selected construction, argument, branch and ownership relations. An isolated packaged JsonCpp experiment additionally verifies four scalar constructor/readback cases, as described under [serialization](myhomeserver1-3.87.13-serialization.md#isolated-original-scalar-constructor-and-readback). It does not execute the scene engine.

The downloaded package lacks referenced extras `80.xtz`, `81.xtz`, `94.xtz` and `95.xtz`, and provides no populated scene file under the selected configured prefix. Actual configuration, service/provider binding, complete accepted scene grammar, error/unwind and concurrent lifetime behavior, delivery, persistence and physical effects remain unresolved. Retained signature blobs have not been shown to authenticate the package through a verified trust chain.
