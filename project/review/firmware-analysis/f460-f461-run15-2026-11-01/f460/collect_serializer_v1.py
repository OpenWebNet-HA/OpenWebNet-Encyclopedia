#!/usr/bin/env python3
"""Exclusive static raw BNLD serializer/operator decoder, conditional JSON contract."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode();s=importlib.util.spec_from_file_location('f460_numericserializer_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/scheduling_manager/scheduling_manager';E='5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62'
SP=[('actual-serializer-hidden-ABI-and-status-gate',0x48710,0x48764),('selected-level-assignment',0x48890,0x488c4),('serializer-normal-return',0x487cc,0x48808),('base-normal-serializer',0x393d0,0x395d4),('operator-initial-value',0x4a2d0,0x4a2e8),('operator-member-and-length-selection',0x4a400,0x4a440),('decode-higher-and-common-store',0x4a4f4,0x4a528),('decode-different',0x4a528,0x4a558),('decode-lower-equal-prefix',0x4a590,0x4a5c8),('decode-lower-tail',0x4a5f4,0x4a608)]
G=[(0x4872c,0xaa0003f4),(0x48734,0xaa0803f3),(0x4874c,0xb9403681),(0x48750,0x3100043f),(0x48890,0xb9403a81),(0x48894,0x910003f4),(0x488a8,0xaa1303e0),(0x488b0,0xaa1403e1),(0x487e8,0xaa1303e0),(0x48804,0xd65f03c0),(0x393ec,0x52800001),(0x393f4,0xaa0803f4),(0x393f8,0xaa0003f5),(0x39400,0xaa0803e0),(0x3944c,0x3940a2a1),(0x394f8,0xb94032a0),(0x394fc,0x3100041f),(0x39504,0x11000400),(0x39508,0x7100101f),(0x395b0,0x937c7c00),(0x395b8,0x91244021),(0x395c0,0xf8606822),(0x395c4,0xf9400461),(0x4a2d0,0x2f07e600),(0x4a2e4,0xfc02c2a0),(0x4a410,0x910123e8),(0x4a418,0xa94487e0),(0x4a428,0xf100183f),(0x4a430,0xf100143f),(0x4a438,0xf100243f),(0x4a4f8,0x528d2d01),(0x4a4fc,0x72ad0ce1),(0x4a518,0xd2800021),(0x4a51c,0x51000421),(0x4a520,0xb90032a1),(0x4a550,0xd2800081),(0x4a5c0,0xd2800061),(0x4a600,0xd2800041)]
def build():
 v=m.ImageVFS();b=v.read_bytes(P);assert H(b)==E and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);p=r[2]+a-r[3];return b[p:p+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def q(a):return int.from_bytes(raw(a,8),'little')
 def cs(a):
  z=bytearray()
  for i in range(128):
   c=raw(a+i,1)
   if c==b'\0':return z.decode()
   z+=c
  raise AssertionError('literalcap')
 def bl(a):
  x=u(a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 for a,w in G:assert u(a)==w,(hex(a),hex(u(a)),hex(w))
 out={};ss=[];hp=v.root/v.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='')
 for name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=z.encode();ss.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(a,e-a).hex(),'sha256':H(raw(a,e-a))})
 rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(s.strip()for s in rels.splitlines()if s.startswith(f'{a:016x} '))
 assert q(0x214078)==0x48710 and q(0x214070)==0x219688 and cs(q(0x219690))=='13BnldCondition';r=rr(0x214078);assert'R_AARCH64_RELATIVE'in r
 assert bl(0x48748)==0x393d0
 imports=[]
 for pc,plt,slot,name in[(0x39414,0x23d30,0x21e508,'_ZN4Json5ValueC1ENS_9ValueTypeE'),(0x3952c,0x24900,0x21eaf0,'_ZN4Json5ValueC1ERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE'),(0x3953c,0x23ce0,0x21e4e0,'_ZN4Json5ValueixEPKc'),(0x39544,0x244c0,0x21e8d0,'_ZN4Json5ValueaSEOS0_'),(0x4889c,0x23ec0,0x21e5d0,'_ZN4Json5ValueC1Ei'),(0x488ac,0x23ce0,0x21e4e0,'_ZN4Json5ValueixEPKc'),(0x488b4,0x244c0,0x21e8d0,'_ZN4Json5ValueaSEOS0_'),(0x488bc,0x23de0,0x21e560,'_ZN4Json5ValueD1Ev'),(0x4a40c,0x24a50,0x21eb98,'_ZNK4Json5ValueixEPKc'),(0x4a414,0x24bf0,0x21ec68,'_ZNK4Json5Value8asStringB5cxx11Ev')]:
  assert bl(pc)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot;r0=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r0 and r0.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(plt,16).hex(),'relocation':r0})
 keys=[]
 for a,c,t,text in[(0x3942c,0x39430,0x198258,'id'),(0x39458,0x3945c,0x1954b0,'enabled'),(0x394c0,0x394c4,0x1954a8,'type'),(0x39530,0x39534,0x1954b8,'operator'),(0x488a0,0x488a4,0x195580,'level'),(0x4a400,0x4a404,0x1954b8,'operator')]:
  x=u(c);assert x&0xffc00000==0x91000000 and ap(a)+(x>>10&4095)==t and cs(t)==text;keys.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'literal':text})
 assert ap(0x395b4)+(u(0x395b8)>>10&4095)==0x213910
 rows=[]
 for i,text in enumerate(['higher','lower','equal','different']):
  a=0x213910+16*(i+1);n,t=struct.unpack('<QQ',raw(a,16));assert n==len(text)and cs(t)==text;rows.append({'raw_operator':i,'table_index':i+1,'row_VA':hex(a),'length':n,'name_VA':hex(t),'name':text,'bytes_hex':raw(a,16).hex()})
 assert u(0x48754)==0x540009e0 and u(0x39500)==0x54000340
 # Reconstruct the exact byte-comparison immediates rather than execute a name parser.
 assert raw(0x4a4f8,12).hex()=='012d8d52e10cad723f00016b'
 pins={P:{'bytes':len(b),'sha256':H(b),'resolved':v.resolve(P)}}
 for p in[V,O/'research/2026-11-01-run14-numeric/REPORT.v2.md',O/'research/2026-11-01-run14-numeric/SOURCE.json',W/'work/f460-f461-comparison/2026-11-01-run14/reviews/f460-source-review.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image':P,'sha256':E,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'raw_slot0':{'AP':'0x214078','target':'0x48710','relocation':r},'base_call':'0x48748→0x393d0 SAMErawthis/hiddenX8 result','keys':keys,'operator_rows':rows,'imports':imports,'selected_contract':{'raw_status52':'-1 selects48890 numericbranch','level':'raw56→JsonValueC1(int)temporary→SAMEresult[level] mutablelookup→moveassignment','status_presence':'selectednumericbranch requestslevel, no statusmember assignment; base selectednormalcalls keysid/enabled/type/operator only','operator':'raw48 0..3→tableindex+1 strings; ownparser matches higher/lower/equal/different→1/2/3/4minus1→raw48','reparse_inherited':'same result to4aa60; statusabsence/default-1 andlevelasInt→raw56; compiledthreshold192 underordinaryJSON/provider/noextra-member premises','scope':'not fullJSON map/assignment/string/provider proof, no allinputroundtrip/units/configured/runtime/query values'},'new_original_execution':0,'models_fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'imports':len(imports),'operator_rows':len(rows),'key_PIC_joins':len(keys),'inputs':len(pins),'original_execution':0}});return out

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
