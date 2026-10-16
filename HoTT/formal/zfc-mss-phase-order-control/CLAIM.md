# `MP-ZFC-MSS-PHASE-ORDER-CONTROL-001`：精确主张与边界

## C-377：参数化轨迹的顺序观察正控制

```lean
theorem temporal_view_determines_ordered_forward :
    Determines temporalView OrderedForward
```

`temporalView` 保留全部 `Bool → Bool` trace，所以 decoder 直接使用
`OrderedForward`。这证明特定 order observation 在保留参数化时可恢复。

## C-378：state-range 投影不决定时间方向

```lean
theorem range_view_does_not_determine_ordered_forward :
    ¬ Determines rangeView OrderedForward
```

固定 witnesses：

```text
forwardTrace(false)=false, forwardTrace(true)=true
reverseTrace(false)=true,  reverseTrace(true)=false
rangeView(forwardTrace)=rangeView(reverseTrace)
OrderedForward(forwardTrace)
¬ OrderedForward(reverseTrace)
```

因此，不存在一个仅见 `RangeView` 的统一 decoder 能决定这个 order-sensitive
observation。

## Source-to-spec status

来源确实讨论 MSS、prediction/future/time 与 phase-space point description；本包只
以它为动机，明示地构造一个有限 representation control。没有把文中的 phase-space
objects强行等同于 `RangeView`。

## 禁止外推

- 不形式化或重放 ZFC、MSS、Padoa、Theorem 5/6；
- 不证明 actual phase-space curve 无法保留 parameter/order；
- 不证明任何物理运动、Zeno 或圆环原任务不完成；
- 不证明 bare ZFC 理论精度不足、object-language inconsistency 或 community policy；
- 不证明同一 Q 与 HoTT H0。
