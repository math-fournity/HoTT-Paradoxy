#!/usr/bin/env python3
"""Exhaustively verify the finite base lemma used in the HoTT time-orientation no-go theorem.

This is an exact finite check on the two-element set {0,1}; it is not presented as a
formalization of univalence itself. It verifies that the two strict total orders are
exchanged by swap and that no strict total order is swap-invariant.
"""
from __future__ import annotations

from itertools import product
from typing import FrozenSet, Iterable, Tuple

Pair = Tuple[int, int]
REL_PAIRS: tuple[Pair, ...] = ((0, 0), (0, 1), (1, 0), (1, 1))


def swap(x: int) -> int:
    if x not in (0, 1):
        raise ValueError(f"Expected 0 or 1, got {x}")
    return 1 - x


def relation(bits: Iterable[int]) -> FrozenSet[Pair]:
    return frozenset(p for p, bit in zip(REL_PAIRS, bits, strict=True) if bit)


def is_strict_total_order(r: FrozenSet[Pair]) -> bool:
    # Irreflexive.
    if (0, 0) in r or (1, 1) in r:
        return False
    # Exactly one direction for the distinct pair.
    if ((0, 1) in r) == ((1, 0) in r):
        return False
    # Transitive (included for completeness).
    for x in (0, 1):
        for y in (0, 1):
            for z in (0, 1):
                if (x, y) in r and (y, z) in r and (x, z) not in r:
                    return False
    return True


def pushforward_by_swap(r: FrozenSet[Pair]) -> FrozenSet[Pair]:
    return frozenset((swap(x), swap(y)) for x, y in r)


def main() -> None:
    strict_orders: list[FrozenSet[Pair]] = []
    for bits in product((0, 1), repeat=len(REL_PAIRS)):
        r = relation(bits)
        if is_strict_total_order(r):
            strict_orders.append(r)

    invariant = [r for r in strict_orders if pushforward_by_swap(r) == r]

    print(f"All binary relations checked: {2 ** len(REL_PAIRS)}")
    print(f"Strict total orders found: {len(strict_orders)}")
    for idx, r in enumerate(strict_orders, start=1):
        print(f"  order {idx}: {sorted(r)} -> swapped: {sorted(pushforward_by_swap(r))}")
    print(f"Swap-invariant strict total orders: {len(invariant)}")

    assert len(strict_orders) == 2
    assert len(invariant) == 0
    assert all(swap(x) != x for x in (0, 1))
    print("VERIFIED: swap has no fixed point and fixes no strict total order on {0,1}.")


if __name__ == "__main__":
    main()
