# Scenario Engine

The Scenario Engine section documents the capability model used by MyHOME_Suite to expose triggers, conditions, and actions and to associate them with OpenWebNet command templates.

It is distinct from:

- functional OpenWebNet scenarios under functional `WHO 0` and `WHO 17`;
- diagnostic and programming scenarios in `OPEN.db`, which describe MyHOME_Suite communication sequences;
- the configuration of scenario-capable Physical Devices.

The canonical sources for this section are the two ScenarioDevices databases preserved under [`sources/`](../sources/myhome-suite/3.5.38/databases/):

- [`ScenarioDevices-program-files.sqlite`](../sources/myhome-suite/3.5.38/databases/ScenarioDevices-program-files.sqlite);
- [`ScenarioDevices-programdata.sqlite`](../sources/myhome-suite/3.5.38/databases/ScenarioDevices-programdata.sqlite).

## Reference

| Subject | Page |
| --- | --- |
| Database roles, schema, relationships, and revision differences | [Database Model](database-model.md) |
| Scenario roles and cross-role matching identifiers | [Categories and Matching](categories-and-matching.md) |
| Resolving systems, Objects, commands, and parameters | [Capability Resolution](capability-resolution.md) |
| Parameter types, operators, domains, and composite values | [Parameters](parameters.md) |
| Interpreting and rendering stored command templates | [Frame Templates](frame-templates.md) |
| Functional/category coverage and source-revision delta | [Capability Coverage](capability-coverage.md) |
| Established action pipeline and runtime boundaries | [Execution Model](execution-model.md) |
| Evidence limits and questions requiring further investigation | [Open Questions](open-questions.md) |

## Canonical hierarchy

Both databases use the same principal hierarchy:

**Object System → Device Object → Command → Parameter**

| Level | Table | Role |
| --- | --- | --- |
| Object System | `ObjectSystems` | groups scenario capabilities by functional area and category |
| Device Object | `DeviceObjects` | describes a scenario-engine Object within one Object System |
| Command | `Commands` | defines a trigger, condition, or action and may provide a frame template |
| Parameter | `Parameters` | defines placeholders, domains, operators, constants, and value types for one Command |

The relationships are declared as SQLite foreign keys:

- `DeviceObjects.ObjectSystem_Id → ObjectSystems.Id`;
- `Commands.DeviceObject_Id → DeviceObjects.Id`;
- `Parameters.Command_Id → Commands.Id`.

These IDs are local to each ScenarioDevices file. They are not `WHO`, `WHAT`, catalogue `id_key_object`, external `key_object`, or Device IDs.

## Source revisions

| Source | Object Systems | Device Objects | Commands | Parameters | Additional field |
| --- | ---: | ---: | ---: | ---: | --- |
| `ScenarioDevices-program-files.sqlite` | 29 | 44 | 157 | 42 | `ObjectSystems.FamilyId` |
| `ScenarioDevices-programdata.sqlite` | 27 | 42 | 151 | 40 | none |

The files overlap substantially but are not byte-identical or row-identical revisions. Documentation must identify which source supports a statement. A row present in one file must not automatically be described as universally available in the other.

The larger `program-files` revision adds Virtual Key Card event capabilities and two Temperature Control actions absent from `programdata`. See [Capability Coverage](capability-coverage.md) for the exact delta.

## Capability path

To enumerate one scenario capability:

1. select an `ObjectSystems` row;
2. enumerate its `DeviceObjects`;
3. enumerate the Commands for each Device Object;
4. load zero or more Parameters for each Command;
5. interpret the Command's `Frame`, `ChiOpen`, `WherePlaceholder`, and `WhereType`;
6. substitute only validated address and parameter values;
7. correlate the rendered result with the relevant functional `WHO` reference;
8. preserve commands whose `Frame` is absent as capabilities requiring separate interpretation rather than discarding them.

## Cross-source boundaries

The ScenarioDevices databases describe scenario-editor capabilities and command templates. They do not directly identify installed Physical Devices or their current configuration.

| Question | Source |
| --- | --- |
| Which Device and Modules are installed? | [Diagnostics](../diagnostics/) |
| Which Objects can firmware expose? | [Device Model](../device-model/) |
| What does a functional frame mean? | [Functional reference](../functional/) |
| How are Devices configured? | [Programming](../programming/) |
| How does MyHOME_Suite order diagnostic/programming exchanges? | `OPEN.db`, not the ScenarioDevices hierarchy |

Equal numeric values across these sources do not establish a join. `ObjectId`, `ObjectMatchingId`, `CommandId`, and `CommandMatchingId` require independent correlation before they can be mapped to another database namespace.

## Evidence status

Established directly:

- table structures and declared foreign keys;
- stored names, IDs, category flags, templates, placeholders, ranges, steps, and constants;
- row counts in the canonical files;
- differences between the two source revisions.

Partially interpreted:

- the practical meaning of `CategoryFlag`, `WhereType`, parameter `Type`, and `OperatorType`;
- the roles of matching IDs;
- commands with symbolic or absent frames;
- how MyHOME_Suite chooses between overlapping rows in the two files.

Unknown values remain unknown until database correlations, application behavior, public documentation, or observed execution establishes their semantics.
