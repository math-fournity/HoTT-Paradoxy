# zeno-zfc-classical：经典芝诺的两句落到 Foundation 的 𝗭𝗙𝗖（CG001-C-423）

> CG-010（worktree `claude/012-opus-w8`）R1。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。精确命题、读法与禁止外推见 `CLAIM.md`。

## 这个包做了什么

经典芝诺（每次走剩下的一半）的两件事，𝗭𝗙𝗖 都证得出：
- 极限意义上“到了”：对每个精度 2⁻ᴷ，从某一步起剩余距离都不超过它；
- 哪一步都没到：没有一步的余量为零。

𝗭𝗙𝗖 也证明不了“在某一步到了”。这补上了缺口表第 9 行此前“数学上显然、没有机器核对”的那一句。按研究发起人 10-14 对 Q 的定义（ASK），它落实的是：𝗭𝗙𝗖 看得见过程的两面，缺的是门口那一问，不是眼睛。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| `GodelQ/ZFC/*`、`GodelQ/ProcessObservation.lean` 等 18 个 | 依赖模块，逐字节复制自 `godel-q-zfc-runner-arrival` |
| `GodelQ/Zeno/ZenoClassicalZFC.lean` | 两句的算术写法；每个 𝗣𝗔⁻ 模型里成立；𝗭𝗙𝗖 证明它们的翻译；𝗭𝗙𝗖 证明不了“有一步余量为零” |
| `GodelQ/Zeno/ZenoReading.lean` | 实数读法：(1/2)ⁿ ≤ (1/2)ᴷ ⟺ K ≤ n，(1/2)ⁿ → 0，(1/2)ⁿ > 0 |
| `GodelQ/Zeno/QualificationZenoZFC.lean` | 命题对照 `qual_C423` |
| `GodelQ/Negative/WrongFiniteArrival.lean` | 负控制：第 0 步余量为零 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261015-CG001-ZENO-ZFC-CLASSICAL-01 --rerun
```

负控制加 `--expect-rejected`，运行目录为 `20261015-CG001-ZENO-ZFC-CLASSICAL-NEG-FINITE-01`。

## 运行（2026-10-15）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261015-CG001-ZENO-ZFC-CLASSICAL-01` | `MP-CG001-ZENO-ZFC-CLASSICAL-001` | 接受 | 0（56 秒，stderr 0 B；92 条公理报告全为三条标准公理） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261015-CG001-ZENO-ZFC-CLASSICAL-NEG-FINITE-01` | `MP-CG001-ZENO-ZFC-CLASSICAL-NEG-001` | 拒绝 | 1：`K = 0` 未解 | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出在 `.claude/goals/CG-001-targeted-overview/verification/` 下，与运行同名；索引在同一目标的 `证据索引.md` §54（012-Opus）与共享矩阵末节。`CLAIM.md`、两份固定记录与源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
