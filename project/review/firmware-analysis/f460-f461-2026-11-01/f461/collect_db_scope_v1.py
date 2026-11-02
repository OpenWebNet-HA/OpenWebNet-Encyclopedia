#!/usr/bin/env python3
"""SQLite schema-count scope supplement only; no stored expressions/values."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,json,sqlite3
D=Path(__file__).resolve().parent;O=D.parents[1];H=lambda z:hashlib.sha256(z).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
def build():
 rows=[]
 for image,tree in [('normal','rootfs'),('recovery','recovery')]:
  p=O/'analysis'/tree/'home/bticino/matrix_mx/MHCatalogue.db';z=p.read_bytes();assert H(z)=='bd2ff4d326692c85bc4eb3f86504d615758da97dc832389fac523734574833e9'
  c=sqlite3.connect(p.resolve().as_uri()+'?mode=ro&immutable=1',uri=True);c.execute('PRAGMA query_only=ON');c.execute('PRAGMA trusted_schema=OFF')
  counts=dict(c.execute('SELECT type,count(*) FROM sqlite_master GROUP BY type ORDER BY type'));names=[x[0]for x in c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'sqlite_%' ORDER BY name")];filtered=c.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'").fetchone()[0];assert counts=={'index':75,'table':75}and names==['sqlite_sequence']and filtered==74;c.close()
  rows.append({'image':image,'path':'/home/bticino/matrix_mx/MHCatalogue.db','bytes':len(z),'sha256':H(z),'all_schema_objects_by_type':counts,'noninternal_table_count':filtered,'internal_table_names':names})
 return J({'scope':'Clarifies existing DATABASE_SCHEMAS.json selected query:74 noninternal tables,75 total including SQLite bookkeeping. Prior generated files/counts unchanged.','queries':['SELECT type,count(*) FROM sqlite_master GROUP BY type ORDER BY type',"SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'sqlite_%' ORDER BY name","SELECT count(*) FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"],'mode':'ro/immutable/query_only/trusted_schemaOFF','databases':rows,'original_execution':0})
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');ck=p.parse_args().check;z=build();out=D/'DB_SCOPE.json';C=D/'db-scope-first-candidate';cp={'DB_SCOPE.json':z,Path(__file__).name:Path(__file__).read_bytes()};ix=J({n:{'bytes':len(b),'sha256':H(b)}for n,b in cp.items()})
 if ck:
  assert out.read_bytes()==z and(C/'INDEX.json').read_bytes()==ix
  for n,b in cp.items():assert(C/n).read_bytes()==b
 else:
  assert not out.exists()and not C.exists();out.open('xb').write(z);C.mkdir()
  for n,b in cp.items():(C/n).open('xb').write(b)
  (C/'INDEX.json').open('xb').write(ix)
 print(json.dumps({'check':ck,'outputs':1,'tables_total':75,'tables_noninternal':74,'original_execution':0}))
if __name__=='__main__':main()
