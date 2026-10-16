#!/usr/bin/env python3
"""Freeze and replay a Coq-HoTT reflective-subuniverse proof-search study.

The evaluator keeps four claims separate:

* Coq-HoTT's source explicitly documents recursive typeclass-search hazards;
* the current library avoids registering the relevant rule automatically;
* registering that rule as an ordinary instance can make a fixed proof search
  fail to complete within a declared observation interval; and
* this does not establish non-termination of kernel checking, a HoTT-specific
  metatheorem, a reality-relative paradox, or a Gödel incompleteness instance.

Native Rocq runs are execution evidence with a frozen scope.  They are not
entered into the project's mathematical claim matrix.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

from machine_overview.util import (
    MachineOverviewError,
    deterministic_tree,
    git_state,
    json_bytes,
    read_json,
    safe_relative,
    sha256_bytes,
    sha256_file,
    utc_now,
    write_bytes,
    write_json,
)


SCOPE_SCHEMA = "machine-overview-coq-hott-typeclass-recursion-scope/v1"
FREEZE_SCHEMA = "machine-overview-coq-hott-typeclass-recursion-freeze/v1"
DECISIONS_SCHEMA = "machine-overview-coq-hott-typeclass-recursion-decisions/v1"
RUN_SCHEMA = "machine-overview-coq-hott-typeclass-recursion-run/v1"
EXPECTATIONS = {
    "ACCEPT",
    "PROOF_SEARCH_FAILURE",
    "SEARCH_DEPTH_LIMIT",
    "OBSERVATION_LIMIT",
}
ENVIRONMENTS = {"COQ_HOTT", "ROCQ_DEFAULT"}
ACTIVE_REGISTRATION_RE = re.compile(
    r"^\s*(?:#\[[^\]]+\]\s*)?(Existing\s+Instance|Hint\s+Resolve|Hint\s+Immediate)\s+isequiv_O_inverts\b"
)


def repo_root() -> Path:
    completed = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
        check=True,
    )
    return Path(completed.stdout.strip()).resolve()


def _under(path: Path, parent: Path, label: str) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(parent.resolve())
    except ValueError as exc:
        raise MachineOverviewError(
            f"COQ_HOTT_TYPECLASS_PATH_OUTSIDE_ROOT:{label}:{path}"
        ) from exc
    return resolved


def _resolve(
    root: Path, value: str, allowed_roots: list[Path], label: str
) -> Path:
    raw = Path(value)
    if raw.is_absolute():
        for allowed in allowed_roots:
            try:
                return _under(raw, allowed, label)
            except MachineOverviewError:
                continue
        raise MachineOverviewError(
            f"COQ_HOTT_TYPECLASS_EXTERNAL_PATH_NOT_ALLOWED:{label}:{value}"
        )
    return _under(root / safe_relative(value), root, label)


def _pin(root: Path, path: Path) -> dict[str, object]:
    resolved = path.resolve()
    try:
        value = resolved.relative_to(root.resolve()).as_posix()
    except ValueError:
        value = str(resolved)
    if not resolved.is_file() or resolved.is_symlink():
        raise MachineOverviewError(f"COQ_HOTT_TYPECLASS_PIN_INVALID:{value}")
    return {
        "path": value,
        "bytes": resolved.stat().st_size,
        "sha256": sha256_file(resolved),
    }


def _allowed_roots(scope: dict) -> list[Path]:
    roots = [Path(value).resolve() for value in scope.get("allowed_external_roots", [])]
    if not roots or any(not path.is_dir() or path.is_symlink() for path in roots):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_ALLOWED_ROOT_INVALID")
    return roots


def _verify_pin(
    root: Path, row: dict, allowed_roots: list[Path], label: str
) -> Path:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise MachineOverviewError(f"COQ_HOTT_TYPECLASS_PIN_ROW_INVALID:{label}")
    path = _resolve(root, row["path"], allowed_roots, label)
    if (
        not path.is_file()
        or path.is_symlink()
        or path.stat().st_size != row.get("bytes")
        or sha256_file(path) != row.get("sha256")
    ):
        raise MachineOverviewError(
            f"COQ_HOTT_TYPECLASS_PIN_CHANGED:{label}:{row.get('path')}"
        )
    return path


def _docker_identity(image: str) -> dict[str, object]:
    completed = subprocess.run(
        ["docker", "image", "inspect", image],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if completed.returncode != 0:
        raise MachineOverviewError(
            f"COQ_HOTT_TYPECLASS_DOCKER_IMAGE_UNAVAILABLE:{image}"
        )
    rows = json.loads(completed.stdout)
    if not isinstance(rows, list) or len(rows) != 1:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_DOCKER_IDENTITY_INVALID")
    row = rows[0]
    return {
        "id": row.get("Id"),
        "architecture": row.get("Architecture"),
        "os": row.get("Os"),
        "repo_digests": sorted(row.get("RepoDigests") or []),
    }


def _git_source_identity(path: Path) -> dict[str, object]:
    def run(*args: str) -> str:
        completed = subprocess.run(
            ["git", "-C", str(path), *args],
            capture_output=True,
            text=True,
            timeout=30,
        )
        if completed.returncode != 0:
            raise MachineOverviewError(
                "COQ_HOTT_TYPECLASS_GIT_IDENTITY_FAILED:" + " ".join(args)
            )
        return completed.stdout

    head = run("rev-parse", "HEAD").strip()
    tree = run("rev-parse", "HEAD^{tree}").strip()
    status = run("status", "--porcelain=v1")
    tracked_raw = subprocess.run(
        ["git", "-C", str(path), "ls-files", "--stage", "-z"],
        capture_output=True,
        timeout=30,
        check=True,
    ).stdout
    tracked = [value for value in tracked_raw.split(b"\0") if value]
    digest = bytearray()
    total = 0
    for entry in tracked:
        metadata, encoded_relative = entry.split(b"\t", 1)
        mode, object_id, stage = metadata.decode("ascii").split()
        relative = encoded_relative.decode("utf-8")
        file_path = path / relative
        if mode == "160000":
            row = {
                "path": relative,
                "mode": mode,
                "gitlink_object": object_id,
                "stage": stage,
            }
        else:
            data = (
                os.readlink(file_path).encode("utf-8")
                if mode == "120000"
                else file_path.read_bytes()
            )
            row = {
                "path": relative,
                "mode": mode,
                "stage": stage,
                "bytes": len(data),
                "sha256": sha256_bytes(data),
            }
            total += len(data)
        digest.extend(json.dumps(row, sort_keys=True).encode("utf-8"))
        digest.extend(b"\n")
    return {
        "head": head,
        "tree": tree,
        "clean": status == "",
        "tracked_files": len(tracked),
        "tracked_bytes": total,
        "tracked_tree_sha256": sha256_bytes(bytes(digest)),
    }


def validate_scope(root: Path, scope: dict) -> dict[str, object]:
    if scope.get("schema_version") != SCOPE_SCHEMA:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_SCOPE_SCHEMA_INVALID")
    allowed = _allowed_roots(scope)

    source = scope.get("source", {})
    source_root = _resolve(root, source.get("root", ""), allowed, "source.root")
    if not source_root.is_dir() or source_root.is_symlink():
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_SOURCE_ROOT_INVALID")
    source_identity = _git_source_identity(source_root)
    if source_identity != source.get("identity"):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_SOURCE_IDENTITY_CHANGED")

    artifacts: dict[str, dict[str, object]] = {}
    for artifact in source.get("artifacts", []):
        artifact_id = artifact.get("artifact_id")
        if not isinstance(artifact_id, str) or artifact_id in artifacts:
            raise MachineOverviewError("COQ_HOTT_TYPECLASS_ARTIFACT_ID_INVALID")
        path = _verify_pin(root, artifact, allowed, artifact_id)
        _under(path, source_root, artifact_id)
        artifacts[artifact_id] = {"row": artifact, "path": path}

    build = scope.get("build", {})
    build_root = _resolve(root, build.get("root", ""), allowed, "build.root")
    if not build_root.is_dir() or build_root.is_symlink():
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_BUILD_ROOT_INVALID")
    build_identity = deterministic_tree(build_root)
    if build_identity != build.get("identity"):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_BUILD_IDENTITY_CHANGED")
    build_files: dict[str, Path] = {}
    for row in build.get("required_files", []):
        file_id = row.get("file_id")
        if not isinstance(file_id, str) or file_id in build_files:
            raise MachineOverviewError("COQ_HOTT_TYPECLASS_BUILD_FILE_ID_INVALID")
        path = _verify_pin(root, row, allowed, file_id)
        _under(path, build_root, file_id)
        build_files[file_id] = path

    docker = scope.get("toolchain", {}).get("docker", {})
    actual_docker = _docker_identity(docker.get("image", ""))
    if actual_docker != docker.get("identity"):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_DOCKER_IDENTITY_CHANGED")
    qualification_files: dict[str, Path] = {}
    for row in scope.get("toolchain", {}).get("qualification_artifacts", []):
        artifact_id = row.get("artifact_id")
        if not isinstance(artifact_id, str) or artifact_id in qualification_files:
            raise MachineOverviewError(
                "COQ_HOTT_TYPECLASS_QUALIFICATION_ARTIFACT_ID_INVALID"
            )
        qualification_files[artifact_id] = _verify_pin(
            root, row, allowed, artifact_id
        )

    question_ids = [row.get("id") for row in scope.get("questions", [])]
    expected_questions = [f"C{i}" for i in range(1, 9)] + [
        f"Q{i}" for i in range(1, 8)
    ]
    if question_ids != expected_questions:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_QUESTION_ROSTER_INVALID")

    plan = scope.get("probe_plan", [])
    probe_ids = [row.get("probe_id") for row in plan]
    if not plan or len(probe_ids) != len(set(probe_ids)):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_PROBE_ROSTER_INVALID")
    for row in plan:
        if row.get("expect") not in EXPECTATIONS:
            raise MachineOverviewError(
                f"COQ_HOTT_TYPECLASS_PROBE_EXPECT_INVALID:{row.get('probe_id')}"
            )
        if row.get("environment") not in ENVIRONMENTS:
            raise MachineOverviewError(
                f"COQ_HOTT_TYPECLASS_PROBE_ENV_INVALID:{row.get('probe_id')}"
            )
        if not isinstance(row.get("timeout_seconds"), int) or row["timeout_seconds"] < 1:
            raise MachineOverviewError(
                f"COQ_HOTT_TYPECLASS_PROBE_TIMEOUT_INVALID:{row.get('probe_id')}"
            )
        if row.get("future_path") not in scope.get("future_paths", []):
            raise MachineOverviewError(
                f"COQ_HOTT_TYPECLASS_PROBE_PATH_UNDECLARED:{row.get('probe_id')}"
            )
        if row["expect"] in {"PROOF_SEARCH_FAILURE", "SEARCH_DEPTH_LIMIT"}:
            if not isinstance(row.get("diagnostic"), str) or not row["diagnostic"]:
                raise MachineOverviewError(
                    f"COQ_HOTT_TYPECLASS_PROBE_DIAGNOSTIC_MISSING:{row.get('probe_id')}"
                )

    attempt_root = _resolve(
        root,
        scope.get("external_attempt_root", ""),
        allowed,
        "external_attempt_root",
    )
    if attempt_root.exists() and (not attempt_root.is_dir() or attempt_root.is_symlink()):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_ATTEMPT_ROOT_INVALID")

    return {
        "allowed_roots": allowed,
        "source_root": source_root,
        "source_identity": source_identity,
        "artifacts": artifacts,
        "build_root": build_root,
        "build_identity": build_identity,
        "build_files": build_files,
        "docker": actual_docker,
        "qualification_files": qualification_files,
        "attempt_root": attempt_root,
    }


def _load_bound(
    root: Path,
    path: Path,
    schema: str,
    scope_path: Path | None = None,
    evaluator_path: Path | None = None,
) -> dict:
    value = read_json(path)
    if value.get("schema_version") != schema:
        raise MachineOverviewError(f"COQ_HOTT_TYPECLASS_BOUND_SCHEMA_INVALID:{path}")
    deterministic = value.get("deterministic")
    if not isinstance(deterministic, dict):
        raise MachineOverviewError(
            f"COQ_HOTT_TYPECLASS_BOUND_DETERMINISTIC_MISSING:{path}"
        )
    if sha256_bytes(json_bytes(deterministic)) != value.get("deterministic_sha256"):
        raise MachineOverviewError(
            f"COQ_HOTT_TYPECLASS_BOUND_DIGEST_CHANGED:{path}"
        )
    if scope_path is not None and deterministic.get("scope") != _pin(root, scope_path):
        raise MachineOverviewError(f"COQ_HOTT_TYPECLASS_SCOPE_BINDING_CHANGED:{path}")
    if evaluator_path is not None and deterministic.get("evaluator") != _pin(
        root, evaluator_path
    ):
        raise MachineOverviewError(
            f"COQ_HOTT_TYPECLASS_EVALUATOR_BINDING_CHANGED:{path}"
        )
    return value


def _run_precheck(root: Path, argv: list[str], timeout: int) -> dict[str, object]:
    started = time.monotonic()
    completed = subprocess.run(
        argv,
        cwd=root,
        capture_output=True,
        timeout=timeout,
    )
    return {
        "argv": argv,
        "exit_code": completed.returncode,
        "stdout": completed.stdout.decode("utf-8", errors="replace"),
        "stderr": completed.stderr.decode("utf-8", errors="replace"),
        "duration_ms": round((time.monotonic() - started) * 1000),
    }


def freeze(scope_path: Path, output: Path) -> dict[str, object]:
    root = repo_root()
    scope_path = scope_path.resolve()
    output = output.resolve()
    if output.exists():
        raise MachineOverviewError(f"COQ_HOTT_TYPECLASS_FREEZE_EXISTS:{output}")
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    for value in scope.get("future_paths", []):
        path = _under(root / safe_relative(value), root, "future-path")
        if path.exists():
            raise MachineOverviewError(
                f"COQ_HOTT_TYPECLASS_FUTURE_PATH_EXISTS:{value}"
            )
    prechecks = [
        _run_precheck(root, [sys.executable, "machine-overview/mo.py", "selftest"], 120),
        _run_precheck(root, [sys.executable, "machine-overview/mo.py", "validate"], 60),
    ]
    if any(row["exit_code"] != 0 for row in prechecks):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_PREFREEZE_CHECK_FAILED")
    deterministic = {
        "evaluation_id": scope["evaluation_id"],
        "freeze_id": scope["freeze_id"],
        "scope": _pin(root, scope_path),
        "evaluator": _pin(root, Path(__file__)),
        "source_identity": validated["source_identity"],
        "build_identity": validated["build_identity"],
        "docker": validated["docker"],
        "qualification_artifacts": [
            _pin(root, path)
            for _, path in sorted(validated["qualification_files"].items())
        ],
        "probe_plan": scope["probe_plan"],
        "qualification_gates": scope["qualification_gates"],
        "future_paths_absent": True,
        "git": git_state(root),
        "prechecks": prechecks,
        "interpretation": scope["freeze_interpretation"],
    }
    value = {
        "schema_version": FREEZE_SCHEMA,
        "generated_at_utc": utc_now(),
        "deterministic": deterministic,
        "deterministic_sha256": sha256_bytes(json_bytes(deterministic)),
    }
    write_json(output, value)
    return {
        "status": "COQ_HOTT_TYPECLASS_FREEZE_CREATED",
        "path": str(output),
        "deterministic_sha256": value["deterministic_sha256"],
    }


def _artifact_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise MachineOverviewError(
            f"COQ_HOTT_TYPECLASS_TEXT_READ_FAILED:{path}"
        ) from exc


def _anchor_checks(scope: dict, validated: dict[str, object]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for artifact in scope["source"]["artifacts"]:
        artifact_id = artifact["artifact_id"]
        text = _artifact_text(validated["artifacts"][artifact_id]["path"])
        for anchor in artifact.get("anchors", []):
            literal = anchor["literal"]
            count = text.count(literal)
            rows.append(
                {
                    "artifact_id": artifact_id,
                    "anchor_id": anchor["anchor_id"],
                    "literal_sha256": sha256_bytes(literal.encode("utf-8")),
                    "occurrences": count,
                    "found": count >= anchor.get("minimum", 1),
                }
            )
    return rows


def _registration_inventory(source_root: Path) -> dict[str, object]:
    active: list[dict[str, object]] = []
    documented: list[dict[str, object]] = []
    phrases = (
        "causes an infinite regress",
        "cause infinite loops",
        "causing loops in typeclass search",
        "long or interminable searches",
    )
    for path in sorted(source_root.rglob("*.v")):
        text = _artifact_text(path)
        for line_no, line in enumerate(text.splitlines(), 1):
            match = ACTIVE_REGISTRATION_RE.search(line)
            if match:
                active.append(
                    {
                        "path": path.relative_to(source_root).as_posix(),
                        "line": line_no,
                        "kind": match.group(1),
                        "line_sha256": sha256_bytes(line.encode("utf-8")),
                    }
                )
            if any(phrase in line for phrase in phrases):
                documented.append(
                    {
                        "path": path.relative_to(source_root).as_posix(),
                        "line": line_no,
                        "line_sha256": sha256_bytes(line.encode("utf-8")),
                    }
                )
    return {
        "active_isequiv_O_inverts_registrations": active,
        "active_registration_count": len(active),
        "documented_recursive_search_boundaries": documented,
        "documented_boundary_count": len(documented),
    }


def decide(scope_path: Path, freeze_path: Path, output: Path) -> dict[str, object]:
    root = repo_root()
    scope_path = scope_path.resolve()
    freeze_path = freeze_path.resolve()
    output = output.resolve()
    if output.exists():
        raise MachineOverviewError(f"COQ_HOTT_TYPECLASS_DECISIONS_EXISTS:{output}")
    evaluator = Path(__file__).resolve()
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    freeze_value = _load_bound(
        root, freeze_path, FREEZE_SCHEMA, scope_path, evaluator
    )
    anchors = _anchor_checks(scope, validated)
    if not anchors or not all(row["found"] for row in anchors):
        missing = [row["anchor_id"] for row in anchors if not row["found"]]
        raise MachineOverviewError(
            "COQ_HOTT_TYPECLASS_SOURCE_ANCHOR_MISSING:" + ",".join(missing)
        )
    inventory = _registration_inventory(validated["source_root"])
    expected = scope["source"]["expected_registration_inventory"]
    if inventory["active_registration_count"] != expected["active_registration_count"]:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_ACTIVE_REGISTRATION_CHANGED")
    if inventory["documented_boundary_count"] != expected["documented_boundary_count"]:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_DOCUMENTED_BOUNDARY_CHANGED")
    probe_rows = []
    for row in scope["probe_plan"]:
        source = _under(
            root / safe_relative(row["future_path"]), root, row["probe_id"]
        )
        probe_rows.append({**row, "source": _pin(root, source)})
    deterministic = {
        "evaluation_id": scope["evaluation_id"],
        "scope": _pin(root, scope_path),
        "freeze": _pin(root, freeze_path),
        "freeze_deterministic_sha256": freeze_value["deterministic_sha256"],
        "evaluator": _pin(root, evaluator),
        "anchor_checks": anchors,
        "all_anchors_found": True,
        "registration_inventory": inventory,
        "probe_plan": probe_rows,
        "predeclared_interpretations": scope["predeclared_interpretations"],
    }
    value = {
        "schema_version": DECISIONS_SCHEMA,
        "generated_at_utc": utc_now(),
        "deterministic": deterministic,
        "deterministic_sha256": sha256_bytes(json_bytes(deterministic)),
    }
    write_json(output, value)
    return {
        "status": "COQ_HOTT_TYPECLASS_DECISIONS_CREATED",
        "path": str(output),
        "anchors": len(anchors),
        "documented_boundaries": inventory["documented_boundary_count"],
        "deterministic_sha256": value["deterministic_sha256"],
    }


def _probe_command(
    scope: dict,
    validated: dict[str, object],
    row: dict,
    attempt: Path,
) -> list[str]:
    image = scope["toolchain"]["docker"]["image"]
    command = [
        "docker",
        "run",
        "--rm",
        "--network",
        "none",
        "--platform",
        scope["toolchain"]["docker"]["platform"],
        "-v",
        f"{validated['build_root']}:/hott:ro",
        "-v",
        f"{attempt}:/probe",
        "-w",
        "/probe",
        image,
        "/usr/bin/timeout",
        f"{row['timeout_seconds']}s",
        "rocq",
        "c",
        "-q",
    ]
    if row["environment"] == "COQ_HOTT":
        command.extend(
            [
                "-noinit",
                "-indices-matter",
                "-native-compiler",
                "no",
                "-R",
                "/hott/theories",
                "HoTT",
            ]
        )
    command.append("/probe/" + Path(row["future_path"]).name)
    return command


def _classify(row: dict, exit_code: int, stdout: bytes, stderr: bytes) -> str:
    output = (stdout + b"\n" + stderr).decode("utf-8", errors="replace")
    if row["expect"] == "ACCEPT" and exit_code == 0:
        return "KERNEL_ACCEPTED"
    if (
        row["expect"] == "PROOF_SEARCH_FAILURE"
        and exit_code == row.get("expected_exit", 1)
        and row["diagnostic"] in output
    ):
        return "EXPECTED_PROOF_SEARCH_FAILURE"
    if (
        row["expect"] == "SEARCH_DEPTH_LIMIT"
        and exit_code == row.get("expected_exit", 1)
        and row["diagnostic"] in output
    ):
        return "EXPECTED_SEARCH_DEPTH_LIMIT"
    if row["expect"] == "OBSERVATION_LIMIT" and exit_code == 124:
        return "EXPECTED_OBSERVATION_LIMIT"
    return "UNEXPECTED_RESULT"


def _execute(argv: list[str], host_timeout: int) -> dict[str, object]:
    started = time.monotonic()
    try:
        completed = subprocess.run(argv, capture_output=True, timeout=host_timeout)
    except subprocess.TimeoutExpired as exc:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_HOST_TIMEOUT") from exc
    return {
        "exit_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "duration_ms": round((time.monotonic() - started) * 1000),
    }


def _prepare_attempt(
    root: Path,
    scope: dict,
    validated: dict[str, object],
    row: dict,
    run_id: str,
    label: str,
    rerun_generation: str | None = None,
) -> tuple[Path, list[str]]:
    segment = run_id if rerun_generation is None else f"verify-{run_id}-{rerun_generation}"
    attempt = (
        validated["attempt_root"] / segment / row["probe_id"] / label
    ).resolve()
    _under(attempt, validated["attempt_root"], row["probe_id"])
    if attempt.exists():
        raise MachineOverviewError(
            f"COQ_HOTT_TYPECLASS_ATTEMPT_EXISTS:{attempt}"
        )
    attempt.mkdir(parents=True)
    source = _under(
        root / safe_relative(row["future_path"]), root, row["probe_id"]
    )
    shutil.copy2(source, attempt / source.name)
    return attempt, _probe_command(scope, validated, row, attempt)


def _write_attempt(
    root: Path,
    base: Path,
    label: str,
    argv: list[str],
    result: dict[str, object],
    classification: str,
) -> dict[str, object]:
    folder = base / label
    folder.mkdir(parents=True, exist_ok=False)
    write_json(
        folder / "command.json",
        {
            "argv": argv,
            "cwd": str(root),
            "network": "none",
            "observation_limit_seconds": int(
                argv[argv.index("/usr/bin/timeout") + 1][:-1]
            ),
        },
    )
    write_bytes(folder / "stdout.txt", result["stdout"])
    write_bytes(folder / "stderr.txt", result["stderr"])
    write_json(
        folder / "result.json",
        {
            "exit_code": result["exit_code"],
            "classification": classification,
            "duration_ms": result["duration_ms"],
        },
    )
    return {
        "command": _pin(root, folder / "command.json"),
        "stdout": _pin(root, folder / "stdout.txt"),
        "stderr": _pin(root, folder / "stderr.txt"),
        "exit_code": result["exit_code"],
        "classification": classification,
    }


def _trace_signature(stdout: bytes) -> dict[str, object]:
    text = stdout.decode("utf-8", errors="replace")
    return {
        "isequiv_O_inverts_steps": text.count("isequiv_O_inverts"),
        "O_functor_occurrences": text.count("O_functor"),
        "contains_first_nested_obligation": "O_inverts O (O_functor O f)" in text,
        "contains_second_nested_obligation": (
            "O_inverts O (O_functor O (O_functor O f))" in text
        ),
        "line_count": len(text.splitlines()),
    }


def _semantic_result(
    probes: list[dict[str, object]], inventory: dict[str, object]
) -> dict[str, object]:
    classes = {row["probe_id"]: row["classification"] for row in probes}
    expected = {
        "P01-DEFAULT-NO-REGISTRATION": "EXPECTED_PROOF_SEARCH_FAILURE",
        "P02-COMMENTED-HINT-IMMEDIATE": "EXPECTED_PROOF_SEARCH_FAILURE",
        "P03-EXISTING-INSTANCE": "EXPECTED_OBSERVATION_LIMIT",
        "P04-HINT-RESOLVE": "EXPECTED_OBSERVATION_LIMIT",
        "P05-BOUNDED-SEARCH-DEPTH": "EXPECTED_SEARCH_DEPTH_LIMIT",
        "P06-KNOWN-EQUIVALENCE": "KERNEL_ACCEPTED",
        "P07-GENERIC-TYPECLASS-RECURSION": "EXPECTED_OBSERVATION_LIMIT",
        "P08-BOUNDED-RECURSION-TRACE": "EXPECTED_SEARCH_DEPTH_LIMIT",
    }
    if classes != expected:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_SEMANTIC_PROBE_SET_INVALID")
    trace_row = next(row for row in probes if row["probe_id"] == "P08-BOUNDED-RECURSION-TRACE")
    trace = trace_row["trace_signature"]
    if (
        trace["isequiv_O_inverts_steps"] < 2
        or trace["O_functor_occurrences"] < 4
        or not trace["contains_first_nested_obligation"]
        or not trace["contains_second_nested_obligation"]
    ):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_TRACE_SIGNATURE_INVALID")
    return {
        "phenomenon_layer": "TYPECLASS_PROOF_SEARCH",
        "community_source": {
            "documents_recursive_search_boundary": True,
            "active_isequiv_O_inverts_registration_count": inventory[
                "active_registration_count"
            ],
            "default_goal_result": "FINITE_SEARCH_FAILURE",
            "commented_hint_immediate_current_result": "FINITE_SEARCH_FAILURE",
            "ordinary_instance_registration_result": "OBSERVATION_LIMIT_REACHED",
            "hint_resolve_registration_result": "OBSERVATION_LIMIT_REACHED",
        },
        "causal_controls": {
            "bounded_depth": "FINITE_LIMIT_REJECTION",
            "known_equivalence": "COMPLETED",
            "generic_recursive_instance_system": "OBSERVATION_LIMIT_REACHED",
            "bounded_trace": trace,
        },
        "qualification": {
            "N0_OBSERVATION_LIMIT": "PASS",
            "N1_CAUSAL_CONTROLS": "PASS",
            "N2_ORDINARY_CONFIGURATION": "FAIL_RULE_NOT_REGISTERED_BY_LIBRARY",
            "N3_HOTT_ESSENTIALITY": "FAIL_GENERIC_ABLATION_REPRODUCES",
            "N4_NATURAL_CONSUMER": "PARTIAL_AUTHOR_DOCUMENTED_DISABLED_BOUNDARY",
            "N5_REALITY_CORRESPONDENCE": "FAIL_NOT_SPECIFIED",
            "N6_MACHINE_PROVED_CLAIM": "FAIL_EXECUTION_EVIDENCE_ONLY",
        },
        "direction_b_status": "ASK_LIKE_DESIGN_GUARD_PRESENT_NOT_BYPASSED",
        "candidate_scope": "COMMUNITY_HOTT_AUTOMATION_RECURSION_BOUNDARY",
        "hott_nonreality_status": "NOT_ESTABLISHED",
        "hott_bug_status": "NOT_ESTABLISHED",
        "godel_status": "NO_OBJECT_LANGUAGE_OR_PROVABILITY_PREDICATE",
        "natural_enabled_consumers": [],
        "semantic_limit": (
            "The observation concerns unbounded typeclass proof search after a rule that the "
            "library deliberately leaves unregistered is registered by the probe.  The same "
            "shape is reproduced without HoTT, while a known equivalence and an explicit depth "
            "bound complete.  No kernel-checking non-completion, reality correspondence, or "
            "Gödel construction follows."
        ),
    }


def run(
    scope_path: Path,
    freeze_path: Path,
    decisions_path: Path,
    run_id: str,
) -> dict[str, object]:
    root = repo_root()
    if not re.fullmatch(r"[A-Z0-9][A-Z0-9._-]{2,127}", run_id):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_RUN_ID_INVALID")
    scope_path = scope_path.resolve()
    freeze_path = freeze_path.resolve()
    decisions_path = decisions_path.resolve()
    evaluator = Path(__file__).resolve()
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    freeze_value = _load_bound(
        root, freeze_path, FREEZE_SCHEMA, scope_path, evaluator
    )
    decisions_value = _load_bound(
        root, decisions_path, DECISIONS_SCHEMA, scope_path, evaluator
    )
    if decisions_value["deterministic"].get("freeze") != _pin(root, freeze_path):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_DECISIONS_FREEZE_CHANGED")
    output = _under(
        root
        / "machine-overview/evaluations/COQ-HOTT-REFLECTIVE-TYPECLASS-RECURSION-001/runs"
        / run_id,
        root,
        "run-root",
    )
    if output.exists():
        raise MachineOverviewError(f"COQ_HOTT_TYPECLASS_RUN_EXISTS:{run_id}")
    output.mkdir(parents=True)

    probes: list[dict[str, object]] = []
    observations: list[dict[str, object]] = []
    for row in scope["probe_plan"]:
        first_attempt, first_argv = _prepare_attempt(
            root, scope, validated, row, run_id, "first"
        )
        replay_attempt, replay_argv = _prepare_attempt(
            root, scope, validated, row, run_id, "replay"
        )
        first_raw = _execute(first_argv, row["timeout_seconds"] + 20)
        replay_raw = _execute(replay_argv, row["timeout_seconds"] + 20)
        first_class = _classify(
            row, first_raw["exit_code"], first_raw["stdout"], first_raw["stderr"]
        )
        replay_class = _classify(
            row,
            replay_raw["exit_code"],
            replay_raw["stdout"],
            replay_raw["stderr"],
        )
        probe_base = output / "probes" / row["probe_id"]
        first = _write_attempt(
            root, probe_base, "first", first_argv, first_raw, first_class
        )
        replay = _write_attempt(
            root, probe_base, "replay", replay_argv, replay_raw, replay_class
        )
        exact = (
            first_raw["exit_code"] == replay_raw["exit_code"]
            and first_raw["stdout"] == replay_raw["stdout"]
            and first_raw["stderr"] == replay_raw["stderr"]
        )
        probe = {
            "probe_id": row["probe_id"],
            "source": _pin(
                root,
                _under(
                    root / safe_relative(row["future_path"]),
                    root,
                    row["probe_id"],
                ),
            ),
            "expect": row["expect"],
            "classification": first_class,
            "expectation_met": first_class != "UNEXPECTED_RESULT",
            "exact_replay": exact and first_class == replay_class,
            "first": first,
            "replay": replay,
        }
        if row.get("trace"):
            probe["trace_signature"] = _trace_signature(first_raw["stdout"])
        probes.append(probe)
        observations.append(
            {
                "probe_id": row["probe_id"],
                "first_duration_ms": first_raw["duration_ms"],
                "replay_duration_ms": replay_raw["duration_ms"],
                "first_attempt_root": str(first_attempt),
                "replay_attempt_root": str(replay_attempt),
            }
        )
    if not all(row["expectation_met"] and row["exact_replay"] for row in probes):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_PROBE_RESULT_INVALID")
    semantic = _semantic_result(
        probes, decisions_value["deterministic"]["registration_inventory"]
    )
    deterministic = {
        "evaluation_id": scope["evaluation_id"],
        "run_id": run_id,
        "scope": _pin(root, scope_path),
        "freeze": _pin(root, freeze_path),
        "freeze_deterministic_sha256": freeze_value["deterministic_sha256"],
        "decisions": _pin(root, decisions_path),
        "decisions_deterministic_sha256": decisions_value["deterministic_sha256"],
        "evaluator": _pin(root, evaluator),
        "source_identity": validated["source_identity"],
        "build_identity": validated["build_identity"],
        "docker": validated["docker"],
        "probes": probes,
        "semantic": semantic,
    }
    value = {
        "schema_version": RUN_SCHEMA,
        "generated_at_utc": utc_now(),
        "run_id": run_id,
        "git": git_state(root),
        "observations": observations,
        "deterministic": deterministic,
        "deterministic_sha256": sha256_bytes(json_bytes(deterministic)),
    }
    write_json(output / "RUN.json", value)
    return {
        "status": "COQ_HOTT_TYPECLASS_RECURSION_RUN_COMPLETE",
        "run_id": run_id,
        "probe_count": len(probes),
        "candidate_scope": semantic["candidate_scope"],
        "hott_nonreality_status": semantic["hott_nonreality_status"],
        "godel_status": semantic["godel_status"],
        "deterministic_sha256": value["deterministic_sha256"],
    }


def _read_attempt(
    root: Path, row: dict, label: str
) -> tuple[int, bytes, bytes, list[str]]:
    attempt = row[label]
    for key in ("command", "stdout", "stderr"):
        _verify_pin(root, attempt[key], [], f"{row['probe_id']}.{label}.{key}")
    command = read_json(root / safe_relative(attempt["command"]["path"]))
    stdout = (root / safe_relative(attempt["stdout"]["path"])).read_bytes()
    stderr = (root / safe_relative(attempt["stderr"]["path"])).read_bytes()
    return int(attempt["exit_code"]), stdout, stderr, command["argv"]


def _next_verify_generation(attempt_root: Path, run_id: str) -> str:
    for value in range(1, 1000):
        generation = f"{value:03d}"
        if not (attempt_root / f"verify-{run_id}-{generation}").exists():
            return generation
    raise MachineOverviewError("COQ_HOTT_TYPECLASS_VERIFY_GENERATION_EXHAUSTED")


def verify(run_path: Path, rerun: bool) -> dict[str, object]:
    root = repo_root()
    run_path = run_path.resolve()
    value = read_json(run_path)
    if value.get("schema_version") != RUN_SCHEMA:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_RUN_SCHEMA_INVALID")
    deterministic = value.get("deterministic")
    if sha256_bytes(json_bytes(deterministic)) != value.get("deterministic_sha256"):
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_RUN_DIGEST_CHANGED")
    scope_path = root / safe_relative(deterministic["scope"]["path"])
    freeze_path = root / safe_relative(deterministic["freeze"]["path"])
    decisions_path = root / safe_relative(deterministic["decisions"]["path"])
    evaluator = Path(__file__).resolve()
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    freeze_value = _load_bound(
        root, freeze_path, FREEZE_SCHEMA, scope_path, evaluator
    )
    decisions_value = _load_bound(
        root, decisions_path, DECISIONS_SCHEMA, scope_path, evaluator
    )
    if freeze_value["deterministic_sha256"] != deterministic[
        "freeze_deterministic_sha256"
    ]:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_RUN_FREEZE_BINDING_CHANGED")
    if decisions_value["deterministic_sha256"] != deterministic[
        "decisions_deterministic_sha256"
    ]:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_RUN_DECISIONS_BINDING_CHANGED")
    if _anchor_checks(scope, validated) != decisions_value["deterministic"][
        "anchor_checks"
    ]:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_ANCHOR_REPLAY_CHANGED")
    if _registration_inventory(validated["source_root"]) != decisions_value[
        "deterministic"
    ]["registration_inventory"]:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_INVENTORY_REPLAY_CHANGED")

    plan = {row["probe_id"]: row for row in scope["probe_plan"]}
    recomputed: list[dict[str, object]] = []
    rerun_rows: list[dict[str, object]] = []
    generation = (
        _next_verify_generation(validated["attempt_root"], value["run_id"])
        if rerun
        else None
    )
    for stored in deterministic["probes"]:
        probe_id = stored["probe_id"]
        row = plan[probe_id]
        _verify_pin(root, stored["source"], [], f"{probe_id}.source")
        first_exit, first_stdout, first_stderr, _ = _read_attempt(
            root, stored, "first"
        )
        replay_exit, replay_stdout, replay_stderr, _ = _read_attempt(
            root, stored, "replay"
        )
        classification = _classify(row, first_exit, first_stdout, first_stderr)
        replay_class = _classify(row, replay_exit, replay_stdout, replay_stderr)
        exact = (
            first_exit == replay_exit
            and first_stdout == replay_stdout
            and first_stderr == replay_stderr
        )
        current = {
            **stored,
            "classification": classification,
            "expectation_met": classification != "UNEXPECTED_RESULT",
            "exact_replay": exact and classification == replay_class,
        }
        if row.get("trace"):
            current["trace_signature"] = _trace_signature(first_stdout)
        if current != stored:
            raise MachineOverviewError(
                f"COQ_HOTT_TYPECLASS_PROBE_RECEIPT_CHANGED:{probe_id}"
            )
        recomputed.append(current)
        if rerun:
            _, argv = _prepare_attempt(
                root,
                scope,
                validated,
                row,
                value["run_id"],
                "rerun",
                generation,
            )
            actual = _execute(argv, row["timeout_seconds"] + 20)
            actual_class = _classify(
                row, actual["exit_code"], actual["stdout"], actual["stderr"]
            )
            exact_recorded = (
                actual["exit_code"] == first_exit
                and actual["stdout"] == first_stdout
                and actual["stderr"] == first_stderr
            )
            if actual_class != classification or not exact_recorded:
                raise MachineOverviewError(
                    f"COQ_HOTT_TYPECLASS_NATIVE_RERUN_CHANGED:{probe_id}"
                )
            rerun_rows.append(
                {
                    "probe_id": probe_id,
                    "classification": actual_class,
                    "exact_recorded_output": exact_recorded,
                }
            )
    semantic = _semantic_result(
        recomputed, decisions_value["deterministic"]["registration_inventory"]
    )
    if semantic != deterministic["semantic"]:
        raise MachineOverviewError("COQ_HOTT_TYPECLASS_SEMANTIC_REPLAY_CHANGED")
    return {
        "status": "COQ_HOTT_TYPECLASS_RECURSION_VALID",
        "run_id": value["run_id"],
        "probe_count": len(recomputed),
        "candidate_scope": semantic["candidate_scope"],
        "hott_nonreality_status": semantic["hott_nonreality_status"],
        "hott_bug_status": semantic["hott_bug_status"],
        "godel_status": semantic["godel_status"],
        "rerun": rerun,
        "rerun_generation": generation,
        "rerun_results": rerun_rows,
        "deterministic_sha256": value["deterministic_sha256"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    freeze_parser = sub.add_parser("freeze")
    freeze_parser.add_argument("--scope", type=Path, required=True)
    freeze_parser.add_argument("--output", type=Path, required=True)
    decide_parser = sub.add_parser("decide")
    decide_parser.add_argument("--scope", type=Path, required=True)
    decide_parser.add_argument("--freeze", type=Path, required=True)
    decide_parser.add_argument("--output", type=Path, required=True)
    run_parser = sub.add_parser("run")
    run_parser.add_argument("--scope", type=Path, required=True)
    run_parser.add_argument("--freeze", type=Path, required=True)
    run_parser.add_argument("--decisions", type=Path, required=True)
    run_parser.add_argument("--run-id", required=True)
    verify_parser = sub.add_parser("verify")
    verify_parser.add_argument("--run", type=Path, required=True)
    verify_parser.add_argument("--rerun", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "freeze":
            result = freeze(args.scope, args.output)
        elif args.command == "decide":
            result = decide(args.scope, args.freeze, args.output)
        elif args.command == "run":
            result = run(args.scope, args.freeze, args.decisions, args.run_id)
        else:
            result = verify(args.run, args.rerun)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (
        MachineOverviewError,
        OSError,
        ValueError,
        TypeError,
        KeyError,
        json.JSONDecodeError,
        subprocess.SubprocessError,
    ) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
