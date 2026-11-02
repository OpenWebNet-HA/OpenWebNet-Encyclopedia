#!/usr/bin/env python3
"""Fresh AArch64 local translation matcher/callsite source; never executes target code."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,struct,importlib.util,json,subprocess,argparse,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=D.parents[1];V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
s=importlib.util.spec_from_file_location('f461_run03_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
FILES={'exe':'home/bticino/bin/coso','core':'home/bticino/libcoso/libcoso.so','plugin':'home/bticino/libcoso/libplug_automation_tr.so'}
SPANS=[('exe',0x2f74,0x2f84,'manager-request'),('exe',0x3df0,0x3e24,'list-prologue'),('exe',0x3e54,0x3f70,'due-field-and-descriptor'),('exe',0x3f70,0x3fd8,'local-post-selection-boundary'),('exe',0x3ffc,0x4078,'criterion-to-callback'),('exe',0x4170,0x4180,'same-manager-wrapper'),('core',0x25a0,0x25c4,'manager-accessor'),('core',0x2888,0x28e4,'registered-list-owner'),('core',0x3088,0x30c4,'numeric-criterion-provenance')]
GUARDS={0x2f74:'001280d2',0x2f80:'2cffff97',0x3e08:'e23b00f9',0x3e94:'9c0240f9',0x3e98:'931340f9',0x3ef8:'1a0c40f9',0x3f14:'212b40f9',0x3f18:'3f0000eb',0x3f28:'131040f9',0x3f38:'760240f9',0x3f3c:'801340b9',0x3f40:'d7624829',0x3ffc:'215340b9',0x4000:'3f00186b',0x4008:'c02640f9',0x400c:'f803172a',0x4010:'f703012a',0x4024:'e40316aa',0x4028:'8c3340b9',0x402c:'e30315aa',0x4030:'e2031caa',0x4034:'e103172a',0x4038:'9f01006b',0x4040:'cc1e40f9',0x4044:'e003182a',0x4048:'80013fd6',0x404c:'c0000035',0x4070:'c02a40f9',0x4170:'e20300aa',0x4178:'00200291',0x417c:'1dffff17'}
def build():
 v=m.ImageVFS('normal');b={k:v.read_bytes(p)for k,p in FILES.items()};L={}
 for k,z in b.items():
  assert z[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',z,18)[0]==183
  ph=struct.unpack_from('<Q',z,32)[0];es,n=struct.unpack_from('<HH',z,54);L[k]=[struct.unpack_from('<II6Q',z,ph+i*es)for i in range(n)];L[k]=[r for r in L[k]if r[0]==1]
 def off(k,a,n):return next(r[2]+a-r[3]for r in L[k]if r[3]<=a and a+n<=r[3]+r[5])
 def raw(k,a,n):o=off(k,a,n);return b[k][o:o+n]
 def u(k,a):return int.from_bytes(raw(k,a,4),'little')
 def branch(k,a):z=u(k,a);assert z&0x7c000000==0x14000000;i=z&0x3ffffff;return a+((i-(1<<26)if i&(1<<25)else i)<<2)
 def adrp(k,a):z=u(k,a);assert z&0x9f000000==0x90000000;i=((z>>5)&0x7ffff)<<2|(z>>29)&3;return(a&~4095)+((i-(1<<21)if i&(1<<20)else i)<<12)
 for a,z in GUARDS.items():assert raw('exe',a,4).hex()==z,hex(a)
 assert branch('exe',0x2f80)==0x2c30 and branch('exe',0x417c)==0x3df0
 assert struct.unpack('<2I',raw('plugin',0x181d0,8))==(1,2)
 out={};env=dict(os.environ,DEBUGINFOD_URLS='');sp=[];rels={}
 for k,p in FILES.items():
  hp=v.root/p;rr=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);rels[k]=rr;out[k+'-relocations.txt']=rr.encode()
  out[k+'-dynamic.txt']=subprocess.check_output(['readelf','-dW',str(hp)],env=env)
 for k,a,e,name in SPANS:
  hp=v.root/FILES[k];txt=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),'/'+FILES[k]);out['spans/'+name+'.txt']=txt.encode();sp.append({'input':k,'VA':hex(a),'end_exclusive':hex(e),'file_offset':hex(off(k,a,e-a)),'bytes_sha256':H(raw(k,a,e-a))})
 # Prove executable get_plug_m PLT slot against original relocation, never trust printed labels.
 assert adrp('exe',0x2c30)==0x17000;z=u('exe',0x2c34);assert z&0xffc00000==0xf9400000 and u('exe',0x2c3c)==0xd61f0220
 slot=0x17000+((z>>10)&4095)*8;assert slot==0x171a0
 getrow=next(x.strip()for x in rels['exe'].splitlines()if x.startswith('00000000000171a0 '));assert 'R_AARCH64_JUMP_SLOT'in getrow and getrow.split()[-3]=='get_plug_m'
 for address,name in [('0000000000017fc8','automation_tr'),('00000000000181c8','automation_tr_translate')]:
  row=next(x.strip()for x in rels['plugin'].splitlines()if x.startswith(address+' '));assert name in row
 assert 'libcoso.so'in out['exe-dynamic.txt'].decode()
 prov={'inputs':[{'image_path':'/'+p,'bytes':len(b[k]),'sha256':H(b[k]),'PT_LOAD':[list(r)for r in L[k]]}for k,p in FILES.items()], 'spans':sp,'guards':{hex(a):z for a,z in GUARDS.items()},'get_plug_m_import':getrow,'get_plug_m_PLT_bytes':raw('exe',0x2c30,16).hex(),'automation_descriptor':'0x18190','automation_direction_words':{'offset64':1,'offset68':2},'actual_indirect_callback':{'load':'0x4040','call':'0x4048','slot_offset':56,'arg0':'selected origin axis W24','arg1':'selected destination axis W23','arg2':'same message X28','arg3':'SP+168 output-list address X21','arg4':'same descriptor X22'},'original_execution':0,'semantic_fixtures_or_models':0}
 out['SOURCE.json']=J(prov)
 paths=[V,D.parent/'2026-11-01-deep-routing/REPORT.v2.md',D.parent/'2026-11-01-deep-routing/SOURCE.json',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']
 out['INPUTS.json']=J({'original_inputs':prov['inputs'],'documentary_inputs':{str(p.relative_to(W)):{'bytes':p.stat().st_size,'sha256':H(p.read_bytes())}for p in paths}})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'originals':3,'spans':len(sp),'guards':len(GUARDS),'new_original_execution':0,'new_semantic_fixtures_models':0}})
 return out
p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');check=p.parse_args().check;out=build();copies={**out,'REPORT.md':(D/'REPORT.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};index=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in copies.items()});C=D/'first-candidate'
if check:
 for n,z in out.items():assert(D/n).read_bytes()==z,n
 assert(C/'INDEX.json').read_bytes()==index
 for n,z in copies.items():assert(C/n).read_bytes()==z,n
else:
 assert not C.exists()and all(not(D/n).exists()for n in out)
 for n,z in out.items():(D/n).parent.mkdir(parents=True,exist_ok=True);(D/n).open('xb').write(z)
 C.mkdir()
 for n,z in copies.items():(C/n).parent.mkdir(parents=True,exist_ok=True);(C/n).open('xb').write(z)
 (C/'INDEX.json').open('xb').write(index)
print(json.dumps({'check':check,'outputs':len(out),'spans':len(SPANS),'guards':len(GUARDS),'firstcopies':len(copies),'original_execution':0}))
