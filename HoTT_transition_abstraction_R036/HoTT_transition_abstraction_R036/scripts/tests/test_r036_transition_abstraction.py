"""Finite positive and adversarial tests. No claim of proof-assistant verification."""
import importlib.util,sys,unittest
from pathlib import Path
path=Path(__file__).resolve().parents[1]/'research/r036_transition_abstraction.py'
spec=importlib.util.spec_from_file_location('r036_model',path);m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m)
class TestAbstraction(unittest.TestCase):
 def setUp(self):self.a=m.specimen();self.s=self.a.source
 def test_source_finishes(self):self.assertTrue(self.s.all_runs_complete())
 def test_source_rank(self):self.assertEqual(self.s.rank(),(2,1,0))
 def test_no_source_cycle(self):self.assertIsNone(self.s.cycle())
 def test_exact_source_prefixes(self):self.assertEqual(self.s.traces(5),((0,),(0,1),(0,1,2)))
 def test_done_preserved(self):self.assertEqual(self.a.target.done,frozenset([1]))
 def test_quotient_edges(self):self.assertEqual(self.a.target.edges,frozenset([(0,0),(0,1)]))
 def test_source_forward_simulation(self):self.assertTrue(all((self.a.alpha[x],self.a.alpha[y]) in self.a.target.edges for x,y in self.s.edges))
 def test_quotient_cycle_certificate(self):self.assertTrue(self.a.target.check_cycle((0,0)))
 def test_quotient_not_complete(self):self.assertFalse(self.a.target.all_runs_complete())
 def test_independent_witness_not_composable(self):self.assertEqual(self.a.edge_witnesses(0,0),((0,1),));self.assertEqual(self.a.lift_sets((0,0,0)),(frozenset([0]),frozenset([1]),frozenset()))
 def test_valid_abstract_loop_prefix(self):self.assertTrue(self.a.abstract_walk_valid((0,)*12))
 def test_valid_abstract_prefix_no_lift(self):self.assertFalse(self.a.lift_sets((0,0,0,1))[-1])
 def test_real_path_does_lift(self):self.assertEqual(self.a.lift_sets((0,0,1))[-1],frozenset([2]))
 def test_missing_back_is_local(self):self.assertEqual(self.a.backward_failures(),((0,1),(1,0)))
 def test_coarse_source_rank_does_not_descend(self):self.assertIsNone(self.a.factor_rank((2,1,0)))
 def test_rank_refinement(self):a=m.Abstraction(self.s,(0,1,2));self.assertTrue(a.target.all_runs_complete());self.assertEqual(a.factor_rank((2,1,0)),(2,1,0));self.assertFalse(a.backward_failures())
 def test_reject_fake_concrete_selfloop_certificate(self):self.assertFalse(self.s.check_cycle((0,0)))
 def test_reject_fake_abstract_edge(self):self.assertFalse(self.a.target.check_cycle((0,1,0)))
 def test_reject_wrong_start_lift(self):self.assertRaises(ValueError,self.a.lift_sets,(1,))
 def test_reject_erased_done(self):self.assertRaises(ValueError,m.Abstraction,self.s,(0,0,0))
 def test_reject_bad_alpha(self):self.assertRaises(ValueError,m.Abstraction,self.s,(0,2,2))
 def test_reject_bool_state(self):self.assertRaises(ValueError,m.System,3,frozenset([(True,2)]),0,frozenset([2]))
 def test_reject_done_outgoing(self):self.assertRaises(ValueError,m.System,1,frozenset([(0,0)]),0,frozenset([0]))
 def test_reject_false_ranking(self):self.assertRaises(ValueError,self.a.factor_rank,(0,0,0))
 def test_non_done_deadlock_is_not_completion(self):s=m.System(2,frozenset(),0,frozenset([1]));self.assertIsNone(s.cycle());self.assertFalse(s.all_runs_complete())
 def test_unreachable_cycle_does_not_refute_initial_termination(self):s=m.System(3,frozenset([(0,1),(2,2)]),0,frozenset([1]));self.assertTrue(s.all_runs_complete());self.assertIsNone(s.rank())
 def test_harmless_merge_sibling_states(self):s=m.System(4,frozenset([(0,1),(0,2),(1,3),(2,3)]),0,frozenset([3]));a=m.Abstraction(s,(0,1,1,2));self.assertTrue(a.target.all_runs_complete());self.assertEqual(a.factor_rank(s.rank()),(2,1,0))
 def test_finite_chain_partition_classification(self):
  result=m.report()['chain_partition_classification'];self.assertEqual([x['Done_preserving_partitions'] for x in result],[1,2,5,15,52]);self.assertTrue(all(x['terminating_quotients']==1 for x in result))
if __name__=='__main__':unittest.main(verbosity=2)
