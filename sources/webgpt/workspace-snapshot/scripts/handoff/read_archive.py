#!/usr/bin/env python3
"""List/read safely from preserved archives, without executing or silently repairing originals."""
from pathlib import Path, PurePosixPath
import argparse, hashlib, json, zipfile

def display_name(i):
 if i.flag_bits&0x800:return i.filename
 try:return i.filename.encode('cp437').decode('utf-8')
 except (UnicodeError,LookupError):return i.filename

def main():
 a=argparse.ArgumentParser();a.add_argument('archive',type=Path);a.add_argument('--member');a.add_argument('--contains',default='');a.add_argument('--start-line',type=int,default=1);a.add_argument('--end-line',type=int);a.add_argument('--extract-to',type=Path)
 ns=a.parse_args()
 with zipfile.ZipFile(ns.archive) as z:
  infos=z.infolist()
  if not ns.member:
   for i in infos:
    if ns.contains.casefold() in (i.filename+' '+display_name(i)).casefold():
     print(json.dumps({'stored_name':i.filename,'display_name':display_name(i),'bytes':i.file_size},ensure_ascii=False))
   return
  matches=[i for i in infos if i.filename==ns.member or display_name(i)==ns.member]
  if len(matches)!=1:raise ValueError('Expected one unambiguous stored/display name')
  i=matches[0];raw=z.read(i)
  if ns.extract_to:
   if Path(display_name(i)).suffix.lower() in ['.ttf','.otf','.woff','.woff2','.ttc']:raise ValueError('Font export is prohibited')
   ns.extract_to.parent.mkdir(parents=True,exist_ok=True)
   with ns.extract_to.open('xb') as f:f.write(raw)
   print(json.dumps({'source':str(ns.archive),'member':i.filename,'target':str(ns.extract_to),'sha256':hashlib.sha256(raw).hexdigest()},ensure_ascii=False));return
  text=raw.decode('utf-8');lines=text.splitlines(keepends=True);end=ns.end_line or len(lines)
  if ns.start_line<1 or end<ns.start_line or end>len(lines):raise ValueError('Invalid line range')
  print(json.dumps({'archive':str(ns.archive),'stored_name':i.filename,'display_name':display_name(i),'sha256':hashlib.sha256(raw).hexdigest(),'start_line':ns.start_line,'end_line':end,'total_lines':len(lines)},ensure_ascii=False))
  print(''.join(lines[ns.start_line-1:end]),end='')
if __name__=='__main__':main()
