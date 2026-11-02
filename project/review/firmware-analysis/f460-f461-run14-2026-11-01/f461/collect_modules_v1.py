#!/usr/bin/env python3
"""Exclusive F461 local module-admission selection, no loader/vendor execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import struct,json,hashlib,importlib.util,subprocess,re,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=W/'work/f461-firmware/2.0.11';V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode();s=importlib.util.spec_from_file_location('modules_vfs',V);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
P='/home/bticino/bin/coso'
SP=[('support-and-directory','0x56f0','0x572c'),('filename-filters-and-open','0x572c','0x578c'),('symbol-gates','0x578c','0x57d0'),('iteration-and-normal-return','0x57d0','0x5808'),('unsupported-diagnostic-return','0x5808','0x5830'),('entry-store-and-initializer-boundary','0x5830','0x586c'),('module-open-and-directory-failure','0x586c','0x589c'),('actual-main-call','0x32f4','0x3300')]
G={0x56fc:0xaa0003f6,0x5700:0xa9057fff,0x5708:0x34000800,0x570c:0xf9400ac0,0x5710:0xd2800002,0x5714:0x52800001,0x571c:0xf9400400,0x5724:0xaa0003f4,0x5728:0xb4000b40,0x574c:0xaa0003f3,0x5750:0xb40004c0,0x5758:0x34ffff40,0x5768:0xaa1303e1,0x576c:0xd2800002,0x5770:0x34fffe80,0x5774:0xf9400ac0,0x5778:0xf9400400,0x5780:0xaa0003f8,0x5784:0x52800061,0x578c:0xaa0003f3,0x5790:0xb40006e0,0x5798:0x910143e2,0x57a4:0x34000120,0x57a8:0x910163e2,0x57c0:0xd2800200,0x57c4:0x35000361,0x57f4:0x52800000,0x5808:0x52800081,0x5820:0x52800020,0x5838:0xf9400ad9,0x5844:0xa9004c38,0x5850:0xf9402be1,0x5854:0xf9000320,0x5858:0xf9400840,0x585c:0xd63f0020,0x5890:0x12800000,0x32f4:0xaa1403e0}
def build():
 f=v.ImageVFS();b=f.read_bytes(P);assert H(b)=='2fb47ebfb8e63df22053a5ca95b08183a11ab93b248dcbc2b2d7a5f682561197'and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  r=next(r for r in L if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return b[o:o+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5&0x7ffff)<<2)|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def bl(a):
  x=u(a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 for a,x in G.items():assert u(a)==x,(hex(a),hex(u(a)))
 assert bl(0x32f8)==0x56f0
 hp=f.root/f.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);symbols=subprocess.check_output(['readelf','-Ws',str(hp)],text=True,env=env);dyn=subprocess.check_output(['readelf','-dW',str(hp)],text=True,env=env);needed=[z.strip()for z in dyn.splitlines()if'Shared library: [libgmodule-2.0.so.0]'in z or'Shared library: [libglib-2.0.so.0]'in z];assert len(needed)==2
 defs=[z.strip()for z in symbols.splitlines()if re.search(r'\bregister_plugins$',z)];assert defs and all('00000000000056f0'in z and'428 FUNC'in z for z in defs)
 literals=[]
 for a,c,t,text in [(0x572c,0x5730,0x62e0,'lib'),(0x5738,0x573c,0x62e8,'.so'),(0x5794,0x579c,0x62f0,'init_plugin'),(0x57b0,0x57b4,0x62b8,'stop_plugin')]:
  x=u(c);assert x&0xffc00000==0x91000000 and ap(a)+(x>>10&4095)==t and raw(t,len(text)+1)==text.encode()+b'\0';literals.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'value':text})
 imports=[]
 for pc,plt,name in [(0x5704,0x2d00,'g_module_supported'),(0x5720,0x2eb0,'g_dir_open'),(0x5744,0x2960,'g_dir_read_name'),(0x5754,0x2c70,'g_str_has_prefix'),(0x5764,0x2e20,'g_str_has_suffix'),(0x577c,0x2d30,'g_build_filename'),(0x5788,0x2d70,'g_module_open'),(0x57a0,0x2c00,'g_module_symbol'),(0x57b8,0x2c00,'g_module_symbol'),(0x57cc,0x2a30,'g_module_close'),(0x57ec,0x2950,'g_dir_close'),(0x581c,0x2ea0,'g_log'),(0x5834,0x2aa0,'g_malloc'),(0x5848,0x2c40,'g_list_append'),(0x5860,0x2dd0,'update_log_type'),(0x586c,0x2dc0,'g_module_error')]:
  assert bl(pc)==plt;x=u(plt+4);assert x&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220;slot=ap(plt)+(x>>10&4095)*8;rr=[z.strip()for z in rels.splitlines()if re.match(r'^[0-9a-fA-F]+\s',z)and int(z.split()[0],16)==slot];assert len(rr)==1 and'JUMP_SLOT'in rr[0]and rr[0].split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'relocation':rr[0]})
 out={};ss=[]
 for name,aa,ee in SP:
  a=int(aa,16);e=int(ee,16);z=raw(a,e-a);t=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=t.encode();ss.append({'name':name,'start_VA':aa,'end_VA_exclusive':ee,'bytes_hex':z.hex(),'sha256':H(z)})
 pins={P:{'size':len(b),'sha256':H(b)}}
 for p in [V,O/'research/2026-11-01-run11-config-selection/REPORT.md',O/'research/2026-11-01-run11-config-selection/SOURCE.json',O/'research/2026-11-01-run04-field-owner/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'size':len(z),'sha256':H(z)}
 out['INPUTS.json']=J(pins);out['SOURCE.json']=J({'image':P,'sha256':H(b),'PT_LOAD':[list(r)for r in L],'definition':defs,'dependency_requests':needed,'spans':ss,'guards':{hex(a):hex(x)for a,x in G.items()},'literal_joins':literals,'imports':imports,'scope':{'provided_owner':'X0savedX22; P=[owner16], LibDir=[P8], moduleentrylistP0, ConfigDir=[P16]','filters':'name prefixlib and suffix.so; notlibplug-specific or a format/security proof','retention':'new16byteentry(path,modulehandle) appendedP0 BEFORE initfunctionrequest','symbols':'both init_plugin and stop_plugin lookups must return nonzero beforeselectedentryappend/init; stopfunctionnotinvokedhere','initializer_boundary':'BLR585c bodyclosed, returnedmachinevalue not tested beforeupdate_log_type/loop continuation','returns':'unsupported branch1 only ifnumericflag4diagnosticreturns; directoryNULL low32−1; normaltraversal0 regardlessselectedentryskip/failure','unclosed':'actualboot/DTB/auxcoreselection, runtimefiles/modules/binding/readiness/lifetime/security outcomes'},'execution':{'original':0,'provider':0,'models':0,'fixtures':0,'target_IO':0}})
 out['OUTPUT_MANIFEST.json']=J({'outputs':{p:{'size':len(z),'sha256':H(z)}for p,z in out.items()},'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes())});return out
out=build();cp={**out,'REPORT.md':(D/'REPORT.md').read_bytes(),Path(__file__).name:Path(__file__).read_bytes()};ix=J({'files':{p:{'size':len(z),'sha256':H(z)}for p,z in cp.items()}});C=D/'first-candidate'
if '--check'in sys.argv:
 for p,z in out.items():assert(D/p).read_bytes()==z,p
 for p,z in cp.items():assert(C/p).read_bytes()==z,p
 assert(C/'INDEX.json').read_bytes()==ix
else:
 assert not C.exists()and all(not(D/p).exists()for p in out)
 for p,z in out.items():q=D/p;q.parent.mkdir(parents=True,exist_ok=True);q.open('xb').write(z)
 for p,z in cp.items():q=C/p;q.parent.mkdir(parents=True,exist_ok=True);q.open('xb').write(z)
 (C/'INDEX.json').open('xb').write(ix)
print(json.dumps({'check':'--check'in sys.argv,'outputs':len(out),'spans':len(SP),'guards':len(G),'literals':4,'imports':16,'pins':len(json.loads(out['INPUTS.json'])),'first_copies':len(cp),'original_execution':0}))
