#!/usr/bin/env python3
"""Prepare the canonical checkpoint for core generation 13.

Generation 13 records the user's refinement that a correctly specified Russell
pattern P can guide an AI's learned knowledge of theory X toward a first-pass
candidate clue, without exhaustive theory traversal.  The script prepares only
the current-truth payload; it neither creates a research Goal nor makes a
mathematical claim.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SID = "S-GOV-20261002-CORE-GENERATION-13-ONEPASS-P"
PREVIOUS = "S-GOV-20261002-CORE-GEN12-ESSAY-ALIGNMENT"
BASE_REVISION = 297
NEXT_REVISION = 298
OLD_GENERATION = "core-cognition-generation-12"
NEW_GENERATION = "core-cognition-generation-13"
OLD_CORE_RECORD = "A-CODEX-CORE-GENERATION-12-001"
CORE_RECORD = "A-CODEX-CORE-GENERATION-13-001"
CORE = "核心认知.md"
MANIFEST = "核心认知.manifest.json"
CURATION = "scripts/audit/core-cognition-curation-v13.json"
TRANSITION = "audit/core-cognition-generation-13-transition-20261002.json"
SOURCE = "sources/prompts/Codex-模式P与一遍匹配-用户原文-20261002.md"
PREPARE = "audit/core-generation-13-onepass/prepare_checkpoint.py"
STATE = ".codex/research/hott/STATE.json"
DIRECTION = "方向追踪.md"
PANORAMA = "全景视野.md"
ESSAY = "扩展认知.md"
MEMORY = "MEMORY.md"
MEMORY_001 = "MEMORY/001 - 当前执行队列.md"
MEMORY_003 = "MEMORY/003 - 当前验证状态与顺序日志.md"
RESUME = ".codex/research/hott/RESUME.md"
RESULT = f".codex/cognition/checkpoints/{SID}/result.json"
SESSION = f".codex/research/hott/sessions/{SID}/SESSION.md"
AUDIT = f".codex/research/hott/sessions/{SID}/CORE_COGNITION_AUDIT.md"
RUNS = f".codex/research/hott/sessions/{SID}/RUNS.json"
CORE_TRANSITION = {"from_generation": OLD_GENERATION, "to_generation": NEW_GENERATION, "manifest": MANIFEST, "transition": TRANSITION}

def load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    if not spec or not spec.loader: raise SystemExit(f"LOAD_FAILED:{rel}")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module); return module

R = load("runtime_core13", ".codex/tools/cognition_runtime.py")
sys.path.insert(0, str(ROOT / "scripts/audit"))
import build_core_cognition as core_builder  # noqa: E402
import projection_edit  # noqa: E402

def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def sha_file(rel: str) -> str: return sha((ROOT / rel).read_bytes())
def dump(value: object) -> str: return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
def once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1: raise ValueError(f"REPLACE_COUNT:{old[:80]}:{count}")
    return text.replace(old, new, 1)
def quote(payload: str, kid: str) -> str:
    body = "\n".join("> " + line if line else ">" for line in payload.splitlines())
    return f"<!-- original:{kid}:begin -->\n{body}\n<!-- original:{kid}:end -->"

def refresh_projection(doc: dict, old_version: str, new_version: str, suffix: str) -> None:
    projection_edit.replace_in_index(doc, old_version, new_version)
    projection_edit.replace_in_index(doc, "日期：2026-10-02", "日期：2026-10-02")
    projection_edit.replace_in_index(doc, "source_state_revision: 297", "source_state_revision: 298")
    match = re.search(r"projection_generation: ([^\n]+)", doc["index_text"])
    if not match: raise ValueError("PROJECTION_GENERATION_MISSING")
    projection_edit.replace_in_index(doc, match.group(0), f"projection_generation: {suffix}-298")

def legacy_audit(manifest: dict) -> str:
    lines = [
        f"# 核心认知逐编号回评：{SID}", "",
        f"> generation：`{NEW_GENERATION}`；KC 总数：62。当前 runtime 对 session audit child 文件的原子写入仍有限制，本轮使用完整单文件 KC 审计并公开该边界。", "",
        "- core_change: YES_ADDITIVE_PRESERVING — generation-12/61 → generation-13/62；61/61 旧 KC 由 transition 映射，新增 KC-000062。",
        "- direction_change: METADATA_ONLY — 只刷新 revision/projection generation；不启动新理论研究。",
        "- panorama_change: METADATA_ONLY — 不新增或升级数学结果、候选命中或现实结论。",
        "- essay_change: YES — 第012片增加‘模式 P 的一遍匹配’解释，基线更新为 generation-13/62。",
        "- update_decision: P 被记录为条件性启发式模式，首轮输出只具有线索身份；不读取权重，不替代后续核验。",
        "- cross_conflicts: 把一遍匹配说成全理论穷尽、性能保证、数学证明或已发现缺陷均与本条原意冲突。",
        "- unresolved: P 的正确规格、实际行为效果、理论 X 的第一线索及所有候选的来源/控制/证明义务仍开放。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决与反证条件 |",
        "|---|---|---|---|---|---|",
    ]
    focus = {
        "KC-000007": ("DEEPENED", "已有知识的模式匹配现在被进一步指定为 P 引导的发现态动作。"),
        "KC-000040": ("DEEPENED", "知识谱作为被考察对象的路径得到 P 一遍匹配的条件性工作说明。"),
        "KC-000058": ("ALIGNED", "启发式不读取权重、不等于证据的边界保持。"),
        "KC-000059": ("DEEPENED", "P 的发现功能被用户明确为依靠理论 X 已有知识匹配线索。"),
        "KC-000060": ("ALIGNED", "一遍匹配仍须从显眼核心承诺开始，不能恢复无边界搜索。"),
        "KC-000061": ("DEEPENED", "新的一遍匹配指导也进入持续加载的工作意识。"),
        "KC-000062": ("ALIGNED", "本条完整原话记录 P 写对时一遍匹配理论 X 线索的条件性预期。"),
    }
    for unit in manifest["units"]:
        kid = str(unit["id"]); label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = focus.get(kid, ("NOT_TOUCHED", "本轮未重新裁决该 KC 的数学、现实或哲学内容。"))
        evidence = f"`核心认知.md` {kid}；generation-13 manifest/transition。"
        next_step = "后续直接使用本条或有新用户原文、来源或反例时再回源重审。"
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | {evidence} | {next_step} |")
    lines.extend([
        "", "## 四件套交叉审视", "",
        "- 最高指示角色复核：本轮为 GOVERNANCE_ALIGNMENT；要保护的发现动作是让 P 引导模型知识走向理论 X 的明显承诺和可检验线索，而不让它变成无界遍历或预告胜利。",
        "- 扩展认知：第012片新增的解释明确区分‘正确 P + 可用理论知识 + 首轮线索’与数学结论、性能保证、权重读取和全理论覆盖。",
        "- 方向与全景：仅刷新 STATE revision metadata；ZFC、HoTT、Power Set 与其他候选仍维持原有证据等级。",
        "- 反证条件：若一个声称的一遍匹配无法指出 P 的具体环节、理论 X 的核心承诺、同一任务与后续控制，它不满足本轮方法论。", "",
    ])
    return "\n".join(lines) + "\n"

def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", type=Path, required=True); args = ap.parse_args()
    if args.output.exists(): raise SystemExit("OUTPUT_EXISTS")
    state = json.loads((ROOT / STATE).read_text())
    if state.get("revision") != BASE_REVISION or state.get("latest_session") != PREVIOUS: raise SystemExit("STATE_BASE_MISMATCH")
    if state.get("current_core", {}).get("generation") != OLD_GENERATION: raise SystemExit("CORE_BASE_MISMATCH")
    if SID in state["records"] or CORE_RECORD in state["records"]: raise SystemExit("RECORD_EXISTS")
    if not all((ROOT / rel).is_file() for rel in (CORE, MANIFEST, CURATION, TRANSITION, SOURCE)): raise SystemExit("GENERATION_INPUT_MISSING")
    manifest = json.loads((ROOT / MANIFEST).read_text())
    if manifest.get("generation") != NEW_GENERATION or manifest.get("counts", {}).get("core_units") != 62: raise SystemExit("GENERATION_NOT_BUILT")
    payloads = core_builder.parse_core_payloads((ROOT / CORE).read_text())
    if payloads.get("KC-000062") is None: raise SystemExit("KC62_MISSING")
    plan = R.plan(ROOT, profile="governance", _allow_core_transition=CORE_TRANSITION)

    direction = projection_edit.load(ROOT, DIRECTION); refresh_projection(direction, "版本：`integrated-direction-portfolio/v1.18`", "版本：`integrated-direction-portfolio/v1.19`", "20261002-direction-onepass")
    panorama = projection_edit.load(ROOT, PANORAMA); refresh_projection(panorama, "版本：`integrated-outcome-panorama/v1.19`", "版本：`integrated-outcome-panorama/v1.20`", "20261002-outcome-onepass")
    essay = projection_edit.load(ROOT, ESSAY)
    essay["index_text"] = once(essay["index_text"], "baseline: core-cognition-generation-12", "baseline: core-cognition-generation-13")
    essay["index_text"] = once(essay["index_text"], "本文根据《核心认知.md》generation-12 的全部 61 段原文持续综合；第 012 片专门展开本轮新增的六条方法论原文。", "本文根据《核心认知.md》generation-13 的全部 62 段原文持续综合；第 012 片展开 2026-10-02 的七条后续理论方法论原文。")
    essay["index_text"] = once(essay["index_text"], "明显核心承诺与持续加载（KC-000056–KC-000061）", "明显核心承诺、持续加载与模式 P 一遍匹配（KC-000056–KC-000062）")
    e012 = "扩展认知/012 - 后续理论靶、罗素模式 P 与工作意识.md"
    essay["shards"][e012] = essay["shards"][e012].rstrip() + f'''\n\n## 模式 P 是把已有理论知识转成首轮线索的方式

{quote(payloads["KC-000062"], "KC-000062")}

[原文出处](../{SOURCE}#L9)

这段新原文补上了 P 的发现功能。它不是要求模型逐条枚举理论 X 的全部定义、定理、库实现和衍生分支；它要求先把 P 写成能抓住理论 X 核心承诺的模式，再以模型已学习的理论 X 知识进行匹配，给出首轮可审线索。这里的“一遍”说的是发现态的首轮匹配，不是完成对理论 X 的穷尽审计，也不是绕过原典、标准回答、反控制或机器证明。

条件不能丢失：P 必须写对；理论 X 的相关知识必须在当前模型可用；产物必须只是线索并能被后续检查。若输出只复述熟悉结论、无法定位核心承诺、无法构造同一任务，或者在来源控制下失败，就不能把它称为 P 的成功匹配。模型也不能把“神经网络中的知识”说成可直接读取或拿来作证的权重与训练样本。
'''
    e005 = "扩展认知/005 - 表达界限、文章作为起点与编写说明.md"
    essay["shards"][e005] = once(essay["shards"][e005], "当前基线：core-cognition-generation-12，61 个语义单元；第 012 片覆盖本轮新增 KC-000056–KC-000061。", "当前基线：core-cognition-generation-13，62 个语义单元；第 012 片覆盖本轮新增 KC-000056–KC-000062。")

    memory = projection_edit.load(ROOT, MEMORY)
    add = """## 模式 P 的一遍匹配方法（2026-10-02）

研究发起人补充：模式 P 是在核心认知和相关理念引导下，让 AI 使用其关于理论 X 的已有知识进行首轮模式匹配的启发式；若 P 写对，目标是无需遍历理论及其衍生细节就找出可检验线索。该条件性方法不等于性能保证、权重读取、穷尽搜索、数学证明或候选命中。它必须继续落到理论 X 的明显承诺、P 的具体环节、同一任务、原典和正反控制上。generation-13 的 KC-000062 保存原话。

"""
    memory["shards"][MEMORY_001] = once(memory["shards"][MEMORY_001], "## 用户当前专题（2026-09-24）", add + "## 用户当前专题（2026-09-24）")
    memory["shards"][MEMORY_003] = memory["shards"][MEMORY_003].rstrip() + f"\n\n{SID}：core generation-13/62 新增 KC-000062。用户将模式 P 明确为引导 AI 以理论 X 已有知识进行一遍匹配线索的条件性启发式；不等于遍历豁免、性能证明、权重读取、理论缺陷或新 Goal。61/61 旧 KC 映射，revision 297→298。\n"
    resume = (ROOT / RESUME).read_text()
    resume = once(resume, "## 历史停止点\n\n", "## 历史停止点\n\n" + f"{SID}：core generation-13/62 增加模式 P 的一遍匹配方法论。它指导发现态，不改变 Goal7、现有候选或数学状态。\n\n")

    state["revision"] = NEXT_REVISION; state["latest_session"] = SID
    state["current_core"] = {"core_sha256": sha_file(CORE), "curation": CURATION, "curation_sha256": sha_file(CURATION), "generation": NEW_GENERATION, "kc_count": 62, "manifest": MANIFEST, "manifest_sha256": sha_file(MANIFEST), "path": CORE, "transition": TRANSITION}
    state["execution_control"]["last_checkpoint_session"] = SID; state["execution_control"]["checkpoint_result"] = RESULT
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20261002-direction-onepass-298"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20261002-outcome-onepass-298"
    old = state["records"][OLD_CORE_RECORD]
    old["lifecycle_status"] = "HISTORICAL"; old["status"] = "superseded_by_generation_13"
    old["resolution"] = {"evidence": [TRANSITION, CORE, MANIFEST], "reason": "Generation-13 preserves all generation-12 units and advances STATE.current_core to the new curation, manifest and transition."}
    old["revalidation"] = (str(old.get("revalidation", "")).strip() + f" {SID}: superseded as current core by generation-13; all generation-12 payloads remain mapped in the new transition.").strip()
    core_sources = [CORE, MANIFEST, CURATION, TRANSITION, SOURCE, "scripts/audit/build_core_cognition.py", "scripts/audit/verify_core_cognition.py", PREPARE]
    state["records"][CORE_RECORD] = {"depends_on": [], "evidence_status": "VERIFIED_WITH_SCOPE / COMPLETE_ADDITIVE_PRESERVING", "full_sources": core_sources, "kind": "core_generation_migration", "lifecycle_status": "CURRENT", "path": TRANSITION, "related_records": [OLD_CORE_RECORD, SID], "scope": "Preserve all 61 generation-12 direct-user units exactly and append KC-000062: a correctly written pattern P is a conditional heuristic for matching the model's learned theory-X knowledge into a first-pass clue without exhaustive traversal. No performance theorem, neural-weight inspection, mathematical theorem, defect verdict, or Goal is added.", "source_hashes": {rel: sha_file(rel) for rel in core_sources}, "status": "closed"}
    state["records"][SID] = {"depends_on": [], "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM", "full_sources": [SESSION, AUDIT, RUNS, RESULT, SOURCE, CURATION, TRANSITION, PREPARE, CORE_RECORD, OLD_CORE_RECORD], "kind": "session", "lifecycle_status": "HISTORICAL", "path": SESSION, "related_records": [PREVIOUS, CORE_RECORD, OLD_CORE_RECORD], "scope": "Apply generation-13's direct-user refinement of P as a conditional one-pass pattern-matching heuristic. No mathematical result, candidate promotion, research Goal, or existing-status change.", "source_hashes": {}, "status": "complete"}
    session = f"""# {SID}

- tier: T3 core-generation and current-state update; no mathematical conclusion.
- role: GOVERNANCE_ALIGNMENT.
- authorization: the user explicitly asked that this refinement of pattern P be recorded.
- core: generation-12/61 → generation-13/62; all 61 prior units are mapped through the generation-13 transition.
- protected meaning: a correctly written P may guide learned knowledge of theory X to a first-pass clue without exhaustive traversal; it does not guarantee success, prove a theory defect, or make neural weights inspectable evidence.
- unchanged: Goal7, current HoTT findings, ZFC evidence status, candidate rankings and mathematical proof records.
"""
    runs = {"schema_version": "hott-session-runs/v2", "session_id": SID, "session_kind": "GOVERNANCE_CORE_GENERATION_PATTERN_P_ONEPASS", "checkpoint_result": RESULT, "base_snapshot": plan["snapshot"], "formal_runs": [], "governance_runs": [{"tool": "build_core_cognition.py", "status": "generation-13 build and transition required"}, {"tool": "verify_core_cognition.py", "status": "source/core/transition verifier required"}, {"tool": "cognition_runtime.py", "status": "CHECKPOINT_COMMITTED is the sole application receipt"}], "new_math_claims": [], "open": ["P specification quality", "future behavior test", "all theory-X candidates"]}
    texts = {rel: (ROOT / rel).read_text() for rel in R.MUTABLE}
    for doc in (direction, panorama, essay, memory): texts[doc["index_path"]] = doc["index_text"]; texts.update(doc["shards"])
    texts[RESUME] = resume; texts[STATE] = dump(state); texts[SESSION] = session; texts[AUDIT] = legacy_audit(manifest); texts[RUNS] = dump(runs)
    payload = {"schema_version": "cognition-checkpoint/v1", "session_id": SID, "authorization": "The user explicitly instructed that the new statement about pattern P as a conditional one-pass heuristic be recorded. This checkpoint performs the required core, exposition, recovery, audit and state update without starting a Goal, pushing, or asserting a mathematical conclusion.", "load_profile": "governance", "task_ids": [], "core_transition": CORE_TRANSITION, "files": [{"path": rel, "expected_sha256": sha((ROOT / rel).read_bytes()) if (ROOT / rel).is_file() else None, "text": text} for rel, text in texts.items()]}
    R.prepare(ROOT, plan["snapshot"], payload)
    args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(dump(payload)); print(json.dumps({"status": "PREPARED", "session_id": SID, "snapshot": plan["snapshot"], "revision": NEXT_REVISION, "files": len(texts), "core_units": 62}, ensure_ascii=False))

if __name__ == "__main__": main()
