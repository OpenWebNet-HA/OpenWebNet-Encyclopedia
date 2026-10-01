#!/usr/bin/env python3
"""Deterministic integrity checks for the external artifact inventory."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import yaml


SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
LANG_RE = re.compile(r"^(?:[a-z]{2}|mul|und)$")
FORBIDDEN_TRACKED_SUFFIXES = {
    ".pdf", ".exe", ".msi", ".fwz", ".db", ".db3", ".sqlite",
    ".bin", ".img", ".hex", ".cab", ".7z", ".rar",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def expected_key(artifact: dict) -> str:
    digest = artifact["sha256"]
    key = f"sha256/{digest[:2]}/{digest[2:4]}/{digest}"
    if artifact["kind"] == "documentation":
        key += ".pdf"
    return key


def tracked_files(root: Path) -> list[str]:
    proc = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [p.decode("utf-8") for p in proc.stdout.split(b"\0") if p]


def main() -> int:
    root = Path(__file__).resolve().parents[3]
    artifact_path = root / "sources" / "artifact-manifest.yaml"
    source_path = root / "sources" / "manifest.yaml"
    pdf_path = root / "sources" / "archive" / "pdf-manifest.json"

    errors: list[str] = []
    manifest = yaml.safe_load(artifact_path.read_text(encoding="utf-8"))
    artifacts = manifest.get("artifacts", [])

    ids: set[str] = set()
    by_hash: dict[str, dict] = {}

    for artifact in artifacts:
        aid = artifact.get("id")
        if not isinstance(aid, str) or not aid:
            fail(errors, "artifact has missing/invalid id")
            continue
        if aid in ids:
            fail(errors, f"duplicate artifact id: {aid}")
        ids.add(aid)

        digest = artifact.get("sha256")
        if not isinstance(digest, str) or not SHA256_RE.fullmatch(digest):
            fail(errors, f"{aid}: invalid lowercase SHA-256")
            continue
        if digest in by_hash:
            fail(errors, f"{aid}: duplicate byte identity already represented by {by_hash[digest]['id']}")
        else:
            by_hash[digest] = artifact

        size = artifact.get("size")
        if not isinstance(size, int) or size <= 0:
            fail(errors, f"{aid}: invalid size")

        storage = artifact.get("storage")
        if not isinstance(storage, dict):
            fail(errors, f"{aid}: missing storage metadata")
            continue
        if storage.get("object_key") != expected_key(artifact):
            fail(errors, f"{aid}: object key does not match SHA-256 layout")

        kind = artifact.get("kind")
        bucket = storage.get("bucket")
        visibility = storage.get("visibility")

        if kind == "documentation":
            if bucket != "openwebnet-documents" or visibility != "public":
                fail(errors, f"{aid}: documentation must use public openwebnet-documents")
            public_url = storage.get("public_url")
            if not isinstance(public_url, str) or not public_url.endswith(storage["object_key"]):
                fail(errors, f"{aid}: documentation public_url/object_key mismatch")
            languages = artifact.get("language")
            if not isinstance(languages, list) or not languages:
                fail(errors, f"{aid}: documentation requires language metadata")
            else:
                for code in languages:
                    if not isinstance(code, str) or not LANG_RE.fullmatch(code):
                        fail(errors, f"{aid}: invalid language code {code!r}")
            if not artifact.get("language_evidence"):
                fail(errors, f"{aid}: missing language_evidence")
        elif kind in {"reference-data", "support-data"}:
            if bucket != "openwebnet-data" or visibility != "private":
                fail(errors, f"{aid}: data must use private openwebnet-data")
            if "public_url" in storage:
                fail(errors, f"{aid}: private data must not expose public_url")
        elif kind in {"software-installer", "firmware"}:
            if bucket != "openwebnet-software" or visibility != "private":
                fail(errors, f"{aid}: software must use private openwebnet-software")
            if artifact.get("redistribution_status") != "private-archive-only":
                fail(errors, f"{aid}: software redistribution_status must be private-archive-only")
            if "public_url" in storage:
                fail(errors, f"{aid}: private software must not expose public_url")
        else:
            fail(errors, f"{aid}: unsupported artifact kind {kind!r}")

        repo_history = artifact.get("repository_history")
        if repo_history is not None:
            paths = repo_history.get("former_paths") if isinstance(repo_history, dict) else None
            if not isinstance(paths, list) or not paths or not all(isinstance(p, str) and p for p in paths):
                fail(errors, f"{aid}: invalid repository_history.former_paths")

        if "former_paths" in artifact:
            fail(errors, f"{aid}: legacy top-level former_paths is not allowed")

    pdf_manifest = json.loads(pdf_path.read_text(encoding="utf-8"))
    for entry in pdf_manifest.get("documents", []):
        digest = entry["sha256"].lower()
        artifact = by_hash.get(digest)
        if artifact is None:
            fail(errors, f"pdf-manifest: SHA {digest} absent from artifact manifest")
            continue
        if artifact.get("kind") != "documentation":
            fail(errors, f"pdf-manifest: SHA {digest} is not documentation")
            continue
        if artifact.get("size") != entry.get("size"):
            fail(errors, f"pdf-manifest: size mismatch for {entry['filename']}")
        storage = artifact.get("storage", {})
        for key in ("object_key", "public_url"):
            if storage.get(key) != entry.get(key):
                fail(errors, f"pdf-manifest: {key} mismatch for {entry['filename']}")
        former = artifact.get("repository_history", {}).get("former_paths", [])
        if entry.get("former_path") not in former:
            fail(errors, f"pdf-manifest: former path missing for {entry['filename']}")

    sources = yaml.safe_load(source_path.read_text(encoding="utf-8"))
    suite = sources["source_sets"]["myhome-suite-3.5.38"]

    for entry in suite["files"]:
        artifact = next((a for a in artifacts if a.get("id") == entry["id"]), None)
        if artifact is None:
            fail(errors, f"sources/manifest.yaml: missing artifact {entry['id']}")
            continue
        if artifact.get("sha256") != entry["sha256"].lower():
            fail(errors, f"{entry['id']}: SHA mismatch with sources/manifest.yaml")
        if artifact.get("size") != entry["size"]:
            fail(errors, f"{entry['id']}: size mismatch with sources/manifest.yaml")
        if artifact.get("storage", {}).get("object_key") != entry.get("object_key"):
            fail(errors, f"{entry['id']}: object key mismatch with sources/manifest.yaml")

    installer = suite["installer"]
    installer_artifact = next(
        (a for a in artifacts if a.get("id") == "myhome-suite-3.5.38-installer"),
        None,
    )
    if installer_artifact is None:
        fail(errors, "missing MyHOME Suite installer artifact")
    else:
        if installer_artifact.get("sha256") != installer["sha256"].lower():
            fail(errors, "MyHOME Suite installer SHA mismatch")
        if installer_artifact.get("size") != installer["size"]:
            fail(errors, "MyHOME Suite installer size mismatch")
        if installer_artifact.get("storage", {}).get("object_key") != installer.get("object_key"):
            fail(errors, "MyHOME Suite installer object key mismatch")

    for rel in tracked_files(root):
        suffix = Path(rel).suffix.lower()
        if suffix in FORBIDDEN_TRACKED_SUFFIXES:
            fail(errors, f"vendor/binary artifact tracked in Git: {rel}")

    if errors:
        for error in errors:
            print("FAIL", error)
        print(f"artifact manifest validation failed ({len(errors)} error(s))")
        return 1

    kinds: dict[str, int] = {}
    for artifact in artifacts:
        kinds[artifact["kind"]] = kinds.get(artifact["kind"], 0) + 1
    print(
        "artifact manifest validation passed:",
        len(artifacts),
        "artifacts;",
        ", ".join(f"{kind}={count}" for kind, count in sorted(kinds.items())),
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
