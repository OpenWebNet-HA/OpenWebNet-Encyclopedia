"""Canonical, deterministic JSON and JSONL bytes for Machine KB build products."""
from __future__ import annotations

import json
import unicodedata
from pathlib import Path
from typing import Any, Iterable

SAFE_INTEGER = 9_007_199_254_740_991


def _validate(value: Any) -> None:
    if isinstance(value, str):
        if unicodedata.normalize("NFC", value) != value:
            raise ValueError("non-NFC string")
    elif type(value) is int:
        if not -SAFE_INTEGER <= value <= SAFE_INTEGER:
            raise ValueError("integer outside interoperable range")
    elif isinstance(value, float):
        raise ValueError("floating-point JSON numbers are not permitted")
    elif value is None or isinstance(value, bool):
        return
    elif isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError("JSON object keys must be strings")
            _validate(key)
            _validate(item)
    elif isinstance(value, list):
        for item in value:
            _validate(item)
    else:
        raise ValueError(f"unsupported JSON value type: {type(value).__name__}")


def json_bytes(value: Any) -> bytes:
    """Return UTF-8 NFC compact JSON with one terminating LF."""
    _validate(value)
    return (json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True,
                       separators=(",", ":")) + "\n").encode("utf-8")


def jsonl_bytes(records: Iterable[dict[str, Any]]) -> bytes:
    """Return canonical JSONL, sorted by ASCII stable ID, or zero bytes when empty."""
    values = list(records)
    ids = [record.get("id") for record in values]
    if any(not isinstance(identifier, str) for identifier in ids):
        raise ValueError("JSONL records require string IDs")
    if ids != sorted(set(ids), key=lambda identifier: identifier.encode("ascii")):
        raise ValueError("JSONL records must have unique ASCII-sorted IDs")
    return b"".join(json_bytes(record) for record in values)


def write_bytes(path: Path, content: bytes) -> None:
    """Atomically write exact bytes without using time, random names, or source paths."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(content)
    temporary.replace(path)
