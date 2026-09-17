# Frame Templates

`Commands.Frame` stores either a literal OpenWebNet template, a symbolic operation, or no frame. Rendering must therefore begin with classification rather than unconditional string replacement.

## Command fields

| Field | Use |
| --- | --- |
| `Frame` | literal or symbolic command representation |
| `ChiOpen` | stored functional `WHO` evidence |
| `WherePlaceholder` | token representing the destination where present |
| `WhereType` | raw address-type discriminator |
| `WhereName` | address-field resource key |
| `Name` | command resource key and semantic evidence |

## Template classes

### Literal OpenWebNet frame

Example stored value:

`*2*1*WHERE##`

This can be parsed as a functional command template. The `WHERE` token still requires the `WHO 2` address grammar and an independently selected destination.

### Literal frame with parameter placeholders

A frame can contain tokens also described by `Parameters.Placeholder`. Each placeholder must be resolved from the Parameter row and validated before substitution.

### Symbolic operation

Example pattern:

`ResetSOS[WHERE]`

This is not a complete OpenWebNet frame. It requires an application mapping or another source before it can be transmitted.

### Missing frame

A `NULL` frame does not prove that the capability is non-executable. It proves only that this database row does not contain a renderable frame template.

## Retrieve one template

```sql
SELECT
    c.Id,
    c.Name,
    c.ChiOpen,
    c.Frame,
    c.WherePlaceholder,
    c.WhereType,
    c.WhereName,
    p.Id AS parameter_id,
    p.Placeholder,
    p.Name AS parameter_name,
    p.Min,
    p.Max,
    p.Step,
    p.Type,
    p.OperatorType,
    p.Value
FROM Commands AS c
LEFT JOIN Parameters AS p
  ON p.Command_Id = c.Id
WHERE c.Id = :command_row_id
ORDER BY p.Id;
```

## Safe rendering algorithm

```text
function render(command, selected_where, supplied_values):
    if command.Frame is NULL:
        return unresolved("no stored frame")

    if command.Frame is not syntactically an OpenWebNet template:
        return unresolved("symbolic operation")

    parsed = parse frame structure before substitution

    if command.ChiOpen is present:
        require parsed WHO agrees with established ChiOpen interpretation

    if command.WherePlaceholder is present:
        validate selected_where using the parsed WHO address grammar
        replace only the complete declared WHERE token
    else if selected_where was supplied:
        reject unused input

    for parameter in command.Parameters:
        value = supplied value or established stored constant
        validate type, operator, min, max, and step where interpreted
        replace only the complete declared placeholder

    require no unresolved placeholder remains
    serialize and parse the result again
    require serialized frame has the expected WHO and frame family

    return rendered frame plus full substitution provenance
```

## Numeric-domain validation

For a numeric Parameter with established numeric semantics:

```text
valid = value >= Min
    and value <= Max
    and (Step is absent or (value - Min) modulo Step == 0)
```

This rule applies only after `Type` and the placeholder have been shown to represent a numeric scalar. Some parameters encode composite values such as time components and cannot be validated as one scalar range.

## Security and correctness rules

- Never substitute unvalidated text directly into a frame.
- Match complete placeholders, not substrings.
- Reject values containing frame delimiters unless the parameter grammar explicitly requires them.
- Reparse the rendered frame before transmission.
- Validate `WHERE` under the functional `WHO`; `WhereType` alone is not a complete address grammar.
- Treat `ChiOpen` as source evidence, not permission to overwrite a contradictory literal frame.
- Preserve the stored template and rendered result together.
- Do not transmit symbolic or unresolved templates.

## Example

For the stored automation action:

```text
ChiOpen = 2
Frame = *2*1*WHERE##
WherePlaceholder = WHERE
```

and an independently validated `WHO 2` destination `11`, rendering produces:

`*2*1*11##`

The resulting `WHAT 1` and `WHERE 11` semantics must still be read from the [`WHO 2` functional reference](../functional/who-2-automation/). The ScenarioDevices row establishes the template offered by MyHOME_Suite; it does not replace the protocol definition.
