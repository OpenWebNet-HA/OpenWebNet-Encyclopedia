#!/usr/bin/env python3
"""Exclusive static F461 main configuration/directory selection; no target execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import struct,json,hashlib,importlib.util,subprocess,re,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=W/'work/f461-firmware/2.0.11';V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode();s=importlib.util.spec_from_file_location('select_vfs',V);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
P='/home/bticino/bin/coso'
SP=[('manager-and-option-destinations',0x2f68,0x301c),('selected-main-config-file-gate',0x3058,0x3064),('selected-main-file-load',0x30a8,0x30c4),('directory-presence-tests',0x3118,0x3128),('default-main-config-path',0x3468,0x347c),('library-and-config-key-readers',0x3738,0x3780),('directory-main-handoff',0x32cc,0x3300),('parent-directory-fallback',0x3568,0x35a0),('plugin-data-copy-and-fallback',0x5640,0x56ec)]
G={0x2f68:0xb00000b3,0x2f6c:0x910c4273,0x2f7c:0xaa0003f4,0x2f8c:0x9101c3eb,0x2f9c:0x910203e7,0x2fac:0x910283e2,0x2fb4:0xf9000e6b,0x2fcc:0xf9006e67,0x2fe8:0xf9011662,0x3018:0x34002640,0x3058:0xf94043e0,0x305c:0xb4002060,0x30b0:0xf94043e1,0x30b4:0xd2800003,0x30b8:0x52800002,0x30c0:0x34002220,0x3118:0xf9403be0,0x311c:0xb4003200,0x3120:0xf94053e0,0x3124:0xb40030a0,0x3474:0xf90043e0,0x3754:0xf90053e0,0x3778:0xf9003be0,0x3244:0xf94053e3,0x3248:0xb4001903,0x3588:0xf90053e1,0x32d4:0xf9403be1,0x32dc:0xf94053e2,0x32e4:0x91004280,0x32ec:0xaa1403e0,0x32f4:0xaa1403e0,0x5668:0xf9000280,0x567c:0xf9000660,0x569c:0xf9000a61,0x56d8:0xf9000a61}
def build():
 f=v.ImageVFS();b=f.read_bytes(P);assert H(b)=='2fb47ebfb8e63df22053a5ca95b08183a11ab93b248dcbc2b2d7a5f682561197'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return b[o:o+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5&0x7ffff)<<2)|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def bl(a):
  x=u(a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 for a,x in G.items():assert u(a)==x,(hex(a),hex(u(a)))
 assert ap(0x2f68)+(u(0x2f6c)>>10&4095)==0x17310
 hp=f.root/f.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):
  z=[z.strip()for z in rels.splitlines()if re.match(r'^[0-9a-fA-F]+\s',z)and int(z.split()[0],16)==a];assert len(z)==1;return z[0]
 def cs(a,cap=96):
  z=bytearray()
  for i in range(cap):
   c=raw(a+i,1)
   if c==b'\0':return z.decode()
   z+=c
  raise AssertionError('literalcap')
 rows=[]
 for row,expected,short,slot,store in [(0,'dirname','d',112,0x2fb4),(4,'configfile','c',128,0x2fcc),(11,'path_to_plug_cfg_dir','p',160,0x2fe8)]:
  a=0x17310+48*row;ptr,ch,flags,arg=struct.unpack('<Qb3xII',raw(a,20));assert cs(ptr)==expected and ch==ord(short)and flags==0 and arg==1;rel=rr(a);assert'RELATIVE'in rel and int(rel.split()[-1],16)==ptr;rows.append({'row':row,'entry_VA':hex(a),'long_option':expected,'short_option':short,'flags':flags,'argument_kind_word':arg,'arg_data_store':hex(store),'stack_destination':slot,'name_relocation':rel,'bytes_hex':raw(a,48).hex()})
 lit=[]
 for a,c,t,text in [(0x3468,0x346c,0x59e8,'cfg/coso_cfg'),(0x3740,0x3748,0x5a88,'Plugins settings'),(0x373c,0x3744,0x5aa0,'PlugCfgDir'),(0x3760,0x3768,0x5a80,'LibDir'),(0x56ac,0x56b0,0x6318,'./')]:
  x=u(c);assert x&0xffc00000==0x91000000 and ap(a)+(x>>10&4095)==t and cs(t)==text;lit.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'value':text})
 imports=[]
 for pc,plt,name in [(0x3000,0x2ac0,'g_option_context_add_main_entries'),(0x3014,0x2ba0,'g_option_context_parse'),(0x30bc,0x2cc0,'g_key_file_load_from_file'),(0x3750,0x29a0,'g_key_file_get_string'),(0x3774,0x29a0,'g_key_file_get_string'),(0x3470,0x2a20,'g_strdup'),(0x356c,0x2e30,'g_file_new_for_path'),(0x3574,0x2a40,'g_file_get_parent'),(0x357c,0x2d90,'g_file_get_path'),(0x5678,0x2a20,'g_strdup'),(0x568c,0x2a20,'g_strdup')]:
  assert bl(pc)==plt;x=u(plt+4);assert x&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220;slot=ap(plt)+(x>>10&4095)*8;z=rr(slot);assert'JUMP_SLOT'in z and z.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'relocation':z})
 calls=[]
 for a,t in [(0x32e8,0x5640),(0x32f0,0x58a0),(0x32f8,0x56f0)]:assert bl(a)==t;calls.append({'call':hex(a),'target':hex(t)})
 out={};sp=[]
 for name,a,e in SP:
  z=raw(a,e-a);t=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=t.encode();sp.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':z.hex(),'sha256':H(z)})
 cfgpath='/home/bticino/cfg/coso_cfg';cb=f.read_bytes(cfgpath);allowed={17:'[Plugins settings]',18:'LibDir=/home/bticino/libcoso',19:'PlugCfgDir=/home/bticino/cfg/coso_plugins'};lines=cb.decode().splitlines();assert all(lines[i-1]==t for i,t in allowed.items())
 cfg={'path':cfgpath,'size':len(cb),'sha256':H(cb),'selected_lines':[{'line':i,'text':t}for i,t in allowed.items()],'scope':'packaged normal image values; not runtime selected configuration'}
 pins={P:{'size':len(b),'sha256':H(b)},cfgpath:{'size':len(cb),'sha256':H(cb)}}
 for p in [V,O/'research/2026-11-01-run04-field-owner/REPORT.md',O/'research/2026-11-01-run04-field-owner/SOURCE.json',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'size':len(z),'sha256':H(z)}
 out['INPUTS.json']=J(pins);out['SOURCE.json']=J({'image':P,'sha256':H(b),'PT_LOAD':[list(q)for q in L],'spans':sp,'guards':{hex(a):hex(x)for a,x in G.items()},'selected_option_rows':rows,'literal_joins':lit,'imports':imports,'local_calls':calls,'configuration_whitelist':cfg,'selection_contract':{'configfile_slot':128,'libdir_slot':112,'plugcfgdir_slot':160,'default_relative_file':'cfg/coso_cfg','successful_file_read_key':'Plugins settings/PlugCfgDir only when slot160null','remaining_null_fallback':'GFile parent(selected configuration filename)→path','main_handoff':'init_plugin_data(&M[16],slot112,slot160); register_plugins(M)','inner_copy':'P24 atM16; LibDir copiedP8; PlugCfgDir copiedP16','module_and_provider_outcome':'unobserved; inherited run04 selected init_plugin request only'},'execution':{'original':0,'provider':0,'models':0,'target_IO':0}})
 out['OUTPUT_MANIFEST.json']=J({'outputs':{p:{'size':len(z),'sha256':H(z)}for p,z in out.items()},'report_sha256':H((D/'REPORT.md').read_bytes()),'collector_sha256':H(Path(__file__).read_bytes())});return out
out=build();cp={**out,'REPORT.md':(D/'REPORT.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({'files':{p:{'size':len(z),'sha256':H(z)}for p,z in cp.items()}});C=D/'first-candidate'
if '--check'in sys.argv:
 for p,z in out.items():assert(D/p).read_bytes()==z,p
 for p,z in cp.items():assert(C/p).read_bytes()==z,p
 assert(C/'INDEX.json').read_bytes()==ix
else:
 assert not C.exists()and all(not(D/p).exists()for p in out)
 for p,z in out.items():q=D/p;q.parent.mkdir(parents=True,exist_ok=True);q.open('xb').write(z)
 for p,z in cp.items():q=C/p;q.parent.mkdir(parents=True,exist_ok=True);q.open('xb').write(z)
 (C/'INDEX.json').open('xb').write(ix)
print(json.dumps({'check':'--check'in sys.argv,'outputs':len(out),'spans':len(SP),'guards':len(G),'option_rows':3,'literal_joins':5,'import_proofs':11,'local_calls':3,'pins':len(json.loads(out['INPUTS.json'])),'first_copies':len(cp),'original_execution':0}))
