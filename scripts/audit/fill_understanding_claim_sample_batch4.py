#!/usr/bin/env python3
"""Fill the current AI's per-claim review verdicts into the batch-4 sample file.

The sample itself is produced deterministically by
`scripts/audit/sample_understanding_claims_batch4.py`; this script only writes the
human review fields (`review_verdict`, `review_reason`) into that JSON so the
record stays contiguous and machine-readable. Verdict vocabulary matches batches
1-3: SUPPORTED / SUPERSEDED_BY_MACHINE_RESULT / UNSUPPORTED / PENDING.
"""
from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SAMPLE = "audit/understanding-claim-sample-batch4-20260912.json"

VERDICTS: dict[str, tuple[str, str]] = {
    "CL-000003": ("SUPPORTED", "直接引用用户原文（T15/W22 读法）；与核心认知 KC-000010 同向，引文与 owner 文本一致。"),
    "CL-000026": ("SUPPORTED", "用户原文（T24）引用；作为目标/期望登记，未被当作已证数学结论。"),
    "CL-000048": ("SUPPORTED", "KC-000010 逐字引用；与 C5 判断『经典悖论性结果尚缺』一致，引用准确。"),
    "CL-000071": ("PENDING", "解释性断言，尚未逐句裁决；机器支线只在固定片段触及该边界（partiality/商层/natural consumer），未裁决全句。"),
    "CL-000093": ("SUPPORTED", "三问任务的原文引用；三问文档与 A0 已存在，历史任务确有落地。"),
    "CL-000215": ("SUPPORTED", "路由元数据（本章处理轮次），与 response ledger 的 W/G 覆盖一致。"),
    "CL-000224": ("SUPPORTED", "用户原文（G5）引用；机器证明请求已由后续 F-011 包部分兑现，引用本身准确。"),
    "CL-000235": ("PENDING", "路线标签指向 RP-B02；该方向在历史记录中为支持方向，尚无机器裁决，留待句级复核。"),
    "CL-000244": ("PENDING", "交付格式说明（第五部分给首选动作+分支），属方法性表述，未句级裁决。"),
    "CL-000255": ("SUPPORTED", "方法路由（步骤 4 对证）与 A10 自身正文及 C3 判词体系一致，属路由/方法元数据。"),
    "CL-000324": ("SUPPORTED", "用户读法原则的转述（A2 首行原则），与 core 的 Thinking in my math philosophy 一致。"),
    "CL-000346": ("SUPPORTED", "引用片段，系账本切分产生的引文残片；与 owner 行原文相符，无独立数学主张。"),
    "CL-000369": ("SUPPORTED", "对参照悖论谱作用的描述，与 A2 正文自述一致。"),
    "CL-000393": ("SUPPORTED", "用户原文（GEMINI-M-007）引用：S 的构造无法完成（拿入/拿出自己），与 core KC-000016 一致。"),
    "CL-000416": ("SUPPORTED", "第二类问题表述（HoTT 何处以理论内逻辑关系超越时序），与 core KC-000024 的表述一致。"),
    "CL-000568": ("SUPPORTED", "路由元数据（本章处理轮次），与 response ledger 覆盖一致。"),
    "CL-000579": ("PENDING", "解释性综合（W44/W45、G20/G21 是原始怀疑的另一半），未句级裁决。"),
    "CL-000589": ("PENDING", "叙述性归纳（W8/W17 构成行动合同），属解释性表述，未句级裁决。"),
    "CL-000600": ("PENDING", "对 G20/G21 与用户关注点的推断（『证明是头号问题』），属解释性断言，未句级裁决。"),
    "CL-000610": ("PENDING", "『W51 与 RP-B01 精确互为表里』为解释性综合；C9 已把 W51-1/2 与 B01-M/E 映射到机器证据，B01-TARGET 仍 OPEN，故该句需按 C9 重述后再裁决。"),
    "CL-000717": ("SUPPORTED", "路由元数据（本章处理轮次），与 A8 正文自述一致。"),
    "CL-000750": ("SUPPORTED", "史料学第一律（原文至上，T18：摘要=偏见）的登记，与 A8 本章整合五律一致。"),
    "CL-000783": ("PENDING", "『无任何项目主张依赖它们』为范围性断言（未整读的材料），需按句级复核确认列举完整，未句级裁决。"),
    "CL-000816": ("PENDING", "`(R5)` 锚点指向历史材料条目，账本抽取后成为残句；需与 owner 行上下文合并后才能裁决。"),
    "CL-000849": ("SUPPORTED", "悖论集锦/MinerU SHA `62cef548…affe2` 与 `sources/SOURCE_MANIFEST.json` 登记一致；动态变更前快照保留可核。"),
    "CL-001374": ("SUPPORTED", "B3 范围声明（历史 transform 状态），与 B3 正文头部声明一致。"),
    "CL-001433": ("SUPPORTED", "R035 有限回答证据判据中的具体陈述；与 B3 第 63 行正文一致。"),
    "CL-001495": ("SUPPORTED", "R027 条目中的 Löb 前提区分登记；与 B3 第 75 行正文一致。"),
    "CL-001557": ("SUPPORTED", "『73 项旧测试 70 过 3 败』与 B3 第 87/152 行正文一致（如实保留失败）。"),
    "CL-001619": ("SUPPORTED", "R026『497 行/32,478 字节逐字节保全』与 B3 第 129 行正文一致；archive/STORE.json 含该 review 资产。"),
    "CL-002124": ("SUPPORTED", "文档头登记（2026-09-11 接手 AI（ZCode）），属身份/时间元数据。"),
    "CL-002133": ("SUPPORTED", "81 chunk=21+17+17+2+24 的分账与 `audit/gemini-thought-ledger.jsonl`（21）、`audit/gemini-execution-ledger.jsonl`（36）及 ledger-summary（24 ordinary text）一致。"),
    "CL-002143": ("SUPPORTED", "对上游 construction 内容的概括（语料/闭包/Schema/三问），与既有文档一致，属路由性描述。"),
    "CL-002154": ("SUPPORTED", "`R:W{节}` 锚点体系说明，与 WebGPT section ledger 111/55 节覆盖一致。"),
    "CL-002164": ("PENDING", "计划条款（写 B0-B5 并回源），属下次工作安排，未句级裁决；B0-B5 已存在，措辞可随后复核。"),
    "CL-002215": ("SUPPORTED", "路由：可见文本/分母/未认证边界以 C0 与顶层 audit 为准；与 C0 现状一致。"),
    "CL-002251": ("SUPPORTED", "读态路由（HoTT-2 其余 ~30 条回复保持 M），与 A8/读遍账本的读态登记一致。"),
    "CL-002287": ("PENDING", "`F 化`进度条目（RP-B01 三件、GEMINI-001 各件），需与当前读态逐项核对后裁决。"),
    "CL-002324": ("PENDING", "『回复总数 220 条 agentMessage』与 ledger-summary 的 `local_gpt_primary_lineage_assistant_responses=220` 一致，但该句范围断言（父线程+主文件均已随轮读尽）未句级裁决。"),
    "CL-002361": ("SUPPORTED", "`记录见 B1§七` 为交叉引用；B1 存在且含 §七，属路由性元数据。"),
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
        "cumulative_sampled": 122 + sum(counts.values()),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FILLED", "summary": payload["review_summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
