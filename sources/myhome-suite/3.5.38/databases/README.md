# MyHOME Suite 3.5.38 Databases

These are canonical, unmodified databases from MyHOME Suite 3.5.38. Exact byte sizes, SHA-256 fingerprints, original filenames, and original Windows paths are recorded in the [Source Manifest](../../../manifest.yaml).

| Repository file | Original installation location |
| --- | --- |
| `MHCatalogue.db` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_MHCatalogue\MHCatalogue.db` |
| `OPEN.db` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\db\OPEN.db` |
| `ScenarioDevices-program-files.sqlite` | `C:\Program Files (x86)\LegrandGroup\MyHOME_Suite_0305\ScenarioDevices.sqlite` |
| `ScenarioDevices-programdata.sqlite` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_ScenarioDevices\ScenarioDevices.sqlite` |
| `rules.db3` | `C:\ProgramData\LegrandGroup\MyHOME_Suite_0305\Shared\Db_KeyOThermoValidator\rules.db3` |

The two `ScenarioDevices.sqlite` source files have intentionally different repository names. They originate from different installation locations and are not byte-identical.

Do not add inferred foreign keys or otherwise transform these files. Reconstructed database relationships belong in the reverse-engineering documentation, not in the canonical databases.
