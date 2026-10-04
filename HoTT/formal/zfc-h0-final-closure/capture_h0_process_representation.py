#!/usr/bin/env python3
"""Capture C-366 against a pinned external Foundation Lean source tree.

The command checks the project-local theorem source through the frozen
Foundation Lake environment.  It deliberately records the Foundation source
tree and lock inputs as external proof dependencies; it does not copy or edit
the external checkout.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import platform
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path("HoTT/formal/zfc-h0-final-closure")
SOURCE = PACKAGE / "H0ProcessRepresentation.lean"
NEGATIVE = PACKAGE / "WrongH0ProcessRepresentation.lean"
CLAIM = PACKAGE / "H0ProcessRepresentation-CLAIM.md"
TOOLCHAIN = PACKAGE / "H0ProcessRepresentation-TOOLCHAIN.json"
README = PACKAGE / "README.md"
DEFAULT_EXTERNAL_ROOT = Path("/tmp/foundation-zfc-f3972f4204fc")


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode()


def relative_row(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(data), "sha256": sha(data)}


def external_file_row(path: Path, label: str) -> dict[str, object]:
    data = path.read_bytes()
    return {"label": label, "local_path": str(path), "bytes": len(data), "sha256": sha(data)}


def deterministic_tree(root: Path) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    total = 0
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.is_symlink() and path.suffix != ".agdai" and path.name != ".DS_Store":
            data = path.read_bytes()
            row = {"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": sha(data)}
            rows.append(row)
            total += len(data)
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {"file_count": len(rows), "total_bytes": total, "tree_sha256": digest.hexdigest()}


def write_new(path: Path, data: bytes) -> None:
    if path.exists():
        raise RuntimeError(f"REFUSE_OVERWRITE:{path}")
    path.write_bytes(data)


def project_file(root: Path, name: str, expected_sha: str) -> Path:
    path = root / name
    if not path.is_file() or path.is_symlink() or sha(path.read_bytes()) != expected_sha:
        raise SystemExit(f"FOUNDATION_PROJECT_INPUT_MISMATCH:{name}")
    return path


def main() -> None:
    negative = "--negative" in sys.argv[1:]
    prefix = "20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-NEG-001-" if negative else "20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-001-"
    run_id = next((arg for arg in sys.argv[1:] if not arg.startswith("--")), f"{prefix}01")
    if "/" in run_id or not run_id.startswith(prefix):
        raise SystemExit("RUN_ID_INVALID")

    source = NEGATIVE if negative else SOURCE
    # C-366's proof input is the exact Lean source, its negative control,
    # package-local claim scope, toolchain declaration, and this capture
    # procedure.  The package README and the evolving total SOP route to this
    # package but are not elaborator inputs; pinning either here would make an
    # unrelated route update falsely look like theorem-source drift.
    inputs = [ROOT / path for path in (SOURCE, NEGATIVE, CLAIM, TOOLCHAIN, Path(__file__).relative_to(ROOT))]
    if any(not path.is_file() for path in inputs):
        raise SystemExit("REQUIRED_INPUT_MISSING")
    spec = json.loads((ROOT / TOOLCHAIN).read_text(encoding="utf-8"))
    external_root = Path(os.environ.get("FOUNDATION_LEAN_ROOT", str(DEFAULT_EXTERNAL_ROOT))).resolve()
    if not external_root.is_dir() or external_root.is_symlink():
        raise SystemExit("FOUNDATION_ROOT_INVALID")
    expected_commit = spec["external_project"]["commit"]
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=external_root, text=True).strip()
    if commit != expected_commit:
        raise SystemExit("FOUNDATION_COMMIT_MISMATCH")
    if subprocess.check_output(["git", "status", "--porcelain=v1"], cwd=external_root, text=True).strip():
        raise SystemExit("FOUNDATION_WORKTREE_NOT_CLEAN")
    files = spec["external_project"]["required_project_files"]
    lakefile = project_file(external_root, "lakefile.toml", files["lakefile.toml_sha256"])
    manifest = project_file(external_root, "lake-manifest.json", files["lake_manifest_sha256"])
    lean_toolchain = project_file(external_root, "lean-toolchain", files["lean_toolchain_sha256"])
    foundation_tree = external_root / spec["external_project"]["source_tree_subpath"]
    if not foundation_tree.is_dir() or foundation_tree.is_symlink():
        raise SystemExit("FOUNDATION_SOURCE_TREE_INVALID")
    # The `elan` launchers are stable dispatch binaries.  Resolving the
    # project-local `lean-toolchain` through `elan which` prevents a login
    # shell from silently selecting the user's global default toolchain.
    elan = Path(subprocess.check_output(["bash", "-c", "command -v elan"], cwd=external_root, text=True).strip())
    if not elan.is_file():
        raise SystemExit("ELAN_BINARY_MISSING")
    lake = Path(subprocess.check_output([str(elan), "which", "lake"], cwd=external_root, text=True).strip()).resolve()
    lean = Path(subprocess.check_output([str(elan), "which", "lean"], cwd=external_root, text=True).strip()).resolve()
    if not lake.is_file() or not lean.is_file():
        raise SystemExit("LEAN_TOOLCHAIN_BINARY_MISSING")

    run = ROOT / "HoTT/verification/runs" / run_id
    if run.exists():
        raise SystemExit("RUN_ALREADY_EXISTS")
    # `--dir` selects the frozen external Lake package while retaining this
    # repository as cwd.  The actual command therefore names the canonical
    # project-relative proof source, which lets the evidence registry bind the
    # checked input rather than an environment-specific absolute locator.
    argv = [str(lake), "--dir", str(external_root), "env", str(lean), str(source)]
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(argv, cwd=ROOT, capture_output=True)
    completed = dt.datetime.now(dt.timezone.utc)
    version = subprocess.check_output([str(lean), "--version"], text=True).strip()
    accepted = result.returncode == 0
    negative_ok = negative and result.returncode != 0 and b"value \xe2\x89\xa0 value" in result.stdout
    proof_id = "MP-ZFC-H0-PROCESS-REPRESENTATION-NEG-001" if negative else "MP-ZFC-H0-PROCESS-REPRESENTATION-001"
    claim_ids = ["C-366 (negative control)"] if negative else ["C-366"]
    external_dependencies = [
        {"label": "foundation-lean-zf-source-tree", "local_path": str(foundation_tree), **deterministic_tree(foundation_tree), "git_commit": commit},
        external_file_row(lakefile, "foundation-lean-zf-lakefile"),
        external_file_row(manifest, "foundation-lean-zf-manifest"),
        external_file_row(lean_toolchain, "foundation-lean-zf-toolchain-file"),
        external_file_row(lean, "lean-4.34.0-binary"),
        external_file_row(lake, "lake-4.34.0-binary"),
    ]
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": proof_id,
        "run_id": run_id,
        "files": [relative_row(path) for path in inputs],
        "external_dependencies": external_dependencies,
        "scope": "Pinned Foundation Lean Zermelo-model sequence representability control; no bare-ZFC completion-policy or H0 semantic-map conclusion.",
    }
    receipt: dict[str, object] = {
        "schema_version": "formal-proof-run/v1",
        "run_id": run_id,
        "proof_id": proof_id,
        "claim_ids": claim_ids,
        "proof_assistant": "Lean",
        "proof_assistant_detail": "Lean 4 via Foundation Lake project",
        "proof_assistant_version": version,
        "theory_variant": spec["theory_variant"],
        "command_argv": argv,
        "cwd": str(ROOT),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": "NEGATIVE_CONTROL_REJECTED" if negative_ok else ("KERNEL_ACCEPTED_WITH_SCOPE" if accepted else "KERNEL_REJECTED"),
        "scope": "C-366 checks an external-source-backed Zermelo-model representation of ordinal-indexed sequence graphs. It is a positive control for representability, not a proof that bare ZFC pays a completion bridge or has/does not have Q.",
        "non_goals": [
            "Does not prove a ZFC object-language theorem, a ZFC consistency statement, or a complete ZFC semantics.",
            "Does not construct an H0Map or interpret fixed Cubical Agda H0 in this set-theoretic model.",
            "Does not establish C_accept, AdequacyLift, SameFullQ, P/A/B attribution, or a bare-ZFC precision defect.",
        ],
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run.mkdir(parents=True)
    for key, name, data in (
        ("stdout", "stdout.txt", result.stdout),
        ("stderr", "stderr.txt", result.stderr),
        ("environment", "environment.txt", (f"platform={platform.platform()}\nexternal_root={external_root}\nexternal_commit={commit}\nlake={lake}\nlean={lean}\n").encode()),
        ("source_manifest", "source-manifest.json", json_bytes(source_manifest)),
    ):
        write_new(run / name, data)
        receipt[key] = {"path": name, "bytes": len(data), "sha256": sha(data)}
    write_new(run / "RUN.json", json_bytes(receipt))
    print(json.dumps({"status": receipt["status"], "run_id": run_id, "exit": result.returncode}, ensure_ascii=False))
    if negative:
        raise SystemExit(0 if negative_ok else 1)
    raise SystemExit(0 if accepted else 1)


if __name__ == "__main__":
    main()
