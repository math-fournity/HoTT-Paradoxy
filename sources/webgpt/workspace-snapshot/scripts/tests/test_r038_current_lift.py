#!/usr/bin/env python3
"""Targeted tests; no extrapolation from finite cases to HoTT theorems."""
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'research'))
from r038_current_lift import *

class CurrentLiftTests(unittest.TestCase):
    def test_r036_rows(self):
        a=specimen();self.assertEqual(row(a,0),{0});self.assertEqual(row(a,1),{1})
    def test_r036_exact_descent_rejected(self):
        with self.assertRaises(DescentError):make_lift_table(specimen())
    def test_r036_current_failures(self):
        self.assertEqual(set(specimen().backward_failures()),{(0,1),(1,0)})
    def test_may_relation_still_valid(self):
        self.assertEqual(specimen().target.edges,{(0,0),(0,1)})
    def test_safe_uniform(self):
        self.assertFalse(uniform_failures(safe_branching()))
    def test_current_lift_table(self):
        a=safe_branching();self.assertTrue(check_lift_table(a,make_lift_table(a)))
    def test_each_current_representative(self):
        a=safe_branching();tab=make_lift_table(a)
        self.assertEqual(lift_path(a,tab,1,(1,2)),(1,3))
        self.assertEqual(lift_path(a,tab,2,(1,2)),(2,3))
    def test_full_finite_path(self):
        a=safe_branching();self.assertEqual(lift_path(a,make_lift_table(a),0,(0,1,2)),(0,1,3))
    def test_fake_global_witness_rejected(self):
        a=safe_branching();tab=make_lift_table(a)
        bad=tuple(LiftEntry(e.current,e.target_label,1) if e.current==2 else e for e in tab)
        self.assertFalse(check_lift_table(a,bad))
    def test_missing_table_entry(self):
        a=safe_branching();self.assertFalse(check_lift_table(a,make_lift_table(a)[:-1]))
    def test_duplicate_table_entry(self):
        a=safe_branching();t=make_lift_table(a);self.assertFalse(check_lift_table(a,t+(t[0],)))
    def test_wrong_start(self):
        a=safe_branching()
        with self.assertRaises(ValueError):lift_path(a,make_lift_table(a),3,(0,1,2))
    def test_false_path_edge(self):
        a=safe_branching()
        with self.assertRaises(ValueError):lift_path(a,make_lift_table(a),0,(0,2))
    def test_bool_not_nat(self):
        with self.assertRaises(ValueError):countdown_prefix(True)
        with self.assertRaises(ValueError):row(specimen(),False)
    def test_source_acc(self):
        a=safe_branching();self.assertTrue(check_acc(a.source,make_acc(a.source,0)))
    def test_acc_transfer(self):
        a=safe_branching();out=migrate_acc(a,make_lift_table(a),make_acc(a.source,0))
        self.assertTrue(check_acc(a.target,out))
    def test_bad_acc_omits_branch(self):
        a=safe_branching();self.assertFalse(check_acc(a.source,AccNode(0,())))
    def test_wrong_acc_label(self):
        a=safe_branching();self.assertFalse(check_acc(a.source,AccNode(1,((3,AccNode(2,())),))))
    def test_cycle_cannot_build_acc(self):
        with self.assertRaises(ValueError):make_acc(specimen().target,0)
    def test_cyclic_proof_rejected(self):
        s=System(1,frozenset({(0,0)}),0,frozenset())
        p=AccNode(0,());object.__setattr__(p,'children',((0,p),))
        self.assertFalse(check_acc(s,p))
    def test_lifting_not_necessary_for_termination(self):
        a=nonuniform_terminating();self.assertTrue(a.target.all_runs_complete())
        self.assertTrue(uniform_failures(a))
        with self.assertRaises(DescentError):make_lift_table(a)
    def test_acc_does_not_mean_done(self):
        s=System(1,frozenset(),0,frozenset())
        self.assertTrue(check_acc(s,make_acc(s,0)));self.assertFalse(s.all_runs_complete())
    def test_identity_descent(self):
        s=specimen().source;a=Abstraction(s,(0,1,2))
        self.assertTrue(check_lift_table(a,make_lift_table(a)))
    def test_finite_prefix_family(self):
        for n in range(17):
            p=countdown_prefix(n)
            self.assertEqual(tuple(map(countdown_label,p)),('Start',)+('Work',)*n)
            self.assertTrue(all(countdown_edge(s,t) for s,t in zip(p,p[1:])))
    def test_chosen_run_reaches_done(self):
        for n in range(17):
            p=committed_countdown(n);self.assertEqual(len(p)-1,n+1)
            self.assertEqual(countdown_label(p[-1]),'Done')
            self.assertTrue(all(countdown_edge(s,t) for s,t in zip(p,p[1:])))
    def test_horizon_witnesses_not_compatible(self):
        for n in range(1,17):self.assertNotEqual(countdown_prefix(n+1)[:n+1],countdown_prefix(n))
    def test_fixed_choice_cannot_lift_all_prefixes(self):
        p=committed_countdown(3)
        self.assertEqual(tuple(map(countdown_label,p)),('Start','Work','Work','Work','Done'))
        self.assertNotEqual(tuple(map(countdown_label,p)),('Start',)+('Work',)*4)
    def test_report(self):
        r=report();self.assertEqual(r['bounds']['horizon_checks'],17)
        self.assertFalse(r['bounds']['claims_HoTT_core_error'])

if __name__=='__main__':unittest.main(verbosity=2)
