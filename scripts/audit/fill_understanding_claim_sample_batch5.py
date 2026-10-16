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
SAMPLE = "audit/understanding-claim-sample-batch5-20260912.json"

VERDICTS: dict[str, tuple[str, str]] = {
    "CL-000265": ("SUPPORTED", "A11 的范围自述（对 171 轮做完整理解后识别未闭合结构）；与句级账本的 171 遍历单元一致。"),
    "CL-000276": ("PENDING", "解释性综合（自指线与时间线并行、自指线只产出条件界）；属叙述判断，未句级裁决。"),
    "CL-000288": ("SUPPORTED", "用户原文引用（G20/W44 的『为什么你们找起来这么慢』）；与 core KC-000025 一致。"),
    "CL-000299": ("PENDING", "『经 workspace 治理记录、OUT 七封信、G12 任务书间接核证』为核证性范围断言，需逐件核对后才可裁决。"),
    "CL-000310": ("SUPPORTED", "路由：本目录句级账本与五类锚点即该口径事件产物；文件与锚点账本均存在。"),
    "CL-000622": ("SUPPORTED", "A6 路由元数据（W33–W45 转发轮），与 response ledger 的网页覆盖一致。"),
    "CL-000636": ("SUPPORTED", "完成性陈述『全部落盘到应该落盘的文件中』；七封信与 IN/OUT 记录在 workspace 与顶层来源中可回源。"),
    "CL-000648": ("SUPPORTED", "OUT-001 清算内容（哥德尔不完备≠语法崩溃≠不停机；独立性/卡住/不可判定三分）与 B3/A6 正文一致。"),
    "CL-000661": ("SUPPORTED", "寄存器机 8 指令、2N+9、31 单测、1,928 组对照（40 UNKNOWN）与 STATE `P-DIAGONAL-MACHINE` 记录一致。"),
    "CL-000673": ("PENDING", "解释性扩充（χ/EM_H/RP-B01 = B 方向骨架定理的对应）；与 C9 部分重叠，需按 C9 重述后裁决。"),
    "CL-000948": ("SUPPORTED", "路由：当前分母/来源 hash/ledger 覆盖由 C0 owner；与 C0 现状一致。"),
    "CL-000955": ("SUPPORTED", "网页线时间与 111 节、workspace 治理记录与 ledger-summary（webgpt_sections=111、56 user 消息）一致。"),
    "CL-000964": ("SUPPORTED", "C-T22-T29→五闭包 G:ALL:8470721；与 ALL-Markdown 历史提交记录一致。"),
    "CL-000971": ("SUPPORTED", "W33/W34→双 JSON 审计（R018/R019）；与 WebGPT STATE 记录一致。"),
    "CL-000979": ("SUPPORTED", "全文加载政策（每轮重读闭包/三问/动态态、压缩后重载记录）；与三件套加载合同一致。"),
    "CL-000987": ("SUPPORTED", "B1 范围声明（历史 transform 状态）；与 B1 正文头部一致。"),
    "CL-001041": ("PENDING", "『十个 HoTT 研究问题』为 B1 内的提炼条目；需与 owner 行上下文合并后裁决。"),
    "CL-001097": ("SUPPORTED", "两种失败均禁止（CONSENSUS_FIRST/USER_ASSERTION_IS_PROOF）；与 T25 双阶段协议合同一致。"),
    "CL-001151": ("PENDING", "『已成立/条件成立/已否定/仍开放』四栏总账条目；需定位对应总账表后裁决。"),
    "CL-001207": ("SUPPORTED", "T37 对照表（215 行、八行裁决、四分类）与 B1 正文及 Schema v0.2 记录一致。"),
    "CL-001263": ("SUPPORTED", "B2 范围声明（历史 transform 状态）；与 B2 正文头部一致。"),
    "CL-001284": ("SUPPORTED", "R016 条目（W31 指令内嵌、Git+scripts 回收、G:WS:d726b2e 起点）；与 workspace git 记录一致。"),
    "CL-001307": ("PENDING", "『(4) 前缀因果性与实现成本的区分定理』为列表残句；需与 owner 行上下文合并后裁决。"),
    "CL-001329": ("SUPPORTED", "『以下为实物层新增』小节标记；与 B2 三栏对照结构一致。"),
    "CL-001350": ("SUPPORTED", "R011 条目（J→A 等价、负像零信息）与 WebGPT R011 记录一致。"),
    "CL-001679": ("SUPPORTED", "B4 范围声明与账本口径（24 ordinary text、17/17 code/result、21 thought）；与 gemini-*.jsonl 及 ledger-summary（24/17/17/2/21/36）一致。"),
    "CL-001687": ("PENDING", "B4 表格行（12/15 Lean4+求值器双轨验证宣称）；需与 Gemini 账本时间线逐条核对后裁决。"),
    "CL-001695": ("SUPPORTED", "IN-001~007 七封信的 chunk 编号与时间记录；与 B4 表格及 A6 逐封展开一致。"),
    "CL-001706": ("PENDING", "解释性综合（技术内核被 OUT-006 收窄为 ReachTrap/量词纪律）；需按源记录重述后裁决。"),
    "CL-001714": ("SUPPORTED", "『卡住≠不停机必须分离』与 OUT-001 三项撤回记录一致。"),
    "CL-001902": ("SUPPORTED", "路由：C0 是当前分母/证据边界 owner；与 C0 现状一致。"),
    "CL-001910": ("SUPPORTED", "历史验证器保留说明（旧 verify_ai_coverage.py 不替代新账本）；文件仍在 `理解章节/` 下。"),
    "CL-001919": ("SUPPORTED", "README 索引行（A2 覆盖芝诺/罗素/Better-Best/圆环/shenchensh与Matrix/说谎者）；与 A2 正文一致。"),
    "CL-001928": ("SUPPORTED", "README 索引行（A11 覆盖 W51×RP-B01 未连接、自指线、A 方向、38 口径教训）；与 A11 正文一致。"),
    "CL-001937": ("SUPPORTED", "机器审计资产位置声明；与顶层 audit/ 结构一致。"),
    "CL-001948": ("SUPPORTED", "上位指令原文引用（除 aistudio-docs 外对照对话录读尽并更新理解章节）；与 ruling/方案头部一致。"),
    "CL-001982": ("PENDING", "『唯一 F 级权威源，目前只有间接引用』为状态判断；需核对读态记录后裁决。"),
    "CL-002018": ("PENDING", "进度表残句（新增 6 项→B3§六、bedbd30 后批次 commit）；需定位对应表行后裁决。"),
    "CL-002054": ("PENDING", "『7,420 路径四级处置无“需读未读”』为覆盖性断言；需重放 disposition 账本后才可裁决。"),
    "CL-002089": ("SUPPORTED", "checkpoints 目录统计（699、结构核验+抽样字节、不逐个读）；与 .codex/cognition/checkpoints 现状与治理口径一致。"),
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
        "cumulative_sampled": 162 + sum(counts.values()),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FILLED", "summary": payload["review_summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
