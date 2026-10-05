# Canonical Field Evidence Repository

This directory contains canonical, privacy-preserving real-world OpenWebNet evidence packages collected from physical hardware installations, conforming to the RFC #536 and Discussion #509 evidence model.

## Policy Boundary & Provenance Split (Discussion #509)

As established in Discussion #509 and governed by `sources/manifest.yaml`:
- **`sources/`**: Contains immutable vendor distribution files (MyHOME Suite SQLite databases, product manuals, protocol PDFs). Network captures are excluded from `sources/` to protect private installation topologies.
- **`evidence/`**: Serves as the canonical repository for **sanitized, reproducible empirical field evidence packages**. Every package is self-contained, reproducible, stripped of private network/topology identities, and validated against formal JSON schemas.

## Evidence Model & Privacy Architecture

Each capture package is self-contained in its own directory:

```
evidence/
├── schema/
│   ├── evidence-manifest.schema.json   # Draft 2020-12 schema for package manifests
│   ├── evidence-frame.schema.json      # Draft 2020-12 schema for on-wire frame records
│   └── evidence-privacy.schema.json    # Draft 2020-12 schema for sanitization profiles
├── validate_evidence.py                # Deterministic validator enforcing schema & timing rules
└── <capture_id>/
    ├── manifest.json                   # Metadata, hardware context, test recipe, claims supported
    ├── frames.jsonl                    # Ordered frames with relative delta timestamps (t_rel_ms)
    └── privacy.json                    # Sanitization profile adhering to evidence-privacy schema
```

### Privacy Contract (RFC #536)
- **Isolated Bench Environment**: Captures are performed on dedicated test benches with physical hardware (BTicino MH200 gateway, firmware 2.1.0).
- **Topology & Schedule Protection**: Real network IP addresses, gateway MACs, and credentials are completely sanitized (`removed_value_classes: [network_address, hardware_id, device_id, credential, installation_topology, location]`). Broad plant baseline sweeps containing multi-zone alarm topologies, audio routing layouts, or wall-clock schedules are strictly excluded from public publication.
- **Synthetically Bound Identifiers**: Configured SCS bus addresses (WHERE `99`, `62`, `74`, `#4#02`) are arbitrary test-bench assignments mapped to durable pseudonymized device identifiers.
- **Relative Chronology**: Timestamps represent relative millisecond offsets (`t_rel_ms`) from the start of the observation window (`t0 = 0`), preserving exact intra-frame timing without leaking real-world operational times.

---

## Evidence Classes and Allowed Combinations

The manifest schema enforces which values may appear together:

| `evidence_class` | `capture_kind` | `epistemic_status` | Context required |
| :--- | :--- | :--- | :--- |
| `public_experiment`, `public_capture` | `controlled_experiment`, `active_observation`, `passive_trace`, `fingerprint` | `experimentally_confirmed`, `observed`, `hypothesized` | `installation_id`, `bus_id`, `gateway_id` (strings), `environment`, `device_under_test` (`sku`, `configured_where`); `sub_bus_id`, if present, is a string; at least one frame and one claim |
| `firmware_emulation` | `firmware_oracle` | `firmware_observed` | `firmware_target`, `result_outcome`; the physical identifiers above are absent or `null` |

- `experimentally_confirmed` is reserved for physical hardware. A firmware result cannot carry it, and a physical package cannot carry `firmware_observed`.
- A firmware result establishes what the executed firmware produced under the recorded harness conditions (for example an ACK, or bytes written toward a simulated bus interface). It does not establish what a physical actuator does.
- `sub_bus_id` may be `null` only in firmware packages. The earlier relaxation to `null` for physical packages was not intended and is reverted.

### Firmware reproducibility context (`firmware_target`)

A firmware package identifies its experiment with the keys of the own-firmware-oracle result header (`oracle/record.py` `HEADER_KEYS`), plus the path of the original result file. All are required:

| Key | Meaning |
| :--- | :--- |
| `product`, `version`, `image_sha256` | Product, firmware version, SHA-256 of the exact firmware artifact |
| `harness`, `target_sha256` | `full` or `unit:<program>`, and the digest of the executed target |
| `adapter` | `<name>-<version>` of the execution adapter (pty, shim, system emulation) |
| `reset`, `bus`, `framer`, `responder`, `settle_ms` | Reset policy, simulated bus, framing, responder and settling policy |
| `suite`, `suite_sha256`, `oracle_version` | Suite identity, digest and oracle revision |
| `source_result` | Path of the original oracle result file |

For firmware packages `environment` is optional; `firmware_target.bus` describes the simulated bus where `environment.bus_topology` describes a physical one.

### Inconclusive and zero-frame results

`result_outcome` is required for firmware packages. `supported` needs at least one claim and may have `frame_count: 0` (for example a documented silence). `inconclusive` (startup failure, unresolved silence) carries no claim and a required `inconclusive_reason`. Physical packages keep the positive `frame_count` and non-empty `claims_supported` requirements.

### Tests

```
python -m pytest evidence/tests
python evidence/validate_evidence.py
```

## Packaged Evidence Index

| Evidence ID | Capture Directory | Hardware & Firmware | Kind | Epistemic Status | Frames | Primary Claims & Boundaries Established |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **`EVID-MH200-F414-DIM1`** | [`cap-mh200-f414-dimmer-20260926`](cap-mh200-f414-dimmer-20260926) | BTicino F414 modular dimmer on MH200 (FW 2.1.0) | Controlled experiment | `experimentally_confirmed` | 18 | F414 utilizes Dimension 1 status queries (`*#1*99*1##` &rarr; `*#1*99*1*200*2##`), accepts fine-grained Dimension 1 writes (`*#1*99*#1*150*0##` &rarr; `*#1*99*1*150*5##`), and internally maps discrete levels to Dimension 1 levels (10&rarr;200, 9&rarr;174, 8&rarr;163, 50%&rarr;WHAT 7). Dimension 4 is neither sent nor tested; open question `q000025` remains open. |
| **`EVID-MH200-F418U2-DIM1`** | [`cap-mh200-f418u2-dimmer-20260927`](cap-mh200-f418u2-dimmer-20260927) | BTicino F418U2 universal dimmer on MH200 (FW 2.1.0) | Controlled experiment | `experimentally_confirmed` | 30 | F418U2 accepts fine Dimension 1 brightness writes (`*#1*62*#1*150*0##` &rarr; `*#1*62*1*150*5##`), preserves non-linear WHAT-to-percentage dimming curves (Level 3&rarr;10%, Level 5&rarr;30%), and answers Dimension 1 queries when OFF (`*#1*62*1##` &rarr; `*#1*62*1*100*2##`). On this MH200 path, Dimension 4 queries and writes elicit no RX reply (query sits ~123s with no reply/NACK; write produces no reply and leaves Dimension 1 unchanged at 150), supporting 'no observable Dimension 4 effect on this path' (`q000024`). |
| **`EVID-MH200-F422-SCOPE`** | [`cap-mh200-f422-scope-20260923`](cap-mh200-f422-scope-20260923) | BTicino F422 interface router (`02`) on MH200 (FW 2.1.0) | Controlled experiment | `observed` | 9 | Area scope command (`*2*1*1#4#02##`) receives gateway socket ACK (`*#*1##`), but produces no cover movement or event from interface 02. In contrast, point command (`*2*1*11#4#02##`) is echoed and results in actuator movement ending in STOP after 60.9s run-time. Area status requests (`*#2*1#4#02##`) are answered per-point behind the interface. |
| **`EVID-MH200-WHAT19-FAULT`** | [`cap-mh200-what19-fault-20260924`](cap-mh200-what19-fault-20260924) | BTicino Lighting Actuator (WHERE 74) on MH200 (FW 2.1.0) | Active observation | `observed` | 3 | Querying an actuator in an anomaly state (`*#1*74##`) returns WHAT 19 (`*1*19*74##`) co-occurring with WHO 1001 autodiagnostic bitmask `*#1001*74*11*111110111111111111110111##` (bits 6 and 21 cleared). Proves WHAT 19 is an unmapped status code emitted alongside autodiagnostics, not a published ON state. |

---

## Machine KB Citation & Evidence Chain

Following Discussion #509, claims in the Encyclopedia and Machine KB cite these packages to establish empirical provenance:

```markdown
> **Evidence**: [`EVID-MH200-F418U2-DIM1`](../../evidence/cap-mh200-f418u2-dimmer-20260927/manifest.json)
> - **Hardware**: BTicino F418U2 universal dimmer via MH200 gateway (FW 2.1.0)
> - **Epistemic Standing**: `experimentally_confirmed`
> - **Frames**: 30 frames with millisecond relative offsets
> - **Supports**: [`ownkb:claim:c007524`](../../knowledge/claims/claims.jsonl#L7446)
> - **Informs**: [`ownkb:question:q000024`](../../reverse-engineering/open-questions.md#evidence-priorities)
```

## Reproducibility & Test Recipes

Every `manifest.json` provides a step-by-step `test_recipe` detailing the exact command sequences and expected responses required to reproduce the observation on physical hardware.
