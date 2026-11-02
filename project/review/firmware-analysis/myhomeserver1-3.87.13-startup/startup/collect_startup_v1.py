#!/usr/bin/env python3
"""Static executable entry / selected service-to-loader argument provenance only."""
import sys
sys.dont_write_bytecode=True
import pathlib,struct,hashlib,json,subprocess,re,os,argparse,importlib.util
O=pathlib.Path(__file__).resolve().parent;W=next(p for p in O.parents if(p/'sources').is_dir());R=W/'work/myhomeserver1-firmware/3.87.13/research/2026-10-31'
spec=importlib.util.spec_from_file_location('ivfs',R/'image_vfs.py');vm=importlib.util.module_from_spec(spec);spec.loader.exec_module(vm)
H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
S='/home/bticino/scheduling_manager/scheduling_manager';C='/home/bticino/scheduling_manager/config.json'
def build():
 v=vm.ImageVFS();b=v.read_bytes(S);assert H(b)=='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26';ph=struct.unpack_from('<I',b,28)[0];sz,n=struct.unpack_from('<HH',b,42);segs=[struct.unpack_from('<8I',b,ph+i*sz)for i in range(n)]
 def off(a,n=1):return next(o+a-va for t,o,va,_,fs,*_ in segs if t==1 and va<=a and a+n<=va+fs)
 def raw(a,n):return b[off(a,n):off(a,n)+n]
 def word(a):return struct.unpack('<I',raw(a,4))[0]
 def txt(a):i=off(a);z=b.index(0,i);assert z-i<256;return b[i:z].decode()
 out={};pins={S:{'sha256':H(b),'bytes':len(b),'resolved_image_path':v.resolve(S)}};cfg=v.read_bytes(C);pins[C]={'sha256':H(cfg),'bytes':len(cfg),'resolved_image_path':v.resolve(C)}
 for p,k in [(R/'image_vfs.py','image_accessor'),(R.parents[1]/'analysis/normal-regular-files.json','regular_metadata'),(R.parents[1]/'analysis/normal-symlinks.json','symlink_metadata')]:z=p.read_bytes();pins[k]={'sha256':H(z),'bytes':len(z)}
 spans=[('elf-entry',0x17228,0x1725c),('main-prefix-and-settings-choice',0x130a0,0x13188),('settings-default-scenes-field',0x1dae4,0x1db34),('settings-parser-request-and-result',0x32cb8,0x32d18),('settings-scenes-path-assignment',0x32ee6,0x32f5a),('settings-scenes-short-copy',0x3341a,0x33438),('scenes-path-getter',0x32ae4,0x32b84),('main-time-service-construction',0x13288,0x132e4),('main-opaque-preloader-calls',0x132e4,0x1333a),('main-scenes-loader-handoff',0x1333a,0x1334e),('main-zero-settings-return-continuation',0x1370a,0x13718),('service-flag-to-thread-request',0xb94f0,0xb9596),('loader-argument-save-prefix',0x17630,0x17650)]
 host=v.root/v.resolve(S).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');records=[]
 for name,a,z in spans:
  s=subprocess.check_output(['objdump','-d','--dwarf=no-follow-links','-M','force-thumb',f'--start-address={a}',f'--stop-address={z}',str(host)],text=True,env=env).replace(str(host),S);s=re.sub(r' <([^>]+)>',lambda m:m[0]if'@plt'in m[1]else'',s);out['spans/'+name+'.txt']=s.encode();records.append({'name':name,'path':S,'start_VA':hex(a),'end_VA_exclusive':hex(z),'file_offset':hex(off(a,z-a)),'raw_sha256':H(raw(a,z-a))})
 guards=[(0x17246,'0448'),(0x17248,'5af80000'),(0x13142,'b8f1010f'),(0x13182,'002c'),(0x13184,'00f0c182'),(0x13716,'37e5'),(0x13298,'7020'),(0x132c8,'0121'),(0x132d2,'4af8103b'),(0x132e0,'cbe900a9'),(0x13342,'dbf80020'),(0x13346,'2146'),(0x13348,'4046'),(0x32afe,'d1e90f65'),(0x32f1c,'c6e90f12'),(0xb9534,'65b9'),(0xb9566,'4460'),(0x17634,'8346'),(0x17642,'0190'),(0x1764c,'0593')]
 for a,h in guards:assert raw(a,len(bytes.fromhex(h))).hex()==h,hex(a)
 joins=[]
 def pic(pool,pc,want,text=None):
  a=(word(pool)+pc+4)&0xffffffff;assert a==want
  if text is not None:assert txt(a)==text
  joins.append({'pool_VA':hex(pool),'pool_word':hex(word(pool)),'ADD_PC_VA':hex(pc),'target_VA':hex(a),'literal':text})
 pic(0x13aa8,0x13152,0x114210,'./scheduling_manager/config.json');pic(0x33748,0x32eec,0x115df8,'scenesPath');pic(0x1dc08,0x1db2a,0x1144a0,'/home/bticino/cfg/extra/0/scheduling_manager')
 entry=struct.unpack_from('<I',b,24)[0];assert entry==0x17229;got=(0x17254+word(0x17254))&0xffffffff;assert got==0x1659a4;slot=got+word(0x17258);assert slot==0x166198 and word(slot)==0x130a1
 controlslot=got+word(0x13ac8);assert controlslot==0x166234;header=word(controlslot);assert header==0x15fd40;rt=word(header+4);name=txt(word(rt+4));assert name=='St23_Sp_counted_ptr_inplaceI19TimeTriggersServiceSaIS0_ELN9__gnu_cxx12_Lock_policyE2EE'
 rel=subprocess.check_output(['readelf','-rW',str(host)],text=True,env=env);rels=[]
 for a in [slot,controlslot]:
  line=next(x for x in rel.splitlines()if x.startswith(f'{a:08x} '));assert'R_ARM_RELATIVE'in line;rels.append(line.strip())
 sy=subprocess.check_output(['readelf','--dyn-syms','-W',str(host)],text=True,env=env);needed=subprocess.check_output(['readelf','-dW',str(host)],text=True,env=env)
 # Whitelist one noncredential setting; never export the full packaged JSON.
 selected=json.loads(cfg)['scenesPath'];assert selected=='/home/bticino/cfg/extra/0/scheduling_manager'
 out['ORIGINAL_SOURCE.json']=J({'spans':records,'file_byte_guards':[{'VA':hex(a),'bytes':h}for a,h in guards],'PIC':joins,'entry_chain':{'e_entry_Thumb':hex(entry),'code_VA':'0x17228','ADR_base_VA':'0x17254','GOT_VA':hex(got),'main_slot_VA':hex(slot),'stored_main_Thumb':hex(word(slot)),'libc_start_main_request_VA':'0x1724c'},'service_control_identity':{'GOT_slot':hex(controlslot),'vtable_header_VA':hex(header),'RTTI_VA':hex(rt),'RTTI_name':name},'selected_relocations':rels})
 out['ARGUMENT_LEDGER.json']=J({'main':'0x130a0','settings':{'object':'mainSP336','constructor':'0x1dae4','input_path':'argv[1] when argc>1, otherwise exact relative default','load_request':'0x1316a→0x32b8c','return_zero':'0x13184→0x1370a diagnostic→0x13716→0x13188; not an exit gate','scenes_key':'scenesPath','field':60,'getter':'0x32ae4','normal_success_assignment':'0x32eee/asString0x32efa→field60 (heap/string-copy branches retain same destination)','packaged_whitelist':{'scenesPath':selected},'default_field_same_path':True,'limits':'Settings parser/file/diagnostic helpers remain normal-return prerequisites; no actual configuration parse or input-file admission asserted.'},'container':{'address':'mainSP160','initialization':'selected local tree/field writes at0x13288; semantic container layout assigned to separate author','preservation':'r4=SP160, held across normal EABI callee-preserving delegates'},'time_service':{'allocation_request_bytes':112,'allocation_base_register':'r9','inner_pointer':'allocation+16 heldsl','constructor':'0xb94f0','supplied_flag':1,'flag_premise':'ctor copies incomingr1 tor5; nonzero→0xb9550 thread allocation/request branch','same_pair_store':'0x132e0 mainSP88=(inner,allocation/controlbase)','stored_service_pointer':'SP88word0','thread_request':'0xb9574 std::thread::_M_start_thread; no successful thread/service assumed'},'loader_call':{'VA':'0x1334a','target':'0x17630','r0':'fresh copy of settings+60 string from getter32ae4 at1333e','r1':'same localcontainerSP160','r2':'same serviceinner pointer loadedSP88 at13342','callee_save':'loader stores containerSP4 at17642 and serviceSP20 at1764c; r0path heldfp','boundary':'Stop at selected loader argument capture. Parsing, registry insertion, later handlers and transport are separate scopes.'},'opaque_preloader_calls':['guardedglobal/container operations between132e4and1333a','settings parser/file helpers','logger/diagnostic calls'], 'original_execution':0})
 out['PROVIDER_REQUESTS.json']=J({'DT_NEEDED':re.findall(r'\(NEEDED\).*?\[(.*?)\]',needed),'selected_import_declarations':[x.strip()for x in sy.splitlines()if any(k in x for k in ['__libc_start_main','_M_start_thread','parseFromStream','basic_filebufIcSt11char_traitsIcEE4open'])],'scope':'Direct executable requests only; no loader-effective binding, libc/libstdc++/JsonCpp bodies, target syscalls or process execution.'})
 cases=[]
 for argc,loaded in [(1,0),(1,1),(2,0),(2,1)]:cases.append({'synthetic_argc':argc,'synthetic_settings_return':loaded,'path_source':'argv[1]'if argc>1 else'default literal','zero_diagnostic_requested':loaded==0,'reaches_selected_constructor_after_normal_delegates':True,'constructor_flag':1,'scope':'Finite branch decisions only; no args/config/parser/process/thread/scene objects executed.'})
 out['HOST_BRANCH_CASES.json']=J({'cases':cases,'original_execution':0});out['INPUTS.json']=J(pins);out['METHOD.json']=J({'method':'ImageVFS original ELF32 PT_LOAD/Thumb2/PIC/GOT/RTTI/relative relocations, safe single-key packaged JSON data extraction, four host branch examples','original_instructions':0,'vendor_processes':0,'target_API_or_IO':0,'native_emulation':0,'configuration_parser_execution':0,'no_transport_auth_session_framing_bodies':True})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(pathlib.Path(__file__).read_bytes()),'report_sha256':H((O/'REPORT.md').read_bytes()),'outputs':{n:{'sha256':H(z),'bytes':len(z)}for n,z in out.items()},'counts':{'spans':len(spans),'byte_guards':len(guards),'PIC':len(joins),'relative_slots':len(rels),'inputs':len(pins),'host_cases':len(cases),'original_execution':0}});return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');check=ap.parse_args().check;o=build()
 if check:
  for n,b in o.items():assert(O/n).read_bytes()==b,n
  ix=json.loads((O/'first-candidate/INDEX.json').read_text())
  for n,r in ix.items():z=(O/'first-candidate'/n).read_bytes();assert z==(O/n).read_bytes()and H(z)==r['sha256']and len(z)==r['bytes']
 else:
  d=O/'first-candidate';assert not d.exists(),'refuse first snapshot overwrite'
  for n in o:assert not(O/n).exists(),'refuse generated overwrite'
  cp={**o,'REPORT.md':(O/'REPORT.md').read_bytes(),pathlib.Path(__file__).name:pathlib.Path(__file__).read_bytes()};ix=J({n:{'sha256':H(z),'bytes':len(z)}for n,z in cp.items()})
  for n,z in o.items():p=O/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  for n,z in cp.items():p=d/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  (d/'INDEX.json').open('xb').write(ix)
 print(json.dumps({'check':check,'outputs':len(o),'original_execution':0}))
if __name__=='__main__':main()
