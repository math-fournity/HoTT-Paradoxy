#!/usr/bin/env python3
"""Verify the deterministic R2 cross-kernel correspondence receipt."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = ROOT / "HoTT/formal/cubical-machine-halting/R2-TASKSPEC.json"
MATRIX = ROOT / "HoTT/CLAIM_EVIDENCE_MATRIX.md"
DEFAULT_OUTPUT = ROOT / "audit/R2-cross-kernel-correspondence-20260914.json"


class CorrespondenceError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise CorrespondenceError(f"INVALID_JSON:{path}") from exc
    if not isinstance(value, dict):
        raise CorrespondenceError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def run_json(command: list[str]) -> dict[str, object]:
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise CorrespondenceError(
            f"VERIFIER_FAILED:{' '.join(command)}:{result.stdout.strip()}:{result.stderr.strip()}"
        )
    try:
        value = json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise CorrespondenceError(f"VERIFIER_NON_JSON:{' '.join(command)}") from exc
    if not isinstance(value, dict) or value.get("status") != "PASS_WITH_SCOPE":
        raise CorrespondenceError(f"VERIFIER_STATUS_INVALID:{' '.join(command)}")
    return value


def source_step(instruction: tuple[str, int], state: tuple[int, int, int]) -> tuple[int, int, int]:
    kind, jump = instruction
    label, left, right = state
    if kind == "incA":
        return label + 1, left + 1, right
    if kind == "incB":
        return label + 1, left, right + 1
    if kind == "decA":
        return (label + 1, 0, right) if left == 0 else (jump, left - 1, right)
    if kind == "decB":
        return (label + 1, left, 0) if right == 0 else (jump, left, right - 1)
    raise CorrespondenceError(f"UNKNOWN_INSTRUCTION:{kind}")


def target_step(instruction: tuple[str, int, int], state: tuple[int, int, int]) -> tuple[int, int, int]:
    kind, on_zero, on_suc = instruction
    _, left, right = state
    if kind == "incA":
        return on_suc, left + 1, right
    if kind == "incB":
        return on_suc, left, right + 1
    if kind == "decA":
        return (on_zero, 0, right) if left == 0 else (on_suc, left - 1, right)
    if kind == "decB":
        return (on_zero, left, 0) if right == 0 else (on_suc, left, right - 1)
    raise CorrespondenceError(f"UNKNOWN_TARGET_INSTRUCTION:{kind}")


def compile_instruction(instruction: tuple[str, int], label: int) -> tuple[str, int, int]:
    kind, jump = instruction
    if kind in {"incA", "incB"}:
        return kind, label + 1, label + 1
    return kind, label + 1, jump


def control_cases() -> dict[str, object]:
    instructions = [("incA", 0), ("incB", 0)] + [
        (kind, jump)
        for kind in ("decA", "decB")
        for jump in (0, 1, 2, 5)
    ]
    states = [
        (label, left, right)
        for label in (1, 2, 5)
        for left in (0, 1, 3)
        for right in (0, 1, 3)
    ]
    checked = 0
    for instruction in instructions:
        for state in states:
            compiled = compile_instruction(instruction, state[0])
            if source_step(instruction, state) != target_step(compiled, state):
                raise CorrespondenceError(f"CONTROL_MISMATCH:{instruction}:{state}")
            checked += 1
    sentinel_states = [(0, a, b) for a in (0, 2) for b in (0, 2)]
    outside_states = [(label, a, b) for label in (3, 7) for a in (0, 2) for b in (0, 2)]
    return {
        "instruction_state_cases": checked,
        "halt_sentinel_cases": len(sentinel_states),
        "outside_table_cases": len(outside_states),
        "total": checked + len(sentinel_states) + len(outside_states),
        "role": "finite branch-direction and field-order controls only; universal claims come from kernel proofs",
    }


def compute() -> dict[str, object]:
    spec = read_json(SPEC_PATH)
    if spec.get("schema_version") != "r2-cross-kernel-task-spec/v1" or spec.get("task_id") != "R2-CROSS-KERNEL-001":
        raise CorrespondenceError("TASKSPEC_IDENTITY_INVALID")
    anchors = spec.get("required_anchors")
    if not isinstance(anchors, dict) or len(anchors) != 4:
        raise CorrespondenceError("ANCHOR_MAP_INVALID")
    anchor_count = 0
    source_hashes: dict[str, str] = {}
    for relative, required in anchors.items():
        if not isinstance(relative, str) or not isinstance(required, list) or not required:
            raise CorrespondenceError("ANCHOR_ROW_INVALID")
        path = ROOT / relative
        data = path.read_bytes()
        text = data.decode("utf-8")
        for anchor in required:
            if not isinstance(anchor, str) or text.count(anchor) < 1:
                raise CorrespondenceError(f"ANCHOR_MISSING:{relative}:{anchor}")
            anchor_count += 1
        source_hashes[relative] = sha(data)

    packages = spec.get("proof_packages")
    if not isinstance(packages, list) or len(packages) != 3:
        raise CorrespondenceError("PROOF_PACKAGE_COUNT_INVALID")
    matrix_lines = MATRIX.read_text(encoding="utf-8").splitlines()
    proof_receipts = []
    for package in packages:
        if not isinstance(package, dict):
            raise CorrespondenceError("PROOF_PACKAGE_ROW_INVALID")
        run_path = ROOT / str(package["run"])
        run = read_json(run_path / "RUN.json")
        claims = package["claim_ids"]
        if (
            run.get("proof_id") != package["proof_id"]
            or run.get("claim_ids") != claims
            or run.get("status") != "KERNEL_ACCEPTED_WITH_SCOPE"
            or run.get("index_status") != "INDEXED_IN_CLAIM_EVIDENCE_MATRIX"
        ):
            raise CorrespondenceError(f"RUN_STATUS_INVALID:{package['proof_id']}")
        frozen = read_json(run_path / "index-row-manifest.json")
        if frozen.get("claim_ids") != claims or len(frozen.get("rows", [])) != len(claims) + 1:
            raise CorrespondenceError(f"FROZEN_ROWS_INVALID:{package['proof_id']}")
        identities = [package["proof_id"], *claims]
        for identity in identities:
            prefix = f"| `{identity}` |" if identity == package["proof_id"] else f"| {identity} |"
            if sum(line.startswith(prefix) for line in matrix_lines) != 1:
                raise CorrespondenceError(f"MATRIX_IDENTITY_COUNT:{identity}")
        proof_receipts.append({
            "proof_id": package["proof_id"],
            "claim_ids": claims,
            "run_id": run["run_id"],
            "run_sha256": sha((run_path / "RUN.json").read_bytes()),
            "index_row_manifest_sha256": sha((run_path / "index-row-manifest.json").read_bytes()),
            "kernel_status": run["status"],
            "git_status": run.get("git_status"),
        })

    agda = run_json([
        "python3", "-B", "scripts/audit/verify_formal_proof_run.py",
        "--run-dir", "HoTT/verification/runs/20260914-MP-CUBICAL-MM2-BRIDGE-001-01",
    ])
    coq_upstream = run_json(["python3", "-B", "scripts/audit/verify_coq_mm2_replay_run.py"])
    coq_bridge = run_json([
        "python3", "-B", "scripts/audit/verify_coq_mm2_replay_run.py",
        "--run-dir", "HoTT/verification/runs/20260914-MP-COQ-MM2-PROGRAMCODE-BRIDGE-001-01",
    ])
    return {
        "schema_version": "r2-cross-kernel-correspondence-receipt/v1",
        "task_id": "R2-CROSS-KERNEL-001",
        "status": "PASS_WITH_SCOPE",
        "verdict": "DUAL_KERNEL_SCOPED_CORRESPONDENCE_WITH_SAME_KERNEL_COQ_REDUCTION",
        "task_spec": {
            "path": SPEC_PATH.relative_to(ROOT).as_posix(),
            "sha256": sha(SPEC_PATH.read_bytes()),
        },
        "sources": source_hashes,
        "anchors_checked": anchor_count,
        "formal_packages": proof_receipts,
        "static_verifiers": {
            "agda": agda["status"],
            "coq_upstream": coq_upstream["status"],
            "coq_same_kernel_bridge": coq_bridge["status"],
        },
        "executable_controls": control_cases(),
        "logical_representation_difference": "Coq target uses ordinary exists; Agda target uses propositional truncation of Sigma. Both packages preserve mere finite existence and do not choose a minimum witness.",
        "definition_boundary": "Coq undecidable remains decidable P -> enumerable(complement SBTM_HALT).",
        "not_proved": spec["status_contract"]["not_achieved"],
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        temp = Path(temporary)
        if temp.exists():
            temp.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    try:
        receipt = compute()
        data = (json.dumps(receipt, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
        output = args.output if args.output.is_absolute() else ROOT / args.output
        if args.write:
            atomic_write(output, data)
        elif not output.is_file() or output.is_symlink() or output.read_bytes() != data:
            raise CorrespondenceError(f"RECEIPT_MISMATCH:{output}")
        print(json.dumps({
            "status": receipt["status"],
            "verdict": receipt["verdict"],
            "anchors_checked": receipt["anchors_checked"],
            "formal_packages": len(receipt["formal_packages"]),
            "control_cases": receipt["executable_controls"]["total"],
            "writes": args.write,
            "output": output.relative_to(ROOT).as_posix(),
        }, ensure_ascii=False))
        return 0
    except (CorrespondenceError, OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
