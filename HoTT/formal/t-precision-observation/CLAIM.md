# T-OBS-001：抽象观察因子化边界

> **证明包：** MP-T-PRECISION-TOBS-001。
>
> **Claim：** C-367。
>
> **身份：** ABSTRACT_OBSERVATION_BOUNDARY_MACHINE_PROVED_WITH_SCOPE。

## 精确形式命题

给定 World、View、project : World → View 与 observe : World → Prop，定义：

~~~text
Determines(project, observe)
  := 存在 decode : View → Prop，
     对每个 world，observe(world) 当且仅当 decode(project(world))。
~~~

Lean core 证明：

~~~text
若 project(x) = project(y)，observe(x) 成立且 observe(y) 不成立，
则不存在 Determines(project, observe)。
~~~

同一源码还给出：

1. identity observation 总能决定任意 observe；
2. 在有限 TinyWorld 中，constant coarse observation 不决定 taskDone；
3. 保留 TinyWorld 自身的 rich observation 决定同一 taskDone。

## 来源层

HoTT Book §6.10 Lemma 6.10.3 说明 quotient 的函数提升需要 relation-respect 条件。Lean 4 core Init/Core.lean 的 Quotient.lift 也要求同一条件。它们支持本包的 factorization 背景。

它们不证明本包的具体 general theorem；该 theorem 的证明由 ObservationPrecision.lean 的 Lean core kernel run 提供。项目内 C-364 是有限 completion-contract instance，不是 C-367 的来源证明。

## 禁止外推

C-367 不证明：

- 某个具体理论缺失时间维度；
- bare ZFC、HoTT 或极限理论有缺陷；
- 任何现实过程或 OriginDone 已被唯一冻结；
- 抽象观察边界自动产生自指、对角化或哥德尔不完备性；
- 一个有限 Bool control 覆盖所有理论或所有判词。

它只给 T-OBS 一个可以机器检查的精确语言：针对指定 project 与指定 observe，存在同纤维异判词见证时，observe 不能只经 project 全域决定。
