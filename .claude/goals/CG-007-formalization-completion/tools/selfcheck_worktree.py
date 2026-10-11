#!/usr/bin/env python3
"""CG-007 worktree 自检：一条命令确认本工作树能否独立开工。

用法（在本 worktree 根目录）：
    python3 -B .claude/goals/CG-007-formalization-completion/tools/selfcheck_worktree.py

它只读不写，逐项检查：
  1. 工作根与分支（必须落在专用 worktree，不是 dev 主检出）；
  2. 开工闭包文件是否都在（goal-x closure + CLAUDE.md 第〇节点名的路径）；
  3. 唯一缺口的源码与已知状态；
  4. Lean 工具链与 Foundation 源码/构建树是否可达；
  5. 开发编译回路（devbuild_ns.py）与正式收据回路（capture_run.py）是否就位。

退出码 0 = 全部就绪；1 = 有硬缺口（会列出是哪一项）。
"""
import json
import subprocess
import sys
from pathlib import Path

EXPECT_TOPLEVEL = "/Volumes/D/HoTT-worktrees/cg007-w8-d3"
EXPECT_BRANCH = "codex/cg007-w8-d3"
DEV_CHECKOUT = "/Volumes/D/HoTT_AI_HANDOFF_20260911"
PACKAGE = "HoTT/formal/claude-cg001/godel-q-zfc-z0-full"

# 开工闭包：goal-x 注入的清单 + CLAUDE.md 第〇节点名的路径
CLOSURE = [
    ("CLAUDE.md", "第〇节：工作根裁定"),
    (".claude/goals/CG-007-formalization-completion/HANDOFF-2026-10-11-CODEX-W8-D3.md",
     "本轮实测交接（唯一缺口、iT_neg 报错、修法、陷阱）"),
    ("最高指示-Claude版.md", "Claude 操作版最高指示（随 .claude/rules 常驻）"),
    ("核心认知.md", "用户原文权威"),
    (".claude/总索引.md", "Claude 工作登记入口"),
    ("形式化追踪/README.md", "形式化各线进度入口"),
]

# 工具链（仓库外，worktree 共用）
TOOLCHAIN = [
    ("/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0", "Lean 4.34.0"),
    ("/Volumes/D/HoTT-toolchain-cache/foundation-src", "Foundation 源码（1fb01b72）"),
    ("/Volumes/D/HoTT-toolchain-cache/foundation-build-1fb01b72-v4.34.0",
     "Foundation 构建树（olean）"),
]

# 本 worktree 内的开发/收据回路
TOOLS = [
    (".claude/goals/CG-007-formalization-completion/tools/devbuild_ns.py",
     "开发编译回路（无沙箱，仅迭代）"),
    (".claude/goals/CG-007-formalization-completion/tools/capture_run.py",
     "正式收据（带沙箱、拒 sorry）"),
    (".claude/goals/CG-006-zfc-complete-formalization/tools/zfc_lean_check.py",
     "收据驱动（capture_run 调用它）"),
    (".claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py",
     "收据校验器（--rerun 精确重放）"),
    (".claude/goals/CG-001-targeted-overview/证据索引.md",
     "CG-001 证据索引（校验器要求先有行）"),
    ("HoTT/CLAIM_EVIDENCE_MATRIX.md", "共享命题-证据矩阵"),
]

# 缺口源码
SOURCES = [
    (f"{PACKAGE}/GodelQ/ZFC/Z0Blocked.lean", "zfcTr_D3_internalize（带 sorry，唯一实质缺口）"),
    (f"{PACKAGE}/GodelQ/ZFC/ShCraigElimNegLaw.lean", "iT_neg（当前拦路石）"),
    (f"{PACKAGE}/GodelQ/ZFC/NegInvolution.lean", "neg_neg_code（已编译，待出收据）"),
    (f"{PACKAGE}/GodelQ/ZFC/SeqTranslateFormula.lean", "isSemiformula_iT（已证，C-391）"),
]

fails: list[str] = []


def ok(label: str, note: str = "") -> None:
    print(f"  ✓ {label}" + (f" — {note}" if note else ""))


def bad(label: str, note: str = "") -> None:
    fails.append(label)
    print(f"  ✗ {label}" + (f" — {note}" if note else ""))


def run_git(*args: str) -> str:
    r = subprocess.run(["git", *args], capture_output=True, text=True)
    return r.stdout.strip()


def main() -> int:
    root = Path.cwd()

    print("1. 工作根与分支")
    top = run_git("rev-parse", "--show-toplevel")
    branch = run_git("rev-parse", "--abbrev-ref", "HEAD")
    if top == EXPECT_TOPLEVEL:
        ok("toplevel", top)
    else:
        bad("toplevel", f"实际 {top}，期望 {EXPECT_TOPLEVEL}")
    if branch == EXPECT_BRANCH:
        ok("branch", branch)
    else:
        bad("branch", f"实际 {branch}，期望 {EXPECT_BRANCH}")
    if (root / ".git").is_file():
        ok(".git 是文件", "worktree 而非主检出")
    else:
        bad(".git 不是文件", "这里可能是主检出，先停下校准")
    if Path(DEV_CHECKOUT).exists():
        dev_head = subprocess.run(
            ["git", "-C", DEV_CHECKOUT, "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True).stdout.strip()
        ok("dev 主检出可见", f"HEAD {dev_head}（集成目标，不要写）")

    print("\n2. 开工闭包")
    for rel, note in CLOSURE:
        (ok if (root / rel).exists() else bad)(rel, note)

    print("\n3. 缺口源码")
    for rel, note in SOURCES:
        p = root / rel
        if not p.exists():
            bad(rel, note)
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        n_sorry = text.count("sorry")
        ok(rel, f"{note}；{len(text.splitlines())} 行，{n_sorry} 处 sorry")

    print("\n4. 工具链（仓库外）")
    for path, note in TOOLCHAIN:
        (ok if Path(path).exists() else bad)(path, note)

    print("\n5. 开发与收据回路")
    for rel, note in TOOLS:
        (ok if (root / rel).exists() else bad)(rel, note)

    print("\n6. 编译缓存")
    cache = root / ".claude/goals/CG-007-formalization-completion/tools/devbuild_ns"
    state = cache / "godel-q-zfc-z0-full" / "_state.json"
    if state.exists():
        d = json.loads(state.read_text())
        ok("缓存 _state.json", f"{len(d)} 个模块条目")
        key = "GodelQ/ZFC/NegInvolution.lean"
        ok("NegInvolution 缓存条目",
           "在（哈希未变会 ## skip；要强制重编译先删该条目）" if key in d
           else "不在（下次会重新编译）")
    else:
        print("  · 缓存尚未建立（首次编译会从零开始，约 90 秒）")

    print("\n7. 未推送提交（本地分支保护）")
    n = run_git("rev-list", "--count", f"{EXPECT_BRANCH}", "--not", "dev")
    if n.isdigit() and int(n) > 0:
        up = run_git("rev-parse", "--abbrev-ref", "@{upstream}")
        if up.startswith("origin/"):
            ahead = run_git("rev-list", "--count", f"{up}..HEAD")
            note = (f"已跟踪 {up}；{ahead} 个提交待推送" if ahead not in ("", "0")
                    else f"已跟踪 {up}，与远端一致")
        else:
            note = "未设上游；push 需研究发起人授权"
        ok(f"{n} 个提交领先 dev", note)
    else:
        print(f"  · 领先 dev 的提交数：{n or '未知'}")

    print()
    if fails:
        print(f"结果：{len(fails)} 项有问题 → {', '.join(fails)}")
        return 1
    print("结果：全部就绪，可以在本 worktree 独立开工。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
