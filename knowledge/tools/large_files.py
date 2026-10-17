"""Fail closed on unhydrated transport pointers; never download during a build."""
from pathlib import Path

POINTER_HEADER = b"version https://git-lfs.github.com/spec/v1\n"
LARGE_FILES = ("knowledge/inputs/claim-records.json", "knowledge/claims/claims.jsonl")


def require_hydrated(path: Path) -> None:
    if not path.is_file():
        return
    with path.open("rb") as stream:
        prefix = stream.read(len(POINTER_HEADER))
    if prefix == POINTER_HEADER:
        raise ValueError(f"{path}: unhydrated Git LFS pointer. Run git lfs pull before reading or validating the KB; full data is required. Builds never fetch it automatically.")


def require_kb_hydrated(root: Path) -> None:
    for name in LARGE_FILES:
        require_hydrated(root / name)
