#!/usr/bin/env python3
"""Synthetic transfer tests; no project research or uploaded source is modified."""
from pathlib import Path
import importlib.util, json, os, tempfile, unittest, zipfile
from delta_tool import DeltaError, git, commit, init_round, export_delta, verify_delta, stage_delta, load_delta, encoded, sha
class DeltaTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory(prefix='hott-delta-tests-');self.addCleanup(self.tmp.cleanup)
  self.home=Path(self.tmp.name);self.repo=self.home/'worker';self.repo.mkdir()
  git(self.repo,'init','-b','main');git(self.repo,'config','user.name','Synthetic test');git(self.repo,'config','user.email','test@local.invalid')
  (self.repo/'.gitignore').write_text('exchange/outbox/\n')
  (self.repo/'change.txt').write_text('before\n');(self.repo/'delete.txt').write_text('delete me\n');(self.repo/'rename_old.txt').write_text('same bytes\n')
  git(self.repo,'add','.');git(self.repo,'commit','-m','base');self.base=commit(self.repo,'HEAD')
  self.auditor=self.home/'auditor';git(self.repo,'clone','--no-hardlinks',str(self.repo),str(self.auditor))
  request=self.home/'request.md';request.write_text('测试：生成一次增量，不是研究成果。\n')
  init_round(self.repo,'TEST-001',request,self.base)
  (self.repo/'change.txt').write_text('after\n');(self.repo/'new.txt').write_text('新内容\n');(self.repo/'delete.txt').unlink()
  (self.repo/'rename_old.txt').rename(self.repo/'rename_new.txt')
  (self.repo/'mode.sh').write_text('#!/bin/sh\nexit 0\n');(self.repo/'mode.sh').chmod(0o755)
  git(self.repo,'add','-A');git(self.repo,'commit','-m','research and audit round');self.head=commit(self.repo,'HEAD')
  self.out=self.repo/'exchange/outbox/TEST-001.zip'
 def export(self):return export_delta(self.repo,'TEST-001',self.base,'HEAD',self.out)
 def mutate(self,op):
  self.export();target=self.home/'bad.zip'
  with zipfile.ZipFile(self.out) as z:data={n:z.read(n) for n in z.namelist()}
  op(data)
  with zipfile.ZipFile(target,'w') as z:
   for n,b in data.items():z.writestr(n,b)
  return target
 def test_roundtrip_add_modify_delete_rename_and_mode(self):
  r=self.export();self.assertEqual(r['head_commit'],self.head)
  v=verify_delta(self.out,self.auditor);self.assertTrue(v['base_content_verified'])
  staged=self.home/'staged';s=stage_delta(self.out,self.auditor,staged)
  self.assertEqual(s['head_commit'],self.head);self.assertFalse((staged/'delete.txt').exists())
  self.assertFalse((staged/'rename_old.txt').exists());self.assertEqual((staged/'rename_new.txt').read_text(),'same bytes\n')
  self.assertEqual((staged/'change.txt').read_text(),'after\n');self.assertTrue((staged/'mode.sh').stat().st_mode&0o111)
  self.assertEqual(commit(self.auditor,'HEAD'),self.base);self.assertFalse(git(self.auditor,'status','--porcelain').stdout)
  self.assertFalse(git(staged,'remote').stdout)
 def test_dirty_refused(self):
  (self.repo/'unrecorded.txt').write_text('dirty')
  with self.assertRaisesRegex(DeltaError,'DIRTY'):self.export()
 def test_payload_tamper_refused(self):
  bad=self.mutate(lambda d:d.__setitem__('payload/new.txt',b'tampered'))
  with self.assertRaisesRegex(DeltaError,'HASH'):load_delta(bad)
 def test_zip_slip_refused(self):
  bad=self.mutate(lambda d:d.__setitem__('../escape',b'x'))
  with self.assertRaisesRegex(DeltaError,'UNSAFE'):load_delta(bad)
 def test_git_admin_member_refused(self):
  bad=self.mutate(lambda d:d.__setitem__('payload/.git/config',b'x'))
  with self.assertRaisesRegex(DeltaError,'GIT_ADMIN'):load_delta(bad)
 def test_stale_baseline_refused_without_touching_source(self):
  self.export();(self.auditor/'another.txt').write_text('other work')
  git(self.auditor,'config','user.name','Test');git(self.auditor,'config','user.email','test@local.invalid');git(self.auditor,'add','.');git(self.auditor,'commit','-m','new head')
  head=commit(self.auditor,'HEAD')
  with self.assertRaisesRegex(DeltaError,'STALE_BASE'):stage_delta(self.out,self.auditor,self.home/'should-not-exist')
  self.assertEqual(commit(self.auditor,'HEAD'),head);self.assertFalse((self.home/'should-not-exist').exists())
 def test_existing_destination_refused(self):
  self.export();dest=self.home/'existing';dest.mkdir();(dest/'keep').write_text('kept')
  with self.assertRaisesRegex(DeltaError,'DESTINATION_EXISTS'):stage_delta(self.out,self.auditor,dest)
  self.assertEqual((dest/'keep').read_text(),'kept')
 def test_export_not_advanced_baseline(self):
  self.export();meta=json.loads((self.repo/'exchange/rounds/TEST-001/ROUND.json').read_text());self.assertEqual(meta['base_commit'],self.base)
 def test_double_export_refused(self):
  self.export()
  with self.assertRaisesRegex(DeltaError,'OUTPUT_EXISTS'):self.export()
 def test_round_reuse_refused(self):
  with self.assertRaisesRegex(DeltaError,'ROUND_ALREADY_EXISTS'):init_round(self.repo,'TEST-001',self.home/'request.md',self.base)
 def test_changed_delete_list_refused_even_rehashed(self):
  def change(d):
   changes=json.loads(d['CHANGES.json']);changes=[c for c in changes if c['operation']!='delete'];d['CHANGES.json']=encoded(changes)
   m=json.loads(d['MANIFEST.json']);m['members']['CHANGES.json']={'bytes':len(d['CHANGES.json']),'sha256':sha(d['CHANGES.json'])};d['MANIFEST.json']=encoded(m)
  bad=self.mutate(change)
  with self.assertRaisesRegex(DeltaError,'CHANGE_LIST'):load_delta(bad)
 def test_missing_round_input_refused(self):
  (self.repo/'exchange/rounds/TEST-001/AUDIT_REQUEST.md').unlink();git(self.repo,'add','-A');git(self.repo,'commit','-m','missing input')
  with self.assertRaisesRegex(DeltaError,'MISSING_COMMITTED'):self.export()
 def test_symlink_refused(self):
  (self.repo/'badlink').symlink_to('/tmp');git(self.repo,'add','.');git(self.repo,'commit','-m','link')
  with self.assertRaisesRegex(DeltaError,'UNSUPPORTED_GIT_MODE'):self.export()
 def test_unexpected_member_refused(self):
  bad=self.mutate(lambda d:d.__setitem__('extra.txt',b'unlisted'))
  with self.assertRaisesRegex(DeltaError,'UNEXPECTED_OR_MISSING'):load_delta(bad)
 def test_case_collision_refused(self):
  (self.repo/'NEW.TXT').write_text('clash');git(self.repo,'add','.');git(self.repo,'commit','-m','case clash')
  with self.assertRaisesRegex(DeltaError,'CASE_COLLISION'):self.export()
 def test_corrupt_bundle_rejected_in_isolated_stage(self):
  def change(d):
   d['commits.bundle']=b'not a git bundle'
   m=json.loads(d['MANIFEST.json']);m['members']['commits.bundle']={'bytes':len(d['commits.bundle']),'sha256':sha(d['commits.bundle'])};d['MANIFEST.json']=encoded(m)
  bad=self.mutate(change)
  with self.assertRaises(DeltaError):stage_delta(bad,self.auditor,self.home/'isolated-failure')
  self.assertEqual(commit(self.auditor,'HEAD'),self.base);self.assertFalse(git(self.auditor,'status','--porcelain').stdout)
if __name__=='__main__':unittest.main(verbosity=2)
