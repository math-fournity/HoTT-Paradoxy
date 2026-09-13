#!/usr/bin/env python3
"""Migrate one existing Markdown document into a v2 shard index (migration tool).

Read-only by default.  ``--apply`` writes the index and the shard files.
Content is moved, never rewritten: each shard carries a marker block, one H1
title line and then the original lines verbatim, so concatenating the shard
bodies in index order reproduces the original file byte for byte.  A JSON
reconciliation report is always produced.

This is migration tooling, not a standing splitter: after migration the shards
are the canonical text and are edited directly (topical owner shard, or the
sequential append target).
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
TABLE_START = "<!-- governance-shard-table:start -->"
TABLE_END = "<!-- governance-shard-table:end -->"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def split_sections(lines: list[str]) -> tuple[list[str], list[tuple[str, int]]]:
    """Return the preamble and the ordered ``## `` sections with their line offsets."""
    offsets = [i for i, line in enumerate(lines) if line.startswith("## ")]
    if not offsets:
        raise ValueError("NO_H2_SECTIONS")
    preamble = lines[: offsets[0]]
    sections = []
    for position, start in enumerate(offsets):
        end = offsets[position + 1] if position + 1 < len(offsets) else len(lines)
        sections.append((lines[start][3:].strip(), start, end))
    return preamble, sections


def build_index(logical_id: str, mode: str, stem: str, shards: list[dict], title: str) -> str:
    last = f"{stem}/{shards[-1]['id']} - {shards[-1]['title']}.md"
    append = last if mode == "sequential" else "-"
    rows = "\n".join(
        f"| {row['id']} | [{row['title']}](<{stem}/{row['id']} - {row['title']}.md>) | {row['scope']} | current |"
        for row in shards
    )
    return (
        f"<!-- governance-shard-index:v2\n"
        f"logical_id: {logical_id}\n"
        f"mode: {mode}\n"
        f"shard_root: {stem}\n"
        f"last_shard: {last}\n"
        f"append_target: {append}\n"
        f"soft_line_target: 300\n"
        f"-->\n\n"
        f"# {title}\n\n"
        f"> 逻辑文档索引。读取顺序 = 本索引 + 下表全部分片；300 行是写作软目标，不是上限。\n"
        f"> 合同：`docs/quality/长治理文档分片与索引合同.md`。\n\n"
        f"{TABLE_START}\n"
        f"| Shard | 文件 | 语义范围 | 状态 |\n|---|---|---|---|\n{rows}\n{TABLE_END}\n"
    )


def shard_text(logical_id: str, index_rel: str, shard_id: str, title: str, body: list[str]) -> str:
    backlink = "../" + PurePosixPath(index_rel).name
    return (
        f"<!-- governance-shard:v2\nlogical_id: {logical_id}\nshard_id: {shard_id}\nindex: {backlink}\n-->\n\n"
        f"# {title}\n\n" + "".join(body)
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--path", required=True, help="canonical Markdown path, relative to the repo root")
    parser.add_argument("--plan", type=Path, required=True, help="shard plan JSON")
    parser.add_argument("--report", type=Path, required=True, help="reconciliation report JSON")
    parser.add_argument("--apply", action="store_true", help="write index and shard files")
    args = parser.parse_args()
    root = args.project_root.resolve()
    target = root / args.path
    original = target.read_bytes()
    lines = original.decode("utf-8").splitlines(keepends=True)
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    logical_id, mode, stem = plan["logical_id"], plan["mode"], PurePosixPath(args.path).stem
    if mode not in ("topical", "sequential"):
        raise SystemExit("MODE_INVALID")
    preamble, sections = split_sections(lines)
    by_title: dict[str, tuple[int, int]] = {}
    for title, start, end in sections:
        if title in by_title:
            raise SystemExit(f"DUPLICATE_SECTION_TITLE:{title}")
        by_title[title] = (start, end)
    used: list[str] = []
    built: list[dict] = []
    for row in plan["shards"]:
        body: list[str] = []
        for title in row["sections"]:
            if title not in by_title:
                raise SystemExit(f"SECTION_NOT_FOUND:{title}")
            if title in used:
                raise SystemExit(f"SECTION_REUSED:{title}")
            used.append(title)
        first = by_title[row["sections"][0]][0]
        last = by_title[row["sections"][-1]][1]
        body.append("".join(lines[first:last]))
        if row["id"] == plan["shards"][0]["id"]:
            body.insert(0, "".join(preamble))
        text = shard_text(logical_id, args.path, row["id"], row["title"], body)
        rel = f"{stem}/{row['id']} - {row['title']}.md"
        built.append({"id": row["id"], "title": row["title"], "scope": row.get("scope", row["title"]),
                      "path": rel, "text": text, "body": "".join(body)})
    ordered_titles = [title for title, _, _ in sections]
    if used != ordered_titles:
        raise SystemExit("SECTIONS_NOT_CONTIGUOUS_OR_INCOMPLETE")
    reconstructed = "".join(row["body"] for row in built)
    report = {
        "schema_version": "shard-migration-report/v1",
        "path": args.path,
        "logical_id": logical_id,
        "mode": mode,
        "shard_root": stem,
        "original_lines": len(lines),
        "original_bytes": len(original),
        "original_sha256": sha(original),
        "reconstructed_sha256": sha(reconstructed.encode("utf-8")),
        "content_preserved": reconstructed == original.decode("utf-8"),
        "sections": ordered_titles,
        "shards": [{"id": row["id"], "title": row["title"], "path": row["path"],
                    "lines": len(row["body"].splitlines(keepends=True))} for row in built],
    }
    if not report["content_preserved"]:
        raise SystemExit("CONTENT_NOT_PRESERVED")
    if args.apply:
        (root / f"{stem}").mkdir(parents=True, exist_ok=True)
        for row in built:
            (root / row["path"]).write_text(row["text"], encoding="utf-8")
        target.write_text(
            build_index(logical_id, mode, stem, built, plan.get("title", logical_id)), encoding="utf-8"
        )
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "APPLIED" if args.apply else "DRY_RUN", "path": args.path,
                      "shards": len(built), "content_preserved": True, "report": str(args.report)},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
