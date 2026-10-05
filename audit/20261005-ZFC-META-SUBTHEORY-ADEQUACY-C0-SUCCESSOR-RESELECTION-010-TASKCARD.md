# C0 successor reselection 010：非标准时间的 bare-ZFC subtraction screen

> **身份：** `CORE_ADEQUACY_TASK_CARD / ACTIVE_SUCCESSOR_SELECTION / NOT_A_MATHEMATICAL_RESULT`。
> **前序：** [C0R9 hybrid non-standard comparative control](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R9-HYBRID-NONSTANDARD-COMPARATIVE-CONTROL.md)。

## 目标

Benveniste et al. 2012 表明 `ZFC + non-standard-analysis axioms` 可以给混合系统一个明确的
temporal operational semantics。它不能自动支持 bare-ZFC insufficiency：一个 extension 的有用性不等于
其 base 无法构造、解释或选择同类对象。

本卡只检查这条 **subtraction**：

```text
对于 source 使用的 non-standard time / infinitesimal-step semantics，
bare ZFC 在哪一层被真正排除？

1. object-language ZFC unable to prove existence?
2. ZFC metatheory can construct a model but source's semantic consumer cannot use it?
3. source simply chooses a stronger/clearer interface without claiming necessity?
4. a required task/bridge is not preserved after returning to standard time?
```

## 最小判别行动

```text
C0R10-NSA-ZFC-SUBTRACTION-SCREEN

冻结 Benveniste paper's exact non-standard assumptions and construction claims；
再读一手非标准分析／模型来源，区分：
  ZFC construction/model existence,
  internal theory extension,
  executable hybrid-language semantics,
  standardization back to physical/simulation task.
```

## 必需 controls

- `RepresentabilityControl`：如果 ZFC 可以在元理论层构造同类 non-standard structure，这只反驳
  “不能表示”，不自动支付/否定 operational bridge。
- `ConsumerControl`：如果 hybrid semantics 仍需额外 axioms、language rules或standardization条件，
  记录它们，不把它们叫作 bare ZFC rule。
- `TaskControl`：program accept/reject、zero-crossing and simulation reproducibility不等于芝诺或圆环
  `OriginDone`。
- `BridgeControl`：从 non-standard run回到standard/physical signals的标准化必须有明确source payment。

## 停止与后继

| 结果 | 处置 |
|---|---|
| source proves bare-ZFC impossibility for required semantic bridge | 进入 C1--C5 same-contract qualification；不得仅凭术语。 |
| source provides ZFC construction/model but needs separate consumer rules | `REPRESENTABILITY_POSITIVE / OPERATIONAL_DUTY_UNPAID`，保留 comparative control。 |
| source only asserts extension convenience | `EXTENSION_CHOICE_WITHOUT_SUBTRACTION_PAYMENT`，关闭该 source leaf。 |
| standardization lacks task bridge | `STANDARDIZATION_BRIDGE_UNPAID`，转 source-local bridge screen，不称bare ZFC verdict。 |
