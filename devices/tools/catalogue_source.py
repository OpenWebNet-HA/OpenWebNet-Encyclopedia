#!/usr/bin/env python3
from __future__ import annotations

import atexit
import hashlib
import subprocess
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
LOCAL_DB = ROOT / "sources" / "myhome-suite" / "3.5.38" / "databases" / "MHCatalogue.db"
MANIFEST = ROOT / "sources" / "manifest.yaml"
FETCH_HELPER = Path("/usr/local/sbin/openwebnet-r2-data-fetch")
_cached: Path | None = None


def _entry() -> dict:
    data = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    for entry in data["source_sets"]["myhome-suite-3.5.38"]["files"]:
        if entry["id"] == "myhome-suite-3.5.38-mhcatalogue":
            return entry
    raise RuntimeError("MHCatalogue entry missing from source manifest")


def _verify(path: Path, entry: dict) -> None:
    content = path.read_bytes()
    digest = hashlib.sha256(content).hexdigest()
    if digest != entry["sha256"].lower() or len(content) != entry["size"]:
        raise RuntimeError("MHCatalogue fingerprint mismatch")


def catalogue_path() -> Path:
    global _cached
    entry = _entry()

    if LOCAL_DB.is_file():
        _verify(LOCAL_DB, entry)
        return LOCAL_DB

    if _cached is not None and _cached.is_file():
        return _cached

    if not FETCH_HELPER.is_file():
        raise RuntimeError(
            "MHCatalogue is private archive material; maintainer fetch helper is unavailable"
        )

    proc = subprocess.run(
        ["sudo", "-n", str(FETCH_HELPER), entry["sha256"].lower()],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode:
        raise RuntimeError(
            proc.stderr.decode("utf-8", errors="replace").strip()
            or "MHCatalogue private-archive fetch failed"
        )

    fd, name = tempfile.mkstemp(prefix="openwebnet-mhcatalogue-", suffix=".db")
    path = Path(name)
    try:
        with open(fd, "wb", closefd=True) as f:
            f.write(proc.stdout)
        _verify(path, entry)
    except Exception:
        path.unlink(missing_ok=True)
        raise

    _cached = path
    atexit.register(lambda: path.unlink(missing_ok=True))
    return path
