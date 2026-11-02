#!/usr/bin/env python3
"""Exclusive fresh BNLD condition factory/compiled selected numeric predicate source."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode();s=importlib.util.spec_from_file_location('f460_bnld_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/scheduling_manager/scheduling_manager';E='5017302a7965f8eafe3ec1ac55946b2aecc3c4c1496923022c6e24ad74d6bf62'
SP=[('own-raw-name-match-and-row-index',0x50dd8,0x50e3c),('own-raw-factory-jump',0x50f60,0x50f7c),('selected-raw-factory-allocation',0x51bb8,0x51c08),('raw-status-default-and-presence',0x4aa94,0x4aac4),('raw-level-asint-no-status',0x4ab4c,0x4ab80),('same-json-reparse-compiled-construction',0xfa5b4,0xfa614),('compiled-field-copy-primary',0x161d00,0x161d34),('predicate-entry-return-query',0x161880,0x161930),('selected-on-string-and-numeric-operators',0x161b9c,0x161c00),('numeric-equal-and-less-threshold',0x161c10,0x161c30)]
G=[(0x50ddc,0x9125837b),(0x50e30,0x5100075a),(0x50f6c,0x787a5800),(0x50f74,0x8b20ab40),(0x51bcc,0x9100631a),(0x51bd0,0xd2800800),(0x51bdc,0xaa1503e1),(0x51bf0,0xf90002b3),(0x51c00,0xfc0342a0),(0x4aa98,0x2f000400),(0x4aab4,0xfc034260),(0x4ab5c,0xfc034260),(0x4ab68,0xb9003a60),(0x4ab6c,0x7100001f),(0x4ab74,0x12800000),(0x4ab78,0xb9003660),(0xfa5c4,0xaa1303e8),(0xfa5cc,0x91030296),(0xfa5d4,0xd63f0020),(0xfa5ec,0xd2801900),(0xfa5fc,0xaa0003f5),(0xfa60c,0xf901d3f5),(0x161d18,0x3940a2a3),(0x161d1c,0x3cc2c2a0),(0x161d20,0xf9000262),(0x161d2c,0x3902c263),(0x161d30,0x3c8b4260),(0x16189c,0xaa0003f3),(0x1618a4,0x91022015),(0x1618a8,0x3942c000),(0x1618b8,0x52800034),(0x1618dc,0x2a1403e0),(0x161910,0x91024262),(0x161914,0x910023e8),(0x161918,0x52800001),(0x161924,0xf94007f6),(0x161bb0,0xb94032c1),(0x161bb4,0x3100041f),(0x161bbc,0xb94032a0),(0x161bd8,0xb9403aa0),(0x161bdc,0x6b01001f),(0x161be0,0x1a9fd7f4),(0x161bf8,0x1a9f07f4),(0x161c18,0x1a9f17f4),(0x161c28,0x1a9fa7f4)]
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
 classes=[]
 for AP,RT,name,slots in[(0x214058,0x219670,'17BaseBnldCondition',{}),(0x214078,0x219688,'13BnldCondition',{0:0x48710}),(0x217f80,0x21d990,'19BnldConditionRunner',{16:0x161880})]:
  assert q(AP-8)==RT and cs(q(RT+8))==name;rows=[rr(AP-8),rr(RT+8)]
  for of,t in slots.items():assert q(AP+of)==t;rows.append(rr(AP+of))
  assert all('R_AARCH64_RELATIVE'in z for z in rows);classes.append({'AP':hex(AP),'RTTI':hex(RT),'name':name,'slots':{str(k):hex(t)for k,t in slots.items()},'relocations':rows})
 assert struct.unpack('<QQ',raw(0x213980,16))==(4,0x196980)and cs(0x196980)=='BNLD'
 ht=struct.unpack('<h',raw(0x196d76,2))[0];hc=struct.unpack('<h',raw(0x1b5958,2))[0];assert ht==0x30f and 0x50f7c+4*ht==0x51bb8 and hc==0x389 and 0xf9790+4*hc==0xfa5b4
 calls=[]
 for a,t in[(0x51bc0,0x4aa60),(0x51be4,0x4e3d0),(0xfa5e0,0x4aa60),(0xfa600,0x161c40),(0xfa610,0xf9450),(0x16191c,0x18def0)]:assert bl(a)==t;calls.append({'VA':hex(a),'target':hex(t),'bytes':raw(a,4).hex(),'body_opaque':t in[0x4e3d0,0x18def0]})
 imports=[]
 for pc,plt,slot,name in[(0x4aab8,0x24230,0x21e788,'_ZNK4Json5Value8isMemberEPKc'),(0x4ab60,0x24a50,0x21eb98,'_ZNK4Json5ValueixEPKc'),(0x4ab64,0x247b0,0x21ea48,'_ZNK4Json5Value5asIntEv'),(0xfa5f4,0x24300,0x21e7f0,'_Znwm@GLIBCXX_3.4')]:
  assert bl(pc)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot;r=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(plt,16).hex(),'relocation':r})
 pp=[]
 for a,c,t in[(0x51bc4,0x51bc8,0x214078),(0xfa5e4,0xfa5e8,0x214078),(0x161d00,0x161d04,0x217f80),(0x4ab50,0x4ab54,0x195580)]:
  x=u(c);assert x&0xffc00000==0x91000000 and ap(a)+(x>>10&4095)==t;pp.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t)})
 assert cs(0x195580)=='level'and cs(0x1954e8)=='status';assert u(0x161b9c)==0x79400021 and u(0x161ba0)==0x528dcde0 and u(0x161ba4)==0x6b00003f
 pins={P:{'bytes':len(b),'sha256':H(b),'resolved':v.resolve(P)}}
 for p in[V,O/'research/2026-11-01-run07-receiver/REPORT.md',O/'research/2026-11-01-run09-condition/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image':P,'sha256':E,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'classes':classes,'own_type_row':{'row':2,'row_VA':'0x213980','literal':'BNLD','name_VA':'0x196980'},'switches':{'raw_index':'row2 minus1=1','raw_entry':'0x196d76','raw_halfword':ht,'raw_base':'0x50f7c','raw_target':'0x51bb8','compiled_entry':'0x1b5958','compiled_halfword':hc,'compiled_base':'0xf9790','compiled_target':'0xfa5b4'},'PIC_joins':pp,'local_calls':calls,'imports':imports,'selected_contract':{'raw_allocation_request':64,'compiled_allocation_request':200,'compiled_destination':'same returned allocation base','field_copy':'raw40→compiled176; raw44..59→compiled180..195','selected_fields':{'type':180,'operator':184,'status':188,'level_threshold':192},'numeric_premises':'enablednonzero; selectedopaquequeryvalidnonnullrecord; recordstatusstringexact2byteson; configuredstatus188==-1; validobservedwordatrecord48','numeric_operand_orientation':'configuredsignedthreshold192 op0< observedrecord48;op1>;op2==;op3!=','query':'18def0 bodyopaque; returnpairSP8/16,keythis144,selector0','same_consumer':'compiledAPslot16; sameconditionrangeappendrequestf9450 inherited run07/09 underactualsamevalidscene/pointerpremises','scope':'No fullrawserializer/provider/coherentJSON/runtimequery/recordtype/units/physical/lifetime proof'},'new_original_execution':0,'models_fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.v2.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'imports':len(imports),'classes':len(classes),'local_calls':len(calls),'inputs':len(pins),'original_execution':0}});return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');ck=p.parse_args().check;o=build();C=D/'first-candidate';cp={**o,'REPORT.v2.md':(D/'REPORT.v2.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in cp.items()})
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
