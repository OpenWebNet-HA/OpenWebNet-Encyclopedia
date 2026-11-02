#!/usr/bin/env python3
"""Exclusive static positive248writer/action-slot8 source, not caller-absence proof."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f460_scenecontrol_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/scheduling_manager/scheduling_manager';E='5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62'
SP=[('provided-receiver-entry',0xf7ad0,0xf7b20),('selected-diagnostic-prefix',0xf7b20,0xf7ba8),('normal-string-cleanup-to-writer',0xf7ba8,0xf7bd8),('positive-writer-action-requests-normal-return',0xf7bd8,0xf7c40)]
G=[(0xf7ad0,0xd503233f),(0xf7aec,0xaa0003f4),(0xf7af8,0xf9402816),(0xf7afc,0xf9402c13),(0xf7b28,0xf1003e7f),(0xf7b30,0xf100067f),(0xf7b38,0x394002c1),(0xf7b9c,0x528000a0),(0xf7bd8,0x52800021),(0xf7bdc,0x9103e280),(0xf7be0,0x089ffc01),(0xf7be4,0xa94dd293),(0xf7be8,0xeb13029f),(0xf7bf0,0xf8410660),(0xf7bf4,0xf9400001),(0xf7bf8,0xf9400421),(0xf7bfc,0xd63f0020),(0xf7c00,0xeb13029f),(0xf7c08,0xf0000920),(0xf7c18,0xeb010042),(0xf7c3c,0xd65f03c0)]
def build():
 v=m.ImageVFS();b=v.read_bytes(P);assert H(b)==E and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);p=r[2]+a-r[3];return b[p:p+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def q(a):return int.from_bytes(raw(a,8),'little')
 def bl(a):
  x=u(a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def cond(a):
  x=u(a);assert x&0xff000010==0x54000000;i=x>>5&0x7ffff;return a+((i-0x80000 if i&0x40000 else i)<<2)
 for a,w in G:assert u(a)==w,(hex(a),hex(u(a)),hex(w))
 out={};ss=[];hp=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='')
 for name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=z.encode();ss.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(a,e-a).hex(),'sha256':H(raw(a,e-a))})
 rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(s.strip()for s in rels.splitlines()if s.startswith(f'{a:016x} '))
 imports=[]
 for pc,plt,slot,name in[(0xf7bbc,0x24310,0x21e7f8,'_ZdlPvm@CXXABI_1.3.9'),(0xf7bd4,0x24310,0x21e7f8,'_ZdlPvm@CXXABI_1.3.9')]:
  assert bl(pc)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot;r=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(plt,16).hex(),'relocation':r})
 branches=[]
 for a,t in[(0xf7b34,0xf7c40),(0xf7bb0,0xf7bc0),(0xf7bc8,0xf7bd8),(0xf7bec,0xf7c08),(0xf7c04,0xf7bf0),(0xf7c20,0xf7c88)]:assert cond(a)==t;branches.append({'VA':hex(a),'target':hex(t),'word':hex(u(a))})
 assert q(0x21cc58)==0x130000;assert'R_AARCH64_RELATIVE'in rr(0x21cc58)
 # Locator only: aligned direct BL/B and ADR/short-window ADRP+ADD forms, not whole-program caller completeness.
 hits=[];adr=[];pair=[];ranges=[]
 for r in L:
  if not r[1]&1:continue
  ranges.append({'VA':hex(r[3]),'file_size':r[5]})
  for o in range(r[2],r[2]+r[5]-3,4):
   x=int.from_bytes(b[o:o+4],'little');a=r[3]+o-r[2]
   if x&0xfc000000 in(0x94000000,0x14000000):
    i=x&0x3ffffff;t=a+((i-0x4000000 if i&0x2000000 else i)<<2)
    if t==0xf7ad0:hits.append(hex(a))
   if x&0x9f000000 in(0x10000000,0x90000000):
    i=((x>>5)&0x7ffff)<<2|(x>>29&3);si=i-0x200000 if i&0x100000 else i
    if x&0x9f000000==0x10000000:
     if a+si==0xf7ad0:adr.append(hex(a))
    elif(a&~4095)+(si<<12)==0xf7000:
     for d in range(4,513,4):
      if o+d+4>r[2]+r[5]:break
      z=int.from_bytes(b[o+d:o+d+4],'little')
      if z&0xffc00000==0x91000000 and(z>>5&31)==(x&31)and(z>>10&4095)==0xad0:pair.append([hex(a),hex(a+d)])
 assert hits==[]and adr==[]and pair==[]
 pins={P:{'bytes':len(b),'sha256':H(b),'resolved':v.resolve(P)}}
 for p in[V,O/'research/2026-11-01-run07-receiver/REPORT.md',O/'research/2026-11-01-run10-action-gate/REPORT.v2.md',O/'research/2026-11-01-run03-sleep-invoker/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image':P,'sha256':E,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'imports':imports,'branches':branches,'selected_inherited_action_slot':{'slot':'0x21cc58','target':'0x130000','relocation':rr(0x21cc58),'body':'opaque; only conditional candidate if actualactionprimaryAP21cc50'},'positive_contract':{'incoming_receiver_saved_X20':'0xf7aec','release_store_1':'receiver+248 at0xf7be0','next_range':[216,224],'entry_bytes':16,'virtual_request_slot_bytes':8,'caller_and_natural_invocation':'OPEN','same_run07_scene_receiver':'explicit conditional identity premise, not proven incoming caller'},'bounded_locator':{'target':'0xf7ad0','RX_ranges':ranges,'aligned_direct_BL_B':hits,'ADR_to_entry':adr,'samebase_ADRP_ADD_512byte_window':pair,'limit':'No hit in these locator forms is not absence, deadcode, fullfunctionpointer/xref/caller proof; no candidate body expanded'},'new_original_execution':0,'models_fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'imports':len(imports),'branches':len(branches),'inputs':len(pins),'original_execution':0}});return out

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
 print(json.dumps({'check':ck,'outputs':len(o),'spans':len(SP),'guards':len(G),'original_execution':0}))
if __name__=='__main__':main()
