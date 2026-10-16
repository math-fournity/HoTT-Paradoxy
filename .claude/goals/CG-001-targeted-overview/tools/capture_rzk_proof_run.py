#!/usr/bin/env python3
"""Capture one pinned Rzk proof run as an F-011 receipt (CG-001, goal-local).

Why this exists: scripts/audit/capture_agda_proof_run.py runs Cubical Agda only.
Claims about simplicial HoTT (sHoTT) need its native checker, Rzk.  This tool
writes the same receipt format (formal-proof-run/v1: RUN.json, stdout.txt,
stderr.txt, environment.txt, source-manifest.json), so the goal-local verifier
verify_cg001_run.py checks and replays Rzk runs exactly as it does Agda runs.

The toolchain is pinned by HoTT/formal/claude-cg001/directed-native/RZK_TOOLCHAIN.json
(official release asset with publisher digest, plus the extracted binary).

Usage:
  python3 .claude/goals/CG-001-targeted-overview/tools/capture_rzk_proof_run.py \
      --run-id 20260925-CG001-<NAME>-01 --proof-id MP-CG001-<NAME>-001 \
      --claim-id CG001-C-NN --source HoTT/formal/claude-cg001/<pkg>/<File>.rzk \
      --manifest-file HoTT/formal/claude-cg001/<pkg>/CLAIM.md \
      --scope "..." [--non-goal "..."]...
Exit code: 0 when the kernel accepts, 42 when it rejects (receipt written either way).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[4]
TOOLCHAIN = Path("HoTT/formal/claude-cg001/directed-native/RZK_TOOLCHAIN.json")
FORBIDDEN = ("#postulate", "#assume", "uses (", "--allow-holes")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def safe_relative(value: str) -> Path:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        raise SystemExit(f"UNSAFE_PATH:{value}")
    return Path(*path.parts)


def file_row(relative: Path) -> dict[str, object]:
    data = (ROOT / relative).read_bytes()
    return {"path": relative.as_posix(), "bytes": len(data), "sha256": sha(data)}


def artifact(run_dir: Path, name: str, data: bytes) -> dict[str, object]:
    (run_dir / name).write_bytes(data)
    return {"path": name, "bytes": len(data), "sha256": sha(data)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--proof-id", required=True)
    parser.add_argument("--claim-id", action="append", required=True)
    parser.add_argument("--source", action="append", required=True)
    parser.add_argument("--manifest-file", action="append", default=[])
    parser.add_argument("--scope", required=True)
    parser.add_argument("--non-goal", action="append", default=[])
    args = parser.parse_args()

    if "-CG001-" not in args.run_id:
        raise SystemExit("RUN_NOT_OWNED_BY_CG001")
    run_dir = ROOT / "HoTT/verification/runs" / args.run_id
    if run_dir.exists():
        raise SystemExit(f"RUN_ALREADY_EXISTS:{args.run_id}")

    toolchain = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    binary = Path(toolchain["pinned_cache"]["binary"])
    asset = Path(toolchain["pinned_cache"]["directory"]) / toolchain["release"]["asset"]
    binary_data = binary.read_bytes()
    asset_data = asset.read_bytes()
    if sha(binary_data) != toolchain["pinned_cache"]["binary_sha256"]:
        raise SystemExit("RZK_BINARY_HASH_MISMATCH")
    if sha(asset_data) != toolchain["release"]["publisher_digest"]:
        raise SystemExit("RZK_ASSET_DIGEST_MISMATCH")

    sources = [safe_relative(s) for s in args.source]
    for relative in sources:
        text = (ROOT / relative).read_text(encoding="utf-8")
        if not text.startswith("#lang rzk-1"):
            raise SystemExit(f"RZK_LANG_PRAGMA_REQUIRED:{relative}")
        for marker in FORBIDDEN:
            if marker in text:
                raise SystemExit(f"RZK_FORBIDDEN_MARKER:{relative}:{marker}")
    extra = [safe_relative(s) for s in args.manifest_file] + [TOOLCHAIN]

    version = subprocess.run([str(binary), "version"], capture_output=True, check=True).stdout.decode().strip()
    argv = [str(binary), "typecheck", *[s.as_posix() for s in sources]]

    run_dir.mkdir(parents=True)
    started = datetime.now(timezone.utc)
    t0 = time.monotonic()
    result = subprocess.run(argv, cwd=ROOT, capture_output=True, check=False)
    duration = time.monotonic() - t0
    completed = datetime.now(timezone.utc)

    env_text = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        f"rzk_executable={binary}",
        f"rzk_version={version}",
        "theory_variant=Riehl-Shulman simplicial type theory as implemented by Rzk; no #postulate, no #assume, no modalities in sources",
        "dependency_policy=official release asset pinned by publisher SHA-256 plus extracted binary hash",
        "secret_policy=no credentials, signed redirects, cookies or full environment dump retained",
    ]) + "\n"

    manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": args.proof_id,
        "run_id": args.run_id,
        "files": [file_row(p) for p in [*sources, *extra]],
        "external_dependencies": [
            {"label": "rzk-release-asset", "local_path": str(asset), "bytes": len(asset_data),
             "sha256": sha(asset_data), "publisher_digest": toolchain["release"]["publisher_digest"],
             "url": toolchain["release"]["url"]},
            {"label": "rzk-binary", "local_path": str(binary), "bytes": len(binary_data), "sha256": sha(binary_data)},
        ],
    }

    accepted = result.returncode == 0
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": args.run_id,
        "proof_id": args.proof_id,
        "claim_ids": args.claim_id,
        "proof_assistant": "Rzk",
        "proof_assistant_version": version,
        "theory_variant": "sHoTT (Riehl-Shulman simplicial type theory) as implemented by Rzk",
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": round(duration, 6),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED",
        "scope": args.scope,
        "non_goals": args.non_goal,
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "stdout": artifact(run_dir, "stdout.txt", result.stdout),
        "stderr": artifact(run_dir, "stderr.txt", result.stderr),
        "environment": artifact(run_dir, "environment.txt", env_text.encode("utf-8")),
        "source_manifest": artifact(run_dir, "source-manifest.json", json_bytes(manifest)),
    }
    (run_dir / "RUN.json").write_bytes(json_bytes(run))
    print(json.dumps({"status": run["status"], "run_path": f"HoTT/verification/runs/{args.run_id}",
                      "exit_code": result.returncode, "stdout_bytes": len(result.stdout),
                      "stderr_bytes": len(result.stderr), "source_files": len(manifest["files"])}))
    return 0 if accepted else 42


if __name__ == "__main__":
    raise SystemExit(main())
