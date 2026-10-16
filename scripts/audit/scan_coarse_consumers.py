#!/usr/bin/env python3
"""Scan pinned corpora for "coarse-domain consumers" (C11 checklist item 1).

C11's sharpened E6 criterion asks for an interface whose *published type* takes a
coarse abstraction (set quotient, propositional truncation, stage-erased class) as
its domain and which must still recover a suspended reality factor.  The type-level
half is closed by the eliminator obligation, so this scanner looks for the
remaining shape: declarations whose type mentions a coarse constructor *and* an
arrow, and reports whether the same declaration also carries an obligation token
(`is-set`, `is-prop`, `respects`, `reflects`, `congruence`, `coherent`, ...).

Hits without an obligation token are the ones a human must read; they are the only
possible "documented promise > type capability" candidates.  The scanner does not
decide semantics and creates no mathematical claim.

Corpora are pinned local trees only (no network):

- `cubical-v0.9` : Cubical Agda library (tag v0.9, tree hash recorded in the N1 audit)
- `agda-unimath` : literate Agda sources at the commit pinned by `MP-UNIMATH-NOSECTION-REPLAY-001`
- repo formal   : `HoTT/formal/**/*.agda` (this repository's own packages)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPORA = (
    ("cubical-v0.9", "/Volumes/D/HoTT-toolchain-cache/cubical-v0.9/cubical", "*.agda"),
    ("agda-unimath", "/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d/src", "*.lagda.md"),
    ("repo-formal", str(ROOT / "HoTT/formal"), "*.agda"),
)
# Operator-position coarse constructors only.  v1 also matched `Trunc`/`trunc-`, which
# made the queue saturate with the record name `Truncated-Type` and `trunc-map`
# (batch 1 of 20 hits was 20/20 false positives); the rule is now operator-based.
COARSE_TOKENS = ("set-quotient", "Set-Quotient", "type-trunc", "is-inhabited-Prop", "mere-", "∥", "/R")
OBLIGATION_TOKENS = (
    "is-set", "is-prop", "is-contr", "is-equiv", "respects", "reflects", "reflecting",
    "congruence", "coherent", "well-defined", "is-effective", "reflecting-map",
    "isGroupoid", "is2Groupoid", "is-trunc", "is-n-type", "is-1-type", "is-2-type",
    "is-3-type", "is-0-connected", "is-n-connected", "is-inhabited", "is-surjective",
    "is-embedding", "is-torsorial", "mere-equiv", "is-slice", "is-relation",
    "isProp", "isSet", "isGroupoid", "isContr", "isEquiv", "isEmbedding",
    "isSurjective", "isTrunc", "isOfHLevel",
)
PROPISH_CODOMAIN = ("Prop", "is-prop", "is-contr", "is-equiv", "Id ", "＝", "≃", "is-set", "Subtype", "subtype")
SIGNATURE = re.compile(r"^([A-Za-z][A-Za-z0-9'\-_]*)\s*:\s*(.*)$")
CONTINUATION = re.compile(r"^\s+\S")
MAX_HITS_PER_CORPUS = 400


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tree_hash(root: Path, pattern: str) -> str:
    h = hashlib.sha256()
    files = sorted(root.rglob(pattern))
    for path in files:
        if "/_build/" in path.as_posix():
            continue
        h.update(path.relative_to(root).as_posix().encode())
        h.update(path.read_bytes())
    return h.hexdigest(), len(files)


def signatures(lines: list[str]) -> list[tuple[str, int, str]]:
    """Yield (name, line_no, signature_text) for top-level declarations.

    A declaration is a line at column 0 of the form `name : ...` (possibly with the
    type continued on indented lines).  Multi-line types end at the first blank line
    or the first line that starts at column 0.
    """
    out: list[tuple[str, int, str]] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = SIGNATURE.match(line)
        if m and not line[0].isspace():
            block = [line]
            j = i + 1
            while j < len(lines) and lines[j].strip() and lines[j][0].isspace():
                block.append(lines[j])
                j += 1
            out.append((m.group(1), i + 1, "\n".join(block)))
            i = j
            continue
        i += 1
    return out


def coarse_in_domain(sig: str) -> bool:
    """True when a coarse constructor appears before the first top-level arrow."""
    head, _, _ = sig.partition("→")
    return any(tok in head for tok in COARSE_TOKENS)


def returns_data(sig: str) -> bool:
    if "→" not in sig:
        return False
    tail = sig.rsplit("→", 1)[-1]
    return not any(tok in tail for tok in PROPISH_CODOMAIN)


def scan_file(path: Path) -> list[dict]:
    hits: list[dict] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (UnicodeDecodeError, OSError):
        return hits
    for name, line_no, sig in signatures(lines):
        if not coarse_in_domain(sig):
            continue
        if not returns_data(sig):
            continue
        hits.append(
            {
                "declaration": name,
                "line": line_no,
                "signature": " ".join(sig.split())[:220],
                "has_obligation_token": any(tok in sig for tok in OBLIGATION_TOKENS),
            }
        )
    return hits


def build_report() -> dict:
    corpora = []
    for name, root_str, pattern in DEFAULT_CORPORA:
        root = Path(root_str)
        entry: dict = {"name": name, "root": root_str, "pattern": pattern}
        if not root.is_dir():
            entry["status"] = "CORPUS_MISSING"
            corpora.append(entry)
            continue
        digest, file_count = tree_hash(root, pattern)
        hits: list[dict] = []
        for path in sorted(root.rglob(pattern)):
            if "/_build/" in path.as_posix():
                continue
            for hit in scan_file(path):
                hit["file"] = path.relative_to(root).as_posix()
                hits.append(hit)
                if len(hits) >= MAX_HITS_PER_CORPUS:
                    break
            if len(hits) >= MAX_HITS_PER_CORPUS:
                break
        no_obligation = [h for h in hits if not h["has_obligation_token"]]
        entry.update(
            {
                "status": "SCANNED",
                "files": file_count,
                "tree_sha256": digest,
                "hits": len(hits),
                "hits_with_obligation_token": len(hits) - len(no_obligation),
                "hits_without_obligation_token": len(no_obligation),
                "capped": len(hits) >= MAX_HITS_PER_CORPUS,
                "triage_queue": no_obligation,
            }
        )
        corpora.append(entry)
    return {
        "schema_version": "coarse-consumer-scan/v1",
        "coarse_tokens": list(COARSE_TOKENS),
        "obligation_tokens": list(OBLIGATION_TOKENS),
        "rule": (
            "A hit is a line mentioning a coarse constructor inside a top-level declaration whose type also "
            "contains an arrow. `has_obligation_token` is lexical only: it records whether the same declaration "
            "mentions a set/prop/equivalence/respect/reflect/congruence token. Hits without such a token require "
            "manual reading; they are the only possible coarse-domain consumers."
        ),
        "semantic_limit": (
            "Lexical scan: it cannot prove that a declaration is a quotient/truncation consumer, nor that its "
            "documentation promises more than its type. It creates no mathematical claim and upgrades nothing."
        ),
        "corpora": corpora,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = build_report()
    if args.output:
        target = ROOT / args.output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = [
        {
            "corpus": c["name"],
            "status": c["status"],
            "files": c.get("files"),
            "hits": c.get("hits"),
            "with_obligation": c.get("hits_with_obligation_token"),
            "without_obligation": c.get("hits_without_obligation_token"),
        }
        for c in report["corpora"]
    ]
    print(json.dumps({"schema_version": report["schema_version"], "corpora": summary}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
