#!/usr/bin/env python3
"""Reproduce SEM-B05's controlled reflection/postulate boundary checks."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
OWN_ROOT = REPO / "semantic-overview"
PROBE_ROOT = OWN_ROOT / "formal" / "sem-b05"
RUN_ID = "20260913-SEM-B05-REFLECTION-POSTULATE-SAFE-001-01"
RUN_ROOT = OWN_ROOT / "runs" / RUN_ID

TOOLCHAIN = Path("/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64")
AGDA = TOOLCHAIN / "agda"
AGDA_XDG_DATA = TOOLCHAIN / "xdg-data"
AGDA_XDG_CONFIG = TOOLCHAIN / "xdg-config"
AGDA_TMP = TOOLCHAIN / "tmp"
PRIM_ROOT = AGDA_XDG_DATA / "agda" / "2.8.0-3d04bac" / "lib" / "prim"

UNIMATH_ROOT = Path("/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d")
SOLVER_SOURCE = UNIMATH_ROOT / "src" / "reflection" / "precategory-solver.lagda.md"
TC_WRAPPER_SOURCE = (
    UNIMATH_ROOT / "src" / "reflection" / "type-checking-monad.lagda.md"
)
TOOLCHAIN_MANIFEST = REPO / "HoTT" / "formal" / "agda-unimath" / "UNIMATH_TOOLCHAIN.json"

UNSAFE = PROBE_ROOT / "SemB05Unsafe.agda"
SAFE = PROBE_ROOT / "SemB05Safe.agda"
SAFE_POSITIVE = PROBE_ROOT / "SemB05SafeReflectionPositive.agda"
NO_AXIOM_NEGATIVE = PROBE_ROOT / "SemB05NoAxiomNegative.agda"

BUILTIN_SOURCES = [
    PRIM_ROOT / "Agda" / "Builtin" / "Reflection.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "Bool.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "Equality.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "Unit.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "List.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "Nat.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "Word.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "String.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "Char.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "Float.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "Int.agda",
    PRIM_ROOT / "Agda" / "Builtin" / "Sigma.agda",
    PRIM_ROOT / "Agda" / "Primitive.agda",
]


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_record(path: Path, kind: str) -> dict:
    data = path.read_bytes()
    try:
        relative = path.relative_to(REPO).as_posix()
    except ValueError:
        relative = None
    return {
        "kind": kind,
        "path": str(path),
        "repo_relative_path": relative,
        "bytes": len(data),
        "sha256": sha256(data),
    }


def environment() -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "XDG_DATA_HOME": str(AGDA_XDG_DATA),
            "XDG_CONFIG_HOME": str(AGDA_XDG_CONFIG),
            "TMPDIR": str(AGDA_TMP),
        }
    )
    return env


def agda_command(target: Path, *, safe: bool = False) -> list[str]:
    argv = [str(AGDA), "--ignore-interfaces"]
    if safe:
        argv.append("--safe")
    argv.extend(["-i", str(PROBE_ROOT), str(target)])
    return argv


def write_stream(name: str, stream: str, data: bytes) -> dict:
    path = RUN_ROOT / f"{name}.{stream}.txt"
    path.write_bytes(data)
    return {
        "path": path.relative_to(RUN_ROOT).as_posix(),
        "bytes": len(data),
        "sha256": sha256(data),
    }


def run_step(
    name: str,
    argv: list[str],
    expected_exit: int,
    markers: tuple[str, ...] = (),
) -> dict:
    started = now_utc()
    start = time.monotonic()
    process = subprocess.run(
        argv,
        cwd=REPO,
        env=environment(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    combined = (process.stdout + process.stderr).decode("utf-8", errors="replace")
    missing = [marker for marker in markers if marker not in combined]
    expected = process.returncode == expected_exit and not missing
    return {
        "name": name,
        "argv": argv,
        "cwd": str(REPO),
        "started_at_utc": started,
        "duration_seconds": round(time.monotonic() - start, 6),
        "exit_code": process.returncode,
        "expected_exit_code": expected_exit,
        "required_markers": list(markers),
        "missing_markers": missing,
        "status": "EXPECTED" if expected else "UNEXPECTED",
        "stdout": write_stream(name, "stdout", process.stdout),
        "stderr": write_stream(name, "stderr", process.stderr),
    }


def line_hits(path: Path, terms: tuple[str, ...]) -> dict[str, list[dict]]:
    hits = {term: [] for term in terms}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for term in terms:
            if term in line:
                hits[term].append({"line": number, "text": line})
    return hits


def normalized_control_body(path: Path) -> str:
    """Remove only the module name and safe option for a controlled source comparison."""
    kept = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("{-# OPTIONS --safe"):
            continue
        if line.startswith("module SemB05"):
            continue
        if line.startswith("-- Same controlled macro"):
            continue
        if line.startswith("-- Controlled capability probe"):
            continue
        if line.startswith("-- postulate at the goal"):
            continue
        kept.append(line)
    return "\n".join(kept).strip() + "\n"


def build_source_audit() -> dict:
    unsafe_body = normalized_control_body(UNSAFE)
    safe_body = normalized_control_body(SAFE)
    return {
        "schema_version": "sem-b05-source-audit/v1",
        "probe_hits": {
            path.name: line_hits(
                path,
                (
                    "declarePostulate",
                    "inferType",
                    "freshName",
                    "unify",
                    "--safe",
                    "true ≡ false",
                    "true ≡ true",
                ),
            )
            for path in (UNSAFE, SAFE, SAFE_POSITIVE, NO_AXIOM_NEGATIVE)
        },
        "unsafe_safe_normalized_body_equal": unsafe_body == safe_body,
        "unsafe_normalized_body_sha256": sha256(unsafe_body.encode("utf-8")),
        "safe_normalized_body_sha256": sha256(safe_body.encode("utf-8")),
        "builtin_reflection_hits": line_hits(
            BUILTIN_SOURCES[0],
            (
                "declarePostulate :",
                "AGDATCMDECLAREPOSTULATE",
                "COMPILE JS declarePostulate",
                "unify            :",
                "AGDATCMUNIFY",
            ),
        ),
        "agda_unimath_wrapper_hits": line_hits(
            TC_WRAPPER_SOURCE,
            ("declare-postulate :", "AGDATCMDECLAREPOSTULATE"),
        ),
        "b04_solver_declare_postulate_call_count": len(
            line_hits(SOLVER_SOURCE, ("declare-postulate",))["declare-postulate"]
        ),
        "scope_interpretation": (
            "The unsafe and source-safe probes contain the same normalized macro body. "
            "Default mode accepts the explicit declarePostulate extension; safe mode "
            "rejects that exact operation. A separate safe reflection macro using only "
            "refl is accepted, so the observed rejection is not a blanket rejection of "
            "reflection. Without the explicit axiom, true equals false is rejected."
        ),
    }


def main() -> int:
    if RUN_ROOT.exists():
        print(f"refusing to overwrite existing run: {RUN_ROOT}", file=sys.stderr)
        return 2
    RUN_ROOT.mkdir(parents=True)

    probes = [UNSAFE, SAFE, SAFE_POSITIVE, NO_AXIOM_NEGATIVE]
    required = [
        AGDA,
        TOOLCHAIN_MANIFEST,
        SOLVER_SOURCE,
        TC_WRAPPER_SOURCE,
        *probes,
        *BUILTIN_SOURCES,
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        (RUN_ROOT / "PRECONDITION_FAILURE.json").write_text(
            json.dumps({"missing": missing}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return 2

    started_at = now_utc()
    start = time.monotonic()
    steps: list[dict] = []
    steps.append(run_step("agda-version", [str(AGDA), "--version"], 0))
    steps.append(run_step("explicit-postulate-default", agda_command(UNSAFE), 0))
    steps.append(
        run_step(
            "same-source-cli-safe-negative",
            agda_command(UNSAFE, safe=True),
            42,
            (
                "[SafeFlagPostulate]",
                "Cannot postulate SemB05Unsafe.sem-b05-declared-axiom with safe flag",
            ),
        )
    )
    steps.append(
        run_step(
            "source-safe-postulate-negative",
            agda_command(SAFE),
            42,
            (
                "[SafeFlagPostulate]",
                "Cannot postulate SemB05Safe.sem-b05-declared-axiom with safe flag",
            ),
        )
    )
    steps.append(run_step("safe-reflection-positive", agda_command(SAFE_POSITIVE), 0))
    steps.append(
        run_step(
            "no-axiom-false-equality-negative",
            agda_command(NO_AXIOM_NEGATIVE),
            42,
            ("[UnequalTerms]", "true != false", "refl has type true ≡ false"),
        )
    )

    audit = build_source_audit()
    (RUN_ROOT / "source-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    toolchain = json.loads(TOOLCHAIN_MANIFEST.read_text(encoding="utf-8"))
    manifest_files = [
        file_record(Path(__file__).resolve(), "runner"),
        *[file_record(path, "probe_source") for path in probes],
        *[file_record(path, "agda_primitive_source") for path in BUILTIN_SOURCES],
        file_record(TC_WRAPPER_SOURCE, "comparative_external_source"),
        file_record(SOLVER_SOURCE, "comparative_external_source"),
        file_record(TOOLCHAIN_MANIFEST, "toolchain_manifest"),
        file_record(AGDA, "proof_assistant_binary"),
    ]
    manifest = {
        "schema_version": "sem-b05-source-manifest/v1",
        "agda_version_identity": "2.8.0-3d04bac",
        "agda_primitive_root": str(PRIM_ROOT),
        "agda_unimath_commit": toolchain["agda_unimath_library"]["commit_sha"],
        "agda_unimath_tree_sha256": toolchain["agda_unimath_library"]["tree_sha256"],
        "files": manifest_files,
    }
    (RUN_ROOT / "source-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    version = (RUN_ROOT / "agda-version.stdout.txt").read_text(
        encoding="utf-8"
    ).strip().replace("\n", " | ")
    environment_text = "\n".join(
        (
            f"platform={platform.platform()}",
            f"python={platform.python_version()}",
            f"agda_executable={AGDA}",
            f"agda_version={version}",
            f"agda_primitive_root={PRIM_ROOT}",
            f"agda_unimath_comparative_source_commit={manifest['agda_unimath_commit']}",
            "execution_stage=Agda type-checking and reflection macro expansion",
            "safe_boundary=default mode versus --safe and source OPTIONS --safe",
            "secret_policy=no full environment, credentials, cookies, or signed URLs retained",
        )
    ) + "\n"
    (RUN_ROOT / "environment.txt").write_text(environment_text, encoding="utf-8")

    all_expected = all(step["status"] == "EXPECTED" for step in steps)
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.strip()
    branch = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=REPO,
        text=True,
        stdout=subprocess.PIPE,
        check=True,
    ).stdout.strip()
    run = {
        "schema_version": "semantic-overview-run/v1",
        "run_id": RUN_ID,
        "started_at_utc": started_at,
        "completed_at_utc": now_utc(),
        "duration_seconds": round(time.monotonic() - start, 6),
        "status": (
            "EXPECTED_BOUNDARY_OBSERVED" if all_expected else "UNEXPECTED_RESULT"
        ),
        "git": {
            "branch": branch,
            "head_before_run": head,
            "state": "LOCAL_UNCOMMITTED_CANDIDATE",
        },
        "scope": (
            "A controlled Agda 2.8 reflection macro that explicitly declares a fresh "
            "postulate at the goal type, checked in default and safe modes, with a "
            "safe ordinary-reflection positive control and a no-axiom false-equality "
            "negative control."
        ),
        "verdict": (
            "EXPLICIT_REFLECTION_POSTULATE_EXTENDS_THEORY_IN_DEFAULT_MODE; "
            "SAFE_MODE_REJECTS_THE_POSTULATE; SAFE_ORDINARY_REFLECTION_ACCEPTED; "
            "NO_KERNEL_INCONSISTENCY_CLAIM; CONTROLLED_CAPABILITY_BOUNDARY_OBSERVED"
        ),
        "non_goals": [
            "No claim that the default theory proves true equals false without an added axiom.",
            "No claim that the Agda kernel is inconsistent or that safe mode proves kernel soundness.",
            "No attribution of declarePostulate use to solve-Precategory!, whose fixed source has zero direct calls.",
            "No audit of every reflection primitive, compiler implementation path, or Agda version.",
            "No executable-runtime or real-world delivery claim; all observations occur during type checking.",
        ],
        "steps": steps,
        "artifacts": {
            "environment": "environment.txt",
            "source_manifest": "source-manifest.json",
            "source_audit": "source-audit.json",
        },
    }
    (RUN_ROOT / "RUN.json").write_text(
        json.dumps(run, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    summary = {
        "run_id": RUN_ID,
        "status": run["status"],
        "steps": len(steps),
        "expected_steps": sum(step["status"] == "EXPECTED" for step in steps),
        "unsafe_safe_normalized_body_equal": audit[
            "unsafe_safe_normalized_body_equal"
        ],
        "b04_solver_declare_postulate_calls": audit[
            "b04_solver_declare_postulate_call_count"
        ],
        "run_root": str(RUN_ROOT),
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if all_expected else 1


if __name__ == "__main__":
    raise SystemExit(main())
