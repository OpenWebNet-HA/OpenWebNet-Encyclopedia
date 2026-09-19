#!/usr/bin/env python3
"""Read-only Phase 3 evidence probes; prints reproducible JSON, not protocol verdicts.

Run from the repository root. Requires PyYAML. No network or Device access.
"""
import hashlib
import json
import sqlite3
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[3]
SOURCES = ROOT / "sources"


def connect(name):
    path = SOURCES / "myhome-suite/3.5.38/databases" / name
    conn = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True)
    conn.row_factory = sqlite3.Row
    return conn


def rows(conn, sql):
    return [dict(row) for row in conn.execute(sql)]


def main():
    manifest = yaml.safe_load((SOURCES / "manifest.yaml").read_text())
    output = {"fingerprints": [], "databases": {}}
    failures = []
    for source_set in manifest["source_sets"].values():
        for entry in source_set["files"]:
            path = SOURCES / entry["path"]
            if not path.is_file():
                failures.append(entry["path"] + ": unavailable locally")
                continue
            content = path.read_bytes()
            digest = hashlib.sha256(content).hexdigest()
            valid = digest == entry["sha256"].lower() and len(content) == entry["size"]
            output["fingerprints"].append({"path": entry["path"], "sha256": digest, "verified": valid})
            if not valid:
                failures.append(entry["path"] + ": fingerprint mismatch")
    for name in ("MHCatalogue.db", "OPEN.db", "ScenarioDevices-program-files.sqlite",
                 "ScenarioDevices-programdata.sqlite", "rules.db3"):
        with connect(name) as conn:
            tables = rows(conn, "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
            output["databases"][name] = {
                "table_counts": {r["name"]: conn.execute('SELECT COUNT(*) FROM "' + r["name"] + '"').fetchone()[0] for r in tables},
                "integrity": conn.execute("PRAGMA integrity_check").fetchone()[0],
            }
    with connect("OPEN.db") as conn:
        output["registry"] = rows(conn, "SELECT s.id_system,s.descr,s.who,s.diag_who,s.managed,COUNT(a.id_open) AS operations FROM EN_SYSTEM s LEFT JOIN AS_OPEN_SYSTEM a USING(id_system) GROUP BY s.id_system ORDER BY s.id_system")
        output["sequences"] = rows(conn, "SELECT s.sequence_label,a.open_order,a.mandatory_open,a.repeated_open,a.status4nack,a.status4error,o.id_open,o.open_label,o.open_string FROM EN_SEQUENCE s JOIN AS_OPEN_SEQUENCE a USING(id_sequence) JOIN EN_OPEN o USING(id_open) ORDER BY s.id_sequence,a.open_order,o.id_open")
        output["timeouts"] = rows(conn, 'SELECT * FROM EN_TIMEOUT ORDER BY id_timeout')
        output["address_rules"] = rows(conn, 'SELECT * FROM EN_ADDRESS_RULE ORDER BY id_address_rule')
        output["identity_parameters"] = rows(conn, "SELECT o.id_open,p.* FROM EN_OPEN o JOIN AS_OPEN_PARAM a USING(id_open) JOIN EN_OPEN_PARAM p USING(id_param) WHERE o.id_open IN (1,21,22,26,78) ORDER BY o.id_open,p.id_param")
    with connect("MHCatalogue.db") as conn:
        output["configuration_owners"] = rows(conn, "SELECT (id_key_object<>0) AS object_owner,(id_firmware<>0) AS firmware_owner,COUNT(*) AS rows FROM EN_CONF GROUP BY object_owner,firmware_owner")
        output["physical_translation"] = rows(conn, "SELECT * FROM EN_PHY_TO_ADV_TRANS ORDER BY id_en_phy_to_adv_trans")
        output["catalogue_systems"] = rows(conn, "SELECT s.id_system,s.name,s.sys_modobj,COUNT(DISTINCT a.id_item) AS items,COUNT(DISTINCT d.id_device) AS devices FROM EN_SYSTEM s LEFT JOIN AS_ITEM_SYSTEM a USING(id_system) LEFT JOIN EN_DEVICE d USING(id_item) GROUP BY s.id_system ORDER BY s.id_system")
    for name in ("ScenarioDevices-program-files.sqlite", "ScenarioDevices-programdata.sqlite"):
        with connect(name) as conn:
            output["databases"][name]["frames"] = rows(conn, "SELECT ChiOpen,COUNT(*) AS commands,SUM(Frame IS NULL) AS absent,SUM(Frame LIKE '*%##') AS literal FROM Commands GROUP BY ChiOpen ORDER BY ChiOpen")
            output["databases"][name]["nonliteral_frames"] = rows(conn, "SELECT Name,Frame FROM Commands WHERE Frame IS NOT NULL AND Frame NOT LIKE '*%##' ORDER BY Name")
            output["databases"][name]["selected_templates"] = rows(conn, "SELECT Name,ChiOpen,Frame FROM Commands WHERE ChiOpen IN ('14','4') OR Name LIKE '%DoorLock%' ORDER BY Name")
    with connect("rules.db3") as conn:
        output["validation_objects"] = rows(conn, "SELECT KOBJECTS,COUNT(*) AS rows FROM rules GROUP BY KOBJECTS")
    query_file = SOURCES / "myhome-suite/3.5.38/support/OpenQuery.txt"
    text = query_file.read_text(encoding="utf-8-sig")
    output["address_query"] = next(line for line in text.splitlines() if line.startswith("systemaddressruleDictQuery="))
    output["query_contains_ampersand"] = "&" in output["address_query"]
    output["failures"] = failures
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return bool(failures)


if __name__ == "__main__":
    raise SystemExit(main())
