#!/usr/bin/env python3
"""Reject large ordinary Git blobs without rewriting or rescanning old history."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

MAX_BLOB_BYTES = 5 * 1024 * 1024
BASELINE_PATH = "project/review/checks/git-storage-baseline.json"
POINTER = re.compile(
    rb"version https://git-lfs.github.com/spec/v1\n"
    rb"oid sha256:[0-9a-f]{64}\nsize (?:0|[1-9][0-9]*)\n"
)


def git(root: Path, *args: str, data: bytes | None = None) -> bytes:
    return subprocess.run(["git", *args], cwd=root, input=data,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout


def commit(root: Path, ref: str) -> str:
    return git(root, "rev-parse", "--verify", "--end-of-options", ref + "^{commit}").decode().strip()


def snapshot(root: Path, head: str | None) -> dict[str, str]:
    command = ("ls-tree", "-r", "-z", "--full-tree", head) if head else ("ls-files", "--stage", "-z")
    result = {}
    for row in git(root, *command).split(b"\0"):
        if not row:
            continue
        metadata, path = row.split(b"\t", 1)
        mode, middle, last = metadata.split()
        if not head and last != b"0":
            raise ValueError("Unmerged index entries must be resolved before checking storage")
        if mode == b"160000":  # A submodule commit is not a file blob.
            continue
        result[path.decode("utf-8", "surrogateescape")] = (last if head else middle).decode()
    return result


def object_sizes(root: Path, oids: set[str]) -> dict[str, int]:
    if not oids:
        return {}
    output = git(root, "cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)",
                 data=("\n".join(sorted(oids)) + "\n").encode())
    result = {}
    for row in output.decode().splitlines():
        oid, kind, size = row.split()
        if kind == "blob":
            result[oid] = int(size)
    return result


def legacy_blobs(root: Path, files: dict[str, str], sizes: dict[str, int]) -> dict[str, str]:
    oid = files.get(BASELINE_PATH)
    if oid is None or sizes[oid] > 64 * 1024:
        raise ValueError("Missing or oversized reviewed Git storage baseline")
    value = json.loads(git(root, "cat-file", "blob", oid))
    if (set(value) != {"format_version", "baseline_commit", "reason", "ordinary_blobs"}
            or value["format_version"] != 1
            or not re.fullmatch(r"[0-9a-f]{40}", value["baseline_commit"])
            or not isinstance(value["reason"], str)
            or not isinstance(value["ordinary_blobs"], list)):
        raise ValueError("Invalid reviewed Git storage baseline")
    result = {}
    for item in value["ordinary_blobs"]:
        if (set(item) != {"path", "git_blob", "size_bytes"}
                or not isinstance(item["path"], str) or item["path"] in result
                or item["path"].startswith("/") or ".." in item["path"].split("/")
                or not re.fullmatch(r"[0-9a-f]{40}", item["git_blob"])
                or type(item["size_bytes"]) is not int or item["size_bytes"] <= MAX_BLOB_BYTES):
            raise ValueError("Invalid or duplicated legacy Git blob exception")
        if object_sizes(root, {item["git_blob"]}).get(item["git_blob"]) != item["size_bytes"]:
            raise ValueError("Legacy Git blob exception has an incorrect size")
        result[item["path"]] = item["git_blob"]
    return result


def check_storage(root: Path, head: str | None = None, base: str | None = None) -> list[str]:
    revision = commit(root, head) if head else None
    files = snapshot(root, revision)
    sizes = object_sizes(root, set(files.values()))
    legacy = legacy_blobs(root, files, sizes)
    errors = []
    for path, oid in sorted(files.items()):
        if sizes[oid] > MAX_BLOB_BYTES and legacy.get(path) != oid:
            errors.append(f"{path!r}: ordinary Git blob is {sizes[oid]} bytes; limit is {MAX_BLOB_BYTES}")
        if path.startswith("project/review/") and path.endswith(".tsv"):
            if sizes[oid] > 1024 or not POINTER.fullmatch(git(root, "cat-file", "blob", oid)):
                errors.append(f"{path!r}: review TSV must be a canonical Git LFS pointer in Git")
    if base:
        start, end = commit(root, base), revision or commit(root, "HEAD")
        try:
            git(root, "merge-base", "--is-ancestor", start, end)
        except subprocess.CalledProcessError as error:
            raise ValueError("Storage comparison base must be an ancestor of the checked commit") from error
        oids = set(git(root, "rev-list", "--objects", "--no-object-names", end, "^" + start).decode().splitlines())
        for oid, size in sorted(object_sizes(root, oids).items()):
            if size > MAX_BLOB_BYTES:
                errors.append(f"New history blob {oid}: {size} bytes exceeds {MAX_BLOB_BYTES}; "
                              "removing it in a later commit does not remove its storage cost")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--head", help="Check this committed tree instead of the staged Git index")
    parser.add_argument("--base", help="Also reject oversized new blobs in this ancestor-to-head history range")
    args = parser.parse_args()
    try:
        root = Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
        errors = check_storage(root, args.head, args.base)
    except (ValueError, KeyError, TypeError, subprocess.CalledProcessError) as error:
        print(f"Git storage check failed: {error}", file=sys.stderr)
        return 1
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print("Use Git LFS for large public text artifacts; keep private/vendor archives in their established storage.",
              file=sys.stderr)
        return 1
    print("Git storage check passed: size limit, exact legacy exceptions and review TSV pointers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
