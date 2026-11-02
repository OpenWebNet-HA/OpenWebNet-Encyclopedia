#!/usr/bin/env python3
"""Exclusive static updater staged-list substring consumer; no downstream operations."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode();s=importlib.util.spec_from_file_location('f460_updateconsumer_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/bin/dedrifupdater';E='8f32212bee98b507690f1e22d6b26524c8a13dc20efcc8cc05900ac4142f9753'
SP=[('same-wrapper-context-and-selector',0x66d0,0x6714),('consumer-context-list-source',0x5f30,0x5fac),('list-text-substring-and-copy-request',0x5fac,0x6000),('other-list-source-branch-only',0x63a4,0x63b8)]
G=[(0x66dc,0x2a0103e3),(0x66e0,0x910013e2),(0x66f4,0x2a0103f4),(0x6704,0x52800061),(0x670c,0xaa0003f3),(0x5f3c,0x7100043f),(0x5f50,0xaa0003f3),(0x5f58,0xaa0203f4),(0x5f5c,0x2a0103f6),(0x5f64,0x2a0303fa),(0x5f74,0xf9400260),(0x5f7c,0xf9401c00),(0x5f80,0xf9400400),(0x5f88,0xaa0003f5),(0x5fa4,0x121e7ad6),(0x5fac,0xf94002a0),(0x5fb8,0xf9400000),(0x5fc8,0xf94006b5),(0x5fd0,0xf94002a0),(0x5fd8,0x92800001),(0x5fdc,0xf9400000),(0x5fe8,0x710006df),(0x5ff0,0xf94002a0),(0x5ff4,0xf9400000),(0x5ffc,0xaa0003f5),(0x63a4,0xf9401800),(0x63a8,0xf9400400)]
def build():
 v=m.ImageVFS();b=v.read_bytes(P);assert H(b)==E and len(b)==43088 and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);p=r[2]+a-r[3];return b[p:p+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def bl(a):
  x=u(a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def cond(a):
  x=u(a);assert x&0xff000010==0x54000000;i=x>>5&0x7ffff;return a+((i-0x80000 if i&0x40000 else i)<<2)
 def cb(a):
  x=u(a);assert x&0x7e000000==0x34000000;i=x>>5&0x7ffff;return a+((i-0x80000 if i&0x40000 else i)<<2)
 for a,w in G:assert u(a)==w,(hex(a),hex(u(a)),hex(w))
 out={};ss=[];hp=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='')
 for name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=z.encode();ss.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(a,e-a).hex(),'sha256':H(raw(a,e-a))})
 rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(s.strip()for s in rels.splitlines()if s.startswith(f'{a:016x} '))
 imports=[]
 for pc,plt,slot,name in[(0x5f84,0x2640,0x19f18,'g_list_first'),(0x63ac,0x2640,0x19f18,'g_list_first'),(0x5fe0,0x2430,0x19e10,'g_strstr_len'),(0x5fbc,0x2430,0x19e10,'g_strstr_len'),(0x5ff8,0x2330,0x19d90,'g_string_new')]:
  assert bl(pc)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot;r=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(plt,16).hex(),'relocation':r})
 assert bl(0x6708)==0x5f30
 branches=[]
 for a,t in[(0x5f78,0x63a4),(0x5fec,0x5fac)]:assert cond(a)==t;branches.append({'VA':hex(a),'target':hex(t),'word':hex(u(a))})
 for a,t in[(0x5f90,0x66c0),(0x5fc0,0x5fc8),(0x5fc4,0x5ff0),(0x5fcc,0x66c0),(0x5fe4,0x5fac)]:assert cb(a)==t;branches.append({'VA':hex(a),'target':hex(t),'word':hex(u(a))})
 literals=[]
 for a,c,t,text in[(0x5f94,0x5f98,0x6a58,'.'),(0x5f9c,0x5fa0,0x7d78,'Image')]:
  x=u(c);assert x&0xffc00000==0x91000000 and ap(a)+(x>>10&4095)==t and raw(t,len(text)+1)==text.encode()+b'\0';literals.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'value':text})
 pins={P:{'bytes':len(b),'sha256':H(b),'resolved':v.resolve(P)}}
 for p in[V,O/'research/2026-11-01-run08-update/REPORT.v3.md',O/'research/2026-11-01-run08-update/SOURCE.json',O/'research/2026-11-01-run08-update/RETURN_VALUE_REFINEMENT.v3.json',W/'work/f460-f461-comparison/2026-11-01-run08/reviews/f460-source-review.v2.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image':P,'sha256':E,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'imports':imports,'branches':branches,'literals':literals,'local_call':{'VA':'0x6708','target':'0x5f30','input_X0':'same supplied wrappercontext','W1':3,'X2':'SP+4 outcell','W3':'savedincomingW1'},'selected_contract':{'unsigned_selector_gate':'3>1 selects C+56 record, list atrecord+8','masked_selector':'W22=W1 &0xfffffffd, selected3becomes1','node_fields':'node0data,node8next; supplieddata GString0text','positive_selection':'g_strstr_len(text,-1,dot) nonzero and maskedselector1','component_request':'g_string_new(SAMEselectedtext) at0x5ff8; returnedX0savedX21','producer_identity':'IF same providedcontext as run08; naturalparse/consumer ordering andconstructor notclosed','stop':'0x6000 onward/downstream filesystem/extraction/install/flash/mount/reboot/provider bodies opaque'},'new_original_execution':0,'models_fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'imports':len(imports),'branches':len(branches),'literal_joins':len(literals),'inputs':len(pins),'original_execution':0}});return out

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
