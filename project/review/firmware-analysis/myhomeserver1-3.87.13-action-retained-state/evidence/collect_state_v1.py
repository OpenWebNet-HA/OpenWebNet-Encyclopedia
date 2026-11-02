#!/usr/bin/env python3
"""One static retained string producer/global/selected status consumer relation."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());R=W/'work/myhomeserver1-firmware/3.87.13/research';V=R/'2026-10-31/image_vfs.py';IMG='/home/bticino/scheduling_manager/scheduling_manager'
H=lambda x:hashlib.sha256(x).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
s=importlib.util.spec_from_file_location('retained_state_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
SPANS=[('first-capture-query-prefix',0xcf5d8,0xcf624),('first-return-nonnull-guard',0xcf622,0xcf640),('first-retained-string-word-stores',0xcf640,0xcf662),('second-global-string-selection',0xcdd9e,0xcddc8),('second-selected-on-arm',0xced78,0xced8a),('second-status-store-rejoin',0xced6a,0xced78),('second-descriptor-merge-guard',0xcddc8,0xcddf4),('second-ID-merge-local',0xce084,0xce0d0),('second-status-pair-copy',0xcddf4,0xcde00),('second-actual-params-source',0xcdf0e,0xcdf1a),('converter-result-source-ABI',0xd1640,0xd165e),('converter-status-guard-index',0xd1668,0xd1674),('converter-status-table-selection',0xd1726,0xd1752),('converter-short-string-branch',0xd18c8,0xd18da),('converter-length-two-copy-path',0xd18e8,0xd18fa),('converter-status-copy-rejoin',0xd1764,0xd1772),('converter-status-member-store',0xd1682,0xd16a6)]
GUARDS=[(0xcf5d8,'8346'),(0xcf5dc,'00f10409'),(0xcf5f4,'036b'),(0xcf5f6,'002b'),(0xcf618,'4b46'),(0xcf61a,'0022'),(0xcf622,'2c68'),(0xcf624,'64b3'),(0xcf644,'04f10801'),(0xcf64a,'1830'),(0xcf654,'626a'),(0xcf658,'1a63'),(0xcf65a,'a26a'),(0xcf65c,'5a63'),(0xcf65e,'e26a'),(0xcf660,'9a63'),(0xcddac,'0121'),(0xcddb0,'d3e90602'),(0xcddbc,'022a'),(0xced78,'0378'),(0xced7a,'6f2b'),(0xced80,'4378'),(0xced82,'6e2b'),(0xced6c,'0139'),(0xced6e,'0123'),(0xced70,'1162'),(0xced72,'1377'),(0xcddd4,'94f84c30'),(0xce0ca,'81f84c30'),(0xcddf4,'4aab'),(0xcddf6,'93e80300'),(0xcddfa,'9dab'),(0xcddfc,'83e80300'),(0xcdf0e,'96ab'),(0xcdf12,'1946'),(0xd1644,'0c46'),(0xd164c,'0646'),(0xd1668,'237f'),(0xd166c,'236a'),(0xd166e,'0133'),(0xd1670,'022b'),(0xd1736,'52f83370'),(0xd173e,'d1f804a0'),(0xd174c,'0097'),(0xd1764,'3a46'),(0xd18c8,'012f'),(0xd18f4,'4046')]
TARGETS=[(0xcf5f8,0xcf6ba),(0xcf61e,0x10f4a0),(0xcf624,0xcf680),(0xcddbe,0xced78),(0xced7c,0xcddc8),(0xced84,0xcddc8),(0xced88,0xced6a),(0xced74,0xcddc8),(0xcddde,0xce084),(0xce0ce,0xcddf4),(0xcdf16,0xd163c),(0xd166a,0xd16b4),(0xd1672,0xd1726),(0xd174e,0xd18c8),(0xd18ca,0xd18e8),(0xd18e8,0xd18f4),(0xd18f8,0xd1764),(0xd1770,0xd1682)]
IMPORTS=[(0xcf64c,0x10d70,0x165ab8,'_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEE9_M_assignERKS4_@GLIBCXX_3.4.21'),(0xd1768,0x11474,0x165d08,'memcpy@GLIBC_2.4'),(0xd168c,0x11558,0x165d54,'_ZN4Json5ValueC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE'),(0xd1696,0x10c70,0x165a64,'_ZN4Json5ValueixEPKc'),(0xd169c,0x11294,0x165c68,'_ZN4Json5ValueaSEOS0_')]
def build():
 v=m.ImageVFS();b=v.read_bytes(IMG);assert H(b)=='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26';assert b[:7]==b'\x7fELF\x01\x01\x01'
 ph=struct.unpack_from('<I',b,28)[0];es,n=struct.unpack_from('<HH',b,42);L=[struct.unpack_from('<8I',b,ph+i*es)for i in range(n)]
 def off(a,n=1):return next(o+a-va for t,o,va,_,fs,*_ in L if t==1 and va<=a and a+n<=va+fs)
 def raw(a,n):o=off(a,n);return b[o:o+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def cs(a):o=off(a);return b[o:b.index(0,o)].decode()
 def br(pc,blx=False):
  x=int.from_bytes(raw(pc,2),'little')
  if not blx and x&0xf500==0xb100:return pc+4+((x>>9)&1)*64+((x>>3)&31)*2,2
  if not blx and x&0xf000==0xd000:
   d=x&255;return pc+4+2*(d-256 if d&128 else d),2
  if not blx and x&0xf800==0xe000:
   d=x&2047;return pc+4+2*(d-2048 if d&1024 else d),2
  x,y=struct.unpack('<HH',raw(pc,4));assert x&0xf800==0xf000
  if blx:assert y&0xd000==0xc000
  else:assert y&0xd000 in(0x8000,0x9000,0xd000)
  if not blx and y&0xd000==0x8000:
   s=x>>10&1;d=s<<20|(y>>11&1)<<19|(y>>13&1)<<18|(x&63)<<12|(y&2047)<<1;return(pc+4+d-((1<<21)if s else 0))&0xffffffff,4
  s=x>>10&1;i=1-((y>>13&1)^s);j=1-((y>>11&1)^s);d=s<<24|i<<23|j<<22|(x&1023)<<12|(y&2047)<<1;return(((pc+4)&~3 if blx else pc+4)+d-((1<<25)if s else 0))&0xffffffff,4
 hp=v.root/v.resolve(IMG).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');out={};sp=[]
 for name,a,e in SPANS:
  z=subprocess.check_output(['objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),IMG);assert'out of bounds'not in z
  out['spans/'+name+'.txt']=z.encode();sp.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'file_offset':hex(off(a,e-a)),'sha256':H(raw(a,e-a))})
 for a,z in GUARDS:assert raw(a,len(bytes.fromhex(z))).hex()==z,hex(a)
 targets=[]
 for pc,target in TARGETS:
  a,k=br(pc);assert a==target,hex(pc);targets.append({'VA':hex(pc),'bytes':raw(pc,k).hex(),'target':hex(target)})
 globalpics=[]
 for pool,pc in[(0xd01ac,0xcf648),(0xd01b0,0xcf656),(0xce890,0xcdda8)]:
  assert(u(pool)+pc+4)&0xffffffff==0x167808;globalpics.append({'pool_VA':hex(pool),'pool_word':hex(u(pool)),'ADD_PC_VA':hex(pc),'PC_value':hex(pc+4),'target_G':'0x167808'})
 rw=next(x for x in L if x[0]==1 and x[2]<=0x167808 and 0x167808+60<=x[2]+x[5]);assert rw[6]&2 and 0x167808>=rw[2]+rw[4]
 sh=struct.unpack_from('<I',b,32)[0];sz,sn,si=struct.unpack_from('<HHH',b,46);SH=[struct.unpack_from('<10I',b,sh+i*sz)for i in range(sn)];ss=SH[si];strings=b[ss[4]:ss[4]+ss[5]];sections=[]
 for x in SH:
  name=strings[x[0]:strings.index(0,x[0])].decode()
  if x[3]<=0x167808 and 0x167808+60<=x[3]+x[5]:assert name=='.bss'and x[1]==8;sections.append({'name':name,'type':'SHT_NOBITS','VA':hex(x[3]),'memory_bytes':x[5]})
 assert len(sections)==1
 rel=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(z.strip()for z in rel.splitlines()if z.startswith(f'{a:08x} '))
 assert (u(0xd1940)+0xd1660+4)&0xffffffff==0x1659a4
 slot=0x1659a4+u(0xd194c);assert slot==0x166eb4 and u(slot)==0x16216c
 table=u(slot);assert u(table+8)==2 and u(table+12)==0x1362d4 and cs(0x1362d4)=='on'
 tr=[]
 for a in(slot,table+12):r=rr(a);assert'R_ARM_RELATIVE'in r;tr.append(r)
 key=(u(0xd1944)+0xd1694+4)&0xffffffff;assert key==0x1151ac and cs(key)=='status'
 def rimm(x):r=((x>>8)&15)*2;z=x&255;return((z>>r)|(z<<(32-r)))&0xffffffff if r else z
 imports=[]
 for pc,plt,sl,name in IMPORTS:
  a,k=br(pc,True);assert a==plt;x,y,z=struct.unpack('<III',raw(plt,12));assert x&0xfffff000==0xe28fc000 and y&0xfffff000==0xe28cc000 and z&0xfffff000==0xe5bcf000;assert plt+8+rimm(x)+rimm(y)+(z&4095)==sl
  r=rr(sl);assert'R_ARM_JUMP_SLOT'in r and r.split()[-1]==name;imports.append({'call_VA':hex(pc),'call_bytes':raw(pc,4).hex(),'ARM_PLT':hex(plt),'ARM_PLT_bytes':raw(plt,12).hex(),'slot':hex(sl),'original_relocation':r})
 pins={IMG:{'sha256':H(b),'bytes':len(b)}}
 for p,role in[(V,'image_accessor'),(R/'2026-11-01-action-output/callable/REPORT.md','inherited_capture_and_callsite'),(R/'2026-11-01-action-output/reviews/callable-source-review.md','inherited_callable_review'),(R/'2026-11-01-action-request-values/values/REPORT.md','inherited_descriptor_and_converter'),(R/'2026-11-01-action-request-values/values/ORIGINAL_SOURCE.json','inherited_values_source'),(R/'2026-11-01-action-request-values/reviews/values-source-review.md','inherited_values_review'),(R/'2026-11-01-double-isolation/harness/RESULTS.json','unchanged_saved_native_ledger')]:
  z=p.read_bytes();pins[role]={'path':str(p.relative_to(W)),'sha256':H(z),'bytes':len(z)}
 out['ORIGINAL_SOURCE.json']=J({'image':IMG,'selected_code_spans':sp,'instruction_guards':[{'VA':hex(a),'bytes':z}for a,z in GUARDS],'selected_local_targets':targets,'retained_global':{'direct_PIC_joins':globalpics,'selected_memory_extent':'G..G+59 lies in writable memory-only PT_LOAD tail','PT_LOAD':{'file_offset':hex(rw[1]),'VA':hex(rw[2]),'file_bytes':rw[4],'memory_bytes':rw[5],'flags':rw[6]},'section':sections,'no_runtime_content_read':True,'no_class_RTTI_or_complete_extent_claim':True},'selected_converter_data':{'GOT_base_pool':'0xd1940','GOT_base_ADD_PC':'0xd1660','table_offset_pool':'0xd194c','GOT_slot':hex(slot),'table':hex(table),'selected_index':1,'selected_length':2,'selected_pointer_VA':hex(table+12),'selected_string_target':'0x1362d4','selected_literal_bytes':'6f6e00','original_relative_relocations':tr,'key_pool':'0xd1944','key_ADD_PC':'0xd1694','key_target':hex(key),'key':'status'},'selected_import_calls':imports,'not_audited':['query10f4a0 body/type/freshness','other record/state/property consumers','global initialization/reference/locking whole-program proof','output5dda0/receiving/transport/MQTT/libjel/auth/session/framing bodies','native/provider runtime/fixtures']})
 out['SELECTED_RELATION.json']=J({'producer':{'premises':['firstcapture48 nonzero and selected query path reached','query returns normalpair word0nonnull','valid returnedrecord string8/readablewords36/40/44 andnormalstringassignmentreturn'],'opaque_query':'0x10f4a0','destination_G':'0x167808','tuple':{'record_string8':'G_string24','record_word36':'G_word48','record_word40':'G_word52','record_word44':'G_word56'}},'consumer':{'source':'sameGstring24 pointer/length','selected_guard':'validlength2 and exact byteson','on_branch':'0xced78','literal_R1_origin':'1atcddac;subtract1atced6c→0','local_record':'SP268:presence28=1/status32=0','actual_copy':'SP296/SP300→SP628/SP632','actual_converter_source':'SP600=descriptorSP524+76; copiedpair28/32','selected_conversion':'source0+1→tableindex1,length2,on; statuskeyassignmentrequest'},'conditional_relation':'If selectedproducerwrite precedes selectedconsumerread without incompatible interveningmutation and allobject/provider/binding/branch premises hold, helperrequestsstatusstringon; no naturalorder/freshness/correlation/runtimeorphysicalproof.','namespaces':['G is fixed linked localglobal, not per-capture member or proven key-specific record','firstcaptureID/secondcaptureID/outerUUID remain distinct','localstatus0 is notOPENWHAT/kind/actionenum','sharedstopbyte167800 is separate fromG167808; no relationship fromadjacency'],'limits':['no broadstate/propertymatrix','no cachedrecordclass/type/layout transfer','no naturalfirst-second ordering or samequeuedaction proof','no wholelifetime/concurrency/initialization/freshness/globalabsence/defect conclusion','no output/success/physicalrestoration claim'],'execution':{'new_original':0,'semantic_models':0,'input_fixtures':0,'prior_ledger_unchanged':{'corpora':1,'entries':8,'original_visits':340,'C_primitives':0,'redirects':12,'EXIT':8,'stops':0,'hooks':360,'data_setup_relocations':4}}})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'sha256':H(z),'bytes':len(z)}for n,z in out.items()},'counts':{'spans':len(SPANS),'guards':len(GUARDS),'local_targets':len(targets),'global_PIC':len(globalpics),'selected_table_rows':1,'selected_table_relative_relocations':2,'import_call_PLT_proofs':len(imports),'inputs':len(pins),'original_execution_additions':0}})
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
 print(json.dumps({'check':ck,'outputs':len(out),'spans':len(SPANS),'guards':len(GUARDS),'local_targets':len(TARGETS),'new_original_execution':0}))
if __name__=='__main__':main()
