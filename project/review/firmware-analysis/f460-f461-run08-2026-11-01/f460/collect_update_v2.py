#!/usr/bin/env python3
"""Exclusive static F460 update manifest selection and local filename-list proof."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode()
s=importlib.util.spec_from_file_location('f460_update_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P='/home/bticino/bin/dedrifupdater';E='8f32212bee98b507690f1e22d6b26524c8a13dc20efcc8cc05900ac4142f9753'
SP=[('file-test-entry',0x5690,0x56dc),('file-read-and-document-gates',0x56f0,0x5798),('actions-node-selection',0x5978,0x59b8),('action-properties-type-selection',0x5a64,0x5b14),('attr-child-normal-recovery-lists',0x5bd8,0x5c90),('normal-cleanup-and-return',0x5c90,0x5cf0),('selected-local-wrapper',0x5d60,0x5de4)]
G=[(0x569c,0x52800201),(0x56b4,0xaa0003f6),(0x56fc,0xb4003060),(0x5720,0x52800002),(0x5724,0xd2800001),(0x572c,0xf9000fe0),(0x5778,0x52800002),(0x577c,0xd2800001),(0x5784,0xf9000fe0),(0x5790,0xf9400c13),(0x599c,0xf9400e74),(0x5a84,0xf9402e9b),(0x5a88,0x52800013),(0x5ab4,0xf9402800),(0x5ac8,0xf94002c0),(0x5acc,0xf9401800),(0x5ad0,0xb9400001),(0x5ad8,0x52800021),(0x5ae0,0xb9000001),(0x5afc,0xf9401c00),(0x5b08,0x52800041),(0x5b10,0xb9000001),(0x5bf4,0xf9402800),(0x5bfc,0x7100067f),(0x5c10,0xf9401c21),(0x5c30,0xf9000700),(0x5c68,0xf9401821),(0x5c6c,0xf9400438),(0x5c7c,0xaa1803e0),(0x5c80,0xf9401858),(0x5c88,0xf9000700),(0x5ca0,0xf9400fe0),(0x5cb4,0x52800000),(0x5d7c,0xaa0003f3),(0x5dcc,0xaa1303e0),(0x5dd8,0x1a9f07e2)]
def build():
 v=m.ImageVFS();b=v.read_bytes(P);br=m.ImageVFS('recovery').read_bytes(P);assert len(b)==43088 and H(b)==E and br==b and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);p=r[2]+a-r[3];return b[p:p+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def cs(a):
  z=bytearray()
  for i in range(96):
   c=raw(a+i,1)
   if c==b'\0':return z.decode()
   z+=c
  raise AssertionError('literal cap')
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
 rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env)
 def rr(a):return next(s.strip()for s in rels.splitlines()if s.startswith(f'{a:016x} '))
 imports=[]
 for pc,plt,slot,name in[(0x56d4,0x2180,0x19cb8,'g_file_test'),(0x5728,0x22b0,0x19d50,'xmlReadFile@LIBXML2_2.6.0'),(0x5780,0x22b0,0x19d50,'xmlReadFile@LIBXML2_2.6.0'),(0x578c,0x2580,0x19eb8,'xmlDocGetRootElement@LIBXML2_2.4.30'),(0x5994,0x2540,0x19e98,'g_strcmp0'),(0x5a7c,0x2540,0x19e98,'g_strcmp0'),(0x5aa8,0x2540,0x19e98,'g_strcmp0'),(0x5ac0,0x2540,0x19e98,'g_strcmp0'),(0x5af0,0x2540,0x19e98,'g_strcmp0'),(0x5be8,0x2540,0x19e98,'g_strcmp0'),(0x5c70,0x2330,0x19d90,'g_string_new'),(0x5c84,0x2510,0x19e80,'g_list_append'),(0x5c18,0x2330,0x19d90,'g_string_new'),(0x5c2c,0x2510,0x19e80,'g_list_append'),(0x5c98,0x2740,0x19f98,'xmlCleanupParser@LIBXML2_2.4.30'),(0x5c9c,0x2500,0x19e78,'xmlMemoryDump@LIBXML2_2.4.30'),(0x5ca4,0x2700,0x19f78,'xmlFreeDoc@LIBXML2_2.4.30'),(0x5cb0,0x2210,0x19d00,'g_unlink')]:
  assert bl(pc)==plt;z=u(plt+4);assert z&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220 and ap(plt)+((z>>10)&4095)*8==slot;r=rr(slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(plt,16).hex(),'relocation':r})
 pp=[]
 for a,c,t in[(0x56b8,0x56bc,0x7bf0),(0x5714,0x5718,0x7bf0),(0x576c,0x5770,0x7bf0),(0x57c8,0x598c,0x7cc8),(0x5a48,0x5a78,0x7d18),(0x5a90,0x5a94,0x7d20),(0x5a58,0x5a5c,0x7d28),(0x5a98,0x5a9c,0x7d38),(0x5a50,0x5a54,0x7d68),(0x5ca8,0x5cac,0x7bf0)]:
  assert ap(a)+ai(c)==t;pp.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'bytes':[raw(a,4).hex(),raw(c,4).hex()]})
 literals={hex(a):cs(a)for a in[0x7bf0,0x7cc8,0x7d18,0x7d20,0x7d28,0x7d38,0x7d68]};assert list(literals.values())==['/tmp/fwz.xml','actions','action','type','firmware','recovery_firmware','attr']
 calls=[]
 for a,t in[(0x56f8,0x5140),(0x5d8c,0x4b60),(0x5dd0,0x5690)]:assert bl(a)==t;calls.append({'VA':hex(a),'target':hex(t),'bytes':raw(a,4).hex(),'delegate_not_audited':t!=0x5690})
 branches=[]
 for a,t in[(0x56d8,0x5758),(0x56fc,0x5d08),(0x5730,0x578c),(0x5788,0x5734),(0x5ad4,0x5ae4),(0x5b04,0x5b14),(0x5c00,0x5c64),(0x5c08,0x5ba0),(0x5d94,0x5dcc)]:
  x=u(a);assert x&0xff000010 in(0x54000000,0xb4000000,0xb5000000)or x&0x7f000000 in(0x34000000,0x35000000);i=(x>>5)&0x7ffff;i-=0x80000 if i&0x40000 else 0;assert a+(i<<2)==t;branches.append({'VA':hex(a),'target':hex(t),'bytes':raw(a,4).hex()})
 manifest=O/'extracted/fwz.xml';mb=manifest.read_bytes();ml=mb.decode().splitlines();chosen=[{'line':i,'text':line}for i,line in enumerate(ml,1)if i in[3,4,5]or 12<=i<=19];assert '<name>F460</name>'in ml and '<fwz_ver>2.0.12</fwz_ver>'in ml
 out['MANIFEST_CONTEXT.json']=J({'path':str(manifest.relative_to(W)),'bytes':len(mb),'sha256':H(mb),'safe_selected_lines':chosen,'scope':'Extracted package declarations, not observed runtime /tmp/fwz.xml, no parser/execution fixture.'})
 pins={P:{'bytes':len(b),'sha256':H(b),'normal_resolved':v.resolve(P),'recovery_sha256':H(br),'normal_recovery_bytes_equal':True},str(manifest.relative_to(W)):{'bytes':len(mb),'sha256':H(mb)}}
 for p in[V,O/'research/2026-11-01/first-pass/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'image':P,'sha256':E,'normal_recovery_same_selected_binary':True,'PT_LOAD':[list(r)for r in L],'spans':ss,'guards':[{'VA':hex(a),'word':hex(w)}for a,w in G],'PIC_joins':pp,'safe_literals':literals,'import_proofs':imports,'local_calls':calls,'branches':branches,'contract':{'saved_context':'entryX0→X22; C=[X22]','selected_firmware_record':'R=[C+48], requiresword0zero, store1; selectedattrcontent→GString→appendR+8','selected_recovery_record':'R=[C+56], requiresword0zero, store2; selectedattrcontent→GString→appendR+8','provider_premises':'ordinary valid libxml nodes/string/list/allocator/provider return paths; no runtime file or tree supplied','local_normal_return':0,'excluded':['0x5140 extraction delegate body','0x4b60 precheck body','signature/version/authenticity and actual update outcomes','flash/mount/reboot/OS/provider bodies','closedreceiving/transport/MQTT/libjel/auth/session/framing']},'new_original_execution':0,'models_fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.v2.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':len(G),'PIC_joins':len(pp),'imports':len(imports),'local_calls':len(calls),'branches':len(branches),'inputs':len(pins),'new_original_execution':0}});return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');ck=p.parse_args().check;o=build();C=D/'first-candidate-v2';cp={**o,'REPORT.v2.md':(D/'REPORT.v2.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({n:{'bytes':len(z),'sha256':H(z)}for n,z in cp.items()})
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
