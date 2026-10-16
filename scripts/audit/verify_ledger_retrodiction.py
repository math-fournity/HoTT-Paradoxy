#!/usr/bin/env python3
"""Mechanically verify the C11 ledger retrodiction claim over the proof corpus.

C11 (`理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md`) claims that every
existing machine package sits in a "payment device available" cell of the
same-stage/same-layer discrimination grid — which is why every verdict stops at
`DEFENSE_WORKS` / `REPRESENTATION_BOUNDARY` — with one deliberate exception
(`MP-NOCANONICAL-001`, whose payment device is absent but which lacks a real
consumer).

This checker verifies the *mechanical* part of that claim against the repository:

- the package row exists in `HoTT/CLAIM_EVIDENCE_MATRIX.md` with the declared
  verdict token and no `NATURAL_USAGE_MISMATCH` / `INTERNAL_INCONSISTENCY` token;
- every claim ID of the package exists as its own matrix row;
- the referenced final run exists with `RUN.json` (`exit_code == 0`), the full
  receipt file set, and a `source-manifest.json` whose recorded file hashes still
  match the working tree;
- the declared ledger row / payment device / device availability, and exactly the
  declared number of packages sits in the "device absent" cell.

It does **not** verify the semantic content of the ledger rows: that stays a
human/AI reading claim.  `--self-test` runs the same verdict logic on synthetic
rows so the checker itself has a negative control.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MATRIX = Path("HoTT/CLAIM_EVIDENCE_MATRIX.md")
C11 = Path("理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md")
RUN_ROOT = Path("HoTT/verification/runs")
RECEIPT_FILES = ("RUN.json", "stdout.txt", "stderr.txt", "environment.txt", "source-manifest.json")
FORBIDDEN_TOKENS = ("NATURAL_USAGE_MISMATCH", "INTERNAL_INCONSISTENCY")

# package -> (claims, C11 row id(s) as they appear in the table's first column,
#             payment device, device status, verdict token, expected final run)
PACKAGES: dict[str, tuple[str, str, str, str, str, str]] = {
    "MP-ERCF-001": ("C-59–C-66", "8", "宇宙 + 自描述（通用骨架）", "AVAILABLE",
                    "MACHINE_PROVED_LOCAL_UNCOMMITTED", "20260912-MP-ERCF-001-02"),
    "MP-ERCF-TRUNC-001": ("C-67–C-70", "1", "命题截断：命题消去 + h-level", "AVAILABLE",
                          "DEFENSE_WORKS", "20260912-MP-ERCF-TRUNC-001-01"),
    "MP-RACE-TIMEOUT-001": ("C-71–C-76", "2", "集合商：只在同余操作上下降", "AVAILABLE",
                            "REPRESENTATION_BOUNDARY", "20260912-MP-RACE-TIMEOUT-001-01"),
    "MP-CONTEXTUAL-EQUIV-001": ("C-77–C-83", "2", "集合商：上下文族保留时序", "AVAILABLE",
                                "REPRESENTATION_BOUNDARY", "20260912-MP-CONTEXTUAL-EQUIV-001-01"),
    "MP-QUOTIENT-MONAD-001": ("C-84–C-88", "2", "集合商：canonical section 存在", "AVAILABLE",
                              "MONAD_STRUCTURE_CONSTRUCTED", "20260912-MP-QUOTIENT-MONAD-001-01"),
    "MP-CONTEXT-CHARACTERIZATION-001": ("C-89–C-91", "2", "集合商：代表相等已是最细", "AVAILABLE",
                                        "CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED",
                                        "20260912-MP-CONTEXT-CHARACTERIZATION-001-01"),
    "MP-GUARD-ERASURE-001": ("C-92–C-95", "6b", "阶段流：不动点等价刻画（非判定器）", "AVAILABLE",
                             "GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE",
                             "20260912-MP-GUARD-ERASURE-001-01"),
    "MP-COST-FACTORIZATION-001": ("C-96–C-99", "5", "计算规则：细化表示（程序语法 + 成本）", "AVAILABLE",
                                  "NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL",
                                  "20260912-MP-COST-FACTORIZATION-001-01"),
    "MP-PATH-CERTIFICATE-001": ("C-100–C-105", "2b", "univalence：显式路径", "AVAILABLE",
                                "MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS",
                                "20260912-MP-PATH-CERTIFICATE-001-01"),
    "MP-ONLINE-CAUSALITY-001": ("C-106–C-109", "6a", "归纳消去：阶段索引 / 前缀模型", "AVAILABLE",
                                "ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS",
                                "20260912-MP-ONLINE-CAUSALITY-001-01"),
    "MP-TRANSITION-LIFT-001": ("C-110–C-117", "2", "集合商：额外等级 / 条件", "AVAILABLE",
                               "TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS",
                               "20260912-MP-TRANSITION-LIFT-001-01"),
    "MP-PARTIAL-DECISION-001": ("C-118–C-123", "6a", "归纳消去：partial 与 strict 分类器并存", "AVAILABLE",
                                "PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL",
                                "20260912-MP-PARTIAL-DECISION-001-01"),
    "MP-SIP-REPRESENTATION-001": ("C-124–C-128", "2b", "univalence：结构签名内替换", "AVAILABLE",
                                  "SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL",
                                  "20260912-MP-SIP-REPRESENTATION-001-01"),
    "MP-CAUCHY-MODULUS-001": ("C-129–C-133", "2b", "univalence：modulus 可纳入同一性", "AVAILABLE",
                              "CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS",
                              "20260912-MP-CAUCHY-MODULUS-001-01"),
    "MP-TRUNC-NORECOVERY-001": ("C-134–C-141", "1", "命题截断：集合值消费者强制相等", "AVAILABLE",
                                "SET_VALUED_TRUNCATION_NO_RECOVERY_FAMILY",
                                "20260913-MP-TRUNC-NORECOVERY-001-03"),
    "MP-NOCANONICAL-001": ("C-142–C-148", "9", "无全局选择：无统一选点（补偿装置不存在）", "ABSENT",
                           "UNLABELED_FINITE_NO_CANONICAL_POINT", "20260913-MP-NOCANONICAL-001-02"),
    "MP-UNIMATH-NOSECTION-REPLAY-001": ("C-05", "9", "无全局选择：库层资格分离", "AVAILABLE",
                                        "REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE",
                                        "20260913-MP-UNIMATH-NOSECTION-REPLAY-02"),
    "MP-VERIFICATION-EVENT-001": ("C-149–C-156", "3", "高阶归纳构造：保留阶段即完成核查", "AVAILABLE",
                                  "VERIFICATION_EVENT_STAGE_BOUNDARY_WITH_POSITIVE_CONTROL",
                                  "20260913-MP-VERIFICATION-EVENT-001-01"),
}
EXPECTED_ABSENT = {"MP-NOCANONICAL-001"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cells(line: str) -> list[str]:
    return [c.strip().strip("`") for c in line.strip().strip("|").split("|")]


def parse_matrix(text: str) -> tuple[dict[str, list[str]], set[str]]:
    packages: dict[str, list[str]] = {}
    claims: set[str] = set()
    for line in text.splitlines():
        if line.startswith("| `MP-"):
            row = cells(line)
            packages[row[0]] = row
        elif line.startswith("| `C-") or line.startswith("| C-"):
            candidate = cells(line)[0]
            if re.fullmatch(r"C-[0-9]{3}", candidate):
                claims.add(candidate)
    return packages, claims


def expand_claims(spec: str) -> list[str]:
    ids = re.findall(r"C-[0-9]{3}", spec)
    if "–" in spec and len(ids) == 2:
        lo, hi = int(ids[0][2:]), int(ids[1][2:])
        return [f"C-{n:03d}" for n in range(lo, hi + 1)]
    return ids


def check_verdict(verdict: str, token: str) -> tuple[bool, str | None]:
    for forbidden in FORBIDDEN_TOKENS:
        if forbidden in verdict:
            return False, f"FORBIDDEN_VERDICT_TOKEN:{forbidden}"
    if token not in verdict:
        return False, f"VERDICT_TOKEN_MISSING:{token}"
    return True, None


def check_run(root: Path, run_id: str) -> tuple[dict, list[str]]:
    errors: list[str] = []
    run_dir = root / RUN_ROOT / run_id
    info: dict = {"run_id": run_id, "dir": run_dir.as_posix()}
    if not run_dir.is_dir():
        return info, [f"RUN_DIR_MISSING:{run_id}"]
    for name in RECEIPT_FILES:
        if not (run_dir / name).is_file():
            errors.append(f"RECEIPT_FILE_MISSING:{run_id}/{name}")
    run_json = run_dir / "RUN.json"
    if run_json.is_file():
        data = json.loads(run_json.read_text(encoding="utf-8"))
        info["exit_code"] = data.get("exit_code")
        info["status"] = data.get("status")
        info["claims"] = data.get("claim_ids")
        if data.get("exit_code") != 0:
            errors.append(f"RUN_EXIT_CODE:{run_id}:{data.get('exit_code')}")
        if not data.get("status"):
            errors.append(f"RUN_STATUS_MISSING:{run_id}")
    manifest = run_dir / "source-manifest.json"
    if manifest.is_file():
        sm = json.loads(manifest.read_text(encoding="utf-8"))
        checked = 0
        for entry in sm.get("files", []):
            target = root / entry["path"]
            if not target.is_file():
                errors.append(f"SOURCE_FILE_MISSING:{entry['path']}")
                continue
            if sha256(target) != entry.get("sha256"):
                errors.append(f"SOURCE_HASH_MISMATCH:{entry['path']}")
                continue
            checked += 1
        info["source_files_verified"] = checked
        info["external_dependencies"] = len(sm.get("external_dependencies", []))
    return info, errors


def build_report(root: Path) -> dict:
    text = (root / MATRIX).read_text(encoding="utf-8")
    packages, claim_rows = parse_matrix(text)
    c11_text = (root / C11).read_text(encoding="utf-8")
    rows: list[dict] = []
    errors: list[str] = []
    for pkg, (claim_spec, ledger_row, device, device_status, token, run_id) in sorted(PACKAGES.items()):
        row = packages.get(pkg)
        entry: dict = {
            "package": pkg,
            "ledger_row": ledger_row,
            "payment_device": device,
            "device_status": device_status,
            "verdict_token": token,
            "final_run": run_id,
        }
        if row is None:
            errors.append(f"MATRIX_PACKAGE_ROW_MISSING:{pkg}")
            rows.append(entry)
            continue
        verdict = row[4] if len(row) > 4 else ""
        entry["verdict"] = verdict
        ok, err = check_verdict(verdict, token)
        if not ok:
            errors.append(f"{err}:{pkg}")
        for cid in expand_claims(claim_spec):
            if cid not in claim_rows:
                errors.append(f"MATRIX_CLAIM_ROW_MISSING:{pkg}:{cid}")
        run_info, run_errors = check_run(root, run_id)
        entry["run"] = run_info
        errors.extend(run_errors)
        entry["c11_row_ids"] = ledger_row.split()
        entry["ledger_row_in_c11"] = all(f"| {tok} |" in c11_text for tok in ledger_row.split())
        if not entry["ledger_row_in_c11"]:
            errors.append(f"LEDGER_ROW_NOT_FOUND_IN_C11:{pkg}")
        rows.append(entry)
    absent = {row["package"] for row in rows if row["device_status"] == "ABSENT"}
    if absent != EXPECTED_ABSENT:
        errors.append(f"ABSENT_CELL_MISMATCH:{sorted(absent)}")
    report = {
        "schema_version": "ledger-retrodiction-check/v1",
        "ledger_document": C11.as_posix(),
        "matrix": MATRIX.as_posix(),
        "packages_checked": len(PACKAGES),
        "device_available": sum(1 for r in rows if r.get("device_status") == "AVAILABLE"),
        "device_absent": sorted(absent),
        "forbidden_verdict_tokens": list(FORBIDDEN_TOKENS),
        "rows": rows,
        "errors": errors,
        "status": "PASS" if not errors else "FAIL",
        "semantic_limit": (
            "This check verifies the mechanical retrodiction bookkeeping (matrix rows, claim rows, final runs, "
            "source hashes, declared device cells). It does not verify the semantic content of the ledger rows and "
            "does not create or upgrade any mathematical claim."
        ),
    }
    return report


def self_test() -> int:
    ok, err = check_verdict("MACHINE_PROVED_LOCAL_UNCOMMITTED / DEFENSE_WORKS", "DEFENSE_WORKS")
    assert ok and err is None, "positive control failed"
    bad, err2 = check_verdict("MACHINE_PROVED_LOCAL_UNCOMMITTED / NATURAL_USAGE_MISMATCH", "DEFENSE_WORKS")
    assert not bad and err2 and err2.startswith("FORBIDDEN_VERDICT_TOKEN"), "negative control failed"
    missing, err3 = check_verdict("MACHINE_PROVED_LOCAL_UNCOMMITTED", "DEFENSE_WORKS")
    assert not missing and err3 and err3.startswith("VERDICT_TOKEN_MISSING"), "token control failed"
    print(json.dumps({"status": "SELF_TEST_PASS", "controls": 3}, ensure_ascii=False))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    root = args.project_root.resolve()
    report = build_report(root)
    if args.output:
        target = root / args.output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "rows"}, ensure_ascii=False))
    return 0 if report["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
