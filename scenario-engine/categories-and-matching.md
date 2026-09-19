# Categories and Matching

This page documents how ScenarioDevices rows classify scenario roles and correlate related trigger, condition, and action capabilities.

## `CategoryFlag`

In `ScenarioDevices-program-files.sqlite`, the observed distribution is:

| `CategoryFlag` | Object Systems | Resource-key evidence | Working interpretation |
| ---: | ---: | --- | --- |
| `0` | 8 | `.trigger`, `.start` | first event/trigger role |
| `1` | 8 | `.trigger`, `.stop` | complementary event/trigger role |
| `2` | 5 | `.condition`, `.if` | condition role |
| `3` | 8 | `.action` | action role |

The `programdata` revision has the same five condition and eight action systems, but only seven systems for each of flags `0` and `1` because it lacks the Virtual Key Card family.

The role correlation is exhaustive across the canonical resource keys, so the numeric classification is strong implementation evidence. The precise distinction between flags `0` and `1` is not uniform enough to rename them globally: Alarm, Auxiliaries, Hotel, Lighting, Scheduled Scenarios, Time, and Virtual Key Card reuse the same `.trigger` key for both, while Temperature Control uses `.start` and `.stop`.

Documentation should therefore retain both the raw flag and a contextual role:

- flag `0`: primary/start event category;
- flag `1`: complementary/stop event category;
- flag `2`: condition category;
- flag `3`: action category.

Do not describe flags `0` and `1` as particular wire states without resolving the contained Commands.

## Duplicate Object Systems

Several Object System resource keys deliberately occur twice with flags `0` and `1`. They are separate rows and have separate Device Objects and Commands even where their names are identical.

The rows preserve distinct categories. Their use to place related events in the scenario editor is inferred from the metadata; actual editor behavior is not established by the duplicate names alone.

## Object matching

`ObjectMatchingId` is `NULL` for most Device Objects. Non-null values occur in three semantic groups:

| Matching ID | Related Object concepts | Rows |
| ---: | --- | ---: |
| `1` | Lighting Light trigger/action | 3 |
| `2` | Lighting Dimmer trigger/action | 3 |
| `13` | Hotel Room trigger/action | 3 |

The three rows per group span the two event categories and the action category. This strongly supports the interpretation that `ObjectMatchingId` correlates compatible concepts across scenario roles.

It does not prove a relationship with `MHCatalogue.db`, and the matching ID is not a Device Object primary key.

## Command matching

Non-null `CommandMatchingId` values likewise correlate cross-role semantics:

| Matching IDs | Area | Evidence |
| --- | --- | --- |
| `1`, `2` | Lighting Light | off/on trigger rows and off/on action rows |
| `3`, `4` | Lighting Dimmer | off/on trigger rows and dimmer off/on action rows |
| `56..59` | Hotel Room | DND and MUR trigger/action concepts |

For Light commands, `CommandId` and `CommandMatchingId` can be equal. For Dimmer and Hotel actions they differ. Therefore:

- `CommandId` identifies the command within the ScenarioDevices command namespace;
- `CommandMatchingId` links a semantic event/action concept across roles;
- equality between them is incidental for some rows, not a general rule.

## Relationship inspection

The following relationship query is useful because it shows the parent roles on both sides of a matching group:

```sql
SELECT
    d.ObjectMatchingId,
    c.CommandMatchingId,
    os.CategoryFlag,
    os.Name AS system_name,
    d.ObjectId,
    d.Name AS object_name,
    c.CommandId,
    c.Name AS command_name,
    c.Frame
FROM ObjectSystems AS os
JOIN DeviceObjects AS d ON d.ObjectSystem_Id = os.Id
JOIN Commands AS c ON c.DeviceObject_Id = d.Id
WHERE d.ObjectMatchingId IS NOT NULL
   OR c.CommandMatchingId IS NOT NULL
ORDER BY d.ObjectMatchingId, c.CommandMatchingId, os.CategoryFlag;
```

## Matching algorithm

The following is a proposed inspection algorithm for finding metadata counterparts, not recovered MyHOME Suite code or an established runtime matching contract. The preference for equal `ObjectMatchingId` is an analysis policy.

```text
function find_semantic_counterparts(source_command):
    require source_command has CommandMatchingId

    candidates = Commands with the same CommandMatchingId
    candidates = candidates joined to their Device Object and Object System

    if source Device Object has ObjectMatchingId:
        prefer candidates whose Device Object has the same ObjectMatchingId

    group by CategoryFlag and preserve all rows
    return trigger/condition/action counterparts with frames and provenance
```

Matching can support editor navigation or trigger/action correlation. It does not by itself define runtime execution, event subscription, or a reversible wire mapping.
