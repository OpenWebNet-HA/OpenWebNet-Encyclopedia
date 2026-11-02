#!/usr/bin/env python3
"""F461 original local field registration/packed route source, host static only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json,struct,subprocess,importlib.util,argparse,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=D.parents[1];V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f461_run04_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
FILES={'plugin':'home/bticino/libcoso/libplug_scs.so','core':'home/bticino/libcoso/libcoso.so','exe':'home/bticino/bin/coso'}
SPANS=[('plugin',0x3180,0x31b8,'init-once'),('plugin',0x31d4,0x3244,'descriptor-private-and-path'),('plugin',0x3248,0x32ec,'config-first-boolean'),('plugin',0x32ec,0x3318,'config-second-boolean'),('plugin',0x33c0,0x342c,'conditional-field-registration'),('plugin',0x342c,0x34a4,'intervening-config-return'),('core',0x2650,0x26d8,'register-field-owner'),('core',0x2cd0,0x2d6c,'message-route-constructors'),('exe',0x5640,0x56ec,'plugin-data-owner'),('exe',0x5794,0x57c8,'initializer-symbol-request'),('exe',0x5830,0x5860,'initializer-argument-call')]
GUARDS=[('plugin',0x31dc,0xf947da61),('plugin',0x3200,0xf9003035),('plugin',0x3218,0xf947d263),('plugin',0x323c,0xf9003074),('plugin',0x3278,0xf947c662),('plugin',0x3280,0x35000b02),('plugin',0x3284,0xf947ce62),('plugin',0x328c,0x35000820),('plugin',0x32d8,0x97fffbce),('plugin',0x32e4,0xb9000040),('plugin',0x3304,0x97fffbc3),('plugin',0x3310,0xb9000020),('plugin',0x33c0,0xf947d260),('plugin',0x33d8,0x97fffade),('plugin',0x3414,0xf947da60),('plugin',0x3424,0x97fffacb),('core',0x2678,0xf9400e80),('core',0x2694,0xf9000e80),('core',0x26b0,0xf9401a62),('core',0x26b4,0xf9003660),('core',0x26bc,0x9100e001),('core',0x26c4,0xd63f0040),('core',0x2cd4,0xd2800900),('core',0x2cf4,0xfd000660),('core',0x2cf8,0xb9001260),('core',0x2d40,0xb9000c01),('core',0x2d60,0xb9000c01),('exe',0x569c,0xf9000a61),('exe',0x5798,0x910143e2),('exe',0x5850,0xf9402be1),('exe',0x5858,0xf9400840),('exe',0x585c,0xd63f0020)]
def build():
 v=m.ImageVFS();B={k:v.read_bytes(p)for k,p in FILES.items()};L={};out={};env=dict(os.environ,DEBUGINFOD_URLS='')
 for k,b in B.items():
  assert b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
  ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L[k]=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(k,a,n):r=next(r for r in L[k]if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return B[k][o:o+n]
 def u(k,a):return int.from_bytes(raw(k,a,4),'little')
 def q(k,a):return int.from_bytes(raw(k,a,8),'little')
 def cs(k,a):z=bytearray();i=0
 # bounded literal reader used only on explicit noncredential names.
 def lit(k,a):
  z=bytearray()
  for i in range(128):
   c=raw(k,a+i,1)
   if c==b'\0':return z.decode()
   z+=c
  raise AssertionError('unterminated literal')
 def bl(k,a):z=u(k,a);assert z&0xfc000000==0x94000000;i=z&0x3ffffff;return a+((i-(1<<26)if i&(1<<25)else i)<<2)
 def adrp(k,a):z=u(k,a);assert z&0x9f000000==0x90000000;i=((z>>5)&0x7ffff)<<2|(z>>29&3);return(a&~4095)+((i-(1<<21)if i&(1<<20)else i)<<12)
 for k,a,w in GUARDS:assert u(k,a)==w,(k,hex(a))
 assert u('plugin',0x15190)==1 and u('plugin',0x15194)==1
 assert q('plugin',0x15270)==0x100000001 and q('plugin',0x15200)==0x200000001
 assert struct.unpack('<2I',raw('core',0x4160,8))==(1,0)
 literals={0x38b8:'scs_cmd',0x38c0:'%s/%s',0x38c8:'SCSEnable',0x38d8:'Communication Settings',0x3938:'SCSAIEnable'}
 for a,t in literals.items():assert lit('plugin',a)==t
 assert lit('exe',0x62f0)=='init_plugin'and lit('exe',0x6318)=='./'
 assert bl('plugin',0x3424)==0x1f50 and bl('plugin',0x33d8)==0x1f50
 rel={};sp=[]
 for k,p in FILES.items():
  hp=v.root/p;rel[k]=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);out[k+'-relocations.txt']=rel[k].encode();out[k+'-dynamic.txt']=subprocess.check_output(['readelf','-dW',str(hp)],env=env)
 for k,a,e,name in SPANS:
  hp=v.root/FILES[k];z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),'/'+FILES[k]);out['spans/'+name+'.txt']=z.encode();sp.append({'input':k,'VA':hex(a),'end_exclusive':hex(e),'sha256':H(raw(k,a,e-a))})
 def rr(k,a):return next(x.strip()for x in rel[k].splitlines()if x.startswith(f'{a:016x} '))
 joins=[]
 for a,name,target in [(0x14fb0,'scs_field_bus',0x15220),(0x14fa0,'scsai_field_bus',0x151b0),(0x14f88,'scs_enable',0x15190),(0x14f98,'scsai_enable',0x15194)]:
  r=rr('plugin',a);assert'R_AARCH64_GLOB_DAT'in r and name in r;assert f'{target:016x}'in r;joins.append(r)
 for a,name in [(0x15250,'scs_init'),(0x15258,'scs_send'),(0x151e0,'scs_init'),(0x151e8,'scs_send')]:r=rr('plugin',a);assert'R_AARCH64_ABS64'in r and name in r;joins.append(r)
 # Actual import PLT, not nearest printed symbol labels.
 assert adrp('plugin',0x1f50)==0x15000;z=u('plugin',0x1f54);slot=0x15000+((z>>10)&4095)*8;assert slot==0x15020 and u('plugin',0x1f5c)==0xd61f0220;r=rr('plugin',slot);assert'register_field_bus'in r;joins.append(r)
 assert bl('core',0x2d38)==0x1f10 and bl('core',0x2d58)==0x1f10
 assert adrp('core',0x1f10)==0x15000 and u('core',0x1f1c)==0xd61f0220
 z=u('core',0x1f14);assert 0x15000+((z>>10)&4095)*8==0x15068
 r=rr('core',0x15068);assert 'R_AARCH64_JUMP_SLOT'in r and 'new_message_to_scs'in r;joins.append(r)
 configs={}
 for p,allowed in [('home/bticino/cfg/coso_plugins/scs_cmd',{'SCSEnable','SCSAIEnable'}),('home/bticino/cfg/coso_cfg',{'PlugCfgDir'})]:
  b=v.read_bytes(p);section=None;rows=[]
  for i,line in enumerate(b.decode().splitlines(),1):
   t=line.strip()
   if t.startswith('[')and t.endswith(']'):section=t[1:-1]
   if '='in t:
    key,val=t.split('=',1)
    if key.strip()in allowed:rows.append({'line':i,'section':section,'key':key.strip(),'value':val.strip()})
  assert len(rows)==len(allowed);configs[p]={'sha256':H(b),'bytes':len(b),'selected':rows}
 assert configs['home/bticino/cfg/coso_plugins/scs_cmd']['selected'][0]['value']=='1'and configs['home/bticino/cfg/coso_plugins/scs_cmd']['selected'][1]['value']=='0'
 source={'originals':{k:{'image_path':'/'+p,'bytes':len(B[k]),'sha256':H(B[k]),'PT_LOAD':[list(r)for r in L[k]]}for k,p in FILES.items()},'spans':sp,'guards':[{'input':k,'VA':hex(a),'word':hex(w)}for k,a,w in GUARDS],'safe_literals':{hex(a):t for a,t in literals.items()},'relocation_joins':joins,'descriptor_routes':{'scs_field_bus':{'VA':'0x15220','route_offset80_words':[1,1]},'scsai_field_bus':{'VA':'0x151b0','route_offset80_words':[1,2]}},'base_message_route_words8':[1,0],'new_message_to_scscmd_store12':1,'new_message_to_scsai_store12':2,'message_direction_word16':2,'original_execution':0,'fixtures_models':0}
 out['SOURCE.json']=J(source);out['CONFIG_WHITELIST.json']=J(configs)
 docs=[V,D.parent/'2026-11-01-run03-translator-dispatch/REPORT.md',D.parent/'2026-11-01-run03-translator-dispatch/SOURCE.json',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']
 out['INPUTS.json']=J({'originals':source['originals'],'configs':{p:{'bytes':x['bytes'],'sha256':x['sha256']}for p,x in configs.items()},'references':{str(p.relative_to(W)):{'bytes':p.stat().st_size,'sha256':H(p.read_bytes())}for p in docs}})
 out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(sp),'guards':len(GUARDS),'originals':3,'configuration_whitelisted_values':3,'new_original_execution':0}});return out
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
print(json.dumps({'check':ck,'outputs':len(out),'spans':len(SPANS),'guards':len(GUARDS),'firstcopies':len(cp),'original_execution':0}))
