#!/usr/bin/env python3
"""Prepare the checkpoint that registers core generation-10 (KC-000052 to KC-000054) and essay shard 011.

Scope (user instruction of 2026-09-30, Claude Code session eadb3381, recorded as message 2 of
sources/prompts/Claude-UR与芝诺的模式匹配-用户原文-20260930.md):

* core generation-10 was already built on disk by scripts/audit/build_core_cognition.py with
  scripts/audit/core-cognition-curation-v10.json; this checkpoint moves STATE.current_core to it
  (canonical core_transition path of the runtime);
* the essay (扩展认知) gets a new shard 011 that carries the context of the user's statement and the
  AI reading the user asked to place there; the index baseline moves to generation-10;
* 方向追踪 and 全景视野 only get their source_state_revision identity refreshed (their content is not
  changed: the user did not ask for a direction or result change; the open tension is registered as a
  follow-up record instead);
* MEMORY/003 and RESUME get one factual log line each; STATE gets the core-generation record, a
  follow-up record and the session record;
* the session bundle (SESSION.md, RUNS.json, CORE_COGNITION_AUDIT.md) is written in the same
  transaction, as the canonical writer requires.

The script only builds the payload; it writes nothing into the repository.  Apply it with
.codex/tools/cognition_runtime.py checkpoint --snapshot <printed snapshot> --payload <output> --apply
Modelled on scripts/audit/prepare_copus_core_generation_9_checkpoint.py.
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

SPEC = importlib.util.spec_from_file_location("runtime_claude10", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402

BSPEC = importlib.util.spec_from_file_location("builder_claude10", SCRIPTS / "build_core_cognition.py")
assert BSPEC and BSPEC.loader
B = importlib.util.module_from_spec(BSPEC)
BSPEC.loader.exec_module(B)

SESSION_ID = "S-GOV-20260930-CLAUDE-CORE-GENERATION-10-UR"
PREV_SESSION = "S-GOV-20260930-COPUS-CORE-GENERATION-9-REGISTRATION"
PREV_REVISION = 290
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"

CORE = "核心认知.md"
MANIFEST = "核心认知.manifest.json"
CURATION = "scripts/audit/core-cognition-curation-v10.json"
TRANSITION = "audit/core-cognition-generation-10-transition-20260930.json"
GEN9 = "core-cognition-generation-9"
GEN10 = "core-cognition-generation-10"
SRC_CODEX = "sources/prompts/Codex-非现实性悖论的目标与A向读法-用户原文-20260930.md"
SRC_CLAUDE = "sources/prompts/Claude-UR与芝诺的模式匹配-用户原文-20260930.md"
C83_CLAIM = "HoTT/formal/claude-cg001/truncation-questioning/CLAIM.md"
CG001_INDEX = ".claude/goals/CG-001-targeted-overview/证据索引.md"
CG001_RELAY = ".claude/goals/CG-001-targeted-overview/relay.md"
PREPARE_SELF = "scripts/audit/prepare_claude_core_generation_10_checkpoint.py"

ESSAY_INDEX = "扩展认知.md"
ESSAY_010 = "扩展认知/010 - 论域元素的存在性追问：罗素线的两批原文.md"
ESSAY_011_TITLE = "本来应该很简单的事：UR 与芝诺的模式匹配"
ESSAY_011 = f"扩展认知/{'011'} - {ESSAY_011_TITLE}.md"
ESSAY_011_TEMPLATE_ENV = "ESSAY_011_TEMPLATE"

CORE_TRANSITION = {
    "from_generation": GEN9,
    "to_generation": GEN10,
    "manifest": MANIFEST,
    "transition": TRANSITION,
}

REC_CORE = "A-CLAUDE-CORE-GENERATION-10-001"
REC_FOLLOW = "G-CLAUDE-CORE-GEN10-FOLLOWUPS-001"

AUTHORIZATION = (
    "User 2026-09-30 (local Claude Code session eadb3381), answering the question whether to enter the UR statement into the core: "
    "我的这次论述，是需要完整记录下来的，但是这次论述的上下文，也是不能不伴随记录的。"
    "我认为你刚刚的回复对我的这次论述的解读，非常适合放入`扩展认知.md`中，那个文件的本意，就是用户说的内容，AI对应的理解是怎样的，我认为你理解得很好。"
    " The checkpoint records the statement and its context (core generation-10, KC-000052 to KC-000054) and the AI reading (essay shard 011); "
    "it does not change direction or result content."
)

PATH_PREFIXES = ("HoTT/", "docs/", ".claude/", "sources/", "scripts/", ".codex/", "扩展认知/", "方向追踪/", "全景视野/", "MEMORY/", "audit/")


def check_paths(label: str, text: str, extra_existing: set[str] = frozenset()) -> None:
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


def sha_file(rel: str) -> str:
    return R.sha((ROOT / rel).read_bytes())


def quote_block(kc: str, payload: str) -> str:
    body = "\n".join(("> " + line) if line else ">" for line in payload.split("\n"))
    return f"<!-- original:{kc}:begin -->\n{body}\n<!-- original:{kc}:end -->"


def verify_essay_originals(texts: dict[str, str], payloads: dict[str, str]) -> int:
    """Every `original:KC-…` block of the essay must equal the core payload byte for byte."""
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

def essay_shard_011(payloads: dict[str, str], template_path: Path) -> str:
    text = template_path.read_text(encoding="utf-8")
    for kc in ("KC-000052", "KC-000053", "KC-000054"):
        placeholder = "{" + kc + "}"
        if text.count(placeholder) != 1:
            raise SystemExit(f"TEMPLATE_PLACEHOLDER:{kc}:{text.count(placeholder)}")
        text = text.replace(placeholder, quote_block(kc, payloads[kc]))
    if "{KC-" in text:
        raise SystemExit("TEMPLATE_PLACEHOLDER_LEFT")
    heading = re.search(r"(?m)^# (.+)$", text)
    if heading is None or heading.group(1).strip() != ESSAY_011_TITLE:
        raise SystemExit("ESSAY_011_TITLE_MISMATCH")
    return text if text.endswith("\n") else text + "\n"


def essay_edits(essay: dict, payloads: dict[str, str], template_path: Path) -> None:
    essay["shards"][ESSAY_011] = essay_shard_011(payloads, template_path)
    idx = essay["index_text"]
    idx = replace_once(idx, f"baseline: {GEN9}", f"baseline: {GEN10}")
    idx = replace_once(idx, "本文根据《核心认知.md》generation-9 的全部 51 段原文综合写成", "本文根据《核心认知.md》generation-10 的全部 54 段原文综合写成")
    idx = replace_once(idx, "本索引 + 下方 10 个分片", "本索引 + 下方 11 个分片")
    idx = replace_once(idx, f"last_shard: {ESSAY_010}", f"last_shard: {ESSAY_011}")
    row10_start = "| 010 | [论域元素的存在性追问：罗素线的两批原文]"
    lines = idx.split("\n")
    pos = [i for i, line in enumerate(lines) if line.startswith(row10_start)]
    if len(pos) != 1:
        raise SystemExit("ESSAY_INDEX_ROW_010")
    row11 = (f"| 011 | [{ESSAY_011_TITLE}](<{ESSAY_011}>) | 用户 2026-09-30 的三段原文（KC-000052–KC-000054）及其上下文："
             "四句证据链被读作非现实性悖论；项目目标不加“存在性”限定；UR 的定义与芝诺的模式匹配；"
             "对照表、两副面孔、教科书消解的对位、“相同可以无限细分”、A／B 两向分工与“找到了”的身份分层 | current |")
    lines.insert(pos[0] + 1, row11)
    essay["index_text"] = "\n".join(lines)


# ----------------------------------------------------------------------------------------------
# audit
# ----------------------------------------------------------------------------------------------

E11 = "扩展认知 011"
NT = "本单元（核心认知第 10 代入核、扩展认知 011、截断对照 C-83）没有重新判断该条所指的内容；原文身份保留。"

AUDIT: dict[int, tuple[str, str, str, str]] = {
    1: ("HoTT悖论研究三问", "NOT_TOUCHED", NT, "写一页“HoTT 的芝诺”时，按三问（找什么、怎么找、凭什么）检查；若短链答不出其中一问，回源本条"),
    2: ("Theory Schema先行", "NOT_TOUCHED", NT, "需要把单价性、高阶归纳类型定位到具体规则时，回 Theory Schema 与本条"),
    3: ("合取前提与稠密过程", "ALIGNED",
        f"模式匹配沿用芝诺的反证结构：推理不错，前提可疑；HoTT 一侧对位的前提是“相同可以无限细分”。芝诺的前提（稠密性）是用户的归因，本单元不检验稠密性本身。证据：{E11} 的对照表与“被改掉的条件”一节；CN-050 第 2、3 节",
        "若有人把本单元读成对稠密性的回答，判偏航；回到稠密性或圆环原题时再触及"),
    4: ("悖论作为反证与运动前提", "ALIGNED",
        f"UR 的推理部分经内核检查（C-75、C-78、C-81，目标本地索引 §19–§21），问题归到前提，与“结论出现矛盾，必然是前提出现了错误”同形。证据：{E11} 对照表“推理本身”一行",
        "若出现证据表明推理依赖了未写明的前提（例如对闭判定器的典范性），把它列入候选前提重审"),
    5: ("先找悖论后作最终归因", "CORRECTED",
        f"按 KC-000049 的修正，本单元在现象显出后直接展开归因（CN-049 第 9 节、CN-050 第 3 节、{E11}“被改掉的条件”一节）；KC-000005 的原话保留",
        "若再以“下一个故事”推迟已有现象的归因，判偏航"),
    6: ("时间机制不能收窄为稠密性", "ALIGNED",
        f"“相同可以无限细分”只借芝诺的结构（每一步留下下一步），不把 HoTT 的问题收窄成稠密性（{E11}“被改掉的条件”一节末段）",
        "若后续叙述把 UR 说成稠密性问题，判收窄"),
    7: ("LLM内在知识与模式匹配", "ALIGNED",
        f"用户以“模式匹配”回答问题，正是本条期待的能力；AI 的回答是逐行对照，并写明对照不是数学同构（CN-050 第 2、6 节；{E11}“本片的限度”）",
        "若对照被当作证明，或只识别已知悖论的名称而不定位前提，判偏航"),
    8: ("历史时间悖论作为HoTT启发", "ALIGNED",
        "芝诺作为历史时间悖论给出模式，本单元据以定位 HoTT 的对位前提（CN-050 第 2 节）",
        "若把芝诺的具体内容（稠密性）直接移植为 HoTT 的前提，判偏航"),
    9: ("定位HoTT理论设定的时间维度", "NOT_TOUCHED", NT, "若要说明 UR 与时间维度的关系（逐层追问是一个过程），回源本条与 KC-000011、KC-000023"),
    10: ("目标是现实相对非现实性而非内部矛盾", "ALIGNED",
         f"UR 的实例：在相同是事实的世界里一问就了结的确认，Think in HoTT 之后是不停机的程序（C-78、C-81，目标本地索引）；重点不在内部矛盾（{E11}“找到了说到哪一层”一节）",
         "若有人据此宣称 HoTT 不一致，判越界"),
    11: ("理论推演排除时序与程序显式时序", "NOT_TOUCHED", NT, "若把“对截断发问”论证为“另记一本账”，回源本条（时序只进对象、不进思考过程）"),
    12: ("ASK计算合法性预分析", "NOT_TOUCHED", NT, "若把修复的“凭定义宣布完成”作为 B 向正式立论，回源 ASK 的定义"),
    13: ("ASK深化与理论工具性异化", "ALIGNED",
         f"UR 的“理论为了好用改掉了条件”与本条“为了理论本身的工具性（好用性）”同向：单价性为经济，高阶归纳类型为普适（{E11}“被改掉的条件”一节）",
         "若找不到改掉条件带来的收益，这一对位撤回"),
    14: ("双向目标的第二方向", "DEEPENED",
         f"两向分工：书式 HoTT 里的现象是 A 向，修复（极限、截断）凭定义宣布完成是 B 向；这是解释，不是定理（CN-050 第 2 节；{E11} 对照表后的第三处对位）。C-83 机器检查了截断一侧：第 1 问停，但把两种自我认同合一，且解码不回去（`{C83_CLAIM}`）",
         "若用户把 B 向限定在理论本身而不在修复，这一分工重写"),
    15: ("抽象即否定现实前提与Z铁律", "ALIGNED",
         f"宇宙与这类乘积没有有限层是已知数学事实（HoTT Book 例 8.8.6；Kraus–Sattler），本单元只把它读成 UR；与“我们只是要寻找和证明，它在HoTT中也存在具体的现象”一致（{E11}“找到了说到哪一层”一节）",
         "若文献查重发现同一读法已被提出，保留事实，改写新颖性的表述"),
    16: ("Russell的构造过程与计算合法性", "ALIGNED",
         f"罗素线的 B 向读法保留在修复一侧：凭定义宣布完成，对应“非法程序被当作理论成功”的形状（{E11} 第三处对位）；KC-000050、KC-000051 的存在性读法未撤回",
         "若用户确认罗素线只挂 A 向，这一条的关联改写"),
    17: ("训练先验批判与Thinking in my math philosophy", "ALIGNED",
         f"教科书消解（极限、截断）被当作对照表里要回答的一行，不被用来否决 UR（CN-050 第 2 节；{E11}“换题”一段）",
         "若回答中出现“截断已经解决了，所以不是悖论”的推断，判偏航"),
    18: ("Z铁律的理论工具性与时间否定", "ALIGNED",
         f"Z 铁律“前提中的 T 变为非 T，结论 C 成为非 C”在本线的读法：T 是“相同是一次检查的事实”，非 T 是“相同是可以无限追问的结构”，C 由“一问了结”变为“永不了结”（{E11}“被改掉的条件”一节）",
         "若对照表明改变 T 不改变 C（例如相同是事实时也不停），这一读法撤回"),
    19: ("合取真值与稠密空间中的完成困难", "ALIGNED",
         f"合取前提：单价性与高阶归纳类型合在一起，才使追问永不停（C-79、C-80、C-82 的对照）；归因写成排序，不是唯一被告（{E11}“被改掉的条件”一节）",
         "若出现去掉其中一项仍永不停的构造，合取结构重审"),
    20: ("悖论反证、运动量子化与HoTT时间怀疑", "CORRECTED",
         "同 KC-000005：其中“下一个故事”一句的工作次序效力已由 KC-000049 修正，本单元直接归因；运动量子化本身未涉及，只在对照表中作为芝诺一侧的离散对照（用户的前提）",
         "同 KC-000005"),
    21: ("机器证明与真实运行要求", "ALIGNED",
         f"本单元新增 C-83（截断对照）：源码、两个负控制、三个运行、目标本地索引 §22，精确重放（`{C83_CLAIM}`）",
         "若共享矩阵要求另建索引行，交 integrator（relay R1）"),
    22: ("两类现实相对悖论", "ALIGNED",
         f"KC-000052 的形状是第一类（现实中能完成，理论中却无法完成）；第二类落在修复一侧（见 KC-000014 行）。证据：{E11}“上下文”一节",
         "若用户确认罗素线应读作第二类，这一条改为 TENSION 并回源"),
    23: ("时间时序处理应可直接定位", "NOT_TOUCHED", NT, "若要指出 UR 对应的时间或时序处理，回源本条"),
    24: ("两类时序悖论与HoTT搜索问题", "ALIGNED",
         f"芝诺作为第一类的范例，“每次走剩下的一半，永远走不完”是不可停机问题；HoTT 的追问同为过程形式的不停机（{E11}“做不完是同一种”）",
         "若把追问的不停机读成“缺统一方法”一类，判混淆（见第 003 片的完成种类）"),
    25: ("自指型悖论为何难找", "NOT_TOUCHED", NT, "若自指型构造进入罗素线，回源本条"),
    26: ("HoTT自身自指不可越过的怀疑", "NOT_TOUCHED", NT, "若自指型构造进入罗素线，回源本条"),
    27: ("HoTT对齐程序后继承程序自反界限", "NOT_TOUCHED", NT, "若有人把追问的不停机读成一般停机界限，回源本条，区分 HoTT 特有与程序共有"),
    28: ("HoTT自反真理验证的不可停机与自馈回环怀疑", "NOT_TOUCHED", NT, "若把逐层追问读作自馈回环，回源本条与 CN-038"),
    29: ("理论经济收益作为自馈回环的高风险位置", "ALIGNED",
         f"单价性“同构即相同”正是经济收益所在，UR 恰出现在这里（{E11}“被改掉的条件”一节）",
         "若证据显示 UR 不依赖单价性（例如相同是事实的世界也不停），这一对位撤回"),
    30: ("历史理论经济认知完整性与HoTT经济学之问", "NOT_TOUCHED", NT, "若要回答 HoTT 追求怎样的理论经济学，以本单元的单价性对位为材料回源"),
    31: ("HoTT严格范型可能拒绝最小理想理论的构造方向", "NOT_TOUCHED", NT, "若构造最小理想理论，回源本条"),
    32: ("悖论反证理论与稠密性否定所引入的存在性", "ALIGNED",
         f"“相同可以无限细分”是理论引入的新内容（无穷多层不平凡的相同），对应本条所说否定现实因素后引入的新内容（{E11}“被改掉的条件”一节）",
         "若用户认为相同的层次在现实中本来存在，这一对位改写"),
    33: ("Russell悖论对无时序不存在性前提的攻击", "NOT_TOUCHED", NT, "若罗素线的 B 向读法正式立论，回源本条"),
    34: ("否定性存在与不存在的现实相对双视角", "NOT_TOUCHED", NT, "若讨论“相同的无限层”是存在性还是不存在性，回源本条"),
    35: ("HoTT能否完整表达用户悖论研究理论", "NOT_TOUCHED", NT, "若问 HoTT 能否表达 UR 本身，回源本条"),
    36: ("HoTT研究哥德尔不完备性时的循环与自馈风险", "NOT_TOUCHED", NT, "若把追问与哥德尔不完备性并论，回源本条"),
    37: ("圆环悖论由用户一眼发明", "ALIGNED",
         f"UR 以“人一眼看过去就能理解的不合理”为判据，与“圆环悖论能够被我一眼想到”的发现姿态相接（{E11}“UR”一节）",
         "若 UR 需要长篇铺垫才能被理解，说明写法未达标，回到一页短链修改"),
    38: ("捕捉HoTT作者思路缺陷原是很基础的工作", "NOT_TOUCHED", NT, "若论证单价性是“基础之处”的缺陷，回源本条与 KC-000039"),
    39: ("机器统观久未发现HoTT悖论的困惑", "NOT_TOUCHED", NT, "若论证单价性是“基础之处”的缺陷，回源本条与 KC-000038"),
    40: ("第三条发现路径：反观训练数据中的HoTT知识谱", "NOT_TOUCHED", NT, "若以训练知识中的经典同伦事实作论证主轴，回源本条（知识谱是被考察对象，不是判断权威）"),
    41: ("AI数学的两件事", "NOT_TOUCHED", NT, "若评估本线对“超越 AI”的意义，回源本条"),
    42: ("助力有多大，阻力就有多大", "NOT_TOUCHED", NT, "若评估本线对“超越 AI”的意义，回源本条"),
    43: ("一体两面：认知惯性与路径依赖", "NOT_TOUCHED", NT, "若出现熟悉答案（极限、截断）被直接用作结论，回源本条"),
    44: ("理论是对现实的骨架式模仿", "NOT_TOUCHED", NT, "向外人解释“是同一个”时，若说出“同伦型没有现实对应”，判偏航并回源本条"),
    45: ("数学与HoTT必然可映射现实", "ALIGNED",
         f"UR 的“现实”即“本来应该很简单的事情”，给现实对齐一个可操作的落点；对照表指出 HoTT 在哪里为经济性舍弃了事实式的相同（{E11}“UR”与“被改掉的条件”两节）",
         "若外行读者读不懂“是同一个，本来是一句话的事”，现实对齐尚未完成"),
    46: ("AI缺的是用现实理解理论的动作", "ALIGNED",
         f"从现实的角度出发理解 HoTT：先问现实里那件简单的事，再看理论里为什么做不到（{E11}“UR”与“模式匹配”两节）",
         "若回答退回“HoTT 的相同没有现实对应”，判偏航（KC-000044）"),
    47: ("经济性与普适性的理想抽象与反证", "ALIGNED",
         f"经济性（单价性）与普适性（高阶归纳类型）两种非现实抽象都在 UR 中出现；按反证回溯，被审的是设计者的抽象（{E11}“被改掉的条件”一节）",
         "若用户裁定两者都不是非现实抽象，归因改写"),
    48: ("针对可疑理论前提设计悖论过程", "ALIGNED",
         "控制专门碰靶前提：相同是事实（C-80）、高度封顶（C-79、C-82）、换成截断（C-83），每一项只改一处（目标本地索引 §20–§22）",
         "若某个控制同时改了多处，敏感性结论降级"),
    49: ("归因是要与用户仔细探讨的正题", "ALIGNED",
         f"归因直接展开：候选前提、竞争归因（含“换题”）、区分证据（含经典同伦对照）、带身份的判断（CN-049 第 9 节；CN-050 第 3 节；{E11}“被改掉的条件”一节）",
         "若归因被推迟，或只给唯一被告而没有竞争归因，判偏航"),
    50: ("论域元素的存在性是理论无法拒绝的问题（P1–P3）", "TENSION",
         f"KC-000052、KC-000053 把四句证据链读作 A 向，并说项目目标不加“存在性”限定；本条以“存在性的追问”定罗素线的成功条件，是 B 向形状。本单元不撤回任何一方，写成两种读法并存（{E11}“上下文”一节；CN-049 第 8 节）。纠偏与回航：方向登记怎样挂，由用户与 integrator 决定（relay R3 第 9 条；{REC_FOLLOW}）",
         "若用户确认两向并列或只挂一向，张力按其裁定解除；若用户说 KC-000053 意在撤回存在性读法，本条关系改写"),
    51: ("算符先于存在性落定（罗素线第二批）", "TENSION",
         f"同 KC-000050；本条的“算符先于存在性落定”在两向分工里落在 B 向一侧（{E11} 第三处对位）",
         "同 KC-000050"),
    52: ("四句证据链就是非现实性悖论", "ALIGNED",
         f"本单元把它入核（核心认知第 10 代），来源文件逐字保存用户消息及其转引的四句（`{SRC_CODEX}`）；{E11}“上下文”一节展开",
         "若核对 0102 发现文字不一致，按来源修正并重建"),
    53: ("项目目标不加“存在性”限定", "ALIGNED",
         f"本单元把它入核；{E11}“上下文”一节写明它不撤回 KC-000050、KC-000051",
         "若用户说它意在撤回存在性读法，KC-000050、KC-000051 的关系改写"),
    54: ("UR 与芝诺的模式匹配", "ALIGNED",
         f"本单元把它完整入核，上下文写入来源文件文首与 {E11}；C-83 补上对照表中截断一行的机器检查（`{C83_CLAIM}`）",
         f"若用户认为解读偏离，按用户的修正重写 {E11}"),
}


def audit_text() -> str:
    rows = []
    counts: dict[str, int] = {}
    for n in range(1, 55):
        name, relation, assess, nxt = AUDIT[n]
        for cell in (name, assess, nxt):
            if "|" in cell:
                raise SystemExit(f"AUDIT_CELL_PIPE:KC-{n:06d}")
        counts[relation] = counts.get(relation, 0) + 1
        rows.append(f"| `KC-{n:06d}` | {name} | {relation} | {assess} | {nxt} |")
    tally = "、".join(f"{k} {v}" for k, v in sorted(counts.items()))
    head = f"""# {SESSION_ID} 完整兼容审计

{GEN10}；54 KC。canonical writer 只授权新 session 目录第一层文件，所以本审计是单文件兼容 bundle；`G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001` 保持。逐条立场由本会话写成（本机 Claude Code 会话 eadb3381；Claude Opus 5.5），依据是本会话压缩后全文读过的四件套与本单元的实际产物。

- core_change: YES_ADDITIVE_PRESERVING — {GEN9}/51 → {GEN10}/54；新增 KC-000052（四句证据链就是非现实性悖论）、KC-000053（项目目标不加“存在性”限定）、KC-000054（UR 与芝诺的模式匹配）；51/51 旧单元 PRESERVED_EXACT、mapping_remainder=0；来源文件两份（`{SRC_CODEX}`、`{SRC_CLAUDE}`），各带上下文说明。
- direction_change: NO_CONTENT_CHANGE — 只把方向追踪索引的 source_state_revision 刷到 291；`DIR-U-RUSSELL-EXISTENCE-QUESTIONING` 与 KC-000052–054 之间有张力（A 向读法、项目目标不加存在性限定），按方向追踪 §7 应降为待重审，但用户本次没有授权改方向内容，列为跟进项 `{REC_FOLLOW}`。
- panorama_change: NO_CONTENT_CHANGE — 只把全景视野索引的 source_state_revision 刷到 291；`OUT-U-RUSSELL-UNIVERSE-QUESTIONING` 仍写“元层推论”，而 Claude 线目标本地索引已有 C-77 至 C-83（交接说明 W1，待授权），列入同一跟进项。
- essay_change: YES_NEW_SHARD — 新增第 011 片《{ESSAY_011_TITLE}》：三段原文块、上下文、用户认可的 AI 解读；索引基线刷到 {GEN10}；扩展认知全部原文块与核心认知逐字一致（准备脚本在写入前逐块比对，共 54 块，每个 KC 至少一次）。
- update_decision: 入核与扩展认知的写入是用户 2026-09-30 明确要求的动作；方向与全景的内容不改；不把用户判定写成数学定理；不宣称 HoTT 不一致；同会话的 C-83 另在 Claude 线目标本地索引登记，不经本 checkpoint。
- cross_conflicts: KC-000050／051（存在性的追问，B 向形状）与 KC-000052／053（A 向读法，项目目标不加存在性限定）并存，本单元写成两种读法并存、两向分工（现象 A、修复 B），不裁定；扩展认知第 010 片“没有单独机器化”一句是写入时的状态，第 011 片注明其后的目标本地索引结果；共享 owner 与目标本地索引对罗素线证据身份的说法不一致（W1）。
- unresolved: 方向登记怎样挂（用户与 integrator）；W1（全景、STATE、MEMORY/002、扩展认知 010 的证据身份）；`rulings.md` 是否同步 KC-000053（方向追踪 §7 要求同步 rulings，本次未授权）；一页“HoTT 的芝诺”（用户已要求，写在 `.claude/` 下，不经本 checkpoint）；C-77 至 C-83 的跨平台重放（W12）。

关系计数：{tally}（计数不认证理解）。

|KC ID|姿态|relation|assessment and evidence|next and falsifier|
|---|---|---|---|---|
"""
    tail = f"""

## 扩展认知按片回评

| 片 | 本单元的关系 | 说明 |
|---|---|---|
| 001 | 未触及 | 问题意识与理论简化；本单元未改变其判断 |
| 002 | 未触及 | 前提改变与时间；“相同可以无限细分”不改写时间与时序的区分 |
| 003 | 触及（使用） | 第 011 片用本片“完成的几种含义”说明 UR 与芝诺同属“每个有限阶段都未到达”与“指定程序不停止” |
| 004 | 未触及 | 走进 HoTT 与理论自反 |
| 005 | 未触及 | 表达界限与编写说明（其原文基线说明仍是 generation-5，属本片自身的历史说明） |
| 006 | 未触及 | 第三条发现路径 |
| 007 | 未触及 | AI 数学的两件事 |
| 008 | 未触及 | 现实对齐 |
| 009 | 未触及 | 从可疑前提到针对性过程 |
| 010 | 触及（张力） | 两种读法并存：本片的存在性读法未撤回；其“没有单独机器化”一句是写入时的状态，第 011 片注明其后的目标本地索引结果；本片未改 |
| 011 | 新增 | 用户 2026-09-30 的三段原文、上下文与 AI 解读 |

## 已走过的路与即将作出的选择

已走过的路（本会话，依时间）：例 8.8.6 邻近对照（C-81、C-82）；中断恢复后读 0102，写 CN-049（A 向读法，第 8 节收窄，第 9 节归因）；用户以 UR 回答，写 CN-050；用户要求“做”，完成 C-83（截断对照，三个运行精确重放）；用户要求入核与写扩展认知，本 checkpoint。

即将作出的选择：

1. 写一页“HoTT 的芝诺”（用户已要求“写”）：支持 KC-000001、KC-000010、KC-000037、KC-000045；可能违背 KC-000017（若把教科书消解写成结论）；做法：先答掉“换题”；反证条件：外行读不懂第一句铺垫。
2. 方向与全景的登记（罗素线的标签、证据身份）：支持 KC-000050–054 的一致；须用户授权；回退：保持现状并在 `{REC_FOLLOW}` 保留。
3. `rulings.md` 同步 KC-000053：方向追踪 §7 的要求；须用户授权。
4. 跨平台重放 C-77 至 C-83：支持 KC-000021；不需授权，但不是本次指示。

## 四项对齐与偏航分析

1. 用户主张：非现实性悖论即 UR（本来应该很简单的事情，甚至在 X 理论中都做不到）；罗素线的四句证据链就是这样一个悖论；项目目标不以“存在性”为定语（KC-000052–054）。
2. 不得收窄成：“截断已经解决了”“极限理论早就回答了芝诺”“这只是已知的同伦群计算”“项目目标就是存在性研究”“HoTT 不一致”。
3. 怎样改变当前任务与证据选择：现实一侧由 UR 的前半句给出；对照表必须包含教科书消解并答掉它（C-83）；归因写成排序并带竞争归因。
4. 仍然开放的证明义务：元层的一致性与典范性（C-77、C-78 同）；任务忠实性由用户裁定；共享 owner 的证据身份（W1）；外部复核与文献查重。

偏航风险与做法：最容易的偏航是把用户的判定写成“HoTT 被证明有悖论”，或者反过来用教科书消解把 UR 消掉。本单元的做法：身份分层（机器证明、用户判定、AI 判断），对照表把消解列为要回答的一行，禁止外推写进 C-83 与第 011 片。
"""
    return head + "\n".join(rows) + tail


# ----------------------------------------------------------------------------------------------
# session files
# ----------------------------------------------------------------------------------------------

LOAD_FILES = [
    "AGENTS.md", "最高指示-Claude版.md", ".claude/rules/hott-claude.md", ".codex/cognition/PROTOCOL.md",
    ".codex/skills/hott-local-session-governance/SKILL.md", ".codex/tools/cognition_runtime.py",
    "scripts/audit/build_core_cognition.py", "scripts/audit/verify_three_way_cognition.py",
    "scripts/audit/prepare_copus_core_generation_9_checkpoint.py",
]


def logical_files(index_rel: str) -> list[str]:
    doc = projection_edit.load(ROOT, index_rel)
    return [index_rel] + list(doc["shards"])


def load_receipt_rows() -> list[str]:
    rows = []
    files = [CORE] + logical_files("方向追踪.md") + logical_files("全景视野.md") + logical_files("扩展认知.md") + LOAD_FILES
    for rel in files:
        data = (ROOT / rel).read_bytes()
        lines = data.decode("utf-8").count("\n")
        rows.append(f"|{rel}|{R.sha(data)[:16]}|{len(data)}|{lines}|")
    return rows


def session_text() -> str:
    receipt = "\n".join(load_receipt_rows())
    return f"""# {SESSION_ID}

核心认知第 10 代入核（KC-000052–KC-000054：用户 2026-09-30 的三段原文及其上下文），扩展认知新增第 011 片（用户要求放入的 AI 解读）；方向追踪与全景视野只刷新 revision；STATE 登记核心代记录、一个跟进项与本 session。

- host: Claude Code（桌面应用 Code 标签页，本机 macOS），会话 eadb3381-629b-4b9b-9fc4-e0fb942a4a9b，分支 main
- model: Claude Opus 5.5（claude-opus-5-5）
- tier: T3
- role: 用户授权的入核与扩展认知写入（治理对齐兼来源解释）；不是研究生成，不是独立审计
- authorization: 用户 2026-09-30：我的这次论述，是需要完整记录下来的，但是这次论述的上下文，也是不能不伴随记录的。我认为你刚刚的回复对我的这次论述的解读，非常适合放入`扩展认知.md`中，那个文件的本意，就是用户说的内容，AI对应的理解是怎样的，我认为你理解得很好。（逐字保存在 `{SRC_CLAUDE}` 第 2 条）
- parent: 不改变 Goal7 / MO3-COVERAGE-C；本会话不是 integrator 的研究单元

## load_receipt

本会话（上下文压缩之后）用 Read 全文读过下列文件；表中是准备载荷时的哈希前缀、字节与行数。四件套按固定顺序读完：核心认知（第 9 代全文；第 10 代新增三条另读，其余 51 条经生成器逐字核对保留）、方向追踪（索引加 5 片）、全景视野（索引加 8 片）、扩展认知（索引加 10 片）。

**公开降级**：`STATE.json`（约 1.48 MB）没有整体读入模型上下文；本事务触及的记录（`current_core`、`latest_session`、`A-COPUS-CORE-GENERATION-9-001`、`A-CORE-GENERATION-4-001`、`G-COPUS-CORE-GEN9-FOLLOWUPS-001`、`G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`、`A-RUSSELL-EXISTENCE-QUESTIONING-001`、`active`、`unresolved`、`execution_control` 的检查点指针）逐项读取，其余由 runtime 的 plan 与 prepare 做结构核对。

|path|sha256 前 16 位|bytes|lines|
|---|---|---|---|
{receipt}

## 做了什么

1. 两个来源文件入 `sources/prompts/`，文字由脚本从原始记录逐字复制（0102 对话存档；本会话的宿主记录），文首写明上下文与时间身份；curation v10；`scripts/audit/build_core_cognition.py --write` 生成第 10 代、manifest 与 transition；`verify_core_cognition.py` PASS_WITH_SCOPE（54 单元，51/51 旧单元逐字保留）。
2. 扩展认知新增第 011 片；全部原文块与核心认知逐字一致（准备脚本逐块比对）。
3. 方向追踪、全景视野只刷新 source_state_revision（290→291）与 projection_generation；内容未改。MEMORY/003 与 RESUME 各追加一行事实记录。STATE 登记 `{REC_CORE}`、`{REC_FOLLOW}` 与本 session。
4. 不做的事（及原因）：不改方向与全景的内容（用户本次没有要求；张力登记在 `{REC_FOLLOW}`）；不改 `rulings.md`；不改扩展认知第 010 片（第 011 片注明其一句的时间状态）；不改 README；不写共享证据矩阵。

|element_usage|本次用途与边界|
|---|---|
|核心认知与最高指示-Claude版|第 10 代全文；UR 的身份分层；不把判定写成定理|
|build_core_cognition 与 verify_core_cognition|生成与校验第 10 代；51 旧单元逐字保留|
|canonical runtime 与 writer|plan、prepare、checkpoint；单文件兼容审计；只认 canonical result|
|projection_edit|扩展认知索引与全部分片同载荷；方向、全景只改身份字段|
|verify_three_way_cognition 与 verify_governance_shards|结构校验；不证明语义|
|CG-001 目标本地索引与 relay|C-83 的证明与登记（不经本 checkpoint）|

验证命令与结果见 RUNS.json。无新数学主张经本 checkpoint 交付；C-83 属于 Claude 线目标本地索引。未推送。
"""


def runs_obj(snapshot: str) -> dict:
    return {
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "session_kind": "GOVERNANCE_CORE_GENERATION_AND_ESSAY_SHARD",
        "checkpoint_result": RESULT_REL,
        "base_snapshot": snapshot,
        "formal_runs": [],
        "related_goal_local_runs": {
            "note": "same session, registered in the Claude CG-001 goal-local index, not delivered through this checkpoint",
            "claim": "CG001-C-83",
            "runs": ["20260930-CG001-TRUNCATION-QUESTIONING-01", "20260930-CG001-TRUNCATION-QUESTIONING-NEG-01", "20260930-CG001-TRUNCATION-QUESTIONING-NEG-02"],
            "verification": "verify_cg001_run.py --rerun: PASS_WITH_SCOPE and two NEGATIVE_CONTROL_REJECTED_AS_EXPECTED, EXACT_EXIT_STDOUT_STDERR_MATCH",
            "index": CG001_INDEX,
        },
        "governance_runs": [
            {"tool": "scripts/audit/build_core_cognition.py",
             "command": f"--curation {CURATION} --transition-output {TRANSITION} --transition-from-ref 2199202f128e3573f23084bcb2dafb361f86930f --write",
             "status": "BUILT / COMPLETE_ADDITIVE_PRESERVING / mapping_count=51 / remainder=0", "generation": f"{GEN9}/51 -> {GEN10}/54"},
            {"tool": "scripts/audit/verify_core_cognition.py", "command": f"--curation {CURATION} --transition {TRANSITION}", "status": "PASS_WITH_SCOPE"},
            {"tool": PREPARE_SELF, "command": "--output <payload>", "status": "PREPARED"},
            {"tool": ".codex/tools/cognition_runtime.py", "command": "checkpoint --snapshot <base_snapshot> --payload <payload> --apply",
             "status": "CHECKPOINT_COMMITTED expected; only the canonical result.json proves it"},
        ],
        "new_math_claims": [],
        "math_status_change": "NONE",
        "push_policy": "no push by this session without the user's instruction",
        "note": "Core entry of the user's 2026-09-30 statements with context and the essay shard the user asked for; no mathematical claim is delivered by this checkpoint.",
    }


# ----------------------------------------------------------------------------------------------
# STATE
# ----------------------------------------------------------------------------------------------

MEMORY_003_ADD = (
    f"\n{SESSION_ID}：核心认知第 10 代（{GEN9}/51 → {GEN10}/54；新增 KC-000052 四句证据链就是非现实性悖论、KC-000053 项目目标不加“存在性”限定、"
    "KC-000054 UR 与芝诺的模式匹配；51/51 `PRESERVED_EXACT`、remainder=0）；扩展认知新增第 011 片（用户要求放入的 AI 解读）；"
    "方向追踪与全景视野只刷新 revision，内容未改；STATE 登记核心代记录与一个跟进项。revision 290→291。无新数学主张经本 checkpoint 交付。\n"
)

RESUME_ADD = (
    f"{SESSION_ID}：用户 2026-09-30 要求完整记录其 UR 论述并伴随记录上下文、把 Claude 的解读放入扩展认知后，核心认知第 10 代（{GEN10}，54 KC，"
    "KC-000052–KC-000054）已应用，扩展认知新增第 011 片。方向追踪与全景视野的内容未改；罗素线方向标签与证据身份的更新待用户与 integrator，"
    f"见 `{REC_FOLLOW}`。不改变当前阶段的 Goal7 / MO3-COVERAGE-C 队列。\n\n"
)


def state_edits(state: dict) -> None:
    session_path = f"{SESSION_REL}/SESSION.md"
    state["revision"] = PREV_REVISION + 1
    state["latest_session"] = SESSION_ID
    state["current_core"] = {
        "core_sha256": sha_file(CORE),
        "curation": CURATION,
        "curation_sha256": sha_file(CURATION),
        "generation": GEN10,
        "kc_count": 54,
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

    core_sources = [CORE, MANIFEST, CURATION, TRANSITION, SRC_CODEX, SRC_CLAUDE,
                    "scripts/audit/build_core_cognition.py", "scripts/audit/verify_core_cognition.py"]
    state["records"][REC_CORE] = {
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / COMPLETE_ADDITIVE_PRESERVING",
        "full_sources": core_sources,
        "kind": "core_generation_migration",
        "lifecycle_status": "CURRENT",
        "path": TRANSITION,
        "related_records": ["A-COPUS-CORE-GENERATION-9-001", SESSION_ID],
        "scope": ("Incrementally add three exact direct-user items of 2026-09-30 while preserving every generation-9 KC byte for byte: "
                  "KC-000052 (the user's reading, in a Codex session, of the Russell line's four-sentence evidence chain as a non-reality paradox), "
                  "KC-000053 (the project goal is HoTT's non-reality paradoxes, not qualified by 'existence'), "
                  "KC-000054 (the UR definition and pattern-matching with Zeno, Claude Code session eadb3381). "
                  "Supersedes A-COPUS-CORE-GENERATION-9-001 as the owner of the current core identity. "
                  "KC-000052/053 timestamps are upper bounds (first commit of dev-notes/0102 lines 428/513); KC-000054 uses the host receive time."),
        "source_hashes": hashes(core_sources),
        "status": "closed",
    }
    state["records"][REC_FOLLOW] = {
        "evidence_status": "PENDING_USER_ACTION / NOT_RUN",
        "full_sources": [session_path, CG001_RELAY, ESSAY_011],
        "kind": "governance_follow_up",
        "lifecycle_status": "OPEN_ISSUE",
        "path": session_path,
        "related_records": [REC_CORE, SESSION_ID, "A-RUSSELL-EXISTENCE-QUESTIONING-001"],
        "scope": ("Follow-ups left open by this checkpoint: (1) DIR-U-RUSSELL-EXISTENCE-QUESTIONING is labelled direction B, while KC-000052/053 read the "
                  "four-sentence chain as direction A and state that the project goal is not qualified by existence; KC-000050/051 still hold the existence "
                  "reading. The label (A primary, B primary or both) needs the user and the integrator (Claude relay R3 item 9). "
                  "(2) The Claude goal-local index now has C-77 to C-83 (non-halting written inside the kernel, neighbour controls, truncation control); "
                  "OUT-U-RUSSELL-UNIVERSE-QUESTIONING, A-RUSSELL-EXISTENCE-QUESTIONING-001, MEMORY/002 and essay shard 010 still say meta-level inference "
                  "(handoff W1, needs authorization). (3) 方向追踪 section 7 asks to sync rulings.md for new user corrections; KC-000053 was not synced "
                  "(not authorized in this checkpoint)."),
        "status": "open",
    }
    state["unresolved"].append(REC_FOLLOW)
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, f"{SESSION_REL}/RUNS.json", f"{SESSION_REL}/CORE_COGNITION_AUDIT.md", RESULT_REL, TRANSITION, CURATION, ESSAY_011],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV_SESSION, REC_CORE, REC_FOLLOW],
        "scope": ("Core generation-10 entry (KC-000052 to KC-000054) with context, and essay shard 011 carrying the AI reading the user asked for. "
                  "User-instructed on 2026-09-30; direction and result content unchanged; does not change the Goal7 / MO3-COVERAGE-C queue; no new mathematics."),
        "source_hashes": {},
        "status": "complete",
    }


# ----------------------------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--essay-template", type=Path, required=True)
    args = parser.parse_args()

    required = [CORE, MANIFEST, CURATION, TRANSITION, SRC_CODEX, SRC_CLAUDE, C83_CLAIM, CG001_INDEX, CG001_RELAY]
    missing = [p for p in required if not (ROOT / p).is_file()]
    if missing:
        raise SystemExit(f"EVIDENCE_MISSING:{missing}")

    state_path = ROOT / R.STATE
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if state.get("revision") != PREV_REVISION or state.get("latest_session") != PREV_SESSION:
        raise SystemExit(f"EXPECTED_REVISION_{PREV_REVISION}:{state.get('revision')}:{state.get('latest_session')}")
    for identity in (SESSION_ID, REC_CORE, REC_FOLLOW):
        if identity in state["records"]:
            raise SystemExit(f"RECORD_ALREADY_EXISTS:{identity}")

    plan = R.plan(ROOT, profile="governance", _allow_core_transition=CORE_TRANSITION)
    payloads = core_payloads()
    if list(payloads)[-3:] != ["KC-000052", "KC-000053", "KC-000054"] or len(payloads) != 54:
        raise SystemExit("CORE_NOT_GENERATION_10")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    for old, new in (
        (f"source_state_revision: {PREV_REVISION}", f"source_state_revision: {PREV_REVISION + 1}"),
        (f"projection_generation: 20260930-direction-{PREV_REVISION}", f"projection_generation: 20260930-direction-{PREV_REVISION + 1}"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    for old, new in (
        (f"source_state_revision: {PREV_REVISION}", f"source_state_revision: {PREV_REVISION + 1}"),
        (f"projection_generation: 20260930-outcome-{PREV_REVISION}", f"projection_generation: 20260930-outcome-{PREV_REVISION + 1}"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    essay = projection_edit.load(ROOT, R.ESSAY)
    essay_edits(essay, payloads, args.essay_template)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    m3 = "MEMORY/003 - 当前验证状态与顺序日志.md"
    if not memory["shards"][m3].endswith("\n"):
        memory["shards"][m3] += "\n"
    memory["shards"][m3] += MEMORY_003_ADD

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(resume, "## 历史停止点\n\n", "## 历史停止点\n\n" + RESUME_ADD)

    state_edits(state)

    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"
    texts: dict[str, str] = {path: (ROOT / path).read_text(encoding="utf-8") for path in R.MUTABLE}
    for document in (direction, panorama, memory, essay):
        texts[document["index_path"]] = document["index_text"]
        texts.update(document["shards"])
    texts[resume_path] = resume
    texts[session_path] = session_text()
    texts[audit_path] = audit_text()
    texts[runs_path] = json.dumps(runs_obj(plan["snapshot"]), ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[R.STATE] = json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n"

    original_blocks = verify_essay_originals(texts, payloads)
    created = {session_path, audit_path, runs_path, RESULT_REL, ESSAY_011}
    for label, body in (("audit", texts[audit_path]), ("session", texts[session_path]), ("essay-011", texts[ESSAY_011]),
                        ("memory", MEMORY_003_ADD + RESUME_ADD)):
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
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": PREV_REVISION + 1, "session_id": SESSION_ID,
                      "files": len(texts), "essay_original_blocks_verified": original_blocks}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
