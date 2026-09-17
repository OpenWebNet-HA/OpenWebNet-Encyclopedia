# Capability Coverage

This page summarizes the capabilities present in `ScenarioDevices-program-files.sqlite`, the larger canonical revision. Counts are descriptive of this source, not protocol limits.

## Coverage by family and category

| Family | Category | Device Objects | Commands | Parameters | Commands with non-null `Frame` |
| --- | --- | ---: | ---: | ---: | ---: |
| Alarm | primary event | 1 | 3 | 0 | 0 |
| Alarm | complementary event | 1 | 3 | 0 | 0 |
| Alarm | action | 1 | 1 | 0 | 1 |
| Automation | action | 7 | 23 | 6 | 23 |
| Auxiliaries | primary event | 1 | 2 | 0 | 0 |
| Auxiliaries | complementary event | 1 | 2 | 0 | 0 |
| Auxiliaries | condition | 1 | 2 | 0 | 0 |
| Delay | action | 1 | 1 | 0 | 0 |
| Hotel | primary event | 2 | 12 | 0 | 0 |
| Hotel | complementary event | 2 | 12 | 0 | 0 |
| Hotel | condition | 1 | 11 | 0 | 0 |
| Hotel | action | 1 | 4 | 0 | 4 |
| Lighting | primary event | 2 | 4 | 0 | 0 |
| Lighting | complementary event | 2 | 4 | 0 | 0 |
| Lighting | condition | 2 | 4 | 1 | 0 |
| Lighting | action | 3 | 12 | 3 | 12 |
| Scenarios | action | 1 | 1 | 1 | 1 |
| Scheduled Scenarios | primary event | 2 | 8 | 8 | 0 |
| Scheduled Scenarios | complementary event | 2 | 8 | 8 | 0 |
| Special Commands | action | 1 | 2 | 0 | 2 |
| Temperature Control | start event | 1 | 2 | 0 | 0 |
| Temperature Control | stop event | 1 | 2 | 0 | 0 |
| Temperature Control | condition | 1 | 2 | 0 | 0 |
| Temperature Control | action | 1 | 19 | 6 | 19 |
| Time | primary event | 1 | 3 | 3 | 0 |
| Time | complementary event | 1 | 3 | 3 | 0 |
| Time | condition | 1 | 3 | 3 | 0 |
| Virtual Key Card | primary event | 1 | 2 | 0 | 0 |
| Virtual Key Card | complementary event | 1 | 2 | 0 | 0 |

Repeated resource keys across primary and complementary event categories are counted as separate scenario roles.

## Frame coverage

| Frame classification | Commands |
| --- | ---: |
| `NULL` | 95 |
| literal OpenWebNet-shaped template | 57 |
| non-null symbolic text | 5 |

Most event and condition rows have no stored frame, while action rows more often contain literal or symbolic rendering data. This asymmetry suggests that incoming event matching is not represented solely by `Commands.Frame`.

## Stored functional `WHO` evidence

| `ChiOpen` | Commands | Functional area indicated by literal frames |
| --- | ---: | --- |
| `NULL` | 99 | events, conditions, delays, symbolic operations, and other rows |
| `0` | 1 | Scenarios |
| `1` | 17 | Lighting |
| `2` | 19 | Automation; one delay row also stores `2` without a frame |
| `4` | 19 | Temperature Control |
| `14` | 2 | Special Commands |

`ChiOpen` aligns with the literal frame `WHO` for established OpenWebNet templates. A non-null value without a literal frame is evidence of intended functional context, not by itself a renderable command.

## Address-type distribution

| `WhereType` | Commands | Observed contexts |
| ---: | ---: | --- |
| `0` | 58 | many frame-absent events and conditions |
| `1` | 59 | Alarm symbolic action, Lighting and Automation actions, other point-address-like templates |
| `2` | 25 | Temperature Control and related zone-address templates |
| `3` | 6 | Auxiliary contact events/conditions |
| `4` | 8 | CEN+ scheduled-scenario events |
| `5` | 1 | Delay action |

The contexts are not sufficient to define a universal address grammar for each numeric type. Use the functional `WHO` and the command template.

## Revision delta

`ScenarioDevices-program-files.sqlite` adds the following resource-key capabilities absent from `programdata`:

- two Virtual Key Card Object Systems;
- two Virtual Key Card Device Objects;
- four Virtual Key Card event Commands across the two event categories;
- Temperature Control local-control action and Parameter;
- Temperature Control fan-coil-speed action and Parameter.

That accounts for the source-count delta:

| Entity | `program-files` | `programdata` | Difference |
| --- | ---: | ---: | ---: |
| Object Systems | 29 | 27 | +2 |
| Device Objects | 44 | 42 | +2 |
| Commands | 157 | 151 | +6 |
| Parameters | 42 | 40 | +2 |

## Scope limits

The coverage table does not establish:

- which capabilities a particular installed Device exposes;
- how a user-authored scenario graph is persisted;
- how frame-absent events are matched at runtime;
- whether every stored action is supported by every gateway;
- whether `program-files` supersedes `programdata`.

Those questions require Device Model, application, runtime, or additional persistence evidence.
