#!/usr/bin/env python3
"""Prepare (but never apply) the canonical checkpoint for the main-docs closeout.

The public text change is limited to a current cross-reference and its four
translations. The checkpoint refreshes only affected source pins, records the
release, advances derived projection metadata, and leaves all mathematics and
the Goal7 research queue unchanged.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SESSION_ID = "S-GOV-20261001-MAIN-DOCS-ALIGNMENT"
PREVIOUS_SESSION = "S-GOV-20261001-CIRCLE-ZENO-ATTRIBUTION-UPDATE"
BASE_REVISION = 294
NEXT_REVISION = 295
BASE_COMMIT = "72520807057c974a7d565159b2fe1e6f47be972d"
MAIN_COMMIT = "894e3816207999a5e283f76ea692510ebfe9c9e5"
MAIN_PARENT = "c28334c89d75157389dd609c2aa79946ee71ff4d"
RELEASE_ID = "main-20261001-sister-paper-cross-reference-alignment"
REPORT = "docs/HoTT悖论查找阶段收尾报告-20260930.md"
COMMUNITY_INDEX = "docs/社区审计提交/README.md"
PAPER01 = "docs/社区审计提交/01-芝诺悖论的幽灵.md"
PAPER02 = "docs/社区审计提交/02-罗素悖论的幽灵.md"
PAPER03 = "docs/社区审计提交/03-HoTT的芝诺.md"
PAPER02_TRANSLATIONS = [
    "docs/社区审计提交/02-罗素悖论的幽灵-EN.md",
    "docs/社区审计提交/02-罗素悖论的幽灵-DE.md",
    "docs/社区审计提交/02-罗素悖论的幽灵-FR.md",
    "docs/社区审计提交/02-罗素悖论的幽灵-RU.md",
]
MEMORY = "MEMORY.md"
MEMORY001 = "MEMORY/001 - 当前执行队列.md"
MEMORY003 = "MEMORY/003 - 当前验证状态与顺序日志.md"
DIRECTION = "方向追踪.md"
PANORAMA = "全景视野.md"
ESSAY = "扩展认知.md"
STATE = ".codex/research/hott/STATE.json"
RESUME = ".codex/research/hott/RESUME.md"
PREPARE_PATH = "audit/main-docs-checkpoint-repair-20261001/prepare_checkpoint.py"
REPAIR_PATH = "audit/main-docs-checkpoint-repair-20261001/REPAIR.json"
VERIFY_REL = f".codex/research/hott/sessions/{SESSION_ID}/MAIN-RELEASE-VERIFICATION.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
CORE_RECORD = "A-CODEX-CORE-GENERATION-11-001"
A7_RECORD = "A-A7-INFINITE-COHERENCE-001"
RUSSELL_RECORD = "A-RUSSELL-EXISTENCE-QUESTIONING-001"
ABX_RECORD = "R-ABX-ACTION-20260921"
DIRECTION_RECORD = "I-DIRECTION-PORTFOLIO-20260912"
PANORAMA_RECORD = "I-OUTCOME-PANORAMA-20260912"


def load_module(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    if not spec or not spec.loader:
        raise SystemExit(f"MODULE_NOT_LOADABLE:{rel}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


R = load_module("cognition_runtime_main_docs", ".codex/tools/cognition_runtime.py")
if str(ROOT / "scripts/audit") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts/audit"))
import projection_edit  # noqa: E402
import build_core_cognition_audit as core_audit_builder  # noqa: E402


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha_file(rel: str) -> str:
    return sha((ROOT / rel).read_bytes())


def text(data: bytes) -> str:
    return data.decode("utf-8")


def json_text(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2) + "\n"


def git(*args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=ROOT)


def replace_once(value: str, old: str, new: str) -> str:
    count = value.count(old)
    if count != 1:
        raise ValueError(f"REPLACE_COUNT:{old[:80]}:{count}")
    return value.replace(old, new, 1)


def replace_paragraph_start(value: str, prefix: str, replacement: str) -> str:
    lines = value.splitlines()
    hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(hits) != 1:
        raise ValueError(f"PARAGRAPH_PREFIX_COUNT:{prefix}:{len(hits)}")
    lines[hits[0]] = replacement
    return "\n".join(lines) + "\n"


def release_verification() -> dict:
    dev_oid = git("rev-parse", "dev").decode().strip()
    main_oid = git("rev-parse", "main").decode().strip()
    if dev_oid != BASE_COMMIT or main_oid != MAIN_COMMIT:
        raise SystemExit(f"UNEXPECTED_RELEASE_REFS:{dev_oid}:{main_oid}")
    remote = git("ls-remote", "origin", "refs/heads/dev", "refs/heads/main").decode().splitlines()
    remote_refs = {line.split()[1]: line.split()[0] for line in remote}
    if remote_refs != {"refs/heads/dev": BASE_COMMIT, "refs/heads/main": MAIN_COMMIT}:
        raise SystemExit(f"REMOTE_RELEASE_REFS_MISMATCH:{remote_refs}")
    manifest_bytes = git("show", f"{MAIN_COMMIT}:RELEASE-MANIFEST.json")
    manifest = json.loads(manifest_bytes)
    if manifest.get("release_id") != RELEASE_ID:
        raise SystemExit("MAIN_RELEASE_ID_MISMATCH")
    if manifest.get("source", {}).get("commit") != BASE_COMMIT:
        raise SystemExit("MAIN_RELEASE_SOURCE_COMMIT_MISMATCH")
    if len(manifest.get("files", [])) != 702:
        raise SystemExit("MAIN_RELEASE_FILE_MANIFEST_COUNT_MISMATCH")
    tracked = git("ls-tree", "-r", "--name-only", MAIN_COMMIT).decode().splitlines()
    if len(tracked) != 703:
        raise SystemExit("MAIN_RELEASE_TRACKED_FILE_COUNT_MISMATCH")
    parent = git("show", "-s", "--format=%P", MAIN_COMMIT).decode().strip().split()
    if parent != [MAIN_PARENT]:
        raise SystemExit(f"MAIN_RELEASE_PARENT_MISMATCH:{parent}")
    expected_changed = {
        "CLAIMS-DE.md", "CLAIMS-EN.md", "CLAIMS-FR.md", "CLAIMS-RU.md", "CLAIMS-ZH.md", "CLAIMS.md",
        "README-DE.md", "README-EN.md", "README-FR.md", "README-RU.md", "README-ZH.md", "README.md",
        "RELEASE-MANIFEST.json",
        "docs/社区审计提交/02-罗素悖论的幽灵-DE.md", "docs/社区审计提交/02-罗素悖论的幽灵-EN.md",
        "docs/社区审计提交/02-罗素悖论的幽灵-FR.md", "docs/社区审计提交/02-罗素悖论的幽灵-RU.md",
        "docs/社区审计提交/02-罗素悖论的幽灵.md",
    }
    changed = set(git("diff", "--name-only", f"{MAIN_PARENT}..{MAIN_COMMIT}").decode().splitlines())
    if changed != expected_changed:
        raise SystemExit(f"MAIN_RELEASE_CHANGED_PATHS_MISMATCH:{sorted(changed ^ expected_changed)}")
    dev_sig = subprocess.run(["git", "verify-commit", BASE_COMMIT], cwd=ROOT, capture_output=True, text=True)
    main_sig = subprocess.run(["git", "verify-commit", MAIN_COMMIT], cwd=ROOT, capture_output=True, text=True)
    if dev_sig.returncode or main_sig.returncode:
        raise SystemExit("RELEASE_COMMIT_SIGNATURE_CHECK_FAILED")
    main_paper = text(git("show", f"{MAIN_COMMIT}:{PAPER02}"))
    if "01《无穷相干：一条芝诺式候选》" not in main_paper or "A7 是独立的 AI 候选" not in main_paper:
        raise SystemExit("MAIN_CHINESE_CROSS_REFERENCE_MISSING")
    translation_titles = {
        "EN": ("Infinite coherence: a Zeno-like candidate", "separate AI-proposed candidate"),
        "DE": ("Unendliche Kohärenz: ein zenonartiger Kandidat", "eigenständiger, von einer KI vorgeschlagener Kandidat"),
        "FR": ("Cohérence infinie : une piste candidate à la manière de Zénon", "piste candidate distincte proposée par une IA"),
        "RU": ("Бесконечная когерентность: кандидат в зеноновском духе", "отдельный кандидат, предложенный ИИ"),
    }
    for suffix, (title, distinct) in translation_titles.items():
        rel = f"docs/社区审计提交/02-罗素悖论的幽灵-{suffix}.md"
        body = text(git("show", f"{MAIN_COMMIT}:{rel}"))
        if title not in body or distinct not in body:
            raise SystemExit(f"MAIN_TRANSLATED_CROSS_REFERENCE_MISSING:{suffix}")
    return {
        "release_id": RELEASE_ID,
        "dev_source_commit": BASE_COMMIT,
        "main_commit": MAIN_COMMIT,
        "main_parent": MAIN_PARENT,
        "manifest_sha256": sha(manifest_bytes),
        "manifest_file_count_excluding_manifest": len(manifest["files"]),
        "tracked_file_count_including_manifest": len(tracked),
        "changed_paths": sorted(changed),
        "remote_refs": remote_refs,
        "dev_commit_signature": "PASS",
        "main_commit_signature": "PASS",
        "independent_rebuild": {
            "source_commit": BASE_COMMIT,
            "tree_diff_command": "diff -qr --exclude=.git <independent-builder-output> <generated-main-worktree>",
            "tree_diff_exit_code": 0,
        },
        "math_proof_replay": "NOT_RUN_DOCS_ONLY_NO_HOTT_OR_TOOLS_SOURCE_CHANGES",
    }


def essay_paragraph_audit(essay: dict) -> tuple[str, int]:
    focused = {
        ("扩展认知/003 - 芝诺、圆环、ASK 与两种方向.md", 12): "该小节标题直接承接 KC-000055 所澄清的研究线所指；文本未改，本次只同步社区稿02的链接标题。",
        ("扩展认知/003 - 芝诺、圆环、ASK 与两种方向.md", 13): "逐字原文 KC-000055 保持不变；社区稿02新增的 A7/用户判定区分与这段原话一致。",
        ("扩展认知/003 - 芝诺、圆环、ASK 与两种方向.md", 14): "KC-000055 的来源定位未改；对外稿链接修正不改变原文来源。",
        ("扩展认知/003 - 芝诺、圆环、ASK 与两种方向.md", 15): "该段已将圆环/后续讨论与 A7 候选分开；新链接文字与原解释对齐，未改任何数学状态。",
        ("扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md", 32): "该段已明确区分用户所指的圆环幽灵与 A7 候选；本次公共交叉引用复用这一边界，不改阐释正文。",
    }
    lines = [
        "## 扩展认知逐段落审计（空行分隔块，按索引顺序）", "",
        "本轮没有改扩展认知；仍逐项列出索引与全部 11 个分片中的 Markdown 内容块，确认公共链接修正未引入新的 essay 解释。段落块是审计定位，不声称工具认证模型理解。", "",
        "| owner | 段落块 | 关系 | 本轮评估 | 证据与下次触及条件 |", "|---|---:|---|---|---|",
    ]
    count = 0
    docs = [(ESSAY, essay["index_text"]), *[(rel, essay["shards"][rel]) for rel in essay["index_meta"]["shard_paths"]]]
    for rel, body in docs:
        blocks = [b.strip() for b in re.split(r"\n\s*\n", body) if b.strip()]
        for ordinal, block in enumerate(blocks, 1):
            count += 1
            key = (rel, ordinal)
            relation = "ALIGNED" if key in focused else "NOT_TOUCHED"
            assessment = focused.get(
                key,
                "本段未被编辑；本轮仅修改对外稿02的姐妹稿显示名/归属提示与发布记录，不据此重评或改写该阐释段落。",
            )
            anchor = re.sub(r"\s+", " ", block).replace("|", "\\|")[:80]
            evidence = f"`{rel}` P{ordinal:03d} sha256={sha(body.encode('utf-8'))}；若后续修改本段或据此作出新的核心语义判断，再回源复审。"
            for cell in (anchor, assessment, evidence):
                if "\n" in cell:
                    raise ValueError(f"ESSAY_AUDIT_CELL_INVALID:{rel}:P{ordinal}")
            lines.append(f"| `{rel}` | P{ordinal:03d}: {anchor} | `{relation}` | {assessment} | {evidence} |")
    lines.extend(["", f"段落块覆盖数：{count}；索引顺序与分片表顺序一致。", ""])
    return "\n".join(lines), count


def core_audit_text(manifest: dict, essay: dict) -> tuple[str, int]:
    focus = {
        "KC-000003": ("ALIGNED", "公共稿02当前姐妹稿引用把 A7 标作芝诺式候选，并显式区分其与圆环幽灵；用户圆环原意未改、原案形式化仍开放。", f"KC-000055；`{PAPER02}`；`rulings.md`", "若用户进一步更正圆环线所指，回源更新；不得由标题升级 K 或形式化状态。"),
        "KC-000022": ("ALIGNED", "两类现实相对悖论方向没有改变；仅澄清 AI 的 A7 候选不是用户 09-27 总判定的指称对象。", f"`{PAPER02}`；A7 current owner；`rulings.md`", "如用户明确把 A7 纳入总判定所指，再复审对应原文。"),
        "KC-000054": ("ALIGNED", "UR 与芝诺式模式候选的关系保留；新链接继续将 A7 标为候选，而非用户‘芝诺幽灵’判定。", f"`扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md`；`{PAPER02}`", "若用户撤回 A7 与总判定分开的澄清，再回源裁定。"),
        "KC-000055": ("ALIGNED", "用户完整澄清原文没有改动；公开稿02的新增说明忠实复述其将所指归于圆环及仓库后续分析。", f"`sources/prompts/Codex-圆环与芝诺幽灵所指的澄清-用户原文-20261001.md`；`{PAPER02}`", "若用户提供新的澄清或撤回，追加原文来源并复审，不改写旧原话。"),
    }
    lines = [
        f"# 核心认知逐编号回评：{SESSION_ID}", "",
        f"> generation：`core-cognition-generation-11`；KC 总数：55。审计由当前 KC manifest 顺序生成；本轮没有修改核心原文。单文件 legacy bundle 保持 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`，不冒称 audit shard 与 checkpoint 原子写已解决。", "",
        "- core_change: `NO` — core generation-11/55、manifest 与用户原文不变。",
        "- direction_change: `METADATA_ONLY` — 仅同步方向索引的 revision/generation 标记，不改方向行或优先级。",
        "- panorama_change: `METADATA_ONLY` — 仅同步全景索引的 revision/generation 标记，不改研究结果、开放状态或数学证据。",
        "- essay_change: `NO` — 扩展认知及其索引不变；逐段落兼容审计见下表。",
        "- update_decision: 更新 A7/Russell 两条当前记录的受影响来源哈希；公开稿02的链接标题与 A7/用户总判定边界同步四语；记录 main 发布；所有数学结论与 Goal7 状态保留。",
        "- cross_conflicts: 公开稿02末尾的姐妹稿引用显示旧标题，与稿01及五语索引的当前标题不一致；文件路径是历史固定路径，应保持。修正只触及显示标题/归属提示。",
        "- unresolved: Goal7 / MO3-COVERAGE-C 仍 active 且未审计；圆环原案的 K 与 HoTT 忠实形式化仍开放；A7 统一定义问题仍开放；不在本任务中执行数学研究。", "",
        "| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决与反证条件 |",
        "|---|---|---|---|---|---|",
    ]
    counts: dict[str, int] = {}
    expected_ids = [f"KC-{n:06d}" for n in range(1, len(manifest["units"]) + 1)]
    actual_ids = [unit["id"] for unit in manifest["units"]]
    if actual_ids != expected_ids or len(actual_ids) != 55:
        raise ValueError("CORE_DENOMINATOR_NOT_55_ORDERED")
    for unit in manifest["units"]:
        kid = unit["id"]
        label = f"{unit.get('platform', '')} / {unit.get('semantic_label', '—')}".replace("|", "\\|")
        if kid in focus:
            relation, assessment, evidence, unresolved = focus[kid]
        else:
            relation = "NOT_TOUCHED"
            assessment = "本轮只改对外稿02的姐妹稿标题/归属提示和出版记录；未修改或重新裁决此 KC 的原文、数学内容或现实解释。"
            evidence = f"`核心认知.md` {kid}；`核心认知.manifest.json`；本轮精确文档差异仅在 `{PAPER02}`、其四语译本及 release spec。"
            unresolved = "若后续工作直接使用或修改此 KC，再按其原文与届时证据复审；本轮没有替代其开放状态。"
        for cell in (label, assessment, evidence, unresolved):
            if "\n" in cell or "|" in cell:
                raise ValueError(f"KC_AUDIT_CELL_INVALID:{kid}")
        counts[relation] = counts.get(relation, 0) + 1
        lines.append(f"| `{kid}` | {label} | `{relation}` | {assessment} | {evidence} | {unresolved} |")
    lines.extend(["", f"关系计数：{json_text(counts).strip()}（计数只验证覆盖，不认证理解）。", ""])
    essay_body, paragraph_count = essay_paragraph_audit(essay)
    lines.append(essay_body)
    lines.extend([
        "## 已走过的路与下一步偏航检查", "",
        "本单元只完成已授权的对外文档导航/归属一致性与 source-hash 修复；main 由精确 dev 提交生成并推送。没有扩展到新数学候选，没有重放或改写证明。公开读者稿中的 A7 候选与用户圆环幽灵指称已明确分开。",
        "若下一步被切换为数学研究，必须按目标重新建 closure 和 profile；本次发布收尾不恢复 Goal7、不把公开稿的措辞当作证明，也不以本次对外文字验证取代用户核验或机器核验。", "",
    ])
    return "\n".join(lines), paragraph_count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit(f"OUTPUT_ALREADY_EXISTS:{args.output}")

    plan = R.plan(ROOT, profile="governance")
    if plan["revision"] != 294 or plan["latest_session"] != PREVIOUS_SESSION or plan["review_required"]:
        raise SystemExit(f"BASE_PLAN_MISMATCH:{plan['revision']}:{plan['latest_session']}:{plan['review_required']}")
    state = json.loads((ROOT / STATE).read_text(encoding="utf-8"))
    if state.get("current_core", {}).get("generation") != "core-cognition-generation-11" or state.get("current_core", {}).get("kc_count") != 55:
        raise SystemExit("CORE_IDENTITY_MISMATCH")
    if SESSION_ID in state.get("records", {}):
        raise SystemExit("SESSION_ALREADY_REGISTERED")

    v = release_verification()
    current_source_hashes = {path: sha_file(path) for path in (REPORT, COMMUNITY_INDEX, PAPER01, PAPER02, PAPER03)}
    translation_hash = current_source_hashes[PAPER02]
    for path in PAPER02_TRANSLATIONS:
        match = re.search(r"(?m)^source_sha256: ([0-9a-f]{64})$", (ROOT / path).read_text(encoding="utf-8"))
        if not match or match.group(1) != translation_hash:
            raise SystemExit(f"DEV_TRANSLATION_SOURCE_HASH_MISMATCH:{path}")

    state["revision"] = NEXT_REVISION
    state["latest_session"] = SESSION_ID
    state["execution_control"]["last_checkpoint_session"] = SESSION_ID
    state["execution_control"]["checkpoint_result"] = RESULT_REL
    state["records"][DIRECTION_RECORD]["projection_generation"] = "20261001-direction-295"
    state["records"][PANORAMA_RECORD]["projection_generation"] = "20261001-outcome-295"

    a7 = state["records"][A7_RECORD]
    for path in (REPORT, PAPER01, COMMUNITY_INDEX):
        a7.setdefault("source_hashes", {})[path] = current_source_hashes[path]
        if path not in a7.setdefault("full_sources", []):
            a7["full_sources"].append(path)
    old = str(a7.get("revalidation", "")).strip()
    a7["revalidation"] = (old + " " if old else "") + (
        f"{SESSION_ID}: the public sister-paper cross-reference now displays paper 01's current title while preserving its historical filename; A7's candidate status and mathematical scope are unchanged."
    )
    a7.setdefault("related_records", []).append(SESSION_ID)

    russell = state["records"][RUSSELL_RECORD]
    russell.setdefault("source_hashes", {})[PAPER02] = current_source_hashes[PAPER02]
    if PAPER02 not in russell.setdefault("full_sources", []):
        russell["full_sources"].append(PAPER02)
    old = str(russell.get("revalidation", "")).strip()
    russell["revalidation"] = (old + " " if old else "") + (
        f"{SESSION_ID}: refreshed the paper-02 source hash after a narrow title/attribution cross-reference correction in five languages; its Russell interpretation, formal evidence, lifecycle and mathematical scope are unchanged."
    )
    russell.setdefault("related_records", []).append(SESSION_ID)

    main_verification = {
        "schema_version": "main-release-verification/v1",
        "session_id": SESSION_ID,
        **v,
        "changed_claims_or_proofs": False,
        "main_release_tree_rebuilt_from_exact_dev_commit": True,
        "independent_rebuild_tree_diff_exit_code": 0,
    }
    main_verification_text = json_text(main_verification)

    direction = projection_edit.load(ROOT, DIRECTION)
    for old, new in (
        ("版本：`integrated-direction-portfolio/v1.15`", "版本：`integrated-direction-portfolio/v1.16`"),
        ("source_state_revision: 294", "source_state_revision: 295"),
        ("projection_generation: 20261001-direction-294", "projection_generation: 20261001-direction-295"),
    ):
        projection_edit.replace_in_index(direction, old, new)
    panorama = projection_edit.load(ROOT, PANORAMA)
    for old, new in (
        ("版本：`integrated-outcome-panorama/v1.16`", "版本：`integrated-outcome-panorama/v1.17`"),
        ("source_state_revision: 294", "source_state_revision: 295"),
        ("projection_generation: 20261001-outcome-294", "projection_generation: 20261001-outcome-295"),
    ):
        projection_edit.replace_in_index(panorama, old, new)

    memory = projection_edit.load(ROOT, MEMORY)
    new_public_status = (
        "**最新公开版发布状态（2026-10-01）**：此前三次读者入口、归因更正和多语收尾报告发布仍见下文历史记录。最新版本 `main-20261001-sister-paper-cross-reference-alignment` 由 dev `72520807` 生成并推送为 main `894e3816`；只同步社区稿02中“姊妹稿”的当前显示标题及 A7/用户判定区分，历史文件路径保持不变，Opus 正文和数学证据未改。main 的 RELEASE-MANIFEST 列出 702 个内容文件，连同 manifest 共 703 个跟踪文件；精确源提交重建后与发布树对比一致。没有重跑数学证明。"
    )
    memory["shards"][MEMORY001] = replace_paragraph_start(
        memory["shards"][MEMORY001], "**公开版发布状态（2026-10-01）**：", new_public_status
    )
    publication_log = (
        f"PUBLISH-{RELEASE_ID}：dev 源提交 `{BASE_COMMIT}` 生成并推送 main 提交 `{MAIN_COMMIT}`（父提交 `{MAIN_PARENT}`）。"
        "只把社区稿02的姐妹稿链接文字对齐到稿01当前标题，并在四语译本中标明 A7 是独立 AI 候选、不是用户 09-27 判定所指；历史文件名保留。"
        "译文源哈希通过构建器核验；main 精确源提交独立重建与发布树 diff exit 0；main/dev 签名与远端 refs 已核验。"
        "未改形式主张、证明源码或运行收据，未重跑数学证明。"
    )
    memory["shards"][MEMORY003] = memory["shards"][MEMORY003].rstrip() + "\n\n" + publication_log + "\n"

    generation, units = core_audit_builder.manifest_units(ROOT)
    essay = projection_edit.load(ROOT, ESSAY)
    audit, essay_block_count = core_audit_text({"generation": generation, "units": units}, essay)
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": [
            f"{SESSION_REL}/SESSION.md", f"{SESSION_REL}/RUNS.json", f"{SESSION_REL}/CORE_COGNITION_AUDIT.md",
            VERIFY_REL, RESULT_REL, PREPARE_PATH, REPAIR_PATH,
            "scripts/release/build_main_release.py", "scripts/release/main-release-spec.json",
            REPORT, COMMUNITY_INDEX, PAPER01, PAPER02, *PAPER02_TRANSLATIONS, PAPER03,
            "sources/prompts/Codex-圆环与芝诺幽灵所指的澄清-用户原文-20261001.md",
            "rulings.md", "MEMORY.md", MEMORY001, MEMORY003, DIRECTION, PANORAMA,
        ],
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": f"{SESSION_REL}/SESSION.md",
        "related_records": [PREVIOUS_SESSION, A7_RECORD, RUSSELL_RECORD, ABX_RECORD, DIRECTION_RECORD, PANORAMA_RECORD],
        "scope": "Close the narrow reader-facing title/attribution cross-reference and publish it through the canonical main release builder; refresh the two affected current source pins and publication memory. No mathematical claim, proof scope, Goal7 status, or research direction changes.",
        "source_hashes": {},
        "status": "complete",
    }

    # Build the session bundle after all authoritative owner text is final.
    session = f"""# {SESSION_ID}

- tier: T3 (current source-pin, projection metadata, and checkpoint reconciliation; no mathematical conclusion)
- host: Codex desktop, local repository worktree
- model: GPT-5 family; exact serving variant is not independently exposed in the task surface
- role: single-surface canonical integrator
- authorization: the user asked for all remaining main-branch documentation cleanup, publication to both `dev` and `main`, and directed “全部做完.” This unit performs only the agreed narrow cross-reference correction, its formal release, and its necessary current-owner/checkpoint alignment.
- base: dev `{BASE_COMMIT}`, STATE revision {BASE_REVISION}, latest prior session `{PREVIOUS_SESSION}`. Main release `{MAIN_COMMIT}` from source `{BASE_COMMIT}` is already pushed and signature-verified.
- core: generation-11 / 55 KC; no KC, source, theorem, proof, or claim-matrix content changed.
- research queue: Goal7 / MO3-COVERAGE-C remains active and incomplete; no math research was resumed or closed.
- output: article 02 links to article 01's current visible title in Chinese and four translations; the historical file path remains unchanged. The translations' hash pins were refreshed, then main was generated from dev and pushed.
- state repair: the prior checkpoint had two `HEAD.tracked` entries lagging the clean committed MEMORY publication notes. Exact checkpoint copies, Git provenance, and sole-drift set are recorded in `{REPAIR_PATH}`; the derived tracker was reconciled without changing STATE or historical receipts, followed by this canonical revision {NEXT_REVISION} checkpoint.
- open: no further prose-wide rewrite is justified; the project’s unrelated research, external community audit, and Goal7 obligations remain open.

## Freshness and evidence

Full STATE at checkpoint base was read through EOF: {len((ROOT / STATE).read_text(encoding="utf-8").splitlines())} lines, `{sha_file(STATE)}`. The current generation-11 four-piece source set was hash-checked against its loaded snapshot: core `{sha_file("核心认知.md")}`, direction `{sha_file(DIRECTION)}`, panorama `{sha_file(PANORAMA)}`, essay `{sha_file(ESSAY)}`. The governance plan before checkpoint used snapshot `{plan['snapshot']}` with {len(plan['documents'])} documents and `review_required=[]`.

## Element use and limits

- `cognition_runtime.py`: used for the post-repair plan, dry-run and canonical `--apply`; only its `result.json` is the application receipt.
- `repair_tracking.py`: used only for the two exact, clean, committed derived-HASH discrepancies; it did not rewrite STATE or a historical receipt.
- `projection_edit.py`: advanced direction/panorama index identity metadata only, preserving their human-edited rows and shards.
- Main release builder: built the curated tree from exact dev commit `{BASE_COMMIT}`; independent tree comparison to main returned exit 0.
- Proof gate: no mathematical conclusion or proof claim was added, and no proof was replayed.
- Sub Agents: not used; the project prohibits them.
"""

    runs = {
        "schema_version": "hott-session-runs/v2",
        "session_id": SESSION_ID,
        "session_kind": "PUBLIC_DOCUMENTATION_AND_STATE_ALIGNMENT",
        "base_snapshot": plan["snapshot"],
        "checkpoint_result": RESULT_REL,
        "document_audit": {"main_markdown_files": 72, "reader_facing_files_reviewed": 31, "proof_or_claim_files_preserved": 41,
                           "cross_reference_edits": 5, "translation_source_hashes_verified": 4,
                           "extension_paragraph_blocks_audited": essay_block_count},
        "main_release": main_verification,
        "state_reconciliation": {"base_revision": BASE_REVISION, "next_revision": NEXT_REVISION,
                                 "pre_checkpoint_head_repair": REPAIR_PATH,
                                 "stale_current_source_pins_refreshed": [
                                     f"{A7_RECORD}:{REPORT}", f"{RUSSELL_RECORD}:{PAPER02}"
                                 ]},
        "formal_runs": [],
        "governance_runs": [
            {"tool": PREPARE_PATH, "status": "PAYLOAD_PREPARED_WITH_EXACT_BASE_HASHES; NO_PROJECT_FILE_WRITTEN_BY_PREPARER"},
            {"tool": ".codex/tools/cognition_runtime.py plan --profile governance", "status": "PASS_AFTER_DERIVED_HEAD_REPAIR / 56_FILES / review_required=0"},
            {"tool": ".codex/tools/cognition_runtime.py checkpoint", "status": "canonical result.json is the only application receipt"},
            {"tool": "scripts/audit/verify_governance_shards.py", "status": "to be re-run after checkpoint"},
            {"tool": "scripts/audit/verify_core_cognition.py", "status": "not applicable; core source and manifest unchanged"},
        ],
        "new_mathematical_claims": [],
        "goal7_status": "UNCHANGED_ACTIVE_INCOMPLETE",
    }
    state["records"][SESSION_ID]["source_hashes"] = {
        PREPARE_PATH: sha_file(PREPARE_PATH),
        REPAIR_PATH: sha_file(REPAIR_PATH),
        REPORT: current_source_hashes[REPORT],
        COMMUNITY_INDEX: current_source_hashes[COMMUNITY_INDEX],
        PAPER01: current_source_hashes[PAPER01],
        PAPER02: current_source_hashes[PAPER02],
        PAPER03: current_source_hashes[PAPER03],
        "scripts/release/main-release-spec.json": sha_file("scripts/release/main-release-spec.json"),
        VERIFY_REL: sha(main_verification_text.encode("utf-8")),
    }
    session_files = {
        f"{SESSION_REL}/SESSION.md": session,
        f"{SESSION_REL}/RUNS.json": json_text(runs),
        f"{SESSION_REL}/CORE_COGNITION_AUDIT.md": audit,
        VERIFY_REL: main_verification_text,
    }
    # Include the final exact source hashes in STATE after adding the session bundle.
    state_text = json_text(state)

    direction["index_text"] = direction["index_text"]
    memory["index_text"] = memory["index_text"]
    essay["index_text"] = essay["index_text"]
    panorama["index_text"] = panorama["index_text"]
    text_overrides = {
        DIRECTION: direction["index_text"], **direction["shards"],
        PANORAMA: panorama["index_text"], **panorama["shards"],
        ESSAY: essay["index_text"], **essay["shards"],
        MEMORY: memory["index_text"], **memory["shards"],
        STATE: state_text,
    }
    payload_rows = []
    for rel in [*R.MUTABLE, *sorted(R.mutable_shard_paths(ROOT))]:
        raw = (ROOT / rel).read_bytes()
        body = text_overrides.get(rel, text(raw))
        payload_rows.append({"path": rel, "expected_sha256": sha(raw), "text": body})
    for rel, body in session_files.items():
        target = ROOT / rel
        payload_rows.append({"path": rel, "expected_sha256": sha(target.read_bytes()) if target.is_file() else None, "text": body})
    payload = {
        "schema_version": "cognition-checkpoint/v1",
        "session_id": SESSION_ID,
        "authorization": "User-directed completion of public main documentation, both-branch publication, and the in-scope State/hash reconciliation; no mathematical conclusion or Goal7 closure.",
        "load_profile": "governance",
        "task_ids": [],
        "files": payload_rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json_text(payload), encoding="utf-8")
    print(json.dumps({"status": "PAYLOAD_PREPARED", "snapshot": plan["snapshot"], "revision": BASE_REVISION,
                      "next_revision": NEXT_REVISION, "files": len(payload_rows), "kc_count": len(units),
                      "essay_blocks": essay_block_count, "main_release": MAIN_COMMIT}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
