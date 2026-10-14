# godel-q-zfc-z0-freevar：自由变量不受 ω 限制，“证明逐条翻译”的不变量在 ℕ 中就不成立（CG001-C-410–C-412）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W8，本机会话 95a1a81b（012-Opus，Opus 5.5），2026-10-14，独立 worktree `claude/012-opus-w8`。精确命题、证明与禁止外推见 `CLAIM.md`。

## 这个包做了什么

- **背景**：要把“𝗭𝗙𝗖 证明不了自己算术影子的一致性”（C-120）读成“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”，还差一条可导性条件 D3。舰队尝试的办法是：把算术推导一步一步翻译成 𝗭𝗙𝗖 推导，对推导作归纳。
- **问题出在自由变量**：把算术句翻译成集合论句时，量词被限制在 ω（自然数集）上，但自由变量没有加“属于 ω”的条件，仍可以是任何集合。推导的中间步骤含自由变量。
- **结果**：
  - 内部翻译对带自由变量的公式也逐字正确（C-410）。这把“自由变量不受 ω 限制”机器证实到内部翻译。
  - 舰队正在证的中间引理 ExsBridge2 是假的，在标准模型 ℕ 里就假（C-411）。
  - 舰队的归纳不变量 Q 也是假的：一条只用逻辑规则、两步长的推导（结论 `{∃x (x<0), ¬(&0<0)}`），翻译后 𝗭𝗙𝗖 推不出来（C-412）。原因一句话：把自由变量 &0 取成 ω，`(&0 < 0)` 的翻译就因前件不可满足而为真，它的否定为假。
- **不说明的**：Z0 的真假、D3 的真假、舰队对句子陈述的 `ShCraigElim` 的真假，这些都不受影响（`CLAIM.md` §4、§5）。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| 23 个依赖模块（`ProcessObservation` 至 `ZFC/TranslateRE.lean`） | 与 `../godel-q-zfc-z0-translate/` 逐字节相同 |
| `GodelQ/ZFC/OpenTranslate.lean` | C-410：`iVE_pquote`、`iT_pquote` |
| `GodelQ/ZFC/SeqTranslate.lean` | 舰队的 `translateSeq`，与 `dev` 逐字节相同 |
| `GodelQ/ZFC/FreeVarCounter.lean` | C-411、C-412：`exsBridge2_false`、`dCounter_not_Q`、`q_invariant_false`、`exsBlockerQ_false` |
| `GodelQ/Negative/WrongCounterInOmega.lean` | 负控制：自由变量改赋 ∅（∅ ∈ ω），同一证明脚本必须被拒绝 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包的逐模块哈希（1,893 个模块，聚合 `02b0e80f…5161`） |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261014-CG001-GODEL-Q-ZFC-Z0-FREEVAR-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261014-CG001-GODEL-Q-ZFC-Z0-FREEVAR-NEG-OMEGA-01 --rerun --expect-rejected
```

## 运行（2026-10-14）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261014-CG001-GODEL-Q-ZFC-Z0-FREEVAR-01` | `MP-CG001-GODEL-Q-ZFC-Z0-FREEVAR-001` | 接受 | 0（84 秒，stderr 0 B；115 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound；14 条警告（`grep -c warning` 计 15 行，其中一行是续行）：10 条在复制来的依赖模块里，4 条是 `OpenTranslate.lean` 中未用到的 simp 参数） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261014-CG001-GODEL-Q-ZFC-Z0-FREEVAR-NEG-OMEGA-01` | `MP-CG001-GODEL-Q-ZFC-Z0-FREEVAR-NEG-OMEGA-001` | 拒绝 | 1：`h0.right` 的类型是 `w 0 = ∅`，证明需要 `w 0 = ω` | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261014-CG001-GODEL-Q-ZFC-Z0-FREEVAR-*.json`。索引：同目标的 `证据索引.md` §50（012-Opus），以及共享矩阵末节。`CLAIM.md`、两份固定记录与三个工具已进入收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
