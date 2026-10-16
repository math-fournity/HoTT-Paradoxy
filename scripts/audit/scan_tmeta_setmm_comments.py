#!/usr/bin/env python3
"""Reproduce T-Meta-001's bounded semantic comment scan of pinned set.mm."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


EXPECTED_SHA256 = "d8420798bcedcd04fcfe337736e2609b66914c76f8f2db967fa79673d5026b2a"
DEFAULT = Path("/Volumes/D/HoTT-downloads/godel-q-setmm-160ebb/set.mm")
TERMS = ("zeno", "hott", "questioning", "delay", "origindone", "completion", "motion")


def comments(text: str) -> list[str]:
    output: list[str] = []
    start = 0
    while True:
        left = text.find("$(", start)
        if left < 0:
            return output
        right = text.find("$)", left + 2)
        if right < 0:
            raise ValueError("UNTERMINATED_METAMATH_COMMENT")
        output.append(text[left + 2:right])
        start = right + 2


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = args.input.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"SETMM_SHA256_MISMATCH:{digest}")
    source_comments = comments(data.decode("utf-8", errors="replace"))
    result = {
        "schema_version": "tmeta-setmm-comment-scan/v1",
        "input": str(args.input),
        "sha256": digest,
        "comment_count": len(source_comments),
        "terms": {
            term: [
                index + 1
                for index, comment in enumerate(source_comments)
                if re.search(
                    r"\b" + re.escape(term) + (r"s?\b" if term == "motion" else r"\b"),
                    comment,
                    flags=re.IGNORECASE,
                )
            ]
            for term in TERMS
        },
        "scope": "Lexical comment inventory only. It neither proves semantic absence nor supplies a bridge between set.mm proof acceptance and an external completion task.",
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
