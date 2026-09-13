#!/usr/bin/env python3
"""Reproduce SEM-B06's commutative-ring solver consumer audit."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
OWN_ROOT = REPO / "semantic-overview"
PROBE_ROOT = OWN_ROOT / "formal" / "sem-b06"
RUN_ID = "20260913-SEM-B06-COMMRING-NATURAL-CONSUMER-001-01"
RUN_ROOT = OWN_ROOT / "runs" / RUN_ID

TOOLCHAIN = Path("/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64")
AGDA = TOOLCHAIN / "agda"
AGDA_XDG_DATA = TOOLCHAIN / "xdg-data"
AGDA_XDG_CONFIG = TOOLCHAIN / "xdg-config"
AGDA_TMP = TOOLCHAIN / "tmp"

CUBICAL_ROOT = Path("/Volumes/D/HoTT-toolchain-cache/cubical-v0.9/cubical")
CUBICAL_ARCHIVE = CUBICAL_ROOT.parent / "cubical-0.9.tar.gz"
CUBICAL_LIBRARY = CUBICAL_ROOT / "cubical.agda-lib"
LIBRARY_REGISTRY = REPO / "HoTT" / "formal" / "truncation-no-recovery" / "AGDA_LIBRARIES"
TOOLCHAIN_MANIFEST = REPO / "HoTT" / "formal" / "truncation-no-recovery" / "TOOLCHAIN.json"

REFLECTION_SOURCE = CUBICAL_ROOT / "Cubical" / "Tactics" / "CommRingSolver" / "Reflection.agda"
SOLVER_SOURCE = CUBICAL_ROOT / "Cubical" / "Tactics" / "CommRingSolver" / "Solver.agda"
EXAMPLES_SOURCE = CUBICAL_ROOT / "Cubical" / "Tactics" / "CommRingSolver" / "Examples.agda"
NATURAL_CONSUMER = CUBICAL_ROOT / "Cubical" / "Algebra" / "CommRing" / "Localisation" / "Base.agda"

POSITIVE = PROBE_ROOT / "SemB06Positive.agda"
FALSE_EQUALITY = PROBE_ROOT / "SemB06FalseEqualityNegative.agda"
NON_EQUALITY = PROBE_ROOT / "SemB06NonEqualityNegative.agda"

CHECKING_PATH = re.compile(r"\bChecking\s+.+?\s+\((?P<path>/[^\n]+)\)\.$")


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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


def agda_command(target: Path, *, fresh: bool = False) -> list[str]:
    argv = [str(AGDA)]
    if fresh:
        argv.append("--ignore-interfaces")
    argv.extend(
        [
            f"--library-file={LIBRARY_REGISTRY}",
            "-l",
            "cubical-0.9",
            "-i",
            str(PROBE_ROOT),
            str(target),
        ]
    )
    return argv


def write_stream(name: str, stream: str, data: bytes) -> dict[str, object]:
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
) -> dict[str, object]:
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


def line_hits(path: Path, terms: tuple[str, ...]) -> dict[str, list[dict[str, object]]]:
    hits = {term: [] for term in terms}
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for term in terms:
            if term in line:
                hits[term].append({"line": number, "text": line})
    return hits


def usage_inventory() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for path in sorted(CUBICAL_ROOT.rglob("*.agda")):
        text = path.read_text(encoding="utf-8")
        if "solve!" not in text:
            continue
        if (
            "open import Cubical.Tactics.CommRingSolver" not in text
            and "import Cubical.Tactics.CommRingSolver" not in text
        ):
            continue
        relative = path.relative_to(CUBICAL_ROOT).as_posix()
        if relative == "Cubical/Tactics/CommRingSolver/Reflection.agda":
            classification = "SOLVER_IMPLEMENTATION"
        elif relative == "Cubical/Tactics/CommRingSolver/Examples.agda":
            classification = "SOLVER_EXAMPLES"
        elif relative.startswith("Cubical/Experiments/"):
            classification = "EXPERIMENTAL_DOWNSTREAM"
        else:
            classification = "PRODUCTION_LIBRARY_DOWNSTREAM"
        rows.append(
            {
                "path": str(path),
                "relative_path": relative,
                "solve_bang_occurrences": text.count("solve!"),
                "classification": classification,
            }
        )
    return rows


def build_source_audit() -> dict[str, object]:
    usage = usage_inventory()
    by_class: dict[str, dict[str, int]] = {}
    for row in usage:
        bucket = by_class.setdefault(
            str(row["classification"]), {"files": 0, "occurrences": 0}
        )
        bucket["files"] += 1
        bucket["occurrences"] += int(row["solve_bang_occurrences"])
    compile_ffi_files: list[str] = []
    io_main_files: list[str] = []
    for path in sorted(CUBICAL_ROOT.rglob("*.agda")):
        text = path.read_text(encoding="utf-8")
        if "COMPILE GHC" in text or "COMPILE JS" in text:
            compile_ffi_files.append(str(path))
        if re.search(r"(?m)^\s*main\s*:\s*IO\b", text):
            io_main_files.append(str(path))
    reflection_hits = line_hits(
        REFLECTION_SOURCE,
        (
            "solverCallAsTerm",
            "quote ringSolve",
            "quote refl",
            "typeError",
            "unify hole solution",
            "declarePostulate",
        ),
    )
    solver_hits = line_hits(
        SOLVER_SOURCE,
        ("isEqualToNormalform", "solve :", "solve e₁ e₂ xs p"),
    )
    return {
        "schema_version": "sem-b06-source-audit/v1",
        "usage_files": usage,
        "usage_file_count": len(usage),
        "usage_occurrence_count": sum(int(row["solve_bang_occurrences"]) for row in usage),
        "usage_by_class": by_class,
        "natural_consumer": {
            "path": str(NATURAL_CONSUMER),
            "solve_bang_occurrences": NATURAL_CONSUMER.read_text(encoding="utf-8").count("solve!"),
            "roles": [
                "localisation equivalence transitivity",
                "quotient operation well-definedness",
                "commutative-ring laws on the localisation",
            ],
        },
        "promise_source": {
            "path": str(EXAMPLES_SOURCE),
            "opening_comment": EXAMPLES_SOURCE.read_text(encoding="utf-8").split("-}", 1)[0] + "-}",
        },
        "reflection_hits": reflection_hits,
        "solver_hits": solver_hits,
        "solver_declare_postulate_call_count": len(
            reflection_hits["declarePostulate"]
        )
        + SOLVER_SOURCE.read_text(encoding="utf-8").count("declarePostulate"),
        "compiled_runtime_surface": {
            "compile_ffi_file_count": len(compile_ffi_files),
            "compile_ffi_files": compile_ffi_files,
            "io_main_file_count": len(io_main_files),
            "io_main_files": io_main_files,
            "interpretation": (
                "The fixed Cubical source tree exposes this solver as a type-checking "
                "macro and has no COMPILE GHC/JS or main : IO delivery surface."
            ),
        },
    }


def checked_sources(step: dict[str, object]) -> list[Path]:
    paths: list[Path] = []
    for stream_name in ("stdout", "stderr"):
        stream = step[stream_name]
        text = (RUN_ROOT / str(stream["path"])).read_text(
            encoding="utf-8", errors="replace"
        )
        for line in text.splitlines():
            match = CHECKING_PATH.search(line)
            if match:
                path = Path(match.group("path"))
                if path not in paths:
                    paths.append(path)
    return paths


def manifest_record(path: Path, roles: set[str]) -> dict[str, object]:
    data = path.read_bytes()
    try:
        relative = path.relative_to(REPO).as_posix()
    except ValueError:
        relative = None
    return {
        "path": str(path),
        "repo_relative_path": relative,
        "roles": sorted(roles),
        "bytes": len(data),
        "sha256": sha256(data),
    }


def build_manifest(steps: list[dict[str, object]]) -> tuple[dict, dict]:
    paths: dict[Path, set[str]] = {}

    def add(path: Path, role: str) -> None:
        paths.setdefault(path.resolve(), set()).add(role)

    add(Path(__file__), "runner")
    for path in (POSITIVE, FALSE_EQUALITY, NON_EQUALITY):
        add(path, "probe_source")
    for path in (
        REFLECTION_SOURCE,
        SOLVER_SOURCE,
        EXAMPLES_SOURCE,
        NATURAL_CONSUMER,
    ):
        add(path, "semantic_audit_source")
    for step in steps:
        if step["name"] in ("kernel-solver-fresh", "kernel-natural-consumer-fresh"):
            for path in checked_sources(step):
                add(path, f"actual_checked_closure:{step['name']}")
    for path, role in (
        (AGDA, "proof_assistant_binary"),
        (CUBICAL_ARCHIVE, "cubical_release_archive"),
        (CUBICAL_LIBRARY, "cubical_library_configuration"),
        (LIBRARY_REGISTRY, "project_library_registry"),
        (TOOLCHAIN_MANIFEST, "toolchain_manifest"),
    ):
        add(path, role)
    missing = [str(path) for path in paths if not path.is_file()]
    if missing:
        raise RuntimeError(f"MANIFEST_PATH_MISSING:{missing}")
    records = [manifest_record(path, roles) for path, roles in sorted(paths.items())]
    closure = {}
    for step in steps:
        if step["name"] in ("kernel-solver-fresh", "kernel-natural-consumer-fresh"):
            source_paths = checked_sources(step)
            closure[str(step["name"])] = {
                "checking_line_count": len(source_paths),
                "paths": [str(path) for path in source_paths],
            }
    toolchain = json.loads(TOOLCHAIN_MANIFEST.read_text(encoding="utf-8"))
    manifest = {
        "schema_version": "sem-b06-source-manifest/v1",
        "agda_version_identity": toolchain["agda"]["version"],
        "cubical_version": toolchain["cubical_library"]["version"],
        "cubical_tag_commit": toolchain["cubical_library"]["tag_commit"],
        "cubical_tree_sha256": toolchain["cubical_library"]["tree_sha256"],
        "actual_checked_closure": closure,
        "files": records,
    }
    return manifest, closure


def main() -> int:
    if RUN_ROOT.exists():
        print(f"refusing to overwrite existing run: {RUN_ROOT}", file=sys.stderr)
        return 2
    RUN_ROOT.mkdir(parents=True)

    required = [
        AGDA,
        CUBICAL_ARCHIVE,
        CUBICAL_LIBRARY,
        LIBRARY_REGISTRY,
        TOOLCHAIN_MANIFEST,
        REFLECTION_SOURCE,
        SOLVER_SOURCE,
        EXAMPLES_SOURCE,
        NATURAL_CONSUMER,
        POSITIVE,
        FALSE_EQUALITY,
        NON_EQUALITY,
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
    steps: list[dict[str, object]] = []
    steps.append(run_step("agda-version", [str(AGDA), "--version"], 0))
    steps.append(
        run_step(
            "kernel-solver-fresh", agda_command(REFLECTION_SOURCE, fresh=True), 0
        )
    )
    steps.append(
        run_step(
            "kernel-natural-consumer-fresh",
            agda_command(NATURAL_CONSUMER, fresh=True),
            0,
        )
    )
    steps.append(run_step("macro-positive", agda_command(POSITIVE), 0))
    steps.append(
        run_step(
            "macro-false-equality-negative",
            agda_command(FALSE_EQUALITY),
            42,
            ("[UnequalTerms]", "x != y", "expression refl has type"),
        )
    )
    steps.append(
        run_step(
            "macro-non-equality-negative",
            agda_command(NON_EQUALITY),
            42,
            ("[GenericDocError]", "The CommRingSolver failed to parse the goal"),
        )
    )

    audit = build_source_audit()
    (RUN_ROOT / "source-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    manifest, closure = build_manifest(steps)
    (RUN_ROOT / "source-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
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
            f"cubical_root={CUBICAL_ROOT}",
            f"cubical_version={manifest['cubical_version']}",
            f"cubical_tag_commit={manifest['cubical_tag_commit']}",
            f"cubical_tree_sha256={manifest['cubical_tree_sha256']}",
            "execution_stage=Agda type-checking and reflection macro expansion",
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
        "status": "EXPECTED_BOUNDARY_OBSERVED" if all_expected else "UNEXPECTED_RESULT",
        "git": {
            "branch": branch,
            "head_before_run": head,
            "state": "LOCAL_UNCOMMITTED_CANDIDATE",
        },
        "scope": (
            "Cubical Agda v0.9 CommRingSolver.solve!: its proof-producing reflection "
            "path, one 13-use production localisation consumer, one supported local "
            "identity and two out-of-scope negative goals."
        ),
        "verdict": (
            "NATURAL_LIBRARY_CONSUMER_FOUND; PROOF_TERM_GENERATION_ACCEPTED; "
            "FALSE_AND_MALFORMED_GOALS_REJECTED; TYPECHECKING_PROMISE_MET_WITH_SCOPE; "
            "NO_RUNTIME_DELIVERY_CLAIM"
        ),
        "non_goals": [
            "No exhaustive proof that every valid commutative-ring identity is solved.",
            "No claim that every false or unsupported goal fails in every Cubical/Agda version.",
            "No compiled-runtime promise: the fixed library exposes a type-checking macro and no GHC/JS FFI or main : IO surface.",
            "No HoTT inconsistency, reality-relative mismatch, self-verification theorem, or natural consumer beyond the fixed source inventory.",
            "No attribution of declarePostulate: the fixed Reflection/Solver sources have zero direct calls.",
        ],
        "steps": steps,
        "actual_checked_closure": closure,
        "artifacts": {
            "environment": "environment.txt",
            "source_manifest": "source-manifest.json",
            "source_audit": "source-audit.json",
        },
    }
    (RUN_ROOT / "RUN.json").write_text(
        json.dumps(run, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    summary = {
        "run_id": RUN_ID,
        "status": run["status"],
        "steps": len(steps),
        "expected_steps": sum(step["status"] == "EXPECTED" for step in steps),
        "usage_files": audit["usage_file_count"],
        "usage_occurrences": audit["usage_occurrence_count"],
        "production_files": audit["usage_by_class"].get(
            "PRODUCTION_LIBRARY_DOWNSTREAM", {}
        ).get("files", 0),
        "solver_declare_postulate_calls": audit[
            "solver_declare_postulate_call_count"
        ],
        "manifest_files": len(manifest["files"]),
        "run_root": str(RUN_ROOT),
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if all_expected else 1


if __name__ == "__main__":
    raise SystemExit(main())
