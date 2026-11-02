#!/usr/bin/env python3
"""F461 host-only first pass: original data/metadata, no target execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,re,sqlite3,struct,subprocess,xml.etree.ElementTree as ET
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f461_verified_vfs',D/'image_vfs.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
SAFE_LINES={'/etc/inittab':[5,9,27,32],'/etc/init.d/rcS':[32],'/etc/init.d/rc':[145,147,170],'/etc/default/volatiles/00_core':[34,35,71],'/etc/init.d/bt_daemon-apps.sh':[15,16,17,19,23,25,26,27,35,36,37,39,40,43,45,46,47,56,57,63,64,65,67,68,71,73,74,75,79,80,81,85,88,90,91,111,112,113,114,115],'/etc/init.d/setup_m4.sh':[4,10,15,16,18,19,24],'/etc/init.d/dedrifu_env.sh':[2],'/home/bticino/bt_drover_mx/bt_drover_mx.sh':[3,4,5,7,8,10],'/etc/fstab':[3,8]}
COMPONENTS=['home/bticino/bin/bt_daemon','home/bticino/bin/scsserver','home/bticino/bin/openserver','home/bticino/bin/bt_device','home/bticino/bin/fw_manager','home/bticino/bin/dedrifupdater','home/bticino/bin/coso','home/bticino/matrix_mx/matrix_mx','home/bticino/bt_drover_mx/bt_drover_mx','home/bticino/bt_smart_home_manager/bt_smart_home_manager','home/bticino/backup_manager/backup_manager','home/bticino/gateway_manager/gateway_manager']
def build():
 out={};pins={}
 def local(p):
  z=p.read_bytes();pins[str(p.relative_to(W))]={'path':str(p.relative_to(W)),'bytes':len(z),'sha256':H(z)};return z
 def image(v,p):
  z=v.read_bytes(p);pins[v.image_label+':'+p]={'image':v.image_label,'path':p,'bytes':len(z),'sha256':H(z)};return z
 vs={}
 for label in ['normal','recovery']:
  v=m.ImageVFS(label);v.image_label=label;vs[label]=v
  for suffix in ['regular-files','symlinks','hardlinks','special-nodes']:
   local(O/'analysis'/f'{label}-{suffix}.json')
  local(O/'analysis'/f'{label}-image-listing.txt')
 local(D/'image_vfs.py');local(O/'extract_v1.py');summary=json.loads(local(O/'analysis/extraction-summary.json'));pkg=json.loads(local(O/'package-image-identities.json'));role=W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md';local(role)
 assert pkg['archive_sha256']=='cb6f3e9d875c14f74a0791d7f3f420ce9d4babadb4459c1250c6cba7e741af2b'and pkg['outer_members']==4
 xml=ET.fromstring(local(O/'extracted/fwz.xml'));assert xml.findtext('name')=='F461'and xml.findtext('fwz_ver')=='2.0.11'and xml.findtext('xml_ver')=='3.1'
 models=[q.text for q in xml.findall('.//object_model')];assert models==['5.0.134']
 out['PACKAGE.json']=J({'archive':{'path':'F461_020011.fwz','bytes':138644991,'sha256':pkg['archive_sha256']},'actual_manifest':{'name':xml.findtext('name'),'version':xml.findtext('fwz_ver'),'xml_version':xml.findtext('xml_ver'),'object_models':models,'actions':[{'type':q.attrib['type'],'provider':q.attrib['provider'],'files':[x.text for x in q.findall('attr')]}for q in xml.findall('./actions/action')],'status4_action_order':[q.attrib['act_id']for q in xml.findall('./actions/status/action')]},'images':pkg['images'],'outer_members':4,'signature_authenticity':'ZIP/gzip hashes/CRCs verified; signature blobs present, not cryptographically verified','key_source':'Curated exact commercial identity; value not exported','extraction':summary})
 # Raw ARM64 Image and FDT metadata; no target or device-tree execution.
 kdir=O/'extracted/Image.zip.sha256.sig.zip.contents/Image.zip.contents';kb=local(kdir/'Image');assert kb[56:60]==b'ARM\x64';banner=re.search(rb'Linux version [^\x00\n]+',kb);assert banner
 def dtb(z):
  magic,total,so,sto,_,_,_,_,ss,sz=struct.unpack_from('>10I',z);assert magic==0xd00dfeed and total==len(z);strings=z[sto:sto+ss];p=so;stack=[];selected=[]
  while p<so+sz:
   tag=int.from_bytes(z[p:p+4],'big');p+=4
   if tag==1:
    e=z.index(0,p);stack.append(z[p:e].decode());p=(e+4)&~3
   elif tag==2:stack.pop()
   elif tag==3:
    n,off=struct.unpack_from('>II',z,p);p+=8;v=z[p:p+n];p=(p+n+3)&~3;e=strings.index(0,off);name=strings[off:e].decode();path='/'+'/'.join(x for x in stack if x)
    if (path=='/'and name in('model','compatible'))or(path.startswith('/cpus/')and name=='compatible'):selected.append({'node':path,'property':name,'strings':[x.decode()for x in v.rstrip(b'\0').split(b'\0')]})
   elif tag==4:continue
   elif tag==9:break
   else:raise AssertionError(tag)
  return selected
 trees=[]
 for p in sorted(kdir.glob('*.dtb')):z=local(p);trees.append({'file':p.name,'bytes':len(z),'sha256':H(z),'whitelisted_metadata':dtb(z)})
 out['PLATFORM.json']=J({'kernel':{'path':str((kdir/'Image').relative_to(O)),'bytes':len(kb),'sha256':H(kb),'ARM64_Image_magic':True,'text_offset':hex(struct.unpack_from('<Q',kb,8)[0]),'declared_Image_size':struct.unpack_from('<Q',kb,16)[0],'banner_file_offset':hex(banner.start()),'banner':banner.group().decode(errors='replace')},'DTBs':trees,'other_kernel_members':[q for q in pkg['members']if q['path'].startswith(str(kdir.relative_to(O))+'/')and not q['path'].endswith(('.dtb','/Image'))],'meaning':'Packaged target metadata only, not actual selected DTB/hardware or running kernel.'})
 # Every extracted regular file is read through full SHA verification before magic census.
 census={};dbs=[];configs=[]
 for label,v in vs.items():
  arches={};elfs=[];magics=[]
  for p,meta in v.regular.items():
   z=v.read_bytes('/'+p)
   if z.startswith(b'\x7fELF'):
    cls=z[4];end='<'if z[5]==1 else'>';machine=struct.unpack_from(end+'H',z,18)[0];typ=struct.unpack_from(end+'H',z,16)[0];entry=struct.unpack_from(end+('Q'if cls==2 else'I'),z,24)[0];key=f'class{cls}/machine{machine}';arches[key]=arches.get(key,0)+1;elfs.append({'path':p,'bytes':len(z),'sha256':meta['sha256'],'ELF_class':cls,'machine':machine,'type':typ,'entry_VA':hex(entry)})
   if z.startswith(b'SQLite format 3\0'):
    fp=v.root/p;conn=sqlite3.connect(fp.resolve().as_uri()+'?mode=ro&immutable=1',uri=True);conn.execute('PRAGMA query_only=ON');conn.execute('PRAGMA trusted_schema=OFF');rows=conn.execute("SELECT type,name,tbl_name,sql FROM sqlite_master WHERE name NOT LIKE 'sqlite_%' ORDER BY type,name").fetchall();sch=[]
    for typ,name,tbl,sql in rows:
     q={'type':typ,'name':name,'table':tbl,'definition_sha256':H((sql or'').encode())}
     if typ=='table'and not(sql or'').upper().startswith('CREATE VIRTUAL'):
      ident='"'+name.replace('"','""')+'"';q['rows']=conn.execute('SELECT count(*) FROM '+ident).fetchone()[0];q['columns']=[{'name':x[1],'declared_type':x[2],'not_null':bool(x[3]),'PK_ordinal':x[5]}for x in conn.execute('PRAGMA table_info('+ident+')')]
     sch.append(q)
    conn.close();dbs.append({'image':label,'path':p,'bytes':len(z),'sha256':meta['sha256'],'magic':'SQLite format 3','tables':sum(q['type']=='table'for q in sch),'schema':sch})
   elif z[:5]==b'REDIS':magics.append({'path':p,'format':'Redis RDB signature','bytes':len(z),'sha256':meta['sha256']})
   if label=='normal'and p.startswith('home/bticino/')and p.endswith('.json'):
    try:q=json.loads(z);configs.append({'path':p,'sha256':meta['sha256'],'top_level_kind':type(q).__name__,'top_level_keys':sorted(q)if isinstance(q,dict)else[]})
    except (ValueError,UnicodeError):configs.append({'path':p,'sha256':meta['sha256'],'JSON_parse':'not parsed; no contents exported'})
  census[label]={'architecture_counts':arches,'ELF_files':elfs,'other_database_magics':magics,'regular_files_scanned':len(v.regular),'full_manifest_SHA_verified_before_magic_scan':True}
 out['FILE_MAGIC_CENSUS.json']=J(census);out['DATABASE_SCHEMAS.json']=J({'method':'All regular-file signatures scanned, not extensions. SQLite mode=ro&immutable=1/query_only/trusted_schemaOFF; schema metadata/counts only, no stored expressions/default values evaluated/exported.','databases':dbs});out['CONFIG_SHAPES.json']=J(configs)
 v=vs['normal'];snips=[]
 for p,nums in SAFE_LINES.items():
  z=image(v,p);lines=z.decode().splitlines();snips.append({'path':p,'sha256':H(z),'selected_lines':[{'line':n,'text':lines[n-1]}for n in nums]})
 out['STARTUP_LINES.json']=J(snips)
 stacks=[]
 for label,v in vs.items():
  for p in ['/home/bticino/cfg/stack_open.xml','/home/bticino/cfg/stack_open_reduced.xml']:
   z=image(v,p);rt=ET.fromstring(z);apps=[]
   for x in rt.iter():
    if x.find('name')is not None and x.find('path')is not None:
     apps.append({'tag':x.tag,'name':x.findtext('name'),'path':x.findtext('path'),'working_mode':x.findtext('working_mode')})
   stacks.append({'image':label,'path':p,'sha256':H(z),'normal_status':[q.text for q in rt.iter('normal_status')],'process_declarations':apps,'count':len(apps)})
 out['STACK_DECLARATIONS.json']=J(stacks);out['BOOT_LINKS.json']=J({label:{p:q for p,q in v.links.items()if p.startswith(('etc/rc5.d/','etc/rcS.d/'))or p=='sbin/init'}for label,v in vs.items()})
 components=[]
 for label,v in vs.items():
  for p in COMPONENTS:
   if p not in v.regular:components.append({'image':label,'path':p,'present_regular':False});continue
   z=image(v,'/'+p);assert z.startswith(b'\x7fELF');fp=v.root/p;dyn=subprocess.check_output(['readelf','-dW',str(fp)],text=True);components.append({'image':label,'path':p,'bytes':len(z),'sha256':H(z),'ELF_class':z[4],'machine':struct.unpack_from('<H',z,18)[0],'entry_VA':hex(struct.unpack_from('<Q'if z[4]==2 else'<I',z,24)[0]),'NEEDED':re.findall(r'\(NEEDED\).*\[([^]]+)\]',dyn),'RPATH_RUNPATH':re.findall(r'\((?:RPATH|RUNPATH)\).*\[([^]]+)\]',dyn)})
 out['COMPONENTS.json']=J(components)
 a,b=vs['normal'].regular,vs['recovery'].regular;shared=set(a)&set(b);out['NORMAL_RECOVERY.json']=J({'shared_equal':sum(a[k]['sha256']==b[k]['sha256']for k in shared),'shared_changed':[k for k in sorted(shared)if a[k]['sha256']!=b[k]['sha256']],'only_normal':sorted(set(a)-set(b)),'only_recovery':sorted(set(b)-set(a)),'scope':'Complete regular-file path/hash comparison only, not identical runtime behavior.'})
 versions=[]
 for label,v in vs.items():
  for p in ['/etc/version','/etc/issue','/home/bticino/sp/dbfiles_ws.xml']:
   z=image(v,p)
   if p.endswith('.xml'):vv=[{'tag':q.tag,'value':q.text}for q in ET.fromstring(z).iter()if q.tag in('ver_webserver','ver_scsserver','ver_openserver')]
   elif p=='/etc/version':vv=z.decode().strip()
   else:vv=[s for s in z.decode().splitlines()if'Poky'in s or'Distribution'in s]
   versions.append({'image':label,'path':p,'sha256':H(z),'whitelisted_version_metadata':vv})
 out['VERSIONS.json']=J(versions)
 # Exact same-path artifact comparison only. No schemas/layouts or behavior transferred.
 comparisons=[]
 for product,path in [('MyHOMEServer1','work/myhomeserver1-firmware/3.87.13/analysis/normal-regular-files.json'),('F460','work/f460-firmware/2.0.12/analysis/normal-regular-files.json')]:
  p=W/path
  if not p.exists():continue
  reg=json.loads(local(p))
  for q in COMPONENTS+['home/bticino/matrix_mx/MHCatalogue.db','home/bticino/cfg/stack_open.xml','etc/init.d/bt_daemon-apps.sh']:
   comparisons.append({'other_product':product,'path':q,'F461':a.get(q),'other':reg.get(q),'exact_same_bytes':q in a and q in reg and a[q]['sha256']==reg[q]['sha256']})
 out['EXACT_COMPARISONS.json']=J(comparisons)
 out['INPUTS.json']=J({'files':pins,'scope':'Exact selected input bytes; entire regular-file manifests separately pin magic-census source identities. No credentials/config values exported beyond explicit public startup/version/path whitelist.'})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'outputs_excluding_manifest':len(out),'input_pins':len(pins),'original_execution':0,'mounts':0,'network_calls':0,'database_files':len(dbs)}})
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');ck=ap.parse_args().check;out=build();C=D/'first-candidate';cp={**out,Path(__file__).name:Path(__file__).read_bytes(),'image_vfs.py':(D/'image_vfs.py').read_bytes()};ix=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in cp.items()})
 if ck:
  for n,z in out.items():assert(D/n).read_bytes()==z,n
  assert(C/'INDEX.json').read_bytes()==ix
  for n,z in cp.items():assert(C/n).read_bytes()==z,n
 else:
  assert not C.exists()and all(not(D/n).exists()for n in out)
  for n,z in out.items():(D/n).open('xb').write(z)
  C.mkdir()
  for n,z in cp.items():(C/n).open('xb').write(z)
  (C/'INDEX.json').open('xb').write(ix)
 print(json.dumps({'mode':'check'if ck else'generate','outputs':len(out),'original_execution':0,'first_copies':len(cp)},sort_keys=True))
if __name__=='__main__':main()
