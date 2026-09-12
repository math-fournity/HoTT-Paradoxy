#!/usr/bin/env python3
"""Preserve every inventoried mounted input, without fetching unseen external data."""
from pathlib import Path, PurePosixPath
import hashlib, io, json, os, shutil, stat, zipfile
ROOT=Path(__file__).resolve().parents[2]; PKG=ROOT.parent
FONT={'.ttf','.otf','.woff','.woff2','.ttc'}
def hashfile(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def checkzip(z,where,depth=0):
 issues=[]
 for e in z.infolist():
  n=e.filename; pp=PurePosixPath(n)
  if pp.suffix.lower() in FONT: issues.append({'path':where+'!/'+n,'issue':'FONT'})
  if n.endswith('.zip') and not n.startswith('__MACOSX/') and depth<8:
   try:
    with zipfile.ZipFile(io.BytesIO(z.read(e))) as nested:issues+=checkzip(nested,where+'!/'+n,depth+1)
   except zipfile.BadZipFile:issues.append({'path':where+'!/'+n,'issue':'INVALID_NESTED_ZIP'})
 return issues

def main():
 data=json.loads((PKG/'manifests/SOURCE_INVENTORY.json').read_text()); rows=[];issues=[];catalog=[]
 for e in data['entries']:
  if e['kind']!='file':raise ValueError('Symlink requires explicit archival policy')
  src=Path(e['source']); dest=PKG/'archive/originals/mnt_data'/e['relative']
  if hashfile(src)!=e['sha256']:raise ValueError('Source changed: '+str(src))
  if src.suffix.lower()=='.zip':
   with zipfile.ZipFile(src) as z:
    zi=checkzip(z,str(src));issues+=zi
    for i in z.infolist():
     if not i.is_dir():catalog.append({'archive':e['relative'],'member':i.filename,'bytes':i.file_size,'compressed_bytes':i.compress_size,'crc32':f'{i.CRC:08x}'})
    if zi:raise ValueError('Review nested archive issues before copying: '+str(zi))
  dest.parent.mkdir(parents=True,exist_ok=True)
  if dest.exists():
   if hashfile(dest)!=e['sha256']:raise ValueError('Existing archival copy differs')
  else:shutil.copy2(src,dest)
  if hashfile(dest)!=e['sha256']:raise ValueError('Copy mismatch')
  rows.append({**e,'packaged_path':dest.relative_to(PKG).as_posix(),'copied_byte_exact':True})
 dump(PKG/'manifests/ARCHIVED_INPUTS.json',{'files':rows,'count':len(rows),'bytes':sum(r['size'] for r in rows),'issues':issues})
 dump(PKG/'manifests/ARCHIVE_MEMBERS.json',{'entries':catalog,'note':'Metadata directory; raw archives retained byte-for-byte; all entries remain historical, not current authority.'})
 print(json.dumps({'preserved_files':len(rows),'preserved_bytes':sum(r['size'] for r in rows),'archive_members':len(catalog),'nested_issues':issues}))
if __name__=='__main__':main()
