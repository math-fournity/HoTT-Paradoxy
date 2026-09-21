#!/usr/bin/env python3
"""Freeze and inspect the P31 public source without treating it as a HoTT proof."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
from pathlib import Path


HERE = Path(__file__).resolve().parent
CHECKOUT = Path("/tmp/tt-provability-p31-69de7983")
REMOTE = "https://github.com/GallagherCommaJack/tt-provability.git"
COMMIT = "69de7983019f2f044a40624b81662d862aca3dff"
RUN = HERE / "runs/20260921-P31-TT-PROVABILITY-SOURCE-01"


def invoke(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=False)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    RUN.mkdir(parents=True, exist_ok=True)
    if not CHECKOUT.exists():
        cloned = invoke(["git", "clone", "--filter=blob:none", "--no-checkout", REMOTE, str(CHECKOUT)])
        if cloned.returncode != 0:
            raise SystemExit(cloned.stderr)
    is_repo = invoke(["git", "rev-parse", "--is-inside-work-tree"], CHECKOUT)
    if is_repo.returncode != 0:
        raise SystemExit("P31_CHECKOUT_NOT_GIT_REPOSITORY")
    checked_out = invoke(["git", "checkout", "--detach", COMMIT], CHECKOUT)
    if checked_out.returncode != 0:
        raise SystemExit(checked_out.stderr)
    head = invoke(["git", "rev-parse", "HEAD"], CHECKOUT)
    status = invoke(["git", "status", "--porcelain=v1"], CHECKOUT)
    log = invoke(["git", "log", "-1", "--format=%H%n%aI%n%s"], CHECKOUT)
    if head.stdout.strip() != COMMIT or status.stdout.strip():
        raise SystemExit("P31_SOURCE_IDENTITY_OR_CLEANLINESS_FAILURE")
    files = [line for line in invoke(["git", "ls-files"], CHECKOUT).stdout.splitlines() if line]
    manifest = {relative: sha256(CHECKOUT / relative) for relative in sorted(files)}
    scan_tokens = [
        "Löb", "box", "⌜_⌝t", "⋆⋆TODO⋆⋆", "postulate", "no-positivity-check",
        "no-termination-check", "univalence", "cubical", "HoTT", "soundness", "provability",
        "consistency", "{!!}",
    ]
    hits: dict[str, list[str]] = {token: [] for token in scan_tokens}
    literal_lines: list[str] = []
    for relative in sorted(path for path in files if path.endswith(".agda")):
        for number, line in enumerate((CHECKOUT / relative).read_text().splitlines(), 1):
            found = [token for token in scan_tokens if token.lower() in line.lower()]
            if found:
                literal_lines.append(f"{relative}:{number}:{line}")
                for token in found:
                    hits[token].append(f"{relative}:{number}")
    (RUN / "git-identity.txt").write_text(log.stdout + status.stdout)
    (RUN / "source-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (RUN / "literal-search.txt").write_text("\n".join(literal_lines) + "\n")
    agda = shutil.which("agda")
    (RUN / "agda-toolchain.txt").write_text(
        "agda_path=" + (agda or "NOT_FOUND") + "\n"
        "kernel_replay=NOT_RUN_WITH_REASON_AGDA_EXECUTABLE_NOT_AVAILABLE_ON_HOST\n"
    )
    payload = {
        "schema_version": "p31-tt-provability-source-run/v1",
        "task_id": "P31-TT-PROVABILITY-TYPE-THEORY-CORPUS-001",
        "status": "SOURCE_AUDIT_COMPLETED_WITH_SCOPE / KERNEL_REPLAY_NOT_RUN_TOOLCHAIN_UNAVAILABLE",
        "remote": REMOTE,
        "commit": COMMIT,
        "commit_identity": log.stdout.splitlines(),
        "checkout": str(CHECKOUT),
        "checkout_clean": True,
        "agda_path": agda,
        "kernel_replay": "NOT_RUN_WITH_REASON_AGDA_EXECUTABLE_NOT_AVAILABLE_ON_HOST",
        "source_file_count": len(files),
        "source_manifest": "source-manifest.json",
        "literal_search": "literal-search.txt",
        "anchors": {
            "typed_lob_constructor": hits["Löb"],
            "box_or_quotation": hits["box"] + hits["⌜_⌝t"],
            "universal_todo_axiom": hits["⋆⋆TODO⋆⋆"],
            "postulates": hits["postulate"],
            "positivity_disabled": hits["no-positivity-check"],
            "termination_disabled": hits["no-termination-check"],
            "semantic_hole": hits["{!!}"],
            "hott_literal_hits": hits["HoTT"] + hits["univalence"] + hits["cubical"],
            "named_soundness_or_consistency_hits": hits["soundness"] + hits["consistency"],
        },
        "scope": "This is a fixed-source inspection. It does not run an Agda kernel and does not establish a theorem about this source, HoTT, or any reality task.",
    }
    (RUN / "RUN.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
