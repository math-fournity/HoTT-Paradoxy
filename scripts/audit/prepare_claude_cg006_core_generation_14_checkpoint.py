#!/usr/bin/env python3
"""Prepare the CG-006 checkpoint: core generation-14 (KC-000063 to KC-000075), essay shard 013, and the
registration of the Gödel-Q results and the two-route target profile in the shared owners.

Scope (research sponsor, local Claude Code session d58e0c0d, 2026-10-07/08):

* full takeover authorization of 2026-10-07 (integrator role, shared owners included);
* approval of the generation-14 inclusion list on 2026-10-08 ("按清单应用，含 dev-01 #13"), with the
  ghost quotes of 09-19/09-27/10-01 excluded this time ("这次不纳入");
* the Targets-with-Profile request of 2026-10-08 (two routes: without/with Gödel; five directions).

The core was built on disk by scripts/audit/build_core_cognition.py with core-cognition-curation-v14.json;
this payload moves STATE.current_core to it through the runtime's canonical core_transition path.
Everything else is written in the same transaction: essay shard 013 and index baseline, two direction
rows and three cross-references, three panorama rows and one open item, MEMORY 001/002/003, RESUME,
STATE records, and the session bundle (SESSION.md, RUNS.json, single-file CORE_COGNITION_AUDIT.md).

The script only builds the payload; it writes nothing into the repository.  Apply it with
.codex/tools/cognition_runtime.py checkpoint --snapshot <printed snapshot> --payload <output> --apply
Modelled on scripts/audit/prepare_claude_core_generation_10_checkpoint.py.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SCRIPTS = ROOT / "scripts/audit"

SPEC = importlib.util.spec_from_file_location("runtime_claude14", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402

BSPEC = importlib.util.spec_from_file_location("builder_claude14", SCRIPTS / "build_core_cognition.py")
assert BSPEC and BSPEC.loader
B = importlib.util.module_from_spec(BSPEC)
BSPEC.loader.exec_module(B)

SESSION_ID = "S-GOV-20261008-CLAUDE-CG006-CORE-GENERATION-14"
PREV_SESSION = "S-RES-20261005-ZFC-META-SUBTHEORY-C0R9-R11-SOURCE-SCREENS-001"
PREV_REVISION = 312
NEW_REVISION = PREV_REVISION + 1
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"

CORE = "核心认知.md"
MANIFEST = "核心认知.manifest.json"
CURATION = "scripts/audit/core-cognition-curation-v14.json"
TRANSITION = "audit/core-cognition-generation-14-transition-20261008.json"
GEN13 = "core-cognition-generation-13"
GEN14 = "core-cognition-generation-14"
SRC14 = "sources/prompts/Codex-ZFC时间观察力与哥德尔路线十三条-用户原文-20261003至20261005.md"
PREPARE_SELF = "scripts/audit/prepare_claude_cg006_core_generation_14_checkpoint.py"

PKG = ".claude/goals/CG-006-zfc-complete-formalization"
TARGETS = f"{PKG}/Targets与Profile.md"
GUI_INDEX = f"{PKG}/GUI查阅索引.md"
BACKTRACE = f"{PKG}/tools/gui_backtrace.py"
ESSAY_TEMPLATE_DEFAULT = f"{PKG}/essay-013-template.md"
CN067 = ".claude/思考与发现/CN-067 - Z0 的最小可续形式状态：两条前提、一个负控制与还差的第三步.md"
CN068 = ".claude/思考与发现/CN-068 - 两条路线与线头：八线倒查后的五个方向.md"
REPORT = "docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md"
GQ = "HoTT/formal/claude-cg001/godel-q"
GQZ = "HoTT/formal/claude-cg001/godel-q-zfc"
GQZ0 = "HoTT/formal/claude-cg001/godel-q-zfc-z0"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
LEDGER = "HoTT/CLAIM_NAMESPACE_LEDGER.md"
CG001_INDEX = ".claude/goals/CG-001-targeted-overview/证据索引.md"
RUNS_DIR = "HoTT/verification/runs"
MAIN_RUNS = ["20261007-CG001-GODEL-Q-01", "20261008-CG001-GODEL-Q-ZFC-01", "20261008-CG001-GODEL-Q-ZFC-Z0-01"]
NEG_RUNS = ["20261007-CG001-GODEL-Q-NEG-SOUNDNESS-01", "20261007-CG001-GODEL-Q-NEG-CONSISTENCY-01",
            "20261007-CG001-GODEL-Q-NEG-EFFECTIVENESS-01", "20261007-CG001-GODEL-Q-NEG-GODEL-II-01",
            "20261008-CG001-GODEL-Q-ZFC-NEG-SOUNDNESS-01", "20261008-CG001-GODEL-Q-ZFC-NEG-DELTA1-01",
            "20261008-CG001-GODEL-Q-ZFC-NEG-CONSISTENCY-01", "20261008-CG001-GODEL-Q-ZFC-Z0-NEG-ISIGMA1-01"]
IMPORT_REPLAY = f"{PKG}/verification/20261008-S7C-IMPORT-REPLAY.json"

ESSAY_INDEX = "扩展认知.md"
ESSAY_012 = "扩展认知/012 - 后续理论靶、罗素模式 P 与工作意识.md"
ESSAY_005 = "扩展认知/005 - 表达界限、文章作为起点与编写说明.md"
ESSAY_013_TITLE = "ZFC 的时间观察力、Q／P／A／B 与哥德尔路线"
ESSAY_013 = f"扩展认知/013 - {ESSAY_013_TITLE}.md"
NEW_KCS = [f"KC-{n:06d}" for n in range(63, 76)]

CORE_TRANSITION = {"from_generation": GEN13, "to_generation": GEN14, "manifest": MANIFEST, "transition": TRANSITION}

REC_CORE = "A-CLAUDE-CORE-GENERATION-14-001"
REC_RESULT = "A-CLAUDE-GODEL-Q-ZFC-FORMAL-001"
REC_TARGETS = "R-CLAUDE-CG006-TARGETS-PROFILE-001"
REC_FOLLOW = "G-CLAUDE-CG006-FOLLOWUPS-001"
REC_PREV_CORE = "A-CODEX-CORE-GENERATION-13-001"

DIR_GODEL = "DIR-U-ZFC-GODEL-Q-OBSERVATION"
DIR_ROUTES = "DIR-U-ZFC-TWO-ROUTES"
OUT_GODEL = "OUT-U-ZFC-GODEL-Q-OBSERVATION-C84-C103"
OUT_IMPORT = "OUT-U-ZFC-BRANCH-IMPORTS-D01-D09"
OUT_TARGETS = "OUT-U-ZFC-TWO-ROUTES-TARGETS-PROFILE"

AUTHORIZATION = (
    "Research sponsor, local Claude Code session d58e0c0d. 2026-10-07: 这个repo全部的分支和git worktree，现在由你全面接手了，"
    "你就是‘最后的AI’，所以你认为应该做的，都可以做，我全面授权你。你要综合所有之前的AI的所有工作，推进到完全的形式化和机器证明的完成。"
    " 2026-10-08, answering the question how to handle the generation-14 inclusion list: 按清单应用，含 dev-01 #13 (Recommended); "
    "and on the ghost quotes of 09-19/09-27/10-01: 这次不纳入 (Recommended). 2026-10-08 Targets with Profile request: "
    "我觉得这个Targets with Profile的工作特别重要，因为它就是你未来工作的抓手。 The checkpoint applies the approved thirteen items "
    "(KC-000063 to KC-000075), writes essay shard 013, and registers the CG-005/006 results, the branch imports and the two-route "
    "target profile in the shared owners; no new mathematical claim is delivered through it."
)

PATH_PREFIXES = ("HoTT/", "docs/", ".claude/", "sources/", "scripts/", ".codex/", "扩展认知/", "方向追踪/", "全景视野/", "MEMORY/",
                 "audit/", "dev-notes/", "git-worktree对话录/")


def check_paths(label: str, text: str, extra_existing: frozenset[str] | set[str] = frozenset()) -> None:
    """Every backticked repository path in generated text must exist (or be created by this checkpoint)."""
    missing = []
    for match in re.finditer(r"`([^`\n]+)`", text):
        token = match.group(1).strip()
        if not token.startswith(PATH_PREFIXES) and token not in ("核心认知.md", "方向追踪.md", "全景视野.md", "扩展认知.md", "rulings.md", "最高指示-Claude版.md"):
            continue
        if "/" not in token and not token.endswith((".md", ".json", ".py", ".sh", ".agda", ".lean")):
            continue
        path = token if token.endswith(("/", ".md", ".json", ".py", ".sh", ".agda", ".lean")) else token.split("（")[0].strip()
        if any(c in path for c in "{<…*／") or (" " in path and not path.endswith((".md", ".json", ".py", ".sh", ".agda", ".lean"))):
            continue
        if path in extra_existing:
            continue
        if not (ROOT / path).exists():
            missing.append(token)
    if missing:
        raise SystemExit(f"PATH_CHECK_FAILED:{label}:{sorted(set(missing))}")


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:70]}:{text.count(old)}")
    return text.replace(old, new, 1)


def insert_before(text: str, anchor: str, block: str) -> str:
    if text.count(anchor) != 1:
        raise ValueError(f"ANCHOR_COUNT:{anchor[:70]}:{text.count(anchor)}")
    i = text.index(anchor)
    return text[:i] + block + text[i:]


def sha_file(rel: str) -> str:
    return R.sha((ROOT / rel).read_bytes())


def quote_block(kc: str, payload: str) -> str:
    body = "\n".join(("> " + line) if line else ">" for line in payload.split("\n"))
    return f"<!-- original:{kc}:begin -->\n{body}\n<!-- original:{kc}:end -->"


def verify_essay_originals(texts: dict[str, str], payloads: dict[str, str]) -> int:
    """Every `original:KC-…` block of the essay must equal the core payload byte for byte; every KC appears."""
    total = 0
    bad = []
    seen: dict[str, int] = {}
    for path, body in texts.items():
        if not path.startswith("扩展认知/"):
            continue
        for m in re.finditer(r"<!-- original:(KC-\d{6}):begin -->\n(.*?)\n<!-- original:\1:end -->", body, re.S):
            total += 1
            seen[m.group(1)] = seen.get(m.group(1), 0) + 1
            lines = []
            for line in m.group(2).split("\n"):
                lines.append(line[2:] if line.startswith("> ") else ("" if line in (">", "> ") else "!!" + line))
            if "\n".join(lines) != payloads[m.group(1)]:
                bad.append((path, m.group(1)))
    if bad:
        raise SystemExit(f"ESSAY_ORIGINAL_BLOCK_MISMATCH:{bad}")
    missing = sorted(set(payloads) - set(seen))
    if missing:
        raise SystemExit(f"ESSAY_ORIGINAL_BLOCK_MISSING:{missing}")
    return total


def core_payloads() -> dict[str, str]:
    return B.parse_core_payloads((ROOT / CORE).read_text(encoding="utf-8"))


# ----------------------------------------------------------------------------------------------
# essay
# ----------------------------------------------------------------------------------------------

def essay_shard_013(payloads: dict[str, str], template_path: Path) -> str:
    text = template_path.read_text(encoding="utf-8")
    for kc in NEW_KCS:
        placeholder = "{" + kc + "}"
        if text.count(placeholder) != 1:
            raise SystemExit(f"TEMPLATE_PLACEHOLDER:{kc}:{text.count(placeholder)}")
        text = text.replace(placeholder, quote_block(kc, payloads[kc]))
    if "{KC-" in text:
        raise SystemExit("TEMPLATE_PLACEHOLDER_LEFT")
    heading = re.search(r"(?m)^# (.+)$", text)
    if heading is None or heading.group(1).strip() != ESSAY_013_TITLE:
        raise SystemExit("ESSAY_013_TITLE_MISMATCH")
    return text if text.endswith("\n") else text + "\n"


def essay_edits(essay: dict, payloads: dict[str, str], template_path: Path) -> None:
    essay["shards"][ESSAY_013] = essay_shard_013(payloads, template_path)
    idx = essay["index_text"]
    idx = replace_once(idx, f"baseline: {GEN13}", f"baseline: {GEN14}")
    idx = replace_once(idx, "本文根据《核心认知.md》generation-13 的全部 62 段原文持续综合；第 012 片展开 2026-10-02 的七条后续理论方法论原文。",
                       "本文根据《核心认知.md》generation-14 的全部 75 段原文持续综合；第 012 片展开 2026-10-02 的七条后续理论方法论原文，"
                       "第 013 片展开 2026-10-03 至 10-05 的十三条 ZFC 与哥德尔路线原文。")
    idx = replace_once(idx, "本索引 + 下方 12 个分片", "本索引 + 下方 13 个分片")
    idx = replace_once(idx, f"last_shard: {ESSAY_012}", f"last_shard: {ESSAY_013}")
    row12_start = "| 012 | [后续理论靶、罗素模式 P 与工作意识]"
    lines = idx.split("\n")
    pos = [i for i, line in enumerate(lines) if line.startswith(row12_start)]
    if len(pos) != 1:
        raise SystemExit("ESSAY_INDEX_ROW_012")
    row13 = (f"| 013 | [{ESSAY_013_TITLE}](<{ESSAY_013}>) | 用户 2026-10-03 至 10-05 的十三条原文（KC-000063–KC-000075）："
             "从 H0 回看 ZFC（Q0（H0（Z0）））；圆环悖论的存在就是 ZFC 的问题；元理论精度就是维度；不是没有，只是不完备；"
             "Q／P／A／B 与 ZFC-1、魔鬼交易；bare ZFC；以 H0 为 B；哥德尔的神似与想法 T；是不是一直在外围 | current |")
    lines.insert(pos[0] + 1, row13)
    essay["index_text"] = "\n".join(lines)
    s5 = essay["shards"][ESSAY_005]
    s5 = replace_once(s5, "本轮第 012 片逐字展开 generation-12 的 KC-000056–KC-000061。当前全文基线是 generation-12，",
                      "第 012 片逐字展开 generation-12、13 的 KC-000056–KC-000062，第 013 片展开 generation-14 的 KC-000063–KC-000075。当前全文基线是 generation-14，")
    s5 = replace_once(s5, "当前基线：core-cognition-generation-13，62 个语义单元；第 012 片覆盖本轮新增 KC-000056–KC-000062。",
                      "当前基线：core-cognition-generation-14，75 个语义单元；第 012 片覆盖 KC-000056–KC-000062，第 013 片覆盖 2026-10-08 入核的 KC-000063–KC-000075。")
    essay["shards"][ESSAY_005] = s5


# ----------------------------------------------------------------------------------------------
# direction and panorama
# ----------------------------------------------------------------------------------------------

DIR_SHARD = "方向追踪/002 - 治理与用户方向.md"
PAN_003 = "全景视野/003 - 当前机器证明包与原生重放.md"
PAN_004 = "全景视野/004 - 距离综合与消费者审计.md"
PAN_008 = "全景视野/008 - 当前未完成.md"
SEMANTIC = "GODEL_Q_CORE_MACHINE_PROVED_ON_ZFC / R_WITHOUT_GODEL_OPEN / F053_C6_NOT_RELEASED"

DIR_ROW_GODEL = (
    f"| `{DIR_GODEL}` | 有哥德尔路线：bare ZFC 在时间维度上的观察力不完备——以 ZFC 自己的可证性为接受接口、以过程停机为原过程完成，"
    "在 Foundation 形式化的真实 𝗭𝗙𝗖 上机器证明“每一刻看得见、永远看不见”、ZFC+P 的二难与 Z0 的条件形式 | "
    "研究发起人 2026-10-04 的哥德尔方向（KC-000072–KC-000074）；2026-10-07 全面授权（CG-006）；2026-10-05、10-07 的两个方向（dev-notes 0115、0114）"
    " | `ACTIVE / CORE_MACHINE_PROVED_WITH_SCOPE (CG001-C-84–C-103) / Z0_CONDITIONAL_ON_TWO_PREMISES / SAME_Q_CROSS_KERNEL_ONLY / NO_BARE_ZFC_INCONSISTENCY_CLAIM` | "
    "`ZENO`、`RUSSELL`、`COMPUTATIONAL_LEGITIMACY`、`THEORY_ECONOMY` | "
    f"`{OUT_GODEL}` | "
    "先证 `𝗜𝚺₁ ⪯ Sh`（与 `models_R0` 同一模型路线），再证 `Sh.RE`，最后把“Sh 一致 ⟺ 𝗭𝗙𝗖 一致”搬进 𝗜𝚺₁；让芝诺、H0、Z0 进入单一内核；写出 P 的语义侧与 ω 完成规则的形式联系 | "
    f"`{GQ}/CLAIM.md`；`{GQZ}/CLAIM.md`；`{GQZ0}/CLAIM.md`；`{REPORT}`；`{TARGETS}` |"
)
DIR_ROW_ROUTES = (
    f"| `{DIR_ROUTES}` | 研究发起人要的两个结果及其综合：无哥德尔的思路（R-无）、有哥德尔的思路（R-有），再综合（R-合）。八条 GUI 线倒查合并为五个方向："
    "Ⅰ 模式 P 与锻刀；Ⅱ A 侧元理论—子理论充分性；Ⅲ Q/P/A/B 形式化；Ⅳ B 侧 H0→Z0；Ⅴ 理论精度 T（Ⅴa 观察精度，Ⅴb 哥德尔式自反） | "
    "研究发起人 2026-10-05“1、无哥德尔的思路。2、有哥德尔的思路。”；2026-10-07“方向分成了两个……能综合起来就是更好的”；2026-10-08 Targets with Profile 要求 | "
    "`ACTIVE / R_WITH_GODEL_CORE_DONE / R_WITHOUT_GODEL_NOT_DELIVERED / SYNTHESIS_OPEN / PROFILE_44_POINTS_19_DONE_19_PARTIAL_4_OPEN_2_REFRAMED` | "
    "`ZENO`、`RUSSELL`、`COMPUTATIONAL_LEGITIMACY`、`THEORY_ECONOMY`、`HOTT_OBJECT` | "
    f"`{OUT_TARGETS}`；`{OUT_GODEL}`；`{OUT_IMPORT}` | "
    "R-无 的交付形态待研究发起人选定：(a) 图灵路线（停机不可判定 + 永不停定理集可枚举 + 一致，不用对角点）；(b) T-OBS 路线（承接时间结构一面：稠密与离散）；"
    "(c) C6 路线（把元理论的审查责任写成精确性质）。无哥德尔各线即 `DIR-U-ZFC-META-SUBTHEORY-ADEQUACY`、`DIR-U-H0-Z0-FOUNDATION-ADEQUACY`、`DIR-U-BARE-ZFC-Q-PRECISION`，线头见 Targets 文件 §2、§5 | "
    f"`{TARGETS}`；`{GUI_INDEX}`；`git-worktree对话录/README.md` |"
)


def direction_edits(direction: dict) -> None:
    for old, new in (
        ("版本：`integrated-direction-portfolio/v1.21`", "版本：`integrated-direction-portfolio/v1.22`"),
        ("日期：2026-10-05", "日期：2026-10-08"),
        ("状态：`F053_CORE_ADEQUACY_ACTIVE / C6_NOT_RELEASED`", f"状态：`{SEMANTIC}`"),
        ("semantic_status: F053_CORE_ADEQUACY_ACTIVE / C6_NOT_RELEASED", f"semantic_status: {SEMANTIC}"),
        (f"source_state_revision: {PREV_REVISION - 1}", f"source_state_revision: {NEW_REVISION}"),
        ("projection_generation: 20261005-zfc-mss-final-receipts-311", f"projection_generation: 20261008-cg006-core-gen14-{NEW_REVISION}"),
    ):
        projection_edit.replace_in_index(direction, old, new)
    shard = direction["shards"][DIR_SHARD]
    shard = insert_before(shard, "| `DIR-U-H0-Z0-FOUNDATION-ADEQUACY` |", DIR_ROW_GODEL + "\n" + DIR_ROW_ROUTES + "\n")
    shard = replace_once(shard, "F-051 是独立、暂停的后续计划 |",
                         f"F-051 是独立、暂停的后续计划。2026-10-08：属无哥德尔路线的方向 Ⅳ；Z0 的哥德尔路线候选（ZFC 的矛盾搜索，C-103 条件形式）见 `{DIR_GODEL}` |")
    shard = replace_once(shard, "或用户指定新的 OriginDone。 |",
                         f"或用户指定新的 OriginDone。2026-10-08：属无哥德尔路线的方向 Ⅴa；R-无 的交付形态见 `{DIR_ROUTES}`。 |")
    shard = replace_once(shard, "and a bare-ZFC foundation bridge. |",
                         f"and a bare-ZFC foundation bridge. 2026-10-08：属无哥德尔路线的方向 Ⅱ；dev-01 分支的 C0–C6 判词（CORE_ADEQUACY_FAILURE_WITH_SCOPE，来源层）与本行的 C0R11 尚未合账，见 `{DIR_ROUTES}`。 |")
    direction["shards"][DIR_SHARD] = shard


PAN_ROW_GODEL = (
    f"| `{OUT_GODEL}` | 哥德尔式 Q 的三层证明包：`MP-CG001-GODEL-Q-001`（C-84–C-94，满足标准元性质的有效理论）；`MP-CG001-GODEL-Q-ZFC-001`"
    "（C-95–C-102，Foundation 的 𝗭𝗙𝗖：Δ1 公理表示、数字、永不停机句可枚举、𝗭𝗙𝗖 ⊳ 𝗥₀、Σ1/Δ0 完全、Σ1 可靠、过程形式含独立性、魔鬼交易、跑者与 𝗭𝗙𝗖 + A = 𝗭𝗙𝗖 + P）；"
    "`MP-CG001-GODEL-Q-ZFC-Z0-001`（C-103，算术影子 Sh 上的条件形式第二定理）；各有在预期处被拒的负控制 | "
    f"`{DIR_GODEL}`、`{DIR_ROUTES}`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | "
    "CG-005（2026-10-07）与 CG-006（2026-10-08），本机会话 d58e0c0d；研究发起人的哥德尔方向（KC-000072–KC-000074） | "
    "`MACHINE_PROVED_WITH_SCOPE / RUNS_REPLAYED_EXACT / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / VERSION_CLOSED_IN_DEV_GIT` | "
    "Lean 4.34.0 + Foundation@1fb01b72 + Mathlib 5ed29652，公理只有 propext、Classical.choice、Quot.sound；在真实 𝗭𝗙𝗖 上：存在永不停机的过程 d，𝗭𝗙𝗖 证明每个有限时刻“尚未停”，"
    "却证明不了“永不停”，也证明不了“停”；𝗭𝗙𝗖 + P（ω 完成规则）要么不可枚举、要么不一致；A_general ↔ Q 完备；Z0 在 `[Sh.RE] [𝗜𝚺₁ ⪯ Sh]` 下成立 | "
    "不推出 ZFC ⊢ ⊥，也不推出 bare ZFC 不一致；𝗭𝗙𝗖 一致与 Σ1 可靠是 Lean 元层（宇宙模型）事实，不是 ZFC 内部可证；“时间维度 = 过程的逐步运行”是解释桥，时空结构（稠密与离散）一面未承接；"
    "芝诺、H0、Z0 的“同一个 Q”只是跨内核图式对应（C-93）；Z0 还差两条前提与内部化；圆环只承接“两端逼近、复原确认不了”一面 | "
    f"`{GQ}/CLAIM.md`；`{GQZ}/CLAIM.md`；`{GQZ0}/CLAIM.md`；`{MATRIX}`（CG-005/006 两节与 S6 一节）；`{CG001_INDEX}` §24–§26；"
    f"`{RUNS_DIR}/{MAIN_RUNS[0]}/RUN.json`；`{RUNS_DIR}/{MAIN_RUNS[1]}/RUN.json`；`{RUNS_DIR}/{MAIN_RUNS[2]}/RUN.json` |"
)
PAN_ROW_IMPORT = (
    f"| `{OUT_IMPORT}` | 接手全部分支：撞号用分支前缀（D01、D02、D09）处理，`dev` 下一个共享编号 C-387；dev-01 的 `zfc-dense-quantized-motion`（D01-C-370）、"
    "`zfc-dense-quantized-contract`（D01-C-371）、`zfc-meta-subtheory-adequacy`（D01-C-369）与 dev-09 的 `cubical-godel-fragment`（D09-C-370–C-386）连同 23 个运行原样并入并本机重放；"
    "dev-02、dev-03/04、dev-09 的 Foundation 重放包留在分支并写明理由 | "
    f"`{DIR_ROUTES}`、`DIR-U-ZFC-META-SUBTHEORY-ADEQUACY`、`DIR-G-MATH-PROOF-DELIVERY-GATE` | CG-006 S7-c（`dev` 提交 4a3535d9） | "
    "`IMPORTED_BYTE_IDENTICAL / REPLAYED_WITH_SCOPE (13_LEAN_EXACT / 8_AGDA_PATH_NORMALIZED / 2_NO_COMMAND)` | "
    "并入的包与分支 blob 逐字节相同；13 个 Lean 运行逐字节重放一致，8 个 Agda 运行替换工作树路径后一致；稠密过程在任何有限阶段都不完成、量子化半步在第 4 步完成（D01-C-370、C-371） | "
    "GPT 分支的自述不是证据；D01-C-369 是条件性的应用充分性，不是 bare ZFC 定理；D09 的 CCTTmini 只到语法形状，没有对象层可证性表示；留在分支的包不等于被否定 | "
    f"`{LEDGER}`；`HoTT/formal/zfc-dense-quantized-motion/`；`HoTT/formal/zfc-dense-quantized-contract/`；`HoTT/formal/zfc-meta-subtheory-adequacy/`；`HoTT/formal/cubical-godel-fragment/`；`{IMPORT_REPLAY}` |"
)
PAN_ROW_TARGETS = (
    f"| `{OUT_TARGETS}` | Targets with Profile：八条 GUI 线从末轮倒查到分叉点（252 轮骨架），合并为五个方向；研究发起人要的“无哥德尔／有哥德尔”两个结果分为 R-无、R-有、R-合；"
    "44 个画像要点逐点对照：✅19、◐19、○4、⊘2 | "
    f"`{DIR_ROUTES}` | 研究发起人 2026-10-08 要求；2026-10-05、10-07 的两个方向 | `DOCUMENTED / TARGET_PROFILE_FROZEN_V1 / NO_MATH_CLAIM` | "
    "有哥德尔路线的核心已在真实 ZFC 上机器证明；无哥德尔各线卡在“原过程完成在 ZFC 语言之外”；GPT 的收敛 SOP 把两个结果写成同一判词位上的互斥值；"
    "两条路线承接“时间”的两个侧面（过程与可计算性；时空结构） | "
    "画像不是数学结论；GPT 的回答是自述；R-无 尚未交付；计数不认证理解 | "
    f"`{TARGETS}`；`{BACKTRACE}`；`{CN068}` |"
)
PAN_ITEM_21 = (
    f"21. `{REC_FOLLOW}`：CG-006 之后仍开放——R-无 的交付形态待研究发起人选定（图灵路线、T-OBS、C6）；Z0 的两条前提与内部化；同一个 Q 进入单一内核；"
    "P 的语义侧与 ω 完成规则的形式联系；圆环的完整结构；想法 T 的一般形式；以已知答案校准模式 P（需研究发起人决定是否重启 P-DAG 节点）；"
    "“社区实际采用 A”“ZFC 放过 HoTT”从来源层到形式层；时间结构一面（稠密与离散）。逐点见 "
    f"`{TARGETS}` §5–§7。\n"
)


def panorama_edits(panorama: dict) -> None:
    for old, new in (
        ("版本：`integrated-outcome-panorama/v1.22`", "版本：`integrated-outcome-panorama/v1.23`"),
        ("日期：2026-10-05", "日期：2026-10-08"),
        ("状态：`F053_CORE_ADEQUACY_ACTIVE / C6_NOT_RELEASED`", f"状态：`{SEMANTIC}`"),
        ("semantic_status: F053_CORE_ADEQUACY_ACTIVE / C6_NOT_RELEASED", f"semantic_status: {SEMANTIC}"),
        (f"source_state_revision: {PREV_REVISION - 1}", f"source_state_revision: {NEW_REVISION}"),
        ("projection_generation: 20261005-zfc-mss-final-receipts-311", f"projection_generation: 20261008-cg006-core-gen14-{NEW_REVISION}"),
        ("两个原生重放 |", "两个原生重放 + ZFC 哥德尔式 Q（C-84–C-103）与 D01/D09 并入 |"),
        ("| C5/N1/N2/N4/N5/N7/N10/S053/S055/N11 + E6 定向搜索/派生扫描/unimath E6 扫描/nocanonical 尝试 |",
         "| C5/N1/N2/N4/N5/N7/N10/S053/S055/N11 + E6 定向搜索/派生扫描/unimath E6 扫描/nocanonical 尝试 + CG-006 两条路线目标画像 |"),
    ):
        projection_edit.replace_in_index(panorama, old, new)
    s3 = panorama["shards"][PAN_003]
    s3 = insert_before(s3, "| `OUT-U-BARE-ZFC-Q-PRECISION-C364` |", PAN_ROW_GODEL + "\n" + PAN_ROW_IMPORT + "\n")
    panorama["shards"][PAN_003] = s3
    s4 = panorama["shards"][PAN_004]
    if not s4.endswith("\n"):
        s4 += "\n"
    panorama["shards"][PAN_004] = s4 + PAN_ROW_TARGETS + "\n"
    s8 = panorama["shards"][PAN_008]
    if not s8.endswith("\n"):
        s8 += "\n"
    panorama["shards"][PAN_008] = s8 + PAN_ITEM_21


# ----------------------------------------------------------------------------------------------
# MEMORY and RESUME
# ----------------------------------------------------------------------------------------------

M1 = "MEMORY/001 - 当前执行队列.md"
M2 = "MEMORY/002 - 当前证据上限与恢复入口.md"
M3 = "MEMORY/003 - 当前验证状态与顺序日志.md"
M1_STRAY_START = "<!-- governance-shard:v2\n"
M1_STRAY_END = "logical_id: MEMORY"
M1_TOP = (
    "## 当前最高优先：两条路线的形式化与综合（CG-006，2026-10-08）\n\n"
    "研究发起人 2026-10-07 全面授权（“这个repo全部的分支和git worktree，现在由你全面接手了，你就是‘最后的AI’……你要综合所有之前的AI的所有工作，推进到完全的形式化和机器证明的完成。”），"
    "并在 2026-10-05、10-07 说明要两个结果：无哥德尔的思路与有哥德尔的思路，最好能综合。现状：\n\n"
    f"- 有哥德尔路线的核心已在 Foundation 形式化的真实 𝗭𝗙𝗖 上机器证明（CG001-C-84–C-103；`{DIR_GODEL}`）；Z0 只到条件形式（C-103），下一步先证 `𝗜𝚺₁ ⪯ Sh`。\n"
    f"- 无哥德尔路线尚未单独交付（`{DIR_ROUTES}`）；交付形态（图灵路线、T-OBS、C6）待研究发起人选定。\n"
    "- 下面 F-053 一节作为无哥德尔路线的方向 Ⅱ 并行保留；dev-01 分支的 C0–C6 判词与主干的 C0R11 尚未合账。\n"
    f"- 线头与逐点对照：`{TARGETS}`；跟进记录 `{REC_FOLLOW}`；Claude 线目标包 `{PKG}/`。\n\n"
)
M1_F053_OLD = "## 当前最高优先：ZFC 元理论—子理论核心充分性最终闭环（2026-10-04）"
M1_F053_NEW = "## 并行活跃：ZFC 元理论—子理论核心充分性最终闭环（2026-10-04；无哥德尔路线的方向 Ⅱ）"
M2_BULLET = (
    "- 哥德尔式 Q 的机器证据上限（2026-10-08）：在 Foundation 形式化的真实 𝗭𝗙𝗖 上，“每一刻看得见、永远看不见”、𝗭𝗙𝗖 + P 的二难、A_general ↔ Q 完备与 Z0 的条件形式，"
    "已由 Lean 4.34.0 内核检查并精确重放（CG001-C-84–C-103）；𝗭𝗙𝗖 一致与 Σ1 可靠是 Lean 元层事实；没有证明 ZFC ⊢ ⊥；同一个 Q 只到跨内核图式；无哥德尔路线还没有关于 bare ZFC 的形式结果。\n"
)
M2_RECOVERY = (
    f"ZFC 两条路线（CG-006）的恢复：先读 `{TARGETS}` 与 `{GUI_INDEX}`，再 query `{REC_RESULT}`、`{REC_FOLLOW}`；Claude 线按 goal-x 的 CG-006 闭包恢复。\n\n"
)
MEMORY_003_ADD = (
    f"\n{SESSION_ID}：核心认知第 14 代（{GEN13}/62 → {GEN14}/75；新增 KC-000063–KC-000075，研究发起人 2026-10-03 至 10-05 的十三条 ZFC 原文；"
    "62/62 `PRESERVED_EXACT`、remainder=0）；扩展认知新增第 013 片；方向追踪新增 "
    f"`{DIR_GODEL}`、`{DIR_ROUTES}`，全景视野登记 CG001-C-84–C-103、D01/D09 并入与 Targets 画像；MEMORY/001 当前最高优先改为两条路线，"
    "并把首行分片注释中混入的 C0R9–C0R11 段落移回正文；STATE 登记核心代、形式结果、Targets 综合、跟进项与本 session。"
    f"revision {PREV_REVISION}→{NEW_REVISION}。无新数学主张经本 checkpoint 交付（CG001-C-84–C-103 已在共享矩阵）。\n"
)
RESUME_ADD = (
    "### CG-006：核心认知第 14 代与两条路线（2026-10-08）\n\n"
    f"研究发起人批准的第 14 代（KC-000063–KC-000075）已应用，扩展认知新增第 013 片。有哥德尔路线的核心已在真实 𝗭𝗙𝗖 上机器证明（`{REC_RESULT}`）；"
    f"无哥德尔路线的交付形态待研究发起人选定（`{REC_FOLLOW}`）。恢复时先读 `{TARGETS}`；Claude 线的目标包是 CG-006（goal-x）。\n\n"
)


def memory_edits(memory: dict) -> None:
    s1 = memory["shards"][M1]
    a = s1.index(M1_STRAY_START) + len(M1_STRAY_START)
    b = s1.index(M1_STRAY_END)
    stray = s1[a:b]
    if not stray.startswith("### `C0R9`") or s1.count(stray) != 1:
        raise SystemExit("MEMORY_001_STRAY_BLOCK_UNEXPECTED")
    s1 = s1[:a] + s1[b:]
    s1 = insert_before(s1, "### `Q_norm` 规范性 extension（2026-10-05）", stray)
    s1 = insert_before(s1, M1_F053_OLD, M1_TOP)
    s1 = replace_once(s1, M1_F053_OLD, M1_F053_NEW)
    memory["shards"][M1] = s1
    s2 = memory["shards"][M2]
    s2 = insert_before(s2, "\n## 恢复入口", "" if s2.split("\n## 恢复入口")[0].endswith("\n") else "\n")
    s2 = replace_once(s2, "\n## 恢复入口\n\n", "\n" + M2_BULLET + "\n## 恢复入口\n\n" + M2_RECOVERY)
    memory["shards"][M2] = s2
    s3 = memory["shards"][M3]
    if not s3.endswith("\n"):
        s3 += "\n"
    memory["shards"][M3] = s3 + MEMORY_003_ADD


# ----------------------------------------------------------------------------------------------
# audit
# ----------------------------------------------------------------------------------------------

E13 = "扩展认知 013"
TP = "Targets 文件"
NT = "本单元（核心认知第 14 代入核、扩展认知 013、CG-005/006 结果与 Targets 画像的登记）没有重新判断该条所指的内容；原文身份保留。"

AUDIT: dict[int, tuple[str, str, str, str]] = {
    1: ("HoTT悖论研究三问", "NOT_TOUCHED", NT, "若要给 ZFC 两条路线写一页人话短稿，按三问检查；答不出其中一问时回源本条"),
    2: ("Theory Schema先行", "NOT_TOUCHED", NT, "若 R-无 需要固定 bare ZFC 的观察接口，回源本条，先定位规则再造过程"),
    3: ("合取前提与稠密过程", "ALIGNED",
        f"有哥德尔路线只承接“过程与可计算性”一面；本条的稠密性一面在 {TP} §4 第 4 点与 §6 第 9 条被单独列为未承接，D01-C-370、C-371（稠密与量子化）是唯一触到它的形式材料",
        "若有人把哥德尔式 Q 读成对稠密性的回答，判收窄；R-无 的 T-OBS 路线是回到本条的入口"),
    4: ("悖论作为反证与运动前提", "ALIGNED",
        f"魔鬼交易定理就是本条“结论出现矛盾，必然是前提出现了错误”的形式：矛盾落在 𝗭𝗙𝗖 + P 上，必要性控制排除其他前提（CG001-C-90、C-101；{E13}“Q、P、A、B 与 ZFC-1”）",
        "若出现证据表明矛盾可推给有限可查性或一致性以外的其他前提，回源重审"),
    5: ("先找悖论后作最终归因", "CORRECTED",
        f"按 KC-000049 的修正，本单元在现象之后直接展开归因（终局报告的归因节；{TP} §4；CN-068 §3）；本条原话保留",
        "若再以“下一个故事”推迟已有现象的归因，判偏航"),
    6: ("时间机制不能收窄为稠密性", "ALIGNED",
        f"{TP} 与 {E13} 都把时间的两个侧面并列（过程与可计算性；时空结构），不把 ZFC 的问题收窄成任一面",
        "若后续叙述只剩其中一面，判收窄"),
    7: ("LLM内在知识与模式匹配", "ALIGNED",
        f"Q0（H0（Z0））的配对是一次模式匹配：H0 的逐层追问对上 ZFC 的矛盾搜索；写明这是 AI 的配对与判断（{E13} 第一节）",
        "若配对被当作证明，或 Z0 的条件形式被说成已完成，判越界"),
    8: ("历史时间悖论作为HoTT启发", "ALIGNED",
        "芝诺、圆环作为历史时间悖论给出 ZFC 一侧的靶（KC-000064），跑者把芝诺写成过程（CG001-C-91、C-101）",
        "若把芝诺的具体机制直接移植为 ZFC 的前提而不经过程，判偏航"),
    9: ("定位HoTT理论设定的时间维度", "NOT_TOUCHED", NT, "若要把同一个 Q 落进 HoTT 的单一内核，回源本条"),
    10: ("目标是现实相对非现实性而非内部矛盾", "ALIGNED",
         "原过程完成取停机，依据正是本条“时间相关的悖论，往往结果就是以不可计算性/不可停机性作为特征”；判词不是 ZFC 内部矛盾（CG001-C-99、C-100）",
         "若有人据此宣称 ZFC 不一致，判越界"),
    11: ("理论推演排除时序与程序显式时序", "ALIGNED",
         "ZFC 能谈论步骤与序列，却不承担“永远”的观察：每一刻看得见、永远看不见（CG001-C-99），正是本条“标的里可以有时间变量，思考过程不想让时序参与”的一个可证形状",
         "若出现 ZFC 在原生规则中承担了“永远”的观察（证明全部真的永不停句），本对位撤回"),
    12: ("ASK计算合法性预分析", "ALIGNED",
         "P（每一刻都没停就宣布永远不停）就是绕过 ASK、凭完成的整体宣布结局；一致的 P 不可计算（CG001-C-90）",
         "若 P 被读成合法的有限检查，判混淆"),
    13: ("ASK深化与理论工具性异化", "ALIGNED",
         f"P 换来的是 A 型便利（把极限理论当作解决芝诺式问题的一般方法），代价是可机械执行或一致（{E13}“魔鬼交易”一段；CG001-C-94）",
         "若找不到 P 带来的便利，这一对位撤回"),
    14: ("双向目标的第二方向", "DEEPENED",
         "P 正是第二种：现实里不能完成的无穷检查，被 𝗭𝗙𝗖 + P 当作已完成；而跑者是第一种的形状：跑者确实到达，ZFC 却确认不了（CG001-C-90、C-101）",
         "若用户认为这两处对位不合其两类划分，按用户裁定改写"),
    15: ("抽象即否定现实前提与Z铁律", "ALIGNED",
         "魔鬼交易以反证形式找到被否定的前提 P；哥德尔、Kleene、Turing 的数学是经典结果，新的是读法与综合（终局报告；CLAIM 的禁止外推）",
         "若文献查重发现同一读法已被提出，保留事实，改写新颖性的表述"),
    16: ("Russell的构造过程与计算合法性", "ALIGNED",
         "罗素的计算内核在本单元读作对角过程：“只要理论接受了‘d 永远不停’，d 就停下”（CG001-C-85、C-99）；Z0 是 ZFC 的矛盾搜索",
         "若用户认为“罗素的计算内核”不是对角过程，按用户裁定改写这一读法"),
    17: ("训练先验批判与Thinking in my math philosophy", "ALIGNED",
         f"“两个方向”按用户自己的话（0115、0114）取，而不按 GPT 收敛 SOP 的判词结构取（{TP} §1）；教科书消解（极限）列为要回答的一行",
         "若回答出现“极限理论早就解决了芝诺，所以没有问题”的推断，判偏航"),
    18: ("Z铁律的理论工具性与时间否定", "ALIGNED",
         "Z 铁律“T 变为非 T，结论 C 变为非 C”在本单元的读法：T = 只凭有限证明宣布事实，非 T = 加上 ω 完成规则 P，C 由“一致而有效”变为“不可枚举或不一致”（CG001-C-90）",
         "若改变 T 不改变 C，这一读法撤回"),
    19: ("合取真值与稠密空间中的完成困难", "ALIGNED",
         "魔鬼交易是四者的合取：有限可查、核实有限事实、不说假话、P；保留前三者，矛盾落在 P 上；本条的稠密性一面未承接（同 KC-000003）",
         "若出现去掉 P 仍有矛盾的构造，合取结构重审"),
    20: ("悖论反证、运动量子化与HoTT时间怀疑", "CORRECTED",
         "同 KC-000005：其中“下一个故事”一句的工作次序效力已由 KC-000049 修正；运动量子化只在 D01-C-370 的量子化半步中作为对照出现",
         "同 KC-000005"),
    21: ("机器证明与真实运行要求", "ALIGNED",
         "CG001-C-84–C-103 都有源码、运行收据与精确重放；分支并入的 23 个运行在本机重放（`HoTT/CLAIM_NAMESPACE_LEDGER.md`）",
         "若共享矩阵或收据被发现不一致，先修收据，不改判词"),
    22: ("两类现实相对悖论", "DEEPENED",
         "两类都出现在哥德尔式 Q 中：跑者确实到达而 ZFC 确认不了（第一类形状），𝗭𝗙𝗖 + P 把不能完成的无穷检查当作已完成（第二类）（CG001-C-90、C-101）",
         "若用户确认两类划分不应这样套用，按用户裁定改写"),
    23: ("时间时序处理应可直接定位", "ALIGNED",
         "ZFC 对时间的处理被定位到一处：理论的定理集只承担有限阶段的观察，不承担“永远”（CG001-C-99、C-100）；本条点名的“ZFC 本身试图以无时序的思维，绕过 ASK”由 P 的二难承接",
         "若有人说这只是一般的停机问题、与 ZFC 无关，见归因：论点是 bare ZFC 不能豁免"),
    24: ("两类时序悖论与HoTT搜索问题", "DEEPENED",
         "本条“悖论们……给自己制造了哥德尔不完备性，也就是在计算理论角度看，是不可停机的问题”在 bare ZFC 上得到一个机器证明的实例；不完备的核心不必依赖自指句（CN-068 §4）",
         "若把这一实例读成“只有 ZFC 有”，判越界；哥德尔现象属于一切足够强的有效理论"),
    25: ("自指型悖论为何难找", "ALIGNED",
         "自指在本单元是构造出来的：对角点由 Kleene 递归定理构造，而不是写进前提（CG001-C-85）",
         "若对角点被写成前提，判形似"),
    26: ("HoTT自身自指不可越过的怀疑", "NOT_TOUCHED", NT, "若把 Z0 的结论搬回 HoTT 的自我验证，回源本条与 KC-000028"),
    27: ("HoTT对齐程序后继承程序自反界限", "ALIGNED",
         "Z0 与 H0 逐字段同形：程序的哥德尔不完备在两边都出现；差别在 HoTT 能证明自己的追问永不停，ZFC 证明不了自己的矛盾搜索永不停（终局报告；CG-005 设计 §3）",
         "若有人把这说成 HoTT 或 ZFC 独有，判越界"),
    28: ("HoTT自反真理验证的不可停机与自馈回环怀疑", "ALIGNED",
         "ZFC 一侧的对应：ZFC 对自身一致性的确认是一条不停的搜索，ZFC 自己证明不了它不停（C-103 的条件形式）",
         "若条件形式的两条前提被证伪，这一对应改写"),
    29: ("理论经济收益作为自馈回环的高风险位置", "ALIGNED",
         "P 恰出现在理论想要经济收益的地方：用“完成的整体”替代逐步的检查（CG001-C-90、C-94）",
         "若证据显示 P 不带来任何经济收益，这一对位撤回"),
    30: ("历史理论经济认知完整性与HoTT经济学之问", "NOT_TOUCHED", NT, "若要回答 ZFC 追求怎样的理论经济学，以 P 的对位为材料回源"),
    31: ("HoTT严格范型可能拒绝最小理想理论的构造方向", "NOT_TOUCHED", NT, "若构造最小理想理论，回源本条"),
    32: ("悖论反证理论与稠密性否定所引入的存在性", "NOT_TOUCHED", NT, "若讨论 P 引入的是存在性还是不存在性，回源本条与 KC-000034"),
    33: ("Russell悖论对无时序不存在性前提的攻击", "NOT_TOUCHED", NT, "若罗素线的 B 向读法与 ZFC 的 P 并论，回源本条"),
    34: ("否定性存在与不存在的现实相对双视角", "NOT_TOUCHED", NT, "同 KC-000032"),
    35: ("HoTT能否完整表达用户悖论研究理论", "NOT_TOUCHED", NT, "若问 Lean 或 HoTT 能否表达想法 T 本身，回源本条"),
    36: ("HoTT研究哥德尔不完备性时的循环与自馈风险", "ALIGNED",
         "本单元用 Lean（带宇宙）研究 ZFC 的不完备：元理论更强，没有陷入循环；“用一个理论研究不完备”与“理论对自身作完备担保”分开写（扩展认知 004；KC-000072 的回答）",
         "若有人把 Lean 元层的证明说成 ZFC 内部可证，判越界"),
    37: ("圆环悖论由用户一眼发明", "ALIGNED",
         "用户一眼指出“圆环悖论的存在，就是 ZFC 的问题”（KC-000064），与本条的发现姿态相接",
         "若把圆环原案简化成“复原确认不了”一面而当作完整承接，判精化冒充原问"),
    38: ("捕捉HoTT作者思路缺陷原是很基础的工作", "NOT_TOUCHED", NT, "若论证 ZFC 的缺口在“基础之处”，回源本条与 KC-000039"),
    39: ("机器统观久未发现HoTT悖论的困惑", "NOT_TOUCHED", NT, "同 KC-000038"),
    40: ("第三条发现路径：反观训练数据中的HoTT知识谱", "NOT_TOUCHED", NT, "若以训练知识中的哥德尔定理作论证主轴，回源本条：知识谱是被考察对象，不是判断权威"),
    41: ("AI数学的两件事", "NOT_TOUCHED", NT, "若评估 GPT 各线为何停在外围，回源本条与 KC-000043"),
    42: ("助力有多大，阻力就有多大", "NOT_TOUCHED", NT, "同 KC-000041"),
    43: ("一体两面：认知惯性与路径依赖", "ALIGNED",
         f"GPT 各线反复要求外部来源付桥、反复判“形式目标未定义”，是一种路径依赖；{TP} §4 写明这是卡点，不是结论",
         "若把这一判断写成对 GPT 能力的定量结论，判加码"),
    44: ("理论是对现实的骨架式模仿", "NOT_TOUCHED", NT, "向外人解释“ZFC 每一刻看得见、永远看不见”时，若说出“ZFC 与现实无关”，判偏航"),
    45: ("数学与HoTT必然可映射现实", "ALIGNED",
         "原过程完成取停机，是一种现实对齐：一个逐步运行的过程停不停下，是现实问题",
         "若外行读者读不懂跑者的故事，现实对齐尚未完成"),
    46: ("AI缺的是用现实理解理论的动作", "ALIGNED",
         "本条“是否可以用基于 HoTT 框架的代码来构造不可停机的程序，就是一个现实问题”，在 ZFC 一侧对应为：ZFC 的矛盾搜索停不停，是现实问题",
         "若回答退回“ZFC 与过程无关”，判偏航"),
    47: ("经济性与普适性的理想抽象与反证", "ALIGNED",
         f"P 在本单元被定位为设计者为经济性与工具性作出的前提，按反证回溯得到（{E13}；CG001-C-90）",
         "若用户裁定 P 不是非现实抽象，归因改写"),
    48: ("针对可疑理论前提设计悖论过程", "ALIGNED",
         "过程专门碰靶前提：对角过程只在理论接受“永不停”时停下；负控制每次只去掉一个前提（CLAIM §5）",
         "若某个控制同时改了多处，敏感性结论降级"),
    49: ("归因是要与用户仔细探讨的正题", "ALIGNED",
         "归因直接展开：候选前提（P、有限可查性、一致性、经典二值性、实无穷）、竞争归因、区分证据与带身份的判断（终局报告的归因节；CN-068 §3）",
         "若归因被推迟，或只给唯一被告而没有竞争归因，判偏航"),
    50: ("论域元素的存在性是理论无法拒绝的问题（P1–P3）", "ALIGNED",
         "ZFC 一侧的类比：“ZFC 一致”即存在一个模型；对它的追问在 ZFC 内部是一条不停的搜索（C-103 的条件形式）。这是类比，不是同一",
         "若用户认为这一类比不合原意，撤回"),
    51: ("算符先于存在性落定（罗素线第二批）", "NOT_TOUCHED", NT, "若把“算符先于存在性落定”搬到 ZFC 的 P 上，回源本条"),
    52: ("四句证据链就是非现实性悖论", "NOT_TOUCHED", NT, "若把 Z0 与罗素线的四句证据链并论，回源本条"),
    53: ("项目目标不加“存在性”限定", "NOT_TOUCHED", NT, "同 KC-000052"),
    54: ("UR 与芝诺的模式匹配", "ALIGNED",
         "Z0 的 UR：“检查自己会不会自相矛盾本来是很简单的事——一直查下去就行——甚至在 ZFC 中都做不到”（终局报告；CG-005 综合报告 §3）",
         "若研究发起人一眼判定这不算 UR，撤回这一读法"),
    55: ("芝诺悖论的幽灵：圆环悖论", "ALIGNED",
         "KC-000064 把圆环悖论的存在指为 ZFC 的问题；跑者的 `Restores` 只承接“两端逼近、复原确认不了”一面",
         "若把这一面当作圆环的完整承接，判精化冒充原问"),
    56: ("后续靶须是支撑数学大厦的基础理论", "ALIGNED",
         "靶是 ZFC：实数与极限所依托的基础理论（KC-000064、KC-000065）",
         "若后续工作滑向某个具体定理而非理论承诺，判偏航"),
    57: ("菲尔兹奖入口不是硬门", "NOT_TOUCHED", NT, "无"),
    58: ("以模型已有数学知识启发式挖掘 ZFC 问题", "ALIGNED",
         "哥德尔的元思维是已有知识；它在这里被用作启发，判词由机器证明与来源检验，不由知识本身担保",
         "若把训练知识当作证据，判越界"),
    59: ("先刻画罗素模式 P，再审视 ZFC", "DEEPENED",
         "本条“ZFC 最大的问题，肯定在于对时间维度的把握上”在 bare ZFC 上得到一个可证形状：观察力在“永远”上不完备（CG001-C-99、C-100）",
         "若后续证据显示 ZFC 的问题另在他处，回源重审"),
    60: ("正确起点是极其明显的核心理论承诺", "ALIGNED",
         "起点是明显的：ZFC 支撑的极限与实数（圆环、芝诺），以及 ZFC 自己的可证性",
         "若起点改成到处搜索，判偏航"),
    61: ("后续理念性指导应完整进入核心认知", "ALIGNED",
         "本单元把 10-03 至 10-05 的十三条入核，并写扩展认知 013，使其每次被加载",
         "若入核文字与来源不一致，按来源修正并重建"),
    62: ("模式 P 写对后一遍匹配线索", "TENSION",
         f"P-FORGE 的三把刀与 P-DAG 没有一遍定位出 ZFC 的 Q（主干 #72–#73 自述 ZFC_Q_NOT_LOCATED）；圆环起点与哥德尔路线都来自研究发起人的提示（{TP} Ⅰ-1）。这不反驳本条：本条的条件是“P 写对”",
         "以已知答案（Z0 = 矛盾搜索；圆环 = 极限交付的完成）盲测 P；若 P 能一遍匹配到它们，张力解除"),
    63: ("Z0、H0 与 Q0", "DEEPENED",
         f"Z0 的候选 = ZFC 对自身矛盾的逐步搜索，与 H0 逐字段同形；对真实 ZFC 只到条件形式（C-103）；R_i ↔ Z_i 的文献线头本单元没有追（{E13} 第一节）",
         "若 Z0 的两条前提之一被证伪，或研究发起人认为 Z0 应是别的对象，改写"),
    64: ("圆环悖论的存在就是 ZFC 的问题", "DEEPENED",
         f"跑者与 `Restores` 承接“两端逼近、复原确认不了”一面（CG001-C-91、C-101）；零大小的点、反向逼近、此前已得到 M 未承接（{TP} Ⅱ-1）",
         "圆环的完整任务合同写出后，若跑者承接不了其核心，降级这一读法"),
    65: ("ZFC 作为 Meta Theory 理论精度不够", "DEEPENED",
         f"“元理论在可计算性观察上的判断力不够”得到精确形式：ZFC 能证明每个有限阶段事实，不能证明全部“永不停”，因此不能审定“极限交付完成”这一一般方法（CG001-C-99–C-101）；元理论的审查责任本身尚未形式化（{TP} Ⅱ-4）",
         "若 C6 路线把审查责任写成精确性质后 ZFC 满足它，这一读法改写"),
    66: ("判词候选：不是没有，只是不完备", "ALIGNED",
         f"“每一刻看得见、永远看不见”即本条的过程形式（CG001-C-99、C-100；{E13}“不是没有，只是不完备”）",
         "若出现 ZFC 证明全部真的永不停句的证据（即 ZFC 不一致或不可靠），本对位失效"),
    67: ("同一个 Q 在 ZFC 中产生矛盾", "DEEPENED",
         "精确回答：矛盾不在 bare ZFC 之内，落在 𝗭𝗙𝗖 + P 之中（CG001-C-90、C-101）；“同一个 Q”目前是跨内核图式（C-93）",
         "若同一个 Q 在单一内核中被证明不成立，改写"),
    68: ("Q／P／A／B 与 ZFC-1 的完整研究假说", "DEEPENED",
         f"证明论一面已支付：P 读作 ω 完成规则；一致的 P 不可计算；A_general ↔ Q 完备；一致有效的理论没有 A_general（CG001-C-90、C-94、C-101）。P 的语义一面、社区实际采用 A 仍开放（{TP} G-3、G-4）",
         "若 P 的语义一面与 ω 规则的联系被证明不成立，降级读法"),
    69: ("与魔鬼的交易：代价是数学真理性", "ALIGNED",
         f"四者不可兼得的定理即故事的形式（CG001-C-90）；“灵魂”是比喻，“数学真理性”读作一致与可靠是解释（{E13}）",
         "若研究发起人不同意把真理性读作一致与可靠，改写解释，不改定理"),
    70: ("我一直说的都是 bare ZFC 理论精度不够", "ALIGNED",
         "目标对象因此落在 Foundation 形式化的真实 𝗭𝗙𝗖 上，不是命题变量叫 ZFC 的夹具；审的是精度，不是一致性",
         "若有人把结论读成 ZFC ⊢ ⊥，判越界"),
    71: ("要找的就是 main 上 HoTT 的那件事", "ALIGNED",
         "H0 固定为 B（CG001-C-78）；Z0 是 ZFC 中与之同形的原生过程",
         "若 H0 的形式结果被撤回，B 侧改写"),
    72: ("形式化能否证明超越 ZFC 本身可证的东西；哥德尔如何证明", "ALIGNED",
         "带宇宙的 Lean 证明了 Con(𝗭𝗙𝗖) 与某个真的永不停句不被 ZFC 证明；元理论更强，与哥德尔第二定理相容",
         "若有人把这说成 ZFC 内部可证，判越界"),
    73: ("借鉴哥德尔的元思维：神似，而不是形似", "ALIGNED",
         "接受 = ZFC 自己的可证性；原过程完成 = 停机（用户口径）；对角点由 Kleene 递归定理构造（CG001-C-85、C-99）；不是表面自指",
         "若对角点或桥被写进前提，判形似"),
    74: ("想法 T：与哥德尔神交", "DEEPENED",
         f"“观察力不完备”一形已有实例：不存在完备的永不完成观察者，任何观察者都有严格更大的、仍有漏点的观察者（CG001-C-86、C-87）；“维度缺失”一形、一般陈述与脚手架未形式化（{TP} Ⅴb-5）",
         "若一般陈述被写出后与实例不相容，改写"),
    75: ("是不是一直在外围", "ALIGNED",
         f"观察接口取 ZFC 自己关于过程完成的定理，判词关于 bare ZFC 本身；同时照实写明 R-无 未交付、时间结构一面未承接（{TP} §6）",
         "若研究发起人认为仍在外围，按其指认的核心层重定目标"),
}


def audit_text(original_blocks: int) -> str:
    rows = []
    counts: dict[str, int] = {}
    for n in range(1, 76):
        name, relation, assess, nxt = AUDIT[n]
        for cell in (name, assess, nxt):
            if "|" in cell:
                raise SystemExit(f"AUDIT_CELL_PIPE:KC-{n:06d}")
        if relation not in R.KC_RELATIONS:
            raise SystemExit(f"AUDIT_RELATION:{n}:{relation}")
        counts[relation] = counts.get(relation, 0) + 1
        rows.append(f"| `KC-{n:06d}` | {name} | {relation} | {assess} | {nxt} |")
    tally = "、".join(f"{k} {v}" for k, v in sorted(counts.items()))
    head = f"""# {SESSION_ID} 完整兼容审计

{GEN14}；75 KC。canonical writer 只授权新 session 目录第一层文件，所以本审计是单文件兼容 bundle；`G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001` 保持。逐条立场由本会话写成（本机 Claude Code 会话 d58e0c0d；Claude Opus 5.5），依据是本会话读过的四件套（见 SESSION.md 的 load_receipt）与本单元的实际产物。

- core_change: YES_ADDITIVE_PRESERVING — {GEN13}/62 → {GEN14}/75；新增 KC-000063–KC-000075（研究发起人 2026-10-03 至 10-05 的十三条 ZFC 与哥德尔路线原文）；62/62 旧单元 PRESERVED_EXACT、mapping_remainder=0；来源文件 `{SRC14}`；纳入清单经研究发起人 2026-10-08 批准（“按清单应用，含 dev-01 #13”），09-19、09-27、10-01 的幽灵原话这次不纳入。
- direction_change: YES — 方向追踪新增 `{DIR_GODEL}` 与 `{DIR_ROUTES}`；三条已有 ZFC 行原位加路线归属的交叉引用；索引身份刷到 revision {NEW_REVISION}。
- panorama_change: YES — 全景视野 003 新增 `{OUT_GODEL}`、`{OUT_IMPORT}`，004 新增 `{OUT_TARGETS}`，008 新增第 21 项；索引身份刷到 revision {NEW_REVISION}。
- essay_change: YES_NEW_SHARD — 新增第 013 片《{ESSAY_013_TITLE}》：十三个原文块与 AI 阐释；索引基线刷到 {GEN14}；第 005 片的基线说明同步；全部原文块与核心认知逐字一致（准备脚本在写入前逐块比对，共 {original_blocks} 块，每个 KC 至少一次）。
- update_decision: 入核按研究发起人批准的清单执行；CG-005/006 的结果、分支并入与两条路线的目标画像登记进共享 owner；MEMORY/001 的当前最高优先改为两条路线，F-053 一节并行保留，并修复首行分片注释中混入的段落；STATE 的执行控制只更新检查点指针，活动目标字段（Goal7 / MO3-COVERAGE-C）未改；无新数学主张经本 checkpoint 交付。
- cross_conflicts: KC-000062（模式 P 一遍匹配）与证据（三刀与 P-DAG 未定位出 ZFC 的 Q）之间写成 TENSION；研究发起人要两个结果，GPT 的收敛 SOP 却把它们写成互斥判词值；时间的两个侧面中，有哥德尔路线只承接过程与可计算性一面，稠密性一面（KC-000003、KC-000048）未承接；dev-01 分支的 C0–C6 判词与主干的 C0R11 尚未合账；STATE 执行控制仍记 Goal7 为活动目标，而实际工作是 CG-006。
- unresolved: R-无 的交付形态（研究发起人选定 a/b/c）；Z0 的两条前提与内部化；同一个 Q 的单一内核证明；P 的语义侧与 ω 规则的形式联系；圆环的完整结构；想法 T 的一般形式；以已知答案校准模式 P（需研究发起人决定是否重启 P-DAG）；来源层到形式层；时间结构一面；`rulings.md` 同步第 14 代裁定；`main` 发布。见 `{REC_FOLLOW}`。

关系计数：{tally}（计数不认证理解）。

|KC ID|姿态|relation|assessment and evidence|next and falsifier|
|---|---|---|---|---|
"""
    tail = f"""

## 扩展认知按片回评

| 片 | 本单元的关系 | 说明 |
|---|---|---|
| 001 | 未触及 | 问题意识与理论的简化；本单元未改变其判断 |
| 002 | 触及（使用） | 时间与时序的澄清被用来区分两条路线承接的两个侧面（{TP} §4 第 4 点；第 013 片“元理论的精度就是维度”） |
| 003 | 触及（使用） | 芝诺、圆环与两种方向：跑者与 P 分别对上两类形状（KC-000014、KC-000022 行） |
| 004 | 触及（使用） | “用一个理论研究不完备”与“理论对自身作完备担保”的区分，用于 KC-000072 的回答 |
| 005 | 改写基线说明 | 编写说明中的当前基线改为 generation-14；正文未改 |
| 006 | 未触及 | 第三条发现路径 |
| 007 | 未触及 | AI 数学的两件事 |
| 008 | 未触及 | 现实对齐 |
| 009 | 未触及 | 从可疑前提到针对性过程 |
| 010 | 未触及 | 罗素线的两批原文 |
| 011 | 未触及 | UR 与芝诺的模式匹配；Z0 的 UR 读法写在终局报告，不改本片 |
| 012 | 触及（张力） | 模式 P 一遍匹配与证据之间的张力（KC-000062 行）；本片未改 |
| 013 | 新增 | 研究发起人 2026-10-03 至 10-05 的十三条原文与 AI 阐释 |

## 已走过的路与即将作出的选择

已走过的路（本会话，依时间）：CG-005 哥德尔式 Q 的抽象定理（C-84–C-94）；CG-006 把它落到 Foundation 的真实 𝗭𝗙𝗖（C-95–C-102）；接手全部分支（撞号映射、D01/D09 四包并入并重放、七个分支独有对话归档）；终局报告初稿；Z0 的条件形式（C-103）；第 14 代纳入清单经研究发起人批准；第四次压缩后，按研究发起人要求完成 Targets with Profile（八线倒查、五个方向、两条路线、44 点对照）；本 checkpoint。

即将作出的选择：

1. R-无 的交付形态：(a) 图灵路线、(b) T-OBS、(c) C6；支持 KC-000065、KC-000070、KC-000075；须研究发起人选定；反证条件：所选路线只得到接口层或来源层结果。
2. Z0 的第一条前提 `𝗜𝚺₁ ⪯ Sh`：支持 KC-000063、KC-000071；不需授权；反证条件：模型路线在 Σ1 归纳处卡住且无替代。
3. `main` 发布与推送：研究发起人已授权推送；`main` 只由发布脚本从 `dev` 生成，父提交 f3127701。
4. `rulings.md` 同步第 14 代裁定与 CG-006 授权：精确路径提交。

## 四项对齐与偏航分析

1. 用户主张：bare ZFC 在时间维度上的理论观察力不完备（不是没有，只是不完备）；Q 缺失允许数学幻觉 P，P 给出想要的 A 与不想要的 B，矛盾在社区实际使用的 ZFC-1 = ZFC + A = ZFC + P 中；回溯找到 P；魔鬼交易；想法 T；要无哥德尔与有哥德尔两个结果并综合（KC-000063–KC-000075；0115、0114）。
2. 不得收窄成：“ZFC ⊢ ⊥”；“只是一般的哥德尔定理”；“ZFC 能表示时间，所以没有问题”；“问题只在应用层，与 ZFC 无关”；“时间只是计算步骤”。
3. 怎样改变当前任务与证据选择：对象是真实的 𝗭𝗙𝗖；有哥德尔与无哥德尔分开记账；时间的两个侧面都要有承接；圆环与芝诺的原案要保住。
4. 仍然开放的证明义务：见 unresolved。

偏航风险与做法：最容易的偏航，一是把机器证明说成“证明了 ZFC 有缺陷”，二是反过来用“哥德尔现象人人都有”把判词消掉。本单元的做法：判词逐句标身份；矛盾的位置写成 𝗭𝗙𝗖 + P；归因写明“bare ZFC 不能豁免”，而不是“只有 ZFC 有”；未承接的部分（R-无、时间结构一面、圆环全貌）照实列出。
"""
    return head + "\n".join(rows) + tail


# ----------------------------------------------------------------------------------------------
# session files
# ----------------------------------------------------------------------------------------------

READ_AFTER_COMPACTION = [
    CORE, "最高指示-Claude版.md", "全景视野.md", "全景视野/004 - 距离综合与消费者审计.md", "全景视野/005 - 证据队列抽样与证据卫生.md",
    "全景视野/006 - ERCF-3 与 T3 脉冲及失败台账.md", "全景视野/007 - 历史来源结果与关系.md", "全景视野/008 - 当前未完成.md", ESSAY_INDEX,
    "扩展认知/001 - 问题意识与理论的简化.md", "扩展认知/002 - 前提改变、结果与时间.md", "扩展认知/004 - 走进 HoTT 与理论自反.md",
    ESSAY_005, "扩展认知/006 - 第三条发现路径：把知识谱当作被考察对象.md", "扩展认知/007 - AI数学的两件事：助力、阻力与符号翻转.md",
    "扩展认知/008 - 现实对齐：理论是现实的骨架式模仿.md", "扩展认知/009 - 从可疑前提到针对性过程.md",
    "扩展认知/010 - 论域元素的存在性追问：罗素线的两批原文.md", ESSAY_012, SRC14,
]
READ_BEFORE_COMPACTION = [
    "方向追踪.md", "方向追踪/001 - 三方职责与状态语义.md", "方向追踪/002 - 治理与用户方向.md", "方向追踪/003 - LocalGPT 与 WebGPT 方向.md",
    "方向追踪/004 - 证据与覆盖方向及 STATE 覆盖表.md", "方向追踪/005 - 交叉审视、优先级与更新规则.md",
    "全景视野/001 - 使用规则与状态语义.md", "全景视野/002 - 治理、门禁与骨架结果.md", "全景视野/003 - 当前机器证明包与原生重放.md",
    "扩展认知/003 - 芝诺、圆环、ASK 与两种方向.md", "扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md",
]
OTHER_READ = ["AGENTS.md", ".claude/rules/hott-claude.md", ".codex/cognition/TASK_ROUTING.md", ".codex/tools/cognition_runtime.py",
              "scripts/audit/prepare_claude_core_generation_10_checkpoint.py", "MEMORY.md", M2, TARGETS]


def receipt_rows(paths: list[str]) -> str:
    rows = []
    for rel in paths:
        data = (ROOT / rel).read_bytes()
        rows.append(f"|{rel}|{R.sha(data)[:16]}|{len(data)}|{data.decode('utf-8').count(chr(10))}|")
    return "\n".join(rows)


def session_text() -> str:
    return f"""# {SESSION_ID}

核心认知第 14 代入核（KC-000063–KC-000075：研究发起人 2026-10-03 至 10-05 的十三条 ZFC 与哥德尔路线原文），扩展认知新增第 013 片；方向追踪、全景视野、MEMORY、RESUME 与 STATE 登记 CG-005/006 的哥德尔式 Q 结果、分支并入和两条路线的目标画像。

- host: Claude Code（桌面应用 Code 标签页，本机 macOS），会话 d58e0c0d-fdab-467e-aa11-6f0151221e2e，分支 dev
- model: Claude Opus 5.5（claude-opus-5-5）
- tier: T3
- role: integrator（研究发起人 2026-10-07 全面授权）兼来源解释；本 checkpoint 不交付新数学主张
- authorization: 见 transaction 的 authorization 字段（2026-10-07 全面授权；2026-10-08 批准第 14 代清单与幽灵原话不纳入；2026-10-08 Targets with Profile 要求）
- parent: Claude 线目标包 CG-006（`{PKG}/`）；不改变 STATE 执行控制中的 Goal7 / MO3-COVERAGE-C 字段

## load_receipt

本会话在第四次上下文压缩之后用 Read 全文读过下表第一组文件；第二组是同一会话在压缩之前全文读过的四件套分片，压缩后按 PROTOCOL 的收据制复认（三触发器均未出现：核心认知只由本事务改变且新增条目已全文读入；档位未升；研究发起人没有要求全文重付），其中方向追踪 002、全景视野 003 在压缩后又读了本事务要改的行；第三组是治理与工具文件。核心认知第 14 代：第 13 代全文已读，新增十三条另读来源文件全文，其余 62 条经生成器逐字核对保留。表中是准备载荷时的哈希前缀、字节与行数。

**公开降级**：`STATE.json`（约 1.5 MB）没有整体读入模型上下文；本事务触及的部分（`current_core`、`latest_session`、`active`、`unresolved`、`execution_control`、记录种类分布、`{REC_PREV_CORE}`、一个 `formal_mathematical_result` 样例、`G-CLAUDE-PHASE-CLOSE-FOLLOWUPS-001`）经脚本逐项读取，其余由 runtime 的 plan 与 prepare 做结构核对。`MEMORY/001 - 当前执行队列.md` 只读了本事务改动的首部区段，没有整体重读；本事务只在首部插入一节、改一个标题，并把首行分片注释中混入的段落原样移回正文。

压缩后读入：

|path|sha256 前 16 位|bytes|lines|
|---|---|---|---|
{receipt_rows(READ_AFTER_COMPACTION)}

压缩前读入（收据制复认）：

|path|sha256 前 16 位|bytes|lines|
|---|---|---|---|
{receipt_rows(READ_BEFORE_COMPACTION)}

治理与工具：

|path|sha256 前 16 位|bytes|lines|
|---|---|---|---|
{receipt_rows(OTHER_READ)}

## 做了什么

1. 来源文件 `{SRC14}`（十三条，逐字取自问答树，时间取自原始 rollout）与 curation v14 已在 `26580ef6` 提交；`scripts/audit/build_core_cognition.py --write` 生成第 14 代、manifest 与 transition；`verify_core_cognition.py` 的结果见 RUNS.json。
2. 扩展认知新增第 013 片（模板 `{ESSAY_TEMPLATE_DEFAULT}`，十三个原文块由准备脚本替换并逐块比对）；索引基线与第 005 片的基线说明同步。
3. 方向追踪新增 `{DIR_GODEL}`、`{DIR_ROUTES}`，三条已有 ZFC 行加路线归属；全景视野新增三行与第 21 项未完成；两份索引的身份字段刷到 revision {NEW_REVISION}。
4. MEMORY/001 新增“当前最高优先：两条路线”，F-053 一节改为并行活跃，并修复首行分片注释中混入的 C0R9–C0R11 段落；MEMORY/002 补一条证据上限与恢复入口；MEMORY/003 与 RESUME 各加一段。
5. STATE 登记 `{REC_CORE}`、`{REC_RESULT}`、`{REC_TARGETS}`、`{REC_FOLLOW}` 与本 session；`execution_control` 只更新检查点指针。
6. 不做的事（及原因）：不改 STATE 的活动目标字段（Goal7 是 Codex 宿主目标，研究发起人没有要求改）；不写 LESSONS 全文日志（不在 canonical writer 的授权路径内，教训记在 CN-068）；不改共享证据矩阵（CG001-C-84–C-103 已在 `dev` 的矩阵中）；`rulings.md` 与 `main` 发布在本事务之后另做。

|element_usage|本次用途与边界|
|---|---|
|核心认知与最高指示-Claude版|第 14 代的十三条原文；判词逐句标身份；不把用户判定写成定理|
|build_core_cognition 与 verify_core_cognition|生成与校验第 14 代；62 个旧单元逐字保留|
|canonical runtime 与 writer|plan、prepare、checkpoint；单文件兼容审计；只认 canonical result|
|projection_edit|方向、全景、MEMORY、扩展认知的索引与全部分片同载荷|
|Targets 文件与 GUI 倒查工具|方向行、全景行与跟进记录的来源；GPT 回答只作自述|
|verify_three_way_cognition 与 verify_governance_shards|结构校验；不证明语义|

验证命令与结果见 RUNS.json。无新数学主张经本 checkpoint 交付。推送与 `main` 发布在本事务之后，由研究发起人的授权覆盖。
"""


def runs_obj(snapshot: str) -> dict:
    return {
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "session_kind": "GOVERNANCE_CORE_GENERATION_ESSAY_SHARD_AND_RESULT_REGISTRATION",
        "checkpoint_result": RESULT_REL,
        "base_snapshot": snapshot,
        "formal_runs": [],
        "related_goal_local_runs": {
            "note": "same session; proof packages registered in the shared claim matrix before this checkpoint; projected here, not re-delivered",
            "claims": "CG001-C-84 to CG001-C-103",
            "main_runs": MAIN_RUNS,
            "negative_control_runs": NEG_RUNS,
            "verification": "verify_cg001_run.py --rerun: PASS_WITH_SCOPE for the main runs and NEGATIVE_CONTROL_REJECTED_AS_EXPECTED for the controls, EXACT_EXIT_STDOUT_STDERR_MATCH",
            "index": CG001_INDEX,
            "imported_branch_runs": IMPORT_REPLAY,
        },
        "governance_runs": [
            {"tool": "scripts/audit/build_core_cognition.py",
             "command": f"--curation {CURATION} --transition-output {TRANSITION} --transition-from-ref 1f60cd57ccc2cf582c56b3269ca6084c93dc62fb --write",
             "status": "BUILT / COMPLETE_ADDITIVE_PRESERVING / mapping_count=62 / remainder=0", "generation": f"{GEN13}/62 -> {GEN14}/75"},
            {"tool": "scripts/audit/verify_core_cognition.py", "command": f"--curation {CURATION} --transition {TRANSITION}", "status": "PASS_WITH_SCOPE expected; see the commit message for the observed output"},
            {"tool": PREPARE_SELF, "command": f"--output <payload> --essay-template {ESSAY_TEMPLATE_DEFAULT}", "status": "PREPARED"},
            {"tool": ".codex/tools/cognition_runtime.py", "command": "checkpoint --snapshot <base_snapshot> --payload <payload> --apply",
             "status": "CHECKPOINT_COMMITTED expected; only the canonical result.json proves it"},
        ],
        "new_math_claims": [],
        "math_status_change": "NONE",
        "push_policy": "push of dev and release of main after this checkpoint, under the research sponsor's 2026-10-07 authorization",
        "note": "Core entry of the research sponsor's thirteen ZFC messages with essay shard 013, and registration of the CG-005/006 results, the branch imports and the two-route target profile.",
    }


# ----------------------------------------------------------------------------------------------
# STATE
# ----------------------------------------------------------------------------------------------

def state_edits(state: dict) -> None:
    session_path = f"{SESSION_REL}/SESSION.md"
    state["revision"] = NEW_REVISION
    state["latest_session"] = SESSION_ID
    state["current_core"] = {
        "core_sha256": sha_file(CORE),
        "curation": CURATION,
        "curation_sha256": sha_file(CURATION),
        "generation": GEN14,
        "kc_count": 75,
        "manifest": MANIFEST,
        "manifest_sha256": sha_file(MANIFEST),
        "path": CORE,
        "transition": TRANSITION,
    }
    ec = state["execution_control"]
    ec["last_checkpoint_session"] = SESSION_ID
    ec["checkpoint_result"] = RESULT_REL

    def hashes(paths: list[str]) -> dict[str, str]:
        return {p: sha_file(p) for p in paths}

    core_sources = [CORE, MANIFEST, CURATION, TRANSITION, SRC14, "scripts/audit/build_core_cognition.py", "scripts/audit/verify_core_cognition.py"]
    state["records"][REC_CORE] = {
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / COMPLETE_ADDITIVE_PRESERVING",
        "full_sources": core_sources,
        "kind": "core_generation_migration",
        "lifecycle_status": "CURRENT",
        "path": TRANSITION,
        "related_records": [REC_PREV_CORE, SESSION_ID],
        "scope": ("Incrementally add thirteen exact direct-user items of 2026-10-03 to 2026-10-05 (the research sponsor's ZFC and Gödel-route messages: "
                  "Q0(H0(Z0)); the circle paradox as ZFC's problem; Meta/Sub-theory precision; 'not absent, only incomplete'; the same-Q contradiction; "
                  "the Q/P/A/B and ZFC-1 hypothesis; the devil's bargain; bare ZFC; H0 as B; Gödel's meta-thinking; idea T; 'still at the periphery?') "
                  "while preserving all 62 generation-13 KCs byte for byte. Approved by the research sponsor on 2026-10-08; the ghost quotes of "
                  f"09-19/09-27/10-01 were excluded this time. Supersedes {REC_PREV_CORE} as the owner of the current core identity. "
                  "Timestamps are the first rollout record of each turn (UTC, seconds)."),
        "source_hashes": hashes(core_sources),
        "status": "closed",
    }
    result_sources = [f"{GQ}/CLAIM.md", f"{GQ}/README.md", f"{GQZ}/CLAIM.md", f"{GQZ}/README.md", f"{GQZ0}/CLAIM.md", f"{GQZ0}/README.md",
                      MATRIX, CG001_INDEX, REPORT] + [f"{RUNS_DIR}/{r}/RUN.json" for r in MAIN_RUNS]
    state["records"][REC_RESULT] = {
        "claim_ids": [f"CG001-C-{n}" for n in range(84, 104)],
        "classification": "GODEL_Q_PROCESS_OBSERVATION_INCOMPLETENESS_ON_FOUNDATION_ZFC_WITH_Z0_CONDITIONAL",
        "depends_on": [],
        "evidence_status": "MACHINE_PROVED_WITH_SCOPE / RUNS_REPLAYED_EXACT / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / VERSION_CLOSED_IN_DEV_GIT",
        "full_sources": result_sources,
        "kind": "formal_mathematical_result",
        "lifecycle_status": "CURRENT",
        "mathematical_status": "ZFC_STAGEWISE_VISIBLE_FOREVER_INVISIBLE / ZFC_PLUS_P_NON_RE_OR_INCONSISTENT / AGENERAL_IFF_Q_COMPLETE / Z0_CONDITIONAL_ON_SH_RE_AND_ISIGMA1",
        "path": f"{GQZ}/CLAIM.md",
        "proof_id": ["MP-CG001-GODEL-Q-001", "MP-CG001-GODEL-Q-ZFC-001", "MP-CG001-GODEL-Q-ZFC-Z0-001"],
        "related_records": [SESSION_ID, REC_TARGETS, REC_FOLLOW],
        "scope": ("Lean 4.34.0 with Foundation@1fb01b72 and Mathlib 5ed29652 (axioms propext, Classical.choice, Quot.sound). Abstract layer C-84..C-94; "
                  "on Foundation's real ZFC C-95..C-102 (Delta1 axiomatization, numerals, r.e. never-sentences, ZFC interprets R0, Sigma1/Delta0 "
                  "completeness, Sigma1 soundness, process form of Gödel I with independence, devil's bargain, runner, ZFC+A = ZFC+P); C-103 the Z0 "
                  "conditional form on the arithmetic shadow. Not ZFC proves False; consistency and Sigma1 soundness of ZFC are Lean meta-level facts "
                  "(Universe model); reading 'time dimension' as stepwise process is an interpretation bridge; the same-Q correspondence with H0 is "
                  "cross-kernel (C-93); Z0 needs two premises and an internalization."),
        "source_hashes": hashes(result_sources),
    }
    target_sources = [TARGETS, CN068, BACKTRACE, GUI_INDEX]
    state["records"][REC_TARGETS] = {
        "depends_on": [],
        "evidence_status": "DOCUMENTED / TARGET_PROFILE_FROZEN_V1 / NO_MATH_CLAIM",
        "full_sources": target_sources,
        "kind": "research_synthesis",
        "lifecycle_status": "CURRENT",
        "path": TARGETS,
        "related_records": [REC_RESULT, REC_FOLLOW, SESSION_ID],
        "scope": ("Targets with Profile (research sponsor's request of 2026-10-08): the eight GUI conversation lines traced back from their last turns to "
                  "their forks; five directions; the sponsor's two routes (without/with Gödel, dev-notes 0115 and 0114) kept as two deliverables plus a "
                  "synthesis; 44 profile points compared with completed work (19 done, 19 partial, 4 open, 2 reframed). GPT answers are self-reports."),
        "source_hashes": hashes(target_sources),
    }
    state["records"][REC_FOLLOW] = {
        "evidence_status": "PENDING_USER_ACTION / NOT_RUN",
        "full_sources": [session_path, TARGETS, CN067, CN068],
        "kind": "governance_follow_up",
        "lifecycle_status": "OPEN_ISSUE",
        "path": session_path,
        "related_records": [REC_RESULT, REC_TARGETS, REC_CORE, SESSION_ID, "MO3-COVERAGE-C"],
        "scope": ("Open after CG-006: (1) the form of the without-Gödel deliverable, to be chosen by the research sponsor: (a) Turing route (halting "
                  "undecidability + r.e. never-theorems + consistency, no diagonal point), (b) T-OBS route (carries the time-structure face: dense versus "
                  "discrete), (c) C6 route (make the metatheory's audit duty precise); (2) Z0: ISigma1 <= Sh, Sh.RE, and internalizing Con(Sh) <-> Con(ZFC); "
                  "(3) the same Q in a single kernel; (4) the formal link between the semantic P and the omega rule; (5) the full circle task contract; "
                  "(6) the general form of idea T; (7) calibrating pattern P against a known answer (needs the sponsor's decision on P-DAG nodes); "
                  "(8) source-layer items (community adoption of A; ZFC passing HoTT) to formal layer; (9) the time-structure face; "
                  "(10) governance: rulings.md sync of the generation-14 decision; STATE execution_control still names Goal7 / MO3-COVERAGE-C while "
                  "the actual work is CG-006; dev-01's C0-C6 verdict and the trunk's C0R11 are not reconciled."),
        "status": "open",
    }
    state["unresolved"].append(REC_FOLLOW)
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, f"{SESSION_REL}/RUNS.json", f"{SESSION_REL}/CORE_COGNITION_AUDIT.md", RESULT_REL, TRANSITION, CURATION, ESSAY_013],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV_SESSION, REC_CORE, REC_RESULT, REC_TARGETS, REC_FOLLOW],
        "scope": ("Core generation-14 entry (KC-000063 to KC-000075) with essay shard 013, and registration of the CG-005/006 Gödel-Q results, the "
                  "branch imports and the two-route target profile in the shared owners. Integrator under the research sponsor's 2026-10-07 "
                  "authorization; no new mathematics delivered through this checkpoint."),
        "source_hashes": {},
        "status": "complete",
    }


# ----------------------------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--essay-template", type=Path, default=ROOT / ESSAY_TEMPLATE_DEFAULT)
    args = parser.parse_args()

    required = [CORE, MANIFEST, CURATION, TRANSITION, SRC14, TARGETS, CN067, CN068, BACKTRACE, GUI_INDEX, REPORT, MATRIX, LEDGER,
                CG001_INDEX, IMPORT_REPLAY] + [f"{RUNS_DIR}/{r}/RUN.json" for r in MAIN_RUNS + NEG_RUNS]
    missing = [p for p in required if not (ROOT / p).is_file()]
    if missing:
        raise SystemExit(f"EVIDENCE_MISSING:{missing}")

    state_path = ROOT / R.STATE
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if state.get("revision") != PREV_REVISION or state.get("latest_session") != PREV_SESSION:
        raise SystemExit(f"EXPECTED_REVISION_{PREV_REVISION}:{state.get('revision')}:{state.get('latest_session')}")
    for identity in (SESSION_ID, REC_CORE, REC_RESULT, REC_TARGETS, REC_FOLLOW):
        if identity in state["records"]:
            raise SystemExit(f"RECORD_ALREADY_EXISTS:{identity}")

    plan = R.plan(ROOT, profile="governance", _allow_core_transition=CORE_TRANSITION)
    payloads = core_payloads()
    if list(payloads)[-13:] != NEW_KCS or len(payloads) != 75:
        raise SystemExit("CORE_NOT_GENERATION_14")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    direction_edits(direction)
    panorama = projection_edit.load(ROOT, R.PANORAMA)
    panorama_edits(panorama)
    essay = projection_edit.load(ROOT, R.ESSAY)
    essay_edits(essay, payloads, args.essay_template)
    memory = projection_edit.load(ROOT, "MEMORY.md")
    memory_edits(memory)

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(resume, "# 接续指针\n", "# 接续指针\n" + RESUME_ADD)

    state_edits(state)

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    texts: dict[str, str] = {path: (ROOT / path).read_text(encoding="utf-8") for path in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[resume_path] = resume
    original_blocks = verify_essay_originals(texts, payloads)
    texts[session_path] = session_text()
    texts[audit_path] = audit_text(original_blocks)
    texts[runs_path] = json.dumps(runs_obj(plan["snapshot"]), ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    created = {session_path, audit_path, runs_path, RESULT_REL, ESSAY_013}
    generated = (
        ("audit", texts[audit_path]), ("session", texts[session_path]), ("essay-013", texts[ESSAY_013]),
        ("direction-rows", DIR_ROW_GODEL + DIR_ROW_ROUTES), ("panorama-rows", PAN_ROW_GODEL + PAN_ROW_IMPORT + PAN_ROW_TARGETS + PAN_ITEM_21),
        ("memory", M1_TOP + M2_BULLET + M2_RECOVERY + MEMORY_003_ADD + RESUME_ADD),
    )
    for label, body in generated:
        check_paths(label, body, created)
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
                      "files": len(texts), "essay_original_blocks_verified": original_blocks}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
