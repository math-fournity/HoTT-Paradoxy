#!/usr/bin/env python3
"""Extract ONLY the research sponsor's own prompts from Codex rollout files.

Derived from the canonical trajectory-gui-ref-export workflow (pdag-isolated-runner-route);
deliberately does NOT modify the canonical tool. This extractor:
  * reads rollout .jsonl.zst streams (sessions/ + archived_sessions/);
  * keeps response_item/message with role=="user" ONLY;
  * drops known host injections by text prefix (# AGENTS.md instructions,
    <app-context>, <environment_context>, <user_instructions>, <turn_aborted>,
    # Codex desktop context, <ENVIRONMENT_CONTEXT>);
  * KEEPS "# Files pasted by the user:" wraps (user-pasted content) with a marker;
  * writes one Markdown file per session into the output dir, plus _INDEX.md.

Modes:
  extract  --list <ts\tcwd\tpath file> [--out DIR]     extract prompts for listed files
  scan     [--out DIR]                                   rescan ALL rollouts' first-line cwd,
                                                         build HoTT list, then extract
  keyword  [--out DIR] [--keywords ...]                  stream-scan NON-HoTT rollouts for
                                                         keyword hits (fallback net)
Privacy: user text only; no assistant replies, no reasoning, no tool bodies.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import subprocess
import sys
from pathlib import Path

CODEX_SESSIONS = Path("~/.codex/sessions").expanduser()
CODEX_ARCHIVED = Path("~/.codex/archived_sessions").expanduser()
DEFAULT_OUT = Path(__file__).resolve().parent.parent / "codex"
INJECT_PREFIXES = (
    "# AGENTS.md instructions",
    "<app-context>",
    "<environment_context>",
    "<ENVIRONMENT_CONTEXT>",
    "<user_instructions>",
    "<turn_aborted>",
    "# Codex desktop context",
    "<permissions",
    "<app-signal",
    "<external_codex_apps",
    "<codex_internal_context",
    "<recommended_plugins",
    "# Files pasted by the user:",  # handled separately below
)
DEFAULT_KEYWORDS = ("HoTT", "悖论", "芝诺", "ZFC", "形式化与机器证明")


def iter_lines(path: Path):
    proc = subprocess.Popen(["zstdcat", str(path)], stdout=subprocess.PIPE)
    for line in proc.stdout:
        yield line
    proc.wait()


def first_line_meta(path: Path) -> dict:
    for line in iter_lines(path):
        try:
            d = json.loads(line)
        except Exception:
            return {}
        return d.get("payload", {}) or {}
    return {}


def user_texts(path: Path):
    """Yield (timestamp, is_paste, text) for every real user message."""
    for line in iter_lines(path):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("type") != "response_item":
            continue
        p = d.get("payload") or {}
        if p.get("type") != "message" or p.get("role") != "user":
            continue
        content = p.get("content") or []
        texts = [
            c.get("text", "")
            for c in content
            if isinstance(c, dict) and c.get("type") in ("input_text", "text")
        ]
        text = "\n".join(t for t in texts if t)
        if not text.strip():
            continue
        stripped = text.lstrip()
        if stripped.startswith("# Files pasted by the user:"):
            yield d.get("timestamp", ""), True, text
            continue
        if any(stripped.startswith(pre) for pre in INJECT_PREFIXES):
            continue
        yield d.get("timestamp", ""), False, text


def session_id_of(path: Path) -> str:
    stem = path.name
    # rollout-<ts>-<uuid>.jsonl.zst -> uuid
    parts = stem.split("-")
    if len(parts) >= 8:
        return "-".join(parts[-5:]).replace(".jsonl.zst", "")
    return stem


def extract_one(path: Path, meta: dict, out_dir: Path) -> dict:
    sid = meta.get("session_id") or session_id_of(path)
    ts0 = meta.get("timestamp", "")
    day = ts0[:10] if ts0 else "unknown-date"
    rows = list(user_texts(path))
    if not rows:
        return {"session": sid, "prompts": 0, "file": None}
    name = f"{day}-{sid[:8]}-{len(rows)}p.md"
    out = out_dir / name
    lines = [
        f"# 用户提示词：Codex 会话 {sid}",
        "",
        f"> 时间：{ts0}｜工作目录：`{meta.get('cwd','?')}`｜"
        f"用户消息 {len(rows)} 条（含粘贴 {sum(1 for _, p, _ in rows if p)} 条）",
        "> 身份：仅研究发起人发出的内容；已剔除 AGENTS 注入等环境消息。",
        "",
    ]
    for ts, is_paste, text in rows:
        tag = "（用户粘贴的文件）" if is_paste else ""
        lines.append(f"## {ts}{tag}")
        lines.append("")
        lines.append("~~~~text")
        lines.append(text.rstrip())
        lines.append("~~~~")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return {"session": sid, "prompts": len(rows), "file": str(out), "cwd": meta.get("cwd",""), "day": day}


def load_list(list_file: Path):
    for line in list_file.read_text().splitlines():
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) >= 3:
            yield parts[2]
        elif len(parts) == 1:
            yield parts[0]


def cmd_extract(args):
    out_dir = Path(args.out); out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for p in load_list(Path(args.list)):
        path = Path(p)
        if not path.is_file():
            results.append({"session": str(path), "prompts": 0, "file": None, "error": "missing"})
            continue
        meta = first_line_meta(path)
        results.append(extract_one(path, meta, out_dir))
    write_index(out_dir, results)
    total = sum(r["prompts"] for r in results)
    print(json.dumps({"mode": "extract", "sessions": len(results), "total_prompts": total,
                      "out": str(out_dir)}, ensure_ascii=False))


def cmd_scan(args):
    out_dir = Path(args.out); out_dir.mkdir(parents=True, exist_ok=True)
    files = sorted(glob.glob(str(CODEX_SESSIONS / "**" / "*.zst"), recursive=True)
                   + glob.glob(str(CODEX_ARCHIVED / "*.zst")))
    results = []
    for i, f in enumerate(files):
        meta = first_line_meta(Path(f))
        cwd = meta.get("cwd", "")
        if "HoTT" in cwd or "hott" in cwd.lower():
            results.append(extract_one(Path(f), meta, out_dir))
        if (i + 1) % 50 == 0:
            print(f"...scanned {i+1}/{len(files)}", file=sys.stderr)
    write_index(out_dir, results)
    total = sum(r["prompts"] for r in results)
    print(json.dumps({"mode": "scan", "files_scanned": len(files), "hott_sessions": len(results),
                      "total_prompts": total, "out": str(out_dir)}, ensure_ascii=False))


def cmd_keyword(args):
    keywords = args.keywords or DEFAULT_KEYWORDS
    out_dir = Path(args.out)
    files = sorted(glob.glob(str(CODEX_SESSIONS / "**" / "*.zst"), recursive=True)
                   + glob.glob(str(CODEX_ARCHIVED / "*.zst")))
    hits = []
    for i, f in enumerate(files):
        path = Path(f)
        meta = first_line_meta(path)
        cwd = meta.get("cwd", "")
        if "HoTT" in cwd or "hott" in cwd.lower():
            continue  # already covered
        found = set()
        for line in iter_lines(path):
            try:
                s = line.decode("utf-8", "ignore")
            except Exception:
                continue
            for kw in keywords:
                if kw in s:
                    found.add(kw)
            if len(found) == len(keywords):
                break
        if found:
            hits.append((str(path), cwd, ",".join(sorted(found))))
        if (i + 1) % 50 == 0:
            print(f"...keyword-scanned {i+1}/{len(files)}", file=sys.stderr)
    kf = out_dir.parent / "source" / "codex-keyword-hits.txt"
    kf.parent.mkdir(parents=True, exist_ok=True)
    with open(kf, "w") as fh:
        for p, c, k in hits:
            fh.write(f"{c}\t{k}\t{p}\n")
    print(json.dumps({"mode": "keyword", "scanned": len(files), "hits": len(hits),
                      "list": str(kf)}, ensure_ascii=False))


def write_index(out_dir: Path, results):
    rows = sorted((r for r in results if r.get("file")), key=lambda r: (r.get("day",""), r["session"]))
    with open(out_dir / "_INDEX.md", "w") as fh:
        fh.write("# Codex 侧用户提示词索引（按会话时间）\n\n")
        fh.write(f"会话 {len(rows)} 个，用户消息共 {sum(r['prompts'] for r in rows)} 条。\n\n")
        fh.write("| 日期 | 会话 | 条数 | 工作目录 | 文件 |\n|---|---|---|---|---|\n")
        for r in rows:
            fh.write(f"| {r.get('day','')} | `{r['session'][:8]}` | {r['prompts']} | "
                     f"`{r.get('cwd','?')}` | {Path(r['file']).name} |\n")


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract"); e.add_argument("--list", required=True); e.add_argument("--out", default=str(DEFAULT_OUT))
    s = sub.add_parser("scan"); s.add_argument("--out", default=str(DEFAULT_OUT))
    k = sub.add_parser("keyword"); k.add_argument("--out", default=str(DEFAULT_OUT)); k.add_argument("--keywords", nargs="*")
    args = ap.parse_args(argv)
    {"extract": cmd_extract, "scan": cmd_scan, "keyword": cmd_keyword}[args.cmd](args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
