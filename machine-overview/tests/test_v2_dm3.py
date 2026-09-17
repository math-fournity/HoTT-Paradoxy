"""Self-test for the DM3 fragment (gap-A acceptance unit).

Acceptance anchors:
* formal/V2DM3.agda sec 8 -- the denominator is FINITE (55 ground values);
* ops closure: every declared op is total on every ground value;
* the three structural witnesses of mirror sec 6 and their same-value
  controls are reproduced EXACTLY by the canonical Python semantics;
* the three witnesses are delay-invisible (L1 cannot see them);
* DM3 is a non-boolean De Morgan algebra (the boolean law FAILS) and it does
  not embed into the point-set boolean face lattice preserving meet and neg;
* the mirror's own algebra laws (commutativity, involution, De Morgan,
  absorption) hold of the canonical Python recomputation.

ORACLE SCOPE (015 §5 / F-011 / 017 §5, upgraded by this unit): this is an
ENGINEERING acceptance test of the DM3 half of the gap-A unit.  It produces no
mathematical conclusion about the real interval I; the only registered
negative fact is that the boolean law is not needed, and its scope is the
algebra DM3 itself.
"""
from __future__ import annotations

import unittest

from machine_overview import v2_dm3 as v2
from machine_overview import v2_dm3_chain as C
from machine_overview.util import MachineOverviewError


class NonClaimRegistryTest(unittest.TestCase):
    def test_registry_is_present_and_nonempty(self):
        # the oracle-scope disclosure lives on the grammar; assert it survives
        import json
        from pathlib import Path
        grammar = json.loads(
            Path("grammars/v2-dm3-a-v1.json").read_text(encoding="utf-8"))
        self.assertIn("scope_disclosure", grammar)
        self.assertIn("DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT",
                      grammar["scope_disclosure"])
        self.assertIn("interval_i_confirmed", grammar["scope_disclosure"])


class DM3FinitenessTest(unittest.TestCase):
    def test_declared_sizes(self):
        self.assertEqual(len(v2.DM3_ELEMENTS), 3)
        self.assertEqual(len(v2.B3_ELEMENTS), 3)
        self.assertEqual(v2.DELAY_INDEX_MAX, 2)
        self.assertEqual(v2.TOWER_MAX, 2)

    def test_ground_value_count_is_55(self):
        values = v2.ground_values()
        self.assertEqual(len(values), 55)
        self.assertEqual(len(set(values)), 55)
        self.assertEqual(values[0], v2.omega())

    def test_ret_enforces_generator_bounds(self):
        with self.assertRaises(MachineOverviewError):
            v2.ret(3, True, 0, 0)
        with self.assertRaises(MachineOverviewError):
            v2.ret(0, True, 3, 0)
        with self.assertRaises(MachineOverviewError):
            v2.ret(0, True, 0, 3)

    def test_single_op_and_op_list_denominators(self):
        self.assertEqual(len(v2.single_ops()), 16)
        ids = [name for name, _ in v2.declared_op_lists()]
        self.assertEqual(len(ids), 64)
        self.assertEqual(len(set(ids)), 64)


class DM3AlgebraTest(unittest.TestCase):
    """The mirror's own algebra laws (V2Cofibration sec 10), recomputed."""

    def test_chain_order(self):
        self.assertTrue(v2.dm3_leq(0, 1) and v2.dm3_leq(1, 2) and v2.dm3_leq(0, 2))
        self.assertFalse(v2.dm3_leq(1, 0) or v2.dm3_leq(2, 1) or v2.dm3_leq(2, 0))

    def test_meet_is_order_consistent(self):
        for x in range(3):
            for y in range(3):
                # x <= y iff meet x y == x (mirror: dm3LeMeet)
                self.assertEqual(v2.dm3_leq(x, y), v2.dm3_meet(x, y) == x)

    def test_commutativity(self):
        for x in range(3):
            for y in range(3):
                self.assertEqual(v2.dm3_meet(x, y), v2.dm3_meet(y, x))
                self.assertEqual(v2.dm3_join(x, y), v2.dm3_join(y, x))

    def test_involution(self):
        for x in range(3):
            self.assertEqual(v2.dm3_neg(v2.dm3_neg(x)), x)

    def test_de_morgan_laws(self):
        for x in range(3):
            for y in range(3):
                self.assertEqual(v2.dm3_neg(v2.dm3_meet(x, y)),
                                 v2.dm3_join(v2.dm3_neg(x), v2.dm3_neg(y)))
                self.assertEqual(v2.dm3_neg(v2.dm3_join(x, y)),
                                 v2.dm3_meet(v2.dm3_neg(x), v2.dm3_neg(y)))

    def test_absorption(self):
        for x in range(3):
            for y in range(3):
                self.assertEqual(v2.dm3_meet(x, v2.dm3_join(x, y)), x)
                self.assertEqual(v2.dm3_join(x, v2.dm3_meet(x, y)), x)

    def test_bottom_and_top(self):
        self.assertEqual(v2.dm3_meet(0, 1), 0)
        self.assertEqual(v2.dm3_join(2, 1), 2)

    def test_boolean_law_FAILS(self):
        # the defining non-boolean fact: a && ~a = a != 0 (mirror: dm3NonBoolean)
        self.assertEqual(v2.dm3_meet(1, v2.dm3_neg(1)), 1)
        self.assertNotEqual(v2.dm3_meet(1, v2.dm3_neg(1)), 0)
        self.assertTrue(v2.dm3_non_boolean())


class OpsTotalityTest(unittest.TestCase):
    def test_every_op_is_total_on_every_ground_value(self):
        for value in v2.ground_values():
            for op in v2.single_ops():
                try:
                    v2.apply_ops([op], value)
                except MachineOverviewError:
                    self.fail(f"op {op} not total on {value}")

    def test_observation_mode_tracks_last_op(self):
        self.assertEqual(v2.observation_mode([]), "delay")
        self.assertEqual(v2.observation_mode([{"kind": "supply", "d": 1}]), "delay")
        self.assertEqual(v2.observation_mode([{"kind": "supply", "d": 1},
                                             {"kind": "fill"}]), "availability")
        self.assertEqual(v2.observation_mode([{"kind": "tower", "level": 1}]), "tower")
        self.assertEqual(v2.observation_mode([{"kind": "between", "a": 0, "b": 2}]),
                         "density")

    def test_unknown_op_is_rejected(self):
        with self.assertRaises(MachineOverviewError):
            v2.apply_ops([{"kind": "nope"}], v2.omega())

    def test_supply_then_fill_makes_the_supplied_coordinate_available(self):
        left = v2.ret(0, True, 1, 0)
        right = v2.ret(0, True, 2, 0)
        ops = [{"kind": "supply", "d": 1}, {"kind": "fill"}]
        (ol, _), (orr, _) = v2.apply_ops(ops, left), v2.apply_ops(ops, right)
        self.assertEqual(ol, ("availability", "available"))
        self.assertEqual(orr, ("availability", "pending"))


class WitnessTest(unittest.TestCase):
    def test_declared_witnesses_match_the_mirror(self):
        result = v2.check_declared_witnesses()
        self.assertTrue(result["all_match"])
        for row in result["rows"]:
            self.assertTrue(row["matches_mirror"], row)

    def test_declared_witnesses_are_delay_invisible(self):
        result = v2.check_declared_witnesses()
        for witness_id, invisible in result["delay_invisible"].items():
            self.assertTrue(invisible, f"{witness_id} is NOT delay-invisible")

    def test_same_value_controls_never_separate(self):
        for spec in v2.SAME_VALUE_CONTROLS:
            got = v2.separates(spec["ops"], spec["left"], spec["right"])
            self.assertFalse(got[0], f"{spec['witness_id']} separated on identical inputs")

    def test_l1_erasure_of_the_three_witnesses(self):
        for spec in v2.DECLARED_WITNESSES:
            self.assertTrue(C.l1_invisible(spec["left"], spec["right"]))
            self.assertEqual(C.l1_erase(spec["left"]),
                             C.l1_erase(spec["right"]))


class GrammarSearchTest(unittest.TestCase):
    def setUp(self):
        self.grammar = C.load_grammar("grammars/v2-dm3-a-v1.json")

    def test_grammar_loads(self):
        self.assertEqual(self.grammar["grammar_id"], "V2-DM3-A-v1")
        self.assertEqual(self.grammar["backend"], "v2-dm3")

    def test_atoms_and_contexts(self):
        self.assertEqual(len(C.enumerate_atoms(self.grammar)), 55)
        contexts = C.enumerate_contexts(self.grammar)
        self.assertTrue(contexts)
        # every context is non-empty and within the declared depth
        for ops in contexts:
            self.assertTrue(ops)
            self.assertLessEqual(len(ops), self.grammar["context_depth_max"])

    def test_membership_rejects_out_of_grammar_candidates(self):
        left = v2.ret(0, True, 1, 0)
        right = v2.ret(0, True, 2, 0)
        ok, reason = C.within_grammar_witness([{"kind": "between", "a": 1, "b": 0}],
                                              left, right, self.grammar)
        self.assertFalse(ok)
        self.assertEqual(reason, "BETWEEN_PAIR")
        ok, reason = C.within_grammar_witness([{"kind": "tower", "level": 3}],
                                              left, right, self.grammar)
        self.assertFalse(ok)
        self.assertEqual(reason, "TOWER_LEVEL")

    def test_search_is_complete_and_order_independent(self):
        semantics = C.compute_search_semantics(self.grammar, {})
        stats = semantics["statistics"]
        self.assertTrue(stats["complete_within_declared_grammar"])
        self.assertEqual(stats["pair_context_checks"], stats["checks_planned"])
        self.assertEqual(stats["grammar_violations"], 0)
        self.assertFalse(stats["truncated"])
        self.assertEqual(sorted(stats["separation_kind_histogram"]),
                         sorted(v2.SEPARATION_KINDS))
        self.assertEqual(semantics["calibration_match"]["status"], "ALL_PRESENT")
        order = C.order_independence(self.grammar, {})
        self.assertTrue(order["statistics_match"])
        self.assertTrue(order["witness_sets_equal"])

    def test_reduction_never_leaves_the_grammar(self):
        semantics = C.compute_search_semantics(self.grammar, {})
        for witness in semantics["witnesses"]:
            left = v2.value_from_json(witness["pair"]["left"])
            right = v2.value_from_json(witness["pair"]["right"])
            ok, reason = C.within_grammar_witness(witness["ops"], left, right,
                                                  self.grammar)
            self.assertTrue(ok, f"{witness['witness_id']} left the grammar: {reason}")
            separated, _ol, _orr, _kind = v2.separates(witness["ops"], left, right)
            self.assertTrue(separated, f"{witness['witness_id']} does not separate")


class NonEmbeddingTest(unittest.TestCase):
    def test_no_point_set_embedding(self):
        result = v2.no_point_set_embedding()
        self.assertTrue(result["result"])
        self.assertEqual(result["domain"]["candidate_functions"], 4096)
        self.assertEqual(result["domain"]["functions_preserving_meet_and_neg"], 0)


if __name__ == "__main__":
    unittest.main()
