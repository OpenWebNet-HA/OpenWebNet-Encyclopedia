#!/usr/bin/env python3
"""Exclusive static F461 HAL platform-selector provenance; no target code or I/O."""
import sys
sys.dont_write_bytecode=True
import hashlib,json,struct,importlib.util,subprocess,re,os
from pathlib import Path
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=W/'work/f461-firmware/2.0.11';V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
s=importlib.util.spec_from_file_location('run09_vfs',V);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
P='/usr/lib/liblghal.so.1.0.0'
SP=[('cache-prefix-and-return',0x251b0,0x25228),('cpuinfo-read-and-marker-gate',0x25228,0x252b0),('classification-prefix-and-cache-store',0x252b0,0x25358),('device-tree-fallback-only',0x25358,0x253a0),('selected-label-path',0x253e0,0x255e0),('fallback-open-failure-bridge',0x253fc,0x25420),('pure-getter-call-only',0xe440,0xe478)]
GUARDS={0x251d4:0xb94022b3,0x251e4:0xa900ffff,0x251e8:0x3100067f,0x251ec:0x540001e0,0x2520c:0x2a1303e0,0x25224:0xd65f03c0,0x25248:0xb4000da0,0x2526c:0xb5000100,0x2527c:0x52800142,0x25284:0xb100041f,0x25288:0x54fffec1,0x25294:0xf94007f4,0x25298:0xb4000674,0x252ac:0xb4000560,0x252c8:0xb90022b3,0x252d8:0x17ffffc6,0x25360:0xf90007ff,0x25378:0xb4000100,0x25384:0x52800142,0x2539c:0xb5fff8b4,0x255d4:0xb4000060,0x255d8:0x528002d3,0x255dc:0x17ffff3b}
def build():
 f=v.ImageVFS('normal');r=v.ImageVFS('recovery');b=f.read_bytes(P);br=r.read_bytes(P);assert b==br and b[:6]==b'\x7fELF\x02\x01' and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[q for i in range(n)if(q:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  q=next(q for q in L if q[3]<=a and a+n<=q[3]+q[5]);o=q[2]+a-q[3];return b[o:o+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5&0x7ffff)<<2)|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def pair(a,c):
  x=u(c);assert x&0xffc00000==0x91000000 and (u(a)&31)==(x>>5&31);return ap(a)+(x>>10&4095)
 def bl(a):
  x=u(a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 for a,x in GUARDS.items():assert u(a)==x,(hex(a),hex(u(a)))
 assert ap(0x251d0)+(u(0x251d4)>>10&4095)*4==0x4c020
 assert raw(0x4c020,4)==b'\xff'*4
 lit=[]
 for a,c,t,expected in [(0x25228,0x2522c,0x2d950,'/proc/cpuinfo'),(0x25238,0x2523c,0x2d948,'r'),(0x2524c,0x25250,0x2d988,'Hardware'),(0x25368,0x2536c,0x33370,'/sys/firmware/devicetree/base/model'),(0x255c4,0x255c8,0x33460,'BEAR')]:
  assert pair(a,c)==t and raw(t,len(expected)+1)==expected.encode()+b'\0';lit.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'literal':expected})
 hp=f.root/f.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);symbols=subprocess.check_output(['readelf','-Ws',str(hp)],text=True,env=env)
 imports=[]
 for pc,plt,name in [(0x25240,0xa900,'fopen@GLIBC_2.17'),(0x25268,0xacf0,'strcasestr@GLIBC_2.17'),(0x25280,0xa7e0,'__getdelim@GLIBC_2.17'),(0x25290,0x9e40,'fclose@GLIBC_2.17'),(0x252d0,0x9fc0,'free@GLIBC_2.17'),(0x25370,0xa900,'fopen@GLIBC_2.17'),(0x2538c,0xa7e0,'__getdelim@GLIBC_2.17'),(0x25394,0x9e40,'fclose@GLIBC_2.17'),(0x255d0,0xacf0,'strcasestr@GLIBC_2.17'),(0xe474,0xa0d0,'hal_board')]:
  assert bl(pc)==plt;x=u(plt+4);assert x&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220;slot=ap(plt)+(x>>10&4095)*8
  rr=[z.strip()for z in rels.splitlines()if re.match(r'^[0-9a-fA-F]+\s',z)and int(z.split()[0],16)==slot];assert len(rr)==1 and 'JUMP_SLOT'in rr[0] and rr[0].split()[-3]==name
  imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'name':name,'relocation':rr[0]})
 defs=[z.strip()for z in symbols.splitlines()if re.search(r'\bhal_board$',z)];assert defs and all('00000000000251b0'in z and '1316 FUNC'in z for z in defs)
 out={};spans=[]
 for name,a,e in SP:
  z=raw(a,e-a);text=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P)
  out['spans/'+name+'.txt']=text.encode();spans.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':z.hex(),'sha256':H(z)})
 inputs={}
 for name,z in [('normal:'+P,b),('recovery:'+P,br)]:inputs[name]={'size':len(z),'sha256':H(z)}
 for p in [V,O/'research/2026-11-01-run07-identity/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']:
  z=p.read_bytes();inputs[str(p.relative_to(W))]={'size':len(z),'sha256':H(z)}
 out['INPUTS.json']=J(inputs)
 out['SOURCE.json']=J({'image_path':P,'sha256':H(b),'normal_recovery_bytes_equal':True,'PT_LOAD':[list(q)for q in L],'symbol':defs,'spans':spans,'guards':{hex(a):hex(x)for a,x in GUARDS.items()},'literal_joins':lit,'imports':imports,'cache':{'VA':'0x4c020','width_bytes':4,'initial_file_bytes_hex':'ffffffff','selected_store':'0x252c8','selected_match_numeric22':'0x255d8','meaning':'local cached selector only, not hardware/model ID'},'excluded_boundary':{'start':'0x253a0','reason':'later command-based fallback; body and command literal not exported or interpreted'},'inherited_getter_scope':'run07 pure getter branch22 only, no uncertain bt_device consumer','execution':{'original':0,'models':0,'target_IO':0,'provider':0}})
 out['OUTPUT_MANIFEST.json']=J({'outputs':{p:{'size':len(z),'sha256':H(z)}for p,z in out.items()},'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes())})
 return out
out=build();cp={**out,'REPORT.md':(D/'REPORT.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({'files':{p:{'size':len(z),'sha256':H(z)}for p,z in cp.items()}});C=D/'first-candidate'
if '--check'in sys.argv:
 for p,z in out.items():assert(D/p).read_bytes()==z,p
 for p,z in cp.items():assert(C/p).read_bytes()==z,p
 assert(C/'INDEX.json').read_bytes()==ix
else:
 assert not C.exists() and all(not(D/p).exists()for p in out)
 for p,z in out.items():q=D/p;q.parent.mkdir(parents=True,exist_ok=True);q.open('xb').write(z)
 for p,z in cp.items():q=C/p;q.parent.mkdir(parents=True,exist_ok=True);q.open('xb').write(z)
 (C/'INDEX.json').open('xb').write(ix)
print(json.dumps({'check':'--check'in sys.argv,'outputs':len(out),'spans':len(SP),'guards':len(GUARDS),'literals':5,'imports':10,'input_pins':len(json.loads(out['INPUTS.json'])),'first_copies':len(cp),'original_execution':0}))
