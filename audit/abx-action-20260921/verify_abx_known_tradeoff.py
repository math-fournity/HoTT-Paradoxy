#!/usr/bin/env python3
"""Verify the source distinctions needed for the ABX known-tradeoff audit.

This check is deliberately about source identity and exact textual/formal
scope. It does not decide whether a user philosophical predicate such as
"non-real" applies to a mathematical construction.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc"
OUT = ROOT / "audit/abx-action-20260921/ABX-KNOWN-TRADEOFF-VERIFICATION.json"
EXPECTED = {
    "reals.tex": "f5e4803e17abdb2fbb75a6ebd30022a9587a914711f3ca77dc8fcce50fda39e7",
    "logic.tex": "76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2",
    "introduction.tex": "a1319432c822d71ee54cd8edd644d3bce1c8d816bd9f2ff6111b8d3db8e28ac4",
}
ANCHORS = {
    "reals.tex": (
        "burden us with bureaucracy that we prefer to avoid",
        "We could identify $\\Omega$ with the ambiguous $\\prop$ and track all the universes",
        "We could assume the propositional resizing axiom",
        "law of excluded middle",
        "initial \\emph{$\\sigma$-frame}",
    ),
    "logic.tex": (
        "It is not the case that for all $A:\\UU$ we have $A+(\\neg A)$",
        "This formulation of \\LEM{} avoids the ``paradoxes''",
        "it may be consistently assumed as an axiom (unlike its $\\infty$-counterpart)",
        "We will not assume this axiom in general",
    ),
    "introduction.tex": (
        "treated purely homotopically, not topologically",
        "no notion of ``open subset''",
    ),
}
LOCAL = {
    "HoTT/formal/dedekind-omega-missile/CLAIM-PACKAGE-REAL-LAYER.md": (
        "Sufficiency", "Necessity", "CONJECTURE",
    ),
    "Astra继续尝试/ZCode-7cb会话成果吸收审查/003 - 语料检索、文献解释与证据治理.md": (
        "充分性/必要性继续分开", "任何只走UA/等价的位置自动丢R信息",
    ),
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def lines(text: str, needle: str) -> list[int]:
    return [n for n, line in enumerate(text.splitlines(), 1) if needle in line]


def main() -> None:
    book = {}
    for name, expected in EXPECTED.items():
        path = BOOK / name
        if not path.is_file() or sha(path) != expected:
            raise SystemExit(f"Book source identity mismatch: {name}")
        text = path.read_text()
        missing = [anchor for anchor in ANCHORS[name] if anchor not in text]
        if missing:
            raise SystemExit(f"Book source anchor missing: {name}: {missing}")
        book[name] = {"sha256": expected, "anchors": {a: lines(text, a) for a in ANCHORS[name]}}

    local = {}
    for rel, required in LOCAL.items():
        path = ROOT / rel
        text = path.read_text()
        missing = [anchor for anchor in required if anchor not in text]
        if missing:
            raise SystemExit(f"local source anchor missing: {rel}: {missing}")
        local[rel] = {"sha256": sha(path), "anchors": {a: lines(text, a) for a in required}}

    result = {
        "schema_version": "abx-known-tradeoff-verification/v1",
        "status": "PASS_WITH_SCOPE",
        "book_commit": "578b85cc8d586b1677ec4335148adeb443057d24",
        "book_sources": book,
        "local_scope_sources": local,
        "verified_distinctions": [
            "Book §11.2 presents universe tracking, propositional resizing, LEM for mere propositions, and an initial sigma-frame as distinct ways to handle a single Ω presentation; it does not label any one a non-real defect.",
            "The Book rejects the all-types principle LEM∞ under univalence, while separately defining a mere-proposition LEM that it says may consistently be assumed.",
            "The current local B1a package proves a sufficiency implication from SingleOmega to its declared real-layer proxy; its converse Necessity remains a conjecture and must not be read as a proof of compulsory payment.",
            "The prior ZCode review already rejects GLM's jump from a source/keyword observation or B1a sufficiency to an automatic loss-of-R claim.",
        ],
        "not_decided": [
            "whether a user philosophical predicate such as non-real applies to any option",
            "whether any specific external application uses an undisclosed premise",
            "whether the abstract-theory-to-nonreal-paradox thesis is true",
            "whether any HoTT theory is inconsistent or defective",
        ],
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": result["status"], "book_files": len(book), "local_files": len(local)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
