# two-choices-cubical：两次选择进 HoTT 的内核；B 不靠 LPO（CG001-C-426）

> CG-010（worktree `claude/012-opus-w8`）R4。本机会话 95a1a81b（012-Opus），Opus 5.5，2026-10-15。精确命题、归因与禁止外推见 `CLAIM.md`。

## 这个包做了什么

研究发起人 2026-10-14 说：“放弃是一次选择，而A是第二次选择。”C-418 在 Lean 里证明，这两次选择在最简一层是同一条原则。本包把它搬进 HoTT 自己的内核（Cubical Agda，`--safe`，什么都不假定），并且放到 B（宇宙上的追问永远问不完，C-78）的旁边。结果如下：

- **两次选择在 HoTT 的内核里也是同一条原则**：`LimBit ↔ LPO`，用的是与“同一个 Q”包相同的 ω 追问类型。
- **B 不靠 LPO**：
  - 这个检查单元没有假定 LPO，宇宙上的追问照样永远不停；
  - 它的回答流每一阶段都是“否”，这是证出来的，不是从 LPO 得到的。
  
  所以 B 不是“放弃 ASK”在真假值上的后果，也不是“看不出停不停”：HoTT 证得出它永远不停。
- **B 只出现在所有层的汇集上**：
  - 全部集合的汇集在第 2 阶段答完，全部 4 型的汇集在第 4 阶段答完；
  - 一般地，(m+1) 型的汇集恰在第 m+1 阶段答完；
  - 永远答不完的，只有把所有层汇在一起的宇宙。这是芝诺的形状搬到了宇宙上。
- **归因**：
  - B 要单价性（没有它，第 1 阶段就停，C-80、C-83）；
  - 也要“所有层的汇集”（只取有限的一层，就在那一层停）；
  - 不要 LPO。
  
  “宇宙作为现成的整体交出来，是宇宙层的 A”是读法，待研究发起人确认。

## 文件

| 文件 | 内容 |
|---|---|
| `TwoChoicesCubical.agda` | `LimBit ↔ LPO`；单调不可去；宇宙的回答流；有限层恰在自己那一层答完；内核实跑；命题对照 `qual-C426` |
| `WrongUniverseSettles.agda` | 负控制：宇宙的回答流第 1 阶段读作“是” |
| `WrongSetsGatheringEarly.agda` | 负控制：集合的汇集第 1 阶段就答完 |
| `WrongAltSettles.agda` | 负控制：不要求单调也会落定 |

依赖导入：`../same-q-univalent/`、`../questioning-delay/`、`../universe-questioning/`、`../pedometer-semantics/`、`../truncation-questioning/`、`../product-questioning/`。

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261015-CG001-TWO-CHOICES-CUBICAL-01 --rerun
```

负控制加 `--expect-rejected`，运行目录换成 `-NEG-01`、`-NEG-02`、`-NEG-03`。

## 运行（2026-10-15，macOS）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261015-CG001-TWO-CHOICES-CUBICAL-01` | `MP-CG001-TWO-CHOICES-CUBICAL-001` | 接受 | 0（88 秒，stderr 0 B） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261015-CG001-TWO-CHOICES-CUBICAL-NEG-01` | `…-NEG-001` | 拒绝 | 42：`false != true` | KERNEL_REJECTED | 精确重放 |
| `20261015-CG001-TWO-CHOICES-CUBICAL-NEG-02` | `…-NEG-002` | 拒绝 | 42：`nothing != just 1` | KERNEL_REJECTED | 精确重放 |
| `20261015-CG001-TWO-CHOICES-CUBICAL-NEG-03` | `…-NEG-003` | 拒绝 | 42：`false != true` | KERNEL_REJECTED | 精确重放 |

- 校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261015-CG001-TWO-CHOICES-CUBICAL-*.json`。
- 索引：同一目标的 `证据索引.md` §57（012-Opus）与共享矩阵末节。
- 同名运行的第一次捕获在入库前作废，原因见 `CLAIM.md` §8。
- `CLAIM.md` 与被导入的源文件进入了收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
