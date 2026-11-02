#!/usr/bin/env python3
"""Static SLEEP inline data/timing-loop/provider/common-marker contract, no execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f460_sleep_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
FILES={'scheduler':'/home/bticino/scheduling_manager/scheduling_manager','libc':'/lib/libc.so.6'}
EXPECTED={'scheduler':'5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62','libc':'e918bb2e904dae5cec4a203741a4379bad4ed05199b69dacd87d7a7a83d01e09'}
SPANS=[('scheduler','manager',0x1125f0,0x11263c),('scheduler','invoker-prefix',0x112640,0x112680),('scheduler','prewait-boundary',0x112828,0x112880),('scheduler','timing-loop-and-return',0x112880,0x1128ec),('scheduler','callable-storage',0x1303f0,0x1304b8),('scheduler','common-inline-marker',0x1301e0,0x130270),('scheduler','marker-accessors',0x1303a0,0x1303bc),('scheduler','inherited-constructor-binding',0x112b34,0x112b68),('libc','nanosleep-wrapper',0xb97c0,0xb9808),('libc','errno-location',0x2b700,0x2b718)]
GUARDS=[('scheduler',0x112630,0xb9400021),('scheduler',0x112634,0xb9000001),('scheduler',0x11265c,0xb9400013),('scheduler',0x112664,0xaa0003f4),('scheduler',0x112880,0xb9400280),('scheduler',0x112884,0xb40001a0),('scheduler',0x11288c,0xa900ffe0),('scheduler',0x11289c,0x7100101f),('scheduler',0x1128a4,0xaa1303e1),('scheduler',0x1128a8,0xaa1303e0),('scheduler',0x1128b0,0x3100041f),('scheduler',0x1128e8,0xd65f03c0),('scheduler',0x130410,0xf9400823),('scheduler',0x13043c,0x52800042),('scheduler',0x130440,0xd63f0060),('scheduler',0x130450,0x3c828261),('scheduler',0x130464,0xa9018660),('scheduler',0x130200,0xb9400c00),('scheduler',0x130210,0x3900227f),('scheduler',0x130218,0xf9401661),('scheduler',0x13021c,0x91006260),('scheduler',0x130224,0xf9400c01),('scheduler',0x130228,0xd63f0020),('scheduler',0x13022c,0xb9401260),('scheduler',0x130238,0x39002260),('scheduler',0x130258,0x52800020),('scheduler',0x1303a4,0x39402000),('scheduler',0x1303b4,0x39002001),('libc',0xb97c8,0xaa0003e2),('libc',0xb97d0,0xaa0103e3),('libc',0xb97d4,0x52800000),('libc',0xb97d8,0x52800001),('libc',0xb97fc,0xb8216840),('libc',0xb9800,0x12800000),('libc',0x2b710,0x8b000020)]
def build():
 v=m.ImageVFS();data={k:v.read_bytes(p)for k,p in FILES.items()};loads={};out={};pins={};env=dict(os.environ,DEBUGINFOD_URLS='')
 for k,b in data.items():
  assert H(b)==EXPECTED[k]and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
  ph=struct.unpack_from('<Q',b,32)[0];sz,n=struct.unpack_from('<HH',b,54);loads[k]=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*sz))[0]==1];pins[FILES[k]]={'resolved':v.resolve(FILES[k]),'bytes':len(b),'sha256':H(b)}
 def raw(k,a,n):
  r=next(r for r in loads[k]if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return data[k][o:o+n]
 def u(k,a):return int.from_bytes(raw(k,a,4),'little')
 def q(k,a):return int.from_bytes(raw(k,a,8),'little')
 def adrp(k,a):
  x=u(k,a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def bl(k,a):
  x=u(k,a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 spans=[]
 for k,name,a,e in SPANS:
  hp=v.root/v.resolve(FILES[k]).lstrip('/');z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),FILES[k]);assert'out of bounds'not in z
  out['spans/'+name+'.txt']=z.encode();spans.append({'object':k,'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'sha256':H(raw(k,a,e-a))})
 for k,a,w in GUARDS:assert u(k,a)==w,(k,hex(a))
 rel={};sym={}
 for k in FILES:
  hp=v.root/v.resolve(FILES[k]).lstrip('/');rel[k]=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);sym[k]=subprocess.check_output(['readelf','-sW',str(hp)],text=True,env=env)
 def rr(k,a):return next(s.strip()for s in rel[k].splitlines()if s.startswith(f'{a:016x} '))
 imports=[]
 for pc,plt,slot,name in[(0x1128ac,0x24140,0x21e710,'nanosleep@GLIBC_2.17'),(0x112894,0x245a0,0x21e940,'__errno_location@GLIBC_2.17')]:
  assert bl('scheduler',pc)==plt;z=u('scheduler',plt+4);assert z&0xffc00000==0xf9400000 and u('scheduler',plt+12)==0xd61f0220;assert adrp('scheduler',plt)+((z>>10)&4095)*8==slot;r=rr('scheduler',slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name
  imports.append({'call':hex(pc),'call_bytes':raw('scheduler',pc,4).hex(),'PLT':hex(plt),'PLT_bytes':raw('scheduler',plt,16).hex(),'slot':hex(slot),'relocation':r})
 assert bl('libc',0xb97dc)==0xb47a0
 definitions=[]
 for n,a in[('nanosleep@@GLIBC_2.17',0xb97c0),('__errno_location@@GLIBC_2.17',0x2b700),('clock_nanosleep@@GLIBC_2.17',0xb47a0)]:
  rows=[s.strip()for s in sym['libc'].splitlines()if s.split()and s.split()[-1]==n];assert len(rows)==1 and int(rows[0].split()[1],16)==a;definitions.append(rows[0])
 tls=[]
 for pc,ldr in[(0xb97f0,0xb97f4),(0x2b704,0x2b708)]:
  z=u('libc',ldr);assert adrp('libc',pc)+((z>>10)&4095)*8==0x19ade0;tls.append({'ADRP':hex(pc),'LDR':hex(ldr),'slot':'0x19ade0'})
 r=rr('libc',0x19ade0);assert'R_AARCH64_TLS_TPREL64'in r
 assert q('scheduler',0x21cc50)==0x1301e0 and'R_AARCH64_RELATIVE'in rr('scheduler',0x21cc50)
 dyn=subprocess.check_output(['readelf','-dW',str(v.root/v.resolve(FILES['scheduler']).lstrip('/'))],text=True,env=env);assert'Shared library: [libc.so.6]'in dyn
 # Selected local branches only; not a semantic simulation or timing fixture.
 branches=[]
 for a,t in[(0x112884,0x1128b8),(0x1128a0,0x1128b8),(0x1128b4,0x112894),(0x130214,0x130270),(0x130230,0x1302f0)]:
  z=u('scheduler',a);i=(z>>5)&0x7ffff;i-=0x80000 if i&0x40000 else 0;assert a+(i<<2)==t;branches.append({'VA':hex(a),'bytes':raw('scheduler',a,4).hex(),'target':hex(t)})
 host=[]
 for p,selectors in[(Path('/usr/include/bits/types/struct_timespec.h'),['__time_t tv_sec','__syscall_slong_t tv_nsec']),(Path('/usr/include/time.h'),['extern int nanosleep (','struct timespec *__remaining);']),(Path('/usr/include/asm-generic/errno-base.h'),['#define\tEINTR'])]:
  z=p.read_bytes();lines=z.decode().splitlines();chosen=[{'line':i,'text':s}for i,s in enumerate(lines,1)if any(x in s for x in selectors)];assert chosen;host.append({'HOST_path':str(p),'sha256':H(z),'bytes':len(z),'selected_lines':chosen,'scope':'Host semantic API context only; not original target header/layout/ABI proof.'})
 for p in[V,O/'research/2026-11-01-deep-scheduler/REPORT.md',O/'research/2026-11-01-deep-scheduler/SOURCE.json',W/'work/f460-f461-comparison/2026-11-01-depth/reviews/f460-source-review.md',W/'work/f460-f461-comparison/2026-11-01-run03/API_CONTEXT.json',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'images':{k:{'path':FILES[k],'sha256':EXPECTED[k],'PT_LOAD':[list(x)for x in loads[k]]}for k in FILES},'spans':spans,'guards':[{'object':k,'VA':hex(a),'word':hex(w)}for k,a,w in GUARDS],'scheduler_import_calls':imports,'candidate_libc_definitions':definitions,'wrapper_local_delegate':{'BL':'0xb97dc','target':'0xb47a0','body_not_followed':True},'errno_TLS':{'joins':tls,'original_relocation':r},'compiled_primary':{'slot':'0x21cc50','target':'0x1301e0','relocation':rr('scheduler',0x21cc50)},'local_branch_targets':branches,'source_boundaries':['opaque formatting/diagnostic helpers','nonnull-delay andduration workers','clock_nanosleep/OS delegate body','receiving/transport/MQTT/libjel/auth/session/framing','actual binding/TLS/error/elapsed/runtime state']})
 out['HOST_API_CONTEXT.json']=J({'evidence':host,'scope':'Not target source/layout. Ordinary Linux/POSIX ABI assumptions are explicit; numeric4 guard in original stands independently.'})
 out['CONTRACT.json']=J({'stored_data':'manageroperation2 copies32-bitword; storagehelper placesinline data24/32,manager40/invoker48','request':'freshLDRW0zeroextends toX0; nonzero→two64bitwords[UInt32,0]atSP8/16; X0=X1=SP8 foractualnanosleeprequest','loop':'return!=-1→normalepilogue; return-1→errno pointer/word; numeric4→retry withsame storage; othercode→normalepilogue','API_premise':'UnderordinaryLinux/POSIXLP64timespec/errno andcandidateproviderbinding, firstwordseconds/secondnanoseconds and4EINTR; no actualalias/rounding/scheduling/elapsed/validalldomains proof','selected_common_caller':'zerooperational12+manager40nonNULL→invoker48(data24),normalreturn→freshoperational16zero→markerbyte8=1 andnormalW0=1','marker_limit':'Normalcallbackreturn includesnon-EINTRerror exits; markerdoesnotproveactualsleep success/elapsedtime/wholeScenecompletion','execution':{'new_original':0,'models':0,'fixtures':0,'old_product_ledgers':'unchanged'}})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(spans),'guards':len(GUARDS),'import_proofs':len(imports),'provider_definitions':len(definitions),'TLS_joins':len(tls),'branches':len(branches),'host_semantic_headers':len(host),'inputs':len(pins),'original_execution':0}});return out

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
 print(json.dumps({'check':ck,'outputs':len(o),'spans':len(SPANS),'guards':len(GUARDS),'new_original_execution':0}))
if __name__=='__main__':main()
