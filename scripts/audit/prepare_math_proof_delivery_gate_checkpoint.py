#!/usr/bin/env python3
"""Prepare revision 26 for the mathematical-proof-before-delivery policy."""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-GOV-20260912-026-MATH-PROOF-DELIVERY-GATE"
EVIDENCE = "audit/数学结论机器证明交付门禁实施证据-20260912.md"
SPEC_PATH = "docs/quality/数学结论机器证明与证据留存规范.md"
SPEC = importlib.util.spec_from_file_location("runtime_math_proof_delivery_gate", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old}:{count}")
    return text.replace(old, new, 1)


def replace_line_prefix(text: str, prefix: str, replacement: str) -> str:
    lines = text.splitlines()
    indexes = [index for index, line in enumerate(lines) if line.startswith(prefix)]
    if len(indexes) != 1:
        raise ValueError(f"LINE_PREFIX_COUNT:{prefix}:{len(indexes)}")
    lines[indexes[0]] = replacement
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def replace_span(text: str, start: str, end: str, replacement: str) -> str:
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"SPAN_MARKER_COUNT:{start}:{text.count(start)}:{end}:{text.count(end)}")
    begin = text.index(start)
    finish = text.index(end, begin) + len(end)
    return text[:begin] + replacement + text[finish:]


def append_unique(values: list[str], value: str) -> None:
    if value not in values:
        values.append(value)


def build_direction(root: Path) -> str:
    body = (root / R.DIRECTION).read_text(encoding="utf-8")
    body = replace_once(body, "integrated-direction-portfolio/v1.3", "integrated-direction-portfolio/v1.4")
    body = replace_once(body, "integrated-direction-portfolio:v1.3", "integrated-direction-portfolio:v1.4")
    body = body.replace(
        "CORE_GENERATION_4_THEORY_ECONOMY_REFLECTION_USER_DIRECTION_ACTIVE",
        "CORE_GENERATION_4_MATH_PROOF_DELIVERY_GATE_ACTIVE",
    )
    body = replace_once(body, "source_state_revision: 25", "source_state_revision: 26")
    body = replace_once(body, "projection_generation: 20260912-direction-009", "projection_generation: 20260912-direction-010")
    divider = "|---|---|---|---|---|---|---|---|"
    gate_row = (
        "| `DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前 AI 的数学结论在交付前必须由匹配语义的 proof assistant/kernel 机器证明；源码、实际 run 与索引全部留在 repo，"
        "`/tmp` 不得成为唯一证据位置 | 用户 ruling §15 / F-011 | `ACTIVE_USER_DIRECTION` | `CORE_UNRELATED/GOVERNANCE_RULING` | "
        "`OUT-TOP-MATH-PROOF-DELIVERY-GATE` | 每个准备晋升为结论的 claim 先建立 formal source→immutable run→claim matrix 链；缺件时降格为问题/猜想/纸笔候选/未重放来源 | "
        "`AGENTS.md`；`docs/quality/数学结论机器证明与证据留存规范.md`；`HoTT/formal/README.md`；`HoTT/verification/runs/README.md`；`HoTT/CLAIM_EVIDENCE_MATRIX.md` |"
    )
    body = replace_once(body, divider, divider + "\n" + gate_row)
    old_rule = "6. 结束时反向检查：本轮结果是否改变方向状态、下一动作、依赖或优先级，以及是否需要更新核心（仅用户新原文才更新核心）。"
    new_rule = old_rule + "\n7. 准备把任何数学命题从候选/纸笔状态提升为结论前，执行 `MATH_PROOF_BEFORE_DELIVERY_V1`；没有 repo 内 source/run/index 链就保持非结论状态。"
    body = replace_once(body, old_rule, new_rule)
    priority_start = "当前优先顺序区分“用户目标”“AI 战略建议”“首个工作包”和“证据/治理队列”，防止一种优先级冒充另一种："
    body = replace_once(
        body,
        priority_start,
        priority_start + "\n\n`DIR-G-MATH-PROOF-DELIVERY-GATE` 是覆盖所有数学方向的硬交付约束，不与研究候选争抢优先级：未过门禁的结果不得晋升为数学结论。",
    )
    old_tail = "本轮已按用户要求形成 C4 条件性数学论证并更新研究航向，但没有启动 proof assistant 机器证明、具体非停机程序运行或外部接口审计。后续每个自然工作单元只推进一个可检查构造，并按 C3/C4 的判词与停止条件收敛。"
    new_tail = "C4 仍是 `PAPER_ONLY` 条件性综合，没有 proof assistant 机器证明、具体非停机程序运行或外部接口审计；在新门禁下不能作为当前 AI 已证明的数学结论重新交付。后续每个数学工作单元必须先形成 repo 内 proof source/run/index 链，否则只交付候选和证明义务。"
    return replace_once(body, old_tail, new_tail)


def build_panorama(root: Path) -> str:
    body = (root / R.PANORAMA).read_text(encoding="utf-8")
    body = replace_once(body, "integrated-outcome-panorama/v1.3", "integrated-outcome-panorama/v1.4")
    body = replace_once(body, "integrated-outcome-panorama:v1.3", "integrated-outcome-panorama:v1.4")
    body = body.replace(
        "CORE_GENERATION_4_THEORY_ECONOMY_REFLECTION_USER_DIRECTION_ACTIVE",
        "CORE_GENERATION_4_MATH_PROOF_DELIVERY_GATE_ACTIVE",
    )
    body = replace_once(body, "source_state_revision: 25", "source_state_revision: 26")
    body = replace_once(body, "projection_generation: 20260912-outcome-009", "projection_generation: 20260912-outcome-010")
    body = replace_line_prefix(
        body,
        "| `PAPER_ONLY`",
        "| `PAPER_ONLY` | 有纸笔推导或说明，未有相称机器证明；按 F-011 不得由当前 AI 重新交付为已成立数学结论 |",
    )
    divider = "|---|---|---|---|---|---|---|---|"
    outcome = (
        "| `OUT-TOP-MATH-PROOF-DELIVERY-GATE` | F-011：数学结论交付前机器证明；证明源码、实际 kernel run 和 claim/proof/run 索引分别由 `HoTT/formal/`、"
        "`HoTT/verification/runs/`、`HoTT/CLAIM_EVIDENCE_MATRIX.md` 持有；无证明则强制降格 | `DIR-G-MATH-PROOF-DELIVERY-GATE` | 当前用户裁定与项目本地治理 3.2 candidate | "
        "`VERIFIED_WITH_SCOPE` | 根/`.codex` AGENTS、PROTOCOL、双 Skills、稳定规范和三类 owner 已接通；4/4 正负向测试与 static verifier 通过 | "
        "不证明未来模型一定遵循，不证明任何 HoTT/ERCF 命题；fresh model behavior `NOT_RUN`，当前未 commit/tag | "
        "`docs/quality/数学结论机器证明与证据留存规范.md`；`audit/数学结论机器证明交付门禁实施证据-20260912.md`；`scripts/audit/verify_math_proof_delivery_governance.py` |"
    )
    body = replace_once(body, divider, divider + "\n" + outcome)
    old_question = "| 状态是否有直接证据 | 文件、代码、测试、运行、Git、source hash 和适用范围 | 降级 `REVIEW_REQUIRED`/`UNKNOWN` |"
    new_question = "| 状态是否有直接证据 | 文件、代码、测试、运行、Git、source hash 和适用范围；数学结论另查 formal source/kernel run/claim index | 降级 `REVIEW_REQUIRED`/`UNKNOWN`；数学命题降格为非结论状态 |"
    body = replace_once(body, old_question, new_question)
    update_anchor = "- 新的稳定数学结论：回到 `HoTT/` 当前 owner，不能只写在本文件；"
    body = replace_once(
        body,
        update_anchor,
        "- 新的数学结论：先通过 `MATH_PROOF_BEFORE_DELIVERY_V1`，把源码/run/index 留在 repo，再回到 `HoTT/` 当前 owner；未通过只能记录为候选/问题，不能只写在本文件；",
    )
    return body


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    counts = {"DEEPENED": 0, "NOT_TOUCHED": 0}
    for unit in manifest["units"]:
        unit_id = str(unit["id"])
        if unit_id in {"KC-000021", "KC-000022"}:
            relation = "DEEPENED"
            assessment = "用户原有‘语言/公式之外必须机器证明并真实运行’要求现在成为所有当前 AI 数学结论的交付 Gate，并补齐 repo 内源码、run、索引和失败降格合同。"
            unresolved = "fresh model behavior 尚未验证；每个未来数学 claim 仍需自己的 proof package。"
        else:
            relation = "NOT_TOUCHED"
            assessment = "本轮只建立数学结论的机器证明交付治理，不改变、证明或反驳该用户悖论/元数学原文。"
            unresolved = "该 KC 的既有数学状态不因治理规则自动提高。"
        counts[relation] += 1
        label = str(unit["semantic_label"]).replace("|", "\\|")
        lines.append(
            f"| `{unit_id}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | AGENTS.md；F-011；{SPEC_PATH}；核心认知.md {unit_id} | {unresolved} |"
        )
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — 本轮是一般治理裁定，不是新的悖论/元数学思想正文；generation-4/36 KC 不变。",
        "- direction_change: `YES_GOVERNANCE_DIRECTION` — 新增跨数学方向的 proof-delivery Gate，不改变研究候选排序。",
        "- panorama_change: `YES_GOVERNANCE_OUTCOME_AND_STATUS_SEMANTICS` — PAPER_ONLY 明确不可交付为结论；新增门禁实施结果。",
        "- update_decision: `用户原意进 rulings，当前要求进 F-011，硬规则进 AGENTS，详细合同/源码/run/index 各归唯一 owner；STATE/MEMORY/三件套同步。`",
        "- cross_conflicts: `NONE` — KC-000021/22 已要求机器证明；新裁定把局部要求提升为全部数学结论的通用交付标准。",
        "- unresolved: `fresh model 实际遵循、首个按新规范生成的数学 proof package、旧结论重放和 Git version-close 尚未完成。`",
        "", "## 汇总", "",
        f"`DEEPENED={counts['DEEPENED']} / NOT_TOUCHED={counts['NOT_TOUCHED']} / DEVIATED=0`。本轮没有把软件治理测试冒充数学证明。", "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()
    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 25 or state.get("latest_session") != "S-RES-20260912-025-MINIMAL-WITNESS-PRECONDITIONS":
        raise SystemExit("EXPECTED_REVISION_25_S025")

    direction = build_direction(root)
    panorama = build_panorama(root)
    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    queue_start = "1. 用户新增并已写入 core 的主方向："
    queue_end = "5. 治理独立验证仍开放：固定 model/host/version 的 fresh Session/真实压缩后行为验收；Python EOF/hash 不替代模型行为。"
    new_queue = """1. 用户新增项目级硬约束 F-011：当前 AI 的所有数学结论在交付前必须有匹配语义的机器证明；源码、实际 kernel run 和 claim/proof/run 索引必须留在 repo，`/tmp` 不能是唯一证据位置。
2. 当前数学主方向仍是 HoTT 自反真理验证/理论经济；下一最小研究结果 ERCF-1/2 只有在 `HoTT/formal/`、`HoTT/verification/runs/` 和 claim matrix 形成完整 proof package 后，才可作为数学结论交付。
3. C4 保持 `PAPER_ONLY`，新规则不追认或伪造历史证明；未来重用其命题时必须逐项形式化和重放。
4. C3 的资格保持性、W51×RP-B01、自指与 R041 partiality 对照继续在全局视野；同样受 F-011 约束。
5. 历史交接开放项仍为 2,396 条 claim、aistudio coverage、历史数学主张和 response→artifact/code/Git 因果；新门禁不批量重写历史状态。
6. 治理独立验证仍开放：fresh Session/真实压缩后模型是否实际遵循 proof Gate；static tests 不能替代行为验收。"""
    memory = replace_span(memory, queue_start, queue_end, new_queue)
    verified_marker = "- S025 补齐 E₀ 的 `a₀:A`/`s₀≠s₁` 见证，并明确有限任务族不自动推出 factorization 可判定。"
    memory = replace_once(
        memory,
        verified_marker,
        verified_marker + "\n- F-011 proof-delivery Gate 已在根/`.codex` AGENTS、PROTOCOL、双 Skills、稳定规范、formal/run/index owner 中实现；4/4 正负向 static tests PASS。它只证明治理结构，不证明未来模型行为或任何数学命题。",
    )
    evidence_marker = "- fresh Python 输入保真可验证；模型对三件套的实际理解仍不由工具认证。"
    memory = replace_once(
        memory,
        evidence_marker,
        evidence_marker + "\n- 数学结论若没有 repo 内匹配语义的 proof source、kernel run 和 claim index，只能保持 `QUESTION/CONJECTURE/HEURISTIC/PAPER_ONLY/COUNTEREXAMPLE_CANDIDATE/SOURCE_REPORTED_NOT_REPLAYED`。",
    )
    recovery_marker = "按根 AGENTS 全文加载 core→direction→panorama。"
    memory = replace_once(memory, recovery_marker, recovery_marker + "任何数学结论交付先执行 F-011，并读 `docs/quality/数学结论机器证明与证据留存规范.md`。")

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = replace_once(
        frontier,
        "本文件是当前注意力槽，不是数学结论数据库。C4 已回答用户问题但证据等级为 `PAPER_ONLY`；本轮没有 proof-assistant 或具体发散运行。",
        "本文件是当前注意力槽，不是数学结论数据库。F-011 现在禁止把无机器证明的候选交付为数学结论；C4 仍为 `PAPER_ONLY`。所有未来数学槽位必须形成 `HoTT/formal/` source、`HoTT/verification/runs/` kernel receipt 与 claim matrix 索引。",
    )
    frontier = replace_line_prefix(
        frontier,
        "| 第一最小可验结果 |",
        "| 第一最小可验结果 | ERCF-1/2 的首个 F-011 proof package | blocked-until-formal-source-run-index | 在 `HoTT/formal/` 固定命题和证明；实际运行匹配语义的 checker；保存五件 run 原件并索引；否则只交付 `PAPER_ONLY` 证明义务 |",
    )
    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8").rstrip()
    if "33. 数学结论交付" not in lessons:
        lessons += "\n33. 数学结论交付必须把自然语言命题、形式命题、proof source、匹配语义的 kernel run、原始输出和 claim index 绑定；代码存在、有限测试、外部论文、旧 aggregate receipt 或 `/tmp` 唯一文件都不能替代。无法闭合时正确结果是降格，而不是补强措辞。"
    lessons += "\n"
    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = replace_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\nF-011 已成为所有未来数学结论的硬交付 Gate：先在 repo 内完成 formal source、kernel run、claim index；否则只能交付问题/猜想/纸笔候选/未重放来源。C4 仍是 `PAPER_ONLY`，没有被追认为已证。\n\n",
    )

    state["revision"] = 26
    state["latest_session"] = SESSION_ID
    state["load_policy"]["manifest_version"] = "3.2.0"
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "status": "MATH_PROOF_DELIVERY_GATE_IMPLEMENTED_STATICALLY_VERIFIED_FRESH_BEHAVIOR_OPEN",
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "next_minimal_verification": "Before any ERCF conclusion, create the first complete F-011 proof package under HoTT/formal and HoTT/verification/runs, index it, and run the matching kernel; otherwise deliver only a paper-only obligation.",
    })
    semantic = "CORE_GENERATION_4_MATH_PROOF_DELIVERY_GATE_ACTIVE"
    state["projection"]["status"] = semantic
    drec = state["records"]["I-DIRECTION-PORTFOLIO-20260912"]
    drec.update({"projection_generation": "20260912-direction-010", "semantic_status": semantic, "scope": "Cross-source portfolio with F-011 as a hard proof-before-delivery constraint over every mathematical direction; research priority remains otherwise unchanged."})
    for path in (SPEC_PATH, EVIDENCE):
        append_unique(drec["full_sources"], path)
    prec = state["records"]["I-OUTCOME-PANORAMA-20260912"]
    prec.update({"projection_generation": "20260912-outcome-010", "semantic_status": semantic, "scope": "Cross-source outcome panorama with explicit proof-delivery eligibility: paper/finite/source-reported results cannot be promoted to current AI mathematical conclusions without a repo-local source/run/index chain."})
    for path in (SPEC_PATH, EVIDENCE):
        append_unique(prec["full_sources"], path)

    hashes = {
        "AGENTS.md": R.sha((root / "AGENTS.md").read_bytes()),
        SPEC_PATH: R.sha((root / SPEC_PATH).read_bytes()),
        "HoTT/formal/README.md": R.sha((root / "HoTT/formal/README.md").read_bytes()),
        "HoTT/verification/runs/README.md": R.sha((root / "HoTT/verification/runs/README.md").read_bytes()),
        "HoTT/CLAIM_EVIDENCE_MATRIX.md": R.sha((root / "HoTT/CLAIM_EVIDENCE_MATRIX.md").read_bytes()),
        "scripts/audit/verify_math_proof_delivery_governance.py": R.sha((root / "scripts/audit/verify_math_proof_delivery_governance.py").read_bytes()),
    }
    state["records"]["A-MATH-PROOF-DELIVERY-GATE-001"] = {
        "kind": "governance_requirement",
        "path": SPEC_PATH,
        "status": "active",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "behavior_status": "FRESH_MODEL_NOT_RUN",
        "depends_on": ["A-LOAD-GOVERNANCE-V3-001"],
        "full_sources": [
            "AGENTS.md", ".codex/AGENTS.md", "rulings.md", "feature-list.md", SPEC_PATH,
            ".codex/cognition/PROTOCOL.md", ".codex/skills/hott-local-session-governance/SKILL.md",
            ".codex/skills/hott-paradox-research/SKILL.md", "HoTT/formal/README.md",
            "HoTT/verification/runs/README.md", "HoTT/CLAIM_EVIDENCE_MATRIX.md",
            "scripts/audit/verify_math_proof_delivery_governance.py",
            "scripts/audit/test_math_proof_delivery_governance.py", EVIDENCE,
        ],
        "source_hashes": hashes,
        "scope": "Require every current-AI mathematical conclusion to have a semantically matching machine proof before delivery, with proof source, raw kernel run evidence and claim index persisted in this repo; otherwise force a non-conclusion status.",
    }

    session_path = f"{R.PREFIX}sessions/{SESSION_ID}/SESSION.md"
    audit_path = f"{R.PREFIX}sessions/{SESSION_ID}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{R.PREFIX}sessions/{SESSION_ID}/RUNS.json"
    state["records"][SESSION_ID] = {
        "kind": "session", "path": session_path, "status": "complete",
        "lifecycle_status": "HISTORICAL", "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": ["S-RES-20260912-025-MINIMAL-WITNESS-PRECONDITIONS", "A-MATH-PROOF-DELIVERY-GATE-001"],
        "full_sources": [session_path, audit_path, runs_path, SPEC_PATH, EVIDENCE, "scripts/audit/prepare_math_proof_delivery_gate_checkpoint.py"],
        "source_hashes": {},
        "mathematical_status": "NO_MATHEMATICAL_CONCLUSION_GOVERNANCE_ONLY",
        "cognition_status": "MATH_PROOF_BEFORE_DELIVERY_POLICY_ROUTED_AND_STATICALLY_VERIFIED",
        "scope": "Persist the user's proof-before-delivery requirement in AGENTS, establish repo-local proof source/run/index ownership, force unproved claims to non-conclusion states, update projections/state and audit all 36 KC.",
    }
    session = f"""# {SESSION_ID}

- 触发：用户要求把“所有当前 AI 数学结论交付前必须机器证明，证明代码和结果必须留在项目并索引，不得只放 `/tmp`”写入项目 AGENTS。
- 决策：F-011 为 accepted project requirement；core 不变，因为这是一般治理裁定而非新的悖论/元数学正文。
- 实现：根/`.codex` AGENTS、PROTOCOL 2.2、治理 Skill 3.2、业务 Skill 1.7、稳定 quality 规范、formal/run/index owner、README/docs/Feature/ruling。
- 验证：4/4 static 正负向测试和 verifier PASS；缺 Skill marker、`/tmp` authority、缺 stderr 合同均被拒绝。
- 边界：本轮没有数学结论，不生成伪 proof package；C4 仍 `PAPER_ONLY`；fresh model behavior、首个真实数学 package 和 Git version-close 均开放。
- Git：未 commit、未 tag、未 push。
"""
    runs = json.dumps({
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID,
        "requirement": "F-011 MATH_PROOF_BEFORE_DELIVERY_V1",
        "software_verification": {
            "unit_tests": "4/4 PASS",
            "static_verifier": "PASS_WITH_SCOPE marker_files=9",
            "negative_cases": ["missing business Skill marker", "authoritative /tmp run root", "missing stderr.txt contract"],
        },
        "mathematics": "NO_MATHEMATICAL_CONCLUSION_THIS_SESSION",
        "proof_package": "NOT_APPLICABLE_GOVERNANCE_ONLY",
        "post_checkpoint_required": ["36/36 KC audit", "three-way 27/27 references", "fresh receipt revision 26", "projection freshness", "static gate tests", "full regression", "git diff --check"],
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    texts = {
        "MEMORY.md": memory, R.DIRECTION: direction, R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier, f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume, R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session, audit_path: audit_text(root), runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID,
        "authorization": "The user explicitly requested this project-local proof-before-delivery governance rule and repo-local proof/result/index retention; updating current projections, state, memory and the per-KC audit is required by the existing project checkpoint protocol.",
        "load_profile": "governance", "task_ids": [],
        "files": [
            {"path": rel, "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None, "text": value}
            for rel, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": 26, "session_id": SESSION_ID, "files": len(texts)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
