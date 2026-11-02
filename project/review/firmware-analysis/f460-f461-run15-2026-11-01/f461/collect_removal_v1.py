#!/usr/bin/env python3
"""Exclusive static F461 local monitor→module-entry removal, no module/provider execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import hashlib,json,struct,importlib.util,subprocess,re,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=W/'work/f461-firmware/2.0.11';V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode();s=importlib.util.spec_from_file_location('removal_vfs',V);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
P='/home/bticino/bin/coso'
SP=[('actual-main-monitor-request',0x32ec,0x32f4),('monitor-callback-registration',0x58a0,0x5908),('callback-input-and-support',0x5350,0x53ac),('retained-path-match-event-gate',0x53a8,0x53dc),('nonmatch-next-node',0x54d0,0x54f0),('selected-stop-remove-close-return',0x5518,0x55bc)]
G={0x32ec:0xaa1403e0,0x58ac:0xaa0003f3,0x58b0:0xf9400800,0x58b4:0xf9400400,0x58cc:0xb4000160,0x58d0:0xd2800a01,0x58e0:0xaa1303e3,0x58ec:0x52800005,0x58f0:0xd2800004,0x58f8:0x52800000,0x5354:0xaa0403e5,0x5368:0x2a0303f3,0x5388:0xaa0103f8,0x5398:0xf94008b6,0x53a4:0x34000a60,0x53a8:0x71000a7f,0x53b0:0xf94002c0,0x53b8:0xaa0003f4,0x53c0:0xf9400295,0x53c4:0xaa1803e0,0x53cc:0xf94002a1,0x53d4:0x340007e0,0x53d8:0x34000a13,0x54d0:0xf9400694,0x54d4:0xb5fff774,0x555c:0xf94006a0,0x5568:0x910123e2,0x5570:0x34000060,0x5574:0xf94027e0,0x5578:0xd63f0000,0x557c:0xf94002c0,0x5580:0xaa1503e1,0x5588:0xaa0003e1,0x558c:0xf94002a0,0x5590:0xf90002c1,0x5598:0xf94006a0,0x55a0:0xaa1503e0,0x55b8:0xd65f03c0}
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
 assert bl(0x32f0)==0x58a0
 joins=[]
 for a,c,t in [(0x58d8,0x58e4,0x5350),(0x58dc,0x58e8,0x6320),(0x5560,0x5564,0x62b8)]:
  x=u(c);assert x&0xffc00000==0x91000000 and ap(a)+(x>>10&4095)==t;joins.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t)})
 assert raw(0x6320,8)==b'changed\0'and raw(0x62b8,12)==b'stop_plugin\0'
 hp=f.root/f.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);imports=[]
 for pc,plt,name in [(0x58b8,0x2e30,'g_file_new_for_path'),(0x58c8,0x2b80,'g_file_monitor_directory'),(0x58d4,0x2cb0,'g_type_check_instance_cast'),(0x58f4,0x2c90,'g_signal_connect_data'),(0x53a0,0x2d00,'g_module_supported'),(0x53b4,0x2db0,'g_list_first'),(0x53c8,0x2d90,'g_file_get_path'),(0x53d0,0x2e20,'g_str_has_suffix'),(0x556c,0x2c00,'g_module_symbol'),(0x5584,0x2e70,'g_list_remove'),(0x5594,0x28f0,'g_free'),(0x559c,0x2a30,'g_module_close'),(0x55a4,0x28f0,'g_free')]:
  assert bl(pc)==plt;x=u(plt+4);assert x&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220;slot=ap(plt)+(x>>10&4095)*8;r=[z.strip()for z in rels.splitlines()if re.match(r'^[0-9a-fA-F]+\s',z)and int(z.split()[0],16)==slot];assert len(r)==1 and'JUMP_SLOT'in r[0]and r[0].split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'relocation':r[0]})
 out={};sp=[]
 for name,a,e in SP:
  z=raw(a,e-a);t=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=t.encode();sp.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':z.hex(),'sha256':H(z)})
 pins={P:{'size':len(b),'sha256':H(b)}}
 for p in [V,O/'research/2026-11-01-run11-config-selection/REPORT.md',O/'research/2026-11-01-run14-boot-selection/REPORT.md',O/'research/2026-11-01-run14-boot-selection/SOURCE.json',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'size':len(z),'sha256':H(z)}
 out['INPUTS.json']=J(pins);out['SOURCE.json']=J({'image':P,'sha256':H(b),'PT_LOAD':[list(r)for r in L],'spans':sp,'guards':{hex(a):hex(x)for a,x in G.items()},'PIC_joins':joins,'safe_literals':{'0x6320':'changed','0x62b8':'stop_plugin'},'imports':imports,'selected_contract':{'owner_data':'mainM→init_dir_monitoring(M), callbackregistrationuserdataM; underordinarychangedABI callbackX4sameM; P=[M16]','registered_callback':'0x5350, notnearestexportedsymbolname','path_gate':'g_str_has_suffix(g_file_get_path(eventfile),entry0storedpath) nonzero; notcanonicalexactidentity','event':'selectednumericW3=0; no public/deleted-eventmeaningassigned','retained_entry':'node0 entry; entry0path/entry8modulehandle inheritedproduceronlyunderSAMEP/list/validpointee premises','ordering':'stop-symbolrequest(handle), conditionalcallable request; removeentryP0/storehead; freepath; closerequesthandle; freeentry; normalreturn','bodies_opaque':['pluginstop','GModule/GFile/GObject/list/free/log providers','othermoduleupdate/reloadbranches','closedoutput/receiving/transport/auth/session/framing/MQTT/libjel']},'execution':{'original':0,'provider':0,'models':0,'fixtures':0,'target_IO':0}})
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
print(json.dumps({'check':'--check'in sys.argv,'outputs':len(out),'spans':len(SP),'guards':len(G),'PIC_joins':3,'safe_literals':2,'imports':13,'pins':len(json.loads(out['INPUTS.json'])),'first_copies':len(cp),'original_execution':0}))
