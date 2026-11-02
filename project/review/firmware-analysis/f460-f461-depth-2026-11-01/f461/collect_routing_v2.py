#!/usr/bin/env python3
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,hashlib,struct,subprocess,importlib.util
D=Path(__file__).resolve().parent;W=D.parents[4];V=D.parent/'2026-11-01/image_vfs.py'
s=importlib.util.spec_from_file_location('f461_source_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);v=m.ImageVFS('normal')
H=lambda b:hashlib.sha256(b).hexdigest()
J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
files={'plugin':'home/bticino/libcoso/libplug_automation_tr.so','core':'home/bticino/libcoso/libcoso.so'}
data={k:v.read_bytes(p) for k,p in files.items()}
def segments(b):
 off=struct.unpack_from('<Q',b,32)[0];n=struct.unpack_from('<H',b,56)[0];sz=struct.unpack_from('<H',b,54)[0];return [struct.unpack_from('<II6Q',b,off+i*sz) for i in range(n) if struct.unpack_from('<I',b,off+i*sz)[0]==1]
def at(k,va,n):
 b=data[k]
 for r in segments(b):
  if r[3]<=va and va+n<=r[3]+r[5]:return b[r[2]+va-r[3]:r[2]+va-r[3]+n]
 raise ValueError('unmapped VA')
spans=[('plugin',0x2150,0x21ac),('plugin',0x21f8,0x22ac),('plugin',0x38b0,0x3930),('plugin',0x3a30,0x3b64),('plugin',0x3b8c,0x3bd0),('plugin',0x3cb8,0x3d64),('core',0x2870,0x28f4)]
guards={0x2200:'97ffff60',0x221c:'f9002c79',0x2264:'528000c4',0x2268:'52800043',0x2278:'b9000a84',0x2280:'b9002a83',0x22a8:'97fffeba',0x3a8c:'7100075f',0x3a94:'71000b5f',0x3aec:'71000b7f',0x3b44:'7100077f',0x3cf4:'b9403a63',0x3cf8:'7100047f',0x3d04:'71002c7f',0x3d0c:'71000c7f',0x3d10:'7a491864'}
for a,w in guards.items():assert struct.unpack('<I',at('plugin',a,4))[0]==int(w,16),(hex(a),w)
assert struct.unpack('<6I',at('plugin',0x18190,24))==(0,1,0,1,1,68)
outs={};inputs=[]
for k,p in files.items():
 backing=v.root/p
 assert data[k][4]==2 and struct.unpack_from('<H',data[k],18)[0]==183
 inputs.append({'image_path':'/'+p,'bytes':len(data[k]),'sha256':H(data[k]),'PT_LOAD':[list(r) for r in segments(data[k])]})
 for kind,args in [('dynamic',['-dW']),('relocations',['-rW']),('symbols',['-Ws'])]:
  raw=subprocess.check_output(['readelf',*args,str(backing)]).decode();outs[f'{k}-{kind}.txt']=raw.replace(str(W)+'/','').encode()
for i,(k,a,z) in enumerate(spans):
 txt=subprocess.check_output(['objdump','-d','-m','aarch64',f'--start-address={a}',f'--stop-address={z}',str(v.root/files[k])]).decode().replace(str(W)+'/','')
 outs[f'span-{i+1}.txt']=txt.encode()
r=outs['plugin-relocations.txt'].decode();assert '0000000000017fc8' in r and 'automation_tr + 0' in r
assert '00000000000181c0' in r and 'automation_tr_init + 0' in r
assert '00000000000181c8' in r and 'automation_tr_translate + 0' in r
outs['SOURCE.json']=J({'inputs':inputs,'guards':{hex(a):w for a,w in guards.items()},'descriptor_VA':'0x18190','descriptor_bytes':at('plugin',0x18190,104).hex(),'span_count':len(spans),'original_execution':0,'semantic_fixtures':0,'scope':'Fresh AArch64 descriptor/registration/admission and byte-slice delegation, no transport/runtime/public semantics.'})
outs['INPUTS.json']=J(inputs+[{'path':str(V.relative_to(W)),'bytes':V.stat().st_size,'sha256':H(V.read_bytes())},{'path':'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md','sha256':H((W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md').read_bytes())}])
report=D/'REPORT.v2.md';assert report.exists();outs['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H(report.read_bytes()),'outputs':{n:{'bytes':len(b),'sha256':H(b)} for n,b in outs.items()}})
if '--check' in sys.argv:
 for n,b in outs.items():assert (D/n).read_bytes()==b,n
else:
 assert not any((D/n).exists() for n in outs)
 for n,b in outs.items():
  with (D/n).open('xb') as f:f.write(b)
 snap=D/'first-candidate';snap.mkdir();copies={**outs,'REPORT.v2.md':report.read_bytes(),'collect_routing_v2.py':Path(__file__).read_bytes()};index={n:{'bytes':len(b),'sha256':H(b)} for n,b in copies.items()}
 for n,b in copies.items():
  with (snap/n).open('xb') as f:f.write(b)
 with (snap/'INDEX.json').open('xb') as f:f.write(J(index))
print(json.dumps({'check':'--check' in sys.argv,'outputs':len(outs),'spans':len(spans),'guards':len(guards),'original_execution':0}))
