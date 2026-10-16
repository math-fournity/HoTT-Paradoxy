#!/usr/bin/env python3
"""Reproduce the bounded agda-unimath E6 source and replay-closure scan.

This is a lexical/source audit, not a mathematical proof and not a complete
semantic search.  It deliberately separates what the saved kernel run checked
from what is merely present in the pinned source tree.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_TOOLCHAIN = REPO / "HoTT/formal/agda-unimath/UNIMATH_TOOLCHAIN.json"
DEFAULT_RUN = REPO / "HoTT/verification/runs/20260913-MP-UNIMATH-NOSECTION-REPLAY-02"
DEFAULT_OUTPUT = REPO / "audit/agda-unimath-e6-source-scan-20260913.json"
DECLARATION = re.compile(r"^\s*(?:private\s+)?(postulate|primitive)\b")
CHECKING = re.compile(r"^\s*Checking\s+([^ ]+)\s+\((/.+)\)\.$")


class ScanError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ScanError(f"INVALID_JSON:{path}") from exc
    if not isinstance(value, dict):
        raise ScanError(f"JSON_OBJECT_REQUIRED:{path}")
    return value


def deterministic_tree(root: Path) -> dict[str, object]:
    if not root.is_dir() or root.is_symlink():
        raise ScanError(f"SOURCE_TREE_INVALID:{root}")
    rows: list[dict[str, object]] = []
    total = 0
    for path in sorted(root.rglob("*")):
        if path.is_file() and not path.is_symlink() and path.suffix != ".agdai" and path.name != ".DS_Store":
            data = path.read_bytes()
            rows.append({"path": path.relative_to(root).as_posix(), "bytes": len(data), "sha256": sha(data)})
            total += len(data)
    digest = hashlib.sha256()
    for row in rows:
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        digest.update(b"\n")
    return {"file_count": len(rows), "total_bytes": total, "tree_sha256": digest.hexdigest()}


def code_lines(path: Path):
    """Yield (line number, line) for Agda code, excluding Markdown prose."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if path.name.endswith(".lagda.md"):
        in_agda = False
        for number, line in enumerate(lines, 1):
            fence = re.match(r"^\s*```\s*([^`]*)$", line)
            if fence:
                if in_agda:
                    in_agda = False
                else:
                    in_agda = fence.group(1).strip().casefold() == "agda"
                continue
            if in_agda:
                yield number, line
    else:
        for number, line in enumerate(lines, 1):
            yield number, line


def declarations(path: Path) -> list[dict[str, object]]:
    found = []
    for number, line in code_lines(path):
        match = DECLARATION.match(line)
        if match:
            found.append({"kind": match.group(1), "line": number, "text": line.strip()})
    return found


def source_anchor(root: Path, rel: str, patterns: list[str]) -> dict[str, object]:
    path = root / rel
    data = path.read_bytes()
    lines = data.decode("utf-8").splitlines()
    hits = []
    for pattern in patterns:
        regex = re.compile(pattern)
        for number, line in enumerate(lines, 1):
            if regex.search(line):
                hits.append({"pattern": pattern, "line": number, "text": line.strip()})
    if any(not any(hit["pattern"] == pattern for hit in hits) for pattern in patterns):
        raise ScanError(f"REQUIRED_ANCHOR_MISSING:{rel}")
    return {"path": rel, "bytes": len(data), "sha256": sha(data), "hits": hits}


def build(toolchain_path: Path, run_dir: Path) -> dict:
    toolchain = load_json(toolchain_path)
    library = toolchain.get("agda_unimath_library", {})
    root = Path(str(library.get("local_root", "")))
    expected_tree = {key: library.get(key) for key in ("tree_file_count", "tree_total_bytes", "tree_sha256")}
    actual_tree_raw = deterministic_tree(root)
    actual_tree = {
        "tree_file_count": actual_tree_raw["file_count"],
        "tree_total_bytes": actual_tree_raw["total_bytes"],
        "tree_sha256": actual_tree_raw["tree_sha256"],
    }
    if actual_tree != expected_tree:
        raise ScanError("PINNED_SOURCE_TREE_MISMATCH")
    source_root = root / "src"
    candidates = sorted(
        path for path in source_root.rglob("*")
        if path.is_file() and not path.is_symlink() and (path.suffix == ".agda" or path.name.endswith(".lagda.md"))
    )
    declaration_files = []
    for path in candidates:
        found = declarations(path)
        if found:
            declaration_files.append({
                "path": path.relative_to(root).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha(path.read_bytes()),
                "declarations": found,
            })
    stdout_path = run_dir / "stdout.txt"
    stdout = stdout_path.read_text(encoding="utf-8")
    checked = []
    for line in stdout.splitlines():
        match = CHECKING.match(line)
        if match:
            checked.append({"module": match.group(1), "path": match.group(2)})
    if not checked:
        raise ScanError("SAVED_REPLAY_CHECKING_LINES_MISSING")
    external_checked = []
    for row in checked:
        path = Path(row["path"])
        try:
            rel = path.relative_to(root).as_posix()
        except ValueError:
            continue
        external_checked.append({"module": row["module"], "path": rel})
    declaration_by_path = {row["path"]: row for row in declaration_files}
    closure_declarations = [declaration_by_path[row["path"]] for row in external_checked if row["path"] in declaration_by_path]
    allow_unsolved = []
    for path in candidates:
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if "--allow-unsolved-metas" in line:
                allow_unsolved.append({"path": path.relative_to(root).as_posix(), "line": number, "text": line.strip()})
    anchors = [
        source_anchor(root, "src/foundation/hilberts-epsilon-operators.lagda.md", [r"^ε-operator-Hilbert\b"]),
        source_anchor(root, "src/foundation/global-choice.lagda.md", [r"^Global-Choice\b", r"^\s*no-global-choice\b", r"no-section-type-2-Element-Type"]),
        source_anchor(root, "src/univalent-combinatorics/finite-choice.lagda.md", [r"^\s*ε-operator-count\b"]),
        source_anchor(root, "src/foundation/decidable-types.lagda.md", [r"^ε-operator-is-decidable\b"]),
        source_anchor(root, "src/logic/double-negation-elimination.lagda.md", [r"^ε-operator-Hilbert-has-double-negation-elim\b"]),
    ]
    postulate_files = [row["path"] for row in declaration_files if any(d["kind"] == "postulate" for d in row["declarations"])]
    primitive_files = [row["path"] for row in declaration_files if any(d["kind"] == "primitive" for d in row["declarations"])]
    global_path = "src/foundation/global-choice.lagda.md"
    return {
        "schema_version": "agda-unimath-e6-source-scan/v1",
        "classification": "SOURCE_INSPECTED_BOUNDED_NEGATIVE",
        "mathematical_certification": "NOT_PERFORMED",
        "source_identity": {
            "repository": library.get("repository"),
            "commit_sha": library.get("commit_sha"),
            "tree": actual_tree,
            "toolchain_path": toolchain_path.relative_to(REPO).as_posix(),
            "toolchain_sha256": sha(toolchain_path.read_bytes()),
        },
        "scan_contract": {
            "candidate_files": "src/**/*.agda and src/**/*.lagda.md",
            "literate_rule": "Only lines inside fenced ```agda blocks count as Agda declarations; prose and other fences are excluded.",
            "declaration_rule": "Line-start postulate or primitive, optionally preceded by private.",
            "semantic_limit": "Lexical declaration and named-interface audit only; no proof of global semantic absence of E6.",
        },
        "source_scan": {
            "candidate_file_count": len(candidates),
            "postulate_file_count": len(postulate_files),
            "primitive_file_count": len(primitive_files),
            "postulate_or_primitive_file_count": len(declaration_files),
            "postulate_files": postulate_files,
            "primitive_files": primitive_files,
            "declaration_files": declaration_files,
            "allow_unsolved_metas_occurrences": allow_unsolved,
            "anchors": anchors,
        },
        "saved_kernel_replay_scope": {
            "run_id": load_json(run_dir / "RUN.json").get("run_id"),
            "stdout_path": stdout_path.relative_to(REPO).as_posix(),
            "stdout_sha256": sha(stdout_path.read_bytes()),
            "checking_line_count": len(checked),
            "external_module_count": len(external_checked),
            "external_modules": external_checked,
            "global_choice_in_replay_closure": any(row["path"] == global_path for row in external_checked),
            "declaration_files_in_replay_closure": closure_declarations,
            "scope_conclusion": "The saved run checks hott-z.NoCanonicalPoint and its imported closure; foundation.global-choice is not in that closure.",
        },
        "e6_assessment": {
            "no_global_choice_status": "SOURCE_INSPECTED_NOT_REPLAYED_BY_THIS_RUN",
            "positive_controls_status": "SOURCE_INSPECTED",
            "verdict": "SOURCE_INSPECTED_BOUNDED_NEGATIVE",
            "limits": [
                "No claim that the full library has been semantically proved free of E6.",
                "No claim that no downstream application or derived development misuses a weaker interface.",
                "No claim that no-global-choice was kernel-replayed by the saved C-05 run.",
            ],
        },
    }


def encoded(value: dict) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, raw = tempfile.mkstemp(prefix="." + path.name + ".", dir=path.parent)
    temp = Path(raw)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data); handle.flush(); os.fsync(handle.fileno())
        os.replace(temp, path)
    finally:
        if temp.exists(): temp.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toolchain", type=Path, default=DEFAULT_TOOLCHAIN)
    parser.add_argument("--run-dir", type=Path, default=DEFAULT_RUN)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    try:
        result = build(args.toolchain.resolve(), args.run_dir.resolve())
        data = encoded(result)
        output = args.output.resolve()
        if args.write:
            atomic_write(output, data)
            status = "WROTE"
        else:
            if not output.is_file() or output.read_bytes() != data:
                raise ScanError("OUTPUT_MISSING_OR_STALE_USE_WRITE")
            status = "PASS"
        print(json.dumps({
            "status": status,
            "output": output.relative_to(REPO).as_posix(),
            "sha256": sha(data),
            "classification": result["classification"],
            "postulate_files": result["source_scan"]["postulate_file_count"],
            "postulate_or_primitive_files": result["source_scan"]["postulate_or_primitive_file_count"],
            "replay_external_modules": result["saved_kernel_replay_scope"]["external_module_count"],
            "replay_closure_declaration_files": len(result["saved_kernel_replay_scope"]["declaration_files_in_replay_closure"]),
            "global_choice_in_replay_closure": result["saved_kernel_replay_scope"]["global_choice_in_replay_closure"],
        }, ensure_ascii=False))
        return 0
    except (ScanError, OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"status": "BLOCKED", "error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
