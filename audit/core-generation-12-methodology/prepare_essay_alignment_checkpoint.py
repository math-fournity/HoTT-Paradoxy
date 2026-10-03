#!/usr/bin/env python3
"""Prepare a narrow checkpoint correcting generation-12 essay routing text."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SID = "S-GOV-20261002-CORE-GEN12-ESSAY-ALIGNMENT"
PREVIOUS = "S-GOV-20261002-CORE-GENERATION-12-METHODOLOGY"
STATE = ".codex/research/hott/STATE.json"
ESSAY = "扩展认知.md"
DIRECTION = "方向追踪.md"
PANORAMA = "全景视野.md"
MEMORY = "MEMORY.md"
MEMORY_003 = "MEMORY/003 - 当前验证状态与顺序日志.md"
RESUME = ".codex/research/hott/RESUME.md"
SESSION = f".codex/research/hott/sessions/{SID}/SESSION.md"
AUDIT = f".codex/research/hott/sessions/{SID}/CORE_COGNITION_AUDIT.md"
RUNS = f".codex/research/hott/sessions/{SID}/RUNS.json"
RESULT = f".codex/cognition/checkpoints/{SID}/result.json"

def load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    if not spec or not spec.loader: raise SystemExit(f"LOAD_FAILED:{rel}")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

R = load("runtime_essay_alignment", ".codex/tools/cognition_runtime.py")
sys.path.insert(0, str(ROOT / "scripts/audit"))
import projection_edit  # noqa:E402

def sha(data: bytes) -> str: return hashlib.sha256(data).hexdigest()
def dump(value: object) -> str: return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
def once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1: raise ValueError(f"REPLACE_COUNT:{old[:72]}:{text.count(old)}")
    return text.replace(old, new, 1)

def audit_text(manifest: dict) -> str:
    lines = [
        f"# 核心认知逐编号回评：{SID}", "",
        "> generation：`core-cognition-generation-12`；KC 总数：61。此轮只校正第四件索引的分片计数与历史基线措辞；不修改 core 原文、curation、transition 或数学结论。", "",
        "- core_change: NO — generation-12/61 的 core、manifest、source和transition字节不变。",
        "- direction_change: METADATA_ONLY — source_state_revision/projection_generation 随 revision 297 对齐。",
        "- panorama_change: METADATA_ONLY — source_state_revision/projection_generation 随 revision 297 对齐。",
        "- essay_change: YES — 首屏‘11个分片’更正为12，编写说明明确历史初稿基线与当前generation-12基线。",
        "- update_decision: 修复读者路由准确性；不新增用户原文、候选、Goal或数学结果。",
        "- cross_conflicts: 表格已有012而首屏仍报11，且旧编写说明单称generation-5，均会误导未来加载者。",
        "- unresolved: 文件路由不认证未来语义使用；所有理论候选与模式P研究仍开放。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决与反证条件 |",
        "|---|---|---|---|---|---|",
    ]
    for u in manifest["units"]:
        kid = u["id"]; label = str(u["semantic_label"]).replace("|", "\\|")
        lines.append(f"| `{kid}` | {label} | `NOT_TOUCHED` | 本轮未改该 KC 原文或其研究含义。 | `核心认知.md` {kid}；generation-12 manifest。 | 若后续工作直接触及本 KC，再按原文重审。 |")
    return "\n".join(lines) + "\n"

def refresh_projection(doc: dict, version_old: str, version_new: str, suffix: str) -> None:
    projection_edit.replace_in_index(doc, version_old, version_new)
    projection_edit.replace_in_index(doc, "source_state_revision: 296", "source_state_revision: 297")
    match = re.search(r"projection_generation: ([^\n]+)", doc["index_text"])
    if not match: raise ValueError("PROJECTION_GENERATION_MISSING")
    projection_edit.replace_in_index(doc, match.group(0), f"projection_generation: {suffix}-297")

def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--output", type=Path, required=True); args = ap.parse_args()
    if args.output.exists(): raise SystemExit("OUTPUT_EXISTS")
    state = json.loads((ROOT / STATE).read_text())
    if state["revision"] != 296 or state["latest_session"] != PREVIOUS: raise SystemExit("STATE_BASE_MISMATCH")
    if SID in state["records"]: raise SystemExit("SESSION_EXISTS")
    plan = R.plan(ROOT, profile="governance")
    essay = projection_edit.load(ROOT, ESSAY)
    essay["index_text"] = once(essay["index_text"], "下方 11 个分片", "下方 12 个分片")
    old = "原文基线：core-cognition-generation-5，40 个语义单元；《核心认知.md》SHA-256：c8554d3180a87b497eb30813d3d7e61636d2f713c65a3f26fc209e172310da57。"
    new = "初稿历史基线：core-cognition-generation-5，40 个语义单元；该历史字节身份保留。当前基线：core-cognition-generation-12，61 个语义单元；第 012 片覆盖本轮新增 KC-000056–KC-000061。"
    e005 = "扩展认知/005 - 表达界限、文章作为起点与编写说明.md"
    essay["shards"][e005] = once(essay["shards"][e005], old, new)
    direction = projection_edit.load(ROOT, DIRECTION); refresh_projection(direction, "版本：`integrated-direction-portfolio/v1.17`", "版本：`integrated-direction-portfolio/v1.18`", "20261002-direction-essay")
    panorama = projection_edit.load(ROOT, PANORAMA); refresh_projection(panorama, "版本：`integrated-outcome-panorama/v1.18`", "版本：`integrated-outcome-panorama/v1.19`", "20261002-outcome-essay")
    memory = projection_edit.load(ROOT, MEMORY)
    memory["shards"][MEMORY_003] = memory["shards"][MEMORY_003].rstrip() + f"\n\n{SID}：core generation-12 第四件索引的分片计数从11更正为12，编写说明区分初稿generation-5与当前generation-12/61基线；不改用户原文、候选、数学结论或Goal状态。STATE revision 296→297。\n"
    resume = (ROOT / RESUME).read_text()
    resume = once(resume, "## 历史停止点\n\n", "## 历史停止点\n\n" + f"{SID}：更正扩展认知第12片接入后的首屏分片数与历史/当前基线说明；core generation-12、Goal7和数学状态不变。\n\n")
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text())
    state["revision"] = 297; state["latest_session"] = SID
    state["execution_control"]["last_checkpoint_session"] = SID; state["execution_control"]["checkpoint_result"] = RESULT
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20261002-direction-essay-297"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20261002-outcome-essay-297"
    state["records"][SID] = {
      "depends_on": [], "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
      "full_sources": [SESSION,AUDIT,RUNS,RESULT,ESSAY,"扩展认知/012 - 后续理论靶、罗素模式 P 与工作意识.md"],
      "kind": "session", "lifecycle_status": "HISTORICAL", "path": SESSION,
      "related_records": [PREVIOUS,"A-CODEX-CORE-GENERATION-12-001"],
      "scope": "Correct the fourth-document shard count and state its historical/current core baselines. No user source, core payload, theory candidate, mathematical result, or Goal changes.", "source_hashes": {}, "status": "complete"}
    session = f"# {SID}\n\n- tier: T3 metadata correction; no mathematical claim.\n- role: GOVERNANCE_ALIGNMENT.\n- purpose: repair the fourth-document routing facts after generation-12 added shard 012.\n- unchanged: core generation-12/61 and its source/curation/transition; all research status and Goal7.\n"
    runs = {"schema_version":"hott-session-runs/v2","session_id":SID,"session_kind":"GOVERNANCE_ESSAY_ROUTING_ALIGNMENT","checkpoint_result":RESULT,"base_snapshot":plan["snapshot"],"formal_runs":[],"governance_runs":[{"tool":"cognition_runtime","status":"canonical checkpoint required"}],"new_math_claims":[]}
    texts = {rel:(ROOT/rel).read_text() for rel in R.MUTABLE}
    for doc in (direction,panorama,essay,memory): texts[doc["index_path"]]=doc["index_text"]; texts.update(doc["shards"])
    texts[RESUME]=resume; texts[STATE]=dump(state); texts[SESSION]=session; texts[AUDIT]=audit_text(manifest); texts[RUNS]=dump(runs)
    payload={"schema_version":"cognition-checkpoint/v1","session_id":SID,"authorization":"The user authorized a complete core-methodology integration. This narrow successor corrects the resulting fourth-document routing inconsistency without changing mathematics, candidates, Goals, commits, or publication.","load_profile":"governance","task_ids":[],"files":[{"path":p,"expected_sha256":sha((ROOT/p).read_bytes()) if (ROOT/p).is_file() else None,"text":v} for p,v in texts.items()]}
    R.prepare(ROOT,plan["snapshot"],payload)
    args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(dump(payload)); print(json.dumps({"status":"PREPARED","snapshot":plan["snapshot"],"revision":297,"files":len(texts)},ensure_ascii=False))

if __name__=="__main__": main()
