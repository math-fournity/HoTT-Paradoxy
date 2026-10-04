# G2 控制：Foundation 中 ZFC 接口与通用哥德尔定理之间的直接映射缺口

> **方案：** `GODEL-Q-REFLECTION-SOP`。
>
> **阶段身份：** `G0/G2_TARGET_MAPPING_CONTROL`；它检验一个已有的通用哥德尔技术基线能否直接实例化到冻结来源中的 ZFC 对象，不释放 G2、G3 或 parent-Q 链。
>
> **判词：** `FOUNDATION_ZFC_INTERFACE_PRESENT / GENERIC_GODEL_INTERFACE_PRESENT / DIRECT_ARITHMETIC_THEORY_INSTANTIATION_REJECTED_WITH_SCOPE`。

## 1. 为什么要做这个控制

此前已在同一冻结的 Foundation 源树中重放了通用第一、第二不完备性接口。仅凭“ZFC 模块”和“哥德尔模块”同在一个仓库，不能把 generic theorem 的 `T : ArithmeticTheory` 自动读成 `T = ZFC`。

这里固定两个最小 wrapper：

- 正控制只检查 Foundation 确实暴露了 `ZermeloFraenkelChoice : SetTheory`、一个 Lean 元层的 `zfc_consistent`，以及通用 `ArithmeticTheory` 的两个 theorem interface；
- 负控制直接尝试 `Arithmetic.incomplete ZermeloFraenkelChoice`，要求 Lean 给出类型拒绝。

这不是尝试“让 Lean 证明 ZFC 失败”。它在检查 target-specific 哥德尔化开始前最容易被偷换的一步：理论对象的类型是否已经真的接上。

## 2. 冻结的来源、命令与结果

来源为 `FormalizedFormalLogic/Foundation@f3972f4204fc61e1b736ed843415894c83f35508`，工具链为 Lean 4.34.0。外部 source worktree 中有一个既有、未跟踪的 `GodelBaseline.lean`；本工作既未读取它作证据，也未改动它。

先构建精确的 `Foundation.FirstOrder.SetTheory.Universe` target；随后运行项目中的两个 wrapper。完整命令、环境、哈希、正控制输出和负控制诊断都保存在 [run receipt](../HoTT/verification/runs/20261004-SOURCE-REPLAY-FOUNDATION-ZFC-GODEL-GAP-001/RUN.json)。

| 控制 | 结果 | 实际说明 |
|---|---|---|
| `FoundationZFCGodelGap.lean` | exit `0` | `𝗭𝗙𝗖` 的类型是 `SetTheory`；`zfc_consistent` 是 Lean 元层的 `Entailment.Consistent 𝗭𝗙𝗖`；通用哥德尔定理要求 `ArithmeticTheory` 和额外层级／soundness 或 consistency 假设。 |
| `WrongFoundationZFCGodelInstantiation.lean` | exit `1`，预期拒绝 | Lean 报告：`𝗭𝗙𝗖 : SetTheory`，但 `Arithmetic.incomplete` 此处需要 `ArithmeticTheory`。 |

正控制打印的 `zfc_consistent` 依赖是 `propext`、`Classical.choice`、`Quot.sound`。因此它不能被重新表述为 ZFC 内部的一致性证明。

## 3. 机器结果精确支持什么

下面的说法已经由这个固定 source 与运行支持：

```text
Foundation 中存在一个 ZFC SetTheory interface。
Foundation 中存在带显式 ArithmeticTheory 假设的通用哥德尔不完备性 interface。
把前者直接作为后者的 T，Lean 在类型层拒绝。
```

它由此阻止如下偷换：

```text
同一源树中有 ZFC 模块和哥德尔 theorem
⇒ 已经得到了 ZFC 的不完备性实例
```

真正的 target-specific G2 若要继续，必须另行构造并核验一种实际解释、reduct、embedding 或 arithmetization，并逐项证明它满足所选 theorem 的 `ArithmeticTheory`、可枚举性、算术强度与 soundness／consistency前提。它还必须与 G0 的实际 `Accept_T` 对齐，不能只在宿主 Lean 中另造一个同名对象。

### 3.1 源树中已有的两种不同能力

为确认这个类型拒绝不是把“ZFC 中不能表达递归”偷换回来，我又在**同一固定 source tree**做了两项窄扫描，全文结果保存在 [source-scan](../HoTT/verification/runs/20261004-SOURCE-REPLAY-FOUNDATION-ZFC-GODEL-GAP-001/source-scan.txt)。

1. `Foundation.FirstOrder.SetTheory.Z.Z` 和 `NaturalNumberRec` 在一个满足集合论接口的模型中定义 `ω`、后继闭包、自然数归纳、`Blueprint.CSeq`、唯一递归结果与可定义性。这是模型层的自然数过程表示与递归正控制。
2. `Foundation.FirstOrder.LK.Interpretation` 定义了通用的 `DirectInterpretation`／`InterpretedBy` 抽象；但对整个固定 source tree 搜索时，所有命中都在该抽象自身的定义与通用组合处，未找到 ZFC 到 `ArithmeticTheory` 的具体实例。

因此这个 source 的当前图景是：**过程／递归模型能力存在，理论到理论的实际算术解释仍未在该 source tree 中给出。**这正好避免两种相反误读：不能从类型拒绝说“ZFC 不能表示自然数过程”，也不能从模型递归说“ZFC 已经被该 generic Gödel theorem 实例化”。

## 4. 这个控制没有说什么

- 它没有证明 bare ZFC 不一致、不完备，或在时间维度上缺少观察力；
- 它没有证明数学上不存在从 ZFC 到算术元理论的编码或解释；
- 它没有把 exact source tree 中没有 concrete `DirectInterpretation` instance 的扫描结果外推到所有版本、所有文献或数学本身；
- 它没有把 `zfc_consistent` 说成 ZFC 在对象语言内部证明自身一致性；
- 它没有定义 `OriginDone`、现实映射 `ρ`、completion bridge、实际 Q policy，或把哥德尔句运输到芝诺、圆环、fixed HoTT H0；
- 它没有改变 `GODEL-Q-REFLECTION-SOP` 的 G1–G6 gate，也不重开 F-050。

## 5. 对当前路线的作用

这是一条有用的“阻断性正果”：它把原先笼统的“尚未映射”收紧成一个可复现的接口事实。Foundation 的 generic theorem 仍可作为技术参照，但不再允许以同源共存为理由跳过 target mapping。

所以 G0 的主要结论不变：真实 proof acceptance interface 已冻结，而 parent completion acceptance interface 仍未在同一 source 中得到。G1–G6 继续停在 `NOT_RELEASED`；本控制属于 `G2_TARGET_MAPPING_GUARD`，不是 G2 的完成。

## 6. 复现

```bash
toolchain=/Users/aurolafly/.elan/toolchains/leanprover--lean4---v4.34.0/bin
source_root=/private/tmp/foundation-zfc-f3972f4204fc
"$toolchain/lake" --dir "$source_root" build Foundation.FirstOrder.SetTheory.Universe
"$toolchain/lake" --dir "$source_root" env "$toolchain/lean" HoTT/formal/godel-q-reflection/FoundationZFCGodelGap.lean
"$toolchain/lake" --dir "$source_root" env "$toolchain/lean" HoTT/formal/godel-q-reflection/WrongFoundationZFCGodelInstantiation.lean
```

最后一个命令应以类型不匹配退出；这只是在这个 exact direct application 上的期望负控制。
