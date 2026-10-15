# two-choices-lpo：两次选择是同一条原则（CG001-C-418 至 C-421）

> CG-007（`.claude/goals/CG-007-formalization-completion/`），W8 之后的单元。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-14；独立 worktree `claude/012-opus-w8`。精确命题、读法、文献与禁止外推见 `CLAIM.md`。

## 这个包做了什么

研究发起人 2026-10-14 说：“放弃是一次选择，而A是第二次选择。A是什么？A就是一个无限的步骤才能到达，从而存在的结果，当作已经存在的结果，参与运算。”（全文见 `.claude/思考与发现/CN-078`）

- **两次选择是同一条原则（C-418）**。
  - “放弃 ASK”落在真假值上，最简单的形态是 LPO：每个无限搜索停不停，已经定了。
  - “A”落在对象上，最简单的形态是：单调序列的终值现成可用。
  - 在不预设排中律的底座上，两者互推。包内的公理审计机器断言：这些证明不用 `Classical.choice`。
- **芝诺的极限用不着 A（C-419）**。芝诺过程在每个精度上的读数，落定的那一步由公式给出，不靠搜索。
- **A 的结果，机器交不出（C-420）**。每个停机搜索的终值，在经典逻辑里都“存在”，可是没有可计算的方法交出它。
- **辨别力不是没有，只是不当门槛用（C-421）**。经典逻辑对“会停”和“永不停”一视同仁，同一个理论又证得出二者可计算性的差别。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| `GodelQ/ProcessObservation.lean` | 过程、完成、阶段观察（逐字节复制自 `godel-q-zfc-turing`） |
| `GodelQ/TwoChoices/Core.lean` | LPO、A 的两种形态与互推；芝诺读数（只用 Lean 内核） |
| `GodelQ/TwoChoices/Machines.lean` | 停机搜索的开关；交不出落定的一步与终值；经典的 LPO 与二值性 |
| `GodelQ/TwoChoices/Rational.lean` | 芝诺的有理数一侧，以及与整数读数的对应（经典） |
| `GodelQ/TwoChoices/QualificationTC.lean` | 命题对照 `qual_C418`–`qual_C421` 与公理审计 |
| `GodelQ/Negative/WrongLPOForFree.lean` | 负控制：借排中律“免费”得到 LPO，被审计拒绝 |
| `GodelQ/Negative/WrongSettlingUnbounded.lean` | 负控制：去掉“有界”仍要落定 |
| `GodelQ/Negative/WrongComputableSettling.lean` | 负控制：一律回答“第 0 步”的落定机器 |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,250 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261014-CG001-TWO-CHOICES-LPO-01 --rerun
```

负控制加 `--expect-rejected`，运行目录换成 `-NEG-FREE-01`、`-NEG-UNBOUNDED-01`、`-NEG-SETTLING-01`。

## 运行（2026-10-14）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261014-CG001-TWO-CHOICES-LPO-01` | `MP-CG001-TWO-CHOICES-LPO-001` | 接受 | 0（8 秒，stderr 0 B；40 条公理报告；审计 12 条“不依赖”、5 条对照“依赖”全部通过） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261014-CG001-TWO-CHOICES-LPO-NEG-FREE-01` | `MP-CG001-TWO-CHOICES-LPO-NEG-001` | 拒绝 | 1：审计报出 `lpo_for_free` 依赖 `Classical.choice` | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |
| `20261014-CG001-TWO-CHOICES-LPO-NEG-UNBOUNDED-01` | `MP-CG001-TWO-CHOICES-LPO-NEG-002` | 拒绝 | 1：`omega` 证不出上界 | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |
| `20261014-CG001-TWO-CHOICES-LPO-NEG-SETTLING-01` | `MP-CG001-TWO-CHOICES-LPO-NEG-003` | 拒绝 | 1：`DoneBy e m ↔ DoneBy e 0` 未解 | KERNEL_REJECTED | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出在 `.claude/goals/CG-001-targeted-overview/verification/` 下，与运行同名；索引在同一目标的 `证据索引.md` §52（012-Opus）与共享矩阵末节。`CLAIM.md`、两份固定记录与源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
