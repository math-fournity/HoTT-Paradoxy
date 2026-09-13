#!/usr/bin/env python3
"""Reproduce SEM-B02 finite-decision kernel and JS delivery probes."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
OWN_ROOT = REPO / "semantic-overview"
PROBE_ROOT = OWN_ROOT / "formal" / "sem-b02"
RUN_ID = "20260913-SEM-B02-FINITE-DECISION-001-01"
RUN_ROOT = OWN_ROOT / "runs" / RUN_ID

TOOLCHAIN = Path("/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64")
AGDA = TOOLCHAIN / "agda"
AGDA_XDG_DATA = TOOLCHAIN / "xdg-data"
AGDA_XDG_CONFIG = TOOLCHAIN / "xdg-config"
AGDA_TMP = TOOLCHAIN / "tmp"
AGDA_JS_RTS = AGDA_XDG_DATA / "agda" / "2.8.0-3d04bac" / "JS" / "agda-rts.js"
NODE = Path("/Users/aurolafly/.local/bin/node")

UNIMATH_ROOT = Path("/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d")
UNIMATH_SRC = UNIMATH_ROOT / "src"
LIBRARY_REGISTRY = REPO / "HoTT" / "formal" / "agda-unimath" / "AGDA_LIBRARIES"
TOOLCHAIN_MANIFEST = REPO / "HoTT" / "formal" / "agda-unimath" / "UNIMATH_TOOLCHAIN.json"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def digest(data: bytes) -> str:
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
        "sha256": digest(data),
    }


def write_output(name: str, stream: str, data: bytes) -> dict:
    path = RUN_ROOT / f"{name}.{stream}.txt"
    path.write_bytes(data)
    return {
        "path": path.relative_to(RUN_ROOT).as_posix(),
        "bytes": len(data),
        "sha256": digest(data),
    }


def command_env() -> dict[str, str]:
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


def run_step(
    name: str,
    argv: list[str],
    expected_exit: int,
    markers: tuple[str, ...] = (),
    env: dict[str, str] | None = None,
) -> dict:
    start_utc = utc_now()
    start = time.monotonic()
    process = subprocess.run(
        argv,
        cwd=REPO,
        env=env or command_env(),
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
        "started_at_utc": start_utc,
        "duration_seconds": round(time.monotonic() - start, 6),
        "exit_code": process.returncode,
        "expected_exit_code": expected_exit,
        "required_markers": list(markers),
        "missing_markers": missing,
        "status": "EXPECTED" if expected else "UNEXPECTED",
        "stdout": write_output(name, "stdout", process.stdout),
        "stderr": write_output(name, "stderr", process.stderr),
    }


def retain_generated(
    source: Path, retained_name: str, needles: tuple[str, ...] = ()
) -> dict:
    destination = RUN_ROOT / "generated" / retained_name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    text = destination.read_text(encoding="utf-8")
    record = file_record(destination, "generated_backend_source")
    record["run_relative_path"] = destination.relative_to(RUN_ROOT).as_posix()
    record["generated_from"] = str(source)
    record["matches"] = [
        {"line": number, "text": line}
        for number, line in enumerate(text.splitlines(), start=1)
        if any(needle in line for needle in needles)
    ]
    return record


def source_audit() -> dict:
    selected = [
        UNIMATH_ROOT / "README.md",
        UNIMATH_SRC / "foundation" / "decidable-types.lagda.md",
        UNIMATH_SRC / "foundation" / "exclusive-sum.lagda.md",
        UNIMATH_SRC / "univalent-combinatorics" / "finite-types.lagda.md",
        UNIMATH_SRC
        / "univalent-combinatorics"
        / "equality-finite-types.lagda.md",
        UNIMATH_SRC
        / "univalent-combinatorics"
        / "orientations-complete-undirected-graph.lagda.md",
    ]
    execution_terms = re.compile(
        r"executable|execution|runtime|compile|compiler|backend|program|algorithm|"
        r"termination|resource|complexity|extract|real-world|real world",
        re.IGNORECASE,
    )
    execution_hits = []
    effective_hits = []
    anchors = {
        "is-finite-Prop": [],
        "has-decidable-equality-is-finite": [],
        "cases-is-prop-type-symmetric-exclusive-sum-Prop": [],
        "cases-g": [],
        "mod-two-number-of-differences-orientation-Complete-Undirected-Graph": [],
    }
    for path in selected:
        text = path.read_text(encoding="utf-8")
        for number, line in enumerate(text.splitlines(), start=1):
            if execution_terms.search(line):
                execution_hits.append(
                    {"path": str(path), "line": number, "text": line}
                )
            if re.search(r"effective", line, re.IGNORECASE):
                effective_hits.append(
                    {"path": str(path), "line": number, "text": line}
                )
            for anchor in anchors:
                if anchor in line:
                    anchors[anchor].append(
                        {"path": str(path), "line": number, "text": line}
                    )

    usage_files = []
    for path in sorted(UNIMATH_SRC.rglob("*.lagda.md")):
        if "has-decidable-equality-is-finite" in path.read_text(encoding="utf-8"):
            usage_files.append(str(path))
    return {
        "schema_version": "sem-b02-source-audit/v1",
        "selected_files": [file_record(path, "source_audit_input") for path in selected],
        "execution_promise_regex": execution_terms.pattern,
        "execution_promise_hits": execution_hits,
        "effective_token_hits": effective_hits,
        "effective_token_note": (
            "The fixed hits are the mathematical term `effective quotient`, not an "
            "executable-delivery promise."
        ),
        "anchors": anchors,
        "has_decidable_equality_is_finite_usage_files": usage_files,
        "has_decidable_equality_is_finite_usage_file_count": len(usage_files),
        "scope_limit": (
            "Fixed agda-unimath commit, the selected definition/natural-consumer files, "
            "and exact source-name usage discovery; no claim about external prose or future versions."
        ),
    }


def main() -> int:
    if RUN_ROOT.exists():
        print(f"refusing to overwrite existing run: {RUN_ROOT}", file=sys.stderr)
        return 2
    RUN_ROOT.mkdir(parents=True)

    probes = [
        PROBE_ROOT / "SemB02Kernel.agda",
        PROBE_ROOT / "SemB02DefinitionalNegative.agda",
        PROBE_ROOT / "SemB02ExplicitRuntime.agda",
        PROBE_ROOT / "SemB02FiniteRuntime.agda",
    ]
    required = [
        AGDA,
        NODE,
        AGDA_JS_RTS,
        LIBRARY_REGISTRY,
        TOOLCHAIN_MANIFEST,
        UNIMATH_ROOT / "agda-unimath.agda-lib",
        *probes,
    ]
    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        (RUN_ROOT / "PRECONDITION_FAILURE.json").write_text(
            json.dumps({"missing": missing}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return 2

    started_at = utc_now()
    start = time.monotonic()
    steps: list[dict] = []
    temp_root = Path(tempfile.mkdtemp(prefix="sem-b02-", dir=AGDA_TMP))
    explicit_js = temp_root / "explicit-js"
    finite_js = temp_root / "finite-js"
    finite_opt_js = temp_root / "finite-opt-js"

    try:
        steps.append(run_step("agda-version", [str(AGDA), "--version"], 0))
        steps.append(run_step("node-version", [str(NODE), "--version"], 0))

        equality_finite = (
            UNIMATH_SRC
            / "univalent-combinatorics"
            / "equality-finite-types.lagda.md"
        )
        fresh = agda_command(equality_finite)
        fresh.insert(1, "--ignore-interfaces")
        steps.append(run_step("kernel-equality-finite-fresh", fresh, 0))

        steps.append(
            run_step(
                "kernel-positive",
                agda_command(PROBE_ROOT / "SemB02Kernel.agda"),
                0,
            )
        )
        steps.append(
            run_step(
                "judgmental-negative",
                agda_command(PROBE_ROOT / "SemB02DefinitionalNegative.agda"),
                42,
                ("[UnequalTerms]", "finiteTag ＝ false"),
            )
        )
        steps.append(
            run_step(
                "explicit-runtime-check",
                agda_command(PROBE_ROOT / "SemB02ExplicitRuntime.agda"),
                0,
            )
        )
        steps.append(
            run_step(
                "finite-runtime-check",
                agda_command(PROBE_ROOT / "SemB02FiniteRuntime.agda"),
                0,
            )
        )

        explicit_compile = agda_command(PROBE_ROOT / "SemB02ExplicitRuntime.agda")
        explicit_compile[1:1] = ["--js", f"--compile-dir={explicit_js}"]
        steps.append(run_step("explicit-js-compile", explicit_compile, 0))
        explicit_env = command_env()
        explicit_env["NODE_PATH"] = os.pathsep.join(
            (str(explicit_js), str(AGDA_JS_RTS.parent))
        )
        steps.append(
            run_step(
                "explicit-node-run",
                [str(NODE), str(explicit_js / "jAgda.SemB02ExplicitRuntime.js")],
                0,
                ("FALSE",),
                explicit_env,
            )
        )

        finite_compile = agda_command(PROBE_ROOT / "SemB02FiniteRuntime.agda")
        finite_compile[1:1] = ["--js", f"--compile-dir={finite_js}"]
        steps.append(run_step("finite-js-compile", finite_compile, 0))
        finite_env = command_env()
        finite_env["NODE_PATH"] = os.pathsep.join(
            (str(finite_js), str(AGDA_JS_RTS.parent))
        )
        steps.append(
            run_step(
                "finite-node-run",
                [str(NODE), str(finite_js / "jAgda.SemB02FiniteRuntime.js")],
                1,
                ("exports.unit-trunc is not a function",),
                finite_env,
            )
        )

        finite_opt_compile = agda_command(PROBE_ROOT / "SemB02FiniteRuntime.agda")
        finite_opt_compile[1:1] = [
            "--js",
            "--js-optimize",
            f"--compile-dir={finite_opt_js}",
        ]
        steps.append(run_step("finite-js-opt-compile", finite_opt_compile, 0))
        finite_opt_env = command_env()
        finite_opt_env["NODE_PATH"] = os.pathsep.join(
            (str(finite_opt_js), str(AGDA_JS_RTS.parent))
        )
        steps.append(
            run_step(
                "finite-node-opt-run",
                [str(NODE), str(finite_opt_js / "jAgda.SemB02FiniteRuntime.js")],
                1,
                ("exports.unit-trunc is not a function",),
                finite_opt_env,
            )
        )

        generated = {
            "schema_version": "sem-b02-generated-evidence/v1",
            "explicit_main": retain_generated(
                explicit_js / "jAgda.SemB02ExplicitRuntime.js",
                "explicit/jAgda.SemB02ExplicitRuntime.js",
            ),
            "finite_main": retain_generated(
                finite_js / "jAgda.SemB02FiniteRuntime.js",
                "finite/jAgda.SemB02FiniteRuntime.js",
            ),
            "finite_kernel": retain_generated(
                finite_js / "jAgda.SemB02Kernel.js",
                "finite/jAgda.SemB02Kernel.js",
                ("finiteDecision", "finiteTag"),
            ),
            "finite_truncations": retain_generated(
                finite_js / "jAgda.foundation.truncations.js",
                "finite/jAgda.foundation.truncations.js",
                (
                    'exports["type-trunc"] = undefined',
                    'exports["unit-trunc"] = undefined',
                    'exports["is-truncation-trunc"] = undefined',
                ),
            ),
            "finite_set_truncations": retain_generated(
                finite_js / "jAgda.foundation.set-truncations.js",
                "finite/jAgda.foundation.set-truncations.js",
                ("equiv-unit-trunc-unit-Set",),
            ),
            "optimized_main": retain_generated(
                finite_opt_js / "jAgda.SemB02FiniteRuntime.js",
                "finite-optimized/jAgda.SemB02FiniteRuntime.js",
            ),
            "optimized_truncations": retain_generated(
                finite_opt_js / "jAgda.foundation.truncations.js",
                "finite-optimized/jAgda.foundation.truncations.js",
                ('exports["unit-trunc"] = undefined',),
            ),
        }
        (RUN_ROOT / "generated-evidence.json").write_text(
            json.dumps(generated, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    audit = source_audit()
    (RUN_ROOT / "source-audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    external_sources = [
        UNIMATH_SRC / "foundation" / "truncations.lagda.md",
        UNIMATH_SRC / "foundation" / "set-truncations.lagda.md",
        UNIMATH_SRC / "foundation" / "decidable-types.lagda.md",
        UNIMATH_SRC / "foundation" / "decidable-equality.lagda.md",
        UNIMATH_SRC / "foundation" / "booleans.lagda.md",
        UNIMATH_SRC / "foundation" / "exclusive-sum.lagda.md",
        UNIMATH_SRC / "foundation-core" / "booleans.lagda.md",
        UNIMATH_SRC / "univalent-combinatorics" / "counting.lagda.md",
        UNIMATH_SRC / "univalent-combinatorics" / "finite-types.lagda.md",
        UNIMATH_SRC
        / "univalent-combinatorics"
        / "equality-finite-types.lagda.md",
        UNIMATH_SRC
        / "univalent-combinatorics"
        / "orientations-complete-undirected-graph.lagda.md",
    ]
    manifest_entries = [
        file_record(Path(__file__).resolve(), "runner"),
        *[file_record(path, "probe_source") for path in probes],
        *[file_record(path, "external_source") for path in external_sources],
        file_record(UNIMATH_ROOT / "agda-unimath.agda-lib", "library_configuration"),
        file_record(LIBRARY_REGISTRY, "library_registry"),
        file_record(TOOLCHAIN_MANIFEST, "toolchain_manifest"),
        file_record(AGDA, "proof_assistant_binary"),
        file_record(NODE, "runtime_binary"),
        file_record(AGDA_JS_RTS, "runtime_support"),
    ]
    toolchain = json.loads(TOOLCHAIN_MANIFEST.read_text(encoding="utf-8"))
    manifest = {
        "schema_version": "sem-b02-source-manifest/v1",
        "agda_unimath_commit": toolchain["agda_unimath_library"]["commit_sha"],
        "agda_unimath_tree_sha256": toolchain["agda_unimath_library"][
            "tree_sha256"
        ],
        "files": manifest_entries,
    }
    (RUN_ROOT / "source-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    agda_version = (RUN_ROOT / "agda-version.stdout.txt").read_text(
        encoding="utf-8"
    ).strip().replace("\n", " | ")
    node_version = (RUN_ROOT / "node-version.stdout.txt").read_text(
        encoding="utf-8"
    ).strip()
    environment = "\n".join(
        (
            f"platform={platform.platform()}",
            f"python={platform.python_version()}",
            f"agda_executable={AGDA}",
            f"agda_version={agda_version}",
            f"node_executable={NODE}",
            f"node_version={node_version}",
            f"ghc_executable={shutil.which('ghc') or 'NOT_AVAILABLE'}",
            f"agda_unimath_root={UNIMATH_ROOT}",
            f"agda_unimath_commit={manifest['agda_unimath_commit']}",
            f"agda_unimath_tree_sha256={manifest['agda_unimath_tree_sha256']}",
            "theory_variant=Agda without-K with postulated truncations (agda-unimath)",
            "secret_policy=no full environment, credentials, cookies, or signed URLs retained",
        )
    ) + "\n"
    (RUN_ROOT / "environment.txt").write_text(environment, encoding="utf-8")

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
        "completed_at_utc": utc_now(),
        "duration_seconds": round(time.monotonic() - start, 6),
        "status": "EXPECTED_BOUNDARY_OBSERVED" if all_expected else "UNEXPECTED_RESULT",
        "git": {
            "branch": branch,
            "head_before_run": head,
            "state": "LOCAL_UNCOMMITTED_CANDIDATE",
        },
        "scope": (
            "A fixed finite-type equality-decision chain: fresh kernel checking, "
            "propositional versus judgmental result, explicit decision runtime control, "
            "and natural `is-finite` theorem module under normal and optimized JS generation."
        ),
        "verdict": (
            "FINITE_DECIDABILITY_KERNEL_ACCEPTED; EXPLICIT_DECISION_RUNTIME_WORKS; "
            "FINITE_THEOREM_MODULE_RUNTIME_BLOCKED_BY_POSTULATE_DEPENDENCY; "
            "NO_Q4_Q7_PROMISE_ESTABLISHED"
        ),
        "non_goals": [
            "The Node failure occurs during transitive module initialization before finiteDecision is selected; it is not a wrong equality answer.",
            "No claim that every finite-type or truncation implementation lacks computation.",
            "No claim that agda-unimath advertises this theorem as an executable decision procedure.",
            "No HoTT inconsistency or natural-usage mismatch claim.",
            "No GHC execution; this run covers Agda kernel and the JavaScript backend only."
        ],
        "steps": steps,
        "artifacts": {
            "environment": "environment.txt",
            "source_manifest": "source-manifest.json",
            "source_audit": "source-audit.json",
            "generated_evidence": "generated-evidence.json",
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
        "usage_files": audit["has_decidable_equality_is_finite_usage_file_count"],
        "execution_promise_hits": len(audit["execution_promise_hits"]),
        "run_root": str(RUN_ROOT),
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if all_expected else 1


if __name__ == "__main__":
    raise SystemExit(main())
