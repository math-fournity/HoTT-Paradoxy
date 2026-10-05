# G0/G2：Flypitch 的 ZFC proof-relation source 卡

> **方案：** `GODEL-Q-REFLECTION-SOP`。
>
> **身份：** `SOURCE_INSPECTED_WITH_SCOPE / META_LEVEL_ZFC_PROOF_RELATION / SOURCE_REPORTED_FORMAL_THEOREM / NOT_A_GODEL_FIXED_POINT`。

> **判词：** `ZFC_PROOF_TREE_AND_SUBSTITUTION_SOURCE_PRESENT / NATURAL_NUMBER_GODELIZATION_NOT_SUPPLIED / PARENT_COMPLETION_BRIDGE_UNPAID`。

## 1. 固定 source

| 字段 | 冻结值 |
|---|---|
| repository | `https://github.com/flypitch/flypitch` |
| commit | `d72904c17fbb874f01ffe168667ba12663a7b853` |
| source toolchain | Lean `3.4.2`；mathlib `883d974b608845bad30ae19e27e33c285200bf84` |
| primary sources | [repository README](https://github.com/flypitch/flypitch/tree/d72904c17fbb874f01ffe168667ba12663a7b853)、[CPP 2020 paper](https://flypitch.github.io/assets/flypitch-cpp.pdf) |
| direct source files | `src/fol.lean`、`src/ZFC.lean`、`src/summary.lean` |

本轮 checkout 哈希：`README.org`=`705a671d83fa64b413a152b1aeb4c8892fcb38ba56ea4f4b7ed25a4bcd3076ff`、`leanpkg.toml`=`2611e2f2421cf9df4720fb72ed36679f50d4d56779d835691b951206fb74a1e3`、`fol.lean`=`d20616abfef8fc19399d6178664f90c72207906cce5301ca1ca0c4dc330a7fa4`、`ZFC.lean`=`4b8bd04ab47c5ef949a879a7f67a161f95f099946c6a90eff3833a6937f53f8b`、`summary.lean`=`89e1480641bb27c613ff11f508527b0656eef71e5c33d8f0795aa47e12350dbb`。

## 2. 该 source 真正给出的对象

Flypitch README 和源码共同固定以下 M 层对象：

```text
ZFC : Theory L
fol.prf Γ f : Type           -- proof tree
T ⊢' f := Nonempty (T ⊢ f)  -- provability relation
substitution / substitution' -- formulae and proofs under substitution
independence_of_CH : independent ZFC CH_f
```

其中 `src/summary.lean` 将 `independent` 定义为 `¬ T ⊢' f ∧ ¬ T ⊢' ∼f`，并报告 `independence_of_CH`。`src/ZFC.lean` 直接含 `CH_f_unprovable` 和 `neg_CH_f_unprovable`；`src/fol.lean`定义 proof-tree relation、formula substitution 和 proof substitution。

这比“有一个字符串 checker”更接近 G2 所需的形式对象：它明确展示一个版本固定的 ZFC first-order theory 与其 proof relation 可以在 M 中被深嵌入并参与真实数学 theorem。

## 3. 它没有支付的义务

| 项 | 状态 | 原因 |
|---|---|---|
| exact source replay | `NOT_RUN` | source要求 Lean 3.4.2 和 pinned mathlib；本机没有 Lean 3 toolchain 或 source mathlib checkout。 |
| source theorem 的当前本机 kernel 复验 | `NOT_RUN` | README 的 `lean --trust=0 ./src/summary.lean` 是 source-declared command，未在本机完成。 |
| `Code : Formula/Proof → Nat` | `NOT_SUPPLIED_BY_SELECTED_FILES` | 深嵌入语法与 substitution 不等于 Gödel numbering。 |
| `Prov_T` 的 T 内算术表示 | `NOT_PAID` | `T ⊢' f` 是 Lean M 层 relation；未显示为 ZFC 内 predicate。 |
| diagonal / quotation / fixed point | `NOT_PAID` | CH independence/forcing 不等于 Gödel self-reference theorem。 |
| parent `OriginDone`、`ρ`、bridge | `NOT_APPLICABLE_TO_THIS_SOURCE` | 该 source 的 consumer 是 formal ZFC proof relation 与 CH statement，不是 Zeno/circle/H0 completion task。 |

### 3.1 `reflect`、`substitution` 与 `godel` 名称的精确去歧义

后续对该 exact source 做的 source scan 不能改变上表，却排除了三种很容易发生的错误读法。完整逐项结果见 [source-scan](20261004-GODEL-Q-REFLECTION-G0-FLYPITCH-ZFC-PROOF-RELATION/source-scan.md)：

- `reflect_prf_lift1` 是从 lifted formula proof 回到原 formula proof 的**宿主 proof transport**；它不是一个 `Prov_ZFC` 谓词、反射 schema 或 fixed-point construction。
- `parse_formula.lean` 的 `has_reflect` 是 Lean meta elaboration 的 reification helper；它没有把 ZFC formula quote 成 ZFC 内自然数。
- source 中名为 `godel_completeness_theorem` 的 theorem 是语义 completeness `T ⊢' ψ ↔ T ⊨ ψ`；它不是 Gödel 不完备性或自指。

因此这张卡的最高资格仍是 `META_LEVEL_ZFC_PROOF_RELATION_SOURCE_PRESENT`。名称相同或均含“reflect”不能替代 G2 所要求的 numeric code、T 内 provability、quote、substitution on codes 和 fixed point。

## 4. 对 G0/G2 的作用

Flypitch 使 G0 的 formal side 不再只有 `set.mm` database 和 external verifier：它额外提供一个公开、深嵌入的 ZFC proof relation、substitution operation 和 source-reported machine theorem。这是 **G2 syntax/proof-relation source baseline**。

但它不能改变当前主判词：

```text
META_LEVEL_ZFC_PROOF_RELATION_SOURCE_PRESENT
NO_T_INTERNAL_GODELIZATION_PAYMENT
PARENT_COMPLETION_ACCEPTANCE_INTERFACE_UNDERDETERMINED_WITH_SCOPE
```

因此它不释放 G2 full payment，更不释放 G1/G3/G4 或 parent-Q chain。它的下一价值是：如果未来找到同一 source owner 的 `OriginDone`/bridge，Flypitch 可作为比较“proof relation是否真的已进入对象理论”的精确反控制。
