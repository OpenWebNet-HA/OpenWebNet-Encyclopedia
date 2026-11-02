#!/usr/bin/env python3
"""Exclusive bounded F461 deadline gap and positive different-object exclusions."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,struct,hashlib,importlib.util,subprocess,re,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=W/'work/f461-firmware/2.0.11';V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode();s=importlib.util.spec_from_file_location('gap_vfs',V);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
P={'automation':'/home/bticino/libcoso/libplug_automation_stm.so','aux':'/home/bticino/libcoso/libplug_aux_stm.so','core':'/home/bticino/libcoso/libcoso.so'}
SP=[('actual-descriptor-registration','automation',0x200c,0x2048),('same-descriptor-initializer-request','core',0x27b8,0x27e8),('private-context-entry','automation',0x23f4,0x2444),('private-null-allocation','automation',0x2b7c,0x2b90),('private-list-return-store','automation',0x25c8,0x25f8),('application-object-preservation','automation',0x2fb0,0x3014),('same-provided-record-append','automation',0x30e8,0x30fc),('aux-nested-parsed-string','aux',0x1f50,0x1f8c)]
G={'automation':{0x200c:0xf947de95,0x203c:0xaa1503e0,0x23f4:0xaa0003f3,0x2428:0xf9402e75,0x242c:0xb4003a95,0x243c:0xf90002b3,0x2b7c:0xd2800e00,0x2b84:0xaa0003f5,0x2b88:0xf9002e60,0x2b8c:0x17fffe29,0x25d0:0xaa0003f9,0x25e4:0xf94012a0,0x25e8:0xf9000323,0x25ec:0xaa1903e1,0x25f4:0xf90012a0,0x2fc8:0xf9400033,0x2fe0:0xa90603e2,0x2ff4:0xaa0103f7,0x300c:0xf9402c98,0x30e8:0xf94033f4,0x30ec:0xaa1703e1,0x30f8:0xf9000280},'core':{0x27c0:0xf9401a62,0x27c4:0xf9003260,0x27c8:0xb4000082,0x27cc:0x91014001,0x27d0:0xaa1303e0,0x27d4:0xd63f0040},'aux':{0x1f60:0xf9400036,0x1f68:0xf9402c13,0x1f6c:0xf94012c0,0x1f74:0xaa0103f4,0x1f78:0xd2800001,0x1f84:0x52800142}}
def build():
 f=v.ImageVFS();B={k:f.read_bytes(p)for k,p in P.items()};L={};HP={};RE={};SY={};env=dict(os.environ,DEBUGINFOD_URLS='')
 for k,b in B.items():
  assert b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183;ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L[k]=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1];HP[k]=f.root/f.resolve(P[k]).lstrip('/');RE[k]=subprocess.check_output(['readelf','-rW',str(HP[k])],text=True,env=env);SY[k]=subprocess.check_output(['readelf','-Ws',str(HP[k])],text=True,env=env)
 def raw(k,a,n):
  r=next(r for r in L[k]if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return B[k][o:o+n]
 def u(k,a):return int.from_bytes(raw(k,a,4),'little')
 def ap(k,a):
  x=u(k,a);assert x&0x9f000000==0x90000000;i=((x>>5&0x7ffff)<<2)|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def bl(k,a):
  x=u(k,a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 def rr(k,a):
  z=[z.strip()for z in RE[k].splitlines()if re.match(r'^[0-9a-fA-F]+\s',z)and int(z.split()[0],16)==a];assert len(z)==1;return z[0]
 for k,gd in G.items():
  for a,x in gd.items():assert u(k,a)==x,(k,hex(a),hex(u(k,a)))
 assert ap('automation',0x1ff8)+(u('automation',0x200c)>>10&4095)*8==0x14fb8
 descriptor=rr('automation',0x14fb8);assert'GLOB_DAT'in descriptor and'automation_stm'in descriptor
 initrel=rr('automation',0x15180);apprel=rr('automation',0x15190);assert'ABS64'in initrel and'automation_stm_init'in initrel and'ABS64'in apprel and'automation_stm_gest_status_from_appli'in apprel
 assert int.from_bytes(raw('automation',0x151a8,8),'little')==0
 imports=[]
 for k,pc,plt,name in [('automation',0x2044,0x1cc0,'register_state_machine'),('core',0x27bc,0x1f80,'get_plug_m'),('automation',0x2b80,0x1d90,'g_malloc0'),('automation',0x25f0,0x1c00,'g_list_append'),('automation',0x30f4,0x1c00,'g_list_append'),('aux',0x1f88,0x1970,'strtol@GLIBC_2.17')]:
  assert bl(k,pc)==plt;x=u(k,plt+4);assert x&0xffc00000==0xf9400000 and u(k,plt+12)==0xd61f0220;slot=ap(k,plt)+(x>>10&4095)*8;r=rr(k,slot);assert'JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'input':k,'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'relocation':r})
 out={};sp=[]
 for name,k,a,e in SP:
  z=raw(k,a,e-a);t=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(HP[k])],text=True,env=env).replace(str(HP[k]),P[k]);out['spans/'+name+'.txt']=t.encode();sp.append({'name':name,'input':k,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':z.hex(),'sha256':H(z)})
 scope=[]
 for k,name,a,size in [('automation','automation_stm_gest_status_from_appli',0x2fb0,2112),('aux','aux_stm_gest_status_from_appli',0x1f50,356)]:
  defs=[r.strip()for r in SY[k].splitlines()if r.rstrip().endswith(' '+name)];assert defs and all(f'{a:016x}'in r and str(size)+' FUNC'in r for r in defs)
  t=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={a+size}',str(HP[k])],text=True,env=env)
  hits=[r.strip()for r in t.splitlines()if re.search(r'\b(?:str\w*|stp)\b',r)and re.search(r'\[x\d+, #32\]',r)];assert hits==[]
  scope.append({'input':k,'function':name,'start_VA':hex(a),'end_exclusive':hex(a+size),'size':size,'source_bytes_sha256':H(raw(k,a,size)),'definition_rows':defs,'query':'rendered STR*/STP with direct non-SP [Xn,#32] operand in these two symbol extents only','matches':hits,'limits':'not alias/bulk/pair-offset/general-callee/whole-image writer analysis; no global absence or untouched-record assertion'})
 pins={P[k]:{'size':len(b),'sha256':H(b)}for k,b in B.items()}
 for p in [V,O/'research/2026-11-01-run12-clock/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'size':len(z),'sha256':H(z)}
 out['INPUTS.json']=J(pins);out['SOURCE.json']=J({'paths':P,'PT_LOAD':{k:[list(r)for r in q]for k,q in L.items()},'spans':sp,'guards':{k:{hex(a):hex(x)for a,x in gd.items()}for k,gd in G.items()},'descriptor':{'VA':'0x15150','bytes':104,'GOT':descriptor,'initializer_slot48':initrel,'application_slot64':apprel,'private_slot88_initial_file_bytes':'0000000000000000'},'imports':imports,'bounded_queries':scope,'positive_exclusions':{'context':'register sameD init48→providedD88 null branch alloc112→D88=P→g_list_append result storedP32','nested_string':'aux Q argX1; parsed=[Q], parsed32 supplied tostrtol, not Q32 numericdeadline','provided_record_append':'automationQ argX1 retainedX23; sameQ to g_list_append, no deadline producer asserted'},'nonzero_record_deadline32_producer':'OPEN','execution':{'original':0,'provider':0,'models':0,'fixtures':0,'target_IO':0}})
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
print(json.dumps({'check':'--check'in sys.argv,'outputs':len(out),'spans':len(SP),'guards':sum(map(len,G.values())),'imports':6,'finite_function_queries':2,'pins':len(json.loads(out['INPUTS.json'])),'first_copies':len(cp),'original_execution':0}))
