#!/usr/bin/env python3
"""Run the private catalogue gate locally; verify its exact-candidate GitHub result in CI."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
REPOSITORY = "OpenWebNet-HA/OpenWebNet-Encyclopedia"
CONTEXT = "Device catalogue validation"
VALIDATOR = "anotherjulien"
PREFIX = "catalogue-inputs-sha256="


def input_digest(root: Path) -> str:
    """Include gate code, index, acceptance ledger, definitions and registered source metadata."""
    paths = {p for p in (root / "devices").rglob("*")
             if p.is_file() and p.suffix in {".py", ".md", ".yaml", ".json"}}
    paths.update(root / name for name in (
        "sources/manifest.yaml", "sources/artifact-manifest.yaml", "check.py",
        ".github/workflows/machine-kb.yml"))
    digest = hashlib.sha256()
    for path in sorted(paths, key=lambda p: p.relative_to(root).as_posix()):
        if root.resolve() not in path.resolve().parents:
            raise ValueError("Catalogue validation input escapes the repository")
        name = path.relative_to(root).as_posix()
        digest.update(name.encode() + b"\0" + hashlib.sha256(path.read_bytes()).digest())
    return digest.hexdigest()


def commit_id(value: str) -> str:
    if not re.fullmatch(r"[0-9a-f]{40}", value):
        raise ValueError("Catalogue validation needs a complete commit SHA")
    return value


def validate_proof(proof: dict, commit: str, root: Path | None = None) -> None:
    root = root or ROOT
    if set(proof) != {"commit", "creator", "state", "context", "description"}:
        raise ValueError("Catalogue status proof has an unsupported shape")
    if proof["commit"] != commit_id(commit) or proof["creator"] != VALIDATOR:
        raise ValueError("Catalogue result is not from the authorized validator for this exact commit")
    if proof["context"] != CONTEXT or proof["state"] != "success":
        raise ValueError("Private catalogue validation has not passed")
    if proof["description"] != PREFIX + input_digest(root):
        raise ValueError("Catalogue validation inputs changed; run the private gate again")


def gh(arguments: list[str], body: dict | None = None) -> str:
    process = subprocess.run(["gh", arguments[0], "--hostname", "github.com", *arguments[1:]], cwd=ROOT, text=True,
                             input=json.dumps(body) if body is not None else None,
                             capture_output=True, check=False)
    if process.returncode:
        raise ValueError("GitHub catalogue status access failed; check repository authentication and status permissions")
    return process.stdout


def post_status(commit: str, state: str, description: str) -> None:
    gh(["api", "--method", "POST", f"repos/{REPOSITORY}/statuses/{commit}", "--input", "-"],
       {"state": state, "context": CONTEXT, "description": description,
        "target_url": f"https://github.com/{REPOSITORY}/commit/{commit}"})


def require_clean_commit(commit: str) -> None:
    head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    dirty = subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True).strip()
    if head != commit or dirty:
        raise ValueError("Run the private gate from the clean checkout of the exact published commit")


def validate_local(commit: str, publish: bool) -> None:
    from catalogue_source import catalogue_path
    require_clean_commit(commit)
    before = input_digest(ROOT)
    path = catalogue_path()  # Verifies registered SHA-256 and byte length before use.
    if publish:
        if json.loads(gh(["api", "user"]))["login"] != VALIDATOR:
            raise ValueError("Publishing requires the explicitly authorized catalogue validator account")
        post_status(commit, "pending", "Private catalogue validation is running")
    commands = [
        [sys.executable, "devices/tools/check-device-definitions.py", "--database", str(path)],
        [sys.executable, "-m", "unittest", "discover", "-s", "devices/tools/tests", "-v"],
    ]
    environment = dict(os.environ, OPENWEBNET_CATALOGUE_PATH=str(path))
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, env=environment, capture_output=True, text=True)
        if result.returncode:
            if publish:
                post_status(commit, "failure", "Private catalogue validation failed")
            raise ValueError("Private catalogue gate failed; inspect locally without publishing source contents")
    require_clean_commit(commit)
    if input_digest(ROOT) != before:
        raise ValueError("Catalogue validation inputs changed during the run")
    if publish:
        post_status(commit, "success", PREFIX + before)
    print("Private source fingerprint, Device completeness and catalogue regressions passed for " + commit)


def verify_remote(commit: str, output: Path, wait_seconds: int) -> None:
    deadline = time.monotonic() + wait_seconds
    while True:
        rows = json.loads(gh(["api", "--paginate", "--slurp",
                              f"repos/{REPOSITORY}/commits/{commit}/statuses?per_page=100"]))
        latest = next((s for page in rows for s in page if s["context"] == CONTEXT), None)
        if latest and latest["state"] != "pending":
            proof = {"commit": commit, "creator": latest["creator"]["login"],
                     "state": latest["state"], "context": latest["context"],
                     "description": latest["description"]}
            validate_proof(proof, commit)
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(json.dumps(proof, sort_keys=True) + "\n")
            print("Authorized exact-commit catalogue result matches all current gate inputs.")
            return
        if time.monotonic() >= deadline:
            raise ValueError("Private catalogue result is missing or pending; run the local gate for this exact commit")
        print("Waiting for the required exact-commit catalogue result.", flush=True)
        time.sleep(min(20, max(0, deadline - time.monotonic())))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    local = sub.add_parser("validate-local")
    local.add_argument("--commit", required=True)
    local.add_argument("--publish", action="store_true")
    remote = sub.add_parser("verify")
    remote.add_argument("--commit", required=True)
    remote.add_argument("--output", type=Path, required=True)
    remote.add_argument("--wait-seconds", type=int, default=600)
    args = parser.parse_args()
    try:
        commit = commit_id(args.commit)
        if args.mode == "validate-local":
            validate_local(commit, args.publish)
        else:
            verify_remote(commit, args.output, args.wait_seconds)
    except (OSError, RuntimeError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, str(error) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
