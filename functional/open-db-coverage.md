# MyHOME_Suite `OPEN.db` Coverage

The MyHOME_Suite `OPEN.db` database provides two different kinds of evidence for functional protocol systems:

1. `EN_SYSTEM` records the system name, functional `WHO`, diagnostic `WHO`, and whether MyHOME_Suite marks the system as managed.
2. `EN_OPEN` together with `AS_OPEN_SYSTEM` records concrete frame templates for a smaller subset of systems. Most of these templates are diagnostic, configuration, calibration, scenario-programming, or service operations rather than ordinary functional `WHAT` commands.

The distinction is important. A system row establishes that MyHOME_Suite knows the namespace; it does not imply that `OPEN.db` contains its complete functional command vocabulary.

## Functional namespace registry

| `WHO` | MyHOME_Suite system | `EN_SYSTEM.id_system` | Diagnostic `WHO` | `managed` | `EN_OPEN` associations | What `OPEN.db` establishes |
| ---: | --- | ---: | ---: | ---: | ---: | --- |
| `0` | Scenarios | `30` | — | `0` | `0` | Namespace and system identity |
| `1` | Light and Automation system | `1` | `1001` | `1` | `65` | Shared Lighting/Automation diagnostic and programming model |
| `1` | Interface AUTOM L3 | `10` | `1001` | `1` | shared | Automation interface level and F422 addressing support |
| `1` | Interface AUTOM L4 | `11` | `1001` | `1` | shared | Automation interface level and F422 addressing support |
| `3` | Load Management system | `7` | — | `0` | `0` | Namespace and system identity |
| `4` | Thermoregulation | `2` | `1004` | `1` | `46` | Diagnostic/configuration workflow plus thermoregulation-specific scan and address rules |
| `5` | Alarms | `3` | — | `0` | `0` | Namespace and system identity |
| `5` | Interface AI L3 | `12` | — | `0` | `0` | Alarm-interface system variant |
| `6` | Interface Multimedia L2 | `13` | — | `0` | `0` | Multimedia interface system variant |
| `6` | Basic Video door entry system | `32` | — | `0` | `0` | Namespace and system identity |
| `7` | Multimedia | `42` | — | `0` | `0` | Namespace and system identity |
| `8` | Video Door entry system and telephony | `5` | `1008` | `1` | `1` | Managed diagnostic family and service-identification operation association |
| `9` | Auxiliaries | `6` | — | `0` | `0` | Namespace and system identity |
| `10` | Navigation command | `33` | — | `0` | `0` | Namespace and system identity |
| `11` | Energy distribution | `34` | — | `0` | `0` | Namespace and system identity |
| `12` | Messages | `39` | — | `0` | `0` | Namespace and system identity |
| `13` | Integration Functions | `26` | `1013` | `1` | `0` | Managed functional/diagnostic family and F422 interface address rules |
| `14` | Special commands | `35` | — | `0` | `0` | Namespace and system identity |
| `15` | Home automation main unit command | `36` | — | `0` | `0` | Namespace and system identity |
| `16` | Sound system | `4` | — | `0` | `0` | Namespace and system identity |
| `17` | Home automation main unit management | `37` | — | `0` | `0` | Namespace and system identity |
| `18` | Energy Management system | `20` | `1018` | `1` | `65` | Shared managed diagnostic/programming model and energy-specific address rules |
| `19` | Interface | `40` | — | `0` | `0` | Namespace and system identity |
| `22` | Multimedia System | `41` | `1022` | `0` | `0` | Functional namespace plus a diagnostic-family identifier |
| `23` | Access Control | `8` | `1023` | `1` | `65` | Shared managed diagnostic/programming model and Access Control address rules |
| `24` | Lighting Management system | `23` | — | `0` | `0` | Namespace and system identity |
| `25` | Transversal Command | `24` | — | `0` | `0` | Namespace and system identity |
| `26` | UPnP Multimedia Command | `25` | — | `0` | `0` | Namespace and system identity |
| `27` | Nurse Call basic level system | `38` | `1027` | `0` | `9` | Authentication/service identity and general diagnostic operations |
| `99` | Service Identification | `31` | — | `0` | `0` | Namespace and system identity |

`WHO 2` is intentionally absent as a separate `EN_SYSTEM` row: MyHOME_Suite groups Lighting and Automation in `id_system = 1`, whose functional `WHO` field is `1` and whose diagnostic family is `1001`. This database representation must not be interpreted as eliminating functional `WHO 2`; the functional protocol still uses `WHO 2` for Automation.

## Systems with concrete `EN_OPEN` templates

### `WHO 1` / diagnostic `WHO 1001`

The `Light and Automation system` is associated with 65 `EN_OPEN` records. The set defines the common managed-device workflow used by Lighting/Automation devices: identity (`DIMENSION 1`, `2`, `3`, `6`, `13`), physical configurators (`DIMENSION 4` and `5`), diagnostic masks (`7`, `8`), Module/Object discovery (`30`, `32`), configuration parameters (`35`, `38`, `39`, `310`), configuration lifecycle, discovery by address or Device ID, and scenario-programming operations.

`OPEN.db` therefore provides substantial evidence about the MyHOME_Suite management plane for Lighting and Automation, but it is not the source of the ordinary `WHO 1` and `WHO 2` functional command tables.

The system-level address rules include normal Light/Automation A/PL addressing and the F422 logic/physical-extension form:

| Rule | Virtual form | Advanced form |
| --- | --- | --- |
| General Light/Automation | `[A][PL]` | `[A][PL]+` |
| F422 logic/physical extension | `[I3][I4]` | `[I3][I4]+` |

### `WHO 4` / diagnostic `WHO 1004`

Thermoregulation is associated with 46 `EN_OPEN` records. It shares the core identity, configuration, Module/Object, diagnostic, and error frames, and adds a thermoregulation-specific scan operation `*#[WHO]*00[ZAZB]*1##`.

`OPEN.db` defines several thermoregulation address classes:

| Target class | Virtual form | Advanced form |
| --- | --- | --- |
| General | `[ZA][ZB]` | `[ZAZB]` |
| Four-zone control unit | `#0#[ZA][ZB]` | `#0#[ZAZB]` |
| Actuator | `[ZA][ZB]#[N]` | `[ZAZB]#[N]` |
| Slave probe | `[SLA][ZA][ZB]` | `[SLA][ZAZB]` |
| External probe | `[PL_N]00` | `[PL_N]00` |

This is stronger implementation evidence than merely knowing that `WHO 4` exists: it establishes the target classes MyHOME_Suite itself distinguishes when constructing management traffic.

### `WHO 8` / diagnostic `WHO 1008`

Video Door Entry and telephony is marked `managed = 1` and assigned diagnostic `WHO 1008`. Its system-level address rule is the F422 public-riser-interface form `1[I1][I2][I3][I4]`, with advanced form `1[I1I2I3I4]`.

The only direct `AS_OPEN_SYSTEM` association is `EN_OPEN.id_open = 59`, labelled `cmd_ident`, with template `*[WHO]*[WHAT]##` and description "programmer send open identification code for the service". Because the frame is parameterized and the database does not enumerate its `WHAT` semantics here, this association establishes a service-identification operation for the system but not a complete `WHO 8` functional vocabulary.

### `WHO 13` / diagnostic `WHO 1013`

`Integration Functions` is marked `managed = 1` and assigned diagnostic `WHO 1013`. No `EN_OPEN` operation is directly associated with the system, but `AS_SYSTEM_ADDRESS_RULE` provides two concrete F422 interface modes:

| F422 mode | Virtual form | Advanced form |
| --- | --- | --- |
| Burglar alarm interface | `[I4]` | `[I4]` |
| Galvanic separation / New physical separation | `[I4]` | `[I4]` |

This shows that the MyHOME_Suite `WHO 13` model is not limited to IP-gateway clock/network information. The implementation data also treats `WHO 13` as the Integration Functions namespace used with F422 interface modes. The public Gateway API and this integration/interface role should therefore be documented as complementary capabilities of the same functional namespace rather than collapsed into transport/session behavior.

### `WHO 18` / diagnostic `WHO 1018`

Energy Management is marked `managed = 1`, uses diagnostic `WHO 1018`, and is associated with the same 65-record managed-device operation set as Lighting/Automation and Access Control. This means MyHOME_Suite supports the common Device → Module → Object → Configuration management model for this family in addition to the functional energy `DIMENSION` operations.

The database defines two Energy Management address classes:

| Target class | Virtual form | Advanced form |
| --- | --- | --- |
| Control unit / measurement target | `5[A1][A2][A3]` | `5[A123]` |
| Actuator | `7[P1][P2]#0` | `7[P]#[PHASE]` |

The functional `WHO 18` reference should preserve the distinction between these implementation address rules and the higher-level meter/actuator `WHERE` forms documented by the public protocol.

### `WHO 23` / diagnostic `WHO 1023`

Access Control is marked `managed = 1`, uses diagnostic `WHO 1023`, and is associated with the same 65-record managed-device operation set. The database therefore establishes that Access Control devices participate in the same identity, discovery, Module/Object, configuration, error, and scenario-programming infrastructure where applicable.

Two Access Control address classes are explicit:

| Target class | Virtual form | Advanced form |
| --- | --- | --- |
| Command or virgin Device | `20` | `20` |
| Indicators | `7[R1][R2]` | `7[R1R2]` |

The labels come directly from the MyHOME_Suite `EN_ADDRESS_RULE` definitions. They should not be generalized into additional Access Control semantics without corroborating evidence.

### `WHO 27` / diagnostic `WHO 1027`

Nurse Call is unusual. `EN_SYSTEM` assigns functional `WHO 27` and diagnostic `WHO 1027`, but `managed` is `0`. Nevertheless, nine concrete `EN_OPEN` records are associated with the system:

| Operation | Frame template | Database description |
| --- | --- | --- |
| Password challenge operations | `*#[OPERATIONS]##` | Device returns logic operations to apply to the password |
| Password result | `*#[RESULT]##` | Programmer sends password result |
| General diagnostic request | `*#[WHO]**7##` | Request general diagnostic A |
| Diagnostic mask response | `*#[WHO]**7*[BIT]##` | Device returns diagnostic mask |
| Automatic diagnostic event | `*#[WHO]**11*[BIT]##` | Hardware/software problem mask |
| WebServer model request | `*#[WHO]**15##` | Request WebServer model |
| MAC request | `*#[WHO]**12##` | Request MAC address |
| WebServer model response | `*#[WHO]**15*[OBJECT_MODEL]##` | Device returns WebServer object model |
| MAC response | `*#[WHO]**12*[MAC1]*[MAC2]*[MAC3]*[MAC4]*[MAC5]*[MAC6]##` | Device returns MAC address |

These records establish a concrete Nurse Call service/diagnostic surface even though `OPEN.db` does not provide the ordinary Nurse Call functional command vocabulary.

## Namespaces represented only by `EN_SYSTEM`

For `WHO 0`, `3`, `5`, `6`, `7`, `9`, `10`, `11`, `12`, `14`, `15`, `16`, `17`, `19`, `22`, `24`, `25`, `26`, and `99`, `OPEN.db` supplies a functional system identity but no direct `AS_OPEN_SYSTEM` → `EN_OPEN` operation association. This is still useful evidence: it confirms the namespace name used by MyHOME_Suite and, in some cases, an interface variant or diagnostic-family assignment. It does **not** establish undocumented `WHAT`, `WHERE`, or `DIMENSION` values.

Notable additional rows are `Interface AI L3` under `WHO 5`, `Interface Multimedia L2` under `WHO 6`, and `Multimedia System` under `WHO 22` with diagnostic `WHO 1022`. These rows show that the database distinguishes interface/system variants even where it does not provide their functional frame vocabulary.

## Interpretation rule

Use `OPEN.db` evidence at the narrowest level it actually establishes:

- `EN_SYSTEM` → namespace/system identity and diagnostic-family association.
- `AS_SYSTEM_ADDRESS_RULE` + `EN_ADDRESS_RULE` → address grammar used by MyHOME_Suite for that system.
- `AS_OPEN_SYSTEM` + `EN_OPEN` → concrete frame template associated with that system.
- `AS_OPEN_PARAM` + `EN_OPEN_PARAM` → parameter layout and constraints for a concrete operation.
- `AS_OPEN_SEQUENCE`, `EN_SEQUENCE`, and timeout tables → workflow ordering and state-machine behavior.

Absence of an `EN_OPEN` association is not evidence that a functional command does not exist. Conversely, a generic parameterized `EN_OPEN` template is not evidence for a particular semantic value until its parameters or another source establish that value.