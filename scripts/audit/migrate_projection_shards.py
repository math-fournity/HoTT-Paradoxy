#!/usr/bin/env python3
"""Migrate 方向追踪.md / 全景视野.md into v2 shard indexes (projection-specific).

Two differences from ``shard_migrate_document.py`` matter:

* the original preamble (H1, 版本/日期/状态, the ``integrated-*-portfolio:vN``
  marker block) stays in the INDEX, because the runtime and the freshness
  verifier read those fields from the physical projection path;
* the big direction/result table is split into row shards by explicit row
  groups, so each family gets its own shard; the table header lines are
  repeated once per row shard (Markdown needs them) and that repetition is the
  only permitted extra content.

Reconciliation is line-exact: every original line must be consumed exactly
once; the table header may be consumed once per row shard; nothing else may be
duplicated and nothing may be dropped.

Read-only unless ``--apply``; ``--emit-bundle`` writes the generated texts to
JSON for use inside a checkpoint payload (required for MUTABLE projections).
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
TABLE_START = "<!-- governance-shard-table:start -->"
TABLE_END = "<!-- governance-shard-table:end -->"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def split_sections(lines: list[str]) -> tuple[list[str], list[tuple[str, int, int]]]:
    offsets = [i for i, line in enumerate(lines) if line.startswith("## ")]
    if not offsets:
        raise ValueError("NO_H2_SECTIONS")
    preamble = lines[: offsets[0]]
    sections = []
    for position, start in enumerate(offsets):
        end = offsets[position + 1] if position + 1 < len(offsets) else len(lines)
        sections.append((lines[start][3:].strip(), start, end))
    return preamble, sections


def table_parts(lines: list[str], start: int, end: int) -> tuple[int, int, int]:
    """Return (header_start, first_row, last_row) inside a table section."""
    header = next((i for i in range(start, end) if lines[i].lstrip().startswith("|")), None)
    if header is None or header + 1 >= end or not lines[header + 1].lstrip().startswith("|"):
        raise ValueError("TABLE_HEADER_NOT_FOUND")
    last = header + 1
    while last + 1 < end and lines[last + 1].lstrip().startswith("|"):
        last += 1
    return header, header + 2, last


def expand_rows(spec) -> list[int]:
    out: list[int] = []
    for item in spec:
        if isinstance(item, int):
            out.append(item)
        elif isinstance(item, list) and len(item) == 2:
            out.extend(range(item[0], item[1] + 1))
        else:
            raise ValueError(f"ROW_SPEC_INVALID:{item!r}")
    return out


def build_index(logical_id: str, stem: str, last: str, preamble: list[str], rows: list[dict]) -> str:
    table = "\n".join(
        f"| {row['id']} | [{row['title']}](<{stem}/{row['id']} - {row['title']}.md>) | {row['scope']} | current |"
        for row in rows
    )
    return (
        f"<!-- governance-shard-index:v2\n"
        f"logical_id: {logical_id}\n"
        f"mode: topical\n"
        f"shard_root: {stem}\n"
        f"last_shard: {last}\n"
        f"append_target: -\n"
        f"soft_line_target: 300\n"
        f"-->\n\n"
        + "".join(preamble)
        + "\n> 读取规则：**本索引 + 上表全部分片 = 逻辑文档全文**；缺任一 shard 即未完成全文加载"
          "（runtime 3.3.0 强制全片覆盖）。修改时在原位 owner shard 收敛，不追加“最新版”覆盖块。\n\n"
        + f"{TABLE_START}\n| Shard | 文件 | 语义范围 | 状态 |\n|---|---|---|---|\n{table}\n{TABLE_END}\n"
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--path", required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--emit-bundle", type=Path, help="write generated texts to JSON without touching the repo")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    root = args.project_root.resolve()
    original = (root / args.path).read_bytes()
    lines = original.decode("utf-8").splitlines(keepends=True)
    plan = json.loads(args.plan.read_text(encoding="utf-8"))
    stem = PurePosixPath(args.path).stem
    preamble, sections = split_sections(lines)
    by_title = {title: (start, end) for title, start, end in sections}
    table_title = plan["table_section"]
    if table_title not in by_title:
        raise SystemExit("TABLE_SECTION_NOT_FOUND")
    t_start, t_end = by_title[table_title]
    header_start, first_row, last_row = table_parts(lines, t_start, t_end)
    header = lines[header_start:first_row]
    row_count = last_row - first_row + 1

    used_lines: collections.Counter = collections.Counter(lines)
    # the preamble stays in the index verbatim (identity/status/marker fields)
    consumed: collections.Counter = collections.Counter(preamble)
    row_owner: dict[int, str] = {}
    built: list[dict] = []
    for row in plan["shards"]:
        parts: list[str] = []
        row_ids: list[str] = []
        if row.get("rows"):
            indexes = expand_rows(row["rows"])
            if row["id"] == plan["heading_shard"]:
                heading = lines[t_start:header_start]
                parts.append("".join(heading))
                consumed.update(heading)
            parts.append("".join(header))
            consumed.update(header)
            for index in indexes:
                if not 0 <= index < row_count:
                    raise SystemExit(f"ROW_INDEX_OUT_OF_RANGE:{index}")
                if index in row_owner:
                    raise SystemExit(f"ROW_ASSIGNED_TWICE:{index}")
                row_owner[index] = row["id"]
                line = lines[first_row + index]
                parts.append(line)
                consumed[line] += 1
                row_ids.append(line.split("`")[1])
            # trailing lines after the table belong to the shard that consumes the last row
            if max(indexes) == row_count - 1:
                trailing = lines[last_row + 1 : t_end]
                if trailing:
                    parts.append("".join(trailing))
                    consumed.update(trailing)
        for title in row.get("sections", []):
            if title not in by_title:
                raise SystemExit(f"SECTION_NOT_FOUND:{title}")
            start, end = by_title[title]
            if title == table_title:
                raise SystemExit("TABLE_SECTION_MUST_BE_ROWS")
            for line in lines[start:end]:
                consumed[line] += 1
            parts.append("".join(lines[start:end]))
        content = "".join(parts)
        link = f"{stem}/{row['id']} - {row['title']}.md"
        built.append({"id": row["id"], "title": row["title"], "scope": row["scope"], "link": link,
                      "path": (PurePosixPath(args.path).parent / link).as_posix(),
                      "rows": row_ids, "lines": content.count("\n"),
                      "text": (f"<!-- governance-shard:v2\nlogical_id: {plan['logical_id']}\n"
                               f"shard_id: {row['id']}\nindex: ../{PurePosixPath(args.path).name}\n-->\n\n"
                               f"# {row['title']}\n\n" + content)})

    missing_rows = sorted(set(range(row_count)) - set(row_owner))
    if missing_rows:
        raise SystemExit(f"ROWS_UNASSIGNED:{missing_rows[:10]}")
    residue = used_lines - consumed
    extra = consumed - used_lines
    row_shards = sum(1 for row in built if row["rows"])
    expected_extra = collections.Counter({line: row_shards - 1 for line in header}) if row_shards > 1 else collections.Counter()
    extra_ok = extra == expected_extra
    report = {
        "schema_version": "projection-shard-migration-report/v1",
        "path": args.path,
        "logical_id": plan["logical_id"],
        "original_lines": len(lines),
        "original_bytes": len(original),
        "original_sha256": sha(original),
        "row_count": row_count,
        "row_shards": {row["id"]: row["rows"] for row in built if row["rows"]},
        "residue_lines": sorted(residue.elements())[:10],
        "extra_lines": sorted(extra.elements())[:10],
        "content_preserved_once": not residue,
        "duplication_is_table_header_only": bool(extra_ok),
        "shards": [{"id": row["id"], "title": row["title"], "path": row["path"],
                    "lines": row["lines"], "rows": len(row["rows"])} for row in built],
    }
    if not (report["content_preserved_once"] and report["duplication_is_table_header_only"]):
        raise SystemExit("RECONCILIATION_FAILED")
    index_text = build_index(plan["logical_id"], stem, built[-1]["link"], preamble, built)
    if args.apply and args.emit_bundle is None:
        (root / PurePosixPath(args.path).parent / stem).mkdir(parents=True, exist_ok=True)
        for row in built:
            (root / row["path"]).write_text(row["text"], encoding="utf-8")
        (root / args.path).write_text(index_text, encoding="utf-8")
    if args.emit_bundle is not None:
        args.emit_bundle.parent.mkdir(parents=True, exist_ok=True)
        args.emit_bundle.write_text(json.dumps({
            "schema_version": "shard-migration-bundle/v1",
            "index_path": args.path,
            "index_text": index_text,
            "shards": [{"path": row["path"], "text": row["text"]} for row in built],
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "APPLIED" if (args.apply and args.emit_bundle is None) else "DRY_RUN",
                      "path": args.path, "shards": len(built), "rows": row_count,
                      "content_preserved_once": report["content_preserved_once"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
