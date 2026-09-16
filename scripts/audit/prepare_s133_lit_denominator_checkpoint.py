#!/usr/bin/env python3
"""Prepare revision 133: register the frozen LIT-DENOMINATOR-001 snapshot."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260914-133-LIT-DENOMINATOR-001"
PREV = "S-GOV-20260914-132-ACTIVE-MACHINE-OVERVIEW-GOAL"
RECORD_ID = "A-LIT-DENOMINATOR-001"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-001"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
AUDIT_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
INDEX = ".codex/research/hott/LIT-DENOMINATOR-001.md"
SHARD_ROOT = ".codex/research/hott/LIT-DENOMINATOR-001"
SNAPSHOT = "audit/literature/LIT-DENOMINATOR-001/discovery-20260914"
MANIFEST = f"{SNAPSHOT}/MANIFEST.json"
CANDIDATES = f"{SNAPSHOT}/DISCOVERY-CANDIDATES.json"
TRIAGE = f"{SNAPSHOT}/TRIAGE.json"
BUILD = "scripts/audit/build_lit_denominator_discovery.py"
TRIAGE_TOOL = "scripts/audit/triage_lit_denominator_candidates.py"
TEST = "scripts/audit/test_lit_denominator.py"
PROGRAM_PLAN_SHARD = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
STATUS = "CORE_GENERATION_4_LIT_DENOMINATOR_V1_FROZEN_R1_MAIN_REPLAY_NEXT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s133", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_line(text: str, marker: str, replacement: str) -> str:
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000001": "三问中的依据层新增具名学术分母和可重放 discovery/triage。",
        "KC-000002": "文献来源按 HoTT 构造、计算机制和机器 TaskSpec 路由，而非只列标题。",
        "KC-000007": "两个 metadata provider、核心 seed 和 UNCLASSIFIED remainder 防止单一检索/训练先验控制分母。",
        "KC-000008": "经典悖论启发被放入 FND/MOC/PAR/HCT/MET 谱系而不替代 HoTT 实例。",
        "KC-000012": "ASK 的学术依赖分解为 halting、semi-decision、proof search、provability 与 representability。",
        "KC-000013": "理论工具性异化现在有 partiality/dominance/guarded/cubical 文献反约束。",
        "KC-000017": "33 seed 中 20 个 API exact miss 直接证明不能把检索排名当知识边界。",
        "KC-000021": "metadata 与文献只作来源；数学结论继续需要 main 机器证明。",
        "KC-000024": "不可停机/不完备谱系获得七主题族、18 查询与机器映射槽。",
        "KC-000025": "Kleene/Lawvere/Löb/strictified syntax 等进入自指候选前提队列。",
        "KC-000027": "程序继承界限将由 R2 对象机和 synthetic computability 文献交叉核验。",
        "KC-000028": "反射自证线加入 internal sconing、2LTT、MetaRocq 与 type-in-type syntax 来源。",
        "KC-000030": "理论经济统观获得截至 2026-09-14 的可审计学术发现分母。",
        "KC-000031": "严格范型/覆盖将用 syntax、conversion、cofibration complexity 和 conservativity 文献判断。",
        "KC-000036": "Gödel路线区分经典、数值编码、synthetic、Agda/Lean/Coq 与 exact HoTT 义务。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮冻结学术发现分母，不新增数学 claim。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的数学、物理或哲学内容。")
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{INDEX}`；{kid} | 全文/citation/primary qualification 与 R2 仍开放。 |")
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户悖论/元数学原文。",
        "- direction_change: YES_IN_PLACE — 计算合法性方向加入 LIT denominator 结果并转 R1 main replay。",
        "- panorama_change: YES_IN_PLACE — 新增 OUT-TOP-LIT-DENOMINATOR-001。",
        "- essay_change: NO。",
        "- update_decision: denominator v1 frozen；corpus review/incompleteness research remains active。",
        "- cross_conflicts: 36/36 API 请求成功但 33 seed 仍有 20 exact miss；已由强制 seed 并集化解，不伪称全面。",
        "- unresolved: 原 19 全文、32 direct/164 adjacent/1745 unclassified、citation/venue snapshots、R1 main replay、R2/R4/现实桥梁。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    shards = sorted((ROOT / SHARD_ROOT).glob("*.md"))
    required = [ROOT / rel for rel in [INDEX, MANIFEST, CANDIDATES, TRIAGE, BUILD, TRIAGE_TOOL, TEST, PROGRAM_PLAN_SHARD]] + shards
    if len(shards) != 5 or any(not path.is_file() for path in required):
        raise SystemExit("DENOMINATOR_INPUT_MISSING")
    discovery = json.loads((ROOT / MANIFEST).read_text(encoding="utf-8"))
    triage = json.loads((ROOT / TRIAGE).read_text(encoding="utf-8"))
    if (discovery["successful_fetches"], discovery["failed_fetches"], discovery["candidate_count"]) != (36, 0, 1941):
        raise SystemExit("DISCOVERY_COUNTS")
    if triage["counts"] != {"ADJACENT_TITLE_SIGNAL": 164, "DIRECT_TITLE_SIGNAL": 32, "UNCLASSIFIED_TITLE_INSUFFICIENT": 1745}:
        raise SystemExit("TRIAGE_COUNTS")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 132 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_132_S132")
    if RECORD_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("RECORD_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][direction_shard] = replace_line(
        direction["shards"][direction_shard],
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 为唯一工作面推进基于计算合法性/不可停机代码的 HoTT 悖论探索；把文献、计划和候选证据纳入项目治理，再完成 R2、exact HoTT Gödel 与现实桥梁 | 用户 2026-09-14 当前指令与 active goal；rulings §22–§23；F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY` | `OUT-TOP-COMPUTABILITY-CONTINUITY-AUDIT`、`OUT-TOP-LIT-DENOMINATOR-001` | `LIT-DENOMINATOR-001` v1 已冻结；下一步把 R1 固定对象机在 main 独立重放，再做 `R2-PROGRAMCODE-001`，随后返回 `LIT-CLASSICS-001` | active goal；项目程序化探索规划第 006 片；`.codex/research/hott/LIT-DENOMINATOR-001.md` |",
    )
    for old, new in (
        ("source_state_revision: 132", "source_state_revision: 133"),
        ("projection_generation: 20260914-direction-114", "projection_generation: 20260914-direction-115"),
        ("semantic_status: CORE_GENERATION_4_ACTIVE_HOTT_MACHINE_OVERVIEW_GOAL", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_ACTIVE_HOTT_MACHINE_OVERVIEW_GOAL`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    panorama_shard = "全景视野/005 - 证据队列抽样与证据卫生.md"
    projection_edit.append_to_shard(
        panorama,
        panorama_shard,
        "| `OUT-TOP-LIT-DENOMINATOR-001` | 截至 2026-09-14 的 HoTT 可计算性/不完备性文献发现分母 v1：七主题族、渠道/场馆、18 查询×2 provider、33 核心 seed、全量 title triage 与 UNCLASSIFIED remainder | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-E-LOCAL-HISTORY-COVERAGE` | 当前 active goal 的第一有界工作单元 | `VERIFIED_WITH_SCOPE / DENOMINATOR_V1_FROZEN / CORPUS_REVIEW_IN_PROGRESS` | 36/36 fetch、1,941 unique candidates；32 direct / 164 adjacent / 1,745 unclassified，合计 remainder=0；33 seed 13 exact hit/20 manual，证明 metadata negative 不可外推；raw/gzip/candidate/hash 离线重放 VALID，专项 4/4 | 不证明 1,941 条已人工审查、全文/citation/venue coverage 完成、学术界全面覆盖或任何 HoTT 数学结论 | `.codex/research/hott/LIT-DENOMINATOR-001.md`；`audit/literature/LIT-DENOMINATOR-001/discovery-20260914/MANIFEST.json`；`TRIAGE.json` |",
    )
    for old, new in (
        ("source_state_revision: 132", "source_state_revision: 133"),
        ("projection_generation: 20260914-outcome-114", "projection_generation: 20260914-outcome-115"),
        ("semantic_status: CORE_GENERATION_4_ACTIVE_HOTT_MACHINE_OVERVIEW_GOAL", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_ACTIVE_HOTT_MACHINE_OVERVIEW_GOAL`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    queue = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][queue] = replace_line(
        memory["shards"][queue],
        "8. 当前优先顺序",
        "8. `LIT-DENOMINATOR-001` v1 已冻结（18×2、1,941 candidates、32/164/1,745、33 seed 13/20）；全文/citation/场馆/primary corpus 仍开放。当前下一步：把 R1 固定对象机在 main 独立重放并进入 F-011，随后推进 `R2-PROGRAMCODE-001`；再返回 `LIT-CLASSICS-001`。不 push、不 tag。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S133 `LIT-DENOMINATOR-001`：冻结 2026-09-14 截止日、七主题族、渠道/场馆、18 个查询和 33 核心 seed；Crossref/OpenAlex 36/36 成功，1,941 去重候选。保守 title triage=32 direct / 164 adjacent / 1,745 unclassified，全部保留；33 seed 仅 13 exact hit、20 manual，直接证明 API 无命中不能作不存在结论。raw/gzip/candidate/hash 离线 verify VALID，专项 4/4。分母 v1 完成；全文/citation/venue/primary review 未完成。下一步 R1 main replay→R2 ProgramCode→LIT Classics。无新数学 claim。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(
        frontier,
        "当前第一工作包为 `LIT-DENOMINATOR-001`：冻结 1931–2026 的经典、类型论、HoTT/cubical 和机器化文献分母；随后让 `LIT-CLASSICS-001`/`LIT-HOTT-COMPUTABILITY-001` 与 `R2-PROGRAMCODE-001`/`R2-FAIR-001` 交替推进。R1 固定程序发散仅有 contributor 证据；R2 universal halting undecidability、exact HoTT calculus、strong representability、HoTT essentiality 与现实 bridge 均 OPEN。",
        "`LIT-DENOMINATOR-001` v1 已冻结：18×2 discovery、1,941 candidates、32/164/1,745 total triage、33 seed 13 exact/20 manual。全文/citation/场馆与 primary qualification 仍 OPEN。当前第一工作包转为 R1 main 独立重放；闭合后做 `R2-PROGRAMCODE-001`，随后返回 `LIT-CLASSICS-001`。R2 universal halting undecidability、exact HoTT calculus、strong representability、HoTT essentiality 与现实 bridge 均 OPEN。",
    )
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\nS133：`LIT-DENOMINATOR-001` v1 已冻结并验证（18 queries×2 providers、1,941 candidates、32 direct/164 adjacent/1,745 unclassified、33 seed 13 exact/20 manual）。这不是全文覆盖。下一步把 R1 固定对象机从只读 contributor 证据在 main 独立重放并过 F-011，然后做 R2 ProgramCode，再回 LIT Classics。\n\n",
    )

    state["revision"] = 133
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_LIT_DENOMINATOR_V1"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = "Independently replay the fixed machine R1 package in main with formal source, canonical kernel run and claim index; then begin R2-PROGRAMCODE-001 and return to LIT-CLASSICS-001."
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-115"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["semantic_status"] = STATUS
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-115"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["semantic_status"] = STATUS

    shard_rels = [str(path.relative_to(ROOT)) for path in shards]
    human_sources = [INDEX] + shard_rels + [MANIFEST, BUILD, TRIAGE_TOOL, TEST]
    source_hashes = {rel: R.sha((ROOT / rel).read_bytes()) for rel in human_sources + [CANDIDATES, TRIAGE]}
    state["records"][RECORD_ID] = {
        "classification": "LITERATURE_DISCOVERY_DENOMINATOR_V1_FROZEN",
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / DENOMINATOR_V1_FROZEN",
        "full_sources": human_sources,
        "kind": "literature_coverage_denominator",
        "lifecycle_status": "CURRENT",
        "path": SNAPSHOT,
        "path_mode": "scope_locator",
        "related_records": [GOAL_ID, PLAN_ID, AUDIT_ID, SESSION_ID],
        "scope": "Cutoff 2026-09-14; seven topic families, declared channels/venues, 18 queries over Crossref/OpenAlex, 1,941 unique candidates, total non-excluding title triage and 33 forced core seeds. Denominator frozen; primary corpus review and comprehensive coverage remain open.",
        "source_hashes": source_hashes,
        "status": "complete",
    }
    goal_record = state["records"][GOAL_ID]
    add_once(goal_record["full_sources"], INDEX)
    add_once(goal_record.setdefault("related_records", []), RECORD_ID)
    goal_record["source_hashes"][INDEX] = R.sha((ROOT / INDEX).read_bytes())
    goal_record["source_hashes"]["feature-list.md"] = R.sha((ROOT / "feature-list.md").read_bytes())
    goal_record["revalidation"] = f"{SESSION_ID}: LIT denominator v1 frozen; goal remains active because primary corpus, R1 main replay, R2/R4 and reality witness are open."
    plan_record = state["records"][PLAN_ID]
    for rel in [INDEX] + shard_rels:
        add_once(plan_record["full_sources"], rel)
        plan_record["source_hashes"][rel] = R.sha((ROOT / rel).read_bytes())
    plan_record["source_hashes"][PROGRAM_PLAN_SHARD] = R.sha((ROOT / PROGRAM_PLAN_SHARD).read_bytes())
    add_once(plan_record.setdefault("related_records", []), RECORD_ID)
    audit_record = state["records"][AUDIT_ID]
    add_once(audit_record["full_sources"], INDEX)
    add_once(audit_record.setdefault("related_records", []), RECORD_ID)
    audit_record["source_hashes"][INDEX] = R.sha((ROOT / INDEX).read_bytes())
    audit_record["revalidation"] = f"{SESSION_ID}: discovery denominator frozen, but primary corpus/comprehensive coverage remains OPEN; no lifecycle promotion."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 工作单元：完成 active goal 的 `LIT-DENOMINATOR-001` v1。
- 分母：2026-09-14 cutoff；七主题族；声明场馆/渠道；18 个查询；Crossref/OpenAlex。
- 运行：36/36 fetch 成功；1,941 unique candidates；raw/gzip/manifest/candidate identity 可重放。
- 分层：32 direct / 164 adjacent / 1,745 unclassified；无候选被 title triage 排除。
- 反遗漏：33 forced seeds 中 13 exact hit / 20 manual，证明 metadata negative 不可外推。
- 验证：discovery VALID、triage VALID、专项 4/4、shard PASS。
- 边界：denominator v1 完成；primary/full-text/citation/venue/comprehensive coverage 未完成；无数学 claim。
- 下一步：R1 main 独立重放并过 F-011 → R2 ProgramCode → LIT Classics。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "discovery": {"queries": 18, "providers": 2, "fetches": 36, "failures": 0, "candidates": 1941, "verify": "VALID"},
        "triage": {"direct": 32, "adjacent": 164, "unclassified": 1745, "seeds": 33, "seed_exact": 13, "seed_manual": 20, "verify": "VALID"},
        "tests": "4/4 PASS", "new_math_claims": []
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [], "evidence_status": "VERIFIED_WITH_SCOPE",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, INDEX, MANIFEST, TEST],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, RECORD_ID, GOAL_ID],
        "scope": "Freeze and verify the literature discovery denominator; no primary-corpus completion or mathematical claim.",
        "source_hashes": {}, "status": "complete",
    }

    texts: dict[str, str] = {rel: (ROOT / rel).read_text(encoding="utf-8") for rel in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[frontier_path] = frontier
    texts[resume_path] = resume
    texts[session_path] = session
    texts[audit_path] = audit_text()
    texts[runs_path] = runs
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "Advance the active user goal by completing LIT-DENOMINATOR-001 in main and preserving all evidence and limits.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 133, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
