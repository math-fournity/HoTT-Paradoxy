#!/usr/bin/env python3
"""Extract ONLY the research sponsor's own prompts from the ZCode session DB.

ZCode-side counterpart of codex_user_prompts_extract.py. Reads
~/.zcode/cli/db/db.sqlite read-only; keeps messages with role=="user" that have
no metadata.source / synthetic markers (todo reminders, agent-listing deltas,
fork markers are dropped); body text comes from the part table (type=="text").
Writes one Markdown file per session into the output dir, plus _INDEX.md.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

DB_PATH = Path.home() / ".zcode" / "cli" / "db" / "db.sqlite"
DEFAULT_OUT = Path(__file__).resolve().parent.parent / "zcode"


def ts_to_local(ms: int) -> str:
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).astimezone().strftime(
        "%Y-%m-%dT%H:%M:%S"
    )


def is_real_user(data: dict) -> bool:
    if data.get("role") != "user":
        return False
    meta = data.get("metadata") or {}
    if data.get("synthetic") or meta.get("synthetic"):
        return False
    if meta.get("source") or data.get("source"):
        return False
    return True


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--project-filter", default="hott",
                    help="substring match on session.project_id (case-insensitive)")
    args = ap.parse_args(argv)

    db = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    sessions = db.execute(
        "SELECT id, project_id FROM session ORDER BY id"
    ).fetchall()
    picked = [(s, p) for s, p in sessions if args.project_filter.lower() in (p or "").lower()]
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    index_rows = []
    total = 0
    for sid, project in picked:
        msgs = db.execute(
            "SELECT id, time_created, data FROM message WHERE session_id=? "
            "ORDER BY time_created, id", (sid,)
        ).fetchall()
        rows = []
        for mid, tcre, data in msgs:
            try:
                d = json.loads(data)
            except Exception:
                continue
            if not is_real_user(d):
                continue
            parts = db.execute(
                "SELECT data FROM part WHERE message_id=? AND json_extract(data,'$.type')='text' "
                "ORDER BY time_created, id", (mid,)
            ).fetchall()
            text = "\n".join(
                (json.loads(p[0]).get("text") or "")
                for p in parts if p[0]
            ).strip()
            if text:
                rows.append((tcre, text))
        if not rows:
            continue
        day = ts_to_local(rows[0][0])[:10]
        name = f"{day}-{sid.replace('sess_','')[:8]}-{len(rows)}p.md"
        out = out_dir / name
        lines = [
            f"# 用户提示词：ZCode 会话 {sid}",
            "",
            f"> 项目：{project}｜首条时间：{ts_to_local(rows[0][0])}｜用户消息 {len(rows)} 条",
            "> 身份：仅研究发起人发出的内容；已剔除 todo 提醒等系统注入。",
            "",
        ]
        for tcre, text in rows:
            lines.append(f"## {ts_to_local(tcre)}")
            lines.append("")
            lines.append("~~~~text")
            lines.append(text)
            lines.append("~~~~")
            lines.append("")
        out.write_text("\n".join(lines), encoding="utf-8")
        index_rows.append((day, sid, len(rows), project, name))
        total += len(rows)
    db.close()
    with open(out_dir / "_INDEX.md", "w") as fh:
        fh.write("# ZCode 侧用户提示词索引\n\n")
        fh.write(f"会话 {len(index_rows)} 个，用户消息共 {total} 条。\n\n")
        fh.write("| 日期 | 会话 | 条数 | 项目 | 文件 |\n|---|---|---|---|---|\n")
        for day, sid, n, project, name in sorted(index_rows):
            fh.write(f"| {day} | `{sid.replace('sess_','')[:8]}` | {n} | `{project}` | {name} |\n")
    print(json.dumps({"platform": "zcode", "sessions": len(index_rows),
                      "total_prompts": total, "out": str(out_dir)}, ensure_ascii=False))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
