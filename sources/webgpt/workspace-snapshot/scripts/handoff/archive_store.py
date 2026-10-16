#!/usr/bin/env python3
"""Lossless ZIP-aware deduplicated source archive. Reconstructs ORIGINAL ZIP/bundle bytes.
No recompression assumption: the original compressed byte streams and every header are preserved.
"""
from __future__ import annotations
from pathlib import Path
import argparse, hashlib, json, os, shutil, struct, tempfile, zipfile
ROOT=Path(__file__).resolve().parents[2];PKG=ROOT.parent

def sha(b):return hashlib.sha256(b).hexdigest()
def dump(p,x):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def boundaries(p):
 n=p.stat().st_size;cuts={0,n}
 if p.suffix.lower()=='.zip':
  with zipfile.ZipFile(p) as z,p.open('rb') as f:
   cuts.add(z.start_dir)
   for i in z.infolist():
    off=i.header_offset;f.seek(off);head=f.read(30)
    if head[:4]!=b'PK\x03\x04':raise ValueError('Unknown ZIP local header')
    namesize,extra=struct.unpack_from('<HH',head,26);start=off+30+namesize+extra
    cuts.update([off,start,start+i.compress_size])
 else:cuts.update(range(0,n,65536))
 if min(cuts)<0 or max(cuts)>n:raise ValueError('Invalid source boundary')
 return sorted(cuts)
def build():
 inv=json.loads((PKG/'manifests/SOURCE_INVENTORY.json').read_text())
 pack=PKG/'archive/objects.pack';index={};files=[];pos=0
 if pack.exists():raise FileExistsError(pack)
 with pack.open('xb') as out:
  for e in inv['entries']:
   if e['kind']!='file':raise ValueError('Unsupported source kind')
   p=Path(e['source']);cuts=boundaries(p);parts=[];whole=hashlib.sha256()
   with p.open('rb') as f:
    for lo,hi in zip(cuts,cuts[1:]):
     b=f.read(hi-lo)
     if len(b)!=hi-lo:raise ValueError('Changed source')
     whole.update(b);h=sha(b);parts.append(h)
     if h not in index:index[h]={'offset':pos,'bytes':len(b)};out.write(b);pos+=len(b)
   if whole.hexdigest()!=e['sha256']:raise ValueError('Source checksum mismatch')
   files.append({**e,'parts':parts})
 manifest={'schema':'hott.lossless-source-store.v1','format':'ordered sha256 blocks in one pack file; ZIP header/compressed-payload boundaries, 64KiB for other files','pack':'objects.pack','objects':index,'files':files,'original_bytes':sum(e['size'] for e in files),'stored_bytes':pos,'source_files':len(files),'lossless':True}
 dump(PKG/'archive/STORE.json',manifest)
 report=verify(PKG/'archive');dump(PKG/'validation/SOURCE_STORE_VERIFICATION.json',report)
 print(json.dumps({k:v for k,v in report.items() if k!='files'},ensure_ascii=False))

def verify(store):
 m=json.loads((store/'STORE.json').read_text());results=[];ok=True
 with (store/m['pack']).open('rb') as f:
  for e in m['files']:
   h=hashlib.sha256();n=0
   for key in e['parts']:
    piece=m['objects'][key];f.seek(piece['offset']);b=f.read(piece['bytes'])
    if len(b)!=piece['bytes'] or sha(b)!=key:raise ValueError('Corrupt archive block')
    h.update(b);n+=len(b)
   good=h.hexdigest()==e['sha256'] and n==e['size'];ok=ok and good
   results.append({'relative':e['relative'],'bytes':n,'sha256':h.hexdigest(),'matches_original':good})
 return {'status':'ALL_ORIGINAL_FILES_BYTE_RECONSTRUCTED' if ok else 'FAIL','original_files':len(results),'original_bytes':m['original_bytes'],'stored_bytes':m['stored_bytes'],'unique_blocks':len(m['objects']),'files':results,'new_research_or_authenticity_validation':False}

def restore(store,dest,relative):
 m=json.loads((store/'STORE.json').read_text());rows=[e for e in m['files'] if relative is None or e['relative']==relative]
 if not rows:raise ValueError('Original file not found; consult STORE.json')
 from delta_tool import inside
 with (store/m['pack']).open('rb') as f:
  for e in rows:
   p=inside(dest.resolve(),e['relative'])
   if p.exists():
    if p.is_file() and sha(p.read_bytes())==e['sha256']:continue
    raise ValueError('Existing destination differs; will not overwrite')
   p.parent.mkdir(parents=True,exist_ok=True);tmp=p.with_name(p.name+'.restoring')
   if tmp.exists():raise FileExistsError(tmp)
   h=hashlib.sha256()
   with tmp.open('xb') as out:
    for key in e['parts']:
     piece=m['objects'][key];f.seek(piece['offset']);b=f.read(piece['bytes'])
     if sha(b)!=key:raise ValueError('Corrupt archive block')
     h.update(b);out.write(b)
   if h.hexdigest()!=e['sha256'] or tmp.stat().st_size!=e['size']:raise ValueError('Reconstruction mismatch')
   os.replace(tmp,p)
 return {'status':'ORIGINAL_BYTES_RESTORED','files':len(rows),'destination':str(dest),'does_not_merge_with_workspace':True}

def prune_duplicate_staging():
 report=verify(PKG/'archive')
 if report['status']!='ALL_ORIGINAL_FILES_BYTE_RECONSTRUCTED':raise ValueError('Not verified')
 # Only removes our generated duplicate staging copies, never original /mnt/data inputs.
 p=PKG/'archive/originals'
 if p.exists():shutil.rmtree(p)
 print('Removed generated duplicate staging only; every original input remains in /mnt/data and in the verified store.')

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('command',choices=['build','verify','restore','prune-generated-duplicates']);ap.add_argument('--store',type=Path,default=PKG/'archive');ap.add_argument('--destination',type=Path);ap.add_argument('--relative');a=ap.parse_args()
 if a.command=='build':build()
 elif a.command=='verify':print(json.dumps(verify(a.store),ensure_ascii=False,indent=2))
 elif a.command=='prune-generated-duplicates':prune_duplicate_staging()
 else:
  if not a.destination:raise ValueError('--destination required')
  print(json.dumps(restore(a.store,a.destination,a.relative),ensure_ascii=False))
if __name__=='__main__':main()
