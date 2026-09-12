#!/usr/bin/env python3
"""Build the integrated repo's deterministic source/provenance manifest.

The manifest is an evidence index, not a semantic truth database. It records
source repo identity, dirty boundaries, copied snapshot trees, explicit source
files, and the user-removed aistudio-docs boundary. It never reads or writes
the private trajectory directory.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "sources" / "SOURCE_MANIFEST.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if result.returncode != 0:
        return f"COMMAND_FAILED({result.returncode}): {result.stderr.strip()}"
    return result.stdout.strip()


def repo_identity(label: str, path: Path) -> dict[str, object]:
    status = run_git(path, "status", "--short", "--branch")
    head = run_git(path, "rev-parse", "HEAD")
    branch = run_git(path, "branch", "--show-current")
    tags = run_git(path, "tag", "--sort=-creatordate")
    return {
        "id": label,
        "path": str(path),
        "head": head,
        "branch": branch,
        "commit_count_head": run_git(path, "rev-list", "--count", "HEAD"),
        "status_line_count": len(status.splitlines()) if status else 0,
        "status_sha256": hashlib.sha256(status.encode("utf-8")).hexdigest(),
        "status_preview": status.splitlines()[:80],
        "tags_preview": tags.splitlines()[:40],
    }


def tree_manifest(rel_root: str) -> dict[str, object]:
    root = ROOT / rel_root
    rows: list[dict[str, object]] = []
    total_bytes = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.is_symlink():
            continue
        if ".git" in path.parts or path.name == ".DS_Store" or "__pycache__" in path.parts:
            continue
        rel = path.relative_to(root).as_posix()
        size = path.stat().st_size
        file_hash = sha256_file(path)
        rows.append({"path": rel, "bytes": size, "sha256": file_hash})
        total_bytes += size
    tree_digest = hashlib.sha256()
    for row in rows:
        tree_digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True).encode("utf-8"))
        tree_digest.update(b"\n")
    return {
        "root": rel_root,
        "file_count": len(rows),
        "total_bytes": total_bytes,
        "tree_sha256": tree_digest.hexdigest(),
        "files": rows,
    }


def explicit_file(path: Path, source_role: str) -> dict[str, object]:
    exists = path.is_file()
    row: dict[str, object] = {
        "path": str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path),
        "source_role": source_role,
        "exists": exists,
    }
    if exists:
        row.update({"bytes": path.stat().st_size, "sha256": sha256_file(path)})
    return row


def main() -> None:
    sources = [
        repo_identity("dialogues-repo", ROOT / "AI对话录"),
        repo_identity("webgpt-workspace-repo", ROOT / "workspace"),
        repo_identity("all-markdown-repo", Path("/Volumes/D/ALL-Markdown")),
    ]
    snapshot_roots = [
        tree_manifest("HoTT"),
        tree_manifest("理解章节"),
        tree_manifest("sources/local-gpt/ALL-Markdown-root"),
        tree_manifest("sources/webgpt/workspace-snapshot"),
        tree_manifest("sources/understanding-transform/AI对话录"),
    ]
    explicit = [
        explicit_file(ROOT / "sources/prompts/Codex-HoTT-2-用户消息提取-20260911.md", "USER_PROMPT_EXTRACT"),
        explicit_file(ROOT / "sources/prompts/ChatGPT-HoTT-Main-用户消息提取-20260911.md", "USER_PROMPT_EXTRACT"),
        explicit_file(ROOT / "sources/prompts/Gemini-AI对话录-用户消息提取-20260911.md", "USER_PROMPT_EXTRACT"),
        explicit_file(ROOT / "sources/prompts/Codex-HoTT父线程-01a059c1-用户消息提取-20260911.md", "CODEX_LINEAGE_SUPPLEMENT"),
        explicit_file(ROOT / "sources/prompts/Codex-并行会话-素数与归档-用户消息提取-20260911.md", "CODEX_AUXILIARY_LINEAGE"),
        explicit_file(ROOT / "sources/webgpt/ChatGPT-HoTT - Main-20260911-1222.md", "WEBGPT_VISIBLE_EXPORT"),
        explicit_file(ROOT / "sources/gemini/Gemini - AI 对话录.json", "GEMINI_RAW_EXPORT"),
        explicit_file(ROOT / "sources/local-gpt/Codex-HoTT-2-完整38轮-用户与AI-20260911.md", "CODEX_VISIBLE_MERGED_EXPORT"),
        explicit_file(ROOT / "sources/local-gpt/HoTT_is_GONE_COMPLETE.md", "HISTORICAL_AI_ARTIFACT"),
        explicit_file(ROOT / "sources/local-gpt/HoTT_is_GONE_and_GONE_with_the_Wind.md", "HISTORICAL_AI_ARTIFACT"),
    ]
    payload = {
        "schema_version": "hott-integrated-source-manifest/v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "integrated_repo_root": str(ROOT),
        "source_repos": sources,
        "snapshot_roots": snapshot_roots,
        "explicit_files": explicit,
        "removed_sources": [
            {
                "path": "/Volumes/D/ALL-Markdown/aistudio-docs/",
                "status": "USER_REMOVED",
                "read_policy": "EXCLUDED_BY_USER",
                "replacement_candidate": "/Volumes/D/ALL-Markdown/HoTT_is_GONE_COMPLETE.md",
                "coverage_status": "NOT_PROVEN",
                "legacy_validator_status": "BLOCKED_SOURCE_REMOVED",
            }
        ],
        "private_trajectory_policy": {
            "directory": str(ROOT / "private-audit"),
            "git_status": "GITIGNORED",
            "reason": "raw trajectory may contain private instructions and hidden reasoning; public ledgers retain visible evidence and locators",
        },
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "output": str(OUT),
        "repo_count": len(sources),
        "snapshot_count": len(snapshot_roots),
        "explicit_file_count": len(explicit),
        "snapshot_files": sum(int(x["file_count"]) for x in snapshot_roots),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
