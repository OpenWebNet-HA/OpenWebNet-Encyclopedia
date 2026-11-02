#!/usr/bin/env python3
"""Bounded static descriptor constants and ID/speed converter/caller joins."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());R=W/'work/myhomeserver1-firmware/3.87.13/research';V=R/'2026-10-31/image_vfs.py';IMG='/home/bticino/scheduling_manager/scheduling_manager'
H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
s=importlib.util.spec_from_file_location('request_values_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
SPANS=[('descriptor-version-and-first-lock',0xd20c0,0xd2118),('descriptor-first-ID-requests',0xd2118,0xd214c),('descriptor-final-class-method',0xd214c,0xd21b0),('descriptor-second-ID-requests',0xd21be,0xd2200),('descriptor-normal-return',0xd2200,0xd221c),('params-initial-ID-guard',0xd163c,0xd1668),('params-ID-arm',0xd1772,0xd1794),('params-speed-guard',0xd16f0,0xd1708),('params-speed-arm',0xd17d8,0xd17fa),('caller-ID-mark-and-speed-input',0xcf72a,0xcf738),('caller-speed-positive-store',0xcf7a6,0xcf7b8),('caller-descriptor-ID-merge-guard',0xcf7b8,0xcf7e4),('caller-ID-out-of-line-merge',0xd05ac,0xd05fa),('caller-ID-non-single-length',0xd0f92,0xd0f9c),('caller-ID-long-copy',0xd0fc8,0xd0fee),('caller-parameter-pair-copy',0xcf7e4,0xcf820),('caller-actual-converter-input',0xcf8fc,0xcf91a)]
GUARDS=[(0xd20d2,'0446'),(0xd20ea,'1888'),(0xd20f6,'0322'),(0xd2102,'a260'),(0xd2104,'e373'),(0xd2112,'0028'),(0xd212a,'2421'),(0xd2136,'616b'),(0xd215a,'84f84cc0'),(0xd2164,'2360'),(0xd2176,'0fcb'),(0xd218c,'04f11c00'),(0xd21a4,'cdf80890'),(0xd21c6,'68bb'),(0xd21d0,'2421'),(0xd21ec,'4046'),(0xd2214,'2046'),(0xd2218,'bde8f087'),(0xd1644,'0c46'),(0xd164a,'0021'),(0xd164c,'0646'),(0xd165e,'2378'),(0xd1774,'211d'),(0xd16f0,'94f82430'),(0xd17da,'a16a'),(0xcf72e,'0170'),(0xcf7aa,'002b'),(0xcf7b0,'9362'),(0xcf7b4,'82f82430'),(0xcf7c4,'94f84c30'),(0xd05b6,'d3e90164'),(0xd05ec,'4c65'),(0xd05f2,'81f84c30'),(0xcf7f0,'2eab'),(0xcf7f2,'93e80300'),(0xcf7f6,'81ab'),(0xcf7f8,'83e80300'),(0xcf8fc,'78ab'),(0xcf900,'1946')]
PICS=[(0xd22b0,0xd20e8,0x116134,'2.0'),(0xd22c0,0xd2170,0x1361d4,'light.setStatus'),(0xd1950,0xd1780,0x116adc,'id'),(0xd195c,0xd17e6,0x115280,'speed')]
BRANCHES=[(0xd1664,0xd1772),(0xd16f6,0xd17d8),(0xcf7ce,0xd05ac),(0xd05ae,0xcf7e4),(0xd05f6,0xcf7e4),(0xd0f94,0xd05e8),(0xd0fea,0xd05e8),(0xcf7c0,0xd20c0),(0xcf904,0xd163c)]
IMPORTS=[(0xd210e,0x10aa0,0x1659cc,'pthread_mutex_lock@GLIBC_2.4'),(0xd211c,0x11228,0x165c44,'uuid_generate_random@UUID_1.0'),(0xd2132,0x1114c,0x165bfc,'_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE12_M_constructEjc@GLIBCXX_3.4.21'),(0xd213a,0x117bc,0x165e1c,'uuid_unparse_lower@UUID_1.0'),(0xd2148,0x1182c,0x165e40,'pthread_mutex_unlock@GLIBC_2.4'),(0xd21ac,0x10d70,0x165ab8,'_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_assignERKS4_@GLIBCXX_3.4.21'),(0xd21c2,0x10aa0,0x1659cc,'pthread_mutex_lock@GLIBC_2.4'),(0xd21ca,0x11228,0x165c44,'uuid_generate_random@UUID_1.0'),(0xd21de,0x117bc,0x165e1c,'uuid_unparse_lower@UUID_1.0'),(0xd21ee,0x10d70,0x165ab8,'_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_assignERKS4_@GLIBCXX_3.4.21'),(0xd165a,0x10cc4,0x165a80,'_ZN4Json5ValueC1ENS_9ValueTypeE'),(0xd1778,0x11558,0x165d54,'_ZN4Json5ValueC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE'),(0xd1782,0x10c70,0x165a64,'_ZN4Json5ValueixEPKc'),(0xd1788,0x11294,0x165c68,'_ZN4Json5ValueaSEOS0_'),(0xd17de,0x10dd4,0x165ad8,'_ZN4Json5ValueC1Ei'),(0xd17e8,0x10c70,0x165a64,'_ZN4Json5ValueixEPKc'),(0xd17ee,0x11294,0x165c68,'_ZN4Json5ValueaSEOS0_'),(0xd0fd0,0x11674,0x165db0,'_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_createERjj@GLIBCXX_3.4.21'),(0xd0fe0,0x11474,0x165d08,'memcpy@GLIBC_2.4')]
def build():
 v=m.ImageVFS();b=v.read_bytes(IMG);assert H(b)=='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26';assert b[:7]==b'\x7fELF\x01\x01\x01'
 ph=struct.unpack_from('<I',b,28)[0];es,n=struct.unpack_from('<HH',b,42);L=[struct.unpack_from('<8I',b,ph+i*es)for i in range(n)]
 def off(a,n=1):return next(o+a-va for t,o,va,_,fs,*_ in L if t==1 and va<=a and a+n<=va+fs)
 def raw(a,n):o=off(a,n);return b[o:o+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def cs(a):o=off(a);return b[o:b.index(0,o)].decode()
 def br(pc,blx=False):
  x,y=struct.unpack('<HH',raw(pc,4));assert x&0xf800==0xf000
  if blx:assert y&0xd000==0xc000
  else:assert y&0xd000 in(0x8000,0x9000,0xd000)
  if not blx and y&0xd000==0x8000:
   s=x>>10&1;d=s<<20|(y>>11&1)<<19|(y>>13&1)<<18|(x&63)<<12|(y&2047)<<1;return(pc+4+d-((1<<21)if s else 0))&0xffffffff
  s=x>>10&1;i=1-((y>>13&1)^s);j=1-((y>>11&1)^s);d=s<<24|i<<23|j<<22|(x&1023)<<12|(y&2047)<<1;return(((pc+4)&~3 if blx else pc+4)+d-((1<<25)if s else 0))&0xffffffff
 hp=v.root/v.resolve(IMG).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');out={};sp=[]
 for name,a,e in SPANS:
  z=subprocess.check_output(['objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),IMG);assert'out of bounds'not in z
  out['spans/'+name+'.txt']=z.encode();sp.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'file_offset':hex(off(a,e-a)),'sha256':H(raw(a,e-a))})
 for a,z in GUARDS:assert raw(a,len(bytes.fromhex(z))).hex()==z,hex(a)
 pics=[]
 for pool,pc,target,z in PICS:
  assert(u(pool)+pc+4)&0xffffffff==target and cs(target)==z;pics.append({'pool_VA':hex(pool),'pool_word':hex(u(pool)),'ADD_PC_VA':hex(pc),'target':hex(target),'literal':z,'literal_bytes':raw(target,len(z)+1).hex()})
 branches=[]
 for pc,target in BRANCHES:
  x=int.from_bytes(raw(pc,2),'little')
  if x&0xf000==0xd000:
   d=x&255;actual=(pc+4+2*(d-256 if d&128 else d))&0xffffffff
  else:actual=br(pc)
  assert actual==target,hex(pc);branches.append({'VA':hex(pc),'bytes':raw(pc,2 if x&0xf000==0xd000 else 4).hex(),'target':hex(target)})
 rel=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(z.strip()for z in rel.splitlines()if z.startswith(f'{a:08x} '))
 def rimm(x):r=((x>>8)&15)*2;z=x&255;return((z>>r)|(z<<(32-r)))&0xffffffff if r else z
 imports=[]
 for pc,plt,slot,name in IMPORTS:
  assert br(pc,True)==plt,hex(pc);x,y,z=struct.unpack('<III',raw(plt,12));assert x&0xfffff000==0xe28fc000 and y&0xfffff000==0xe28cc000 and z&0xfffff000==0xe5bcf000
  assert plt+8+rimm(x)+rimm(y)+(z&4095)==slot
  r=rr(slot);assert'R_ARM_JUMP_SLOT'in r and r.split()[-1]==name
  imports.append({'call_VA':hex(pc),'call_bytes':raw(pc,4).hex(),'ARM_PLT':hex(plt),'ARM_PLT_bytes':raw(plt,12).hex(),'slot':hex(slot),'original_relocation':r})
 classes=[]
 for pool,slot,h,ti,np,name in[(0xd22ac,0x165fd0,0x1607e8,0x1631e8,0x11615c,'14JsonRpcRequest'),(0xd22bc,0x166460,0x162154,0x1650dc,0x13629c,'18LightSetStatusBean')]:
  assert 0x1659a4+u(pool)==slot and u(slot)==h and u(h)==0 and u(h+4)==ti and u(ti+4)==np and cs(np)==name
  rs=[]
  for a in(slot,h+4,ti+4):r=rr(a);assert'R_ARM_RELATIVE'in r;rs.append(r)
  classes.append({'pool_VA':hex(pool),'GOT_slot':hex(slot),'header_VA':hex(h),'address_point':hex(h+8),'RTTI_VA':hex(ti),'name_VA':hex(np),'RTTI_name':name,'primary_Thumb':hex(u(h+8)),'relative_relocations':rs})
 bases=[]
 for pool,pc in[(0xd22a8,0xd20d6),(0xd1940,0xd1660)]:assert(u(pool)+pc+4)&0xffffffff==0x1659a4;bases.append({'pool':hex(pool),'word':hex(u(pool)),'ADD_PC_VA':hex(pc),'GOT_base':'0x1659a4'})
 pins={IMG:{'sha256':H(b),'bytes':len(b)}}
 for p,role in[(V,'image_accessor'),(R/'2026-11-01-action-output/callable/REPORT.md','inherited_capture_and_request_handoff'),(R/'2026-11-01-action-output/callable/ORIGINAL_SOURCE.json','inherited_callsite_source'),(R/'2026-11-01-action-output/reviews/callable-source-review.md','prior_independent_source_review'),(R/'2026-11-01-double-isolation/harness/RESULTS.json','unchanged_saved_native_ledger'),(W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0199-myhomeserver1-home-automation-server.md','current_curated_role')]:
  z=p.read_bytes();pins[role]={'path':str(p.relative_to(W)),'sha256':H(z),'bytes':len(z)}
 out['ORIGINAL_SOURCE.json']=J({'image':IMG,'PT_LOAD':[{'file_offset':hex(o),'VA':hex(va),'file_bytes':fs,'memory_bytes':ms,'flags':f}for t,o,va,pa,fs,ms,f,al in L if t==1],'selected_code_spans':sp,'instruction_guards':[{'VA':hex(a),'bytes':z}for a,z in GUARDS],'literal_pool_data':pics,'GOT_base_PIC':bases,'class_data':classes,'local_control_flow':branches,'selected_import_calls':imports,'not_audited':['descriptor primary virtual body0xd197c','other params fields/status-table/value cases','output5dda0 and receiving/transport/MQTT/libjel/auth/session/framing delegate bodies','provider bodies/runtime/canonical fixtures']})
 out['SELECTED_CONTRACT.json']=J({'descriptor':{'version_string4':'2.0','method_string28':'light.setStatus','outer_ID_string52':'two generation/unparse request pairs; later temporary string assignment replaces earlier outerID on normal path','initial_RTTI':'14JsonRpcRequest','final_RTTI':'18LightSetStatusBean','params_presence76':'initialized0'},'params_helper_ABI':'hidden resultR0/sourceR1, savedR6/R4; no this/vtable dispatch here','selected_params':[{'key':'id','presence_byte':0,'value':'string subobject4','arm':'0xd1772'},{'key':'speed','presence_byte':36,'value':'signedword40 to Json::Value(int)','arm':'0xd17d8'}],'first_caller_join':{'capture':'configuredIDstring4/capturedspeedword0 distinct52Bcapture','prefix':'SP148: IDpresence0=1; signedpositivecapture0→presence36=1/value40','descriptor':'SP404; constructorpresence76=0 selectsout-of-lineIDcopyd05ac→d05f2→cf7e4','actual_converter_source':'SP480=descriptor+76, not prefixSP148','ID':'descriptor80=source4; copiedconfiguredID string, not outerUUIDID','speed':'pairSP184/188(prefix36/40)→SP516/520(convertersource36/40)','assumptions':['blocks reached normally with valid object/storage','normal string allocation/copy/assignment, UUID/mutex and JsonCpp/provider returns','same captured/merged record lifetime and no incompatible mutation','candidate import binding/ABI/canary']},'limits':['not a full payload/schema/status table','no actual UUID values/uniqueness/randomness','no naturalscene/physicalcommand/delivery/restore/correlation','no outputdelegate implementation','no whole constructor/unwind/concurrency ownership proof'],'execution':{'new_original':0,'semantic_models':0,'input_fixtures':0,'prior_ledger_unchanged':{'corpora':1,'entries':8,'original_visits':340,'C_primitives':0,'redirects':12,'EXIT':8,'stops':0,'hooks':360,'data_setup_relocations':4}}})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'sha256':H(z),'bytes':len(z)}for n,z in out.items()},'counts':{'code_spans':len(SPANS),'guards':len(GUARDS),'literal_PIC':len(pics),'class_identities':len(classes),'relative_relocations':6,'GOT_base_PIC':len(bases),'local_branches_calls':len(branches),'import_call_PLT_proofs':len(imports),'inputs':len(pins),'original_execution_additions':0}})
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
 print(json.dumps({'check':ck,'outputs':len(out),'spans':len(SPANS),'guards':len(GUARDS),'import_call_proofs':len(IMPORTS),'new_original_execution':0}))
if __name__=='__main__':main()
