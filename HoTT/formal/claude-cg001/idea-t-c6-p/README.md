# idea-t-c6-p：想法 T 的两种形式；C6 审查力（AI 提案）；P 的两侧（CG001-C-114、C-115、C-116）

> CG-007（`.claude/goals/CG-007-formalization-completion/`）单元 W7，本机会话 d58e0c0d，Opus 5.5，2026-10-09。精确命题与禁止外推见 `CLAIM.md`。

## 这个包做了什么

三件事，各承接研究发起人的一段话：

1. **想法 T**（KC-000074）：“不完备，就是低精度理论的精度低，表现形式：维度缺失，或者维度不缺失，但是理论在某个维度上的观察力不完备。”
   - 一个观察者经接口看对象，去确认一个“维度”（一族事实）。它确认不全，恰有两个原因：接口把这一维的差别压平了（形式一），或者这一维的真假本身不可枚举（形式二）。二者可以分开检查（脚手架），也确实不是一回事。
   - 芝诺：只看极限值的接口，判不了“是否在有限阶段取到”（形式一）。𝗭𝗙𝗖：它证明的“永不停机”漏掉的过程，无穷且列不全（形式二）。
2. **元理论的审查**（KC-000065）：“Meta Theory应该能够检验Sub Theory的边界……它对于Sub Theory的错误，无法产生批判力”。
   - 审查定义成：对每个芝诺式跑者，证明标准解（极限意义的到达）在它上面“充分”或“不充分”。这是 AI 的提案。
   - 任何有效的审查都不完备。对 𝗭𝗙𝗖：标准解确实出错（极限说到了，原过程永远没到），𝗭𝗙𝗖 却证明不了它出错的跑者有无穷多个，列不全；不论用哪个公式写“出错”，都是如此。
3. **P 的两侧**（KC-000068）：P“本质上是反现实的，是不可计算的”；“ZFC-1=ZFC+A，则ZFC-1=ZFC+P”。
   - 反现实：统一地把形式完成说成原完成，一个稠密实例就否定了它。
   - 不可计算：对整族跑者统一接受形式完成，接受集就不可枚举。
   - 不要求有效性的跑者理论上，A（把 P₁ 当接受规则）恰是 ω 完成规则 P。

## 文件（按编译次序）

| 文件 | 内容 |
|---|---|
| 20 个依赖模块 | 逐字节复制：18 个自 `godel-q-zfc-turing`，2 个自 `zeno-density-attainment` |
| `GodelQ/IdeaT.lean` | 想法 T：形式一、形式二、脚手架、两种形式不同；𝗭𝗙𝗖 与芝诺实例 |
| `GodelQ/C6Review.lean` | C6（AI 提案）：`Review`、有效审查不完备、𝗭𝗙𝗖 的审查缺口、任一公式下的批判力缺口 |
| `GodelQ/PTwoSides.lean` | P 的两侧：抽象层、实数轴与格点、跑者族、`LooseRunnerTheory` 上 A ⟺ P、两侧合一 |
| `GodelQ/QualificationW7.lean` | 命题对照 `qual_C114`、`qual_C115`、`qual_C116`；依赖检查（哪些证明不经对角点） |
| `GodelQ/Negative/WrongLimitDecoder.lean` | 负控制：极限接口上的“取到”判据 |
| `GodelQ/Negative/WrongCompleteReview.lean` | 负控制：照真值裁决的审查冒充有效审查 |
| `GodelQ/Negative/WrongRealP1.lean` | 负控制：借格点定理证稠密实数轴上的语义 P₁ |
| `LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json` | 固定的 Lean 文件与导入闭包（1,889 个模块）的逐模块哈希 |

## 复现

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-IDEA-T-C6-P-01 --rerun
```

```bash
python3 -B .claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --run-dir HoTT/verification/runs/20261009-CG001-IDEA-T-C6-P-NEG-01 --rerun --expect-rejected
```

另两个负控制把 `NEG-01` 换成 `NEG-02`、`NEG-03`。

## 运行（2026-10-09）

| run | proof | 预期 | 退出 | 结果 | 重放 |
|---|---|---|---|---|---|
| `20261009-CG001-IDEA-T-C6-P-01` | `MP-CG001-IDEA-T-C6-P-001` | 接受 | 0（80 秒，stderr 0 B；144 条 `#print axioms` 全为 propext、Classical.choice、Quot.sound，其中 3 条不依赖任何公理；依赖检查通过） | KERNEL_ACCEPTED_WITH_SCOPE | PASS_WITH_SCOPE，EXACT_EXIT_STDOUT_STDERR_MATCH |
| `20261009-CG001-IDEA-T-C6-P-NEG-01` | `MP-CG001-IDEA-T-C6-P-NEG-001` | 拒绝 | 1：目标 `∃ n, s n = limUnder atTop s` 未解 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |
| `20261009-CG001-IDEA-T-C6-P-NEG-02` | `MP-CG001-IDEA-T-C6-P-NEG-002` | 拒绝 | 1：`re_inadequate` 处 `simp` 无进展 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |
| `20261009-CG001-IDEA-T-C6-P-NEG-03` | `MP-CG001-IDEA-T-C6-P-NEG-003` | 拒绝 | 1：目标 `∃ k, s n = ↑k` 未解 | KERNEL_REJECTED（细化阶段） | NEGATIVE_CONTROL_REJECTED_AS_EXPECTED，精确重放 |

校验输出：`.claude/goals/CG-001-targeted-overview/verification/20261009-CG001-IDEA-T-C6-P-*.json`。索引：同目标的 `证据索引.md` §32，以及共享矩阵末节。`CLAIM.md`、两份固定记录与三个工具已进入收据的源清单哈希，此后不得改动；更正写进 `REVISIONS.md`。
