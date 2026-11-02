#!/usr/bin/env python3
"""Bounded original static runner joins; exclusive generation and read-only replay."""
import argparse, hashlib, importlib.util, json, struct, subprocess, sys
from pathlib import Path
sys.dont_write_bytecode = True
D = Path(__file__).resolve().parent
P = D.parents[2]
W = P.parents[2]
H = lambda b: hashlib.sha256(b).hexdigest()
J = lambda x: (json.dumps(x, indent=2, sort_keys=True) + '\n').encode()
HELPER = P / 'research/2026-10-31/image_vfs.py'
spec = importlib.util.spec_from_file_location('runner_image_vfs', HELPER)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
BIN = '/home/bticino/scheduling_manager/scheduling_manager'
SHA = '7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
SPANS = [
 ('constructor', 0xaf3d4, 0xaf418),
 ('initializer-prefix', 0xa72c0, 0xa7398),
 ('initializer-action-dispatch', 0xa75c8, 0xa767a),
 ('initializer-action-append', 0xa767a, 0xa7712),
 ('launch-conditional', 0xa5db0, 0xa60b0),
 ('stop-request', 0xa60b0, 0xa6200),
 ('launch-direct', 0xa6210, 0xa6508),
 ('worker-actions', 0xa6734, 0xa6d10),
 ('worker-condition-prefix', 0xa6d10, 0xa6d9e),
 ('worker-condition-tail', 0xa6e9a, 0xa7100),
]
def build():
 v = mod.ImageVFS(); b = v.read_bytes(BIN); assert H(b) == SHA
 u = lambda o: struct.unpack_from('<I', b, o)[0]
 ph = u(28); es, count = struct.unpack_from('<HH', b, 42)
 loads = []
 for i in range(count):
  t, off, va, _, fs, ms, flags, _ = struct.unpack_from('<8I', b, ph+i*es)
  if t == 1: loads.append((va, off, fs, flags))
 def at(va, n):
  for a,o,s,f in loads:
   if a <= va and va+n <= a+s: return b[o+va-a:o+va-a+n]
  raise ValueError(('unmapped original range', hex(va), n))
 word = lambda a: struct.unpack('<I', at(a,4))[0]
 out = {}; spans = []
 for name,a,z in SPANS:
  raw = at(a,z-a)
  spans.append({'name':name,'image_path':BIN,'start_va':hex(a),'end_exclusive':hex(z),'sha256':H(raw),'bytes':len(raw)})
  s = subprocess.check_output(['objdump','-d','-m','arm','-M','force-thumb','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={z}',str(v.root/BIN.lstrip('/'))],text=True)
  out[f'spans/{name}.txt'] = s.replace(str(W)+'/', '').encode()
 # Data slots in the RW mapping have a distinct VA/file offset. Relocations are retained.
 vt = [word(a) for a in range(0x161de8,0x161e10,4)]
 assert vt == [0,0x164d84,0xa5651,0xa5669,0xa6d19,0,0x164d90,0xa5689,0xa56a1,0xa6d11]
 relocs=[]
 for target, expected in [(0x161df8,0xa6d19),(0x161e0c,0xa6d11)]:
  rows=[a for a in range(0x498c,0x100d4,8) if word(a)==target and word(a+4)==23]
  assert len(rows)==1 and word(target)==expected
  relocs.append({'slot_va':hex(target),'relocation_entry_va':hex(rows[0]),'type':'R_ARM_RELATIVE','original_thumb_pointer':hex(expected),'instruction_va':hex(expected&~1)})
 pools=[]
 for name,add,pool,target in [('conditional-thread-vtable',0xa5e1a,0xa6084,0x161de8),('direct-thread-vtable',0xa627a,0xa64e4,0x161de8),('initializer-start-callback',0xa7376,0xa7f00,0xa60a9),('initializer-manager-callback',0xa737a,0xa7f04,0xa56c1)]:
  value=word(pool); assert (add+4+value)&0xffffffff==target
  pools.append({'name':name,'add_pc_va':hex(add),'pool_va':hex(pool),'pool_word':hex(value),'target':hex(target)})
 boundaries=[]; ex=[]
 for p in range(0x14bfc0,0x14f8f8,8):
  val=word(p)&0x7fffffff; val-= (1<<31) if val&(1<<30) else 0
  ex.append(((p+val)&0xfffffffe,p))
 for a in [0xa5db0,0xa6210,0xa72c0]:
  idx=next(p for target,p in ex if target==a); end=next(target for target,p in ex if target>a)
  boundaries.append({'start':hex(a),'next_exidx_start':hex(end),'index_va':hex(idx)})
 table=0xa7600; selected=struct.unpack('<H',at(table+10*2,2))[0]
 assert selected==0x18 and table+selected*2==0xa7630
 # Opcode-exact bounded locator, not all possible encodings/accesses or whole-program absence.
 hits=[]
 for a in range(0x11880,0x113fb0-3,2):
  x,y=struct.unpack('<HH',at(a,4))
  if x&0xfff0==0xf890 and y&0xfff==65: hits.append(hex(a))
 assert hits==['0x1d7e6','0x36ce6','0xa5dbc','0xa621c']
 out.update({
  'INPUTS.v1.json':J([{'path':str((v.root/BIN.lstrip('/')).relative_to(W)),'sha256':H(b),'bytes':len(b)},{'path':str(HELPER.relative_to(W)),'sha256':H(HELPER.read_bytes()),'bytes':HELPER.stat().st_size}]),
  'SOURCE_SPANS.v1.json':J(spans), 'VTABLE_RELOCATIONS.v1.json':J({'base_va':'0x161de8','words':[hex(x)for x in vt],'worker_slots':relocs}),
  'PIC_POOLS.v1.json':J(pools),'EXIDX.v1.json':J(boundaries),
  'ACTION_TABLE.v1.json':J({'table_base':hex(table),'selected_local_enum':10,'halfword':hex(selected),'branch':hex(table+2*selected),'scope':'Halfwords are data. Selected branch only; no action executed.'}),
  'ENABLED_LOCATOR.v1.json':J({'opcode':'Thumb32 LDRB immediate12=65','range':['0x11880','0x113fb0'],'hits':hits,'scope':'Locator for this one opcode form only, not an absence/full-program access claim.'}),
  'METHOD.v1.json':J({'original_execution':0,'target_processes':0,'threads':0,'timers':0,'SQL':0,'bus_or_network':0,'host_scene_fixtures':0,'method':'Original static Thumb2 disassembly, PT_LOAD mapping, relative data relocations, PIC arithmetic and exidx boundaries. Standard thread/JSON/allocation APIs remain unexecuted delegates. Nearest exported symbol labels are not function identities. Literal pools and TBH data are not instructions.','limits':'Only selected normal paths; full initializer/CFG/unwind, active provider, objects, registration/callback success, elapsed timing, concurrency and physical effects remain unproved.'})})
 return out
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); args=ap.parse_args()
 out=build(); out['OUTPUT_MANIFEST.v1.json']=J({n:{'sha256':H(b),'bytes':len(b)}for n,b in out.items()})
 if args.check:
  for n,b in out.items(): assert (D/n).read_bytes()==b,n
 else:
  assert not any((D/n).exists() for n in out),'refuse output overwrite'
  snap=D/'first-candidate'; assert not snap.exists()
  copies={**out,Path(__file__).name:Path(__file__).read_bytes()}
  for n,b in out.items(): p=D/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  for n,b in copies.items(): p=snap/n;p.parent.mkdir(parents=True,exist_ok=True);p.open('xb').write(b)
  (snap/'SNAPSHOT.json').open('xb').write(J({n:{'sha256':H(b),'bytes':len(b)}for n,b in copies.items()}))
 print(json.dumps({'check':args.check,'outputs':len(out),'original_execution':0,'source_spans':len(SPANS)}))
if __name__=='__main__': main()
