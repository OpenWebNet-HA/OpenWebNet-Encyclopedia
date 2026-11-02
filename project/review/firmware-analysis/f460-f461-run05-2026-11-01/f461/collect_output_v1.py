#!/usr/bin/env python3
"""One original typed-object translator normal form and local record construction. Static only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json,struct,subprocess,importlib.util,argparse,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=D.parents[1];V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
s=importlib.util.spec_from_file_location('f461_run05_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
FILES={'plugin':'home/bticino/libcoso/libplug_automation_tr.so','core':'home/bticino/libcoso/libcoso.so'}
SPANS=[('plugin',0x3a30,0x3a84,'argument-capture'),('plugin',0x3b60,0x3bc0,'selected-parsed-kind'),('plugin',0x4518,0x4554,'selected-command-parse'),('plugin',0x4600,0x4620,'command-one'),('plugin',0x3be8,0x3c1c,'selected-address-zero'),('plugin',0x49c0,0x4a58,'address-payload-and-helper'),('plugin',0x41b0,0x41c0,'selected-return-code'),('plugin',0x3c80,0x3cb8,'temporary-cleanup'),('plugin',0x3ab8,0x3ad8,'return-epilogue'),('core',0x3a00,0x3a84,'local-record-copy-and-list')]
G=[(0x3b64,0xd2800900),(0x3b68,0xf9402f9b),(0x3b8c,0xb9403a63),(0x3b98,0x71000c7f),(0x3ba0,0xf9400260),(0x3ba8,0xb9406803),(0x3bbc,0x54004ae0),(0x4524,0xaa0003f6),(0x4534,0xf9400860),(0x4538,0x97fff6ae),(0x453c,0xf1002c1f),(0x4548,0xf100081f),(0x4600,0xb4006a40),(0x4604,0xf100041f),(0x4618,0xaa0003fa),(0x461c,0x17fffd73),(0x3c00,0xf9401097),(0x3c14,0x97fff90b),(0x3c18,0x34006d40),(0x49d0,0x97fff514),(0x49e0,0xf9401820),(0x49e4,0xb40000a0),(0x49fc,0xaa1a03e3),(0x4a00,0xaa1603e2),(0x4a04,0xaa1703e1),(0x4a10,0x97fff504),(0x4a14,0xf90002a0),(0x4a28,0x97fff4f6),(0x4a30,0xb9400760),(0x4a38,0x54000380),(0x4a3c,0xf94033e2),(0x4a44,0x910283e0),(0x4a48,0x52800023),(0x4a50,0x97fff548),(0x41b4,0x52800017),(0x3ca4,0x34fff0b7)]
LITS={0x6038:'0',0x64e0:'B1',0x6528:'12',0x6530:'08',0x6718:'%s00',0x6740:'B',0x6750:'%s%s%s'}
def build():
 v=m.ImageVFS();B={k:v.read_bytes(p)for k,p in FILES.items()};L={};out={};env=dict(os.environ,DEBUGINFOD_URLS='')
 for k,b in B.items():
  assert b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
  ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L[k]=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(k,a,n):r=next(r for r in L[k]if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return B[k][o:o+n]
 def u(k,a):return int.from_bytes(raw(k,a,4),'little')
 def ap(k,a):z=u(k,a);assert z&0x9f000000==0x90000000;i=((z>>5)&0x7ffff)<<2|(z>>29&3);return(a&~4095)+((i-(1<<21)if i&(1<<20)else i)<<12)
 def bl(k,a):z=u(k,a);assert z&0xfc000000==0x94000000;i=z&0x3ffffff;return a+((i-(1<<26)if i&(1<<25)else i)<<2)
 def literal(a):
  z=bytearray()
  for i in range(64):
   c=raw('plugin',a+i,1)
   if c==b'\0':return z.decode()
   z+=c
  raise AssertionError('literal length bound')
 for a,z in G:assert u('plugin',a)==z,hex(a)
 for a,z in LITS.items():assert literal(a)==z
 PICS=[(0x4518,0x451c,0x6528),(0x460c,0x4610,0x6530),(0x3c08,0x3c0c,0x6038),(0x49c0,0x49c8,0x64e0),(0x49c4,0x49cc,0x6718),(0x4a08,0x4a0c,0x6750),(0x4a18,0x4a20,0x6740)]
 for pc,add,t in PICS:
  z=u('plugin',add);assert z&0xffc00000==0x91000000 and ap('plugin',pc)+((z>>10)&4095)==t
 # Exact local helper metadata/ID stores and source ranges (64-bit pointers/data).
 CG=[(0x3a04,0x52800000),(0x3a08,0x3cc08021),(0x3a10,0x3cc18020),(0x3a14,0x3c808041),(0x3a18,0xb9402c23),(0x3a1c,0x3c818040),(0x3a20,0xf9402021),(0x3a24,0xb9002c43),(0x3a28,0xf9002041),(0x3a34,0x52800065),(0x3a38,0x52800024),(0x3a50,0xb9002845),(0x3a54,0xb9003043),(0x3a58,0xb9003844),(0x3a70,0xf9000261)]
 for a,z in CG:assert u('core',a)==z,hex(a)
 rel={};sp=[]
 for k,p in FILES.items():
  hp=v.root/p;rel[k]=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);out[k+'-relocations.txt']=rel[k].encode();out[k+'-dynamic.txt']=subprocess.check_output(['readelf','-dW',str(hp)],env=env)
 for k,a,e,name in SPANS:
  hp=v.root/FILES[k];txt=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),'/'+FILES[k]);out['spans/'+name+'.txt']=txt.encode();sp.append({'input':k,'VA':hex(a),'end_exclusive':hex(e),'sha256':H(raw(k,a,e-a))})
 def rr(k,a):return next(x.strip()for x in rel[k].splitlines()if x.startswith(f'{a:016x} '))
 specs=[('plugin',0x4538,0x1ff0,0x18150,'g_ascii_strtoll'),('plugin',0x49d0,0x1e20,0x18068,'g_strdup_printf'),('plugin',0x4a10,0x1e20,0x18068,'g_strdup_printf'),('plugin',0x4a50,0x1f70,0x18110,'prepare_briefscs_frames'),('core',0x3a5c,0x1fa0,0x150b0,'prepare_scs_from_open'),('core',0x3a68,0x1f90,0x150a8,'g_list_append')];imports=[]
 for k,pc,plt,slot,name in specs:
  assert bl(k,pc)==plt;z=u(k,plt+4);assert z&0xffc00000==0xf9400000 and u(k,plt+12)==0xd61f0220;assert ap(k,plt)+((z>>10)&4095)*8==slot;r=rr(k,slot);assert'R_AARCH64_JUMP_SLOT'in r and name in r;imports.append({'object':k,'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(k,plt,16).hex(),'relocation':r})
 source={'originals':{k:{'image_path':'/'+p,'bytes':len(B[k]),'sha256':H(B[k]),'PT_LOAD':[list(r)for r in L[k]]}for k,p in FILES.items()},'spans':sp,'plugin_guards':[{'VA':hex(a),'word':hex(z)}for a,z in G],'core_guards':[{'VA':hex(a),'word':hex(z)}for a,z in CG],'safe_literals':{hex(a):z for a,z in LITS.items()},'PIC_literal_joins':[{'ADRP':hex(a),'ADD':hex(c),'target':hex(t)}for a,c,t in PICS],'import_proofs':imports,'selected_form':{'format':'%s%s%s','arguments':['B100 (source %s00 with B1)','12','08'],'derived_ASCII':'B1001208','scope':'conditional source normal form, not an executed fixture/output capture'},'record_contract':{'bytes_requested':72,'body_pointer_offset':0,'output_word40':3,'output_word48':1,'output_word56':1,'source_copied_ranges':[[8,16],[24,16],[44,4],[64,8]],'same_output_record_appended':True},'new_original_execution':0,'models_fixtures':0}
 out['SOURCE.json']=J(source)
 docs=[V,D.parent/'2026-11-01-run03-translator-dispatch/REPORT.md',D.parent/'2026-11-01-run04-field-owner/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']
 out['INPUTS.json']=J({'originals':source['originals'],'references':{str(p.relative_to(W)):{'bytes':p.stat().st_size,'sha256':H(p.read_bytes())}for p in docs}})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(sp),'plugin_guards':len(G),'core_guards':len(CG),'PIC_joins':len(PICS),'imports':len(imports),'safe_literals':len(LITS),'original_execution':0}});return out
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
