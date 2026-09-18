# Open Questions

These questions require evidence not currently present in the canonical databases and published documentation.

## Diagnostic and programming fields

### `DIMENSION 1` VALUE 2

Observed values do not establish whether this field represents a hardware class, platform, form factor, or another implementation property. It must remain unlabeled until a stable database or product correlation is found.

### `DIMENSION 32.SYS`

`MHCatalogue.db.EN_SYSTEM.sys_modobj` is the leading candidate. A non-Lighting capture is required to distinguish it from database system IDs and functional `WHO` values.

### `DIMENSION 4` and `5`

The twelve reported/programmed values are related to configurator transfer, but their exact representation remains unresolved. In particular, the hypothesis that the two frames indicate presence or contents for physical positions `1`–`6` and `7`–`12` needs controlled captures.

### `DIMENSION 310`

The value has no generic configuration index or parameter metadata in `OPEN.db`. Its meaning must be resolved per Object and Device family.

## Address selection

- How does MyHOME Suite select among multiple address rules after system and Object-family filtering?
- What role do `validity_rule`, `level_2_rule`, `level_4_rule`, and `offset_adv` play in the final encoder?
- Does `DIMENSION 32.SYS` always correspond to one catalogue `sys_modobj`, including Objects assigned to several systems?
- Under which layouts does the diagnostic outer `WHERE` follow internal slot `1`?

## Catalogue behavior

- What exact algorithm selects one firmware definition when version, build, and default metadata overlap?
- Which `fixed_ko`, visibility, condition, and product rules determine whether the UI permits Object replacement?
- Can physical-to-advanced mappings be reconstructed systematically beyond the three firmware definitions represented in `EN_PHY_TO_ADV_TRANS`?
- Does `N_CONF` equal a reproducible count of applicable physical firmware fields across the whole catalogue?

## Scenario Engine

- Which ScenarioDevices source copy does MyHOME Suite load or prioritize?
- Where are user-authored scenario graphs stored?
- How are frame-absent triggers and conditions connected to runtime events?
- What exact enumerations define `CategoryFlag`, `WhereType`, Parameter `Type`, and `OperatorType`?
- What runtime purpose do `ObjectMatchingId` and `CommandMatchingId` serve?

## Application internals

- When and how are the databases opened, cached, refreshed, or migrated?
- Which application components execute the queries in `OpenQuery.txt`?
- Is the bitwise expression in `systemaddressruleDictQuery` intentional and consumed?
- Where are localization resources and fallback rules implemented?

## Evidence priorities

The highest-value next observations are:

1. one successful Thermoregulation, Energy Management, Access Control, or Integration `DIMENSION 32` response;
2. controlled `DIMENSION 4`/`5` captures across known physical configurator changes;
3. file-access and save-operation traces while creating one minimal scenario;
4. product documentation and captures for additional non-six-position `N_CONF` Devices;
5. a controlled Device/firmware case with several catalogue firmware candidates.

Each result should update the [Relationship Register](relationship-register.md) and then the appropriate reference section.
