# Stereo control

## Summary

L4561N / 003586 integrates an external stereo source into the MyHOME sound system. It accepts stereo RCA audio and learns the source’s infrared commands, allowing configured ON/OFF and source-event sequences to be sent through its IR transmitter.

| Field | Value | Evidence |
| --- | --- | --- |
| Device ID | `OWN-DEV-0100` | Project identity |
| Technical description | Stereo control | Canonical catalogue |
| Commercial identities | `L4561N`, `003586` | Canonical commercial records |
| Catalogue item | `1130` | Canonical catalogue |
| Main catalogue system | Sound system | Canonical catalogue |
| Item model / `modobj` | `6` | Canonical inventory |
| Firmware definition | `4.0.6` | Canonical firmware catalogue |
| Declared Modules | `1` | Canonical firmware catalogue |
| Categories | Sound system | Capability model |

## Commercial identities

| Brand / line | Reference | Relationship | Evidence |
| --- | --- | --- | --- |
| BTicino | `L4561N` | Established catalogue identity | canonical commercial record for item `1130` |
| Legrand | `003586` | Established catalogue identity | canonical commercial record for item `1130` |

## Documentation

| Document | Type | Revision / date | Coverage | Archived original | Publisher source |
| --- | --- | --- | --- | --- | --- |
| MyHOME Suite `MHCatalogue.db` | canonical configuration catalogue | `3.5.38` | commercial identity, firmware, Module/Object topology and configuration surfaces | [Archived source database](../../sources/myhome-suite/3.5.38/databases/) | Bundled with MyHOME Suite `3.5.38` |
| MyHOME residential automation catalogue | Product catalogue | not stated in retained row | L4561N stereo source interface: printed p. 28 / PDF p. 28; commercial cross-reference printed p. 34 / PDF p. 34; only cited applicable leaves examined; unrelated guide pages and linked dedicated documents unexamined | [Archived PDF](https://archive.openwebnet-ha.org/sha256/13/8e/138e7a234fe24fb044d3bfc82954e08b2887be22f3f8ceb24aecaeff6ed2f2e5.pdf) | [Official source](https://assets.legrand.com/pim/DOCUMENT/BR%20MyHOME%20HPML0714.pdf) |
| `U2109G_I_EN.pdf` | Installer manual · EN | Revision G in filename; printed issue date not stated | Entire substantive chapters, printed/PDF pp. 4–10; exact L4561N connectors, configuration, reset and appendix; front/closing leaves outside operating claims | [Archived original](https://archive.openwebnet-ha.org/sha256/d2/67/d267def402aabbd1d7356afcbbbdfe57da3be2dad4446272c6079eeaec3d45f6.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/U2109G_I_EN.pdf) |
| `T9523G.pdf` | Illustrated installation instructions · multilingual | 01PC-12W48 | All four PDF pages; printed pp. 2–4 and unnumbered first diagram; exact stereo/BUS/IR connection and placement | [Archived original](https://archive.openwebnet-ha.org/sha256/1c/12/1c12ae9dd5b66a58d6ab3fc18be1ec15c007c32a82b5d03b400ffdce891488bb.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/T9523G.pdf) |
| `U2109B_S_IT.pdf` | TiStereoControl software manual · IT | Version 1.0; 02/08-01PC | Entire substantive chapters, printed/PDF pp. 4–21; connection, IR capture, associations, settings, tests, .xml/.MDB and .fwz transfer; front/closing leaves outside operating claims | [Archived original](https://archive.openwebnet-ha.org/sha256/26/0c/260cf214c8e3fbc7bc3353003aadb025b7e272a977bafacc9ae14bddc16cba1b.pdf) | [Publisher source](https://dar.bticino.it/asset/Documents/U2109B_S_IT.pdf) |

## Physical and electrical characteristics

| Property | Value | Evidence |
| --- | --- | --- |
| Construction / connectors | Four `17.5 mm` DIN modules; stereo RCA input, IR receiver, `3.5 mm` IR-transmitter jack, USB and eight-pole sound BUS | BR-MyHOME p. 28; U2109G_I_EN p. 4; T9523G PDF p. 1 |
| Power / temperature | `18..27 Vdc`; standby maximum `50 mA`, operating maximum `40 mA`; `5..35 °C` | U2109G_I_EN appendix p. 10; unusual standby/active ordering preserved |
| Audio input | `14 kΩ` input impedance; sensitivity `0.2..1 Vrms`; channel balance TYP `±0.5 dB` / MIN `±1.5 dB` | Same appendix; literal source labels retained |
| Bandwidth / IR learning | `0.2..20 kHz` at `−3 dB` measured through the whole chain at amplifier output; IR carrier `30..80 kHz` | Same appendix; not isolated-unit bandwidth or RF support |
| Included connections | BUS cable `2 m`, IR lead `1.8 m`, RCA lead; device within `1 m` of source; IR emitter within `1 cm` of receiver, not directly on it | Installer pp. 5–6; no IR cable extension documented |

## Identity

| Field | Value | Evidence |
| --- | --- | --- |
| `EN_ITEM.id_item` | `1130` | Canonical catalogue |
| Technical item | Stereo control | Canonical catalogue |
| Main system | Sound system | Canonical catalogue |
| Item model / `modobj` | `6` | Canonical inventory |
| Commercial records | `2` | Canonical catalogue |

### Catalogue system and bus scope

| System | Item model / modobj | Main mapping | Evidence |
| --- | --- | --- | --- |
| Sound system | `6` | Yes | Canonical item/system relationship |

| Catalogue bus | Level | Evidence |
| --- | --- | --- |
| Multimedia | private riser | Canonical item/bus relationship |

These associations describe software applicability, not physical connector counts or observed services.

### Commercial-record metadata

| Commercial record | Reference | Brand key | Line key | Catalogue description |
| --- | --- | --- | --- | --- |
| `1130` | `L4561N` | `1` | `5` | Empty in source |
| `2121` | `003586` | `2` | `5` | `Legrand_Undefined_Stereo control` |

| Record | Visible | Dependent | Gateway flag | Visibility type |
| --- | --- | --- | --- | --- |
| `1130` | `1` | `0` | `0` | Empty in source |
| `2121` | `1` | `0` | `0` | Empty in source |

These flags are catalogue metadata, not physical capability or present market availability.

## Firmware and hardware

| Firmware ID | Version | Revision | Build | Declared Modules | Default | Catalogue status |
| --- | --- | --- | --- | --- | --- | --- |
| `65` | `4` | `0` | `6` | `1` | Catalogue default | Official |

Version/revision/build `-1` retains wildcard or unspecified applicability in the catalogue; it is distinct from Deprecated status. Status and default are metadata of this historical source snapshot, not present-day market availability or installed state. Installed firmware must be corroborated through the applicable diagnostic context.

### Parameter and package associations

| Firmware | Parameter record | Catalogue brand scope | Line scope | Parameter family | Source path |
| --- | --- | --- | --- | --- | --- |
| `65` | `35` | BTicino (key `1`) | `0` | external software | `TiStereoControl_0201` |
| `65` | `519` | Legrand (key `2`) | `0` | external software | `StereoControlConfig_0101` |

All 2 parameter-file associations are shown. Brand and line keys are parameter scopes, not diagnostic identifiers. Referenced payloads were not included in this catalogue extraction and have not been inspected; their contents are not inferred from filenames.

No `AS_FW_PACKAGE` association is stored. This is catalogue coverage, not a claim that manufacturer firmware downloads never existed.

## Module, Object, and Virgin Object model

| Firmware | Module slot | External Object | Catalogue placement | Catalogue slot row ID | Catalogue Object key | Object/Firmware relation |
| --- | --- | --- | --- | --- | --- | --- |
| `65` | `1` | `161` Phonic source | Fixed/designated metadata | `2298` | `161` | `976` |

Module slot is the Device-local placement, not a database row identifier. Fixed/designated metadata and candidate membership do not prove the installed active Object; use the conditions and runtime diagnostics in their established contexts.

### Virgin Objects

| Firmware | External Virgin Object | Module slots | Permitted external Objects | Catalogue Virgin Object key | Firmware/Virgin relation |
| --- | --- | --- | --- | --- | --- |
| all | None associated | - | - | - | - |

## Configuration modes

| Firmware | Mode | Catalogue mode | Evidence |
| --- | --- | --- | --- |
| `65` | Product Programming | `3` | Canonical firmware/mode association |

| Firmware | Connection | Evidence |
| --- | --- | --- |
| `65` | Serial | Canonical firmware/connection association |

Product setup procedures and catalogue mode identifiers have different scopes. A mode association does not prove every reusable Object field is physically available.

## Firmware-scoped configuration

Catalogue domains/defaults below are firmware-scoped, separate from the product-document and software Object domains. The source does not specify a default where the table says so.

| Firmware | Field | Catalogue domain | Catalogue default | Meaning |
| --- | --- | --- | --- | --- |
| `65` | `AID` | Identity template `********`; permitted character set not specified | Not specified in source | Device identity token; not a physical configurator |
| `65` | `S1` | `0..4` | `0` | S1 |
| `65` | `M1` | `0..4` | `0` | M1 |
| `65` | `M2` | `0..6` | `0` | M2 |

## Object configuration surfaces

The following domains and defaults describe reusable Object definitions in the canonical MyHOME Suite `3.5.38` catalogue. Numeric values are catalogue values; product units and physical configurator limits are separate scopes. Defaults do not establish installed state. Apply the firmware-specific restrictions under Conditions, filters, and conversions after resolving the active Object.

### Object `161` - Phonic source

| Field | Reusable domain | Reusable default | Meaning |
| --- | --- | --- | --- |
| `RECEIVE_MODE` | `0..1` | `0` | Set the reception mode of the radio signal |
| `NUM_STATION` | `0..3` | `0` | Set the number of station presets. 0 or 1for 5 station, 2 for 10 station and 3 for 15 station |
| `S` | `0..255` | `1` | Area |
| `SUB_SOURCE` | `0..15` | `0` | Max subsource |

### Device-specific interpretation

Official/default firmware `65`=4.0.6 declares one Module with Object `161` Phonic source, no Virgins, conditions, filters or conversions. Product Programming mode 3 and Serial connection 1 are stored; parameter records 35 and 519 have brand scopes 1/2 and line 0. The manufacturer software manual explicitly connects by USB-miniUSB and selects a COM port, reconciling the transport terminology without claiming a physical RS-232 socket. Firmware S1/M1=`0..4` and M2=`0..6` default 0; the physical installation source specifies S/M1=`1..4` and maintenance reset `M2=9`. The reset procedure does not widen the live catalogue field domain. Reusable NUM_STATION radio enums 0/1 five, 2 ten, 3 fifteen, S=`0..255` default 1 and SUB_SOURCE=`0..15` default 0 do not prove a built-in radio or guarantee all values apply to this IR-controlled external source.

## Conditions, filters, and conversions

### Slot conditions

| Firmware | Module slot | External Object | Condition ID | Stored predicate | Conversion rule |
| --- | --- | --- | --- | --- | --- |
| all | - | - | None | No slot-condition rows associated | None |

Empty predicates, missing condition rows and fixed placement metadata are not evidence of unconditional runtime activation. Preserve out-of-domain selectors and unresolved symbols as source irregularities; do not invent selection precedence.

### Object/Firmware restrictions

| Firmware | External Object | Filter ID | Field | Effective catalogue domain | Reusable default | Evidence / applicability |
| --- | --- | --- | --- | --- | --- | --- |
| all | - | None | - | No relation-specific filters associated | - | Canonical catalogue |

### Device-specific conversions

| Referenced rule | Item-side condition | Object configuration result | Source path / limitation |
| --- | --- | --- | --- |
| None | - | No conversion reference associated with these slot rows | Canonical catalogue |

These maps describe stored conversion branches after Object selection. Validate input against the exact firmware domain and output against the selected Object/Firmware restriction; a stored symbolic branch may be unreachable on this firmware. Generic evaluation and ambiguity handling remain in [Catalogue Resolution](../../internals/catalogue-resolution.md).

## Diagnostic applicability

| Diagnostic surface | Device-specific use | Canonical reference |
| --- | --- | --- |
| `DIMENSION 1` | corroborate technical identity for catalogue item `1130` / `modobj = 6` | [Device Identity](../../diagnostics/dim1-device-identity.md) |
| `DIMENSION 2` | select/corroborate the applicable catalogue firmware tuple while preserving wildcard semantics | [Dimension Reference](../../diagnostics/dimension-reference.md) |
| `DIMENSION 30` | corroborate declared Module/Object topology (`161`) | [Modules](../../diagnostics/dim30-modules.md) |
| `DIMENSION 32` | corroborate addressing only after the active Module/Object context is resolved | [Addressing](../../diagnostics/dim32-addressing.md) |
| `DIMENSION 35` | inspect physical/software configuration against firmware fields, conditions and filters | [Configuration](../../diagnostics/dim35-configuration.md) |

## Functional applicability

| External Object | Catalogue functional role | Applicability / evidence |
| --- | --- | --- |
| `161` Phonic source | Sound system | Firmware/Object capability association; resolve the slot and configuration first |

Catalogue system identifiers are not `WHO` numbers. The source establishes the roles shown, not a complete command vocabulary or proof of every installed function. Correlate the selected role with [Functional Protocol](../../functional/) before sending functional commands. Product behavior is additionally bounded by the publisher evidence below; uncorroborated transport and firmware details remain open work.

### Manufacturer-documented functions

| Function / setting | Documented behavior | Evidence |
| --- | --- | --- |
| IR event sequences | Learnt commands become available through sound-system amplifiers, special controls and Touchscreen; ON/OFF and four source events | TiStereoControl v1.0, printed/PDF pp. 8, 18 |
| Sequence settings | At most four commands per event; delay `1..60` seconds default 3; IR power Minimum/Medium/Maximum default Medium | Software pp. 15–16; not catalogue firmware field defaults |
| Multichannel restriction | S/M1 physically `1..4`; with F441M multichannel M1 must be 1 | Installer p. 7; set before connecting BUS |
| Status / adjustment | Signal LED off absent, green present/optimal with occasional orange peak, steady orange excessive; supply green standby / yellow operating; signal-level buttons | Installer p. 4; troubleshooting wording differs on p. 9 |

## Observed behavior and corroboration

No additional publishable Device-specific hardware/runtime observation is currently retained for this exact technical item.

## Programming

### Configuration and IR acquisition

U2109G_I_EN, printed/PDF pp. 5–8, sets physical S and M1 in `1..4`; F441M requires `M1=1`. The source recommends checking remote batteries and using a compatible single IR receiver, positioning the transmitter close to that receiver without covering it or extending its cable. USB leads longer than 5 m are not recognized.

U2109B_S_IT (02/08-01PC), printed/PDF pp. 8–21, documents TiStereoControl Version 1.0. It connects by USB-miniUSB with the Device BUS-powered and selects the correct COM port. The historical requirements are Windows XP or later, Internet Explorer 6 or later and the supplied USB drivers; this does not establish compatibility with current operating systems. Create a remote with mandatory type, brand, model and description; hold each remote button during capture and repeat the command capture for confirmation. Associate up to four commands per ON/OFF or source event, with independently editable `1..60` s delays (default 3) and three IR-power settings (default Medium). Test single commands and full event sequences with the connected Device.

Projects are .xml; remote databases import/export .MDB. Opening a saved project highlights absent remotes in red and offers import into the current database. Save a project and Download it to the Device, checking the reported success. Firmware update selects .fwz, Info displays version differences, then Update transfers the file. File payloads and build compatibility are not examined. The software p. 19 instruction calls for the installer’s restoration procedure after configuration updating; its exact configuration-versus-reset consequence requires corroboration and is retained as a source instruction, not an assumed safe universal routine.

### Recovery scope

Installer p. 8 says failed programming is retried after disconnecting BUS and USB. Its factory-restoration procedure powers off, sets S and M1 empty and `M2=9`, powers on until LED 3 lights, then powers off and restores configuration. `M2=9` is a maintenance setup outside the recorded firmware M2=`0..6` domain. Reset must not be equated with a runtime sound command or used to invent an extra legal software field.

## Source reconciliation

The BR catalogue p. 34 cross-reference uses old 03586 → L4561N, while the canonical SKU is 003586. U2109G_I_EN has no printed issue date found; its revision letter is filename evidence. T9523G prints 01PC-12W48; U2109B_S_IT prints 02/08-01PC and Version 1.0, independently of catalogue firmware `4.0.6`. Physical USB and the software’s COM selection provide source context for the canonical Serial association, without establishing an RS-232 connector. Installer p. 9 calls an excessive-signal indicator red and refers to a potentiometer, whereas p. 4 documents orange and buttons: these inconsistent troubleshooting terms do not add a control or overwrite the diagram. No built-in radio is inferred from Object `161`.

The catalogue-domain and conversion discrepancies are explained under [Device-specific interpretation](#device-specific-interpretation), alongside the complete reusable fields.

## Evidence limits and open work

- Parameter payloads 35/519, linked .fwz files, current PC compatibility and installed IR/transfer behavior remain unexamined.
- The software instruction to restore after updating configuration and the installer’s colour/control terminology discrepancy require source-specific follow-up; they are not silently rewritten.
- Applicable exact-product guide leaves were inspected; unrelated guide pages and linked dedicated documents remain unexamined.

- The retained catalogue is a historical software applicability source. Installed firmware, active Objects and protocol behavior are not corroborated by hardware captures. Manufacturer software, referenced parameter payloads, unexamined download links and unrelated guide pages are not treated as inspected originals.

## Sources

- [Device Database Inventory](../inventory/)
- [Device Source Index](../../sources/devices/index.md)
- [Firmware](../../device-model/firmware.md)
- [Configuration](../../device-model/configuration.md)
- [Physical Devices](../../device-model/physical-devices.md)

- [Semantic review record, 6 October 2026](../../project/review/device-reviews-0091-0100-2026-10-06.md#own-dev-0100)
