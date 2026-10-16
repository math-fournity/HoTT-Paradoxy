#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DECLARATIONS = {
    "claim": (ROOT / "CLAIM_LEDGER.md", re.compile(r"^\|\s*(Z-\d+)\s*\|", re.M)),
    "proof": (ROOT / "PROOF_ATTEMPTS.md", re.compile(r"^##\s+(PA-\d+)\b", re.M)),
    "result": (ROOT / "RESULTS.md", re.compile(r"^##\s+(R-\d+)\b", re.M)),
    "literature": (ROOT / "LITERATURE_MAP.md", re.compile(r"^##\s+(LIT-\d+)\b", re.M)),
}

report: dict[str, object] = {
    "schema_version": "hott_z_round3_index_integrity.v1",
    "files": {},
    "ok": True,
}
all_declared: set[str] = set()

for kind, (path, pattern) in DECLARATIONS.items():
    text = path.read_text(encoding="utf-8")
    ids = pattern.findall(text)
    counts = Counter(ids)
    duplicates = sorted(k for k, v in counts.items() if v > 1)
    all_declared.update(ids)
    report["files"][kind] = {
        "path": str(path.relative_to(ROOT)),
        "declaration_count": len(ids),
        "unique_count": len(counts),
        "duplicates": duplicates,
        "max_numeric_id": max((int(re.search(r"\d+", x).group()) for x in ids), default=None),
    }
    if duplicates:
        report["ok"] = False

# Check that the source-specific validated index only references declared research IDs.
index_path = ROOT / "HOTT_Z_后续研究可用性总索引_第三轮.md"
index_text = index_path.read_text(encoding="utf-8")
refs = set(re.findall(r"\b(?:Z|PA|R|LIT)-\d+\b", index_text))
missing = sorted(refs - all_declared)
report["validated_index"] = {
    "path": str(index_path.relative_to(ROOT)),
    "reference_count": len(refs),
    "missing_declarations": missing,
}
if missing:
    report["ok"] = False

# Source registry uniqueness.
registry_path = ROOT / "HOTT_Z_SOURCE_REGISTRY.json"
registry = json.loads(registry_path.read_text(encoding="utf-8"))
source_ids = [s["id"] for s in registry.get("sources", [])]
source_dups = sorted(k for k, v in Counter(source_ids).items() if v > 1)
report["source_registry"] = {
    "path": str(registry_path.relative_to(ROOT)),
    "source_count": len(source_ids),
    "unique_count": len(set(source_ids)),
    "duplicates": source_dups,
}
if source_dups:
    report["ok"] = False

# Expected final active maxima after reconciliation.
expected = {"claim": 162, "proof": 76, "result": 73, "literature": 63}
maxima_ok = True
for kind, value in expected.items():
    actual = report["files"][kind]["max_numeric_id"]
    if actual != value:
        maxima_ok = False
report["expected_maxima"] = {"expected": expected, "ok": maxima_ok}
if not maxima_ok:
    report["ok"] = False

json_path = ROOT / "verification" / "round3_index_integrity_check.json"
txt_path = ROOT / "verification" / "round3_index_integrity_check.txt"
json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

lines = [
    "HOTT-Z round 3 index integrity check",
    f"overall_ok: {str(report['ok']).lower()}",
]
for kind, info in report["files"].items():
    lines.append(
        f"{kind}: declarations={info['declaration_count']} unique={info['unique_count']} "
        f"max={info['max_numeric_id']} duplicates={info['duplicates']}"
    )
lines.append(f"validated_index_missing: {missing}")
lines.append(f"source_registry_duplicates: {source_dups}")
lines.append(f"expected_maxima_ok: {str(maxima_ok).lower()}")
txt_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

print("\n".join(lines))
raise SystemExit(0 if report["ok"] else 1)
