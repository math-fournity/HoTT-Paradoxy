#!/usr/bin/env python3
"""Create or verify a conservative title-signal triage for LIT-DENOMINATOR-001.

The output never excludes a candidate from the denominator.  It only separates
direct title signals, adjacent title signals, and the title-insufficient
UNCLASSIFIED remainder for later primary-source review.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path
from typing import Any


SCHEMA = "hott-literature-title-triage/v1"

HOTT_TERMS = (
    "homotopy type theory", "univalent type theory", "univalent foundations",
    "cubical type theory", "cubical agda", "two-level type theory", "2ltt",
)
TYPE_THEORY_TERMS = HOTT_TERMS + (
    "dependent type theory", "type theory", "calculus of inductive constructions",
)
COMPUTATION_TERMS = (
    "computab", "undecid", "incomplet", "gödel", "goedel", "turing", "halting",
    "partial", "recursion", "termination", "normalization", "normalisation",
    "canonicity", "decidab", "proof search", "reflection", "syntax", "cofibration",
    "oracle", "church thesis", "löb", "lob", "productiv", "guarded", "clocked",
    "type checking", "type-checking", "provability", "diagonal",
)
DIRECT_PHRASES = (
    "synthetic computability", "synthetic undecidability", "synthetic incompleteness",
    "gödel's incompleteness", "goedel's incompleteness", "gödel’s incompleteness",
    "essential incompleteness", "machine-assisted proof of gödel", "formalisation of godel",
    "formalization of godel", "formalizing mathematical logic", "type theory in type theory",
)

SEEDS = [
    ("SEED-GODEL-1931", "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I", "paper"),
    ("SEED-TURING-1936", "On Computable Numbers, with an Application to the Entscheidungsproblem", "paper"),
    ("SEED-CHURCH-1936", "An Unsolvable Problem of Elementary Number Theory", "paper"),
    ("SEED-ROSSER-1936", "Extensions of Some Theorems of Gödel and Church", "paper"),
    ("SEED-KLEENE-1938", "On Notation for Ordinal Numbers", "paper"),
    ("SEED-POST-1944", "Recursively Enumerable Sets of Positive Integers and Their Decision Problems", "paper"),
    ("SEED-RICE-1953", "Classes of Recursively Enumerable Sets and Their Decision Problems", "paper"),
    ("SEED-LOB-1955", "Solution of a Problem of Leon Henkin", "paper"),
    ("SEED-RADO-1962", "On Non-Computable Functions", "paper"),
    ("SEED-LAWVERE-1969", "Diagonal Arguments and Cartesian Closed Categories", "paper"),
    ("SEED-CAPRETTA-2005", "General Recursion via Coinductive Types", "paper"),
    ("SEED-OConnor-2005", "Essential Incompleteness of Arithmetic Verified by Coq", "paper"),
    ("SEED-PARTIALITY-REVISITED", "Partiality, Revisited", "paper"),
    ("SEED-2LTT-2017", "Two-Level Type Theory and Applications", "paper"),
    ("SEED-DOMINANCES-2017", "Partial Elements and Recursion via Dominances in Univalent Type Theory", "paper"),
    ("SEED-CUBICAL-NORM-2021", "Normalization for Cubical Type Theory", "paper"),
    ("SEED-PARAMETRIC-CT-2021", "Parametric Church's Thesis: Synthetic Computability without Choice", "paper"),
    ("SEED-KIRST-HERMES-2021", "Synthetic Undecidability and Incompleteness of First-Order Axiom Systems in Coq", "paper"),
    ("SEED-CUBICAL-ASSEMBLIES", "On Church's Thesis in Cubical Assemblies", "paper"),
    ("SEED-KIRST-PETERS-2023", "Gödel's Theorem Without Tears - Essential Incompleteness in Synthetic Computability", "paper"),
    ("SEED-INTERNAL-SCONING-2023", "For the Metatheory of Type Theory, Internal Sconing Is Enough", "paper"),
    ("SEED-CANONICITY-COMPUTABILITY-2023", "Canonicity and Computability in Homotopy Type Theory", "paper"),
    ("SEED-ORACLE-MODALITIES-2024", "Oracle modalities", "paper"),
    ("SEED-POST-CIC-2024", "The Kleene-Post and Post's Theorem in the Calculus of Inductive Constructions", "paper"),
    ("SEED-SYNTHETIC-OVERVIEW-2025", "Synthetic Mathematics for the Mechanisation of Computability Theory and Logic", "paper"),
    ("SEED-COFIBRATION-COMPLEXITY-2025", "Complexity of Cubical Cofibration Logics I: coNP-Complete Examples", "paper"),
    ("SEED-STRICTIFIED-SYNTAX-2025", "Type Theory in Type Theory using a Strictified Syntax", "paper"),
    ("SEED-ORDINAL-DECIDABILITY-2026", "Generalized Decidability via Brouwer Trees", "paper"),
    ("SEED-GROUPOID-SYNTAX-2026", "The Groupoid-Syntax of Type Theory Is a Set", "paper"),
    ("SEED-EXTENSION-TYPES-2026", "Extension Types for Free", "paper"),
    ("SEED-AGDA-GODEL", "agda-godel-tree", "official_project"),
    ("SEED-LEAN-FOUNDATION", "FormalizedFormalLogic Foundation", "official_project"),
    ("SEED-METAROQ", "MetaRocq", "official_project"),
]


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    return re.sub(r"[^a-z0-9]+", "", value)


def contains_any(text: str, terms: tuple[str, ...]) -> list[str]:
    lowered = text.casefold()
    return [term for term in terms if term in lowered]


def classify(title: str) -> tuple[str, list[str]]:
    hott = contains_any(title, HOTT_TERMS)
    type_theory = contains_any(title, TYPE_THEORY_TERMS)
    computation = contains_any(title, COMPUTATION_TERMS)
    direct = contains_any(title, DIRECT_PHRASES)
    reasons: list[str] = []
    if direct:
        reasons.append("direct_phrase:" + ",".join(direct))
    if hott:
        reasons.append("hott:" + ",".join(hott))
    if computation:
        reasons.append("computation:" + ",".join(computation))
    if direct or (hott and computation):
        return "DIRECT_TITLE_SIGNAL", reasons
    if (type_theory and computation) or hott:
        if type_theory and not hott:
            reasons.append("type_theory:" + ",".join(type_theory))
        return "ADJACENT_TITLE_SIGNAL", reasons
    return "UNCLASSIFIED_TITLE_INSUFFICIENT", ["requires_abstract_or_primary_source_review"]


def build(source: Path, output: Path) -> int:
    if output.exists():
        raise SystemExit("OUTPUT_EXISTS")
    raw = source.read_bytes()
    source_doc = json.loads(raw)
    rows = source_doc["candidates"]
    triaged = []
    counts: Counter[str] = Counter()
    for row in rows:
        tier, reasons = classify(str(row["title"]))
        item = dict(row)
        item["triage_tier"] = tier
        item["triage_reasons"] = reasons
        triaged.append(item)
        counts[tier] += 1
    title_map: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        title_map.setdefault(normalize(str(row["title"])), []).append(row)
    seed_rows = []
    for seed_id, title, kind in SEEDS:
        matches = title_map.get(normalize(title), []) if kind == "paper" else []
        seed_rows.append({
            "seed_id": seed_id,
            "title": title,
            "kind": kind,
            "discovery_match": bool(matches),
            "candidate_keys": [row["candidate_key"] for row in matches],
            "status": "DISCOVERED_EXACT_TITLE" if matches else "REQUIRES_MANUAL_PRIMARY_ENTRY",
        })
    document = {
        "schema_version": SCHEMA,
        "asset_class": "MACHINE_GENERATED_CONSERVATIVE_TRIAGE",
        "source_path": str(source),
        "source_bytes": len(raw),
        "source_sha256": sha(raw),
        "evidence_boundary": "TITLE_SIGNAL_ONLY_NO_EXCLUSION_NO_PRIMARY_SOURCE_QUALIFICATION",
        "counts": dict(sorted(counts.items())),
        "total": len(triaged),
        "seed_count": len(seed_rows),
        "seed_exact_matches": sum(row["discovery_match"] for row in seed_rows),
        "seed_manual_entries": sum(not row["discovery_match"] for row in seed_rows),
        "seeds": seed_rows,
        "candidates": triaged,
    }
    output.write_text(json.dumps(document, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "TRIAGE_CREATED",
        "output": str(output.resolve()),
        "total": len(triaged),
        "counts": dict(sorted(counts.items())),
        "seed_exact_matches": document["seed_exact_matches"],
        "seed_manual_entries": document["seed_manual_entries"],
    }, ensure_ascii=False))
    return 0


def verify(source: Path, output: Path) -> int:
    document = json.loads(output.read_text(encoding="utf-8"))
    raw = source.read_bytes()
    errors: list[str] = []
    if document.get("schema_version") != SCHEMA:
        errors.append("SCHEMA")
    if document.get("source_sha256") != sha(raw) or document.get("source_bytes") != len(raw):
        errors.append("SOURCE_IDENTITY")
    rows = document.get("candidates", [])
    if len(rows) != document.get("total"):
        errors.append("TOTAL")
    keys = [row.get("candidate_key") for row in rows]
    if len(keys) != len(set(keys)):
        errors.append("DUPLICATE_KEYS")
    recomputed = Counter(row.get("triage_tier") for row in rows)
    if dict(sorted(recomputed.items())) != document.get("counts"):
        errors.append("COUNTS")
    if any(row.get("triage_tier") not in {"DIRECT_TITLE_SIGNAL", "ADJACENT_TITLE_SIGNAL", "UNCLASSIFIED_TITLE_INSUFFICIENT"} for row in rows):
        errors.append("UNKNOWN_TIER")
    if len(document.get("seeds", [])) != len(SEEDS):
        errors.append("SEEDS")
    status = "VALID" if not errors else "INVALID"
    print(json.dumps({"status": status, "errors": errors, "total": len(rows), "counts": dict(sorted(recomputed.items())), "seed_count": len(document.get("seeds", []))}, ensure_ascii=False))
    return 0 if not errors else 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("build", "verify"):
        item = sub.add_parser(command)
        item.add_argument("--source", type=Path, required=True)
        item.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    return build(args.source, args.output) if args.command == "build" else verify(args.source, args.output)


if __name__ == "__main__":
    raise SystemExit(main())
