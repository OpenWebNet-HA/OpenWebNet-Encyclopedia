# Burglar alarm unit with PSTN communicator

## Summary

This burglar-alarm central unit combines intrusion-system management with a fixed-line telephone communicator. Its documented zone organization includes intrusion and technical alarms, with 16 partition scenarios and published OPEN-SCS functions for system interaction.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0132` | Project identity |
| Technical description | Burglar alarm unit with PSTN communicator | Canonical catalogue and source-scoped manufacturer documents |
| Commercial identities | `573934`, `067520` | All explicit catalogue commercial relationships; product documentation scoped separately |
| Catalogue item | `1423` | MyHOME Suite `3.5.38`, canonical `MHCatalogue.db` |
| Main catalogue system | Burglar alarm system | Main system association |
| Item model / `modobj` | `203` | Main association; independent of project ID |
| Firmware definition | `105`, `641` | Catalogue firmware IDs; version/build table below |
| Declared Modules | `1` | Firmware metadata |
| Categories | User interfaces, Gateways and interfaces, Multifunction devices | Source-derived roles |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| Legrand - Arteor | `573934` | Established catalogue identity | Manufacturer database commercial record `976` explicitly links this SKU to item `1423` |
| Legrand - Céliane | `067520` | Established catalogue identity | Manufacturer database commercial record `1423` explicitly links this SKU to item `1423` |

### Catalogue labels and classifications

| Reference | Catalogue name | Evidence |
| --- | --- | --- |
| `573934` | Burglar alarm central unit with communicator | Canonical commercial record `976` |
| `067520` | Burglar alarm central unit with communicator | Canonical commercial record `1423` |

Both commercial records are enabled for catalogue display, have no visibility-type value, and are not marked dependent or gateway in this historical commercial table. These classifications do not establish market availability, installed state or functional gateway capability. Empty or truncated internal description labels are not used to infer additional product features.

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| `u3500a.pdf` | Installation manual | `u3500a; 11/08-01 PC` | Exact 573934/573935 shared installer original; review examined identity/overview pp. 1–12, installation/commissioning pp. 14–34 and protocol/appendix pp. 69–82. Detailed menu pages 35–68 not fully rechecked; 573935 remains outside this item. | [Archived original](https://archive.openwebnet-ha.org/sha256/a3/75/a375768955e0bd9d19a227b8f9416584cbbdfa7443d0cf23552aecb20a68b6d0.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/np-ft-gt/u3500a.pdf) |
| `u3501a_s_uk.pdf` | SecurityConfig manual | `u3501a_s_uk; original publication date not established` | Exact Arteor SecurityConfig manual; pp. 4–20 and 46–54 examined for project/connection/parameter transfer/history/voice/update procedures. Detailed parameter screens pp. 21–45 remain unexamined in this review. | [Archived original](https://archive.openwebnet-ha.org/sha256/72/35/7235899a2edacb9dddd4ba11aed4a033b2c2a03d7c8897bcee4ccc123ea453ac.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/np-ft-gt/u3501a_s_uk.pdf) |
| `U3887A.pdf` | French/English Céliane installation manual | `U3887A; 11/09-01 PC` | Exact 067520 manual; selected English installation/learning/PC and protocol/technical comparison pp. 98–104, 112–113, 161–164 examined. Other English pages and the French translation not claimed as fully reconciled in this review. | [Archived original](https://archive.openwebnet-ha.org/sha256/40/7e/407e5481847fadc8e3180c703fcc464a2c1c6c2987079be71d34690d8d70d983.pdf) | [Publisher original](https://assets.legrand.com/pim/NP-FT-GT/U3887A.pdf) |
| `u3499a.pdf` | Exact historical manufacturer documentation | `u3499a; 11/08-01 PC` | Exact Arteor user manual, PDF pp. 1–40 examined; alarm/key/zone/call/voice and remote-operation scopes, distinct local/telephone lockouts and published examples. | [Archived original](https://archive.openwebnet-ha.org/sha256/b7/c3/b7c3620e398e201f98ff2760806a8c885a81e4f2e953dc20a7e0d6ce47566882.pdf) | [Publisher original](https://assets.legrand.com/general/legrand-exp/np-ft-gt/u3499a.pdf) |
| MyHOME Suite `MHCatalogue.db` | Canonical configuration catalogue | `3.5.38` | All item, commercial, system, Firmware, Module/Object/Virgin, field, filter, condition, conversion and ancillary associations for item `1423` | [Archived database metadata](../../sources/myhome-suite/3.5.38/databases/) | Bundled manufacturer software |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| SCS supply, Arteor manual | `18..28 V` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Current draw, as printed | `standby 55..90 mA Max` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Operating temperature | `5..40 °C` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Dimensions, both manuals | `125 x 128 x 31 mm` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Enclosure | `IP30` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Zones | `0: up to 9 connectors; 1..8: intrusion sensors; 9: technical/auxiliary alarms` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Partition scenarios | `16` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Telephone book | `jolly number + 10 stored numbers` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Simplified telephone commands | `9` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |
| Telephone interface | `two-wire pair; DTMF/pulses line label; selection specified DTMF only` | `U3500A` printed/PDF pp. 11-12, 81; `U3887A` English printed/PDF p. 163 |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1423` | Canonical catalogue |
| Technical item description | Burglar alarm central unit with communicator | Canonical catalogue |
| Item family | 0; key `10` | Canonical catalogue |
| Main system | Burglar alarm system; key `3` | `AS_ITEM_SYSTEM` |
| Main item model / `modobj` | `203` | `AS_ITEM_SYSTEM` |
| Commercial record count | `2` | `EN_DEVICE` |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Burglar alarm system | `203` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Burglar alarm | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `105` | `1` | `0` | `17` | `1` | Catalogue default | Official |
| `641` | `2` | `0` | `0` | `1` | Not catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

No installed release, hardware revision or microcontroller fingerprint is corroborated. Missing build rows mean unknown build, not build zero.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `105` | `167` | Legrand (key `2`) | `0` | external software | `SecurityConfig_020030` |
| `105` | `628` | Legrand (key `2`) | `4` | external software | `UNAVAILABLE_0000` |
| `105` | `631` | Legrand (key `2`) | `2` | external software | `SecurityConfig_0100` |
| `641` | `629` | Legrand (key `2`) | `4` | external software | `SecurityConfig_0200` |
| `641` | `630` | Legrand (key `2`) | `2` | external software | `SecurityConfig_0200` |

All 5 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `105` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2262` | `13` | `940` |
| `641` | `1` | `13` AI Control Unit With Communicator Pstn | Fixed/designated metadata | `2466` | `13` | `1118` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | Not applicable | Not applicable | Not applicable | Not applicable |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `105` | Product Programming | `3` | Canonical firmware/mode association |
| `641` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `105` | Serial | Canonical firmware/connection association |
| `641` | Serial | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Domains and defaults are catalogue evidence. `AID` is a literal mask with no stored default or established character set; it is not a physical configurator.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `105` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |
| `641` | `AID` | `********` = AID | Not specified in source | Device identity token; not a physical configurator |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `13` - AI Control Unit With Communicator Pstn

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `NUM_PSTN` | No legal values specified in source | Not specified in source | Telephone number PSTN |
| `FW_VER` | No legal values specified in source | Not specified in source | Firmware version |
| `IS_GATEWAY` | `0` = Disable; `1` = Enable | `0` | Gateway |

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | Not applicable | Not applicable | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | Not applicable | None | Not applicable | No relation-specific filters associated | Not applicable | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | Not applicable | No conversion reference associated with these slot rows | Canonical catalogue |

No conversion rule is attached to these slot rows. Resolve the active Object and apply its exact Firmware restrictions; generic resolution and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | Corroborate item model `203` and variant identity in this Device’s diagnostic system context | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | Read installed firmware and compare with the applicability table | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 3` | Obtain hardware revision; no source-backed installed value | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 6` | Obtain microcontroller identity; no fingerprint retained | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | Resolve active Modules/Objects independently of candidate metadata | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | Corroborate installed addressing and distinguish physical from reusable ranges | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | Compare installed configuration with the exact firmware/Object restrictions | [Configuration](../../diagnostics/dim35-configuration.md) |

These are catalogue-derived diagnostic candidates. No Device-specific response or support across all commercial variants is established by a hardware capture.

## Functional applicability

| Catalogue Object / role | Applicability | Evidence |
| --- | --- | --- |
| `13` - AI Control Unit With Communicator Pstn | Applicable only after resolving its Firmware/Module placement and attached restrictions | Canonical catalogue relationship |

These are catalogue-derived functional roles, not a declaration that every candidate is simultaneously configured. Product UI pages may control remote subsystems without instantiating their Objects locally. System/model mappings in Identity are not WHO values. See [Functional Protocol](../../functional/) for canonical system semantics.

U3500A printed/PDF p. 81 explicitly lists OPEN-SCS families `WHO 0`, `WHO 1`, `WHO 2`, `WHO 4`, `WHO 5`, `WHO 9`; its commands on pp. 69-80 include alarm status, auxiliary commands, scenarios and stored-event readback. These are published capabilities, not measured installed responses.

## Observed behavior and corroboration

No publishable Device-specific hardware captures or experiments are retained for this cluster. Manufacturer operating descriptions are documented behavior; catalogue relationships are implementation capability metadata. Neither is a measured response from an installed Physical Device.

## Programming

Commission through system learning, sensor/zone test, scenario and key setup, date/time and telephone-dialler configuration. The installer workflow separately exposes zones, devices, event history, automation associations, preferences, maintenance, jolly/directory numbers, call events, vocal messages and telephone commands. SecurityConfig transfers configuration/history, customizes voice messages and updates firmware. Three incorrect keys block arming/disarming/menu access for one minute. The Céliane manual’s English section repeats these commissioning and OPEN command functions for 067520. Telephone service compatibility and Contact ID monitoring are documented capabilities, not contemporary provider availability or installed behavior. Credentials and installation-specific values are not reproduced.

Apply the complete catalogue domains, defaults, conditions and relation-specific filters above. A legal reusable value is not necessarily legal for this Firmware. Configuration paths and package labels are source associations, not verified payload encoding. The generic validation/session algorithm remains in [Programming](../../programming/).

### Commissioning and PC configuration

U3500A pp. 14–34 and the corresponding Céliane English sections pp. 98–104, 112–113 distinguish the local maintenance slide switch from software configuration. With the switch OFF, select language and run automatic learning; resolve reported tamper errors, then send the learned configuration to ready display devices when present. Switch ON, leave maintenance, return to System Test and check sensors without generating an alarm; configure keys/scenarios and date/time. Re-run learning after adding/removing devices and after SecurityConfig changes. The PSTN unit is placed first on the internal telephone line, ahead of other telephone devices (p. 16 / p. 98).

SecurityConfig pp. 5–20 uses a selected COM port through cable `049234` between a PC USB port and the unit's six-way connector. Start learning and follow the software's switch/cable prompts. Receive configuration before editing an existing system; compatibility comparison exposes differences. Force sends the project's parameters to the unit; Align changes the project to match the unit.  Event memory can be received and exported. Project files use `.jai`; configuration exports use `.csv`.

Voice-message receive and loading preset messages overwrite the corresponding project content. WAV imports require PCM 8 kHz, 8-bit mono, with duration bounded by the selected message. The firmware workflow selects `.fwz`, compares versions and prompts for the maintenance-switch/cable sequence; after successful transfer it requires disconnection and a unit reset. Reset cancels date/time according to the installer troubleshooting appendix. Payloads, real recordings, telephone numbers and installation credentials were not examined (SecurityConfig pp. 46–53; U3500A pp. 31, 82).

The exact user manual pp. 12–35 distinguishes intrusion-zone selection, enabling/disabling keys, alarm-history display, siren stopping, telephone-call suppression and remote-management authorization. Telephone remote management can be ON, Manager only, User only or OFF. A directory can contain ten entries but each event call set selects up to four, after the Jolly number; disabling that set does not suppress Jolly. Three wrong telephone credentials end the call, distinct from the local one-minute lockout. These are documented workflows, not tested service availability.

## Source reconciliation

573934 and 067520 are explicit Legrand - Arteor/Céliane database identities. U3500A covers 573934/35; U3887A covers 067520. The adjacent 573935 model is not an extra member of this cluster. The rich installer/software configuration remains outside the database’s three sparse Object `13` fields; sparse fields do not negate those published functions. U3500A’s standby wording and DTMF/pulses versus DTMF-only statements are retained as separate source claims. The later Céliane manual is a different product-line scope, not proof that every Arteor physical dimension applies to Céliane.

### Retained source accounting

| Original | Role / reconciliation scope |
| --- | --- |
| `u3500a.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `u3501a_s_uk.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `U3887A.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |
| `u3499a.pdf` | Device-specific ratings, roles, configuration or operating procedures incorporated above; material revision differences and remaining limits are stated here. |

The Céliane appendix independently repeats the `125 x 128 x 31 mm`, supply, current, temperature and IP30 data; those facts therefore have direct support for both product lines. The physical rechargeable battery is documented in installation, while its exact chemistry/capacity is not fixed by the quoted technical tables.

### Semantic review findings

Both catalogue commercial records establish identities; the shared Arteor manual also covers `573935`, which is outside this item and is not added as a variant. Both exact installer manuals state SCS `18..28 V` and the unusual standby `55..90 mA Max` wording, retained without inventing a separate peak rating. Firmware `105` (`1.0.17`, default) and `641` (`2.0.0`, nondefault) each place Object `13` in one slot, without Virgin, filter, condition or conversion associations. Their small AID/FW_VER/SYSADDRESS schema does not describe all local menus, telephone functions or SecurityConfig parameters. Five parameter associations include the literal `UNAVAILABLE_0000`; this named catalogue association is not silently dropped. The serial catalogue connection is consistent with USB-to-six-way adapter `049234`, not a native USB socket. U3500A p. 80 incorrectly prints WHO `1` in its auxiliary table although its example, p. 70 family table and Céliane p. 162 specify WHO `9`. No protocol KB change or observed compatibility claim is inferred.

## Evidence limits and open work

Battery replacement applicability, PSTN provider compatibility, per-line physical differences, installed firmware, telephone security behavior and device-specific captures remain open.

No installed release, hardware revision or microcontroller fingerprint has been established for this cluster. The diagnostic table describes source-derived candidates. Further manufacturer discovery and hardware corroboration remain partial; catalogue extraction and source reconciliation are complete for the retained evidence listed here.

Detailed per-parameter SecurityConfig screens on pp. 21–45 and installer menu details outside the examined commissioning/protocol scopes have not been fully rechecked during this review. The Céliane French translation and remaining English menu details are not claimed as fully reconciled. A regional Legrand Tunisia exact 067520 product-page lead was found, but retrieval returned HTTP 403; its search-result barcode was not incorporated without retaining and verifying the original. Source references to historical portals or Contact ID services do not establish their current availability.

## Sources

Complete implementation extraction uses the retained canonical `MHCatalogue.db`, SHA-256 `f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5`. Commercial/system/firmware/build associations, reusable fields and their ranges/defaults, slot/Object/Virgin relationships, every attached filter/condition/conversion, modes, connections, parameters and packages are separately scoped above. Archived documents and publisher provenance are paired in Documentation.

- [Device Database Inventory](../inventory/)
- [Canonical catalogue source and fingerprint](../../sources/myhome-suite/3.5.38/databases/)
- [Device Source Index](../../sources/devices/index.md)
- [Catalogue Resolution](../../internals/catalogue-resolution.md)
- [Physical Devices](../../device-model/physical-devices.md)
- [Programming](../../programming/)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0131-0140-2026-10-06.md#own-dev-0132)
