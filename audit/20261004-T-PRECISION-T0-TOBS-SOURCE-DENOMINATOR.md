# T-PRECISION T0：T-OBS-001 来源与开源代码分母

> **关联卡：** T0 抽象观察边界冻结卡。
>
> **状态：** SOURCE_ADMISSION_PASS / C-367_MACHINE_PROVED_WITH_SCOPE。
>
> **读取日期：** 2026-10-04。
>
> **范围：** 本文只核验 T-OBS-001 所需的数学背景和 Lean 实现接口；不把 quotient/factorization 文献归因于想法 T、bare ZFC、HoTT、芝诺或任何现实过程。

## 1. 来源分母

| ID | 身份 | 固定材料 | 支持什么 | 不支持什么 |
|---|---|---|---|---|
| S1 | 一手基础文本 | Univalent Foundations Program, Homotopy Type Theory: Univalent Foundations of Mathematics, §6.10，Lemma 6.10.3，在线 PDF 第 211 页 | 集合商的 universal property：由商映射预合成的函数，等价于在 relation 上保持相等的原函数 | 不支持任意观察接口、bare ZFC、完成谓词或现实解释 |
| S2 | 固定开源核心实现 | Lean 4.34.1 core，commit 5045d0056413266e57c625dcd7c365b10e377c52，Init/Core.lean 1918--1991，SHA-256 6218a9825a0ce51a6bbe3949ec7a86c4406f4f216bd3cd1262736cfc1c997c54 | Quotient.lift 要求被提升函数 respect quotient relation；提供本机 proof kernel 的实际基础接口 | 不证明 T-OBS-001，亦不表示项目使用了 quotient |
| S3 | 开源数学库语料 | leanprover-community/mathlib4 的公开源树与自动生成文档 | Mathlib 是 Lean 4 的公开数学库；可作为后续比较 quotient/factorization API 的来源 | 本轮没有固定或运行 Mathlib；不得写成 Mathlib replay |
| S4 | 项目校准 | C-364 / MP-BARE-ZFC-Q-PRECISION-001 | 固定两世界 completion-contract interface 上，coarse view 不决定 OriginDone，rich view 可决定 | 不等于 T-OBS 的一般命题，也不等于 bare ZFC 结论 |

## 2. 一手数学来源的精确读取

HoTT Book §6.10 将 set-quotient 写成 relation 的 coequalizer。Lemma 6.10.3 说明：对任意 set B，经 q 预合成得到的函数，与满足 relation-respect 条件的函数相对应；其反向构造就是 quotient 的 recursion principle。

这与 T-OBS-001 的关系只是一条受限的数学启发：

~~~text
若某观察 π 把 x、y 压到同一输出，
而判词 D 在 x、y 上有相反真值，
则任何让 D 只由 π 输出决定的 decoder
都会把相同输出要求为同时支持相反判词。
~~~

这是一种“factor through observation”的反例。它不依赖 HoTT Book 的 set-quotient、univalence、HIT 或 truncation；本轮 Lean 证明故意选择更小的 Function/Prop fragment。

## 3. 开源代码核验

本机固定 Lean core 的 Init/Core.lean 明确写道：

- quotient 上的函数必须证明它 respect setoid relation；
- Quotient.lift 由该 respect 条件定义；
- Quotient.ind 提供从 representatives 推理 quotient 的原则。

本轮不使用 Quotient.lift，因为 T-OBS-001 的 Determines π D 直接把“存在 decoder”作为命题。选择较小 fragment 的原因是避免把 quotient 实现或任何额外公理误写成 T 的必要条件。

Lean binary identity：

~~~text
Lean 4.34.1
commit 5045d0056413266e57c625dcd7c365b10e377c52
binary SHA-256 1b370cfcbf44e80d1b004ab1b1ab9a4c73951f9f7c242140bcff9bc577576554
~~~

## 4. 结论与下一动作

SOURCE_ADMISSION_PASS_FOR_ABSTRACT_FACTORISATION：

1. S1 支持 factorization/respect-relation 的标准数学背景；
2. S2 支持本机 Lean core 有与该背景一致的 quotient-lift 设计；
3. S4 给出项目内 concrete control；
4. 没有一项来源把 T-OBS-001 变成“理论抽象必然导致悖论”或具体 ZFC 诊断。

下一动作可以是构造一个不导入 Mathlib 的 Lean core proof package，包含：

- 一般 collision-to-no-decoder 定理；
- Bool 到 Unit 的 concrete collision；
- identity/rich-view 正控制；
- 对伪 decoder 的 expected-negative rejection；
- 完整 run receipt、claim-index 与版本闭合。

该动作已经完成为 MP-T-PRECISION-TOBS-001 / C-367。primary run 是 20261004-MP-T-PRECISION-TOBS-001-06；它使用本卡锁定的 source denominator，但没有把 S1--S3 的外部文本变成 Lean 公理。

## 5. 来源链接

- HoTT Book PDF §6.10：<https://homotopytypetheory.org/wp-content/uploads/2013/03/hott-online-611-ga1a258c.pdf>
- Lean core source（当前公开 branch，版本固定读取另见 S2）：<https://github.com/leanprover/lean4/blob/master/src/Init/Core.lean>
- Mathlib source：<https://github.com/leanprover-community/mathlib4>
