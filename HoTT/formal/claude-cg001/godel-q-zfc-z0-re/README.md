# godel-q-zfc-z0-re：𝗭𝗙𝗖 的定理集可枚举；Z0 归结为一条纯语法引理（CG001-C-111）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W4a，本机会话 d58e0c0d，Opus 5.5，2026-10-09。精确命题、阻塞分析与禁止外推见 `CLAIM.md`。

## 这个包做了什么

- 𝗭𝗙𝗖 能证明的句子可以被机器一一列出（`zfc_provable_re`）。
- 所以只要“把算术句翻译成集合论句”这个具体的语法函数可计算，𝗭𝗙𝗖 的算术影子就可枚举，Z0 就成立（`zfc_z0_of_translate_computable`）。
- 剩下的这条引理与 𝗭𝗙𝗖 的可证性无关；它的证明路线与工作量见 `CLAIM.md` §4。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| 20 个依赖模块（`ProcessObservation` 至 `ZFC/Z0PA.lean`） | 与 `../godel-q-zfc-z0-pa/` 逐字节相同 |
| `GodelQ/ZFC/ShRE.lean` | 定理集可枚举；`Sh.RE` 归结为翻译的可计算性；Z0 的新条件形式 |
| `GodelQ/ZFC/QualificationShRE.lean` | 命题对照 `qual_C111` |
| `GodelQ/Negative/WrongShREWithoutComputability.lean` | 负控制：不给可计算性 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-RE-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-RE-NEG-COMP-01 --rerun --expect-rejected
```

## 运行（2026-10-09）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261009-CG001-GODEL-Q-ZFC-Z0-RE-01` | `MP-CG001-GODEL-Q-ZFC-Z0-RE-001` | 接受 | 0（54 秒，stderr 0 B；97 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261009-CG001-GODEL-Q-ZFC-Z0-RE-NEG-COMP-01` | `MP-CG001-GODEL-Q-ZFC-Z0-RE-NEG-COMP-001` | 拒绝 | 1：`simp` 无进展 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261009-CG001-GODEL-Q-ZFC-Z0-RE-*.json`；索引：同目标 `证据索引.md` §30；共享矩阵末节。
