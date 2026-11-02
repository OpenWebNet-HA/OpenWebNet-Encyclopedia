# Installation and Source Layout

The retained MyHOME Suite `3.5.38` source set combines files from an installation with separately preserved installer resources. Original Windows paths are evidence of packaging location; they do not by themselves establish which copy is opened first, whether data is copied or synchronized at runtime, or whether a file is writable during normal use.

## Preserved implementation files

| Original file / provenance label | Original installation path | Size | SHA-256 |
| --- | --- | ---: | --- |
| `MHCatalogue.db` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_MHCatalogue\MHCatalogue.db` | 2,625,536 | `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5` |
| `OPEN.db` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\db\OPEN.db` | 80,896 | `d864a4946b47c3671a74a6844cec4da605cf20b33ac14f49959785778f104051` |
| `ScenarioDevices-program-files.sqlite` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\ScenarioDevices.sqlite` | 35,840 | `2ce7ffe1286c3246271aed160116fe664407d9e8ff43595f50192e7d2ac85569` |
| `ScenarioDevices-programdata.sqlite` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_ScenarioDevices\ScenarioDevices.sqlite` | 34,816 | `cd3b9b67160f468cdbd30134357b8733c696aacd5d625129240dff6b79224fc3` |
| `rules.db3` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_KeyOThermoValidator\rules.db3` | 36,864 | `23b62e3bb7a11ede3f91561b63a1aaf39449da47025626a2c477e9833347cb06` |
| `OpenQuery.txt` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\db\OpenQuery.txt` | 3,661 | `104bc9fcd780799f3b6bb85f2510b1b0424747c30c315f0a04c93e88f4163c10` |


The installer is not redistributed. Its registered size is 599,437,936 bytes and its SHA-256 is `707D8A43A5296A1EA87C33F111E9269C8BBD0FE524AC5EFE87BDEDE8B6EB311B`. The recorded Authenticode signature is valid and identifies BTICINO S.P.A. as signer.

## Repository naming

Both ScenarioDevices source files were originally named `ScenarioDevices.sqlite`. Their repository names record their distinct origins and prevent one from overwriting the other.

The names `program-files` and `programdata` are provenance labels, not asserted runtime roles. The Program Files copy is larger and contains additional capability rows, but that does not prove that it supersedes, migrates, or updates the ProgramData copy.

## File-format observations

All five database files are SQLite databases. `OpenQuery.txt` is preserved as UTF-8 with a byte-order mark and CRLF line endings.

The canonical-source policy requires byte-for-byte preservation. Do not:

- add inferred foreign keys to a canonical database;
- normalize or translate stored values in place;
- replace an older-looking ScenarioDevices copy with the larger copy;
- change line endings or encoding in `OpenQuery.txt`;
- store project-specific packet captures under `sources/`.

Derived schemas, relationship maps, comparison output, and interpretations belong in documentation or reproducible analysis outside the canonical source directory.

## Version boundary

All quantitative statements in this section are scoped to MyHOME Suite 3.5.38. A later installation may contain different Device and firmware coverage, revised management sequences or timer defaults, a different ScenarioDevices schema or capability set, or additional validation databases.

When comparing releases, identify rows by stable semantic context where possible and always preserve the source fingerprint. Local SQLite row IDs are not release-stable identifiers unless independent evidence establishes that stability.

## What installation paths do not prove

The available corpus does not establish database open order, update/synchronization direction, cache invalidation, all application-module ownership or project-edit transaction boundaries. The project templates establish declared persistence structures, and selected ScenarioSuite methods establish script/index writer calls; a genuine configured saved project or traced consumer is still needed for complete persistence behavior.

The packaging layout does not resolve those application runtime policies.

## Installer database census

The decoded index of the registered installer contains 20 database-extension paths representing 13 distinct SQLite payloads. Their source identities and private storage are recorded separately in the [artifact manifest](../sources/artifact-manifest.yaml). Aliases retain the same byte identity; different contents remain separate artifacts.

| Database family | Installer paths | Distinct payloads | Source treatment |
| --- | ---: | ---: | --- |
| MHCatalogue | 2 | 1 | Existing catalogue matches its restore alias |
| OPEN | 1 | 1 | Existing protocol/workflow source |
| rules | 1 | 1 | Existing linked-property source |
| ScenarioDevices | 3 | 2 | Existing program-files/programdata variants; restore alias retained |
| ScenarioSuite | 4 | 2 | [Distinct MH200N and MH202/common profiles](../scenario-engine/scenario-suite-variants.md) |
| systems | 7 | 4 | [F454 and touchscreen application profiles](device-application-databases.md) |
| MHPrj | 1 | 1 | [Project template](project-and-plant-templates.md) |
| PTDB | 1 | 1 | [Plant/spatial template](project-and-plant-templates.md) |

The census covers the decoded installer index and database-like extensions. It does not exhaust opaque/nested archives, extensionless files or the complete container format. The [installer evidence record](../project/review/installer-databases-3.5.38/README.md) retains extraction, integrity and coverage details. These installer files do not become databases bundled inside the separately examined gateway Firmware images.
