#!/usr/bin/env python3
"""Evaluate eight frozen ground instances of QTT Var/App resource bookkeeping.

This is a source-reading aid, not a QTT kernel or a proof of substitution.
No dependent types, equality, lambda, tensor, universes, or completeness claim.
"""
import argparse
import hashlib
import json
from pathlib import Path

A = "A"
BOOL = "Bool"
ENV = {"x": A, "f": (2, A, A), "g": (1, A, A), "z": (0, A, A)}


def infer(term, mode):
    if mode not in (0, 1):
        raise ValueError("RESULT_MODE_NOT_0_OR_1")
    if term[0] == "var":
        name = term[1]
        return ENV[name], {n: mode if n == name else 0 for n in ENV}
    if term[0] == "true":
        return BOOL, {n: 0 for n in ENV}
    if term[0] == "app":
        ft, fr = infer(term[1], mode)
        if not isinstance(ft, tuple):
            raise ValueError("FUNCTION_TYPE_REQUIRED")
        pi, dom, cod = ft
        argument_mode = 0 if pi == 0 or mode == 0 else 1
        if len(term) == 4 and term[3] != argument_mode:
            raise ValueError("APP_RESULT_ARGUMENT_MODE_SIDE_CONDITION")
        at, ar = infer(term[2], argument_mode)
        if at != dom:
            raise ValueError("ARGUMENT_TYPE_MISMATCH")
        return cod, {n: fr[n] + pi * ar[n] for n in ENV}
    raise ValueError("OUTSIDE_GROUND_READER_GRAMMAR")


X = ("var", "x")
F = ("var", "f")
G = ("var", "g")
Z = ("var", "z")
# Exact expected observations are frozen before execution, with rule locators in
# RULE-REVIEW.md. Equal erased variable/type lists are fixed by the single ENV.
CASES = [
    ("Q01-scaled-argument", ("app", F, X), 1, {"f": 1, "x": 2}, True),
    ("Q02-understated-argument", ("app", F, X), 1, {"f": 1, "x": 1}, False),
    ("Q03-shared-function", ("app", G, ("app", G, X)), 1, {"g": 2, "x": 1}, True),
    ("Q04-understated-shared-function", ("app", G, ("app", G, X)), 1, {"g": 1, "x": 1}, False),
    ("Q05-erased-argument", ("app", Z, X), 1, {"z": 1}, True),
    ("Q06-erased-to-present-attempt", ("app", F, X, 0), 1, "APP_RESULT_ARGUMENT_MODE_SIDE_CONDITION", True),
    ("Q07-arbitrary-result-mode-attempt", G, 2, "RESULT_MODE_NOT_0_OR_1", True),
    ("Q08-closed-present-constant", ("true",), 1, {}, True),
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    rows = []
    for cid, term, mode, expected, expectation in CASES:
        try:
            ty, usage = infer(term, mode)
            observed = {k: v for k, v in usage.items() if v != 0}
        except ValueError as exc:
            ty, observed = None, str(exc)
        matches = observed == expected
        rows.append({"id": cid, "term": term, "mode": mode, "observed_type": ty,
                     "observed_usage_or_rejection": observed, "proposed_usage_or_rejection": expected,
                     "proposal_matches_observation": matches, "expected_match": expectation,
                     "expectation_met": matches == expectation})
    result = {"scope": __doc__, "source_pdf_sha256": "1af7f05a0952f5969e5a7420d442632f110ee7e2f06f558d13ca7dd7f66e71d0",
              "source_pages": [3, 4, 5], "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "cases": rows, "case_count": len(rows), "all_expected": all(x["expectation_met"] for x in rows),
              "native_proof": False, "exhaustive_grammar_coverage": False}
    with Path(args.out).open("x") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["all_expected"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
