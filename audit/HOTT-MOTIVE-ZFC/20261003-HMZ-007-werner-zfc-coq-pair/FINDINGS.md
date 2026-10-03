# HMZ-007：有界发现

> **证据身份：** `SOURCE_REPORTED + SOURCE_INSPECTED_WITH_SCOPE + CONTROLLED_NO_CANDIDATE_SEED`。

## 1. 新增的真正信息

WoLLIC 的作者动机不再只有一句无法核查的比较。Werner 的论文和 archive 使一个具体任务可见：在 CIC/Coq 内用
`Ens`、`IN` 和 `EQ` 表示集合，并证明相应的 ZF/ZFC 公理。这个任务有真实的 formation 与 consumer，也有可定位的
成本：full ZFC 依赖 EM 与 TTDA/TTCA 等 non-computational Choice principles；历史代码在 Replacement 处直接写出其中的 choice 依赖。

## 2. 为什么它没有生成 Q

第一，Werner 的 `Ens` 是 **CIC 内的 set model**，不是 bare ZFC 自己的对象层。它能说明一种 proof-formalization
／model construction 如何工作，不能单独说明 ZFC 的 formation rule 在数学实践中把未形成对象交给算符。

第二，关键跨越已经被来源标为支付。用 Prop-level existential 建造 Replacement／Choice 所需 set 的困难没有被假装消失：论文和代码都加入非计算的 Choice／TTDA，并明确其作用。

第三，Russell 文件是反控制。它只从“有一个包含一切 `Ens` 的 U”推出矛盾；bounded `Comp U` 不会自己形成这个 U。
这与用户所说需要追问“对象在形成未落定时是否已被同一算符使用”不同。

第四，`Power` 不是所求 H0 对应。它由 host CIC 的 `sup`、`A → Prop` 与 impredicative Prop 形成；`EQ` 又是 Prop-level
extensional relation。高阶相同的 subject、逐层追问过程和 Done 都已改变，因此不能把它包装成 `H0→Z0`。

## 3. 当前判词

```text
SOURCE-SUPPORTED PAIRING: YES, but NOT_ATTRIBUTED_TO_VOEVODSKY
SOURCE-SUPPORTED PAYMENTS/GUARDS: YES
P-QUALIFIED ZFC Q: NO
POWER SET R-BRIDGE: NO
H0→Z0: ANTI_ANALOGY_CONTROL
```

这不是“ZFC 没有问题”的结论。它只使下一次检索更精确：必须找同一 ZFC-level task 中**支付仍不可见**的 consumer，或一条真正保真而非 CIC model 的 H0／Power Set bridge。
