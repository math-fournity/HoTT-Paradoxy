# halting-without-lem：判不全不靠排中律（CG001-C-422）

> CG-007（`.claude/goals/CG-007-formalization-completion/`），W8 之后的单元。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-14；独立 worktree `claude/012-opus-w8`。精确命题、读法与禁止外推见 `CLAIM.md`。

## 这个包做了什么

CN-079 说，判不全是现实：任何机器都判定不了停机，这个证明用不到排中律。那一句原先凭记忆，本包把它的逻辑核心做成机器证明。

- **构造一侧（不依赖任何公理）**：
  - 前提只要一条编程事实：给定程序 `d`，能写出“翻转程序” `f`。`f` 在 `x` 上停机，恰好当 `d` 对 (x, x) 回答“否”。
  - 在任何满足它的编程系统里，没有程序恰好认出“永不停机”，也没有完全的停机判定器。
  - 证明就是把翻转程序喂给它自己，得到说谎者的形状 `P ↔ ¬P`。
- **实例（经典）**：Mathlib 的部分递归函数代码有翻转程序，所以论证在真实的计算模型里成立。经典的只是“翻转程序存在”这句正面事实；Mathlib 自己的停机定理也依赖 `Classical.choice`，审计核对过。
- **正控制**：去掉翻转程序，认出者可以存在。所以这一条是用到的前提。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| `GodelQ/Diagonal/Core.lean` | 编程系统、对角论证、正控制（只用 Lean 内核） |
| `GodelQ/Diagonal/MathlibCodes.lean` | Mathlib 计算模型的翻转程序与实例 |
| `GodelQ/Diagonal/QualificationDiag.lean` | 命题对照 `qual_C422`、`qual_C422_codes` 与公理审计 |
| `GodelQ/Negative/WrongRecognizerWithoutFlip.lean` | 负控制：没有翻转程序也照搬对角论证 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,193 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261014-CG001-HALTING-WITHOUT-LEM-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261014-CG001-HALTING-WITHOUT-LEM-NEG-FLIP-01 --rerun --expect-rejected
```

## 运行（2026-10-14）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261014-CG001-HALTING-WITHOUT-LEM-01` | `MP-CG001-HALTING-WITHOUT-LEM-001` | 接受 | 0（5 秒，stderr 0 B；审计 5 条“不依赖”、4 条对照“依赖”全部通过） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261014-CG001-HALTING-WITHOUT-LEM-NEG-FLIP-01` | `MP-CG001-HALTING-WITHOUT-LEM-NEG-001` | 拒绝 | 1：`hd d d` 是 `True ↔ ¬False`，不是 `P ↔ ¬P` | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出在 `.claude/goals/CG-001-targeted-overview/verification/` 下，与运行同名；索引在同一目标的 `证据索引.md` §53（012-Opus）与共享矩阵末节。`CLAIM.md`、两份固定记录与源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
