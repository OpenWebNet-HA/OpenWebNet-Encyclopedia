#!/usr/bin/env python3
"""Exclusive static F460 action-handle dispatch/marker-poll source reconstruction."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f460_action_gate_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/scheduling_manager/scheduling_manager';E='5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62'
SP=[('initializer-receiver',0xf94c0,0xf94ec),('selected-action-handle-publication',0x100010,0x100078),('pair-vector-append',0xf9480,0xf94b8),('same-local-receiver',0xf84d0,0xf8518),('action-range-dispatch',0xf86b0,0xf8710),('poll-tail-selection',0xf8818,0xf883c),('one-entry-marker-tail',0xf8a3c,0xf8a50),('false-marker-wait-and-recheck',0xf8760,0xf87c8),('normal-scene-flags-and-return',0xf89c8,0xf8a14),('entire-marker-getter',0x1303a0,0x1303ac)]
G=[(0xf94d8,0xaa0003f4),(0x100010,0xf901d3f3),(0x100014,0xf901ebf3),(0x100018,0xf901efff),(0x100034,0x910f43e2),(0x100040,0xa9028be1),(0x10004c,0xf9000833),(0x100054,0xf901d3ff),(0x100068,0xf9401be2),(0x10006c,0x91036280),(0xf9488,0xa9409001),(0xf9498,0xa9007c20),(0xf949c,0x91004020),(0xf94a4,0xa9007c5f),(0xf94a8,0xf9000424),(0xf94ac,0xf9000460),(0xf84f0,0xaa0003f6),(0xf86b0,0xa94dd6d3),(0xf86c0,0x9103e2d8),(0xf86c8,0x91004273),(0xf86d4,0xf9400260),(0xf86d8,0xf9400001),(0xf86dc,0xf9400021),(0xf86e0,0xd63f0020),(0xf86e4,0x08dfff00),(0xf86e8,0x72001c1f),(0xf86f0,0xa94dded3),(0xf86fc,0x9344fc00),(0xf8830,0xf100041f),(0xf8a3c,0xf9400260),(0xf8a44,0x72001c1f),(0xf8788,0xaa1403e1),(0xf878c,0xaa1403e0),(0xf879c,0x08dfff00),(0xf87a0,0x72001c1f),(0xf87a8,0xa94dded3),(0xf89c8,0x9103e6c0),(0xf89cc,0x089ffc1f),(0xf89d0,0x9103e2d6),(0xf89d4,0x089ffedf),(0xf8a10,0xd65f03c0),(0x1303a0,0xd503245f),(0x1303a4,0x39402000),(0x1303a8,0xd65f03c0)]
def build():
 v=m.ImageVFS();b=v.read_bytes(P);assert H(b)==E and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);p=r[2]+a-r[3];return b[p:p+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def q(a):return int.from_bytes(raw(a,8),'little')
 def bl(a,tail=False):
  x=u(a);assert x&0xfc000000==(0x14000000 if tail else 0x94000000);i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 def cond(a):
  x=u(a);assert x&0xff000010==0x54000000;i=x>>5&0x7ffff;return a+((i-0x80000 if i&0x40000 else i)<<2)
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 for a,w in G:assert u(a)==w,(hex(a),hex(u(a)),hex(w))
 out={};ss=[];hp=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='')
 for name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=z.encode();ss.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(a,e-a).hex(),'sha256':H(raw(a,e-a))})
 rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(s.strip()for s in rels.splitlines()if s.startswith(f'{a:016x} '))
 calls=[]
 for a,t in[(0x100058,0xf7040),(0x100060,0x40630),(0x100074,0xf9480),(0xf8a40,0x1303a0)]:assert bl(a)==t;calls.append({'VA':hex(a),'target':hex(t),'bytes':raw(a,4).hex()})
 assert bl(0xf94b4,True)==0x10f2c0 and bl(0xf8a4c,True)==0xf8760
 bs=[]
 for a,t in[(0xf86b8,0xf883c),(0xf86d0,0xf86f0),(0xf86ec,0xf86c8),(0xf8834,0xf8a3c),(0xf8a48,0xf8838),(0xf8764,0xf8838),(0xf8798,0xf8778),(0xf87a4,0xf8838),(0xf94b4-36,0xf94b4)]:
  assert cond(a)==t;bs.append({'VA':hex(a),'target':hex(t),'word':hex(u(a))})
 imports=[]
 for pc,plt,slot,name in[(0x100028,0x24300,0x21e7f0,'_Znwm@GLIBCXX_3.4'),(0xf8778,0x245a0,0x21e940,'__errno_location@GLIBC_2.17'),(0xf8790,0x24140,0x21e710,'nanosleep@GLIBC_2.17')]:
  assert bl(pc)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot;r=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(plt,16).hex(),'relocation':r})
 assert q(0x21cc50)==0x1301e0;primary={'slot':'0x21cc50','target':'0x1301e0','relocation':rr(0x21cc50)};assert'R_AARCH64_RELATIVE'in primary['relocation']
 pins={P:{'bytes':len(b),'sha256':H(b),'resolved':v.resolve(P)}}
 for p in[V,O/'research/2026-11-01-run07-receiver/REPORT.md',O/'research/2026-11-01-run03-sleep-invoker/REPORT.md',O/'research/2026-11-01-deep-scheduler/REPORT.md',W/'work/f460-f461-comparison/2026-11-01-run07/reviews/f460-source-review.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image':P,'sha256':E,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'local_calls':calls,'conditional_branches':bs,'imports':imports,'inherited_selected_primary':primary,'new_source_contract':{'scene_action_range':[216,224,232],'entry_bytes':16,'dispatch':'first pointer primary slot0; scene248 acquireload after normal call return','single_entry_poll':'original1303a0 reads action byte8; low8 tested','scene_flags_normal_cleanup':'release zero at249 then248','action_marker_is_not_scene_flags':True,'growth_delegate':'0x10f2c0 opaque','publication_control_helpers':['0xf7040','0x40630'],'new_original_execution':0,'models_fixtures':0}})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'imports':len(imports),'local_calls':len(calls),'branches':len(bs),'inputs':len(pins),'original_execution':0}});return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');ck=p.parse_args().check;o=build();C=D/'first-candidate';cp={**o,'REPORT.md':(D/'REPORT.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in cp.items()})
 if ck:
  for n,z in o.items():assert(D/n).read_bytes()==z,n
  assert(C/'INDEX.json').read_bytes()==ix
  for n,z in cp.items():assert(C/n).read_bytes()==z,n
 else:
  assert not C.exists()and all(not(D/n).exists()for n in o)
  for n,z in o.items():(D/n).parent.mkdir(parents=True,exist_ok=True);(D/n).open('xb').write(z)
  C.mkdir()
  for n,z in cp.items():(C/n).parent.mkdir(parents=True,exist_ok=True);(C/n).open('xb').write(z)
  (C/'INDEX.json').open('xb').write(ix)
 print(json.dumps({'check':ck,'outputs':len(o),'spans':len(SP),'guards':len(G),'original_execution':0}))
if __name__=='__main__':main()
