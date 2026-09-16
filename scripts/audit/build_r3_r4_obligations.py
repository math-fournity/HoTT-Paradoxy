#!/usr/bin/env python3
"""Build the exact R3-to-R4 HoTT calculus obligation matrix."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "audit/r3-r4-godel"
SCHEMA = "hott-r3-r4-obligation-matrix/v1"
RECEIPT_SCHEMA = "hott-r3-r4-obligation-receipt/v1"
ALLOWED_STATUS = {
    "PRESENT_MACHINE_PROVED",
    "PRESENT_SOURCE_REPORTED_NOT_REPLAYED",
    "ABSENT_BY_DEFINITION",
    "OPEN",
    "NOT_APPLICABLE",
}

R3_RUN = "HoTT/verification/runs/20260915-MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001-01"
GROUP_RUN = "HoTT/verification/runs/20260914-MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001-01"

SOURCES = [
    ".codex/research/hott/R3-R4-GODEL-RETURN-001.md",
    ".codex/research/hott/R4-HOTT-NAT-EFFECTIVITY-001.md",
    "HoTT/formal/external-coq-synthetic-incompleteness/CLAIM-R3-SYNTHETIC-INCOMPLETENESS.md",
    "HoTT/formal/external-coq-synthetic-incompleteness/Qualification.v",
    f"{R3_RUN}/RUN.json",
    f"{R3_RUN}/source-manifest.json",
    f"{R3_RUN}/index-row-manifest.json",
    "HoTT/formal/external-cubical-groupoid-syntax/CLAIM-G-HOTT-SYNTAX.md",
    f"{GROUP_RUN}/RUN.json",
    f"{GROUP_RUN}/index-row-manifest.json",
    "HoTT/CLAIM_EVIDENCE_MATRIX.md",
    "HoTT/verification/PROOF_VERSION_CLOSURE.json",
    "audit/ce-map/REPORT.md",
    "scripts/audit/build_r3_r4_obligations.py",
    "scripts/audit/test_r3_r4_obligations.py",
]


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def source_rows() -> list[dict[str, Any]]:
    rows = []
    for rel in sorted(SOURCES):
        path = ROOT / rel
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"SOURCE_MISSING:{rel}")
        data = path.read_bytes()
        rows.append({"path": rel, "bytes": len(data), "sha256": sha(data)})
    return rows


def obligations() -> list[dict[str, Any]]:
    return [
        {
            "id": "H-SYNTAX",
            "status": "PRESENT_MACHINE_PROVED",
            "present_scope": "Four-sort Con/Sub/Ty/Tm Cubical HIIT syntax with terminal context, context extension, U/El, Pi, lambda/app, beta/eta, truncation constructors and second-order coherence.",
            "missing_scope": "Nat, general object identity/Path, object univalence/HIT, and a single complete raw HoTT calculus.",
            "evidence": ["C-223", "C-226", "HoTT/formal/external-cubical-groupoid-syntax/CLAIM-G-HOTT-SYNTAX.md"],
        },
        {
            "id": "H-CONVERSION",
            "status": "OPEN",
            "present_scope": "The HIIT syntax carries judgmental/path equations and coherence constructors.",
            "missing_scope": "No total executable conversion or derivation checker for the exact quotient/HIIT object syntax has been constructed.",
            "evidence": ["C-223", "C-224"],
        },
        {
            "id": "H-NAT",
            "status": "ABSENT_BY_DEFINITION",
            "present_scope": "No Nat constructor occurs in the frozen TT syntax module denominator.",
            "missing_scope": "Nat formation, zero, successor, eliminator, computation rules, addition/multiplication and coding arithmetic.",
            "evidence": ["C-223", "C-226", "G-HOTT-SYNTAX-CORE-001"],
        },
        {
            "id": "H-ID/PATH",
            "status": "ABSENT_BY_DEFINITION",
            "present_scope": "Cubical paths are used by the host to define the HIIT and prove coherence.",
            "missing_scope": "A general identity/Path type former and its formation/introduction/elimination/computation rules inside the object calculus.",
            "evidence": ["C-223", "HoTT/formal/external-cubical-groupoid-syntax/CLAIM-G-HOTT-SYNTAX.md"],
        },
        {
            "id": "H-UNIVALENCE/HIT",
            "status": "ABSENT_BY_DEFINITION",
            "present_scope": "U/El and the syntax HIIT itself are present at the host/formalisation level.",
            "missing_scope": "Object-level univalence and named higher-inductive type rules in the exact calculus.",
            "evidence": ["C-223", "C-226"],
        },
        {
            "id": "H-PROOF-CODE",
            "status": "OPEN",
            "present_scope": "C-157-C-187 provide proof/formula coding for a separate small K/S/MP system.",
            "missing_scope": "Natural-number code, decoder, total checker and fair proof enumeration for derivations of the same HoTT calculus named by H-SYNTAX.",
            "evidence": ["C-157", "C-187", "R3-R4-GODEL-RETURN-001"],
        },
        {
            "id": "H-SUBSTITUTION",
            "status": "PRESENT_MACHINE_PROVED",
            "present_scope": "The groupoid syntax has typed substitutions, composition, identity, action on types/terms, and second-order coherence.",
            "missing_scope": "An executable capture-avoiding formula substitution operation on a proof-coded arithmetic/HoTT language suitable for diagonalisation.",
            "evidence": ["C-223", "C-225", "G-HOTT-SYNTAX-CORE-001"],
        },
        {
            "id": "H-ARITH-INTERP",
            "status": "OPEN",
            "present_scope": "R3 Coq source formalises Robinson Q and its standard first-order arithmetic infrastructure.",
            "missing_scope": "A machine-checked interpretation of Q or another sufficient arithmetic theory into the exact H-SYNTAX calculus.",
            "evidence": ["C-248", "C-223"],
        },
        {
            "id": "H-REPRESENTABILITY",
            "status": "OPEN",
            "present_scope": "C-246 assumes strong separation; the author R3 development proves it for its first-order arithmetic route.",
            "missing_scope": "Object-level strong representation of the HoTT proof predicate, coding and substitution functions in the target calculus.",
            "evidence": ["C-246", "C-248", "R3-R4-GODEL-RETURN-001"],
        },
        {
            "id": "H-FIXPOINT",
            "status": "OPEN",
            "present_scope": "The R3 package contains the recursive-separation/diagonal mechanism for its source theory.",
            "missing_scope": "A fixed-point/diagonal lemma whose quotation and substitution operate on the exact target HoTT derivation syntax.",
            "evidence": ["C-245", "C-246"],
        },
        {
            "id": "H-INDEPENDENCE",
            "status": "OPEN",
            "present_scope": "C-246 and C-248 establish conditional independence in general formal systems and Robinson-Q extensions.",
            "missing_scope": "An independent sentence theorem with the target T instantiated to the exact HoTT calculus and every premise discharged or retained explicitly.",
            "evidence": ["C-246", "C-248"],
        },
        {
            "id": "H-EFFECTIVITY",
            "status": "OPEN",
            "present_scope": "The R3 source theory assumes/proves enumerability in its own first-order setting; finite host source files type-check.",
            "missing_scope": "Effective enumeration of the exact target rule/axiom schemas and proof relation, including the status of univalence, HIT, resizing, quotient or oracle rules.",
            "evidence": ["C-248", "C-223", "C-226"],
        },
    ]


def build_core() -> tuple[dict[str, Any], str]:
    sources = source_rows()
    rows = obligations()
    ids = [row["id"] for row in rows]
    if len(ids) != 12 or len(set(ids)) != 12:
        raise ValueError("OBLIGATION_DENOMINATOR_INVALID")
    for row in rows:
        if row["status"] not in ALLOWED_STATUS:
            raise ValueError(f"STATUS_INVALID:{row['id']}:{row['status']}")
        if not row["evidence"] or not row["present_scope"] or not row["missing_scope"]:
            raise ValueError(f"OBLIGATION_FIELDS_MISSING:{row['id']}")
    rows.sort(key=lambda row: ids.index(row["id"]))
    counts = dict(sorted(Counter(row["status"] for row in rows).items()))
    blockers = [row["id"] for row in rows if row["status"] in {"OPEN", "ABSENT_BY_DEFINITION"}]
    snapshot = sha(json_bytes(sources))
    matrix = {
        "schema_version": SCHEMA,
        "status": "R3_MACHINE_REPLAYED_R4_OBLIGATION_MATRIX_COMPLETE_WITH_SCOPE",
        "source_snapshot": snapshot,
        "source_theory": {
            "id": "R3-COQ-SYNTHETIC-INCOMPLETENESS-CD7D849",
            "proof_id": "MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001",
            "claims": ["C-244", "C-245", "C-246", "C-247", "C-248", "C-249"],
            "scope": "Conditional general essential incompleteness and Robinson-Q independence in first-order arithmetic.",
        },
        "target_calculus": {
            "id": "G-HOTT-GROUPOID-SYNTAX-5BABC385",
            "proof_id": "MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001",
            "claims": ["C-223", "C-224", "C-225", "C-226"],
            "scope": "Exact Pi/U/El four-sort groupoid syntax slice, not a complete HoTT calculus.",
        },
        "allowed_status": sorted(ALLOWED_STATUS),
        "sources": sources,
        "counts": {"total": len(rows), "by_status": counts, "blockers": len(blockers)},
        "input_remainder": 0,
        "obligations": rows,
        "blocking_obligations": blockers,
        "r4_readiness": "NOT_READY",
        "hott_essentiality": "NOT_ESTABLISHED",
        "reality_correspondence": "NOT_ESTABLISHED",
        "next_minimal_slice": {
            "id": "R4-HOTT-NAT-EFFECTIVITY-001",
            "goal": "Choose or extend one exact target syntax with Nat and a finite derivation representation, then machine-check one end-to-end encoded derivation and a negative control.",
            "anti_shortcut": "Do not add representability, universality, consistency, or a proof predicate as an unproved constructor/postulate.",
        },
        "non_goals": [
            "The matrix does not prove that the missing obligations are impossible.",
            "The R3 theorem is not thereby instantiated to HoTT.",
            "Host-language definability is not object-language representability.",
            "No HoTT paradox, internal inconsistency, novelty, or reality-relative witness is claimed.",
        ],
    }
    return matrix, render_report(matrix)


def render_report(matrix: dict[str, Any]) -> str:
    table = "\n".join(
        f"| `{row['id']}` | `{row['status']}` | {row['present_scope']} | {row['missing_scope']} |"
        for row in matrix["obligations"]
    )
    counts = matrix["counts"]["by_status"]
    return f"""# R3→R4 Gödel 保真义务矩阵

状态：`{matrix['status']}`  
source snapshot：`{matrix['source_snapshot']}`  
R3 source：`MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001` / C-244–C-249  
R4 target slice：`MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001` / C-223–C-226

## 判词

R3 的一般 essential incompleteness 与 Robinson Q 条件独立句已在 Coq 8.15.2 中从 exact source archive 重放。它尚未成为 HoTT 不完备性定理。12 项 R4 义务中，`PRESENT_MACHINE_PROVED`={counts.get('PRESENT_MACHINE_PROVED', 0)}、`ABSENT_BY_DEFINITION`={counts.get('ABSENT_BY_DEFINITION', 0)}、`OPEN`={counts.get('OPEN', 0)}；R4 readiness=`NOT_READY`。

## 逐项矩阵

| 义务 | 状态 | 当前已有 | 要闭合的缺口 |
|---|---|---|---|
{table}

`H-SYNTAX` 与 `H-SUBSTITUTION` 的机器状态只覆盖当前 groupoid syntax 的结构层。宿主 Cubical Agda 的 Path 与 HIIT 能力不自动成为对象 calculus 的 `H-ID/PATH` 或 `H-UNIVALENCE/HIT`。C-157–C-187 的 proof code 属于另一小型系统，也不能直接填 `H-PROOF-CODE`。

## 下一最小切片

`{matrix['next_minimal_slice']['id']}`：{matrix['next_minimal_slice']['goal']}

禁止把 representability、universality、consistency 或 proof predicate 作为未证明 constructor/postulate 添加；那会把最主要的 Gödel 义务写进假设。

## 边界

本矩阵证明的是“当前证据在哪些义务上存在或缺失”的完整登记。它不证明缺口不可实现，不证明 exact HoTT R4，不证明 HoTT essentiality，也没有建立现实同任务桥梁。
"""


def bundle() -> dict[str, bytes]:
    first = build_core()
    second = build_core()
    matrix_bytes, report_bytes = json_bytes(first[0]), first[1].encode()
    if (matrix_bytes, report_bytes) != (json_bytes(second[0]), second[1].encode()):
        raise ValueError("NONDETERMINISTIC_BUILD")
    receipt = {
        "schema_version": RECEIPT_SCHEMA,
        "status": first[0]["status"],
        "source_snapshot": first[0]["source_snapshot"],
        "obligations": 12,
        "input_remainder": 0,
        "r4_readiness": "NOT_READY",
        "outputs": {
            "R3-R4-OBLIGATIONS.json": {"bytes": len(matrix_bytes), "sha256": sha(matrix_bytes)},
            "REPORT.md": {"bytes": len(report_bytes), "sha256": sha(report_bytes)},
        },
        "deterministic_repeat": True,
        "negative_control": "scripts/audit/test_r3_r4_obligations.py removes H-NAT and validator must fail",
    }
    return {
        "R3-R4-OBLIGATIONS.json": matrix_bytes,
        "REPORT.md": report_bytes,
        "RECEIPT.json": json_bytes(receipt),
    }


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(name, path)
    except BaseException:
        try:
            os.unlink(name)
        except FileNotFoundError:
            pass
        raise


def validate(output: Path, matrix_override: Path | None = None) -> dict[str, Any]:
    paths = {
        "R3-R4-OBLIGATIONS.json": matrix_override or output / "R3-R4-OBLIGATIONS.json",
        "REPORT.md": output / "REPORT.md",
        "RECEIPT.json": output / "RECEIPT.json",
    }
    for path in paths.values():
        if not path.is_file():
            raise ValueError(f"OUTPUT_MISSING:{path}")
    actual = {name: path.read_bytes() for name, path in paths.items()}
    matrix = json.loads(actual["R3-R4-OBLIGATIONS.json"])
    if matrix.get("schema_version") != SCHEMA:
        raise ValueError("MATRIX_SCHEMA")
    rows = matrix.get("obligations", [])
    ids = [row.get("id") for row in rows]
    expected_ids = [row["id"] for row in obligations()]
    if ids != expected_ids:
        raise ValueError(f"OBLIGATION_DENOMINATOR_MISMATCH:{ids}")
    for row in rows:
        if row.get("status") not in ALLOWED_STATUS or not row.get("evidence"):
            raise ValueError(f"OBLIGATION_INVALID:{row.get('id')}")
    if matrix.get("input_remainder") != 0 or matrix.get("counts", {}).get("total") != 12:
        raise ValueError("MATRIX_REMAINDER")
    receipt = json.loads(actual["RECEIPT.json"])
    if receipt.get("schema_version") != RECEIPT_SCHEMA or receipt.get("obligations") != 12:
        raise ValueError("RECEIPT_INVALID")
    for name in ("R3-R4-OBLIGATIONS.json", "REPORT.md"):
        identity = receipt["outputs"][name]
        if identity["bytes"] != len(actual[name]) or identity["sha256"] != sha(actual[name]):
            raise ValueError(f"RECEIPT_HASH:{name}")
    drift = []
    for row in matrix["sources"]:
        path = ROOT / row["path"]
        if not path.is_file() or len(path.read_bytes()) != row["bytes"] or sha(path.read_bytes()) != row["sha256"]:
            drift.append(row["path"])
    if not drift:
        expected = bundle()
        mismatch = [name for name in expected if actual[name] != expected[name]]
        if mismatch:
            raise ValueError(f"NONCANONICAL_OUTPUT:{mismatch}")
    return {
        "status": "VALID" if not drift else "VALID_WITH_SOURCE_EVOLUTION",
        "source_drift": drift,
        "obligations": len(rows),
        "by_status": matrix["counts"]["by_status"],
        "r4_readiness": matrix["r4_readiness"],
        "next": matrix["next_minimal_slice"]["id"],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build")
    build.add_argument("--write", action="store_true")
    build.add_argument("--output", type=Path, default=OUTPUT)
    check = sub.add_parser("validate")
    check.add_argument("--output", type=Path, default=OUTPUT)
    check.add_argument("--matrix", type=Path)
    query = sub.add_parser("query")
    query.add_argument("--output", type=Path, default=OUTPUT)
    query.add_argument("--obligation", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "build":
            values = bundle()
            if args.write:
                for name, data in values.items():
                    atomic_write(args.output.resolve() / name, data)
                result = validate(args.output.resolve())
            else:
                matrix = json.loads(values["R3-R4-OBLIGATIONS.json"])
                result = {"status": "DRY_RUN", "writes": False, "obligations": 12, "source_snapshot": matrix["source_snapshot"]}
        elif args.command == "validate":
            result = validate(args.output.resolve(), args.matrix.resolve() if args.matrix else None)
        else:
            validate(args.output.resolve())
            matrix = json.loads((args.output.resolve() / "R3-R4-OBLIGATIONS.json").read_text(encoding="utf-8"))
            matches = [row for row in matrix["obligations"] if row["id"] == args.obligation]
            if not matches:
                result = {"status": "NOT_FOUND", "obligation": args.obligation}
                print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
                return 1
            result = {"status": "FOUND", "obligation": matches[0]}
        print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "INVALID", "error": str(exc)}, ensure_ascii=False, sort_keys=True))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
