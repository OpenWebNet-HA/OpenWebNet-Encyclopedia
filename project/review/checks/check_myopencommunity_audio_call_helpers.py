#!/usr/bin/env python3
"""Run archived local-audio logic in a scratch Qt environment; no hardware calls."""
import argparse, pathlib, subprocess, hashlib, json, shlex, re, os
PINS={'BtExperience':'b88cdac9665d28494f19d6a5d759acf8d5f00ad9','libqtdevices':'13f0c2049666d234e9cd4b0396863da01636d0f5'}
p=argparse.ArgumentParser();p.add_argument('--repositories',type=pathlib.Path,required=True);p.add_argument('--work',type=pathlib.Path,required=True);p.add_argument('--qt-prefix',type=pathlib.Path,required=True);a=p.parse_args();a.work.mkdir(parents=True,exist_ok=True)
fingerprints=[]
def original(repo,path):
 rev=PINS[repo];cmd=['git','--git-dir='+str(a.repositories/(repo+'.git'))];b=subprocess.check_output(cmd+['show',rev+':'+path]);blob=subprocess.check_output(cmd+['rev-parse',rev+':'+path]).decode().strip();fingerprints.append(dict(repository=repo,revision=rev,path=path,blob=blob,sha256=hashlib.sha256(b).hexdigest()));return b.decode()
def write(path,text):
 x=a.work/path;x.parent.mkdir(parents=True,exist_ok=True);x.write_text(text)
# Complete original AudioState and RingtoneManager files. Dependency substitutes are explicit.
for n in ['audiostate.cpp','audiostate.h','ringtonemanager.cpp','ringtonemanager.h']:write(n,original('BtExperience','gui/'+n))
for n in ['statemachine.cpp','statemachine.h']:write(n,original('libqtdevices',n))
write('multimediaplayer.h',r'''
#pragma once
#include <QObject>
#include <QString>
class MultiMediaPlayer: public QObject {
 Q_OBJECT
public:
 enum PlayerState {Stopped,Playing,AboutToPause,Paused};
 enum AudioOutputState {AudioOutputInactive,AudioOutputActive};
 PlayerState state=Stopped; AudioOutputState output=AudioOutputInactive; bool mute=false;
 int pauses=0,resumes=0,releases=0,plays=0; QString source;
 PlayerState getPlayerState()const{return state;} AudioOutputState getAudioOutputState()const{return output;} bool getMute()const{return mute;}
 void setCurrentSource(QString s){source=s;}
 void play(){++plays;state=Playing;output=AudioOutputActive;emit playerStateChanged(state);emit audioOutputStateChanged(output);}
 void pause(){++pauses;state=AboutToPause;emit playerStateChanged(state);}
 void acknowledgePause(){state=Paused;output=AudioOutputInactive;emit playerStateChanged(state);emit audioOutputStateChanged(output);}
 void resume(){++resumes;state=Playing;output=AudioOutputActive;emit playerStateChanged(state);emit audioOutputStateChanged(output);}
 void releaseOutputDevices(){++releases;}
 void stop(){state=Stopped;output=AudioOutputInactive;emit playerStateChanged(state);emit audioOutputStateChanged(output);}
signals:
 void playerStateChanged(MultiMediaPlayer::PlayerState);void audioOutputStateChanged(MultiMediaPlayer::AudioOutputState);
};
''')
write('libqtcommon/mediaplayer.h',r'''
#pragma once
#include <QObject>
class SoundPlayer:public QObject {Q_OBJECT
public:bool active=false;bool isActive()const{return active;} void stop(){if(active){active=false;emit soundFinished();}}
signals:void soundStarted();void soundFinished();};
''')
write('mediaobjects.h',r'''
#pragma once
#include <QObject>
class SourceBase:public QObject {Q_OBJECT
public:bool active=false;bool isActive()const{return active;}
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
write('vct.h',r'''
#pragma once
class CCTV {public:enum {ExternalPlace1=2,ExternalPlace2,ExternalPlace3,ExternalPlace4};};
class Intercom {public:enum{Internal=6,External=7,Floorcall=13};};
''')
write('xml_functions.h',r'''
#pragma once
#include <QDomDocument>
#include <QList>
inline QDomNode getChildWithName(QDomNode n,QString s){return n.firstChildElement(s);}
inline QList<QDomNode> getChildren(QDomNode n,QString s){QList<QDomNode> r;for(QDomNode c=n.firstChild();!c.isNull();c=c.nextSibling())if(c.nodeName()==s)r<<c;return r;}
inline QString getTextChild(QDomNode n,QString s){return n.firstChildElement(s).text();}
''')
write('main.cpp',r'''
#include "audiostate.h"
#include "ringtonemanager.h"
#include "statemachine.h"
#include "libqtcommon/mediaplayer.h"
#include "bt_global_config.h"
#include <QCoreApplication>
#include <QEventLoop>
#include <QTimer>
#include <QFile>
#include <QTextStream>
#include <cstdlib>
QStringList commands;QHash<QString,QString> settings;namespace bt_global{QHash<QString,QString>*config=&settings;}
void need(bool v,const char*s){if(!v){qFatal("Assertion failed: %s",s);}}
void waitms(int ms){QEventLoop loop;QTimer::singleShot(ms,&loop,&QEventLoop::quit);loop.exec();}
int main(int argc,char**argv){QCoreApplication app(argc,argv);
 // Actual original generic stack: repeated current state is pushed, not reference-counted flags.
 {StateMachine s;s.addState(0);s.addState(1);s.start(0);int re=0;QObject::connect(&s,&StateMachine::stateReentered,[&](int,int){++re;});s.toState(1);s.toState(1);need(re==1,"duplicate stack reentry");s.removeState(1);need(s.currentState()==1,"one removal leaves duplicate");s.removeState(1);need(s.currentState()==0,"second removal restores idle");}
 // Actual native timer + original routing, recording-only hardware seams.
 {AudioState s(nullptr);SoundPlayer b;s.registerBeep(&b);s.enableState(AudioState::Idle);s.enableState(AudioState::ScsVideoCall);s.vdeEnable(true);s.disableState(AudioState::ScsVideoCall);commands.clear();waitms(400);need(s.getState()==AudioState::Idle,"call already ended");need(commands.size()==1&&commands[0].endsWith("VDE_Conversation_silent.sh"),"delayed on remains after call exit");}
 {AudioState s(nullptr);SoundPlayer b;s.registerBeep(&b);s.enableState(AudioState::Idle);s.enableState(AudioState::ScsVideoCall);s.vdeEnable(true);s.vdeEnable(false);commands.clear();waitms(400);need(commands.isEmpty(),"explicit disable cancels timer");}
 {AudioState s(nullptr);SoundPlayer b;s.registerBeep(&b);s.enableState(AudioState::Idle);s.enableState(AudioState::ScsVideoCall);s.enableState(AudioState::ScsVideoCall);s.disableState(AudioState::ScsVideoCall);need(s.getState()==AudioState::Idle,"enabled flag idempotent");commands.clear();s.enableState(AudioState::IpVideoCall);need(s.getState()==AudioState::IpVideoCall&&commands.isEmpty(),"IP state has no dedicated routing calls");s.disableState(AudioState::IpVideoCall);commands.clear();s.enableState(AudioState::Teleloop);need(s.getState()==AudioState::Teleloop&&commands.isEmpty(),"teleloop no dedicated routing calls");}
 // Substituted multimedia acknowledgements are separate from original routing controller.
 {AudioState s(nullptr);SoundPlayer b;MultiMediaPlayer media;s.registerBeep(&b);s.registerMediaPlayer(&media);s.enableState(AudioState::Idle);media.play();need(s.getState()==AudioState::LocalPlayback,"playing enables local playback");s.enableState(AudioState::ScsVideoCall);need(media.pauses==1&&media.releases>=1&&s.getState()==AudioState::LocalPlayback,"wait for paused acknowledgement");media.acknowledgePause();need(s.getState()==AudioState::ScsVideoCall,"pause completes transition");s.disableState(AudioState::ScsVideoCall);need(s.getState()==AudioState::LocalPlayback&&media.resumes==1,"temporarily paused playback resumes");}
 {AudioState s(nullptr);SoundPlayer b;MultiMediaPlayer dif;s.registerBeep(&b);s.registerSoundDiffusionPlayer(&dif);s.enableState(AudioState::Idle);dif.play();s.enableState(AudioState::Ringtone);need(dif.pauses==0,"ordinary ringtone permits diffusion");s.enableState(AudioState::VdeRingtone);need(dif.pauses==1,"call ringtone pauses diffusion");dif.acknowledgePause();s.disableState(AudioState::VdeRingtone);need(dif.resumes==1,"diffusion resumes at ringtone");}
 QFile xml("ringtones.xml");need(xml.open(QIODevice::WriteOnly),"synthetic XML creation");xml.write("<root><ringtones><item><id_ringtone>1</id_ringtone><descr>synthetic.wav</descr></item></ringtones></root>");xml.close();
 {AudioState s(nullptr);SoundPlayer b;MultiMediaPlayer ring;s.registerBeep(&b);s.enableState(AudioState::Idle);RingtoneManager r("ringtones.xml",&ring,&s,nullptr);r.playRingtone("synthetic.wav",AudioState::FloorCall);need(ring.plays==1&&s.getState()==AudioState::FloorCall,"ordinary ringtone enabled");ring.stop();need(s.getState()==AudioState::Idle,"ordinary ringtone leaves state");r.playRingtoneAndKeepState("synthetic.wav",AudioState::VdeRingtone);ring.stop();need(s.isStateEnabled(AudioState::VdeRingtone),"keep-state retains state after stop");s.disableState(AudioState::VdeRingtone);r.playRingtone("",AudioState::FloorCall);need(s.getState()==AudioState::Idle&&ring.plays==2,"empty path does not enable state");}
 {AudioState s(nullptr);SoundPlayer b;MultiMediaPlayer ring;s.registerBeep(&b);s.enableState(AudioState::Idle);RingtoneManager r("ringtones.xml",&ring,&s,nullptr);bool once=true;QObject::connect(&r,&RingtoneManager::ringtoneFinished,[&]{if(once){once=false;r.playRingtone("replacement.wav",AudioState::Ringtone);}});r.playRingtone("synthetic.wav",AudioState::FloorCall);ring.stop();need(ring.plays==2&&!s.isStateEnabled(AudioState::Ringtone),"finished callback replacement loses its new state");}
 QTextStream(stdout)<<"PASS original stack, native delayed audio timer, flag routing, controlled pause/resume, ringtone lifetime and reentrant cleanup\n";
}
''')

# Original older stack graph and logical amplifier handlers, with recording callbacks.
old=original('libqtdevices','ts_10/audiostatemachine.cpp');write('audiostatemachine.h',original('libqtdevices','ts_10/audiostatemachine.h'))
def mask(t):return re.sub(r'//[^\n]*|/\*[\s\S]*?\*/|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'',lambda m:''.join('\n' if c=='\n' else ' ' for c in m[0]),t)
def bodies(t):
 m=mask(t)
 for h in re.finditer(r'^[^\n;{}]*\bAudioStateMachine::(\w+)\s*\([^;{}]*\)[^;{}]*\{',m,re.M):
  i=h.end();depth=1
  while depth:depth+=(m[i]=='{')-(m[i]=='}');i+=1
  yield h[1],t[h.start():i],h.end()-1-h.start()
kept={'AudioStateMachine','toState','changeState','forceStateChange','completeStateChange','manageMediaPlaybackStates','setLocalAmplifierTemporaryOff','setLocalAmplifierVolume','getLocalAmplifierVolume','setLocalAmplifierStatus','getLocalAmplifierStatus','setLocalSourceStatus','getLocalSourceStatus','setMediaPlayerActive','setMediaPlayerTemporaryPause','isSoundDiffusionActive','setDirectAudioAccess','isDirectAudioAccess'}
oldtu=r"""
#include "audiostatemachine.h"
#include "bt_global_config.h"
#include <QTimer>
#include <QtDebug>
#define VOLUME_TIMER_SECS 5
#define TRANSITION_TIMEOUT_SECS 10
#define DEFAULT_VOLUME 20
namespace Volumes{enum Type{VIDEODOOR,INTERCOM,MM_LOCALE,BEEP,RINGTONES,FILE,VCTIP,MICROPHONE,MM_SOURCE,MM_AMPLIFIER,INTERCOMIP,COUNT};}
static QByteArray volumes(Volumes::COUNT,DEFAULT_VOLUME);
extern QStringList commands;
static void changeVolumePath(Volumes::Type p,int v=-1){commands<<QString("volume:%1:%2").arg(p).arg(v<0?int(volumes[p]):v);}
static void activateLocalSource(){commands<<"source-on";}static void deactivateLocalSource(){commands<<"source-off";}
static void activateLocalAmplifier(){commands<<"amp-on";}static void deactivateLocalAmplifier(){commands<<"amp-off";}
static bool isVideoCallState(int s){using namespace AudioStates;return s==IP_INTERCOM_CALL||s==IP_VIDEO_CALL||s==SCS_INTERCOM_CALL||s==SCS_VIDEO_CALL||s==PLAY_VDE_RINGTONE||s==MUTE||s==PLAY_FLOORCALL;}
static bool isAlarmState(int s){return s==AudioStates::ALARM_TO_SPEAKER;}
static bool isMediaPlaybackState(int s){return s==AudioStates::PLAY_MEDIA_TO_SPEAKER||s==AudioStates::PLAY_DIFSON;}
using namespace AudioStates;
"""
for name,body,op in bodies(old):
 if name in kept:oldtu+=body+'\n'
 elif name=='start':oldtu+=body[:op]+'{ StateMachine::start(state); }\n'
 else:
  sig=body[:op];ret='return 0;' if re.search(r'^\s*(int|bool)\b',sig) else ''
  oldtu+=sig+'{'+ret+'}\n'
write('oldgraph.cpp',oldtu)
write('oldmain.cpp',r"""
#include "audiostatemachine.h"
#include "bt_global_config.h"
#include <QCoreApplication>
#include <QEventLoop>
#include <QTimer>
#include <QTextStream>
#include <QtDebug>
QStringList commands;QHash<QString,QString> settings;namespace bt_global{QHash<QString,QString>*config=&settings;}
void need(bool b,const char*s){if(!b)qFatal("Assertion failed: %s",s);}
int main(int argc,char**argv){QCoreApplication app(argc,argv);using namespace AudioStates;
 {AudioStateMachine s;s.toState(ALARM_TO_SPEAKER);s.toState(SCS_VIDEO_CALL);s.toState(PLAY_RINGTONE);need(s.currentState()==SCS_VIDEO_CALL,"call outranks lower queued states");s.removeState(SCS_VIDEO_CALL);need(s.currentState()==ALARM_TO_SPEAKER,"alarm resumes first");s.removeState(ALARM_TO_SPEAKER);need(s.currentState()==PLAY_RINGTONE,"lower ringtone resumes");}
 {AudioStateMachine s;s.toState(BEEP_ON);s.toState(SCS_VIDEO_CALL);s.toState(SCREENSAVER);need(s.currentState()==SCS_VIDEO_CALL,"screen state below call");s.removeState(SCS_VIDEO_CALL);need(s.currentState()==SCREENSAVER,"screen sits above beep");s.removeState(SCREENSAVER);need(s.currentState()==BEEP_ON,"beep returns");}
 {AudioStateMachine s;int changes=0;QObject::connect(&s,&StateMachine::stateChanged,[&](int,int){++changes;});s.setDirectAudioAccess(true);s.toState(SCS_VIDEO_CALL);need(changes==0&&s.currentState()==SCS_VIDEO_CALL,"logical top precedes completed transition");QEventLoop loop;QTimer::singleShot(10500,&loop,&QEventLoop::quit);loop.exec();need(changes==1&&s.isDirectAudioAccess(),"10-second guard completes without clearing direct-access flag");}
 {AudioStateMachine s;s.setLocalAmplifierStatus(true);s.setLocalAmplifierVolume(12);commands.clear();s.setLocalAmplifierTemporaryOff(true);need(s.getLocalAmplifierStatus()&&commands.last()=="volume:9:0","temporary silence preserves logical status");commands.clear();s.setLocalAmplifierVolume(23);need(commands.isEmpty()&&s.getLocalAmplifierVolume()==23,"silenced volume updates cache only");s.setLocalAmplifierTemporaryOff(false);need(commands.last()=="volume:9:23","restore uses latest cached volume");}
 QTextStream(stdout)<<"PASS original older priority graph, native 10-second guard and logical amplifier temporary silence\n";}
""")

flags=shlex.split(subprocess.check_output(['pkg-config','--cflags','--libs','Qt5Core'],text=True));inc=['-I'+str(a.work),'-I'+str(a.qt_prefix/'usr/include/qt5'),'-I'+str(a.qt_prefix/'usr/include/qt5/QtXml')]
headers=['audiostate.h','ringtonemanager.h','statemachine.h','multimediaplayer.h','libqtcommon/mediaplayer.h','mediaobjects.h'];mocs=[]
for i,h in enumerate(headers):
 out='moc'+str(i)+'.cpp';subprocess.run(['moc-qt5',*inc,h,'-o',out],cwd=a.work,check=True);mocs.append(out)
subprocess.run(['g++','-std=c++17','-fPIC',*inc,'audiostate.cpp','ringtonemanager.cpp','statemachine.cpp','main.cpp',*mocs,*flags,'-l:libQt5Xml.so.5','-o','helpers'],cwd=a.work,check=True)
r=subprocess.run([str(a.work/'helpers')],cwd=a.work,text=True,capture_output=True,env=dict(os.environ,QT_FORCE_STDERR_LOGGING='1'));(a.work/'runtime.log').write_text(r.stdout+r.stderr);print(r.stdout);print(r.stderr[-3000:] if r.returncode else '');r.check_returncode()

subprocess.run(['moc-qt5',*inc,'audiostatemachine.h','-o','mocold.cpp'],cwd=a.work,check=True)
subprocess.run(['g++','-std=c++17','-fPIC',*inc,'oldgraph.cpp','statemachine.cpp','oldmain.cpp','mocold.cpp','moc2.cpp',*flags,'-o','oldhelpers'],cwd=a.work,check=True)
ro=subprocess.run([str(a.work/'oldhelpers')],cwd=a.work,text=True,capture_output=True,env=dict(os.environ,QT_FORCE_STDERR_LOGGING='1'));(a.work/'old-runtime.log').write_text(ro.stdout+ro.stderr);print(ro.stdout);print(ro.stderr[-3000:] if ro.returncode else '');ro.check_returncode()
record={'schema_version' :'1.0','pins':PINS,'helper_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),'original_files':fingerprints,'compiler':subprocess.check_output(['g++','--version'],text=True).splitlines()[0],'qt':subprocess.check_output(['pkg-config','--modversion','Qt5Core'],text=True).strip(),'results':[{'experiment':'audio_ring','result':r.stdout.strip(),'failed_tests':[]},{'experiment':'oldgraph','result':ro.stdout.strip(),'failed_tests':[]}],'conditions':['Complete original AudioState/RingtoneManager/StateMachine translation units and headers execute under Qt 5.15.19 with native timers and signals.','Hardware/process functions only record commands; multimedia, beep, source, ringtone enum and XML dependency seams are controlled substitutes.','Older graph selected original method bodies and original header use substitute startup, callbacks, volume paths and hardware helpers; native QTimer and complete original generic stack execute.','No QML, original QtTest suite, Qt 4 application, hardware, firmware or audible output executes.']};(a.work/'execution.json').write_text(json.dumps(record,indent=2)+'\n')
