# Addressing

OpenWebNet addressing is system-specific. `WHERE` identifies the destination or source of a frame, but its grammar depends on the selected `WHO` and must not be interpreted as a single universal address type.

## Address interpretation

A parser must resolve `WHO` before interpreting `WHERE`. Different systems can use different address layouts, ranges, hierarchy levels, and advanced-address forms.

Lighting (`WHO 1`) and Automation (`WHO 2`) share the SCS `A`/`PL` address family, but their published `WHERE` tables are not identical. Common point, area, group, and general forms can therefore be described together only where both specifications agree; less common local-bus variants must remain `WHO`-specific.

Other systems, such as Thermoregulation and Energy Management, use different grammars and must not be decoded with the `A`/`PL` rules below.

## Lighting and Automation A/PL grammar

### Common private-riser forms

The published `WHO 1` and `WHO 2` specifications agree on these base forms:

| Scope | `WHERE` syntax | Valid values |
| --- | --- | --- |
| General | `0` | complete system selected by `WHO` |
| Environment / area | `A` | `00`, `1..9`, or `100` |
| Point to point | `APL` | valid combinations listed below |
| Group | `#GR` | `GR = 1..255` |

The labels *environment*, *ambient*, and *area* are used by different sources for the same collective `A` level. The meaning remains scoped to the selected functional `WHO`.

### Point-to-point A/PL

A point address is the concatenation of its `A` and `PL` representations; it is not an arbitrary decimal integer.

| `A` representation | Valid `PL` | Examples |
| --- | --- | --- |
| `1..9` | `1..9` | `11`, `56`, `99` |
| `00` | `01..15` | `0001`, `0015` |
| `10` | `01..15` | `1001`, `1015` |
| `01..09` | `10..15` | `0110`, `0915` |

The ordinary physical-configurator range therefore produces two-digit point addresses such as `56`. Extended values produce four-digit forms such as `0015`, `0311`, or `1014`. A three-digit string is not a valid representation of this grammar: leading zeroes are required to keep the `A`/`PL` boundary unambiguous.

For example, `56` is `A=5, PL=6`; `0311` is `A=03, PL=11`; and `1014` is `A=10, PL=14`. Converting `WHERE` to an integer before parsing would destroy information required to distinguish these forms.

### Collective addresses

`WHERE=0` is the general address and targets the complete functional system selected by `WHO`.

An environment/area address contains only the `A` component. Valid forms are `1..9`, `00`, and `100`. In particular, `100` is the collective address for `A=10`; it is not a point address.

A group address is explicitly marked by `#`: `#1` through `#255`. The prefix is part of the protocol syntax, so a group must not be represented as the bare decimal group number.

## Routing qualifiers

The public specifications and MyHOME Suite implementation data are most coherently represented as a **base address plus an optional routing qualifier**:

~~~text
BASE
BASE#3
BASE#4#INTERFACE
~~~

`BASE` is the functional target: General, Area, Group, or point where that combination is defined by the selected `WHO`. `INTERFACE` is the address of the routing interface. The `Int` label used by the `WHO 1` specification, the `interface` label used by `WHO 2`, and the `I3`/`I4` components used by MyHOME Suite describe the same interface-address concept in their respective notations.

`#3` selects the riser/backbone level. `#4#INTERFACE` selects a local bus reached through the specified interface. These suffixes are therefore routing qualifications of a target address rather than new point-address formats.

### Level 3 / riser

MyHOME Suite's address-rule model contains separate level-rule fields and supports a Level-3/riser qualification layer. A wire form such as `BASE#3`, when established for the selected system and operation, should be retained structurally: the qualifier is not part of `A`, `PL`, or a group number.

The preserved public `WHO 1` table describes unqualified private-riser targets and explicit Level-4 forms; it does not itself enumerate `BASE#3` variants. Level-3 applicability is therefore implementation/address-rule evidence in this corpus, not a published universal Lighting grammar. Do not generate `0#3`, `A#3`, `#GR#3`, or `APL#3` merely from the generalized model without system- and operation-specific evidence.

### Level 4 / local bus

Local-bus addressing is the Level-4 routing form:

~~~text
BASE#4#INTERFACE
~~~

`INTERFACE` is the routing-interface address. The published specifications use different labels for the same field: `Int` in `WHO 1` and `interface` in `WHO 2`; MyHOME Suite represents its components as `I3`/`I4`.

The combined Light/Automation model in MyHOME Suite supports treating this as a shared SCS routing concept rather than two unrelated `WHO`-specific mechanisms. The base target can be General, Area, Group, or point where that scope is applicable:

| Scope | Level-4 `WHERE` form |
| --- | --- |
| General | `0#4#INTERFACE` |
| Area | `A#4#INTERFACE` |
| Group | `#GR#4#INTERFACE` |
| Point to point | `APL#4#INTERFACE` |

#### Interface address components `I3` and `I4`

`INTERFACE` is not merely an integer formatted as two decimal digits. In the SCS configuration model it is formed from the interface configurator positions `I3` and `I4`. For the F422 SCS/SCS interface these positions identify the interface within the installation; in modes that use an A/PL-like interface address, they are assigned with the same structure as the normal `A` and `PL` positions:

~~~text
I3 ≈ A
I4 ≈ PL
INTERFACE = I3I4
~~~

The distinction is historical and structural: `I3` and `I4` are separate SCS configuration positions, not a protocol-level split of an abstract decimal number into tens and units.

Their exact role depends on the operating mode of the interface. In F422 physical-expansion mode (`MOD=1`), `I3` and `I4` define the **separation address** between the two connected bus sections. For example, `I3=3, I4=2` establishes separation address `32`: Automation addresses below that boundary belong on the lower-address side and addresses above it on the higher-address side. In logical-expansion mode (`MOD=2`), the interface address is again assigned using the A/PL method; documentation also permits `I3=0, I4=1..9` to avoid consuming an ordinary `11..99` Automation address.

Consequently, a wire value such as `#4#03` should be preserved structurally as interface address `I3=0, I4=3`, rather than normalized to integer `3`. Leading zeroes can therefore carry address-component information just as they do in extended A/PL addressing.

This configurator-level explanation and the OpenWebNet routing syntax describe different layers of the same concept: `I3`/`I4` define the SCS interface address, while `#4#INTERFACE` uses that address to qualify a functional target as being on the local bus reached through that interface.

The public `WHO 1` material explicitly enumerates all four forms. The public `WHO 2` document shows the point form `APL#4#interface`; this is best understood as an instance of the same routing grammar, not as evidence for a different Automation local-bus mechanism.

The source documents differ in the range they state for the interface field: the Lighting document gives `01..09` and `11..15`, while the Automation document expresses it as `[0-1][1-9]` (`01..09`, `11..19`). This is a source-level constraint discrepancy within the shared concept. Implementations should preserve that discrepancy until Device/interface evidence establishes whether the broader range is universally valid.

Examples include `13#4#03` for point `A=1, PL=3` through interface `03`, and `0311#4#12` for extended point `A=03, PL=11` through interface `12`.

## Parsing rules

An implementation should preserve the raw `WHERE` string and classify it using the grammar for the selected `WHO`. Resolve the functional system first, recognize structural markers such as `#` before numeric conversion, preserve leading zeroes, validate the complete syntactic form and its ranges, and only then expose structured components such as `A`, `PL`, group, or interface.

A syntactically valid address is not necessarily applicable to every Device or Object. Device capabilities, Object family, system rules, and operation-specific restrictions can further constrain which addresses are meaningful.

## Cross-source interpretation

Three source layers contribute different kinds of evidence:

| Source | What it establishes |
| --- | --- |
| Published OpenWebNet `WHO 1` specification | Lighting `WHERE` grammar, including General/Area/Group/point local-bus variants and the Lighting interface range |
| Published OpenWebNet `WHO 2` specification | Automation General/Area/Group/point grammar and its point local-bus/interface rule |
| MyHOME Suite `OPEN.db` | Address-rule templates and applicability used by MyHOME Suite management workflows |

The public functional specifications are authoritative for functional `WHO 1`/`WHO 2` wire syntax. `OPEN.db` is complementary implementation evidence: `EN_ADDRESS_RULE` and `AS_SYSTEM_ADDRESS_RULE` show that MyHOME Suite selects address rules by system and, for some rules, by Object/Device family.

For the combined Light/Automation system, `OPEN.db` records a general virtual form `[A][PL]` with advanced form `[A][PL]+`, plus F422 logic/physical-extension forms `[I3][I4]` and `[I3][I4]+`. Together with the separate `level_2_rule` and `level_4_rule` fields, this supports modeling advanced addressing as qualification/routing layered onto a base address. The `+` notation belongs to the database's address-rule vocabulary; it should not be emitted literally as part of an OpenWebNet `WHERE`, and it does not by itself establish which qualifier combinations are legal for a particular functional `WHO`.

The database also contains `validity_rule`, `object_device_family`, `level_2_rule`, `level_4_rule`, and `offset_adv`. These fields are evidence that syntactic range validation alone is insufficient for every managed Object. Where an address rule is family-qualified, its `object_device_family` correlates with the catalogue Object-family model; applicability should be resolved before encoding a Device-specific management address.

## Other WHO families

The `A`/`PL` grammar above must not be treated as a global OpenWebNet address grammar. MyHOME Suite itself records different address-rule structures for other managed families, including Thermoregulation, Video Door Entry, Energy Management, Access Control, and interface systems.

Their canonical functional `WHERE` syntax belongs in the relevant `WHO` documentation. The common rule is only that `WHERE` is parsed in the context of `WHO`, not that all systems share a common numeric address space.

See the relevant functional `WHO` addressing page for system-specific applicability, [Frame Syntax](frame-syntax.md) for the position of `WHERE` in OpenWebNet frames, and [MyHOME Suite OPEN.db Coverage](../functional/open-db-coverage.md) for the implementation address-rule inventory.
