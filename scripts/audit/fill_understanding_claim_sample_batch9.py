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
SAMPLE = "audit/understanding-claim-sample-batch9-20260912.json"

VERDICTS: dict[str, tuple[str, str]] = {
    "CL-000005": ("SUPPORTED", "KC-000004/000020 引文（芝诺幽灵在圆环悖论中再现）；与 core 一致。"),
    "CL-000028": ("PENDING", "长引文残片（T25 锋利表述开头）；需与完整引文一起裁决。"),
    "CL-000050": ("SUPPORTED", "攻击面精确化条目（前提层的时间处理）；与 KC-000011/000024 一致。"),
    "CL-000073": ("PENDING", "方向 B 残片（非计算性原则允许定义总分类函数）；需与 RP-B01 记录合并裁决。"),
    "CL-000095": ("SUPPORTED", "KC-000005 引文（批注轮开场）；与 core 一致。"),
    "CL-000326": ("SUPPORTED", "罗素悖论自指问题引文；与 A2 与来源一致。"),
    "CL-000348": ("PENDING", "解释条目（用户对旧文本态度：意思>措辞）；属判断性表述。"),
    "CL-000371": ("PENDING", "解释性综合（圆环是铁律的实验演示）；属判断条目。"),
    "CL-000395": ("SUPPORTED", "KC-000016 关键句（非法命题/程序不是理论的失败）；与 core 一致。"),
    "CL-000418": ("SUPPORTED", "A/B 两柜二分与针对 HoTT 的审查问句条目；与 C1/C3 结构一致。"),
    "CL-000531": ("SUPPORTED", "用户原文引用（问题在于理论本身是否有时间维度）；与 A4 与 core 时间线一致。"),
    "CL-000537": ("SUPPORTED", "解释条目（程序三构造强制考虑时序）；与 KC-000011 一致。"),
    "CL-000545": ("PENDING", "方法论条目（重要判据靠落盘进制度）；属叙述判断。"),
    "CL-000553": ("PENDING", "解释条目（堵住表述性辩护）；属判断性表述。"),
    "CL-000561": ("SUPPORTED", "四件工具按序使用清单（判据→问句→接口清单→公平条款）；与 A4/A10 一致。"),
    "CL-000623": ("SUPPORTED", "A6 路由元数据（W35/W41 附件转发等）；与 response ledger 一致。"),
    "CL-000637": ("SUPPORTED", "用户原文（W37 询问是否回信完整回应）；与来源一致。"),
    "CL-000649": ("PENDING", "论辩条目（『HIT/transport 遍历连续统卡死』收窄为归约停滞）；需回源核对后裁决。"),
    "CL-000662": ("SUPPORTED", "OUT-005 条目（撤 AllRealizable 过强目标）；与 B3/RP-B01 记录一致。"),
    "CL-000674": ("SUPPORTED", "提取接口拒绝=ASK 正面证据条目；与 N2/T4 审计判词一致。"),
    "CL-000991": ("SUPPORTED", "B1 可回源声明（父线程 186 + 主 34）；与 ledger-summary 220 一致。"),
    "CL-001045": ("PENDING", "AI 撤回记录（『矛盾种子』指分岔非内部 ⊥）；需回源核对后裁决。"),
    "CL-001101": ("PENDING", "A 章锚点增补条目（条件版失配定理出处=T12）；需回源核对。"),
    "CL-001156": ("SUPPORTED", "T18 计数（2,087 源→2,006 excerpt、131MB、18.39%）；与 A8 语料记录一致。"),
    "CL-001211": ("PENDING", "拒搬条目（QuasiInverseData 非 mere proposition 不得与 isEquiv 统一）；需回源核对后裁决。"),
    "CL-001378": ("SUPPORTED", "B3 表头（用户节/workspace 锚点/实际产物）；与 B3 三栏结构一致。"),
    "CL-001438": ("PENDING", "trim 细节条目（μ_w(v) 与分量查询能力区分、q=1−μ_w([])）；需回源核对。"),
    "CL-001499": ("SUPPORTED", "R028 引文（结论与前提都会被过度解释）；与 B3 正文一致。"),
    "CL-001561": ("PENDING", "判断条目（漂移判断被双重证实、质量高与方向偏同时为真）；属评价性判断。"),
    "CL-001623": ("SUPPORTED", "R026 P3 条目（线性 λ 权重不变量 w(A⊸B)=w(B)−w(A)）；与 B3 第 129 行一致。"),
    "CL-002176": ("SUPPORTED", "审计锚点声明（verify_ai_coverage.py 逐项核验存在性/计数）；脚本仍在。"),
    "CL-002182": ("SUPPORTED", "Gemini 分账（81=21+17+17+2+24）与 gemini-*.jsonl 及 summary 一致。"),
    "CL-002190": ("SUPPORTED", "R 系列 hash 核验点清单；与 workspace git log 记录一致。"),
    "CL-002198": ("SUPPORTED", "残片（exchange/rounds/R041-ZCODE-GOVERNANCE）；路径实体存在。"),
    "CL-002207": ("SUPPORTED", "关键条目（Gemini chunk15/72 机器证明宣称被 IN-002 撤回）；与 A6/B4 一致。"),
    "CL-002218": ("SUPPORTED", "读态四级定义（F/D/S/M）；与账本头部一致。"),
    "CL-002254": ("SUPPORTED", "111=56+55 三重确认；与历史账本 PASS 一致。"),
    "CL-002290": ("PENDING", "三栏对照零差异的核证性断言；需重放对照后裁决。"),
    "CL-002327": ("PENDING", "A11.2 原始出处条目（T5 直指复原）；需回源核对。"),
    "CL-002364": ("SUPPORTED", "读态行（Codex 38 轮 F）；与 186+34=220 与账本一致。"),
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
        "cumulative_sampled": 322 + sum(counts.values()),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FILLED", "summary": payload["review_summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
