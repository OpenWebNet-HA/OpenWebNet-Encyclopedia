# Catalogue Resolution

`MHCatalogue.db` is the principal product-capability model. It connects marketed Devices and SKUs to shared items, firmware definitions, Modules, Objects, Virgin Objects, configuration definitions, and contextual constraints.

## Principal capability path

| Stage | Principal structure | Result |
| --- | --- | --- |
| Product | `EN_DEVICE` | branded Device record, standard name, and product code/SKU |
| Shared capability | `EN_ITEM` | item shared by one or more Device records |
| System identity | `AS_ITEM_SYSTEM` | catalogue system association and item-level `modobj` |
| Firmware | `EN_FIRMWARE`, `EN_BUILDS` | versioned capability definition |
| Object support | `AS_OBJECT_FIRMWARE` | Objects supported by one firmware |
| Module placement | `EN_SLOTS` | Object alternatives at Device-local `slot` positions |
| Configurable template | Virgin-Object association tables | permitted Object set before final assignment |
| Configuration | `EN_CONF` and related tables | properties, domains, filters, conditions, and conversions |

The conceptual model is **Physical Device → Firmware → Module → Object → Configuration**.

![Catalogue identity and capability model](../assets/diagrams/catalogue-capability.svg)

The diagram shows established catalogue relationships and association tables. It is a capability model: installed Device state still comes from diagnostics or a loaded project.

## Identity resolution

A diagnostic identity response does not return an `EN_DEVICE` primary key. Resolution proceeds through meaning:

1. retain the raw diagnostic Device ID as an installed-instance identifier;
2. correlate `DIMENSION 1.OBJECT_MODEL` with `AS_ITEM_SYSTEM.modobj`;
3. correlate brand and line values with their catalogue model fields;
4. resolve the shared `EN_ITEM`;
5. enumerate candidate `EN_DEVICE` records and product codes;
6. use `EN_DEVICE.name` as the standard MyHOME Suite-facing Device description;
7. use firmware, hardware, UI, and product evidence to narrow the candidate set.

Several SKUs can share one item and firmware capability. Preserve the candidate set unless the evidence identifies one marketed product uniquely.

In the ordinary addressed Device form, `DIMENSION 1.N_CONF` is the second payload value, immediately after `OBJECT_MODEL`, and reports the number of physical configurator positions provided by the Device. This interpretation is corroborated by `OPEN.db`, catalogue configuration definitions, observed responses, and product diagrams; it is not an Object, Virgin Object, form factor, firmware class, or database key. The separate empty-`WHERE` gateway form is not covered by that interpretation: observed MH202 and F454 gateway tuples return `N_CONF = 15`, outside the ordinary `0..12` range, and its exact gateway semantics remain unresolved. See [`DIMENSION 1`: Device Identity](../diagnostics/dim1-device-identity.md#n_conf-and-physical-configurators).

## Firmware and Module resolution

An item can have multiple firmware definitions. Resolve the three-component `V.R.b` identity across `EN_FIRMWARE.firmware_V`, `EN_FIRMWARE.firmware_R`, and `EN_BUILDS.firmware_b`. The installed firmware response and default/localization metadata can narrow the choice, but the exact MyHOME Suite selection algorithm is not present in the canonical corpus.

An explicit component value of `-1` is strongly corroborated as **any or unspecified** for that component: the catalogue contains both `-1.-1.-1` defaults and concrete `V.R.-1` definitions. Preserve this as an inferred wildcard/default semantic, not as a proven precedence algorithm. Do not equate an explicit build of `-1` with the absence of an `EN_BUILDS` row. See [Firmware](../device-model/firmware.md#the--1-sentinel) for the evidence and counts.

Once firmware is resolved, `AS_OBJECT_FIRMWARE` gives supported Objects, `EN_SLOTS.first_slot` places Object alternatives, Virgin-Object associations describe configurable templates, and slot conditions can remove alternatives in a particular configuration.

Do not count `EN_SLOTS` rows as Modules: one `slot` can have several Object alternatives.

## Runtime Module projection

`DIMENSION 30` selects the meaning of `KEYO` through `STATE`:

| `STATE` | `KEYO` namespace | Meaning |
| ---: | --- | --- |
| `0` | `EN_KEY_OBJECT.key_object` | enabled Module; regular configured Object |
| `1` | `EN_VIRGIN_OBJECT.virgin_key_object` | disabled Module; Virgin Object and configurable role |

This is a state-dependent external identifier. The `DIMENSION 30` polarity is established by controlled diagnostic/programming evidence correlated with MyHOME_Suite UI behavior; it is neither `EN_KEY_OBJECT.id_key_object` nor `EN_VIRGIN_OBJECT.id_virgin_key_object`.

Use the same `slot` to attach `DIMENSION 32` address data and `DIMENSION 35` configuration values. Do not renumber protocol slots to match the UI.

## Configuration ownership

`EN_CONF` uses two exclusive ownership patterns:

| Scope | Key pattern |
| --- | --- |
| Object-scoped | resolved `id_key_object`; `id_firmware = 0` |
| Firmware-scoped | `id_key_object = 0`; resolved `id_firmware` |

The zero values are “not applicable” sentinels. Treating both columns as mandatory foreign keys would erase the ownership discriminator.

A complete property dictionary is the union of both scopes in the resolved Object/firmware context. The configuration `idx` is not globally unique; it becomes a meaningful `DIMENSION 35.INDEX` only after Device, firmware, Module, and Object context are known.

## Reconstructed relationships

Many catalogue relationships are not declared as SQLite foreign keys. They are supported by association-table structure, complete parent-key coverage in the canonical revision, consistent use across the capability graph, and diagnostic/UI corroboration.

Document these as reconstructed relationships. Do not alter the canonical database to make them appear declared.

One especially important exclusion is `EN_DEVICE.code`: it is a product code/SKU, not a reference to `EN_LANGUAGE.code`. Column-name similarity is not relational evidence.

## Physical-configuration resolution

Physical configuration is a firmware-contextual catalogue problem. The catalogue does not provide one global table that maps a raw configurator number to a universal meaning, nor does it require a hand-maintained topology table for each firmware.

### Configuration-mode boundary

`EN_CONFIG_MODE` registers four distinct modes in the canonical catalogue:

| `id_config_mode` | Catalogue label | `config_mode` |
| ---: | --- | ---: |
| `1` | Virtual Configuration | `1` |
| `2` | Advanced Configuration | `2` |
| `3` | Physical configuration | `0` |
| `4` | Product Programming | `3` |

`AS_FIRMWARE_CONFIG_MODE` records which catalogue modes a firmware supports. Do not collapse Virtual Configuration and Advanced Configuration into one category merely because both are non-physical.

`OPEN.db` has a separate sequence vocabulary. In particular, `ConfConfigurators` is described as "To set device configurators, virtual configuration", while `ConfKO` is described as advanced configuration. Those labels establish the purpose of the registered programming workflows. They do not establish that sequence labels, catalogue mode records, and MyHOME Suite UI labels are interchangeable concepts.

### Resolver inputs and outputs

The catalogue resolver takes:

- one exact `EN_FIRMWARE.id_firmware`;
- a candidate physical configuration keyed by exact firmware configuration symbols;
- the firmware's Object/slot capability rows;
- the stored slot conditions and conversion rules for those rows.

It should return:

- whether Physical configuration is registered for the firmware;
- the relevant firmware configuration definitions and their legal domains;
- candidate Objects by internal `slot`;
- stored condition branches and whether each is reachable for this firmware;
- the Object selected for each internal `slot`, when selection is unique;
- applicable `EN_CONDITION.id_conv_rule` values and resulting Object-property conversions, where resolvable;
- explicit zero-match, multi-match, unsupported-expression, and unresolved states.

This is catalogue capability resolution. It does not prove that an installed Device is currently using Physical configuration.

### 1. Establish Physical-mode support

Use the explicit firmware-to-mode association:

```sql
SELECT
    cm.id_config_mode,
    cm.descr,
    cm.config_mode
FROM AS_FIRMWARE_CONFIG_MODE AS fm
JOIN EN_CONFIG_MODE AS cm
  ON cm.id_config_mode = fm.id_config_mode
WHERE fm.id_firmware = :firmware_id
ORDER BY cm.id_config_mode;
```

Physical configuration is catalogue-supported when the result contains the distinct `Physical configuration` record. Mode support is a firmware capability, not installed-state evidence.

### 2. Resolve exact configurator definitions and legal domains

Demonstrated physical firmware fields in the canonical catalogue are firmware-scoped `EN_CONF` rows with `idx = -1`, making that structure a useful candidate set. It is not a sufficient physical-position test: the common `AID`/ID row is also firmware-scoped with `idx = -1` but is not a literal physical configurator. For topology resolution, parse the symbols used by explicit physical slot predicates and resolve those symbols to the exact firmware definitions. Treat additional `idx = -1` rows as candidate metadata unless independent canonical evidence establishes their physical role.

Retrieve each definition together with its domain:

```sql
SELECT
    c.id_conf,
    c.conf_name,
    c.descr,
    c.descr_ext,
    c.id_conf_type,
    ct.descr AS conf_type,
    c.id_conf_data_type,
    dt.data_type,
    c.progressive,
    c.idx,
    r.value,
    r.name AS value_name,
    r.descr_ext AS value_description,
    r."default" AS default_value,
    r.min_value,
    r.max_value,
    r.step
FROM EN_CONF AS c
LEFT JOIN EN_CONF_TYPE AS ct
  ON ct.id_conf_type = c.id_conf_type
LEFT JOIN EN_CONF_DATA_TYPE AS dt
  ON dt.id_conf_data_type = c.id_conf_data_type
LEFT JOIN EN_CONF_RANGE AS r
  ON r.id_conf = c.id_conf
WHERE c.id_firmware = :firmware_id
  AND c.id_key_object = 0
  AND c.idx = -1
ORDER BY c.progressive, r.progressive, r.id_conf_range;
```

Interpret a raw physical value only through the exact `EN_CONF.id_conf` selected in the firmware context. Conceptually, the lookup key is:

```text
firmware + exact EN_CONF definition + raw value
```

not:

```text
raw value -> universal configurator meaning
```

The canonical data demonstrates why. In firmware `145`, raw `14` means `AMB` for `A1` and `A2`, but `CEN` for `M1` and `M2`. Raw `15` means `AUX` on those `A` fields and `PUL` on the `M` fields. Elsewhere in the catalogue, raw `14` also appears as `UP/DOWN monostable` for `PL` fields. Numeric equality therefore carries no universal configurator semantics.

### 3. Enumerate Object/slot candidates

`AS_OBJECT_FIRMWARE` supplies Objects supported by the firmware. `EN_SLOTS` places those Object/firmware associations at Device-local `slot` positions:

```sql
SELECT
    s.id_slot,
    s.first_slot,
    s.fixed_ko,
    ofw.id_object_firmware,
    ofw.id_key_object,
    ko.key_object,
    ko.descr AS object_description
FROM AS_OBJECT_FIRMWARE AS ofw
JOIN EN_KEY_OBJECT AS ko
  ON ko.id_key_object = ofw.id_key_object
JOIN EN_SLOTS AS s
  ON s.id_object_firmware = ofw.id_object_firmware
WHERE ofw.id_firmware = :firmware_id
ORDER BY s.first_slot, ko.key_object, s.id_slot;
```

These rows are candidate capability placements. `AS_OBJECT_FIRMWARE.id_key_object` is the database-local key; join `EN_KEY_OBJECT` before presenting the external Object number `key_object`. Several Objects can share one `first_slot`. Do not choose an Object because it appears first, has the lowest identifier, or has `fixed_ko` set.

### 4. Retrieve stored selection branches

Attach the stored slot conditions:

```sql
SELECT
    s.id_slot,
    s.first_slot,
    s.fixed_ko,
    ofw.id_object_firmware,
    ofw.id_key_object,
    ko.key_object,
    ko.descr AS object_description,
    sc.id_condition,
    c.condition,
    c.id_conv_rule
FROM AS_OBJECT_FIRMWARE AS ofw
JOIN EN_KEY_OBJECT AS ko
  ON ko.id_key_object = ofw.id_key_object
JOIN EN_SLOTS AS s
  ON s.id_object_firmware = ofw.id_object_firmware
LEFT JOIN AS_SLOT_CONDITION AS sc
  ON sc.id_slot = s.id_slot
LEFT JOIN EN_CONDITION AS c
  ON c.id_condition = sc.id_condition
WHERE ofw.id_firmware = :firmware_id
ORDER BY s.first_slot, ko.key_object, c.id_condition;
```

A non-empty `EN_CONDITION.condition` is an explicit catalogue predicate associated with an Object/slot candidate. In the canonical data, physical branches commonly use semicolon-separated conjunctions containing `=` and `<>`, for example `M1=CEN;M2=O/I`.

A machine resolver can implement the condition forms actually represented in the source. It must fail closed on syntax it does not understand rather than inventing an interpretation.

Empty condition rows and candidates with no `AS_SLOT_CONDITION` row remain catalogue capability metadata. Their lack of a predicate is not, by itself, an instruction to activate that Object under a physical configuration.

### 5. Apply legal-domain reachability before matching

A stored condition is not automatically a legal physical branch for the selected firmware. Parse every symbol referenced by a condition, resolve it to the exact firmware `EN_CONF` definition, and constrain it by that definition's `EN_CONF_RANGE`.

A branch is unreachable when its predicate has no solution inside the firmware's legal domains. For example, an equality to a symbolic value that the exact firmware definition does not permit is unreachable even if the shared condition row exists in the database.

This filtering is required before topology selection:

```text
stored condition
    -> legal firmware configurator value
    -> reachable physical condition
    -> selected Object/slot topology
```

Keep unreachable rows as provenance. Do not delete or reinterpret them merely because they cannot occur on the firmware currently being resolved.

### 6. Evaluate the candidate physical configuration

Normalize each supplied physical value through its exact `EN_CONF_RANGE` so the resolver retains both raw value and catalogue symbolic meaning. Evaluate every reachable explicit predicate against that normalized configuration.

Group satisfied branches by `EN_SLOTS.first_slot`:

- one distinct satisfied Object candidate: condition-selected Object;
- no satisfied Object candidate: zero-match result;
- more than one distinct satisfied Object candidate: ambiguous result;
- unsupported condition syntax or unresolved symbol: unresolved result.

Do not invent a precedence rule to break ambiguity. Multiple condition rows that select the same Object/slot association are branch evidence for the same candidate, not separate Objects.

### 7. Separate topology selection from property conversion

Topology selection answers:

> Which Object alternative is selected at each `slot` by the physical configuration?

Property conversion is a later operation:

> Given the selected Object and physical/item values, what Object-level configuration values result?

Do not merge these operations.

For each satisfied condition that supplies `EN_CONDITION.id_conv_rule`, retrieve the conversion rows:

```sql
SELECT
    id_conv_rule,
    item_conf,
    item_conf_value,
    object_conf,
    object_conf_value,
    always_true,
    jump_id_conv_rule,
    id
FROM EN_CONV_RULE
WHERE id_conv_rule = :conv_rule_id
ORDER BY id;
```

Apply item-side predicates only in the established physical configuration context, follow `jump_id_conv_rule` according to the stored rule data, and validate any produced Object value against the selected Object's effective domain. If the selected Object/firmware association has `EN_FILTER` and `EN_FILTER_RANGE` rows for the produced property, apply those contextual restrictions after the Object has been selected; they constrain that Object implementation's effective property domain and are not topology-selection edges.

`CONF_SYMBOL_REF` can provide an explicit item-symbol to Object-symbol correspondence for one `key_system` and `slot`:

```sql
SELECT
    item_conf_symbol,
    ko_conf_sysmbol,
    key_system,
    slot,
    descr
FROM CONF_SYMBOL_REF
WHERE item_conf_symbol = :item_symbol
  AND key_system = :key_system
ORDER BY slot, id;
```

The table has no firmware column. Use it only when the system and slot context are independently established. It is not a global symbol-alias table.

### Worked example: firmware `157`

Firmware `157` demonstrates the generic procedure; it is not a firmware-specific rule embedded in the resolver.

The catalogue registers four `slot` positions and associates this firmware with Virtual Configuration, Advanced Configuration, and Physical configuration. Its relevant firmware-scoped physical definitions are:

| Symbol | `progressive` | Legal physical domain |
| --- | ---: | --- |
| `A1` | `1` | `0..9` |
| `PL1` | `2` | `0..9` |
| `M1` | `3` | `0..8`; `9 = O/I`; `10 = OFF`; `12 = UP/DOWN`; `13 = UP/DOWN monostable`; `14 = CEN`; `15 = PUL` |
| `A2` | `4` | `0..9` |
| `PL2` | `5` | `0..9` |
| `M2` | `6` | same stored domain as `M1` |

The firmware also owns `AID` at `progressive = 0`. That is an ID field, not one of the six physical configurator positions above.

Candidate placements include Objects `6`, `7`, `400`, `401`, `404`, and `406` across the four slots. The explicit physical condition rows narrow those candidates.

For the representative physical configuration:

```text
M1=CEN
M2=O/I
```

the matching canonical branches are:

| `slot` | Selected Object | Condition | `id_conv_rule` |
| ---: | ---: | --- | ---: |
| `1` | `6` | `M1=CEN;M2=O/I` | `25` |
| `2` | `6` | `M1=CEN;M2=O/I` | `25` |
| `3` | `400` | `M1=CEN;M2=O/I` | `4` |
| `4` | `400` | `M1=CEN;M2=O/I` | `4` |

The condition-selected topology is therefore `[6, 6, 400, 400]`.

`AS_KO_CMD_KO_DEV` independently associates `key_object_cmd = 400` (`key_object_cmd_desc = Light Double Command`) with `key_object_dev = 6` (`key_object_dev_desc = Actuator Scs Lights`). In the slot capability rows, the corresponding `EN_KEY_OBJECT.key_object` values are described as `Light control` and `Light actuator`. Keep those description fields in their source namespaces. The association is catalogue family evidence; it does not encode a per-instance or per-slot edge such as "slot 1 is hard-linked to slot 3", so no such linkage follows from this example.

The same firmware demonstrates why reachability is mandatory. Its `A2` domain is only `0..9`, while stored slot conditions also contain branches such as `A2=AMB`, `A2=GR`, `A2=GEN`, and `A2=AUX`. Those are stored catalogue conditions but cannot be satisfied by firmware `157`'s legal `A2` domain. Some stored branches also reference an `M2=ON` value that is absent from firmware `157`'s `M2` domain.

The selected branches point to conversion rules `25` and `4`. Preserve those rule IDs and evaluate their rows only after Object selection. Rule `4` has direct matching rows for this candidate configuration: `M1=CEN` produces values `1` and `2` for the two stored `CEN_BUTT` Object-property symbols, while `M2=O/I` produces `M = 9`. The canonical `EN_CONV_RULE.object_conf` strings for the two `CEN_BUTT` rows contain trailing whitespace; preserve the raw strings when implementing exact database matching rather than silently trimming them. This still demonstrates that one physical selector can contribute to more than one resulting Object property.

Rule `25` also belongs to the selected actuator branch, but the canonical data contains a textual irregularity: the physical domain and condition use `O/I`, while the relevant rule-`25` item rows use `I/O`. Do not silently normalize those tokens or claim the corresponding rule-`25` outputs for this input unless canonical evidence establishes equivalence.

### `DIMENSION 4` and `5` are a transport boundary

`OPEN.db` defines:

```text
*#[WHO]*[WHERE]*4*[C1]*[C2]*[C3]*[C4]*[C5]*[C6]##
*#[WHO]*[WHERE]*5*[C7]*[C8]*[C9]*[C10]*[C11]*[C12]##
```

Each `C1..C12` parameter has the transport range `0..255`. The `ConfConfigurators` sequence sends the corresponding `#4` and `#5` programming forms and is described as virtual configuration in `OPEN.db`.

Those are canonical transport facts. `MHCatalogue.db` separately defines firmware-specific symbols, legal domains, conditions, and conversions.

The two databases contain no explicit relation establishing, for every firmware:

```text
DIMENSION 4.C1 = EN_CONF.progressive 1
```

or an equivalent positional rule. `EN_CONF.progressive` can resemble physical ordering in examples, but that resemblance is not a cross-database key. Not every firmware-owned `EN_CONF` definition represents a literal physical plug position. Keep transport position and catalogue configuration definition as separate namespaces until a correlation is independently established.

### `EN_PHY_TO_ADV_TRANS` boundary

The canonical `EN_PHY_TO_ADV_TRANS` table contains only three rows, for firmware IDs `160`, `691`, and `722`. Firmware `157` has no row.

This table is useful evidence for those three recorded cases. It is not the generic physical-to-advanced or physical-to-topology mechanism. The wider catalogue mechanism is represented by firmware-specific `EN_CONF` domains, Object/slot candidates, slot predicates, `EN_CONDITION.id_conv_rule`, `EN_CONV_RULE`, filters, and contextual symbol references.

### Resolution pseudocode

```text
function resolve_physical_configuration(firmware_id, physical_values):
    firmware = require_exact_EN_FIRMWARE(firmware_id)

    modes = load_AS_FIRMWARE_CONFIG_MODE(firmware_id)
    if Physical_configuration not in modes:
        return unsupported_physical_configuration

    definitions = load_firmware_EN_CONF_with_ranges(firmware_id)
    candidates = load_AS_OBJECT_FIRMWARE_and_EN_SLOTS(firmware_id)
    branches = load_AS_SLOT_CONDITION_and_EN_CONDITION(candidates)

    parsed = []
    referenced_symbols = set()
    for branch in branches with nonempty condition:
        ast = parse_supported_condition_grammar(branch.condition)
        if ast is unsupported:
            mark branch unresolved
            continue
        parsed.append(branch, ast)
        referenced_symbols += symbols(ast)

    physical_defs = {}
    for symbol in referenced_symbols union supplied_symbols(physical_values):
        matches = firmware_EN_CONF_definitions_named(definitions, symbol)
        if count(matches) != 1:
            mark symbol unresolved
            continue
        physical_defs[symbol] = matches[0]

    normalized = {}
    for supplied symbol/value:
        definition = require_resolved_definition(physical_defs, symbol)
        normalized[symbol] = decode_with_EN_CONF_RANGE(definition, value)
        if value not in definition.legal_domain:
            return invalid_physical_value

    reachable = []
    for branch, ast in parsed:
        if any referenced symbol is unresolved:
            mark branch unresolved
            continue
        if predicate_has_no_solution(ast, physical_defs):
            mark branch unreachable
            continue
        reachable.append(branch)

    selected = evaluate_reachable_branches(reachable, normalized)

    for internal_slot:
        distinct_objects = selected objects for internal_slot
        if count(distinct_objects) == 0:
            report zero-match
        else if count(distinct_objects) > 1:
            report ambiguous
        else:
            retain selected Object and satisfied condition

    for selected branch with id_conv_rule:
        evaluate EN_CONV_RULE after Object selection
        use CONF_SYMBOL_REF only in matching system/slot context
        revalidate produced Object values

    return topology, converted properties, provenance, and error states
```

The resolver should retain candidate rows, rejected unreachable branches, satisfied predicates, conversion-rule paths, and unresolved expressions as provenance. A successful catalogue result remains capability evidence rather than proof of Device runtime behavior.

For the conceptual model, see [Configuration](../device-model/configuration.md). For installed read-back, see [Diagnostics](../diagnostics/).
