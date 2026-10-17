# SCS Configurator Labels

SCS/MyHOME configurators are removable plugs used to assign addresses, select functions and set parameters. A plug's marking, the socket into which it is inserted, and the configured Device's role together determine its meaning. MyHOME Suite exposes software counterparts and additional settings.

This reference distinguishes manufacturer-defined functions from catalogue encodings and simulator behavior. Product sheets determine which combinations are supported; the tables below do not authorize every label in every socket.

## Reference

| Subject | Section |
| --- | --- |
| Lettered and arrow plugs | [Plug vocabulary](#plug-vocabulary) |
| PUL on commands and actuators | [PUL behavior](#pul-behavior) |
| Physical socket names | [Positions and functions](#positions-and-functions) |
| Thermoregulation, Energy and other systems | [System-specific positions](#system-specific-positions) |
| Software settings and numerical encodings | [Configuration modes](#configuration-modes) and [Catalogue encodings](#catalogue-encodings) |

## Plug vocabulary

The manufacturer sells the lettered plugs below, alongside numeric configurators. `3501/T` and `3501/TM` are product references for the arrow plugs, not socket names. See the [BTicino configurator catalogue](https://www.bticino.com/products/smart-home-and-home-automation-systems/home-automation-system-myhome-bus-solutions/common-wiring-devices-interfaces-and-accessories).

| Plug | Literal meaning or manufacturer function name | Function and usual context |
| --- | --- | --- |
| `0..9` | Numeric value | Address digit or parameter selector; the meaning and permitted range depend on the socket and product |
| `AMB` | *Ambiente* - room/environment | Selects a room command, commonly in `A`; the point field then identifies the room |
| `GEN` | *Generale* - general | Selects a general command, commonly in `A`; remaining address fields follow the product's rules |
| `GR` | *Gruppo* - group | Selects a group command, commonly in `A`; distinct from an actuator's numeric group-membership field |
| `AUX` | Auxiliary | Selects auxiliary-channel operation where supported; an `AUX` socket can instead hold the numeric channel |
| `ON` | On | ON-only command when used as a command-mode selector |
| `OFF` | Off | OFF-only lighting command; can instead disable an output or select a product-specific shutter mode |
| `O/I`, `0/1` | OFF/ON | Selects separate OFF and ON operations; button/input assignment and dimming support depend on the product |
| `PUL` | *Pulsante* - pushbutton | Momentary lighting-command mode; actuator use has additional collective-command semantics described below |
| `SLA` | Slave | Selects a follower role; actuator followers and supplementary temperature probes perform different functions |
| `CEN` | CEN / centralized scenario control | In a command-mode socket, enables interactions for a scenario programmer; other sockets have different uses |
| `↑↓` (`3501/T`) | Up/down, bistable control | Starts opening or closing; a subsequent key press stops movement |
| `↑↓M` (`3501/TM`) | Up/down, monostable control | Movement continues while the key is held; release stops movement |

Italian and English product tables establish *ambiente*, *generale*, *gruppo* and *pulsante* directly. `CEN` is retained as the manufacturer's function label rather than assigned an unverified long-form acronym. The functional [CEN](../functional/who-15-cen/) and [CEN+](../functional/who-25-transversal/cen-plus.md) references describe their distinct wire namespaces.

### Command modes

| Mode | Control behavior | Software counterpart |
| --- | --- | --- |
| Cyclic | Successive presses alternate ON/OFF; some point controls also dim on a long press | Cyclic; Cyclical ON/OFF; Cyclical dimmer are separate supported choices |
| `O/I` | Typically upper ON and lower OFF; with adjustment, long upper/lower presses increase/decrease brightness | ON/OFF; ON/OFF with adjustment |
| `PUL` | ON while pressed, OFF on release | Pushbutton |
| Numeric timed mode | Sends a timed operation selected by the product's mode table | ON timed; customised timed ON |
| Arrow modes | Bistable or monostable movement as defined above | Bistable control; Monostable control |

These are command functions, not statements about the mechanical latching of the keys. The [Suite lighting-control help](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/modalita_comando_luce.html) distinguishes cyclic controls with and without adjustment. Its [Automation-control help](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/modalita_comando_automazione.html) distinguishes bistable, monostable and blade-control variants.

On the F428 contact interface, `SPE=0, M=O/I` assigns OFF to `N1` and ON to `N2`; long-pressure regulation is available in the documented point-to-point dimmer mode. `SPE=0, M=PUL` selects pushbutton mode. Up/down modes use `PL1=PL2`. These are F428 combinations, not universal `SPE` values. See the [F428 sheet, pages 2..4](https://dar.bticino.it/asset/Documents/MQ00283_c_IT.pdf).

## PUL behavior

### Lighting command

`PUL` is an established momentary command function: the load is commanded ON while the control is held and OFF when released. The [Voice Control installation and use manual, page 55](https://dar.bticino.it/asset/Documents/RA00168AA_IT.pdf) states this explicitly and distinguishes it from cyclic and timed operation.

An illustrative point command to Lighting address `11` therefore uses ON `*1*1*11##` on press and OFF `*1*0*11##` on release. These examples illustrate the ordinary Lighting vocabulary, not a captured exchange or a guarantee of delivery. `PUL` does not introduce a new `WHO` or `WHAT`.

### Actuator and local control

An actuator's PUL setting must be read in its own mode table. F411U2 and F411/4 sheets define Master PUL and exclusion of Room and General controls. Slave operation follows a Master with the same address; available OFF delays and Slave PUL settings depend on the product and Configuration method. See [F411U2, pages 2..3](https://dar.bticino.com/asset/Documents/ST_00000893_EN.pdf) and [F411/4, pages 2..3](https://dar.bticino.com/asset/Documents/ST_00000896_EN.pdf).

PUL on an actuator does not universally make its local key momentary. The [MHKIT1116 instructions, pages 5..6](https://dar.bticino.it/asset/Documents/LE08838AC.pdf) explicitly describe local ON/OFF cyclic operation with `M1=PUL`, or with `M1=CEN, M2=PUL` in the corresponding two-load mode, while excluding Room and General commands. The command function and the actuator's collective filtering must therefore remain separate.

The same instructions use `M1=CEN` as a selector in the two-load actuator combinations. In their single-load shutter table, `M1=OFF` instead selects up/down with a two-minute stop and Room/General exclusion. Neither plug therefore has one universal effect independent of the selected function.

### Collective commands and status

| Source and scope | PUL collective-command treatment |
| --- | --- |
| Older manufacturer SCS guide, actuator modes, printed page 36 | Explicitly permits point and group ON/OFF; excludes Room and General |
| F411U2 and F411/4 sheets dated 23 March 2021 | State exclusion of Room and General; do not explicitly settle group handling in that PUL description |
| Suite function help, `MHS_function_0304b`, Lighting, Automation, shutter and dimmer actuators | Master PUL and Slave PUL exclude general, group and room controls for the listed products |

The older [manufacturer SCS guide](https://leonardocanducci.org/wiki/tp3/_media/guida_myhome_bticino.pdf) and [Suite actuator help](https://myhomeswupdate.bticino.com/MyHOMESuite_Docs/MHS_function_0304b/EN_MHS_function_0304/attuatore_automazione.html) differ explicitly on groups. The 2021 sheets' omission of groups is not itself a contradiction. The sources do not establish a physical Firmware boundary or prove that selecting Physical versus software Configuration explains the difference.

Room/General exclusion is documented behavior, not merely an inference from a simulator. Group handling requires the applicable product/mode evidence. Status-request responses are a separate question: command filtering alone does not establish whether a Device answers point, group, Room or General status requests. The [F411 simulator model](configuration.md#f411-simulator-configuration) must not settle that hardware question.

## Positions and functions

Socket names identify fields; plug markings identify values. For example, `M=SLA` inserts the Slave plug into the mode socket, whereas a probe's `SLA=3` inserts a numeric plug into the socket marked SLA. Fields without a product-sheet example below are catalogue descriptions from MyHOME Suite 3.5.38; their presence does not prove a physical socket on every associated product.

| Position | Meaning/function | Context |
| --- | --- | --- |
| `A` | *Ambiente*, room/environment or addressing scope | Lighting/Automation controls and actuators; command scope plugs can replace the room digit |
| `PL` | *Punto luce*, lighting point | Point within the addressed room; reused as a target selector for collective controls |
| `A1`, `PL1`; `A2`, `PL2` | Address fields for separate channels/functions | Combined controls and actuators; not always successive digits of one address |
| `PL1..PL4` | Per-output point addresses | Multi-relay Lighting actuators with a shared `A` |
| `G`, `G1..G3` | *Gruppo*, group membership | Actuator participation in one or more groups; number of positions depends on product |
| `M`, `M1`, `M2`, `MOD`, `MODE` | Operating mode | Select function, local control behavior, follower role or a parameter; no global mode-number table |
| `SPE` | Special-function selector | Changes interpretation of the other fields; F428 and special wall-control codes differ |
| `AUX` | Auxiliary channel | Input auxiliary-channel selection on a special control; distinct from `A=AUX` command addressing |
| `I` | Destination interface/bus selector | Supported commands can target another local bus or the riser |
| `Ar`, `PLr` | Reference actuator room and point | Advanced shutter control uses a reference actuator to update status for a collective target |
| `PRE` | Preset | Shutter preset-related setting in the catalogue; it is not the functional `DIMENSION` number |
| `LIV1`, `LIV2`, `LIV1/AUX` | Level or reused parameter fields | Special controls reinterpret them according to `SPE`; timer mode can repurpose them for minutes/seconds |
| `LED`, `INT`, `SET` | Local indication/interface settings | Meaning depends on the control and Firmware definition; not functional ON/OFF state |
| `MIN`, `MIN1`, `MIN2`, `TY` | Minimum dimming level and load type | Dimmer settings; channel suffixes and numeric domains are product-specific |
| `C` | Zero-crossing/load-contact selection | F411U2 `C=0` with zero crossing, `C=1` without; unrelated to `C` in other product families |

The [advanced shutter-control sheet, page 2](https://dar.bticino.com/asset/Documents/MQ00591_c_EN.pdf) defines `Ar`/`PLr` and distinguishes installation level from destination level: for this product, `I=1..9` selects a local bus, `I=CEN` the riser, and `I=0` the complete system. A [special wall-control sheet](https://configuratoren.legrand.nl/documize/2015/10/20151002_111284_1.pdf) instead describes `I=0` as its local line. These product descriptions must not be collapsed into one universal meaning for `I=0`.

The same special-control sheet defines input `AUX` as a channel whose event activates the configured command as though its key were pressed. Its `SPE=ON` timer mode reuses `M`, `LIV1` and `LIV2` for two minute digits and a seconds selector. Socket reuse explains why a field name alone cannot determine a unit or function.

## System-specific positions

### Temperature Control

| Position/value | Meaning/function | Product scope |
| --- | --- | --- |
| `ZA`, `ZB` | Zone-address components | Probes and Temperature Control actuators; matching zone addresses associate them |
| `ZB1..ZB4` | Per-output zone component | Relevant multi-output actuators; `OFF` can exclude an output |
| `N`, `N1`, `N2` | Progressive actuator number within a zone, or pump number | Temperature Control actuator; not a Lighting point or probe Slave index |
| `MOD=SLA` | Supplementary Slave probe | Eligible probe without selector knob |
| `SLA` socket, numeric | Slave count on a Master; progressive Slave number on a Slave | 4692/4693 family in the cited sheet |
| `FUN` | Function selector | Local displays; catalogue meaning requires the selected display definition |
| `TYPE` | System-probe, hotel or residential thermostat role | H4691/LN4691 and variants in the cited sheet |
| `HEAT`, `COOL` | Heating and cooling load type | H4691/LN4691; separate from the current heating/cooling runtime mode |
| `COOL=CEN` | Share the heating load for cooling | H4691/LN4691; actuator `N=1`, with `HEAT` neither `0` nor Fil Pilote `5` |
| `PUMP` | Pump arrangement | H4691/LN4691; selects none, heating, cooling or shared pumps |
| `IN` | External-contact action | H4691/LN4691; selects protection, OFF, ECO, COMFORT or heating/cooling changeover |
| `WARM`, `COLD` | Winter/summer function enablement | Temperature central-unit catalogue definitions; not physical plug labels inferred from the column pattern |

In the [4692-family probe sheet, page 2](https://dar.bticino.com/asset/Documents/MQ00179_c_EN.pdf), a Master averages its reading with those of up to eight Slave probes in the zone. Its numeric `SLA` value gives the number of Slaves; Slave indices start at `1` without gaps. The selector-knob 4692 is Master-only; eligible 4693 probes use `MOD=SLA`. The sheet also notes removal of `P`, `MOD` and `DEL` sockets from the revised selector probe. Older socket layouts must not be assumed for that product revision.

The [F430/2 sheet, pages 2..4](https://dar.bticino.com/asset/Documents/ST_00000902_EN.pdf) shows why `ZA`, `ZB` and `N` must be interpreted together: they support zone-valve, Open/Close and circulation-pump arrangements. The [H4691/LN4691 sheet, page 2](https://dar.bticino.com/asset/Documents/MM00789_b_EN.pdf) provides the thermostat mappings above. With `TYPE=0`, its heating/cooling loads and pumps are configured through the central unit; `HEAT`, `COOL` and `PUMP` are not populated as in standalone thermostat modes.

The `[SLA]` placeholder in diagnostic Slave-probe address rules denotes the probe selector, not the lettered plug's raw code. See [Temperature Control addressing](../functional/who-4-temperature-control/addressing.md) and [Address discovery](../diagnostics/address-discovery.md).

### Energy Management

| Position | Meaning/function | Product scope |
| --- | --- | --- |
| `A1`, `A2`, `A3` | Hundreds, tens and units of an Energy address | Energy products with this address layout; not three Lighting command channels |
| `A3-Ta`, `A3-Tb`, `A3-Tc` | Units for the three meter input addresses, sharing `A1`/`A2` | F520 |
| `T↑` | Toroid-direction handling | F520; unrelated to the up/down control plug `3501/T` |
| `MUL`, `DIV` | Multiplier and divider | 3522N pulse-count scaling |
| `PF` | Power-factor setting | Catalogue Firmware `229`, current-sensing actuator; unrelated to a Sound System's sound-point label |
| `P`, `TOL` | Rated-power and tolerance settings | Load-management central-unit catalogue context; numerical units require that definition |
| `SM`, `G` | Energy pulse-counter selectors | Legacy catalogue Firmware `200`; their short names alone do not establish a scale or unit |

The [F520 sheet, page 2](https://dar.bticino.com/asset/Documents/MQ00358_d_EN.pdf) limits meter addresses to `127`, prohibits zero in `A3-Ta`, and permits zero in `A3-Tb`/`A3-Tc` for unused inputs. Its direction selector `0` measures independently of toroid mounting direction; `1` makes measurement direction-dependent.

The [3522N instructions, page 2](https://assets.legrand.com/pim/NP-FT-GT/LE06852AC.pdf) map `MUL=0..6` to factors `1, 2, 5, 10, 20, 50, 100`, and `DIV=0..7` to divisors `1, 10, 100, 1000, 2, 20, 200, 2000`. The plug number is a selector, not the multiplier/divisor itself. Runtime measurements remain documented under [Energy Management](../functional/who-18-energy-management/).

### Routing, sensors and Alarm

| Position | Meaning/function | Product scope |
| --- | --- | --- |
| `I1..I4`, `MOD` | Interface identity/boundary and operating mode | F422; occupied positions and interpretation change with mode |
| `S`, `T`, `D`, `M` | Movement sensitivity, load timer, daylight threshold and operating mode | BMSE2002 Lighting sensor |
| `Z`, `N°`, `MOD`, `AUX` | Alarm zone, progressive detector number, detection mode and auxiliary channel | 4610-family Alarm detector |

The [F422 sheet](https://dar.bticino.com/asset/Documents/MQ00280_f_EN.pdf) distinguishes physical expansion, logical expansion, public-riser, inter-system and separation modes. `I3`/`I4` must be interpreted in the selected mode, not invariably as the suffix of a local-bus OpenWebNet address. See [Routing and bus selectors](../protocol/addressing.md).

For [BMSE2002, page 3](https://dar.bticino.com/asset/Documents/MM00297_c_EN.pdf), `S=1,2,3` selects medium, high and very high movement sensitivity; no plug selects low. `D=1..5` selects `20,100,300,500,1000` lux. `M=2` reports movement/brightness to a scenario programmer rather than directly managing the load, and leaves `S`/`T` unconfigured. These are sensor settings, not universal `S`, `D` or `M` meanings.

The [4610-family detector sheet, page 2](https://dar.bticino.com/asset/Documents/MQ00035_c_EN.pdf) permits zones `1..8` and progressive detector numbers `1..9`. It also permits the `AUX` plug in `MOD`, where it changes auxiliary-event behavior; the numeric plug in `AUX` selects the channel. This illustrates another use of a lettered plug outside an address socket. These product limits do not define the entire [Alarm](../functional/who-5-alarm/) or [Auxiliaries](../functional/who-9-auxiliaries/) protocol domains.

### Sound, hotel and door-entry systems

| Position | Meaning/function | Product scope |
| --- | --- | --- |
| `A`, `PF` | Room and sound-point address | F503 amplifier; `PF` is the sound point (*punto fonico*) in Sound System terminology |
| `M1`, `M2`, `M3` | Paging volume/mute/follower role; source selection; output-channel assignment | F503 |
| `R1`, `R2` | Room-number tens and units | Hotel indicator and room-status Devices |
| `L`, `M` | LED/occupancy indication and management mode | H4650/LN4650 hotel indicator |
| `DEL1`, `DEL2` | Entry/exit delay | H4648/LN4648 key-card switch; depends on scenario mode |
| `N`, `P`, `M` | Internal-unit number, associated entrance panel and key operating mode | Classe 100 V16B `344652` |
| `A`, `B`, `C`, `M`, `T` | Device address, operating mode and local relay time | `353000` keypad; interpretation depends on stand-alone, entrance-panel or access-control installation |

The [F503 sheet, page 2](https://assets.legrand.com/general/legrand-exp/np-ft-gt/mq00271-c-uk.pdf) assigns `M1=SLA` to amplifier Slave operation. `M2` empty recalls the last source (Follow Me); `M2=1..4` selects a specific source. Its `AUX IN`/`AUX OUT` are analogue audio connectors, not SCS auxiliary configurators or `WHO 9` channels. See [Sound Diffusion](../functional/who-22-sound-diffusion/).

The [hotel-indicator sheet, page 2](https://dar.bticino.com/asset/Documents/MM00774_b_EN.pdf) defines `R1`/`R2`, `L` and `M`. The [RFID key-card switch sheet, page 2](https://dar.bticino.com/asset/Documents/MM00771_a_EN.pdf) distinguishes centralized CEN events from stored-scenario/group operation; `DEL1` and `DEL2` must be empty in its documented centralized mode.

For the [Classe 100 V16B, page 2](https://dar.bticino.com/asset/Documents/ST_00000691_EN.pdf), `P` associates the entrance panel used for idle door-lock release and first camera activation. For the [353000 keypad, page 2](https://assets.legrand.com/pim/NP-FT-GT/ST-00000684-EN.pdf), `A/B/C` form a `000..999` address only in the documented stand-alone configuration; other modes leave positions unused or repurpose them. `T` is a relay-duration selector, not the shutter up/down plug.

## Configuration modes

| Method | Representation | Interpretation |
| --- | --- | --- |
| Physical Configuration | Plugs in supported sockets | Read the product's position/mode table, including unused positions and combined selectors |
| Virtual Configuration | Software values corresponding to supported configurator/function settings | Can offer addresses and parameters unavailable through plugs; capability remains product-specific |
| Advanced Configuration | Firmware-supported Objects, Modules and richer properties | Separate catalogue mode; not a synonym for every software setting |
| Product Programming | Separate catalogue mode | Support and workflow require the selected Firmware definition |

A product sheet may call its Suite settings “virtual configuration” without proving the active catalogue mode for every software operation. The catalogue registers Virtual and Advanced Configuration separately. See [Configuration modes and ownership](configuration.md#physical-configuration-and-configuration-modes).

Software-only fields such as IP addresses, ports, serial identifiers and unique codes can share the firmware-scoped `idx=-1` pattern with physical-position definitions. Their presence does not create physical sockets. Nor does a displayed label prove that a Configuration value was read from plugs rather than programmed in software.

## Catalogue encodings

In the retained MyHOME Suite 3.5.38 catalogue, raw values resolve through the exact Firmware and `EN_CONF` definition. The following are examples of catalogue encodings, not universal OpenWebNet wire codes:

| Firmware definition | Exact field | Raw value | Catalogue label |
| ---: | --- | ---: | --- |
| `145` | `A1` / `A2` | `12`, `13`, `14`, `15` | `GEN`, `GR`, `AMB`, `AUX` |
| `145` | `M1` / `M2` | `9`, `10`, `11` | `O/I`, `OFF`, `ON` |
| `145` | `M1` / `M2` | `12`, `13`, `14`, `15` | `UP/DOWN`, `UP/DOWN monostable`, `CEN`, `PUL` |
| `132` | `M` | `11`, `15` | `SLA`, `PUL` |

Thus raw `11` can mean ON for a control and SLA for an actuator; raw `15` can mean AUX in an address field and PUL in a mode field. The Firmware numbers above are database definition IDs, not reported physical Firmware versions. These rows are verified in the [canonical catalogue](../sources/myhome-suite/3.5.38/databases/).

The catalogue also contains `PLU` instead of `PUL` for raw `15` in Firmware `659` (`MODE`) and `669` (`M`). Preserve those stored tokens when implementing catalogue resolution; a likely spelling irregularity does not prove an application normalization rule. Likewise, the existing `O/I` versus `I/O` conversion-rule question remains open. See [Catalogue Resolution](../internals/catalogue-resolution.md#physical-configuration-resolution).

An empty socket, an explicit numeric zero and an empty catalogue range row are not universally interchangeable. Product instructions sometimes define “no configurator” as a default, but another position may require a digit or use zero to disable a channel. Resolve that equivalence only in the applicable product/definition context.

## Evidence limits

The manufacturer sheets and Suite help establish the named functions and scoped combinations above. Catalogue descriptions supply additional field names and numerical mappings; they do not prove deployed behavior. Historical client tests establish their classification and cache choices, and simulator code establishes its model behavior.

Remaining questions concern PUL group filtering on particular products/Firmware/modes, status-request behavior, deployment applicability, exact catalogue-token normalization and diagnostic position ordering. They do not make the basic manufacturer-defined meanings of PUL, SLA or O/I uncertain. Source fingerprints, candidate claims and the bounded vocabulary disposition are retained in the [Configurator-label review](../project/review/scs-configurator-labels-review.md).
