#!/usr/bin/env python3
"""Original static SCENARIO action compilation and captured registry/start callback. No execution."""
import argparse,hashlib,importlib.util,json,re,struct,subprocess,sys
from pathlib import Path
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent;P=D.parents[2];W=P.parents[2]
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
HELPER=P/'research/2026-10-31/image_vfs.py'
spec=importlib.util.spec_from_file_location('scenario_vfs',HELPER);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
IMAGE='/home/bticino/scheduling_manager/scheduling_manager';SHA='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
SPANS=[('compiled-dispatch',0xa75f0,0xa7630),('compiled-scenario',0xabc50,0xabd36),('compiled-pools',0xac7b4,0xac7c4),('scenario-runner-constructor',0x113a88,0x113c54),('functor-manager',0x113a5c,0x113a88),('scenario-invoker',0x113c54,0x113fb0),('registry-key-predicate',0xb6580,0xb65bc),('registry-value-normal-path',0xb69fc,0xb6ab0),('functor-storage',0xcd988,0xcda3c),('serializer-derived-field',0x25014,0x2503e),('serializer-pools',0x25100,0x25128)]
CALLS=[(0xabc6c,0x2af90),(0xabc9c,0x113a88),(0xabcaa,0xb444c),(0xabd32,0xa7288),(0x113b52,0xcd988),(0x113b70,0xcd990),(0x113da0,0xb6580),(0x113df8,0xb69fc),(0x113e2c,0xa5db0),(0x113e68,0xa5db0)]
GUARDS=[(0xa75f4,'cb69'),(0xa75fc,'dfe813f0'),(0xabc92,'caf82800'),(0xabca0,'6420'),(0xabcea,'3366'),(0x113b40,'e365'),(0x113b46,'2266'),(0x113b5e,'0593'),(0x113b62,'0693'),(0x113d9c,'d5e90010'),(0x113df2,'d5e90021'),(0x113e9e,'0398'),(0xb65b0,'0020'),(0xb65b2,'0120'),(0x25020,'a96a')]
def build():
 v=m.ImageVFS();b=v.read_bytes(IMAGE);assert H(b)==SHA;ph=struct.unpack_from('<I',b,28)[0];es,n=struct.unpack_from('<HH',b,42);loads=[]
 for i in range(n):
  t,o,a,pa,fs,ms,fl,al=struct.unpack_from('<8I',b,ph+i*es)
  if t==1:loads.append((a,o,fs))
 def at(a,n):
  for va,o,fs in loads:
   if va<=a and a+n<=va+fs:return b[o+a-va:o+a-va+n]
  raise ValueError(('unmapped source',hex(a),n))
 word=lambda a:struct.unpack('<I',at(a,4))[0]
 def st(a):z=at(a,128).split(b'\0')[0];assert len(z)<128;return z.decode('ascii')
 def tool(*a):return subprocess.check_output(a,text=True).replace(str(W)+'/', '')
 bp=v.root/IMAGE.lstrip('/');out={};sp=[]
 for name,a,e in SPANS:
  z=at(a,e-a);sp.append({'name':name,'start_va':hex(a),'end_va_exclusive':hex(e),'bytes':len(z),'sha256':H(z)})
  out['spans/'+name+'.txt']=tool('objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(bp)).encode()
 table=0xa7600;half=struct.unpack('<H',at(table+11*2,2))[0];assert half==0x2328 and table+half*2==0xabc50
 pic=[]
 for name,pool,pc,target in [('sceneId',0xac7b8,0xabc7e,0x1152b0),('invoker',0x113c44,0x113b66,0x113c55),('functor-manager',0x113c48,0x113b6c,0x113a5d),('serialized-sceneId',0x25110,0x2502c,0x1152b0)]:
  w=word(pool);assert(w+pc+4)&0xffffffff==target;pic.append({'name':name,'pool_va':hex(pool),'pool_word':hex(w),'add_pc_va':hex(pc),'target_va':hex(target),'literal':st(target)if name in ['sceneId','serialized-sceneId']else None})
 assert pic[0]['literal']==pic[3]['literal']=='sceneId'
 # Selected raw JSON class has44 bytes; compiled derived class has100 bytes.
 base=0x1659a4;slot=0x16610c;vt=0x164d3c
 for pool in [0xac7bc,0x113c40]:assert(base+word(pool))&0xffffffff==slot
 assert word(slot)==vt;values=[word(vt+i)for i in range(0,32,4)];assert values==[0,0x164880,0xcd849,0xcd6f1,0xcd551,0xffffffcc,0x164880,0x24fa5]
 assert st(word(0x164880+4))=='20ScenarioActionRunner'
 rr=tool('readelf','-rW',str(bp));rels=[]
 for a in [slot,vt+8,vt+12,vt+16,vt+28]:
  lines=[x for x in rr.splitlines()if re.match('^'+f'{a:08x}'+r'\s',x)];assert len(lines)==1 and 'R_ARM_RELATIVE'in lines[0];rels+=lines
 calls=[]
 for pc,target in CALLS:
  a,z=struct.unpack('<HH',at(pc,4));assert a&0xf800==0xf000 and z&0xd000==0xd000;s=(a>>10)&1;i1=1-(((z>>13)&1)^s);i2=1-(((z>>11)&1)^s);imm=(s<<24)|(i1<<23)|(i2<<22)|((a&1023)<<12)|((z&2047)<<1);got=(pc+4+imm-((1<<25)if s else 0))&0xffffffff;assert got==target;calls.append({'call_va':hex(pc),'bytes_hex':at(pc,4).hex(),'target_va':hex(target)})
 guards=[]
 for a,h in GUARDS:assert at(a,len(bytes.fromhex(h))).hex()==h;guards.append({'va':hex(a),'bytes_hex':h})
 inputs=[]
 for p,raw in [(bp,b),(HELPER,HELPER.read_bytes())]+[(P/x,(P/x).read_bytes())for x in ['research/2026-10-31-factories/factories/REPORT.md','research/2026-10-31-factories/runner/REPORT.md']]:inputs.append({'path':str(p.relative_to(W)),'bytes':len(raw),'sha256':H(raw)})
 out.update({'INPUTS.v1.json':J(inputs),'SOURCE_SPANS.v1.json':J(sp),'PIC_TARGETS.v1.json':J(pic),'DISPATCH.v1.json':J({'local_action_enum':11,'table_base_va':hex(table),'entry_va':hex(table+22),'halfword':hex(half),'target_va':'0xabc50','scope':'Original selected initializer branch, no original invocation.'}),'VTABLE.v1.json':J({'got_base_va':hex(base),'slot_va':hex(slot),'header_va':hex(vt),'words':[hex(x)for x in values],'primary_address_point':'0x164d44','secondary_at_compiled_offset52_address_point':'0x164d58','rtti':'20ScenarioActionRunner','original_relative_relocations':rels}),'DIRECT_CALLS.v1.json':J(calls),'CRITICAL_BYTES.v1.json':J(guards),'METHOD.v1.json':J({'original_execution':0,'native_entries':0,'models_or_scene_fixtures':0,'target_IO':0,'host_method':'Static fresh original Thumb2/binutils/Python bytes only. VA mapped by actual PT_LOAD; original tables and pools are data.','history':'No generated candidate correction, failed canonical generation, or overwrite.','boundary':'Selected normal-return construction/copy/registry/callback path only. Supplied context identity and live map population, weak ownership/expired handle, common runner virtual execution, provider exceptions, scene state/thread success and physical effects remain unexecuted/unproved. No complete no-stop/whole-program claim.'})})
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args();out=build();out['OUTPUT_MANIFEST.v1.json']=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()})
 if a.check:
  for n,z in out.items():assert(D/n).read_bytes()==z,n
 else:
  assert not any((D/n).exists()for n in out),'refuse existing outputs';S=D/'first-candidate';assert not S.exists();copies={**out,Path(__file__).name:Path(__file__).read_bytes()};idx=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in copies.items()})
  for n,z in out.items():p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  for n,z in copies.items():p=S/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  (S/'SNAPSHOT.json').open('xb').write(idx)
 print(json.dumps({'check':a.check,'outputs':len(out),'spans':len(SPANS),'PIC_targets':4,'direct_calls':len(CALLS),'byte_guards':len(GUARDS),'relocation_rows':5,'inputs':4,'original_execution':0}))
if __name__=='__main__':main()
