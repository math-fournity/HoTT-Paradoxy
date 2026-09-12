#!/usr/bin/env python3
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
from r039_silent_steps import *

class SilentTests(unittest.TestCase):
 def setUp(self):self.g=minimal_delay();self.bad,_=self.g.fixed_point('bad');self.good,_=self.g.fixed_point('good')
 def test_01_return(self):self.assertEqual(self.g.outcome('ret0')['value'],0)
 def test_02_two_delays(self):self.assertEqual(self.g.outcome('two0')['delay_steps'],2)
 def test_03_lasso(self):self.assertEqual(self.g.outcome('spin')['cycle'],['spin'])
 def test_04_bad_to_both_values(self):self.assertTrue({('spin','ret0'),('spin','ret1')}<=self.bad)
 def test_05_bad_not_transitive(self):self.assertIn(('ret0','spin'),self.bad);self.assertIn(('spin','ret1'),self.bad);self.assertNotIn(('ret0','ret1'),self.bad)
 def test_06_bad_cycle_certificate(self):self.assertTrue(self.g.postfixed({('spin','ret0')},'bad'))
 def test_07_false_certificate(self):self.assertFalse(self.g.postfixed({('ret0','ret1')},'bad'))
 def test_08_unknown_certificate_node(self):self.assertFalse(self.g.postfixed({('not_a_state','ret0')},'bad'))
 def test_09_least_fixpoint(self):least,_=self.g.fixed_point('bad',False);self.assertNotIn(('spin','ret0'),least);self.assertNotIn(('spin','spin'),least)
 def test_10_good_preserves_termination(self):self.assertNotIn(('spin','ret0'),self.good)
 def test_11_good_finite_delay(self):self.assertIn(('two0','ret0'),self.good)
 def test_12_good_reflexive_spin(self):self.assertIn(('spin','spin'),self.good)
 def test_13_good_value_discrimination(self):self.assertNotIn(('ret0','ret1'),self.good)
 def test_14_quotient_bad(self):self.assertIn(('ret0','ret1'),equiv_closure(self.g.nodes,self.bad))
 def test_15_quotient_good(self):self.assertNotIn(('ret0','ret1'),equiv_closure(self.g.nodes,self.good))
 def test_16_bad_no_value_descender(self):self.assertFalse(respects(equiv_closure(self.g.nodes,self.bad),{'ret0':0,'ret1':1}))
 def test_17_credit_finite_skip(self):
  c={'a':{'pair':['wait0','ret0'],'credit':1,'rule':'left','next':'b'},'b':{'pair':['ret0','ret0'],'credit':0,'rule':'now'}}
  self.assertTrue(check_credit_certificate(self.g,c,'a'))
 def test_18_credit_reject_infinite_single_skip(self):
  c={'a':{'pair':['spin','ret0'],'credit':1,'rule':'left','next':'a'}};self.assertFalse(check_credit_certificate(self.g,c,'a'))
 def test_19_credit_both_infinite_ok(self):
  c={'a':{'pair':['spin','spin'],'credit':0,'rule':'both','next':'a'}};self.assertTrue(check_credit_certificate(self.g,c,'a'))
 def test_20_credit_reject_fake_now(self):
  c={'a':{'pair':['ret0','ret1'],'credit':0,'rule':'now'}};self.assertFalse(check_credit_certificate(self.g,c,'a'))
 def test_21_credit_reject_bool(self):
  c={'a':{'pair':['ret0','ret0'],'credit':True,'rule':'now'}};self.assertFalse(check_credit_certificate(self.g,c,'a'))
 def test_22_bad_input(self):
  with self.assertRaises(TypeError):Now(True)
  with self.assertRaises(ValueError):DelayGraph({'a':Later('missing')})
 def test_23_weak_fast_retry(self):r,_=completion_lts().weak_bisim();self.assertIn(('fast','retry'),r)
 def test_24_weak_positive_wait(self):r,_=completion_lts().weak_bisim();self.assertIn(('wait','fast'),r)
 def test_25_may_both(self):g=completion_lts();self.assertTrue(g.may_done('fast') and g.may_done('retry'))
 def test_26_must_difference(self):g=completion_lts();self.assertIn('fast',g.must_done_states());self.assertNotIn('retry',g.must_done_states())
 def test_27_divergence_sensitive(self):r,_=completion_lts().weak_bisim(True);self.assertNotIn(('fast','retry'),r);self.assertIn(('fast','wait'),r)
 def test_28_explicit_done_not_erasable(self):r,_=completion_lts().weak_bisim();self.assertNotIn(('fast','end'),r)
 def test_29_deadlock_not_completion(self):g=LTS(['dead'],[]);self.assertFalse(g.may_done('dead'));self.assertNotIn('dead',g.must_done_states())
 def test_30_graph_reject_edge(self):
  with self.assertRaises(ValueError):LTS(['a'],[('a','tau','b')])
 def test_31_exact_small_deterministic_graphs(self):
  count=0
  for n in (1,2,3):
   names=[str(i) for i in range(n)];nodes=[Now(0),Now(1)]+[Later(s) for s in names]
   for vs in product(nodes,repeat=n):
    g=DelayGraph(dict(zip(names,vs)));r,_=g.fixed_point('good')
    for p,q in product(names,repeat=2):
     a,b=g.outcome(p),g.outcome(q)
     expected=(a['kind']==b['kind']=='DIVERGENCE_LASSO') or (a['kind']==b['kind']=='RETURN' and a['value']==b['value'])
     self.assertEqual((p,q) in r,expected)
    count+=1
  self.assertEqual(count,144)

if __name__=='__main__':unittest.main(verbosity=2)
