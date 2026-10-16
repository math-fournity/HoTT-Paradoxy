#!/usr/bin/env python3
"""Prepare revision 46: record the N4 candidate generation and route N5.

N4 generated candidates over DIR01-DIR09 x OP01-OP08, eliminated the
ua-regularity candidate with a real Cubical probe, and selected the
derived-development consumer audit (N5) as the next work package.
Paper-only; no mathematical claim is upgraded.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SESSION_ID = "S-RES-20260912-046-NEW-CANDIDATES"
PREV_SESSION = "S-RES-20260912-045-TRANSITION-LIFT"
RESULT_ID = "A-NEW-CANDIDATES-001"
C6 = "理解章节/C6-新候选生成与派生开发消费者审计-20260912.md"
MERGE = "audit/understanding-chapter-merge-manifest.json"
PROBE = f".codex/research/hott/sessions/{SESSION_ID}/evidence/agda/UAProbe.agda"
MATRIX = "HoTT/CLAIM_EVIDENCE_MATRIX.md"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
NEW_STATUS = "NEW_CANDIDATES_GENERATED_DERIVED_DEVELOPMENT_AUDIT_NEXT"

SPEC = importlib.util.spec_from_file_location("runtime_new_candidates", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sub_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    if count != 1:
        raise ValueError(f"SUB_COUNT:{count}:{old[:80]}")
    return text.replace(old, new, 1)


def audit_text(root: Path) -> str:
    manifest = json.loads((root / "核心认知.manifest.json").read_text(encoding="utf-8"))
    touched = {
        "KC-000005": ("ALIGNED", "N4 继续以“先找具体机制”为目标，不把一般计算界限改名为 HoTT 悖论。"),
        "KC-000008": ("DEEPENED", "历史悖论只作启发；候选改为按 DIR×OP 与 HoTT 规则钩子生成。"),
        "KC-000010": ("ALIGNED", "候选矩阵继续服务现实相对非现实性目标，并明确区分 defense/boundary/candidate。"),
        "KC-000012": ("DEEPENED", "ASK 被写成候选四项门槛与 E6 目标；没有真实接口承诺不得升级。"),
        "KC-000013": ("ALIGNED", "理论经济/遗忘在候选矩阵中作为抽象维度登记，而不是结论。"),
        "KC-000014": ("ALIGNED", "方向 B 的派生开发自述成为 N5 的审计对象。"),
        "KC-000022": ("ALIGNED", "两类现实相对框架保持不变；候选未升级为已完成目标。"),
        "KC-000027": ("ALIGNED", "HoTT 继承程序界限的候选仍要求 HoTT 规则进入关键步骤。"),
        "KC-000029": ("DEEPENED", "理论经济候选（SIP/表示、quotient 商）被明确登记为待证机制。"),
        "KC-000036": ("ALIGNED", "ERCF-3 继续 gated；自指候选未被提前启动。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> 状态：`MANUAL_SEMANTIC_REVIEW_COMPLETE_WITH_SCOPE`；generation：`{manifest['generation']}`；KC 总数：`{len(manifest['units'])}`。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |", "|---|---|---|---|---|---|",
    ]
    aligned = deepened = 0
    for unit in manifest["units"]:
        label = str(unit["semantic_label"]).replace("|", "\\|")
        relation, assessment = touched.get(
            unit["id"],
            ("NOT_TOUCHED", "本轮是 N4 候选生成；未研究、改写或重新裁决该条用户原文。"),
        )
        aligned += relation == "ALIGNED"
        deepened += relation == "DEEPENED"
        lines.append(
            f"| `{unit['id']}` | `{unit['platform']}` / {label} | `{relation}` | {assessment} | S046/SESSION.md；理解章节/C6-新候选生成与派生开发消费者审计-20260912.md | N5、ERCF-3 与其它接口仍开放。 |"
        )
    not_touched = len(manifest["units"]) - aligned - deepened
    lines.extend([
        "", "## 三件套交叉与更新归属", "",
        "- core_change: `NO` — generation-4/36 KC 不变，本轮没有新的用户原文。",
        "- direction_change: `YES` — N4 候选生成完成；第一工作包转 N5 派生开发消费者审计；revision 46/generation 030。",
        "- panorama_change: `YES` — 新增 `OUT-TOP-CANDIDATE-GENERATION`；理解章节 inventory 更新为 31/24。",
        "- update_decision: `C6 与 UA regularity 探针进入 audit/理解章节；候选池收敛到五个短名单；`CAND-REGULARITY` 在该工具链实测排除。`",
        "- cross_conflicts: `NONE_OBSERVED` — claim matrix 未变；探针结果与该工具链一致。",
        "- unresolved: `N5、type-quotient/Cauchy 备选、ERCF-3、fresh model behavior 与 Git version-close 仍开放。`",
        "", "## 汇总", "",
        f"`ALIGNED={aligned}`、`DEEPENED={deepened}`、`NOT_TOUCHED={not_touched}`；本轮无新数学结论，状态为 `CANDIDATES_GENERATED_WITH_ONE_PROBE_ELIMINATION`。", "",
    ])
    return "\n".join(lines)


def session_text() -> str:
    return "\n".join([
        f"# {SESSION_ID}",
        "",
        "- 触发：S045 后的 N4 工作包（新候选生成）。",
        "- 方法：DIR01–DIR09 × OP01–OP08；每个候选必须写出 HoTT 规则钩子、任务、抽象、下游操作与 E6 目标；不得改名重述既有反例。",
        "- 探针：`UAProbe.agda` 在 Cubical Agda 2.8.0/Cubical v0.9 中 exit 0；`transport (ua idEquiv) true` 与 `transport (ua notEquiv) true` 都可定义性归约；`CAND-REGULARITY` 在该工具链实测排除。",
        "- 候选池：`CAND-TRUNCATION-COHERENCE`、`CAND-TYPEQUOT-SECTION`、`CAND-CAUCHY-MODULUS`、`CAND-SIP-REPRESENTATION`、`CAND-PATH-INVERSE-ROLLBACK`、`CAND-FINITE-INFINITE-CHOICE`、`CAND-QUOTIENT-EFFECTIVE-EXTENSION`、`CAND-ERASURE-PHASE`、`CAND-DERIVED-DEVELOPMENT`。",
        "- 选择：N5 派生开发消费者审计（固定论文/库版本，逐条核对“可计算/可提取/可序列化/可交付”自述的假设）。",
        "- 边界：本轮无新数学结论；候选仅为研究位置。",
        "- 三件套：direction/panorama revision 46/generation 030；core 不变（无新用户原文）。",
        "- Git：未 commit、未 tag、未 push。",
        "",
    ])


def apply_projection_edits(root: Path) -> dict[str, str]:
    direction = (root / R.DIRECTION).read_text(encoding="utf-8")
    direction = sub_once(
        direction,
        "状态：`CORE_GENERATION_4_TRANSITION_LIFT_PROVED_NEW_CANDIDATE_GENERATION_NEXT`",
        "状态：`CORE_GENERATION_4_NEW_CANDIDATES_GENERATED_DERIVED_DEVELOPMENT_AUDIT_NEXT`",
    )
    direction = sub_once(direction, "source_state_revision: 45", "source_state_revision: 46")
    direction = sub_once(direction, "projection_generation: 20260912-direction-029", "projection_generation: 20260912-direction-030")
    direction = sub_once(
        direction,
        "semantic_status: CORE_GENERATION_4_TRANSITION_LIFT_PROVED_NEW_CANDIDATE_GENERATION_NEXT",
        "semantic_status: CORE_GENERATION_4_NEW_CANDIDATES_GENERATED_DERIVED_DEVELOPMENT_AUDIT_NEXT",
    )
    direction = sub_once(
        direction,
        "；`MP-ONLINE-CAUSALITY-001` 原生给出在线因果资格边界（`C-106`–`C-109`）。",
        "；`MP-ONLINE-CAUSALITY-001` 原生给出在线因果资格边界（`C-106`–`C-109`）；`MP-TRANSITION-LIFT-001` 原生证明 R036/R038 核心边界（`C-110`–`C-117`：过渡抽象/极限）。",
    )
    direction = sub_once(
        direction,
        "4. **当前第一工作包**：N4 新候选生成——按 `hott-paradox-research` 的 OP01–OP08 与 DIR01–DIR09 对未触达方向（先后/依赖、形成资格、历史/来源、方向/不可逆、运动/连续、自指）系统生成候选；每个候选必须固定 HoTT 配置、任务、抽象与后续操作，关键步骤必须让 UA/Id/HIT/Π 或 truncation 真正参与，并直接指向 E6（natural consumer）；不得改名重述 R036/R038/R034/race-timeout 的既有反例。",
        "4. **当前第一工作包**：N5 派生开发消费者审计——固定论文/库版本与 hash，逐条提取派生开发对自身构造的“可计算/可提取/可序列化/可交付”承诺，核对所需假设（choice、modulus、section、coherence）是否在接口中显式；输出 `FOUND_CANDIDATE` / `BOUNDED_DEFENSE` / `INCONCLUSIVE_SOURCE_UNAVAILABLE`；只有找到候选才进入 F-011 机器化，备选为 `CAND-TYPEQUOT-SECTION`。",
    )

    panorama = (root / R.PANORAMA).read_text(encoding="utf-8")
    panorama = sub_once(
        panorama,
        "状态：`CORE_GENERATION_4_TRANSITION_LIFT_PROVED_NEW_CANDIDATE_GENERATION_NEXT`",
        "状态：`CORE_GENERATION_4_NEW_CANDIDATES_GENERATED_DERIVED_DEVELOPMENT_AUDIT_NEXT`",
    )
    panorama = sub_once(panorama, "source_state_revision: 45", "source_state_revision: 46")
    panorama = sub_once(panorama, "projection_generation: 20260912-outcome-029", "projection_generation: 20260912-outcome-030")
    panorama = sub_once(
        panorama,
        "semantic_status: CORE_GENERATION_4_TRANSITION_LIFT_PROVED_NEW_CANDIDATE_GENERATION_NEXT",
        "semantic_status: CORE_GENERATION_4_NEW_CANDIDATES_GENERATED_DERIVED_DEVELOPMENT_AUDIT_NEXT",
    )
    row = (
        "| `OUT-TOP-CANDIDATE-GENERATION` | N4 新候选生成：DIR01–DIR09 × OP01–OP08 候选矩阵；`CAND-REGULARITY`（ua regularity）由 Cubical 2.8.0 探针实测排除；候选池收敛到 type-quotient section、Cauchy modulus、SIP 表示、有限/无限选择、派生开发自述五类 |"
        " `DIR-TOP-QUALIFICATION-PRESERVATION`、`DIR-L-TIME-WORK-DIMENSION`、`DIR-G-MATH-PROOF-DELIVERY-GATE` |"
        " 当前人工生成 | `DOCUMENTED` |"
        " 候选写入固定字段（HoTT 钩子/任务/抽象/下游操作/E6 目标）；`UAProbe.agda` 实际运行 exit 0；排除规则与停止条件已写明 |"
        " 候选不是数学结论；`CAND-REGULARITY` 的排除只覆盖该工具链与所列探针 |"
        " `理解章节/C6-新候选生成与派生开发消费者审计-20260912.md`；S046 evidence/agda/UAProbe.agda |\n"
    )
    panorama = sub_once(panorama, "| `OUT-TOP-CORE-FOUNDATION` |", row + "| `OUT-TOP-CORE-FOUNDATION` |")
    panorama = sub_once(
        panorama,
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 30/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C5 共 6 个独有文件（nonidentical union entries=15）；逐文件处置已生成 |",
        "| `OUT-UNDERSTANDING-MERGE` | 两个理解章节目录当前为 31/24 文件 inventory；24 个同名对中 15 对字节相同、9 对差异；顶层 C0–C6 共 7 个独有文件（nonidentical union entries=16）；逐文件处置已生成 |",
    )
    panorama = sub_once(
        panorama,
        "C3/C4/C5 为 top-level current AI strategy/research synthesis，nested 历史源仍保留 | 不推出数学内容等价，不删除历史源，不把 line diff 代替人工数学语义判断；2,396 条旧 claim 未因 C4/C5 自动裁决 |",
        "C3/C4/C5/C6 为 top-level current AI strategy/research synthesis，nested 历史源仍保留 | 不推出数学内容等价，不删除历史源，不把 line diff 代替人工数学语义判断；2,396 条旧 claim 未因 C4/C5/C6 自动裁决 |",
    )
    panorama = sub_once(
        panorama,
        "N4 新候选生成、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
        "N4 新候选生成已完成（C6，含 `CAND-REGULARITY` 实测排除）；N5 派生开发消费者审计、R032 回放、B01-TARGET 的其它接口、有效自我 ASK、具体发散、coverage no-go 与 ERCF-3/Gödel 内部化仍未完成。",
    )

    frontier = (root / f"{R.PREFIX}FRONTIER.md").read_text(encoding="utf-8")
    frontier = sub_once(
        frontier,
        "N3 把 R036/R038 核心边界原生机器化（C-110–C-117，零 warning），判 `TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`。所有新结论继续执行 F-011。",
        "N3 把 R036/R038 核心边界原生机器化（C-110–C-117，零 warning），判 `TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`；N4 生成 DIR×OP 候选矩阵并用 Cubical 探针排除 ua-regularity 候选。所有新结论继续执行 F-011。",
    )
    frontier = sub_once(
        frontier,
        "| 第一工作包 | N4 新候选生成（DIR01–DIR09 × OP01–OP08） | generation / paper-first | 对未触达方向系统生成候选；每个候选固定 HoTT 配置/任务/抽象/后续操作，关键步骤必须使用 UA/Id/HIT/Π 或 truncation，并直接指向 E6；不得改名重述既有反例 |",
        "| 第一工作包 | N5 派生开发消费者审计 | audit / paper-and-library-evidence | 固定论文/库版本与 hash，逐条核对派生开发对“可计算/可提取/可序列化/可交付”的自述是否超出接口资格；输出 `FOUND_CANDIDATE`/`BOUNDED_DEFENSE`/`INCONCLUSIVE_SOURCE_UNAVAILABLE`；备选 `CAND-TYPEQUOT-SECTION` |",
    )

    memory = (root / "MEMORY.md").read_text(encoding="utf-8")
    memory = sub_once(
        memory,
        "2. 当前第一工作包转为 N4 新候选生成：按 OP01–OP08 × DIR01–DIR09 对未触达方向系统生成候选；每个候选固定 HoTT 配置/任务/抽象/后续操作，关键步骤必须让 UA/Id/HIT/Π 或 truncation 真正参与，并直接指向 E6（natural consumer）；不得改名重述既有反例。",
        "2. 当前第一工作包转为 N5 派生开发消费者审计：固定论文/库版本与 hash，逐条核对派生开发对“可计算/可提取/可序列化/可交付”的自述是否超出接口资格；输出 `FOUND_CANDIDATE`/`BOUNDED_DEFENSE`/`INCONCLUSIVE_SOURCE_UNAVAILABLE`；备选 `CAND-TYPEQUOT-SECTION`。",
    )
    memory = sub_once(
        memory,
        "- N3 过渡抽象/极限边界（S045）已由 `MP-TRANSITION-LIFT-001` 原生机器化：C-110–C-117，零 warning、exact replay；十个旧包在矩阵增长后全部 row-stable；`DIR-W-TRANSITION-ABSTRACTION` 与 `DIR-W-CURRENT-STATE-LIFT` 转 `CLOSED_WITH_SCOPE`。",
        "- N3 过渡抽象/极限边界（S045）已由 `MP-TRANSITION-LIFT-001` 原生机器化：C-110–C-117，零 warning、exact replay；十个旧包在矩阵增长后全部 row-stable；`DIR-W-TRANSITION-ABSTRACTION` 与 `DIR-W-CURRENT-STATE-LIFT` 转 `CLOSED_WITH_SCOPE`。\n"
        "- N4 新候选生成（S046）：DIR01–DIR09 × OP01–OP08 候选矩阵与五个短名单；`CAND-REGULARITY` 由 Cubical 2.8.0 探针实测排除；下一工作包转 N5 派生开发消费者审计。",
    )
    memory = sub_once(
        memory,
        "`A-RP-B01-EXTRACTION-AUDIT-001`、`A-TRANSITION-LIFT-FORMAL-001`。六条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 把 R036/R038 核心边界原生机器化并转 N4 新候选生成，不直接跳 ERCF-3。",
        "`A-RP-B01-EXTRACTION-AUDIT-001`、`A-TRANSITION-LIFT-FORMAL-001`、`A-NEW-CANDIDATES-001`。六条机器支线（partiality、guard-erasure、cost、路径证书、在线因果、过渡抽象/极限）均已闭合；C5 固定第二级距离，N1 给出 bounded negative，N2 给出 scoped `DEFENSE_WORKS`，N3 关闭过渡边界，N4 生成候选并转 N5 派生开发消费者审计，不直接跳 ERCF-3。",
    )

    resume = (root / f"{R.PREFIX}RESUME.md").read_text(encoding="utf-8")
    resume = sub_once(
        resume,
        "## 当前停止点\n\n",
        "## 当前停止点\n\n"
        "S046 完成 N4 新候选生成：DIR01–DIR09 × OP01–OP08 候选矩阵与五个短名单；`CAND-REGULARITY`（ua regularity）由 Cubical Agda 2.8.0/Cubical v0.9 探针实测排除。下一工作包为 N5 派生开发消费者审计（固定论文/库版本，核对“可计算/可提取/可序列化/可交付”自述的假设）；备选 `CAND-TYPEQUOT-SECTION`。ERCF-3 继续 gated。\n\n",
    )

    lessons = (root / f"{R.PREFIX}LESSONS.md").read_text(encoding="utf-8")
    lessons = sub_once(
        lessons,
        "44. 原生升级旧的有限检查边界时，先固定 claim 映射与禁止外推，再处理实现警告：把索引归纳族改成构造子递归的函数定义（如 `_≤_`）可消除 `UnsupportedIndexedMatch` 而不改变命题；矩阵追加新 proof 后必须重放全部旧包并保持 row-stable，不能只验证新包。",
        "44. 原生升级旧的有限检查边界时，先固定 claim 映射与禁止外推，再处理实现警告：把索引归纳族改成构造子递归的函数定义（如 `_≤_`）可消除 `UnsupportedIndexedMatch` 而不改变命题；矩阵追加新 proof 后必须重放全部旧包并保持 row-stable，不能只验证新包。\n"
        "45. 候选生成必须先用最小探针排除可证伪的机制：`ua` regularity 在 Cubical Agda 2.8.0/Cubical v0.9 中由 `probe-regular = refl` 直接排除，不能靠文献印象保留。N1–N3 表明核心库接口系统性防御；E6 更可能在派生开发对自身构造的承诺中，因此 N5 审计派生开发而不是继续重审核心库。",
    )
    return {
        "MEMORY.md": memory,
        R.DIRECTION: direction,
        R.PANORAMA: panorama,
        f"{R.PREFIX}FRONTIER.md": frontier,
        f"{R.PREFIX}LESSONS.md": lessons,
        f"{R.PREFIX}RESUME.md": resume,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, default=ROOT)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = args.project_root.resolve()

    plan = R.plan(root, profile="governance")
    state = json.loads((root / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != 45 or state.get("latest_session") != PREV_SESSION:
        raise SystemExit("EXPECTED_REVISION_45_AND_S045")
    for required in (C6, MERGE, PROBE, MATRIX):
        if not (root / required).is_file():
            raise SystemExit(f"REQUIRED_FILE_MISSING:{required}")
    merge = json.loads((root / MERGE).read_text(encoding="utf-8"))
    if merge.get("counts", {}).get("union_files") != 31 or merge.get("counts", {}).get("top_level_unique") != 7:
        raise SystemExit("MERGE_MANIFEST_NOT_REBUILT_FOR_C6")

    new_hashes = {C6: sha(root / C6), MERGE: sha(root / MERGE), PROBE: sha(root / PROBE), MATRIX: sha(root / MATRIX)}
    observed_stale: list[tuple[str, str]] = []
    for rid, rec in state["records"].items():
        for rel, exp in rec.get("source_hashes", {}).items():
            path = root / rel
            current = sha(path) if path.is_file() else None
            if current != exp:
                observed_stale.append((rid, rel))
    unexpected = sorted({rel for _, rel in observed_stale} - {MERGE})
    if unexpected:
        raise SystemExit(f"UNEXPECTED_STALE:{unexpected}")
    for rid, rel in observed_stale:
        state["records"][rid].setdefault("source_hashes", {})[rel] = new_hashes[rel]
        state["records"][rid]["revalidation"] = "The understanding-chapter merge manifest was rebuilt after C6 was added; the record's scope is unchanged."
    session_path = f"{SESSION_REL}/SESSION.md"
    audit_path = f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"
    runs_path = f"{SESSION_REL}/RUNS.json"

    state["records"][RESULT_ID] = {
        "kind": "candidate_generation",
        "path": C6,
        "status": "complete",
        "lifecycle_status": "CURRENT",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "classification": "CANDIDATES_GENERATED_WITH_UA_REGULARITY_PROBE_ELIMINATION",
        "full_sources": [C6, MERGE, PROBE, MATRIX,
                         "audit/natural-consumer审计-20260912.md",
                         "audit/rp-b01-extraction-interface审计-20260912.md",
                         "HoTT/formal/transition-lift/TransitionLift.agda"],
        "source_hashes": {C6: new_hashes[C6], MERGE: new_hashes[MERGE], PROBE: new_hashes[PROBE], MATRIX: new_hashes[MATRIX]},
        "resolution": {
            "reason": "Candidate matrix generated over DIR01-DIR09 x OP01-OP08; UAProbe.agda (exit 0) eliminated the ua-regularity candidate in Cubical Agda 2.8.0/Cubical v0.9; N5 derived-development audit selected.",
            "evidence": [C6, PROBE, MERGE],
        },
        "scope": "Paper-only candidate generation for N4; no mathematical claim; CAND-REGULARITY excluded only for the probed toolchain; N5 routed.",
    }

    state["records"][SESSION_ID] = {
        "kind": "session",
        "path": session_path,
        "status": "complete",
        "lifecycle_status": "HISTORICAL",
        "evidence_status": "VERIFIED_WITH_SCOPE",
        "depends_on": [PREV_SESSION, RESULT_ID],
        "full_sources": [session_path, audit_path, runs_path, C6, MERGE, PROBE, MATRIX],
        "source_hashes": {C6: new_hashes[C6], PROBE: new_hashes[PROBE], MERGE: new_hashes[MERGE]},
        "mathematical_status": "NO_NEW_MATHEMATICS_CANDIDATE_GENERATION",
        "cognition_status": "NEW_CANDIDATES_GENERATED_AND_DERIVED_DEVELOPMENT_AUDIT_ROUTED",
        "scope": "Generate candidates over DIR01-DIR09 x OP01-OP08, run the ua-regularity probe, select N5; no claim upgrade.",
    }

    for rid in ("I-DIRECTION-PORTFOLIO-20260912", "I-OUTCOME-PANORAMA-20260912"):
        rec = state["records"][rid]
        rec["projection_generation"] = "20260912-direction-030" if rid.startswith("I-DIRECTION") else "20260912-outcome-030"
        rec["semantic_status"] = "CORE_GENERATION_4_" + NEW_STATUS
        for rel in (C6, MERGE, PROBE):
            if rel not in rec["full_sources"]:
                rec["full_sources"].append(rel)
    state["records"]["I-DIRECTION-PORTFOLIO-20260912"]["scope"] = (
        "Portfolio after N4 candidate generation: five shortlisted candidate families; the first work package is the N5 derived-development consumer audit."
    )
    state["records"]["I-OUTCOME-PANORAMA-20260912"]["scope"] = (
        "Panorama includes the N4 candidate-generation result and the ua-regularity probe elimination; the next strand is N5."
    )

    state["revision"] = 46
    state["latest_session"] = SESSION_ID
    state["execution_control"].update({
        "last_checkpoint_session": SESSION_ID,
        "checkpoint_result": "CHECKPOINT_APPLIED_PENDING_GIT_COMMIT",
        "status": NEW_STATUS,
        "next_minimal_verification": (
            "N5: audit derived developments (fixed versions/URLs/hashes) for self-claims of computation/extraction/serialization/delivery beyond their interfaces. "
            "Sources: Partiality Revisited (arXiv:1610.09254), Quotienting the delay monad (MSCS 29(1)), What Monads Can and Cannot Do (arXiv:2311.15919), "
            "Cost-Aware Type Theory (arXiv:2011.03660), and available HoTT-derived developments. For each claim, record the exact locator and interface signature, "
            "check whether choice/modulus/section/coherence assumptions are explicit, and output FOUND_CANDIDATE / BOUNDED_DEFENSE / INCONCLUSIVE_SOURCE_UNAVAILABLE. "
            "Only FOUND_CANDIDATE enters F-011 machine formalisation; the fallback machine construction is CAND-TYPEQUOT-SECTION."
        ),
    })
    state["projection"]["status"] = "CORE_GENERATION_4_" + NEW_STATUS

    runs = json.dumps({
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "kind": "candidate_generation",
        "new_machine_proofs": [],
        "proof_sources_changed": False,
        "claim_matrix_sha256": new_hashes[MATRIX],
        "probe": {"file": PROBE, "tool": "Agda 2.8.0-3d04bac + Cubical v0.9", "exit_code": 0,
                  "result": "transport (ua idEquiv) true and transport (ua notEquiv) true both reduce definitionally; CAND-REGULARITY eliminated for this toolchain"},
        "evidence": {"c6": C6, "merge_manifest": MERGE, "probe": PROBE, "matrix": MATRIX},
        "mathematics": "NO_NEW_MATHEMATICS / CANDIDATES_ONLY",
        "git_commit": "NOT_AUTHORIZED_THIS_TURN",
    }, ensure_ascii=False, indent=2) + "\n"

    edited = apply_projection_edits(root)
    texts = {
        **edited,
        R.STATE: json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n",
        session_path: session_text(),
        audit_path: audit_text(root),
        runs_path: runs,
    }
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": (
            "User goal: pursue the HoTT-paradox research, keep the trio current after each result and coordinate the next package. "
            "This in-scope checkpoint records the N4 candidate generation (C6), the ua-regularity probe elimination, and the N5 derived-development audit route. "
            "No mathematical claim is upgraded. No Git commit, tag or push."
        ),
        "load_profile": "governance",
        "task_ids": [],
        "files": [
            {
                "path": rel,
                "expected_sha256": R.sha((root / rel).read_bytes()) if (root / rel).exists() else None,
                "text": value,
            }
            for rel, value in texts.items()
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "PREPARED",
        "snapshot": plan["snapshot"],
        "revision": 46,
        "session_id": SESSION_ID,
        "merge_union_files": merge["counts"]["union_files"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
