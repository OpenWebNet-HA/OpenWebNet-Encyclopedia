"""Acceptance checks for the evidence-manifest class/status/context contract."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

EVIDENCE_DIR = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((EVIDENCE_DIR / "schema" / "evidence-manifest.schema.json").read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA)
SHA = "a" * 64
COMMIT = "b" * 40


def physical() -> dict:
    path = EVIDENCE_DIR / "cap-mh200-what19-fault-20260924" / "manifest.json"
    return json.loads(path.read_text(encoding="utf-8"))


def firmware() -> dict:
    return {
        "evidence_id": "EVID-MH200N-FW-LIGHT1",
        "capture_id": "cap-mh200n-fw-light1",
        "title": "Firmware oracle light command acknowledgement",
        "capture_kind": "firmware_oracle",
        "epistemic_status": "firmware_observed",
        "confidence": "medium",
        "evidence_class": "firmware_emulation",
        "recorded_at": "2026-10-05T00:00:00Z",
        "installation_id": None,
        "bus_id": None,
        "sub_bus_id": None,
        "gateway_id": None,
        "device_under_test": None,
        "summary": "Firmware acknowledges a light ON command on the simulated bus.",
        "test_recipe": ["1. Run suite light1 against the pinned image."],
        "claims_supported": ["Firmware ACKs *1*1*21##."],
        "frame_count": 2,
        "result_outcome": "supported",
        "firmware_target": {
            "product": "MH200N",
            "version": "1.0.0",
            "image_sha256": SHA,
            "target_config_sha256": SHA,
            "harness": "full",
            "target_sha256": SHA,
            "adapter": "pty-1",
            "reset": "each",
            "bus": "scs-sim",
            "framer": "own",
            "responder": "none",
            "settle_ms": "500",
            "quiet_ms": "50",
            "suite": "light1",
            "suite_sha256": SHA,
            "oracle_version": "1",
            "oracle_commit": COMMIT,
            "source_result": "results/MH200N/010108/checks/lights-level.tsv",
            "source_cases": "oracle/cases/lights-level.cases",
        },
    }


def errors(manifest: dict) -> list[str]:
    return [e.message for e in VALIDATOR.iter_errors(manifest)]


def test_existing_physical_packages_pass() -> None:
    for path in sorted(EVIDENCE_DIR.glob("cap-*/manifest.json")):
        assert errors(json.loads(path.read_text(encoding="utf-8"))) == [], path


def test_complete_firmware_package_passes() -> None:
    assert errors(firmware()) == []


@pytest.mark.parametrize(
    "key",
    [
        "image_sha256",
        "target_config_sha256",
        "harness",
        "target_sha256",
        "adapter",
        "reset",
        "settle_ms",
        "quiet_ms",
        "suite",
        "suite_sha256",
        "oracle_version",
        "oracle_commit",
        "source_result",
        "source_cases",
    ],
)
def test_firmware_rejects_missing_reproducibility_metadata(key: str) -> None:
    m = firmware()
    del m["firmware_target"][key]
    assert errors(m)


def test_firmware_requires_target_block() -> None:
    m = firmware()
    del m["firmware_target"]
    assert errors(m)


@pytest.mark.parametrize(
    "bad_digest",
    [
        SHA[:63],      # too short (63 chars)
        SHA + "a",     # too long (65 chars)
        SHA.upper(),   # uppercase hex rejected
        " " + SHA,     # leading whitespace
        SHA + " ",     # trailing whitespace
        "g" * 64,      # non-hex chars
    ],
)
def test_firmware_rejects_malformed_sha256_digests(bad_digest: str) -> None:
    m = firmware()
    m["firmware_target"]["image_sha256"] = bad_digest
    assert errors(m)


@pytest.mark.parametrize(
    "bad_commit",
    [
        COMMIT[:39],    # too short (39 chars)
        COMMIT + "b",   # too long (41 chars)
        COMMIT.upper(), # uppercase hex rejected
        " " + COMMIT,   # leading whitespace
        COMMIT + " ",   # trailing whitespace
        "g" * 40,       # non-hex chars
    ],
)
def test_firmware_rejects_malformed_git_commit(bad_commit: str) -> None:
    m = firmware()
    m["firmware_target"]["oracle_commit"] = bad_commit
    assert errors(m)


@pytest.mark.parametrize("field", ["product", "version", "adapter", "suite"])
def test_firmware_rejects_whitespace_in_tokens(field: str) -> None:
    m1 = firmware()
    m1["firmware_target"][field] = " " + m1["firmware_target"][field]
    assert errors(m1)

    m2 = firmware()
    m2["firmware_target"][field] = m2["firmware_target"][field] + " "
    assert errors(m2)


@pytest.mark.parametrize("valid_reset", ["each", "batch-1", "batch-10", "0", "1"])
def test_firmware_accepts_valid_reset_policies(valid_reset: str) -> None:
    m = firmware()
    m["firmware_target"]["reset"] = valid_reset
    assert errors(m) == []


@pytest.mark.parametrize("invalid_reset", ["cold", "warm", "batch-0", "batch-", "each ", " 0"])
def test_firmware_rejects_invalid_reset_policies(invalid_reset: str) -> None:
    m = firmware()
    m["firmware_target"]["reset"] = invalid_reset
    assert errors(m)


def test_firmware_cannot_claim_experimental_confirmation() -> None:
    m = firmware()
    m["epistemic_status"] = "experimentally_confirmed"
    assert errors(m)


def test_firmware_rejects_physical_context() -> None:
    m = firmware()
    m["gateway_id"] = "c9c79529-1399-5c4f-ac30-ec3bc466b291"
    assert errors(m)


def test_physical_cannot_use_firmware_status() -> None:
    m = physical()
    m["epistemic_status"] = "firmware_observed"
    assert errors(m)


def test_physical_cannot_use_firmware_capture_kind() -> None:
    m = physical()
    m["capture_kind"] = "firmware_oracle"
    assert errors(m)


def test_physical_rejects_null_sub_bus_id() -> None:
    m = physical()
    m["sub_bus_id"] = None
    assert errors(m)


def test_physical_rejects_firmware_fields() -> None:
    m = physical()
    m["firmware_target"] = firmware()["firmware_target"]
    assert errors(m)


def test_physical_still_needs_a_frame_and_a_claim() -> None:
    m = physical()
    m["frame_count"] = 0
    assert errors(m)
    m = physical()
    m["claims_supported"] = []
    assert errors(m)


def test_firmware_zero_frame_supported_silence_package() -> None:
    """A complete supported package with 0 frames represents intentional silence."""
    m = firmware()
    m.update(
        frame_count=0,
        result_outcome="supported",
        summary="Firmware deliberately ignores and remains silent on unconfigured query.",
        claims_supported=["Firmware remains silent and produces no response on *#1*99##."],
    )
    assert errors(m) == []


def test_firmware_zero_frame_inconclusive_package() -> None:
    """A complete inconclusive package carries an inconclusive_reason and no claims."""
    m = firmware()
    m.update(
        frame_count=0,
        result_outcome="inconclusive",
        summary="Target daemon crashed during initialization before processing inputs.",
        claims_supported=[],
        machine_kb_claims=[],
        inconclusive_reason="Target daemon process crashed during startup initialization.",
    )
    assert errors(m) == []


def test_inconclusive_rejects_supported_claims_and_machine_kb_claims() -> None:
    m = firmware()
    m.update(
        frame_count=0,
        result_outcome="inconclusive",
        claims_supported=[],
        inconclusive_reason="Daemon died before accepting connections.",
    )
    # Having claims_supported in an inconclusive package must be rejected
    bad1 = copy.deepcopy(m)
    bad1["claims_supported"] = ["Some claim"]
    assert errors(bad1)

    # Having machine_kb_claims in an inconclusive package must also be rejected
    bad2 = copy.deepcopy(m)
    bad2["machine_kb_claims"] = ["ownkb:claim:c001234"]
    assert errors(bad2)


def test_supported_firmware_needs_a_claim() -> None:
    m = firmware()
    m["claims_supported"] = []
    assert errors(m)
