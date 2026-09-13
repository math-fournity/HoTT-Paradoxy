#!/usr/bin/env python3
"""Reproduce the SEM-B01 kernel, reduction, and delivery boundary probes."""

from __future__ import annotations

import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path


REPO = Path(__file__).resolve().parents[2]
OWN_ROOT = REPO / "semantic-overview"
PROBE_ROOT = OWN_ROOT / "formal" / "sem-b01"
RUN_ID = "20260913-SEM-B01-TRUNCATION-DELIVERY-001-01"
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


def sha256_bytes(data: bytes) -> str:
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
        "sha256": sha256_bytes(data),
    }


def output_record(path: Path, data: bytes) -> dict:
    path.write_bytes(data)
    return {
        "path": path.relative_to(RUN_ROOT).as_posix(),
        "bytes": len(data),
        "sha256": sha256_bytes(data),
    }


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def base_env() -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "XDG_DATA_HOME": str(AGDA_XDG_DATA),
            "XDG_CONFIG_HOME": str(AGDA_XDG_CONFIG),
            "TMPDIR": str(AGDA_TMP),
        }
    )
    return env


def agda_args(target: Path) -> list[str]:
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
    required_markers: tuple[str, ...] = (),
    env: dict[str, str] | None = None,
) -> dict:
    started = utc_now()
    start = time.monotonic()
    completed = subprocess.run(
        argv,
        cwd=REPO,
        env=env or base_env(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    duration = time.monotonic() - start
    stdout_path = RUN_ROOT / f"{name}.stdout.txt"
    stderr_path = RUN_ROOT / f"{name}.stderr.txt"
    stdout = output_record(stdout_path, completed.stdout)
    stderr = output_record(stderr_path, completed.stderr)
    combined = (completed.stdout + completed.stderr).decode("utf-8", errors="replace")
    missing_markers = [marker for marker in required_markers if marker not in combined]
    expected = completed.returncode == expected_exit and not missing_markers
    return {
        "name": name,
        "argv": argv,
        "cwd": str(REPO),
        "started_at_utc": started,
        "duration_seconds": round(duration, 6),
        "exit_code": completed.returncode,
        "expected_exit_code": expected_exit,
        "required_markers": list(required_markers),
        "missing_markers": missing_markers,
        "status": "EXPECTED" if expected else "UNEXPECTED",
        "stdout": stdout,
        "stderr": stderr,
    }


def retain_generated(
    path: Path, retained_name: str, needles: tuple[str, ...] = ()
) -> dict:
    destination = RUN_ROOT / "generated" / retained_name
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(path, destination)
    text = destination.read_text(encoding="utf-8")
    matches = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        if any(needle in line for needle in needles):
            matches.append({"line": line_number, "text": line})
    record = file_record(destination, "generated_backend_source")
    record["run_relative_path"] = destination.relative_to(RUN_ROOT).as_posix()
    record["generated_from"] = str(path)
    record["matches"] = matches
    return record


def main() -> int:
    if RUN_ROOT.exists():
        print(f"refusing to overwrite existing run: {RUN_ROOT}", file=sys.stderr)
        return 2
    RUN_ROOT.mkdir(parents=True)

    required = [
        AGDA,
        NODE,
        AGDA_JS_RTS,
        LIBRARY_REGISTRY,
        TOOLCHAIN_MANIFEST,
        UNIMATH_ROOT / "agda-unimath.agda-lib",
        PROBE_ROOT / "SemB01Kernel.agda",
        PROBE_ROOT / "SemB01DefinitionalNegative.agda",
        PROBE_ROOT / "SemB01DirectRuntime.agda",
        PROBE_ROOT / "SemB01TruncatedRuntime.agda",
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
    temp_root = Path(tempfile.mkdtemp(prefix="sem-b01-", dir=AGDA_TMP))
    direct_js = temp_root / "direct-js"
    truncated_js = temp_root / "truncated-js"
    ghc_source = temp_root / "ghc-source"

    try:
        steps.append(run_step("agda-version", [str(AGDA), "--version"], 0))
        steps.append(run_step("node-version", [str(NODE), "--version"], 0))

        polynomial = (
            UNIMATH_SRC
            / "commutative-algebra"
            / "polynomials-commutative-semirings.lagda.md"
        )
        polynomial_args = agda_args(polynomial)
        polynomial_args.insert(1, "--ignore-interfaces")
        steps.append(run_step("kernel-polynomial-fresh", polynomial_args, 0))

        steps.append(
            run_step(
                "kernel-positive",
                agda_args(PROBE_ROOT / "SemB01Kernel.agda"),
                0,
            )
        )
        steps.append(
            run_step(
                "judgmental-negative",
                agda_args(PROBE_ROOT / "SemB01DefinitionalNegative.agda"),
                42,
                ("[UnequalTerms]", "truncatedResult ＝ true"),
            )
        )
        steps.append(
            run_step(
                "direct-runtime-check",
                agda_args(PROBE_ROOT / "SemB01DirectRuntime.agda"),
                0,
            )
        )
        steps.append(
            run_step(
                "truncated-runtime-check",
                agda_args(PROBE_ROOT / "SemB01TruncatedRuntime.agda"),
                0,
            )
        )

        direct_compile = agda_args(PROBE_ROOT / "SemB01DirectRuntime.agda")
        direct_compile[1:1] = ["--js", f"--compile-dir={direct_js}"]
        steps.append(run_step("direct-js-compile", direct_compile, 0))

        node_direct_env = base_env()
        node_direct_env["NODE_PATH"] = os.pathsep.join(
            (str(direct_js), str(AGDA_JS_RTS.parent))
        )
        steps.append(
            run_step(
                "direct-node-run",
                [str(NODE), str(direct_js / "jAgda.SemB01DirectRuntime.js")],
                0,
                ("TRUE",),
                node_direct_env,
            )
        )

        truncated_compile = agda_args(PROBE_ROOT / "SemB01TruncatedRuntime.agda")
        truncated_compile[1:1] = ["--js", f"--compile-dir={truncated_js}"]
        steps.append(run_step("truncated-js-compile", truncated_compile, 0))

        node_truncated_env = base_env()
        node_truncated_env["NODE_PATH"] = os.pathsep.join(
            (str(truncated_js), str(AGDA_JS_RTS.parent))
        )
        steps.append(
            run_step(
                "truncated-node-run",
                [str(NODE), str(truncated_js / "jAgda.SemB01TruncatedRuntime.js")],
                1,
                ("unit-trunc is not a function",),
                node_truncated_env,
            )
        )

        ghc_compile = agda_args(PROBE_ROOT / "SemB01Kernel.agda")
        ghc_compile[1:1] = [
            "--compile",
            "--ghc-dont-call-ghc",
            "--no-main",
            f"--compile-dir={ghc_source}",
        ]
        steps.append(run_step("ghc-source-generate", ghc_compile, 0))

        js_truncations = truncated_js / "jAgda.foundation.truncations.js"
        hs_truncations = (
            ghc_source
            / "MAlonzo"
            / "Code"
            / "Qfoundation"
            / "Qtruncations.hs"
        )
        generated = {
            "schema_version": "sem-b01-generated-evidence/v1",
            "js_truncations": retain_generated(
                js_truncations,
                "js/jAgda.foundation.truncations.js",
                (
                    'exports["type-trunc"] = undefined',
                    'exports["is-trunc-type-trunc"] = undefined',
                    'exports["unit-trunc"] = undefined',
                    'exports["is-truncation-trunc"] = undefined',
                ),
            ),
            "ghc_truncations": retain_generated(
                hs_truncations,
                "ghc/Qfoundation/Qtruncations.hs",
                ("postulate evaluated: foundation.truncations",),
            ),
            "direct_main_js": retain_generated(
                direct_js / "jAgda.SemB01DirectRuntime.js",
                "js/jAgda.SemB01DirectRuntime.js",
            ),
            "truncated_main_js": retain_generated(
                truncated_js / "jAgda.SemB01TruncatedRuntime.js",
                "js/jAgda.SemB01TruncatedRuntime.js",
            ),
            "kernel_probe_js": retain_generated(
                truncated_js / "jAgda.SemB01Kernel.js",
                "js/jAgda.SemB01Kernel.js",
            ),
        }
        (RUN_ROOT / "generated-evidence.json").write_text(
            json.dumps(generated, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    finally:
        shutil.rmtree(temp_root, ignore_errors=True)

    source_paths = [
        (Path(__file__).resolve(), "runner"),
        (PROBE_ROOT / "SemB01Kernel.agda", "probe_source"),
        (PROBE_ROOT / "SemB01DefinitionalNegative.agda", "negative_probe_source"),
        (PROBE_ROOT / "SemB01DirectRuntime.agda", "positive_control_source"),
        (PROBE_ROOT / "SemB01TruncatedRuntime.agda", "runtime_probe_source"),
        (UNIMATH_SRC / "foundation" / "truncations.lagda.md", "external_source"),
        (
            UNIMATH_SRC / "foundation" / "propositional-truncations.lagda.md",
            "external_source",
        ),
        (
            UNIMATH_SRC
            / "foundation"
            / "universal-property-propositional-truncation-into-sets.lagda.md",
            "external_source",
        ),
        (
            UNIMATH_SRC / "foundation" / "weakly-constant-maps.lagda.md",
            "external_source",
        ),
        (
            UNIMATH_SRC
            / "commutative-algebra"
            / "polynomials-commutative-semirings.lagda.md",
            "external_source",
        ),
        (
            UNIMATH_SRC / "foundation-core" / "booleans.lagda.md",
            "external_source",
        ),
        (UNIMATH_SRC / "foundation" / "unit-type.lagda.md", "external_source"),
        (UNIMATH_ROOT / "agda-unimath.agda-lib", "library_configuration"),
        (LIBRARY_REGISTRY, "library_registry"),
        (TOOLCHAIN_MANIFEST, "toolchain_manifest"),
        (AGDA, "proof_assistant_binary"),
        (NODE, "runtime_binary"),
        (AGDA_JS_RTS, "runtime_support"),
    ]
    toolchain_data = json.loads(TOOLCHAIN_MANIFEST.read_text(encoding="utf-8"))
    source_manifest = {
        "schema_version": "sem-b01-source-manifest/v1",
        "agda_unimath_commit": toolchain_data["agda_unimath_library"]["commit_sha"],
        "agda_unimath_tree_sha256": toolchain_data["agda_unimath_library"][
            "tree_sha256"
        ],
        "files": [file_record(path, kind) for path, kind in source_paths],
    }
    (RUN_ROOT / "source-manifest.json").write_text(
        json.dumps(source_manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    agda_version = next(step for step in steps if step["name"] == "agda-version")
    node_version = next(step for step in steps if step["name"] == "node-version")
    agda_text = (RUN_ROOT / agda_version["stdout"]["path"]).read_text(
        encoding="utf-8"
    ).strip().replace("\n", " | ")
    node_text = (RUN_ROOT / node_version["stdout"]["path"]).read_text(
        encoding="utf-8"
    ).strip()
    environment = "\n".join(
        (
            f"platform={platform.platform()}",
            f"python={platform.python_version()}",
            f"agda_executable={AGDA}",
            f"agda_version={agda_text}",
            f"node_executable={NODE}",
            f"node_version={node_text}",
            f"ghc_executable={shutil.which('ghc') or 'NOT_AVAILABLE'}",
            f"agda_unimath_root={UNIMATH_ROOT}",
            f"agda_unimath_commit={source_manifest['agda_unimath_commit']}",
            f"agda_unimath_tree_sha256={source_manifest['agda_unimath_tree_sha256']}",
            "theory_variant=Agda without-K with postulated truncations (agda-unimath)",
            "secret_policy=no full environment, credentials, cookies, or signed URLs retained",
        )
    ) + "\n"
    (RUN_ROOT / "environment.txt").write_text(environment, encoding="utf-8")

    all_expected = all(step["status"] == "EXPECTED" for step in steps)
    git_head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=REPO,
        stdout=subprocess.PIPE,
        check=True,
        text=True,
    ).stdout.strip()
    git_branch = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=REPO,
        stdout=subprocess.PIPE,
        check=True,
        text=True,
    ).stdout.strip()
    run = {
        "schema_version": "semantic-overview-run/v1",
        "run_id": RUN_ID,
        "started_at_utc": started_at,
        "completed_at_utc": utc_now(),
        "duration_seconds": round(time.monotonic() - start, 6),
        "status": "EXPECTED_BOUNDARY_OBSERVED" if all_expected else "UNEXPECTED_RESULT",
        "git": {
            "branch": git_branch,
            "head_before_run": git_head,
            "state": "LOCAL_UNCOMMITTED_CANDIDATE",
        },
        "scope": (
            "A closed agda-unimath propositional-truncation consumer: kernel acceptance, "
            "lack of judgmental unit reduction, JS source generation, direct-runtime positive "
            "control, forced truncated-runtime evaluation, and GHC source generation."
        ),
        "verdict": (
            "KERNEL_ACCEPTS_PROPOSITIONAL_COMPUTATION; "
            "JS_RUNTIME_BLOCKED_BY_UNIMPLEMENTED_TRUNCATION_POSTULATES; "
            "NO_EFFECTIVE_DELIVERY_CLAIM_ESTABLISHED"
        ),
        "non_goals": [
            "No claim that every implementation of propositional truncation is noncomputable.",
            "No claim that agda-unimath promises executable delivery for this API.",
            "No HoTT inconsistency or natural-usage mismatch claim.",
            "The GHC backend generated source only; GHC is unavailable and no native executable ran.",
            "The full polynomial value was not executed; the closed bool probe isolates the same truncation consumer interface."
        ],
        "steps": steps,
        "artifacts": {
            "environment": "environment.txt",
            "source_manifest": "source-manifest.json",
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
        "run_root": str(RUN_ROOT),
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0 if all_expected else 1


if __name__ == "__main__":
    raise SystemExit(main())
