#!/usr/bin/env python3
"""Tests of the R016 declared operational fragment, not a HoTT kernel."""
from pathlib import Path
import importlib.util
import sys
import unittest

PATH = Path(__file__).resolve().parents[1] / 'research/r016_axiomatic_transport.py'
spec = importlib.util.spec_from_file_location('r016_fragment', PATH)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)


class FragmentTests(unittest.TestCase):
    def test_bool_type(self):
        self.assertEqual(m.type_of(m.Bit(1)), m.BOOL)

    def test_invalid_bool_rejected(self):
        for bad in (-1, 2, True, '1'):
            with self.assertRaises(ValueError):
                m.Bit(bad)

    def test_unbound_variable_rejected(self):
        self.assertEqual(m.normalize(m.Var(0))['status'], 'ILL_TYPED')

    def test_context_variable(self):
        self.assertEqual(m.type_of(m.Var(1), (m.BOOL_PATH, m.BOOL)), m.BOOL)

    def test_invalid_application(self):
        self.assertEqual(m.normalize(m.App(m.Bit(1), m.Bit(0)))['status'], 'ILL_TYPED')

    def test_invalid_branch_types(self):
        self.assertEqual(m.normalize(m.If(m.Bit(0), m.Bit(1), m.ReflBool()))['status'], 'ILL_TYPED')

    def test_invalid_condition(self):
        self.assertEqual(m.normalize(m.If(m.ReflBool(), m.Bit(1), m.Bit(0)))['status'], 'ILL_TYPED')

    def test_invalid_transport_path(self):
        self.assertEqual(m.normalize(m.CoeBool(m.Bit(0), m.Bit(1)))['status'], 'ILL_TYPED')

    def test_invalid_transport_argument(self):
        self.assertEqual(m.normalize(m.CoeBool(m.ReflBool(), m.ReflBool()))['status'], 'ILL_TYPED')

    def test_ua_requires_bijection(self):
        for bad in ((0, 0), (1, 1), (0, 2), [0, 1], (True, 0)):
            with self.assertRaises(ValueError):
                m.UaBool(bad)

    def test_beta_identity(self):
        self.assertEqual(m.normalize(m.App(m.Lam(m.BOOL, m.Var(0)), m.Bit(1)))['value'], 1)

    def test_beta_outer_variable_under_binder(self):
        # (lambda x. lambda y. x) true false = true
        term = m.App(m.App(m.Lam(m.BOOL, m.Lam(m.BOOL, m.Var(1))), m.Bit(1)), m.Bit(0))
        self.assertEqual(m.normalize(term)['value'], 1)

    def test_beta_inner_variable_shadows_outer(self):
        term = m.App(m.App(m.Lam(m.BOOL, m.Lam(m.BOOL, m.Var(0))), m.Bit(1)), m.Bit(0))
        self.assertEqual(m.normalize(term)['value'], 0)

    def test_substitution_avoids_capture(self):
        # Substitute a free variable through a lambda: it must remain free.
        t = m.substitute(m.Lam(m.BOOL, m.Var(1)), 0, m.Var(0))
        self.assertEqual(t, m.Lam(m.BOOL, m.Var(1)))

    def test_shift_preserves_bound_variable(self):
        self.assertEqual(m.shift(m.Lam(m.BOOL, m.Var(0)), 3), m.Lam(m.BOOL, m.Var(0)))

    def test_shift_moves_free_variable(self):
        self.assertEqual(m.shift(m.Lam(m.BOOL, m.Var(1)), 1), m.Lam(m.BOOL, m.Var(2)))

    def test_negative_shift_rejected(self):
        with self.assertRaises(ValueError):
            m.shift(m.Var(0), -1)

    def test_false_branch(self):
        self.assertEqual(m.normalize(m.If(m.Bit(0), m.Bit(0), m.Bit(1)))['value'], 1)

    def test_true_branch(self):
        self.assertEqual(m.normalize(m.If(m.Bit(1), m.Bit(0), m.Bit(1)))['value'], 0)

    def test_refl_coercion(self):
        self.assertEqual(m.normalize(m.CoeBool(m.ReflBool(), m.Bit(1)))['value'], 1)

    def test_opaque_transport_no_basic_redex(self):
        t = m.CoeBool(m.UaBool((1, 0)), m.Bit(0))
        self.assertIsNone(m.step(t))
        r = m.normalize(t)
        self.assertEqual(r['status'], 'NORMAL_NONCANONICAL')
        self.assertEqual(r['steps'], 0)
        self.assertFalse(r['divergence_proved'])

    def test_ua_identity_does_not_automatically_become_refl(self):
        self.assertEqual(m.normalize(m.CoeBool(m.UaBool((0, 1)), m.Bit(0)))['status'], 'NORMAL_NONCANONICAL')

    def test_strong_normalization_reduces_transport_argument(self):
        t = m.CoeBool(m.UaBool((1, 0)), m.App(m.Lam(m.BOOL, m.Var(0)), m.Bit(1)))
        r = m.normalize(t)
        self.assertEqual(r['status'], 'NORMAL_NONCANONICAL')
        self.assertEqual(r['steps'], 1)
        self.assertEqual(r['normal_form'], 'coe(ua(not), true)')

    def test_path_expression_reduces_to_refl(self):
        p = m.App(m.Lam(m.BOOL_PATH, m.Var(0)), m.ReflBool())
        r = m.normalize(m.CoeBool(p, m.Bit(1)))
        self.assertEqual(r['value'], 1)

    def test_boolean_observer_blocked(self):
        t = m.If(m.CoeBool(m.UaBool((1, 0)), m.Bit(0)), m.Bit(0), m.Bit(1))
        self.assertEqual(m.normalize(t)['status'], 'NORMAL_NONCANONICAL')

    def test_discarding_noncanonical_argument_returns(self):
        t = m.App(m.Lam(m.BOOL, m.Bit(0)), m.CoeBool(m.UaBool((1, 0)), m.Bit(0)))
        self.assertEqual(m.normalize(t)['value'], 0)

    def test_direct_permutations(self):
        for table in ((0, 1), (1, 0)):
            for bit in (0, 1):
                self.assertEqual(m.normalize(m.App(m.permutation_term(table), m.Bit(bit)))['value'], table[bit])

    def test_proof_rewrite_recorded_not_implicit_kernel_step(self):
        t = m.CoeBool(m.UaBool((1, 0)), m.Bit(0))
        r = m.normalize(t, 'PROOF_GUIDED_REWRITE')
        self.assertEqual(r['value'], 1)
        self.assertIn('NOT_KERNEL_REDUCTION', r['trace'][0]['rule'])

    def test_nested_transports_parity(self):
        t = m.CoeBool(m.UaBool((1, 0)), m.CoeBool(m.UaBool((1, 0)), m.Bit(1)))
        self.assertEqual(m.normalize(t, 'PROOF_GUIDED_REWRITE')['value'], 1)
        self.assertEqual(m.normalize(t)['status'], 'NORMAL_NONCANONICAL')

    def test_insufficient_fuel_does_not_prove_divergence(self):
        t = m.App(m.Lam(m.BOOL, m.Var(0)), m.Bit(1))
        r = m.normalize(t, fuel=0)
        self.assertEqual(r['status'], 'FUEL_EXHAUSTED')
        self.assertFalse(r['divergence_proved'])
        self.assertEqual(m.normalize(t, fuel=1)['value'], 1)

    def test_normal_form_at_zero_fuel_not_timeout(self):
        self.assertEqual(m.normalize(m.Bit(1), fuel=0)['status'], 'VALUE')
        self.assertEqual(m.normalize(m.CoeBool(m.UaBool((0, 1)), m.Bit(0)), fuel=0)['status'], 'NORMAL_NONCANONICAL')

    def test_invalid_fuel(self):
        for bad in (-1, True, 0.5):
            with self.assertRaises(ValueError):
                m.normalize(m.Bit(1), fuel=bad)

    def test_unknown_mode_rejected(self):
        with self.assertRaises(ValueError):
            m.normalize(m.Bit(1), mode='CUBICAL')

    def test_strong_reduction_under_lambda_preserves_type(self):
        t = m.Lam(m.BOOL, m.App(m.Lam(m.BOOL, m.Var(0)), m.Var(0)))
        r = m.normalize(t)
        self.assertEqual(r['steps'], 1)
        self.assertEqual(r['normal_form'], '(lambda:Bool. #0)')
        self.assertEqual(r['type'], '(Bool -> Bool)')

    def test_finite_family_counts(self):
        r = m.run_experiments(6)
        self.assertEqual(r['family_inputs'], 254)
        self.assertEqual(r['basic_family_noncanonical'], 252)
        self.assertEqual(r['basic_family_values'], 2)
        self.assertFalse(r['scope']['full_hott_kernel'])
        self.assertFalse(r['scope']['cubical_implementation'])

    def test_invalid_family_bound(self):
        for bound in (-1, 9, True):
            with self.assertRaises(ValueError):
                m.run_experiments(bound)


if __name__ == '__main__':
    unittest.main(verbosity=2)
