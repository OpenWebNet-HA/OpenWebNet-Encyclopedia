#!/usr/bin/env python3
"""Static BN3L capture/adapters and selected local request-call edges only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());R=W/'work/myhomeserver1-firmware/3.87.13/research';V=R/'2026-10-31/image_vfs.py';IMG='/home/bticino/scheduling_manager/scheduling_manager'
H=lambda x:hashlib.sha256(x).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
s=importlib.util.spec_from_file_location('callable_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
SPANS=[('first-capture-source',0xcf19c,0xcf294),('second-capture-source',0xcf2f0,0xcf392),('first-manager-selector',0xcdbf8,0xcdc3c),('first-manager-copy',0xcdc68,0xcdcc4),('first-manager-string-arms',0xcdcc4,0xcdce6),('second-manager-selector',0xcdb00,0xcdb42),('second-manager-copy',0xcdb6a,0xcdbca),('first-invoker',0xd14a4,0xd14aa),('second-invoker',0xcf064,0xcf06a),('first-body-prefix-query',0xcf5c8,0xcf624),('first-record-prefix',0xcf6ba,0xcf7c4),('first-request-assembly',0xcf88c,0xcf93a),('second-record-prefix',0xcdd14,0xcddd4),('second-request-assembly',0xcde9e,0xcdf4c)]
GUARDS=[(0xd14a4,'0068'),(0xcf064,'0068'),(0xcf1f6,'3420'),(0xcf238,'43f8042b'),(0xcf248,'6860'),(0xcf286,'41f98f0a'),(0xcf28c,'c5e90b23'),(0xcf32a,'1820'),(0xcf344,'0360'),(0xcf370,'6e60'),(0xcdc16,'022a'),(0xcdc6a,'3420'),(0xcdcb8,'2560'),(0xcdcbe,'c5e90b23'),(0xcdb1c,'022a'),(0xcdb6c,'1820'),(0xcdba2,'2560'),(0xcf5d8,'8346'),(0xcf5f4,'036b'),(0xcf5f6,'002b'),(0xcf6ba,'dbe90164'),(0xcf7aa,'002b'),(0xcf7b4,'82f82430'),(0xcf900,'1946'),(0xcf922,'2146'),(0xcf92a,'3246'),(0xcdd2a,'0646'),(0xcdd34,'d0e90074'),(0xcdf34,'3946'),(0xcdf3e,'2246')]
CALLS=[(0xd14a6,0xcf5c8,'B.W adapter'),(0xcf066,0xcdd14,'B.W adapter'),(0xcf1ae,0xcdaec,'operational duration getter'),(0xcf290,0xcd990,'first callable storage'),(0xcf382,0xcda40,'second callable storage'),(0xcf61e,0x10f4a0,'opaque local query boundary'),(0xcf7c0,0xd20c0,'opaque descriptor request'),(0xcf904,0xd163c,'opaque params conversion'),(0xcf930,0x5dda0,'opaque local output request'),(0xcddd0,0xd20c0,'opaque descriptor request'),(0xcdf16,0xd163c,'opaque params conversion'),(0xcdf42,0x5dda0,'opaque local output request')]
KEYS=[(0xd01bc,0xcf8a8,0x115e04,'jsonrpc'),(0xd01c0,0xcf8ca,0x115e0c,'method'),(0xd01c4,0xcf8ea,0x116adc,'id'),(0xd01c8,0xcf90e,0x116144,'params'),(0xce898,0xcdeba,0x115e04,'jsonrpc'),(0xce89c,0xcdedc,0x115e0c,'method'),(0xce8a0,0xcdefc,0x116adc,'id'),(0xce8a4,0xcdf20,0x116144,'params')]
def build():
 v=m.ImageVFS();b=v.read_bytes(IMG);assert H(b)=='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
 assert b[:7]==b'\x7fELF\x01\x01\x01' and struct.unpack_from('<H',b,18)[0]==40
 ph=struct.unpack_from('<I',b,28)[0];es,n=struct.unpack_from('<HH',b,42);L=[struct.unpack_from('<8I',b,ph+i*es)for i in range(n)]
 def off(a,n=1):return next(o+a-va for t,o,va,_,fs,*_ in L if t==1 and va<=a and a+n<=va+fs)
 def raw(a,n):o=off(a,n);return b[o:o+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 hp=v.root/v.resolve(IMG).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');out={};spans=[]
 for name,a,e in SPANS:
  z=subprocess.check_output(['objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),IMG)
  assert 'out of bounds' not in z
  out['spans/'+name+'.txt']=z.encode();spans.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'file_offset':hex(off(a,e-a)),'sha256':H(raw(a,e-a))})
 for a,z in GUARDS:assert raw(a,len(bytes.fromhex(z))).hex()==z,hex(a)
 calls=[]
 for pc,target,kind in CALLS:
  x,y=struct.unpack('<HH',raw(pc,4));assert x&0xf800==0xf000 and y&0xd000 in(0x9000,0xd000)
  s=x>>10&1;i=1-((y>>13&1)^s);j=1-((y>>11&1)^s);d=s<<24|i<<23|j<<22|(x&1023)<<12|(y&2047)<<1;actual=(pc+4+d-((1<<25)if s else 0))&0xffffffff;assert actual==target,hex(pc)
  calls.append({'VA':hex(pc),'bytes':raw(pc,4).hex(),'target':hex(target),'kind':kind})
 keys=[]
 for pool,pc,target,key in KEYS:
  assert(u(pool)+pc+4)&0xffffffff==target
  assert raw(target,len(key)+1)==key.encode()+b'\0'
  keys.append({'pool_VA':hex(pool),'pool_word':hex(u(pool)),'ADD_PC_VA':hex(pc),'PC_value':hex(pc+4),'target':hex(target),'literal':key,'bytes':raw(target,len(key)+1).hex()})
 pointers=[]
 for pool,pc,target in [(0xcf59c,0xcf26e,0xd14a5),(0xcf5a0,0xcf27e,0xcdbf9),(0xcf5a8,0xcf372,0xcf065),(0xcf5ac,0xcf376,0xcdb01)]:
  assert(u(pool)+pc+4)&0xffffffff==target;pointers.append({'pool_VA':hex(pool),'word':hex(u(pool)),'ADD_PC_VA':hex(pc),'Thumb_target':hex(target)})
 bases=[]
 for pool,pc in[(0xd0194,0xcf5da),(0xce884,0xcdd28)]:
  base=(u(pool)+pc+4)&0xffffffff;assert base==0x1659a4;bases.append({'pool_VA':hex(pool),'word':hex(u(pool)),'ADD_PC_VA':hex(pc),'base':hex(base)})
 rel=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);rr=next(x.strip()for x in rel.splitlines()if x.startswith('001666a4 '));assert'R_ARM_RELATIVE'in rr and u(0x1666a4)==0x16711c
 assert u(0xd01cc)==u(0xce8a8)==0xd00 and 0x1659a4+0xd00==0x1666a4
 imports=[]
 for slot,name in[(0x165a64,'_ZN4Json5ValueixEPKc'),(0x165c68,'_ZN4Json5ValueaSEOS0_'),(0x165d54,'_ZN4Json5ValueC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE')]:
  z=next(x.strip()for x in rel.splitlines()if x.startswith(f'{slot:08x} '));assert'R_ARM_JUMP_SLOT'in z and z.split()[-1]==name;imports.append(z)
 pins={IMG:{'sha256':H(b),'bytes':len(b)}}
 for p,role in [(V,'image_accessor'),(R/'2026-10-31-cancellation/action-lifecycle/REPORT.md','inherited_duration_binding'),(R/'2026-10-31-lifetime/schema-activation/REPORT.md','inherited_class_activation'),(R/'2026-11-01-serialization/serializer/REPORT.md','inherited_raw_serializer'),(R/'2026-11-01-double-isolation/harness/RESULTS.json','unchanged_native_ledger'),(W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0199-myhomeserver1-home-automation-server.md','current_curated_role')]:
  z=p.read_bytes();pins[role]={'path':str(p.relative_to(W)),'sha256':H(z),'bytes':len(z)}
 out['ORIGINAL_SOURCE.json']=J({'image':IMG,'ELF_PT_LOAD':[{'offset':hex(o),'VA':hex(va),'file_bytes':fs,'memory_bytes':ms,'flags':fl}for t,o,va,pa,fs,ms,fl,al in L if t==1],'code_spans':spans,'instruction_guards':[{'VA':hex(a),'bytes':z}for a,z in GUARDS],'direct_calls':calls,'literal_pool_data':{'keys':keys,'callable_pointers':pointers,'GOT_bases':bases,'receiver':{'offset_pools':['0xd01cc','0xce8a8'],'offset':'0xd00','slot':'0x1666a4','linked_addend':'0x16711c','original_relocation':rr}},'selected_JsonCpp_import_declarations':imports,'source_scope':'Only selected code spans and data are emitted; descriptor/query/converter/output delegate bodies are not audited by this packet. Symbol declarations do not prove live binding.'})
 out['CALLABLE_HANDOFF.json']=J({'object_namespaces':{'compiled_action':'116 bytes, first callable data16/manager24/invoker28; second data32/manager40/invoker44 (inherited)','first_heap_capture':{'bytes':52,'word0':'compiled112','string4':'copied ID; length8/inline12','words28_44':'compiled92/96/100/104/108','word48':'operational duration getter result'},'second_heap_capture':{'bytes':24,'string0':'copied ID; length4/inline8'}},'adapters':[{'entry':'0xd14a4','input':'R0 points callable storage','receiver':'word0 of storage','tail':'0xcf5c8'},{'entry':'0xcf064','input':'R0 points callable storage','receiver':'word0 of storage','tail':'0xcdd14'}],'manager_copy':'operation2 copies into separate52/24-byte captures under normal allocator/string returns; does not prove running lifetime','selected_requests':[{'call':'0xcf930','opaque_callee':'0x5dda0','R0':'relative GOT1666a4 linked addend16711c','R1':'SP432 method string','R2':'SP72 JsonCpp object','members':{'jsonrpc':'string SP408','method':'string SP432','id':'string SP456','params':'opaque d163c result from local record SP480'}},{'call':'0xcdf42','opaque_callee':'0x5dda0','R0':'same relative GOT1666a4 linked addend16711c','R1':'SP552 method string','R2':'SP56 JsonCpp object','members':{'jsonrpc':'string SP528','method':'string SP552','id':'string SP576','params':'opaque d163c result from local record SP600'}}],'premises':['selected blocks actually reached under original preceding guards','normal valid objects/storage/ABI and allocation/string/JsonCpp/helper returns','candidate import and relative data binding','capture/receiver alive and no incompatible mutation'],'unproved':['actual descriptor strings and full params','whole callable path/return or invocation order','natural configured scene','send result/downstream/accepted protocol/physical operation','snapshot restoration/cache freshness','whole concurrency/ownership/unwind'],'execution':{'new_original':0,'semantic_models':0,'input_fixtures':0,'unchanged_prior':{'corpora':1,'entries':8,'original_visits':340,'C_primitives':0,'redirects':12,'EXIT':8,'stops':0,'hooks':360,'data_setup_relocations':4}}})
 out['INPUTS.json']=J(pins)
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'sha256':H(z),'bytes':len(z)}for n,z in out.items()},'counts':{'spans':len(SPANS),'guards':len(GUARDS),'direct_calls':len(calls),'key_PIC':len(keys),'callable_PIC':len(pointers),'GOT_base_PIC':len(bases),'receiver_relative_relocations':1,'import_declarations':len(imports),'inputs':len(pins),'new_original_execution':0}})
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');ck=ap.parse_args().check;out=build();C=D/'first-candidate';cp={**out,'REPORT.md':(D/'REPORT.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({n:{'sha256':H(z),'bytes':len(z)}for n,z in cp.items()})
 if ck:
  for n,z in out.items():assert(D/n).read_bytes()==z,n
  assert(C/'INDEX.json').read_bytes()==ix
  for n,z in cp.items():assert(C/n).read_bytes()==z,n
 else:
  assert not C.exists();assert all(not(D/n).exists()for n in out)
  for n,z in out.items():p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  C.mkdir()
  for n,z in cp.items():p=C/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  (C/'INDEX.json').open('xb').write(ix)
 print(json.dumps({'check':ck,'outputs':len(out),'spans':len(SPANS),'guards':len(GUARDS),'direct_calls':len(CALLS),'new_original_execution':0}))
if __name__=='__main__':main()
