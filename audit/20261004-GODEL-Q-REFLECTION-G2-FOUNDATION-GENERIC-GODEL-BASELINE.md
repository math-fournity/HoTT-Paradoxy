# G2：Foundation 通用哥德尔技术基线的精确 source replay

> **方案：** `GODEL-Q-REFLECTION-SOP`。
>
> **身份：** `SOURCE_REPLAYED_WITH_SCOPE / GENERIC_GODEL_TECHNICAL_BASELINE / NOT_A_BARE_ZFC_INSTANTIATION`。

> **判词：** `GENERIC_CODE_QUOTE_SUBSTITUTION_PROVABILITY_AND_INCOMPLETENESS_MACHINE_REPLAYED_WITH_EXPLICIT_ASSUMPTIONS`。

## 1. 已重放的 exact source

在冻结的 `FormalizedFormalLogic/Foundation@f3972f4204fc61e1b736ed843415894c83f35508` 和 exact Lean 4.34.0 dependency closure 下，以下文件均实际退出码 `0`：

1. `Foundation/FirstOrder/Incompleteness/First.lean`；
2. `Foundation/FirstOrder/Incompleteness/Second.lean`；
3. 本项目最小 wrapper `HoTT/formal/godel-q-reflection/FoundationGodelBaseline.lean`。

完整命令、环境、source manifest 和 wrapper 输出见 [run receipt](../HoTT/verification/runs/20261004-SOURCE-REPLAY-FOUNDATION-GODEL-001/RUN.json)。

## 2. 机器实际检查的哥德尔结构

`First.lean` 的通用定理是：

```text
incomplete (T : ArithmeticTheory)
  [T.Δ₁] [R₀ ⪯ T] [T.SoundOnHierarchy Σ 1] : Incomplete T
```

其 source body 实际使用：一个递归可枚举 predicate `D`、`codeOfREPred D`、formula quote `⌜δ⌝`、substitution 和对角句 `π = δ/[⌜δ⌝]`，再导出 `T ⊢ π ↔ T ⊢ ¬π` 的矛盾结构。

`Second.lean` 的通用定理是：

```text
consistent_unprovable (T : ArithmeticTheory)
  [T.Δ₁] [IΣ₁ ⪯ T] [Consistent T] : T ⊬ T.consistent.val
```

它通过 `T.standardProvability`、derivability conditions 和 consistency predicate 给出第二不完备性接口。wrapper 的 `#print axioms` 显示这两条已检查 theorem 只报告 Lean 的 `propext`、`Classical.choice`、`Quot.sound`。

## 3. 这对当前 GODEL-Q 路线意味着什么

这次 replay 给出了用户所说“神似地借鉴哥德尔”所需的**可执行技术骨架**，并且不是只用自然语言比喻：

| 哥德尔步骤 | Foundation 已实际重放的机制 | 当前 G0 仍需要的 target-specific 支付 |
|---|---|---|
| 语法／可证明性 | ArithmeticTheory、standard provability、`T ⊢`。 | 将 `set.mm` 或另一个 actual ZFC-facing interface 匹配到该 exact theory class。 |
| 编码／引用 | RE predicate、`codeOfREPred`、quote。 | 目标 `Accept_T` 的 code domain 与 T 内 representability。 |
| substitution／对角化 | formula substitution、`δ/[⌜δ⌝]`。 | 目标 consumer 的 quote/substitute/fixed point，而不是同名外部函数。 |
| 不完备性／反射 | First/Second theorem。 | parent `OriginDone`、`ρ`、completion bridge 与 actual source policy。 |

因此这个 run 使“哥德尔技术本身是否能被精确形式化”从猜测变为已重放的通用基线；但它**不能**把当前 target 写成 `T = bare ZFC`，因为本卡没有证明 ZFC 满足 source theorem 的 `ArithmeticTheory`、`Δ₁`、`R₀`/`IΣ₁`、soundness 或 consistency hypotheses。

### 3.1 同一 Foundation source 内的 target-mapping 检查

为避免把同一仓库中的相邻模块误当作已连接接口，本轮在冻结 source 的 `Foundation/FirstOrder/SetTheory` 子树上检索了：

```text
ArithmeticTheory | standardProvability | codeOfREPred | provabilityPred
```

结果为零个命中文件。这个结果只支持下述有界判断：**该 exact SetTheory source slice 没有显式暴露一条从其 Zermelo/SetTheory interface 到已重放 ArithmeticTheory provability hierarchy 的直接源码映射。**它不证明全库、未来版本或数学上不存在这种映射，也不证明 ZFC 无法满足哥德尔定理的标准前提。

它与 C-366 的角色正好相符：C-366 支持 set-theoretic process representation，不支付 arithmetic provability / quote / fixed-point interface。

更不能把通用 arithmetic provability sentence 解释为芝诺、圆环或 fixed H0 的 completion task。`OriginDone`、reality map `ρ` 与 bridge 仍是 G0 的实际缺口。

## 4. 结论与下一动作

```text
FOUNDATION_GENERIC_GODEL_BASELINE = MACHINE_REPLAYED_WITH_SCOPE
SETMM_OR_BARE_ZFC_INSTANTIATION = NOT_PAID
PARENT_COMPLETION_BRIDGE = NOT_PAID
```

下一动作不应重复一份 generic Gödel theorem。它必须回到 G0 的 source gap：找到同一版本固定 source，将一个 ZFC-facing formal acceptance interface、明确 process `OriginDone` 和 bridge/task switch 置于同一消费合同内。只有那时，Foundation 的通用骨架才可能被合法地用于 target-specific G2/G3。
