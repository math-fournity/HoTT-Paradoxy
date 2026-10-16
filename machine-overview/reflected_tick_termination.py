#!/usr/bin/env python3
"""Replay Reflection/tick observations and proof-checking termination controls.

This evaluator keeps four propositions separate:

* a macro can inspect the normal form of syntax supplied at one call site;
* an object-level function must respect a Path between its arguments;
* a proof-checking process can fail to complete after termination checking has
  been explicitly overridden; and
* that controlled non-completion does not by itself establish a HoTT-specific
  paradox or an internal Gödel instance.

The native probes and bounded search are research evidence.  They do not add a
claim to the project's mathematical claim matrix.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
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


SCOPE_SCHEMA = "machine-overview-reflected-tick-termination-scope/v1"
FREEZE_SCHEMA = "machine-overview-reflected-tick-termination-freeze/v1"
DECISIONS_SCHEMA = "machine-overview-reflected-tick-termination-decisions/v1"
RUN_SCHEMA = "machine-overview-reflected-tick-termination-run/v1"
QUESTION_IDS = [f"R{i}" for i in range(1, 9)] + [f"N{i}" for i in range(1, 7)]
EXPECTATIONS = {"ACCEPT", "TYPE_REJECTION", "OBSERVATION_LIMIT"}
ANNOTATION_RE = re.compile(
    r"^\s*\{-#\s+(TERMINATING|NON_TERMINATING|NO_TERMINATION_CHECK)"
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
            f"REFLECTED_TICK_PATH_OUTSIDE_ROOT:{label}:{path}"
        ) from exc
    return resolved


def _resolve(root: Path, value: str, allowed_roots: list[Path], label: str) -> Path:
    raw = Path(value)
    if raw.is_absolute():
        for allowed in allowed_roots:
            try:
                return _under(raw, allowed, label)
            except MachineOverviewError:
                continue
        raise MachineOverviewError(
            f"REFLECTED_TICK_EXTERNAL_PATH_NOT_ALLOWED:{label}:{value}"
        )
    return _under(root / safe_relative(value), root, label)


def _pin(root: Path, path: Path) -> dict[str, object]:
    resolved = path.resolve()
    try:
        value = resolved.relative_to(root.resolve()).as_posix()
    except ValueError:
        value = str(resolved)
    if not resolved.is_file() or resolved.is_symlink():
        raise MachineOverviewError(f"REFLECTED_TICK_PIN_FILE_INVALID:{value}")
    return {
        "path": value,
        "bytes": resolved.stat().st_size,
        "sha256": sha256_file(resolved),
    }


def _allowed_roots(scope: dict) -> list[Path]:
    roots = [Path(value).resolve() for value in scope.get("allowed_external_roots", [])]
    if not roots or any(not path.is_dir() or path.is_symlink() for path in roots):
        raise MachineOverviewError("REFLECTED_TICK_ALLOWED_ROOT_INVALID")
    return roots


def _verify_pin(
    root: Path, row: dict, allowed_roots: list[Path], label: str
) -> Path:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise MachineOverviewError(f"REFLECTED_TICK_PIN_INVALID:{label}")
    path = _resolve(root, row["path"], allowed_roots, label)
    if (
        not path.is_file()
        or path.is_symlink()
        or path.stat().st_size != row.get("bytes")
        or sha256_file(path) != row.get("sha256")
    ):
        raise MachineOverviewError(
            f"REFLECTED_TICK_PIN_CHANGED:{label}:{row.get('path')}"
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
            f"REFLECTED_TICK_DOCKER_IMAGE_UNAVAILABLE:{image}"
        )
    rows = json.loads(completed.stdout)
    if not isinstance(rows, list) or len(rows) != 1:
        raise MachineOverviewError("REFLECTED_TICK_DOCKER_IDENTITY_INVALID")
    row = rows[0]
    return {
        "id": row.get("Id"),
        "architecture": row.get("Architecture"),
        "os": row.get("Os"),
        "repo_digests": sorted(row.get("RepoDigests") or []),
    }


def validate_scope(root: Path, scope: dict) -> dict[str, object]:
    if scope.get("schema_version") != SCOPE_SCHEMA:
        raise MachineOverviewError("REFLECTED_TICK_SCOPE_SCHEMA_INVALID")
    if [row.get("id") for row in scope.get("questions", [])] != QUESTION_IDS:
        raise MachineOverviewError("REFLECTED_TICK_QUESTION_ROSTER_INVALID")
    allowed = _allowed_roots(scope)

    artifacts: dict[str, dict[str, object]] = {}
    source_ids: set[str] = set()
    for source in scope.get("sources", []):
        source_id = source.get("source_id")
        if not isinstance(source_id, str) or source_id in source_ids:
            raise MachineOverviewError("REFLECTED_TICK_SOURCE_ID_INVALID")
        source_ids.add(source_id)
        for artifact in source.get("artifacts", []):
            artifact_id = artifact.get("artifact_id")
            if not isinstance(artifact_id, str) or artifact_id in artifacts:
                raise MachineOverviewError("REFLECTED_TICK_ARTIFACT_ID_INVALID")
            path = _verify_pin(root, artifact, allowed, artifact_id)
            artifacts[artifact_id] = {"row": artifact, "path": path}

    trees: dict[str, dict[str, object]] = {}
    for row in scope.get("trees", []):
        tree_id = row.get("tree_id")
        if not isinstance(tree_id, str) or tree_id in trees:
            raise MachineOverviewError("REFLECTED_TICK_TREE_ID_INVALID")
        path = _resolve(root, row.get("path", ""), allowed, tree_id)
        actual = deterministic_tree(path)
        if actual != row.get("identity"):
            raise MachineOverviewError(f"REFLECTED_TICK_TREE_CHANGED:{tree_id}")
        if row.get("role") not in {"PRODUCTION", "CHECKER_TEST", "CHECKER_EXAMPLE"}:
            raise MachineOverviewError(f"REFLECTED_TICK_TREE_ROLE_INVALID:{tree_id}")
        trees[tree_id] = {"row": row, "path": path, "identity": actual}

    plan = scope.get("probe_plan", [])
    probe_ids = [row.get("probe_id") for row in plan]
    if not plan or len(probe_ids) != len(set(probe_ids)):
        raise MachineOverviewError("REFLECTED_TICK_PROBE_ROSTER_INVALID")
    for row in plan:
        if row.get("expect") not in EXPECTATIONS:
            raise MachineOverviewError(
                f"REFLECTED_TICK_PROBE_EXPECT_INVALID:{row.get('probe_id')}"
            )
        if not isinstance(row.get("timeout_seconds"), int) or row["timeout_seconds"] < 1:
            raise MachineOverviewError(
                f"REFLECTED_TICK_PROBE_TIMEOUT_INVALID:{row.get('probe_id')}"
            )
        if row.get("future_path") not in scope.get("future_paths", []):
            raise MachineOverviewError(
                f"REFLECTED_TICK_PROBE_PATH_UNDECLARED:{row.get('probe_id')}"
            )
        if row["expect"] == "TYPE_REJECTION" and not row.get("diagnostic"):
            raise MachineOverviewError(
                f"REFLECTED_TICK_PROBE_DIAGNOSTIC_MISSING:{row.get('probe_id')}"
            )

    tool = scope.get("toolchain", {})
    binary = _verify_pin(root, tool.get("binary", {}), allowed, "toolchain.binary")
    compiler_root = _resolve(
        root, tool.get("compiler_root", ""), allowed, "toolchain.compiler_root"
    )
    guarded_root = _resolve(
        root, tool.get("guarded_root", ""), allowed, "toolchain.guarded_root"
    )
    docker = tool.get("docker", {})
    actual_docker = _docker_identity(docker.get("image", ""))
    if actual_docker != docker.get("identity"):
        raise MachineOverviewError("REFLECTED_TICK_DOCKER_IMAGE_CHANGED")
    return {
        "allowed_roots": allowed,
        "artifacts": artifacts,
        "trees": trees,
        "binary": binary,
        "compiler_root": compiler_root,
        "guarded_root": guarded_root,
        "docker": actual_docker,
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
        raise MachineOverviewError(f"REFLECTED_TICK_BOUND_SCHEMA_INVALID:{path}")
    deterministic = value.get("deterministic")
    if not isinstance(deterministic, dict):
        raise MachineOverviewError(f"REFLECTED_TICK_BOUND_DETERMINISTIC_MISSING:{path}")
    if sha256_bytes(json_bytes(deterministic)) != value.get("deterministic_sha256"):
        raise MachineOverviewError(f"REFLECTED_TICK_BOUND_DIGEST_CHANGED:{path}")
    if scope_path is not None:
        expected = deterministic.get("scope")
        if expected != _pin(root, scope_path):
            raise MachineOverviewError(f"REFLECTED_TICK_SCOPE_BINDING_CHANGED:{path}")
    if evaluator_path is not None:
        expected = deterministic.get("evaluator")
        if expected != _pin(root, evaluator_path):
            raise MachineOverviewError(f"REFLECTED_TICK_EVALUATOR_BINDING_CHANGED:{path}")
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
        raise MachineOverviewError(f"REFLECTED_TICK_FREEZE_EXISTS:{output}")
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    for value in scope.get("future_paths", []):
        path = _under(root / safe_relative(value), root, "future-path")
        if path.exists():
            raise MachineOverviewError(f"REFLECTED_TICK_FUTURE_PATH_EXISTS:{value}")
    prechecks = [
        _run_precheck(root, [sys.executable, "machine-overview/mo.py", "selftest"], 120),
        _run_precheck(root, [sys.executable, "machine-overview/mo.py", "validate"], 60),
    ]
    if any(row["exit_code"] != 0 for row in prechecks):
        raise MachineOverviewError("REFLECTED_TICK_PREFREEZE_CHECK_FAILED")
    deterministic = {
        "evaluation_id": scope["evaluation_id"],
        "freeze_id": scope["freeze_id"],
        "scope": _pin(root, scope_path),
        "evaluator": _pin(root, Path(__file__)),
        "source_artifacts": len(validated["artifacts"]),
        "source_trees": [
            {
                "tree_id": key,
                "path": row["row"]["path"],
                "role": row["row"]["role"],
                "identity": row["identity"],
            }
            for key, row in sorted(validated["trees"].items())
        ],
        "docker": validated["docker"],
        "probe_plan": scope["probe_plan"],
        "qualification_gates": scope["qualification_gates"],
        "trigger_cube": scope["trigger_cube"],
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
        "status": "REFLECTED_TICK_FREEZE_CREATED",
        "path": str(output),
        "deterministic_sha256": value["deterministic_sha256"],
    }


def _artifact_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise MachineOverviewError(f"REFLECTED_TICK_TEXT_READ_FAILED:{path}") from exc


def _anchor_checks(scope: dict, validated: dict[str, object]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for source in scope["sources"]:
        for artifact in source["artifacts"]:
            artifact_id = artifact["artifact_id"]
            text = _artifact_text(validated["artifacts"][artifact_id]["path"])
            for anchor in artifact.get("anchors", []):
                literal = anchor["literal"]
                count = text.count(literal)
                rows.append(
                    {
                        "source_id": source["source_id"],
                        "artifact_id": artifact_id,
                        "anchor_id": anchor["anchor_id"],
                        "literal_sha256": sha256_bytes(literal.encode("utf-8")),
                        "occurrences": count,
                        "found": count >= anchor.get("minimum", 1),
                    }
                )
    return rows


def _source_file(path: Path) -> bool:
    return ".agda" in path.name or ".lagda" in path.name


def _termination_inventory(validated: dict[str, object]) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for tree_id, data in sorted(validated["trees"].items()):
        rows: list[dict[str, object]] = []
        root = data["path"]
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.is_symlink() or not _source_file(path):
                continue
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except UnicodeError:
                continue
            for line_no, line in enumerate(lines, 1):
                match = ANNOTATION_RE.search(line)
                if match:
                    rows.append(
                        {
                            "path": path.relative_to(root).as_posix(),
                            "line": line_no,
                            "annotation": match.group(1),
                            "line_sha256": sha256_bytes(line.encode("utf-8")),
                        }
                    )
        result.append(
            {
                "tree_id": tree_id,
                "role": data["row"]["role"],
                "tree_identity": data["identity"],
                "matches": len(rows),
                "files_with_matches": len({row["path"] for row in rows}),
                "by_annotation": {
                    name: sum(row["annotation"] == name for row in rows)
                    for name in (
                        "TERMINATING",
                        "NON_TERMINATING",
                        "NO_TERMINATION_CHECK",
                    )
                },
                "rows": rows,
            }
        )
    return result


def decide(
    scope_path: Path, freeze_path: Path, output: Path
) -> dict[str, object]:
    root = repo_root()
    scope_path = scope_path.resolve()
    freeze_path = freeze_path.resolve()
    output = output.resolve()
    if output.exists():
        raise MachineOverviewError(f"REFLECTED_TICK_DECISIONS_EXIST:{output}")
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
            "REFLECTED_TICK_SOURCE_ANCHOR_MISSING:" + ",".join(missing)
        )
    inventory = _termination_inventory(validated)
    inventory_by_id = {row["tree_id"]: row for row in inventory}
    for row in scope["trees"]:
        actual = inventory_by_id[row["tree_id"]]["matches"]
        expected = row.get("expected_annotation_matches")
        if expected is not None and actual != expected:
            raise MachineOverviewError(
                f"REFLECTED_TICK_ANNOTATION_INVENTORY_CHANGED:{row['tree_id']}:{actual}:{expected}"
            )
    probe_rows = []
    for row in scope["probe_plan"]:
        source = _under(root / safe_relative(row["future_path"]), root, row["probe_id"])
        probe_rows.append({**row, "source": _pin(root, source)})
    deterministic = {
        "evaluation_id": scope["evaluation_id"],
        "freeze": _pin(root, freeze_path),
        "freeze_deterministic_sha256": freeze_value["deterministic_sha256"],
        "scope": _pin(root, scope_path),
        "evaluator": _pin(root, evaluator),
        "anchor_checks": anchors,
        "all_anchors_found": True,
        "termination_annotation_inventory": inventory,
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
        "status": "REFLECTED_TICK_DECISIONS_CREATED",
        "path": str(output),
        "anchors": len(anchors),
        "deterministic_sha256": value["deterministic_sha256"],
    }


def _probe_command(
    root: Path,
    scope: dict,
    validated: dict[str, object],
    row: dict,
) -> list[str]:
    source = _under(root / safe_relative(row["future_path"]), root, row["probe_id"])
    probe_root = (root / "machine-overview/evaluations/REFLECTED-TICK-REDUCTION-OBSERVER-001/probes").resolve()
    source = _under(source, probe_root, row["probe_id"])
    tool = scope["toolchain"]
    docker = tool["docker"]
    binary = validated["binary"]
    return [
        "docker",
        "run",
        "--rm",
        "--network",
        "none",
        "--platform",
        docker["platform"],
        "-e",
        "Agda_datadir=/agda-source/src/data",
        "-v",
        f"{binary.parent}:/tool:ro",
        "-v",
        f"{validated['compiler_root']}:/agda-source",
        "-v",
        f"{validated['guarded_root']}:/guarded",
        "-v",
        f"{probe_root}:/probes",
        "-w",
        "/guarded/src",
        docker["image"],
        "/usr/bin/timeout",
        f"{row['timeout_seconds']}s",
        f"/tool/{binary.name}",
        "--ignore-interfaces",
        "--no-libraries",
        "-i",
        "/guarded/src",
        "-i",
        "/probes",
        "/probes/" + source.relative_to(probe_root).as_posix(),
    ]


def _classify(row: dict, exit_code: int, stdout: bytes, stderr: bytes) -> str:
    output = (stdout + b"\n" + stderr).decode("utf-8", errors="replace")
    if row["expect"] == "ACCEPT" and exit_code == 0:
        return "KERNEL_ACCEPTED"
    if (
        row["expect"] == "TYPE_REJECTION"
        and exit_code == row.get("expected_exit", 42)
        and row["diagnostic"] in output
    ):
        return "EXPECTED_TYPE_REJECTION"
    if row["expect"] == "OBSERVATION_LIMIT" and exit_code == 124:
        return "EXPECTED_OBSERVATION_LIMIT"
    return "UNEXPECTED_RESULT"


def _execute(argv: list[str], host_timeout: int) -> dict[str, object]:
    started = time.monotonic()
    try:
        completed = subprocess.run(
            argv, capture_output=True, timeout=host_timeout
        )
    except subprocess.TimeoutExpired as exc:
        raise MachineOverviewError("REFLECTED_TICK_HOST_TIMEOUT") from exc
    return {
        "exit_code": completed.returncode,
        "stdout": completed.stdout,
        "stderr": completed.stderr,
        "duration_ms": round((time.monotonic() - started) * 1000),
    }


def _write_probe_attempt(
    root: Path,
    base: Path,
    label: str,
    argv: list[str],
    result: dict[str, object],
    classification: str,
) -> dict[str, object]:
    folder = base / label
    folder.mkdir(parents=True, exist_ok=False)
    command = {
        "argv": argv,
        "cwd": str(root),
        "network": "none",
        "observation_limit_seconds": int(argv[argv.index("/usr/bin/timeout") + 1][:-1]),
    }
    write_json(folder / "command.json", command)
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


def _semantic_result(probes: list[dict[str, object]]) -> dict[str, object]:
    classes = {row["probe_id"]: row["classification"] for row in probes}
    expected = {
        "P01-REFLECTION-REDUCTION-CLASSIFICATION": "KERNEL_ACCEPTED",
        "P02-PATH-INDEXED-OBSERVATION-CLAIM": "EXPECTED_TYPE_REJECTION",
        "P03-REFLECTED-BINDER-RECONSTRUCTION": "KERNEL_ACCEPTED",
        "P04-TERMINATION-CHECK-REJECTS-LOOP": "EXPECTED_TYPE_REJECTION",
        "P05-CERTIFIED-FRAGMENT-REJECTS-OVERRIDE": "EXPECTED_TYPE_REJECTION",
        "P06-TERMINATION-OVERRIDE-ACCEPTS-SELF-EQUALITY": "KERNEL_ACCEPTED",
        "P07-TERMINATION-OVERRIDE-FORCED-EQUALITY": "EXPECTED_OBSERVATION_LIMIT",
        "P08-OPAQUE-RECURSIVE-EQUALITY": "EXPECTED_TYPE_REJECTION",
        "P09-GUARDED-INFINITE-NORMALISATION": "KERNEL_ACCEPTED",
        "P10-REFLECTION-NORMALISES-RECURSIVE-TERM": "EXPECTED_OBSERVATION_LIMIT",
    }
    if classes != expected:
        raise MachineOverviewError("REFLECTED_TICK_SEMANTIC_PROBE_SET_INVALID")
    return {
        "reflection": {
            "call_site_syntax_split": True,
            "uniform_object_observer_preserves_path": True,
            "uniform_object_observer_retains_split": False,
            "path_indexed_reification": "TYPE_REJECTED_TRUE_FALSE_BOUNDARY",
            "tick_and_forcing_binders_reconstructed": True,
            "verdict": "HOST_SYNTAX_OBSERVATION_WITH_OBJECT_LEVEL_CONGRUENCE_FENCE",
        },
        "termination": {
            "ordinary_recursion_check": "REJECTED",
            "certified_fragment_override": "REJECTED",
            "declared_recursive_self_equality": "ACCEPTED_WITHOUT_FORCED_NORMAL_FORM",
            "declared_recursive_forced_equality": "OBSERVATION_LIMIT_REACHED",
            "opaque_recursive_equality": "TYPE_REJECTED_WITHOUT_UNFOLDING",
            "guarded_productive_infinite_object": "NORMALISATION_COMPLETED_AT_DELAY_BOUNDARY",
            "reflection_forced_recursive_normalisation": "OBSERVATION_LIMIT_REACHED",
            "verdict": "EXPLICIT_TERMINATION_ASSERTION_CAN_MAKE_PROOF_CHECKING_NOT_COMPLETE",
        },
        "trigger_cube": {
            "full_conjunction": [
                "SELF_RECURSIVE_TERM",
                "TERM_DECLARED_AVAILABLE_TO_JUDGEMENTAL_REDUCTION",
                "PROOF_CHECK_FORCES_A_DISTINCT_NORMAL_FORM",
            ],
            "full_result": "OBSERVATION_LIMIT_REACHED",
            "ablations": [
                {"removed": "SELF_RECURSIVE_TERM", "probe": "P09", "result": "COMPLETED"},
                {"removed": "TERM_DECLARED_AVAILABLE_TO_JUDGEMENTAL_REDUCTION", "probe": "P08", "result": "TYPE_REJECTED"},
                {"removed": "PROOF_CHECK_FORCES_A_DISTINCT_NORMAL_FORM", "probe": "P06", "result": "COMPLETED"},
            ],
        },
        "natural_usage_mismatches": [],
        "hott_godel_instances": [],
        "candidate_scope": "REPRESENTATION_BOUNDARY_AND_TERMINATION_CALIBRATION",
        "hott_nonreality_status": "NOT_ESTABLISHED",
        "godel_status": "GENERIC_SELF_REDUCTION_CALIBRATION_ONLY",
        "semantic_limit": (
            "The non-completing checks require an explicit source annotation that "
            "overrides termination analysis.  The guarded infinite control completes, "
            "and Reflection does not turn its call-site distinction into one Path-respecting "
            "object function."
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
        raise MachineOverviewError("REFLECTED_TICK_RUN_ID_INVALID")
    scope_path = scope_path.resolve()
    freeze_path = freeze_path.resolve()
    decisions_path = decisions_path.resolve()
    evaluator = Path(__file__).resolve()
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    freeze_value = _load_bound(root, freeze_path, FREEZE_SCHEMA, scope_path, evaluator)
    decisions_value = _load_bound(root, decisions_path, DECISIONS_SCHEMA, scope_path, evaluator)
    if decisions_value["deterministic"].get("freeze") != _pin(root, freeze_path):
        raise MachineOverviewError("REFLECTED_TICK_DECISIONS_FREEZE_CHANGED")
    run_root = _under(
        root / "machine-overview/evaluations/REFLECTED-TICK-REDUCTION-OBSERVER-001/runs",
        root,
        "run-root",
    )
    output = run_root / run_id
    if output.exists():
        raise MachineOverviewError(f"REFLECTED_TICK_RUN_EXISTS:{run_id}")
    output.mkdir(parents=True)

    probes: list[dict[str, object]] = []
    observations: list[dict[str, object]] = []
    for row in scope["probe_plan"]:
        argv = _probe_command(root, scope, validated, row)
        probe_base = output / "probes" / row["probe_id"]
        first_raw = _execute(argv, row["timeout_seconds"] + 20)
        first_class = _classify(
            row, first_raw["exit_code"], first_raw["stdout"], first_raw["stderr"]
        )
        replay_raw = _execute(argv, row["timeout_seconds"] + 20)
        replay_class = _classify(
            row, replay_raw["exit_code"], replay_raw["stdout"], replay_raw["stderr"]
        )
        first = _write_probe_attempt(
            root, probe_base, "first", argv, first_raw, first_class
        )
        replay = _write_probe_attempt(
            root, probe_base, "replay", argv, replay_raw, replay_class
        )
        exact = (
            first_raw["exit_code"] == replay_raw["exit_code"]
            and first_raw["stdout"] == replay_raw["stdout"]
            and first_raw["stderr"] == replay_raw["stderr"]
        )
        probes.append(
            {
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
        )
        observations.append(
            {
                "probe_id": row["probe_id"],
                "first_duration_ms": first_raw["duration_ms"],
                "replay_duration_ms": replay_raw["duration_ms"],
            }
        )
    if not all(row["expectation_met"] and row["exact_replay"] for row in probes):
        raise MachineOverviewError("REFLECTED_TICK_PROBE_RESULT_INVALID")

    semantic = _semantic_result(probes)
    deterministic = {
        "evaluation_id": scope["evaluation_id"],
        "run_id": run_id,
        "scope": _pin(root, scope_path),
        "freeze": _pin(root, freeze_path),
        "freeze_deterministic_sha256": freeze_value["deterministic_sha256"],
        "decisions": _pin(root, decisions_path),
        "decisions_deterministic_sha256": decisions_value["deterministic_sha256"],
        "evaluator": _pin(root, evaluator),
        "source_count": len(scope["sources"]),
        "artifact_count": len(validated["artifacts"]),
        "anchor_count": len(decisions_value["deterministic"]["anchor_checks"]),
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
        "status": "REFLECTED_TICK_TERMINATION_RUN_COMPLETE",
        "run_id": run_id,
        "probe_count": len(probes),
        "hott_nonreality_status": semantic["hott_nonreality_status"],
        "godel_status": semantic["godel_status"],
        "deterministic_sha256": value["deterministic_sha256"],
    }


def _read_attempt(root: Path, row: dict, label: str) -> tuple[int, bytes, bytes, list[str]]:
    attempt = row[label]
    for key in ("command", "stdout", "stderr"):
        _verify_pin(root, attempt[key], [], f"{row['probe_id']}.{label}.{key}")
    command = read_json(root / safe_relative(attempt["command"]["path"]))
    stdout = (root / safe_relative(attempt["stdout"]["path"])).read_bytes()
    stderr = (root / safe_relative(attempt["stderr"]["path"])).read_bytes()
    return int(attempt["exit_code"]), stdout, stderr, command["argv"]


def verify(run_path: Path, rerun: bool) -> dict[str, object]:
    root = repo_root()
    run_path = run_path.resolve()
    value = read_json(run_path)
    if value.get("schema_version") != RUN_SCHEMA:
        raise MachineOverviewError("REFLECTED_TICK_RUN_SCHEMA_INVALID")
    deterministic = value.get("deterministic")
    if sha256_bytes(json_bytes(deterministic)) != value.get("deterministic_sha256"):
        raise MachineOverviewError("REFLECTED_TICK_RUN_DIGEST_CHANGED")
    scope_path = root / safe_relative(deterministic["scope"]["path"])
    freeze_path = root / safe_relative(deterministic["freeze"]["path"])
    decisions_path = root / safe_relative(deterministic["decisions"]["path"])
    evaluator = Path(__file__).resolve()
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    freeze_value = _load_bound(root, freeze_path, FREEZE_SCHEMA, scope_path, evaluator)
    decisions_value = _load_bound(root, decisions_path, DECISIONS_SCHEMA, scope_path, evaluator)
    if freeze_value["deterministic_sha256"] != deterministic["freeze_deterministic_sha256"]:
        raise MachineOverviewError("REFLECTED_TICK_RUN_FREEZE_BINDING_CHANGED")
    if decisions_value["deterministic_sha256"] != deterministic["decisions_deterministic_sha256"]:
        raise MachineOverviewError("REFLECTED_TICK_RUN_DECISIONS_BINDING_CHANGED")
    if _anchor_checks(scope, validated) != decisions_value["deterministic"]["anchor_checks"]:
        raise MachineOverviewError("REFLECTED_TICK_ANCHOR_REPLAY_CHANGED")
    if _termination_inventory(validated) != decisions_value["deterministic"]["termination_annotation_inventory"]:
        raise MachineOverviewError("REFLECTED_TICK_INVENTORY_REPLAY_CHANGED")

    plan = {row["probe_id"]: row for row in scope["probe_plan"]}
    recomputed: list[dict[str, object]] = []
    rerun_rows: list[dict[str, object]] = []
    for stored in deterministic["probes"]:
        probe_id = stored["probe_id"]
        row = plan[probe_id]
        _verify_pin(root, stored["source"], [], f"{probe_id}.source")
        first_exit, first_stdout, first_stderr, argv = _read_attempt(root, stored, "first")
        replay_exit, replay_stdout, replay_stderr, replay_argv = _read_attempt(root, stored, "replay")
        classification = _classify(row, first_exit, first_stdout, first_stderr)
        replay_class = _classify(row, replay_exit, replay_stdout, replay_stderr)
        if argv != replay_argv:
            raise MachineOverviewError(f"REFLECTED_TICK_COMMAND_REPLAY_CHANGED:{probe_id}")
        exact = (
            first_exit == replay_exit
            and first_stdout == replay_stdout
            and first_stderr == replay_stderr
        )
        current = {**stored, "classification": classification, "expectation_met": classification != "UNEXPECTED_RESULT", "exact_replay": exact and classification == replay_class}
        if current != stored:
            raise MachineOverviewError(f"REFLECTED_TICK_PROBE_RECEIPT_CHANGED:{probe_id}")
        recomputed.append(current)
        if rerun:
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
                raise MachineOverviewError(f"REFLECTED_TICK_NATIVE_RERUN_CHANGED:{probe_id}")
            rerun_rows.append(
                {
                    "probe_id": probe_id,
                    "classification": actual_class,
                    "exact_recorded_output": exact_recorded,
                }
            )
    if _semantic_result(recomputed) != deterministic["semantic"]:
        raise MachineOverviewError("REFLECTED_TICK_SEMANTIC_REPLAY_CHANGED")
    return {
        "status": "REFLECTED_TICK_REDUCTION_TERMINATION_VALID",
        "run_id": value["run_id"],
        "probe_count": len(recomputed),
        "reflection_verdict": deterministic["semantic"]["reflection"]["verdict"],
        "termination_verdict": deterministic["semantic"]["termination"]["verdict"],
        "hott_nonreality_status": deterministic["semantic"]["hott_nonreality_status"],
        "godel_status": deterministic["semantic"]["godel_status"],
        "rerun": rerun,
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
    except (MachineOverviewError, OSError, ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
