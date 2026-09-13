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
SAMPLE = "audit/understanding-claim-sample-batch7-20260912.json"

VERDICTS: dict[str, tuple[str, str]] = {
    "CL-000004": ("SUPPORTED", "KC-000004 引文与转述（极限理论用 N→∞ 处理芝诺）；与核心认知一致。"),
    "CL-000027": ("SUPPORTED", "KC 引用（『像芝诺/罗素/圆环一样精彩的 HoTT 悖论』）；与 T24 记录一致。"),
    "CL-000049": ("PENDING", "解释性断言（这一轮比 T15 多出四个精确件）；属叙述判断，未句级裁决。"),
    "CL-000072": ("PENDING", "问题残句（为什么任务被理论化绑上难题）；属研究问题条目，需与上下文合并裁决。"),
    "CL-000094": ("SUPPORTED", "KC-000002 逐字引用（Theory Schema 必要性）；与 core 一致。"),
    "CL-000325": ("SUPPORTED", "A2 用户说条目（罗素悖论：所有不含自身的集合）；与来源提取一致。"),
    "CL-000347": ("PENDING", "残句（『我的理解：三个信号。』）；需与 owner 上下文合并后裁决。"),
    "CL-000370": ("SUPPORTED", "W22 引文（圆环被拿掉一点无法还原）；与 KC-000010 一致。"),
    "CL-000394": ("SUPPORTED", "KC-000016 引文（罗素构造是不可计算过程）；与 core 一致。"),
    "CL-000417": ("PENDING", "路由残句（以及成本论（A3.6 展开））；需与上下文合并后裁决。"),
    "CL-000441": ("SUPPORTED", "用户批注轮原文（计算合法性/非法命题）；与 A3 与 sources 提取一致。"),
    "CL-000457": ("SUPPORTED", "KC-000012/000013 引文（人们希望绕过 ASK）；与 core 一致。"),
    "CL-000475": ("SUPPORTED", "KC-000022 逐字引用（第二类：理论假装已完成）；与 core 一致。"),
    "CL-000491": ("PENDING", "解释性断言（ASK 不只是入口检查）；属综合判断，未句级裁决。"),
    "CL-000511": ("PENDING", "成本论解释（时序对平凡问题是纯成本）；与 A3.6 阐述一致但属解释性表述，未句级裁决。"),
    "CL-000719": ("SUPPORTED", "用户指令原文（去 aistudio-docs 找 HoTT 文件提炼到 HoTT 子目录）；与来源提取一致。"),
    "CL-000752": ("SUPPORTED", "史料学第三律（个位数较真：2087≠2094）；与 T20/T21 记录一致。"),
    "CL-000785": ("SUPPORTED", "保全分类条目（经典数学常识件：参考性、排除）；与 A8 正文一致。"),
    "CL-000818": ("PENDING", "残句（必要条件+省略≠否定+抽象不变量充要定理（R7））；需与 owner 上下文合并后裁决。"),
    "CL-000851": ("SUPPORTED", "GONE 判决书条目（COMPLETE 版为同文扩编）；与来源原件一致。"),
    "CL-000884": ("SUPPORTED", "A9 归档声明（后勤/推进轮在章末按推进含义归档）；与 A9 正文结构一致。"),
    "CL-000896": ("SUPPORTED", "用户原文（W9 要求把回复整理成 .codex Skill）；与来源一致。"),
    "CL-000909": ("SUPPORTED", "用户原文（W32 禁 inline、代码写入 scripts 后调用）；与 rulings 一致。"),
    "CL-000922": ("SUPPORTED", "『这份交接包就是该轮指令的产物』与 R040/R041 交接记录一致。"),
    "CL-000935": ("SUPPORTED", "治理清单条目（代码先落盘再执行，W31/W32）；与 rulings 一致。"),
    "CL-000989": ("SUPPORTED", "读态边界声明（F/M 读态不是模型理解认证）；与 README/C0 边界一致。"),
    "CL-001043": ("PENDING", "问题残句（judgmental equality 是否擦除归约轨迹？）；需与上下文合并裁决。"),
    "CL-001099": ("PENDING", "解释性修正（§三『数学推进少』需精确化）；属判断条目，未句级裁决。"),
    "CL-001154": ("PENDING", "T17 细节条目（五 wave 执行、SHA 前缀、IMPLEMENTED_PENDING_FRESH_）；需逐件核对后裁决。"),
    "CL-001209": ("PENDING", "六项补充计划条目（语法—语义模型、相干性、同名概念对照）；属计划性表述，未句级裁决。"),
    "CL-001264": ("SUPPORTED", "B2 分母声明（56 Prompt/55 Response/111 section 以 C0 与 webgpt-section-ledger 为准）；与账本一致。"),
    "CL-001285": ("SUPPORTED", "R017 条目（W32 指令内嵌、禁 inline 入宪）；与 rulings 一致。"),
    "CL-001308": ("PENDING", "R028 细节条目（43,690 延迟塔枚举、16 万能固定点器候选全败、510 自然性实例）；需回源核对后裁决。"),
    "CL-001330": ("SUPPORTED", "表头标记（轮/SESSION 实物新增/PROOF_NOTE 正文核验）；与 B2 三栏结构一致。"),
    "CL-001351": ("SUPPORTED", "R030 条（§9.1 源码字面像枚举恢复正例）；与 B2 正文一致。"),
    "CL-001376": ("SUPPORTED", "B3 锚点系声明（W 节、A:R{xxx}、G:WS）；与 B3 正文一致。"),
    "CL-001435": ("SUPPORTED", "R035 判据细节（8,191 轨迹+4,096 单射样本）；与 B3 第 63 行一致。"),
    "CL-001497": ("SUPPORTED", "R028 条目（reach_trap 量词过强）；与 B3 正文一致。"),
    "CL-001559": ("PENDING", "修正性判断（B3§二-三『局限』段需修正、多个实质纸笔定理）；属判断条目，未句级裁决。"),
    "CL-001621": ("SUPPORTED", "R026 矩阵条目（C-12—C-16 仅动证据字段）；与 C-矩阵记录一致。"),
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
        "cumulative_sampled": 242 + sum(counts.values()),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FILLED", "summary": payload["review_summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
