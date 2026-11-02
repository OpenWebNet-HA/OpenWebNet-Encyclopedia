#!/usr/bin/env python3
"""Pure HAL compile-time identity branches only; caller bodies explicitly excluded."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json,struct,subprocess,importlib.util,argparse,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=D.parents[1];V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f461_identity_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
FILES={'HAL':'/usr/lib/liblghal.so.1','device':'/home/bticino/bin/bt_device'}
SPANS=[(0xcc20,0xcc70,'code-board-prefix'),(0xce20,0xce34,'code-selected-literal-output'),(0xcd1c,0xcd4c,'code-normal-epilogue'),(0xe440,0xe4a0,'codename-board-prefix'),(0xe604,0xe618,'codename-selected-literal-output'),(0xe558,0xe58c,'codename-normal-epilogue')]
G=[(0xcc3c,0xaa0003f4),(0xcc4c,0x97fff521),(0xcc50,0x121d7801),(0xcc54,0x7100403f),(0xcc58,0x540005a0),(0xcc5c,0x71004c1f),(0xcc60,0x7a5a1804),(0xcc64,0x54000d40),(0xcc68,0x7100581f),(0xcc6c,0x54000da0),(0xce20,0xb0000100),(0xce24,0x91074000),(0xce28,0x97fff476),(0xce2c,0xf9000280),(0xce30,0x17ffffbb),(0xe464,0xaa0003f5),(0xe474,0x97ffef17),(0xe47c,0x121d7801),(0xe484,0x7100403f),(0xe48c,0x540005e0),(0xe490,0x71004c1f),(0xe494,0x54000ae0),(0xe498,0x7100581f),(0xe49c,0x54000b40),(0xe604,0xf00000e0),(0xe608,0x910de000),(0xe60c,0x97ffee7d),(0xe610,0xf90002a0),(0xe614,0x17ffffd1)]
def build():
 v=m.ImageVFS();B={k:v.read_bytes(p)for k,p in FILES.items()};L={};out={};env=dict(os.environ,DEBUGINFOD_URLS='');ident={}
 for k,b in B.items():
  assert b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
  ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L[k]=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1];ident[k]={'requested_image_path':FILES[k],'resolved_image_path':v.resolve(FILES[k]),'bytes':len(b),'sha256':H(b),'PT_LOAD':[list(r)for r in L[k]]}
 def raw(k,a,n):r=next(r for r in L[k]if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return B[k][o:o+n]
 def u(k,a):return int.from_bytes(raw(k,a,4),'little')
 def ap(k,a):z=u(k,a);assert z&0x9f000000==0x90000000;i=((z>>5)&0x7ffff)<<2|(z>>29&3);return(a&~4095)+((i-(1<<21)if i&(1<<20)else i)<<12)
 def bl(k,a):z=u(k,a);assert z&0xfc000000==0x94000000;i=z&0x3ffffff;return a+((i-(1<<26)if i&(1<<25)else i)<<2)
 for a,z in G:assert u('HAL',a)==z,hex(a)
 assert raw('HAL',0x2d378,5)==b'F461\0'and raw('HAL',0x2d1d0,4)==b'134\0'
 assert ap('HAL',0xe604)+((u('HAL',0xe608)>>10)&4095)==0x2d378
 assert ap('HAL',0xce20)+((u('HAL',0xce24)>>10)&4095)==0x2d1d0
 hp=v.root/v.resolve(FILES['HAL']).lstrip('/');rel=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);sym=subprocess.check_output(['readelf','-Ws',str(hp)],text=True,env=env);dyn=subprocess.check_output(['readelf','-dW',str(hp)],text=True,env=env)
 defs=[]
 for name,address in [('hal_get_codename',0xe440),('hal_get_code',0xcc20),('hal_board',0x251b0)]:
  rows=[x.strip()for x in sym.splitlines()if x.split()and x.split()[-1]==name];assert len(rows)==1 and int(rows[0].split()[1],16)==address;defs+=rows
 assert'Library soname: [liblghal.so.1]'in dyn
 imports=[]
 for pc,plt,slot,name in [(0xe474,0xa0d0,0x4b8c0,'hal_board'),(0xcc4c,0xa0d0,0x4b8c0,'hal_board'),(0xe60c,0xa000,0x4b858,'strdup@GLIBC_2.17'),(0xce28,0xa000,0x4b858,'strdup@GLIBC_2.17')]:
  assert bl('HAL',pc)==plt;z=u('HAL',plt+4);assert z&0xffc00000==0xf9400000 and u('HAL',plt+12)==0xd61f0220 and ap('HAL',plt)+((z>>10)&4095)*8==slot;r=next(x.strip()for x in rel.splitlines()if x.startswith(f'{slot:016x} '));assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw('HAL',plt,16).hex(),'relocation':r})
 dpath=v.root/v.resolve(FILES['device']).lstrip('/');dr=subprocess.check_output(['readelf','-rW',str(dpath)],text=True,env=env);dd=subprocess.check_output(['readelf','-dW',str(dpath)],text=True,env=env);assert'Shared library: [liblghal.so.1]'in dd
 declarations=[]
 for slot,name in [(0x3cd40,'hal_get_codename'),(0x3c688,'hal_get_code')]:r=next(x.strip()for x in dr.splitlines()if x.startswith(f'{slot:016x} '));assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;declarations.append(r)
 out['SELECTED_METADATA.json']=J({'HAL_definitions':defs,'HAL_SONAME':[x.strip()for x in dyn.splitlines()if'SONAME'in x],'device_NEEDED_HAL':[x.strip()for x in dd.splitlines()if'Shared library: [liblghal.so.1]'in x],'device_import_declarations_only':declarations,'scope':'No device caller or transport/auth/framing body included; imports do not establish effective binding or natural invocation.'})
 sp=[]
 for a,e,name in SPANS:
  text=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),v.resolve(FILES['HAL']));out['spans/'+name+'.txt']=text.encode();sp.append({'VA':hex(a),'end_exclusive':hex(e),'sha256':H(raw('HAL',a,e-a))})
 alias={p:t for p,t in v.links.items()if p in ['usr/lib/liblghal.so.1','usr/lib/liblghal.so']};assert'usr/lib/liblghal.so.1'in alias
 source={'originals':ident,'image_alias_metadata':alias,'spans':sp,'guards':[{'VA':hex(a),'word':hex(z)}for a,z in G],'import_proofs':imports,'safe_compiled_literals':{'0x2d378':'F461','0x2d1d0':'134'},'selected_contract':{'opaque_board_result':22,'codename_output_pointer':'originalX0 savedX21; requeststrdupF461thenstore[X21]','code_output_pointer':'originalX0 savedX20; requeststrdup134thenstore[X20]','function_integer_return_status':'not established','scope':'Conditional puregetter compiletimebranches, not installed/hardware identity or a demonstrated permitted caller'},'new_original_execution':0,'models_fixtures':0}
 out['SOURCE.json']=J(source)
 refs=[V,O/'analysis/normal-symlinks.json',D.parent/'2026-11-01/REPORT.v2.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']
 out['INPUTS.json']=J({'originals':ident,'references':{str(p.relative_to(W)):{'bytes':p.stat().st_size,'sha256':H(p.read_bytes())}for p in refs}})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(sp),'guards':len(G),'getter_import_proofs':len(imports),'original_execution':0}});return out
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
print(json.dumps({'check':ck,'outputs':len(out),'spans':len(SPANS),'guards':len(G),'firstcopies':len(cp),'original_execution':0}))
