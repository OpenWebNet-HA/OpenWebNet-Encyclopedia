#!/usr/bin/env python3
"""Execute pinned generic-script helpers in a synthetic Qt harness; no hardware."""
import subprocess,pathlib,json,hashlib,shutil,argparse,shlex
p=argparse.ArgumentParser();p.add_argument("--repositories",type=pathlib.Path,required=True);p.add_argument("--work",type=pathlib.Path,required=True);p.add_argument("--qt-prefix",type=pathlib.Path,required=True);a=p.parse_args()
if a.work.resolve().is_relative_to(a.repositories.resolve()):raise SystemExit("Scratch output must be outside preserved repositories")
B=a.work;B.mkdir(parents=True,exist_ok=True);S=B/'src';S.mkdir(exist_ok=True);H=B/'shim';H.mkdir(exist_ok=True)
pin='4f93f44ee5ec7f89a3de9e040141755c847a5eda';repo=str(a.repositories/'MyHomeSystemEmulator.git');artifacts=[]
files=['bt_GEN_DEV_PGIN/genmsgworker.cpp','bt_GEN_DEV_PGIN/genmsgworker.h','bt_GEN_DEV_PGIN/gen_xmlserializer.cpp','bt_GEN_DEV_PGIN/gen_xmlserializer.h','bt_GEN_DEV_PGIN/action.h','bt_GEN_DEV_PGIN/message.h','bt_GEN_DEV_PGIN/scenario.h','libplant/plantmessage.cpp','libplant/plantmessage.h','libplant/libplant_global.h','libplant/eventhandler.h','libplant/syserror.h']
for path in files:
 raw=subprocess.check_output(['git','--git-dir='+repo,'show',pin+':'+path]);(S/pathlib.Path(path).name).write_bytes(raw);artifacts.append(dict(path=path,sha256=hashlib.sha256(raw).hexdigest(),git_blob=subprocess.check_output(['git','--git-dir='+repo,'rev-parse',pin+':'+path]).decode().strip()))
(H/'bt_gen_dev.h').write_text('#include <QString>\nclass BtGEN_dev { public: static QString className(){return "synthetic-class";} };\n')
(H/'plantmgr.h').write_text('#include <QString>\nclass PlantMgr { public: static PlantMgr& getInstance(){static PlantMgr p;return p;} QString getBuses(){return "synthetic-bus";} };\n')
(S/'harness.cpp').write_text(r'''
#include <QCoreApplication>
#include <QDomDocument>
#include <QDebug>
#include <gen_xmlserializer.h>
#include <genmsgworker.h>
#include <cstdio>
#include <cstdlib>
struct H : EventHandler { QList<QByteArray> events; void handleEvent(CMD_PRIO,const QByteArray& b){events<<b;} };
void need(bool b){if(!b)std::abort();}
QDomDocument doc(const QString& s){QDomDocument d;need(d.setContent(s));return d;}
int main(int argc,char**argv){ QCoreApplication app(argc,argv);
 if(argc>1){Message m;m.setMsgValue("[1..2]");m.getMsgValue(0);return 3;}
 QMap<QString,QSharedPointer<Scenario>> map;SysError err;
 auto xml=doc("<Root><Scenario descr='first'><Trigger><Message value='synthetic-trigger' chan='MON'/></Trigger><Action from='2' repeat='3'><Message chan='CMD' value='synthetic-[index]' delay='0'/><Message chan='MON' value='monitor-[index]' delay='0'/><Message chan='GUI' value='gui-[index]' delay='0'/><Message chan='UNKNOWN' value='unused' delay='0'/></Action></Scenario></Root>");
 GEN_xmlserializer::loadScenarios(xml,map,err);need(map.size()==1);
 H handler;PlantMessage input;input.setId(42);input.setSourceAddr(qMakePair(QString("synthetic-origin"),QString("synthetic-channel")));
 GenMsgWorker worker(&handler,map["synthetic-trigger"],input);QList<PlantMessage> outputs;
 QObject::connect(&worker,&GenMsgWorker::ReleaseResponse,[&](QObject* o){auto p=dynamic_cast<PlantResponse*>(o);need(p);outputs<<p->getRspMessage();delete p;});
 worker.run();need(outputs.size()==4&&handler.events.size()==2);
 need(outputs[0].getValue(PlantMessage::OPEN)=="synthetic-2");need(outputs[2].getValue(PlantMessage::OPEN)=="synthetic-3");
 need(outputs[0].getDestAddr()==input.getSourceAddr());need(outputs[1].getDestAddr()==qMakePair(PlantMessage::INTERNAL,PlantMessage::GATEWAY));
 need(outputs[1].getId()==42&&outputs[3].getId()==42);need(handler.events[0]=="gui-2");
 auto reload=doc("<Root><Scenario descr='replacement'><Trigger><Message value='new-trigger'/></Trigger></Scenario><Scenario descr='last'><Trigger><Message value='new-trigger'/></Trigger></Scenario></Root>");
 GEN_xmlserializer::loadScenarios(reload,map,err);need(map.size()==2);need(map.contains("synthetic-trigger"));need(map["new-trigger"]->getName()=="last");
 Message m;m.setMsgValue("synthetic-[2..4]-[index]");auto ranged=m.getMsgValue(7);need(ranged.endsWith("-7"));int value=ranged.section('-',1,1).toInt();need(value>=2&&value<=4);
 QDomDocument saved;GEN_xmlserializer::serialize("synthetic-id","synthetic-bus","synthetic-script",saved,err);
 need(saved.documentElement().elementsByTagName("Scenario").isEmpty());need(saved.toString().contains("synthetic-script"));
 puts("PASS original worker: inclusive loop, channel destinations, GUI sink and unknown-channel discard; original loader: stale triggers and last duplicate; original range substitution; configuration saves a script reference");
}
''')
for n in ['genmsgworker.h']:
 subprocess.run(['moc-qt5',str(S/n),'-o',str(S/('moc_'+n.replace('.h','.cpp')))],check=True,capture_output=True)
flags=shlex.split(subprocess.check_output(['pkg-config','--cflags','--libs','Qt5Core'],text=True))
flags += ['-I'+str(a.qt_prefix/'usr/include/qt5'),'-I'+str(a.qt_prefix/'usr/include/qt5/QtXml'),'-l:libQt5Xml.so.5']
cmd=['g++','-std=c++17','-fPIC','-include','QDebug','-I'+str(H),'-I'+str(S),str(S/'harness.cpp'),str(S/'gen_xmlserializer.cpp'),str(S/'genmsgworker.cpp'),str(S/'plantmessage.cpp'),str(S/'moc_genmsgworker.cpp'),'-o',str(B/'helper')]+flags
p=subprocess.run(cmd,capture_output=True,text=True);(B/'compile.log').write_text(p.stdout+p.stderr)
if p.returncode:print(p.stderr[-5000:]);raise SystemExit(p.returncode)
p=subprocess.run([str(B/'helper')],capture_output=True,text=True,timeout=5);(B/'run.log').write_text(p.stdout+p.stderr);print(p.stdout);p.check_returncode()
try:subprocess.run([str(B/'helper'),'leading-range'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,timeout=1);raise AssertionError('Expected nonprogressing original range loop')
except subprocess.TimeoutExpired:print('PASS leading numeric range: controlled process does not terminate within one-second bound and is killed')
record=dict(schema_version='1.0',helper_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],qt=subprocess.check_output(['pkg-config','--modversion','Qt5Core'],text=True).strip(),repository='MyOpenCommunity/MyHomeSystemEmulator',revision=pin,method='helper_execution',conditions=['Native Qt 5.15.19 Core/Xml on Linux; unchanged original files recorded by Git blob and SHA-256.','Original GenMsgWorker::run invoked synchronously; no worker scheduling, plant bus, gateway, plugin loader, physical Device or hardware executes.','Synthetic XML, trigger strings and destinations; all message delays zero. EventHandler records GUI requests.','BtGEN_dev className and PlantMgr getBuses are substitutes used only by configuration serialization; original dispatcher BtGEN_dev is source-inspected, not executed.','One leading numeric range runs in an isolated subprocess; nontermination is measured only to a one-second bound, then the subprocess is killed.'],artifacts=artifacts,results=[dict(name='script-loading-and-worker',result='passed inclusive indices, four command/monitor responses, two GUI sink calls, unknown-channel discard, duplicate replacement, retained old trigger, valid range and saved reference'),dict(name='leading-numeric-range',result='subprocess exceeded one-second bound; killed; no universal timing claim')])
(B/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
