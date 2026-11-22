#!/usr/bin/env python3
"""Inventory pinned retained traffic separately from oracle and test expectations.

Read-only with respect to both source repositories. No raw log lines or device
metadata are copied into the output. Counts are literal payload occurrences, not
deduplicated physical events or an independent certification of capture origin.
"""
from __future__ import annotations

import argparse
import ast
from collections import Counter
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
import subprocess

MYHOME_REV = "a881a4be711e7b8f03f044505c3810cfffcad403"
OWND_REV = "d04e453ea99b2b5dcaf36b2bfccc073eda522c48"
ORACLE_REV = "3c1634b00f8b165d1f63ddd4289171a9826ff501"
FRAME = re.compile(r"\*#4\*[^*\r\n]*\*(?:19|#?20)(?:\*[^#\r\n]*)?##")
EXTENSIONS = {".json", ".jsonl", ".log", ".txt"}
RANGES = {"10..13": range(10, 14), "14..16": range(14, 17),
          "17..22": range(17, 23), "101..200": range(101, 201)}
META_KEYS = {"capture", "gateway", "environment", "_source", "telemetry",
             "oracle", "meta", "metadata"}


def git(root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(root), *args])


def literal_frames(value):
    if isinstance(value, str):
        if FRAME.fullmatch(value.strip()):
            yield value.strip()
    elif isinstance(value, list):
        for item in value:
            yield from literal_frames(item)
    elif isinstance(value, dict):
        for key, item in value.items():
            if key not in META_KEYS:
                yield from literal_frames(item)


def values(frame: str) -> list[int]:
    # Read requests have no payload; DIMENSION 19 has CV and HV, not one value.
    return [int(v) for v in frame[2:-2].split("*")[3:]
            if re.fullmatch(r"[0-9]+", v)]


def classification(path: str, data) -> str:
    capture = data.get("capture", {}) if isinstance(data, dict) else {}
    if (isinstance(data, dict) and data.get("synthetic") is True
            or capture.get("synthetic") is True
            or "synthetic" in str(capture.get("kind", "")).lower()
            or "oracle" in path.lower()):
        return "synthetic_or_oracle"
    if (isinstance(data, dict) and data.get("synthetic") is False
            or capture.get("kind") in {"trace", "sweep", "derived_trace_archive"}):
        return "recorded_capture_as_described"
    return "retained_fixture_or_log_origin_not_independently_certified"


def summary(frames) -> dict:
    frames = list(frames)
    hist = Counter(v for f in frames for v in values(f))
    return {"output_payload_occurrences": sum(bool(values(f)) for f in frames),
            "value_histogram": {str(k): hist[k] for k in sorted(hist)},
            "target_range_occurrences": {k: sum(hist[v] for v in vs)
                                         for k, vs in RANGES.items()}}


def paired_intervals(frames: list[dict]) -> list[dict]:
    """Pair exact actuator/value frames, never merely neighbouring traffic."""
    pairs = []
    for i, write in enumerate(frames):
        raw = write.get("raw", "")
        if not FRAME.fullmatch(raw) or "*#20*" not in raw or not values(raw):
            continue
        expected = raw.replace("*#20*", "*20*", 1)
        reply = next((r for r in frames[i + 1:] if r.get("raw") == expected
                      and Decimal(str(r["timestamp"])) >= Decimal(str(write["timestamp"]))), None)
        if reply is not None:
            parts = raw[2:-2].split("*")
            pairs.append({"where": parts[1], "value": parts[3],
                          "interval_ms": str((Decimal(str(reply["timestamp"]))
                                               - Decimal(str(write["timestamp"]))) * 1000)})
    return pairs


def inventory(root: Path, repository: str, revision: str) -> dict:
    if git(root, "rev-parse", "HEAD").decode().strip() != revision:
        raise ValueError(f"wrong pinned revision: {repository}")
    tree = git(root, "rev-parse", "HEAD^{tree}").decode().strip()
    tracked = {}
    for item in git(root, "ls-tree", "-rz", "--full-tree", "HEAD").split(b"\0"):
        if not item:
            continue
        info, path = item.split(b"\t", 1)
        mode, kind, blob = info.decode().split()
        if kind == "blob" and mode in {"100644", "100755"}:
            tracked[path.decode()] = blob
    rows = []
    for path, blob in sorted(tracked.items()):
        primary = repository.endswith("/MyHOME") and path.startswith("tests/fixtures/") and Path(path).suffix in EXTENSIONS
        derived = (path.startswith("tests/") and Path(path).suffix in {".py", ".yaml", ".json"}
                   and not path.startswith("tests/fixtures/"))
        oracle_context = (repository.endswith("/own-firmware-oracle")
                          and Path(path).suffix in {".py", ".yaml", ".yml", ".json", ".md", ".tsv", ".seq", ".txt"})
        if not primary and not derived and not oracle_context:
            continue
        raw = (root / path).read_bytes()
        actual_blob = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
        if actual_blob != blob:
            raise ValueError(f"checkout differs from pinned blob: {repository}:{path}")
        text = raw.decode("utf-8")
        data = None
        if Path(path).suffix == ".json":
            data = json.loads(text)
        elif Path(path).suffix == ".jsonl":
            data = [json.loads(line) for line in text.splitlines() if line.strip()]
        if primary:
            frames = list(literal_frames(data)) if data is not None else FRAME.findall(text)
            kind = classification(path, data)
        else:
            frames = FRAME.findall(text)
            kind = ("oracle_input_result_or_context_not_live_capture" if oracle_context
                    else "derived_test_or_golden_context_not_live_evidence")
        row = {"path": path, "git_blob": blob, "sha256": hashlib.sha256(raw).hexdigest(),
               "bytes": len(raw), "classification": kind, **summary(frames),
               "text_target_range_occurrences": summary(FRAME.findall(text))["target_range_occurrences"]}
        rows.append(row)
    excerpt = None
    if repository.endswith("/OWNd"):
        path = "tests/test_f461_live_plant.py"
        raw = (root / path).read_bytes()
        module = ast.parse(raw.decode())
        assignment = next(n for n in module.body if isinstance(n, ast.Assign)
                          and any(isinstance(t, ast.Name) and t.id == "GATEWAY_FRAMES" for t in n.targets))
        # Only the expressly recorded gateway frames, not assertions or commands.
        excerpt = {"path": path, "start_line": assignment.lineno,
                   "end_line": assignment.end_lineno,
                   "git_blob": tracked[path], "sha256": hashlib.sha256(raw).hexdigest(),
                   "line_count": len(raw.splitlines()),
                   "classification": "retained_physical_capture_excerpt_as_described",
                   **summary(f for f in ast.literal_eval(assignment.value) if FRAME.fullmatch(f))}
    result = {"repository": repository, "revision": revision, "git_tree": tree,
            "git_tree_contents_sha256": hashlib.sha256(git(root, "cat-file", "tree", tree)).hexdigest(),
            "files": rows, "retained_capture_excerpt": excerpt}
    if repository.endswith("/MyHOME"):
        path = "tests/fixtures/traces/issue_908/myhome_trace_MyHomeServer1_fancoil_dim20_100_2026-11-14.json"
        raw = (root / path).read_bytes()
        if hashlib.sha256(raw).hexdigest() != "2ae9b60d22a30d5dc7a5e8eb91450637922935c699b0256503c122cb44b6a346":
            raise ValueError("timing fixture differs from the original pinned live trace")
        result["live_write_status_pairs"] = paired_intervals(json.loads(raw, parse_float=Decimal)["frames"])
    return result


def audit(myhome: Path, ownd: Path, oracle: Path) -> dict:
    repos = [inventory(myhome, "OpenWebNet-HA/MyHOME", MYHOME_REV),
             inventory(ownd, "OpenWebNet-HA/OWNd", OWND_REV),
             inventory(oracle, "OpenWebNet-HA/own-firmware-oracle", ORACLE_REV)]
    for repo in repos:
        groups = {}
        for row in repo["files"]:
            group = groups.setdefault(row["classification"], {"files": 0, "payload_occurrences": 0,
                                                              "target_range_occurrences": dict.fromkeys(RANGES, 0)})
            group["files"] += 1
            group["payload_occurrences"] += row["output_payload_occurrences"]
            for k, v in row["target_range_occurrences"].items():
                group["target_range_occurrences"][k] += v
        repo["summary"] = groups
    return {"format_version": "1.0.0", "audit_date": "2026-11-21",
            "method": "Pinned tracked-file inventory and literal WHO 4 DIMENSION 19/20/#20 payload scan",
            "repositories": repos,
            "limitations": [
                "Counts are occurrences in retained payloads, not independent or deduplicated physical events.",
                "JSON metadata prose is excluded; requests without output values do not count as reports.",
                "Explicit synthetic/oracle fixtures and derived unit/golden expectations are recorded separately.",
                "Oracle bench fixtures describe virtual plants and emulator results, not new physical observations; the separately named bench capture archive was not identified there.",
                "Capture origin is taken from retained source descriptions; no hardware was operated.",
                "Separate own-bench-captures material was not available and is not covered.",
                "No claim is made about deleted/history-only files, other branches, unretained traffic or future captures."]}


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--myhome", required=True, type=Path)
    p.add_argument("--ownd", required=True, type=Path)
    p.add_argument("--oracle", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    a = p.parse_args()
    result = audit(a.myhome, a.ownd, a.oracle)
    a.output.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2) + "\n")
    print(json.dumps([{k: r[k] for k in ["repository", "revision", "summary", "retained_capture_excerpt"]}
                      for r in result["repositories"]], sort_keys=True))


if __name__ == "__main__":
    main()
