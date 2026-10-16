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
SAMPLE = "audit/understanding-claim-sample-batch6-20260912.json"

VERDICTS: dict[str, tuple[str, str]] = {
    "CL-000116": ("SUPPORTED", "A1 章组织声明（按论证结构组织轮次、时间序为辅）；与 A1 正文结构一致。"),
    "CL-000135": ("PENDING", "解释性裁定（可证的是条件版失配定理、校准使谱表述更重要）；属论证判断，未句级裁决。"),
    "CL-000155": ("SUPPORTED", "被替换前提=对现实的否定（现实是量子化、离散的）；与 KC-000015/000019 一致。"),
    "CL-000175": ("SUPPORTED", "用户要求『完整地、认真地记录到认知闭包』的转述；与 T18 记录口径一致。"),
    "CL-000196": ("SUPPORTED", "KC-000018 逐字引用（深切怀疑 HoTT 也这样做、认知惯性/路径依赖）；与 core 一致。"),
    "CL-000686": ("SUPPORTED", "A7 路由元数据（C-T10/C-T27/G7/G12§八）；与 response ledger 覆盖一致。"),
    "CL-000691": ("SUPPORTED", "KC-000017 训练数据双重身份（有益/有害、不许当裁判）；与 core 一致。"),
    "CL-000698": ("PENDING", "解释性断言（同一指令逐字重申、学风是普适合同）；属综合判断，未句级裁决。"),
    "CL-000704": ("SUPPORTED", "用户原文引用（允许质疑工具与自己的研究方法）；与 T27 记录一致。"),
    "CL-000710": ("SUPPORTED", "护栏条目（训练 prior=历史参考非裁判）；与 KC-000017 一致。"),
    "CL-000718": ("SUPPORTED", "KC 含用户原话（proofs/dev-docs 是其他 AI 整理物）；与 sources 提取一致。"),
    "CL-000751": ("SUPPORTED", "史料学第二律（保全先于利用，T1：归集→审计→超越）；与 A8 五律一致。"),
    "CL-000784": ("PENDING", "覆盖性断言（原文副本件已覆盖、F 级）；需重放覆盖核对后才可裁决。"),
    "CL-000817": ("PENDING", "残句（『充分理解』=纤维因子分解规范形（R6））；需与 owner 行上下文合并后裁决。"),
    "CL-000850": ("SUPPORTED", "GONE 判决书资产条目；三罪证与芝诺『放映机』类比在来源原件中可回源。"),
    "CL-000988": ("PENDING", "分母声明（38-turn/220 visible assistant/1143 主线 tool-pair）；220/38 与账本一致，1143 需另核。"),
    "CL-001042": ("PENDING", "问题残句（Gate 在对象层还是元层？）；需与 owner 上下文合并后裁决。"),
    "CL-001098": ("SUPPORTED", "T26 Z 铁律五层表述与『朴素集合论的失败…』的判断；与 T25/T26 记录一致。"),
    "CL-001152": ("PENDING", "漂移诊断出处判断（早于三阶段史索引 10 天）；属叙述判断，未句级裁决。"),
    "CL-001208": ("PENDING", "解释性综合（己方胜在书式核心规则、固定版本保全、时间研究方向）；属判断，未句级裁决。"),
    "CL-001375": ("SUPPORTED", "B3 边界声明（映射仍需 ledger 到 artifact/Git 复核，不能以旧『全部完成』代替 C0）；与 C0 一致。"),
    "CL-001434": ("SUPPORTED", "R035 正例条目（像类型+答案图 isProp(Answer(s)) 恢复布尔）；与 B3 正文一致。"),
    "CL-001496": ("SUPPORTED", "4,330 有限模型与 `workspace/artifacts/r027/FINITE_MODEL_RESULTS.json`（labelled_models=4330）一致；7 份 Lean 文件 NOT_RUN 亦与记录一致。"),
    "CL-001558": ("SUPPORTED", "R040 交接结论引文；与 B3/R040 记录一致。"),
    "CL-001620": ("PENDING", "R026 细节（V0 执行后加强类型检查、V0/V1 双收据）；需核对 reviews 目录收据后裁决。"),
    "CL-001724": ("SUPPORTED", "B5 路由声明（当前拥有/证据层/未知由 C0 与 audit ledger 复核）；与 C0 一致。"),
    "CL-001742": ("PENDING", "成果总账行（Acc 迁移：当前态路径提升支持 Acc 终止证据迁移）；该行与 R038-A/B 的 paper 状态需复核。"),
    "CL-001761": ("SUPPORTED", "archive 盘点条目（324 原件 748MB 可重建）；与 archive/STORE.json 及 verify_ai_coverage 核对一致。"),
    "CL-001781": ("SUPPORTED", "test_r034：24 tests、24 ran OK；与 `workspace/artifacts/r034` 与 B5 总账一致。"),
    "CL-001800": ("SUPPORTED", "§一 各行获得 SESSION+PROOF_NOTE 双重背书；对应 reviews/ 目录文件存在。"),
    "CL-001949": ("SUPPORTED", "方案执行凭据声明（每批完成在 §六 打勾并 commit）；与方案头部一致。"),
    "CL-001983": ("SUPPORTED", "批次更新章节清单（A1/A2/A3/A4 注记、B1）；与方案条款一致。"),
    "CL-002019": ("SUPPORTED", "批次 2 状态（r024 全文精读+305 测试隔离重执行全过、4 审计脚本重跑、计数吻合→B5 升级 E2+）；与 B5 总账合计 305 PASS 一致。"),
    "CL-002055": ("PENDING", "批次进度残句（verify 29→36 项全 PASS、A8 批次 10 节、c96599a）；需定位对应表行后裁决。"),
    "CL-002090": ("SUPPORTED", "checkpoints 盘点条目（artifacts/ 766、汇总级 JSON 全读+抽样核对）；与治理口径一致。"),
    "CL-002216": ("SUPPORTED", "读遍账本声明（F/D/S/M 是当时 AI 的阅读状态，不是本 repo 模型理解证明）；与 README/C0 边界一致。"),
    "CL-002252": ("SUPPORTED", "读态路由（R006-R019 各 SESSION.md 治理层已 F）；与 workspace reviews 目录一致。"),
    "CL-002288": ("PENDING", "抽核对性断言（IN-002~007 与 TO_GEMINI 抽样一致）；需重放样本后裁决。"),
    "CL-002325": ("PENDING", "三栏对零矛盾的结论；属核证性判断，未句级裁决。"),
    "CL-002362": ("SUPPORTED", "读遍账本行（用户侧 119 条发言+句级账本 F）；与 S061 口径对照的 119 数字一致。"),
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
        "cumulative_sampled": 202 + sum(counts.values()),
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "FILLED", "summary": payload["review_summary"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
