#!/usr/bin/env python3
"""Read-only view of original F460 image paths; never trusts extracted symlinks.
No CLI intentionally: importing this module never prints firmware file contents.
"""
from pathlib import Path
import collections,hashlib,json,os,stat as hoststat

class VFSError(Exception): pass
class PathEscape(VFSError): pass
class LinkCycle(VFSError): pass
class MissingImagePath(FileNotFoundError,VFSError): pass
class IntegrityError(VFSError): pass
class NotRegularFile(VFSError): pass

class ImageVFS:
    def __init__(self,image='normal',research_dir=None):
        if image not in ('normal','recovery'): raise ValueError('image must be normal or recovery')
        self.research=Path(research_dir) if research_dir else Path(__file__).resolve().parent
        analysis=self.research.parents[1]/'analysis'
        self.root=analysis/('rootfs' if image=='normal' else 'recovery')
        self.regular=json.loads((analysis/f'{image}-regular-files.json').read_text())
        self.links=json.loads((analysis/f'{image}-symlinks.json').read_text())
        text=(analysis/f'{image}-image-listing.txt').read_text().split('----------\n',1)[1]
        self.entries={}
        for block in text.split('\n\n'):
            row=dict(s.split(' = ',1) for s in block.splitlines() if ' = ' in s)
            if 'Path' in row and not row['Path'].startswith('[SYS]'):self.entries[row['Path']]=row
        self.entries['']={'Path':'','Mode':'drwxr-xr-x','Folder':'+','Size':''}

    @staticmethod
    def _parts(path):
        if '\x00' in str(path): raise VFSError('NUL in image path')
        return str(path).split('/')

    def resolve(self,path,follow_final=True):
        """Return canonical absolute image path; relative inputs start at image root."""
        pending=collections.deque(self._parts(path));parts=[];states=set();hops=0
        while pending:
            segment=pending.popleft()
            if segment in ('','.'):continue
            if segment=='..':
                if not parts:raise PathEscape('path escapes image root')
                parts.pop();continue
            candidate='/'.join(parts+[segment])
            if candidate in self.links and (follow_final or pending):
                state=(candidate,tuple(pending))
                if state in states:raise LinkCycle(f'cyclic image symlink at /{candidate}')
                states.add(state);hops+=1
                if hops>128:raise LinkCycle('image symlink expansion limit exceeded')
                target=self.links[candidate]
                if target.startswith('/'):parts=[]
                pending.extendleft(reversed(self._parts(target)))
                continue
            if candidate not in self.entries:raise MissingImagePath('/'+candidate)
            if pending and not self.entries[candidate].get('Mode','').startswith('d'):
                # A following .. still requires a directory in normal path traversal.
                raise NotADirectoryError('/'+candidate)
            parts.append(segment)
        key='/'.join(parts)
        if key not in self.entries:raise MissingImagePath('/'+key)
        return '/'+key

    def _verified_bytes(self,key):
        if key not in self.regular:raise NotRegularFile('/'+key)
        expected=self.regular[key];p=self.root
        for segment in key.split('/'):
            p=p/segment
            try:mode=p.lstat().st_mode
            except FileNotFoundError as e:raise IntegrityError(f'missing extracted backing for /{key}') from e
            if hoststat.S_ISLNK(mode):raise IntegrityError(f'host symlink in backing for /{key}')
        fd=os.open(p,os.O_RDONLY|os.O_NOFOLLOW)
        with os.fdopen(fd,'rb') as f:
            info=os.fstat(f.fileno())
            if not hoststat.S_ISREG(info.st_mode):raise IntegrityError('backing is not regular')
            if info.st_size!=expected['size']:raise IntegrityError(f'backing size mismatch for /{key}')
            data=f.read()
        if hashlib.sha256(data).hexdigest()!=expected['sha256']:raise IntegrityError(f'backing hash mismatch for /{key}')
        return data

    def read_bytes(self,path):
        return self._verified_bytes(self.resolve(path).lstrip('/'))

    def read(self,path):
        return self.read_bytes(path)

    def read_text(self,path,encoding='utf-8',errors='strict'):
        return self.read_bytes(path).decode(encoding,errors)

    def stat(self,path,follow_symlinks=True,verify=True):
        canonical=self.resolve(path,follow_final=follow_symlinks);key=canonical.lstrip('/')
        row=self.entries[key];mode=row.get('Mode','')
        result={'path':canonical,'mode':mode,'kind':'symlink' if mode.startswith('l') else 'directory' if mode.startswith('d') else 'regular' if mode.startswith('-') else 'special','size':int(row['Size']) if row.get('Size') else None,'uid':row.get('User ID'),'gid':row.get('Group ID'),'inode':row.get('iNode')}
        if key in self.links:result['target']=self.links[key]
        if key in self.regular:
            result['sha256']=self.regular[key]['sha256']
            if verify:self._verified_bytes(key)
            result['backing_verified']=verify
        return result

# Convenience functions; methods are preferable when making many reads.
def resolve(path,image='normal'):return ImageVFS(image).resolve(path)
def read_bytes(path,image='normal'):return ImageVFS(image).read_bytes(path)
def read_text(path,image='normal',encoding='utf-8',errors='strict'):return ImageVFS(image).read_text(path,encoding,errors)
def stat(path,image='normal',follow_symlinks=True,verify=True):return ImageVFS(image).stat(path,follow_symlinks,verify)
