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
SAMPLE = "audit/understanding-claim-sample-batch10-20260912.json"

VERDICTS: dict[str, tuple[str, str]] = {
    "CL-000266": ("SUPPORTED", "A11 纪律声明（每条注明证据来源）；与 A11 正文体例一致。"),
    "CL-000277": ("PENDING", "解释性判断（『我不相信』是方向押注、未被正面构造回应）；属判断条目。"),
    "CL-000289": ("SUPPORTED", "W51 条目（HoTT 已消化已知悖论家族——防御面）；与 C9 的 W51-1/W51-2 判词一致。"),
    "CL-000300": ("SUPPORTED", "回源机制声明（按句级审计账本定位）；账本与脚本存在。"),
    "CL-000311": ("PENDING", "AI 自白引文条目（R009 的『停留在证明表示不够』）；引文与 B3 一致，但『双重自白』综合属解释。"),
    "CL-000442": ("SUPPORTED", "用户原文（有些命题不具可计算性）；与 A3 与 KC-000012 一致。"),
    "CL-000458": ("SUPPORTED", "KC-000013 引文（所有悖论本质是不可停机/不合法问题被拿到理论中推演）；与 core 一致。"),
    "CL-000476": ("SUPPORTED", "KC-000022 逐字引用（两种你都能找到并机器证明吗？）；与 core 一致。"),
    "CL-000493": ("SUPPORTED", "ASK 追踪条目（依据被略过：尚未形成的对象直接被使用）；与 A3 的追踪表一致。"),
    "CL-000512": ("SUPPORTED", "『悖论恰是时序是影响因子的非平凡问题』与 KC-000024 一致。"),
    "CL-000570": ("SUPPORTED", "用户原文（结合提取文档询问最根本怀疑点）；与来源提取一致。"),
    "CL-000580": ("SUPPORTED", "校准条目（自指线校准为 self-metatheory/reflection gap；旧 G≃Map(1,G) 公式无效）；与 A11 与 W51 记录一致。"),
    "CL-000590": ("SUPPORTED", "KC-000025 引文（为什么你们找起来这么慢）；与 core 一致。"),
    "CL-000601": ("SUPPORTED", "KC-000027 自引全文（HoTT 已消化已知悖论家族、程序界限成为它的问题）；与 core 一致。"),
    "CL-000611": ("PENDING", "解释性判断（研究前沿与用户认知前沿错位）；属综合判断。"),
    "CL-000992": ("SUPPORTED", "B1 表头（产物/锚点/内容）；与 B1 三栏体例一致。"),
    "CL-001046": ("SUPPORTED", "形式化条目（强否定 vs 结构否定三分）；与 B1 与五类否定记录一致。"),
    "CL-001102": ("PENDING", "出处映射条目（A2.2 六值审计状态=T8）；需回源核对后裁决。"),
    "CL-001157": ("SUPPORTED", "manager 1.1.0 条目（19 份非问答候选全文保留、否定 ±40 行窗口方案）；与 B1 与方案记录一致。"),
    "CL-001212": ("PENDING", "残句（外部依赖图箭头未注明关系种类）；需与上下文合并后裁决。"),
    "CL-001265": ("SUPPORTED", "B2 锚点系声明（W 节/R:W/A:R/G:WS）；与 B2 一致。"),
    "CL-001286": ("SUPPORTED", "R004 条目（rev16 稀疏挂载修复 restore_rev16.py）；与 B2 与 workspace 记录一致。"),
    "CL-001309": ("SUPPORTED", "R004 条目（PermissionError→独立包 HoTT_R001_skill_execution）；与 B2 一致。"),
    "CL-001331": ("SUPPORTED", "条目（R004-ENTRY：v1.3.0 ZIP 恢复 225 文件）；与 B2/artifacts 记录一致。"),
    "CL-001352": ("SUPPORTED", "R014 条目（E_mark 证据族显式构造）；与 B2 与 A:R 记录一致。"),
    "CL-001379": ("SUPPORTED", "B3 行（W36 IN-002 大撤退信；G:WS:3e529cd/8e6641d；未寄出辩论稿带出处保留）；与 B3 与 commit 记录一致。"),
    "CL-001439": ("SUPPORTED", "R041 关键句（商掉冗余历史、不必商掉完成能力；困难在接口而非商规则）；与 R041 与 C-71–C-76 判词一致。"),
    "CL-001500": ("SUPPORTED", "R029 条目（d(x)=not(E(x,x)) 完整对角、代码即数据）；与 B3 正文一致。"),
    "CL-001562": ("SUPPORTED", "时间线新证（A_k 逆极限例在 R038 非 R036）；与 B3 与 R038 记录一致。"),
    "CL-001624": ("SUPPORTED", "P5 条目（同语句异语境交付 ⟺ 答案落入交集 ⋂Ans(u,c)）；与 B3 第 129 行一致。"),
    "CL-001952": ("SUPPORTED", "方案读态行（网页 55/55 节、503KB、F 级）；与历史账本 PASS 一致。"),
    "CL-001985": ("PENDING", "archive 处置条目（324 份原件、748MB、逐份定性）；数字与 STORE 一致，但『已审计』范围判断需逐份核。"),
    "CL-002021": ("SUPPORTED", "r028 重跑条目（234/20/10·11）；与 B3 的 234 模型检查记录一致。"),
    "CL-002057": ("PENDING", "盘点条目（find 排除 aistudio-docs/.git 得 7,420 文件）；需重放盘点后裁决。"),
    "CL-002092": ("PENDING", "盘点条目（scripts/session+recovered+tools 274、session 全读 117）；需重放核对。"),
    "CL-002125": ("SUPPORTED", "文档自述（升级工程调查结论+执行方案、可审计）；与文档结构一致。"),
    "CL-002134": ("SUPPORTED", "出处陷阱条目：workspace 确实**没有** scripts/governance/r017_…（实际存在的是 scripts/research/r017_local_execution.py 与 scripts/session/r017_cognition.py），与条目所说『文件系统自述不可作为项目状态变更证据』一致。"),
    "CL-002144": ("SUPPORTED", "章节映射条目（B2-治理与研究：W1-W34 ↔ R004-R019）；与文件名与 R 记录一致。"),
    "CL-002155": ("SUPPORTED", "锚点系条目（R:G{chunk} Gemini 24 条）；与 gemini ledger 24 一致。"),
    "CL-002165": ("PENDING", "计划条目（A 系列 11 章各增【AI 工作对照】小节）；属计划/状态描述，需核完成度。"),
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
        "cumulative_sampled": 362 + sum(counts.values()),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FILLED", "summary": payload["review_summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
