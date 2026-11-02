#!/usr/bin/env python3
"""Exclusive F461 typed context/suffix source; no firmware/provider/model execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import struct,json,hashlib,importlib.util,subprocess,re,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=W/'work/f461-firmware/2.0.11';V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode()
s=importlib.util.spec_from_file_location('suffix_vfs',V);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
P='/home/bticino/libcoso/libplug_automation_tr.so'
SP=[('record-to-provided-parsed-object',0x3b8c,0x3bc8),('provided-string-context',0x4024,0x40c8),('inherited-prefix-return-connector',0x56bc,0x56c4),('suffix-selection-and-append',0x4404,0x4454),('local-free-to-address-component',0x4138,0x4174),('formatter-return-store-boundary',0x4174,0x41ac)]
G={0x400c:0xb9400762,0x4018:0xb9006be2,0x4060:0x35003c80,0x406c:0x54006480,0x3b8c:0xb9403a63,0x3b98:0x71000c7f,0x3ba0:0xf9400260,0x3ba4:0xf9004fe0,0x3ba8:0xb9406803,0x4024:0xf9404fe1,0x4028:0xf940103b,0x402c:0xa9435037,0x4068:0x7100105f,0x4078:0xaa1403e0,0x4084:0x2a0003e1,0x4090:0xaa0003f9,0x40a8:0x52800014,0x56bc:0xf94043e4,0x56c0:0x17fffb51,0x4404:0xf100033f,0x4414:0x9a99037b,0x4418:0xaa1903e0,0x4420:0x7100001f,0x4424:0xf9403be0,0x4428:0x7a400a84,0x442c:0xaa1b03e2,0x4430:0x9103e003,0x443c:0x9a831003,0x4440:0xaa1803e0,0x4450:0x17ffff3a,0x416c:0xf9400317,0x4180:0xaa1703e1,0x4198:0xf90002a0,0x41a0:0x910283e0}
def build():
 f=v.ImageVFS();b=f.read_bytes(P);assert H(b)=='d7d361798ccec65843bd41c9ad7b8897645a334b0cd08121d372949f78eac277' and struct.unpack_from('<H',b,18)[0]==183
 ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L=[q for i in range(n)if(q:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1]
 def raw(a,n):
  q=next(q for q in L if q[3]<=a and a+n<=q[3]+q[5]);o=q[2]+a-q[3];return b[o:o+n]
 def u(a):return int.from_bytes(raw(a,4),'little')
 def ap(a):
  x=u(a);assert x&0x9f000000==0x90000000;i=((x>>5&0x7ffff)<<2)|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def bl(a):
  x=u(a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 for a,x in G.items():assert u(a)==x,(hex(a),hex(u(a)))
 literals=[]
 for a,c,t,reg,text in [(0x3ff8,0x4058,0x60f8,1,'4'),(0x4080,0x4088,0x6608,0,'%X'),(0x4408,0x440c,0x6038,27,'0'),(0x43c8,0x4410,0x6228,1,'F'),(0x4434,0x4438,0x61c8,0,'3'),(0x4444,0x4448,0x66d0,1,'%s1%s'),(0x4188,0x418c,0x6708,0,'%s%s%s%s')]:
  x=u(c);assert x&0xffc00000==0x91000000 and x&31==reg;assert ap(a)+(x>>10&4095)==t;assert raw(t,len(text)+1)==text.encode()+b'\0';literals.append({'ADRP':hex(a),'ADD':hex(c),'literal_VA':hex(t),'value':text,'ADDword':hex(x)})
 # X4 is reloaded at56bc from SP128 saved on the inherited D1 prefix; X0 base6000 is reloaded from SP112.
 assert u(0x4004)==0xf9003be1 and u(0x43dc)==0xf90043e4
 hp=f.root/f.resolve(P).lstrip('/');env=dict(os.environ,DEBUGINFOD_URLS='');rels=subprocess.check_output(['readelf','-rW',str(hp)],text=True,env=env);imports=[]
 for pc,plt,name in [(0x405c,0x2040,'g_strcmp0'),(0x407c,0x1ff0,'g_ascii_strtoll'),(0x408c,0x1e20,'g_strdup_printf'),(0x4098,0x1df0,'g_strdup'),(0x40aC,0x1df0,'g_strdup'),(0x40b8,0x1df0,'g_strdup'),(0x40c4,0x1fe0,'automation_get_where_type'),(0x441c,0x2040,'g_strcmp0'),(0x444c,0x2000,'g_string_append_printf'),(0x4190,0x1e20,'g_strdup_printf'),(0x41a8,0x1d50,'prepare_extscs_frames')]:
  assert bl(pc)==plt;x=u(plt+4);assert x&0xffc00000==0xf9400000 and u(plt+12)==0xd61f0220;slot=ap(plt)+(x>>10&4095)*8;rs=[z.strip()for z in rels.splitlines()if re.match(r'^[0-9a-fA-F]+\s',z)and int(z.split()[0],16)==slot];assert len(rs)==1 and'JUMP_SLOT'in rs[0]and rs[0].split()[-3]==name;imports.append({'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'relocation':rs[0],'boundary_only':pc==0x41a8})
 out={};ss=[]
 for name,a,e in SP:
  z=raw(a,e-a);t=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(hp)],text=True,env=env).replace(str(hp),P);out['spans/'+name+'.txt']=t.encode();ss.append({'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':z.hex(),'sha256':H(z)})
 pins={P:{'size':len(b),'sha256':H(b)}}
 for p in [V,O/'research/2026-11-01-run06-address/REPORT.md',O/'research/2026-11-01-run06-address/SOURCE.json',O/'research/2026-11-01-run03-translator-dispatch/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'size':len(z),'sha256':H(z)}
 out['INPUTS.json']=J(pins);out['SOURCE.json']=J({'image':P,'sha256':H(b),'PT_LOAD':[list(q)for q in L],'spans':ss,'guards':{hex(a):hex(x)for a,x in G.items()},'literal_joins':literals,'imports':imports,'flags':{'CCMP_VA':'0x4428','word':'0x7a400a84','condition':'EQ','false_NZCV':4,'false_Z':1,'true_compare':'W20 minus0','CSEL_VA':'0x443c','condition':'NE','NE_value':'literal3','otherwise':'literal4','selected_prior_store_W20':'0x40a8 constant0'},'opaque_boundary':'0x41a8 prepare_extscs_frames body closed; no raw/frame/delivery claims','premises':'local caller reached with valid same objects, prior normal provider returns; prefix path retains W20=0, source/provided object fields and actual routing/parser acceptance unobserved','execution':{'original':0,'models':0,'fixtures':0,'target_IO':0}})
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
print(json.dumps({'check':'--check'in sys.argv,'outputs':len(out),'spans':len(SP),'guards':len(G),'literals':7,'imports':11,'inputs':len(json.loads(out['INPUTS.json'])),'copies':len(cp),'original_execution':0}))
