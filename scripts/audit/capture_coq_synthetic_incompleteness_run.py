#!/usr/bin/env python3
"""Capture the F-011 main replay of the CSL 2023 Coq R3 theorem package."""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUN_ID = "20260915-MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001-01"
PROOF_ID = "MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001"
CLAIM_IDS = ["C-244", "C-245", "C-246", "C-247", "C-248", "C-249"]
RUN_REL = Path("HoTT/verification/runs") / RUN_ID
RUN_DIR = ROOT / RUN_REL
PACKAGE = Path("HoTT/formal/external-coq-synthetic-incompleteness")
ARCHIVE = ROOT / PACKAGE / "upstream-cd7d849.tar.gz"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def file_row(relative: Path) -> dict[str, object]:
    path = ROOT / relative
    if not path.is_file() or path.is_symlink():
        raise RuntimeError(f"SOURCE_INVALID:{relative}")
    data = path.read_bytes()
    return {"path": relative.as_posix(), "bytes": len(data), "sha256": sha(data)}


def external_file(path: Path, label: str) -> dict[str, object]:
    data = path.read_bytes()
    return {"label": label, "local_path": str(path), "bytes": len(data), "sha256": sha(data)}


def exclusive_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("xb") as handle:
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())


def main() -> int:
    if not (ROOT / ".git").is_dir():
        raise SystemExit("PROJECT_GIT_ROOT_REQUIRED")
    if RUN_DIR.exists():
        raise SystemExit("RUN_DIRECTORY_ALREADY_EXISTS")
    toolchain = json.loads((ROOT / PACKAGE / "TOOLCHAIN.json").read_text(encoding="utf-8"))
    source_paths = [
        PACKAGE / "README.md",
        PACKAGE / "CLAIM-R3-SYNTHETIC-INCOMPLETENESS.md",
        PACKAGE / "SOURCE_TREE_MANIFEST.json",
        PACKAGE / "SOURCE_ARCHIVE.json",
        PACKAGE / "TOOLCHAIN.json",
        PACKAGE / "Qualification.v",
        PACKAGE / "Dockerfile",
        PACKAGE / "CeCILL_LICENSE.txt",
        PACKAGE / "IMPORT.json",
        Path("scripts/audit/import_coq_synthetic_incompleteness.py"),
        Path("scripts/audit/replay_coq_synthetic_incompleteness.py"),
        Path("scripts/audit/capture_coq_synthetic_incompleteness_run.py"),
        Path("scripts/audit/verify_formal_proof_run.py"),
        Path(".codex/research/hott/R3-R4-GODEL-RETURN-001.md"),
        Path("audit/imports/machine-overview-ce-map-20260915/source/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001/BUILD-RECEIPT.json"),
        Path("audit/imports/machine-overview-ce-map-20260915/source/evaluations/COQ-SYNTHETIC-INCOMPLETENESS-REPLAY-001/REPORT.md"),
    ]
    source_rows = [file_row(path) for path in source_paths]
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": PROOF_ID,
        "run_id": RUN_ID,
        "files": source_rows,
        "external_dependencies": [
            external_file(ARCHIVE, "coq-synthetic-incompleteness-source-archive")
        ],
    }
    source_manifest_data = json_bytes(source_manifest)
    command = ["/usr/bin/env", "python3", "-B", "scripts/audit/replay_coq_synthetic_incompleteness.py"]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(command, cwd=ROOT, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)
    environment = "\n".join(
        [
            f"platform={platform.platform()}",
            f"machine={platform.machine()}",
            f"python={platform.python_version()}",
            f"coq_image={toolchain['derived_image']['reference']}",
            f"coq_image_id={toolchain['derived_image']['id']}",
            "coq_version=8.15.2",
            "upstream=uds-psl/coq-synthetic-incompleteness csl@cd7d8490f8542bfe85658c465bcb26b2ed163f53",
            "replay=fresh repo-contained archive extraction; fol_incompleteness.vo build; qualification twice",
            "trust_scope=Coq kernel plus explicit theorem parameters and pinned source/image",
            "",
        ]
    ).encode()
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": RUN_ID,
        "proof_id": PROOF_ID,
        "claim_ids": CLAIM_IDS,
        "proof_assistant": "Coq",
        "proof_assistant_version": "8.15.2",
        "theory_variant": "Coq CIC replay of synthetic essential incompleteness and Robinson Q",
        "command_argv": command,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "KERNEL_ACCEPTED_WITH_SCOPE" if result.returncode == 0 else "KERNEL_REJECTED",
        "scope": (
            "Freshly build the exact CSL 2023 first-order incompleteness target and replay theorem signatures/assumptions for recursive-separation divergence, abstract essential incompleteness, EPF-mu-to-CTQ, and conditional Robinson-Q independence."
        ),
        "non_goals": [
            "The theorem types retain is_universal, strong separation, Peirce, CTQ, Q containment, enumerability, and consistency premises.",
            "The object theory is first-order arithmetic, not an exact HoTT calculus.",
            "The run does not establish HoTT essentiality, ambient Church thesis, internal inconsistency, novelty, or an empirical same-task reality bridge.",
            "A bounded or observed proof search is not used as evidence of independence; the kernel-checked conditional theorem is the evidence.",
        ],
        "stdout": {"path": "stdout.txt", "bytes": len(result.stdout), "sha256": sha(result.stdout)},
        "stderr": {"path": "stderr.txt", "bytes": len(result.stderr), "sha256": sha(result.stderr)},
        "environment": {"path": "environment.txt", "bytes": len(environment), "sha256": sha(environment)},
        "source_manifest": {"path": "source-manifest.json", "bytes": len(source_manifest_data), "sha256": sha(source_manifest_data)},
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    RUN_DIR.mkdir(parents=True, exist_ok=False)
    try:
        exclusive_write(RUN_DIR / "stdout.txt", result.stdout)
        exclusive_write(RUN_DIR / "stderr.txt", result.stderr)
        exclusive_write(RUN_DIR / "environment.txt", environment)
        exclusive_write(RUN_DIR / "source-manifest.json", source_manifest_data)
        exclusive_write(RUN_DIR / "RUN.json", json_bytes(run))
    except BaseException:
        print(f"PARTIAL_RUN_DIRECTORY_RETAINED:{RUN_REL.as_posix()}")
        raise
    print(
        json.dumps(
            {
                "status": run["status"],
                "run_path": RUN_REL.as_posix(),
                "exit_code": result.returncode,
                "duration_seconds": run["duration_seconds"],
                "stdout_bytes": len(result.stdout),
                "stderr_bytes": len(result.stderr),
                "source_files": len(source_rows),
                "external_dependencies": 1,
                "index_status": run["index_status"],
            },
            ensure_ascii=False,
        )
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
