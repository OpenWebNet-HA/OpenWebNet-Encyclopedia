#!/usr/bin/env python3
"""Extract original archived bodies and compile disposable controlled Qt experiments."""
import argparse,hashlib,json,pathlib,re,subprocess
p=argparse.ArgumentParser();p.add_argument('--repositories',type=pathlib.Path,required=True);p.add_argument('--output',type=pathlib.Path,required=True);a=p.parse_args()
root=a.repositories.resolve();out=a.output.resolve()
if root==out or root in out.parents:raise ValueError('output must be outside repositories')
out.mkdir(parents=True,exist_ok=True)
pins={'BtExperience':'b88cdac9665d28494f19d6a5d759acf8d5f00ad9','libqtcommon':'825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2'}
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
flags=subprocess.check_output(['pkg-config','--cflags','--libs','Qt5Core']).decode().split()
common='''#include <QtCore>\n#include <QFutureInterface>\n#include <QFutureWatcher>\n#include <cassert>\n#include <iostream>\n#include <thread>\n'''
results=[]
def execute(name,code,moc=False):
 cpp=out/(name+'.cpp');cpp.write_text(common+code)
 if moc:subprocess.run(['moc-qt5',str(cpp),'-o',str(out/(name+'.moc'))],check=True)
 compiled=subprocess.run(['g++','-std=c++17','-fPIC','-O0','-g','-pthread',str(cpp),'-o',str(out/name),*flags],capture_output=True,text=True)
 (out/(name+'-compile.log')).write_text(compiled.stdout+compiled.stderr);compiled.check_returncode()
 r=subprocess.run([str(out/name),str(out)],capture_output=True,text=True,timeout=35)
 (out/(name+'.stdout')).write_text(r.stdout);(out/(name+'.stderr')).write_text(r.stderr)
 r.check_returncode();results.append({'experiment':name,'result':r.stdout.strip()});print(name+': '+r.stdout.strip())
scan_header=r'''
struct FolderListModelMemento {QString path;};
class DirectoryListModel:public QObject {public:QString path;DirectoryListModel(QObject*p=nullptr):QObject(p){} void setRootPath(QString p){path=p;} FolderListModelMemento*clone(){return new FolderListModelMemento{path};} void restore(FolderListModelMemento*m){path=m->path;}};
QString makeModelPath(QString p){return p;}
namespace EntryInfo {enum{AUDIO=1};}
QStringList getFileFilter(int){return {"*.mp3"};}
template<class T>T makeAbsolute(T v){for(auto &i:v)i=QFileInfo(i.absoluteFilePath());return v;}
struct MountPoint {bool mounted=true;QString path;bool getMounted(){return mounted;}QString getPath(){return path;}};
class SourceLocalMedia:public QObject {Q_OBJECT
public:using AsyncRes=QPair<DirectoryListModel*,bool* volatile>;bool* volatile terminate=nullptr;MountPoint*mount_point;SourceLocalMedia(MountPoint*m):mount_point(m){} void playFirstMediaContent();static AsyncRes scanPath(DirectoryListModel*,QString,bool*volatile);
signals:void firstMediaContentStatus(bool);
public slots:void pathScanComplete(){} // deliberately not the unsafe archived completion
};
struct Pending {DirectoryListModel*model;QString path;bool*flag;QFutureInterface<SourceLocalMedia::AsyncRes> future;};
QList<Pending*> pending;
namespace QtConcurrent {QFuture<SourceLocalMedia::AsyncRes> run(SourceLocalMedia::AsyncRes(*)(DirectoryListModel*,QString,bool*volatile),DirectoryListModel*m,QString p,bool*f){auto*w=new Pending{m,p,f,{}};w->future.reportStarted();pending<<w;return w->future.future();}}
'''
scan_bodies='\n'.join(original('BtExperience','BtObjects/mediaobjects.cpp',x) for x in ['SourceLocalMedia::scanPath','SourceLocalMedia::playFirstMediaContent'])
scan_main=r'''
int main(int argc,char**argv){QCoreApplication app(argc,argv);QTemporaryDir fixture;assert(fixture.isValid());QString before=QDir::currentPath();QDir::setCurrent(fixture.path());QFile song("fixture.mp3");assert(song.open(QIODevice::WriteOnly));song.close();
 DirectoryListModel m;bool stop=false;auto r=SourceLocalMedia::scanPath(&m,fixture.path()+"/removed",&stop);assert(!stop && r.first->path==fixture.path());
 DirectoryListModel n;stop=true;auto cancelled=SourceLocalMedia::scanPath(&n,fixture.path(),&stop);assert(stop && n.path.isEmpty());
 QFile::remove("fixture.mp3");DirectoryListModel z;stop=false;SourceLocalMedia::scanPath(&z,fixture.path(),&stop);assert(stop && z.path.isEmpty());
 MountPoint mount;mount.path=fixture.path();auto source=new SourceLocalMedia(&mount);int negative=0;QObject::connect(source,&SourceLocalMedia::firstMediaContentStatus,[&](bool v){negative+=!v;});
 source->playFirstMediaContent();assert(pending.size()==1 && !*pending[0]->flag);source->playFirstMediaContent();assert(pending.size()==2 && *pending[0]->flag && !*pending[1]->flag && source->children().size()==2);
 mount.mounted=false;source->playFirstMediaContent();assert(negative==1 && !*pending[1]->flag && pending.size()==2);
 auto surviving=pending[1]->future.future();delete source;assert(!surviving.isCanceled() && !*pending[1]->flag);
 for(auto*w:pending){w->future.reportResult(qMakePair(w->model,w->flag));w->future.reportFinished();delete w->model;delete w->flag;delete w;}pending.clear();assert(surviving.isFinished());QDir::setCurrent(before);
 std::cout<<"controlled scan/request/lifetime scenarios passed\n";
}
#include "scan.moc"
'''
execute('scan',scan_header+scan_bodies+scan_main,True)
metadata_header=r'''
using Info=QMap<QString,QString>;
Info startFakePlayer(const QString&,const QString&,Info){return {};}
Info getAudioDataSearchMap(){return {};}
struct Pending {QFutureInterface<Info> future;QString track;};QList<Pending*> pending;
namespace QtConcurrent {QFuture<Info> run(Info(*)(const QString&,const QString&,Info),QString,QString track,Info){auto*p=new Pending;p->track=track;p->future.reportStarted();pending<<p;return p->future.future();}}
class MediaPlayer:public QObject {Q_OBJECT
public:QFutureWatcher<Info>*info_watcher=nullptr;QString global_player_executable;void requestInitialPlayingInfo(const QString&);
signals:void playingInfoUpdated(Info);
public slots:void infoReceived();
};
void finish(Pending*p){p->future.reportResult(Info{{"meta_title",p->track}});p->future.reportFinished();}
void pump(){QCoreApplication::sendPostedEvents(nullptr,QEvent::FutureCallOut);QCoreApplication::processEvents();}
void deferred(){QCoreApplication::sendPostedEvents(nullptr,QEvent::DeferredDelete);}
'''
metadata_bodies='\n'.join(original('libqtcommon','mediaplayer.cpp',x) for x in ['MediaPlayer::requestInitialPlayingInfo','MediaPlayer::infoReceived'])
metadata_main=r'''
int main(int argc,char**argv){QCoreApplication app(argc,argv);MediaPlayer m;QStringList delivered;QObject::connect(&m,&MediaPlayer::playingInfoUpdated,[&](Info i){delivered<<i["meta_title"];});
 m.requestInitialPlayingInfo("A");auto*old=m.info_watcher;QPointer<QObject>oldptr(old);finish(pending[0]);m.requestInitialPlayingInfo("B");QPointer<QObject>newptr(m.info_watcher);finish(pending[1]);
 QCoreApplication::sendPostedEvents(old,QEvent::FutureCallOut);assert(delivered==QStringList{"B"} && m.info_watcher==nullptr);deferred();assert(oldptr.isNull() && newptr.isNull());
 m.requestInitialPlayingInfo("D");QPointer<QObject>dptr(m.info_watcher);QPointer<QObject>reentrant;
 auto c=QObject::connect(&m,&MediaPlayer::playingInfoUpdated,[&](Info i){if(i["meta_title"]=="D"){m.requestInitialPlayingInfo("E");reentrant=m.info_watcher;}});
 finish(pending[2]);pump();assert(m.info_watcher==nullptr && pending.size()==4);deferred();assert(reentrant.isNull() && dptr.isNull());finish(pending[3]);pump();assert(!delivered.contains("E"));QObject::disconnect(c);
 auto owner=new MediaPlayer;owner->requestInitialPlayingInfo("F");auto future=pending.last()->future.future();delete owner;assert(!future.isCanceled());finish(pending.last());assert(future.isFinished());
 for(auto*p:pending)delete p;
 std::cout<<"controlled native-Qt watcher scenarios passed\n";
}
#include "metadata.moc"
'''
execute('metadata',metadata_header+metadata_bodies+metadata_main,True)
probe_bodies='\n'.join(original('libqtcommon','mediaplayer.cpp',x) for x in ['getAudioDataSearchMap','parsePlayerOutput','extractMPlayerInfo','startFakePlayer'])
probe_main=r'''
#define MPLAYER_INFO_TIMEOUT_SECS 5
'''+probe_bodies+r'''
int main(int argc,char**argv){QCoreApplication app(argc,argv);QTemporaryDir d;QString script=d.path()+"/probe";QFile f(script);assert(f.open(QIODevice::WriteOnly));f.write("#!/bin/sh\nprintf 'Title: synthetic-title\\nA: 1.0 (0:01.0) of 9.0 (0:09.0)\\n'\n");f.close();f.setPermissions(QFileDevice::ReadOwner|QFileDevice::WriteOwner|QFileDevice::ExeOwner);
 auto repeated=parsePlayerOutput("Title: first\nTitle: last\n",getAudioDataSearchMap());assert(repeated["meta_title"]=="last");
 auto info=startFakePlayer(script,"synthetic-track",getAudioDataSearchMap());assert(info["meta_title"]=="synthetic-title" && info.contains("current_time"));
 assert(f.open(QIODevice::WriteOnly|QIODevice::Truncate));f.write("#!/bin/sh\nprintf 'Title: partial\\n'\nexit 17\n");f.close();QElapsedTimer timer;timer.start();auto partial=startFakePlayer(script,"synthetic-track",getAudioDataSearchMap());assert(partial["meta_title"]=="partial" && !partial.contains("current_time") && timer.elapsed()>=4900 && timer.elapsed()<8000);
 timer.restart();auto missing=startFakePlayer(d.path()+"/missing","synthetic-track",getAudioDataSearchMap());assert(missing.isEmpty() && timer.elapsed()>=4900 && timer.elapsed()<8000);
 std::cout<<"controlled native-Qt process-probe scenarios passed\n";
}
'''
execute('probe',probe_main)
browser_header=r'''
using XmlArguments=QHash<QString,QString>;using XmlResponse=QMap<int,QVariant>;using QDomNode=QString;
namespace XmlResponses{enum{WELCOME,ACK,SERVER_LIST,SERVER_SELECTION,CHDIR,TRACK_SELECTION,BROWSE_UP,LIST_ITEMS,SET_CONTEXT,INVALID};}
namespace XmlError{enum{CLIENT,SERVER_DOWN,BROWSING,EMPTY_CONTENT,PARSE};}
QString getTextChild(QString node,QString){return node;}
struct FakeXmlClient{bool connected=false;int connects=0;QStringList sent;bool isConnected(){return connected;}void connectToHost(){++connects;}void sendCommand(QString s){sent<<s;}};
struct XmlDevice{struct QueuedCommand{QString command;XmlArguments arguments;int ordinal;QueuedCommand(QString c,XmlArguments a,int o):command(c),arguments(a),ordinal(o){}};
 FakeXmlClient*xml_client;bool welcome_received=false;int command_ordinal=0,last_sent=0,last_response=0,pid=0;QString sid,local_addr,server_addr;QList<QueuedCommand>message_queue;QList<XmlArguments>sent_args;int errors=0;
 void error(int,int){++errors;}QString buildCommand(QString c,XmlArguments a){sent_args<<a;sid="controlled-busy";return c;}
 void reset();void cleanSessionInfo();void handleClientError();void sendFirstQueuedMessage();void sendCommand(const QString&,const XmlArguments& = {});void sendCommand(const QString&,const XmlArguments&,int);bool parseAck(const QDomNode&);
 void requestUPnPServers();void selectServer(const QString&);void chDir(const QString&);void browseUp();void listItems(unsigned int,unsigned int);void setContext(const QString&,const QStringList&);void select(const QString&);
 int lastQueuedCommand()const;int lastAnsweredCommand()const;
};
struct EntryInfo{enum Type{DIRECTORY=1,AUDIO=2,VIDEO=4};QString name;int type;QString path;EntryInfo(QString n="",int t=AUDIO,QString p=""):name(n),type(t),path(p){}};using EntryInfoList=QList<EntryInfo>;
struct UPnpEntryList{int total=0,start=1;EntryInfoList entries;};Q_DECLARE_METATYPE(UPnpEntryList)
class TreeBrowser:public QObject{Q_OBJECT
public:virtual void getFileList(){};virtual bool isRoot(){return true;}virtual void enterDirectory(const QString&){};virtual void exitDirectory(){};
signals:void directoryChanged();void contextChanged();void directoryChangeError();void genericError();void listReceived(EntryInfoList);void listRetrieveError();void emptyDirectory();void isRootChanged();void rootDirectoryEntered();
};
class UPnpClientBrowser:public TreeBrowser {public:XmlDevice*dev;int level=0,starting_element=1,num_elements=0,filter_mask=7;QStringList context,new_context;EntryInfoList cached_elements;
 UPnpClientBrowser(XmlDevice*d):dev(d){};void reset();void enterDirectory(const QString&);void exitDirectory();void getFileList();void getFileList(int);void getPreviousFileList();void getNextFileList();int getNumElements();int getStartingElement();bool isRoot();void setContext(const QStringList&);int lastQueuedCommand()const;int lastAnsweredCommand()const;void handleResponse(const XmlResponse&);void handleError(int,int);
};
class TreeBrowserListModelBase:public QAbstractListModel{Q_OBJECT
public:int rowCount(const QModelIndex& = QModelIndex()) const override{return 0;} QVariant data(const QModelIndex&,int = Qt::DisplayRole)const override{return {};} TreeBrowser*browser;int min_range,max_range,filter;bool loading;TreeBrowserListModelBase(TreeBrowser*,QObject*parent=nullptr);void setLoading(bool);bool isLoading(){return loading;};
signals:void directoryChangeError();void emptyDirectory();void isRootChanged();void loadingChanged();void countChanged();
public slots:void directoryChanged(){};void resetLoadingFlag(){setLoading(false);}
};
struct FileObject{int writes=0;void setFileInfo(EntryInfo,QStringList){++writes;}};
class PagedFolderListModel;PagedFolderListModel*activeModel=nullptr;
class PagedFolderListModel:public TreeBrowserListModelBase{public:UPnpClientBrowser*browser;int item_count=0,current_index=0,start_index=0,discard_operations=0,resets=0;QList<FileObject*>item_list;
 PagedFolderListModel(UPnpClientBrowser*b):TreeBrowserListModelBase(b),browser(b){min_range=0;max_range=4;connect(b,SIGNAL(listRetrieveError()),this,SLOT(resetLoadingFlag()));}int getCount(){return item_count;}QStringList getCurrentPath(){return {};};void reset(){++resets;}void gotFileList(EntryInfoList);
};
'''
browser_bodies='\n'.join(original('libqtcommon','xmldevice.cpp',x) for x in ['XmlDevice::reset','XmlDevice::cleanSessionInfo','XmlDevice::handleClientError','XmlDevice::sendFirstQueuedMessage','XmlDevice::sendCommand','XmlDevice::parseAck','XmlDevice::requestUPnPServers','XmlDevice::selectServer','XmlDevice::chDir','XmlDevice::browseUp','XmlDevice::listItems','XmlDevice::setContext','XmlDevice::select','XmlDevice::lastQueuedCommand','XmlDevice::lastAnsweredCommand'])
# The second overload is retained separately; the extractor's first match is the two-argument method.
full=subprocess.check_output(['git','--git-dir='+str(root/'libqtcommon.git'),'show',pins['libqtcommon']+':xmldevice.cpp']).decode()
second_symbol='XmlDevice::sendCommand'
start=full.index('void XmlDevice::sendCommand(const QString &message, const XmlArguments &arguments, int ordinal)');end=full.index('\nvoid XmlDevice::select(',start)
second=full[start:end].rstrip();browser_bodies+='\n'+second
records.append({'repository':'MyOpenCommunity/libqtcommon','revision':pins['libqtcommon'],'path':'xmldevice.cpp','symbol':'XmlDevice::sendCommand(three arguments)','git_blob':subprocess.check_output(['git','--git-dir='+str(root/'libqtcommon.git'),'rev-parse',pins['libqtcommon']+':xmldevice.cpp']).decode().strip(),'file_sha256':hashlib.sha256(full.encode()).hexdigest(),'start_line':full[:start].count('\n')+1,'end_line':full[:start+len(second)].count('\n')+1,'body_sha256':hashlib.sha256(second.encode()).hexdigest()})
browser_bodies+='\n'+'\n'.join(original('libqtcommon','treebrowser.cpp',x) for x in ['UPnpClientBrowser::reset','UPnpClientBrowser::enterDirectory','UPnpClientBrowser::exitDirectory','UPnpClientBrowser::getFileList','UPnpClientBrowser::getPreviousFileList','UPnpClientBrowser::getNextFileList','UPnpClientBrowser::getNumElements','UPnpClientBrowser::getStartingElement','UPnpClientBrowser::isRoot','UPnpClientBrowser::setContext','UPnpClientBrowser::lastQueuedCommand','UPnpClientBrowser::lastAnsweredCommand','UPnpClientBrowser::handleResponse','UPnpClientBrowser::handleError'])
full=subprocess.check_output(['git','--git-dir='+str(root/'libqtcommon.git'),'show',pins['libqtcommon']+':treebrowser.cpp']).decode();start=full.index('void UPnpClientBrowser::getFileList(int s)');end=full.index('\nvoid UPnpClientBrowser::getPreviousFileList',start);second=full[start:end].rstrip();browser_bodies+='\n'+second
records.append({'repository':'MyOpenCommunity/libqtcommon','revision':pins['libqtcommon'],'path':'treebrowser.cpp','symbol':'UPnpClientBrowser::getFileList(int)','git_blob':subprocess.check_output(['git','--git-dir='+str(root/'libqtcommon.git'),'rev-parse',pins['libqtcommon']+':treebrowser.cpp']).decode().strip(),'file_sha256':hashlib.sha256(full.encode()).hexdigest(),'start_line':full[:start].count('\n')+1,'end_line':full[:start+len(second)].count('\n')+1,'body_sha256':hashlib.sha256(second.encode()).hexdigest()})
browser_bodies+='\n'+'\n'.join(original('BtExperience','BtObjects/folderlistmodel.cpp',x) for x in ['TreeBrowserListModelBase::TreeBrowserListModelBase','TreeBrowserListModelBase::setLoading','PagedFolderListModel::gotFileList'])
browser_main=r'''
#define ELEMENTS_DISPLAYED 4
'''+browser_bodies+r'''
int main(int argc,char**argv){QCoreApplication app(argc,argv);FakeXmlClient client;XmlDevice dev;dev.xml_client=&client;dev.sendCommand("A");dev.sendCommand("B");assert(dev.message_queue.size()==2 && dev.command_ordinal==2);client.connected=true;dev.sendFirstQueuedMessage();assert(client.sent.isEmpty());dev.welcome_received=true;dev.sendFirstQueuedMessage();assert(client.sent==QStringList{"A"} && dev.last_sent==1);dev.parseAck("200");assert(client.sent==QStringList({"A","B"}) && dev.last_sent==2);dev.sendCommand("C");assert(dev.message_queue.size()==1);dev.reset();assert(dev.message_queue.size()==1);dev.cleanSessionInfo();assert(dev.sid.isEmpty() && dev.message_queue.size()==1 && dev.command_ordinal==3);dev.handleClientError();assert(dev.last_response==2 && dev.errors==1);
 UPnpClientBrowser b(&dev);TreeBrowserListModelBase model(&b);int generic=0,empty=0;QObject::connect(&b,&TreeBrowser::genericError,[&]{++generic;});QObject::connect(&b,&TreeBrowser::emptyDirectory,[&]{++empty;});
 b.context=QStringList{"server"};b.level=1;b.enterDirectory("missing");model.setLoading(true);b.handleError(XmlResponses::CHDIR,XmlError::BROWSING);assert(!model.loading && b.context==QStringList({"server","missing"}) && b.level==1);
 model.setLoading(true);b.handleError(XmlResponses::CHDIR,XmlError::EMPTY_CONTENT);assert(model.loading && empty==1);b.handleError(XmlResponses::CHDIR,XmlError::SERVER_DOWN);assert(model.loading && generic==1);b.handleError(XmlResponses::LIST_ITEMS,XmlError::SERVER_DOWN);assert(model.loading);
 b.setContext({"server","album","sub"});assert(b.level==2);b.handleError(XmlResponses::SET_CONTEXT,XmlError::BROWSING);assert(b.level==2 && b.new_context.size()==3);
 b.level=1;b.context=QStringList{"server"};b.exitDirectory();assert(b.level==0 && b.context==QStringList{"server"});int queued=dev.command_ordinal;b.reset();assert(b.level==0 && b.context.isEmpty() && b.new_context.size()==3 && dev.command_ordinal==queued);b.handleResponse(XmlResponse{{XmlResponses::CHDIR,true}});assert(b.level==1 && b.context.isEmpty());
 b.context=QStringList{"server"};b.level=1;b.handleError(XmlResponses::BROWSE_UP,XmlError::BROWSING);assert(b.level==0 && b.context.isEmpty());
 b.level=1;b.context=QStringList{"server"};b.handleError(XmlResponses::BROWSE_UP,XmlError::SERVER_DOWN);assert(b.level==1 && b.context.size()==1);
 EntryInfoList received;QObject::connect(&b,&TreeBrowser::listReceived,[&](EntryInfoList l){received=l;});UPnpEntryList page;page.total=2;page.entries={EntryInfo("audio",EntryInfo::AUDIO),EntryInfo("video",EntryInfo::VIDEO)};b.filter_mask=EntryInfo::AUDIO;b.handleResponse(XmlResponse{{XmlResponses::LIST_ITEMS,QVariant::fromValue(page)}});assert(received.size()==1 && b.num_elements==2);
 PagedFolderListModel paged(&b);paged.setLoading(true);b.handleError(XmlResponses::LIST_ITEMS,XmlError::SERVER_DOWN);assert(!paged.loading);FileObject f; paged.item_list={&f,&f,&f,&f};b.num_elements=8;dev.last_response=8;paged.discard_operations=8;activeModel=&paged;paged.gotFileList({EntryInfo("x")});assert(paged.item_count==0 && f.writes==0);paged.discard_operations=7;activeModel=nullptr;paged.gotFileList({EntryInfo("x")});assert(paged.item_count==0);activeModel=&paged;
 int before=dev.command_ordinal;for(int i=0;i<3;++i)paged.gotFileList({});assert(paged.current_index==0 && paged.item_count==8 && dev.command_ordinal==before+3);for(int i=dev.message_queue.size()-3;i<dev.message_queue.size();++i)assert(dev.message_queue[i].arguments["rank"]=="1");
 std::cout<<"controlled queue/browser/model scenarios passed\n";
}
#include "browser.moc"
'''
execute('browser',browser_header+browser_main,True)

(out/'execution.json').write_text(json.dumps({'bodies':records,'results':results,'qt_version':subprocess.check_output(['pkg-config','--modversion','Qt5Core']).decode().strip()},indent=2)+'\n')
