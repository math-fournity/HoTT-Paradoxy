#!/usr/bin/env python3
"""Finite positive/negative tests. General results are separate paper proofs."""
import importlib.util
import sys
import json
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('r032',ROOT/'scripts/research/r032_restricted_reflection.py')
r=importlib.util.module_from_spec(spec);sys.modules[spec.name]=r;spec.loader.exec_module(r)
P,Q,R=r.atom(0),r.atom(1),r.atom(2)
ID=r.lam(P,r.var(0))

class ReflectionTests(unittest.TestCase):
    def reject(self,call):
        with self.assertRaises(r.Rejected): call()
    def test_01_identity(self):
        self.assertEqual(r.infer(ID,{}).formula,r.imp(P,P))
    def test_02_composition(self):
        proof=r.lam(r.imp(P,Q),r.lam(r.imp(Q,R),r.lam(P,r.app(r.var(1),r.app(r.var(2),r.var(0))))))
        c=r.infer(proof,{})
        self.assertEqual(c.formula,r.imp(r.imp(P,Q),r.imp(r.imp(Q,R),r.imp(P,R))))
        value=r.interpret(proof,{},{})(lambda x:x+1)(lambda x:x*2)(4)
        self.assertEqual(value,10)
    def test_03_ill_typed_application(self):
        self.reject(lambda:r.infer(r.app(ID,r.lam(Q,r.var(0))),{}))
    def test_04_free_quote_rejected(self):
        self.reject(lambda:r.quote({},r.var(0)))
    def test_05_refl_expands(self):
        self.assertEqual(r.expand(r.reflect(r.quote({},ID)),{}),ID)
    def test_06_refl_under_binder(self):
        p=r.lam(P,r.app(r.reflect(r.quote({},ID)),r.var(0)))
        self.assertEqual(r.infer(r.expand(p,{}),{}).formula,r.imp(P,P))
    def test_07_false_axiom_is_conditional(self):
        p=r.absurd(P,r.ax('bad'))
        self.assertEqual(r.infer(p,{'bad':r.BOT}).support,frozenset({'bad'}))
        self.reject(lambda:r.interpret(p,{'bad':r.BOT},{}))
    def test_08_changed_used_axiom_rejected(self):
        pkg=r.quote({'permit':P},r.ax('permit'))
        self.reject(lambda:r.migrate(pkg,{'permit':Q}))
    def test_09_irrelevant_change_accepted(self):
        pkg=r.quote({'irrelevant':r.BOT},ID)
        self.assertEqual(r.migrate(pkg,{'irrelevant':Q}),ID)
    def test_10_used_preserved_accepted(self):
        pkg=r.quote({'p':P},r.ax('p'))
        self.assertEqual(r.infer(r.migrate(pkg,{'p':P,'q':Q}),{'p':P,'q':Q}).formula,P)
    def test_11_actual_bridge_axiom_deleted(self):
        pkg=r.quote({'id':r.imp(P,P)},r.ax('id'))
        self.assertEqual(r.migrate(pkg,{}, {'id':ID}),ID)
    def test_12_bridge_wrong_type_rejected(self):
        pkg=r.quote({'p':P},r.ax('p'))
        self.reject(lambda:r.migrate(pkg,{}, {'p':ID}))
    def test_13_bridge_not_closed_rejected(self):
        pkg=r.quote({'p':P},r.ax('p'))
        self.reject(lambda:r.migrate(pkg,{}, {'p':r.var(0)}))
    def test_14_bridge_checked_in_target(self):
        pkg=r.quote({'p':P},r.ax('p'))
        self.reject(lambda:r.migrate(pkg,{'q':Q}, {'p':r.ax('p')}))
    def test_15_bridge_under_two_binders(self):
        source={'id':r.imp(P,P)}
        proof=r.lam(Q,r.lam(P,r.app(r.ax('id'),r.var(0))))
        moved=r.migrate(r.quote(source,proof),{}, {'id':ID})
        self.assertEqual(r.infer(moved,{}).formula,r.imp(Q,r.imp(P,P)))
        self.assertEqual(r.interpret(moved,{},{})(99)(True),True)
    def test_16_digest_tamper(self):
        pkg=r.quote({'p':P},r.ax('p'));pkg['environment']['p']=Q
        self.reject(lambda:r.check_package(pkg))
    def test_17_goal_tamper(self):
        pkg=r.quote({},ID);pkg['goal']=P
        self.reject(lambda:r.check_package(pkg))
    def test_18_support_tamper(self):
        pkg=r.quote({'p':P},r.ax('p'));pkg['support']=[]
        self.reject(lambda:r.check_package(pkg))
    def test_19_bare_receipt_rejected(self):
        self.reject(lambda:r.expand(r.reflect({'accepted':True,'goal':P}),{}))
    def test_20_reflection_not_allowed_inside_base(self):
        self.reject(lambda:r.quote({},r.reflect(r.quote({},ID))))
    def test_21_cyclic_input(self):
        p=r.lam(P,{});p['body']=p
        self.reject(lambda:r.infer(p,{}))
    def test_22_bool_index_rejected(self):
        self.reject(lambda:r.infer(r.var(True),{},(P,P)))
    def test_23_no_falsehood_introduction(self):
        self.reject(lambda:r.infer({'rule':'bottom'},{}))
    def test_24_countermodel(self):
        v={0:False,1:True}
        self.assertTrue(r.truth(Q,v));self.assertFalse(r.truth(P,v))
    def test_25_whole_transfer_yields_axiom_bridges(self):
        source={'identity':r.imp(P,P),'compose':r.imp(r.imp(P,Q),r.imp(P,Q))}
        bridges={'identity':ID,'compose':r.lam(r.imp(P,Q),r.var(0))}
        for label,a in source.items():
            transported=r.migrate(r.quote(source,r.ax(label)),{},bridges)
            self.assertEqual(r.infer(transported,{}).formula,a)
    def test_26_support_sufficient_not_necessary_for_goal(self):
        # This concrete derivation uses p, yet its conclusion has an independent proof.
        proof=r.app(r.lam(P,r.lam(Q,r.var(0))),r.ax('p'))
        pkg=r.quote({'p':P},proof)
        self.reject(lambda:r.migrate(pkg,{}))
        other=r.lam(Q,r.var(0))
        self.assertEqual(r.infer(other,{}).formula,pkg['goal'])
    def test_27_relabel_with_proof(self):
        pkg=r.quote({'old':P},r.ax('old'))
        moved=r.migrate(pkg,{'new':P},{'old':r.ax('new')})
        self.assertEqual(r.infer(moved,{'new':P}).support,frozenset({'new'}))
    def test_28_semantic_realisers_needed_only_for_support(self):
        self.assertTrue(r.interpret(ID,{'falsehood':r.BOT},{ })(True))
    def test_29_extra_rule_field_not_trusted(self):
        p=dict(ID,verified=True)
        self.reject(lambda:r.infer(p,{}))
    def test_30_unknown_rule_rejected(self):
        self.reject(lambda:r.infer({'rule':'verified_by_other_ai','goal':P},{}))

    def test_31_json_roundtrip_checked(self):
        pkg=r.quote({'p':P},r.ax('p'))
        restored=r.package_from_json(json.loads(r.encode_data(pkg)))
        self.assertEqual(restored,pkg)
    def test_32_serialized_false_index_rejected(self):
        self.reject(lambda:r.formula_from_json(['atom',True]))
    def test_33_sample_counterexample_source_consistent(self):
        # Both snapshots have Boolean models; the rejection is not based on
        # inserting an inconsistent axiom into the source theory.
        result=r.migration_claims()['changed_axiom']
        self.assertTrue(all(r.truth(a,{0:True,1:True}) for a in result['source'].values()))
        self.assertTrue(all(r.truth(a,{0:False,1:True}) for a in result['target'].values()))

if __name__=='__main__': unittest.main(verbosity=2)
