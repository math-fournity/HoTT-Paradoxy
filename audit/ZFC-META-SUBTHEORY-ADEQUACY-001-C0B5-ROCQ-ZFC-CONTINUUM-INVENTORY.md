# C0B5：Rocq ZFC encoding 的连续统子理论盘点

> **身份：** `C0B_INDEPENDENT_FORMALIZATION_INVENTORY / BOUNDED_NEGATIVE / NOT_A_GLOBAL_ABSENCE_CLAIM`。
>
> **TaskCard：** [C0B5](ZFC-META-SUBTHEORY-ADEQUACY-001-C0B5-TASKCARD.md)。
>
> **frozen source：** `https://github.com/rocq-archive/zfc@ede7126560844c381c2b021003a8dbcb0668ecad`，只读clone `/private/tmp/c0b5-rocq-zfc-ede712`，commit timestamp 2022-12-17。
>
> **判词：** `ROCQ_ZFC_CORE_PRESENT_NO_ADMISSIBLE_CONTINUUM_S_WITH_SCOPE / C0B5_LOCAL_LEAF_CLOSED`。

## 1. 实际 source scope

README/description明确把该树定义为 Coq 中的 Zermelo–Fraenkel Set Theory encoding：`Ens`、membership/equality，且说明ZFC axioms在development中被证明为theorems。它还明确说明使用一个non-computational type-theoretic choice axiom来取得replacement和set-theoretic AC。

这使它成为一个有价值的**ZFC encoding**候选，但不是bare ZFC本身，也不能因其在Coq中可表达ZFC就自动支付物理或application-level adequacy。

## 2. 连续统 S 的有界盘点

冻结树含`Axioms.v`、`Sets.v`、`Replacement.v`、`Omega.v`、`Ordinal_theory.v`等；全文路径及内容检索覆盖：

```text
real / cauchy / dedekind / limit / continuous / derivative / series /
sequence / rational / natural
```

唯一相关的数学入口是 `Omega.v` 对自然数集合的处理。没有real-number construction、Cauchy/Dedekind reals、real sequence convergence、continuous function、derivative、geometric-series或runner/trajectory contract。因此它不能给本SOP提供S。

## 3. 判词范围

```text
ROCQ_ZFC_CORE_PRESENT_NO_ADMISSIBLE_CONTINUUM_S_WITH_SCOPE
```

这只关闭这一exact historical source revision的F-B continuum route。它不判断Coq、ZFC或所有Rocq libraries不能承载real analysis，也不重跑其历史Coq toolchain。

## 4. 自动后继

进入 **C0R3：F-B/F-C frontier reconciliation**。C0R3必须把已审的Mizar、Isabelle/ZF、Foundation、set.mm与Rocq candidates按“是否支付M→S / Q / P / Bridge”重排；若F-B的freeze denominator达到remainder zero，转F-C寻找actual foundation-facing adequacy source；否则新candidate必须明确为什么能支付此前未付的字段。
