#!/usr/bin/env python3
"""Prepare the CG-010 checkpoint for the main release of 2026-10-15 (revision 314 -> 315).

Scope (research sponsor, 2026-10-15): "把方案全部做完，然后你自己进行审查，然后全部推送到github上……然后更新原repo的main
分支，然后push到远程。"  dev was fast-forwarded to 29741a5b and main 615b7c4f was generated from it by
scripts/release/build_main_release.py and pushed; the remote tree was read back and equals the build.  After the push the
release was rebuilt independently from 29741a5b (identical to `git archive 615b7c4f`) and every run of the published main
was replayed with the published tools/replay.py.

This payload records that release in STATE through the runtime's canonical path, the way S-GOV-20261001-MAIN-DOCS-ALIGNMENT
did: a session record with the release verification and the full replay report, and fresh source pins (with a revalidation
note) for the two live records whose pinned documents this unit changed (community paper 03 version 2; the phase-close
report's pointer to the README's renumbered section).  Historical session records keep the hashes of their time.  Nothing
else changes; the core stays at generation 15.  Following the root CLAUDE.md (section 1, item 3), no further ritual.

The script only builds the payload; it writes nothing into the repository.  Apply it with
.codex/tools/cognition_runtime.py checkpoint --snapshot <printed snapshot> --payload <output> --apply
Modelled on scripts/audit/prepare_claude_cg010_core_generation_15_checkpoint.py.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import importlib.util
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RUNTIME_PATH = ROOT / ".codex/tools/cognition_runtime.py"
SPEC = importlib.util.spec_from_file_location("runtime_claude_release", RUNTIME_PATH)
assert SPEC and SPEC.loader
R = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(R)

SESSION_ID = "S-GOV-20261015-CLAUDE-CG010-MAIN-RELEASE"
PREV_SESSION = "S-GOV-20261015-CLAUDE-CG010-CORE-GENERATION-15"
PREV_REVISION = 314
NEW_REVISION = PREV_REVISION + 1
RESULT_REL = f".codex/cognition/checkpoints/{SESSION_ID}/result.json"
SESSION_REL = f".codex/research/hott/sessions/{SESSION_ID}"
PREPARE_SELF = "scripts/audit/prepare_claude_cg010_main_release_checkpoint.py"

DEV_BEFORE = "cc7eea2b"
DEV_COMMIT = "29741a5bc14404d875b39fb16d3a2fcb7d798085"
MAIN_COMMIT = "615b7c4f39501a33051610844cc472c958daf94b"
MAIN_PARENT = "f31277019c21eb497dc9923fbdf420c4920571ac"
MAIN_TREE = "fd611eb81c66cbfe3f213513755ca12f19bff9d8"
MANIFEST_SHA = "39a5ceff578388f15651a327733401f250b60d2fea76e1e053d24ae6a8fecbe5"
RELEASE_ID = "main-20261015-zfc1-convergence"
PAPER03 = "docs/社区审计提交/03-HoTT的芝诺.md"
REPORT = "docs/HoTT悖论查找阶段收尾报告-20260930.md"
SELF_REVIEW = ".claude/goals/CG-010-remaining-formalization-alignment/H5-发布自审-20261015.md"
LINE_BY_LINE = "docs/ZFC-1的问题-原话逐句对照与机器证明-20261015.md"
RELEASE_FILES = ["scripts/release/main-release-spec.json", "scripts/release/build_main_release.py", "scripts/release/replay.py",
                 "scripts/release/main-README.md", SELF_REVIEW, LINE_BY_LINE, PAPER03, REPORT]
REVALIDATE = {
    "A-RUSSELL-EXISTENCE-QUESTIONING-001": (PAPER03,
        "S-GOV-20261015-CLAUDE-CG010-MAIN-RELEASE: community paper 03 is at version 2 — per the research sponsor's ruling D4 of "
        "2026-10-15, its 'which premise' paragraph names one defendant, the ready-made collection (the sponsor's A on the ZFC side), "
        "with univalence a cause, and cites the consolidating theorem C-430; the formal evidence, lifecycle and scope of this record "
        "are unchanged."),
    "A-A7-INFINITE-COHERENCE-001": (REPORT,
        "S-GOV-20261015-CLAUDE-CG010-MAIN-RELEASE: the phase-close report's pointer to the main README now names section 10 "
        "(the README gained a section 6 on ZFC-1); A7's candidate status, machine evidence and open uniform-definition question "
        "are unchanged."),
}
AUTHORIZATION = (
    "Research sponsor, 2026-10-15, goal set in this session (91beaf35): \"把方案全部做完，然后你自己进行审查，然后全部推送到github上。"
    "本地的所有和当前repo这个HoTT命名的有关的git worktree，全部推送到远程GitHub上……所有的branch，全部推送到远程。然后更新原repo的main分支，"
    "然后push到远程。\" The self-review the sponsor asked for is the file named in SESSION.md; dev and main were pushed without force."
)

# KC quotations in the main README (checked against 核心认知.md; self-review section 1)
NEW_QUOTED = {"KC-000064", *(f"KC-{n:06d}" for n in range(76, 84))}
HEADER_KCS = {"KC-000068", "KC-000069"}
CARRIED_KCS = {"KC-000047", "KC-000050", "KC-000051", "KC-000054", "KC-000055"}
ROWS = {
    "new": ("ALIGNED", "本轮在 main README 新写的段落里逐字引用（中文版；四种译本保留中文原文并附译文）；逐字核对见自审第 1 节",
            "若引文与本条原文不逐字一致，以本条为准改 README"),
    "header": ("ALIGNED", "研究发起人 10-04 亲手放在 main 文首的“ZFC Failure”取自本条；本轮原样补进 dev 的模板，重新生成后仍在页首，20 行逐行在本条中（自审第 1 节）",
               "若页首与研究发起人的原文不一致，以原文为准"),
    "carried": ("NOT_TOUCHED", "10-01 版 README 已逐字引用本条，本轮原样带上，没有改动，也没有重新判断该条所指的内容",
                "若引文与本条原文不逐字一致，以本条为准改 README"),
    "default": ("NOT_TOUCHED", "本单元是 main 发布与发布自审，没有重新判断该条所指的内容；原文身份保留。",
                "若 README 对本条的转述与原文不符，以原文为准改 README"),
}


def sha_file(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def labels() -> dict[str, str]:
    text = (ROOT / "核心认知.md").read_text(encoding="utf-8")
    return {m.group(1): m.group(2).strip()
            for m in re.finditer(r"^### (KC-\d{6}) · [^·]+? · [^·]+? · (.+)$", text, re.M)}


def audit_text() -> str:
    lab = labels()
    if len(lab) != 83:
        raise SystemExit("CORE_NOT_83")
    rows, counts = [], {}
    for kc, label in lab.items():
        key = "new" if kc in NEW_QUOTED else "header" if kc in HEADER_KCS else "carried" if kc in CARRIED_KCS else "default"
        rel, ass, nxt = ROWS[key]
        counts[rel] = counts.get(rel, 0) + 1
        cell = lambda s: s.replace("|", "／")
        rows.append(f"| `{kc}` | {cell(label)} | {rel} | {cell(ass)} | {cell(nxt)} |")
    tally = "、".join(f"{k} {v}" for k, v in sorted(counts.items()))
    return "\n".join([
        f"# {SESSION_ID} 完整兼容审计", "",
        "core-cognition-generation-15；83 KC。canonical writer 只授权新 session 目录第一层文件，所以本审计是单文件兼容 bundle。逐条立场由本会话写成（Claude Code 会话 91beaf35，012-Opus），计数不认证理解。", "",
        "- core_change: NO — 核心认知保持第 15 代；本单元只发布与登记。",
        "- direction_change: NO — 研究方向不变（找到 ZFC-1=ZFC+A 的问题并机器证明，根 `CLAUDE.md` 第四节）。",
        f"- panorama_change: NO — 新证明此前已登记；本单元把 20 个包、57 个运行放上 `main`（`{RELEASE_ID}`）。",
        "- essay_change: NO — 不加扩展认知分片。",
        f"- update_decision: 研究发起人 2026-10-15 设定的目标要求做完、自审、推送；自审见 `{SELF_REVIEW}`；`dev` 快进到 `{DEV_COMMIT[:8]}`，`main` 生成为 `{MAIN_COMMIT[:8]}` 并推送，远程回读一致，独立重建一致，全量重放见 `FULL-REPLAY.json`。",
        "- cross_conflicts: CLAIMS 第 1 节的来源在 10-03 被另一会话加了 C-357、C-358 两行，本单元把两个包与被引用的四个运行一并发布；10-01 版 README 另有 6 处引文不在核心认知里（自审第 1 节），本轮没有改它们，也没有重新对照转录。",
        "- unresolved: 10-15 收敛原话入不入核（研究发起人一句话）；译本未经母语读者校对；`--foundation-root` 未在全新 lake 构建上实测；外部复核与文献查重未做。",
        "", f"关系计数：{tally}。", "",
        "|KC ID|姿态|relation|assessment and evidence|next and falsifier|", "|---|---|---|---|---|", *rows, "",
    ])


def replay_summary(report: dict) -> dict:
    runs = report["runs"]
    by = collections.Counter((r["kind"], r["expected"], r["result"]) for r in runs)
    return {
        "tool": "tools/replay.py of the published main (scripts/release/replay.py on dev at the source commit)",
        "checkout": f"independent rebuild of main from {DEV_COMMIT[:8]} (identical to git archive {MAIN_COMMIT[:8]})",
        "jobs": 4,
        "toolchain": {
            "agda": "Agda 2.8.0 (/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64), cubical v0.9 (/Volumes/D/HoTT-toolchain-cache/cubical-v0.9)",
            "lean": "Lean 4.34.0 (pinned toolchain prefix, called directly, not through elan)",
            "lean_libraries": "Foundation 1fb01b72 built for Lean 4.34.0 (/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0) and Mathlib 5ed29652 with its packages, given with --lean-lib",
        },
        "counts": dict(collections.Counter(r["result"] for r in runs)),
        "by_kind_expected_result": {f"{k}/{e}/{res}": n for (k, e, res), n in sorted(by.items())},
        "total": len(runs),
        "report_file": "FULL-REPLAY.json",
    }


def verification_obj(report: dict) -> dict:
    return {
        "schema_version": "main-release-verification/v1",
        "session_id": SESSION_ID,
        "release_id": RELEASE_ID,
        "dev_source_commit": DEV_COMMIT,
        "dev_commit_signature": "PASS",
        "main_commit": MAIN_COMMIT,
        "main_commit_signature": "PASS",
        "main_parent": MAIN_PARENT,
        "main_parent_note": "f3127701 is the research sponsor's own commit 'ZFC Failure 研究收敛' (2026-10-04); its README header is carried verbatim by the template on dev and stays at the top",
        "main_tree": MAIN_TREE,
        "main_release_tree_rebuilt_from_exact_dev_commit": True,
        "independent_rebuild": {"source_commit": DEV_COMMIT,
                                "tree_diff_command": f"diff -qr <independent-builder-output> <git archive {MAIN_COMMIT[:8]}>",
                                "tree_diff_exit_code": 0},
        "manifest_sha256": MANIFEST_SHA,
        "tracked_file_count_including_manifest": 1334,
        "manifest_file_count_excluding_manifest": 1333,
        "build": {"status": "BUILT", "runs": 164, "accepted": 69, "rejected_as_expected": 95,
                  "units": {"UR": 84, "A7": 45, "ZFC1": 53}, "runs_without_unit": [], "paths_on_dev": 34,
                  "translation_checks": "all document and CLAIMS translation hashes current; no check relaxed"},
        "changes_against_parent": {"added": 631, "modified": 26, "deleted": 0,
                                   "claims": "CLAIMS gains section 1 rows for C-357/C-358 and section 4 (ZFC side); the run list becomes section 5; no existing claim row removed or changed"},
        "remote_refs": {"refs/heads/dev": DEV_COMMIT, "refs/heads/main": MAIN_COMMIT},
        "push": {"dev": f"{DEV_BEFORE}..{DEV_COMMIT[:8]} fast-forward", "main": f"{MAIN_PARENT[:8]}..{MAIN_COMMIT[:8]} fast-forward", "force": False},
        "math_proof_replay": replay_summary(report),
        "replay_before_push": "the 57 runs new to main: PASS 57 (41 Mathlib/Foundation, 16 Agda), same outcome class and same normalized stdout",
        "self_review": SELF_REVIEW,
    }


def session_text(rs: dict) -> str:
    counts = "、".join(f"{k} {v}" for k, v in sorted(rs["counts"].items()))
    return "\n".join([
        f"# {SESSION_ID}", "",
        f"`main` 发布 `{RELEASE_ID}`：研究发起人的 ZFC-1 收敛，五种语言的 README 第 6 节、CLAIMS 第 4 节、20 个包与 57 个运行。", "",
        "- host: Claude Code（桌面应用 Code 标签页，本机 macOS），会话 91beaf35-237d-4c5d-887c-cb72c58ccca2，独立 worktree `/Volumes/D/HoTT-worktrees/012-opus-w8`，分支 `claude/012-opus-w8`",
        "- model: Claude Opus 5.5（claude-opus-5-5）",
        "- role: 执行者（CG-010 移交清单 H5）；本 checkpoint 不交付新数学主张",
        f"- authorization: {AUTHORIZATION}", "",
        "## 做了什么", "",
        f"- `dev`：`{DEV_BEFORE}` → `{DEV_COMMIT[:8]}`，快进推送，不强推。",
        f"- `main`：由 `{DEV_COMMIT[:8]}` 经 `scripts/release/build_main_release.py` 生成，父提交 `{MAIN_PARENT[:8]}`（研究发起人 10-04 亲手加“ZFC Failure”的那次提交），新提交 `{MAIN_COMMIT[:8]}`（SSH 签名，签名核对通过），推送后回读：远程树 `{MAIN_TREE[:8]}` 与构建输出相同。",
        f"- 独立重建：从 `{DEV_COMMIT[:8]}` 重新构建，与 `git archive {MAIN_COMMIT[:8]}` 逐文件比对，`diff -qr` 退出码 0（1334 个文件）。",
        f"- 推送前，新收的 57 个运行在本机重放全部通过。推送后，用发布出去的 `tools/replay.py` 对重建的 `main` 全量重放 {rs['total']} 个运行：{counts}（报告 `FULL-REPLAY.json`）。",
        f"- 发布前的自审：`{SELF_REVIEW}`（机械核对、D01–D24 结论表、九处修正、未覆盖的部分）。",
        "- 重钉：`A-RUSSELL-EXISTENCE-QUESTIONING-001`（社区稿 03 第 2 版）、`A-A7-INFINITE-COHERENCE-001`（收尾报告的 README 节号），各写了 revalidation。", "",
        "## 照实说", "",
        "- 核心认知、方向追踪、全景视野、扩展认知、MEMORY 原样带上。",
        "- STATE.json 没有整体读入模型上下文；本事务只经脚本改 `revision`、`latest_session`、`execution_control` 的两个字段、两条记录的钉住哈希与 revalidation，并加本 session 记录。",
        "- `FULL-REPLAY.json` 是重放工具的原始报告，只把 `root` 一项（本机临时目录）换成说明文字。", "",
    ])


def runs_obj(snapshot: str, rs: dict) -> dict:
    counts = ", ".join(f"{k} {v}" for k, v in sorted(rs["counts"].items()))
    return {
        "schema_version": "hott-session-runs/v2", "session_id": SESSION_ID, "session_kind": "GOVERNANCE_MAIN_RELEASE",
        "checkpoint_result": RESULT_REL, "base_snapshot": snapshot, "formal_runs": [],
        "governance_runs": [
            {"tool": "scripts/release/build_main_release.py", "command": f"--source {DEV_COMMIT[:8]} --out <empty directory>",
             "status": "BUILT / 1334 files / 164 runs / 69 accepted"},
            {"tool": "scripts/release/replay.py", "command": "--lean-sysroot <Lean 4.34.0> --lean-lib <Foundation+Mathlib libraries> --only <41 runs>",
             "status": "PASS 41 (before push)"},
            {"tool": "scripts/release/replay.py", "command": "--agda <Agda 2.8.0> --cubical-lib <cubical v0.9> --only <16 runs>", "status": "PASS 16 (before push)"},
            {"tool": "git", "command": f"push origin {DEV_COMMIT[:8]}:dev; commit-tree -S <build tree> -p {MAIN_PARENT[:8]}; push origin main",
             "status": f"dev {DEV_BEFORE}..{DEV_COMMIT[:8]}; main {MAIN_PARENT[:8]}..{MAIN_COMMIT[:8]}; remote tree equals build"},
            {"tool": "scripts/release/build_main_release.py + diff", "command": f"--source {DEV_COMMIT[:8]} --out <fresh directory>; diff -qr <it> <git archive {MAIN_COMMIT[:8]}>",
             "status": "BUILT; diff exit 0"},
            {"tool": "tools/replay.py (published main)", "command": "--jobs 4 --lean-lib <Foundation+Mathlib libraries> --json FULL-REPLAY.json (AGDA, CUBICAL_LIB, LEAN_SYSROOT set)",
             "status": f"{rs['total']} runs: {counts}"},
            {"tool": PREPARE_SELF, "command": "--replay-report <FULL-REPLAY source> --output <payload>", "status": "PREPARED"},
            {"tool": ".codex/tools/cognition_runtime.py", "command": "checkpoint --snapshot <base_snapshot> --payload <payload> --apply",
             "status": "CHECKPOINT_COMMITTED expected; only the canonical result.json proves it"},
        ],
        "new_math_claims": [], "math_status_change": "NONE",
        "push_policy": "dev and main pushed on the research sponsor's goal of 2026-10-15; no force",
    }


def state_edits(state: dict) -> None:
    session_path = f"{SESSION_REL}/SESSION.md"
    state["revision"] = NEW_REVISION
    state["latest_session"] = SESSION_ID
    ec = state["execution_control"]
    ec["last_checkpoint_session"] = SESSION_ID
    ec["checkpoint_result"] = RESULT_REL
    for rec_id, (path, note) in REVALIDATE.items():
        rec = state["records"][rec_id]
        assert path in rec["source_hashes"], (rec_id, path)
        rec["source_hashes"][path] = sha_file(path)
        old = str(rec.get("revalidation") or "").strip()
        rec["revalidation"] = (old + " " + note).strip() if old else note
    sources = [session_path, f"{SESSION_REL}/RUNS.json", f"{SESSION_REL}/CORE_COGNITION_AUDIT.md",
               f"{SESSION_REL}/MAIN-RELEASE-VERIFICATION.json", f"{SESSION_REL}/FULL-REPLAY.json", RESULT_REL] + RELEASE_FILES
    state["records"][SESSION_ID] = {
        "depends_on": [],
        "evidence_status": "GOVERNANCE_CHECKPOINT_COMMITTED / VERIFIED_WITH_SCOPE / NO_NEW_MATH_CLAIM",
        "full_sources": sources,
        "kind": "session",
        "lifecycle_status": "HISTORICAL",
        "path": session_path,
        "related_records": [PREV_SESSION, *REVALIDATE.keys()],
        "scope": (f"Main release {RELEASE_ID}: dev fast-forwarded to {DEV_COMMIT[:8]}, main {MAIN_COMMIT[:8]} generated from it and pushed, "
                  "remote tree read back equal to the build and an independent rebuild identical to it; the ZFC side (README section 6 in "
                  "five languages, CLAIMS section 4, 20 packages, 57 runs) published after the self-review the research sponsor asked for; "
                  "every run of the published main replayed with the published tool; two live records re-pinned with revalidation. "
                  "No new mathematics delivered through this checkpoint."),
        "source_hashes": {p: sha_file(p) for p in RELEASE_FILES},
        "status": "complete",
    }


RESUME_ADD = (
    "### CG-010：`main` 发布 ZFC-1 收敛（2026-10-15）\n\n"
    f"`main` `{MAIN_COMMIT[:8]}`（由 `dev` `{DEV_COMMIT[:8]}` 生成，`{RELEASE_ID}`）：README 五种语言加第 6 节“回到页首：ZFC-1 的问题”，"
    "CLAIMS 加第 4 节（ZFC 一侧），20 个包、57 个运行，重放工具可重放 Mathlib／Foundation 运行。"
    f"发布前自审见 `{SELF_REVIEW}`。仍等研究发起人一句话：10-15 收敛那段入不入核。\n\n"
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--replay-report", type=Path, required=True, help="JSON report of the full replay of the published main")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    missing = [p for p in RELEASE_FILES if not (ROOT / p).is_file()]
    if missing:
        raise SystemExit(f"EVIDENCE_MISSING:{missing}")
    report = json.loads(args.replay_report.read_text(encoding="utf-8"))
    if len(report.get("runs", [])) != 164:
        raise SystemExit(f"REPLAY_REPORT_INCOMPLETE:{len(report.get('runs', []))}")
    report["root"] = f"<independent rebuild of main {MAIN_COMMIT[:8]} from dev {DEV_COMMIT[:8]}; temporary directory of the replaying machine>"
    state = json.loads((ROOT / R.STATE).read_text(encoding="utf-8"))
    if state.get("revision") != PREV_REVISION or state.get("latest_session") != PREV_SESSION:
        raise SystemExit(f"EXPECTED_REVISION_{PREV_REVISION}:{state.get('revision')}:{state.get('latest_session')}")
    if SESSION_ID in state["records"]:
        raise SystemExit(f"RECORD_ALREADY_EXISTS:{SESSION_ID}")
    rs = replay_summary(report)
    plan = R.plan(ROOT, profile="governance")
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
    texts[f"{SESSION_REL}/SESSION.md"] = session_text(rs)
    texts[f"{SESSION_REL}/CORE_COGNITION_AUDIT.md"] = audit_text()
    texts[f"{SESSION_REL}/RUNS.json"] = json.dumps(runs_obj(plan["snapshot"], rs), ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[f"{SESSION_REL}/MAIN-RELEASE-VERIFICATION.json"] = json.dumps(verification_obj(report), ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    texts[f"{SESSION_REL}/FULL-REPLAY.json"] = json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    payload = {
        "schema_version": "cognition-checkpoint/v1", "session_id": SESSION_ID, "authorization": AUTHORIZATION,
        "load_profile": "governance", "task_ids": [],
        "files": [{"path": path, "expected_sha256": R.sha((ROOT / path).read_bytes()) if (ROOT / path).exists() else None, "text": value}
                  for path, value in texts.items()],
    }
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "PREPARED", "snapshot": plan["snapshot"], "revision": NEW_REVISION, "session_id": SESSION_ID,
                      "files": len(texts), "replay": rs["counts"]}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
