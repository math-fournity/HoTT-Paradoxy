import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'research'))
from r033_dependent_migration import (Action, Arrow, ModelError, all_local_maps,
    c2_family, evidence, naturality, perm_then)

class DependentMigrationTests(unittest.TestCase):
    def setUp(self):
        self.swap=c2_family(swapped=True)
        self.trivial=c2_family(swapped=False)
        self.r=Arrow('base','base',0)
        self.l=Arrow('base','base',1)
    def test_reflexivity(self): self.assertEqual(self.swap.apply(self.r,'0'),'0')
    def test_nontrivial_loop(self): self.assertEqual(self.swap.apply(self.l,'0'),'1')
    def test_loop_inverse(self): self.assertEqual(self.l.then(self.l.inverse()), self.r)
    def test_pair_identity(self): self.swap.pair_path(self.r,'0','0')
    def test_pair_flip(self): self.swap.pair_path(self.l,'0','1')
    def test_bad_pair_component(self):
        with self.assertRaises(ModelError): self.swap.pair_path(self.l,'0','0')
    def test_target_wrong_fibre(self):
        with self.assertRaises(ModelError): self.swap.pair_path(self.r,'0','2')
    def test_transport_ill_typed(self):
        with self.assertRaises(ModelError): self.swap.apply(self.l,'2')
    def test_identity_is_natural(self): self.assertTrue(naturality(self.swap,self.swap,{'base':('0','1')})['natural'])
    def test_not_is_natural(self): self.assertTrue(naturality(self.swap,self.swap,{'base':('1','0')})['natural'])
    def test_constant0_not_natural(self): self.assertFalse(naturality(self.swap,self.swap,{'base':('0','0')})['natural'])
    def test_constant1_not_natural(self): self.assertFalse(naturality(self.swap,self.swap,{'base':('1','1')})['natural'])
    def test_all_trivial_maps_natural(self):
        self.assertTrue(all(naturality(self.trivial,self.trivial,m)['natural'] for m in all_local_maps(self.trivial,self.trivial)))
    def test_no_trivial_to_swap(self):
        self.assertFalse(any(naturality(self.trivial,self.swap,m)['natural'] for m in all_local_maps(self.trivial,self.swap)))
    def test_only_two_swap_maps(self):
        self.assertEqual(sum(naturality(self.swap,self.swap,m)['natural'] for m in all_local_maps(self.swap,self.swap)),2)
    def test_missing_local_map(self):
        with self.assertRaises(ModelError): naturality(self.swap,self.swap,{})
    def test_wrong_local_type(self):
        with self.assertRaises(ModelError): naturality(self.swap,self.swap,{'base':('0','2')})
    def test_identity_erase_succeeds(self): self.assertEqual(self.trivial.endpoint_table()[('base','base')],('0','1'))
    def test_swap_erase_fails(self):
        with self.assertRaises(ModelError): self.swap.endpoint_table()
    def test_boolean_twist_rejected(self):
        with self.assertRaises(ModelError): Arrow('base','base',True)
    def test_noncomposable(self):
        with self.assertRaises(ModelError): Arrow('a','b',0).then(Arrow('a','b',0))
    def test_incomplete_action(self):
        with self.assertRaises(ModelError): Action({'x':('0','1')},{Arrow('x','x',0):('0','1')})
    def test_bad_identity(self):
        with self.assertRaises(ModelError): Action({'x':('0','1')},{Arrow('x','x',0):('1','0'),Arrow('x','x',1):('1','0')})
    def test_noninjective_action(self):
        with self.assertRaises(ModelError): Action({'x':('0','1')},{Arrow('x','x',0):('0','1'),Arrow('x','x',1):('0','0')})
    def test_nonfunctorial_threecycle(self):
        with self.assertRaises(ModelError): Action({'x':('0','1','2')},{Arrow('x','x',0):('0','1','2'),Arrow('x','x',1):('1','2','0')})
    def test_noncommuting_order(self):
        a,b=(1,0,2),(0,2,1)
        self.assertEqual(perm_then(a,b)[0],2)
        self.assertEqual(perm_then(b,a)[0],1)
    def test_action_summary_composition(self):
        a,b=(1,0,2),(0,2,1)
        self.assertEqual(perm_then(perm_then(a,b),b),a)
    def test_two_object_local_is_not_global(self):
        a=c2_family(swapped=True,objects=('left','right'))
        self.assertFalse(naturality(a,a,{'left':('0','1'),'right':('1','0')})['natural'])
    def test_results(self):
        d=evidence()
        self.assertEqual(d['two_objects'],{'local_tables':16,'natural_tables':2})
        self.assertEqual(len(d['loop_action_criterion_checks']),18)

if __name__=='__main__': unittest.main(verbosity=2)
