# z0-omega-question：Z0 作为具体的 ω 追问（CG001-C-427）

> CG-010（worktree `claude/012-opus-w8`）R9。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。精确命题、读法与禁止外推见 `CLAIM.md`。

## 这个包做了什么

研究发起人说过“Q0（H0（Z0））”：Z0 是 HoTT 那件事（H0）在 ZFC 里的对应物。此前，Z0 在 Lean 的图式里只是“某个过程”（C-93），在 Agda 里是参数（C-112、C-113）。本包把它写成 Lean 里一个具体的追问，第 k 问是“到第 k 步，找到 𝗭𝗙𝗖 的矛盾了吗”。

- **它永不落定**：𝗭𝗙𝗖 一致，所以永远找不到。这一点在元层成立，用的是 Lean 里的集合宇宙模型。
- **𝗭𝗙𝗖 每一刻都看得见**：对每个 k，𝗭𝗙𝗖 都证明“到第 k 步还没找到”。
- **𝗭𝗙𝗖 看不见“永不”**：Foundation 的一致性句在自然数里为真，恰好当这个追问永不落定；𝗭𝗙𝗖 证明不了这句话（C-417）。
- **与芝诺同一个类型、同一个图式**：完成的整体（“全部证明的集合”）推不出某一步完成；由它驱动的哥德尔–芝诺跑者到达。

和芝诺、H0 并排看：
- 芝诺：𝗭𝗙𝗖 证得出“没有哪一步到了”（C-423）；
- H0：HoTT 证得出“永远问不完”（C-78）；
- Z0：每一刻都看得见，“永不”却证不出。

## 文件（按编译次序）

- 32 个依赖模块，逐字节复制自 `../godel-q-zfc-z0-sigma1/GodelQ/`；`GodelQ/OmegaQuestion.lean`，逐字节复制自 `../godel-q/GodelQ/`。
- 新文件：

| 文件 | 内容 |
|---|---|
| `GodelQ/ZFC/Z0OmegaQuestion.lean` | Z0 的程序与 ω 追问；永不落定；每一刻的确认；一致性句的真；跑者到达 |
| `GodelQ/ZFC/QualificationZ0Omega.lean` | 命题对照 `qual_C427`（导入 C-417） |
| `GodelQ/Negative/WrongStagesMakeNever.lean` | 负控制：把每一刻的确认当作“永不”的证明 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,893 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261015-CG001-Z0-OMEGA-QUESTION-01 --rerun
```

负控制加 `--expect-rejected`，运行目录为 `20261015-CG001-Z0-OMEGA-QUESTION-NEG-STAGES-01`。

## 运行（2026-10-15）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261015-CG001-Z0-OMEGA-QUESTION-01` | `MP-CG001-Z0-OMEGA-QUESTION-001` | 接受 | 0（107 秒，stderr 0 B；150 条公理报告全为三条标准公理） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261015-CG001-Z0-OMEGA-QUESTION-NEG-STAGES-01` | `MP-CG001-Z0-OMEGA-QUESTION-NEG-001` | 拒绝 | 1：类型不符 | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

- 校验输出在 `.claude/goals/CG-001-targeted-overview/verification/` 下，与运行同名。
- 索引在同一目标的 `证据索引.md` §58（012-Opus）与共享矩阵末节。
- `CLAIM.md`、两份固定记录与源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
