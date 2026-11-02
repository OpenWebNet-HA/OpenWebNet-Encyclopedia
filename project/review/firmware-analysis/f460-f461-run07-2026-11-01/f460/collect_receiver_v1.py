#!/usr/bin/env python3
"""Exclusive F460 captured receiver/owner/gate/thread-state source proof. Static only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f460_receiver_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/scheduling_manager/scheduling_manager';E='5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62'
SP=[('selected-owner-allocation',0x2cc20,0x2cc98),('owner-constructor',0x105740,0x1057a8),('alternative-constructor',0x105690,0x1056f8),('gate-and-thread-state-request',0xf7650,0xf774c),('previous-holder-nonzero-branch',0xf79b8,0xf79c0),('condition-worker-entry',0xf8cb0,0xf8d6c),('single-pointer-dispatch',0xf8edc,0xf8f20),('single-predicate-tail',0xf90b4,0xf90d4),('normal-true-path-local-handoff',0xf8f00,0xf9058)]
G=[(0x2cc20,0xd2802200),(0x2cc38,0xaa0003f8),(0x2cc58,0xf8010703),(0x2cc6c,0xaa1803e0),(0x2cc90,0xa90683f8),(0x105750,0xaa0003f3),(0x10576c,0x7901f27f),(0x105774,0x3903ea7f),(0x105780,0xaa1303e0),(0x10578c,0x3c8e8260),(0x1056a0,0xaa0003f3),(0x1056bc,0x7901f27f),(0xf766c,0xaa0003f3),(0xf7670,0x3941c400),(0xf7688,0x08dffc01),(0xf7698,0x089ffc01),(0xf76a0,0x089ffc1f),(0xf76a4,0xd2800100),(0xf76b0,0xd2800200),(0xf76b4,0xf900029f),(0xf76d4,0xa9004c64),(0xf76dc,0xf90003e3),(0xf76e8,0xb4000080),(0xf76f4,0xd63f0020),(0xf76f8,0xf9407a60),(0xf76fc,0xf9007a74),(0xf7704,0xf9400001),(0xf7708,0xb5001581),(0xf770c,0xd2800101),(0xf8cc4,0xf9400403),(0xf8cd4,0xa94c5873),(0xf8cec,0x9345fc14),(0xf8ef4,0xf100041f),(0xf90b4,0xf9400260),(0xf90bc,0xf9400821),(0xf90c0,0xd63f0020),(0xf90c4,0x72001c1f),(0xf90cc,0xf94006a3),(0xf903c,0xf94006a0)]
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
 def bl(a,tail=False):
  x=u(a);assert x&0xfc000000==(0x14000000 if tail else 0x94000000);i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 for a,w in G:assert u(a)==w,(hex(a),hex(u(a)),hex(w))
 out={};ss=[];hp=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='')
 for name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=z.encode();ss.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(a,e-a).hex(),'sha256':H(raw(a,e-a))})
 rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(s.strip()for s in rels.splitlines()if s.startswith(f'{a:016x} '))
 tables=[]
 for header,rtti,expected,slots in[(0x213440,0x2190d0,'St23_Sp_counted_ptr_inplaceI11SceneRunnerSaIS0_ELN9__gnu_cxx12_Lock_policyE2EE',{0:0x30680,8:0x31290,16:0x314d0}),(0x216f70,0x21cc90,'*NSt6thread11_State_implINS_8_InvokerISt5tupleIJZN11SceneRunner21verifySceneConditionsEvEUlvE_EEEEEE',{0:0xf6bf0,8:0xf6c10,16:0xf8cb0})]:
  assert q(header)==0 and q(header+8)==rtti and cs(q(rtti+8))==expected;rs=[rr(header+8),rr(rtti+8)]
  for off,t in slots.items():assert q(header+16+off)==t;rs.append(rr(header+16+off))
  assert all('R_AARCH64_RELATIVE'in r for r in rs);tables.append({'header':hex(header),'AP':hex(header+16),'RTTI':hex(rtti),'name':expected,'name_VA':hex(q(rtti+8)),'slots':{str(o):hex(t)for o,t in slots.items()},'relocations':rs})
 pp=[]
 for a,c,t in[(0x2cc3c,0x2cc40,0x213450),(0xf76c0,0xf76c4,0x216f70)]:
  assert ap(a)+ai(c)==t;pp.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'bytes':[raw(a,4).hex(),raw(c,4).hex()]})
 assert u(0xf76cc)==0x91004084 # explicit AP+16 after header construction
 cc=[]
 for a,t in[(0x2cc70,0x105740),(0x105760,0x10fe60),(0x105790,0xf94c0),(0x1056b0,0x54050),(0x1056e0,0xf94c0)]:
  assert bl(a)==t;cc.append({'BL':hex(a),'target':hex(t),'bytes':raw(a,4).hex()})
 assert bl(0xf9054,True)==0xf84d0
 imports=[]
 for pc,plt,slot,name,tail in[(0x2cc28,0x24300,0x21e7f0,'_Znwm@GLIBCXX_3.4',False),(0xf76a8,0x24300,0x21e7f0,'_Znwm@GLIBCXX_3.4',False),(0xf76b8,0x24300,0x21e7f0,'_Znwm@GLIBCXX_3.4',False),(0xf76e0,0x24240,0x21e790,'_ZNSt6thread15_M_start_threadESt10unique_ptrINS_6_StateESt14default_deleteIS1_EEPFvvE@GLIBCXX_3.4.22',False),(0xf7710,0x24310,0x21e7f8,'_ZdlPvm@CXXABI_1.3.9',False),(0xf7748,0x24af0,0x21ebe8,'_ZNSt6thread6detachEv@GLIBCXX_3.4.11',True),(0xf79bc,0x23ba0,0x21e440,'_ZSt9terminatev@GLIBCXX_3.4',False)]:
  assert bl(pc,tail)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot;r=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'call':hex(pc),'tail':tail,'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(plt,16).hex(),'relocation':r})
 branches=[]
 for a,t in[(0xf7680,0xf7828),(0xf7690,0xf774c),(0xf7708,0xf79b8),(0xf8ef8,0xf90b4),(0xf90c8,0xf8d6c)]:
  x=u(a);assert x&0xff000010 in(0x54000000,0xb4000000,0xb5000000)or x&0x7f000000 in(0x34000000,0x35000000);i=(x>>5)&0x7ffff;i-=0x80000 if i&0x40000 else 0;assert a+(i<<2)==t;branches.append({'VA':hex(a),'bytes':raw(a,4).hex(),'target':hex(t)})
 pins={P:{'sha256':H(b),'bytes':len(b),'resolved':v.resolve(P)}}
 for p in[V,O/'research/2026-11-01-run06-trigger/REPORT.md',O/'research/2026-11-01-run06-trigger/SOURCE.json',W/'work/f460-f461-comparison/2026-11-01-run06/reviews/f460-source-review.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image':P,'sha256':E,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'tables':tables,'PIC_joins':pp,'direct_calls':cc,'import_proofs':imports,'branches':branches,'next_local_tail':{'VA':'0xf9054','target':'0xf84d0','body_not_audited':True},'contract':{'owner_allocation_bytes':272,'inner_offset':16,'inner_storage_bytes':256,'state_allocation_bytes':16,'state_receiver_offset':8,'thread_holder_offset':240,'condition_pointer_range_offsets':[192,200],'selected_case':'one remaining valid condition pointer, ordinary predicate low8true and normal intermediate returns, no fixture supplied','gate_offsets':[113,249],'stores_before_thread_request':{'249':1,'248':0},'constructor_initialization':'248/249/250 and newlocal pointer/vector storagezero; not a global reset/lifetime proof'},'new_original_execution':0,'models_fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'tables':len(tables),'PIC_joins':len(pp),'direct_calls':len(cc),'imports':len(imports),'branches':len(branches),'inputs':len(pins),'original_execution':0}});return out

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
