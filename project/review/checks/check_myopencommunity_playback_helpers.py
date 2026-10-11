#!/usr/bin/env python3
"""Read preserved Git files; build only disposable, controlled substitutes."""
import pathlib,subprocess,json,hashlib,re,argparse
parser=argparse.ArgumentParser(description="Execute six pinned original playback helpers in controlled C++ seams.")
parser.add_argument("--repositories",type=pathlib.Path,required=True,help="Read-only directory containing the four bare Git mirrors")
parser.add_argument("--output",type=pathlib.Path,required=True,help="Scratch directory outside preserved repositories and canonical source material")
args=parser.parse_args()
PINS={'BtExperience': 'b88cdac9665d28494f19d6a5d759acf8d5f00ad9', 'libqtcommon': '825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2', 'libqtdevices': '736f41c4df17d8782f15b441c59bdf72a56f56ed', 'MyHomeSystemEmulator': '4f93f44ee5ec7f89a3de9e040141755c847a5eda'}
base=args.output.resolve();base.mkdir(parents=True,exist_ok=True)
if args.repositories.resolve() == base or args.repositories.resolve() in base.parents:raise ValueError("output must be outside the preserved repository directory")
def method(repo,path,symbol):
 s=subprocess.check_output(["git","--git-dir="+str(args.repositories/(repo+".git")),"show",PINS[repo]+":"+path]).decode();start=s.index(symbol+'(');start=s.rfind('\n',0,start)+1;o=s.index('{',start);i=o+1;d=1
 while d:
  d+=(s[i]=='{')-(s[i]=='}');i+=1
 return s[start:i]
bodies=[]
for repo,path,syms in [('libqtcommon','mediaplayer.cpp',['MediaPlayer::mplayerFinished']),('BtExperience','BtObjects/playlistplayer.cpp',['PlayListPlayer::checkLoop','PlayListPlayer::resetLoopCheck','AudioVideoPlayer::handleMediaPlayerStateChange']),('libqtcommon','list_manager.cpp',['UPnpListManager::handleError'])]:
 for sym in syms:bodies.append((repo,path,sym,method(repo,path,sym)))
header=r'''
#include <cassert>
#include <iostream>
#define emit
#define BT_EXPERIENCE_TODO_REVIEW_ME
#define LOOP_TIMEOUT 2000
struct Log {template<class T> Log& operator<<(const T&){return *this;}};
Log qWarning(){return {};}
void qDebug(const char*,int){}
namespace QProcess {enum ExitStatus {NormalExit,CrashExit};}
struct MediaPlayer {bool active=true; int done=0,stopped=0; void mplayerDone(){++done;} void mplayerStopped(){++stopped;} void mplayerFinished(int,QProcess::ExitStatus);};
struct List {int index=0,total=3; int currentIndex(){return index;} int totalFiles(){return total;}};
struct Clock {int ms=0; void start(){ms=0;} int elapsed(){return ms;}};
struct PlayListPlayer {List *actual_list=nullptr;int loop_starting_file=-1,loop_total_time=0,loops=0;Clock loop_time_counter;void loopDetected(){++loops;}bool checkLoop();void resetLoopCheck();};
struct MultiMediaPlayer {enum PlayerState {Stopped=1,Paused=2,Playing=3,AboutToPause=4};};
struct AudioVideoPlayer:PlayListPlayer {bool user_track_change_request=false;int advances=0,notifications=0;void next(){++advances;}void playingChanged(){++notifications;}void stoppedChanged(){++notifications;}void handleMediaPlayerStateChange(MultiMediaPlayer::PlayerState);};
namespace XmlResponses {enum {TRACK_SELECTION=1,INVALID=2,SERVER_LIST=3};}
namespace XmlError {enum {SERVER_DOWN=1,PARSE=2};}
struct UPnpListManager {int downs=0;void serverDown(){++downs;}void handleError(int,int);};
'''
main=r'''
int main(){
 MediaPlayer m; m.mplayerFinished(0,QProcess::NormalExit); assert(m.done==1 && m.stopped==0 && !m.active);
 m.active=true;m.mplayerFinished(1,QProcess::NormalExit);assert(m.stopped==1);
 m.active=true;m.mplayerFinished(2,QProcess::NormalExit);assert(m.stopped==1 && m.done==1 && !m.active);
 m.active=true;m.mplayerFinished(7,QProcess::CrashExit);assert(m.stopped==2);
 m.mplayerFinished(0,QProcess::NormalExit);assert(m.done==1);
 List l;PlayListPlayer p;p.actual_list=&l;assert(!p.checkLoop());assert(p.loop_total_time==6000);
 l.index=2;p.loop_time_counter.ms=5999;assert(p.checkLoop() && p.loops==1);
 p.loop_time_counter.ms=6000;assert(!p.checkLoop());
 l.total=1;l.index=0;p.loop_starting_file=0;p.loop_time_counter.ms=1;assert(p.checkLoop());
 p.actual_list=nullptr;assert(p.checkLoop());p.resetLoopCheck();assert(p.loop_starting_file==-1);
 AudioVideoPlayer a;a.actual_list=&l;a.handleMediaPlayerStateChange(MultiMediaPlayer::Stopped);assert(a.advances==1);
 a.user_track_change_request=true;a.handleMediaPlayerStateChange(MultiMediaPlayer::Stopped);assert(a.advances==1 && !a.user_track_change_request);
 UPnpListManager u;u.handleError(XmlResponses::TRACK_SELECTION,XmlError::SERVER_DOWN);assert(u.downs==1);
 u.handleError(XmlResponses::INVALID,XmlError::SERVER_DOWN);assert(u.downs==2);
 u.handleError(XmlResponses::SERVER_LIST,XmlError::SERVER_DOWN);assert(u.downs==2);
 u.handleError(XmlResponses::TRACK_SELECTION,XmlError::PARSE);assert(u.downs==2);
 std::cout<<"18 controlled comparisons passed\n";
}
'''
cpp=base/'helpers.cpp';cpp.write_text(header+'\n'.join(b[3] for b in bodies)+main)
subprocess.run(['g++','-std=c++17','-O0','-g',str(cpp),'-o',str(base/'helpers')],check=True)
res=subprocess.run([str(base/'helpers')],capture_output=True,text=True);print(res.stdout);res.check_returncode()
uaf_body=method('BtExperience','BtObjects/mediaobjects.cpp','SourceLocalMedia::pathScanComplete')
uafheader=r'''
#include <utility>
#define emit
struct Log{template<class T>Log& operator<<(const T&){return *this;}};Log qDebug(){return {};}
struct FileObject{enum{Audio=1};int getFileType(){return Audio;}};
struct DirectoryListModel{int getCount(){return 0;}FileObject* getObject(int){return nullptr;}void deleteLater(){}};
template<class T>struct QFutureWatcher{T value;T result(){return value;}void deleteLater(){}};
struct SourceLocalMedia{using AsyncRes=std::pair<DirectoryListModel*,bool*>;void* watcher;void* sender(){return watcher;}void startPlay(DirectoryListModel*,int,int){}void firstMediaContentStatus(bool){}void pathScanComplete();};
'''
uafsrc=base/'completion-uaf.cpp';uafsrc.write_text(uafheader+uaf_body+'\nint main(){DirectoryListModel files;QFutureWatcher<SourceLocalMedia::AsyncRes> watch;watch.value={&files,new bool(true)};SourceLocalMedia m;m.watcher=&watch;m.pathScanComplete();}\n')
subprocess.run(['g++','-std=c++17','-g','-O0','-fsanitize=address',str(uafsrc),'-o',str(base/'completion-uaf')],check=True)
uaf=subprocess.run([str(base/'completion-uaf')],capture_output=True,text=True);(base/'completion-uaf.log').write_text(uaf.stderr)
assert uaf.returncode!=0 and 'heap-use-after-free' in uaf.stderr
print('AddressSanitizer confirms completion flag read after deletion under the controlled empty/cancelled-result seam')
records=[]
for repo,path,sym,body in bodies+ [('BtExperience','BtObjects/mediaobjects.cpp','SourceLocalMedia::pathScanComplete',uaf_body)]:
 records.append({'repository':'MyOpenCommunity/'+repo,'revision':PINS[repo],'path':path,'symbol':sym,'body_sha256':hashlib.sha256(body.encode()).hexdigest()})
(base/'helper-results.json').write_text(json.dumps({'bodies':records,'comparisons':18,'completion_result':'heap-use-after-free','conditions':['Process exit signals are counters; no process is launched.','List index/count, elapsed milliseconds and XML error codes are controlled inputs.','Completion watcher/model/sender are controlled C++ seams, with an empty cancelled result.','No Qt event loop, original suite, media decoding, network, transport or hardware is executed.']},indent=2)+'\n')
