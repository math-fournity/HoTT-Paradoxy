"""Self-test for the declared L2-cofibration fragment (V2 calibration model).

Acceptance anchor: ``Atria的方案/修订片/015`` §3.4 (ii) -- finiteness of the
declared ``FACES`` / ``SUPPLIED`` / ``TOWER_MAX`` and ops closure, plus the
explicit registry of what the model does NOT claim (see NON_CLAIM_REGISTRY).

This is an ENGINEERING acceptance test of a calibration model.  It produces no
mathematical conclusion (F-011): every separation computed here is an
enumerator-internal candidate, and oracle verdicts must come from the native
kernel on the real interval ``I``.
"""
from __future__ import annotations

import unittest
from itertools import product

from machine_overview import model as l1
from machine_overview import v2_cofibration as v2
from machine_overview.util import MachineOverviewError

I, J, ONE, ZERO = v2.FACE_I, v2.FACE_J, v2.FACE_ONE, v2.FACE_ZERO

#: Explicit registry of what this model does NOT claim.  A test asserts the
#: registry survives, so the disclosures cannot be silently deleted.
NON_CLAIM_REGISTRY = {
    "BOOLEAN_LAWS_HOLD_IN_MODEL_ONLY": (
        "face_min(a, face_neg(a)) == FACE_ZERO and face_max(a, face_neg(a)) == FACE_ONE "
        "hold for all 16 faces in this point-set model, but the interval I is a De "
        "Morgan algebra in which they FAIL.  The model is SOUND but NOT COMPLETE "
        "(revision 015 §3.4): a separation witness valid in the model need not lift "
        "to the real interval."
    ),
    "DENSITY_OP_IS_VALUE_DEPENDENT": (
        "between(a, b) tests the VALUE's own face for lying strictly inside (a, b).  A "
        "value-independent reading would make density_observation unreachable by "
        "separates, contradicting revision 015 §3.2/§3.3."
    ),
    "DELAY_INDEX_BOUND_IS_GENERATOR_ONLY": (
        "ret() rejects n > DELAY_INDEX_MAX / level > TOWER_MAX as GENERATOR discipline, "
        "but later/bind compose indices (n1 + n2 + 1) and can exceed DELAY_INDEX_MAX, "
        "mirroring l1 model.py.  The enumeration denominator is bounded by the search "
        "layer's declared depth, not by the value constructor."
    ),
    "ENUMERATOR_ONLY": (
        "Every separation computed by this module is an enumerator-internal candidate; "
        "oracle verdicts must come from the native Cubical Agda kernel on the real "
        "interval I (F-011, revision 015 §3.4)."
    ),
}


def ground_values():
    """All 289 declared ground values: omega + ret(n, b, face, level)."""
    out = [v2.omega()]
    for n, b, face, level in product(
        range(v2.DELAY_INDEX_MAX + 1),
        v2.BOOLS,
        range(v2.FACE_COUNT),
        range(v2.TOWER_MAX + 1),
    ):
        out.append(v2.ret(n, b, face, level))
    return out


GROUND = ground_values()


def project_to_l1(value):
    """Drop the structural axis (face, level); keep the computation axis."""
    if value[0] == "omega":
        return l1.omega()
    return ("ret", value[1], value[2])


def value_well_formed(value) -> bool:
    if value == ("omega",):
        return True
    if value[0] != "ret" or len(value) != 5:
        return False
    _kind, n, b, face, level = value
    return (
        type(n) is int and n >= 0
        and type(b) is bool
        and type(face) is int and 0 <= face < v2.FACE_COUNT
        and type(level) is int and 0 <= level <= v2.TOWER_MAX
    )


def observation_well_formed(obs) -> bool:
    if obs[0] == "delay":
        return value_well_formed(obs[1])
    if obs[0] == "optional":
        return obs[1] == ("none",) or (obs[1][0] == "some" and type(obs[1][1]) is bool)
    if obs[0] == "availability":
        return obs[1] in v2.AVAILABILITY
    if obs[0] in ("tower", "density"):
        return type(obs[1]) is bool
    return False


CONT = {
    True: v2.ret(0, True, I, 0),
    False: v2.ret(1, False, J, 1),
}
CONT_JSON = v2.continuation_to_json(CONT)
PARTNER_JSON = v2.value_to_json(v2.ret(1, False, J, 1))

#: One representative op-list per declared kind (totality + closure checks).
OP_SPECS = [
    ("race_left", [{"kind": "race_left", "partner": PARTNER_JSON}]),
    ("race_right", [{"kind": "race_right", "partner": PARTNER_JSON}]),
    ("bind", [{"kind": "bind", "continuation": CONT_JSON}]),
    ("supply", [{"kind": "supply", "face": I}]),
    ("deadline", [{"kind": "deadline", "k": 1}]),
    ("fill", [{"kind": "supply", "face": I}, {"kind": "fill"}]),
    ("fill_of", [{"kind": "fill_of", "face": I}]),
    ("tower", [{"kind": "tower", "level": 1}]),
    ("between", [{"kind": "between", "a": ZERO, "b": ONE}]),
    ("race+deadline", [{"kind": "race_left", "partner": PARTNER_JSON}, {"kind": "deadline", "k": 1}]),
    ("bind+tower", [{"kind": "bind", "continuation": CONT_JSON}, {"kind": "tower", "level": 1}]),
]


class NonClaimRegistryTest(unittest.TestCase):
    def test_registry_is_present_and_nonempty(self):
        for key, text in NON_CLAIM_REGISTRY.items():
            self.assertIsInstance(key, str)
            self.assertIsInstance(text, str)
            self.assertGreater(len(text), 40)
        self.assertEqual(
            set(NON_CLAIM_REGISTRY),
            {
                "BOOLEAN_LAWS_HOLD_IN_MODEL_ONLY",
                "DENSITY_OP_IS_VALUE_DEPENDENT",
                "DELAY_INDEX_BOUND_IS_GENERATOR_ONLY",
                "ENUMERATOR_ONLY",
            },
        )


class FaceFinitenessTest(unittest.TestCase):
    def test_declared_sizes(self):
        self.assertEqual(v2.POINT_COUNT, 4)
        self.assertEqual(v2.FACE_COUNT, 16)
        self.assertEqual(v2.FACE_ZERO, 0)
        self.assertEqual(v2.FACE_ONE, 15)
        self.assertEqual(len(v2.POINTS), 4)
        self.assertEqual(v2.TOWER_MAX, 2)
        self.assertEqual(v2.DELAY_INDEX_MAX, 2)

    def test_point_indexing_is_the_4_point_cube(self):
        # BOOLS = (True, False), so i then j iterates (T,T), (T,F), (F,T), (F,F).
        self.assertEqual(v2.POINTS, ((True, True), (True, False), (False, True), (False, False)))

    def test_faces_are_in_declared_range(self):
        for face in range(v2.FACE_COUNT):
            for k in range(v2.POINT_COUNT):
                self.assertIsInstance(v2.face_point(face, k), bool)
        for bad in (-1, v2.FACE_COUNT, 17, 2 ** 8):
            with self.assertRaisesRegex(MachineOverviewError, "FACE_OUT_OF_DECLARED_RANGE"):
                v2.face_point(bad, 0)

    def test_generator_faces_match_their_truth_tables(self):
        for k, (i, j) in enumerate(v2.POINTS):
            self.assertEqual(v2.face_point(ZERO, k), False)
            self.assertEqual(v2.face_point(ONE, k), True)
            self.assertEqual(v2.face_point(I, k), i)
            self.assertEqual(v2.face_point(J, k), j)

    def test_min_max_neg_are_pointwise_boolean(self):
        for a, b in product(range(v2.FACE_COUNT), repeat=2):
            for k in range(v2.POINT_COUNT):
                pa, pb = v2.face_point(a, k), v2.face_point(b, k)
                self.assertEqual(v2.face_point(v2.face_min(a, b), k), pa and pb)
                self.assertEqual(v2.face_point(v2.face_max(a, b), k), pa or pb)
                self.assertEqual(v2.face_point(v2.face_neg(a), k), not pa)

    def test_min_max_neg_closed_in_declared_range(self):
        for a, b in product(range(v2.FACE_COUNT), repeat=2):
            self.assertTrue(0 <= v2.face_min(a, b) < v2.FACE_COUNT)
            self.assertTrue(0 <= v2.face_max(a, b) < v2.FACE_COUNT)
        for a in range(v2.FACE_COUNT):
            self.assertTrue(0 <= v2.face_neg(a) < v2.FACE_COUNT)

    def test_generators_close_to_all_16_faces(self):
        reached = {ZERO, ONE, I, J}
        frontier = list(reached)
        while frontier:
            new = []
            for a in frontier:
                for b in list(reached):
                    for cand in (v2.face_min(a, b), v2.face_max(a, b), v2.face_neg(a)):
                        if cand not in reached:
                            reached.add(cand)
                            new.append(cand)
            frontier = new
        self.assertEqual(reached, set(range(v2.FACE_COUNT)))

    def test_face_between_existence_form(self):
        # With 4 points, the difference set is counted in POINTS; FACE_I = 3
        # covers indices 0,1, FACE_J = 5 covers indices 0,2, I|J = 7.
        self.assertTrue(v2.face_between(ZERO, ONE))      # diff = 4 points
        self.assertTrue(v2.face_between(I, ONE))         # diff = 2 points
        self.assertTrue(v2.face_between(ZERO, I))        # diff = 2 points
        self.assertFalse(v2.face_between(I, I))          # empty diff
        self.assertFalse(v2.face_between(I | J, ONE))    # diff = 1 point

    def test_face_strictly_between_positional_form(self):
        for f in range(1, v2.FACE_COUNT - 1):
            self.assertTrue(v2.face_strictly_between(ZERO, f, ONE))
        self.assertFalse(v2.face_strictly_between(ZERO, ZERO, ONE))  # f == lower bound
        self.assertFalse(v2.face_strictly_between(ZERO, ONE, ONE))   # f == upper bound
        self.assertFalse(v2.face_strictly_between(I, I, J))          # f not subset b
        self.assertTrue(v2.face_strictly_between(I, I | J, ONE))     # I < I|J < ONE


class DeMorganSoundnessTest(unittest.TestCase):
    """Exhaustive over the declared 16-face denominator (revision 015 §3.4)."""

    def test_commutativity(self):
        for a, b in product(range(v2.FACE_COUNT), repeat=2):
            self.assertEqual(v2.face_min(a, b), v2.face_min(b, a))
            self.assertEqual(v2.face_max(a, b), v2.face_max(b, a))

    def test_associativity(self):
        for a, b, c in product(range(v2.FACE_COUNT), repeat=3):
            self.assertEqual(v2.face_min(a, v2.face_min(b, c)), v2.face_min(v2.face_min(a, b), c))
            self.assertEqual(v2.face_max(a, v2.face_max(b, c)), v2.face_max(v2.face_max(a, b), c))

    def test_absorption(self):
        for a, b in product(range(v2.FACE_COUNT), repeat=2):
            self.assertEqual(v2.face_max(a, v2.face_min(a, b)), a)
            self.assertEqual(v2.face_min(a, v2.face_max(a, b)), a)

    def test_involution(self):
        for a in range(v2.FACE_COUNT):
            self.assertEqual(v2.face_neg(v2.face_neg(a)), a)

    def test_de_morgan_laws(self):
        for a, b in product(range(v2.FACE_COUNT), repeat=2):
            self.assertEqual(v2.face_neg(v2.face_min(a, b)), v2.face_max(v2.face_neg(a), v2.face_neg(b)))
            self.assertEqual(v2.face_neg(v2.face_max(a, b)), v2.face_min(v2.face_neg(a), v2.face_neg(b)))

    def test_BOTTOM_and_TOP(self):
        for a in range(v2.FACE_COUNT):
            self.assertEqual(v2.face_min(a, ZERO), ZERO)
            self.assertEqual(v2.face_max(a, ONE), ONE)

    def test_boolean_laws_hold_in_the_model_but_are_NOT_claimed_of_I(self):
        # This is the sound-but-not-complete boundary of §3.4: the model
        # validates boolean laws the real interval I does NOT satisfy.
        for a in range(v2.FACE_COUNT):
            self.assertEqual(v2.face_min(a, v2.face_neg(a)), ZERO)
            self.assertEqual(v2.face_max(a, v2.face_neg(a)), ONE)
        self.assertIn("BOOLEAN_LAWS_HOLD_IN_MODEL_ONLY", NON_CLAIM_REGISTRY)


class ValueDomainTest(unittest.TestCase):
    def test_ground_value_count_is_289(self):
        self.assertEqual(len(GROUND), 289)
        self.assertEqual(len(set(GROUND)), 289)
        self.assertEqual(v2.omega(), ("omega",))
        self.assertNotIn(("omega",), [v for v in GROUND if v[0] == "ret"])

    def test_ret_enforces_generator_bounds(self):
        with self.assertRaisesRegex(MachineOverviewError, "DELAY_INDEX_OUT_OF_DECLARED_RANGE"):
            v2.ret(v2.DELAY_INDEX_MAX + 1, True, I, 0)
        with self.assertRaisesRegex(MachineOverviewError, "LEVEL_OUT_OF_DECLARED_RANGE"):
            v2.ret(0, True, I, v2.TOWER_MAX + 1)
        with self.assertRaisesRegex(MachineOverviewError, "FACE_OUT_OF_DECLARED_RANGE"):
            v2.ret(0, True, v2.FACE_COUNT, 0)

    def test_later_and_omega(self):
        self.assertEqual(v2.later(v2.omega()), v2.omega())
        v = v2.ret(0, True, I, 2)
        stepped = v2.later(v)
        self.assertEqual(stepped[0], "ret")
        self.assertEqual(stepped[1], 1)
        self.assertEqual(stepped[2:], v[2:])

    def test_availability_states_are_declared(self):
        self.assertEqual(v2.AVAILABILITY, ("absent", "pending", "available"))

    def test_declared_observation_and_separation_kinds(self):
        self.assertEqual(v2.OBSERVATION_KINDS, ("delay", "optional", "availability", "tower", "density"))
        self.assertEqual(v2.SEPARATION_KINDS[:3], ("value_mismatch", "completion_divergence", "deadline_observation"))
        self.assertEqual(
            v2.SEPARATION_KINDS[3:],
            ("availability_observation", "level_observation", "density_observation"),
        )


class OpsTotalityTest(unittest.TestCase):
    def test_every_op_is_total_on_every_ground_value(self):
        for value in GROUND:
            for name, ops in OP_SPECS:
                try:
                    obs, supplied = v2.apply_ops(ops, value)
                except MachineOverviewError as exc:
                    self.fail(f"op {name} raised on {value!r}: {exc}")
                self.assertTrue(observation_well_formed(obs), f"{name} -> ill-formed {obs!r}")
                self.assertIsInstance(supplied, frozenset)
                for face in supplied:
                    self.assertTrue(0 <= face < v2.FACE_COUNT)

    def test_observation_mode_tracks_last_op(self):
        cases = [
            ([], "delay"),
            ([{"kind": "race_left", "partner": PARTNER_JSON}], "delay"),
            ([{"kind": "supply", "face": I}], "delay"),
            ([{"kind": "bind", "continuation": CONT_JSON}], "delay"),
            ([{"kind": "deadline", "k": 1}], "optional"),
            ([{"kind": "supply", "face": I}, {"kind": "fill"}], "availability"),
            ([{"kind": "fill_of", "face": I}], "availability"),
            ([{"kind": "tower", "level": 1}], "tower"),
            ([{"kind": "between", "a": ZERO, "b": ONE}], "density"),
            ([{"kind": "supply", "face": I}, {"kind": "tower", "level": 1}], "tower"),
        ]
        for ops, expected in cases:
            self.assertEqual(v2.observation_mode(ops), expected)

    def test_unknown_op_is_rejected(self):
        with self.assertRaisesRegex(MachineOverviewError, "UNKNOWN_CONTEXT_OP"):
            v2.apply_ops([{"kind": "no_such_op"}], v2.ret(0, True, I, 0))

    def test_supply_and_fill_of_track_supplied_faces(self):
        value = v2.ret(0, True, J, 0)
        _obs, supplied = v2.apply_ops([{"kind": "supply", "face": I}], value)
        self.assertEqual(supplied, frozenset({I}))
        _obs2, supplied2 = v2.apply_ops([{"kind": "supply", "face": I}, {"kind": "supply", "face": J}], value)
        self.assertEqual(supplied2, frozenset({I, J}))
        obs, _s = v2.apply_ops([{"kind": "fill_of", "face": J}], value, frozenset({I}))
        self.assertEqual(obs, ("availability", "pending"))
        obs, _s = v2.apply_ops([{"kind": "fill_of", "face": J}], value, frozenset({I, J}))
        self.assertEqual(obs, ("availability", "available"))

    def test_fill_availability_tri_state(self):
        # absent: no filler exists (omega)
        obs, _s = v2.apply_ops([{"kind": "fill"}], v2.omega())
        self.assertEqual(obs, ("availability", "absent"))
        # pending: filler exists but that face was not supplied
        obs, _s = v2.apply_ops([{"kind": "fill"}], v2.ret(0, True, J, 0))
        self.assertEqual(obs, ("availability", "pending"))
        # available: the value's face was supplied
        obs, _s = v2.apply_ops([{"kind": "supply", "face": J}, {"kind": "fill"}], v2.ret(0, True, J, 0))
        self.assertEqual(obs, ("availability", "available"))


class SeparationTest(unittest.TestCase):
    def test_l1_shared_three_kinds_coincide_with_l1(self):
        l1_kinds = {
            l1.separation_kind([{"kind": "deadline", "k": 0}], ("none",), ("some", True)),
            l1.separation_kind([], ("omega",), ("ret", 0, True)),
            l1.separation_kind([], ("ret", 0, True), ("ret", 0, False)),
        }
        self.assertEqual(l1_kinds, set(v2.SEPARATION_KINDS[:3]))

    def test_new_three_kinds_are_disjoint_from_l1(self):
        l1_kinds = {"deadline_observation", "completion_divergence", "value_mismatch"}
        self.assertEqual(set(v2.SEPARATION_KINDS[3:]) & l1_kinds, set())
        self.assertEqual(len(set(v2.SEPARATION_KINDS)), 6)

    # ---- positive controls: inputs delay-equivalent, new axis separates ----

    def test_positive_control_G_b_availability(self):
        ops = [{"kind": "supply", "face": I}, {"kind": "fill"}]
        left, right = v2.ret(0, True, I, 0), v2.ret(0, True, J, 0)
        self.assertTrue(v2.delay_equivalent(left, right))
        sep, ol, orr, kind = v2.separates(ops, left, right)
        self.assertTrue(sep)
        self.assertEqual(kind, "availability_observation")
        self.assertEqual(ol, ("availability", "available"))
        self.assertEqual(orr, ("availability", "pending"))

    def test_positive_control_G_c_level(self):
        ops = [{"kind": "tower", "level": 0}]
        left, right = v2.ret(0, True, I, 0), v2.ret(0, True, I, 1)
        self.assertTrue(v2.delay_equivalent(left, right))
        sep, ol, orr, kind = v2.separates(ops, left, right)
        self.assertTrue(sep)
        self.assertEqual(kind, "level_observation")
        self.assertEqual(ol, ("tower", True))
        self.assertEqual(orr, ("tower", False))

    def test_positive_control_G_a_density(self):
        ops = [{"kind": "between", "a": ZERO, "b": ONE}]
        left, right = v2.ret(0, True, I, 0), v2.ret(0, True, ONE, 0)
        self.assertTrue(v2.delay_equivalent(left, right))
        sep, ol, orr, kind = v2.separates(ops, left, right)
        self.assertTrue(sep)
        self.assertEqual(kind, "density_observation")
        self.assertEqual(ol, ("density", True))
        self.assertEqual(orr, ("density", False))

    def test_positive_control_kinds_are_the_new_three(self):
        self.assertEqual(
            {"availability_observation", "level_observation", "density_observation"},
            set(v2.SEPARATION_KINDS[3:]),
        )

    # ---- negative controls ----

    def test_negative_control_no_ops(self):
        left, right = v2.ret(0, True, I, 0), v2.ret(0, False, J, 2)
        sep, ol, orr, kind = v2.separates([], left, right)
        self.assertFalse(sep)
        self.assertIsNone(kind)

    def test_negative_control_identical_inputs_in_delay_context(self):
        ops = [{"kind": "race_left", "partner": PARTNER_JSON}, {"kind": "bind", "continuation": CONT_JSON}]
        value = v2.ret(1, False, J, 1)
        sep, ol, orr, kind = v2.separates(ops, value, value)
        self.assertFalse(sep)
        self.assertIsNone(kind)

    def test_negative_control_G_b_when_both_faces_supplied(self):
        ops = [{"kind": "supply", "face": I}, {"kind": "supply", "face": J}, {"kind": "fill"}]
        left, right = v2.ret(0, True, I, 0), v2.ret(0, True, J, 0)
        sep, ol, orr, kind = v2.separates(ops, left, right)
        self.assertFalse(sep)
        self.assertIsNone(kind)

    def test_negative_control_G_c_equal_levels(self):
        ops = [{"kind": "tower", "level": 1}]
        left, right = v2.ret(0, True, I, 1), v2.ret(0, True, J, 1)
        sep, ol, orr, kind = v2.separates(ops, left, right)
        self.assertFalse(sep)
        self.assertIsNone(kind)

    def test_negative_control_G_a_both_faces_at_bounds(self):
        ops = [{"kind": "between", "a": ZERO, "b": ONE}]
        left, right = v2.ret(0, True, ZERO, 0), v2.ret(0, True, ONE, 0)
        sep, ol, orr, kind = v2.separates(ops, left, right)
        self.assertFalse(sep)
        self.assertIsNone(kind)

    # ---- L1 shared kinds must remain reachable in the V2 fragment ----

    def test_l1_shared_value_mismatch_is_reachable(self):
        ops = [{"kind": "race_left", "partner": PARTNER_JSON}]
        left, right = v2.ret(0, True, I, 0), v2.ret(0, False, I, 0)
        sep, ol, orr, kind = v2.separates(ops, left, right)
        self.assertTrue(sep)
        self.assertEqual(kind, "value_mismatch")

    def test_l1_shared_completion_divergence_is_reachable(self):
        ops = [{"kind": "bind", "continuation": {
            "true": {"kind": "omega"},
            "false": {"kind": "ret", "n": 0, "value": False, "face": J, "level": 0},
        }}]
        left, right = v2.ret(0, True, I, 0), v2.ret(0, False, I, 0)
        sep, ol, orr, kind = v2.separates(ops, left, right)
        self.assertTrue(sep)
        self.assertEqual(kind, "completion_divergence")

    def test_l1_shared_deadline_observation_is_reachable(self):
        ops = [{"kind": "deadline", "k": 0}]
        left, right = v2.ret(0, True, I, 0), v2.ret(1, True, I, 0)
        sep, ol, orr, kind = v2.separates(ops, left, right)
        self.assertTrue(sep)
        self.assertEqual(kind, "deadline_observation")


class L1SynonymyTest(unittest.TestCase):
    """On the computation axis the shared ops must be the L1 ops (010 §3)."""

    def test_delay_equivalent_agrees_on_all_ground_pairs(self):
        for left in GROUND:
            pl = project_to_l1(left)
            for right in GROUND:
                pr = project_to_l1(right)
                self.assertEqual(
                    v2.delay_equivalent(left, right),
                    l1.delay_equivalent(pl, pr),
                )

    def test_race_value_agrees_on_the_computation_axis(self):
        partners = [v2.omega(), v2.ret(0, True, I, 0), v2.ret(2, False, J, 2), v2.ret(1, True, ONE, 1)]
        for value in GROUND:
            pv = project_to_l1(value)
            for partner in partners:
                pp = project_to_l1(partner)
                got = v2.race_value(value, partner)
                want = l1.race_value(pv, pp)
                self.assertEqual(project_to_l1(got), want)

    def test_bind_value_agrees_on_the_computation_axis(self):
        cont_l1 = {True: project_to_l1(CONT[True]), False: project_to_l1(CONT[False])}
        for value in GROUND:
            pv = project_to_l1(value)
            got = v2.bind_value(value, CONT)
            want = l1.bind_value(pv, cont_l1)
            self.assertEqual(project_to_l1(got), want)

    def test_conv_agrees(self):
        for value in GROUND:
            pv = project_to_l1(value)
            for b in v2.BOOLS:
                self.assertEqual(v2.conv(value, b), l1.conv(pv, b))


class JsonRoundTripTest(unittest.TestCase):
    def test_all_ground_values_round_trip(self):
        for value in GROUND:
            self.assertEqual(v2.value_from_json(v2.value_to_json(value)), value)

    def test_continuation_round_trip(self):
        self.assertEqual(v2.continuation_from_json(v2.continuation_to_json(CONT)), CONT)

    def test_unknown_json_kind_is_rejected(self):
        with self.assertRaisesRegex(MachineOverviewError, "UNKNOWN_VALUE_JSON"):
            v2.value_from_json({"kind": "bogus"})


if __name__ == "__main__":
    unittest.main()
