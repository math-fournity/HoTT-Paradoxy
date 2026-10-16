"""Focused R034 tests: no equation is accepted just because it has a type."""
import copy, json, sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'research'))
import r034_path_certificates as m
class Certificates(unittest.TestCase):
    def setUp(self):self.e=m.bool_env();self.t=m.cast(m.gen(),m.lit(0));self.p=m.calc(self.t,m.lit(1))
    def test_original(self):self.assertEqual(m.check(self.p,self.e)['equation_leaves'][0]['value'],1)
    def test_wrong_result(self):
        with self.assertRaises(m.Rejected):m.check(m.calc(self.t,m.lit(0)),self.e)
    def test_identity(self):m.check(m.calc(m.cast(m.ident(),m.lit(0)),m.lit(0)),self.e)
    def test_inverse(self):m.check(m.calc(m.cast(m.seq(m.gen(),m.inv(m.gen())),m.lit(0)),m.lit(0)),self.e)
    def test_false_metadata(self):
        p=m.quote(self.p,self.e);p['goal']=m.eq(self.t,m.lit(0))
        with self.assertRaises(m.Rejected):m.validate_package(p)
    def test_digest(self):
        p=m.quote(self.p,self.e);p['environment']['generators']['p']['table']=[0,1]
        with self.assertRaises(m.Rejected):m.validate_package(p)
    def test_digest_not_truth(self):
        p=m.quote(self.p,self.e);p['environment']['generators']['p']['table']=[0,1];p['environment_hash']=m.digest(p['environment'])
        with self.assertRaises(m.Rejected):m.validate_package(p)
    def test_support(self):
        p=m.quote(self.p,self.e);p['path_support']=[]
        with self.assertRaises(m.Rejected):m.validate_package(p)
    def test_json_roundtrip(self):m.validate_package(json.loads(json.dumps(m.quote(self.p,self.e))))
    def test_same_action(self):m.same_action_on_support(m.quote(self.p,self.e),self.e)
    def test_different_action(self):
        with self.assertRaises(m.Rejected):m.same_action_on_support(m.quote(self.p,self.e),m.bool_env((0,1)))
    def test_unused_generator(self):
        e=copy.deepcopy(self.e);e['generators']['unused']={'source':'B','target':'B','table':[0,1]};m.same_action_on_support(m.quote(self.p,self.e),e)
    def test_bool_not_index(self):
        with self.assertRaises(m.Rejected):m.eval_value(m.lit(False),self.e)
    def test_non_bijection(self):
        with self.assertRaises(m.Rejected):m.check(self.p,m.bool_env((0,0)))
    def test_mere_not_path(self):
        with self.assertRaises(m.Rejected):m.check(m.calc(m.cast({'op':'mere','source':'B','target':'B'},m.lit(0)),m.lit(1)),self.e)
    def test_cycles(self):
        p={'rule':'lam','domain':m.eq(m.lit(0),m.lit(0))};p['body']=p
        with self.assertRaises(m.Rejected):m.check(p,self.e)
    def test_unbound(self):
        with self.assertRaises(m.Rejected):m.check({'rule':'var','index':0},self.e)
    def test_forged_calc_extra(self):
        p=copy.deepcopy(self.p);p['accepted']=True
        with self.assertRaises(m.Rejected):m.check(p,self.e)
    def test_arrow(self):
        a=m.eq(self.t,m.lit(1));p={'rule':'lam','domain':a,'body':{'rule':'var','index':0}};r=m.check(p,self.e);self.assertEqual(r['r032']['proof']['rule'],'lam')
    def test_mismatched_application(self):
        a=m.eq(m.lit(0),m.lit(0));p={'rule':'app','function':{'rule':'lam','domain':a,'body':{'rule':'var','index':0}},'argument':self.p}
        with self.assertRaises(m.Rejected):m.check(p,self.e)
    def test_noncomposable(self):
        e=copy.deepcopy(self.e);e['fibres']['C']=2
        with self.assertRaises(m.Rejected):m.path_semantics(m.seq(m.gen(),m.ident('C')),e)
    def test_cross_type_value(self):
        e=copy.deepcopy(self.e);e['fibres']['C']=2
        with self.assertRaises(m.Rejected):m.eval_value(m.cast(m.gen(),m.lit(0,'C')),e)
    def test_positive_weakening_not_replay(self):
        target=m.bool_env((0,1));self.assertEqual(m.eval_value(self.t,target)[0],'B')
        with self.assertRaises(m.Rejected):m.replay_receipt({'term':self.t,'expected':m.lit(1)},self.e,target)
    def test_evidence(self):
        r=m.evidence();self.assertEqual(r['natural_under_target_flip'],[]);self.assertTrue(r['fixed_input_2_replay_succeeds_under_changed_action'])
if __name__=='__main__':unittest.main()
