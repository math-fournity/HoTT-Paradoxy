#!/usr/bin/env python3
"""Reproduce SEM-B04 precategory-reflection positive and negative checks."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
OWN_ROOT = REPO / "semantic-overview"
PROBE_ROOT = OWN_ROOT / "formal" / "sem-b04"
RUN_ID = "20260913-SEM-B04-PRECATEGORY-REFLECTION-001-01"
RUN_ROOT = OWN_ROOT / "runs" / RUN_ID

TOOLCHAIN = Path("/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64")
AGDA = TOOLCHAIN / "agda"
AGDA_XDG_DATA = TOOLCHAIN / "xdg-data"
AGDA_XDG_CONFIG = TOOLCHAIN / "xdg-config"
AGDA_TMP = TOOLCHAIN / "tmp"

UNIMATH_ROOT = Path("/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d")
UNIMATH_SRC = UNIMATH_ROOT / "src"
SOLVER_SOURCE = UNIMATH_SRC / "reflection" / "precategory-solver.lagda.md"
TC_SOURCE = UNIMATH_SRC / "reflection" / "type-checking-monad.lagda.md"
LIBRARY_REGISTRY = REPO / "HoTT" / "formal" / "agda-unimath" / "AGDA_LIBRARIES"
TOOLCHAIN_MANIFEST = REPO / "HoTT" / "formal" / "agda-unimath" / "UNIMATH_TOOLCHAIN.json"


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


def agda_command(target: Path) -> list[str]:
    return [
        str(AGDA),
        f"--library-file={LIBRARY_REGISTRY}",
        "-l",
        "agda-unimath",
        "-i",
        str(PROBE_ROOT),
        str(target),
    ]


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
    text = (process.stdout + process.stderr).decode("utf-8", errors="replace")
    missing = [marker for marker in markers if marker not in text]
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


def build_source_audit() -> dict:
    solver_terms = (
        "solves any equation",
        "solve-Precategory-Expression",
        "build-Precategory-Expression",
        "infer-type",
        "reduce",
        "normalize",
        "unify",
        "declare-postulate",
    )
    tc_terms = ("declare-postulate", "AGDATCMDECLAREPOSTULATE", "unify", "AGDATCMUNIFY")
    usage_files = []
    for path in sorted(UNIMATH_SRC.rglob("*.lagda.md")):
        if "solve-Precategory!" in path.read_text(encoding="utf-8"):
            usage_files.append(str(path))
    solver_hits = line_hits(SOLVER_SOURCE, solver_terms)
    return {
        "schema_version": "sem-b04-source-audit/v1",
        "solver_source": file_record(SOLVER_SOURCE, "source_audit_input"),
        "type_checker_source": file_record(TC_SOURCE, "source_audit_input"),
        "solver_hits": solver_hits,
        "type_checker_hits": line_hits(TC_SOURCE, tc_terms),
        "solver_declare_postulate_call_count": len(solver_hits["declare-postulate"]),
        "solve_precategory_usage_files": usage_files,
        "solve_precategory_usage_file_count": len(usage_files),
        "scope_interpretation": (
            "The reflection API exposes declare-postulate, but the fixed solver source does "
            "not call it. The solver builds a term using the soundness theorem and asks "
            "Agda's unifier to fill the goal. Exact-name uses are confined to the solver "
            "module's own examples in this fixed tree."
        ),
    }


def main() -> int:
    if RUN_ROOT.exists():
        print(f"refusing to overwrite existing run: {RUN_ROOT}", file=sys.stderr)
        return 2
    RUN_ROOT.mkdir(parents=True)

    probes = [
        PROBE_ROOT / "SemB04Positive.agda",
        PROBE_ROOT / "SemB04FalseEqualityNegative.agda",
        PROBE_ROOT / "SemB04NonEqualityNegative.agda",
    ]
    sources = [
        SOLVER_SOURCE,
        TC_SOURCE,
        UNIMATH_SRC / "reflection" / "terms.lagda.md",
        UNIMATH_SRC / "reflection" / "arguments.lagda.md",
        UNIMATH_SRC / "reflection" / "definitions.lagda.md",
        UNIMATH_SRC / "category-theory" / "precategories.lagda.md",
    ]
    required = [
        AGDA,
        LIBRARY_REGISTRY,
        TOOLCHAIN_MANIFEST,
        UNIMATH_ROOT / "agda-unimath.agda-lib",
        *probes,
        *sources,
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

    fresh = agda_command(SOLVER_SOURCE)
    fresh.insert(1, "--ignore-interfaces")
    steps.append(run_step("kernel-solver-fresh", fresh, 0))
    steps.append(run_step("macro-positive", agda_command(probes[0]), 0))
    steps.append(
        run_step(
            "macro-false-equality-negative",
            agda_command(probes[1]),
            42,
            ("[UnequalTerms]", "f != g", "refl has type"),
        )
    )
    steps.append(
        run_step(
            "macro-non-equality-negative",
            agda_command(probes[2]),
            42,
            ("[GenericDocError]", "is not a ＝-type"),
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
        *[file_record(path, "external_source") for path in sources],
        file_record(UNIMATH_ROOT / "agda-unimath.agda-lib", "library_configuration"),
        file_record(LIBRARY_REGISTRY, "library_registry"),
        file_record(TOOLCHAIN_MANIFEST, "toolchain_manifest"),
        file_record(AGDA, "proof_assistant_binary"),
    ]
    manifest = {
        "schema_version": "sem-b04-source-manifest/v1",
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
    env_text = "\n".join(
        (
            f"platform={platform.platform()}",
            f"python={platform.python_version()}",
            f"agda_executable={AGDA}",
            f"agda_version={version}",
            f"agda_unimath_root={UNIMATH_ROOT}",
            f"agda_unimath_commit={manifest['agda_unimath_commit']}",
            f"agda_unimath_tree_sha256={manifest['agda_unimath_tree_sha256']}",
            "execution_stage=Agda type-checking and reflection macro expansion",
            "secret_policy=no full environment, credentials, cookies, or signed URLs retained",
        )
    ) + "\n"
    (RUN_ROOT / "environment.txt").write_text(env_text, encoding="utf-8")

    all_expected = all(step["status"] == "EXPECTED" for step in steps)
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"], cwd=REPO, text=True,
        stdout=subprocess.PIPE, check=True
    ).stdout.strip()
    branch = subprocess.run(
        ["git", "branch", "--show-current"], cwd=REPO, text=True,
        stdout=subprocess.PIPE, check=True
    ).stdout.strip()
    run = {
        "schema_version": "semantic-overview-run/v1",
        "run_id": RUN_ID,
        "started_at_utc": started_at,
        "completed_at_utc": now_utc(),
        "duration_seconds": round(time.monotonic() - start, 6),
        "status": "EXPECTED_BOUNDARY_OBSERVED" if all_expected else "UNEXPECTED_RESULT",
        "git": {
            "branch": branch,
            "head_before_run": head,
            "state": "LOCAL_UNCOMMITTED_CANDIDATE",
        },
        "scope": (
            "The fixed agda-unimath solve-Precategory! reflection macro: fresh source "
            "checking, an associative equation it promises to solve, an arbitrary false "
            "morphism equality, and a non-equality goal."
        ),
        "verdict": (
            "REFLECTION_SOLVER_GENERATES_CHECKED_PROOF_TERM; "
            "FALSE_AND_MALFORMED_GOALS_REJECTED; DECLARE_POSTULATE_NOT_USED; "
            "DEFENSE_WORKS_WITH_SCOPE"
        ),
        "non_goals": [
            "No proof that every input or future solver version fails closed.",
            "No audit of Agda compiler implementation internals beyond observed behavior and fixed source bindings.",
            "No claim that reflection primitives are available as compiled runtime functions; the execution surface is type checking.",
            "No HoTT inconsistency, effective-delivery mismatch, or self-verification theorem.",
            "The fixed tree has no exact-name use outside the solver module's own examples."
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
        "solver_declare_postulate_calls": audit["solver_declare_postulate_call_count"],
        "usage_files": audit["solve_precategory_usage_file_count"],
        "run_root": str(RUN_ROOT),
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if all_expected else 1


if __name__ == "__main__":
    raise SystemExit(main())
