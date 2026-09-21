#!/usr/bin/env python3
"""Audit the fixed HoTT Book source for an ABX bridge in its core rules.

The audit does not ask whether a future application could misuse an
equivalence.  It asks the narrower question whether the pinned textbook's
basic homotopy/univalence presentation itself states a point-set
homeomorphism or a path/equivalence-to-strong-restoration contract.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BOOK = ROOT / "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc"
OUT = ROOT / "audit/abx-action-20260921/ABX-3-D3-BOOK-CORE.json"
EXPECTED = {
    "introduction.tex": "a1319432c822d71ee54cd8edd644d3bce1c8d816bd9f2ff6111b8d3db8e28ac4",
    "basics.tex": "516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533",
    "equivalences.tex": "037dce18db74526a3f7148c353bb5459da1c4b65e046780a208de39633df1722",
}
REQUIRED = {
    "introduction.tex": ("purely homotopically, not topologically", "open subset", "convergence"),
    "basics.tex": ("idtoeqv", "Univalence", "equivalent types may be identified", "transport"),
    "equivalences.tex": ("Quasi-inverses", "On the definition of equivalences", "\\isequiv"),
}
ABX_TERMS = ("homeomorph", "RichCurve", "Done_strong", "PuncturedRealCircle", "OpenRealInterval", "R_origin")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def line_numbers(text: str, needle: str) -> list[int]:
    return [n for n, line in enumerate(text.splitlines(), 1) if needle.lower() in line.lower()]


def main() -> None:
    entries = {}
    for name, expected in EXPECTED.items():
        path = BOOK / name
        if not path.is_file() or sha(path) != expected:
            raise SystemExit(f"pinned Book identity mismatch: {name}")
        text = path.read_text()
        missing = [anchor for anchor in REQUIRED[name] if anchor not in text]
        if missing:
            raise SystemExit(f"Book anchor missing in {name}: {missing}")
        entries[name] = {
            "sha256": expected,
            "anchors": {anchor: line_numbers(text, anchor) for anchor in REQUIRED[name]},
            "abx_term_lines": {term: line_numbers(text, term) for term in ABX_TERMS},
        }

    tex_files = sorted(BOOK.glob("*.tex"))
    if len(tex_files) != 18:
        raise SystemExit(f"unexpected Book tex denominator: {len(tex_files)}")
    homeomorph_files = []
    for path in tex_files:
        lines = line_numbers(path.read_text(), "homeomorph")
        if lines:
            homeomorph_files.append({"path": path.name, "lines": lines})
    result = {
        "schema_version": "abx-d3-book-core/v1",
        "status": "PASS_WITH_SCOPE",
        "source": {
            "book_commit": "578b85cc8d586b1677ec4335148adeb443057d24",
            "root": str(BOOK),
            "selected_core_files": entries,
            "all_tex_file_count": len(tex_files),
            "homeomorph_lexical_matches": homeomorph_files,
        },
        "verdict": "NO_H_TOP_OR_U_TO_DONE_STRONG_BRIDGE_WITHIN_BOOK_D_ABX_3",
        "supported_reading": [
            "The pinned introduction distinguishes a homotopical interpretation of types from point-set topology and explicitly says open subsets and sequence convergence are not notions of a type.",
            "The pinned univalence presentation identifies universe paths with type equivalences and describes transport in a type family; it does not specify an erasure map from a structured record to its carrier.",
            "The pinned equivalence chapter defines type-theoretic equivalence through maps, homotopies and inverse/fiber data, not a point-set homeomorphism or a physical restoration task.",
            "No `homeomorph` lexical occurrence appears in the declared 18-file Book tex denominator.",
        ],
        "not_proved": [
            "that no paper, library, or user can define a problematic consumer K",
            "that the Book validates or refutes the user's R_origin relation",
            "any HoTT inconsistency, defect, or global safety theorem",
        ],
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "status": result["status"],
        "tex_files": len(tex_files),
        "homeomorph_matches": len(homeomorph_files),
        "verdict": result["verdict"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
