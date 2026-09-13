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
SAMPLE = "audit/understanding-claim-sample-batch8-20260912.json"

VERDICTS: dict[str, tuple[str, str]] = {
    "CL-000117": ("SUPPORTED", "用户原文引用（Z 铁律核心：前提改变必然导致结果改变）；与 KC-000018 一致。"),
    "CL-000136": ("PENDING", "解释性埋线判断（普朗克尺度为合取-量子化论证提前埋线）；属叙述判断。"),
    "CL-000156": ("SUPPORTED", "悖论生成定义条目（稠密性空间中无法完成现实可完成的事）；与 KC-000003/000019 一致。"),
    "CL-000176": ("PENDING", "解释性断言（三问文献把恢复条件对照列为标准步骤）；属核证性判断。"),
    "CL-000197": ("SUPPORTED", "KC-000018 解释条目（宾语精确限定为时间维度；朴素集合论把可描述/可构造/存在合一）；与 core 一致。"),
    "CL-000720": ("SUPPORTED", "用户指令原文（grep 文档、阅读、审计 HOTT_Z 另一个 AI 的认知）；与来源提取一致。"),
    "CL-000753": ("SUPPORTED", "史料学第三律条目（本日 38≠41）；与 T20/T21 个位数较真一致。"),
    "CL-000786": ("PENDING", "条目（Z-62/Z-70 是两条根）；需回源核对 Z-62/Z-70 原文后裁决。"),
    "CL-000819": ("PENDING", "残句（X∪Y 不一致+pₙ₊₁=¬pₙ 坍缩（R8））；需与 owner 上下文合并后裁决。"),
    "CL-000852": ("SUPPORTED", "docs/ 16 topic README 为职责定义 stub 的核对结论；与 docs/ 结构一致。"),
    "CL-000990": ("SUPPORTED", "B1 锚点系声明（E/T/G:ALL/C-T）；与 B1 正文一致。"),
    "CL-001044": ("PENDING", "残句（R016/R017 的种子在此）；需与上下文合并后裁决。"),
    "CL-001100": ("PENDING", "判断条目（真正缺口是『HoTT 特定悖论零交付』）；属研究判断。"),
    "CL-001155": ("SUPPORTED", "诚实边界条目（Fresh Session 未跑、Git 未版本闭合 HEAD dc1e369）；与 ALL-Markdown HEAD 历史一致。"),
    "CL-001210": ("PENDING", "技术条目（J 无判断计算规则、uses≠requires、三篇新论文接入）；需回源核对后裁决。"),
    "CL-001377": ("SUPPORTED", "B3 本期主线（Gemini 九轮→反射/迁移→暂停对齐→收尾三连）；与 response ledger 覆盖一致。"),
    "CL-001437": ("PENDING", "R035 trim 唯一性细节条目；需与 PROOF_NOTE 正文核对后裁决。"),
    "CL-001498": ("SUPPORTED", "R028 细节（234 模型检查、20 个全称模型无返回态）；与 B3 正文一致。"),
    "CL-001560": ("PENDING", "判断条目（研究质量比路径审视 v1 估计更高）；属评价性判断。"),
    "CL-001622": ("SUPPORTED", "R026 细节（P1-P6 已读、P2 类型路径不决定元素相等）；与 B3 第 129 行一致。"),
    "CL-001725": ("SUPPORTED", "边界声明（旧 E1–E5 标签不自动等于当前数学认证）；与 F-011 口径一致。"),
    "CL-001743": ("PENDING", "总账行（有限前缀可实现⇏单一无限相容执行，E2，R038）；行本身可回源，但 E2 分级需复核。"),
    "CL-001763": ("SUPPORTED", "三个 git 仓库 commit 数（ALL-Markdown 8、workspace 46+、AI对话录 2+）；与各仓库 log 一致。"),
    "CL-001782": ("SUPPORTED", "test_r036：28 tests、28 ran OK；与 B5 总账第 55 行一致。"),
    "CL-001801": ("PENDING", "起源夜条目（Agda 实编译 3 wrapper+9 自包含+Lean、E1 升级理由）；需回源核对执行记录后裁决。"),
    "CL-001820": ("SUPPORTED", "C0 边界声明（A/B 章节旧『已完成/全部覆盖/读态 F』属历史 transform 记录）；与 C0 定位一致。"),
    "CL-001836": ("SUPPORTED", "LocalGPT 分母行（186+34=220 visible assistant）；与 ledger-summary 的 220 一致。"),
    "CL-001852": ("PENDING", "快照计数 16,151 与 ledger-summary 的 16,209 不同；属分母口径差，需复核后裁决。"),
    "CL-001869": ("PENDING", "残句（SEMANTIC_WORK_PRODUCT_MAPPING_PENDING）；需与上下文合并后裁决。"),
    "CL-001885": ("SUPPORTED", "C0 NOT_PROVEN 边界（HoTT_is_GONE_COMPLETE 不证明等价覆盖 aistudio-docs）；与 A-AISTUDIO-COVERAGE-001 状态一致。"),
    "CL-001950": ("SUPPORTED", "恢复协议声明（凭方案+读遍账本恢复，不重读已勾项）；与方案头部一致。"),
    "CL-001984": ("PENDING", "批次 1 清单条目；需逐件核对清单完成度后裁决。"),
    "CL-002020": ("SUPPORTED", "批次 3 状态（r024 四计数 1928/1888/40/241 实物✓）；与 COMPILER_RESULTS 计数一致。"),
    "CL-002056": ("SUPPORTED", "背景引文（用户追问 ALL-Markdown 处理是否完整）；与用户原文一致。"),
    "CL-002091": ("SUPPORTED", "盘点条目（.codex/research/hott/ 290、全读）；与目录实况一致。"),
    "CL-002217": ("SUPPORTED", "读遍账本目的声明；与账本头部一致。"),
    "CL-002253": ("SUPPORTED", "完成节奏（每批更新账本+章节+commit）；与方案一致。"),
    "CL-002289": ("PENDING", "处置条目（元数据 JSON 已由正文覆盖）；属范围判断，未句级裁决。"),
    "CL-002326": ("PENDING", "实质新发现清单（B1§五六项）；需逐项回源核对后裁决。"),
    "CL-002363": ("SUPPORTED", "读态行（网页 GPT 55 节回复 F）；与 ledger-summary 55 一致。"),
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
        "cumulative_sampled": 282 + sum(counts.values()),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FILLED", "summary": payload["review_summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
