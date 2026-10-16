# C0R8：MSS phase-space 表示与时间顺序的 source-to-spec 控制

> **身份：** `SOURCE_TO_SPEC_FIDELITY_CARD / P2_P3_CALIBRATION / NOT_A_CORE_CONTRACT`。
> **primary source：** da Costa--Sant'Anna `gr-qc/0102107v2`，PDF p.8 / printed p.8。
> **machine package：** `MP-ZFC-MSS-PHASE-ORDER-CONTROL-001` / `C-377`、`C-378`。

## 1. 原典支付的文本事实

源页依次做了四件不同的事：

1. 以 Padoa reasoning 将 MSS 的 `T` 说成由 position/forces 可定义；
2. 将 P7 称为 autonomous，意即不再以 `t` 作为 independent variable；
3. 说 prediction refers to future and therefore time；
4. 以 phase-space points 的 physical-state description重述 MSS 的主目标，并说明 phase
   space不引用参数 `t`。

它没有给出“无参数 state set 与原 prediction 同一”的 theorem，也没有定义芝诺、圆环或任何
process completion `OriginDone`。

## 2. 保真映射

| source expression | Lean object | 映射的保真点 | 没有声称的东西 |
|---|---|---|---|
| time parameter `t` in `s_p(t), f(p,q,t), g_p(t)` | `TemporalTrace := Bool → Bool` | 明确保留 stage-indexed state value | 不编码 real time、particle、force、differentiability。 |
| phase-space state points / a set of points | `RangeView := Bool × Bool` | 以 finite characteristic vector 表示 which state values occur | 不等同于论文的 full phase space、curve、oriented curve或 physical state。 |
| prediction/future vs description | `OrderedForward` | 固定一个最低限度的 order-sensitive observation：哪个 state是起点、哪个是终点 | 不把它等同于 prediction、causality或原过程完成。 |
| no reference to parameter in state-set view | `rangeView` | view只记录 membership，不记录 producing stage | 不称论文已实际实行此 exact projection。 |

## 3. 机器结果与控制

### C-377：parameter-preserving positive control

`temporalView` 为 identity。因此在 `TemporalTrace` 上有直接 decoder 判断
`OrderedForward`。这排除“只要有抽象表示，时间顺序就必然丢失”的过强说法。

### C-378：range-only negative control

`forwardTrace` 与 `reverseTrace` 的 range characteristic vector 相同，但前者满足
`OrderedForward`，后者不满足。kernel 因而证明不存在只由 `RangeView` 给出的统一 decoder。

这正是该 source phrase 需要面对的最低理论条件：如果一个实际 no-time representation
真的只保留 visited-state set，则不能自称还决定起点到终点的 time-order observation。

## 4. 当前判词

```text
SOURCE_TIME_PARAMETER_VS_STATE_DESCRIPTION_TENSION = SUPPORTED
FINITE_RANGE_ORDER_ERASURE_CONTROL                 = MACHINE_PROVED_WITH_SCOPE
MSS_PHASE_SET_IS_EXACT_RANGEVIEW                    = NOT_PROVED
PREDICTION_OR_ORIGINDONE_IS_ORDEREDFORWARD          = NOT_PROVED
ZFC_SPECIFIC_M_AND_ACTUAL_BRIDGE                    = NOT_PAID
C0_C1_TO_C6_ADMISSION                               = NOT_RELEASED
```

这张卡把“时间维度”从一个笼统词拆开：

```text
time carrier/domain          -- C-375 的 recovery control
time parameter/order         -- C-377/C-378 的 retention/loss control
physical prediction/task     -- 仍要求 source-defined consumer 和 bridge
```

因此它支持继续找 Q，但不允许把这个有限 model 直接读成 bare ZFC 的理论精度结论。

## 5. 反控制与后继

- 源文本中的 phase-space curve 可以携带比普通 state set 更多的结构；C-378 不能替代
  具体 curve semantics 审计；
- Definition 12 of the thermodynamics paper仍以 domain components保留 time；
- Earman--Norton 条件 Newtonian model 说明连续过程 completion可以有物理 bridge；
- 下一 source action须找实际 representation/consumer 的 order/prediction preservation theorem，或
  记录没有这种 bridge的有界范围；只有同一 M/S/Q/P/Adequacy到位才进入 C1--C5。
