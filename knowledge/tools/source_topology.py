"""Closed, incremental ingestion of accepted Device definitions.

The public device-model area is semantic, rather than a directory constraint.
Device pages keep their original paths and all existing format enums and IDs.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

AREAS = ("protocol", "functional", "diagnostics", "programming", "device-model",
         "internals", "reverse-engineering", "scenario-engine")
DEVICE_PATH = re.compile(r"^devices/definitions/own-dev-(\d{4})-[a-z0-9-]+\.md$")
GATES = {"identity_scope", "claim_evidence", "source_reconciliation",
         "information_architecture", "reader_usefulness", "evidence_limits",
         "presentation", "validation"}


def device_sources(root: Path) -> list[dict]:
    definitions = sorted(str(p.relative_to(root)) for p in (root / "devices/definitions").glob("*.md")
                         if p.name != "README.md")
    inventory = root / "knowledge/inputs/device-sources.json"
    if not inventory.exists():
        if definitions:
            raise ValueError("Device definition inventory is missing")
        return []  # Synthetic fixtures without a Device tree retain the original topology.
    value = json.loads(inventory.read_text(encoding="utf-8"))
    if set(value) != {"format_version", "definitions"} or value["format_version"] != "0.1.0":
        raise ValueError("Device definition inventory has an unsupported shape")
    rows = value["definitions"]
    if not isinstance(rows, list):
        raise ValueError("Device definition inventory must contain an array")
    paths, ids = [], []
    for row in rows:
        if set(row) != {"device_id", "path", "state"}:
            raise ValueError("Device definition inventory has unknown or missing fields")
        match = DEVICE_PATH.fullmatch(row["path"])
        if not match or row["device_id"] != "OWN-DEV-" + match[1]:
            raise ValueError("Device definition path and project identity disagree")
        if row["state"] not in {"pending", "integrated"}:
            raise ValueError("Device definition has an invalid ingestion state")
        paths.append(row["path"])
        ids.append(row["device_id"])
    if sorted(paths) != definitions or len(set(paths)) != len(paths) or len(set(ids)) != len(ids):
        raise ValueError("Device definition inventory is stale, duplicate, or incomplete")
    selected = [row for row in rows if row["state"] == "integrated"]
    if selected:
        import yaml
        queue = yaml.safe_load((root / "devices/work-queue.yaml").read_text(encoding="utf-8"))
        outcomes = {}
        for item in queue["items"].values():
            for identity in item.get("outcome", {}).get("device_ids", []):
                if identity in outcomes:
                    raise ValueError("Device has duplicate work-queue outcomes")
                outcomes[identity] = item
        for row in selected:
            item = outcomes.get(row["device_id"], {})
            review = item.get("review", {})
            gate = review.get("review_gate", {})
            if (item.get("state") != "reviewed" or review.get("final_review") != "complete"
                    or set(gate) != GATES or any(v != "complete" for v in gate.values())):
                raise ValueError("Device ingestion requires an accepted eight-check review: " + row["device_id"])
    return rows


def canonical_paths(root: Path) -> list[str]:
    paths = [str(p.relative_to(root)) for area in AREAS for p in (root / area).rglob("*.md")]
    paths.extend(row["path"] for row in device_sources(root) if row["state"] == "integrated")
    return sorted(paths)


def semantic_area(path: str) -> str:
    return "device-model" if DEVICE_PATH.fullmatch(path) else path.split("/", 1)[0]
