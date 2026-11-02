#!/usr/bin/env python3
"""Original address shape helper and one local prefix-normalizer consumer; static only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json,struct,subprocess,importlib.util,argparse,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=D.parents[1];V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f461_run06_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
FILES={'helper':'/home/bticino/lib/libautomation.so.1','plugin':'/home/bticino/libcoso/libplug_automation_tr.so'}
SPANS=[('helper',0x1c10,0x1d28,'shape-classifier'),('plugin',0x400c,0x404c,'parsed-pointer-and-local-string'),('plugin',0x40c0,0x40e8,'actual-helper-caller'),('plugin',0x43c4,0x4404,'class-four-prefix-and-length'),('plugin',0x568c,0x56c4,'two-byte-conversion-and-append')]
G={'helper':[(0x1c44,0x97fffd03),(0x1c4c,0x350001c0),(0x1c94,0x97fffcd3),(0x1c9c,0x34fffda0),(0x1cac,0x97fffce9),(0x1cb0,0x34000200),(0x1cc0,0x97fffce4),(0x1cc4,0x34000160),(0x1cd0,0x97fffcd8),(0x1cd4,0xf100041f),(0x1cdc,0xd1000800),(0x1ce0,0x52800082),(0x1ce4,0xf27ef81f),(0x1ce8,0x5a9f0042),(0x1c6c,0x2a0203e0)],'plugin':[(0x4028,0xf940103b),(0x40c0,0xaa1b03e0),(0x40c4,0x97fff7c7),(0x40cc,0x71000c1f),(0x40d0,0x54006460),(0x40d4,0x5400178c),(0x43c4,0x7100101f),(0x43cc,0x54ffeb61),(0x43f0,0xf100081f),(0x43f8,0x540094a0),(0x568c,0x39400360),(0x5690,0x97fff21c),(0x5698,0x39400760),(0x56a0,0x97fff218),(0x56a4,0x2a0003e3),(0x56a8,0x2a1b03e2),(0x56ac,0xaa1803e0),(0x56b8,0x97fff252),(0x56c0,0x17fffb51)]}
LITS={'helper':{0x21a8:'0',0x21e0:'#',0x21e8:'00',0x21f0:'100'},'plugin':{0x5fe8:'D1',0x6030:'%d%d'}}
def build():
 v=m.ImageVFS();B={k:v.read_bytes(p)for k,p in FILES.items()};L={};out={};env=dict(os.environ,DEBUGINFOD_URLS='');originals={}
 for k,b in B.items():
  assert b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
  ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L[k]=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1];originals[k]={'requested_image_path':FILES[k],'resolved_image_path':v.resolve(FILES[k]),'bytes':len(b),'sha256':H(b),'PT_LOAD':[list(r)for r in L[k]]}
 def raw(k,a,n):r=next(r for r in L[k]if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return B[k][o:o+n]
 def u(k,a):return int.from_bytes(raw(k,a,4),'little')
 def ap(k,a):z=u(k,a);assert z&0x9f000000==0x90000000;i=((z>>5)&0x7ffff)<<2|(z>>29&3);return(a&~4095)+((i-(1<<21)if i&(1<<20)else i)<<12)
 def bl(k,a):z=u(k,a);assert z&0xfc000000==0x94000000;i=z&0x3ffffff;return a+((i-(1<<26)if i&(1<<25)else i)<<2)
 def literal(k,a):
  z=bytearray()
  for i in range(64):
   c=raw(k,a+i,1)
   if c==b'\0':return z.decode()
   z+=c
  raise AssertionError('literal bound')
 for k,rows in G.items():
  for a,z in rows:assert u(k,a)==z,(k,hex(a))
 for k,rows in LITS.items():
  for a,z in rows.items():assert literal(k,a)==z
 pics=[('helper',0x1c1c,0x1c20,0x21a8),('helper',0x1c8c,0x1c90,0x21e0),('helper',0x1ca0,0x1ca4,0x21e8),('helper',0x1cb4,0x1cb8,0x21f0),('plugin',0x43d4,0x43d8,0x5fe8),('plugin',0x56b0,0x56b4,0x6030)]
 for k,a,c,t in pics:assert u(k,c)&0xffc00000==0x91000000 and ap(k,a)+((u(k,c)>>10)&4095)==t
 rel={};sp=[]
 for k,p in FILES.items():
  hp=v.root/v.resolve(p).lstrip('/');rel[k]=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);out[k+'-relocations.txt']=rel[k].encode();out[k+'-dynamic.txt']=subprocess.check_output(['readelf','-dW',str(hp)],env=env);out[k+'-symbols.txt']=subprocess.check_output(['readelf','-Ws',str(hp)],env=env)
 assert'Shared library: [libautomation.so.1]'in out['plugin-dynamic.txt'].decode()
 rows=[x for x in out['helper-symbols.txt'].decode().splitlines()if x.split()and x.split()[-1]=='automation_get_where_type'];assert len(rows)==1 and int(rows[0].split()[1],16)==0x1c10;definition=rows[0]
 for k,a,e,name in SPANS:
  hp=v.root/v.resolve(FILES[k]).lstrip('/');txt=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),v.resolve(FILES[k]));out['spans/'+name+'.txt']=txt.encode();sp.append({'input':k,'VA':hex(a),'end_exclusive':hex(e),'sha256':H(raw(k,a,e-a))})
 def rr(k,a):return next(x.strip()for x in rel[k].splitlines()if x.startswith(f'{a:016x} '))
 specs=[('plugin',0x43e0,0x1e90,0x180a0,'g_string_printf'),('plugin',0x43ec,0x1f10,0x180e0,'g_utf8_strlen'),('plugin',0x40c4,0x1fe0,0x18148,'automation_get_where_type'),('plugin',0x5690,0x1f00,0x180d8,'g_ascii_digit_value'),('plugin',0x56a0,0x1f00,0x180d8,'g_ascii_digit_value'),('plugin',0x56b8,0x2000,0x18158,'g_string_append_printf'),('helper',0x1c44,0x1050,0x12f30,'g_strcmp0'),('helper',0x1c94,0xfe0,0x12ef8,'g_ascii_strncasecmp'),('helper',0x1cd0,0x1030,0x12f20,'g_utf8_strlen')];imports=[]
 for k,pc,plt,slot,name in specs:
  assert bl(k,pc)==plt;z=u(k,plt+4);assert z&0xffc00000==0xf9400000 and u(k,plt+12)==0xd61f0220 and ap(k,plt)+((z>>10)&4095)*8==slot;r=rr(k,slot);assert'R_AARCH64_JUMP_SLOT'in r and name in r;imports.append({'object':k,'BL':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(k,plt,16).hex(),'relocation':r})
 links={p:t for p,t in v.links.items()if p in ['home/bticino/lib/libautomation.so.1','home/bticino/lib/libautomation.so']};assert 'home/bticino/lib/libautomation.so.1'in links
 source={'originals':originals,'image_alias_metadata':links,'spans':sp,'guards':{k:[{'VA':hex(a),'word':hex(z)}for a,z in rows]for k,rows in G.items()},'safe_literals':{k:{hex(a):t for a,t in rows.items()}for k,rows in LITS.items()},'PIC_joins':[{'object':k,'ADRP':hex(a),'ADD':hex(c),'target':hex(t)}for k,a,c,t in pics],'import_proofs':imports,'helper_definition':definition,'prefix_contract':'selected class4 and repeatedlength2 →GStringD1+append%d%d with g_ascii_digit_value byte0,byte1; suffix/output unclosed','new_original_execution':0,'semantic_fixtures_models':0}
 out['SOURCE.json']=J(source)
 docs=[V,O/'analysis/normal-symlinks.json',D.parent/'2026-11-01-run05-translator-output/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']
 out['INPUTS.json']=J({'originals':originals,'references':{str(p.relative_to(W)):{'bytes':p.stat().st_size,'sha256':H(p.read_bytes())}for p in docs}})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(sp),'helper_guards':len(G['helper']),'plugin_guards':len(G['plugin']),'PIC_joins':len(pics),'imports':len(imports),'original_execution':0}});return out
p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');ck=p.parse_args().check;out=build();cp={**out,'REPORT.md':(D/'REPORT.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in cp.items()});C=D/'first-candidate'
if ck:
 for n,z in out.items():assert(D/n).read_bytes()==z,n
 assert(C/'INDEX.json').read_bytes()==ix
 for n,z in cp.items():assert(C/n).read_bytes()==z,n
else:
 assert not C.exists()and all(not(D/n).exists()for n in out)
 for n,z in out.items():(D/n).parent.mkdir(parents=True,exist_ok=True);(D/n).open('xb').write(z)
 C.mkdir()
 for n,z in cp.items():(C/n).parent.mkdir(parents=True,exist_ok=True);(C/n).open('xb').write(z)
 (C/'INDEX.json').open('xb').write(ix)
print(json.dumps({'check':ck,'outputs':len(out),'spans':len(SPANS),'firstcopies':len(cp),'original_execution':0}))
