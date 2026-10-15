# zfc-con-pa-boundary：𝗭𝗙𝗖 证 Con(𝗣𝗔) 落在哪条义务上（CG001-C-429；CG-010 R8 BLOCKED）

> CG-010（worktree `claude/012-opus-w8`）R8。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。精确命题、剩余义务与禁止外推见 `CLAIM.md`。

## 这个包做了什么

“𝗭𝗙𝗖 证明 𝗣𝗔 一致”是经典定理：在 𝗭𝗙𝗖 里 ω 是 𝗣𝗔 的模型，再在 ω 上定义真值并证明推导保持真值。本包**没有**在 Foundation 的 𝗭𝗙𝗖 上证出它，而是用机器把它归结成一条义务，并说明那条义务不能怎样付：

- **归结**：𝗭𝗙𝗖 证明 Con(𝗣𝗔)，当且仅当 𝗭𝗙𝗖 每个模型里的 ω 都满足 Con(𝗣𝗔)。
- **标准模型满足它**：所以 𝗭𝗙𝗖 驳不倒 Con(𝗣𝗔)。
- **只靠“ω 是 𝗣𝗔 的模型”不够**：有的 𝗣𝗔 模型不满足 Con(𝗣𝗔)（𝗣𝗔 的第二不完备）。
- **剩下的**：在 𝗭𝗙𝗖 的任意模型里，用它的集合给 ω 上的全部公式定义真值，并证明 𝗣𝗔 的公理都真、内部推导保持真值。Foundation 没有现成的；工作量估计大于 W8 的 D3，照实标为 BLOCKED。

## 文件（按编译次序）

- 18 个依赖模块，逐字节复制自 `../godel-q-zfc-runner-arrival/GodelQ/`。
- 新文件：

| 文件 | 内容 |
|---|---|
| `GodelQ/ZFC/ConPABoundary.lean` | 归结、标准模型、𝗭𝗙𝗖 驳不倒、有的 𝗣𝗔 模型不满足 |
| `GodelQ/ZFC/QualificationConPA.lean` | 命题对照 `qual_C429` |
| `GodelQ/Negative/WrongEveryPAModelCon.lean` | 负控制：把 ℕ 上的证明照搬到任意 𝗣𝗔 模型 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,893 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261015-CG001-ZFC-CON-PA-BOUNDARY-01 --rerun
```

负控制加 `--expect-rejected`，运行目录为 `20261015-CG001-ZFC-CON-PA-BOUNDARY-NEG-01`。

## 运行（2026-10-15）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261015-CG001-ZFC-CON-PA-BOUNDARY-01` | `MP-CG001-ZFC-CON-PA-BOUNDARY-001` | 接受 | 0（49 秒，stderr 0 B；87 条公理报告全为三条标准公理） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261015-CG001-ZFC-CON-PA-BOUNDARY-NEG-01` | `MP-CG001-ZFC-CON-PA-BOUNDARY-NEG-001` | 拒绝 | 1：`Consistent ℕ` 不是 `Consistent V` | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

- 校验输出在 `.claude/goals/CG-001-targeted-overview/verification/` 下，与运行同名。
- 索引在同一目标的 `证据索引.md` §60（012-Opus）与共享矩阵末节。
- `CLAIM.md`、两份固定记录与源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
