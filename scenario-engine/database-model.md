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

Attach both files and compare semantic columns rather than local row IDs:

```sql
ATTACH DATABASE 'ScenarioDevices-program-files.sqlite' AS files_db;
ATTACH DATABASE 'ScenarioDevices-programdata.sqlite' AS data_db;

SELECT
    f.Name AS command_name,
    f.CommandId AS files_command_id,
    d.CommandId AS data_command_id,
    f.Frame AS files_frame,
    d.Frame AS data_frame
FROM files_db.Commands AS f
LEFT JOIN data_db.Commands AS d
  ON d.Name = f.Name
WHERE d.Id IS NULL
   OR d.CommandId IS NOT f.CommandId
   OR d.Frame IS NOT f.Frame
ORDER BY f.Name;
```

`Name` is useful comparison evidence because it is a resource key, but it is not declared as a unique cross-file key. Preserve duplicate matches and inspect their parent Object/System context.

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
