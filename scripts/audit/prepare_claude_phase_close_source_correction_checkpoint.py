#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prepare the checkpoint that corrects one source statement right after the phase close (2026-09-30).

While rewriting the root README after checkpoint S-GOV-20260930-CLAUDE-PARADOX-SEARCH-PHASE-CLOSE, the session found that
several texts said "the universe and these products have no finite level; experts have long known it (HoTT Book
Example 8.8.6; Kraus-Sattler 2015)".  Checked against the source (HoTT Book 2013, end of section 8.8): the product is the
Book's Example 8.8.6, but for the universe itself the Book only says it is expected and "has not yet been done";
Kraus-Sattler 2015 prove that the n-th universe of a univalent hierarchy is not an n-type.  The single universe with
higher inductive types is machine-proved in this repository (C-75); whether a published proof appeared later is left
to the literature check.

Scope of this checkpoint:

* 扩展认知 shard 011: the sentence is corrected and one limits bullet records the direction label chosen at the phase close;
* 全景视野 shard 002: one cell of `OUT-U-RUSSELL-UNIVERSE-QUESTIONING` is corrected (outcome panorama v1.15);
* STATE: the hash of community draft 03 (corrected before its first commit) is re-pinned in the Russell record, the
  phase-close follow-up records the new literature question Q0, and the session is recorded;
* MEMORY/003 and RESUME: one line each; the direction index only refreshes its revision.

The core is not changed (generation-10).  Apply with
.codex/tools/cognition_runtime.py checkpoint --snapshot <printed snapshot> --payload <output> --apply
"""

from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _load(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


P10 = _load("prep10", "scripts/audit/prepare_claude_core_generation_10_checkpoint.py")
PC = _load("prepclose", "scripts/audit/prepare_claude_paradox_search_phase_close_checkpoint.py")
R = P10.R
projection_edit = P10.projection_edit
replace_once = P10.replace_once
sha_file = P10.sha_file
check_paths = P10.check_paths

SESSION_ID = "S-GOV-20260930-CLAUDE-PHASE-CLOSE-SOURCE-CORRECTION"
PREV_SESSION = PC.SESSION_ID
PREV_REVISION = 292
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
GEN10 = PC.GEN10
SELF = "scripts/audit/prepare_claude_phase_close_source_correction_checkpoint.py"
CN050 = ".claude/思考与发现/CN-050 - UR 与芝诺的模式匹配：本来一句话就了结的“是同一个”，在 HoTT 的宇宙里永远了结不了.md"

AUTHORIZATION = (
    "User 2026-09-30 (local Claude Code session eadb3381): 把所有该做的，全部做完，我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。"
    " Under that instruction the session corrects a source statement it had itself introduced (the universe side of 'no finite level' was "
    "written as long known; the HoTT Book says expected but not yet done) and re-pins the hash of community draft 03, corrected before its first "
    "commit. No new mathematical claim; the core is unchanged; Goal7 / MO3-COVERAGE-C is not touched."
)

ESSAY_011_OLD_A = ("- 宇宙与这类乘积没有有限层，这件数学事实专家早就知道（HoTT Book 例 8.8.6；Kraus–Sattler 2015）。几何级数人人会算；新的是把它读成 UR，"
                   "并指出它指向哪一个前提。KC-000015 说，要找的正是这种现象在 HoTT 中也存在。这一读法没有做过文献查重。")
ESSAY_011_NEW_A = ("- 数学事实大多不新：这类乘积没有有限层，是 HoTT Book 的例 8.8.6；宇宙本身，书里写的是预计可以证明它不是任何 n-型、但尚未做出（§8.8 末尾），"
                   "Kraus–Sattler 2015 证明了单价宇宙层级里的第 n 个宇宙不是 n-型（不用高阶归纳类型），含高阶归纳类型的单个宇宙则在本仓库有机器证明（C-75），"
                   "此后的文献里有没有公开证明待查。几何级数人人会算；新的主要是把它读成 UR，并指出它指向哪一个前提。KC-000015 说，要找的正是这种现象在 HoTT 中也存在。"
                   "这一读法没有做过文献查重。（2026-09-30 回源更正：本片初写为“这件数学事实专家早就知道”，对宇宙一侧说过了头。）")
ESSAY_011_OLD_B = ("- 方向登记怎样挂（A 向为主、B 向为主，还是两向并列），以及用户这两天的原话怎样影响方向追踪与全景视野，由用户与研究 integrator 决定；"
                   "相关提问见 `.claude/思考与发现/` 下的 CN-049 与 CN-050。")
ESSAY_011_NEW_B = (ESSAY_011_OLD_B + "2026-09-30 阶段收尾时，研究发起人要求“把所有该做的，全部做完”，方向登记按会话此前的建议挂为 A 向为主、B 向读法在修复一侧"
                   "（方向追踪 `DIR-U-RUSSELL-EXISTENCE-QUESTIONING`）。")

PANORAMA_OLD = "宇宙与乘积没有有限层是已知数学；"
PANORAMA_NEW = ("乘积没有有限层是 HoTT Book 例 8.8.6，宇宙一侧书中写为预计、当时尚未做出（§8.8 末尾），本仓库 C-75 有机器证明，"
                "文献里是否已有公开证明待查（调研请求 Q0）；")

MEMORY_003_ADD = (
    f"\n{SESSION_ID}：阶段收尾之后的回源更正。“宇宙与这类乘积没有有限层，专家早就知道”对宇宙一侧说过了头：HoTT Book §8.8 末尾写的是预计可以证明、"
    "但尚未做出（乘积一侧才是例 8.8.6）；Kraus–Sattler 2015 证明的是层级里第 n 个宇宙不是 n-型。扩展认知 011 一句与全景罗素结果行一格更正，"
    "社区稿 03 在首次提交前更正并重新钉住哈希。revision 292→293。无新数学主张。\n"
)
RESUME_ADD = (
    f"{SESSION_ID}：阶段收尾之后的回源更正（宇宙一侧“没有有限层”的文献身份：HoTT Book 写为预计、尚未做出）；扩展认知 011、全景罗素结果行、"
    "社区稿 03 的哈希同步。\n\n"
)

NT = ("本单元（回源更正：扩展认知 011 一句与一条限度说明、全景罗素结果行一格、社区稿 03 两处并重新钉住其哈希）没有重新判断该条所指的内容；"
      "原文身份保留。")


def audit_rows() -> dict[int, tuple[str, str, str, str]]:
    rows = {n: (P10.AUDIT[n][0], "NOT_TOUCHED", NT, "—") for n in range(1, 55)}
    rows[15] = (P10.AUDIT[15][0], "ALIGNED",
                "原文要的是“寻找和证明，它在HoTT中也存在具体的现象、表现”；本单元把“这件数学事实专家早就知道”更正为“数学事实大多不新，宇宙一侧书中写为预计”，"
                "新颖性本来就不是判据，所以更正不改变判断（扩展认知 011；社区稿 03）",
                "若文献查重（调研请求 Q0）找到 2013 年之后的公开证明，按来源补引，判断不变")
    rows[54] = (P10.AUDIT[54][0], "ALIGNED",
                "本单元只更正来源身份；UR 的形状、两种教科书消解的对位与归因排序都不依赖“这件事早已有公开证明”",
                "若社区审计指出 UR 的“简单的事”被描述得不公，按其意见回源，与本单元无关")
    return rows


def audit_text() -> str:
    rows = audit_rows()
    lines = []
    counts: dict[str, int] = {}
    for n in range(1, 55):
        name, relation, assess, nxt = rows[n]
        for cell in (name, assess, nxt):
            if "|" in cell:
                raise SystemExit(f"AUDIT_CELL_PIPE:KC-{n:06d}")
        counts[relation] = counts.get(relation, 0) + 1
        lines.append(f"| `KC-{n:06d}` | {name} | {relation} | {assess} | {nxt} |")
    tally = "、".join(f"{k} {v}" for k, v in sorted(counts.items()))
    head = f"""# {SESSION_ID} 完整兼容审计

{GEN10}；54 KC。canonical writer 只授权新 session 目录第一层文件，所以本审计是单文件兼容 bundle；`G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001` 保持。逐条立场由本会话写成（本机 Claude Code 会话 eadb3381；Claude Opus 5.5）。

- core_change: NO — 核心认知仍是第 10 代（54 条），本单元不改。
- direction_change: NO — 方向追踪内容不变，索引只把 revision 刷到 293。
- panorama_change: YES_IN_PLACE — `OUT-U-RUSSELL-UNIVERSE-QUESTIONING` 的“禁止外推”一格更正（宇宙一侧没有有限层的文献身份）；索引 revision 293、版本 v1.15。
- essay_change: YES_IN_PLACE — 第 011 片“还差什么”一节的第三条按来源更正；“本片的限度”最后一条补记阶段收尾时的方向挂法。原文块未动。
- update_decision: 回源（HoTT Book 2013，§8.8 末尾）表明“宇宙与这类乘积没有有限层，专家早就知道”对宇宙一侧说过了头：书里写的是预计可以证明、但尚未做出；乘积一侧是例 8.8.6；Kraus–Sattler 2015 证明的是层级里第 n 个宇宙不是 n-型。按研究发起人“把所有该做的，全部做完”的指示一并更正，并重新钉住首次提交前改过的社区稿 03 的哈希。
- cross_conflicts: 无新冲突。上一单元 SESSION.md 说四件套“在本会话压缩后全文读过”，指的是第 10 代入核时那一次压缩之后；此后上下文又压缩了一次，见本单元 SESSION.md 的 load_receipt。
- unresolved: 文献查重新增 Q0（含高阶归纳类型的单个宇宙不是任何 n-型，2013 年后是否已有公开证明）；其余仍按 `{PC.REC_FOLLOW}`。

关系计数：{tally}（计数不认证理解）。

|KC ID|姿态|relation|assessment and evidence|next and falsifier|
|---|---|---|---|---|
"""
    tail = f"""

## 扩展认知按片回评

| 片 | 本单元的关系 | 说明 |
|---|---|---|
| 001–010 | 未触及 | 本单元未改变其判断 |
| 011 | 触及（一句更正、一条补记） | “数学事实大多不新”取代“专家早就知道”；方向挂法补记 |

## 已走过的路与即将作出的选择

已走过的路：阶段收尾 checkpoint（revision 292）之后，改写根 README 前回读收尾报告，发现“专家早就知道”一句；在 sciverse 全文里回读 HoTT Book §8.8 末尾与 Kraus–Sattler 2015 的摘要，确认对宇宙一侧说过了头；更正收尾报告、社区稿 03、调研请求（新增 Q0）、CN-050（补注二）、一页稿草稿（文首加注）；本 checkpoint 更正两处共享 owner 并重新钉住 03 的哈希。

即将作出的选择：根 README 按阶段收尾改写（不重复这一说法）；交接说明加注；Claude 总索引维护；提交与推送。

## 四项对齐与偏航分析

1. 用户主张：非现实性悖论即 UR；要找的是这种现象在 HoTT 中也存在（KC-000015、KC-000054）。
2. 不得收窄成：“全是已知事实，所以没有发现”；也不得反过来说成“发现了新定理”。
3. 怎样改变当前任务：来源身份按原文写；新颖性不是判据，判断不变。
4. 仍开放的证明义务：不变（元层的一致性与典范性；外部复核与文献查重；C-81 至 C-83 的第二平台重放）。

偏航风险与做法：这次的偏航是把“专家预期”写成“专家早已知道”，属于解释加码。做法：回源，按原文改，并在每一处更正旁写明更正。
"""
    return head + "\n".join(lines) + tail


def session_text() -> str:
    receipt = "\n".join(P10.load_receipt_rows())
    return f"""# {SESSION_ID}

阶段收尾之后的回源更正：扩展认知 011、全景视野罗素结果行、STATE（社区稿 03 的哈希、跟进项的 Q0）、MEMORY/003、RESUME。

- host: Claude Code（桌面应用 Code 标签页，本机 macOS），会话 eadb3381-629b-4b9b-9fc4-e0fb942a4a9b，分支 main
- model: Claude Opus 5.5（claude-opus-5-5）
- tier: T3
- role: 用户授权的阶段收尾登记的一部分（治理对齐，来源更正）；不是研究生成
- authorization: 用户 2026-09-30：把所有该做的，全部做完，我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。
- parent: `{PREV_SESSION}`；不关闭 Goal7 / MO3-COVERAGE-C

## load_receipt

**公开说明**：四件套全文是在本会话较早的上下文窗口里读的（第 10 代入核时，见 `S-GOV-20260930-CLAUDE-CORE-GENERATION-10-UR` 的 SESSION.md）。此后上下文又压缩了一次；压缩后核心认知哈希未变（`c4ec670e519b`，与 goal-x 开工回执一致），按 PROTOCOL 的收据制复认，没有全文重付。压缩后本会话回读了 Claude 总索引全文、上一单元的准备脚本全文、根 README 索引与七个分片、收尾报告、社区稿 03、KC-000015 与 KC-000052 至 KC-000054 原文，以及本单元改动的两处 owner 段落。上一单元 SESSION.md 的“在本会话压缩后全文读过”指的是第 10 代入核时那一次压缩之后。`STATE.json` 没有整体读入模型上下文，只读本事务触及的记录。表中是准备载荷时的哈希前缀、字节与行数。

|path|sha256 前 16 位|bytes|lines|
|---|---|---|---|
{receipt}

## 回源

- HoTT Book（2013，arXiv 版，sciverse 全文 `05a533d30addb060…`，§8.8 末尾，PDF 第 304 页）：“We expect it should also be possible to show that a universe 𝒰 itself is not an n-type for any n, using the fact that it contains higher inductive types such as 𝕊ⁿ for all n. However, this has not yet been done.”
- 同书 §7.1（PDF 第 227 页）：“(Kraus has also shown that the nth nested univalent universe is also not an n-type, without using any higher inductive types.)”
- Kraus–Sattler，ACM TOCL 2015（sciverse `9db35c429e8ec035…`）摘要：对单价宇宙层级 U₀ : U₁ : …，证明 Uₙ 不是 n-型。

## 做了什么

1. 扩展认知第 011 片：“还差什么”一节第三条按来源更正；“本片的限度”最后一条补记阶段收尾时的方向挂法。
2. 全景视野 002：`OUT-U-RUSSELL-UNIVERSE-QUESTIONING` 的“禁止外推”一格更正；索引 v1.15、revision 293。方向追踪索引只刷新 revision。
3. STATE：`{PC.REC_RUSSELL}` 重新钉住 `{PC.DOC03}`（首次提交前更正了两处）的哈希；`{PC.REC_FOLLOW}` 记下调研请求的 Q0；本 session 记录。
4. MEMORY/003、RESUME 各一行。
5. 本 checkpoint 之外、同一单元内：收尾报告第 5 节与第 10 节、社区稿 03 两处、调研请求（新增 Q0）、CN-050 补注二、一页稿草稿文首加注。

验证命令与结果见 RUNS.json。无新数学主张经本 checkpoint 交付。
"""


def runs_obj(snapshot: str) -> dict:
    return {
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "session_kind": "GOVERNANCE_SOURCE_CORRECTION",
        "checkpoint_result": RESULT_REL,
        "base_snapshot": snapshot,
        "formal_runs": [],
        "source_checks": [
            {"source": "HoTT Book (2013), arXiv version, end of section 8.8", "via": "sciverse full text doc 05a533d30addb060a89fba1d1bef15d1f6f115c1f01c8b7f6ed3b2660608179a",
             "finding": "universe not an n-type for any n: expected, 'has not yet been done'; Example 8.8.6 is the product"},
            {"source": "Kraus and Sattler, ACM TOCL 2015", "via": "sciverse doc 9db35c429e8ec03544f94874ce8628658f08a3a8966b0067dc025d7031286377 (abstract)",
             "finding": "U_n is not an n-type in a hierarchy of univalent universes, without higher inductive types"},
        ],
        "governance_runs": [
            {"tool": SELF, "command": "--output <payload>", "status": "PREPARED"},
            {"tool": ".codex/tools/cognition_runtime.py", "command": "checkpoint --snapshot <base_snapshot> --payload <payload> --apply",
             "status": "CHECKPOINT_COMMITTED expected; only the canonical result.json proves it"},
        ],
        "new_math_claims": [],
        "math_status_change": "NONE",
        "note": "Source correction right after the phase close; no mathematical claim is delivered by this checkpoint.",
    }


def state_edits(state: dict) -> None:
    session_path = f"{SESSION_REL}/SESSION.md"
    state["revision"] = PREV_REVISION + 1
    state["latest_session"] = SESSION_ID
    ec = state["execution_control"]
    ec["last_checkpoint_session"] = SESSION_ID
    ec["checkpoint_result"] = RESULT_REL

    rec = state["records"][PC.REC_RUSSELL]
    rec["source_hashes"] = {p: sha_file(p) for p in (PC.DOC02, PC.DOCREADME, PC.DOC03)}
    rec["revalidation"] = (rec["revalidation"] + " 2026-09-30 source correction (session " + SESSION_ID + "): draft 03 was corrected before its first "
                           "commit (the universe side of 'no finite level' had been written as long known; the HoTT Book says expected but not yet done) "
                           "and its hash re-pinned after reading.")
    if SESSION_ID not in rec["related_records"]:
        rec["related_records"].append(SESSION_ID)

    follow = state["records"][PC.REC_FOLLOW]
    follow["scope"] = (follow["scope"] + " Literature item (2) now also asks (Q0) whether a published proof exists that a universe containing higher "
                       "inductive types is not an n-type for any n: the HoTT Book (2013, end of section 8.8) says it was expected but not yet done; "
                       "this repository machine-proves it (C-75).")
    if REQUEST_REL not in follow["full_sources"]:
        follow["full_sources"].append(REQUEST_REL)
    if SESSION_ID not in follow["related_records"]:
        follow["related_records"].append(SESSION_ID)

    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, f"{SESSION_REL}/RUNS.json", f"{SESSION_REL}/CORE_COGNITION_AUDIT.md", RESULT_REL, PC.DOC03, PC.ESSAY_011],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV_SESSION, PC.REC_RUSSELL, PC.REC_FOLLOW],
        "scope": ("Source correction right after the phase close: the universe side of 'no finite level' was overstated as long known; the HoTT Book "
                  "says expected but not yet done. Essay shard 011 and one panorama cell corrected; community draft 03 corrected before its first commit "
                  "and re-pinned; literature question Q0 recorded. No new mathematics."),
        "source_hashes": {},
        "status": "complete",
    }


REQUEST_REL = PC.REQUEST


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    for p in (PC.DOC03, PC.REPORT, REQUEST_REL, CN050):
        if not (ROOT / p).is_file():
            raise SystemExit(f"EVIDENCE_MISSING:{p}")
    doc03 = (ROOT / PC.DOC03).read_text(encoding="utf-8")
    if "专家早就知道" in doc03 or "预计也能证明它不是任何 n-型" not in doc03:
        raise SystemExit("DOC03_NOT_CORRECTED")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != PREV_REVISION or state.get("latest_session") != PREV_SESSION:
        raise SystemExit(f"EXPECTED_REVISION_{PREV_REVISION}:{state.get('revision')}:{state.get('latest_session')}")
    if SESSION_ID in state["records"]:
        raise SystemExit(f"RECORD_ALREADY_EXISTS:{SESSION_ID}")

    plan = R.plan(ROOT, profile="governance")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    for old, new in (
        (f"source_state_revision: {PREV_REVISION}", f"source_state_revision: {PREV_REVISION + 1}"),
        (f"projection_generation: 20260930-direction-{PREV_REVISION}", f"projection_generation: 20260930-direction-{PREV_REVISION + 1}"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    panorama["shards"][PC.P2] = replace_once(panorama["shards"][PC.P2], PANORAMA_OLD, PANORAMA_NEW)
    for old, new in (
        (f"source_state_revision: {PREV_REVISION}", f"source_state_revision: {PREV_REVISION + 1}"),
        (f"projection_generation: 20260930-outcome-{PREV_REVISION}", f"projection_generation: 20260930-outcome-{PREV_REVISION + 1}"),
        ("版本：`integrated-outcome-panorama/v1.14`", "版本：`integrated-outcome-panorama/v1.15`"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    essay = projection_edit.load(ROOT, R.ESSAY)
    essay["shards"][PC.ESSAY_011] = replace_once(essay["shards"][PC.ESSAY_011], ESSAY_011_OLD_A, ESSAY_011_NEW_A)
    essay["shards"][PC.ESSAY_011] = replace_once(essay["shards"][PC.ESSAY_011], ESSAY_011_OLD_B, ESSAY_011_NEW_B)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    if not memory["shards"][PC.M3].endswith("\n"):
        memory["shards"][PC.M3] += "\n"
    memory["shards"][PC.M3] += MEMORY_003_ADD

    resume = (ROOT / PC.RESUME).read_text(encoding="utf-8")
    resume = replace_once(resume, "## 历史停止点\n\n", "## 历史停止点\n\n" + RESUME_ADD)

    state_edits(state)

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    texts: dict[str, str] = {path: (ROOT / path).read_text(encoding="utf-8") for path in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[PC.RESUME] = resume
    texts[session_path] = session_text()
    texts[audit_path] = audit_text()
    texts[runs_path] = json.dumps(runs_obj(plan["snapshot"]), ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    payloads = P10.core_payloads()
    blocks = P10.verify_essay_originals(texts, payloads)
    created = {session_path, audit_path, runs_path, RESULT_REL}
    for label, body in (("audit", texts[audit_path]), ("session", texts[session_path]), ("essay", ESSAY_011_NEW_A + ESSAY_011_NEW_B),
                        ("panorama", PANORAMA_NEW), ("memory", MEMORY_003_ADD + RESUME_ADD)):
        check_paths(label, body, created)
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": AUTHORIZATION,
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {"path": path, "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None, "text": value}
            for path, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": PREV_REVISION + 1, "session_id": SESSION_ID,
                      "files": len(texts), "essay_original_blocks_verified": blocks}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
