#!/usr/bin/env python3
"""Prepare revision 138: register the first LIT-CLASSICS-001 primary review."""
from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts/audit"
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260914-138-LIT-CLASSICS-FIRST-PASS"
PREV = "S-RES-20260914-137-R2-PROGRAMCODE-THIN-SLICE"
RECORD_ID = "A-LIT-CLASSICS-001"
GOAL_ID = "A-HOTT-MACHINE-OVERVIEW-GOAL-001"
PLAN_ID = "A-HOTT-PROGRAMMATIC-COMPLETENESS-001"
COVERAGE_ID = "A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001"
DENOMINATOR_ID = "A-LIT-DENOMINATOR-001"
R2_ID = "A-CUBICAL-PROGRAM-CODE-001"
INDEX = ".codex/research/hott/LIT-CLASSICS-001.md"
SHARD_ROOT = ".codex/research/hott/LIT-CLASSICS-001"
IMPORT = "audit/literature/LIT-CLASSICS-001/mineru/IMPORT.json"
IMPORTER = "scripts/audit/import_lit_classics_mineru.py"
PDF_README = "audit/literature/PDF-to-Markdown-20260914/README.md"
PROGRAM_006 = ".codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS/006 - 计算合法性主线与学术谱系覆盖审计.md"
DENOMINATOR_005 = ".codex/research/hott/LIT-DENOMINATOR-001/005 - 冻结判词、未完成审查与下一批全文.md"
STATUS = "CORE_GENERATION_4_LIT_CLASSICS_FIRST_PASS_R2_NATCODE_NEXT"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"

SPEC = importlib.util.spec_from_file_location("runtime_s138", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{text.count(old)}")
    return text.replace(old, new, 1)


def replace_line(text: str, marker: str, replacement: str) -> str:
    lines = text.splitlines()
    matches = [i for i, line in enumerate(lines) if line.startswith(marker)]
    if len(matches) != 1:
        raise ValueError(f"LINE_MATCH_COUNT:{marker}:{len(matches)}")
    lines[matches[0]] = replacement
    return "\n".join(lines) + "\n"


def add_once(values: list[str], item: str) -> None:
    if item not in values:
        values.append(item)


def audit_text() -> str:
    manifest = json.loads((ROOT / "核心认知.manifest.json").read_text(encoding="utf-8"))
    focus = {
        "KC-000001": "研究依据层加入经典原文与现代机器化对照，并保持 source-reported 与本项目机器证明分离。",
        "KC-000002": "Turing/Church/Gödel 的有效代码、decoder、规则枚举、证明检查和 representability 被整理为 Theory Schema 前提链。",
        "KC-000007": "12 份 MinerU 输出进入 main；正规化 origin 与输入 PDF 不字节相同的事实被显式保留。",
        "KC-000012": "ASK 现可精确区分 bounded evaluator、semi-decision、total decider、对象层表示和现实可完成性。",
        "KC-000013": "经典原文直接显示：存在有限见证的搜索与统一否定答案不是同一计算能力。",
        "KC-000016": "Lawvere 把 Russell/Cantor/Gödel 对角统一为有前提的 fixed-point schema；不能省略 naming/surjectivity。",
        "KC-000021": "PDF、MinerU Markdown、逐页结构、图片和 import tree hash 构成可追溯来源链。",
        "KC-000024": "不可停机路线获得 Turing/Church/Kleene/Rice 的精确对象和反误读边界。",
        "KC-000025": "Kleene self-reference 被还原为有效编号 + s-m-n + universal evaluation，而非文本无限展开。",
        "KC-000026": "2LTT 证明 inner HoTT 与 outer metatheory 必须区分；HoTT 对自身说话不是默认能力。",
        "KC-000027": "R2 继承程序自反边界所需的 numeric code、fairness、universality 和 certified reduction 已显式化。",
        "KC-000028": "EPF 路线能为候选 decider 构造发散 index，但 EPF 在 HoTT 中有明确 model/modality 适用域。",
        "KC-000031": "2LTT 的基础 conservativity 与强化后未知被纳入 exact HoTT calculus 选择。",
        "KC-000036": "Gödel、Rosser、Löb、O’Connor 与 Kirst–Peters 的条件链被分开；R4 仍未机器化。",
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`；本轮形成 LIT-CLASSICS-001 第一轮 primary review，不新增本项目数学 claim。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |",
        "|---|---|---|---|---|---|",
    ]
    for unit in manifest["units"]:
        kid = unit["id"]
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation = "DEEPENED" if kid in focus else "NOT_TOUCHED"
        assessment = focus.get(kid, f"本轮没有重新裁决“{label}”的数学、现实或哲学内容。")
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | `{INDEX}`；{kid} | Rosser/Post、R2 numeric/fair/universal、R4、natural consumer 与 reality bridge 仍开放。 |")
    lines += [
        "", "## 四件套交叉与更新归属", "",
        "- core_change: NO — 无新用户悖论／元数学原文。",
        "- direction_change: YES_IN_PLACE — LIT Classics 第一轮结束，当前转 R2-NATCODE-001。",
        "- panorama_change: YES_IN_PLACE — 新增 OUT-TOP-LIT-CLASSICS-001。",
        "- essay_change: NO。",
        "- update_decision: 新增两条 HoTT-specific candidate schema；均无 natural consumer，未提升为结果。",
        "- cross_conflicts: synthetic EPF 对 constructive metatheory 有效，但 Swan–Uemura 显示它不是完整 cubical universe 的无条件事实；以 universe/modality 资格化。",
        "- unresolved: Rosser/Post primary body、coverage slots、R2-NATCODE/FAIR/UNDEC、exact HoTT、EPF modality consumer、self-guarantee consumer、reality bridge。",
    ]
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    shards = sorted((ROOT / SHARD_ROOT).glob("*.md"))
    if len(shards) != 6:
        raise SystemExit("LIT_CLASSICS_SHARD_COUNT")
    required = [INDEX, IMPORT, IMPORTER, PDF_README, PROGRAM_006, DENOMINATOR_005]
    if any(not (ROOT / rel).is_file() for rel in required):
        raise SystemExit("LIT_CLASSICS_INPUT_MISSING")
    imported = json.loads((ROOT / IMPORT).read_text(encoding="utf-8"))
    if (imported.get("status"), imported.get("source_count"), imported.get("file_count"), imported.get("total_bytes")) != ("VALID", 12, 584, 15978067):
        raise SystemExit("MINERU_IMPORT_COUNTS")

    plan = R.plan(ROOT, profile="governance")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 137 or state.get("latest_session") != PREV:
        raise SystemExit("EXPECTED_REVISION_137_S137")
    if RECORD_ID in state["records"] or SESSION_ID in state["records"]:
        raise SystemExit("LIT_CLASSICS_RECORD_ALREADY_EXISTS")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_shard = "方向追踪/002 - 治理与用户方向.md"
    direction["shards"][direction_shard] = replace_line(
        direction["shards"][direction_shard],
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`",
        "| `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY` | 以 main 为唯一工作面推进基于计算合法性／不可停机代码的 HoTT 悖论探索；R1、R2 ProgramCode 与 LIT Classics 第一轮已贯通，继续 numeric/fair/undec、exact HoTT Gödel 与现实桥梁 | 用户 2026-09-14 当前指令与 active goal；rulings §22–§23；F-011/F-015/F-016 | `ACTIVE_USER_DIRECTION` | `COMPUTATIONAL_LEGITIMACY`, `SELF_REFERENCE`, `THEORY_SCHEMA`, `EVIDENCE_DISCIPLINE`, `PARADOX_DISCOVERY` | `OUT-TOP-LIT-DENOMINATOR-001`、`OUT-TOP-R1-FIXED-MACHINE-001`、`OUT-TOP-R2-PROGRAMCODE-001`、`OUT-TOP-LIT-CLASSICS-001` | 当前做 `R2-NATCODE-001`；随后补 Rosser/Post 与 `LIT-HOTT-COMPUTABILITY-001`，再做 FAIR/UNDEC；R4 与现实桥梁仍开放 | active goal；`.codex/research/hott/LIT-CLASSICS-001.md`；`audit/literature/LIT-CLASSICS-001/mineru/IMPORT.json` |",
    )
    for old, new in (
        ("source_state_revision: 137", "source_state_revision: 138"),
        ("projection_generation: 20260914-direction-119", "projection_generation: 20260914-direction-120"),
        ("semantic_status: CORE_GENERATION_4_R2_PROGRAMCODE_THIN_SLICE_PROVED_LIT_CLASSICS_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R2_PROGRAMCODE_THIN_SLICE_PROVED_LIT_CLASSICS_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    projection_edit.append_to_shard(
        panorama,
        "全景视野/005 - 证据队列抽样与证据卫生.md",
        "| `OUT-TOP-LIT-CLASSICS-001` | LIT Classics 第一轮：12 份用户 MinerU 转换导入；Turing/Church/Gödel/Kleene/Rice/Löb/Lawvere与 O’Connor/Kirst/2LTT/cubical assemblies 前提链；两条 HoTT-specific candidate schema | `DIR-TOP-COMPUTABILITY-MAIN-CONTINUITY`、`DIR-E-LOCAL-HISTORY-COVERAGE` | 当前 active goal 的文献—机器交替单元 | `VERIFIED_WITH_SCOPE / PRIMARY_CORPUS_REVIEW_IN_PROGRESS / NO_NEW_MATH_CLAIM` | import 12 sources / 584 files / 15,978,067 bytes / tree `cea1d649…` VALID；6-shard owner PASS；源 PDF 与 MinerU normalized origin 双身份；Kleene 150–155 视觉检查 | Rosser/Post primary body、Tarski/HBL/Rice–Shapiro/Rogers/Chaitin、citation graph 未闭合；外部 theorem 未在 main 重放；EPF modality 与 self-guarantee 均无 natural consumer | `.codex/research/hott/LIT-CLASSICS-001.md`；`audit/literature/LIT-CLASSICS-001/mineru/IMPORT.json` |",
    )
    for old, new in (
        ("source_state_revision: 137", "source_state_revision: 138"),
        ("projection_generation: 20260914-outcome-119", "projection_generation: 20260914-outcome-120"),
        ("semantic_status: CORE_GENERATION_4_R2_PROGRAMCODE_THIN_SLICE_PROVED_LIT_CLASSICS_NEXT", f"semantic_status: {STATUS}"),
        ("状态：`CORE_GENERATION_4_R2_PROGRAMCODE_THIN_SLICE_PROVED_LIT_CLASSICS_NEXT`", f"状态：`{STATUS}`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    queue = "MEMORY/001 - 当前执行队列.md"
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "3. 当前 Host goal",
        "3. 当前 Host goal 保持 ACTIVE。R1 与 R2 ProgramCode 第一薄层已机器闭合；`LIT-CLASSICS-001` 第一轮已形成 6-shard owner 并导入 12 份 MinerU 转换。文献把下一缺口固定为 numeric code／fairness／universality／certified reduction，以及 EPF modality 与 inner/outer 资格；最终 HoTT witness 仍未找到。",
    )
    memory["shards"][queue] = replace_line(
        memory["shards"][queue], "8. `LIT-DENOMINATOR-001`",
        "8. `LIT-DENOMINATOR-001` v1、R1、R2 ProgramCode 第一薄层与 LIT Classics 第一轮已完成各自 scoped 增量。当前做 `R2-NATCODE-001`；随后补 Rosser/Post 与 HoTT computability 文献，再推进 FAIR/UNDEC。转换入口有 13 个有效 PDF，其中 12 个已导入 MinerU；不 push、不 tag。",
    )
    projection_edit.append_to_shard(
        memory,
        "MEMORY/003 - 当前验证状态与顺序日志.md",
        "\n- S138 LIT Classics 第一轮：用户完成的 12 个 MinerU 目录已导入 main（584 files / 15,978,067 bytes / tree `cea1d649…`，verify VALID）；MinerU origin 与输入 PDF 均不字节相同，双身份保留。6-shard owner 提取 Turing circle-free≠modern halt、Church normal-form/Entscheidung、Gödel ω-consistency、Kleene s-m-n/SRT、Rice extensional class、Lawvere point-surjectivity、O’Connor representability/HBL 缺口、Kirst EPF/strong separation、2LTT inner/outer、Swan–Uemura CT modality。Rosser/Post primary body 仍缺；两条 HoTT-specific schema 均无 natural consumer。下一步 R2-NATCODE-001。\n",
    )
    essay = projection_edit.load(ROOT, R.ESSAY)

    frontier_path = ".codex/research/hott/FRONTIER.md"
    frontier = (ROOT / frontier_path).read_text(encoding="utf-8")
    frontier = replace_once(frontier, "# HoTT 研究前沿（S137 R2 ProgramCode 第一薄层完成）", "# HoTT 研究前沿（S138 LIT Classics 第一轮完成）")
    frontier = replace_once(
        frontier,
        "R1 固定机器与 R2 ProgramCode 第一薄层均已在 main 通过 F-011。后者以 C-191–C-194 给出有限程序表、总 decoder、universal bounded evaluator、R1 一致性与 controls；它仍没有 numeric code、fair enumeration、universality 或 undecidability。当前第一工作包转为 `LIT-CLASSICS-001`；随后返回 ProgramCode 编码／枚举与 `R2-FAIR-001`。exact HoTT calculus、strong representability、HoTT essentiality 与现实 bridge 均 OPEN。",
        "R1 与 R2 ProgramCode 第一薄层已在 main 通过 F-011；LIT Classics 第一轮现又固定了 numeric code/universal evaluation/s-m-n、proof representability、EPF modality 与 inner/outer 前提。12 份 MinerU 导入 VALID；Rosser/Post primary body 仍开放。当前第一工作包是 `R2-NATCODE-001`；随后补文献并推进 FAIR/UNDEC。exact HoTT calculus、natural consumer、HoTT essentiality 与现实 bridge 均 OPEN。",
    )
    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(
        resume, "## 当前停止点\n\n",
        "## 当前停止点\n\nS138：LIT Classics 第一轮已建立。12 份 MinerU 转换导入 VALID（584 files / tree `cea1d649…`）；6 shards 固定经典与现代前提。Rosser/Post、其余 coverage slots 仍 OPEN；无新数学 claim。下一步 `R2-NATCODE-001`，实现 ProgramCode 的自然数 encode/decode 与 evaluator 对齐。\n\n",
    )

    state["revision"] = 138
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = "CHECKPOINT_APPLIED_LIT_CLASSICS_FIRST_PASS"
    state["execution_control"]["status"] = STATUS
    state["execution_control"]["next_minimal_verification"] = "Implement R2-NATCODE-001 in main: numeric Instr/ProgramCode encoding and decoding with image round-trip, then align the numeric bounded evaluator."
    state["projection"]["status"] = STATUS
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["projection_generation"] = "20260914-direction-120"
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["semantic_status"] = STATUS
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["projection_generation"] = "20260914-outcome-120"
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["semantic_status"] = STATUS

    shard_rels = [str(path.relative_to(ROOT)) for path in shards]
    sources = [INDEX] + shard_rels + [IMPORT, IMPORTER, PDF_README]
    state["records"][RECORD_ID] = {
        "classification": "CLASSIC_PREMISE_CHAIN_ESTABLISHED_WITH_SCOPE",
        "depends_on": [],
        "evidence_status": "DOCUMENTED / PRIMARY_RELEVANT_SECTIONS_REVIEWED / MINERU_IMPORT_VERIFIED",
        "full_sources": sources,
        "kind": "literature_primary_corpus_review",
        "lifecycle_status": "OPEN_ISSUE",
        "path": INDEX,
        "related_records": [GOAL_ID, PLAN_ID, COVERAGE_ID, DENOMINATOR_ID, R2_ID, SESSION_ID],
        "scope": "First LIT-CLASSICS-001 primary review through Turing, Church, Goedel, Kleene, Rice, Loeb, Lawvere and five modern mechanised/HoTT contrasts; 12 MinerU conversions imported. Rosser/Post primary bodies and remaining classic/citation coverage stay open. External theorems are source-reported, not current-project machine proofs.",
        "source_hashes": {rel: R.sha((ROOT / rel).read_bytes()) for rel in sources},
        "status": "active",
    }
    for record_id in [GOAL_ID, PLAN_ID, COVERAGE_ID, DENOMINATOR_ID]:
        record = state["records"][record_id]
        add_once(record.setdefault("related_records", []), RECORD_ID)
        add_once(record.setdefault("full_sources", []), INDEX)
        record.setdefault("source_hashes", {})[INDEX] = R.sha((ROOT / INDEX).read_bytes())
    state["records"][GOAL_ID]["revalidation"] = f"{SESSION_ID}: classic premise chain and two HoTT-specific candidate schemas added; goal remains active because R2/R4, natural consumers, reality witness and comprehensive literature coverage remain open."
    plan_record = state["records"][PLAN_ID]
    for rel in shard_rels + [PROGRAM_006]:
        add_once(plan_record["full_sources"], rel)
        plan_record["source_hashes"][rel] = R.sha((ROOT / rel).read_bytes())
    plan_record["revalidation"] = f"{SESSION_ID}: primary classic premises now constrain R2/R4 and EPF modality; completeness envelope remains open."
    denominator = state["records"][DENOMINATOR_ID]
    denominator["source_hashes"][DENOMINATOR_005] = R.sha((ROOT / DENOMINATOR_005).read_bytes())
    denominator["revalidation"] = f"{SESSION_ID}: first classics review started from the frozen denominator; Rosser/Post and remaining primary/citation coverage stay open."
    coverage = state["records"][COVERAGE_ID]
    coverage["source_hashes"][PROGRAM_006] = R.sha((ROOT / PROGRAM_006).read_bytes())
    coverage["revalidation"] = f"{SESSION_ID}: classic premise chain established with scoped primary review; comprehensive coverage remains OPEN."

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    session = f"""# {SESSION_ID}

- 工作单元：LIT-CLASSICS-001 第一轮 primary-corpus review。
- 用户转换：12 个 MinerU 目录导入 main；584 files / 15,978,067 bytes / tree `cea1d649…`；verify VALID。
- 来源边界：MinerU normalized origin 与原 PDF 非字节同一；双身份与页结构保留；OCR/公式仍需具体页判断。
- 研究结果：经典 numeric code/universal/s-m-n/representation 条件链；EPF modality 与 2LTT inner/outer 两个 HoTT 资格轴。
- 候选：`CAND-HOTT-EPF-MODALITY-001`、`CAND-HOTT-SELF-GUARANTEE-001`；均无 natural consumer，不是发现结果。
- 未完成：Rosser/Post primary body、coverage slots/citations、R2 numeric/fair/universal/undec、R4、reality bridge。
- 新数学 claim：无；外部 theorem 统一为 source-reported。
- 下一步：`R2-NATCODE-001`。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "checkpoint_result": RESULT_REL,
        "mineru_import": {"sources": 12, "files": 584, "bytes": 15978067, "tree_sha256": imported["tree_sha256"], "verify": "VALID"},
        "logical_document": {"shards": 6, "validator": "PASS"},
        "new_math_claims": [],
        "next": "R2-NATCODE-001",
    }, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    state["records"][SESSION_ID] = {
        "depends_on": [], "evidence_status": "VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, audit_path, runs_path, RESULT_REL, INDEX, IMPORT],
        "kind": "session", "lifecycle_status": "HISTORICAL", "path": session_path,
        "related_records": [PREV, RECORD_ID, GOAL_ID, R2_ID],
        "scope": "Register the first LIT-CLASSICS-001 primary review and MinerU import; route the next code slice to R2-NATCODE-001.",
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
        "authorization": "Advance the active goal by ingesting the user-produced MinerU corpus, extracting classic premises, and continuing to the next R2 code slice.",
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": rel, "expected_sha256": R.sha((ROOT / rel).read_bytes()) if (ROOT / rel).exists() else None, "text": value} for rel, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 138, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
