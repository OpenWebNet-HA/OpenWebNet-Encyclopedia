# Capability Resolution

This page describes how to turn ScenarioDevices rows into a structured scenario-editor capability without assuming that every stored identifier is an OpenWebNet wire value.

## Input

Start with one source file and, where possible:

- a desired functional area;
- a desired role such as trigger, condition, or action;
- the installed Device/Object context from diagnostics and the Device Model;
- the functional `WHO` reference needed to validate a stored frame.

## Resolution path

1. Select candidate `ObjectSystems` rows by established system/category evidence.
2. Enumerate their `DeviceObjects`.
3. Retain `ObjectId` and `ObjectMatchingId` as ScenarioDevices identifiers.
4. Enumerate each Object's Commands.
5. Load all Parameters for each Command.
6. Classify the command as literal-frame, symbolic-frame, or frame-absent.
7. Validate any stored `ChiOpen` against the functional frame.
8. Resolve `WHERE` according to the functional `WHO`, not `WhereType` alone.
9. Validate parameter values against stored metadata and the functional reference.
10. Return the capability with source-file and row provenance.

## Resolve the hierarchy

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
    c.WherePlaceholder,
    c.WhereType,
    c.WhereName,
    c.ChiOpen,
    c.Frame,
    p.Id AS parameter_row,
    p.Placeholder,
    p.Name AS parameter_name,
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
WHERE os.Id = :object_system_id
ORDER BY d.Id, c.Id, p.Id;
```

## Reference algorithm

```text
function resolve_capabilities(source, requested_context):
    systems = query ObjectSystems compatible with requested_context
    output = []

    for system in systems:
        for object in DeviceObjects where ObjectSystem_Id == system.Id:
            object_match = correlate_only_with_established_mapping(object)

            for command in Commands where DeviceObject_Id == object.Id:
                parameters = Parameters where Command_Id == command.Id

                capability = {
                    source file and row IDs,
                    resource keys,
                    ScenarioDevices IDs,
                    category evidence,
                    stored WHO evidence,
                    address metadata,
                    frame template,
                    parameter definitions
                }

                if command.Frame is a literal OpenWebNet template:
                    capability.rendering = parse_without_substitution(command.Frame)
                else if command.Frame is symbolic:
                    capability.rendering = unresolved symbolic operation
                else:
                    capability.rendering = no stored frame

                validate against functional reference and installed Object context
                output.append(capability with resolution status)

    return output without first-row-wins selection
```

## Category handling

Resource keys commonly end in `.trigger`, `.condition`, or `.action`, and their `CategoryFlag` values form consistent clusters. This is strong implementation evidence, but the draft does not yet declare a universal numeric enumeration for the flags.

Present both:

- the resource-key-derived role;
- the raw `CategoryFlag`.

Do not discard a row solely because its flag is not yet interpreted. See [Categories and Matching](categories-and-matching.md) for the complete observed flag distribution and the evidence supporting the current role names.

## Installed-Device filtering

The ScenarioDevices files contain no installed Device ID and no direct Module slot. Filtering capabilities for a real installation therefore requires a staged correlation:

1. diagnose the Device and resolve its configured Object;
2. determine the functional system and behavior supported by that Object;
3. correlate that established behavior with ScenarioDevices Object/resource keys;
4. retain ambiguity where `ObjectId` or matching IDs lack a proven mapping.

Do not write a cross-database SQL join equating `DeviceObjects.ObjectId` with `EN_KEY_OBJECT.key_object` unless independent evidence establishes that relationship for the relevant rows.

## Result

Parameter rows require type-specific handling, especially where several rows share one composite placeholder. See [Parameters](parameters.md).

Return a capability record containing:

- source database and row IDs;
- Object System and Device Object resource keys;
- raw category and matching identifiers;
- Command name and identifiers;
- functional `WHO` evidence;
- address requirements;
- frame classification;
- complete parameter definitions;
- correlations and their evidence level;
- status: resolved, partial, ambiguous, symbolic, or unsupported.
