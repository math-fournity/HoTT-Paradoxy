# GZ-007：R4 exact cubical derivation source 分诊

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G1-R4`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / GZ-008_SUCCESSOR_REQUIRED`。

## 1. Parent gap

GZ-006 在 cctt 的冻结 source 中没有得到可用于 Gödel技术的 finite derivation/proof-code
relation。该局部 source gap 不能被“换一个实现再跑些 Nat/Path 测试”掩盖。GZ-007 的任务是找出
并资格化一个**不同的、版本固定的 cubical/HoTT source denominator**，它有机会支付 object-level
derivation 与有效性义务。

## 2. 先于候选检索的资格标准

候选要进入实际 source qualification，至少需要所有前四项：

| Gate | 必须有的 source evidence | 不可替代物 |
|---|---|---|
| `D1` | explicit raw syntax / context / term / type 的 data 或 formal grammar | 只给语义范畴、模型对象或 API 名称 |
| `D2` | judgement 或 derivation relation，或输入为 finite code 的明确 type/proof checker | 普通 elaborator 过程、CLI exit、单个 theorem statement |
| `D3` | code/decoding、finite certificate 或可枚举 relation 的明确接口 | source text、`Show`、无关系的 serializer |
| `D4` | source-level termination/effectivity theorem，或明确可验证的 total fragment与边界 | 一次 run、某个 input 很快、没有观察到 timeout |
| `D5` | Nat 与 Path/identity rule 同时被该 relation 覆盖 | 只含 Nat 或只含 equality 的弱 calculus |
| `D6` | univalence/HIT 若被宣传为必要机制，须在同一 relation 中定位 | 另一个 repo 的 cubical feature list |

任何候选在 `D1`--`D4` 任一处失败，都只能作为 scope-limited control。GZ-007 不会为了让
候选通过而把 GZ-005 的 project profile、外部 Haskell code 或 Foundation 一阶算术 theorem 嵌入其中。

## 3. 反控制与停止条件

- 纯 cubical model、presheaf semantics、relative consistency proof，若没有 finite derivation relation，判为 `MODEL_NOT_DERIVATION_CONTROL`；
- proof assistant 实现，若只有 host checker 而无对象层 proof-code，判为 `IMPLEMENTATION_NOT_DERIVATION_CONTROL`；
- formalized syntax，若缺 Nat/Path 或 effectivity，判为 `WEAK_OR_INEFFECTIVE_CALCULUS_CONTROL`；
- 只有一个固定候选的 source tree、version、D1--D6 表与正反控制都收齐，才可 local close；之后必须选择不同 target 或回到另一 READY route。

本文件现阶段只冻结检索标准；不代表已经找到候选，更不代表 R4、HoTT 或 bare ZFC 有任何新的数学结论。

## 4. 冻结候选池与资格化结果

### 4.1 `dlicata335/cart-cube`

```text
source: https://github.com/dlicata335/cart-cube
commit: f80af5cf6638c85ffda2397a8e097b3e9decac1b
denominator: 63 agda files under agda/ + README
```

该 repo 的 README 明确说 `agda/` 是与发表论文 *Syntax and models of Cartesian
Cubical Type Theory* 对应的完整 Agda formalization；`ABCFHL.agda` 导入 `Nat`、`Path`、
`Glue`、universe 和 `Univalence`。`universe/Nat.agda`、`universe/Path.agda` 的 `Nat-code`
与 `Path-code` 是**模型 universe 中的 codes**，不是有限语法或 proof codes。

对 63 个 Agda 源文件检索 `Ctx/Context/Tm/Term/Ty/Type/Deriv/Judg/Proof` 的 data/record
declaration，结果为零个 matching raw-syntax declaration。`Kan.agda` 的中心对象是
`Set`-valued fibrations、`relCom`、`hasCom`；它是语义模型和 Kan operation 的 formalization。

| Gate | verdict | 理由 |
|---|---|---|
| D1--D3 | `MODEL_NOT_DERIVATION_CONTROL` | 没有现成 raw term/context/derivation code relation。 |
| D4 | `NOT_APPLICABLE_TO_PROOF_CODE` | README 指向 Agda 2.6.1.2；当前 host 无 `agda`。即使旧 formalization 可重放，也不能把 semantic model 的 typechecking 改写为 proof-code checker。 |
| D5--D6 | `SEMANTIC_FEATURES_PRESENT` | Nat、Path、Glue、univalence 的模型性质确实由 source 明示。 |

### 4.2 `RedPRL/redtt`

```text
source: https://github.com/RedPRL/redtt
commit: ae76658873a647eb43d8cf84365a9d68e9a3273c
denominator: 102 OCaml source/interface/grammar files under src/ + README/library
```

这是比 cctt 更丰富的 Cartesian cubical core language。`TmData.ml` 给出 raw term functor；
`Typing.mli` 中的 `check` 与 `infer` 是 actual checking interfaces；library 中有 `data nat`、
path definitions、univalent universes 和 parametric HITs 的 source assets。

但 `Typing.check` 的类型是 `cx -> value -> Tm.tm -> unit`，由 exception/control flow 表示失败；
它不输出 derivation certificate。102 个 source/interface/grammar 文件中没有符合 `Deriv`、`Proof` 或
`Judg` 的 declaration。`RotIO` 的 encode/serialization 是 interactive resolver state 资产，不是
`Proof_T(p,q)`。当前 host 也没有 OCaml/Dune build lane。

| Gate | verdict | 理由 |
|---|---|---|
| D1 | `PRESENT_SOURCE_REPORTED` | `TmData`/grammar 给 raw syntax。 |
| D2 | `IMPLEMENTATION_NOT_DERIVATION_CONTROL` | executable type checking exists, but returns unit/errors, not a proof certificate relation. |
| D3--D4 | `UNPAID_WITH_SCOPE` | no derivation-code/enumerator or totality theorem in fixed source denominator; missing local OCaml/Dune blocks a fresh run but source gap already prevents payment. |
| D5--D6 | `FEATURES_PRESENT_SOURCE_REPORTED` | Nat/path/univalent universes/HIT features are source-located; this does not repair D3--D4. |

### 4.3 `L-TChen/TTasQIIRT`

```text
source: https://github.com/L-TChen/TTasQIIRT
commit: 8db08306287333067b2749f95f8ad3ba7a0e14d1
denominator: 30 Theory/*.agda modules + README/index
```

TTasQIIRT is the strongest intrinsic-syntax control in this triage. Its `Syntax.agda` explicitly
declares `Ctx`、`Sub`、`Ty`、`Tm` and their QIIRT constructors, with intrinsic `tyOf` and
substitution equations. This is genuine formal syntax, not a host elaborator. It also contains
`encode/decode` constructions, but those encode **paths/equalities of contexts** into a `Cover`
object; they are not a natural-number coding of syntax/derivations or an enumerable proof relation.

The README fixes its three object theories as SC, SC+Π+Bool and SC+El+Π+Bool. A complete search
of `src/Theory` finds no object-language Nat constructor, Path/identity constructor, Glue or
univalence rule. Cubical paths occur in the Agda metatheory/library, so they cannot be promoted to
the object's identity rule. The local host has no `agda` binary; that preserves a separate replay
gap rather than changing the feature verdict.

| Gate | verdict | 理由 |
|---|---|---|
| D1 | `PRESENT_SOURCE_REPORTED` | intrinsically typed QIIRT syntax. |
| D2 | `INTRINSIC_WELLFORMEDNESS_NOT_DERIVATION_CERTIFICATE` | typed constructors encode formation, but no separate finite proof certificate relation is supplied. |
| D3--D4 | `UNPAID_WITH_SCOPE` | equality `encode/decode` is not syntactic Gödel coding; no numeric/enumerable checker or effectivity theorem is located. |
| D5--D6 | `WEAK_CALCULUS_CONTROL` | object theory lacks Nat + Path/identity and deliberately avoids Glue/univalence. |

## 5. Triage verdict

```text
THREE_SOURCE_TRIAGE_COMPLETED_WITH_SCOPE
SEMANTIC_MODEL_NOT_DERIVATION_CONTROL: cart-cube
IMPLEMENTATION_NOT_DERIVATION_CONTROL: redtt
INTRINSIC_SYNTAX_BUT_WEAK_CALCULUS_CONTROL: TTasQIIRT
NO_SINGLE_SOURCE_IN_THIS_FROZEN_POOL_PAYS_D1_TO_D6
```

这不是对所有 cubical theories、所有 formalizations 或所有未来版本的负结论。它也不说
Gödel式 R4 bridge 不存在。它只说明：在这三种分别最有希望的 source 形态中，不能偷偷把
semantic universe code、implementation source text 或 intrinsic well-formed constructor 当成
`Proof_T(p,q)`。

## 6. Required successor

`GZ-008 / R4-SOURCE-CORRESPONDING-CUBICAL-PROOF-CODE-FRAGMENT-001`：不再把不同 source
拼接成一个虚构的完整 calculus。它要设计一个**明确标为项目定义、source-corresponding fragment**的
最小对象：有限 syntax、Nat、Path/refl、typed derivation certificate、structural checker 和代码域；并逐字段
标注它与 redtt/cctt source 的 syntax correspondence、与 cart-cube 的 semantic feature correspondence、以及
未覆盖 univalence/HIT/完整 cubical composition 的部分。

该 fragment 若机器化成功，只能形成 `HOTT_GODEL_BRIDGE_FRAGMENT_MACHINE_PROVED`；它不能自动成为
exact Cubical Agda H0、full HoTT 或 bare ZFC 的实例。随后仍需用 source-preserving map 逐步扩展，或找到
新 source 满足 D1--D6。

## 7. Reopen conditions

GZ-007 在以下条件重开：找到一个版本固定 source 同时支付 D1--D4 和 object Nat/Path；cart-cube 给出另一个
raw-syntax companion；redtt 提供 formal derivation/checker theorem；或 TTasQIIRT 新增 object identity/Nat/
univalence theory并给出可编码 proof relation。
