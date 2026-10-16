#!/usr/bin/env python3
"""Prepare/apply a canonical checkpoint for the user-authorized tracking recovery.

All unchanged mutable documents are carried byte-for-byte. The recovery receipt
is a new event, never a replacement for a historical transaction.
"""
import argparse
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent / "tracking-recovery"
SID = "S-GOV-20260919-ASTRA-LOAD-REPAIR"
BASE = ".codex/research/hott/sessions/" + SID + "/"
spec = importlib.util.spec_from_file_location("cognition", ROOT / ".codex/tools/cognition_runtime.py")
R = importlib.util.module_from_spec(spec)
spec.loader.exec_module(R)

SESSION = """# S-GOV-20260919-ASTRA-LOAD-REPAIR

- host: Codex desktop local session
- model: GPT-6-based Codex; exact serving model is not independently certified
- tier: T3 mutation (state checkpoint, no mathematical conclusion)
- role: CANONICAL_INTEGRATOR_FOR_USER_AUTHORIZED_LOAD_REPAIR
- authorization: 用户明确选择“先修复全项目加载与检查点，再执行”；原任务仍为执行 Astra 断点与证明机制检查。
- load_receipt: audit/astra-breakpoint-20260919/tracking-recovery/LOAD-RECEIPT.json
- baseline: Git 40b1ca78fe0e391201848923e09423808a2178ee; STATE revision 171
- scope: 恢复已提交 MEMORY/001 与 HEAD.tracked 的登记一致，校准两个投影索引的状态版本元数据，并保存新的 canonical checkpoint；不改证明、四件套正文、用户原文或既有研究队列。

## 直接证据与边界

research plan 原报 UNCOMMITTED_STATE，但 MEMORY/001 在 Git 中 clean。完整受管哈希对账只发现该文件一项差异。
commit 49d5286827e5cb9424025e421af3960abbec9192 只为此文件追加第27项公开包计划；其父版本哈希恰等于旧登记，提交版本哈希恰等于当前文件。
repair_tracking.py 在 exact HEAD、干净目标、无锁/事务及唯一差异前提下更正派生 HEAD，保存 before/after/diff/REPAIR.json；STATE 未在该步骤改写。
本 checkpoint 才通过原 runtime 写入 revision 172 和当前 session；以工具 result.json 为唯一应用收据。
三方校验另报 DIRECTION_STATE_REVISION_STALE：两个投影索引仍登记169而治理STATE已到171。本事务仅同步版本元数据，不冒充数学正文已按新审计重写。

全文恢复覆盖四件套25个物理文件、STATE 11990行以及 research profile 其余26文件。大输出曾被截断，随后以小块补读至EOF；不得把最初截断调用算为完整读取。
STATE 的历史 record、旧 source hashes 与最新机器源码并不总一致；它们是导航与历史证据，数学验收仍须直接核当前 source/run/index。
旧前沿中的“Ω收费钉死”不是本轮接受的数学结论；本轮不处理该争议，不恢复旧 Goal 或关闭数学开放项。

## element_usage

| 元件 | 使用与作用 |
|---|---|
| Git/file baseline | used：区分已提交更新与并行未提交修改 |
| full-set + STATE | used：保持当前任务、历史与证据等级分离 |
| runtime plan/read/check | used：重新验证52文件加载及字节闭包 |
| bounded recovery | used：只接受已核定的一条哈希差异 |
| canonical checkpoint | used：真实 before/after/transaction/result |
| 数学核 | not used：治理恢复不伪称数学实验 |
| Sub Agent | not used：遵守项目禁止 |

## 返回父任务

恢复验证通过即返回 Astra 的 BP-U00/U01，随后执行六机制横向检查。该恢复不是研究完成，也不证明 HoTT 的正确或错误。
Git 未提交、不push、不tag。当前修复为 LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED。
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    plan = R.plan(ROOT, profile="research")
    assert plan["revision"] == 171
    chunks = []
    for d in plan["documents"]:
        start = 1
        while start is not None:
            c = R.read_chunk(ROOT, plan["snapshot"], d["path"], start, 200000, profile="research")
            chunks.append(c)
            start = c["next_start_line"]
    coverage = R.check_coverage(plan, chunks)
    receipt = {"schema": "astra-load-verification/v1", "snapshot": plan["snapshot"],
               "coverage": coverage, "documents": plan["documents"],
               "body_read_method": "model-visible bounded filesystem outputs; independently checked by canonical read_chunk/check_coverage",
               "state_full_read_complete": True, "model_understanding": "NOT_CERTIFIED_BY_TOOL"}
    (OUT / "LOAD-RECEIPT.json").write_bytes(R.dump(receipt))
    state = json.loads((ROOT / R.STATE).read_bytes())
    old_session = state["latest_session"]
    state["revision"] += 1
    state["latest_session"] = SID
    state["records"][SID] = {
        "kind": "session", "path": BASE + "SESSION.md", "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM", "status": "complete",
        "depends_on": [], "related_records": [old_session],
        "full_sources": [BASE + "SESSION.md", BASE + "RUNS.json", BASE + "CORE_COGNITION_AUDIT.md", "audit/astra-breakpoint-20260919/tracking-recovery/REPAIR.json"],
        "scope": "User-authorized exact one-file tracking recovery and new canonical checkpoint; no historical receipt or mathematical source rewritten."
    }
    audit = "# " + SID + " · 核心认知回评\n\n"
    audit += "core-cognition-generation-7；46条；本单元仅修复加载登记。按 PROTOCOL §5 的 writer 兼容例外使用 legacy 表，登记 G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001；未声称分片已原子写入。\n\n"
    audit += "- core_change: NO\n- direction_change: METADATA_ONLY\n- panorama_change: METADATA_ONLY\n- essay_change: NO\n- update_decision: 修复受管登记及投影版本元数据并留真实新事务，完成后返回原任务。\n- cross_conflicts: source_state_revision169与STATE171的机械漂移本次同步；不凭版本同步提升旧数学叙述。MEMORY哈希漂移有exact Git原因。\n- unresolved: 新数学检查尚未开始；旧研究问题不在本修复中关闭。\n\n"
    audit += "| KC | 主题 | relation | 工作姿态、实际动作与理由 | 证据、下次触及与反证条件 |\n|---|---|---|---|---|\n"
    headings = re.findall(r"^### (KC-\d+) · .*? · .*? · (.+)$", (ROOT / "核心认知.md").read_text(), re.M)
    assert len(headings) == 46
    for kc, title in headings:
        audit += f"| `{kc}` | {title} | NOT_TOUCHED | 本单元不作该数学主张的证明或裁决；只恢复可信读取入口，保留其原意与待检身份。 | REPAIR.json、LOAD-RECEIPT.json；返回该主题的实际构造时重新评价；若本次变更改变了其原文、证明或研究优先级，应撤回NOT_TOUCHED判定并复审。 |\n"
    audit += "\n## 扩展认知回评\n\n八片均已重读；1的问题生成姿态、5的形式化不换题及7的路径依赖提醒用于限定本修复，不作数学检验。2、3、4、6、8的具体数学/现实内容均NOT_TOUCHED；相应构造执行时再评。所有展开仍为AI阐释而非用户原文权威。\n\n## 已走过的路与下一选择\n\n只修正一个可由Git完整解释的登记差异；未为通过加载器批量重绑数学source pins。返回用户指定的Astra方案；若plan再次失配，先保存新差异，禁止覆盖其他写者。系统化搜索cells本单元NOT_APPLICABLE，后继数学单元必须另列真实覆盖。\n"
    runs = {"schema_version": "hott-session-runs/v1", "session_id": SID,
            "repair_receipt": "audit/astra-breakpoint-20260919/tracking-recovery/REPAIR.json",
            "load_receipt": "audit/astra-breakpoint-20260919/tracking-recovery/LOAD-RECEIPT.json",
            "mathematical_runs": [], "historical_receipts_rewritten": False}
    files = []
    for record, kind in [("I-DIRECTION-PORTFOLIO-20260912", "direction"), ("I-OUTCOME-PANORAMA-20260912", "outcome")]:
        state["records"][record]["projection_generation"] = "20260919-" + kind + "-172"
    paths = list(R.MUTABLE) + list(R.mutable_shard_paths(ROOT))
    for rel in paths:
        b = (ROOT / rel).read_bytes()
        body = R.dump(state).decode() if rel == R.STATE else b.decode()
        if rel in (R.DIRECTION, R.PANORAMA):
            body, count = re.subn(r"(?m)^source_state_revision: 169$", "source_state_revision: 172", body)
            assert count == 1
            kind = "direction" if rel == R.DIRECTION else "outcome"
            body, count = re.subn(r"(?m)^projection_generation: .+$", "projection_generation: 20260919-" + kind + "-172", body)
            assert count == 1
        files.append({"path": rel, "expected_sha256": R.sha(b), "text": body})
    for name, body in [("SESSION.md", SESSION), ("RUNS.json", R.dump(runs).decode()), ("CORE_COGNITION_AUDIT.md", audit)]:
        files.append({"path": BASE + name, "expected_sha256": None, "text": body})
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID,
               "load_profile": "research", "task_ids": [], "authorization": "用户明确选择：先修复全项目加载与检查点，再执行", "files": files}
    (OUT / "checkpoint-payload.json").write_bytes(R.dump(payload))
    result = R.checkpoint(ROOT, plan["snapshot"], payload, apply=a.apply)
    (OUT / ("checkpoint-apply-output.json" if a.apply else "checkpoint-dry-run.json")).write_bytes(R.dump(result))
    print(json.dumps({k:v for k,v in result.items() if k != "paths"}, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
