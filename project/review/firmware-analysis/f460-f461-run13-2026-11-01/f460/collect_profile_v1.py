#!/usr/bin/env python3
"""Exclusive static local profile-result gate; no environment/provider execution."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse,hashlib,importlib.util,json,os,struct,subprocess
D=Path(__file__).resolve().parent;O=D.parents[1];W=next(p for p in D.parents if(p/'sources').is_dir());V=O/'research/2026-11-01/image_vfs.py';H=lambda b:hashlib.sha256(b).hexdigest();J=lambda x:(json.dumps(x,sort_keys=True,indent=2)+'\n').encode();s=importlib.util.spec_from_file_location('f460_profile_vfs',V);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
P={'exe':'/home/bticino/bin/dedrifupdater','lib':'/usr/lib/libdedrifupdater.so.1.0.0'};E={'exe':'8f32212bee98b507690f1e22d6b26524c8a13dc20efcc8cc05900ac4142f9753','lib':'ccd87b29d164976bb5ab626ead466fb1875854bb2fbb036982d4e3eea9e4cc89'}
SP=[('exe','actual-local-objects-construction',0x2888,0x28bc),('exe','mode-result-branch-and-forward',0x28b8,0x290c),('exe','mode2-diagnostic-bridge',0x2aa0,0x2aac),('lib','provided-platform-constructor-prefix',0x2fe0,0x3008),('lib','selected-constructor-path-field48',0x30e8,0x30f8),('lib','entire-profile-result-getter',0x3200,0x32c8)]
G={'exe':[(0x288c,0x910103f4),(0x2890,0x2a1703e1),(0x2894,0xaa1403e0),(0x2898,0x9101a3f5),(0x28a0,0xaa1503e0),(0x28b8,0xaa1503e0),(0x28c4,0x2a0003f3),(0x28c8,0x7100081f),(0x28d4,0x7100067f),(0x28f8,0x2a1303e1),(0x28fc,0xaa1403e0)],'lib':[(0x2ff0,0xaa0003f3),(0x2ff4,0x2a0103f4),(0x3000,0xb9000a60),(0x30f4,0xf9001a60),(0x3220,0xaa0003f3),(0x3224,0xf9401800),(0x3234,0xf9400000),(0x3238,0xf90003ff),(0x3244,0xf9401a60),(0x3248,0x910003e1),(0x324c,0xd2800003),(0x3250,0xd2800002),(0x3254,0xf9400000),(0x3260,0x52800013),(0x3280,0x2a1303e0),(0x3294,0xd65f03c0),(0x3298,0xf94003e0),(0x32ac,0xf100001f),(0x32b4,0x1a9f07f3),(0x32b8,0x11000673)]}
def build():
 v=m.ImageVFS();B={k:v.read_bytes(p)for k,p in P.items()};assert v.resolve('/usr/lib/libdedrifupdater.so.1')==P['lib'];L={};HP={};rels={};syms={};env=dict(os.environ,DEBUGINFOD_URLS='')
 for k,b in B.items():
  assert H(b)==E[k]and b[:6]==b'\x7fELF\x02\x01'and struct.unpack_from('<H',b,18)[0]==183;ph=struct.unpack_from('<Q',b,32)[0];es,n=struct.unpack_from('<HH',b,54);L[k]=[r for i in range(n)if(r:=struct.unpack_from('<II6Q',b,ph+i*es))[0]==1];HP[k]=v.root/v.resolve(P[k]).lstrip('/');rels[k]=subprocess.check_output(['readelf','-rW',str(HP[k])],text=True,env=env);syms[k]=subprocess.check_output(['readelf','-Ws',str(HP[k])],text=True,env=env)
 def raw(k,a,n):
  r=next(r for r in L[k]if r[3]<=a and a+n<=r[3]+r[5]);p=r[2]+a-r[3];return B[k][p:p+n]
 def u(k,a):return int.from_bytes(raw(k,a,4),'little')
 def bl(k,a):
  x=u(k,a);assert x&0xfc000000==0x94000000;i=x&0x3ffffff;return a+((i-0x4000000 if i&0x2000000 else i)<<2)
 def ap(k,a):
  x=u(k,a);assert x&0x9f000000==0x90000000;i=((x>>5)&0x7ffff)<<2|(x>>29&3);return(a&~4095)+((i-0x200000 if i&0x100000 else i)<<12)
 for k,g in G.items():
  for a,w in g:assert u(k,a)==w,(k,hex(a),hex(u(k,a)),hex(w))
 out={};ss=[]
 for k,name,a,e in SP:
  z=subprocess.check_output(['objdump','-d','-m','aarch64','--dwarf=no-follow-links',f'--start-address={a}',f'--stop-address={e}',str(HP[k])],text=True,env=env).replace(str(HP[k]),P[k]);out['spans/'+name+'.txt']=z.encode();ss.append({'input':k,'name':name,'start_VA':hex(a),'end_VA_exclusive':hex(e),'bytes_hex':raw(k,a,e-a).hex(),'sha256':H(raw(k,a,e-a))})
 def rr(k,a):return next(s.strip()for s in rels[k].splitlines()if s.startswith(f'{a:016x} '))
 imports=[]
 for k,pc,plt,slot,name in[('exe',0x28a8,0x2780,0x19fb8,'_ZN8PlatformC1Ei'),('exe',0x28bc,0x22f0,0x19d70,'_ZN8Platform16get_working_modeEv'),('exe',0x2900,0x2550,0x19ea0,'_ZN13StatusMachine9next_stepE11WorkingMode'),('lib',0x2ff8,0x2920,0x16f98,'_ZN8Platform20get_running_platformEv'),('lib',0x30f0,0x25a0,0x16dd8,'g_string_new'),('lib',0x323c,0x26e0,0x16e78,'stat@GLIBC_2.33'),('lib',0x3258,0x2740,0x16ea8,'g_file_get_contents'),('lib',0x32a8,0x2730,0x16ea0,'g_strrstr'),('lib',0x32bc,0x2770,0x16ec0,'g_free')]:
  assert bl(k,pc)==plt;z=u(k,plt+4);assert z&0xffc00000==0xf9400000 and u(k,plt+12)==0xd61f0220 and ap(k,plt)+((z>>10)&4095)*8==slot;r=rr(k,slot);assert'R_AARCH64_JUMP_SLOT'in r and r.split()[-3]==name;imports.append({'input':k,'call':hex(pc),'PLT':hex(plt),'slot':hex(slot),'PLT_bytes':raw(k,plt,16).hex(),'relocation':r})
 literals=[]
 for a,c,t,text in[(0x30e8,0x30ec,0x4ac8,'/var/tmp/dedrifu_env.txt'),(0x32a0,0x32a4,0x4c08,'MYRECOVERY=y')]:
  x=u('lib',c);assert x&0xffc00000==0x91000000 and ap('lib',a)+(x>>10&4095)==t and raw('lib',t,len(text)+1)==text.encode()+b'\0';literals.append({'ADRP':hex(a),'ADD':hex(c),'target':hex(t),'value':text})
 assert u('lib',0x3240)==0x37f80100 and u('lib',0x325c)==0x350001e0 and u('lib',0x329c)==0xb4fffe20 and u('exe',0x28d0)==0x54000e80
 x=u('exe',0x2aa8);i=x&0x3ffffff;assert x&0xfc000000==0x14000000 and 0x2aa8+((i-0x4000000 if i&0x2000000 else i)<<2)==0x28ec
 defs={}
 for name,a in[('_ZN8PlatformC1Ei',0x2fe0),('_ZN8Platform16get_working_modeEv',0x3200)]:
  r=[z.strip()for z in syms['lib'].splitlines()if z.split()and z.split()[-1]==name];assert r and all(int(z.split()[1],16)==a for z in r);defs[name]=r
 dyn=subprocess.check_output(['readelf','-dW',str(HP['exe'])],text=True,env=env);assert'Shared library: [libdedrifupdater.so.1]'in dyn
 pins={P[k]:{'bytes':len(b),'sha256':H(b),'resolved':v.resolve(P[k])}for k,b in B.items()}
 for p in[V,O/'research/2026-11-01-run08-update/REPORT.v3.md',O/'research/2026-11-01-run12-update-consumer/REPORT.md',W/'OpenWebNet-Encyclopedia/devices/definitions/own-dev-0207-f460-myhome-server.md']:
  z=p.read_bytes();pins[str(p.relative_to(W))]={'bytes':len(z),'sha256':H(z)}
 out['SOURCE.json']=J({'images':{k:{'path':P[k],'sha256':E[k],'PT_LOAD':[list(r)for r in L[k]]}for k in B},'spans':ss,'guards':{k:[{'VA':hex(a),'word':hex(w)}for a,w in g]for k,g in G.items()},'imports':imports,'literal_joins':literals,'candidate_definitions':defs,'binding':'executableDTNEEDEDlibdedrifupdater.so.1 and metadataalias1→1.0.0; activebinding/interposition remainsconditional','contract':{'Platform':'actualprovidedconstructoraddressSP104; selectednormalctorpathstoresnewGStringatobject48','getter':'statnegative→0; contentsfalse/null→0; g_strrstr compiledmarker nonnull→2,otherwise1','caller':'samePlatformSP104→getter; returnedW0retainedW19; cmp2diagnosticbranch; W1mode toStatusMachineSP64 next_step request','separate_domains':['PlatformSP104','StatusMachineSP64','mode0/1/2','XMLstatus4','recordkind2'],'limits':'No targetenvfile read; get_running_platform/next_step andallupdate/extraction/flash/mount/reboot/providers opaque'},'new_original_execution':0,'models_fixtures':0})
 out['INPUTS.json']=J(pins);out['OUTPUT_MANIFEST.json']=J({'collector_sha256':H(Path(__file__).read_bytes()),'report_sha256':H((D/'REPORT.md').read_bytes()),'outputs':{n:{'bytes':len(z),'sha256':H(z)}for n,z in out.items()},'counts':{'spans':len(SP),'guards':sum(map(len,G.values())),'imports':len(imports),'literal_joins':len(literals),'inputs':len(pins),'original_execution':0}});return out

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
 print(json.dumps({'check':ck,'outputs':len(o),'spans':len(SP),'guards':sum(map(len,G.values())),'original_execution':0}))
if __name__=='__main__':main()
