# Overview

The functional protocol reference documents OpenWebNet systems using `WHO` as the canonical protocol namespace. Each `WHO` defines the context in which its `WHAT` values, `WHERE` grammar, `DIMENSION` identifiers, parameters, and operation-specific behavior are interpreted.

Common frame syntax is defined in [`../protocol/`](../protocol/). Reference material is organized by protocol namespace, while the indexes below provide both protocol-oriented and function-oriented navigation to the same canonical pages.

## By `WHO`

| `WHO` | System | Reference |
| ---: | --- | --- |
| `0` | Scenarios | [`who-0-scenarios/`](who-0-scenarios/) |
| `1` | Lighting | [`who-1-lighting/`](who-1-lighting/) |
| `2` | Automation | [`who-2-automation/`](who-2-automation/) |
| `3` | Load Management | [`who-3-load-management/`](who-3-load-management/) |
| `4` | Temperature Control | [`who-4-temperature-control/`](who-4-temperature-control/) |
| `5` | Alarm | [`who-5-alarm/`](who-5-alarm/) |
| `6` | Basic Video Door Entry | [`who-6-basic-video-door-entry/`](who-6-basic-video-door-entry/) |
| `7` | Multimedia / Video | [`who-7-multimedia-video/`](who-7-multimedia-video/) |
| `8` | Video Door Entry and Telephony | [`who-8-video-door-entry-telephony/`](who-8-video-door-entry-telephony/) |
| `9` | Auxiliaries | [`who-9-auxiliaries/`](who-9-auxiliaries/) |
| `10` | Navigation commands | [`who-10-navigation/`](who-10-navigation/) |
| `11` | Energy distribution | [`who-11-energy-distribution/`](who-11-energy-distribution/) |
| `12` | Messages | [`who-12-messages/`](who-12-messages/) |
| `13` | Integration / Gateway functions | [`who-13-integration-gateway/`](who-13-integration-gateway/) |
| `14` | Special commands | [`who-14-special-commands/`](who-14-special-commands/) |
| `15` | Home-automation Main Unit / CEN | [`who-15-cen/`](who-15-cen/) |
| `16` | Sound System | [`who-16-sound-system/`](who-16-sound-system/) |
| `17` | Scenario Management | [`who-17-scenario-management/`](who-17-scenario-management/) |
| `18` | Energy Management | [`who-18-energy-management/`](who-18-energy-management/) |
| `19` | Interface | [`who-19-interface/`](who-19-interface/) |
| `22` | Multimedia / Sound Diffusion | [`who-22-sound-diffusion/`](who-22-sound-diffusion/) |
| `23` | Access Control | [`who-23-access-control/`](who-23-access-control/) |
| `24` | Lighting Management | [`who-24-lighting-management/`](who-24-lighting-management/) |
| `25` | Transversal Functions | [`who-25-transversal/`](who-25-transversal/) |
| `26` | UPnP multimedia command | [`who-26-upnp-multimedia/`](who-26-upnp-multimedia/) |
| `27` | Nurse Call basic level | [`who-27-nurse-call/`](who-27-nurse-call/) |
| `99` | Service Identification | [`who-99-service-identification/`](who-99-service-identification/) |

The table reflects the functional namespace established by the public specifications together with the MyHOME_Suite implementation data, including the `OPEN.db` system definitions. A listed `WHO` does not imply that every semantic value is currently known.

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

## Scope

`WHAT` and `DIMENSION` identifiers are documented within the `WHO` that defines them. `WHERE` is likewise interpreted according to the selected `WHO`; it is not a universal address type.

Where one `WHO` contains several functional groups, those groups are divided into subordinate pages when that improves the reference while remaining under the canonical `WHO` directory. Systems with a larger established vocabulary use dedicated `WHAT`, addressing, or `DIMENSION` pages; smaller or less completely established systems keep the supported semantics together.

Diagnostic and configuration/programming operations are documented separately under `diagnostics/` and `programming/`.