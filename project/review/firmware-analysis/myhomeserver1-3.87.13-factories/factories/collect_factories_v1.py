#!/usr/bin/env python3
"""Fresh scheduler static action factories. Exclusive immutable output; --check is read-only."""
import argparse,hashlib,importlib.util,json,re,struct,subprocess,sys
from pathlib import Path
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent;P=D.parents[2];W=P.parents[2]
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda o:(json.dumps(o,sort_keys=True,indent=2)+'\n').encode()
HELPER=P/'research/2026-10-31/image_vfs.py'
spec=importlib.util.spec_from_file_location('factory_source_vfs',HELPER);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
IMAGE='/home/bticino/scheduling_manager/scheduling_manager'
EXPECTED='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
SPANS=[('trigger-discrimination',0x2e9fc,0x2eb00),('condition-discrimination',0x2fa4c,0x2fb40),('action-discrimination',0x30cb0,0x30da8),('action-cleanup-and-advance',0x30e34,0x30eba),('selected-scenario-and-sleep',0x31406,0x314a6),('base-action-json',0x2af90,0x2b0b4),('base-action-copy',0x2e1ac,0x2e274),('pointer-vector-append',0x30c8c,0x30cb0),('trigger-pools',0x2f630,0x2f644),('condition-pools',0x306a0,0x306b4),('action-pools',0x31950,0x319ec)]
PIC=[('action-type',0x3195c,0x30cf2,'type'),('base-id',0x2b09c,0x2afb8,'id'),('base-delay',0x2b0a0,0x2afd4,'delay'),('base-duration',0x2b0a4,0x2afe4,'duration'),('base-type',0x2b0a8,0x2aff6,'type'),('sleep-seconds',0x319e4,0x3146c,'seconds'),('scenario-id',0x319dc,0x3141c,'sceneId')]
TABLES=[('triggers',0x2f630,0x2ea20,0x2f640,0x166978,0x160450,24),('conditions',0x306a0,0x2fa70,0x306b0,0x166b68,0x1605b0,23),('actions',0x31958,0x30cd0,0x31968,0x166650,0x160710,24)]
CALLS=[(0x3140a,0x2af90),(0x3143e,0x2e1ac),(0x31450,0x30c8c),(0x3145a,0x2af90),(0x3148e,0x2e1ac),(0x314a0,0x30c8c)]
GUARDS=[(0x30d74,'dfe814f0'),(0x31430,'2c20'),(0x31480,'2c20'),(0x3144c,'b362'),(0x3149c,'b362'),(0x2afd2,'fb61'),(0x2afe0,'3862'),(0x2aff2,'7b62'),(0x2b02e,'fc61'),(0x30c8c,'d0e90132'),(0x30c9a,'43f8040b'),(0x30c9e,'0a60'),(0x30ca0,'ccf80430')]
def build():
 v=m.ImageVFS();b=v.read_bytes(IMAGE);assert H(b)==EXPECTED
 phoff=struct.unpack_from('<I',b,28)[0];sz,n=struct.unpack_from('<HH',b,42);loads=[]
 for i in range(n):
  t,o,a,pa,fs,ms,fl,al=struct.unpack_from('<8I',b,phoff+i*sz)
  if t==1:loads.append((a,o,fs,fl))
 def at(a,n):
  for va,o,fs,fl in loads:
   if va<=a and a+n<=va+fs:return b[o+a-va:o+a-va+n]
  raise ValueError(('original unmapped range',hex(a),n))
 def word(a):return struct.unpack('<I',at(a,4))[0]
 def cstr(a):
  z=at(a,128).split(b'\0')[0];assert len(z)<128;return z.decode('ascii')
 def tool(*args):return subprocess.run(args,check=True,capture_output=True,text=True).stdout.replace(str(W)+'/', '')
 binpath=v.root/IMAGE.lstrip('/');out={};sp=[]
 for name,a,e in SPANS:
  raw=at(a,e-a);sp.append({'name':name,'start_va':hex(a),'end_va_exclusive':hex(e),'bytes':len(raw),'sha256':H(raw)})
  out['spans/'+name+'.txt']=tool('objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(binpath)).encode()
 pools=[]
 for name,pool,pc,want in PIC:
  target=(word(pool)+pc+4)&0xffffffff;assert cstr(target)==want
  pools.append({'name':name,'pool_va':hex(pool),'pool_word':hex(word(pool)),'add_pc_va':hex(pc),'target_va':hex(target),'literal':want})
 reloc=tool('readelf','-rW',str(binpath));tables=[]
 for name,bpool,pc,tpool,slot,tab,count in TABLES:
  base=(word(bpool)+pc+4)&0xffffffff;assert base==0x1659a4;assert(base+word(tpool))&0xffffffff==slot;assert word(slot)==tab
  assert re.search(r'^'+f'{slot:08x}'+r'\s+.*R_ARM_RELATIVE',reloc,re.M)
  rows=[]
  for i in range(count):
   size,ptr=struct.unpack('<II',at(tab+i*8,8));s=cstr(ptr);assert len(s.encode())==size
   rows.append({'index':i,'length':size,'name':s,'row_va':hex(tab+i*8),'name_va':hex(ptr)})
  tables.append({'family':name,'got_base':hex(base),'base_pool_va':hex(bpool),'add_pc_va':hex(pc),'slot_offset_pool_va':hex(tpool),'got_slot_va':hex(slot),'slot_relocation':'R_ARM_RELATIVE','table_va':hex(tab),'rows':rows,'scope':'Local enum declarations, not exhaustive runtime support or public WHO/type namespace.'})
 action=tables[2]['rows'];selected=[]
 for index,want,target in [(7,'TIME',0x30e58),(10,'SLEEP',0x31456),(11,'SCENARIO',0x31406)]:
  assert action[index]['name']==want;entry=struct.unpack('<H',at(0x30d78+index*2,2))[0];assert 0x30d78+entry*2==target
  selected.append({'local_index':index,'name':want,'tbh_instruction_va':'0x30d74','table_base_va':'0x30d78','entry_va':hex(0x30d78+index*2),'entry_value':entry,'target_va':hex(target),'scope':'Selected source branch, not invocation or full support statement.'})
 # Both caller and base-action constructor select the SAME enum table.
 assert(0x1659a4+word(0x2b0ac))&0xffffffff==0x166650
 vtables=[]
 for name,pool,slot,tab,entry,typename in [('SLEEP',0x319e0,0x16651c,0x15ffb0,0x24c9d,'11SleepAction'),('SCENARIO',0x319d8,0x166f00,0x15ffa4,0x24fa5,'14ScenarioAction')]:
  assert(0x1659a4+word(pool))&0xffffffff==slot;assert word(slot)==tab;assert word(tab)==0;assert word(tab+8)==entry
  ti=word(tab+4);nameptr=word(ti+4);assert cstr(nameptr)==typename
  assert re.search(r'^'+f'{slot:08x}'+r'\s+.*R_ARM_RELATIVE',reloc,re.M)
  vtables.append({'name':name,'offset_pool_va':hex(pool),'got_slot_va':hex(slot),'vtable_header_va':hex(tab),'stored_address_point_va':hex(tab+8),'typeinfo_va':hex(ti),'typeinfo_name_va':hex(nameptr),'typeinfo_name':typename,'first_function_pointer':hex(entry),'scope':'Original vtable/typeinfo identity; selected first method is not treated as an action execution entry.'})
 calls=[]
 for pc,want in CALLS:
  a,z=struct.unpack('<HH',at(pc,4));assert a&0xf800==0xf000 and z&0xd000==0xd000
  s=(a>>10)&1;i1=1-(((z>>13)&1)^s);i2=1-(((z>>11)&1)^s);imm=(s<<24)|(i1<<23)|(i2<<22)|((a&1023)<<12)|((z&2047)<<1)
  target=(pc+4+imm-((1<<25)if s else 0))&0xffffffff;assert target==want
  calls.append({'call_va':hex(pc),'bytes_hex':at(pc,4).hex(),'target_va':hex(target)})
 guards=[]
 for va,h in GUARDS:assert at(va,len(bytes.fromhex(h))).hex()==h;guards.append({'va':hex(va),'bytes_hex':h})
 provider='/usr/lib/libjsoncpp.so.1.9.5';pb=v.read_bytes(provider);assert H(pb)=='5916ac361655304327bbf9b2632c1724e49e25b3dd2a10bb27aaa815503ebc36'
 ds=tool('readelf','-dW',str(binpath));sy=tool('readelf','-WsW',str(binpath));ps=tool('readelf','-WsW',str(v.root/provider.lstrip('/')))
 required=['_ZNK4Json5Value6asUIntEv','_ZNK4Json5Value8asStringB5cxx11Ev','_ZNK4Json5ValueixEPKc']
 declarations=[]
 for sym in required:
  aa=[x for x in sy.splitlines()if x.rstrip().endswith(sym)];bb=[x for x in ps.splitlines()if x.rstrip().endswith(sym)];assert aa and bb;declarations.append({'symbol':sym,'scheduler_declaration':aa,'packaged_candidate_definition':bb})
 predecessor=P/'research/2026-10-31-consumers/scheduler/REPORT.md'
 inputs=[]
 for p,raw in [(binpath,b),(v.root/provider.lstrip('/'),pb),(HELPER,HELPER.read_bytes()),(predecessor,predecessor.read_bytes())]:inputs.append({'path':str(p.relative_to(W)),'bytes':len(raw),'sha256':H(raw)})
 out.update({'INPUTS.v1.json':J(inputs),'SOURCE_SPANS.v1.json':J(sp),'PIC_LITERALS.v1.json':J(pools),'LOCAL_ENUM_TABLES.v1.json':J(tables),'SELECTED_DISPATCH.v1.json':J(selected),'VTABLE_IDENTITIES.v1.json':J(vtables),'DIRECT_CALLS.v1.json':J(calls),'CRITICAL_BYTES.v1.json':J(guards),'PROVIDERS.v1.json':J({'needed':re.findall(r'\(NEEDED\).*?\[(.*?)\]',ds),'jsoncpp_image_path':provider,'jsoncpp_sha256':H(pb),'declarations_and_candidate_definitions':declarations,'boundary':'Static declarations and packaged definitions, no live loader/interposition/JsonCpp conversion execution.'}),'METHOD.v1.json':J({'original_execution':0,'native_top_entries':0,'host_scene_fixtures':0,'host_semantic_models':0,'stored_expressions_evaluated':0,'code_mode':'Thumb2, explicit force-thumb; tables/pools in spans are data, not executed instructions.','image_path':IMAGE,'history':'No generated candidate overwrites/corrections. An exploratory python command failed because python alias is absent; retried using python3 before any candidate generation.','scope':'Three factory discrimination prefixes and two action construction branches. No whole scene schema, trigger/condition branch coverage, runner/sleep execution, timer units, target resolution, live provider or physical action conclusion.'})})
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args();out=build();out['OUTPUT_MANIFEST.v1.json']=J({'files':{n:{'bytes':len(b),'sha256':H(b)}for n,b in out.items()}})
 if a.check:
  for n,b in out.items():assert(D/n).read_bytes()==b,n
 else:
  assert not any((D/n).exists()for n in out),'refuse existing outputs';S=D/'first-candidate';assert not S.exists();copies={**out,'collect_factories_v1.py':Path(__file__).read_bytes()};idx=J({n:{'bytes':len(b),'sha256':H(b)}for n,b in copies.items()})
  for n,b in out.items():p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  for n,b in copies.items():p=S/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  (S/'SNAPSHOT.json').open('xb').write(idx)
 print(json.dumps({'check':a.check,'outputs':len(out),'spans':len(SPANS),'PIC_literals':len(PIC),'factory_tables':len(TABLES),'selected_branches':3,'direct_calls':len(CALLS),'byte_guards':len(GUARDS),'inputs':4,'original_execution':0}))
if __name__=='__main__':main()
