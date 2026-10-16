#!/usr/bin/env python3
"""Lint active HOTT-Z theory/paper files for previously refuted proof patterns.

This is a textual regression test, not a mathematical proof.  It intentionally
scans only active theory and paper manuscripts; historical source quotations and
red-team files are excluded.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = [ROOT / "theory", ROOT / "papers"]
EXCLUDE_PARTS = {"technical_appendices"}  # appendices may quote historical formulations

# Patterns are deliberately narrow. A hit means the active manuscript contains
# an unqualified old formulation that must be reviewed.
BANNED = {
    "map_point_as_loop_space": re.compile(r"Map\s*\(\s*(?:1|\*)\s*,\s*G\s*\)\s*(?:is|是|=|≃).*?(?:loop space|环空间)", re.I),
    "raw_godel_space": re.compile(r"G\s*[≃=]\s*Map\s*\(\s*(?:1|\*)\s*,\s*G\s*\)"),
    "universe_role_implies_equivalence": re.compile(r"U[_₀-₉i]+\s*≃\s*U[_₁-₉i+]+"),
    "hott_self_violates_univalence": re.compile(r"HoTT.{0,30}(?:自己|自身).{0,20}(?:违反|违背).{0,20}(?:单价|univalence)", re.I),
    "all_hott_arrows_reversible": re.compile(r"HoTT.{0,30}(?:所有|一切).{0,20}(?:箭头|函数|过程).{0,10}(?:可逆|reversible)", re.I),
    "observer_dimension_plus_one": re.compile(r"观察者.{0,30}(?:n\s*\+\s*1|高一维|更高一维)"),
    "quantum_successor_attack": re.compile(r"(?:量子纠缠|EPR).{0,40}(?:后继函数|successor)", re.I),
    "one_shot_transport_contradiction": re.compile(r"(?:一次性|one[- ]shot).{0,40}transport.{0,50}(?:矛盾|contradiction)", re.I),
    "undefined_translate_halting": re.compile(r"Translate\s*:\s*InformalProblem\s*[→-]+\s*Type"),
    "internal_inconsistency_claim": re.compile(r"(?:HoTT\s*(?:⊢|\\vdash)\s*(?:⊥|\\bot)|HoTT.{0,25}(?:内部不一致|inconsistent))", re.I),
}

ALLOWED_CONTEXT = {
    # Corrective statements may mention a banned expression only to deny it.
    "map_point_as_loop_space": ["not", "不是", "误认", "错误"],
    "raw_godel_space": ["not self-reference", "不含哥德尔自指", "废弃", "错误"],
    "universe_role_implies_equivalence": ["不能", "不应", "not", "invalid", "错误"],
    "all_hott_arrows_reversible": ["不能说", "not", "不证明", "不是"],
    "internal_inconsistency_claim": ["不能说", "not", "不证明", "不是", "does not"],
}

issues: list[dict[str, object]] = []
files_checked = 0
control_chars: list[dict[str, object]] = []
placeholders: list[dict[str, object]] = []

for base in TARGETS:
    for path in sorted(base.rglob("*.md")):
        if any(part in EXCLUDE_PARTS for part in path.parts):
            continue
        files_checked += 1
        text = path.read_text(encoding="utf-8")
        rel = str(path.relative_to(ROOT))
        split_lines = text.splitlines()
        for i, line in enumerate(split_lines, start=1):
            # Detect accidental C0 controls except tab.
            bad = [ord(ch) for ch in line if ord(ch) < 32 and ch != "\t"]
            if bad:
                control_chars.append({"file": rel, "line": i, "codes": bad})
            if re.search(r"\b(?:TODO|TBD|FIXME|XXX)\b", line):
                placeholders.append({"file": rel, "line": i, "text": line.strip()})
            for key, pat in BANNED.items():
                if not pat.search(line):
                    continue
                context = " ".join(split_lines[max(0, i-3):min(len(split_lines), i+1)]).lower()
                if any(tok.lower() in context for tok in ALLOWED_CONTEXT.get(key, [])):
                    continue
                issues.append({"rule": key, "file": rel, "line": i, "text": line.strip()})

report = {
    "schema_version": "hott_z.active_claim_lint.v1",
    "files_checked": files_checked,
    "banned_pattern_hits": issues,
    "control_character_hits": control_chars,
    "placeholder_hits": placeholders,
    "passed": not issues and not control_chars and not placeholders,
    "scope_note": "Textual regression check only; it does not establish mathematical validity.",
}

out_json = ROOT / "verification" / "active_claim_lint.json"
out_txt = ROOT / "verification" / "active_claim_lint.txt"
out_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
lines = [
    "HOTT-Z active claim lint",
    f"files_checked={files_checked}",
    f"banned_pattern_hits={len(issues)}",
    f"control_character_hits={len(control_chars)}",
    f"placeholder_hits={len(placeholders)}",
    f"passed={str(report['passed']).lower()}",
]
for issue in issues + control_chars + placeholders:
    lines.append(json.dumps(issue, ensure_ascii=False))
out_txt.write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
raise SystemExit(0 if report["passed"] else 1)
