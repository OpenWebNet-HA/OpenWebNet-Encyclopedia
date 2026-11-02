#!/usr/bin/env python3
"""F461 static logging-selection collector; no original code or service execution."""
import sys,struct,hashlib,json,importlib.util,subprocess,re
from pathlib import Path
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'work/f461-firmware').is_dir())
VFS=ROOT/'work/f461-firmware/2.0.11/research/2026-11-01/image_vfs.py'
s=importlib.util.spec_from_file_location('image_vfs_run08',VFS);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
H=lambda b:hashlib.sha256(b).hexdigest()
def ident(p,b):return {'path':p,'size':len(b),'sha256':H(b)}
def build():
 inputs=[];D={};cfg=[]
 for kind in ['normal','recovery']:
  f=v.ImageVFS(kind);d=f.read_bytes('/home/bticino/bin/bt_daemon');D[kind]=d;inputs.append(ident(kind+':/home/bticino/bin/bt_daemon',d))
  for p in ['/home/bticino/cfg/stack_open.xml','/home/bticino/cfg/stack_open_reduced.xml']:
   b=f.read_bytes(p);inputs.append(ident(kind+':'+p,b));lines=[{'line':i,'text':line.strip()} for i,line in enumerate(b.decode().splitlines(),1) if re.fullmatch(r'\s*<logrotation>[01]</logrotation>\s*',line)]
   cfg.append({'image':kind,'path':p,'selected_lines':lines});assert lines==[{'line':62,'text':'<logrotation>1</logrotation>'}]
 d=D['normal'];assert H(d)=='b1a3f99cb78c97cd0aa98616c8074f56c8fd34fb10d2500138ea74ed5ed54c4e';assert d==D['recovery']
 ph=struct.unpack_from('<Q',d,32)[0];es,n=struct.unpack_from('<HH',d,54);loads=[struct.unpack_from('<II6Q',d,ph+i*es) for i in range(n) if struct.unpack_from('<I',d,ph+i*es)[0]==1]
 def off(a,n=4):
  for p in loads:
   if p[3]<=a and a+n<=p[3]+p[5]:return p[2]+a-p[3]
  raise AssertionError(hex(a))
 def u(a):return struct.unpack_from('<I',d,off(a))[0]
 def adrp(a):
  w=u(a);assert w&0x9f000000==0x90000000;i=(w>>5&0x7ffff)<<2|(w>>29&3);i=i-(1<<21) if i&(1<<20) else i;return (a&~4095)+(i<<12)
 def ptr(a,b):
  w=u(b);assert w&0xffc00000==0x91000000;assert u(a)&31==w>>5&31;return adrp(a)+(w>>10&4095)
 literals=[]
 for a,b,t,text in [(0x1348c,0x13490,0x1d4e8,'/home/bticino/cfg/extra/70'),(0x1797c,0x17980,0x1ee88,'logrotation'),(0x195c0,0x195c4,0x1ee88,'logrotation'),(0x17c14,0x17c18,0x1bd70,'0'),(0x17c44,0x17c48,0x1e298,'')]:
  assert ptr(a,b)==t;b0=text.encode()+b'\0';assert d[off(t,len(b0)):off(t,len(b0))+len(b0)]==b0;literals.append({'adrp':hex(a),'add':hex(b),'literal_va':hex(t),'value':text})
 guards={0x13464:0x7100041f,0x13468:0x54000281,0x13470:0x3945a281,0x1347c:0x34000361,0x134a4:0x340002c0,0x134a8:0x52803fe1,0x17988:0x34001460,0x17c24:0x35000100,0x17c28:0x3905a27f,0x17c54:0x34fffea0,0x17c58:0x52800020,0x17c5c:0x3905a260,0x19118:0x3905a27f,0x195dc:0x350068c0,0x1a308:0x7100001f,0x1a30c:0x1a9f07e0,0x1a310:0x3905a300,0x62c0:0xaa1303e0}
 for a,w in guards.items():assert u(a)==w,(hex(a),hex(u(a)))
 calls={0x13450:('get_mystatus_extras_status',0x57d0),0x13460:('strtol',0x5ac0),0x134a0:('stat',0x4eb0),0x134b0:('mkdir',0x5490),0x134b4:('hal_restart_SysLog',0x4fc0),0x134fc:('hal_stop_SysLog_service',0x5740),0x13504:('_ZN6logger13load_old_logsEv',0x5210),0x13508:('hal_restart_SysLog',0x4fc0),0x1a304:('g_key_file_get_integer',0x5190)}
 binary=ROOT/'work/f461-firmware/2.0.11/analysis/rootfs/home/bticino/bin/bt_daemon'
 rel=subprocess.run(['readelf','-rW',str(binary)],capture_output=True,text=True,check=True).stdout
 bindings=[]
 for a,(name,t) in calls.items():
  w=u(a);assert w&0xfc000000==0x94000000;i=w&0x3ffffff;i=i-(1<<26) if i&(1<<25) else i;assert a+i*4==t
  l=u(t+4);assert l&0xffc00000==0xf9400000;slot=adrp(t)+(l>>10&4095)*8
  rs=[z for z in rel.splitlines() if z.split() and int(z.split()[0],16)==slot];assert len(rs)==1 and name in rs[0] and 'JUMP_SLOT' in rs[0]
  bindings.append({'call':hex(a),'plt':hex(t),'got_slot':hex(slot),'symbol':name,'relocation':rs[0].strip()})
 for a,t in [(0x62c4,0x133f0),(0x63bc,0x133f0),(0x1359c,0x133f0)]:
  w=u(a);i=w&0x3ffffff;i=i-(1<<26) if i&(1<<25) else i;assert w>>26==0x25 and a+i*4==t
 spans=[('logging-selection',0x133f0,0x13514),('xml-key',0x17978,0x1798c),('xml-boolean',0x17c14,0x17c60),('default-byte',0x190ec,0x1911c),('keyfile-key',0x195bc,0x195e0),('keyfile-boolean',0x1a2f4,0x1a318),('startup-call',0x62b8,0x62c8),('local-caller',0x13594,0x135a0)]
 out={};raw=[]
 for name,a,b in spans:
  z=d[off(a,b-a):off(a,b-a)+b-a];out['spans/'+name+'.bin']=z;raw.append({'name':name,'va_start':hex(a),'va_end_exclusive':hex(b),'file_offset':hex(off(a)),'sha256':H(z),'size':len(z)})
 out['INPUTS.json']=J({'inputs':inputs,'accessor':ident(str(VFS.relative_to(ROOT)),VFS.read_bytes())})
 out['EVIDENCE.json']=J({'scope':'static original byte/dataflow checks only; no original execution','normal_recovery_daemon_identical':True,'loads':[list(p) for p in loads],'spans':raw,'guards':{hex(a):hex(w) for a,w in guards.items()},'literals':literals,'import_requests':bindings,'direct_local_callers':['0x62c4','0x63bc','0x1359c'],'configuration_lines':cfg,'execution':{'original_instructions':0,'service_calls':0,'target_file_calls':0,'models':0}})
 out['output-manifest.json']=J({'files':{p:{'sha256':H(b),'size':len(b)} for p,b in out.items()},'report':ident('REPORT.md',(HERE/'REPORT.md').read_bytes()),'collector':ident(Path(__file__).name,Path(__file__).read_bytes())})
 return out
out=build()
if '--check' in sys.argv:
 for p,b in out.items():assert (HERE/p).read_bytes()==b,p
 print(json.dumps({'check':'PASS','outputs':len(out),'spans':8,'word_guards':18,'literal_joins':5,'import_call_proofs':9,'inputs':6,'original_instructions':0}));sys.exit()
for p in out:assert not (HERE/p).exists(),p
assert not (HERE/'first-candidate').exists()
for p,b in out.items():q=HERE/p;q.parent.mkdir(parents=True,exist_ok=True);q.open('xb').write(b)
copies={**out,'REPORT.md':(HERE/'REPORT.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};idx=J({'files':{p:{'sha256':H(b),'size':len(b)} for p,b in copies.items()}})
for p,b in copies.items():q=HERE/'first-candidate'/p;q.parent.mkdir(parents=True,exist_ok=True);q.open('xb').write(b)
(HERE/'first-candidate/INDEX.json').open('xb').write(idx)
print(json.dumps({'generated':len(out),'first_copies':len(copies),'original_instructions':0}))
