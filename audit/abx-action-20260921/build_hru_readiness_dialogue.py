#!/usr/bin/env python3
"""Project an archived H/R question and answer verbatim into the ABX dossier."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "dev-notes/0093 - 2026-09-19 - 另外一个AI正在为你的审计报告增加索引，这不应该影响你继续工作.md"
MARKER = "<!-- conversation-archive-turn: skill-turn-00c6e386d3b94f2ab41ecce9cc031c5e "
TARGET = ROOT / "audit/abx-action-20260921/H-R-K查找思路整备/001 - 本轮完整问答与分类结论.md"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()
    source_bytes = SOURCE.read_bytes()
    source = source_bytes.decode("utf-8")
    start = source.index(MARKER)
    next_marker = source.find("<!-- conversation-archive-turn:", start + len(MARKER))
    block = source[start:] if next_marker == -1 else source[start:next_marker]
    if "### 用户提问" not in block or "### AI 最终回复" not in block:
        raise SystemExit("archived dialogue headings missing")
    text = (
        "<!-- governance-shard:v2\n"
        "logical_id: ABX-HRK-READINESS\n"
        "shard_id: 001\n"
        "index: ../H-R-K查找思路整备.md\n"
        "generated: build_hru_readiness_dialogue.py\n"
        "-->\n\n"
        "# 本轮完整问答与分类结论\n\n"
        "> 身份：MACHINE_GENERATED_VERBATIM_SOURCE_PROJECTION。\n"
        f"> 来源：{SOURCE.relative_to(ROOT)}；SHA-256：{sha(source_bytes)}。\n"
        "> 范围：下方从 conversation-archive marker 到下一 marker 的全部内容逐字复制；"
        "它保存用户关于第一弹、H/R 和新拓扑学的问题，以及当轮 AI 最终回复，"
        "不将其升级为数学定理。\n\n"
        + block
    )
    encoded = text.encode("utf-8")
    if args.write:
        TARGET.write_text(text, encoding="utf-8")
    elif args.check:
        if not TARGET.is_file():
            raise SystemExit(f"missing projection: {TARGET}")
        if TARGET.read_bytes() != encoded:
            raise SystemExit("projection differs from the archived dialogue source")
    print(f"source_sha256={sha(source_bytes)}")
    print(f"target_sha256={sha(encoded)}")
    print(f"target={TARGET.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
