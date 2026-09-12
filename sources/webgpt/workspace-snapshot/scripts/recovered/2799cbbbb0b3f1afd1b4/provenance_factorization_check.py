#!/usr/bin/env python3
"""Finite sanity checks for the history/provenance Z-factorization theorem.

This script is not an unbounded formal proof. It exhaustively checks the smallest
finite model used in the paper:
  History = Snapshot × {original, replica}
and confirms that IsOriginal does not factor through the snapshot projection,
while it does factor through the enriched identity representation.
"""
from __future__ import annotations

from itertools import product
from typing import Dict, Hashable, Iterable, Tuple

History = Tuple[str, str]


def all_boolean_functions(domain: Iterable[Hashable]):
    domain = tuple(domain)
    for values in product((False, True), repeat=len(domain)):
        yield dict(zip(domain, values))


def main() -> None:
    snapshots = ("same-current-structure",)
    provenances = ("original", "replica")
    histories: Tuple[History, ...] = tuple(product(snapshots, provenances))

    coarse = {h: h[0] for h in histories}
    fine = {h: h for h in histories}
    is_original = {h: h[1] == "original" for h in histories}

    coarse_factorizations = []
    for predictor in all_boolean_functions(snapshots):
        if all(predictor[coarse[h]] == is_original[h] for h in histories):
            coarse_factorizations.append(predictor)

    # The enriched representation has the obvious predictor.
    fine_predictor: Dict[History, bool] = {h: is_original[h] for h in histories}
    fine_factors = all(fine_predictor[fine[h]] == is_original[h] for h in histories)

    # Exhaustively test whether the non-injective coarse map has a left inverse.
    # A candidate beta maps the single snapshot back to one of the two histories.
    left_inverses = []
    for chosen in histories:
        beta = {snapshots[0]: chosen}
        if all(beta[coarse[h]] == h for h in histories):
            left_inverses.append(beta)

    print("Finite provenance factorization sanity check")
    print("Histories:", histories)
    print("Coarse fibers:", {s: [h for h in histories if coarse[h] == s] for s in snapshots})
    print("IsOriginal values:", is_original)
    print("Coarse factorization count:", len(coarse_factorizations))
    print("Fine representation factors:", fine_factors)
    print("Exact left inverse count for coarse abstraction:", len(left_inverses))

    assert len(coarse_factorizations) == 0
    assert fine_factors
    assert len(left_inverses) == 0
    print("PASS: provenance is not recoverable from the coarse snapshot, but is recoverable after enrichment.")


if __name__ == "__main__":
    main()
