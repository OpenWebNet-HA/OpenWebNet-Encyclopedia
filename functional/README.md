# Functional Protocol

The functional protocol reference documents OpenWebNet systems using `WHO` as the canonical protocol namespace. Each `WHO` defines the context in which its `WHAT` values, `WHERE` grammar, `DIMENSION` identifiers, parameters, and operation-specific behavior are interpreted.

Common frame syntax is defined in [Protocol](../protocol/). Reference material is organized by protocol namespace, while the indexes below provide both protocol-oriented and function-oriented navigation to the same canonical pages.

The [`Functional Source Coverage`](source-coverage.md) page records which namespaces have a dedicated public specification and which rely on narrower implementation evidence. The MyHOME_Suite [`OPEN.db` coverage matrix](open-db-coverage.md) documents what that implementation database establishes for every functional namespace: system identity, diagnostic-family mapping, management support, address rules, and concrete `EN_OPEN` frame associations where present. The broader [`cross-database functional coverage`](cross-database-coverage.md) correlates `OPEN.db` with `MHCatalogue.db`, the two ScenarioDevices databases, and `rules.db3`, including functional command templates and Device/Object applicability that are not represented in `OPEN.db` alone.

## By `WHO`

| `WHO` | System | Reference |
| ---: | --- | --- |
| `0` | Scenarios | [`WHO 0` - Scenarios](who-0-scenarios/) |
| `1` | Lighting | [`WHO 1` - Lighting](who-1-lighting/) |
| `2` | Automation | [`WHO 2` - Automation](who-2-automation/) |
| `3` | Load Management | [`WHO 3` - Load Management](who-3-load-management/) |
| `4` | Temperature Control | [`WHO 4` - Temperature Control](who-4-temperature-control/) |
| `5` | Alarm | [`WHO 5` - Alarm](who-5-alarm/) |
| `6` | Basic Video Door Entry | [`WHO 6` - Basic Video Door Entry](who-6-basic-video-door-entry/) |
| `7` | Multimedia / Video | [`WHO 7` - Multimedia System](who-7-multimedia-video/) |
| `8` | Video Door Entry and Telephony | [`WHO 8` - Video Door Entry and Telephony](who-8-video-door-entry-telephony/) |
| `9` | Auxiliaries | [`WHO 9` - Auxiliaries](who-9-auxiliaries/) |
| `10` | Navigation commands | [`WHO 10` - Navigation Commands](who-10-navigation/) |
| `11` | Energy distribution | [`WHO 11` - Energy Distribution](who-11-energy-distribution/) |
| `12` | Messages | [`WHO 12` - Messages](who-12-messages/) |
| `13` | Integration / Gateway functions | [`WHO 13` - Integration and Gateway Functions](who-13-integration-gateway/) |
| `14` | Special commands | [`WHO 14` - Special Commands](who-14-special-commands/) |
| `15` | Home-automation Main Unit / CEN | [`WHO 15` - CEN](who-15-cen/) |
| `16` | Sound System | [`WHO 16` - Sound System](who-16-sound-system/) |
| `17` | Scenario Management | [`WHO 17` - Scenario Management](who-17-scenario-management/) |
| `18` | Energy Management | [`WHO 18` - Energy Management](who-18-energy-management/) |
| `19` | Interface | [`WHO 19` - Interface](who-19-interface/) |
| `22` | Multimedia / Sound Diffusion | [`WHO 22` - Sound Diffusion](who-22-sound-diffusion/) |
| `23` | Access Control | [`WHO 23` - Access Control](who-23-access-control/) |
| `24` | Lighting Management | [`WHO 24` - Lighting Management](who-24-lighting-management/) |
| `25` | Transversal Functions | [`WHO 25` - Transversal Functions](who-25-transversal/) |
| `26` | UPnP multimedia command | [`WHO 26` - UPnP Multimedia](who-26-upnp-multimedia/) |
| `27` | Nurse Call basic level | [`WHO 27` - Nurse Call Basic Level](who-27-nurse-call/) |
| `99` | Service Identification | [`WHO 99` - Session and Service Identification](who-99-service-identification/) |

The table reflects the functional namespace established by the public specifications together with the MyHOME_Suite implementation data. A listed `WHO` does not imply that every semantic value is currently known.

## By function

| Functional area | Protocol reference |
| --- | --- |
| Scenarios | [`WHO 0`](who-0-scenarios/), [`WHO 17`](who-17-scenario-management/) |
| Lighting | [`WHO 1`](who-1-lighting/), [`WHO 24`](who-24-lighting-management/) |
| Automation | [`WHO 2`](who-2-automation/) |
| Load and energy | [`WHO 3`](who-3-load-management/), [`WHO 11`](who-11-energy-distribution/), [`WHO 18`](who-18-energy-management/) |
| Temperature control | [`WHO 4`](who-4-temperature-control/) |
| Alarm | [`WHO 5`](who-5-alarm/) |
| Video Door Entry and multimedia | [`WHO 6`](who-6-basic-video-door-entry/), [`WHO 7`](who-7-multimedia-video/), [`WHO 8`](who-8-video-door-entry-telephony/), [`WHO 26`](who-26-upnp-multimedia/) |
| Auxiliaries | [`WHO 9`](who-9-auxiliaries/) |
| Navigation and messages | [`WHO 10`](who-10-navigation/), [`WHO 12`](who-12-messages/) |
| Integration and interface | [`WHO 13`](who-13-integration-gateway/), [`WHO 19`](who-19-interface/) |
| Special commands | [`WHO 14`](who-14-special-commands/) |
| CEN / CEN+ | [`WHO 15`](who-15-cen/), [CEN+ in `WHO 25`](who-25-transversal/cen-plus.md) |
| Sound | [`WHO 16`](who-16-sound-system/), [`WHO 22`](who-22-sound-diffusion/) |
| Access control | [`WHO 23`](who-23-access-control/) |
| Dry contacts / IR | [Dry-contact and IR functions in `WHO 25`](who-25-transversal/dry-contact-ir.md) |
| Nurse Call | [`WHO 27`](who-27-nurse-call/) |
| Protocol services | [`WHO 99`](who-99-service-identification/) |

## Evidence labels

Each page should distinguish:

- **published protocol** - values and grammar stated by a canonical public `WHO` document;
- **implementation evidence** - MyHOME Suite database templates, address rules, or scenario capabilities;
- **observed behavior** - private captures or Device experiments;
- **unresolved** - namespace or field exists, but the current corpus does not establish its semantics.

A namespace row is not evidence for a complete vocabulary. Conversely, absence from an implementation table is not proof that a published functional operation does not exist.

## Scope

`WHAT` and `DIMENSION` identifiers are documented within the `WHO` that defines them. `WHERE` is likewise interpreted according to the selected `WHO`; it is not a universal address type.

Where one `WHO` contains several functional groups, those groups are divided into subordinate pages when that improves the reference while remaining under the canonical `WHO` directory. Systems with a larger established vocabulary use dedicated `WHAT`, addressing, or `DIMENSION` pages; smaller or less completely established systems keep the supported semantics together.

Diagnostic and configuration/programming operations are documented separately under `diagnostics/` and `programming/`. The [`OPEN.db` coverage matrix](open-db-coverage.md) cross-references those management capabilities without reclassifying diagnostic frames as functional `WHO` commands; the [`cross-database functional coverage`](cross-database-coverage.md) adds catalogue and scenario-engine evidence while preserving each database's independent identifier spaces.