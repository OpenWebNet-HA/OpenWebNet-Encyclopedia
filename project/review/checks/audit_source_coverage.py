#!/usr/bin/env python3
"""Read-only Phase 3 evidence probes; prints reproducible JSON, not protocol verdicts.

Run from the repository root. Requires PyYAML. No network or Device access.
"""
import hashlib
import json
import sqlite3
import subprocess
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
SOURCES = ROOT / "sources"
FETCH_HELPER = Path("/usr/local/sbin/openwebnet-r2-data-fetch")


def materialize(entry, directory):
    if not FETCH_HELPER.is_file():
        raise RuntimeError(f"private artifact fetch helper unavailable: {FETCH_HELPER}")
    target = directory / Path(entry["path"]).name
    proc = subprocess.run(
        ["sudo", "-n", str(FETCH_HELPER), entry["sha256"].lower()],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode:
        raise RuntimeError(proc.stderr.decode("utf-8", errors="replace").strip() or "private artifact fetch failed")
    target.write_bytes(proc.stdout)
    content = target.read_bytes()
    digest = hashlib.sha256(content).hexdigest()
    if digest != entry["sha256"].lower() or len(content) != entry["size"]:
        raise RuntimeError(f"materialized artifact fingerprint mismatch: {entry['id']}")
    return target


def connect(path):
    conn = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def rows(conn, sql):
    return [dict(row) for row in conn.execute(sql)]


def main():
    manifest = yaml.safe_load((SOURCES / "manifest.yaml").read_text())
    output = {"fingerprints": [], "databases": {}}
    failures = []

    with tempfile.TemporaryDirectory(prefix="openwebnet-private-evidence-") as tmp:
        tempdir = Path(tmp)
        materialized = {}

        for source_set in manifest["source_sets"].values():
            for entry in source_set["files"]:
                if entry.get("storage") == "private-r2":
                    try:
                        path = materialize(entry, tempdir)
                        materialized[Path(entry["path"]).name] = path
                        digest = hashlib.sha256(path.read_bytes()).hexdigest()
                        output["fingerprints"].append({
                            "path": entry["path"],
                            "sha256": digest,
                            "verified": True,
                            "storage": "private-r2",
                        })
                    except Exception as exc:
                        failures.append(entry["path"] + ": " + str(exc))
                    continue

                path_value = entry.get("path", "")
                if path_value.startswith(("http://", "https://")):
                    output["fingerprints"].append({
                        "path": path_value,
                        "sha256": entry["sha256"].lower(),
                        "verified": True,
                        "storage": "external-public",
                    })
                    continue

                path = SOURCES / path_value
                if not path.is_file():
                    failures.append(path_value + ": unavailable locally")
                    continue
                content = path.read_bytes()
                digest = hashlib.sha256(content).hexdigest()
                valid = digest == entry["sha256"].lower() and len(content) == entry["size"]
                output["fingerprints"].append({"path": path_value, "sha256": digest, "verified": valid})
                if not valid:
                    failures.append(path_value + ": fingerprint mismatch")

        required = (
            "MHCatalogue.db",
            "OPEN.db",
            "ScenarioDevices-program-files.sqlite",
            "ScenarioDevices-programdata.sqlite",
            "rules.db3",
            "OpenQuery.txt",
        )
        missing = [name for name in required if name not in materialized]
        if missing:
            failures.append("private artifacts unavailable: " + ", ".join(missing))
        else:
            for name in ("MHCatalogue.db", "OPEN.db", "ScenarioDevices-program-files.sqlite",
                         "ScenarioDevices-programdata.sqlite", "rules.db3"):
                with connect(materialized[name]) as conn:
                    tables = rows(conn, "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
                    output["databases"][name] = {
                        "table_counts": {r["name"]: conn.execute('SELECT COUNT(*) FROM "' + r["name"] + '"').fetchone()[0] for r in tables},
                        "integrity": conn.execute("PRAGMA integrity_check").fetchone()[0],
                    }

            with connect(materialized["OPEN.db"]) as conn:
                output["registry"] = rows(conn, "SELECT s.id_system,s.descr,s.who,s.diag_who,s.managed,COUNT(a.id_open) AS operations FROM EN_SYSTEM s LEFT JOIN AS_OPEN_SYSTEM a USING(id_system) GROUP BY s.id_system ORDER BY s.id_system")
                output["sequences"] = rows(conn, "SELECT s.sequence_label,a.open_order,a.mandatory_open,a.repeated_open,a.status4nack,a.status4error,o.id_open,o.open_label,o.open_string FROM EN_SEQUENCE s JOIN AS_OPEN_SEQUENCE a USING(id_sequence) JOIN EN_OPEN o USING(id_open) ORDER BY s.id_sequence,a.open_order,o.id_open")
                output["timeouts"] = rows(conn, 'SELECT * FROM EN_TIMEOUT ORDER BY id_timeout')
                output["address_rules"] = rows(conn, 'SELECT * FROM EN_ADDRESS_RULE ORDER BY id_address_rule')
                output["identity_parameters"] = rows(conn, "SELECT o.id_open,p.* FROM EN_OPEN o JOIN AS_OPEN_PARAM a USING(id_open) JOIN EN_OPEN_PARAM p USING(id_param) WHERE o.id_open IN (1,21,22,26,78) ORDER BY o.id_open,p.id_param")

            with connect(materialized["MHCatalogue.db"]) as conn:
                output["configuration_owners"] = rows(conn, "SELECT (id_key_object<>0) AS object_owner,(id_firmware<>0) AS firmware_owner,COUNT(*) AS rows FROM EN_CONF GROUP BY object_owner,firmware_owner")
                output["physical_translation"] = rows(conn, "SELECT * FROM EN_PHY_TO_ADV_TRANS ORDER BY id_en_phy_to_adv_trans")
                output["catalogue_systems"] = rows(conn, "SELECT s.id_system,s.name,s.sys_modobj,COUNT(DISTINCT a.id_item) AS items,COUNT(DISTINCT d.id_device) AS devices FROM EN_SYSTEM s LEFT JOIN AS_ITEM_SYSTEM a USING(id_system) LEFT JOIN EN_DEVICE d USING(id_item) GROUP BY s.id_system ORDER BY s.id_system")

            for name in ("ScenarioDevices-program-files.sqlite", "ScenarioDevices-programdata.sqlite"):
                with connect(materialized[name]) as conn:
                    output["databases"][name]["frames"] = rows(conn, "SELECT ChiOpen,COUNT(*) AS commands,SUM(Frame IS NULL) AS absent,SUM(Frame LIKE '*%##') AS literal FROM Commands GROUP BY ChiOpen ORDER BY ChiOpen")
                    output["databases"][name]["nonliteral_frames"] = rows(conn, "SELECT Name,Frame FROM Commands WHERE Frame IS NOT NULL AND Frame NOT LIKE '*%##' ORDER BY Name")
                    output["databases"][name]["selected_templates"] = rows(conn, "SELECT Name,ChiOpen,Frame FROM Commands WHERE ChiOpen IN ('14','4') OR Name LIKE '%DoorLock%' ORDER BY Name")

            with connect(materialized["rules.db3"]) as conn:
                output["validation_objects"] = rows(conn, "SELECT KOBJECTS,COUNT(*) AS rows FROM rules GROUP BY KOBJECTS")

            text = materialized["OpenQuery.txt"].read_text(encoding="utf-8-sig")
            output["address_query"] = next(line for line in text.splitlines() if line.startswith("systemaddressruleDictQuery="))
            output["query_contains_ampersand"] = "&" in output["address_query"]

    output["failures"] = failures
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return bool(failures)



if __name__ == "__main__":
    raise SystemExit(main())
