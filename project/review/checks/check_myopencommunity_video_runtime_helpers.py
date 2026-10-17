#!/usr/bin/env python3
"""Extract original archived bodies and compile disposable controlled Qt experiments."""
import argparse,hashlib,json,pathlib,re,subprocess
p=argparse.ArgumentParser();p.add_argument('--repositories',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);p.add_argument('--qt-prefix',type=pathlib.Path,required=True);a=p.parse_args()
root=a.repositories.resolve();out=a.output.resolve()
if root==out or root in out.parents:raise ValueError('output must be outside repositories')
out.mkdir(parents=True,exist_ok=True)
pins={'BtExperience':'b88cdac9665d28494f19d6a5d759acf8d5f00ad9','libqtcommon':'825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2','libqtdevices':'736f41c4df17d8782f15b441c59bdf72a56f56ed'}
records=[]
def original(repo,path,symbol):
 data=subprocess.check_output(['git','--git-dir='+str(root/(repo+'.git')),'show',pins[repo]+':'+path]);s=data.decode()
 masked=re.sub(r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'',lambda m:''.join('\n' if c=='\n' else ' ' for c in m[0]),s)
 hit=re.search(r'^([^\n;{}]*?\b'+re.escape(symbol)+r'\s*\([^;{}]*\)[^;{}]*?)\{',masked,re.M)
 if not hit:raise ValueError(symbol)
 start=hit.start();i=hit.end();depth=1
 while depth:depth+=(masked[i]=='{')-(masked[i]=='}');i+=1
 body=s[start:i];blob=subprocess.check_output(['git','--git-dir='+str(root/(repo+'.git')),'rev-parse',pins[repo]+':'+path]).decode().strip()
 rec={'repository':'MyOpenCommunity/'+repo,'revision':pins[repo],'path':path,'symbol':symbol,'git_blob':blob,'file_sha256':hashlib.sha256(data).hexdigest(),'start_line':s[:start].count('\n')+1,'end_line':s[:i].count('\n')+1,'body_sha256':hashlib.sha256(body.encode()).hexdigest()}
 if rec not in records:records.append(rec)
 return body
files=[];results=[]
def copy(repo,path,name=None):
 data=subprocess.check_output(['git','--git-dir='+str(root/(repo+'.git')),'show',pins[repo]+':'+path]);dest=out/(name or pathlib.Path(path).name);dest.write_bytes(data)
 files.append({'repository':'MyOpenCommunity/'+repo,'revision':pins[repo],'path':path,'git_blob':subprocess.check_output(['git','--git-dir='+str(root/(repo+'.git')),'rev-parse',pins[repo]+':'+path]).decode().strip(),'sha256':hashlib.sha256(data).hexdigest(),'line_count':len(data.splitlines())})
 return dest
flags=subprocess.check_output(['pkg-config','--cflags','--libs','Qt5Core','Qt5Network']).decode().split()
for m in ['Concurrent','Xml','Test']:
 flags+=['-I'+str(a.qt_prefix/'usr/include/qt5'/('Qt'+m)),str(pathlib.Path('/usr/lib64')/('libQt5'+m+'.so.5'))]
flags+=['-I'+str(a.qt_prefix/'usr/include/qt5'),'-I'+str(out)]
def moc(name):subprocess.run(['moc-qt5',str(out/name),'-o',str(out/('moc_'+pathlib.Path(name).stem+'.cpp'))],check=True)
def execute(name,sources,extra=(),timeout=40):
 cmd=['g++','-std=c++17','-fPIC','-O0','-g','-pthread',*[str(out/s) for s in sources],'-o',str(out/name),*flags,*extra]
 c=subprocess.run(cmd,capture_output=True,text=True);(out/(name+'-compile.log')).write_text(c.stdout+c.stderr);c.check_returncode()
 run=subprocess.run([str(out/name)],capture_output=True,text=True,timeout=timeout);(out/(name+'.stdout')).write_text(run.stdout);(out/(name+'.stderr')).write_text(run.stderr)
 summary=re.search(r'Totals: [^\n]+',run.stdout).group(0) if name.startswith('original_') else run.stdout.strip()
 results.append({'experiment':name,'exit_code':run.returncode,'result':summary,'failed_tests':re.findall(r'FAIL!  : TestXmlDevice::(\w+)',run.stdout)});print(name+': '+str(run.returncode)+' '+summary,flush=True)
 # Preserve actual original-suite failures; controlled experiments must pass.
 if name=='original_xmldevice':
  assert re.findall(r'FAIL!  : TestXmlDevice::(\w+)',run.stdout)==['testBuildCommand','testBuildCommandWithArg'] and 'Totals: 32 passed, 2 failed' in run.stdout
 else:run.check_returncode()
for n in ['xmlclient.h','xmlclient.cpp','xmldevice.h','xmldevice.cpp','entryinfo.h','entryinfo.cpp']:
 copy('libqtcommon',n)
for n in ['test_xmlclient.h','test_xmlclient.cpp','test_xmldevice.h','test_xmldevice.cpp','xmldevice_tester.h','xmldevice_tester.cpp']:copy('libqtcommon','test/'+n)
copy('BtExperience','BtObjects/generic_functions.h')
copy('libqtdevices','xml_functions.h')
(out/'xml_subset.cpp').write_text('#include "xml_functions.h"\n#include <QStringList>\n'+'\n'.join(original('libqtdevices','xml_functions.cpp',s) for s in ['getElement','getTextChild','getChildren']))
for n in ['xmlclient.h','xmldevice.h','test_xmlclient.h','test_xmldevice.h']:moc(n)
xml_sources=['xmlclient.cpp','xmldevice.cpp','entryinfo.cpp','xml_subset.cpp','moc_xmlclient.cpp','moc_xmldevice.cpp']
for name,cl in [('original_xmlclient','TestXmlClient'),('original_xmldevice','TestXmlDevice')]:
 stem='test_'+name.removeprefix('original_');(out/(name+'.cpp')).write_text('#include <QtTest>\n#include "'+stem+'.h"\nint main(int c,char**v){QCoreApplication a(c,v);'+cl+' t;return QTest::qExec(&t,c,v);}\n')
 execute(name,[*xml_sources,stem+'.cpp','moc_'+stem+'.cpp',name+'.cpp']+(['xmldevice_tester.cpp'] if cl=='TestXmlDevice' else []))
(out/'network.cpp').write_text(r'''
#include <QtCore>
#include <QtNetwork>
#include <QDomDocument>
#include <cassert>
#include <iostream>
#include "xmlclient.h"
#include "xmldevice.h"
class TestXmlClient {public:static QString buffer(XmlClient&c){return c.buffer;}};
class XmlDeviceTester {public:
 static void endpoint(XmlDevice&d,int p){delete d.xml_client;d.xml_client=new XmlClient("127.0.0.1",p);QObject::connect(d.xml_client,SIGNAL(dataReceived(QString)),&d,SLOT(handleData(QString)));QObject::connect(d.xml_client,SIGNAL(connectionUp()),&d,SLOT(sendFirstQueuedMessage()));QObject::connect(d.xml_client,SIGNAL(connectionDown()),&d,SLOT(cleanSessionInfo()));QObject::connect(d.xml_client,SIGNAL(connectionDown()),&d,SLOT(handleClientError()));}
 static XmlClient*client(XmlDevice&d){return d.xml_client;}static int queued(XmlDevice&d){return d.message_queue.size();}static QString sid(XmlDevice&d){return d.sid;}static int sent(XmlDevice&d){return d.last_sent;}static bool welcome(XmlDevice&d){return d.welcome_received;}
};
template<class F>void wait(F f){QElapsedTimer t;t.start();while(!f()&&t.elapsed()<3000){QCoreApplication::processEvents();QThread::msleep(1);}assert(f());}
void tick(){QElapsedTimer t;t.start();while(t.elapsed()<30){QCoreApplication::processEvents();QThread::msleep(1);}}
QTcpSocket* accept(QTcpServer&s){wait([&]{return s.hasPendingConnections();});return s.nextPendingConnection();}
QString envelope(QString tag,QString sid="synthetic",int pid=0){return "<OWNxml><Hdr><MsgID><SID>"+sid+"</SID><PID>"+QString::number(pid)+"</PID></MsgID><Dst><IP>127.0.0.1</IP></Dst><Src><IP>127.0.0.1</IP></Src></Hdr><Cmd>"+tag+"</Cmd></OWNxml>";}
void send(QTcpSocket*s,QString v){assert(s->write(v.toUtf8())>=0);s->flush();tick();}
int main(int argc,char**argv){QCoreApplication app(argc,argv);QTcpServer server;assert(server.listen(QHostAddress::LocalHost,0));
 {XmlClient c("127.0.0.1",server.serverPort());QStringList got;QObject::connect(&c,&XmlClient::dataReceived,[&](QString v){got<<v;});c.connectToHost();auto peer=accept(server);wait([&]{return c.isConnected();});
 send(peer,"<OWNxml>old");wait([&]{return TestXmlClient::buffer(c).contains("old");});peer->disconnectFromHost();wait([&]{return !c.isConnected();});c.connectToHost();peer=accept(server);send(peer,"new</OWNxml>");wait([&]{return got.size()==1;});assert(got[0]=="<OWNxml>oldnew</OWNxml>");
 peer->write("<OWNxml>\xc3",9);peer->flush();wait([&]{return TestXmlClient::buffer(c).contains(QChar(0xfffd));});peer->write("\xa9</OWNxml>");peer->flush();wait([&]{return got.size()==2;});assert(got[1].count(QChar(0xfffd))==2);c.disconnectFromHost();tick();}
 {XmlDevice d;XmlDeviceTester::endpoint(d,server.serverPort());XmlDeviceTester::client(d)->connectToHost();auto peer=accept(server);send(peer,envelope("<AW26C1/>"));assert(XmlDeviceTester::welcome(d));XmlDeviceTester::client(d)->disconnectFromHost();tick();}
 {XmlDevice d;XmlDeviceTester::endpoint(d,server.serverPort());int welcome=0;QList<int> acknowledged;QStringList selected;QObject::connect(&d,&XmlDevice::responseReceived,[&](XmlResponse r){if(r.contains(XmlResponses::WELCOME))++welcome;if(r.contains(XmlResponses::ACK))acknowledged<<d.lastAnsweredCommand();if(r.contains(XmlResponses::SERVER_SELECTION))selected<<r[XmlResponses::SERVER_SELECTION].toString();});
 d.requestUPnPServers();d.selectServer("B");auto peer=accept(server);send(peer,envelope("<WMsg/>"));assert(welcome==1&&XmlDeviceTester::queued(d)==2&&!peer->bytesAvailable()); // welcome header requeues A behind B
 send(peer,envelope("<ACK><RC>200</RC></ACK>"));wait([&]{return peer->bytesAvailable()>0;});QString first=QString::fromUtf8(peer->readAll());assert(first.contains("<id>B</id>")&&XmlDeviceTester::sent(d)==2);assert(acknowledged.last()==0);
 // A valid but mismatched SID/PID/header is adopted, and attributed to last_sent.
 send(peer,envelope("<AW26C2><current_server>stale</current_server></AW26C2>","different-session",999));assert(selected==QStringList{"stale"}&&XmlDeviceTester::sid(d)=="different-session"&&d.lastAnsweredCommand()==2);
 send(peer,envelope("<ACK><RC>200</RC></ACK>","different-session",1000));wait([&]{return peer->bytesAvailable()>0;});QString second=QString::fromUtf8(peer->readAll());assert(second.contains("<RW26C1/>")&&acknowledged.last()==2&&XmlDeviceTester::sent(d)==1);
 d.selectServer("C");assert(XmlDeviceTester::queued(d)==1);peer->disconnectFromHost();wait([&]{return !XmlDeviceTester::client(d)->isConnected();});assert(!XmlDeviceTester::welcome(d)&&XmlDeviceTester::queued(d)==1);tick();assert(!server.hasPendingConnections());
 d.selectServer("D");peer=accept(server);send(peer,envelope("<WMsg/>"));assert(XmlDeviceTester::queued(d)==2);send(peer,envelope("<ACK><RC>200</RC></ACK>"));wait([&]{return peer->bytesAvailable()>0;});QString reconnected=QString::fromUtf8(peer->readAll());assert(reconnected.contains("<id>D</id>")&&!reconnected.contains("<RW26C1"));assert(XmlDeviceTester::queued(d)==1);XmlDeviceTester::client(d)->disconnectFromHost();tick();}
 std::cout<<"native loopback framing, non-WMsg welcome state, mismatched identity, welcome rotation, ACK attribution and reconnect scenarios passed\n";
}
''')
execute('network',[*xml_sources,'network.cpp'])
# The entire shared MediaPlayer translation unit and header are unchanged.
for n in ['mediaplayer.h','mediaplayer.cpp']:copy('libqtcommon',n)
moc('mediaplayer.h')
video_selector=original('BtExperience','BtObjects/multimediaplayer.cpp','isVideoFile')
(out/'worker.cpp').write_text(r'''
#include <QtCore>
#include <QtConcurrentRun>
#include <cassert>
#include <iostream>
#include "mediaplayer.h"
#include "entryinfo.h"
bool isVideoFile(QString);
template<class F>void wait(F f){QElapsedTimer t;t.start();while(!f()&&t.elapsed()<6000){QCoreApplication::processEvents();QThread::msleep(1);}assert(f());}
void executable(QString p,QByteArray data){QFile f(p);assert(f.open(QIODevice::WriteOnly));f.write(data);f.close();f.setPermissions(QFile::ReadOwner|QFile::WriteOwner|QFile::ExeOwner);}
int main(int argc,char**argv){QCoreApplication app(argc,argv);assert(isVideoFile("clip.mp4")&&isVideoFile("clip.avi")&&isVideoFile("clip.mpg")&&!isVideoFile("clip.MP4")&&!isVideoFile("clip.mp3"));QTemporaryDir d;QString probe=d.path()+"/probe";executable(probe,"#!/bin/sh\nprintf 'Title: worker\\nA: 1.0 (0:01.0) of 9.0 (0:09.0)\\n'\n");MediaPlayer::setGlobalCommandLineArguments(probe,{},{});
 MediaPlayer m;int delivered=0;QObject::connect(&m,&MediaPlayer::playingInfoUpdated,[&](QMap<QString,QString> i){assert(i["meta_title"]=="worker");if(++delivered==1){m.requestInitialPlayingInfo("replacement");}});m.requestInitialPlayingInfo("original");wait([&]{return delivered==1;});QCoreApplication::sendPostedEvents(nullptr,QEvent::DeferredDelete);wait([&]{return QThreadPool::globalInstance()->activeThreadCount()==0;});QCoreApplication::processEvents();assert(delivered==1);assert(m.findChildren<QFutureWatcher<QMap<QString,QString>>*>().isEmpty());
 executable(probe,"#!/bin/sh\nsleep 0.15\nprintf 'Title: worker\\nA: 1.0 (0:01.0) of 9.0 (0:09.0)\\n'\n");auto owner=new MediaPlayer;owner->requestInitialPlayingInfo("destroyed-owner");auto watcher=owner->findChild<QFutureWatcher<QMap<QString,QString>>*>();assert(watcher);auto future=watcher->future();delete owner;assert(!future.isCanceled());wait([&]{return future.isFinished();});assert(future.result()["meta_title"]=="worker");
 executable(probe,"#!/bin/sh\nprintf 'VIDEO: synthetic 320x240\\n'\n");assert(m.checkVideoResolution("synthetic"));executable(probe,"#!/bin/sh\nprintf 'VIDEO: synthetic 321x240\\n'\n");assert(!m.checkVideoResolution("synthetic"));
 std::cout<<"original MediaPlayer with native QtConcurrent: reentrant watcher removal, surviving worker, video suffix selection and video-resolution boundaries passed\n";
}
'''+video_selector)
execute('worker',['mediaplayer.cpp','entryinfo.cpp','moc_mediaplayer.cpp','worker.cpp'],['-DMEDIAPLAYER_DISABLE_HARDWARE_FUNCTIONS','-DMEDIAPLAYER_MULTIPLE_PLAYERS','-DBT_EXPERIENCE_TODO_REVIEW_ME'],60)

scan_header=r"""
#include <QtCore>
#include <QtConcurrentRun>
#include <cassert>
#include <iostream>
#include "entryinfo.h"
QSemaphore reached,releaseWorker;
struct FolderListModelMemento {QVariantList path;};
class DirectoryListModel:public QObject {public:QVariantList path;DirectoryListModel(QObject*p=nullptr):QObject(p){}void setRootPath(QVariantList p){reached.release();releaseWorker.acquire();path=p;}FolderListModelMemento*clone(){return new FolderListModelMemento{path};}void restore(FolderListModelMemento*m){path=m->path;}};
struct MountPoint{QString path;bool getMounted(){return true;}QString getPath(){return path;}};
class SourceLocalMedia:public QObject {Q_OBJECT
public:using AsyncRes=QPair<DirectoryListModel*,bool*volatile>;bool*volatile terminate=nullptr;MountPoint*mount_point;SourceLocalMedia(MountPoint*m):mount_point(m){}void playFirstMediaContent();static AsyncRes scanPath(DirectoryListModel*,QString,bool*volatile);
signals:void firstMediaContentStatus(bool);
public slots:void pathScanComplete(){} // unsafe original completion is outside this scenario
};
template<class R>
"""
scan_bodies='\n'.join(original('BtExperience','BtObjects/mediaobjects.cpp',x) for x in ['makeAbsolute','makeModelPath','SourceLocalMedia::scanPath','SourceLocalMedia::playFirstMediaContent'])
scan_main=r"""
int main(int argc,char**argv){QCoreApplication app(argc,argv);QTemporaryDir d;QFile f(d.path()+"/worker.mp3");assert(f.open(QIODevice::WriteOnly));f.close();MountPoint mount{d.path()};auto owner=new SourceLocalMedia(&mount);owner->playFirstMediaContent();assert(reached.tryAcquire(1,3000));auto watcher=owner->findChild<QFutureWatcher<SourceLocalMedia::AsyncRes>*>();assert(watcher);auto future=watcher->future();delete owner;assert(!future.isCanceled()&&!future.isFinished());releaseWorker.release();future.waitForFinished();auto r=future.result();assert(!*r.second&&!r.first->path.isEmpty());delete r.first;delete r.second;
std::cout<<"original discovery dispatcher/worker survives owner destruction under a gated model seam\n";
}
#include "scan_native.moc"
"""
(out/'scan_native.cpp').write_text(scan_header+scan_bodies+scan_main);subprocess.run(['moc-qt5',str(out/'scan_native.cpp'),'-o',str(out/'scan_native.moc')],check=True)
execute('scan_native',['scan_native.cpp','entryinfo.cpp'])
gst_header=r"""
#include <QtCore>
#include <QProcess>
#include <QSocketNotifier>
#include <fcntl.h>
#include <unistd.h>
#include <cassert>
#include <iostream>
class GstMediaPlayerImplementation:public QObject {Q_OBJECT
public:int sought=-1;QString track;QRect rect;QMap<QString,QString>getPlayingInfo(){return {};}void setPlayerRect(int x,int y,int w,int h){rect=QRect(x,y,w,h);}void setTrack(QString t){track=t;}bool play(QString t){track=t;return true;}void pause(){}void resume(){}void seek(int s){sought=s;}
signals:void gstPlayerStarted();void gstPlayerPaused();void gstPlayerResumed();void gstPlayerDone();void gstPlayerStopped();
};
class GstMain:public QObject {Q_OBJECT
public:QTimer*poll;GstMediaPlayerImplementation*player;QMap<QString,QString>metadata;QString input;GstMain(GstMediaPlayerImplementation*);void start(int,char**);
public slots:void paused();void checkMetadata();void pollGlib(){};void readInput();void parseLine(QString);
};
class GstMediaPlayer {public:int done=0,stopped=0;void gstPlayerDone(){++done;}void gstPlayerStopped(){++stopped;}void mplayerFinished(int,QProcess::ExitStatus);};
"""
gst_bodies='\n'.join(original('BtExperience','gstmediaplayer/gstmain.cpp',x) for x in ['GstMain::GstMain','GstMain::start','GstMain::paused','GstMain::checkMetadata','GstMain::readInput','GstMain::parseLine'])
gst_bodies+='\n'+original('BtExperience','BtObjects/gstmediaplayer.cpp','parsePlayerOutput')+'\n'+original('BtExperience','BtObjects/gstmediaplayer.cpp','GstMediaPlayer::mplayerFinished')
gst_main=r"""
int main(int argc,char**argv){QCoreApplication app(argc,argv);GstMediaPlayerImplementation backend;GstMain control(&backend);control.parseLine("seek 3");assert(backend.sought==3);control.parseLine("set_track /synthetic/video.mp4");assert(backend.track=="/synthetic/video.mp4");control.parseLine("resize 1 2 30 40");assert(backend.rect==QRect(1,2,30,40));
auto first=parsePlayerOutput("meta_title: hel");auto second=parsePlayerOutput("lo\ncurrent_time: 2\n");assert(first["meta_title"]=="hel"&&!second.contains("meta_title")&&second["current_time"]=="2");
QTimer::singleShot(0,&backend,[&]{emit backend.gstPlayerStopped();});int result=app.exec();assert(result==0);GstMediaPlayer wrapper;wrapper.mplayerFinished(result,QProcess::NormalExit);assert(wrapper.done==1&&wrapper.stopped==0);wrapper.mplayerFinished(2,QProcess::NormalExit);assert(wrapper.done==1&&wrapper.stopped==0);wrapper.mplayerFinished(1,QProcess::NormalExit);assert(wrapper.stopped==1);wrapper.mplayerFinished(0,QProcess::CrashExit);assert(wrapper.stopped==2);
std::cout<<"original GStreamer control glue with synthetic backend: command parsing, split metadata and zero-exit error-signal classification passed\n";
}
#include "gst_glue.moc"
"""
(out/'gst_glue.cpp').write_text(gst_header+gst_bodies+gst_main);subprocess.run(['moc-qt5',str(out/'gst_glue.cpp'),'-o',str(out/'gst_glue.moc')],check=True)
execute('gst_glue',['gst_glue.cpp'])
(out/'execution.json').write_text(json.dumps({'original_files':files,'bodies':records,'results':results,'qt_version':subprocess.check_output(['pkg-config','--modversion','Qt5Core']).decode().strip(),'compiler_version':subprocess.check_output(['g++','--version']).decode().splitlines()[0],'moc_version':subprocess.check_output(['moc-qt5','-v'],stderr=subprocess.STDOUT).decode().strip(),'dependency_packages':[{'name':p.name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(a.qt_prefix.glob('*.rpm'))],'conditions':['Original XML client/device translation units and original QtTest classes compile unchanged under Qt 5; a minimal QCoreApplication test driver and three original XML utility bodies are supplied.','Synthetic localhost TCP service only; no deployed OpenXml gateway or UPnP server.','Original MediaPlayer translation unit uses native QtConcurrent and a synthetic local MPlayer-shaped executable; hardware functions disabled, multiple players enabled, no LAYOUT_TS_10.','Discovery uses native QtConcurrent with a gated substitute directory model and a safe empty completion slot; original unsafe completion is not executed.','GStreamer glue uses a synthetic backend; no GStreamer decoder, plugin, overlay or hardware executes.'],'helper_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()},indent=2)+'\n')
