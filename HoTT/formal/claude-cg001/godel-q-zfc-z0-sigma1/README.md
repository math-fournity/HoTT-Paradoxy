# godel-q-zfc-z0-sigma1：𝗭𝗙𝗖 证明不了“𝗭𝗙𝗖 一致”——完整 Z0，不带前提（CG001-C-413–C-417）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W8，本机会话 95a1a81b（012-Opus，Opus 5.5），2026-10-14，独立 worktree `claude/012-opus-w8`。精确命题、证明与禁止外推见 `CLAIM.md`。

## 这个包做了什么

- **要证的事**：𝗭𝗙𝗖 证明不了“𝗭𝗙𝗖 一致”（Gödel 第二不完全性对 𝗭𝗙𝗖 的形式）。
  - 本仓库此前只有两样：一是对 𝗭𝗙𝗖 的算术影子的版本（C-120）；二是 `Z0Full.lean` 的条件定理，前提是一条可导性条件 D3。
  - D3 说：若 𝗭𝗙𝗖 证明了某个算术句的翻译，那么 𝗭𝗙𝗖 也证明“𝗭𝗙𝗖 证明了它”的翻译。
- **怎么证的**：D3 来自一条更一般的事实。凡是“存在一个有限的见证”这一类为真的算术句（Σ1 句），它的翻译 𝗭𝗙𝗖 都能证明。“𝗭𝗙𝗖 证明了 τ”正是这一类句子。本包把这条事实在任意算术模型 V 中证出来（形式化的 Σ1 完全性）。
- **难点**：
  - 集合论语言里没有“数字”这种项，只能用公式描述“第 a 个自然数”：空集、空集的后继……（Rayo 式数字公式）。
  - V 中的 a 可以是非标准的“无穷大”数，这些公式本身也要在 V 里构造。
  - 加法、乘法、小于、有界量词，都要在 𝗭𝗙𝗖 内部、对这种数字逐一证明。
  - 舰队走的是“把推导逐条翻译”的路线，那条路线的不变量在 ℕ 中就不成立（C-410–C-412）。本包换了路线，只对标准公式作元层归纳，非标准的只有数字。
- **结果**：`zfc_z0_unconditional : 𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent)`，不带未证前提。所需的“𝗭𝗙𝗖 一致”由 Lean 自己的元理论提供：Foundation 的 `zfc_consistent`，一个 Lean 元层的 𝗭𝗙𝗖 模型（见 `CLAIM.md` §4）。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| 23 个依赖模块（`ProcessObservation` 至 `ZFC/TranslateRE.lean`） | 与 `../godel-q-zfc-z0-translate/` 逐字节相同 |
| `GodelQ/ZFC/Z0Full.lean` | 与 `dev`（`53f4f82d`）逐字节相同，SHA-256 `660f2755…bc75a` |
| `GodelQ/ZFC/IntLogic.lean` | 内部逻辑小工具：上下文中的 ∃ 引入与消去、引号的 simp 标准形 |
| `GodelQ/ZFC/SetNum.lean`、`SetNumArith.lean` | C-413：数字公式的存在、属于 ω、唯一、相合；加法、乘法、小于、不小于、不等 |
| `GodelQ/ZFC/TransTyped.lean` | 翻译的有型形状：变量等式在参数代换下的形状、原子公式 |
| `GodelQ/ZFC/TransTerm.lean` | C-414：上下文平移、参数假设、反向加法与乘法、项引理 `term_ve` |
| `GodelQ/ZFC/TransBall.lean` | C-415：有界 ∀ 的合并（V 中归纳） |
| `GodelQ/ZFC/TransSigma1.lean` | C-416：经翻译的形式化 Σ1 完全性 |
| `GodelQ/ZFC/Z0D3.lean` | C-417：D3 与完整 Z0 |
| `GodelQ/Negative/BallMergeOffByOne.lean` | 负控制：合并的界错一位，同一证明脚本必须被拒绝 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包的逐模块哈希（1,893 个模块，聚合 `02b0e80f…5161`） |
| `PLAN.md` | 施工计划与记录（不进收据） |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-NEG-BALL-01 --rerun --expect-rejected
```

## 运行（2026-10-14）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-01` | `MP-CG001-GODEL-Q-ZFC-Z0-SIGMA1-001` | 接受 | 0（110 秒，stderr 0 B；138 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound；43 条警告全是 linter 提示：10 条在复制来的依赖模块，33 条在新文件，都是未用的 simp 参数或“`simpa` 可改 `simp`”） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-NEG-BALL-01` | `MP-CG001-GODEL-Q-ZFC-Z0-SIGMA1-NEG-BALL-001` | 拒绝 | 1（107 秒）：`BallMergeOffByOne.lean:118:39`，`key b le_rfl` 给出关于 N_b 的结论，与要求的 N_{b+1} 不符 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

- 校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261014-CG001-GODEL-Q-ZFC-Z0-SIGMA1-*.json`。
- 索引：同目标的 `证据索引.md` §51（012-Opus），以及共享矩阵末节。
- `CLAIM.md`、两份固定记录与三个工具已进入收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
- 负控制的第一次捕获，源文件末尾多了一行 `#print axioms`。被拒绝的定理因此带出 `sorryAx`，冻结的校验器对任何含 `sorryAx` 的输出一律不通过。我删去这一行，把那次运行目录移入废纸篓，按 `tools/README.md` 的规定以同名 run-id 重新捕获。上表是重捕的结果。
