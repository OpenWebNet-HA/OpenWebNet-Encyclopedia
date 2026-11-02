#!/usr/bin/env python3
"""Exclusive original F460 registry/callable/argument-owner source proof, static only."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f460_selector_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/matrix_mx/matrix_mx';E='16d92b02ffe89819f6947d93efa76a0f24f8b590a43d3e5d8fdc7226ec68a4ff'
SP=[('registration-global-and-range',0x27ff0,0x282e0),('callable-addresses',0x28208,0x28220),('key89-pointer-key-producer',0x28614,0x286f4),('registry-construction-request',0x286f4,0x287a4),('selected-entry-node-copy',0x12fb74,0x12fc84),('caller-entry-owner-range',0xed610,0xed6b4),('existing-key-tuple-check',0xed6b4,0xed750),('selected-hash-lookup-and-call',0xed7d8,0xed8cc),('callable-pointer-invoker',0xf0d00,0xf0d78),('callable-copy-manager',0xf5350,0xf5394),('owner-word120-getter',0x17abe0,0x17abec),('owner-word124-getter',0x17ac60,0x17ac6c),('owner-word128-getter',0x17aca0,0x17acac)]
G=[(0x282d4,0x91166260),(0x28628,0x913f4042),(0x2864c,0x52800b35),(0x286a4,0x911ae3ea),(0x286dc,0xb906b3f5),(0x286e0,0xa9007d42),(0x286e8,0xa9012149),(0x12fb88,0xb9400286),(0x12fbf4,0xb9000801),(0x12fc08,0x91002281),(0x12fc10,0x52800042),(0x12fc14,0xd63f0060),(0x12fc18,0x3cc18280),(0x12fc1c,0x3d800aa0),(0x12fc74,0x9100a294),(0xed62c,0xaa0003f5),(0xed630,0xf9400000),(0xed644,0xa941d814),(0xed678,0xb9400293),(0xed7d8,0xf942d2e2),(0xed7e0,0xf942cee1),(0xed7f8,0xb9400b60),(0xed7fc,0x6b00027f),(0xed838,0x9100437b),(0xed85c,0xb90027fc),(0xed864,0x290387e0),(0xed868,0xf9400b60),(0xed878,0xf9400f64),(0xed884,0xaa1c03e8),(0xed88c,0xd63f0080),(0xed894,0xa9408801),(0xed8a4,0xa9007c23),(0xed8b8,0xf9000402),(0xf0d18,0xf9400005),(0xf0d1c,0xb9400020),(0xf0d20,0xb9400041),(0xf0d24,0xb9400062),(0xf0d3c,0xd63f00a0),(0xf5370,0xf9400021),(0xf5374,0xf9000001),(0x17abe4,0xb9407800),(0x17ac64,0xb9407c00),(0x17aca4,0xb9408000)]
def build():
 v=m.ImageVFS();b=v.read_bytes(P);assert H(b)==E and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);p=r[2]+a-r[3];return b[p:p+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def ai(a):
  x=u(a);assert x&0xffc00000==0x91000000;return(x>>10)&4095
 def bl(a):
  x=u(a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 for a,w in G:assert u(a)==w,(hex(a),hex(u(a)),hex(w))
 out={};ss=[];hp=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='')
 for name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=z.encode();ss.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(a,e-a).hex(),'sha256':H(raw(a,e-a))})
 pp=[]
 for a,c,t in[(0x27d50,0x27ff0,0x31a200),(0x28624,0x28628,0x112fd0),(0x28210,0x28214,0xf0d00),(0x28218,0x2821c,0xf5350),(0xed654,0xed658,0x31a200)]:
  assert ap(a)+ai(c)==t;pp.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'bytes':[raw(a,4).hex(),raw(c,4).hex()]})
 cc=[]
 for a,t in[(0x287a0,0x12fad0),(0xed688,0x17abe0),(0xed694,0x17ac60),(0xed6a0,0x17aca0),(0xed83c,0x17abe0),(0xed848,0x17ac60),(0xed858,0x17aca0)]:
  assert bl(a)==t;cc.append({'BL':hex(a),'target':hex(t),'bytes':raw(a,4).hex()})
 # Source branch arithmetic, not runtime/semantic fixtures.
 branches=[]
 for a,t in[(0xed7f0,0xed750),(0xed800,0xed82c),(0xed808,0xed750),(0xed820,0xed750),(0xed828,0xed804),(0xed86c,0xeda1c),(0xf5364,0xf5370)]:
  x=u(a);assert x&0xff000010 in(0x54000000,0xb4000000,0xb5000000)or x&0x7f000000 in(0x34000000,0x35000000);i=(x>>5)&0x7ffff;i-=0x80000 if i&0x40000 else 0;assert a+(i<<2)==t;branches.append({'VA':hex(a),'bytes':raw(a,4).hex(),'target':hex(t)})
 assert (2072-32)//40==51 and(1712-32)%40==0 and 0x31a200+1432==0x31a798
 pins={P:{'sha256':H(b),'bytes':len(b),'resolved':v.resolve(P)}}
 for p in[V,O/'research/2026-11-01-run04-catalogue/REPORT.v2.md',O/'research/2026-11-01-run04-catalogue/SOURCE.json',W/'work/f460-f461-comparison/2026-11-01-run04/reviews/f460-source-review.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'original_image':P,'sha256':E,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'PIC_joins':pp,'direct_calls':cc,'selected_branches':branches,'source_contract':{'registered_key':89,'constructor':'0x112fd0','manager':'0xf5350','invoker':'0xf0d00','registry':'0x31a798','owner_input':'provided pointee at saved entry[X0]','provided_owner_fields_to_constructor_words':{'120':'W0/modobj request','124':'W1/line_modobj request','128':'W2/brand_modobj request'},'hidden_result':'SP40 sameX8','premises':['static initializer/ordinary helper returns','selected key89 and valid original map/callable state','same provided owner object/lifetime','selected new-object route/normal returns','provider/SQL behavior inherited conditional']},'new_original_execution':0,'models':0,'fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'PIC_joins':len(pp),'direct_calls':len(cc),'branches':len(branches),'inputs':len(pins),'original_execution':0}});return out

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
 print(json.dumps({'check':ck,'outputs':len(o),'spans':len(SP),'guards':len(G),'new_original_execution':0}))
if __name__=='__main__':main()
