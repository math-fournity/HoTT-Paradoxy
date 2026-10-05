#!/usr/bin/env python3
"""Capture an exact source replay for set.mm's object-level geometric series theorem.

This is source-execution evidence for C0B4, not a replacement for the
project's proof-package/claim-matrix gate and not a ZFC adequacy theorem.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "20261005-SOURCE-REPLAY-SETMM-GEO-LIMIT-001"
RUN_DIR = ROOT / "HoTT/verification/runs" / RUN_ID
DATABASE = Path("/Volumes/D/HoTT-downloads/godel-q-setmm-160ebb/set.mm")
VERIFIER = Path("/Volumes/D/HoTT-downloads/godel-q-setmm-160ebb/metamath-exe-current/src/metamath")
DATABASE_COMMIT = "160ebb63ec17ff00a809520a420c92914a424622"
DATABASE_SHA256 = "d8420798bcedcd04fcfe337736e2609b66914c76f8f2db967fa79673d5026b2a"
VERIFIER_SHA256 = "35351c6d9c1795604e3cfa8ef8359c5118c45b54ca415e61e54d2813512feb68"
SOURCE = Path("HoTT/verification/runs/20261004-SOURCE-REPLAY-SETMM-OBJECT-CODING-001/RUN.json")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def write_new(path: Path, data: bytes) -> None:
    with path.open("xb") as out:
        out.write(data)
        out.flush()
        os.fsync(out.fileno())


def source_locator(path: Path, label: str) -> dict[str, object]:
    text = path.read_text(encoding="utf-8")
    line = next((index + 1 for index, item in enumerate(text.splitlines()) if label in item), None)
    if line is None:
        raise RuntimeError(f"LABEL_MISSING:{label}")
    return {"label": label, "line": line}


def main() -> int:
    if RUN_DIR.exists():
        raise SystemExit("RUN_DIRECTORY_ALREADY_EXISTS")
    if not DATABASE.is_file() or not VERIFIER.is_file() or not (ROOT / SOURCE).is_file():
        raise SystemExit("REQUIRED_INPUT_MISSING")
    if sha(DATABASE.read_bytes()) != DATABASE_SHA256:
        raise SystemExit("DATABASE_HASH_MISMATCH")
    if sha(VERIFIER.read_bytes()) != VERIFIER_SHA256:
        raise SystemExit("VERIFIER_HASH_MISMATCH")

    input_text = (
        f'READ "{DATABASE}"\n'
        "VERIFY PROOF *\n"
        "SHOW TRACE_BACK geoihalfsum / AXIOMS\n"
        "S\n"
        "EXIT\n"
    )
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run([str(VERIFIER)], input=input_text.encode("utf-8"), cwd=ROOT, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)
    stdout = result.stdout.decode("utf-8", "replace")
    required = (
        "All proofs in the database were verified",
        'Statement "geoihalfsum" assumes the following axioms',
        "ax-rep",
        "ax-pow",
        "ax-inf2",
        "df-rlim",
        "df-sum",
    )
    missing = [item for item in required if item not in stdout]
    if result.returncode != 0 or missing:
        raise SystemExit(f"SOURCE_REPLAY_FAILED:{result.returncode}:{','.join(missing)}")

    inventory = {
        "schema_version": "setmm-geometric-source-inventory/v1",
        "database_commit": DATABASE_COMMIT,
        "database_sha256": DATABASE_SHA256,
        "labels": [
            source_locator(DATABASE, "df-rlim $a"),
            source_locator(DATABASE, "df-sum $a"),
            source_locator(DATABASE, "df-seq $a"),
            source_locator(DATABASE, "geoihalfsum $p"),
            source_locator(DATABASE, "ax-ac $a"),
        ],
        "trace_back_axiom_markers": ["ax-rep", "ax-pow", "ax-un", "ax-inf2"],
        "absence_control": "The trace output does not list ax-ac among the displayed all-axiom dependencies for geoihalfsum; this is a fixed-database trace fact, not a global theorem about alternate databases.",
    }
    manifest = {
        "schema_version": "source-replay-manifest/v1",
        "database": {
            "repository": "https://github.com/metamath/set.mm",
            "commit": DATABASE_COMMIT,
            "external_path": str(DATABASE),
            "bytes": DATABASE.stat().st_size,
            "sha256": DATABASE_SHA256,
        },
        "verifier": {
            "repository": "https://github.com/metamath/metamath-exe.git",
            "external_path": str(VERIFIER),
            "bytes": VERIFIER.stat().st_size,
            "sha256": VERIFIER_SHA256,
        },
        "project_inputs": [
            {"path": SOURCE.as_posix(), "bytes": (ROOT / SOURCE).stat().st_size, "sha256": sha((ROOT / SOURCE).read_bytes())},
            {"path": Path(__file__).relative_to(ROOT).as_posix(), "bytes": Path(__file__).stat().st_size, "sha256": sha(Path(__file__).read_bytes())},
        ],
    }
    environment = (
        f"platform={platform.platform()}\n"
        f"database_commit={DATABASE_COMMIT}\n"
        f"database_sha256={DATABASE_SHA256}\n"
        f"verifier_sha256={VERIFIER_SHA256}\n"
        "scope=exact external source and verifier replay; no bare-ZFC adequacy claim\n"
    ).encode("utf-8")
    receipt = {
        "schema_version": "source-replay-run/v1",
        "run_id": RUN_ID,
        "status": "EXACT_SETMM_GEOMETRIC_LIMIT_SOURCE_REPLAYED_WITH_SCOPE",
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "command_argv": [str(VERIFIER)],
        "stdin": input_text,
        "database": {"repository": "https://github.com/metamath/set.mm", "commit": DATABASE_COMMIT, "sha256": DATABASE_SHA256},
        "verification": {
            "exit_code": result.returncode,
            "full_database_proofs_verified": True,
            "target_theorem": "geoihalfsum",
            "target_formula": "sum_ k e. NN ( 1 / ( 2 ^ k ) ) = 1",
            "trace_back_axiom_markers": inventory["trace_back_axiom_markers"],
        },
        "scope": "Exact set.mm object-level geometric-series theorem and dependency trace. This is source-replay evidence for M→S, not an actual physical motion promotion, bridge, or bare-ZFC adequacy verdict.",
        "non_goals": [
            "Does not prove physical spacetime discreteness or invalidate standard real analysis.",
            "Does not show IEP or the mathematical community consumed set.mm to solve Zeno.",
            "Does not construct an internal ZFC model, prove bare ZFC consistency/inconsistency, or pay a completion bridge.",
        ],
    }
    RUN_DIR.mkdir(parents=True, exist_ok=False)
    try:
        write_new(RUN_DIR / "stdout.txt", result.stdout)
        write_new(RUN_DIR / "stderr.txt", result.stderr)
        write_new(RUN_DIR / "environment.txt", environment)
        write_new(RUN_DIR / "source-manifest.json", json_bytes(manifest))
        write_new(RUN_DIR / "source-inventory.json", json_bytes(inventory))
        for key, filename, data in (
            ("stdout", "stdout.txt", result.stdout),
            ("stderr", "stderr.txt", result.stderr),
            ("environment", "environment.txt", environment),
            ("source_manifest", "source-manifest.json", json_bytes(manifest)),
            ("source_inventory", "source-inventory.json", json_bytes(inventory)),
        ):
            receipt[key] = {"path": filename, "bytes": len(data), "sha256": sha(data)}
        write_new(RUN_DIR / "RUN.json", json_bytes(receipt))
    except BaseException:
        raise
    print(json.dumps({"status": receipt["status"], "run_id": RUN_ID, "exit_code": result.returncode}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
