#!/usr/bin/env python3
"""Finite sanity check for the temporal-order automorphism obstruction.

This script is NOT the general proof. It exhaustively checks small finite sets:
no strict total order is invariant under a non-identity permutation, and hence
no order is invariant under all automorphisms when n >= 2.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Iterable, Tuple

Order = Tuple[int, ...]
Permutation = Tuple[int, ...]


def relabel_order(order: Order, permutation: Permutation) -> Order:
    """Push an enumeration/order forward along a permutation."""
    return tuple(permutation[x] for x in order)


def permutations(n: int) -> Iterable[Permutation]:
    return itertools.permutations(range(n))


def check_n(n: int) -> dict[str, int | bool]:
    orders = list(itertools.permutations(range(n)))
    autos = list(permutations(n))
    identity = tuple(range(n))
    nontrivial_autos = [p for p in autos if p != identity]

    fixed_by_all = [
        order
        for order in orders
        if all(relabel_order(order, p) == order for p in autos)
    ]

    first_nontrivial = nontrivial_autos[0] if nontrivial_autos else identity
    fixed_by_first_nontrivial = [
        order for order in orders if relabel_order(order, first_nontrivial) == order
    ]

    return {
        "n": n,
        "strict_total_order_count": len(orders),
        "expected_factorial": math.factorial(n),
        "automorphism_count": len(autos),
        "orders_fixed_by_all_automorphisms": len(fixed_by_all),
        "orders_fixed_by_first_nonidentity_automorphism": len(fixed_by_first_nontrivial),
        "obstruction_holds": (n < 2) or len(fixed_by_all) == 0,
    }


def main() -> None:
    records = [check_n(n) for n in range(0, 9)]
    payload = {
        "scope": "finite_sanity_check_only",
        "theorem_not_claimed_from_search": True,
        "statement": (
            "For each tested n >= 2, no strict total order on an n-element "
            "set is invariant under all automorphisms."
        ),
        "records": records,
    }

    out = Path("/mnt/data/verification/temporal_order_obstruction_finite.json")
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(out)
    for record in records:
        print(record)


if __name__ == "__main__":
    main()
