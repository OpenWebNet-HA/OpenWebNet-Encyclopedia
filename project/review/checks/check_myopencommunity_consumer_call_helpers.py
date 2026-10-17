#!/usr/bin/env python3
"""Execute original audio producer/controller with a synthetic child; no audio hardware."""
import argparse,pathlib,subprocess,hashlib,json,shlex,os
p=argparse.ArgumentParser();p.add_argument('--repositories',type=pathlib.Path,required=True);p.add_argument('--work',type=pathlib.Path,required=True);p.add_argument('--qt-prefix',type=pathlib.Path,required=True);a=p.parse_args();a.work.mkdir(parents=True,exist_ok=True)
PINS={'BtExperience':'b88cdac9665d28494f19d6a5d759acf8d5f00ad9','libqtcommon':'825dc72cf0a4b202c0e8d2efd9bd50ce2dd23aa2'};fingerprints=[]
def original(r,p):
 c=['git','--git-dir='+str(a.repositories/(r+'.git'))];b=subprocess.check_output(c+['show',PINS[r]+':'+p]);fingerprints.append(dict(repository=r,revision=PINS[r],path=p,blob=subprocess.check_output(c+['rev-parse',PINS[r]+':'+p],text=True).strip(),sha256=hashlib.sha256(b).hexdigest()));return b.decode()
def write(p,s):
 x=a.work/p;x.parent.mkdir(parents=True,exist_ok=True);x.write_text(s)
for n in ['audiostate.cpp','audiostate.h']:write(n,original('BtExperience','gui/'+n))
for n in ['multimediaplayer.cpp','multimediaplayer.h']:write(n,original('BtExperience','BtObjects/'+n))
for n in ['mediaplayer.cpp','mediaplayer.h','entryinfo.cpp','entryinfo.h']:write('libqtcommon/'+n,original('libqtcommon',n))
write('gstmediaplayer.h',r'''
#pragma once
#include <QtCore>
class GstMediaPlayer:public QObject {Q_OBJECT
public:GstMediaPlayer(QObject*p=nullptr):QObject(p){} void setPlayerRect(QRect){} QMap<QString,QString>getPlayingInfo(){return {};}void play(QRect,QString){qFatal("Video seam must not execute");}void pause(){qFatal("Video seam must not execute");}void resume(){qFatal("Video seam must not execute");}void stop(){qFatal("Video seam must not execute");}void setTrack(QString){qFatal("Video seam must not execute");}bool isInstanceRunning(){return false;}
signals:void gstPlayerStarted();void gstPlayerResumed();void gstPlayerDone();void gstPlayerStopped();void gstPlayerPaused();void playingInfoUpdated(QMap<QString,QString>);void outputAvailable();};
''')
write('mediaobjects.h',r'''
#pragma once
#include <QObject>
class SourceBase:public QObject {Q_OBJECT
public:bool isActive()const{return false;}
signals:void activeChanged();};
''')
write('bt_global_config.h',r'''
#pragma once
#include <QHash>
#include <QString>
#define SOURCE_ADDRESS "source"
#define AMPLIFIER_ADDRESS "amplifier"
namespace bt_global {extern QHash<QString,QString>*config;}
''')
write('generic_functions.h',r'''
#pragma once
#include <QStringList>
extern QStringList commands;
inline void smartExecute(QString s){commands<<s;}
inline void smartExecute_synch(QString s){commands<<s;}
inline void smartExecute_synch(QString s,QStringList args){commands<<s+" "+args.join(" ");}
''')
# Signal handling supplies controlled exit conventions. This child implements only the exercised slave commands.
write('backend.py',r'''#!/usr/bin/python3
import sys,signal
code=next((x for x in sys.argv[1:] if x in ['0','1','2','crash']),None)
if code is None:
 print('Title: synthetic\nA: 12.750 (0:12.750) of 90.0 (1:30.0)',flush=True)
 sys.exit(0)
if code!='crash':signal.signal(signal.SIGTERM,lambda *_:sys.exit(int(code)))
print('Title: synthetic\nA: 12.750 (0:12.750) of 90.0 (1:30.0)',flush=True)
for line in sys.stdin:
 if line.strip()=='pause':print('=====  PAUSE  =====',flush=True)
''');(a.work/'backend.py').chmod(0o700)
write('main.cpp',r'''
#include <QtCore>
#include "audiostate.h"
#include "multimediaplayer.h"
#include "libqtcommon/mediaplayer.h"
#include "bt_global_config.h"
#include <cassert>
QStringList commands;QHash<QString,QString> settings;namespace bt_global {QHash<QString,QString>*config=&settings;}
class TestMultiMediaPlayer {public:static MediaPlayer*backend(MultiMediaPlayer&m){return m.player;}};
template<class F>void wait(F f){QElapsedTimer t;t.start();while(!f()&&t.elapsed()<4000){QCoreApplication::processEvents();QThread::msleep(1);}if(!f())qFatal("Timed out");}
void tick(int ms=80){QElapsedTimer t;t.start();while(t.elapsed()<ms){QCoreApplication::processEvents();QThread::msleep(1);}}
void setup(QString code){MultiMediaPlayer::setGlobalCommandLineArguments(QDir::currentPath()+"/backend.py",QStringList{code,"<FILE_NAME>","<SEEK_TIME>"},{});}
int main(int argc,char**argv){QCoreApplication app(argc,argv);QStringList result;
 // Original process starts/pauses/resumes and wrapper emits native signals, without injected callbacks.
 {setup("1");MultiMediaPlayer p;p.setCurrentSource("synthetic.mp3");p.play();wait([&]{return p.getTrackInfo().contains("current_time");});assert(p.getPlayerState()==MultiMediaPlayer::Playing);p.pause();assert(p.getPlayerState()==MultiMediaPlayer::AboutToPause);wait([&]{return p.getPlayerState()==MultiMediaPlayer::Paused;});assert(p.getAudioOutputState()==MultiMediaPlayer::AudioOutputActive&&TestMultiMediaPlayer::backend(p)->isInstanceRunning());QStringList order;QObject::connect(&p,&MultiMediaPlayer::playerStateChanged,[&](MultiMediaPlayer::PlayerState s){order<<QString("state:%1:output:%2").arg(s).arg(p.getAudioOutputState());});QObject::connect(&p,&MultiMediaPlayer::audioOutputStateChanged,[&](MultiMediaPlayer::AudioOutputState s){order<<QString("output:%1").arg(s);});p.releaseOutputDevices();wait([&]{return p.getAudioOutputState()==MultiMediaPlayer::AudioOutputStopped;});assert(p.getPlayerState()==MultiMediaPlayer::Paused&&!TestMultiMediaPlayer::backend(p)->isInstanceRunning());assert(order==QStringList({"state:2:output:2","output:2"}));p.resume();wait([&]{return p.getPlayerState()==MultiMediaPlayer::Playing;});p.stop();result<<"native pause acknowledgement, state/output ordering and exit-1 release/resume passed";}
 for(QString code:{QString("1"),QString("crash"),QString("0"),QString("2")}){
 setup(code);AudioState s(nullptr);SoundPlayer beep;s.registerBeep(&beep);MultiMediaPlayer p;s.registerMediaPlayer(&p);s.enableState(AudioState::Idle);p.setCurrentSource("synthetic.mp3");p.play();wait([&]{return p.getTrackInfo().contains("current_time");});assert(s.getState()==AudioState::LocalPlayback);s.enableState(AudioState::ScsVideoCall);tick(600);
 if(code=="1"||code=="crash"){assert(s.getState()==AudioState::ScsVideoCall&&p.getPlayerState()==MultiMediaPlayer::Paused&&p.getAudioOutputState()==MultiMediaPlayer::AudioOutputStopped);s.disableState(AudioState::ScsVideoCall);wait([&]{return s.getState()==AudioState::LocalPlayback&&p.getPlayerState()==MultiMediaPlayer::Playing;});}
 if(code=="0"){assert(s.getState()==AudioState::ScsVideoCall&&p.getPlayerState()==MultiMediaPlayer::Stopped&&p.getCurrentSource().isEmpty());s.disableState(AudioState::ScsVideoCall);assert(s.getState()==AudioState::Idle&&p.getPlayerState()==MultiMediaPlayer::Stopped);}
 if(code=="2"){assert(!TestMultiMediaPlayer::backend(p)->isInstanceRunning());assert(s.getState()==AudioState::LocalPlayback&&p.getPlayerState()==MultiMediaPlayer::AboutToPause&&p.getAudioOutputState()==MultiMediaPlayer::AudioOutputActive);s.disableState(AudioState::ScsVideoCall);}
 p.stop();result<<"call interruption with controlled exit "+code+" passed";
 }
 // Sound Diffusion remains a distinct registered role; pause does not release its native process.
 {setup("1");AudioState s(nullptr);SoundPlayer beep;s.registerBeep(&beep);MultiMediaPlayer p;s.registerSoundDiffusionPlayer(&p);s.enableState(AudioState::Idle);p.setCurrentSource("synthetic.mp3");p.play();wait([&]{return p.getTrackInfo().contains("current_time");});assert(s.getState()==AudioState::Idle);s.enableState(AudioState::ScsVideoCall);wait([&]{return p.getPlayerState()==MultiMediaPlayer::Paused;});assert(TestMultiMediaPlayer::backend(p)->isInstanceRunning()&&p.getAudioOutputState()==MultiMediaPlayer::AudioOutputActive&&s.getState()==AudioState::ScsVideoCall);s.disableState(AudioState::ScsVideoCall);wait([&]{return p.getPlayerState()==MultiMediaPlayer::Playing;});p.stop();result<<"native Sound Diffusion pause/resume keeps process and reported output active passed";}
 for(auto x:result)QTextStream(stdout)<<x<<"\n";
}
''')
inc=['-I'+str(a.work),'-I'+str(a.work/'libqtcommon'),'-I'+str(a.qt_prefix/'usr/include/qt5'),'-I'+str(a.qt_prefix/'usr/include/qt5/QtConcurrent')];flags=shlex.split(subprocess.check_output(['pkg-config','--cflags','--libs','Qt5Core'],text=True));mocs=[]
for i,h in enumerate(['audiostate.h','multimediaplayer.h','gstmediaplayer.h','mediaobjects.h','libqtcommon/mediaplayer.h']):
 out='moc'+str(i)+'.cpp';subprocess.run(['moc-qt5',*inc,h,'-o',out],cwd=a.work,check=True);mocs.append(out)
subprocess.run(['g++','-std=c++17','-fPIC',*inc,'-DMEDIAPLAYER_DISABLE_HARDWARE_FUNCTIONS','-DMEDIAPLAYER_MULTIPLE_PLAYERS','-DBT_EXPERIENCE_TODO_REVIEW_ME','audiostate.cpp','multimediaplayer.cpp','libqtcommon/mediaplayer.cpp','libqtcommon/entryinfo.cpp','main.cpp',*mocs,*flags,'-l:libQt5Concurrent.so.5','-o','helpers'],cwd=a.work,check=True)
r=subprocess.run([str(a.work/'helpers')],cwd=a.work,text=True,capture_output=True,timeout=40);(a.work/'runtime.log').write_text(r.stdout+r.stderr);print(r.stdout);print(r.stderr[-3500:] if r.returncode else '');r.check_returncode()
record={'schema_version':'1.0','pins':PINS,'helper_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'original_files':fingerprints,'compiler':subprocess.check_output(['g++','--version'],text=True).splitlines()[0],'qt':subprocess.check_output(['pkg-config','--modversion','Qt5Core'],text=True).strip(),'results':[{'experiment':'original_audio_chain','result':r.stdout.strip(),'failed_tests':[]}],'conditions':['Complete original MediaPlayer, MultiMediaPlayer, AudioState and EntryInfo files run with native Qt 5 timers, QProcess and signals.', 'Build defines MEDIAPLAYER_DISABLE_HARDWARE_FUNCTIONS, MEDIAPLAYER_MULTIPLE_PLAYERS and BT_EXPERIENCE_TODO_REVIEW_ME; original hardware access is disabled and separate QProcess player instances are selected.','Synthetic slave child emits a controlled pause marker and SIGTERM exits 0, 1, 2 or unhandled-signal crash; these are not measured MPlayer exits.','Routing and hardware functions record requests; source/config dependencies are substitutes. Unused GStreamer seam aborts if video playback is attempted.','No original QtTest suite, original Qt 4 GUI, QML, physical audio, bus or deployed firmware executes.']};(a.work/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
