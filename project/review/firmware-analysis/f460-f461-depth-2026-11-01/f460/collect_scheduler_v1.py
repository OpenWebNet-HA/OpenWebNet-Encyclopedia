#!/usr/bin/env python3
"""One fresh AArch64 raw SleepAction serializer/selected initializer join. Static only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';IMG='/home/bticino/scheduling_manager/scheduling_manager';H=lambda z:hashlib.sha256(z).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('fresh_f460_scheduler_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
SPANS=[('raw-selected-construction',0x530b4,0x53128),('raw-serializer-result-type-prefix',0x37e60,0x37ed8),('raw-serializer-seconds',0x37f34,0x37f70),('initializer-serializer-reparse',0xfff2c,0xfffa8),('initializer-final-class',0xfffe4,0x10000c),('compiled-constructor-prefix',0x112a30,0x112ac0),('compiled-seconds-and-callable',0x112af0,0x112b68)]
GUARDS=[(0x37e88,'f50308aa'),(0x37f44,'813640b9'),(0x530ec,'000780d2'),(0x5310c,'b80200f9'),(0x53114,'a23600b9'),(0xfff3c,'e80315aa'),(0xfff4c,'20003fd6'),(0xfff50,'e10315aa'),(0xfff8c,'e27f05b9'),(0xfff94,'001380d2'),(0xffff8,'640200f9'),(0x112a54,'f30300aa'),(0x112a58,'f40301aa'),(0x112b24,'843640b9'),(0x112b28,'a43600b9'),(0x112b5c,'e40b00b9')]
PAIRS=[(0x530c4,0x530c8,0x212cf0),(0xfff5c,0xfff60,0x212cf0),(0xfffe8,0xfffec,0x21cc50),(0x112af4,0x112af8,0x21cc50),(0x530cc,0x530d0,0x195738),(0xfff64,0xfff68,0x195738),(0x37f50,0x37f54,0x195738),(0x37ec0,0x37ec4,0x213bf0)]
CALLS=[(0x530c0,0x496d0),(0x53100,0x4e710),(0x53120,0x52660),(0xfff58,0x496d0),(0xfff90,0x112a30),(0xfffa4,0x10def0),(0x112b64,0x1303f0)]
IMPORTS=[(0x530dc,0x24a50,0x21eb98,'_ZNK4Json5ValueixEPKc'),(0x530e0,0x23e00,0x21e570,'_ZNK4Json5Value6asUIntEv'),(0xfff74,0x24a50,0x21eb98,'_ZNK4Json5ValueixEPKc'),(0xfff78,0x23e00,0x21e570,'_ZNK4Json5Value6asUIntEv'),(0x37f4c,0x23cb0,0x21e4c8,'_ZN4Json5ValueC1Ej'),(0x37f5c,0x23ce0,0x21e4e0,'_ZN4Json5ValueixEPKc')]
def build():
 v=m.ImageVFS();b=v.read_bytes(IMG);assert H(b)=='5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62'and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];sz,n=struct.unpack_from('<HH',b,54);L=[struct.unpack_from('<II6Q',b,ph+i*sz)for i in range(n)]
 def off(a,n=1):return next(o+a-va for t,f,o,va,pa,fs,*_ in L if t==1 and va<=a and a+n<=va+fs)
 def raw(a,n):o=off(a,n);return b[o:o+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def q(a):return int.from_bytes(raw(a,8),'little')
 def cs(a):o=off(a);return b[o:b.index(0,o)].decode()
 def adrp(pc):
  z=u(pc);assert z&0x9f000000==0x90000000;i=((z>>5)&0x7ffff)<<2|(z>>29&3);return(pc&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def bl(pc):z=u(pc);assert z&0xfc000000==0x94000000;i=z&0x3ffffff;return pc+((i-0x4000000 if i&0x2000000 else i)<<2)
 hp=v.root/v.resolve(IMG).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');out={};sp=[]
 for name,a,e in SPANS:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),IMG);out['spans/'+name+'.txt']=z.encode();sp.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'file_offset':hex(off(a,e-a)),'sha256':H(raw(a,e-a))})
 for a,z in GUARDS:assert raw(a,4).hex()==z,hex(a)
 pairs=[]
 for pc,add,target in PAIRS:
  z=u(add);assert z&0xffc00000==0x91000000 and(z>>5&31)==(u(pc)&31);assert adrp(pc)+((z>>10)&4095)==target;pairs.append({'ADRP':hex(pc),'ADD':hex(add),'bytes':raw(pc,4).hex()+'/'+raw(add,4).hex(),'target':hex(target)})
 calls=[]
 for pc,t in CALLS:assert bl(pc)==t;calls.append({'VA':hex(pc),'bytes':raw(pc,4).hex(),'target':hex(t)})
 rel=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(x.strip()for x in rel.splitlines()if x.startswith(f'{a:016x} '))
 imports=[]
 for pc,plt,slot,name in IMPORTS:
  assert bl(pc)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220;assert adrp(plt)+((z>>10)&4095)*8==slot;r=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name
  imports.append({'call':hex(pc),'PLT':hex(plt),'PLT_bytes':raw(plt,16).hex(),'slot':hex(slot),'original_relocation':r})
 classes=[]
 for h,ti,np,name in[(0x212ce0,0x218aa0,0x195d78,'11SleepAction'),(0x21cc40,0x21c290,0x1b6078,'17SleepActionRunner')]:
  assert q(h)==0 and q(h+8)==ti and q(ti+8)==np and cs(np)==name
  rs=[rr(a)for a in(h+8,ti+8,h+16)];assert all('R_AARCH64_RELATIVE'in x for x in rs)
  classes.append({'header':hex(h),'AP':hex(h+16),'RTTI':hex(ti),'name':name,'primary':hex(q(h+16)),'relocations':rs})
 assert q(0x213bf0+10*16)==5 and q(0x213bf0+10*16+8)==0x196ad0 and cs(0x196ad0)=='SLEEP';assert cs(0x195738)=='seconds'
 out['SOURCE.json']=J({'image':IMG,'spans':sp,'guards':[{'VA':hex(a),'bytes':z}for a,z in GUARDS],'ADRP_ADD_pairs':pairs,'direct_BL':calls,'import_binding_proofs':imports,'classes':classes,'name_table':{'base':'0x213bf0','selected_row':10,'row_VA':'0x213c90','length':5,'pointer':'0x196ad0','literal':'SLEEP','scope':'table row position, not integer5/WHO/kind/completefactory-dispatch proof'},'ABI':'AArch64 X0this/X1source; virtualJsonreturn X8; UInt result W0. Candidate imports only; no target/provider execution.','limits':['outer switch/class-selection premise','baseparser496d0/copy4e710/move10def0/storage1303f0 remain opaque','no callback invocation/timing unit/physical meaning/wholeJSON validity or runtime ownership claim','objdump nearest PLT symbols are not accepted as actual imports; original PLT/GOT/rela checked']})
 pins={}
 for p in[V,O/'research/2026-11-01/first-pass/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 pins[IMG]={'bytes':len(b),'sha256':H(b)};out['INPUTS.json']=J(pins)
 report='''# F460 2.0.12: fresh AArch64 SleepAction schema/initializer join

One selected original scheduler path connects a raw SleepAction serializer to a same-result JSON reparse, an unsigned `seconds` field and a concrete compiled action constructor/callable-storage request. This is source analysis, not a configured scene, full factory admission proof, action invocation, timing-unit measurement or physical result. New original execution/models/fixtures are0; earlier MHS/product ledgers remain unchanged.

Original `/home/bticino/scheduling_manager/scheduling_manager` SHA256 `5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62` is fresh ELF64 AArch64. PT_LOADs,64-bit relocations and original bytes are derived afresh; no ARM32 object layout, address or harness is transferred. Curated OWN-DEV0207 supplies product context only. Receiving/transport/MQTT/libjel/auth/session/framing bodies remain closed.

## Selected raw source and actual class

Relocation-backed raw header0x212ce0/AP0x212cf0 refers to RTTI0x218aa0/name `11SleepAction`; primary slot0 is original0x37e60. The action-name table at0x213bf0 has16-byte entries. Row10 at0x213c90 is length5/string `SLEEP` at0x196ad0:5 is the string length, not the selected enum. The raw serializer reads type word40, bounds it against23 and uses this table; complete upstream parsing/selection of row10 is a premise, not reimplemented.

The selected raw-construction block0x530b4..0x53128 calls common parser0x496d0, sets that raw AP, looks up literal `seconds`0x195738 through const JsonCpp member access, requests asUInt, requests56-byte allocation/copy0x4e710, stores the returned word at raw52, reinstalls the AP and supplies the pointer to local vector helper0x52660. Those allocator/base-parser/copy/vector providers and the outer branch admission remain conditional. Nearest stripped/template names are not used to label functions.

## Serializer value to selected initializer consumer

Method0x37e60 retains rawthisX0 inX20 and hidden JSON resultX8 inX21. Its selected0x37f44..0x37f6c path loads raw52, requests `Json::Value(unsigned int)`, obtains member `seconds` in that result and requests assignment. The actual PLT at0x23cb0 resolves through slot0x21e4c8 to C1Ej; despite the displayed neighboring objdump symbol, it is not accepted as ios_base. Other scalar/default/assignment/provider behavior and full JSON coherence are not executed here.

At selected initializer0xfff2c the raw object's slot0 is called with resultX8=SP+488. The same result address is passed to common parser0x496d0 at0xfff58. The selected block then sets the temporary raw AP, reads `seconds` from that same JSON through actual const access0x24a50/GOT0x21eb98, calls actual asUInt0x23e00/GOT0x21e570 and stores its word atSP+1404 (temporary raw SP+1352+52). This is an original virtual-return/caller dataflow, not a supplied parsed-object fixture or a guarantee that all raw values round-trip successfully.

The temporary raw is passed to compiled constructor0x112a30 at0xfff90. The initializer next requests152 bytes, calls move helper0x10def0 and reinstalls compiled primary AP0x21cc50 at0xffff8. That header0x21cc40 has fresh RTTI `17SleepActionRunner`, distinct from the56-byte raw object. Append/vector ownership after this selected construction is not claimed here.

## Concrete compiled seconds and callable binding

Constructor0x112a30 saves destinationX0/sourceX1 inX19/X20. Its own code setsX21=destination+96. At0x112b24..0x112b28 it reads raw52 and stores to[X21+52], i.e. compiled148. Later0x112b38 reloads that exact word, builds a temporary callable whose manager/invoker pointers resolve0x1125f0/0x112640, stores the word into its data atSP+8 and requests local storage helper0x1303f0 at0x112b64. These are binding/storage requests; the manager/invoker/storage bodies, wait implementation and actual callback timing are not examined. The literal key `seconds` is a schema spelling, not measured elapsed behavior or proof that arbitrary UInt values are valid.

## Reproduction and limits

`python3 -B work/f460-firmware/2.0.12/research/2026-11-01-deep-scheduler/collect_scheduler_v1.py --check`

The collector checks7 source spans, selected byte guards, fresh ADRP/ADD and BL targets, raw/compiled RTTI-relative relocations, a single action-name table row and actual import PLT/GOT relocations. Source code and table/data evidence are separate. Generation is exclusive and immediately copies report/outputs/collector byte-for-byte with an index computed before opening it; --check only recomputes and compares. No canonical failed generation or overwritten candidate exists. An initial objdump probe selected an address outside .text and returned no code; no bogus source decode was used.

This is one bounded initializer/value-consumer proof. Unknown actual scene assets, JSON validity/conversion/exceptions, full switch/factory selection, import binding, raw/base/move/storage delegates, runtime objects/lifetime and physical meaning remain explicit premises/gaps. Shared MHS spellings are not a behavioral transfer. No vendor/native/provider/OS/bus/network execution occurred.
'''
 out['REPORT.md']=report.encode();out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SPANS),'guards':len(GUARDS),'ADRP_ADD':len(pairs),'direct_BL':len(calls),'import_proofs':len(imports),'classes':len(classes),'inputs':len(pins),'new_original_execution':0}});return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');ck=p.parse_args().check;o=build();C=D/'first-candidate';cp={**o,Path(__file__).name:Path(__file__).read_bytes()};ix=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in cp.items()})
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
 print(json.dumps({'check':ck,'outputs':len(o),'original_execution':0}))
if __name__=='__main__':main()
