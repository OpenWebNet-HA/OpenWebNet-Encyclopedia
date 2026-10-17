"""Conserve prepared Device source units and their reviewed claim dispositions."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from serialization import json_bytes


def source_units(section: dict) -> list[dict]:
    """Headers are part of each row fingerprint; nested lists are never flattened away."""
    units = []

    def walk(block: dict, key: str, index: int) -> None:
        kind = block["type"]
        if kind == "table":
            for number, row in enumerate(block["rows"]):
                data = {"type": "table_row", "header": [c["text"] for c in block["header"]],
                        "cells": [c["text"] for c in row]}
                add(f"{key}:r{number}", index, data)
        elif kind == "list":
            for number, item in enumerate(block["items"]):
                for child, value in enumerate(item["blocks"]):
                    walk(value, f"{key}:i{number}:b{child}", index)
        elif kind == "blockquote":
            for number, value in enumerate(block["blocks"]):
                walk(value, f"{key}:q{number}", index)
        elif kind == "rule":
            return
        elif kind in {"paragraph", "code"}:
            add(key, index, {"type": kind, "text": block["text"]})
        else:
            raise ValueError("unsupported Device source unit: " + kind)

    def add(key: str, index: int, data: dict) -> None:
        units.append({"key": key, "block_index": index, "data": data,
                      "sha256": hashlib.sha256(json_bytes(data)).hexdigest()})

    for index, block in enumerate(section["blocks"]):
        walk(block, f"b{index}", index)
    return units


def validate_device_units(ir: dict, claims: list[dict], path: Path) -> dict:
    documents = [d for d in ir["documents"] if d["path"].startswith("devices/definitions/")]
    if not documents and not path.exists():
        return {"documents": 0, "units": 0, "claimed": 0, "nonclaim": 0}
    value = json.loads(path.read_text(encoding="utf-8"))
    if set(value) != {"format_version", "documents"} or value["format_version"] != "0.1.0":
        raise ValueError("Device unit review has an unsupported shape")
    rows = value["documents"]
    by_path = {row["path"]: row for row in rows}
    if len(by_path) != len(rows) or set(by_path) != {d["path"] for d in documents}:
        raise ValueError("Device unit review selection is stale, duplicate, or incomplete")
    by_id = {claim["id"]: claim for claim in claims}
    context_path = path.with_name("claim-context.json")
    contexts = ({r["id"]: r for r in json.loads(context_path.read_text(encoding="utf-8"))["claims"]}
                if context_path.exists() else None)
    metrics = {"documents": len(documents), "units": 0, "claimed": 0, "nonclaim": 0}
    for doc in documents:
        row = by_path[doc["path"]]
        if set(row) != {"path", "document_id", "sections", "review_note"} or row["document_id"] != doc["id"] or not row["review_note"]:
            raise ValueError("Device unit review document identity or findings are invalid")
        sections = {s["section_id"]: s for s in row["sections"]}
        if len(sections) != len(row["sections"]) or set(sections) != {s["id"] for s in doc["sections"]}:
            raise ValueError("Device unit review sections are incomplete")
        for section in doc["sections"]:
            reviewed = sections[section["id"]]
            digest = hashlib.sha256(json_bytes(section)).hexdigest()
            if set(reviewed) != {"section_id", "section_sha256", "units"} or reviewed["section_sha256"] != digest:
                raise ValueError("Device unit review source changed; review before repinning")
            expected = {u["key"]: u for u in source_units(section)}
            dispositions = {u["key"]: u for u in reviewed["units"]}
            if len(dispositions) != len(reviewed["units"]) or set(dispositions) != set(expected):
                raise ValueError("Device source units were omitted, duplicated, or added")
            for key, unit in dispositions.items():
                if set(unit) != {"key", "sha256", "status", "claim_ids", "reason"} or unit["sha256"] != expected[key]["sha256"]:
                    raise ValueError("Device source unit or table headers changed")
                if unit["status"] not in {"claimed", "nonclaim"} or not unit["reason"]:
                    raise ValueError("Device source unit lacks a reviewed disposition")
                identities = unit["claim_ids"]
                if not isinstance(identities, list) or len(set(identities)) != len(identities):
                    raise ValueError("Device source unit has invalid claim identities")
                if (unit["status"] == "claimed") != bool(identities):
                    raise ValueError("Device source unit disposition disagrees with its claims")
                for identity in identities:
                    claim = by_id.get(identity)
                    if not claim or not any(p["location"]["section_id"] == section["id"] for p in claim["provenance"]):
                        raise ValueError("Device source unit has a missing or wrongly scoped claim")
                    if contexts is not None:
                        context = contexts.get(identity, {})
                        if any(context.get(k, {}).get("source_unit_key") != key for k in ("atomicity", "evidence")):
                            raise ValueError("Device claim review and unit ledger name different source units")
                if identities:
                    text = " ".join(by_id[identity]["statement"] for identity in identities)
                    normalize = lambda value: re.sub(r"\s+", " ", value).strip()
                    data = expected[key]["data"]
                    values = data["cells"] if data["type"] == "table_row" else [data["text"]]
                    if any(normalize(v) not in normalize(text) for v in values if v.strip()):
                        raise ValueError("Device claim lost source-cell content or governing qualification")
                metrics["units"] += 1
                metrics[unit["status"]] += 1
        mapped = {identity for s in row["sections"] for u in s["units"] for identity in u["claim_ids"]}
        emitted = {c["id"] for c in claims if any(p["location"]["document_id"] == doc["id"] for p in c["provenance"])}
        if mapped != emitted:
            raise ValueError("Device claims and source-unit review disagree")
    return metrics
