#!/usr/bin/env python3
"""Verify the scoped H/R/K readiness dossier and its no-repeat anchors."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
INDEX = "audit/abx-action-20260921/H-R-K查找思路整备.md"
SHARDS = [
    "audit/abx-action-20260921/H-R-K查找思路整备/001 - 本轮完整问答与分类结论.md",
    "audit/abx-action-20260921/H-R-K查找思路整备/002 - 证据分母、时间线与代码运行资产.md",
    "audit/abx-action-20260921/H-R-K查找思路整备/003 - H、R、U 与操作合同覆盖矩阵.md",
    "audit/abx-action-20260921/H-R-K查找思路整备/004 - K、消费者与社区边界审计.md",
    "audit/abx-action-20260921/H-R-K查找思路整备/005 - 未覆盖义务、禁止重复与重新出发条件.md",
]
RECEIPT = "audit/abx-action-20260921/HRK-READINESS-VERIFICATION.json"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def count_history(path: str) -> int:
    return int(
        subprocess.check_output(
            ["git", "rev-list", "--count", "HEAD", "--", path],
            cwd=ROOT,
            text=True,
        ).strip()
    )


def tracked_inventory(path: str) -> dict[str, object]:
    paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", "HEAD", "--", path],
        cwd=ROOT,
        text=True,
    ).splitlines()
    return {
        "files": len(paths),
        "suffixes": dict(sorted(Counter(Path(item).suffix for item in paths).items())),
    }


def relevant_run_inventory() -> dict[str, object]:
    rows = []
    for run in sorted((ROOT / "HoTT/verification/runs").iterdir()):
        receipt = run / "RUN.json"
        if not receipt.is_file():
            continue
        try:
            data = json.loads(receipt.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        claims = data.get("claim_ids", [])
        if any(
            isinstance(claim, str) and claim.startswith("C-") and 250 <= int(claim[2:]) <= 324
            for claim in claims
        ):
            rows.append((data.get("status"), data.get("proof_assistant")))
    return {
        "run_json": len(rows),
        "status": dict(sorted(Counter(status for status, _ in rows).items())),
        "proof_assistant": dict(sorted(Counter(tool for _, tool in rows).items())),
    }


def need(path: str) -> Path:
    value = ROOT / path
    if not value.is_file():
        raise SystemExit(f"missing source: {path}")
    return value


def marker(path: str, text: str) -> None:
    if text not in need(path).read_text(encoding="utf-8"):
        raise SystemExit(f"missing marker {text!r} in {path}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    for path in [INDEX, *SHARDS]:
        need(path)
    for path in [
        "Astra继续尝试/断点与证明机制系统检查/第一轮执行报告.md",
        "Astra继续尝试/断点与证明机制系统检查/第三十五轮执行报告.md",
        "Astra继续尝试/断点与证明机制系统检查/系统化后续检查方案.md",
        "HoTT/formal/astra-breakpoint-check/PathExclusion.agda",
        "HoTT/formal/astra-breakpoint-check/EndpointMaps.agda",
        "HoTT/formal/agda-unimath/hott-z/NativeOpenInterval.agda",
        "HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda",
        "HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda",
        "audit/abx-action-20260921/ABX-3-D2-原生直接消费者审计.md",
        "audit/abx-action-20260921/ABX-圆环挑战的HoTT社区认识范围审计-20260921.md",
    ]:
        need(path)

    marker(SHARDS[0], "### 用户提问")
    marker(SHARDS[0], "### AI 最终回复")
    marker(SHARDS[1], "C-250–C-260")
    marker(SHARDS[1], "C-281–C-324")
    marker(SHARDS[2], "裸载体检查不足")
    marker(SHARDS[3], "D2")
    marker(SHARDS[4], "禁止重复清单")
    marker("HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda", "plainNNotSatisfied")
    marker("HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda", "samePairDifferentOperations")

    history = {
        "breakpoint_documents": count_history("Astra继续尝试/断点与证明机制系统检查"),
        "breakpoint_formal": count_history("HoTT/formal/astra-breakpoint-check"),
        "native_hott_z": count_history("HoTT/formal/agda-unimath/hott-z"),
        "flash": count_history("Flash的第一次寻找尝试"),
    }
    expected = {
        "breakpoint_documents": 67,
        "breakpoint_formal": 2,
        "native_hott_z": 19,
        "flash": 1,
    }
    if history != expected:
       raise SystemExit(f"history denominator changed: {history!r}")

    inventory = {
        "breakpoint_documents": tracked_inventory("Astra继续尝试/断点与证明机制系统检查"),
        "breakpoint_formal": tracked_inventory("HoTT/formal/astra-breakpoint-check"),
        "native_hott_z": tracked_inventory("HoTT/formal/agda-unimath/hott-z"),
        "flash_formal": tracked_inventory("HoTT/formal/flash-first-hunt"),
        "flash_documents": tracked_inventory("Flash的第一次寻找尝试"),
        "lean_geometry": tracked_inventory("HoTT/formal/astra-real-geometry"),
        "runs": relevant_run_inventory(),
    }
    expected_inventory = {
        "breakpoint_documents": {"files": 308, "suffixes": {".json": 19, ".md": 218, ".py": 5, ".txt": 66}},
        "breakpoint_formal": {"files": 15, "suffixes": {".agda": 15}},
        "native_hott_z": {"files": 43, "suffixes": {".agda": 43}},
        "flash_formal": {"files": 4, "suffixes": {".agda": 4}},
        "flash_documents": {"files": 3, "suffixes": {".md": 3}},
        "lean_geometry": {"files": 18, "suffixes": {".json": 6, ".lean": 6, ".py": 6}},
        "runs": {
            "run_json": 68,
            "status": {"KERNEL_ACCEPTED_WITH_SCOPE": 52, "KERNEL_REJECTED": 16},
            "proof_assistant": {"Agda (agda-unimath)": 22, "Cubical Agda": 36, "Lean": 10},
        },
    }
    if inventory != expected_inventory:
        raise SystemExit(f"file/run inventory changed: {inventory!r}")

    receipt = {
        "schema_version": "abx-hrk-readiness-verification/v1",
        "status": "PASS_WITH_SCOPE",
        "scope": (
            "Checks the declared H/R/K readiness document, selected source/code anchors, "
            "and fixed Git-history counts. It does not prove the semantic completeness of every "
            "historical file, a new topology, an actual K, or a HoTT defect."
        ),
        "files": {path: sha(need(path)) for path in [INDEX, *SHARDS]},
       "history_denominator": history,
        "tracked_inventory": inventory,
        "verdict": "HRK_PREPARATION_COVERAGE_REGISTERED_NO_REPEAT_WITHOUT_NEW_EVIDENCE",
    }
    if args.write:
        (ROOT / RECEIPT).write_text(
            json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
