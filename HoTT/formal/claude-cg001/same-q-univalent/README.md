# same-q-univalent：同一个 ω 追问，在一个有单价性的内核里（CG001-C-112、C-113）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W6，本机会话 d58e0c0d，Opus 5.5，2026-10-09。精确命题与禁止外推见 `CLAIM.md`。

## 这个包做了什么

C-93 把芝诺、H0、Z0 放进同一个 ω 追问图式时，H0 在 Lean 里只能是参数，因为 H0 的“永不停”要靠单价性。本包在 Cubical Agda 这一个有单价性的内核里写出：

- 一个共同的类型（逐阶段的回答流）、一个共同的程序（找到即停的搜索）、一个共同的跑者（未落定就减半）；
- 共同的定理：永不落定 ⟺ 搜索永远跑下去 ⟺ 跑者到达（单调时；单调前提不可去）；“完成的整体 ⟹ 有限阶段完成”被否定；C-77 的判定器追问恰是这个搜索；
- 四个实例：
  - 芝诺；
  - 单价宇宙上的 H0：原生，经 C-78，内核实跑燃料 100 得 `nothing`；
  - 截断宇宙：第 1 阶段就停，跑者不动；
  - Z0：以参数接入。

## 文件

| 文件 | 内容 |
|---|---|
| `SameQ.agda` | 图式、跑者、判定器追问即搜索、四个实例、命题对照 `qual-C112`、`qual-C113` |
| `WrongH0Settles.agda` | 负控制：单价宇宙上第 1 阶段就有输出 |
| `WrongTruncUnsettled.agda` | 负控制：截断宇宙第 1 阶段未落定 |
| `WrongRunnerWithoutMonotone.agda` | 负控制：去掉单调前提 |

依赖导入：`../pedometer-semantics/`、`../questioning-delay/`、`../truncation-questioning/`、`../product-questioning/`、`../universe-questioning/`。

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-SAME-Q-UNIVALENT-01 --rerun
```

负控制同法，加 `--expect-rejected`，运行名 `20261009-CG001-SAME-Q-UNIVALENT-NEG-01` 至 `-NEG-03`。

## 运行（2026-10-09，macOS）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261009-CG001-SAME-Q-UNIVALENT-01` | `MP-CG001-SAME-Q-UNIVALENT-001` | 接受 | 0（92 秒） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261009-CG001-SAME-Q-UNIVALENT-NEG-01` | `…-NEG-001` | 拒绝 | 42：`nothing != just 1` | KERNEL_REJECTED | 精确重放 |
| `20261009-CG001-SAME-Q-UNIVALENT-NEG-02` | `…-NEG-002` | 拒绝 | 42：`true != false` | KERNEL_REJECTED | 精确重放 |
| `20261009-CG001-SAME-Q-UNIVALENT-NEG-03` | `…-NEG-003` | 拒绝 | 42：`alt k != not (alt k)` | KERNEL_REJECTED | 精确重放 |

校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261009-CG001-SAME-Q-UNIVALENT-*.json`；索引：同目标 `证据索引.md` §31；共享矩阵末节。`CLAIM.md` 与被导入的源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
