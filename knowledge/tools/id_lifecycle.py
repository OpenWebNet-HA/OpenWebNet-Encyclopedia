"""Validate the public curated-ID lifecycle registry against emitted artifacts."""
from __future__ import annotations
from typing import Iterable
from validate_schema import validate_registry

def emitted_ids(claims: list[dict], chunks: list[dict], references: Iterable[dict]) -> set[str]:
    result = {record["id"] for record in claims}
    result.update(record["id"] for record in chunks)
    result.update(record["document_id"] for record in chunks)
    result.update(record["section_id"] for record in chunks)
    result.update(record["id"] for record in references)
    return result

def validate_lifecycle(registry: dict, current_ids: set[str]) -> dict[str, int]:
    validate_registry(registry)
    canonical = {entry["id"]: entry for entry in registry["ids"]}
    live = {identifier for identifier, entry in canonical.items() if entry["lifecycle"] == "live"}
    inactive = set(canonical) - live
    aliases = {entry["alias"] for entry in registry["aliases"]}
    if live != current_ids:
        missing = sorted(current_ids - live)
        stale = sorted(live - current_ids)
        raise ValueError(f"ID lifecycle live set mismatch: missing={missing[:3]}, stale={stale[:3]}")
    if inactive & current_ids:
        raise ValueError("deprecated or retired ID was emitted as current")
    if aliases & current_ids:
        raise ValueError("alias was emitted as a canonical current ID")
    return {"aliases": len(aliases), "live": len(live), "retired": sum(x["lifecycle"] == "retired" for x in canonical.values())}
