#!/usr/bin/env python3
"""Verify the local anchors of the bounded ABX community-awareness review."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REPORT = "audit/abx-action-20260921/ABX-圆环挑战的HoTT社区认识范围审计-20260921.md"
RECEIPT = "audit/abx-action-20260921/ABX-COMMUNITY-AWARENESS-VERIFICATION.json"
ABX_INDEX = "ABX行动.md"
ABX_STATE = "ABX行动/005 - 状态、停止条件与未来交接.md"
BOOK_INTRO = "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/introduction.tex"
BOOK_PRELIM = "sources/webgpt/workspace-snapshot/HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(text: str, needle: str, owner: str) -> None:
    if needle not in text:
        raise SystemExit(f"missing required anchor in {owner}: {needle!r}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    files = {
        REPORT: ROOT / REPORT,
        ABX_INDEX: ROOT / ABX_INDEX,
        ABX_STATE: ROOT / ABX_STATE,
        BOOK_INTRO: ROOT / BOOK_INTRO,
        BOOK_PRELIM: ROOT / BOOK_PRELIM,
    }
    for rel, path in files.items():
        if not path.is_file():
            raise SystemExit(f"missing required source: {rel}")

    report = files[REPORT].read_text(encoding="utf-8")
    for marker in (
        "SOURCE_REVIEWED_WITH_SCOPE",
        "NO_COMMUNITY_WIDE_KNOWLEDGE_CLAIM",
        "NO_CHANGE_TO_ABX_K_GATE",
        "NOT_ESTABLISHED",
        "NO_EXACT_ABX_FORMULATION_FOUND_WITHIN_DECLARED_SOURCES_AND_QUERIES",
        "https://groups.google.com/g/HomotopyTypeTheory/c/OxOXaZ46aPg/m/sno0YO-9BAAJ",
        "https://arxiv.org/abs/1509.07584",
        "https://arxiv.org/abs/1408.0054",
    ):
        require(report, marker, REPORT)
    require(files[BOOK_INTRO].read_text(encoding="utf-8"), "purely homotopically, not topologically", BOOK_INTRO)
    prelim = files[BOOK_PRELIM].read_text(encoding="utf-8")
    require(prelim, "punctured disc", BOOK_PRELIM)
    require(prelim, "hold both endpoints fixed", BOOK_PRELIM)
    require(files[ABX_INDEX].read_text(encoding="utf-8"), "社区认识范围审计", ABX_INDEX)
    require(files[ABX_STATE].read_text(encoding="utf-8"), "社区认识范围审计", ABX_STATE)

    receipt = {
        "schema_version": "abx-community-awareness-verification/v1",
        "status": "PASS_WITH_SCOPE",
        "scope": "Checks local report anchors and pinned Book excerpts only; it does not re-fetch the web, prove a community-wide fact, establish K, or prove a mathematical claim.",
        "files": {rel: digest(path) for rel, path in files.items()},
        "network_sources_recorded": [
            "https://homotopytypetheory.org/book/",
            "https://groups.google.com/g/HomotopyTypeTheory/c/OxOXaZ46aPg/m/sno0YO-9BAAJ",
            "https://mathoverflow.net/questions/169097/a-pointless-circle-in-hott",
            "https://arxiv.org/abs/1509.07584",
            "https://arxiv.org/abs/1408.0054",
        ],
        "verdict": "COMMUNITY_RELEVANT_BOUNDARIES_SOURCE_REVIEWED_NO_EXACT_ABX_CONTRACT_OR_K_FOUND",
    }
    if args.write:
        (ROOT / RECEIPT).write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
