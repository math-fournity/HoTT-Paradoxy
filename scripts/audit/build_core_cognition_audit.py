#!/usr/bin/env python3
"""Create or verify a complete per-KC assessment table.

Generation is deliberately mechanical only.  The scaffold marks every row as
pending; it never infers semantic alignment from keywords.  A human/current AI
must replace each placeholder and the three-way decision, then ``--verify-only``
checks denominator, enums and non-placeholder evidence.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ALLOWED = {"ALIGNED", "DEEPENED", "CORRECTED", "TENSION", "DEVIATED", "NOT_TOUCHED"}
ROW_RE = re.compile(r"^\| `(?P<id>KC-[0-9]{6})` \| .*? \| `(?P<relation>[A-Z_]+)` \|(?P<rest>.*)$")


def manifest_units(root: Path) -> tuple[str, list[dict]]:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    units = manifest.get("units")
    if not isinstance(units, list) or not units:
        raise ValueError("CORE_UNITS_MISSING")
    return str(manifest.get("generation")), units


def build_scaffold(root: Path, session_id: str) -> Path:
    generation, units = manifest_units(root)
    target = root / ".codex/research/hott/sessions" / session_id / "CORE_COGNITION_AUDIT.md"
    if target.exists():
        raise ValueError(f"SESSION_AUDIT_ALREADY_EXISTS:{target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# 核心认知逐编号回评：{session_id}", "",
        f"> 状态：`DRAFT_REQUIRES_MANUAL_SEMANTIC_REVIEW`；generation：`{generation}`；KC 总数：`{len(units)}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in units:
        label = str(unit.get("semantic_label", "—")).replace("|", "\\|")
        lines.append(
            f"| `{unit['id']}` | `{unit.get('platform')}` / {label} | `NOT_TOUCHED` | "
            "REVIEW_REQUIRED_PLACEHOLDER | — | 逐项人工评估待完成。 |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `REVIEW_REQUIRED_PLACEHOLDER`",
        "- direction_change: `REVIEW_REQUIRED_PLACEHOLDER`",
        "- panorama_change: `REVIEW_REQUIRED_PLACEHOLDER`",
        "- update_decision: `REVIEW_REQUIRED_PLACEHOLDER`",
        "- cross_conflicts: `REVIEW_REQUIRED_PLACEHOLDER`",
        "- unresolved: `REVIEW_REQUIRED_PLACEHOLDER`", "",
    ])
    target.write_text("\n".join(lines), encoding="utf-8")
    return target


def verify(root: Path, session_id: str) -> dict[str, object]:
    generation, units = manifest_units(root)
    expected = [str(unit["id"]) for unit in units]
    target = root / ".codex/research/hott/sessions" / session_id / "CORE_COGNITION_AUDIT.md"
    body = target.read_text(encoding="utf-8")
    if "REVIEW_REQUIRED_PLACEHOLDER" in body:
        raise ValueError("AUDIT_PLACEHOLDER_REMAINS")
    rows = []
    for line in body.splitlines():
        match = ROW_RE.match(line)
        if match:
            rows.append((match.group("id"), match.group("relation"), match.group("rest")))
    actual = [row[0] for row in rows]
    if actual != expected:
        raise ValueError(f"KC_DENOMINATOR_OR_ORDER_MISMATCH:expected={len(expected)}:actual={len(actual)}")
    if any(relation not in ALLOWED for _, relation, _ in rows):
        raise ValueError("AUDIT_RELATION_INVALID")
    if any(" | — |" in rest or not rest.strip() for _, _, rest in rows):
        raise ValueError("AUDIT_EVIDENCE_MISSING")
    for field in ("core_change", "direction_change", "panorama_change", "update_decision", "cross_conflicts", "unresolved"):
        if not re.search(rf"(?m)^- {field}: `?.+", body):
            raise ValueError(f"THREE_WAY_DECISION_MISSING:{field}")
    counts = {value: sum(1 for _, relation, _ in rows if relation == value) for value in sorted(ALLOWED)}
    return {"status": "PASS", "session_id": session_id, "generation": generation,
            "kc_count": len(rows), "relation_counts": counts,
            "semantic_review": "PUBLIC_TEXT_PRESENT_NOT_MODEL_HIDDEN_STATE_CERTIFICATION"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--session-id", required=True)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    root = args.project_root.resolve()
    try:
        if args.verify_only:
            result = verify(root, args.session_id)
        else:
            path = build_scaffold(root, args.session_id)
            result = {"status": "SCAFFOLD_BUILT", "path": str(path), "semantic_review": "REQUIRED"}
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (OSError, UnicodeError, ValueError, TypeError, KeyError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
