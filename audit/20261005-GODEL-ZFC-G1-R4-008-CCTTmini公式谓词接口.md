# GZ-010：CCTTmini₀ formula / proof-predicate interface

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G1-R4`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / GZ-011_SUCCESSOR_REQUIRED`。

## 1. Parent gap

GZ-009 已经能把 finite `RawCert` 变成可解码的自然数，但 Gödel技术不是“有一个 code”就完成；
还需要区分对象公式里**说**的 `Prov(n)` 与元层里**验证**的 certificate。当前单位先建立两者的
有限接口，而不声称有算术表示性。

## 2. 冻结对象与层级

```text
Formula            ::= provF Nat | atomF Nat | Formula ⇒ Formula | ⊥
validCode n        := accepts [] (decode n)         -- meta-level Bool
ProvWitness n      := ∃ raw certificate c,
                      code c = n ∧ Checked [] c     -- meta-level evidence
quoteCert c        := provF (code c)                -- formula syntax
```

`Formula` 是可编码对象；`validCode` 与 `ProvWitness` 不自动成为 formula 内部可表示 predicate。
这是本单位最关键的边界。其正控制须构造一个 closed certificate `reflC zeroC` 的 witness；其负控制
须拒绝把该 `provF` 公式当作 `⊥` 或任意不同公式。

## 3. Machine targets

1. `closedAccepted`：closed certificate 的 checker acceptance；
2. `closedProvWitness`：其 Nat code 有 actual `ProvWitness`；
3. `quoteClosed`：formula syntactically引用该 Nat code；
4. `quoteClosedHolds`：formula semantics 的 `provF` clause由同一 witness 支付；
5. `wrongQuoteAsBottom`：主张同一 quoted formula 等于 `⊥` 的负控制必须被 kernel 拒绝。

本单位结束后 successor 必须是 formula coding / substitution / self-code instance；不得把它直接叫作
diagonal fixed point、representability 或 incompleteness theorem。

## 4. 实际 kernel 结果

`CCTTminiFormula.agda` 将 `Formula`、`provF`、`validCode`、`ProvWitness`、`quoteCert` 和只对
`provF` 开放的 `ProvHolds` 分开。主 run
[`20261005-MP-CUBICAL-GODEL-FORMULA-PREDICATE-001-01`](../HoTT/verification/runs/20261005-MP-CUBICAL-GODEL-FORMULA-PREDICATE-001-01/RUN.json)
以 exit 0 接受：

```text
C-379  validCode (code closedC) = true
C-380  closedProvWitness : ProvWitness (code closedC)
C-381  quoteCert closedC = provF (code closedC)
C-382  ProvHolds (quoteCert closedC)
```

negative source `WrongCCTTminiFormula.agda` 要求 `quoteCert closedC ≡ botF`，在
`provF (code closedC) != botF` 处以 exit 42 被拒绝。该 run 继承 GZ-009 的
`UnsupportedIndexedMatch` warning；其含义仍严格限于 `CCTTminiNat.≤-trans` 在 general
transport 下的计算，不影响这些 fixed formula declarations 的 kernel acceptance，也不被隐藏。

## 5. 局部判词

```text
FORMULA_SYNTAX_AND_META_CERTIFICATE_INTERFACE_MACHINE_PROVED_WITH_SCOPE
META_OBJECT_BOUNDARY_PRESERVED
ARITHMETIC_REPRESENTABILITY_AND_FIXED_POINT_UNPAID
```

## 6. Required successor

`GZ-011 / R4-CCTTMINI-FORMULA-NAT-CODE-SUBSTITUTION-001`：定义 formula 的 total Nat coding/decoder、
formula variables 的 capture-free numeral substitution，以及 `quoteFormula`/self-code instance。它必须让
`provF` 接收的 numeral来自 formula 自己的 code，同时保留“这只是 syntax-level diagonal shape、不是
representability/fixed-point theorem”的边界。
