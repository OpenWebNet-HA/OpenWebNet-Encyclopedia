# Sound Matrix Source Routing

`WHO 16` switches which source an amplifier listens to through a three-digit `WHERE` that no published specification describes. This page records how that address was recovered, what each claim rests on, and where the boundary of the evidence lies. The operational result is on the [`WHO 16` reference](../functional/who-16-sound-system/).

## Why the published specification is insufficient

[`WHO 16`](../sources/openwebnet-public/pdf/WHO_16.pdf) documents amplifier and source power, volume, tone, sleep, Follow Me, tuner frequency, stored stations, and RDS. Its `WHERE` table admits `0`, `#0`-`#9`, `01`-`99`, `100`, and `101`-`109`. It contains no message that assigns a source to an amplifier.

The document does describe a source **cycle** command (`*16*20*100##` / `*16*23*100##`) whose monitor flow emits `WHAT` `0`/`3` for the newly activated source and `10`/`13` for the previous one. Cycling is therefore specified; directed selection is not.

Implementations nonetheless perform directed selection, and the frames they use are the subject of this page.

## The observed address

Two installations emit three-digit `WHERE` values in the `1xx` range that are neither amplifiers (`01`-`99`) nor sources (`101`-`109`):

| `WHERE` | Emitted when |
| --- | --- |
| `111`, `112` | a room listening to source 1, then to source 2 |
| `121`, `122` | a different room, same two sources |
| `131`, `141`, `151`, `161`, `171`, `181` | a general power-on, one frame per room |

The contest is between two readings of the middle and last digits: `1` + source + environment, or `1` + environment + source.

## Discriminating observations

### 1. One amplifier, two sources

Plant B switched amplifier `11` between its two sources and emitted `*16*3*112##` and `*16*3*111##`. The middle digit did not move; the last digit followed the source. Under the competing reading the middle digit would have moved with the source and the last digit would have identified the amplifier's room, which did not happen.

*Evidence class: controlled Device change, scoped to plant B.*

### 2. Eight rooms, one source

Plant B's general power-on emitted `111`, `121`, `131`, `141`, `151`, `161`, `171`, `181` in sequence, each preceded by a `WHO 22` frame addressing a different area. Reading the middle digit as the source would require eight sources on a matrix with four inputs.

*Evidence class: observed traffic, scoped to plant B.*

### 3. The matrix answers for the addressed environment

On plant A, `*16*3*121##` and `*16*3*122##` were each answered with `*#16*23*1*<volume>##`, the volume of amplifier `23`. Amplifier `23` belongs to environment 2, not environment 1 or 3. A routing frame therefore reaches the amplifiers whose **first** address digit equals the frame's middle digit.

*Evidence class: controlled Device change, scoped to plant A.*

### 4. The other dialect writes the fields out

Plant B's gateway announces every `WHO 16` sound event a second time in the [`WHO 22`](../functional/who-22-sound-diffusion/) dialect, which uses separator-delimited fields rather than a packed address:

| `WHO 16` | `WHO 22` counterpart | `WHO 22` fields |
| --- | --- | --- |
| `*16*3*111##` | `*22*2#4#1*5#2#1##` | area `1`, source `1` |
| `*16*3*112##` | `*22*2#4#1*5#2#2##` | area `1`, source `2` |
| `*16*3*121##` | `*22*2#4#2*5#2#1##` | area `2`, source `1` |
| `*16*3*181##` | `*22*2#4#8*5#2#1##` | area `8`, source `1` |
| `*16*3*11##` | `*#22*3#1#1*12*1*4##` | area `1`, point `1` |
| `*16*3*12##` | `*#22*3#1#2*12*1*4##` | area `1`, point `2` |
| `*#16*11*1*17##` | `*#22*3#1#1*1*17##` | area `1`, point `1`, volume `17` |
| `*#16*101*8*…##` | `*#22*5#2#1*10*…##` | source `1`, RDS text |

`WHO 22` carries the area in `WHAT` (`WHAT#MULTIMEDIA_TYPE#AREA`) and the source in `WHERE` (`5#2#SOURCE_ID`). Between the first two rows only the source field changes; between the first and third only the area field changes.

This is the strongest single observation, because it is not an inference about a packed address: the same device states the same fact twice, once packed and once labelled.

*Evidence class: observed traffic on one Device emitting two dialects, scoped to plant B's MH200N firmware.*

## Claim records

### Claim 1: routing address form

| Field | Content |
| --- | --- |
| Claim | In `WHO 16`, a `WHERE` of the form `1ES` with `E` in `1..9` routes the amplifiers of environment `E` to source `S`, using `WHAT` `3` for the stereo channel |
| Source | Plant A (MH200 + F441M) and plant B (MH200N + F441M) captures; `WHO 22` counterpart frames on plant B |
| Revision | Plant A: gateway model MH200. Plant B: gateway model MH200N. Firmware not recorded on either |
| Namespace | `E` is the environment digit shared with amplifier addressing; `S` is the source identifier used by `101`-`109` |
| Conditions | `E` = `0` does not occur: `10S` is a source device address |
| Cardinality | one environment to one source; an environment's amplifiers cannot differ |
| Coverage | environments 1, 2, 3 and 8 observed; sources 1 and 2 observed |
| Supporting evidence | observations 1-4 above |
| Counterevidence | none observed |
| Alternatives | `1` + source + environment, rejected by observations 1, 2 and 4 |
| Confidence | **Corroborated**, from independent evidence classes (controlled change, observed traffic, cross-dialect correspondence) on two Devices |
| Falsifier | a plant in which `1ES` reaches amplifiers whose first address digit differs from `E`, or a `WHO 22` counterpart naming a different area |
| Destination | [`WHO 16` reference](../functional/who-16-sound-system/) |

### Claim 2: amplifier address decomposition

| Field | Content |
| --- | --- |
| Claim | A two-digit `WHO 16` amplifier `WHERE` `EA` decomposes into environment `E` and amplifier `A` within that environment |
| Source | `WHO 22` counterpart frames (`3#AREA#POINT`); F441M product documentation; plant A and plant B captures |
| Revision | as above; product documentation for F441M |
| Namespace | the same `E` used by claim 1 |
| Conditions | single-digit addresses are ambiguous and are treated as their own environment; not observed on either plant |
| Cardinality | one environment to many amplifiers; plant A has three amplifiers in environment 2, plant B two in environment 1 |
| Coverage | `11`, `12`, `21`, `31`, `41` on plant B; `14`, `17`, `18`, `21`, `22`, `23`, `35`, `36` on plant A |
| Supporting evidence | `11` ↔ `3#1#1`, `12` ↔ `3#1#2`, `31` ↔ `3#3#1`; F441M documentation requires amplifiers on output `n` to carry room address `A = n` |
| Counterevidence | none observed |
| Alternatives | a flat two-digit identifier with no internal structure, rejected by the `WHO 22` counterparts |
| Confidence | **Corroborated** |
| Falsifier | an amplifier whose `WHO 22` counterpart names an area other than its first address digit |
| Destination | [`WHO 16` reference](../functional/who-16-sound-system/) |

### Claim 3: dual-dialect emission

| Field | Content |
| --- | --- |
| Claim | One MH200N emits a `WHO 22` counterpart for every `WHO 16` sound event it reports |
| Source | five plant B captures covering amplifier power, volume, source power, routing and RDS |
| Revision | plant B's MH200N; firmware not recorded |
| Coverage | every `WHO 16` frame in those captures has a `WHO 22` neighbour; no unpaired `WHO 16` frame observed |
| Supporting evidence | the correspondence table above |
| Counterevidence | plant A's MH200 emits no `WHO 22` frames at all, so the behaviour is not universal |
| Alternatives | the two dialects originate in different devices on the same bus rather than in the gateway, which these captures do not distinguish |
| Confidence | **Established for that Device**; **Unknown** whether it is a gateway behaviour, a matrix behaviour, or a firmware option |
| Falsifier | an MH200N that emits only one dialect, or a capture locating the second dialect at a different bus device |
| Destination | [`WHO 22` reference](../functional/who-22-sound-diffusion/) |

## What remains unknown

- **Whether directed selection has a specified form.** The captured address may be a documented private mechanism rather than an undocumented one; no published source examined so far contains it.
- **Environment `0` and the `#E` form.** `WHO 16` admits `#0`-`#9` as an environment address for power commands. Whether routing accepts that form, and what `10S` would mean under it, is untested. No capture uses it.
- **Base band.** Every routing frame observed uses `WHAT 3` (stereo channel). Whether base-band installations require `WHAT 0` for the same address is untested.
- **Sources above 4.** `101`-`109` is the specified range; both plants have four-input matrices.
- **Single-digit amplifier addresses.** Admitted by the specification, absent from both plants.

These are recorded in [Open Questions](open-questions.md).

## Related pages

| Subject | Page |
| --- | --- |
| Operational `WHO 16` reference | [`WHO 16` Sound System](../functional/who-16-sound-system/) |
| The dialect used for corroboration | [`WHO 22` Sound Diffusion](../functional/who-22-sound-diffusion/) |
| Evidence classes and confidence vocabulary | [Evidence and Confidence](evidence-and-confidence.md) |
| Capture handling and publication rules | [Capture Analysis](capture-analysis.md) |
