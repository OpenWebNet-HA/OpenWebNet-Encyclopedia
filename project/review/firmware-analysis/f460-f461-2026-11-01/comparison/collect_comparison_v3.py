#!/usr/bin/env python3
"""Read-only structural/product/catalogue comparison. No firmware execution."""
from pathlib import Path
import argparse,collections,hashlib,importlib.util,json,os,sqlite3,struct,subprocess,sys
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;W=O.parents[2];H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
V=W/'work/myhomeserver1-firmware/3.87.13/research/2026-10-31/image_vfs.py';s=importlib.util.spec_from_file_location('comparison_verified_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
PRODUCTS={'F460':'work/f460-firmware/2.0.12','F461':'work/f461-firmware/2.0.11','MHS1':'work/myhomeserver1-firmware/3.87.13'}
SELECTED=['home/bticino/bin/'+n for n in ['bt_daemon','coso','scsserver']]+['home/bticino/'+n+'/'+n for n in ['matrix_mx','scheduling_manager','alarm_manager','backup_manager','gateway_manager','energy_manager','player_manager','bt_smart_home_manager','bt_drover_mx','bt_netatmo']]
def pin(p):b=p.read_bytes();return {'path':str(p.relative_to(W)),'bytes':len(b),'sha256':H(b)}
def elfmeta(b):
 assert b[:4]==b'\x7fELF'and b[5]==1
 c=b[4];assert c in(1,2)
 if c==1:
  v=struct.unpack_from('<HHIIIIIHHHHHH',b,16);typ,mach,_,entry,ph,*_=v;es,n=v[8],v[9]
  hdr=[struct.unpack_from('<8I',b,ph+i*es)for i in range(n)];interps=[b[q[1]:q[1]+q[4]].rstrip(b'\0').decode()for q in hdr if q[0]==3]
 else:
  v=struct.unpack_from('<HHIQQQIHHHHHH',b,16);typ,mach,_,entry,ph,*_=v;es,n=v[8],v[9]
  hdr=[struct.unpack_from('<II6Q',b,ph+i*es)for i in range(n)];interps=[b[q[2]:q[2]+q[5]].rstrip(b'\0').decode()for q in hdr if q[0]==3]
 return {'ELF_class':32 if c==1 else 64,'machine':mach,'type':typ,'linked_entry':hex(entry),'interpreter':interps,'flags':hex(v[6])}
def dbsummary(p):
 c=sqlite3.connect(p.resolve().as_uri()+'?mode=ro&immutable=1',uri=True);c.execute('PRAGMA query_only=ON');c.execute('PRAGMA trusted_schema=OFF');assert c.execute('PRAGMA query_only').fetchone()==(1,);assert c.execute('PRAGMA quick_check').fetchall()==[('ok',)]
 tables={}
 def enc(v):return ['blob',v.hex()]if isinstance(v,bytes)else[type(v).__name__,v]
 for name,sql in c.execute("SELECT name,sql FROM sqlite_master WHERE type='table' ORDER BY name"):
  q='"'+name.replace('"','""')+'"';rows=sorted(J([enc(x)for x in row])for row in c.execute('SELECT * FROM '+q));h=hashlib.sha256()
  for z in rows:h.update(struct.pack('>Q',len(z)));h.update(z)
  tables[name]={'rows':len(rows),'table_SQL_sha256':H((sql or '').encode()),'typed_row_multiset_sha256':h.hexdigest()}
 indexes=[{'name':n,'table':t,'SQL_sha256':H((sql or '').encode())}for n,t,sql in c.execute("SELECT name,tbl_name,sql FROM sqlite_master WHERE type='index' ORDER BY name")];c.close()
 return {'identity':pin(p),'quick_check':'ok','tables':tables,'indexes':indexes,'table_count':len(tables),'index_count':len(indexes),'scope':'Complete structural/typed-row-multiset hashes; no raw row/config values exported, no stable-ID semantic interpretation'}
def pair(a,b,ma,mb):
 common=set(ma)&set(mb);same=sorted(p for p in common if ma[p]['sha256']==mb[p]['sha256']);different=sorted(common-set(same))
 app=lambda p:p.startswith('home/bticino/')and p.count('/')==3 and p.split('/')[-1]==p.split('/')[-2]
 return {'left':a,'right':b,'left_regular_paths':len(ma),'right_regular_paths':len(mb),'common_paths':len(common),'same_hash_at_common_path':len(same),'different_hash_at_common_path':len(different),'left_only_paths':len(set(ma)-set(mb)),'right_only_paths':len(set(mb)-set(ma)),'left_only_application_paths':sorted(p for p in set(ma)-set(mb)if app(p)),'right_only_application_paths':sorted(p for p in set(mb)-set(ma)if app(p)),'scope':'Path/hash census only, not runtime or behavior equivalence, capability absence or coverage percentage'}
def build():
 out={};inputs=[pin(V),pin(O/'ACQUISITION_COMPLETE.json')];maps={};vfs={};selected={};env=dict(os.environ,DEBUGINFOD_URLS='')
 for name,rel in PRODUCTS.items():
  root=W/rel;research=root/'research/2026-11-01'if name!='MHS1'else root/'research/2026-10-31';v=m.ImageVFS('normal',research_dir=research);vfs[name]=v;maps[name]={}
  for image in ['normal','recovery']:
   p=root/'analysis'/f'{image}-regular-files.json';maps[name][image]=json.loads(p.read_text());inputs.append(pin(p))
  selected[name]={}
  for p in SELECTED:
   if p not in v.regular:selected[name][p]={'present_as_regular_file':False,'scope':'Exact path in extracted normal image only; not whole-product function absence'};continue
   b=v.read_bytes(p);x={'present_as_regular_file':True,'sha256':H(b),'bytes':len(b)}
   if b.startswith(b'\x7fELF'):
    x['ELF']=elfmeta(b);d=subprocess.check_output(['readelf','-dW',str(v.root/p)],text=True,env=env);import re;x['DT_NEEDED']=re.findall(r'\(NEEDED\).*?\[(.*?)\]',d)
   selected[name][p]=x
 out['SELECTED_COMPONENTS.json']=J(selected)
 comparisons=[]
 for image in ['normal','recovery']:
  for a,b in [('F460','F461'),('F460','MHS1'),('F461','MHS1')]:comparisons.append({'image':image,**pair(a,b,maps[a][image],maps[b][image])})
 out['PATH_HASH_COMPARISON.json']=J(comparisons)
 dbs={}
 for name in PRODUCTS:
  v=vfs[name];p='home/bticino/matrix_mx/MHCatalogue.db';b=v.read_bytes(p);assert b.startswith(b'SQLite format 3\0');dbs[name]=dbsummary(v.root/p)
 assert dbs['F460']['identity']['sha256']==dbs['F461']['identity']['sha256']=='bd2ff4d326692c85bc4eb3f86504d615758da97dc832389fac523734574833e9'
 suite=W/'work/installer-database-audit/2026-10-31/recovered/f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5.bin';assert H(suite.read_bytes())=='f0c9d24f988937d1c8654c72b034fc02c7aacb37dc099bbc926f0c58363fe8e5';dbs['Suite']=dbsummary(suite);out['CATALOGUE_PROFILES.json']=J(dbs)
 pairs=[]
 for a,b in [('F460','F461'),('F460','MHS1'),('F460','Suite')]:
  ta,tb=dbs[a]['tables'],dbs[b]['tables'];shared=set(ta)&set(tb)
  pairs.append({'left':a,'right':b,'same_whole_DB_hash':dbs[a]['identity']['sha256']==dbs[b]['identity']['sha256'],'left_table_count':len(ta),'right_table_count':len(tb),'left_only_tables':sorted(set(ta)-set(tb)),'right_only_tables':sorted(set(tb)-set(ta)),'equal_table_SQL':sorted(t for t in shared if ta[t]['table_SQL_sha256']==tb[t]['table_SQL_sha256']),'equal_row_multisets':sorted(t for t in shared if ta[t]['typed_row_multiset_sha256']==tb[t]['typed_row_multiset_sha256']),'different_row_multisets':sorted(t for t in shared if ta[t]['typed_row_multiset_sha256']!=tb[t]['typed_row_multiset_sha256']),'scope':'No semantic correspondence from shared IDs; runtime installed-capability policy unproved'})
 out['CATALOGUE_COMPARISON.json']=J(pairs)
 bundle={}
 for name in ['F460','F461']:
  root=W/PRODUCTS[name];d=root/({'F460':'extracted/nested/Image.zip','F461':'extracted/Image.zip.sha256.sig.zip.contents/Image.zip.contents'}[name]);assert d.is_dir();bundle[name]={};inputs.append(pin(root/({'F460':'image-extraction-provenance.json','F461':'package-image-identities.json'}[name])))
  for n in ['Image','hygw_cortex-m.bin',*sorted(p.name for p in d.glob('*.dtb'))]:
   p=d/n;assert p.is_file()and not p.is_symlink();bundle[name][n]=pin(p)
 common=set(bundle['F460'])&set(bundle['F461']);out['BOOT_BUNDLE_COMPARISON.json']=J({'products':bundle,'same_hash_members':sorted(n for n in common if bundle['F460'][n]['sha256']==bundle['F461'][n]['sha256']),'different_hash_members':sorted(n for n in common if bundle['F460'][n]['sha256']!=bundle['F461'][n]['sha256']),'scope':'Payload bytes only, not deployment/hardware behavior or cryptographic signature verification'})
 for name in dbs:inputs.append(dbs[name]['identity'])
 out['INPUTS.json']=J(inputs);out['METHOD.json']=J({'original_vendor_execution':0,'whole_process_services_OS_peripherals_network_bus_physical_execution':0,'SQLite':'Host query-only immutable reads; hashes/rowcounts only; no guest SQLite execution','image_view':'Existing verified host ImageVFS parser reused with each own product manifests; no transferred firmware ABI/layout','earlier_MHS_F454_MH202_native_ledgers':'Unchanged, separate','sensitive_data':'No packaged credentials/privatekeys/config rows exported','inventory_counts':'Structural reach/integrity, not coverage percentage or semantic capability approval'})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'products':3,'path_hash_pairs':6,'selected_paths_per_product':len(SELECTED),'catalogue_profiles':4,'catalogue_pairs':3,'new_original_execution':0}})
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args();out=build()
 if a.check:
  for n,z in out.items():assert(O/n).read_bytes()==z,n
 else:
  assert all(not(O/n).exists()for n in out);s=O/'comparison-first-candidate';assert not s.exists();s.mkdir();rows={}
  for n,z in {**out,Path(__file__).name:Path(__file__).read_bytes()}.items():
   if n in out:(O/n).open('xb').write(z)
   (s/n).open('xb').write(z);rows[n]={'bytes':len(z),'sha256':H(z)}
  (s/'INDEX.json').open('x').write(json.dumps(rows,indent=2)+'\n')
 print(json.dumps({'check':a.check,'outputs':len(out),'products':3,'catalogue_profiles':4,'new_original_execution':0}))
if __name__=='__main__':main()
