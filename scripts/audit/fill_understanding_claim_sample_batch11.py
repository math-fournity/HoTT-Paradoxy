#!/usr/bin/env python3
"""Fill the current AI's per-claim review verdicts for the batch-5 sample (N16).

Verdict vocabulary matches batches 1-4:
SUPPORTED / SUPERSEDED_BY_MACHINE_RESULT / UNSUPPORTED / PENDING.
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SAMPLE = "audit/understanding-claim-sample-batch11-20260912.json"

VERDICTS: dict[str, tuple[str, str]] = {
    "CL-000216": ("SUPPORTED", "W8 用户引文（自主运行、系统化寻找）；与来源提取一致。"),
    "CL-000225": ("SUPPORTED", "G10 用户引文（机器证明要真的在沙盒中运行过）；与 KC-000021 一致。"),
    "CL-000236": ("SUPPORTED", "RP-OPEN 清单条目；与 A10 的开放方向记录一致。"),
    "CL-000245": ("PENDING", "评价性判断（用户方法论最完整成文）；属解释条目。"),
    "CL-000256": ("PENDING", "残句（源头 A1.3）；需与上下文合并后裁决。"),
    "CL-000721": ("PENDING", "残句（审视它的工作包分解）；需与上下文合并后裁决。"),
    "CL-000754": ("SUPPORTED", "史料学第四律（形态诚实，T19）；与 A8 五律一致。"),
    "CL-000787": ("SUPPORTED", "交接包最强综合结论条目（Z-73/74/81/94；三重不完备）；与 canonical 台账记录一致。"),
    "CL-000820": ("SUPPORTED", "残句（R9 未完成 stub）；与 A8 记录一致。"),
    "CL-000853": ("SUPPORTED", "canonical/governance/AGENTS.md（1,842 行、§12–22 与台账互证）；与来源结构一致。"),
    "CL-000886": ("PENDING", "问句残片（是不是没有使用 depth=1？）；需与上下文合并后裁决。"),
    "CL-000897": ("SUPPORTED", "W11/W12 用户引文（Skill 必须每次完整加载认知闭包、跨压缩）；与治理要求一致。"),
    "CL-000910": ("PENDING", "解释条目（代码的史料学：过程代码是证据）；属判断性表述。"),
    "CL-000923": ("SUPPORTED", "用户治理终极态度（治理本身是可交接资产、简版等于没有）；与 W42 与治理记录一致。"),
    "CL-000936": ("SUPPORTED", "治理条目（工作认知跨压缩保全，W42）；与 Skill/LOAD_SET 设计一致。"),
    "CL-000993": ("SUPPORTED", "语料基线条目（G:ALL:dc1e369、16 文件 12,444 行迁入 HoTT/sources）；与 ALL-Markdown 历史一致。"),
    "CL-001047": ("SUPPORTED", "形式陈述条目（Γ_S≢Γ_T ⇒ Cn 不等；集合级铁律严格成立）；与 B1 的形式化记录一致。"),
    "CL-001103": ("PENDING", "出处映射条目（A2.4 SameMissingOrigin=T13）；需回源核对。"),
    "CL-001158": ("SUPPORTED", "五类结构统计类别（qa_dialogue/prompt_response/headed_prose/unheaded_prose）；与 manager 分类一致。"),
    "CL-001213": ("PENDING", "解释性条目（Cubical 最强默认是工程建议；Lean Eq 取值于 Prop）；属技术判断，需回源核对。"),
    "CL-001380": ("SUPPORTED", "B3 行（W38 IN-003 缠绕数；G:WS:38d6d70；OUT-003 草稿）；与 R023 记录一致。"),
    "CL-001440": ("SUPPORTED", "R016 条目（68 份源码回收+300 来源映射+4 commit，d726b2e 起）；与 B2/B3 一致。"),
    "CL-001501": ("SUPPORTED", "R029 引文（只需覆盖这一项：使用它自己作取反）；与 B3 一致。"),
    "CL-001563": ("SUPPORTED", "『逻辑+几何+程序』精确化版本由 R035 保存；与 R035 记录一致。"),
    "CL-001625": ("SUPPORTED", "R027 条目（先 commit 07ee915 保全新 IN-006 再研究）；与 B3 一致。"),
    "CL-001726": ("SUPPORTED", "B5 定位声明（交接级文档、新 AI 不读原始记录也知有什么/证据多硬）；与 B5 结构一致。"),
    "CL-001744": ("SUPPORTED", "silent-steps 行（弱互模拟保 may 不保 must）；与 R039 一致。"),
    "CL-001764": ("SUPPORTED", "R040 完整交接包+onboarding 导览；与交接记录一致。"),
    "CL-001783": ("SUPPORTED", "test_r038 28/28；与 B5 总账第 55 行一致。"),
    "CL-001802": ("SUPPORTED", "11 项入 B1§五（漂移诊断/直指复原/最锋利表述三条件版等）；与 B1 记录一致。"),
    "CL-001903": ("SUPPORTED", "README 边界（A/B 章节与旧读态终态为历史 transform，不能覆盖 C0/manifest/ledger）；与 README 头部一致。"),
    "CL-001911": ("SUPPORTED", "版本链（v1=1d12edb→v2=1ccb299→9ee73e2→46bf864…）；与历史 commit 一致。"),
    "CL-001920": ("SUPPORTED", "README 索引行（A3 覆盖诞生/命名/定义/四变体/中途失效/时序成本论）；与 A3 正文一致。"),
    "CL-001929": ("SUPPORTED", "README 索引行（B0 三时代编年总线）；与 B0 正文一致。"),
    "CL-001938": ("SUPPORTED", "C0 路由声明（只负责当前判定和路由，逐条需回源 ledger）；与 C0 一致。"),
    "CL-002219": ("SUPPORTED", "账本可审计声明（F/D 项可由后续 AI 重读复核）；与账本体例一致。"),
    "CL-002255": ("PENDING", "『导出中有 3 处非交替』为核证性断言；需重放后裁决。"),
    "CL-002291": ("PENDING", "进度条目（新增 6 项实物细节入 B3§六）；需核完成度。"),
    "CL-002328": ("SUPPORTED", "B1§五条目（T6 四层时间+不可擦除测试+temporally unindexed 首出处）；与 B1 一致。"),
    "CL-002365": ("SUPPORTED", "读态行（Gemini 24 实质 chunk+17 code+17 execresult+thought 抽样 F+全扫）；与账本一致。"),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--sample", type=Path, default=None)
    args = parser.parse_args()
    root = args.project_root.resolve()
    path = args.sample or (root / SAMPLE)
    payload = json.loads(path.read_text(encoding="utf-8"))
    counts = collections.Counter()
    missing = []
    for entry in payload["entries"]:
        verdict = VERDICTS.get(entry["claim_id"])
        if verdict is None:
            missing.append(entry["claim_id"])
            continue
        entry["review_verdict"], entry["review_reason"] = verdict
        counts[entry["review_verdict"]] += 1
    if missing:
        raise SystemExit(f"missing verdicts: {missing}")
    payload["review_summary"] = {
        "SUPPORTED": counts["SUPPORTED"],
        "SUPERSEDED_BY_MACHINE_RESULT": counts["SUPERSEDED_BY_MACHINE_RESULT"],
        "UNSUPPORTED": counts["UNSUPPORTED"],
        "PENDING": counts["PENDING"],
        "total": sum(counts.values()),
        "cumulative_sampled": 402 + sum(counts.values()),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FILLED", "summary": payload["review_summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
