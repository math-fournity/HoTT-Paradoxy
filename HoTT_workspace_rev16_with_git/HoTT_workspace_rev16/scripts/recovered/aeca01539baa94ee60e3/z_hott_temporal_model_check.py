#!/usr/bin/env python3
"""Finite sanity checks for the Z–HoTT temporal no-go arguments.

This script does NOT formalize HoTT. It checks the finite countermodels used in
Sections 2, 5, and 6 of HOTT_Z_内生时间不完备性_论文草案_v1.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable, Dict, FrozenSet, Iterable, Tuple

Bool = bool
History = str


def check_factorization_obstruction() -> None:
    """No Boolean function on a one-point abstraction fits opposite truths."""
    histories: Tuple[History, ...] = ("a_before_b", "b_before_a")
    abstraction: Dict[History, str] = {h: "unordered_{a,b}" for h in histories}
    truth: Dict[History, Bool] = {
        "a_before_b": True,
        "b_before_a": False,
    }

    abstract_states = sorted(set(abstraction.values()))
    candidates = []
    for values in product((False, True), repeat=len(abstract_states)):
        predictor = dict(zip(abstract_states, values))
        correct = all(predictor[abstraction[h]] == truth[h] for h in histories)
        candidates.append((predictor, correct))

    assert not any(correct for _, correct in candidates)
    print("[PASS] Z factorization obstruction: 0/2 abstract predictors fit both histories.")


@dataclass(frozen=True)
class TinyCategory:
    """A two-object category represented only by its nonidentity generating arrows."""

    name: str
    arrows: FrozenSet[Tuple[int, int]]

    @property
    def core(self) -> FrozenSet[Tuple[int, int]]:
        # In these examples the only invertible arrows are identities.
        return frozenset({(0, 0), (1, 1)})

    def forward_only(self) -> Bool:
        return (0, 1) in self.arrows and (1, 0) not in self.arrows


def check_groupoid_core_obstruction() -> None:
    c_plus = TinyCategory("C_plus", frozenset({(0, 1)}))
    c_minus = TinyCategory("C_minus", frozenset({(1, 0)}))

    assert c_plus.core == c_minus.core
    assert c_plus.forward_only() is True
    assert c_minus.forward_only() is False
    print("[PASS] Core obstruction: equal cores, opposite irreversible-direction truth values.")


def swap(x: int) -> int:
    if x not in (0, 1):
        raise ValueError("swap is defined only on the two-element set {0,1}")
    return 1 - x


def compose(f: Tuple[int, int], g: Callable[[int], int]) -> Tuple[int, int]:
    """Return f ∘ g for f represented by its values on 0 and 1."""
    return (f[g(0)], f[g(1)])


def check_univalent_orientation_obstruction() -> None:
    # The two equivalences 2 ≃ 2, represented as ordered images of 0 and 1.
    orientations: Tuple[Tuple[int, int], ...] = ((0, 1), (1, 0))
    fixed = [f for f in orientations if compose(f, swap) == f]

    assert fixed == []
    print("[PASS] Swap monodromy: neither of the two temporal labelings is fixed.")


def main() -> None:
    check_factorization_obstruction()
    check_groupoid_core_obstruction()
    check_univalent_orientation_obstruction()
    print("All finite sanity checks passed.")
    print("Scope: finite countermodel validation only; not a proof-assistant verification of HoTT.")


if __name__ == "__main__":
    main()
