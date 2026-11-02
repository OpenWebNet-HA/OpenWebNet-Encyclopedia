#!/usr/bin/env python3
"""Exclusive static F461 deferred-record scheduling/clock source, no execution/models."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json,struct,hashlib,importlib.util,subprocess,re,os
D=Path(__file__).resolve().parent;W=next(p for p in D.parents if(p/'sources').is_dir());O=W/'work/f461-firmware/2.0.11';V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,indent=2,sort_keys=True)+'\n').encode();s=importlib.util.spec_from_file_location('clock_vfs',V);v=importlib.util.module_from_spec(s);s.loader.exec_module(v)
PATHS={'exe':'/home/bticino/bin/coso','glib':'/usr/lib/libglib-2.0.so.0.7200.3'}
SP=[('provided-owner-and-list','exe',0x3df0,0x3e14),('local-min-initialization','exe',0x3e68,0x3e90),('unsigned-due-min-and-branch','exe',0x3e94,0x3ef4),('signed-delta-source-requests-return','exe',0x40e8,0x4164),('same-data-callback-reentry','exe',0x4170,0x4180),('candidate-realtime-provider','glib',0x570e0,0x57150),('candidate-interval-field-request','glib',0x592d0,0x59320),('candidate-ready-helper-flag-gate','glib',0x55a40,0x55a60),('candidate-ready-helper-factor1000','glib',0x55ae8,0x55b08)]
G={'exe':{0x3dfc:0xaa0003f3,0x3e08:0xf9003be2,0x3e70:0xf9003fff,0x3e78:0xa94783f6,0x3e94:0xf940029c,0x3e98:0xf9401393,0x3ea0:0x91002800,0x3ea4:0xeb00027f,0x3ea8:0x54000269,0x3eac:0xf9401380,0x3eb0:0xb4000096,0x3eb8:0xeb00003f,0x3ebc:0x54000049,0x3ec0:0xf9003fe0,0x3ed0:0xb5001000,0x40f0:0xcb000038,0x4104:0x9b407f00,0x4108:0x9347fc00,0x410c:0xcb98fc00,0x4118:0xd2800003,0x411c:0xf9403be2,0x4120:0xaa0003f3,0x4124:0xf947c421,0x4130:0xaa0003e1,0x4144:0x52800000,0x4160:0xd65f03c0,0x4170:0xaa0003e2,0x4174:0xd2800001,0x4178:0x91022000,0x417c:0x17ffff1d},'glib':{0x570ec:0xd2800001,0x570f0:0x910023e0,0x57110:0xa9408be0,0x57118:0xd2884803,0x5711c:0xf2a001e3,0x57124:0x9b030800,0x592e4:0x2a0003f4,0x592f4:0xb9006014,0x55a58:0xb9406400,0x55a5c:0x34000460,0x55ae8:0xb9406262,0x55aec:0x52807d00,0x55af0:0x9ba00441}}
def build():
 f=v.ImageVFS();B={k:f.read_bytes(p)for k,p in PATHS.items()};assert H(B['exe'])=='2fb47ebfb8e63df22053a5ca95b08183a11ab93b248dcbc2b2d7a5f682561197';assert f.resolve('/usr/lib/libglib-2.0.so.0')==PATHS['glib'];M={};HP={};rels={};symbols={};env=dict(os.environ,DEBUGINFOD_URLS='')
 for k,b in B.items():
  assert b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183;ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);M[k]=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1];HP[k]=f.root/f.resolve(PATHS[k]).lstrip('/');rels[k]=subprocess.check_output(['readelf','-rW',str(HP[k])],text=True,env=env);symbols[k]=subprocess.check_output(['readelf','-Ws',str(HP[k])],text=True,env=env)
 def raw(k,a,n):
  r=next(r for r in M[k]if r[3]<=a and a+n<=r[3]+r[5]);o=r[2]+a-r[3];return B[k][o:o+n]
 def u(k,a):return int.from_bytes(raw(k,a,4),'little')
 def ap(k,a):
  x=u(k,a);assert x&0x9f000000==0x90000000;i=((x>>5&0x7ffff)<<2)|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 def bl(k,a):
  x=u(k,a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 def rr(k,a):
  r=[r.strip()for r in rels[k].splitlines()if re.match(r'^[0-9a-fA-F]+\s',r)and int(r.split()[0],16)==a];assert len(r)==1;return r[0]
 for k,gd in G.items():
  for a,x in gd.items():assert u(k,a)==x,(k,hex(a),hex(u(k,a)))
 for a,w in [(0x40f4,0xd29ef9e0),(0x40f8,0xf2bc6a60),(0x40fc,0xf2d374a0),(0x4100,0xf2e41880)]:assert u('exe',a)==w
 callback=rr('exe',0x16f88);assert'RELATIVE'in callback and callback.split()[-1]=='4170'
 # The callback pointer is read through its actual virtual-address PT_LOAD mapping.
 assert int.from_bytes(raw('exe',0x16f88,8),'little')==0x4170
 imports=[]
 for k,pc,plt,name in [('exe',0x3e9c,0x2ee0,'g_get_real_time'),('exe',0x40e8,0x2ee0,'g_get_real_time'),('exe',0x4110,0x2c80,'g_timeout_source_new'),('exe',0x4128,0x29e0,'g_source_set_callback'),('exe',0x412c,0x2920,'get_main_context'),('exe',0x4138,0x2de0,'g_source_attach'),('exe',0x4140,0x2d80,'g_source_unref'),('glib',0x5710c,0x1d0b0,'gettimeofday@GLIBC_2.17')]:
  assert bl(k,pc)==plt;x=u(k,plt+4);assert x&0xffc00000==0xf9400000 and u(k,plt+12)==0xd61f0220;slot=ap(k,plt)+(x>>10&4095)*8;r=rr(k,slot);assert'JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'input':k,'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'relocation':r})
 for a,t in [(0x592f0,0x54d20),(0x592fc,0x571d0),(0x59308,0x55a40)]:assert bl('glib',a)==t
 defs={}
 for name,a in [('g_get_real_time',0x570e0),('g_timeout_source_new',0x592d0)]:
  r=[r.strip()for r in symbols['glib'].splitlines()if re.search(r'\b'+name+r'$',r)];assert r and all(f'{a:016x}'in z for z in r);defs[name]=r
 out={};ss=[]
 for name,k,a,e in SP:
  z=raw(k,a,e-a);t=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(HP[k])],text=True,env=env).replace(str(HP[k]),PATHS[k]);out['spans/'+name+'.txt']=t.encode();ss.append({'name':name,'input':k,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':z.hex(),'sha256':H(z)})
 pins={PATHS[k]:{'size':len(b),'sha256':H(b)}for k,b in B.items()}
 for p in [V,O/'research/2026-11-01-run03-translator-dispatch/REPORT.md',O/'research/2026-11-01-run03-translator-dispatch/SOURCE.json',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0208-f461-myhome-server-third-party-integration.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'size':len(z),'sha256':H(z)}
 out['INPUTS.json']=J(pins);out['SOURCE.json']=J({'paths':PATHS,'PT_LOAD':{k:[list(r)for r in l]for k,l in M.items()},'spans':ss,'guards':{k:{hex(a):hex(x)for a,x in g.items()}for k,g in G.items()},'imports':imports,'candidate_definitions':defs,'callback':{'slot':'0x16f88','target':'0x4170','relocation':callback,'data':'same supplied third argument savedSP112; callbackX0→X2, X0+136→list-address, X1=0; tail3df0'},'source_arithmetic':{'field_offset':32,'field_width_bytes':8,'due_gate':'unsigned64 field <= freshclock+10','deferred_local_min':'SP120 initial0, replace with smaller deferred field under unsigned comparison','delta':'SUB64(minimum,newclock), signed interpretation for next operations; no positive/nooverflow guarantee','reciprocal_hex':'0x20c49ba5e353f7cf','quotient_sequence':'SMULH signed64; ASR7; subtract(delta ASR63)','interval_argument':'low32 passed by candidate g_timeout_source_new W0→field96','producer_of_nonzero_message_field32':'OPEN; timestamp24 is separate'},'provider_scope':{'real_time':'gettimeofday request then pairword0*1000000+pairword1; ordinary successful AArch64 timevalABI required','timeout':'W0 saved32→field96; separate g_get_monotonic_time request; helper flag100==0 branch forms now+1000*unsignedfield96 then tail g_source_set_ready_time','excluded':'OS/gettimeofday, monotonic clock, source dispatch/attach/readiness implementations remain opaque; no provider execution'},'execution':{'original':0,'provider':0,'models':0,'fixtures':0,'target_IO':0}})
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
print(json.dumps({'check':'--check'in sys.argv,'outputs':len(out),'spans':len(SP),'guards':sum(map(len,G.values())),'reciprocal_words':4,'imports':8,'pins':len(json.loads(out['INPUTS.json'])),'first_copies':len(cp),'original_execution':0}))
