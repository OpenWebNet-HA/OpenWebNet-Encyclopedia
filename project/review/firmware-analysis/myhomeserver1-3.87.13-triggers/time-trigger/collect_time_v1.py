#!/usr/bin/env python3
"""Static TIME trigger schema, derived class and registration argument handoff only."""
import argparse,hashlib,importlib.util,json,struct,subprocess,sys,re
from pathlib import Path
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent;P=D.parents[2];W=P.parents[2];H=lambda z:hashlib.sha256(z).hexdigest();J=lambda o:(json.dumps(o,sort_keys=True,indent=2)+'\n').encode()
HELPER=P/'research/2026-10-31/image_vfs.py';spec=importlib.util.spec_from_file_location('time_vfs',HELPER);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
IMAGE='/home/bticino/scheduling_manager/scheduling_manager';SHA='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
SPANS=[('raw-factory-discriminator',0x2e9fc,0x2eac0),('raw-special-allocation',0x2f7ec,0x2f842),('raw-special-pools',0x2f954,0x2f960),('base-trigger-json',0x2c678,0x2c904),('time-json-parser',0x2d140,0x2d298),('raw-base-copy',0x2df3c,0x2e014),('time-serializer',0x29af0,0x29d50),('initializer-dispatch',0xa731e,0xa735e),('compiled-time-handoff',0xa8108,0xa8338),('compiled-time-pools',0xa8af0,0xa8b10),('compiled-time-constructor',0xb8e7c,0xb908c)]
PIC=[('time',0x2d284,0x2d170,'time'),('days',0x2d288,0x2d1b0,'days'),('enabled',0x2c8d8,0x2c6a6,'enabled'),('id-presence',0x2c8dc,0x2c6d0,'id'),('id',0x2c8e0,0x2c6e2,'id'),('type',0x2c8e8,0x2c748,'type'),('operator',0x2c8f0,0x2c79a,'operator'),('serialized-time',0x29d40,0x29bd8,'time'),('serialized-days',0x29d44,0x29c62,'days')]
CALLS=[(0x2f7f0,0x2d140),(0x2f7fe,0x2df3c),(0x2f82a,0x2e84c),(0x2d164,0x2c678),(0xa813e,0xb43d8),(0xa815a,0x2d140),(0xa816c,0xb8e7c),(0xa830e,0xb9814),(0xb8fa0,0xb8be0)]
GUARDS=[(0x2eab4,'013c'),(0x2eab6,'162c'),(0x2eab8,'00f29886'),(0x2f7f4,'4420'),(0x2d1c2,'0628'),(0x2d1dc,'302a'),(0x2d1e0,'312a'),(0x2d1f2,'2064'),(0xa81a2,'7020'),(0xa829e,'c7e900a8'),(0xa82ca,'c6e900a8'),(0xa82e6,'de66'),(0xb8f3a,'84f83030'),(0xb8f90,'6265'),(0xb8f98,'c4ed160b')]
def build():
 v=m.ImageVFS();b=v.read_bytes(IMAGE);assert H(b)==SHA;ph=struct.unpack_from('<I',b,28)[0];sz,n=struct.unpack_from('<HH',b,42);loads=[]
 for i in range(n):
  t,o,a,pa,fs,ms,f,al=struct.unpack_from('<8I',b,ph+i*sz)
  if t==1:loads.append((a,o,fs))
 def at(a,n):
  for va,o,s in loads:
   if va<=a and a+n<=va+s:return b[o+a-va:o+a-va+n]
  raise ValueError(hex(a))
 w=lambda a:struct.unpack('<I',at(a,4))[0]
 def st(a):z=at(a,128).split(b'\0')[0];assert len(z)<128;return z.decode('ascii')
 bp=v.root/IMAGE.lstrip('/');out={};sp=[]
 for name,a,e in SPANS:
  sp.append({'name':name,'start_va':hex(a),'end_va_exclusive':hex(e),'bytes':e-a,'sha256':H(at(a,e-a))});out['spans/'+name+'.txt']=subprocess.check_output(['objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(bp)],text=True).replace(str(W)+'/', '').encode()
 pools=[]
 for name,pool,pc,literal in PIC:
  target=(w(pool)+pc+4)&0xffffffff;assert st(target)==literal;pools.append({'name':name,'pool_va':hex(pool),'word':hex(w(pool)),'add_pc_va':hex(pc),'target_va':hex(target),'literal':literal})
 # Independently rederive the two distinct local enum zero routes.
 assert w(0x160450)==4 and st(w(0x160454))=='TIME';assert struct.unpack('<H',at(0xa732e,2))[0]==0x6ed and 0xa732e+2*0x6ed==0xa8108
 callbacks=[]
 for pool,pc,target in [(0xa8af0,0xa8120,0xa60a9),(0xa8af4,0xa8124,0xa56c1)]:assert(w(pool)+pc+4)&0xffffffff==target;callbacks.append({'pool_va':hex(pool),'add_pc_va':hex(pc),'target_thumb_pointer':hex(target)})
 rel=subprocess.check_output(['readelf','-rW',str(bp)],text=True);vt=[]
 for name,pools_,header,want in [('raw-TimeTrigger',[0x2f95c,0xb9078,0xa8b04],0x1603dc,'11TimeTrigger'),('compiled-TimeTriggerRunner',[0xa8b08],0x161e5c,'17TimeTriggerRunner')]:
  chains=[]
  for pool in pools_:
   slot=(0x1659a4+w(pool))&0xffffffff;assert w(slot)==header;lines=[x for x in rel.splitlines()if re.match('^'+f'{slot:08x}'+r'\s',x)];assert len(lines)==1 and 'R_ARM_RELATIVE'in lines[0];chains.append({'pool_va':hex(pool),'got_slot_va':hex(slot),'relocation':lines[0]})
  rt=w(header+4);assert st(w(rt+4))==want;vt.append({'name':name,'header_va':hex(header),'rtti_va':hex(rt),'rtti_name':want,'words':[hex(w(header+i))for i in range(0,40,4)],'chains':chains})
 assert vt[0]['words'][4]=='0x29af1';assert(w(0xb907c)+0xb8f8a+4)&0xffffffff==0x161e5c
 calls=[]
 for pc,want in CALLS:
  a,z=struct.unpack('<HH',at(pc,4));assert a&0xf800==0xf000 and z&0xd000==0xd000;s=(a>>10)&1;i1=1-(((z>>13)&1)^s);i2=1-(((z>>11)&1)^s);imm=(s<<24)|(i1<<23)|(i2<<22)|((a&1023)<<12)|((z&2047)<<1);assert(pc+4+imm-((1<<25)if s else 0))&0xffffffff==want;calls.append({'call_va':hex(pc),'bytes_hex':at(pc,4).hex(),'target_va':hex(want)})
 guards=[]
 for a,h in GUARDS:assert at(a,len(bytes.fromhex(h))).hex()==h;guards.append({'va':hex(a),'bytes_hex':h})
 inputs=[]
 for p,z in [(bp,b),(HELPER,HELPER.read_bytes())]+[(P/q,(P/q).read_bytes())for q in ['research/2026-10-31-factories/factories/REPORT.md','research/2026-10-31-factories/runner/REPORT.md']]:inputs.append({'path':str(p.relative_to(W)),'bytes':len(z),'sha256':H(z)})
 out.update({'INPUTS.v1.json':J(inputs),'SOURCE_SPANS.v1.json':J(sp),'PIC_KEYS.v1.json':J(pools),'VTABLE_CHAINS.v1.json':J(vt),'CALLBACK_TARGETS.v1.json':J(callbacks),'DIRECT_CALLS.v1.json':J(calls),'CRITICAL_BYTES.v1.json':J(guards),'METHOD.v1.json':J({'original_execution':0,'host_models':0,'scene_or_calendar_fixtures':0,'scope':'Raw TIME localenum0; selected compiled constructor/aggregate/registration argument handoff. No calendar-preparation or framework registration implementation/firing analysis. No new runtime/physical validity claim.','history':'One exploratory disassembly slice began inside a Thumb BL; its first bogus decode was discarded. All retained spans start at verified instruction/function boundaries. No generated candidate failed or was overwritten.','code_mode':'Fresh original Thumb2/PT_LOAD; literal/TBH tables are data. JsonCpp/allocation/string/callback delegates unexecuted. No old firmware object layout reused.'})})
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args();out=build();out['OUTPUT_MANIFEST.v1.json']=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()})
 if a.check:
  for n,z in out.items():assert(D/n).read_bytes()==z,n
 else:
  assert not any((D/n).exists()for n in out),'refuse overwrite';S=D/'first-candidate';assert not S.exists();copies={**out,Path(__file__).name:Path(__file__).read_bytes()};idx=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in copies.items()})
  for n,z in out.items():p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  for n,z in copies.items():p=S/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  (S/'SNAPSHOT.json').open('xb').write(idx)
 print(json.dumps({'check':a.check,'outputs':len(out),'spans':len(SPANS),'PIC_keys':len(PIC),'vtables':2,'relocation_chains':4,'direct_calls':len(CALLS),'byte_guards':len(GUARDS),'inputs':4,'original_execution':0}))
if __name__=='__main__':main()
