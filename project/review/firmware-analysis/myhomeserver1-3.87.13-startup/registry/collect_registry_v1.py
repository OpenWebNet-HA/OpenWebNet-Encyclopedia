#!/usr/bin/env python3
"""Static loader/container/scene-ID insertion and captured callback-context alias proof."""
import argparse,hashlib,importlib.util,json,struct,subprocess,sys
from pathlib import Path
sys.dont_write_bytecode=True
D=Path(__file__).resolve().parent;P=D.parents[2];W=P.parents[2];H=lambda z:hashlib.sha256(z).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
HELPER=P/'research/2026-10-31/image_vfs.py';sp=importlib.util.spec_from_file_location('registry_vfs',HELPER);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m)
IMAGE='/home/bticino/scheduling_manager/scheduling_manager';SHA='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
SPANS=[('startup-container-headers',0x13288,0x132b6),('startup-loader-call',0x1333a,0x1334e),('loader-input-alias',0x17630,0x17650),('loader-runner-construct',0x1786a,0x178b2),('category2-key-reassignment',0x178c4,0x178f4),('loader-insertion-call',0x17b9e,0x17bb6),('runner-constructor-forwarding',0xaf3d4,0xaf418),('initializer-context-save',0xa72c0,0xa7304),('scene-id-conversion',0x31ef0,0x31f58),('registry-insert-precheck',0xb6ea8,0xb6ff0),('registry-node-insertion',0xb71d4,0xb72b0),('category2-key-selector',0xb6480,0xb653c),('scenario-context-argument',0xabc92,0xabca0),('scenario-context-capture',0x113a88,0x113b74),('same-registry-key-reader',0xb6580,0xb65bc),('same-registry-value-reader',0xb69fc,0xb6a70)]
CALLS=[(0x1334a,0x17630),(0x178ae,0xaf3d4),(0xaf3e0,0xb57fc),(0xaf410,0xa72c0),(0x178ec,0xb6480),(0x17ba4,0xb6ea8),(0xb6f24,0xb71d4),(0xabc9c,0x113a88)]
GUARDS=[(0x17642,'0190'),(0x1764c,'0593'),(0x178a6,'019b'),(0x178aa,'059a'),(0x17ba0,'0198'),(0xaf3d8,'1546'),(0xaf3da,'1e46'),(0xaf3f0,'3246'),(0xaf3f2,'2946'),(0xa72fa,'cde90512'),(0x31f46,'6062'),(0xb6ebe,'d8f82460'),(0xb6f00,'0020'),(0xb7234,'2961'),(0xb7242,'41f98f07'),(0xb725e,'c8f81430')]
def build():
 v=m.ImageVFS();b=v.read_bytes(IMAGE);assert H(b)==SHA;po=struct.unpack_from('<I',b,28)[0];sz,n=struct.unpack_from('<HH',b,42);loads=[]
 for i in range(n):
  q=struct.unpack_from('<8I',b,po+i*sz)
  if q[0]==1:loads.append((q[2],q[1],q[4]))
 def at(a,n):
  for va,o,s in loads:
   if va<=a and a+n<=va+s:return b[o+a-va:o+a-va+n]
  raise ValueError(hex(a))
 word=lambda a:struct.unpack('<I',at(a,4))[0]
 bp=v.root/IMAGE.lstrip('/');out={};src=[]
 for name,a,e in SPANS:
  src.append({'name':name,'start_va':hex(a),'end_va_exclusive':hex(e),'bytes':e-a,'sha256':H(at(a,e-a))});out['spans/'+name+'.txt']=subprocess.check_output(['objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(bp)],text=True).replace(str(W)+'/', '').encode()
 calls=[]
 for pc,target in CALLS:
  a,z=struct.unpack('<HH',at(pc,4));assert a&0xf800==0xf000 and z&0xd000==0xd000;s=(a>>10)&1;i1=1-(((z>>13)&1)^s);i2=1-(((z>>11)&1)^s);imm=(s<<24)|(i1<<23)|(i2<<22)|((a&1023)<<12)|((z&2047)<<1);assert(pc+4+imm-((1<<25)if s else 0))&0xffffffff==target;calls.append({'call_va':hex(pc),'bytes_hex':at(pc,4).hex(),'target_va':hex(target)})
 guards=[]
 for a,h in GUARDS:assert at(a,len(bytes.fromhex(h))).hex()==h;guards.append({'va':hex(a),'bytes_hex':h})
 pools=[]
 for pool,pc in [(0x32438,0x31efa),(0x3243c,0x31f08)]:
  t=(word(pool)+pc+4)&0xffffffff;assert at(t,3)==b'id\0';pools.append({'pool_va':hex(pool),'add_pc_va':hex(pc),'target_va':hex(t),'literal':'id'})
 inputs=[]
 for p,z in [(bp,b),(HELPER,HELPER.read_bytes())]+[(P/q,(P/q).read_bytes())for q in ['research/2026-10-31-actions/scenario/REPORT.v2.md','research/2026-10-31-consumers/scheduler/REPORT.md']]:inputs.append({'path':str(p.relative_to(W)),'bytes':len(z),'sha256':H(z)})
 out.update({'INPUTS.v1.json':J(inputs),'SOURCE_SPANS.v1.json':J(src),'DIRECT_CALLS.v1.json':J(calls),'CRITICAL_BYTES.v1.json':J(guards),'PIC_KEYS.v1.json':J(pools),'ALIASES.v1.json':J({'startup_container':'entry SP+160; passed r1 to17630','loader_container':'incomingr1→loaderSP+4→af3d4r3→a72c0r2→initializerSP+24→SCENARIOconstructorr2→compiled96/capturedpairsecondword','loader_service':'incomingr2→loaderSP+20→af3d4r2→a72c0r1→initializerSP+20; distinct from captured registry','insert_receiver':'loaderSP+4→b6ea8r0; first tree rooted receiver+8','key':'sceneobject+36 loadedb6ebe→payloadword0→node+16','value':'two-word handle(pointer=160Ballocation+12,allocation/controlbase)→node+20/+24','reader_join':'SCENARIO suppliedcontext to b6580/b69fc uses same first-tree root+8/nodekey+16/value+20/+24','scope':'Original normal-return static aliases, not naturally populated/live registry, thread safety or activation.'}),'METHOD.v1.json':J({'original_execution':0,'host_models_or_scene_fixtures':0,'SQL_JSON_expressions_executed':0,'target_IO':0,'scope':'Selected loader/container/ID/first-tree insertion and captured context. Directory IO/JSON/provider/stdtree rebalance remain unexecuted delegates; no transport/session/auth/framing bodies. Category2 reassignment source kept separate from ordinary untouched ID.','history':'No generated candidate overwrite or failed first generation. Literal pools/table data are not instructions; nearest exported labels are not adopted as function identities.'})})
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');a=ap.parse_args();out=build();out['OUTPUT_MANIFEST.v1.json']=J({n:{'sha256':H(z),'bytes':len(z)}for n,z in out.items()})
 if a.check:
  for n,z in out.items():assert(D/n).read_bytes()==z,n
 else:
  assert not any((D/n).exists()for n in out),'refuse overwrite';S=D/'first-candidate';assert not S.exists();copies={**out,Path(__file__).name:Path(__file__).read_bytes()};idx=J({n:{'sha256':H(z),'bytes':len(z)}for n,z in copies.items()})
  for n,z in out.items():p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  for n,z in copies.items():p=S/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(z)
  (S/'SNAPSHOT.json').open('xb').write(idx)
 print(json.dumps({'check':a.check,'outputs':len(out),'spans':len(SPANS),'calls':len(CALLS),'byte_guards':len(GUARDS),'PIC_keys':2,'inputs':4,'original_execution':0}))
if __name__=='__main__':main()
