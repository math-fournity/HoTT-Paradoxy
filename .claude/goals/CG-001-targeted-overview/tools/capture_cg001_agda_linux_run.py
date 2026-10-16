#!/usr/bin/env python3
"""Capture one Cubical Agda run on Linux as an F-011 receipt (CG001 line, goal-local).

Derived on 2026-09-30 (Claude Code cloud session 01FJANnV) from
Cloud-Opus审计并补完GLM/tools/capture_copus_run.py as of commit 4603eb2a, which
is kept unchanged.  Why a copy: the CG001 packages of 2026-09-30 import packages
that live in other directories (the questioning program imports the Delay type
of pedometer-semantics and the universe theorem of universe-questioning), so a
run needs several include roots (-i), which the canonical entry point
scripts/audit/capture_agda_proof_run.py does not take; and the Cloud-Opus tool
accepts only -COPUS- run ids.  Differences from the Cloud-Opus tool, nothing
else changed:

  * run ids must contain -CG001- (they are checked by
    .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py);
  * ROOT is four directories up (this file lives in the CG-001 tools folder);
  * the audit_session string and the capture_tool line of environment.txt
    name this tool and this session.

Everything else is the Cloud-Opus tool: the canonical helpers and receipt schema
(formal-proof-run/v1, formal-proof-source-manifest/v1), the Linux toolchain record
HoTT/formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json by default, the pinned
release-asset, binary, library-file and tree hashes, publisher_digest = null for
the Linux Agda asset, and the rejection-stage classification for negative controls.

Usage (cwd = repository root):
  python3 -B .claude/goals/CG-001-targeted-overview/tools/capture_cg001_agda_linux_run.py \
      --run-id 20260930-CG001-<NAME>-01 --proof-id MP-CG001-<NAME>-001 --claim-id CG001-C-NN \
      --source HoTT/formal/claude-cg001/<pkg>/<File>.agda [--include <dir>]... \
      [--manifest-file <path>]... --expect ACCEPT|REJECT --scope "..." \
      [--non-goal "..."]... [--audit-note "..."]...
"""
from __future__ import annotations

import argparse
import datetime as dt
import importlib.util
import json
import platform
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
CANONICAL_CAPTURE = ROOT / "scripts/audit/capture_agda_proof_run.py"

SCOPE_STAGE_TAGS = {
    "NotInScope", "AmbiguousName", "ModuleNameDoesntMatchFileName", "FileNotFound",
    "ParseError", "NoParseForApplication", "AmbiguousParseForApplication",
    "ModuleDoesntExport", "ClashingDefinition", "DuplicateImports",
}


def load_canonical():
    spec = importlib.util.spec_from_file_location("canonical_capture", CANONICAL_CAPTURE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> int:
    cc = load_canonical()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--proof-id", required=True)
    ap.add_argument("--claim-id", action="append", required=True)
    ap.add_argument("--source", required=True)
    ap.add_argument("--include", action="append", default=[], help="extra include root (repo-relative dir)")
    ap.add_argument("--manifest-file", action="append", default=[])
    ap.add_argument("--agda-flag", action="append", default=[])
    ap.add_argument("--toolchain", default="HoTT/formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json")
    ap.add_argument("--expect", choices=["ACCEPT", "REJECT"], required=True)
    ap.add_argument("--scope", required=True)
    ap.add_argument("--non-goal", action="append", default=[])
    ap.add_argument("--audit-note", action="append", default=[])
    args = ap.parse_args()

    root = ROOT
    if not all(c.isalnum() or c in "._-" for c in args.run_id) or "-CG001-" not in args.run_id:
        raise SystemExit("RUN_ID_INVALID_OR_NOT_CG001")
    run_relative = cc.RUN_ROOT / args.run_id
    run_dir = root / run_relative
    if run_dir.exists():
        raise SystemExit("RUN_DIRECTORY_ALREADY_EXISTS")

    source = cc.safe_relative(args.source)
    toolchain_relative = cc.safe_relative(args.toolchain)
    toolchain = json.loads((root / toolchain_relative).read_text(encoding="utf-8"))
    if toolchain.get("schema_version") != "hott-cubical-agda-toolchain/v1":
        raise SystemExit("TOOLCHAIN_SCHEMA_INVALID")
    library_registry = cc.safe_relative(str(toolchain["project_library_registry"]))

    manifest_paths = [source, toolchain_relative, library_registry]
    for value in args.manifest_file:
        p = cc.safe_relative(value)
        if p not in manifest_paths:
            manifest_paths.append(p)
    source_rows = []
    for relative in manifest_paths:
        row = cc.file_row(root / relative)
        row["path"] = relative.as_posix()
        source_rows.append(row)

    agda = toolchain["agda"]
    cubical = toolchain["cubical_library"]
    cache = toolchain["runtime_cache"]
    agda_archive = Path(agda["local_archive"])
    agda_binary = Path(agda["local_binary"])
    cubical_archive = Path(cubical["local_archive"])
    cubical_root = Path(cubical["local_root"])
    library_file = Path(cubical["library_file"])
    cc.expect_file(agda_archive, agda["asset_bytes"], agda["asset_sha256"], "agda-release-asset")
    cc.expect_file(agda_binary, agda["binary_bytes"], agda["binary_sha256"], "agda-binary")
    cc.expect_file(cubical_archive, cubical["asset_bytes"], cubical["asset_sha256"], "cubical-release-asset")
    cc.expect_file(library_file, cubical["library_file_bytes"], cubical["library_file_sha256"], "cubical-library-file")
    tree = cc.deterministic_tree(cubical_root)
    if tree != {"file_count": cubical["tree_file_count"], "total_bytes": cubical["tree_total_bytes"], "tree_sha256": cubical["tree_sha256"]}:
        raise SystemExit("CUBICAL_TREE_MISMATCH")
    for key in ("xdg_data_home", "xdg_config_home", "tmpdir"):
        Path(cache[key]).mkdir(parents=True, exist_ok=True)

    include_roots = [str((root / source).parent)]
    for inc in args.include:
        d = root / cc.safe_relative(inc)
        if not d.is_dir():
            raise SystemExit(f"INCLUDE_ROOT_MISSING:{inc}")
        if str(d) not in include_roots:
            include_roots.append(str(d))
    env_prefix = [
        "/usr/bin/env",
        f"XDG_DATA_HOME={cache['xdg_data_home']}",
        f"XDG_CONFIG_HOME={cache['xdg_config_home']}",
        f"TMPDIR={cache['tmpdir']}",
    ]
    command = env_prefix + [str(agda_binary), "--ignore-interfaces",
                            f"--library-file={root / library_registry}",
                            "-l", f"cubical-{cubical['version']}"]
    for inc in include_roots:
        command += ["-i", inc]
    command += list(args.agda_flag)
    command += [source.as_posix()]

    version = subprocess.run(env_prefix + [str(agda_binary), "--version"], cwd=root, capture_output=True, check=False)
    if version.returncode != 0:
        raise SystemExit("AGDA_VERSION_COMMAND_FAILED")
    started = dt.datetime.now(dt.timezone.utc)
    result = subprocess.run(command, cwd=root, capture_output=True, check=False)
    completed = dt.datetime.now(dt.timezone.utc)

    out_text = result.stdout.decode("utf-8", "replace")
    tag_match = re.search(r"error: \[([A-Za-z.]+)\]", out_text)
    error_tag = tag_match.group(1) if tag_match else None
    if result.returncode == 0:
        status = "KERNEL_ACCEPTED_WITH_SCOPE"
        stage = None
    elif error_tag and error_tag.split(".")[0] in SCOPE_STAGE_TAGS:
        status = "REJECTED_BEFORE_TYPE_CHECKING"
        stage = "SCOPE_OR_PARSE"
    else:
        status = "KERNEL_REJECTED"
        stage = "TYPE_CHECKING"
    first_error = None
    if result.returncode != 0:
        lines = out_text.splitlines()
        for i, line in enumerate(lines):
            if "error: [" in line:
                first_error = "\n".join(lines[i:i + 6])
                break

    external = [
        {**cc.file_row(agda_archive, label="agda-release-asset"),
         "publisher_digest": agda["asset_sha256"] if agda.get("asset_sha256_is_publisher_digest") else None,
         "url": agda["asset_url"]},
        {**cc.file_row(agda_binary, label="agda-binary")},
        {**cc.file_row(cubical_archive, label="cubical-release-asset"),
         "publisher_digest": cubical["asset_sha256"], "url": cubical["asset_url"]},
        {**cc.file_row(library_file, label="cubical-library-file")},
        {"label": "cubical-extracted-tree", "local_path": str(cubical_root), **tree,
         "release_tag": cubical["release_tag"], "tag_commit": cubical["tag_commit"]},
    ]
    source_manifest = {
        "schema_version": "formal-proof-source-manifest/v1",
        "proof_id": args.proof_id,
        "run_id": args.run_id,
        "files": source_rows,
        "external_dependencies": external,
    }
    source_manifest_data = cc.json_bytes(source_manifest)
    environment = "\n".join([
        f"platform={platform.platform()}",
        f"machine={platform.machine()}",
        f"python={platform.python_version()}",
        f"agda_executable={agda_binary}",
        "agda_version=" + version.stdout.decode("utf-8", "replace").strip().replace("\n", " | "),
        f"cubical_library_version={cubical['version']}",
        f"cubical_library_tag_commit={cubical['tag_commit']}",
        f"cubical_library_tree_sha256={tree['tree_sha256']}",
        "theory_variant=Cubical Agda native Path and higher inductive types; source OPTIONS --safe --cubical",
        "dependency_policy=release assets pinned by SHA-256 plus extracted binary/library tree hashes; Linux Agda asset has no readable publisher digest (see TOOLCHAIN note)",
        "capture_tool=.claude/goals/CG-001-targeted-overview/tools/capture_cg001_agda_linux_run.py (derived from Cloud-Opus审计并补完GLM/tools/capture_copus_run.py; reuses canonical capture helpers)",
        "secret_policy=no credentials, signed redirects, cookies or full environment dump retained",
        "",
    ]).encode("utf-8")
    run = {
        "schema_version": "formal-proof-run/v1",
        "run_id": args.run_id,
        "proof_id": args.proof_id,
        "claim_ids": args.claim_id,
        "proof_assistant": "Cubical Agda",
        "proof_assistant_version": version.stdout.decode("utf-8", "replace").strip(),
        "theory_variant": toolchain["theory_variant"],
        "command_argv": command,
        "cwd": str(root),
        "include_roots": include_roots,
        "extra_agda_flags": list(args.agda_flag),
        "started_at_utc": started.isoformat(),
        "completed_at_utc": completed.isoformat(),
        "duration_seconds": (completed - started).total_seconds(),
        "exit_code": result.returncode,
        "status": status,
        "expected_outcome": args.expect,
        "outcome_matches_expectation": (result.returncode == 0) == (args.expect == "ACCEPT"),
        "rejection_stage": stage,
        "agda_error_tag": error_tag,
        "first_error_excerpt": first_error,
        "scope": args.scope,
        "non_goals": args.non_goal,
        "audit_notes": args.audit_note,
        "audit_session": "Claude CG001 line, Claude Code cloud session 01FJANnV, branch claude/charming-pasteur-mvzlio, 2026-09-30",
        "stdout": {"path": "stdout.txt", "bytes": len(result.stdout), "sha256": cc.sha(result.stdout)},
        "stderr": {"path": "stderr.txt", "bytes": len(result.stderr), "sha256": cc.sha(result.stderr)},
        "environment": {"path": "environment.txt", "bytes": len(environment), "sha256": cc.sha(environment)},
        "source_manifest": {"path": "source-manifest.json", "bytes": len(source_manifest_data), "sha256": cc.sha(source_manifest_data)},
        "index_status": "PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE",
        "git_status": "LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED",
    }
    run_dir.mkdir(parents=True, exist_ok=False)
    cc.exclusive_write(run_dir / "stdout.txt", result.stdout)
    cc.exclusive_write(run_dir / "stderr.txt", result.stderr)
    cc.exclusive_write(run_dir / "environment.txt", environment)
    cc.exclusive_write(run_dir / "source-manifest.json", source_manifest_data)
    cc.exclusive_write(run_dir / "RUN.json", cc.json_bytes(run))
    print(json.dumps({"run": run_relative.as_posix(), "status": status, "exit_code": result.returncode,
                      "expected": args.expect, "matches": run["outcome_matches_expectation"],
                      "error_tag": error_tag, "seconds": round(run["duration_seconds"], 1)}, ensure_ascii=False))
    return 0 if run["outcome_matches_expectation"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
