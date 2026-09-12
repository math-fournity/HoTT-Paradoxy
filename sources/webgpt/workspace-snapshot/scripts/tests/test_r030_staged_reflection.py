#!/usr/bin/env python3
"""Targeted R030 tests, not native HoTT validation or infinite termination tests."""
from pathlib import Path
import hashlib, importlib.util, json, random, sys, unittest
ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'scripts/research/r030_staged_reflection.py'
s=importlib.util.spec_from_file_location('r030',SRC);m=importlib.util.module_from_spec(s);sys.modules[s.name]=m;s.loader.exec_module(m)
COUNTS={}
class Tests(unittest.TestCase):
 def test_pair_roundtrip(self):
  for n in range(1024):self.assertEqual(m.pair(*m.unpair(n)),n)
  COUNTS['pair_roundtrips']=1024
 def test_children_decrease(self):
  for n in range(1,2049):
   tag,p=m.unpair(n-1);self.assertLess(p,n)
   a,b=m.unpair(p);self.assertLess(a,n);self.assertLess(b,n)
  COUNTS['descent_codes']=2048
 def test_actual_diag_code(self):
  self.assertEqual(m.old_eval(0,m.VAR,m.VAR),16)
  self.assertEqual(m.diagonal_code(0),207)
 def test_first_domain_break(self):
  d=m.diagonal_code(0)
  self.assertEqual(m.checked_eval(0,d,d)['status'],'REJECTED_NOT_IN_LANGUAGE')
  self.assertFalse(m.raw_eval(0,d,d))
  self.assertEqual(m.checked_eval(1,d,d),{'status':'RETURNED','value':True})
 def test_valid_old_programs_conservative(self):
  codes=set(range(256))
  for n in range(6):
   codes.add(m.eq(m.VAR,m.nat_lit(n)))
  for c in tuple(codes):
   if m.well(0,c):codes.add(m.neg(c));codes.add(m.conj(c,m.TRUE))
  total=0
  for c in sorted(codes):
   if m.well(0,c):
    for x in [0,1,2,7,207,1000]:
     self.assertEqual(m.raw_eval(0,c,x),m.raw_eval(1,c,x));self.assertTrue(m.well(1,c));total+=1
  COUNTS['old_new_conservative_cases']=total
 def test_several_levels(self):
  total=0
  for k in range(5):
   d=m.diagonal_code(k)
   self.assertFalse(m.well(k,d));self.assertTrue(m.well(k+1,d))
   for x in [0,1,2,16,207,d]:
    self.assertEqual(m.raw_eval(k+1,d,x),not m.raw_eval(k,x,x));total+=1
   self.assertTrue(m.raw_eval(k+1,d,d))
  COUNTS['stage_diagonal_cases']=total
 def test_queries_keep_their_version(self):
  d=m.diagonal_code(0)
  for k in range(1,5):self.assertTrue(m.raw_eval(k,d,d))
  self.assertFalse(m.raw_eval(1,m.old_eval(0,m.nat_lit(d),m.VAR),d))
 def test_rejection_not_false_certificate(self):
  for c in [0,m.node(0,1),m.node(99),m.neg(0),m.conj(m.TRUE,0),m.old_eval(1,m.VAR,m.VAR)]:
   self.assertEqual(m.checked_eval(1,c,0)['status'],'REJECTED_NOT_IN_LANGUAGE')
   self.assertIsNone(m.checked_eval(1,c,0)['value'])
 def test_literal_query_and_non_self_control(self):
  self.assertTrue(m.raw_eval(1,m.old_eval(0,m.nat_lit(m.TRUE),m.VAR),207))
  self.assertFalse(m.raw_eval(1,m.old_eval(0,m.nat_lit(m.FALSE),m.VAR),207))
 def test_nonstaged_trace_invariant(self):
  t=m.trace(24);d=m.diagonal_code(0);q=m.old_eval(0,m.VAR,m.VAR)
  for row in t:
   n=row['time'];self.assertEqual(row['code'],d if n%2==0 else q)
   self.assertEqual(row['pending_not'],(n+1)//2);self.assertEqual(row['input'],d)
   self.assertIsNone(row['result']);self.assertFalse(row['rejected'])
  COUNTS['finite_nonstaged_transitions']=24
 def test_nonstaged_positive_control(self):
  state=m.Config(m.neg(m.TRUE),0)
  for _ in range(4):state=m.unstratified_step(state)
  self.assertEqual(state.result,False)
 def test_reject_python_pseudo_numbers(self):
  for v in [-1,True,1.2,'0']:
   with self.assertRaises(ValueError):m.well(0,v)
 def test_one_observation_is_already_impossible(self):
  for b in [False,True]:self.assertNotEqual(b,not b)

def main():
 suite=unittest.defaultTestLoader.loadTestsFromTestCase(Tests)
 result=unittest.TextTestRunner(verbosity=2).run(suite)
 report={'status':'PASS_FINITE_SCOPE' if result.wasSuccessful() else 'FAIL','tests_run':result.testsRun,'counts':COUNTS,'source_sha256':hashlib.sha256(SRC.read_bytes()).hexdigest(),'test_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'diag0':m.diagonal_code(0),'old_checked':m.checked_eval(0,207,207),'old_raw_default':m.raw_eval(0,207,207),'new_checked':m.checked_eval(1,207,207),'unstratified_trace':m.trace(12),'scope':'New explicit language, not HoTT kernel. Finite checks do not prove unbounded claims.','native_formal_verification':'NOT_RUN'}
 out=ROOT/'artifacts/r030/RESULTS_FIXED.json'
 if out.exists():raise FileExistsError(out)
 out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 return 0 if result.wasSuccessful() else 1
if __name__=='__main__':raise SystemExit(main())
