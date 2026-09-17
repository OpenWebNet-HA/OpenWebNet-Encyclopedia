# Parameters

`Parameters` describes additional values needed by a Command or by the scenario editor. A Command has zero, one, or two Parameter rows in the canonical `program-files` revision.

| Parameters per Command | Commands |
| ---: | ---: |
| 0 | 116 |
| 1 | 40 |
| 2 | 1 |

The two-parameter Command is a lighting dimmer action whose shared placeholder encodes both level and transition time.

## Field model

| Field | Established role | Interpretation limit |
| --- | --- | --- |
| `Id` | local row primary key | not stable across databases by declaration |
| `Command_Id` | foreign key to `Commands.Id` | local to one file |
| `Name` | localization/resource key | not necessarily unique |
| `Placeholder` | token or composite pattern used by the command/application | can be `NULL` |
| `Min`, `Max` | stored numeric bounds | meaningful only after type interpretation |
| `Step` | stored increment | not sufficient for composite values |
| `Type` | parameter editor/value-type discriminator | numeric enumeration is not published |
| `OperatorType` | operator/editor discriminator | numeric enumeration is not published |
| `Value` | stored fixed or selector value | role depends on the Parameter context |

## Observed `Type` values

| Type | Rows in `program-files` | Observed contexts | Evidence-based description |
| ---: | ---: | --- | --- |
| `1` | 3 | time and time-range conditions | time-oriented editor/value |
| `2` | 24 | shutter levels, steps, scenario numbers, lighting level | numeric scalar |
| `3` | 4 | Temperature Control setpoints | temperature value with `0.5` step |
| `4` | 3 | time and date | time/date editor/value |
| `5` | 3 | time and days of week | time/weekday editor/value |
| `6` | 2 | dimmer level and transition value sharing `liv*v` | composite dimmer value component |
| `7` | 1 | timed-light `ora*min*sec` | composite duration |
| `8` | 1 | Temperature Control local-control enabling | enumeration or specialized selector; only in `program-files` |
| `9` | 1 | fan-coil speed | enumeration or specialized selector; only in `program-files` |

These descriptions are derived from resource keys and value shapes. Retain the numeric Type in machine-readable output.

## Observed `OperatorType` values

| Operator type | Rows | Observed context |
| ---: | ---: | --- |
| `0` | 38 | ordinary values and action parameters | direct/single-value editor |
| `1` | 1 | lighting dimmer condition with stored `Value=1` | condition-specific operator/value selector |
| `2` | 3 | time-range conditions | range-oriented editor |

The names above are working descriptions, not a published enumeration.

## Scalar validation

For a Parameter proven to be a numeric scalar:

```text
require Min is absent or value >= Min
require Max is absent or value <= Max
if Step is present and non-zero:
    require (value - Min) / Step is integral within numeric tolerance
```

Do not apply that algorithm to composite Types `6` or `7`, or to time/date structures, without first expanding their grammar.

## Composite placeholders

### `liv*v`

Two Parameter rows can target the same placeholder:

- level: `1..100`, step `1`;
- transition/time component: `1..254`, step `1`.

The placeholder contains an internal delimiter and represents a composite encoded field. Rendering must combine the two validated components according to the functional frame grammar; replacing the same token twice is incorrect.

### `ora*min*sec`

This placeholder describes multiple duration components. `Min`, `Max`, and `Step` are absent, so the ScenarioDevices row alone does not define each component's domain.

### `c1c2c3c4`

Temperature setpoint actions use a `3..40` semantic range with step `0.5`, while the placeholder name suggests a fixed encoded representation. The conversion from temperature to the four-character wire field must come from the functional Temperature Control definition or corroborated application behavior.

## Parameters without placeholders

A `NULL` Placeholder can still describe editor state, comparison criteria, time structures, or fixed selections. Such Parameters are not automatically unused and should not be discarded.

## Resolution algorithm

```text
function resolve_parameters(command):
    rows = Parameters for command ordered by Id
    group rows by Placeholder, keeping NULL rows separate

    for group in rows:
        classify Type and OperatorType only from established evidence

        if one scalar row targets one placeholder:
            build scalar domain from Min, Max, Step
        else if several rows target one placeholder:
            require an established composite encoding rule
        else if placeholder is NULL:
            retain as application/editor metadata

        attach stored Value without assuming it is a default

    return typed parameter model plus unresolved semantics
```

## Revision differences

`programdata` lacks Types `8` and `9` because it lacks the local-control and fan-coil-speed Commands and their Parameters. The common Types and rows otherwise substantially overlap, but correspondence should be checked by parent Command and resource key rather than primary key alone.
