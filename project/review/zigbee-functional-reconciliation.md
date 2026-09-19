# ZigBee Functional Reconciliation - Step 1

This review records the source-bounded reconciliation of the ZigBee OpenWebNet version 4.0 functional variants for `WHO 1`, `WHO 2`, `WHO 4`, and `WHO 18`.

The review is governed by the [Encyclopedia Core Values](../encyclopedia-core-values.md) and [Encyclopedia Style Guide](../encyclopedia-style-guide.md). It is intentionally limited to Step 1 of the remaining ZigBee completeness work and does not adjudicate `WHO 1000` discovery beyond cross-references needed to interpret these functional sections.

## Evidence basis and applicability

Primary source: `sources/openwebnet-public/pdf/OpenWebNet_Zigbee.pdf`, ZigBee OpenWebNet version 4.0, 22 November 2016.

The inspected source carries Confidential footers and its public-release provenance remains unresolved. Claims from it are therefore described as **specification evidence**, not as independently established public-protocol or interoperability evidence.

Current `zigbee-reconciliation` documentation derived from the reviewed `main` baseline is authoritative for the existing SCS-oriented encyclopedia. Numeric equality across variants is not treated as semantic identity.

The historical `zigbee-documentation` branch is not used as authority for any promoted claim.

## `WHO 1` - Lighting

| Source location | Item | Existing encyclopedia state | Adjudication | Canonical result |
| --- | --- | --- | --- | --- |
| pp. 22-29, sections 8.2-8.3.6 | `WHAT 0`, `1`, `2..18`, speed forms | SCS command meanings already documented | Same semantic operation where source meanings agree; ZigBee address/transport applicability differs | [ZigBee Lighting Variant](../../functional/who-1-lighting/zigbee-variant.md) |
| pp. 22, 28-29 | `WHAT 17` | SCS source has 30-second/30-minute conflict | ZigBee source repeatedly states 30 seconds; does not resolve SCS conflict | ZigBee-specific value documented; SCS conflict retained |
| pp. 21, 30-31 | `WHAT 32` Toggle | Not in current SCS-oriented `WHAT` table | ZigBee-specific extension | ZigBee variant |
| pp. 21-22, 32 | `WHAT 34`, `39` movement events | Not in current SCS-oriented `WHAT` table | ZigBee-specific events | ZigBee variant |
| pp. 23-31 | Supervisor state reports | Current ZigBee management page establishes Supervisor mode but not Lighting event consequences | ZigBee-specific behavior | ZigBee variant, cross-linked to `WHO 13` |
| pp. 30-31 | Toggle reply without Supervisor and possible duplicate report with Supervisor | Missing | ZigBee-specific behavior | ZigBee variant |
| pp. 21, 32 | Movement events require prior source-named PnL procedure | Binding page documents OpenWebNet-visible `WHO 25` lifecycle | OpenWebNet-visible prerequisite retained; underlying ZigBee mechanics excluded | ZigBee variant with binding cross-reference |
| pp. 33-34 | `DIMENSION 1` read/write | SCS `DIMENSION 1` exists with different value semantics | Materially different variant semantics | ZigBee variant |
| pp. 33-34 | `LEVEL=101..200` | SCS reference also defines `100` OFF | ZigBee source does not define `100` here | Do not import SCS OFF sentinel into ZigBee definition |
| pp. 33-34 | `SPEED=0..255`, `0` immediate, `255` maximum delay | SCS `DIMENSION 1` labels `0` last speed and `255` default | Materially different variant semantics | ZigBee variant |
| p. 35 | General state request | SCS request exists with different `WHERE` family | Same mechanism class, variant address/response applicability | ZigBee variant |
| ZigBee section 8 omissions | SCS blinking, relative dimming, `WHAT 1000`, `DIMENSION 2/3/4/8/9` | Present in SCS reference | Not established by this ZigBee source; not a non-support claim | Explicit evidence limit |

## `WHO 2` - Automation

| Source location | Item | Existing encyclopedia state | Adjudication | Canonical result |
| --- | --- | --- | --- | --- |
| pp. 36-38 | `WHAT 0` Stop, `1` Up, `2` Down | Same base values in SCS reference | Same detailed semantic operation; ZigBee address/transport differs | [ZigBee Automation Variant](../../functional/who-2-automation/zigbee-variant.md) |
| p. 11 versus pp. 36, 38 | Automation Up numeric value | Existing ZigBee interface page records conflict | Source-internal contradiction: page 11 uses `WHAT 2` for Up; detailed section uses `WHAT 1` | Conflict preserved in ZigBee variant |
| pp. 37-38 | Supervisor command-state reports | Not detailed in SCS reference as ZigBee behavior | ZigBee-specific behavior | ZigBee variant |
| p. 36 | Up reaches limit: Up report, Stop report, then position status | Missing | ZigBee-specific documented sequence | ZigBee variant, not generalized to all shutters |
| pp. 37, 39 | `DIMENSION 10` payload | SCS has same four field names with richer value domains | Materially narrower ZigBee semantics | ZigBee variant |
| p. 39 | Uncalibrated position returns `255` | SCS reference already defines `255` unknown but not this ZigBee calibration condition | ZigBee-specific applicability condition | ZigBee variant |
| pp. 39-40 | `DIMENSION 11` move to position | SCS form includes priority parameter | Materially different ZigBee grammar: level only | ZigBee variant |
| p. 40 | State request | SCS request model exists with different `WHERE` | Same mechanism class, variant address/response applicability | ZigBee variant |
| ZigBee section 9 omissions | SCS advanced `WHAT 10..12`, translation `WHAT 1000`, richer priority/info states | Present in SCS reference | Not established by this ZigBee source | Explicit evidence limit |

## `WHO 4` - Temperature Control

| Source location | Item | Existing encyclopedia state | Adjudication | Canonical result |
| --- | --- | --- | --- | --- |
| p. 41, section 10 | `WHAT` table | Broad SCS `WHAT` model exists | ZigBee section contains no `WHAT` entries; do not import SCS commands | [ZigBee Temperature Control Variant](../../functional/who-4-temperature-control/zigbee-variant.md) |
| p. 41 | `DIMENSION 0` Temperature level | SCS `DIMENSION 0` measured-temperature operation exists | Same identifier, materially different payload/applicability | ZigBee variant |
| p. 41 | Server-originated temperature report only | SCS reference defines a client request | ZigBee source does not establish a request | ZigBee variant; no inferred request |
| p. 41 | `C1C2C3C4` signed temperature encoding | SCS reference uses a different measured-temperature representation | Materially different variant semantics | ZigBee variant |
| p. 41 | Prior source-named PnL procedure | Not part of SCS Temperature Control | ZigBee-specific prerequisite; underlying radio mechanics excluded | ZigBee variant with `WHO 25` cross-reference |
| ZigBee section 10 omissions | SCS central-unit, zone, actuator, setpoint, program, fan-coil and split-control surfaces | Present in SCS reference | Not established by this ZigBee source | Explicit evidence limit |

## `WHO 18` - Energy Management

| Source location | Item | Existing encyclopedia state | Adjudication | Canonical result |
| --- | --- | --- | --- | --- |
| p. 53 section heading | "Automation WHO = 18" | Canonical namespace is Energy Management | Source editorial inconsistency; prose and operations are energy-related | Recorded, not promoted as a second meaning |
| p. 53 summary versus detailed Reset | `WHAT 0` versus `WHAT 75` Reset | SCS reference uses `WHAT 75` for a parameterized totalizer reset | Source-internal contradiction; SCS numeric match is not independent ZigBee evidence | [ZigBee Energy Management Variant](../../functional/who-18-energy-management/zigbee-variant.md) |
| pp. 54-56 | `DIMENSION 11`, `17`, `51`, `112`, `113`, `114`, `115`, `117` | Current SCS registry differs substantially | ZigBee-specific or materially different variant semantics | ZigBee variant |
| p. 53 use case versus pp. 54-55 | Frequency uses `DIMENSION 51` in use case; table/details use `112`, with `51` Energy | Not previously recorded | Source-internal contradiction | ZigBee variant and this review |
| pp. 54-56 | Measurement `VALUE` fields | SCS reference contains units for some overlapping operations | ZigBee source says only named quantity "in decimal" | Units/scaling remain unresolved; do not import SCS units |
| p. 57 | `DIMENSION 1200` Report Power | SCS `DIMENSION 1200` exists | Materially different grammar and timing units | ZigBee variant |
| p. 57 | `TIME=0..255` seconds | SCS reference uses minutes | Materially different variant semantics | ZigBee variant |
| p. 57 | Resulting report payload | Current SCS reference links reporting to active-power events | ZigBee section does not show or identify the later report frame | Unresolved; no inferred `DIMENSION 113` event linkage |
| ZigBee section 12 omissions | SCS Stop&Go, historical series, actuator-control and family-specific address model | Present in SCS reference | Not established by this ZigBee source | Explicit evidence limit |

## Out-of-scope material

No ZigBee-native routing, ZCL/ZDO semantics, radio commissioning internals, calibration internals, or binding-table internals are promoted. Terms such as "PnL", calibration, broadcast, and Supervisor are documented only to the extent that the source exposes consequences through OpenWebNet.

Real example MAC-derived product identifiers from the source are not reproduced. Canonical pages use symbolic `WHERE` forms.

## Step 1 coverage conclusion

Sections 8, 9, 10, and 12 of ZigBee OpenWebNet version 4.0 were read in full. Related cross-cutting evidence needed for these sections was also checked, including the page-11 general frame examples, ZigBee acknowledgement behavior, `WHO 13` Supervisor semantics, and the `WHO 25` prerequisite references.

For these four namespaces, every `WHAT`, `DIMENSION`, general request form, material event/report behavior, and material source conflict present in the inspected ZigBee version 4.0 source is now assigned to a canonical documentation location or an explicit evidence-limit/conflict record.

Accordingly, `WHO 1`, `WHO 2`, `WHO 4`, and `WHO 18` are **source-bounded complete for the ZigBee OpenWebNet version 4.0 specification**, subject to the explicit unresolved contradictions and source-provenance qualification above. This conclusion does not establish runtime support or identical behavior across every ZigBee gateway, Device, or Firmware.

`WHO 1000` discovery reconciliation and the final ZigBee source-to-documentation completeness matrix remain later tasks and are intentionally outside this Step 1 review.
