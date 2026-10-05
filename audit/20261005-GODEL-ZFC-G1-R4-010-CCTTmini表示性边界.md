# GZ-012：CCTTmini₀ 的对象／元层可表示性边界

> **身份：** `ROUTE_UNIT_RECORD / G1-R4 / SOURCE_AND_KERNEL_BOUNDARY`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / S_M4M5_SUCCESSOR_REQUIRED`。

## 固定 target、构造与反证条件

冻结两个已 kernel-checked 的 project fragments：`CCTTminiFormulaCode.Formula₁` 的
`prov₁ : Expr₁ → Formula₁`，以及 `CCTTminiFormula.ProvWitness : Nat → Set`。检验问题不是“能否
给二者临时写一个同名 predicate”，而是 source 是否已给出 object-level arithmetic representation：

```text
Provₒ(n) : Formula₁
object semantics for Provₒ(lit n)
↔ meta-level ProvWitness n
```

自己的反证构造是：若存在这种 payment，至少必须提供共同的 formula-code domain、从 `prov₁` 到
`provF` 或反向的 translation，以及对所有相关 `n` 的 theorem；只对 `closedC` 的一个 witness 或
syntax self-substitution 都不足以支付它。发现上述 translation/theorem 时，本卡撤回。

## 实际源码与运行证据

- `CCTTminiFormulaCode` 只有 `Expr₁ ::= lit | fvar` 与 `Formula₁ ::= prov₁ | bot₁`；它给出 formula
  code/decoder 和 `prov₁(fvar 0)` 的 self-code substitution shape（C-383–C-386）。
- `CCTTminiFormula` 的 `ProvWitness n` 由 `RawCert`、`code c ≡ n` 和 `Checked [] c` 在 Agda 元层构造；
  `ProvHolds` 仅为 `provF n` 给 partial clause（C-379–C-382）。
- 两个 module 没有相互 import，没有 `Formula₁ → Formula` translation、没有共同 code theorem，亦没有
  算术 theory、derivation enumeration、representability或 fixed-point equivalence。现有 run 的明确 non-goal
  也排除了 object-arithmetic representability。

## 判词、控制与后继

```text
META_OBJECT_REPRESENTABILITY_UNPAID_WITH_SCOPE
SYNTAX_LEVEL_DIAGONAL_SHAPE_ONLY
NO_SOURCE_PAID_HOTT_PROOF_PREDICATE
```

正控制是两个模块各自在其范围内实际通过 Cubical Agda kernel；DifferentTask control 是 `closedC` 的
单个 certificate witness 不等于对全部 formula codes 的 representability theorem。此结果不证明
representability 不可能，更不涉及 full cctt/redtt/HoTT 或 bare ZFC。

后继为 `S-001 / SameFullQ-and-attribution-reconciliation`：将 D-001、A-001、H-001、GZ-012 的
actual/task bridges 放在同一支付表中，检查是否已有可进入 M4/M5 的真实 SameFullQ；若没有，形成
有界拒绝而不宣称总路线结束。新 exact calculus 的 object-level representation theorem 会重开 GZ-012。
