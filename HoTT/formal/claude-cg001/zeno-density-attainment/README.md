# zeno-density-attainment：取到与贴近——稠密性恰是芝诺缺口的前提（CG001-C-106 至 C-108）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W2，本机会话 d58e0c0d，Opus 5.5，2026-10-08。精确命题、归因与禁止外推见 `CLAIM.md`。

## 这个包做了什么

无哥德尔路线的候选形态 (b)，承接“时间”的时空结构一面（稠密与离散）。研究发起人：“在稠密性的空间中，无法完成现实可以完成事情”（KC-000003）；“芝诺悖论对理论的攻击角度，是紧紧瞄准了稠密性来的”（KC-000048）。

- **两种“到了”**：在某一步恰好到了（原过程完成）；无限贴近（标准解的极限）。它们恰好在终点不孤立时分开，也就是空间稠密时；在量子化的格点上，它们是一回事（C-106）。
- **两种跑者**：量子化跑者每步走一半再取整到格点，恰在第 m+1 步到达，此前与稠密跑者一步不差；稠密跑者永不到达。两者的极限都是 1，所以只看极限判不了“到没到”。粒度越来越细，每一档都到得了，极限处的稠密跑者却到不了：“到达”在稠密化的极限里丢失了（C-107）。
- **时间一侧**：稠密的时间里，无穷多步可以挤在时刻 1 之前（超任务），标准解在时刻 1 宣布到达，但时刻 1 不是任何一步；在量子化的时间里，这样的超任务根本不存在（C-108）。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| `GodelQ/Zeno/Attainment.lean` | 取到与贴近；孤立点刻画（归因定理）；ℝ 的芝诺式过程；格点上贴近即取到；离散空间 |
| `GodelQ/Zeno/Runners.lean` | 稠密与量子化跑者；闭式；完成阶段；极限接口的碰撞与正控制；累次极限；时间一侧的超任务 |
| `GodelQ/Zeno/QualificationZeno.lean` | 命题对照 `qual_C106`、`qual_C107`、`qual_C108` |
| `GodelQ/Negative/WrongDenseAttains.lean` | 负控制：在稠密的 ℝ 里把终点当作孤立点 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,681 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261008-CG001-ZENO-DENSITY-ATTAINMENT-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261008-CG001-ZENO-DENSITY-ATTAINMENT-NEG-DENSE-01 --rerun --expect-rejected
```

## 运行（2026-10-08）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261008-CG001-ZENO-DENSITY-ATTAINMENT-01` | `MP-CG001-ZENO-DENSITY-ATTAINMENT-001` | 接受 | 0（10 秒，stderr 0 B；22 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261008-CG001-ZENO-DENSITY-ATTAINMENT-NEG-DENSE-01` | `MP-CG001-ZENO-DENSITY-ATTAINMENT-NEG-DENSE-001` | 拒绝 | 1：`Isolated (1 : ℝ)` 处留下未解目标 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261008-CG001-ZENO-DENSITY-ATTAINMENT-*.json`；索引：同目标 `证据索引.md` §28；共享矩阵末节。`CLAIM.md`、两份固定记录与三个工具进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
