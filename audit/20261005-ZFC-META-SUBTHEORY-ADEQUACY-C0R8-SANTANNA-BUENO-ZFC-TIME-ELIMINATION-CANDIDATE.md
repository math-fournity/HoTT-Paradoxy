# C0R8：ZFC 中 MSS time eliminability 是 P 的候选位置，也是反误报控制

> **身份：** `ZFC_SOURCE_CANDIDATE / P_CAPABILITY_CALIBRATION / SOURCE_TO_SPEC_CONTROL_COMPLETE / REAL_CONSUMER_SEED_FOUND / Q_NOT_YET_LOCATED`。
>
> **来源：** [Sant’Anna–Bueno 2014 snapshot](../sources/external/zfc-meta-subtheory-c0r8-santanna-bueno-2014-20261005/README.md)，以及其引用的 [da Costa–Sant'Anna 2001 primary snapshots](../sources/external/zfc-meta-subtheory-c0r8-dacosta-santanna-2001-20261005/README.md)。

## 1. 为什么这是一个真实的 ZFC 候选位置

这不是从“ZFC 里没有时间”猜出来的位置。论文在 ZFC 中首先给出 McKinsey–Sugar–Suppes (MSS) classical particle mechanics：

```text
P = particles
T = real numbers measuring elapsed time from an origin
s(p,t) = physical position of p at instant t
f(p,q,t), g(p,t) = forces at instant t
```

随后论文的 Theorem 8 说：`Time is eliminable in a MSS system`。理由是 `s,f,g` 的定义域依赖 `T`；不能改变 `T` 而不改变这些函数，所以 `T` 可定义，进而可在重述中不显式出现。

这正好位于研究发起人所问的高价值位置：**一个 ZFC-based physical formalization 对时间作了理论经济性处理。**

## 2. `T/u/F/C/Q/I/O/Done` 冻结

| 字段 | 当前 source card |
|---|---|
| `T` | ZFC（论文明确先在 ZFC 中表示 MSS）及其 set-theoretic function/domain conception。 |
| `u` | physical elapsed time `T`，以及 position/force的时间化输入。 |
| `F` | `s,f,g` 作为函数；其 domain 包含/依赖 `T`。 |
| `C` | Padoa definability：time 若不独立于其余 primitives则可定义、可 eliminable。 |
| `I` | 物理 particles、elapsed times、position-at-instant、internal/external forces。 |
| `O` | source给出的模型／函数域／real interval与物理解释。 |
| `Done` | source只证明“可在重述中不显式提 time”；尚**未**给用户的 process completion `OriginDone`。 |

## 3. P1/P2/P3 的初步卡位

### P1：位置

候选位置是 **ZFC 内物理理论的 primitive-concept elimination**，不是 ZFC 的空泛 universe 或“时间不存在”断言。其 2001 MSS companion source 已把 prediction/future/time 与 phase-space physical-state description并列；其 thermodynamics companion source 又将 no-explicit-time formulation与“not very operational”的 practical qualification并列。它因此有 actual consumer seed，但尚未显示 formation/reentry pressure，也未固定用户的 process-Q。

### P2：逻辑翻译

论文的逻辑形式是：

```text
T is not independent of s,f,g
because changing T changes the interpretation of their domains
⇒ T is definable
⇒ T is eliminable in the explicit presentation.
```

这是一种 definitional elimination，不是已经证明 `T` 的所有结构、顺序或物理作用消失。

### P3：构造／过程检查

当前最强 **positive control** 是 source 自己的恢复条件：`T` 可由 `s,f,g` 的 domains 定义。若过程的时间顺序、阶段或边界仍可从这些 domains和real interval结构重建，那么“时间被省掉”没有构成过程信息的遗失。

这项控制已经进入 `MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001`：最小 graph/domain
representation 机器证明 endpoint membership 可由 graph domain 恢复。它是
source-motivated representation control，不是 MSS/ZFC 形式化重放。

另一方面，论文 p.274 明说 N-MSS 与 ZFC-MSS 不完全等价，因为 N 的 functions 没有 domains。
同一机器包构造 function-only 的两实例控制：相同 function view 可以对应不同 endpoint membership，
所以真正被丢掉 designated time carrier 时，endpoint observation 不再由该 view 决定。这不是 full N-MSS
model，也不证明 N 的物理错误；它只把 P 的追问精确到“carrier 是否保留”。

当前缺口已被收紧：来源确实指定了 operational/practical consumer，但还没有固定一个与用户 Zeno／圆环原任务相同的 `Q`、`OriginDone`，也没有证明该 consumer 在 ZFC-MSS retained data中不可恢复。MSS source的 prediction→state-description 是 source-side goal reframing；thermodynamics source的“不很具操作性”没有给出可机器化的 task/Done predicate。因此 `TimeEliminable` 仍只能是 `P_CAPABILITY_CALIBRATION`，不能是 Q。

## 4. 当前判词

```text
ZFC_TIME_ELIMINATION_SITE = SOURCE_SUPPORTED
TIME_AS_PRIMITIVE = ELIMINABLE_IN_FIXED_MSS_SYSTEM
ZFC_GRAPH_DOMAIN_ENDPOINT_OBSERVATION = MACHINE_PRESERVED_WITH_SCOPE
DOMAINLESS_FUNCTION_ENDPOINT_OBSERVATION = MACHINE_NONDETERMINATE_WITH_SCOPE
MSS_PHASE_RANGE_ORDER_OBSERVATION = MACHINE_NONDETERMINATE_WITH_SCOPE
REAL_OPERATIONAL_CONSUMER = SOURCE_SUPPORTED_WITHOUT_FIXED_Q
TIME_AS_PROCESS_OBSERVATION = NOT_YET_SHOWN_LOST_FOR_A_REAL_MSS_CONSUMER
Q_STATUS = Q_GENERATE_CANDIDATE / NOT_YET_Q_NARROWED
NAIVE_TIME_ABSENCE_INFERENCE = REJECTED_BY_DOMAIN_RECOVERY_CONTROL
```

这同时回应研究发起人的精确表述：bare ZFC 的问题如果存在，更可能是对时间相关任务的**观察/判断不完备**，而不是不能写出 time、sequence或trajectory。这个来源确实能写出它们；因此它替我们排掉“语言缺失”这一过强路线。

## 5. 接下来可检验的两条路线

1. **已完成的保真重述与顺序控制：**最小 graph/domain fragment 的 `T = domain` 机制已在 C-375 机器化；对固定 endpoint observation，保留 domain 的显式-time elimination 是正控制。并行的 domainless projection C-376 说明，真正缺少 carrier 时才有 observation loss。2001 MSS 的 phase-space phrase还启发 C-377/C-378：保留 parameterized trace可决定固定 start/end order，而只保留 visited-state range则不能。精确 source-to-spec 比对见 [domain control](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-DOMAIN-ELIMINATION-SOURCE-TO-SPEC-CONTROL.md)、[phase-order control](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-MSS-PHASE-ORDER-SOURCE-TO-SPEC-CONTROL.md) 与 [real consumer screen](20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-DACOSTA-SANTANNA-REAL-CONSUMER-SCREEN.md)。
2. **下一 source route：**只寻找一个 version-fixed source，使 ZFC-specific或明确 ZFC-founded physical model、一个具体 operational/prediction/process task、以及 order/endpoint/Done preservation的 bridge 在同一合同中出现。只有这一项命中才能进入 P2/P3、P-DAG或 Q-qualification。

## 6. 禁止外推

- Theorem 8 是来源报告，不是本项目已经重放的 ZFC machine proof；
- `Time is eliminable` 不等于 physical time is unreal、unobservable或不存在；
- MSS不完整涵盖 Newtonian mechanics，source自己承认这一点；
- 不把 N 语言的 domainless-function proposal与 ZFC 内 MSS消去混为同一理论；
- 不把本卡说成 ZFC 发现、Zeno解决/未解决、HoTT同Q或 bare ZFC 矛盾。
