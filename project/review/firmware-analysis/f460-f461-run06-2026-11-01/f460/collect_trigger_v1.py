#!/usr/bin/env python3
"""Exclusive F460 BNIL factory/compiled/local-admission source proof. Static only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f460_trigger_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/scheduling_manager/scheduling_manager';E='5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62'
SP=[('raw-factory-admission',0x4f5f8,0x4f680),('raw-factory-switch',0x4f79c,0x4f7b8),('selected-raw-factory',0x502f0,0x5033c),('raw-common-enabled-type',0x4ba70,0x4bc10),('raw-status-parser',0x4c100,0x4c234),('raw-copy-fields',0x4e328,0x4e37c),('raw-virtual-result-ABI',0x48bd0,0x48c48),('initializer-entry-and-switch',0xf94c0,0xf9540),('callback-virtual-result-reparse',0xfac10,0xfacac),('compiled-constructor',0x15dbd0,0x15dd00),('compiled-aggregate-handoff',0xfad18,0xfadb8),('callback-copy-helper',0x10ddd0,0x10de20),('callback-pointer-manager',0xf6cb0,0xf6cf4),('callback-local-receiver-tail',0xf7ac0,0xf7acc),('compiled-primary-callback',0x15dba0,0x15dbcc),('local-string-admission',0x15dda0,0x15debc),('selected-local-caller',0x8474c,0x847e8),('ID-byte-comparison',0x7e750,0x7e7a0)]
G=[(0x4f620,0x911bc37b),(0x4f630,0x9100437b),(0x4f674,0x5100075a),(0x4f678,0x71005f5f),(0x50304,0xd2800700),(0x50324,0xf9000353),(0x5032c,0xb9003742),(0x4bae4,0x3900a2a0),(0x4bbf0,0xb9002eb3),(0x4c144,0xb9003661),(0x4c1fc,0xb9003661),(0xf951c,0xb9402c00),(0xf9520,0x7100601f),(0xf9530,0x78605821),(0xf9538,0x8b21a801),(0xfac44,0xf90b4bf4),(0xfac4c,0xf90b53e3),(0xfac50,0xf90b57e2),(0xfac64,0xaa1303e8),(0xfac6c,0xf9400821),(0xfac70,0xd63f0020),(0xfaca4,0xf90c07e3),(0x15dcb4,0x39014264),(0x15dcb8,0xfc054260),(0x15dcc8,0xb9005e64),(0xfad20,0xd2800e00),(0xfad50,0xf8010700),(0xfad94,0xb9003780),(0xfada8,0xf9000ac3),(0xfadac,0xf9001702),(0x10ddec,0x52800042),(0x10de00,0xd63f0060),(0xf6cd0,0xf9400021),(0xf6cd4,0xf9000001),(0xf7ac4,0xf9400000),(0x15dda4,0x39414002),(0x15ddac,0xf9400422),(0x15ddc0,0xf100085f),(0x15ddc8,0xf1000c5f),(0x15ddd8,0x528dcde1),(0x15ddf0,0x528ccde2),(0x15de00,0x7101983f),(0x15de30,0xb9405802),(0x15de34,0x51000421),(0x15de38,0x7100085f),(0x15de40,0x71000c5f),(0x15de60,0xf9400c01),(0x15de6c,0xf9400c01),(0x15de80,0xb9405c02),(0x15de94,0x6b01005f),(0x84774,0xd37cef7b),(0x84778,0xf87b681b),(0x847bc,0x9100c363),(0x847d8,0x91004321)]
def build():
 v=m.ImageVFS();b=v.read_bytes(P);assert H(b)==E and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);p=r[2]+a-r[3];return b[p:p+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def q(a):return int.from_bytes(raw(a,8),'little')
 def cs(a):
  z=bytearray()
  for i in range(192):
   c=raw(a+i,1)
   if c==b'\0':return z.decode()
   z+=c
  raise AssertionError('literal cap')
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def ai(a):
  x=u(a);assert x&0xffc00000==0x91000000;return(x>>10)&4095
 def bl(a):
  x=u(a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 for a,w in G:assert u(a)==w,(hex(a),hex(u(a)),hex(w))
 out={};ss=[];hp=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='')
 for name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=z.encode();ss.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(a,e-a).hex(),'sha256':H(raw(a,e-a))})
 rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(s.strip()for s in rels.splitlines()if s.startswith(f'{a:016x} '))
 defs=[]
 for header,rtti,name,apoint,slots in[(0x214190,0x219730,'11BnilTrigger',0x2141a0,{16:0x48bd0}),(0x214158,0x219718,'15BaseBnilTrigger',0x214168,{}),(0x217ef8,0x21d920,'17BnilTriggerRunner',0x217f08,{0:0x15dba0})]:
  assert q(header)==0 and q(header+8)==rtti and cs(q(rtti+8))==name
  rows=[rr(header+8),rr(rtti+8)]
  for off,t in slots.items():assert q(apoint+off)==t;rows.append(rr(apoint+off))
  assert all('R_AARCH64_RELATIVE'in r for r in rows);defs.append({'header':hex(header),'RTTI':hex(rtti),'name':name,'name_VA':hex(q(rtti+8)),'AP':hex(apoint),'selected_slots':{str(o):hex(t)for o,t in slots.items()},'relocations':rows})
 assert q(0x21ee10)==0x217ef8 and q(0x21edb8)==0x21d920
 pp=[]
 for a,c,t in[(0x4f61c,0x4f620,0x2136f0),(0x4f79c,0x4f7a0,0x196d44),(0x502fc,0x50300,0x2141a0),(0xf9528,0xf952c,0x1b5920),(0xfac14,0xfac18,0xf7ac0),(0xfac1c,0xfac20,0xf6cb0),(0xfac88,0xfac8c,0x2141a0),(0x15dc90,0x15dc94,0x217f08),(0x15dca0,0x15dca4,0x217f30),(0x15de4c,0x15de50,0x15dba0)]:
  assert ap(a)+ai(c)==t;pp.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'bytes':[raw(a,4).hex(),raw(c,4).hex()]})
 row=struct.unpack('<2Q',raw(0x213700,16));assert row==(4,0x196828)and cs(row[1])=='BNIL'
 jt=[]
 for a,base,t in[(0x196d44,0x4f7b8,0x502f0),(0x1b5922,0xf9540,0xfac10)]:
  h=struct.unpack('<h',raw(a,2))[0];assert base+h*4==t;jt.append({'entry_VA':hex(a),'signed_halfword':h,'base':hex(base),'target':hex(t),'bytes':raw(a,2).hex()})
 cc=[]
 for a,t in[(0x502f8,0x4c100),(0x50318,0x4e2b0),(0x50338,0x4f030),(0xfac58,0x10ddd0),(0xfac84,0x4c100),(0xfaca8,0x15dbd0),(0xfad64,0x10ddd0),(0xfad78,0x4e2b0),(0xfadb4,0xf6d00),(0x847cc,0x7e750),(0x847e0,0x15dda0)]:
  assert bl(a)==t;cc.append({'BL':hex(a),'target':hex(t),'bytes':raw(a,4).hex()})
 x=u(0xf7ac8);assert x&0xfc000000==0x14000000;i=x&0x3ffffff;i-=0x4000000 if i&0x2000000 else 0;assert 0xf7ac8+(i<<2)==0xf7650
 imports=[]
 for pc,plt,slot,name in[(0x4bad8,0x24a50,0x21eb98,'_ZNK4Json5ValueixEPKc'),(0x4badc,0x24560,0x21e920,'_ZNK4Json5Value6asBoolEv'),(0x4c15c,0x24bf0,0x21ec68,'_ZNK4Json5Value8asStringB5cxx11Ev'),(0x4f650,0x23db0,0x21e548,'memcmp@GLIBC_2.17'),(0x84798,0x243f0,0x21e868,'__dynamic_cast@CXXABI_1.3'),(0x7e784,0x23db0,0x21e548,'memcmp@GLIBC_2.17')]:
  assert bl(pc)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot;r=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(plt,16).hex(),'relocation':r})
 literals={hex(a):cs(a)for a in[0x1954a8,0x1954b0,0x1954e8,0x198258]};assert list(literals.values())==['type','enabled','status','id']
 pins={P:{'sha256':H(b),'bytes':len(b),'resolved':v.resolve(P)}}
 for p in[V,O/'research/2026-11-01-deep-scheduler/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image':P,'sha256':E,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'classes':defs,'PIC_joins':pp,'jump_entries':jt,'raw_type_row':{'VA':'0x213700','row':1,'length':4,'literal':'BNIL','literal_VA':'0x196828'},'direct_calls':cc,'import_proofs':imports,'safe_literals':literals,'callback_tail':{'B':'0xf7ac8','target':'0xf7650','body_not_audited':True},'selected_scope':'valid local supplied raw/compiled/string/callback objects and ordinary providers; no event/JSON/wire/runtime acceptance','new_original_execution':0,'models_fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'classes':len(defs),'PIC_joins':len(pp),'jump_entries':len(jt),'local_calls':len(cc),'imports':len(imports),'inputs':len(pins),'new_original_execution':0}});return out

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
