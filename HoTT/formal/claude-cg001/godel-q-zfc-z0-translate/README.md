# godel-q-zfc-z0-translate：翻译可计算；Z0 的影子形式不再带前提（CG001-C-119、C-120）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W4b，本机会话 d58e0c0d，Opus 5.5，2026-10-09。精确命题、还差的一步与禁止外推见 `CLAIM.md`。

## 这个包做了什么

- **问题**：Z0 问的是“𝗭𝗙𝗖 能不能确认自己的矛盾搜索永不停”。此前它被归结为一条语法引理：把算术句翻译成集合论句的那个具体函数，能用机器算出来（C-111）。
- **做法**：在算术理论 𝗜𝚺₁ 内部，把这条翻译重写一遍，写成一个 Σ1 函数：项一层、原子公式一层、公式一层，量词限制在 ω 上。然后证明，在 𝗜𝚺₁ 的每个模型里，它都恰好算出翻译后句子的编码。到了自然数 ℕ，这就是一个算得出来的函数。
- **结果**：
  - 翻译可计算（C-111 的阻塞引理）；
  - 𝗭𝗙𝗖 能证明的“翻译后的算术句”可以被机器一一列出；
  - Z0 的影子形式不再带任何前提：𝗭𝗙𝗖 证明不了它的算术影子的一致性句（翻译后）。
- **还差一步**：把这个一致性句换成 𝗭𝗙𝗖 自己的一致性句，需要在 𝗜𝚺₁ 内部把证明也翻译过去（W8，见 `CLAIM.md` §4）。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| 21 个依赖模块（`ProcessObservation` 至 `ZFC/ShRE.lean`） | 与 `../godel-q-zfc-z0-re/` 逐字节相同 |
| `GodelQ/ZFC/InternalTranslate.lean` | 内部翻译 `iVE`、`iTR`、`iT`，Σ1 定义与正确性 `iVE_quote`、`iT_quote` |
| `GodelQ/ZFC/TranslateRE.lean` | `translate_computable`、`translate_provable_re`、`Sh_RE`、`zfc_z0`、`sh_z0` |
| `GodelQ/ZFC/QualificationTranslate.lean` | 命题对照 `qual_C119`、`qual_C120` |
| `GodelQ/Negative/WrongZ0WithoutRE.lean` | 负控制：没有内部翻译，就没有 `Sh.RE` |
| `GodelQ/Negative/WrongTranslateNoDomain.lean` | 负控制：量词去掉 ω 限制 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-RE-01 --rerun --expect-rejected
```

另一个负控制把 `NEG-RE-01` 换成 `NEG-DOMAIN-01`。

## 运行（2026-10-09）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-01` | `MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-001` | 接受 | 0（72 秒，stderr 0 B；106 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound；11 条警告都在复制来的依赖模块里） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-RE-01` | `MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-RE-001` | 拒绝 | 1：找不到实例 `Theory.RE Sh` | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |
| `20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-DOMAIN-01` | `MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-DOMAIN-001` | 拒绝 | 1：目标 `^∀ imp ℒₛₑₜ domZero ⌜φ⌝ = ^∀ ⌜φ⌝` 未解 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-*.json`。索引：同目标的 `证据索引.md` §34，以及共享矩阵末节。`CLAIM.md`、两份固定记录与三个工具已进入收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
