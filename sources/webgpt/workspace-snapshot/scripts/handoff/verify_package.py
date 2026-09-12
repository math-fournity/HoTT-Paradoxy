#!/usr/bin/env python3
"""Verify a sealed full handoff package without executing its research code.
Use a trusted copy of this verifier when checking untrusted deliveries. Hashes are not signatures.
"""
from pathlib import Path, PurePosixPath
import argparse,hashlib,json,subprocess,sys,os

def sha_file(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--package-root',type=Path,default=Path(__file__).resolve().parents[3]);ap.add_argument('--skip-source-store',action='store_true');a=ap.parse_args();root=a.package_root.resolve()
 m=json.loads((root/'validation/FILE_MANIFEST.json').read_text());expected={r['path']:r for r in m['files']};observed={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.relative_to(root).as_posix()!='validation/FILE_MANIFEST.json'}
 if observed!=set(expected):raise ValueError('Unexpected/missing files: '+repr((observed-set(expected),set(expected)-observed)))
 for rel,r in expected.items():
  q=PurePosixPath(rel)
  if q.is_absolute() or '..' in q.parts or '\\' in rel:raise ValueError('Unsafe manifest path')
  p=root/rel
  if p.is_symlink() or p.stat().st_size!=r['bytes'] or sha_file(p)!=r['sha256']:raise ValueError('File mismatch: '+rel)
 w=root/'workspace';identity=json.loads((root/'manifests/HANDOFF_IDENTITY.json').read_text())
 def git(*args):
  p=subprocess.run(['git','-c','core.hooksPath='+str(root/'validation/empty-hooks'),'-C',str(w),*args],capture_output=True,text=True,env={**os.environ, "GIT_OPTIONAL_LOCKS":"0", "GIT_CONFIG_NOSYSTEM":"1", "GIT_CONFIG_GLOBAL":os.devnull, "GIT_NO_REPLACE_OBJECTS":"1"})
  if p.returncode:raise ValueError(p.stderr)
  return p.stdout.strip()
 if git('rev-parse','HEAD')!=identity['head_commit']:raise ValueError('HEAD mismatch')
 if git('rev-parse','handoff-r040^{commit}')!=identity['head_commit']:raise ValueError('Tag mismatch')
 if git('status','--porcelain'):raise ValueError('Dirty handoff workspace')
 git('fsck','--full')
 if git('remote'):raise ValueError('Unexpected Git remote')
 from govern import load
 plan=load(w).plan(w)
 if plan['revision']!=40:raise ValueError('Unexpected governance revision')
 reading=json.loads((root/'onboarding/READING_PLAN.json').read_text())
 if plan['snapshot']!=reading['snapshot']:raise ValueError('Reading volumes are stale')
 for c in reading['chunks']:
  vol=(root/'onboarding'/c['volume']).read_bytes()
  header=f'\n\n===== SOURCE {c["source"]} | SHA256 {c["source_sha256"]} | LINES {c["start_line"]}-{c["end_line"]}/{c["total_lines"]} =====\n'.encode()
  if vol.count(header)!=1:raise ValueError('Fulltext source header missing or duplicate')
  begin=vol.index(header)+len(header);body=vol[begin:begin+c['body_bytes']]
  if hashlib.sha256(body).hexdigest()!=c['body_sha256']:raise ValueError('Fulltext body mismatch')
 from archive_store import verify
 source=None if a.skip_source_store else verify(root/'archive')
 if source is not None and source['status']!='ALL_ORIGINAL_FILES_BYTE_RECONSTRUCTED':raise ValueError('Archive source mismatch')
 print(json.dumps({'status':'PACKAGE_INTEGRITY_AND_RESTORE_METADATA_VERIFIED','files':len(expected),'head_commit':identity['head_commit'],'revision':plan['revision'],'core_documents':len(plan['documents']),'source_files':None if source is None else source['original_files'],'source_bytes':None if source is None else source['original_bytes'],'math_certified':False,'AI_full_cognition_certified':False,'historical_test_failures_preserved':3},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
