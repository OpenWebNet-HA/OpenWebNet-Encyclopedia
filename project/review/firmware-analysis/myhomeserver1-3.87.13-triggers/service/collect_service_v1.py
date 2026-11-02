#!/usr/bin/env python3
"""Selected original TIME service/callback/condition-worker joins; static only."""
import argparse,hashlib,importlib.util,json,struct,subprocess,sys
from pathlib import Path
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent;P=D.parents[2];W=P.parents[2]
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
HELPER=P/'research/2026-10-31/image_vfs.py'
spec=importlib.util.spec_from_file_location('service_vfs',HELPER);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
BIN='/home/bticino/scheduling_manager/scheduling_manager';LIB='/usr/lib/libstdc++.so.6.0.29'
SHA='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26';LSHA='02d98c9486577d7be0b3fb71b5f0c0b6c090b72554c83640cb525cb3a3c1549a'
SPANS=[('weekday-initializers',BIN,0x146b0,0x1488c),('weekday-tree-builder',BIN,0xb891c,0xb8a08),('time-fire',BIN,0xb8a08,0xb8ad4),('deadline-accessors',BIN,0xb8bcc,0xb8be0),('deadline-preparation',BIN,0xb8be0,0xb8e7c),('service-constructor',BIN,0xb94f0,0xb9638),('service-register',BIN,0xb9814,0xb98a0),('service-worker',BIN,0xbb5ec,0xbbd8c),('scene-start-wrapper',BIN,0xa60a8,0xa60b0),('condition-worker',BIN,0xa6d18,0xa7098),('time-registration-handoff',BIN,0xa8108,0xa8338),('callback-copy-helper',BIN,0xb43d8,0xb444c),('system-clock-provider',LIB,0x959a0,0x959cc)]
def build():
 v=mod.ImageVFS();raws={p:v.read_bytes(p)for p in [BIN,LIB]};assert H(raws[BIN])==SHA and H(raws[LIB])==LSHA
 loads={}
 for p,b in raws.items():
  ph=struct.unpack_from('<I',b,28)[0];es,n=struct.unpack_from('<HH',b,42);loads[p]=[]
  for i in range(n):
   t,o,a,_,fs,ms,fl,al=struct.unpack_from('<8I',b,ph+i*es)
   if t==1:loads[p].append((a,o,fs,fl))
 def at(p,a,n):
  for va,off,size,fl in loads[p]:
   if va<=a and a+n<=va+size:return raws[p][off+a-va:off+a-va+n]
  raise ValueError(('unmapped original range',p,hex(a),n))
 u=lambda a:struct.unpack('<I',at(BIN,a,4))[0]
 out={};sp=[]
 for name,p,a,z in SPANS:
  bb=at(p,a,z-a);sp.append({'name':name,'image_path':p,'start_va':hex(a),'end_exclusive':hex(z),'bytes':len(bb),'sha256':H(bb)})
  s=subprocess.check_output(['objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={z}',str(v.root/p.lstrip('/'))],text=True)
  out['spans/'+name+'.txt']=s.replace(str(W)+'/','').encode()
 pic=[]
 for name,pool,add,target in [('condition-weekday-map',0x14788,0x146f2,0x1674f8),('trigger-weekday-map',0x14878,0x147e2,0x167510),('trigger-map-consumer',0xb8ac8,0xb8a52,0x167510),('time-format',0xb8e70,0xb8cfe,0x135818),('time-start-invoker',0xa8af0,0xa8120,0xa60a9),('time-function-manager',0xa8af4,0xa8124,0xa56c1),('service-thread-vtable',0xb9630,0xb956c,0x161e8c)]:
  x=u(pool);assert(x+add+4)&0xffffffff==target;pic.append({'name':name,'pool':hex(pool),'word':hex(x),'add_pc':hex(add),'target':hex(target)})
 assert at(BIN,0x135818,6)==b'%H:%M\0'
 pairs=[(0,0),(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)]
 for base in [0x14750,0x14840]:assert struct.unpack('<12I',at(BIN,base,48))==tuple(x for row in pairs[1:]for x in row)
 vals=struct.unpack('<72I',at(BIN,0x15fb1c,72*4));assert vals[14]==0x146b1 and vals[15]==0x147a1
 rel=[]
 for target,want in [(0x161e64,0xb8a09),(0x161e68,0xb8be1),(0x161e9c,0xbbd85),(0x164dfc,0x135820),(0x164e1c,0x135834)]:
  assert u(target)==want;rows=[a for a in range(0x498c,0x100d4,8)if u(a)==target and u(a+4)==23];assert len(rows)==1
  rel.append({'slot':hex(target),'entry':hex(rows[0]),'type':'R_ARM_RELATIVE','value':hex(want)})
 assert at(BIN,0x135820,20).split(b'\0')[0]==b'17TimeTriggerRunner'
 assert 'TimeTriggersService'in at(BIN,0x135834,110).split(b'\0')[0].decode()
 ex=[]
 for a in range(0x14bfc0,0x14f8f8,8):
  x=u(a)&0x7fffffff;x-=(1<<31)if x&(1<<30)else 0;ex.append(((a+x)&0xfffffffe,a))
 bounds=[]
 for pc in [0xb8a08,0xb8be0,0xb94f0,0xb9814,0xbb5ec,0xa6d18]:
  idx=next(a for x,a in ex if x==pc);end=next(x for x,a in ex if x>pc);bounds.append({'start':hex(pc),'next_exidx_start':hex(end),'index':hex(idx)})
 declarations={}
 for p in [BIN,LIB]:
  sy=subprocess.check_output(['readelf','-WsW',str(v.root/p.lstrip('/'))],text=True)
  declarations[p]=[l.strip()for l in sy.splitlines()if any(x in l for x in ['system_clock3now','localtime','mktime','pthread_cond_timedwait'])]
 inputs=[{'path':str((v.root/p.lstrip('/')).relative_to(W)),'bytes':len(b),'sha256':H(b)}for p,b in raws.items()]
 for p in [HELPER,D/'API_CONTEXT.json',P/'research/2026-10-31-factories/runner/REPORT.md']:
  b=p.read_bytes();inputs.append({'path':str(p.relative_to(W)),'bytes':len(b),'sha256':H(b)})
 ledger={'register':'b9814 normal capacity branch copies same two-word handle to service end, increments ownership word, advances8, unlocks+20 and notifiesCV+48; reallocationbbd8c remainsdelegate','constructor':'b94f0 vectorzero, runningbyte12=1, CV48, threadholder16; nonzero suppliedflag requests state thread; state vtable161e94 slot8→bbd84→bb5ec','deadline':'b8be0 requests time/localtime and %H:%M streamparse; selected stores replace current tmhour/minute andzero seconds; mktime signedseconds*1e9; ifearlier than systemclock add86400000000000 once; field88/92','due_entry':'Selected live first serviceentry; queueordering/rebuild helpers remain unclosed','window':'After wait firstclock N1>=D; selectedsecond N2 has abs(N2-D)<=30000000000 (bounded nonoverflow arithmetic) before virtualslot0 callbb906','rearm':'After normal virtualslot0 return reloadsameobjectdeadline andadd86400000000000 via b8bd8; not a measurednextcalendarwalltime/DST policy','fire':'b8a08 gates ownenabled48, weekdaymap anddaysmask84, callablemanager12; invokesinvoker16 withdata4; installedcapture reachesa60a8→a5db0','condition_worker':'a6d18 conditionpointerrange116/120 andvptr+8; firstzero falsepath clears scene145/144 at a6e6a/a6e76 thenreturns. Allnonzero/empty normalrange reaches a6f8c→a6734','limits':'No configuredscenes/APIobjects/actualthread/timer/clock, fullparser/queue/ownership/unwind/concurrency/catchup/DST/runtime/physical guarantee.'}
 out.update({'INPUTS.v1.json':J(inputs),'SOURCE_SPANS.v1.json':J(sp),'PIC_RELOC_EXIDX.v1.json':J({'PIC':pic,'relative_slots':rel,'boundaries':bounds,'init_array_entries':[{'index':14,'pointer':'0x146b1'},{'index':15,'pointer':'0x147a1'}]}),'WEEKDAY_MAPS.v1.json':J({'pairs':pairs,'initializer14_map':'0x1674f8','initializer15_map':'0x167510','sixpair_literals':['0x14750','0x14840'],'firstpair':'Original zero STRD into stack24; sixdoubleword poolcopies follow; allocation/treeinsertion delegated normalreturns','node_pair_store':'b8976 stores original key/value at new24byte node16/20','conditional_character_order':'Under ordinary tm_wday0Sunday and rawbits6..0, sevencharacter days is Monday through Sunday','limits':'No actualinitialization, targetheader/live timezone/ABI or tree mutation/concurrency proof.'}),'SERVICE_LEDGER.v1.json':J(ledger),'PROVIDERS.v1.json':J(declarations),'METHOD.v1.json':J({'original_target_SQL_parser_threads_timers_network_bus_physical_execution':0,'semantic_host_cases':0,'method':'Original static Thumb2/PT_LOAD/data/PIC/relocs/exidx/init-array/provider definitions; externalAPIcontext separated. No vendor execution or imported-success stubs.','development':'Exploratory inline exidx locator Python else-spacing SyntaxError corrected before collector/report/output generation. First apply_patch spelling typo rejected whole patch before files were created; corrected before source generation. No candidate changed. PC/pool locator candidates only promoted where original LDR/ADD source agrees.','scope':'Selected normal capacity/live-handle/provider branches; fullqueue ordering and standard-library tree/stream/thread/kernel execution and Deviceapproval remain unclosed.'})})
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args();out=build();out['OUTPUT_MANIFEST.v1.json']=J({'files':{n:{'bytes':len(b),'sha256':H(b)}for n,b in out.items()}})
 if args.check:
  for n,b in out.items():assert(D/n).read_bytes()==b,n
 else:
  assert not any((D/n).exists()for n in out),'refuse overwrite';s=D/'first-candidate';assert not s.exists();copies={**out,Path(__file__).name:Path(__file__).read_bytes(),'API_CONTEXT.json':(D/'API_CONTEXT.json').read_bytes()}
  for n,b in out.items():p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  for n,b in copies.items():p=s/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  (s/'SNAPSHOT.json').open('xb').write(J({n:{'bytes':len(b),'sha256':H(b)}for n,b in copies.items()}))
 print(json.dumps({'check':args.check,'outputs':len(out),'spans':len(SPANS),'original_execution':0}))
if __name__=='__main__':main()
