#!/usr/bin/env python3
"""Static compiled-action contract; explicit host-only decision/arithmetic cases.
Never executes vendor helpers, timer/thread APIs or SQL. First writes exclusive.
"""
import sys
sys.dont_write_bytecode=True
import argparse,pathlib,struct,json,hashlib,subprocess,re,importlib.util,os
O=pathlib.Path(__file__).resolve().parent;W=next(x for x in O.parents if(x/'sources').is_dir());R=W/'work/myhomeserver1-firmware/3.87.13/research/2026-10-31'
spec=importlib.util.spec_from_file_location('original_vfs',R/'image_vfs.py');vmod=importlib.util.module_from_spec(spec);spec.loader.exec_module(vmod)
H=lambda z:hashlib.sha256(z).hexdigest();J=lambda z:(json.dumps(z,indent=2,sort_keys=True,ensure_ascii=True)+'\n').encode()
S='/home/bticino/scheduling_manager/scheduling_manager';L='/usr/lib/libstdc++.so.6.0.29'
def build():
 v=vmod.ImageVFS();out={};pins={};blobs={};maps={};env=dict(os.environ,DEBUGINFOD_URLS='')
 for name in [S,L]:
  bb=v.read_bytes(name);blobs[name]=bb;pins[name]={'bytes':len(bb),'sha256':H(bb),'resolved_image_path':v.resolve(name)}
  ph=struct.unpack_from('<I',bb,28)[0];size,n=struct.unpack_from('<HH',bb,42);maps[name]=[struct.unpack_from('<8I',bb,ph+i*size)for i in range(n)]
 assert H(blobs[S])=='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
 for file,name in [(R/'image_vfs.py','image_accessor'),(R.parents[1]/'analysis/normal-regular-files.json','regular_metadata'),(R.parents[1]/'analysis/normal-symlinks.json','symlink_metadata')]:bb=file.read_bytes();pins[name]={'bytes':len(bb),'sha256':H(bb)}
 def off(a,n=1,path=S):return next(o+a-va for t,o,va,_,fs,*_ in maps[path]if t==1 and va<=a and a+n<=va+fs)
 def raw(a,n,path=S):return blobs[path][off(a,n,path):off(a,n,path)+n]
 def word(a,path=S):return struct.unpack('<I',raw(a,4,path))[0]
 def txt(a):
  z=off(a);end=blobs[S].index(0,z);assert end-z<512;return blobs[S][z:end].decode()
 spans=[(S,'execute-entry-inline-branch',0xcd848,0xcd896),(S,'execute-delay-thread-request',0xcd896,0xcd8e0),(S,'execute-duration-thread-request',0xcd8e0,0xcd936),(S,'delay-worker-deadline',0xcd5c4,0xcd620),(S,'delay-worker-wait-and-callback',0xcd620,0xcd6ca),(S,'duration-worker-deadline',0xcd720,0xcd77c),(S,'duration-worker-wait-and-callback',0xcd77c,0xcd826),(S,'shared-stop-notify',0xcd6f0,0xcd71c),(S,'primary-third-slot-noop',0xcd550,0xcd554),(S,'completion-and-first-wait-accessors',0xcd97c,0xcd98c),(S,'second-wait-accessors',0xcdaec,0xcdaf4),(S,'shared-domain-initializer',0x15474,0x154a8),(S,'base-operational-move',0xb444c,0xb44de),(S,'sleep-operational-zero-prefix',0xb75a6,0xb75d2),(S,'sleep-metadata-and-first-wait-store',0xb7626,0xb7656),(S,'selected-completion-caller',0xa6906,0xa6914),(L,'candidate-steady-clock-now',0x959cc,0x959f6)]
 provenance=[]
 for path,name,a,z in spans:
  host=v.root/v.resolve(path).lstrip('/');s=subprocess.run(['objdump','-d','--dwarf=no-follow-links','-M','force-thumb',f'--start-address={a}',f'--stop-address={z}',str(host)],capture_output=True,text=True,check=True,env=env).stdout.replace(str(host),path);s=re.sub(r' <([^>]+)>',lambda q:q[0]if'@plt'in q[1]else'',s);out['spans/'+name+'.txt']=s.encode();provenance.append({'path':path,'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(z),'file_offset':hex(off(a,z-a,path)),'sha256':H(raw(a,z-a,path))})
 guards=[(0xcd862,[0x7105]),(0xcd864,[0xb9be]),(0xcd872,[0x68e3]),(0xcd87a,[0x7123]),(0xcd5e8,[0x689f]),(0xcd744,[0x68df]),(0xcd606,[0xfba7,0x3603]),(0xcd60a,[0xfb02,0x6607]),(0xcd638,[0x2201]),(0xcd642,[0xf743,0xeb52]),(0xcd676,[0x711a]),(0xcd706,[0xf884,0x3048]),(0xcd550,[0x4770]),(0xcd97c,[0x7900]),(0xcd988,[0x6081]),(0xcdaf0,[0x60c1]),(0x1548e,[0xf884,0x3048]),(0xb7632,[0xee10,0x1b90]),(0xb763c,[0xf943,0x078f]),(0xb75ce,[0xf940,0x078f])]
 for a,half in guards:assert raw(a,2*len(half))==struct.pack('<'+'H'*len(half),*half),hex(a)
 pools=[]
 def pic(pool,pc,want):
  a=(word(pool)+pc+4)&0xffffffff;assert a==want;pools.append({'pool_VA':hex(pool),'word':hex(word(pool)),'ADD_PC_VA':hex(pc),'target_VA':hex(a)});return a
 for pool,pc in [(0x154a8,0x1547a),(0xcd6e0,0xcd5e0),(0xcd6ec,0xcd6b0),(0xcd71c,0xcd6f4),(0xcd838,0xcd73c),(0xcd844,0xcd80c)]:pic(pool,pc,0x1677b8)
 for pool,pc in [(0xcd974,0xcd8b0),(0xcd978,0xcd8fa)]:pic(pool,pc,0x162100)
 assert struct.unpack('<Q',raw(0xcd6d0,8))[0]==1000000000 and struct.unpack('<Q',raw(0xcd828,8))[0]==1000000000
 # Reconstruct exactly the UMULL/MLA source constant, not units from field names.
 lo=(0xf847<<16)|0x5800;hi=13;factor=(hi<<32)|lo;assert factor==60000000000
 vtables=[]
 for name,header,expected in [('ActionRunner',0x162128,'12ActionRunner'),('SleepActionRunner',0x164d5c,'17SleepActionRunner')]:
  rt=word(header+4);np=word(rt+4);assert txt(np)==expected;methods=[word(header+8+4*i)for i in range(3)];assert methods==[0xcd849,0xcd6f1,0xcd551];vtables.append({'name':name,'header_VA':hex(header),'address_point':hex(header+8),'header_file_offset':hex(off(header,20)),'RTTI_VA':hex(rt),'RTTI_name_VA':hex(np),'RTTI_name':txt(np),'primary_methods_Thumb':[hex(x)for x in methods],'raw_header_sha256':H(raw(header,20))})
 threadslots=[]
 for ap,worker in [(0x162108,0xcd5c5),(0x16211c,0xcd721)]:
  assert word(ap+8)==worker;threadslots.append({'address_point':hex(ap),'worker_slot':hex(ap+8),'stored_Thumb_pointer':hex(worker)})
 host=v.root/v.resolve(S).lstrip('/');rel=subprocess.run(['readelf','-rW',str(host)],capture_output=True,text=True,check=True).stdout;relocated=[]
 for a in [0x162130,0x162134,0x162138,0x164d64,0x164d68,0x164d6c,0x162110,0x162124]:
  line=next(x for x in rel.splitlines()if x.startswith(f'{a:08x} '));assert 'R_ARM_RELATIVE'in line;relocated.append(line.strip())
 bb=blobs[S];sh=struct.unpack_from('<I',bb,32)[0];ss,n,si=struct.unpack_from('<HHH',bb,46);sects=[struct.unpack_from('<10I',bb,sh+i*ss)for i in range(n)];names=bb[sects[si][4]:sects[si][4]+sects[si][5]];ar=next(x for x in sects if names[x[0]:].split(b'\0',1)[0]==b'.init_array');arr=struct.unpack_from('<'+'I'*(ar[5]//4),bb,ar[4]);assert 0x15475 in arr
 out['ORIGINAL_SOURCE.json']=J({'spans':provenance,'Thumb_halfword_assertions':[{'VA':hex(a),'halfwords':[hex(x)for x in half],'file_bytes':struct.pack('<'+'H'*len(half),*half).hex()}for a,half in guards],'PIC_joins':pools,'primary_vtables':vtables,'thread_worker_slots':threadslots,'selected_relocations':relocated,'initializer':{'init_array_VA':hex(ar[3]),'stored_Thumb_pointer':'0x15475','index':arr.index(0x15475)},'wait_factor':{'low_word':hex(lo),'high_word':hi,'unsigned64_factor':factor,'divisor_pools':['0xcd6d0','0xcd828'],'divisor_uint64':1000000000}})
 meta={}
 for path in [S,L]:
  host=v.root/v.resolve(path).lstrip('/');dyn=subprocess.run(['readelf','-dW',str(host)],capture_output=True,text=True,check=True,env=env).stdout;sy=subprocess.run(['readelf','--dyn-syms','-W',str(host)],capture_output=True,text=True,check=True,env=env).stdout;meta[path]={'DT_NEEDED':re.findall(r'\(NEEDED\).*?\[(.*?)\]',dyn),'selected_symbols':[x.strip()for x in sy.splitlines()if any(k in x for k in ['steady_clock3now','clock_gettime','pthread_cond_clockwait','pthread_mutex_','condition_variable','_M_start_thread','thread6detach'])]}
 out['PROVIDER_DECLARATIONS.json']=J({'objects':meta,'boundary':'Direct declarations/candidate definition only; no effective symbol resolution, target syscall, provider return or target clock observed.'})
 out['FIELD_AND_BRANCH_LEDGER.json']=J({'common_primary_methods':{'execute':'0xcd848','stop':'0xcd6f0','third_method':'0xcd550 immediate BXLR; not completion getter'},'per_action':{'completion_byte':4,'first_operational_wait_word':8,'second_operational_wait_word':12,'start_callable_data':16,'start_callable_manager':24,'start_callable_invoker':28,'stop_callable_data':32,'stop_callable_manager':40,'stop_callable_invoker':44,'thread_holder':48},'shared_domain':{'base':'0x1677b8','condition_variable_request':0,'mutex_base':48,'stop_byte':72,'initializer_zero_store':'0x1548e','stop_set_store':'0xcd706','scope':'Same exact PC-derived global across selected common methods, not a per-action stop byte. No exhaustive indirect-alias/reset absence claim.'},'execute':{'entry_resets_completion_to':0,'first_word_zero':['call start callable inline','if secondword0 set completion1','else request duration worker thread; completion remains0 until worker normal callback return'],'first_word_nonzero':['request delay worker thread','local execute does not request duration worker on this branch'],'local_normal_return':1,'not_checked':['shared stop flag on inline path','already active/completed guard','successful thread run or delivery']},'wait_workers':{'first':'0xcd5c4 loads action8, calls start callable after selected deadline','second':'0xcd720 loads action12, calls stop callable after selected deadline','shared_wait_flow':['lock global mutex; lock nonzero requests system_error throw','steady_clock now + unsigned32word*60000000000 modulo2^64','if shared flag nonzero unlock/return without callback/completion write','divide signed64 deadline by1e9; pass low32 quotient/remainder pair to clockwait clockID1','ignore clockwait return; refresh clock and compare signed deadline','if not reached and flag0 repeat; flag1 unlock/return','when reached unlock; if savedflag0 invoke phase callback then set action completion1'],'callback_scope':'Opaque installed action-specific callable, no inspection or synthetic successful callback here. Flag changed while inside callable is not rechecked before subsequent completion1 store.'},'stop':{'receiver_used':False,'effect':['lock shared mutex','set sharedbyte1','notify_all shared condition variable','unlock'],'does_not_locally':['invoke action-specific stop callable','set per-action completion1','reset shared stopbyte']},'selected_sleep_metadata_distinction':{'operational8_12_initial_zero':True,'parsed32_36_copied_metadata84_88':True,'parsed_delay_to_operational8':'sourceb7632→b7652→cd988','JSON_duration_to_operational12':'not established; metadata88 must not be substituted for operational12','normalbasecopy':'b444c copies actual operational8/12 independently of later JSON metadata'},'completion_caller':{'accessor':'0xcd97c reads action byte4','selected_direct_call':'0xa6908 tests its return','boundary':'Caller polling source, not successful eventual completion or elapsed guarantee'},'unclosed':['all setters/later global resets via other forms','natural runtime activation and live stop state','full callables/error/unwind/shared ownership','API clock/provider/binding and time structures beyond source arguments','all derived action applicability and complete cancellation/concurrency'], 'original_execution':0})
 # Host decision cases describe preselected source branches only, not timing/runtime simulation.
 execution=[]
 for d,u,f in [(0,0,0),(0,1,0),(1,0,0),(1,1,0),(0,0,1),(1,0,1)]:
  execution.append({'synthetic_fields':{'word8':d,'word12':u,'shared_stopbyte':f},'execute_path':'request-delay-worker'if d else('inline-start-then-request-duration-worker'if u else'inline-start-then-completion1'),'source_flag_checked_by_execute':False,'completion_written_inline':bool(not d and not u),'model_scope':'Branch selection after ordinary delegate returns; no thread/callback executed.'})
 workers=[]
 for initial,past,after in [(1,False,1),(0,False,0),(0,False,1),(0,True,0),(0,True,1)]:workers.append({'synthetic_shared_flag_initial':initial,'synthetic_after_wait_now_at_or_past_deadline':past,'synthetic_shared_flag_after_wait':after,'selected_outcome':'unlock-no-callback-no-completion-write'if initial or after else('unlock-callback-then-completion1'if past else'repeat-wait'),'boundary':'No OS wait/notify order, natural callback or actual clock is modeled.'})
 arithmetic=[]
 for value in [0,1,2,0xffffffff]:
  product=(value*factor)&((1<<64)-1);deadline=(1000+product)&((1<<64)-1);signed=deadline if deadline<(1<<63)else deadline-(1<<64);q=(abs(signed)//1000000000)*(1 if signed>=0 else-1);rem=signed-q*1000000000
  arithmetic.append({'synthetic_unsigned_word':value,'synthetic_now':1000,'product_mod64':product,'deadline_mod64':deadline,'signed_deadline':signed,'quotient_trunc_toward0':q,'remainder':rem,'passed_timespec_words':[q&0xffffffff,rem&0xffffffff],'scope':'Pure integer instruction-arithmetic illustration; maxword is not claimed admitted input, valid timer or a defect/hardware occurrence.'})
 out['HOST_MODELS.json']=J({'execute_cases':execution,'wait_guard_cases':workers,'arithmetic_cases':arithmetic,'original_execution':0,'target_API_calls':0,'unit_boundary':'Conditional ordinary successful clock_gettime seconds/nanoseconds API + candidate steady_clock conversion gives ns ticks; factor60000000000 is then60seconds per operationalword unit, not measured elapsed or universalJSON duration.'})
 out['INPUTS.json']=J(pins);out['METHOD.json']=J({'method':'Static image bytes/PT_LOAD/Thumb2/PIC/relocs/RTTI/init_array; readelf direct declarations; finite host branch/integer cases only','original_execution':0,'vendor_process':0,'target_API_or_network':0,'SQL_JSON_execution':0,'scope':'Shared ActionRunner methods only. Derived SLEEP/SCENARIO callbacks remain opaque, except narrow Sleep metadata-vs-operational-store corroboration. No transport/auth/session/framing bodies.'})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(pathlib.Path(__file__).read_bytes()),'report_sha256':H((O/'REPORT.md').read_bytes()),'outputs':{name:{'bytes':len(bb),'sha256':H(bb)}for name,bb in out.items()},'counts':{'spans':len(spans),'halfword_assertions':len(guards),'PIC':len(pools),'primary_vtables':2,'thread_worker_slots':2,'relocations':len(relocated),'inputs':len(pins),'host_execute_cases':len(execution),'host_wait_cases':len(workers),'host_arithmetic_cases':len(arithmetic),'original_execution':0}})
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');check=ap.parse_args().check;out=build()
 if check:
  for name,bb in out.items():assert(O/name).read_bytes()==bb,name
  idx=json.loads((O/'first-candidate/INDEX.json').read_text())
  for name,r in idx.items():bb=(O/'first-candidate'/name).read_bytes();assert bb==(O/name).read_bytes()and H(bb)==r['sha256']and len(bb)==r['bytes']
 else:
  d=O/'first-candidate';assert not d.exists(),'refuse first candidate overwrite'
  for name in out:assert not(O/name).exists(),'refuse generated overwrite'
  copies={**out,'REPORT.md':(O/'REPORT.md').read_bytes(),pathlib.Path(__file__).name:pathlib.Path(__file__).read_bytes()};ix=J({n:{'bytes':len(bb),'sha256':H(bb)}for n,bb in copies.items()})
  for name,bb in out.items():p=O/name;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(bb)
  for name,bb in copies.items():p=d/name;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(bb)
  (d/'INDEX.json').open('xb').write(ix)
 print(json.dumps({'check':check,'outputs':len(out),'original_execution':0}))
if __name__=='__main__':main()
