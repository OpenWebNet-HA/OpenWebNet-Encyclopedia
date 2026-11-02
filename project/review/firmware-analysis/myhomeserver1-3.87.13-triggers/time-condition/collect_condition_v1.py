#!/usr/bin/env python3
"""Static TIME condition dataflow. Host arithmetic only; exclusive first writes."""
import sys
sys.dont_write_bytecode=True
import pathlib,struct,hashlib,json,subprocess,re,os,argparse,importlib.util
O=pathlib.Path(__file__).resolve().parent;W=next(x for x in O.parents if(x/'sources').is_dir());R=W/'work/myhomeserver1-firmware/3.87.13/research/2026-10-31'
sp=importlib.util.spec_from_file_location('vfs',R/'image_vfs.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
H=lambda x:hashlib.sha256(x).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
S='/home/bticino/scheduling_manager/scheduling_manager';L='/usr/lib/libstdc++.so.6.0.29';C='/lib/libc.so.6'
def build():
 v=m.ImageVFS();out={};bb={};segs={};pins={};env=dict(os.environ,DEBUGINFOD_URLS='')
 for p in [S,L,C]:
  b=v.read_bytes(p);bb[p]=b;pins[p]={'sha256':H(b),'bytes':len(b),'resolved_image_path':v.resolve(p)};ph=struct.unpack_from('<I',b,28)[0];sz,n=struct.unpack_from('<HH',b,42);segs[p]=[struct.unpack_from('<8I',b,ph+i*sz)for i in range(n)]
 assert H(bb[S])=='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
 for p,label in [(R/'image_vfs.py','accessor'),(R.parents[1]/'analysis/normal-regular-files.json','regular_metadata'),(R.parents[1]/'analysis/normal-symlinks.json','symlink_metadata')]:b=p.read_bytes();pins[label]={'sha256':H(b),'bytes':len(b)}
 def off(a,n=1,p=S):return next(o+a-va for t,o,va,_,fs,*_ in segs[p]if t==1 and va<=a and a+n<=va+fs)
 def raw(a,n,p=S):return bb[p][off(a,n,p):off(a,n,p)+n]
 def word(a):return struct.unpack('<I',raw(a,4))[0]
 def txt(a):
  i=off(a);e=bb[S].index(0,i);assert e-i<512;return bb[S][i:e].decode()
 spans=[(S,'raw-factory-discriminator',0x2fa4c,0x2fb3a),(S,'raw-time-allocation',0x3038e,0x30424),(S,'raw-factory-pools',0x306a0,0x3073c),(S,'base-enabled-enum',0x2b7d0,0x2b8de),(S,'base-pools',0x2ba20,0x2ba4c),(S,'raw-time-constructor',0x2c1b8,0x2c310),(S,'time-serializer',0x246a4,0x24808),(S,'compiled-condition-dispatch',0xa74e4,0xa7544),(S,'compiled-time-allocation',0xa7d86,0xa7de4),(S,'compiled-time-constructor',0xb7c94,0xb7f10),(S,'boundary-helper',0xb7f10,0xb86a4),(S,'time-predicate',0xb86a4,0xb87b8),(L,'candidate-system-clock-now',0x959a0,0x959cc)]
 source=[]
 for p,n,a,z in spans:
  host=v.root/v.resolve(p).lstrip('/');s=subprocess.check_output(['objdump','-d','--dwarf=no-follow-links','-M','force-thumb',f'--start-address={a}',f'--stop-address={z}',str(host)],text=True,env=env).replace(str(host),p);s=re.sub(r' <([^>]+)>',lambda q:q[0]if'@plt'in q[1]else'',s);out['spans/'+n+'.txt']=s.encode();source.append({'path':p,'name':n,'start_VA':hex(a),'end_VA_exclusive':hex(z),'file_offset':hex(off(a,z-a,p)),'raw_sha256':H(raw(a,z-a,p))})
 guards=[(0x2fb02,[0x3c01]),(0x2fb0a,[0xe8df,0xf014]),(0x2c222,[0x2c06]),(0x2c278,[0x2407]),(0x2c250,[0x65ac]),(0xb7d42,[0xf884,0x3084]),(0xb7de6,[0xf8c4,0x10c0]),(0xb86ba,[0xf890,0x3084]),(0xb86be,[0xb96b]),(0xb86c0,[0x2001]),(0xb86f2,[0x6980]),(0xb873e,[0xf002,0x021f]),(0xb8748,[0xd0bb]),(0xb8778,[0xd0a2]),(0xb8786,[0x4297]),(0xb878c,[0x419d]),(0xb8790,[0x2000]),(0xb80e8,[0x6093]),(0xb80ee,[0xf942,0x078f]),(0xb8106,[0xfb80,0x0303])]
 for a,hs in guards:assert raw(a,len(hs)*2)==struct.pack('<'+'H'*len(hs),*hs),hex(a)
 joins=[]
 def pic(pool,pc,want,text=None):
  a=(word(pool)+pc+4)&0xffffffff;assert a==want
  if text is not None:assert txt(a)==text
  joins.append({'pool_VA':hex(pool),'pool_word':hex(word(pool)),'ADD_PC_VA':hex(pc),'target_VA':hex(a),'literal':text});return a
 pic(0x2ba30,0x2b7fe,0x1143e0,'enabled');pic(0x2ba40,0x2b8a0,0x115f5c,'type')
 for pool,pc,a,t in [(0x2c2f4,0x2c1e0,0x11526c,'from'),(0x2c2f8,0x2c1f8,0x115274,'to'),(0x2c2fc,0x2c210,0x115264,'days'),(0x247f8,0x246d2,0x11526c,'from'),(0x247fc,0x246f2,0x115274,'to'),(0x24800,0x24782,0x115264,'days'),(0xb865c,0xb7f78,0x1357d4,'Fri Apr 16 '),(0xb8660,0xb7f9e,0x1357e0,':00 2021'),(0xb8680,0xb8202,0x1357bc,'%a %b %d %H:%M:%S %Y')]:pic(pool,pc,a,t)
 pic(0xb87ac,0xb86f4,0x1674f8);pic(0xb7efc,0xb7dd4,0x161e38)
 assert word(0x1605b8)==4 and txt(word(0x1605bc))=='TIME'
 assert struct.unpack('<H',raw(0x2fb0e,2))[0]==0x440 and 0x2fb0e+2*0x440==0x3038e
 assert struct.unpack('<H',raw(0xa7518,2))[0]==0x438 and 0xa7516+2*0x438==0xa7d86
 got=(0x2c1ca+4+word(0x2c2ec))&0xffffffff;assert got==0x1659a4;assert word(got+word(0x2c2f0))==0x160148
 tables=[]
 for name,h,rtname,methods in [('TimeCondition',0x160148,'13TimeCondition',[0x246a5,0x22649]),('TimeConditionRunner',0x161e38,'19TimeConditionRunner',[0xb8861,0xb87bd,0xb86a5])]:
  rt=word(h+4);assert txt(word(rt+4))==rtname;actual=[word(h+8+4*i)for i in range(len(methods))];assert actual==methods;tables.append({'name':name,'header_VA':hex(h),'address_point':hex(h+8),'RTTI_VA':hex(rt),'RTTI_name':rtname,'methods_Thumb':[hex(x)for x in actual]})
 host=v.root/v.resolve(S).lstrip('/');rel=subprocess.check_output(['readelf','-rW',str(host)],text=True,env=env);rels=[]
 for a in [0x160150,0x161e40,0x161e44,0x161e48,0x161e54]:
  line=next(s for s in rel.splitlines()if s.startswith(f'{a:08x} '));assert 'R_ARM_RELATIVE'in line;rels.append(line.strip())
 decl={}
 for p in [S,L,C]:
  host=v.root/v.resolve(p).lstrip('/');sy=subprocess.check_output(['readelf','--dyn-syms','-W',str(host)],text=True,env=env);dyn=subprocess.check_output(['readelf','-dW',str(host)],text=True,env=env);decl[p]={'DT_NEEDED':re.findall(r'\(NEEDED\).*?\[(.*?)\]',dyn),'selected_symbols':[s.strip()for s in sy.splitlines()if any(t in s for t in ['system_clock3now',' localtime@',' time@',' mktime@','clock_gettime@'])]}
 out['ORIGINAL_SOURCE.json']=J({'spans':source,'halfword_assertions':[{'VA':hex(a),'halfwords':[hex(x)for x in hs]}for a,hs in guards],'PIC_joins':joins,'vtables':tables,'selected_relocations':rels,'condition_factory':{'table_VA':'0x1605b0','local_index':1,'text':'TIME','decremented_TBH_index':0,'raw_branch':'0x3038e','compiled_branch':'0xa7d86'},'weekday_map':'0x1674f8','weekday_map_initialization':'not examined; no weekday-to-bit orientation claim'})
 out['PROVIDER_DECLARATIONS.json']=J({'objects':decl,'boundary':'Candidate definitions/direct requests only; effective binding and API success/timezone/locale not observed.'})
 out['FIELDS_AND_FLOW.json']=J({'raw':{'enabled_byte':28,'local_enum_word':32,'from_string':40,'to_string':64,'days_mask':88,'size_at_factory':92,'serializer':'0x246a4'},'compiled':{'size_at_call':200,'enabled_byte':132,'local_enum_word':136,'from_string':144,'to_string':168,'days_mask':192,'scene_range_base':116,'predicate':'0xb86a4'},'days_parse':{'selected_prefix_length':'min(string_length,7)','empty_mask':0,'binary_order':'selected prefix first character is highest bit of selected prefix','invalid_selected_character':'requests invalid_argument throw','serializer':'exactly7characters from bit6 to bit0'},'predicate':{'enabled_zero':1,'enabled_nonzero':['time/localtime','returned word24→map key; mapped value20 masked31→bit','day bit clear→0','two independent boundary helper calls','system_clock now','boundaries equal→1','otherwise signed64 from<now AND now<to'],'missing_map_key':'out_of_range throw request','scope':'Method result only; generic worker inversion/conjunction/admission not investigated.'},'boundary_helper':{'entry':'0xb7f10','parse_text':"Fri Apr 16 <supplied boundary>:00 2021",'format':'%a %b %d %H:%M:%S %Y','date_preservation':'copies parsed first3 words into current localtime object; remaining date/DST words not copied from parsed temporary','normal_conversion':'mktime then signed32 result times1000000000→64bit return object','failure_boundary':'stream fail flags flow through clear then same conversion if clear returns; sentry-false also reaches conversion; no separate successful-parse Boolean branch before conversion. No malformed-string outcome or provider exception prediction.'},'unclosed':['weekday map initializer/orientation','complete JsonCpp/time_get accepted grammar or locale','effective providers and ordinary target tm layout/API success','timezone/DST and midnight races across separate time samples','mktime/time/localtime failure policy beyond local source','natural scene activation and generic worker policy','runtime elapsed/physical device behavior'],'original_execution':0})
 def mask(s):
  prefix=s[:7]
  if any(c not in '01'for c in prefix):return {'delegate':'invalid_argument request'}
  return {'mask':int(prefix,2)if prefix else 0}
 # Pure source-shaped decisions with synthetic integer ticks, never clock calls.
 cases=[]
 for enabled,day,f,t,n in [(0,False,10,20,15),(1,False,10,20,15),(1,True,10,10,999),(1,True,10,20,10),(1,True,10,20,11),(1,True,10,20,20),(1,True,20,10,15)]:cases.append({'synthetic':{'enabled':enabled,'day_bit':day,'from':f,'to':t,'now':n},'return':1 if not enabled else int(day and(f==t or(f<n<t))),'scope':'pure selected branch model; not time parsing, actual date, accepted scene or execution'})
 out['HOST_MODELS.json']=J({'predicate_cases':cases,'days_prefix_cases':[{'synthetic_string':s,'result':mask(s)}for s in ['', '1','1000000','10000001','0000000X','01X']],'original_execution':0,'clock_calls':0})
 out['INPUTS.json']=J(pins);out['METHOD.json']=J({'method':'Original ImageVFS bytes; ELF32 PT_LOAD/Thumb2/PIC/GOT/RTTI/relative relocations and readelf direct declarations; finite host integers only','original_target_or_vendor_execution':0,'native_emulation':0,'target_API_calls':0,'SQL_JSON_expression_execution':0,'no_transport_auth_session_framing':True})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(pathlib.Path(__file__).read_bytes()),'report_sha256':H((O/'REPORT.md').read_bytes()),'outputs':{n:{'sha256':H(b),'bytes':len(b)}for n,b in out.items()},'counts':{'spans':len(spans),'halfword_guards':len(guards),'PIC':len(joins),'vtables':len(tables),'relocations':len(rels),'inputs':len(pins),'predicate_host_cases':len(cases),'days_host_cases':6,'original_execution':0}})
 return out

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');check=ap.parse_args().check;o=build()
 if check:
  for n,b in o.items():assert(O/n).read_bytes()==b,n
  ix=json.loads((O/'first-candidate/INDEX.json').read_text())
  for n,r in ix.items():b=(O/'first-candidate'/n).read_bytes();assert b==(O/n).read_bytes()and H(b)==r['sha256']and len(b)==r['bytes']
 else:
  d=O/'first-candidate';assert not d.exists(),'refuse first snapshot overwrite'
  for n in o:assert not(O/n).exists(),'refuse generated overwrite'
  copies={**o,'REPORT.md':(O/'REPORT.md').read_bytes(),pathlib.Path(__file__).name:pathlib.Path(__file__).read_bytes()};ix=J({n:{'sha256':H(b),'bytes':len(b)}for n,b in copies.items()})
  for n,b in o.items():p=O/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  for n,b in copies.items():p=d/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  (d/'INDEX.json').open('xb').write(ix)
 print(json.dumps({'check':check,'outputs':len(o),'original_execution':0}))
if __name__=='__main__':main()
