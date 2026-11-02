from pathlib import Path
import json,struct,hashlib,importlib.util,sys
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;W=O.parents[4];p=W/'work/myhomeserver1-firmware/3.87.13/research/2026-10-31/image_vfs.py';s=importlib.util.spec_from_file_location('state_parent_vfs',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
b=m.ImageVFS().read_bytes('/home/bticino/scheduling_manager/scheduling_manager');sha=hashlib.sha256(b).hexdigest();assert sha=='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
ph=struct.unpack_from('<I',b,28)[0];ps,pn=struct.unpack_from('<HH',b,42);ls=[struct.unpack_from('<8I',b,ph+i*ps)for i in range(pn)];ls=[q for q in ls if q[0]==1]
def at(a,n):
 q=next(q for q in ls if q[2]<=a and a+n<=q[2]+q[4]);x=q[1]+a-q[2];return b[x:x+n]
def word(a):return struct.unpack('<I',at(a,4))[0]
rows=[]
for pool,pc in[(0xd01ac,0xcf648),(0xd01b0,0xcf656),(0xce890,0xcdda8)]:
 a=(word(pool)+pc+4)&0xffffffff;assert a==0x167808;rows.append({'pool':hex(pool),'ADD_PC':hex(pc),'linked_global':hex(a)})
g=0x167808;q=next(q for q in ls if q[2]<=g<q[2]+q[5]);assert g>=q[2]+q[4]
t=word(0x166eb4);assert t==0x16216c and word(t+8)==2 and word(t+12)==0x1362d4 and at(0x1362d4,3)==b'on\0'
r={'scope':'Parent readonly verification of already-reviewed exact PICglobal equality/memory-only location and selectedstatus table row; no runtime content read or supplied','image_sha256':sha,'global_PIC':rows,'memory_only_global':hex(g),'selected_table':hex(t),'selected_row':1,'string':'on','new_execution_models_fixtures':0};raw=(json.dumps(r,indent=2)+'\n').encode()
if '--check'in sys.argv:assert(O/'PARENT_SOURCE_SPOTCHECK.json').read_bytes()==raw
else:(O/'PARENT_SOURCE_SPOTCHECK.json').open('xb').write(raw)
print(json.dumps({'global_joins':3,'selected_table_rows':1,'original_execution':0}))
