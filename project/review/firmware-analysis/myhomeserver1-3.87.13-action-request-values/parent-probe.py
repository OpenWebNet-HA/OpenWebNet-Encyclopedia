from pathlib import Path
import json,struct,hashlib,importlib.util,sys
sys.dont_write_bytecode=True
O=Path(__file__).resolve().parent;W=O.parents[4]
p=W/'work/myhomeserver1-firmware/3.87.13/research/2026-10-31/image_vfs.py'
s=importlib.util.spec_from_file_location('parent_values_vfs',p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
b=m.ImageVFS().read_bytes('/home/bticino/scheduling_manager/scheduling_manager');sha=hashlib.sha256(b).hexdigest();assert sha=='7d748f49f55a2fe788a6797fd59eef90e79e417f9b309f39e58207a52504da26'
ph=struct.unpack_from('<I',b,28)[0];ps,pn=struct.unpack_from('<HH',b,42);ls=[struct.unpack_from('<8I',b,ph+i*ps)for i in range(pn)];ls=[q for q in ls if q[0]==1]
def at(a,n):
 q=next(q for q in ls if q[2]<=a and a+n<=q[2]+q[4]);x=q[1]+a-q[2];return b[x:x+n]
def word(a):return struct.unpack('<I',at(a,4))[0]
rows=[]
for pool,pc,expected in [(0xd22b0,0xd20e8,'2.0'),(0xd22c0,0xd2170,'light.setStatus'),(0xd1950,0xd1780,'id'),(0xd1944,0xd1694,'status')]:
 a=(word(pool)+pc+4)&0xffffffff;actual=at(a,len(expected)+1);assert actual==expected.encode()+b'\0';rows.append({'pool_VA':hex(pool),'ADD_PC':hex(pc),'literal_VA':hex(a),'literal':expected,'literal_bytes_sha256':hashlib.sha256(actual).hexdigest()})
result={'scope':'Parent independent source PIC literal check only; imported providers and field-to-params join are independent review obligations','image_sha256':sha,'PIC_literals':rows,'new_original_execution_fixtures_models':0}
raw=(json.dumps(result,indent=2)+'\n').encode()
if '--check'in sys.argv:assert(O/'PARENT_SOURCE_SPOTCHECK.json').read_bytes()==raw
else:(O/'PARENT_SOURCE_SPOTCHECK.json').open('xb').write(raw)
print(json.dumps({'PIC_literals':len(rows),'new_execution':0,'check':'--check'in sys.argv}))
