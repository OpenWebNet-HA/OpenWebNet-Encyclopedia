#!/usr/bin/env python3
"""Exclusive static F460 selected catalogue producer/reader proof; no target or SQL execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py'
H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f460_catalogue_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/matrix_mx/matrix_mx';E='16d92b02ffe89819f6947d93efa76a0f24f8b590a43d3e5d8fdc7226ec68a4ff'
SP=[('global-base',0x27d30,0x27d78),('template-producer',0x27eac,0x27ec0),('cstring-constructor',0xda5f0,0xda6d8),('base-sql-copy',0x112060,0x1120f8),('substitution-requests',0x1120f8,0x112368),('concrete-constructor-reader',0x112fd0,0x113190),('virtual-reader',0xfa970,0xfab00)]
G=[(0x27eac,0x910802d4),(0x1120cc,0xf9410061),(0x1120d4,0xf94004c2),(0x1120d0,0xf9000ebf),(0x1120ec,0x3c8082a0),(0x113010,0xd2800b00),(0x11303c,0x52800b21),(0x113040,0xf8010685),(0x11305c,0xf9000aa0),(0x113064,0x39008282),(0x1130a0,0x52800022),(0x1130b4,0xf9401ea1),(0x1130dc,0x7101941f),(0x1130e8,0xb4000313),(0x1130f4,0x528001a1),(0x11310c,0xb9001a82),(0x113114,0x528001c1),(0x11312c,0xb9001e81),(0x113138,0x7101901f),(0x113154,0xa90056d4),(0xfa9e0,0x52800022),(0xfa9f4,0xf9401681),(0xfaa1c,0x7101941f),(0xfaa28,0xb40002d3),(0xfaa30,0x528001a1),(0xfaa48,0xb9001a80),(0xfaa4c,0x528001c1),(0xfaa64,0xb9001e80),(0xfaa70,0x7101901f)]
def build():
 v=m.ImageVFS();b=v.read_bytes(P);assert H(b)==E and b[:6]==b'\x7fELF\x02\x01' and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];sz,n=struct.unpack_from('<HH',b,54);ls=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*sz))[0]==1]
 def raw(a,n):
  r=next(r for r in ls if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return b[o:o+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def q(a):return int.from_bytes(raw(a,8),'little')
 def cs(a):
  z=bytearray()
  while len(z)<8192:
   c=raw(a+len(z),1)
   if c==b'\0':return z.decode()
   z+=c
  raise AssertionError('string cap')
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def ai(a):
  x=u(a);assert x&0xffc00000==0x91000000;return(x>>10)&4095
 def call(a,tail=False):
  x=u(a);assert x&0xfc000000==(0x14000000 if tail else 0x94000000);i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 hp=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');rr=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rel(a):return next(s.strip()for s in rr.splitlines()if s.startswith(f'{a:016x} '))
 out={};sp=[]
 for name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P)
  out['spans/'+name+'.txt']=z.encode();sp.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(a,e-a).hex(),'sha256':H(raw(a,e-a))})
 for a,x in G:assert u(a)==x,(hex(a),hex(u(a)),hex(x))
 joins=[]
 for a,c,t in[(0x27d50,0x27d54,0x31a200),(0x27d50,0x27eac,0x31a200),(0x27eb0,0x27eb8,0x28be38),(0x112078,0x11207c,0x31a200),(0x113054,0x113058,0x3103b0),(0x113068,0x11306c,0x2945d0),(0xfa998,0xfa99c,0x2945d0),(0x1121ac,0x1121b0,0x2948f8),(0x112260,0x112264,0x294908),(0x112314,0x112318,0x294918)]:
  assert ap(a)+ai(c)==t;joins.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'bytes':[raw(a,4).hex(),raw(c,4).hex()]})
 assert cs(0x2945d0)=='/home/bticino/matrix_mx/MHCatalogue.db' and cs(0x294f28)=='13kobj_value_89'
 assert q(0x3103a0)==0 and q(0x3103a8)==0x314c98 and q(0x314ca0)==0x294f28 and q(0x3103b0)==0xfa970
 rs=[rel(a)for a in[0x3103a8,0x3103b0,0x314ca0]];assert all('R_AARCH64_RELATIVE'in r for r in rs)
 imports=[]
 specs=[(0xfa9c4,0x20f20,0x317270,'stat@GLIBC_2.33'),(0xfa9e4,0x22500,0x317d60,'sqlite3_open_v2'),(0xfaa0c,0x21bd0,0x3178c8,'sqlite3_prepare_v2'),(0xfaa18,0x21180,0x3173a0,'sqlite3_step'),(0xfaa38,0x20f10,0x317268,'sqlite3_column_text'),(0xfaa44,0x22360,0x317c90,'strtol@GLIBC_2.17'),(0xfaa7c,0x21c60,0x317910,'sqlite3_finalize'),(0xfaab4,0x22260,0x317c10,'sqlite3_close')]
 for pc,plt,slot,name in specs:
  assert call(pc,pc==0xfaab4)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot
  r=rel(slot);assert 'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name
  imports.append({'call':hex(pc),'bytes':raw(pc,4).hex(),'PLT':hex(plt),'PLT_bytes':raw(plt,16).hex(),'slot':hex(slot),'relocation':r})
 calls=[]
 for a,t in[(0x27ebc,0xda5f0),(0x1120f4,0xd8f10),(0x113048,0x112060),(0x113014,0x21000),(0x113088,0x20f20),(0x1130a4,0x22500),(0x1130cc,0x21bd0),(0x1130d8,0x21180),(0x1130f8,0x20f10),(0x113104,0x22360),(0x113118,0x20f10),(0x113124,0x22360),(0x113134,0x21180),(0x113144,0x21c60),(0x11314c,0x22260)]:
  assert call(a)==t;calls.append({'VA':hex(a),'target':hex(t),'bytes':raw(a,4).hex()})
 sql=cs(0x28be38);proj=sql.split(' FROM ',1)[0].removeprefix('SELECT DISTINCT ').split(', ');assert len(proj)==15 and proj[13]=='EN_KEY_OBJECT.slots'and proj[14]=='AS_OBJECT_SYSTEM.id_system'
 assert all(t in sql for t in['$modobj$','$line_modobj$','$brand_modobj$','$key_object$','ORDER BY EN_CONF.idx'])
 out['SQL_TEMPLATE.json']=J({'VA':'0x28be38','sha256_utf8':H(sql.encode()),'compiled_template':sql,'zero_based_projection':dict(enumerate(proj)),'scope':'Original compiled template, not evaluated SQL or database rows.'})
 pins={P:{'resolved':v.resolve(P),'bytes':len(b),'sha256':H(b)}}
 db='/home/bticino/matrix_mx/MHCatalogue.db';dbb=v.read_bytes(db);assert len(dbb)==2633728 and H(dbb)=='bd2ff4d326692c85bc4eb3f86504d615758da97dc832389fac523734574833e9';pins[db]={'bytes':len(dbb),'sha256':H(dbb)}
 for p in[V,O/'research/2026-11-01/first-pass/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image_path':P,'sha256':E,'PT_LOAD':[list(x)for x in ls],'spans':sp,'guards':[{'VA':hex(a),'word':hex(x)}for a,x in G],'PIC_joins':joins,'RTTI':{'header':'0x3103a0','primary_AP':'0x3103b0','RTTI':'0x314c98','name_VA':'0x294f28','name':cs(0x294f28),'relocations':rs},'import_proofs':imports,'local_call_targets':calls,'new_original_execution':0,'models':0,'fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.v2.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'PIC_joins':len(joins),'import_proofs':len(imports),'local_call_targets':len(calls),'inputs':len(pins),'new_original_execution':0}});return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');ck=p.parse_args().check;o=build();C=D/'first-candidate-v2';cp={**o,'REPORT.v2.md':(D/'REPORT.v2.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in cp.items()})
 if ck:
  for n,z in o.items():assert(D/n).read_bytes()==z,n
  assert(C/'INDEX.json').read_bytes()==ix
  for n,z in cp.items():assert(C/n).read_bytes()==z,n
 else:
  assert not C.exists()and all(not(D/n).exists()for n in o)
  for n,z in o.items():(D/n).parent.mkdir(parents=True,exist_ok=True);(D/n).open('xb').write(z)
  C.mkdir()
  for n,z in cp.items():(C/n).parent.mkdir(parents=True,exist_ok=True);(C/n).open('xb').write(z)
  (C/'INDEX.json').open('xb').write(ix)
 print(json.dumps({'check':ck,'outputs':len(o),'spans':len(SP),'guards':len(G),'new_original_execution':0}))
if __name__=='__main__':main()
