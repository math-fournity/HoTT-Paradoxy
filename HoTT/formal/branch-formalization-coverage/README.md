# branch-formalization-coverage：八个 git worktree 的形式化资产在 `dev` 上全部有可重放收据（CG001-C-123 至 C-126）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W9。精确命题、逐线覆盖判定与禁止外推见 `CLAIM.md`。

## 这个包做了什么

- **问题**：研究发起人要求 Cover 八个 worktree 留下的工作方向。八条线的形式资产此前分三处：已并入 `dev` 的（有 `dev` 收据）、留在分支上的（只有分支自己的收据，`dev` 指向不到）、以及根本没有形式包的。
- **做法**：把第二类里能用本机 Lean core 执行的全部源（16 正 + 2 负控制）逐字节复制过来，用 pinned Lean 4.34.1 在禁网沙盒里重新编译，生成 `dev` 上的正式收据。
- **结果**：八个方向上，每一条要么有 `dev` 收据（已并入的两条 + 本包补齐的三条），要么照实判为不适用（无形式包的三条），要么判为本机不可重放并保持 `SOURCE_REPORTED_NOT_REPLAYED`（dev-09 的外部 Foundation 包，它的运行依赖一个已不存在的检出）。
- **没有做**：没有证明任何新命题。所有定理在各自分支上已被 GPT 各线证明。

## 文件

| 文件 | 内容 |
|---|---|
| `GodelQ/*.lean`（18 个） | 从 `origin/dev-02`、`origin/dev-03`、`origin/dev-04` 逐字节复制的 Lean-core 源；16 个正源 + 2 个负控制 |
| `LEAN_TOOLCHAIN.json` | pinned Lean 4.34.1 二进制（字节 + SHA-256）与版本行 |
| `CLAIM.md` | 逐线覆盖判定、精确命题、禁止外推、逐文件来源 |

驱动：`.claude/goals/CG-007-formalization-completion/tools/capture_branch_run.py`。

## 运行（2026-10-09）

| run | proof | 预期 | 退出 | 结果 |
|---|---|---|---|---|
| `20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-06` | `MP-CG001-BRANCH-FORMALIZATION-COVERAGE-001` | 接受 | 0（16 个正源，165 条 `#print axioms` 全为无公理） | KERNEL_ACCEPTED_WITH_SCOPE |
| `20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-NEG-02` | `MP-CG001-BRANCH-FORMALIZATION-COVERAGE-NEG-001` | 拒绝 | 1（`assumption` 失败 / 模块解析失败，均在预定点） | KERNEL_REJECTED（预期内） |

`-01/02/03/04/05` 与 `-NEG-01` 是修正驱动时的失败或不完整尝试，不是结论证据；判据以 `-06` 与 `-NEG-02` 为准，理由见 `CLAIM.md` §3。索引路线（为什么本包不进 `PROOF_VERSION_CLOSURE`）见 `CLAIM.md` §6。

索引：CG-001 目标 `证据索引.md` §36，共享矩阵末节。
