#!/usr/bin/env python3
"""Static original-byte SQL owner/registry joins; never executes SQL or image code.
Exclusive first generation; --check only reads/compares. No emulation.
"""
import sys
sys.dont_write_bytecode=True
import argparse,hashlib,importlib.util,json,pathlib,re,struct,subprocess,os
O=pathlib.Path(__file__).resolve().parent;W=next(p for p in O.parents if(p/'sources').is_dir());R=W/'work/myhomeserver1-firmware/3.87.13/research/2026-10-31'
spec=importlib.util.spec_from_file_location('frozen_vfs',R/'image_vfs.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
H=lambda b:hashlib.sha256(b).hexdigest();J=lambda v:(json.dumps(v,indent=2,sort_keys=True,ensure_ascii=True)+'\n').encode()
P='/home/bticino/matrix_mx/matrix_mx'
def build():
 out={};pins={};v=m.ImageVFS();b=v.read_bytes(P);assert H(b)=='96348136c2a0ebe859c689eb6246e3889e5154fdb63ffd5f3fc76975ac596717'
 pins['normal:'+P]={'bytes':len(b),'sha256':H(b),'resolved_image_path':v.resolve(P)}
 for p,n in [(R/'image_vfs.py','image_accessor'),(R.parents[1]/'analysis/normal-regular-files.json','regular_metadata'),(R.parents[1]/'analysis/normal-symlinks.json','symlink_metadata')]:bb=p.read_bytes();pins[n]={'bytes':len(bb),'sha256':H(bb)}
 ph=struct.unpack_from('<I',b,28)[0];sz,n=struct.unpack_from('<HH',b,42);segs=[struct.unpack_from('<8I',b,ph+i*sz)for i in range(n)]
 def off(a,z=1):return next(o+a-va for t,o,va,_,fs,*_ in segs if t==1 and va<=a and a+z<=va+fs)
 def raw(a,z):return b[off(a,z):off(a)+z]
 def word(a):return struct.unpack('<I',raw(a,4))[0]
 def text(a):
  q=off(a);end=b.index(0,q);assert end-q<4096;return b[q:end].decode()
 host=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='')
 # Each tuple is bounded original source. Runtime/global registration is not executed.
 spans=[('reader-column-alias',0xa8c56,0xa8ca8),('factory-prologue-and-base-vtable',0xb9934,0xb99aa),('factory-inline-query-results',0xb99aa,0xb9a38),('base-query-copy-and-context',0xb91b0,0xb9220),('replace-modobj',0xb9220,0xb9278),('replace-line-modobj',0xb9298,0xb92f8),('replace-brand-modobj',0xb9314,0xb9372),('replace-key-object',0xb938e,0xb93e6),('startup-template-copy',0x155ac,0x155d2),('startup-registry-setup',0x156a2,0x156d8),('startup-callable-columns',0x15894,0x158d2),('startup-key139-record',0x15d0e,0x15d3a),('startup-registry-construction',0x15d9a,0x15dc8),('initializer-veneer',0x161c8,0x161cc),('natural-registry-lookup',0xa13a0,0xa13e0),('natural-callable-invocation',0xa1400,0xa1440),('callable-invoker',0xa2a14,0xa2a5c),('context-getter-model',0x10017c,0x100180),('context-getter-line',0x1001b4,0x1001b8),('context-getter-brand',0x1001d0,0x1001d4),('string-range-copy',0x95384,0x9540c),('signed-decimal-string',0x6e810,0x6e978)]
 prov=[]
 for name,a,z in spans:
  s=subprocess.run(['objdump','-d','--dwarf=no-follow-links','-M','force-thumb',f'--start-address={a}',f'--stop-address={z}',str(host)],capture_output=True,text=True,check=True,env=env).stdout.replace(str(host),P)
  s=re.sub(r' <([^>]+)>',lambda mm:mm.group(0)if '@plt'in mm[1]else'',s);out['spans/'+name+'.txt']=s.encode();prov.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(z),'file_offset':hex(off(a,z-a)),'bytes':z-a,'sha256':H(raw(a,z-a))})
 # Explicit halfwords avoid confusing objdump display order with file byte order.
 guards=[(0xb997e,[0x218b]),(0xb9982,[0xf7ff,0xfc15]),(0xb99a4,[0x60e3]),(0xb99dc,[0x6b21]),(0xb9a0a,[0x6223]),(0xb9a1c,[0x6263]),(0xb9210,[0xe9d3,0x1200]),(0xb921c,[0xf7dc,0xf8b2]),(0xb9238,[0x6871]),(0xb92b0,[0x68b1]),(0xb932c,[0x68f1]),(0xb93a8,[0x6931]),(0x15d24,[0xf8c4,0xc384]),(0x15d36,[0xf8c4,0x3388]),(0xa143c,[0x47c0]),(0xa2a3a,[0x47a8]),(0x10017c,[0x6cc0]),(0x1001b4,[0x6d00]),(0x1001d0,[0x6d40])]
 for a,words in guards:assert raw(a,2*len(words))==struct.pack('<'+'H'*len(words),*words),hex(a)
 pool=[]
 def pic(p,a,want):
  target=(word(p)+a+4)&0xffffffff;assert target==want;pool.append({'pool_VA':hex(p),'word':hex(word(p)),'ADD_PC_VA':hex(a),'target_VA':hex(target)});return target
 template_global=pic(0x16010,0x155b8,0x210720);sqladdr=pic(0x16014,0x155ba,0x1c4f70);assert pic(0xb94b8,0xb91fc,0x210720)==template_global
 got=pic(0x15fcc,0x154a8,0x20de04);assert pic(0xb9a88,0xb9950,0x20de04)==got
 assert pic(0xb9a94,0xb999c,0x1ccdec)==0x1ccdec
 for p,a,t in [(0xb94bc,0xb922a,0x1cce54),(0xb94c0,0xb92a6,0x1cce60),(0xb94c4,0xb9322,0x1cce70),(0xb94c8,0xb939a,0x1cce80)]:pic(p,a,t)
 pic(0x16044,0x156ba,0x210720);pic(0xa1504,0xa1354,0x210720)
 slots=[]
 for p,expected_slot,expected_value in [(0xb9a90,0x20e64c,0x20a878),(0x1612c,0x20ec9c,0xb9935),(0x16074,0x20ee98,0xa2a15),(0x16078,0x20ecd8,0xa63b5)]:
  slot=got+word(p);assert slot==expected_slot and word(slot)==expected_value;slots.append({'pool_VA':hex(p),'offset':hex(word(p)),'GOT_base':hex(got),'slot_VA':hex(slot),'slot_file_offset':hex(off(slot,4)),'stored_value':hex(word(slot))})
 assert word(0x20a880)==0xa8c01 and word(0x20a87c)==0x20cba0 and word(0x20cba4)==0x1cd1a0 and text(0x1cd1a0)=='14kobj_value_139'
 data=[{'name':'class139-vtable','start_VA':'0x20a878','file_offset':hex(off(0x20a878,32)),'words':[hex(word(a))for a in range(0x20a878,0x20a898,4)],'sha256':H(raw(0x20a878,32))},{'name':'class139-RTTI','start_VA':'0x20cba0','file_offset':hex(off(0x20cba0,12)),'words':[hex(word(a))for a in range(0x20cba0,0x20cbac,4)],'name_pointer':'0x1cd1a0','name':text(0x1cd1a0),'sha256':H(raw(0x20cba0,12))}]
 rel=subprocess.run(['readelf','-rW',str(host)],capture_output=True,text=True,check=True,env=env).stdout
 selected=[]
 for a in [0x20a87c,0x20a880,0x20cba4,0x20e64c,0x20ec9c,0x20ee98,0x20ecd8]:
  line=next(l for l in rel.splitlines()if l.startswith(f'{a:08x} '));assert 'R_ARM_RELATIVE'in line;selected.append(line.strip())
 sh=struct.unpack_from('<I',b,32)[0];ss,n,si=struct.unpack_from('<HHH',b,46);sections=[struct.unpack_from('<10I',b,sh+i*ss)for i in range(n)];ns=b[sections[si][4]:sections[si][4]+sections[si][5]];ar=next(x for x in sections if ns[x[0]:].split(b'\0',1)[0]==b'.init_array');vals=struct.unpack_from('<'+'I'*(ar[5]//4),b,ar[4]);assert vals[11]==0x161c9
 sql=text(sqladdr);assert sql.startswith('SELECT DISTINCT ') and '$key_object$'in sql
 columns=sql.split(' FROM ',1)[0].removeprefix('SELECT DISTINCT ').split(', ');assert len(columns)==15 and columns[13]=='EN_KEY_OBJECT.slots'and columns[14]=='AS_OBJECT_SYSTEM.id_system'
 placeholders=['$modobj$','$line_modobj$','$brand_modobj$','$key_object$'];assert all(sql.count(x)==1 for x in placeholders)
 out['SQL_TEMPLATE.json']=J({'original_VA':hex(sqladdr),'file_offset':hex(off(sqladdr)),'sha256_UTF8':H(sql.encode()),'bytes_excluding_NUL':len(sql.encode()),'SQL':sql,'columns_zero_based':[{'index':i,'expression':x}for i,x in enumerate(columns)],'statement_execution':0,'privacy':'Only original SQL schema/column/predicate text, never returned data/default/config values'})
 out['ORIGINAL_SOURCE.json']=J({'ELF':P,'sha256':H(b),'spans':prov,'assertions':[{'VA':hex(a),'Thumb_halfwords':[hex(x)for x in words],'file_bytes':struct.pack('<'+'H'*len(words),*words).hex()}for a,words in guards],'PIC_pool_arithmetic':pool,'GOT_value_chains':slots,'relocations':selected,'relocated_data':data,'initializer':{'section_VA':hex(ar[3]),'file_offset':hex(ar[4]),'entries':len(vals),'index':11,'stored_Thumb_pointer':'0x161c9','tail_target':'0x15464'},'BSS_note':'Templateglobal210720 and registry210b1c are derived initialized addresses, not fabricated file-backed pointers or observed live values.'})
 out['OWNER_ALIAS_LEDGER.json']=J({'class_RTTI':'14kobj_value_139','vtable_address_point':'0x20a880','method0_stored_Thumb_pointer':'0xa8c01','factory_entry':'0xb9934','allocation_request_bytes':72,'returned_pair':'inner=allocation+12 plus shared ownership/control pointer allocation','base_constructor':'0xb91b0','base_input_arguments':['inner','key139','modobj','line_modobj','brand_modobj'],'inner_fields':{'4':'modobj','8':'line_modobj','12':'brand_modobj','16':'key139','20':'last selected converted EN_KEY_OBJECT.slots','24':'last selected converted AS_OBJECT_SYSTEM.id_system','36':'SQL string pointer','40':'SQL length','44':'SQL inline/capacity storage'},'outer_to_inner':{'outer48':'inner36 SQL','outer32':'inner20 slots','outer36':'inner24 systemID'},'template_global':'0x210720','replacement_order':placeholders,'replacement_field_offsets':[4,8,12,16],'startup_registry':'0x210b1c','selected_registry_record':{'relative_to_stack_array_base':900,'key':139,'factory_data_offset':904,'manager_offset':912,'invoker_offset':916,'factory_Thumb_pointer':'0xb9935','invoker_Thumb_pointer':'0xa2a15'},'natural_walker':{'entry':'0xa1320','current_integer_keys':'vector-like current range through word[input+0] offsets12/16; actual producer not traced','registry_base_PC_join':'0xa1354 target210720 plus1020','lookup_requires':'matching current integer key, present registry entry, nonempty selected callable','context_value_sources':{'modobj':'current context+76 via10017c','line_modobj':'current context+80 via1001b4','brand_modobj':'current context+84 via1001d0'},'indirect_call':'a143c→selected invokera2a14→storedfactoryb9934','conditionality':'Requires normal initializer/container/callable completion, selected139 entry retained without interposition/later mutation, current key139 and successful allocation/string/provider delegates; not runtime activation.'},'not_established':['all registry keys/collision/later mutation policy','natural source of context numeric values or integer-key list','complete device/Firmware/version eligibility','later uses of slots/systemID after selected stores','query success or actual row ordering/cardinality','complete shared ownership/destructor/exception behavior'],'original_execution':0,'SQL_execution':0})
 # Pure textual fixture only. No SQLite connection or expression evaluator is used.
 fixture={'$modobj$':2,'$line_modobj$':0,'$brand_modobj$':1,'$key_object$':139};rendered=sql
 for k,num in fixture.items():rendered=rendered.replace(k,str(num))
 out['HOST_TEXT_MODEL.json']=J({'scope':'Synthetic positive integer text substitution after the original construction/formatting boundaries; not original helper execution, accepted device or SQL evaluation','fixture':fixture,'rendered_SQL_sha256':H(rendered.encode()),'remaining_placeholders':any(k in rendered for k in placeholders),'selected_column_to_field':[{'column':13,'expression':columns[13],'inner_offset':20,'outer_offset':32},{'column':14,'expression':columns[14],'inner_offset':24,'outer_offset':36}],'SQL_execution':0,'original_execution':0})
 refs=json.loads((O/'references-v1/INDEX.json').read_text())
 for name,r in refs.items():bb=(O/'references-v1'/name).read_bytes();assert H(bb)==r['sha256'];pins['reference:'+name]=r
 out['INPUTS.json']=J(pins);out['METHOD.json']=J({'host_operations':['original image byte reads','readelf/objdump','PT_LOAD mapping','explicit file-byte assertions','relocation/PIC data references','SQL SELECT-list textual split','finite plain-text replacement model'],'vendor_or_original_execution':0,'SQL_execution':0,'original_JSON_execution':0,'transport_session_auth_framing_inspected':False,'reference_scope':'Earlier selected reader source report preserved, no old output altered','counts':{'source_spans':len(spans),'file_byte_assertions':len(guards),'PIC_joins':len(pool),'GOT_chains':len(slots),'selected_relocations':len(selected),'SQL_columns':len(columns),'host_text_cases':1,'input_pins':len(pins)}})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(pathlib.Path(__file__).read_bytes()),'report_sha256':H((O/'REPORT.md').read_bytes()),'outputs':{name:{'bytes':len(bb),'sha256':H(bb)}for name,bb in out.items()}})
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args();out=build()
 if a.check:
  for name,bb in out.items():assert(O/name).read_bytes()==bb,name
  idx=json.loads((O/'initial-generated-v1/SNAPSHOT_INDEX.json').read_text())
  for name,r in idx.items():bb=(O/'initial-generated-v1'/name).read_bytes();assert bb==(O/name).read_bytes() and H(bb)==r['sha256']and len(bb)==r['bytes']
 else:
  snap=O/'initial-generated-v1';assert not snap.exists(),'refuse snapshot overwrite'
  for name in out:assert not(O/name).exists(),'refuse generated overwrite'
  copies={**out,'REPORT.md':(O/'REPORT.md').read_bytes(),pathlib.Path(__file__).name:pathlib.Path(__file__).read_bytes()};index=J({n:{'bytes':len(bb),'sha256':H(bb)}for n,bb in copies.items()})
  for name,bb in out.items():p=O/name;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(bb)
  for name,bb in copies.items():p=snap/name;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(bb)
  (snap/'SNAPSHOT_INDEX.json').open('xb').write(index)
 print(json.dumps({'check':a.check,'outputs':len(out),'original_execution':0,'SQL_execution':0}))
if __name__=='__main__':main()
