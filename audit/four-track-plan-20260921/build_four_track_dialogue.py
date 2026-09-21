#!/usr/bin/env python3
"""Project the four-branch answer verbatim into the future-work plan."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'dev-notes/0093 - 2026-09-19 - 另外一个AI正在为你的审计报告增加索引，这不应该影响你继续工作.md'
MARKER = '<!-- conversation-archive-turn: skill-turn-a1d733e345b64dac8c3e05f9658c7e21 '
TARGET = ROOT / 'HoTT后续研究总体方案/001 - 上一轮问答与四分支校正.md'


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def render() -> tuple[bytes, bytes]:
    source_bytes = SOURCE.read_bytes()
    source = source_bytes.decode('utf-8')
    start = source.index(MARKER)
    next_marker = source.find('<!-- conversation-archive-turn:', start + len(MARKER))
    block = source[start:] if next_marker == -1 else source[start:next_marker]
    if '### 用户提问' not in block or '### AI 最终回复' not in block:
        raise SystemExit('archived dialogue headings missing')
    text = (
        '<!-- governance-shard:v2\n'
        'logical_id: HOTT-FOUR-TRACK-PLAN\n'
        'shard_id: 001\n'
        'index: ../HoTT后续研究总体方案.md\n'
        'generated: build_four_track_dialogue.py\n'
        '-->\n\n'
        '# 上一轮问答与四分支校正\n\n'
        '> 身份：MACHINE_GENERATED_VERBATIM_SOURCE_PROJECTION。\n'
        f'> 来源：{SOURCE.relative_to(ROOT)}；SHA-256：{sha(source_bytes)}。\n'
        '> 范围：下方从本 turn marker 到下一 marker 的全部内容逐字复制；它保存用户关于 K、理论问题与四分支的提问，以及当轮 AI 最终回复，不将其升级为数学定理。\n\n'
        + block
    )
    return source_bytes, text.encode('utf-8')


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    source_bytes, rendered = render()
    if args.write:
        TARGET.parent.mkdir(parents=True, exist_ok=True)
        TARGET.write_bytes(rendered)
    elif args.check:
        if not TARGET.is_file():
            raise SystemExit(f'missing projection: {TARGET}')
        if TARGET.read_bytes() != rendered:
            raise SystemExit('projection differs from the archived dialogue source')
    print(f'source_sha256={sha(source_bytes)}')
    print(f'target_sha256={sha(rendered)}')
    print(f'target={TARGET.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
