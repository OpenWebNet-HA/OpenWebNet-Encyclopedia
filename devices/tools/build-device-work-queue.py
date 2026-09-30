#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, sqlite3
from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "sources" / "myhome-suite" / "3.5.38" / "databases" / "MHCatalogue.db"
QUEUE = ROOT / "devices" / "work-queue.yaml"
DASH = ROOT / "devices" / "work-queue.md"

STATES = ["unreviewed","triaged","research","definition-in-progress","review-ready","reviewed"]
REVIEW_VALUES = ["pending","partial","complete","not-applicable"]
REVIEW_KEYS = [
    "commercial_identities","database_extraction","documentation_discovery",
    "documentation_archive","source_reconciliation","definition",
    "hardware_corroboration","final_review",
]
PRIORITIES = ["high","normal","low"]

def source_sha():
    return hashlib.sha256(DB.read_bytes()).hexdigest()

def catalogue():
    con=sqlite3.connect(DB); con.row_factory=sqlite3.Row
    rows=[dict(r) for r in con.execute("""
      select i.id_item,i.descr,count(d.id_device) commercial_records,
             group_concat(d.code, ', ') codes
      from EN_ITEM i join EN_DEVICE d on d.id_item=i.id_item
      group by i.id_item,i.descr order by i.id_item
    """)]
    con.close()
    return {str(r["id_item"]):r for r in rows}

def fresh_entry():
    return {
      "state":"unreviewed","priority":"normal","outcome":None,
      "review":{
        "commercial_identities":"pending",
        "database_extraction":"pending",
        "documentation_discovery":"pending",
        "documentation_archive":"pending",
        "source_reconciliation":"pending",
        "definition":"pending",
        "hardware_corroboration":"pending",
        "final_review":"pending",
      },
      "blockers":[],"notes":[],
    }

def load():
    if not QUEUE.exists():
        return {"version":1,"source":{"mhcatalogue_sha256":source_sha()},"items":{}}
    with QUEUE.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}

def sync(data):
    cat=catalogue()
    items=data.setdefault("items",{})
    for item_id in cat:
        if item_id not in items:
            items[item_id]=fresh_entry()
    unknown=sorted(set(items)-set(cat), key=int)
    if unknown:
        raise SystemExit("queue contains item IDs absent from canonical catalogue: "+", ".join(unknown))
    data["version"]=1
    data["source"]={"mhcatalogue_sha256":source_sha()}
    data["items"]={k:items[k] for k in sorted(items,key=int)}
    return data

def definition_exists(device_id):
    for p in (ROOT/"devices"/"definitions").glob("*.md"):
        if device_id in p.read_text(encoding="utf-8"):
            return True
    return False

def validate(data):
    cat=catalogue(); seen={}
    if data.get("version")!=1:
        raise SystemExit("unsupported queue version")
    if data.get("source",{}).get("mhcatalogue_sha256")!=source_sha():
        raise SystemExit("queue source SHA-256 is stale; run --sync")
    if set(data.get("items",{}))!=set(cat):
        raise SystemExit("queue item set differs from canonical catalogue; run --sync")
    for item_id,e in data["items"].items():
        if e.get("state") not in STATES:
            raise SystemExit(f"{item_id}: invalid state")
        if e.get("priority") not in PRIORITIES:
            raise SystemExit(f"{item_id}: invalid priority")
        review=e.get("review",{})
        if set(review)!=set(REVIEW_KEYS):
            raise SystemExit(f"{item_id}: review keys incomplete")
        for k,v in review.items():
            if v not in REVIEW_VALUES:
                raise SystemExit(f"{item_id}: invalid {k}={v}")
        out=e.get("outcome")
        if out is not None:
            if out.get("type") not in ["device-definition","split","merged","not-applicable"]:
                raise SystemExit(f"{item_id}: invalid outcome type")
            for did in out.get("device_ids",[]) or []:
                if did in seen and seen[did]!=item_id:
                    raise SystemExit(f"{did} claimed by items {seen[did]} and {item_id}")
                seen[did]=item_id
                if not definition_exists(did):
                    raise SystemExit(f"{item_id}: missing definition for {did}")
        if e["state"]=="reviewed":
            for k in ["commercial_identities","database_extraction","documentation_discovery","source_reconciliation","definition","final_review"]:
                if review[k] not in ["complete","not-applicable"]:
                    raise SystemExit(f"{item_id}: reviewed but {k}={review[k]}")

def dump(data):
    with QUEUE.open("w",encoding="utf-8") as f:
        yaml.safe_dump(data,f,sort_keys=False,allow_unicode=True,width=1000)

def dashboard(data):
    cat=catalogue(); counts=Counter(e["state"] for e in data["items"].values())
    lines=[
      "# Device Work Queue","",
      "> Generated from devices/work-queue.yaml plus the canonical catalogue. Edit the YAML ledger, not this page.","",
      "## Overview","",
      "| State | Items |","| --- | ---: |",
    ]
    for state in STATES:
        lines.append(f"| {state} | {counts[state]} |")
    lines += [
      "",f"Total: **{len(data['items'])}** technical-item clusters.","",
      "Database extraction is mechanically available for every cluster in this catalogue revision. The queue tracks when that source material has actually been reviewed and integrated into a Device definition.","",
      "## Next work","",
      "| Priority | Item | Description | Commercial records | State | Definition outcome | Documents | Archive | Source reconciliation | Hardware | Blockers |",
      "| --- | ---: | --- | ---: | --- | --- | --- | --- | --- | --- | --- |"
    ]
    rank={v:i for i,v in enumerate(PRIORITIES)}
    state_rank={v:i for i,v in enumerate(STATES)}
    active=[(k,e) for k,e in data["items"].items() if e["state"]!="reviewed"]
    active.sort(key=lambda kv:(rank[kv[1]["priority"]],state_rank[kv[1]["state"]],-cat[kv[0]]["commercial_records"],int(kv[0])))
    for item_id,e in active:
        c=cat[item_id]; out=e.get("outcome") or {}; did=", ".join(out.get("device_ids",[]) or []) or "-"
        blockers="; ".join(e.get("blockers",[]) or []) or "-"
        desc=str(c["descr"]).replace("|","\\|")
        blockers=blockers.replace("|","\\|")
        lines.append(f"| {e['priority']} | {item_id} | {desc} | {c['commercial_records']} | {e['state']} | {did} | {e['review']['documentation_discovery']} | {e['review']['documentation_archive']} | {e['review']['source_reconciliation']} | {e['review']['hardware_corroboration']} | {blockers} |")
    lines += ["","## Reviewed","",
              "| Item | Description | Outcome |","| ---: | --- | --- |"]
    reviewed=[(k,e) for k,e in data["items"].items() if e["state"]=="reviewed"]
    for item_id,e in sorted(reviewed,key=lambda kv:int(kv[0])):
        out=e.get("outcome") or {}; did=", ".join(out.get("device_ids",[]) or []) or out.get("type","-")
        desc=str(cat[item_id]["descr"]).replace("|","\\|")
        lines.append(f"| {item_id} | {desc} | {did} |")
    lines += [
      "","## Workflow","",
      "`unreviewed -> triaged -> research -> definition-in-progress -> review-ready -> reviewed`","",
      "The state is the overall workflow position. The review dimensions explain what remains. A reviewed dossier may still record explicit evidence gaps; reviewed means all currently known sources have been processed and the remaining limits are documented, not that no future evidence can exist.",""
    ]
    DASH.write_text("\n".join(lines),encoding="utf-8")

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--sync",action="store_true")
    ap.add_argument("--check",action="store_true")
    args=ap.parse_args()
    data=load()
    if args.sync:
        data=sync(data); dump(data)
    validate(data)
    if args.check:
        expected=DASH.read_text(encoding="utf-8") if DASH.exists() else None
        dashboard(data)
        actual=DASH.read_text(encoding="utf-8")
        if expected != actual:
            raise SystemExit("dashboard out of date; regenerate")
    else:
        dashboard(data)

if __name__=="__main__":
    main()
