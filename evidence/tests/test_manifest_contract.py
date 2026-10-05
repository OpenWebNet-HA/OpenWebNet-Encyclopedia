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
            "product": "MH200N", "version": "1.0.0", "image_sha256": SHA,
            "harness": "full", "target_sha256": SHA, "adapter": "pty-1",
            "reset": "cold", "bus": "scs-sim", "framer": "own", "responder": "none",
            "settle_ms": "500", "suite": "light1", "suite_sha256": SHA,
            "oracle_version": "1", "source_result": "MH200N/1.0.0/oracle/full/light1.tsv",
        },
    }


def errors(manifest: dict) -> list[str]:
    return [e.message for e in VALIDATOR.iter_errors(manifest)]


def test_existing_physical_packages_pass() -> None:
    for path in sorted(EVIDENCE_DIR.glob("cap-*/manifest.json")):
        assert errors(json.loads(path.read_text(encoding="utf-8"))) == [], path


def test_complete_firmware_package_passes() -> None:
    assert errors(firmware()) == []


@pytest.mark.parametrize("key", ["image_sha256", "suite_sha256", "harness", "reset", "settle_ms", "source_result"])
def test_firmware_rejects_missing_reproducibility_metadata(key: str) -> None:
    m = firmware()
    del m["firmware_target"][key]
    assert errors(m)


def test_firmware_requires_target_block() -> None:
    m = firmware()
    del m["firmware_target"]
    assert errors(m)


def test_firmware_rejects_bad_digest() -> None:
    m = firmware()
    m["firmware_target"]["image_sha256"] = "abc"
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


def test_firmware_zero_frame_supported_silence_is_allowed() -> None:
    m = firmware()
    m["frame_count"] = 0
    assert errors(m) == []


def test_inconclusive_run_needs_reason_and_no_claim() -> None:
    m = firmware()
    m.update(result_outcome="inconclusive", claims_supported=[], frame_count=0)
    assert errors(m)
    m["inconclusive_reason"] = "Image failed to boot; no output captured."
    assert errors(m) == []
    bad = copy.deepcopy(m)
    bad["claims_supported"] = ["claim"]
    assert errors(bad)


def test_supported_firmware_needs_a_claim() -> None:
    m = firmware()
    m["claims_supported"] = []
    assert errors(m)
