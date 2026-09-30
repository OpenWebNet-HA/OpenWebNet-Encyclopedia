# Canonical Field Evidence Repository

This directory contains canonical, privacy-preserving real-world OpenWebNet evidence packages collected from physical hardware installations, conforming to the RFC #536 and Discussion #509 evidence model.

## Evidence Model & Privacy Architecture

Each capture package is self-contained in its own directory:

```
evidence/
└── <capture_id>/
    ├── manifest.json       # Metadata, hardware environment, test recipe, claims supported
    ├── frames.jsonl        # Ordered frames with relative delta timestamps (t_rel_ms)
    └── privacy.json        # Sanitization profile adhering to privacy-metadata.schema.json
```

### Privacy Contract (RFC #536)
- **Known Identifiers Pseudonymized**: Device addresses, serial numbers, gateway MACs, and private network IPs are converted into stable synthetic pseudonyms (e.g. Legrand OUI `00:03:50` preserved with randomized suffix, RFC 5737 TEST-NET IPs).
- **Unknown Protocol Data Faithfully Preserved**: Undocumented dimensions, parameters, WHAT states, and autodiagnostic bitmasks are preserved exactly as emitted on the physical bus.
- **Relative Chronology**: Timestamps represent relative millisecond offsets (`t_rel_ms`) from the start of the observation window, preventing leakage of absolute wall-clock activity schedules while preserving exact frame timing relationships.

---

## Packaged Evidence Index

| Evidence ID | Capture Directory | Hardware & Firmware | Kind | Epistemic Status | Primary Claims Established |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **`EVID-MH200-F414-DIM1`** | [`cap-mh200-f414-dimmer-20260926`](cap-mh200-f414-dimmer-20260926) | BTicino F414 modular dimmer on MH200 (FW 2.1.0) | Controlled experiment | `experimentally_confirmed` | Classic 10-level dimmers utilize Dimension 1 query/event (`*#1*WHERE*1##`) and discrete Level 1..10 commands (`*1*WHAT*WHERE##`), but ignore Dimension 4. |
| **`EVID-MH200-F418U2-DIM1`** | [`cap-mh200-f418u2-dimmer-20260927`](cap-mh200-f418u2-dimmer-20260927) | BTicino F418U2 universal dimmer on MH200 (FW 2.1.0) | Controlled experiment | `experimentally_confirmed` | F418U2 accepts fine Dimension 1 brightness writes (`*#1*WHERE*#1*LEVEL*SPEED##`), preserves non-linear WHAT-to-percentage dimming curves, answers Dimension 1 queries when OFF, and ignores Dimension 4 writes. |
| **`EVID-MH200-F422-SCOPE`** | [`cap-mh200-f422-scope-20260923`](cap-mh200-f422-scope-20260923) | BTicino F422 interface router (`02`) on MH200 (FW 2.1.0) | Controlled experiment | `experimentally_confirmed` | General and Area scope commands (`*2*1*1#4#02##`) do NOT cross the F422 router despite syntactically valid grammar. Only point commands (`*2*1*11#4#02##`) cross. Scope status requests are answered per-object behind the interface. |
| **`EVID-MH200-WHAT19-FAULT`** | [`cap-mh200-what19-fault-20260924`](cap-mh200-what19-fault-20260924) | BTicino Lighting Actuator on MH200 (FW 2.1.0) | Active observation | `observed` | Lighting WHAT 19 is an autodiagnostic fault state emitted alongside WHO 1001 autodiagnostic mask `*#1001*WHERE*11*MASK##`, not an 'ON' state. |
| **`EVID-MH200-SWEEP-001`** | [`cap-mh200-sweep-20260911`](cap-mh200-sweep-20260911) | BTicino MH200 Gateway (FW 2.0.0, WHO 13 type 4) | Diagnostic sweep | `observed` | Full authentic baseline interrogation across WHO 13 (clock, model, firmware), WHO 1 (lights), WHO 2 (covers), WHO 4 (thermo), WHO 5 (alarm), and WHO 16 (audio). |

---

## Machine KB Citation Format

Claims in the Encyclopedia and Machine KB cite these packages using standard evidence provenance:

```markdown
> **Evidence**: [`EVID-MH200-F418U2-DIM1`](../../evidence/cap-mh200-f418u2-dimmer-20260927/manifest.json)
> - **Hardware**: BTicino F418U2 universal dimmer via MH200 gateway (FW 2.1.0)
> - **Epistemic Standing**: `experimentally_confirmed`
> - **Frames**: 30 frames with millisecond relative offsets
```
