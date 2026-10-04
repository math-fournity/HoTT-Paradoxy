#!/usr/bin/env python3
"""Capture MP-BARE-ZFC-Q-PRECISION-001 with a pinned Lean-core checker.

The capture records source-card documents as inputs without pretending Lean
proves their web/history content. The expected-negative control is captured
separately by the caller because it must exit nonzero.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import platform
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RUN_ID = sys.argv[1] if len(sys.argv) > 1 else "20261004-MP-BARE-ZFC-Q-PRECISION-001-01"
PROOF_ID = "MP-BARE-ZFC-Q-PRECISION-001"
SOURCE = Path("HoTT/formal/bare-zfc-q-precision/BareZFCPrecision.lean")
CLAIM = Path("HoTT/formal/bare-zfc-q-precision/CLAIM.md")
PACKAGE_README = Path("HoTT/formal/bare-zfc-q-precision/README.md")
TOOLCHAIN = Path("HoTT/formal/bare-zfc-q-precision/LEAN_CORE_TOOLCHAIN.json")
SOURCE_CARD = Path("audit/20261004-BARE-ZFC-Q-PRECISION-P0-P3-来源接口与完成合同.md")
NODECARD = Path("audit/20261004-P-DAG-SOURCE-095-BARE-ZFC-Q-PRECISION-NODECARD.md")
PROMPT = Path("audit/20261004-P-DAG-SOURCE-095-BARE-ZFC-Q-PRECISION-PROMPT.md")
WORKER_REPORT = Path("audit/20261004-P-DAG-SOURCE-095-BARE-ZFC-Q-PRECISION-Terra-Max.md")
USER_SOURCE = Path("sources/prompts/Codex-ZFC元理论子理论时间与完成桥-用户原文-20261003.md")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def main() -> None:
    if "/" in RUN_ID or not RUN_ID.startswith("20261004-MP-BARE-ZFC-Q-PRECISION-001-"):
        raise SystemExit("RUN_ID_INVALID")
    inputs = [ROOT / p for p in (
        SOURCE, CLAIM, PACKAGE_README, TOOLCHAIN, SOURCE_CARD, NODECARD,
        PROMPT, WORKER_REPORT, USER_SOURCE, Path(__file__).relative_to(ROOT),
    )]
    if any(not path.is_file() for path in inputs):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    toolchain = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    lean_spec = toolchain.get("lean")
    if not isinstance(lean_spec, dict) or not isinstance(lean_spec.get("root"), str):
        raise SystemExit("LEAN_TOOLCHAIN_INVALID")
    lean = Path(str(lean_spec["root"])) / "bin" / "lean"
    if not lean.is_file() or lean.is_symlink():
        raise SystemExit("LEAN_BINARY_INVALID")
    run = ROOT / "HoTT/verification/runs" / RUN_ID
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    argv = [str(lean), SOURCE.as_posix()]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, capture_output=True)
    completed = dt.datetime.now(dt.timezone.utc)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    accepted = result.returncode == 0 and b"sorryAx" not in result.stdout and b"declaration uses 'sorry'" not in result.stderr
    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": [row(path) for path in inputs],
        "external_dependencies": [{
            "label": "lean-4.34.1-core-binary",
            "local_path": str(lean),
            "bytes": lean.stat().st_size,
            "sha256": sha(lean.read_bytes()),
        }],
        "policy": "Source cards classify a fixed ZFC-supported application interface; Lean proves only the finite projection/decoder and completion-bridge consequences stated in BareZFCPrecision.lean.",
    }
    environment = (
        f"platform={platform.platform()}\nlean={version}\n"
        "imports=Lean core only\naxioms=printed in stdout; expected none\n"
    ).encode("utf-8")
    receipt = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": ["C-364"],
        "proof_assistant": "Lean",
        "proof_assistant_version": version,
        "theory_variant": toolchain["theory_variant"],
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": "Finite source-contract control: a fixed coarse standard-resolution application view does not determine OriginDone or pay a universal FormalDone-to-OriginDone bridge; richer contract/coded views do determine OriginDone.",
        "non_goals": [
            "Does not formalize bare ZFC syntax, a ZFC model, or ZFC inconsistency.",
            "Does not prove a source webpage or mathematical-community policy inside Lean.",
            "Does not prove that all ZFC encodings omit Q or that Zeno and HoTT are the same complete Q.",
        ],
        "axiom_policy": "The proof source prints Lean's kernel axiom report; this pinned core run is accepted only when the report shows no axioms.",
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    for key, name, data in (
        ("stdout", "stdout.txt", result.stdout),
        ("stderr", "stderr.txt", result.stderr),
        ("environment", "environment.txt", environment),
        ("source_manifest", "source-manifest.json", json_bytes(manifest)),
    ):
        write_new(run / name, data)
        receipt[key] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run / "RUN.json", json_bytes(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit": result.returncode}, ensure_ascii=False))


if __name__ == "__main__":
    main()
