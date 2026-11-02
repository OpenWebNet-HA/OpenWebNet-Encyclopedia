#!/usr/bin/env python3
"""Exclusive F460 condition-pointer producer and complete scalar predicate source, static only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f460_condition_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/scheduling_manager/scheduling_manager';E='5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62'
SP=[('condition-common-enabled',0x4a260,0x4a2e8),('condition-common-type-row',0x4a384,0x4a3e4),('selected-raw-parser-prefix',0x10b8b0,0x10b90c),('condition-loop-own-switch',0xf974c,0xf9790),('selected-reparse-construction-publication',0xf9d6c,0xf9df4),('compiled-destination-source-prefix',0x128d20,0x128db8),('enabled-byte-and-type-copy',0x128df4,0x128e24),('compiled-primary-install-normal-return',0x128e8c,0x128eec),('pointer-vector-append',0xf9450,0xf9480),('entire-selected-predicate',0x128d10,0x128d20)]
G=[(0x4a2d4,0x3900a2a0),(0x4a3e0,0xb9002eb3),(0x10b8cc,0xaa0003f3),(0x10b908,0xf80386a0),(0xf974c,0xa941e697),(0xf976c,0xb9402c01),(0xf9770,0x71005c3f),(0xf9780,0x78615842),(0xf9788,0x8b22a822),(0xf9d78,0xaa1303e8),(0xf9d84,0x91030296),(0xf9d9c,0xd2802000),(0xf9da8,0xaa0003f8),(0xf9db8,0xf901d3f8),(0xf9dc0,0xf941d3e0),(0xf9dc4,0xb4000080),(0xf9dcc,0xf9400421),(0x128d38,0xaa0003f3),(0x128d58,0xaa0103f4),(0x128e00,0xfc42c280),(0x128e04,0x3940a281),(0x128e0c,0xfc0b4260),(0x128e18,0x3902c261),(0x128ea8,0xf9000262),(0x128eb0,0xf9004660),(0xf9450,0xa9408803),(0xf945c,0x540000c0),(0xf9460,0xf9400020),(0xf9464,0xf8008460),(0xf9468,0xf900003f),(0xf946c,0xf9000483),(0x128d10,0xd503245f),(0x128d14,0x3942c000),(0x128d18,0x52000000),(0x128d1c,0xd65f03c0)]
def build():
 v=m.ImageVFS();b=v.read_bytes(P);assert H(b)==E and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);p=r[2]+a-r[3];return b[p:p+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def q(a):return int.from_bytes(raw(a,8),'little')
 def cs(a):
  z=bytearray()
  for i in range(128):
   c=raw(a+i,1)
   if c==b'\0':return z.decode()
   z+=c
  raise AssertionError('literal cap')
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def ai(a):
  x=u(a);assert x&0xffc00000==0x91000000;return(x>>10)&4095
 def bl(a,tail=False):
  x=u(a);assert x&0xfc000000==(0x14000000 if tail else 0x94000000);i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 for a,w in G:assert u(a)==w,(hex(a),hex(u(a)),hex(w))
 out={};ss=[];hp=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='')
 for name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=z.encode();ss.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(a,e-a).hex(),'sha256':H(raw(a,e-a))})
 rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(s.strip()for s in rels.splitlines()if s.startswith(f'{a:016x} '))
 classes=[]
 for hd,rt,name,slots in[(0x212d98,0x218b40,'18BncuSceneCondition',{0:0x39d50}),(0x217300,0x21d078,'24BncuSceneConditionRunner',{0:0x129150,8:0x129070,16:0x128d10})]:
  assert q(hd)==0 and q(hd+8)==rt and cs(q(rt+8))==name;rs=[rr(hd+8),rr(rt+8)]
  for o,t in slots.items():assert q(hd+16+o)==t;rs.append(rr(hd+16+o))
  assert all('R_AARCH64_RELATIVE'in r for r in rs);classes.append({'header':hex(hd),'AP':hex(hd+16),'RTTI':hex(rt),'name':name,'name_VA':hex(q(rt+8)),'slots':{str(o):hex(t)for o,t in slots.items()},'relocations':rs})
 pp=[]
 for a,c,t in[(0x4a2a0,0x4a2a4,0x1954b0),(0x4a384,0x4a388,0x1954a8),(0x4a3a4,0x4a3a8,0x213960),(0x10b900,0x10b904,0x212da8),(0xf9778,0xf977c,0x1b5954),(0x128e98,0x128e9c,0x217310),(0x128ea0,0x128ea4,0x217338)]:
  assert ap(a)+ai(c)==t;pp.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'bytes':[raw(a,4).hex(),raw(c,4).hex()]})
 l,p=struct.unpack('<2Q',raw(0x213a80,16));assert(l,p)==(9,0x1968e8)and cs(p)=='BNCUSCENE';h=struct.unpack('<h',raw(0x1b5978,2))[0];assert h==0x177 and 0xf9790+h*4==0xf9d6c
 calls=[]
 for a,t in[(0x10b8fc,0x4a260),(0xf9d98,0x10b8b0),(0xf9dac,0x128d20),(0xf9dbc,0xf9450)]:assert bl(a)==t;calls.append({'VA':hex(a),'target':hex(t),'bytes':raw(a,4).hex()})
 assert bl(0xf947c,True)==0x10f190
 imports=[]
 for pc,plt,slot,name in[(0x4a2c8,0x24a50,0x21eb98,'_ZNK4Json5ValueixEPKc'),(0x4a2cc,0x24560,0x21e920,'_ZNK4Json5Value6asBoolEv'),(0x4a398,0x24bf0,0x21ec68,'_ZNK4Json5Value8asStringB5cxx11Ev'),(0x4a3d8,0x23db0,0x21e548,'memcmp@GLIBC_2.17'),(0xf9da0,0x24300,0x21e7f0,'_Znwm@GLIBCXX_3.4')]:
  assert bl(pc)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot;r=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(plt,16).hex(),'relocation':r})
 pins={P:{'bytes':len(b),'sha256':H(b),'resolved':v.resolve(P)}}
 for p in[V,O/'research/2026-11-01-run07-receiver/REPORT.md',O/'research/2026-11-01-run07-receiver/SOURCE.json',W/'work/f460-f461-comparison/2026-11-01-run07/reviews/f460-source-review.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image':P,'sha256':E,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'classes':classes,'PIC_joins':pp,'condition_type_row':{'row':18,'VA':'0x213a80','length':l,'literal':'BNCUSCENE','literal_VA':'0x1968e8'},'initializer_jump':{'entry_VA':'0x1b5978','halfword':h,'base':'0xf9790','target':'0xf9d6c'},'local_calls':calls,'imports':imports,'publication':{'selected_allocation_request':256,'constructor_destination':'same returned allocation base','published_pointer':'same allocation X24 via cellSP928','append_receiver':'same initializer receiver+192','entry_stride':8,'source_pointer_cleared_on_available_capacity':True,'growth_delegate':'0x10f190 body opaque'},'predicate':{'VA':'0x128d10','end_exclusive':'0x128d20','entire_bytes':raw(0x128d10,16).hex(),'scalar_source':'unsigned byte at176 XOR immediate1','conditional_boolean_interpretation':'only ordinary asBool0/1 construction and successfulsamecopy/nomutation; not arbitrarybyte logicalnot or scene-state proof'},'new_original_execution':0,'models_fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'classes':len(classes),'PIC_joins':len(pp),'imports':len(imports),'local_calls':len(calls),'inputs':len(pins),'new_original_execution':0}});return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');ck=p.parse_args().check;o=build();C=D/'first-candidate';cp={**o,'REPORT.md':(D/'REPORT.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in cp.items()})
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
