#!/usr/bin/env python3
"""Freeze, run and replay the HoTT quotation/later bridge evaluation.

This evaluator keeps three roles distinct:

* Agda ``TC A`` is a host type-checking computation;
* quotation ``Box A`` is syntax or typed proof code;
* guarded ``Later k A`` means availability after a clock tick.

Semantic H1-H6 decisions are explicit review input.  The evaluator verifies
their frozen source anchors and executes the declared Agda probes; it never
infers a HoTT bug from shared vocabulary or a successful conditional target.
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

SCOPE_SCHEMA = "machine-overview-hott-quotation-bridge-scope/v1"
DECISIONS_SCHEMA = "machine-overview-hott-quotation-bridge-decisions/v1"
FREEZE_SCHEMA = "machine-overview-hott-quotation-bridge-freeze/v1"
RUN_SCHEMA = "machine-overview-hott-quotation-bridge-run/v1"
QUESTIONS = [f"H{i}" for i in range(1, 7)]
ROLES = ["HOST_TC", "SYNTAX_QUOTATION", "TEMPORAL_LATER"]
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
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True,
    )
    return Path(result.stdout.strip()).resolve()


def _under(path: Path, parent: Path, label: str) -> Path:
    resolved = path.resolve()
    try:
        resolved.relative_to(parent.resolve())
    except ValueError as exc:
        raise MachineOverviewError(f"BRIDGE_PATH_OUTSIDE_ROOT:{label}:{path}") from exc
    return resolved


def _resolve(root: Path, value: str, allowed_roots: list[Path], label: str) -> Path:
    raw = Path(value)
    if raw.is_absolute():
        for allowed in allowed_roots:
            try:
                return _under(raw, allowed, label)
            except MachineOverviewError:
                continue
        raise MachineOverviewError(f"BRIDGE_EXTERNAL_PATH_NOT_ALLOWED:{label}:{value}")
    return _under(root / safe_relative(value), root, label)


def _pin(root: Path, path: Path) -> dict:
    resolved = path.resolve()
    try:
        relative = resolved.relative_to(root.resolve()).as_posix()
        value = relative
    except ValueError:
        value = str(resolved)
    if not resolved.is_file() or resolved.is_symlink():
        raise MachineOverviewError(f"BRIDGE_PIN_FILE_INVALID:{value}")
    return {"path": value, "bytes": resolved.stat().st_size, "sha256": sha256_file(resolved)}


def _verify_pin(root: Path, row: dict, allowed_roots: list[Path], label: str) -> Path:
    if not isinstance(row, dict) or not isinstance(row.get("path"), str):
        raise MachineOverviewError(f"BRIDGE_PIN_INVALID:{label}")
    path = _resolve(root, row["path"], allowed_roots, label)
    if (not path.is_file() or path.is_symlink() or path.stat().st_size != row.get("bytes")
            or sha256_file(path) != row.get("sha256")):
        raise MachineOverviewError(f"BRIDGE_PIN_CHANGED:{label}:{row.get('path')}")
    return path


def _normalized(data: bytes, kind: str) -> str:
    text = data.decode("utf-8", errors="strict")
    if kind == "html":
        parser = _VisibleText()
        parser.feed(text)
        text = " ".join(parser.parts)
    return " ".join(html.unescape(text).split())


def _allowed_roots(scope: dict) -> list[Path]:
    roots = [Path(value).resolve() for value in scope.get("allowed_external_roots", [])]
    if not roots or any(not root.is_dir() or root.is_symlink() for root in roots):
        raise MachineOverviewError("BRIDGE_ALLOWED_ROOT_INVALID")
    return roots


def validate_scope(root: Path, scope: dict) -> dict:
    if scope.get("schema_version") != SCOPE_SCHEMA:
        raise MachineOverviewError("BRIDGE_SCOPE_SCHEMA_INVALID")
    if scope.get("roles") != ROLES:
        raise MachineOverviewError("BRIDGE_ROLE_ROSTER_INVALID")
    if [row.get("id") for row in scope.get("questions", [])] != QUESTIONS:
        raise MachineOverviewError("BRIDGE_QUESTION_ROSTER_INVALID")
    allowed = _allowed_roots(scope)
    source_ids = [row.get("source_id") for row in scope.get("sources", [])]
    if not source_ids or len(source_ids) != len(set(source_ids)):
        raise MachineOverviewError("BRIDGE_SOURCE_ROSTER_INVALID")
    artifacts: dict[str, dict] = {}
    for source in scope["sources"]:
        for row in source.get("artifacts", []):
            artifact_id = row.get("artifact_id")
            if not isinstance(artifact_id, str) or artifact_id in artifacts:
                raise MachineOverviewError(f"BRIDGE_ARTIFACT_ID_INVALID:{artifact_id}")
            path = _verify_pin(root, row, allowed, artifact_id)
            artifacts[artifact_id] = {
                "row": row,
                "path": path,
                "normalized": _normalized(path.read_bytes(), row.get("kind", "text")),
            }
    trees = []
    for index, row in enumerate(scope.get("trees", [])):
        path = _resolve(root, row.get("path", ""), allowed, f"tree.{index}")
        actual = deterministic_tree(path)
        if actual != row.get("identity"):
            raise MachineOverviewError(f"BRIDGE_TREE_CHANGED:{row.get('tree_id')}")
        trees.append({"tree_id": row["tree_id"], "path": str(path), "identity": actual})
    return {"allowed_roots": allowed, "artifacts": artifacts, "trees": trees}


def reflection_inventory(scope: dict, validated: dict) -> dict:
    tree = next((row for row in validated["trees"] if row["tree_id"] == "CUBICAL-V0.9"), None)
    if tree is None:
        raise MachineOverviewError("BRIDGE_CUBICAL_TREE_MISSING")
    patterns = {key: re.compile(value) for key, value in scope["inventory_patterns"].items()}
    rows = {key: [] for key in patterns}
    tree_root = Path(tree["path"])
    for path in sorted(tree_root.rglob("*")):
        if not path.is_file() or path.is_symlink() or path.suffix not in {".agda", ".md"}:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(tree_root).as_posix()
        for key, pattern in patterns.items():
            count = len(pattern.findall(text))
            if count:
                rows[key].append({"path": relative, "count": count})
    return {
        key: {
            "file_count": len(value),
            "occurrences": sum(item["count"] for item in value),
            "files": value,
        }
        for key, value in rows.items()
    }


def validate_decisions(root: Path, scope: dict, decisions: dict, validated: dict) -> dict:
    if decisions.get("schema_version") != DECISIONS_SCHEMA:
        raise MachineOverviewError("BRIDGE_DECISIONS_SCHEMA_INVALID")
    if decisions.get("evaluation_id") != scope.get("evaluation_id"):
        raise MachineOverviewError("BRIDGE_EVALUATION_ID_MISMATCH")
    expected_sources = [row["source_id"] for row in scope["sources"]]
    rows = decisions.get("sources", [])
    if [row.get("source_id") for row in rows] != expected_sources:
        raise MachineOverviewError("BRIDGE_DECISION_SOURCE_ROSTER_MISMATCH")
    anchor_checks = []
    semantic_rows = []
    for row in rows:
        answers = row.get("answers", {})
        if list(answers) != QUESTIONS:
            raise MachineOverviewError(f"BRIDGE_QUESTION_COVERAGE_INVALID:{row['source_id']}")
        if row.get("role") not in ROLES:
            raise MachineOverviewError(f"BRIDGE_DECISION_ROLE_INVALID:{row['source_id']}")
        for question, answer in answers.items():
            if answer.get("status") not in DECISION_STATUSES:
                raise MachineOverviewError(f"BRIDGE_DECISION_STATUS_INVALID:{row['source_id']}:{question}")
            evidence = answer.get("evidence", [])
            if not evidence:
                raise MachineOverviewError(f"BRIDGE_DECISION_EVIDENCE_MISSING:{row['source_id']}:{question}")
            for item in evidence:
                artifact = validated["artifacts"].get(item.get("artifact_id"))
                if artifact is None:
                    raise MachineOverviewError(f"BRIDGE_EVIDENCE_ARTIFACT_UNKNOWN:{item.get('artifact_id')}")
                for needle in item.get("anchors", []):
                    normalized = " ".join(html.unescape(needle).split())
                    found = normalized in artifact["normalized"]
                    anchor_checks.append({
                        "source_id": row["source_id"],
                        "question": question,
                        "artifact_id": item["artifact_id"],
                        "anchor_sha256": sha256_bytes(normalized.encode("utf-8")),
                        "found": found,
                    })
                    if not found:
                        raise MachineOverviewError(
                            f"BRIDGE_EVIDENCE_ANCHOR_MISSING:{row['source_id']}:{question}:{item['artifact_id']}"
                        )
        semantic_rows.append({
            "source_id": row["source_id"],
            "role": row["role"],
            "answers": answers,
            "classification": row.get("classification"),
            "erases_guard": answers["H6"]["status"] == "PASS",
        })
    probe_ids = [row.get("probe_id") for row in decisions.get("probes", [])]
    if not probe_ids or len(probe_ids) != len(set(probe_ids)):
        raise MachineOverviewError("BRIDGE_PROBE_ROSTER_INVALID")
    for row in decisions["probes"]:
        _verify_pin(root, row.get("source"), validated["allowed_roots"], f"probe.{row['probe_id']}")
        if row.get("expect") not in {"ACCEPT", "TYPE_REJECTION", "TOOLCHAIN_MISMATCH"}:
            raise MachineOverviewError(f"BRIDGE_PROBE_EXPECTATION_INVALID:{row['probe_id']}")
        if not isinstance(row.get("command_argv"), list) or not row["command_argv"]:
            raise MachineOverviewError(f"BRIDGE_PROBE_COMMAND_INVALID:{row['probe_id']}")
    return {
        "sources": semantic_rows,
        "anchor_checks": anchor_checks,
        "all_anchors_found": all(item["found"] for item in anchor_checks),
        "guard_erasure_consumers": [row["source_id"] for row in semantic_rows if row["erases_guard"]],
    }


def _expand_command(root: Path, scope: dict, validated: dict, row: dict) -> list[str]:
    toolchain = read_json(root / scope["toolchain"]["config_path"])
    replacements = {
        "${AGDA}": toolchain["agda"]["local_binary"],
        "${ROOT}": str(root),
        "${LIBRARY_FILE}": str(root / toolchain["project_library_registry"]),
        "${CUBICAL_ROOT}": toolchain["cubical_library"]["local_root"],
    }
    for index, value in enumerate(scope.get("command_paths", [])):
        replacements[f"${{PATH_{index}}}"] = value
    command = []
    for token in row["command_argv"]:
        expanded = replacements.get(token, token)
        if token.startswith("${PATH_") and token not in replacements:
            raise MachineOverviewError(f"BRIDGE_COMMAND_PLACEHOLDER_UNKNOWN:{token}")
        command.append(expanded)
    if Path(command[0]).resolve() != Path(toolchain["agda"]["local_binary"]).resolve():
        raise MachineOverviewError(f"BRIDGE_COMMAND_BINARY_INVALID:{row['probe_id']}")
    return command


def _classify_probe(row: dict, exit_code: int, stdout: bytes, stderr: bytes) -> dict:
    text = (stdout + b"\n" + stderr).decode("utf-8", errors="replace")
    expect = row["expect"]
    if expect == "ACCEPT":
        matched = exit_code == 0
        classification = "KERNEL_ACCEPTED" if matched else "UNEXPECTED_REJECTION"
    elif expect == "TYPE_REJECTION":
        marker = row.get("diagnostic", "[UnequalTerms]")
        matched = exit_code == 42 and marker in text
        classification = "EXPECTED_TYPE_REJECTION" if matched else "UNEXPECTED_REJECTION_DIAGNOSTIC"
    else:
        marker = row.get("diagnostic", "[InvalidTypeSort]")
        matched = exit_code == 42 and marker in text
        classification = "EXPECTED_TOOLCHAIN_VERSION_MISMATCH" if matched else "UNEXPECTED_TOOLCHAIN_RESULT"
    return {"classification": classification, "expectation_met": matched}


def _run_once(root: Path, run_dir: Path, scope: dict, validated: dict, row: dict, suffix: str) -> dict:
    command = _expand_command(root, scope, validated, row)
    started = utc_now()
    start = time.monotonic()
    completed = subprocess.run(command, cwd=root, capture_output=True, timeout=row.get("timeout_seconds", 300))
    duration = time.monotonic() - start
    classification = _classify_probe(row, completed.returncode, completed.stdout, completed.stderr)
    target = run_dir / "probes" / row["probe_id"] / suffix
    command_payload = json_bytes({"command_argv": command, "cwd": str(root)})
    environment_payload = (
        f"platform={platform.platform()}\npython={platform.python_version()}\n"
        f"agda_binary={command[0]}\nagda_sha256={sha256_file(Path(command[0]))}\n"
    ).encode("utf-8")
    write_bytes(target / "stdout.txt", completed.stdout)
    write_bytes(target / "stderr.txt", completed.stderr)
    write_bytes(target / "command.json", command_payload)
    write_bytes(target / "environment.txt", environment_payload)
    return {
        "started_at_utc": started,
        "duration_seconds": duration,
        "command_argv": command,
        "cwd": str(root),
        "exit_code": completed.returncode,
        **classification,
        "artifacts": {
            "stdout": {"path": f"probes/{row['probe_id']}/{suffix}/stdout.txt", "bytes": len(completed.stdout), "sha256": sha256_bytes(completed.stdout)},
            "stderr": {"path": f"probes/{row['probe_id']}/{suffix}/stderr.txt", "bytes": len(completed.stderr), "sha256": sha256_bytes(completed.stderr)},
            "command": {"path": f"probes/{row['probe_id']}/{suffix}/command.json", "bytes": len(command_payload), "sha256": sha256_bytes(command_payload)},
            "environment": {"path": f"probes/{row['probe_id']}/{suffix}/environment.txt", "bytes": len(environment_payload), "sha256": sha256_bytes(environment_payload)},
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
        "role": row["role"],
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
        raise MachineOverviewError("BRIDGE_FREEZE_ALREADY_EXISTS")
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    existing = [value for value in scope["future_paths"] if (root / safe_relative(value)).exists()]
    if existing:
        raise MachineOverviewError(f"BRIDGE_FUTURE_PATH_EXISTS:{existing[0]}")
    evidence_dir = output_path.parent
    evidence_dir.mkdir(parents=True, exist_ok=True)
    checks = []
    for label, command in (
        ("selftest", [sys.executable, "machine-overview/mo.py", "selftest"]),
        ("validate", [sys.executable, "machine-overview/mo.py", "validate"]),
    ):
        completed = subprocess.run(command, cwd=root, capture_output=True, timeout=360)
        stdout_path = evidence_dir / f"pre-{label}-stdout.txt"
        stderr_path = evidence_dir / f"pre-{label}-stderr.txt"
        write_bytes(stdout_path, completed.stdout)
        write_bytes(stderr_path, completed.stderr)
        if completed.returncode != 0:
            raise MachineOverviewError(f"BRIDGE_FREEZE_{label.upper()}_FAILED")
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
        "roles": scope["roles"],
        "questions": scope["questions"],
        "future_paths": scope["future_paths"],
        "future_paths_absent": True,
        "pre_checks": checks,
        "git": git_state(root),
        "interpretation": (
            "The roles, source set, H1-H6 questions and probe purposes were frozen before probe source "
            "or semantic decisions existed. The same AI designed the evaluation; this is provenance and "
            "role-separation evidence, not blind novelty evidence."
        ),
    }
    write_json(output_path, result)
    return result


def _validate_freeze(root: Path, scope: dict, freeze_row: dict, validated: dict) -> dict:
    allowed = validated["allowed_roots"]
    freeze_path = _verify_pin(root, freeze_row, allowed, "freeze")
    freeze = read_json(freeze_path)
    if freeze.get("schema_version") != FREEZE_SCHEMA:
        raise MachineOverviewError("BRIDGE_FREEZE_SCHEMA_INVALID")
    _verify_pin(root, freeze.get("evaluator"), allowed, "freeze.evaluator")
    _verify_pin(root, freeze.get("scope"), allowed, "freeze.scope")
    if freeze.get("roles") != scope.get("roles") or freeze.get("questions") != scope.get("questions"):
        raise MachineOverviewError("BRIDGE_FREEZE_SEMANTIC_ROSTER_CHANGED")
    return freeze


def _run(root: Path, scope_path: Path, decisions_path: Path, output_path: Path, run_id: str) -> dict:
    if output_path.exists() or output_path.parent.exists():
        raise MachineOverviewError("BRIDGE_RUN_ALREADY_EXISTS")
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    decisions = read_json(decisions_path)
    freeze = _validate_freeze(root, scope, decisions["freeze"], validated)
    decision_result = validate_decisions(root, scope, decisions, validated)
    inventory = reflection_inventory(scope, validated)
    output_path.parent.mkdir(parents=True, exist_ok=False)
    probes = [_probe_pair(root, output_path.parent, scope, validated, row) for row in decisions["probes"]]
    all_probes = all(row["accepted"] for row in probes)
    temporal_collapse = next(row for row in probes if row["probe_id"] == "P06-GUARDED-FORCE-COLLAPSE")
    local_force_rejection = next(row for row in probes if row["probe_id"] == "P07-BAD-FIXED-FORCE")
    clock_scope_rejection = next(row for row in probes if row["probe_id"] == "P09-BAD-LOCAL-FROM-GLOBAL")
    deterministic = {
        "evaluation_id": scope["evaluation_id"],
        "freeze_id": freeze["freeze_id"],
        "scope": _pin(root, scope_path),
        "decisions": _pin(root, decisions_path),
        "source_count": len(scope["sources"]),
        "artifact_count": len(validated["artifacts"]),
        "anchor_checks": decision_result["anchor_checks"],
        "all_anchors_found": decision_result["all_anchors_found"],
        "roles": ROLES,
        "source_decisions": decision_result["sources"],
        "reflection_inventory": inventory,
        "guard_erasure_consumers": decision_result["guard_erasure_consumers"],
        "probes": probes,
        "all_probes_match_expectation_and_exact_replay": all_probes,
        "temporal_collapse_probe": temporal_collapse["accepted"],
        "fixed_clock_force_rejected": local_force_rejection["accepted"],
        "clock_quantifier_scope_rejected": clock_scope_rejection["accepted"],
        "verdict": (
            "GUARDED_FORCE_ERASURE_CONDITIONAL_COLLAPSE_WITH_DEFENSE"
            if all_probes and temporal_collapse["accepted"] and local_force_rejection["accepted"]
            and not decision_result["guard_erasure_consumers"]
            else "BRIDGE_REVIEW_REQUIRED"
        ),
        "hott_bug_status": "NOT_ESTABLISHED",
        "semantic_limit": (
            "The native collapse is conditional on a fixed-clock force operation. Fixed sources and probes "
            "show the real systems retain TC/quotation/tick/clock boundaries. Source semantic decisions are "
            "review judgments; no bounded absence result is a global nonexistence theorem."
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
            if (not path.is_file() or path.stat().st_size != row["bytes"]
                    or sha256_file(path) != row["sha256"]):
                raise MachineOverviewError(f"BRIDGE_RUN_ARTIFACT_CHANGED:{probe['probe_id']}:{stage}:{label}")


def _verify(root: Path, run_path: Path, rerun: bool) -> dict:
    payload = read_json(run_path)
    if payload.get("schema_version") != RUN_SCHEMA:
        raise MachineOverviewError("BRIDGE_RUN_SCHEMA_INVALID")
    deterministic = payload["deterministic"]
    scope_path = root / safe_relative(deterministic["scope"]["path"])
    decisions_path = root / safe_relative(deterministic["decisions"]["path"])
    scope = read_json(scope_path)
    validated = validate_scope(root, scope)
    _verify_pin(root, payload.get("evaluator"), validated["allowed_roots"], "run.evaluator")
    decisions = read_json(decisions_path)
    _validate_freeze(root, scope, decisions["freeze"], validated)
    decision_result = validate_decisions(root, scope, decisions, validated)
    if reflection_inventory(scope, validated) != deterministic["reflection_inventory"]:
        raise MachineOverviewError("BRIDGE_INVENTORY_REPLAY_MISMATCH")
    run_dir = run_path.parent
    for probe in deterministic["probes"]:
        _verify_artifacts(run_dir, probe)
    rerun_results = []
    if rerun:
        by_id = {row["probe_id"]: row for row in decisions["probes"]}
        for recorded in deterministic["probes"]:
            row = by_id[recorded["probe_id"]]
            command = _expand_command(root, scope, validated, row)
            completed = subprocess.run(command, cwd=root, capture_output=True, timeout=row.get("timeout_seconds", 300))
            classification = _classify_probe(row, completed.returncode, completed.stdout, completed.stderr)
            exact = (
                completed.returncode == recorded["first"]["exit_code"]
                and sha256_bytes(completed.stdout) == recorded["first"]["artifacts"]["stdout"]["sha256"]
                and sha256_bytes(completed.stderr) == recorded["first"]["artifacts"]["stderr"]["sha256"]
            )
            rerun_results.append({
                "probe_id": row["probe_id"],
                **classification,
                "exact_recorded_output": exact,
            })
            if not classification["expectation_met"] or not exact:
                raise MachineOverviewError(f"BRIDGE_PROBE_RERUN_MISMATCH:{row['probe_id']}")
    if decision_result["guard_erasure_consumers"] != deterministic["guard_erasure_consumers"]:
        raise MachineOverviewError("BRIDGE_CONSUMER_DECISION_CHANGED")
    return {
        "status": "HOTT_QUOTATION_BRIDGE_VALID",
        "run_id": payload["run_id"],
        "verdict": deterministic["verdict"],
        "hott_bug_status": deterministic["hott_bug_status"],
        "source_count": deterministic["source_count"],
        "probe_count": len(deterministic["probes"]),
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
                "status": "HOTT_QUOTATION_BRIDGE_FROZEN",
                "freeze_id": result["freeze_id"],
                "source_artifacts": result["source_artifacts"],
                "future_paths": len(result["future_paths"]),
            }, ensure_ascii=False, indent=2))
        elif args.command == "run":
            result = _run(root, root / args.scope, root / args.decisions, root / args.out, args.run_id)
            print(json.dumps({
                "status": "HOTT_QUOTATION_BRIDGE_RUN_WRITTEN",
                "run_id": result["run_id"],
                "verdict": result["deterministic"]["verdict"],
                "deterministic_sha256": result["deterministic_sha256"],
            }, ensure_ascii=False, indent=2))
        else:
            print(json.dumps(_verify(root, root / args.run, args.rerun), ensure_ascii=False, indent=2))
    except (MachineOverviewError, OSError, ValueError, KeyError, UnicodeError, subprocess.SubprocessError) as exc:
        print(json.dumps({"status": "FAIL", "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
