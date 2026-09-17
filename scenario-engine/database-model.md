# Database Model

The ScenarioDevices databases are compact SQLite capability catalogues used by the MyHOME_Suite scenario editor. They describe available scenario Objects and commands; they are not databases of user-authored scenario instances.

## Source files

| File | Role established by content |
| --- | --- |
| `ScenarioDevices-program-files.sqlite` | larger capability set and the only revision with `ObjectSystems.FamilyId` |
| `ScenarioDevices-programdata.sqlite` | closely related capability set without `FamilyId` |

The filenames suggest different packaging roles, but the precise application selection rule is not yet established.

## Tables

### `ObjectSystems`

Groups Device Objects into named functional/category contexts.

| Column | Notes |
| --- | --- |
| `Id` | local primary key |
| `FamilyId` | present only in `program-files`; semantics require further correlation |
| `Name` | localization/resource key such as `miniScenarioSuite.automation.action` |
| `CategoryFlag` | numeric category discriminator; names strongly suggest trigger/condition/action grouping, but numeric semantics remain provisional |

### Observed `FamilyId` grouping

`FamilyId` appears only in the Program Files copy and consistently groups all category rows for one resource-key functional family:

| `FamilyId` | Resource-key family |
| ---: | --- |
| `1` | Alarm |
| `2` | Automation |
| `3` | Auxiliaries |
| `4` | Delay |
| `5` | Hotel |
| `6` | Lighting |
| `7` | Scenarios |
| `8` | Scheduled Scenarios |
| `9` | Special Commands |
| `10` | Temperature Control |
| `11` | Time |
| `12` | Virtual Key Card |

This establishes `FamilyId` as a local scenario-editor family grouping. It does not establish equality with a functional `WHO`, `OPEN.db` system ID, catalogue family ID, or any other database namespace.

### `DeviceObjects`

| Column | Notes |
| --- | --- |
| `Id` | local primary key |
| `ObjectId` | scenario-engine Object identifier; not proven equal to `EN_KEY_OBJECT.key_object` |
| `ObjectMatchingId` | optional matching identifier with unresolved cross-source semantics |
| `Name` | localization/resource key |
| `ObjectSystem_Id` | declared foreign key to `ObjectSystems.Id` |

### `Commands`

| Column | Notes |
| --- | --- |
| `Id` | local primary key |
| `CommandId` | scenario-engine command identifier |
| `CommandMatchingId` | optional matching identifier |
| `Name` | localization/resource key |
| `WherePlaceholder` | address placeholder where present |
| `WhereType` | numeric address-type discriminator |
| `WhereName` | localization/resource key for the address field |
| `ChiOpen` | stored functional `WHO` evidence where present |
| `Frame` | literal or symbolic frame template; can be `NULL` |
| `DeviceObject_Id` | declared foreign key to `DeviceObjects.Id` |

### `Parameters`

| Column | Notes |
| --- | --- |
| `Id` | local primary key |
| `Min`, `Max`, `Step` | numeric-domain metadata where applicable |
| `Placeholder` | text substituted into a frame or interpreted by the application |
| `Name` | localization/resource key |
| `OperatorType` | numeric operator discriminator |
| `Value` | stored constant or selector value where present |
| `Type` | numeric parameter-type discriminator |
| `Command_Id` | declared foreign key to `Commands.Id` |

## Declared relationships

```sql
SELECT
    os.Id AS object_system_row,
    os.Name AS object_system_name,
    os.CategoryFlag,
    d.Id AS device_object_row,
    d.ObjectId,
    d.ObjectMatchingId,
    d.Name AS device_object_name,
    c.Id AS command_row,
    c.CommandId,
    c.CommandMatchingId,
    c.Name AS command_name,
    c.ChiOpen,
    c.Frame,
    p.Id AS parameter_row,
    p.Placeholder,
    p.Min,
    p.Max,
    p.Step,
    p.Type,
    p.OperatorType,
    p.Value
FROM ObjectSystems AS os
JOIN DeviceObjects AS d
  ON d.ObjectSystem_Id = os.Id
JOIN Commands AS c
  ON c.DeviceObject_Id = d.Id
LEFT JOIN Parameters AS p
  ON p.Command_Id = c.Id
ORDER BY os.Id, d.Id, c.Id, p.Id;
```

Use the row primary keys for joins inside one file. Do not join the two files by `Id`: corresponding semantic rows can have different local identities or be absent.

## Compare the revisions

Attach both files and compare a Command by its full hierarchy rather than local IDs or `Commands.Name` alone:

```sql
ATTACH DATABASE 'ScenarioDevices-program-files.sqlite' AS files_db;
ATTACH DATABASE 'ScenarioDevices-programdata.sqlite' AS data_db;

WITH files_commands AS (
    SELECT
        os.Name AS system_name,
        os.CategoryFlag,
        d.Name AS object_name,
        d.ObjectId,
        d.ObjectMatchingId,
        c.Name AS command_name,
        c.CommandId,
        c.CommandMatchingId,
        c.WherePlaceholder,
        c.WhereType,
        c.WhereName,
        c.ChiOpen,
        c.Frame
    FROM files_db.ObjectSystems AS os
    JOIN files_db.DeviceObjects AS d ON d.ObjectSystem_Id = os.Id
    JOIN files_db.Commands AS c ON c.DeviceObject_Id = d.Id
),
data_commands AS (
    SELECT
        os.Name AS system_name,
        os.CategoryFlag,
        d.Name AS object_name,
        d.ObjectId,
        d.ObjectMatchingId,
        c.Name AS command_name,
        c.CommandId,
        c.CommandMatchingId,
        c.WherePlaceholder,
        c.WhereType,
        c.WhereName,
        c.ChiOpen,
        c.Frame
    FROM data_db.ObjectSystems AS os
    JOIN data_db.DeviceObjects AS d ON d.ObjectSystem_Id = os.Id
    JOIN data_db.Commands AS c ON c.DeviceObject_Id = d.Id
)
SELECT f.*
FROM files_commands AS f
LEFT JOIN data_commands AS d
  ON d.system_name = f.system_name
 AND d.CategoryFlag = f.CategoryFlag
 AND d.object_name = f.object_name
 AND d.command_name = f.command_name
WHERE d.command_name IS NULL
   OR d.ObjectId IS NOT f.ObjectId
   OR d.ObjectMatchingId IS NOT f.ObjectMatchingId
   OR d.CommandId IS NOT f.CommandId
   OR d.CommandMatchingId IS NOT f.CommandMatchingId
   OR d.WherePlaceholder IS NOT f.WherePlaceholder
   OR d.WhereType IS NOT f.WhereType
   OR d.WhereName IS NOT f.WhereName
   OR d.ChiOpen IS NOT f.ChiOpen
   OR d.Frame IS NOT f.Frame
ORDER BY f.system_name, f.CategoryFlag, f.object_name, f.command_name;
```

The canonical comparison shows that the semantic rows in `programdata` are an exact subset of `program-files` when the full parent path and non-local fields are used. The six additional Commands are four Virtual Key Card event rows and the Temperature Control local-control and fan-coil-speed actions. The latter two have one additional Parameter each.

`Commands.Name` alone is unsafe as a comparison key because the same resource key can occur beneath primary and complementary event categories.

## Integrity checks

```sql
PRAGMA foreign_key_check;

SELECT c.Id, c.Name
FROM Commands AS c
LEFT JOIN DeviceObjects AS d ON d.Id = c.DeviceObject_Id
WHERE d.Id IS NULL;

SELECT p.Id, p.Name
FROM Parameters AS p
LEFT JOIN Commands AS c ON c.Id = p.Command_Id
WHERE c.Id IS NULL;
```

The canonical files declare the three hierarchy foreign keys. Application-level identifiers and cross-database correlations remain outside those constraints.
