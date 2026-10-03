#!/usr/bin/env python3
"""Verify the frozen source denominator of the Pattern-P full-history audit.

The list is intentionally small and explicit. It checks byte-level source identity;
the U archive is append-only, so it checks its frozen prefix at the declared cutoff
and reports later appends separately. It does not decide whether a source is
semantically in scope, whether a user message was correctly interpreted, or whether
a tool change is justified. Those judgments remain in the full-history audit and its
Tool-BirthCards.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


SCHEMA_VERSION = "pattern-p-full-history-source-verification/v2"

EXPECTED = (
    ("S01", "sources/prompts/Codex-自反真理验证与理论经济学-用户原文-20260912.md", "e3db2ef6ce1bf93d0b484126b96d8e8b63a545f091eac32040e08f5aa9e449e2", 7, 3248),
    ("S02", "sources/prompts/Codex-知识谱自反与第三条发现路径-用户原文-20260916.md", "f26ef9b383e965a90d624ca0289b2179d1494767f9a746a320de349edfde093a", 7, 1797),
    ("S03", "sources/prompts/Codex-AI数学用好与超越-用户原文-20260916.md", "bc5b43837fccff4474324d079393c09328d941adaaa3edbcfe8a36eeff520e13", 14, 731),
    ("S04", "sources/prompts/Codex-理论是对现实的骨架式模仿-用户原文-20260916.md", "7beabdcb1e2b63a8c8013c5a76739da86e97a963d021435f9280324852833078", 17, 2028),
    ("S05", "sources/prompts/Codex-理论经济与针对性悖论策略-用户原文-20260922.md", "59f87cfb09a0c2124454759600ca538f6e035fdbb54024c539c2ea2fd041a565", 13, 2965),
    ("S06", "sources/prompts/Claude-归因是正题-用户原文-20260924.md", "89076899be25f75c4bcc8bdb92d9a08aae347c52d7e8b0c8a0904a18a43019a9", 9, 779),
    ("S07", "sources/prompts/Claude-罗素原则P1至P3-用户原文-20260926.md", "1b37b69fb305778006b10745a1bcff93e763a91ce932ca5142754d7f026ec226", 15, 1671),
    ("S08", "sources/prompts/GLM-算符先行于存在性落定-用户原文-20260926.md", "ac9b6600d708cfb19b59299e087d1ab0e7a1a9043d3e7fbd4fc7b79457d49034", 19, 2213),
    ("S09", "sources/prompts/Codex-非现实性悖论的目标与A向读法-用户原文-20260930.md", "6e04fc609f70998aef975d43c2dcc4fda9789d0360bad49029c4bd731d839734", 27, 3175),
    ("S10", "sources/prompts/Claude-UR与芝诺的模式匹配-用户原文-20260930.md", "a7577323fc91bbb3cb53df590362677282f65fd3f919e246f89666e6113e00d0", 43, 3841),
    ("S11", "sources/prompts/Codex-圆环与芝诺幽灵所指的澄清-用户原文-20261001.md", "53e9c4f551f5809ba8f40ce0bc543294c5e3e371a45d015497fced057eb915cc", 7, 498),
    ("S12", "sources/prompts/Codex-后续理论靶与罗素模式P-用户原文-20261002.md", "1cc94f9fdae3bc3c38484fb76e40f98022fd356c83fa0d82c9827732cccd04fa", 29, 3687),
    ("S13", "sources/prompts/Codex-模式P与一遍匹配-用户原文-20261002.md", "1b280968cc14702750d68de2b04314e3a017edfab08d67ec8d9ce425a94b184d", 9, 1100),
    ("R0", "dev-notes/0014 - 2026-09-17 - 哥德尔镜头下的四弹一体（收官综合）.md", "dc8f03b29e10b2550ab0830738136fb2ac7bc5589435e727ae69e50df46ef50c", 45, 6093),
    ("R1", "dev-notes/0015 - 2026-09-17 - 第四弹方案文档收官版（027 升华重写）.md", "0c0ad4d0d2e6c5f6a0c073158c826b4e6062b43801990357908322d9ecd7a388", 46, 4095),
    ("R2", "dev-notes/0102 - 2026-09-30 - 这个repo现在被Opus接手了，它推进了很多工作，它现在因为用量而中断了，我并不是要让你接手它的工作，它用量恢复了之后可以继续工作，但是....md", "3fd6c54820ba1d4b60020347f18310a76e80c8b0c07cb3d96e2bed7e25def848", 663, 67657),
    ("C", "dev-notes/0108 - 2026-10-02 - 我觉得你们找的都有问题，你看芝诺悖论打的是微积分的基础理论，极限理论，或者说实数理论、数轴都可以.md", "cb14057dc2155cfff60e47ec2666abd042f7816f494c1122d66a5014a96f0e62", 539, 57355),
    ("U", "dev-notes/0109 - 2026-10-02 - ZFC最大的问题，肯定在于对“时间维度”的把握上.md", "fd0c995bd31195514ef469583a1dc9b2e6624e043b451b1ecbe84c9a08247c55", 1849, 150776),
)

# This archive is extended by the required end-of-turn transcript writer. The full
# history audit is deliberately frozen through the final response to U19. Later
# turns are observable but do not silently enter the U1-U19 semantic denominator.
APPEND_ONLY_PREFIX_CUTOFFS = {
    "U": "through skill-turn-10e7913cb3e84d919199427c034b8358 terminal answer",
}


def verify(root: Path) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    failures: list[dict[str, object]] = []
    for identifier, relative, expected_sha, expected_lines, expected_bytes in EXPECTED:
        path = root / relative
        row: dict[str, object] = {"id": identifier, "path": relative}
        if not path.is_file():
            row["status"] = "MISSING"
            failures.append(row)
            rows.append(row)
            continue
        data = path.read_bytes()
        expected = {"sha256": expected_sha, "lines": expected_lines, "bytes": expected_bytes}
        if identifier in APPEND_ONLY_PREFIX_CUTOFFS:
            if len(data) < expected_bytes:
                actual = {
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "lines": data.count(b"\n"),
                    "bytes": len(data),
                }
                row.update({
                    "expected": expected,
                    "actual_prefix": actual,
                    "verification_scope": "APPEND_ONLY_PREFIX",
                    "cutoff": APPEND_ONLY_PREFIX_CUTOFFS[identifier],
                    "status": "TRUNCATED_BEFORE_CUTOFF",
                })
            else:
                prefix = data[:expected_bytes]
                actual = {
                    "sha256": hashlib.sha256(prefix).hexdigest(),
                    "lines": prefix.count(b"\n"),
                    "bytes": len(prefix),
                }
                appended = data[expected_bytes:]
                row.update({
                    "expected": expected,
                    "actual_prefix": actual,
                    "verification_scope": "APPEND_ONLY_PREFIX",
                    "cutoff": APPEND_ONLY_PREFIX_CUTOFFS[identifier],
                    "archive_current": {"lines": data.count(b"\n"), "bytes": len(data)},
                    "appended_after_cutoff": {"lines": appended.count(b"\n"), "bytes": len(appended)},
                })
                row["status"] = "PASS" if actual == expected else "MISMATCH"
        else:
            actual = {
                "sha256": hashlib.sha256(data).hexdigest(),
                "lines": data.count(b"\n"),
                "bytes": len(data),
            }
            row.update({"expected": expected, "actual": actual, "verification_scope": "FULL_FILE"})
            row["status"] = "PASS" if actual == expected else "MISMATCH"
        if row["status"] != "PASS":
            failures.append(row)
        rows.append(row)
    return {
        "schema_version": SCHEMA_VERSION,
        "root": str(root),
        "count": len(rows),
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "rows": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = verify(args.root.resolve())
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(f"{result['status']}: {result['count']} Pattern-P origin sources")
        for failure in result["failures"]:
            print(f"  {failure['id']}: {failure['status']} {failure['path']}")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
