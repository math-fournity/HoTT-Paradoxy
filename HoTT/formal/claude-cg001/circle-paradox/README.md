# circle-paradox：圆环悖论本身（CG001-C-424）

> CG-010（worktree `claude/012-opus-w8`）R2。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。精确命题、逐句对照与禁止外推见 `CLAIM.md`。

## 这个包做了什么

研究发起人 2026-09-01 自己发明的圆环悖论：一个圆取一点拿走（M），两端展开成线段（N）；从 M 到 N 没有障碍，可从 N 逐步合回 M，“无论N的两端逼近到什么接近的程度，都无法再还原到M的状态。可是，可是，我们当初确实得到了M啊！”

- **拆开一步**：M 与 N 同胚。
- **合回永远差一点**：
  - 远端越来越近，任何有限阶段都没合上；
  - 每个有限阶段的形态都不是 M，只在极限那一刻是 M；
  - 缺口永远含无穷多个点，长度大于 0，所以“点没有大小”时，缺口永远不是“只剩一个点”。
- **圆环就是芝诺的幽灵**：合回的远端恰是芝诺跑者（C-106 的 `zenoSeq`）。
- **为什么**：拿走的那一点在圆上不是孤立点，即稠密。
- **离散环对照**：点有大小时，合回在有限步完成。

## 文件

| 文件 | 内容 |
|---|---|
| `GodelQ/Zeno/Attainment.lean` | 取到与贴近（逐字节复制自 `zeno-density-attainment`） |
| `GodelQ/Circle/CircleParadox.lean` | M、N、展开同胚、逐步合回、缺口、离散对照 |
| `GodelQ/Circle/QualificationCircle.lean` | 命题对照 `qual_C424` |
| `GodelQ/Negative/WrongFiniteClosing.lean` | 负控制：第 0 步就合上 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261015-CG001-CIRCLE-PARADOX-01 --rerun
```

负控制加 `--expect-rejected`，运行目录为 `20261015-CG001-CIRCLE-PARADOX-NEG-CLOSE-01`。

## 运行（2026-10-15）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261015-CG001-CIRCLE-PARADOX-01` | `MP-CG001-CIRCLE-PARADOX-001` | 接受 | 0（9 秒，stderr 0 B；20 条公理报告全为三条标准公理） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261015-CG001-CIRCLE-PARADOX-NEG-CLOSE-01` | `MP-CG001-CIRCLE-PARADOX-NEG-001` | 拒绝 | 1：`↑1 − ↑2⁻¹ = 0` 未解 | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出在 `.claude/goals/CG-001-targeted-overview/verification/` 下，与运行同名；索引在同一目标的 `证据索引.md` §55（012-Opus）与共享矩阵末节。`CLAIM.md`、两份固定记录与源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
