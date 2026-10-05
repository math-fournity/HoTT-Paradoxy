# GZ-011：CCTTmini₀ formula coding、numeral substitution 与 self-code instance

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G1-R4`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / GZ-012_SUCCESSOR_REQUIRED`。

## 1. Parent gap

GZ-010 有 `provF Nat` syntax 和 meta-level `ProvWitness`，但 formula 自身没有 Nat coding，也没有
变量替换。为了接近对角化，需要先把“公式谈论自己的 code”做成可检查的 syntax fact；这一步仍不能被称为
representability 或 fixed point。

## 2. 冻结最小 formula calculus `Fmini`

```text
Expr₁    ::= lit Nat | fvar Nat
Formula₁ ::= prov₁ Expr₁ | ⊥₁

codeE / decodeE
codeF / decodeF
substNum k x : Formula₁ → Formula₁
quoteFormula φ := lit (codeF φ)
selfInstance φ := substNum (codeF φ) 0 φ
```

`Fmini` 是 GZ-010 Formula 的**新、显式受限 successor**：`prov₁` 的表面角色对应 `provF`，但它不与旧
Formula 同名，也不把旧 `ProvWitness` 作为 constructor。它没有 binder，因此 numeral substitution 天然无捕获；
这一点必须写为范围限制，不能被外推为含量词的替换定理。

## 3. 冻结 machine targets

1. `decodeExprCode` 与 `decodeFormulaCode`：编码像上的 roundtrip；
2. `formulaCodeInjective`：formula code injection；
3. `selfInstanceShape`：`prov₁(fvar 0)` 代入它自己的 formula code 后成为 `prov₁(lit(codeF template))`；
4. `selfInstanceQuotesFormula`：同一式等于引用函数的 syntax；
5. negative control：self instance 不能被伪造为 `⊥₁`。

后继 `GZ-012` 才能问：给定 `ProvWitness` / `validCode`，是否有一个明确、非循环的 object arithmetic
representation theorem把它连接到 `prov₁`；若没有，只能保留 `META_OBJECT_REPRESENTABILITY_UNPAID`。

## 4. 实际 kernel 结果

主 run
[`20261005-MP-CUBICAL-GODEL-FORMULA-CODING-001-01`](../HoTT/verification/runs/20261005-MP-CUBICAL-GODEL-FORMULA-CODING-001-01/RUN.json)
以 exit 0 machine-check：`decodeExprCode`、`decodeFormulaCode`、`formulaCodeInjective`、
`selfInstanceShape` 与 `selfInstanceQuotesFormula`。公式模板是
`template = prov₁ (fvar 0)`，因此其 self instance 精确变成
`prov₁ (lit (codeFormula template))`。

negative `WrongCCTTminiFormulaCode.agda` 声称该 self instance 等于 `bot₁`，在
`... != bot₁` 处以 exit 42 被拒绝。GZ-009 的 `UnsupportedIndexedMatch` warning 经 `CCTTminiNat`
依赖继承并保留；GZ-011 没有新增 warning。

## 5. 局部判词

```text
FMINI_FORMULA_CODE_AND_SELF_SUBSTITUTION_MACHINE_PROVED_WITH_SCOPE
SYNTAX_LEVEL_DIAGONAL_SHAPE_NOT_FIXED_POINT
META_OBJECT_REPRESENTABILITY_UNPAID
```

## 6. Required successor

`GZ-012 / R4-CCTTMINI-REPRESENTABILITY-BOUNDARY-001` 必须明确测试下列命题是否有意义且可支付：

```text
对固定 Formula₁ 的 prov₁ syntax，
是否存在 object-level arithmetic semantics，使 prov₁(lit n)
与 meta-level ProvWitness n 在足够范围内相符？
```

先形成正／反候选与“不可循环”的来源合同，再决定是构造一个明确的项目定义 arithmetic model，还是记录
`REPRESENTABILITY_NOT_SOURCE_PAID_WITH_SCOPE`。即使项目定义模型成功，也只能证明该模型，不能把它称为
redtt/cctt/HoTT 或 bare ZFC 的实际 proof predicate。
