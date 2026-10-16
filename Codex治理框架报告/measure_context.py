#!/usr/bin/env python3
"""Codex 治理框架上下文成本测量脚本（调查报告配套工具）。

口径（见报告 002 分片）：
- est_tokens = CJK 字符数 × 1.0 + 非 CJK 字符数 ÷ 3.8
  （CJK≈1 token/字，ASCII/markdown≈3.8 字符/token，混合文本的经验估计，±20% 区间）
- 只统计文本内容字符，不含文件系统元数据。

用法：
  python3 measure_context.py <path>... [--ext .md,.json] [--top 30] [--sum-only]
"""
import argparse
import os
import sys


def is_cjk(ch):
    cp = ord(ch)
    return (
        0x4E00 <= cp <= 0x9FFF or 0x3400 <= cp <= 0x4DBF
        or 0x20000 <= cp <= 0x2A6DF or 0xF900 <= cp <= 0xFAFF
        or 0x3000 <= cp <= 0x303F or 0xFF00 <= cp <= 0xFFEF  # CJK标点/全角
    )


def measure_file(path):
    try:
        raw = open(path, "rb").read()
    except OSError:
        return None
    b = len(raw)
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("utf-8", "replace")
    cjk = sum(1 for c in text if is_cjk(c))
    other = len(text) - cjk
    est = cjk + other / 3.8
    return {"bytes": b, "lines": text.count("\n"), "cjk": cjk, "other": other,
            "tokens": est, "path": path}


def walk(paths, exts):
    rows = []
    for p in paths:
        if os.path.isfile(p):
            if os.path.splitext(p)[1] in exts:
                r = measure_file(p)
                if r:
                    rows.append(r)
        elif os.path.isdir(p):
            for root, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in
                           (".git", "__pycache__", "node_modules", ".pytest_cache")]
                for f in files:
                    if os.path.splitext(f)[1] in exts:
                        fp = os.path.join(root, f)
                        r = measure_file(fp)
                        if r:
                            rows.append(r)
    rows.sort(key=lambda r: -r["tokens"])
    return rows


def fmt(n):
    return f"{n:,.0f}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--ext", default=".md,.json")
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--sum-only", action="store_true")
    a = ap.parse_args()
    exts = set(a.ext.split(","))
    rows = walk(a.paths, exts)
    tot = {k: sum(r[k] for r in rows) for k in ("bytes", "lines", "cjk", "other", "tokens")}
    if not a.sum_only:
        print(f"{'est_tokens':>12} {'bytes':>10} {'lines':>7} {'cjk':>8}  path")
        for r in rows[: a.top]:
            print(f"{fmt(r['tokens']):>12} {fmt(r['bytes']):>10} {fmt(r['lines']):>7} "
                  f"{fmt(r['cjk']):>8}  {r['path']}")
        if len(rows) > a.top:
            print(f"... 共 {len(rows)} 个文件，仅显示前 {a.top}")
    print(f"TOTAL files={len(rows)} tokens≈{fmt(tot['tokens'])} bytes={fmt(tot['bytes'])} "
          f"lines={fmt(tot['lines'])} cjk={fmt(tot['cjk'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
