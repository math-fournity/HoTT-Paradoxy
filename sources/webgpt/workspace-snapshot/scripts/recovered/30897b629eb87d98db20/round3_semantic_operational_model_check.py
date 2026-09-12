#!/usr/bin/env python3
"""Finite sanity checks for round-3 semantic-role, operational-cost, and fixed-point examples.

These checks validate only the displayed finite countermodels. They are not an
unbounded proof, a proof-assistant compilation, or a verification of the Rice-style theorem.
"""
from itertools import product
import json
from pathlib import Path

out = {}

# 1. One bare object, two forgotten roles. No recovery q: Bare -> Role can recover both.
bare = [0]
roles = ["Arith", "Index"]
enriched = [(0, r) for r in roles]
recoveries = [{0: r} for r in roles]
valid_role_recoveries = [
    q for q in recoveries
    if all(q[b] == r for b, r in enriched)
]
out["semantic_role_non_descent"] = {
    "bare_states": bare,
    "enriched_states": enriched,
    "candidate_recoveries": len(recoveries),
    "valid_exact_recoveries": len(valid_role_recoveries),
    "passed": len(valid_role_recoveries) == 0,
}

# 2. Two programs, same extensional denotation, different costs.
programs = {
    "fast_id": {"denotation": (0, 1), "cost": 1},
    "slow_id": {"denotation": (0, 1), "cost": 3},
}
denotations = sorted(set(v["denotation"] for v in programs.values()))
# A cost function on denotations chooses one natural number for the single denotation.
candidate_costs = [{denotations[0]: c} for c in range(5)]
valid_cost_recoveries = [
    q for q in candidate_costs
    if all(q[p["denotation"]] == p["cost"] for p in programs.values())
]
out["operational_cost_non_descent"] = {
    "programs": programs,
    "distinct_denotations": len(denotations),
    "candidate_cost_maps_checked": len(candidate_costs),
    "valid_exact_cost_maps": len(valid_cost_recoveries),
    "passed": len(valid_cost_recoveries) == 0,
}

# 3. Bool negation has no fixed point but has arbitrarily long finite prefixes of a trajectory.
def neg(b: bool) -> bool:
    return not b
fixed_points = [b for b in [False, True] if b == neg(b)]
trajectory = [False]
for _ in range(15):
    trajectory.append(neg(trajectory[-1]))
trajectory_ok = all(trajectory[n+1] == neg(trajectory[n]) for n in range(len(trajectory)-1))
out["static_fixed_point_vs_dynamic_trajectory"] = {
    "fixed_points": fixed_points,
    "trajectory_prefix": trajectory,
    "trajectory_equations_hold": trajectory_ok,
    "passed": len(fixed_points) == 0 and trajectory_ok,
}

# 4. Exact left inverse to the role-forgetting map cannot exist.
# Enumerate maps r: Bare -> Enriched and test r(pi(e)) = e for every e.
candidate_sections = [{0: e} for e in enriched]
exact_left_inverses = [
    r for r in candidate_sections
    if all(r[b] == (b, role) for b, role in enriched)
]
out["no_exact_reconstruction_left_inverse"] = {
    "candidate_maps": len(candidate_sections),
    "exact_left_inverses": len(exact_left_inverses),
    "passed": len(exact_left_inverses) == 0,
}

out["scope_warning"] = (
    "Finite enumeration only. It does not prove the general dependent-type/SIP theorem, "
    "the unbounded program-equivalence theorem, or any inconsistency of HoTT."
)
out["all_finite_checks_passed"] = all(
    v.get("passed", True) if isinstance(v, dict) else True for v in out.values()
)

path = Path('/mnt/data/verification/round3_semantic_operational_model_check.json')
path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out, ensure_ascii=False, indent=2))
