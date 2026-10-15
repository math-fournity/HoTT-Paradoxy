#!/usr/bin/env python3
"""Prepare the CG-010 checkpoint: core generation-15 (KC-000076 to KC-000083) and its letter-evolution registry.

Scope (research sponsor, 2026-10-15):

* the generation-15 plan approved in the GLM ruling session, round 17 ("按照你说的入核"); plan in
  .claude/goals/CG-010-remaining-formalization-alignment/待你裁定-人话版/10-裁定结果-20261015.md (入核方案):
  new originals of 10-14 and 10-15, a letter-evolution registry, and the current meanings registered;
* the research sponsor's 2026-10-15 instruction to the executing session: "确保了这些之后，你立即开始做，直至全部做完".

The core was built on disk by scripts/audit/build_core_cognition.py with core-cognition-curation-v15.json.
This payload moves STATE.current_core to it through the runtime's canonical core_transition path, and writes the
session bundle.  Following the root CLAUDE.md (section 1, item 3: use the existing scripts minimally, no added
ritual), nothing else changes: direction, panorama, essay, MEMORY, FRONTIER and LESSONS are carried unchanged;
RESUME gets one pointer.  The AI elaboration of the new units lives in
docs/ZFC-1的问题-原话逐句对照与机器证明-20261015.md and in the registry 核心认知-字母演变登记表.md.

The script only builds the payload; it writes nothing into the repository.  Apply it with
.codex/tools/cognition_runtime.py checkpoint --snapshot <printed snapshot> --payload <output> --apply
Modelled on scripts/audit/prepare_claude_cg006_core_generation_14_checkpoint.py.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SPEC = importlib.util.spec_from_file_location("runtime_claude15", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)

SESSION_ID = "S-GOV-20261015-CLAUDE-CG010-CORE-GENERATION-15"
PREV_SESSION = "S-GOV-20261008-CLAUDE-CG006-CORE-GENERATION-14"
PREV_REVISION = 313
NEW_REVISION = PREV_REVISION + 1
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
PREPARE_SELF = "scripts/audit/prepare_claude_cg010_core_generation_15_checkpoint.py"

CORE = "核心认知.md"
MANIFEST = "核心认知.manifest.json"
CURATION = "scripts/audit/core-cognition-curation-v15.json"
TRANSITION = "audit/core-cognition-generation-15-transition-20261015.json"
REGISTRY = "核心认知-字母演变登记表.md"
SRC_CLAUDE = "sources/prompts/Claude-012Opus-ZFC-1与Q的定义-用户原文-20261014至20261015.md"
SRC_GLM = "sources/prompts/GLM-CG010裁定-同一个Q即A与现实观-用户原文-20261015.md"
RULINGS = ".claude/goals/CG-010-remaining-formalization-alignment/待你裁定-人话版/10-裁定结果-20261015.md"
LINE_BY_LINE = "docs/ZFC-1的问题-原话逐句对照与机器证明-20261015.md"
GEN14 = "core-cognition-generation-14"
GEN15 = "core-cognition-generation-15"
CORE_TRANSITION = {"from_generation": GEN14, "to_generation": GEN15, "manifest": MANIFEST, "transition": TRANSITION}
FROM_REF = "ffb2c31192aaf8e4c416f8663e2c4dc78421024d"

REC_CORE = "A-CLAUDE-CORE-GENERATION-15-001"
REC_PREV_CORE = "A-CLAUDE-CORE-GENERATION-14-001"
NEW_KCS = [f"KC-{n:06d}" for n in range(76, 84)]

AUTHORIZATION = (
    "Research sponsor, 2026-10-15, GLM ruling session round 17: \"按照你说的入核\" — generation 15 = new originals of 10-14/10-15 "
    "(the 10-14 evening paragraph, the 10-14 late-night sentence, the 矛盾 sentence, the 10-15 restatement and reality view) + a "
    "letter-evolution registry + the current meanings registered; ghost quotes stay out, work instructions stay out. Research sponsor, "
    "2026-10-15, to this session (91beaf35, resumed from 95a1a81b): \"确保了这些之后，你立即开始做，直至全部做完\". Written in the "
    "independent worktree claude/012-opus-w8; not pushed."
)


def sha_file(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


# Pre-existing drift: after revision 313 three CG-007 commits on dev (4c0f8df6d, fda0287b0, 7452752fa; merged here by
# cc7eea2b) edited this MEMORY shard directly, without a checkpoint, so HEAD.tracked holds a stale hash and plan() stops
# with UNCOMMITTED_STATE.  Precedent S154 (prepare_s154_core_generation_7_rename_premise001_checkpoint.py): rebuild
# HEAD.tracked from the committed files, keep revision and latest_session, and say so in the session record.
EXPECTED_DRIFT = {"MEMORY/001 - 当前执行队列.md"}
HEAD_DRIFT_NOTE = (
    "既有漂移：第 313 版之后，CG-007 在 `dev` 上的三次提交（`4c0f8df6d`、`fda0287b0`、`7452752fa`，经 `cc7eea2b` 合入本分支）"
    "直接改了 `MEMORY/001 - 当前执行队列.md`，没有经过 checkpoint，HEAD.tracked 的哈希因此过期，plan 报 `UNCOMMITTED_STATE`。"
    "按 S154 的先例，从已提交的文件重建 HEAD.tracked，revision 与 latest_session 不变；本会话没有改这一分片的内容。"
)


def repair_head() -> list[str]:
    head_path = ROOT / R.HEAD
    head = json.loads(head_path.read_bytes())
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if head.get("revision") != state.get("revision") or head.get("latest_session") != state.get("latest_session"):
        raise SystemExit("HEAD_STATE_MISMATCH")
    tracked: dict[str, str] = {}
    for rel in R.MUTABLE:
        data = R.read_bytes(ROOT, rel)
        tracked[rel] = R.sha(data)
        index = R.parse_shard_index(data, rel)
        if index is not None:
            for row in index["shards"]:
                tracked[row["path"]] = R.sha(R.read_bytes(ROOT, row["path"]))
    old = head.get("tracked", {})
    drifted = sorted(p for p in set(tracked) | set(old) if tracked.get(p) != old.get(p))
    unexpected = [p for p in drifted if p not in EXPECTED_DRIFT]
    if unexpected:
        raise SystemExit(f"UNEXPECTED_HEAD_DRIFT:{unexpected}")
    if drifted:
        head["tracked"] = tracked
        head_path.write_bytes(R.dump(head))
    return drifted


# ----------------------------------------------------------------------------------------------
# per-KC audit (single-file v1 table, strict KC order)
# ----------------------------------------------------------------------------------------------

DEFAULT_ROW = ("NOT_TOUCHED",
               "本单元（核心认知第 15 代入核、字母演变登记表、ZFC-1 原话逐句对照）没有重新判断该条所指的内容；原文身份保留。",
               "若字母演变登记表与本条当时的字母意思不符，以原文为准改登记表")

TOUCHED: dict[str, tuple[str, str, str]] = {
    "KC-000004": ("ALIGNED", "KC-000083（10-15）把本条“运动是量子化的”说成“只看量子化这一层就够、现实是跳着完成的”；离散一侧的数学对应物是 C-106 (3)(4)、C-107、C-108 (4)、C-424 (11)(12)", "若把现实判断当成定理，判越界"),
    "KC-000012": ("ALIGNED", "Q 按 KC-000076 定义为 ASK 那一问；登记表“Q”“ASK”两节记下本条里 Q 是被分析的那个问题", "若把本条的 Q 读成 10-14 的观察力，判字母漂移"),
    "KC-000013": ("ALIGNED", "同 KC-000012；“绕过 ASK”即没有门（C-421）", "同上"),
    "KC-000014": ("ALIGNED", "“理论中绕过 ASK 然后完成”就是 A 的样子（KC-000077）；逐句对照第 2 节第 2、12 行", "若只算第一种方向，判漏"),
    "KC-000022": ("ALIGNED", "第二种悖论（现实不能完成、理论当作已完成）即 A；第一种的实例是芝诺与圆环", "同上"),
    "KC-000023": ("ALIGNED", "“ZFC 本身试图以无时序的思维，绕过 ASK”与 KC-000076、KC-000078 同向", "若把 ZFC 的问题收窄成某条公理，判偏"),
    "KC-000024": ("ALIGNED", "“ASK 会拒绝”对应门：C-431（不设门的定义原则推出一切）是它的形式影子", "若把门说成判完一切停机，判越界（答补不上，C-422）"),
    "KC-000047": ("ALIGNED", "KC-000081（D5-3 作确认读）：矛盾是理论结果与现实的矛盾，即本条的反证法；逐句对照第 2 节第 4 行", "若把矛盾读成形式上的 ⊥，判偏（CN-080）"),
    "KC-000048": ("ALIGNED", "KC-000083 把芝诺的问题分成两个：A 宣布走完，稠密造出走不完；稠密与 A 是两个前提（CN-081 §3.1）", "若把稠密说成 A 的一种，判混同"),
    "KC-000054": ("ALIGNED", "UR 记入登记表；跑者算不算 UR 已按第 11 站不再单独判定，跑者句子留作 README 素材", "若由 AI 替研究发起人判 UR，判越权"),
    "KC-000059": ("ALIGNED", "登记表把本条的“模式 P”与 KC-000068 的“数学幻觉 P”分开：同一个字母，两件无关的事", "若混用两个 P，判字母漂移"),
    "KC-000062": ("ALIGNED", "同 KC-000059；P-DAG 自 10-08 暂停", "同上"),
    "KC-000063": ("ALIGNED", "Z0 读作“ZFC 一遍一遍找自己的矛盾”，D2-2 确认；Q0、Q1…、Z1…、R1… 记为当时的编号", "若把 Q0 读成现行的 Q，判字母漂移"),
    "KC-000064": ("ALIGNED", "圆环逐句形式化 C-424 为唯一标准（D7）；合回的远端就是芝诺跑者", "若用旧 Markov 写法代表圆环，判过时"),
    "KC-000065": ("ALIGNED", "精度不够的两种表现形式对应 C-114（D1-1 依原文落定）", "若把两种毛病合成一种，判偏"),
    "KC-000066": ("ALIGNED", "“不是没有，只是没有完备的观察力”是两层中的“能答多少”，另一层是“当不当门槛”（D1-2）", "同上"),
    "KC-000067": ("CORRECTED", "研究发起人 10-15 自己重述（KC-000082）：此处“同样一个……Q”实指 A；原文保留，登记表与逐句对照标出", "若按字面把这里的 Q 当观察力去证“同一个 Q”，判过时"),
    "KC-000068": ("DEEPENED", "逐句对照全文（docs/ZFC-1的问题-原话逐句对照与机器证明-20261015.md 第 2 节）；10-14 的 KC-000076–KC-000079 给出 Q、A 的定义与两次选择；“ZFC-1 导致 B”按 D4 定形，被告为 A", "若把本条的 A（想要的结果）与 10-14 的 A（动作）混为一谈而不标，判字母漂移"),
    "KC-000069": ("ALIGNED", "魔鬼交易的形式：吃下 P 又能机械检查的理论要么不能检查、要么矛盾（C-90、C-99）；魔鬼收走的那一份是 Z0（C-417、C-427）", "若把比喻当成定理，判越界"),
    "KC-000070": ("ALIGNED", "全部 ZFC 结果都在 Foundation 的 bare 𝗭𝗙𝗖 上", "若把扩张的结果说成 bare ZFC，判越界"),
    "KC-000071": ("ALIGNED", "B 即 main 的 HoTT 那件事（H0）；成因 A 加单价性，被告 A（D4；C-430）", "若把单价性说成被告，判与裁定冲突"),
    "KC-000073": ("ALIGNED", "哥德尔一路作为深化保留：研究发起人 10-15“哥德尔的启发我们可以参考……没有帮助，我们就沿着自己的方向一路进行到底”", "若让哥德尔一路定议程，判偏"),
    "KC-000074": ("ALIGNED", "想法 T 的形式（C-114）D1-1 依原文落定", "同上"),
}
NEW_ROWS = {
    "KC-000076": "本代新增。Q 的定义；逐句对照第 3 节第 1–3 行：两层（C-99、C-100、C-105；C-421）；“算法合法的最根本的前提”的形式影子 C-431；研究发起人称末句为“全文最实的落点”",
    "KC-000077": "本代新增。两次选择在最简一层是同一原则（C-418、C-425、C-426）；A 的定义与几种数学形态；逐句对照第 3 节第 4、5 行",
    "KC-000078": "本代新增。罗素的计算内核与 HoTT 的 B 都指出 ZFC-1 的问题（C-85、C-90、C-422 (1)；C-430）；重心在 A（C-420）；逐句对照第 3 节第 6–8 行",
    "KC-000079": "本代新增。两种现实（C-420、C-422；C-106–C-108、C-424）与思维中的悖论实例（C-423、C-424、C-430）；“必然”是论题，不是定理",
    "KC-000080": "本代新增。哥德尔一路：ZFC 在“会停”一侧完备、缺口全在“永不停”一侧（C-100、C-416、C-99），Z0（C-417、C-427）",
    "KC-000081": "本代新增。“矛盾”的意思，D5-3 作确认读；与 KC-000047 一致",
    "KC-000082": "本代新增。研究发起人对 KC-000067 的重述：同一个 Q 实指 A（D2-1）；与 D4 合流",
    "KC-000083": "本代新增。芝诺的两个问题与现实观；现实判断，离散侧数学对应物另有定理，身份不互冒",
}


def labels() -> dict[str, str]:
    text = (ROOT / CORE).read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^### (KC-\d{6}) · [^·]+? · [^·]+? · (.+)$", text, re.M):
        out[m.group(1)] = m.group(2).strip()
    return out


def audit_text() -> str:
    lab = labels()
    if len(lab) != 83 or list(lab)[-8:] != NEW_KCS:
        raise SystemExit("CORE_NOT_GENERATION_15")
    rows = []
    counts: dict[str, int] = {}
    for kc, label in lab.items():
        if kc in NEW_ROWS:
            relation, assess, nxt = "ALIGNED", NEW_ROWS[kc], "若有句子没有对上证明或被说成定理，以逐句对照与 CLAIM 为准改正"
        else:
            relation, assess, nxt = TOUCHED.get(kc, DEFAULT_ROW)
        counts[relation] = counts.get(relation, 0) + 1
        cell = lambda s: s.replace("|", "／")
        rows.append(f"| `{kc}` | {cell(label)} | {relation} | {cell(assess)} | {cell(nxt)} |")
    tally = "、".join(f"{k} {v}" for k, v in sorted(counts.items()))
    return "\n".join([
        f"# {SESSION_ID} 完整兼容审计",
        "",
        f"{GEN15}；83 KC。canonical writer 只授权新 session 目录第一层文件，所以本审计是单文件兼容 bundle。逐条立场由本会话写成（Claude Code 会话 91beaf35，012-Opus），计数不认证理解。",
        "",
        f"- core_change: YES_ADDITIVE_PRESERVING — {GEN14}/75 → {GEN15}/83；新增 KC-000076–KC-000083（研究发起人 10-14、10-15 的八个原文单元）；75/75 旧单元逐字节保留；本代起附字母演变登记表 `{REGISTRY}`（AI 整理，不是原文，哈希钉在 manifest）。",
        "- direction_change: NO — 研究方向（找到 ZFC-1=ZFC+A 的问题并机器证明）已由根 `CLAUDE.md` 第四节与形式化追踪承载；方向追踪的 ZFC 两行不变。",
        "- panorama_change: NO — 新证明（C-430、C-431）已登记在共享矩阵与 CG-001 证据索引。",
        f"- essay_change: NO — 新单元的 AI 阐释在 `{LINE_BY_LINE}` 与字母演变登记表中，本代不加扩展认知分片。",
        f"- update_decision: 按研究发起人 2026-10-15 批准的入核方案执行（`{RULINGS}`）；幽灵几句维持 10-08 的“不纳入”；工作指示不入核；10-15 的字母漂移原话引在登记表说明里，不另立条目；10-15 的收敛原话等研究发起人一句话再定。",
        "- cross_conflicts: KC-000067 与 KC-000082：研究发起人自己的重述，按登记表与逐句对照处理，原文不改；GLM 对 A 的几处读法过了头（稠密并进 A 等），更正见 CN-081 §3。" + HEAD_DRIFT_NOTE,
        "- unresolved: 10-15 收敛原话入不入核（研究发起人一句话）；扩展认知没有为新单元加分片；外部复核与文献查重没有发生。",
        "",
        f"关系计数：{tally}。",
        "",
        "|KC ID|姿态|relation|assessment and evidence|next and falsifier|",
        "|---|---|---|---|---|",
        *rows,
        "",
    ])


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "核心认知第 15 代入核（KC-000076–KC-000083：研究发起人 2026-10-14、10-15 的八个原文单元），并随代建立字母演变登记表。",
        "",
        "- host: Claude Code（桌面应用 Code 标签页，本机 macOS），会话 91beaf35-237d-4c5d-887c-cb72c58ccca2（由 95a1a81b 恢复），独立 worktree `/Volumes/D/HoTT-worktrees/012-opus-w8`，分支 `claude/012-opus-w8`",
        "- model: Claude Opus 5.5（claude-opus-5-5）",
        "- role: 执行者（研究发起人 2026-10-15 与 GLM 会话裁定后的移交清单 H4）；本 checkpoint 不交付新数学主张",
        f"- authorization: {AUTHORIZATION}",
        "- parent: Claude 线目标包 CG-010（`.claude/goals/CG-010-remaining-formalization-alignment/`）；不改变 STATE 执行控制中的其他字段",
        "",
        "## 做了什么",
        "",
        f"- 来源：`{SRC_CLAUDE}`（三条消息，取自会话记录，与 `dev-notes/0118` 第 10、11 轮逐字一致）、`{SRC_GLM}`（两条消息，取自 GLM 转录）。",
        f"- curation：`{CURATION}`，继承 v14，八个单元；`build_core_cognition.py` 加了可选的 `letter_registry`（钉哈希、写 manifest、核心文件头加一行指针；不声明时与原来逐字节相同，重建第 14 代核对过）。",
        f"- 构建：`--transition-from-ref {FROM_REF}`；`verify_core_cognition.py` PASS_WITH_SCOPE，映射 75、余数 0。",
        f"- 登记表：`{REGISTRY}`。逐句对照：`{LINE_BY_LINE}`。",
        "",
        "## 照实说",
        "",
        "- 方向追踪、全景视野、扩展认知、MEMORY 原样带上，没有改；根 `CLAUDE.md` 第一节要求最小化地走框架。",
        "- STATE.json 没有整体读入模型上下文；本事务只经脚本改 `revision`、`latest_session`、`current_core`、`execution_control` 的两个字段与两条新记录。",
        f"- {HEAD_DRIFT_NOTE}",
        "",
    ])


def runs_obj(snapshot: str) -> dict:
    return {
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "session_kind": "GOVERNANCE_CORE_GENERATION_AND_LETTER_REGISTRY",
        "checkpoint_result": RESULT_REL,
        "base_snapshot": snapshot,
        "formal_runs": [],
        "governance_runs": [
            {"tool": "scripts/audit/build_core_cognition.py",
             "command": f"--curation {CURATION} --transition-output {TRANSITION} --transition-from-ref {FROM_REF} --write",
             "status": "BUILT / COMPLETE_ADDITIVE_PRESERVING / mapping_count=75 / remainder=0", "generation": f"{GEN14}/75 -> {GEN15}/83"},
            {"tool": "scripts/audit/verify_core_cognition.py", "command": f"--curation {CURATION} --transition {TRANSITION}",
             "status": "PASS_WITH_SCOPE"},
            {"tool": "scripts/audit/test_core_cognition.py", "command": "", "status": "7 tests OK"},
            {"tool": PREPARE_SELF, "command": "repair_head()", "status": "HEAD.tracked rebuilt for the pre-existing drift of "
             "'MEMORY/001 - 当前执行队列.md' (CG-007 direct edits after revision 313); revision and latest_session unchanged"},
            {"tool": PREPARE_SELF, "command": "--output <payload>", "status": "PREPARED"},
            {"tool": ".codex/tools/cognition_runtime.py", "command": "checkpoint --snapshot <base_snapshot> --payload <payload> --apply",
             "status": "CHECKPOINT_COMMITTED expected; only the canonical result.json proves it"},
        ],
        "new_math_claims": [],
        "math_status_change": "NONE",
        "push_policy": "not pushed; dev integration and push only on the research sponsor's word",
        "note": "Core entry of the research sponsor's eight 10-14/10-15 units, with the letter-evolution registry pinned per generation.",
    }


def state_edits(state: dict) -> None:
    session_path = f"{SESSION_REL}/SESSION.md"
    state["revision"] = NEW_REVISION
    state["latest_session"] = SESSION_ID
    state["current_core"] = {
        "core_sha256": sha_file(CORE),
        "curation": CURATION,
        "curation_sha256": sha_file(CURATION),
        "generation": GEN15,
        "kc_count": 83,
        "manifest": MANIFEST,
        "manifest_sha256": sha_file(MANIFEST),
        "path": CORE,
        "transition": TRANSITION,
    }
    ec = state["execution_control"]
    ec["last_checkpoint_session"] = SESSION_ID
    ec["checkpoint_result"] = RESULT_REL
    core_sources = [CORE, MANIFEST, CURATION, TRANSITION, SRC_CLAUDE, SRC_GLM, REGISTRY,
                    "scripts/audit/build_core_cognition.py", "scripts/audit/verify_core_cognition.py"]
    state["records"][REC_CORE] = {
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / COMPLETE_ADDITIVE_PRESERVING",
        "full_sources": core_sources,
        "kind": "core_generation_migration",
        "lifecycle_status": "CURRENT",
        "path": TRANSITION,
        "related_records": [REC_PREV_CORE, SESSION_ID],
        "scope": ("Incrementally add eight exact direct-user units of 2026-10-14/15 (the definition of Q; the two choices and the definition of A; "
                  "ZFC-1 facing the Russell and HoTT paradoxes with its denial of reality lying in A; logic as an abstraction of reality and thought; "
                  "the link to Gödel incompleteness through non-halting; the meaning of 矛盾; the restatement that the 'same Q' is A; the reality view) "
                  "while preserving all 75 generation-14 KCs byte for byte, and pin the AI-curated letter-evolution registry per generation. "
                  f"Approved by the research sponsor on 2026-10-15. Supersedes {REC_PREV_CORE} as the owner of the current core identity."),
        "source_hashes": {p: sha_file(p) for p in core_sources},
        "status": "closed",
    }
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, f"{SESSION_REL}/RUNS.json", f"{SESSION_REL}/CORE_COGNITION_AUDIT.md", RESULT_REL, TRANSITION, CURATION, REGISTRY],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV_SESSION, REC_CORE],
        "scope": "Core generation-15 entry (KC-000076 to KC-000083) with the letter-evolution registry; executing session of the 2026-10-15 rulings (CG-010 H4); no new mathematics delivered through this checkpoint.",
        "source_hashes": {},
        "status": "complete",
    }


RESUME_ADD = (
    "### CG-010：核心认知第 15 代与字母演变登记表（2026-10-15）\n\n"
    f"研究发起人批准的第 15 代（KC-000076–KC-000083：10-14 的 Q 的定义、两次选择与 A、ZFC-1 与悖论、逻辑学与现实，10-14 深夜关于哥德尔的那句，“矛盾”那句，10-15 的“同一个 Q 实指 A”与现实观）已应用；字母演变登记表 `{REGISTRY}` 随代钉哈希。"
    f"研究发起人原话的逐句对照与机器证明见 `{LINE_BY_LINE}`；裁定档案 `{RULINGS}`。\n\n"
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    required = [CORE, MANIFEST, CURATION, TRANSITION, REGISTRY, SRC_CLAUDE, SRC_GLM, RULINGS, LINE_BY_LINE]
    missing = [p for p in required if not (ROOT / p).is_file()]
    if missing:
        raise SystemExit(f"EVIDENCE_MISSING:{missing}")
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != PREV_REVISION or state.get("latest_session") != PREV_SESSION:
        raise SystemExit(f"EXPECTED_REVISION_{PREV_REVISION}:{state.get('revision')}:{state.get('latest_session')}")
    for identity in (SESSION_ID, REC_CORE):
        if identity in state["records"]:
            raise SystemExit(f"RECORD_ALREADY_EXISTS:{identity}")
    drifted = repair_head()
    plan = R.plan(ROOT, profile="governance", _allow_core_transition=CORE_TRANSITION)
    texts: dict[str, str] = {path: (ROOT / path).read_text(encoding="utf-8") for path in R.MUTABLE}
    # the runtime requires every shard of a sharded MUTABLE document in the checkpoint; carried unchanged
    for shard in R.mutable_shard_paths(ROOT):
        texts.setdefault(shard, (ROOT / shard).read_text(encoding="utf-8"))
    resume_path = ".codex/research/hott/RESUME.md"
    marker = "# 接续指针\n"
    if texts[resume_path].count(marker) != 1:
        raise SystemExit("RESUME_MARKER")
    texts[resume_path] = texts[resume_path].replace(marker, marker + RESUME_ADD, 1)
    state_edits(state)
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[f"{SESSION_REL}/SESSION.md"] = session_text()
    texts[f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"] = audit_text()
    texts[f"{SESSION_REL}/RUNS.json"] = json.dumps(runs_obj(plan["snapshot"]), ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": AUTHORIZATION,
        "load_profile": "governance",
        "task_ids": [],
        "core_transition": CORE_TRANSITION,
        "files": [
            {"path": path, "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None, "text": value}
            for path, value in texts.items()
        ],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": NEW_REVISION, "session_id": SESSION_ID,
                      "files": len(texts), "head_drift_rebased": drifted}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
