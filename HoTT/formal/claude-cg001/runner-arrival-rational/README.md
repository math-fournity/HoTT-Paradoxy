# runner-arrival-rational：极限的有理数 ε–N 写法落到 𝗭𝗙𝗖（CG001-C-428）

> CG-010（worktree `claude/012-opus-w8`）R7。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。精确命题、读法与禁止外推见 `CLAIM.md`。

## 这个包做了什么

研究发起人问过：“明明芝诺悖论没有解决，为什么极限理论可以声称已经在ZFC中解决了呢？”此前，𝗭𝗙𝗖 里的极限句只用 2⁻ᴷ 这一族精度（写成“已减半至少 K 次”），通常的极限定义却对每个正精度说话。本包把精度换成全部正有理数 p/q，用 Foundation 的算术指数写出通常的 ε–N 句：

- **经典芝诺**：𝗭𝗙𝗖 证明“对每个正有理数 p/q，从某一步起 2⁻ⁿ < p/q”。这正是极限理论对芝诺的判词。
- **哥德尔–芝诺跑者**：
  - 通常写法的“跑者到达”，在 𝗭𝗙𝗖 里逐个等价于 2⁻ᴷ 写法，也等价于“永不停机”；
  - 有一个跑者确实到达，𝗭𝗙𝗖 每一刻都看得见它还没停，却证明不了它“到了”。
- **字面意思**：两句话在自然数里逐字就是通常的 ε–N 写法，ε 取遍正有理数。

没有做的：在 𝗭𝗙𝗖 内部把实数构造成集合。“ε 取遍正有理数”与“ε 取遍正实数”等价，是阿基米德性质，留在 Lean 元层；完整构造 ℝ 的工作量与 W8 的 D3 同级，照实不做。

## 文件（按编译次序）

- 23 个依赖模块，逐字节复制自 `../godel-q-zfc-runner-arrival/GodelQ/`。
- 新文件：

| 文件 | 内容 |
|---|---|
| `GodelQ/ZFC/ArrivalRational.lean` | 有理精度的到达句与极限句：模型、𝗭𝗙𝗖、ℕ 三层 |
| `GodelQ/ZFC/QualificationArrivalRational.lean` | 命题对照 `qual_C428` |
| `GodelQ/Negative/WrongRationalStepZero.lean` | 负控制：从第 0 步起就够近 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,889 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261015-CG001-RUNNER-ARRIVAL-RATIONAL-01 --rerun
```

负控制加 `--expect-rejected`，运行目录为 `20261015-CG001-RUNNER-ARRIVAL-RATIONAL-NEG-STEP-01`。

## 运行（2026-10-15）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261015-CG001-RUNNER-ARRIVAL-RATIONAL-01` | `MP-CG001-RUNNER-ARRIVAL-RATIONAL-001` | 接受 | 0（71 秒，stderr 0 B；144 条公理报告全为三条标准公理） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261015-CG001-RUNNER-ARRIVAL-RATIONAL-NEG-STEP-01` | `MP-CG001-RUNNER-ARRIVAL-RATIONAL-NEG-001` | 拒绝 | 1：需要 `q ≤ n`，只有 `0 ≤ n` | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

- 校验输出在 `.claude/goals/CG-001-targeted-overview/verification/` 下，与运行同名。
- 索引在同一目标的 `证据索引.md` §59（012-Opus）与共享矩阵末节。
- `CLAIM.md`、两份固定记录与源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
