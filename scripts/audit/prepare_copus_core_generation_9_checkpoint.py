#!/usr/bin/env python3
"""Prepare the checkpoint that registers core generation-9 and the two "ghost" lines.

Scope (user authorization of 2026-09-27, Cloud-Opus audit session: "入核和登记我现在就授权你，
立即完成所有剩余的你可以完成的工作"):

* core generation-9 (KC-000049 attribution correction, KC-000050 Russell principles P1-P3,
  KC-000051 second batch) was already built on disk by scripts/audit/build_core_cognition.py;
  this checkpoint moves STATE.current_core to it (canonical core_transition path of the runtime);
* the essay (扩展认知) gets the attribution correction (shards 003, 005, 009) and a new shard 010;
* 方向追踪 and 全景视野 register the Zeno line (A7), the Russell line, the audit of the GLM line and
  the attribution correction; MEMORY, RESUME and STATE follow;
* the session bundle (SESSION.md, RUNS.json, CORE_COGNITION_AUDIT.md) is written in the same
  transaction, exactly as the canonical writer requires.

The script only builds the payload; it writes nothing into the repository.  Apply it with
.codex/tools/cognition_runtime.py checkpoint --snapshot <printed snapshot> --payload <output> --apply
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

SPEC = importlib.util.spec_from_file_location("runtime_copus9", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))
import projection_edit  # noqa: E402

BSPEC = importlib.util.spec_from_file_location("builder_copus9", SCRIPTS / "build_core_cognition.py")
assert BSPEC and BSPEC.loader
B = importlib.util.module_from_spec(BSPEC)
BSPEC.loader.exec_module(B)

SESSION_ID = "S-GOV-20260930-COPUS-CORE-GENERATION-9-REGISTRATION"
PREV_SESSION = "S-RES-20260924-MO3-C-B02"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"

CORE = "核心认知.md"
MANIFEST = "核心认知.manifest.json"
CURATION = "scripts/audit/core-cognition-curation-v9.json"
TRANSITION = "audit/core-cognition-generation-9-transition-20260930.json"
GEN8 = "core-cognition-generation-8"
GEN9 = "core-cognition-generation-9"
SRC_ATTR = "sources/prompts/Claude-归因是正题-用户原文-20260924.md"
SRC_P13 = "sources/prompts/Claude-罗素原则P1至P3-用户原文-20260926.md"
SRC_B2 = "sources/prompts/GLM-算符先行于存在性落定-用户原文-20260926.md"
DOC01 = "docs/社区审计提交/01-芝诺悖论的幽灵.md"
DOC02 = "docs/社区审计提交/02-罗素悖论的幽灵.md"
DOCREADME = "docs/社区审计提交/README.md"
COPUS = "Cloud-Opus审计并补完GLM"
RECORD15 = f"{COPUS}/15-入核与登记记录.md"

ESSAY_INDEX = "扩展认知.md"
ESSAY_003 = "扩展认知/003 - 芝诺、圆环、ASK 与两种方向.md"
ESSAY_005 = "扩展认知/005 - 表达界限、文章作为起点与编写说明.md"
ESSAY_009 = "扩展认知/009 - 从可疑前提到针对性过程.md"
ESSAY_010_TITLE = "论域元素的存在性追问：罗素线的两批原文"
ESSAY_010 = f"扩展认知/010 - {ESSAY_010_TITLE}.md"

CORE_TRANSITION = {
    "from_generation": GEN8,
    "to_generation": GEN9,
    "manifest": MANIFEST,
    "transition": TRANSITION,
}

REC_CORE = "A-COPUS-CORE-GENERATION-9-001"
REC_A7 = "A-A7-INFINITE-COHERENCE-001"
REC_RUSSELL = "A-RUSSELL-EXISTENCE-QUESTIONING-001"
REC_FOLLOW = "G-COPUS-CORE-GEN9-FOLLOWUPS-001"

AUTHORIZATION = (
    "User 2026-09-27 (Cloud-Opus audit session) explicitly authorized core entry and registration and all remaining "
    "completable work: 入核和登记我现在就授权你，立即完成所有剩余的你可以完成的工作。"
    "The attribution-correction patch (.claude/relay/20260924-attribution-correction/) was chosen by the user on 2026-09-24."
)


PATH_PREFIXES = ("HoTT/", "Cloud-Opus", "docs/", ".claude/", "sources/", "GLM-5.3-Flash/", "scripts/", ".codex/", "扩展认知/", "方向追踪/", "全景视野/", "MEMORY/")


def check_paths(label: str, text: str, extra_existing: set[str] = frozenset()) -> None:
    """Every backticked repository path in generated text must exist (or be created by this checkpoint)."""
    missing = []
    for match in re.finditer(r"`([^`\n]+)`", text):
        token = match.group(1).strip()
        if not token.startswith(PATH_PREFIXES) and token not in ("核心认知.md", "方向追踪.md", "全景视野.md", "扩展认知.md", "rulings.md", "最高指示-Claude版.md"):
            continue
        if "/" not in token and not token.endswith((".md", ".json", ".py", ".sh", ".agda", ".lean")):
            continue  # a tag or identifier, not a path
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
    body = "\n".join("> " + line for line in payload.split("\n"))
    return f"<!-- original:{kc}:begin -->\n{body}\n<!-- original:{kc}:end -->"


def verify_essay_originals(texts: dict[str, str], payloads: dict[str, str]) -> int:
    """Every `original:KC-…` block of the essay must equal the core payload byte for byte."""
    total = 0
    bad = []
    for path, body in texts.items():
        if not path.startswith("扩展认知/"):
            continue
        for m in re.finditer(r"<!-- original:(KC-\d{6}):begin -->\n(.*?)\n<!-- original:\1:end -->", body, re.S):
            total += 1
            lines = []
            for line in m.group(2).split("\n"):
                lines.append(line[2:] if line.startswith("> ") else ("" if line == ">" else "!!" + line))
            if "\n".join(lines) != payloads[m.group(1)]:
                bad.append((path, m.group(1)))
    if bad:
        raise SystemExit(f"ESSAY_ORIGINAL_BLOCK_MISMATCH:{bad}")
    return total


def core_payloads() -> dict[str, str]:
    return B.parse_core_payloads((ROOT / CORE).read_text(encoding="utf-8"))


# ----------------------------------------------------------------------------------------------
# essay
# ----------------------------------------------------------------------------------------------

def essay_edits(essay: dict, payloads: dict[str, str]) -> None:
    sh = essay["shards"]

    # P6 (attribution correction, essay 003): the paragraph after the KC-000005 original block.
    old6 = ("这句话保护着发现工作。研究当然需要列清所用前提，但不必在看到现象之前，就把唯一病因、最终本体解释和完整修复全部解决。"
            "应当先构造一个真正值得解释的困难，确定它确实发生在所声明的范围，再讨论它最终指向哪个前提。")
    new6 = (
        "这句话当时保护的是发现工作：不必在看到现象之前，就把唯一病因、最终本体解释和完整修复全部解决。"
        "2026-09-24，提出者本人修正了它的工作次序效力：\n\n"
        + quote_block("KC-000049", payloads["KC-000049"])
        + "\n\n[原文出处](/Volumes/D/HoTT_AI_HANDOFF_20260911/sources/prompts/Claude-归因是正题-用户原文-20260924.md:9)\n\n"
        "修正之后，“先发现”只保留一层意思：没有现象时，不拿病因猜测去否决候选。困难一旦显出，归因就是正题，要与提出者仔细讨论："
        "列出候选前提（理论规则、可选公理、库与实现、解释桥、现实侧前提），写出彼此竞争的归因，说明什么证据或对照能区分它们，"
        "并把自己的判断连同身份交给提出者检验。KC-000005、KC-000020 的原话作为历史记录保留；其中“下一个故事”一句不再作为工作次序。"
    )
    sh[ESSAY_003] = replace_once(sh[ESSAY_003], old6, new6)

    # P7 (essay 009)
    old7 = "最后再讨论理论、公理、使用与实现的归因。这样的顺序与“先找到现象、后定最终病因”相容。"
    new7 = ("现象一旦显出，就与提出者一起讨论理论、公理、使用与实现的归因（KC-000049）。"
            "“先找到现象”只意味着不拿病因猜测否决尚未显出现象的候选，不意味着把归因推迟到研究之后。")
    sh[ESSAY_009] = replace_once(sh[ESSAY_009], old7, new7)

    # P8 (essay 005)
    old8 = "能够复述“先发现后归因”，却要求一个候选起步时交齐最终归因，那么"
    new8 = ("能够复述“先发现、再与提出者一起归因”，却要求一个候选起步时交齐最终归因，"
            "或者反过来，在现象已经显出之后仍以“下一个故事”搁置归因（KC-000049），那么")
    sh[ESSAY_005] = replace_once(sh[ESSAY_005], old8, new8)

    # new shard 010
    sh[ESSAY_010] = essay_shard_010(payloads)

    idx = essay["index_text"]
    idx = replace_once(idx, "baseline: core-cognition-generation-8", f"baseline: {GEN9}")
    idx = replace_once(idx, "本文根据《核心认知.md》generation-8 的全部 48 段原文综合写成", "本文根据《核心认知.md》generation-9 的全部 51 段原文综合写成")
    idx = replace_once(idx, "本索引 + 下方 9 个分片", "本索引 + 下方 10 个分片")
    idx = replace_once(idx, "last_shard: 扩展认知/009 - 从可疑前提到针对性过程.md", f"last_shard: {ESSAY_010}")
    row9 = "| 009 | [从可疑前提到针对性过程](<扩展认知/009 - 从可疑前提到针对性过程.md>) | KC47–48完整原文、敏感过程、模型保真及机器统观教训 | current |\n"
    row10 = (f"| 010 | [{ESSAY_010_TITLE}](<{ESSAY_010}>) | 论域元素的存在性是理论无法拒绝的问题；算符先于存在性落定的次序；"
             "追问在现实中不停机即成功——用户 2026-09-26 的两批原文（KC-000050–KC-000051）；归因修正（KC-000049）见第 003 片 | current |\n")
    idx = replace_once(idx, row9, row9 + row10)
    essay["index_text"] = idx


def essay_shard_010(payloads: dict[str, str]) -> str:
    return f"""<!-- governance-shard:v2
logical_id: CORE-ESSAY
shard_id: 010
index: ../扩展认知.md
-->

# {ESSAY_010_TITLE}

本片展开用户 2026-09-26 同日提出的两批原文（KC-000050、KC-000051）。它们把罗素悖论读成一个关于“论域元素的存在性”的问题，并给出一个具体的成功判据。本片不把这个读法升级成定理；它只说明这个读法怎样改变“要找什么”和“怎样问”。用户 2026-09-24 关于归因的修正（KC-000049）见第 003 片。

## 理论无法拒绝自己论域元素的存在性问题

{quote_block("KC-000050", payloads["KC-000050"])}

[原文出处](/Volumes/D/HoTT_AI_HANDOFF_20260911/sources/prompts/Claude-罗素原则P1至P3-用户原文-20260926.md:13)

这段话分三步：理论有论域；论域元素的存在性是理论必须面对的问题，别的问题理论可以拒绝，这一个不能拒绝；对一个论域元素存在性的追问，如果在现实中会引发无法停机的计算（无限追溯），就是成功。

它和前面几段是一条线。KC-000018 问的是“S 都无法构建出来，存在性都没有，何以归类为集合”，这里从 S 推到任何论域元素；KC-000012、KC-000013 里的 ASK 是“先问这个问题合不合法、做不做得完”，这里把它用在“存在”上。

有三处不要读窄。第一，不要把它读成“宇宙没有截断层级是已知定理”或“HoTT 有模型，所以没有问题”：这些是被检验的材料，不是答案。第二，“追问”是一个在现实中会被执行的过程，不是一个静态的性质；把追问落实成具体的过程，是一步解释，用户没有改写它，也没有被裁定。第三，成功判据说的是“在现实中会引发无法停机的计算”，它不要求理论内部出现矛盾（KC-000010）。

## 算符先于存在性落定

{quote_block("KC-000051", payloads["KC-000051"])}

[原文出处](/Volumes/D/HoTT_AI_HANDOFF_20260911/sources/prompts/GLM-算符先行于存在性落定-用户原文-20260926.md:11)

第二批在第一批之上多了三件事。

- 次序：罗素悖论里，S 的存在性还没有确定，S 就已经被放进朴素集合论的算符里讨论了（去问别的集合是不是它的元素）。用户把这称为数学上不合理的次序：只有先确定了 S 是论域里的元素，才该允许对它做算符操作。
- 静与动两种读法：这样一通操作之后，结局可以静态地读成“S 不存在”，也可以动态地读成“对 S 的存在性，也就是它是不是论域元素的身份的合法性追溯，是永不停机的计算”。用户要的是动态读法。
- 成功判据落到 HoTT：如果对 HoTT 论域元素的存在性的追问，在现实中会引发无法停机的计算（无限追溯），那么我们就成功了。

两批合在一起，改变了要找的东西：不是在理论内部找矛盾，而是找一个理论不能不面对的论域元素，看理论是不是在它的存在性还没有落定时，就已经让算符在它上面运转；再看对它的存在性追问，落成现实里的过程以后，是不是停不下来。

## 这条线走到哪里

这两批原文所触发的具体研究，是把宇宙当作 HoTT 的论域元素，并逐层追问它的成员以什么方式相同。进展、机器证明的范围和没有证明的事，由 `方向追踪.md` 的 `DIR-U-RUSSELL-EXISTENCE-QUESTIONING` 与 `全景视野.md` 的 `OUT-U-RUSSELL-UNIVERSE-QUESTIONING` 拥有，完整叙述见 `docs/社区审计提交/02-罗素悖论的幽灵.md`。本片只留三点提醒。

- “对每一层都答否”是机器证明的事实；“所以追问永不停机”是由它加追问过程的定义与理论一致性得出的元层推论，没有单独机器化。
- 把“追问存在性”落实成“逐层问成员以什么方式相同”，以及“一个总体要算存在，它的相同必须在某一层落定”这一现实侧前提，是待用户裁定、待社区审计的解释与哲学前提，不是已证结论。
- 本片不认证模型对原文的理解，也不构成数学结论。
"""


# ----------------------------------------------------------------------------------------------
# direction / panorama rows
# ----------------------------------------------------------------------------------------------

DIR_ROWS = [
    "| `DIR-U-A7-INFINITE-COHERENCE` | 芝诺面（A 向，无穷相干）：单价性把“相同”从事实改成结构；半单纯结构的一行定义在“相同是事实”的世界一步完成，在 HoTT 里每补一级相干都长出下一级；统一定义在书式 HoTT 内部写不出，是公开的开放问题。判别它是不是“每步可行、缺统一方法”的芝诺式完不成 "
    "| 用户方向（KC-000003／010／022／024／044／047／048）；用户 2026-09-27 判定“复活了芝诺悖论的幽灵”；Claude Code 研究会话 CG-001 至 CG-003（2026-09-26）；Cloud-Opus 审计会话的 Linux 重放与整理（2026-09-27） "
    "| `ACTIVE_USER_DIRECTION / USER_VERDICT_REVIVED_20260927 / COMMUNITY_AUDIT_PENDING` "
    "| `ZENO`, `PARADOX_DISCOVERY`, `THEORY_ECONOMY`, `ABSTRACTION_AND_NEGATION`, `HOTT_OBJECT` "
    "| `OUT-U-A7-INFINITE-COHERENCE` "
    "| 交社区审计：六边形与 P₄ 相干是否标准、文献状态、“每步可行缺统一方法”算不算芝诺式完不成；书式 HoTT 内出现统一定义则撤回强形式；不可能性未证明，是否升为条件式合格命中由用户裁定，AI 不自证 "
    "| `docs/社区审计提交/01-芝诺悖论的幽灵.md`；`.claude/思考与发现/` 的 CN-035、CN-037；`.claude/goals/CG-001-targeted-overview/证据索引.md` 的 C-62 至 C-72；`Cloud-Opus审计并补完GLM/证据索引.md` 4.4、4.5 |\n",

    "| `DIR-U-RUSSELL-EXISTENCE-QUESTIONING` | 罗素面（B 向，论域元素的存在性追问）：宇宙是 HoTT 不能不放进论域的元素（单价性是关于它的陈述）；把“追问其存在性”落实为逐层问“成员以什么方式相同”，最低宇宙对每一层都答“否”（机器证明），追问永不停机（元层推论）；HoTT 却用形成规则一次交出它，算符从一开始就在其上运转。解释桥与“存在要求落定”是待裁定的哲学前提 "
    "| 用户罗素原则 P1–P3 与第二批原文（KC-000050／051）及 KC-000012／013／014／016／018／022／048；用户 2026-09-27 判定“复活了罗素悖论的幽灵”；Claude Code 研究会话 CG-001（C-63、C-71 至 C-76）；GLM-5.3-Flash 平行工作；Cloud-Opus 审计与补完（2026-09-27） "
    "| `ACTIVE_USER_DIRECTION / USER_VERDICT_REVIVED_20260927 / BRIDGE_AND_EXISTENCE_PREMISE_UNADJUDICATED` "
    "| `RUSSELL`, `EXISTENCE_NEGATION_DUALITY`, `COMPUTATIONAL_LEGITIMACY`, `ASK`, `BEING_AND_BECOMING`, `PARADOX_DISCOVERY`, `HOTT_OBJECT` "
    "| `OUT-U-RUSSELL-UNIVERSE-QUESTIONING`、`OUT-U-COPUS-GLM-AUDIT` "
    "| 交社区审计：解释桥（追问存在性即逐层问成员以什么方式相同）、现实侧前提（存在要求落定）、对“有限证明即回答”的回应；未做：元层推论（全称否定加一致性推出追问不停）的单独机器化；未发生：外部独立复核（`Cloud-Opus审计并补完GLM/13-外部复核请求.md`）、Terra 对 019／020 的回应 "
    "| `docs/社区审计提交/02-罗素悖论的幽灵.md`；`Cloud-Opus审计并补完GLM/14-罗素面终局判词.md`；`.claude/思考与发现/` 的 CN-038、CN-039；`GLM-5.3-Flash/罗素线-平行工作索引.md` |\n",

    "| `DIR-G-ATTRIBUTION-IS-MAIN-TOPIC` | 归因是要与用户仔细讨论的正题：现象显出后，直接展开候选前提（理论规则、可选公理、库与实现、解释桥、现实侧前提）、竞争归因、能区分它们的证据与带身份的判断；KC-000005、KC-000020 中“下一个故事”一句不再作为工作次序，原话作为历史保留 "
    "| 用户 2026-09-24 修正（KC-000049）；Claude 起草的归因修正补丁（`.claude/relay/20260924-attribution-correction/`），用户选定“保留原话并加修正”，2026-09-27 授权执行 "
    "| `ACTIVE_USER_DIRECTION` "
    "| `RESEARCH_METHOD`, `PARADOX_DISCOVERY` "
    "| `OUT-TOP-ATTRIBUTION-CORRECTION-APPLIED` "
    "| 每个已有现象的候选，按“候选前提、竞争归因、区分证据、判断与身份”四件事写归因；KC-000005／020 是否从当前核心删去由用户决定（当前保留）；`.codex/skills/hott-paradox-search-sop/SKILL.md` 第 119 行的“先发现后归因”措辞，待在用户本机通过框架自维护 Gate 后修订 "
    "| `核心认知.md` 的 KC-000049；`扩展认知/003 - 芝诺、圆环、ASK 与两种方向.md`；`rulings.md`；`Cloud-Opus审计并补完GLM/15-入核与登记记录.md` |\n",
]

OUT_ROWS = [
    "| `OUT-U-A7-INFINITE-COHERENCE` | 芝诺线（无穷相干）的正反照与实例：Lean 4（相等证明唯一）中六边形自动成立；Cubical Agda 中同一行定义接受不相干数据（圆周上两路线绕 1 圈与 2 圈），补六边形后补法不唯一、下一级（P₄）可失败；各层是集合时第一级、各层是群胚时第二级自动成立；有限层机器检查到第 5 层；宇宙与 hSet 宇宙都不是集合；玩具语法的自解释两难（缩影） "
    "| `DIR-U-A7-INFINITE-COHERENCE` "
    "| Claude Code 研究会话 CG-001 至 CG-003 的原运行（macOS，2026-09-26）；Cloud-Opus 的 16 个 Linux 重放与 5 个 Lean 补充控制（2026-09-27） "
    "| `FORMAL_CHECKED_WITH_SCOPE / CROSS_PLATFORM_REPLAYED / NOT_IN_PROOF_VERSION_CLOSURE_REGISTRY` "
    "| 01 稿附录 A 所列形式命题在 Cubical Agda 2.8.0（cubical 0.9）与 Lean 4.34.0 中由内核检查通过并各有负控制；Linux 重放与 macOS 原收据（Agda 逐行、Lean 逐字节）一致；“后退第一、二级在 HoTT 出现而在 UIP 中消失”是实例级事实 "
    "| 不证明半单纯类型在书式 HoTT 中不可定义（开放问题）；不证明 HoTT 不一致；“各层是 t 层补 t+1 级”的一般形式是元层论证；Lean 两条是 UIP 世界命题；用户判定是判定不是定理；Lean 原负控制由细化器而非内核拒绝，已补内核级对照 "
    "| `docs/社区审计提交/01-芝诺悖论的幽灵.md` 附录 A 至 D；`Cloud-Opus审计并补完GLM/证据索引.md` 4.4、4.5；`HoTT/CLAIM_EVIDENCE_MATRIX.md` 末节 |\n",

    "| `OUT-U-RUSSELL-UNIVERSE-QUESTIONING` | 罗素线：宇宙存在性追问的三级阶梯——UIP 世界的 `Type` 第一步停（C-72）；HoTT 的 `hSet ℓ-zero` 第二步停（C-71 加 C-76 上界，另有 Kraus–Sattler 5.10 在 n=0 的独立路线 COPUS-KS-C06）；HoTT（含高阶归纳类型）的 `Type ℓ-zero` 对每个 m 不在第 m 层落定（C-75）；不用高阶归纳类型时，Kraus–Sattler 5.9／5.10 对一般 n 的重放（COPUS-KS-C01 至 C05）与名称级无 HIT 证书；“追问永不停机”是元层推论 "
    "| `DIR-U-RUSSELL-EXISTENCE-QUESTIONING` "
    "| Claude Code 研究会话 CG-001 的原运行（macOS，2026-09-26）；GLM-5.3-Flash 平行工作；Cloud-Opus 的重放、补完与名称级证书（2026-09-27） "
    "| `FORMAL_CHECKED_WITH_SCOPE / META_INFERENCE_NOT_MACHINIZED / BRIDGE_AND_EXISTENCE_PREMISE_UNADJUDICATED` "
    "| 三份目录各自的精确命题由内核检查通过并各有负控制；最低宇宙“每一层都答否”是机器事实；“追问永不停”是由它加追问过程 Q 的定义与理论一致性得出的元层推论（立方类型论有立方集合模型，来源转述） "
    "| 不证明 HoTT 不一致；“永不停机”的主语只是过程 Q，不是证明器、一致性或单个成员；不证明“高阶归纳类型对单个宇宙的永不停是必要的”（来源级）；解释桥与“存在要求落定”由用户裁定与社区审计；用户判定是判定不是定理 "
    "| `docs/社区审计提交/02-罗素悖论的幽灵.md` 附录 A；`Cloud-Opus审计并补完GLM/14-罗素面终局判词.md`；`HoTT/CLAIM_EVIDENCE_MATRIX.md` 末节 |\n",

    "| `OUT-U-COPUS-GLM-AUDIT` | Cloud-Opus 对 GLM 罗素线的“声明层与证明层”逐命题审计与补完：查出一处见证错位（GLM-R1-C02 的 `valReflT/F` 只陈述端点定义性相等）、一处负控制失效（GLM-R3-C01 的原负控制死在作用域检查）、若干越界读法；补上修复件、名称级高阶归纳类型证书（HITScan）、Kraus–Sattler 5.9／5.10 的一般 n 重放、Lean 补充控制；自查又查出 C-65 与 C-72 的 Lean 负控制由细化器而非内核拒绝并补了内核级对照；46 个 `20260927-COPUS-*` 运行逐字节重放一致（23 接受、23 按预期被拒） "
    "| `DIR-U-RUSSELL-EXISTENCE-QUESTIONING`、`DIR-U-A7-INFINITE-COHERENCE` "
    "| Cloud-Opus 审计会话（Claude Code 云端，2026-09-27 至 2026-09-30） "
    "| `VERIFIED_WITH_SCOPE / SELF_AUDITED / EXTERNAL_REVIEW_NOT_YET` "
    "| 审计发现与修正逐条可回溯；机器运行在 Linux 上可复现 "
    "| 不是独立审计：没有外部复核，且被重放的一部分（芝诺线）是同一模型家族的研究；外部复核请求已成文但未发生；Terra 未回应 019／020；不证明数学结论的哲学正当性 "
    "| `Cloud-Opus审计并补完GLM/README.md`；`Cloud-Opus审计并补完GLM/13-外部复核请求.md`；`Cloud-Opus审计并补完GLM/证据索引.md`；`Cloud-Opus审计并补完GLM/10-T2审计集/` |\n",

    "| `OUT-TOP-ATTRIBUTION-CORRECTION-APPLIED` | 用户 2026-09-24 归因修正的落实：入核为 KC-000049（核心认知第 9 代，同时入核 KC-000050／051）；扩展认知 003／005／009 三片原位修订并新增第 010 片；`rulings.md` 相应一句修订；`最高指示-Claude版.md` 升至 v1.2；KC-000005／020 原话保留；`.codex/skills/hott-paradox-search-sop/SKILL.md` 与时间审查地图未改（前者须先过框架自维护 Gate，后者不在本仓库） "
    "| `DIR-G-ATTRIBUTION-IS-MAIN-TOPIC` "
    "| 用户 2026-09-24 修正与 2026-09-27 授权；`.claude/relay/20260924-attribution-correction/` 补丁 "
    "| `VERIFIED_WITH_SCOPE / PATCH_PARTIALLY_APPLIED` "
    "| 核心认知第 9 代由规范生成器重建并经 `verify_core_cognition.py` 校验，48 条旧单元逐字保留；扩展认知的原文块与核心认知逐字一致 "
    "| 不证明工作姿态已改变（未来行为未认证）；未应用的两项补丁见方向行；不改 KC-000005／020 "
    "| `核心认知.md`；`核心认知.manifest.json`；`audit/core-cognition-generation-9-transition-20260930.json`；`Cloud-Opus审计并补完GLM/15-入核与登记记录.md` |\n",
]

PANORAMA_008_ADD = """
18. `A-A7-INFINITE-COHERENCE-001`：芝诺线未完成——统一定义的不可能性（开放问题，未证明）；社区对六边形与 P₄ 相干的标准性、文献状态、“每步可行缺统一方法”算不算芝诺式完不成的审计；一般“各层是 t 层补 t+1 级”的元层论证未机器化；Terra 对 019／020 的回应未发生。
19. `A-RUSSELL-EXISTENCE-QUESTIONING-001`：罗素线未完成——解释桥与“存在要求落定”由用户裁定、待社区审计；“追问永不停机”的元层推论未单独机器化；不用高阶归纳类型时单个宇宙的相容性只有来源级支持；外部独立复核（`Cloud-Opus审计并补完GLM/13-外部复核请求.md`）未发生。
20. `G-COPUS-CORE-GEN9-FOLLOWUPS-001`：治理跟进——`.codex/cognition/CORE_COGNITION.schema.json` 的平台枚举需加入 `Claude` 与 `GLM`；`.codex/skills/hott-paradox-search-sop/SKILL.md` 第 119 行措辞；二者都属框架改动，须在用户本机通过全局自维护 Gate（云端会话无此 Gate，未改）；`verify_projection_freshness.py` 在本次之前已失败（旧合并来源哈希与 2026-09-12 新鲜收据过期），未处理；两个标签 `Cloud-Opus对GLM的审计`、`Cloud-Opus工作完成` 因云端 git 通道只放行分支推送而未推送。
"""

MEMORY_001_ADD = """
## 用户判定与并行审计线（2026-09-27 至 2026-09-30）

用户 2026-09-27 判定：本 repo 复活了芝诺悖论的幽灵和罗素悖论的幽灵，并且找到了 HoTT 理论的问题（研究发起人的判定，不是数学定理；不宣称 HoTT 不一致）。两条线的精确状态见 `方向追踪.md` 的 `DIR-U-A7-INFINITE-COHERENCE`、`DIR-U-RUSSELL-EXISTENCE-QUESTIONING` 与 `全景视野.md` 的对应结果；供社区审计的两份稿子在 `docs/社区审计提交/`。用户 2026-09-24 的归因修正与 2026-09-26 的两批罗素原文已入核（核心认知第 9 代，KC-000049–KC-000051，48 条旧单元逐字保留）。归因是正题：现象显出后直接展开候选前提、竞争归因、区分证据与带身份的判断。这一段不改变上面 Goal7 / MO3-COVERAGE-C 的执行队列。
"""

MEMORY_002_ADD = (
    "- 芝诺线与罗素线的机器证据上限：附录所列形式命题在 Cubical Agda 2.8.0 与 Lean 4.34.0 中由内核检查通过并在 Linux 上重放一致（46 个 `20260927-COPUS-*` 运行）；"
    "没有证明半单纯类型在书式 HoTT 中不可定义，没有证明 HoTT 不一致；“追问永不停机”是元层推论，不是机器事实；解释桥与“存在要求落定”未被裁定；外部独立复核未发生。\n"
)

MEMORY_003_ADD = (
    f"\n{SESSION_ID}：核心认知第 9 代（{GEN8}/48 → {GEN9}/51；新增 KC-000049 归因修正、KC-000050 罗素原则 P1–P3、KC-000051 第二批原文；48/48 `PRESERVED_EXACT`、remainder=0）；"
    "规范生成器新增 `Claude`、`GLM` 两个来源平台（框架 Schema 的平台枚举未改，见 `G-COPUS-CORE-GEN9-FOLLOWUPS-001`）；扩展认知 003／005／009 原位修订、新增第 010 片；"
    "方向追踪与全景视野登记芝诺线、罗素线、对 GLM 的审计与归因修正；STATE 登记三条记录与一个跟进项。revision 289→290。无新数学主张；未 push 的只有两个标签。\n"
)

RESUME_ADD = (
    f"{SESSION_ID}：用户 2026-09-27 授权入核与登记后，核心认知第 9 代（{GEN9}，51 KC，KC-000049–KC-000051）已应用，扩展认知新增第 010 片并修订 003／005／009，"
    "方向追踪与全景视野登记芝诺线与罗素线及对 GLM 的审计，STATE 登记对应记录。不改变当前阶段的 Goal7 / MO3-COVERAGE-C 队列。"
    "供社区审计的两份稿子在 `docs/社区审计提交/`；应用记录见 `Cloud-Opus审计并补完GLM/15-入核与登记记录.md`。\n\n"
)


# ----------------------------------------------------------------------------------------------
# audit
# ----------------------------------------------------------------------------------------------

SHORT = {
    "00": "00-工作日志.md", "01": "01-工具链与复现.md", "02": "02-断裂审计-逐命题（D1）.md",
    "03": "03-R1-HIT依赖闭包判定.md", "04": "04-Q7-数学终审逐行核验.md", "05": "05-R2至R8处置.md",
    "06": "06-一般n外归纳（D3）.md", "07": "07-悖论卷宗-最终完整版（D4）.md", "08": "08-一页裁定书（D6）.md",
}
AUDIT_SET = f"{COPUS}/10-T2审计集/Cloud-Opus本会话审计集"


def expand_paths(text: str) -> str:
    def repl(m: re.Match) -> str:
        key = m.group(1)
        return f"{COPUS}/{SHORT[key]}" if key in SHORT else m.group(0)

    text = re.sub(r"`(0[0-8])`", repl, text)
    text = text.replace("`11-…json`", f"{COPUS}/11-收据核验结果.json")
    text = text.replace("`证据索引.md`", f"{COPUS}/证据索引.md")
    text = text.replace("`附件/`", f"{COPUS}/附件/")
    text = text.replace("004 片", f"{AUDIT_SET}/004 - 已走过的路与即将作出的选择.md")
    text = text.replace("ks-universe-tower `CLAIM.md`", "HoTT/formal/cloud-opus-glm-audit/ks-universe-tower/CLAIM.md")
    text = text.replace("GN-002 修订块三", "GLM-5.3-Flash/思考与发现/ 中 GN-002 的修订块三")
    text = text.replace("策略快照附录四 ③", "GLM-5.3-Flash/策略快照/20260926-D2后罗素线策略-大白话快照.md 附录四 ③")
    text = text.replace("`11-…json`；", f"{COPUS}/11-收据核验结果.json；")
    return text


OVERRIDES: dict[str, tuple[str, str, str, str]] = {
    "KC-000003": ("合取前提与稠密过程", "ALIGNED",
                  "芝诺线把同一套反证推理用到另一个前提上：理论为了好用把“相同是落定的事实”改成结构，这个非现实前提作为合取推断里的一项，推出现实里没有的完成困难；它没有检验稠密性本身。证据：docs/社区审计提交/01-芝诺悖论的幽灵.md 第 1、5 节",
                  "回到稠密性或圆环的原问题时再触及；若把芝诺线说成对稠密性的回答，判偏航"),
    "KC-000005": ("先找悖论，后作归因", "CORRECTED",
                  "用户 2026-09-24 的修正（KC-000049）改变了“至于悖论作为矛盾，它到底是否定了哪个前提，那是未来的下一个故事”一句的工作次序效力：现象已有，就直接展开归因。两份社区稿按“候选前提、竞争归因、区分证据、判断与身份”四件事写归因，原话在核心认知里保留。证据：docs/社区审计提交/01-芝诺悖论的幽灵.md 第 7 节；docs/社区审计提交/02-罗素悖论的幽灵.md 第 9 节；扩展认知/003 - 芝诺、圆环、ASK 与两种方向.md 的 KC-000049 原文块",
                  "KC-000005 与 KC-000020 是否从当前核心删去由用户决定；若再有人以“下一个故事”推迟已有现象的归因，判偏航"),
    "KC-000019": ("合取真值与稠密空间", "ALIGNED",
                  "同 KC-000003：芝诺线借用“全真才真、缺一项则不定”的合取结构，把被改动的前提换成“相同是落定的事实”，没有检验稠密空间本身。证据：docs/社区审计提交/01-芝诺悖论的幽灵.md 第 5 节",
                  "回到稠密空间时再触及"),
    "KC-000020": ("悖论反证、运动量子化、HoTT 时间怀疑", "CORRECTED",
                  "同 KC-000005：其中“那是未来的下一个故事”一句的工作次序效力被 KC-000049 修正，本轮不推迟归因；运动量子化本身本轮不涉及。证据：同 KC-000005",
                  "同 KC-000005"),
    "KC-000025": ("自指型为何难找", "ALIGNED",
                  "芝诺线的玩具语法（编号 C-67）是自解释两难的缩影，范围已收窄（其 (b) 支比真实语法强，更公平的障碍是“目标必须是集合”）；罗素线把 GLM 的自指格只当边界，不当罗素面。证据：HoTT/formal/claude-cg001/self-interpretation/REVISIONS.md",
                  "做真实语法的自解释构造时再触及"),
    "KC-000047": ("经济性与普适性的理想抽象", "ALIGNED",
                  "两条线都从“理论为了好用改掉了什么”出发：芝诺线盯“相同是事实”被改成结构，罗素线盯“宇宙一次交出”；各自写出收益、被改动的条件、专门碰它的过程与观察。证据：docs/社区审计提交/ 两份稿子的第 0–3 节",
                  "若换一个与被改动条件无关的普通过程也得到同样的困难，则靶点未被敏感地检验"),
    "KC-000048": ("针对可疑前提设计过程", "ALIGNED",
                  "两条线的过程都专门碰被改动的条件：逐层补相干；逐层问成员以什么方式相同；用 Lean 与去掉高阶归纳类型的对照，以及负控制，隔离靶条件。证据：docs/社区审计提交/ 两份稿子的第 4 节与附录 B",
                  "若过程只改了名字而靶条件未变，则判换题"),
    "KC-000049": ("归因是要与用户仔细探讨的正题", "ALIGNED",
                  "本轮把它入核（核心认知第 9 代），并落实到两份社区稿的归因节、扩展认知 003／005／009、rulings、最高指示-Claude版 v1.2；归因不再推迟。证据：核心认知.md 的 KC-000049；docs/社区审计提交/01-芝诺悖论的幽灵.md 第 7 节；docs/社区审计提交/02-罗素悖论的幽灵.md 第 9 节",
                  "用户决定 KC-000005／020 的处置；若日后又把归因写成“以后再定”，判偏航"),
    "KC-000050": ("论域元素的存在性是理论无法拒绝的问题", "ALIGNED",
                  "罗素线是它的落实：宇宙是 HoTT 不能不放进论域的元素；追问落成逐层问“成员以什么方式相同”的过程（解释桥，待裁定）；机器证明每层答否，永不停机是元层推论。证据：docs/社区审计提交/02-罗素悖论的幽灵.md 第 2–5 节；Cloud-Opus审计并补完GLM/14-罗素面终局判词.md",
                  "解释桥与“存在要求落定”由用户裁定与社区审计；元层推论尚未机器化"),
    "KC-000051": ("算符先于存在性落定的次序非法", "ALIGNED",
                  "第二批在罗素线里对应：单价性等运算在宇宙的存在性追问未落定时已在其上运转。这一对应是解释，不是机器事实；静动两种读法中采用动态读。证据：docs/社区审计提交/02-罗素悖论的幽灵.md 第 6 节",
                  "若有人指出运算并未先于落定，须回到原文重审"),
}

NOT_TOUCHED_TEXT = "本次登记的芝诺线、罗素线与归因修正没有重新判断该条所指的内容；原文身份保留。"


def audit_rows() -> tuple[list[str], dict[str, int]]:
    shard = (ROOT / f"{AUDIT_SET}/002 - 核心认知逐条五元组.md").read_text(encoding="utf-8")
    parsed: dict[str, list[str]] = {}
    for line in shard.splitlines():
        m = re.match(r"^\| (KC-\d{6}) ?([^|]*)\|(.*)$", line)
        if not m:
            continue
        cells = [c.strip() for c in ("|" + m.group(3)).strip().strip("|").split("|")]
        # cells: relation, posture/action, evidence, next
        parsed[m.group(1)] = [m.group(2).strip()] + cells
    rows: list[str] = []
    counts: dict[str, int] = {}
    for n in range(1, 52):
        kc = f"KC-{n:06d}"
        if kc in OVERRIDES:
            name, relation, assess, nxt = OVERRIDES[kc]
        else:
            name, relation_raw, posture, evidence, nxt = parsed[kc][0], *parsed[kc][1:5]
            relation = re.match(r"[A-Z_]+", relation_raw).group(0)
            if relation == "NOT_TOUCHED":
                assess = NOT_TOUCHED_TEXT
                if posture.strip("—") and posture != "—":
                    assess = f"{posture}。{NOT_TOUCHED_TEXT}"
            else:
                assess = posture
                if evidence.strip("—"):
                    assess = f"{posture}。证据：{evidence}"
            if nxt.strip("—") == "":
                nxt = "无新增触及条件；若后续工作改变该条相关的判断，再回源重审"
        assess = expand_paths(assess).replace("|", "／")
        nxt = expand_paths(nxt).replace("|", "／")
        name = name.replace("|", "／")
        counts[relation] = counts.get(relation, 0) + 1
        rows.append(f"| `{kc}` | {name} | {relation} | {assess} | {nxt} |")
    return rows, counts


def audit_text() -> str:
    rows, counts = audit_rows()
    tally = "、".join(f"{k} {v}" for k, v in sorted(counts.items()))
    head = f"""# {SESSION_ID} 完整兼容审计

{GEN9}；51 KC。canonical writer 只授权新 session 目录第一层文件，所以本审计是单文件兼容 bundle；`G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001` 保持。本轮的逐条材料来自 Cloud-Opus 本会话审计集（`{AUDIT_SET}.md`）对 KC-000001 至 KC-000048 的五元组，以及本轮新增的 KC-000049 至 KC-000051；KC-000005、KC-000020、KC-000049 三条按用户 2026-09-24 的修正重评。

- core_change: YES_ADDITIVE_PRESERVING — {GEN8}/48 → {GEN9}/51；新增 KC-000049（归因修正）、KC-000050（罗素原则 P1–P3）、KC-000051（第二批原文）；48/48 旧单元 PRESERVED_EXACT、mapping_remainder=0；规范生成器新增 Claude、GLM 两个来源平台。
- direction_change: YES_IN_PLACE — 新增 DIR-U-A7-INFINITE-COHERENCE、DIR-U-RUSSELL-EXISTENCE-QUESTIONING、DIR-G-ATTRIBUTION-IS-MAIN-TOPIC；方向追踪索引的 source_state_revision 刷到 290。
- panorama_change: YES_IN_PLACE — 新增 OUT-U-A7-INFINITE-COHERENCE、OUT-U-RUSSELL-UNIVERSE-QUESTIONING、OUT-U-COPUS-GLM-AUDIT、OUT-TOP-ATTRIBUTION-CORRECTION-APPLIED；“当前未完成”增补第 18–20 项；全景视野索引刷到 290。
- essay_change: YES_IN_PLACE — 扩展认知 003／005／009 按归因修正原位修订，新增第 010 片（KC-000050／051 的展开）；索引基线刷到 {GEN9}；扩展认知中全部 51 个原文块与核心认知逐字一致（准备脚本在写入前逐块比对）。
- update_decision: 入核与登记为用户 2026-09-27 明确授权的动作；不改变 Goal7 / MO3-COVERAGE-C 的执行队列；不把“用户判定”写成数学定理；不宣称 HoTT 不一致；不认证解释桥与“存在要求落定”。
- cross_conflicts: 用户判定（两条线复活）与机器事实、元层推论、来源转述、开放问题分表；Lean 原负控制的注释（声称内核拒绝）与实际行为（细化器拒绝）的冲突已由内核级对照补上；KC-000005／020 的原话与 KC-000049 的修正并存，按用户选择保留原话加修正。
- unresolved: 解释桥与现实侧前提待用户裁定与社区审计；外部独立复核未发生；Terra 未回应；框架 Schema 的平台枚举与 SOP 技能措辞待用户本机的全局自维护 Gate；`verify_projection_freshness.py` 在本次之前已失败；两个标签未推送。

关系计数：{tally}（计数不认证理解）。

|KC ID|姿态|relation|assessment and evidence|next and falsifier|
|---|---|---|---|---|
"""
    tail = f"""

## 四项对齐与偏航分析

1. 用户主张：归因是正题（KC-000049）；论域元素的存在性是理论无法拒绝的问题，追问若在现实中不停机即成功（KC-000050）；算符先于存在性落定是不合理的次序，合法性追溯是永不停机的计算（KC-000051）。
2. 不得收窄成：“宇宙没有截断层级是已知定理”“HoTT 有模型所以没有问题”“归因以后再说”“下一个故事”。
3. 怎样改变当前任务与证据选择：现象已有，就直接展开归因；把“追问存在性”落成会被执行的过程并标明这是解释；把机器证明的事（每层答否）与元层推论（追问不停）分开。
4. 仍然开放的证明义务：元层推论未机器化；不用高阶归纳类型时单个宇宙的相容性仅来源级；统一定义的不可能性是开放问题；外部独立复核。

偏航风险与做法：最容易的偏航是把用户的强判定写成“HoTT 被证明有悖论”或“不一致”。本轮的做法是判定标【用户原话】，证据状态逐项分级，“不宣称不一致”写进两份稿子的首节；解释桥与现实侧前提写明为待裁定。
"""
    return head + "\n".join(rows) + tail


# ----------------------------------------------------------------------------------------------
# session files
# ----------------------------------------------------------------------------------------------

def session_text() -> str:
    return f"""# {SESSION_ID}

核心认知第 9 代入核，扩展认知修订，方向追踪与全景视野登记芝诺线与罗素线、对 GLM 的审计、归因修正；STATE 登记。

- host: Claude Code（claude.ai/code 云端会话，分支 claude/charming-pasteur-mvzlio）
- model: 不写入仓库产物（会话策略）；模型身份只在会话聊天中查询
- tier: T3
- role: 用户授权的入核与登记；不是研究生成，不是独立审计
- load_receipt: 读取 `.codex/tools/cognition_runtime.py` 全文、PROTOCOL §4A/§5/§7、s154 准备脚本、`核心认知.md` 第 9 代全文（KC-000049–KC-000051 与 48 条旧单元逐字保留已由生成器校验）、方向追踪与全景视野的索引及相关分片、扩展认知 003／005／009 与索引、MEMORY 三片、RESUME 首部；plan snapshot 见 RUNS.json
- authorization: 用户 2026-09-27：入核和登记我现在就授权你，立即完成所有剩余的你可以完成的工作
- parent: 不改变 Goal7 / MO3-COVERAGE-C；本会话不是 integrator 的研究单元

做了什么：

1. 三个来源文件入 `sources/prompts/`（逐字，带哈希；时间为上界，来源文件内写明）；curation v9；生成器新增 `Claude`、`GLM` 平台；`scripts/audit/build_core_cognition.py --write` 生成第 9 代、manifest 与 transition；`verify_core_cognition.py` PASS_WITH_SCOPE。
2. 扩展认知：003／005／009 原位修订（归因修正），新增 010；扩展认知全部 51 个原文块与核心认知逐字一致（准备脚本在写入前逐块比对）。
3. 方向追踪新增 3 行，全景视野新增 4 行并增补“当前未完成”第 18–20 项；MEMORY、RESUME 同步；STATE 登记 1 个核心代记录、2 个候选、1 个跟进项与本 session。
4. 不做的事（及原因）：不改 `.codex/cognition/CORE_COGNITION.schema.json` 与 `.codex/skills/hott-paradox-search-sop/SKILL.md`（框架改动须过用户本机的全局自维护 Gate，见 `{REC_FOLLOW}`）；不改 KC-000005／020 原话；不推送标签；不处理 `verify_projection_freshness.py` 的既有失败。

|element_usage|本次用途与边界|
|---|---|
|核心认知与原版最高指示|KC-000047–051 与第 9 代全文；归因是正题；不把判定写成定理|
|canonical runtime 与 writer|plan/prepare/checkpoint；单文件兼容审计；只认 canonical result|
|build_core_cognition 与 verify_core_cognition|重建与校验第 9 代；48 旧单元逐字保留|
|projection_edit|索引与全部分片同 payload 原位修改|
|verify_three_way_cognition 与 verify_governance_shards|结构校验；不证明语义|

验证命令与结果见 RUNS.json。无新数学主张；本 session 登记的形式结果属于 Cloud-Opus 审计会话的 46 个运行，它们各自的收据不因本 checkpoint 改变。未 push（标签需用户在本机推送）。
"""


def runs_obj(snapshot: str) -> dict:
    return {
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "session_kind": "GOVERNANCE_CORE_GENERATION_AND_LINE_REGISTRATION",
        "checkpoint_result": RESULT_REL,
        "base_snapshot": snapshot,
        "formal_runs": [],
        "registered_formal_runs": {
            "note": "registered by reference, not re-run by this checkpoint; each keeps its own F-011 receipt",
            "cloud_opus_runs": 46,
            "accepted": 23,
            "negative_controls_rejected_as_expected": 23,
            "byte_exact_replay_result": "Cloud-Opus审计并补完GLM/附件/工作过程文件/自查轮/verify-all-rerun-46个运行.json",
        },
        "governance_runs": [
            {"tool": "scripts/audit/build_core_cognition.py", "command": f"--curation {CURATION} --transition-output {TRANSITION} --transition-from-ref 4603eb2a5a6b27c7732931a171c1ab54e6d74b79 --write",
             "status": "BUILT / COMPLETE_ADDITIVE_PRESERVING / mapping_count=48 / remainder=0", "generation": f"{GEN8}/48 -> {GEN9}/51"},
            {"tool": "scripts/audit/verify_core_cognition.py", "command": f"--curation {CURATION} --transition {TRANSITION}", "status": "PASS_WITH_SCOPE"},
            {"tool": ".codex/tools/cognition_runtime.py", "command": "checkpoint --snapshot <base_snapshot> --payload <payload> --apply",
             "status": "CHECKPOINT_COMMITTED expected; only the canonical result.json proves it"},
        ],
        "new_math_claims": [],
        "math_status_change": "NONE",
        "push_policy": "branch push only; the two tags need the user's machine",
        "note": "Core entry and registration authorized by the user on 2026-09-27; no mathematical claim is delivered by this checkpoint.",
    }


# ----------------------------------------------------------------------------------------------
# STATE
# ----------------------------------------------------------------------------------------------

def state_edits(state: dict, sources_hash_paths: dict[str, list[str]]) -> None:
    session_path = f"{SESSION_REL}/SESSION.md"
    state["revision"] = 290
    state["latest_session"] = SESSION_ID
    state["current_core"] = {
        "core_sha256": sha_file(CORE),
        "curation": CURATION,
        "curation_sha256": sha_file(CURATION),
        "generation": GEN9,
        "kc_count": 51,
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

    core_sources = [CORE, MANIFEST, CURATION, TRANSITION, SRC_ATTR, SRC_P13, SRC_B2,
                    "scripts/audit/build_core_cognition.py", "scripts/audit/verify_core_cognition.py"]
    state["records"][REC_CORE] = {
        "depends_on": [],
        "evidence_status": "VERIFIED_WITH_SCOPE / COMPLETE_ADDITIVE_PRESERVING / FRAMEWORK_SCHEMA_PLATFORM_ENUM_NOT_UPDATED",
        "full_sources": core_sources,
        "kind": "core_generation_migration",
        "lifecycle_status": "CURRENT",
        "path": TRANSITION,
        "related_records": ["A-CORE-GENERATION-4-001", SESSION_ID],
        "scope": ("Incrementally add three exact direct-user items (KC-000049 attribution correction of 2026-09-24, KC-000050 Russell principles P1-P3 and "
                  "KC-000051 second batch of 2026-09-26) while preserving every generation-8 KC byte for byte. Supersedes A-CORE-GENERATION-4-001 as the owner of "
                  "the current core identity (that record's hash pin is stale since generation-5). Source timestamps of KC-000050/051 are upper bounds stated in their source files."),
        "source_hashes": hashes(core_sources),
        "status": "closed",
    }
    a7_sources = [DOC01, DOCREADME, f"{COPUS}/证据索引.md", "HoTT/formal/claude-cg001/wild-sst/CLAIM.md",
                  "HoTT/formal/claude-cg001/wild-sst-lean/CLAIM.md", "HoTT/formal/cloud-opus-glm-audit/lean-controls/CLAIM.md"]
    state["records"][REC_A7] = {
        "classification": "USER_DECLARED_REVIVED_ZENO_GHOST_A_DIRECTION",
        "depends_on": [],
        "evidence_status": "FORMAL_CHECKED_WITH_SCOPE / CROSS_PLATFORM_REPLAYED / IMPOSSIBILITY_OPEN / COMMUNITY_AUDIT_PENDING",
        "full_sources": a7_sources,
        "kind": "candidate",
        "lifecycle_status": "ACTIVE_WORK",
        "path": DOC01,
        "related_records": [REC_CORE, REC_RUSSELL, SESSION_ID],
        "scope": ("Zeno-face line (direction A): sameness as structure under univalence; semi-simplicial structure defined in one line where sameness is a fact, "
                  "with a new coherence level at every step in HoTT. Machine-checked instances and a UIP contrast world; uniform internal definition is an open problem. "
                  "The user's verdict of 2026-09-27 is a judgment, not a theorem; no HoTT inconsistency is claimed."),
        "source_hashes": hashes([DOC01, DOCREADME]),
        "status": "active",
    }
    russell_sources = [DOC02, DOCREADME, f"{COPUS}/14-罗素面终局判词.md", f"{COPUS}/13-外部复核请求.md", f"{COPUS}/证据索引.md",
                       "HoTT/formal/cloud-opus-glm-audit/ks-universe-tower/CLAIM.md", "HoTT/formal/cloud-opus-glm-audit/hitscan/CLAIM.md",
                       "HoTT/formal/cloud-opus-glm-audit/glm-repairs/CLAIM.md", "HoTT/formal/cloud-opus-glm-audit/lean-controls/CLAIM.md",
                       "HoTT/formal/claude-cg001/universe-questioning/CLAIM.md"]
    state["records"][REC_RUSSELL] = {
        "classification": "USER_DECLARED_REVIVED_RUSSELL_GHOST_B_DIRECTION",
        "depends_on": [],
        "evidence_status": "FORMAL_CHECKED_WITH_SCOPE / META_INFERENCE_NOT_MACHINIZED / BRIDGE_AND_EXISTENCE_PREMISE_UNADJUDICATED / EXTERNAL_REVIEW_NOT_YET",
        "full_sources": russell_sources,
        "kind": "candidate",
        "lifecycle_status": "ACTIVE_WORK",
        "path": DOC02,
        "related_records": [REC_CORE, REC_A7, SESSION_ID],
        "scope": ("Russell-face line (direction B): the universe as a domain element HoTT cannot refuse; the existence questioning read as a level-by-level process; "
                  "every level answers no (machine-proved), never halting is a meta-level inference; HoTT hands the universe over at once. Bridge and the 'existence requires settling' "
                  "premise are unadjudicated; audit of the GLM line included; no HoTT inconsistency is claimed."),
        "source_hashes": hashes([DOC02, DOCREADME]),
        "status": "active",
    }
    state["records"][REC_FOLLOW] = {
        "evidence_status": "PENDING_USER_ACTION / NOT_RUN",
        "full_sources": [RECORD15, "rulings.md"],
        "kind": "governance_follow_up",
        "lifecycle_status": "OPEN_ISSUE",
        "path": RECORD15,
        "related_records": [REC_CORE, SESSION_ID],
        "scope": ("Follow-ups the cloud session cannot complete: (1) CORE_COGNITION.schema.json platform enums need Claude and GLM; (2) hott-paradox-search-sop SKILL.md line 119 wording; "
                  "both are framework edits needing the user's global self-maintenance gate on the local machine; (3) verify_projection_freshness.py already failed before this checkpoint; "
                  "(4) the two tags Cloud-Opus对GLM的审计 and Cloud-Opus工作完成 were not pushed (the cloud git channel allows branch pushes only)."),
        "status": "open",
    }
    state["unresolved"].append(REC_FOLLOW)
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [session_path, f"{SESSION_REL}/RUNS.json", f"{SESSION_REL}/CORE_COGNITION_AUDIT.md", RESULT_REL, TRANSITION, CURATION, RECORD15],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV_SESSION, REC_CORE, REC_A7, REC_RUSSELL, REC_FOLLOW],
        "scope": ("Core generation-9 entry (KC-000049-051), essay revision, registration of the Zeno and Russell lines, the audit of the GLM line and the attribution correction. "
                  "User-authorized on 2026-09-27; does not change the Goal7 / MO3-COVERAGE-C queue; no new mathematics."),
        "source_hashes": {},
        "status": "complete",
    }


# ----------------------------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    required = [CORE, MANIFEST, CURATION, TRANSITION, SRC_ATTR, SRC_P13, SRC_B2, DOC01, DOC02, DOCREADME, RECORD15,
                f"{AUDIT_SET}/002 - 核心认知逐条五元组.md"]
    missing = [p for p in required if not (ROOT / p).is_file()]
    if missing:
        raise SystemExit(f"EVIDENCE_MISSING:{missing}")

    state_path = ROOT / R.STATE
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if state.get("revision") != 289 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit(f"EXPECTED_REVISION_289:{state.get('revision')}:{state.get('latest_session')}")
    for identity in (SESSION_ID, REC_CORE, REC_A7, REC_RUSSELL, REC_FOLLOW):
        if identity in state["records"]:
            raise SystemExit(f"RECORD_ALREADY_EXISTS:{identity}")

    plan = R.plan(ROOT, profile="governance", _allow_core_transition=CORE_TRANSITION)
    payloads = core_payloads()
    if list(payloads)[-3:] != ["KC-000049", "KC-000050", "KC-000051"]:
        raise SystemExit("CORE_NOT_GENERATION_9")

    direction = projection_edit.load(ROOT, R.DIRECTION)
    d2 = "方向追踪/002 - 治理与用户方向.md"
    for row in DIR_ROWS:
        projection_edit.append_to_shard(direction, d2, row)
    for old, new in (
        ("source_state_revision: 289", "source_state_revision: 290"),
        ("projection_generation: 20260924-direction-289", "projection_generation: 20260930-direction-290"),
        ("版本：`integrated-direction-portfolio/v1.12`", "版本：`integrated-direction-portfolio/v1.13`"),
        ("日期：2026-09-24", "日期：2026-09-30"),
    ):
        projection_edit.replace_in_index(direction, old, new)

    panorama = projection_edit.load(ROOT, R.PANORAMA)
    p2 = "全景视野/002 - 治理、门禁与骨架结果.md"
    for row in OUT_ROWS:
        projection_edit.append_to_shard(panorama, p2, row)
    p8 = "全景视野/008 - 当前未完成.md"
    projection_edit.append_to_shard(panorama, p8, PANORAMA_008_ADD)
    for old, new in (
        ("source_state_revision: 289", "source_state_revision: 290"),
        ("projection_generation: 20260924-outcome-289", "projection_generation: 20260930-outcome-290"),
        ("版本：`integrated-outcome-panorama/v1.12`", "版本：`integrated-outcome-panorama/v1.13`"),
        ("日期：2026-09-24", "日期：2026-09-30"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    essay = projection_edit.load(ROOT, R.ESSAY)
    essay_edits(essay, payloads)

    memory = projection_edit.load(ROOT, "MEMORY.md")
    m1 = "MEMORY/001 - 当前执行队列.md"
    m2 = "MEMORY/002 - 当前证据上限与恢复入口.md"
    m3 = "MEMORY/003 - 当前验证状态与顺序日志.md"
    memory["shards"][m1] = replace_once(
        memory["shards"][m1],
        "\n## 既有项目队列与历史进展（2026-09-16至19，逐项保留其原时间）",
        MEMORY_001_ADD + "\n## 既有项目队列与历史进展（2026-09-16至19，逐项保留其原时间）",
    )
    # MEMORY/002: insert the new ceiling bullet as the last bullet of the ceiling list
    body2 = memory["shards"][m2]
    marker = "\n\n## 恢复入口"
    if body2.count(marker) != 1:
        raise SystemExit("MEMORY_002_MARKER")
    memory["shards"][m2] = body2.replace(marker, "\n" + MEMORY_002_ADD.rstrip("\n") + marker, 1)
    if not memory["shards"][m3].endswith("\n"):
        memory["shards"][m3] += "\n"
    memory["shards"][m3] += MEMORY_003_ADD

    resume_path = ".codex/research/hott/RESUME.md"
    resume = (ROOT / resume_path).read_text(encoding="utf-8")
    resume = replace_once(resume, "## 历史停止点\n\n", "## 历史停止点\n\n" + RESUME_ADD)

    state_edits(state, {})

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
    if original_blocks != 51:
        raise SystemExit(f"ESSAY_ORIGINAL_BLOCK_COUNT:{original_blocks}")
    created = {session_path, audit_path, runs_path, RESULT_REL, ESSAY_010}
    for label, body in (("audit", texts[audit_path]), ("session", texts[session_path]), ("essay-010", texts[ESSAY_010]),
                        ("direction-rows", "".join(DIR_ROWS)), ("outcome-rows", "".join(OUT_ROWS)),
                        ("panorama-008", PANORAMA_008_ADD), ("memory", MEMORY_001_ADD + MEMORY_002_ADD + MEMORY_003_ADD + RESUME_ADD)):
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
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 290, "session_id": SESSION_ID, "files": len(texts), "essay_original_blocks_verified": original_blocks}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
