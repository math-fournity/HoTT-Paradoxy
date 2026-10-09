# godel-q-zfc-turing：图灵路线——不对 𝗭𝗙𝗖 做自指的观察力不完备（CG001-C-104、C-105）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W1，本机会话 d58e0c0d，Opus 5.5，2026-10-08。精确命题与禁止外推见 `CLAIM.md`。

## 这个包做了什么

研究发起人要两个结果：“1、无哥德尔的思路。2、有哥德尔的思路。”（dev-notes 0115）本包是无哥德尔路线的第一个形式交付，落在 Foundation 中真实的 `𝗭𝗙𝗖` 上，只比较两个集合：

- 𝗭𝗙𝗖 能证明为“永不停”的过程，可以被机器列出；
- 真正永不停的过程，没有机器能列全。

所以 𝗭𝗙𝗖 必有漏点。这些漏点恰是“永不停机”句独立于 𝗭𝗙𝗖 的过程：它们有无穷多个，列不全，有限的补丁补不完；而对其中每一个，𝗭𝗙𝗖 在每个有限时刻都证明“还没停”。证明里没有关于 𝗭𝗙𝗖 的自指过程或自指句，源码末尾的依赖检查在 Lean 中机器核对了这一点。

【翻查】GPT 的线上没有这条路线的先例。主干 dev-08 #4–#9 提醒过：不能拿停机问题、“不可枚举”直接替代原问题。本包没有替代：任务、观察与 Done 都与 C-99/C-100 相同（𝗭𝗙𝗖 对过程停机的观察），只是换了一种证明手法。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| `GodelQ/ProcessObservation.lean`、`EffectiveTheory.lean` | 与 `../godel-q-zfc/` 逐字节相同 |
| `GodelQ/Turing.lean` | 抽象层：漏点不可枚举、无穷、有限补丁补不完；有效理论的 Q 不完备（图灵式）；依赖检查器 `GodelQ.reaches` |
| `GodelQ/GodelZenoRunner.lean`、`FoundationArith.lean`、`GodelQ/ZFC/` 的 12 个模块（SetLanguage 至 Soundness） | 与 `../godel-q-zfc/` 逐字节相同 |
| `GodelQ/ZFC/TuringZFC.lean` | 𝗭𝗙𝗖 实例：漏点 = 独立点、不可枚举、无穷、每一刻看得见、𝗭𝗙𝗖 不完全、有限补丁；依赖检查 |
| `GodelQ/ZFC/QualificationTuring.lean` | 命题对照 `qual_C104`、`qual_C105` |
| `GodelQ/Negative/WrongTuringWithTruthObserver.lean` | 负控制：把不可枚举的真理观察者当作可枚举观察者 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,889 个模块）的逐模块哈希 |

## 复现

在仓库根目录：

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261008-CG001-GODEL-Q-ZFC-TURING-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261008-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-01 --rerun --expect-rejected
```

## 运行（2026-10-08）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261008-CG001-GODEL-Q-ZFC-TURING-01` | `MP-CG001-GODEL-Q-ZFC-TURING-001` | 接受 | 0（58 秒，stderr 0 B；87 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound；两行依赖检查通过） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261008-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-01` | `MP-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-001` | 拒绝 | 1：`re` 字段处 `simp` 无进展 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261008-CG001-GODEL-Q-ZFC-TURING-*.json`；索引：同目标 `证据索引.md` §27；共享矩阵末节。`CLAIM.md`、两份固定记录与三个工具（驱动、固定记录生成、捕获）进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
