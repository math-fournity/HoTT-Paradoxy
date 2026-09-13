#!/usr/bin/env python3
"""Fill the current AI's per-claim review verdicts for the batch-12 sample (N41).

Verdict vocabulary matches batches 1-11:
SUPPORTED / SUPERSEDED_BY_MACHINE_RESULT / UNSUPPORTED / PENDING.

Calibration used for batch 12 (same as batch 11):
- SUPPORTED: quotes, records, consistent conceptual clarifications and
  mechanically re-checked counts.
- SUPERSEDED_BY_MACHINE_RESULT: a historical status/gap that a later machine
  result or audit has taken over.
- PENDING: fragments, evaluative statements, unresolved caliber questions.
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SAMPLE = "audit/understanding-claim-sample-batch12-20260912.json"

VERDICTS: dict[str, tuple[str, str]] = {
    # A0
    "CL-000006": ("SUPPORTED", "Z 铁律前提的工具性/缺陷双读；与 core KC-000013/000015/000018 一致（研究立场，非数学结论）。"),
    "CL-000029": ("SUPPORTED", "用户原文（KC-000015 逐字句）；与 core 一致。"),
    "CL-000051": ("SUPPORTED", "成果形态判据（构造过程而非断言/综述）；与 C3 战略与 F-011 交付门禁一致。"),
    "CL-000074": ("PENDING", "解释性研究方针（追问经典定义在哪里被当成总算法）；需上下文合并后裁决。"),
    "CL-000096": ("SUPPORTED", "用户原文（KC-000005 逐字句）；与 core 一致。"),
    # A1
    "CL-000118": ("PENDING", "残句（小节标题「什么是抽象？」）；需与上下文合并。"),
    "CL-000137": ("SUPPORTED", "用户原文（Z 铁律最锋利表述；与 KC-000015 同源）。"),
    "CL-000157": ("PENDING", "残句（枚举项 (6) 的交叉引用）；需上下文合并。"),
    "CL-000177": ("SUPPORTED", "用户原文重复引用（A1 与 KC-000015 同源）；一致。"),
    "CL-000198": ("PENDING", "残句（枚举项 (2)）；需上下文合并。"),
    # A2
    "CL-000327": ("PENDING", "残句（Russell 叙述的单个句子）；需上下文合并。"),
    "CL-000349": ("PENDING", "评价性条目（「原文至上但不迷信原文」的示范）；属判断。"),
    "CL-000372": ("PENDING", "解释性映射条目（T15 幽灵再现论）；需回源与上下文。"),
    "CL-000396": ("SUPPORTED", "用户原文（KC-000016 逐字句）；与 core 一致。"),
    "CL-000419": ("SUPPORTED", "原始问法记录 + 后续三分律校准说明；与 A2/C2 记录一致（原始连线已标注为研究路标）。"),
    # B1
    "CL-000994": ("PENDING", "计数条目口径待核：B1 记 2,091 源→2,006 片段，batch 9 核过的 A8 记录为 2,087 源→2,006 excerpt；2,006 部分一致，源数差待回源。"),
    "CL-001048": ("SUPERSEDED_BY_MACHINE_RESULT", "该历史条件句已由 MP-ERCF-001（C-59–C-66：Lean 一般 Type 因子化 no-go + 正反控制）机器化接管；历史表述保留。"),
    "CL-001104": ("PENDING", "映射元数据条目（A4=temporally unindexed=T14）；需回源核对。"),
    "CL-001159": ("SUPPORTED", "治理设计条目（不可变 generation + 原子 CURRENT 切换）；与 LOAD_SET/STATE/cognition_runtime 实现一致。"),
    "CL-001214": ("SUPPORTED", "B1 引用的自我修正句（不让吸收外部资料导致研究目标漂移）；与 B1/治理记录一致。"),
    # B3
    "CL-001381": ("SUPPORTED", "WebGPT 记录行（W39→R024 对角编译器实测、OUT-004 草稿）；与 B3/R024 记录一致。"),
    "CL-001441": ("SUPPORTED", "概念条目（transport(ua(e),0) 非规范形≠发散）仍成立；本 repo MP-PATH-CERTIFICATE-001（C-100–C-105）已原生给出 ua 计算规则与路径控制。"),
    "CL-001502": ("SUPPORTED", "校正条目（「强规范系统绝不可能有自解释器」口号过强）与当前理解一致（S053/T3 边界）。"),
    "CL-001564": ("SUPERSEDED_BY_MACHINE_RESULT", "历史缺口已被接管：race/timeout 下降条件由 MP-RACE-TIMEOUT-001（C-71–C-76）机器闭合，RP-B01 由 N2 提取接口审计并 PARKED；历史描述（R039→R040 未开始）仍真。"),
    "CL-001626": ("SUPPORTED", "4,330 标签模型穷举与 workspace/artifacts/r027/FINITE_MODEL_RESULTS.json（labelled_models=4330）一致（batch 6 已核）。"),
    # B4
    "CL-001680": ("SUPPORTED", "inlineFile 更正条目（不再按 old「empty」处理）；与 ledger/lesson 4 及 Gemini 计数一致。"),
    "CL-001688": ("PENDING", "表格残行（时间线第 18 条）；需上下文合并。"),
    "CL-001696": ("PENDING", "解释性分期（共鸣期→冒进期→收敛期）；chunk 区间未逐项重核。"),
    "CL-001707": ("PENDING", "残句（「四处误判、五项发现：」后接列表）；需上下文合并。"),
    "CL-001715": ("PENDING", "开放缺口条目（6 个 IDEA 未系统消化、A11 应补记）；需回源核对 A11 是否已补记。"),
    # 全量精读工作方案
    "CL-001953": ("SUPPORTED", "Gemini 实质 chunk 24/24 与 ledger 计数一致（24 ordinary text；另 21 thought/17 code/17 exec/2 inlineFile 已核）；125KB 未单独复核。"),
    "CL-001986": ("PENDING", "残句（Archive.zip 同表处置）；需上下文合并。"),
    "CL-002022": ("SUPPORTED", "覆盖边界条目（R006–R015 artifacts 不在当前 repo）：现场核验 workspace/artifacts 从 r016 起、r006–r015 缺失；与 archive 旧 ZIP 记录一致。"),
    "CL-002058": ("PENDING", "残句（缺口列表引导句）；需上下文合并。"),
    "CL-002093": ("PENDING", "残句（recovered 106 逐份定性+关键读）；需上下文合并。"),
    # 读遍账本
    "CL-002220": ("PENDING", "引用块残句（创建时间与缘由）；需上下文合并。"),
    "CL-002256": ("SUPPORTED", "节 53P→54P 消息合并与 AI 回信引文；与消息提取/读遍账本记录一致。"),
    "CL-002292": ("SUPPORTED", "文件条目核验：workspace/scripts/research/r024_diagonal_machine.py 存在（7,304 bytes）；行数口径差记账（本包 wc -l=237，账本记 238 行）。"),
    "CL-002329": ("PENDING", "残句（枚举项 ④）；需上下文合并。"),
    "CL-002366": ("SUPPORTED", "workspace 计数现场核验：44 SESSION ✓、9 PROOF_NOTE ✓、10 reviews ✓（owner 8 份未单独复核）。"),
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
    extra = sorted(set(VERDICTS) - {e["claim_id"] for e in payload["entries"]})
    if extra:
        raise SystemExit(f"verdicts for unsampled claims: {extra}")
    payload["review_summary"] = {
        "schema_version": "understanding-claim-sample-batch12-review/v1",
        "verdicts": dict(counts),
        "total": sum(counts.values()),
        "e6_found": False,
        "caliber_items": [
            "CL-000994: 2,091 sources (B1) vs 2,087 sources (A8/batch 9); the 2,006-excerpt figure matches.",
            "CL-002292: file line count 237 (wc -l) vs 238 recorded in the ledger.",
        ],
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FILLED", "verdicts": dict(counts), "total": sum(counts.values())}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
