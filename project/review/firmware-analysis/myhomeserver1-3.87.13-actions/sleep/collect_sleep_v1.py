#!/usr/bin/env python3
"""Original static SLEEP construction, callable binding and libc request ABI."""
import argparse,hashlib,importlib.util,json,struct,subprocess,sys
from pathlib import Path
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent;P=D.parents[2];W=P.parents[2]
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
HELPER=P/'research/2026-10-31/image_vfs.py'
spec=importlib.util.spec_from_file_location('sleep_image_vfs',HELPER);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
BIN='/home/bticino/scheduling_manager/scheduling_manager';LIB='/lib/libc.so.6'
SHA='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26';LSHA='c8598ca6fd7a47a301fd0b09937f5ab3e270e53db22c7a35b196485c2772d5c6'
SPANS=[('initializer-got',BIN,0xa72c0,0xa7330),('initializer-sleep-convert',BIN,0xa75c8,0xa767a),('initializer-sleep-append',BIN,0xa767a,0xa7712),('sleep-constructor',BIN,0xb7590,0xb7758),('captured-function-manager',BIN,0xb72b0,0xb72d4),('sleep-callback',BIN,0xb72d4,0xb7590),('operational-delay-setter',BIN,0xcd988,0xcd990),('callable-installation',BIN,0xcd990,0xcda3c),('runner-move-prefix',BIN,0xb444c,0xb44e8),('libc-nanosleep32',LIB,0x860d4,0x86130)]
def build():
 v=mod.ImageVFS();raws={p:v.read_bytes(p)for p in [BIN,LIB]};assert H(raws[BIN])==SHA and H(raws[LIB])==LSHA
 maps={}
 for p,b in raws.items():
  ph=struct.unpack_from('<I',b,28)[0];es,n=struct.unpack_from('<HH',b,42);rows=[]
  for i in range(n):
   t,o,a,_,fs,ms,fl,al=struct.unpack_from('<8I',b,ph+i*es)
   if t==1:rows.append((a,o,fs,fl))
  maps[p]=rows
 def at(p,va,n):
  for a,o,s,f in maps[p]:
   if a<=va and va+n<=a+s:return raws[p][o+va-a:o+va-a+n]
  raise ValueError(('unmapped original range',p,hex(va),n))
 word=lambda a:struct.unpack('<I',at(BIN,a,4))[0]
 out={};sp=[]
 for name,p,a,z in SPANS:
  bb=at(p,a,z-a);sp.append({'name':name,'image_path':p,'start_va':hex(a),'end_exclusive':hex(z),'sha256':H(bb),'bytes':len(bb)})
  s=subprocess.check_output(['objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={z}',str(v.root/p.lstrip('/'))],text=True)
  out['spans/'+name+'.txt']=s.replace(str(W)+'/','').encode()
 pic=[]
 for name,add,pool,target in [('constructor-GOT',0xb75a4,0xb7734,0x1659a4),('initializer-GOT',0xa72f0,0xa7ef4,0x1659a4),('function-invoker',0xb7662,0xb7744,0xb72d5),('function-manager',0xb7668,0xb7748,0xb72b1)]:
  x=word(pool);assert(add+4+x)&0xffffffff==target;pic.append({'name':name,'add_pc_va':hex(add),'pool_va':hex(pool),'word':hex(x),'target':hex(target)})
 assert word(0xb7740)==word(0xa7f4c)==0x540 and word(0x1659a4+0x540)==0x164d5c
 vt=[word(a)for a in range(0x164d5c,0x164d7c,4)];assert vt==[0,0x1648a0,0xcd849,0xcd6f1,0xcd551,0xffffffcc,0x1648a0,0x24c9d]
 name=word(0x1648a4);assert name==0x1342ec and at(BIN,name,20).split(b'\0')[0]==b'17SleepActionRunner'
 rel=[]
 for target in [0x165ee4,0x164d60,0x164d64,0x164d68,0x164d6c,0x164d78,0x1648a4]:
  matches=[a for a in range(0x498c,0x100d4,8)if word(a)==target and word(a+4)==23];assert len(matches)==1
  rel.append({'slot_va':hex(target),'entry_va':hex(matches[0]),'type':'R_ARM_RELATIVE','value':hex(word(target))})
 guards=[(BIN,0xb75ce,'40f98f07'),(BIN,0xb7632,'10ee901b'),(BIN,0xb7640,'ab6a'),(BIN,0xb7642,'e365'),(BIN,0xb765e,'0393'),(BIN,0xcd988,'8160'),(BIN,0xb746e,'2b68'),(BIN,0xb7470,'7bb1'),(BIN,0xb7476,'cde90332'),(BIN,0xb7486,'2146'),(BIN,0xb7488,'2046'),(BIN,0xb748e,'0130'),(BIN,0xb7482,'042b'),(LIB,0x860d4,'d0e90032'),(LIB,0x860e0,'db17')]
 gw=[]
 for p,a,expected in guards:bb=at(p,a,len(bytes.fromhex(expected)));assert bb.hex()==expected,(p,hex(a),bb.hex());gw.append({'image_path':p,'va':hex(a),'file_bytes':expected})
 def bl(a):
  x,y=struct.unpack('<HH',at(BIN,a,4));assert x&0xf800==0xf000 and y&0xd000==0xd000;s=(x>>10)&1;i1=1-(((y>>13)&1)^s);i2=1-(((y>>11)&1)^s);n=(s<<24)|(i1<<23)|(i2<<22)|((x&1023)<<12)|((y&2047)<<1);return(a+4+n-((1<<25)if s else 0))&0xffffffff
 calls=[]
 for a,t in [(0xa7676,0xb7590),(0xa7684,0xb444c),(0xa7706,0xa7288),(0xb7652,0xcd988),(0xb7670,0xcd990)]:
  assert bl(a)==t;calls.append({'call_va':hex(a),'target':hex(t),'bytes':at(BIN,a,4).hex()})
 defs=subprocess.check_output(['readelf','-WsW',str(v.root/LIB.lstrip('/'))],text=True)
 imp=subprocess.check_output(['readelf','-WsW',str(v.root/BIN.lstrip('/'))],text=True)
 selected=lambda s:[l.strip()for l in s.splitlines()if 'nanosleep'in l or '__errno_location'in l]
 assert any('000860d5' in l and 'nanosleep@@GLIBC_2.4'in l for l in defs.splitlines())
 context=(D/'API_CONTEXT.json').read_bytes();json.loads(context)
 refs=P/'research/2026-10-31-factories/runner/REPORT.md';inputs=[{'path':str((v.root/p.lstrip('/')).relative_to(W)),'sha256':H(b),'bytes':len(b)}for p,b in raws.items()]
 for p in [HELPER,refs,D/'API_CONTEXT.json']:bb=p.read_bytes();inputs.append({'path':str(p.relative_to(W)),'sha256':H(bb),'bytes':len(bb)})
 out.update({'INPUTS.v1.json':J(inputs),'SOURCE_SPANS.v1.json':J(sp),'PIC_AND_VTABLE.v1.json':J({'PIC':pic,'GOT_slot':'0x165ee4','header':'0x164d5c','vtable_words':[hex(x)for x in vt],'RTTI_name':'17SleepActionRunner','relocations':rel}),'BYTE_GUARDS.v1.json':J(gw),'DIRECT_CALLS.v1.json':J(calls),'PROVIDERS.v1.json':J({'original_imports':selected(imp),'packaged_candidate_definitions':selected(defs),'libc_nanosleep32_entry':'0x860d4','request_read':'ldrd first32,second32; first ASR31 sign-extension to time64 temporary','remainder_copy':'on code4 with nonnull remainder, copied back to supplied output','limits':'Static packaged definitions and import version, not effective loader binding or provider/kernel execution.'}),'BINDING_LEDGER.v1.json':J({'JSON_action_offsets':{'32':'delay','36':'duration','40':'seconds'},'metadata_runtime_offsets':{'84':'raw delay','88':'raw duration','92':'raw seconds'},'operational_offsets':{'8':'delay copied by cd988','12':'zero from selected constructor and move-copy, no duration setter on selected path','16':'start callable capturing seconds','24':'start manager','28':'start invoker','32':'stop callable data remains initially empty','40':'stop manager initially0','44':'stop invoker initially0'},'same_object_chain':['selected initializer index10','b7590 temporary compiled object','b444c move prefix into96-byte heap object','derived vtable reinstall and metadata copy','runner+128 append'],'callback_capture_word':'unsigned source word read unchanged from captured function data; not runtime object+92 alias after copy','sleep_request':'if capturedword!=0, two32words[capturedword,0], req and rem same private stack address','retry':'only ret==-1 and errno==4; same request/remainder address reused','stop_scope':'Selected blocking callback loop contains no explicit shared cancellation flag read or conditional-variable wait. Common stop signaling is separate, not an observed interruption.','units':'seconds/nanoseconds under ordinary successful packaged libc/Linux nanosleep ABI; first32 signed-extension limits are distinct from JSON asUInt','original_execution':0,'semantic_host_cases':0}),'METHOD.v1.json':J({'original_instructions_executed':0,'target_process_SQL_threads_services_bus_network_physical_execution':0,'primitive_callbacks':0,'semantic_host_models':0,'method':'Original static Thumb2 source, fresh PT_LOAD mappings, bytes/PIC/relocs and versioned provider symbols; external API context is not target source.','limits':'No accepted scenes, timer/elapsed measurement, full provider closure, whole-program state/lifetime/cancellation/concurrency proof. All ordinary imported string/allocation/logging/thread/kernel calls remain unexecuted delegates.','development':'Pre-generation direct byte audit caught one manually transcribed VST1 guard byte (0f versus8f), exact draft and audit retained under development. Fixed before first collector invocation or output; source interpretation unchanged. Unknown provider/runtime state is not forced.'})})
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();out=build();out['OUTPUT_MANIFEST.v1.json']=J({'files':{n:{'bytes':len(b),'sha256':H(b)}for n,b in out.items()}})
 if args.check:
  for n,b in out.items():assert(D/n).read_bytes()==b,n
 else:
  assert not any((D/n).exists()for n in out),'refuse output overwrite';s=D/'first-candidate';assert not s.exists();copies={**out,Path(__file__).name:Path(__file__).read_bytes(),'API_CONTEXT.json':(D/'API_CONTEXT.json').read_bytes()}
  for n,b in out.items():p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  for n,b in copies.items():p=s/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  (s/'SNAPSHOT.json').open('xb').write(J({n:{'bytes':len(b),'sha256':H(b)}for n,b in copies.items()}))
 print(json.dumps({'check':args.check,'outputs':len(out),'source_spans':len(SPANS),'original_execution':0}))
if __name__=='__main__':main()
