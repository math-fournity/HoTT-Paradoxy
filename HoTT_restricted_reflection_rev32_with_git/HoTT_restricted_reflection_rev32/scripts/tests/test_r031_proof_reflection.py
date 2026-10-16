#!/usr/bin/env python3
"""Tests for the declared finite certificate rules, not HoTT metatheory."""
from pathlib import Path
import importlib.util
import sys
import unittest

source = Path(__file__).resolve().parents[1] / 'research/r031_proof_reflection.py'
spec = importlib.util.spec_from_file_location('r031_proof_reflection', source)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)

class CertificateTests(unittest.TestCase):
    def test_identity_has_no_trusted_theorems(self):
        p=m.atom('P'); r=m.replay(m.identity_certificate(p), {})
        self.assertEqual(r['closed_theorem_parameters'], [])
        self.assertEqual(r['conclusion'], '(P -> P)')
    def test_closed_necessitation(self):
        r=m.replay(m.identity_certificate(m.atom('P'), True), {})
        self.assertEqual(r['conclusion'], 'Box((P -> P))')
    def test_loeb_dependency_identity(self):
        c,e=m.loeb_certificate(); r=m.replay(c,e)
        self.assertEqual(r['conclusion'], 'BOTTOM')
        self.assertEqual(set(r['closed_theorem_parameters']), set(e))
        self.assertFalse(r['parameter_proofs_checked'])
        self.assertFalse(r['hott_kernel_verification'])
    def test_other_target(self):
        c,e=m.loeb_certificate(m.atom('Other')); r=m.replay(c,e)
        self.assertEqual(r['conclusion'],'Other')
    def test_globals_remain_in_necessitation(self):
        c,e=m.loeb_certificate(); r=m.replay(c,e)
        self.assertEqual(set(r['trace'][19]['closed_theorem_parameters']),set(e))
    def test_all_negatives(self):
        for name,c,e in m.negative_cases():
            with self.subTest(name=name), self.assertRaises(m.Rejected):
                m.replay(c,e)
    def test_context_identity_matters(self):
        p=m.atom('P'); b=m.Builder()
        h1=b.add('hyp',formula=p); h2=b.add('hyp',formula=p)
        a=b.add('intro',hypothesis=h1,body=h2)
        b.add('nec',body=a)
        with self.assertRaises(m.Rejected):m.replay(b.finish(m.box(m.imp(p,p))),{})
    def test_empty_rejected(self):
        with self.assertRaises(m.Rejected):
            m.replay({'schema':'r031-conditional-k4/v1','nodes':[],'conclusion':m.BOTTOM},{})
    def test_extra_header_field_rejected(self):
        c=m.identity_certificate(m.atom('P'));c['verified']=True
        with self.assertRaises(m.Rejected):m.replay(c,{})
    def test_whitelist_content_not_overridden(self):
        c,e=m.loeb_certificate();e['Reflection']=m.imp(m.atom('X'),m.BOTTOM)
        with self.assertRaises(m.Rejected):m.replay(c,e)

if __name__=='__main__':unittest.main(verbosity=2)
