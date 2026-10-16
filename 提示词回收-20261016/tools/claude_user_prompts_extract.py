#!/usr/bin/env python3
"""Extract ONLY the research sponsor's own prompts from Claude Code session JSONLs.

Claude-side counterpart of codex_user_prompts_extract.py. Scans
~/.claude/projects/<dir>/*.jsonl; keeps type=="user" messages whose text is a
real typed prompt (or a user paste), dropping host injections with known
prefixes (compaction summaries, usage-limit notices, cut-off resume directives,
command echoes, system reminders) and tool_result-only rows.
Writes one Markdown file per session into the output dir, plus _INDEX.md.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECTS = Path.home() / ".claude" / "projects"
DEFAULT_OUT = Path(__file__).resolve().parent.parent / "claude"
DROP_PREFIXES = (
    "[Request interrupted by user",  # kept? this IS user action but not text; drop body-empty
    "This session is being continued",
    "[Usage limit reached",
    "[Earlier usage-limit notes",
    "Your response above was cut off",
    "<command-name>",
    "<command-message>",
    "<local-command-caveat>",
    "<local-command-stdout>",
    "<system-reminder>",
    "<system-warning>",
)


def decode_project_dir(name: str) -> str:
    return name.lstrip("-")


def extract_session(jsonl: Path):
    rows = []
    with open(jsonl, encoding="utf-8", errors="ignore") as fh:
        for line in fh:
            try:
                d = json.loads(line)
            except Exception:
                continue
            if d.get("type") != "user" or d.get("isMeta"):
                continue
            m = d.get("message") or {}
            meta = m.get("metadata") or {}
            if meta.get("source") or meta.get("synthetic") or d.get("synthetic"):
                continue
            c = m.get("content")
            if isinstance(c, str):
                text = c
            elif isinstance(c, list):
                texts = [b.get("text", "") for b in c
                         if isinstance(b, dict) and b.get("type") == "text"]
                text = "\n".join(texts)
            else:
                continue
            text = text.strip()
            if not text:
                continue
            if any(text.startswith(p) for p in DROP_PREFIXES):
                continue
            ts = d.get("timestamp", "")
            is_paste = text.startswith("<pasted_content")
            rows.append((ts, is_paste, text))
    return rows


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    ap.add_argument("--match", default="HoTT", help="substring on project dir name")
    args = ap.parse_args(argv)

    dirs = sorted(p for p in PROJECTS.iterdir() if p.is_dir() and args.match in p.name)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    index_rows = []
    total = 0
    for proj in dirs:
        for jsonl in sorted(proj.glob("*.jsonl")):
            try:
                rows = extract_session(jsonl)
            except Exception as e:
                print(f"WARN {jsonl.name}: {e}", file=sys.stderr)
                continue
            if not rows:
                continue
            day = (rows[0][0] or "")[:10] or "unknown"
            name = f"{day}-{jsonl.stem[:8]}-{len(rows)}p.md"
            out = out_dir / name
            lines = [
                f"# 用户提示词：Claude 会话 {jsonl.stem}",
                "",
                f"> 项目目录：`{decode_project_dir(proj.name)}`｜用户消息 {len(rows)} 条"
                f"（含粘贴 {sum(1 for _, p, _ in rows if p)} 条）",
                "> 身份：仅研究发起人发出的内容；已剔除压缩摘要/限额提示/命令回显等注入。",
                "",
            ]
            for ts, is_paste, text in rows:
                tag = "（用户粘贴）" if is_paste else ""
                lines.append(f"## {ts}{tag}")
                lines.append("")
                lines.append("~~~~text")
                lines.append(text.rstrip())
                lines.append("~~~~")
                lines.append("")
            out.write_text("\n".join(lines), encoding="utf-8")
            index_rows.append((day, jsonl.stem, len(rows), decode_project_dir(proj.name), name))
            total += len(rows)
    with open(out_dir / "_INDEX.md", "w") as fh:
        fh.write("# Claude 侧用户提示词索引\n\n")
        fh.write(f"项目目录 {len(dirs)} 个（含 HoTT），会话 {len(index_rows)} 个，"
                 f"用户消息共 {total} 条。\n\n")
        fh.write("| 日期 | 会话 | 条数 | 项目目录 | 文件 |\n|---|---|---|---|---|\n")
        for day, sid, n, proj, name in sorted(index_rows):
            fh.write(f"| {day} | `{sid[:8]}` | {n} | `{proj}` | {name} |\n")
    print(json.dumps({"platform": "claude", "project_dirs": len(dirs),
                      "sessions": len(index_rows), "total_prompts": total,
                      "out": str(out_dir)}, ensure_ascii=False))


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
