# Legacy gateway application-data sources

Source from F450 and F459 describes application-data requests, while the inspected legacy packages supply no recovered plaintext application database. This distinction matters when using manufacturer software as evidence for configuration or interoperability: library presence, compiled SQL and file names are not actual data or successful persistence.

Exact builds and separate product roles are in the [legacy Firmware reference](f450-f453av-f455-f459-mh200n.md#reference-and-applicability). Manufacturer installer databases are documented separately under [application databases](../../internals/device-application-databases.md) and [project/plant templates](../../internals/project-and-plant-templates.md).

## What the database evidence establishes

| Source | Established evidence | Limit |
| --- | --- | --- |
| F450 PROD `50.xtz` | Original encrypted container naming `50/master.sqlite` in central-directory metadata | No plaintext header, schema, rows or effective decoder recovered |
| F450 source | Compiled copy request from `cfg/extra/50/master.sqlite` to `/var/tmp/db/master.sqlite`, followed by an opening request for that destination; separate configuration/archive inputs | No successful copy/open/query or established link from extra50 bytes to the consumer |
| F459 shared store | Opening request for `/tmp/plugin.shared.sqlite`, SQL/read/write, namespace, watcher and teardown contracts | No recovered runtime database, schema/rows, freshness or durable transaction |
| Packaged SQLite libraries | Distinct legacy-interface and SQLite3 import evidence | No automatic assignment of the active provider or file format |
| `Thumbs.db` candidate | OLE container header | No application catalogue established |

The [format assessment](f450-f459-database-byte-followup.md) searches a declared finite set of signatures beyond file prefixes. Its negative result does not exclude encrypted, compressed, custom-format, fragmented, configured or runtime-created stores. SQL declarations were not used to manufacture an original-looking database, and no incompatible legacy parser was substituted.

## Product-specific implications

F450 standard and PROD retain different package identities. Selected markup-to-context fields, an archive request and a conditional configuration-path alias explain local data sources without supplying actual live values or decryption. Its BACnet resource helper's input/return-word edge does not establish a complete template or mapping parser. See [F450 configuration and data requests](f450-f453av-f455-f459-mh200n.md#f450-configuration-and-archive-requests-remain-distinct-from-extra50).

F459's selected store separates namespace, key, value and `persistent` SQL arguments. The integer's placeholder role is not a durability guarantee. Watcher/static callback metadata establishes local ownership and name/index relations, not delivered file events or fresh query results. See [F459 shared-store behavior](f450-f453av-f455-f459-mh200n.md#f459-a-shared-store-request-is-not-durable-state).

MH200N/F453AV resource/application evidence and F455's format hypothesis are separate from database recovery. Image views and application bundles do not establish a deployed overlay; script-file requests do not supply a configured scenario or accepted compiler grammar. See [resource context](f450-f453av-f455-f459-mh200n.md#mh200n-and-f453av-resource-and-module-requests-need-their-own-environment).

## Original data

The preserved F450 PROD support container is 72,774 bytes, SHA-256 `824b9b224689afa75d27d5271cbb812d18d0a13915696f1404d21500191bf9d8`. It is an encrypted original, not plaintext `master.sqlite`. The [classified source record](../../project/review/firmware-analysis/remaining-firmware-2026-11-01/archive-index.json) and [archive receipt](../../project/review/firmware-analysis/remaining-firmware-2026-11-01/archive-receipt.json) identify that object. One support container and zero plaintext database objects describes this investigation, not every object in the private archive.

## Evidence

| Subject | Source evidence |
| --- | --- |
| Original packages and initial file survey | [Acquisition and source catalogue](../../project/review/firmware-analysis/remaining-firmware-2026-11-01/README.md) |
| Configuration origins and namespace | [Path/owner source records](../../project/review/firmware-analysis/remaining-firmware-run05-2026-11-01/README.md) |
| Resource and lifetime requests | [Resource/teardown records](../../project/review/firmware-analysis/remaining-firmware-run06-2026-11-01/README.md) |
| Script requests, watcher and F455 provenance | [Application/metadata evidence](../../project/review/firmware-analysis/remaining-firmware-run07-2026-11-01/README.md) |
| Line consumer and callback identity | [Consumer/metadata records](../../project/review/firmware-analysis/remaining-firmware-run08-2026-11-01/README.md) |
| Embedded format qualification | [Signature/header evidence](../../project/review/firmware-analysis/sequential-databases-2026-11-02/README.md) |

## Evidence limits

A properly attributed plaintext database or qualified alternate-format extent would provide a stronger data source. Accepted schema/rows, complete error handling, active providers, natural caller/configuration, freshness, ownership/concurrency and physical behavior remain unresolved. Static requests and source metadata cannot supply those observations.

## Source scope

The [preserved research record](../../project/review/firmware-analysis/remaining-firmware-final-2026-11-02/README.md) retains the investigation's scope and remaining evidence gaps. Its process history and archival workflow are supporting records; the reference conclusions above concern application data and their limits.
