#!/usr/bin/env python3
"""Finite sanity check for the two-event Z/Padoa obstruction.

This is not a proof of Beth's theorem or a proof-assistant verification.
It only enumerates the two strict total orders on a two-element domain,
checks that they share the same atemporal equality reduct, and checks
that the swap automorphism reverses each order.
"""
from __future__ import annotations

import json
from itertools import permutations
from pathlib import Path

U = (0, 1)
SWAP = {0: 1, 1: 0}


def order_from_permutation(p: tuple[int, ...]) -> frozenset[tuple[int, int]]:
    pos = {x: i for i, x in enumerate(p)}
    return frozenset((x, y) for x in U for y in U if pos[x] < pos[y])


def transport_relation(
    rel: frozenset[tuple[int, int]], perm: dict[int, int]
) -> frozenset[tuple[int, int]]:
    return frozenset((perm[x], perm[y]) for x, y in rel)


def main() -> None:
    orders = [order_from_permutation(p) for p in permutations(U)]
    unique_orders = sorted(set(orders), key=lambda r: sorted(r))
    assert len(unique_orders) == 2

    plus, minus = unique_orders
    same_equality_reduct = True  # both structures have domain U and equality only
    distinct_temporal_expansions = plus != minus
    swapped_plus = transport_relation(plus, SWAP)
    swapped_minus = transport_relation(minus, SWAP)
    swap_exchanges_orders = swapped_plus == minus and swapped_minus == plus
    invariant_orders = [r for r in unique_orders if transport_relation(r, SWAP) == r]

    record = {
        "domain": list(U),
        "atemporal_reduct": "pure equality on {0,1}",
        "strict_total_orders": [sorted(map(list, r)) for r in unique_orders],
        "same_atemporal_reduct": same_equality_reduct,
        "distinct_temporal_expansions": distinct_temporal_expansions,
        "swap_exchanges_orders": swap_exchanges_orders,
        "swap_invariant_strict_total_order_count": len(invariant_orders),
        "padoa_witness_holds": (
            same_equality_reduct
            and distinct_temporal_expansions
            and swap_exchanges_orders
            and not invariant_orders
        ),
        "scope": (
            "finite two-event sanity check only; not a proof of Beth definability "
            "and not a proof-assistant verification of HoTT"
        ),
    }

    out = Path('/mnt/data/verification/temporal_reduct_definability.json')
    out.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding='utf-8')
    print(out)
    print(json.dumps(record, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
