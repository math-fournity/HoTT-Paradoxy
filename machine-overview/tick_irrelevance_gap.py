#!/usr/bin/env python3
"""Replay the CCTT tick-irrelevance / operational-reduction boundary.

The evaluator keeps three claims separate:

* a forcing tick can trigger judgemental computation;
* tick irrelevance supplies paths at the extensional level; and
* a path is not, by itself, a certificate that both endpoints reduce in the
  same way at the same stage.

It also performs a finite, complete equality-graph search for the smallest
conditional contradiction obtained by internalising an operational tick
observer.  The search and native probes are exploratory evidence.  They do
not create a project mathematical claim or establish a HoTT defect.
"""
from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import platform
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


SCOPE_SCHEMA = "machine-overview-tick-operational-gap-scope/v1"
DECISIONS_SCHEMA = "machine-overview-tick-operational-gap-decisions/v1"
FREEZE_SCHEMA = "machine-overview-tick-operational-gap-freeze/v1"
RUN_SCHEMA = "machine-overview-tick-operational-gap-run/v1"
QUESTION_IDS = [f"G{i}" for i in range(1, 9)]
DECISION_STATUSES = {"PASS", "PARTIAL", "FAIL", "NOT_APPLICABLE"}


class _VisibleText(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.hidden = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style"}:
            self.hidden += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style"} and self.hidden:
            self.hidden -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden:
            self.parts.append(data)


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
        raise MachineOverviewError(f"TICK_GAP_PATH_OUTSIDE_ROOT:{label}:{path}") from exc
    return resolved


def _resolve(root: Path, value: str, allowed_roots: list[Path], label: str) -> Path:
    raw = Path(value)
    if raw.is_absolute():
        for allowed in allowed_roots:
            try:
                return _under(raw, allowed, label)
            except MachineOverviewError:
                continue
        raise MachineOverviewError(f"TICK_GAP_EXTERNAL_PATH_NOT_ALLOWED:{label}:{value}")
    return _under(root / safe_relative(value), root, label)


def _pin(root: Path, path: Path) -> dict:
    resolved = path.resolve()
    try:
        value = resolved.relative_to(root.resolve()).as_posix()
    except ValueError:
        value = str(resolved)
    if not resolved.is_file() or resolved.is_symlink():
        raise MachineOverviewError(f"TICK_GAP_PIN_FILE_INVALID:{value}")
    return {"path": value, "bytes": resolved.stat().st_size, "sha256": sha256_file(resolved)}


def _verify_pin(root: Path, row: dict, allowed_roots: list[Path], label: str) -> Path:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise MachineOverviewError(f"TICK_GAP_PIN_INVALID:{label}")
    path = _resolve(root, row["path"], allowed_roots, label)
    if (
        not path.is_file()
        or path.is_symlink()
        or path.stat().st_size != row.get("bytes")
        or sha256_file(path) != row.get("sha256")
    ):
        raise MachineOverviewError(f"TICK_GAP_PIN_CHANGED:{label}:{row.get('path')}")
    return path


def _normalise(data: bytes, kind: str) -> str | None:
    if kind == "binary":
        return None
    value = data.decode("utf-8", errors="strict")
    if kind == "html":
        parser = _VisibleText()
        parser.feed(value)
        value = " ".join(parser.parts)
    return " ".join(html.unescape(value).split())


def _allowed_roots(scope: dict) -> list[Path]:
    roots = [Path(value).resolve() for value in scope.get("allowed_external_roots", [])]
    if not roots or any(not path.is_dir() or path.is_symlink() for path in roots):
        raise MachineOverviewError("TICK_GAP_ALLOWED_ROOT_INVALID")
    return roots


def _docker_identity(image: str) -> dict:
    completed = subprocess.run(
        ["docker", "image", "inspect", image], capture_output=True, text=True, timeout=30,
    )
    if completed.returncode != 0:
        raise MachineOverviewError(f"TICK_GAP_DOCKER_IMAGE_UNAVAILABLE:{image}")
    rows = json.loads(completed.stdout)
    if not isinstance(rows, list) or len(rows) != 1:
        raise MachineOverviewError("TICK_GAP_DOCKER_IMAGE_IDENTITY_INVALID")
    row = rows[0]
    return {
        "id": row.get("Id"),
        "architecture": row.get("Architecture"),
        "os": row.get("Os"),
        "repo_digests": sorted(row.get("RepoDigests") or []),
    }


def validate_scope(root: Path, scope: dict) -> dict:
    if scope.get("schema_version") != SCOPE_SCHEMA:
        raise MachineOverviewError("TICK_GAP_SCOPE_SCHEMA_INVALID")
    if [row.get("id") for row in scope.get("questions", [])] != QUESTION_IDS:
        raise MachineOverviewError("TICK_GAP_QUESTION_ROSTER_INVALID")
    allowed = _allowed_roots(scope)
    source_ids = [row.get("source_id") for row in scope.get("sources", [])]
    if not source_ids or len(source_ids) != len(set(source_ids)):
        raise MachineOverviewError("TICK_GAP_SOURCE_ROSTER_INVALID")
    artifacts: dict[str, dict] = {}
    for source in scope["sources"]:
        for row in source.get("artifacts", []):
            artifact_id = row.get("artifact_id")
            if not isinstance(artifact_id, str) or artifact_id in artifacts:
                raise MachineOverviewError(f"TICK_GAP_ARTIFACT_ID_INVALID:{artifact_id}")
            path = _verify_pin(root, row, allowed, artifact_id)
            artifacts[artifact_id] = {
                "row": row,
                "path": path,
                "normalised": _normalise(path.read_bytes(), row.get("kind", "text")),
            }
    trees = []
    for index, row in enumerate(scope.get("trees", [])):
        path = _resolve(root, row.get("path", ""), allowed, f"tree.{index}")
        actual = deterministic_tree(path)
        if actual != row.get("identity"):
            raise MachineOverviewError(f"TICK_GAP_TREE_CHANGED:{row.get('tree_id')}")
        trees.append({"tree_id": row["tree_id"], "path": str(path), "identity": actual})
    graph = scope.get("search_graph", {})
    vertices = graph.get("vertices", [])
    assumptions = graph.get("assumptions", [])
    if len(vertices) != len(set(vertices)) or not vertices:
        raise MachineOverviewError("TICK_GAP_SEARCH_VERTICES_INVALID")
    assumption_ids = [row.get("id") for row in assumptions]
    if len(assumption_ids) != len(set(assumption_ids)) or not assumption_ids:
        raise MachineOverviewError("TICK_GAP_SEARCH_ASSUMPTIONS_INVALID")
    if any(row.get("left") not in vertices or row.get("right") not in vertices for row in assumptions):
        raise MachineOverviewError("TICK_GAP_SEARCH_ENDPOINT_INVALID")
    target = graph.get("target", {})
    if target.get("left") not in vertices or target.get("right") not in vertices:
        raise MachineOverviewError("TICK_GAP_SEARCH_TARGET_INVALID")
    gate = scope.get("natural_usage_gate")
    if not isinstance(gate, dict) or not gate.get("required_conditions"):
        raise MachineOverviewError("TICK_GAP_NATURAL_USAGE_GATE_INVALID")
    probe_plan = scope.get("probe_plan", [])
    probe_ids = [row.get("probe_id") for row in probe_plan]
    if not probe_plan or len(probe_ids) != len(set(probe_ids)):
        raise MachineOverviewError("TICK_GAP_PROBE_PLAN_INVALID")
    if any(row.get("runner") not in {"host_agda", "forcing_agda"} for row in probe_plan):
        raise MachineOverviewError("TICK_GAP_PROBE_PLAN_RUNNER_INVALID")
    if any(row.get("expect") not in {"ACCEPT", "TYPE_REJECTION"} for row in probe_plan):
        raise MachineOverviewError("TICK_GAP_PROBE_PLAN_EXPECT_INVALID")
    for row in probe_plan:
        locators = [key for key in ("future_path", "artifact_id") if row.get(key)]
        if len(locators) != 1:
            raise MachineOverviewError(f"TICK_GAP_PROBE_PLAN_SOURCE_INVALID:{row.get('probe_id')}")
        if row.get("future_path") and row["future_path"] not in scope.get("future_paths", []):
            raise MachineOverviewError(f"TICK_GAP_PROBE_FUTURE_PATH_UNDECLARED:{row.get('probe_id')}")
        if row.get("artifact_id") and row["artifact_id"] not in artifacts:
            raise MachineOverviewError(f"TICK_GAP_PROBE_ARTIFACT_UNKNOWN:{row.get('probe_id')}")
    docker = scope.get("toolchains", {}).get("forcing_agda", {}).get("docker", {})
    if docker:
        actual = _docker_identity(docker.get("image", ""))
        if actual != docker.get("identity"):
            raise MachineOverviewError("TICK_GAP_DOCKER_IMAGE_CHANGED")
    return {"allowed_roots": allowed, "artifacts": artifacts, "trees": trees}


def _edge_rows(graph: dict, removed: set[str] | None = None) -> list[dict]:
    removed = removed or set()
    rows = []
    for assumption in graph["assumptions"]:
        if assumption["id"] in removed:
            continue
        rows.append({
            "edge_id": assumption["id"],
            "left": assumption["left"],
            "right": assumption["right"],
            "orientation": "forward",
        })
        rows.append({
            "edge_id": assumption["id"],
            "left": assumption["right"],
            "right": assumption["left"],
            "orientation": "symmetric",
        })
    return rows


def _search_paths(graph: dict, removed: set[str] | None = None, reverse_order: bool = False) -> list[dict]:
    edges = _edge_rows(graph, removed)
    edges.sort(key=lambda row: (row["edge_id"], row["orientation"], row["left"], row["right"]), reverse=reverse_order)
    start = graph["target"]["left"]
    finish = graph["target"]["right"]
    maximum = graph["max_edges"]
    found: list[dict] = []

    def visit(vertex: str, path: list[dict], visited: set[str]) -> None:
        if vertex == finish:
            found.append({
                "edge_count": len(path),
                "steps": [dict(row) for row in path],
                "witness": " ; ".join(
                    ("sym " if row["orientation"] == "symmetric" else "") + row["edge_id"]
                    for row in path
                ),
            })
            return
        if len(path) >= maximum:
            return
        for edge in edges:
            if edge["left"] != vertex or edge["right"] in visited:
                continue
            visit(edge["right"], path + [edge], visited | {edge["right"]})

    visit(start, [], {start})
    canonical = {
        json.dumps(row, ensure_ascii=False, sort_keys=True): row
        for row in found
    }
    return sorted(canonical.values(), key=lambda row: (row["edge_count"], row["witness"]))


def equality_search(scope: dict) -> dict:
    graph = scope["search_graph"]
    paths = _search_paths(graph)
    shuffled = _search_paths(graph, reverse_order=True)
    canonical = [json.dumps(row, ensure_ascii=False, sort_keys=True) for row in paths]
    shuffled_canonical = [json.dumps(row, ensure_ascii=False, sort_keys=True) for row in shuffled]
    ablations = []
    for assumption_id in graph["required_assumptions"]:
        values = _search_paths(graph, {assumption_id})
        ablations.append({"removed": assumption_id, "target_paths": len(values)})
    if not paths:
        raise MachineOverviewError("TICK_GAP_SEARCH_TARGET_NOT_FOUND")
    if canonical != shuffled_canonical:
        raise MachineOverviewError("TICK_GAP_SEARCH_ORDER_DEPENDENT")
    if any(row["target_paths"] != 0 for row in ablations):
        raise MachineOverviewError("TICK_GAP_SEARCH_ABLATION_FAILED")
    return {
        "vertices": graph["vertices"],
        "assumption_count": len(graph["assumptions"]),
        "directed_edge_count": len(_edge_rows(graph)),
        "max_edges": graph["max_edges"],
        "target": graph["target"],
        "target_paths": len(paths),
        "minimal_edge_count": paths[0]["edge_count"],
        "minimal_witnesses": [row for row in paths if row["edge_count"] == paths[0]["edge_count"]],
        "order_independent": True,
        "ablations": ablations,
        "interpretation": (
            "The graph search is complete only for the frozen equality-composition grammar. "
            "It derives a conditional observer collision; it does not assert that CCTT contains such an observer."
        ),
    }


def source_inventory(scope: dict, validated: dict) -> dict:
    patterns = {
        key: re.compile(value)
        for key, value in scope.get("inventory_patterns", {}).items()
    }
    results = {}
    for tree in validated["trees"]:
        tree_root = Path(tree["path"])
        matches = {key: [] for key in patterns}
        scanned_files = 0
        for path in sorted(tree_root.rglob("*")):
            if not path.is_file() or path.is_symlink() or path.suffix not in {".agda", ".hs", ".md"}:
                continue
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except UnicodeDecodeError:
                continue
            scanned_files += 1
            relative = path.relative_to(tree_root).as_posix()
            for line_number, line in enumerate(lines, 1):
                for key, pattern in patterns.items():
                    count = len(pattern.findall(line))
                    if count:
                        matches[key].append({
                            "path": relative,
                            "line": line_number,
                            "text": line.rstrip(),
                            "count": count,
                        })
        results[tree["tree_id"]] = {
            "scanned_files": scanned_files,
            "patterns": {
                key: {
                    "matching_lines": len(rows),
                    "occurrences": sum(row["count"] for row in rows),
                    "files": len({row["path"] for row in rows}),
                    "matches": rows,
                }
                for key, rows in matches.items()
            },
        }
    return results


def candidate_signature(scope: dict, inventory: dict) -> dict:
    rows = []
    for requirement in scope.get("candidate_signature", {}).get("requirements", []):
        tree_id = requirement["tree_id"]
        pattern_id = requirement["pattern_id"]
        try:
            stats = inventory[tree_id]["patterns"][pattern_id]
        except KeyError as exc:
            raise MachineOverviewError(
                f"TICK_GAP_SIGNATURE_LOCATOR_INVALID:{requirement.get('id')}"
            ) from exc
        actual = stats[requirement.get("metric", "occurrences")]
        minimum = requirement["minimum"]
        rows.append({
            "id": requirement["id"],
            "tree_id": tree_id,
            "pattern_id": pattern_id,
            "metric": requirement.get("metric", "occurrences"),
            "minimum": minimum,
            "actual": actual,
            "matched": actual >= minimum,
        })
    if not rows:
        raise MachineOverviewError("TICK_GAP_SIGNATURE_EMPTY")
    return {
        "requirements": rows,
        "complete": all(row["matched"] for row in rows),
        "interpretation": (
            "This conjunction detects the frozen source shape: an operational tick split and diamond-only "
            "fixed-point reduction coexist with path-level tick irrelevance. It does not decide semantic misuse."
        ),
    }


def validate_decisions(root: Path, scope: dict, decisions: dict, validated: dict) -> dict:
    if decisions.get("schema_version") != DECISIONS_SCHEMA:
        raise MachineOverviewError("TICK_GAP_DECISIONS_SCHEMA_INVALID")
    if decisions.get("evaluation_id") != scope.get("evaluation_id"):
        raise MachineOverviewError("TICK_GAP_EVALUATION_ID_MISMATCH")
    rows = decisions.get("sources", [])
    expected_sources = [row["source_id"] for row in scope["sources"]]
    if [row.get("source_id") for row in rows] != expected_sources:
        raise MachineOverviewError("TICK_GAP_DECISION_SOURCE_ROSTER_MISMATCH")
    anchor_checks = []
    for source in rows:
        answers = source.get("answers", {})
        if list(answers) != QUESTION_IDS:
            raise MachineOverviewError(f"TICK_GAP_QUESTION_COVERAGE_INVALID:{source['source_id']}")
        for question_id, answer in answers.items():
            if answer.get("status") not in DECISION_STATUSES:
                raise MachineOverviewError(f"TICK_GAP_DECISION_STATUS_INVALID:{source['source_id']}:{question_id}")
            evidence = answer.get("evidence", [])
            if not evidence:
                raise MachineOverviewError(f"TICK_GAP_DECISION_EVIDENCE_MISSING:{source['source_id']}:{question_id}")
            for evidence_row in evidence:
                artifact = validated["artifacts"].get(evidence_row.get("artifact_id"))
                if artifact is None or artifact["normalised"] is None:
                    raise MachineOverviewError(f"TICK_GAP_EVIDENCE_ARTIFACT_INVALID:{evidence_row.get('artifact_id')}")
                for anchor in evidence_row.get("anchors", []):
                    normalised = " ".join(html.unescape(anchor).split())
                    found = normalised in artifact["normalised"]
                    anchor_checks.append({
                        "source_id": source["source_id"],
                        "question": question_id,
                        "artifact_id": evidence_row["artifact_id"],
                        "anchor_sha256": sha256_bytes(normalised.encode("utf-8")),
                        "found": found,
                    })
                    if not found:
                        raise MachineOverviewError(
                            f"TICK_GAP_EVIDENCE_ANCHOR_MISSING:{source['source_id']}:{question_id}:{evidence_row['artifact_id']}"
                        )
    probe_ids = [row.get("probe_id") for row in decisions.get("probes", [])]
    if not probe_ids or len(probe_ids) != len(set(probe_ids)):
        raise MachineOverviewError("TICK_GAP_PROBE_ROSTER_INVALID")
    for index, row in enumerate(decisions["probes"]):
        _verify_pin(root, row.get("source"), validated["allowed_roots"], f"probe.{row['probe_id']}")
        if row.get("runner") not in {"host_agda", "forcing_agda"}:
            raise MachineOverviewError(f"TICK_GAP_PROBE_RUNNER_INVALID:{row['probe_id']}")
        if row.get("expect") not in {"ACCEPT", "TYPE_REJECTION"}:
            raise MachineOverviewError(f"TICK_GAP_PROBE_EXPECT_INVALID:{row['probe_id']}")
        plan_row = scope["probe_plan"][index]
        expected_path = plan_row.get("future_path")
        if plan_row.get("artifact_id"):
            expected_path = validated["artifacts"][plan_row["artifact_id"]]["row"]["path"]
        if row["source"].get("path") != expected_path:
            raise MachineOverviewError(f"TICK_GAP_PROBE_SOURCE_CHANGED:{row['probe_id']}")
    frozen_plan = [
        {key: row.get(key) for key in (
            "probe_id", "runner", "purpose", "expect", "diagnostic", "expected_exit", "future_path", "artifact_id",
        )}
        for row in scope["probe_plan"]
    ]
    decision_plan = [
        {
            **{key: row.get(key) for key in ("probe_id", "runner", "purpose", "expect", "diagnostic", "expected_exit")},
            "future_path": scope["probe_plan"][index].get("future_path"),
            "artifact_id": scope["probe_plan"][index].get("artifact_id"),
        }
        for index, row in enumerate(decisions["probes"])
    ]
    if decision_plan != frozen_plan:
        raise MachineOverviewError("TICK_GAP_PROBE_PLAN_CHANGED")
    consumers = decisions.get("consumer_promotions", [])
    consumer_ids = [row.get("consumer_id") for row in consumers]
    if not consumers or len(consumer_ids) != len(set(consumer_ids)):
        raise MachineOverviewError("TICK_GAP_CONSUMER_ROSTER_INVALID")
    allowed_classes = {
        "PATH_ONLY", "JUDGEMENTAL_COMPUTATION", "NO_PROMOTION", "OPERATIONAL_PROMOTION",
    }
    for row in consumers:
        if row.get("classification") not in allowed_classes:
            raise MachineOverviewError(f"TICK_GAP_CONSUMER_CLASSIFICATION_INVALID:{row.get('consumer_id')}")
        artifact = validated["artifacts"].get(row.get("artifact_id"))
        if artifact is None or artifact["normalised"] is None or not row.get("anchors"):
            raise MachineOverviewError(f"TICK_GAP_CONSUMER_EVIDENCE_INVALID:{row.get('consumer_id')}")
        for anchor in row["anchors"]:
            normalised = " ".join(html.unescape(anchor).split())
            found = normalised in artifact["normalised"]
            anchor_checks.append({
                "source_id": "CONSUMER-REVIEW",
                "question": row["consumer_id"],
                "artifact_id": row["artifact_id"],
                "anchor_sha256": sha256_bytes(normalised.encode("utf-8")),
                "found": found,
            })
            if not found:
                raise MachineOverviewError(f"TICK_GAP_CONSUMER_ANCHOR_MISSING:{row['consumer_id']}")
    return {"anchor_checks": anchor_checks, "all_anchors_found": all(row["found"] for row in anchor_checks)}


def _standard_agda(root: Path, scope: dict) -> tuple[str, str, str]:
    toolchain = read_json(root / safe_relative(scope["toolchains"]["host_agda"]["config_path"]))
    return (
        toolchain["agda"]["local_binary"],
        str(root / toolchain["project_library_registry"]),
        toolchain["cubical_library"]["local_root"],
    )


def _probe_command(root: Path, scope: dict, validated: dict, row: dict) -> list[str]:
    source = _verify_pin(root, row["source"], validated["allowed_roots"], f"probe-command.{row['probe_id']}")
    if row["runner"] == "host_agda":
        binary, library_file, cubical_root = _standard_agda(root, scope)
        return [
            binary,
            "--ignore-interfaces",
            "--guardedness",
            "--library-file", library_file,
            "-i", cubical_root,
            "-i", str(source.parent),
            str(source),
        ]
    forcing = scope["toolchains"]["forcing_agda"]
    docker = forcing["docker"]
    binary = _resolve(root, forcing["binary"]["path"], validated["allowed_roots"], "forcing-binary")
    guarded = _resolve(root, forcing["guarded_root"], validated["allowed_roots"], "guarded-root")
    compiler_root = _resolve(root, forcing["compiler_root"], validated["allowed_roots"], "compiler-root")
    probe_root = (root / "machine-overview/evaluations/TICK-IRRELEVANCE-OPERATIONAL-GAP-001/probes").resolve()
    if source.is_relative_to(guarded):
        container_source = "/guarded/" + source.relative_to(guarded).as_posix()
    elif source.is_relative_to(probe_root):
        container_source = "/probes/" + source.relative_to(probe_root).as_posix()
    else:
        raise MachineOverviewError(f"TICK_GAP_FORCING_SOURCE_ROOT_INVALID:{source}")
    return [
        "docker", "run", "--rm", "--network", "none", "--platform", docker["platform"],
        "-e", "Agda_datadir=/agda-source/src/data",
        "-v", f"{binary.parent}:/tool:ro",
        "-v", f"{compiler_root}:/agda-source",
        "-v", f"{guarded}:/guarded",
        "-v", f"{probe_root}:/probes",
        "-w", "/guarded/src",
        docker["image"],
        f"/tool/{binary.name}",
        "--ignore-interfaces", "--no-libraries", "-i", "/guarded/src", "-i", "/probes", container_source,
    ]


def _classify(row: dict, exit_code: int, stdout: bytes, stderr: bytes) -> dict:
    value = (stdout + b"\n" + stderr).decode("utf-8", errors="replace")
    if row["expect"] == "ACCEPT":
        met = exit_code == 0
        classification = "KERNEL_ACCEPTED" if met else "UNEXPECTED_REJECTION"
    else:
        marker = row.get("diagnostic", "")
        met = exit_code == row.get("expected_exit", 42) and marker in value
        classification = "EXPECTED_TYPE_REJECTION" if met else "UNEXPECTED_REJECTION_DIAGNOSTIC"
    return {"classification": classification, "expectation_met": met}


def _run_once(root: Path, run_dir: Path, scope: dict, validated: dict, row: dict, stage: str) -> dict:
    command = _probe_command(root, scope, validated, row)
    started = utc_now()
    began = time.monotonic()
    completed = subprocess.run(command, cwd=root, capture_output=True, timeout=row.get("timeout_seconds", 300))
    duration = time.monotonic() - began
    classification = _classify(row, completed.returncode, completed.stdout, completed.stderr)
    target = run_dir / "probes" / row["probe_id"] / stage
    command_data = json_bytes({"command_argv": command, "cwd": str(root)})
    environment_data = (
        f"platform={platform.platform()}\npython={platform.python_version()}\n"
        f"runner={row['runner']}\n"
    ).encode("utf-8")
    write_bytes(target / "stdout.txt", completed.stdout)
    write_bytes(target / "stderr.txt", completed.stderr)
    write_bytes(target / "command.json", command_data)
    write_bytes(target / "environment.txt", environment_data)
    return {
        "started_at_utc": started,
        "duration_seconds": duration,
        "command_argv": command,
        "cwd": str(root),
        "exit_code": completed.returncode,
        **classification,
        "artifacts": {
            "stdout": {"path": f"probes/{row['probe_id']}/{stage}/stdout.txt", "bytes": len(completed.stdout), "sha256": sha256_bytes(completed.stdout)},
            "stderr": {"path": f"probes/{row['probe_id']}/{stage}/stderr.txt", "bytes": len(completed.stderr), "sha256": sha256_bytes(completed.stderr)},
            "command": {"path": f"probes/{row['probe_id']}/{stage}/command.json", "bytes": len(command_data), "sha256": sha256_bytes(command_data)},
            "environment": {"path": f"probes/{row['probe_id']}/{stage}/environment.txt", "bytes": len(environment_data), "sha256": sha256_bytes(environment_data)},
        },
    }


def _probe_pair(root: Path, run_dir: Path, scope: dict, validated: dict, row: dict) -> dict:
    first = _run_once(root, run_dir, scope, validated, row, "first")
    replay = _run_once(root, run_dir, scope, validated, row, "replay")
    exact = (
        first["exit_code"] == replay["exit_code"]
        and first["artifacts"]["stdout"]["sha256"] == replay["artifacts"]["stdout"]["sha256"]
        and first["artifacts"]["stderr"]["sha256"] == replay["artifacts"]["stderr"]["sha256"]
    )
    return {
        "probe_id": row["probe_id"],
        "runner": row["runner"],
        "purpose": row["purpose"],
        "expect": row["expect"],
        "source": row["source"],
        "first": first,
        "replay": replay,
        "replay_classification": "EXACT_EXIT_STDOUT_STDERR_MATCH" if exact else "REPLAY_MISMATCH",
        "accepted": first["expectation_met"] and replay["expectation_met"] and exact,
    }


def _freeze(root: Path, scope_path: Path, output_path: Path) -> dict:
    if output_path.exists():
        raise MachineOverviewError("TICK_GAP_FREEZE_ALREADY_EXISTS")
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    existing = [value for value in scope["future_paths"] if (root / safe_relative(value)).exists()]
    if existing:
        raise MachineOverviewError(f"TICK_GAP_FUTURE_PATH_EXISTS:{existing[0]}")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    checks = []
    for label, command in (
        ("selftest", [sys.executable, "machine-overview/mo.py", "selftest"]),
        ("validate", [sys.executable, "machine-overview/mo.py", "validate"]),
    ):
        completed = subprocess.run(command, cwd=root, capture_output=True, timeout=360)
        stdout_path = output_path.parent / f"pre-{label}-stdout.txt"
        stderr_path = output_path.parent / f"pre-{label}-stderr.txt"
        write_bytes(stdout_path, completed.stdout)
        write_bytes(stderr_path, completed.stderr)
        if completed.returncode != 0:
            raise MachineOverviewError(f"TICK_GAP_FREEZE_{label.upper()}_FAILED")
        checks.append({
            "label": label,
            "command_argv": command,
            "exit_code": completed.returncode,
            "stdout": _pin(root, stdout_path),
            "stderr": _pin(root, stderr_path),
        })
    result = {
        "schema_version": FREEZE_SCHEMA,
        "freeze_id": scope["freeze_id"],
        "created_at_utc": utc_now(),
        "evaluator": _pin(root, Path(__file__).resolve()),
        "scope": _pin(root, scope_path),
        "source_artifacts": len(validated["artifacts"]),
        "source_trees": validated["trees"],
        "questions": scope["questions"],
        "search_graph": scope["search_graph"],
        "candidate_signature": scope["candidate_signature"],
        "probe_plan": scope["probe_plan"],
        "natural_usage_gate": scope["natural_usage_gate"],
        "future_paths": scope["future_paths"],
        "future_paths_absent": True,
        "pre_checks": checks,
        "git": git_state(root),
        "interpretation": (
            "Source identities, G1-G8, the equality-search grammar, probe purposes and expected result classes "
            "were frozen before final probe sources, decisions or run receipts existed. This is a same-designer "
            "pre-registration, not blind evaluation or novelty evidence."
        ),
    }
    write_json(output_path, result)
    return result


def _validate_freeze(root: Path, scope: dict, freeze_row: dict, validated: dict) -> dict:
    freeze_path = _verify_pin(root, freeze_row, validated["allowed_roots"], "freeze")
    freeze = read_json(freeze_path)
    if freeze.get("schema_version") != FREEZE_SCHEMA:
        raise MachineOverviewError("TICK_GAP_FREEZE_SCHEMA_INVALID")
    _verify_pin(root, freeze.get("evaluator"), validated["allowed_roots"], "freeze.evaluator")
    _verify_pin(root, freeze.get("scope"), validated["allowed_roots"], "freeze.scope")
    if (
        freeze.get("questions") != scope.get("questions")
        or freeze.get("search_graph") != scope.get("search_graph")
        or freeze.get("candidate_signature") != scope.get("candidate_signature")
        or freeze.get("probe_plan") != scope.get("probe_plan")
        or freeze.get("natural_usage_gate") != scope.get("natural_usage_gate")
    ):
        raise MachineOverviewError("TICK_GAP_FREEZE_SEMANTICS_CHANGED")
    return freeze


def _run(root: Path, scope_path: Path, decisions_path: Path, output_path: Path, run_id: str) -> dict:
    if output_path.exists() or output_path.parent.exists():
        raise MachineOverviewError("TICK_GAP_RUN_ALREADY_EXISTS")
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    decisions = read_json(decisions_path)
    freeze = _validate_freeze(root, scope, decisions["freeze"], validated)
    decision_checks = validate_decisions(root, scope, decisions, validated)
    search = equality_search(scope)
    inventory = source_inventory(scope, validated)
    signature = candidate_signature(scope, inventory)
    output_path.parent.mkdir(parents=True, exist_ok=False)
    probes = [_probe_pair(root, output_path.parent, scope, validated, row) for row in decisions["probes"]]
    all_probes = all(row["accepted"] for row in probes)
    consumer_promotions = decisions.get("consumer_promotions", [])
    natural_mismatches = [row for row in consumer_promotions if row.get("classification") == "OPERATIONAL_PROMOTION"]
    verdict = (
        "EXTENSIONAL_TICK_IRRELEVANCE_WITH_METALEVEL_OPERATIONAL_SPLIT"
        if all_probes and search["target_paths"] and signature["complete"] and not natural_mismatches
        else "TICK_OPERATIONAL_GAP_REVIEW_REQUIRED"
    )
    deterministic = {
        "evaluation_id": scope["evaluation_id"],
        "freeze_id": freeze["freeze_id"],
        "scope": _pin(root, scope_path),
        "decisions": _pin(root, decisions_path),
        "source_count": len(scope["sources"]),
        "artifact_count": len(validated["artifacts"]),
        "anchor_checks": decision_checks["anchor_checks"],
        "all_anchors_found": decision_checks["all_anchors_found"],
        "equality_search": search,
        "source_inventory": inventory,
        "candidate_signature": signature,
        "consumer_promotions": consumer_promotions,
        "natural_usage_mismatches": natural_mismatches,
        "probes": probes,
        "all_probes_match_expectation_and_exact_replay": all_probes,
        "verdict": verdict,
        "candidate_scope": "REPRESENTATION_BOUNDARY",
        "hott_bug_status": "NOT_ESTABLISHED",
        "semantic_limit": (
            "CCTT distinguishes operational tick forms in syntax and reduction while using paths for extensional "
            "reasoning. The finite search proves only a conditional observer collision in its frozen grammar. "
            "No fixed-source consumer was judged to turn Path equality into judgemental reduction."
        ),
    }
    payload = {
        "schema_version": RUN_SCHEMA,
        "run_id": run_id,
        "generated_at_utc": utc_now(),
        "evaluator": _pin(root, Path(__file__).resolve()),
        "deterministic": deterministic,
        "deterministic_sha256": sha256_bytes(json_bytes(deterministic)),
        "git": git_state(root),
    }
    write_json(output_path, payload)
    return payload


def _verify_artifacts(run_dir: Path, probe: dict) -> None:
    for stage in ("first", "replay"):
        for label, row in probe[stage]["artifacts"].items():
            path = run_dir / row["path"]
            if not path.is_file() or path.stat().st_size != row["bytes"] or sha256_file(path) != row["sha256"]:
                raise MachineOverviewError(f"TICK_GAP_RUN_ARTIFACT_CHANGED:{probe['probe_id']}:{stage}:{label}")


def _verify(root: Path, run_path: Path, rerun: bool) -> dict:
    payload = read_json(run_path)
    if payload.get("schema_version") != RUN_SCHEMA:
        raise MachineOverviewError("TICK_GAP_RUN_SCHEMA_INVALID")
    deterministic = payload["deterministic"]
    scope_path = root / safe_relative(deterministic["scope"]["path"])
    decisions_path = root / safe_relative(deterministic["decisions"]["path"])
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    _verify_pin(root, payload.get("evaluator"), validated["allowed_roots"], "run.evaluator")
    decisions = read_json(decisions_path)
    _validate_freeze(root, scope, decisions["freeze"], validated)
    decision_checks = validate_decisions(root, scope, decisions, validated)
    if equality_search(scope) != deterministic["equality_search"]:
        raise MachineOverviewError("TICK_GAP_SEARCH_REPLAY_MISMATCH")
    if source_inventory(scope, validated) != deterministic["source_inventory"]:
        raise MachineOverviewError("TICK_GAP_INVENTORY_REPLAY_MISMATCH")
    if candidate_signature(scope, deterministic["source_inventory"]) != deterministic["candidate_signature"]:
        raise MachineOverviewError("TICK_GAP_SIGNATURE_REPLAY_MISMATCH")
    if decisions.get("consumer_promotions", []) != deterministic["consumer_promotions"]:
        raise MachineOverviewError("TICK_GAP_CONSUMER_DECISIONS_CHANGED")
    if not decision_checks["all_anchors_found"]:
        raise MachineOverviewError("TICK_GAP_ANCHOR_REPLAY_MISMATCH")
    run_dir = run_path.parent
    for probe in deterministic["probes"]:
        _verify_artifacts(run_dir, probe)
    rerun_results = []
    if rerun:
        rows = {row["probe_id"]: row for row in decisions["probes"]}
        for recorded in deterministic["probes"]:
            row = rows[recorded["probe_id"]]
            command = _probe_command(root, scope, validated, row)
            completed = subprocess.run(command, cwd=root, capture_output=True, timeout=row.get("timeout_seconds", 300))
            classification = _classify(row, completed.returncode, completed.stdout, completed.stderr)
            exact = (
                completed.returncode == recorded["first"]["exit_code"]
                and sha256_bytes(completed.stdout) == recorded["first"]["artifacts"]["stdout"]["sha256"]
                and sha256_bytes(completed.stderr) == recorded["first"]["artifacts"]["stderr"]["sha256"]
            )
            rerun_results.append({"probe_id": row["probe_id"], **classification, "exact_recorded_output": exact})
            if not classification["expectation_met"] or not exact:
                raise MachineOverviewError(f"TICK_GAP_PROBE_RERUN_MISMATCH:{row['probe_id']}")
    recomputed_digest = sha256_bytes(json_bytes(deterministic))
    if recomputed_digest != payload.get("deterministic_sha256"):
        raise MachineOverviewError("TICK_GAP_DETERMINISTIC_DIGEST_MISMATCH")
    return {
        "status": "TICK_IRRELEVANCE_OPERATIONAL_GAP_VALID",
        "run_id": payload["run_id"],
        "verdict": deterministic["verdict"],
        "candidate_scope": deterministic["candidate_scope"],
        "hott_bug_status": deterministic["hott_bug_status"],
        "source_count": deterministic["source_count"],
        "probe_count": len(deterministic["probes"]),
        "search_witnesses": deterministic["equality_search"]["target_paths"],
        "natural_usage_mismatches": len(deterministic["natural_usage_mismatches"]),
        "rerun": rerun,
        "rerun_results": rerun_results,
        "deterministic_sha256": payload["deterministic_sha256"],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    freeze = sub.add_parser("freeze")
    freeze.add_argument("--scope", required=True)
    freeze.add_argument("--out", required=True)
    run = sub.add_parser("run")
    run.add_argument("--scope", required=True)
    run.add_argument("--decisions", required=True)
    run.add_argument("--run-id", required=True)
    run.add_argument("--out", required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("--run", required=True)
    verify.add_argument("--rerun", action="store_true")
    args = parser.parse_args(argv)
    root = repo_root()
    try:
        if args.command == "freeze":
            result = _freeze(root, root / args.scope, root / args.out)
            print(json.dumps({
                "status": "TICK_IRRELEVANCE_OPERATIONAL_GAP_FROZEN",
                "freeze_id": result["freeze_id"],
                "source_artifacts": result["source_artifacts"],
                "future_paths": len(result["future_paths"]),
            }, ensure_ascii=False, indent=2))
        elif args.command == "run":
            result = _run(root, root / args.scope, root / args.decisions, root / args.out, args.run_id)
            print(json.dumps({
                "status": "TICK_IRRELEVANCE_OPERATIONAL_GAP_RUN_WRITTEN",
                "run_id": result["run_id"],
                "verdict": result["deterministic"]["verdict"],
                "deterministic_sha256": result["deterministic_sha256"],
            }, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(_verify(root, root / args.run, args.rerun), ensure_ascii=False, indent=2))
    except (
        MachineOverviewError,
        OSError,
        ValueError,
        KeyError,
        UnicodeError,
        json.JSONDecodeError,
        subprocess.SubprocessError,
    ) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
