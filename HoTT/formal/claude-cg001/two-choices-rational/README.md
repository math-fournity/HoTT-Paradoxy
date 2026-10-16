# two-choices-rational：两次选择的有理数形态（CG001-C-425）

> CG-010（worktree `claude/012-opus-w8`）R3。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。精确命题、读法、文献与禁止外推见 `CLAIM.md`。

## 这个包做了什么

研究发起人 2026-10-14 说：“放弃是一次选择，而A是第二次选择。A是什么？A就是一个无限的步骤才能到达，从而存在的结果，当作已经存在的结果，参与运算。”

C-418（`../two-choices-lpo/`）在整数刻度上证明了两次选择互推，但实数形态只能引文献，因为 Mathlib 的 ℚ 本身用了排中律。本包自己写一套最小的有理数（整数对，交叉相乘比较），补上这一形态：

- **两次选择在实数形态上也是同一条原则（C-425 (1)(2)）**：
  - 在不预设排中律的底座上，“每个有界单调的有理数列都收敛”与 LPO 互推。前者是 A 落在实数上的样子：单调有界数列的极限现成可用；后者是“放弃 ASK”落在真假值上的样子：每个无限搜索停不停已经定了。
  - 包内的公理审计机器断言：这些证明不用 `Classical.choice`。
- **芝诺的极限用不着 A（C-425 (3)–(9)）**：
  - 芝诺位置 1 − 2⁻ⁿ 每一步都小于 1；
  - 柯西步与“离 1 小于 1/(k+1)”的步都由公式 k + 1 直接给出，不搜索，不用 LPO；
  - 步数不能一律取 0，所以这个公式是实质内容。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| `GodelQ/TwoChoices/Core.lean` | LPO、A 的整数形态与互推（逐字节复制自 `two-choices-lpo`） |
| `GodelQ/TwoChoices/RationalConstructive.lean` | 自写的有理数；`BMCQ ↔ LPO`；芝诺对照 |
| `GodelQ/TwoChoices/QualificationRational.lean` | 命题对照 `qual_C425` 与公理审计 |
| `GodelQ/Negative/WrongBMCQForFree.lean` | 负控制：借排中律“免费”得到 `BMCQ`，被审计拒绝 |
| `GodelQ/Negative/WrongZenoModulus.lean` | 负控制：芝诺的柯西步一律取第 0 步 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,180 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261015-CG001-TWO-CHOICES-RATIONAL-01 --rerun
```

负控制加 `--expect-rejected`，运行目录换成 `20261015-CG001-TWO-CHOICES-RATIONAL-NEG-FREE-01` 或 `-NEG-MODULUS-01`。

## 运行（2026-10-15）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261015-CG001-TWO-CHOICES-RATIONAL-01` | `MP-CG001-TWO-CHOICES-RATIONAL-001` | 接受 | 0（4 秒，stderr 0 B；16 条公理报告；审计 15 条“不依赖”、2 条对照“依赖”全部通过） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261015-CG001-TWO-CHOICES-RATIONAL-NEG-FREE-01` | `MP-CG001-TWO-CHOICES-RATIONAL-NEG-001` | 拒绝 | 1：审计报出 `bmcQ_for_free` 依赖 `Classical.choice` | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |
| `20261015-CG001-TWO-CHOICES-RATIONAL-NEG-MODULUS-01` | `MP-CG001-TWO-CHOICES-RATIONAL-NEG-002` | 拒绝 | 1：`omega` 证不出 `k + 1 ≤ m` | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出在 `.claude/goals/CG-001-targeted-overview/verification/` 下，与运行同名；索引在同一目标的 `证据索引.md` §56（012-Opus）与共享矩阵末节。`CLAIM.md`、两份固定记录与源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
